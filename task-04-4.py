'''
Четверте завдання

Напишіть консольного бота помічника, який розпізнаватиме команди, що вводяться з 
клавіатури, та буде відповідати відповідно до введеної команди.

☝ Бот помічник повинен стати для нас прототипом застосунку-асистента, який ми 
озробимо в наступних домашніх завданнях. Застосунок-асистент в першому наближенні
 повинен вміти працювати з книгою контактів та календарем.
'''
import datetime


def say_hello():
    return "How can I help you?"
def parse_input(cmd_line:str):
    info = cmd_line.split(" ")
    info[0] = info[0].strip(" ").lower()
    return info

def add_contact(args, contacts) -> str:
    if len(args)<2:
        return "not enought information to add"
    name, phone = args
    if not name in contacts:
        contacts[name] = phone
        return "contact added"
    else:
        return "contact already exists"

def change_contact(args, contacts) -> str:
    if len(args)<2:
        return "not enought information to change"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "contact updated"
    else:
        return "contact not found"

def del_contact(args, contacts) -> str:
    if len(args)<1:
        return "need name to delete"
    name = args[0]
    if name in contacts:
        del contacts[name]
        return "contact deleted"
    else:
        return "contact not found"

def print_contact(contacts) -> list:
    items = list()
    if len(contacts)>0:
        for names, phones in contacts.items():
            items.append(f'{names},{phones}')
    return items


def get_phone(name, contacts):
    s = contacts.get(name)
    if s!=None:
        print(contacts[name])
        return 'successfully founded'
    else:
        return 'not found'

def curr_date():
    dt = datetime.datetime.now()
    return dt.strftime("%Y-%m-%d")

def curr_time():
    dt = datetime.datetime.now()
    return dt.strftime("%H:%M:%S")

def main():
    CLI_header = '****************************************\n'\
                 '**         Command line assistant     **\n'\
                 '****************************************\n'

    print(CLI_header)
    print(say_hello())
    contacts = dict()

    while True:
        text = input('Type here your command: ')
        cmds = parse_input(text)
        if cmds[0]=='help':
            print(CLI_header)
            print('type "list" to see all commands')
        elif cmds[0]=='list':
            print(  'bye, exit, close  - exit from assistant\n'\
                    'help              - get help\n'\
                    'add name phone    - add phone to contact list\n'\
                    'del name          - delete contact from list\n'\
                    'change name phone - update phone number for name\n'\
                    'all               - print all contact book\n'\
                    'phone name        - get phone number for name\n'\
                    'date              - get current date\n'\
                    'time              - get current time\n'\
                    'list              - get commands list')
        elif cmds[0] in ['bye','exit','close']:
            print('good bye')
            break
        elif cmds[0]=='hello':
            print(say_hello())
        elif cmds[0]=='add':
            print(add_contact(cmds[1:], contacts))
        elif cmds[0]=='del':
            print(del_contact(cmds[1:], contacts))
        elif cmds[0]=='change':
            print(change_contact(cmds[1:], contacts))
        elif cmds[0]=='phone':
            print(get_phone(cmds[1], contacts))
        elif cmds[0]=='all':
            contacts = print_contact(contacts)
            for i in contacts:
                print(i)
        elif cmds[0]=='date':
            print(curr_date())
        elif cmds[0]=='time':
            print(curr_time())
        else:
            print(f'I don\'t understand {cmds}')

if __name__ == "__main__":
    main()