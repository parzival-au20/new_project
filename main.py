import threading
import time
import logging
from datetime import datetime
from AinOnline import fetch_ainonline_news
from requests_ntlm import HttpNtlmAuth



news_fetch_functions = [
    fetch_ainonline_news,
]

for fetch_function in news_fetch_functions:
    try:
        counter = 0
        start_time_fetch = time.time()
        
        fetch_function()
        
        end_time_fetch = time.time()
        elapsed_time_fetch = end_time_fetch - start_time_fetch
        print(f"{fetch_function.__name__} islemi  {elapsed_time_fetch} saniye surdu")
        logging.info(f"{fetch_function.__name__} islemi  {elapsed_time_fetch} saniye surdu")
    except Exception as e:
        print(f"Hata oluştu: {e}")
        logging.error(f"Hata oluştu: {e}")

print("Haberler başarıyla çekildi.")
