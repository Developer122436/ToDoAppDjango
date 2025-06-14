import requests
import pandas as pd
from bs4 import BeautifulSoup
from translate import Translator
import time

translator = Translator(to_lang="en", from_lang="he", provider="mymemory")

kibbutz_list = [
    "מתחדש",
    "שיתופי",
    "עירוני",
    "קיבוץ עירוני",
]

kibbutz_list_ENGLISH = []



for name in kibbutz_list:
    try:
        print(f"Translating {name}...")
        translated_name = translator.translate(name)
        kibbutz_list_ENGLISH.append(translated_name)
    except Exception as e:
        print(f"Could not translate {name} due to error: {e}")


# Create a Pandas DataFrame
df = pd.DataFrame({
    'Kibbutz Name Hebrew': kibbutz_list,
    'Kibbutz Name': kibbutz_list_ENGLISH
})

# Write the DataFrame to an Excel file
df.to_excel('list_of_RegionalCouncil1.xlsx', index=False, sheet_name='Kibbutzim')
