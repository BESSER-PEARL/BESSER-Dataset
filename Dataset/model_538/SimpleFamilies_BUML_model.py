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
SimpleFamilies_FamilyMember = Class(name="SimpleFamilies::FamilyMember")
SimpleFamilies_FamilyRegister = Class(name="SimpleFamilies::FamilyRegister")
SimpleFamilies_Family = Class(name="SimpleFamilies::Family")

# SimpleFamilies_FamilyMember class attributes and methods
SimpleFamilies_FamilyMember_name: Property = Property(name="name", type=StringType)
SimpleFamilies_FamilyMember.attributes={SimpleFamilies_FamilyMember_name}

# SimpleFamilies_FamilyRegister class attributes and methods

# SimpleFamilies_Family class attributes and methods
SimpleFamilies_Family_name: Property = Property(name="name", type=StringType)
SimpleFamilies_Family.attributes={SimpleFamilies_Family_name}

# Relationships
father1: BinaryAssociation = BinaryAssociation(
    name="father1",
    ends={
        Property(name="SimpleFamilies_FamilyMember", type=SimpleFamilies_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleFamilies_Family2", type=SimpleFamilies_FamilyMember, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
families0: BinaryAssociation = BinaryAssociation(
    name="families0",
    ends={
        Property(name="SimpleFamilies_Family", type=SimpleFamilies_FamilyRegister, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleFamilies_FamilyRegister", type=SimpleFamilies_Family, multiplicity=Multiplicity(0, 5), is_composite=True)
    }
)
mother3: BinaryAssociation = BinaryAssociation(
    name="mother3",
    ends={
        Property(name="SimpleFamilies_FamilyMember5", type=SimpleFamilies_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleFamilies_Family4", type=SimpleFamilies_FamilyMember, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sons6: BinaryAssociation = BinaryAssociation(
    name="sons6",
    ends={
        Property(name="SimpleFamilies_FamilyMember8", type=SimpleFamilies_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleFamilies_Family7", type=SimpleFamilies_FamilyMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
daughters9: BinaryAssociation = BinaryAssociation(
    name="daughters9",
    ends={
        Property(name="SimpleFamilies_FamilyMember11", type=SimpleFamilies_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleFamilies_Family10", type=SimpleFamilies_FamilyMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="SimpleFamilies",
    types={SimpleFamilies_FamilyMember, SimpleFamilies_FamilyRegister, SimpleFamilies_Family},
    associations={father1, families0, mother3, sons6, daughters9},
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