#somehow take those curly braces out!!!#
from Tkinter import *
import MySQLdb
#from PIL import ImageTk, Image

class program:
#----------------------------------------------------------------------------------------------#
	#constructor#
	def __init__(self,m):
		self.m=m
		self.l=[]
		self.n=0
		self.db=MySQLdb.connect(host="localhost",user="root",passwd="febe",db="test2")
		self.cursor=self.db.cursor()
	#ends here#	
#-----------------------------------------------------------------------------------------------#	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
#------------------------------------------------------------------------------------------------#	
	#function for pressing first no#
	def firstno(self,n,f,f2):
		f.destroy()
		f2.destroy()
		frame2=Frame(self.m,relief=RAISED,borderwidth=10,bg="blue")
		frame2.pack(side=BOTTOM,expand=True,fill="both",padx=5)
		frame=Frame(self.m,bg="blue",relief=RAISED,borderwidth=10)
		frame.pack(side=TOP, anchor=N, padx=5, pady=70,expand=True,fill="both")
		del self.l[:]
		print("n at last="+n)
		
		
		
		Label(frame,text="Sorry,Shushrut couldn't figure out the exact disease",width=40,font=("bold",20)).pack()
		b="a"
		if(n=="Rashes"):
			b="Skin Dermatologist"
		elif(n=="Stomach" and s1[0]=="Hammoroids"):
			b="Surgery"
		elif(n=="Bone"):
			b="Orthopedics"
		elif(n=="ENT"):
			b="ENT"
		else:
			b="General medicine"
		
		#changing here
		Button(frame2,text="Next",command=lambda:self.docdetails(b,frame,frame2),font=("bold",20),width=20).pack(side=BOTTOM)
		#ends
		'''
		self.cursor.execute("select * from doctor_table where specialization='%s'"%b)
		s3=self.cursor.fetchall()
			
		Label(frame,text="For better treatment and guidance for your category of disease, please consult:").pack(side=TOP)
		for i in s3:
			for j in i:
				Label(frame,text=j).pack(side=TOP)
			print()
			'''
	#ends here
#-------------------------------------------------------------------------------------------------#	













#--------------------------------------------------------------------------------------------------#	
	def docleveln(self,s1,n,f,f2):
		f.destroy()
		f2.destroy()
		frame2=Frame(self.m,relief=RAISED,borderwidth=10,bg="blue")
		frame2.pack(side=BOTTOM,expand=True,fill="both",padx=5)
		frame=Frame(self.m,bg="blue",relief=RAISED,borderwidth=10)
		frame.pack(side=TOP, anchor=N, padx=5, pady=70,expand=True,fill="both")
		del self.l[:]
		print("n at last="+n)
		
		
		Label(frame,text="Sorry,Shushrut couldn't figure out the exact disease",font=("bold",20),width=40).pack()
		#changing here
		#Button(frame2,text="Ok",command=lambda:self.create1(n,frame,frame2),width=40,font=("bold",20)).pack(side=BOTTOM)
		#ends

		b="a"
		if(n=="Rashes"):
			b="Skin Dermatologist"
		elif(n=="Stomach" and s1[0]=="Hammoroids"):
			b="Surgery"
		elif(n=="Bone"):
			b="Orthopedics"
		elif(n=="ENT"):
			b="ENT"
		else:
			b="General medicine"
		
		Button(frame2,text="Next",command=lambda:self.docdetails(b,frame,frame2),font=("bold",20),width=20).pack(side=BOTTOM)
		#self.cursor.execute("select * from doctor_table where specialization='%s'"%b)
		#s3=self.cursor.fetchall()
			
		#Label(frame,text="For better treatment and guidance please consult:").pack(side=TOP)
		#for i in s3:
		#	for j in i:
		#		Label(frame,text=j).pack(side=TOP)
		#	print()

			
			
#------------------------------------------------------------------------------------------------#

	'''def printed(self,v,s3,f,f2):
		f.destroy()
		f2.destroy()
		frame2=Frame(self.m,relief=RAISED,borderwidth=10,bg="blue")
		frame2.pack(side=BOTTOM,expand=True,fill="both",padx=5)
		frame=Frame(self.m,bg="blue",relief=RAISED,borderwidth=10)
		frame.pack(side=TOP, anchor=N, padx=5, pady=70,expand=True,fill="both")
		num=s3
		b1=Button(frame2,text="Next",font=("bold",20))	
		h=0
		while(h<s3.row_count()):
			b1.bind('<Button-1>',h=h+1)'''
			
	
		
