import scrapy

class PlayerSpider(scrapy.Spider):
    name = "players"

    def start_requests(self):
        urls = [ "http://www.rotoworld.com/player/nba/" + str(x) for x in range(1,500)]
        
        #urls = [
        #    'http://www.rotoworld.com/player/nba/1',
        #    'http://www.rotoworld.com/player/nba/2',
        #    'http://www.rotoworld.com/player/nba/3',
        #    'http://www.rotoworld.com/player/nba/4',
        #    'http://www.rotoworld.com/player/nba/5'
        #]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        yield {
            'name' : response.css('.playername h1::text').extract()[0].split('|')[0],
            'pos': response.css('.playername h1::text').extract()[0].split('|')[1],
            'dob': response.xpath('//*[contains(@id,"tblPlayerDetails")]//tr//td/text()').extract()[2].split()[2],
            'height': response.xpath('//*[contains(@id,"tblPlayerDetails")]//tr//td/text()').extract()[4].split()[0],
            'weight': response.xpath('//*[contains(@id,"tblPlayerDetails")]//tr//td/text()').extract()[4].split()[2]
        }
