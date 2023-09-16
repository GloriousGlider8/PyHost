import funcs as f
import colorama as c
import os
from time import sleep as wait
import runpy

print(c.Fore.RED + "Warning!\n" + c.Fore.YELLOW + "PyHost is not recommended for production.\nIt only runs basic security checks!\nFor more security, open a pull request on our GitHub with extra security." + c.Style.RESET_ALL)
wait(3)
os.system("cls")
print(c.Fore.YELLOW + "Heads Up!\n" + c.Style.RESET_ALL + "Without unrecomended actions, you can only host files and folders to users on your local network!")
wait(3)
os.system("cls")
print(c.Fore.BLUE + "Notice\n" + c.Fore.CYAN + "PyHost and it's creators are not responsible for any damage caused by using this product.\nOpen issues on our GitHub" + c.Style.RESET_ALL)

action = f.selPrompt(["Host a File", "Host a Folder", "Quit"], ["📤", "📤", "🚪"], "Welcome to PyHost, choose an option.")

if action != 2:
	if action == 0:
		runpy.run_path("filehost.py")
	else:
		runpy.run_path("folderhost.py")
