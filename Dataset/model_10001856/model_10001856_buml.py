####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
user = Class(name="user")
teacher = Class(name="teacher")
Student = Class(name="Student")
Department = Class(name="Department")
Mark = Class(name="Mark")
Task = Class(name="Task")
Quiz = Class(name="Quiz")
news = Class(name="news")

# user class attributes and methods
user_id: Property = Property(name="id", type=IntegerType)
user_name: Property = Property(name="name", type=StringType)
user.attributes={user_name, user_id}

# teacher class attributes and methods
teacher_id: Property = Property(name="id", type=IntegerType)
teacher_name: Property = Property(name="name", type=StringType)
teacher.attributes={teacher_id, teacher_name}

# Student class attributes and methods
Student_name: Property = Property(name="name", type=StringType)
Student_id: Property = Property(name="id", type=IntegerType)
Student.attributes={Student_name, Student_id}

# Department class attributes and methods
Department_id: Property = Property(name="id", type=IntegerType)
Department_name: Property = Property(name="name", type=StringType)
Department_teachers__: Property = Property(name="teachers__", type=IntegerType)
Department_modules__: Property = Property(name="modules__", type=StringType)
Department.attributes={Department_teachers__, Department_modules__, Department_id, Department_name}

# Mark class attributes and methods
Mark_id: Property = Property(name="id", type=Student)
Mark_Mark: Property = Property(name="Mark", type=IntegerType)
Mark.attributes={Mark_id, Mark_Mark}

# Task class attributes and methods

# Quiz class attributes and methods
Quiz_title: Property = Property(name="title", type=StringType)
Quiz_moduleName: Property = Property(name="moduleName", type=StringType)
Quiz_questions__: Property = Property(name="questions__", type=StringType)
Quiz.attributes={Quiz_title, Quiz_questions__, Quiz_moduleName}

# news class attributes and methods
news_author: Property = Property(name="author", type=StringType)
news_dlnews: Property = Property(name="dlnews", type=StringType)
news.attributes={news_author, news_dlnews}

# Domain Model
domain_model = DomainModel(
    name="____M0L8xEeeEXb8Dudo6PQ",
    types={user, teacher, Student, Department, Mark, Task, Quiz, news},
    associations={},
    generalizations={},
    metadata=None
)

###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)