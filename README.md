# Clinical Patient BMI Analyzer (v1.0)

## 🩺 Project Overview
This Python-based diagnostic tool is designed for healthcare settings to process patient biometric data. It focuses on the "Input-Process-Output" pipeline, bridging the gap between common user measurements (Feet) and clinical metric standards (Meters/Kilograms).

## 🧬 Engineering Logic & Workflow
As a Biomedical Engineering project, the code follows a strict logical sequence to ensure data integrity:

1. **Data Acquisition:** Captures weight (kg) and height (ft) as string inputs from the clinician.
2. **Unit Normalization:** Performs a mathematical conversion of Imperial measurements (ft) into Metric standards (m) using the constant factor of `0.3048`.
3. **Data Casting:** Converts raw string data into `float` types to allow for high-precision decimal calculations.
4. **Calculations:** Applies the standard BMI formula: $BMI = weight / height^2$.
5. **Expert System Analysis:** Uses conditional logic to categorize the patient based on World Health Organization (WHO) standards.



## 🚀 Key Features
- **Smart Conversion:** Automatically handles the math required to normalize user inputs for medical formulas.
- **Clinical Precision:** Outputs results formatted to 2 decimal places, meeting standard medical reporting requirements.
- **Automated Recommendations:** Provides immediate diagnostic status and lifestyle suggestions (e.g., Underweight, Normal, Overweight, Obese).



## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Development Environment:** IDLE & Replit
- **Concepts Applied:** Casting, String Formatting, Arithmetic Operators, Conditional Logic.

## ✍️ Author
**Ejidike Michael** *Biomedical Engineering Undergraduate* *David Umahi Federal University of Health Sciences (DUFUHS)*
