def read_last_5_lines(filename):
    try:
        with open(filename,'r')as file:
            lines=file.readlines()
            last_lines=lines[-5:]
            print("last 5 lines of the file:")
            for line in last_lines:
                print(line.strip())
    except FileNotFoundError:
         print(f"file'{filename}'not found.")
    except Exception as e:
            print("an error occurred:",e)
read_last_5_lines('ckr.txt')