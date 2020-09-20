import sys

def get_filename():
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
        return filename
    else:
        print("You should run this program by calling 333 python parser.py filename")
        return ""

def read_from_file_to_list(filename):
    output =[]
    with open(filename, "r") as file_to_read :
        for line in file_to_read.readlines():
            row  = line.replace("\n", "").split(" ")
            output.append(row)

    return output


def main(): 
    filename = get_filename()

    if len(filename) == 0:
        return

    print(f"File to parse: {filename}")
    data_list = read_from_file_to_list(filename)
    print(data_list)

if __name__ == "__main__":
    main()