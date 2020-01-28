from pcpartpicker import API
import json

#TODO: Write tests for format_data ASAP

class DataHandler:
    def __init__(self):
        self.api = API()

    def init_data(self):
        """Init the raw data from pcpartpicker api so that it can be formatted into json later"""
            
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

        #TODO: This format isn't gonna work. We need a list of lists of dictionaries
        formatted_data = [dict(),dict(),dict(),dict(),dict(),dict(),dict()]

        for i in range(0,len(json_data)):
            for k in range(0,len(json_data[i])):
                formatted_data[i] = {"brand": json_data[k]["brand"],
                                     "model": json_data[k]["model"],
                                     "price": json_data[k]["price"][1]}
            

        return formatted_data