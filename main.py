from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from src.spiders.genshin import GenshinSpider

OUTPUT = 'output/output.json'

# Create a CrawlerProcess
process = CrawlerProcess(get_project_settings())

# Set Output
process.settings.set('OUTPUT', OUTPUT)
process.settings.set('FEEDS', {OUTPUT: {'format': 'json'}})

# Set up your spider
spider = GenshinSpider

# Start the spider
process.crawl(spider)
process.start()
