"""
    predictor.py

    Main program used to tell users if they are allowed to take the car outside or not.
    This prediction is based on the Pico & Placa restrictions previously implemented in
    the city of Quito.

    To run the program successfully the user must provide a valid license plate, a date (dd/mm/yyyy),
    and a time (HH:MM) with the correct format.
"""

import enum
import datetime


# maps the license plate last digits with the corresponding day of restriction
class DateDigits(enum.Enum):
    Mon = [1, 2]
    Tue = [3, 4]
    Wed = [5, 6]
    Thu = [7, 8]
    Fri = [9, 0]


# contains rush hours time limits in a day
class RushHours(enum.Enum):
    Morning = [datetime.time(7, 0), datetime.time(9, 30)]
    Evening = [datetime.time(16, 0), datetime.time(19, 30)]


# returns true if given time is within rush hours, false if not
def is_time_within_rush_hours(time_input):
    time_flag = False

    if ((RushHours.Morning.value[0] <= time_input <= RushHours.Morning.value[1]) or (
            RushHours.Evening.value[0] <= time_input <= RushHours.Evening.value[1])):
        time_flag = True

    return time_flag


# returns true if a car can go outside and false if not
def predictor(plate_input, date_input, time_input):
    plate = plate_input
    last_digit = int(plate[-1])
    date = datetime.datetime.strptime(date_input, "%d/%m/%Y")
    time = datetime.datetime.strptime(time_input, "%H:%M").time()
    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    selected_day_indx = datetime.datetime.date(date).weekday()
    selected_day = week_days[selected_day_indx]
    message_flag = True

    # verifies if car has a restriction for the given date
    # note that weekends do not have any restrictions
    if selected_day == "Monday":
        if last_digit == DateDigits.Mon.value[0] or last_digit == DateDigits.Mon.value[1]:
            if is_time_within_rush_hours(time):
                message_flag = False
    elif selected_day == "Tuesday":
        if last_digit == DateDigits.Tue.value[0] or last_digit == DateDigits.Tue.value[1]:
            if is_time_within_rush_hours(time):
                message_flag = False
    elif selected_day == "Wednesday":
        if last_digit == DateDigits.Wed.value[0] or last_digit == DateDigits.Wed.value[1]:
            if is_time_within_rush_hours(time):
                message_flag = False
    elif selected_day == "Thursday":
        if last_digit == DateDigits.Thu.value[0] or last_digit == DateDigits.Thu.value[1]:
            if is_time_within_rush_hours(time):
                message_flag = False
    elif selected_day == "Friday":
        if last_digit == DateDigits.Fri.value[0] or last_digit == DateDigits.Fri.value[1]:
            if is_time_within_rush_hours(time):
                message_flag = False

    return message_flag


# determines if a given license plate is valid or not
def plate_validation(plate_input):
    digits_num = len(plate_input)
    correct_format = True

    # checks if license plate has the correct format
    if digits_num != 6 and digits_num != 7:
        correct_format = False
    else:
        letters = plate_input[0:3]
        numbers = plate_input[3:]

        # checks if first three characters of plate are letters
        if not letters.isalpha():
            correct_format = False

        # checks if the last 3 or 4 characters are numbers
        if correct_format:
            numbers_length = len(numbers)

            if numbers_length != 3 and numbers_length != 4:
                correct_format = False
            else:
                if not numbers.isdigit():
                    correct_format = False

    return correct_format


# returns true if date has the correct format, false if not
def date_validation(date_input):
    format = "%d/%m/%Y"
    correct_format = True

    try:
        datetime.datetime.strptime(date_input, format)
    except ValueError:
        correct_format = False

    return correct_format


# returns true if time has the correct format, false if not
def time_validation(time_input):
    format = "%H:%M"
    correct_format = True

    try:
        datetime.datetime.strptime(time_input, format)
    except ValueError:
        correct_format = False

    return correct_format


def display_menu_options():
    print("1. Start Prediction")
    print("2. Exit")

# displays main menu that guides the user
def main():
    menu_option = -1

    user_plate = ""
    user_date = ""
    user_time = ""

    positive_message = "Prediction: You are allowed to take your car outside. Have a safe trip!"
    negative_message = "Prediction: Don't take your car outside. Stay at home until rush hours are over and avoid unnecessary fines."
    exit_message = "Thank you for using the Pico & Place Predictor. Hope to see you again soon!"

    # Title and welcoming message
    print("-----------------------------------------------------------------------")
    print("-----------------------------------------------------------------------")
    print("\t\t\t\t\t\tPICO & PLACA PREDICTOR")
    print("-----------------------------------------------------------------------")
    print("-----------------------------------------------------------------------")

    print("Welcome to the Pico & Placa predictor. To find out if you are allowed to")
    print("take your car outside just type your license plate, a date, and a time. With")
    print("this information the system will let you know if its ok to go outside or not.\n")

    while menu_option != 2:
        print("Please select one of the following options: ")
        display_menu_options()
        menu_option = input("Option: ")

        try:
            menu_option = int(menu_option)
        except ValueError:
            menu_option = -1

        # menu option 1 corresponds to the prediction functionality
        if menu_option == 1:
            print("Enter the following information.")
            valid_plate = False
            valid_date = False
            valid_time = False

            while not valid_plate:
                user_plate = input("License plate: ")

                if plate_validation(user_plate):
                    valid_plate = True
                else:
                    print("Invalid license plate!")

            while not valid_date:
                user_date = input("Date in (dd/mm/yyyy) format: ")

                if date_validation(user_date):
                    valid_date = True
                else:
                    print("Invalid date format!")

            while not valid_time:
                user_time = input("Time in (HH:MM) format: ")

                if time_validation(user_time):
                    valid_time = True
                else:
                    print("Invalid time format!")

            continue_option = ""
            prediction = predictor(user_plate, user_date, user_time)

            if prediction:
                print(positive_message)
            else:
                print(negative_message)

            print("Do you want to return to the main menu?")
            continue_option = input("Type 'y' if yes or any other key to exit program: ")

            if continue_option != 'y':
                print(exit_message)
                break

        # menu option 2 allows the user to exit program
        elif menu_option == 2:
            print(exit_message)
        # any other option is considered invalid
        else:
            print("Invalid option!")
            menu_option = -1


if __name__ == "__main__":
    main()
