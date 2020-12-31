#!/usr/bin/env python
# coding: utf-8

# In[25]:


#
import datetime
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from platypus import NSGAII, Problem, Real
from pyswmm import Simulation, SystemStats, LidControls, LidGroups, Subcatchments, Nodes

#
from tkinter import *
import tkinter.filedialog
from tkinter.simpledialog import *

#
root = Tk()
root.geometry('1024x480')
root.title('多目标优化')

# 
def xz1():
    global filename1
    filename1=tkinter.filedialog.askopenfilename()
    if filename1 != '':
        lb1.config(text='文件地址 '+filename1)
    else:
        lb1.config(text='您没有选择任何文件')

# 
def xz2():
    global filename2
    filename2=tkinter.filedialog.askdirectory()
    if filename2 != '':
        lb2.config(text='图片保存文件夹 '+filename2)
    else:
        lb2.config(text='您没有选择任何文件夹')
        
#
def run1():
    global s
    s=askstring('请输入','请输入循环次数')
    lbB.config(text=s)    

# 设计空间多目标优化算法的web交互
def swmm(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32,x33,x34,x35,x36,x37,x38,x39,x40):
    # from pyswmm import Simulation, SystemStats, LidControls, LidGroups, Subcatchments, Nodes
    # 输入SWMM的input文件（路径）——交互输入
    with Simulation(filename1) as sim:
        system_routing = SystemStats(sim)
        node_object = Nodes(sim)
        # 选择规模变化的LID设施——交互输入，比如Out1=xxx（xxx为SWMM模型中outfall的name），
        # lid1=Sn（Sn为LID规模变化的subcatchment的name）,lid2=Sm....
        # 最好设计成可以用户添加的交互，比如用户可以添加一个LID，也可以添加多个
        Out1 = node_object["Out1"]
        lid1 = LidGroups(sim)["S1"]
        lid9 = LidGroups(sim)["S9"]
        lid13 = LidGroups(sim)["S13"]
        lid19 = LidGroups(sim)["S19"]
        lid22 = LidGroups(sim)["S22"]
        lid24 = LidGroups(sim)["S24"]
        lid25 = LidGroups(sim)["S25"]
        lid87 = LidGroups(sim)["S87"]
        lid92 = LidGroups(sim)["S92"]
        lid93 = LidGroups(sim)["S93"]
        lid94 = LidGroups(sim)["S94"]
        lid95 = LidGroups(sim)["S95"]
        lid96 = LidGroups(sim)["S96"]
        lid99 = LidGroups(sim)["S99"]
        lid130 = LidGroups(sim)["S130"]
        lid64 = LidGroups(sim)["S64"]
        lid66 = LidGroups(sim)["S66"]
        lid108 = LidGroups(sim)["S108"]
        lid106 = LidGroups(sim)["S106"]
        lid110 = LidGroups(sim)["S110"]
        lid60 = LidGroups(sim)["S60"]
        lid112 = LidGroups(sim)["S112"]
        lid100 = LidGroups(sim)["S100"]
        lid107 = LidGroups(sim)["S107"]
        lid109 = LidGroups(sim)["S109"]
        lid14 = LidGroups(sim)["S14"]
        lid81 = LidGroups(sim)["S81"]
        lid4 = LidGroups(sim)["S4"]
        lid91 = LidGroups(sim)["S91"]
        lid15 = LidGroups(sim)["S15"]
        lid17 = LidGroups(sim)["S17"]
        lid18 = LidGroups(sim)["S18"]
        lid6 = LidGroups(sim)["S6"]
        lid12 = LidGroups(sim)["S12"]
        lid16 = LidGroups(sim)["S16"]
        lid11 = LidGroups(sim)["S11"]
        lid117 = LidGroups(sim)["S117"]
        lid101 = LidGroups(sim)["S101"]
        lid86 = LidGroups(sim)["S86"]
        lid50 = LidGroups(sim)["S50"]
        
        # 定义每个可变规模的LID的面积——内部运算（基于上述输入的可变规模的LID）
        for lid in lid1:lid.unit_area=x1
        for lid in lid9:lid.unit_area=x2
        for lid in lid13:lid.unit_area=x3
        for lid in lid19:lid.unit_area=x4
        for lid in lid22:lid.unit_area=x5
        for lid in lid24:lid.unit_area=x6
        for lid in lid25:lid.unit_area=x7
        for lid in lid87:lid.unit_area=x8
        for lid in lid92:lid.unit_area=x9
        for lid in lid93:lid.unit_area=x10
        for lid in lid94:lid.unit_area=x11
        for lid in lid95:lid.unit_area=x12
        for lid in lid96:lid.unit_area=x13
        for lid in lid99:lid.unit_area=x14
        for lid in lid130:lid.unit_area=x15
        for lid in lid64:lid.unit_area=x16
        for lid in lid66:lid.unit_area=x17
        for lid in lid108:lid.unit_area=x18
        for lid in lid106:lid.unit_area=x19
        for lid in lid110:lid.unit_area=x20
        for lid in lid60:lid.unit_area=x21
        for lid in lid112:lid.unit_area=x22
        for lid in lid100:lid.unit_area=x23
        for lid in lid107:lid.unit_area=x24
        for lid in lid109:lid.unit_area=x25
        for lid in lid14:lid.unit_area=x26
        for lid in lid81:lid.unit_area=x27
        for lid in lid4:lid.unit_area=x28
        for lid in lid91:
            lid.unit_area=x29
        for lid in lid15:
            lid.unit_area=x30
        for lid in lid17:
            lid.unit_area=x31
        for lid in lid18:
            lid.unit_area=x32
        for lid in lid6:
            lid.unit_area=x33
        for lid in lid12:
            lid.unit_area=x34
        for lid in lid16:
            lid.unit_area=x35
        for lid in lid11:
            lid.unit_area=x36
        for lid in lid117:
            lid.unit_area=x37
        for lid in lid101:
            lid.unit_area=x38
        for lid in lid86:
            lid.unit_area=x39
        for lid in lid50:
            lid.unit_area=x40
        for step in sim:
            pass
        y = round((Out1.cumulative_inflow*7.47*0.0037854/1261),6)
    return y;

