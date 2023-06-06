Skapiec.pl eShop URL Scraper
=============================

This Python script scrapes the first 10 pages of the Skapiec.pl gardening section and saves the unique URLs of eShops to a file.

Prerequisites
-------------

- Python 3.x
- `requests` library
- `beautifulsoup4` library

Install the required libraries using the command.

Usage
-----

1. Clone the repository or download the script directly.
2. Open the script in a Python editor or IDE.
3. Run the script.

The script will scrape the specified number of pages from Skapiec.pl and save the unique eShop URLs along with their corresponding page numbers to a file named `eshop_urls.txt` in the same directory as the script.

Customization
-------------

- To scrape a different number of pages, modify the range in the `for` loop (`for page_number in range(1, 11)`).
- To change the target URL, update the `skapiec_url` variable.
- If the CSS class for eShop URLs changes, adjust the `class_` parameter in the `find_all` method accordingly.


