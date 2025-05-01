import tkinter as tk
from tkinter import messagebox

def main():
    print ('starting\n\n')
    # Create the main window
    root = tk.Tk()
    root.title("File Not Found Error")
    root.geometry("300x200")

    # Create a label and pack it into the window
    label = tk.Label(root, text="Check the console for output.")
    label.pack(pady=20)

    # Start the Tkinter event loop
    root.mainloop()

    # Attempt to open and read the file
    try:
        with open("input.csv", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        
        tk.Tk()
        root.withdraw()  # Hide the main window
        messagebox.showerror("Error", "input.csv not found.")
        root.destroy()


if __name__ == "__main__":
    main()
    

    
    
        