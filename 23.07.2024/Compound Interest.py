def compound_interest(principal, rate, time, n):
    amount = principal * (1 + rate / (n * 100)) ** (n * time)
    interest = amount - principal
    return interest

principal = 1000
rate = 5
time = 10
n = 12
print(f"Compound Interest: {compound_interest(principal, rate, time, n)}")
