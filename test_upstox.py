from upstox_api.api import Upstox
from upstox_setup import api_key  # ⬅️ Your API Key from upstox_setup.py

# 🧠 Access token read from file
with open("access_token.txt", "r") as f:
    access_token = f.read().strip()

# ✅ Setup Upstox session
u = Upstox(api_key, access_token)
u.set_access_token(access_token)

# 📊 Fetch and print profile to test login
print("✅ Login successful! Your profile:")
print(u.get_profile())
