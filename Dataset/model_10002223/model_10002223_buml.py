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
DaysAttended = Class(name="DaysAttended")
Salary = Class(name="Salary")
Work_days = Class(name="Work_days")

# Login class attributes and methods
Login_User_Name: Property = Property(name="User_Name", type=StringType)
Login_Password: Property = Property(name="Password", type=StringType)
Login.attributes={Login_Password, Login_User_Name}

# Employee class attributes and methods
Employee_Emp_Id: Property = Property(name="Emp_Id", type=StringType)
Employee_Emp_Name: Property = Property(name="Emp_Name", type=StringType)
Employee_Emp_FName: Property = Property(name="Emp_FName", type=StringType)
Employee.attributes={Employee_Emp_FName, Employee_Emp_Name, Employee_Emp_Id}

# DaysAttended class attributes and methods
DaysAttended_Emp_Id: Property = Property(name="Emp_Id", type=StringType)
DaysAttended_Emp_BasicSalary: Property = Property(name="Emp_BasicSalary", type=StringType)
DaysAttended_Additional_hours__: Property = Property(name="Additional_hours__", type=StringType)
DaysAttended.attributes={DaysAttended_Additional_hours__, DaysAttended_Emp_BasicSalary, DaysAttended_Emp_Id}

# Salary class attributes and methods
Salary_Emp_Id: Property = Property(name="Emp_Id", type=StringType)
Salary_Days_attended: Property = Property(name="Days_attended", type=IntegerType)
Salary_Net_Salary: Property = Property(name="Net_Salary", type=StringType)
Salary_Bonus__: Property = Property(name="Bonus__", type=StringType)
Salary.attributes={Salary_Bonus__, Salary_Days_attended, Salary_Emp_Id, Salary_Net_Salary}

# Work_days class attributes and methods
Work_days__No__of_working_days_: Property = Property(name="_No__of_working_days_", type=IntegerType)
Work_days_Days_Attended: Property = Property(name="Days_Attended", type=IntegerType)
Work_days.attributes={Work_days_Days_Attended, Work_days__No__of_working_days_}

# Relationships
Login_Employee: BinaryAssociation = BinaryAssociation(
    name="Login_Employee",
    ends={
        Property(name="employee0", type=Employee, multiplicity=Multiplicity(0, 9999)),
        Property(name="login1", type=Login, multiplicity=Multiplicity(1, 1))
    }
)
Employee_DaysAttended: BinaryAssociation = BinaryAssociation(
    name="Employee_DaysAttended",
    ends={
        Property(name="daysAttended2", type=DaysAttended, multiplicity=Multiplicity(0, 9999)),
        Property(name="employee3", type=Employee, multiplicity=Multiplicity(1, 1))
    }
)
DaysAttended_Work_days: BinaryAssociation = BinaryAssociation(
    name="DaysAttended_Work_days",
    ends={
        Property(name="work_days4", type=Work_days, multiplicity=Multiplicity(0, 9999)),
        Property(name="daysAttended5", type=DaysAttended, multiplicity=Multiplicity(0, 9999))
    }
)
Work_days_Salary: BinaryAssociation = BinaryAssociation(
    name="Work_days_Salary",
    ends={
        Property(name="salary6", type=Salary, multiplicity=Multiplicity(0, 9999)),
        Property(name="work_days7", type=Work_days, multiplicity=Multiplicity(0, 9999))
    }
)
Employee_Salary: BinaryAssociation = BinaryAssociation(
    name="Employee_Salary",
    ends={
        Property(name="salary8", type=Salary, multiplicity=Multiplicity(1, 1)),
        Property(name="employee9", type=Employee, multiplicity=Multiplicity(1, 1))
    }
)
Employee_Salary2: BinaryAssociation = BinaryAssociation(
    name="Employee_Salary2",
    ends={
        Property(name="salary10", type=Salary, multiplicity=Multiplicity(1, 1)),
        Property(name="employee11", type=Employee, multiplicity=Multiplicity(0, 9999))
    }
)
DaysAttended_Salary: BinaryAssociation = BinaryAssociation(
    name="DaysAttended_Salary",
    ends={
        Property(name="salary12", type=Salary, multiplicity=Multiplicity(1, 1)),
        Property(name="daysAttended13", type=DaysAttended, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_xkuVUJFVEeiZHpoWpW9xEA",
    types={Login, Employee, DaysAttended, Salary, Work_days},
    associations={Login_Employee, Employee_DaysAttended, DaysAttended_Work_days, Work_days_Salary, Employee_Salary, Employee_Salary2, DaysAttended_Salary},
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