from automata import Automata, parseAutomataFromFile

def main():
	auto = parseAutomataFromFile("machines/test_automata.txt")
	auto.transitions[0]['a'].append(1)
	auto.transitions[0]['a'].append(0)
	auto.display()
	# print(auto.transitions)

if __name__=="__main__":
	main()