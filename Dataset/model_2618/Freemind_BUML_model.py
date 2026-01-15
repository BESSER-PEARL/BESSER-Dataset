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
BOLDType: Enumeration = Enumeration(
    name="BOLDType",
    literals={
            EnumerationLiteral(name="true")
    }
)

FOLDEDType: Enumeration = Enumeration(
    name="FOLDEDType",
    literals={
            EnumerationLiteral(name="true"),
			EnumerationLiteral(name="false")
    }
)

ITALICType: Enumeration = Enumeration(
    name="ITALICType",
    literals={
            EnumerationLiteral(name="true"),
			EnumerationLiteral(name="false")
    }
)

POSITIONType: Enumeration = Enumeration(
    name="POSITIONType",
    literals={
            EnumerationLiteral(name="left"),
			EnumerationLiteral(name="right")
    }
)

# Classes
Freemind_ArrowlinkType = Class(name="Freemind::ArrowlinkType")
Freemind_EStringToStringMapEntry = Class(name="Freemind::EStringToStringMapEntry")
Freemind_CloudType = Class(name="Freemind::CloudType")
Freemind_DocumentRoot = Class(name="Freemind::DocumentRoot")
Freemind_IconType = Class(name="Freemind::IconType")
Freemind_MapType = Class(name="Freemind::MapType")
Freemind_EdgeType = Class(name="Freemind::EdgeType")
Freemind_FontType = Class(name="Freemind::FontType")
Freemind_HookType = Class(name="Freemind::HookType")
Freemind_NodeType = Class(name="Freemind::NodeType")
Freemind_ParametersType = Class(name="Freemind::ParametersType")
Freemind_TextType = Class(name="Freemind::TextType")

# Freemind_ArrowlinkType class attributes and methods
Freemind_ArrowlinkType_EndInclination: Property = Property(name="EndInclination", type=StringType)
Freemind_ArrowlinkType_Id: Property = Property(name="Id", type=StringType)
Freemind_ArrowlinkType_StartArrow: Property = Property(name="StartArrow", type=StringType)
Freemind_ArrowlinkType_Color: Property = Property(name="Color", type=StringType)
Freemind_ArrowlinkType_Destination: Property = Property(name="Destination", type=StringType)
Freemind_ArrowlinkType_EndArrow: Property = Property(name="EndArrow", type=StringType)
Freemind_ArrowlinkType_StartInclination: Property = Property(name="StartInclination", type=StringType)
Freemind_ArrowlinkType.attributes={Freemind_ArrowlinkType_StartInclination, Freemind_ArrowlinkType_EndInclination, Freemind_ArrowlinkType_EndArrow, Freemind_ArrowlinkType_Destination, Freemind_ArrowlinkType_StartArrow, Freemind_ArrowlinkType_Id, Freemind_ArrowlinkType_Color}

# Freemind_EStringToStringMapEntry class attributes and methods

# Freemind_CloudType class attributes and methods
Freemind_CloudType_Color: Property = Property(name="Color", type=StringType)
Freemind_CloudType.attributes={Freemind_CloudType_Color}

# Freemind_DocumentRoot class attributes and methods
Freemind_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
Freemind_DocumentRoot.attributes={Freemind_DocumentRoot_mixed}

# Freemind_IconType class attributes and methods
Freemind_IconType_Builtin: Property = Property(name="Builtin", type=StringType)
Freemind_IconType.attributes={Freemind_IconType_Builtin}

# Freemind_MapType class attributes and methods
Freemind_MapType_version: Property = Property(name="version", type=StringType)
Freemind_MapType.attributes={Freemind_MapType_version}

# Freemind_EdgeType class attributes and methods
Freemind_EdgeType_Color: Property = Property(name="Color", type=StringType)
Freemind_EdgeType_Style: Property = Property(name="Style", type=StringType)
Freemind_EdgeType_Width: Property = Property(name="Width", type=StringType)
Freemind_EdgeType.attributes={Freemind_EdgeType_Color, Freemind_EdgeType_Style, Freemind_EdgeType_Width}

