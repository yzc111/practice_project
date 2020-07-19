from tkinter import scrolledtext 
from tkinter import *
import os
import os.path
import tkinter.messagebox

import tkinter.font as tf
import sqlite3
from  tkinter import ttk  #导入内部包

db=sqlite3.connect("C:\\Users\\Administrator\\Desktop\\私活\\gui\\tongxunlu.db")
#db.execute("create table TXL (sno varchar(20) not null unique,sname varchar(20),sex varchar(20),telno varchar(20),QQ varchar(20),home varchar(20))")
#db.execute('drop table TXL')
#插入界面#插入界面#插入界面#插入界面#插入界面#插入界面#插入界面


def insert():
    wdinsert=Tk()
    wdinsert.title("添加一条记录")
    wdinsert.geometry("1300x800")


    labelsno=Label(wdinsert,text="学号")
    labelsno.place(x=0,y=0)
    entrysno=Entry(wdinsert)
    entrysno.place(x=80,y=0)



    labelsname=Label(wdinsert,text="姓名")
    labelsname.place(x=0,y=30)
    entrysname=Entry(wdinsert)
    entrysname.place(x=80,y=30)



    labelsex=Label(wdinsert,text="性别")
    labelsex.place(x=0,y=60)
    entrysex=Entry(wdinsert)
    entrysex.place(x=80,y=60)


    labeltel=Label(wdinsert,text="手机号")
    labeltel.place(x=0,y=90)
    entrytel=Entry(wdinsert)
    entrytel.place(x=80,y=90)



    labelQQ=Label(wdinsert,text="QQ号")
    labelQQ.place(x=0,y=120)
    entryQQ=Entry(wdinsert)
    entryQQ.place(x=80,y=120)


    labelhome=Label(wdinsert,text="家庭住址")
    labelhome.place(x=0,y=150)
    entryhome=Entry(wdinsert)
    entryhome.place(x=80,y=150)

    tree=ttk.Treeview(wdinsert,show="headings")#表格
    tree["columns"]=("学号","姓名","性别","手机号","QQ号","家庭住址")
    tree.column("学号",width=100)   #表示列,不显示
    tree.column("姓名",width=100)
    tree.column("性别",width=100)
    tree.column("手机号",width=100)
    tree.column("QQ号",width=100)
    tree.column("家庭住址",width=150)

     
    tree.heading("学号",text="学号")  #显示表头
    tree.heading("姓名",text="姓名")
    tree.heading("性别",text="性别")
    tree.heading("手机号",text="手机号")  
    tree.heading("QQ号",text="QQ号")
    tree.heading("家庭住址",text="家庭住址")
    tree.place(x=250,y=0)
    def delButton(tree):
        x=tree.get_children()
        for item in x:
            tree.delete(item)
 

    delButton(tree)
    for i in db.execute('select * from TXL order by sno'):
        temp=str(str(i))
        temp=temp.strip("(")
        temp=temp.strip(")\n")
        temp1=temp.replace("'","")
        a=temp1.split(',',6)
        a=list(a)

        tree.insert("",0,text="" ,values=(a[0],a[1],a[2],a[3],a[4],a[5]))
        
    db.commit()

    def insertsummit():
        try:
            value=[]
            sno=str(entrysno.get())
            value.append(sno)
            sname=str(entrysname.get())
            value.append(sname)
            sex=str(entrysex.get())
            value.append(sex)
            telno=str(entrytel.get())
            value.append(telno)
            QQ=str(entryQQ.get())
            value.append(QQ)
            home=str(entryhome.get())
            value.append(home)
            if(sno==''or sname==''or sex==''or telno==''or QQ==''or home==''):
                tkinter.messagebox.askquestion(title="错误",message="不要空")
            else:
                db.execute('insert into TXL values(?,?,?,?,?,?)',value)
                db.commit()
                tkinter.messagebox.askquestion(title="正确",message="插入成功")

                delButton(tree)
                for i in db.execute('select * from TXL order by sno'):
                    temp=str(i)
                    temp=temp.strip("(")
                    temp=temp.strip(")\n")
                    temp1=temp.replace("'","")
                    a=temp1.split(',',6)
                    a=list(a)
                    tree.insert("",0,text="" ,values=(a[0],a[1],a[2],a[3],a[4],a[5]))
                    


            
        except BaseException as e:
            tkinter.messagebox.askquestion(title="错误",message="插入失败")
        
            
        
        
    btsummit=Button(wdinsert,text="提交",command=insertsummit)
    btsummit.place(x=80,y=180)

    btconcel=Button(wdinsert,text="取消")
    btconcel.place(x=120,y=180)

