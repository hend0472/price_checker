import requests
import bs4
import time
import random
import webbrowser


print('''
██████╗ ██████╗ ██╗ ██████╗███████╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗
██╔══██╗██╔══██╗██║██╔════╝██╔════╝    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██████╔╝██████╔╝██║██║     █████╗      ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
██╔═══╝ ██╔══██╗██║██║     ██╔══╝      ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║     ██║  ██║██║╚██████╗███████╗    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝╚═╝ ╚═════╝╚══════╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝''')
print('\n\n')
time.sleep(1)

header_1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
						  'Chrome/54.0.2840.71 Safari/537.36'}
header_2 = {'User-Agent': 'Mozilla/5.0'}
header_3 = {'User-Agent': 'my-app/0.0.1'}
header_4 = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
header_5 = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
header_6 = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "en-US,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
}


header_list = []
header_list.append(header_1)
# header_list.append(header_2)
# header_list.append(header_3)
header_list.append(header_4)
header_list.append(header_5)
header_list.append(header_6)


def check_barcode():
	try:
		global price_list
		price_list = {}
		scan = str(input('\nSCAN BARCODE: '))
		get_item_name(scan)
		open_search_pages(scan, product_name)

	except Exception as e:
		print('ITEM NOT FOUND.')
		print(e)
		pass


def get_item_name(barcode):
	global product_name
	base_url = 'https://www.upcdatabase.com/item/' + str(barcode)
	res = requests.get(base_url)
	soup = bs4.BeautifulSoup(res.text, 'html.parser')
	table = soup.find('table', attrs={'class': 'data'})
	product_name = ''
	for item in table.findAll('tr'):
		for item2 in item.findAll('td'):
			product_name += item2.text + ' '
	shit_words = ['UPC-A', 'EAN/UCC-13', 'Description', 'Size/Weight']
	for word in shit_words:
		if word in product_name:
			product_name = str(product_name).replace(word, '')
	product_name = product_name.split('Issuing Country')
	product_name = str(product_name[0]).lstrip().rstrip()
	product_name = product_name.replace('  ', ' ')
	print('\nCHECKING FOR --- ' + str(product_name).upper())


def open_search_pages(barcode, product_name):
	amazon_page = 'https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=' + str(barcode)
	amazon_page2 = 'https://www.amazon.com/s/ref=nb_sb078742371535' \
				   '_noss_2?url=search_alias%3Daps&field-keywords=' + str(
		product_name)
	walmart_page = 'https://www.walmart.com/search/?query=' + str(product_name)
	ebay_page = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=' + str(product_name).replace(' ',
				 '+') + '&_sacat=0'
	etsy_page = 'https://www.etsy.com/search?q=' + str(product_name)
	google_shop_page = 'https://www.google.com/search?q=' + str(barcode) + '&source=lnms&tbm=shop'
	webbrowser.open(google_shop_page)
	webbrowser.open(walmart_page)
	webbrowser.open(amazon_page)
	webbrowser.open(amazon_page2)
	webbrowser.open(ebay_page)
	webbrowser.open(etsy_page)




if __name__ in '__main__':
	while True:
		check_barcode()
