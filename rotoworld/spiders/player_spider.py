import scrapy

class PlayerSpider(scrapy.Spider):
    name = "players"

    def start_requests(self):
        urls = [ "http://www.rotoworld.com/player/nba/" + str(x) for x in range(1,1000)]
        
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
        table_items =  response.xpath('//*[contains(@id,"tblPlayerDetails")]//tr//td/text()').extract()
        name_items =  response.css('.playername h1::text').extract()
        yield {
            'name' : name_items[0].split('|')[0].strip(),
            'pos': name_items[0].split('|')[1].strip(),
            'dob': table_items[2].split()[2].strip(),
            'height': table_items[4].split()[0].strip(),
            'weight': table_items[4].split()[2].strip()
        }
