import pyodbc
import pandas as pd
from sklearn import tree

con = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=SqlServerName;"
                      "Database=Learn;"
                      "Trusted_Connection=yes;")

df = pd.read_sql('SELECT * FROM TableName',con)
priceList= df['Price'].str.strip().replace(',', '',regex=True).replace("agreement","0")
ageList = df['Age'].str.strip()
df['Name']=df['Name'].str.strip()
df['Kilometer']=df['Kilometer'].str.strip()
df['Price']=list(map(int,priceList))
df["Age"]=list(map(int,ageList))
clf=tree.DecisionTreeClassifier()
clf=clf.fit(df[['Price','Age']],df[['Name','Kilometer']])
price=int(input("price(default:1000000000):").strip() or "1000000000")
age=int(input("Age(default:1400):").strip() or "1400")
while(price!=0):
    inputData=[price,age]
    answer = clf.predict([inputData])
    print(answer)
    price=int(input("price(default:1000000000):").strip() or "1000000000")
    age=int(input("Age(default:1400):").strip() or "1400")