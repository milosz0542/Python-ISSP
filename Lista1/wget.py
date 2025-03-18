from urllib.request import urlretrieve
import sys

# Save sys args to variable
url = sys.argv[1]

# Get filename from url
filename = url.split('/')[-1] if url[-1] != '/' else 'index.html'

# Check if the url is valid and download the file
try:
    urlretrieve(url, filename)
    print('Downloaded')
except:
    print('Invalid URL')
    sys.exit()