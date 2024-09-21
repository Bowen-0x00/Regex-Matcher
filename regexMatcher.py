import tkinter as tk
from tkinter import messagebox
import re

def match_regex():
    text = text_entry.get("1.0", tk.END).strip()
    pattern = regex_entry.get().strip()
    
    try:
        compiled_pattern = re.compile(pattern)
    except re.error:
        messagebox.showerror("Invalid Regex", "The provided regular expression is not valid.")
        return
    
    matches = compiled_pattern.findall(text)
    result_entry.delete("1.0", tk.END)
    result_entry.insert(tk.END, "\n".join(matches) if matches else "No matches found")

def non_match_regex():
    text = text_entry.get("1.0", tk.END).strip()
    pattern = regex_entry.get().strip()
    
    try:
        compiled_pattern = re.compile(pattern)
    except re.error:
        messagebox.showerror("Invalid Regex", "The provided regular expression is not valid.")
        return
    
    matches = compiled_pattern.findall(text)
    non_matches = [line for line in text.splitlines() if not compiled_pattern.search(line)]
    result_entry.delete("1.0", tk.END)
    result_entry.insert(tk.END, "\n".join(non_matches) if non_matches else "All lines match")

def format_match():
    text = text_entry.get("1.0", tk.END).strip()
    pattern = regex_entry.get().strip()
    format_string = format_entry.get().strip()
    
    try:
        compiled_pattern = re.compile(pattern)
    except re.error:
        messagebox.showerror("Invalid Regex", "The provided regular expression is not valid.")
        return
    
    def replace(match):
        result = format_string
        for i in range(1, len(match.groups()) + 1):
            result = result.replace(f"${i}", match.group(i))
        return result

    matches = compiled_pattern.finditer(text)
    formatted_results = [replace(match) for match in matches]
    
    result_entry.delete("1.0", tk.END)
    result_entry.insert(tk.END, "\n".join(formatted_results) if formatted_results else "No matches found")

def count_matches():
    text = text_entry.get("1.0", tk.END).strip()
    pattern = regex_entry.get().strip()
    
    try:
        compiled_pattern = re.compile(pattern)
    except re.error:
        messagebox.showerror("Invalid Regex", "The provided regular expression is not valid.")
        return
    
    matches = compiled_pattern.findall(text)
    count = len(matches)
    result_entry.delete("1.0", tk.END)
    result_entry.insert(tk.END, f"Number of matches: {count}")

# Create the main window
root = tk.Tk()
root.title("Regex Matcher")

# Configure the grid
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_rowconfigure(7, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)  # Add an extra column for the new button

# Create and place the text entry box
tk.Label(root, text="Input Text:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
text_entry = tk.Text(root, height=10, width=50)
text_entry.grid(row=1, column=0, columnspan=4, padx=10, pady=5, sticky="nsew")

# Create and place the regex entry box
tk.Label(root, text="Regex Pattern:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
regex_entry = tk.Entry(root, width=50)
regex_entry.grid(row=3, column=0, columnspan=4, padx=10, pady=5, sticky="nsew")

# Create and place the format entry box
tk.Label(root, text="Format String:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
format_entry = tk.Entry(root, width=50)
format_entry.grid(row=5, column=0, columnspan=4, padx=10, pady=5, sticky="nsew")

# Create and place the result entry box
tk.Label(root, text="Result:").grid(row=6, column=0, padx=10, pady=5, sticky="w")
result_entry = tk.Text(root, height=10, width=50)
result_entry.grid(row=7, column=0, columnspan=4, padx=10, pady=5, sticky="nsew")

# Create and place the buttons
match_button = tk.Button(root, text="Show Matches", command=match_regex)
match_button.grid(row=8, column=0, padx=10, pady=10, sticky="ew")

non_match_button = tk.Button(root, text="Show Non-Matches", command=non_match_regex)
non_match_button.grid(row=8, column=1, padx=10, pady=10, sticky="ew")

format_button = tk.Button(root, text="Format Matches", command=format_match)
format_button.grid(row=8, column=2, padx=10, pady=10, sticky="ew")

count_button = tk.Button(root, text="Count Matches", command=count_matches)
count_button.grid(row=8, column=3, padx=10, pady=10, sticky="ew")

# Start the main event loop
root.mainloop()
