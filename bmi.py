def calculate_bmi(height,weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

#code to calc bmi
    bmi = weight/(height*height)
    print("BMI = " + str(bmi))

# Classify weight status based on BMI
    if bmi <18.5:
        print("Under Weight")
        return -1

    elif 18.5<=bmi<=25.0:
        print("Normal Weight")
        return 0
    else: 
        print("Over Weight")
        return 1

calculate_bmi(weight=67, height=1.76)

