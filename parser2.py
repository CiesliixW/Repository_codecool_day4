import sys


def get_filename():
    if len(sys.argv) >= 3:
        input1 = int(sys.argv[1])
        input2 = int(sys.argv[2])
        return input1 + input2
    else:
        print("You should run this program by calling python parser2.py input1 input2")
        return ""

def main(): 
    filename = get_filename()

    if filename == "":
        return

    print(f"File to parse: {filename}")

if __name__ == "__main__":
    main()