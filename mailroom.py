import sys
from statistics import mean


def sort_key(donor):
    return donor[1]

donor = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ("John Cena", [1457.23, 42069.69])
            ]

for i in range(len(donor)):
    donor[i][1].sort(reverse=True)
donor = sorted(donor, key=sort_key, reverse=True)


def pr_list():
    print("{:20} | {:10} | {:8} | {:12}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    for i in range(len(donor)):
        print("{:20} $ {:12.2f}   {:8} $ {:12.2f}".format(donor[i][0], sum(donor[i][1]), len(donor[i][1]), mean(donor[i][1])))


def thanks():
    name = input(("Please provide a full name('list' for list of donors) >> "))
    if name == "list":
        pr_list()
        print("")
        thanks()
    elif name == "quit":
        main()
    else: 
        for i in range(len(donor)):
            if name == donor[i][0]:
                amount = input("Please provide the donation amount >> ")
                try:
                    amount = int(amount)
                except ValueError:
                    print("You need to provide a number!")
                    thanks()
                donor[i][1].append(amount)
                email(amount, name)
        amount = input("Please provide the donation amount >> ")
        try:
            amount = int(amount)
        except ValueError:
            print("You need to provide a number!")
            thanks()
        donor.append((name, [amount]))
    print(f"Thank you for sending us the generous amount of {amount}, Mr./Mrs. {name}")
    main()

def email(amount, name):
    print(f"Thank you for sending us the generous amount of {amount}, Mr./Mrs. {name}")
    main()


def report():
    pr_list()
    main()

def quit():
    exit()

def main():
    choice = input("""Choose an option
        1 --> Send a Thank You
        2 --> Create a Report
        3 --> Quit Program
        >>> """)
    if choice == '1':
        thanks()
    elif choice == '2':
        report()
    elif choice == '3':
        quit()
    else:
        main()


if __name__ == "__main__":
    main()
