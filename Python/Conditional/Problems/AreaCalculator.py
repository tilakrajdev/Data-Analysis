# Area Calculator
print("***** Area Calculator *****")
print("""press 1 to get the area of square
press 2 to get the area of rectangle
press 3 to get the area of circle
press 4 to get the area of triangle""")

choice = int(input("Enter a number between 1-4: "))
if(choice == 1):
    side = float(input("Enter the length of side: "))
    area = side**2
    print("The area of square is ", area)
    
elif(choice == 2):
    side1 = float(input("Enter the side1 of the rectangle: "))
    side2 = float(input("Enter the side2 of the rectangle: "))
    area = side1 * side2
    print("The area of rectangle is ", area)

elif(choice == 3):
    radius = float(input("Enter the radius of the circle: "))
    area = 3.14 * radius**2
    print("The area of circle is ", area)
    
elif(choice == 4):
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = ((0.5) * base * height)
    print("The area of circle is ", area)