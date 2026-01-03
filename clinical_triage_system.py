# ==============================================================================
# PROJECT: CLINICAL TRIAGE SYSTEM (v2.0)
# ENGINEER: [YOUR NAME]
# ORGANIZATION: DUFUHS Biomedical Engineering
# DESCRIPTION:
#   A Continuous Vital Signs Monitor that analyzes Heart Rate, Blood Pressure,
#   and Body Temperature using logical operators and loops.
# ==============================================================================

print("---- PATIENT TRIAGE SYSTEM ----")
print("System Initialized... Waiting for Input.")

# ------------------------------------------------------------------
# MAIN SYSTEM LOOP
# This 'while True' loop keeps the software running continuously
# until the user explicitly chooses to quit.
# ------------------------------------------------------------------
while True:
    
    # --- DISPLAY MENU OPTIONS ---
    print("\nSELECT A VITAL SIGN TO TEST: ".upper())
    print("1. Heart rate(BPM)")
    print("2. Temperature")
    print("3. Blood Pressure")
    print("Q. Quit system")
    
    # --- GET USER SELECTION ---
    # .lower() ensures that 'Q' and 'q' are treated the same way
    choice=input(">> enter selection: ").lower()

    # ==============================================================
    # OPTION 1: HEART RATE MONITOR
    # Uses simple Comparison Operators (<, >)
    # ==============================================================
    if choice=="1":
        print("\n--- heart rate monitor active ---".upper())

        # We must cast input to 'int' to perform math comparisons
        bpm_input= input("ENTER PATIENT BPM: ")
        bpm= int(bpm_input)

        # Check for Bradycardia (Too Slow)
        if bpm< 60:
            print(f"[!]alert: bradycardia detected({bpm} bpm)".upper())
            print(" >>> Check for hypothermia or medecation effect.".upper())

        # Check for Tachycardia (Too Fast)
        elif bpm> 100:
            print(f"[!]alert: tachycardia detected({bpm} bpm)".upper())
            print(" >>> check for fever, stress, or arrhythmia.".upper())
            
        # If neither alarm triggers, the patient is stable
        else :
            print(f"status: normal sinus rhythm ({bpm} bpm)".upper())
        
    # ==============================================================
    # OPTION 3: BODY TEMPERATURE
    # Uses Floats (decimals) for precision measurement
    # ==============================================================
    elif choice=="2":
        print("\n--- temperature monitor active ---".upper())

        # Using float() because temp can be 36.5 (integers would crash here)
        temp_input= input("enter body temp (°c): ".upper())
        temp= float(temp_input)

        if temp> 38.0:
            print(f"[!]alert: hyperpyrexia / high fever detected({temp}°c)".upper())
            print(" >>> recommendation: administer cooling protocol.".upper())

        elif temp< 35.0:
            print(f"[!]alert: hypothermia detected ({temp}°c)".upper())
            print(" >>> recommendation: apply warming blankets.".upper())

        else:
            print(f"status: normothermia / normal range ({temp}°c)".upper())

    # ==============================================================
    # OPTION 2: BLOOD PRESSURE MONITOR
    # Uses Logical Operators ('or', 'and') for complex checks
    # ==============================================================
    elif choice=="3":
        print("\n--- blood pressure monitor active ---".upper())

        # We need two separate inputs for Systolic (Top) and Diastolic (Bottom)
        # Using .upper() in the prompt saves the user from seeing lowercase text
        sys_input= input("enter systolic value (top#): ".upper())
        dia_input= input("enter diastolic value (bottom#): ".upper())

        sys= int(sys_input)
        dia= int(dia_input)

        # CRITICAL: LOGIC GATES
        # Hypertension: Uses 'or' because if EITHER number is high, it is dangerous.
        if sys>= 140 or dia>= 90:
            print(f"[!] CRITICAL: HYPERTENSION STAGE 2 DETECTED ({sys}/{dia} mmHg)")
            print(" >>> protocol: immediate medication review required.".upper())

        # Hypotension: Uses 'or' because low pressure in EITHER reading is bad.
        elif sys<= 90 or dia<= 60:
            print(f"[!] ALERT: HYPOTENSION DETECTED ({sys}/{dia} mmHg)")
            print(" >>> protocol: check for shock or dehydration.".upper())

        # Normal: Uses 'and' because BOTH numbers must be safe to be healthy.
        elif sys< 120 and dia< 80:
            print(f"STATUS: NORMOTENSIVE / OPTIMAL RANGE ({sys}/{dia} mmHg)")

        # Elevated: Catch-all for patients who are not critical but not perfect
        else:
            print(f"STATUS: ELEVATED / PRE-HYPERTENSION ({sys}/{dia} mmHg)")
            print(" >>> recommendation: lifestyle change advised.".upper())
            
    # ==============================================================
    # SYSTEM CONTROLS
    # ==============================================================
    elif choice=="q":
        print("\nSaving Dats... System Shutting Down".upper())
        break  # 'break' stops the loop immediately

    else :
        print("\n [!]Invalid Selection. Please Try Again.")
    
