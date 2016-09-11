import requests
from logging import getLogger

logger = getLogger(__name__)


def run(urls=['http://example.com/'],
        download=lambda x: requests.get(x).text,
        parse=lambda x: x, store=print):
    for url in urls:
        logger.debug("Downloading {} ...".format(url))
        page = download(url)
        logger.debug("Parsing ...")
        parsed = parse(page)
        logger.debug("Storing ...")
        store(parsed)
