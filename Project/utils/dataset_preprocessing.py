import numpy as np
import pandas as pd
from .utility_functions import *
from tld import get_tld

def preprocessing(urldata):
    urldata['url_length'] = urldata['url'].apply(lambda i: len(str(i)))
    urldata['hostname_length'] = urldata['url'].apply(lambda i: len(urlparse(i).netloc))
    urldata['path_length'] = urldata['url'].apply(lambda i: len(urlparse(i).path))
    urldata['fd_length'] = urldata['url'].apply(lambda i: fd_length(i))
    urldata['tld'] = urldata['url'].apply(lambda i: get_tld(i,fail_silently=True))
    urldata['tld_length'] = urldata['tld'].apply(lambda i: tld_length(i))
    # print(urldata.head())
    urldata = urldata.drop("tld",1)
    urldata['count-'] = urldata['url'].apply(lambda i: i.count('-'))
    urldata['count@'] = urldata['url'].apply(lambda i: i.count('@'))
    urldata['count?'] = urldata['url'].apply(lambda i: i.count('?'))
    urldata['count%'] = urldata['url'].apply(lambda i: i.count('%'))
    urldata['count.'] = urldata['url'].apply(lambda i: i.count('.'))
    urldata['count='] = urldata['url'].apply(lambda i: i.count('='))
    urldata['count-http'] = urldata['url'].apply(lambda i : i.count('http'))
    urldata['count-https'] = urldata['url'].apply(lambda i : i.count('https'))
    urldata['count-www'] = urldata['url'].apply(lambda i: i.count('www'))
    urldata['count-digits']= urldata['url'].apply(lambda i: digit_count(i))
    urldata['count-letters']= urldata['url'].apply(lambda i: letter_count(i))
    urldata['count_dir'] = urldata['url'].apply(lambda i: no_of_dir(i))
    # print(urldata.head())
    urldata['use_of_ip'] = urldata['url'].apply(lambda i: having_ip_address(i))
    urldata['short_url'] = urldata['url'].apply(lambda i: shortening_service(i))
    # print(urldata.head())
    return urldata