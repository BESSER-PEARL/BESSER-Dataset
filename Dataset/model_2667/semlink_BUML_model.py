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
semlink_G = Class(name="semlink::G")
NamedElement = Class(name="NamedElement")
semlink_A = Class(name="semlink::A")
semlink_B = Class(name="semlink::B")
semlink_NamedElement = Class(name="semlink::NamedElement")
semlink_C = Class(name="semlink::C")

# semlink_G class attributes and methods

# NamedElement class attributes and methods

# semlink_A class attributes and methods

# semlink_B class attributes and methods

# semlink_NamedElement class attributes and methods
semlink_NamedElement_name: Property = Property(name="name", type=StringType)
semlink_NamedElement.attributes={semlink_NamedElement_name}

# semlink_C class attributes and methods

# Relationships
subgs1: BinaryAssociation = BinaryAssociation(
    name="subgs1",
    ends={
        Property(name="semlink_G", type=semlink_G, multiplicity=Multiplicity(1, 1)),
        Property(name="semlink_G0", type=semlink_G, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cs6: BinaryAssociation = BinaryAssociation(
    name="cs6",
    ends={
        Property(name="semlink_A7", type=semlink_C, multiplicity=Multiplicity(0, 9999)),
        Property(name="semlink_C8", type=semlink_A, multiplicity=Multiplicity(1, 1))
    }
)
bs9: BinaryAssociation = BinaryAssociation(
    name="bs9",
    ends={
        Property(name="semlink_B", type=semlink_A, multiplicity=Multiplicity(1, 1)),
        Property(name="semlink_A10", type=semlink_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
a11: BinaryAssociation = BinaryAssociation(
    name="a11",
    ends={
        Property(name="semlink_A13", type=semlink_B, multiplicity=Multiplicity(1, 1)),
        Property(name="semlink_B12", type=semlink_A, multiplicity=Multiplicity(0, 1))
    }
)
c14: BinaryAssociation = BinaryAssociation(
    name="c14",
    ends={
        Property(name="semlink_C16", type=semlink_B, multiplicity=Multiplicity(1, 1)),
        Property(name="semlink_B15", type=semlink_C, multiplicity=Multiplicity(0, 1))
    }
)
as2: BinaryAssociation = BinaryAssociation(
    name="as2",
    ends={
        Property(name="semlink_A", type=semlink_G, multiplicity=Multiplicity(1, 1)),
        Property(name="semlink_G3", type=semlink_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cs4: BinaryAssociation = BinaryAssociation(
    name="cs4",
    ends={
        Property(name="semlink_C", type=semlink_G, multiplicity=Multiplicity(1, 1)),
        Property(name="semlink_G5", type=semlink_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_semlink_G_NamedElement = Generalization(general=NamedElement, specific=semlink_G)
gen_semlink_C_NamedElement = Generalization(general=NamedElement, specific=semlink_C)
gen_semlink_B_NamedElement = Generalization(general=NamedElement, specific=semlink_B)
gen_semlink_A_NamedElement = Generalization(general=NamedElement, specific=semlink_A)

# Domain Model
domain_model = DomainModel(
    name="semlink",
    types={semlink_G, NamedElement, semlink_A, semlink_B, semlink_NamedElement, semlink_C},
    associations={subgs1, cs6, bs9, a11, c14, as2, cs4},
    generalizations={gen_semlink_G_NamedElement, gen_semlink_C_NamedElement, gen_semlink_B_NamedElement, gen_semlink_A_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)