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

# Enumerations
TextType1: Enumeration = Enumeration(
    name="TextType1",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="XOR")
    }
)

TextType2: Enumeration = Enumeration(
    name="TextType2",
    literals={
            EnumerationLiteral(name="channel"),
			EnumerationLiteral(name="store")
    }
)

TextTypeMember0: Enumeration = Enumeration(
    name="TextTypeMember0",
    literals={
            EnumerationLiteral(name="inflow"),
			EnumerationLiteral(name="outflow"),
			EnumerationLiteral(name="biflow"),
			EnumerationLiteral(name="inhibitor"),
			EnumerationLiteral(name="reset")
    }
)

Tool: Enumeration = Enumeration(
    name="Tool",
    literals={
            EnumerationLiteral(name="Yasper")
    }
)

Version: Enumeration = Enumeration(
    name="Version",
    literals={
            EnumerationLiteral(name="_1")
    }
)

# Classes
YasperEPNML114_Arc = Class(name="YasperEPNML114_Arc")
YasperEPNML114_ArcType = Class(name="YasperEPNML114_ArcType")
YasperEPNML114_AnnotationGraphics = Class(name="YasperEPNML114_AnnotationGraphics")
YasperEPNML114_TwoDimVector = Class(name="YasperEPNML114_TwoDimVector")
YasperEPNML114_ToolspecificType = Class(name="YasperEPNML114_ToolspecificType")
YasperEPNML114_EdgeGraphics = Class(name="YasperEPNML114_EdgeGraphics")
YasperEPNML114_Inscription = Class(name="YasperEPNML114_Inscription")
YasperEPNML114_PnmlAnnotation = Class(name="YasperEPNML114_PnmlAnnotation")
YasperEPNML114_Stat = Class(name="YasperEPNML114_Stat")
YasperEPNML114_ConnectionWeights = Class(name="YasperEPNML114_ConnectionWeights")
YasperEPNML114_ConnectionWeight = Class(name="YasperEPNML114_ConnectionWeight")
YasperEPNML114_EStringToStringMapEntry = Class(name="YasperEPNML114_EStringToStringMapEntry")
YasperEPNML114_Pnml = Class(name="YasperEPNML114_Pnml")
YasperEPNML114_Cost = Class(name="YasperEPNML114_Cost")
YasperEPNML114_DocumentRoot = Class(name="YasperEPNML114_DocumentRoot")
YasperEPNML114_InitialMarking = Class(name="YasperEPNML114_InitialMarking")
YasperEPNML114_NetGraphics = Class(name="YasperEPNML114_NetGraphics")
YasperEPNML114_PlaceType1 = Class(name="YasperEPNML114_PlaceType1")
YasperEPNML114_Net = Class(name="YasperEPNML114_Net")
YasperEPNML114_Transition = Class(name="YasperEPNML114_Transition")
YasperEPNML114_Page = Class(name="YasperEPNML114_Page")
YasperEPNML114_NodeGraphics = Class(name="YasperEPNML114_NodeGraphics")
YasperEPNML114_ReferencePlace = Class(name="YasperEPNML114_ReferencePlace")
YasperEPNML114_TransitionType = Class(name="YasperEPNML114_TransitionType")
YasperEPNML114_Place = Class(name="YasperEPNML114_Place")
YasperEPNML114_PlaceType = Class(name="YasperEPNML114_PlaceType")
Place = Class(name="Place")
YasperEPNML114_ProcessingTime = Class(name="YasperEPNML114_ProcessingTime")
YasperEPNML114_ReferencePlaceSpecific = Class(name="YasperEPNML114_ReferencePlaceSpecific")
YasperEPNML114_Role = Class(name="YasperEPNML114_Role")
YasperEPNML114_Roles = Class(name="YasperEPNML114_Roles")
YasperEPNML114_Transformation = Class(name="YasperEPNML114_Transformation")
YasperEPNML114_TransitionSpecific = Class(name="YasperEPNML114_TransitionSpecific")

