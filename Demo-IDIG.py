from tkinter import *
from customtkinter import *
import requests
import re

root = Tk()
root.title("Instagram UID Finder")
root.geometry('600x500')
root.resizable(False, False)
root.configure(bg="#333333")

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

def click_handler():
    usernames = entry.get().split(',')  # แยกชื่อผู้ใช้ Instagram ด้วยเครื่องหมายคอมมา
    result_textbox.configure(state='normal')
    for username in usernames:
        uid = get_instagram_uid(username.strip())  # ตัดช่องว่างที่อาจมีอยู่ทั้งสองข้างของชื่อผู้ใช้ Instagram
        if uid:
            result_textbox.insert(END, f"ชื่อ: {username}\nไอดี: {uid}\n------------------------------------\n")
        else:
            result_textbox.insert(END, f"ไม่สามารถดึงข้อมูลของ {username} ได้\n------------------------------------\n")
    result_textbox.configure(state='disabled')


def clear_textbox():
    result_textbox.configure(state='normal')
    result_textbox.delete("1.0", END)
    result_textbox.configure(state='disabled')

entry = CTkEntry(master=root, placeholder_text="UserName...", width=600)
btn_submit = CTkButton(master=root, text='Submit', command=click_handler)
btn_clear = CTkButton(master=root, text='Clear', command=clear_textbox)
result_textbox = CTkTextbox(master=root, border_width=2, state="disabled")

result_label = Label(root, text="Instagram User Information:")
result_label.configure(bg="#333333", fg="white")
result_label.pack(anchor="w", padx=10, pady=(10, 0))

result_textbox.pack(fill="both", expand=True, padx=10, pady=(0, 10))
entry.pack(anchor="n", expand=True, padx=10, pady=10)
btn_submit.pack(anchor="s", expand=True, padx=1, pady=5)
btn_clear.pack(anchor="n", expand=True, padx=1, pady=5)

root.mainloop()
