from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
import calendar 
from sqlalchemy.orm import sessionmaker

# First, you need to create your database file. To create it, you should use the create_engine() method, where file_name is the database file name
engine = create_engine('sqlite:///todo.db?check_same_thread=False')

# Once you've created your database file, you need to create a table in it. First, create a model class that describes the table in the database. 
# All model classes should inherit from the DeclarativeMeta class that is returned by declarative_base()

Base = declarative_base()

class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today())
 
    def __repr__(self):
        return self.task

# After we've described our table, it's time to create it in our database. All we need is to call the create_all() method and pass engine to it
Base.metadata.create_all(engine)

# Now we can access the database and store data in it. To access the database, we need to create a session
Session = sessionmaker(bind=engine)
session = Session()

def display_tasks():
	print("""\n1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit""")

def todays_tasks():
	today = datetime.today().date() # get todays date
	day = today.day # get the day for date
	month = today.strftime('%b') # converts the month in to proper readable format like 8 is converted to Aug
	# get all rows where date matches todays date
	rows = session.query(Table).filter(Table.deadline == today).all()
	if rows == []:
		print(f"\nToday {day} {month}:")
		print("Nothing to do!")
	else:
		print(f"\nToday {day} {month}:")
		for row in rows:
			print(row.task) # print all tasks

def weeks_tasks():
	today = datetime.today().date() # get todays date
	# iterate 7 times so that we can get a weeks data from todays date
	for counter in range(0,7):
		print(" ")
		week_date = today + timedelta(days=counter) # this will add set number of days to todays's date to give a new date
		week_day_name = calendar.day_name[week_date.weekday()] # convert day into day name using calender package
		day = week_date.day
		month = week_date.strftime('%b')
		rows = session.query(Table).filter(Table.deadline == week_date).all()
		if rows == []:
			print(f"{week_day_name} {day} {month}:")
			print("Nothing to do!")
		else:
			print(f"{week_day_name} {day} {month}:")
			j = 1
			for row in rows:
				print(f"{j}. {row.task}")
				j +=1

def all_tasks():
	rows = session.query(Table).order_by(Table.deadline).all()
	counter = 1
	for row in rows:
		print(f"{counter}. {row.task} {row.deadline.day} {row.deadline.strftime('%b')}")
		counter += 1

def missed_tasks():
	today = datetime.today().date() # get todays date
	# get tasks where deadline is less than todays date
	rows = session.query(Table).filter(Table.deadline < datetime.today()).order_by(Table.deadline).all()
	print("Missed tasks:")
	counter = 1
	for row in rows:
		day = row.deadline.day
		month = row.deadline.strftime('%b')
		print(f"{counter}. {row.task} {day} {month}")
		counter += 1

def add_task():
	print("Enter task")
	user_task = input()
	print("Enter deadline (yyyy-mm-dd)")
	task_deadline = input()
	task_deadline_obj = datetime.strptime(task_deadline, '%Y-%m-%d') # convert string obj into datetime object
	new_row = Table(task = user_task, deadline = task_deadline_obj)
	session.add(new_row)
	session.commit()
	print("The task has been added!")

def delete_task():
	rows = session.query(Table).order_by(Table.deadline).all()
	if rows == []:
		print("Nothing to delete")
	else:
		print("Here are all the tasks : ")
		counter = 1
		for row in rows:
			print(f"{counter}. {row.task} {row.deadline.day} {row.deadline.strftime('%b')}")
			counter += 1
		delete_row = int(input("Chose the number of the task you want to delete: "))
		delete_row -= 1
		session.delete(rows[delete_row])
		session.commit()
		print("The task has been deleted!")

display_tasks()
user_input = input("Enter your choice : ")

while user_input != "0":
	if user_input in ["1","2","3","4","5","6"]:
		if user_input == "1":
			todays_tasks()
		elif user_input == "2":
			weeks_tasks()
		elif user_input == "3":
			all_tasks()
		elif user_input == "4":
			missed_tasks()
		elif user_input == "5":
			add_task()
		elif user_input == "6":
			delete_task()
	else :
		print("Please choose an option from the list.")
	display_tasks()
	user_input = input("Enter your choice : ")

print("Bye!")
