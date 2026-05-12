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
Scanner = Class(name="Scanner")
Error_code = Class(name="Error_code")
History = Class(name="History")
Employee_Management_System_Component = Class(name="Employee_Management_System_Component")
Authentication_UseCase = Class(name="Authentication_UseCase")
Salary_Management_UseCase = Class(name="Salary_Management_UseCase")
Administrator_Actor = Class(name="Administrator_Actor")
Employee_Actor = Class(name="Employee_Actor")
Login_external = Class(name="Login_external")
Logout_external = Class(name="Logout_external")

# Scanner class attributes and methods
Scanner_code_Id: Property = Property(name="code_Id", type=IntegerType)
Scanner_code_serial: Property = Property(name="code_serial", type=StringType)
Scanner_code_serial1: Property = Property(name="code_serial1", type=StringType)
Scanner_code_MOB: Property = Property(name="code_MOB", type=DateType)
Scanner_Code_EOD: Property = Property(name="Code_EOD", type=DateType)
Scanner_Code_amount: Property = Property(name="Code_amount", type=FloatType)
Scanner.attributes={Scanner_code_serial1, Scanner_Code_amount, Scanner_code_Id, Scanner_code_serial, Scanner_code_MOB, Scanner_Code_EOD}

# Error_code class attributes and methods
Error_code_Code_Id: Property = Property(name="Code_Id", type=StringType)
Error_code_Code_serial: Property = Property(name="Code_serial", type=StringType)
Error_code_Code_Exp: Property = Property(name="Code_Exp", type=StringType)
Error_code.attributes={Error_code_Code_Exp, Error_code_Code_serial, Error_code_Code_Id}

# History class attributes and methods
History_Code_id: Property = Property(name="Code_id", type=StringType)
History_Code_amount: Property = Property(name="Code_amount", type=StringType)
History.attributes={History_Code_amount, History_Code_id}

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
    name="fc1530b1_b071_4637_bab4_bef815e0aacc",
    types={Scanner, Error_code, History, Employee_Management_System_Component, Authentication_UseCase, Salary_Management_UseCase, Administrator_Actor, Employee_Actor, Login_external, Logout_external},
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