def main():
    counter = 0
    gap = 1
    four_counter = 4
    total = 0
    for n in range(0,501**2):
        if counter == 0:
            total += n
            counter = gap
            four_counter -= 1
        elif counter != 0: 
            counter -=1
        if four_counter == 0:
            gap +=2
            four_counter = 4
    if __name__ == "__main__":
        print(total)

