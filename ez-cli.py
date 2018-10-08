#!/usr/bin/env python3

import subprocess, readline

CLI_CMD = ["HELP", "QUIT"]

class CLIMate():
	def __init__(self):
		self.run = None
		self.arg = ""
		self.fnc = [("help", self.help), ("quit", self.quit)]

		readline.parse_and_bind('set editing-mode vi')
		readline.parse_and_bind('tab: complete')
		readline.set_completer(self.completer)

	def completer(self, text, state):
		options = [i for i in CLI_CMD if i.startswith(text.upper())]
		if (state < len(options)):
			return options[state]
		else:
			return None
 
	def get_args(self):
		self.run = self.sub_call
		self.arg = input("\nez-cli> ")
		if (self.arg == ""):
			self.get_help("nothing")
		else:
			for f in self.fnc:
				if (self.arg.lower().startswith(f[0])):
					self.run = f[1]
		self.run(self.arg)

	def quit(self, parm):
		print("Goodbye.", "")

	def help(self, parm):
		print("EZ-CLI COMMANDS\n\tHELP - this\n\tQUIT - exit")

	def sub_call(self, parm):
		subprocess.run(['/bin/bash', '-i', '-c', parm + "&& exit"])
def main():
	cli = CLIMate()
	while not (cli.run == cli.quit):
		try:
			cli.get_args()
		except KeyboardInterrupt:
			print("Type QUIT to exit EZ-CLI")

if __name__ == "__main__":
	main()
