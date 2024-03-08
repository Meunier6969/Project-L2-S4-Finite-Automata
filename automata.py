from typing import Optional

class Automata:
	symbols: int = 0
	states: int = 0
	initial_state: list[int] = []
	final_state: list[int] = []
	# State -> Symbol -> Transition (Null or tuple)
	transitions: list[list[Optional[tuple]]] = [[]]

	def __init__(self, sym: int, sta: int, i_sta: list[int], f_sta: list[int]) -> None:
		print(f"Initializing Automata : {self}...")
		self.symbols = sym
		self.states = sta
		self.initial_state = i_sta
		self.final_state = f_sta
		self.transitions = [[None for _ in range(self.symbols)] for _ in range(self.states)]

	def displayTransition(self) -> None:
		SYM = [chr(i) for i in range(97, 126)]

		# Top row
		print(f"{' ':10}", end="")
		for _ in range(self.symbols):
			print(f"{SYM[_]:<10}", end="")
		print()

		# Main table
		for i, state in enumerate(self.transitions):
			print(f"{i:<10}", end="")
			for trans in state:
				print(f"{str(trans):<10}", end="")
			print()


	def display(self) -> None:
		print("Symbols : ", self.symbols)
		print("States : ", self.states)
		print("Initial States : ", self.initial_state)
		print("Final States : ", self.final_state)


def parseAutomataFromFile() -> Automata:
	pass