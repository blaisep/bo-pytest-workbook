# sums.py
# add the numbers in `data.txt`
import sys

def main():
    sum = 0.0

    try:
        sys.argv[1]
    except IndexError:
        raise Exception(f'Usage: {sys.argv[0]} <datafile>')

    datafile = sys.argv[1]
    with open(datafile, "r") as file:
        for line in file:
            number = float(line)
            sum += number

    print(f"{sum:.2f}")


if __name__ == "__main__":
    main()
