#!/usr/bin/env python3

'''
    // Program Name: gs1.py
    // Created by: Alejo Pijuan
    // Date: 10/12/18
    // PURPOSE: Implementing Gale-Shapley algorithm
    // INPUT(S): 500-5000 (men and women)
    // OUTPUT(S): Time taken to create every stable pair
'''
import getopt
import random
import sys
import time


def CreatePeople(Userinput):
    
#    Accepts :input from user
#    Returns :lists of men and women
    
    Men = []
    Women = []
    for num in range(Userinput):
        Men.append("M"+str(num))
        Women.append("W"+str(num))
    return Men, Women




def MakePrefer(Men, Women, amount):
    
#    Accepts:list of men, women, and amount of people involved
#    Returns:dictionary containing preferences
    
    for eachMan in Men:
        pref[eachMan] = [0,1]
        Makesingle(eachMan)
        tempWomen = Women[0:]
        for i in range(int(amount)):
            RandInd = random.randrange(int(amount)-i)
            pref[eachMan].append(tempWomen.pop(RandInd))

    for eachWoman in Women:
        pref[eachWoman] = [0,1]
        Makesingle(eachWoman)
        tempMen = Men[0:]
        for i in range(int(amount)):
            RandInd = random.randrange(int(amount)-i)
            pref[eachWoman].append(tempMen.pop(RandInd))

def Alone(possiblePartner):

#    Accepts: The name of the person to check for.
#    Return: True if lonely False if not lonely.

    if pref[possiblePartner][0] == 'lonely':
        return True
    else:   
        return False

def Makesingle(ManOrWoman):


#    Accepts: the name of the person who get dumped
#    Return: none
 
    pref[ManOrWoman][0] = 'lonely'

def MakeEngaged(ManOrWoman):

#    Accepts: the name of the person who successfully proposed
#    Return: none

    pref[ManOrWoman][0] = 'engaged'

def ManProposes(man, possiblePartner):

#    Accepts:name of the person who proposes, name of the person who is proposed
  #  Returns:None

    if(Alone(possiblePartner)):
        Engagement(man, possiblePartner)
    else:
        if(TradeForBetter(man, possiblePartner)):
            DeEngage(possiblePartner)
            Engagement(man, possiblePartner)

def Engagement(ManOrWoman, possiblePartner):

#    Accepts: name of the person who proposes successfully and proposed
#    Returns: None

    pref[ManOrWoman][1] = RankNumber(ManOrWoman, possiblePartner)
    pref[possiblePartner][1] = RankNumber(possiblePartner, ManOrWoman)
    MakeEngaged(ManOrWoman)
    MakeEngaged(possiblePartner)

def candidate(ManOrWoman):

 #   Accepts: name of a person
#    Returns: name of the person who is a target for proposal

    pref[ManOrWoman][1] += 1
    index = pref[ManOrWoman][1]
    return pref[ManOrWoman][index]

def partner(ManOrWoman):

#    Accepts: name of a person
#    Returns: name of the partner of the person
 
    index = pref[ManOrWoman][1]
    return pref[ManOrWoman][index]

def TradeForBetter(ManOrWoman, possiblePartner):

#    Accepts: name of a person and the target of that person
#    Returns: Boolean if can trade up or not

    ranked = RankNumber(possiblePartner, ManOrWoman)
    candidateRank = RankNumber(possiblePartner, partner(possiblePartner))
    if ranked < candidateRank :
        return True
    else:
        return False

def DeEngage(possiblePartner):

#    Accepts: name of a person who dumps
#    Returns: None
 
    Makesingle(partner(possiblePartner))

def RankNumber(ManOrWoman, possiblePartner):

#    Accepts: person and a canidate
 #   Returns: the rank of first on the other's preference list.

    return pref[ManOrWoman].index(possiblePartner)

def ShowPref():

#    Print the pref for each person
#    Accepts: None
#    Returns: None

    print("Preferences: ")
    for ManOrWoman in pref:
        print("{:<4}".format(ManOrWoman),end=": ")
        for each in pref[ManOrWoman][2:]:
            print("{: <5}".format(each),end="")
        print()

def ShowEverybody():
 
#    Print list of suitors and girls
#    Accepts: None
 #   Returns: None

    print("Participants: ")
    for each in MenList:
        print("{: <5}".format(each),end="")
    print()
    for each in WomenList:
        print("{: <5}".format(each),end="")
    print("\n")

def ShowPair():
    print("Pairing:")
    for each in MenList:
        print("{:>4} - {:<4}".format(each,partner(each)))

def PairUp():
    pairing_complete = False
    while (not pairing_complete):
        pairing_complete = True
        for person in MenList:
            if(Alone(person)):
                pairing_complete = False
                possiblePartner = candidate(person)
                ManProposes(person, possiblePartner)

def main(argv):
    time.clock()
    global MenList, WomenList, pref
    MenList, WomenList = CreatePeople(int(argv))
    pref = dict()
    start = time.time()
    MakePrefer(MenList, WomenList, argv)
    PairUp()
    end = time.time()
    wall_clock = time.clock()

    print("{:>6}\t{:.6f}".format(argv, end-start))

if __name__ == "__main__":
   main(sys.argv[1])
