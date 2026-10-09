name = input("Enter your Fullname: ")
role = input("Enter the field your working in: ")
prlanguage = input("Enter your favorite programming language: ")
exp = int(input("Entert the number coding exp you have: "))
goal = input("What is your primary goal for 2026: ")


bio_card = f"""

==================================
                BIO
==================================
Applicant Name: {name}
Current_Field: {role}
Favorite_Programming_language: {prlanguage}
Experience_of_working: {exp}
Goal_for_2026: {goal}

"""

with open("user_bio.txt", "w") as f:
    f.write(bio_card)

with open("user_bio.txt", "r") as f:
    saved_content = f.read()

print("[SUCCESS]: File written and verified.")
print(saved_content)