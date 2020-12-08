# Defining Function
import math


def f(x):
    return x ** 4 + x ** 3 - 3 * x ** 2


# A derivative definition of f
def f_derivative(x):
    return 4 * x ** 3 + 3 * x ** 2 - 6 * x


# Implementing Bisection Method for a short range of values
def Bisection_Method(a, b, type_of_f):
    # Implementing Bisection Method on f
    if type_of_f == "f":
        # Checking Correctness of initial guess values and bisecting
        if f(a) * f(b) > 0.0:
            print('Given guess values do not bracket the root.')

        else:
            step = 1
            condition = True
            error = - math.log(exp/(b-a)) / math.log(2)

            while condition:

                if step > error:
                    print("The roots cannot be found using the bisection method")
                    exit(0)

                c = (a + b) / 2

                if f(a) * f(c) < 0:
                    b = c
                else:
                    a = c

                step = step + 1
                condition = abs(f(c)) > e

            result.append(c)

    # Implementing Bisection Method on f' (f_derivative)
    elif type_of_f == "f_derivative":
        # Checking Correctness of initial guess values and bisecting
        if f_derivative(a) * f_derivative(b) > 0.0:
            print('Given guess values do not bracket the root.')

        else:
            step = 1
            condition = True
            error = - math.log(exp / (b - a)) / math.log(2)

            while condition:

                if step > error:
                    print("The roots cannot be found using the bisection method")
                    exit(0)

                c = (a + b) / 2

                if f_derivative(a) * f_derivative(c) < 0:
                    b = c
                else:
                    a = c

                step = step + 1
                condition = abs(f_derivative(c)) > e

            # Check whether placing the value c in the function f will give us 0 (intersection point)
            if f(round(c, 1)) == 0.0:
                result.append(c)


# Implementing Bisection Method for a long range of values
def Bisection_Method_Max_Range(min_range, max_range, section):
    section_list = []  # List for all entries after distribution into sections
    counter = min_range

    while counter <= max_range:
        section_list.append(round(counter, 1))
        counter += section
    section_list.append(max_range)

    # Finding the root in the desired range
    for idx, j in enumerate(section_list):
        if idx < len(section_list) - 1:

            # Check whether the value 0 is included in the given range, if so, we will treat it individually
            if section_list[idx+1] == 0:
                if idx < len(section_list) - 2:

                    if f(j) * f(section_list[idx + 2]) < 0.0:
                        Bisection_Method(j, section_list[idx + 2], "f")

                    if f_derivative(j) * f_derivative(section_list[idx + 2]) < 0.0:
                        Bisection_Method(j, section_list[idx + 2], "f_derivative")

            # Check if f(x1)*f(x2) < 0 for f function
            if f(j) * f(section_list[idx + 1]) < 0.0:
                Bisection_Method(j, section_list[idx + 1], "f")

            # Check if f(x1)*f(x2) < 0 for f' function
            if f_derivative(j) * f_derivative(section_list[idx + 1]) < 0.0:
                Bisection_Method(j, section_list[idx + 1], "f_derivative")


if __name__ == "__main__":
    result = []
    e = 0.0001  # epsilon
    exp = 10 ** -10

    a = float(input("Please enter a range for 'a': "))
    b = float(input("Please enter a range for 'b': "))
    section = float(input("Please select the difference between each section: "))   # The difference between a
    # section and a section within the range of values

    Bisection_Method_Max_Range(a, b, section)
    print(f"{len(result)} roots were found for the function")

    for i, j in enumerate(result):
        print(f"{i + 1}. {j}")

