#NASA API POTD Code
#Written by AutomatedRouting
#Date May 26, 2021

import requests
import json

#NASA's Picture of the Day
POTD = "https://api.nasa.gov/planetary/apod"
api_key = "api_key=REMOVED!!!"

#Create a websession and authenticate with NASA.
#This return raw JSON and not an image.
try:

	potd_request = requests.get(f"{POTD}?{api_key}")
	potd_request.raise_for_status() #Error Handling (optional)

	print(f"Successfully Authenticated with NASA and retreived data.")

except requests.exceptions.HTTPError as auth_error:

    print(f"{auth_error}") #403 Client Error: Forbidden for url
    SystemExit()

#Safe method as only local, no need for try.
nasa_json = json.loads(potd_request.text)
print(f"{json.dumps(nasa_json, indent=4)}")

for key, value in nasa_json.items():
	if key == "hdurl":
		image_url = value
		image_name = image_url.split('/')[-1]

#Downloads the actual image file returned by the JSON above.
try:
	with open(f'./{image_name}', 'wb') as image_file:
		print(f"Downloading Image...")
		request_image = requests.get(f"{image_url}")
		image_file.write(request_image.content)

	print(f"Saved as {image_name}.")

except requests.exceptions.HTTPError as image_dl_error:
	print(f"{image_dl_error}")
	SystemExit()
