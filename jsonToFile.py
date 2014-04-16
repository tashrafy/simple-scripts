#!/usr/bin/python

"""This is a simple python script to simply fetch a JSON response from an API/
server-side endpoint, and output it to a file.
"""

import os
import sys
import urllib
import urllib2
import json

def fetchFeed(requestURL):
  """
    This function simply reads the json response from a url and stores it to a file.
  """
  request   = urllib2.Request(requestURL)
  response  = urllib2.urlopen(request)
  save_feed = response.read()
  fileOutput = open('response.json', 'wb+')
  fileOutput.write(save_feed)
  fileOutput.close()
  
def main():
  # TODO: Implement multiple arguments for url parameters
  # fetch_func = getattr(sys.modules[__name__], sys.argv[1])
  # endpoint = sys.argv[2]
  # fetch_func(endpoint)
  # To test, simply pass in a url 'string' from command line:
  # For example: 
  #   python jsonToFile.py 'http://wwww.helloworld.com/get?user=bob'
  
  endpoint = sys.argv[1]
  fetchFeed(endpoint)
  
if __name__ == "__main__":
    main()