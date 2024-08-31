import tkinter as tk
from tkinter import ttk

def convertorForLength(a, a1, b):
    if a == 'mile' and b == 'kilometer':
        return a1 * 1.6
    elif a == 'mile' and b == 'meter':
        return a1 * 1600
    elif a == 'mile' and b == 'centimeter':
        return a1 * 160000
    elif a == 'mile' and b == 'millimeter':
        return a1 * 1600000
    elif a == 'kilometer' and b == 'mile':
        return a1 / 1.6
    elif a == 'kilometer' and b == 'meter':
        return a1 * 1000
    elif a == 'kilometer' and b == 'centimeter':
        return a1 * 100000
    elif a == 'kilometer' and b == 'millimeter':
        return a1 * 1000000
    elif a == 'meter' and b == 'kilometer':
        return a1 / 1000
    elif a == 'meter' and b == 'mile':
        return a1 / 1600
    elif a == 'meter' and b == 'centimeter':
        return a1 * 100
    elif a == 'meter' and b == 'millimeter':
        return a1 * 1000
    elif a == 'centimeter' and b == 'kilometer':
        return a1 / 100000
    elif a == 'centimeter' and b == 'mile':
        return a1 / 160000
    elif a == 'centimeter' and b == 'meter':
        return a1 / 100
    elif a == 'centimeter' and b == 'millimeter':
        return a1 * 10
    elif a == 'millimeter' and b == 'kilometer':
        return a1 / 1000000
    elif a == 'millimeter' and b == 'mile':
        return a1 / 1600000
    elif a == 'millimeter' and b == 'meter':
        return a1 / 1000
    elif a == 'millimeter' and b == 'centimeter':
        return a1 / 10

def convertorForWeight(a, a1, b):
    if a == 'kilogram' and b == 'gram':
        return a1 * 1000
    elif a == 'kilogram' and b == 'tonne':
        return a1 / 1000
    elif a == 'tonne' and b == 'kilogram':
        return a1 * 1000
    elif a == 'tonne' and b == 'gram':
        return a1 * 1000000
    elif a == 'gram' and b == 'tonne':
        return a1 / 1000000
    elif a == 'gram' and b == 'kilogram':
        return a1 / 1000

def convertorForTime(a, a1, b):
    if a == 'hour' and b == 'minute':
        return a1 * 60
    elif a == 'hour' and b == 'second':
        return a1 * 3600
    elif a == 'hour' and b == 'day':
        return a1 / 24
    elif a == 'hour' and b == 'week':
        return a1 / 168
    elif a == 'minute' and b == 'second':
        return a1 * 60
    elif a == 'minute' and b == 'hour':
        return a1 / 60
    elif a == 'minute' and b == 'week':
        return a1 / 10080
    elif a == 'minute' and b == 'day':
        return a1 / 1440
    elif a == 'second' and b == 'week':
        return a1 / 604800
    elif a == 'second' and b == 'hour':
        return a1 / 3600
    elif a == 'second' and b == 'minute':
        return a1 / 60
    elif a == 'second' and b == 'day':
        return a1 / 86400
    elif a == 'day' and b == 'second':
        return a1 * 86400
    elif a == 'day' and b == 'week':
        return a1 / 7
    elif a == 'day' and b == 'minute':
        return a1 * 1440
    elif a == 'day' and b == 'hour':
        return a1 * 24
    elif a == 'week' and b == 'second':
        return a1 * 604800
    elif a == 'week' and b == 'day':
        return a1 * 7
    elif a == 'week' and b == 'minute':
        return a1 * 10080
    elif a == 'week' and b == 'hour':
        return a1 * 168

def perform_conversion():
    unit_type = combo.get()
    from_unit = from_combo.get()
    to_unit = to_combo.get()
    amount = int(entry_amount.get())
    
    if unit_type == 'Length':
        result = convertorForLength(from_unit, amount, to_unit)
    elif unit_type == 'Weight':
        result = convertorForWeight(from_unit, amount, to_unit)
    elif unit_type == 'Time':
        result = convertorForTime(from_unit, amount, to_unit)
    
    label_result.config(text=f"Result: {result}")

# Створення головного вікна
root = tk.Tk()
root.title("Converter")

# Поле вибору типу конвертації
label_type = tk.Label(root, text="Choose what you want to convert:")
label_type.grid(row=0, column=0, padx=10, pady=10)
combo = ttk.Combobox(root, values=["Length", "Weight", "Time"])
combo.grid(row=0, column=1, padx=10, pady=10)

# Поле вибору одиниці з якої конвертувати
label_from = tk.Label(root, text="From what you want to convert:")
label_from.grid(row=1, column=0, padx=10, pady=10)
from_combo = ttk.Combobox(root)
from_combo.grid(row=1, column=1, padx=10, pady=10)

# Поле вибору одиниці в яку конвертувати
label_to = tk.Label(root, text="To what you want to convert:")
label_to.grid(row=2, column=0, padx=10, pady=10)
to_combo = ttk.Combobox(root)
to_combo.grid(row=2, column=1, padx=10, pady=10)

# Поле введення кількості
label_amount = tk.Label(root, text="How many:")
label_amount.grid(row=3, column=0, padx=10, pady=10)
entry_amount = tk.Entry(root)
entry_amount.grid(row=3, column=1, padx=10, pady=10)

# Кнопка виконання конвертації
button_convert = tk.Button(root, text="Convert", command=perform_conversion)
button_convert.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Результат
label_result = tk.Label(root, text="Result:")
label_result.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Оновлення одиниць залежно від типу конвертації
def update_units(event):
    unit_type = combo.get()
    if unit_type == 'Length':
        from_combo['values'] = ['mile', 'kilometer', 'meter', 'centimeter', 'millimeter']
        to_combo['values'] = ['mile', 'kilometer', 'meter', 'centimeter', 'millimeter']
    elif unit_type == 'Weight':
        from_combo['values'] = ['kilogram', 'gram', 'tonne']
        to_combo['values'] = ['kilogram', 'gram', 'tonne']
    elif unit_type == 'Time':
        from_combo['values'] = ['hour', 'minute', 'second', 'day', 'week']
        to_combo['values'] = ['hour', 'minute', 'second', 'day', 'week']

combo.bind("<<ComboboxSelected>>", update_units)

root.mainloop()
    