# YasperEPNML114_Arc class attributes and methods
YasperEPNML114_Arc_group: Property = Property(name="group", type=StringType)
YasperEPNML114_Arc_id: Property = Property(name="id", type=StringType)
YasperEPNML114_Arc_source: Property = Property(name="source", type=StringType)
YasperEPNML114_Arc_target: Property = Property(name="target", type=StringType)
YasperEPNML114_Arc.attributes={YasperEPNML114_Arc_group, YasperEPNML114_Arc_id, YasperEPNML114_Arc_target, YasperEPNML114_Arc_source}

# YasperEPNML114_ArcType class attributes and methods
YasperEPNML114_ArcType_text: Property = Property(name="text", type=StringType)
YasperEPNML114_ArcType.attributes={YasperEPNML114_ArcType_text}

# YasperEPNML114_AnnotationGraphics class attributes and methods

# YasperEPNML114_TwoDimVector class attributes and methods
YasperEPNML114_TwoDimVector_x: Property = Property(name="x", type=StringType)
YasperEPNML114_TwoDimVector_y: Property = Property(name="y", type=StringType)
YasperEPNML114_TwoDimVector.attributes={YasperEPNML114_TwoDimVector_y, YasperEPNML114_TwoDimVector_x}

# YasperEPNML114_ToolspecificType class attributes and methods
YasperEPNML114_ToolspecificType_mixed: Property = Property(name="mixed", type=StringType)
YasperEPNML114_ToolspecificType_group: Property = Property(name="group", type=StringType)
YasperEPNML114_ToolspecificType_any: Property = Property(name="any", type=StringType)
YasperEPNML114_ToolspecificType_tool: Property = Property(name="tool", type=StringType)
YasperEPNML114_ToolspecificType_version: Property = Property(name="version", type=StringType)
YasperEPNML114_ToolspecificType.attributes={YasperEPNML114_ToolspecificType_tool, YasperEPNML114_ToolspecificType_any, YasperEPNML114_ToolspecificType_mixed, YasperEPNML114_ToolspecificType_group, YasperEPNML114_ToolspecificType_version}

# YasperEPNML114_EdgeGraphics class attributes and methods

# YasperEPNML114_Inscription class attributes and methods
YasperEPNML114_Inscription_text: Property = Property(name="text", type=StringType)
YasperEPNML114_Inscription.attributes={YasperEPNML114_Inscription_text}

# YasperEPNML114_PnmlAnnotation class attributes and methods
YasperEPNML114_PnmlAnnotation_text: Property = Property(name="text", type=StringType)
YasperEPNML114_PnmlAnnotation.attributes={YasperEPNML114_PnmlAnnotation_text}

# YasperEPNML114_Stat class attributes and methods
YasperEPNML114_Stat_text: Property = Property(name="text", type=StringType)
YasperEPNML114_Stat.attributes={YasperEPNML114_Stat_text}

# YasperEPNML114_ConnectionWeights class attributes and methods

# YasperEPNML114_ConnectionWeight class attributes and methods
YasperEPNML114_ConnectionWeight_connection: Property = Property(name="connection", type=StringType)
YasperEPNML114_ConnectionWeight.attributes={YasperEPNML114_ConnectionWeight_connection}

# YasperEPNML114_EStringToStringMapEntry class attributes and methods

# YasperEPNML114_Pnml class attributes and methods
YasperEPNML114_Pnml_group: Property = Property(name="group", type=StringType)
YasperEPNML114_Pnml.attributes={YasperEPNML114_Pnml_group}

# YasperEPNML114_Cost class attributes and methods

# YasperEPNML114_DocumentRoot class attributes and methods
YasperEPNML114_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
YasperEPNML114_DocumentRoot.attributes={YasperEPNML114_DocumentRoot_mixed}

# YasperEPNML114_InitialMarking class attributes and methods
YasperEPNML114_InitialMarking_text: Property = Property(name="text", type=StringType)
YasperEPNML114_InitialMarking.attributes={YasperEPNML114_InitialMarking_text}

