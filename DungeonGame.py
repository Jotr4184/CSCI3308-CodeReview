"""
	Josh Trujillo
	9/08
	HW#2 Dungeon Game
"""

print("Welcome to Josh's Dungeon!")

currentRoom = 'kitchen'
userCommand = ''

while userCommand != 'q':
	if currentRoom == 'kitchen':
		userCommand = input("You are in the kitchen. There are doors to the west (w), south (s) and east (e).")
		
		if userCommand == 's':
			currentRoom = 'furnace'
		
		elif userCommand == 'w':
			currentRoom = 'hallway'
		
		elif userCommand == 'e':
			currentRoom = 'living room'
	
	elif currentRoom == 'hallway':
		userCommand = input("You are in the hallway. There are doors to the north (n), south (s) and east (e).")
		
		if userCommand == 'e':
			currentRoom = 'kitchen'
		
		elif userCommand == 's':
			currentRoom = 'library'
		
		elif userCommand == 'n':
			currentRoom = 'bedroom'
	
	elif currentRoom == 'bedroom':
		userCommand = input("You are in the bedroom. There are doors to the south (s), and north (n).")
		
		if userCommand == 's':
			currentRoom = 'hallway'
			
		elif userCommand == 'n':
			currentRoom = 'office'
	
	elif currentRoom == 'office':
		userCommand = input("You are in the office. There are doors to the north (n) and south (s).")
		
		if userCommand == 's':
			currentRoom = 'bedroom'
			
		elif userCommand == 'n':
			currentRoom = 'laboratory'
	
	elif currentRoom == 'laboratory':
		userCommand = input("You are in the laboratory. There is a door to the south (s).")
		
		if userCommand == 's':
			currentRoom = 'office'
			
	elif currentRoom == 'living room':
		userCommand = input("You are in the living room. There is a door to the west (w).")
		
		if userCommand == 'w':
			currentRoom = 'kitchen'
	
	elif currentRoom == 'library':
		print("You are in the library. You found the Princess! You are a Hero!")
		userCommand = 'q'	
	
	elif currentRoom == 'furnace':
		print("You entered the furnace and fry yourself to death!")
		userCommand = 'q'
print("Goodbye!")
		

