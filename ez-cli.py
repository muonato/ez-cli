#!/usr/bin/env python3

import subprocess, readline

CLI_CMD = []

class CLIMate():
	def __init__(self):
		self.run = None
		self.arg = ""
		self.fnc = []

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
					self.run = eval(f[1])
		self.run(self.arg)

	def cmd_quit(self, parm):
		print("Goodbye.", "")

	def cmd_help(self, parm):
		print("EZ-CLI COMMANDS\n\tHELP - this\n\tQUIT - exit")

	def sub_call(self, parm):
		try:
			subprocess.call(parm, shell=True)
		except KeyboardInterrupt:
			print("Terminated by keystroke")

def main():
	cli = CLIMate()

	for cmd in dir(CLIMate):
		if cmd.startswith("cmd_"): 
			cli.fnc.append((cmd[4:], 'self.' + cmd))
			CLI_CMD.append(cmd[4:].upper())

	while not (cli.run == cli.cmd_quit):
		try:
			cli.get_args()
		except KeyboardInterrupt:
			print("Type QUIT to exit EZ-CLI")

if __name__ == "__main__":
	main()
