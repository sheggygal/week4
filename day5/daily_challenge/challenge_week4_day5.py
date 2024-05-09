import requests
import time

def get_website_load_time(url):
    try:
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()

        if response.status_code == 200:
            load_time = end_time - start_time
            return load_time
        else:
            print("Error: Status code", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None


websites = ["https://www.google.com", "https://www.ynet.co.il", "https://www.imdb.com"]

for website in websites:
    load_time = get_website_load_time(website)
    if load_time is not None:
        print("Load time for", website, ":", load_time, "seconds")
