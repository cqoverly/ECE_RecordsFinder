

'''
        This script is used to take a list of student numbers in a text file separate by newline and return any matching records from any csv output of a report that has student numbers in the first index of the record. A csv file is generated with the matching records from the report.
        
        The numbers file needs to be named 'numbers.txt' and the report file must be named 'report.csv'. Both need to be added to same folder as this script.
'''


import csv
import os


# Load CSV Data
def load_data(csv_data):
    loaded_records = []
    loaded_fields = []
    with open(csv_data, 'r') as f:
        data = csv.reader(f)
        all_rows = [r for r in data]
        loaded_fields = all_rows[0]
        loaded_records = all_rows[1:]
    print(f'Fields Loaded: {len(loaded_fields)}')
    print(f'Records Loaded: {len(loaded_records)}')
    return (loaded_fields, loaded_records)


def make_number_list(text_file):
    with open(text_file, 'r') as f:
        number_list = [n.strip() for n in f.readlines()]
        return number_list


def get_records(numbers, records): 
    # match the numbers to numbers in the records and return matched records.
    matched_records = []
    for rec in records:
        if rec[0] in numbers:
            matched_records.append(rec)
    print(f'Records to find: {len(numbers)}')
    print(f'Records found: {len(matched_records)}')
    return matched_records


def generate_records_csv(fields, records):
    save_name = 'untitled'
    save_name += '.csv'
    with open(save_name, 'w') as f:
        records.insert(0, fields) # add column names
        writer = csv.writer(f)
        writer.writerows(records)
    os.system("open -a 'Microsoft Excel.app' {}".format(save_name))
    

def finder_main(student_numbers, report_path):
    # print('\n\n============= CHOOSE NUMBERS .TXT FILE =================\n')
    # numbers_file = file_chooser.choose_file()
    # while not numbers_file:
    #     pass
    # print('n\n\============= CHOOSE REPORT .CSV FILE =================\n')
    # student_numbers = make_number_list(numbers_file)
    # report_file = file_chooser.choose_file()

    main_fields, main_records = load_data(report_path)
    print(len(main_fields), len(main_records))
    retrieved_records = get_records(student_numbers, main_records)
    generate_records_csv(main_fields, retrieved_records)
    return len(retrieved_records)

if __name__ == '__main__':

    finder_main()


    # print('\n\n============= CHOOSE NUMBERS .TXT FILE =================\n')
    # numbers_file = file_chooser.choose_file()
    # while not numbers_file:
    #     pass
    # print('n\n\============= CHOOSE REPORT .CSV FILE =================\n')
    # student_numbers = make_number_list('numbers.txt')
    # report_file = file_chooser.choose_file()
    # main_fields, main_records = load_data('report.csv')
    # print(len(main_fields), len(main_records))
    # retrieved_records = get_records(student_numbers, main_records)
    # generate_records_csv(main_fields, retrieved_records)