import csv
with open("aprts_data_raw.csv", "r", encoding='utf8',newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    my_file = open("aprt_total_area.txt", "w+")
    for line in reader:
        area = line[6].split(' ')
        result_area = 0
        for m in area:
            try:
                result_area = result_area + float(m)
            except:
                pass
        my_file.write(str(f'{result_area:.1f}') + '\n')