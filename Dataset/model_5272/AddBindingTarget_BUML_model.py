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
AddBindingTarget_Type1 = Class(name="AddBindingTarget::Type1")
AddBindingTarget_Type2 = Class(name="AddBindingTarget::Type2")
AddBindingTarget_Type3 = Class(name="AddBindingTarget::Type3")

# AddBindingTarget_Type1 class attributes and methods
AddBindingTarget_Type1_name: Property = Property(name="name", type=StringType)
AddBindingTarget_Type1.attributes={AddBindingTarget_Type1_name}

# AddBindingTarget_Type2 class attributes and methods
AddBindingTarget_Type2_name: Property = Property(name="name", type=StringType)
AddBindingTarget_Type2.attributes={AddBindingTarget_Type2_name}

# AddBindingTarget_Type3 class attributes and methods

# Relationships
b0: BinaryAssociation = BinaryAssociation(
    name="b0",
    ends={
        Property(name="AddBindingTarget_Type2", type=AddBindingTarget_Type1, multiplicity=Multiplicity(1, 1)),
        Property(name="AddBindingTarget_Type1", type=AddBindingTarget_Type2, multiplicity=Multiplicity(0, 1))
    }
)
refToType31: BinaryAssociation = BinaryAssociation(
    name="refToType31",
    ends={
        Property(name="AddBindingTarget_Type3", type=AddBindingTarget_Type1, multiplicity=Multiplicity(1, 1)),
        Property(name="AddBindingTarget_Type12", type=AddBindingTarget_Type3, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="AddBindingTarget",
    types={AddBindingTarget_Type1, AddBindingTarget_Type2, AddBindingTarget_Type3},
    associations={b0, refToType31},
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