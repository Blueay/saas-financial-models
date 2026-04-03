# Input Mask Guide · SaaS FP&A Dashboard

**Module:** Controlling & Financial Planning  
**Tab:** ✏️ Input Mask  
**Version:** 1.0.0

---

## Overview

The Input Mask is the control layer of the SaaS FP&A dashboard. It lets you replace the built-in dummy data with your own assumptions — without touching a single line of code. Every slider, number field, and dropdown feeds directly into the financial model engine. Once you click **Apply & Recalculate**, all charts, KPI cards, tables, and forecasts across all six dashboard tabs update instantly.

The mask is designed for three workflows:

- **Exploring scenarios** — use the Bull / Bear / Base presets to stress-test the model in seconds
- **Planning cycles** — enter your actual budget assumptions to generate a 24-month operating plan
- **Board preparation** — tune assumptions until the model reflects your narrative, then screenshot or export

---

## How to Use the Input Mask

### Step 1 — Open the tab

Click **✏️ Input Mask** in the top-right of the navigation bar. It sits deliberately separated from the analytical tabs to signal that this is where you configure, not just view.

### Step 2 — Choose a starting point

At the top of the mask you will find the **Scenario Switcher**. Pick one of the three presets — Base, Bull, or Bear — to pre-fill all parameters with a consistent set of assumptions. This is the fastest way to get a meaningful model running. You can then fine-tune individual fields from there.

### Step 3 — Review the Live Preview strip

Directly below the scenario buttons is the **Live Preview** strip — eight KPI cards that recalculate in real time as you change any input. You do not need to click Apply to see these update. Use the preview to sanity-check your assumptions before committing:

- Green values indicate healthy, benchmark-grade metrics
- Yellow values signal a metric worth watching
- Red values flag a problem that may need attention

The preview also surfaces **validation warnings** at the bottom of the page if your inputs produce a structurally broken model (e.g. churn rate exceeding growth rate, or LTV below CAC).

### Step 4 — Edit parameters

Work through the six input sections. Each section groups related parameters. Use sliders for rates and percentages — they give you intuitive, bounded control. Use number fields for absolute dollar amounts and counts where precision matters.

### Step 5 — Apply the model

Click **▶ Apply & Recalculate Model**. The engine re-runs all 24 months of projections and rebuilds every chart. The company name in the header also updates to reflect the Company Settings section. The process takes less than a second.

### Step 6 — Reset if needed

Click **↩ Reset to Defaults** at any time to restore all parameters to the original dummy-data assumptions. The active scenario badge also resets to Base Case.

---

## Input Sections & Parameters

### 💰 Revenue Assumptions

This section defines how revenue enters and grows in the model. It is the most impactful section — changes here cascade through MRR, ARR, P&L, unit economics, and forecast tabs.

| Parameter | Type | Default | Range | Description |
|-----------|------|---------|-------|-------------|
| Starting MRR | Number field | $500,000 | $10K – $50M | The Monthly Recurring Revenue at period 1 (January 2024). This is the base from which all growth compounds. Set this to your actual MRR at the start of the planning period. |
| MRR Growth Rate (Y1) | Slider | 8.2% | 1% – 30% | Monthly MRR growth rate applied across the first 12 periods. This drives new MRR, not total MRR — it controls how aggressively new bookings and expansion are assumed to grow. |
| MRR Growth Rate (Y2) | Slider | 5.0% | 1% – 20% | Monthly MRR growth rate applied to periods 13–24. Typically lower than Y1 as the business matures and growth normalises. Most SaaS companies transition from hyper-growth to steady-state in year 2 or 3. |
| ARPU (Monthly) | Number field | $3,200 | $100 – $100K | Average Revenue Per Unit per month. Used to convert customer counts into MRR. If your product has multiple tiers, use a blended average weighted by customer distribution. |
| New Customers (Month 1) | Number field | 45 | 1 – 5,000 | The number of net new customers added in the first period. The model compounds this forward using the Y1/Y2 growth rates. This drives new MRR calculations each month. |

