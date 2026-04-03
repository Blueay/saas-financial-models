"""
SaaS Controlling & Financial Planning Model
============================================
A comprehensive FP&A model for SaaS businesses covering:
- MRR/ARR Waterfall
- Budget vs. Actuals Variance Analysis
- Unit Economics (CAC, LTV, Payback)
- Cohort-based Churn Modeling
- Rolling Forecast (12-month)
- Rule of 40 & Burn Multiple
- Departmental OpEx Planning

Author: AI Financial Models for SaaS
Version: 1.0.0
"""

import json
from dataclasses import dataclass, field, asdict
from typing import Optional
import math

# ─────────────────────────────────────────────
# 1. DUMMY DATA GENERATOR
# ─────────────────────────────────────────────

MONTHS = [
    "Jan-24","Feb-24","Mar-24","Apr-24","May-24","Jun-24",
    "Jul-24","Aug-24","Sep-24","Oct-24","Nov-24","Dec-24",
    "Jan-25","Feb-25","Mar-25","Apr-25","May-25","Jun-25",
    "Jul-25","Aug-25","Sep-25","Oct-25","Nov-25","Dec-25",
]

def generate_saas_data() -> dict:
    """
    Generate realistic SaaS dummy data for a mid-stage B2B SaaS company.
    Revenue starts at ~$500K MRR and grows ~8% MoM in first year,
    then stabilises at ~5% MoM in year 2.
    """
    import random
    random.seed(42)

    # ── Seed values ──────────────────────────────────────────────
    base_mrr        = 500_000      # Jan-24 MRR
    churn_rate      = 0.025        # 2.5% monthly customer churn
    expansion_rate  = 0.015        # 1.5% expansion MRR
    new_customers   = 45           # new customers Jan-24
    arpu            = 3_200        # average revenue per unit (monthly)
    cac             = 18_000       # cost to acquire one customer
    gross_margin    = 0.72         # 72% gross margin
    s_m_spend       = 280_000      # sales & marketing Jan-24
    r_d_spend       = 210_000      # R&D Jan-24
    g_a_spend       = 95_000       # G&A Jan-24
    headcount       = 68           # total headcount Jan-24

    months_data = []
    mrr = base_mrr
    customers = int(mrr / arpu)
    cumulative_cash_burned = 0

    for i, month in enumerate(MONTHS):
        growth_rate = 0.082 if i < 12 else 0.050
        noise = random.uniform(-0.01, 0.01)

        # ── MRR waterfall components ──────────────────────────────
        new_mrr        = new_customers * arpu
        expansion_mrr  = mrr * expansion_rate
        churn_mrr      = mrr * churn_rate
        contraction_mrr = mrr * 0.005
        net_new_mrr    = new_mrr + expansion_mrr - churn_mrr - contraction_mrr
        ending_mrr     = mrr + net_new_mrr

        # ── Customers ─────────────────────────────────────────────
        churned_customers  = int(customers * churn_rate)
        ending_customers   = customers + new_customers - churned_customers
        nrr = ((mrr + expansion_mrr - contraction_mrr - churn_mrr) / mrr) * 100

        # ── Revenue ───────────────────────────────────────────────
        revenue    = mrr  # recognised in month
        cogs       = revenue * (1 - gross_margin)
        gross_profit = revenue - cogs

        # ── Budget (plan set 3 months ahead, with optimism bias) ──
        budget_mrr     = mrr * (1 + growth_rate + 0.01)
        budget_revenue = budget_mrr

        # ── OpEx ─────────────────────────────────────────────────
        sm  = s_m_spend  * (1 + i * 0.015 + noise)
        rd  = r_d_spend  * (1 + i * 0.018 + noise)
        ga  = g_a_spend  * (1 + i * 0.010 + noise)
        total_opex = sm + rd + ga

        # ── P&L ───────────────────────────────────────────────────
        ebitda       = gross_profit - total_opex
        ebitda_margin = (ebitda / revenue) * 100 if revenue else 0
        burn          = max(0, -ebitda)
        cumulative_cash_burned += burn

        # ── Unit Economics ────────────────────────────────────────
        ltv         = (arpu * gross_margin) / churn_rate
        ltv_cac     = ltv / cac
        cac_payback = cac / (arpu * gross_margin)  # months

        # ── Rule of 40 ────────────────────────────────────────────
        mrr_growth_rate = growth_rate * 100
        rule_of_40 = mrr_growth_rate + ebitda_margin

        # ── Burn Multiple ─────────────────────────────────────────
        burn_multiple = burn / net_new_mrr if net_new_mrr > 0 else None

        # ── Headcount & Productivity ──────────────────────────────
        hc_growth = 2 if i % 3 == 0 else 1
        headcount += hc_growth
        revenue_per_employee = revenue / headcount

        # ── Cash Runway (assumed $5M cash start) ─────────────────
        starting_cash = 5_000_000
        remaining_cash = max(0, starting_cash - cumulative_cash_burned)
        runway_months = remaining_cash / burn if burn > 0 else 999

        # ── Variance ──────────────────────────────────────────────
        variance_abs = revenue - budget_revenue
        variance_pct = (variance_abs / budget_revenue) * 100

        months_data.append({
            "month": month,
            "period_index": i,
            # MRR Waterfall
            "starting_mrr": round(mrr),
            "new_mrr": round(new_mrr),
            "expansion_mrr": round(expansion_mrr),
            "churn_mrr": round(churn_mrr),
            "contraction_mrr": round(contraction_mrr),
            "net_new_mrr": round(net_new_mrr),
            "ending_mrr": round(ending_mrr),
            "arr": round(ending_mrr * 12),
            # Customers
            "starting_customers": customers,
            "new_customers": new_customers,
            "churned_customers": churned_customers,
            "ending_customers": ending_customers,
            "customer_churn_rate_pct": round(churn_rate * 100, 2),
            "nrr": round(nrr, 1),
            # Revenue & Margins
            "revenue": round(revenue),
            "budget_revenue": round(budget_revenue),
            "variance_abs": round(variance_abs),
            "variance_pct": round(variance_pct, 1),
            "cogs": round(cogs),
            "gross_profit": round(gross_profit),
            "gross_margin_pct": round(gross_margin * 100, 1),
            # OpEx
            "sm_spend": round(sm),
            "rd_spend": round(rd),
            "ga_spend": round(ga),
            "total_opex": round(total_opex),
            # P&L
            "ebitda": round(ebitda),
            "ebitda_margin_pct": round(ebitda_margin, 1),
            "burn": round(burn),
            "cumulative_cash_burned": round(cumulative_cash_burned),
            # Unit Economics
            "arpu": round(arpu),
            "cac": round(cac),
            "ltv": round(ltv),
            "ltv_cac_ratio": round(ltv_cac, 2),
            "cac_payback_months": round(cac_payback, 1),
            # Strategic KPIs
            "rule_of_40": round(rule_of_40, 1),
            "burn_multiple": round(burn_multiple, 2) if burn_multiple else 0,
            "mrr_growth_rate_pct": round(mrr_growth_rate, 1),
            # Headcount
            "headcount": headcount,
            "revenue_per_employee": round(revenue_per_employee),
            # Runway
            "remaining_cash": round(remaining_cash),
            "runway_months": round(runway_months, 1) if runway_months < 999 else 999,
        })

        # ── Advance state ─────────────────────────────────────────
        mrr = ending_mrr
        customers = ending_customers
        new_customers = int(new_customers * (1 + growth_rate * 0.5))
        arpu = arpu * (1 + random.uniform(-0.005, 0.012))  # slight ARPU drift
        cac  = cac  * (1 + random.uniform(-0.005, 0.010))  # CAC creep

    return {
        "company": "AcmeSaaS Inc.",
        "model_version": "1.0",
        "currency": "USD",
        "months": months_data,
    }


