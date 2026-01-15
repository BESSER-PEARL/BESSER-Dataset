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
ce_Company = Class(name="ce::Company")
ce_Employee = Class(name="ce::Employee")

# ce_Company class attributes and methods
ce_Company_name: Property = Property(name="name", type=StringType)
ce_Company.attributes={ce_Company_name}

# ce_Employee class attributes and methods
ce_Employee_name: Property = Property(name="name", type=StringType)
ce_Employee_address: Property = Property(name="address", type=StringType)
ce_Employee_department: Property = Property(name="department", type=StringType)
ce_Employee.attributes={ce_Employee_department, ce_Employee_name, ce_Employee_address}

# Relationships
works0: BinaryAssociation = BinaryAssociation(
    name="works0",
    ends={
        Property(name="ce_Employee", type=ce_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="ce_Company", type=ce_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="ce",
    types={ce_Company, ce_Employee},
    associations={works0},
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