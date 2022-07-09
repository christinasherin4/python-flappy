# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 06:40:21 2022

@author: Christina sherin
"""

f=open("C:\\Users\\ASUS\\Desktop\\file.txt", "r")
data_types=["int", "float", "char", "double", "short", "long"]
d_types=[]
stack=[]
identifiers=[]
initial_values = []
return_type = []
type_of_parameters = []
parameters_count=[]
while f:
 input=f.readline().rstrip("\n")
 if(input==""):
  break
 else:
  for i in range(len(input)):
   if(input[i] == " " and input[i+1]!="," and input[i+1]!="=" and input[i-1]!="="and input[i+1]!=";"):
    if("".join(stack) in data_types):
     for j in range(len(input[i+1:len(input)].split(","))):
      d_types.append("".join(stack))
      stack.clear()
    elif(input[i]=="," or input[i]==";"):
     if("".join(stack).find("=")!=-1):

      if(d_types[len(d_types)-1]=="char"):
       initial_values.append(''.join(stack).split("=")[1])
     elif(d_types[len(d_types)-1]=="float"):
      initial_values.append(''.join(stack).split("=")[1])
     elif(d_types[len(d_types)-1]=="int"):
      initial_values.append(''.join(stack).split("=")[1])
     else:
       initial_values.append("".join(stack).split("=")[1])
       identifiers.append("".join(stack).split("=")[0])
       type_of_parameters.append("-")
       parameters_count.append("-")
       return_type.append("-")
       stack.clear()
   else:
     if(d_types[len(d_types)-1] == "int"):
        identifiers.append("".join(stack))
        type_of_parameters.append("-")
        parameters_count.append("-")
        return_type.append("-")
        initial_values.append(0)
     elif(d_types[len(d_types)-1] == "float"):
         identifiers.append("".join(stack))
         type_of_parameters.append("-")
         parameters_count.append("-")
         return_type.append("-")
         initial_values.append(0.0)
     elif(d_types[len(d_types)-1] == "char"):

         identifiers.append("".join(stack))
         type_of_parameters.append("-")
         parameters_count.append("-")
         return_type.append("-")
         initial_values.append("-")
         stack.clear()
     elif(input.find("(")>0 and input.find(")")>0):
        k=input.find("(")
        m=input.find(")")
        d_types.append("-")
        initial_values.append("-")
        return_type.append(input[:k].split(" ")[0])
        identifiers.append(input[:k].split(" ")[1])
        parameters_count.append(len(input[k:].split(",")))
        empty = []
        for item in input[k+1:len(input)-1].split(","):
          b=item.strip().split(" ")
          empty.append(b[0])
        type_of_parameters.append(empty)
        break
     elif(input[i]!=""):
       stack.append(input[i])
       print(input)
       f.close()
       print("\nSymbol Table: \n")
       print("ID\t\t\tData Type\t\tReturn Type\t\tInitial Value\t\t\tNo. of Parameters\tType of Parameters")
     for i in range(len(identifiers)):

       print(str(identifiers[i])+"\t\t\t"+str(d_types[i])+"\t\t\t\t"+str(return_type[i])+"\t\t\t\t\t"
+str(initial_values[i])+"\t\t\t\t\t\t"+str(parameters_count[i])+"\t\t\t\t\t\t"+str(type_of_parameters[i]))