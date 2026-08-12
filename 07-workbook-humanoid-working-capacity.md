# Humanoid Working-Capacity Workbook (Release Asset #11)

## Scope statement — read this first

This workbook is an **illustrative embodied-capacity extension** of the whitepaper's core chain (Energy → hardware → compute → models → tokens → AI working capacity → digital work → outcomes → value → agency), extended to: *Capital + energy + maintenance + utilisation + orchestration → humanoid physical working capacity.*

It is **not** a general claim about robotics economics, a product recommendation, a forecast of any real robot's field performance, or investment/procurement guidance. It models one narrow question — *what does an hour of a humanoid robot's uptime cost to own, under stated assumptions* — using (a) one clearly-labelled scenario assumption (the author's original €25,000 illustrative robot) and (b) a real market price range assembled from four named, currently sold or announced platforms. All figures below are either cited primary specs/prices, attributed secondary claims, transparent arithmetic, or explicitly labelled scenario assumptions — never a forecast. **This is educational research and scenario analysis, not investment, procurement, tax, or policy advice.** This boundary applies to every section below, not only here.

### Evidence class legend (used throughout)

| Tag | Meaning |
|---|---|
| **OBSERVED FACT** | Primary/official source, checked live on or immediately before 2026-08-12 |
| **ATTRIBUTED STATEMENT** | A named party's on-the-record claim; not independently proven true |
| **DERIVED CALCULATION** | Transparent arithmetic from cited inputs; formula always shown |
| **SCENARIO ASSUMPTION** | A visible, editable parameter, not a market figure |
| **INTERPRETATION** | A labelled explanation of how items may connect — never presented as fact |

---

## Part 1 — Two starting points: illustrative scenario vs. real market range

| Case | Price | Evidence class | Source |
|---|---|---|---|
| **Illustrative base case** | €25,000 (≈ $27,000 at an assumed 1.08 EUR/USD rate) | **SCENARIO ASSUMPTION** — the author's own original worked example; not a real product price | Author's prior calculation (per project background); FX rate is a separate SCENARIO ASSUMPTION, not a market rate |
| **Real-range LOW** | $13,500 | **OBSERVED FACT** — Unitree G1 entry price, "from $13.5K," tax/shipping excluded | https://www.unitree.com/g1, checked 2026-08-12 |
| **Real-range MID (consumer/prosumer)** | $20,000 upfront (or $499/month subscription) | **ATTRIBUTED STATEMENT** — 1X NEO early-access price, reported by Engadget (2025-10-29); not confirmed on 1X's own pricing page in the fetch performed for the source register | https://www.engadget.com/ai/1x-neo-is-a-20000-home-robot-that-will-learn-chores-via-teleoperation-040252200.html |
| **Real-range HIGH (enterprise)** | ~$250,000 | **ATTRIBUTED STATEMENT** — Agility Robotics Digit, convergent across multiple secondary/aggregator sources; no primary Agility pricing page was accessible to confirm directly | Multiple secondary sources (GrabARobot, RoboSelect360, Humanoza, et al.), checked 2026-08-12 |

Explicitly excluded from this workbook's numeric model because pricing is unconfirmed or non-existent as of 2026-08-12: Tesla Optimus (Musk has repeated a **$20,000–$30,000 long-term target**, ATTRIBUTED STATEMENT, no commercial orders or confirmed retail price exist) and Figure AI's Figure 03 (no official pricing published at all; a ~$20,000 figure circulates only via third-party aggregators). Both would sit inside or near the MID band if their aspirational figures ever became real prices — flagged here as INTERPRETATION, not fact.

**INTERPRETATION:** the €25,000 (~$27,000) illustrative case sits between the real-world MID consumer band ($20,000) and would be roughly 2x the observed LOW price and roughly 1/9th the ATTRIBUTED enterprise HIGH price. It is a plausible illustrative point *within* the real spread, not an outlier — but it is still not a verified market price for any named product.

---

## Part 2 — Required economic layer separation

Per this project's modelling rules, the layers below are kept separate and never collapsed into one number: **capital cost → financing cost → electricity (operating) cost → maintenance reserve → utilisation → cost-per-productive-hour**. (The further layers — token production cost, workload/AI-working-capacity cost, outcome/value — are out of scope for a hardware-hours model and are addressed only in the Part 6 interpretation, explicitly labelled as such.)

### 2.1 Capital layer (all four price points)

| Case | Price | Down payment (20%, SCENARIO ASSUMPTION) | Amount financed |
|---|---|---|---|
| Illustrative (€25,000 / ~$27,000) | $27,000 | $5,400 | $21,600 |
| Real LOW ($13,500) | $13,500 | $2,700 | $10,800 |
| Real MID ($20,000) | $20,000 | $4,000 | $16,000 |
| Real HIGH ($250,000) | $250,000 | $50,000 | $200,000 |

The 20% down payment is a **SCENARIO ASSUMPTION** controlling how much capital is financed vs. paid up front; it is editable (see Part 3.2 sensitivity).

---

## Part 3 — Financing layer

**DERIVED CALCULATION.** Standard amortizing-loan formula:

`M = P × i / (1 − (1+i)^-n)`  where P = amount financed, i = monthly rate (annual rate ÷ 12), n = number of monthly payments (years × 12).

Base case: 5-year term, 8% annual rate (both **SCENARIO ASSUMPTIONS** — editable; 8% is illustrative, not a quoted lender rate). Down payment is amortized straight-line over the same term and added back so total capital+financing cost is comparable across cases.

`Total annual capital+financing cost = (M × 12) + (Down payment ÷ financing term years)`

### 3.1 Base case (5yr @ 8%, 20% down)

| Case | Monthly payment | Annual financing (M×12) | Down payment amortized/yr | **Total capital+financing cost/yr** |
|---|---|---|---|---|
| Illustrative (~$27,000 / €25,000) | $437.97 (≈€405.53) | $5,255.64 | $1,080.00 | **$6,335.64** (≈€5,866.33 — matches the original EUR worked example) |
| Real LOW ($13,500) | $218.99 | $2,627.82 | $540.00 | **$3,167.82** |
| Real MID ($20,000) | $324.42 | $3,893.07 | $800.00 | **$4,693.07** |
| Real HIGH ($250,000) | $4,055.28 | $48,663.35 | $10,000.00 | **$58,663.35** |

### 3.2 Financing-term sensitivity (8% rate, 20% down held constant) — total capital+financing cost/yr

| Case | 3 yr | 4 yr | 5 yr | 7 yr |
|---|---|---|---|---|
| Illustrative (~$27,000) | $9,921.79 | $7,677.83 | $6,335.64 | $4,811.38 |
| Real LOW ($13,500) | $4,961.19 | $3,838.91 | $3,167.82 | $2,405.69 |
| Real MID ($20,000) | $7,349.92 | $5,687.28 | $4,693.07 | $3,563.98 |
| Real HIGH ($250,000) | $91,873.94 | $71,091.01 | $58,663.35 | $44,549.77 |

(Illustrative column recomputed at the $27,000 USD-equivalent scale for internal consistency; native-EUR values scale proportionally.)

### 3.3 Down-payment sensitivity (5yr @ 8% held constant) — total capital+financing cost/yr

| Case | 0% down | 20% down | 40% down |
|---|---|---|---|
| Illustrative (~$27,000) | $6,569.55 | $6,335.64 | $6,101.73 |
| Real LOW ($13,500) | $3,284.78 | $3,167.82 | $3,050.87 |
| Real MID ($20,000) | $4,866.33 | $4,693.07 | $4,519.80 |
| Real HIGH ($250,000) | $60,829.18 | $58,663.35 | $56,497.51 |

**INTERPRETATION:** term length matters far more than down-payment size in this model — stretching from 3 to 7 years cuts the annual capital+financing burden by roughly half, while doubling the down payment only trims it by a few percent. Both are editable levers, not market facts.

---

## Part 4 — Electricity layer

Two parallel methods, both **SCENARIO ASSUMPTIONS** unless noted:

**(a) Flat operating-hour assumption** (as in the original illustrative case): $0.11/operating hour (≈€0.10/h at the assumed FX rate) — a simple placeholder, not tied to any specific robot's power draw.

**(b) Spec-derived rate**, using 1X NEO's OBSERVED battery spec (842 Wh runtime over 4 hours → average continuous draw ≈ 0.2105 kW) at an illustrative $0.15/kWh electricity price (**SCENARIO ASSUMPTION** — a plausible commercial/industrial US-average rate, not a quoted utility tariff):

`Electricity $/hour = average power draw (kW) × electricity price ($/kWh)`
`= 0.2105 kW × $0.15/kWh = $0.0316/hour`

Source for the underlying spec: https://www.1x.tech/neo (OBSERVED FACT — 842 Wh runtime, 4-hour battery life), checked 2026-08-12.

**INTERPRETATION:** the spec-derived figure is an order of magnitude lower than the flat $0.11/h placeholder — humanoid robots at ~200W average draw are electrically cheap to run relative to almost any other capital cost in this model; electricity is not the binding cost driver here (unlike in data-center/token-production economics elsewhere in the whitepaper). This spec applies to 1X NEO specifically and is used as an illustrative order-of-magnitude anchor for the other three price points too — it is not verified for Unitree G1, Agility Digit, or the illustrative case.

---

## Part 5 — Maintenance layer

**SCENARIO ASSUMPTION:** maintenance/repair reserve = 10% of purchase price per year (unchanged from the original illustrative case; not a manufacturer-quoted service contract for any of the four platforms — none of the four sources in the register publish a maintenance-cost figure).

| Case | Maintenance reserve/yr |
|---|---|
| Illustrative (~$27,000) | $2,700 |
| Real LOW ($13,500) | $1,350 |
| Real MID ($20,000) | $2,000 |
| Real HIGH ($250,000) | $25,000 |

---

## Part 6 — Utilization sensitivity and cost-per-hour ranges

**DERIVED CALCULATION.**

`Cost/hour (financing+electricity) = (Total capital+financing cost/yr + electricity $/hr × annual hours) ÷ annual hours`
`Cost/hour (financing+electricity+maintenance) = (Total capital+financing cost/yr + electricity $/hr × annual hours + maintenance/yr) ÷ annual hours`

Shown at both electricity assumptions (flat $0.11/h vs. spec-derived $0.0316/h) and four productive-utilization levels (2,000 / 4,000 / 6,000 / 8,000 hours/year — themselves SCENARIO ASSUMPTIONS bracketing single-shift to near-continuous operation).

### 6.1 Illustrative base case (~$27,000 / €25,000) — USD, native-EUR cross-check in parentheses

| Utilization (h/yr) | Fin+elec (flat) | Fin+elec+maint (flat) | Fin+elec (spec) | Fin+elec+maint (spec) |
|---|---|---|---|---|
| 2,000 | $3.28 (€3.03) | $4.63 (€4.28) | $3.20 | $4.55 |
| 4,000 | $1.69 (€1.57) | $2.37 (€2.19) | $1.62 | $2.29 |
| 6,000 | $1.17 (€1.08) | $1.62 (€1.49) | $1.09 | $1.54 |
| 8,000 | $0.90 (€0.83) | $1.24 (€1.15) | $0.82 | $1.16 |

(EUR values shown are the exact recomputation in native EUR at €0.10/h flat electricity — they match the original worked example, confirming internal consistency.)

### 6.2 Real-range LOW ($13,500, Unitree G1)

| Utilization (h/yr) | Fin+elec (flat) | Fin+elec+maint (flat) | Fin+elec (spec) | Fin+elec+maint (spec) |
|---|---|---|---|---|
| 2,000 | $1.69 | $2.37 | $1.62 | $2.29 |
| 4,000 | $0.90 | $1.24 | $0.82 | $1.16 |
| 6,000 | $0.64 | $0.86 | $0.56 | $0.79 |
| 8,000 | $0.51 | $0.68 | $0.43 | $0.60 |

### 6.3 Real-range MID ($20,000, 1X NEO early-access price)

| Utilization (h/yr) | Fin+elec (flat) | Fin+elec+maint (flat) | Fin+elec (spec) | Fin+elec+maint (spec) |
|---|---|---|---|---|
| 2,000 | $2.46 | $3.46 | $2.38 | $3.38 |
| 4,000 | $1.28 | $1.78 | $1.21 | $1.71 |
| 6,000 | $0.89 | $1.23 | $0.81 | $1.15 |
| 8,000 | $0.70 | $0.95 | $0.62 | $0.87 |

### 6.4 Real-range HIGH ($250,000, Agility Digit)

| Utilization (h/yr) | Fin+elec (flat) | Fin+elec+maint (flat) | Fin+elec (spec) | Fin+elec+maint (spec) |
|---|---|---|---|---|
| 2,000 | $29.44 | $41.94 | $29.36 | $41.86 |
| 4,000 | $14.78 | $21.03 | $14.70 | $20.95 |
| 6,000 | $9.89 | $14.05 | $9.81 | $13.98 |
| 8,000 | $7.44 | $10.57 | $7.36 | $10.49 |

### 6.5 Summary — cost-per-productive-hour range across the whole spread

| Utilization | Full observed/attributed spread (incl. maintenance, flat electricity) | Illustrative case sits at |
|---|---|---|
| 2,000 h/yr | $2.37 – $41.94 | $4.63 |
| 4,000 h/yr | $1.24 – $21.03 | $2.37 |
| 6,000 h/yr | $0.86 – $14.05 | $1.62 |
| 8,000 h/yr | $0.68 – $10.57 | $1.24 |

**INTERPRETATION:** utilization dominates the cost-per-hour result more than any other single variable in this model — moving from 2,000 to 8,000 hours/year cuts the per-hour cost by roughly 3.5–4x at every price point, because capital and financing costs are fixed while the denominator (hours) grows. The illustrative €25,000/~$27,000 case tracks closely with the real MID consumer band ($20,000, 1X NEO) once financing/maintenance assumptions are held constant — it is not an outlier relative to real currently-purchasable platforms, but it sits far below the ATTRIBUTED enterprise-tier HIGH case, whose cost-per-hour is dominated by a purchase price that itself rests only on secondary-source corroboration, not a primary Agility Robotics price sheet.

---

## Part 7 — What this model explicitly excludes

Per the original scope (unchanged; **SCENARIO ASSUMPTION** boundary, not a completeness claim): supervision/human-oversight labor cost, robot software/subscription fees, insurance, workspace modification, consumables, and downtime/unplanned-repair time beyond the flat maintenance reserve. None of the four cited platforms publish data allowing these to be estimated from a primary source as of 2026-08-12; adding them would only push cost-per-hour higher, so all figures above should be read as a **floor**, not a full commercial cost.

---

## Part 8 — Where this connects to the wider chain (interpretation only)

**INTERPRETATION:** this workbook extends the whitepaper's core chain — Capital + energy + maintenance + utilisation + orchestration → humanoid physical working capacity — but stops at "capacity," deliberately not continuing into "work → outcome → value." A robot costing $1/hour to own tells you nothing about whether the work it performs is worth $1, $100, or nothing at all; per the whitepaper's value framework, working capacity is not value, and more hours of operation are not automatically better. Any use of these cost-per-hour figures to argue a specific business case, investment decision, or procurement choice would be going beyond what this workbook supports — **this is not investment, procurement, tax, legal, or policy advice**, and the figures above are illustrative arithmetic on stated, editable assumptions, not a forecast of any real deployment's economics.

---

### Full input register for this workbook (for editing)

| Parameter | Value used | Class | Controls |
|---|---|---|---|
| Illustrative robot price | €25,000 (~$27,000) | SCENARIO ASSUMPTION | Base-case capital layer |
| EUR/USD FX rate | 1.08 | SCENARIO ASSUMPTION | USD conversion of illustrative case only |
| Unitree G1 price | $13,500 | OBSERVED FACT (unitree.com, checked 2026-08-12) | Real-range LOW |
| 1X NEO price | $20,000 / $499/mo | ATTRIBUTED STATEMENT (Engadget, 2025-10-29) | Real-range MID |
| Agility Digit price | ~$250,000 | ATTRIBUTED STATEMENT (multiple secondary sources) | Real-range HIGH |
| Down payment | 20% (sensitivity: 0%/40%) | SCENARIO ASSUMPTION | Capital layer split |
| Financing rate | 8% APR | SCENARIO ASSUMPTION | Financing layer |
| Financing term | 5 yr (sensitivity: 3/4/7 yr) | SCENARIO ASSUMPTION | Financing layer |
| Flat electricity rate | $0.11/hr (≈€0.10/hr) | SCENARIO ASSUMPTION | Electricity layer (method a) |
| Electricity price for spec-derived method | $0.15/kWh | SCENARIO ASSUMPTION | Electricity layer (method b) |
| 1X NEO average power draw | 0.2105 kW (842 Wh / 4 h) | OBSERVED FACT (1x.tech, checked 2026-08-12) | Electricity layer (method b) |
| Maintenance reserve | 10% of purchase price/yr | SCENARIO ASSUMPTION | Maintenance layer |
| Productive utilization | 2,000 / 4,000 / 6,000 / 8,000 h/yr | SCENARIO ASSUMPTION | Utilization sensitivity |

---

This workbook (Part 1 real-price sourcing, Parts 2–6 arithmetic, Parts 7–8 scope/interpretation) is a standalone numeric asset for the whitepaper "Why Are They Spending Trillions on AI?" (CC BY 4.0, Valto Loikkanen). No file path was specified for this deliverable in the task; the full content above is the release asset itself, returned as markdown text. If a physical file location is wanted (e.g., under `Storage-wiki/Storage/Other/`), it was not created in this run — only the content was produced here.