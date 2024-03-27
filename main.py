from automata import Automata, parseAutomataFromFile

def main():
	# auto: Automata = parseAutomataFromFile("machines/example_automata.txt")
	# auto: Automata = parseAutomataFromFile("machines/test_automata.txt")
	# auto: Automata = parseAutomataFromFile("machines/deterministic_automata.txt")
	# auto: Automata = parseAutomataFromFile("machines/complete_automata.txt")
	auto: Automata = parseAutomataFromFile("machines/standard_automata.txt")
	auto.display()
	# auto.isComplete(verbose=True)
	auto.isStandard(verbose=True)

if __name__=="__main__":
	main()