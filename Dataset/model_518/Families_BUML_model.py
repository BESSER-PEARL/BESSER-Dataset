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
Families_Families = Class(name="Families::Families")
Families_Family = Class(name="Families::Family")
Families_Member = Class(name="Families::Member", is_abstract=True)
Families_Male = Class(name="Families::Male")
Member = Class(name="Member")
Families_Female = Class(name="Families::Female")

# Families_Families class attributes and methods

# Families_Family class attributes and methods
Families_Family_lastname: Property = Property(name="lastname", type=StringType)
Families_Family.attributes={Families_Family_lastname}

# Families_Member class attributes and methods
Families_Member_firstname: Property = Property(name="firstname", type=StringType)
Families_Member.attributes={Families_Member_firstname}

# Families_Male class attributes and methods

# Member class attributes and methods

# Families_Female class attributes and methods

# Relationships
members2: BinaryAssociation = BinaryAssociation(
    name="members2",
    ends={
        Property(name="family", type=Families_Member, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="Member", type=Families_Family, multiplicity=Multiplicity(1, 1))
    }
)
families0: BinaryAssociation = BinaryAssociation(
    name="families0",
    ends={
        Property(name="Family", type=Families_Families, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=Families_Family, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
container1: BinaryAssociation = BinaryAssociation(
    name="container1",
    ends={
        Property(name="Families", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="families", type=Families_Families, multiplicity=Multiplicity(1, 1))
    }
)
family3: BinaryAssociation = BinaryAssociation(
    name="family3",
    ends={
        Property(name="Family4", type=Families_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="members", type=Families_Family, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_Families_Male_Member = Generalization(general=Member, specific=Families_Male)
gen_Families_Female_Member = Generalization(general=Member, specific=Families_Female)

# Domain Model
domain_model = DomainModel(
    name="Families",
    types={Families_Families, Families_Family, Families_Member, Families_Male, Member, Families_Female},
    associations={members2, families0, container1, family3},
    generalizations={gen_Families_Male_Member, gen_Families_Female_Member},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)