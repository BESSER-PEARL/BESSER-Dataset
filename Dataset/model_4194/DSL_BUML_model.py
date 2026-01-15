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
dSL_Model = Class(name="dSL::Model")
dSL_Greeting = Class(name="dSL::Greeting")
dSL_EClass = Class(name="dSL::EClass")

# dSL_Model class attributes and methods

# dSL_Greeting class attributes and methods

# dSL_EClass class attributes and methods

# Relationships
greetings0: BinaryAssociation = BinaryAssociation(
    name="greetings0",
    ends={
        Property(name="dSL_Greeting", type=dSL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="dSL_Model", type=dSL_Greeting, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eClass1: BinaryAssociation = BinaryAssociation(
    name="eClass1",
    ends={
        Property(name="dSL_EClass", type=dSL_Greeting, multiplicity=Multiplicity(1, 1)),
        Property(name="dSL_Greeting2", type=dSL_EClass, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="dSL",
    types={dSL_Model, dSL_Greeting, dSL_EClass},
    associations={greetings0, eClass1},
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