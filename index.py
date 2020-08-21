
#Different libraries used to provide GUI
from tkinter import *
import time
import numpy as np
import matplotlib.pyplot as plt

#Pseudo Window created to show pseudo code of bubble sort
def bubble_pseudo_window():
    root7=Tk()
    root7.title("Pseudo Code")
    root7.geometry("650x850+100+0")
    
    def prev():
        root7.destroy()
        bubble()

    #Button created to invoke pseudo window
    button19=Button(root7,text="Previous Page",bg='#EBF5E6',command=prev)
    button19.grid(row=1,sticky=E)
    
    img2=PhotoImage(file="pic11.png")
    label2=Label(root7,image=img2)
    label2.grid(row=0)  
    root7.mainloop()

 #Simulation Window created to display simulation of bubble sort   
def bubble_simuation_window():
    root8=Tk()
    root8.title("Simulation Window")
    root8.geometry("1080x850+100+0")
    root8.configure(bg="white")
    
    def prev11():
        root8.destroy()
        bubble()

    #Button created to invoke Simulation window
    button19=Button(root8,text="Previous Page",bg='#EBF5E6',command=prev11)
    button19.grid(row=1,sticky=W)
    
    i=0
    while True:
        if i==0:
            img100=PhotoImage(file="pic39.png")
            label2=Label(root8,image=img100,bg="white")
            label2.grid(sticky=W,padx=200)
        i+=1
        root8.update()
        time.sleep(3)
        if i==1:    
            img101=PhotoImage(file="pic40.png")
            label3=Label(root8,image=img101,bg="white")
            label3.grid(sticky=W,padx=200)
        i+=1
        root8.update()
        time.sleep(3)
        if i==2:
            img102=PhotoImage(file="pic41.png")
            label4=Label(root8,image=img102,bg="white")
            label4.grid(sticky=W,padx=200)
        i+=1
        root8.update()
        time.sleep(3)
        if i==3: 
            img103=PhotoImage(file="pic42.png")
            label5=Label(root8,image=img103,bg="white")
            label5.grid(sticky=W,padx=200,pady=5)
        i+=1
        root8.update()
        time.sleep(3)    
        if i==4:
            img104=PhotoImage(file="pic43.png")
            label6=Label(root8,image=img104,bg="white")
            label6.grid(sticky=W,padx=200,pady=5)
        i+=1
        root8.update()
        time.sleep(3)
        if i==5:    
            img105=PhotoImage(file="pic44.png")
            label7=Label(root8,image=img105,bg="white")
            label7.grid(sticky=W,padx=200,pady=5)
        i+=1
        root8.update()
        time.sleep(3)
        if i==6:
            img106=PhotoImage(file="pic45.png")
            label8=Label(root8,image=img106,bg="white")
            label8.grid(sticky=W,padx=200,pady=5)
        i+=1
        root8.update()
        time.sleep(3)
        if i==7: 
            img107=PhotoImage(file="pic46.png")
            label9=Label(root8,image=img107,bg="white")
            label9.grid(sticky=W,padx=200,pady=5)
        i+=1
        root8.update()
        time.sleep(3)
        if i==8: 
            img108=PhotoImage(file="pic47.png")
            label10=Label(root8,image=img108,bg="white")
            label10.grid(sticky=W,padx=200,pady=5)    
            break
    
    root8.mainloop()

#Graph Window created to show complexity graph of bubble sort    
def Bubble_graph_window():
    root9=Tk()
    root9.title("complexity Graph")
    root9.geometry("755x790+100+0")
    root9.configure(bg="white")

    x = np.linspace(0, 6, 100)
    y_1 = np.power(x, 2)
    y_2 = np.power(x, 2)
    y_3 = np.power(x, 1)
    plt.plot(x, y_1, label = "Average CAse")
    plt.plot(x, y_2+0.5, label = "Worst Case")
    plt.plot(x, y_3, label = "Best Case")
    plt.title('Compexity of Bubble Sort')
    plt.xlabel('Time')
    plt.show()

    
    
    def prev21():
        root9.destroy()
        bubble()

    #Button created to invoke Graph window
    button19=Button(root9,text="Previous Page",bg='#EBF5E6',command=prev21)
    button19.grid(row=1,sticky=S)
    
    root9.mainloop()

#Pseudo Window created to display pseudo code of Insertion sort
def insertion_pseudo_window():
    root10=Tk()
    root10.title("Pseudo Code")
    root10.geometry("650x850+100+0")
    
    def prev2():
        root10.destroy()
        insertion()

    #Button created to invoke Pseudo window
    button19=Button(root10,text="Previous Page",bg='#EBF5E6',command=prev2)
    button19.grid(row=1,sticky=E)
    
    img2=PhotoImage(file="pic12.png")
    label2=Label(root10,image=img2)
    label2.grid(row=0)
    
    root10.mainloop()

 #Simulation Window created to show simulation of insertion sort  
