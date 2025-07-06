# Revenue Optimization through Dynamic Pricing Strategy

This project implements a **dynamic pricing strategy** for BuildMax Rentals, a heavy equipment rental company, to optimize revenue and fleet utilization. Using a **linear programming model**, we analyzed inventory allocation and pricing strategies to balance short- and long-term rentals while maximizing profitability.

The project was developed as part of the *Pricing Analytics* module at Warwick Business School.

---

## 📂 Repository Contents

| File                              | Description                                                                                      |
|------------------------------------|--------------------------------------------------------------------------------------------------|
| `BuildMax_code_group15.py`        | Python script implementing the linear programming model for revenue optimization.                |
| `BuildMax_Data.xlsx`              | Dataset with historical rental data including inventory, demand, and pricing metrics.            |
| `Final Report_Group15.pdf`        | Detailed report outlining methodology, results, and business recommendations.                   |
| `Pricing Analytics Group 15.pdf`  | Executive summary presentation of key insights and strategies for stakeholders.                  |

---

## 📝 Project Overview

- **Objective**: Maximize revenue and ROI for BuildMax Rentals through optimal pricing and inventory allocation.  
- **Business Context**:
  - BuildMax operates across multiple locations with a fixed fleet of heavy equipment.  
  - Challenges include seasonal demand fluctuations, fleet relocation costs, and maintenance downtime.  

---

## 📊 Key Outcomes

| Metric                           | Improvement                     |
|-----------------------------------|----------------------------------|
| **Revenue Growth**               | +11.22%                         |
| **Return on Investment (ROI)**   | +15.45%                         |
| **Excavators Revenue**           | +10.14%                         |
| **Cranes Revenue**               | +12.44%                         |
| **Bulldozers Revenue**           | +10.72%                         |

- Optimized allocation between short-term and long-term rentals.  
- Implemented pricing segmentation strategies based on industry and urgency.  
- Recommended centralized inventory management for efficient fleet distribution.

---

## 🛠️ Tools & Techniques

- **Languages**: Python  
- **Libraries**: pandas, NumPy, PuLP (for linear programming)  
- **Techniques**: Dynamic Pricing, Linear Programming, ROI Analysis  
- **Visualization**: matplotlib  

---

## 📁 File Descriptions

### `BuildMax_code_group15.py`
- Implements the linear programming model:
  - Decision variables for equipment allocation.  
  - Constraints for inventory capacity and demand.  
  - Objective function to maximize weekly revenue.  

---

### `BuildMax_Data.xlsx`
- Historical dataset containing:
  - Equipment inventory levels across branches.  
  - Weekly demand for excavators, cranes, and bulldozers.  
  - Pricing data for various lease durations (1–16 weeks).  

---

### `Final Report_Group15.pdf`
- Detailed analysis covering:
  - Revenue management conditions and challenges.  
  - Optimization model formulation and results.  
  - Business implications and ROI impact.  

---

### `Pricing Analytics Group 15.pdf`
- Concise presentation for stakeholders:
  - Key findings, visualizations, and strategic recommendations.  

---

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/<yourusername>/dynamic-pricing-buildmax.git
   cd dynamic-pricing-buildmax