# Freemind_FontType class attributes and methods
Freemind_FontType_Name: Property = Property(name="Name", type=StringType)
Freemind_FontType_Size: Property = Property(name="Size", type=StringType)
Freemind_FontType_Bold: Property = Property(name="Bold", type=StringType)
Freemind_FontType_Italic: Property = Property(name="Italic", type=StringType)
Freemind_FontType.attributes={Freemind_FontType_Italic, Freemind_FontType_Size, Freemind_FontType_Bold, Freemind_FontType_Name}

# Freemind_HookType class attributes and methods
Freemind_HookType_Name: Property = Property(name="Name", type=StringType)
Freemind_HookType.attributes={Freemind_HookType_Name}

# Freemind_NodeType class attributes and methods
Freemind_NodeType_group: Property = Property(name="group", type=StringType)
Freemind_NodeType_BackgroundColor: Property = Property(name="BackgroundColor", type=StringType)
Freemind_NodeType_Color: Property = Property(name="Color", type=StringType)
Freemind_NodeType_Created: Property = Property(name="Created", type=StringType)
Freemind_NodeType_Id: Property = Property(name="Id", type=StringType)
Freemind_NodeType_Link: Property = Property(name="Link", type=StringType)
Freemind_NodeType_Modified: Property = Property(name="Modified", type=StringType)
Freemind_NodeType_Position: Property = Property(name="Position", type=StringType)
Freemind_NodeType_EncryptedContent: Property = Property(name="EncryptedContent", type=StringType)
Freemind_NodeType_Folded: Property = Property(name="Folded", type=StringType)
Freemind_NodeType_Hgap: Property = Property(name="Hgap", type=StringType)
Freemind_NodeType_Vshift: Property = Property(name="Vshift", type=StringType)
Freemind_NodeType_Style: Property = Property(name="Style", type=StringType)
Freemind_NodeType_Text: Property = Property(name="Text", type=StringType)
Freemind_NodeType_Vgap: Property = Property(name="Vgap", type=StringType)
Freemind_NodeType.attributes={Freemind_NodeType_Style, Freemind_NodeType_Color, Freemind_NodeType_group, Freemind_NodeType_EncryptedContent, Freemind_NodeType_Created, Freemind_NodeType_BackgroundColor, Freemind_NodeType_Link, Freemind_NodeType_Modified, Freemind_NodeType_Vgap, Freemind_NodeType_Vshift, Freemind_NodeType_Hgap, Freemind_NodeType_Position, Freemind_NodeType_Text, Freemind_NodeType_Folded, Freemind_NodeType_Id}

# Freemind_ParametersType class attributes and methods
Freemind_ParametersType_RemindUserAt: Property = Property(name="RemindUserAt", type=StringType)
Freemind_ParametersType.attributes={Freemind_ParametersType_RemindUserAt}

# Freemind_TextType class attributes and methods

