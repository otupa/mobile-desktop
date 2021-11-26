''' Tkinter Functions to user Interactions '''

from datetime import datetime
import locale

from tkinter.constants import END, TRUE
from typing import List
from tkinter import filedialog
from sources import DataExtructure

from sources import (
    extract,
    DataExtructure,
    create_sql_table,
    insert_data,
    search_runs,
    show_tables,
    ConfigJson,
    save_report
)

class TkFunctions():        
    """Functions for UI interactios"""
    def list_moto(self) -> List:
        """"Return a list with motorist name""" 
        list_ = [item[0] for item in self.config.get_records()]
        if list_ == []: list_ = ["not motorists"]
        return list_

    def insert_treeview_data(self, data_frame: List) -> None:
        """Insert in Treeview Data"""
        self.data_treeview.delete(
            *self.data_treeview.get_children())
        [self.data_treeview.insert(
            "", END, values=(data[0], data[1], data[2]))
                                for data in data_frame]

    def insert_treeview_result(self, data_frame: List) -> None:
        """Insert in Treeview Result"""
        self.result_treeview.delete(
            *self.result_treeview.get_children())
        [self.result_treeview.insert(
            "", END, values=(
                data[0], data[1], data[2], data[3]))
                                        for data in data_frame]

    def pick_date(self, option: int) -> datetime:
        """Formate date in correct format"""
        if option == 0:
            return datetime.strptime(self.left_calendar.get(), '%d/%m/%Y')
        elif option == 1:
            return datetime.strptime(self.right_calendar.get(), '%d/%m/%Y')
        
    def search_(self) -> None:
        """Search Motorist Faturation"""
        name = self.str_var.get()
        if name == "MOTORISTAS": return None

        date_one = self.pick_date(0)
        date_two = self.pick_date(1)

        porcents = self.check_porcent(name)

        data_frame = search_runs(name, date_one, date_two)
        motorist = DataExtructure(
            data_frame, 
            porcents,
            )

        result = motorist.get_result()

        self.insert_treeview_data(data_frame)
        self.insert_treeview_result(result)

    def export_pdf(self) -> None:
        """Export a pdf File in specific directory"""
        directory = filedialog.askdirectory()
        date_one = self.pick_date(0)
        date_two = self.pick_date(1)
        print(date_one, date_two)
        name = self.str_var.get()
        if name == 'MOTORISTAS': return None

        data_frame = search_runs(name, date_one, date_two)
        porcents = self.check_porcent(name)
        motorist = DataExtructure(data_frame, porcents)
        save_report(
            name.upper(),
            str(date_one)[:-9], str(date_two)[:-9],
            motorist.get_result(),
            directory)
        
        self.insert_treeview_data(data_frame)
        self.insert_treeview_result(motorist.get_result())
    
    def check_porcent(self, name: str) -> List:
        """Check porcents from Motorists"""
        state = self.config.get_record_porcent(name)
        if state == 0:
            return [self.porcents[0], self.porcents[1]]
        elif state == 1:
            return [self.porcents[2], self.porcents[3]]

    def export_all(self) -> None:
        """Report Pdf for All Motrists"""
        date_one = self.pick_date(0)
        date_two = self.pick_date(1)
        directory = filedialog.askdirectory()
        for name in self.list_moto():
            data_frame = search_runs(name, date_one, date_two)
            porcents = self.check_porcent(name)
            if not data_frame: continue
            motorist = DataExtructure(data_frame, porcents)
            save_report(
                name.upper(),
                str(date_one)[:-9], str(date_two)[:-9],
                motorist.get_result(),
                directory)
                
    def import_data(self) -> None:
        """Import Files Data for the System"""
        extract(filedialog.askdirectory(), 'G4 MOBILE', 'reais')
        create_sql_table()
        insert_data()
        self.list_moto()


    def load_motorists(self) -> None:
        """Insert motorists data in list boxes"""
        self.config.mod_record_list(show_tables())
        for item in self.config.get_records():
            if item[1] == 0:
                self.fist_list_box.insert(END, item[0])
            elif item[1] == 1:
                self.second_list_box.insert(END, item[0])



    def move_right(self) -> None:
        """Move record for right list box"""
        indice = self.fist_list_box.curselection()[0]
        name = self.fist_list_box.get(indice)
        self.second_list_box.insert(END, name)
        self.fist_list_box.delete(indice)
        self.config.mod_records(name, 1)

    def move_left(self) -> None:
        """Move record for left list box"""
        indice = self.second_list_box.curselection()[0]
        name = self.second_list_box.get(indice)
        self.fist_list_box.insert(END, name)
        self.second_list_box.delete(indice)
        self.config.mod_records(name, 0)

    def set_porcents(self) -> None:
        """Set porcents with window porcent"""
        self.config.mod_values([
            [
                int(self.var_porcent_one.get()),
                int(self.var_porcent_two.get()),
                int(self.var_porcent_tree.get())
            ],
            [
                int(self.var_porcent_desc_one.get()),
                int(self.var_porcent_desc_two.get()),
                int(self.var_porcent_desc_tree.get())
            ],
            [
                int(self.var_porcent_special_one.get()),
                int(self.var_porcent_special_two.get()),
                int(self.var_porcent_special_tree.get())
            ],
            [
                int(self.var_porcent_special_desc_one.get()),
                int(self.var_porcent_special_desc_two.get()),
                int(self.var_porcent_special_desc_tree.get())
            ]
        ])
        self.porcents = self.config.get_values()
