# Supervised ML Project-4

Project Description

With the pandemic subsiding slowly, people are excited about travel and outdoor activities. Our project focused analyzing historical hourly weather data to develop a weather prediction tool. 
This tool predicts the weather based on user inputs and provides recommendations for planning outdoor activities according to the predicted weather.
For this pilot project, our team selected historical weather data between 2015-2018 for one city in Spain (Valencia) to build and test the tool. 
As historical data was readily available, our team chose supervised machine learning to build the prediction tool 

Data Source  
https://www.kaggle.com/datasets/nicholasjhana/energy-consumption-generation-prices-and-weather?resource=download&select=weather_features.csv
![image](https://user-images.githubusercontent.com/95728097/174938724-f3584b7b-30bf-4843-9f74-ecc29f99af83.png)

![image](https://user-images.githubusercontent.com/95728097/174938752-e72ce8fd-87b9-403a-bc92-5d491737b4b3.png)
![image](https://user-images.githubusercontent.com/95728097/174938769-78e055a0-b8e6-4025-9606-d6f975a64bfd.png)

The available dataset contained four years (2015 till 2018)  of hourly weather data that used to describe the weather (shown in the figure):

Avg Temp
Min Temp
Max Temp
Pressure 
Humidity 
Wind speed 
Wind degree
Rain 1h
Rain 3h
Cloud cover
We decided to keep the outliers in the data![image](https://user-images.githubusercontent.com/95728097/174938799-95cdb2b5-c7a2-46bc-83b3-ce1d2810daf3.png)

This data was imbalanced, meaning, 85 % of the data is either clear or cloudy for the City of Valencia. 
Due to processing speed and memory size constraint only Valencia city data is used for prediction. 
Valencia data contains 34k total rows 
clouds                      17346
clear                       15535
rain                          796
mist                          190
thunderstorm                  169
drizzle                        58
fog                            42
smoke                           6
haze                            3
Data Clean Up Steps: 
Removed the data with  null values.
Dropped columns not relevant to ML 
development.
Saved the data to SQL – Postgres database.
![image](https://user-images.githubusercontent.com/95728097/174938817-2f3532af-034a-4034-ae36-14fa9a15ae31.png)

Retrieve data from Postgres
Independent Variables (X):
Data type: Numeric
Use filter-based Feature Selection method to choose relevant features
Used Standard Scaler to scale the input (X)
Dependent Variable (Y):
 Data type: String
Used Label Encoder to encode categorical data to numeric values
ML Models:
Used Random Forest Classifier with and without  feature selection
Used Logistic Regression with and without feature selection
Used Support Vector Machine (non-linear kernels)
Polynomial
Gaussian radial basis function (rbf)
Hyperparameter tuning
![image](https://user-images.githubusercontent.com/95728097/174938883-ac020860-230b-40b8-8419-b0885ddd800b.png)

![image](https://user-images.githubusercontent.com/95728097/174938935-238fd2a6-303a-4496-9bc7-a40f83fa61b4.png)

Data Rendering:  
A html webpage calls a flask application which scales the input ( weather features ) and then sends the data to Model. 
Model then predicts the weather which is rendered on  html page. 

Data Visualization : 
Tableau is used for data insights and for historical weather trend analysis.
Tableau report is published and is embedded in html to render weather trends. 
![image](https://user-images.githubusercontent.com/95728097/174938967-c1158e94-dcdd-461d-9604-dd2869a8170c.png)

Limitations and Future Analysis

To avoid imbalanced data either drop the minority data (count < 1%)  or use the SMOTE method to balance the data.
SMOTE is an algorithm that performs data augmentation by creating synthetic data points based on the original data points.
ANOVA technique to check the impact of the features by comparing the means of different samples
Weather parameters available in the dataset were in SI units, may need to convert data to locally used units
Using SVM with Hyperparameter tuning required high processing time (500 iterations)
Scaling the model to include more cities and using current weather data
We completed the ETL process for the energy consumption dataset but due to time constraint, we decided to drop it from the scope. Future analysis can include using historical weather and energy consumption data to predict energy pricing
![image](https://user-images.githubusercontent.com/95728097/174938983-ec5f2f2e-6cca-4277-bc0b-2ec901aba0b4.png)

