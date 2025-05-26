def check_case(Letter):
    if Letter.isupper():
        return "The letter is uppercase"
    elif Letter.islower():
        return "The letter is lowercase"
    else:
        return "Neither uppercase or lowercase"
 


def main():
    Letter = str(input("Enter a single letter: "))
    if len(Letter) != 1:
        print("Enter exactly one letter")
    result = check_case(Letter)
    print(f"The letter {Letter} is:{result} ")

main()

    





