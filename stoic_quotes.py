from bs4 import BeautifulSoup
import requests

# Information is passed into a few different lists as the script runs. I probably could have accomplished this with less lists, but this made it easier to code
# and easier to read/understand what stage the information is in each list
stoic_quotes = []
stoic_quotes_decoded = []
twit_quotes = []
index = 0

# This is the function to be used to visit urls and iterate through pages. The number of pages to iterate through is defined by web_page_num. 
# the author is also added in this step. It was the least complicated way I could find to print the correct author at the end of their respective quotes
def get_stoic_quotes(url, web_page_num, author):
    
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
                
            # You never know what weird characters will show up while scraping for quotes. I needed to remove all non-ascii characters.
            stoic_quote = (quotes_raw[0]).encode('ascii', 'ignore')

            quote_decoded = stoic_quote.decode()
            stoic_quotes_decoded.append(quote_decoded)
            
            # list comprehension to get rid of quotes of some empty quotes
            stoic_quotes_decoded = [i for i in stoic_quotes_decoded if not i.startswith(' ')]

            full_quote = (stoic_quotes_decoded[inner_index], '\n', '\n', author)
            inner_index += 1
            stoic_quotes.append(full_quote)



# Simply add the url to the goodreads page containing the stoic philosopher you want to scrape quotes for. I limited my own search to 5 pages as it seemed
# after that, the quotes began repeating or were gernerally just incorrect. Since each page will contain 30 quotes, we end up with 450 quotes total
get_stoic_quotes('https://www.goodreads.com/work/quotes/31010?', 5, 'Marcus Aurelius')
get_stoic_quotes('https://www.goodreads.com/work/quotes/93900-epistulae-morales-ad-lucilium?', 5, 'Seneca The Younger')
get_stoic_quotes('https://www.goodreads.com/work/quotes/1889585?', 5, 'Epictetus')

# filter to get rid of quotes with a length greater than 281.
stoic_quotes_clean = list(filter(lambda quote_text: len(quote_text) < 281, stoic_quotes))

# since the list consists of tuples, I had to find another way to get all of the information I wanted in the correct format.
for item in stoic_quotes_clean:
    twit_quotes.append(str(item[0]) + (item[1]) + (item[2]) + item[3])
    index += 1
