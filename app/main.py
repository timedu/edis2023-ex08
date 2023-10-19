

from os import environ 

'''
EDIS / Assignment 8
'''


if __name__ == '__main__':


    '''
    Parse arguments
    '''

    from  argparse import ArgumentParser

    parser = ArgumentParser(
        description='Assignment 8'
    )

    parser.add_argument(
        '-r', '--review', choices=['0', '1', '2'], default='0',
        help='whose code is being run, default: 0 (your code)'
    ) 
    args = vars(parser.parse_args())


    '''
    Import modules and update config
    '''

    from supp.repl import repl

    if args['review'] == '1':
         from todos.review_1 import requests, handlers 
    elif args['review'] == '2':
         from todos.review_2 import requests, handlers
    else:
         from todos.your_code import requests, handlers 

    import supp.config
    supp.config.todo['requests'] = requests     
    supp.config.todo['handlers'] = handlers     


    '''
    Run REPL
    '''

    client_type = environ.get('CLIENT_TYPE', '?')
    client_id = environ.get('HOSTNAME','??????????')[9:]
    todo_folder = 'your_code' if not int(args.get('review')) else f'review_{args["review"]}'

    repl(prompt = f'[{todo_folder} / client-{client_type}-{client_id}] > ')
