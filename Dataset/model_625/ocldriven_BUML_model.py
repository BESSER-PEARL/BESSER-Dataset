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
ocldriven_Library = Class(name="ocldriven::Library")
ocldriven_Media = Class(name="ocldriven::Media")
ocldriven_Member = Class(name="ocldriven::Member")
ocldriven_Loans = Class(name="ocldriven::Loans")
ocldriven_Dependancy = Class(name="ocldriven::Dependancy")

# ocldriven_Library class attributes and methods

# ocldriven_Media class attributes and methods
ocldriven_Media_name: Property = Property(name="name", type=StringType)
ocldriven_Media_copies: Property = Property(name="copies", type=StringType)
ocldriven_Media.attributes={ocldriven_Media_name, ocldriven_Media_copies}

# ocldriven_Member class attributes and methods
ocldriven_Member_name: Property = Property(name="name", type=StringType)
ocldriven_Member.attributes={ocldriven_Member_name}

# ocldriven_Loans class attributes and methods
ocldriven_Loans_date: Property = Property(name="date", type=DateType)
ocldriven_Loans.attributes={ocldriven_Loans_date}

# ocldriven_Dependancy class attributes and methods

# Relationships
medias0: BinaryAssociation = BinaryAssociation(
    name="medias0",
    ends={
        Property(name="Media", type=ocldriven_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library", type=ocldriven_Media, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
members1: BinaryAssociation = BinaryAssociation(
    name="members1",
    ends={
        Property(name="library2", type=ocldriven_Member, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="Member", type=ocldriven_Library, multiplicity=Multiplicity(1, 1))
    }
)
library6: BinaryAssociation = BinaryAssociation(
    name="library6",
    ends={
        Property(name="Library", type=ocldriven_Media, multiplicity=Multiplicity(1, 1)),
        Property(name="medias", type=ocldriven_Library, multiplicity=Multiplicity(0, 1))
    }
)
loans3: BinaryAssociation = BinaryAssociation(
    name="loans3",
    ends={
        Property(name="ocldriven_Loans", type=ocldriven_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="ocldriven_Library", type=ocldriven_Loans, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependancies4: BinaryAssociation = BinaryAssociation(
    name="dependancies4",
    ends={
        Property(name="ocldriven_Dependancy", type=ocldriven_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="ocldriven_Library5", type=ocldriven_Dependancy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
member7: BinaryAssociation = BinaryAssociation(
    name="member7",
    ends={
        Property(name="ocldriven_Member", type=ocldriven_Loans, multiplicity=Multiplicity(1, 1)),
        Property(name="ocldriven_Loans8", type=ocldriven_Member, multiplicity=Multiplicity(1, 1))
    }
)
media9: BinaryAssociation = BinaryAssociation(
    name="media9",
    ends={
        Property(name="ocldriven_Media", type=ocldriven_Loans, multiplicity=Multiplicity(1, 1)),
        Property(name="ocldriven_Loans10", type=ocldriven_Media, multiplicity=Multiplicity(1, 1))
    }
)
library11: BinaryAssociation = BinaryAssociation(
    name="library11",
    ends={
        Property(name="Library12", type=ocldriven_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="members", type=ocldriven_Library, multiplicity=Multiplicity(0, 1))
    }
)
before13: BinaryAssociation = BinaryAssociation(
    name="before13",
    ends={
        Property(name="ocldriven_Media15", type=ocldriven_Dependancy, multiplicity=Multiplicity(1, 1)),
        Property(name="ocldriven_Dependancy14", type=ocldriven_Media, multiplicity=Multiplicity(0, 1))
    }
)
after16: BinaryAssociation = BinaryAssociation(
    name="after16",
    ends={
        Property(name="ocldriven_Media18", type=ocldriven_Dependancy, multiplicity=Multiplicity(1, 1)),
        Property(name="ocldriven_Dependancy17", type=ocldriven_Media, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="ocldriven",
    types={ocldriven_Library, ocldriven_Media, ocldriven_Member, ocldriven_Loans, ocldriven_Dependancy},
    associations={medias0, members1, library6, loans3, dependancies4, member7, media9, library11, before13, after16},
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