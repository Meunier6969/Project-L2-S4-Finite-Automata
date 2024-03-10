from automata import Automata, parseAutomataFromFile

def main():
	auto: Automata = parseAutomataFromFile("machines/example_automata.txt")
	# auto.addTransition(0, 'a', 0)
	# auto.addTransition(0, 'a', 1)
	# auto.addTransition(0, 'a', 2)
	auto.display()
	# print(auto.transitions)

if __name__=="__main__":
	main()