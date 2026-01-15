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
employee_Employee = Class(name="employee::Employee")
employee_Department = Class(name="employee::Department")

# employee_Employee class attributes and methods
employee_Employee_name: Property = Property(name="name", type=StringType)
employee_Employee_salary: Property = Property(name="salary", type=StringType)
employee_Employee_age: Property = Property(name="age", type=StringType)
employee_Employee_hireDate: Property = Property(name="hireDate", type=StringType)
employee_Employee.attributes={employee_Employee_hireDate, employee_Employee_name, employee_Employee_salary, employee_Employee_age}

# employee_Department class attributes and methods
employee_Department_name: Property = Property(name="name", type=StringType)
employee_Department.attributes={employee_Department_name}

# Relationships
employees0: BinaryAssociation = BinaryAssociation(
    name="employees0",
    ends={
        Property(name="employee_Employee", type=employee_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Department", type=employee_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="employee",
    types={employee_Employee, employee_Department},
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