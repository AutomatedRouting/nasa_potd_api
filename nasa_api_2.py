import requests, json

POTD = "https://api.nasa.gov/planetary/apod"
api_key = "api_key=REMOVED!!!"

potd_request = requests.get(f"{POTD}?{api_key}")
nasa_json = json.loads(potd_request.text)

for key, value in nasa_json.items():
	if key == "hdurl":
		image_url = value
		image_name = image_url.split('/')[-1]

with open(f'./{image_name}', 'wb') as image_file:
	request_image = requests.get(f"{image_url}")
	image_file.write(request_image.content)
print('done.')