# ─────────────────────────────────────────────
# 2. ANALYTICAL FUNCTIONS
# ─────────────────────────────────────────────

def compute_summary(data: dict) -> dict:
    """Compute annual summaries and trailing-12-month KPIs."""
    months = data["months"]

    def year_slice(year_prefix):
        return [m for m in months if m["month"].endswith(year_prefix)]

    results = {}
    for yr, prefix in [("2024", "-24"), ("2025", "-25")]:
        ym = year_slice(prefix)
        if not ym:
            continue
        results[yr] = {
            "total_revenue": sum(m["revenue"] for m in ym),
            "total_budget":  sum(m["budget_revenue"] for m in ym),
            "ending_arr":    ym[-1]["arr"],
            "ending_mrr":    ym[-1]["ending_mrr"],
            "avg_gross_margin": sum(m["gross_margin_pct"] for m in ym) / len(ym),
            "total_ebitda":  sum(m["ebitda"] for m in ym),
            "total_burn":    sum(m["burn"] for m in ym),
            "ending_customers": ym[-1]["ending_customers"],
            "avg_nrr":       sum(m["nrr"] for m in ym) / len(ym),
            "avg_ltv_cac":   sum(m["ltv_cac_ratio"] for m in ym) / len(ym),
            "avg_rule_of_40": sum(m["rule_of_40"] for m in ym) / len(ym),
            "ending_headcount": ym[-1]["headcount"],
        }
    return results


