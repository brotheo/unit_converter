import argparse
import converter

# Mapping of categories and conversion codes to functions
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

# Argument parser for CLI
parser = argparse.ArgumentParser(description="Unit Converter")
parser.add_argument("category", choices=conversion_map.keys(), help="Conversion category")
parser.add_argument("conversion", help="Conversion code (e.g. c2f, km2mi)")
parser.add_argument("value", type=float, help="Value to convert")
args = parser.parse_args()

def perform_conversion():
    category = args.category
    conv = args.conversion.lower()
    val = args.value

    # Lookup the conversion function
    if conv in conversion_map[category]:
        from_unit, to_unit, func = conversion_map[category][conv]
        result = func(val)
        print(f"{val} {from_unit} = {result:.2f} {to_unit}")
    else:
        print(f"Unknown {category} conversion: {conv}")

perform_conversion()

