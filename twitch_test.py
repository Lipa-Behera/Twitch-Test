from selenium import webdriver
import time
import os 
import shutil
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#open mobile emulator view in chrome
#mobile_emulation = { "deviceName": "iphone X" }
#option = webdriver.ChromeOptions()
#option.add_experimental_option("mobileEmulation", mobile_emulation)
# Initialize the Chrome driver with mobile emulation
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)

screenshot_path="C:\\temp"
#open web view in chrome
option = webdriver.ChromeOptions()
driver=webdriver.Chrome()

#go to twitch 
driver.get("https://www.twitch.tv/")
#input starcraft II
search_bar=driver.find_element(By.XPATH,"//input[@aria-label='Search Input' and @placeholder='Search']")
search_bar.send_keys("starcraft II")
#click on search icon
click_element=driver.find_element(By.XPATH,"//div[contains(@class, 'ScButtonIconWrapper')]")
click_element.click()
#scroll down 2 times
actions = ActionChains(driver)
actions.send_keys(Keys.PAGE_DOWN).perform()  # First Page Down
time.sleep(2)  # Wait for the content to load
actions.send_keys(Keys.PAGE_DOWN).perform()  # Second Page Down
time.sleep(2)  # Wait for the content to load
try:
    wait = WebDriverWait(driver, 10)
    # select one streamer
    video_link = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'Layout-sc-1xcs6mc-0 cVmNmw')]//a")))
    video_link.click()
    time.sleep(5)#wait 5 sec to play the video 
   
    if os.path.exists(screenshot_path):
        # Use shutil.rmtree() to force delete the directory
        shutil.rmtree(screenshot_path)
        print(f"Directory '{screenshot_path}' forcefully deleted.")
    else:
        print(f"Directory '{screenshot_path}' does not exist.")
    os.mkdir(screenshot_path)
    #take a screenshot
    screen_path = os.path.join(screenshot_path, "screenshot.png")
    driver.save_screenshot(screen_path)
    print(f"Screenshot saved at: {screen_path}")

except Exception as e:
    print("An error occurred:", e)

#closed the browser
driver.quit()    
