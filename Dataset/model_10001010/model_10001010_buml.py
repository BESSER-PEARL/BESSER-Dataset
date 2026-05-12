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
Employee = Class(name="Employee")
Authenticate_staff = Class(name="Authenticate_staff")
Login = Class(name="Login")
Employee_Management_System_Component = Class(name="Employee_Management_System_Component")
Authentication_UseCase = Class(name="Authentication_UseCase")
Salary_Management_UseCase = Class(name="Salary_Management_UseCase")
Administrator_Actor = Class(name="Administrator_Actor")
Employee_Actor = Class(name="Employee_Actor")
Login_external = Class(name="Login_external")
Logout_external = Class(name="Logout_external")

# Employee class attributes and methods
Employee_Emp_Id: Property = Property(name="Emp_Id", type=IntegerType)
Employee_Emp_Name: Property = Property(name="Emp_Name", type=StringType)
Employee_Emp_Address: Property = Property(name="Emp_Address", type=StringType)
Employee_Emp_DOB: Property = Property(name="Emp_DOB", type=DateType)
Employee_Emp_Date_Of_Joint: Property = Property(name="Emp_Date_Of_Joint", type=DateType)
Employee_Emp_Position: Property = Property(name="Emp_Position", type=StringType)
Employee.attributes={Employee_Emp_Date_Of_Joint, Employee_Emp_Position, Employee_Emp_Id, Employee_Emp_Name, Employee_Emp_DOB, Employee_Emp_Address}

# Authenticate_staff class attributes and methods
Authenticate_staff_UserName: Property = Property(name="UserName", type=StringType)
Authenticate_staff_Password: Property = Property(name="Password", type=StringType)
Authenticate_staff_Authendication_Mood: Property = Property(name="Authendication_Mood", type=StringType)
Authenticate_staff.attributes={Authenticate_staff_UserName, Authenticate_staff_Authendication_Mood, Authenticate_staff_Password}

# Login class attributes and methods
Login_UserName: Property = Property(name="UserName", type=StringType)
Login_Password: Property = Property(name="Password", type=StringType)
Login.attributes={Login_UserName, Login_Password}

# Employee_Management_System_Component class attributes and methods

# Authentication_UseCase class attributes and methods

# Salary_Management_UseCase class attributes and methods

# Administrator_Actor class attributes and methods

# Employee_Actor class attributes and methods

# Login_external class attributes and methods

# Logout_external class attributes and methods

# Relationships
Employee_Login: BinaryAssociation = BinaryAssociation(
    name="Employee_Login",
    ends={
        Property(name="login0", type=Login_external, multiplicity=Multiplicity(0, 1)),
        Property(name="employee1", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Logout: BinaryAssociation = BinaryAssociation(
    name="Employee_Logout",
    ends={
        Property(name="logout2", type=Logout_external, multiplicity=Multiplicity(0, 1)),
        Property(name="employee3", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_7a9d2c95_adc9_4b9b_ae6a_5deb8b8ac09a",
    types={Employee, Authenticate_staff, Login, Employee_Management_System_Component, Authentication_UseCase, Salary_Management_UseCase, Administrator_Actor, Employee_Actor, Login_external, Logout_external},
    associations={Employee_Login, Employee_Logout},
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