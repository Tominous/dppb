from pcpartpicker import API
import json

#TODO: Write tests for format_data ASAP

class InvalidPart(Exception):
    pass

class DataHandler:
    def __init__(self):
        self.api = API()
        self.raw_data =[self.api.retrieve("cpu"), 
                        self.api.retrieve("video-card"), 
                        self.api.retrieve("power-supply"), 
                        self.api.retrieve("memory"), 
                        self.api.retrieve("motherboard"), 
                        self.api.retrieve("internal-hard-drive"), 
                        self.api.retrieve("case")]

    def format_data(self):
        """Convert self.raw_data into json, get the data we need, and return a list with the data on various parts"""

        json_data = [None, None, None, None, None, None, None]
        for i in range(len(self.raw_data)):
            top_level_key = next(self.raw_data[i].keys())
            json_data[i] = json.loads(self.raw_data[i].to_json())[top_level_key]

        formatted_data = {"cpu": [], 
                          "gpu": [], 
                          "psu": [], 
                          "ram": [],
                          "mobo": [],
                          "hdd": [],
                          "case": []}

        key = next(formatted_data).key()
        for i in range(0,len(json_data)):
            formatted_data[key].append({
                                        f"{json_data[i]['brand']} {json_data[i]['model']}": 
                                        f"${json_data[i]['price'][1]}"
                                      })
        return formatted_data

    def get_part_data(self, part):
        """Retrieve the data on a particular part out of the mess that is the return of format_data
           Parts must be cpu, gpu, psu, ram, mobo, hdd, or case"""
        try:
            return self.format_data()[part]
        except KeyError:
            raise InvalidPart("User entered a part that isn\'t supported/doesn\'t exist")