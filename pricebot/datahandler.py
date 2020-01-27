from pcpartpicker import API
import json

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
        for i in range(0,6):
            json_data[i] = json.load(self.raw_data[i].to_json())

        formatted_data = [dict(),dict(),dict(),dict(),dict(),dict(),dict()]

        for i in range(0,len(json_data)):
            for i in range(0,len(json_data[i])):
                pass
            

        return formatted_data