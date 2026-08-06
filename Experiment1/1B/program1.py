import pandas as pd
student_data = {
    "Roll-No":[101,102,103,104],
    "Name":["Anusha","Babitha","charitha","deepika"],
    "Department":["IT","IT","CSE","ECE"],
    "Percentage":[89,92,88,85]
}
df = pd.DataFrame(student_data)
df.to_json(
    "students.json", orient="records", indent =4
)
print("JSON file created successfully")

#students.json is created because of the above code snippet.