#

	def docdetails(self,b,f,f2):
		f.destroy()
		f2.destroy()
		frame2=Frame(self.m,relief=RAISED,borderwidth=10,bg="blue")
		frame2.pack(side=BOTTOM,expand=True,fill="both",padx=5)
		frame=Frame(self.m,bg="blue",relief=RAISED,borderwidth=10)
		frame.pack(side=TOP, anchor=N, padx=5, pady=70,expand=True,fill="both")
		del self.l[:]
		print("n at last="+b)#for debugging#
		v=0
		#v=0
		Label(frame,text="Please Consult:",width=20,font=("bold",30)).pack(side=TOP)
		self.cursor.execute("select * from doctor_table where specialization='%s'"%b)
		s3=self.cursor.fetchall()
		b1=Button(frame2,text="Next",font=("bold",20))	
		#b1.bind('<Button-1>',v=self.printed(v,s3,frame,frame2))
		
		#Label(frame,text="please consult:",font=("bold",20)).pack(side=TOP)
		scrollbar = Scrollbar(frame)
		scrollbar.pack(side=RIGHT)

		listbox = Listbox(frame,bg="blue",font=("bold",20))
		listbox.pack(side=TOP,expand=True,fill="both")
		
		listbox.config(yscrollcommand=scrollbar.set)
		scrollbar.config(command=listbox.yview)

		
		print(s3)
		d=1
		listbox.insert(END,"")
		for v in s3:
			#listbox(frame,text="",font=("bold",20),bg="blue").pack()
			listbox.insert(END,"name="+v[0])
			#listbox(END,text="",font=("bold",20),bg="blue").pack()
			listbox.itemconfig(d,bg="white",fg="red")
			print(d)
			d=d+2
			listbox.insert(END,"")
			listbox.insert(END,"phone_no="+v[1])
			#	Label(frame,text="",font=("bold",20),bg="blue").pack()
			listbox.insert(END,"")
			listbox.itemconfig(d,bg="white")
			print(d*6+3)
			d=d+2
			listbox.insert(END,"mail_id="+v[2])
			listbox.insert(END,"")
			print(d*6+5)
			
			listbox.itemconfig(d,bg="white")
			d=d+2
			listbox.insert(END,"address="+v[3])
			print(d*6+7)
			#listbox.insert(END,"phone_no="+v[4])
			listbox.insert(END,"")
			listbox.itemconfig(d,bg="white")
			d=d+2
			listbox.insert(END,"specialization="+v[4])
			listbox.insert(END,"")
			print(d*6+9)
			listbox.itemconfig(d,bg="white")
			d=d+2
			listbox.insert(END,"doctor_id="+v[5])
			listbox.insert(END,"")
			listbox.itemconfig(d,bg="white")
			d=d+2
			print(d*6+11)
			#listbox.insert(END,"__________________________________________________________________________")
			
		Button(frame2,text="Ok",command=lambda:self.create1('b',frame,frame2),font=("blue",20),width=40).pack(side=BOTTOM)






#------------------------------------------------------------------------------------------------#
	#function for pressing "yes"
	def doclevely(self,s1,n,f,f2):
		print("IN MEDICIMES")
		#--------------------------------------------------#
		k=0
		f.destroy()
		f2.destroy()
		frame2=Frame(self.m,relief=RAISED,borderwidth=10,bg="blue")
		frame2.pack(side=BOTTOM,expand=True,fill="both",padx=5)
		frame=Frame(self.m,bg="blue",relief=RAISED,borderwidth=10)
		frame.pack(side=TOP, anchor=N, padx=5, pady=70,expand=True,fill="both")
		del self.l[:]
		#--------------------------------------------------#
		
		
		b="a"
		print("n at last="+n)#for debugging#
		#changing here
				#ends
		c="select dname from %s where s2='%s';" %(n,s1[0])
		self.cursor.execute(c)
		s2=self.cursor.fetchone()
		Label(frame,text="Most probably,the disease is:"+s2[0],font=("bold",20),width=40,fg="red").pack(side=TOP)
		Label(frame,text="",font=("bold",20),bg="blue").pack()
		#changing here
		print("the disease is"+s2[0])
		x=s2[0]
		if x=="Hammoroids":
			x="Piles"
		h="select medicine from medicines where disease='%s';"%(x)
		self.cursor.execute(h)
		tt=self.cursor.fetchall()
		Label(frame,text="Medicines that could be taken:-",font=("bold",20),width=40).pack(side=TOP)
		Label(frame,text="",font=("bold",20),bg="blue").pack()
		for i in range(self.cursor.rowcount):
			Label(frame,text=tt[i],font=("bold",20),width=40).pack(side=TOP)
			Label(frame,text="",font=("bold",20),bg="blue").pack()
		#ends
		
		if(n=="Rashes"):
			b="Skin Dermatologist"
		elif(n=="Stomach" and s2[0]=="Hammoroids"):
			b="Surgery"
		elif(n=="Bone"):
			b="Orthopedics"
		elif(n=="ENT"):
			b="ENT"
		else:
			b="General medicine"
		Button(frame2,text="Next",command=lambda:self.docdetails(b,frame,frame2),font=("bold",20),width=20).pack(side=BOTTOM)

		#self.docdetails(b,frame,frame2)
		#self.cursor.execute("select * from doctor_table where specialization='%s'"%b)
		#s3=self.cursor.fetchall()
			
		#Label(frame,text="please consult:",font=("bold",20)).pack(side=TOP)
		#for i in s3:
		#	for j in i:
		#		Label(frame,text=j,font=("bold",20)).pack(side=TOP)
	#		print()
			
