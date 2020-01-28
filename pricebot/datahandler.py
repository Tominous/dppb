from pcpartpicker import API
import json

#TODO: Write tests for format_data ASAP

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
        for i in range(0,len(self.raw_data)):
            #A stupidly long oneliner to remove the unecessary object at the start of the json
            json_data[i] = json.loads(self.raw_data[i].to_json())[next(iter(json.loads(self.raw_data[i].to_json())))]

        #A list of dictionaries of a list of dictionaries
        formatted_data = {"cpu": [], 
                          "gpu": [], 
                          "psu": [], 
                          "ram": [],
                          "mobo": [],
                          "hdd": [],
                          "case": []}

        for i in range(0,len(json_data)):
            formatted_data[next(iter(formatted_data))].append({
                                                                     (str(json_data[i]["brand"]) + " " + str(json_data[i]["model"])): 
                                                                      "$" + str(json_data[i]["price"][1])
                                                                   })
        return formatted_data

    def get_part_data(self, part):
        """Retrieve the data on a particular part out of the mess that is the return of format_data
           Parts must be cpu, gpu, psu, ram, mobo, hdd, or case"""
        return self.format_data()[part]