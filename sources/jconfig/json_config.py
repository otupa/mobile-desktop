import os
from json import load, dump
from typing import List

from settings import PROJECT_PATH

class ConfigJson():
    def __init__(self):
        self.archive = os.path.join(PROJECT_PATH, 'config')
        try:
            with open(self.archive, 'r') as file:
                self.data = load(file)
        except:
            self.data = {}
            self.base_config()


    def save_config(self):
        with open(self.archive, 'w') as file:
            dump(self.data, file, indent=3)


    def base_config(self):
        self.data["values"] = {"common":{}, "special":{}}
        self.data["values"]["common"] = {"normal":{}, "desc":{}}
        self.data["values"]["special"] = {"normal":{}, "desc":{}}
        self.data["records"] = {}
        self.save_config()


    def mod_records(self, name, porcent):
        self.data["records"][name] = {}
        self.data["records"][name]["porcent"] = porcent
        self.save_config()


    def mod_values(self, values: List) -> None:
        """Define Porcents In Config"""
        self.data["values"]["common"]["normal"] = values[0]
        self.data["values"]["common"]["desc"] = values[1]
        self.data["values"]["special"]["normal"] = values[2]
        self.data["values"]["special"]["desc"] = values[3]
        self.save_config()


    def del_record(self, name):
        del self.data["records"][name]
        self.save_config()


    def mod_record_list(self, record: List) -> None:
        """Set values for motorists"""
        for item in record:
            if not self.data["records"].get(item):
                self.mod_records(item, 0)
        self.save_config()


    def get_records(self) -> List:
        """Get a list with all records"""
        return [(item, value.get('porcent')) 
            for item, value in self.data["records"].items()]


    def get_values(self) -> List:
        """Get a list with Values"""
        return [
            self.data["values"]["common"]["normal"],
            self.data["values"]["common"]["desc"],
            self.data["values"]["special"]["normal"],
            self.data["values"]["special"]["desc"]
            ]
    
    def get_record_porcent(self, record:str) -> int:
        """Return a record porcent from 
        specific record"""
        return self.data["records"][record]["porcent"]