---

### 👥 Customer Metrics

This section controls the retention and expansion dynamics of your existing customer base. These are the most sensitive levers in SaaS — small changes to churn have outsized effects on NRR, LTV, and long-term ARR.

| Parameter | Type | Default | Range | Description |
|-----------|------|---------|-------|-------------|
| Monthly Churn Rate | Slider | 2.5% | 0.5% – 10% | The percentage of customers who cancel each month. At 2.5%, roughly 26% of customers churn annually. Industry benchmark for B2B SaaS is 1–3% monthly. Rates above 4% typically indicate product-market fit or pricing issues. |
| Expansion MRR Rate | Slider | 1.5% | 0% – 8% | The percentage of existing MRR that is added each month through upsells, seat expansions, or tier upgrades. An expansion rate that exceeds churn produces Net Revenue Retention above 100% — sometimes called "negative churn". |
| Contraction Rate | Slider | 0.5% | 0% – 5% | The percentage of existing MRR lost each month through downgrades or seat reductions. This is distinct from full churn — the customer stays but pays less. Combined with churn MRR, this feeds the MRR waterfall as the loss side. |

**How these interact:** NRR is calculated as `(Starting MRR + Expansion − Contraction − Churn) / Starting MRR × 100`. With defaults, NRR is approximately 98.5%. Push expansion above churn to achieve NRR > 100%, which means the existing customer base grows revenue on its own.

---

### ⚙️ Unit Economics

This section drives the efficiency metrics: how much it costs to acquire customers, how much each customer is worth over their lifetime, and how healthy the underlying business margins are.

| Parameter | Type | Default | Range | Description |
|-----------|------|---------|-------|-------------|
| CAC (per customer) | Number field | $18,000 | $500 – $500K | Customer Acquisition Cost — the fully-loaded cost to acquire one new customer, including sales salaries, commissions, marketing spend, and tooling. Used to calculate LTV:CAC ratio and payback period. |
| Gross Margin | Slider | 72.0% | 20% – 95% | The percentage of revenue remaining after Cost of Goods Sold (COGS). For SaaS, COGS typically includes hosting, infrastructure, customer success, and support. Typical range is 65–85%. This directly affects LTV, EBITDA, and burn calculations. |
| Starting Cash | Number field | $5,000,000 | $0 – $500M | Cash on hand at model start. Used to calculate cash runway (months of operation remaining at current burn rate). If the model projects EBITDA-positive operation throughout, runway will display as unlimited (999+). |

**Derived metrics from these inputs:**

- `LTV = (ARPU × Gross Margin) / Monthly Churn Rate`
- `LTV:CAC = LTV / CAC` — healthy benchmark is ≥ 3x, excellent is ≥ 5x
- `CAC Payback = CAC / (ARPU × Gross Margin)` — benchmark: ≤ 18 months

---

### 📋 OpEx Planning

This section sets the operating expense base for each department and controls how fast costs grow over the 24-month model horizon.

| Parameter | Type | Default | Range | Description |
|-----------|------|---------|-------|-------------|
| Sales & Marketing (Month 1) | Number field | $280,000 | $0 – $10M | Monthly S&M spend at period 1. Includes sales headcount, commissions, marketing programs, paid acquisition, events, and related tools. This is typically the largest OpEx line for growth-stage SaaS. |
| Research & Development (Month 1) | Number field | $210,000 | $0 – $10M | Monthly R&D spend at period 1. Includes engineering, product, and design headcount plus their tooling and infrastructure costs. The model grows R&D slightly faster than other departments (growth rate × 1.2×) to reflect typical hiring velocity. |
| General & Administrative (Month 1) | Number field | $95,000 | $0 – $5M | Monthly G&A spend at period 1. Includes finance, HR, legal, office, and executive costs. The model grows G&A more slowly than S&M and R&D (growth rate × 0.7×), reflecting the more stable nature of overhead functions. |
| Monthly OpEx Growth Rate | Slider | 1.5% | 0% – 10% | The base monthly growth rate applied to all three OpEx departments. Each department scales this differently: S&M at 1.0×, R&D at 1.2×, G&A at 0.7×. Set to 0% to model a fully fixed cost structure. |

