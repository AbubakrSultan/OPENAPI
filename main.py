import requests
import yaml

yaml_file = requests.get(
    "https://raw.githubusercontent.com/open-data/OpenCanadaAPI/main/openapi.yaml"
).text
data = yaml.safe_load(yaml_file)


def findkeys(node, kv):
    if isinstance(node, list):
        for i in node:
            for x in findkeys(i, kv):
                yield x
    elif isinstance(node, dict):
        if kv in node:
            yield node[kv]
        for j in node.values():
            for x in findkeys(j, kv):
                yield x


numbers, values = [], []
with open("output.txt", "w") as f:
    for i in list(findkeys(data, "description")):
        values.append(f"{i}\n")

    for i in range(len(list(findkeys(data, "description")))):
        f.write(f"{i + 1}. {values[i]}")
