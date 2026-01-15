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
families_FamilyModel = Class(name="families::FamilyModel")
families_Family = Class(name="families::Family")
families_Member = Class(name="families::Member")

# families_FamilyModel class attributes and methods

# families_Family class attributes and methods
families_Family_lastName: Property = Property(name="lastName", type=StringType)
families_Family_street: Property = Property(name="street", type=StringType)
families_Family_town: Property = Property(name="town", type=StringType)
families_Family.attributes={families_Family_street, families_Family_lastName, families_Family_town}

# families_Member class attributes and methods
families_Member_firstName: Property = Property(name="firstName", type=StringType)
families_Member_age: Property = Property(name="age", type=IntegerType)
families_Member.attributes={families_Member_age, families_Member_firstName}

# Relationships
sons3: BinaryAssociation = BinaryAssociation(
    name="sons3",
    ends={
        Property(name="Member4", type=families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="familySon", type=families_Member, multiplicity=Multiplicity(0, 9999))
    }
)
daughters5: BinaryAssociation = BinaryAssociation(
    name="daughters5",
    ends={
        Property(name="Member6", type=families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="familyDaughter", type=families_Member, multiplicity=Multiplicity(0, 9999))
    }
)
model7: BinaryAssociation = BinaryAssociation(
    name="model7",
    ends={
        Property(name="FamilyModel", type=families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="families", type=families_FamilyModel, multiplicity=Multiplicity(1, 1))
    }
)
familyFather8: BinaryAssociation = BinaryAssociation(
    name="familyFather8",
    ends={
        Property(name="Family", type=families_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="father", type=families_Family, multiplicity=Multiplicity(0, 1))
    }
)
familyMother9: BinaryAssociation = BinaryAssociation(
    name="familyMother9",
    ends={
        Property(name="Family10", type=families_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="mother", type=families_Family, multiplicity=Multiplicity(0, 1))
    }
)
familySon11: BinaryAssociation = BinaryAssociation(
    name="familySon11",
    ends={
        Property(name="Family12", type=families_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="sons", type=families_Family, multiplicity=Multiplicity(0, 1))
    }
)
familyDaughter13: BinaryAssociation = BinaryAssociation(
    name="familyDaughter13",
    ends={
        Property(name="Family14", type=families_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="daughters", type=families_Family, multiplicity=Multiplicity(0, 1))
    }
)
model15: BinaryAssociation = BinaryAssociation(
    name="model15",
    ends={
        Property(name="FamilyModel16", type=families_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="members", type=families_FamilyModel, multiplicity=Multiplicity(1, 1))
    }
)
father0: BinaryAssociation = BinaryAssociation(
    name="father0",
    ends={
        Property(name="Member", type=families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="familyFather", type=families_Member, multiplicity=Multiplicity(1, 1))
    }
)
mother1: BinaryAssociation = BinaryAssociation(
    name="mother1",
    ends={
        Property(name="Member2", type=families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="familyMother", type=families_Member, multiplicity=Multiplicity(1, 1))
    }
)
families17: BinaryAssociation = BinaryAssociation(
    name="families17",
    ends={
        Property(name="Family18", type=families_FamilyModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model", type=families_Family, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
members19: BinaryAssociation = BinaryAssociation(
    name="members19",
    ends={
        Property(name="Member21", type=families_FamilyModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model20", type=families_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="families",
    types={families_FamilyModel, families_Family, families_Member},
    associations={sons3, daughters5, model7, familyFather8, familyMother9, familySon11, familyDaughter13, model15, father0, mother1, families17, members19},
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