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
ref_C2 = Class(name="ref::C2")
ref_C = Class(name="ref::C")
ref_D = Class(name="ref::D")
ref_C1 = Class(name="ref::C1")
ref_C4 = Class(name="ref::C4")
ref_A = Class(name="ref::A")
ref_B = Class(name="ref::B")
ref_C3 = Class(name="ref::C3")
ref_unsettable_C1U = Class(name="ref::unsettable::C1U")
AU = Class(name="AU")
BU = Class(name="BU")
ref_unsettable_C2U = Class(name="ref::unsettable::C2U")
ref_unsettable_AU = Class(name="ref::unsettable::AU")
ref_E = Class(name="ref::E")
DU = Class(name="DU")
ref_unsettable_CU = Class(name="ref::unsettable::CU")
C4U = Class(name="C4U")
ref_unsettable_DU = Class(name="ref::unsettable::DU")
EU = Class(name="EU")
ref_unsettable_C4U = Class(name="ref::unsettable::C4U")
ref_unsettable_C3U = Class(name="ref::unsettable::C3U")
C2U = Class(name="C2U")
CU = Class(name="CU")
ref_unsettable_BU = Class(name="ref::unsettable::BU")
ref_unsettable_EU = Class(name="ref::unsettable::EU")

# ref_C2 class attributes and methods

# ref_C class attributes and methods

# ref_D class attributes and methods

# ref_C1 class attributes and methods

# ref_C4 class attributes and methods

# ref_A class attributes and methods

# ref_B class attributes and methods

# ref_C3 class attributes and methods

# ref_unsettable_C1U class attributes and methods

# AU class attributes and methods

# BU class attributes and methods

# ref_unsettable_C2U class attributes and methods

# ref_unsettable_AU class attributes and methods

# ref_E class attributes and methods
ref_E_ids: Property = Property(name="ids", type=StringType)
ref_E_labels: Property = Property(name="labels", type=StringType)
ref_E_name: Property = Property(name="name", type=StringType)
ref_E.attributes={ref_E_name, ref_E_labels, ref_E_ids}

# DU class attributes and methods

# ref_unsettable_CU class attributes and methods

# C4U class attributes and methods

# ref_unsettable_DU class attributes and methods

# EU class attributes and methods

# ref_unsettable_C4U class attributes and methods

# ref_unsettable_C3U class attributes and methods

# C2U class attributes and methods

# CU class attributes and methods

# ref_unsettable_BU class attributes and methods

# ref_unsettable_EU class attributes and methods
ref_unsettable_EU_name: Property = Property(name="name", type=StringType)
ref_unsettable_EU_ids: Property = Property(name="ids", type=StringType)
ref_unsettable_EU_labels: Property = Property(name="labels", type=StringType)
ref_unsettable_EU.attributes={ref_unsettable_EU_ids, ref_unsettable_EU_name, ref_unsettable_EU_labels}

