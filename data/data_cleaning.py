import csv

# Define the input and output file names
input_file = 'data/eu_flights.txt'
output_file = 'eu_flights.csv'

# Read the text file
with open(input_file, 'r') as file:
    lines = file.readlines()

# Process the lines to remove "Flights to" and strip whitespace
cities = [line.replace('Flights to ', '').strip() for line in lines]

# Write the data to a CSV file
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['City'])  # Write the header
    for city in cities:
        writer.writerow([city])  # Write each city

print(f"Data has been successfully written to {output_file}")
