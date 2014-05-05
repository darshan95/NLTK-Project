import re
import nltk
match_info=''
question_info=''
desc=''
profile={}
description = {}
ret_variable=0
def parse_match_info(question,list_words):
    global match_info
    match_info = question
    for i in range(0,len(list_words)):
#        print list_words[i]
        if "match" in list_words[i]:
            if list_words[i-1] == "first" or list_words[i-1] =="second" or list_words[i-1] == "third" or list_words[i-1] ==  "fourth" or list_words[i-1] ==  "fifth":
 #               print "aaaaaa"
                match_info = list_words[i-1]
  #              print match_info
                return i
            elif list_words[i+1] == "first" or list_words[i+1] =="second" or list_words[i+1] == "third" or list_words[i+1] ==  "fourth" or list_words[i+1] ==  "fifth":
                match_info = list_words[i+1]
                return i+1
        if i == len(list_words)-1:
            return -1;

def parse_question_info(remain_info):
    global question_info
    for k in range(len(remain_info)-1,-1,-1):
        if remain_info[k]=="which":
            if remain_info[k+1] == "ball?" or remain_info[k+1] == "over?" or remain_info[k+1] == "bowler?" or remain_info[k+1] == "bowler(s)?" or remain_info[k+1] == "bowlers?" or remain_info[k+1] == "over(s)?" or remain_info[k+1] == "ball(s)?" or remain_info[k+1] == "overs?" or remain_info[k+1] == "balls?":
                question_info = remain_info[k+1].split("?")
                question_info=question_info[0]
                return k;
        if remain_info[k]=="who":
            if remain_info[k+1] == "dismissed?" or remain_info[k+1] == "dismisses?": 
                question_info = remain_info[k+1].split("?")
                question_info=question_info[0]
                return k;
        elif remain_info[k] == "whom?":
            if (remain_info[k-1] == "by" and remain_info[k-2] == "dismissed") or (remain_info[k-1] == "by" and remain_info[k-2] == "hit"):
                if remain_info[k-2] == "dismissed":
                    question_info = "dismiss"
                    return k-2
                if remain_info[k-2] == "hit":
                    question_info = "hit"
                    return k-1
        if k == 0:
            return -1

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



