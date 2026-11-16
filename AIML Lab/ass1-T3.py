def get_temperature():
    while True:
        try:
            temperature = float(input("Enter room temperature (0-50°C): "))

            if 0 <= temperature <= 50:
                return temperature
            else:
                print("Invalid temperature! Enter between 0 and 50.")

        except ValueError:
            print("Invalid input! Please enter a numeric value.")


# Function to get valid human presence
def get_presence():
    while True:
        presence = input(
            "Is a person present? (yes/no): "
        ).strip().lower()

        if presence == "yes":
            return True
        elif presence == "no":
            return False
        else:
            print("Invalid input! Please enter yes or no.")


# Intelligent Agent
def smart_home_agent(temperature, person_present):

    print("\n----- AGENT DECISION -----")

    if person_present:
        print("Person detected in the room.")

        # Control lights
        print("Lights: ON")

        # Control AC
        if temperature > 25:
            print("AC: ON")
            print("Room temperature is high.")
        else:
            print("AC: OFF")
            print("Room temperature is comfortable.")

    else:
        print("No person detected in the room.")
        print("Lights: OFF")
        print("AC: OFF")


# Main program
def main():

    # PEAS Representation
    print("===== PEAS REPRESENTATION =====")
    print("Performance Measure: Comfort and energy efficiency")
    print("Environment: Smart Home / Room")
    print("Actuators: AC and Lights")
    print("Sensors: Temperature Sensor and Motion Sensor")

    while True:

        print("\n===== SENSOR INPUTS =====")

        # Get sensor readings
        temperature = get_temperature()
        person_present = get_presence()

        # Agent processes the sensor inputs
        smart_home_agent(temperature, person_present)

        # Ask whether to continue
        while True:
            choice = input(
                "\nDo you want to continue? (yes/no): "
            ).strip().lower()

            if choice in ["yes", "no"]:
                break

            print("Invalid input! Enter yes or no.")

        if choice == "no":
            print("\nSmart Home Agent stopped.")
            break

main()
