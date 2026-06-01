# online-retail-data-analysis
Data analytics pipeline for an online retail dataset featuring cleaning, aggregation, outlier detection, and hypothesis testing
This project demonstrates an end-to-end data analysis workflow using Python, Pandas, SciPy, and Matplotlib on a real-world e-commerce transaction dataset.

The goal was to transform raw retail transaction data into actionable business insights through data cleaning, feature engineering, statistical analysis, and visualization.

Skills Demonstrated
Data Cleaning & Preprocessing
Missing Value Handling
Feature Engineering
Exploratory Data Analysis (EDA)
Data Aggregation with Pandas
Pivot Tables & GroupBy Operations
Statistical Hypothesis Testing
Outlier Detection using Z-Scores
Data Visualization
Vectorized Data Processing
Dataset

Online Retail Dataset II

The dataset contains transactional records from a UK-based online retailer, including:

Invoice information
Product details
Customer IDs
Purchase quantities
Transaction dates
Unit prices
Customer countries
Project Workflow
1. Data Cleaning
Identified missing values
Removed records with missing customer IDs
Forward-filled missing date values
Separated product returns from completed sales transactions
Converted date fields into proper datetime format
2. Feature Engineering
Created Total_Spent metric
Extracted Month and DayOfWeek features
Categorized countries into business regions
3. Business Analytics
Identified top-spending customers
Generated sales trend analyses
Built pivot-table summaries
Calculated regional pricing metrics
4. Statistical Analysis
Detected transaction outliers using Z-Scores
Performed Independent T-Test comparing UK and European customer spending
Evaluated statistical significance at the 95% confidence level
Technologies Used
Python
Pandas
NumPy
SciPy
Matplotlib
Visualizations

The project includes:

Sales trend analysis visualization
Outlier detection scatter plot
