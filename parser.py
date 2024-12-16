import xml.etree.ElementTree as ET
import re
import csv
import pandas as pd

field = ['name']

def read_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    games = root.findall('games')
    
    regex = "\\>(.*?)\\<"
    matches = []
    # Iterate through the elements and print their tags and text
    print(len(games[0]))
    for i in range(len(games[0])):
        match = re.findall(regex, ET.tostring(games[0][i][1]).decode("utf-8"))
        matches.append(match)

    df = pd.DataFrame(matches, columns = field)
    print(df['name'])
    df.to_csv('output.csv', index=False)

# Example usage
file_path = 'test.xml'
read_xml(file_path)