
# This is a simple automation bot for filling out forms

# Note: If using Google Chrome, Edge, or any other browser. Then you will need to download that specific driver.
# The driver for Chrome can be found here: https://chromedriver.chromium.org/downloads
# The driver for Edge can be found here: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
# I used Safari driver which is natively installed on my OS.

# Importing needed packages
from selenium import webdriver
from selenium.webdriver.common.by import By

# Creating the driver and requesting the site
web = webdriver.Safari()
web.get('https://alexandergursky001.wixsite.com/mysite')

# Imputing the 'name' field
FullName = "Alexander Gursky"
namexpath = web.find_element(By.XPATH, '//*[@id="input_comp-lbwlwk5b"]')
namexpath.send_keys(FullName)

# Imputing the 'email' field
Email = "johndoe45@gmail.com"
emailxpath = web.find_element(By.XPATH, '//*[@id="input_comp-lbwlwk5y"]')
emailxpath.send_keys(Email)

# Imputing the 'subject' field
Subject = "Testing 123"
subjectxpath = web.find_element(By.XPATH, '//*[@id="input_comp-lbwlwk69"]')
subjectxpath.send_keys(Subject)

# Imputing the 'message' field
Message = "This is an automated test."
messagexpath = web.find_element(By.XPATH, '//*[@id="textarea_comp-lbwlwk6k"]')
messagexpath.send_keys(Message)

# Submitting the form
RadioButtonSubmit = web.find_element(By.XPATH, '//*[@id="comp-lbwlwk70"]/button')
RadioButtonSubmit.click()
