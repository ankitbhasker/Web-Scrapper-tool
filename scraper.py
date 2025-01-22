# scraper.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time


def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Headless mode to run in background
    service = Service(executable_path=r"C:\WebDriver\bin\chromedriver.exe")  # Specify path to your chromedriver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver


def scrape_page(url):
    driver = get_driver()
    driver.get(url)
    time.sleep(3)  # Wait for the page to load

    page_source = driver.page_source
    driver.quit()

    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(page_source, 'lxml')

    # Example: Extract all <h1> tags from the page
    titles = soup.find_all('h1')
    data = [title.get_text() for title in titles]

    return data

# scraper.py
from dotenv import load_dotenv
import os
from langchain_ollama import OllamaLLM

# Load environment variables from .env
load_dotenv()

# Access the Langchain API key
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")


def process_with_langchain(text_data):
    ollama = Ollama(api_key=langchain_api_key)

    # AI prompt to summarize the scraped data
    prompt = f"Summarize the following text:\n{text_data}"

    # Get response from LLM
    response = ollama.run(prompt)

    return response


# scraper.py

def scrape_and_analyze(url):
    # Step 1: Scrape the webpage
    scraped_data = scrape_page(url)

    # Join the scraped text into one string for analysis
    text_data = ' '.join(scraped_data)

    # Step 2: Process the scraped data with Langchain AI
    analysis_result = process_with_langchain(text_data)

    return analysis_result