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
mpupkb_NamedElement = Class(name="mpupkb::NamedElement", is_abstract=True)
mpupkb_Comment = Class(name="mpupkb::Comment")
mpupkb_Thing = Class(name="mpupkb::Thing")
NamedElement = Class(name="NamedElement")
mpupkb_Own = Class(name="mpupkb::Own")

# mpupkb_NamedElement class attributes and methods
mpupkb_NamedElement_name: Property = Property(name="name", type=StringType)
mpupkb_NamedElement.attributes={mpupkb_NamedElement_name}

# mpupkb_Comment class attributes and methods
mpupkb_Comment_content: Property = Property(name="content", type=StringType)
mpupkb_Comment.attributes={mpupkb_Comment_content}

# mpupkb_Thing class attributes and methods
mpupkb_Thing_id: Property = Property(name="id", type=IntegerType)
mpupkb_Thing.attributes={mpupkb_Thing_id}

# NamedElement class attributes and methods

# mpupkb_Own class attributes and methods
mpupkb_Own_since: Property = Property(name="since", type=StringType)
mpupkb_Own_ownerName: Property = Property(name="ownerName", type=StringType)
mpupkb_Own.attributes={mpupkb_Own_ownerName, mpupkb_Own_since}

# Relationships
comment2: BinaryAssociation = BinaryAssociation(
    name="comment2",
    ends={
        Property(name="mpupkb_Comment", type=mpupkb_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="mpupkb_NamedElement", type=mpupkb_Comment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownership0: BinaryAssociation = BinaryAssociation(
    name="ownership0",
    ends={
        Property(name="Own", type=mpupkb_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="thing", type=mpupkb_Own, multiplicity=Multiplicity(0, 1))
    }
)
ownershi1: BinaryAssociation = BinaryAssociation(
    name="ownershi1",
    ends={
        Property(name="mpupkb_Own", type=mpupkb_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="mpupkb_Thing", type=mpupkb_Own, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thing3: BinaryAssociation = BinaryAssociation(
    name="thing3",
    ends={
        Property(name="Thing", type=mpupkb_Own, multiplicity=Multiplicity(1, 1)),
        Property(name="ownership", type=mpupkb_Thing, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_mpupkb_Own_NamedElement = Generalization(general=NamedElement, specific=mpupkb_Own)
gen_mpupkb_Thing_NamedElement = Generalization(general=NamedElement, specific=mpupkb_Thing)

# Domain Model
domain_model = DomainModel(
    name="mpupkb",
    types={mpupkb_NamedElement, mpupkb_Comment, mpupkb_Thing, NamedElement, mpupkb_Own},
    associations={comment2, ownership0, ownershi1, thing3},
    generalizations={gen_mpupkb_Own_NamedElement, gen_mpupkb_Thing_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)