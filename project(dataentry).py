#please check out why we get error when we write something like:e1=Entry(m).grid(row=0,column=1)

from Tkinter import *

#dbms section# 



import MySQLdb
db=MySQLdb.connect(host="localhost",user="root",passwd="febe",db="test2")
cursor=db.cursor()
#cursor.execute("select * from users4")
#data=cursor.fetchall()
#print(data)
#try:
    
 #   cursor.execute("select * from users4")
  #  data=cursor.fetchall()
   # print(type(data[0]))
  #  for row in data:
   #     print(row[0]+"          "+row[1]+"          "+row[2]+"          "+row[3]+"          "+row[4])
        
    #print(data)
#except:
    #print("sorry")








#GUI section#
def get_data():
	try:
		print("first name=%s" %(e1.get()))
		
		cursor.execute("insert into entered_user(name,age,sex,phoneno,mail_id,patient_id) values('%s','%s','%s','%s','%s','%s')"% (e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get())) 
	except:
		print("sorry")
	db.commit()
	db.close()

	
m=Tk()
Label(m,text="please enter your data").grid(row=0,column=1)
Label(m,text="name:").grid(row=1)
Label(m,text="age:").grid(row=2)
Label(m,text="sex:").grid(row=3)
Label(m,text="phone no:").grid(row=4)
Label(m,text="mail id:").grid(row=5)
Label(m,text="patient id:").grid(row=6)


e1=Entry(m)
e1.grid(row=1,column=1)
e2=Entry(m)
e2.grid(row=2,column=1)
e3=Entry(m)
e3.grid(row=3,column=1)
e4=Entry(m)
e4.grid(row=4,column=1)
e5=Entry(m)
e5.grid(row=5,column=1)
e6=Entry(m)
e6.grid(row=6,column=1)

Button(m,text="enter",command=get_data).grid(row=7,column=1)



mainloop() 