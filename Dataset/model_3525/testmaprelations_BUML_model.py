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
testmaprelations_CB0 = Class(name="testmaprelations::CB0")
testmaprelations_MapCA1ToCB1MapEntry = Class(name="testmaprelations::MapCA1ToCB1MapEntry")
testmaprelations_CA1 = Class(name="testmaprelations::CA1")
testmaprelations_CB1 = Class(name="testmaprelations::CB1")
testmaprelations_CA2 = Class(name="testmaprelations::CA2")
testmaprelations_MapCA2ToCB2MapEntry = Class(name="testmaprelations::MapCA2ToCB2MapEntry")
testmaprelations_CB2 = Class(name="testmaprelations::CB2")
testmaprelations_MapCA0ToCB0MapEntry = Class(name="testmaprelations::MapCA0ToCB0MapEntry")
testmaprelations_CA0 = Class(name="testmaprelations::CA0")
testmaprelations_MapCA3ToCB3MapEntry = Class(name="testmaprelations::MapCA3ToCB3MapEntry")
testmaprelations_CA3 = Class(name="testmaprelations::CA3")
testmaprelations_CA4 = Class(name="testmaprelations::CA4")
testmaprelations_MapCA4ToCB4MapEntry = Class(name="testmaprelations::MapCA4ToCB4MapEntry")
testmaprelations_CB4 = Class(name="testmaprelations::CB4")
testmaprelations_CA5 = Class(name="testmaprelations::CA5")
testmaprelations_MapCA5ToCB5MapEntry = Class(name="testmaprelations::MapCA5ToCB5MapEntry")
testmaprelations_CB3 = Class(name="testmaprelations::CB3")
testmaprelations_MapCA6ToCB6MapEntry = Class(name="testmaprelations::MapCA6ToCB6MapEntry")
testmaprelations_CA6 = Class(name="testmaprelations::CA6")
testmaprelations_CB6 = Class(name="testmaprelations::CB6")
testmaprelations_CA7 = Class(name="testmaprelations::CA7")
testmaprelations_MapCA7ToCB7MapEntry = Class(name="testmaprelations::MapCA7ToCB7MapEntry")
testmaprelations_CB7 = Class(name="testmaprelations::CB7")
testmaprelations_CA8 = Class(name="testmaprelations::CA8")
testmaprelations_MapCA8ToCB8MapEntry = Class(name="testmaprelations::MapCA8ToCB8MapEntry")
testmaprelations_CB8 = Class(name="testmaprelations::CB8")
testmaprelations_MapCA9ToCB9MapEntry = Class(name="testmaprelations::MapCA9ToCB9MapEntry")
testmaprelations_CA9 = Class(name="testmaprelations::CA9")
testmaprelations_CB9 = Class(name="testmaprelations::CB9")
testmaprelations_CB5 = Class(name="testmaprelations::CB5")

# testmaprelations_CB0 class attributes and methods

# testmaprelations_MapCA1ToCB1MapEntry class attributes and methods

# testmaprelations_CA1 class attributes and methods

# testmaprelations_CB1 class attributes and methods

# testmaprelations_CA2 class attributes and methods

# testmaprelations_MapCA2ToCB2MapEntry class attributes and methods

# testmaprelations_CB2 class attributes and methods

# testmaprelations_MapCA0ToCB0MapEntry class attributes and methods

# testmaprelations_CA0 class attributes and methods

# testmaprelations_MapCA3ToCB3MapEntry class attributes and methods

# testmaprelations_CA3 class attributes and methods

# testmaprelations_CA4 class attributes and methods

# testmaprelations_MapCA4ToCB4MapEntry class attributes and methods

# testmaprelations_CB4 class attributes and methods

# testmaprelations_CA5 class attributes and methods

# testmaprelations_MapCA5ToCB5MapEntry class attributes and methods

# testmaprelations_CB3 class attributes and methods

# testmaprelations_MapCA6ToCB6MapEntry class attributes and methods

# testmaprelations_CA6 class attributes and methods

# testmaprelations_CB6 class attributes and methods

# testmaprelations_CA7 class attributes and methods

# testmaprelations_MapCA7ToCB7MapEntry class attributes and methods

# testmaprelations_CB7 class attributes and methods

# testmaprelations_CA8 class attributes and methods

# testmaprelations_MapCA8ToCB8MapEntry class attributes and methods

