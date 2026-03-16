flights = {
    "AV101": ("Bogota", 5, 300),
    "AV202": ("Medellin", 3, 200),
    "AV303": ("Cartagena", 4, 250),
    "AV404": ("Cali", 2, 220)
}

bookings = []
money = 0

print('Welcome to the AirCumbia')

option = 'yes'

while option == 'yes':
    name = input('type the name of the passenger\n')
    flight_code = input('type the flight code\n').upper()
    
    if flights.get(flight_code):
        amount = int(input('type the amount of passengers\n'))
        
        flight_info = flights[flight_code]
        available_amount = flight_info[1]
        
        if amount > available_amount:
            print('insufficient available amount')
        else:
            bookings.append((name, flight_code, amount))
            money += flight_info[2]
            # Actualiza el diccionario creando una nueva tupla con el stock restante
            flights[flight_code] = (flight_info[0], available_amount - amount, flight_info[2])
    else:
        print('this code is not valid')

    option = input('would you like to add a new booking? yes/no\n')

print(bookings)
print(flights)