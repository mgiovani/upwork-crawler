import requests
from loguru import logger

from crawlers.login import Login
from crawlers.homepage import HomepageCrawler

def main():
    logger.debug('Starting login crawler...')
    login_crawler = Login()
    login_crawler.run()
    web_driver = login_crawler.get_web_driver()

    logger.debug('Starting homepage crawler...')
    homepage_crawler = HomepageCrawler(web_driver)
    homepage_crawler.run()

    web_driver.quit()

if __name__=='__main__':
    main()