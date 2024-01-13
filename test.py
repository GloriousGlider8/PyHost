import funcs as f
import os
from time import sleep as wait

while True:
	os.system("cls")
	prg = f.progressBar("Loading...", 14)
	prg.render()
	wait(5)
	prg.increase(2)
	prg.render()
	wait(0.5)
	prg.increase(3)
	prg.render()
	wait(1)
	prg.increase(9)
	prg.setTitle("Loaded!")
	prg.render()
	wait(2)
	os.system("cls")
	intro = str("\n").join(input("[string] Intro: ").split("\\n"))
	default = input("[string] Default Value: ")
	numReq = input("[binary] Numerical Requirement: ") == "1"
	intReq = input("[binary] Integer Requirement: ") == "1"
	fltReq = input("[binary] Floating Point Requirement: ") == "1"
	posReq = input("[binary] Positive Requirement: ") == "1"
	negReq = input("[binary] Negative Requirement: ") == "1"
	maxChar = int(input("[int] Maximum Characters: "))
	minChar = int(input("[int] Minimum Characters: "))
	regexMatch = input("[string] Regular Expression Match: ")
	
	print(f.stringSelect(intro, default, numReq, intReq, fltReq, posReq, negReq, maxChar, minChar, regexMatch))
	print("Correct!")
	os.system("timeout /t -1")