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
ref_A = Class(name="ref_A")
ref_B = Class(name="ref_B")
ref_C2 = Class(name="ref_C2")
ref_C = Class(name="ref_C")
ref_D = Class(name="ref_D")
ref_C1 = Class(name="ref_C1")
ref_C4 = Class(name="ref_C4")
ref_E = Class(name="ref_E")
ref_C3 = Class(name="ref_C3")
ref_unsettable_C1U = Class(name="ref_unsettable_C1U")
AU = Class(name="AU")
BU = Class(name="BU")
ref_unsettable_C2U = Class(name="ref_unsettable_C2U")
ref_unsettable_AU = Class(name="ref_unsettable_AU")
C2U = Class(name="C2U")
CU = Class(name="CU")
ref_unsettable_BU = Class(name="ref_unsettable_BU")
DU = Class(name="DU")
ref_unsettable_CU = Class(name="ref_unsettable_CU")
C4U = Class(name="C4U")
ref_unsettable_DU = Class(name="ref_unsettable_DU")
EU = Class(name="EU")
ref_unsettable_C4U = Class(name="ref_unsettable_C4U")
ref_unsettable_C3U = Class(name="ref_unsettable_C3U")
ref_unsettable_EU = Class(name="ref_unsettable_EU")

# ref_A class attributes and methods

# ref_B class attributes and methods

# ref_C2 class attributes and methods

# ref_C class attributes and methods

# ref_D class attributes and methods

# ref_C1 class attributes and methods

# ref_C4 class attributes and methods

# ref_E class attributes and methods
ref_E_name: Property = Property(name="name", type=StringType)
ref_E_ids: Property = Property(name="ids", type=StringType)
ref_E_labels: Property = Property(name="labels", type=StringType)
ref_E.attributes={ref_E_labels, ref_E_ids, ref_E_name}

# ref_C3 class attributes and methods

# ref_unsettable_C1U class attributes and methods

# AU class attributes and methods

# BU class attributes and methods

# ref_unsettable_C2U class attributes and methods

# ref_unsettable_AU class attributes and methods

# C2U class attributes and methods

# CU class attributes and methods

# ref_unsettable_BU class attributes and methods

# DU class attributes and methods

# ref_unsettable_CU class attributes and methods

# C4U class attributes and methods

# ref_unsettable_DU class attributes and methods

# EU class attributes and methods

# ref_unsettable_C4U class attributes and methods

# ref_unsettable_C3U class attributes and methods

