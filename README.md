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
  
Can pick a desired chart type (from Chartjs), and the page will send a response to the server (Python and Flask based, deployed on Heroku), which will then send a request to the database (MongoDB), which then sends the chart data back to the server which is received on the frontend. It is made using REST API, and can send requests to add/delete new data to/from the database. The charts will then dynamically reload when a change in the data is detected. Initially, it may take some time for the data to load (especially for Line and Bar Charts due to their large amounts of data), because the server is hosted (for free) on Heroku. For faster speeds, you can clone the repo and run the webapp locally (refer below).

## Dashboard
![Alt Text](https://raw.githubusercontent.com/jihwankimqd/PortfolioIntel/master/DASHBOARD.gif)  
  
A Machine Learning Dashboard, which shows the
