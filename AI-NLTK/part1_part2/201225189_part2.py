import nltk
import sys

connector_info=''
# function to add the contents of file, after proper parsing, to the given dictionary
def add_to_dict(dictionary, fname):
    c=','
    f = open(fname, 'r')
    for line in f:
        temp = line[:-1]
        temp = temp.split(c)
        a = temp[0]
        b = temp[1:]
        if a not in dictionary:
            dictionary[a] = b

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

# It retrieves the variable names corresponding to players of the match
def parse_for_players_winteam(profile,winning_team):
    toreturn  = []
    if winning_team[0] == 'tied':
        return toreturn
    # team for which player plays is in 3rd column
    for i in profile:
        temp = profile[i]
        temp1 = temp[3]
        temp2 = temp1.split(', ')
        if winning_team[0] in temp2:
            toreturn.append(i)
    return toreturn

def parse_for_players_losing_team(winning_team,profile):
    toreturn  = []
    if winning_team[0] == 'tied':
        return toreturn
    if winning_team[0] == 'New Zealand':
        losing_team = 'India'
    else:
        losing_team = 'New Zealand'
    # team for which player plays is in 3rd column
    for i in profile:
        temp = profile[i]
        temp1 = temp[3]
        temp2 = temp1.split(',')
        if losing_team in temp2:
            toreturn.append(i)
    return toreturn

def parse_for_duck(bats):
    toreturn = []
    for i in bats:
        temp = bats[i]
  #      print temp
        temp1 = temp[1]
   #     print temp1
        if temp1=='0':
    #        print temp1
            toreturn.append(i)
    return toreturn

def parse_lessthan26(profile):
    toreturn  = []
    # team for which player plays is in 3rd column
    for i in profile:
        temp = profile[i]
        temp1 = temp[2]
        temp2 = temp1.split(' ')
        temp3 = int(temp2[0])
        if temp3 < 26:
            toreturn.append(i)
    return toreturn

score = {}
no_ducks = []
def parse_250run(bats1,bats2,bats3,bats4,bats5):
    toreturn = []
    for i in bats1:
        temp = bats1[i]
        runs = int(temp[1])
        score[i] = runs
        if runs > 0 :
            no_ducks.insert(len(no_ducks),i)
    for i in bats2:
        temp = bats2[i]
        runs = int(temp[1])
        if i not in score:
            score[i] = runs 
        else:
            score[i] += runs
        if runs == 0:
            if i in no_ducks:
                no_ducks.remove(i);
        elif runs > 0:
            if i not in bats1:
                no_ducks.insert(len(no_ducks),i)
            
    for i in bats3:
        temp = bats3[i]
        runs = int(temp[1])
        if i not in score:
            score[i] = runs 
        else:
            score[i] += runs
        if runs == 0:
            if i in no_ducks:
                no_ducks.remove(i);
        elif runs > 0:
            if i not in bats1 and i not in bats2:
                no_ducks.insert(len(no_ducks),i)
            

    for i in bats4:
        temp = bats4[i]
        runs = int(temp[1])
        if i not in score:
            score[i] = runs 
        else:
            score[i] += runs
        if runs == 0:
            if i in no_ducks:
                no_ducks.remove(i);
        elif runs > 0:
            if i not in bats1 and i not in bats2 and i not in bats3 :
                no_ducks.insert(len(no_ducks),i)
    
    for i in bats5:
        temp = bats5[i]
        runs = int(temp[1])
        if i not in score:
            score[i] = runs 
        else:
            score[i] += runs
        if runs == 0:
            if i in no_ducks:
                no_ducks.remove(i);
        elif runs > 0:
            if i not in bats1 and i not in bats2 and i not in bats3 and i not in bats4 :
                no_ducks.insert(len(no_ducks),i)
    for i in score:
        total_score = score[i]
        if total_score > 250:
            toreturn.append(i)
    return toreturn



# This function returns a list of variable, corresponding to players who satisfy the criteria : strike rate > 150.0
def parse_for_sr(bat, num):
    toreturn = []
    # strike rate is in the 7th column
    for i in bat:
        temp = bat[i]
        k = float(temp[6])
        if k > num:
            toreturn.append(i)
    return  toreturn

def parse_for_belowstr(bat,num):
    toreturn = []
    for i in bat:
        temp = bat[i]
        k = float(temp[6])
        if k < num:
            toreturn.append(i)
    return toreturn

# It retrieves the variable names corresponding to players, who have greater than 0 sixes
def parse_for_six_thanfour(bat):
    toreturn  = []
    # number of six hit are in 6th column
    for i in bat:
        temp = bat[i]
        num_six = int(temp[5])
        num_four = int(temp[4])
        if num_six > num_four:
            toreturn.append(i)                                                    
    return toreturn   

