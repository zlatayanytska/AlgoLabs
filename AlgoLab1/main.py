from insect import Insect
from counter import Counter
from datetime import datetime
from insertion_sort import insertion_sort
from quicksort import Quicksort
import csv


def read_data_from_file():
    insect_list = []
    try:
        with open('insect_data.csv') as csvin:
            reader = csv.reader(csvin)
            for row in reader:
                new_insect = Insect(row[0], int(row[1]), int(row[2]))
                insect_list.append(new_insect)
    except FileNotFoundError:
        print("File with data does not exist!")
    return insect_list



def work_time(start, finish) :
    return finish - start



def print_answer(algo_name, work_time, compare_num, exchange_num, sorted_list):
    print(str(algo_name)+"\nWORK TIME: "+str(work_time)+"\nCOMPARISON NUMBER: "+str(compare_num)+
          "\nEXCHANGE NUMBER: "+str(exchange_num)+"\nSORT RESULT: \n"+str(sorted_list))



if __name__ == "__main__":

    insect_list = read_data_from_file()
    start = datetime.now().microsecond
    select_sorted_list = insertion_sort(insect_list)
    finish = datetime.now().microsecond
    print_answer("INSERTION SORT", work_time(start, finish), Counter.compare_num,
                 Counter.exchange_num, select_sorted_list)
    print("\n\n-------------------------------------------------------------------------------------------\n\n")
    Counter.count_reset()
    quicksort = Quicksort(insect_list)
    start = datetime.now().microsecond
    quicksort.quick_sort(0, len(insect_list) - 1)
    finish = datetime.now().microsecond
    print_answer("QUICKSORT", work_time(start, finish), Counter.compare_num, Counter.exchange_num, quicksort.sort_list)
    print("\n\n-------------------------------------------------------------------------------------------\n\n")
