from tkinter import *
from tkinter import ttk, messagebox
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ================= GLOBAL DICT =================
fields_dict = {}

# ================= FUNCTION =================
def get_entry_data():
    try:
        # -------- INPUTS --------
        age = int(fields_dict["Age"].get())

        business_travel = {
            "Non Travel":0,
            "Travel Frequently":1,
            "Travel Rarely":2
        }[fields_dict["Business Travel"].get()]

        daily_rate = int(fields_dict["Daily Rate"].get())

        dept = {
            "Human Resources":0,
            "Research & Development":1,
            "Sales":2
        }[fields_dict["Department"].get()]

        dist_home = int(fields_dict["Distance From Home"].get())
        education = int(fields_dict["Education (1-5)"].get())

        edu_field = {
            "Human Resources":0,
            "Life Sciences":1,
            "Marketing":2,
            "Medical":3,
            "Other":4
        }[fields_dict["Education Field"].get()]

        env_sat = int(fields_dict["Environment Satisfaction (1-5)"].get())

        gender = {
            "Female":0,
            "Male":1
        }[fields_dict["Gender"].get()]

        hourly_rate = int(fields_dict["Hourly Rate"].get())
        job_inv = int(fields_dict["Job Involvement (1-5)"].get())
        job_level = int(fields_dict["Job Level (1-5)"].get())

        job_role = {
            "Health Care Representative":0,
            "Human Resources":1,
            "Laboratory Technician":2,
            "Manager":3,
            "Manufacturing Director":4,
            "Research Director":5,
            "Research Scientist":6,
            "Sales Executive":7
        }[fields_dict["Job Role"].get()]

        job_sat = int(fields_dict["Job Satisfaction (1-5)"].get())

        martital = {
            "Single":0,
            "Divorced":1,
            "Married":2
        }[fields_dict["Marital Status"].get()]

        monthly_income = int(fields_dict["Monthly Income"].get())
        monthly_rate = int(fields_dict["Monthly Rate"].get())
        num_companies = int(fields_dict["Num Companies Worked"].get())

        over_time = {
            "No":0,
            "Yes":1
        }[fields_dict["Over Time"].get()]

        percent_hike = int(fields_dict["Percent Salary Hike"].get())
        performance_rating = int(fields_dict["Performance Rating"].get())
        relationship_sat = int(fields_dict["Relationship Satisfaction (1-5)"].get())
        total_work_years = int(fields_dict["Total Working Years"].get())
        training_times = int(fields_dict["Training Times Last Year"].get())
        work_life_balance = int(fields_dict["Work Life Balance (1-5)"].get())
        years_at_company = int(fields_dict["Years At Company"].get())
        years_in_role = int(fields_dict["Years In Current Role"].get())
        years_since_promo = int(fields_dict["Years Since Last Promotion"].get())
        years_with_manager = int(fields_dict["Years With Current Manager"].get())

        input_data = [[
            age, business_travel, daily_rate, dept, dist_home,
            education, edu_field, env_sat, gender, hourly_rate,
            job_inv, job_level, job_role, job_sat, martital,
            monthly_income, monthly_rate, num_companies, over_time,
            percent_hike, performance_rating, relationship_sat,
            total_work_years, training_times, work_life_balance,
            years_at_company, years_in_role, years_since_promo,
            years_with_manager
        ]]

        # -------- MODEL --------
        data = pd.read_csv('Datasets/WA_Fn-UseC_-HR-Employee-Attrition.csv')
        data = data.drop(columns=['StandardHours','EmployeeCount','Over18','EmployeeNumber','StockOptionLevel'])

        from sklearn.preprocessing import LabelEncoder
        le = LabelEncoder()
        for col in ['Attrition','BusinessTravel','Department','EducationField','Gender','JobRole','MaritalStatus','OverTime']:
            data[col] = le.fit_transform(data[col])

        X = data.drop('Attrition', axis=1)
        y = data['Attrition']

        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.33,random_state=42)

        from sklearn.linear_model import LogisticRegression
        model = LogisticRegression(max_iter=1000)
        model.fit(X_train,y_train)

        result = model.predict(input_data)
        prob = model.predict_proba(input_data)[0]
        accuracy = round(model.score(X_test,y_test)*100,2)

        # -------- RESULT --------
        if result[0] == 0:
            risk = "LOW RISK"
            msg = "Employee will STAY"
        else:
            risk = "HIGH RISK"
            msg = "Employee may LEAVE"

        messagebox.showinfo("Result", f"{msg}\nRisk: {risk}\nAccuracy: {accuracy}%")

        # -------- GRAPH --------
        plt.figure()
        plt.bar(["Stay","Leave"], prob)
        plt.title("Attrition Probability")
        plt.ylabel("Probability")
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ================= GUI =================
gui = Tk()
gui.title("HR Attrition Prediction System")
gui.geometry("720x750")
gui.configure(bg="#eef2f7")

