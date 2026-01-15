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
employeeDsl_EmployeeContainer = Class(name="employeeDsl::EmployeeContainer")
employeeDsl_Employee = Class(name="employeeDsl::Employee")

# employeeDsl_EmployeeContainer class attributes and methods

# employeeDsl_Employee class attributes and methods
employeeDsl_Employee_ID: Property = Property(name="ID", type=IntegerType)
employeeDsl_Employee_name: Property = Property(name="name", type=StringType)
employeeDsl_Employee_salary: Property = Property(name="salary", type=IntegerType)
employeeDsl_Employee.attributes={employeeDsl_Employee_salary, employeeDsl_Employee_ID, employeeDsl_Employee_name}

# Relationships
employees0: BinaryAssociation = BinaryAssociation(
    name="employees0",
    ends={
        Property(name="employeeDsl_Employee", type=employeeDsl_EmployeeContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="employeeDsl_EmployeeContainer", type=employeeDsl_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="employeeDsl",
    types={employeeDsl_EmployeeContainer, employeeDsl_Employee},
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