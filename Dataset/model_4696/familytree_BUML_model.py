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
familytree_Member = Class(name="familytree::Member")

# familytree_FamilyTree class attributes and methods

# familytree_Member class attributes and methods
familytree_Member_name: Property = Property(name="name", type=StringType)
familytree_Member_age: Property = Property(name="age", type=IntegerType)
familytree_Member.attributes={familytree_Member_name, familytree_Member_age}

# Relationships
members0: BinaryAssociation = BinaryAssociation(
    name="members0",
    ends={
        Property(name="familytree_Member", type=familytree_FamilyTree, multiplicity=Multiplicity(1, 1)),
        Property(name="familytree_FamilyTree", type=familytree_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children2: BinaryAssociation = BinaryAssociation(
    name="children2",
    ends={
        Property(name="Member", type=familytree_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="parents", type=familytree_Member, multiplicity=Multiplicity(0, 9999))
    }
)
parents4: BinaryAssociation = BinaryAssociation(
    name="parents4",
    ends={
        Property(name="Member5", type=familytree_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=familytree_Member, multiplicity=Multiplicity(0, 2))
    }
)

# Domain Model
domain_model = DomainModel(
    name="familytree",
    types={familytree_FamilyTree, familytree_Member},
    associations={members0, children2, parents4},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)