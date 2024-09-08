# import requests
# import argparse
# import json
# import sys

# THORN = 'þ'

# def fetch_data_from_api(page):
#     url = f"https://api.fbi.gov/wanted/v1/list?page={page}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         print(f"Error fetching data from API: {response.status_code}")
#         return None

# def parse_data(data):
#     output = []
#     for item in data['items']:
#         title = item.get('title', '')
#         subjects = ','.join(item.get('subjects', []))
#         field_offices = ','.join(item.get('field_offices') or [])
#         output.append(f"{title}{THORN}{subjects}{THORN}{field_offices}")
#     return output

# def fetch_data_from_file(filepath):
#     with open(filepath, 'r') as file:
#         data = json.load(file)
#     return data

# def main(page=None, file=None):
#     if page is not None:
#         data = fetch_data_from_api(page)
#     elif file is not None:
#         data = fetch_data_from_file(file)
#     else:
#         print("Please provide a valid page number or file.")
#         sys.exit(1)
#     if data is None:
#         print("No data to parse.")
#     elif data:
#         parsed_data = parse_data(data)
#         for row in parsed_data:
#             print(row)
    

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--page", type=int, help="Specify page number to fetch data from FBI API.")
#     parser.add_argument("--file", type=str, help="Specify the file path to read JSON data.")

#     args = parser.parse_args()

#     main(page=args.page, file=args.file)
# -*- coding: utf-8 -*-
import argparse
import requests
import json
import sys
import os

THORN = 'þ'

def fetch_data_from_api(page):
    """
    Fetch data from the FBI API for the specified page number.
    """
    url = f"https://api.fbi.gov/wanted/v1/list?page={page}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data from API: {response.status_code}")
        return None

def fetch_data_from_file(filepath):
    """
    Fetch data from a specified JSON file location.
    """

    url = f"https://api.fbi.gov/wanted/v1/list"
    response = requests.get(url)
    data = json.loads(response.content)
    if os.path.exists(filepath):
        try :
            with open(filepath, 'w') as file:
                json.dump(data["items"], file)
                
            return data
        except FileNotFoundError:
            print("File not found")
            return None
    else:
        print("File not found")
        return None

def parse_data(data):
    """
    Parse the FBI data and format it as thorn-separated values.
    """
    output = []
    for item in data.get('items', []):
        title = item.get('title', '')
        subjects = ','.join(item.get('subjects', []))
        field_offices = ','.join(item.get('field_offices') or [])
        output.append(f"{title}{THORN}{subjects}{THORN}{field_offices}")
    return output

def main(page=None, file=None):
    """
    Main function to handle both page-based API fetching and file-based input.
    """
    if page is not None:
        # Download data from the FBI API
        data = fetch_data_from_api(page)
    elif file is not None:
        # Read data from a local JSON file
        data = fetch_data_from_file(file)
    else:
        print("Please provide either a valid page number or file.")
        sys.exit(1)
    
    # Process and print thorn-separated output
    if data:
        parsed_data = parse_data(data)
        for row in parsed_data:
            print(row)
    else:
        print("No data to parse.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--page", type=int, help="Specify page number to fetch data from FBI API.")
    parser.add_argument("--file", type=str, help="Specify the file path to read JSON data.")
    
    args = parser.parse_args()

    if args.page:
        main(page=args.page)
    elif args.file:
        main(file=args.file)
    else:
        parser.print_help(sys.stderr)
