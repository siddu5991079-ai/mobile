
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options

# Appium aur Emulator ki settings
options = UiAutomator2Options()
options.platform_name = 'Android'
options.automation_name = 'UiAutomator2'
options.no_reset = True 

# Aapki app ki details
options.app_package = 'com.asadapps.live.ten.sports'
# Correct Entry Gate jo humne pichli dafa dhonda tha taake permission error na aaye
options.app_activity = 'com.asadapps.live.ten.sports.ui.activities.EntryActivity'

try:
    print("Appium server se connect ho raha hoon...")
    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    
    print("App open ho gayi hai, UI load hone ke liye 15 seconds wait kar raha hoon...")
    time.sleep(15) 
    
    print("Screenshot DRM flag ki wajah se blocked hai. UI ka XML code extract kar raha hoon...")
    
    # App ke current page ka pura XML source code nikalna
    page_source = driver.page_source
    
    # Us code ko ek text (XML) file mein save karna
    xml_filename = "app_ui_dump.xml"
    with open(xml_filename, "w", encoding="utf-8") as file:
        file.write(page_source)
        
    print(f"Success! UI Dump '{xml_filename}' ke naam se save ho gaya.")

except Exception as e:
    print(f"Error aya hai: {e}")

finally:
    # Aakhir mein driver ko close lazmi karna hai
    if 'driver' in locals():
        driver.quit()
















# ==========================================================================================================
# ================== Screenshot flags are there =======================
# ==========================================================================================================




# from appium import webdriver
# from appium.options.android import UiAutomator2Options
# import time

# options = UiAutomator2Options()
# options.platform_name = 'Android'
# options.automation_name = 'UiAutomator2'
# options.no_reset = True

# # Aapki app ka package name
# options.app_package = 'com.asadapps.live.ten.sports'

# # TODO: Yahan App ki Main Activity dalni hogi (abhi farzi dali hai)
# # options.app_activity = 'com.asadapps.live.ten.sports.MainActivity' 
# # Purani line ki jagah yeh exact line likhein:
# # options.app_activity = 'com.asadapps.live.ten.sports.ui.activities.MainActivity'
# # Is line ko update karein
# options.app_activity = 'com.asadapps.live.ten.sports.ui.activities.EntryActivity'

# print("App open kar raha hoon...")
# driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

# # App puri tarah load hone ka wait (10 seconds)
# time.sleep(10)

# # Screenshot capture karna
# driver.save_screenshot('capture.png')
# print("Screenshot save ho gaya!")

# driver.quit()
