# saas-financial-models
SaaS FP&amp;A dashboard — MRR/ARR waterfall, budget variance, unit economics &amp; cohort retention. Python model engine + interactive HTML dashboard with live scenario input mask.


# 📊 SaaS Controlling & Financial Planning Model

> **Module:** Controlling & Financial Planning (FP&A)  
> **Series:** AI-Powered Financial Models for SaaS  
> **Version:** 1.0.0 | Python · No external dependencies  
> **License:** MIT

---

## 🧭 What Is This Model?

This is a **Python-native FP&A (Financial Planning & Analysis) model** built specifically for SaaS businesses. It simulates and analyzes the full controlling stack — from MRR waterfall mechanics to budget variance, unit economics, cohort retention, and rolling forecasts.

Unlike Excel-based templates, this model is **code-first**: all logic is transparent, version-controllable, testable, and extensible with real data connectors (Stripe, HubSpot, Snowflake, etc.).

---

## 🎯 Goal

| # | Objective |
|---|-----------|
| 1 | Model **recurring revenue dynamics** (MRR/ARR waterfall) month by month |
| 2 | Perform **budget vs. actuals variance analysis** with automated flagging |
| 3 | Compute **unit economics**: CAC, LTV, Payback Period, LTV:CAC |
| 4 | Run **cohort-based churn analysis** to forecast retention curves |
| 5 | Generate a **rolling 3–6 month forecast** using smoothed growth assumptions |
| 6 | Track **strategic KPIs**: Rule of 40, Burn Multiple, NRR, Headcount efficiency |
| 7 | Serve as the **data engine** for an interactive financial dashboard |

---

## 👥 Target Group

| Role | Use Case |
|------|----------|
| **CFO / VP Finance** | Board reporting, budget approval, strategic decisions |
| **FP&A Analyst** | Monthly close, variance commentary, forecast updates |
| **Controller** | OpEx tracking, departmental budgets, accruals |
| **SaaS Founders / CEOs** | KPI monitoring, runway, growth rate health checks |
| **Investors / VCs** | Due diligence, cohort quality, unit economics review |
| **Data Engineers** | Foundation for automated finance pipelines |

---

## 📐 Scope

```
Controlling & FP&A Model
│
├── 1. Revenue Engine
│   ├── MRR Waterfall (New, Expansion, Churn, Contraction)
│   ├── ARR Calculation
│   └── Budget vs. Actuals (Revenue Variance)
│
├── 2. Customer Metrics
│   ├── Customer Count (Add / Churn)
│   ├── ARPU (Average Revenue Per Unit)
│   ├── NRR (Net Revenue Retention)
│   └── Cohort Retention Table
│
├── 3. Unit Economics
│   ├── CAC (Customer Acquisition Cost)
│   ├── LTV (Customer Lifetime Value)
│   ├── LTV:CAC Ratio
│   └── CAC Payback Period (months)
│
├── 4. P&L Summary
│   ├── Gross Profit & Gross Margin %
│   ├── OpEx by Department (S&M, R&D, G&A)
│   ├── EBITDA & EBITDA Margin %
│   └── Burn Rate
│
├── 5. Strategic KPIs
│   ├── Rule of 40 (Growth Rate + EBITDA Margin)
│   ├── Burn Multiple (Burn / Net New ARR)
│   ├── Cash Runway (months)
│   └── Revenue per Employee
│
└── 6. Forecasting
    ├── Rolling 3-Month Forecast (MRR, ARR, Customers)
    └── Confidence Levels (High / Medium / Low)
```

---

## ⚙️ Key Metrics Explained

### MRR Waterfall
```
Ending MRR = Starting MRR
           + New MRR        (new subscriptions)
           + Expansion MRR  (upsells / seat expansions)
           − Churn MRR      (cancellations)
           − Contraction MRR (downgrades)
```

### NRR (Net Revenue Retention)
```
NRR = (Starting MRR + Expansion − Contraction − Churn) / Starting MRR × 100
> 100% = growing from existing base alone (best-in-class SaaS)
```

