import sqlite3


class SQLManager:

	def __init__(self):
		self.conn = sqlite3.connect('students.db')
		self.c = self.conn.cursor()

	def close(self):
		self.conn.close()

	def clean(self, input_):
		return input_.replace('(', '').replace(')', '').replace(';', '').replace('\"', '').replace('\'', '')

	def create_table(self):
		with self.conn:
			self.c.execute("""
				CREATE TABLE students (
					first text,
					last text,
					labs text,
					v integer
				)
			""")

	def insert_student(self, student):
		with self.conn:
			self.c.execute("""
				INSERT INTO students VALUES (:first, :last, :labs, :v)
			""", {'first': student.first, 'last': student.last, 'labs': student.labs, 'v': student.v})

	def get_student(self, student_first, student_last):
		self.c.execute("""
			SELECT * FROM students WHERE first = :first AND last = :last
		""", {'first': student_first, 'last': student_last})
		return self.c.fetchall()

	def add_labs(self, student, labs):
		with self.conn:
			for lab in labs.split():
				self.c.execute("""
					UPDATE students SET labs = :new_labs WHERE first = :first AND last = :last
				""", {'new_labs': ' '.join(student.labs.split().append(lab)), \
					'first': student.first, 'last': student.last})

	def delete_student(self, student):
		with self.conn:
			self.c.execute("""
				DELETE from students WHERE first = :first AND last = :last
			""", {'first': student.first, 'last': student.last})