#插入界面#插入界面#插入界面#插入界面#插入界面#插入界面#插入界面





#修改界面#修改界面#修改界面#修改界面#修改界面#修改界面#修改界面


def modify():
    wdmodify=Tk()
    wdmodify.title("修改记录")
    wdmodify.geometry("1000x400")

    

    
    mlabelsno=Label(wdmodify,text="学号")
    mlabelsno.place(x=0,y=0)
    mentrysno=Entry(wdmodify)
    mentrysno.place(x=80,y=0)



    mlabelsname=Label(wdmodify,text="姓名")
    mlabelsname.place(x=0,y=30)
    mentrysname=Entry(wdmodify)
    mentrysname.place(x=80,y=30)



    mlabelsex=Label(wdmodify,text="性别")
    mlabelsex.place(x=0,y=60)
    mentrysex=Entry(wdmodify)
    mentrysex.place(x=80,y=60)


    mlabeltel=Label(wdmodify,text="手机号")
    mlabeltel.place(x=0,y=90)
    mentrytel=Entry(wdmodify)
    mentrytel.place(x=80,y=90)



    mlabelQQ=Label(wdmodify,text="QQ号")
    mlabelQQ.place(x=0,y=120)
    mentryQQ=Entry(wdmodify)
    mentryQQ.place(x=80,y=120)


    mlabelhome=Label(wdmodify,text="家庭住址")
    mlabelhome.place(x=0,y=150)
    mentryhome=Entry(wdmodify)
    mentryhome.place(x=80,y=150)

    

    tree=ttk.Treeview(wdmodify,show="headings")#表格
    tree["columns"]=("学号","姓名","性别","手机号","QQ号","家庭住址")
    tree.column("学号",width=100)   #表示列,不显示
    tree.column("姓名",width=100)
    tree.column("性别",width=100)
    tree.column("手机号",width=100)
    tree.column("QQ号",width=100)
    tree.column("家庭住址",width=150)

     
    tree.heading("学号",text="学号")  #显示表头
    tree.heading("姓名",text="姓名")
    tree.heading("性别",text="性别")
    tree.heading("手机号",text="手机号")  
    tree.heading("QQ号",text="QQ号")
    tree.heading("家庭住址",text="家庭住址")
    tree.place(x=250,y=0)
    def delButton(tree):
        x=tree.get_children()
        for item in x:
            tree.delete(item)
 

    delButton(tree)
    for i in db.execute('select * from TXL order by sno'):
        temp=str(str(i))
        temp=temp.strip("(")
        temp=temp.strip(")\n")
        temp1=temp.replace("'","")
        a=temp1.split(',',6)
        a=list(a)

        tree.insert("",0,text="" ,values=(a[0],a[1],a[2],a[3],a[4],a[5]))
        
    db.commit()


    def treeviewClick(event):#单击
        for item in tree.selection():
            mentrysno.delete(0,END)
            mentrysname.delete(0,END)
            mentrysex.delete(0,END)
            mentrytel.delete(0,END)
            mentryQQ.delete(0,END)
            mentryhome.delete(0,END)
            a= tree.item(item,"values")
            #print(a[0])#输出所选行的第一列的值
            mentrysno.insert(1,a[0])
            mentrysname.insert(1,a[1])
            mentrysex.insert(1,a[2])
            mentrytel.insert(1,a[3])
            mentryQQ.insert(1,a[4])
            mentryhome.insert(1,a[5])
     
    tree.bind('<ButtonRelease-1>', treeviewClick)#绑定单击离开事件


    def modifysummit():
        try:
            value=[]
            sno=str(mentrysno.get())
            sname=str(mentrysname.get())
            sex=str(mentrysex.get())
            telno=str(mentrytel.get())
            QQ=str(mentryQQ.get())
            home=str(mentryhome.get())
            
            if(sno==''or sname==''or sex==''or telno==''or QQ==''or home==''):
                tkinter.messagebox.askquestion(title="错误",message="不要空")
            else:
                try:
                    db.execute('update TXL set sname=? where sno=?',(sname,sno))
                    db.execute('update TXL set sex=? where sno=?',(sex,sno))
                    db.execute('update TXL set telno=? where sno=?',(telno,sno))
                    db.execute('update TXL set QQ=? where sno=?',(QQ,sno))
                    db.execute('update TXL set home=? where sno=?',(home,sno))

                    db.commit()
                    tkinter.messagebox.askquestion(title="正确",message="修改成功")

                    scr = scrolledtext.ScrolledText(wdmodify, width=1000, height=400, wrap=tkinter.WORD)
                    scr.delete(1.0, END)
                    s="     学号          姓名    性别      手机号            QQ号          家庭住址  \n"
                    scr.insert(END,s)
                    for i in db.execute('select * from TXL order by sno'):
                        scr.insert(END,(str(i)+'\n'))
            
                except BaseException as e:
                    print(e)
                    tkinter.messagebox.askquestion(title="错误",message="修改失败")
        except Exception as e:
            print(e)
       
            
        
        
    btsummit=Button(wdmodify,text="确认修改",command=modifysummit)
    btsummit.place(x=60,y=180)

    btconcel=Button(wdmodify,text="取消")
    btconcel.place(x=120,y=180)

