import json

# Read the input JSON file
with open('bank.json', 'r') as infile:
    data = json.load(infile)

# Initialize variables
branch_list = []
pk = 1  # Starting value for primary key

# Loop over the banks and their branches to format the data
for bank_idx, bank in enumerate(data, start=1):
    for district in bank['districts']:
        for branch in district['branches']:
            branch_data = {
                "model": "seller_management.bankbranch",
                "pk": str(pk),
                "fields": {
                    "bank": str(bank_idx),  # Use bank index as the foreign key reference
                    "name": branch["branch_name"],
                    "routing_number": branch["routing_number"]
                }
            }
            branch_list.append(branch_data)
            pk += 1  # Increment the primary key for each branch

# Write the processed data to a new JSON file (bankbranch_list.json)
with open('bankbranch_list.json', 'w') as outfile:
    json.dump(branch_list, outfile, indent=4)

print("Branch data has been written to bankbranch_list.json")
