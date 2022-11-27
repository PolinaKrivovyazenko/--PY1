import json


INPUT_FILE = "input.csv"


#TODO реализовать конвертер из csv в json


def csv_to_list_dict(input_file) -> list[dict]:
    row_list = []
    values = []
    row_list_values = []
    new_row = '\n'
    delimiter = ','
    row_ = []
    dict_ = {}
    with open(input_file) as file:
        for row in file:
            row_list.append(row.rsplit())
    for item in row_list:
        if item == row_list[0]:
            row_list_keys = item
            keys_list = item[0].split(delimiter)
        else:
            values.append(item)
    for item in values:
        row_list_value = item
        row_list_values.append(item[0].split(delimiter))
    for item in range(len(row_list)-1):
        line_list_item = row_list_values[item]
        for k in range(len(keys_list)):
            dict_[keys_list[k]] = line_list_item[k]
        row_.append(dict_.copy())
    return row_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

