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
helloworld150_World = Class(name="helloworld150::World")
helloworld150_Thing = Class(name="helloworld150::Thing")
helloworld150_Own = Class(name="helloworld150::Own")
helloworld150_NamedElement = Class(name="helloworld150::NamedElement", is_abstract=True)
helloworld150_Person = Class(name="helloworld150::Person")
helloworld150_Profession = Class(name="helloworld150::Profession")
NamedElement = Class(name="NamedElement")
helloworld150_Comment = Class(name="helloworld150::Comment")

# helloworld150_World class attributes and methods

# helloworld150_Thing class attributes and methods
helloworld150_Thing_id: Property = Property(name="id", type=IntegerType)
helloworld150_Thing.attributes={helloworld150_Thing_id}

# helloworld150_Own class attributes and methods
helloworld150_Own_since: Property = Property(name="since", type=StringType)
helloworld150_Own_ownerName: Property = Property(name="ownerName", type=StringType)
helloworld150_Own.attributes={helloworld150_Own_since, helloworld150_Own_ownerName}

# helloworld150_NamedElement class attributes and methods
helloworld150_NamedElement_name: Property = Property(name="name", type=StringType)
helloworld150_NamedElement.attributes={helloworld150_NamedElement_name}

# helloworld150_Person class attributes and methods
helloworld150_Person_forName: Property = Property(name="forName", type=StringType)
helloworld150_Person_birthDate: Property = Property(name="birthDate", type=StringType)
helloworld150_Person.attributes={helloworld150_Person_birthDate, helloworld150_Person_forName}

# helloworld150_Profession class attributes and methods
helloworld150_Profession_name: Property = Property(name="name", type=StringType)
helloworld150_Profession.attributes={helloworld150_Profession_name}

# NamedElement class attributes and methods

# helloworld150_Comment class attributes and methods
helloworld150_Comment_content: Property = Property(name="content", type=StringType)
helloworld150_Comment.attributes={helloworld150_Comment_content}

# Relationships
things0: BinaryAssociation = BinaryAssociation(
    name="things0",
    ends={
        Property(name="helloworld150_Thing", type=helloworld150_World, multiplicity=Multiplicity(1, 1)),
        Property(name="helloworld150_World", type=helloworld150_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownership5: BinaryAssociation = BinaryAssociation(
    name="ownership5",
    ends={
        Property(name="Own", type=helloworld150_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="thing", type=helloworld150_Own, multiplicity=Multiplicity(0, 1))
    }
)
ownerships6: BinaryAssociation = BinaryAssociation(
    name="ownerships6",
    ends={
        Property(name="helloworld150_Own", type=helloworld150_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="helloworld150_Thing7", type=helloworld150_Own, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
persons1: BinaryAssociation = BinaryAssociation(
    name="persons1",
    ends={
        Property(name="helloworld150_Person", type=helloworld150_World, multiplicity=Multiplicity(1, 1)),
        Property(name="helloworld150_World2", type=helloworld150_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
professions3: BinaryAssociation = BinaryAssociation(
    name="professions3",
    ends={
        Property(name="helloworld150_Profession", type=helloworld150_World, multiplicity=Multiplicity(1, 1)),
        Property(name="helloworld150_World4", type=helloworld150_Profession, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thing9: BinaryAssociation = BinaryAssociation(
    name="thing9",
    ends={
        Property(name="Thing", type=helloworld150_Own, multiplicity=Multiplicity(1, 1)),
        Property(name="ownership", type=helloworld150_Thing, multiplicity=Multiplicity(0, 1))
    }
)
person10: BinaryAssociation = BinaryAssociation(
    name="person10",
    ends={
        Property(name="helloworld150_Person12", type=helloworld150_Own, multiplicity=Multiplicity(1, 1)),
        Property(name="helloworld150_Own11", type=helloworld150_Person, multiplicity=Multiplicity(0, 1))
    }
)
comment8: BinaryAssociation = BinaryAssociation(
    name="comment8",
    ends={
        Property(name="helloworld150_Comment", type=helloworld150_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="helloworld150_NamedElement", type=helloworld150_Comment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
profession13: BinaryAssociation = BinaryAssociation(
    name="profession13",
    ends={
        Property(name="helloworld150_Profession15", type=helloworld150_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="helloworld150_Person14", type=helloworld150_Profession, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_helloworld150_Thing_NamedElement = Generalization(general=NamedElement, specific=helloworld150_Thing)
gen_helloworld150_Person_NamedElement = Generalization(general=NamedElement, specific=helloworld150_Person)
gen_helloworld150_Own_NamedElement = Generalization(general=NamedElement, specific=helloworld150_Own)

# Domain Model
domain_model = DomainModel(
    name="helloworld150",
    types={helloworld150_World, helloworld150_Thing, helloworld150_Own, helloworld150_NamedElement, helloworld150_Person, helloworld150_Profession, NamedElement, helloworld150_Comment},
    associations={things0, ownership5, ownerships6, persons1, professions3, thing9, person10, comment8, profession13},
    generalizations={gen_helloworld150_Thing_NamedElement, gen_helloworld150_Person_NamedElement, gen_helloworld150_Own_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)