def parse_for_1boundary(bat):
    toreturn  = []
    # number of boundary hit are in 5th column
    for i in bat:
        temp = bat[i]
        runs = int(temp[1])
      #  print i + '->' + str(num_four)
        if runs > 50:
            toreturn.append(i)                                                    
    return toreturn   

def parse_for_1wicket(ball):
    toreturn  = []
    # number of boundary hit are in 5th column
    for i in ball:
        temp = ball[i]
        num_wickets = int(temp[3])
        if num_wickets > 0:
            toreturn.append(i)                                                    
    return toreturn   


def parse_for_50runs(bat):
    toreturn  = []
    # number of boundary hit are in 5th column
    for i in bat:
        temp = bat[i]
        runs = int(temp[1])
      #  print i + '->' + str(num_four)
        if runs > 50:
            toreturn.append(i)                                                    
    return toreturn   

def parse_for_scorehundred(bat):
    toreturn  = []
    for i in bat:
        temp = bat[i]
        runs = int(temp[1])
        if runs > 99:
            toreturn.append(i)                                                    
    return toreturn   

def parse_for_nowickets(ball):
    toreturn  = []
    # number of boundary hit are in 5th column
    for i in ball:
        temp = ball[i]
        wickets = int(temp[3])
        if wickets == 0:
            toreturn.append(i)                                                    
    return toreturn   

def parse_for_rhb_bowlers(balls,profile):
    toreturn  = []
    # team for which player plays is in 3rd column
    for i in balls:
        temp = profile[i]
        temp1 = temp[-1]
        if 'right' in temp1 or 'Right' in temp1:
            if (int(balls[i][3])>0):
                toreturn.append(i)
    return toreturn


def parse_for_lhb_bowlers(balls,profile):
    toreturn  = []
    # team for which player plays is in 3rd column
    for i in balls:
        temp = profile[i]
        temp1 = temp[-1]
        if 'left' in temp1 or 'Left' in temp1: 
            if (int(balls[i][3])>0):
                toreturn.append(i)
    return toreturn

def parse_for_7overs(ball):
    toreturn  = []
    for i in ball:
        temp = ball[i]
        overs = float(temp[0])
        if overs > 7:
            toreturn.append(i)                                                    
    return toreturn  

def parse_for_economygr8_than8(ball):
    toreturn  = []
    for i in ball:
        temp = ball[i]
        economy = float(temp[4])
        if economy > 8.00:
            toreturn.append(i)                                                    
    return toreturn 

mom = []
def parse_gt2player_match(player_match):
    toreturn  = []
    for i in player_match:
        temp = player_match[i]
        player = temp[0]
        if player in mom:
            toreturn.append(player)
        else:
            mom.insert(len(mom),player)
    return toreturn 

quantifier_info = ''
def parse_for_quantifier_info(list_words):
    global quantifier_info
#    list_words = query.split()
    if (list_words[0] == "for" or list_words[0] == "For") and list_words[1] == "all":
        if list_words[2] == "matches," or list_words[2] == "matches":
            quantifier_info = "for_match"
            return 2
        elif list_words[2] == "innings," or list_words[2] == "innings":
            quantifier_info = "innings"
            return 2
        else:
            return -1
    elif (list_words[0] == "There" or list_words[0] == "there") and list_words[1] == "exists":
        if list_words[2] == "a" and list_words[3] == "match":
            quantifier_info = "exist_match"
            return 3
        elif list_words[2] == "a" and (list_words[3] == "player" or list_words[3] == "player,"):
            quantifier_info = "player"
            return 2
        else:
            return -1
    else:
        return -1

def wickets_claimed_rhb(balls,c1):
    rhb_wickets = 0;
    for bowler in c1:
        if bowler in balls:
            temp = balls[bowler];
            temp1 = int(temp[3])
            rhb_wickets += temp1
    return rhb_wickets
 
def wickets_claimed_lhb(balls,c2):
    lhb_wickets = 0;
    for bowler in c2:
        if bowler in balls:
            temp = balls[bowler];
            temp1 = int(temp[3])
            lhb_wickets += temp1
    return lhb_wickets    

def parse_for_rhb_gtlhb(balls,profile):
    c1 = parse_for_rhb_bowlers(balls,profile);
    c2 = parse_for_lhb_bowlers(balls,profile);
    right_wickets = wickets_claimed_rhb(balls,c1);
    left_wickets = wickets_claimed_lhb(balls,c2);
    if right_wickets > left_wickets:
        toreturn = c1;
    else:
        toreturn = []
    return toreturn

