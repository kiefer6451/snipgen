from time import sleep
from selenium import webdriver
import re

class Scraper:
    def __init__(self):
        driver = webdriver.Firefox(timeout=20)
        driver.set_page_load_timeout(9)
        self.driver = driver
    
    def scrape(self, query):
        search = "https://www.google.com/search?q=site:stackoverflow.com+{}".format(query.replace(" ", "+"))
        
        try:
            self.driver.get(search)
            html = self.driver.page_source
            res = re.finditer("stackoverflow.com/questions/", html)
            indices = [m.start(0) for m in res]
            final = list()
            for item in indices:
                item2 = html[item+28:item+100].partition("/")[0]
                final.append(int(item2))
            return final
        except Exception as e:
            print(e)
            return None

def main():
    scraper = Scraper()
    while True:
        q = input("Enter query: ")
        result = scraper.scrape(q)
        print(result)

if __name__ == "__main__":
    main()
