import json
from pcpartpicker import API

def main():
    api = API()
    raw_data = api.retrieve("cpu")
    json_data = json.loads(raw_data.to_json())
    print(type(json_data['cpu']))
    print(type(json_data['cpu'][0]))

if __name__ == "__main__":
    main()