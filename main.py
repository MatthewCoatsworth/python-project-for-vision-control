class bird:
    # class attributes
    name = ""
    age = 0


if __name__ == '__main__':
    bird1 = bird()
    bird1.name = 'evil bird'
    bird1.age = 10

    bird2 = bird()
    bird2.name = 'kind bird'
    bird2.age = 100

    print(f"{bird1.name} is {bird1.age} minutes old.")