def insertion_simulation_window():
    root11=Tk()
    root11.title("Simulation Window")
    root11.geometry("1080x850+100+0")
    root11.configure(bg="white")
    
    def prev12():
        root11.destroy()
        insertion()

    #Button created to invoke simulation window
    button19=Button(root11,text="Previous Page",bg='#EBF5E6',command=prev12)
    button19.grid(row=1,sticky=W)
    
    i=0
    while True:
        if i==0:
            img100=PhotoImage(file="pic30.png")
            label2=Label(root11,image=img100,bg="white")
            label2.grid(sticky=W,padx=200,pady=10)
        i+=1
        root11.update()
        time.sleep(3)
        if i==1:    
            img101=PhotoImage(file="pic31.png")
            label3=Label(root11,image=img101,bg="white")
            label3.grid(sticky=W,padx=200,pady=10)
        i+=1
        root11.update()
        time.sleep(3)
        if i==2:
            img102=PhotoImage(file="pic32.png")
            label4=Label(root11,image=img102,bg="white")
            label4.grid(sticky=W,padx=200,pady=10)
        i+=1
        root11.update()
        time.sleep(3)
        if i==3: 
            img103=PhotoImage(file="pic33.png")
            label5=Label(root11,image=img103,bg="white")
            label5.grid(sticky=W,padx=200,pady=10)
        i+=1
        root11.update()
        time.sleep(3)    
        if i==4:
            img104=PhotoImage(file="pic34.png")
            label6=Label(root11,image=img104,bg="white")
            label6.grid(sticky=W,padx=202,pady=10)
        i+=1
        root11.update()
        time.sleep(3)
        if i==5:    
            img105=PhotoImage(file="pic35.png")
            label7=Label(root11,image=img105,bg="white")
            label7.grid(sticky=W,padx=201,pady=10)
        i+=1
        root11.update()
        time.sleep(3)
        if i==6:
            img106=PhotoImage(file="pic36.png")
            label8=Label(root11,image=img106,bg="white")
            label8.grid(sticky=W,padx=200,pady=10)
        i+=1
        root11.update()
        time.sleep(3)
        if i==7: 
            img107=PhotoImage(file="pic37.png")
            label9=Label(root11,image=img107,bg="white")
            label9.grid(sticky=W,padx=200,pady=10) 
        i+=1
        root11.update()
        time.sleep(3)
        if i==8: 
            img108=PhotoImage(file="pic38.png")
            label10=Label(root11,image=img108,bg="white")
            label10.grid(sticky=W,padx=200,pady=10)    
            break
    
    root11.mainloop()

 #Graph Window designed to show complexity graph of insertion sort   
def insertion_graph_window():
    root12=Tk()
    root12.title("complexity Graph")
    root12.geometry("750x790+100+0")
    root12.configure(bg="white")

    
    x = np.linspace(0, 6, 100)
    y_1 = np.power(x,2)

    plt.subplot(211)
    plt.plot(x, y_1)
    plt.title('Compexity of Quick Sort')
    plt.ylabel('Worst Case')
    plt.xlabel('Time')

    fig, ax = plt.subplots()
    dt = 0.01
    x = np.arange(dt, 20.0, dt)
    ax.semilogx(x, np.exp(-x / 5.0))
    plt.ylabel('Average Case')
    plt.xlabel('Time')
    plt.title('Compexity of Quick Sort')

    fig, ax = plt.subplots()
    dt = 0.01
    x = np.arange(dt, 20.0, dt)
    ax.semilogx(x, np.exp(-x / 5.0))
    plt.ylabel('Best Case')
    plt.xlabel('Time')
    plt.title('Compexity of Quick Sort')
    plt.show()
    def prev22():
        root12.destroy()
        insertion()

    #Button created to invoke graph window
    button19=Button(root12,text="Previous Page",bg='#EBF5E6',command=prev22)
    button19.grid(row=1,sticky=S)
    
    root12.mainloop()

#Pseudo Window created to show pseudo code of selection sort    
def selection_pseudo_window():
    root13=Tk()
    root13.title("Pseudo Code")
    root13.geometry("650x850+100+0")
    
    def prev3():
        root13.destroy()
        selection()

    #Button created to invoke pseudo window
    button19=Button(root13,text="Previous Page",bg='#EBF5E6',command=prev3)
    button19.grid(row=1,sticky=E)
    
    img2=PhotoImage(file="pic13.png")
    label2=Label(root13,image=img2)
    label2.grid(row=0)
    
    root13.mainloop()

 #Simulation Window created to show simulation of selection sort   
