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
Employees_EmployeeContainer = Class(name="Employees::EmployeeContainer")
Employees_Employee = Class(name="Employees::Employee")

# Employees_EmployeeContainer class attributes and methods

# Employees_Employee class attributes and methods
Employees_Employee_name: Property = Property(name="name", type=StringType)
Employees_Employee_salary: Property = Property(name="salary", type=IntegerType)
Employees_Employee_ID: Property = Property(name="ID", type=IntegerType)
Employees_Employee.attributes={Employees_Employee_name, Employees_Employee_ID, Employees_Employee_salary}

# Relationships
employees0: BinaryAssociation = BinaryAssociation(
    name="employees0",
    ends={
        Property(name="Employees_Employee", type=Employees_EmployeeContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="Employees_EmployeeContainer", type=Employees_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="Employees",
    types={Employees_EmployeeContainer, Employees_Employee},
    associations={employees0},
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