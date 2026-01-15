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
testtypesystem_State = Class(name="testtypesystem::State")
testtypesystem_Assignment = Class(name="testtypesystem::Assignment")
testtypesystem_Expression = Class(name="testtypesystem::Expression", is_abstract=True)
testtypesystem_Value = Class(name="testtypesystem::Value", is_abstract=True)

# testtypesystem_State class attributes and methods

# testtypesystem_Assignment class attributes and methods

# testtypesystem_Expression class attributes and methods

# testtypesystem_Value class attributes and methods

# Relationships
value0: BinaryAssociation = BinaryAssociation(
    name="value0",
    ends={
        Property(name="testtypesystem_Expression", type=testtypesystem_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="testtypesystem_Assignment", type=testtypesystem_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="testtypesystem",
    types={testtypesystem_State, testtypesystem_Assignment, testtypesystem_Expression, testtypesystem_Value},
    associations={value0},
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