def selection_simulation_window():
    root14=Tk()
    root14.title("Simulation Window")
    root14.geometry("1080x850+100+0")
    root14.configure(bg="white")
    

    
    def prev13():
        root14.destroy()
        selection()

    #Button created to invoke Simulation window
    button19=Button(root14,text="Previous Page",bg='#EBF5E6',command=prev13)
    button19.grid(row=1,sticky=W)
    
    i=0
    while True:
        if i==0:
            img100=PhotoImage(file="pic20.png")
            label2=Label(root14,image=img100,bg="white")
            label2.grid(sticky=W,padx=200)
        i+=1
        root14.update()
        time.sleep(3)
        if i==1:    
            img101=PhotoImage(file="pic21.png")
            label3=Label(root14,image=img101,bg="white")
            label3.grid(sticky=W,padx=193)
        i+=1
        root14.update()
        time.sleep(3)
        if i==2:
            img102=PhotoImage(file="pic22.png")
            label4=Label(root14,image=img102,bg="white")
            label4.grid(sticky=W,padx=193)
        i+=1
        root14.update()
        time.sleep(3)
        if i==3: 
            img103=PhotoImage(file="pic23.png")
            label5=Label(root14,image=img103,bg="white")
            label5.grid(sticky=W,padx=196)
        i+=1
        root14.update()
        time.sleep(3)
        if i==4: 
            img104=PhotoImage(file="pic24.png")
            label6=Label(root14,image=img104,bg="white")
            label6.grid(sticky=W,padx=198)
        i+=1
        root14.update()
        time.sleep(3)
        if i==5: 
            img105=PhotoImage(file="pic25.png")
            label7=Label(root14,image=img105,bg="white")
            label7.grid(sticky=W,padx=199)
        i+=1
        root14.update()
        time.sleep(3)
        if i==6: 
            img106=PhotoImage(file="pic26.png")
            label8=Label(root14,image=img106,bg="white")
            label8.grid(sticky=W,padx=193)
        i+=1
        root14.update()
        time.sleep(3)
        if i==7: 
            img107=PhotoImage(file="pic27.png")
            label9=Label(root14,image=img107,bg="white")
            label9.grid(sticky=W,padx=183)
        i+=1
        root14.update()
        time.sleep(3)
        if i==8: 
            img108=PhotoImage(file="pic28.png")
            label10=Label(root14,image=img108,bg="white")
            label10.grid(sticky=W,padx=195)    
            break
    
    root14.mainloop()

 #Graph Window created to show complexity graph of selection sort   
def selection_graph_window():
    root15=Tk()
    root15.title("complexity Graph")
    root15.geometry("755x790+100+0")
    root15.configure(bg="white")

    x = np.linspace(0, 6, 100)
    y_1 = np.power(x, 2)
    y_2 = np.power(x, 2)
    y_3 = np.power(x, 2)
    plt.plot(x, y_1, label = "Average Case")
    plt.plot(x, y_2+0.5, label = "Worst Case")
    plt.plot(x, y_3+1, label = "Best Case")
    plt.title('Compexity of Selection Sort')
    plt.xlabel('Time')
    plt.show()
    def prev23():
        root15.destroy()
        selection()
    #Button created to invoke graph window
    button19=Button(root15,text="Previous Page",bg='#EBF5E6',command=prev23)
    button19.grid(row=1,sticky=S)
    
    root15.mainloop()

 #Pseudo Window created to show pseudo code of merge sort   
def merge_pseudo_window():
    root16=Tk()
    root16.title("Pseudo Code")
    root16.geometry("650x850+100+0")
    
    def prev4():
        root16.destroy()
        merge()

    #Button created to invoke pseudo window
    button19=Button(root16,text="Previous Page",bg='#EBF5E6',command=prev4)
    button19.grid(row=1,sticky=E)
    
    img2=PhotoImage(file="pic14.png")
    label2=Label(root16,image=img2)
    label2.grid(row=0)
    
    root16.mainloop()

 #Simulation Window created to show simulation of merge sort   
