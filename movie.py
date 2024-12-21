def get_available_seats(total_seats, booked_seats):
    return [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]


def book_seat(booked_seats, seat_to_book):
    if seat_to_book in booked_seats:
        return f"Seat {seat_to_book} is already booked."
    booked_seats.append(seat_to_book)
    return f"Seat {seat_to_book} booked."


def cancel_seat(booked_seats, seat_to_cancel):
    if seat_to_cancel not in booked_seats:
        return f"Seat {seat_to_cancel} is not booked."
    booked_seats.remove(seat_to_cancel)
    return f"Seat {seat_to_cancel} canceled."
total_seats = 10
booked_seats = [2, 5, 7]
print(book_seat(booked_seats, 3))
print(cancel_seat(booked_seats, 5))
print("Available seats:", get_available_seats(total_seats, booked_seats))
