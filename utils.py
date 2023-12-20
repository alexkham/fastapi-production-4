import requests
import json
import numpy as np

# Assuming your FastAPI server is running locally on port 8000
API_URL = "http://localhost:8001/trigo/all_trigo/"

# Convert degrees to radians
def degrees_to_radians(degrees):
    return degrees * (np.pi / 180)

# Initialize an empty list to store the trigonometric values
trigonometric_table = []

# Loop through each angle from 0 to 360 degrees
for angle in range(361):
    # Call the API for each angle
    response = requests.get(f"{API_URL}{angle}/", params={"unit": "degrees"})
    if response.status_code == 200:
        data = response.json()
        # Add radians value and angle to the response data
        data["angle_degrees"] = angle
        data["angle_radians"] = degrees_to_radians(angle)
        trigonometric_table.append(data)
    else:
        print(f"Failed to get data for angle: {angle} degrees")

# Convert the list to a JSON string
json_data = json.dumps(trigonometric_table, indent=4)

# Optionally, save the JSON data to a file
with open('trigonometric_table.json', 'w') as file:
    file.write(json_data)

print("Trigonometric table generated successfully.")
