import json

input_filename = 'list.txt'
output_filename = 'list.json'

with open(input_filename, 'r') as input_file:
    text = input_file.read()

items = []
for line in text.split('\n'):
    if line.strip() != '':
        items.append(line.strip().split('. ')[1])

json_data = json.dumps(items)

with open(output_filename, 'w') as output_file:
    output_file.write(json_data)

print(f'Successfully saved JSON data to {output_filename}')
