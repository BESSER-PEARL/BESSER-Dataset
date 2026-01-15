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
properties_Department = Class(name="properties::Department")
properties_Employee = Class(name="properties::Employee")

# properties_Department class attributes and methods

# properties_Employee class attributes and methods

# Relationships
hasEmployee0: BinaryAssociation = BinaryAssociation(
    name="hasEmployee0",
    ends={
        Property(name="Employee", type=properties_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="hasDepartment", type=properties_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hasDepartment1: BinaryAssociation = BinaryAssociation(
    name="hasDepartment1",
    ends={
        Property(name="Department", type=properties_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="hasEmployee", type=properties_Department, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="properties",
    types={properties_Department, properties_Employee},
    associations={hasEmployee0, hasDepartment1},
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