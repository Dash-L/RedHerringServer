import requests
from bs4 import BeautifulSoup

def remove_chars(old_str, chars):
    """Removes each character in the string `chars` from `old_str` and returns the new string"""
    new_string = old_str
    for char in chars:
        new_string = new_string.replace(char, '')
    
    return new_string

def strip_headlines(headlines):
    return [remove_chars(headline.upper(), '\'"-\u2018\u2019\u201A\u201B\u201C\u201D\u201E\u201F') for headline in headlines]

def get_headlines():
    data = []
    # urls could be saved in a separate file
    urls = {
        'https://forbes.com/': {"selector":"a", "class":'happening__title'},
        'https://bbc.com/news/': {"selector":"a", "class":'gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor'},
        'https://newyorker.com/': {"selector":"h3", "class":'Card__hed___31cLY'},
        'https://foreignaffairs.com/': {"selector":"p", "class":'magazine-deck ls-0 mb-0 f-serif'},
        'https://theatlantic.com/most-popular': {"selector":"h2", "class":'LandingRiver_title__ifZrN'},
        'https://www.theatlantic.com/latest/': {"selector":"h2", "class":"hed"},
        'https://www.economist.com/': {"selector":"a", "class":"headline-link"},
        'https://cnn.com/us': {"selector":"span", "class":"cd__headline-text vid-left-enabled"},
        'https://cnn.com/business': {"selector":"span", "class":"cd__headline-text vid-left-enabled"},
        'https://politico.com/': {"selector":"h3", "class":"headline"},
        'https://today.com': {"selector":"h2", "class":"tease-card__headline"},
        'https://npr.org': {"selector":"h3", "class":"title"},
    }
    for url, info in urls.items():
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'lxml')
        for selector in soup.find_all(info["selector"], class_=info["class"]):
            if not 'video' in selector.text.lower():
                if len(selector.text.strip().split(" ")) >= 4: # removing short headlines because they mess with the results
                    data.append(selector.text.strip())

    return strip_headlines(list(set(data))) 