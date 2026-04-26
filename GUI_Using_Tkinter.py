from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import numpy as np


business_travel=3
dept=3
edu_field=3
gender=3
job_role=3
martital=3
over_time=3


def get_entry_data():
    import numpy as np
    import pandas as pd
    from tkinter import messagebox

    age = int(el1.get())

    if el2.get() == "Non Travel":
        business_travel = 0
    elif el2.get() == "Travel Frequently":
        business_travel = 1
    else:
        business_travel = 2

    daily_rate = int(el3.get())

    if el4.get() == "Human Resources":
        dept = 0
    elif el4.get() == "Research & Development":
        dept = 1
    else:
        dept = 2

    dist_home = int(el5.get())
    education = int(el6.get())

    if el7.get() == "Human Resources":
        edu_field = 0
    elif el7.get() == "Life Sciences":
        edu_field = 1
    elif el7.get() == "Marketing":
        edu_field = 2
    elif el7.get() == "Medical":
        edu_field = 3
    else:
        edu_field = 4

    Environment_satification = int(el8.get())

    if el9.get() == "Female":
        gender = 0
    else:
        gender = 1

    Hourly_rate = int(el10.get())
    job_invol = int(el11.get())
    job_level = int(el12.get())

    if el13.get() == "Health Care Representative":
        job_role = 0
    elif el13.get() == "Human Resources":
        job_role = 1
    elif el13.get() == "Laboratory Technician":
        job_role = 2
    elif el13.get() == "Manager":
        job_role = 3
    elif el13.get() == "Manufacturing Director":
        job_role = 4
    elif el13.get() == "Research Director":
        job_role = 5
    elif el13.get() == "Research Scientist":
        job_role = 6
    else:
        job_role = 7

    job_satisifaction = int(el14.get())

    if el15.get() == "Single":
        martital = 0
    elif el15.get() == "Divorced":
        martital = 1
    else:
        martital = 2

    monthly_income = int(el16.get())
    monthly_rate = int(el17.get())
    num_company = int(el18.get())

    if el19.get() == "No":
        over_time = 0
    else:
        over_time = 1

    salary_hike = int(el20.get())
    performance_rate = int(el21.get())
    relationship_satisfaction = int(el22.get())
    total_work_years = int(el23.get())
    training_time = int(el24.get())
    work_life_bal = int(el25.get())
    year_at_company = int(el26.get())
    year_in_role = int(el27.get())
    last_promotion = int(el28.get())
    current_manager = int(el29.get())

    # Prepare input
    input_data = [[
        age, business_travel, daily_rate, dept, dist_home,
        education, edu_field, Environment_satification, gender, Hourly_rate,
        job_invol, job_level, job_role, job_satisifaction, martital,
        monthly_income, monthly_rate, num_company, over_time,
        salary_hike, performance_rate, relationship_satisfaction,
        total_work_years, training_time, work_life_bal,
        year_at_company, year_in_role, last_promotion,
        current_manager
    ]]

    # Load dataset
    data = pd.read_csv('Datasets/WA_Fn-UseC_-HR-Employee-Attrition.csv')
    data = data.drop(columns=['StandardHours','EmployeeCount','Over18','EmployeeNumber','StockOptionLevel'])

    from sklearn import preprocessing
    le = preprocessing.LabelEncoder()
    categorical = ['Attrition','BusinessTravel','Department','EducationField','Gender','JobRole','MaritalStatus','OverTime']
    
    for col in categorical:
        data[col] = le.fit_transform(data[col])

    X = data.drop('Attrition', axis=1)
    y = data['Attrition']

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Prediction
    result = model.predict(input_data)

    if result[0] == 0:
        messagebox.showinfo("Result", "Employee will STAY")
    else:
        messagebox.showinfo("Result", "Employee may LEAVE")
gui = Tk()

gui.title('HR ANALYSIS OF EMPLOYEE ATTRITION GUI')
gui.geometry('600x700')
gui.configure(background="light blue")

class TableDropDown(ttk.Combobox):
    def __init__(self, parent):
        self.current_table = tk.StringVar() # create variable for table
        ttk.Combobox.__init__(self, parent)#  init widget
        self.config(textvariable = self.current_table, state = "readonly", values = ["Customers", "Pets", "Invoices", "Prices"])
        self.current(0) # index of values for current table
        self.place(x = 50, y = 50, anchor = "w") # place drop down box 

l1=Label(gui, text='Enter Age')
l1.grid(row=0, column=0,padx=10,pady=2)
el1 = Entry(gui)
el1.grid(row=0, column=1)

l2=Label(gui, text='Business travel:')
l2.grid(row=2, column=0,padx=10,pady=2)
el2 = ttk.Combobox(gui, width="18", values=("Non Travel","Travel Frequently","Travel Rarely"))
el2.grid(row=2, column=1)

l3=Label(gui, text='Enter Daily Rate')
l3.grid(row=3, column=0,padx=10,pady=2)
el3 = Entry(gui)
el3.grid(row=3, column=1)

l4=Label(gui, text='Enter Department')
l4.grid(row=4, column=0,padx=10,pady=2)
el4 = ttk.Combobox(gui, width="18", values=("Human Resources","Research & Development","Sales"))
el4.grid(row=4, column=1)

l5=Label(gui, text='Enter Distance From Home')
l5.grid(row=5, column=0,padx=10,pady=2)
el5 = Entry(gui)
el5.grid(row=5, column=1)

