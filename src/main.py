import requests

from crawlers.login import Login
from crawlers.homepage import HomepageCrawler

def main():
    login_crawler = Login()
    login_crawler.run()
    web_driver = login_crawler.get_web_driver()

    homepage_crawler = HomepageCrawler(web_driver)
    homepage_crawler.run()

    web_driver.quit()

if __name__=='__main__':
    main()
