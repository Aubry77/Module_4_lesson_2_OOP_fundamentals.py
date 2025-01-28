class Vehicle:
    """Represents a vehicle with a registration number, type, and owner."""

    def __init__(self, reg_num, vehicle_type, owner):
        """
        Initializes a new Vehicle instance.

        Parameters:
        reg_num (str): The registration number of the vehicle.
        vehicle_type (str): The type of the vehicle.
        owner (str): The owner of the vehicle.
        """
        self.registration_number = reg_num
        self.type = vehicle_type
        self.owner = owner

    def update_owner(self, new_owner):
        """
        Updates the owner of the vehicle.

        Parameters:
        new_owner (str): The new owner of the vehicle.
        """
        self.owner = new_owner
        print(f"Owner updated to {new_owner} for vehicle with registration number {self.registration_number}")

# Demonstration script
if __name__ == "__main__":
    
    #Demonstrates the creation of Vehicle instances and updating their owners.
    
    vehicle1 = Vehicle("ABC123", "Car", "John Doe")
    vehicle2 = Vehicle("XYZ789", "Motorcycle", "Jane Smith")

    # Display initial owners
    print(f"Initial owner of vehicle {vehicle1.registration_number}: {vehicle1.owner}")
    print(f"Initial owner of vehicle {vehicle2.registration_number}: {vehicle2.owner}")

    # Update owners
    vehicle1.update_owner("Alice Johnson")
    vehicle2.update_owner("Bob Brown")

    # Display updated owners
    print(f"Updated owner of vehicle {vehicle1.registration_number}: {vehicle1.owner}")
    print(f"Updated owner of vehicle {vehicle2.registration_number}: {vehicle2.owner}")


class Vehicle:
    
    """Represents a vehicle with a registration number, type, and owner."""

    def __init__(self, reg_num, vehicle_type, owner):
        
        """
        Initializes a new Vehicle instance.

        Parameters:
        reg_num (str): The registration number of the vehicle.
        vehicle_type (str): The type of the vehicle.
        owner (str): The owner of the vehicle.
        """
        self.registration_number = reg_num
        self.type = vehicle_type
        self.owner = owner

    def update_owner(self, new_owner):
        
        """
        Updates the owner of the vehicle.

        Parameters:
        new_owner (str): The new owner of the vehicle.
        """
        
        self.owner = new_owner
        print(f"Owner updated to {new_owner} for vehicle with registration number {self.registration_number}")

# Demonstration script
vehicle1 = Vehicle("ABC123", "Car", "John Doe")
vehicle2 = Vehicle("XYZ789", "Motorcycle", "Jane Smith")

# Display initial owners
print(f"Initial owner of vehicle {vehicle1.registration_number}: {vehicle1.owner}")
print(f"Initial owner of vehicle {vehicle2.registration_number}: {vehicle2.owner}")

# Update owners
vehicle1.update_owner("Alice Johnson")
vehicle2.update_owner("Bob Brown")

# Display updated owners
print(f"Updated owner of vehicle {vehicle1.registration_number}: {vehicle1.owner}")
print(f"Updated owner of vehicle {vehicle2.registration_number}: {vehicle2.owner}")
