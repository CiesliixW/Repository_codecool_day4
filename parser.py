import sys

NAME_INDEX = 0

def get_filename():
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
        return filename
    else:
        print("You should run this program by calling python parser.py filename")
        return ""

def read_from_file_to_list(filename):
    output =[]
    with open(filename, "r") as file_to_read :
        for line in file_to_read.readlines():
            row  = line.replace("\n", "").split(" ")
            output.append(row)

    return output

def get_names(data_list):
    name = []

    for line in data_list:
        name.append(line[NAME_INDEX])
    
    return name

def save_report_to_file(report, filename):
    with open("output.txt", "w+") as file_to_read:
        for report_data in report:
            file_to_read.write(report_data)

def generate_report(data_list):
    output = []

    output.append(f"Ilosc danych {len(data_list)}")
    output.append(f"Imiona{get_names(data_list)}")

    return output

def main(): 
    filename = get_filename()

    if len(filename) == 0:
        return

    print(f"File to parse: {filename}")
    data_list = read_from_file_to_list(filename)
    print(data_list)
    report = generate_report(data_list)
    print(report)
    save_report_to_file(report, "output.txt")

if __name__ == "__main__":
    main()