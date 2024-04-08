from typing import Optional

class Automata:
	symbols: list[str] = []
	states: int = 0
	initial_state: list[int] = []
	final_state: list[int] = []
	# [State]['Symbol'] -> [Transition]
	transitions: dict[dict[list]] = {}
		
	def __init__(self, sym: int, sta: int, i_sta: list[int], f_sta: list[int]) -> None:
		# print(f"Initializing Automata : {self}...")
		self.symbols = self.initSymbols(sym)
		self.states = sta
		self.initial_state = i_sta
		self.final_state = f_sta
		self.transitions = self.initTransitions()

	def initSymbols(self, numberOfSymbol: int) -> list[str]:
		return [chr(i+97) for i in range(numberOfSymbol)]

	def initTransitions(self) -> dict[dict[list]]:
		return {str(i):{C:[] for C in self.symbols} for i in range(self.states)}

	def addTransition(self, state: int, symbol: str, transition: int) -> None:
		if symbol not in self.symbols:
			print(f"Symbol {symbol} not in FA.")
			return

		if state >= self.states or state < 0:
			print(f"State {state} is not in FA.")
			return

		if transition >= self.states or transition < 0:
			print(f"Transition {transition} is not in FA.")
			return

		if transition not in self.transitions[state][symbol]:
			self.transitions[state][symbol].append(transition)

	def displayTransition(self) -> None:
		# Top row
		print(f"{' ':10}", end="")
		for char in self.symbols:
			print(f"{char:10}", end="")
		print()

		# Main table
		for state, transition in self.transitions.items():
			if state in self.initial_state :
				print("->",f"{state:<10}", end="")
			elif state in self.final_state :
				print("<-",f"{state:<10}", end="")
			else :
				print("  ",f"{state:<10}", end="")

			for sym in self.symbols:
				if transition.get(sym) in [None,[]]:
					print(f"{'--':<10}", end="")
				else:
					print(f"{str( transition.get(sym) ):<10}", end="")
			print()

	def display(self) -> None:
		print("Symbols : ", *self.symbols)
		print("States : ", self.states)
		print("Initial State(s) : ", self.initial_state)
		print("Final State(s) : ", self.final_state)
		print("Transitions : ")
		self.displayTransition()

	def isStandard(self, verbose:bool = False) -> bool:
		if len(self.initial_state) != 1:
			if verbose: print(f"FA is not standard :\nFA contains multiples initial states : {self.initial_state}")
			return False

		initState = self.initial_state[0]

		for i, state in enumerate(self.transitions):
			for symbol in self.symbols:
				if initState in state.get(symbol):
					if verbose: print(f"FA is not standard :\nFA goes back to initial state : {state} -> {self.initial_state}")
					return False

		if verbose: print("FA is standard")
		return True


	def isDeterministic(self, verbose:bool = False) -> bool:
		if len(self.initial_state) != 1:
			if verbose: print(f"FA is not deterministic :\nFA contains multiples initial states : {self.initial_state}")
			return False

		for i, state in enumerate(self.transitions):
			for symbol in self.symbols:
				if len(state.get(symbol)) > 1:
					if verbose: print(f"FA is not deterministic :\nState {i} has multiple transitions with symbol '{symbol}' : {state.get(symbol)}")
					return False

		if verbose: print("FA is deterministic")
		return True

	def isComplete(self, verbose:bool = False) -> bool:
		if not self.isDeterministic(verbose=True):
			if verbose: print("FA is not complete")
			return False

		for i, state in enumerate(self.transitions):
			for symbol in self.symbols:
				if len(state.get(symbol)) == 0:
					if verbose: print(f"FA is not complete :\nState {i} has either no transitions with symbol '{symbol}' : {state.get(symbol)}")
					return False

		if verbose: print("FA is complete")
		return True

	def standardize(self) -> "Automata":
		if self.isStandard():
			return self

		newAutomata = Automata(
			len(self.symbols), 
			self.states + 1,
			[self.states],
			self.final_state
		)

		newAutomata.display()

	def completion(self) -> "Automata":
		if self.isComplete():
			return self
		
		# créer nouveau automate state "poubelle"

		for i, state in enumerate(self.transitions):
			for symbol in self.symbols:
				pass
				# si rien -> poubelle
		
		# return

	def determinization(self) -> "Automata":
		if self.isDeterministic():
			return self
		pass 

	def determinizationAndCompletion(self) -> "Automata":
		if self.isDeterministic() and self.isComplete():
			return self

		cdfa = self

		if not cdfa.isDeterministic():
			cdfa = cdfa.determinization()

		if not cdfa.isComplete():
			cdfa = cdfa.completion()

		return cdfa


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

	newAutomata =  Automata(nosym, nosta, insta, fista)

	# Number of transitions
	file.readline() # We can ignore this line

	# Transitions
	transitions = file.readlines()
	# transitions = [trans.removesuffix('\n') for trans in transitions]

	# Assuming state, character and transition is one character each
	for trans in transitions:
		newAutomata.addTransition(int(trans[0]), trans[1], int(trans[2]))
		
	return newAutomata

