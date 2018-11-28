# Scrapy example for capturing rotoword player data
This repo contains a Scrapy project with a simple spider set up to capture basic player stats.

Information about getting started with Scrapy can be found here:

* https://doc.scrapy.org/en/latest/intro/install.html
* https://doc.scrapy.org/en/latest/intro/tutorial.html

The basic structure of this repository is a Scrapy project started with the name 'rotoworld'. Within the 'rotoworld' directory there are some placeholder files that Scrapy makes use of including items.py which is where we can define structures to hold scraped data. There is a basic outline in items.py but it is not yet implemented in the spider.

The spider that does all the work currently is *scrapy-rotoworld/rotoworld/spiders/player_spider.py*

You can initialize a scrape by cloning this repo and running some basic scrapy commands from the command line while in the main directory (scrapy-rotoworld):

For JSON:

_scrapy crawl players -o players.json_

For CSV:

_scrapy crawl players -o players.csv -t csv_
      

