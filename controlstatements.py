num=int(input("Enter a number: "))

if num%2==0:
    print(f"{num} is an even number.")

else:
    print(f"{num} is an odd number.")


    #create a program that checks if someone can vote or not using age above 18

    age=int(input("Enter your age: "))
    if age>=18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")

        #create a program to grade student a to fail

        marks=int(input("Enter your marks: "))

        if marks<=100 and marks>=80:
            print("You have an A")
        elif marks<=79 and marks>=60:
            print("You have an B")
        elif marks<=40 and marks>=59:
            print("You have an C")
        elif marks==0 and marks>=39:
            print("You have failed terribly")
        else:
            print("Invalid marks entered")