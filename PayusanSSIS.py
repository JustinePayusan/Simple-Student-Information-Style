from tkinter import*
from tkinter import ttk
import tkinter.ttk as ttk
import tkinter.messagebox
import os
import csv

class StudentInformationSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Information System")
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#FFC0CB")
        self.root.resizable(False,False)
        self.data=dict()
        self.temp=dict()
        self.filename="StudentData.csv"

        StudentID= StringVar()
        Surname = StringVar()
        Firstname = StringVar()
        Middlename = StringVar()
        Gender = StringVar()
        Yearlevel = StringVar()
        Course = StringVar()
        Searchbar=StringVar()
        

        title=Label(self.root, text = "MSU-IIT STUDENT INFORMATION SYSTEM",bd=4,relief=RIDGE, font=("Palatino Linotype",40,"bold"),bg="#f25278", fg="white")
        title.pack(side=TOP, fill=X)
        
        if not os.path.exists(self.filename):
            with open('StudentData.csv',mode = 'w') as csv_file:
                fieldnames = ["StudentID", "Surname", "Firstname", "Middlename", "Gender", "Course", "Yearlevel"]
                writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
                writer.writeheader()
        else:
            with open('StudentData.csv', newline='') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    self.data[row["StudentID"]] = {'Surname': row["Surname"], 'Firstname': row["Firstname"], 'Middlename': row["Middlename"],'Gender': row["Gender"], 'Course': row["Course"],'Yearlevel': row["Yearlevel"] }
            self.temp = self.data.copy()
            

        #======Functions========

        def iExit():
            iExit = tkinter.messagebox.askyesno("Student Information System","Do you want to exit?")
            if iExit > 0:
                root.destroy()
                return
            
        
        def addData():
            with open('Studentdata.csv', "a", newline="") as file:
                csvfile = csv.writer(file)
                if StudentID.get()=="" or Surname.get()=="" or Firstname.get()=="" or  Yearlevel.get()=="":
                    tkinter.messagebox.showinfo("Student Information System","Please fill in the box.")
                else:
                    ID = StudentID.get()
                    ID_list = []
                    for i in ID:
                        ID_list.append(i)
                    if "-" in ID_list:
                        x = ID.split("-")
                        y = x[0]
                        n = x[1]
                        if y.isdigit()==False or n.isdigit()==False:
                            try:
                                tkinter.messagebox.showerror("Student Information System", "INVALID ID Number")
                            except:
                                pass
                        elif y==" " or n==" ":
                            try:
                                tkinter.messagebox.showerror("Student Information System", "INVALID ID Number")
                            except:
                                pass
                        else:
                            if ID in self.data:
                                tkinter.messagebox.showinfo("Student Information System","StudentID already exist")
                            else:
                                self.data[StudentID.get()] = { 'Surname': Surname.get(), 'Firstname': Firstname.get(), 'Middlename': Middlename.get(), 'Gender': Gender.get(), 'Course': Course.get(),'Yearlevel': Yearlevel.get() }
                                self.saveData()
                                tkinter.messagebox.showinfo("Student Information System", "Student Information: Recorded Successfully")
                                Clear()
                    else:
                        tkinter.messagebox.showerror("Student Information System", "INVALID ID Number")      
                displayData()

    
        def Clear():
            StudentID.set("")
            Surname.set("")
            Firstname.set("")
            Midname.set("")
            Gender.set("")
            Yearlevel.set("")
            Course.set("")

        def displayData():
            tree.delete(*tree.get_children())
            with open('StudentData.csv') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    StudentID=row['StudentID']
                    Surname=row['Surname']
                    Firstname=row['Firstname']
                    Middlename=row['Middlename']
                    Gender=row['Gender']
                    Yearlevel=row['Yearlevel']
                    Course=row['Course']
                    tree.insert("",0, values=(StudentID, Firstname, Middlename, Surname,Course, Yearlevel, Gender))
                    
        def search():
            if self.Search.get() in self.data:
                vals = list(self.data[self.Search.get()].values())
                tree.delete(*tree.get_children())
                tree.insert("",0, values=(self.Search.get(), vals[0],vals[1],vals[2],vals[3],vals[4],vals[5]))
            elif self.Search.get() == "":
                displayData()
            else:
                tkinter.messagebox.showerror("Student Information System","Student's Information not found")
                return

        def delete():
            if tree.focus()=="":
                tkinter.messagebox.showerror("Student Information System","Please select the studen's' information you want to delete")
                return
            id_no = tree.item(tree.focus(),"values")[0]
            
            self.data.pop(id_no, None)
            self.saveData()
            tree.delete(tree.focus())
            tkinter.messagebox.showinfo("Student Information System","Student's Information Deleted Successfully")
            displayData()

        def editData():
            if tree.focus() == "":
                tkinter.messagebox.showerror("Student Information System", "Please select the student's information you want to edit")
                return
            values = tree.item(tree.focus(), "values")
            StudentID.set(values[0])
            Surname.set(values[1])
            Firstname.set(values[2])
            Midname.set(values[3])
            Gender.set(values[4])
            Course.set(values[5])
            Yearlevel.set(values[6])
           
       
       
        def updateData():
            with open('StudentData.csv', "a", newline="") as file:
                csvfile = csv.writer(file)
                if StudentID.get()=="" or Firstname.get()=="" or Surname.get()=="" or Course.get()=="" or Yearlevel.get()=="":
                    tkinter.messagebox.showinfo("Student Information System","Please select the student's information you want to update")
                else:
                    self.data[StudentID.get()] = {'Surname': Surname.get(), 'Firstname': Firstname.get(), 'Middlename': Middlename.get(), 'Gender': Gender.get() , 'Course': Course.get(),'Yearlevel': Yearlevel.get()}
                    self.saveData()
                    tkinter.messagebox.showinfo("Student Information System", "Successfully Updated")
                Clear()
                displayData()     
        
            
            
                        
         
                
        #-------------Frames---------#
        ManageFrame=Frame(self.root, bd=4, relief =RIDGE, bg="#FFC0CB")
        ManageFrame.place(x=20, y=100,width=450, height=560)
        
        DetailFrame=Frame(self.root, bd=4, relief =RIDGE, bg="#FFC0CB")
        DetailFrame.place(x=500, y=100,width=830, height=560)

        ButtonFrame=Frame(ManageFrame, bd=4, relief=RIDGE, bg="#FFC0CB")
        ButtonFrame.place(x=10,y=410, width=420, height=130)

        #-------------Labels and Entry Widgets ---------#

        title=Label(ManageFrame, text="STUDENT'S INFORMATION",bg="#FFC0CB", fg="Black", font=("Palatino Linotype",20,"bold"))
        title.grid(row=0, columnspan=2, pady=20)
        
        self.lblStdID = Label(ManageFrame, font=("Palatino Linotype",15,"bold"),text="ID Number:", padx=2, pady=2, bg="#f25278", fg="white")
        self.lblStdID.grid(row=1, column=0,padx=5,pady=5, sticky="w")
        self.txtStdID = Entry(ManageFrame, font=("Palatino Linotype",13,"normal"),textvariable=StudentID, relief=GROOVE, width=31)
        self.txtStdID.grid(row=1, column=1)
        self.txtStdID.insert(0, "YYYY-NNNN")
        self.txtStdID.grid(row=1, column=1)

        self.lblSurname = Label(ManageFrame, font=("Palatino Linotype",15,"bold"),text="Surname:", padx=2, pady=2, bg="#f25278", fg="white")
        self.lblSurname.grid(row=2, column=0,padx=5,pady=5, sticky="w")
        self.txtSurname = Entry(ManageFrame, font=("Palatino Linotype",13,"normal"),textvariable=Surname, relief=GROOVE,width=31)
        self.txtSurname.grid(row=2, column=1)

        self.lblFirstname = Label(ManageFrame,font=("Palatino Linotype",15,"bold"),text="First Name:", padx=2, pady=2, bg="#f25278", fg="white")
        self.lblFirstname.grid(row=3, column=0,padx=5,pady=5, sticky="w")
        self.txtFirstname = Entry(ManageFrame, font=("Palatino Linotype",13,"normal"),textvariable=Firstname, relief=GROOVE,width=31)
        self.txtFirstname.grid(row=3, column=1)
        
        self.lblMiddlename = Label(ManageFrame, font=("Palatino Linotype",15,"bold"),text="Middle Initial:", padx=2, pady=2, bg="#f25278", fg="white")
        self.lblMiddlename.grid(row=4, column=0,padx=5,pady=5, sticky="w")
        self.txtMiddlename = Entry(ManageFrame, font=("Palatino Linotype",13,"normal"),textvariable=Middlename, relief=GROOVE,width=31)
        self.txtMiddlename.grid(row=4, column=1)

        self.lblGender = Label(ManageFrame, font=("Palatino Linotype",15,"bold"),text="Gender:", padx=2, pady=2, bg="#f25278", fg="white")
        self.lblGender.grid(row=5, column=0,padx=5,pady=5, sticky="w")
        self.comboGender=ttk.Combobox(ManageFrame,font=("Palatino Linotype",13,"normal"), state="readonly",width=29, textvariable=Gender)
        self.comboGender['values']=("Male", "Female")
        self.comboGender.grid(row=5,column=1)

        self.lblYearlevel = Label(ManageFrame, font=("Palatino Linotype",15,"bold"),text="Year Level:", padx=2, pady=2, bg="#f25278", fg="white")
        self.lblYearlevel.grid(row=6, column=0,padx=5,pady=5, sticky="w")
        self.comboYearlevel=ttk.Combobox(ManageFrame,font=("Palatino Linotype",13,"normal"), state="readonly",width=29, textvariable=Yearlevel)
        self.comboYearlevel['values']=("First Year","Second Year", "Third Year", "Fourth Year", "Fifth Year")
        self.comboYearlevel.grid(row=6,column=1)

        self.lblCourse = Label(ManageFrame, font=("Palatino Linotype",15,"bold"),text="Course:", padx=2, pady=2, bg="#f25278", fg="white")
        self.lblCourse.grid(row=7, column=0,padx=5,pady=5, sticky="w")
        self.txtCourse = Entry(ManageFrame, font=("Palatino Linotype",13,"normal"),textvariable=Course, relief=GROOVE,width=31)
        self.txtCourse.grid(row=7, column=1)

        #-------------Button Widget---------#

        self.btnAddData = Button(ButtonFrame, text="Add", font=("Palatino Linotype",10,"bold"),bg="#f26b8a", fg="black", height=1, width=12, bd=4,command=addData)
        self.btnAddData.grid(row=0, column=0, padx=15, pady=15)

        self.btnUpdateData = Button(ButtonFrame, text="Update", font=("Palatino Linotype",10,"bold"),bg="#f26b8a", fg="black", height=1, width=12, bd=4, command=updateData)
        self.btnUpdateData.grid(row=0, column=2, padx=15, pady=15)

        self.btnClearData = Button(ButtonFrame, text="Clear", font=("Palatino Linotype",10,"bold"),bg="#f26b8a", fg="black", height=1, width=12, bd=4,command=Clear)
        self.btnClearData.grid(row=1, column=0,padx=15, pady=15)

        self.btnExit = Button(ButtonFrame, text="Exit", font=("Palatino Linotype",10,"bold"),bg="#f26b8a", fg="black", height=1, width=12, bd=4, command=iExit)
        self.btnExit.grid(row=1, column=1,padx=15, pady=15)

        self.btnDeleteData = Button(ButtonFrame, text="Delete", font=("Palatino Linotype",10,"bold"),bg="#f26b8a", fg="black", height=1, width=12, bd=4, command=delete)
        self.btnDeleteData.grid(row=1, column=2,padx=15, pady=15)

        #-------------Detail Frame ---------#
        self.lblSearch = Label(DetailFrame, font=('Palatino Linotype',10,'bold'),text="Search (ID Number)", padx=2, pady=2, bg="#FFC0CB", fg="black")
        self.lblSearch.grid(row=1, column=0,padx=5,pady=5, sticky="w")
        self.Search = Entry(DetailFrame, font=('Palatino Linotype',10,'normal'),textvariable=Searchbar, relief=GROOVE,width=25)
        self.Search.grid(row=1, column=1)

        self.btnSearch = Button(DetailFrame, text="Search",font=("Palatino Linotype",10,"bold"),bg="#f26b8a", fg="black", height=1, width=12, bd=4, command=search)
        self.btnSearch.grid(row=1, column=2,padx=15, pady=15)
        
        self.btnDisplayData = Button(DetailFrame, text="Select", font=("Palatino Linotype",10,"bold"),bg="#f26b8a", fg="black", height=1, width=12, bd=4,command=editData)
        self.btnDisplayData.grid(row=1, column=3, padx=15, pady=15)
        
        TableFrame=Frame(DetailFrame, bd=4,relief=RIDGE,bg='#ecc19c')
        TableFrame.place(x=10,y=80, width=790, height=450)

        scroll_y=Scrollbar(TableFrame, orient=VERTICAL)

        tree = ttk.Treeview(TableFrame, height=10, columns=("StudentID","Firstname","Middlename","Surname","Course","Yearlevel","Gender"), yscrollcommand=scroll_y.set)

        scroll_y.pack(side=RIGHT, fill=Y)

        tree.heading("StudentID", text="Student ID")
        tree.heading("Surname", text="Surname")
        tree.heading("Firstname", text="First Name")
        tree.heading("Middlename", text="Middle Initial")
        tree.heading("Gender", text="Gender")
        tree.heading("Course", text="Course")
        tree.heading("Yearlevel", text="Year Level")
        tree['show'] = 'headings'

        tree.column("StudentID", width=70)
        tree.column("Surname", width=100)
        tree.column("Firstname", width=100)
        tree.column("Middlename", width=70)
        tree.column("Gender", width=70)
        tree.column("Course", width=120)
        tree.column("Yearlevel", width=70)
        tree.pack(fill=BOTH,expand=1)

        displayData()

    def saveData(self):
        temps = []
        with open('StudentData.csv', "w", newline ='') as update:
            fieldnames = ["StudentID","Surname","Firstname","Middlename","Gender","Course","YearLevel"]
            writer = csv.DictWriter(update, fieldnames=fieldnames, lineterminator='\n')
            writer.writeheader()
            for id, val in self.data.items():
                temp ={"StudentID": id}
                for key, value in val.items():
                    temp[key] = value
                temps.append(temp)
            writer.writerows(temps)

        
        


if __name__=='__main__':
    root = Tk()
    application = StudentInformationSystem(root)
    root.mainloop()
