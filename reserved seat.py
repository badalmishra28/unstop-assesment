def reserve_seats(requested_seats):
    # Example seat layout (initially all available)
    seat_layout = [
        ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7'],
        ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7'],
        # ...
        ['K1', 'K2', 'K3']  # Last row
    ]
    # Check if a row can accommodate the requested seats
    for row in seat_layout:
        available_seats = [seat for seat in row if seat_available(seat)]
        if len(available_seats) >= requested_seats:
            # Book consecutive seats in this row
            booked_seats = available_seats[:requested_seats]
            for seat in booked_seats:
                mark_as_booked(seat)
            return booked_seats
    
    # If no single row can accommodate, find nearby seats
    return split_seat_allocation(requested_seats)

def seat_available(seat):
    # Query the seat status from the database
    pass

def mark_as_booked(seat):
    # Update the seat status in the database
    pass
