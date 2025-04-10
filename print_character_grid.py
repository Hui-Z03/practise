'''
The task is: Given a URL, there is a table of data on the webpage that includes coordinates and content.
You need to print out the content based on the coordinates to form characters (i.e., decode the hidden message).

Note:
The direction of the coordinate axes;
Blank grid coordinate points;
Avoid excessive memory usage when the table is too large.

Example table:
This is an example document showing the format of the input data for the coding assessment exercise.

x-coordinate Character y-coordinate

0 █ 0
0 █ 1
0 █ 2
1 ▀ 1
1 ▀ 2
2 ▀ 1
2 ▀ 2
3 ▀ 2

'''
import requests
from bs4 import BeautifulSoup
from itertools import groupby

def extract_table_from_google_doc(url):
    # Send an HTTP request to fetch the page content
    response = requests.get(url)
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the table in the document (Assuming it's the only table)
    table = soup.find('table')
    if not table:
        print("No table found in the document.")
        return []
    table_data = []
    
    # Loop all rows in the table, skipping the header row
    # Assuming the first row is the header
    for row in table.find_all('tr')[1:]:  # Skip the header row
        row_data = []
        # Loop through all cells in the row (td)
        for cell in row.find_all('td'):
            row_data.append(cell.get_text(strip=True))
        # Append it to the table data
        if row_data:
            table_data.append(row_data)
    # Sort table_data for printing
    sort_table_data = sorted(table_data, key=lambda x: (-int(x[2]), int(x[0])))
    # group data for grid
    grouped_data = []
    for key, group in groupby(sort_table_data, key=lambda x: x[2]):
        grouped_data.append(list(group))

    # find max_x and max_y
    max_x = 0
    max_y = 0
    for row in grouped_data:
        for coord in row:
            x, _, y = coord
            max_x = max(max_x, int(x))
            max_y = max(max_y, int(y))

    # Initialize a blank grid for printing
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Fill the grid with the content from the table
    for row in grouped_data:
        for coord in row:
            x, content, y = coord
            grid[int(y)][int(x)] = content
    
    # Print the grid
    for y in range(max_y, -1, -1):
        print(''.join(grid[y]))


# Example usage
url = " "
table_data = extract_table_from_google_doc(url)

