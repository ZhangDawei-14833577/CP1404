
# Define a constant dictionary (COLOUR_CODES)
COLOUR_CODES = {
    "aliceblue": "#f0f8ff",
    "antiquwhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blanchedalmond": "#ffencd",
    "blue": "#0000ff"
}

# Prompt for input
colour_name = input("Enter a colour name: ").lower()

# Loop input until a blank line
while colour_name != "":
    try:
        print(f"The code for {colour_name} is {COLOUR_CODES[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter a colour name: ").lower()
