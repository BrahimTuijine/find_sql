from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options
import socket

class bingSearch:
	
	def __init__(self,host):
		self.host = host
		

	def mypages(self):
		#options = Options()
		#options.headless = True
		browser = webdriver.Firefox()
		url = "https://www.bing.com/"
		browser.get(url)
		search = browser.find_element_by_id("sb_form_q")
		argument = "ip:" + str(socket.gethostbyname(self.host)) + " id="
		search.send_keys(argument)
		search.submit()
		time.sleep(4)
		listpages = []
		listpages.append(browser.current_url)
		pages = browser.find_elements_by_xpath("//li//a[@class='b_widePag sb_bp']")
		for i in pages:
			href = i.get_attribute("href")
			listpages.append(href)
		browser.quit()
		return listpages
	
	def urlSearch(self):
		listpages = self.mypages()
		for link in listpages:
			# 7ell el browser w jib el hrefs 
			browser = webdriver.Firefox()
			browser.get(link)
			print("fetching result from : "+ str(link))
			time.sleep(4)
			try:
				links = browser.find_elements_by_xpath("//li[@class='b_algo']//h2//a")
			except:
				pass

			results = []
			for i in links:
				href = i.get_attribute("href")
				print(href)
				results.append(href)
			browser.quit()
		return results
	
	def sql_detect_from_source(self):
		url_results = self.urlSearch()
		for url in url_results:
			browser = webdriver.Firefox()
			try:
				browser.get(url + "'")
				source = browser.page_source

				if "You have an error in your SQL syntax" in source:
					print("You have an error in your SQL syntax ==>  " + url)
			except:
				print("there is an error in the web page")
				pass
			browser.quit()