import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import time
import random

QUERY = "laptop"
PAGES = 2

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "en-IN,en;q=0.9"
}

def extract_price(tag):
    if not tag:
        return ""
    text = tag.get_text(strip=True).replace(",", "")
    return text.replace("₹", "").strip()

def fetch_page(page_number):
    url = f"https://www.amazon.in/s?k={QUERY}&page={page_number}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print(f"Page {page_number} blocked or unavailable.")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    containers = soup.find_all("div", {"data-component-type": "s-search-result"})
    collected = []

    for box in containers:
        title_tag = box.find("h2")
        title = title_tag.get_text(strip=True) if title_tag else ""

        img_tag = box.find("img")
        image = img_tag["src"] if img_tag else ""

        rate_tag = box.find("span", class_="a-icon-alt")
        rating = rate_tag.get_text(strip=True) if rate_tag else ""

        price_tag = box.find("span", class_="a-offscreen")
        price = extract_price(price_tag)

        sponsored = box.find("span", string="Sponsored")
        item_type = "Ad" if sponsored else "Organic"

        collected.append({
            "Image": image,
            "Title": title,
            "Rating": rating,
            "Price": price,
            "Ad / Organic": item_type
        })

    return collected

def main():
    all_rows = []

    for p in range(1, PAGES + 1):
        print(f"Scraping Page {p}...")
        items = fetch_page(p)
        all_rows.extend(items)
        time.sleep(random.uniform(1.2, 2.2))

    filename = f"amazon_laptops_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["Image", "Title", "Rating", "Price", "Ad / Organic"]
        )
        writer.writeheader()
        writer.writerows(all_rows)

    print(f"\nCompleted. Total rows: {len(all_rows)}")
    print(f"Saved as: {filename}")

if __name__ == "__main__":
    main()
