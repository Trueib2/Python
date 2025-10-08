choice=input("Enter '1' to convert feet to meters or '2' to convert meters to feet:")
if choice=='1':
    feet=input("Enter the distance in feet:")
    meters=float(feet)*0.3048
    print("The distance in meters is:",meters)
elif choice=='2':
    meters=input("Enter the distance in meters:")
    feet=float(meters)*3.28084
    print("The distance in feet is:",feet)