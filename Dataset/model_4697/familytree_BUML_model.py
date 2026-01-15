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
RelationshipStatus: Enumeration = Enumeration(
    name="RelationshipStatus",
    literals={
            EnumerationLiteral(name="Single"),
			EnumerationLiteral(name="Widowed"),
			EnumerationLiteral(name="Divorced"),
			EnumerationLiteral(name="Liaised"),
			EnumerationLiteral(name="Married")
    }
)

# Classes
familytree_FamilyTree = Class(name="familytree::FamilyTree")
familytree_Woman = Class(name="familytree::Woman")
Person = Class(name="Person")
familytree_Man = Class(name="familytree::Man")
familytree_Person = Class(name="familytree::Person", is_abstract=True)

# familytree_FamilyTree class attributes and methods

# familytree_Woman class attributes and methods

# Person class attributes and methods

# familytree_Man class attributes and methods

# familytree_Person class attributes and methods
familytree_Person_firstName: Property = Property(name="firstName", type=StringType)
familytree_Person_secondName: Property = Property(name="secondName", type=StringType)
familytree_Person_dayOfBirth: Property = Property(name="dayOfBirth", type=DateType)
familytree_Person_nameOfBirth: Property = Property(name="nameOfBirth", type=StringType)
familytree_Person_relationshipStatus: Property = Property(name="relationshipStatus", type=StringType)
familytree_Person_died: Property = Property(name="died", type=BooleanType)
familytree_Person_dayOfDeath: Property = Property(name="dayOfDeath", type=DateType)
familytree_Person_locationOfBirth: Property = Property(name="locationOfBirth", type=StringType)
familytree_Person_imagePaths: Property = Property(name="imagePaths", type=StringType)
familytree_Person.attributes={familytree_Person_nameOfBirth, familytree_Person_relationshipStatus, familytree_Person_firstName, familytree_Person_secondName, familytree_Person_dayOfBirth, familytree_Person_imagePaths, familytree_Person_dayOfDeath, familytree_Person_locationOfBirth, familytree_Person_died}

# Relationships
members11: BinaryAssociation = BinaryAssociation(
    name="members11",
    ends={
        Property(name="familytree_Person", type=familytree_FamilyTree, multiplicity=Multiplicity(1, 1)),
        Property(name="familytree_FamilyTree", type=familytree_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children1: BinaryAssociation = BinaryAssociation(
    name="children1",
    ends={
        Property(name="Person", type=familytree_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="parents", type=familytree_Person, multiplicity=Multiplicity(0, 9999))
    }
)
parents3: BinaryAssociation = BinaryAssociation(
    name="parents3",
    ends={
        Property(name="Person4", type=familytree_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=familytree_Person, multiplicity=Multiplicity(0, 2))
    }
)
inRelationWith6: BinaryAssociation = BinaryAssociation(
    name="inRelationWith6",
    ends={
        Property(name="Person7", type=familytree_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="inRelationTo", type=familytree_Person, multiplicity=Multiplicity(0, 1))
    }
)
inRelationTo9: BinaryAssociation = BinaryAssociation(
    name="inRelationTo9",
    ends={
        Property(name="Person10", type=familytree_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="inRelationWith", type=familytree_Person, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_familytree_Woman_Person = Generalization(general=Person, specific=familytree_Woman)
gen_familytree_Man_Person = Generalization(general=Person, specific=familytree_Man)

# Domain Model
domain_model = DomainModel(
    name="familytree",
    types={familytree_FamilyTree, familytree_Woman, Person, familytree_Man, familytree_Person, RelationshipStatus},
    associations={members11, children1, parents3, inRelationWith6, inRelationTo9},
    generalizations={gen_familytree_Woman_Person, gen_familytree_Man_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)