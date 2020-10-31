from stoic_quotes import twit_quotes
import csv
import sys

sys.stdout = open('quote_text_tweets.csv', 'w')
csv_writer = csv.writer(sys.stdout)
csv_writer.writerow(['QUOTE'])
index = 0

for quote in twit_quotes:
    csv_writer.writerow([twit_quotes[index]])
    index += 1


# This script simply writes all the content of the twit_quotes list into a .csv file for me to use in my bot code.