def merge_simulation_window():
    root17=Tk()
    root17.title("Simulation Window")
    root17.geometry("1210x850+100+0")
    root17.configure(background="#1F333C")
                     
    def prev14():
        root17.destroy()
        merge()

    #Button created to invoke simulation window
    button19=Button(root17,text="Previous Page",bg='#EBF5E6',command=prev14)
    button19.grid(row=6,column=0,sticky=W)                 
                     
    i=0
    while True:
        if i==0:
            img100=PhotoImage(file="pic15.png")
            label2=Label(root17,image=img100,bg="#1F333C")
            label2.grid(pady=50,sticky=W)
        i+=1
        root17.update()
        time.sleep(3)
        if i==1:    
            img101=PhotoImage(file="pic16.png")
            label3=Label(root17,image=img101,bg="#1F333C")
            label3.grid(pady=25,sticky=W)
        i+=1
        root17.update()
        time.sleep(3)
        if i==2:
            img102=PhotoImage(file="pic17.png")
            label4=Label(root17,image=img102,bg="#1F333C")
            label4.grid(pady=25,sticky=W)
        i+=1
        root17.update()
        time.sleep(3)
        if i==3: 
            img103=PhotoImage(file="pic18.png")
            label5=Label(root17,image=img103,bg="#1F333C")
            label5.grid(pady=25,sticky=W)
        i+=1
        root17.update()
        time.sleep(3)
        if i==4: 
            img104=PhotoImage(file="pic19.png")
            label6=Label(root17,image=img104,bg="#1F333C")
            label6.grid(sticky=W)    
            break
    
    root17.mainloop()

 #Graph Window created to show complexity graph of merge sort   
def merge_graph_window():
    root18=Tk()
    root18.title("complexity Graph")
    root18.geometry("755x730+100+0")
    root18.configure(bg="white")
    
    np.random.seed(19680801)

    # make up some data in the interval ]0, 1[
    y = np.random.normal(loc=0.5, scale=0.4, size=1000)
    y = y[(y > 0) & (y < 1)]
    y.sort()
    x = np.arange(len(y))

    plt.subplot(221)
    plt.plot(x, y)
    plt.yscale('log')
    plt.ylabel("Worst Case")
    plt.title('Time Complexity of Merge Sort')
    plt.grid(True)
    plt.subplot(222)
    plt.plot(x, y, color = 'red')
    plt.ylabel('Average Case')
    plt.yscale('log')
    plt.grid(True)
    plt.subplot(223)
    plt.plot(x, y, color = 'orange')
    plt.ylabel('Best Case')
    plt.yscale('log')
    plt.grid(True)


    plt.show()
    
    def prev24():
        root18.destroy()
        merge()
    
    #Button created to invoke graph window
    button19=Button(root18,text="Previous Page",bg='#EBF5E6',command=prev24)
    button19.grid(row=1,sticky=S)
    
    root18.mainloop()

#Overview Window displays overview of project
def overview():
    root1=Tk()
    root1.title("Overview")
    root1.geometry("1080x850+100+0")
    
    def home6():
        root1.destroy()
        Home()
    def insert6():
        root1.destroy()
        insertion()
    def select6():
        root1.destroy()
        selection()
    def bubb6():
        root1.destroy()
        bubble()
    def merg6():
        root1.destroy()
        merge()
    def sort6():
        root1.destroy()
        sorting()
    
    frame1=Frame(root1)
    
    img0=PhotoImage(file="pic.png")
    label=Label(frame1,image=img0)
    label.grid(row=0)
    
    img1=PhotoImage(file="pic1.png")
    label1=Label(frame1,image=img1)
    label1.grid(row=1)
        
    img2=PhotoImage(file="pic2.png")
    label2=Label(frame1,image=img2)
    label2.grid(row=5)
    
    button1=Button(frame1,text="SA-Home",bg='#EBF5E6',command=home6)
    button1.grid(row=2,padx=20,pady=10,ipadx=22,sticky=W)
    
    button2=Button(frame1,text="SA-Overview",bg='#EBF5E6')
    button2.grid(row=3,padx=20,pady=2,ipadx=14,sticky=W)
    
    button1=Button(frame1,text="Sorting Algorithm",bg='#EBF5E6',command=sort6)
    button1.grid(row=4,padx=20,pady=10,sticky=W)
    
    button3=Button(frame1,text="Bubble Sort",bg='#EBF5E6',command=bubb6)
    button3.grid(row=6,padx=20,pady=10,ipadx=20,sticky=W)
    
    button4=Button(frame1,text="Insertion Sort",bg='#EBF5E6',command=insert6)
    button4.grid(row=7,padx=20,pady=2,ipadx=15,sticky=W)
    
    button5=Button(frame1,text="Selection Sort",bg='#EBF5E6',command=select6)
    button5.grid(row=8,padx=20,pady=10,ipadx=14,sticky=W)
    
    button6=Button(frame1,text="Merge Sort",bg='#EBF5E6',command=merg6)
    button6.grid(row=9,padx=20,pady=2,ipadx=22,sticky=W)
      
    frame1.grid(row=0,column=0,sticky=N)
    
    frame2=Frame(root1)
    
    img3=PhotoImage(file="pic5.png")
    label3=Label(frame2,image=img3)
    label3.grid(row=0,sticky=NW)
    
    frame2.grid(row=0,column=1,sticky=N)
    
    root1.mainloop()

