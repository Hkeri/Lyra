from datetime import datetime
import customtkinter
import random
import warnings
import customtkinter


def destroy():
    root.destroy()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
warnings.filterwarnings("ignore")
root = customtkinter.CTk()
customtkinter.set_widget_scaling(0.80)
customtkinter.set_window_scaling(1)
root.attributes('-alpha', 0.935)
root.resizable(False, False)

root.title("Lyra")

# Center the window
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
window_width = 950
window_height = 500
x = (width // 2) - (window_width // 2)
y = (height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

my_font = customtkinter.CTkFont(family="Consolas", size=25, slant="italic")
my_font_for_buttons = customtkinter.CTkFont(family="Consolas", size=15)
my_font_for_buttons_2 = customtkinter.CTkFont(family="Consolas", size=13)

def change():
    global mode
    if mode == "dark":
        customtkinter.set_appearance_mode("light")
        mode = "light"
    else:
        customtkinter.set_appearance_mode("dark")
        mode = "dark"

mode = "dark"

quotes = [
    '"Love what you do."',
    '"Believe in yourself."',
    '"Create your own future."',
    '"Never give up."',
]

def c_time():
    string = datetime.now().strftime("%H:%M:%S")
    time_label.configure(text=string)
    time_label.after(1000, c_time)

def date():
    string = datetime.now().strftime("%d/%m/%Y")
    date_label.configure(text=string)
    date_label.after(1000, date)

def C_Day():
    day = datetime.today().weekday() + 1
    Day_dict = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }
    return Day_dict.get(day, "")

def Temp(city1):
    import requests
    import json

    api_key = "57750a40690b5a50f53cc755c386cfbc"  # Replace with your actual OpenWeatherMap API key
    endpoint = "http://api.openweathermap.org/data/2.5/weather"

    # send GET request to API endpoint
    response = requests.get(
        endpoint, params={"q": city1, "appid": api_key, "units": "metric"}
    )

    # check if the request was successful
    if response.status_code == 200:
        # parse JSON response
        data = json.loads(response.text)

        # check if 'main' key is present
        if "main" in data:
            # extract temperature in Celsius
            temperature_celsius = data["main"]["temp"]
            return temperature_celsius
        else:
            print("Error: 'main' key not found in API response")
    else:
        print(
            f"Error: Failed to fetch data from API. \nStatus code: {response.status_code}"
        )
    IP = requests.get("https://api.ipify.org").text
    url = "https://get.geojs.io/v1/ip/geo/" + IP + ".json"
    geo_reqeust = requests.get(url)
    geo_data = geo_reqeust.json()
    city = geo_data["city"]

    city = city
    return None

# Centered widgets
lyra_label = customtkinter.CTkLabel(
    root, text="lyra", font=("Ankh Sanctuary", 165), text_color="#41FDFE"
)
lyra_label.place(relx=0.5, rely=0.15, anchor="center")

quote_label = customtkinter.CTkLabel(
    root, text=f"{random.choice(quotes)}", font=my_font
)
quote_label.place(relx=0.5, rely=0.3, anchor="center")

time_label = customtkinter.CTkLabel(root, text="", font=("Consolas", 45))
time_label.place(relx=0.9, rely=0.1, anchor="center")  # Adjusted placement
c_time()

date_label = customtkinter.CTkLabel(root, text="", font=("Consolas", 30))
date_label.place(relx=0.9, rely=0.175, anchor="center")
date()

day_label = customtkinter.CTkLabel(root, text=C_Day(), font=("Consolas", 25))
day_label.place(relx=0.9, rely=0.25, anchor="center")

input_box = customtkinter.CTkEntry(
    root,
    width=420,
    height=75,
    placeholder_text="Type Your Question",
    font=("Consolas", 20),
    corner_radius=50,
)
input_box.place(relx=0.5, rely=0.50, anchor="center")

send_button = customtkinter.CTkButton(
    root,
    text="➤",
    text_color="white",
    corner_radius=50,
    width=35,
    height=45,
    font=("Consolas", 25),
    fg_color="transparent",
    border_width=1,
)
send_button.place(relx=0.715, rely=0.50, anchor="center")

change_mode_button = customtkinter.CTkButton(
    root,
    text="Change Light/Dark",
    command=change,
    corner_radius=50,
    font=my_font_for_buttons_2,
    fg_color="transparent",
    border_width=1,
)
change_mode_button.place(relx=0.075, rely=0.950, anchor="center")

exit_button = customtkinter.CTkButton(
    root,
    text="Exit",
    command=destroy,
    corner_radius=50,
    font=my_font_for_buttons_2,
    fg_color="transparent",
    border_width=1,
    hover_color="red",
)
exit_button.place(relx=0.925, rely=0.950, anchor="center")

feedback_textbox = customtkinter.CTkTextbox(
    root,
    width=325,
    height=325,
    font=("Consolas", 15),
    corner_radius=50
)
feedback_textbox.place(relx=0.15725, rely=0.32575, anchor="center")


if __name__ == "__main__":
    # Initialize the main loop
    root.mainloop()
