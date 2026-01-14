# Calculator made by Mitsos

A simple GUI calculator implemented with Python's Tkinter. This program provides a basic calculator interface with digits, arithmetic operators, parentheses and exponentiation. It was created as a small desktop utility and demo of Tkinter UI building.

Features
- Basic arithmetic: +, -, *, /
- Parentheses: ( )
- Decimal numbers (.)
- Exponentiation: `**`
- Clear (`C`) and evaluate (`=`) buttons
- Simple, responsive grid layout

Requirements
- Python 3.7+ (recommended)
- Tkinter (usually included with standard Python distributions)
  - On some Linux distributions you may need to install the system package, e.g. `sudo apt install python3-tk`

Installation
1. Clone the repository or copy the script into a file, for example `calculator.py`.
2. Ensure Python and Tkinter are installed on your system.

Usage
Run the script with Python:

```bash
python3 calculator.py
```

The calculator window will open. Click the buttons to build an expression and press `=` to evaluate it. Press `C` to clear the current input.

Code overview
- The UI is built with Tkinter using a grid of Buttons.
- `equation` is a `StringVar` bound to the Entry widget used as the display.
- `press(num)` appends the pressed button text to the `result` string and updates the display.
- `clear()` empties the input.
- `equalpress()` evaluates the `result` string using Python's `eval()` and shows the result or `Error` on exception.

Security note — use of eval()
The program uses Python's built-in `eval()` to compute the entered expression. `eval()` will execute arbitrary Python code and therefore is unsafe if untrusted input is possible (for example, if you share the app or accept input from others). For local, personal use this may be acceptable, but if you plan to distribute or harden the app you should replace `eval()` with a safe expression evaluator.

Example safer alternatives:
- Use a vetted third-party evaluator such as `simpleeval`, `asteval` or `numexpr`.
- Implement a parser (e.g., Shunting-yard algorithm) to parse and evaluate only allowed operators and numbers.

Minimal example of a restricted evaluator using `ast` (illustrative; test thoroughly before use):

```python
import ast
import operator as op

# supported operators
_allowed_ops = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.USub: op.neg
}

def safe_eval(expr: str):
    """
    Evaluate a simple math expression safely using ast.
    Supports +, -, *, /, **, parentheses and floats/ints.
    """
    def _eval(node):
        if isinstance(node, ast.BinOp):
            left = _eval(node.left)
            right = _eval(node.right)
            op_type = type(node.op)
            if op_type in _allowed_ops:
                return _allowed_ops[op_type](left, right)
            raise ValueError("Unsupported operator")
        elif isinstance(node, ast.UnaryOp):
            operand = _eval(node.operand)
            op_type = type(node.op)
            if op_type in _allowed_ops:
                return _allowed_ops[op_type](operand)
            raise ValueError("Unsupported unary operator")
        elif isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.Expression):
            return _eval(node.body)
        else:
            raise ValueError("Unsupported expression")

    parsed = ast.parse(expr, mode='eval')
    return _eval(parsed)
```

You can call `safe_eval(result)` in place of `eval(result)` inside `equalpress()` to reduce risk. Note: the above is a basic example. If you need more operators or functions (sin, cos, etc.), extend the parser carefully or use a tested library.

Potential improvements
- Add keyboard input handling so users can type expressions.
- Add a history of recent calculations.
- Add scientific functions (sin, cos, log) via a safe whitelist.
- Improve styling (colors, fonts) and make window resizable-friendly.

Contributing
Contributions are welcome. Open an issue to propose changes or create a pull request with improvements. If you add functionality that extends expression parsing or evaluation, include tests and documentation explaining safety considerations.

License
Choose a license for your project (for example MIT). If you want me to add a LICENSE file here, tell me which license you prefer and I can generate it.

Contact
If you want help improving the app (making evaluation safer, adding features, packaging), tell me which area you'd like to work on and I can suggest changes or provide code.