**How EBITDA is calculated:**

```
Gross Profit = Revenue × Gross Margin %
EBITDA       = Gross Profit − (S&M + R&D + G&A)
EBITDA Margin = EBITDA / Revenue × 100
```

Burn is the absolute value of EBITDA when negative. Once EBITDA turns positive, burn is zero and runway is unlimited.

---

### 🔮 Budget & Forecast Settings

This section controls how the model constructs budget targets, and how the rolling forecast is generated and presented.

| Parameter | Type | Default | Range | Description |
|-----------|------|---------|-------|-------------|
| Budget Optimism Bias | Slider | 1.0% | 0% – 15% | The percentage by which the budget exceeds the model's base projection each period. Boards and investors typically set budgets 5–10% above base-case assumptions. This creates the "below budget" variance you see in the default model. Set to 0% for a neutral budget that matches actuals. |
| Forecast Periods | Slider | 3 months | 1 – 12 months | The number of months the rolling forecast projects beyond the last modelled period. More periods reduce forecast confidence. The Forecast tab displays a confidence rating: High (1 month), Medium (2 months), Low (3+ months). |
| Starting Headcount | Number field | 68 | 1 – 10,000 | Total full-time employees at period 1. Used to calculate Revenue per Employee — a key operational efficiency metric that should trend upward as the business scales. |
| Headcount Growth per Quarter | Slider | +2 FTE | 0 – 20 FTE | The number of net new hires added every three months. The model adds this headcount in quarter-start months (January, April, July, October). Headcount growth affects Revenue per Employee but does not independently drive OpEx — that is controlled by the OpEx Growth Rate. |

---

### 🏢 Company Settings

This section configures metadata that affects labels, formatting, and display throughout the dashboard. These settings do not affect calculations — they affect presentation.

| Parameter | Type | Default | Options / Notes |
|-----------|------|---------|-----------------|
| Company Name | Text field | AcmeSaaS Inc. | Updates the header subtitle across the entire dashboard when you apply the model. |
| Currency | Dropdown | USD | USD, EUR, GBP, CHF. Updates the currency symbol displayed in the header. Note: exchange rate conversion is not applied — all values remain in the units you enter. |
| Model Start | Dropdown | Jan 2024 | Jan 2024, Jul 2024, Jan 2025, Jul 2025. Controls the label of the first period in the month sequence. |
| Variance Alert Threshold | Number field | 3% | 0.5% – 20%. The minimum variance percentage that triggers a flag in the variance analysis. Periods where actual revenue deviates from budget by more than this threshold are highlighted in the P&L table. |

---

## Model Assumptions

The following assumptions are baked into the model engine and apply regardless of inputs. They reflect standard SaaS financial modelling conventions.

### Revenue Recognition
- Revenue is recognised in the month it is earned, not when cash is received
- MRR and ARR are subscription-based — one-time or professional services revenue is not modelled
- ARR is calculated as `Ending MRR × 12` (annualised snapshot, not a sum of monthly figures)
- Budget is set as `MRR × (1 + Growth Rate + Optimism Bias)` — a forward-looking plan rather than a zero-based budget

### MRR Waterfall
- Each month: `Ending MRR = Starting MRR + New MRR + Expansion MRR − Churn MRR − Contraction MRR`
- New MRR derives from `New Customers × ARPU`
- Churn MRR derives from `Starting MRR × Monthly Churn Rate`
- Expansion and Contraction MRR derive from `Starting MRR × respective rates`

### Customer Count
- Starting customer count is derived as `Starting MRR / ARPU` (rounded)
- New customers are compounded forward each month using `New Customers × (1 + Growth Rate × 0.5)` — customer growth is assumed to lag MRR growth by half, reflecting typical sales cycle dynamics
- Churned customers are calculated as `Starting Customers × Monthly Churn Rate` (rounded)

