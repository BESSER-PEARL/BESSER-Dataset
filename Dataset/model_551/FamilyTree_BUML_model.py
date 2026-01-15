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
familyTree_FamilyTree = Class(name="familyTree::FamilyTree")
familyTree_Person = Class(name="familyTree::Person", is_abstract=True)
familyTree_Male = Class(name="familyTree::Male")
familyTree_Female = Class(name="familyTree::Female")
Person = Class(name="Person")

# familyTree_FamilyTree class attributes and methods

# familyTree_Person class attributes and methods
familyTree_Person_name: Property = Property(name="name", type=StringType)
familyTree_Person_lastName: Property = Property(name="lastName", type=StringType)
familyTree_Person.attributes={familyTree_Person_lastName, familyTree_Person_name}

# familyTree_Male class attributes and methods

# familyTree_Female class attributes and methods

# Person class attributes and methods

# Relationships
leaves0: BinaryAssociation = BinaryAssociation(
    name="leaves0",
    ends={
        Property(name="Person", type=familyTree_FamilyTree, multiplicity=Multiplicity(1, 1)),
        Property(name="tree", type=familyTree_Person, multiplicity=Multiplicity(0, 9999))
    }
)
father1: BinaryAssociation = BinaryAssociation(
    name="father1",
    ends={
        Property(name="Male", type=familyTree_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=familyTree_Male, multiplicity=Multiplicity(0, 1))
    }
)
mother2: BinaryAssociation = BinaryAssociation(
    name="mother2",
    ends={
        Property(name="Female", type=familyTree_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="children3", type=familyTree_Female, multiplicity=Multiplicity(0, 1))
    }
)
wife5: BinaryAssociation = BinaryAssociation(
    name="wife5",
    ends={
        Property(name="Female6", type=familyTree_Male, multiplicity=Multiplicity(1, 1)),
        Property(name="husband", type=familyTree_Female, multiplicity=Multiplicity(0, 1))
    }
)
children7: BinaryAssociation = BinaryAssociation(
    name="children7",
    ends={
        Property(name="Person8", type=familyTree_Male, multiplicity=Multiplicity(1, 1)),
        Property(name="father", type=familyTree_Person, multiplicity=Multiplicity(0, 1))
    }
)
tree4: BinaryAssociation = BinaryAssociation(
    name="tree4",
    ends={
        Property(name="FamilyTree", type=familyTree_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="leaves", type=familyTree_FamilyTree, multiplicity=Multiplicity(0, 1))
    }
)
children11: BinaryAssociation = BinaryAssociation(
    name="children11",
    ends={
        Property(name="Person12", type=familyTree_Female, multiplicity=Multiplicity(1, 1)),
        Property(name="mother", type=familyTree_Person, multiplicity=Multiplicity(0, 1))
    }
)
husband9: BinaryAssociation = BinaryAssociation(
    name="husband9",
    ends={
        Property(name="Male10", type=familyTree_Female, multiplicity=Multiplicity(1, 1)),
        Property(name="wife", type=familyTree_Male, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_familyTree_Male_Person = Generalization(general=Person, specific=familyTree_Male)
gen_familyTree_Female_Person = Generalization(general=Person, specific=familyTree_Female)

# Domain Model
domain_model = DomainModel(
    name="familyTree",
    types={familyTree_FamilyTree, familyTree_Person, familyTree_Male, familyTree_Female, Person},
    associations={leaves0, father1, mother2, wife5, children7, tree4, children11, husband9},
    generalizations={gen_familyTree_Male_Person, gen_familyTree_Female_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)