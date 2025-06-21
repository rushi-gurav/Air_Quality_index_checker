import requests
from tkinter import *

def get_air_quality():
	city_name = ent_city.get()
	api_token = "#"  
	url = f"https://api.waqi.info/feed/{city_name}/?token={api_token}"
    
	try:
		response = requests.get(url)
		data = response.json()

		if data.get("status") == "ok":
			aqi = data["data"]["aqi"]             
			if 0 <= aqi <= 50:
				quality = "Good"
			elif 51 <= aqi <= 100:
				quality = "Moderate"
			elif 101 <= aqi <= 150:
				quality = "Unhealthy for Sensitive Groups"
			elif 151 <= aqi <= 200:
				quality = "Unhealthy"
			elif 201 <= aqi <= 300:
				quality = "Very Unhealthy"
			else:
				quality = "Hazardous"
			
			result_label.config(text=f"City: {city_name}\nAQI: {aqi} => {quality}", font=("Arial", 16, "bold"))
		else:
			result_label.config(text="Error: City not found or invalid API token.", font=("Arial", 16, "bold"))
	
	except Exception as e:
		result_label.config(text=f"An error occurred: {e}", font=("Arial", 16, "bold"))

	ent_city.delete(0, END)

root = Tk()
root.title("Air Quality Index Checker")
root.geometry("700x400+300+100")
f = ("Arial", 20, "bold")

lab_header = Label(root, text="Air Quality Index Checker by Rushi", font=f)
lab_header.place(x=160, y=20)

lab_city = Label(root, text="Enter City Name:", font=f)
ent_city = Entry(root, font=f)
lab_city.place(x=50, y=100)
ent_city.place(x=300, y=100)
ent_city.delete(0, END)

button_generate = Button(root, text="Find AQI", font=f, command=get_air_quality)
button_generate.place(x=220, y=200)

result_label = Label(root, text="", font=("Arial", 16, "bold"), wraplength=400, justify="center")
result_label.place(x=200, y=260)

root.mainloop()
