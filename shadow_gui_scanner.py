# --------------------------------------------------
# Tool Name: Shadow-Network-Scanner (GUI)
# Created by: المبرمج الظلي (ShadowCoder)
# Description: Professional Python Network Scanner with GUI
# --------------------------------------------------

import tkinter as tk
from tkinter import messagebox
import socket
import threading

def scan_ports():
    target = ip_entry.get()
    if not target:
        messagebox.showerror("Error", "Please enter a target IP or URL!")
        return
        
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"[*] Starting Security Scan on: {target}...\n")
    result_text.insert(tk.END, "=====================================\n")
    
    def run_scanner():
        ports = [21, 22, 80, 443, 8080]
        for port in ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1.0)
            result = s.connect_ex((target, port))
            if result == 0:
                result_text.insert(tk.END, f"[+] Port {port}: OPEN 🔥\n")
            else:
                result_text.insert(tk.END, f"[-] Port {port}: Closed\n")
            s.close()
        result_text.insert(tk.END, "\n[+] Scan Finished Successfully. ✅\n")
        
    threading.Thread(target=run_scanner).start()

# --- GUI Design ---
root = tk.Tk()
root.title("Shadow Network Scanner v1.0")
root.geometry("450x550")
root.configure(bg="#1e1e1e")

title_label = tk.Label(root, text="SHADOW NETWORK SCANNER", font=("Arial", 16, "bold"), fg="#00ff00", bg="#1e1e1e")
title_label.pack(pady=15)

author_label = tk.Label(root, text="Coded by: ShadowCoder (المبرمج الظلي)", font=("Arial", 10, "italic"), fg="#aaaaaa", bg="#1e1e1e")
author_label.pack()

input_frame = tk.Frame(root, bg="#1e1e1e")
input_frame.pack(pady=20)

ip_label = tk.Label(input_frame, text="Target (IP/URL): ", font=("Arial", 11), fg="#ffffff", bg="#1e1e1e")
ip_label.pack(side=tk.LEFT, padx=5)

ip_entry = tk.Entry(input_frame, font=("Arial", 11), width=20)
ip_entry.insert(0, "127.0.0.1")
ip_entry.pack(side=tk.LEFT)

scan_button = tk.Button(root, text="Start Security Scan 🛡️", font=("Arial", 12, "bold"), fg="#ffffff", bg="#0055ff", activebackground="#0033aa", activeforeground="#ffffff", command=scan_ports)
scan_button.pack(pady=10)

result_text = tk.Text(root, font=("Consolas", 10), width=50, height=15, bg="#000000", fg="#00ff00")
result_text.pack(pady=15)
result_text.insert(tk.END, "Enter target and click 'Start Security Scan' to view results...")

root.mainloop()
