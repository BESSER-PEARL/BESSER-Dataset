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
Household_HouseholdRoot = Class(name="Household::HouseholdRoot")
Household_Family = Class(name="Household::Family")
Household_Member = Class(name="Household::Member")

# Household_HouseholdRoot class attributes and methods

# Household_Family class attributes and methods
Household_Family_lastName: Property = Property(name="lastName", type=StringType)
Household_Family.attributes={Household_Family_lastName}

# Household_Member class attributes and methods
Household_Member_firstName: Property = Property(name="firstName", type=StringType)
Household_Member.attributes={Household_Member_firstName}

# Relationships
have0: BinaryAssociation = BinaryAssociation(
    name="have0",
    ends={
        Property(name="Household_Family", type=Household_HouseholdRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Household_HouseholdRoot", type=Household_Family, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
father1: BinaryAssociation = BinaryAssociation(
    name="father1",
    ends={
        Property(name="Household_Member", type=Household_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="Household_Family2", type=Household_Member, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mother3: BinaryAssociation = BinaryAssociation(
    name="mother3",
    ends={
        Property(name="Household_Member5", type=Household_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="Household_Family4", type=Household_Member, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
son6: BinaryAssociation = BinaryAssociation(
    name="son6",
    ends={
        Property(name="Household_Member8", type=Household_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="Household_Family7", type=Household_Member, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
daughter9: BinaryAssociation = BinaryAssociation(
    name="daughter9",
    ends={
        Property(name="Household_Member11", type=Household_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="Household_Family10", type=Household_Member, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="Household",
    types={Household_HouseholdRoot, Household_Family, Household_Member},
    associations={have0, father1, mother3, son6, daughter9},
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