def make_model(m_of_match,winning_team,profile,bats,balls,c1):
    name_to_var = {}
    count=0;
    man_of_match = m_of_match[0]
    man_of_match = [man_of_match]
    players_winning_team = parse_for_players_winteam(profile,winning_team)
    players_scored_duck = parse_for_duck(bats);
    players_losing_team = parse_for_players_losing_team(winning_team,profile);
    strate_above200 = parse_for_sr(bats, 200.0)
    six_thanfour = parse_for_six_thanfour(bats)
    atleast_1boundary = parse_for_1boundary(bats);
    strate_below100 = parse_for_belowstr(bats,100);
    gt50runs = parse_for_50runs(bats);
    atleast_1wicket = parse_for_1wicket(balls);
    players_nowickets = parse_for_nowickets(balls);
    gt7overs = parse_for_7overs(balls);
    economygt8=parse_for_economygr8_than8(balls);
    score_hundred = parse_for_scorehundred(bats);
    rhb_gt_lhb = parse_for_rhb_gtlhb(balls,profile);
    for i in profile:
        if i not in name_to_var:
            name_to_var[i] = 'r' + str(count)
            count += 1
    # Now for creating a Model, we need to write down a string which shows mapping from predicates to varible names
    temp_strin1 = ''
    for i in name_to_var:
        temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
    
    # this is for the predicate "m_of_match"
    temp_strin2 = 'm_of_match => {'
    for i in man_of_match:
        temp_strin2 += name_to_var[i] +  ','
    temp_strin2 = temp_strin2[:-1]  #removing the extra "," character                                                           
    temp_strin2 += '} \n'
    #now for the predicate "players_winteam"
    temp_strin3 = 'players_winteam => {'
    if players_winning_team!=[]:
        for i in players_winning_team:
            temp_strin3 += name_to_var[i] + ','
        temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
    temp_strin3 += '}\n'
    # this is for the predicate "duck"
    temp_strin4 = 'players_scored_duck => {'
    if players_scored_duck!=[]:
        for i in players_scored_duck:
            temp_strin4 += name_to_var[i] +  ','
        temp_strin4 = temp_strin4[:-1]  #removing the extra "," character                                                           
    temp_strin4 += '} \n'
    #now for the predicate "players_winteam"
    temp_strin5 = 'players_losing_team => {'
    if players_losing_team!=[]:
        for i in players_losing_team:
            temp_strin5 += name_to_var[i] + ','
        temp_strin5 = temp_strin5[:-1]  #removing the extra "," charater
    temp_strin5 += '}\n'
