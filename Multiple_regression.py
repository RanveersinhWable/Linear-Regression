import pandas #Used for reading the csv file
from sklearn import linear_model #Used for regression
data = pandas.read_csv('data.csv') #reading csv file
def encode(company,car): #for encoding
    data['need'] = 0 #Additional column ('need')
    count = 0; ist = 0
    for i in data['Company']:
       if (i == company):
            if (data['Car'][count] == car):
               data.loc[count , 'need'] = '1' #loc so that we can give a value 1 to column need and row count
               ist = ist + 1;
       count = count + 1
    if (ist == 0): #Checking if the requirement exists
        print("Company or car name not in CSV file!")
        exit()
print(data,"\n")
print("From above table:-\n")
company = input("Enter the car company name :") #taking inputs
car = input("Enter the car name :")
vol = float(input("Enter any volume(integer/decimal value) of your choice : "))
encode(company,car)
X = data[['need','Volume']] #considering 2 columns (intput columns) of the table
y = data['CO2'] #considering the output column of the table (or the output data to be shown)
regr = linear_model.LinearRegression() #linear regression variable is declared
regr.fit(X.values,y.values) #linear regression applied on values of X and y
predict = regr.predict([[1,vol]]) #Predicting the output for value 1 of 'need' column at a specific volume (it return the y value i.e CO2 emission and saved in predict)
data['need'] = 0 #need column made 0
print("CO2 emission is :",predict) #printing the predicted value




