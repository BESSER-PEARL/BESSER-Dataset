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

# employee_Employee class attributes and methods
employee_Employee_name: Property = Property(name="name", type=StringType)
employee_Employee_accounts: Property = Property(name="accounts", type=StringType)
employee_Employee.attributes={employee_Employee_name, employee_Employee_accounts}

# Relationships
partner1: BinaryAssociation = BinaryAssociation(
    name="partner1",
    ends={
        Property(name="employee_Employee", type=employee_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Employee0", type=employee_Employee, multiplicity=Multiplicity(0, 1))
    }
)
manages3: BinaryAssociation = BinaryAssociation(
    name="manages3",
    ends={
        Property(name="employee_Employee4", type=employee_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Employee2", type=employee_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refManages6: BinaryAssociation = BinaryAssociation(
    name="refManages6",
    ends={
        Property(name="employee_Employee7", type=employee_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Employee5", type=employee_Employee, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="employee",
    types={employee_Employee},
    associations={partner1, manages3, refManages6},
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