# this is for the predicate "srate"
    temp_strin6 = 'srate_above200 => {'
    if strate_above200!=[]:
        for i in strate_above200:
            temp_strin6 += name_to_var[i] +  ','
        temp_strin6 = temp_strin6[:-1]  #removing the extra "," character
    temp_strin6 += '} \n'
    #print temp_strin6
    #now for the predicate "gtsixthan4"
    temp_strin7 = 'gtsixthan4 => {'
    if six_thanfour!=[]:
        for i in six_thanfour:
            temp_strin7 += name_to_var[i] + ','
        temp_strin7 = temp_strin7[:-1]  #removing the extra "," charater
    temp_strin7 += '}\n'
    temp_strin8 = '1boundary => {'
    if atleast_1boundary!=[]:
        for i in atleast_1boundary:
            temp_strin8 += name_to_var[i] + ','
        temp_strin8 = temp_strin8[:-1]  #removing the extra "," charater
    temp_strin8 += '} \n'
    temp_strin9 = 'strbelow100 => {'
    if strate_below100!=[]:
        for i in strate_below100:
            temp_strin9 += name_to_var[i] + ','
        temp_strin9 = temp_strin9[:-1]  #removing the extra "," charater
    temp_strin9 += '}\n'
    temp_strin10 = 'gt50runs => {'
    if gt50runs!=[]:
        for i in gt50runs:
            temp_strin10 += name_to_var[i] +  ','
        temp_strin10 = temp_strin10[:-1]  #removing the extra "," character
    temp_strin10 += '} \n'
    #now for the predicate "gtsixthan4"
    temp_strin11 = 'atleast_1wicket => {'
    if atleast_1wicket!=[]:
        for i in atleast_1wicket:
            temp_strin11 += name_to_var[i] + ','
        temp_strin11 = temp_strin11[:-1]  #removing the extra "," charater
    temp_strin11 += '}\n'
    temp_strin12 = ''
    temp_strin12 = 'nowickets => {'
    if players_nowickets!=[]:
        for i in players_nowickets:
            temp_strin12 += name_to_var[i] +  ','
        temp_strin12 = temp_strin12[:-1]  #removing the extra "," character
    temp_strin12 += '} \n'
    #now for the preicate "gtsixthan4"
    temp_strin13 = 'gt7overs => {'
    if gt7overs!=[]:
        for i in gt7overs:
            temp_strin13 += name_to_var[i] + ','
        temp_strin13 = temp_strin13[:-1]  #removing the extra "," charater
    temp_strin13 += '}\n'
    temp_strin14 = '8economy => {'
    if economygt8!=[]:
        for i in economygt8:
            temp_strin14 += name_to_var[i] + ','
        temp_strin14 = temp_strin14[:-1]  #removing the extra "," charater
    temp_strin14 += '}\n'
    temp_strin15 = 'scorehundred=> {'
    if score_hundred!=[]:
        for i in score_hundred:
            temp_strin15 += name_to_var[i] +  ','
        temp_strin15 = temp_strin15[:-1]  #removing the extra "," character
 #   else:
  #      temp_strin2 += ' '
    temp_strin15 += '} \n'
    temp_strin16 = 'rhb_bowlers_btlhb=> {'
    if rhb_gt_lhb!=[]:
        for i in rhb_gt_lhb:
            temp_strin16 += name_to_var[i] +  ','
        temp_strin16 = temp_strin16[:-1]  #removing the extra "," character
    temp_strin16 += '}\n'
    age_lt26 = parse_lessthan26(profile);
    gt250 = c1;
    players_noducks = no_ducks;
    temp_strin17 = 'lessthan26=> {'
    if age_lt26!=[]:
        for i in age_lt26:
            temp_strin17 += name_to_var[i] +  ','
        temp_strin17 = temp_strin17[:-1]  #removing the extra "," character
    temp_strin17 += '}\n'
    temp_strin18 = 'gt250run => {'
    if gt250!=[]:
        for i in gt250:
            temp_strin18 += name_to_var[i] + ','
        temp_strin18 = temp_strin18[:-1]  #removing the extra "," charater
    temp_strin18 += '}\n'
    temp_strin19 = 'noducks => {'
    if players_noducks!=[]:
        for i in players_noducks:
            temp_strin19 += name_to_var[i] + ','
        temp_strin19 = temp_strin4[:-1]  #removing the extra "," charater
    temp_strin19 += '}'
 

    v = temp_strin1 + temp_strin2 + temp_strin3 + temp_strin4 + temp_strin5 + temp_strin6 + temp_strin7 + temp_strin8 + temp_strin9 + temp_strin10 + temp_strin11 + temp_strin12 + temp_strin13 + temp_strin14 + temp_strin15 + temp_strin16 + temp_strin17 + temp_strin18 + temp_strin19
    val = nltk.parse_valuation(v)
  #  dom = val.domain
   # m = nltk.Model(dom, val)
    return val


def parse_for_connector_info(remain_info):
    global connector_info
    for i in range(0,len(remain_info)):
        if remain_info[i] == "contains":
            connector_info="contains"
            return i
        elif remain_info[i] == "consists" and remain_info[i+1] == "of":
            connector_info="consists"
            return i
        elif remain_info[i] == "is" and remain_info[i+1] == "given" and remain_info[i+2] == "to":
            connector_info = "given"
            return i
        elif remain_info[i] == "and":
            connector_info = "and"
            return i
    if ("if" in remain_info) and ("then" in remain_info):
        connector_info = "if"
        index = remain_info.index("then")
        return index
    return -1

