from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import re

class Scraper:
    def __init__(self):
        self.driver = None

    def setup(self):
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options)
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
                item2 = html[item+28:item+100].partition("/")[0].partition("\"")[0]
                #print(item2)
                final.append(int(item2))
            #print("DEBUG: the responses are {}".format(final))
            return list(dict.fromkeys(final))
        except Exception as e:
            print(e)
            return None

    def die(self):
        if self.driver is not None:
            self.driver.close()

def main():
    scraper = Scraper()
    scraper.setup()
    while True:
        q = input("Enter query: ")
        result = scraper.scrape(q)
        print(result)

if __name__ == "__main__":
    main()
