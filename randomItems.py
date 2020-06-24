import csv
import sys
from pprint import pprint
loot_table = 'LootTables/The One Loot Table To Rule Them All - Dungeon Loot.csv'
def read_table(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    loot_table = []
    itemNum = 1
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            if row[0] != '':
                dictionary = { 'ItemNumber': itemNum,
                    'Name': row[0],
                                'Description': row[1],
                                'Properties': row[7]
                                }
                loot_table.append(dictionary)
                itemNum+=1
    return loot_table


def print_item(my_item):
    print(f"You have received the: {my_item['Name']}")
    if my_item['Properties'] != '':
        print(f"This item has the following properties: {my_item['Properties']} ")

    print(f"The item has the following description: {my_item['Description']}")




loot = read_table(loot_table)
pprint(loot)
my_item = next((item for item in loot if item['ItemNumber'] == 485), None)

if my_item != None:
    print_item(my_item)
else:
    print("The item does not exist! Please try again")




