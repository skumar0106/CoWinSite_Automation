# CoWinSite_Automation
CoWin Slot Booking Trial

## Prerequisite

```sh
!pip install selenium
!pip install -U selenium
```

# Download the ChromeDriver and change the Path as per your own OS
#### Code Snippet in the file to set :
```sh
driver_path = './chromedriver_linux64 _89/chromedriver' # LINE NUMBER 43
```

## STEPS FOR Execution

### 1) Enter all the Values in the parameters.json file provided 
#### NOTE  : Please Enter the Exact Names as visible on the website

```sh
{
	"Candidate": {
		"MobileNumber": "9021XXXXXX",
		"NameOfCandidate": "SUMEET KUMAR",
		"StateName": " Maharashtra",
		"DistrictName": "Pune",
		"Centers": ["New Akurdi Hospital (18-44Yrs)", "Primary Health Center Wagholi Pune", "MALEGAON BK"]
	}
}
```

# 2) Submit the code or run the same on Jupyter Notebook

# 3) Enter OTP in the browser within 18 secs when asked and do not press confirm OTP button.

---------------------------------
#### WORKING OF THE CODE

```sh
Once all the Inputs are provided in the JSON, and the code is submitted , it will work as a scrapper and try to search for an available slot by iterating through all the Centers specified.
Please note that if a Center is not listed on the COWIN Site itself and is being repeatedly searched for, it takes much time to scrape it, so its better to remove it from the JSON once the logs are handy.
The cod ekeeps on running till one OTP expires which is about 15 minutes per session.
```

# 4) A User should keep an Eye on the browser as because in case a slot is available , it will land into that page and select the slot of '03:00PM-06:00PM' and wait for 8 seconds for the user to enter the CAPTCHA and then click on 'CONFIRM" button.'









