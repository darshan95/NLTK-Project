import sys 
import re
from nltk.corpus import wordnet as wn 
def lemmalist(str): 
	syn_set = [] 
	for synset in wn.synsets(str): 
		for item in synset.lemma_names: 
			syn_set.append(item) 
	return syn_set

def check_commentary(nouns,verbs,question,match_info):
    if match_info == "1":
        f = open("match1_innings1",'r')
        fn = open("match1_innings2",'r')
    elif match_info == "2":
        f = open("match2_innings1",'r')
        fn = open("match2_innings2",'r')
    elif match_info == "3":
        f = open("match3_innings1",'r')
        fn = open("match3_innings2",'r')
    elif match_info == "4":
        f = open("match4_innings1",'r')
        fn = open("match4_innings2",'r')
    elif match_info == "5":
        f = open("match5_innings1",'r')
        fn = open("match5_innings2",'r')
    desc1 = f.readlines()
    desc2 = fn.readlines()
    desc = desc1 + desc2
    for line in desc:
        flag=0;flag1=0
        for word in nouns:
            if re.search(word,line,re.IGNORECASE):
                flag=1
            else:
                flag = 0
                break
        if flag==1:
            for word in verbs:
                syn = lemmalist(word)
                for i in syn:
                    if i in line:
                        flag1 = 1
                        break
                if flag1 == 0:
                    break


def main():
    ind = "./player_profile/indian_players_profile.txt"
    nz = "./player_profile/nz_players_profile.txt"
    add_to_dict_profile(profile,ind);
    add_to_dict_profile(profile,nz);
    question = raw_input('Enter a question: ')
    #print question
    text = nltk.word_tokenize(question)
    pos = nltk.pos_tag(text)
    nouns=[]
    verbs=[]
    match_info = ''
    question_info = ''
    for i in range(0,len(pos)):
        if pos[i][0] != "started" and pos[i][0] != "over" and pos[i][0] != "most":
            if "NN" in pos[i][1]:
                if re.match("match",pos[i][0],re.IGNORECASE):
                    if pos[i+1][1] == "CD":
                        match_info = pos[i+1][0]
                    elif pos[i-1][0] == "first":
                        match_info = '1'
                    elif pos[i-1][0] == "second":
                        match_info = '2'
                    elif pos[i-1][0] == "third":
                        match_info = '3'
                    elif pos[i-1][0] == "fourth":
                        match_info = '4' 
                    elif pos[i-1][0] == "fifth":
                        match_info = '5'
	        else:
           	    nouns.insert(len(nouns),pos[i][0])
            if "VB" in pos[i][1]:
	        if pos[i][0] != "was" or pos[i][0] != "is" or pos[i][0] != "were":
            	    verbs.insert(len(verbs),pos[i][0])
	    if pos[i][0][0] == "W":
	        question_info = pos[i][0]
    check_commentary(nouns,verbs,question,match_info)


