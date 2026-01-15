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
familytree_FamilyTree = Class(name="familytree::FamilyTree")
familytree_Person = Class(name="familytree::Person", is_abstract=True)
familytree_Wedding = Class(name="familytree::Wedding")
familytree_Man = Class(name="familytree::Man")
Person = Class(name="Person")
familytree_Woman = Class(name="familytree::Woman")

# familytree_FamilyTree class attributes and methods
familytree_FamilyTree_name: Property = Property(name="name", type=StringType)
familytree_FamilyTree.attributes={familytree_FamilyTree_name}

# familytree_Person class attributes and methods
familytree_Person_firstName: Property = Property(name="firstName", type=StringType)
familytree_Person_lastName: Property = Property(name="lastName", type=StringType)
familytree_Person_birthYear: Property = Property(name="birthYear", type=IntegerType)
familytree_Person_deathYear: Property = Property(name="deathYear", type=IntegerType)
familytree_Person.attributes={familytree_Person_birthYear, familytree_Person_lastName, familytree_Person_deathYear, familytree_Person_firstName}

# familytree_Wedding class attributes and methods

# familytree_Man class attributes and methods

# Person class attributes and methods

# familytree_Woman class attributes and methods

# Relationships
persons0: BinaryAssociation = BinaryAssociation(
    name="persons0",
    ends={
        Property(name="familytree_Person", type=familytree_FamilyTree, multiplicity=Multiplicity(1, 1)),
        Property(name="familytree_FamilyTree", type=familytree_Person, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
weddings1: BinaryAssociation = BinaryAssociation(
    name="weddings1",
    ends={
        Property(name="familytree_Wedding", type=familytree_FamilyTree, multiplicity=Multiplicity(1, 1)),
        Property(name="familytree_FamilyTree2", type=familytree_Wedding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children4: BinaryAssociation = BinaryAssociation(
    name="children4",
    ends={
        Property(name="Person", type=familytree_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="parents", type=familytree_Person, multiplicity=Multiplicity(0, 9999))
    }
)
parents6: BinaryAssociation = BinaryAssociation(
    name="parents6",
    ends={
        Property(name="Person7", type=familytree_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=familytree_Person, multiplicity=Multiplicity(2, 2))
    }
)
wife8: BinaryAssociation = BinaryAssociation(
    name="wife8",
    ends={
        Property(name="Woman", type=familytree_Man, multiplicity=Multiplicity(1, 1)),
        Property(name="husband", type=familytree_Woman, multiplicity=Multiplicity(0, 1))
    }
)
husband9: BinaryAssociation = BinaryAssociation(
    name="husband9",
    ends={
        Property(name="Man", type=familytree_Woman, multiplicity=Multiplicity(1, 1)),
        Property(name="wife", type=familytree_Man, multiplicity=Multiplicity(0, 1))
    }
)
wife10: BinaryAssociation = BinaryAssociation(
    name="wife10",
    ends={
        Property(name="familytree_Woman", type=familytree_Wedding, multiplicity=Multiplicity(1, 1)),
        Property(name="familytree_Wedding11", type=familytree_Woman, multiplicity=Multiplicity(1, 1))
    }
)
husband12: BinaryAssociation = BinaryAssociation(
    name="husband12",
    ends={
        Property(name="familytree_Man", type=familytree_Wedding, multiplicity=Multiplicity(1, 1)),
        Property(name="familytree_Wedding13", type=familytree_Man, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_familytree_Man_Person = Generalization(general=Person, specific=familytree_Man)
gen_familytree_Woman_Person = Generalization(general=Person, specific=familytree_Woman)

# Domain Model
domain_model = DomainModel(
    name="familytree",
    types={familytree_FamilyTree, familytree_Person, familytree_Wedding, familytree_Man, Person, familytree_Woman},
    associations={persons0, weddings1, children4, parents6, wife8, husband9, wife10, husband12},
    generalizations={gen_familytree_Man_Person, gen_familytree_Woman_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)