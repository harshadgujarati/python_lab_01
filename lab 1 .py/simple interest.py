def calculate_simple_interest(principal, time, rate):
    simple_interest = (principal * time * rate) / 100
    return simple_interest

principal = float(input("Enter the principal amount: "))
time = float(input("Enter the time (in years): "))
rate = float(input("Enter the rate of interest (per annum): "))

interest = calculate_simple_interest(principal, time, rate)

print(f"Simple Interest: {interest}")