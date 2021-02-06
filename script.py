import json
import re
import os
import curlify
import requests

#Ask user for search query and replace whitespace with '+' sign
query = input("Please enter a search query: ")
query = re.sub("\s+", "+", query.strip())

#append the url with user input query. This will be our request url
url = "https://pixabay.com/api/videos/?key=19967863-5e5af76c750214a4d4d221b38&q=" + query + "&pretty=true&min_width=1920&min_height=1080"

#Request url for json data
response = requests.get(url).json()

# Make a new directory for every search query
if not os.path.exists(query):
	os.makedirs(query)

#Counter for total no. of files
i = 0

for each in response['hits']:

	i = i+1;
	#print (each['videos']['large']['url'])

	#Make request to each url from json data
	#Extract filename from url 
	r = requests.get(each['videos']['large']['url'], allow_redirects=True)
	fileurl = (r.url)
	filename = fileurl.split("filename=")[-1] 
	
	#Join the filename with desired directory
	directory = './' + query + '/'
	file_path = os.path.join(directory, filename)
	
	#Open file in desired path, write and close it
	writefile = open(file_path, 'wb')
	writefile.write(r.content)
	writefile.close()
	print ( str(i) + " File Downloaded!")
