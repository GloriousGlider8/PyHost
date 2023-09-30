import funcs as f
import colorama as c
import os
from time import sleep as wait
import runpy
import yaml

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
		temp = open("host.yml", "r")
		hostyml = temp.read()
		temp.close()

		hostfile = open("host.yml", "w")

		host = yaml.load(hostyml, Loader=yaml.FullLoader)

		exitLoop = False

		while exitLoop == False:
			action = f.selPrompt(["Denylist", "Allowlist", "List Usage", "Response Type", "Response Code", "Quit", "Save"], ["❌", "✅", "⚖️", "📄", "#️⃣", "🚪", "💾"], "Settings")
			if action == 5:
				exitLoop = True
			else:
				if action == 0:
					temp = host["denylist"]
					length = len(temp) - 1
					temp1 = []
					for i, v in enumerate(temp):
						if v == None:
							temp.pop(i)
							host["denylist"].pop(i)
						else:
							temp1.append("❌")
					temp.append("New")
					temp1.append("➕")
					temp.append("Back")
					temp1.append("⬅️")
					action1 = f.selPrompt(temp, temp1, "Settings / Allowlist")

					if action1 <= length:
						host["denylist"][action1] = None
					else:
						temp2 = action1 - length

						if temp2 == 1:
							newone = f.stringSelect("Enter an IP to block.", "", False, False, False, False, False, -1, 1)
							host["denylist"].append(newone)