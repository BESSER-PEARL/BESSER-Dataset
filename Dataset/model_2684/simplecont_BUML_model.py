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
simplecont_A = Class(name="simplecont::A")
simplecont_X = Class(name="simplecont::X")
simplecont_B = Class(name="simplecont::B")
simplecont_C = Class(name="simplecont::C")

# simplecont_A class attributes and methods
simplecont_A_name: Property = Property(name="name", type=StringType)
simplecont_A.attributes={simplecont_A_name}

# simplecont_X class attributes and methods

# simplecont_B class attributes and methods
simplecont_B_name: Property = Property(name="name", type=StringType)
simplecont_B.attributes={simplecont_B_name}

# simplecont_C class attributes and methods
simplecont_C_id: Property = Property(name="id", type=StringType)
simplecont_C.attributes={simplecont_C_id}

# Relationships
b3: BinaryAssociation = BinaryAssociation(
    name="b3",
    ends={
        Property(name="simplecont_B5", type=simplecont_C, multiplicity=Multiplicity(1, 1)),
        Property(name="simplecont_C4", type=simplecont_B, multiplicity=Multiplicity(0, 1))
    }
)
as6: BinaryAssociation = BinaryAssociation(
    name="as6",
    ends={
        Property(name="simplecont_A7", type=simplecont_X, multiplicity=Multiplicity(1, 1)),
        Property(name="simplecont_X", type=simplecont_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bs0: BinaryAssociation = BinaryAssociation(
    name="bs0",
    ends={
        Property(name="simplecont_B", type=simplecont_A, multiplicity=Multiplicity(1, 1)),
        Property(name="simplecont_A", type=simplecont_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cs1: BinaryAssociation = BinaryAssociation(
    name="cs1",
    ends={
        Property(name="simplecont_C", type=simplecont_A, multiplicity=Multiplicity(1, 1)),
        Property(name="simplecont_A2", type=simplecont_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="simplecont",
    types={simplecont_A, simplecont_X, simplecont_B, simplecont_C},
    associations={b3, as6, bs0, cs1},
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