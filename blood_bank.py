# ---------------------------------------------------------
# PROJECT: BLOOD BANK INVENTORY SYSTEM
# ENGINEER: MICHAEL EJIDIKE (Biomedical Engineering Student)
# PURPOSE: A Dictionary-based system to track critical 
#          blood resources in a Trauma Center.
# FEATURES: Input Validation, Logic Checks, Critical Alerts.
# ---------------------------------------------------------

# --- CHAPTER 1: DATABASE SETUP ---
inventory = {
    "O_NEG": 5,   # Universal Donor (Critical Resource)
    "A_POS": 10,
    "AB_POS": 2,  # Starting with low stock to test alerts
    "B_NEG": 4
}

def get_int(prompt):
    """Accepts ONLY positive integers. Rejects negatives and text."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("   [!] ERROR: Value must be a positive number.")
            else:
                return value
        except ValueError:
            print("   [!] ERROR: Numbers only (e.g., 3, 5, 10).")
# --- CHAPTER 2: MAIN SYSTEM LOOP ---
while True:
    print("\n" + "="*40)
    print(" TRAUMA CENTER BLOOD BANK ")
    print("="*40)
    print("1. View Current Inventory")
    print("2. Log New Donation (Add Stock)")
    print("3. Dispatch for Surgery (Remove Stock)")
    print("4. Check Critical Levels (Warning)")
    print("5. Quit System")

    choice = input("\n>> SELECT ACTION (1-5): ")

    # --- OPTION 1: VIEW STOCK ---
    if choice == "1":
        print("\n--- CURRENT STOCK LEVELS ---")
        for b_type, count in inventory.items():
            print(f"   [{b_type}] : {count} Units")

    # --- OPTION 2: ADD DONATION ---
    elif choice == "2":
        print("\n--- LOG NEW DONATION ---")
        b_type = input("   Enter Blood Type (e.g., A_POS): ").upper()
        amount = get_int("   Units Donated: ")

        if b_type in inventory:
            inventory[b_type] += amount
            print(f"   ✅ SUCCESS: Added {amount} units to {b_type}.")
            print(f"   [NEW TOTAL]: {inventory[b_type]} Units")
        else:
            inventory[b_type] = amount
            print(f"   [NOTE] New blood type '{b_type}' added to database.")
            print(f"   ✅ SUCCESS: Added {amount} units.")

    # --- OPTION 3: DISPATCH (REMOVE) ---
    elif choice == "3":
        print("\n--- EMERGENCY DISPATCH ---")
        req_type = input("   Required Blood Type: ").upper()

        if req_type in inventory:
            amount = get_int(f"   Units needed for {req_type}: ")

            if inventory[req_type] >= amount:
                inventory[req_type] -= amount
                print(f"   🚨 DISPATCHING {amount} UNITS...")
                print(f"   [REMAINING STOCK]: {inventory[req_type]} Units")
                if inventory[req_type] < 5:
                    print(f"   ⚠️ URGENT ALERT: Stock level for {req_type} is CRITICAL!")
                    print(f"      Please restock immediately.")
            else:
                print(f"   ❌ CRITICAL ERROR: Insufficient Stock! Only {inventory[req_type]} units available.")
        else:
            print(f"   ❌ ERROR: Blood Type '{req_type}' not found in bank.")

    # --- OPTION 4: CRITICAL ALERTS ---
    elif choice == "4":
        print("\n--- CHECKING CRITICAL LEVELS ---")
        low_stock_found = False
        
        for b_type, count in inventory.items():
            if count < 5:
                print(f"   ⚠️ WARNING: [{b_type}] is LOW! (Only {count} Left)")
                low_stock_found = True
        
        if not low_stock_found:
            print("   ✅ All stock levels are healthy.")

    # --- OPTION 5: EXIT ---
    elif choice == "5":
        print("System Shutting Down...")
        break 
    
    else:
        print("   [!] Invalid Selection, Try Again.")
