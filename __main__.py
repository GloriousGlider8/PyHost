import funcs as f
import colorama as c
import os
from time import sleep as wait
import runpy
import json

if os.path.exists(os.path.join(os.getenv("APPDATA"), "PyHost", "PATH")):
    homePathTxt = open(os.path.join(os.getenv("APPDATA"), "PyHost", "PATH"))
    homePath = homePathTxt.read()
    homePathTxt.close()
    homePathTxt = None
    if not os.path.exists(homePath):
        raise OSError("PyHost HOME is not valid")
else:
    raise OSError("PyHost HOME is missing")

os.chdir(homePath)

os.system("cls")
print(c.Fore.RED + "Warning!\n" + c.Fore.YELLOW + "PyHost is not recommended for production.\nIt only runs basic security checks!\nFor more security, open a pull request on our GitHub with extra security." + c.Style.RESET_ALL)
os.system("timeout /t -1")
os.system("cls")
print(c.Fore.YELLOW + "Heads Up!\n" + c.Style.RESET_ALL + "Without unrecommended actions, you can only host files and folders to users on your local network!")
os.system("timeout /t -1")
os.system("cls")
print(c.Fore.BLUE + "Notice\n" + c.Fore.CYAN + "PyHost and it's creators are not responsible for any damage caused by using this product.\nOpen issues on our GitHub" + c.Style.RESET_ALL)
os.system("timeout /t -1")

action = f.selPrompt(["Host a File", "Host a Folder", "Change Settings", "Quit"], ["📄", "📁", "⚙️", "🚪"], "Welcome to PyHost, choose an option.")

if action != 3:
	if action == 0:
		runpy.run_path("filehost.py")
	elif action == 1:
		runpy.run_path("folderhost.py")
	else:
		temp = open(homePath + "\\host.json", "r")
		hostjs = temp.read()
		temp.close()

		host = json.loads(hostjs)

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
							newone = f.stringSelect("Enter an IP to block.", "", False, False, False, False, False, -1, 1, "\\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\\.|$)){4}\\b")
							host["denylist"].append(newone)