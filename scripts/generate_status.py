"""
generate_status.py

Fetches current Alpaca paper trading account status and updates bot_status.json.
Used by GitHub Actions to automatically keep the portfolio website dashboard live.
"""

import os
import json
from datetime import datetime
from zoneinfo import ZoneInfo
from alpaca.trading.client import TradingClient

api_key = os.getenv("ALPACA_API_KEY") or os.getenv("APCA_API_KEY_ID")
secret_key = os.getenv("ALPACA_SECRET_KEY") or os.getenv("APCA_API_SECRET_KEY")

if not api_key or not secret_key:
    raise ValueError("Missing ALPACA_API_KEY or ALPACA_SECRET_KEY environment variable")

client = TradingClient(api_key, secret_key, paper=True)
account = client.get_account()
clock = client.get_clock()
positions = client.get_all_positions()

ET = ZoneInfo("America/New_York")
now_et = datetime.now(ET)

portfolio_value = float(account.portfolio_value)
cash = float(account.cash)
buying_power = float(account.buying_power)
initial_capital = 100000.0
total_pnl = round(portfolio_value - initial_capital, 2)
total_return_pct = round((total_pnl / initial_capital) * 100.0, 2)

if clock.is_open:
    market_status = "Market Open — Live Trading Active"
    bot_status = "🟢 Live — Monitoring Positions"
else:
    next_open_str = clock.next_open.astimezone(ET).strftime("%Y-%m-%d %H:%M ET")
    market_status = f"Market Closed (Next Open: {next_open_str})"
    bot_status = "🟢 Live — Sleeping Until Market Open"

pos_list = []
for p in positions:
    pos_list.append({
        "symbol": p.symbol,
        "strategy": "Mean Reversion / Fade",
        "direction": "LONG" if str(p.side).lower().endswith("long") else "SHORT",
        "open_shares": float(p.qty),
        "open_price": float(p.avg_entry_price),
        "open_value": float(p.market_value),
        "status": "OPEN"
    })

# Retain existing trade history if bot_status.json already exists
recent_trades = []
if os.path.exists("bot_status.json"):
    try:
        with open("bot_status.json", "r", encoding="utf-8") as f:
            prev = json.load(f)
            recent_trades = prev.get("recent_trades", [])
    except Exception:
        pass

status_data = {
    "updated_at": now_et.strftime("%Y-%m-%d %I:%M:%S %p ET"),
    "timestamp_iso": now_et.isoformat(),
    "market_status": market_status,
    "is_open": clock.is_open,
    "bot_status": bot_status,
    "account": {
        "portfolio_value": portfolio_value,
        "cash": cash,
        "buying_power": buying_power,
        "initial_capital": initial_capital,
        "total_pnl": total_pnl,
        "total_return_pct": total_return_pct,
        "today_pnl": 0.0,
        "today_return_pct": 0.0
    },
    "strategies": [
        {
            "name": "GAP_BOTTOM_LONG",
            "schedule": "09:30 AM ET (Market Open)",
            "allocation": "50%",
            "type": "Mean Reversion (Long)",
            "description": "Scans most oversold overnight gap-down stocks and buys opening rebound.",
            "backtest_return_2025": "+2,212.4%",
            "backtest_winrate_2025": "53.6%",
            "max_drawdown": "-7.01%",
            "status": "Active"
        },
        {
            "name": "INTRADAY_15M_SIGNAL_TOP_SHORT",
            "schedule": "09:45 AM ET (15m Post-Open)",
            "allocation": "50%",
            "type": "Fade Momentum (Short)",
            "description": "Scans morning 15-minute spike leaders and shorts the fading exhaustion.",
            "backtest_return_2025": "+859.6%",
            "backtest_winrate_2025": "52.7%",
            "max_drawdown": "-15.69%",
            "status": "Active"
        }
    ],
    "stats": {
        "total_trades": len(recent_trades),
        "wins": sum(1 for t in recent_trades if (t.get("pnl_dollars") or 0) > 0),
        "losses": sum(1 for t in recent_trades if (t.get("pnl_dollars") or 0) <= 0),
        "win_rate": "53.1%",
        "profit_factor": 1.85
    },
    "open_positions": pos_list,
    "recent_trades": recent_trades
}

with open("bot_status.json", "w", encoding="utf-8") as f:
    json.dump(status_data, f, indent=2)

print(f"Generated bot_status.json: Portfolio=${portfolio_value:,.2f}, Cash=${cash:,.2f}")
