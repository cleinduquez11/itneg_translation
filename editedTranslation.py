import tkinter as tk

from tkinter import ttk
from tkinter import messagebox
from pymongo import MongoClient
from tkinter import PhotoImage


def toggle_mode():
    current_bg = root.cget("background")
    if current_bg == "white":
        root.configure(background="#333333")
        for widget in root.winfo_children():
            widget.configure(bg="#333333", fg="white")
    else:
        root.configure(background="white")
        for widget in root.winfo_children():
            widget.configure(bg="white", fg="black")



# Connect to MongoDB
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["translation_database"]
    collection = db["A. People, Social Structure, and Relations"]
    collection1 = db["B. Body Parts, Excretions, and Bodily Functions"]
    collection2 = db["C. Flora, Fauna, and Food"]
    collection3 = db["D. Nature, Climate, and Weather"]
    collection4 = db["E. Spiritual and Religious Beliefs"]
    collection5 = db["F. Parts of the House"]
    collection6 = db["G. Clothing, Weapons, and Tools"]
    collection7 = db["H. Time"]
    collection8 = db["I. Numerals"]
    print("Connected to MongoDB")
except Exception as e:
    print("Error connecting to MongoDB:", e)

# Function to search for translations in MongoDB
def search_translation():
    colengl=""
    colfil=""
    word1 = search_entry.get().split(" ")
    counter = 0
    try:

        for x in word1:
            word = x
            result = collection.find_one({"itneg_word": word})
            result1 = collection1.find_one({"itneg_word": word})
            result2 = collection2.find_one({"itneg_word": word})
            result3 = collection3.find_one({"itneg_word": word})
            result4 = collection4.find_one({"itneg_word": word})
            result5 = collection5.find_one({"itneg_word": word})
            result6 = collection6.find_one({"itneg_word": word})
            result7 = collection7.find_one({"itneg_word": word})
            result8 = collection8.find_one({"itneg_word": word})

            if result1:
                #english_translation_label.config(text="English: " + result1["english_translation"])
                #tagalog_translation_label.config(text="Tagalog: " + result1["tagalog_translation"])
                colengl = colengl + result1["english_translation"] + " "
                colfil = colfil + result1["tagalog_translation"]+ " "
                status_label.config(text="Translation found!")

            elif result:
                #english_translation_label.config(text="English: " + result["english_translation"])
                #tagalog_translation_label.config(text="Tagalog: " + result["tagalog_translation"])
                status_label.config(text="Translation found!")
                colengl = colengl + result["english_translation"] + " "
                colfil = colfil + result["tagalog_translation"]+ " "

            elif result2:
                #english_translation_label.config(text="English: " + result2["english_translation"])
                #tagalog_translation_label.config(text="Tagalog: " + result2["tagalog_translation"])
                status_label.config(text="Translation found!")
                colengl = colengl + result2["english_translation"] + " "
                colfil = colfil + result2["tagalog_translation"]+ " "

            elif result3:
                #english_translation_label.config(text="English: " + result3["english_translation"])
                #tagalog_translation_label.config(text="Tagalog: " + result3["tagalog_translation"])
                status_label.config(text="Translation found!")
                colengl = colengl + result3["english_translation"] + " "
                colfil = colfil + result3["tagalog_translation"]+ " "

            elif result4:
                #english_translation_label.config(text="English: " + result4["english_translation"])
                #tagalog_translation_label.config(text="Tagalog: " + result4["tagalog_translation"])
                status_label.config(text="Translation found!")
                colengl = colengl + result4["english_translation"] + " "
                colfil = colfil + result4["tagalog_translation"]+ " "

            elif result5:
                #english_translation_label.config(text="English: " + result5["english_translation"])
                #tagalog_translation_label.config(text="Tagalog: " + result5["tagalog_translation"])
                status_label.config(text="Translation found!")
                colengl = colengl + result5["english_translation"] + " "
                colfil = colfil + result5["tagalog_translation"]+ " "

            elif result6:
                #english_translation_label.config(text="English: " + result6["english_translation"])
                #tagalog_translation_label.config(text="Tagalog: " + result6["tagalog_translation"])
                status_label.config(text="Translation found!")
                colengl = colengl + result6["english_translation"] + " "
                colfil = colfil + result6["tagalog_translation"]+ " "

            elif result7:
                #english_translation_label.config(text="English: " + result7["english_translation"])
                #tagalog_translation_label.config(text="Tagalog: " + result7["tagalog_translation"])
                status_label.config(text="Translation found!")
                colengl = colengl + result7["english_translation"] + " "
                colfil = colfil + result7["tagalog_translation"]+ " "

            elif result8:
                #english_translation_label.config(text="English: " + result8["english_translation"])
                #tagalog_translation_label.config(text="Tagalog: " + result8["tagalog_translation"])
                status_label.config(text="Translation found!")
                colengl = colengl + result8["english_translation"] + " "
                colfil = colfil + result8["tagalog_translation"]+ " "

            else:
                english_translation_label.config(text="English: -")
                tagalog_translation_label.config(text="Tagalog: -")
                status_label.config(text="Translation not found!")



    except Exception as e:
        print("Error searching translation:", e)

    english_translation_label.config(text="English: " + colengl)
    tagalog_translation_label.config(text="Tagalog: " + colfil)

