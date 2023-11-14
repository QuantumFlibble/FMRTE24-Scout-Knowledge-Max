#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import os


# This script will add knowledge of all nations to any exported scout files in the scouts folder
def main():
    """
    Main function of the script.
    Calls the add_knowledge function to add knowledge of all nations to the scout files.
    """

    with open('nations.json') as nation_list:
        data = json.load(nation_list)

        # Create a list of dictionaries containing the nation ID and the scout's knowledge of that nation
        knowledge_list = [{'Country.Id': int(nation['NationID']), 'Value': 100} for nation in data]

    # Call the add_knowledge function to add knowledge of all nations to the scout files
    amended_scout = add_knowledge(knowledge_list)
    if amended_scout:
        print('Scout knowledge has been amended successfully.')


def add_knowledge(knowledge_list):
    """
    Adds knowledge of all nations to the scout files in the scouts folder.
    :param knowledge_list: A list of dictionaries containing the nation ID and the scout's knowledge of that nation
    """

    scout_list = os.listdir('scouts/')
    for scout_details in scout_list:
        with open(os.path.join('scouts', scout_details), 'r') as f:
            scout_json = json.load(f)
        scout_json['Knowledge'] = knowledge_list
        with open(os.path.join('scouts', scout_details), 'w') as f:
            json.dump(scout_json, f)

    return True


# Run the main function
if __name__ == '__main__':
    main()
