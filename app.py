import bs4
import requests
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return  render_template("index.html")

result = requests.get("https://www.last.fm/user/")
soup = bs4.BeautifulSoup(result.text, "lxml")

songRightNow = soup.select(".chartlist-name")[0]
print(songRightNow.text.replace("\n", ""))

artistRightNow = soup.select(".chartlist-artist")[0]
print(artistRightNow.text.replace("\n", ""))

file = open("templates/index.html","r+")
file.truncate(0)
file.close()

with open("templates/index.html", "a") as f:
	f.write('<html>')
	f.write('<head>')
	f.write('<title>Songs</title>')
	f.write('</head>')
	f.write('<body style="background-color: #121212; color: wheat">')
	f.write('<h1>Songs</h1>')
	f.write("Currently listening to: " + songRightNow.text.replace("\n", ""))
	f.write("<br> By: " + artistRightNow.text.replace("\n", ""))
	f.write('</body>')
	f.write('</html>')