import json
import time
import threading
# from pynput import mouse
from pynput import keyboard

import pyautogui
import pygetwindow as gw
from screeninfo import get_monitors
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

output_json_data = {}
current_step_index = 0
stop_bot_flag = False
stop_listener = threading.Event()
ignore_listener = False  # Flag to disable listener temporarily
driver = None

# Monitor that is used by pyautogui => Primary monitor
monitors = get_monitors()
primary_monitor_index = next(i for i, monitor in enumerate(monitors) if monitor.is_primary)
monitor = monitors[primary_monitor_index]

############################ Temp Performance ##############################

# Read JSON
def read_data():
    try:
        with open('input.json', 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("input.json file not found.")
        return {}
    except json.JSONDecodeError:
        print("Error decoding input.json.")
        return {}

# Write JSON
def write_data(data):
    with open('output.json', 'w') as file:
        json.dump(data, file, indent=4)

############################ Individual Bot Performance ##############################

def capture_screen():
    return pyautogui.screenshot()

def move_mouse(x, y):
    global ignore_listener
    ignore_listener = True  # Disable listener temporarily
    pyautogui.moveTo(monitor.x + x, monitor.y + y, duration=0.5)
    ignore_listener = False  # Re-enable listener

def click_mouse():
    pyautogui.click()

def enter_text(data, name):
    current_mouse_position = pyautogui.position()
    x, y = current_mouse_position
    element = {
        "value": data,
        "position": {
            "x": x,
            "y": y
        },
        "action_type": "input"
    }
    output_json_data[name] = element
    pyautogui.typewrite(data, interval=0.1)

def delete_all_text():
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')

def select_dropdown_option(dropdown_image_path, option_image_path):
    try:
        dropdown_location = list(pyautogui.locateCenterOnScreen(dropdown_image_path, confidence=0.9, grayscale=True))
        move_mouse(dropdown_location[0], dropdown_location[1])
        time.sleep(1)
        click_mouse()
        time.sleep(1)
        option_location = list(pyautogui.locateCenterOnScreen(option_image_path, confidence=0.9, grayscale=True))
        move_mouse(option_location[0], option_location[1])
        time.sleep(1)
        click_mouse()
        time.sleep(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

############################ Bot Workflow ##############################

def perform(type):
    global current_step_index
    data = read_data()
    if type == 'workflow':
        workflow_data = data.get('workflow', [])
        while current_step_index < len(workflow_data):
            item = workflow_data[current_step_index]
            if stop_bot_flag:
                return
            if item['action'] == 'input':
                move_mouse(item['parameters']['x'], item['parameters']['y'])
                time.sleep(1)
                click_mouse()
                time.sleep(1)
                delete_all_text()
                time.sleep(1)
                enter_text(item['description'], item['name'])
            elif item['action'] == 'click':
                move_mouse(item['parameters']['x'], item['parameters']['y'])
                time.sleep(1)
                click_mouse()
            elif item['action'] == 'select':
                select_dropdown_option(item['parameters']['dropdown'], item['parameters']['option'])
            elif item['action'] == 'delay':
                time.sleep(item['time'])
            current_step_index += 1

############################# Total Workflow #############################
def open_chrome():
    global driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(), options=chrome_options)
    chrome_window = gw.getWindowsWithTitle('Chrome')[0]
    chrome_window.moveTo(monitor.x, monitor.y)
    driver.get('https://stage-api.stage-easymerchant.io/js-sdk')
    time.sleep(3)

def close_chrome():
    global driver
    driver.quit()

############################# Keyboard Event #############################

def on_activate():
    global stop_bot_flag
    stop_bot_flag = True

def main():
    hotkey_listener = keyboard.GlobalHotKeys({
        '<alt>+x': on_activate
    })
    hotkey_listener.start()

    open_chrome()
    perform('workflow')
    close_chrome()
    write_data(output_json_data)

if __name__ == "__main__":
    main()