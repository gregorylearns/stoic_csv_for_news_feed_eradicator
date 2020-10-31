from bs4 import BeautifulSoup
import requests


stoic_quotes = []
stoic_quotes_decoded = []
twit_quotes = []
index = 0


def get_stoic_quotes(url, web_page_num, author):

    # initialize list to contain the links to be scraped
    global stoic_quotes_decoded
    global stoic_quotes
    stoic_links = []
    page_num = 1

    for pages in range(web_page_num):

        links = url + f'page={page_num}'
        links_source = requests.get(links).text
        stoic_links.append(links)

        page_num += 1

        stoic_soup = BeautifulSoup(links_source, 'html.parser')

        # Now iterating over the html data from each link. The rest is a matter of cutting the text that is returned
        # into the desired information
        inner_index = 0

        for quote in stoic_soup.find_all('div', class_='quote'):

            try:
                quotes_raw = quote.find('div', class_='quoteText').text.strip().splitlines()
            except Exception as e:
                quotes_raw = None

            stoic_quote = (quotes_raw[0]).encode('ascii', 'ignore')

            quote_decoded = stoic_quote.decode()
            stoic_quotes_decoded.append(quote_decoded)
            stoic_quotes_decoded = [i for i in stoic_quotes_decoded if not i.startswith(' ')]

            full_quote = (stoic_quotes_decoded[inner_index], '\n', '\n', author)
            inner_index += 1
            stoic_quotes.append(full_quote)




get_stoic_quotes('https://www.goodreads.com/work/quotes/31010?', 5, 'Marcus Aurelius')
get_stoic_quotes('https://www.goodreads.com/work/quotes/93900-epistulae-morales-ad-lucilium?', 5, 'Seneca The Younger')
get_stoic_quotes('https://www.goodreads.com/work/quotes/1889585?', 5, 'Epictetus')


stoic_quotes_clean = list(filter(lambda quote_text: len(quote_text) < 281, stoic_quotes))

for item in stoic_quotes_clean:
    twit_quotes.append(str(item[0]) + (item[1]) + (item[2]) + item[3])
    index += 1
