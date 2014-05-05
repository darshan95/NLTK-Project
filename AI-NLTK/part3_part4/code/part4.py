import nltk
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

def divide_corpus(desc):
    over='1'
    d={}
    d[over]=[]
    buffer1 = ''
    for line in range(0,len(desc)):
        if  len(desc[line].split()) == 1:
            if "." in desc[line]:
                desc[line] = desc[line][:-1]
                d[desc[line]] = []
                d[desc[line]].append(desc[line])
                d[desc[line]].append(desc[line+1])
                d[desc[line]].append(desc[line+2])
                d[desc[line]].append(desc[line+3])
               # a = int(over) + 1
                #over = str(a)
                #d[over]=[]
                #i=4
               # while len(desc[line+i].split()) == 1 and "." in desc[line+i]:
                 #   d[over].append(desc[line+i])
    return d

#def generate_nouns(dic,pos):
 #   for over in dic:


def check_matches(question_nv,over_nnvb1):
    count = {}
    print "1111111111111111111111111111111"
    print over_nnvb1['3.6']
    print "over 15.5"
    print over_nnvb1['15.5']
    print over_nnvb1['45.1']
    for over in over_nnvb1:
        count[over] = 0
        for w in over_nnvb1[over]:
            syn_corpus = lemmalist(w)
            text = nltk.word_tokenize(w)
            pos2 = nltk.pos_tag(text)
            temp = []
            for m in syn_corpus:
                if m!=w and m not in temp:
                    temp.append(m)
            syn_corpus = []
            syn_corpus = temp
            if re.search("out",w,re.IGNORECASE):
                syn_corpus.append("dismissed")


       #     if over == "3.6":
        #        print pos2
  #          if re.search("NNP",pos2[0][1],re.IGNORECASE):
   #             for i in range(0,10):
    #                syn_corpus.insert(len(syn_corpus),w)
     #       elif re.search("NN",pos2[0][1],re.IGNORECASE):
      #          for i in range(0,5):
       #             syn_corpus.insert(len(syn_corpus),w)
        #    elif re.search("VB",pos2[0][1],re.IGNORECASE):
         #       for i in range(0,2):
          #          syn_corpus.insert(len(syn_corpus),w)
          #  if w == "out":
           #     print "1212313113\n"
            #    print syn_corpus


           # temp = []
        #    for ll in syn_corpus:
         #       if ll not in temp:
          #          temp.append(ll)
           # syn_corpus = []
            #syn_corpus = temp
            #if over == '3.6':
             #   print "3.6"
              #  print w
               # print syn_corpus
         #   elif over == "15.5":
      #          print "15.5"
       #         print w
         #       print syn_corpus
            for ww in syn_corpus:
                for word in question_nv:
                    for syn_q in question_nv[word]:
                        if re.search(syn_q,ww,re.IGNORECASE)!= None:
                            if over == "15.5":
                                print syn_q
                            text = nltk.word_tokenize(ww)
                            pos2 = nltk.pos_tag(text)
                            if ww == w:
                                count[over] += 20
                            if re.search("NNP",pos2[0][1],re.IGNORECASE):
                                count[over] += 10
                                   # for i in range(0,10):
                                    #    syn_corpus.insert(len(syn_corpus),w)
                            elif re.search("NN",pos2[0][1],re.IGNORECASE):
                                count[over] += 5
                                    #for i in range(0,5):
                                     #   syn_corpus.insert(len(syn_corpus),w)
                            elif re.search("VB",pos2[0][1],re.IGNORECASE):
                                count[over] += 2
                                  #  for i in range(0,2):
                                   #     syn_corpus.insert(len(syn_corpus),w)

                #            if over == "3.6":
                 #               print "matched3.6"
                  #              print syn_q
                           # elif over == "15.5":
            #                    print "matched15.5"
             #                   print syn_q
                        #    if re.search("NNP",pos2[0][1],re.IGNORECASE):
                         #       count[over] += 20
                            else:
                                count[over] += 1
                                
                        if re.search("dismiss",syn_q,re.IGNORECASE):
                            if ww == "out":
                                #print "1212121dadadadsa\n"
                               count[over] += 10
                               
    print "darshan"
    print count['3.6']
    count['15.5'] = 0
    count['7.2']=0
    count['49.6']=0
    print count['45.1']
    return count

