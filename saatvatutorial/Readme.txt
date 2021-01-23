display the expectation of scrappy
    Define website link
    Scrappy goes to the website 
    Extracts the data in “xpath”

Step 0: design what information you want to display
    https://www.saatva.com/mattresses/saatva-classic 
        Mattress name
        size
        price
NOTE: Scrapy does not work on the saatva website!!!!!

Install scrapy: Pip install scrapy

Change directory to desired location:
    Ls to check files
    Cd desktop
    Create project
        Scrapy startproject saatvaproj
    Create spider file
        saatvaproj/spiders/ new_py_file.py
Code!
    Import scrapy
    Create class
        Works similar to a function
        Define a name
        The variable name in paranthesis (library_name.variable)
    defining global variables and functions
        Global variables are needed to for your website link
        Functions are used to extract data from the website
Xpath
    Testing xpath: 
        open terminal
        Execute: scrapy shell <weblink>
        Ex: 
            response.xpath('//h1[class=productPanel__headingTitle]/text()').extract()
            response.xpath('//h1[@class="productPanel__headingTitle"]/text()').extract()  
            response.xpath('//h1[@class="productPanel__headingTitle"]/text()').extract_first()
Getting “Queen”
    Pull xpath:
        <div class="u-fullWidth u-flexDisplay u-flexJustify--spaceBetween"><span>Queen</span><div class="strikethroughPrice"><span>$1,199</span>&nbsp;<span class="strikethroughPrice__original">$1,399</span></div></div>
        <div class="u-fullWidth u-flexDisplay u-flexJustify--spaceBetween"><span>Queen</span><div class="strikethroughPrice"><span>$1,199</span>&nbsp;<span class="strikethroughPrice__original">$1,399</span></div></div>
    Test xpath:
        response.xpath('//div[@class="u-fullWidth u-flexDisplay u-flexJustify--spaceBetween"]').extract()
        response.xpath('//div[@class="u-fullWidth u-flexDisplay u-flexJustify--spaceBetween"]/span/text()').extract()
    We found queen…. But it is in a list
Getting price:
    Test the xpath using the xpath above: response.xpath('//div[@class="strikethroughPrice"]/span/text()').extract()
    We get a list of prices but no indicator the correct price with the size.

Time saver:
    The javascript changes based on user actions
