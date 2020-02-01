import scrapy

from ..items import QuoteItem

class QuoteSpider(scrapy.Spider):
	name = 'quotes'
	start_urls = [
		'http://quotes.toscrape.com/'
	]
	def parse(self, response):
		item = QuoteItem()

		all_div = response.css("div.quote")


		for qu in all_div:
			dat = qu.css("span.text::text").extract()
			auth = qu.css(".author::text").extract()
			tag = qu.css(".tag::text").extract()

			item['dat'] = dat
			item['auth'] = auth
			item['tag'] = tag
			yield  item