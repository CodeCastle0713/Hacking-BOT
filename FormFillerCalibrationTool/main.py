import tkinter as tk
import pyautogui
import json
import pygetwindow as gw
from screeninfo import get_monitors
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pynput import keyboard

index = 0
can_get_position = True
monitors = get_monitors()
primary_monitor_index = next(i for i, monitor in enumerate(monitors) if monitor.is_primary)
monitor = monitors[primary_monitor_index]

with open('default.json', 'r') as file:
    data = json.load(file)
guide_flow = data['workflow']

def get_mouse_position():
    if can_get_position:
        x, y = pyautogui.position()
        guide_flow[index]['parameters']['x'] = x
        guide_flow[index]['parameters']['y'] = y
        position_label.config(text=f"(X , Y) : ({x} , {y})")

def previous():
    global index, can_get_position
    next_button.config(state=tk.NORMAL)
    if index >= 1:
        index -= 1
    if index == 0:
        previous_button.config(state=tk.DISABLED)
    if guide_flow[index]['action'] == 'select' or guide_flow[index]['action'] == 'delay':
        can_get_position = False
        comment_label.config(text=f"This is <{guide_flow[index]['comment']}> select field. Just click <Next> Button.")
        position_label.config(text=f"")
    else:
        can_get_position = True
        comment_label.config(text=f"Get the position of <"+guide_flow[index]['comment']+"> field.")
        position_label.config(text=f"(X , Y) : ({guide_flow[index]['parameters']['x']} , {guide_flow[index]['parameters']['y']})")

def next():
    global index, can_get_position
    previous_button.config(state=tk.NORMAL)
    if index <= len(guide_flow) - 2:
        index += 1
    if index == len(guide_flow) - 1:
        next_button.config(state=tk.DISABLED)
    if guide_flow[index]['action'] == 'select' or guide_flow[index]['action'] == 'delay':
        can_get_position = False
        comment_label.config(text=f"This is <{guide_flow[index]['comment']}> select field. Just click <Next> Button.")
        position_label.config(text=f"")
    else:
        can_get_position = True
        comment_label.config(text=f"Get the position of <"+guide_flow[index]['comment']+"> field.")
        position_label.config(text=f"(X , Y) : ({guide_flow[index]['parameters']['x']} , {guide_flow[index]['parameters']['y']})")

def output():
    element = {
        "workflow": guide_flow
    }
    with open('input.json', 'w') as json_file:
        json.dump(element, json_file, indent=4)
    print(f"Outputted JSON successfully")

def show_main_window():
    alert.destroy()
    root.deiconify()

def on_close():
    driver.quit()
    root.destroy()

def on_activate():
    get_mouse_position()

# Set up the hotkey listener using pynput
hotkey_listener = keyboard.GlobalHotKeys({
    '<alt>+x': on_activate
})
hotkey_listener.start()

global driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(), options=chrome_options)
chrome_window = gw.getWindowsWithTitle('Chrome')[0]
chrome_window.moveTo(monitor.x, monitor.y)
driver.get('https://stage-api.stage-easymerchant.io/js-sdk')

root = tk.Tk()
root.title("Mouse Position Tracker")
root.attributes('-topmost', True)
root.geometry("450x200")
root.withdraw()  # Hide the main window initially
root.protocol("WM_DELETE_WINDOW", on_close)

alert = tk.Toplevel(root)
alert.title("Alert")
alert.geometry("500x100")
alert.attributes('-topmost', True)

alert_label = tk.Label(alert, text="Keep your target application on primary monitor...", font=('Helvetica', 12))
alert_label.pack(expand=True)

# Show the main window after 5 seconds
root.after(3000, show_main_window)

comment_label = tk.Label(root, text="Get the position of <"+guide_flow[0]['comment']+"> field.")
comment_label.pack(pady=10)

position_label = tk.Label(root, text="(X , Y) : (? , ?)")
position_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

previous_button = tk.Button(button_frame, text="Previous", command=previous)
next_button = tk.Button(button_frame, text="Next", command=next)

previous_button.config(state=tk.DISABLED)
previous_button.pack(side=tk.LEFT, padx=5)
next_button.pack(side=tk.LEFT, padx=5)

output_button = tk.Button(root, text="Output JSON", command=output)
output_button.pack(pady=10)

root.mainloop()