l6=Label(gui, text='Enter Education(Rating out of 5)')
l6.grid(row=6, column=0,padx=10,pady=2)
el6 = Entry(gui)
el6.grid(row=6, column=1)

l7=Label(gui, text='Enter Education Field')
l7.grid(row=7, column=0,padx=10,pady=2)
el7 = ttk.Combobox(gui, width="18", values=("Human Resources","Life Sciences","Marketing","Medical","Other"))
el7.grid(row=7, column=1)

l8=Label(gui, text='Enter Environment Satisfaction(Rating out of 5)')
l8.grid(row=8, column=0,padx=10,pady=2)
el8 = Entry(gui)
el8.grid(row=8, column=1)

l9=Label(gui, text='Enter Gender')
l9.grid(row=9, column=0,padx=10,pady=2)
el9 = ttk.Combobox(gui, width="18", values=("Female","Male"))
el9.grid(row=9, column=1)

l10=Label(gui, text='Enter Hourly Rate')
l10.grid(row=10, column=0,padx=10,pady=2)
el10 = Entry(gui)
el10.grid(row=10, column=1)

l11=Label(gui, text='Enter Job Involvement(Rating out of 5)')
l11.grid(row=11, column=0,padx=10,pady=2)
el11 = Entry(gui)
el11.grid(row=11, column=1)

l12=Label(gui, text='Enter Job Level(Rating out of 5)')
l12.grid(row=12, column=0,padx=10,pady=2)
el12 = Entry(gui)
el12.grid(row=12, column=1)

l13=Label(gui, text='Enter Job Role')
l13.grid(row=13, column=0,padx=10,pady=2)
el13 = ttk.Combobox(gui, width="18", values=("Health Care Representative","Human Resources","Laboratory Technician","Manager","Manufacturing Director","Research Director","Research Scientist","Sales Executive"))
el13.grid(row=13, column=1)

l14=Label(gui, text='Enter Job Satisfaction(Out of 5)')
l14.grid(row=14, column=0,padx=10,pady=2)
el14 = Entry(gui)
el14.grid(row=14, column=1)

l15=Label(gui, text='Enter Marital Status')
l15.grid(row=15, column=0,padx=10,pady=2)
el15 = ttk.Combobox(gui, width="18", values=("Single","Divorced","Married"))
el15.grid(row=15, column=1)

l16=Label(gui, text='Enter Monthly Income')
l16.grid(row=16, column=0,padx=10,pady=2)
el16 = Entry(gui)
el16.grid(row=16, column=1)

l17=Label(gui, text='Enter Monthly Rate')
l17.grid(row=17, column=0,padx=10,pady=2)
el17 = Entry(gui)
el17.grid(row=17, column=1)

l18=Label(gui, text='Enter Num Companies Worked')
l18.grid(row=18, column=0,padx=10,pady=2)
el18 = Entry(gui)
el18.grid(row=18, column=1)

l19=Label(gui, text='Enter OverTime')
l19.grid(row=19, column=0,padx=10,pady=2)
el19 = ttk.Combobox(gui, width="18", values=("No","Yes"))
el19.grid(row=19, column=1)

l20=Label(gui, text='Enter Percent Salary Hike(Out of 100)')
l20.grid(row=20, column=0,padx=10,pady=2)
el20 = Entry(gui)
el20.grid(row=20, column=1)

l21=Label(gui, text='Enter Performance Rating(Out of 5)')
l21.grid(row=21, column=0,padx=10,pady=2)
el21 = Entry(gui)
el21.grid(row=21, column=1)

l22=Label(gui, text='Enter Relationship Satisfaction(Out of 5)')
l22.grid(row=22, column=0,padx=10,pady=2)
el22 = Entry(gui)
el22.grid(row=22, column=1)

l23=Label(gui, text='Enter Total Working Years')
l23.grid(row=23, column=0,padx=10,pady=2)
el23 = Entry(gui)
el23.grid(row=23, column=1)

l24=Label(gui, text='Enter Training Times Last Year')
l24.grid(row=24, column=0,padx=10,pady=2)
el24 = Entry(gui)
el24.grid(row=24, column=1)

l25=Label(gui, text='Enter Work Life Balance(Out of 5)')
l25.grid(row=25, column=0,padx=10,pady=2)
el25 = Entry(gui)
el25.grid(row=25, column=1)

l26=Label(gui, text='Enter Years At Company')
l26.grid(row=26, column=0,padx=10,pady=2)
el26 = Entry(gui)
el26.grid(row=26, column=1)

l27=Label(gui, text='Enter Years In Current Role')
l27.grid(row=27, column=0,padx=10,pady=2)
el27 = Entry(gui)
el27.grid(row=27, column=1)

l28=Label(gui, text='Enter Years Since Last Promotion')
l28.grid(row=28, column=0,padx=10,pady=2)
el28 = Entry(gui)
el28.grid(row=28, column=1)

l29=Label(gui, text='Enter Years With Current Manager')
l29.grid(row=29, column=0,padx=10,pady=2)
el29 = Entry(gui)
el29.grid(row=29, column=1)

action_button = Button(gui)
action_button.configure(text='Submit',fg="black",bg="light green", command=get_entry_data)
action_button.grid(row=30, column=1,padx=10,pady=2)

gui.mainloop()
