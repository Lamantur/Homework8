import re
import csv
data_info = ['info_1.txt', 'info_2.txt', 'info_3.txt']
main_data = [['Изготовитель системы',
              'Название ОС', 'Код продукта', 'Тип системы']]


def get_data(main_data):

    j = 0
    while j < 4:
        column = []
        k = 0
        while k < 3:
            file = open(data_info[k], "r")
            string_from_file = file.readlines()

            for i in range(len(string_from_file)):
                if re.findall(main_data[0][j], string_from_file[i]) == [main_data[0][j]]:
                    string_from_file[i] = [
                        x.rstrip(main_data[0][j]) for x in string_from_file[i]]
                    string_from_file[i] = [
                        x.rstrip('\n') for x in string_from_file[i]]

                    string_from_file[i] = [
                        x.rstrip(':') for x in string_from_file[i]]
                    string_from_file[i] = "".join(string_from_file[i])
                    column.append(string_from_file[i])

            k = k + 1
            file.close()

        # main_data.append(main_data[j])
        j = j+1
        main_data.append(column)
        print(f"Добавлены данные: {column}")
    return main_data


def write_to_csv(main_data):
    main_data = get_data(main_data)
    with open('data_report2.csv', 'w') as f_n:
        f_n_writer = csv.writer(f_n)
        for row in main_data:
            f_n_writer.writerow(row)


write_to_csv(main_data)