# testmaprelations_CB8 class attributes and methods

# testmaprelations_MapCA9ToCB9MapEntry class attributes and methods

# testmaprelations_CA9 class attributes and methods

# testmaprelations_CB9 class attributes and methods

# testmaprelations_CB5 class attributes and methods

# Relationships
value1: BinaryAssociation = BinaryAssociation(
    name="value1",
    ends={
        Property(name="CB0", type=testmaprelations_MapCA0ToCB0MapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="mapca0tocb0mapentry2", type=testmaprelations_CB0, multiplicity=Multiplicity(0, 1))
    }
)
mapca0tocb0mapentry3: BinaryAssociation = BinaryAssociation(
    name="mapca0tocb0mapentry3",
    ends={
        Property(name="MapCA0ToCB0MapEntry", type=testmaprelations_CA0, multiplicity=Multiplicity(1, 1)),
        Property(name="key", type=testmaprelations_MapCA0ToCB0MapEntry, multiplicity=Multiplicity(0, 1))
    }
)
mapca0tocb0mapentry4: BinaryAssociation = BinaryAssociation(
    name="mapca0tocb0mapentry4",
    ends={
        Property(name="MapCA0ToCB0MapEntry5", type=testmaprelations_CB0, multiplicity=Multiplicity(1, 1)),
        Property(name="value", type=testmaprelations_MapCA0ToCB0MapEntry, multiplicity=Multiplicity(0, 1))
    }
)
key6: BinaryAssociation = BinaryAssociation(
    name="key6",
    ends={
        Property(name="CA1", type=testmaprelations_MapCA1ToCB1MapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="mapca0tocb0mapentry7", type=testmaprelations_CA1, multiplicity=Multiplicity(0, 9999))
    }
)
value8: BinaryAssociation = BinaryAssociation(
    name="value8",
    ends={
        Property(name="CB1", type=testmaprelations_MapCA1ToCB1MapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="mapca0tocb0mapentry9", type=testmaprelations_CB1, multiplicity=Multiplicity(0, 9999))
    }
)
mapca0tocb0mapentry10: BinaryAssociation = BinaryAssociation(
    name="mapca0tocb0mapentry10",
    ends={
        Property(name="MapCA1ToCB1MapEntry", type=testmaprelations_CB1, multiplicity=Multiplicity(1, 1)),
        Property(name="value11", type=testmaprelations_MapCA1ToCB1MapEntry, multiplicity=Multiplicity(0, 1))
    }
)
mapca0tocb0mapentry12: BinaryAssociation = BinaryAssociation(
    name="mapca0tocb0mapentry12",
    ends={
        Property(name="MapCA1ToCB1MapEntry14", type=testmaprelations_CA1, multiplicity=Multiplicity(1, 1)),
        Property(name="key13", type=testmaprelations_MapCA1ToCB1MapEntry, multiplicity=Multiplicity(0, 1))
    }
)
mapca0tocb0mapentry15: BinaryAssociation = BinaryAssociation(
    name="mapca0tocb0mapentry15",
    ends={
        Property(name="MapCA2ToCB2MapEntry", type=testmaprelations_CA2, multiplicity=Multiplicity(1, 1)),
        Property(name="key16", type=testmaprelations_MapCA2ToCB2MapEntry, multiplicity=Multiplicity(0, 9999))
    }
)
key0: BinaryAssociation = BinaryAssociation(
    name="key0",
    ends={
        Property(name="CA0", type=testmaprelations_MapCA0ToCB0MapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="mapca0tocb0mapentry", type=testmaprelations_CA0, multiplicity=Multiplicity(0, 1))
    }
)
mapca0tocb0mapentry24: BinaryAssociation = BinaryAssociation(
    name="mapca0tocb0mapentry24",
    ends={
        Property(name="MapCA3ToCB3MapEntry", type=testmaprelations_CB3, multiplicity=Multiplicity(1, 1)),
        Property(name="value25", type=testmaprelations_MapCA3ToCB3MapEntry, multiplicity=Multiplicity(0, 9999))
    }
)
mapca0tocb0mapentry26: BinaryAssociation = BinaryAssociation(
    name="mapca0tocb0mapentry26",
    ends={
        Property(name="MapCA3ToCB3MapEntry28", type=testmaprelations_CA3, multiplicity=Multiplicity(1, 1)),
        Property(name="key27", type=testmaprelations_MapCA3ToCB3MapEntry, multiplicity=Multiplicity(0, 9999))
    }
)
key29: BinaryAssociation = BinaryAssociation(
    name="key29",
    ends={
        Property(name="CA3", type=testmaprelations_MapCA3ToCB3MapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="mapca0tocb0mapentry30", type=testmaprelations_CA3, multiplicity=Multiplicity(0, 9999))
    }
)
value31: BinaryAssociation = BinaryAssociation(
    name="value31",
    ends={
        Property(name="CB3", type=testmaprelations_MapCA3ToCB3MapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="mapca0tocb0mapentry32", type=testmaprelations_CB3, multiplicity=Multiplicity(0, 9999))
    }
)
mapca0tocb0mapentry33: BinaryAssociation = BinaryAssociation(
    name="mapca0tocb0mapentry33",
    ends={
        Property(name="MapCA4ToCB4MapEntry", type=testmaprelations_CA4, multiplicity=Multiplicity(1, 1)),
        Property(name="key34", type=testmaprelations_MapCA4ToCB4MapEntry, multiplicity=Multiplicity(0, 1))
    }
)
key35: BinaryAssociation = BinaryAssociation(
    name="key35",
    ends={
        Property(name="CA4", type=testmaprelations_MapCA4ToCB4MapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="mapca0tocb0mapentry36", type=testmaprelations_CA4, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value37: BinaryAssociation = BinaryAssociation(
    name="value37",
    ends={
        Property(name="CB4", type=testmaprelations_MapCA4ToCB4MapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="mapca0tocb0mapentry38", type=testmaprelations_CB4, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mapca0tocb0mapentry39: BinaryAssociation = BinaryAssociation(
    name="mapca0tocb0mapentry39",
    ends={
        Property(name="MapCA4ToCB4MapEntry41", type=testmaprelations_CB4, multiplicity=Multiplicity(1, 1)),
        Property(name="value40", type=testmaprelations_MapCA4ToCB4MapEntry, multiplicity=Multiplicity(0, 1))
    }
)
mapca0tocb0mapentry42: BinaryAssociation = BinaryAssociation(
    name="mapca0tocb0mapentry42",
    ends={
        Property(name="MapCA5ToCB5MapEntry", type=testmaprelations_CA5, multiplicity=Multiplicity(1, 1)),
        Property(name="key43", type=testmaprelations_MapCA5ToCB5MapEntry, multiplicity=Multiplicity(0, 1))
    }
)
mapca0tocb0mapentry17: BinaryAssociation = BinaryAssociation(
    name="mapca0tocb0mapentry17",
    ends={
        Property(name="MapCA2ToCB2MapEntry19", type=testmaprelations_CB2, multiplicity=Multiplicity(1, 1)),
        Property(name="value18", type=testmaprelations_MapCA2ToCB2MapEntry, multiplicity=Multiplicity(0, 9999))
    }
)
key20: BinaryAssociation = BinaryAssociation(
    name="key20",
    ends={
        Property(name="CA2", type=testmaprelations_MapCA2ToCB2MapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="mapca0tocb0mapentry21", type=testmaprelations_CA2, multiplicity=Multiplicity(0, 1))
    }
)
value22: BinaryAssociation = BinaryAssociation(
    name="value22",
    ends={
        Property(name="CB2", type=testmaprelations_MapCA2ToCB2MapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="mapca0tocb0mapentry23", type=testmaprelations_CB2, multiplicity=Multiplicity(0, 1))
    }
)
key51: BinaryAssociation = BinaryAssociation(
    name="key51",
    ends={
        Property(name="testmaprelations_CA6", type=testmaprelations_MapCA6ToCB6MapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="testmaprelations_MapCA6ToCB6MapEntry", type=testmaprelations_CA6, multiplicity=Multiplicity(0, 1))
    }
)
value52: BinaryAssociation = BinaryAssociation(
    name="value52",
    ends={
        Property(name="testmaprelations_CB6", type=testmaprelations_MapCA6ToCB6MapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="testmaprelations_MapCA6ToCB6MapEntry53", type=testmaprelations_CB6, multiplicity=Multiplicity(0, 1))
    }
)
key54: BinaryAssociation = BinaryAssociation(
    name="key54",
    ends={
        Property(name="testmaprelations_CA7", type=testmaprelations_MapCA7ToCB7MapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="testmaprelations_MapCA7ToCB7MapEntry", type=testmaprelations_CA7, multiplicity=Multiplicity(0, 9999))
    }
)
value55: BinaryAssociation = BinaryAssociation(
    name="value55",
    ends={
        Property(name="testmaprelations_CB7", type=testmaprelations_MapCA7ToCB7MapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="testmaprelations_MapCA7ToCB7MapEntry56", type=testmaprelations_CB7, multiplicity=Multiplicity(0, 9999))
    }
)
key57: BinaryAssociation = BinaryAssociation(
    name="key57",
    ends={
        Property(name="testmaprelations_CA8", type=testmaprelations_MapCA8ToCB8MapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="testmaprelations_MapCA8ToCB8MapEntry", type=testmaprelations_CA8, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value58: BinaryAssociation = BinaryAssociation(
    name="value58",
    ends={
        Property(name="testmaprelations_CB8", type=testmaprelations_MapCA8ToCB8MapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="testmaprelations_MapCA8ToCB8MapEntry59", type=testmaprelations_CB8, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
key60: BinaryAssociation = BinaryAssociation(
    name="key60",
    ends={
        Property(name="testmaprelations_CA9", type=testmaprelations_MapCA9ToCB9MapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="testmaprelations_MapCA9ToCB9MapEntry", type=testmaprelations_CA9, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value61: BinaryAssociation = BinaryAssociation(
    name="value61",
    ends={
        Property(name="testmaprelations_CB9", type=testmaprelations_MapCA9ToCB9MapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="testmaprelations_MapCA9ToCB9MapEntry62", type=testmaprelations_CB9, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mapca0tocb0mapentry44: BinaryAssociation = BinaryAssociation(
    name="mapca0tocb0mapentry44",
    ends={
        Property(name="MapCA5ToCB5MapEntry46", type=testmaprelations_CB5, multiplicity=Multiplicity(1, 1)),
        Property(name="value45", type=testmaprelations_MapCA5ToCB5MapEntry, multiplicity=Multiplicity(0, 1))
    }
)
key47: BinaryAssociation = BinaryAssociation(
    name="key47",
    ends={
        Property(name="CA5", type=testmaprelations_MapCA5ToCB5MapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="mapca0tocb0mapentry48", type=testmaprelations_CA5, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value49: BinaryAssociation = BinaryAssociation(
    name="value49",
    ends={
        Property(name="CB5", type=testmaprelations_MapCA5ToCB5MapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="mapca0tocb0mapentry50", type=testmaprelations_CB5, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="testmaprelations",
    types={testmaprelations_CB0, testmaprelations_MapCA1ToCB1MapEntry, testmaprelations_CA1, testmaprelations_CB1, testmaprelations_CA2, testmaprelations_MapCA2ToCB2MapEntry, testmaprelations_CB2, testmaprelations_MapCA0ToCB0MapEntry, testmaprelations_CA0, testmaprelations_MapCA3ToCB3MapEntry, testmaprelations_CA3, testmaprelations_CA4, testmaprelations_MapCA4ToCB4MapEntry, testmaprelations_CB4, testmaprelations_CA5, testmaprelations_MapCA5ToCB5MapEntry, testmaprelations_CB3, testmaprelations_MapCA6ToCB6MapEntry, testmaprelations_CA6, testmaprelations_CB6, testmaprelations_CA7, testmaprelations_MapCA7ToCB7MapEntry, testmaprelations_CB7, testmaprelations_CA8, testmaprelations_MapCA8ToCB8MapEntry, testmaprelations_CB8, testmaprelations_MapCA9ToCB9MapEntry, testmaprelations_CA9, testmaprelations_CB9, testmaprelations_CB5},
    associations={value1, mapca0tocb0mapentry3, mapca0tocb0mapentry4, key6, value8, mapca0tocb0mapentry10, mapca0tocb0mapentry12, mapca0tocb0mapentry15, key0, mapca0tocb0mapentry24, mapca0tocb0mapentry26, key29, value31, mapca0tocb0mapentry33, key35, value37, mapca0tocb0mapentry39, mapca0tocb0mapentry42, mapca0tocb0mapentry17, key20, value22, key51, value52, key54, value55, key57, value58, key60, value61, mapca0tocb0mapentry44, key47, value49},
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