def parse_for_desc(remain_info,profile,pos):
    global description
    first_name=[]
    last_name=[]
    main_extra = []
    index_extra = -1;
    name=''
    for player in profile:
        player_name = player.split(' ')
        last_name.insert(len(last_name),player_name[1])
        first_name.insert(len(first_name),player_name[0])
    for word in remain_info:
        if word in last_name:
            if word == "McCullum":
                indx=remain_info.index(word)
                if remain_info[indx-1] == "NL" or remain_info[indx-1] == "BB":
                    name = remain_info[indx-1] + " " + word
                else:
                    name = "NL" + word
            elif word == "Sharma":
                indx=remain_info.index(word)
                if remain_info[indx-1] == "I" or remain_info[indx-1] == "RG":
                    name = remain_info[indx-1] + " " + word
                else:
                    name = "I" + word
            elif word == "Shami":
                indx=remain_info.index(word)
                if remain_info[indx-1] == "Mohammad":
                    name = remain_info[indx-1] + " " + word
                else:
                    name = word
    
            else:
                name = word
            break
    if question_info == "dismiss":
        description = {}
        description["dismiss"]=[]
        description["dismiss"].insert(len(description["dismiss"]),name)
    #dismiss case
   # for word in remain_info:
   #     iindxx = remain_info.index(word)
    #    if word == dis
    variable_flag=0
    for word in remain_info:
        iindxx = remain_info.index(word)
        if word == "hit" or word == "hits" or word=="hitting":
            indx = remain_info.index(word)
            if pos[indx+1]!="DT":
                flag = indx
            else:
                flag = indx + 1
            if "maximum" in remain_info and name=='' and question_info=="hit":
                variable_flag=1
            elif name=='' and question_info=="hit":
                flag = -1
            if variable_flag==0 and (remain_info[flag+1] == "ones" or remain_info[flag+1] == "twos" or remain_info[flag+1] == "fours" or remain_info[flag+1] == "sixes"):
                final_index = flag+2
                description={}
                description["hit"] = []
                description["hit"].insert(0,name)
                if remain_info[flag+1] == "ones":
                    description["hit"].insert(1,"1 run,")
                elif remain_info[flag+1] == "twos":
                    description["hit"].insert(1,"2 run,")
                elif remain_info[flag+1] == "fours":
                    description["hit"].insert(1,"FOUR,")
                elif remain_info[flag+1] == "sixes":
                    description["hit"].insert(1,"SIX,")
                extra_info = remain_info[final_index:]
                extra_desc = ' '.join(extra_info)
            else:#number case or maximum
                description={}
                description["hit"] = []
                max_flag=1;
                for item in pos:
                    if item[1] == "CD":
                        if remain_info[flag+1] == item[0]:
                            if remain_info[flag+2] == "ones" or remain_info[flag+2] == "twos" or remain_info[flag+2] == "fours" or remain_info[flag+2] == "sixes" or remain_info[flag+2] == "two" or remain_info[flag+2] == "four" or remain_info[flag+2] == "six" or remain_info[flag+2] == "one":
                                final_index=flag+3;
                                description={};
                                description["hit"] = []
                                description["hit"].insert(0,name)
                                description["hit"].insert(1,"number")
                                if remain_info[flag+1]=="one":
                                    remain_info[flag+1] = 1;
                                elif remain_info[flag+1]=="two":
                                    remain_info[flag+1]  = 2;
                                elif remain_info[flag+1] =="three":
                                    remain_info[flag+1]  = 3;
                                elif remain_info[flag+1] =="four":
                                    remain_info[flag+1]  = 4;
                                elif remain_info[flag+1] =="five":
                                    remain_info[flag+1]  = 5;
                                elif remain_info[flag+1] =="six":
                                    remain_info[flag+1]  = 6;
                                elif remain_info[flag+1] =="seven":
                                    remain_info[flag+1]  = 7;
                                elif remain_info[flag+1] =="ten":
                                    remain_info[flag+1]  = 10;
                                elif remain_info[flag+1] =="twenty":
                                    remain_info[flag+1]  =20;
                                elif remain_info[flag+1] =="thirty":
                                    remain_info[flag+1]  = 30;
                                elif remain_info[flag+1] =="forty":
                                    remain_info[flag+1]  = 40;
                                elif remain_info[flag+1] =="fifty":
                                    remain_info[flag+1]  = 50;
                                elif remain_info[flag+1] =="eight":
                                    remain_info[flag+1]  = 8;
                                elif remain_info[flag+1] =="nine":
                                    remain_info[flag+1]  = 9;
                                description["hit"].insert(2,remain_info[flag+1])
                                max_flag=0;
                                if remain_info[flag+2] == "ones" or remain_info[flag+2] =="one":
                                    description["hit"].insert(3,"1 run,")
                                elif remain_info[flag+2] == "twos" or remain_info[flag+2] =="two":
                                    description["hit"].insert(3,"2 run,")
                                elif remain_info[flag+2] == "fours" or remain_info[flag+2] =="four":
                                    description["hit"].insert(3,"FOUR,")
                                elif remain_info[flag+2] == "sixes" or remain_info[flag+2] =="six":
                                    description["hit"].insert(3,"SIX,")
                               # description["hit"].insert(3,remain_info[flag+2])
                                extra_info = remain_info[final_index:]
                                extra_desc = ' '.join(extra_info)
                            elif item[0]=="one" or item[0]=="two" or item[0]=="three" or item[0]=="four" or item[0]=="six":
                                final_index = flag+2
                                description={}
                                description["hit"] = []
                                description["hit"].insert(0,name)
                                max_flag=0;
                                if remain_info[flag+1] == "one":
                                    description["hit"].insert(1,"1 run,")
                                elif remain_info[flag+1] == "two":
                                    description["hit"].insert(1,"2 runs,")
                                elif remain_info[flag+1] == "three":
                                    description["hit"].insert(1,"3 runs,")
                                elif remain_info[flag+1] == "four":
                                    description["hit"].insert(1,"FOUR,")
                                elif remain_info[flag+1] == "six":
                                    description["hit"].insert(1,"SIX,")
                               # description["hit"].insert(1,remain_info[flag+1])
                                extra_info = remain_info[final_index:]
                                extra_desc = ' '.join(extra_info)
                if len(description["hit"]) == 0:
                    description["hit"].insert(0,name)
                    if "maximum" in remain_info:
                        iinx = remain_info.index("maximum")
                   # if remain_info[flag+1] == "maximum":
                        if remain_info[iinx+1] == "ones" or remain_info[iinx+1] == "twos" or remain_info[iinx+1] == "fours" or remain_info[iinx+1] == "sixes" or remain_info[iinx+1] == "two" or remain_info[iinx+1] == "four" or remain_info[iinx+1] == "six" or remain_info[iinx+1] == "one":
                            final_index = flag+3
                            description["hit"].insert(1,"max")
                           # description["hit"].insert(2,remain_info[flag+1])
                            if remain_info[iinx+1] == "ones" or remain_info[iinx+1] =="one":
                                description["hit"].insert(2,"1 run,")
                            elif remain_info[iinx+1] == "twos" or remain_info[iinx+1] =="two":
                                description["hit"].insert(2,"2 runs,")
                            elif remain_info[iinx+1] == "fours" or remain_info[iinx+1] =="four":
                                description["hit"].insert(2,"FOUR,")
                            elif remain_info[iinx+1] == "sixes" or remain_info[iinx+1] =="six":
                                description["hit"].insert(2,"SIX,")
                            extra_info = remain_info[final_index:]
                            extra_desc = ' '.join(extra_info)
            try:
                extra_desc
            except NameError:
                print "write number as digits\n"
                global ret_variable
                ret_variable=1
                return
            if len(extra_desc) > 0:
                text = nltk.word_tokenize(extra_desc)
                extra_pos = nltk.pos_tag(text)
                for i in range(0,len(extra_pos)):
                      #  if item[0] == "IN":
                       #     over_indx=extra_info.index("over")
                    if extra_pos[i][0] == "over":
                        if extra_pos[i+1][1] == "CD":
                            index_extra = i;
                            description["hit"].insert(len(description["hit"]),"xx")
                            description["hit"].insert(len(description["hit"]),extra_pos[i+1][0])
                for k in range(0,len(extra_pos)):
                    if extra_pos[k][1] == "NNS" or extra_pos[k][1] == "NN":
                        if k!=index_extra:
                            description["hit"].insert(len(description["hit"]),extra_pos[k][0])
        elif word == "out":
            description={}
            description["out"]=[]
            description["out"].insert(len(description["out"]),name)
            ll = remain_info.index(word)
            extra_info=[]
            extra_info = remain_info[ll+1:]
            extra_desc = ' '.join(extra_info)
            if len(extra_desc) > 0:
                text = nltk.word_tokenize(extra_desc)
                extra_pos = nltk.pos_tag(text)
                for i in range(0,len(extra_pos)):
                      #  if item[0] == "IN":
                       #     over_indx=extra_info.index("over")
                    if extra_pos[i][0] == "over":
                        if extra_pos[i+1][1] == "CD":
                            index_extra = i;
                            if extra_pos[i+1][0]=="one":
                                extra_pos[i+1][0] = 1;
                            elif extra_pos[i+1][0]=="two":
                                extra_pos[i+1][0] = 2;
                            elif extra_pos[i+1][0]=="three":
                                extra_pos[i+1][0] = 3;
                            elif extra_pos[i+1][0]=="four":
                                extra_pos[i+1][0] = 4;
                            elif extra_pos[i+1][0]=="five":
                                extra_pos[i+1][0] = 5;
                            elif extra_pos[i+1][0]=="six":
                                extra_pos[i+1][0] = 6;
                            elif extra_pos[i+1][0]=="seven":
                                extra_pos[i+1][0] = 7;
                            if extra_pos[i+1][0]=="ten":
                                extra_pos[i+1][0] = 10;
                            elif extra_pos[i+1][0]=="twenty":
                                extra_pos[i+1][0] =20;
                            elif extra_pos[i+1][0]=="thirty":
                                extra_pos[i+1][0] = 30;
                            elif extra_pos[i+1][0]=="forty":
                                extra_pos[i+1][0] = 40;
                            elif extra_pos[i+1][0]=="fifty":
                                extra_pos[i+1][0] = 50;
                            elif extra_pos[i+1][0]=="eight":
                                extra_pos[i+1][0] = 8;
                            elif extra_pos[i+1][0]=="nine":
                                extra_pos[i+1][0] = 9;

                            description["out"].insert(len(description["out"]),"xx")
                            description["out"].insert(len(description["out"]),extra_pos[i+1][0])

                for k in range(0,len(extra_pos)):
                    if extra_pos[k][1] == "NNS" or extra_pos[k][1] == "NN":
                        if k!=index_extra:
                            description["out"].insert(len(description["out"]),extra_pos[k][0])
        elif word=="wide" or word=="wides" or (word=="no" and remain_info[iindxx+1] == "ball") or (word=="no" and remain_info[iindxx+1] == "balls"):
            description={}
            description["wide"]=[]
            if word == "wide" or word=="wides":
                description["wide"].insert(len(description["wide"]),"ww")
            else:
                description["wide"].insert(len(description["wide"]),"nn")
            description["wide"].insert(len(description["wide"]),name)
            index = remain_info.index(word)
        #    ll = remain_info.index(word)
            extra_info=[]
            extra_info = remain_info[index+1:]
            extra_desc = ' '.join(extra_info)
            #print extra_desc

            #check for number case
            for item in pos:
                if item[1] == "CD":
                    if remain_info[index-1] == item[0]:
                        description["wide"].insert(2,"number");
                        if remain_info[index-1]=="one":
                            remain_info[index-1] = 1;
                        elif remain_info[index-1]=="two":
                            remain_info[index-1]  = 2;
                        elif remain_info[index-1] =="three":
                            remain_info[index-1]  = 3;
                        elif remain_info[index-1] =="four":
                            remain_info[index-1]  = 4;
                        elif remain_info[index-1] =="five":
                            remain_info[index-1]  = 5;
                        elif remain_info[index-1] =="six":
                            remain_info[index-1]  = 6;
                        elif remain_info[index-1] =="seven":
                            remain_info[index-1]  = 7;
                        elif remain_info[index-1] =="ten":
                            remain_info[index-1]  = 10;
                        elif remain_info[index-1] =="twenty":
                            remain_info[index-1]  =20;
                        elif remain_info[index-1] =="thirty":
                            remain_info[index-1]  = 30;
                        elif remain_info[index-1] =="forty":
                            remain_info[index-1]  = 40;
                        elif remain_info[index-1] =="fifty":
                            remain_info[index-1]  = 50;
                        elif remain_info[index-1] =="eight":
                            remain_info[index-1]  = 8;
                        elif remain_info[index-1] =="nine":
                            remain_info[index-1]  = 9;
                        description["wide"].insert(3,remain_info[index-1])
            #check for other then number
            if len(description["wide"]) < 3:
                if remain_info[index-1] == "maximum":
                    description["wide"].insert(2,"max")
                else:
                    description["wide"].insert(2,"no")
                    #description["wide"].insert(3,"1")
            if len(extra_desc) > 0:
                #print "aaaaaaa\n"
                text = nltk.word_tokenize(extra_desc)
                extra_pos = nltk.pos_tag(text)
                for i in range(0,len(extra_pos)):
                    if extra_pos[i][0] == "over":
                        if extra_pos[i+1][1] == "CD":
                            index_extra = i;
                            if extra_pos[i+1][0]=="one":
                                extra_pos[i+1][0] = 1;
                            elif extra_pos[i+1][0]=="two":
                                extra_pos[i+1][0] = 2;
                            elif extra_pos[i+1][0]=="three":
                                extra_pos[i+1][0] = 3;
                            elif extra_pos[i+1][0]=="four":
                                extra_pos[i+1][0] = 4;
                            elif extra_pos[i+1][0]=="five":
                                extra_pos[i+1][0] = 5;
                            elif extra_pos[i+1][0]=="six":
                                extra_pos[i+1][0] = 6;
                            elif extra_pos[i+1][0]=="seven":
                                extra_pos[i+1][0] = 7;
                            elif extra_pos[i+1][0]=="ten":
                                extra_pos[i+1][0] = 10;
                            elif extra_pos[i+1][0]=="twenty":
                                extra_pos[i+1][0] =20;
                            elif extra_pos[i+1][0]=="thirty":
                                extra_pos[i+1][0] = 30;
                            elif extra_pos[i+1][0]=="forty":
                                extra_pos[i+1][0] = 40;
                            elif extra_pos[i+1][0]=="fifty":
                                extra_pos[i+1][0] = 50;
                            elif extra_pos[i+1][0]=="eight":
                                extra_pos[i+1][0] = 8;
                            elif extra_pos[i+1][0]=="nine":
                                extra_pos[i+1][0] = 9;
                            description["wide"].insert(len(description["wide"]),"xx")
                            description["wide"].insert(len(description["wide"]),extra_pos[i+1][0])
                for k in range(0,len(extra_pos)):
                    if extra_pos[k][1] == "NNS" or extra_pos[k][1] == "NN":
                        if k!=index_extra:
                            description["wide"].insert(len(description["wide"]),extra_pos[k][0])
    #print description
    #return description

