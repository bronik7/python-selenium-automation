def challenge_035():
    count = 1
    while count <= 3:
        name = str(input("Enter your name: ")).strip()
        print("Your name : " + name)
        count += 1


challenge_035()


def challenge_036():
    try:
        result = str(
            input("Enter your name and number of times you want your name to be displayed: (exp: Alex 4): ")).strip()
        name_number = result.split(" ")

        if len(name_number) == 1 or len(name_number) > 2:
            raise ValueError("Invalid input")

        for count in range(int(name_number[1])):
            print(name_number[0])

    except ValueError as e:
        print(e)


challenge_036()


def challenge_037():
    result = input("Enter your name: ")
    for i in range(len(result)):
        print(result[i])


challenge_037()


def challenge_038():
    try:
        result = str(
            input("Enter your name and number of times you want your name to be displayed: (exp: Alex 4): ")).strip()
        name_number = result.split(" ")

        if len(name_number) == 1 or len(name_number) > 2:
            raise ValueError("Invalid input")

        for count in range(int(name_number[1])):
            print("\n")
            for n in range(len(name_number[0])):
                print(name_number[0][n])

    except ValueError as e:
        print(e)


challenge_038()


def challenge_040():
    try:
        result = int(input("Please enter number bellow 50: "))
        if result >= 50:
            raise ValueError("Number must be bellow 50")
        else:
            count = 50
            while count != result:
                count -= 1
                print(count)
    except ValueError as e:
        print(e)


challenge_040()


def challenge_041():
    result = str(input("Please enter your name and a number: ")).strip()
    try:
        name_number = result.split(" ")

        if len(name_number) == 1 or len(name_number) > 2:
            raise ValueError("Invalid input")
        else:
            number = int(name_number[1])
            if number < 10:
                print(f'{name_number[0]}\n' * number)
            else:
                print("Too high\n" * 3)

    except ValueError as e:
        print(e)


challenge_041()


def challenge_042():
    try:
        total = 0
        count = 1
        while count <= 5:
            number = int(input("Please enter a number: "))
            include_in_total = input("Do you want this number to be included in total (Yes = Y, No= N): ")
            if str(include_in_total).lower() != "y" and str(include_in_total).lower() != "n":
                raise ValueError("Invalid answer")
            else:
                if str(include_in_total).lower() == "y":
                    total += number
            count += 1

        print(f"Total is: {total}")
    except ValueError as e:
        print(e)


challenge_042()


def challenge_043():
    try:
        number_to_count = 0
        count = 0
        up_down = str(input("Do you want to count up or down? exp('UP','DOWN')")).strip()
        if up_down.lower() != "up" and up_down.lower() != "down":
            raise ValueError("I don't understand")
        if up_down.lower() == "up":
            number_to_count = int(input("Please enter number:"))
            count = 0
            while count < number_to_count:
                count += 1
                print(str(count))
        else:
            number_to_count = int(input("Please enter number bellow 20: "))
            if number_to_count >= 20:
                raise ValueError("Number must be bellow 20")
            count = 20
            while count >= number_to_count:
                print(str(count))
                count -= 1

    except ValueError as e:
        print(e)


challenge_043()


def challenge_044():
    try:
        number_of_invitations = int(input("How many people you want to invite to your party? "))
        if number_of_invitations < 10:
            if number_of_invitations <= 0:
                raise ValueError("Invalid input")
            count = 1
            while count <= 10:
                name = str(input("Please enter name: ")).strip()
                print(f"{name} has been invited")
                count += 1
        else:
            print("Too many people")
    except ValueError as e:
        print(e)


challenge_044()


def challenge_045():
    try:
        total = 0
        while total <= 50:
            total += int(input("Please enter a number: "))

        print(f"Total is {total}")
    except ValueError as e:
        print(e)


challenge_045()


def challenge_046():
    try:
        number = 0
        while number <= 5:
            number = int(input("Please enter number"))

        print(f"The last number you entered was a {number}")
    except ValueError as e:
        print(e)


challenge_046()


def challenge_047():
    try:
        answer = "y"
        total = int(input("Please enter first number: "))
        total += int(input("Please enter second number: "))
        while answer.lower() == "y":
            answer = str(input("Do you want to add another number? ('Yes'=Y, No= 'N')")).strip()
            if answer.lower() != "y" and answer.lower() != "n":
                raise ValueError("Invalid input.")
            elif answer.lower() == "y":
                total += int(input("Please add another number:"))
            else:
                answer = "n"

        print(f"Total is: {total}")
    except ValueError as e:
        print(e)


challenge_047()


def challenge_048():
    try:

        invitation_text = "Please enter name of a person you want to invite: "
        answer = "y"
        name = str(input(invitation_text)).strip()
        total = 1

        print("{0} has been invited to the party".format(name))
        while answer.lower() == "y":
            answer = str(input("Do you want to invite another person? ('Yes'=Y, No= 'N')")).strip()
            if answer.lower() != "y" and answer.lower() != "n":
                raise ValueError("Invalid input.")
            elif answer.lower() == "y":
                name = str(input(invitation_text)).strip()
                print("{0} has been invited to the party".format(name))
                total += 1
            else:
                answer = "n"

        print(f"Total people coming: {total}")
    except ValueError as e:
        print(e)


challenge_048()


def challenge_049():
    try:
        campnum = 50
        number_of_tries = 1
        text = "Please enter number: "
        number = int(input(text))
        while number != campnum:
            if number > campnum:
                print("Number is too high")
            else:
                print("Number is too low")
            number_of_tries += 1
            number = int(input(text))

        print(f"Well done, you took {number_of_tries} attempts")
    except ValueError as e:
        print(e)


challenge_049()


def challenge_050():
    try:
        number = 1
        while number < 10 or number > 20:
            number = int(input("Please enter number between 10 and 20: "))
            if number < 10:
                print("Too low")
            elif number > 20:
                print("Too high")
            else:
                print("Thank you")
    except ValueError as e:
        print(e)


challenge_050()


def challenge_051():
    try:
        count = 10

        while count > 0:
            result = int(input(
                f"There are {count} green bottles hanging on the wall,\n{count} green bottles hanging on the wall,\nand if 1 green bottle should accidentally fall,\nhow many bottles will be hanging on the wall? "))
            count -= 1
            while result != count:
                result = int(input("No, try again. How many green bottles hanging ot the wall? "))
        print("There are no more green bottles hanging on the wall.")
    except ValueError as e:
        print(e)


challenge_051()
