from bs4 import BeautifulSoup
import requests
from imdb.items import ImdbItem
import scrapy
import re

class IMDBSpider(scrapy.Spider):
    name = "imdb"
    allowed_domains = ["imdb.com"]
    start_urls = ["https://www.imdb.com/chart/top"]

    def parse(self,response):
        soup = BeautifulSoup(response.text)
        movies = soup.find("tbody",{"class":"lister-list"})
        for movie in movies.findAll("tr"):
            item = ImdbItem()
            poster = movie.find("td",{"class":"posterColumn"})
            item["score"]= poster.find("span",{"name":"ir"})["data-value"]
            movie_link = movie.find("td",{"class":"titleColumn"}).find('a')["href"]
            url = "http://www.imdb.com" + movie_link
            year_str = movie.find("td",{"class":"titleColumn"}).text
            year_pattern = re.compile('\d{4}')
            item["year"] = int(year_pattern.search(year_str).group())
            id_pattern = re.compile(r'(?<=tt)\d+(?=/?)')
            item["movie_id"] = int(id_pattern.search(movie_link).group())
            item["movie_name"] = movie.select_one('.titleColumn').select_one('a').string
            # yield item
            yield scrapy.Request(url, meta={'item': item}, callback = self.parse_2)


    def parse_2(self,response):
        soup = BeautifulSoup(response.text, 'lxml')

        item = response.meta['item']
        item["director"]= soup.find("div",{"class":"credit_summary_item"}).find("a").text
        yield item
        # soup["actors"] =


