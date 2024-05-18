import tkinter as tk
from tkhtmlview import HTMLLabel

def load_html():
    global html_label
    try:
        with open('html/index.html', 'r') as file:
            html_content = file.read()
            html_label.set_html(html_content)
    except FileNotFoundError:
        html_label.set_html("<h1>Error: HTML file not found</h1>")

root = tk.Tk()
root.title("HTML in Python GUI")

# สร้าง HTML label
html_label = HTMLLabel(root, html="")
html_label.pack(fill=tk.BOTH, expand=True)

# Load HTML content immediately
load_html()

root.mainloop()
