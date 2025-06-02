import sys
import io
import time
import requests
import pyautogui
import pyperclip

# Fix encoding to print emojis etc.
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

headers = {
    "Authorization": "Bearer ",
    "Content-Type": "application/json"
}

# Step 1: Click the icon to open chat or focus window
pyautogui.moveTo(747, 1059, duration=0.5)
pyautogui.click()
time.sleep(1)  # Wait for window to be active

# Step 2: Select the chat history text on screen (adjust coordinates as needed)
pyautogui.moveTo(918, 293, duration=1)
pyautogui.mouseDown()
pyautogui.moveTo(1792, 914, duration=1)
pyautogui.mouseUp()
time.sleep(0.5)

# Step 3: Copy selected text to clipboard
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)  # Wait for clipboard update

# Step 4: Get copied chat history
copied_text = pyperclip.paste()
print("Copied chat history:", copied_text)

# Step 5: Prepare data for chatbot API with system prompt and copied chat
data = {
    "model": "openai/gpt-3.5-turbo",
    "messages": [
        {
            "role": "system",
            "content": (
                "You are Ashi, a loving Indian girl who speaks in Hinglish. "
                "reply in a soft, casual, and short way without emojis"
                "use ehehe sometimes to look non-serious"
                "Example: 'kya hua bolo?' or 'main yahi hu, aap bolo.'"
            )
        },
        {"role": "user", "content": copied_text}
    ]
}

# Step 6: Call the chatbot API
response = requests.post("", headers=headers, json=data)
reply = response.json()["choices"][0]["message"]["content"]
print("Chatbot reply:", reply)

# Step 7: Click to the chat input box (adjust coordinates if needed)
pyautogui.click(1109, 967)
time.sleep(0.5)

# Step 8: Paste chatbot reply and send
pyperclip.copy(reply)  # Copy reply to clipboard
pyautogui.hotkey('ctrl', 'v')  # Paste
time.sleep(0.5)
pyautogui.press('enter')  # Send message