### LTV:CAC Ratio
```
LTV = (ARPU × Gross Margin %) / Monthly Churn Rate
CAC Payback = CAC / (ARPU × Gross Margin %)   [in months]
Healthy benchmark: LTV:CAC ≥ 3:1 | Payback ≤ 18 months
```

### Rule of 40
```
Rule of 40 = MRR Growth Rate % + EBITDA Margin %
≥ 40 = healthy | ≥ 50 = excellent
```

### Burn Multiple
```
Burn Multiple = Net Cash Burned / Net New ARR
< 1 = efficient | > 2 = investigate
```

---

## 🚀 How To Use

### 1. Run the Model (zero setup)
```bash
python saas_controlling_model.py
```

### 2. Generate Full JSON Output
```python
from saas_controlling_model import run_model
results = run_model()

# Access monthly data
months = results["raw_data"]["months"]

# Access annual KPI summary
summary = results["annual_summary"]

# Access variance flags (>3% off budget)
flags = results["variance_flags"]

# Cohort retention table
cohorts = results["cohort_table"]

# Rolling forecast
forecast = results["rolling_forecast"]
```

### 3. Plug in Real Data
Replace `generate_saas_data()` with your own data connector:
```python
# Example: load from CSV
import csv
def load_from_csv(path: str) -> dict:
    with open(path) as f:
        reader = csv.DictReader(f)
        months = [row for row in reader]
    return {"company": "YourCo", "months": months}
```

### 4. Connect to Stripe / HubSpot
```python
# Coming in v1.1 — connect to Stripe MRR API
import stripe
stripe.api_key = "sk_live_..."
charges = stripe.Charge.list(limit=100)
```

---

## 🗂️ Repository Structure (Recommended)

```
saas-financial-models/
│
├── 01_controlling_fpa/
│   ├── saas_controlling_model.py   ← This file
│   ├── README.md                   ← This documentation
│   ├── dashboard.html              ← Interactive dashboard
│   └── data/
│       └── sample_data.json        ← Generated dummy data
│
├── 02_finance_operations/          ← Coming next
│   └── ...
│
└── 03_strategic_finance/           ← Coming next
    └── ...
```

---

## 📊 Benchmarks (Industry Reference)

| Metric | Seed | Series A | Series B | Public |
|--------|------|----------|----------|--------|
| MRR Growth | 15–25% | 10–20% | 8–15% | 3–8% |
| Gross Margin | 65–75% | 70–78% | 72–80% | 70–85% |
| NRR | 95–105% | 100–110% | 105–120% | 110–130% |
| LTV:CAC | 2–3x | 3–4x | 3–5x | 4–6x |
| CAC Payback | 18–24 mo | 12–18 mo | 10–15 mo | 8–12 mo |
| Rule of 40 | n/a | 20–35 | 35–50 | 40+ |
| Burn Multiple | 2–4 | 1–2 | < 1.5 | < 1 |

---

## 🔗 Related Models in This Series

| # | Model | Status |
|---|-------|--------|
| 1 | **Controlling & FP&A** ← you are here | ✅ Live |
| 2 | Finance Operations & Accounting | 🔜 Next |
| 3 | Strategic Finance & Capital Allocation | 🔜 Planned |

---

## 📚 References & Inspiration

- [Corporate Finance Institute – SaaS Financial Modeling](https://corporatefinanceinstitute.com/resources/financial-modeling/saas-financial-model/)
- [SaaS Capital – Benchmarks](https://www.saas-capital.com/research/)
- [OpenView Partners – SaaS Metrics](https://openviewpartners.com/blog/)
- [GitHub: financial-modeling topic](https://github.com/topics/financial-modeling)
- [GitHub: financial-dashboard topic](https://github.com/topics/financial-dashboard)

---

*Built with ❤️ for the SaaS finance community. PRs welcome.*
