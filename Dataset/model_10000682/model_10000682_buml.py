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
User_Actor = Class(name="User_Actor")
test_UseCase = Class(name="test_UseCase")
Guest = Class(name="Guest")
VirtualTour = Class(name="VirtualTour")
User = Class(name="User")
Admin = Class(name="Admin")
Lecturer = Class(name="Lecturer")
Society = Class(name="Society")
Student = Class(name="Student")
Post = Class(name="Post")
Event = Class(name="Event")
Location = Class(name="Location")
Comment = Class(name="Comment")
Guest1 = Class(name="Guest1")
VirtualTour1 = Class(name="VirtualTour1")
User1 = Class(name="User1")
Post1 = Class(name="Post1")
Event1 = Class(name="Event1")
Location1 = Class(name="Location1")
Comment1 = Class(name="Comment1")
Lecturer1 = Class(name="Lecturer1")
Society1 = Class(name="Society1")
Student1 = Class(name="Student1")
Admin1 = Class(name="Admin1")

# User_Actor class attributes and methods

# test_UseCase class attributes and methods

# Guest class attributes and methods

# VirtualTour class attributes and methods

# User class attributes and methods

# Admin class attributes and methods

# Lecturer class attributes and methods

# Society class attributes and methods

# Student class attributes and methods

# Post class attributes and methods

# Event class attributes and methods

# Location class attributes and methods

# Comment class attributes and methods

# Guest1 class attributes and methods

# VirtualTour1 class attributes and methods
VirtualTour1_URL: Property = Property(name="URL", type=StringType)
VirtualTour1.attributes={VirtualTour1_URL}

# User1 class attributes and methods
User1_username: Property = Property(name="username", type=StringType)
User1_email: Property = Property(name="email", type=StringType)
User1_name: Property = Property(name="name", type=StringType)
User1_campus: Property = Property(name="campus", type=StringType)
User1_isStaff: Property = Property(name="isStaff", type=BooleanType)
User1_attribute: Property = Property(name="attribute", type=StringType)
User1.attributes={User1_attribute, User1_isStaff, User1_username, User1_name, User1_campus, User1_email}

# Post1 class attributes and methods
Post1_date: Property = Property(name="date", type=StringType)
Post1_title: Property = Property(name="title", type=StringType)
Post1_body: Property = Property(name="body", type=StringType)
Post1_author: Property = Property(name="author", type=StringType)
Post1_files: Property = Property(name="files", type=StringType)
Post1.attributes={Post1_author, Post1_title, Post1_body, Post1_files, Post1_date}

# Event1 class attributes and methods
Event1_name: Property = Property(name="name", type=StringType)
Event1_location: Property = Property(name="location", type=Location)
Event1_date: Property = Property(name="date", type=StringType)
Event1_rating: Property = Property(name="rating", type=IntegerType)
Event1_eventOwner: Property = Property(name="eventOwner", type=User1)
Event1_size: Property = Property(name="size", type=IntegerType)
Event1_isOpen: Property = Property(name="isOpen", type=BooleanType)
Event1_invites: Property = Property(name="invites", type=StringType)
Event1_joined: Property = Property(name="joined", type=StringType)
Event1.attributes={Event1_size, Event1_joined, Event1_rating, Event1_location, Event1_name, Event1_invites, Event1_isOpen, Event1_date, Event1_eventOwner}

# Location1 class attributes and methods
Location1_name: Property = Property(name="name", type=StringType)
Location1_address: Property = Property(name="address", type=StringType)
Location1_capacity: Property = Property(name="capacity", type=IntegerType)
Location1.attributes={Location1_address, Location1_capacity, Location1_name}

# Comment1 class attributes and methods
Comment1_author: Property = Property(name="author", type=StringType)
Comment1_date: Property = Property(name="date", type=StringType)
Comment1_body: Property = Property(name="body", type=StringType)
Comment1.attributes={Comment1_date, Comment1_body, Comment1_author}

# Lecturer1 class attributes and methods
Lecturer1_school: Property = Property(name="school", type=StringType)
Lecturer1.attributes={Lecturer1_school}

# Society1 class attributes and methods
Society1_yearEstablished: Property = Property(name="yearEstablished", type=IntegerType)
Society1.attributes={Society1_yearEstablished}

# Student1 class attributes and methods
Student1_school: Property = Property(name="school", type=StringType)
Student1_course: Property = Property(name="course", type=StringType)
Student1_yearOfStudy: Property = Property(name="yearOfStudy", type=IntegerType)
Student1.attributes={Student1_school, Student1_yearOfStudy, Student1_course}

# Admin1 class attributes and methods

