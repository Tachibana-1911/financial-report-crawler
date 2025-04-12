from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless")

# 自動で適合するChromeDriverを取得
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://cover-corp.com/ir/library")
print(driver.title)
driver.quit()
