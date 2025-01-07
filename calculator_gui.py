import tkinter as tk

def calculate_emission():
    try:
        transport = transport_var.get()  # Get selected transport
        distance = float(distance_entry.get())
        load_weight = float(weight_entry.get())

        if distance <= 0 or load_weight <= 0:
            raise ValueError("Distance and weight must be greater than zero.")

        # Emissions per km per ton
        emission_per_km = 0.062 if transport == "FTL" else 0.150
        load_weight_tons = load_weight / 1000  # Weight in tons
        emission = emission_per_km * distance * load_weight_tons

        # Display the result
        result_label.config(text=f"CO₂ Emission: {emission:.2f} kg", fg="green")
    except ValueError:
        result_label.config(text="Error: Please enter valid data.", fg="red")

# Main window
root = tk.Tk()
root.title("Carbon Footprint Calculator")
root.geometry("400x300")

# Label
label = tk.Label(root, text="Select type of transport:", font=("Arial", 12))
label.pack(pady=10)

# Transport selection
transport_var = tk.StringVar(value="FTL")  # Default to FTL
tk.Radiobutton(root, text="FTL (Full Truck Load)", variable=transport_var, value="FTL").pack()
tk.Radiobutton(root, text="LTL (Less Than Truck Load)", variable=transport_var, value="LTL").pack()

# Distance input
distance_label = tk.Label(root, text="Enter distance (km):", font=("Arial", 12))
distance_label.pack(pady=5)
distance_entry = tk.Entry(root)
distance_entry.pack()

# Weight input
weight_label = tk.Label(root, text="Enter load weight (kg):", font=("Arial", 12))
weight_label.pack(pady=5)
weight_entry = tk.Entry(root)
weight_entry.pack()

# Calculate button
calculate_button = tk.Button(root, text="Calculate Emission", command=calculate_emission)
calculate_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Run the application
root.mainloop()
