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
family_Parent = Class(name="family::Parent")
Person = Class(name="Person")
family_Child = Class(name="family::Child")
family_Mother = Class(name="family::Mother")
Parent = Class(name="Parent")
family_Father = Class(name="family::Father")
family_Person = Class(name="family::Person")
family_Family = Class(name="family::Family")

# family_Parent class attributes and methods

# Person class attributes and methods

# family_Child class attributes and methods

# family_Mother class attributes and methods

# Parent class attributes and methods

# family_Father class attributes and methods

# family_Person class attributes and methods
family_Person_firstname: Property = Property(name="firstname", type=StringType)
family_Person_lastname: Property = Property(name="lastname", type=StringType)
family_Person_birthdate: Property = Property(name="birthdate", type=DateType)
family_Person.attributes={family_Person_birthdate, family_Person_firstname, family_Person_lastname}

# family_Family class attributes and methods

# Relationships
children0: BinaryAssociation = BinaryAssociation(
    name="children0",
    ends={
        Property(name="family_Child", type=family_Parent, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Parent", type=family_Child, multiplicity=Multiplicity(0, 9999))
    }
)
husband1: BinaryAssociation = BinaryAssociation(
    name="husband1",
    ends={
        Property(name="family_Father", type=family_Mother, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Mother", type=family_Father, multiplicity=Multiplicity(0, 1))
    }
)
wife2: BinaryAssociation = BinaryAssociation(
    name="wife2",
    ends={
        Property(name="family_Mother4", type=family_Father, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Father3", type=family_Mother, multiplicity=Multiplicity(0, 1))
    }
)
mother5: BinaryAssociation = BinaryAssociation(
    name="mother5",
    ends={
        Property(name="family_Mother7", type=family_Child, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Child6", type=family_Mother, multiplicity=Multiplicity(0, 1))
    }
)
father8: BinaryAssociation = BinaryAssociation(
    name="father8",
    ends={
        Property(name="family_Father10", type=family_Child, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Child9", type=family_Father, multiplicity=Multiplicity(0, 1))
    }
)
members11: BinaryAssociation = BinaryAssociation(
    name="members11",
    ends={
        Property(name="family_Person", type=family_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Family", type=family_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_family_Parent_Person = Generalization(general=Person, specific=family_Parent)
gen_family_Mother_Parent = Generalization(general=Parent, specific=family_Mother)
gen_family_Father_Parent = Generalization(general=Parent, specific=family_Father)
gen_family_Child_Person = Generalization(general=Person, specific=family_Child)

# Domain Model
domain_model = DomainModel(
    name="family",
    types={family_Parent, Person, family_Child, family_Mother, Parent, family_Father, family_Person, family_Family},
    associations={children0, husband1, wife2, mother5, father8, members11},
    generalizations={gen_family_Parent_Person, gen_family_Mother_Parent, gen_family_Father_Parent, gen_family_Child_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)