# 🧬 Biomedical Engineering Python Portfolio
**Author:** Ejidike Michael | **Institution:** DUFUHS

Welcome to my coding portfolio. As a Biomedical Engineering student, I am learning Python to build tools that automate clinical diagnostics and process medical data.

---

## 📂 Project 3: Blood Bank Inventory Manager (v1.0)
**File:** `blood_bank.py`

### 🩺 Overview
A dictionary-based logistics tool designed to simulate the management of critical blood resources in a Trauma Center. It addresses the challenge of real-time inventory tracking and safety alerts during surgical dispatch.

### 🚀 Key Features
* **Data Structures:** Uses Python **Dictionaries** (`{Key: Value}`) for dynamic inventory tracking.
* **Smart Validation:** Features a custom `get_int()` shield that blocks negative numbers and invalid text inputs to prevent database corruption.
* **Active Monitoring:** Automatically triggers `⚠️ CRITICAL WARNING` alerts if specific blood types drop below safety thresholds (5 units).
* **Logic Gates:** Prevents dispatching more blood than is currently available.

---

## 📂 Project 2: Clinical Triage System (v2.0)
**File:** `clinical_triage_system.py`

### 🩺 Overview
A command-line interface (CLI) that acts as a **Continuous Vital Signs Monitor**. It runs on an infinite loop, allowing clinicians to switch between diagnostic modes without restarting.

### 🚀 Key Features
* **Event Loop:** Uses `while True` to keep the system active (Continuous Integration).
* **Complex Logic:** Detects **Hypertension (Stage 2)** using `OR` logic (Sys ≥ 140 or Dia ≥ 90).
* **Multi-Modal:** Monitors Heart Rate, Blood Pressure, and Body Temperature.
* **Safety:** Includes a safe shutdown sequence.

---

## 📂 Project 1: Patient BMI Analyzer (v1.0)
**File:** `bmi_calculator.py`

### 🩺 Overview
A diagnostic tool designed to process patient biometric data. It converts imperial measurements (feet) to metric (meters) and calculates Body Mass Index with precision.

### 🚀 Key Features
* **Unit Normalization:** Converts user inputs into standard medical units (SI).
* **Classification:** Categorizes patients based on WHO standards (Underweight, Normal, Obese).
* **Data Casting:** Handles float precision for accurate results.

---

## 🛠️ Tech Stack & Concepts Learned
* **Languages:** Python 3.x
* **Data Structures:** Dictionaries, Lists.
* **Control Flow:** While Loops, Nested If/Else statements.
* **Logic:** Boolean Gates (AND/OR), Comparators.
* **Error Handling:** Try/Except blocks for Input Sanitization.
