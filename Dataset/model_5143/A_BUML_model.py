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
a_Root = Class(name="a::Root")
a_A = Class(name="a::A")
a_B = Class(name="a::B")

# a_Root class attributes and methods
a_Root_visible: Property = Property(name="visible", type=BooleanType)
a_Root.attributes={a_Root_visible}

# a_A class attributes and methods
a_A_tob: Property = Property(name="tob", type=StringType)
a_A_names: Property = Property(name="names", type=StringType)
a_A.attributes={a_A_tob, a_A_names}

# a_B class attributes and methods
a_B_name: Property = Property(name="name", type=StringType)
a_B.attributes={a_B_name}

# Relationships
refa0: BinaryAssociation = BinaryAssociation(
    name="refa0",
    ends={
        Property(name="a_A", type=a_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="a_Root", type=a_A, multiplicity=Multiplicity(0, 1))
    }
)
a1: BinaryAssociation = BinaryAssociation(
    name="a1",
    ends={
        Property(name="a_A3", type=a_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="a_Root2", type=a_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
b4: BinaryAssociation = BinaryAssociation(
    name="b4",
    ends={
        Property(name="a_B", type=a_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="a_Root5", type=a_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="a",
    types={a_Root, a_A, a_B},
    associations={refa0, a1, b4},
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