# ref_unsettable_EU class attributes and methods
ref_unsettable_EU_name: Property = Property(name="name", type=StringType)
ref_unsettable_EU_ids: Property = Property(name="ids", type=StringType)
ref_unsettable_EU_labels: Property = Property(name="labels", type=StringType)
ref_unsettable_EU.attributes={ref_unsettable_EU_name, ref_unsettable_EU_ids, ref_unsettable_EU_labels}

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
        Property(name="AU44", type=ref_unsettable_C2U, multiplicity=Multiplicity(1, 1)),
        Property(name="c2u", type=AU, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bu45: BinaryAssociation = BinaryAssociation(
    name="bu45",
    ends={
        Property(name="BU47", type=ref_unsettable_C2U, multiplicity=Multiplicity(1, 1)),
        Property(name="c2u46", type=BU, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bu48: BinaryAssociation = BinaryAssociation(
    name="bu48",
    ends={
        Property(name="BU49", type=ref_unsettable_AU, multiplicity=Multiplicity(1, 1)),
        Property(name="au", type=BU, multiplicity=Multiplicity(1, 1))
    }
)
c2u50: BinaryAssociation = BinaryAssociation(
    name="c2u50",
    ends={
        Property(name="C2U", type=ref_unsettable_AU, multiplicity=Multiplicity(1, 1)),
        Property(name="au51", type=C2U, multiplicity=Multiplicity(0, 1))
    }
)
cu52: BinaryAssociation = BinaryAssociation(
    name="cu52",
    ends={
        Property(name="CU", type=ref_unsettable_AU, multiplicity=Multiplicity(1, 1)),
        Property(name="ref_unsettable_AU", type=CU, multiplicity=Multiplicity(0, 1))
    }
)
au53: BinaryAssociation = BinaryAssociation(
    name="au53",
    ends={
        Property(name="AU54", type=ref_unsettable_BU, multiplicity=Multiplicity(1, 1)),
        Property(name="bu", type=AU, multiplicity=Multiplicity(1, 1))
    }
)
c2u55: BinaryAssociation = BinaryAssociation(
    name="c2u55",
    ends={
        Property(name="C2U57", type=ref_unsettable_BU, multiplicity=Multiplicity(1, 1)),
        Property(name="bu56", type=C2U, multiplicity=Multiplicity(0, 1))
    }
)
du58: BinaryAssociation = BinaryAssociation(
    name="du58",
    ends={
        Property(name="DU", type=ref_unsettable_BU, multiplicity=Multiplicity(1, 1)),
        Property(name="ref_unsettable_BU", type=DU, multiplicity=Multiplicity(0, 9999))
    }
)
du59: BinaryAssociation = BinaryAssociation(
    name="du59",
    ends={
        Property(name="DU60", type=ref_unsettable_CU, multiplicity=Multiplicity(1, 1)),
        Property(name="cu", type=DU, multiplicity=Multiplicity(0, 9999))
    }
)
c4u61: BinaryAssociation = BinaryAssociation(
    name="c4u61",
    ends={
        Property(name="C4U", type=ref_unsettable_CU, multiplicity=Multiplicity(1, 1)),
        Property(name="cu62", type=C4U, multiplicity=Multiplicity(0, 1))
    }
)
cu63: BinaryAssociation = BinaryAssociation(
    name="cu63",
    ends={
        Property(name="CU64", type=ref_unsettable_DU, multiplicity=Multiplicity(1, 1)),
        Property(name="du", type=CU, multiplicity=Multiplicity(1, 1))
    }
)
c4u65: BinaryAssociation = BinaryAssociation(
    name="c4u65",
    ends={
        Property(name="C4U67", type=ref_unsettable_DU, multiplicity=Multiplicity(1, 1)),
        Property(name="du66", type=C4U, multiplicity=Multiplicity(0, 1))
    }
)
eu68: BinaryAssociation = BinaryAssociation(
    name="eu68",
    ends={
        Property(name="EU", type=ref_unsettable_DU, multiplicity=Multiplicity(1, 1)),
        Property(name="du69", type=EU, multiplicity=Multiplicity(0, 9999))
    }
)
cu70: BinaryAssociation = BinaryAssociation(
    name="cu70",
    ends={
        Property(name="CU71", type=ref_unsettable_C4U, multiplicity=Multiplicity(1, 1)),
        Property(name="c4u", type=CU, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
du72: BinaryAssociation = BinaryAssociation(
    name="du72",
    ends={
        Property(name="DU74", type=ref_unsettable_C4U, multiplicity=Multiplicity(1, 1)),
        Property(name="c4u73", type=DU, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cu75: BinaryAssociation = BinaryAssociation(
    name="cu75",
    ends={
        Property(name="CU76", type=ref_unsettable_C3U, multiplicity=Multiplicity(1, 1)),
        Property(name="ref_unsettable_C3U", type=CU, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
c37: BinaryAssociation = BinaryAssociation(
    name="c37",
    ends={
        Property(name="ref_C39", type=ref_C3, multiplicity=Multiplicity(1, 1)),
        Property(name="ref_C338", type=ref_C, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
du77: BinaryAssociation = BinaryAssociation(
    name="du77",
    ends={
        Property(name="DU79", type=ref_unsettable_C3U, multiplicity=Multiplicity(1, 1)),
        Property(name="ref_unsettable_C3U78", type=DU, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
du80: BinaryAssociation = BinaryAssociation(
    name="du80",
    ends={
        Property(name="DU81", type=ref_unsettable_EU, multiplicity=Multiplicity(1, 1)),
        Property(name="eu", type=DU, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="ref",
    types={ref_A, ref_B, ref_C2, ref_C, ref_D, ref_C1, ref_C4, ref_E, ref_C3, ref_unsettable_C1U, AU, BU, ref_unsettable_C2U, ref_unsettable_AU, C2U, CU, ref_unsettable_BU, DU, ref_unsettable_CU, C4U, ref_unsettable_DU, EU, ref_unsettable_C4U, ref_unsettable_C3U, ref_unsettable_EU},
    associations={b0, c21, c3, a4, c25, d8, a9, b11, b14, a16, d19, c420, c22, e23, c425, d28, c30, d32, d35, au40, bu41, au43, bu45, bu48, c2u50, cu52, au53, c2u55, du58, du59, c4u61, cu63, c4u65, eu68, cu70, du72, cu75, c37, du77, du80},
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