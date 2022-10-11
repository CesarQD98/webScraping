# webScrapCyc.py - Opens in the browser the cheapest microphone on sale

import webbrowser
import requests
import sys
import bs4

try:
    res = requests.get('https://cyccomputer.pe/busqueda?controller=search&orderby=position&orderway=desc&search_category=all&s=' +
                       str(sys.argv[1]) + '&order=product.price.asc')
    res.raise_for_status()
    cheapest = bs4.BeautifulSoup(res.text, 'html.parser')
    microphones = cheapest.select('div > article > div > div.laber-product-description > h2 > a')[0]
    print(microphones.getText())
    print(microphones.attrs)

    cheapestURL = microphones.get('href')

    webbrowser.open(cheapestURL)
        


except:
    print('More than one word inputs should be typed with double quotes -> \"\"')
