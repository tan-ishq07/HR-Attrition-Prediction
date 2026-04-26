import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns

# ================= LOAD DATA =================
data = pd.read_csv(r"C:\Users\tanis\Downloads\WA_Fn-UseC_-HR-Employee-Attrition.csv")

# ================= MAIN WINDOW =================
root = tk.Tk()
root.title("Employee Attrition Analytics Dashboard")
root.geometry("1200x700")
root.configure(bg="#f4f6f9")

# ================= SIDEBAR =================
sidebar = tk.Frame(root, bg="#1e293b", width=200)
sidebar.pack(side="left", fill="y")

title = tk.Label(sidebar, text="HR Analytics", fg="white", bg="#1e293b", font=("Arial", 16, "bold"))
title.pack(pady=20)

# ================= MAIN AREA =================
main_frame = tk.Frame(root, bg="#f4f6f9")
main_frame.pack(side="right", expand=True, fill="both")

# ================= HEADER =================
header = tk.Label(main_frame, text="Employee Attrition Dashboard",
                  font=("Arial", 20, "bold"), bg="#f4f6f9")
header.pack(pady=10)

# ================= CARD FRAME =================
card_frame = tk.Frame(main_frame, bg="#f4f6f9")
card_frame.pack(pady=10)

def create_card(parent, text, value):
    frame = tk.Frame(parent, bg="white", width=200, height=100, bd=1, relief="solid")
    frame.pack(side="left", padx=10)
    label1 = tk.Label(frame, text=text, bg="white", font=("Arial", 10))
    label1.pack(pady=5)
    label2 = tk.Label(frame, text=value, bg="white", font=("Arial", 16, "bold"))
    label2.pack()

# ================= METRICS =================
create_card(card_frame, "Total Rows", data.shape[0])
create_card(card_frame, "Total Columns", data.shape[1])
create_card(card_frame, "Attrition Yes %", round((data['Attrition']=="Yes").mean()*100,2))

# ================= GRAPH AREA =================
graph_frame = tk.Frame(main_frame, bg="#f4f6f9")
graph_frame.pack(fill="both", expand=True)

def clear_graph():
    for widget in graph_frame.winfo_children():
        widget.destroy()

# ================= GRAPH FUNCTIONS =================
def show_attrition_plot():
    clear_graph()
    fig, ax = plt.subplots(figsize=(5,4))
    sns.countplot(x='Attrition', data=data, ax=ax)
    ax.set_title("Attrition Distribution")

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

def show_heatmap():
    clear_graph()
    fig, ax = plt.subplots(figsize=(6,5))
    sns.heatmap(data.select_dtypes(include='number').corr(), cmap="coolwarm", ax=ax)
    ax.set_title("Correlation Heatmap")

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

def show_boxplot():
    clear_graph()
    fig, ax = plt.subplots(figsize=(5,4))
    sns.boxplot(x='Attrition', y='MonthlyIncome', data=data, ax=ax)
    ax.set_title("Income vs Attrition")

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

def show_histogram():
    clear_graph()
    fig, ax = plt.subplots(figsize=(5,4))
    sns.histplot(data['Age'], kde=True, ax=ax)
    ax.set_title("Age Distribution")

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# ================= SIDEBAR BUTTONS =================
def add_button(text, command):
    btn = tk.Button(sidebar, text=text, fg="white", bg="#334155",
                    relief="flat", command=command)
    btn.pack(fill="x", pady=5, padx=10)

add_button("Overview", show_attrition_plot)
add_button("Heatmap", show_heatmap)
add_button("Boxplot", show_boxplot)
add_button("Histogram", show_histogram)

# ================= RUN =================
root.mainloop()