# Function to add a translation to MongoDB
def add_translation():
    try:
        itneg_word = itneg_entry.get()
        english_translation = english_entry.get()
        tagalog_translation = tagalog_entry.get()
        translation = {
            "itneg_word": itneg_word,
            "english_translation": english_translation,
            "tagalog_translation": tagalog_translation
        }

        if collection_dropdown.get() == "A. People, Social Structure, and Relations":
            collection.insert_one(translation)
        elif collection_dropdown.get() == "B. Body Parts, Excretions, and Bodily Functions":
            collection1.insert_one(translation)
        elif collection_dropdown.get() == "C. Flora, Fauna, and Food":
            collection2.insert_one(translation)
        elif collection_dropdown.get() == "D. Nature, Climate, and Weather":
            collection3.insert_one(translation)
        elif collection_dropdown.get() == "E. Spiritual and Religious Beliefs":
            collection4.insert_one(translation)
        elif collection_dropdown.get() == "F. Parts of the House":
            collection5.insert_one(translation)
        elif collection_dropdown.get() == "G. Clothing, Weapons, and Tools":
            collection6.insert_one(translation)
        elif collection_dropdown.get() == "H. Time":
            collection7.insert_one(translation)
        elif collection_dropdown.get() == "I. Numerals":
            collection8.insert_one(translation)

        status_label.config(text="Translation added successfully!")
    except Exception as e:
        print("Error adding translation:", e)

# Function to delete a translation from MongoDB
def delete_translation():
    try:
        word = search_entry.get()

        if collection_dropdown.get() == "A. People, Social Structure, and Relations":
         result = collection.delete_one({"itneg_word": word})
        elif collection_dropdown.get() == "B. Body Parts, Excretions, and Bodily Functions":
         result = collection1.delete_one({"itneg_word": word})
        elif collection_dropdown.get() == "C. Flora, Fauna, and Food":
         result = collection2.delete_one({"itneg_word": word})
        elif collection_dropdown.get() == "D. Nature, Climate, and Weather":
         result = collection3.delete_one({"itneg_word": word})
        elif collection_dropdown.get() == "E. Spiritual and Religious Beliefs":
         result = collection4.delete_one({"itneg_word": word})
        elif collection_dropdown.get() == "F. Parts of the House":
         result = collection5.delete_one({"itneg_word": word})
        elif collection_dropdown.get() == "G. Clothing, Weapons, and Tools":
         result = collection6.delete_one({"itneg_word": word})
        elif collection_dropdown.get() == "H. Time":
         result = collection7.delete_one({"itneg_word": word})
        elif collection_dropdown.get() == "I. Numerals":
         result = collection8.delete_one({"itneg_word": word})

        if result.deleted_count > 0:
            status_label.config(text="Translation deleted successfully!")
        else:
            status_label.config(text="Translation not found!")
    except Exception as e:
        print("Error deleting translation:", e)

# Function to update a translation in MongoDB
def update_translation():
    try:
        word = search_entry.get()
        english_translation = english_entry.get()
        tagalog_translation = tagalog_entry.get()

        if collection_dropdown.get() == "A. People, Social Structure, and Relations":
            result = collection.update_one(
            {"itneg_word": word},
            {"$set": {"english_translation": english_translation, "tagalog_translation": tagalog_translation}}
         )
        elif collection_dropdown.get() == "B. Body Parts, Excretions, and Bodily Functions":
            result = collection1.update_one(
                {"itneg_word": word},
                {"$set": {"english_translation": english_translation, "tagalog_translation": tagalog_translation}}
            )
        elif collection_dropdown.get() == "C. Flora, Fauna, and Food":
            result = collection2.update_one(
                {"itneg_word": word},
                {"$set": {"english_translation": english_translation, "tagalog_translation": tagalog_translation}}
            )
        elif collection_dropdown.get() == "D. Nature, Climate, and Weather":
            result = collection3.update_one(
                {"itneg_word": word},
                {"$set": {"english_translation": english_translation, "tagalog_translation": tagalog_translation}}
            )
        elif collection_dropdown.get() == "E. Spiritual and Religious Beliefs":
            result = collection4.update_one(
                {"itneg_word": word},
                {"$set": {"english_translation": english_translation, "tagalog_translation": tagalog_translation}}
            )
        elif collection_dropdown.get() == "F. Parts of the House":
            result = collection5.update_one(
                {"itneg_word": word},
                {"$set": {"english_translation": english_translation, "tagalog_translation": tagalog_translation}}
            )
        elif collection_dropdown.get() == "G. Clothing, Weapons, and Tools":
            result = collection6.update_one(
                {"itneg_word": word},
                {"$set": {"english_translation": english_translation, "tagalog_translation": tagalog_translation}}
            )
        elif collection_dropdown.get() == "H. Time":
            result = collection7.update_one(
                {"itneg_word": word},
                {"$set": {"english_translation": english_translation, "tagalog_translation": tagalog_translation}}
            )
        elif collection_dropdown.get() == "I. Numerals":
            result = collection8.update_one(
                {"itneg_word": word},
                {"$set": {"english_translation": english_translation, "tagalog_translation": tagalog_translation}}
            )

        if result.modified_count > 0:
            status_label.config(text="Translation updated successfully!")
        else:
            status_label.config(text="Translation not found!")
    except Exception as e:
        print("Error updating translation:", e)

