#=======================================
#THIS IS A PATIENT CLINICAL BMI ANALYSER
# BIOMEDICAL INFORMATICS
# AUTHOR (EJIDIKE MICHAEL)
#======================================

print( "-----PATIENT CLINICAL BMI ANALYSER V(1.0)-----\n")



#INPUT/SENSOR
#We prompt the user to enter their weightin (kg)
#We prompt the user to enter their height in (m)

raw_weight=input( "PLEASE ENTER WEIGHT IN (kg): ")
raw_height=input( "PLEASE ENTER HEIGHT IN (ft e.g, 5.9):  ")



#CASTING
#We convert the string input value into float to be used for calculations


weight= float(raw_weight)
height= float(raw_height)

#CONVERSION
#We convert the value in ft into meters
height= (height*0.3048)

#CALCULATIONS
# The formula for calculating the value of bmi is (height)/(weight**)

bmi= weight/(height**2)

#OUTPUT
# The the output of the calculations are displayed to the patient
print(f"\n[ANALYSIS COMPLETE]")
print(f"\nCalculated BMI: {bmi:.2f} kg/m²\n")


#DIAGNOSTIC LOGIC
if bmi < 18.5:
    print("STATUS: UNDERWEIGHT")
    print("RECOMMENDATION: INCREASE YOUR CALORIE INTAKE")
elif 18.5<= bmi <=24.9:
  print("STATUS: NORMAL WEIGHT")
  print("RECOMMENDATION: MAINTAIN YOUR CURRENT DIET")
elif 25.0<= bmi <=29.9:
  print("STATUS: OVERWEIGHT")
  print("RECOMMENDATION: REDUCE YOUR CALORIE INTAKE")
else:
   print("STATUS: OBESE")
   print("RECOMMENDATION: CONSULT A DOCTOR")