def func_dismiss(dictionary):
    global match_info
    if match_info == "first":
        f = open("match1_innings1",'r')
        fn = open("match1_innings2",'r')
    elif match_info == "second":
        f = open("match2_innings1",'r')
        fn = open("match2_innings2",'r')
    elif match_info == "third":
        f = open("match3_innings1",'r')
        fn = open("match3_innings2",'r')
    elif match_info == "fourth":
        f = open("match4_innings1",'r')
        fn = open("match4_innings2",'r')
    elif match_info == "fifth":
        f = open("match5_innings1",'r')
        fn = open("match5_innings2",'r')
    desc1 = f.readlines()
    desc2 = fn.readlines()
    desc = desc1 + desc2
    for line in range(0,len(desc)):
        if "OUT,\n" == desc[line]:
            bats_ball = desc[line-1].split(" to ")
            bats = bats_ball[1]
            bowler = bats_ball[0]
            pp = dictionary["dismiss"][0] + ",\n"
            if  pp == bats:
                ba=desc[line-2].split(".")
                ball = ba[1]
                over = int(ba[0]) + 1
                if question_info == "dismiss":
                    print bowler,
                    print "is the bowler\n"
                    return
              
def check_commentary(dictionary):
    if match_info == "first":
        f = open("match1_innings1",'r')
        fn = open("match1_innings2",'r')
    elif match_info == "second":
        f = open("match2_innings1",'r')
        fn = open("match2_innings2",'r')
    elif match_info == "third":
        f = open("match3_innings1",'r')
        fn = open("match3_innings2",'r')
    elif match_info == "fourth":
        f = open("match4_innings1",'r')
        fn = open("match4_innings2",'r')
    elif match_info == "fifth":
        f = open("match5_innings1",'r')
        fn = open("match5_innings2",'r')
    desc1 = f.readlines()
    desc2 = fn.readlines()
    desc = desc1 + desc2
    b_l = []
   # print dictionary
    if "out" in dictionary:
        over_list = []
        bowler_list=[]
        for line in range(0,len(desc)):
            if "OUT,\n" == desc[line]:
                bats = desc[line-1].split(" ")
                ba=desc[line-2].split(".")
                ball = ba[1].split("\n")[0]
                over = int(ba[0]) + 1
                bowler = desc[line-1].split("to")
                bowler = bowler[0]
                bowler_list.insert(len(bowler_list),bowler)
                over_list.insert(len(over_list),over)
                if dictionary["out"][0]!='':
                    pp = dictionary["out"][0] + ",\n"
                    if  pp == bats[-1]:
                        if len(dictionary["out"])>1:
                            if dictionary["out"][1]=="xx":
                                if over != int(dictionary["out"][2]):
                                    print "NONE\n"
                                    return
                        if question_info == "ball":
                            print ball,
                            print " is the ball\n"
                            return
                        elif question_info == "bowler" or question_info=="bowler(s)" or question_info=="bowlers":
                            print bowler,
                            print " is the bowler\n"
                            return
                        elif question_info == "over":
                            print over,
                            print " is the over\n"
                            return
                        elif question_info == "dismissed":
                            print bowler,
                            print " is the bowler who dismissed\n"
                            return
                else:
                    if "xx" in dictionary["out"]:
                        if over == int(dictionary["out"][2]):
                            if question_info == "ball":
                                print ball,
                                print " is the ball\n"
                                return
                            elif question_info == "bowler" or question_info=="bowler(s)" or question_info=="bowlers":
                                print bowler,
                                print " is the bowler\n"
                                return
       #return
        if dictionary["out"][0]=='':
            if question_info == "over" or question_info == "overs" or question_info=="over(s)":
                temp = []
                for i in over_list:
                    if i not in temp:
                        temp.insert(len(temp),i)
                if len(temp)>0:
                    print temp,
                    print "is/are the required overs\n"
                    return
                else:
                    print "NONE\n"
                    return
            elif question_info == "bowler" or question_info == "bowlers" or question_info=="bowler(s)":
                temp = []
                for i in bowler_list:
                    if i not in temp:
                        temp.insert(len(temp),i)
                if len(temp)>0:
                    print temp,
                    print "is/are the required bowlers\n"
                    return
                else:
                    print "NONE\n"
                    return
        print "NONE\n"
    elif "hit" in dictionary:
        #print "dictionary[hiy]",
       # print dictionary["hit"]
        printing_done=0;
        over_list=[]
        bowler_list=[]
        bowlerss_list=[]
        ball_list = []
        ball_list_specific = []
        count=0  
        max_runs={}
        #runs_bowler={}
        max_runs_bowler = {}
        max_runs_batsman={}
        count_obtained = 0;#checking if the number of runs(ones/twos/4s/6s) given is obtained
        for i in range(1,51):
            max_runs[i] = 0;#index is the over
        for line in range(0,len(desc)):
            bat_ball = desc[line].split()
            if len(bat_ball) <= 5:
                if "to" in bat_ball:
                    ix = bat_ball.index("to")
                    batsman = ' '.join(bat_ball[ix+1:])
                    if dictionary["hit"][0]+","==batsman:
                        #if no number number case
                        if dictionary["hit"][1]!="number" and dictionary["hit"][1]!="max":
                            #if runs scored = given runs
                            if dictionary["hit"][1] + "\n" == desc[line+1]:
                                over_ball = desc[line-1].split(".")
                                over_list.insert(len(over_list),int(over_ball[0]) + 1)
                                bowler_list.insert(len(bowler_list),' '.join(bat_ball[:ix]))
                                ball = int(over_ball[1].split("\n")[0])
                                #ball = over_ball[1]
                                if "xx" in dictionary["hit"]:
                                    inx = dictionary["hit"].index("xx")
                                    if str(over_list[len(over_list)-1]-1) == dictionary["hit"][inx+1]:
                                        if question_info == "ball(s)" or "balls":
                                            ball_list.insert(len(ball_list),ball)
                                        if question_info == "bowler":
                                            print bowler_list[len(bowler_list)-1],
                                            print "is the required bowler\n"
                                            printing_done=1;
                                            break
                                        if question_info == "ball":
                                            print ball,
                                            print "is the required ball\n"
                                            printing_done=1;
                                            break
                                else:
                                    ball_list.insert(len(ball_list),ball)
                                    if question_info == "ball":
                                        temp=[]
                                        for i in ball_list:
                                            if i not in temp:
                                                temp.insert(len(temp),i)
                                        print temp[0],
                                        print "is the required ball\n"
                                        printing_done=1;
                                        break
                        elif dictionary["hit"][1] == "max":
                            if dictionary["hit"][2] + "\n" == desc[line+1]:
                                over_ball = desc[line-1].split(".")
                                over_list.insert(len(over_list),int(over_ball[0]) + 1)
                                bowler = ' '.join(bat_ball[:ix])
                                bowler_list.insert(len(bowler_list),' '.join(bat_ball[:ix]))
                              #  ball = over_ball[1]
                               # ball_list.insert(len(ball_list),ball)
                                max_runs[int(over_ball[0])+1] += 1;
                                if bowler not in max_runs_bowler:
                                    max_runs_bowler[bowler] = 0;
                                max_runs_bowler[bowler] += 1;
                                printing_done = 0;
                        else:#if number case
                            #checking run scored
                            if dictionary["hit"][3] + "\n" == str(desc[line+1]):
                                over_ball = desc[line-1].split(".")
                                over_list.insert(len(over_list),int(over_ball[0]) + 1)
                                ball = int(over_ball[1].split("\n")[0])
                                #ball = int(over_ball[1])
                                fl=0;
                                if "xx" not in dictionary["hit"]:
                                    ball_list.insert(len(ball_list),ball)
                                    count +=1
                                    try:
                                        if int(dictionary["hit"][2]):
                                            sammpp=1
                                    except ValueError:
                                        print "put digits in place of number in words in the question"
                                        return
                                    bowlerss_list.insert(len(bowlerss_list),' '.join(bat_ball[:ix]))
                                    if count == int(dictionary["hit"][2]):
                                        count_obtained = 1;
                                        #for checking if count after becoming 0 in that over has reached the answer
                                        bowler_list.insert(len(bowler_list),' '.join(bat_ball[:ix]))
                                        if question_info == "bowler":
                                            if len(bat_ball[:ix]) > 1:
                                                print " ".join(bat_ball[:ix]),
                                            else:
                                                print ' '.join(bat_ball[:ix]),
                                            print "is the required bowler\n"
                                            printing_done=1;
                                        elif question_info == "bowler(s)":
                                            print bowlerss_list,
                                            print "is/are the required bowlers\n"
                                            printing_done=1
                                            return
                                       #     bowler_list.insert(len(bowler_list),bat_ball[:ix])
                                        elif question_info == "over":
                                            cnt=0;
                                            for ov in over_list:
                                                if ov==int(over_ball[0])+1:
                                                    cnt +=1
                                            if cnt > count:
                                                count=0
                                                fl = 1
                                            if fl != 1:
                                                flag=0;
                                                if ball!= 6:
                                                    l = line
                                                    for temp_iter in range(l,len(desc)):
                                                        if "." in desc[temp_iter]:
                                                            over_ball1 = desc[temp_iter].split(".")
                                                            if len(over_ball1)==2:
                                                                if over_ball[0]!=over_ball1[0]:
                                                                    break
                                                                ball1 = int(over_ball1[1])
                                                                if dictionary["hit"][3] + "\n" == desc[line+1]:
                                                                    count = 0;
                                                                    flag=1;
                                            if flag!=1:
                                                print over_ball[0],
                                                print "is the required over\n"
                                                printing_done=1;
                                        elif question_info == "ball":
                                            print ball,
                                            print "is the required ball\n"
                                            printing_done=1;
                                else:
                                    inx = dictionary["hit"].index("xx")
                                    if str(over_list[-1]) == dictionary["hit"][inx+1]:
                                        count += 1;
                                        ball_list.insert(len(ball_list),ball)
                                        if count == int(dictionary["hit"][2]):
                                            count_obtained=1
                                            if question_info == "bowler":
                                                if len(bat_ball[:ix]) > 1:
                                                    print " ".join(bat_ball[:ix]),
                                                else:
                                                    print bat_ball[:ix],
                                                print "is the required bowler\n"
                                                printing_done=1;
                                            elif question_info == "ball":
                                                print ball
                                                print "is the required ball\n"
                                                printing_done=1;
                                if count==0:
                                    bowler_list=[]
                    elif dictionary["hit"][0] == '':
                        print over_list
                        #number case
                        if dictionary["hit"][1]=="number":
                            #checking for the run
                            if dictionary["hit"][3] + "\n" == str(desc[line+1]):
                                over_ball = desc[line-1].split(".")
                                over_list.insert(len(over_list),int(over_ball[0]) + 1)
                                ball = int(over_ball[1].split("\n")[0])
                                fl=0;
                                if "xx" in dictionary:
                                    inx = dictionary["hit"].index("xx")
                                    if str(over_list[-1]) == dictionary["hit"][inx+1]:
                                        count += 1;
                                        ball_list.insert(len(ball_list),ball)
                                        batsman = ' '.join(bat_ball[ix+1:])
                                        if batsman not in max_runs_batsman:
                                            max_runs_batsman[batsman] = 0;
                                        max_runs_batsman[batsman] += 1
                                        if count == int(dictionary["hit"][2]):
                                            count_obtained=1
                                            if question_info == "bowler":
                                                if len(bat_ball[:ix]) > 1:
                                                    print " ".join(bat_ball[:ix]),
                                                else:
                                                    print bat_ball[:ix],
                                                print "is the required bowler\n"
                                                return
                                                printing_done=1;
                                            elif question_info == "ball":
                                                print ball
                                                print "is the required ball\n"
                                                return
                                                printing_done=1;
                                else:
                                    count +=1
                                  #  ball_list.insert(len(ball_list),ball)
                                    try:
                                        if int(dictionary["hit"][2]):
                                            sammpp=1
                                    except ValueError:
                                        print "put digits in place of number in words in the question"
                                        return
                                    bowler = ' '.join(bat_ball[:ix])
                                    if bowler not in max_runs_bowler:
                                        max_runs_bowler[bowler]=0
                                    max_runs_bowler[bowler] += 1;
                                    ball_list.insert(len(ball_list),ball)
                                   # bowlerss_list.insert(len(bowlerss_list),' '.join(bat_ball[:ix]))
                                    batsman = ' '.join(bat_ball[ix+1:])
                                    if batsman not in max_runs_batsman:
                                        max_runs_batsman[batsman] = 0;
                                    max_runs_batsman[batsman] += 1
                                    #print dictionary
                                    if count == int(dictionary["hit"][2]):
                                        count_obtained = 1;
                                        #for checking if count after becoming 0 in that over has reached the answer
                                        bowler_list.insert(len(bowler_list),' '.join(bat_ball[:ix]))
                                      #  if question_info == "bowler(s)" or question_info == "bowler":
                                       #     print bowlerss_list,
                                        #    print "is/are the required bowlers\n"
                                         #   printing_done=1
                                          #  return
                                        if question_info == "ball" or question_info == "balls":
                                            print ball_list,
                                            print "is/are the required balls\n"
                                            printing_done=1;
                                            return 
                        elif dictionary["hit"][1] == "max":
                            if dictionary["hit"][2] + "\n" == desc[line+1]:
                                over_ball = desc[line-1].split(".")
                                over_list.insert(len(over_list),int(over_ball[0]) + 1)
                                bowler = ' '.join(bat_ball[:ix])
                                bowler_list.insert(len(bowler_list),bowler)
                                batsman = ' '.join(bat_ball[ix+1:])
                                #batsman_list.insert(len(batsman_list),batsman)
                                max_runs[int(over_ball[0])+1] += 1;
                                if bowler not in max_runs_bowler:
                                    max_runs_bowler[bowler] = 0;
                                if batsman not in max_runs_batsman:
                                    max_runs_batsman[batsman] = 0;
                                max_runs_bowler[bowler] += 1;
                                max_runs_batsman[batsman] += 1;
                                printing_done = 0;
                        else:            
                            #if runs scored = given runs
                                if dictionary["hit"][1] + "\n" == desc[line+1]:
                                    over_ball = desc[line-1].split(".")
                                    over_list.insert(len(over_list),int(over_ball[0]) + 1)
                                    bowler_list.insert(len(bowler_list),' '.join(bat_ball[:ix]))
                                    ball = int(over_ball[1].split("\n")[0])
                                    if "xx" in dictionary["hit"]:
                                        inx = dictionary["hit"].index("xx")
                                        if str(over_list[len(over_list)-1]-1) == dictionary["hit"][inx+1]:
                                            batsman = ' '.join(bat_ball[ix+1:])
                                            if batsman not in max_runs_batsman:
                                                max_runs_batsman[batsman] = 0;
                                            max_runs_batsman[batsman] += 1
                                            ball_list.insert(len(ball_list),ball)
                                            if question_info == "bowler":
                                                print bowler_list[len(bowler_list)-1],
                                                print "is the required bowler\n"
                                                printing_done=1;
                                                return
                                                break
                                            if question_info == "ball":
                                                print ball,
                                                print "is the required ball\n"
                                                printing_done=1;
                                                return
                                                break
                                    else:
                                        batsman = ' '.join(bat_ball[ix+1:])
                                        if batsman not in max_runs_batsman:
                                            max_runs_batsman[batsman] = 0;
                                        max_runs_batsman[batsman] += 1
                                        bowler = ' '.join(bat_ball[:ix])
                                        if bowler not in max_runs_bowler:
                                            max_runs_bowler[bowler]=0
                                        max_runs_bowler[bowler] += 1;
                                        ball_list.insert(len(ball_list),ball)
                                        if question_info == "ball":
                                            temp=[]
                                            for i in ball_list:
                                                if i not in temp:
                                                    temp.insert(len(temp),i)
                                            print temp[0],
                                            print "is the required ball\n"
                                            printing_done=1;
                                            return
                                            break
        if printing_done==0:
            if question_info == "hit":
                if dictionary["hit"][1] == "max":
                    if dictionary["hit"][0]=='':
                        max1 = 0;
                        ans=0;
                        #print max_runs_bowler
                        for bow in max_runs_batsman:
                            if max_runs_batsman[bow] > max1:
                                max1 = max_runs_batsman[bow]
                                ans = bow
                        print ans,
                        print "is the required batsman\n"
                        return
                elif dictionary["hit"][0] == '':
                    if dictionary["hit"][1] == "number":
                        max1 = 0;
                        ans=[];
                        for bow in max_runs_batsman:
                            if max_runs_batsman[bow] >= int(dictionary["hit"][2]):
                                ans.insert(len(ans),bow)
                        print ans,
                        print "is/are the required batsmen\n"
                        return
                    else:
                        ans=[]
                        for bow in max_runs_batsman:
                            if max_runs_batsman[bow] > 0:
                                ans.insert(len(ans),bow)
                        print ans,
                        print "is/are the required batsmen\n"
                        return
            if question_info == "over":
                if dictionary["hit"][1] == "max":
                    if dictionary["hit"][0]!='':
                        max1 = 0;
                        ans=0;
                        print max_runs
                        for ov in max_runs:
                            if max_runs[ov] > max1:
                                max1 = max_runs[ov]
                                ans = ov
                        print ans,
                        print "is the required over"
            elif (question_info == "bowler" or question_info=="bowler(s)" or question_info=="bowlers") and dictionary["hit"][0] == '':
                if dictionary["hit"][0] == '':
                    if dictionary["hit"][1] == "number":
                        max1 = 0;
                        ans=[];
                        for bow in max_runs_bowler:
                            if max_runs_bowler[bow] >= int(dictionary["hit"][2]):
                                ans.insert(len(ans),bow)
                        print ans,
                        print "is/are the required bowlers\n"
                        return
                    else:
                        ans=[]
                        for bow in max_runs_bowler:
                            if max_runs_bowler[bow] > 0:
                                ans.insert(len(ans),bow)
                        print ans,
                        print "is/are the required bowlers\n"
                        return

            elif (question_info == "ball" or question_info=="ball(s)" or question_info=="balls") and dictionary["hit"][0] == '':
                temp=[]
                for i in ball_list:
                    if i not in temp:
                        temp.insert(len(temp),i)
                if dictionary["hit"][1] == "number" and int(dictionary["hit"][2]) != len(temp):
                        print "NONE\n"
                else:
                    if len(temp)>0:
                        print temp,
                        print "is/are the required balls\n"
                    else:
                        print "NONE\n"

            elif question_info == "bowler":
                if dictionary["hit"][1] == "max":
                    if dictionary["hit"][0]!='':
                        max1 = 0;
                        ans=0;
                        print max_runs_bowler
                        for bow in max_runs_bowler:
                            if max_runs_bowler[bow] > max1:
                                max1 = max_runs_bowler[bow]
                                ans = bow
                        print ans,
                        print "is the required bowler\n"
                
            elif question_info == "over(s)" or question_info == "overs":
                temp=[]
                for i in over_list:
                    if i not in temp:
                        temp.insert(len(temp),i)
                if dictionary["hit"][1] == "number" and int(dictionary["hit"][2]) != len(temp):
                        print "NONE\n"
                else:
                    if len(temp)>0:
                        print temp,
                        print "is/are the required overs\n"
                    else:
                        print "NONE\n"
            elif question_info == "bowler(s)" or question_info == "bowlers":
                temp=[]
                for i in bowler_list:
                    if i not in temp:
                        temp.insert(len(temp),i)
                if dictionary["hit"][1] == "number" and int(dictionary["hit"][2]) != len(temp):
                        print "NONE\n"
                else:
                    if len(temp)>0:
                        print temp,
                        print "is/are the required bowlers\n"
                    else:
                        print "NONE\n"
            elif question_info == "ball(s)" or question_info == "balls":
                temp=[]
                if count_obtained==0:
                    print "NONE"
                else:
                    for i in ball_list:
                        if i not in temp:
                            temp.insert(len(temp),i)
                    if dictionary["hit"][1] == "number" and int(dictionary["hit"][2]) != len(temp):
                            print "NONE\n"
                    elif len(temp)>0:
                        print temp,
                        #print ball_list,
                        print "is/are the required balls\n"
                    else:
                        print "NONE\n"

            else:
                print "NONE\n"
    elif "wide" in dictionary:
        #print "dictionary[wide]",
        #print dictionary["wide"]
        printing_done=0;
        over_list=[]
        bowler_list=[]
        ball_list = []
        ball_list_specific = []
        count=0
        number_wide = 0
        max_wides = {}  #index=over value = num of wides in d over
        max_wides_bowler = {}
        #wides
        for i in range(1,51):
            max_wides[i] = 0;
        #for i in range(1,51):
         #   max_wides_bowler[i] = 0;
        for line in range(0,len(desc)):
            temp = desc[line].split()
            if len(temp)==2 or len(temp)==3:
                word1=''
                word2=''
                word3=''
                if len(temp)==2:
                    if dictionary["wide"][0] == "ww":
                        word1 = "wide,"
                        word2 = "wides,"
                        word3 = "wide"
                else:
                    if dictionary["wide"][0] == "nn":
                        word1 = "ball,"
                        word2 = "balls,"
                        word3 = "ball"
                        if temp[2] == word1 or temp[2] == word2:
                            if temp[1] == "no":
                                word1 = "no"
                                word2 = "no"
                if temp[1] == word1 or temp[1] == word2 or temp[1] == word3:
                    if dictionary["wide"][1]!='':
                        bats_balls=desc[line-1].split(" to ")
                        #print bats_balls[0]
                        bowler = bats_balls[0]
                       # print len(bats_balls[0])
                        if dictionary["wide"][1] == bowler:
                            #if number_wide == 0:
                                #print "temp[0]",
                                #print temp[0]
                            number_wide = int(temp[0])
                            #print "over111111\n"
                            over_ball = desc[line-2].split(".")
                            over_list.insert(len(over_list),int(over_ball[0]) + 1)
                            ball = int(over_ball[1])
                            #print over_ball[0];
                            #print "number_wide",
                            #print number_wide
                            max_wides[int(over_ball[0])+1] += int(number_wide)
                            fl=0;
                            ball_list.insert(len(ball_list),ball)
                            #check number case
                            if str(dictionary["wide"][2])==str("number"):
                                if "xx" not in dictionary:
                                    count+=int(number_wide)
                                    if count == int(dictionary["wide"][3]):
                                        if question_info == "ball":
                                            if str(dictionary["wide"][3]) == str(number_wide):
                                                print ball,
                                                print "is the required ball\n"
                                                printing_done=1;
                                        elif question_info == "over":
                                            cnt=0;
                                            for ov in over_list:
                                                if ov==int(over_ball[0])+1:
                                                    cnt +=1
                                            if cnt > count:
                                                count=0
                                                fl = 1
                                            if fl != 1:
                                                flag=0;
                                                if ball!= 6:
                                                    l = line
                                                    for temp_iter in range(l,len(desc)):
                                                        if "." in desc[temp_iter]:
                                                            over_ball1 = desc[temp_iter].split(".")
                                                            if len(over_ball1)==2:
                                                                if over_ball[0]!=over_ball1[0]:
                                                                    break
                                                                ball1 = int(over_ball1[1])
                                                                temp = desc[temp_iter+2].split()
                                                                #print "temp",
                                                                #print temp
                                                                if len(temp)==2 or len(temp)==3:
                                                                    if len(temp)==2:
                                                                        if dictionary["wide"][0] == "ww":
                                                                            word1 = "wide,"
                                                                            word2 = "wides,"
                                                                    else:
                                                                        if dictionary["wide"][0] == "nn":
                                                                            word1 = "ball,"
                                                                            word2 = "balls,"
                                                                        if temp[2] == word1 or temp[2] == word2:
                                                                            if temp[1] == "no":
                                                                                word1 = "no"
                                                                                word2 = "no"
                                                                    if temp[1] == word1 or temp[1] == word2:
                                                                        count = 0;
                                                                        flag=1;
                                            if flag!=1:
                                                print int(over_ball[0]) + 1,
                                                print "is the required over\n"
                                                printing_done=1;
                                elif "xx" in dictionary:
                                    inx = dictionary["wide"].index("xx")
                                    #var = over_list[-1] + 1
                                    if str(over_list[-1]-1) == str(dictionary["wide"][inx+1]):
                                        count += int(number_wide);
                                        if count == int(dictionary["wide"][3]):
                                            if question_info == "bowler":
                                                print bowler,
                                                print "is the required bowler\n"
                                                printing_done=1;
                                            elif question_info == "ball":
                                                print ball,
                                                print "is the required ball\n"
                                                printing_done=1;
                                if count==0:
                                    bowler_list=[]
                            elif str(dictionary["wide"][2])==str("no"):
                                if "xx" not in dictionary["wide"]:
                                    if question_info == "over":
                                        if printing_done!=1:
                                            print over_list[-1],
                                            print "is the required over\n"
                                            printing_done=1
                                elif "xx" in dictionary["wide"]:
                                    inx1 = dictionary["wide"].index("xx")
                                    #print over_list[-1]
                                    #print dictionary["wide"][inx1+1]
                                    if str(over_list[-1]) == str(dictionary["wide"][inx1+1]):
                                        b_l.insert(len(b_l),ball)
                                        if question_info == "ball":
                                            if printing_done!=1:
                                                print ball,
                                                print "is the required ball\n"
                                                printing_done=1;
                                    
                    else:
                        bats_balls=desc[line-1].split(" to ")
                        #print bats_balls[0]
                        bowler = bats_balls[0]
                        if bowler not in max_wides_bowler:
                            max_wides_bowler[bowler] = 0;
                        number_wide = int(temp[0])
                        max_wides_bowler[bowler] += int(number_wide)
            #        if dictionary["hit"][0]+","==batsman:
        if printing_done==0:
            if str(dictionary["wide"][2])==str("no"):
                if "xx" not in dictionary["wide"]:
                    if question_info == "over(s)" or question_info=="overs":
                        temp = []
                        for i in over_list:
                            if i not in temp:
                                temp.insert(len(temp),i)
                        print temp,
                        print "is/are the required overs"
                elif "xx" in dictionary["wide"]:
                    if question_info == "ball(s)" or question_info == "balls":
                        temp = []
                        for i in b_l:
                            if i not in temp:
                                temp.insert(len(temp),i)
                        print temp,
                        print "is/are the required overs"

            elif dictionary["wide"][2] == "max":
                if question_info == "over":
                    if dictionary["wide"][1]!='':
                        max1 = 0;
                        ans=0;
                        #print max_wides
                        for ov in max_wides:
                            if max_wides[ov] > max1:
                                max1 = max_wides[ov]
                                ans = ov
                       # over_var=0;
                        #max_count = 0;
                       # ans=0;
                        #count_over = 0;
                       # if len(over_list)>0:
                        #    over_var = over_list[0];
                       # for i in over_list:
                        #    if i==over_var:
                         #       count_over += 1
                          #  else:
                           #     over_var = i
                            #    count_over = 1
                            #if count_over > max_count:
                            #    ans = i;
                        print ans,
                        print "is the required over\n"
                elif question_info == "bowler":
                    if dictionary["wide"][1]=='':
                        max1 = 0;
                        ans=0;
                        #print max_wides_bowler
                        for bow in max_wides_bowler:
                            if max_wides_bowler[bow] > max1:
                                max1 = max_wides_bowler[bow]
                                ans = bow
                        print ans,
                        print "is the required bowler\n"
            else:
                print "NONE\n"

    f.close()

