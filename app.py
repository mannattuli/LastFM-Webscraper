import requests 
import bs4

result = requests.get("https://www.last.fm/user/mxnnxtz")
soup = bs4.BeautifulSoup(result.text, "lxml")

songRightNow = soup.select(".chartlist-name")[0]
print(songRightNow.text.replace("\n", ""))

artistRightNow = soup.select(".chartlist-artist")[0]
print(artistRightNow.text.replace("\n", ""))

image = soup.select('img')[4]
links = image['src']
print(image)

file = open("index.html","r+")
file.truncate(0)
file.close()

with open("index.html", "a") as f:
	f.write('<html>')
	f.write('<head>')
	f.write('<title>Songs</title>')
	f.write('</head>')
	f.write('<body style="background-color: #121212; color: wheat">')
	f.write('<h1>Song</h1>')
	f.write("Currently listening to: " + songRightNow.text.replace("\n", ""))
	f.write("<br> By: " + artistRightNow.text.replace("\n", ""))
	f.write("<br>")
	f.write('<img src="' + links + '" style="height:100px; width:100px">')
	f.write('</body>')
	f.write('</html>')
	file.close()
