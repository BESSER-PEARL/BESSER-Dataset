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
Families_Family = Class(name="Families::Family")
Families_Member = Class(name="Families::Member")
Families_FamilyRegistry = Class(name="Families::FamilyRegistry")

# Families_Family class attributes and methods
Families_Family_lastName: Property = Property(name="lastName", type=StringType)
Families_Family_address: Property = Property(name="address", type=StringType)
Families_Family.attributes={Families_Family_lastName, Families_Family_address}

# Families_Member class attributes and methods
Families_Member_firstName: Property = Property(name="firstName", type=StringType)
Families_Member_age: Property = Property(name="age", type=IntegerType)
Families_Member.attributes={Families_Member_firstName, Families_Member_age}

# Families_FamilyRegistry class attributes and methods

# Relationships
sons0: BinaryAssociation = BinaryAssociation(
    name="sons0",
    ends={
        Property(name="Families_Member", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_Family", type=Families_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
daughters1: BinaryAssociation = BinaryAssociation(
    name="daughters1",
    ends={
        Property(name="Families_Member3", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_Family2", type=Families_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mother4: BinaryAssociation = BinaryAssociation(
    name="mother4",
    ends={
        Property(name="Families_Member6", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_Family5", type=Families_Member, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
father7: BinaryAssociation = BinaryAssociation(
    name="father7",
    ends={
        Property(name="Families_Member9", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_Family8", type=Families_Member, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
links11: BinaryAssociation = BinaryAssociation(
    name="links11",
    ends={
        Property(name="Families_Family12", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_Family10", type=Families_Family, multiplicity=Multiplicity(0, 9999))
    }
)
relatives14: BinaryAssociation = BinaryAssociation(
    name="relatives14",
    ends={
        Property(name="Families_Member15", type=Families_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_Member13", type=Families_Member, multiplicity=Multiplicity(0, 1))
    }
)
families16: BinaryAssociation = BinaryAssociation(
    name="families16",
    ends={
        Property(name="Families_Family17", type=Families_FamilyRegistry, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_FamilyRegistry", type=Families_Family, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="Families",
    types={Families_Family, Families_Member, Families_FamilyRegistry},
    associations={sons0, daughters1, mother4, father7, links11, relatives14, families16},
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