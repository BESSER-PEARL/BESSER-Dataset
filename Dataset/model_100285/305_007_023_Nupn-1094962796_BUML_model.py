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
nupn_StructureType = Class(name="nupn_StructureType")
nupn_SizeType = Class(name="nupn_SizeType")
nupn_UnitType = Class(name="nupn_UnitType")
nupn_NUPNToolspecificType = Class(name="nupn_NUPNToolspecificType")
nupn_EStringToStringMapEntry = Class(name="nupn_EStringToStringMapEntry")

# nupn_StructureType class attributes and methods
nupn_StructureType_safe: Property = Property(name="safe", type=StringType)
nupn_StructureType_units: Property = Property(name="units", type=StringType)
nupn_StructureType_root: Property = Property(name="root", type=StringType)
nupn_StructureType.attributes={nupn_StructureType_units, nupn_StructureType_safe, nupn_StructureType_root}

# nupn_SizeType class attributes and methods
nupn_SizeType_transitions: Property = Property(name="transitions", type=StringType)
nupn_SizeType_arcs: Property = Property(name="arcs", type=StringType)
nupn_SizeType_places: Property = Property(name="places", type=StringType)
nupn_SizeType.attributes={nupn_SizeType_arcs, nupn_SizeType_transitions, nupn_SizeType_places}

# nupn_UnitType class attributes and methods
nupn_UnitType_id: Property = Property(name="id", type=StringType)
nupn_UnitType_places: Property = Property(name="places", type=StringType)
nupn_UnitType_subunits: Property = Property(name="subunits", type=StringType)
nupn_UnitType.attributes={nupn_UnitType_subunits, nupn_UnitType_id, nupn_UnitType_places}

# nupn_NUPNToolspecificType class attributes and methods
nupn_NUPNToolspecificType_tool: Property = Property(name="tool", type=StringType)
nupn_NUPNToolspecificType_version: Property = Property(name="version", type=StringType)
nupn_NUPNToolspecificType_mixed: Property = Property(name="mixed", type=StringType)
nupn_NUPNToolspecificType.attributes={nupn_NUPNToolspecificType_tool, nupn_NUPNToolspecificType_version, nupn_NUPNToolspecificType_mixed}

# nupn_EStringToStringMapEntry class attributes and methods

# Relationships
unit0: BinaryAssociation = BinaryAssociation(
    name="unit0",
    ends={
        Property(name="nupn_UnitType", type=nupn_StructureType, multiplicity=Multiplicity(1, 1)),
        Property(name="nupn_StructureType", type=nupn_UnitType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
size1: BinaryAssociation = BinaryAssociation(
    name="size1",
    ends={
        Property(name="nupn_SizeType", type=nupn_NUPNToolspecificType, multiplicity=Multiplicity(1, 1)),
        Property(name="nupn_NUPNToolspecificType", type=nupn_SizeType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
structure2: BinaryAssociation = BinaryAssociation(
    name="structure2",
    ends={
        Property(name="nupn_StructureType4", type=nupn_NUPNToolspecificType, multiplicity=Multiplicity(1, 1)),
        Property(name="nupn_NUPNToolspecificType3", type=nupn_StructureType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
xMLNSPrefixMap5: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap5",
    ends={
        Property(name="nupn_EStringToStringMapEntry", type=nupn_NUPNToolspecificType, multiplicity=Multiplicity(1, 1)),
        Property(name="nupn_NUPNToolspecificType6", type=nupn_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation7: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation7",
    ends={
        Property(name="nupn_EStringToStringMapEntry9", type=nupn_NUPNToolspecificType, multiplicity=Multiplicity(1, 1)),
        Property(name="nupn_NUPNToolspecificType8", type=nupn_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="nupn",
    types={nupn_StructureType, nupn_SizeType, nupn_UnitType, nupn_NUPNToolspecificType, nupn_EStringToStringMapEntry},
    associations={unit0, size1, structure2, xMLNSPrefixMap5, xSISchemaLocation7},
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