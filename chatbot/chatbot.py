import spacy
import nltk
import pickle
from nltk import word_tokenize,pos_tag
#nltk.download('vader_lexicon')
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
import os
import openai
openai.organization = "org-uvHQNvTvEsAhMnH7UybEdwB8"
openai.api_key = "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"

class User: #This is the user model class
    name = ''
    likes = []
    dislikes = []
    conversation_log = []
    
    #constructor for the user model class
    def __init__(self):
        self.name = ''
        self.likes = set()
        self.dislikes = set()
        self.conversation_log = []
    
    #method to add a like
    def add_like(self, like):
        self.likes.add(like)
        
    #method to add a dislike
    def add_dislike(self, dislike):
        self.dislikes.add(dislike)
    
    #method to remove a like
    def rm_like(self, like):
        self.likes.remove(like)
    
    #method to remove a dislike
    def rm_dislike(self, dislike):
        self.dislikes.remove(dislike)
        
    #method to add a convo
    def add_convo(self, convo):
        self.conversation_log.append(convo)
        
    #method to get the likes
    def get_likes(self):
        return self.likes
        
    #method to get the dislikes
    def get_dislikes(self):
        return self.dislikes
        
    #method to get the convo log
    def get_convo_log(self):
        return self.conversation_log
        
        
        
        
def chatbot():
    #we first open both the pickle files to get the kb and user data
    kb = pickle.load(open('kb.p','rb'))
    try:
        users = pickle.load(open('users.p','rb'))
    except EOFError:
        users = []
        
    #importing the spacy nlp library
    nlp = spacy.load("en_core_web_md")
    print('Starbot: Hello! Welcome!')
    user_name = None
    user_input = None
    
    #Performing NER to find the name of the user, will stay on this loop until found
    while user_name==None:
        user_input = input('Starbot: Before we begin, could you please tell me your name? \nYou: ')
        doc = nlp(user_input)
        for e in doc.ents:
            if e.label_=='PERSON':
                user_name = e.text
    
    #Getting all the users information
    u = User()
    for user in users:
        if user_name==user['name']:
            print(f'Starbot: Welcome back {user_name}!')
            u.name = user_name
            u.likes = user['likes']
            u.dislikes = user['dislikes']
            u.conversation_log = user['conversation_log']
            users.remove(user)
    
    if u.name == '':
        print('Starbot: Pleased to meet you',user_name,'!!')
        u.name = user_name
        
    #setting the role of the system in open ai's api
    messages = [{"role": "system", "content" : "Your name is Starbot. You are an assistant who can help answer questions only about Star Wars and talk about the users likes and dislikes only about Star Wars. Keep track of the user's likes and dislikes as well. All your answers should be in a single sentence. If the user asks how to quit, tell them to type in QUIT."}]
    likes = 'The user\'s likes are as follows: ' + ','.join(u.likes)
    dislikes = 'The user\'s dislikes are as follows: ' + ','.join(u.dislikes)
    messages.append({"role": "system", "content": likes})
    messages.append({"role": "system", "content": dislikes})
    
    #this marks the start of the while loop and the chatbot
    while(True):
        user_input = input('You: ')
        #breaks to quit
        if user_input =='QUIT':
            break
        
        log_output = 'User Input: '+user_input+' Starbot Output: '
        messages.append({"role": "user", "content": user_input})
        
        #Analyzing the sentiment of user input
        sia = SentimentIntensityAnalyzer()
        stop_words = set(stopwords.words('english'))
        scores = sia.polarity_scores(user_input.lower())
        #print(scores)
        
        #Based on scores, likes and dislikes will be created, using POS tagging
        if scores['pos']>0.5:
            tokenized_inp = nltk.word_tokenize(user_input)
            filtered_inp = [w for w in tokenized_inp if not w.lower() in stop_words]
            tagged_inp = nltk.pos_tag(filtered_inp)
            for i in tagged_inp:
                if i[1]=='NNP' or i[1]=='NN':
                    if i[0][0].isupper():
                        u.add_like(i[0])
                    if i[0] in u.dislikes:
                        u.rm_dislike(i[0])
        elif scores['neg']>0.5:
            tokenized_inp = nltk.word_tokenize(user_input)
            filtered_inp = [w for w in tokenized_inp if not w.lower() in stop_words]
            tagged_inp = nltk.pos_tag(filtered_inp)
            for i in tagged_inp:
                if i[1]=='NNP' or i[1]=='NN':
                    if i[0] in u.likes:
                        u.rm_like(i[0])
                    if i[0][0].isupper():
                        u.add_dislike(i[0])
                        
            
        #The request to ChatGPT is made
        request = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages)
        chat_response = request.choices[0].message.content
        
        #the response is tokenized using POS tagging to find key words
        tokenized_sent = nltk.word_tokenize(chat_response)
        filtered_sentence = [w for w in tokenized_sent if not w.lower() in stop_words]
        tagged_sent = nltk.pos_tag(filtered_sentence)
        
        #This step finds the most similar sentence in the database using spacy's cosine similarity function, kb and the response.
        most_similar = None
        similarity_rate = 0.0
        for i in tagged_sent:
            if i[1]=='NN':
                if i[0] in kb:
                    for sentence in kb[i[0]]:
                        s1 = nlp(sentence)
                        s2 = nlp(chat_response)
                        temp_sim = s1.similarity(s2)
                        if temp_sim>similarity_rate:
                            similarity_rate = temp_sim
                            most_similar = sentence
        
        
        #Either response is printed depending on the similarity rate. This is to maintain consistency with the user.
        if similarity_rate>0.8:
            print(f'Starbot: {most_similar}')
            log_output+=most_similar
        else:
            print(f'Starbot: {chat_response}')
            log_output+=chat_response
        u.conversation_log.append(log_output)
    
    
    #The latest version of the user information is printed to the log as well as saved back to the pickle file.
    u_dict = u.__dict__
    users.append(u.__dict__)
    pickle.dump(users, open('users.p','wb'))
    print('Name of most recent user:',u_dict['name'])
    print('likes of most recent user:',u_dict['likes'])
    print('dislikes of most recent user:',u_dict['dislikes'])
    print('This user\'s convo log has also been saved. In order to view it, uncomment the line that prints out the convo log')
    #print('User Convo Log:',u_dict['conversation_log'])
    
            
if __name__ == '__main__':
    #Main function to run the chatbot code
    chatbot()
    exit()
    


