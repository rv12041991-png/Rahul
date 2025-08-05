from upstox_api.api import Upstox
from upstox_api.api import Session

# 🧠 Upstox credentials
api_key = '8992e97a-1ee2-4267-8ee6-224bdbf68ad5'
access_token = 'eyJ0eXAiOiJKV1QiLCJrZXlfaWQiOiJza192MS4wIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiJEQTMzNzgiLCJqdGkiOiI2ODkxZDU4ZTAyZmQwYzc0OTgxZDY0NDkiLCJpc011bHRpQ2xpZW50IjpmYWxzZSwiaXNQbHVzUGxhbiI6dHJ1ZSwiaWF0IjoxNzU0Mzg3ODU0LCJpc3MiOiJ1ZGFwaS1nYXRld2F5LXNlcnZpY2UiLCJleHAiOjE3NTQ0MzEyMDB9.rUQxhbwWV9JfMPBG5uI15H7WLryY0O78EDSAFoPnV7k'

# ✅ Setup session
session = Session(api_key)
session.set_access_token(access_token)

# ✅ Initialize Upstox client
u = Upstox(session)

# 🔍 Fetch and print user profile
profile = u.get_profile()
print("✅ Login successful!")
print("👤 Profile:", profile)
