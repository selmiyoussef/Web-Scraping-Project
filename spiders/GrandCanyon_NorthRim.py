from National_Park_Project.items import National_Park_ProjectItem 
from scrapy import Spider

class National_Park_ProjectSpider(Spider):
    name = "GrandCanyon_NorthRim"
    allowed_urls = ['https://www.recreation.gov']
    start_urls = ['https://www.recreation.gov/campsitePaging.do?contractCode=NRSO&parkId=70970&startIdx='+str(i) for i in range(0,100,25)]
  
    def parse(self,response):
        review_t = response.xpath("//tr[@class='br']")

        for i in review_t: 
    
            Site = i.xpath('./td/div/a/text()').extract()
            Facility_Area = i.xpath('(./td)[2]/text()').extract()
            SiteType = i.xpath('(./td)[3]/text()').extract()
            Maximum_Number_of_People = i.xpath('(./td)[4]/text()').extract()
            Equiplength_or_Driveway = i.xpath('(./td)[5]/text()').extract()
            Pets =i.xpath("(./td/div[@class='amenitiesicons']/img)[3]/@title").extract()
        
            item = National_Park_ProjectItem()
            item['ParkName']=['GrandCanyon']
            item['Location']= ['North Rim CampGround']
            item['Longtitude']= ['-112.05997809999997']
            item['Latitude']= ['36.2097538']
            item['Stars'] = ['4.7']
            item['Reviews'] = ['1992']
            item['Site'] = Site
            item['Facility_Area'] = Facility_Area
            item['SiteType'] =SiteType
            item['Maximum_Number_of_People'] = Maximum_Number_of_People
            item['Equiplength_or_Driveway'] = Equiplength_or_Driveway
            item['Pets'] = Pets

            yield item


