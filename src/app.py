import pandas as pd
from utils import db_connect
engine = db_connect()

# your code here
engine
if engine:
    print("Conexión exitosa")

data = pd.read_csv('https://raw.githubusercontent.com/4GeeksAcademy/linear-regression-project-tutorial/main/medical_insurance_cost.csv')
data.to_sql('tabla seguro', engine, if_exists='replace', index=False)