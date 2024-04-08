from typing import Optional

class Automata:
	symbols: list[str] = []
	states: list[str] = []
	initial_state: list[str] = []
	final_state: list[str] = []
	# [State]['Symbol'] -> [Transition]
	transitions: dict[dict[list]] = {}
		
	def __init__(self, sym: int, sta: int, i_sta: list[str], f_sta: list[str]) -> None:
		# print(f"Initializing Automata : {self}...")
		self.symbols = self.initSymbols(sym)
		self.states = self.initState(sta)
		self.initial_state = i_sta
		self.final_state = f_sta
		self.transitions = self.initTransitions()

	def initSymbols(self, numberOfSymbol: int) -> list[str]:
		return [chr(i+97) for i in range(numberOfSymbol)]

	def initState(self, numberOfState: int) -> list[str]:
		return [str(i) for i in range(numberOfState)]

	def initTransitions(self) -> dict[dict[list]]:
		return {state:{C:[] for C in self.symbols} for state in self.states}

	def addTransition(self, state: str, symbol: str, transition: str) -> None:
		if symbol not in self.symbols:
			print(f"Symbol {symbol} not in FA.")
			return

		if state not in self.states:
			print(f"State {state} is not in FA.")
			return

		if transition not in self.states:
			print(f"Transition {transition} is not in FA.")
			return

		if transition not in self.transitions[state][symbol]:
			self.transitions[state][symbol].append(transition)

	def displayTransition(self) -> None:
		# Top row
		print(f"{' ':14}", end="")
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
	
	def complementary(self) -> "Automata":
		
		newAutomata = Automata(
			len(self.symbols), 
			self.states + 1,
			[self.states],
			self.final_state
		)
		# ini: list[int] = []
		# for i, state in enumerate(self.initial_state):
		pass
		

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
	insta.pop(0)

	# Final states
	fista = file.readline().split(' ')
	fista.pop(0)

	newAutomata =  Automata(nosym, nosta, insta, fista)

	# Number of transitions
	file.readline() # We can ignore this line

	# Transitions
	transitions = file.readlines()
	# transitions = [trans.removesuffix('\n') for trans in transitions]

	# TODO: fix svp
	# Assuming state, character and transition is one character each
	for trans in transitions:
		newAutomata.addTransition(trans[0], trans[1], trans[2])
		
	return newAutomata