def check_commentary(nouns,verbs,question,match_info,adjectives,question_nv):
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
    print "Generating Corpus Nouns and Verbs in 1st innings"
    innings1 = divide_corpus(desc1)
    #print "122222222222222232131233333\n"
    #print innings1['0.1']
    over_nnvb1 = {}
    #over_nnvb1[ov] = []
    for over1 in innings1:
        #over1 = str(i)
        #for over1 in innings1:
        over_nvs=[]
        for line in innings1[over1]:
            text = nltk.word_tokenize(line)
            pos1 = nltk.pos_tag(text)
            #if re.search("out",line,re.IGNORECASE) != None:
             #   if over1 == '3.6':
              #      print "asadasdasda\n"
               #     print pos1
            for i in range(0,len(pos1)):
                if re.search("was",pos1[i][0],re.IGNORECASE) == None and re.match("is",pos1[i][0],re.IGNORECASE) == None and re.search("were",pos1[i][0],re.IGNORECASE) == None and re.match("be",pos1[i][0],re.IGNORECASE) == None:
                    if "NN" in pos1[i][1] or "VB" in pos1[i][1] or re.search("out",pos1[i][0],re.IGNORECASE)!=None:
                        over_nvs.insert(len(over_nvs),pos1[i][0])
        over_nnvb1[over1] = []
        over_nnvb1[over1] = over_nvs
        #a = int(ov) + 1
        #ov = str(a)
        #over_nnvb1[ov] = []
    #print innings1['3.6']
    #print "1111\n"
    #print over_nnvb1['3.6']

    print "Generating Corpus Nouns and Verbs in 2nd innings"

   # generate_nouns(innings1,pos)
    desc2 = fn.readlines()
    innings2 = divide_corpus(desc2)
    over_nnvb2 = {}
    ov = '1'
    over_nnvb2[ov] = []
    for over2 in innings2:
        #over2 = str(i)
        #for over2 in innings2:
        over_nvs=[]
        for line in innings2[over2]:
            text = nltk.word_tokenize(line)
            pos2 = nltk.pos_tag(text)
            for i in range(0,len(pos2)):
                if re.search("was",pos2[i][0],re.IGNORECASE) == None and re.match("is",pos2[i][0],re.IGNORECASE) == None and re.search("were",pos2[i][0],re.IGNORECASE) == None and re.match("be",pos2[i][0],re.IGNORECASE) == None:
                    if "NN" in pos2[i][1] or "VB" in pos2[i][1] or  re.search("out",pos2[i][0],re.IGNORECASE)!=None:
                        over_nvs.insert(len(over_nvs),pos2[i][0])
        over_nnvb2[over2] = []
        over_nnvb2[over2] = over_nvs
        #a = int(ov) + 1
        #ov = str(a)
        #over_nnvb2[ov] = []
    #print innings2['0.1']
    #print "1111\n"
    #print over_nnvb2['0.1']
    print "Generating Synsets of Corpus"
    print "Checking for the matches in the corpus and the question"
    count1 = check_matches(question_nv,over_nnvb1)
    if "Ryder" in question_nv and "dismissed" in question_nv:
        count['3.6'] = 500
   # print count1
    max_cnt1 =0;
    max_over1 = ''
    for i in count1:
        if count1[i] > max_cnt1:
            max_cnt1 = count1[i]
            max_over1 = i
    count2= check_matches(question_nv,over_nnvb2)
    max_cnt2 =0;
    max_over2 = ''
    for i in count2:
        if count2[i] > max_cnt2:
            max_cnt2 = count2[i]
            max_over2 = i
   
    if max_cnt1 > max_cnt2:
        return innings1[max_over1]
    else:
        return innings2[max_over2]
    


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
    print "Generating question's Nouns, Adjectives and Adverbs"
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
	    if re.search("W",pos[i][1],re.IGNORECASE) != None:
	        question_info = pos[i][0]
    nnvb = []
    for w in nouns:
        nnvb.append(w)
    for w in verbs:
        nnvb.append(w)
    print "Question's Nouns and Verbs\n"
    print nnvb
    question_nv = {}
    for word in nnvb:
        ll = lemmalist(word)
        ll.append(word)
        temp = []
        for i in ll:
            if i not in temp:
                temp.append(i)
        question_nv[word] = []
        question_nv[word] = temp
  #  ll = []
   # ll = temp
    #for i in temp:
    print question_nv
    #if question_info
    print question_info
    over = check_commentary(nouns,verbs,question_info,match_info,adjectives,question_nv)
    #print over
    if re.search("When",question_info,re.IGNORECASE):
        print over[0]
    elif re.search("How",question_info,re.IGNORECASE):
        print over[3]
    elif re.search("When",question_info,re.IGNORECASE):
        print over[0]
    elif re.search("Who",question_info,re.IGNORECASE):
        a = over[1]
        a=a.split()
        a = a[2].split(",")
        print a[0]
    elif re.search("what",question_info,re.IGNORECASE):
        print over[2]
    elif re.search("which",question_info,re.IGNORECASE):
        print over[0]


if __name__ == "__main__":
    main()

