import pandas as pd
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)
print("First five rows of the dataset!")
print(df.head())
print("\nDataset information:")
df.info()
print("\nNumber of rows and columns:")
print(df.shape)
df.to_csv("iris_output.csv", index=False)
print("The data has been successfully written to iris_output.csv")
df = pd.read_table("students.txt")   # Correct filename
print(df)
student_data = {
    "Roll-No":[101,102,103,104],
    "Name":["Anusha","Babitha","charitha","deepika"],
    "Department":["IT","IT","CSE","ECE"],
    "Percentage":[89,92,88,85]
}
df = pd.DataFrame(student_data)
df.to_csv("student_output.txt",sep = "\t",index = False)
print("Data successfully written to student_output.txt")