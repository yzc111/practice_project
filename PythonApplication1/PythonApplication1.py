
from sqlite3 import *
from tkinter import *
from tkinter.messagebox import *
from traceback import *
import tkinter.messagebox
import  pickle
rt=Tk()

rt.geometry('600x400')   #制作主界面大小
rt.title('迷你图书管理')   #标题
idat = PhotoImage(file = 'timg.gif')
labl = Label(image=idat)
labl.place(x = 0,y = 0)








manfra = LabelFrame()
manfra.pack()
dbfile = 'BookInfo.dat'#数据库名称
#浏览图书部分
def dispbook():
    global manfra
    cn = connect(dbfile)
    cur = cn.execute('select * from book')
    book = cur.fetchall()
    cn.close()
    manfra.destroy()
    #对图书进行讨论
    if len(book)==0:
        showwarning('图书管理','没有图书!')
    else:                
        manfra=LabelFrame(text='图书信息')
        manfra.pack(anchor='center',pady=50,ipadx=5,ipady=5)#设置图书信息界面的大小
        manfra.columnconfigure(1,minsize=80)
        manfra.columnconfigure(2,minsize=100)   
        manfra.columnconfigure(3,minsize=200)
        Label(manfra,text='图书序号',
            font=('微软雅黑',9,'normal'),bd=1,
            relief=SOLID).grid(row=1,column=1,sticky=N+E+S+W)
        Label(manfra,text='图书号',
            font=('微软雅黑',9,'normal'),bd=1,
            relief=SOLID).grid(row=1,column=2,sticky=N+E+S+W)
        Label(manfra,text='图书名称',
            font=('微软雅黑',9),bd=1,
            relief=SOLID).grid(row=1,column=3,sticky=N+E+S+W)                
        rn = 2                
        for x in book:
            cn = 1
            Label(manfra,text=str(rn-1),
                font=('微软雅黑',9,'bold'),bd=1,
                relief=SOLID).grid(row=rn,column=cn,sticky=N+E+S+W)
            for a in x:
                cn+=1
                Label(manfra,text=str(a),
                    font=('微软雅黑',9),bd=1,
                    relief=SOLID).grid(row=rn,column=cn,sticky=N+E+S+W)
            rn+=1
#编辑图书的界面部分
def editbook():
    global manfra
    manfra.destroy()
    manfra = LabelFrame(text='编辑图书')
    manfra.pack(anchor='center',pady=50,ipadx=5,ipady=5)
    tf = LabelFrame(manfra,text='查找图书')
    tf.pack(anchor='center',pady=10,ipadx=5,ipady=5)            
    Label(tf,text='输入图书号',anchor=E).grid(row=1,column=1)
    cno = StringVar()            
    txtcno = Entry(tf,textvariable=cno)
    txtcno.grid(row=1,column=2)            
    btok = Button(tf,text='查找')
    btok.grid(row=1,column=3)
    editframe = LabelFrame(manfra,text='编辑图书')
    editframe.pack(anchor='center',pady=20,ipadx=5,ipady=5)
    btdel = Button(editframe,text='删除图书',state=DISABLED)
    btdel.pack(anchor=NW)
    op = LabelFrame(editframe,text='修改图书')
    op.pack(anchor='center',pady=10,ipadx=5,ipady=5)
    Label(op,text='新图书号',anchor=E).grid(row=1,column=1)
    newuserid = StringVar()            
    newtxtuid = Entry(op,textvariable=newuserid)
    newtxtuid.grid(row=1,column=2)
    Label(op,text='新图书名',anchor=E).grid(row=2,column=1,sticky=E)
    newpassword = StringVar()            
    newtxtpwd = Entry(op,textvariable=newpassword)
    newtxtpwd.grid(row=2,column=2)
    bteditsave = Button(op,text=' 修改',state=DISABLED)
    bteditsave.grid(row=1,column=3,rowspan=2,sticky=N+E+S+W)
    def dofind():
        cid = cno.get()  
        if find(cid)==-1:
            showinfo('图书管理','%s 没有记录！' % cid)
        else:
            btdel.config(state='normal')
            bteditsave.config(state='normal')
    def dodelete():
        cid = cno.get()
        if askokcancel('图书管理', "确认删除：%s？" % cid):
            cn = connect(dbfile)
            cn.execute('delete from book where cno=?',(cid,))
            cn.commit()
            cn.close()
            showinfo('图书管理', "成功删除：%s" % cid)         
    def saveedit():
        cid = cno.get()
        newname=newuserid.get()
        if newname=='':
            showerror('图书管理','新图书名错误：%s' % newname)
            newtxtuid.focus_set()
        else:                                                        
            if find(newname)==1:
                showerror('图书管理','图书  %s已经存在：' % newname)
                newtxtuid.focus_set()
            else:
                cna=newpassword.get()
                if cna=='':
                    showerror('图书管理','图书号无效!')
                    newtxtpwd.focus_set()                   
                else:
                    cn=connect(dbfile)               
                    cn.execute('update book set cno=?,cname=?\
                        where cno=?',(newname,cna,cid))
                    cn.commit()
                    cn.close()
                    showinfo('图书管理','修改成功!')
    btok.config(command = dofind)
    btdel.config(command = dodelete)
    bteditsave.config(command = saveedit)
