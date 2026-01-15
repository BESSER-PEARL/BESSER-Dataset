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
household_HouseholdRoot = Class(name="household::HouseholdRoot")
household_Family = Class(name="household::Family")
household_Member = Class(name="household::Member")

# household_HouseholdRoot class attributes and methods

# household_Family class attributes and methods
household_Family_name: Property = Property(name="name", type=StringType)
household_Family.attributes={household_Family_name}

# household_Member class attributes and methods
household_Member_name: Property = Property(name="name", type=StringType)
household_Member.attributes={household_Member_name}

# Relationships
have0: BinaryAssociation = BinaryAssociation(
    name="have0",
    ends={
        Property(name="household_Family", type=household_HouseholdRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="household_HouseholdRoot", type=household_Family, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
father1: BinaryAssociation = BinaryAssociation(
    name="father1",
    ends={
        Property(name="household_Member", type=household_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="household_Family2", type=household_Member, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mother3: BinaryAssociation = BinaryAssociation(
    name="mother3",
    ends={
        Property(name="household_Member5", type=household_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="household_Family4", type=household_Member, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
son6: BinaryAssociation = BinaryAssociation(
    name="son6",
    ends={
        Property(name="household_Member8", type=household_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="household_Family7", type=household_Member, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
daughter9: BinaryAssociation = BinaryAssociation(
    name="daughter9",
    ends={
        Property(name="household_Member11", type=household_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="household_Family10", type=household_Member, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="household",
    types={household_HouseholdRoot, household_Family, household_Member},
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