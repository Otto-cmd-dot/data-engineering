## Python Best Practices for Better Code

1. Maximum line length: one line code should not longer than 79 characters.
2. Blank lines: 
    + Surround top-level function and class definitions with tw0 blank lines.
    + Use blank lines to indicate logica section
3. Implement logging 
    + Use the logging module
    + Choose the logging level wisely
    + Use timestamps when logging
    + Empty the logging bin: Use <b>RotatingFileHandler</b> classes, such as the <b>TimedRotatingFileHandler</b>, instead of FileHandler, to archive, compress, or delete old log files to prevent memory space issues. These classes will clean space once a size limit or a time condition is triggered.
4. Comment the complex code
5. Write docstring if needed
6. Use virtual environment 
7. Naming convention
