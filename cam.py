import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QLabel
from PyQt5.QtMultimediaWidgets import QCameraViewfinder
from PyQt5.QtMultimedia import QCamera
from PyQt5.QtCore import Qt

class WebcamApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Webcam App")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.viewfinder = QCameraViewfinder(self)
        self.layout.addWidget(self.viewfinder)

        self.camera = QCamera()
        self.camera.setViewfinder(self.viewfinder)
        self.camera.start()

        self.capture_button = QPushButton("Capture", self)
        self.capture_button.clicked.connect(self.capture_image)
        self.layout.addWidget(self.capture_button, alignment=Qt.AlignTop)

    def capture_image(self):
        # You can capture the image here or save it to a file
        image = self.viewfinder.grab()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WebcamApp()
    window.show()
    sys.exit(app.exec_())
