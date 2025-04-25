#Employee Eligibility Check

employees = ["Imane", "Thomson", "Peter", "Gertrued", "Joe"]

departments = ["Sales", "HR", "IT", "Finance", "Marketing"]

ratings = [4.5, 3.8, 5.0, 2.5, 4.0]

eligible_departments = ("Sales", "IT", "Marketing")

min_rating =  4.0

if departments[0] in eligible_departments and ratings[0] >= min_rating:
    print(f"Imane from Sales is eligible for the bonus")
else:
    print(f"Imane from Sales is not eligible for the bonus")

if departments[1] in eligible_departments and ratings[1] >= min_rating:
    print(f"Thompson from HR is eligible for the bonus")
else:
    print(f"Thompson from HR is not eligible for the bonus")
    
if departments[2] in eligible_departments and ratings[2] >= min_rating:
    print(f"Peter from IT is eligible for the bonus")
else:
    print(f"Peter from IT  is not eligible for the bonus")
    
if departments[3] in eligible_departments and ratings[3] >= min_rating:
    print(f"Gertrude from Finance is eligible for the bonus")
else:
    print(f"Gertrude from Finance is not eligible for the bonus")
    
if departments[4] in eligible_departments and ratings[4] >= min_rating:
    print(f"Joe from Marketing is eligible for the bonus")
else:
    print(f"Joe from Marketing is not eligible for the bonus")
    
    
    
    