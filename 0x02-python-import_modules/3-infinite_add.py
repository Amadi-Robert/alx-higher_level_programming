#!/usr/bin/python3

if __name__ == "__main__":

    import sys

if len(sys.argv) <= 1:
    sys.exit(1)

total = 0

for arg in sys.argv[1:]:
    num = int(arg)

    total += num

    print(total)