canvas = Canvas(gui, bg="#eef2f7", highlightthickness=0)
scrollbar = Scrollbar(gui, orient="vertical", command=canvas.yview)
main_frame = Frame(canvas, bg="#eef2f7")

main_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0,0), window=main_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Header
Label(main_frame, text="Employee Attrition Prediction System",
      font=("Segoe UI",16,"bold"),
      bg="#eef2f7").pack(pady=10)

def create_section(title):
    frame = Frame(main_frame, bg="white", bd=1, relief=RIDGE, padx=10, pady=10)
    frame.pack(fill=X, padx=15, pady=10)

    Label(frame, text=title,
          font=("Segoe UI",12,"bold"),
          bg="white").grid(row=0,column=0,columnspan=2,sticky=W)

    return frame

def add_field(frame,row,text,values=None):
    Label(frame,text=text,bg="white").grid(row=row,column=0,sticky=W,pady=3)

    if values:
        e = ttk.Combobox(frame, values=values)
    else:
        e = Entry(frame)

    e.grid(row=row,column=1,pady=3)
    fields_dict[text] = e


# ===== SECTIONS =====
sec1 = create_section("Personal Information")
add_field(sec1,1,"Age")
add_field(sec1,2,"Business Travel",["Non Travel","Travel Frequently","Travel Rarely"])
add_field(sec1,3,"Daily Rate")
add_field(sec1,4,"Department",["Human Resources","Research & Development","Sales"])
add_field(sec1,5,"Distance From Home")
add_field(sec1,6,"Gender",["Male","Female"])
add_field(sec1,7,"Marital Status",["Single","Married","Divorced"])

sec2 = create_section("Education")
add_field(sec2,1,"Education (1-5)")
add_field(sec2,2,"Education Field",["Human Resources","Life Sciences","Marketing","Medical","Other"])

sec3 = create_section("Job Details")
add_field(sec3,1,"Job Role",[
"Health Care Representative","Human Resources","Laboratory Technician",
"Manager","Manufacturing Director","Research Director",
"Research Scientist","Sales Executive"])
add_field(sec3,2,"Job Level (1-5)")
add_field(sec3,3,"Job Involvement (1-5)")
add_field(sec3,4,"Job Satisfaction (1-5)")
add_field(sec3,5,"Hourly Rate")

sec4 = create_section("Salary")
add_field(sec4,1,"Monthly Income")
add_field(sec4,2,"Monthly Rate")
add_field(sec4,3,"Percent Salary Hike")

sec5 = create_section("Work Experience")
add_field(sec5,1,"Total Working Years")
add_field(sec5,2,"Years At Company")
add_field(sec5,3,"Years In Current Role")
add_field(sec5,4,"Years Since Last Promotion")
add_field(sec5,5,"Years With Current Manager")
add_field(sec5,6,"Num Companies Worked")

sec6 = create_section("Performance & Satisfaction")
add_field(sec6,1,"Environment Satisfaction (1-5)")
add_field(sec6,2,"Relationship Satisfaction (1-5)")
add_field(sec6,3,"Work Life Balance (1-5)")
add_field(sec6,4,"Performance Rating")
add_field(sec6,5,"Training Times Last Year")
add_field(sec6,6,"Over Time",["Yes","No"])

# Button
Button(main_frame,
       text="Predict Attrition",
       bg="#27ae60",
       fg="white",
       font=("Segoe UI",12,"bold"),
       command=get_entry_data).pack(pady=20)

gui.mainloop()