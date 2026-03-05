import random

MIN_LIMIT = 1
MAX_LIMIT = 1000

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int] | str:
    if min < MIN_LIMIT:
        return f"Min should be more than {MIN_LIMIT}"
    if max > MAX_LIMIT:
        return f"Max should be less than {MAX_LIMIT}"
    if min > max:
        return "Invalid min or max parameters"
    if quantity < 1 or quantity > (max - min + 1):
        return "Invalid quantity parameter"
    
    numbers_range = range(min, max + 1)
    numbers_ticket = random.sample(numbers_range, quantity)

    return sorted(numbers_ticket)

