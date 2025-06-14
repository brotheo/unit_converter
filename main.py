# main.py
import argparse
import converter

# Map: category -> conversion code -> (from_unit, to_unit, function)
conversion_map = {
    "temperature": {
        "c2f": ("°C", "°F", converter.celsius_to_fahrenheit),
        "f2c": ("°F", "°C", converter.fahrenheit_to_celsius),
    },
    "distance": {
        "km2mi": ("km", "mi", converter.km_to_miles),
        "mi2km": ("mi", "km", converter.miles_to_km),
    },
    "weight": {
        "kg2lb": ("kg", "lb", converter.kg_to_pounds),
        "lb2kg": ("lb", "kg", converter.pounds_to_kg),
    }
}

def perform_conversion(category, conv, val):
    if conv in conversion_map.get(category, {}):
        from_unit, to_unit, func = conversion_map[category][conv]
        result = func(val)
        print(f"{val} {from_unit} = {result:.2f} {to_unit}")
    else:
        print(f"Unknown {category} conversion: {conv}")

def interactive_mode():
    print("Welcome to the Unit Converter!")
    print("Type 'exit' anytime to quit.")
    while True:
        print("\nCategories:", ", ".join(conversion_map.keys()))
        category = input("Enter category: ").strip().lower()
        if category == "exit":
            print("Exiting interactive mode.")
            break
        if category not in conversion_map:
            print("Invalid category. Please try again or type 'exit' to quit.")
            continue

        print("Available conversions:", ", ".join(conversion_map[category].keys()))
        conv = input("Enter conversion code: ").strip().lower()
        if conv == "exit":
            print("Exiting interactive mode.")
            break
        if conv not in conversion_map[category]:
            print("Invalid conversion code. Please try again or type 'exit' to quit.")
            continue

        val_input = input("Enter value to convert: ").strip()
        if val_input.lower() == "exit":
            print("Exiting interactive mode.")
            break

        try:
            val = float(val_input)
        except ValueError:
            print("Invalid number. Please try again or type 'exit' to quit.")
            continue

        perform_conversion(category, conv, val)

def main():
    parser = argparse.ArgumentParser(description="Unit Converter")
    parser.add_argument("category", nargs="?", help="Conversion category (e.g., temperature, distance, weight)")
    parser.add_argument("conversion", nargs="?", help="Conversion code (e.g. c2f, km2mi)")
    parser.add_argument("value", nargs="?", type=float, help="Value to convert")

    args = parser.parse_args()

    if args.category and args.conversion and args.value is not None:
        perform_conversion(args.category.lower(), args.conversion.lower(), args.value)
    else:
        interactive_mode()

if __name__ == "__main__":
    main()