# YasperEPNML114_NetGraphics class attributes and methods
YasperEPNML114_NetGraphics_group: Property = Property(name="group", type=StringType)
YasperEPNML114_NetGraphics.attributes={YasperEPNML114_NetGraphics_group}

# YasperEPNML114_PlaceType1 class attributes and methods

# YasperEPNML114_Net class attributes and methods
YasperEPNML114_Net_group: Property = Property(name="group", type=StringType)
YasperEPNML114_Net_id: Property = Property(name="id", type=StringType)
YasperEPNML114_Net_type: Property = Property(name="type", type=StringType)
YasperEPNML114_Net.attributes={YasperEPNML114_Net_id, YasperEPNML114_Net_group, YasperEPNML114_Net_type}

# YasperEPNML114_Transition class attributes and methods
YasperEPNML114_Transition_group: Property = Property(name="group", type=StringType)
YasperEPNML114_Transition_id: Property = Property(name="id", type=StringType)
YasperEPNML114_Transition.attributes={YasperEPNML114_Transition_group, YasperEPNML114_Transition_id}

# YasperEPNML114_Page class attributes and methods
YasperEPNML114_Page_group: Property = Property(name="group", type=StringType)
YasperEPNML114_Page_id: Property = Property(name="id", type=StringType)
YasperEPNML114_Page.attributes={YasperEPNML114_Page_group, YasperEPNML114_Page_id}

# YasperEPNML114_NodeGraphics class attributes and methods
YasperEPNML114_NodeGraphics_group: Property = Property(name="group", type=StringType)
YasperEPNML114_NodeGraphics.attributes={YasperEPNML114_NodeGraphics_group}

# YasperEPNML114_ReferencePlace class attributes and methods
YasperEPNML114_ReferencePlace_group: Property = Property(name="group", type=StringType)
YasperEPNML114_ReferencePlace_id: Property = Property(name="id", type=StringType)
YasperEPNML114_ReferencePlace_ref: Property = Property(name="ref", type=StringType)
YasperEPNML114_ReferencePlace.attributes={YasperEPNML114_ReferencePlace_group, YasperEPNML114_ReferencePlace_ref, YasperEPNML114_ReferencePlace_id}

# YasperEPNML114_TransitionType class attributes and methods
YasperEPNML114_TransitionType_text: Property = Property(name="text", type=StringType)
YasperEPNML114_TransitionType.attributes={YasperEPNML114_TransitionType_text}

# YasperEPNML114_Place class attributes and methods
YasperEPNML114_Place_group: Property = Property(name="group", type=StringType)
YasperEPNML114_Place_id: Property = Property(name="id", type=StringType)
YasperEPNML114_Place.attributes={YasperEPNML114_Place_group, YasperEPNML114_Place_id}

# YasperEPNML114_PlaceType class attributes and methods
YasperEPNML114_PlaceType_text: Property = Property(name="text", type=StringType)
YasperEPNML114_PlaceType.attributes={YasperEPNML114_PlaceType_text}

# Place class attributes and methods

# YasperEPNML114_ProcessingTime class attributes and methods

# YasperEPNML114_ReferencePlaceSpecific class attributes and methods
YasperEPNML114_ReferencePlaceSpecific_tool: Property = Property(name="tool", type=StringType)
YasperEPNML114_ReferencePlaceSpecific_version: Property = Property(name="version", type=StringType)
YasperEPNML114_ReferencePlaceSpecific.attributes={YasperEPNML114_ReferencePlaceSpecific_version, YasperEPNML114_ReferencePlaceSpecific_tool}

# YasperEPNML114_Role class attributes and methods
YasperEPNML114_Role_text: Property = Property(name="text", type=StringType)
YasperEPNML114_Role.attributes={YasperEPNML114_Role_text}

# YasperEPNML114_Roles class attributes and methods