def find_predicate(predicate):
    #print predicate
    for i in range(0,len(predicate)):
        if (predicate[i] == "player"  or predicate[i] == "\"Player"):
            if len(predicate) > i+2:
                if predicate[i+1]=="of" and ("match" in predicate[i+2]):
                    final_predicate = "m_of_match"
                    return final_predicate        
        #if (predicate[i] == "winning" and (predicate[i+1] == "side" or predicate[i+1] == "team" or predicate[i+1] == "team." or predicate[i+1] == "teams" or predicate[i+1] == "teams." or "side" in predicate[i+1] or "team" in predicate[i+1])) or (predicate[i]=="team" and (predicate[i+1]=="won" or "won" in predicate[i+1])):
        if predicate[i] == "winning":
            if len(predicate) > i+1:
                if "side" in predicate[i+1] or "team" in predicate[i+1]:
                    final_predicate = "players_winteam"
                    return final_predicate
        if predicate[i] == "team":
            if len(predicate) > i+1:
                if "won" in predicate[i+1]:
                    final_predicate = "players_winteam"
                    return final_predicate
       # if predicate[i] == "losing" and (predicate[i+1] == "side" or predicate[i+1] == "team" or "side" in predicate[i+1] or "team" in predicate[i+1] ) or (predicate[i]=="team" and (predicate[i+1]=="lost" or "lost" in predicate[i+1])):
        if predicate[i] == "losing":
            if len(predicate) > i+1:
                if "side" in predicate[i+1] or "team" in predicate[i+1]:
                    final_predicate = "players_losing_team"
                    return final_predicate
        if predicate[i] == "team":
            if len(predicate) > i+1:
                if "lost" in predicate[i+1]:
                    final_predicate = "players_losing_team"
                    return final_predicate

        if predicate[i] == "ducks" or predicate[i] == "duck" or "duck" in predicate[i]:
            if "without" in  predicate[:i]:
                final_predicate = "noducks"
                return final_predicate
            else:
                final_predicate = "players_scored_duck"
                return final_predicate
        if predicate[i] == "strike":
            if len(predicate) > i+1:
                if predicate[i+1] == "rate":
                    if ("200" in predicate or "200." in predicate or "200.0" in predicate) and ("above" in predicate):
                        final_predicate = "srate_above200"
                        return final_predicate
                    elif (("100" in predicate) or ("100." in predicate) or "100.0" in predicate) and ("below" in predicate or "below." in predicate):
                        #print "predicate"
                        final_predicate = "strbelow100"
                        return final_predicate
        if predicate[i] == "more":
            if len(predicate) > i+3:
                if predicate[i+1] == "sixes" and predicate[i+2] == "than" and ("fours" in predicate[i+3]):
                    final_predicate = "gtsixthan4"
                    return final_predicate
        if predicate[i] == "boundary":
            final_predicate = "1boundary"
            return final_predicate
        if predicate[i] == "50":
            if len(predicate) > i+1:
                if "runs" in predicate[i+1]:
                    final_predicate = "gt50runs"
                    return final_predicate
        if predicate[i] == "1":
            if len(predicate) > i+1:
                if "wicket" in predicate[i+1]:
                    final_predicate = "atleast_1wicket"
                    return final_predicate
        if predicate[i] == "any":
            if len(predicate) > i+1:
                if "wicket" in predicate[i+1]:
                    if "failed" in predicate or ("not" in predicate[:i] and "did" in predicate[:i]):
                        final_predicate = "nowickets"
                        return final_predicate
        if predicate[i] == "7":
            if len(predicate) > i+1:
                if "overs" in predicate[i+1]:
                    final_predicate = "gt7overs"
                    return final_predicate
        if predicate[i] == "7overs":
            final_predicate = "gt7overs"
            return final_predicate
        if predicate[i] == "8":
            if len(predicate) > i+3:
                if predicate[i+1] == "runs" and predicate[i+2] == "per" and "over" in predicate[i+3]:
                    final_predicate = "8economy"
                    return final_predicate
        if predicate[i] == "scored":
            if len(predicate) > i+1:
                if "hundred" in predicate[i+1]:
                    final_predicate = "scorehundred"
                    return final_predicate
        if predicate[i] == "right":
            if len(predicate) > i+2:
                if "bowlers" in predicate[i+2]:
                    if "wickets" in predicate and ("left" in predicate and "bowlers" == predicate[predicate.index("left")+2]):
                        final_predicate = "rhb_bowlers_btlhb"
                        return final_predicate
        if predicate[i] == "26":
            if len(predicate) > i+2:
                if predicate[i+1] == "years" and predicate[i+2] == "old":
                    final_predicate = "lessthan26"
                    return final_predicate
        if predicate[i] == "250":
            if len(predicate) > i+1:
                if predicate[i+1] == "runs" and ("more" in predicate):
                    final_predicate = "gt250run"
                    return final_predicate
    return "nvalid"


def check_exists(predicate):
    for i in range(0,len(predicate)):
        if predicate[i]=="at" and predicate[i+1] == "least":
            return "exists"
        if predicate[i]=="there" and predicate[i+1] == "exists":
            return "exists"
    return "no"

def generate_query(final_predicate1,final_predicate2,connector_info,inside_quantifier):
    query = "notvalid"
    if connector_info == "if":
        query = inside_quantifier + " x (" + final_predicate1 + "(x) -> " + final_predicate2 + "(x))"
    elif connector_info == "given":
        query = inside_quantifier +" x (" + final_predicate1 + "(x) -> " + final_predicate2 + "(x))"
    elif connector_info == "and":
        query = inside_quantifier + " x (" + final_predicate1 + "(x) & " + final_predicate2 + "(x))"
    elif connector_info == "contains":
        query = inside_quantifier + " x (" + final_predicate1 + "(x) & " + final_predicate2 + "(x))"
    elif connector_info == "consists":
        query = inside_quantifier + " x (" + final_predicate1 + "(x) & " + final_predicate2 + "(x))"
    return query

def get_answer(val,gen_query):
    dom = val.domain
    m = nltk.Model(dom, val)
    g = nltk.Assignment(dom, [])
    result = m.evaluate(gen_query, g)
    return result

