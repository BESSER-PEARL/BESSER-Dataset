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
Families_FamilyRegister = Class(name="Families::FamilyRegister")
Families_Family = Class(name="Families::Family")
Families_FamilyMember = Class(name="Families::FamilyMember")

# Families_FamilyRegister class attributes and methods

# Families_Family class attributes and methods
Families_Family_name: Property = Property(name="name", type=StringType)
Families_Family.attributes={Families_Family_name}

# Families_FamilyMember class attributes and methods
Families_FamilyMember_name: Property = Property(name="name", type=StringType)
Families_FamilyMember.attributes={Families_FamilyMember_name}

# Relationships
families0: BinaryAssociation = BinaryAssociation(
    name="families0",
    ends={
        Property(name="Family", type=Families_FamilyRegister, multiplicity=Multiplicity(1, 1)),
        Property(name="familiesInverse", type=Families_Family, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sons4: BinaryAssociation = BinaryAssociation(
    name="sons4",
    ends={
        Property(name="FamilyMember5", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="sonsInverse", type=Families_FamilyMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
daughters6: BinaryAssociation = BinaryAssociation(
    name="daughters6",
    ends={
        Property(name="FamilyMember7", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="daughtersInverse", type=Families_FamilyMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
familiesInverse8: BinaryAssociation = BinaryAssociation(
    name="familiesInverse8",
    ends={
        Property(name="FamilyRegister", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="families", type=Families_FamilyRegister, multiplicity=Multiplicity(0, 1))
    }
)
fatherInverse9: BinaryAssociation = BinaryAssociation(
    name="fatherInverse9",
    ends={
        Property(name="Family10", type=Families_FamilyMember, multiplicity=Multiplicity(1, 1)),
        Property(name="father", type=Families_Family, multiplicity=Multiplicity(0, 1))
    }
)
motherInverse11: BinaryAssociation = BinaryAssociation(
    name="motherInverse11",
    ends={
        Property(name="Family12", type=Families_FamilyMember, multiplicity=Multiplicity(1, 1)),
        Property(name="mother", type=Families_Family, multiplicity=Multiplicity(0, 1))
    }
)
sonsInverse13: BinaryAssociation = BinaryAssociation(
    name="sonsInverse13",
    ends={
        Property(name="Family14", type=Families_FamilyMember, multiplicity=Multiplicity(1, 1)),
        Property(name="sons", type=Families_Family, multiplicity=Multiplicity(0, 1))
    }
)
daughtersInverse15: BinaryAssociation = BinaryAssociation(
    name="daughtersInverse15",
    ends={
        Property(name="Family16", type=Families_FamilyMember, multiplicity=Multiplicity(1, 1)),
        Property(name="daughters", type=Families_Family, multiplicity=Multiplicity(0, 1))
    }
)
father1: BinaryAssociation = BinaryAssociation(
    name="father1",
    ends={
        Property(name="FamilyMember", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="fatherInverse", type=Families_FamilyMember, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mother2: BinaryAssociation = BinaryAssociation(
    name="mother2",
    ends={
        Property(name="FamilyMember3", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="motherInverse", type=Families_FamilyMember, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="Families",
    types={Families_FamilyRegister, Families_Family, Families_FamilyMember},
    associations={families0, sons4, daughters6, familiesInverse8, fatherInverse9, motherInverse11, sonsInverse13, daughtersInverse15, father1, mother2},
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