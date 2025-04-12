from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import os
import time
import requests

def setup_driver(headless=True):
    options = Options()
    if headless:
        options.add_argument("--headless")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def download_pdf(link, filename):
    try:
        response = requests.get(link)
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"✅ 保存成功: {filename}")
    except Exception as e:
        print(f"⚠️ 保存失敗: {link} → {e}")

def scrape_pdfs_from_ir(ir_url, save_dir, headless=True):
    driver = setup_driver(headless)
    driver.get(ir_url)
    time.sleep(3)

    os.makedirs(save_dir, exist_ok=True)

    try:
        select_elem = driver.find_element(By.TAG_NAME, "select")
        select = Select(select_elem)

        for option in select.options:
            year = option.text.strip()
            print(f"\n📘 年度: {year} を選択中...")

            select.select_by_visible_text(year)
            time.sleep(2)

            pdf_links = driver.find_elements(By.XPATH, "//a[contains(@href, '.pdf')]")
            for i, link in enumerate(pdf_links):
                href = link.get_attribute("href")
                if href:
                    filename = os.path.join(save_dir, f"{year}_{i+1}.pdf")
                    print(f"⬇️  {href}")
                    download_pdf(href, filename)
    except Exception as e:
        print(f"⚠️ 年度選択またはPDF抽出エラー: {e}")
    finally:
        driver.quit()
