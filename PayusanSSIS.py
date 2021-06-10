from tkinter import *
from tkinter import ttk
import tkinter.ttk as ttk
import tkinter.messagebox
import os 
import csv

class Student:
    
    def __init__ (self,root):
        self.root = root
        self.root.title("STUDENT INFORMATION SYSTEM")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="#FFC0CB")
        self.root.resizable(False,False)
        self.data = dict()
        self.temp = dict()
        self.filename = "StudentData.csv"
        
        FirstName = StringVar()
        MiddleName = StringVar()
        LastName = StringVar()
        StudID = StringVar()
        YearLevel = StringVar()
        Gender = StringVar()
        Course = StringVar()
        Searchbar = StringVar()
        
        if not os.path.exists('StudentData.csv'):
            with open('StudentData.csv', mode='w') as csv_file:
                fieldnames = ["Student ID", "Last Name", "First Name", "Middle Name","Gender", "Year Level", "Course"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
        
        else:
            with open('StudentData.csv', newline='') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    self.data[row["Student ID"]] = {'Last Name': row["Last Name"], 'First Name': row["First Name"], 'Middle Name': row["Middle Name"], 'Gender': row["Gender"],'Year Level': row["Year Level"], 'Course': row["Course"]}
            self.temp = self.data.copy()
        
        
         
        #=============================================================FUNCTIONS================================================================#
        
        def iExit():
            iExit = tkinter.messagebox.askyesno("SIS","Confirm to EXIT")
            if iExit > 0:
                root.destroy()
                return
            
        def addStd():
            with open('StudentData.csv', "a", newline="") as file:
                csvfile = csv.writer(file)
                if StudID.get()=="" or FirstName.get()=="" or MiddleName.get()=="" or LastName.get()=="" or YearLevel.get()=="":
                    tkinter.messagebox.showinfo("SIS","Please fill in the box.")
                else:
                    self.data[StudID.get()] = {'Last Name': LastName.get(), 'First Name': FirstName.get(), 'Middle Name': MiddleName.get(), 'Gender': Gender.get(),'Year Level': YearLevel.get(), 'Course': Course.get()}
                    self.saveData()
                    tkinter.messagebox.showinfo("SIS", "Success!")
                ClearStd()
                DisplayStd()
                    
        def ClearStd():
            StudID.set("")
            FirstName.set("")
            MiddleName.set("")
            LastName.set("")
            YearLevel.set("")
            Gender.set("")
            Course.set("")
        
        def DisplayStd():
            tree.delete(*tree.get_children())
            with open('StudentData.csv') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    IDNumber=row['Student ID']
                    LastName=row['Last Name']
                    FirstName=row['First Name']
                    MiddleName=row['Middle Name']
                    YearLevel=row['Year Level']
                    Course=row['Course']
                    Gender=row['Gender']
                    tree.insert("",END, values=(IDNumber, LastName, FirstName, MiddleName, Gender, YearLevel, Course))
                    
        def deleteStd():
            if tree.focus()=="":
                tkinter.messagebox.showerror("SIS","Select a student")
                return
            id_no = tree.item(tree.focus(),"values")[0]
            
            self.data.pop(id_no, None)
            self.saveData()
            tree.delete(tree.focus())
            tkinter.messagebox.showinfo("SIS","Record Deleted!")
            
        def searchStd():
            if self.Search.get() in self.data:
                vals = list(self.data[self.Search.get()].values())
                tree.delete(*tree.get_children())
                tree.insert("",0, values=(self.Search.get(), vals[0],vals[1],vals[2],vals[3],vals[4],vals[5]))
            elif self.Search.get() == "":
                DisplayStd()
            else:
                tkinter.messagebox.showerror("SIS", "Student not found")
                return
        
        def editStd():
            if tree.focus() == "":
                tkinter.messagebox.showerror("SIS", "Please elect a student")
                return
            values = tree.item(tree.focus(), "values")
            StudID.set(values[0])
            LastName.set(values[1])
            FirstName.set(values[2])
            MiddleName.set(values[3])
            Gender.set(values[4])
            YearLevel.set(values[5])
            Course.set(values[6])
       
        def updateStd():
            with open('StudentData.csv', "a", newline="") as file:
                csvfile = csv.writer(file)
                if StudID.get()=="" or FirstName.get()=="" or MiddleName.get()=="" or LastName.get()=="" or YearLevel.get()=="":
                    tkinter.messagebox.showinfo("SIS","Please select a student")
                else:
                    self.data[StudID.get()] = {'Last Name': LastName.get(), 'First Name': FirstName.get(), 'Middle Name': MiddleName.get(), 'Gender': Gender.get(),'Year Level': YearLevel.get(), 'Course': Course.get()}
                    self.saveData()
                    tkinter.messagebox.showinfo("SIS", "Updated Successfully ")
                ClearStd()
                DisplayStd()     

        #============================================================FRAMES=====================================================================#

        ManageFrame=Frame(self.root, bd=5, relief =RIDGE,  bg="#FFC0CB")
        ManageFrame.place(x=20, y=100,width=470, height=500)

        title=Label(self.root, text = "MSU-IIT STUDENT INFORMATION SYSTEM",bd=4,relief=RIDGE, font=("Times new roman",40,"bold"),bg="#f25278", fg="white")
        title.pack(side=TOP)
        
        DetailFrame=Frame(self.root, bd=4, relief =RIDGE,  bg="#FFC0CB")
        DetailFrame.place(x=510, y=100,width=830, height=500)

        ButtonFrame=Frame(self.root, bd=4, bg="thistle1", relief = RIDGE)
        ButtonFrame.place(x=260,y=620, width=880, height=90)
        
        #============================================================LABELS AND ENTRY WIDGETS====================================================#

        title=Label(ManageFrame, text="STUDENT'S INFORMATION",bg="#f25278", fg="white", font=("Times new roman",20,"bold"))
        title.grid(row=0, columnspan=2, pady=20)
        
        self.lblStdID = Label(ManageFrame, font=("Times new roman",15,"bold"),text="ID Number:", padx=2, pady=2, bg="#f25278", fg="white",  height=1, width=11)
        self.lblStdID.grid(row=1, column=0,padx=5,pady=5)
        self.txtStdID = Entry(ManageFrame, font=("Times new roman",15,"bold"),textvariable=StudID, relief=GROOVE, width=27)
        self.txtStdID.grid(row=1, column=1)
        self.txtStdID.place(x=150,y=85)

        self.lblFirstname = Label(ManageFrame,font=("Times new roman",15,"bold"),text="Last Name:", padx=2, pady=2, bg="#f25278", fg="white", height=1, width=11)
        self.lblFirstname.grid(row=2, column=0,padx=5,pady=5, sticky="w")        
        self.txtFirstname = Entry(ManageFrame, font=("Times new roman",15,"bold"),textvariable=LastName, relief=GROOVE,width=27)
        self.txtFirstname.grid(row=2, column=1)
        self.txtFirstname.place(x=150,y=127)
        
        self.lblMidname = Label(ManageFrame, font=("Times new roman",15,"bold"),text="First Name:", padx=2, pady=2, bg="#f25278", fg="white", height=1, width=11)
        self.lblMidname.grid(row=3, column=0,padx=5,pady=5, sticky="w")
        self.txtMidname = Entry(ManageFrame, font=("Times new roman",15,"bold"),textvariable=FirstName, relief=GROOVE,width=27)
        self.txtMidname.grid(row=3, column=1)
        self.txtMidname.place(x=150,y=169)

        self.lblSurname = Label(ManageFrame, font=("Times new roman",15,"bold"),text="Middle Initial:", padx=2, pady=2, bg="#f25278", fg="white", height=1, width=11)
        self.lblSurname.grid(row=4, column=0,padx=5,pady=5, sticky="w")
        self.txtSurname = Entry(ManageFrame, font=("Times new roman",15,"bold"),textvariable=MiddleName, relief=GROOVE,width=27)
        self.txtSurname.grid(row=4, column=1)
        self.txtSurname.place(x=150,y=211)

        self.lblYearlevel = Label(ManageFrame, font=("Times new roman",15,"bold"),text="Year Level:", padx=2, pady=2, bg="#f25278", fg="white", height=1, width=11)
        self.lblYearlevel.grid(row=5, column=0,padx=5,pady=5, sticky="w")
        self.comboYearlevel=ttk.Combobox(ManageFrame,font=("Times new roman",15,"bold"), state="readonly",width=26, textvariable=YearLevel)
        self.comboYearlevel['values']=("First Year","Second Year", "Third Year", "Fourth Year", "Fifth Year")
        self.comboYearlevel.grid(row=5,column=1)
        self.comboYearlevel.place(x=150,y=253)

        self.lblGender = Label(ManageFrame, font=("Times new roman",15,"bold"),text="Gender:", padx=2, pady=2, bg="#f25278", fg="white", height=1, width=11)
        self.lblGender.grid(row=6, column=0,padx=5,pady=5, sticky="w")
        self.comboGender=ttk.Combobox(ManageFrame,font=("Times new roman",15,"bold"), state="readonly",width=26, textvariable=Gender)
        self.comboGender['values']=("Male","Female")
        self.comboGender.grid(row=6,column=1)
        self.comboGender.place(x=150,y=295)

        self.lblCourse = Label(ManageFrame, font=("Times new roman",15,"bold"),text="Course:", padx=2, pady=2, bg="#f25278", fg="white", height=1, width=11)
        self.lblCourse.grid(row=7, column=0,padx=5,pady=5, sticky="w")
        self.txtCourse = Entry(ManageFrame, font=("Times new roman",15,"bold"),textvariable=Course, relief=GROOVE,width=27)
        self.txtCourse.grid(row=7, column=1)

        #============================================================BUTTON WIDGET====================================================#

        self.btnAddData = Button(ButtonFrame,text="Add", font=("Times new roman",10,"bold"),bg="#f26b8a", fg="black", height=3, width=14, bd=5,command=addStd)
        self.btnAddData.grid(row=0, column=0, padx=15, pady=15)
        self.btnAddData.place(x=20,y=10)

        self.btnUpdateData = Button(ButtonFrame, text="Update", font=("Times new roman",10,"bold"),bg="#f26b8a", fg="black", height=3, width=14, bd=5, command=updateStd)
        self.btnUpdateData.grid(row=0, column=2, padx=15, pady=15)
        self.btnUpdateData.place(x=200,y=10)

        self.btnClearData = Button(ButtonFrame, text="Clear", font=("Times new roman",10,"bold"),bg="#f26b8a", fg="black", height=3, width=14, bd=5,command=ClearStd)
        self.btnClearData.grid(row=1, column=0,padx=15, pady=15)
        self.btnClearData.place(x=380,y=10)

        self.btnDeleteData = Button(ButtonFrame, text="Delete", font=("Times new roman",10,"bold"),bg="#f26b8a", fg="black", height=3, width=14, bd=5, command=deleteStd)
        self.btnDeleteData.grid(row=1, column=1,padx=15, pady=15)
        self.btnDeleteData.place(x=560,y=10)

        self.btnExit = Button(ButtonFrame, text="Exit", font=("Times new roman",10,"bold"),bg="#f26b8a", fg="black", height=3, width=12, bd=4, command=iExit)
        self.btnExit.grid(row=1, column=2,padx=15, pady=15)
        self.btnExit.place(x=740,y=10)

        #============================================================DETAIL FRAME====================================================#
        
        self.lblSearch = Label(DetailFrame, font=('Times new roman',15,'bold'),text="Search by ID:", padx=2, pady=2,bg="#FFC0CB", fg="black", height=1, width=12)
        self.lblSearch.grid(row=1, column=0,padx=2,pady=2, sticky="w")
        self.lblSearch.place(x=50,y=30)
        
        self.Search = Entry(DetailFrame, font=('Times new roman',15,'normal'),textvariable=Searchbar, relief=GROOVE, width=20, bg="#f26b8a", fg="black")
        self.Search.grid(row=1, column=1)
        self.Search.place(x=220,y=30)

        self.btnSearch = Button(DetailFrame, text="Search",font=("Times new roman",12,"bold"),bg="#f26b8a", fg="black", height=1, width=12, bd=4, command=searchStd)
        self.btnSearch.grid(row=1, column=2,padx=15, pady=15)
        self.btnSearch.place(x=480,y=25)
        
        self.btnDisplayData = Button(DetailFrame, text="Select", font=("Times new roman",12,"bold"),bg="#f26b8a", fg="black", height=1, width=12, bd=4,command=editStd)
        self.btnDisplayData.grid(row=1, column=3, padx=15, pady=15)
        self.btnDisplayData.place(x=650,y=25)
        
        TableFrame=Frame(DetailFrame, bd=4,relief=RIDGE,bg='#ecc19c')
        TableFrame.place(x=20,y=80, width=790, height=400)

        scroll_y=Scrollbar(TableFrame, orient=VERTICAL)

        tree = ttk.Treeview(TableFrame, height=10, columns=("StudID","LastName","FirstName","MiddleName","Gender","YearLevel","Course"), yscrollcommand=scroll_y.set)
        
        scroll_y.pack(side=LEFT, fill=Y)

        tree.heading("StudID", text="Student ID")
        tree.heading("LastName", text="Last Name")
        tree.heading("FirstName", text="First Name")
        tree.heading("MiddleName", text="Middle Initial")
        tree.heading("Gender", text="Gender")
        tree.heading("YearLevel", text="Year Level")
        tree.heading("Course", text="Course")
        tree['show'] = 'headings'

        tree.column("StudID", width=110,anchor='center')
        tree.column("LastName", width=110,anchor='center')
        tree.column("FirstName", width=110,anchor='center')
        tree.column("MiddleName", width=130,anchor='center')
        tree.column("Gender", width=90,anchor='center')
        tree.column("YearLevel", width=120,anchor='center')
        tree.column("Course", width=100,anchor='center')
        tree.pack(fill=BOTH,expand=1,anchor='center')
        
        DisplayStd()

        
        #===========================================================================================================================================================#
    def saveData(self):
        temps = []
        with open('StudentData.csv', "w", newline ='') as update:
            fieldnames = ["Student ID","Last Name","First Name","Middle Name","Gender","Year Level","Course"]
            writer = csv.DictWriter(update, fieldnames=fieldnames, lineterminator='\n')
            writer.writeheader()
            for id, val in self.data.items():
                temp ={"Student ID": id}
                for key, value in val.items():
                    temp[key] = value
                temps.append(temp)
            writer.writerows(temps)
            

if __name__ =='__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()