def pollutant(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32,x33,x34,x35,x36,x37,x38,x39,x40):
    #from pyswmm import Simulation, SystemStats, LidControls, LidGroups, Subcatchments, Nodes
    #和上面是同一个路径的input文件
    with Simulation(filename1) as sim:
        system_routing = SystemStats(sim)
        node_object = Nodes(sim)
        #和上面同样定义的各个LID
        Out1 = node_object["Out1"]
        lid1 = LidGroups(sim)["S1"]
        lid9 = LidGroups(sim)["S9"]
        lid13 = LidGroups(sim)["S13"]
        lid19 = LidGroups(sim)["S19"]
        lid22 = LidGroups(sim)["S22"]
        lid24 = LidGroups(sim)["S24"]
        lid25 = LidGroups(sim)["S25"]
        lid87 = LidGroups(sim)["S87"]
        lid92 = LidGroups(sim)["S92"]
        lid93 = LidGroups(sim)["S93"]
        lid94 = LidGroups(sim)["S94"]
        lid95 = LidGroups(sim)["S95"]
        lid96 = LidGroups(sim)["S96"]
        lid99 = LidGroups(sim)["S99"]
        lid130 = LidGroups(sim)["S130"]
        lid64 = LidGroups(sim)["S64"]
        lid66 = LidGroups(sim)["S66"]
        lid108 = LidGroups(sim)["S108"]
        lid106 = LidGroups(sim)["S106"]
        lid110 = LidGroups(sim)["S110"]
        lid60 = LidGroups(sim)["S60"]
        lid112 = LidGroups(sim)["S112"]
        lid100 = LidGroups(sim)["S100"]
        lid107 = LidGroups(sim)["S107"]
        lid109 = LidGroups(sim)["S109"]
        lid14 = LidGroups(sim)["S14"]
        lid81 = LidGroups(sim)["S81"]
        lid4 = LidGroups(sim)["S4"]
        lid91 = LidGroups(sim)["S91"]
        lid15 = LidGroups(sim)["S15"]
        lid17 = LidGroups(sim)["S17"]
        lid18 = LidGroups(sim)["S18"]
        lid6 = LidGroups(sim)["S6"]
        lid12 = LidGroups(sim)["S12"]
        lid16 = LidGroups(sim)["S16"]
        lid11 = LidGroups(sim)["S11"]
        lid117 = LidGroups(sim)["S117"]
        lid101 = LidGroups(sim)["S101"]
        lid86 = LidGroups(sim)["S86"]
        lid50 = LidGroups(sim)["S50"]
        #根据上面输入的LID进行内部运算
        for lid in lid1:
            lid.unit_area=x1
        for lid in lid9:
            lid.unit_area=x2
        for lid in lid13:
            lid.unit_area=x3
        for lid in lid19:
            lid.unit_area=x4
        for lid in lid22:
            lid.unit_area=x5
        for lid in lid24:
            lid.unit_area=x6
        for lid in lid25:
            lid.unit_area=x7
        for lid in lid87:
            lid.unit_area=x8
        for lid in lid92:
            lid.unit_area=x9
        for lid in lid93:
            lid.unit_area=x10
        for lid in lid94:
            lid.unit_area=x11
        for lid in lid95:
            lid.unit_area=x12
        for lid in lid96:
            lid.unit_area=x13
        for lid in lid99:
            lid.unit_area=x14
        for lid in lid130:
            lid.unit_area=x15
        for lid in lid64:
            lid.unit_area=x16
        for lid in lid66:
            lid.unit_area=x17
        for lid in lid108:
            lid.unit_area=x18
        for lid in lid106:
            lid.unit_area=x19
        for lid in lid110:
            lid.unit_area=x20
        for lid in lid60:
            lid.unit_area=x21
        for lid in lid112:
            lid.unit_area=x22
        for lid in lid100:
            lid.unit_area=x23
        for lid in lid107:
            lid.unit_area=x24
        for lid in lid109:
            lid.unit_area=x25
        for lid in lid14:
            lid.unit_area=x26
        for lid in lid81:
            lid.unit_area=x27
        for lid in lid4:
            lid.unit_area=x28
        for lid in lid91:
            lid.unit_area=x29
        for lid in lid15:
            lid.unit_area=x30
        for lid in lid17:
            lid.unit_area=x31
        for lid in lid18:
            lid.unit_area=x32
        for lid in lid6:
            lid.unit_area=x33
        for lid in lid12:
            lid.unit_area=x34
        for lid in lid16:
            lid.unit_area=x35
        for lid in lid11:
            lid.unit_area=x36
        for lid in lid117:
            lid.unit_area=x37
        for lid in lid101:
            lid.unit_area=x38
        for lid in lid86:
            lid.unit_area=x39
        for lid in lid50:
            lid.unit_area=x40
        for step in sim:
            pass
        data=Out1.outfall_statistics
        a=data.get("pollutant_loading")
        data=a
        b=float(data["SS"])
        c=round(b/13.9258,6)
    return c;

