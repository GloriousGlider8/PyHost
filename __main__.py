import funcs as f
import colorama as c
import os
from time import sleep as wait
import runpy
import yaml

os.chdir("E:\\test\\sharing\\webTest-main")

os.system("cls")
print(c.Fore.RED + "Warning!\n" + c.Fore.YELLOW + "PyHost is not recommended for production.\nIt only runs basic security checks!\nFor more security, open a pull request on our GitHub with extra security." + c.Style.RESET_ALL)
print(c.Fore.GREEN + "5")
wait(1)
f.upAndClear()
print(c.Fore.GREEN + "4")
wait(1)
f.upAndClear()
print(c.Fore.YELLOW + "3")
wait(1)
f.upAndClear()
print(c.Fore.YELLOW + "2")
wait(1)
f.upAndClear()
print(c.Fore.RED + "1" + c.Style.RESET_ALL)
wait(1)
f.upAndClear()
os.system("cls")
print(c.Fore.YELLOW + "Heads Up!\n" + c.Style.RESET_ALL + "Without unrecommended actions, you can only host files and folders to users on your local network!")
print(c.Fore.GREEN + "5")
wait(1)
f.upAndClear()
print(c.Fore.GREEN + "4")
wait(1)
f.upAndClear()
print(c.Fore.YELLOW + "3")
wait(1)
f.upAndClear()
print(c.Fore.YELLOW + "2")
wait(1)
f.upAndClear()
print(c.Fore.RED + "1" + c.Style.RESET_ALL)
wait(1)
f.upAndClear()
os.system("cls")
print(c.Fore.BLUE + "Notice\n" + c.Fore.CYAN + "PyHost and it's creators are not responsible for any damage caused by using this product.\nOpen issues on our GitHub" + c.Style.RESET_ALL)
print(c.Fore.GREEN + "5")
wait(1)
f.upAndClear()
print(c.Fore.GREEN + "4")
wait(1)
f.upAndClear()
print(c.Fore.YELLOW + "3")
wait(1)
f.upAndClear()
print(c.Fore.YELLOW + "2")
wait(1)
f.upAndClear()
print(c.Fore.RED + "1" + c.Style.RESET_ALL)
wait(1)
f.upAndClear()

action = f.selPrompt(["Host a File", "Host a Folder", "Change Settings", "Quit"], ["📄", "📁", "⚙️", "🚪"], "Welcome to PyHost, choose an option.")

if action != 3:
	if action == 0:
		runpy.run_path("filehost.py")
	elif action == 1:
		runpy.run_path("folderhost.py")
	else:
		hostymlWrite = open("host.yml", "w")
		hostyml = open("host.yml", "r+")

		host = yaml.load(hostyml.read(), Loader=yaml.Loader)

		exitLoop = False

		while exitLoop == False:
			action = f.selPrompt(["Denylist", "Allowlist", "List Usage", "Conflict Handling", "Response Type", "Response Code"], ["❌", "✅", "⚖️", "⚖️", "📄", "#️"], "Settings\nUse [CTRL] + [C] to exit.")