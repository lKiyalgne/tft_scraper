from selenium import webdriver
from selenium.webdriver.chrome.options import Options

CHROME_PATH = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
CHROMEDRIVER_PATH = "C:\\Users\\Fourth\\.PyCharm2019.3\\chromedriver.exe"
WINDOW_SIZE = "1920,1080"

chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.binary_location = CHROME_PATH

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                          options=chrome_options
                         )  
driver.get("https://www.google.com")
driver.get_screenshot_as_file("capture.png")
driver.close()