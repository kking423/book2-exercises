import pdb


def add_one(num):
    result = num + 1
    print(result)
    return result


def main():
    pdb.set_trace()
    for num in range(10):
        add_one(num)


if __name__ == "__main__":
    main()
