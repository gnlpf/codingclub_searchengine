"""
Erstellt am 22.06.2015 10:59:44
@author: loop28
"""

import urllib2
import numpy as np
# from BeautifulSoup import BeautifulSoup

def getLinkFromIndex(htmlString):
	''' diese methode finded den ersten Link in einem gegebenen String'''

	start_link = htmlString.find('<a href=')
	start_quote = htmlString.find('"', start_link)
	end_quote = htmlString.find('"', start_quote+1)

	# check if an occurence has been found
	if start_link == -1 or start_quote == -1 or end_quote == -1 :
		return False, -1

	url = htmlString[start_quote+1:end_quote]

	# check if url is empty
	if not url:
		return url, -1

	return url, end_quote

def crawlPage(link):
	try:
		page = urllib2.urlopen(link).read()
	except urllib2.HTTPError, e:
		print 'A problem occured while loading the page [' + link + ']. Please try again. ' + e
		return

	try:
		page
	except:
		page = "empty"
		return

	# Speichere alle gefundenen Links in einer Variablen
	linksList = []

	# mach eine schleife
	# um alle Links in einer Website zu finden
	while page:
		# finde den ersten Link in einem String:
		new_url, end_quote = getLinkFromIndex(page)

		if new_url and not end_quote == -1:
			linksList.append(new_url)
			page = page[end_quote:]
		else:
			page = None

	return linksList

def getLinkToPage():
	''' fragt nach einer url '''
	return raw_input("Bitte gib eine URL ein:")

def makeAbsoluteLink(link, origin):
	# TODO
	# convert relative links, like "/kontakt.php"
	# to an absolute link: "http://..../kontakt.php"
	stringpart = link.split('://')

	# if link contains http or https then it is already an absolute link
	if len(stringpart) > 1:
		print link
		return link

	splitOrigin = origin.split('://')

	protocol = ''
	domain = ''
	path = ''

	if len(splitOrigin) > 1:
		protocol = splitOrigin[0]

	domainAndPath = splitOrigin[1].split('/')
	domain = domainAndPath[0]

	if len(domainAndPath) > 1:
		path.join(domainAndPath[1:],'/')

	print '-------'
	print 'origin: '
	print origin
	print 'protocol:'
	print protocol
	print 'domain'
	print domain
	print 'path:'
	print path
	print '--------'

	link = protocol + '://' + domain
	if len(path) > 1:
		link = link + '/' + path

	return link


def main():

	#    start by asking for a link
	toCrawl = []
	crawled = []
	toCrawl.append(getLinkToPage())
	#    print "got page " + pageLink

	maxPagesSearched = 100
	i = 0

	#   search this page for links
	while len(toCrawl) > 0:
		# get first entry of "toCrawl" list
		crawl = toCrawl.pop()

		# ensure that this link is not contained in the "crawled" list
		if crawl in crawled:
			# continue with the next loop
			continue

		if link in crawled:
			#continue with the next loop
			continue

		links = crawlPage(crawl)

		# put into "crawled" list
		crawled.append(crawl)

		# add new found links to "toCrawl" list
		for link in links:
			# ensure that the link is not in the "crawled" list
			if link not in crawled:
				toCrawl.append(makeAbsoluteLink(link, crawl))
				print makeAbsoluteLink(link, crawl)

		#stop loop after .. iterations
		i += 1
		if i >= maxPagesSearched:
			break

	return 0
