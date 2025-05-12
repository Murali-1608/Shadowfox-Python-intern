import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_quotes(pages=5):
    base_url = "https://quotes.toscrape.com/page/{}/"
    all_quotes = []

    for page in range(1, pages + 1):
        response = requests.get(base_url.format(page))
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('div', class_='quote')

        for quote in quotes:
            text = quote.find('span', class_='text').get_text()
            author = quote.find('small', class_='author').get_text()
            tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]

            all_quotes.append({
                'Quote': text,
                'Author': author,
                'Tags': ", ".join(tags)
            })

    return all_quotes

# Save the scraped quotes to a CSV file
if __name__ == "__main__":
    data = scrape_quotes()
    df = pd.DataFrame(data)
    df.to_csv("quotes.csv", index=False)
    print("✅ Quotes saved to quotes.csv")
