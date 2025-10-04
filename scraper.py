import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime

# Step 1: Fetch the webpage
today = datetime.datetime.today().strftime("%Y%m%d")
url = f"https://funebres.eldia.com/edis/{today}/funebres2.htm"
response = requests.get(url)
response.raise_for_status()  # Raise error if request failed

# Step 2: Parse HTML and extract all <li> tag values
soup = BeautifulSoup(response.text, 'html.parser')
li_tags = soup.find_all('li')
li_texts = [li.get_text(strip=True) for li in li_tags]

# Step 3: Save to DataFrame and CSV
df = pd.DataFrame({'li_text': li_texts})
df.to_csv('funebres_li_tags.csv', index=False)

print("Scraping complete. Data saved to funebres_li_tags.csv")
