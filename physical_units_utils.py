
"""
This module implements various functions for physical units conversion.
"""
import numbers

def convert_speed(value, actual_unit: str, target_unit: str):
    """
    Convert speed value from actual_unit to target_unit. Return converted value.
    :param value: numeric value to convert
    :param actual_unit: string actual physical unit (mph, kph)
    :param target_unit: string target physical unit (mph, kph)
    :return: converted value
    :raises ValueError: exception due to wrong value, actual_unit, target_unit value
    """
   
    # test acceptable inputs
    if isinstance(value, numbers.Number) and \
            all(x in ["mph", "kph"] for x in [actual_unit, target_unit]):
        # check units equality
        if actual_unit == target_unit:
            return value
        # dictionary for conversion, key is target unit
        conversion = {"mph": lambda x: x * 0.621371192,
                    "kph": lambda x: x * 1.609344
                    }
        return conversion[target_unit](value)
    raise ValueError("value must be numeric,"
                    " actual_unit and target_unit accept only mph (mile) or kph values")

def convert_temperature(value, actual_unit: str, target_unit: str):
    """
    Convert temperature value from actual_unit to target_unit. Return converted value.
    :param value: numeric value to convert
    :param actual_unit: string actual physical unit (C, F)
    :param target_unit: string target physical unit (C, F)
    :return: converted value
    :raises ValueError: exception due to wrong value, actual_unit, target_unit value
    """
    # test acceptable inputs
    if isinstance(value, numbers.Number) and \
            all(x in ["C", "F"] for x in [actual_unit, target_unit]):
        # check units equality
        if actual_unit == target_unit:
            return value
        # dictionary for conversion, key is target unit
        conversion = {"C": lambda x: (x - 32) * 5 / 9,
                    "F": lambda x: x * 9 / 5 + 32
                    }
        return conversion[target_unit](value)
    raise ValueError("value must be numeric,"
                    " actual_unit and target_unit accept only C or F values")


def convert_length(value, actual_unit: str, target_unit: str):
    """
    Convert length value from actual_unit to target_unit. Return converted value.
    :param value: numeric value to convert
    :param actual_unit: string actual physical unit (m, ft)
    :param target_unit: string target physical unit (m, ft)
    :return: converted value
    :raises ValueError: exception due to wrong value, actual_unit, target_unit value
    """
    # test acceptable inputs
    if isinstance(value, numbers.Number) and \
            all(x in ["m", "ft"] for x in [actual_unit, target_unit]):
        # check units equality
        if actual_unit == target_unit:
            return value
        # dictionary for conversion, key is target unit
        conversion = {"ft": lambda x: x * 3.28084,
                    "m": lambda x: x / 3.28084
                    }
        return conversion[target_unit](value)
    raise ValueError("value must be numeric,"
                    " actual_unit and target_unit accept only m or ft values")


def main():
    while True:
        # Ask user for physical parameter
        physical_parameter = input("Which physical parameter do you want to convert? (speed, length or temperature): ")
        valid_parameters = ["speed", "length", "temperature"]
        if physical_parameter.lower() not in valid_parameters:
            print("Invalid input. Please choose from: ", valid_parameters)
        else:
            break

    while True:
        try:
            value = float(input("Enter the value: "))
            break  # exit loop if no exception is raisd
        except ValueError():
            print("Invalid input. Please try again. The value needs to be a number-numeric.")
    # Convert based on physical parameter+ask for unit-loop for exceptions if not the unit from two choices-error handled
    if physical_parameter.lower() == "speed":
        while True:
            actual_unit = input("Enter the actual unit (mph or kph): ")
            target_unit = input("Enter the target unit (mph or kph): ")
            if actual_unit.lower() not in ["mph", "kph"] or target_unit.lower() not in ["mph", "kph"]:
                print("Invalid input. Please enter either 'mph' or 'kph' for units.")
            else:
                break
        result = convert_speed(float(value), actual_unit.lower(), target_unit.lower())
        print(f"{value} {actual_unit} is equal to {result} {target_unit}.")

    elif physical_parameter.lower() == "length":
        while True:
            actual_unit = input("Enter the actual unit (m or ft): ")
            target_unit = input("Enter the target unit(m or ft): ")
            if actual_unit.lower() not in ["m", "ft"] or target_unit.lower() not in ["m", "ft"]:
                print("Invalid input. Please enter either 'm' or 'ft' for units.")
            else:
                break
        result = convert_length(float(value), actual_unit.lower(), target_unit.lower())
        print(f"{value} {actual_unit} is equal to {result} {target_unit}.")

    elif physical_parameter.lower() == "temperature":
        while True:
            actual_unit = input("Enter the actual unit (C or F): ")
            target_unit = input("Enter the target unit (C or F): ")
            if actual_unit.upper() not in ["C", "F"] or target_unit.upper() not in ["C", "F"]:
                print("Invalid input. Please enter either 'C' or 'F' for units.")
            else:
                break
        result = convert_temperature(float(value), actual_unit.upper(), target_unit.upper())
        print(f"{value} {actual_unit} is equal to {result} {target_unit}.")

if __name__ == "__main__":
    main()
