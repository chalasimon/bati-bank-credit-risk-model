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
  ### 3. key trade-offs between using a simple, interpretable model (like Logistic Regression with WoE) versus a complex, high-performance model (like Gradient Boosting) in a regulated financial context
  
  **Simple, Interpretable Models (e.g., Logistic Regression)**
- ***Advantages:***
  - *High interpretability*: Easy to explain feature importance to stakeholders and regulators.
  - *Regulatory Compliance*: Meets Basel II’s transparency requirements.
  - *Ease of Deployment*: Faster to implement with linear data relationships.

- ***Disadvantages:***
  - *Lower Predictive Power*: Often underperforms vs. boosting models (e.g., lower AUC).
  - *Limited Flexibility*: Struggles with complex, non-linear data patterns.
  
**Complex, High-Performance Models (e.g., Gradient Boosting)**
- ***Advantages:***
  - *Higher Accuracy*: Better at predicting defaults, especially with rich datasets.
  - *Handles Complex Data*: Captures non-linear relationships and high-dimensional features.
  - *Basel II Alignment*: Supports advanced IRB approaches for risk-sensitive capital calculations.

- ***Disadvantages:***
  - *Black-Box Nature* – Hard to interpret, raising regulatory and trust concerns.
  - *Higher Compliance Costs* – Requires extensive validation and governance.
  - *Data Quality Demands* – Sensitive to noise; needs rigorous preprocessing.
  - *Bias Risks* – Opacity makes fairness harder to audit.

**Bridging the Gap: Interpretability Techniques**
  - Emerging tools (SHAP, LIME, ELI5) help explain complex models, balancing:
    - ***Performance (boosting algorithms) + Transparency (interpretability methods)***.
    - Critical for meeting Basel II’s auditability requirements while leveraging ML advancements.

**Key Takeaways:**
- Hybrid approaches (interpretable ML techniques) are increasingly vital for compliance and performance.

## Project Structure
The project is organized into several key directories and files:
- **data**: Contains the dataset used for training and testing the credit scoring model.
- **notebooks**: Jupyter notebooks for exploratory data analysis (EDA) and model development.
- **src**: Source code for data preprocessing, model training, and evaluation.
- **requirements.txt**: Python package dependencies for the project.
- **README.md**: Project documentation and instructions.
## Getting Started
To get started with the project, follow these steps:
1. Clone the repository:
    ```bash
    git clone https://github.com/chalasimon/bati-bank-credit-risk-model.git
    cd bati-bank-credit-risk-model
    ```
2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
3. Explore the Jupyter notebooks in the `notebooks` directory for data analysis and model development.
4. Run the scripts in the `src` directory to preprocess data, train models, and evaluate performance.

