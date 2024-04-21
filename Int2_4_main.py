from Int2_4_automata import Automata, parseAutomataFromFile
import os

def debug():
	# auto: Automata = parseAutomataFromFile("machines/example_automata.txt")
	# auto: Automata = parseAutomataFromFile("machines/test_automata.txt")
	auto: Automata = parseAutomataFromFile("machines/deterministic_automata.txt")
	# auto: Automata = parseAutomataFromFile("machines/complete_automata.txt")
	# auto: Automata = parseAutomataFromFile("machines/standard_automata.txt")
	# auto: Automata = parseAutomataFromFile("machines/given/automata_44.txt")
	# auto: Automata = parseAutomataFromFile("machines/nondeter_automata.txt")
	# auto: Automata = parseAutomataFromFile("machines/epsilon_automata.txt")

	# auto.standardization().display()
	auto.display()
	auto.isDeterministic(True)

	print("=== READING ===")

	while 1:
		word = input("> ")
		if word == "end": 
			break

		auto.readWord(word, True)

def main():
	#First main menu -> Choose to : 1.Choose an Automaton, 0.quit
	#If 1 : To choose an automaton from the test automaton, the given automaton, or the newly created automatons

	#Second main menu ->When an automaton is choosen : 1.Display, 2.Check, 3. Standardization, 4.Determinization, 5.Completion, 
	#6.Minimize, 7.Complementary, 8.Read Word, 0.Go back

	run1 = True
	while run1 == True :
		os.system("cls")
		print("--- Efrei Finite Automata Project ---\nPress :\n1.Choose an automaton\n0.Quit")
		inp1 = input("-> ")
		match inp1:
			case "1":
				os.system("cls")
				print("--- To choose an automaton, please indicate which type of automaton you wish to use ---\n1.Test Automatons\n2.Given Automatons\n3.Newly Created Automatons")
				inp2 = input ("-> ")
				match inp2:
					case "1": #For choosing an automata that we use for debugging
						os.system("cls")
						print("--- Choose from these automatons ---\n1.exemple_automata\n2.test_automata\n3.deterministic_automata\n4.complete_automata\n5.standard_automata")
						inp3 = input("-> ")
						match inp3:
							case "1" :
								auto: Automata = parseAutomataFromFile("machines/example_automata.txt")
							case "2" :
								auto: Automata = parseAutomataFromFile("machines/test_automata.txt")
							case "3" :
								auto: Automata = parseAutomataFromFile("machines/deterministic_automata.txt")
							case "4" :
								auto: Automata = parseAutomataFromFile("machines/complete_automata.txt")
							case "5" :
								auto: Automata = parseAutomataFromFile("machines/standard_automata.txt")
					case "2": #For choosing an automata from thise given the 8 April
						os.system("cls")
						print("--- There are 44 automatons, from 1 to 44. ---\nEnter a number between 1 and 44")
						inp4="0"
						while int(inp4)<1 or int(inp4)>44:
							print("Please enter the input")
							inp4 = input("-> ")
						auto: Automata = parseAutomataFromFile("machines/given/automata_"+inp4+".txt")
					case "3":
						print("Nothing here yet. Will need a way to check if there is even anything")
						return
				run2 = True
				while run2 == True :
					os.system("cls")
					print("--- You have choosen an automata. What do you wish to with it ? ---\n1.Display\n2.Check\n3.Standardization\n4.Determinization\n5.Completion\n6.Minimize\n7.Complementary\n8.Read Word\n0.Return")
					inp5 = input("-> ")
					match inp5 :
						case "1" : #Display
							os.system("cls")
							print("--- You choose to Display ---")
							auto.display()
							etc = input("Press to continue -> ")
						case "2" : #Check to see if the choosen automata is standard, deterministic or complete.
							os.system("cls")
							print("--- You choose to Check ---")
							auto.isComplete(True)
							etc = input("Press to continue -> ")
						case "3" : #Standardization
							os.system("cls")
							print("--- You choose to Standardize the automata ---")
							if auto.isStandard() == True :
								print("This automata is actually already Standard")
							else :
								newAuto = auto.standardization()
								newAuto.display()
							etc = input("Press to continue -> ")
						case "4" : #Determinization
							os.system("cls")
							print("--- You choose to Determinize the automata ---")
							if auto.isDeterministic() == True :
								print("This automata is actually already Deterministic")
							else :
								newAuto = auto.determinization()
								newAuto.display()
							etc = input("Press to continue -> ")
						case "5" : #Completion
							os.system("cls")
							print("--- You choose to Complete the automata ---")
							if auto.isComplete() == True :
								print("This automata is actually already Complete")
							else :
								if auto.isDeterministic() == False :
									newAuto = auto.determinizationAndCompletion()
									newAuto.display()
								else :
									newAuto = auto.completion()
									newAuto.display()
							etc = input("Press to continue -> ")
						case "6" : #Minimize
							os.system("cls")
							print("--- You choose to Minimize the automata ---\nI don't think it will happen on this version")
							etc = input("Press to continue -> ")
						case "7" : #Complementary
							os.system("cls")
							print("--- You choose to make the Complementary of the automata ---")
							newAuto = auto.complementary()
							newAuto.display()
							etc = input("Press to continue -> ")
						case "8" : #Read Word
							os.system("cls")
							print("--- You choose to Read a Word. ---")
							str = input("Enter a string -> ")
							auto.readWord(str, True)
							etc = input("Press to continue -> ")
						case "0" : #Return to previous menu
							run2 = False
			case "0": #To quit the whole program.
				return
		
if __name__=="__main__": 
	main()
	# debug()
