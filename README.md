# LinkedIn_Tenure_extraction

This is a demo project to extract average tenure from a linkedin profile using Flask API

Prerequisites
Python and Flask (for API) installed.

Project Structure
This project has four major parts :
- a.py - This contains Flask APIs that receives linkedin profile id  through r API calls, computes the average tenure and returns it.
- By executing the code 'browser=webdriver.Chrome('chromedriver.exe')' a new browser will open and using get() function open LinkedIn login page.
- Then open the config.txt file and read the first two lines (User Id and Password), send the keys to the browser using send_keys() function finally, submit the details using submit() function doing so you will be able to login to your LinkedIn account.

- templates - This folder contains the HTML template to allow user to enter  detail and displays the average tenure.
Running the project
Run a.py using below command to start Flask API
python a.py
By default, flask will run on port 5000.

Navigate to URL http://localhost:5000
You should be able to view the homepage as below

Enter valid linkedin profile id and hit submit button
If everything goes well, you should be able to see the caculated average tenure on the HTML page!



