import os

# Function to check if a string contains alphabetic characters
def contains_alphabetic(s):
    return any(char.isalpha() for char in s)

# Function to get a numerical input with custom prompt
def get_numerical_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Invalid input. Please enter a numerical value.")

# Function to get the city for the flight
def get_city():
    while True:
        city = input("Enter the city you will be flying to: ")
        if contains_alphabetic(city):
            return city
        else:
            print("Invalid input. Please enter an alphanumeric value.")

# Function to get the number of nights for the hotel stay
def get_num_nights():
    while True:
        prompt = "Enter the number of nights you will stay at a hotel: "
        num_nights = get_numerical_input(prompt)
        if num_nights >= 0:
            return num_nights
        else:
            print("Invalid input. Number of nights cannot be negative.")

# Function to get the number of days for car rental
def get_rental_days():
    while True:
        prompt = "Enter the number of days for car rental: "
        rental_days = get_numerical_input(prompt)
        if rental_days >= 0:
            return rental_days
        else:
            print("Invalid input. Number of rental days cannot be negative.")

# Function to calculate the hotel cost based on a total of nights
def hotel_cost(num_nights):
    # Predefined hotel nightly rate
    HOTEL_NIGHTLY_RATE = 100  # Assuming £100 per night
    return HOTEL_NIGHTLY_RATE * num_nights

# Function to calculate the plane cost based on the selected city
def plane_cost(city):
    # Prices for different cities
    CITY_PRICES = {
        "London": 200.20,
        "Paris": 250.48,
        "New York": 500.35,
        "Tokyo": 700.33,
        "Milan": 180.44,
        "Amsterdam": 100.59,
        "Ankara": 240.22,
        "Bucharest": 310.43,
        "Sofia": 350.11,
        "Budapest": 280.10,
    }
    DEFAULT_PRICE = 300.55  # Default price if city not found
    return CITY_PRICES.get(city, DEFAULT_PRICE)

# Function to calculate the car rental cost based on total of rental days
def car_rental_cost(rental_days):
    # Predefined daily car rental rate
    DAILY_CAR_RENTAL_RATE = 50  # Assuming £50 per day
    return DAILY_CAR_RENTAL_RATE * rental_days

# Function to calculate the total holiday cost
def holiday_cost(city, num_nights, rental_days):
    # Calculate individual costs
    hotel = hotel_cost(num_nights)
    plane = plane_cost(city)
    car = car_rental_cost(rental_days)

    # Calculate total holiday cost
    total_cost = hotel + plane + car
    return hotel, plane, car, total_cost

# Main function to gather user inputs and calculate the holiday cost
def main():
    # Get user inputs
    city = get_city()
    num_nights = get_num_nights()
    rental_days = get_rental_days()

    # Calculate individual costs
    hotel, plane, car, total_cost = holiday_cost(city, num_nights, rental_days)

    # Print details about the holiday
    print("\nHoliday Details:")
    print("-" * 20)
    print(f"City: {city}")
    print(f"Number of Nights: {num_nights}")
    print(f"Number of Rental Days: {rental_days}")
    print("-" * 20)
    print(f"Hotel Cost: £{hotel:.2f}")
    print(f"Plane Cost: £{plane:.2f}")
    print(f"Car Rental Cost: £{car:.2f}")
    print("-" * 20)
    print(f"Total Holiday Cost: £{total_cost:.2f}")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()