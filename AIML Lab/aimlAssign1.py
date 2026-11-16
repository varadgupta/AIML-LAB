# Metallurgical Blast Furnaces

def temp_cont(temp):
    if 500 <= temp <= 2200:
        print(f"Temperature = {temp:.1f}°C (Normal)")
    elif temp > 2200:
        print("Temperature exceeding safety range!")
        print("Executing cooling mechanism...")

        while temp > 1500:
            temp -= 1      # Cooling mechanism

        print(f"Temperature stabilized at {temp:.1f}°C")
    else:
        print("Temperature below safety range!")
        print("Executing heating mechanism...")

        while temp < 1500:
            temp += 1      # Heating mechanism

        print(f"Temperature stabilized at {temp:.1f}°C")

print("===== Select temperature unit =====")
print("1. Celsius")
print("2. Fahrenheit")
print("3. Kelvin")
print("4. Exit")

while True:
  choice = int(input("Choose option: "))

  if choice == 1:
      i_temp = float(input("Enter temperature (°C): "))
      while i_temp < 100 or i_temp > 2500:
          i_temp = float(input("Enter a valid temperature (100-2500 °C): "))
      temp = i_temp
      temp_cont(temp)

  elif choice == 2:
      i_temp = float(input("Enter temperature (°F): "))
      while i_temp < 212 or i_temp > 4532:
          i_temp = float(input("Enter a valid temperature (212-4532 °F): "))
      temp = (i_temp - 32) * 5 / 9
      temp_cont(temp)

  elif choice == 3:
      i_temp = float(input("Enter temperature (K): "))
      while i_temp < 373 or i_temp > 2773:
          i_temp = float(input("Enter a valid temperature (373-2773 K): "))
      temp = i_temp - 273.15
      temp_cont(temp)

  elif choice == 4:
    print("Exiting!")
    break

  else:
    print("Invalid choice!")

# if temp is not None:
#     temp_cont(temp)