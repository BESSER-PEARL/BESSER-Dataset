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
FamilyMModel_Family = Class(name="FamilyMModel::Family")
FamilyMModel_Member = Class(name="FamilyMModel::Member")

# FamilyMModel_Family class attributes and methods
FamilyMModel_Family_lastName: Property = Property(name="lastName", type=StringType)
FamilyMModel_Family.attributes={FamilyMModel_Family_lastName}

# FamilyMModel_Member class attributes and methods
FamilyMModel_Member_firstName: Property = Property(name="firstName", type=StringType)
FamilyMModel_Member_relation: Property = Property(name="relation", type=StringType)
FamilyMModel_Member.attributes={FamilyMModel_Member_relation, FamilyMModel_Member_firstName}

# Relationships
member0: BinaryAssociation = BinaryAssociation(
    name="member0",
    ends={
        Property(name="FamilyMModel_Member", type=FamilyMModel_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="FamilyMModel_Family", type=FamilyMModel_Member, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="FamilyMModel",
    types={FamilyMModel_Family, FamilyMModel_Member},
    associations={member0},
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