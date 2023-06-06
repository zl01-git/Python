pencil_qty, pen_qty, feltpen_qty = map(int, input().split())

pencil_price = 3
pen_price = pencil_price + 2
feltpen_price = pen_price + 7
total_price = (pencil_qty * pencil_price + 
               pen_qty * pen_price + 
               feltpen_qty * feltpen_price)
print(total_price)