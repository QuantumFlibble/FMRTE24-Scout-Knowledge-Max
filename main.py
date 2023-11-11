import json
import os

def main():
    with open('nations.json') as nation_list:
        data = json.load(nation_list)

        knowledge_list = [{"Country.Id": int(nation['NationID']), "Value": 100} for nation in data]

    amended_scout = add_knowledge(knowledge_list)
    if amended_scout:
        print("Scout knowledge has been amended successfully.")

def add_knowledge(knowledge_list):
    scout_list = os.listdir("scouts/")
    for scout_details in scout_list:
        with open(os.path.join("scouts", scout_details), "r") as f:
            scout_json = json.load(f)
        scout_json['Knowledge'] = knowledge_list
        with open(os.path.join("scouts", scout_details), "w") as f:
            json.dump(scout_json, f)

    return True

if __name__ == '__main__':
    main()