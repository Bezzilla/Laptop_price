"""This module is to create main UI for the program"""
import customtkinter as ctk
from CTkListbox import *
from laptop_csv_reader import DATA_INDEX

COMPARE_DATA = []


class Menu(ctk.CTkTabview):
    """Create menu"""
    def __init__(self, parent, data):
        """initiated component"""
        super().__init__(master=parent)
        self.grid(row=0, column=0, sticky='nsew')
        self.data = data

        # taps
        self.add('Data comparison')
        self.add('Story telling')

        Data_Comparison(self.tab('Data comparison'), data=self.data)
        Story_Telling(self.tab('Story telling'), data=self.data)


class Data_Comparison(ctk.CTkFrame):
    """Data comparison tap"""

    def __init__(self, parent, data):
        """initiated component"""
        super().__init__(master=parent, fg_color='transparent')
        self.pack(expand=True, fill='both')
        self.data = data
        Search_Panel(self, data=self.data)


class Story_Telling(ctk.CTkFrame):
    """Story telling tap"""
    def __init__(self, parent, data):
        """initiated component"""
        super().__init__(master=parent, fg_color='transparent')
        self.pack(expand=True, fill='both')
        Story_Panel(self, data=data)


class Panel(ctk.CTkFrame):
    """Panel to be used in tap"""
    def __init__(self, parent):
        """initiated component"""
        super().__init__(master=parent, fg_color='#4a4a4a')
        self.pack(fill='x', pady=4, padx=4)


class Search_Panel(Panel):
    """Data comparison tap UI"""

    def __init__(self, parent, data):
        """initiated component"""
        super().__init__(parent=parent)
        self.data = data
        self.compare_index = []

        self.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.columnconfigure((0, 1, 2), weight=1)

        self.search_label = ctk.CTkLabel(self, text="Search by")
        self.search_label.grid(row=0, column=0, sticky='W', padx=5, pady=5)

        self.filter_search = ctk.CTkComboBox(self, values=data[0])
        self.filter_search.grid(row=0, column=1, sticky='E', padx=5, pady=5,
                                columnspan=2)

        self.search_panel = ctk.CTkEntry(self)
        self.search_panel.grid(row=1, column=0, sticky='EW', padx=5, pady=5,
                               columnspan=3)
        self.search_panel.bind("<KeyRelease>", self.Search_list_box)

        self.search_list_box = CTkListbox(self, width=250)
        self.search_list_box.grid(row=2, column=0, sticky='EW', padx=5,
                                  pady=5, columnspan=3)

        self.add_button = ctk.CTkButton(self, text="Add to Compare List",
                                        command=self.add_to_compare_list)
        self.add_button.grid(row=3, column=0, sticky='EW', padx=5, pady=5,
                             columnspan=3)

        self.selected_label = ctk.CTkLabel(self, text="Selected List")
        self.selected_label.grid(row=4, column=0, sticky='N', padx=5, pady=5,
                                 columnspan=3)

        self.compare_list_box = CTkListbox(self, width=250)
        self.compare_list_box.grid(row=5, column=0, sticky='EW', padx=5,
                                   pady=5, columnspan=3)

        self.del_button = ctk.CTkButton(self, text="Delete",
                                        command=self.del_button)
        self.del_button.grid(row=6, column=0, sticky='N', padx=5,
                             pady=5)

        self.compare_button = ctk.CTkButton(self, text="Compare"
                                            , command=self.compare_button)
        self.compare_button.grid(row=6, column=1, padx=5,
                                 pady=5)

        self.clear_button = ctk.CTkButton(self, text="Clear",
                                          command=self.clear_button)
        self.clear_button.grid(row=6, column=2, padx=5,
                               pady=5)

    def Search_list_box(self, event):
        """search box """
        index = int(DATA_INDEX[self.filter_search.get()])
        count = 0
        try:
            self.search_list_box.delete(0, 'end')
            search_text = self.search_panel.get().lower()
            if search_text != "":
                for row in self.data:
                    if search_text.lower() in row[index].lower():
                        self.search_list_box.insert('end',
                                                    f"{row[-1]}:{row[index]}")
                        count += 1
        except Exception as e:
            pass

    def add_to_compare_list(self):
        """add to compare list"""
        index = self.search_list_box.curselection()
        selected_value = self.search_list_box.get(index).split(':')
        index = selected_value[0]
        self.compare_index += [index]
        self.compare_list_box.insert('end', selected_value)

    def clear_button(self):
        """clear compare list"""
        self.compare_list_box.delete(0, 'end')

    def del_button(self):
        """delete item from compare list"""
        selected_index = self.compare_list_box.curselection()
        if selected_index:
            self.compare_list_box.delete(selected_index)

    def compare_button(self):
        """compare the value"""
        global COMPARE_DATA
        COMPARE_DATA = self.compare_index
        self.master.master.master.master.receive_compare_data(COMPARE_DATA)


class Story_Panel(Panel):
    """Story telling tap UI"""
    def __init__(self, parent, data):
        """initiated component"""
        super().__init__(parent=parent)
        self.data = data

        self.rowconfigure((0, 1, 2), weight=1)
        self.columnconfigure((0, 1), weight=1)

        self.blox_plot_price_manufactory = (
            ctk.CTkButton(self, text="Box Plot"))
        self.blox_plot_price_manufactory.grid(row=0, column=0,
                                              padx=5, pady=5, sticky="w")
        self.blox_plot_price_manufactory.configure(command=self.plot_box)

        self.hist = ctk.CTkButton(self, text="Histogram")
        self.hist.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.hist.configure(command=self.histogram)

        self.scatter_plot = ctk.CTkButton(self, text="Scatter Plot")
        self.scatter_plot.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.scatter_plot.configure(command=self.scatter)

        self.heatmap_plot = ctk.CTkButton(self, text="Descriptive")
        self.heatmap_plot.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.heatmap_plot.configure(command=self.descriptive)

    def plot_box(self):
        """plot box plot"""
        self.master.master.master.master.plot_box_price()

    def histogram(self):
        """plot histogram"""
        self.master.master.master.master.plot_histogram()

    def scatter(self):
        """plot scatter plot"""
        self.master.master.master.master.plot_scatter()

    def descriptive(self):
        """descriptive statistic"""
        self.master.master.master.master.show_descriptive_statistics()
