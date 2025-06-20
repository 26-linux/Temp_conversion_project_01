import tkinter as tk
from tkinter import ttk, messagebox

class TemperatureConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Temperature Converter")
        self.root.geometry("500x460")
        self.root.configure(bg="#000000")  # Black background

        self.setup_ui()

    def setup_ui(self):
        # Heading
        heading = tk.Label(
            self.root, text="Temperature Converter",
            font=("Georgia", 20, "bold"), bg="#000000", fg="#FFFFFF"
        )
        heading.pack(pady=20)

        # Temperature input
        tk.Label(self.root, text="Enter Temperature Value:", font=("Georgia", 12), bg="#000000", fg="#FFFFFF").pack()
        self.temp_entry = tk.Entry(
            self.root, font=("Georgia", 13, "bold"), width=22, justify='center',
            bg="#E05CAB", fg="#000000", insertbackground="#000000"
        )
        self.temp_entry.pack(pady=10)

        # Dropdown label
        tk.Label(self.root, text="Select Unit:", font=("Georgia", 12), bg="#000000", fg="#FFFFFF").pack()

        # Dropdown styling
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TCombobox",
                        fieldbackground="#6C4CF1",
                        background="#6C4CF1",
                        foreground="#000000",
                        selectbackground="#6C4CF1",
                        selectforeground="#000000",
                        arrowcolor="#000000",
                        font=('Georgia', 12, 'bold'))

        self.unit_var = tk.StringVar()
        self.unit_dropdown = ttk.Combobox(
            self.root, textvariable=self.unit_var,
            values=["Celsius", "Fahrenheit", "Kelvin"],
            state="readonly", width=25, style="TCombobox"
        )
        self.unit_dropdown.set("Celsius")
        self.unit_dropdown.pack(pady=8)

        # Convert Button
        tk.Button(
            self.root, text="Convert",
            command=self.convert_temperature,
            font=("Georgia", 12, "bold"), bg="#6C4CF1", fg="#000000", width=16
        ).pack(pady=15)

        # Result display
        self.result_label = tk.Label(
            self.root, text="", font=("Georgia", 13, "bold"),
            bg="#E05CAB", fg="#000000", width=35, height=3, relief="groove", bd=2, justify="center"
        )
        self.result_label.pack(pady=10)

        # Reset Button
        tk.Button(
            self.root, text="Reset",
            command=self.reset,
            font=("Georgia", 11, "bold"), bg="#E05CAB", fg="#000000", width=10
        ).pack(pady=5)

        # Footer credit
        tk.Label(
            self.root, text="Designed by Sneha Karmakar", font=("Georgia", 9, "bold"),
            bg="#000000", fg="#FFFFFF"
        ).pack(side="bottom", pady=12)

    def convert_temperature(self):
        try:
            value = float(self.temp_entry.get())
            unit = self.unit_var.get()

            if unit == "Celsius":
                f = (value * 9/5) + 32
                k = value + 273.15
                result = f"Fahrenheit: {f:.2f}°F\nKelvin: {k:.2f}K"
            elif unit == "Fahrenheit":
                c = (value - 32) * 5/9
                k = c + 273.15
                result = f"Celsius: {c:.2f}°C\nKelvin: {k:.2f}K"
            elif unit == "Kelvin":
                c = value - 273.15
                f = (c * 9/5) + 32
                result = f"Celsius: {c:.2f}°C\nFahrenheit: {f:.2f}°F"
            else:
                result = "Unknown unit selected."

            self.result_label.config(text=result)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a numeric temperature.")
            self.result_label.config(text="")

    def reset(self):
        self.temp_entry.delete(0, tk.END)
        self.unit_dropdown.set("Celsius")
        self.result_label.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverterApp(root)
    root.mainloop()
