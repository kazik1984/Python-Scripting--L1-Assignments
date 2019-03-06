import sys

def isWhiteLine(line):
    try:
        if len(line.split()) == 0:
            return True
        else:
            return False
    except AttributeError as e:
        print(e)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("One argument is required. Put  name of text file.")
        exit()
    else:
        try:
            text = open(sys.argv[1],"r")
            lines_of_text = text.readlines()
            text.close()
            for i in lines_of_text:
                if isWhiteLine(i) == False:
                    print(i,end = "")
        except FileNotFoundError as e:
            print(e)



