🧮 Calculator made by Mitsos
A simple yet functional calculator made with Python’s Tkinter library.
This desktop application features a modern UI with arithmetic operations, parentheses, and power (**) support.

🚀 Features
Clean and minimalist graphical interface using Tkinter

Supports basic arithmetic operations:

Addition (+)

Subtraction (−)

Multiplication (×)

Division (÷)

Power (**)

Parentheses for complex expressions

Responsive grid layout that adjusts to window size

Error handling for invalid inputs

🛠️ Installation & Setup
1. Clone the repository
bash
git clone https://github.com/<your-username>/calculator-tkinter.git
cd calculator-tkinter
2. Run the program
Make sure you have Python 3.x installed.

bash
python calculator.py
That’s it! The GUI window should open, ready for calculations.

💡 How It Works
The program uses a StringVar() object to manage the display text.
Each button press updates a global result string which gets evaluated when you press =.

Key functions:

press(num): Appends clicked button text to the equation.

equalpress(): Evaluates the entered expression using eval().

clear(): Resets the display.

🎨 UI Design
Background: Dark gray (#1e1e1e)

Buttons: Soft red (#ff9999) with black text

Font: Arial, clean and readable

📷 Screenshot
(Add a screenshot of your calculator GUI here)
Example:

text
![Calculator Preview](screenshot.png)
⚠️ Note
This calculator uses Python’s eval() function for simplicity.
Do not use untrusted input with it in production environments.

🧑‍💻 Author
Mitsos
Made with ❤️ using Python and Tkinter.
This project is open-source and free to use for learning and personal projects.
