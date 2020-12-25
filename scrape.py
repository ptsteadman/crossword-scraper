import urllib.request
from datetime import datetime, timedelta
import time
from os import path

from PyPDF2 import PdfFileMerger

NUM_DAYS = 106

base = datetime.today()
date_list = [base - timedelta(days=x) for x in range(NUM_DAYS)]
date_list.reverse()
print(date_list)
date_strs = [d.strftime('%b%d%y') for d in date_list]

def output_filename(datestr):
    return './output/' + datestr + '.pdf'

for d in date_strs:
    if path.exists(output_filename(d)):
        continue
    print('Fetching ' + d)
    try:
        urllib.request.urlretrieve(
            'https://www.poblib.org/images/pdfdocs/Crosswords/' + d + '.pdf',
            output_filename(d)
        )
    except:
        print('Could not fetch crossword')
    time.sleep(2)

print(date_strs)
files = [output_filename(d) for d in date_strs]
print(files)

merger = PdfFileMerger()

for f in files:
    if path.exists(f):
        merger.append(f)

print('Writing book...')
merger.write('0utput-Crossword-Book.pdf')
merger.close()
