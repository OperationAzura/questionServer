import json
import argparse

# Define the command-line arguments
parser = argparse.ArgumentParser(description='Convert plain text file to JSON')
parser.add_argument('-i', '--input-file', help='path to the input file', required=True)
parser.add_argument('-o', '--output-file', help='path to the output file', required=True)

# Parse the command-line arguments
args = parser.parse_args()

# Read the input file and convert to a list
with open(args.input_file, 'r') as f:
    lines = f.read().splitlines()

# Write list to output file in JSON format
with open(args.output_file, 'w') as f:
    json.dump(lines, f, indent=4)
