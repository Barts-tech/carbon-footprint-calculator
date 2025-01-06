#Carbon Footprint Calculator for Transport

def calculate_carbon_footprint():
    print("\n Witaj w kalkulatorze śladu węglowego dla transportu!")
    print("Wybierz rodzaj transportu:")
    print("1: FTL ( Full truck Load)")
    print("2: LTL ( Less than Truck Load)")

    transport = int(input("Wprowadź numer typu transportu (1-2):"))

    if transport not in [1, 2]:
        print("Nieprawidłowy wybór, wprowadź numer ponownie.")
        return
    
    try:
        distance = float(input("Podaj odległość w kilometrach (KM):"))
        load_weight = float(input("Podaj masę ładunku w kilogramach (KG):"))

        if distance <= 0 or load_weight <= 0:
            print("Odległość oraz masa ładunku muszą być większe od zera.")
            return
        # Konwersja masy z kg na tony 
        load_weight_tons = load_weight / 1000

        # Emisja CO₂ w kg na tonokilometr (Dane ogólne)
        emission_per_km = {
        1: 0.062,  # FTL (średnio)
        2: 0.150  # LTL (średnio)
        }

        emission = emission_per_km[transport] * distance * load_weight_tons
        transport_names = {1: "Transport FTL", 2: "Transport LTL"}
        print(f"\nPodróż {transport_names[transport]} na odległość {distance:.1f} km z ładunkiem {load_weight:.1f} kg generuje około {emission:.2f} kg CO₂.")
    
    except ValueError:
        print("Nieprawidłowe dane wejściowe. Upewnij się, że podajesz liczby.")

        #wywołanie funkcji
if __name__ == "__main__":       
    calculate_carbon_footprint()


        



