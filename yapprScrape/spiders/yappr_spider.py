# -*- coding: utf-8 -*-
import scrapy
from yapprScrape.items import YapprItem


class YapprSpiderSpider(scrapy.Spider):
    name = 'yappr_spider'
    main_url = "http://www.fci.be"

    start_urls = [main_url + '/en/Nomenclature/Default.aspx/']

    def parse(self, response):
        # get letters
        letters = response.xpath("//ul[@class='initiales']/li/a/text()").extract()

        # scrape letters
        # for l in [letters[0]]:
        for l in letters:
            yield scrapy.Request(self.main_url + "/en/nomenclature/races.aspx?init=" + l, callback=self.parse_letter)

    def parse_letter(self,response):
        # get breed links
        breed_links = response.xpath('//ul[@class="listeraces"]/li/a/@href').extract()

        # for b in breed_links[0:2]:
        for b in breed_links:
            yield scrapy.Request(self.main_url + b, callback=self.parse_breed)

    def parse_breed(self, response):
        original_label = response.xpath('//*[@id="ContentPlaceHolder1_NomOrigineLabel"]//text()').get()
        breed_id = response.xpath('//*[@id="ContentPlaceHolder1_NumeroLabel"]//text()').get()
        group = response.xpath('//*[@id="ContentPlaceHolder1_GroupeHyperLink"]//text()').get()

        english = response.xpath('//*[@id="ContentPlaceHolder1_NomEnLabel"]/text()').get()
        french = response.xpath('//*[@id="ContentPlaceHolder1_NomFRLabel"]/text()').get()
        german = response.xpath('//*[@id="ContentPlaceHolder1_NomDELabel"]/text()').get()
        spanish = response.xpath('//*[@id="ContentPlaceHolder1_NomESLabel"]/text()').get()

        section = response.xpath('//*[@id="ContentPlaceHolder1_SectionLabel"]/text()').get()
        subsection = response.xpath('//*[@id="ContentPlaceHolder1_SousSectionLabel"]/text()').get()
        date_of_acceptance = response.xpath('//*[@id="ContentPlaceHolder1_DateReconnaissanceLabel"]/text()').get()
        official_lang = response.xpath('//*[@id="ContentPlaceHolder1_LangueOrigineLabel"]/text()').get()
        date_of_publish = response.xpath('//*[@id="ContentPlaceHolder1_DateStandardEnVigueurLabel"]/text()').get()
        status = response.xpath('//*[@id="ContentPlaceHolder1_StatutLabel"]/text()').get()
        country = response.xpath('//*[@id="ContentPlaceHolder1_PaysOrigineLabel"]/text()').get()
        working_trial = response.xpath('//*[@id="ContentPlaceHolder1_EpreuveTravailLabel"]/text()').get()

        item = YapprItem()
        item["original_label"] = original_label
        item["breed_id"] = breed_id
        item["group"] = group
        item["english"] = english
        item["french"] = french
        item["german"] = german
        item["spanish"] = spanish
        item["section"] = section
        item["subsection"] = subsection
        item["date_of_acceptance"] = date_of_acceptance
        item["official_lang"] = official_lang
        item["date_of_publish"] = date_of_publish
        item["status"] = status
        item["country"] = country
        item["working_trial"] = working_trial
        yield item