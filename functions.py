import sqlite3
from datetime import date
today = date.today()
con = sqlite3.connect("data.db")
cur = con.cursor()

def success():
    print("has been created successfully!")
    
def create_data(projectName ):
    project_name = projectName.replace(" " , "_")
    cur.execute(f"CREATE TABLE {project_name}(title,desc,date)")
    success()
def check_name_project(projectname):
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (projectname,))
    if cur.fetchone() !=  None:
        print(f"this name '{projectname}' already exists")
        close_db()
        exit()

def close_db():
    con.close()

def create_title_and_desc(projectname):
    title = input("write title : ")
    desc = input("write descrption : ")
    date = today.strftime("%B %d, %Y")
    cur.execute(f"INSERT INTO {projectname} VALUES (?, ?, ?)", (title, desc, date))
    con.commit()
    success()