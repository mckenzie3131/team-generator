import csv
import time
from random import randint


class TeamGenerator:
    def read_input_file(self, filename=str):
        one_line = []
        with open(filename) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            for row in reader:
                one_line.append(row[0])
        return one_line

    def append_with_random_number(self, list_of_names):
        list_with_numbers = []
        for name in list_of_names:
            list_with_numbers.append(name + " " + str(randint(1, 2)))
        return list_with_numbers

    def process_data(self):
        filename = "input.csv"
        names_list = self.append_with_random_number(self.read_input_file(filename))
        print("drum rolllllll")
        for name in names_list:
            print(name)
            time.sleep(1)


if __name__ == "__main__":
    tg = TeamGenerator()
    tg.process_data()
