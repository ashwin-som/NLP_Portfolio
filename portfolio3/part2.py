from nltk import word_tokenize
from nltk.util import ngrams
import pickle
import sys

def compute(sent,ug_map,bg_map,v): #This function computes the probability of a sentence being a particular language
    sent_bigrams = list(ngrams(word_tokenize(sent),2))
    probability = 1.0

    for bigram in sent_bigrams:
        if bigram in bg_map:
            b = bg_map[bigram]
        else:
            b = 0
        if bigram[0] in ug_map:
            u = ug_map[bigram[0]]
        else:
            u = 0
        probability*=(b+1)/(u+v)   #probability calculation usign laplace smoothing

    return probability

if __name__ == "__main__":
    path = ''
    if len(sys.argv) <2:
        print('Please provide the path to the data file as a system arg')
    else:
        e_uni_map = pickle.load(open('e_uni_map.p', 'rb'))
        e_bi_map = pickle.load(open('e_bi_map.p', 'rb'))
        f_uni_map = pickle.load(open('f_uni_map.p', 'rb'))         #We are loading all of the dictionaries saved from the previous program
        f_bi_map = pickle.load(open('f_bi_map.p', 'rb'))
        i_uni_map = pickle.load(open('i_uni_map.p', 'rb'))
        i_bi_map = pickle.load(open('i_bi_map.p', 'rb'))
        v = len(e_uni_map)+len(f_uni_map)+len(i_uni_map)
        path = sys.argv[1]
        file = open(path)
        file = file.read().split('\n')
        output = []
        for sentence in file:           #for reach sentence, we are computing 3 probabilities and assigning the higest as the language
            prob_english = compute(sentence,e_uni_map,e_bi_map,v)
            prob_french = compute(sentence,f_uni_map,f_bi_map,v)
            prob_italian = compute(sentence,i_uni_map,i_bi_map,v)
            if prob_english>=prob_french and prob_english>=prob_italian:
                output.append('English')
            elif prob_french>=prob_english and prob_french>=prob_italian:
                output.append('French')
            else:
                output.append('Italian')
        with open('predicted.txt', 'w') as f:   #we are writing the output to a file
            for i in range(len(output)):
                f.write(str(i+1))
                f.write(' ')    
                f.write(output[i])
                f.write('\n')

        sol_file = open('data/LangId.sol')  #opening the solution file
        sol_file = sol_file.read().split('\n')
        L = len(sol_file)
        count = 0
        actual_count = 0
        for i in range(L):
            actual_count+=1
            if output[i] in sol_file[i]:   #calculating the number of correctly classified to compute accuracy
                count+=1
            else:
                print(actual_count)
            
        print(count/L)






