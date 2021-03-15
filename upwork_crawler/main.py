from loguru import logger

from crawlers.login import Login
from crawlers.homepage import HomepageCrawler
from crawlers.profile import ProfileCrawler


def main():
    logger.level('INFO')
    logger.info('Starting login crawler...')
    login_crawler = Login()
    login_crawler.run()
    web_driver = login_crawler.get_web_driver()

    logger.info('Starting homepage crawler...')
    homepage_crawler = HomepageCrawler(web_driver)
    fwh_model = homepage_crawler.run()

    profile_cipher = fwh_model.identity.ciphertext
    logger.info('Starting profile crawler...')
    profile_crawler = ProfileCrawler(web_driver)
    profile_crawler.profile_cipher = profile_cipher
    profile_crawler.run()

    web_driver.quit()


if __name__ == '__main__':
    main()
