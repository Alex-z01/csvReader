import operator
import main

commands_dict = {
    '-search': 'Search a CSV with numerical comparison. Ex -search Money > 1500',
    '-contains': 'Search a CSV for a string. Ex -contains Bob Username',
    '-path': 'Change CSV file path. Ex -path logins.csv',
    '-open': 'Open CSV file. Ex -open logins.csv',
    '-help': 'View commands',
}

help_dict = {
    '-search': '[field] [operator] [value]',
    '-contains': '[value] [field]',
    '-path': '[path]',
    '-open': '[path]'
}

operator_dict = {
    '>': operator.gt,
    '>=': operator.ge,
    '<': operator.lt,
    '<=': operator.le,
    '=': operator.eq,
    '!=': operator.ne
}

numericalFields = [
    'BE',
    'RP',
    'RP_Refunds',
    'Level',
    'Champs',
    'Skins',
]

basicFields = [
    'Username',
    'Password',
    'Account_Status',
    'Region',
    'Email',
    'Summoner_Name',
    'Curr_Rank',
    'Prev_Rank',
    'Last_Played'
]


# command = None
def parseSearch():
    global command
    splits = command.split(' ')
    if (len(splits) == 4):
        if (numericalFields.__contains__(splits[1]) and operator_dict.__contains__(splits[2])):
            for split in splits:
                split = split.replace('_', ' ')
            main.numericalSearch(splits[1], splits[2], splits[3], 'D')
        else:
            print('Use -contains to search non-numerical fields.')
    else:
        print('Improper syntax, proper usage: -search', help_dict[splits[0]])


def parseContains():
    global command
    splits = command.split(' ')
    if (len(splits) == 3):
        for split in splits:
            split = split.replace('_', ' ')
        main.randSearch(splits[1], splits[2])
    else:
        print('Improper syntax, proper usage: -contains', help_dict[splits[0]])


def parsePath():
    global command
    splits = command.split(' ')
    if (len(splits) != 2):
        print('Improper syntax, proper usage: -path', help_dict[splits[0]])
    else:
        main.load(splits[1])

def parseOpen():
    global command
    splits = command.split(' ')
    if (len(splits) == 1):
        main.openFile(main.pathCSV)
    elif (len(splits) == 2):
        main.openFile(splits[1])
    else:
        print('Improper syntax, proper usage: -open', help_dict[splits[0]])


def commands():
    global command
    splits = command.split(' ')
    if commands_dict.__contains__(splits[0]):
        if (splits[0] == '-help'):
            print("\nCommands")
            for comm in commands_dict:
                print('\t', comm, ':', commands_dict[comm])
        if (splits[0] == '-search'):
            parseSearch()
        if (splits[0] == '-contains'):
            parseContains()
        if (splits[0] == '-path'):
            parsePath()
        if (splits[0] == '-open'):
            parseOpen()
    else:
        print('Command', command, 'does not exist\n')
    waitCommand()


def waitCommand():
    global command
    command = input('')
    commands()


print("Welcome to LolSearch\n")

# fullCommand = '-search BE > 100'
# cutCommand = fullCommand.replace('-search ','')
# s = cutCommand.split(' ')

waitCommand()
