data = {
    1: [
        { "seat_name": "a1", "isTaken": True },
        { "seat_name": "a2", "isTaken": False },
        { "seat_name": "a3", "isTaken": True },
        { "seat_name": "a4", "isTaken": True },
        { "seat_name": "a5", "isTaken": False },
    ],
    2: [
        { "seat_name": "b1", "isTaken": False },
        { "seat_name": "b2", "isTaken": False },
        { "seat_name": "b3", "isTaken": True },
        { "seat_name": "b4", "isTaken": False },
        { "seat_name": "b5", "isTaken": True },
    ],
    3: [
        { "seat_name": "c1", "isTaken": False },
        { "seat_name": "c2", "isTaken": True },
        { "seat_name": "c3", "isTaken": True },
        { "seat_name": "c4", "isTaken": True },
        { "seat_name": "c5", "isTaken": False },
    ],
}

def find_nearest_free_seat(cart_num, seat_list, entered_seat):
    if cart_num not in data:
        print("Invalid cart number")
        return False

    nearest_seat_distance = float('inf')
    nearest_seat = None

    for cart_seat in seat_list:
        if not cart_seat['isTaken']:
            seat_distance = abs(ord(cart_seat['seat_name'][0]) - ord(entered_seat[0]))
            if seat_distance < nearest_seat_distance:
                nearest_seat_distance = seat_distance
                nearest_seat = cart_seat

    if nearest_seat:
        print(f"Your seat is taken, nearest free seat in cart {cart_num}, seat {nearest_seat['seat_name']}")
        return True
    else:
        print("No free seats in this cart")
        return False

def check_cart_seats(cart_num, entered_seat, unchecked_carts = [1, 2, 3]):
    if not find_nearest_free_seat(cart_num, data[cart_num], entered_seat):
        unchecked_carts.remove(cart_num)

        if unchecked_carts:
            new_cart_num = cart_num - 1 if cart_num > 1 else 3
            check_cart_seats(new_cart_num, entered_seat, unchecked_carts)
        else:
            print("No free seats")

def main():
    entered_cart = int(input("Enter your cart: "))
    entered_seat = input("Enter seat number: ").lower()
    
    check_cart_seats(entered_cart, entered_seat)
    
if __name__ == "__main__":
    main()
