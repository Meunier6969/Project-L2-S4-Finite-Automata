from typing import Optional

class Automata:
	symbols: list[str] = []
	states: int = 0
	initial_state: list[int] = []
	final_state: list[int] = []
	# [State]['Symbol'] -> [Transition]
	transitions: list[dict] = [{}]

	def __init__(self, sym: int, sta: int, i_sta: list[int], f_sta: list[int]) -> None:
		print(f"Initializing Automata : {self}...")
		self.symbols = self.initSymbols(sym)
		self.states = sta
		self.initial_state = i_sta
		self.final_state = f_sta
		self.transitions = self.initTransitions()

	def initSymbols(self, numberOfSymbol: int) -> list[str]:
		return [chr(i+97) for i in range(numberOfSymbol)]

	def initTransitions(self) -> list[dict]:
		return [{C:[] for C in self.symbols} for _ in range(self.states)]

	def addTransition(self) -> None:
		pass

	def displayTransition(self) -> None:
		# Top row
		print(f"{' ':10}", end="")
		for char in self.symbols:
			print(f"{char:10}", end="")
		print()

		# Main table
		for i, state in enumerate(self.transitions):
			print(f"{i:<10}", end="")
			for sym in self.symbols:
				if state.get(sym) in [None,[]]:
					print(f"{'--':<10}", end="")
				else:
					print(f"{str( state.get(sym) ):<10}", end="")
			print()

	def display(self) -> None:
		print("Symbols : ", *self.symbols)
		print("States : ", self.states)
		print("Initial States : ", self.initial_state)
		print("Final States : ", self.final_state)
		print("Transitions : ")
		self.displayTransition()


def parseAutomataFromFile(path: str) -> Automata:
	try:
		file = open(path, "r")
	except Exception as e:
		print(e)
		return None

	# Number of symbols
	nosym = file.readline()
	nosym = int(nosym)
	
	# Number of states
	nosta = file.readline()
	nosta = int(nosta)
	
	# Initial states
	insta = file.readline().split(' ')
	insta = [int(x) for x in insta]
	insta.pop(0)

	# Final states
	fista = file.readline().split(' ')
	fista = [int(x) for x in fista]
	fista.pop(0)

	# Number of transitions
	# Transitions

	return Automata(nosym, nosta, insta, fista)