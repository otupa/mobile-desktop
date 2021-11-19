''' Tkinter Functions to user Interactions '''


from datetime import datetime
from tkinter.constants import END, TRUE
from typing import List
import locale
from tkinter import filedialog
from sources import DataExtructure


from sources import (
    extract,
    DataExtructure,
    create_sql_table,
    insert_data,
    search_runs,
    show_tables,
    ConfigJson
    
)

from . main import *



class TkFunctions():        
    """Functions for UI interactios"""
    def list_moto(self):
        data = self.config.get_records()
        list_ = [item[0] for item in data]
        if list_ == []: list_ = ["not motorists"]
        return list_

    def insert_treeview_data(self, data_frame: List) -> None:
        """Insert in Treeview Data"""
        self.dataTreeview.delete(
            *self.dataTreeview.get_children())
        [self.dataTreeview.insert(
            "", END, values=(data[0], locale.currency(data[1]), data[2]))
                                for data in data_frame]

    def insert_treeview_result(self, data_frame: List) -> None:
        """Insert in Treeview Result"""
        self.resultTreeview.delete(
            *self.resultTreeview.get_children())
        [self.resultTreeview.insert(
            "", END, values=(
                data[0], data[1], data[2], data[3], data[4], data[5]))
                                        for data in data_frame]

    def pick_date(self, option: int) -> datetime:
        """Formate date in correct format"""
        if option == 0:
            return datetime.strptime(self.leftCalendar.get(), '%d/%m/%Y')
        elif option == 1:
            return datetime.strptime(self.rightCalendar.get(), '%d/%m/%Y')
        
    def search_(self):
        """Search Motorist Faturation"""
        date_one = self.pick_date(0)
        date_two = self.pick_date(1)
        name = self.stringVar.get()
        porcents = self.check_porcent(name)

        # analyse informations
        data_frame = search_runs(name, date_one, date_two)
        motorist = DataExtructure(
            name, 
            (date_one, date_two), 
            data_frame, 
            porcents,
            )
        result = motorist.get_result_faturation_list()

        self.insert_treeview_data(data_frame)
        self.insert_treeview_result(result)

    def export_pdf(self) -> None:
        """Export a pdf File in specific directory"""
        directory = filedialog.askdirectory()
        date_one = self.pick_date(0)
        date_two = self.pick_date(1)
        name = self.stringVar.get()
        if name == 'MOTORISTAS':
            return None

        data_frame = search_runs(name, date_one, date_two)
        porcents = self.check_porcent(name)
        motorist = DataExtructure(name, (date_one, date_two), data_frame, porcents)
        motorist.report_pdf(directory, [date_one, date_two]) 
    
    def check_porcent(self, name: str) -> List:
        state = self.config.get_record_porcent(name)
        porcents = self.config.get_values_list()
        if state == 0:
            return [porcents[0], porcents[1]]
        elif state == 1:
            return [porcents[2], porcents[3]]

    def export_all(self):
        """Report Pdf for All Motrists"""
        date_one = self.pick_date(0)
        date_two = self.pick_date(1)
        directory = filedialog.askdirectory()
        for name in self.list_moto():
            data_frame = search_runs(name, date_one, date_two)
            porcents = self.check_porcent(name)
            if not data_frame: continue
            motorist = DataExtructure(name, (date_one, date_two), data_frame, porcents)
            motorist.report_pdf(directory, [date_one, date_two])

                
    def importar(self):
        extract(filedialog.askdirectory(), 'G4 MOBILE', 'reais')
        create_sql_table()
        insert_data()
        self.list_moto()


    def load_motorists(self) -> None:
        """Insert motorists data in list boxes"""
        self.config.mod_record_list(show_tables())
        data = self.config.get_records()
        print(data)
        # for item in :
        #     print(item)
        #     if item[1].get('porcent') == 0:
        #         self.fist_list_box.insert(END, item[0])
        #     elif item[1].get('porcent') == 1:
        #         self.second_list_box.insert(END, item[0])



    def move_right(self):
        indice = self.fist_list_box.curselection()[0]
        name = self.fist_list_box.get(indice)
        self.second_list_box.insert(END, name)
        self.fist_list_box.delete(indice)
        self.config.mod_records(name, 1)

    def move_left(self):
        indice = self.second_list_box.curselection()[0]
        name = self.second_list_box.get(indice)
        self.fist_list_box.insert(END, name)
        self.second_list_box.delete(indice)
        self.config.mod_records(name, 0)

    def set_porcents(self):
        self.config.mod_values([
            [
                self.var_porcent_one.get(),
                self.var_porcent_two.get(),
                self.var_porcent_tree.get()
            ],
            [
                self.var_porcent_desc_one.get(),
                self.var_porcent_desc_two.get(),
                self.var_porcent_desc_tree.get()
            ],
            [
                self.var_porcent_special_one.get(),
                self.var_porcent_special_two.get(),
                self.var_porcent_special_tree.get()
            ],
            [
                self.var_porcent_special_desc_one.get(),
                self.var_porcent_special_desc_two.get(),
                self.var_porcent_special_desc_tree.get()
            ]
        ])

        
    def reset_values(self):
        self.config.mod_values((
            ((10, 15, 20), (-90, -15, -20)),
            ((10, 15, 20), (-90, -15, -20)),
        ))
