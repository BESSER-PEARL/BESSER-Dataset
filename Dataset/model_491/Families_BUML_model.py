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
Families_Member = Class(name="Families_Member")
Family = Class(name="Family")
Families_MemberMale = Class(name="Families_MemberMale")
Families_Family = Class(name="Families_Family")
Member = Class(name="Member")

# Families_Member class attributes and methods
Families_Member_firstName: Property = Property(name="firstName", type=StringType)
Families_Member.attributes={Families_Member_firstName}

# Family class attributes and methods

# Families_MemberMale class attributes and methods
Families_MemberMale_test: Property = Property(name="test", type=StringType)
Families_MemberMale.attributes={Families_MemberMale_test}

# Families_Family class attributes and methods
Families_Family_lastName: Property = Property(name="lastName", type=StringType)
Families_Family.attributes={Families_Family_lastName}

# Member class attributes and methods

# Relationships
sons3: BinaryAssociation = BinaryAssociation(
    name="sons3",
    ends={
        Property(name="Member4", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="familySon", type=Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
daughters5: BinaryAssociation = BinaryAssociation(
    name="daughters5",
    ends={
        Property(name="Member6", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="familyDaughter", type=Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
familyFather7: BinaryAssociation = BinaryAssociation(
    name="familyFather7",
    ends={
        Property(name="Family", type=Families_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="father", type=Family, multiplicity=Multiplicity(0, 1))
    }
)
familyMother8: BinaryAssociation = BinaryAssociation(
    name="familyMother8",
    ends={
        Property(name="Family9", type=Families_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="mother", type=Family, multiplicity=Multiplicity(0, 1))
    }
)
familySon10: BinaryAssociation = BinaryAssociation(
    name="familySon10",
    ends={
        Property(name="Family11", type=Families_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="sons", type=Family, multiplicity=Multiplicity(0, 1))
    }
)
familyDaughter12: BinaryAssociation = BinaryAssociation(
    name="familyDaughter12",
    ends={
        Property(name="Family13", type=Families_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="daughters", type=Family, multiplicity=Multiplicity(0, 1))
    }
)
father0: BinaryAssociation = BinaryAssociation(
    name="father0",
    ends={
        Property(name="Member", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="familyFather", type=Member, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mother1: BinaryAssociation = BinaryAssociation(
    name="mother1",
    ends={
        Property(name="Member2", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="familyMother", type=Member, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_Families_MemberMale_Member = Generalization(general=Member, specific=Families_MemberMale)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={Families_Member, Family, Families_MemberMale, Families_Family, Member},
    associations={sons3, daughters5, familyFather7, familyMother8, familySon10, familyDaughter12, father0, mother1},
    generalizations={gen_Families_MemberMale_Member},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)