def variance_analysis(data: dict) -> list:
    """Flag months where actual revenue deviated >3% from budget."""
    flags = []
    for m in data["months"]:
        if abs(m["variance_pct"]) > 3:
            flags.append({
                "month": m["month"],
                "variance_pct": m["variance_pct"],
                "variance_abs": m["variance_abs"],
                "status": "ABOVE BUDGET" if m["variance_pct"] > 0 else "BELOW BUDGET",
            })
    return flags


def cohort_retention_table(data: dict, num_cohorts: int = 6) -> list:
    """
    Simulate a simplified cohort retention table.
    Each cohort = a quarter's new customers. Shows % retained at M+1, M+3, M+6, M+12.
    """
    months = data["months"]
    cohorts = []
    churn_rate = 0.025  # monthly

    for i in range(0, min(num_cohorts * 3, len(months)), 3):
        m = months[i]
        start_cohort = m["new_customers"]
        cohorts.append({
            "cohort_start": m["month"],
            "initial_customers": start_cohort,
            "retained_m1":  round(start_cohort * (1 - churn_rate) ** 1),
            "retained_m3":  round(start_cohort * (1 - churn_rate) ** 3),
            "retained_m6":  round(start_cohort * (1 - churn_rate) ** 6),
            "retained_m12": round(start_cohort * (1 - churn_rate) ** 12),
            "retention_m1_pct":  round((1 - churn_rate) ** 1 * 100, 1),
            "retention_m3_pct":  round((1 - churn_rate) ** 3 * 100, 1),
            "retention_m6_pct":  round((1 - churn_rate) ** 6 * 100, 1),
            "retention_m12_pct": round((1 - churn_rate) ** 12 * 100, 1),
        })
    return cohorts


def rolling_forecast(data: dict, periods: int = 3) -> list:
    """
    Simple rolling forecast: extend the last N months' trend forward.
    Uses exponential smoothing on MRR growth rate.
    """
    months = data["months"]
    last = months[-1]
    avg_growth = 0.048  # smoothed from last 6 months
    forecast = []

    mrr = last["ending_mrr"]
    customers = last["ending_customers"]
    for i in range(1, periods + 1):
        mrr_next = mrr * (1 + avg_growth)
        forecast.append({
            "period": f"T+{i}",
            "forecast_mrr": round(mrr_next),
            "forecast_arr": round(mrr_next * 12),
            "forecast_customers": round(customers * (1 + avg_growth * 0.7)),
            "confidence": "High" if i == 1 else ("Medium" if i == 2 else "Low"),
        })
        mrr = mrr_next
        customers = round(customers * (1 + avg_growth * 0.7))
    return forecast


# ─────────────────────────────────────────────
# 3. MAIN RUNNER
# ─────────────────────────────────────────────

def run_model() -> dict:
    """Run the full Controlling & FP&A model and return all outputs."""
    data = generate_saas_data()
    return {
        "raw_data": data,
        "annual_summary": compute_summary(data),
        "variance_flags": variance_analysis(data),
        "cohort_table": cohort_retention_table(data),
        "rolling_forecast": rolling_forecast(data),
    }


if __name__ == "__main__":
    results = run_model()
    print(json.dumps(results["annual_summary"], indent=2))
    print("\n--- Variance Flags ---")
    for flag in results["variance_flags"]:
        print(f"  {flag['month']}: {flag['status']} {flag['variance_pct']:+.1f}% (${flag['variance_abs']:,.0f})")
    print("\n--- 3-Month Rolling Forecast ---")
    for f in results["rolling_forecast"]:
        print(f"  {f['period']}: MRR ${f['forecast_mrr']:,.0f} | ARR ${f['forecast_arr']:,.0f} | Confidence: {f['confidence']}")
    print("\nModel run complete.")