# Relationships
b0: BinaryAssociation = BinaryAssociation(
    name="b0",
    ends={
        Property(name="B", type=ref_A, multiplicity=Multiplicity(1, 1)),
        Property(name="a", type=ref_B, multiplicity=Multiplicity(1, 1))
    }
)
c21: BinaryAssociation = BinaryAssociation(
    name="c21",
    ends={
        Property(name="C2", type=ref_A, multiplicity=Multiplicity(1, 1)),
        Property(name="a2", type=ref_C2, multiplicity=Multiplicity(0, 1))
    }
)
c3: BinaryAssociation = BinaryAssociation(
    name="c3",
    ends={
        Property(name="ref_C", type=ref_A, multiplicity=Multiplicity(1, 1)),
        Property(name="ref_A", type=ref_C, multiplicity=Multiplicity(1, 1))
    }
)
a4: BinaryAssociation = BinaryAssociation(
    name="a4",
    ends={
        Property(name="A", type=ref_B, multiplicity=Multiplicity(1, 1)),
        Property(name="b", type=ref_A, multiplicity=Multiplicity(1, 1))
    }
)
c25: BinaryAssociation = BinaryAssociation(
    name="c25",
    ends={
        Property(name="C27", type=ref_B, multiplicity=Multiplicity(1, 1)),
        Property(name="b6", type=ref_C2, multiplicity=Multiplicity(0, 1))
    }
)
d8: BinaryAssociation = BinaryAssociation(
    name="d8",
    ends={
        Property(name="ref_D", type=ref_B, multiplicity=Multiplicity(1, 1)),
        Property(name="ref_B", type=ref_D, multiplicity=Multiplicity(0, 9999))
    }
)
a9: BinaryAssociation = BinaryAssociation(
    name="a9",
    ends={
        Property(name="ref_A10", type=ref_C1, multiplicity=Multiplicity(1, 1)),
        Property(name="ref_C1", type=ref_A, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
b11: BinaryAssociation = BinaryAssociation(
    name="b11",
    ends={
        Property(name="ref_B13", type=ref_C1, multiplicity=Multiplicity(1, 1)),
        Property(name="ref_C112", type=ref_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
b14: BinaryAssociation = BinaryAssociation(
    name="b14",
    ends={
        Property(name="B15", type=ref_C2, multiplicity=Multiplicity(1, 1)),
        Property(name="c2", type=ref_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
a16: BinaryAssociation = BinaryAssociation(
    name="a16",
    ends={
        Property(name="A18", type=ref_C2, multiplicity=Multiplicity(1, 1)),
        Property(name="c217", type=ref_A, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
d19: BinaryAssociation = BinaryAssociation(
    name="d19",
    ends={
        Property(name="D", type=ref_C, multiplicity=Multiplicity(1, 1)),
        Property(name="c", type=ref_D, multiplicity=Multiplicity(0, 9999))
    }
)
c420: BinaryAssociation = BinaryAssociation(
    name="c420",
    ends={
        Property(name="C4", type=ref_C, multiplicity=Multiplicity(1, 1)),
        Property(name="c21", type=ref_C4, multiplicity=Multiplicity(0, 1))
    }
)
d28: BinaryAssociation = BinaryAssociation(
    name="d28",
    ends={
        Property(name="D29", type=ref_E, multiplicity=Multiplicity(1, 1)),
        Property(name="e", type=ref_D, multiplicity=Multiplicity(0, 9999))
    }
)
c30: BinaryAssociation = BinaryAssociation(
    name="c30",
    ends={
        Property(name="C31", type=ref_C4, multiplicity=Multiplicity(1, 1)),
        Property(name="c4", type=ref_C, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
d32: BinaryAssociation = BinaryAssociation(
    name="d32",
    ends={
        Property(name="D34", type=ref_C4, multiplicity=Multiplicity(1, 1)),
        Property(name="c433", type=ref_D, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
d35: BinaryAssociation = BinaryAssociation(
    name="d35",
    ends={
        Property(name="ref_D36", type=ref_C3, multiplicity=Multiplicity(1, 1)),
        Property(name="ref_C3", type=ref_D, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
c37: BinaryAssociation = BinaryAssociation(
    name="c37",
    ends={
        Property(name="ref_C39", type=ref_C3, multiplicity=Multiplicity(1, 1)),
        Property(name="ref_C338", type=ref_C, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
au40: BinaryAssociation = BinaryAssociation(
    name="au40",
    ends={
        Property(name="AU", type=ref_unsettable_C1U, multiplicity=Multiplicity(1, 1)),
        Property(name="ref_unsettable_C1U", type=AU, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bu41: BinaryAssociation = BinaryAssociation(
    name="bu41",
    ends={
        Property(name="BU", type=ref_unsettable_C1U, multiplicity=Multiplicity(1, 1)),
        Property(name="ref_unsettable_C1U42", type=BU, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
au43: BinaryAssociation = BinaryAssociation(
    name="au43",
    ends={
        Property(name="unsettable", type=ref_unsettable_C2U, multiplicity=Multiplicity(1, 1)),
        Property(name="AU44", type=AU, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bu45: BinaryAssociation = BinaryAssociation(
    name="bu45",
    ends={
        Property(name="unsettable47", type=ref_unsettable_C2U, multiplicity=Multiplicity(1, 1)),
        Property(name="BU46", type=BU, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bu48: BinaryAssociation = BinaryAssociation(
    name="bu48",
    ends={
        Property(name="unsettable50", type=ref_unsettable_AU, multiplicity=Multiplicity(1, 1)),
        Property(name="BU49", type=BU, multiplicity=Multiplicity(1, 1))
    }
)
c22: BinaryAssociation = BinaryAssociation(
    name="c22",
    ends={
        Property(name="C", type=ref_D, multiplicity=Multiplicity(1, 1)),
        Property(name="d", type=ref_C, multiplicity=Multiplicity(1, 1))
    }
)
e23: BinaryAssociation = BinaryAssociation(
    name="e23",
    ends={
        Property(name="E", type=ref_D, multiplicity=Multiplicity(1, 1)),
        Property(name="d24", type=ref_E, multiplicity=Multiplicity(0, 9999))
    }
)
c425: BinaryAssociation = BinaryAssociation(
    name="c425",
    ends={
        Property(name="C427", type=ref_D, multiplicity=Multiplicity(1, 1)),
        Property(name="d26", type=ref_C4, multiplicity=Multiplicity(0, 1))
    }
)
au54: BinaryAssociation = BinaryAssociation(
    name="au54",
    ends={
        Property(name="unsettable56", type=ref_unsettable_BU, multiplicity=Multiplicity(1, 1)),
        Property(name="AU55", type=AU, multiplicity=Multiplicity(1, 1))
    }
)
c2u57: BinaryAssociation = BinaryAssociation(
    name="c2u57",
    ends={
        Property(name="unsettable59", type=ref_unsettable_BU, multiplicity=Multiplicity(1, 1)),
        Property(name="C2U58", type=C2U, multiplicity=Multiplicity(0, 1))
    }
)
du60: BinaryAssociation = BinaryAssociation(
    name="du60",
    ends={
        Property(name="DU", type=ref_unsettable_BU, multiplicity=Multiplicity(1, 1)),
        Property(name="ref_unsettable_BU", type=DU, multiplicity=Multiplicity(0, 9999))
    }
)
du61: BinaryAssociation = BinaryAssociation(
    name="du61",
    ends={
        Property(name="unsettable63", type=ref_unsettable_CU, multiplicity=Multiplicity(1, 1)),
        Property(name="DU62", type=DU, multiplicity=Multiplicity(0, 9999))
    }
)
c4u64: BinaryAssociation = BinaryAssociation(
    name="c4u64",
    ends={
        Property(name="unsettable65", type=ref_unsettable_CU, multiplicity=Multiplicity(1, 1)),
        Property(name="C4U", type=C4U, multiplicity=Multiplicity(0, 1))
    }
)
cu66: BinaryAssociation = BinaryAssociation(
    name="cu66",
    ends={
        Property(name="unsettable68", type=ref_unsettable_DU, multiplicity=Multiplicity(1, 1)),
        Property(name="CU67", type=CU, multiplicity=Multiplicity(1, 1))
    }
)
c4u69: BinaryAssociation = BinaryAssociation(
    name="c4u69",
    ends={
        Property(name="unsettable71", type=ref_unsettable_DU, multiplicity=Multiplicity(1, 1)),
        Property(name="C4U70", type=C4U, multiplicity=Multiplicity(0, 1))
    }
)
eu72: BinaryAssociation = BinaryAssociation(
    name="eu72",
    ends={
        Property(name="unsettable73", type=ref_unsettable_DU, multiplicity=Multiplicity(1, 1)),
        Property(name="EU", type=EU, multiplicity=Multiplicity(0, 9999))
    }
)
cu74: BinaryAssociation = BinaryAssociation(
    name="cu74",
    ends={
        Property(name="unsettable76", type=ref_unsettable_C4U, multiplicity=Multiplicity(1, 1)),
        Property(name="CU75", type=CU, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
du77: BinaryAssociation = BinaryAssociation(
    name="du77",
    ends={
        Property(name="unsettable79", type=ref_unsettable_C4U, multiplicity=Multiplicity(1, 1)),
        Property(name="DU78", type=DU, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cu80: BinaryAssociation = BinaryAssociation(
    name="cu80",
    ends={
        Property(name="CU81", type=ref_unsettable_C3U, multiplicity=Multiplicity(1, 1)),
        Property(name="ref_unsettable_C3U", type=CU, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
c2u51: BinaryAssociation = BinaryAssociation(
    name="c2u51",
    ends={
        Property(name="unsettable52", type=ref_unsettable_AU, multiplicity=Multiplicity(1, 1)),
        Property(name="C2U", type=C2U, multiplicity=Multiplicity(0, 1))
    }
)
cu53: BinaryAssociation = BinaryAssociation(
    name="cu53",
    ends={
        Property(name="CU", type=ref_unsettable_AU, multiplicity=Multiplicity(1, 1)),
        Property(name="ref_unsettable_AU", type=CU, multiplicity=Multiplicity(0, 1))
    }
)
du85: BinaryAssociation = BinaryAssociation(
    name="du85",
    ends={
        Property(name="unsettable87", type=ref_unsettable_EU, multiplicity=Multiplicity(1, 1)),
        Property(name="DU86", type=DU, multiplicity=Multiplicity(0, 9999))
    }
)
du82: BinaryAssociation = BinaryAssociation(
    name="du82",
    ends={
        Property(name="DU84", type=ref_unsettable_C3U, multiplicity=Multiplicity(1, 1)),
        Property(name="ref_unsettable_C3U83", type=DU, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="ref",
    types={ref_C2, ref_C, ref_D, ref_C1, ref_C4, ref_A, ref_B, ref_C3, ref_unsettable_C1U, AU, BU, ref_unsettable_C2U, ref_unsettable_AU, ref_E, DU, ref_unsettable_CU, C4U, ref_unsettable_DU, EU, ref_unsettable_C4U, ref_unsettable_C3U, C2U, CU, ref_unsettable_BU, ref_unsettable_EU},
    associations={b0, c21, c3, a4, c25, d8, a9, b11, b14, a16, d19, c420, d28, c30, d32, d35, c37, au40, bu41, au43, bu45, bu48, c22, e23, c425, au54, c2u57, du60, du61, c4u64, cu66, c4u69, eu72, cu74, du77, cu80, c2u51, cu53, du85, du82},
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