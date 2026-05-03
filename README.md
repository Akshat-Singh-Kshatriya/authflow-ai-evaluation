# AuthFlow: AI Prior Authorization System

## Project Overview
AuthFlow is a multi-agent system developed to automate medical prior authorization workflows. By breaking clinical reviews into structured sub-tasks, the system analyzes 1,300 claims to evaluate decision accuracy and consistency while mitigating clinical and financial risk.

## Key Results & Impact
* **High Decision Precision**: Achieved a **95.6% final decision accuracy** across complex medical claims.
* **Structured Review**: Delivered **86.2% checklist-level accuracy** by decomposing clinical reviews into granular sub-tasks.
* **Risk Mitigation**: Successfully identified high-risk outliers (e.g., high-BMI smokers) and implemented a mandatory **Human-in-the-loop** review threshold at **0.70 confidence**.
* **Stakeholder Alignment**: Developed financial dashboards showing regional accuracy trends and cost-per-claim impact to support phased deployment.

## Technical Implementation
* **Language**: Python.
* **Engine**: Multi-agent LLM logic that processes claims data and compares AI outputs against clinical ground truth.
* **SQL Analytics**: Benchmarked LLM performance across different geographic regions and identified cost-variance in claim approvals.
* **Visual Risk Analysis**: Used Seaborn to visualize the distribution of confidence scores and isolate cases where model uncertainty posed financial risk.

## Performance Summary
| Metric | Result |
| :--- | :--- |
| **Total Claims Analyzed** | 1,300 |
| **Final Decision Accuracy** | 95.6% |
| **Checklist-Level Accuracy** | 86.2% |
| **Human Review Threshold** | Confidence Score < 0.7 |
