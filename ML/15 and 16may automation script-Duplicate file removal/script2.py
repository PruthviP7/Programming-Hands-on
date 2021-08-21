#Directory Handling script #python script2 Demo.....run kartanna asa takaycha...Demo he apla folder ch naav ahe

from sys import *
import os

def DirectoryTraversal(path):
	print("Contents of the directory are")

	for Folder, Subfolder, Filename in os.walk(path):	#return value of walk() function is..1)our parent folder name 2)Subfolder names and 3)File names
								#...which is of list type
		print("Directory name is : "+Folder)
		for sub in Subfolder:
			print("Subfolder of "+Folder+ " is " +sub)
		for file in Filename: 
			print("File name is "+file)

def main():
	print("Marvellous Infosystems")
	print("Directory traversal script")

	if(len(argv)!=2):
		print("Error : Invalid number of arguments")
		exit()

	if(argv[1]=="-h") or (argv[1] == "-H"):
		print("It is a Directory Cleaner script")
		exit()

	if(argv[1]=="-u") or (argv[1] == "-U"):
		print("Usage : Provide the absolute path of the target directory")
		exit()
	
	DirectoryTraversal(argv[1])

if __name__ == "__main__":
	main()