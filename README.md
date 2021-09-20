
# Cloud Conditions

As we know that weathers plays very important role in our life 
because the fresh oxygen which we inhale from all types trees & 
plants who help them to grow water and that water comes from rain
without rain we cannot give water to the trees and plants, same 
water we us for drinking purpose also. 

So of life depends on all the Season i.e. summer, rainy, winter,
spring. This all happen just because of different types cloud conditions.

There are many types of cloud conditions some them are as follow:
* Partly Cloudy, Overcast
* Foggy, Breezy and Dry
* Breezy and Mostly Cloudy
* Light Rain
* Clear
* Breezy and Partly Cloudy
* Breezy and Overcast
* Humid and Mostly Cloudy
* Mostly Cloudy
* Humid and Partly Cloudy
* Windy and Foggy
* Windy and Overcast
* Windy and Partly Cloudy
* Breezy
* Dry and Partly Cloudy
* Windy and Mostly Cloudy
* Dangerously Windy and Partly Cloudy
* Dry
* Windy
* Humid and Overcast
* Breezy and Foggy
* Drizzle
* Windy and Dry
* Dry and Mostly Cloudy
## Data Analysis

In Cloud Condition dataset we have 73 features(including target 
variable) and 855969 records.

* Cloud_Condition : All the types of Cloud Condition
* Rain_OR_SNOW : wheather the its Rainning or snowning
* Temperature (C) : Temperaturein degree celcius
* Apparant Temperature (C) : Apparent temperature is the 
  equivalent perceived by humans
* Humidity : Humidity is the amount of water vapor in the air
* Wind Speed (km/h) : Speed of winf in km/hr.
* Wind Bearing (degrees) : Wind Bearing in degree.
* Visibility (km) : Visibilityin kilometer
* Pressure (millibars) :Sea level pressure
* Condensation : water which collects as droplets on a cold surface when humid air is in contact with it.
* Solar irradiance intensity : Solar irradiance is the power per unit area received from the Sun in the form of electromagnetic radiation
## Approach

Our Main goal is to know that whether which Cloud condition 
it belong to.

* Data Exploration : Exploring dataset using pandas, numpy, matplotlib and seaborn.
* Data visualization : Use Tableau Data visualizationtools and also Ploted graphs to get insights about dependend and independed variables.
* Model Selection I : Tested all base models to check the base accuracy. Also ploted and calculate Performance Metrics to check whether a model is a good fit or not.
* Model Selection II : After testing all base if some of them are not working properly then we have to do model tunning. 
* Pickle File : Selected model as per best accuracy and created pickle file using pickle library.
* Webpage & deployment : Created a webform that takes all the necessary inputs from user and shows output. After that I have deployed project on Herokuapp. 

## Technologies Used

* Jupyter notebook, Spyder, VScode Is Used For IDE.
* For Visualization Of The Plots Matplotlib , Seaborn Are Used.
* Herokuapp is Used For Model Deployment.
* Front End Deployment Is Done Using HTML, CSS, Bootstrap.
* Flask is for creating the application server and pages.
* Git Hub Is Used As A Version Control System.
* os is used for creating and deleting folders.
* csv is used for creating .csv format file.
* numpy is for arrays computations and mathematical operations
* pandas is for Manipulation and wrangling structured data
* scikit-learn is used for machine learning tool kit
* pickle is used for saving model
* Decision Tree is used for DecisionTreeClassifier Implementation.
* Random Forest is used for RandomForestClassifier Implementation.
* Extra tree is used for ExtratreesClassifier Implementation.
  
## Deployment

**Herokuapp Link:** https://cloud-condition-webapplication.herokuapp.com/
  
## Deployment

To Clone this project run

```bash
git clone https://github.com/vish-68/Cloud-Conditions
```
Go to Project directory
```bash
cd Cloud-Conditions
```
Install dependencies
``` bash
pip install -r requirements.txt
```  
Run the app.py
```bash
python app.py
```
## Conclusion

We developed Cloud condition model which is capable to predict
the conditions of clouds. In this dataset 12 features(including 
target variable). 
* Our 1st step is to import dataset and check all
  the details like shape, info(), describe() for getting better knowledge
  about data or each variable.
* 2nd step is to checking missing value and datatype of missing variable
  by looking at info(). after that we have to delete those 
  variable whose missing value is more than 50% of data. Other 
  variable should be treat as repect to their datatype
* 3rd step After handling all this we have to do data 
  visualization for getting some insight for eg. we have to check 
  for ouliers, imbalanced variable or imbalanced data so wre have to 
  remove ouliers or do upsampling for those here we don upsampling 
  for "RAIN_Or_SNOW" variable.
* 4th step we have group all the same kinds of cloud condition in one groups
* 5th step converting all categorical variable into numerical eg RAIN_Or_SNOW, Condensation and Cloud Conddition
* 6th step Splitting data into training and validation data and building 
  different ML model like Decision Tree, Random Forest, Extra Tree. 
  Out of all Extra tree is working properly.
* Last step is model Deployment using Flask Framework.
  For model deployment we have to dump our model using pickle library
  and can save our model in .pkl or .sav extension.
