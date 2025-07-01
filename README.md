# Credit Risk Modeling Project for Bati Bank
Bati Bank, a leading financial services provider with 10+ years of experience, is partnering with an eCommerce company to offer a buy-now-pay-later (BNPL) service. This project aims to develop a Credit Scoring Model using eCommerce data to predict the likelihood of customer defaults.

## Credit Scoring Business Understanding.
The goal is to create a model that can accurately predict the probability of a customer defaulting on their BNPL payments. This will help Bati Bank make informed lending decisions and manage risk effectively.
### 1. Basel II Accord and Model Requirements
The Basel II Accord enhances banking stability by enforcing stricter risk measurement, capital adequacy, and transparency in credit risk models. Its influence on interpretability and documentation includes:
- **Advanced Risk Measurement:**
    - Encourages Internal Ratings-Based (IRB) approaches, where banks use internal models to estimate Probability of Default (PD), Loss Given Default (LGD), and Exposure at Default (EAD)
    - Requires transparent, well-documented models for regulatory approval, especially under the Advanced IRB (AIRB) framework.

- **Supervisory Review:**
    - Mandates Internal Capital Adequacy Assessment Process (ICAAP), subject to regulatory scrutiny
    - Models must be auditable, well-governed, and clearly documented for supervisory validation.

- **Trust & Accountability:**
    - *Interpretability* is critical—risk officers and regulators must understand model logic to prevent bias, ensure fairness, and maintain trust.
    - Complex models (e.g., machine learning) face adoption barriers if they lack explainability.

- **Operational Implementation:**
    - Banks and fintechs (e.g., online lenders) now design models with explainable outputs (e.g., "Strengths and Weaknesses Analysis") for faster, compliant decision-making.
### 2. Proxy Variables in Credit Scoring
**Why Use a Proxy Variable?**
- ***No Direct Default Data Available***: For MSMEs (Micro-, Small, and Medium-sized Enterprises), traditional loan default records are often missing. Alternative data (e.g., transaction history) may not include actual defaults.
- ***Feasibility in Early Testing***: In proof-of-concept (POC) studies, proxies (e.g., late service payments) allow model development before real loan performance data exists.

**Business Risks of Proxy-Based Predictions**

***Accuracy Mismatch***:
  - A proxy (e.g., late utility payments) may not perfectly predict actual loan defaults, leading to higher risk or missed opportunities.

***Limited Model Scope***:
  - Proxies may restrict models to "pre-screening" rather than true default prediction.

***Data Quality & Bias Risks***:
  - Poor proxy relevance can weaken model reliability.
  - Proxies may introduce unintended bias (e.g., unfairly penalizing certain groups).

***Regulatory & Trust Challenges***:
  - Basel II requires transparent, interpretable models. Proxies complicate validation if their link to real risk is unclear.
  - Lenders may distrust models based on non-intuitive proxies.

