import datetime
import random

class Train:
    def __init__(self, name, departure_city, arrival_city, departure_time):
        self.name = name
        self.departure_city = departure_city
        self.arrival_city = arrival_city
        self.departure_time = departure_time  # string format: 'YYYY-MM-DD HH:MM'
        self.delay_minutes = 0

    def predict_arrival(self):
        # Fixed travel time in hours (simplified assumption)
        travel_time_hours = 5

        # Simulate random delay between 0 and 120 minutes
        self.delay_minutes = random.randint(0, 120)

        # Convert departure time string to datetime object
        departure_datetime = datetime.datetime.strptime(self.departure_time, '%Y-%m-%d %H:%M')

        # Calculate predicted arrival time including delay
        arrival_datetime = departure_datetime + datetime.timedelta(hours=travel_time_hours, minutes=self.delay_minutes)

        return arrival_datetime.strftime('%Y-%m-%d %H:%M')

def main():
    print("Welcome to Railway Time Tracking & Arrival Prediction System\n")

    # Take user input for train details
    train_name = input("Enter train name: ")
    departure_city = input("Enter departure city: ")
    arrival_city = input("Enter arrival city: ")
    departure_time = input("Enter departure time (YYYY-MM-DD HH:MM): ")

    # Create Train object
    train = Train(train_name, departure_city, arrival_city, departure_time)

    # Predict arrival time
    predicted_arrival = train.predict_arrival()

    # Display results
    print(f"\nTrain '{train.name}' from {train.departure_city} to {train.arrival_city} is predicted to arrive at {predicted_arrival}.")
    print(f"Estimated delay: {train.delay_minutes} minutes.")

if __name__ == "__main__":
    main()
