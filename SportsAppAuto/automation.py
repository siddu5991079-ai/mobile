from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

options = UiAutomator2Options()
options.platform_name = 'Android'
options.automation_name = 'UiAutomator2'
options.no_reset = True

# Aapki app ka package name
options.app_package = 'com.asadapps.live.ten.sports'

# TODO: Yahan App ki Main Activity dalni hogi (abhi farzi dali hai)
# options.app_activity = 'com.asadapps.live.ten.sports.MainActivity' 
# Purani line ki jagah yeh exact line likhein:
# options.app_activity = 'com.asadapps.live.ten.sports.ui.activities.MainActivity'
# Is line ko update karein
options.app_activity = 'com.asadapps.live.ten.sports.ui.activities.EntryActivity'

print("App open kar raha hoon...")
driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

# App puri tarah load hone ka wait (10 seconds)
time.sleep(10)

# Screenshot capture karna
driver.save_screenshot('capture.png')
print("Screenshot save ho gaya!")

driver.quit()
