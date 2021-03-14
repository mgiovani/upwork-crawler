from loguru import logger
from dotenv import load_dotenv
load_dotenv()

from crawlers.login import Login
from crawlers.homepage import HomepageCrawler


def main():
    logger.level('INFO')
    logger.info('Starting login crawler...')
    login_crawler = Login()
    login_crawler.run()
    web_driver = login_crawler.get_web_driver()

    logger.info('Starting homepage crawler...')
    homepage_crawler = HomepageCrawler(web_driver)
    homepage_crawler.run()

    web_driver.quit()


if __name__ == '__main__':
    main()
