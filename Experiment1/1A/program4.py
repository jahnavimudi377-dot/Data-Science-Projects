import pandas as pd
student_data = {
    "Roll-No":[101,102,103,104],
    "Name":["Anusha","Babitha","charitha","deepika"],
    "Department":["IT","IT","CSE","ECE"],
    "Percentage":[89,92,88,85]
}
df = pd.DataFrame(student_data)
df.to_csv("student_output.txt",sep = "\t",index = False)
print("Data successfully written to student_output.txt")
#student_output.txt is created because of the above code snippet.
# The data is written to a text file named "student_output.txt" with tab-separated values and without including the index column.