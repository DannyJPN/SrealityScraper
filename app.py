from flask import Flask, render_template, request, jsonify
import logging
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.sreality_spider import SrealityScraper

app = Flask(__name__, static_folder='static')

# Configure logging
logging.basicConfig(level=logging.DEBUG)

propTypes = [
  { "id":"byty", "text":"Byty"},
  { "id":"domy", "text":"Domy"},
  { "id":"pozemky", "text":"Pozemky"},
  { "id":"komercni", "text":"Komerční"},
  { "id":"ostatni", "text":"Ostatní"}
]

adTypes = [
  { "id":"prodej", "text":"Prodej"},
  { "id":"pronajem", "text":"Pronájem"},
  { "id":"drazba", "text":"Dražba"},
  { "id":"podil", "text":"Podíl"}
]


@app.route("/")
def main_page():
    return render_template('index.html',propTypes=propTypes,adTypes=adTypes)

@app.route("/compose-url", methods=["GET"])
def compose_url():
    try:
        property_type = request.args.get('property_type')
        transaction_type = request.args.get('advert_type')
        target_url = f"https://www.sreality.cz/hledani/{transaction_type}/{property_type}"
        logging.info(f"Composed URL: {target_url}")
        scraped_data=[]
        # Set up and start the Scrapy spider
        #process = CrawlerProcess(get_project_settings())
        #process.crawl(SrealityScraper, url=target_url)
        #process.start()
        #
        ## Assuming the spider stores results in a class variable `items`
        #scraped_data = SrealityScraper.items

        return render_template('index.html',propTypes=propTypes,adTypes=adTypes, target_url=target_url, scraped_data=scraped_data,property_type=property_type,transaction_type=transaction_type)
    except Exception as e:
        logging.error(f"Error composing URL: {str(e)}", exc_info=True)
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(port=8000)