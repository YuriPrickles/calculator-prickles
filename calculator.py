
print("Calculator")

operator_list = "+-*/"

class Expression:
	operator:str = ""
	term1 = 0
	term2 = 0
	def __init__(self,op,t1,t2):
		self.operator = op
		self.term1 = t1
		self.term2 = t2
	def evaluate_expression(self,t1,t2,op):
		match op:
			case "+":
				return t1 + t2
			case "-":
				return t1 - t2
			case "*":
				return t1 * t2
class Main:
	saved_answer = 0
	def run_calc(self):
		first_loop = True
		while True:
			operator_input = input(f"Input operator [+][-][*][/]\n[Q] to exit\n")

			if operator_input.upper() == "Q":
				print(f"Goodbye.\n\nLast saved result: {self.saved_answer}")
				break

			if len(operator_input) != 1 or not operator_list.__contains__(operator_input):
				raise Exception(f"Operation \"{operator_input}\" not recognized\nLast saved resuklt: {self.saved_answer}")

			term1_input = input(f"Input first term of [x] {operator_input} y\nLeave blank to use previous result: [{"" if not first_loop else self.saved_answer}]\n")
			term1_input = self.saved_answer if not term1_input else int(term1_input)

			term2_input = input(f"Input second term of {term1_input} {operator_input} [y]\nLeave blank to use previous result: [{"" if not first_loop else self.saved_answer}]\n")
			term2_input = self.saved_answer if not term2_input else int(term2_input)

			expr = Expression(operator_input, term1_input, term2_input)
			expr_answer = expr.evaluate_expression(expr.term1,expr.term2,expr.operator)
			self.saved_answer = expr_answer

			print(f"{term1_input} {operator_input} {term2_input} = {expr_answer}")
			first_loop = False
		exit()

instance = Main()
instance.run_calc()