#Sorting Window designed which gives basic idea about data structures and sorting       algorithms
def sorting():
    root2=Tk()
    root2.title("Sorting Algorithms")
    root2.geometry("1080x850+100+0")
    
    def over5():
        root2.destroy()
        overview()
    def insert5():
        root2.destroy()
        insertion()
    def select5():
        root2.destroy()
        selection()
    def bubb5():
        root2.destroy()
        bubble()
    def merg5():
        root2.destroy()
        merge()
    def home5():
        root2.destroy()
        Home()
    
    frame1=Frame(root2)
    
    img0=PhotoImage(file="pic.png")
    label=Label(frame1,image=img0)
    label.grid(row=0)
    
    img1=PhotoImage(file="pic1.png")
    label1=Label(frame1,image=img1)
    label1.grid(row=1)
        
    img2=PhotoImage(file="pic2.png")
    label2=Label(frame1,image=img2)
    label2.grid(row=5)
        
    button1=Button(frame1,text="SA-Home",bg='#EBF5E6',command=home5)
    button1.grid(row=2,padx=20,pady=10,ipadx=22,sticky=W)
    
    button2=Button(frame1,text="SA-Overview",bg='#EBF5E6',command=over5)
    button2.grid(row=3,padx=20,pady=2,ipadx=14,sticky=W)
    
    button1=Button(frame1,text="Sorting Algorithm",bg='#EBF5E6')
    button1.grid(row=4,padx=20,pady=10,sticky=W)
    
    button3=Button(frame1,text="Bubble Sort",bg='#EBF5E6',command=bubb5)
    button3.grid(row=6,padx=20,pady=10,ipadx=20,sticky=W)
    
    button4=Button(frame1,text="Insertion Sort",bg='#EBF5E6',command=insert5)
    button4.grid(row=7,padx=20,pady=2,ipadx=15,sticky=W)
    
    button5=Button(frame1,text="Selection Sort",bg='#EBF5E6',command=select5)
    button5.grid(row=8,padx=20,pady=10,ipadx=14,sticky=W)
    
    button6=Button(frame1,text="Merge Sort",bg='#EBF5E6',command=merg5)
    button6.grid(row=9,padx=20,pady=2,ipadx=22,sticky=W)

    frame1.grid(row=0,column=0,sticky=N)
    
    frame2=Frame(root2)
    
    img3=PhotoImage(file="pic6.png")
    label3=Label(frame2,image=img3)
    label3.grid(row=0,sticky=NW)
    
    frame2.grid(row=0,column=1,sticky=N)
    
    root2.mainloop()

#Bubble Window designed which explains about bubble sort    
def bubble():
    root3=Tk()
    root3.title("Bubble Sort")
    root3.geometry("1080x850+100+0")
    
    def g1():
        root3.destroy()
        Bubble_graph_window()
    
    def s1():
        root3.destroy()
        bubble_simuation_window()
    
    def e1():
        root3.destroy()
        bubble_pseudo_window()
    
    def over4():
        root3.destroy()
        overview()
    def insert4():
        root3.destroy()
        insertion()
    def select4():
        root3.destroy()
        selection()
    def home4():
        root3.destroy()
        Home()
    def merg4():
        root3.destroy()
        merge()
    def sort4():
        root3.destroy()
        sorting()
    
    frame1=Frame(root3)
    
    img0=PhotoImage(file="pic.png")
    label=Label(frame1,image=img0)
    label.grid(row=0)
    
    img1=PhotoImage(file="pic1.png")
    label1=Label(frame1,image=img1)
    label1.grid(row=1)
        
    img2=PhotoImage(file="pic2.png")
    label2=Label(frame1,image=img2)
    label2.grid(row=5)
    
    button1=Button(frame1,text="SA-Home",bg='#EBF5E6',command=home4)
    button1.grid(row=2,padx=20,pady=10,ipadx=22,sticky=W)
    
    button2=Button(frame1,text="SA-Overview",bg='#EBF5E6',command=over4)
    button2.grid(row=3,padx=20,pady=2,ipadx=14,sticky=W)
    
    button1=Button(frame1,text="Sorting Algorithm",bg='#EBF5E6',command=sort4)
    button1.grid(row=4,padx=20,pady=10,sticky=W)
    
    button3=Button(frame1,text="Bubble Sort",bg='#EBF5E6')
    button3.grid(row=6,padx=20,pady=10,ipadx=20,sticky=W)
    
    button4=Button(frame1,text="Insertion Sort",bg='#EBF5E6',command=insert4)
    button4.grid(row=7,padx=20,pady=2,ipadx=15,sticky=W)
    
    button5=Button(frame1,text="Selection Sort",bg='#EBF5E6',command=select4)
    button5.grid(row=8,padx=20,pady=10,ipadx=14,sticky=W)
    
    button6=Button(frame1,text="Merge Sort",bg='#EBF5E6',command=merg4)
    button6.grid(row=9,padx=20,pady=2,ipadx=22,sticky=W)
     
    frame1.grid(row=0,column=0,sticky=N)
    
    frame2=Frame(root3)
    
    img3=PhotoImage(file="pic7.png")
    label3=Label(frame2,image=img3)
    label3.grid(row=0,sticky=NW,columnspan=3)
    
    button7=Button(frame2,text="Pseudo Code",bg='#EBF5E6',command=e1)
    button7.grid(row=2,padx=20,pady=10,ipadx=22,sticky=W)
    
    button8=Button(frame2,text="Simulation",bg='#EBF5E6',command=s1)
    button8.grid(row=2,column=1,padx=20,pady=10,ipadx=22,sticky=W)
    
    button9=Button(frame2,text="Complexity Graph",bg='#EBF5E6',command=g1)
    button9.grid(row=2,column=2,padx=20,pady=10,ipadx=22,sticky=W)
    
    frame2.grid(row=0,column=1,sticky=N)
    
    root3.mainloop()

