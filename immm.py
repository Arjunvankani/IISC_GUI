import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap,QFont
from PyQt5.QtCore import QTimer, Qt

class ImageDisplay(QMainWindow):
    def __init__(self):
        super(ImageDisplay, self).__init__()

        self.init_ui()

    def init_ui(self):
        # Set up the main window
        self.setWindowTitle('Task Management Application')
        self.setGeometry(100, 100, 400, 300)

        # Create a central widget and layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Add a heading
        heading_label = QLabel('Welcome to Task Management Application', self)
        heading_font = QFont('Cursive', 25, QFont.Courier)  # Set the font size to 16 and make it bold
        heading_label.setFont(heading_font)
        heading_label.setAlignment(Qt.AlignCenter)
        heading_label.setStyleSheet('color: #996633;')  # #999999 corresponds to light grey

        layout.addWidget(heading_label)

        # Add an image to the layout
        image_label = QLabel(self)
        pixmap = QPixmap('task-management-process.png')  # Replace with the actual path to your image
        image_label.setPixmap(pixmap)
        layout.addWidget(image_label, alignment=Qt.AlignCenter)

        # Set up a timer to close the window after 10 seconds
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.close)
        self.timer.start(4000)  # 10 seconds in milliseconds

    def closeEvent(self, event):
        # Stop the timer when the window is closed
        self.timer.stop()
        super().closeEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageDisplay()
    window.show()
    sys.exit(app.exec_())
