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
Example_Family = Class(name="Example::Family")
Example_Member = Class(name="Example::Member", is_abstract=True)
Example_Parent = Class(name="Example::Parent")
Example_Son = Class(name="Example::Son")
Member = Class(name="Member")
Example_Daughter = Class(name="Example::Daughter")
Example_Pet = Class(name="Example::Pet", is_abstract=True)
Example_Dog = Class(name="Example::Dog")
Pet = Class(name="Pet")
Example_Cat = Class(name="Example::Cat")
Example_RaceDog = Class(name="Example::RaceDog")
Dog = Class(name="Dog")
Example_HuntingDog = Class(name="Example::HuntingDog")

# Example_Family class attributes and methods
Example_Family_address: Property = Property(name="address", type=StringType)
Example_Family.attributes={Example_Family_address}

# Example_Member class attributes and methods
Example_Member_firstName: Property = Property(name="firstName", type=StringType)
Example_Member_lastName: Property = Property(name="lastName", type=StringType)
Example_Member.attributes={Example_Member_firstName, Example_Member_lastName}

# Example_Parent class attributes and methods

# Example_Son class attributes and methods

# Member class attributes and methods

# Example_Daughter class attributes and methods

# Example_Pet class attributes and methods
Example_Pet_name: Property = Property(name="name", type=StringType)
Example_Pet_breed: Property = Property(name="breed", type=StringType)
Example_Pet.attributes={Example_Pet_breed, Example_Pet_name}

# Example_Dog class attributes and methods

# Pet class attributes and methods

# Example_Cat class attributes and methods

# Example_RaceDog class attributes and methods

# Dog class attributes and methods

# Example_HuntingDog class attributes and methods

# Relationships
parents0: BinaryAssociation = BinaryAssociation(
    name="parents0",
    ends={
        Property(name="Parent", type=Example_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family", type=Example_Parent, multiplicity=Multiplicity(0, 2), is_composite=True)
    }
)
sons1: BinaryAssociation = BinaryAssociation(
    name="sons1",
    ends={
        Property(name="Son", type=Example_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family2", type=Example_Son, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
family6: BinaryAssociation = BinaryAssociation(
    name="family6",
    ends={
        Property(name="Family", type=Example_Parent, multiplicity=Multiplicity(1, 1)),
        Property(name="parents", type=Example_Family, multiplicity=Multiplicity(1, 1))
    }
)
daughters3: BinaryAssociation = BinaryAssociation(
    name="daughters3",
    ends={
        Property(name="Daughter", type=Example_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family4", type=Example_Daughter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pets5: BinaryAssociation = BinaryAssociation(
    name="pets5",
    ends={
        Property(name="Example_Pet", type=Example_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="Example_Family", type=Example_Pet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
family7: BinaryAssociation = BinaryAssociation(
    name="family7",
    ends={
        Property(name="Family8", type=Example_Son, multiplicity=Multiplicity(1, 1)),
        Property(name="sons", type=Example_Family, multiplicity=Multiplicity(1, 1))
    }
)
family9: BinaryAssociation = BinaryAssociation(
    name="family9",
    ends={
        Property(name="Family10", type=Example_Daughter, multiplicity=Multiplicity(1, 1)),
        Property(name="daughters", type=Example_Family, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_Example_Parent_Member = Generalization(general=Member, specific=Example_Parent)
gen_Example_Son_Member = Generalization(general=Member, specific=Example_Son)
gen_Example_Dog_Pet = Generalization(general=Pet, specific=Example_Dog)
gen_Example_Cat_Pet = Generalization(general=Pet, specific=Example_Cat)
gen_Example_RaceDog_Dog = Generalization(general=Dog, specific=Example_RaceDog)
gen_Example_HuntingDog_Dog = Generalization(general=Dog, specific=Example_HuntingDog)
gen_Example_Daughter_Member = Generalization(general=Member, specific=Example_Daughter)

# Domain Model
domain_model = DomainModel(
    name="Example",
    types={Example_Family, Example_Member, Example_Parent, Example_Son, Member, Example_Daughter, Example_Pet, Example_Dog, Pet, Example_Cat, Example_RaceDog, Dog, Example_HuntingDog},
    associations={parents0, sons1, family6, daughters3, pets5, family7, family9},
    generalizations={gen_Example_Parent_Member, gen_Example_Son_Member, gen_Example_Dog_Pet, gen_Example_Cat_Pet, gen_Example_RaceDog_Dog, gen_Example_HuntingDog_Dog, gen_Example_Daughter_Member},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)