# YasperEPNML114_Transformation class attributes and methods
YasperEPNML114_Transformation_text: Property = Property(name="text", type=StringType)
YasperEPNML114_Transformation.attributes={YasperEPNML114_Transformation_text}

# YasperEPNML114_TransitionSpecific class attributes and methods
YasperEPNML114_TransitionSpecific_tokenCaseSensitive: Property = Property(name="tokenCaseSensitive", type=StringType)
YasperEPNML114_TransitionSpecific_tool: Property = Property(name="tool", type=StringType)
YasperEPNML114_TransitionSpecific_version: Property = Property(name="version", type=StringType)
YasperEPNML114_TransitionSpecific.attributes={YasperEPNML114_TransitionSpecific_tool, YasperEPNML114_TransitionSpecific_version, YasperEPNML114_TransitionSpecific_tokenCaseSensitive}

# Relationships
type1: BinaryAssociation = BinaryAssociation(
    name="type1",
    ends={
        Property(name="YasperEPNML114_ArcType", type=YasperEPNML114_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Arc", type=YasperEPNML114_ArcType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
offset0: BinaryAssociation = BinaryAssociation(
    name="offset0",
    ends={
        Property(name="YasperEPNML114_TwoDimVector", type=YasperEPNML114_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_AnnotationGraphics", type=YasperEPNML114_TwoDimVector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
description8: BinaryAssociation = BinaryAssociation(
    name="description8",
    ends={
        Property(name="YasperEPNML114_PnmlAnnotation10", type=YasperEPNML114_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Arc9", type=YasperEPNML114_PnmlAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
toolspecific11: BinaryAssociation = BinaryAssociation(
    name="toolspecific11",
    ends={
        Property(name="YasperEPNML114_ToolspecificType", type=YasperEPNML114_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Arc12", type=YasperEPNML114_ToolspecificType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
graphics2: BinaryAssociation = BinaryAssociation(
    name="graphics2",
    ends={
        Property(name="YasperEPNML114_EdgeGraphics", type=YasperEPNML114_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Arc3", type=YasperEPNML114_EdgeGraphics, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inscription4: BinaryAssociation = BinaryAssociation(
    name="inscription4",
    ends={
        Property(name="YasperEPNML114_Inscription", type=YasperEPNML114_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Arc5", type=YasperEPNML114_Inscription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name6: BinaryAssociation = BinaryAssociation(
    name="name6",
    ends={
        Property(name="YasperEPNML114_PnmlAnnotation", type=YasperEPNML114_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Arc7", type=YasperEPNML114_PnmlAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
weight13: BinaryAssociation = BinaryAssociation(
    name="weight13",
    ends={
        Property(name="YasperEPNML114_Stat", type=YasperEPNML114_ConnectionWeight, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_ConnectionWeight", type=YasperEPNML114_Stat, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
xMLNSPrefixMap21: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap21",
    ends={
        Property(name="YasperEPNML114_EStringToStringMapEntry", type=YasperEPNML114_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_DocumentRoot", type=YasperEPNML114_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation22: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation22",
    ends={
        Property(name="YasperEPNML114_EStringToStringMapEntry24", type=YasperEPNML114_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_DocumentRoot23", type=YasperEPNML114_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pnml25: BinaryAssociation = BinaryAssociation(
    name="pnml25",
    ends={
        Property(name="YasperEPNML114_Pnml", type=YasperEPNML114_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_DocumentRoot26", type=YasperEPNML114_Pnml, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectionWeight14: BinaryAssociation = BinaryAssociation(
    name="connectionWeight14",
    ends={
        Property(name="YasperEPNML114_ConnectionWeight15", type=YasperEPNML114_ConnectionWeights, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_ConnectionWeights", type=YasperEPNML114_ConnectionWeight, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fixed16: BinaryAssociation = BinaryAssociation(
    name="fixed16",
    ends={
        Property(name="YasperEPNML114_Stat17", type=YasperEPNML114_Cost, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Cost", type=YasperEPNML114_Stat, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable18: BinaryAssociation = BinaryAssociation(
    name="variable18",
    ends={
        Property(name="YasperEPNML114_Stat20", type=YasperEPNML114_Cost, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Cost19", type=YasperEPNML114_Stat, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
position27: BinaryAssociation = BinaryAssociation(
    name="position27",
    ends={
        Property(name="YasperEPNML114_TwoDimVector29", type=YasperEPNML114_EdgeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_EdgeGraphics28", type=YasperEPNML114_TwoDimVector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
graphics32: BinaryAssociation = BinaryAssociation(
    name="graphics32",
    ends={
        Property(name="YasperEPNML114_AnnotationGraphics34", type=YasperEPNML114_Inscription, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Inscription33", type=YasperEPNML114_AnnotationGraphics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
graphics30: BinaryAssociation = BinaryAssociation(
    name="graphics30",
    ends={
        Property(name="YasperEPNML114_AnnotationGraphics31", type=YasperEPNML114_InitialMarking, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_InitialMarking", type=YasperEPNML114_AnnotationGraphics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
graphics35: BinaryAssociation = BinaryAssociation(
    name="graphics35",
    ends={
        Property(name="YasperEPNML114_NetGraphics", type=YasperEPNML114_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Net", type=YasperEPNML114_NetGraphics, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
place36: BinaryAssociation = BinaryAssociation(
    name="place36",
    ends={
        Property(name="YasperEPNML114_PlaceType1", type=YasperEPNML114_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Net37", type=YasperEPNML114_PlaceType1, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition38: BinaryAssociation = BinaryAssociation(
    name="transition38",
    ends={
        Property(name="YasperEPNML114_Net39", type=YasperEPNML114_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="YasperEPNML114_Transition", type=YasperEPNML114_Net, multiplicity=Multiplicity(1, 1))
    }
)
arc40: BinaryAssociation = BinaryAssociation(
    name="arc40",
    ends={
        Property(name="YasperEPNML114_Arc42", type=YasperEPNML114_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Net41", type=YasperEPNML114_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name45: BinaryAssociation = BinaryAssociation(
    name="name45",
    ends={
        Property(name="YasperEPNML114_PnmlAnnotation47", type=YasperEPNML114_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Net46", type=YasperEPNML114_PnmlAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
description48: BinaryAssociation = BinaryAssociation(
    name="description48",
    ends={
        Property(name="YasperEPNML114_PnmlAnnotation50", type=YasperEPNML114_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Net49", type=YasperEPNML114_PnmlAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
page43: BinaryAssociation = BinaryAssociation(
    name="page43",
    ends={
        Property(name="YasperEPNML114_Page", type=YasperEPNML114_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Net44", type=YasperEPNML114_Page, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
toolspecific51: BinaryAssociation = BinaryAssociation(
    name="toolspecific51",
    ends={
        Property(name="YasperEPNML114_ToolspecificType53", type=YasperEPNML114_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Net52", type=YasperEPNML114_ToolspecificType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
position54: BinaryAssociation = BinaryAssociation(
    name="position54",
    ends={
        Property(name="YasperEPNML114_TwoDimVector56", type=YasperEPNML114_NetGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_NetGraphics55", type=YasperEPNML114_TwoDimVector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dimension57: BinaryAssociation = BinaryAssociation(
    name="dimension57",
    ends={
        Property(name="YasperEPNML114_TwoDimVector59", type=YasperEPNML114_NetGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_NetGraphics58", type=YasperEPNML114_TwoDimVector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
position60: BinaryAssociation = BinaryAssociation(
    name="position60",
    ends={
        Property(name="YasperEPNML114_TwoDimVector61", type=YasperEPNML114_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_NodeGraphics", type=YasperEPNML114_TwoDimVector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dimension62: BinaryAssociation = BinaryAssociation(
    name="dimension62",
    ends={
        Property(name="YasperEPNML114_TwoDimVector64", type=YasperEPNML114_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_NodeGraphics63", type=YasperEPNML114_TwoDimVector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referencePlace65: BinaryAssociation = BinaryAssociation(
    name="referencePlace65",
    ends={
        Property(name="YasperEPNML114_ReferencePlace", type=YasperEPNML114_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Page66", type=YasperEPNML114_ReferencePlace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type70: BinaryAssociation = BinaryAssociation(
    name="type70",
    ends={
        Property(name="YasperEPNML114_TransitionType", type=YasperEPNML114_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Page71", type=YasperEPNML114_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
place72: BinaryAssociation = BinaryAssociation(
    name="place72",
    ends={
        Property(name="YasperEPNML114_PlaceType174", type=YasperEPNML114_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Page73", type=YasperEPNML114_PlaceType1, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
graphics67: BinaryAssociation = BinaryAssociation(
    name="graphics67",
    ends={
        Property(name="YasperEPNML114_NetGraphics69", type=YasperEPNML114_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Page68", type=YasperEPNML114_NetGraphics, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arc78: BinaryAssociation = BinaryAssociation(
    name="arc78",
    ends={
        Property(name="YasperEPNML114_Arc80", type=YasperEPNML114_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Page79", type=YasperEPNML114_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
page82: BinaryAssociation = BinaryAssociation(
    name="page82",
    ends={
        Property(name="YasperEPNML114_Page83", type=YasperEPNML114_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Page81", type=YasperEPNML114_Page, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition75: BinaryAssociation = BinaryAssociation(
    name="transition75",
    ends={
        Property(name="YasperEPNML114_Transition77", type=YasperEPNML114_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Page76", type=YasperEPNML114_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name84: BinaryAssociation = BinaryAssociation(
    name="name84",
    ends={
        Property(name="YasperEPNML114_Page85", type=YasperEPNML114_PnmlAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="YasperEPNML114_PnmlAnnotation86", type=YasperEPNML114_Page, multiplicity=Multiplicity(1, 1))
    }
)
description87: BinaryAssociation = BinaryAssociation(
    name="description87",
    ends={
        Property(name="YasperEPNML114_PnmlAnnotation89", type=YasperEPNML114_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Page88", type=YasperEPNML114_PnmlAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
toolspecific90: BinaryAssociation = BinaryAssociation(
    name="toolspecific90",
    ends={
        Property(name="YasperEPNML114_ToolspecificType92", type=YasperEPNML114_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Page91", type=YasperEPNML114_ToolspecificType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
graphics94: BinaryAssociation = BinaryAssociation(
    name="graphics94",
    ends={
        Property(name="YasperEPNML114_NodeGraphics96", type=YasperEPNML114_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Place95", type=YasperEPNML114_NodeGraphics, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type93: BinaryAssociation = BinaryAssociation(
    name="type93",
    ends={
        Property(name="YasperEPNML114_PlaceType", type=YasperEPNML114_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Place", type=YasperEPNML114_PlaceType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name100: BinaryAssociation = BinaryAssociation(
    name="name100",
    ends={
        Property(name="YasperEPNML114_PnmlAnnotation102", type=YasperEPNML114_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Place101", type=YasperEPNML114_PnmlAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
description103: BinaryAssociation = BinaryAssociation(
    name="description103",
    ends={
        Property(name="YasperEPNML114_PnmlAnnotation105", type=YasperEPNML114_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Place104", type=YasperEPNML114_PnmlAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialMarking97: BinaryAssociation = BinaryAssociation(
    name="initialMarking97",
    ends={
        Property(name="YasperEPNML114_InitialMarking99", type=YasperEPNML114_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Place98", type=YasperEPNML114_InitialMarking, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
toolspecific106: BinaryAssociation = BinaryAssociation(
    name="toolspecific106",
    ends={
        Property(name="YasperEPNML114_ToolspecificType108", type=YasperEPNML114_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Place107", type=YasperEPNML114_ToolspecificType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
net109: BinaryAssociation = BinaryAssociation(
    name="net109",
    ends={
        Property(name="YasperEPNML114_Net111", type=YasperEPNML114_Pnml, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Pnml110", type=YasperEPNML114_Net, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
toolspecific112: BinaryAssociation = BinaryAssociation(
    name="toolspecific112",
    ends={
        Property(name="YasperEPNML114_ToolspecificType114", type=YasperEPNML114_Pnml, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Pnml113", type=YasperEPNML114_ToolspecificType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
graphics115: BinaryAssociation = BinaryAssociation(
    name="graphics115",
    ends={
        Property(name="YasperEPNML114_AnnotationGraphics117", type=YasperEPNML114_PnmlAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_PnmlAnnotation116", type=YasperEPNML114_AnnotationGraphics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mean118: BinaryAssociation = BinaryAssociation(
    name="mean118",
    ends={
        Property(name="YasperEPNML114_Stat119", type=YasperEPNML114_ProcessingTime, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_ProcessingTime", type=YasperEPNML114_Stat, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
description129: BinaryAssociation = BinaryAssociation(
    name="description129",
    ends={
        Property(name="YasperEPNML114_ReferencePlace130", type=YasperEPNML114_PnmlAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="YasperEPNML114_PnmlAnnotation131", type=YasperEPNML114_ReferencePlace, multiplicity=Multiplicity(1, 1))
    }
)
deviation120: BinaryAssociation = BinaryAssociation(
    name="deviation120",
    ends={
        Property(name="YasperEPNML114_Stat122", type=YasperEPNML114_ProcessingTime, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_ProcessingTime121", type=YasperEPNML114_Stat, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
graphics123: BinaryAssociation = BinaryAssociation(
    name="graphics123",
    ends={
        Property(name="YasperEPNML114_NodeGraphics125", type=YasperEPNML114_ReferencePlace, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_ReferencePlace124", type=YasperEPNML114_NodeGraphics, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name126: BinaryAssociation = BinaryAssociation(
    name="name126",
    ends={
        Property(name="YasperEPNML114_PnmlAnnotation128", type=YasperEPNML114_ReferencePlace, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_ReferencePlace127", type=YasperEPNML114_PnmlAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
toolspecific132: BinaryAssociation = BinaryAssociation(
    name="toolspecific132",
    ends={
        Property(name="YasperEPNML114_ToolspecificType134", type=YasperEPNML114_ReferencePlace, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_ReferencePlace133", type=YasperEPNML114_ToolspecificType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pathGraphics135: BinaryAssociation = BinaryAssociation(
    name="pathGraphics135",
    ends={
        Property(name="YasperEPNML114_NodeGraphics136", type=YasperEPNML114_ReferencePlaceSpecific, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_ReferencePlaceSpecific", type=YasperEPNML114_NodeGraphics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
role137: BinaryAssociation = BinaryAssociation(
    name="role137",
    ends={
        Property(name="YasperEPNML114_Role", type=YasperEPNML114_Roles, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Roles", type=YasperEPNML114_Role, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
graphics138: BinaryAssociation = BinaryAssociation(
    name="graphics138",
    ends={
        Property(name="YasperEPNML114_AnnotationGraphics139", type=YasperEPNML114_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Transformation", type=YasperEPNML114_AnnotationGraphics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type140: BinaryAssociation = BinaryAssociation(
    name="type140",
    ends={
        Property(name="YasperEPNML114_TransitionType142", type=YasperEPNML114_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Transition141", type=YasperEPNML114_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
graphics143: BinaryAssociation = BinaryAssociation(
    name="graphics143",
    ends={
        Property(name="YasperEPNML114_NodeGraphics145", type=YasperEPNML114_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Transition144", type=YasperEPNML114_NodeGraphics, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transformation146: BinaryAssociation = BinaryAssociation(
    name="transformation146",
    ends={
        Property(name="YasperEPNML114_Transformation148", type=YasperEPNML114_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Transition147", type=YasperEPNML114_Transformation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name149: BinaryAssociation = BinaryAssociation(
    name="name149",
    ends={
        Property(name="YasperEPNML114_PnmlAnnotation151", type=YasperEPNML114_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Transition150", type=YasperEPNML114_PnmlAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
description152: BinaryAssociation = BinaryAssociation(
    name="description152",
    ends={
        Property(name="YasperEPNML114_PnmlAnnotation154", type=YasperEPNML114_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Transition153", type=YasperEPNML114_PnmlAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
toolspecific155: BinaryAssociation = BinaryAssociation(
    name="toolspecific155",
    ends={
        Property(name="YasperEPNML114_ToolspecificType157", type=YasperEPNML114_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_Transition156", type=YasperEPNML114_ToolspecificType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
roles158: BinaryAssociation = BinaryAssociation(
    name="roles158",
    ends={
        Property(name="YasperEPNML114_Roles159", type=YasperEPNML114_TransitionSpecific, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_TransitionSpecific", type=YasperEPNML114_Roles, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cost160: BinaryAssociation = BinaryAssociation(
    name="cost160",
    ends={
        Property(name="YasperEPNML114_Cost162", type=YasperEPNML114_TransitionSpecific, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_TransitionSpecific161", type=YasperEPNML114_Cost, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
processingTime163: BinaryAssociation = BinaryAssociation(
    name="processingTime163",
    ends={
        Property(name="YasperEPNML114_ProcessingTime165", type=YasperEPNML114_TransitionSpecific, multiplicity=Multiplicity(1, 1)),
        Property(name="YasperEPNML114_TransitionSpecific164", type=YasperEPNML114_ProcessingTime, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_YasperEPNML114_PlaceType1_Place = Generalization(general=Place, specific=YasperEPNML114_PlaceType1)

# Domain Model
domain_model = DomainModel(
    name="YasperEPNML114",
    types={YasperEPNML114_Arc, YasperEPNML114_ArcType, YasperEPNML114_AnnotationGraphics, YasperEPNML114_TwoDimVector, YasperEPNML114_ToolspecificType, YasperEPNML114_EdgeGraphics, YasperEPNML114_Inscription, YasperEPNML114_PnmlAnnotation, YasperEPNML114_Stat, YasperEPNML114_ConnectionWeights, YasperEPNML114_ConnectionWeight, YasperEPNML114_EStringToStringMapEntry, YasperEPNML114_Pnml, YasperEPNML114_Cost, YasperEPNML114_DocumentRoot, YasperEPNML114_InitialMarking, YasperEPNML114_NetGraphics, YasperEPNML114_PlaceType1, YasperEPNML114_Net, YasperEPNML114_Transition, YasperEPNML114_Page, YasperEPNML114_NodeGraphics, YasperEPNML114_ReferencePlace, YasperEPNML114_TransitionType, YasperEPNML114_Place, YasperEPNML114_PlaceType, Place, YasperEPNML114_ProcessingTime, YasperEPNML114_ReferencePlaceSpecific, YasperEPNML114_Role, YasperEPNML114_Roles, YasperEPNML114_Transformation, YasperEPNML114_TransitionSpecific, TextType1, TextType2, TextTypeMember0, Tool, Version},
    associations={type1, offset0, description8, toolspecific11, graphics2, inscription4, name6, weight13, xMLNSPrefixMap21, xSISchemaLocation22, pnml25, connectionWeight14, fixed16, variable18, position27, graphics32, graphics30, graphics35, place36, transition38, arc40, name45, description48, page43, toolspecific51, position54, dimension57, position60, dimension62, referencePlace65, type70, place72, graphics67, arc78, page82, transition75, name84, description87, toolspecific90, graphics94, type93, name100, description103, initialMarking97, toolspecific106, net109, toolspecific112, graphics115, mean118, description129, deviation120, graphics123, name126, toolspecific132, pathGraphics135, role137, graphics138, type140, graphics143, transformation146, name149, description152, toolspecific155, roles158, cost160, processingTime163},
    generalizations={gen_YasperEPNML114_PlaceType1_Place},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)