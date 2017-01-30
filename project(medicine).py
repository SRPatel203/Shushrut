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
		
		cursor.execute("insert into medicines(disease,medicine,price) values('%s','%s','%s')"% (e1.get(),e2.get(),e3.get())) 
	except:
		print("sorry")
	db.commit()
	#e1.delete(0,END)
	#e2.delete(0,END)
	#e3.delete(0,END)
	#e4.delete(0,END)
	#e5.delete(0,END)
	#e6.delete(0,END)
	return 0
	#db.close()
m=Tk()
while(1):	
        
        Label(m,text="please enter medicine data").grid(row=0,column=1)
        Label(m,text="disease:").grid(row=1)
        Label(m,text="medicine:").grid(row=2)
        Label(m,text="price:").grid(row=3)
        #Label(m,text="address:").grid(row=4)
        #Label(m,text="specialization:").grid(row=5)
        #Label(m,text="Doctor_id:").grid(row=6)


        e1=Entry(m)
        e1.grid(row=1,column=1)
        e2=Entry(m)
        e2.grid(row=2,column=1)
        e3=Entry(m)
        e3.grid(row=3,column=1)
        #e4=Entry(m)
        #e4.grid(row=4,column=1)
        #e5=Entry(m)
        #e5.grid(row=5,column=1)
        #e6=Entry(m)
        #e6.grid(row=6,column=1)

        Button(m,text="enter",command=get_data).grid(row=7,column=1)



	mainloop() 
