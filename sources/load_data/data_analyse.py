""" Analyse informations from LoadData """

from typing import Dict, List, Tuple
from collections import Counter

import locale

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

class DataAnalyse:
    """ Analyse data for the faturation document """
    def analyse_faturation(self) -> List:
        """ Pick incidences in the list"""
        incidences = Counter([(item[1], item[2]) for item in self.data_list])
        result_list =  list([[item[0], incidences[item], item[1]] for item in incidences])


        
        for item in result_list:
            item.append(item[0] * (item)[1])
            item.append(item[3] * self.set_porcent(item) / 100)
        

        total_runs = sum([abs(item[1]) for item in result_list])

        total_receved = [item[3] for item in result_list]

        total_receved_desc = sum([item[3] for item in result_list if item[2] == '-'])
        print(total_receved_desc)

        total_to_pay = sum([item[4] for item in result_list])

        if total_to_pay <= 50:
            total_to_pay = 50 - total_receved_desc

        for item in result_list:
            value = item.pop(2)
            if value == "-":
                item[2] = item[2] * -1

        
        result_list.append([
            0,
            total_runs,
            sum(total_receved),
            total_to_pay
        ])

        return result_list

    def set_porcent(self, data) -> List:
        """define a porcent values for incidences"""
        porcents = self.porcents
        if data[0] >= 0 and data[0] <= 12:
            if data[2] == "+":
                return porcents[0][0]
            if data[2] == "-":
                return porcents[1][0]
        if data[0] >= 13 and data[0] <= 22:
            if data[2] == "+":
                return porcents[0][1]
            if data[2] == "-":
                return porcents[1][1]
        if data[0] >= 23:
            if data[2] == "+":
                return porcents[0][2]
            if data[2] == "-":
                return porcents[1][2]


