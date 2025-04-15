command = ""
command_list = [
    '(command to start car) : start',
    '(command to stop car) : stop',
    '(command to quit game) : quit'
]

while command != "quit":
    command = input("<type command>: ").lower()

    if command == 'start':
        print('Car started.')
    elif command == 'stop':
        print("Car stopped.")
    elif command == 'help':
        print("Here is the command list:")
        for item in command_list:
            print(f" - {item}")
    elif command == 'quit':
        print("Game exited.")
    else:
        print("I don't understand that command.")
