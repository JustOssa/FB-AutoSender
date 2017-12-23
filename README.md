# FB AutoSender
> Quick script made back in early 2017 with Python to send automated messages on Facebook via the browser.



## About The Project

It is a python script that sends Facebook messages automatically to saved users. It can be configured to send advertising messages to customers. It read data from an excel sheet and send a configured message to people.

It's based on Selenium, a web browser automation tool. You can find out more [here](https://www.selenium.dev).


### Built With
* [Python](https://www.python.org)


## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

In order to run the python script, your system must have the following programs/packages installed.

* [Python 3](https://www.python.org/downloads)

* [Google Chrome](https://www.google.com/chrome)

* [ChromeDriver](https://chromedriver.chromium.org/downloads) : You need to put it in this project folder, you can keep the repo driver if you are using Chrome version 92.



### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/JustOssa/FB-AutoSender.git
   ```
2. Install selenium package
   ```sh
   pip install selenium
   ```
3. Enter your facebook credentials in `fb.conf`
   ```
   [Creds]
   username= your@email.here
   password= yourpassword
   ```
4. Enter your target users in `ids.csv`

### Usage

Run the script in any shell on a system with Python installed/configured.
   ```sh
   python main.py
   ```


## To do
- Add gui


## Notes
If you wish to send an image instead of text you can uncomment attachment section in `main.py`.
 
This script is for saved contact ids only, if you want to retrieve facebook ids in bulk from friends/groups. You may prefer another repository.

* Repository: https://github.com/JustOssa/FB-AutoExtracter

Facebook constantly change their html class names, which may break this script. File an issue if something weird happens -- or more likely, doesn't happen.


## Contact

Created by [@JustOssa](https://github.com/JustOssa) - feel free to contact me!
