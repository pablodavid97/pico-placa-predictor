import enum
import datetime


class DateDigits(enum.Enum):
    Mon = [1, 2]
    Tue = [3, 4]
    Wed = [5, 6]
    Thu = [7, 8]
    Fri = [9, 0]


class RushHours(enum.Enum):
    Morning = [datetime.time(7, 0), datetime.time(9, 30)]
    Evening = [datetime.time(16, 0), datetime.time(19, 30)]


def pico_placa(plate_input, date_input, time_input):
    plate = plate_input
    last_digit = int(plate[-1])
    date = datetime.datetime.strptime(date_input, "%d/%m/%Y")
    time = datetime.datetime.strptime(time_input, "%H:%M").time()
    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    selected_day_indx = datetime.datetime.date(date).weekday()
    selected_day = week_days[selected_day_indx]
    message_flag = True

    if selected_day == "Monday":
        if last_digit == DateDigits.Mon.value[0] or last_digit == DateDigits.Mon.value[1]:
            if ((RushHours.Morning.value[0] <= time <= RushHours.Morning.value[1]) or (
                    RushHours.Evening.value[0] <= time <= RushHours.Evening.value[1])):
                message_flag = False
    elif selected_day == "Tuesday":
        if last_digit == DateDigits.Tue.value[0] or last_digit == DateDigits.Tue.value[1]:
            if ((RushHours.Morning.value[0] <= time <= RushHours.Morning.value[1]) or (
                    RushHours.Evening.value[0] <= time <= RushHours.Evening.value[1])):
                message_flag = False
    elif selected_day == "Wednesday":
        if last_digit == DateDigits.Wed.value[0] or last_digit == DateDigits.Wed.value[1]:
            if ((RushHours.Morning.value[0] <= time <= RushHours.Morning.value[1]) or (
                    RushHours.Evening.value[0] <= time <= RushHours.Evening.value[1])):
                message_flag = False
    elif selected_day == "Thursday":
        if last_digit == DateDigits.Thu.value[0] or last_digit == DateDigits.Thu.value[1]:
            if ((RushHours.Morning.value[0] <= time <= RushHours.Morning.value[1]) or (
                    RushHours.Evening.value[0] <= time <= RushHours.Evening.value[1])):
                message_flag = False
    elif selected_day == "Friday":
        if last_digit == DateDigits.Fri.value[0] or last_digit == DateDigits.Fri.value[1]:
            if ((RushHours.Morning.value[0] <= time <= RushHours.Morning.value[1]) or (
                    RushHours.Evening.value[0] <= time <= RushHours.Evening.value[1])):
                message_flag = False

    return message_flag

def display_menu_options():
    print("1. Start Prediction")
    print("2. Exit")

def main():
    menu_option = -1

    # Test values
    user_plate = "ABC1233"
    user_date = "27/04/2021"
    user_time = "19:00"

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

        if(menu_option == 1):
            print("Enter the following information.")
            user_plate = input("License plate: ")
            user_date = input("Date in (dd/mm/yyyy) format: ")
            user_time = input("Time in (HH:MM) format: ")
            continue_option = ""
            prediction = pico_placa(user_plate, user_date, user_time)

            if prediction:
                print(positive_message)
            else:
                print(negative_message)

            print("Do you want to return to the main menu?")
            continue_option = input("Type 'y' if yes or any other key to exit program: ")

            if (continue_option != 'y'):
                print(exit_message)
                break

        elif(menu_option == 2):
            print(exit_message)
        else:
            print("Invalid option!")
            menu_option = -1


if __name__ == "__main__":
    main()