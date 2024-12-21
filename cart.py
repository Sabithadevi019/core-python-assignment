def caluclate_total(cart):
    total=sum(cart.values())
    if len(cart)>=5:
            print("more than 5 items 10% discount")
            total = total * 0.9
    elif total>20000 and total<30000:
            print("more than 20 less than 30")
            total = total * 0.9
    elif total>50000:
            print("more than 50k")
            total=total*0.85
    return total
def cal(cart):
    sum=0
    print("more than 25000")
    for i in cart.values():
        if i>=25000:
            sum=sum+i
    return sum
cart={'laptop':2500,'headphone':40000,'mouse':25000,'monitor':30000,'cpu':4500}
print(caluclate_total(cart))
print(cal(cart))