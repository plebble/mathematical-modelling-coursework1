import json
import csv
import copy

with open("export_main.json","r") as file:
    input_data = json.load(file)

output_data = {}

for bump in input_data:
    bump_width = bump["bump_width"]
    bump_height = bump["bump_height"]

    try:
        output_data[bump_width]
    except:
        output_data[bump_width] = {}


    del bump["bump_width"]
    del bump["bump_height"]

    output_data[bump_width][bump_height] = bump.copy()

with open("export_processed.json","w") as file:
    json.dump(output_data,file,indent=4,sort_keys=True)

column_headers = list(output_data.keys())
row_headers = list(output_data[column_headers[0]].keys())

table_template = [[""] + column_headers]
for row_header in row_headers:
    table_template += [[row_header]+([""] * len(column_headers))]


col_lookup = {}
for col,value in enumerate(column_headers):
    col_lookup[value] = col + 1

row_lookup = {}
for row,value in enumerate(row_headers):
    row_lookup[value] = row + 1

csv_output = {"max_accel":copy.deepcopy(table_template),"min_accel":copy.deepcopy(table_template),"max_jerk":copy.deepcopy(table_template),"min_jerk":copy.deepcopy(table_template)}


with open("export_main.json","r") as file:
    input_data = json.load(file)

for bump in input_data:
    bump_width = bump["bump_width"]
    bump_height = bump["bump_height"]

    for i in ["max_accel","min_accel","max_jerk","min_jerk"]:
        csv_output[i][row_lookup[bump_height]][col_lookup[bump_width]] = bump[i]


for key in list(csv_output.keys()):
    print(key)

    with open("{}.csv".format(key),"w",newline="") as file:
        csv_writer = csv.writer(file,delimiter=",")
        csv_writer.writerows(csv_output[key])


print("done!")