#内部运算
def schaffer(vars):
    x1=vars[0]
    x2=vars[1]
    x3=vars[2]
    x4=vars[3]
    x5=vars[4]
    x6=vars[5]
    x7=vars[6]
    x8=vars[7]
    x9=vars[8]
    x10=vars[9]
    x11=vars[10]
    x12=vars[11]
    x13=vars[12]
    x14=vars[13]
    x15=vars[14]
    x16=vars[15]
    x17=vars[16]
    x18=vars[17]
    x19=vars[18]
    x20=vars[19]
    x21=vars[20]
    x22=vars[21]
    x23=vars[22]
    x24=vars[23]
    x25=vars[24]
    x26=vars[25]
    x27=vars[26]
    x28=vars[27]
    x29=vars[28]
    x30=vars[29]
    x31=vars[30]
    x32=vars[31]
    x33=vars[32]
    x34=vars[33]
    x35=vars[34]
    x36=vars[35]
    x37=vars[36]
    x38=vars[37]
    x39=vars[38]
    x40=vars[39] 
    return [round(((x1+x2+x3+x4+x5+x6+x7+x15+x18+x19+x20+x22+x23+x24+x25+x26+x28+x30+x31+x32+x33+x34+x35+x36+x37+x38)*50+(x8+x9+x10+x11+x12+x13+x14+x16+x17+x21+x29+x40)*150)/10000,4),
            swmm(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32,x33,x34,x35,x36,x37,x38,x39,x40),
            pollutant(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32,x33,x34,x35,x36,x37,x38,x39,x40)]

