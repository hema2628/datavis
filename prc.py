import json

import pandas as pd
import types

def read_data(path):
    data = pd.read_csv(path)
    data = data.dropna(subset=["Medal"])

    return data

def get_list(data, kw):
    res = data[kw]
    res = set(res)

    return res

def create_obj(data,cty_list,spt_list):

    obj_1 = {
        "name":"athlete",
        "children" :[]
    }

    for i in cty_list:
        obj_2 = {
            "name": i,
            "children": []
        }
        data_by_cty = data[data["NOC"] == i]

        if(len(data_by_cty)>0):
            print(len(data_by_cty))
            for j in spt_list:
                data_by_spt = data_by_cty[data_by_cty["Sport"] == j]

                if (len(data_by_spt) > 0):
                    obj_3 = {
                        "name": j,
                        "value": len(data_by_spt)
                    }
                    obj_2["children"].append(obj_3)
            obj_1["children"].append(obj_2)

    json_str = json.dumps(obj_1)
    with open('athlete2_zoomable_node_0_0.json', 'w') as json_file:
        json_file.write(json_str)

if __name__ == "__main__":
    data = read_data("athlete_events.csv")
    cty = get_list(data,"NOC")
    spt = get_list(data,"Sport")

    create_obj(data,cty,spt)