#添加图书界面部分
def appebook():
    global manfra            
    manfra.destroy()
    manfra = LabelFrame(text='添加图书')
    manfra.pack(anchor=CENTER,pady=120,ipadx=5,ipady=5)
    tf=Frame(manfra)
    tf.pack()
    Label(tf,text='图书号',anchor=E).grid(row=1,column=1)
    cno = StringVar()            
    txtcno = Entry(tf,textvariable=cno)
    txtcno.grid(row=1,column=2)
    Label(tf,text='图书名',anchor=E).grid(row=2,column=1,sticky=E)
    cname = StringVar()            
    txtcna = Entry(tf,textvariable=cname)
    txtcna.grid(row=2,column=2)
    tf2 = Frame(manfra)
    tf2.pack()
    btok = Button(tf2,text='添加')
    btok.grid(row=1,column=1)
    btclear = Button(tf2,text='清空')
    btclear.grid(row=1,column=2)
    def clearall():
        cno.set('')
        cname.set('')
    def savenew():
        cid = cno.get()
        cna = cname.get()
        if cid=='':
            showerror('图书管理','图书名无效!')        
        else:        
            if find(cid)==1:
                showerror('图书管理','图书名已经存在!')
                txtcno.focus()
            else:
                if cna=='':
                    showerror('图书管理','图书名输入无效！')
                else:
                    cn=connect(dbfile)
                    cn.execute('insert into book values(?,?)',(cid,cna))
                    cn.commit()
                    cn.close() 
                    showinfo('图书管理','已成功添加图书！')   
    btclear.config(command = clearall)
    btok.config(command = savenew)                       
def find(namekey):
    cn = connect(dbfile)
    cur = cn.execute('select * from book where cno=?',(namekey,))
    books = cur.fetchall()
    if len(books)>0:
        n=1
    else:
        n=-1
    cn.close()
    return n
def resetdb():
    global manfra
    manfra.destroy()
    if askokcancel('图书管理', '清除图书!\n是否继续？'):
        cn = connect(dbfile)
        cn.execute('drop table if exists book')
        cn.execute('create table book(cno text primary key,cname text)')
        cn.close()
        showinfo('图书管理','初始图书记录成功！')
def sysexit():
    if askokcancel('图书管理', "确认退出?"):
        rt.destroy()
#关于帮助
def dispinfo():
    global manfra
    manfra.destroy() 
    manfra = LabelFrame(text='帮助',bd=1,relief=SUNKEN)
    manfra.pack(expand=YES,fill=BOTH)
    sc = Scrollbar(manfra)
    sc.pack(side=RIGHT,fill=Y)
    text1 = Text(manfra)
    text1.pack(expand=YES,fill=BOTH)
    text1.config(yscrollcommand=sc.set)
    sc.config(command=text1.yview) 
    log = open('Help.txt','r',encoding = 'utf8')
    logtxt = log.read()
    log.close()
    text1.insert('2.0',logtxt)
def dispabout():
    showinfo('版权','图书管理 v2.0\n 谢谢使用该系统!\n2020年6月11日') 