def run2():
    problem = Problem(40, 3)
    #输入上述每个LID的可变规模区间——交互输入，如lid1=（x，y）x为面积下限，y为上限
    problem.types[:] = [Real(1000,6500),Real(1000,6400),Real(1000,4200),Real(1000,4600),Real(700,3000),Real(1000,7450),Real(2000,9500),Real(1000,4300),Real(700,3400),Real(1000,4100),Real(1000,4200),Real(1000,5500),Real(700,3600),Real(1000,4000),Real(1000,14000),Real(1000,9500),Real(1000,9600),Real(1000,6100),Real(1000,4900),Real(1000,4500),Real(1000,3900),Real(1000,3600),Real(1000,3400),Real(1000,3400),Real(1000,3400),Real(1000,3200),Real(1000,3200),Real(1000,2900),Real(1000,2700),Real(1000,2700),Real(1000,2700),Real(1000,2500),Real(1000,2400),Real(1000,2400),Real(1000,2400),Real(1000,2200),Real(1000,2200),Real(1000,2200),Real(1000,2200),Real(1000,2200)]
    problem.function = schaffer
    
    #
    num = int(s)

    #starttime = datetime.datetime.now()
    algorithm = NSGAII(problem)
    #输入循环次数——交互输入
    algorithm.run(num)

    for solution in algorithm.result:
        print(solution.objectives)
        print(solution)
    endtime = datetime.datetime.now()
    
    #
    fig=plt.figure()
    x=[s.objectives[0] for s in algorithm.result]
    y=[s.objectives[1] for s in algorithm.result]
    z=[s.objectives[2] for s in algorithm.result]
    ax = Axes3D(fig)
    ax.scatter(x, y, z)

    ax.set_zlabel('SS', fontdict={'size': 10, 'color': 'red'})
    ax.set_ylabel('RUNOFF', fontdict={'size': 10, 'color': 'red'})
    ax.set_xlabel('COST', fontdict={'size': 10, 'color': 'red'})

    plt.savefig(str(filename2)+'/result.png')
    plt.show()
    
#
btn1=Button(root,text='选择inp文件',command=xz1)
btn1.pack()
btn1.place(relx=0.1, rely=0.1, relwidth=0.1, relheight=0.1)
#
lb1 = Label(root,text='您没有选择任何文件')
lb1.pack()
lb1.place(relx=0.2, rely=0.1, relwidth=0.5, relheight=0.1)

#
btn2=Button(root,text='保存文件夹',command=xz2)
btn2.pack()
btn2.place(relx=0.1, rely=0.25, relwidth=0.1, relheight=0.1)
#
lb2 = Label(root,text='您没有选择任何文件夹')
lb2.pack()
lb2.place(relx=0.2, rely=0.25, relwidth=0.5, relheight=0.1)

#
Bbtn=Button(root,text='请输入循环次数',command=run1)
Bbtn.place(relx=0.1, rely=0.4, relwidth=0.1, relheight=0.1)
#
lbB = Label(root,text='您没有输入有效循环次数')
lbB.pack()
lbB.place(relx=0.2, rely=0.4, relwidth=0.5, relheight=0.1)

#
Rbtn=Button(root,text='运算',command=run2)
Rbtn.place(relx=0.1, rely=0.6, relwidth=0.1, relheight=0.1)

    
#
root.mainloop()


# In[ ]:




