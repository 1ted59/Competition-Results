#colorama allows usage of escape chars on any platform
#install it with "pip install colorama"
import colorama
from colorama import init,Fore,Back,deinit
init()

#escape codes for custom behavior in terminal
CLEAR = '\033[2J'
RESETTEXT = '\033[0m'

#file locations, change them here if you want
RESULTSFILE = "results.txt"
LINEFILE = "resultsline.txt"

def main():
	#get the result info 
	print(CLEAR + "Getting lines from file.")
	compData = open(RESULTSFILE, "r")
	compInfo = compData.readlines()
	compData.close()
	
	
	#clears the file used 
	clearTextFile()
	
	dqMarker = -1
	num = 0

	print("Checking for correct formatting (DQ empty line).")
	for compLine in compInfo:
		num += 1
		if compLine.strip() == "":
			dqMarker = num
			break
			
	assert dqMarker != -1, "Empty line not found before DQs! Exiting..."

	dqMarker-=1
	
	compInfo.pop(dqMarker)
	compInfo = reverseArray(compInfo, dqMarker)
	
	
	print("Ready to start printing info, press enter to start.")
	
	print("\nTotal Entrants:", len(compInfo),"\nNon-DQs:", end=" ")
	print(dqMarker,"\nDQs:",len(compInfo) - dqMarker)
	
	i=0
	for line in compInfo:
		if i >= dqMarker:
			print(Back.RED, end="")
		if line.strip() == "":
			print("(empty line)", end="")
		print(line.strip() + RESETTEXT)
		i+=1
	
	input()
	print(CLEAR, end="")
	
	startComp(compInfo, dqMarker)
		
	writeTextToResults("Thanks for watching!")
	
	print(CLEAR)
	print("Printed 'Thanks for watching!'\n\nPress enter to exit.")
	input()
	print(CLEAR)
	
	clearTextFile()
	
def startComp(compInfo, dqMarker):
	"""
	loops over the array compInfo, displaying all the results at once
	with the current placing highlighted. Pressing enter moves on to
	the next placing. All placings after the int dqMarker in the array
	are displayed on a red background to differentiate them.
	"""
	
	#loop over the array for every entry in it
	currentSpot = 0
	while currentSpot < len(compInfo):
		print(CLEAR, end="")
		#display every entry in the array by looping over it
		i = 0
		for compLine in compInfo:
			
			#replace characters that don't show up in some fonts
			compLine = compLine.replace('“','"').replace('”','"').replace("’","'").strip()
			
			#if the line is a DQ display it with a red background
			if i >= dqMarker:
				print(Back.RED,end="")
				
			# if the current placing is up, display it on a white background with black text
			if i == currentSpot:
				print(Back.WHITE + Fore.BLACK + ">",end="")
				compOutput = compLine
				
				#if it is over the length, cut off some data at the end
				if len(compLine) > 64:
					compOutput = compOutput[:64]
					compOutput = compOutput[:compOutput.rfind(" ")]
					compOutput += "..."
					
				#write output to the line file
				writeTextToResults(compOutput)
				
			if compLine.strip() == "":
				print("(Empty line)",end="")
			#print line and reset text styles
			print(compLine + RESETTEXT)
			i += 1
			
		#wait until the user presses enter to continue
		input()
		currentSpot += 1
		

def writeTextToResults(text):
	"""sets the resultsline file to the inputted text"""
	compData = open(LINEFILE, "w")
	compData.write(text.strip())
	compData.close()
	
def clearTextFile():
	"""clears the results text file"""
	writeTextToResults("")
	
def reverseArray(data, dqMarker):
	"""
	reverses the contents of the array 'data'
	before the spot marked by the int dqMarker
	
	returns the array after reversing it
	"""
	print("Reversing array")
	temp = -1
	counter = 0
	
	#iterate through the list until halfway point (not counting dqs)
	#swapping 1st and last to be able to see in reverse order
	while counter < (dqMarker // 2):
		temp = data[counter]
		data[counter] = data[dqMarker - counter - 1]
		data[dqMarker - counter - 1] = temp
		counter += 1
	
	return data
	
main()

#turn off colorama as the script is done
deinit()