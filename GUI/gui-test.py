# A way to test the GUI functionalities of the options that I have selected. 

# code pulled from gemini to test and see if this works. 

import sys
# If using PyQt5, change 'PyQt6' to 'PyQt5'
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Configure window settings
        self.setWindowTitle("Object-Oriented PyQt Application")
        self.setGeometry(100, 100, 400, 200) # x, y, width, height

        # Create a widget and a layout container
        layout = QVBoxLayout()
        
        # Add a visual element (Label)
        label = QLabel("Hello! This is a clean PyQt GUI.")
        layout.addWidget(label)

        # Set the central widget of the main window
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Instantiate your custom window class
    window = MainWindow()
    window.show()
    
    # Start the application loop (use app.exec_() if using PyQt5)
    sys.exit(app.exec())


