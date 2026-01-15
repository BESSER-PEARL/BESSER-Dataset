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
cde_Company = Class(name="cde::Company")
cde_Department = Class(name="cde::Department")
cde_Employee = Class(name="cde::Employee")

# cde_Company class attributes and methods
cde_Company_name: Property = Property(name="name", type=StringType)
cde_Company.attributes={cde_Company_name}

# cde_Department class attributes and methods
cde_Department_name: Property = Property(name="name", type=StringType)
cde_Department.attributes={cde_Department_name}

# cde_Employee class attributes and methods
cde_Employee_name: Property = Property(name="name", type=StringType)
cde_Employee_address: Property = Property(name="address", type=StringType)
cde_Employee.attributes={cde_Employee_name, cde_Employee_address}

# Relationships
belongs0: BinaryAssociation = BinaryAssociation(
    name="belongs0",
    ends={
        Property(name="cde_Department", type=cde_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="cde_Company", type=cde_Department, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
works1: BinaryAssociation = BinaryAssociation(
    name="works1",
    ends={
        Property(name="cde_Employee", type=cde_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="cde_Department2", type=cde_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="cde",
    types={cde_Company, cde_Department, cde_Employee},
    associations={belongs0, works1},
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