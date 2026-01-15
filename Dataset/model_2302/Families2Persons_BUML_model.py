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
Families2Persons_Person = Class(name="Families2Persons::Person")
Families2Persons_Member2Male = Class(name="Families2Persons::Member2Male")
MemberToPerson = Class(name="MemberToPerson")
Families2Persons_Member2Female = Class(name="Families2Persons::Member2Female")
Families2Persons_MemberToPerson = Class(name="Families2Persons::MemberToPerson", is_abstract=True)
Families2Persons_Member = Class(name="Families2Persons::Member")

# Families2Persons_Person class attributes and methods

# Families2Persons_Member2Male class attributes and methods

# MemberToPerson class attributes and methods

# Families2Persons_Member2Female class attributes and methods

# Families2Persons_MemberToPerson class attributes and methods
Families2Persons_MemberToPerson_firstName: Property = Property(name="firstName", type=StringType)
Families2Persons_MemberToPerson_familyName: Property = Property(name="familyName", type=StringType)
Families2Persons_MemberToPerson.attributes={Families2Persons_MemberToPerson_familyName, Families2Persons_MemberToPerson_firstName}

# Families2Persons_Member class attributes and methods

# Relationships
member0: BinaryAssociation = BinaryAssociation(
    name="member0",
    ends={
        Property(name="Families2Persons_Member", type=Families2Persons_MemberToPerson, multiplicity=Multiplicity(1, 1)),
        Property(name="Families2Persons_MemberToPerson", type=Families2Persons_Member, multiplicity=Multiplicity(0, 1))
    }
)
person1: BinaryAssociation = BinaryAssociation(
    name="person1",
    ends={
        Property(name="Families2Persons_Person", type=Families2Persons_MemberToPerson, multiplicity=Multiplicity(1, 1)),
        Property(name="Families2Persons_MemberToPerson2", type=Families2Persons_Person, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_Families2Persons_Member2Male_MemberToPerson = Generalization(general=MemberToPerson, specific=Families2Persons_Member2Male)
gen_Families2Persons_Member2Female_MemberToPerson = Generalization(general=MemberToPerson, specific=Families2Persons_Member2Female)

# Domain Model
domain_model = DomainModel(
    name="Families2Persons",
    types={Families2Persons_Person, Families2Persons_Member2Male, MemberToPerson, Families2Persons_Member2Female, Families2Persons_MemberToPerson, Families2Persons_Member},
    associations={member0, person1},
    generalizations={gen_Families2Persons_Member2Male_MemberToPerson, gen_Families2Persons_Member2Female_MemberToPerson},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)