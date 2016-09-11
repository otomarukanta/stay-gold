import requests
from logging import getLogger


def default_download(url):
    res = requests.get(url)
    return res.text


class StayGold():

    logger = getLogger(__name__)

    def __init__(self, select=None, download=default_download,
                 parse=None, store=print):
        self.__select = select
        self.__download = download
        self.__parse = parse
        self.__store = store

    def run(self):
        for url in self.__select():
            self.logger.debug("Downloading {}".format(url))
            page = self.__download(url)
            parsed = self.__parse(page)
            self.__store(parsed)