#------------------------------------------------------------------------------------------------










#------------------------------------------------------------------------------------------------
	def lvl2(self,ss1,n,f,f2):
		k=0
		f.destroy()
		f2.destroy()
		frame2=Frame(self.m,relief=RAISED,borderwidth=10,bg="blue")
		frame2.pack(side=BOTTOM,expand=True,fill="both",padx=5)
		frame=Frame(self.m,bg="blue",relief=RAISED,borderwidth=10)
		frame.pack(side=TOP, anchor=N, padx=5, pady=70,expand=True,fill="both")
		Label(frame,text="Are these the other Symptoms?",font=("bold",30),width=40).pack(side=TOP)
		del self.l[:]
		print("type======")
		print(ss1)
		#changing here
		Button(frame2,text="Back",command=lambda:self.category(n,frame,frame2),width=20,font=("bold",20)).pack(side=BOTTOM)
		#ends
		d=(n,ss1)
		c="select s2,s3,s4,s5 from %s where s1='%s';"% (n,ss1[0])
		self.cursor.execute(c)
		s2=self.cursor.fetchone()
		for i in s2:
			self.l.append(Label(frame,text=i,font=("bold",20),width=40))
			k=k+1
		Label(frame,text="",font=("bold",20),bg="blue").pack()
		for i in range(k):
			self.l[i].pack(side=TOP)
			Label(frame,text="",font=("bold",20),bg="blue").pack()
		Button(frame2,text="Yes",width=20,command=lambda:self.doclevely(s2,n,frame,frame2),font=("bold",20)).pack(side=LEFT)
		Button(frame2,text="No",width=20,command=lambda:self.docleveln(s2,n,frame,frame2),font=("bold",20)).pack(side=RIGHT)
			
		print("Reached")
#ends here#
#-----------------------------------------------------------------------------------------------#	





















#------------------------------------------------------------------------------------------------#	
	#categorization#
	def category(self,n,f,f2):
		f.destroy()
		f2.destroy()
		
		
		frame=Frame(self.m,bg="blue",relief=RAISED,borderwidth=10)
		frame.pack(side=TOP, anchor=N, padx=5, pady=70,expand=True,fill="both")
		frame2=Frame(self.m,relief=RAISED,borderwidth=10,bg="blue")
		frame2.pack(side=BOTTOM,expand=True,fill="both",padx=5)
		k=0
		del self.l[:]
		print("in ENT")
		print(n)
		ss1=n;
		g=IntVar()
		
		Label(frame2,text="",font=("bold",20),bg="blue").pack()
		
		
		try:
			c="select s1 from %s"% n
			self.cursor.execute(c)
		except:
			print("sorry")
		s1=self.cursor.fetchall()
		print("$$$$$")
		print(s1[0][0])
		#changing here
		Label(frame,text="How are you feeling?",font=("bold",40)).pack(side=TOP)
		#Label(frame,text=" ",font=("bold",20),bg="blue").pack(side=TOP)
		
		Button(frame2,text="None",command=lambda:self.firstno(n,frame,frame2),width=10,font=("bold",20)).pack(side=LEFT)
		Button(frame2,text="Back",command=lambda:self.create1(n,frame,frame2),font=("bold",20),width=10).pack(side=RIGHT)
		#ends
		for i in range(self.cursor.rowcount):
			print(type(s1[i]))
			self.l.append(Radiobutton(frame,text=s1[i][0],indicatoron=0,width=40,font=("bold",20),variable=g,value=i))
			k=k+1
			
		Label(frame,text=" ",font=("bold",20),bg="blue").pack(side=TOP)
		for i in range(k):
			self.l[i].pack(side=TOP)
			Label(frame,text=" ",font=("bold",20),bg="blue").pack(side=TOP)
		for i in range(k):
			
			self.l[i].configure(command=lambda:self.lvl2(s1[g.get()],n,frame,frame2))
		#ends here#
