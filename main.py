
#  WEIGHT CONVERTER PROJECT

weight = float(input("Weight: "))
unit = input("(K)gs or (L)bs")

if unit.lower() == 'l' and type(weight) == float:
    weight = weight * 0.45
    print("Weight in Kgs: " + str(weight))

elif unit.lower() == 'k' and type(weight) == float:
    weight = weight / 0.45
    print("Weight in Lbs: " + str(weight))

else:
    print("Incorrect input!!!")
