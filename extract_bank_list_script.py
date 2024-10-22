import json

# Step 1: Read the input JSON file
with open('bank.json', 'r') as f:
    data = json.load(f)

# Step 2: Process the data to extract bank names in the desired format


def process_bank_names(data):
    processed_data = []
    bank_id = 1

    for bank in data:
        processed_bank = {
            "model": "seller_management.bank",
            "id": bank_id,
            "fields": {
                "name": bank['name']
            }
        }
        processed_data.append(processed_bank)
        bank_id += 1

    return processed_data


# Step 3: Process the data to extract bank names
processed_data = process_bank_names(data)

# Step 4: Write the processed data to a new JSON file (bank_list.json)
with open('bank_list.json', 'w') as outfile:
    json.dump(processed_data, outfile, indent=4)

print("Processed data has been written to bank_list.json")
