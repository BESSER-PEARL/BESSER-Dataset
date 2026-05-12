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
Days_Attended = Class(name="Days_Attended")
Leave = Class(name="Leave")
Admin = Class(name="Admin")

# Login class attributes and methods
Login_Username: Property = Property(name="Username", type=StringType)
Login_Password: Property = Property(name="Password", type=StringType)
Login.attributes={Login_Password, Login_Username}

# Employee class attributes and methods
Employee_EmployeeId: Property = Property(name="EmployeeId", type=StringType)
Employee_EmplyeeName: Property = Property(name="EmplyeeName", type=StringType)
Employee_EmployeePhoneNumber: Property = Property(name="EmployeePhoneNumber", type=IntegerType)
Employee_EmployeeEmail: Property = Property(name="EmployeeEmail", type=StringType)
Employee.attributes={Employee_EmplyeeName, Employee_EmployeeId, Employee_EmployeePhoneNumber, Employee_EmployeeEmail}

# Salary class attributes and methods
Salary_EmployeeID: Property = Property(name="EmployeeID", type=StringType)
Salary_DaysAttended: Property = Property(name="DaysAttended", type=IntegerType)
Salary_Bonus: Property = Property(name="Bonus", type=IntegerType)
Salary_NetSalary: Property = Property(name="NetSalary", type=IntegerType)
Salary.attributes={Salary_DaysAttended, Salary_NetSalary, Salary_Bonus, Salary_EmployeeID}

# Days_Attended class attributes and methods
Days_Attended_EmployeeId: Property = Property(name="EmployeeId", type=StringType)
Days_Attended_EmployeeBasicSalary: Property = Property(name="EmployeeBasicSalary", type=IntegerType)
Days_Attended_OverTime: Property = Property(name="OverTime", type=IntegerType)
Days_Attended_Total_no__of_workingdays: Property = Property(name="Total_no__of_workingdays", type=IntegerType)
Days_Attended_Days_attended: Property = Property(name="Days_attended", type=IntegerType)
Days_Attended.attributes={Days_Attended_Total_no__of_workingdays, Days_Attended_OverTime, Days_Attended_EmployeeId, Days_Attended_Days_attended, Days_Attended_EmployeeBasicSalary}

# Leave class attributes and methods
Leave_Leave_Detail: Property = Property(name="Leave_Detail", type=StringType)
Leave_Leave_NoOfDays: Property = Property(name="Leave_NoOfDays", type=IntegerType)
Leave_attribute: Property = Property(name="attribute", type=StringType)
Leave.attributes={Leave_Leave_Detail, Leave_attribute, Leave_Leave_NoOfDays}

# Admin class attributes and methods
Admin_Name: Property = Property(name="Name", type=StringType)
Admin_Email: Property = Property(name="Email", type=StringType)
Admin.attributes={Admin_Email, Admin_Name}

# Relationships
Login_Employee: BinaryAssociation = BinaryAssociation(
    name="Login_Employee",
    ends={
        Property(name="employee0", type=Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="login1", type=Login, multiplicity=Multiplicity(1, 1))
    }
)
Employee_Salary: BinaryAssociation = BinaryAssociation(
    name="Employee_Salary",
    ends={
        Property(name="salary2", type=Salary, multiplicity=Multiplicity(0, 1)),
        Property(name="employee3", type=Employee, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Days_Attended: BinaryAssociation = BinaryAssociation(
    name="Employee_Days_Attended",
    ends={
        Property(name="days_Attended4", type=Days_Attended, multiplicity=Multiplicity(0, 9999)),
        Property(name="employee5", type=Employee, multiplicity=Multiplicity(1, 1))
    }
)
Employee_Leave: BinaryAssociation = BinaryAssociation(
    name="Employee_Leave",
    ends={
        Property(name="leave6", type=Leave, multiplicity=Multiplicity(1, 1)),
        Property(name="employee7", type=Employee, multiplicity=Multiplicity(1, 1))
    }
)
Admin_Employee: BinaryAssociation = BinaryAssociation(
    name="Admin_Employee",
    ends={
        Property(name="employee8", type=Employee, multiplicity=Multiplicity(0, 9999)),
        Property(name="admin9", type=Admin, multiplicity=Multiplicity(1, 1))
    }
)
Salary_Days_Attended: BinaryAssociation = BinaryAssociation(
    name="Salary_Days_Attended",
    ends={
        Property(name="days_Attended10", type=Days_Attended, multiplicity=Multiplicity(0, 1)),
        Property(name="salary11", type=Salary, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_DLOU4JbbEeiilJ4tAEXZQQ",
    types={Login, Employee, Salary, Days_Attended, Leave, Admin},
    associations={Login_Employee, Employee_Salary, Employee_Days_Attended, Employee_Leave, Admin_Employee, Salary_Days_Attended},
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