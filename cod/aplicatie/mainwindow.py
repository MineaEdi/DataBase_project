# This Python file uses the following encoding: utf-8
import datetime
import hashlib
import sqlite3
import sys
import random

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QListWidgetItem

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.current_user_id = None  # initializam user-ul curent cand se porneste aplicatia

        self.ui.pushButton_5.clicked.connect(self.Autentificare)
        self.ui.pushButton_6.clicked.connect(self.new_user)
        self.ui.pushButton_9.clicked.connect(self.Inregistrare)
        self.ui.pushButton_10.clicked.connect(self.returnToLoginPage)
        self.ui.pushButton_3.clicked.connect(self.LogOut)
        self.ui.pushButton_4.clicked.connect(self.myReservationsButtonClicked)
        self.ui.pushButton_8.clicked.connect(self.returnToTablePage)
        self.ui.pushButton.clicked.connect(self.reservationButtonClicked)
        self.ui.pushButton_2.clicked.connect(self.checkingButtonClicked)
        self.ui.pushButton_7.clicked.connect(self.undoReservation)


    def Autentificare(self):
        connection = sqlite3.connect("cruise.db")
        cursor = connection.cursor()

        username = self.ui.lineEdit_3.text()

        # Hash the entered password
        hashed_password = self.hash_password(self.ui.lineEdit_4.text())

        # Check if the user is registered and if the password is correct
        login_result = self.is_valid_login(username, hashed_password)

        if login_result == "success":
            # Successful login, set the current_user_id
            self.current_user_id = self.get_user_id(username)
            # Switch to the next window
            self.ui.stackedWidget.setCurrentIndex(0)
            # Display current user
            sql_query = "SELECT d.nume, d.prenume FROM user_detail d, users u WHERE d.id = u.id AND u.username = ?"
            cursor.execute(sql_query, (username,))  # Substituiți self.username cu numele utilizatorului curent

            # Obțineți rezultatele interogării
            result = cursor.fetchone()

            # Verificați dacă ați găsit un rezultat
            if result:
                # Extrageți numele și prenumele din rezultat
                nume, prenume = result

                # Construiți un șir pentru afișare
                display_text = f"{prenume} {nume}"

                # Setați textul în QTextBrowser
                self.ui.textBrowser.setText(display_text)
            else:
                # Dacă nu ați găsit un rezultat, afișați un mesaj corespunzător în QTextBrowser
                self.ui.textBrowser.setText("Numele și prenumele nu au fost găsite.")
        elif login_result == "user_not_found":
            # Username not recognized, show a pop-up message
            QMessageBox.warning(self, "Login Failed", "Invalid username. Please register.")
        elif login_result == "incorrect_password":
            # Incorrect password, show a pop-up message
            QMessageBox.warning(self, "Login Failed", "Incorrect password. Please try again.")
        elif login_result == "not_registered":
            # User is not registered, show a pop-up message
            QMessageBox.warning(self, "Login Failed", "You are not registered. Please register before logging in.")

    def reservationButtonClicked(self):
        # Get the selected parking spot from the listWidget
        selected_item = self.ui.listWidget.currentItem()

        if selected_item:
            # Extract the room number from the selected item text
            item_text = selected_item.text()
            room_id = int(item_text.split("Camera numarul:")[1].split(",")[0].strip())

            item_text = selected_item.text()
            pret_part = item_text.split("pretul:")[1].split(",")[0].strip()

            item_text = selected_item.text()
            nava_part = item_text.split("pe nava:")[1].split(",")[0].strip()

            # Get the user ID and selected date and time
            user_id = self.current_user_id

            # Obțineți data curentă în formatul "yyyy-MM"
            current_date = datetime.datetime.now().strftime("%d-%m-%Y")

            conn = sqlite3.connect("cruise.db")
            cursor = conn.cursor()

            try:
                # Insert the reservation into the 'reservations' table
                cursor.execute("""
                        INSERT INTO transactions (id_client, nume_nava, camera_rezervata, data_rezervarii, pret)
                        VALUES (?, ?, ?, ?, ?)
                    """, (user_id, nava_part, room_id, current_date, pret_part))

                print((user_id, nava_part, room_id, current_date, pret_part))
                conn.commit()
                conn.close()

                QMessageBox.information(self, "Reservation", "Voyage reserved successfully.")
            except sqlite3.IntegrityError as e:
                # Extract the error message raised by the database
                error_message = str(e)
                # Display the error message in a QMessageBox
                QMessageBox.warning(self, "Reservation Failed", error_message)
        else:
            QMessageBox.warning(self, "Reservation Failed", "Please select a room from the list.")

    def checkingButtonClicked(self):
        # Get the selected check-in and check-out date and time
        checkin_date = self.ui.calendarWidget.selectedDate().toString("yyyy-MM-dd")
        checkout_date = self.ui.calendarWidget_2.selectedDate().toString("yyyy-MM-dd")
        nr_camere_2 = self.ui.spinBox.value()
        nr_camere_3 = self.ui.spinBox_2.value()
        nr_camere_4 = self.ui.spinBox_3.value()

        # Query the reservations table to find overlapping reservations
        conn = sqlite3.connect("cruise.db")
        cursor = conn.cursor()

        # Obțineți data curentă în formatul "yyyy-MM"
        # current_date = datetime.datetime.now().strftime("%d-%m-%Y")

        cursor.execute("""
            SELECT p.id_camera, p.nume_nava, p.tip, p.pret, s.destinatie, s.data_plecare
            FROM prices p
            JOIN ships s ON p.nume_nava = s.nume
            WHERE p.id_camera NOT IN (
                SELECT DISTINCT t.camera_rezervata
                FROM transactions t
                WHERE (
                    date(t.data_rezervarii) >= date(?) AND
                    date(t.data_rezervarii) <= date(?) AND
                    p.nume_nava = t.nume_nava
                )
            ) AND p.nume_nava IN (
                SELECT s.nume
                FROM ships s
                WHERE date(s.data_plecare) >= date(?) AND date(s.data_plecare) <= date(?)
                AND s.nr_2 >= ?
                AND s.nr_3 >= ?
                AND s.nr_4 >= ?
            ) 
        """, (checkin_date, checkout_date, checkin_date, checkout_date, nr_camere_2, nr_camere_3, nr_camere_4))

        print(checkin_date, checkout_date, checkin_date, checkout_date, nr_camere_2, nr_camere_3, nr_camere_4)
        available_cameras = cursor.fetchall()
        print(available_cameras)
        conn.close()

        # Clear existing items in the listWidget
        self.ui.listWidget.clear()

        if available_cameras:
            # Add available rooms as new items in the listWidget
            for camera in available_cameras:
                camera_id = camera[0]
                nume_nava = camera[1]
                tip_camera = camera[2]
                pret = camera[3]
                # Adăugați destinația și data plecării la rezultatele returnate
                destinatie = camera[4]
                data_plecare_str = camera[5]
                data_plecare = datetime.datetime.strptime(data_plecare_str, "%Y-%m-%d").date()

                # Extrageți ziua și luna din data_plecare
                zi_plecare = data_plecare.day
                luna_plecare = data_plecare.month

                # Construiți descrierea datei de plecare
                data_plecare_descriere = f"{zi_plecare:02d}-{luna_plecare}-{data_plecare.year}"

                # Adăugați descrierea tipului camerei în funcție de tip
                if tip_camera == 'nr_2':
                    tip_descriere = "2 persoane"
                elif tip_camera == 'nr_3':
                    tip_descriere = "3 persoane"
                elif tip_camera == 'nr_4':
                    tip_descriere = "4 persoane"
                else:
                    tip_descriere = "N/A"

                item_text = f"Camera numarul: {camera_id}, pe nava: {nume_nava}, tip camera: {tip_descriere}, pretul: {pret}, destinatie: {destinatie}, data plecare: {data_plecare_descriere}"
                item = QListWidgetItem(item_text)
                self.ui.listWidget.addItem(item)
        else:
            QMessageBox.information(self, "Availability", "No available rooms for the selected period.")

    def undoReservation(self):
        # Get the selected reservation item from the listWidget_2
        selected_item = self.ui.listWidget_2.currentItem()
        selected_item_text = selected_item.text()

        if selected_item:
            # Extract reservation details from the selected item text
            parts = selected_item_text.split(", ")

            nume_nava = parts[0].split(": ")[1]
            camera_rezervata = parts[1].split(": ")[1]
            pret = int(parts[2].split(": ")[1])
            data_rezervare = parts[3].split(": ")[1]

            conn = sqlite3.connect("cruise.db")
            cursor = conn.cursor()

            try:
                # Delete the reservation based on parking_number, checkin_date, and checkin_hour
                cursor.execute("""
                    DELETE FROM transactions
                    WHERE id_client = ? AND nume_nava = ? AND camera_rezervata = ? AND pret = ?;
                """, (self.current_user_id, nume_nava, camera_rezervata, pret))

                print(self.current_user_id, nume_nava, camera_rezervata, pret, data_rezervare)
                conn.commit()

                # Check if any rows were affected (reservation was deleted)
                if cursor.rowcount > 0:
                    QMessageBox.information(self, "Reservation Deleted", "Reservation deleted successfully.")
                    self.ui.listWidget_2.takeItem(self.ui.listWidget_2.row(selected_item))
                else:
                    QMessageBox.warning(self, "Deletion Failed", "Reservation not found for deletion.")
            except sqlite3.Error as e:
                error_message = str(e)
                QMessageBox.warning(self, "Deletion Failed", f"Error deleting reservation: {error_message}")
            finally:
                conn.close()
        else:
            QMessageBox.warning(self, "Deletion Failed", "Please select a reservation to delete.")

    def new_user(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def returnToLoginPage(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_5.clear()
        self.ui.lineEdit_6.clear()
        self.ui.lineEdit_7.clear()

    def LogOut(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.current_user_id = None
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()

    def Inregistrare(self):
        conn = sqlite3.connect("cruise.db")
        cursor = conn.cursor()

        nume = self.ui.lineEdit.text()
        prenume = self.ui.lineEdit_2.text()
        mail = self.ui.lineEdit_5.text()
        username = self.ui.lineEdit_6.text()

        # Verificare dacă numele și prenumele conțin doar litere
        if not nume.isalpha() or not prenume.isalpha():
            QMessageBox.warning(self, "Registration Failed",
                                "Name and surname should contain only letters. Please check your input.")
            return

        # Hash the entered password before storing
        hashed_password = self.hash_password(self.ui.lineEdit_7.text())

        # Înainte de blocul try, adăugați validarea NOT NULL
        if not nume or not prenume or not username or not mail or not hashed_password:
            QMessageBox.warning(self, "Registration Failed",
                                "All fields are mandatory. Please fill in all the details.")
            return
        try:
            # Blocul try existent pentru inserția utilizatorului
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))

            # Obțineți ID-ul atribuit
            new_user_id = cursor.lastrowid
            # Utilizați new_user_id pentru a face ce trebuie în continuare
            cursor.execute("INSERT INTO user_detail (id, nume, prenume, mail) VALUES (?, ?, ?, ?)",
                           (new_user_id, nume, prenume, mail))

            conn.commit()
            QMessageBox.information(self, "Registration", "Registration successful. You can now log in.")
        except sqlite3.IntegrityError as e:
            if "UNIQUE constraint failed: user_detail.mail" in str(e):
                QMessageBox.warning(self, "Registration Failed", "Email address already exists. Please choose another.")
            else:
                # Altă eroare de integritate pe care nu o anticipăm
                QMessageBox.warning(self, "Registration Failed", "Wrong e-mail format.")
                print("Unexpected IntegrityError:", e)
            self.ui.lineEdit_5.clear()
        except Exception as e:
            # Orice altă excepție care poate apărea
            QMessageBox.warning(self, "Registration Failed", "An unexpected error occurred during registration.")
            print("Unexpected Exception:", e)
            self.ui.lineEdit_5.clear()
        finally:
            conn.close()

    def returnToTablePage(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def myReservationsButtonClicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        conn = sqlite3.connect("cruise.db")
        cursor = conn.cursor()

        cursor.execute("""
                SELECT nume_nava, camera_rezervata, pret, data_rezervarii
                FROM transactions
                WHERE id_client = ?
            """, (self.current_user_id,))

        reservations = cursor.fetchall()
        conn.close()

        # Clear existing items in the listWidget_2
        self.ui.listWidget_2.clear()

        if reservations:
            # Add reservations as new items in the listWidget_2
            for reservation in reservations:
                nume_nava = reservation[0]
                camera_rezervata = reservation[1]
                pret = reservation[2]
                data_rezervare = reservation[3]

                item_text = f"Ai rezervat pe nava: {nume_nava}, camera: {camera_rezervata}, la pretul: {pret}, pe data: {data_rezervare}"
                item = QListWidgetItem(item_text)
                self.ui.listWidget_2.addItem(item)
        else:
            QMessageBox.information(self, "My Reservations", "No reservations found.")

    def is_valid_login(self, username, hashed_password):
        conn = sqlite3.connect("cruise.db")
        cursor = conn.cursor()

        # Check if the username is registered
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        user = cursor.fetchone()

        if user:
            # Username found, check if the password is correct
            cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
            user_with_password = cursor.fetchone()

            if user_with_password:
                # Password is correct
                conn.close()
                self.ui.lineEdit.clear()
                return "success"
            else:
                # Incorrect password
                conn.close()
                self.ui.lineEdit.clear()
                return "incorrect_password"
        else:
            # Username not found
            conn.close()
            self.ui.lineEdit.clear()
            return "not_registered"

    def get_user_id(self, username):
        conn = sqlite3.connect("cruise.db")
        cursor = conn.cursor()

        # Get the user ID based on the username
        cursor.execute("SELECT id FROM users WHERE username=?", (username,))
        user_id = cursor.fetchone()[0]  # Assuming the user ID is the first column

        conn.close()

        return user_id

    def hash_password(self, password):
        # Use SHA-256 for password hashing
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password

if __name__ == "__main__":
    #conectare baza de date
    conn = sqlite3.connect("cruise.db")
    cursor = conn.cursor()

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
    """)

    cursor.execute("""
                CREATE TABLE IF NOT EXISTS user_detail (
                    id INTEGER,
                    nume VARCHAR2(50) NOT NULL,
                    prenume VARCHAR2(50) NOT NULL,
                    mail VARCHAR2(50) UNIQUE NOT NULL,
                    CHECK (mail LIKE '%_@%_.__%')
                    FOREIGN KEY (id) REFERENCES users(id)
                )
    """)

    # Check if the 'ship' table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='ships'")
    ships_table_exists = cursor.fetchone()

    if not ships_table_exists:
        # Create the 'ships' table
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS ships (
                    nume VARCHAR2(50) PRIMARY KEY NOT NULL,
                    data_plecare DATE,
                    destinatie TEXT NOT NULL,
                    nr_2 INTEGER,
                    nr_3 INTEGER,
                    nr_4 INTEGER
                )
        """)

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS prices (
                id_camera INTEGER PRIMARY KEY AUTOINCREMENT,
                nume_nava VARCHAR2(50) NOT NULL,
                tip INTEGER,
                pret INTEGER,
                FOREIGN KEY (nume_nava) REFERENCES ships(nume)
            )
    """)

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id_client INTEGER,
                nume_nava VARCHAR2(50) NOT NULL,
                camera_rezervata TEXT UNIQUE NOT NULL,
                data_rezervarii DATETIME, 
                pret INTEGER,
                FOREIGN KEY (id_client) REFERENCES users(id),
                FOREIGN KEY (nume_nava) REFERENCES ships(nume)
            )
    """)

    #Populam tabelele
    cursor.execute("""
        INSERT OR REPLACE INTO ships (nume, data_plecare, destinatie, nr_2, nr_3, nr_4)
        VALUES 
            ('Siu', '2024-01-07', 'Portugalia', 4, 6, 7),
            ('Ankara', '2024-01-11', 'America-de-Sud', 4, 3, 6),
            ('Romina', '2024-01-23', 'Japonia', 5, 5, 6),
            ('Yamato', '2024-01-18', 'Grecia', 5, 5, 3),
            ('Essex', '2024-01-02', 'Italia', 2, 6, 7),
            ('Magnifica', '2024-01-14', 'Franta', 5, 6, 4),
            ('Sirena', '2024-01-27', 'Spania', 4, 2, 5)
    """)

    tipuri_camere = ['nr_2', 'nr_3', 'nr_4']
    nume_nave = ['Siu', 'Ankara', 'Romina', 'Yamato', 'Essex', 'Magnifica', 'Sirena']

    for nume_nava in nume_nave:
        cursor.execute("""
            SELECT nr_2, nr_3, nr_4 FROM ships WHERE nume = ?
        """, (nume_nava,))
        nr_2, nr_3, nr_4 = cursor.fetchone()

        # Adaugă prețurile pentru fiecare tip de cameră doar dacă nu există deja înregistrări
        for tip_camera in tipuri_camere:
            if tip_camera == 'nr_2' and nr_2 > 0:
                existing_rows = cursor.execute("""
                    SELECT COUNT(*) FROM prices WHERE nume_nava = ? AND tip = 'nr_2'
                """, (nume_nava,)).fetchone()[0]
                if existing_rows == 0:
                    for _ in range(nr_2):
                        pret_camera_nr_2 = random.randint(100, 500)
                        cursor.execute("""
                            INSERT INTO prices (nume_nava, tip, pret)
                            VALUES (?, ?, ?)
                        """, (nume_nava, 'nr_2', pret_camera_nr_2))

            elif tip_camera == 'nr_3' and nr_3 > 0:
                existing_rows = cursor.execute("""
                    SELECT COUNT(*) FROM prices WHERE nume_nava = ? AND tip = 'nr_3'
                """, (nume_nava,)).fetchone()[0]
                if existing_rows == 0:
                    for _ in range(nr_3):
                        pret_camera_nr_3 = random.randint(100, 500)
                        cursor.execute("""
                            INSERT INTO prices (nume_nava, tip, pret)
                            VALUES (?, ?, ?)
                        """, (nume_nava, 'nr_3', pret_camera_nr_3))

            elif tip_camera == 'nr_4' and nr_4 > 0:
                existing_rows = cursor.execute("""
                    SELECT COUNT(*) FROM prices WHERE nume_nava = ? AND tip = 'nr_4'
                """, (nume_nava,)).fetchone()[0]
                if existing_rows == 0:
                    for _ in range(nr_4):
                        pret_camera_nr_4 = random.randint(100, 500)
                        cursor.execute("""
                            INSERT INTO prices (nume_nava, tip, pret)
                            VALUES (?, ?, ?)
                        """, (nume_nava, 'nr_4', pret_camera_nr_4))

    conn.commit()
    conn.close()

    #start aplicatie
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
