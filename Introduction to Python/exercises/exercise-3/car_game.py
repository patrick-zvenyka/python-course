command = ""
command_list = [
    'start car: start',
    'stop car: stop',
    'quit game: quit'
]
started = False
while True:
    command = input("<type command>: ").lower()

    if command == 'start':
        if started:
            print('Car already started')
        else:
            started = True
            print('Car started.')

    elif command == 'stop':
        if not started:
            print('Car is already stopped!')
        else:
            started = False
            print("Car stopped.")


    elif command == 'help':
        print("Here is the command list:")
        for item in command_list:
            print(f" - {item}")
    elif command == 'quit':
        print("Game exited.")
        break
    else:
        print("I don't understand that command.")