#Insertion Window designed which explains about insertion sort
def insertion():
    root4=Tk()
    root4.title("Insertion Sort")
    root4.geometry("1080x850+100+0")
    
    def g2():
        root4.destroy()
        insertion_graph_window()
    
    def s2():
        root4.destroy()
        insertion_simulation_window()
    
    def e2():
        root4.destroy()
        insertion_pseudo_window()
    
    def over3():
        root4.destroy()
        overview()
    def home3():
        root4.destroy()
        insertion()
    def select3():
        root4.destroy()
        selection()
    def bubb3():
        root4.destroy()
        bubble()
    def merg3():
        root4.destroy()
        merge()
    def sort3():
        root4.destroy()
        sorting()
    
    frame1=Frame(root4)
    
    img0=PhotoImage(file="pic.png")
    label=Label(frame1,image=img0)
    label.grid(row=0)
    
    img1=PhotoImage(file="pic1.png")
    label1=Label(frame1,image=img1)
    label1.grid(row=1)
    
    img2=PhotoImage(file="pic2.png")
    label2=Label(frame1,image=img2)
    label2.grid(row=5)
    
    button1=Button(frame1,text="SA-Home",bg='#EBF5E6',command=home3)
    button1.grid(row=2,padx=20,pady=10,ipadx=22,sticky=W)
    
    button2=Button(frame1,text="SA-Overview",bg='#EBF5E6',command=over3)
    button2.grid(row=3,padx=20,pady=2,ipadx=14,sticky=W)
    
    button1=Button(frame1,text="Sorting Algorithm",bg='#EBF5E6',command=sort3)
    button1.grid(row=4,padx=20,pady=10,sticky=W)
    
    button3=Button(frame1,text="Bubble Sort",bg='#EBF5E6',command=bubb3)
    button3.grid(row=6,padx=20,pady=10,ipadx=20,sticky=W)
    
    button4=Button(frame1,text="Insertion Sort",bg='#EBF5E6')
    button4.grid(row=7,padx=20,pady=2,ipadx=15,sticky=W)
    
    button5=Button(frame1,text="Selection Sort",bg='#EBF5E6',command=select3)
    button5.grid(row=8,padx=20,pady=10,ipadx=14,sticky=W)
    
    button6=Button(frame1,text="Merge Sort",bg='#EBF5E6',command=merg3)
    button6.grid(row=9,padx=20,pady=2,ipadx=22,sticky=W)
    
    frame1.grid(row=0,column=0,sticky=N)
    
    frame2=Frame(root4)
    
    img3=PhotoImage(file="pic10.png")
    label3=Label(frame2,image=img3)
    label3.grid(row=0,sticky=NW,columnspan=3)
    
    button10=Button(frame2,text="Pseudo Code",bg='#EBF5E6',command=e2)
    button10.grid(row=2,padx=20,pady=10,ipadx=22,sticky=W)
    
    button11=Button(frame2,text="Simulation",bg='#EBF5E6',command=s2)
    button11.grid(row=2,column=1,padx=20,pady=10,ipadx=22,sticky=W)
    
    button12=Button(frame2,text="Complexity Graph",bg='#EBF5E6',command=g2)
    button12.grid(row=2,column=2,padx=20,pady=10,ipadx=22,sticky=W)
    frame2.grid(row=0,column=1,sticky=N)
    
    root4.mainloop()

