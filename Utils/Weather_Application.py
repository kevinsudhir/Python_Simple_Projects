# Importing functions from the tkinter 
from tkinter import * 
from tkinter import messagebox 

def display_weather() : 
	import requests, json 
	api_key = "b07a02ff7b57b9d3615e591a89f3f2af"
	base_url = "http://api.openweathermap.org/data/2.5/weather?"
	city_name = city_field.get() 
	complete_url = base_url + "q=" + city_name + "&appid=" + api_key +"&units=metric"

	clear_all(2)

	response = requests.get(complete_url) 
	x = response.json() 
	if x["cod"] != "404" : 
		y = x["main"] 
		current_temperature = y["temp"]
		current_pressure = y["pressure"] 
		current_humidiy = y["humidity"] 
		z = x["weather"] 
		weather_description = z[0]["description"] 
		temp_field.insert(15, str(current_temperature) + " Celsius") 
		atm_field.insert(10, str(current_pressure) + " hPa") 
		humid_field.insert(15, str(current_humidiy) + " %") 
		desc_field.insert(10, str(weather_description).capitalize() ) 

	else : 
		messagebox.showerror("Error", "City Not Found \n"
							"Please enter valid city name") 
		city_field.delete(0, END) 

def clear_all(ch) :
	if ch == 1 :

		city_field.delete(0, END) 
		temp_field.delete(0, END) 
		atm_field.delete(0, END) 
		humid_field.delete(0, END) 
		desc_field.delete(0, END) 
		city_field.focus_set() 

	else:
		temp_field.delete(0, END) 
		atm_field.delete(0, END) 
		humid_field.delete(0, END) 
		desc_field.delete(0, END) 
 
if __name__ == "__main__" :  
	root = Tk() 
	root.title("Weather Application") 

	# Setting the background colour of GUI window 
	root.configure(background = "black") 

	# Setting the configuration of GUI window 
	root.geometry("800x250") 

	# Creating a Weather Gui Application label 
	headlabel = Label(root, text = "Weather GUI Application", font=("Arial", 15), fg = 'white', bg = 'Black') 
	
	# Creating a City name : label 
	label1 = Label(root, text = "City name : ", font=("Arial", 11), fg = 'white', bg = 'black') 
	
	# Creating Temperature : label 
	label2 = Label(root, text = "Temperature :", font=("Arial", 11), fg = 'white', bg = 'black') 

	# Creating Atmospheric pressure : label 
	label3 = Label(root, text = "Atmospheric pressure :", font=("Arial", 11), fg = 'white', bg = 'black') 

	# Creating Humidity : label 
	label4 = Label(root, text = "Humidity :", font=("Arial", 11), fg = 'white', bg = 'black') 

	# Creating Description :label 
	label5 = Label(root, text = "Description :", font=("Arial", 11), fg = 'white', bg = 'black') 
	
	headlabel.grid(row = 0, column = 1) 
	label1.grid(row = 1, column = 0, sticky ="E") 
	label2.grid(row = 3, column = 0, sticky ="E") 
	label3.grid(row = 4, column = 0, sticky ="E") 
	label4.grid(row = 5, column = 0, sticky ="E") 
	label5.grid(row = 6, column = 0, sticky ="E") 


	city_field = Entry(root) 
	temp_field = Entry(root) 
	atm_field = Entry(root) 
	humid_field = Entry(root) 
	desc_field = Entry(root) 
 
	city_field.grid(row = 1, column = 1, ipadx ="250", ipady="3") 
	temp_field.grid(row = 3, column = 1, ipadx ="250", ipady="3") 
	atm_field.grid(row = 4, column = 1, ipadx ="250", ipady="3") 
	humid_field.grid(row = 5, column = 1, ipadx ="250", ipady="3") 
	desc_field.grid(row = 6, column = 1, ipadx ="250", ipady="3") 

	button1 = Button(root, text = "Submit", font=("Arial", 11), bg = "grey", fg = "black", command = display_weather) 

	button2 = Button(root, text = "Clear", font=("Arial", 11), bg = "grey" , fg = "black", command=lambda: clear_all(1))  
	button1.grid(row = 2, column = 1) 
	button2.grid(row = 7, column = 1) 
	
	# Starts the GUI 
	root.mainloop() 