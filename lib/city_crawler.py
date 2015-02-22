##############################################################################################
# The Everything Pin Project
# 
# File: lib\city_crawler.py
# Desc: wrapper class for crawling an entire city
##############################################################################################

import imp 						#better module importing

#load local modules
ylc = imp.load_source('', 'yelp_list_crawler.py')

class CityCrawler:

	#####################
	#Class Variables
	#####################

	yelp_cats = ["Restaurants", "Bars", "Doctors"]	#yelp categories that are crawled
	
	def __init__(self, city, state, cats = yelp_cats):
		self.city = city.replace(' ', '+')
		self.state = state
		self.yelp_crawlers = [ylc.YelpListCrawler(self.city, self.state, cat) for cat in cats]

	def CrawlYelp(self):
		for ylc in self.yelp_crawlers:
			ylc.Crawl(0)	#testing; crawl only first page HTML for now until we figure out how to get JSON for later items

	def Crawl(self):
		self.CrawlYelp()
		