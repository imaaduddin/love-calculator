print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_name = name1 + name2
lowercase_combined_name = combined_name.lower()

check_for_t = lowercase_combined_name.count("t")
check_for_r = lowercase_combined_name.count("r")
check_for_u = lowercase_combined_name.count("u")
check_for_e = lowercase_combined_name.count("e")

total_for_true = check_for_t + check_for_r + check_for_u + check_for_e

check_for_l = lowercase_combined_name.count("l")
check_for_o = lowercase_combined_name.count("o")
check_for_v = lowercase_combined_name.count("v")
check_for_e2 = lowercase_combined_name.count("e")

total_for_love = check_for_l + check_for_o + check_for_v + check_for_e2
total_score = int(str(total_for_true) + str(total_for_love))

if total_score < 10 or total_score > 90:
  print(f"Your score is {total_score}, you go together like coke and mentos.")
elif total_score >= 40 and total_score <= 50:
  print(f"Your score is {total_score}, you are alright together.") 
else:
  print(f"Your score is {total_score}")