### ARPU and CAC Drift
- ARPU drifts upward slightly each period (+0.2% per month) to reflect modest pricing power and mix shift toward higher tiers
- CAC drifts upward slightly each period (+0.1% per month) to reflect increasing competition and market saturation — a common real-world pattern

### OpEx Growth
- S&M grows at `1.0 × OpEx Growth Rate` per month
- R&D grows at `1.2 × OpEx Growth Rate` per month (engineering tends to scale faster)
- G&A grows at `0.7 × OpEx Growth Rate` per month (overhead scales slower than revenue)

### Headcount
- Headcount increases in quarter-start months only (periods 1, 4, 7, 10, 13, 16, 19, 22)
- Revenue per Employee is `Monthly Revenue / Total Headcount` — a lagging indicator of operational efficiency

### Cash and Runway
- Cash runway is calculated as `Remaining Cash / Monthly Burn`
- Burn is zero in any month where EBITDA ≥ 0
- Runway displays as 999 when the model projects EBITDA-positive operations (unlimited runway)
- The model does not account for fundraising events, debt, or interest income

### Cohort Retention
- Cohort retention is modelled using a constant monthly churn rate (from the Customer Metrics section)
- Retention at M+N is calculated as `(1 − Churn Rate)^N`
- This assumes constant churn across all cohorts — real businesses often see older cohorts retain better as low-intent customers churn early

---

## Scenario Switcher — Parameter Sets

The three scenario presets apply a coordinated set of assumptions designed to represent internally consistent views of the business. Switching scenarios loads all parameters simultaneously to avoid contradictory combinations (e.g. high growth with very low marketing spend).

---

### Base Case

The default operating plan. Reflects a well-managed, mid-stage B2B SaaS company growing steadily with controlled burn and healthy unit economics.

| Parameter | Base Case Value | Rationale |
|-----------|----------------|-----------|
| MRR Growth Rate Y1 | 8.2% | Solid but achievable growth for a $500K MRR starting company |
| MRR Growth Rate Y2 | 5.0% | Normalised growth as the business matures |
| Monthly Churn Rate | 2.5% | Mid-range B2B SaaS — room for improvement but not alarming |
| Expansion MRR Rate | 1.5% | Moderate upsell motion, not yet systematic |
| Gross Margin | 72.0% | Typical for a cloud-hosted B2B SaaS product |
| Budget Optimism Bias | 1.0% | Lightly optimistic plan — close to actuals |
| S&M Budget (Month 1) | $280,000 | Healthy sales team with moderate marketing investment |
| R&D Budget (Month 1) | $210,000 | Engineering-led team with product focus |

**Expected outcomes:** ARR reaches approximately $54M by period 24. Rule of 40 score crosses 40 around month 9 and climbs to ~64 by year-end 2025. The model turns EBITDA-positive around month 4.

---

### Bull Case 🟢

An optimistic scenario where product-market fit is strong, churn is low, expansion is a systematic motion, and sales efficiency is high. Appropriate for investor presentations modelling upside, or for testing whether aggressive targets are financially coherent.

| Parameter | Bull Case Value | Change vs. Base |
|-----------|----------------|-----------------|
| MRR Growth Rate Y1 | 14.0% | +5.8 pp — aggressive new business growth |
| MRR Growth Rate Y2 | 9.0% | +4.0 pp — strong second-year momentum |
| Monthly Churn Rate | 1.5% | −1.0 pp — excellent product stickiness |
| Expansion MRR Rate | 2.5% | +1.0 pp — active upsell and expansion motion |
| Gross Margin | 76.0% | +4.0 pp — infrastructure efficiency gains at scale |
| Budget Optimism Bias | 0.5% | −0.5 pp — budget nearly matches actuals |
| S&M Budget (Month 1) | $340,000 | +$60K — increased investment in go-to-market |
| R&D Budget (Month 1) | $250,000 | +$40K — product investment supporting retention |

