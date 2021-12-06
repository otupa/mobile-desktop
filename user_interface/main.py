''' User Interface - Tkinter '''

"""System Imports"""
from datetime import datetime, timedelta
import locale

from sources.mariadb_connect.connect_sql import show_tables

"""Grafical Interface Imports"""
from tkinter import Tk, ttk, filedialog
from tkinter import *
from tkcalendar import Calendar, DateEntry

"""Modules Imports"""
from sources import ConfigJson
from .functions_ui import TkFunctions

class Application(TkFunctions):
    '''Render UI
    FunctionsInterface is responsable 
    with integrate functions
    '''
    def __init__(self):
        """Contructor method for execute application"""
        self.window = Tk()
        self.config = ConfigJson()
        self.window.title("Soft G4")
        self.window.configure(background='#1e3743')
        self.window.geometry('1000x600')
        self.window.resizable(True, True)

        self.date_one = datetime.now()

        self.date_two = self.date_one - timedelta(days=7)
        
        self.porcents = self.config.get_values()

        """Define Brasil Locale for Currency"""
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


        """Render Components"""
        self.menu_bar()
        self.data_view()
        self.menu_view()
        self.list_box()

        """Initial Configurations"""
        self.load_motorists()

        """Loop for Application"""
        self.window.mainloop()

    def menu_bar(self):
        """Top Menu with sections of the software"""
        menu_bar = Menu(self.window, tearoff=0)
        self.window.config(menu=menu_bar)

        archives = Menu(menu_bar, tearoff=0)
        help_menu = Menu(menu_bar, tearoff=0)

        archives.add_command(label="Importar", command=self.import_data) 
        archives.add_command(label="Exportar", command=None)
        archives.add_command(label="Salvar csv", command=self.export_csv)
        archives.add_command(label="sair", command=None)
        menu_bar.add_cascade(label="Arquivo", menu=archives)
        menu_bar.add_cascade(label="Ajuda", menu=help_menu)


    def data_view(self):
        """Visualizations of Searchs"""
        self.frame_data_view = Frame(
            self.window, 
            bd=4, bg='#dfe3ee',
            highlightbackground='#759fe6', 
            highlightthickness=3)

        self.frame_data_view.place(
            relx=0.51, 
            rely=0.03, 
            relwidth=0.47, 
            relheight=0.95)

        """Treeview for Data Visualization"""
        self.data_treeview = ttk.Treeview(
            self.frame_data_view, 
            height=2,
            column=("coll1", "coll2", "coll3"))

        self.data_treeview.place(
            relx=0.02, 
            rely=0.51, 
            relwidth=0.96, 
            relheight=0.47)

        self.scroll_data = Scrollbar(
            self.data_treeview, 
            orient='vertical',
            command=self.data_treeview.yview)

        self.scroll_data.place(
            relx=0.96, 
            rely=0.016, 
            relwidth=0.03, 
            relheight=0.97)

        self.data_treeview.configure(
            yscrollcommand=self.scroll_data.set)
        
        self.data_treeview.heading("#0", text="")
        self.data_treeview.heading("#1", text="date-time")
        self.data_treeview.heading("#2", text="valor")
        self.data_treeview.heading("#3", text="op.")

        self.data_treeview.column("#0", width=40, stretch = "no")
        self.data_treeview.column("#1", width=140)
        self.data_treeview.column("#2", width=100)
        self.data_treeview.column("#3", width=80)

        """Treeview for Result Visualization"""
        self.result_treeview = ttk.Treeview(
            self.frame_data_view, height=3, 
            column=("coll1", "coll2", "coll3", "coll4"))

        self.result_treeview.place(
            relx=0.02, 
            rely=0.02, 
            relwidth=0.96, 
            relheight=0.47)

        self.scroll_result = Scrollbar(
            self.result_treeview, 
            orient='vertical', 
            command=self.result_treeview.yview)

        self.scroll_result.place(
            relx=0.96, 
            rely=0.016, 
            relwidth=0.03, 
            relheight=0.97)

        self.result_treeview.configure(
            yscrollcommand=self.scroll_result.set)

        self.result_treeview.heading("#0", text="")
        self.result_treeview.heading("#1", text="Valores")
        self.result_treeview.heading("#2", text="n°")
        self.result_treeview.heading("#3", text="Recebido")
        self.result_treeview.heading("#4", text="A Pagar")

        self.result_treeview.column("#0", width=13, stretch = "no", anchor='center')
        self.result_treeview.column("#1", width=80, anchor='center')
        self.result_treeview.column("#2", width=40, anchor='center')
        self.result_treeview.column("#3", width=50, anchor='center')
        self.result_treeview.column("#4", width=93, anchor='center')


    def menu_view(self):
        """Menu with integrations functions"""

        """Left Frame"""
        self.left_frame = Frame(
            self.window, 
            bd=4, bg='#dfe3ee',
            highlightbackground='#759fe6', 
            highlightthickness=3
            )

        self.left_frame.place(
            relx=0.02, 
            rely=0.03, 
            relwidth=0.47, 
            relheight=0.95
            )

        self.menu_frame = Frame(
            self.left_frame, 
            bd=1, bg='#dfe3ee',
            )

        self.menu_frame.place(
            relx=0.02, 
            rely=0.55, 
            relwidth=0.96, 
            relheight=0.40
            )

        """Left Calendar"""
        self.left_calendar = DateEntry(
            self.menu_frame, 
            width=12, 
            background='#3D51C3', 
            foreground='white', 
            borderwidth=2, 
            font="Arial 12", 
            selectmode='day', 
            cursor="hand1", 
            year=self.date_two.year, 
            month=self.date_two.month, 
            day=self.date_two.day, 
            date_pattern='dd/mm/Y'
            )

        self.left_calendar.place(
            relx=0.02, 
            rely=0.02, 
            relwidth=0.47, 
            relheight=0.20
            )

        """Right Calendar"""
        self.right_calendar = DateEntry(
            self.menu_frame, 
            width=12, 
            background='#3D51C3',
            foreground='white', 
            borderwidth=2, 
            font="Arial 12", 
            selectmode='day', 
            cursor="hand1", 
            year=self.date_one.year, 
            month=self.date_one.month, 
            day=self.date_one.day,
            date_pattern='dd/mm/Y'
            )

        self.right_calendar.place(
            relx=0.52,
            rely=0.02,
            relwidth=0.46,
            relheight=0.20
            )

        """Drop Menu"""
        self.str_var = StringVar()
        self.str_var.set("MOTORISTAS")

        self.drop_menu = OptionMenu(
            self.menu_frame, 
            self.str_var, 
            *self.list_moto()
            )

        self.drop_menu.place(
            relx = 0.02, 
            rely = 0.27, 
            relwidth = 0.96, 
            relheight = 0.18
            )

        """Button Search"""
        bt_search = Button(
            self.menu_frame, 
            text="Pesquisar", 
            bd=2, 
            bg='#364094', 
            fg='white', 
            font=('verdana', 10, 'bold'), 
            command=self.search_
            )

        bt_search.place(
            relx=0.02,
            rely=0.50,
            relwidth=0.47,
            relheight=0.23
            )

        """Button Export"""
        self.bt_export = Button(
            self.menu_frame, 
            text="Exportar", 
            bd=2, 
            bg='#364094', 
            fg='white', 
            font=('verdana', 10, 'bold'), 
            command=self.export_pdf
            )

        self.bt_export.place(
            relx=0.51,
            rely=0.50,
            relwidth=0.47,
            relheight=0.23
            )

        """Button All"""
        self.bt_export_all = Button(
            self.menu_frame, 
            text="Exportar Todos", 
            bd=2, 
            bg='#D92A2A', 
            fg='white', 
            font=('verdana', 10, 'bold'), 
            command=self.export_all
            )

        self.bt_export_all.place(
            relx=0.02,
            rely=0.75,
            relwidth=0.96,
            relheight=0.23
            )


    def list_box(self):
        """List box for Motorist Groups"""
        self.list_box_frame = Frame(
            self.left_frame, 
            bd=1, bg='#dfe3ee',
            )

        self.list_box_frame.place(
            relx=0.02, 
            rely=0.02, 
            relwidth=0.96, 
            relheight=0.49
            )

        """Fist ListBox"""
        self.fist_list_box = Listbox(self.list_box_frame)
        self.fist_list_box.place(
            relx=0.02,
            rely=0.02,
            relwidth=0.43,
            relheight=0.96
            )
        
        self.scroll = Scrollbar(
            self.fist_list_box, 
            orient='vertical',
            command=self.fist_list_box.yview
            )

        self.scroll.place(
            relx=0.9, 
            rely=0.016, 
            relwidth=0.07, 
            relheight=0.97
            )

        """Second ListBox"""
        self.second_list_box = Listbox(self.list_box_frame)

        self.second_list_box.place(
            relx=0.54,
            rely=0.02,
            relwidth=0.43,
            relheight=0.96
            )

        self.scroll = Scrollbar(
            self.second_list_box, 
            orient='vertical',
            command=self.second_list_box.yview
            )

        self.scroll.place(
            relx=0.9, 
            rely=0.016, 
            relwidth=0.07, 
            relheight=0.97
            )

        """Button Move Right"""
        self.bt_move_right = Button(
            self.list_box_frame, 
            text=">", 
            bd=2, 
            bg='#364094', 
            fg='white', 
            font=('verdana', 10, 'bold'), 
            command=self.move_right
            )

        self.bt_move_right.place(
            relx=0.47, 
            rely=0.35, 
            relwidth=0.055, 
            relheight=0.05
            )

        """Button Move Left"""
        self.bt_move_left = Button(
            self.list_box_frame, 
            text="<", 
            bd=2, 
            bg='#364094', 
            fg='white', 
            font=('verdana', 10, 'bold'), 
            command=self.move_left
            )
        
        self.bt_move_left.place(
            relx=0.47, 
            rely=0.5, 
            relwidth=0.055, 
            relheight=0.05
            )

        """Button Porcents"""
        self.bt_porcent = Button(
            self.list_box_frame, 
            text="%", 
            bd=2, 
            bg='#364094', 
            fg='white', 
            font=('verdana', 10, 'bold'), 
            command=self.window_porcent
            )
        
        self.bt_porcent.place(
            relx=0.47, 
            rely=0.7, 
            relwidth=0.055, 
            relheight=0.05
            )

    def window_porcent(self):
        """ toplevel window """
        window_porcent = Toplevel(self.window)
        window_porcent.geometry('400x250')

        """Button Confirm Porcents"""
        bt_confirm = Button(
            window_porcent, 
            text="Confirmar", 
            bd=2, 
            bg='#364094', 
            fg='white', 
            font=('verdana', 10, 'bold'), 
            command=self.set_porcents
            )

        bt_confirm.place(
            relx=0.38,
            rely=0.82,
            relheight=0.12,
            relwidth=0.2
            )

        frame_porcent = Frame(
            window_porcent, 
            bd=4, 
            bg='#dfe3ee',
            highlightbackground='#759fe6', 
            highlightthickness=3
            )
        
        frame_porcent.place(
            relx=0.02,
            rely=0.02,
            relheight=0.76,
            relwidth=0.46
            )
        
        lb_title = Label(
            frame_porcent, 
            text = "Definir Porcentagens", 
            bg = '#dfe3ee'
            )

        lb_title.place(
            relx=0.2,
            rely=0.02,
            )

        lb_valor = Label(
            frame_porcent,
            text='Valor',
            bg = '#dfe3ee'
            )

        lb_valor.place(
            relx=0.02,
            rely=0.2
            )

        lb_porcent = Label(
            frame_porcent,
            text='Porcent',
            bg = '#dfe3ee'
            )

        lb_porcent.place(
            relx=0.35,
            rely=0.2
            )

        lb_porcent_desc = Label(
            frame_porcent,
            text='P. desc.',
            bg = '#dfe3ee'
            )

        lb_porcent_desc.place(
            relx=0.70,
            rely=0.2
            )

        lb_porcent_one = Label(
            frame_porcent, 
            text = "R$12", 
            bg = '#dfe3ee'
            )

        lb_porcent_one.place(
            relx=0.02,
            rely=0.4
            )

        lb_porcent_two = Label(
            frame_porcent, 
            text = "R$13", 
            bg = '#dfe3ee'
            )

        lb_porcent_two.place(
            relx=0.02,
            rely=0.6
            )

        lb_porcent_tree = Label(
            frame_porcent, 
            text = "R$23", 
            bg = '#dfe3ee'
            )

        lb_porcent_tree.place(
            relx=0.02,
            rely=0.8
            )

        """Porcent Common Normal One"""
        self.var_porcent_one = StringVar(
            self.window, 
            self.porcents[0][0]
            )

        self.porcent_entry_one = Entry(
            frame_porcent, 
            textvariable=self.var_porcent_one
            )

        self.porcent_entry_one.place(
            relx=0.4, 
            rely=0.4, 
            relwidth=0.14, 
            relheight=0.12)


        """Porcent Common Normal Two"""
        self.var_porcent_two = StringVar(
            self.window, 
            self.porcents[0][1]
            )

        self.porcent_entry_two = Entry(
            frame_porcent,
            textvariable=self.var_porcent_two
            )

        self.porcent_entry_two.place(
            relx=0.4, 
            rely=0.6, 
            relwidth=0.14, 
            relheight=0.12
            )    


        """Porcent Common Normal Tree"""
        self.var_porcent_tree = StringVar(
            self.window, 
            self.porcents[0][2]
            )    

        self.porcent_entry_tree = Entry(
            frame_porcent,
            textvariable=self.var_porcent_tree
            )

        self.porcent_entry_tree.place(
            relx=0.4, 
            rely=0.8, 
            relwidth=0.14, 
            relheight=0.12)


        """Porcent Common Desc One"""
        self.var_porcent_desc_one = StringVar(
            self.window, 
            self.porcents[1][0]
            )

        self.porcent_entry_one_desc = Entry(
            frame_porcent,
            textvariable=self.var_porcent_desc_one
            )

        self.porcent_entry_one_desc.place(
            relx=0.7,
            rely=0.4,
            relwidth=0.14, 
            relheight=0.12)

        """Porcent Common Desc Two"""
        self.var_porcent_desc_two = StringVar(
            self.window,
            self.porcents[1][1]
            )

        self.porcent_entry_two_desc = Entry(
            frame_porcent,
            textvariable=self.var_porcent_desc_two
            )

        self.porcent_entry_two_desc.place(
            relx=0.7, 
            rely=0.6, 
            relwidth=0.14, 
            relheight=0.12
            )        

        """Porcent Common Desc Tree"""
        self.var_porcent_desc_tree = StringVar(
            self.window,
            self.porcents[1][2]
            )

        self.porcent_entry_tree_desc = Entry(
            frame_porcent,
            textvariable=self.var_porcent_desc_tree
            )

        self.porcent_entry_tree_desc.place(
            relx=0.7, 
            rely=0.8, 
            relwidth=0.14, 
            relheight=0.12)

        """Frames for Special Porcents"""
        frame_porcentTwo = Frame(
            window_porcent, 
            bd=4, 
            bg='#dfe3ee',
            highlightbackground='#759fe6', 
            highlightthickness=3)
        
        frame_porcentTwo.place(
            relx=0.50,
            rely=0.02,
            relheight=0.76,
            relwidth=0.48)

        
        # --------- Labels ----------- #

        lb_title_special = Label(
            frame_porcentTwo, 
            text = "Definir Porcentagens", 
            bg = '#dfe3ee'
            )

        lb_title_special.place(
            relx=0.2,
            rely=0.02,
            )

        lb_valor_special = Label(
            frame_porcentTwo,
            text='Valor',
            bg = '#dfe3ee'
            )

        lb_valor_special.place(
            relx=0.02,
            rely=0.2
            )

        lb_porcent_special = Label(
            frame_porcentTwo,
            text='Porcent',
            bg = '#dfe3ee'
            )

        lb_porcent_special.place(
            relx=0.35,
            rely=0.2)

        lb_porcent_desc_special = Label(
            frame_porcentTwo,
            text='P. desc.',
            bg = '#dfe3ee'
            )

        lb_porcent_desc_special.place(
            relx=0.70,
            rely=0.2)

        lb_porcent_one_special = Label(
            frame_porcentTwo, 
            text = "R$12", 
            bg = '#dfe3ee'
            )

        lb_porcent_one_special.place(
            relx=0.02,
            rely=0.4
            )

        lb_porcent_two_special = Label(
            frame_porcentTwo, 
            text = "R$13", 
            bg = '#dfe3ee'
            )

        lb_porcent_two_special.place(
            relx=0.02,
            rely=0.6
            )

        lb_porcent_tree_special = Label(
            frame_porcentTwo, 
            text = "R$23", 
            bg = '#dfe3ee'
            )

        lb_porcent_tree_special.place(
            relx=0.02,
            rely=0.8
            )

        

        """Porcent Special Normal One"""
        self.var_porcent_special_one = StringVar(
            self.window,
            self.porcents[2][0]
            )

        self.porcent_entry_one_special = Entry(
            frame_porcentTwo,
            textvariable=self.var_porcent_special_one
            )

        self.porcent_entry_one_special.place(
            relx=0.4, 
            rely=0.4, 
            relwidth=0.14, 
            relheight=0.12
            )

        """Porcent Special Normal Two"""
        self.var_porcent_special_two = StringVar(
            self.window,
            self.porcents[2][1]
            )

        self.porcent_entry_two_special = Entry(
            frame_porcentTwo,
            textvariable=self.var_porcent_special_two
            )

        self.porcent_entry_two_special.place(
            relx=0.4, 
            rely=0.6, 
            relwidth=0.14, 
            relheight=0.12
            )        
            
        """Porcent Special Normal Tree"""
        self.var_porcent_special_tree = StringVar(
            self.window,
            self.porcents[2][2]
            )

        self.porcent_entry_tree_special = Entry(
            frame_porcentTwo,
            textvariable=self.var_porcent_special_tree
            )

        self.porcent_entry_tree_special.place(
            relx=0.4, 
            rely=0.8, 
            relwidth=0.14, 
            relheight=0.12)


        """Porcent Special Desc One"""
        self.var_porcent_special_desc_one = StringVar(
            self.window,
            self.porcents[3][0]
            )

        self.porcent_entry_one_desc_special = Entry(
            frame_porcentTwo,
            textvariable=self.var_porcent_special_desc_one
            )

        self.porcent_entry_one_desc_special.place(
            relx=0.7, 
            rely=0.4, 
            relwidth=0.14, 
            relheight=0.12)

        """Porcent Special Desc Two"""
        self.var_porcent_special_desc_two = StringVar(
            self.window,
            self.porcents[3][1]
            )

        self.porcent_entry_two_desc_special = Entry(
            frame_porcentTwo,
            textvariable=self.var_porcent_special_desc_two
            )

        self.porcent_entry_two_desc_special.place(
            relx=0.7, 
            rely=0.6, 
            relwidth=0.14, 
            relheight=0.12)        
            
        """Porcent Special Desc Tree"""
        self.var_porcent_special_desc_tree = StringVar(
            self.window,
            self.porcents[3][2]
            )

        self.porcent_entry_tree_desc_special = Entry(
            frame_porcentTwo,
            textvariable=self.var_porcent_special_desc_tree
            )

        self.porcent_entry_tree_desc_special.place(
            relx=0.7, 
            rely=0.8, 
            relwidth=0.14, 
            relheight=0.12
            )