#------------------------------------------------------------------------------------------------#
			
			
			
			
			
			
			
			
			
			
			
			
				
#------------------------------------------------------------------------------------------------
	#creating the first page#
	def create1(self,n,f,f2):
		f.destroy()
		f2.destroy()
		#im=Image.open('life.jpg')
		#logo=ImageTk.PhotoImage(im)
		
		frame=Frame(self.m,relief=RAISED,borderwidth=10,bg="blue")
		frame.pack(side=TOP, anchor=N, padx=5, pady=70,expand=True,fill="both")
		Label(frame,text="Category of problem:",font=('bold',30),width=40).pack(side=TOP,pady=15)
		Label(frame,text="",font=('bold',10),bg="blue").pack()
		v=IntVar()
		v=[]
		path = "projectimage.jpg"

		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
	#	Label(self.m,compound=CENTER,image=logo).pack(side=TOP)
		v.append("ENT")
		v.append("Stomach")
		v.append("Cough")
		v.append("Fever")
		v.append("Rashes")
		v.append("Muscle")
		v.append("Bone")
		r1=Radiobutton(frame,text="Stomach related problems",font=('bold',20),bg="blue",indicatoron=0,width=40,padx=20,command=lambda:self.category(v[1],frame,frame))
		
		r2=Radiobutton(frame,text="ENT related problems",indicatoron=0,font=('bold',20),width=40,padx=20,command=lambda:self.category(v[0],frame,frame))
		r3=Radiobutton(frame,text="Cough related problems",indicatoron=0,font=('bold',20),width=40,padx=20,command=lambda:self.category(v[2],frame,frame))
		r4=Radiobutton(frame,text="Fever related problems",indicatoron=0,font=('bold',20),width=40,padx=20,command=lambda:self.category(v[3],frame,frame))
		r5=Radiobutton(frame,text="Rashes related problems",indicatoron=0,font=('bold',20),width=40,padx=20,command=lambda:self.category(v[4],frame,frame))
		r6=Radiobutton(frame,text="Muscle related problems",indicatoron=0,font=('bold',20),width=40,padx=20,command=lambda:self.category(v[5],frame,frame))
		r7=Radiobutton(frame,text="Bone related problems",indicatoron=0,font=('bold',20),width=40,padx=20,command=lambda:self.category(v[6],frame,frame))

		
		r1.pack(side=TOP)
		#r2=Radiobutton(m,text="ENT related problems",indicatoron=0,width=20,variable=v,padx=20,value=2,command=dest)
		#r2.grid(row=3,column=1)
		Label(frame,text="",font=('bold',20),bg="blue").pack()
		r2.pack(side=TOP)
		#r3=Radiobutton(m,text="Cough related problems",indicatoron=0,width=20,variable=v,padx=20,value=3,command=dest)
		Label(frame,text="",font=('bold',20),bg="blue").pack()
		r3.pack(side=TOP)
		Label(frame,text="",font=('bold',20),bg="blue").pack()
		r4.pack(side=TOP)
		Label(frame,text="",font=('bold',20),bg="blue").pack()
		r5.pack(side=TOP)
		Label(frame,text="",font=('bold',20),bg="blue").pack()
		r6.pack(side=TOP)
		Label(frame,text="",font=('bold',20),bg="blue").pack()
		r7.pack(side=TOP)
		Label(frame,text="",font=('bold',20),bg="blue").pack(side=BOTTOM)
		Label(frame,text="abcd",font=('bold',20)).pack(side=BOTTOM)
		#ends here
#-----------------------------------------------------------------------------------------------#		







#------------------------------------------------------------------------------------------------#
#changed here
root = Tk()
root.title("Join")
root.geometry("720x420")
root.configure(bg="#747a99")
#root.configure(background='#D4FFEA')
root.rowconfigure((0,1), weight=1)  # make buttons stretch when
root.columnconfigure((0,2), weight=1)  # when window is resized
f=Frame()
f.pack()
program=program(root)
program.create1('b',f,f)
mainloop()
#ends
#------------------------------------------------------------------------------------------------#