#修改界面#修改界面#修改界面#修改界面#修改界面#修改界面#修改界面




#查看界面#查看界面#查看界面#查看界面#查看界面#查看界面#查看界面#查看界面


def look():
    
    wdlook=Tk()
    wdlook.title("查看")
    wdlook.geometry("1000x300")
    
    labelsno=Label(wdlook,text="学号")
    labelsno.place(x=0,y=0)
    lentrysno=Entry(wdlook)
    lentrysno.place(x=80,y=0)

    tree=ttk.Treeview(wdlook,show="headings")#表格
    tree["columns"]=("学号","姓名","性别","手机号","QQ号","家庭住址")
    tree.column("学号",width=100)   #表示列,不显示
    tree.column("姓名",width=100)
    tree.column("性别",width=100)
    tree.column("手机号",width=100)
    tree.column("QQ号",width=100)
    tree.column("家庭住址",width=150)

    tree.heading("学号",text="学号")  #显示表头
    tree.heading("姓名",text="姓名")
    tree.heading("性别",text="性别")
    tree.heading("手机号",text="手机号")  
    tree.heading("QQ号",text="QQ号")
    tree.heading("家庭住址",text="家庭住址")
    tree.place(x=250,y=0)
    
    def delButton(tree):#清空表格
        x=tree.get_children()
        for item in x:
            tree.delete(item)

    delButton(tree)
    
    for i in db.execute('select * from TXL order by sno'):
        temp=str(str(i))
        temp=temp.strip("(")
        temp=temp.strip(")\n")
        temp1=temp.replace("'","")
        a=temp1.split(',',6)
        a=list(a)

        tree.insert("",0,text="" ,values=(a[0],a[1],a[2],a[3],a[4],a[5]))
        
    db.commit()

    def looksummit():
        sno=lentrysno.get()
        delButton(tree)
        for i in db.execute('select * from TXL where sno= ?',[sno]):
            temp=str(str(i))
            temp=temp.strip("(")
            temp=temp.strip(")\n")
            temp1=temp.replace("'","")
            a=temp1.split(',',6)
            a=list(a)
            tree.insert("",0,text="" ,values=(a[0],a[1],a[2],a[3],a[4],a[5]))
        
    db.commit()
    btsummit=Button(wdlook,text="提交",command=looksummit)
    btsummit.place(x=80,y=180)

    btconcel=Button(wdlook,text="取消")
    btconcel.place(x=120,y=180)
        
 
