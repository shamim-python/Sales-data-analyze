
'''Project title: Clean & Analyze Sales Data(No Visualization) '''
import pandas as pd
#1. Read the csv file
df=pd.read_csv('client style.csv')
print(df)
#2.Drop rows with missing Order ID, Quantity,or Price
dp=df.dropna(subset=["Order ID","Quantity Ordered","Price Each"])

#3. Convert 'Order Date' to dtaetime,errors='coerce' to handle invalid dates
dp["Order Date"]=pd.to_datetime(dp["Order Date"],errors='coerce')

#4.Drop rowse where data conversion failed(NaT)
dp=dp.dropna(subset=["Order Date"])

#5. Convrt Quantity and price to numeric
dp["Quantity Ordered"]=pd.to_numeric(dp["Quantity Ordered"])

dp["Price Each"]= pd.to_numeric(dp["Price Each"])

#6 calculate Total price
dp["Total Price"]=dp["Quantity Ordered"] * dp["Price Each"]

#7 Group by product to find total quantity 
top_products=df.groupby("Product")["Quantity Ordered"].sum().sort_values(ascending=False)

print('Cleaned Data')
print("\nTop 3 Besttselling Products:")
print(top_products.head(3))
