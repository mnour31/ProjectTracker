from functions import create_data , check_name_project , close_db , create_title_and_desc
frist_user_input = input("what do you want : show , create , update? ")

def create():
    project_name = input("write project name : ")
    
    # check name
    name_pro = project_name.replace(" " ,"_")
    check_name_project(name_pro)

    # create data in database
    create_data(project_name)
    ask_user = input("does you want create info now? write yes or no")
    if ask_user == "yes":
        create_title_and_desc(name_pro)
        
    elif ask_user == "no" :
        close_db()
        print("Thank you for using this program.")
        exit()
    else:
        print("Unclear , answer please try again")

def update():
    get_project_name = input("please project name :  ")
if frist_user_input == "create":
    create()
    
# update code
elif frist_user_input == "update":
    update()