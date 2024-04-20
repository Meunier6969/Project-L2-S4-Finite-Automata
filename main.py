from automata import Automata, parseAutomataFromFile

def debug():
	# auto: Automata = parseAutomataFromFile("machines/example_automata.txt")
	# auto: Automata = parseAutomataFromFile("machines/test_automata.txt")
	# auto: Automata = parseAutomataFromFile("machines/deterministic_automata.txt")
	# auto: Automata = parseAutomataFromFile("machines/complete_automata.txt")
	# auto: Automata = parseAutomataFromFile("machines/standard_automata.txt")
	auto: Automata = parseAutomataFromFile("machines/given/automata_10.txt")

	auto.display()

	newAuto = auto.standardization()

	print("=== NEW AUTO ===")
	newAuto.display()

def main():
	#Choose to : 1.Choose an Automaton, 2.quit
	#If 1 : To choose an automaton from the test automaton, the given automaton, or the newly created automatons
	#Tell how many .txt there is in the choosen folder. If there are none, it will go back to the previous screen to choose a folder
	#When an automaton is choosen : 1.Check and Display, 2. Standardization, 3.Determinization, 4.Completion (will say if it's deterministic or not, and let the choice), 
	#5.Minimize, 6.Complementary, 7.Read Word, 8.Go back
	run1 = True
	while run1 == True :
		print("--- Efrei Finite Automata Project ---\nPress :\n1.Choose an automaton\n2.Quit")
		inp1 = input("-> ")
		match inp1:
			case "1":
				
				print("--- To choose an automaton, please indicate which type of automaton you wish to use ---\n1.Test Automatons\n2.Given Automatons\n3.Newly Created Automatons")
				inp2 = input ("-> ")
				match inp2:
					case "1":
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
					case "2":
						print("--- There are 44 automatons, from 1 to 44. ---\nEnter a number between 1 and 44")
						inp4="0"
						while int(inp4)<1 or int(inp4)>44:
							print("Please enter the input")
							inp4 = input("-> ")
						auto: Automata = parseAutomataFromFile("machines/given/automata_"+inp4+".txt")

					case "3":
						print("Nothing here yet. Will need a way to check if there is even anything")
					
				run2 = True
				while run2 == True :
					print("--- You have choosen an automata. What do you wish to with it ?\n1.Display\n2.Check\n3.Standardization\n4.Determinization\n5.Completion\n6.Minimize\n7.Complementary\n8.Quit")
					inp5 = input("-> ")
					match inp5 :
						case "1" :
							print("--- You choose to Display ---")
							auto.display()
						case "2" :
							print("--- You choose to Check ---")
							print("-> Is it Standard ?")
							auto.isStandard(True)
							print("-> Is it Deterministic ?")
							auto.isDeterministic(True)
							print("-> Is it Complete ?")
							auto.isComplete(True)
						case "3" :
							print("--- You choose to Standardize the automata ---")
							if auto.isStandard() == True :
								print("This automata is actually already Standard")
							else :
								newAuto = auto.standardization()
								newAuto.display()
						case "4" :
							print("--- You choose to Determinize the automata ---")
							if auto.isDeterministic() == True :
								print("This automata is actually already Deterministic")
							else :
								print("Not implemented yet, sorry")
						case "5" : #Are there more checks to do ? I will need to rewatch the lesson I think
							print("--- You choose to Complete the automata ---")
							if auto.isComplete() == True :
								print("This automata is actually already Complete")
							else :
								newAuto = auto.completion()
								newAuto.display()
						case "6" : #Could be read word or Minimize here
							print("--- You choose to Minimize the automata ---\nI don't think it will happen on this version")
						case "7" :
							print("--- You choose to make the Complementary of the automata ---")
							newAuto = auto.complementary()
							newAuto.display()
						case "8" :
							run2 = False
			case "2":
				return
		
if __name__=="__main__":
	main()
