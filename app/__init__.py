"""
App Package Initialization

This __init__.py file makes the 'app' directory a Python package.

What is a Python Package?
- A directory with an __init__.py file
- Allows importing modules from this directory
- Can contain initialization code that runs when package is imported

Example Usage:
    from app.main import app        # Import specific module
    from app import some_function   # Import from __init__.py
    import app                      # Import entire package

Package Structure Best Practices:
- Keep __init__.py minimal (often empty)
- Use it to expose commonly used functions/classes
- Document package purpose at the top

This file can be empty, but we include this docstring for educational purposes.
"""

# This file is intentionally left empty
# It exists only to make 'app' a Python package

# Advanced Usage Example (commented out):
# If you want to expose certain imports at the package level:
#
# from app.main import app
# from app.models import User, Item
#
# __all__ = ["app", "User", "Item"]
#
# Then you could do: from app import app, User, Item
# Instead of: from app.main import app

