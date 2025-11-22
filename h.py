# CALCULATES SPEED IN KM/H AND OPTIONALLY CONVERTS TO MPH BASED ON USER INPUT.

# Function to check if the input value is a valid float
def check_valid_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Get user input for distance and time, validate if they are valid floats
while True:
    # Prompt user to enter distance and time values
    abc = raw_input("Enter distance traveled in kms: ")
    xyz = raw_input("Enter hours required: ")

    # Check if both inputs are valid floats
    if not check_valid_float(abc) or not check_valid_float(xyz):
        # Display error message for invalid input
        print("Invalid input: Please enter a valid number.")
    else:
        # Convert inputs to floats
        ABC = float(abc)
        XYZ = float(xyz)

        # Check if inputs are positive values
        if ABC <= 0 or XYZ <= 0:
            # Display error message for non-positive values
            print("Invalid input: Distance and hours should be greater than zero.")
        else:
            # Calculate speed in km/h
            speed = float(ABC / XYZ)
            # Display calculated speed
            print("Speed is {} km/h".format(speed))
            # Exit the input loop as valid input is obtained
            break

# Ask the user if they want to convert the speed to miles/h
while True:

    ASK = input("Do you want to convert the speed from km/h to miles/h? Type 'yes' or 'no': ").lower()
    if ASK == "yes":
    # Convert speed to miles/h and display the result
        speed_miles = speed * 0.621371
        print("Speed is {} miles/h".format(speed_miles))
    elif ASK == "no":
    # Display thank you message if conversion is not requested
        print("Thanks")
        break   