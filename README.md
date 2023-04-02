# NLP_Portfolio

## [Overview of NLP](https://github.com/ashwin-som/NLP_Portfolio/blob/main/Overview_of_NLP.pdf)
This document provides a high level overview of NLP, it's use cases and my reason for interest in it. It also goes on to describe the three approaches to NLP ranging from the 1960s to 2010s.


## [Porfolio Assignment 1](https://github.com/ashwin-som/NLP_Portfolio/blob/main/portfolio1/axs180183_portfolio1.py)
- This program takes in an input csv file of the details of people, processes the details, and re-organizes it in the form of objects to be respresented clearly. 
- To run this program, execute <code>python axs180183_portfolio1.py data/data.csv</code> in terminal for a Unix/Linux based system.
- To run this program, execute <code>python axs180183_portfolio1.py data/data.csv</code> in powershell for a Windows based system.
- Please ensure that you have the proper libraries downloaded such as re, sys, pickle. Also ensure that python works on your operating system. (data/ folder should be on the same level as the program file)
- Python is generally a strong choice for text processing as it has many inbuilt methods for processing. libraries such as 're' are useful as well. One downside would be that it might be a little slower than other compiled languages for runtime but this is usually overcome by maintaining good coding style.
- In this assignment, I was able to review and learn many concepts such as file IO, regex in python as well as certain inbuilt functions in python. Especially through regex, i learned some new ways of making more code more efficient for matching strings given in input to what I would require. 

## [Porfolio Assignment 2](https://github.com/ashwin-som/NLP_Portfolio/blob/main/portfolio2/axs180183_portfolio2.py)
- This program takes in an input txt file of a chapter in anatomy and performs some basic text processing operations on it. The latter half of the program also inlcudes a word guessing game built off of the most frequent nouns appearing from the text processed.
- To run this program, execute <code>python axs180183_portfolio2.py anat19.txt</code> in terminal for a Unix/Linux based system.
- To run this program, execute <code>python axs180183_portfolio1.py anat19.txt</code> in powershell for a Windows based system.
- Please ensure that you have the proper libraries downloaded:these are included at the top of the axs180183_portfolio2.py. Also ensure that python works on your operating system. (data/ folder should be on the same level as the program file)

## [Porfolio Assignment 3](https://github.com/ashwin-som/NLP_Portfolio/blob/main/WordNetAssignment.pdf)
- This python notebook explores all that WordNet and SentiWordNet have to offer, along with explorign some word similarity algorithms such as Wu-Palmer and Lesk.

## [Porfolio Assignment 4](https://github.com/ashwin-som/NLP_Portfolio/tree/main/portfolio3)
- This python program utilizes ngrams on 3 trxt files to create 3 language models. Using these language models, the program then attempts to classify sentences in a test file to a particular language based on laplacian smoothing probabilities of the bigrams and unigrams.
- To run part1.py, execute <code>python part1.py data/LangId.train.English data/LangId.train.French data/LangId.train.Italian</code> in terminal for a Unix/Linux based system.
- To run part1.py, execute <code>python part1.py data/LangId.train.English data/LangId.train.French data/LangId.train.Italian</code> in powershell for a Windows based system.
- To run part2.py, execute <code>python part2.py data/LangId.test</code> in terminal for a Unix/Linux based system.
- To run part2.py, execute <code>python part2.py data/LangId.test</code> in powershell for a Windows based system.
- Please ensure that you have the proper libraries downloaded:these are included at the top of the part1.py and part2.py. Also ensure that python works on your operating system. (data/ folder should be on the same level as the program file)

## [Porfolio Assignment 5, Sentence Parsing](https://github.com/ashwin-som/NLP_Portfolio/blob/main/sentence_parsing.pdf)
- This pdf document explores three different methods for sentence parsing, PSG parsing, dependency parsing, and SRL parsing.

## [Porfolio Assignment 6, Web Crawling](https://github.com/ashwin-som/NLP_Portfolio/blob/main/web_crawling/wc.py)
- This program performs web crawling to obtain 15 urls, for which it scrapes data and then does some text processing. In particular, the program creates a knowledge base from 10 most frequent words occuring in the text data, this can be utilized as the first step to building a chatbot.
- To run this program, execute <code>python wc.py</code> in terminal for a Unix/Linux based system.
- To run this program, execute <code>python wc.py</code> in powershell for a Windows based system.
- Please ensure that you have the proper libraries downloaded:these are included at the top of the wc.py. Also ensure that python works on your operating system. 


## [Porfolio Assignment 7, Text Classification with machine learning](https://github.com/ashwin-som/NLP_Portfolio/blob/main/text_classification.pdf
)
- This python notebook explores Text Classification utilizgin three learning models: Naive Bayes, Logistics Regression, and MLP Neural Networks. IT consists of a comprehensive report on the performance analysis of each model and the tradeoffs.



