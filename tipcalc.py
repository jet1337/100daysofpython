# calculate the bill for x people
# tip added after split

bill = float(input("Enter the total amount for the bill: "))
party = int(input("Enter the amount of people in your party: "))
tip = float(input("Enter the percentage you each want to leave: ")) / 100

split_check = bill / party
final_amount =  split_check + split_check * tip

print(f"The final amount per person is {final_amount}")