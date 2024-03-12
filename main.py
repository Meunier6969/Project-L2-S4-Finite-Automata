from automata import Automata, parseAutomataFromFile

def main():
	# auto: Automata = parseAutomataFromFile("machines/deterministic_automata.txt")
	# auto: Automata = parseAutomataFromFile("machines/example_automata.txt")
	auto: Automata = parseAutomataFromFile("machines/test_automata.txt")
	auto.display()
	print(f"Deterministic : {auto.isDeterministic(True)}")
	print(f"Complete : {auto.isComplete()}")

if __name__=="__main__":
	main()