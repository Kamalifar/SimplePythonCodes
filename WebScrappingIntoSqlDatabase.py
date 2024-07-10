from bs4 import BeautifulSoup
import requests
import pyodbc
import pandas

carBrand=input("Please enter your car brand:(toyota,bmw,...)").lower()
pages=int(input("Howmany pages do you like to get?"))

con = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=SqlServerName;"
                      "Database=Learn;"
                      "Trusted_Connection=yes;")

for pageNumber in range(1,pages+1):
    content=requests.get("https://www.OneUrlForExample....com/used-cars-for-sale/listings/"+carBrand+"?page="+str(pageNumber))

    if content.status_code!=200:
        print("The url address didn't any response.")
        con.close()
        break
    else:
        bs=BeautifulSoup(content.text,"html.parser")
        cars=bs.find_all("div",attrs={"data-test":"usedListing"})
        cursor=con.cursor()
    
        for car in cars:
            name=car.find("div",attrs={"data-test":"vehicleCardTrim"})
            price=car.find("span",attrs={"data-test":"vehicleCardPriceLabelAmount"})
            kilometer=car.find("div",attrs={"data-test":"vehicleMileage"})
            model=name.text.split(' ',1)[0]
            cursor.execute("INSERT INTO TableName VALUES ('%s','%s','%s','%s')" % (str.replace(name.text,chr(39),"`"),price.text,kilometer.text,model))
        cursor.commit()
con.close()
    
# df=pandas.DataFrame({"name":names,"price":prices,"kilometer":kilometers})
