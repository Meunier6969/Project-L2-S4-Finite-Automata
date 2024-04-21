from re import split as regexSplit
from typing import Optional
from copy import deepcopy

class Automata:
	symbols: list[str] = []
	states: list[str] = []
	initial_state: list[str] = []
	final_state: list[str] = []
	# ['State']['Symbol'] -> [Transition]
	transitions: dict[dict[list]] = {}

	asyncronous: bool = False

	def __init__(self, sym: int, sta: int, i_sta: list[str], f_sta: list[str], asyncronous:bool = False) -> None:
		# print(f"Initializing Automata : {self}...")
		self.symbols = self.initSymbols(sym)
		self.states = self.initState(sta)
		self.initial_state = i_sta
		self.final_state = f_sta

		self.asyncronous = asyncronous
		if asyncronous:
			self.symbols.append("E")

		self.transitions = self.initTransitions()

	def copy(self) -> "Automata":
		copied = Automata(
			0,
			0,
			deepcopy(self.initial_state),
			deepcopy(self.final_state)
		)

		copied.symbols = deepcopy(self.symbols)
		copied.states = deepcopy(self.states)
		copied.transitions = deepcopy(self.transitions)

		return copied

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
			print(f"{char:10}", end="")
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
					print(f"{str( mergeSortList(transition.get(sym), ',') ):<10}", end="")
			print()

	def display(self) -> None:
		print("Symbols : ", *self.symbols)
		print("States : ", self.states)
		print("Initial State(s) : ", self.initial_state)
		print("Final State(s) : ", self.final_state)
		print("Transitions : ")
		self.displayTransition()


	def isAsyncronous(self, verbose:bool = False) -> bool:
		if verbose:
			if self.asyncronous: print("FA is asyncronous: FA contain epsilon")
			if not self.asyncronous: print("FA is syncronous: FA doesn't contain epsilon")
		return self.asyncronous

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
			if verbose: print("FA is not complete : FA is not deterministic")
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
		
		standard = self.copy()
		standard.addNewState("I")

		# Check if the new state I should be a final state
		if any([i in self.final_state for i in self.initial_state]):
			standard.final_state.append("I")

		newtransitions = {C:[] for C in self.symbols}

		for symbol in self.symbols:
			temp = []
			for initstate in self.initial_state:
				temp += self.transitions[initstate][symbol]
			newtransitions[symbol] = removeDuplicate(temp)

		standard.transitions["I"] = newtransitions
		standard.initial_state = ["I"]

		return standard

	def determinization(self) -> "Automata":
		# Removing the "E" symbol if present
		if self.isAsyncronous():
			deter = Automata(len(self.symbols) - 1, 0, [], [])
		else:
			deter = Automata(len(self.symbols), 0, [], [])

		# Find epsilon-closure
		epsilonclosure = {}
		for state in self.states:
			epsilonclosure.update({state: self.findEpsilonClosure(state)})

		initstate = []
		for init in self.initial_state:
			initstate += epsilonclosure[init]

		initstate = mergeSortList(initstate)
		
		deter.addNewState(initstate)
		deter.initial_state = [initstate]

		queue = [deter.initial_state[0]]

		while queue:
			current = queue.pop(0)
			isfinal = False

			for sym in deter.symbols:
				newtransition = []
				
				for c in current: # Get each transition from the original automata
					for smth in self.transitions[c][sym]:
						newtransition += epsilonclosure[smth]
					if c in self.final_state:
						isfinal = True

				if newtransition == []:
					continue

				newtransition = mergeSortList(removeDuplicate(newtransition))
					
				if isfinal and current not in deter.final_state:
					deter.final_state.append(current)

				if newtransition not in deter.states:
					deter.addNewState(newtransition)
					queue.append(newtransition)

				deter.addTransition(current, sym, newtransition)

		return deter


	def completion(self) -> "Automata":
		if self.isComplete():
			return self

		completeAutomata = self.copy()

		completeAutomata.addNewState("P")

		for state in completeAutomata.states:
			for symbol in completeAutomata.symbols:
				if completeAutomata.transitions[state][symbol] == []:
					completeAutomata.addTransition(state, symbol, "P")

		return completeAutomata


	def determinizationAndCompletion(self) -> "Automata":
		if self.isDeterministic() and self.isComplete():
			return self

		cdfa = self.copy()

		if not cdfa.isDeterministic():
			cdfa = cdfa.determinization()

		if not cdfa.isComplete():
			cdfa = cdfa.completion()

		return cdfa


	def findEpsilonClosure(self, state: str) -> list:
		if not self.isAsyncronous():
			return [state]
		
		epsilonclosure = []
		queue = [state]

		while queue:
			current = queue.pop(0)
			epsilonclosure.append(current)
			for temp in self.transitions[current].get('E'):
				queue.append(temp)

		return sorted(epsilonclosure)


	def complementary(self) -> "Automata":
		complementaryAutomata = self.copy()
		complementaryAutomata.final_state = [state for state in self.states if state not in self.final_state]

		return complementaryAutomata

	def readWord(self, word: str) -> bool:
		if not self.isDeterministic():
			print("Can't read word: FA is not deterministic")
			return False

		currentstate = self.initial_state[0]

		for current in word:
			print(current)


def parseAutomataFromFile(path: str) -> Automata:
	try:
		file = open(path, "r")
	except Exception as e:
		print(e)
		return None

	file = file.readlines()

	# Number of symbols
	nosym = int(file[0])
	
	# Number of states
	nosta = int(file[1])
	
	# Initial states
	insta = file[2].split(' ')
	insta.pop(0)
	if len(insta) != 0:
		insta[-1] = insta[-1].removesuffix('\n')

	# Final states
	fista = file[3].split(' ')
	fista.pop(0)
	if len(fista) != 0:
		fista[-1] = fista[-1].removesuffix('\n')

	# Checking if automata is asyncronous
	asyncronous = False
	for transition in file[5:]:
		if "E" in transition: asyncronous = True

	newAutomata =  Automata(nosym, nosta, insta, fista, asyncronous)

	# Number of transitions
	# We can ignore this line

	# Transitions
	for trans in file[5:]:
		trans = parseTransition(trans)
		newAutomata.addTransition(trans[0], trans[1], trans[2])
		
	return newAutomata

def parseTransition(transition: str) -> list:
	i = 0
	while transition[i] not in "abcdefghijklmnopqrstuvwxyzE":
		i += 1

	return [transition[:i], transition[i], transition[i+1:].removesuffix('\n')]

def mergeSortList(transition: list, sep: str = '') -> str:
	# ['0', '1', '2', '5'] => '0125'
	transition = sorted(transition)
	return sep.join(transition)

def removeDuplicate(transition: list):
	return sorted(list(set(transition)))