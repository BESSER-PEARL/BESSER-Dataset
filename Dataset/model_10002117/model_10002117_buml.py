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
Course = Class(name="Course")
Login = Class(name="Login")
names = Class(name="names")
New_user = Class(name="New_user")
Interface_Interface = Class(name="Interface_Interface")
Class_ = Class(name="Class")
Interface1_Interface = Class(name="Interface1_Interface")
Interface2_Interface = Class(name="Interface2_Interface")
Home_page = Class(name="Home_page")
Show_all_grades = Class(name="Show_all_grades")
Add_notes = Class(name="Add_notes")

# Course class attributes and methods
Course_Course_name: Property = Property(name="Course_name", type=StringType)
Course_Day: Property = Property(name="Day", type=StringType)
Course_Time: Property = Property(name="Time", type=StringType)
Course_Room: Property = Property(name="Room", type=IntegerType)
Course_Teacher: Property = Property(name="Teacher", type=StringType)
Course_Student_ID: Property = Property(name="Student_ID", type=IntegerType)
Course_Grade_earned: Property = Property(name="Grade_earned", type=StringType)
Course_Status: Property = Property(name="Status", type=StringType)
Course_Course_Index: Property = Property(name="Course_Index", type=IntegerType)
Course.attributes={Course_Time, Course_Teacher, Course_Student_ID, Course_Course_name, Course_Course_Index, Course_Grade_earned, Course_Status, Course_Day, Course_Room}

# Login class attributes and methods
Login_Student_ID: Property = Property(name="Student_ID", type=IntegerType)
Login_Password: Property = Property(name="Password", type=StringType)
Login_Email: Property = Property(name="Email", type=StringType)
Login.attributes={Login_Email, Login_Student_ID, Login_Password}

# names class attributes and methods

# New_user class attributes and methods
New_user_Student_ID: Property = Property(name="Student_ID", type=IntegerType)
New_user_First_name: Property = Property(name="First_name", type=StringType)
New_user_Last_Name: Property = Property(name="Last_Name", type=StringType)
New_user_Major: Property = Property(name="Major", type=StringType)
New_user_Student_ID1: Property = Property(name="Student_ID1", type=IntegerType)
New_user_Contact_No: Property = Property(name="Contact_No", type=IntegerType)
New_user.attributes={New_user_Last_Name, New_user_First_name, New_user_Contact_No, New_user_Major, New_user_Student_ID1, New_user_Student_ID}

# Interface_Interface class attributes and methods

# Class class attributes and methods

# Interface1_Interface class attributes and methods

# Interface2_Interface class attributes and methods

# Home_page class attributes and methods

# Show_all_grades class attributes and methods
Show_all_grades_Student_ID: Property = Property(name="Student_ID", type=IntegerType)
Show_all_grades_First_Name: Property = Property(name="First_Name", type=StringType)
Show_all_grades_Last_Name: Property = Property(name="Last_Name", type=StringType)
Show_all_grades_Course_name: Property = Property(name="Course_name", type=StringType)
Show_all_grades_Teacher: Property = Property(name="Teacher", type=StringType)
Show_all_grades_Grade_earned: Property = Property(name="Grade_earned", type=StringType)
Show_all_grades.attributes={Show_all_grades_Grade_earned, Show_all_grades_Teacher, Show_all_grades_First_Name, Show_all_grades_Student_ID, Show_all_grades_Last_Name, Show_all_grades_Course_name}

# Add_notes class attributes and methods
Add_notes_Student_ID: Property = Property(name="Student_ID", type=IntegerType)
Add_notes_Course_Name: Property = Property(name="Course_Name", type=StringType)
Add_notes_Notes_taken: Property = Property(name="Notes_taken", type=StringType)
Add_notes.attributes={Add_notes_Course_Name, Add_notes_Notes_taken, Add_notes_Student_ID}

# Relationships
Login_New_user: BinaryAssociation = BinaryAssociation(
    name="Login_New_user",
    ends={
        Property(name="new_user0", type=New_user, multiplicity=Multiplicity(0, 1)),
        Property(name="login1", type=Login, multiplicity=Multiplicity(0, 1))
    }
)
Login_Home_page: BinaryAssociation = BinaryAssociation(
    name="Login_Home_page",
    ends={
        Property(name="home_page2", type=Home_page, multiplicity=Multiplicity(0, 1)),
        Property(name="login3", type=Login, multiplicity=Multiplicity(0, 1))
    }
)
Home_page_Show_all_grades: BinaryAssociation = BinaryAssociation(
    name="Home_page_Show_all_grades",
    ends={
        Property(name="show_all_grades4", type=Show_all_grades, multiplicity=Multiplicity(0, 1)),
        Property(name="home_page5", type=Home_page, multiplicity=Multiplicity(0, 1))
    }
)
Home_page_Course: BinaryAssociation = BinaryAssociation(
    name="Home_page_Course",
    ends={
        Property(name="course6", type=Course, multiplicity=Multiplicity(0, 1)),
        Property(name="home_page7", type=Home_page, multiplicity=Multiplicity(0, 1))
    }
)
Home_page_Add_notes: BinaryAssociation = BinaryAssociation(
    name="Home_page_Add_notes",
    ends={
        Property(name="add_notes8", type=Add_notes, multiplicity=Multiplicity(0, 1)),
        Property(name="home_page9", type=Home_page, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_pSnXACrpEem05KmXgSfXig",
    types={Course, Login, names, New_user, Interface_Interface, Class_, Interface1_Interface, Interface2_Interface, Home_page, Show_all_grades, Add_notes},
    associations={Login_New_user, Login_Home_page, Home_page_Show_all_grades, Home_page_Course, Home_page_Add_notes},
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