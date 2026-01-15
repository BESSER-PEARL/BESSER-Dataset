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

# Enumerations
SexType: Enumeration = Enumeration(
    name="SexType",
    literals={
            EnumerationLiteral(name="male"),
			EnumerationLiteral(name="female")
    }
)

# Classes
family_FNamedElement = Class(name="family::FNamedElement", is_abstract=True)
family_Person = Class(name="family::Person", is_abstract=True)
family_Family = Class(name="family::Family")
family_Father = Class(name="family::Father")
family_Mother = Class(name="family::Mother")
family_Child = Class(name="family::Child")
Person = Class(name="Person")
FNamedElement = Class(name="FNamedElement")

# family_FNamedElement class attributes and methods
family_FNamedElement_name: Property = Property(name="name", type=StringType)
family_FNamedElement.attributes={family_FNamedElement_name}

# family_Person class attributes and methods
family_Person_sex: Property = Property(name="sex", type=StringType)
family_Person_age: Property = Property(name="age", type=IntegerType)
family_Person.attributes={family_Person_sex, family_Person_age}

# family_Family class attributes and methods

# family_Father class attributes and methods

# family_Mother class attributes and methods

# family_Child class attributes and methods

# Person class attributes and methods

# FNamedElement class attributes and methods

# Relationships
members0: BinaryAssociation = BinaryAssociation(
    name="members0",
    ends={
        Property(name="family_Person", type=family_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Family", type=family_Person, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
father1: BinaryAssociation = BinaryAssociation(
    name="father1",
    ends={
        Property(name="family_Father", type=family_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Family2", type=family_Father, multiplicity=Multiplicity(0, 1))
    }
)
mother3: BinaryAssociation = BinaryAssociation(
    name="mother3",
    ends={
        Property(name="family_Mother", type=family_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Family4", type=family_Mother, multiplicity=Multiplicity(0, 1))
    }
)
children5: BinaryAssociation = BinaryAssociation(
    name="children5",
    ends={
        Property(name="family_Child", type=family_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Family6", type=family_Child, multiplicity=Multiplicity(0, 9999))
    }
)
children7: BinaryAssociation = BinaryAssociation(
    name="children7",
    ends={
        Property(name="Child", type=family_Father, multiplicity=Multiplicity(1, 1)),
        Property(name="father", type=family_Child, multiplicity=Multiplicity(0, 9999))
    }
)
wife8: BinaryAssociation = BinaryAssociation(
    name="wife8",
    ends={
        Property(name="Mother", type=family_Father, multiplicity=Multiplicity(1, 1)),
        Property(name="husband", type=family_Mother, multiplicity=Multiplicity(0, 1))
    }
)
husband11: BinaryAssociation = BinaryAssociation(
    name="husband11",
    ends={
        Property(name="wife", type=family_Father, multiplicity=Multiplicity(0, 1)),
        Property(name="Father", type=family_Mother, multiplicity=Multiplicity(1, 1))
    }
)
mother12: BinaryAssociation = BinaryAssociation(
    name="mother12",
    ends={
        Property(name="Mother13", type=family_Child, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=family_Mother, multiplicity=Multiplicity(0, 1))
    }
)
father14: BinaryAssociation = BinaryAssociation(
    name="father14",
    ends={
        Property(name="Father16", type=family_Child, multiplicity=Multiplicity(1, 1)),
        Property(name="children15", type=family_Father, multiplicity=Multiplicity(0, 1))
    }
)
children9: BinaryAssociation = BinaryAssociation(
    name="children9",
    ends={
        Property(name="Child10", type=family_Mother, multiplicity=Multiplicity(1, 1)),
        Property(name="mother", type=family_Child, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_family_Family_FNamedElement = Generalization(general=FNamedElement, specific=family_Family)
gen_family_Father_Person = Generalization(general=Person, specific=family_Father)
gen_family_Mother_Person = Generalization(general=Person, specific=family_Mother)
gen_family_Person_FNamedElement = Generalization(general=FNamedElement, specific=family_Person)
gen_family_Child_Person = Generalization(general=Person, specific=family_Child)

# Domain Model
domain_model = DomainModel(
    name="family",
    types={family_FNamedElement, family_Person, family_Family, family_Father, family_Mother, family_Child, Person, FNamedElement, SexType},
    associations={members0, father1, mother3, children5, children7, wife8, husband11, mother12, father14, children9},
    generalizations={gen_family_Family_FNamedElement, gen_family_Father_Person, gen_family_Mother_Person, gen_family_Person_FNamedElement, gen_family_Child_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)