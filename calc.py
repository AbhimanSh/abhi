import tkinter as tk
from tkinter import messagebox
import re

# Function to check password strength
def check_password_strength(password):
    score = 0
    suggestions = []

    # Password checks
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Increase the length to at least 8 characters.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one digit.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Include at least one special character (e.g., !, @, #).")  

    if len(set(password)) >= len(password) - 2:
        score += 1
    else:
        suggestions.append("Avoid repeated characters.")

    return score, suggestions

# GUI Application
def password_checker_gui():
    def check_password():
        password = password_entry.get()
        if not password:
            messagebox.showerror("Error", "Please enter a password!")
            return

        score, suggestions = check_password_strength(password)

        # Update results
        score_label.config(text=f"Score: {score}/6")
        feedback_label.config(
            text=("Strong" if score == 6 else "Fair" if score >= 4 else "Weak"),
            fg=("green" if score == 6 else "orange" if score >= 4 else "red")
        )

        suggestions_text.delete("1.0", tk.END)
        suggestions_text.insert(tk.END, "\n".join(suggestions) if suggestions else "No suggestions! Your password is excellent.")

    # Create main window
    root = tk.Tk()
    root.title("Password Checker")
    root.geometry("300x300")

    # Widgets
    tk.Label(root, text="Enter Password:").pack(pady=5)
    password_entry = tk.Entry(root, show="*", width=25)
    password_entry.pack(pady=5)
    
    tk.Button(root, text="Check", command=check_password).pack(pady=10)

    score_label = tk.Label(root, text="")
    score_label.pack(pady=5)

    feedback_label = tk.Label(root, text="")
    feedback_label.pack(pady=5)

    suggestions_text = tk.Text(root, height=6, width=35)
    suggestions_text.pack(pady=5)

    root.mainloop()

# Run the app
if __name__ == "__main__":
    password_checker_gui()
