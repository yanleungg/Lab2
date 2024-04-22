def calculate_bmi(height,weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

#code to calc bmi
    bmi = weight/(height*height)
    print("BMI = " + str(bmi))

# Classify weight status based on BMI
    if bmi <18.5:
        print("Under Weight")
    elif 18.5<=bmi<=25.0:
        print("Normal Weight")
    else: 
        print("Over Weight")

calculate_bmi(weight=67, height=1.76)
