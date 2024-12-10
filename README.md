# Retail Sales Analysis

## Table of Contents
  - [Project Overview](#project-overview)
  - [Data Sources](#data-sources)
  - [Tools](#tools)
  - [Data Preparation](#data-preparation)
  - [Solutions](#solutions)
  - [Recommendations](#recommendations)

    
### Project Overview:

The project is aimed to provide insights into retail sales performance of an e-commerce company with 3 months. By analysing various aspects of the data, we seek to identify trends, make data driven solutions and gain better understanding of the business performance.

### Data Sources

Sales data: Dataset was obtained from Kaggle. Data is a csv file containing sales transactions for 3 months from 3 stores in different cities.

### Tools
- Python: To import downloaded data into PostgreSQL
- PostgrSQL: Data wrangling and analysis

### Data Preparation

- Python
   - Downloaded dataset from Kaggle was read in pandas to get a quick overview.
   - Below sript was written to import the dataset into postgreSQL
      - ```python
        import pandas as pd  
        from sqlalchemy import create_engine 
        
        conn_string = 'postgresql://postgres:Onajourney123#@localhost/walmart'
        db = create_engine(conn_string)
        conn = db.connect()
        
        df = pd.read_csv('C:/Users/aniwa/OneDrive/Desktop/New World/Data Analyst Portfolio/Walmart Sales Analysis SQL/walmartsalesdata.csv')
        print(df.info)
               
        df.to_sql('walmartsalesdata', con=conn, if_exists='replace', index=False)

        ```

  - PostgreSQL
     - Created new columns 'time_of_day'. 'day_name', 'month_name' using queries
     - Used queries to update newly created columns
       - ```sql
                            -- Added new column 'time_of_day'
                -- Alter table walmartsalesdata add column time_of_day varchar(20)
                
                -- ----------------------------------------------------------------------------------
                -- Used case statement to obtain time_of_day
                -- select time,
                -- case
                -- when Time between '00:00:00' and '12:00:00' then 'Morning'
                -- when Time between '12:01:00' and '16:00:00' then 'Afternoon'
                -- Else 'Evening'
                -- End as time_of_date
                -- from walmartsalesdata
                
                -- -----------------------------------------------------------------------------
                -- Used Case statement to update the created time_of_day colum
                
                -- Update walmartsalesdata
                -- set time_of_day = (
                -- case
                -- when Time between '00:00:00' and '12:00:00' then 'Morning'
                -- when Time between '12:01:00' and '16:00:00' then 'Afternoon'
                -- Else 'Evening'
                -- End)
                
                
                -- ---------------------------------------------------------------------------------
                
                -- Add new column day of the week as day_name
                
                -- Alter table walmartsalesdata
                -- Add column day_name varchar(20)
                
                -- Extract the day name from date column and update day_name column. Because date was in string data format, used to_date to convert to date data type
                
                -- Update walmartsalesdata
                -- Set  day_name = (To_CHAR(to_date(date, 'DD/MM/YY'), 'FMDay'))
                
                --- -----------------------------------------------------------------------------------
                -- Add a new column 'month_name'
                
                -- Alter table walmartsalesdata
                -- add column month_name varchar(20)
                
                -- ----------------------------------------------------------------------------------- 
                -- Extract the month name from date column and update in the month_name column
                
                -- Update walmartsalesdata
                -- Set month_name = (to_char(to_date(date, 'DD/MM/YY'), 'Month'))
           ```

### Solutions 
  - Wrote queries to answer business question [Link to solutions](https://github.com/awahcodes/Retail-Sales-Analysis-in-SQL/blob/master/Solution%20to%20Business%20Qusetions.txt)

### Results
#### Sales
  - Most sales occurred during the evening on Sundays.
  - The store is busiest in the evening hours.

#### 


### Recommendations
  - Evaluate pricing strategies in cities with high VAT to ensure profitability remains intact.
  - Inform customers about how taxes contribute to final prices to manage expectations.
  - Consider targeting advertising efforts in cities with lower VAT to highlight competitive pricing.
  - If VAT disproportionately affects specific customer types, consider offering VAT-inclusive pricing to make costs more predictable.
  - Use the information to structure promotions or incentives for high VAT-paying customer types, emphasizing overall value rather than price.
  - Focus marketing efforts on the top revenue-generating customer type.
  - Create loyalty programs or tailored offers for these customers to increase repeat purchases.
