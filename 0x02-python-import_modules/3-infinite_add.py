#!/usr/bin/python3

if __name__ == "__main__":

    import sys

if len(sys.argv) <= 1:
    sys.exit(1)

total = 0

for arg in sys.argv[1:]:
    try:
        num = int(arg)
    except valueError:
        sys.exit(1)

    total += num

    print(total)
