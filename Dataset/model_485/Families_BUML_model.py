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
families_Family = Class(name="families::Family")
families_Member = Class(name="families::Member")

# families_Family class attributes and methods
families_Family_lastName: Property = Property(name="lastName", type=StringType)
families_Family.attributes={families_Family_lastName}

# families_Member class attributes and methods
families_Member_firstName: Property = Property(name="firstName", type=StringType)
families_Member.attributes={families_Member_firstName}

# Relationships
father0: BinaryAssociation = BinaryAssociation(
    name="father0",
    ends={
        Property(name="Member", type=families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="familyFather", type=families_Member, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mother1: BinaryAssociation = BinaryAssociation(
    name="mother1",
    ends={
        Property(name="Member2", type=families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="familyMother", type=families_Member, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
familyDaughter12: BinaryAssociation = BinaryAssociation(
    name="familyDaughter12",
    ends={
        Property(name="Family13", type=families_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="daughters", type=families_Family, multiplicity=Multiplicity(0, 1))
    }
)
sons3: BinaryAssociation = BinaryAssociation(
    name="sons3",
    ends={
        Property(name="Member4", type=families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="familySon", type=families_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
daughters5: BinaryAssociation = BinaryAssociation(
    name="daughters5",
    ends={
        Property(name="Member6", type=families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="familyDaughter", type=families_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
familyFather7: BinaryAssociation = BinaryAssociation(
    name="familyFather7",
    ends={
        Property(name="Family", type=families_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="father", type=families_Family, multiplicity=Multiplicity(0, 1))
    }
)
familyMother8: BinaryAssociation = BinaryAssociation(
    name="familyMother8",
    ends={
        Property(name="Family9", type=families_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="mother", type=families_Family, multiplicity=Multiplicity(0, 1))
    }
)
familySon10: BinaryAssociation = BinaryAssociation(
    name="familySon10",
    ends={
        Property(name="Family11", type=families_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="sons", type=families_Family, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="families",
    types={families_Family, families_Member},
    associations={father0, mother1, familyDaughter12, sons3, daughters5, familyFather7, familyMother8, familySon10},
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