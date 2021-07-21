import os
import parsing
import pandas as pd

fieldnames = ['Username', 'Password', 'Account Status', 'Region', 'Email', 'Summoner Name', 'BE', 'RP', 'RP Refunds',
              'Level', 'Curr Rank', 'Prev Rank', 'Champs', 'Skins', 'Last Played']

pathCSV = "bruh.csv"
pd.set_option('display.max_rows', 0)
pd.set_option('display.max_columns', 0)
pd.set_option('display.width', 0)

# Load csv file into variable df
def load(path):
    global df
    df = pd.read_csv(pathCSV)


def up(range1, range2):
    print(df[['Username', 'Password']][range1:range2])


def numericalSearch(header, opr, queryValue, order):
    result = 0
    queryValue = int(queryValue)
    if order == 'A':
        order = True
    else:
        order = False

    sortedCSV = df.sort_values(header, ascending=order)
    result = sortedCSV

    result = sortedCSV.loc[parsing.operator_dict[opr](sortedCSV[header], queryValue)]

    result.to_csv('result.csv', sep=',', encoding='utf-8')
    openFile('result.csv')
    return result

def regularSearch(header, order):
    if order == 'A':
        order = True
    if order == 'D':
        order = False
    result = df.sort_values(header, ascending=order)
    print(result)

def randSearch(query, field):
    if(field != None):
        field = field.replace('_', ' ')
    if(fieldnames.__contains__(field)):
        new_df = df[df[field].str.contains(query, na=False)]
        new_df = new_df.sort_values('Username', ascending=True)
        if (new_df.shape[0] != 0):
            new_df.to_csv('result.csv', sep=',', encoding='utf-8')
            openFile('result.csv')
        else:
            print("No results")
        return
    else:
        print("Unknown field")



def openFile(fileName):
    print('Opening', fileName + '...')
    os.system(fileName)

#    new_df = df[df['Username'].str.contains('z', na=False)] SEARCHES FOR CONTAINING STRING IN DF
#    new_df = new_df.sort_values('Username', ascending=True) SORTS NEW DF ON USERNAME
#    print(new_df) PRINTS IT


# up()
# search("RP", 200, "more")
load(pathCSV)
#randSearch("Unverif")
#header = input("Enter header\n")
#queryValue = input("Enter query\n")
#numeration = input("More/Less\n")
#order = input("Ascending/Descending (A/D)\n")
#if(header == 'BE' or header == 'RP' or 'Level' or 'Champs' or 'Skins'):
#    openFile(numericalSearch(header, queryValue, numeration, order))
#else:
#    regularSearch(header, order)

