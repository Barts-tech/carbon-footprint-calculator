# Carbon Footprint Calculator for Transport

def calculate_carbon_footprint():
    print("\n Welcome to the Carbon Footprint Calculator for Transport!")
    print("Choose the type of transport:")
    print("1: FTL (Full Truck Load)")
    print("2: LTL (Less Than Truck Load)")

    transport = int(input("Enter the transport type number (1-2):"))

    if transport not in [1, 2]:
        print("Invalid choice, please enter a valid number.")
        return
    
    try:
        distance = float(input("Enter the distance in kilometers (KM):"))
        load_weight = float(input("Enter the load weight in kilograms (KG):"))

        if distance <= 0 or load_weight <= 0:
            print("Distance and load weight must be greater than zero.")
            return
        # Convert weight from kg to tons 
        load_weight_tons = load_weight / 1000

        # CO₂ emission in kg per ton-kilometer (General data)
        emission_per_km = {
            1: 0.062,  # FTL (average)
            2: 0.150  # LTL (average)
        }

        emission = emission_per_km[transport] * distance * load_weight_tons
        transport_names = {1: "FTL Transport", 2: "LTL Transport"}
        print(f"\n A {transport_names[transport]} trip over a distance of {distance:.1f} km with a load of {load_weight:.1f} kg generates approximately {emission:.2f} kg of CO₂.")
    
    except ValueError:
        print("Invalid input. Please ensure you enter numeric values.")

if __name__ == "__main__":       
    calculate_carbon_footprint()

        