#登录函数
def usr_log_in():
    def login():
        #输入框获取用户名密码
        name=var_usr_name.get()
        pwd=var_usr_pwd.get()
        #从本地字典获取用户信息，如果没有则新建本地数据库
        try:
            with open('usr_info.pickle','rb') as usr_file:
                usrs_info=pickle.load(usr_file)
        except FileNotFoundError:
            with open('usr_info.pickle','wb') as usr_file:
                usrs_info={'admin':'admin'}
                pickle.dump(usrs_info,usr_file)
        #判断用户名和密码是否匹配
        if name in usrs_info:
            if pwd == usrs_info[name]:
                tkinter.messagebox.showinfo(title='welcome',
                                       message='欢迎您：'+name)
                Label.pack_forget
            else:
                tkinter.messagebox.showerror(message='密码错误')
        #用户名密码不能为空
        elif name=='' or pwd=='' :
            tkinter.messagebox.showerror(message='用户名或密码为空')
        #不在数据库中弹出是否注册的框
        else:
            print("111")
            is_signup=tkinter.messagebox.askyesno('欢迎','您还没有注册，是否现在注册')
            if is_signup:
                usr_sign_up()
 #新建登录界面
    window_sign_up=Toplevel(rt)
    window_sign_up.geometry('350x200')
    window_sign_up.title('登录')
    #用户名变量及标签、输入框
    var_usr_name=StringVar()
    Label(window_sign_up,text='用户名：').place(x=10,y=10)
    Entry(window_sign_up,textvariable=var_usr_name).place(x=150,y=10)
    #密码变量及标签、输入框
    var_usr_pwd=StringVar()
    Label(window_sign_up,text='请输入密码：').place(x=10,y=50)
    Entry(window_sign_up,textvariable=var_usr_pwd,show='*').place(x=150,y=50)    
    #确认注册按钮及位置
    bt_confirm_sign_up=Button(window_sign_up,text='确认登录',
                                 command=login)
    bt_confirm_sign_up.place(x=150,y=130)   
#注册函数
def usr_sign_up():
    #确认注册时的相应函数
    def signtowcg():
        #获取输入框内的内容
        nn=new_name.get()
        np=new_pwd.get()
        npf=new_pwd_confirm.get()
 
        #本地加载已有用户信息,如果没有则已有用户信息为空
        try:
            with open('usr_info.pickle','rb') as usr_file:
                exist_usr_info=pickle.load(usr_file)
        except FileNotFoundError:
            exist_usr_info={}           
            
        #检查用户名存在、密码为空、密码前后不一致
        if nn in exist_usr_info:
            tkinter.messagebox.showerror('错误','用户名已存在')
        elif np =='' or nn=='':
            tkinter.messagebox.showerror('错误','用户名或密码为空')
        elif np !=npf:
            tkinter.messagebox.showerror('错误','密码前后不一致')
        #注册信息没有问题则将用户名密码写入数据库
        else:
            exist_usr_info[nn]=np
            with open('usr_info.pickle','wb') as usr_file:
                pickle.dump(exist_usr_info,usr_file)
            tkinter.messagebox.showinfo('欢迎','注册成功')
            #注册成功关闭注册框
            window_sign_up.destroy()

#新建注册界面
    window_sign_up=Toplevel(rt)
    window_sign_up.geometry('350x200')
    window_sign_up.title('注册')
    #用户名变量及标签、输入框
    new_name=StringVar()
    Label(window_sign_up,text='用户名：').place(x=10,y=10)
    Entry(window_sign_up,textvariable=new_name).place(x=150,y=10)
    #密码变量及标签、输入框
    new_pwd=StringVar()
    Label(window_sign_up,text='请输入密码：').place(x=10,y=50)
    Entry(window_sign_up,textvariable=new_pwd,show='*').place(x=150,y=50)    
    #重复密码变量及标签、输入框
    new_pwd_confirm=StringVar()
    Label(window_sign_up,text='请再次输入密码：').place(x=10,y=90)
    Entry(window_sign_up,textvariable=new_pwd_confirm,show='*').place(x=150,y=90)    
    #确认注册按钮及位置
    bt_confirm_sign_up=Button(window_sign_up,text='确认注册',
                                 command=signtowcg)
    bt_confirm_sign_up.place(x=150,y=130)
#退出的函数
def usr_sign_quit():
    rt.destroy()

#登录 注册按钮
bt_login=Button(rt,text='登录',command=usr_log_in)
bt_login.place(x=480,y=10)
bt_logup=Button(rt,text='注册',command=usr_sign_up)
bt_logup.place(x=520,y=10)
bt_logquit=Button(rt,text='退出',command=usr_sign_quit)
bt_logquit.place(x=560,y=10)
menubar = Menu(rt)
rt.config(menu=menubar)
file = Menu(menubar,tearoff=0)
file.add_command(label='浏览图书',command=dispbook)
file.add_separator()
file.add_command(label='添加图书',command=appebook)
file.add_command(label='编辑图书',command=editbook)
file.add_command(label='清空图书',command=resetdb) 
file.add_separator()
file.add_command(label='退出',command=sysexit)
menubar.add_cascade(label='图书',menu=file)
help =Menu(menubar,tearoff=0)
help.add_command(label='信息',command=dispinfo) 
help.add_command(label='关于',command=dispabout)
menubar.add_cascade(label='帮助',menu=help)

rt.mainloop()