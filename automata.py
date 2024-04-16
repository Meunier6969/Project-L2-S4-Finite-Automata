from re import split as regexSplit
from typing import Optional
from copy import deepcopy

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

	def addNewState(self, newState: str) -> None:
		self.states.append(newState)
		self.transitions.update({newState:{C:[] for C in self.symbols}})

	def displayTransition(self) -> None:
		# Top row
		print(f"{' ':13}", end="")
		for char in self.symbols:
			print(f"{char:12}", end="")
		print()

		# Main table
		for state, transition in self.transitions.items():
			if state in self.initial_state and state in self.final_state :
				print("<>",f"{state:<10}", end="")
			elif state in self.initial_state :
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

		for state, transition in self.transitions.items():
			for symbol in self.symbols:
				if initState in transition[symbol]:
					if verbose: print(f"FA is not standard :\nFA goes back to initial state : {state} -> {self.initial_state}")
					return False

		if verbose: print("FA is standard")
		return True

	def isDeterministic(self, verbose:bool = False) -> bool:
		if len(self.initial_state) != 1:
			if verbose: print(f"FA is not deterministic :\nFA contains multiples initial states : {self.initial_state}")
			return False

		for state, transition in self.transitions.items():
			for symbol in self.symbols:
				if len(transition[symbol]) > 1:
					if verbose: print(f"FA is not deterministic :\nState {state} has multiple transitions with symbol '{symbol}' : {transition.get(symbol)}")
					return False

		if verbose: print("FA is deterministic")
		return True

	def isComplete(self, verbose:bool = False) -> bool:
		if not self.isDeterministic(verbose):
			if verbose: print("FA is not complete")
			return False

		for state, transition in self.transitions.items():
			for symbol in self.symbols:
				if len(transition[symbol]) == 0:
					if verbose: print(f"FA is not complete :\nState {state} has no transitions with symbol '{symbol}'")
					return False

		if verbose: print("FA is complete")
		return True

	def standardization(self) -> "Automata":
		if self.isStandard():
			return self

		standardized = Automata(
			len(self.symbols),
			len(self.states) + 1,
			["I"],
			deepcopy(self.final_state)
		)

		standardized.states[-1] = "I"
		standardized.transitions = standardized.initTransitions() # Add "I" to the list of transition, might be better to add a function to do that

		return standardized
		standardAutomata = Automata(
			len(self.symbols), 
			self.states + 1,
			[self.states],
			self.final_state
		)

		standardAutomata.display()

	def determinization(self) -> "Automata":
		if self.isDeterministic():
			return self
		pass 

	def completion(self) -> "Automata":
		if self.isComplete():
			return self

		completeAutomata = Automata(
			len(self.symbols),
			len(self.states),
			self.initial_state,
			self.final_state
		)

		# completeAutomata.states.append("P")

		# completeAutomata.transitions["P"] = {symbol: ["P"] for symbol in completeAutomata.symbols}

		# completeAutomata.transitions.update({state: {symbol: transitions.copy() for symbol, transitions in self.transitions[state].items()} for state in self.transitions})

		completeAutomata.transitions = deepcopy(self.transitions)
		completeAutomata.addNewState("P")

		print(completeAutomata.states)

		for state in completeAutomata.states:
			# if state != "P":
			for symbol in completeAutomata.symbols:
				if not completeAutomata.transitions[state].get(symbol):
					completeAutomata.addTransition(state, symbol, "P")


		return completeAutomata



	def determinizationAndCompletion(self) -> "Automata":
		if self.isDeterministic() and self.isComplete():
			return self

		cdfa = self

		if not cdfa.isDeterministic():
			cdfa = cdfa.determinization()

		if not cdfa.isComplete():
			cdfa = cdfa.completion()

		return cdfa


	def complementary(self) -> "Automata":
		complementaryAutomata = Automata(
			len(self.symbols), 
			len(self.states),
			self.initial_state,
			# self.states - self.final_state
			[state for state in self.states if state not in self.final_state]
		)

		complementaryAutomata.transitions = self.transitions

		return complementaryAutomata


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
	insta[-1] = insta[-1].removesuffix('\n')

	# Final states
	fista = file.readline().split(' ')
	fista.pop(0)
	fista[-1] = fista[-1].removesuffix('\n')

	newAutomata =  Automata(nosym, nosta, insta, fista)

	# Number of transitions
	file.readline() # We can ignore this line

	# Transitions
	transitions = file.readlines()
	# transitions = [trans.removesuffix('\n') for trans in transitions]

	# Assuming state, character and transition is one character each
	for trans in transitions:
		trans = regexSplit("(\d+)", trans)[1:]
		newAutomata.addTransition(trans[0], trans[1], trans[2])
		
	return newAutomata
