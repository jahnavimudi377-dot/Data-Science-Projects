import pandas as pd
from io import StringIO
json_data = """
[
{
"Roll-No": 101,
"Name": "Anusha",
"Percentage": 89
},
{
"Roll-No": 102,
"Name": "Babitha",
"Percentage": 92
},{
"Roll-No": 103,
"Name": "charitha",
"Percentage": 88
}
]
"""
df = pd.read_json(StringIO(json_data))
print("ParsedJSON data")
print(df)