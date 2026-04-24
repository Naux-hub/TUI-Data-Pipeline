\# TUI Analytics — dbt Project



\## Overview

dbt transformation layer built on top of the TUI Hotel Booking pipeline.

Transforms raw booking data into business-ready analytical models.



\## Models

| Model | Type | Description |

|-------|------|-------------|

| stg\_bookings | view | Cleaned and staged raw booking data |

| mart\_cancellations | view | Cancellation rate by hotel type |

| mart\_lead\_time | view | Average booking lead time by country |



\## Tech Stack

\- dbt-core 1.11

\- DuckDB

\- Python 3.12



\## How to run

```bash

dbt run

```



\## Key Insights

\- City Hotels have 41.79% cancellation rate vs 27.77% for Resort Hotels

\- Germany (DEU) books furthest in advance — avg 139 days

\- UK (GBR) follows with avg 126 days

