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
FamiliesWithSiblings_Family = Class(name="FamiliesWithSiblings::Family")
FamiliesWithSiblings_FamilyMember = Class(name="FamiliesWithSiblings::FamilyMember")
FamiliesWithSiblings_FamilyRegister = Class(name="FamiliesWithSiblings::FamilyRegister")

# FamiliesWithSiblings_Family class attributes and methods
FamiliesWithSiblings_Family_name: Property = Property(name="name", type=StringType)
FamiliesWithSiblings_Family.attributes={FamiliesWithSiblings_Family_name}

# FamiliesWithSiblings_FamilyMember class attributes and methods
FamiliesWithSiblings_FamilyMember_name: Property = Property(name="name", type=StringType)
FamiliesWithSiblings_FamilyMember.attributes={FamiliesWithSiblings_FamilyMember_name}

# FamiliesWithSiblings_FamilyRegister class attributes and methods

# Relationships
families0: BinaryAssociation = BinaryAssociation(
    name="families0",
    ends={
        Property(name="Family", type=FamiliesWithSiblings_FamilyRegister, multiplicity=Multiplicity(1, 1)),
        Property(name="familiesInverse", type=FamiliesWithSiblings_Family, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
father1: BinaryAssociation = BinaryAssociation(
    name="father1",
    ends={
        Property(name="FamilyMember", type=FamiliesWithSiblings_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="fatherInverse", type=FamiliesWithSiblings_FamilyMember, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mother2: BinaryAssociation = BinaryAssociation(
    name="mother2",
    ends={
        Property(name="FamilyMember3", type=FamiliesWithSiblings_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="motherInverse", type=FamiliesWithSiblings_FamilyMember, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sons4: BinaryAssociation = BinaryAssociation(
    name="sons4",
    ends={
        Property(name="FamilyMember5", type=FamiliesWithSiblings_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="sonsInverse", type=FamiliesWithSiblings_FamilyMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
daughters6: BinaryAssociation = BinaryAssociation(
    name="daughters6",
    ends={
        Property(name="FamilyMember7", type=FamiliesWithSiblings_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="daughtersInverse", type=FamiliesWithSiblings_FamilyMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
familiesInverse8: BinaryAssociation = BinaryAssociation(
    name="familiesInverse8",
    ends={
        Property(name="FamilyRegister", type=FamiliesWithSiblings_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="families", type=FamiliesWithSiblings_FamilyRegister, multiplicity=Multiplicity(0, 1))
    }
)
siblings10: BinaryAssociation = BinaryAssociation(
    name="siblings10",
    ends={
        Property(name="FamiliesWithSiblings_Family", type=FamiliesWithSiblings_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="FamiliesWithSiblings_Family9", type=FamiliesWithSiblings_Family, multiplicity=Multiplicity(0, 5))
    }
)
fatherInverse11: BinaryAssociation = BinaryAssociation(
    name="fatherInverse11",
    ends={
        Property(name="Family12", type=FamiliesWithSiblings_FamilyMember, multiplicity=Multiplicity(1, 1)),
        Property(name="father", type=FamiliesWithSiblings_Family, multiplicity=Multiplicity(0, 1))
    }
)
motherInverse13: BinaryAssociation = BinaryAssociation(
    name="motherInverse13",
    ends={
        Property(name="Family14", type=FamiliesWithSiblings_FamilyMember, multiplicity=Multiplicity(1, 1)),
        Property(name="mother", type=FamiliesWithSiblings_Family, multiplicity=Multiplicity(0, 1))
    }
)
sonsInverse15: BinaryAssociation = BinaryAssociation(
    name="sonsInverse15",
    ends={
        Property(name="Family16", type=FamiliesWithSiblings_FamilyMember, multiplicity=Multiplicity(1, 1)),
        Property(name="sons", type=FamiliesWithSiblings_Family, multiplicity=Multiplicity(0, 1))
    }
)
daughtersInverse17: BinaryAssociation = BinaryAssociation(
    name="daughtersInverse17",
    ends={
        Property(name="Family18", type=FamiliesWithSiblings_FamilyMember, multiplicity=Multiplicity(1, 1)),
        Property(name="daughters", type=FamiliesWithSiblings_Family, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="FamiliesWithSiblings",
    types={FamiliesWithSiblings_Family, FamiliesWithSiblings_FamilyMember, FamiliesWithSiblings_FamilyRegister},
    associations={families0, father1, mother2, sons4, daughters6, familiesInverse8, siblings10, fatherInverse11, motherInverse13, sonsInverse15, daughtersInverse17},
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