from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service  # ✅ Import Service for local driver

import time

app = FastAPI()

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/search")
def search_papers(query: str):
    print("Starting search for:", query)

    options = Options()
   # options.add_argument("--headless")  # run Chrome in background
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = None
    try:
        # ✅ Use your local ChromeDriver path here
        service = Service("C:\\tools\\chromedriver.exe")
        driver = webdriver.Chrome(service=service, options=options)
        print("Chrome driver launched")

        url = f"https://www.semanticscholar.org/search?q={query}&sort=relevance"
        driver.get(url)
        time.sleep(3)  # wait manually to allow page JS to run

        # Wait for search results
        try:
            WebDriverWait(driver, 40).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-selenium-selector="result-row"]'))
            )
        except Exception as wait_err:
            print("Timeout or error while waiting for articles:", wait_err)
            return {"error": "Timeout or error while waiting for articles"}

        articles = driver.find_elements(By.CSS_SELECTOR, '[data-selenium-selector="result-row"]')
        print(f"Found {len(articles)} articles")

        results = []
        for i, article in enumerate(articles[:5]):
            try:
                title_elem = article.find_element(By.CSS_SELECTOR, '[data-selenium-selector="title-link"]')
                title = title_elem.text
                link = title_elem.get_attribute('href')
                print(f"{i+1}. {title} - {link}")
                results.append({"title": title, "url": link})
            except Exception as e:
                print("Error extracting article:", e)

        return {"results": results}

    except Exception as e:
        print("General error occurred during search:", e)
        return {"error": str(e)}

    finally:
        if driver:
            driver.quit()
