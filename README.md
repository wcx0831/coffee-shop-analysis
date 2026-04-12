1. Problem Definition and User
-Business Problem
Coffee shop owners face multiple operational challenges: inefficient staffing due to unclear peak hours, blind inventory planning without product performance insights, and ineffective marketing due to unknown seasonal trends.
-Target User
This project is designed for small to medium coffee shop owners and operators, providing data-driven insights to optimize daily operations and boost revenue.
 -Project Goal
Through analyzing coffee shop sales data,the project identify peak sales periods, top-performing products, customer behavior patterns, and seasonal trends, and finally deliver actionable operational recommendations.

2. Data Relevance & Source
 -Dataset Fields
 hour_of_day: Transaction hour (for peak hour analysis)
 cash_type: Payment method (for customer behavior analysis)
 money: Sales revenue (for revenue calculation)
 coffee_name: Coffee product type (for product performance analysis)
 Time_of_Day: Time period (Morning/Afternoon/Night, for operational planning)
 Weekday: Transaction weekday (for weekly trend analysis)
 Month_name: Transaction month (for seasonal analysis)
 -Data Relevance
This dataset is 100% relevant to the project goal:
- Time-related fields directly enable peak hour, weekly, and seasonal sales analysis, solving staffing and marketing challenges.
- Product and revenue fields allow us to identify top-selling and high-revenue items, supporting inventory and menu optimization.
- Payment method data reveals customer payment preferences, ensuring stable digital payment operations.
- The dataset covers all core operational dimensions of a coffee shop, providing a complete foundation for data-driven decision-making.

3. Methods
- Data cleaning and preprocessing with Pandas
- Exploratory data analysis (EDA)
- Data visualization with Matplotlib and Seaborn
- Business insight extraction and recommendation generation

4. Key Findings
-Product Performance: Latte is the highest-revenue product, while Americano with Milk is the most frequently ordered.
-Peak Hours: The daily sales peak is at 10:00 AM, with revenue evenly distributed across morning, afternoon, and night periods.
-Weekly/Monthly Trends: Tuesday is the highest-sales day, Sunday is the lowest; March is the peak season, April is the off-season.
-Payment Behavior: 100% of transactions are via card, requiring stable digital payment infrastructure.

5. How to Run
-Open "coffee_sales_analysis.ipynb" in Jupyter Lab/Jupyter Notebook
-Run all cells sequentially to reproduce the analysis and visualizations
-View the final conclusion and recommendations at the end of the notebook

6. Demo Video
[https://www.bilibili.com/video/BV1wkDQBVEoF/?vd_source=130568a0c42f61c2ac5e423b84506188]

7. Limitations
- The dataset only includes one coffee shop's data, limiting the generalizability of insights.
- No cost data is available, so profit analysis cannot be performed.

8.Next Steps
- Integrate multi-store data for comparative analysis
- Add cost data to conduct profit margin analysis
- Develop a predictive model for future sales forecasting
