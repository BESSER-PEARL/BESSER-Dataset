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
family_Member = Class(name="family::Member", is_abstract=True)
family_Family = Class(name="family::Family")

# family_Member class attributes and methods
family_Member_name: Property = Property(name="name", type=StringType)
family_Member.attributes={family_Member_name}

# family_Family class attributes and methods
family_Family_lastName: Property = Property(name="lastName", type=StringType)
family_Family.attributes={family_Family_lastName}

# Relationships
familyMother1: BinaryAssociation = BinaryAssociation(
    name="familyMother1",
    ends={
        Property(name="Family2", type=family_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="mother", type=family_Family, multiplicity=Multiplicity(0, 1))
    }
)
familySon3: BinaryAssociation = BinaryAssociation(
    name="familySon3",
    ends={
        Property(name="Family4", type=family_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="son", type=family_Family, multiplicity=Multiplicity(0, 1))
    }
)
familyDaughter5: BinaryAssociation = BinaryAssociation(
    name="familyDaughter5",
    ends={
        Property(name="Family6", type=family_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="daughter", type=family_Family, multiplicity=Multiplicity(0, 1))
    }
)
father7: BinaryAssociation = BinaryAssociation(
    name="father7",
    ends={
        Property(name="Member", type=family_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="familyFather", type=family_Member, multiplicity=Multiplicity(0, 1))
    }
)
mother8: BinaryAssociation = BinaryAssociation(
    name="mother8",
    ends={
        Property(name="Member9", type=family_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="familyMother", type=family_Member, multiplicity=Multiplicity(0, 1))
    }
)
son10: BinaryAssociation = BinaryAssociation(
    name="son10",
    ends={
        Property(name="Member11", type=family_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="familySon", type=family_Member, multiplicity=Multiplicity(0, 9999))
    }
)
daughter12: BinaryAssociation = BinaryAssociation(
    name="daughter12",
    ends={
        Property(name="Member13", type=family_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="familyDaughter", type=family_Member, multiplicity=Multiplicity(0, 9999))
    }
)
familyFather0: BinaryAssociation = BinaryAssociation(
    name="familyFather0",
    ends={
        Property(name="Family", type=family_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="father", type=family_Family, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="family",
    types={family_Member, family_Family},
    associations={familyMother1, familySon3, familyDaughter5, father7, mother8, son10, daughter12, familyFather0},
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