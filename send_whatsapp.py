import pywhatkit
import datetime
import time

print("📱 WhatsApp Message Sender using Python\n")

# 📥 Input receiver details
phone_number = input("📲 Enter recipient phone number (with country code, e.g., +91XXXXXXXXXX): ").strip()
message = input("💬 Enter your message: ").strip()

# ⏰ Automatically calculate next minute (and handle overflow)
now = datetime.datetime.now()
hour = now.hour
minute = now.minute + 1

if minute == 60:
    minute = 0
    hour = (hour + 1) % 24

# 🔔 Notify user
print(f"\n🕐 Message will be sent at {hour:02d}:{minute:02d}...")

# 📨 Send the WhatsApp message
try:
    pywhatkit.sendwhatmsg(phone_number, message, hour, minute, wait_time=10, tab_close=True)
    print("✅ WhatsApp message successfully scheduled!")
except Exception as e:
    print(f"❌ Error sending message: {e}")

# 🕒 Optional: Keep script alive to ensure delivery
time.sleep(15)
