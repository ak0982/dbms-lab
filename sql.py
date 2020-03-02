#with open('input.txt','r') as f:
f = open('dept.txt','r') 
ff = open('deptsql.txt','w')
for line in f:
     cl = line.split(",")
     #if cl[2] =="R128":
#	print(cl[0])     
    # ff.write("("+cl[0]+","+cl[1]+","+cl[2]+"),"+"\n")
     ff.write("("+cl[0]+","+"'"+cl[1]+"'"+","+cl[2]+","+cl[3]+"),"+"\n")


f.close()
ff.close()