#Selection Window designed which explains about selection sort
def selection():
    root5=Tk()
    root5.title("Selection Sort")
    root5.geometry("1080x850+100+0")
    
    def g3():
        root5.destroy()
        selection_graph_window()
    
    def s3():
        root5.destroy()
        selection_simulation_window()
    
    def e3():
        root5.destroy()
        selection_pseudo_window()
    
    def over2():
        root5.destroy()
        overview()
    def insert2():
        root5.destroy()
        insertion()
    def home2():
        root5.destroy()
        Home()
    def bubb2():
        root5.destroy()
        bubble()
    def merg2():
        root5.destroy()
        merge()
    def sort2():
        root5.destroy()
        sorting()
    
    frame1=Frame(root5)
    
    img0=PhotoImage(file="pic.png")
    label=Label(frame1,image=img0)
    label.grid(row=0)
    
    img1=PhotoImage(file="pic1.png")
    label1=Label(frame1,image=img1)
    label1.grid(row=1)
    
    img2=PhotoImage(file="pic2.png")
    label2=Label(frame1,image=img2)
    label2.grid(row=5)
    
    button1=Button(frame1,text="SA-Home",bg='#EBF5E6',command=home2)
    button1.grid(row=2,padx=20,pady=10,ipadx=22,sticky=W)
    
    button2=Button(frame1,text="SA-Overview",bg='#EBF5E6',command=over2)
    button2.grid(row=3,padx=20,pady=2,ipadx=14,sticky=W)
    
    button1=Button(frame1,text="Sorting Algorithm",bg='#EBF5E6',command=sort2)
    button1.grid(row=4,padx=20,pady=10,sticky=W)
    
    button3=Button(frame1,text="Bubble Sort",bg='#EBF5E6',command=bubb2)
    button3.grid(row=6,padx=20,pady=10,ipadx=20,sticky=W)
    
    button4=Button(frame1,text="Insertion Sort",bg='#EBF5E6',command=insert2)
    button4.grid(row=7,padx=20,pady=2,ipadx=15,sticky=W)
    
    button5=Button(frame1,text="Selection Sort",bg='#EBF5E6')
    button5.grid(row=8,padx=20,pady=10,ipadx=14,sticky=W)
    
    button6=Button(frame1,text="Merge Sort",bg='#EBF5E6',command=merg2)
    button6.grid(row=9,padx=20,pady=2,ipadx=22,sticky=W)

    frame1.grid(row=0,column=0,sticky=N)
    
    frame2=Frame(root5)
    
    img3=PhotoImage(file="pic8.png")
    label3=Label(frame2,image=img3)
    label3.grid(row=0,sticky=NW,columnspan=3)
    
    frame2.grid(row=0,column=1,sticky=N)
    
    button13=Button(frame2,text="Pseudo Code",bg='#EBF5E6',command=e3)
    button13.grid(row=2,padx=20,pady=10,ipadx=22,sticky=W)
    
    button14=Button(frame2,text="Simulation",bg='#EBF5E6',command=s3)
    button14.grid(row=2,column=1,padx=20,pady=10,ipadx=22,sticky=W)
    
    button15=Button(frame2,text="Complexity Graph",bg='#EBF5E6',command=g3)
    button15.grid(row=2,column=2,padx=20,pady=10,ipadx=22,sticky=W)
    root5.mainloop()    

