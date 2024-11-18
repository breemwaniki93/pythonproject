#list datastructures, mutables(chnageable)

cars=["Nissan","Subaru","BMW","Mercedez"]
cars[1]="Subaru"


num=[6,5,7,1,3,4,12,0]


print(cars)
print(f"I love {cars[1]}")


#tuple,ordered,imutable,index
fruits=("Apple","Mangoes","Oranges","Watermelon","bananas")


print(fruits)
print(f"I love eating {fruits[2]}")


#set,unordered, non index
comp={"hp","dell","lenovo","Macbook"}
print(comp)

#dictionaries
employee={"name":"Daniel","age":34,"salary":30000}
print(employee)
print(f"The name of the employee is {employee['name']}")
print(f"The age of the employee is {employee['age']}")