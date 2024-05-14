import requests
import re

def get_instagram_uid(username):
    url = f"https://www.instagram.com/{username}/"
    response = requests.get(url)
    
    if response.status_code == 200:
        html = response.text
        match = re.search(r'"profilePage_(\d+)"', html)
        if match:
            user_id = match.group(1)
            return user_id
        else:
            return None
    else:
        return None

# ตัวอย่างการใช้งาน
username = "apiratchayabee63327"  # แทนที่ username_here ด้วยชื่อผู้ใช้ Instagram ที่ต้องการหา UID
uid = get_instagram_uid(username)
if uid:
    print(f"User ID ของ {username} UID: {uid}")
else:
    print("ไม่สามารถดึงข้อมูลได้ โปรดตรวจสอบชื่อผู้ใช้หรือการเชื่อมต่ออินเทอร์เน็ต")
