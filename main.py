import pandas as pd

fieldnames = ['Username', 'Password', 'Account Status', 'Region', 'Email', 'Summoner Name', 'BE', 'RP', 'RP Refunds',
              'Level', 'Curr Rank', 'Prev Rank', 'Champs', 'Skins', 'Last Played']

# pathcsv = "bruh.csv"
pd.set_option('display.max_rows', 0)
pd.set_option('display.max_columns', 0)
pd.set_option('display.width', 0)

# Load csv file into variable df
def load():
    global df
    df = pd.read_csv("bruh.csv")


def up(range1, range2):
    print(df[['Username', 'Password']][range1:range2])


def numericalSearch(header, queryValue, numeration, order):
    result = 0
    queryValue = int(queryValue)
    if order == 'A':
        order = True
    else:
        order = False

    sortedCSV = df.sort_values(header, ascending=order)
    result = sortedCSV

    if numeration == "more":
        result = sortedCSV.loc[sortedCSV[header] > queryValue]
    if numeration == "less":
        result = sortedCSV.loc[sortedCSV[header] < queryValue]
    return result

def regularSearch(header, order):
    if order == 'A':
        order = True
    else:
        order = False
    result = df.sort_values(header, ascending=order)
    print(result)

def randSearch(query):
    # USING FOR LOOP SO IT SEARCHES THROUGH EVERY FIELD, IF IT COULD SEARCH THROUGH ENTIRE DF THATD BE BETTER
    for field in fieldnames:
        new_df = df[df[field].str.contains(query, na=False)]
        new_df = new_df.sort_values('Username', ascending=True)
        if(new_df.shape[0] != 0):
            print(new_df)

#    new_df = df[df['Username'].str.contains('z', na=False)] SEARCHES FOR CONTAINING STRING IN DF
#    new_df = new_df.sort_values('Username', ascending=True) SORTS NEW DF ON USERNAME
#    print(new_df) PRINTS IT



# up()
# search("RP", 200, "more")
load()
randSearch("Unverif")
#header = input("Enter header\n")
#queryValue = input("Enter query\n")
#numeration = input("More/Less\n")
#order = input("Ascending/Descending (A/D)\n")
#if(header == 'BE' or header == 'RP' or 'Level' or 'Champs' or 'Skins'):
#    print(numericalSearch(header, queryValue, numeration, order))
#else:
#    regularSearch(header, order)

