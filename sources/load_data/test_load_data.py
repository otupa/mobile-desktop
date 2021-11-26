from typing import List, Type
from .load_data import DataExtructure
from pandas import DataFrame
from pytest import mark

list_ = [
    ["31-01-2021 11:33", 11, "-"],
    ["31-01-2021 11:55", 13, "+"],
    ["31-01-2021 13:04", 13, "+"],
    ["31-01-2021 13:32", 16, "+"],
    ["05-02-2021 18:44", 16, "+"],
    ["05-02-2021 19:06", 25, "+"],
    ["05-02-2021 19:27", 25, "+"],
    ["06-02-2021 13:38", 11, "+"],
    ["06-02-2021 14:01", 11, "+"],

]


porcent = {
    "12":(10, -90),
    "13":(15, -85),
    "23":(20, -80),
    }

args = [list_, porcent]

def test_get_result_faturation_return_pd_dataframe():
    app = DataExtructure(*args)
    result = app.analyse_faturation()
    assert type(result) == list

def test_result_faturation():
    app = DataExtructure(*args)
    result = app.get_result()
    assert type(result) == list