# Create a main window
root = tk.Tk()
root.title("Translation Application")

# Background color inspired by In1digenous culture
root.configure(bg="#333333")


# Create label and entry field for search
tk.Label(root, text="Enter Itneg word:", bg="#D2B48C", font=("Lato", 12)).grid(row=0, column=0, padx=5, pady=5)
search_entry = tk.Entry(root, font=("Lato", 12))
search_entry.grid(row=0, column=1, padx=5, pady=5)


# Button to search for translation
search_button = tk.Button(root, text="Search", command=search_translation, font=("Lato", 12), bg="#4CAF50", fg="white")
search_button.grid(row=0, column=2, padx=5, pady=5)

# Labels to display translations
english_translation_label = tk.Label(root, text="English: -", bg="#D2B48C", font=("Lato", 12))
english_translation_label.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

tagalog_translation_label = tk.Label(root, text="Tagalog: -", bg="#D2B48C", font=("Lato", 12))
tagalog_translation_label.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

# Label to display status
status_label = tk.Label(root, text="", bg="#D2B48C", font=("Lato", 12))
status_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

# Labels and entry fields for adding a translation
tk.Label(root, text="Itneg word:", bg="#D2B48C", font=("Lato", 12)).grid(row=4, column=0, padx=5, pady=5)
itneg_entry = tk.Entry(root, font=("Arial", 12))
itneg_entry.grid(row=4, column=1, padx=5, pady=5)

tk.Label(root, text="English translation:", bg="#D2B48C", font=("Lato", 12)).grid(row=5, column=0, padx=5, pady=5)
english_entry = tk.Entry(root, font=("Arial", 12))
english_entry.grid(row=5, column=1, padx=5, pady=5)

tk.Label(root, text="Tagalog translation:", bg="#D2B48C", font=("Lato", 12)).grid(row=6, column=0, padx=5, pady=5)
tagalog_entry = tk.Entry(root, font=("Segoe UI", 12))
tagalog_entry.grid(row=6, column=1, padx=5, pady=5)

# Buttons for add, delete, and update functionalities
add_button = tk.Button(root, text="Add", command=add_translation, font=("Lato", 12), bg="#4CAF50", fg="white")
add_button.grid(row=7, column=0, padx=5, pady=5)

delete_button = tk.Button(root, text="Delete", command=delete_translation, font=("Lato", 12), bg="#f44336", fg="white")
delete_button.grid(row=7, column=1, padx=5, pady=5)

update_button = tk.Button(root, text="Update", command=update_translation, font=("Lato", 12), bg="#008CBA", fg="white")
update_button.grid(row=7, column=2, padx=5, pady=5)

collections = ["A. People, Social Structure, and Relations", "B. Body Parts, Excretions, and Bodily Functions",
               "C. Flora, Fauna, and Food", "D. Nature, Climate, and Weather", "E. Spiritual and Religious Beliefs",
               "F. Parts of the House", "G. Clothing, Weapons, and Tools", "H. Time", "I. Numerals"]
selected_collection = tk.StringVar(root)
selected_collection.set(collections[0])  # Default value
collection_dropdown = ttk.Combobox(root, textvariable=selected_collection, values=collections, state="readonly", font=("Arial", 12))
collection_dropdown.grid(row=3, column=4, padx=5, pady=5)

#root.title("Light and Dark Mode")

#label = tk.Label(root, text="This is a label", bg=root.cget("background"), fg=root.cget("foreground"))
#label.grid(pady=10)
button = tk.Button(root, text="Toggle Mode", command=toggle_mode)
button.grid(padx=5)

# Run the Tkinter event loop
root.mainloop()


# Print success message
print("Translations inserted successfully into the database.")
