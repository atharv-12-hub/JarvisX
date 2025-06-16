def execute_command(command):
    import os
    import pyautogui

    if "volume up" in command:
        pyautogui.press("volumeup")
        return "Volume increased"
    elif "volume down" in command:
        pyautogui.press("volumedown")
        return "Volume decreased"
    elif "mute" in command:
        pyautogui.press("volumemute")
        return "Volume muted"
    elif "open notepad" in command:
        os.system("notepad")
        return "Opening Notepad"
    else:
        return "System command not recognized"