# Relationships
User_Event2: BinaryAssociation = BinaryAssociation(
    name="User_Event2",
    ends={
        Property(name="event22", type=Event1, multiplicity=Multiplicity(0, 1)),
        Property(name="user23", type=User1, multiplicity=Multiplicity(0, 1))
    }
)
Post_Comment: BinaryAssociation = BinaryAssociation(
    name="Post_Comment",
    ends={
        Property(name="comment24", type=Comment1, multiplicity=Multiplicity(0, 9999)),
        Property(name="post25", type=Post1, multiplicity=Multiplicity(1, 1))
    }
)
Event_Post: BinaryAssociation = BinaryAssociation(
    name="Event_Post",
    ends={
        Property(name="post26", type=Post1, multiplicity=Multiplicity(0, 9999)),
        Property(name="event27", type=Event1, multiplicity=Multiplicity(1, 1))
    }
)
Location_Event2: BinaryAssociation = BinaryAssociation(
    name="Location_Event2",
    ends={
        Property(name="event28", type=Event1, multiplicity=Multiplicity(1, 1)),
        Property(name="location229", type=Location1, multiplicity=Multiplicity(1, 1))
    }
)
MyClass_MyClass2: BinaryAssociation = BinaryAssociation(
    name="MyClass_MyClass2",
    ends={
        Property(name="myClass20", type=VirtualTour, multiplicity=Multiplicity(0, 1)),
        Property(name="myClass1", type=Guest, multiplicity=Multiplicity(0, 1))
    }
)
User_Post: BinaryAssociation = BinaryAssociation(
    name="User_Post",
    ends={
        Property(name="post2", type=Post, multiplicity=Multiplicity(0, 1)),
        Property(name="user3", type=User, multiplicity=Multiplicity(0, 1))
    }
)
User_Event: BinaryAssociation = BinaryAssociation(
    name="User_Event",
    ends={
        Property(name="event4", type=Event, multiplicity=Multiplicity(0, 1)),
        Property(name="user5", type=User, multiplicity=Multiplicity(0, 1))
    }
)
Location_Event: BinaryAssociation = BinaryAssociation(
    name="Location_Event",
    ends={
        Property(name="event6", type=Event, multiplicity=Multiplicity(0, 1)),
        Property(name="location7", type=Location, multiplicity=Multiplicity(0, 1))
    }
)
Comment_Post: BinaryAssociation = BinaryAssociation(
    name="Comment_Post",
    ends={
        Property(name="post8", type=Post, multiplicity=Multiplicity(0, 1)),
        Property(name="comment9", type=Comment, multiplicity=Multiplicity(0, 1))
    }
)
Comment_User: BinaryAssociation = BinaryAssociation(
    name="Comment_User",
    ends={
        Property(name="user10", type=User, multiplicity=Multiplicity(0, 1)),
        Property(name="comment11", type=Comment, multiplicity=Multiplicity(0, 1))
    }
)
User_VirtualTour: BinaryAssociation = BinaryAssociation(
    name="User_VirtualTour",
    ends={
        Property(name="virtualTour12", type=VirtualTour, multiplicity=Multiplicity(0, 1)),
        Property(name="user13", type=User, multiplicity=Multiplicity(0, 1))
    }
)
MyClass_MyClass22: BinaryAssociation = BinaryAssociation(
    name="MyClass_MyClass22",
    ends={
        Property(name="myClass214", type=VirtualTour1, multiplicity=Multiplicity(0, 1)),
        Property(name="myClass15", type=Guest1, multiplicity=Multiplicity(0, 1))
    }
)
User_VirtualTour2: BinaryAssociation = BinaryAssociation(
    name="User_VirtualTour2",
    ends={
        Property(name="virtualTour16", type=VirtualTour1, multiplicity=Multiplicity(0, 1)),
        Property(name="user17", type=User1, multiplicity=Multiplicity(0, 1))
    }
)
User_Post2: BinaryAssociation = BinaryAssociation(
    name="User_Post2",
    ends={
        Property(name="post18", type=Post1, multiplicity=Multiplicity(0, 1)),
        Property(name="user19", type=User1, multiplicity=Multiplicity(0, 1))
    }
)
Comment_User2: BinaryAssociation = BinaryAssociation(
    name="Comment_User2",
    ends={
        Property(name="user20", type=User1, multiplicity=Multiplicity(0, 1)),
        Property(name="comment21", type=Comment1, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_54c35781_cf12_4767_9e1e_e36004666c7d",
    types={User_Actor, test_UseCase, Guest, VirtualTour, User, Admin, Lecturer, Society, Student, Post, Event, Location, Comment, Guest1, VirtualTour1, User1, Post1, Event1, Location1, Comment1, Lecturer1, Society1, Student1, Admin1},
    associations={User_Event2, Post_Comment, Event_Post, Location_Event2, MyClass_MyClass2, User_Post, User_Event, Location_Event, Comment_Post, Comment_User, User_VirtualTour, MyClass_MyClass22, User_VirtualTour2, User_Post2, Comment_User2},
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