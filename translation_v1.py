import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
def search_translation():
    # Implement the search translation functionality
    pass

def add_translation():
    # Implement the add translation functionality
    pass

def delete_translation():
    # Implement the delete translation functionality
    pass

def update_translation():
    # Implement the update translation functionality
    pass

def toggle_mode():
    # Implement the toggle mode functionality
    pass

def show_user_page():
    clear_frame()
    create_search_ui()

def show_admin_page():
    clear_frame()
    # create_search_ui()
    create_admin_ui()

def create_search_ui():
    tk.Label(root, text="Enter Itneg word:", bg="#D2B48C", font=("Lato", 12)).grid(row=0, column=0, padx=5, pady=5)
    search_entry = tk.Entry(root, font=("Lato", 12))
    search_entry.grid(row=0, column=1, padx=5, pady=5)

    search_button = tk.Button(root, text="Search", command=search_translation, font=("Lato", 12), bg="#4CAF50", fg="white")
    search_button.grid(row=0, column=2, padx=5, pady=5)

    english_translation_label = tk.Label(root, text="English: -", bg="#D2B48C", font=("Lato", 12))
    english_translation_label.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

    tagalog_translation_label = tk.Label(root, text="Tagalog: -", bg="#D2B48C", font=("Lato", 12))
    tagalog_translation_label.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

    status_label = tk.Label(root, text="", bg="#D2B48C", font=("Lato", 12))
    status_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

def create_admin_ui():
    tk.Label(root, text="Itneg word:", bg="#D2B48C", font=("Lato", 12)).grid(row=4, column=0, padx=5, pady=5)
    itneg_entry = tk.Entry(root, font=("Arial", 12))
    itneg_entry.grid(row=4, column=1, padx=5, pady=5)

    tk.Label(root, text="English translation:", bg="#D2B48C", font=("Lato", 12)).grid(row=5, column=0, padx=5, pady=5)
    english_entry = tk.Entry(root, font=("Arial", 12))
    english_entry.grid(row=5, column=1, padx=5, pady=5)

    tk.Label(root, text="Tagalog translation:", bg="#D2B48C", font=("Lato", 12)).grid(row=6, column=0, padx=5, pady=5)
    tagalog_entry = tk.Entry(root, font=("Segoe UI", 12))
    tagalog_entry.grid(row=6, column=1, padx=5, pady=5)

    add_button = tk.Button(root, text="Add", command=add_translation, font=("Lato", 12), bg="#4CAF50", fg="white")
    add_button.grid(row=7, column=0, padx=5, pady=5)

    delete_button = tk.Button(root, text="Delete", command=delete_translation, font=("Lato", 12), bg="#f44336", fg="white")
    delete_button.grid(row=7, column=1, padx=5, pady=5)

    update_button = tk.Button(root, text="Update", command=update_translation, font=("Lato", 12), bg="#008CBA", fg="white")
    update_button.grid(row=7, column=2, padx=5, pady=5)

def clear_frame():
    for widget in root.winfo_children():
        widget.destroy()

def create_landing_page():
    tk.Button(root, text="User", command=show_user_page, font=("Lato", 14), bg="#4CAF50", fg="white").pack(pady=20)
    tk.Button(root, text="Admin", command=show_admin_page, font=("Lato", 14), bg="#008CBA", fg="white").pack(pady=20)

# Create the main window
root = tk.Tk()
root.title("Translation Application")
root.geometry("600x400")
root.resizable(False, False) 

# Set background image
# background_image = tk.PhotoImage(Image.open("chess_1.jpg"))  # Make sure to replace with the actual path to your image
# background_label = tk.Label(root, image=background_image)
# background_label.place(relwidth=1, relheight=1)

# Create the landing page
create_landing_page()

# Run the Tkinter event loop
root.mainloop()




