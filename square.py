def calculate_area(L):
    return L**2
def calculate_perimeter(L):
    return 4*L

def main():
    L = float(input("Enter the length of the square: "))
    area = calculate_area(L)
    perimeter = calculate_perimeter(L)
    print(f"The area of a square of side length {L} is {area} and the perimeter is {perimeter}")
  
main()