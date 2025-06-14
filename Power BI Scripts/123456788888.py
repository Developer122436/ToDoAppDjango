import pyautogui
import time
import os

# Updated path to Power BI Desktop executable for Power BI Desktop RS
power_bi_path = "C:\\Program Files (x86)\\Microsoft Power BI Desktop RS\\bin\\PBIDesktop.exe"

# Path to your .pbix file
pbix_file = "C:\\Users\\dimas\\OneDrive\\Desktop\\Programming\\Data Analyst\\Power BI\\My Power BI Projects\\Settlements Project\\SettlementsDev.pbix"

# Open Power BI Desktop with the file
os.startfile(power_bi_path)
time.sleep(10)  # Wait for Power BI to open

# Open file
pyautogui.hotkey('ctrl', 'o')  # Open file dialog
time.sleep(2)
pyautogui.typewrite(pbix_file)  # Type the file path
pyautogui.press('enter')
time.sleep(10)  # Wait for file to open

# Navigate to the 'Home' tab (if necessary)
pyautogui.click(801, 187)  # Coordinates of the 'Home' tab, if not already selected

# Wait for refresh to complete
time.sleep(30)


pyautogui.click(49, 113)

pyautogui.click(125, 278)


# Save and close
pyautogui.hotkey('ctrl', 's')
time.sleep(2)
pyautogui.hotkey('ctrl', 'w')
time.sleep(2)

# Close Power BI Desktop
pyautogui.hotkey('alt', 'f4')
