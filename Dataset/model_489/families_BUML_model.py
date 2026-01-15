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
families_FamilyRegister = Class(name="families::FamilyRegister")
families_Family = Class(name="families::Family")
families_Member = Class(name="families::Member")

# families_FamilyRegister class attributes and methods
families_FamilyRegister_id: Property = Property(name="id", type=StringType)
families_FamilyRegister.attributes={families_FamilyRegister_id}

# families_Family class attributes and methods
families_Family_lastName: Property = Property(name="lastName", type=StringType)
families_Family.attributes={families_Family_lastName}

# families_Member class attributes and methods
families_Member_firstName: Property = Property(name="firstName", type=StringType)
families_Member.attributes={families_Member_firstName}

# Relationships
families0: BinaryAssociation = BinaryAssociation(
    name="families0",
    ends={
        Property(name="families_Family", type=families_FamilyRegister, multiplicity=Multiplicity(1, 1)),
        Property(name="families_FamilyRegister", type=families_Family, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sons1: BinaryAssociation = BinaryAssociation(
    name="sons1",
    ends={
        Property(name="Member", type=families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="familySon", type=families_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
daughters2: BinaryAssociation = BinaryAssociation(
    name="daughters2",
    ends={
        Property(name="Member3", type=families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="familyDaughter", type=families_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
familySon8: BinaryAssociation = BinaryAssociation(
    name="familySon8",
    ends={
        Property(name="Family", type=families_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="sons", type=families_Family, multiplicity=Multiplicity(0, 1))
    }
)
familyDaughter9: BinaryAssociation = BinaryAssociation(
    name="familyDaughter9",
    ends={
        Property(name="Family10", type=families_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="daughters", type=families_Family, multiplicity=Multiplicity(0, 1))
    }
)
familyFather11: BinaryAssociation = BinaryAssociation(
    name="familyFather11",
    ends={
        Property(name="Family12", type=families_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="father", type=families_Family, multiplicity=Multiplicity(0, 1))
    }
)
familyMother13: BinaryAssociation = BinaryAssociation(
    name="familyMother13",
    ends={
        Property(name="Family14", type=families_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="mother", type=families_Family, multiplicity=Multiplicity(0, 1))
    }
)
father4: BinaryAssociation = BinaryAssociation(
    name="father4",
    ends={
        Property(name="Member5", type=families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="familyFather", type=families_Member, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mother6: BinaryAssociation = BinaryAssociation(
    name="mother6",
    ends={
        Property(name="Member7", type=families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="familyMother", type=families_Member, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="families",
    types={families_FamilyRegister, families_Family, families_Member},
    associations={families0, sons1, daughters2, familySon8, familyDaughter9, familyFather11, familyMother13, father4, mother6},
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