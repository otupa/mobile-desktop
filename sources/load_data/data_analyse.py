""" Analyse informations from LoadData """

from typing import List, Tuple
from collections import Counter


class DataAnalyse:
    """ analyse elements of object """

    def set_incidences(self, data_frame: List) -> List:
        """ This method count how many
        incidences of an int
        and return a Dict
        """
        dict_ = dict(Counter([(item[1], item[2]) for item in data_frame]))
        return [[item[0], dict_[item], item[1]] for item in dict_]


    def analyse_faturation(self, porcents: Tuple) -> List:
        """ result of analysis """
        return self.apply_calc(porcents)


    def apply_calc(self, porcent: Tuple) -> List:
        """ extruture dataframe """
        data_frame = [self.set_porcent(item, porcent) for item in self.get_incidences()]
        for item in data_frame:
            item.append(self.calc_total_receved(item))
            item.append(self.calc_porcent(item))
        return data_frame, self.calc_total_faturation(data_frame)


    def calc_total_faturation(self, data_frame: List) -> List:
        """ calculate total faturtion data """
        total_amount = sum([(item[1]) for item in data_frame])
        total_receved = sum([(item[4]) for item in data_frame])
        total_revenue = sum([(item[5]) for item in data_frame])
        total_porcent = total_revenue * 100 / total_receved
        return (
            "total",
            total_amount,
            "=",
            round(total_porcent, 2),
            total_receved,
            total_revenue,
            )


    def calc_total_receved(self, data: List) -> int:
        """ multiply valor an amount """
        return data[0] * data[1]


    def calc_porcent(self, data: List) -> float:
        """ define revenue valor """
        return data[3] * data[4] / 100


    def set_porcent(self, data: List, porcent: Tuple) -> List:
        """ define a porcent values for incidences """
        if data[0] == 10:
            if data[2] == "+":
                return [data[0], data[1], data[2], porcent[0][0]]
            if data[2] == "-":
                return [data[0], data[1], data[2], porcent[1][0]]
        elif data[0] <= 20:
            if data[2] == "+":
                return [data[0], data[1], data[2], porcent[0][1]]
            if data[2] == "-":
                return [data[0], data[1], data[2], porcent[1][1]]
        elif data[0] >= 20:
            if data[2] == "+":
                return [data[0], data[1], data[2], porcent[0][2]]
            if data[2] == "-":
                return [data[0], data[1], data[2], porcent[1][2]]
