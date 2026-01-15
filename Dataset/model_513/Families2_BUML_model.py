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
Families_FamilyRegistry = Class(name="Families::FamilyRegistry")
Families_Family = Class(name="Families::Family")
Families_Member = Class(name="Families::Member")

# Families_FamilyRegistry class attributes and methods

# Families_Family class attributes and methods
Families_Family_address: Property = Property(name="address", type=StringType)
Families_Family_lastName: Property = Property(name="lastName", type=StringType)
Families_Family.attributes={Families_Family_address, Families_Family_lastName}

# Families_Member class attributes and methods
Families_Member_firstName: Property = Property(name="firstName", type=StringType)
Families_Member_age: Property = Property(name="age", type=IntegerType)
Families_Member.attributes={Families_Member_age, Families_Member_firstName}

# Relationships
guardian7: BinaryAssociation = BinaryAssociation(
    name="guardian7",
    ends={
        Property(name="Families_Family9", type=Families_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_Member8", type=Families_Family, multiplicity=Multiplicity(0, 1))
    }
)
families10: BinaryAssociation = BinaryAssociation(
    name="families10",
    ends={
        Property(name="Families_Family11", type=Families_FamilyRegistry, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_FamilyRegistry", type=Families_Family, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children0: BinaryAssociation = BinaryAssociation(
    name="children0",
    ends={
        Property(name="Families_Member", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_Family", type=Families_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mother1: BinaryAssociation = BinaryAssociation(
    name="mother1",
    ends={
        Property(name="Families_Member3", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_Family2", type=Families_Member, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
father4: BinaryAssociation = BinaryAssociation(
    name="father4",
    ends={
        Property(name="Families_Member6", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_Family5", type=Families_Member, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="Families",
    types={Families_FamilyRegistry, Families_Family, Families_Member},
    associations={guardian7, families10, children0, mother1, father4},
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