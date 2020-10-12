#Srinivas Rao Kuthyar 11 Oct 20
#WORD GAME VERSION 1.0
#Doesn't include timer
#TO INCLUDE SCORE ON TOP
#Not YET programmed for length of Computer word to be around same as Length of User input
#Tested with Upper case
def wordgame5():
    import random
    import sys
    f1=open('wordlist.txt','r')
    user_word=[]
    last_letter=[]
    comp_word=[""]
    user_word=[""]
    rep_word=[]
    rep=[]
    sm1="Comp's chance:"
    sm2="User's chance: "
    sm3="Word already used. Computer wins"
    sm4="Start letter doesn't match end letter. Computer wins"
    sm5="User has won the game"
    def read(f1):
        with f1 as file:
            comp_dict=[line.rstrip() for line in file]
        return comp_dict

    def compare1(comp_input,user_input):
        len1=len(comp_input)
        len2=len(user_input)
        last_letter_comp=comp_input[len1-1::].lower()
        first_letter_user=user_input[0:1].lower()

        if(first_letter_user==last_letter_comp):
            last_letter_user=user_input[len2-1::].lower()
            return last_letter_user
        else:
            return 0
     
    def compare2(user_input,user_word,comp_word):
        user_input=user_input.lower()
        len1=len(user_word)
        len2=len(comp_word)
        count=0
        for i in range(0,len1,1):
            if(user_input==user_word[i].lower()):
                return 0
                break
            else:
                count=count+1
                if(count==len1):
                    count=0
                    for i in range(0,len2,1):
                        if(user_input==comp_word[i].lower()):
                            return 0
                            break
                        else:
                            count=count+1
                            if(count==len2):
                                return 1

    def getword(last_letter,words,rep):
        
        a=0
        b=0
        len2=len(words)
        len3=len(rep)
        count=0
        count_rep=0        
        for i in range(0,len2,1):
            first_letter=words[i][0:1]
            
            if(last_letter==first_letter):
                count_rep=0
                for j in range(0,len3,1):
                    if(words[i]==rep[j]):
                        count=count+1
                        break
                    else:
                        count_rep=count_rep+1
                        if(count_rep==len3):
                            a=i
                            b=1
                            break
            else:
                count=count+1

              
            if count==len2-1:
                b=0
                break
            if(b):
                break
        
        if(b):
            return(words[a])
        else:
            return 0
    comp_dict=read(f1)
    start_word_index=random.randint(1,20)
    start_word=comp_dict[start_word_index]
    comp_word.append(start_word)
    print(sm1,start_word)
    while(1):
        
        user_input=input(sm2)

        last_letter_user=compare1(comp_word[len(comp_word)-1],user_input)
        
        if(last_letter_user):
            return1=compare2(user_input,user_word,comp_word)
            
            if(return1):
                user_word.append(user_input)
                rep.append(user_input)
                
                comp_input=getword(last_letter_user,comp_dict,rep)
                if(comp_input==0):
                    print(sm5)
                    sys.exit()
                else:
                    comp_word.append(comp_input)
                    rep.append(comp_input)
                    print(sm1,comp_input)
                
                   
            else:
                print(sm3)
                break
                
        else:
            print(sm4)
            break
wordgame5()
      



