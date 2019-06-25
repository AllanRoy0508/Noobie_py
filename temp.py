# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
d={11:"faheera",12:"treasa",13:"vicky"}
ch2='y'
g=0
f=0
while (ch2=='y'):
    ch= int (input ("Enter your choice:1.FEO 2.Manager 3.Owner:"))
    if(ch==1):
        pwd1=input ("Enter your password,FEO:")
        if (pwd1=='1234'):
            id=int (input ("Enter the ID to search"))
            for i in d:
                if (i==id):
                    print("The id is present")
                    f=1
            if(f==0):
            
                    print("Not found")
        else:
            print("Incorrect password")
    elif (ch==2):
            pwd1=input ("Enter your password,Manager:")
            if (pwd1=='4567'):
               id=int (input ("Enter the ID to search"))
               for i in d:
                   if (i==id):
                       print("The name is: "+d[i])
                       g=1
               if(g==0):
                       print("Invalid Id")
            else:
               print("Incorrect password")
    elif (ch==3):
            pwd1=input ("Enter your password,Owner:")
            if (pwd1=='7890'):
               ch1=int (input ("Choose to 1.delete 2.details"))
               if(ch1==1):
                   id= int (input ("Enter the id:"))
                   del d[id]
               elif (ch1==2):
                    id=int ("Enter id:")
                    print (d.get(id))
            else:
                print("Invalid password")
    else:
        print("Invalid choice")
ch2= (input ("Enter y to continue"))
               
               
               

   