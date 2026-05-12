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
Login = Class(name="Login")
Employee = Class(name="Employee")
Salary = Class(name="Salary")
Expenses = Class(name="Expenses")
Leave = Class(name="Leave")
Attendance = Class(name="Attendance")
Permanant = Class(name="Permanant")
Temporary = Class(name="Temporary")
Sick_Leave = Class(name="Sick_Leave")
Casual_Leave = Class(name="Casual_Leave")
Half_Day = Class(name="Half_Day")
User = Class(name="User")
Admin = Class(name="Admin")
Supervisor = Class(name="Supervisor")
Normal_User = Class(name="Normal_User")
Employer = Class(name="Employer")
Backup = Class(name="Backup")
Awards = Class(name="Awards")

# Login class attributes and methods

# Employee class attributes and methods

# Salary class attributes and methods

# Expenses class attributes and methods

# Leave class attributes and methods

# Attendance class attributes and methods

# Permanant class attributes and methods

# Temporary class attributes and methods

# Sick_Leave class attributes and methods

# Casual_Leave class attributes and methods

# Half_Day class attributes and methods

# User class attributes and methods

# Admin class attributes and methods

# Supervisor class attributes and methods

# Normal_User class attributes and methods

# Employer class attributes and methods

# Backup class attributes and methods

# Awards class attributes and methods

# Relationships
Employee_Awards: BinaryAssociation = BinaryAssociation(
    name="Employee_Awards",
    ends={
        Property(name="_0___10", type=Awards, multiplicity=Multiplicity(0, 1)),
        Property(name="employee11", type=Employee, multiplicity=Multiplicity(1, 1))
    }
)
Employer_Login: BinaryAssociation = BinaryAssociation(
    name="Employer_Login",
    ends={
        Property(name="login12", type=Login, multiplicity=Multiplicity(0, 1)),
        Property(name="employer13", type=Employer, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Login: BinaryAssociation = BinaryAssociation(
    name="Employee_Login",
    ends={
        Property(name="Employee_Login_00", type=Login, multiplicity=Multiplicity(0, 1)),
        Property(name="employee1", type=Employee, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Salary: BinaryAssociation = BinaryAssociation(
    name="Employee_Salary",
    ends={
        Property(name="salary2", type=Salary, multiplicity=Multiplicity(1, 1)),
        Property(name="employee3", type=Employee, multiplicity=Multiplicity(1, 1))
    }
)
Employee_Attendance: BinaryAssociation = BinaryAssociation(
    name="Employee_Attendance",
    ends={
        Property(name="attendance4", type=Attendance, multiplicity=Multiplicity(0, 1)),
        Property(name="employee5", type=Employee, multiplicity=Multiplicity(1, 1))
    }
)
Salary_Expenses: BinaryAssociation = BinaryAssociation(
    name="Salary_Expenses",
    ends={
        Property(name="expenses6", type=Expenses, multiplicity=Multiplicity(0, 1)),
        Property(name="salary7", type=Salary, multiplicity=Multiplicity(0, 1))
    }
)
Leave_Employee: BinaryAssociation = BinaryAssociation(
    name="Leave_Employee",
    ends={
        Property(name="employee8", type=Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="_0___9", type=Leave, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_MB5EMJMMEeeaCsv2qBF4QA",
    types={Login, Employee, Salary, Expenses, Leave, Attendance, Permanant, Temporary, Sick_Leave, Casual_Leave, Half_Day, User, Admin, Supervisor, Normal_User, Employer, Backup, Awards},
    associations={Employee_Awards, Employer_Login, Employee_Login, Employee_Salary, Employee_Attendance, Salary_Expenses, Leave_Employee},
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