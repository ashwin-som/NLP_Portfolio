import nltk
from nltk import word_tokenize
import sys
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import random
from heapq import heapify, heappush, heappop


def process_txt(filename):
    #this takes care of opening the .txt file and extracting the input as raw text
    file = open(filename)
    text_data = file.read().replace('\n',' ')
    #text_data = text_data.lower() # makes the raw text lowercase

    #This calculates the lexical diversity (# of unique words in the text w.r.t total words)
    tokens = word_tokenize(text_data)
    set_tokens = set(tokens)
    print(f'Lexical Diversity: {len(set_tokens)/len(tokens)}')

    #this part takes care of tokenizing the text and pre processing it to include: only alpha, >5 length, no stopwords
    tokens_lower = [token.lower() for token in tokens]
    tokens = [token for token in tokens_lower if token.isalpha() and token not in stopwords.words('english') and len(token)>5]

    #this part takes care of producing unique lemmas (root words) from the tokens
    lemmatizer = WordNetLemmatizer()
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    unique_lemmas = set(lemmas)
    
    #This part create the pos-tagging for unique lemmas
    tags = nltk.pos_tag(unique_lemmas)
    #print(tags[:20])

    #This part extracts all the nouns from the pos tags
    nouns = []
    for tag in tags:
        if tag[1][0] == 'N':
            nouns.append(tag[0])

    return tokens,nouns

def print_word(word): #This function takes care of printing a word as per the assignment instructions
    output = ''
    for i in word:
        output+=i+' '
    print(output)

def play_game(words):
    #choosing a random word
    word = words[random.randint(0,len(words)-1)]
    guess = ['_' for i in word]
    score = 5
    guess_input = None

    #The game is continuously played until either of thes conditions are met. 
    while score>=0 and guess_input!='!':
        print_word(guess)
        guess_input = input('Guess a letter:')
        if guess_input=='!':  #If '!' is inputted, the game ends.
            break
        if guess_input not in word: #If the guess is not right, the user tries again until score is negative
            score-=1
            print(f'Sorry, guess again. Score is {score}')
            continue

        score+=1
        print(f'Right! Score is {score}')
        for i in range(len(word)):
            if word[i]==guess_input:
                guess[i] = guess_input  #if the guess is right, the guessed letter is filled in the word
        if '_' not in guess: #If there are no more underscores in the word, then the word has been correctly guessed, we can move on to the next word.
            print_word(word)
            print('You solved it!')
            print(f'Current Score: {score}')
            print('Guess another word')   
            #At this point, we have reset the game with a new word for the player to guess and will repeat the entire process again
            word = words[random.randint(0,len(words)-1)]
            guess = ['_' for i in word]
            guess_input = None
    if score<0:
        print('You have exhausted all your points!')
    else:
        print('You have quit the game')
    print('The game is complete')



if __name__ == "__main__":
    path = ''
    #this checks for the file path as a sys arg
    if len(sys.argv) <2:
        print('Please provide the path to the data file as a system arg')
    else:
        path = sys.argv[1]
        tokens , nouns = process_txt(path)
        print('Number of tokens: ',len(tokens))
        print('Numbers of nouns: ',len(nouns))

        #Creating a map of nouns from the tokens and their # of occurences
        map = {}
        for noun in nouns:
            count = 0
            for token in tokens:
                if token==noun:
                    count+=1
            map[noun] = count*-1  #Multiplying the # here by -1 to ensure that the min heap processes the most frequent words first

        list_from_map = list(map.items())
        heap = [(i[1],i[0]) for i in list_from_map]
        heapify(heap) #This is the creation of a min heap wrt the count of the nouns from the line above
        word_list = []
        sorted_map = {} #this contains the nouns sorted by their count
        for i in range(len(map)):
            (val,key) = heappop(heap)
            if i<50:
                word_list.append(key) #appending the 50 most frequent nouns to a list for the guessing game
            sorted_map[key] = val*-1 #For each pop, we plug in the corresponding pair into the 
        
        for w in word_list:
            print(w,sorted_map[w]) #we print the top 50 frequent nouns here

        #now we are ready to play the guessing game
        print('Let\'s play a word guessing game!')
        play_game(word_list)