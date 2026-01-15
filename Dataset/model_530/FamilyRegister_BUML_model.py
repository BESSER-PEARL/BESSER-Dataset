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
FamilyRegister_FamilyRegister = Class(name="FamilyRegister::FamilyRegister")
FamilyRegister_Family = Class(name="FamilyRegister::Family")
FamilyRegister_Member = Class(name="FamilyRegister::Member")

# FamilyRegister_FamilyRegister class attributes and methods

# FamilyRegister_Family class attributes and methods
FamilyRegister_Family_name: Property = Property(name="name", type=StringType)
FamilyRegister_Family.attributes={FamilyRegister_Family_name}

# FamilyRegister_Member class attributes and methods
FamilyRegister_Member_name: Property = Property(name="name", type=StringType)
FamilyRegister_Member.attributes={FamilyRegister_Member_name}

# Relationships
mother1: BinaryAssociation = BinaryAssociation(
    name="mother1",
    ends={
        Property(name="FamilyRegister_Member", type=FamilyRegister_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="FamilyRegister_Family2", type=FamilyRegister_Member, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
father3: BinaryAssociation = BinaryAssociation(
    name="father3",
    ends={
        Property(name="FamilyRegister_Member5", type=FamilyRegister_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="FamilyRegister_Family4", type=FamilyRegister_Member, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
families0: BinaryAssociation = BinaryAssociation(
    name="families0",
    ends={
        Property(name="FamilyRegister_Family", type=FamilyRegister_FamilyRegister, multiplicity=Multiplicity(1, 1)),
        Property(name="FamilyRegister_FamilyRegister", type=FamilyRegister_Family, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
daughter9: BinaryAssociation = BinaryAssociation(
    name="daughter9",
    ends={
        Property(name="FamilyRegister_Member11", type=FamilyRegister_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="FamilyRegister_Family10", type=FamilyRegister_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
son6: BinaryAssociation = BinaryAssociation(
    name="son6",
    ends={
        Property(name="FamilyRegister_Member8", type=FamilyRegister_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="FamilyRegister_Family7", type=FamilyRegister_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="FamilyRegister",
    types={FamilyRegister_FamilyRegister, FamilyRegister_Family, FamilyRegister_Member},
    associations={mother1, father3, families0, daughter9, son6},
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