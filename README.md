# KTO-JuiceShop

## About the project
**KTO-JuiceShop** is a project aiming to test the security/sturdiness of the login/register features for the well-known application [JuiceShop](https://juice-shop.herokuapp.com/#/)

The idea is to document all the possible scenarios related to those two features, including both UI and API access, and then code the proposed test cases.

## Documentation

In the folder named **Documentation** you'll be able to find all the files created for each test case, both for UI and API.

These files include general information about the test case, like:

 - Test Case Name
 - Test Case ID
 - Test Case Description
 - Steps and Expected results for each step
 - Final expected result
 - Extra screenshots/indications

> **NOTE:** Test cases are coded based on the indications from these files.

## Set up

I used Python and Selenium as the main tools to code the test cases, so in order to be able to run the software inside the folder called **Test Suite**, you will need to install a couple things first.

### 1- Python
In case you don't have Python installed already, you can go to [Python Download Page](https://www.python.org/downloads/), select you OS, and download the latest version.
Once downloaded, just open the file and click "Next".

> **NOTE:** In order to avoid problems with next steps, if you see a checkbox asking you "Add Python to PATH?" while installing, click the checkbox in order to add python to path.

### 2- Selenium
Selenium is the software in charge of controlling the web browser and perform automated actions. In order to install Selenium, you have to open the command line, and type the following command:

    pip install selenium
In case you get an error (can happen if you using MacOS/Linux), try with the following command:

    python3 -m pip install selenium

### 3- ChromeDriver
In order to access the website in an automated way, we'll need a web browser. In this case I used Chrome, so make sure you have Chrome installed in your machine.

But sometimes having Chrome installed isn't enough. So just to make sure, go to [ChromeDriver Download Page](https://chromedriver.storage.googleapis.com/index.html?path=114.0.5735.90/) and select the option based on your OS.

Once downloaded, move the .zip file to the C:/ folder and unzip it there. You should see a file called **chromedriver.exe**. If you do, you're good to go.

## Getting the code

Now we're ready. But before executing the suites, you'll need to have the code in your machine. Your first option, if you have git installed, is to **clone the repository** using the following command:

    git clone https://github.com/agustinthedev/KTO-JuiceShop
In case you don't have git installed, you can manually download the code by clicking in the *Download* button:

![Manually download code from repository](Pictures/DownloadRepo.png)

Once downloaded, just unzip the file and you should have all the code.

## Executing the suites
Once you get the code, you're ready to execute the suites.

Get into the **Test Suite** folder and you'll see two files:

 1. *Run API Test Suite*
 2. *Run UI Test Suite*

As their names indicate, each files execute all the test cases from either UI or API category. Once all test cases are executed, you'll receive a quick breakdown of how many test cases were executed in total, how many failed and how many passed.

You can also check the logs.txt file, where each test case writes detailed information about the execution. This way it's easier to debug in case of any problem.

