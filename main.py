import os
import json
from rich import print
import re

"""
This script is used to substitute the words in the raw text with the words in the json file.
The json file should be in the following format:
{
    "word1": "substitute1",
    "word2": "substitute2",
    "word3": "substitute3",
    ...
}

The script will substitute the words in the raw text with the words in the json file and save the new text in a new file.
"""

def substitute(data, raw_data):
    pattern = re.compile(r'\b(' + '|'.join(re.escape(key) for key in data) + r')\b')
    return pattern.sub(lambda x: data[x.group()], raw_data)

def get_subs(foldername: str = "subs", filename: str = "ti.json"):
    try:
        filename=os.path.join(foldername,filename)
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("[red]The file does not exist![/red]")
        data = {}
    except json.JSONDecodeError:
        print("[red]The file is not in the correct format![/red]")
        data = {}

    return data

def get_raw_data(filename: str = "raw.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        raw_data = f.read()
    return raw_data

def save_data(data, filename: str = "new.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(data)

def main():
    os.makedirs("subs", exist_ok=True)
    
    filename_local="ti.json"
    foldername_local="subs"
    data = get_subs(foldername=foldername_local, filename=filename_local)
  
    raw_data = get_raw_data()

    if not data:
        print("[red]No substitutions found![/red]")
        return
    
    if not raw_data:
        print("[red]No raw data found![/red]")
        return

    new_data = substitute(data, raw_data)

    save_data(new_data)
    print("[green]Done![/green]")


main()