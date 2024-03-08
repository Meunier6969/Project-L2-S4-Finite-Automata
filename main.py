from automata import Automata

def main():
	auto = Automata(2, 5, [0], [4])
	auto.transitions[0][0] = (1,2)
	auto.displayTransition()

if __name__=="__main__":
	main()