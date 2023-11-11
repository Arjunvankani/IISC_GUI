from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from registerWindow import RegisterWindow
import bcrypt
import style
from dataEnum import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

class LoginWindow(QDialog):
    login_successful = pyqtSignal(str)

    def __init__(self, connection, cursor):
        super().__init__()
        self.connection = connection
        self.cursor = cursor
        
        self.media_player = QMediaPlayer()
        self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile("arjun_login.mp3")))
        self.media_player.setVolume(50)  # Adjust the volume as needed
        self.media_player.play()
        
        

        self.setWindowTitle("Login Window")
        self.setWindowIcon(QIcon("icons/login.png"))
        self.setWindowFlags(self.windowFlags() & (~Qt.WindowContextHelpButtonHint))
        
        self.setGeometry(100, 150, 400+600, 300+400)
        self.setFixedSize(self.size())
        self.create_UI()

    def create_UI(self):
        self.create_widgets()
        self.create_layouts()

    def create_widgets(self):
        self.name_entry = QLineEdit()
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.Password)

        # buttons
        self.register_btn = QPushButton('New User')
        self.register_btn.setStyleSheet(style.register_btn_style())
        self.register_btn.setAutoDefault(False)
        self.register_btn.clicked.connect(self.add_user)

        self.login_btn = QPushButton('Login')
        self.login_btn.setStyleSheet(style.btn_style())
        self.login_btn.clicked.connect(self.log_into)

    def create_layouts(self):
        self.main_layout = QVBoxLayout()
        
        # Add the heading
        heading_label = QLabel('Welcome to Task Management Application', self)
        heading_font = QFont('Cursive', 16, QFont.Bold)
        heading_label.setStyleSheet('color: #996633;') 
        heading_label.setFont(heading_font)
        heading_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(heading_label)
        
        # Add the image
        image_label = QLabel(self)
        pixmap = QPixmap('task-management-process.png')  # Replace with the actual path to your image
        image_label.setPixmap(pixmap)
        self.main_layout.addWidget(image_label, alignment=Qt.AlignCenter)
        
        

        # Add the user name and password entries
        form_layout = QFormLayout()
        form_layout.addRow(QLabel("User Name: "), self.name_entry)
        
        form_layout.addRow(QLabel('Password: '), self.password_entry)

        # Add the buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.register_btn)
        button_layout.addWidget(self.login_btn)

        # Add form_layout and button_layout to main_layout
        self.main_layout.addLayout(form_layout)
        self.main_layout.addLayout(button_layout)

        self.setLayout(self.main_layout)

    def log_into(self):
        username = self.name_entry.text()
        password = self.password_entry.text()

        if username and password:
            self.confirm_data(username, password)
        else:
            QMessageBox.information(self, "Warning", 'Fields: "User name" and "Password" cannot be empty.')

    def confirm_data(self, username, password):
        users = self.get_users()
        users_name = self.get_users_name()

        if not any(username in user for user in users_name):
            QMessageBox.information(self, "Warning", 'Invalid username.')

        for user in users:
            if username == user[UserData.NAME]:
                if bcrypt.checkpw(password.encode(), user[UserData.PASSWORD]):
                    self.logged_user_id = user[UserData.ID]
                    self.login_successful.emit(username)
                    self.close()
                else:
                    QMessageBox.information(self, "Warning", 'Login failed. Invalid username or password.')

    def add_user(self):
        self.new_user = RegisterWindow(self.connection, self.cursor)

    def get_users(self):
        return self.cursor.execute("SELECT * FROM users").fetchall()

    def get_users_name(self):
        return self.cursor.execute("SELECT name FROM users").fetchall()

    def closeEvent(self, event):
        # Stop the music when the window is closed
        self.media_player.stop()
        super().closeEvent(event)