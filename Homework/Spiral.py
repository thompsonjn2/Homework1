def main():
    count = 0
    gap = 1
    four_count = 4
    total = 0
    for n in range(0,501**2):
        if count == 0:
            total += n
            count = gap
            four_count -= 1
        elif count != 0: 
            count -=1
        if four_count == 0:
            gap +=2
            four_count = 4
    if __name__ == "__main__":
        print(total)

