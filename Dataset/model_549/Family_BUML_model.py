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
family_Person = Class(name="family::Person", is_abstract=True)
family_Male = Class(name="family::Male")
family_Female = Class(name="family::Female")
Person = Class(name="Person")
family_FamilyTree = Class(name="family::FamilyTree")

# family_Person class attributes and methods
family_Person_name: Property = Property(name="name", type=StringType)
family_Person_age: Property = Property(name="age", type=IntegerType)
family_Person_size: Property = Property(name="size", type=IntegerType)
family_Person_weight: Property = Property(name="weight", type=IntegerType)
family_Person.attributes={family_Person_name, family_Person_age, family_Person_weight, family_Person_size}

# family_Male class attributes and methods

# family_Female class attributes and methods

# Person class attributes and methods

# family_FamilyTree class attributes and methods

# Relationships
father0: BinaryAssociation = BinaryAssociation(
    name="father0",
    ends={
        Property(name="family_Male", type=family_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Person", type=family_Male, multiplicity=Multiplicity(0, 1))
    }
)
mother1: BinaryAssociation = BinaryAssociation(
    name="mother1",
    ends={
        Property(name="family_Female", type=family_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Person2", type=family_Female, multiplicity=Multiplicity(0, 1))
    }
)
children4: BinaryAssociation = BinaryAssociation(
    name="children4",
    ends={
        Property(name="family_Person5", type=family_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Person3", type=family_Person, multiplicity=Multiplicity(0, 9999))
    }
)
relative7: BinaryAssociation = BinaryAssociation(
    name="relative7",
    ends={
        Property(name="family_Person8", type=family_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Person6", type=family_Person, multiplicity=Multiplicity(0, 1))
    }
)
people9: BinaryAssociation = BinaryAssociation(
    name="people9",
    ends={
        Property(name="family_Person10", type=family_FamilyTree, multiplicity=Multiplicity(1, 1)),
        Property(name="family_FamilyTree", type=family_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_family_Male_Person = Generalization(general=Person, specific=family_Male)
gen_family_Female_Person = Generalization(general=Person, specific=family_Female)

# Domain Model
domain_model = DomainModel(
    name="family",
    types={family_Person, family_Male, family_Female, Person, family_FamilyTree},
    associations={father0, mother1, children4, relative7, people9},
    generalizations={gen_family_Male_Person, gen_family_Female_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)