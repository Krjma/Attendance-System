import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('attendance.db')
cursor = conn.cursor()

# Create Advisors Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Advisors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    password TEXT NOT NULL
)
''')

# Create Instructors Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Instructors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    password TEXT NOT NULL
)
''')

# Create Classes Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Classes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    instructor_id INTEGER,
    FOREIGN KEY (instructor_id) REFERENCES Instructors(id)
)
''')

# Create Students Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    password INTEGER NOT NULL,
    name TEXT,
    class_id INTEGER,
    advisor_id INTEGER,
    FOREIGN KEY (class_id) REFERENCES Classes(id),
    FOREIGN KEY (advisor_id) REFERENCES Advisors(id)
)
''')

# Create AttendanceRecord Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS AttendanceRecord (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    date TEXT,
    status TEXT,
    excuse TEXT,
    class_id INTEGER,
    excuse_status TEXT,
    FOREIGN KEY (student_id) REFERENCES Students(id),
    FOREIGN KEY (class_id) REFERENCES Classes(id)
)
''')

# Insert Advisors
cursor.executemany('''
INSERT INTO Advisors (name, password) VALUES (?, ?)
''', [('Dr. Ali', 'password1'), ('Dr. Hassan', 'password2'), ('Dr. Omar', 'password3')])

# Insert Instructors
cursor.executemany('''
INSERT INTO Instructors (name, password) VALUES (?, ?)
''', [('Mr. Saeed', 'password4'), ('Mr. Yasser', 'password5'), ('Mr. Nasser', 'password6')])

# Insert Classes and Assign to Instructors
cursor.executemany('''
INSERT INTO Classes (name, instructor_id) VALUES (?, ?)
''', [('Math 101', 1), ('Physics 201', 2), ('Computer Science 101', 3)])

# Insert Students and Assign to Classes and Advisors
cursor.executemany('''
INSERT INTO Students (id, name, class_id, advisor_id, password) VALUES (?, ?, ?, ?, ?)
''', [
    (1, 'Ahmed', 1, 1, 'student_password1'),
    (2, 'Mohammed', 1, 1, 'student_password2'),
    (3, 'Omar', 2, 2, 'student_password3'),
    (4, 'Hassan', 2, 2, 'student_password4'),
    (5, 'Khaled', 3, 3, 'student_password5'),
    (6, 'Fahad', 3, 3, 'student_password6')
])

# Insert Attendance Records
cursor.executemany('''
INSERT INTO AttendanceRecord (student_id, date, status, excuse, class_id, excuse_status) VALUES (?, ?, ?, ?, ?, ?)
''', [
    (1, '2024-10-27', 'Present', None, 1, None),
    (2, '2024-10-27', 'Absent', 'medical', 1, 'wait to approve'),
    (3, '2024-10-27', 'Present', None, 2, None),
    (4, '2024-10-27', 'Absent', 'medical', 2, 'wait to approve')
])


# Commit changes and close connection
conn.commit()
conn.close()

print("Database created and populated successfully.")