**Expected outcomes:** ARR exceeds $80M by period 24. NRR climbs above 101% (net negative churn). Rule of 40 score exceeds 60 by mid-year 2024. CAC Payback falls below 8 months. LTV:CAC ratio exceeds 6x.

**Key risk:** Higher S&M and R&D spend requires the growth assumptions to materialise — if growth disappoints while costs are elevated, burn spikes quickly.

---

### Bear Case 🔴

A conservative stress-test scenario where growth is slower than expected, churn is elevated, and margins are compressed. Use this to model downside risk, calculate minimum viable runway, or pressure-test the business model's resilience.

| Parameter | Bear Case Value | Change vs. Base |
|-----------|----------------|-----------------|
| MRR Growth Rate Y1 | 4.5% | −3.7 pp — sluggish new business pipeline |
| MRR Growth Rate Y2 | 2.5% | −2.5 pp — further deceleration |
| Monthly Churn Rate | 4.5% | +2.0 pp — significant retention problem |
| Expansion MRR Rate | 0.8% | −0.7 pp — limited upsell motion |
| Gross Margin | 68.0% | −4.0 pp — higher infrastructure or support costs |
| Budget Optimism Bias | 5.0% | +4.0 pp — board set aggressive targets, actuals disappoint |
| S&M Budget (Month 1) | $220,000 | −$60K — cost reduction in response to miss |
| R&D Budget (Month 1) | $180,000 | −$30K — engineering freeze |

**Expected outcomes:** ARR reaches approximately $22M by period 24. NRR falls to ~95%, meaning the existing customer base is shrinking. Rule of 40 score stays negative or near zero throughout most of Y1. Burn extends deeper into 2024, and cash runway shortens significantly depending on the Starting Cash input.

**Key risk:** At 4.5% monthly churn, roughly 42% of customers churn annually. Combined with slow new business growth, this creates a "leaky bucket" dynamic where the top-of-funnel cannot compensate for the losses at the bottom. The model will flag a validation warning if churn approaches or exceeds growth rate.

---

## Validation Warnings

The input mask checks three conditions and displays a warning panel if any are triggered. These do not block you from applying the model — they are advisory.

| Warning | Condition | What it means |
|---------|-----------|---------------|
| Churn ≥ Growth Rate | Monthly churn rate ≥ Y1 growth rate | Net new MRR will be negative — the bucket is leaking faster than it is being filled |
| LTV:CAC < 1x | CAC > LTV | Each customer costs more to acquire than it will ever return — the unit economics are inverted |
| OpEx > 3× Starting MRR | Total OpEx exceeds $1.5M at default starting MRR | Burn in early months will be very high — check Starting Cash and runway |

---

## Tips for Getting the Most from the Input Mask

**Start with a scenario, then adjust.** Rather than entering every field from scratch, pick the scenario closest to your view and tweak 2–3 parameters. This keeps assumptions internally consistent.

**Use the live preview as a reality check.** Before applying, verify that the projected ARR, LTV:CAC, and Rule of 40 are in a plausible range for your company stage. If ARR looks too high or too low, the growth rate or ARPU is likely the culprit.

**Match ARPU to your actual blended rate.** If you have three pricing tiers at $1K, $3K, and $8K, and your customer mix is 60/30/10, your blended ARPU is `(0.6×1000) + (0.3×3000) + (0.1×8000) = $2,300` — not the simple average of your tiers.

**Set churn honestly.** Churn is the most impactful lever in the model. Understating it produces an unrealistically optimistic ARR trajectory. If you do not yet have reliable churn data, use 3–4% as a conservative assumption for an early-stage B2B SaaS product.

**The budget bias is not a fudge factor.** It models the real-world dynamic where finance teams and boards set aspirational targets above the base operating plan. Setting it to 0% gives you a neutral budget. Setting it to 10% reflects an aggressive board target — and explains why every month shows "below budget" in the P&L tab.

---

*Part of the AI-Powered SaaS Financial Models series · Module 02: Controlling & Financial Planning*
