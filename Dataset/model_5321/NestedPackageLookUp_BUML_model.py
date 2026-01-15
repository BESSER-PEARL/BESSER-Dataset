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
root_RootTest = Class(name="root::RootTest")
NestedTest = Class(name="NestedTest")
root_nested_NestedTest = Class(name="root::nested::NestedTest")

# root_RootTest class attributes and methods

# NestedTest class attributes and methods

# root_nested_NestedTest class attributes and methods

# Relationships
nested0: BinaryAssociation = BinaryAssociation(
    name="nested0",
    ends={
        Property(name="NestedTest", type=root_RootTest, multiplicity=Multiplicity(1, 1)),
        Property(name="root_RootTest", type=NestedTest, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="root",
    types={root_RootTest, NestedTest, root_nested_NestedTest},
    associations={nested0},
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