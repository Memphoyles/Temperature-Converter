from tkinter import *


def celsius_converter(value, convert_to, output_entry):
    if value.isdigit():
        value = float(value)
    else:
        value = 0

    if convert_to == "Fahrenheit":
        output = value * 9 / 5 + 32
    elif convert_to == "Kelvin":
        output = 273 + value
    else:
        output = value

    output_entry.delete(0, END)
    output_entry.insert(0, output)


def fahrenheit_converter(value, convert_to, output_entry):
    if value.isdigit():
        value = float(value)
    else:
        value = 0

    value = float(value)
    if convert_to == "Celsius":
        output = (value - 32) * 5 / 9
    elif convert_to == "Kelvin":
        output = (value + 459.67) * 5 / 9
    else:
        output = value

    output_entry.delete(0, END)
    output_entry.insert(0, output)


def kelvin_converter(value, convert_to, output_entry):
    if value.isdigit():
        value = float(value)
    else:
        value = 0

    value = float(value)
    if convert_to == "Celsius":
        output = value - 273
    elif convert_to == "Fahrenheit":
        celsius = value - 273
        output = (celsius * 9 / 5) + 32
    else:
        output = value

    output_entry.delete(0, END)
    output_entry.insert(0, output)


def check_entry():
    if temperature_input.get() == "Celsius":
        celsius_converter(value_entry.get(), temperature_output.get(), output_entry)
    elif temperature_input.get() == "Kelvin":
        kelvin_converter(value_entry.get(), temperature_output.get(), output_entry)
    else:
        fahrenheit_converter(value_entry.get(), temperature_output.get(), output_entry)

        # root.after(200, check_entry)


def update_entry():
    temperature_input.trace("u", check_entry())
    root.after(1, update_entry)


root = Tk()
root.title("Ultimate Temperature Converter")

temperature_list = ["Celsius", "Kelvin", "Fahrenheit"]

temperature_input = StringVar(root)
temperature_input.set(temperature_list[0])

temperature_output = StringVar(root)
temperature_output.set(temperature_list[0])

value_entry = Entry(root)
value_entry.pack()

om_input = OptionMenu(root, temperature_input, "Celsius", "Kelvin", "Fahrenheit", command=lambda x: check_entry())
om_input.pack()

om_output = OptionMenu(root, temperature_output, "Celsius", "Kelvin", "Fahrenheit", command=lambda x: check_entry())
om_output.pack()

output_entry = Entry(root, state=NORMAL)
output_entry.pack()

root.after(1, update_entry)
root.mainloop()
