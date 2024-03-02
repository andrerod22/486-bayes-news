import operator
import os
import sys
import math
import re
import pdb
import preprocess
from collections import defaultdict
from pathlib import Path

def default_value0():
    return 0

def default_value1():
    return 1

def default_value2():
    return {}

def testNaiveBayes(doc, input_path, class_prob, word_prob):
    """Test Function for Naive Bayes."""
    categories = defaultdict(default_value0)
    for c in class_prob.keys(): categories[c]
    text = [t.rstrip('\n') for t in open(doc)]
    for t in text:
        t.strip()
        temp_text = preprocess.tokenizeText(t) if text != '' else ''
        for temp in temp_text:
            for te in word_prob.keys():
                if temp in word_prob[te].keys():
                    categories[te] += word_prob[te][temp]
    
    for te in categories.keys():
        categories[te] = categories[te] * categories[te]
    return max(categories.items(), key=operator.itemgetter(1))[0].split('.')[0]

def trainNaiveBayes(news, input_path):
    """Training Function for Test Files."""
    classprobs = defaultdict(default_value1)
    wordprobs = defaultdict(default_value1)

    # Building the classprobs dictionary
    for doc in news:
        doc = str(doc).split('/')
        doc = re.sub(r'.txt', '', doc[1])
        doc = re.sub(r'[0-9]', '', doc[1])
        classprobs[doc] += 1
    

    for c in classprobs.keys():
        classprobs[c] = float(classprobs[c])/len(news)
    
    # Building the wordprobs dictionary (Determining Vocab)
    words = defaultdict(default_value2)
    vocabulary = []
    for doc in news:
        text = [t.rstrip('\n') for t in open(doc)]
        doc = str(doc).split('/')
        altered_doc = re.sub(r'.txt', '', doc[1])
        altered_doc = re.sub(r'[0-9]', '', doc[1])
        #if altered_doc not in words.keys():
        words[altered_doc]
        for txt in text:
            txt.strip()
            temp_text = preprocess.tokenizeText(txt) if text != '' else ''
            for t in temp_text:
                words[altered_doc] = defaultdict(default_value1)
                words[altered_doc][t] += 1
                if t not in vocabulary:
                    vocabulary += t
    
    # Iterate through the new built up words dictionary:
    for w in words.keys():
        wordprobs[w] = defaultdict(default_value2)
        for v in vocabulary:
            # breakpoint()
            if v in words[w].keys():
                wordprobs[w][v] = math.log10(float(words[w][v] + 1)/float(sum(words[w].values()) + len(vocabulary)))
            else:
                wordprobs[w][v] = math.log10(float(1)/float(sum(words[w].values()) + len(vocabulary)))
    
    return classprobs, wordprobs

def invoke_naive_bayes():
    # Extract all news from 
    correct_predictions = 0
    results = []
    input_path = Path(sys.argv[1])
    news = [doc for doc in input_path.iterdir() if doc.is_file()]

    for doc in news:
        class_prob, word_prob = trainNaiveBayes(news, input_path)
        proposed_prediction = testNaiveBayes(doc, input_path, class_prob, word_prob)
        doc = str(doc).split('/')
        results.append(doc[1] + ' ' + proposed_prediction + '\n')
        # breakpoint()
        doc = re.sub(r'.txt', '', doc[1])
        doc = re.sub(r'[0-9]', '', doc[1])
        correct_predictions = correct_predictions + 1 if proposed_prediction == doc else correct_predictions
    
    # breakpoint()
    with open("naivebayes.output." + str(input_path), "w+") as w:
        for prediction in results:
            w.write(str(prediction))
    breakpoint()
    accuracy_results = float(correct_predictions)/float(len(news))
    print(accuracy_results)


if __name__ == '__main__':
    invoke_naive_bayes()
