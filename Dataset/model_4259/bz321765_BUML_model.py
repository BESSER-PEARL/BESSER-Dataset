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
bz321765_Employee = Class(name="bz321765::Employee")
bz321765_EmployeePK = Class(name="bz321765::EmployeePK")

# bz321765_Employee class attributes and methods
bz321765_Employee_title: Property = Property(name="title", type=StringType)
bz321765_Employee_salary: Property = Property(name="salary", type=StringType)
bz321765_Employee.attributes={bz321765_Employee_title, bz321765_Employee_salary}

# bz321765_EmployeePK class attributes and methods
bz321765_EmployeePK_id: Property = Property(name="id", type=StringType)
bz321765_EmployeePK_firstName: Property = Property(name="firstName", type=StringType)
bz321765_EmployeePK_lastName: Property = Property(name="lastName", type=StringType)
bz321765_EmployeePK.attributes={bz321765_EmployeePK_id, bz321765_EmployeePK_lastName, bz321765_EmployeePK_firstName}

# Relationships
employeePK0: BinaryAssociation = BinaryAssociation(
    name="employeePK0",
    ends={
        Property(name="bz321765_EmployeePK", type=bz321765_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="bz321765_Employee", type=bz321765_EmployeePK, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="bz321765",
    types={bz321765_Employee, bz321765_EmployeePK},
    associations={employeePK0},
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