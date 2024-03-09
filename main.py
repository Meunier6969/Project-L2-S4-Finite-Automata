from automata import Automata, parseAutomataFromFile

def main():
	auto = parseAutomataFromFile("machines/test_automata.txt")
	auto.display()

if __name__=="__main__":
	main()