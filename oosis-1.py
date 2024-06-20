def calculate_BMI(weight, height):
    
    # Calculate BMI (Body Mass Index)
   
    bmi = weight / (height ** 2)
    return bmi

def get_bmi_category(BMI):
    
    # Get BMI category based on WHO classification
    
    if BMI < 20:
        return "Underweight"
    elif BMI < 25:
        return "Normal weight"
    elif BMI < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("BMI Calculator")
    print("----------------")

    weight = float(input("Enter your weight (in kg): "))
    height = float(input("Enter your height (in meters): "))

    BMI = calculate_BMI(weight, height)
    BMI_category = get_bmi_category(BMI)

    print(f"Your BMI is: {BMI:.2f}")
    print(f"Your BMI category is: {BMI_category}")

if __name__ == "__main__":
    main()