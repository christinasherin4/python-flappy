# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 07:27:38 2022

@author: christina sherin
@regno:URK19CS1063
"""
print("...............................................")
print("Name:L.CHRISTINA SHERIN")
print("Name:URK19CS1063")
print("................................................")
l=input("Enter the reference in a single line ")
l1=l.split()
k_list=['False', 'None', 'True', 'and', 'as', 'end','assert', 'async','await',
'break', 'class', 'continue', 'def', 'del', 'elif','int','float','str','char',
'else', 'except', 'finally', 'for', 'from', 'global','if', 'import', 'in', 'is',
'lambda','nonlocal', 'not', 'or', 'pass', 'raise','return', 'try', 'while',
'with', 'yield']
op_list=['+','-','*','/','%','**','//','=','+=','-=','*=','/=','%=','//','**','&=','|=','**=','&=','|=','^=','>>=','<<=','==','!=','>','<','>=','<=']
p_list=['!',' " ',' # ',' $', ',','%','&',';'," ' " ,'( ',')',' *', '+' ,' -','.', "/", ":"," ;", "<","=", " >"," ?" ,"@ ","[","\ ","]", "^","_","`","{","|","}","~" ]
num_list= list(range(1,999999))
num_list2=str(num_list)
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
for i in l1:
    if i in k_list:
        print("< ",i,", keyword >")
        count1+=1
    elif i in op_list:
        if i=="=":
            print("< ",i,", arithmetic or assignment operator >")
            count2=count2+1
        if i=="<=" or i== ">=":
            print("< ", i, ",relational operator >")
            count3=count3+1
    elif i in p_list:
        print("< ",i,", punctuation >")
        count4=count4+1
    elif i in num_list2:
        print("< ", i, ", number>")
        count5=count5+1
    else:
        count6=count6+1
        print("< ", i, ", identifier id-",count6,">")
count=count1+count2+count3+count4+count5+count6
print("The total no .of token(s) is/are: ",count)

