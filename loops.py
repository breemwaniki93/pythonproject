#while loop
from datastructures import fruits

num=5

while num<=15:
    print(f"loop: {num} ")
    num+=1


#incremental loop
#create a loop from 100 decrease by 5 to zero

num=100

while num>=0:
    print(f"loop: {num} ")
    num-=5

    #for loop

    fruits=["mangoes","oranges","pineapples","apples"]

    for i in fruits:
        print(i)

        numbers=[23,1,4,65,98]
        numbers.sort()
        print(numbers)

        # Example of a while loop
        count = 1
        while count <= 5:
            print(count)  # Output: 1, 2, 3, 4, 5 (each on a new line)
            count += 1