def print_answer(val,gen_query,ans,name_to_var):
  #  val = nltk.parse_valuation(v)
    dom = val.domain
    m = nltk.Model(dom, val)
    g = nltk.Assignment(dom, [])
    result = m.evaluate(gen_query, g)
    # to show the variable (corresponding to player names) for which "srate(x) -> gtsix(x) you can do
    if result:
        l = nltk.LogicParser()
        c1 = l.parse(gen_query)
        varnames =  m.satisfiers(c1, 'x', g)
        #print "varnames",
        #print varnames
        for i in varnames:
            #    print i
            for p,q in name_to_var.iteritems():   # naive method to get key given value, in a dictionary
                if q == i:
                    if p not in ans:
                        ans.insert(len(ans),p)
    return ans

def main():
    bats = {}
    bowl = {}
    player_match = {}
    win = {}
    profile = {}
    toss={}
    bat21 = './dataset/match2/odi2_inn1_bat.txt'
    bat22 = './dataset/match2/odi2_inn2_bat.txt'
    ball21 = './dataset/match2/odi2_inn1_bowl.txt'
    ball22 = './dataset/match2/odi2_inn2_bowl.txt'
    bat11 = './dataset/match1/odi1_inn1_bat.txt'
    bat12 = './dataset/match1/odi1_inn2_bat.txt'
    ball11 = './dataset/match1/odi1_inn1_bowl.txt'
    ball12 = './dataset/match1/odi1_inn2_bowl.txt'
    bat31 = './dataset/match3/odi3_inn1_bat.txt'
    bat32 = './dataset/match3/odi3_inn2_bat.txt'
    ball31 = './dataset/match3/odi3_inn1_bowl.txt'
    ball32 = './dataset/match3/odi3_inn2_bowl.txt'
    bat41 = './dataset/match4/odi4_inn1_bat.txt'
    bat42 = './dataset/match4/odi4_inn2_bat.txt'
    ball42 = './dataset/match4/odi4_inn2_bowl.txt'
    ball41 = './dataset/match4/odi4_inn1_bowl.txt'
    bat51 = './dataset/match5/odi5_inn1_bat.txt'
    bat52 = './dataset/match5/odi5_inn2_bat.txt'
    ball51 = './dataset/match5/odi5_inn1_bowl.txt'
    ball52 = './dataset/match5/odi5_inn2_bowl.txt'
    mom3 = './dataset/match3/mom.txt' 
    mom2 = './dataset/match2/mom.txt' 
    mom1 = './dataset/match1/mom.txt' 
    mom4 = './dataset/match4/mom.txt' 
    mom5 = './dataset/match5/mom.txt' 
    winning_1 = './dataset/match1/wonby.txt' 
    winning_2 = './dataset/match2/wonby.txt' 
    winning_3 = './dataset/match3/wonby.txt' 
    winning_4 = './dataset/match4/wonby.txt' 
    winning_5 = './dataset/match5/wonby.txt' 
    toss_5 = './dataset/match5/wontoss.txt' 
    toss_4 = './dataset/match4/wontoss.txt' 
    toss_3 = './dataset/match3/wontoss.txt' 
    toss_2 = './dataset/match2/wontoss.txt' 
    toss_1 = './dataset/match1/wontoss.txt' 
    profile1 = './dataset/player_profile/indian_players_profile.txt' 
    profile2 = './dataset/player_profile/nz_players_profile.txt' 
    add_to_dict(player_match,mom1);
    add_to_dict(player_match,mom2);
    add_to_dict(player_match,mom3);
    add_to_dict(player_match,mom4);
    add_to_dict(player_match,mom5);
    add_to_dict(win, winning_1)
    add_to_dict(win, winning_2)
    add_to_dict(win, winning_3)
    add_to_dict(win, winning_4)
    add_to_dict(win, winning_5)
    add_to_dict(toss,toss_5)
    add_to_dict(toss,toss_4)
    add_to_dict(toss,toss_3)
    add_to_dict(toss,toss_2)
    add_to_dict(toss,toss_1)
    add_to_dict_profile(profile,profile1);
    add_to_dict_profile(profile,profile2);
    model = []
    query = raw_input('Enter a query: ')
    list_words = query.split()
    index_quantifier = parse_for_quantifier_info(list_words)
    if index_quantifier == -1:
        print "Grammar not properly defined\n"
        return
    remain_info = list_words[index_quantifier+1:]
    index_connector = parse_for_connector_info(remain_info)
    global con4nector_info
    #print "wwwwwww\n"
    #print connector_info
    if index_connector == -1:
        print "Grammar not properly defined\n"
        return
    predicate1 = remain_info[:index_connector]
    predicate2 = remain_info[index_connector+1:]
    inside_quantifier = check_exists(predicate1)
    if inside_quantifier == "no":
        inside_quantifier = check_exists(predicate2)
    if inside_quantifier == "no":
        if "a" in predicate1:
            inside_quantifier = "exists"
    if inside_quantifier == "no":
        inside_quantifier = "all"
    final_predicate1 = find_predicate(predicate1)
    final_predicate2 = find_predicate(predicate2)
    if final_predicate1 == "nvalid" or final_predicate2 == "nvalid":
        print "Not valid predicates\n"
        return
    gen_query = generate_query(final_predicate1,final_predicate2,connector_info,inside_quantifier)
    if gen_query == "notvalid":
        print "Query is not valid\n"
        return
    ans=[]
    if quantifier_info == "for_match":
        c1=[]
        for i in range(1,6):
            count=0
            name_to_var = {}
            for j in profile:
                if j not in name_to_var:
                    name_to_var[j] = 'r' + str(count)
                    count += 1
            bats={}
            balls={}
            if i==1:
                add_to_dict(bats,bat11);
                add_to_dict(bats,bat12);
                add_to_dict(balls,ball12);
                add_to_dict(balls,ball11);
            elif i==2:
                add_to_dict(bats,bat21);
                add_to_dict(bats,bat22);
                add_to_dict(balls,ball22);
                add_to_dict(balls,ball21);
            elif i==3:
                add_to_dict(bats,bat31);
                add_to_dict(bats,bat32);
                add_to_dict(balls,ball32);
                add_to_dict(balls,ball31);
            elif i==4:
                add_to_dict(bats,bat41);
                add_to_dict(bats,bat42);
                add_to_dict(balls,ball41);
                add_to_dict(balls,ball42);
            elif i==5:
                add_to_dict(bats,bat51);
                add_to_dict(bats,bat52);
                add_to_dict(balls,ball51);
                add_to_dict(balls,ball52);
            model.insert(len(model),make_model(player_match[str(i)],win[str(i)],profile,bats,balls,c1))
            result = get_answer(model[i-1],gen_query)
            if result:
                indx = gen_query.index("(")
                var = gen_query[indx:]
                ans = print_answer(model[i-1],var,ans,name_to_var)
            else:
                print "False\n"
                return
        print ans
        return
    match=[]
    if quantifier_info == "exist_match":
        c1=[]
        flag=0
        for i in range(1,6):
            count=0
            name_to_var = {}
            for j in profile:
                if j not in name_to_var:
                    name_to_var[j] = 'r' + str(count)
                    count += 1
            bats={}
            balls={}
            if i==1:
                add_to_dict(bats,bat11);
                add_to_dict(bats,bat12);
                add_to_dict(balls,ball12);
                add_to_dict(balls,ball11);
            elif i==2:
                add_to_dict(bats,bat21);
                add_to_dict(bats,bat22);
                add_to_dict(balls,ball22);
                add_to_dict(balls,ball21);
            elif i==3:
                add_to_dict(bats,bat31);
                add_to_dict(bats,bat32);
                add_to_dict(balls,ball32);
                add_to_dict(balls,ball31);
            elif i==4:
                add_to_dict(bats,bat41);
                add_to_dict(bats,bat42);
                add_to_dict(balls,ball41);
                add_to_dict(balls,ball42);
            elif i==5:
                add_to_dict(bats,bat51);
                add_to_dict(bats,bat52);
                add_to_dict(balls,ball51);
                add_to_dict(balls,ball52);
            model.insert(len(model),make_model(player_match[str(i)],win[str(i)],profile,bats,balls,c1))
            result = get_answer(model[i-1],gen_query)
            if result:
                flag=1
                indx = gen_query.index("(")
                var = gen_query[indx:]
                ans = print_answer(model[i-1],var,ans,name_to_var)
                match.insert(len(match),i)
        if flag:
            print "players",
            print ans
            print "matches",
            print match
            return
        else:
            print "False\n"
    if quantifier_info == "innings":
        c1=[]
        for i in range(1,11):
            count=0
            name_to_var = {}
            for j in profile:
                if j not in name_to_var:
                    name_to_var[j] = 'r' + str(count)
                    count += 1
            bats={}
            balls={}
            if i==1:
                add_to_dict(bats,bat11);
                add_to_dict(balls,ball11);
            elif i==2:
                add_to_dict(bats,bat12);
                add_to_dict(balls,ball12);
            elif i == 3:
                add_to_dict(bats,bat21);
                add_to_dict(balls,ball21);
            elif i == 4:
                add_to_dict(bats,bat22);
                add_to_dict(balls,ball22);
            elif i==5:
                add_to_dict(bats,bat31);
                add_to_dict(balls,ball31);
            elif i == 6:
                add_to_dict(bats,bat32);
                add_to_dict(balls,ball32);
            elif i==7:
                add_to_dict(bats,bat41);
                add_to_dict(balls,ball41);
            elif i==8:
                add_to_dict(bats,bat42);
                add_to_dict(balls,ball42);
            elif i==9:
                add_to_dict(bats,bat51);
                add_to_dict(balls,ball51);
            elif i==10:
                add_to_dict(bats,bat52);
                add_to_dict(balls,ball52);
            model.insert(len(model),make_model(player_match[str(i)],win[str(i)],profile,bats,balls,c1))
            result = get_answer(model[i-1],gen_query)
            if result:
                indx = gen_query.index("(")
                var = gen_query[indx:]
                ans = print_answer(model[i-1],var,ans,name_to_var)
            else:
                print "False\n"
                return
        print ans
        return
    if quantifier_info == "player":
        if "same" in predicate2:
            inx = predicate2.index["same"]
            if "match" in predicate2[inx+1]:
                flag=0
                c1=[]
                for i in range(1,6):
                    count=0
                    name_to_var = {}
                    for j in profile:
                        if j not in name_to_var:
                            name_to_var[j] = 'r' + str(count)
                            count += 1
                        bats={}
                        balls={}
                        if i==1:
                            add_to_dict(bats,bat11);
                            add_to_dict(bats,bat12);
                            add_to_dict(balls,ball12);
                            add_to_dict(balls,ball11);
                        elif i==2:
                            add_to_dict(bats,bat21);
                            add_to_dict(bats,bat22);
                            add_to_dict(balls,ball22);
                            add_to_dict(balls,ball21);
                        elif i==3:
                            add_to_dict(bats,bat31);
                            add_to_dict(bats,bat32);
                            add_to_dict(balls,ball32);
                            add_to_dict(balls,ball31);
                        elif i==4:
                            add_to_dict(bats,bat41);
                            add_to_dict(bats,bat42);
                            add_to_dict(balls,ball41);
                            add_to_dict(balls,ball42);
                        elif i==5:
                            add_to_dict(bats,bat51);
                            add_to_dict(bats,bat52);
                            add_to_dict(balls,ball51);
                            add_to_dict(balls,ball52);
                        model.insert(len(model),make_model(player_match[str(i)],win[str(i)],profile,bats,balls,c1))
                        result = get_answer(model[i-1],gen_query)
                        if result:
                            flag=1
                            indx = gen_query.index("(")
                            var = gen_query[indx:]
                            ans = print_answer(model[i-1],var,ans,name_to_var)
                    if flag:         
                        print ans
                        return
                    else:
                        print "False\n"
        else:
            flag=0
            for i in range(0,len(predicate2)):
                if predicate2[i] == "any":
                    if len(predicate2) > i+2:
                        if "matches." in predicate2[i+1:]:
    			    bats1={}
    			    bats2={}
    		    	    bats3={}
		            bats4={}
    			    bats5={};balls1={};balls2={};balls3={};balls4={};balls5={}
    		            add_to_dict(bats1,bat11);add_to_dict(bats1,bat12);add_to_dict(bats2,bat21);
    			    add_to_dict(bats2,bat22);
    			    add_to_dict(bats3,bat31);
    			    add_to_dict(bats3,bat32);
    			    add_to_dict(bats4,bat41);
    			    add_to_dict(bats4,bat42);
			    add_to_dict(bats5,bat51);
    			    add_to_dict(bats5,bat52);
			    add_to_dict(balls1,ball12);
    			    add_to_dict(balls1,ball11);
    			    add_to_dict(balls2,ball22);
    			    add_to_dict(balls2,ball21);
    			    add_to_dict(balls3,ball32);
    			    add_to_dict(balls3,ball31);
    			    add_to_dict(balls4,ball41);
    			    add_to_dict(balls4,ball42);
    			    add_to_dict(balls5,ball51);
    			    add_to_dict(balls5,ball52);
			    c1 = parse_250run(bats1,bats2,bats3,bats4,bats5)
                            model.insert(len(model),make_model(player_match[str(i)],win[str(i)],profile,bats,balls,c1))
                            #model.insert(len(model),make_model(player_match[str(i)],win[str(i)],profile,bats,balls,c1))
                            result = get_answer(model[i-1],gen_query)
                            if result:
                                flag=1
                                indx = gen_query.index("(")
                                var = gen_query[indx:]
                                ans = print_answer(model[i-1],var,ans,name_to_var)
                        if flag:
                            print ans
                            return
                        else:
                            print "False\n"        


if __name__ == "__main__":
        main()
