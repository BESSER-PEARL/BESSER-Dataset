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

# Enumerations
GenderType: Enumeration = Enumeration(
    name="GenderType",
    literals={
            EnumerationLiteral(name="male"),
			EnumerationLiteral(name="female")
    }
)

# Classes
Families_Member = Class(name="Families_Member")
Families_Families = Class(name="Families_Families")
Families_Family = Class(name="Families_Family")

# Families_Member class attributes and methods
Families_Member_firstname: Property = Property(name="firstname", type=StringType)
Families_Member_gender: Property = Property(name="gender", type=StringType)
Families_Member.attributes={Families_Member_gender, Families_Member_firstname}

# Families_Families class attributes and methods

# Families_Family class attributes and methods
Families_Family_lastname: Property = Property(name="lastname", type=StringType)
Families_Family.attributes={Families_Family_lastname}

# Relationships
container1: BinaryAssociation = BinaryAssociation(
    name="container1",
    ends={
        Property(name="Families", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="families", type=Families_Families, multiplicity=Multiplicity(1, 1))
    }
)
members2: BinaryAssociation = BinaryAssociation(
    name="members2",
    ends={
        Property(name="Member", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family", type=Families_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
family3: BinaryAssociation = BinaryAssociation(
    name="family3",
    ends={
        Property(name="Family4", type=Families_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="members", type=Families_Family, multiplicity=Multiplicity(1, 1))
    }
)
families0: BinaryAssociation = BinaryAssociation(
    name="families0",
    ends={
        Property(name="Family", type=Families_Families, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=Families_Family, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="Families",
    types={Families_Member, Families_Families, Families_Family, GenderType},
    associations={container1, members2, family3, families0},
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