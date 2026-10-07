# End-of-Day Reconciliation & Counterfactual Report (2026-10-07)

> [!NOTE]
> This report reconciles **Actual Live Paper Execution** against **'What Would Have Been'** counterfactual scenarios to measure the exact value added by the 1-hour bounce exit and stop-loss risk controls.

## Performance Scorecard: Actual vs Counterfactuals

| Scenario | Total P&L ($) | Win Rate (%) | Performance Delta vs Live |
| :--- | :---: | :---: | :---: |
| **Actual Live Execution** | **$-126.91** | **33.3%** | **Baseline** |
| **What-If Held to EOD Close** | $-55.42 | 0.0% | $-71.49 |
| **What-If 1-Hour Hold (07:30 PT)** | $-83.33 | 33.3% | $-43.58 |

**Net Rule Alpha (Value added by active exit timing):** `$-71.49`

## Stop-Loss Efficacy Audit

*No stop-losses were triggered today (all positions remained within the -6.0% risk limit).*

## Complete Trade-by-Trade Counterfactual Breakdown

| Symbol | Side | Exit Reason | Live Entry | Live Exit | Close Price | Live P&L ($) | What-If Close P&L ($) | Exit Alpha ($) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `STZ` | LONG | `1H_EXIT` | $118.86 | $115.35 | $118.39 | **$-79.23** | $-10.61 | **$-68.62** |
| `BMNR` | LONG | `1H_EXIT` | $25.04 | $24.53 | $24.67 | **$-51.53** | $-37.39 | **$-14.14** |
| `U` | SHORT | `EOD_CLOSE` | $45.30 | $45.23 | $45.44 | **$+3.85** | $-7.42 | **$+11.27** |
