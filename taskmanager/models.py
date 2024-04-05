from taskmanager import db


class Category(db.Model):
    # Schema for the Category table
    id = db.Column(db.Integer, primary_key=True) # Primary key
    category_name = db.Column(db.String(25), unique=True, nullable=False) # Category name
    tasks = db.relationship('Task', backref='category', lazy=True, cascade="all, delete-orphan") # Relationship with Task table


    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.category_name



class Task(db.Model):
    # Schema for the Task table
    id = db.Column(db.Integer, primary_key=True) # Primary key
    task_name = db.Column(db.String(50), unique=True, nullable=False) # Task name
    task_description = db.Column(db.Text, nullable=False) # Task description
    is_urgent = db.Column(db.Boolean, default=False, nullable=False) # Task urgency
    due_date = db.Column(db.DateTime, nullable=False) # Task due date
    category_id = db.Column(db.Integer, db.ForeignKey('category.id', ondelete = "CASCADE"), nullable=False) # Foreign key to Category table


    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0}, - Task {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        ) 
 