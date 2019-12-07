import random
import math
import consoleq

def writeOut(list):
	counter = 1
	for time in list:
		print(str(counter) + ". " + time + "\n")
		counter += 1
	print("------\n")

def strike(text):
	result = ''
	for c in text:
		result = result + c + '\u0336'
	return result

masterList = ["start of Greek Civilization", "start of Minoan Civilization", "Minoans develop their writing system", "Minoan ceramicists create Kamares Ware", "start of Minoan peak", "start of Mycenaean Civilization", "Eruption of Thera", "creation of Grave Circle A", "Tholos Tomb creation",  "end of Minoan peak", "end of the Minoan Civilization", "Mycenaeans enter Minoan Palaces", "start of the late Bronze Age", "creation of the lions in the Lions Gate", "end of the late Bronze Age", "fall of the Mycenaeans", "start of the Dark Ages", "Lord Elgin sends two of his people to explore the Peloponnese", "Kyriakos Psistakis excavates Lions Gate", "Heinrich Schliemann uncovers Grave Circle A", "Heinrich Schliemann discovers Troy", "Sir Arthur Evans discovers Knossos", "Sir Arthur Evans excavates Knossos", "Grave Circle B is discovered", "Michael Ventris translates Linear B", "an international team goes to Santorini to explore Akrotiri"]
correctList = []
outputList = []
userList = []
outputListHolder = []

instructions = "Type replace, then the number to replace to replace a number.\nHit enter to submit your answers.\n-------"
outputList = random.sample(masterList, random.randint(3, len(masterList) - 15))
outputListHolder = list(outputList)

deletedNumber = 0
deleteProcess = False

for object in masterList:
	if object in outputList:
		correctList.append(object)
print(instructions)
writeOut(outputList)

while True:
	userInput = input("")
	if userInput == "":
		break
	try:
		userInput = int(userInput)
		if deleteProcess == True:
			if "" in userList:
				userList.remove("")
				userList.insert(deletedNumber, outputList[userInput - 1])
				deleteProcess = False
			else:
				del(userList[userInput - 1])
				userList.insert(userInput - 1, "")
				deletedNumber = userInput - 1
		else:
			#problem
			if userInput - 1 <= len(outputList): #and userList[userInput - 1] not in userList:
				userList.append(outputList[userInput - 1])
	except:
		if userInput == "replace" or userInput == "Replace":
			deleteProcess = True
	finally:
		console.clear()
		print(instructions)
		index = 0
		for element in outputList:
			if element in userList:
				outputListHolder[index] = strike(outputList[index])
			else:
				outputListHolder[index] = outputList[index]
			index += 1
		writeOut(outputListHolder)
		writeOut(userList)

if userList == correctList:
	print("CORRECT!\n")
print("\nCorrect List:\n")
for time in correctList:
	print(time)
print("\nFull List\n-------")
for time in masterList:
	print(time)
