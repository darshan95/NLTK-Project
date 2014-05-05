import sys 
import re
import nltk
from nltk.corpus import wordnet as wn 
def lemmalist(str): 
	syn_set = [] 
	for synset in wn.synsets(str): 
		for item in synset.lemma_names: 
			syn_set.append(item) 
	return syn_set

def add_to_dict_profile(dictionary, fname):
    c='\t'
    f = open(fname, 'r')
    for line in f:
        temp = line[:-1]
        temp = temp.split(c)
        a = temp[0]
        b = temp[1:]
        if a not in dictionary:
            dictionary[a] = b



def check_commentary(nouns,verbs,question,match_info,adjectives):
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
    ans=[]
    noun_match=[]
    verb_match=[]
    adj_match=[]
    ans_lines=[]
    flag=0;flag1=0
    for line in range(0,len(desc)):
        for word in nouns:
            if re.search(word,desc[line],re.IGNORECASE)!=None:
                noun_match.insert(len(noun_match),desc[line]);
                flag=1
            else:
                flag = 0
                break
     #   if flag==1:
          #  print desc[line]
        for word in verbs:
        #        syn = lemmalist(word)
         #       if word == "dismissed" or word=="dismiss":
          #          syn.insert(len(syn),"out");
                #print syn
           #     for i in syn:
            if word == "dismissed" or word =="dismiss" or re.match("out",word,re.IGNORECASE):
                if len(desc[line-1].split()) < 2:
                    if re.match("out,",desc[line-1],re.IGNORECASE)!=None:
                        if flag==1:
                            print "333333333333\n"
                            print desc[line-1]
                            print desc[line]
                            flag = 3
                            ans.insert(len(ans),desc[line]);
                            print ans
                            ans_lines.insert(len(ans_lines),line);
                            break
                #if flag1 != 1:
                  #  if len(desc[line-1].split()) < 2:
                      #  print "2222222\n"
                       # print desc[line-1]
            else:
                if re.search(word,desc[line],re.IGNORECASE)!=None:
                    print "11111111111\n"
                    print desc[line]
                   # flag = 1
                    print i
                    if flag==1:
                        flag=2
                        ans.insert(len(ans),desc[line]);
                        ans_lines.insert(len(ans_lines),line);
                        break
                    verb_match.insert(len(verb_match),desc[line]);
                #flag1=0
        if flag==3:
            break
        for word in adjectives:
            if re.search(word,desc[line],re.IGNORECASE)!=None:
                if flag==1 and flag!=3:
                    a=1
                  #  print desc[line]
                #    ans.insert(len(ans),desc[line]);
                 #   ans_lines.insert(len(ans_lines),line);
                adj_match.insert(len(adj_match),desc[line]);
        if flag==3:
            break
    if flag==3:
        print "122222223455"
        print ans[0]
        return
    for line in noun_match:
        if line in verb_match:
            if line in adj_match:
                #print line
                break
            else:
                ans.insert(len(ans),line)
        else:
            ans.insert(len(ans),line)
    if len(ans) == 1:
        line_max = desc.index(ans)
        print ans
    final=[]
    if len(ans) >= 0:
        for i in nouns:
            final.insert(len(final),i)
        for i in verbs:
            final.insert(len(final),i)
        for i in adjectives:
            final.insert(len(final),i)
     #   print "final"
      #  print final
        max_cnt = 0
        line_max=0;
        for line in range(0,len(desc)):
            count=0
            for word in final:
                if re.search(word,desc[line],re.IGNORECASE)!=None:
                #    print "11111\n"
               #     print word
                    count += 1;
                if max_cnt <= count:
                    line_max = line
                    max_cnt = count
            #if count > 0:
             #   print desc[line]
              #  print count
        print desc[line_max]
    for i in range(3,len(desc)):
        if len(desc[line-i].split()) == 1: 
            if "." in desc[line-i]:
                over = desc[line-i]
                break

    if re.match("when",question,re.IGNORECASE)!=None:
        print over,
        print "are the overs"
    elif re.match("how",question,re.IGNORECASE)!=None:
        print desc[line_max],
        print "is the answer"  
    elif re.match("which",question,re.IGNORECASE)!=None:
        print over,
        print "is the answer"  
       

"""
    if len(ans) == 0:
        print noun_match
        print verb_match
        print adj_match
    else:
        print "ans"
        cnt =1 
        for i in ans:
            print cnt,
            print i
            cnt += 1
"""


def main():
    profile={}
    ind = "./player_profile/indian_players_profile.txt"
    nz = "./player_profile/nz_players_profile.txt"
    add_to_dict_profile(profile,ind);
    add_to_dict_profile(profile,nz);
    question = raw_input('Enter a question: ')
    text = nltk.word_tokenize(question)
    pos = nltk.pos_tag(text)
    nouns=[]
    verbs=[]
    adjectives=[]
    match_info = ''
    question_info = ''
    for i in range(0,len(pos)):
        if re.match("started",pos[i][0],re.IGNORECASE) == None and re.match("over",pos[i][0],re.IGNORECASE) == None and re.match("most",pos[i][0],re.IGNORECASE) == None:
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
	        if re.match("was",pos[i][0],re.IGNORECASE) == None and re.match("is",pos[i][0],re.IGNORECASE) == None and re.match("were",pos[i][0],re.IGNORECASE) == None:
            	    verbs.insert(len(verbs),pos[i][0])
            if "JJ" in pos[i][1]:
                adjectives.insert(len(adjectives),pos[i][0]);
	    if pos[i][0][0] == "W":
	        question_info = pos[i][0]
    print nouns
    print verbs
    print adjectives
    print match_info
    print question_info
    check_commentary(nouns,verbs,question,match_info,adjectives)

if __name__ == "__main__":
    main()
    