# Relationships
xMLNSPrefixMap0: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap0",
    ends={
        Property(name="Freemind_EStringToStringMapEntry", type=Freemind_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Freemind_DocumentRoot", type=Freemind_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cloud6: BinaryAssociation = BinaryAssociation(
    name="cloud6",
    ends={
        Property(name="Freemind_CloudType", type=Freemind_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Freemind_DocumentRoot7", type=Freemind_CloudType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation1: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation1",
    ends={
        Property(name="Freemind_EStringToStringMapEntry3", type=Freemind_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Freemind_DocumentRoot2", type=Freemind_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arrowlink4: BinaryAssociation = BinaryAssociation(
    name="arrowlink4",
    ends={
        Property(name="Freemind_ArrowlinkType", type=Freemind_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Freemind_DocumentRoot5", type=Freemind_ArrowlinkType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
icon14: BinaryAssociation = BinaryAssociation(
    name="icon14",
    ends={
        Property(name="Freemind_IconType", type=Freemind_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Freemind_DocumentRoot15", type=Freemind_IconType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
map16: BinaryAssociation = BinaryAssociation(
    name="map16",
    ends={
        Property(name="Freemind_MapType", type=Freemind_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Freemind_DocumentRoot17", type=Freemind_MapType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge8: BinaryAssociation = BinaryAssociation(
    name="edge8",
    ends={
        Property(name="Freemind_EdgeType", type=Freemind_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Freemind_DocumentRoot9", type=Freemind_EdgeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
font10: BinaryAssociation = BinaryAssociation(
    name="font10",
    ends={
        Property(name="Freemind_FontType", type=Freemind_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Freemind_DocumentRoot11", type=Freemind_FontType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hook12: BinaryAssociation = BinaryAssociation(
    name="hook12",
    ends={
        Property(name="Freemind_HookType", type=Freemind_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Freemind_DocumentRoot13", type=Freemind_HookType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node18: BinaryAssociation = BinaryAssociation(
    name="node18",
    ends={
        Property(name="Freemind_NodeType", type=Freemind_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Freemind_DocumentRoot19", type=Freemind_NodeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters20: BinaryAssociation = BinaryAssociation(
    name="parameters20",
    ends={
        Property(name="Freemind_ParametersType", type=Freemind_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Freemind_DocumentRoot21", type=Freemind_ParametersType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
text22: BinaryAssociation = BinaryAssociation(
    name="text22",
    ends={
        Property(name="Freemind_TextType", type=Freemind_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Freemind_DocumentRoot23", type=Freemind_TextType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters24: BinaryAssociation = BinaryAssociation(
    name="parameters24",
    ends={
        Property(name="Freemind_ParametersType26", type=Freemind_HookType, multiplicity=Multiplicity(1, 1)),
        Property(name="Freemind_HookType25", type=Freemind_ParametersType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
text27: BinaryAssociation = BinaryAssociation(
    name="text27",
    ends={
        Property(name="Freemind_TextType29", type=Freemind_HookType, multiplicity=Multiplicity(1, 1)),
        Property(name="Freemind_HookType28", type=Freemind_TextType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arrowlink33: BinaryAssociation = BinaryAssociation(
    name="arrowlink33",
    ends={
        Property(name="Freemind_ArrowlinkType35", type=Freemind_NodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="Freemind_NodeType34", type=Freemind_ArrowlinkType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node30: BinaryAssociation = BinaryAssociation(
    name="node30",
    ends={
        Property(name="Freemind_NodeType32", type=Freemind_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="Freemind_MapType31", type=Freemind_NodeType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
edge39: BinaryAssociation = BinaryAssociation(
    name="edge39",
    ends={
        Property(name="Freemind_EdgeType41", type=Freemind_NodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="Freemind_NodeType40", type=Freemind_EdgeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
font42: BinaryAssociation = BinaryAssociation(
    name="font42",
    ends={
        Property(name="Freemind_FontType44", type=Freemind_NodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="Freemind_NodeType43", type=Freemind_FontType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cloud36: BinaryAssociation = BinaryAssociation(
    name="cloud36",
    ends={
        Property(name="Freemind_CloudType38", type=Freemind_NodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="Freemind_NodeType37", type=Freemind_CloudType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node52: BinaryAssociation = BinaryAssociation(
    name="node52",
    ends={
        Property(name="Freemind_NodeType51", type=Freemind_NodeType, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="Freemind_NodeType53", type=Freemind_NodeType, multiplicity=Multiplicity(1, 1))
    }
)
hook45: BinaryAssociation = BinaryAssociation(
    name="hook45",
    ends={
        Property(name="Freemind_HookType47", type=Freemind_NodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="Freemind_NodeType46", type=Freemind_HookType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
icon48: BinaryAssociation = BinaryAssociation(
    name="icon48",
    ends={
        Property(name="Freemind_IconType50", type=Freemind_NodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="Freemind_NodeType49", type=Freemind_IconType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="Freemind",
    types={Freemind_ArrowlinkType, Freemind_EStringToStringMapEntry, Freemind_CloudType, Freemind_DocumentRoot, Freemind_IconType, Freemind_MapType, Freemind_EdgeType, Freemind_FontType, Freemind_HookType, Freemind_NodeType, Freemind_ParametersType, Freemind_TextType, BOLDType, FOLDEDType, ITALICType, POSITIONType},
    associations={xMLNSPrefixMap0, cloud6, xSISchemaLocation1, arrowlink4, icon14, map16, edge8, font10, hook12, node18, parameters20, text22, parameters24, text27, arrowlink33, node30, edge39, font42, cloud36, node52, hook45, icon48},
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