from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,classification_report,accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from configuration import *
import pandas as pd
from utils.utility_functions import *

urldata = pd.read_csv(PREPROCESSED_DATASET)

x = urldata[['hostname_length','path_length', 'fd_length', 'tld_length', 'count-', 'count@', 'count?',
             'count%', 'count.', 'count=', 'count-http','count-https', 'count-www', 'count-digits','count-letters', 'count_dir', 'use_of_ip']]
y = urldata['result']
# print(x.shape)
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.3, random_state=42)

################ Testing with our data ########################
# test_url = "http://192.168.61.2.org/adffcfg/szgdh/bbakjdxkjls/sacfhgbhdsgvfhhgkrkfdbkfjdb/@#vbgfjghgdckjfvjhvgjkv@@#$$%r/"
test_url = "https://www.wikipedia.com"
hostname_length = lambda i: len(urlparse(i).netloc)
pred = []
length = hostname_length(test_url)
pred.append(length)
path_length_finder1 = lambda i: len(urlparse(i).path)
path_length = path_length_finder1(test_url)
pred.append(path_length)
fd_length_finder = lambda i: fd_length(i)
fd_length = fd_length_finder(test_url)
pred.append(fd_length)
tld_length_finder= lambda i: tld_length(i)
tld_length = tld_length_finder(test_url) 
pred.append(tld_length)
count_hiphen_finder = lambda i: i.count('-')
count_hiphen = count_hiphen_finder(test_url) 
pred.append(count_hiphen)
count_at_finder = lambda i: i.count('@')
count_hiphen = count_at_finder(test_url)
pred.append(count_hiphen)

count_questionmark_finder = lambda i: i.count('?')
count_questionmark = count_questionmark_finder(test_url)
pred.append(count_questionmark)

count_percentage_finder = lambda i: i.count('%')
count_percentage = count_percentage_finder(test_url)
pred.append(count_percentage)

count_dot_finder = lambda i: i.count('.')
count_dot = count_dot_finder(test_url)
pred.append(count_dot)

count_equalto_finder = lambda i: i.count('=')
count_equalto = count_equalto_finder(test_url)
pred.append(count_equalto)

count_http_finder = lambda i: i.count('http')
count_http = count_http_finder(test_url)
pred.append(count_http)

count_https_finder = lambda i: i.count('https')
count_https = count_https_finder(test_url)
pred.append(count_https)

count_www_finder = lambda i: i.count('www')
count_www = count_www_finder(test_url)
pred.append(count_www)

count_digits_finder = lambda i: digit_count(i)
count_digits = count_digits_finder(test_url)
pred.append(count_digits)

count_letters_finder = lambda i: letter_count(i)
count_letters = count_letters_finder(test_url)
pred.append(count_letters)


count_directories_finder = lambda i: no_of_dir(i)
count_directories = count_directories_finder(test_url)
pred.append(count_directories)

count_ip_address_finder = lambda i: having_ip_address(i)
count_ip_address = count_ip_address_finder(test_url)
pred.append(count_ip_address)

print(pred)
pred_2d = []
pred_2d.append(pred)
print(pred_2d)

rfc = RandomForestClassifier()
rfc.fit(x_train, y_train)
rfc_predictions = rfc.predict(pred_2d)
print(rfc_predictions)
if rfc_predictions[0] == 1:
    print("Malicious URL")
else:
    print("URL is benign")
# accuracy_score(y_test, rfc_predictions)
# print(confusion_matrix(y_test,rfc_predictions))