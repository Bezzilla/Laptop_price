"""This module is to read csv file"""
import csv

DATA_INDEX = {
    'company': '0',
    'product': '1',
    'typeName': '2',
    'inches': '3',
    'screenresolution': '4',
    'cpu': '5',
    'ram': '6',
    'memory': '7',
    'gpu': '8',
    'opsys': '9',
    'weight': '10',
    'price': '11'
}


class CSVdata:
    """to read csv file"""
    def __init__(self, file_path):
        """initiated component"""
        self.data = []
        self.file_path = file_path

    def read_csv(self):
        """read the csv file"""
        with open(self.file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            self.data = list(reader)
            for i in range(len(self.data)):
                if str(i) == "0":
                    self.data[i] += ["index"]
                else:
                    self.data[i] += [str(i)]

    def get_data(self):
        """return data"""
        return self.data
