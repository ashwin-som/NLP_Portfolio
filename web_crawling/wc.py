from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from heapq import heapify, heappush, heappop
import pickle


def get_urls(starting_url): #this function mainly creates 15 urls based on the url given so that we can go through them (using beautiful soup)
    results = requests.get(starting_url)
    data = results.text
    crawler =  BeautifulSoup(data,features='html.parser')
    #unique_hosts = set()
    #unique_hosts = set(['www.linkedin.com','itunes.apple.com','play.google.com','id.ndl.go.jp','www.idref.fr','catalogue.bnf.fr','id.loc.gov','auth.fandom.com'])
    output = []
    cnt = 0
    for link in crawler.find_all('a'):
        href_link = link.get('href')
        if href_link!=None and href_link.find('https')!=-1:
            #print(href_link)
            pass
        else:
            continue
        host = urlparse(href_link).hostname
        #print(host)
        tr = requests.get(href_link)
        t = tr.text
        #print(t)
        
        if t.lower().find('star wars')!=-1:  #used to find only relevant links
            output.append(href_link)

            #unique_hosts.add(host)
            cnt+=1
            #print(cnt)
        if cnt==15:
            break

    return output

def parse_text(url, filename): #This function parses each of the urls to find all the paragraph text to add to unique files for each url
    f = open(filename,'w')
    result = requests.get(url)
    data = result.text
    scraper =  BeautifulSoup(data,features='html.parser')
    for p in scraper.find_all('p'):
        f.write(p.get_text())
        f.write('\n')
    print('File saved: ',filename)

def clean_text(): #This function cleans the text by removing new lines among others, then creates new sentences and puts them in new files
    file = 'file'
    out = 'sent'
    for i in range(1,16):
        filename = file+str(i)+'.txt'
        #print(filename)
        f = open(filename,'r')
        text_data = f.read().replace('\n',' ')
        f.close()
        sent_list = sent_tokenize(text_data) #tokenizes text into list of sentences
        output_file = out+str(i)+'.txt'
        f = open(output_file,'w')
        for s in sent_list:
            f.write(s)
            f.write('\n')
    print('files cleaned')


def top_25(): #This function heapifies the map with terms count and extracts the top 40
    file = 'sent'
    tf_map = {}
    for i in range(1,16):
        filename = file+str(i)+'.txt'
        f = open(filename)
        sent_list = f.readlines()
        for s in sent_list:
            s = s.lower()
            words = word_tokenize(s)
            for word in words:
                if word.isalpha() and word not in stopwords.words('english') and len(word)>=5: #Checking only proper terms to be include in dictionary
                    if word in tf_map:
                        tf_map[word]-=1
                    else:
                        tf_map[word] = -1
    list_from_map = list(tf_map.items()) 
    heap = [(i[1],i[0]) for i in list_from_map]
    heapify(heap)
    tf_list = []
    for i in range(40):
        (val,key) = heappop(heap)
        tf_list.append(key)
    return tf_list


def create_knowledge_base(word_list): #This function is used to create the knowledge base by adding sentences which containa top 10 words
    knowledge_base = {}
    for word in word_list:
        knowledge_base[word] = []
        file = 'sent'
        tf_map = {}
        for i in range(1,16):
            filename = file+str(i)+'.txt'
            f = open(filename)
            sent_list = f.readlines()
            for s in sent_list:
                if word in s.lower():
                    knowledge_base[word].append(s.strip())

    return knowledge_base 

    


if __name__ == '__main__':
    starting_link = 'https://starwars.fandom.com/wiki/Star_Wars'

    urls = get_urls(starting_link)
    file = 'file'
    c = 1
    for url in urls:
        print(url)
        filename = file+str(c)+'.txt'
        c+=1
        parse_text(url,filename)
    clean_text()
    print('Here are the top 40 entries with the highest term frequency')
    print(top_25())
    my_10_terms = ['empire','republic','mandalorian','skywalker','lucasfilm','disney','kenobi','anakin','lucas','trilogy']
    kb = create_knowledge_base(my_10_terms)
    pickle.dump(kb, open('kb.p','wb')) #dumping kb into a pickle file
    print('Sentences related to mandalorian (example of the knowledge base): ')
    print(kb['mandalorian'][0])
    print(kb['mandalorian'][1])
    print(kb['mandalorian'][2])
    print(kb['mandalorian'][3])
    print(kb['mandalorian'][4])
    
    exit()
    

    



