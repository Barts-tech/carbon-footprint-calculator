# eco_transport_interface.py

import tkinter as tk 
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def calculate_fuel_efficiency():
    try:
        # Retrieve data from input fields
        load_type = load_type_var.get()
        load_weight = float(load_weight_entry.get())
        distance = float(distance_entry.get())
        fuel_consumption = float(fuel_consumption_entry.get())
        fuel_type = fuel_type_var.get()

        if load_type == "FTL":
            efficiency_penalty = 0.1 * load_weight  # Full load
        elif load_type == "LTL":
            efficiency_penalty = 0.05 * load_weight  # Partial load (less impact)

        # Set CO2 emission per liter of fuel
        if fuel_type == "gasoline":
            co2_emission_per_liter = 2.31  # kg CO2 per liter
        elif fuel_type == "diesel":
            co2_emission_per_liter = 2.68  # kg CO2 per liter
        else:
            raise ValueError("Invalid fuel type")

        # Calculations
        total_fuel = (fuel_consumption + efficiency_penalty) * distance / 100
        co2_emission = total_fuel * co2_emission_per_liter

        # Display results in the window
        result_text.set(f"Estimated fuel consumption: {total_fuel:.2f} liters\nEstimated CO2 emissions: {co2_emission:.2f} kg")

        # Set text color based on CO2 emissions
        if co2_emission < 100:  # If emissions are low, green color
            result_label.config(fg="green")
            comment.set("Eco-friendly! Keep it up!")
        elif co2_emission < 500:  # If emissions are moderate, orange color
            result_label.config(fg="orange")
            comment.set("Consider reducing emissions.")
        else:  # If emissions are high, red color
            result_label.config(fg="red")
            comment.set("Your emissions are too high! Take action to protect the planet!")

        # Save results for PDF generation
        global pdf_data
        pdf_data = {
            "load_type": load_type,
            "load_weight": load_weight,
            "distance": distance,
            "fuel_consumption": fuel_consumption,
            "fuel_type": fuel_type,
            "total_fuel": total_fuel,
            "co2_emission": co2_emission
        }

    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {str(e)}")

def generate_pdf():
    try:
        if not pdf_data:
            messagebox.showerror("Error", "No data available to generate PDF. Please calculate first.")
            return

        filename = "fuel_efficiency_report.pdf"
        c = canvas.Canvas(filename, pagesize=letter)
        c.setFont("Helvetica", 12)

        c.drawString(100, 750, "Fuel Efficiency and CO2 Emission Report")
        c.drawString(100, 730, f"Transport Type: {pdf_data['load_type']}")
        c.drawString(100, 710, f"Load Weight: {pdf_data['load_weight']} tons")
        c.drawString(100, 690, f"Distance: {pdf_data['distance']} km")
        c.drawString(100, 670, f"Fuel Consumption: {pdf_data['fuel_consumption']} liters/100 km")
        c.drawString(100, 650, f"Fuel Type: {pdf_data['fuel_type']}")
        c.drawString(100, 630, f"Total Fuel Used: {pdf_data['total_fuel']:.2f} liters")
        c.drawString(100, 610, f"CO2 Emissions: {pdf_data['co2_emission']:.2f} kg")

        c.save()

        messagebox.showinfo("Success", f"PDF report generated: {os.path.abspath(filename)}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate PDF: {str(e)}")

# Main application window
root = tk.Tk()
root.title("Eco Transport Interface")
root.geometry("600x500")
root.configure(bg="#f0f8ff")

# GUI variables
load_type_var = tk.StringVar()
fuel_type_var = tk.StringVar()
result_text = tk.StringVar()
comment = tk.StringVar()
pdf_data = None

# Enhanced styling
def create_label(master, text, row, col, **kwargs):
    label = tk.Label(master, text=text, bg="#f0f8ff", font=("Arial", 12))
    label.grid(row=row, column=col, padx=10, pady=5, **kwargs)
    return label

def create_entry(master, row, col, **kwargs):
    entry = tk.Entry(master, font=("Arial", 12))
    entry.grid(row=row, column=col, padx=10, pady=5, **kwargs)
    return entry

def create_button(master, text, command, row, col, **kwargs):
    button = tk.Button(master, text=text, command=command, font=("Arial", 12), bg="#4682b4", fg="white", relief="groove", cursor="hand2")
    button.grid(row=row, column=col, padx=10, pady=15, **kwargs)
    return button

def create_radiobutton(master, text, variable, value, row, col, **kwargs):
    radiobutton = tk.Radiobutton(master, text=text, variable=variable, value=value, bg="#f0f8ff", font=("Arial", 12), cursor="hand2")
    radiobutton.grid(row=row, column=col, padx=10, pady=5, **kwargs)
    return radiobutton

# Interface - Labels and input fields
create_label(root, "Select transport type:", 0, 0)
create_radiobutton(root, "FTL (Full Load)", load_type_var, "FTL", 0, 1)
create_radiobutton(root, "LTL (Partial Load)", load_type_var, "LTL", 0, 2)

create_label(root, "Enter load weight (tons):", 1, 0)
load_weight_entry = create_entry(root, 1, 1)

create_label(root, "Enter distance (km):", 2, 0)
distance_entry = create_entry(root, 2, 1)

create_label(root, "Enter fuel consumption (liters per 100 km):", 3, 0)
fuel_consumption_entry = create_entry(root, 3, 1)

create_label(root, "Fuel type:", 4, 0)
create_radiobutton(root, "Gasoline", fuel_type_var, "gasoline", 4, 1)
create_radiobutton(root, "Diesel", fuel_type_var, "diesel", 4, 2)

# Calculate button
calculate_button = create_button(root, "Calculate", calculate_fuel_efficiency, 5, 1)

# Generate PDF button
generate_pdf_button = create_button(root, "Generate PDF Report", generate_pdf, 6, 1)

# Result display field
result_label = tk.Label(root, textvariable=result_text, justify="left", bg="#f0f8ff", font=("Arial", 12))
result_label.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

# Environmental comment
comment_label = tk.Label(root, textvariable=comment, justify="left", bg="#f0f8ff", font=("Arial", 12, "italic"))
comment_label.grid(row=8, column=0, columnspan=3, padx=10, pady=5)

# Run the application
root.mainloop()
