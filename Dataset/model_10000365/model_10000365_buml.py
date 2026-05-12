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
Employee_DB = Class(name="Employee_DB")
Administration = Class(name="Administration")
Employee_Actor = Class(name="Employee_Actor")
Log_In_UseCase = Class(name="Log_In_UseCase")
Log_Out_UseCase = Class(name="Log_Out_UseCase")
Notes___Comments_UseCase = Class(name="Notes___Comments_UseCase")
Administrator_Actor = Class(name="Administrator_Actor")
Managing_Users_UseCase = Class(name="Managing_Users_UseCase")
Reporting_UseCase = Class(name="Reporting_UseCase")
Edit__Archive_UseCase = Class(name="Edit__Archive_UseCase")
Print_UseCase = Class(name="Print_UseCase")
Employee_Title__Non_Admin = Class(name="Employee_Title__Non_Admin")

# Employee_DB class attributes and methods
Employee_DB_Name__1st_and_last_: Property = Property(name="Name__1st_and_last_", type=Employee_Actor)
Employee_DB_Username: Property = Property(name="Username", type=Log_In_UseCase)
Employee_DB_Password: Property = Property(name="Password", type=StringType)
Employee_DB_Employee_ID: Property = Property(name="Employee_ID", type=IntegerType)
Employee_DB_Address: Property = Property(name="Address", type=StringType)
Employee_DB_Telephone: Property = Property(name="Telephone", type=IntegerType)
Employee_DB_E_Mail: Property = Property(name="E_Mail", type=StringType)
Employee_DB_Date_of_Birth: Property = Property(name="Date_of_Birth", type=IntegerType)
Employee_DB_SSN: Property = Property(name="SSN", type=IntegerType)
Employee_DB_Title: Property = Property(name="Title", type=Employee_Title__Non_Admin)
Employee_DB_Supervisor: Property = Property(name="Supervisor", type=Administrator_Actor)
Employee_DB_Salary: Property = Property(name="Salary", type=IntegerType)
Employee_DB.attributes={Employee_DB_Employee_ID, Employee_DB_Address, Employee_DB_SSN, Employee_DB_Telephone, Employee_DB_Username, Employee_DB_Salary, Employee_DB_Supervisor, Employee_DB_Name__1st_and_last_, Employee_DB_E_Mail, Employee_DB_Date_of_Birth, Employee_DB_Title, Employee_DB_Password}

# Administration class attributes and methods
Administration_Executive_Director___COO: Property = Property(name="Executive_Director___COO", type=Administrator_Actor)
Administration_Asst__Executive_Director: Property = Property(name="Asst__Executive_Director", type=Administrator_Actor)
Administration_CFO: Property = Property(name="CFO", type=Administrator_Actor)
Administration_Office_Manager: Property = Property(name="Office_Manager", type=Employee_Actor)
Administration.attributes={Administration_CFO, Administration_Executive_Director___COO, Administration_Office_Manager, Administration_Asst__Executive_Director}

# Employee_Actor class attributes and methods

# Log_In_UseCase class attributes and methods

# Log_Out_UseCase class attributes and methods

# Notes___Comments_UseCase class attributes and methods

# Administrator_Actor class attributes and methods

# Managing_Users_UseCase class attributes and methods

# Reporting_UseCase class attributes and methods

# Edit__Archive_UseCase class attributes and methods

# Print_UseCase class attributes and methods

# Employee_Title__Non_Admin class attributes and methods
Employee_Title__Non_Admin_Teacher: Property = Property(name="Teacher", type=Employee_Actor)
Employee_Title__Non_Admin_Cook: Property = Property(name="Cook", type=Employee_Actor)
Employee_Title__Non_Admin_Assistant_Teacher: Property = Property(name="Assistant_Teacher", type=Employee_Actor)
Employee_Title__Non_Admin_Maintenance: Property = Property(name="Maintenance", type=Employee_Actor)
Employee_Title__Non_Admin_Community_Service: Property = Property(name="Community_Service", type=StringType)
Employee_Title__Non_Admin_Work_Study: Property = Property(name="Work_Study", type=StringType)
Employee_Title__Non_Admin.attributes={Employee_Title__Non_Admin_Work_Study, Employee_Title__Non_Admin_Community_Service, Employee_Title__Non_Admin_Maintenance, Employee_Title__Non_Admin_Teacher, Employee_Title__Non_Admin_Cook, Employee_Title__Non_Admin_Assistant_Teacher}

