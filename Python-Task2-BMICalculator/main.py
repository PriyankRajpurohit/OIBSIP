"""A beginner-friendly command-line BMI calculator."""

from math import isfinite


def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Return BMI using kilograms and metres."""
    if not isfinite(weight_kg) or weight_kg <= 0:
        raise ValueError("Weight must be a positive number.")
    if not isfinite(height_m) or height_m <= 0:
        raise ValueError("Height must be a positive number.")

    try:
        height_squared = height_m**2
        if height_squared == 0:
            raise ValueError("Height is too small for this calculator's supported range.")
        bmi = weight_kg / height_squared
    except OverflowError as error:
        raise ValueError("Those values are outside the supported range.") from error

    if not isfinite(bmi) or bmi <= 0:
        raise ValueError("Those values are outside the supported range.")
    return bmi


def bmi_category(bmi: float) -> str:
    """Return the standard adult BMI category for a BMI value."""
    if not isfinite(bmi) or bmi <= 0:
        raise ValueError("BMI must be a finite, positive number.")
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25:
        return "Normal"
    if bmi < 30:
        return "Overweight"
    return "Obese"


def read_positive_number(prompt: str) -> float | None:
    """Read a positive finite number; return None if the user quits."""
    while True:
        entered = input(prompt).strip()
        if entered.lower() in {"q", "quit", "exit"}:
            return None

        try:
            value = float(entered)
        except ValueError:
            print("Please enter a number, such as 70 or 1.75.")
            continue

        if not isfinite(value):
            print("Please enter a finite number.")
        elif value <= 0:
            print("Please enter a number greater than zero.")
        else:
            return value


def main() -> None:
    print("BMI Calculator (metric units)")
    print("Enter q at either prompt to quit.\n")

    weight_kg = read_positive_number("Weight in kilograms: ")
    if weight_kg is None:
        print("Goodbye.")
        return

    height_m = read_positive_number("Height in metres: ")
    if height_m is None:
        print("Goodbye.")
        return

    try:
        bmi = calculate_bmi(weight_kg, height_m)
    except ValueError as error:
        print(f"Unable to calculate BMI: {error}")
        return
    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"Category: {bmi_category(bmi)}")
    print("\nBMI is a screening measure, not a diagnosis.")
    print("These categories are for adults aged 20 and older.")


if __name__ == "__main__":
    main()
