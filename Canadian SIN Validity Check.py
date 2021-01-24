def sin_validity(sin):
    total = 0
    for i in range(len(sin)):
        if i % 2 != 0:
            double = int(sin[i]) * 2
            if len(str(double)) == 2:
                total += int(str(double)[0]) + int(str(double)[1])
            else:
                total += double
        else:
            total += int(sin[i])
            
    if total % 10 == 0:
        print(f"SIN {sin} is valid!")
    else:
        print(f"SIN {sin} is NOT valid!")

sin = input("Enter SIN to check:\n")
sin_validity(sin)