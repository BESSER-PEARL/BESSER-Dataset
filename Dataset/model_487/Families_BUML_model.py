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
Family = Class(name="Family")
Member = Class(name="Member")

# Families_Family class attributes and methods
Families_Family_lastName: Property = Property(name="lastName", type=StringType)
Families_Family.attributes={Families_Family_lastName}

# Families_Member class attributes and methods
Families_Member_firstName: Property = Property(name="firstName", type=StringType)
Families_Member.attributes={Families_Member_firstName}

# Family class attributes and methods

# Member class attributes and methods

# Relationships
daughters7: BinaryAssociation = BinaryAssociation(
    name="daughters7",
    ends={
        Property(name="#9", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="08", type=Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
familyFather10: BinaryAssociation = BinaryAssociation(
    name="familyFather10",
    ends={
        Property(name="#12", type=Families_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="011", type=Family, multiplicity=Multiplicity(0, 1))
    }
)
familyMother13: BinaryAssociation = BinaryAssociation(
    name="familyMother13",
    ends={
        Property(name="#15", type=Families_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="014", type=Family, multiplicity=Multiplicity(0, 1))
    }
)
familySon16: BinaryAssociation = BinaryAssociation(
    name="familySon16",
    ends={
        Property(name="#18", type=Families_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="017", type=Family, multiplicity=Multiplicity(0, 1))
    }
)
familyDaughter19: BinaryAssociation = BinaryAssociation(
    name="familyDaughter19",
    ends={
        Property(name="#21", type=Families_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="020", type=Family, multiplicity=Multiplicity(0, 1))
    }
)
father0: BinaryAssociation = BinaryAssociation(
    name="father0",
    ends={
        Property(name="#", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="0", type=Member, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mother1: BinaryAssociation = BinaryAssociation(
    name="mother1",
    ends={
        Property(name="#3", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="02", type=Member, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sons4: BinaryAssociation = BinaryAssociation(
    name="sons4",
    ends={
        Property(name="#6", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="05", type=Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={Families_Family, Families_Member, Family, Member},
    associations={daughters7, familyFather10, familyMother13, familySon16, familyDaughter19, father0, mother1, sons4},
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