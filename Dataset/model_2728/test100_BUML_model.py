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
test100_B = Class(name="test100::B")
test100_DsmlRelation = Class(name="test100::DsmlRelation")
test100_C = Class(name="test100::C")
test100_A = Class(name="test100::A")
B = Class(name="B")

# test100_B class attributes and methods
test100_B_id: Property = Property(name="id", type=StringType)
test100_B.attributes={test100_B_id}

# test100_DsmlRelation class attributes and methods
test100_DsmlRelation_name: Property = Property(name="name", type=StringType)
test100_DsmlRelation_mandatory: Property = Property(name="mandatory", type=BooleanType)
test100_DsmlRelation_details: Property = Property(name="details", type=StringType)
test100_DsmlRelation.attributes={test100_DsmlRelation_details, test100_DsmlRelation_mandatory, test100_DsmlRelation_name}

# test100_C class attributes and methods

# test100_A class attributes and methods
test100_A_name: Property = Property(name="name", type=StringType)
test100_A.attributes={test100_A_name}

# B class attributes and methods

# Relationships
bs1: BinaryAssociation = BinaryAssociation(
    name="bs1",
    ends={
        Property(name="test100_B", type=test100_A, multiplicity=Multiplicity(1, 1)),
        Property(name="test100_A2", type=test100_B, multiplicity=Multiplicity(0, 9999))
    }
)
relateds3: BinaryAssociation = BinaryAssociation(
    name="relateds3",
    ends={
        Property(name="test100_DsmlRelation", type=test100_A, multiplicity=Multiplicity(1, 1)),
        Property(name="test100_A4", type=test100_DsmlRelation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
as0: BinaryAssociation = BinaryAssociation(
    name="as0",
    ends={
        Property(name="test100_A", type=test100_C, multiplicity=Multiplicity(1, 1)),
        Property(name="test100_C", type=test100_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromDsml5: BinaryAssociation = BinaryAssociation(
    name="fromDsml5",
    ends={
        Property(name="test100_A7", type=test100_DsmlRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="test100_DsmlRelation6", type=test100_A, multiplicity=Multiplicity(0, 1))
    }
)
toDsml8: BinaryAssociation = BinaryAssociation(
    name="toDsml8",
    ends={
        Property(name="test100_A10", type=test100_DsmlRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="test100_DsmlRelation9", type=test100_A, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_test100_A_B = Generalization(general=B, specific=test100_A)

# Domain Model
domain_model = DomainModel(
    name="test100",
    types={test100_B, test100_DsmlRelation, test100_C, test100_A, B},
    associations={bs1, relateds3, as0, fromDsml5, toDsml8},
    generalizations={gen_test100_A_B},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)