def main():
    ind = "./player_profile/indian_players_profile.txt"
    nz = "./player_profile/nz_players_profile.txt"
    add_to_dict_profile(profile,ind);
    add_to_dict_profile(profile,nz);
    question = raw_input('Enter a question: ')
    #print question
    text = nltk.word_tokenize(question)
    pos = nltk.pos_tag(text)
    #print pos
    #print pos[0]
    #print pos[0][1]
    list_words=question.split()
    index_match = parse_match_info(question,list_words)
 #   print "asadasdas",
#    print match_info
    if index_match!= -1:
        remain_info = list_words[index_match+1:]
   #     print "remain",
  #      print remain_info
        index_question = parse_question_info(remain_info);
        if index_question == -1:
            print "Grammar for question not properly defined"
        else:
            remain_info = remain_info[:index_question]
    elif index_match == -1:
        print "Question is not following the defined grammar"
    if index_match!=-1 and index_question!=-1:
        if question_info == "dismiss":
            parse_for_desc(remain_info,profile,pos)
            func_dismiss(description)
        else:
            parse_for_desc(remain_info,profile,pos)
            if ret_variable == 0:
  #          print description
 #           print match_info,question_info,remain_info
                check_commentary(description)


#print match_info

if __name__ == "__main__":
    main()
