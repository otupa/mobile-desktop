list_ = [
    ["31-01-2021 11:33", 11, "+"],
    ["31-01-2021 11:55", 11, "+"],
    ["31-01-2021 13:04", 11, "+"],
    ["31-01-2021 13:32", 11, "+"],
    ["31-01-2021 13:51", 60, "+"],
    ["31-01-2021 16:52", 11, "+"],
]

from load_data import DataExtructure

motorista = DataExtructure(
    "mariano_tupa", 
    ("10-10-10", "10-10-10"),
    list_,
    [
        [
            10,
            15,
            20
        ],
        [
            10,
            15,
            20
        ]
    ],
    ).get_result_faturation()