# Relationships
Employee_Log_In: BinaryAssociation = BinaryAssociation(
    name="Employee_Log_In",
    ends={
        Property(name="log_In0", type=Log_In_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="employee1", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Log_Out: BinaryAssociation = BinaryAssociation(
    name="Employee_Log_Out",
    ends={
        Property(name="log_Out2", type=Log_Out_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="employee3", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Note___Comments: BinaryAssociation = BinaryAssociation(
    name="Employee_Note___Comments",
    ends={
        Property(name="note___Comments4", type=Notes___Comments_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="employee5", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Log_In: BinaryAssociation = BinaryAssociation(
    name="Administrator_Log_In",
    ends={
        Property(name="log_In6", type=Log_In_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator7", type=Administrator_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Log_Out: BinaryAssociation = BinaryAssociation(
    name="Administrator_Log_Out",
    ends={
        Property(name="log_Out8", type=Log_Out_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator9", type=Administrator_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Reporting: BinaryAssociation = BinaryAssociation(
    name="Administrator_Reporting",
    ends={
        Property(name="reporting10", type=Reporting_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator11", type=Administrator_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Edit___Print: BinaryAssociation = BinaryAssociation(
    name="Administrator_Edit___Print",
    ends={
        Property(name="edit___Print12", type=Edit__Archive_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator13", type=Administrator_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Note___Comments: BinaryAssociation = BinaryAssociation(
    name="Administrator_Note___Comments",
    ends={
        Property(name="note___Comments14", type=Notes___Comments_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator15", type=Administrator_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Archive___Save: BinaryAssociation = BinaryAssociation(
    name="Administrator_Archive___Save",
    ends={
        Property(name="archive___Save16", type=Print_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator17", type=Administrator_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Managing_Users: BinaryAssociation = BinaryAssociation(
    name="Administrator_Managing_Users",
    ends={
        Property(name="managing_Users18", type=Managing_Users_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator19", type=Administrator_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Print: BinaryAssociation = BinaryAssociation(
    name="Employee_Print",
    ends={
        Property(name="print20", type=Print_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="employee21", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Employee_DB_Employee_Title__Non_Admin: BinaryAssociation = BinaryAssociation(
    name="Employee_DB_Employee_Title__Non_Admin",
    ends={
        Property(name="employee_Title__Non_Admin22", type=Employee_Title__Non_Admin, multiplicity=Multiplicity(0, 1)),
        Property(name="employee_DB23", type=Employee_DB, multiplicity=Multiplicity(0, 1))
    }
)
Employee_DB_Administration: BinaryAssociation = BinaryAssociation(
    name="Employee_DB_Administration",
    ends={
        Property(name="administration24", type=Administration, multiplicity=Multiplicity(0, 1)),
        Property(name="employee_DB25", type=Employee_DB, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_2d5d0efe_4a85_427d_a8e9_53a4d43ecdd9",
    types={Employee_DB, Administration, Employee_Actor, Log_In_UseCase, Log_Out_UseCase, Notes___Comments_UseCase, Administrator_Actor, Managing_Users_UseCase, Reporting_UseCase, Edit__Archive_UseCase, Print_UseCase, Employee_Title__Non_Admin},
    associations={Employee_Log_In, Employee_Log_Out, Employee_Note___Comments, Administrator_Log_In, Administrator_Log_Out, Administrator_Reporting, Administrator_Edit___Print, Administrator_Note___Comments, Administrator_Archive___Save, Administrator_Managing_Users, Employee_Print, Employee_DB_Employee_Title__Non_Admin, Employee_DB_Administration},
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