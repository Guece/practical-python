# mortgage.py
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

months = 1
extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if months >= extra_payment_start_month and months < extra_payment_end_month:
        paid = payment + extra_payment
    else:
        paid = payment 
    
    principalBefore = principal
    principal = principal * (1+rate/12) - paid
    if principal < 0:
        paid = principalBefore
        principal = 0

    total_paid = total_paid + paid
   
    output = f"{months} Monate :: ${total_paid:0.2f} Paid :: ${principal:0.2f} Remaining"
    print(output)
    months = months + 1
# Exercise 1.7
