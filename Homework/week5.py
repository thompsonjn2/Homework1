import sys
def add_them_all(filename):
    sum = 0
   
    with open ('a.txt', 'r') as filename:
        for line in filename:
           sum += int(line)
        return sum
if __name__ == "__main__":
    fname = sys.argv[1]
    print(f"Processing {fname}")
    print(add_them_all(fname))