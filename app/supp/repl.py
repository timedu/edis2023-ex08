
from supp.utils import send_request
from supp.config import todo

import traceback

try:
    import readline
except:
    pass 

def repl(prompt):

    while True:

        try:
            user_input = input(prompt)

        except EOFError:
            print('')
            break        

        if not user_input.strip():
            continue

        input_strings = user_input.split()

        command = input_strings[0].lower()

        try:

            if len(input_strings) == 1:

                if command in ('exit', 'quit'):
                    break

                if command == 'list':

                    response = send_request({'operation': 'list'})
                    print(response)
                    continue 

                if command == 'reset':

                    todo['handlers'].reset()
                    continue 

            if len(input_strings) == 2:

                assert all(char.isdigit() for char in input_strings[1])
                key = int(input_strings[1])

                if command == 'set':

                    todo['handlers'].set(key)
                    continue 

                if command == 'del':

                    todo['handlers'].remove(key)
                    continue

                if command == 'get':

                    todo['handlers'].get(key)
                    continue
                
            raise AssertionError

        except AssertionError:
            print('Usage: { {set|get|del} <int> } | list|reset | exit|quit }')

        except Exception as err:
            print(err)
            traceback.print_exc()