#Merge Window designed which explains about merge sort
def merge():
    root6=Tk()
    root6.title("Merge Sort")
    root6.geometry("1080x850+100+0")
    
    def g4():
        root6.destroy()
        merge_graph_window()
    
    def s4():
        root6.destroy()
        merge_simulation_window()
    
    def e4():
        root6.destroy()
        merge_pseudo_window()
    
    def over1():
        root6.destroy()
        overview()
    def insert1():
        root6.destroy()
        insertion()
    def select1():
        root6.destroy()
        selection()
    def bubb1():
        root6.destroy()
        bubble()
    def home1():
        root6.destroy()
        Home()
    def sort1():
        root6.destroy()
        sorting()
    
    frame1=Frame(root6)
    
    img0=PhotoImage(file="pic.png")
    label=Label(frame1,image=img0)
    label.grid(row=0)
    
    img1=PhotoImage(file="pic1.png")
    label1=Label(frame1,image=img1)
    label1.grid(row=1)
       
    img2=PhotoImage(file="pic2.png")
    label2=Label(frame1,image=img2)
    label2.grid(row=5)
    
    button1=Button(frame1,text="SA-Home",bg='#EBF5E6',command=home1)
    button1.grid(row=2,padx=20,pady=10,ipadx=22,sticky=W)
    
    button2=Button(frame1,text="SA-Overview",bg='#EBF5E6',command=over1)
    button2.grid(row=3,padx=20,pady=2,ipadx=14,sticky=W)
    
    button1=Button(frame1,text="Sorting Algorithm",bg='#EBF5E6',command=sort1)
    button1.grid(row=4,padx=20,pady=10,sticky=W)
    
    button3=Button(frame1,text="Bubble Sort",bg='#EBF5E6',command=bubb1)
    button3.grid(row=6,padx=20,pady=10,ipadx=20,sticky=W)
    
    button4=Button(frame1,text="Insertion Sort",bg='#EBF5E6',command=insert1)
    button4.grid(row=7,padx=20,pady=2,ipadx=15,sticky=W)
    
    button5=Button(frame1,text="Selection Sort",bg='#EBF5E6',command=select1)
    button5.grid(row=8,padx=20,pady=10,ipadx=14,sticky=W)
    
    button6=Button(frame1,text="Merge Sort",bg='#EBF5E6')
    button6.grid(row=9,padx=20,pady=2,ipadx=22,sticky=W)
    

    
    frame1.grid(row=0,column=0,sticky=N)
    
    frame2=Frame(root6)
    
    img3=PhotoImage(file="pic9.png")
    label3=Label(frame2,image=img3)
    label3.grid(row=0,sticky=NW,columnspan=3)
    
    frame2.grid(row=0,column=1,sticky=N)
    
    button16=Button(frame2,text="Pseudo Code",bg='#EBF5E6',command=e4)
    button16.grid(row=2,padx=20,pady=10,ipadx=22,sticky=W)
    
    button17=Button(frame2,text="Simulation",bg='#EBF5E6',command=s4)
    button17.grid(row=2,column=1,padx=20,pady=10,ipadx=22,sticky=W)
    
    button18=Button(frame2,text="Complexity Graph",bg='#EBF5E6',command=g4)
    button18.grid(row=2,column=2,padx=20,pady=10,ipadx=22,sticky=W)
    root6.mainloop()

    
#Home window designed which provides user interface
def Home():
    root=Tk()
    root.title("Sorting")
    root.geometry("1080x850+100+0") 
    
    def over():
        root.destroy()
        overview()
    def insert():
        root.destroy()
        insertion()
    def select():
        root.destroy()
        selection()
    def bubb():
        root.destroy()
        bubble()
    def merg():
        root.destroy()
        merge()
    def sort():
        root.destroy()
        sorting()
    
    frame1=Frame(root)
    
    img0=PhotoImage(file="pic.png")
    label=Label(frame1,image=img0)
    label.grid(row=0)
    
    img1=PhotoImage(file="pic1.png")
    label1=Label(frame1,image=img1)
    label1.grid(row=1)
    
    img2=PhotoImage(file="pic2.png")
    label2=Label(frame1,image=img2)
    label2.grid(row=5)
    
    button1=Button(frame1,text="SA-Home",bg='#EBF5E6')
    button1.grid(row=2,padx=20,pady=10,ipadx=22,sticky=W)
    
    button2=Button(frame1,text="SA-Overview",bg='#EBF5E6',command=over)
    button2.grid(row=3,padx=20,pady=2,ipadx=14,sticky=W)
    
    button1=Button(frame1,text="Sorting Algorithm",bg='#EBF5E6',command=sort)
    button1.grid(row=4,padx=20,pady=10,sticky=W)
    
    button3=Button(frame1,text="Bubble Sort",bg='#EBF5E6',command=bubb)
    button3.grid(row=6,padx=20,pady=10,ipadx=20,sticky=W)
    
    button4=Button(frame1,text="Insertion Sort",bg='#EBF5E6',command=insert)
    button4.grid(row=7,padx=20,pady=2,ipadx=15,sticky=W)
    
    button5=Button(frame1,text="Selection Sort",bg='#EBF5E6',command=select)
    button5.grid(row=8,padx=20,pady=10,ipadx=14,sticky=W)
    
    button6=Button(frame1,text="Merge Sort",bg='#EBF5E6',command=merg)
    button6.grid(row=9,padx=20,pady=2,ipadx=22,sticky=W)
    
    frame1.grid(row=0,column=0,sticky=N)
    
    frame2=Frame(root)
    
    img3=PhotoImage(file="pic3.png")
    label3=Label(frame2,image=img3)
    label3.grid(row=0,sticky=NW)
    
    img4=PhotoImage(file="pic4.png")
    label6=Label(frame2,image=img4)
    label6.grid(row=1)
    
    frame2.grid(row=0,column=1,sticky=N)

    root.mainloop()
Home()


