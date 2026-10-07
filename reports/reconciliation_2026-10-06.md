# End-of-Day Reconciliation & Counterfactual Report (2026-10-06)

> [!NOTE]
> This report reconciles **Actual Live Paper Execution** against **'What Would Have Been'** counterfactual scenarios to measure the exact value added by the 1-hour bounce exit and stop-loss risk controls.

## Performance Scorecard: Actual vs Counterfactuals

| Scenario | Total P&L ($) | Win Rate (%) | Performance Delta vs Live |
| :--- | :---: | :---: | :---: |
| **Actual Live Execution** | **$+95.88** | **40.0%** | **Baseline** |
| **What-If Held to EOD Close** | $+70.92 | 52.0% | $+24.96 |
| **What-If 1-Hour Hold (10:30 ET)** | $-273.97 | 40.0% | $+369.85 |

**Net Rule Alpha (Value added by active exit timing):** `$+24.96`

## Stop-Loss Efficacy Audit

*No stop-losses were triggered today (all positions remained within the -6.0% risk limit).*

## Complete Trade-by-Trade Counterfactual Breakdown

| Symbol | Side | Exit Reason | Live Entry | Live Exit | Close Price | Live P&L ($) | What-If Close P&L ($) | Exit Alpha ($) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ANF` | LONG | `1H_EXIT` | $141.40 | $140.05 | $141.28 | **$-38.39** | $-3.41 | **$-34.98** |
| `MRVL` | LONG | `1H_EXIT` | $279.23 | $297.64 | $286.50 | **$+276.62** | $+109.24 | **$+167.38** |
| `TCOM` | LONG | `1H_EXIT` | $38.24 | $38.32 | $38.26 | **$+8.34** | $+2.08 | **$+6.26** |
| `CCL` | LONG | `1H_EXIT` | $25.92 | $26.57 | $26.57 | **$+102.52** | $+102.11 | **$+0.41** |
| `WDC` | LONG | `1H_EXIT` | $422.36 | $417.76 | $412.41 | **$-42.92** | $-92.79 | **$+49.87** |
| `AAPL` | LONG | `1H_EXIT` | $332.84 | $332.13 | $333.72 | **$-8.58** | $+10.62 | **$-19.20** |
| `GE` | LONG | `1H_EXIT` | $306.90 | $309.30 | $309.42 | **$+31.50** | $+33.07 | **$-1.57** |
| `LYFT` | LONG | `1H_EXIT` | $15.79 | $15.80 | $15.77 | **$+2.55** | $-5.10 | **$+7.65** |
| `PBR` | LONG | `1H_EXIT` | $23.91 | $23.98 | $23.80 | **$+12.09** | $-17.52 | **$+29.61** |
| `CHWY` | LONG | `1H_EXIT` | $18.22 | $17.92 | $18.14 | **$-66.07** | $-16.53 | **$-49.54** |
| `SYY` | LONG | `1H_EXIT` | $76.65 | $76.76 | $77.44 | **$+5.79** | $+41.56 | **$-35.77** |
| `NVO` | LONG | `1H_EXIT` | $37.36 | $37.36 | $37.53 | **$+0.00** | $+18.26 | **$-18.26** |
| `MCD` | LONG | `1H_EXIT` | $232.97 | $232.20 | $232.45 | **$-13.28** | $-8.97 | **$-4.31** |
| `APO` | LONG | `1H_EXIT` | $116.00 | $114.81 | $115.91 | **$-41.47** | $-3.14 | **$-38.33** |
| `DHR` | LONG | `1H_EXIT` | $226.25 | $226.20 | $215.61 | **$-0.91** | $-193.32 | **$+192.41** |
| `TWLO` | LONG | `1H_EXIT` | $306.49 | $300.23 | $280.21 | **$-84.23** | $-353.88 | **$+269.65** |
| `VZ` | LONG | `1H_EXIT` | $45.72 | $45.57 | $45.97 | **$-13.02** | $+21.91 | **$-34.93** |
| `DHI` | LONG | `1H_EXIT` | $134.28 | $134.02 | $136.72 | **$-7.88** | $+73.76 | **$-81.64** |
| `ACHR` | LONG | `1H_EXIT` | $4.75 | $4.74 | $4.66 | **$-9.57** | $-76.50 | **$+66.93** |
| `GLW` | LONG | `1H_EXIT` | $161.85 | $163.44 | $169.02 | **$+40.20** | $+180.98 | **$-140.78** |
| `CMCSA` | LONG | `1H_EXIT` | $21.73 | $21.60 | $21.59 | **$-24.11** | $-27.01 | **$+2.90** |
| `RBLX` | LONG | `1H_EXIT` | $43.94 | $44.26 | $45.57 | **$+28.60** | $+146.95 | **$-118.35** |
| `LEN` | LONG | `1H_EXIT` | $75.80 | $75.81 | $77.38 | **$+0.63** | $+85.32 | **$-84.69** |
| `TSCO` | LONG | `1H_EXIT` | $31.63 | $31.40 | $32.30 | **$-29.00** | $+85.15 | **$-114.15** |
| `TTD` | LONG | `1H_EXIT` | $12.04 | $11.94 | $11.91 | **$-33.53** | $-41.92 | **$+8.39** |
