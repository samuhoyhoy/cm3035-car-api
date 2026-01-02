def clean_displacement(value):
    if value is None:
        return None

    value_str = str(value).strip()  # Convert to string

    if value_str == "":
        return None

    # Extract the first number using regex
    match = re.search(r'\d+(\.\d+)?', value_str)
    if match:
        return float(match.group())
    return None