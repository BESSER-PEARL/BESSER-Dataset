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
Families_Father = Class(name="Families::Father")
Families_Mother = Class(name="Families::Mother")
Families_Son = Class(name="Families::Son")
Families_Daughter = Class(name="Families::Daughter")
Families_Member = Class(name="Families::Member", is_abstract=True)
Member = Class(name="Member")

# Families_Family class attributes and methods
Families_Family_lastName: Property = Property(name="lastName", type=StringType)
Families_Family.attributes={Families_Family_lastName}

# Families_Father class attributes and methods

# Families_Mother class attributes and methods

# Families_Son class attributes and methods

# Families_Daughter class attributes and methods

# Families_Member class attributes and methods
Families_Member_firstName: Property = Property(name="firstName", type=StringType)
Families_Member.attributes={Families_Member_firstName}

# Member class attributes and methods

# Relationships
father0: BinaryAssociation = BinaryAssociation(
    name="father0",
    ends={
        Property(name="Father", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family", type=Families_Father, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mother1: BinaryAssociation = BinaryAssociation(
    name="mother1",
    ends={
        Property(name="Mother", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family2", type=Families_Mother, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sons3: BinaryAssociation = BinaryAssociation(
    name="sons3",
    ends={
        Property(name="Son", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family4", type=Families_Son, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
daughters5: BinaryAssociation = BinaryAssociation(
    name="daughters5",
    ends={
        Property(name="Daughter", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family6", type=Families_Daughter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
family7: BinaryAssociation = BinaryAssociation(
    name="family7",
    ends={
        Property(name="Family", type=Families_Father, multiplicity=Multiplicity(1, 1)),
        Property(name="father", type=Families_Family, multiplicity=Multiplicity(1, 1))
    }
)
family8: BinaryAssociation = BinaryAssociation(
    name="family8",
    ends={
        Property(name="Family9", type=Families_Mother, multiplicity=Multiplicity(1, 1)),
        Property(name="mother", type=Families_Family, multiplicity=Multiplicity(1, 1))
    }
)
family10: BinaryAssociation = BinaryAssociation(
    name="family10",
    ends={
        Property(name="Family11", type=Families_Son, multiplicity=Multiplicity(1, 1)),
        Property(name="sons", type=Families_Family, multiplicity=Multiplicity(1, 1))
    }
)
family12: BinaryAssociation = BinaryAssociation(
    name="family12",
    ends={
        Property(name="Family13", type=Families_Daughter, multiplicity=Multiplicity(1, 1)),
        Property(name="daughters", type=Families_Family, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_Families_Father_Member = Generalization(general=Member, specific=Families_Father)
gen_Families_Mother_Member = Generalization(general=Member, specific=Families_Mother)
gen_Families_Son_Member = Generalization(general=Member, specific=Families_Son)
gen_Families_Daughter_Member = Generalization(general=Member, specific=Families_Daughter)

# Domain Model
domain_model = DomainModel(
    name="Families",
    types={Families_Family, Families_Father, Families_Mother, Families_Son, Families_Daughter, Families_Member, Member},
    associations={father0, mother1, sons3, daughters5, family7, family8, family10, family12},
    generalizations={gen_Families_Father_Member, gen_Families_Mother_Member, gen_Families_Son_Member, gen_Families_Daughter_Member},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)