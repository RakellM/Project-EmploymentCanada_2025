# %%
# !pip freeze 
# !pip list --outdated
# !pip install -r requirements.txt
# !pip freeze > requirements.txt
# !pip install pymysql

# %%
## LIBRARY
#--------------------------------------
import pandas as pd
import os
import yaml

from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()

# %%
## PATH & OTHERS
#--------------------------------------
# Project Directory
project_dir = os.path.join(os.path.expanduser("~"), "OneDrive", "Nerd_Code", "Project-EmploymentCanada_2025")

# Data path
data_path = os.path.join(project_dir, "data", "raw")

# Credentials path
cred_path = os.path.join(os.path.expanduser("~"), "OneDrive", "Nerd_Code", "credentials.yaml")
# load yaml file as dictionary
CREDENTIAL = yaml.safe_load(open(cred_path))

# Database connection string
db_connection_str = f"mysql+pymysql://{CREDENTIAL['mysql_employmentca']['username']}:{CREDENTIAL['mysql_employmentca']['password']}@{CREDENTIAL['mysql_employmentca']['hostname']}/{CREDENTIAL['mysql_employmentca']['database']}"
db_connection = create_engine(db_connection_str)

# Create a connection
connection = db_connection.connect()


# %%
## DATA
#--------------------------------------
df_labor = pd.read_csv(os.path.join(data_path, '14100023/14100023.csv'))
df_labor_earnings = pd.read_csv(os.path.join(data_path, '14100223/14100223.csv'))
df_labor_ssn_adj = pd.read_csv(os.path.join(data_path, '14100287/14100287.csv'), low_memory=False)
df_undergrad = pd.read_csv(os.path.join(data_path, '37100003/37100003.csv'))
df_postgrad = pd.read_csv(os.path.join(data_path, '37100018/37100018.csv'), low_memory=False)


# %%
# Load data to MySQL
df_labor.to_sql('bronze_labor', 
                con=connection, 
                if_exists='replace', 
                index=False)

df_labor_earnings.to_sql('bronze_labor_earnings', 
                         con=connection, 
                         if_exists='replace',
                         index=False)

df_labor_ssn_adj.to_sql('bronze_labor_ssn_adj',
                        con=connection, 
                        if_exists='replace', 
                        index=False)

df_undergrad.to_sql('bronze_undergrad', 
                    con=connection, 
                    if_exists='replace', 
                    index=False)

df_postgrad.to_sql('bronze_postgrad', 
                   con=connection, 
                   if_exists='replace', 
                   index=False)

# Close the connection
connection.close()

# %%
