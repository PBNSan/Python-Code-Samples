# Wikipedia WebCrawler - How to do
# page = a random starting page
# article_chain = []
# while title of page isn't 'Philosophy' and we have not discovered a cycle:
#     append page to article_chain
#     download the page content
#     find the first link in the content
#     page = that link
#     pause for a second

import time
import requests
import urllib
from bs4 import BeautifulSoup

start_url = "https://en.wikipedia.org/wiki/Special:Random"
target_url = "https://en.wikipedia.org/wiki/Philosophy"

def find_first_link(url):
	# get the HTML from "url", use the requests library
	response = requests.get(url)
	html = response.text
	# feed the HTML into Beautiful Soup
	soup = BeautifulSoup(html,'html.parser')
	# find the first link in the article
	content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
	article_link =None

	for element in content_div.find_all("p",recursive=False):
		if element.find("a",recursive=False):
			article_link = element.find("a",recursive=False).get("href")
			break
	# return the first link as a string, or return None if there is no link
	if not article_link:
		return 

	# Build a full url from the relative article_link url
	first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)

	return first_link


def continue_crawl(search_history,target_url,max_steps=25):
	last_found_url = search_history[-1]
	search_history_set=set(search_history)
	check_list = []
	if last_found_url == target_url:
		return False
	elif len(search_history) > max_steps:
		return False
	elif len(search_history_set) != len(search_history):
		for element in search_history_set:
			for elements in search_history:
				if element == elements:
					check_list.append(elements)
				if len(check_list) > 1:
					return False
	else:
		return True

#approach 2

# def continue_crawl(search_history, target_url):
#     if search_history[-1] == target_url:
#         print("We've found the target article!")
#         return False
#     elif len(search_history) > 25:
#         print("The search has gone on suspiciously long; aborting search!")
#         return False
#     elif search_history[-1] in search_history[:-1]:
#         print("We've arrived at an article we've already seen; aborting search!")
#         return False
#     else:
#         return True
  


# Writing the Main Loop
	# download html of last article in article_chain
	# find the first link in that html
	# add the first link to article_chain
	# delay for about two seconds
article_chain =[start_url]

#TODO: import something?

while continue_crawl(article_chain, target_url):
	print(article_chain[-1])
	# download html of last article in article_chain
	# find the first link in that html
	first_link = find_first_link(article_chain[-1])
	if not first_link:
		print("We've arrived at an article with no links, aborting search!")
		break
	# add the first link to article chain
	article_chain.append(first_link)
	# delay for about two seconds
	# TODO: YOUR CODE HERE!
	time.sleep(2)