#查看界面#查看界面#查看界面#查看界面#查看界面#查看界面#查看界面#查看界面


















#删除界面#删除界面#删除界面#删除界面#删除界面#删除界面#删除界面#删除界面


def delete():
    wddelete=Tk()
    wddelete.title("修改记录")
    wddelete.geometry("1000x400")


    dlabelsno=Label(wddelete,text="学号")
    dlabelsno.place(x=0,y=0)
    dentrysno=Entry(wddelete)
    dentrysno.place(x=80,y=0)


    tree=ttk.Treeview(wddelete,show="headings")#表格
    tree["columns"]=("学号","姓名","性别","手机号","QQ号","家庭住址")
    tree.column("学号",width=100)   #表示列,不显示
    tree.column("姓名",width=100)
    tree.column("性别",width=100)
    tree.column("手机号",width=100)
    tree.column("QQ号",width=100)
    tree.column("家庭住址",width=150)

    tree.heading("学号",text="学号")  #显示表头
    tree.heading("姓名",text="姓名")
    tree.heading("性别",text="性别")
    tree.heading("手机号",text="手机号")  
    tree.heading("QQ号",text="QQ号")
    tree.heading("家庭住址",text="家庭住址")
    tree.place(x=250,y=0)
    
    def delButton(tree):#清空表格
        x=tree.get_children()
        for item in x:
            tree.delete(item)

    delButton(tree)
    for i in db.execute('select * from TXL order by sno'):
        temp=str(str(i))
        temp=temp.strip("(")
        temp=temp.strip(")\n")
        temp1=temp.replace("'","")
        a=temp1.split(',',6)
        a=list(a)
        tree.insert("",0,text="" ,values=(a[0],a[1],a[2],a[3],a[4],a[5]))  
    db.commit()


    

    def deletesummit():
        try:
            sno=str(dentrysno.get())           
            if(sno==''):
                tkinter.messagebox.askquestion(title="错误",message="不要空")
            else:
                db.execute('delete from TXL where sno=? ',[sno])
                db.commit()
                tkinter.messagebox.askquestion(title="正确",message="删除成功")
                delButton(tree)
                for i in db.execute('select * from TXL order by sno'):
                    temp=str(str(i))
                    temp=temp.strip("(")
                    temp=temp.strip(")\n")
                    temp1=temp.replace("'","")
                    a=temp1.split(',',6)
                    a=list(a)
                    tree.insert("",0,text="" ,values=(a[0],a[1],a[2],a[3],a[4],a[5]))  
                    db.commit()
        except BaseException as e:
            tkinter.messagebox.askquestion(title="错误",message="删除失败")
       
            
        
        
    btsummit=Button(wddelete,text="确认删除",command=deletesummit)
    btsummit.place(x=60,y=180)

    btconcel=Button(wddelete,text="取消")
    btconcel.place(x=120,y=180)

#删除界面#删除界面#删除界面#删除界面#删除界面#删除界面#删除界面#删除界面




















#主界面#主界面#主界面#主界面#主界面#主界面#主界面#主界面#主界面

wdmain=Tk()
wdmain.title("我的通讯录")
wdmain.geometry("400x300")

ft = tf.Font(family='华文隶书', size=20)
frame1 = Frame(wdmain)
label= Label(frame1,text="电子通讯录",justify=LEFT,font = ft)
label.pack(side=LEFT)
frame1.pack(padx=1,pady=1)
frame1.place(x = 120,y = 90)
btinsert=Button(wdmain,text="添加",command=insert)
btinsert.place(x=113,y=120)

btlook=Button(wdmain,text="查看",command=look)
btlook.place(x=153,y=120)

btmodify=Button(wdmain,text="修改",command=modify)
btmodify.place(x=193,y=120)

btdelete=Button(wdmain,text="删除",command=delete)
btdelete.place(x=233,y=120)
wdmain.mainloop()
#主界面#主界面#主界面#主界面#主界面#主界面#主界面#主界面#主界面








