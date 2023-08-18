from functions import create_data , check_name_project , close_db , create_title_and_desc
import colorama
from colorama import Fore
#Initialize colorama
colorama.init(autoreset=True)


frist_user_input = input(Fore.CYAN +"what do you want : show , create , update? ")

def create():
    project_name = input(Fore.CYAN +"write project name : ")
    
    # check name
    name_pro = project_name.replace(" " ,"_")
    res = check_name_project(name_pro)
    if res:
        close_db()
        exit()

    # create data in database
    create_data(project_name)
    ask_user = input(Fore.CYAN +"does you want create info now? write yes or no")
    if ask_user == "yes":
        create_title_and_desc(name_pro)
        
    elif ask_user == "no" :
        close_db()
        print(Fore.CYAN +"Thank you for using this program.")
        exit()
    else:
        print(Fore.CYAN +"Unclear , answer please try again")

def update():
    get_project_name = input(Fore.CYAN +"please project name :  ")
    name_pro = get_project_name.replace(" " ,"_")
    res = check_name_project(name_pro)
    if res:
        create_title_and_desc(name_pro)
    else:
        print(Fore.CYAN +"We do not have a project with this name. Do you want to create a project with a name?")
        get_input = input(Fore.CYAN +"yes or no : ")
        if get_input == "yes":
            create()
        else:
            close_db()
            exit()
if frist_user_input == "create":
    create()
    
# update code
elif frist_user_input == "update":
    update()