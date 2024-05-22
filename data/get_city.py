import csv

# Define the input and output file names
input_file = 'eu_flights.csv'
output_file = 'flights_with_details.csv'

# Define the mapping of cities to countries and airport codes
city_details = {
    'Amsterdam': ('Netherlands', 'AMS'),
    'Athens': ('Greece', 'ATH'),
    'Barcelona': ('Spain', 'BCN'),
    'Berlin': ('Germany', 'BER'),
    'Brussels': ('Belgium', 'BRU'),
    'Copenhagen': ('Denmark', 'CPH'),
    'Dublin': ('Ireland', 'DUB'),
    'Edinburgh': ('United Kingdom', 'EDI'),
    'Frankfurt': ('Germany', 'FRA'),
    'Geneva': ('Switzerland', 'GVA'),
    'Istanbul': ('Turkey', 'IST'),
    'Lisbon': ('Portugal', 'LIS'),
    'London': ('United Kingdom', 'LHR'),  # Assuming Heathrow
    'Madrid': ('Spain', 'MAD'),
    'Milan': ('Italy', 'MXP'),  # Assuming Malpensa
    'Nice': ('France', 'NCE'),
    'Paris': ('France', 'CDG'),  # Assuming Charles de Gaulle
    'Reykjavik': ('Iceland', 'KEF'),
    'Rome': ('Italy', 'FCO'),  # Assuming Fiumicino
    'Shannon': ('Ireland', 'SNN'),
    'Stockholm': ('Sweden', 'ARN'),
    'Zurich': ('Switzerland', 'ZRH')
}

# Read the input CSV file
with open(input_file, 'r') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Read the header
    rows = list(reader)

# Add the new columns to the header
header.extend(['Country', 'Airport Code'])

# Process the rows to add country and airport code
new_rows = []
for row in rows:
    city = row[0]
    country, airport_code = city_details.get(city, ('Unknown', 'Unknown'))
    new_row = row + [country, airport_code]
    new_rows.append(new_row)

# Write the data to a new CSV file
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)  # Write the header
    writer.writerows(new_rows)  # Write the rows

print(f"Data has been successfully written to {output_file}")