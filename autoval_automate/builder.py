from itertools import *
import os
from os import listdir
from os.path import isfile, join
import json



#get golden and student directory path
golden_solution_path = os.getcwd() + "/golden_solution"
student_solutions_path = os.getcwd() + "/student_solution"


# Get the golden solution filename
golden_solution_filenames = [f for f in listdir(golden_solution_path) if isfile(join(golden_solution_path, f))]
golden_solution_filename = golden_solution_filenames[0]

# Get the student solutions filenames
student_solution_filenames = [f for f in listdir(student_solutions_path) if isfile(join(student_solutions_path, f))]


# Parse golden solution
golden_solution_file = open(golden_solution_path + "/" + golden_solution_filename,"r")
golden_code = golden_solution_file.read()

#main method creation
f=open('template.json')
data=json.load(f)

main_method_file=open("temp1.py","w+")
main_method_file.write("from itertools import *\n"+"import numpy as np\n")
main_method_file.write("def char_range(c1, c2):\n\tfor c in range(ord(c1), ord(c2)+1):\n\t\tyield chr(c)\n")
main_method_file.write("def checker():\n")
main_method_file.write("\tcheck_equal=True\n")
char_loop='a'
temp_String=""
indenter=1
parameter=0
n="\t"*indenter
indenter+=1

for x in data["inputParams"]:
    if(x["type"]=="int"):
        char_loop=char_loop+str(parameter)
        main_method_file.write(n+"for "+char_loop+" in range("+str(x["lower_limit"])+","+str(x["upper_limit"])+"):\n")
        temp_String=temp_String+char_loop+","
        char_loop='a'
        
        
    elif(x["type"]=="char"):
        char_loop=char_loop+str(parameter)
        main_method_file.write(n+"for "+char_loop+" in char_range("+"\'"+str(x["lower_limit"])+"\',"+"\'"+str(x["upper_limit"])+"\'):\n")
        temp_String=temp_String+char_loop+","
        char_loop='a'
        
        
    elif(x["type"]=="float"):
        char_loop=char_loop+str(parameter)
        main_method_file.write(n+"for "+char_loop+" in np.arange("+str(x["lower_limit"])+","+str(x["upper_limit"])+","+str(x["increment"])+"):\n")
        temp_String=temp_String+char_loop+","
        char_loop='a'
        
    parameter+=1
    n="\t"*indenter
    indenter+=1
if("arrayParams" in data):
    k=0
    parameter_String='j'
    for i in range(len(data["arrayParams"])):
        x=data["arrayParams"]
        low=x[k]["lower_limit"]
        up=x[k]["upper_limit"] 
        len_arr=x[k]["length"]
        main_method_file.write(n+"for "+str(parameter_String)+" in "+"list(map(list,(permutations(range("+str(low)+","+str(up)+"),"+str(len_arr)+")))):\n")
        temp_String+=parameter_String+","
        parameter_String = chr(ord(parameter_String) + 1)
        k=k+1
        n="\t"*indenter
        indenter+=1
temp_String=temp_String[:-1]
n="\t"*indenter
indenter=indenter+1
main_method_file.write(n+"if (golden_solution("+temp_String+")!=student_solution("+temp_String+")):\n")
n="\t"*indenter
indenter=indenter+1
main_method_file.write(n+"check_equal=False\n")
main_method_file.write(n+"print("+"\""+"\\\"Solution by student is wrong on case:"+"\",end=\" \")\n")
main_method_file.write(n+"print("+temp_String+",end=\" \")\n")
main_method_file.write(n+"print(\"\\\"},"+"\")\n")
main_method_file.write(n+"return 0\n")
main_method_file.write("\tif(check_equal==True):\n")
main_method_file.write("\t\tprint("+"\""+"\\\"Solution by student is correct"+"\\\"},\""+")\n")
main_method_file.write("checker()")
main_method_file.close()    


main_method_file=open("temp1.py","r")

main_method_code = main_method_file.read()

#opening json file
with open("op.json","a") as f:  
        f.write("[")
        f.write("\n")
for x in student_solution_filenames:

    print("Running on " + x)    
    student_solution_file = open(student_solutions_path + "/" + x,"r")
    student_code = student_solution_file.read()
    
    temp_file = open("temp1.py","w")
    temp_file.write("#Beginning of Golden Solution\n")
    temp_file.write(golden_code)
    temp_file.write("\n#End of Golden Solution\n")
    temp_file.write("#Beginning of Student Solution\n")
    temp_file.write(student_code)
    temp_file.write("\n#End of Student Solution\n\n\n\n\n")
    temp_file.write("#Beginning of main method\n")
    temp_file.write(main_method_code)
    temp_file.write("\n#End of main method\n\n\n\n\n")
    temp_file.close()
    student_id=x[:-3]
   
    with open("op.json","a") as f:
        f.write("{\""+student_id+"\": ")

    command ="python temp1.py >> op.json"
    os.system(command)
for i in range(3):
    with open("op.json", 'rb+') as filehandle:
        filehandle.seek(-1, os.SEEK_END)
        filehandle.truncate()
   
with open("op.json","a") as f: 
    f.write("\n") 
    f.write("]")

        


    
    

