import urllib.request,json
from .models import Quotes

# Getting api key
api_key = None
def configure_request(app):
    global BASE_URL
    BASE_URL =app.config['QUOTES_API_URL']
    BASE_URL = None

def get_quote():
    '''
    Function that gets the json response to our url request
    '''
    QUOTE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'

    with urllib.request.urlopen(QUOTE_URL) as url:
        get_quote_data = url.read()
        quote_response = json.loads(get_quote_data)
        if quote_response:
            author=quote_response['author']
            quote=quote_response['quote']
            permalink=quote_response['permalink']
            
        new_random_quote=Quotes(author,quote,permalink)
    return new_random_quote