import json
import ast
import os

def main():
    with open('nations.json') as nation_list:
        data = json.load(nation_list)
        nation_count = len(data)

        knowledge_list = []
        temp_count = 0
        for nation in data:
            if temp_count != nation_count - 1:
                temp_json = json.dumps({ "Country.Id": int(nation['NationID']), "Value": 100 })
                temp_knowledge = ast.literal_eval("{}".format(temp_json))
                knowledge_list.append(temp_knowledge)
            else:
                temp_json = json.dumps({ "Country.Id": int(nation['NationID']), "Value": 100 })
                temp_knowledge = ast.literal_eval("{}".format(temp_json))
                knowledge_list.append(temp_knowledge)

            temp_count += 1

    amended_scout = add_knowledge(knowledge_list)
    if amended_scout:
        print("Scout knowledge has been amended successfully.")

def add_knowledge(knowledge_list):
    scout_list = os.listdir("scouts/")
    for scout_details in scout_list:
        f = open("scouts/{}".format(scout_details), "r")
        scout_json = json.loads(f.read())
        scout_json['Knowledge'] = knowledge_list
        f.close()
        f = open("scouts/{}".format(scout_details), "w")
        f.write(json.dumps(scout_json))
        f.close()

    return True


if __name__ == '__main__':
    main()


