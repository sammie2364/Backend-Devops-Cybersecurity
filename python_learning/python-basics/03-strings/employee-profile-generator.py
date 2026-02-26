# Employee Profile Generator
# This script demonstrates string concatenation, slicing,
# formatting, and structured output using f-strings.

# Employee basic information
first_name = 'Samuel'
last_name = 'Njenga'

# Combine first and last name
full_name = first_name + ' ' + last_name

# Address with appended apartment
address = '123 Main Street'
address += ', Apartment 4B'

# Employee details
employee_age = 21
experience_years = 5
position = 'Data Analyst'
salary = 75000

# Employee code format: DEPT-YEAR-INITIALS-ID
employee_code = 'DEV-2026-JD-001'

# Extract information from employee code
department = employee_code[0:3]
year_code = employee_code[4:8]
initials = employee_code[9:11]

# Create employee card using formatted string
employee_card = f"""
{"#"*45}
Employee Profile
{"#"*45}
Name: {full_name}
Age: {employee_age}
Address: {address}
Experience: {experience_years} years
Position: {position}
Salary: ${salary:,}
Department: {department}
Year Code: {year_code}
Initials: {initials}
{"#"*45}
"""

# Display the employee card
print(employee_card)