# Ji Hwan KIM Intel Portfolio
### Live Demo at: https://jihwankimqd.github.io/jhkintelportfolio/

This is the deployment version of the Portfolio intel repository. For a version which only supports local development, check [Here](https://github.com/jihwankimqd/PortfolioIntel).

## Tools/Technologies Used
Frontend: Vue.js  
Backend: Python, Flask  
Database: MongoDB

## Guide
This fullstack web application is a portfolio which contains 5 differnt sections which can be accessed in the HOME page or using the Navbar. The application is divided into:
1. Home
2. About
3. Chartjs
4. Dashboard
5. Projects

## Home
![Alt Text](https://raw.githubusercontent.com/jihwankimqd/PortfolioIntel/master/HOME.gif)  
  
A landing page with smooth scrolling, and hover effects made with Vue components and CSS. Other sections of the webapp can be accessed by clicking the references.

## About
![Alt Text](https://raw.githubusercontent.com/jihwankimqd/PortfolioIntel/master/ABOUT.gif)  
  
An about page with hardcoded information about myself.

## Chartjs
![Alt Text](https://raw.githubusercontent.com/jihwankimqd/PortfolioIntel/master/CHARTJS.gif)  
  
Can pick a desired chart type (from Chartjs), and the page will send a response to the server (Python and Flask based, deployed on Heroku), which will then send a request to the database (MongoDB), which then sends the chart data back to the server which is received on the frontend. It is made using REST API, and can send requests to add/delete new data to/from the database. The data can be inserted into the forms, which will have example values by default. To add new data, simply type in the desired values (keep the same format as the examples). If the data doesn't exist in the database, the data is added. To delete a data, type in the data (exact values), and the data will be deleted. The charts will then dynamically reload when a change in the data is detected. Initially, it may take some time for the data to load (especially for Line and Bar Charts due to their large amounts of data), because the server is hosted (for free) on Heroku. For faster speeds, you can clone the repo and run the webapp locally (refer below).

## Dashboard
![Alt Text](https://raw.githubusercontent.com/jihwankimqd/PortfolioIntel/master/DASHBOARD.gif)  
  
A **Machine Learning Dashboard**, which shows multiple charts of stock data. The three charts above show analysed data, and the single chart below shows the predicted price for a given stock. The stock symbol should be entered instead of the name  
(e.g 삼성전자(x) 005930(o), SK이노베이션(x) 096770(o) ).  
**Click Process Data/Process Data Machine Learning First** and then wait for the loading screen to finish and the webpage should give an alert when the loading is completed. **Then, click Update Chart/Update Chart Machine Learning** to update the charts. The process may take some time, because the server is deployed (for free) on Heroku, which is not very fast. To experience faster loading time, clone/download the repository and run the files locally.  
When **Process Data** is clicked, the input stock symbol (e.g. '096770') is sent the the server which runs a python script to scrape the data and clean it. Numerous features are gathered (Stock Data, Dow Jows Index Closing Price, Korean Interest Rates, WTI Oil Prices, USD to KRW Exchange Rates). Initially, the stock data was scraped using BeautifulSoup, but the process took too long, and was therefore substituted by an API. The collected data is cleaned and processed in the 'datapreprocessing.py' file in the server, and  the resultant data is fed into the 'modelfitting.py' file which uses scikit-learn to apply ML Models to output a predicted price. The output results (predicted price for the stock) is then updated in the database and sent to the server which is then received by the frontend.



## Projects
![Alt Text](https://raw.githubusercontent.com/jihwankimqd/PortfolioIntel/master/PROJECTS.gif)  
  
A gallery of personal projects. The images are gifs and ordered neatly using the Vue-Bootstrap components. The images can be clicked and it will redirect the page to the clicked project. Details of individual projects can be found in their respective links.


## Deploy Locally
  
To deploy the project locally, simply clone/download the repository. The server and client apps have to be deployed separately. 
1. Download all the dependencies such as Python, Pymongo, Flask, Flask_Cors, Pandas... (Best practice is to run the file first and check the logs to download the requirements which you may be missing.) The application was developed on MacOS, and when tested on a Windows (with different settings and missing requirements), the missing dependencies had been downloaded using 
```
pip install pymongo
pip install flask
pip install flask_cors
pip install pandas
pip install requests
pip install pandas_datareader
pip install dnspython
```
The specific requirements/dependencies will vary on different machines.  
2. After downloading the requirements (if needed), direct into the /Backend folder and run 
```
python app.py
```
3. The server will be running on:
```
 * Running on http://127.0.0.1:5000/
```
4. Now change the directory into the /Frontend folder
5. Install the requirements/dependencies and make sure you have Vue.js installed. Then run the follow commands:
```
# Using npm
# Project Setup
npm install

# Compiles and hot-reloads for development
npm run serve

# Using yarn
# Project Setup
yarn install

# Compiles and hot-reloads for development
yarn serve
```
