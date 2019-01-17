#!/usr/bin/env python
# encoding: utf from xml.dom 

from xml.dom import *
from xml.dom.minidom import parse
from urllib2 import urlopen
from sys import argv

# Overall program illustrates the glorious support
# Python has for XML.  The xml.dom.minidom module
# provides the parse method, which knows how to 
# pull XML content through an open internet connection
# and build an in-memory, tree version of the document.
# The full xml.dom package is what defines the Document

def listAllArticles(rssURL):
"""Lists all of the titles of the articles identified by the specified feed"""
  conn = urlopen(rssURL)
  xmldoc = parse(conn)
  items = xmldoc.getElementsByTagName("item")
  for item in items:
    titles = item.getElementsByTagName("title")
    title = titles[0].
    childNodes[0].nodeValue
    print("Article Title: %s" % title.encode('utf-8'))
    
def extractFeedName():
"""Pulls the URL from the command line if there is one, but otherwise uses a default."""
  defaultFeedURL = "http://feeds.chicagotribune.com/chicagotribune/news/"
  feedURL = defaultFeedURL
  if (len(argv) == 2):
    feedURL = argv[1]
  return feedURL
  
listAllArticles(extractFeedName())
