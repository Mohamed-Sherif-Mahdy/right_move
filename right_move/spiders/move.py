#importing the libraries
import scrapy
#making the class inheriting scrapy.Spider class
class MoveSpider(scrapy.Spider):
    name = 'move' #name of the spider
    allowed_domains = ['rightmove.co.uk'] #allowed domains
    #starting urls
    start_urls = ['https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E1498&index={}&propertyTypes=&includeLetAgreed=false&mustHave=&dontShow=&furnishTypes=&keywords='.format(i) for i in range(1,198,24)]
    #function to parse the data
    def parse(self, response):
        #  #selecting all ads in the page and extracting price,address, size, descriotion,date, added by of each one ad
        for house in response.css("div.l-searchResult.is-list") :
            yield {
                'price': house.css("span.propertyCard-priceValue::text").get(),
                'address': house.css("address.propertyCard-address>meta::attr(content)").get(),
                'size': response.css("h2.propertyCard-title::text").get().replace("\n            ","").replace("        ","").split(),
                'description':house.css("a.propertyCard-link>span::text").get(),
                'date':house.css("span.propertyCard-branchSummary-addedOrReduced::text").get(),
                'added_by':house.css("span.propertyCard-branchSummary-branchName::text").get()
            }
        

