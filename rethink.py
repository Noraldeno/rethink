#Trip Cost


def gas(mileage):
	return (370.7 / mileage) * 3.00 * 2

def airBNB_cost(days, rent):
	cost = (days - 1) * rent
	return cost

def food(days, numPeople):
	return days * numPeople * 12 * 3

def ticket(numPeople):
	return numPeople * 45

def total_cost(mileage, days, numPeople, rent, vehicle):
	total = gas(mileage) + airBNB_cost(days, rent) + ticket(numPeople) + food(days, numPeople) + vehicle
	return total

def per_person(total, numPeople):
        return total/numPeople

numPeople = int(input("Enter number of people: "))
days = int(input("Enter number of days: "))
vehicle = float(input("Enter cost of vehicle: "))
mileage = float(input("Enter gas mileage of vehicle: "))
rent = float(input("Enter price of house rent: "))

total = total_cost(mileage, days, numPeople, rent, vehicle)
person = per_person(total, numPeople)


print("\n\n**********Cost Breakdown**********")
print("Number of People: %d"%(numPeople))
print("Number of days: %d"%(days))
print("Tickets: $%.2f"%(ticket(numPeople)))
print("Food: $%.2f"%(food(days, numPeople)))
print("AirBNB: $%.2f"%(airBNB_cost(days, rent)))
print("Gas: $%.2f"%(gas(mileage)))
print("Vehicle: $%.2f"%(vehicle))
print("_______________________________________")
print("The total cost is $%.2f.\nEach person will pay $%.2f"%(total, person))
