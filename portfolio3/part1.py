from nltk import word_tokenize
from nltk.util import ngrams
import pickle
import sys

def process_csv(filename):   #This function processes the file to create unigram and bigram dictionaries for each
    file = open(filename)
    text_data = file.read().replace('\n',' ')
    unigrams = word_tokenize(text_data)
    bigrams = list(ngrams(unigrams,2))
    unigram_set = set(unigrams)
    bigram_set = set(bigrams)

    unigram_map = {}
    bigram_map = {}
    for unigram in unigram_set:
        unigram_map[unigram] = unigrams.count(unigram)    #creating the unigram dicionary

    for bigram in bigram_set:
        bigram_map[bigram] = bigrams.count(bigram)     #creating the bigram dictionary

    return unigram_map, bigram_map

if __name__ == "__main__":
    path = ''
    if len(sys.argv) <4:
        print('Please provide the path to the data file as a system arg')
    else:
        english_path = sys.argv[1]          
        french_path = sys.argv[2]
        italian_path = sys.argv[3]
        #We are dumping the 6 dictionaries into pickle files
        e_uni_map,e_bi_map = process_csv(english_path)
        pickle.dump(e_uni_map, open('e_uni_map.p','wb'))
        pickle.dump(e_bi_map, open('e_bi_map.p','wb'))
        print('Finished english dictionaries')
        f_uni_map,f_bi_map = process_csv(french_path)
        pickle.dump(f_uni_map, open('f_uni_map.p','wb'))
        pickle.dump(f_bi_map, open('f_bi_map.p','wb'))
        print('Finished french dictionaries')
        i_uni_map,i_bi_map = process_csv(italian_path)
        pickle.dump(i_uni_map, open('i_uni_map.p','wb'))
        pickle.dump(i_bi_map, open('i_bi_map.p','wb'))
        print('Finished italian dictionaries')


