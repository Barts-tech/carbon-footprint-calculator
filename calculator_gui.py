import tkinter as tk

def calculate_emission():
    try:
        transport = transport_var.get()  # Pobierz wybrany transport
        distance = float(distance_entry.get())
        load_weight = float(weight_entry.get())

        if distance <= 0 or load_weight <= 0:
            raise ValueError("Odległość i waga muszą być większe od zera.")

        # Emisje na km na tonę
        emission_per_km = 0.062 if transport == "FTL" else 0.150
        load_weight_tons = load_weight / 1000  # Waga w tonach
        emission = emission_per_km * distance * load_weight_tons

        # Wyświetlenie wyniku
        result_label.config(text=f"Emisja CO₂: {emission:.2f} kg", fg="green")
    except ValueError:
        result_label.config(text="Błąd: Wprowadź poprawne dane.", fg="red")

# Główne okno
root = tk.Tk()
root.title("Kalkulator Śladu Węglowego")
root.geometry("400x300")

# Etykieta
label = tk.Label(root, text="Wybierz rodzaj transportu:", font=("Arial", 12))
label.pack(pady=10)

# Pole wyboru transportu
transport_var = tk.StringVar(value="FTL")  # Domyślnie FTL
tk.Radiobutton(root, text="FTL (pełny ładunek)", variable=transport_var, value="FTL").pack()
tk.Radiobutton(root, text="LTL (częściowy ładunek)", variable=transport_var, value="LTL").pack()

# Pole tekstowe dla odległości
distance_label = tk.Label(root, text="Podaj odległość (km):", font=("Arial", 12))
distance_label.pack(pady=5)
distance_entry = tk.Entry(root)
distance_entry.pack()

# Pole tekstowe dla wagi
weight_label = tk.Label(root, text="Podaj wagę ładunku (kg):", font=("Arial", 12))
weight_label.pack(pady=5)
weight_entry = tk.Entry(root)
weight_entry.pack()

# Przycisk
calculate_button = tk.Button(root, text="Oblicz emisję", command=calculate_emission)
calculate_button.pack(pady=10)

# Wynik
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Uruchomienie aplikacji
root.mainloop()
