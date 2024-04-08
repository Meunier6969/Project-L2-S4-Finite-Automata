from automata import Automata, parseAutomataFromFile

def main():
	auto: Automata = parseAutomataFromFile("machines/example_automata.txt")
	# auto: Automata = parseAutomataFromFile("machines/test_automata.txt")
	# auto: Automata = parseAutomataFromFile("machines/deterministic_automata.txt")
	# auto: Automata = parseAutomataFromFile("machines/complete_automata.txt")
	# auto: Automata = parseAutomataFromFile("machines/standard_automata.txt")

	# auto = Automata(3, 5, [0], [1,2])
	# auto.transitions[2]['b'] = [69]

	# print(auto.states)

	auto.display()
	# auto.isStandard(verbose=True)
	# auto.isDeterministic(verbose=True)
	auto.isComplete(verbose=True)


if __name__=="__main__":
	main()
