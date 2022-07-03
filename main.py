from selenium import webdriver
import time

def get_driver():
  # Set Options To Make Browsing Easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
  
  driver = webdriver.Chrome(options=options)
  driver.get("http://automated.pythonanywhere.com/login/")
  return driver
  
def main():
  driver = get_driver()
  time.sleep(2)
  driver.find_element(by="id", value="id_username").send_keys("automated")

print(main())
  