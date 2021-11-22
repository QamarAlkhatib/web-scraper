import requests
from bs4 import BeautifulSoup


def get_citations_needed_count(URL):
    res = requests.get(URL)
    soup = BeautifulSoup(res.content,'html.parser')

    res_div = soup.find('div', id='bodyContent')
    res_p = res_div.find_all('p')

    all_citation_needed = []
    for i in res_p:
        count = i.find_all('sup', class_='noprint Inline-Template Template-Fact')
        if count != []:
            all_citation_needed.append(count)
            get_text = i.get_text().strip()
    num_of_citation = len(all_citation_needed)
    print(num_of_citation)
    return num_of_citation

def get_citations_needed_report(URL):
    res = requests.get(URL)
    soup = BeautifulSoup(res.content,'html.parser')

    res_div = soup.find('div', id='bodyContent')
    res_p = res_div.find_all('p')
    all_string_text=[]
    for i in res_p:
        string_text=i.find_all('sup',class_="noprint Inline-Template Template-Fact")
        if string_text != []:
            all_string_text.append(string_text)
            text=i.get_text().strip()
            print(text)
    return text
    

get_citations_needed_count('https://en.wikipedia.org/wiki/History_of_Mexico')
get_citations_needed_report('https://en.wikipedia.org/wiki/History_of_Mexico')
