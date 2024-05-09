import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Convert JSON string to Python dictionary
sample_dict = json.loads(sampleJson)

salary = sample_dict['company']['employee']['payable']['salary']
print("Salary:", salary)

sample_dict['company']['employee']['birth_date'] = "1990-01-01"

# Convert the modified dictionary back to JSON string
modified_json = json.dumps(sample_dict, indent=4)

with open("modified_data.json", "w") as f:
    f.write(modified_json)
