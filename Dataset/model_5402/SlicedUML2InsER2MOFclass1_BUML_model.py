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
UML2_Reception = Class(name="UML2::Reception")
UML2_Class = Class(name="UML2::Class")

# UML2_Reception class attributes and methods

# UML2_Class class attributes and methods
UML2_Class_isActive: Property = Property(name="isActive", type=BooleanType)
UML2_Class.attributes={UML2_Class_isActive}

# Relationships
ownedReception0: BinaryAssociation = BinaryAssociation(
    name="ownedReception0",
    ends={
        Property(name="UML2_Reception", type=UML2_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Class", type=UML2_Reception, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="UML2",
    types={UML2_Reception, UML2_Class},
    associations={ownedReception0},
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