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
TypeB_BStringElement = Class(name="TypeB::BStringElement")
TypeB_BDoubleElement = Class(name="TypeB::BDoubleElement")

# TypeB_BStringElement class attributes and methods
TypeB_BStringElement_stringValue: Property = Property(name="stringValue", type=StringType)
TypeB_BStringElement.attributes={TypeB_BStringElement_stringValue}

# TypeB_BDoubleElement class attributes and methods
TypeB_BDoubleElement_doubleValue: Property = Property(name="doubleValue", type=FloatType)
TypeB_BDoubleElement.attributes={TypeB_BDoubleElement_doubleValue}

# Domain Model
domain_model = DomainModel(
    name="TypeB",
    types={TypeB_BStringElement, TypeB_BDoubleElement},
    associations={},
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