import datetime

def convert_file():
    file = open("data_file/CNAB.txt", "r")
    file_read = file.readlines()
    new_file = []
    for information in file_read:
        new_information = {}
        new_information["type"] = information[0]
        new_information["date"] = f"{information[1:5]}-{information[5:7]}-{information[7:9]}"
        new_information["value"] = int(information[9:19])/100.00
        new_information["CPF"] = information[19:30]
        new_information["card"] = information[30:42]
        new_information["hour"] = f"{information[1:5]}-{information[5:7]}-{information[7:9]} {information[43:44]}:{information[44:46]}:{information[46:48]}"
        new_information["store_owner"] = information[48:62].strip()
        new_information["store_name"] = information[62:81].strip()
        new_file.append(new_information)

    file.close()
    return new_file