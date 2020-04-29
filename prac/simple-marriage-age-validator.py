
gender = input("Type in your gender (male/female): ")

print( "You are a {}".format(gender) )

age = int(input("Type your age: "))

print( "You are {} ".format(age) )

if gender == "male" and age >= 21:
    print("Congratulations! You are {} and a {}. So, you are eligible to get married!".format(age, gender))
elif gender == "male" and age < 21:
    print( "Sorry! You are {} and a {}. So, you are not eligible to get married!".format(age, gender))
elif gender == "female" and age >= 18:
    print("Congratulations! You are {} and a {}. So, you are eligible to get married!".format(age, gender))
elif gender == "female" and age < 18:
    print( "Sorry! You are {} and a {}. So, you are not eligible to get married!".format(age, gender))    
else:
    print("Please insert credentials accurtely!")

