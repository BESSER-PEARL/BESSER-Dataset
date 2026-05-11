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
ColorLed: Enumeration = Enumeration(
    name="ColorLed",
    literals={
            EnumerationLiteral(name="BLUE"),
			EnumerationLiteral(name="RED"),
			EnumerationLiteral(name="YELLOW"),
			EnumerationLiteral(name="GREEN"),
			EnumerationLiteral(name="WHITE")
    }
)

Mode: Enumeration = Enumeration(
    name="Mode",
    literals={
            EnumerationLiteral(name="OFF"),
			EnumerationLiteral(name="ON")
    }
)

EBool: Enumeration = Enumeration(
    name="EBool",
    literals={
            EnumerationLiteral(name="TRUE"),
			EnumerationLiteral(name="FALSE")
    }
)

# Classes
drn_Hmax = Class(name="drn_Hmax")
drn_Parametre = Class(name="drn_Parametre")
drn_Expression = Class(name="drn_Expression")
drn_Model = Class(name="drn_Model")
drn_Context = Class(name="drn_Context")
drn_Assignement = Class(name="drn_Assignement")
drn_RefPart = Class(name="drn_RefPart")
drn_Limit = Class(name="drn_Limit")
drn_Vmax = Class(name="drn_Vmax")
Limit = Class(name="Limit")
drn_DepZ_Impl = Class(name="drn_DepZ_Impl")
drn_With = Class(name="drn_With")
Expression = Class(name="Expression")
drn_And = Class(name="drn_And")
drn_Rotate = Class(name="drn_Rotate")
drn_DepX_Impl = Class(name="drn_DepX_Impl")
drn_DepY_Impl = Class(name="drn_DepY_Impl")
drn_DepXZ_IMPL = Class(name="drn_DepXZ_IMPL")
drn_DepXY_IMPL = Class(name="drn_DepXY_IMPL")
drn_UP = Class(name="drn_UP")
DepZ_Impl = Class(name="DepZ_Impl")
drn_DOWN = Class(name="drn_DOWN")
drn_DepXY = Class(name="drn_DepXY")
DepXY_IMPL = Class(name="DepXY_IMPL")
drn_FORWARD = Class(name="drn_FORWARD")
DepY_Impl = Class(name="DepY_Impl")
drn_BACKWARD = Class(name="drn_BACKWARD")
drn_LEFT = Class(name="drn_LEFT")
DepX_Impl = Class(name="DepX_Impl")
drn_RIGHT = Class(name="drn_RIGHT")
drn_CERCLEYZ = Class(name="drn_CERCLEYZ")
drn_CARREYZ = Class(name="drn_CARREYZ")
drn_CERCLEXY = Class(name="drn_CERCLEXY")
drn_CARREXY = Class(name="drn_CARREXY")
drn_DepYZ_IMPL = Class(name="drn_DepYZ_IMPL")
drn_DepYZ = Class(name="drn_DepYZ")
DepYZ_IMPL = Class(name="DepYZ_IMPL")
drn_Flip = Class(name="drn_Flip")
drn_DepXZ = Class(name="drn_DepXZ")
DepXZ_IMPL = Class(name="DepXZ_IMPL")
drn_DepXYZ_IMPL = Class(name="drn_DepXYZ_IMPL")
drn_DepXYZ = Class(name="drn_DepXYZ")
DepXYZ_IMPL = Class(name="DepXYZ_IMPL")
drn_Land = Class(name="drn_Land")
drn_Option = Class(name="drn_Option")
drn_Wait = Class(name="drn_Wait")
drn_TakeOff = Class(name="drn_TakeOff")
drn_Led_Impl = Class(name="drn_Led_Impl")
Option = Class(name="Option")
drn_LedBlink = Class(name="drn_LedBlink")
drn_CameraFront = Class(name="drn_CameraFront")
drn_CameraBottom = Class(name="drn_CameraBottom")

# drn_Hmax class attributes and methods

# drn_Parametre class attributes and methods
drn_Parametre_name: Property = Property(name="name", type=StringType)
drn_Parametre.attributes={drn_Parametre_name}

# drn_Expression class attributes and methods
drn_Expression_repeatCST: Property = Property(name="repeatCST", type=StringType)
drn_Expression.attributes={drn_Expression_repeatCST}

# drn_Model class attributes and methods

# drn_Context class attributes and methods

# drn_Assignement class attributes and methods
drn_Assignement_name: Property = Property(name="name", type=StringType)
drn_Assignement.attributes={drn_Assignement_name}

# drn_RefPart class attributes and methods
drn_RefPart_params: Property = Property(name="params", type=StringType)
drn_RefPart.attributes={drn_RefPart_params}

# drn_Limit class attributes and methods
drn_Limit_name: Property = Property(name="name", type=StringType)
drn_Limit_value: Property = Property(name="value", type=StringType)
drn_Limit.attributes={drn_Limit_value, drn_Limit_name}

# drn_Vmax class attributes and methods

# Limit class attributes and methods

# drn_DepZ_Impl class attributes and methods
drn_DepZ_Impl_name: Property = Property(name="name", type=StringType)
drn_DepZ_Impl_distanceCST: Property = Property(name="distanceCST", type=StringType)
drn_DepZ_Impl_tempsCST: Property = Property(name="tempsCST", type=StringType)
drn_DepZ_Impl.attributes={drn_DepZ_Impl_tempsCST, drn_DepZ_Impl_name, drn_DepZ_Impl_distanceCST}

# drn_With class attributes and methods
drn_With_name: Property = Property(name="name", type=StringType)
drn_With.attributes={drn_With_name}

# Expression class attributes and methods

# drn_And class attributes and methods
drn_And_name: Property = Property(name="name", type=StringType)
drn_And.attributes={drn_And_name}

# drn_Rotate class attributes and methods
drn_Rotate_name: Property = Property(name="name", type=StringType)
drn_Rotate_angleCST: Property = Property(name="angleCST", type=StringType)
drn_Rotate_tempsCST: Property = Property(name="tempsCST", type=StringType)
drn_Rotate.attributes={drn_Rotate_name, drn_Rotate_tempsCST, drn_Rotate_angleCST}

# drn_DepX_Impl class attributes and methods
drn_DepX_Impl_name: Property = Property(name="name", type=StringType)
drn_DepX_Impl_distanceCST: Property = Property(name="distanceCST", type=StringType)
drn_DepX_Impl_tempsCST: Property = Property(name="tempsCST", type=StringType)
drn_DepX_Impl.attributes={drn_DepX_Impl_tempsCST, drn_DepX_Impl_distanceCST, drn_DepX_Impl_name}

# drn_DepY_Impl class attributes and methods
drn_DepY_Impl_name: Property = Property(name="name", type=StringType)
drn_DepY_Impl_distanceCST: Property = Property(name="distanceCST", type=StringType)
drn_DepY_Impl_tempsCST: Property = Property(name="tempsCST", type=StringType)
drn_DepY_Impl.attributes={drn_DepY_Impl_name, drn_DepY_Impl_tempsCST, drn_DepY_Impl_distanceCST}

# drn_DepXZ_IMPL class attributes and methods

# drn_DepXY_IMPL class attributes and methods
drn_DepXY_IMPL_name: Property = Property(name="name", type=StringType)
drn_DepXY_IMPL_tempsCST: Property = Property(name="tempsCST", type=StringType)
drn_DepXY_IMPL.attributes={drn_DepXY_IMPL_name, drn_DepXY_IMPL_tempsCST}

# drn_UP class attributes and methods

# DepZ_Impl class attributes and methods

# drn_DOWN class attributes and methods

# drn_DepXY class attributes and methods
drn_DepXY_distanceCST: Property = Property(name="distanceCST", type=StringType)
drn_DepXY.attributes={drn_DepXY_distanceCST}

# DepXY_IMPL class attributes and methods

# drn_FORWARD class attributes and methods

# DepY_Impl class attributes and methods

# drn_BACKWARD class attributes and methods

# drn_LEFT class attributes and methods

# DepX_Impl class attributes and methods

# drn_RIGHT class attributes and methods

# drn_CERCLEYZ class attributes and methods
drn_CERCLEYZ_rayonCST: Property = Property(name="rayonCST", type=StringType)
drn_CERCLEYZ.attributes={drn_CERCLEYZ_rayonCST}

# drn_CARREYZ class attributes and methods
drn_CARREYZ_coteCST: Property = Property(name="coteCST", type=StringType)
drn_CARREYZ.attributes={drn_CARREYZ_coteCST}

# drn_CERCLEXY class attributes and methods
drn_CERCLEXY_rayonCST: Property = Property(name="rayonCST", type=StringType)
drn_CERCLEXY.attributes={drn_CERCLEXY_rayonCST}

# drn_CARREXY class attributes and methods
drn_CARREXY_coteCST: Property = Property(name="coteCST", type=StringType)
drn_CARREXY.attributes={drn_CARREXY_coteCST}

# drn_DepYZ_IMPL class attributes and methods
drn_DepYZ_IMPL_name: Property = Property(name="name", type=StringType)
drn_DepYZ_IMPL_tempsCST: Property = Property(name="tempsCST", type=StringType)
drn_DepYZ_IMPL.attributes={drn_DepYZ_IMPL_name, drn_DepYZ_IMPL_tempsCST}

# drn_DepYZ class attributes and methods
drn_DepYZ_distanceCST: Property = Property(name="distanceCST", type=StringType)
drn_DepYZ.attributes={drn_DepYZ_distanceCST}

# DepYZ_IMPL class attributes and methods

# drn_Flip class attributes and methods

# drn_DepXZ class attributes and methods
drn_DepXZ_name: Property = Property(name="name", type=StringType)
drn_DepXZ_distanceCST: Property = Property(name="distanceCST", type=StringType)
drn_DepXZ_tempsCST: Property = Property(name="tempsCST", type=StringType)
drn_DepXZ.attributes={drn_DepXZ_tempsCST, drn_DepXZ_name, drn_DepXZ_distanceCST}

# DepXZ_IMPL class attributes and methods

# drn_DepXYZ_IMPL class attributes and methods
drn_DepXYZ_IMPL_name: Property = Property(name="name", type=StringType)
drn_DepXYZ_IMPL.attributes={drn_DepXYZ_IMPL_name}

# drn_DepXYZ class attributes and methods
drn_DepXYZ_distanceCST: Property = Property(name="distanceCST", type=StringType)
drn_DepXYZ_tempsCST: Property = Property(name="tempsCST", type=StringType)
drn_DepXYZ.attributes={drn_DepXYZ_tempsCST, drn_DepXYZ_distanceCST}

# DepXYZ_IMPL class attributes and methods

# drn_Land class attributes and methods
drn_Land_name: Property = Property(name="name", type=StringType)
drn_Land.attributes={drn_Land_name}

# drn_Option class attributes and methods
drn_Option_name: Property = Property(name="name", type=StringType)
drn_Option.attributes={drn_Option_name}

# drn_Wait class attributes and methods
drn_Wait_name: Property = Property(name="name", type=StringType)
drn_Wait_tempsCST: Property = Property(name="tempsCST", type=StringType)
drn_Wait.attributes={drn_Wait_tempsCST, drn_Wait_name}

# drn_TakeOff class attributes and methods
drn_TakeOff_name: Property = Property(name="name", type=StringType)
drn_TakeOff.attributes={drn_TakeOff_name}

# drn_Led_Impl class attributes and methods
drn_Led_Impl_color: Property = Property(name="color", type=StringType)
drn_Led_Impl.attributes={drn_Led_Impl_color}

# Option class attributes and methods

# drn_LedBlink class attributes and methods
drn_LedBlink_color: Property = Property(name="color", type=StringType)
drn_LedBlink_blink_per_secCST: Property = Property(name="blink_per_secCST", type=StringType)
drn_LedBlink.attributes={drn_LedBlink_color, drn_LedBlink_blink_per_secCST}

# drn_CameraFront class attributes and methods
drn_CameraFront_mode: Property = Property(name="mode", type=StringType)
drn_CameraFront.attributes={drn_CameraFront_mode}

# drn_CameraBottom class attributes and methods
drn_CameraBottom_mode: Property = Property(name="mode", type=StringType)
drn_CameraBottom.attributes={drn_CameraBottom_mode}

# Relationships
parametre7: BinaryAssociation = BinaryAssociation(
    name="parametre7",
    ends={
        Property(name="drn_Parametre", type=drn_Assignement, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_Assignement8", type=drn_Parametre, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operandes9: BinaryAssociation = BinaryAssociation(
    name="operandes9",
    ends={
        Property(name="drn_Expression", type=drn_Assignement, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_Assignement10", type=drn_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
context0: BinaryAssociation = BinaryAssociation(
    name="context0",
    ends={
        Property(name="drn_Context", type=drn_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_Model", type=drn_Context, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignement1: BinaryAssociation = BinaryAssociation(
    name="assignement1",
    ends={
        Property(name="drn_Assignement", type=drn_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_Model2", type=drn_Assignement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
main3: BinaryAssociation = BinaryAssociation(
    name="main3",
    ends={
        Property(name="drn_RefPart", type=drn_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_Model4", type=drn_RefPart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
limit5: BinaryAssociation = BinaryAssociation(
    name="limit5",
    ends={
        Property(name="drn_Limit", type=drn_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_Context6", type=drn_Limit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
depxy29: BinaryAssociation = BinaryAssociation(
    name="depxy29",
    ends={
        Property(name="drn_DepXY_IMPL", type=drn_And, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_And30", type=drn_DepXY_IMPL, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
depz31: BinaryAssociation = BinaryAssociation(
    name="depz31",
    ends={
        Property(name="drn_DepZ_Impl", type=drn_And, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_And32", type=drn_DepZ_Impl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
distanceVar33: BinaryAssociation = BinaryAssociation(
    name="distanceVar33",
    ends={
        Property(name="drn_Parametre35", type=drn_DepY_Impl, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_DepY_Impl34", type=drn_Parametre, multiplicity=Multiplicity(0, 1))
    }
)
repeatVAR11: BinaryAssociation = BinaryAssociation(
    name="repeatVAR11",
    ends={
        Property(name="drn_Parametre13", type=drn_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_Expression12", type=drn_Parametre, multiplicity=Multiplicity(0, 1))
    }
)
with_14: BinaryAssociation = BinaryAssociation(
    name="with_14",
    ends={
        Property(name="drn_With", type=drn_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_Expression15", type=drn_With, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
then17: BinaryAssociation = BinaryAssociation(
    name="then17",
    ends={
        Property(name="drn_Expression18", type=drn_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_Expression16", type=drn_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable_partie19: BinaryAssociation = BinaryAssociation(
    name="variable_partie19",
    ends={
        Property(name="drn_Assignement21", type=drn_RefPart, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_RefPart20", type=drn_Assignement, multiplicity=Multiplicity(0, 1))
    }
)
rotate22: BinaryAssociation = BinaryAssociation(
    name="rotate22",
    ends={
        Property(name="drn_Rotate", type=drn_And, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_And", type=drn_Rotate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
depx23: BinaryAssociation = BinaryAssociation(
    name="depx23",
    ends={
        Property(name="drn_DepX_Impl", type=drn_And, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_And24", type=drn_DepX_Impl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
depy25: BinaryAssociation = BinaryAssociation(
    name="depy25",
    ends={
        Property(name="drn_DepY_Impl", type=drn_And, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_And26", type=drn_DepY_Impl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
depxz27: BinaryAssociation = BinaryAssociation(
    name="depxz27",
    ends={
        Property(name="drn_DepXZ_IMPL", type=drn_And, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_And28", type=drn_DepXZ_IMPL, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tempsVAR51: BinaryAssociation = BinaryAssociation(
    name="tempsVAR51",
    ends={
        Property(name="drn_Parametre53", type=drn_DepXY_IMPL, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_DepXY_IMPL52", type=drn_Parametre, multiplicity=Multiplicity(0, 1))
    }
)
tempsVAR36: BinaryAssociation = BinaryAssociation(
    name="tempsVAR36",
    ends={
        Property(name="drn_Parametre38", type=drn_DepY_Impl, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_DepY_Impl37", type=drn_Parametre, multiplicity=Multiplicity(0, 1))
    }
)
distanceVar39: BinaryAssociation = BinaryAssociation(
    name="distanceVar39",
    ends={
        Property(name="drn_Parametre41", type=drn_DepX_Impl, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_DepX_Impl40", type=drn_Parametre, multiplicity=Multiplicity(0, 1))
    }
)
tempsVAR42: BinaryAssociation = BinaryAssociation(
    name="tempsVAR42",
    ends={
        Property(name="drn_Parametre44", type=drn_DepX_Impl, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_DepX_Impl43", type=drn_Parametre, multiplicity=Multiplicity(0, 1))
    }
)
distanceVar45: BinaryAssociation = BinaryAssociation(
    name="distanceVar45",
    ends={
        Property(name="drn_Parametre47", type=drn_DepZ_Impl, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_DepZ_Impl46", type=drn_Parametre, multiplicity=Multiplicity(0, 1))
    }
)
tempsVAR48: BinaryAssociation = BinaryAssociation(
    name="tempsVAR48",
    ends={
        Property(name="drn_Parametre50", type=drn_DepZ_Impl, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_DepZ_Impl49", type=drn_Parametre, multiplicity=Multiplicity(0, 1))
    }
)
rayonVar64: BinaryAssociation = BinaryAssociation(
    name="rayonVar64",
    ends={
        Property(name="drn_Parametre65", type=drn_CERCLEYZ, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_CERCLEYZ", type=drn_Parametre, multiplicity=Multiplicity(0, 1))
    }
)
coteVAR66: BinaryAssociation = BinaryAssociation(
    name="coteVAR66",
    ends={
        Property(name="drn_Parametre67", type=drn_CARREYZ, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_CARREYZ", type=drn_Parametre, multiplicity=Multiplicity(0, 1))
    }
)
distanceVar54: BinaryAssociation = BinaryAssociation(
    name="distanceVar54",
    ends={
        Property(name="drn_Parametre55", type=drn_DepXY, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_DepXY", type=drn_Parametre, multiplicity=Multiplicity(0, 1))
    }
)
rayonVar56: BinaryAssociation = BinaryAssociation(
    name="rayonVar56",
    ends={
        Property(name="drn_Parametre57", type=drn_CERCLEXY, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_CERCLEXY", type=drn_Parametre, multiplicity=Multiplicity(0, 1))
    }
)
coteVAR58: BinaryAssociation = BinaryAssociation(
    name="coteVAR58",
    ends={
        Property(name="drn_Parametre59", type=drn_CARREXY, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_CARREXY", type=drn_Parametre, multiplicity=Multiplicity(0, 1))
    }
)
tempsVAR60: BinaryAssociation = BinaryAssociation(
    name="tempsVAR60",
    ends={
        Property(name="drn_Parametre61", type=drn_DepYZ_IMPL, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_DepYZ_IMPL", type=drn_Parametre, multiplicity=Multiplicity(0, 1))
    }
)
distanceVar62: BinaryAssociation = BinaryAssociation(
    name="distanceVar62",
    ends={
        Property(name="drn_Parametre63", type=drn_DepYZ, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_DepYZ", type=drn_Parametre, multiplicity=Multiplicity(0, 1))
    }
)
tempsVAR75: BinaryAssociation = BinaryAssociation(
    name="tempsVAR75",
    ends={
        Property(name="drn_Parametre77", type=drn_DepXYZ, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_DepXYZ76", type=drn_Parametre, multiplicity=Multiplicity(0, 1))
    }
)
distanceVar68: BinaryAssociation = BinaryAssociation(
    name="distanceVar68",
    ends={
        Property(name="drn_Parametre69", type=drn_DepXZ, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_DepXZ", type=drn_Parametre, multiplicity=Multiplicity(0, 1))
    }
)
tempsVAR70: BinaryAssociation = BinaryAssociation(
    name="tempsVAR70",
    ends={
        Property(name="drn_Parametre72", type=drn_DepXZ, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_DepXZ71", type=drn_Parametre, multiplicity=Multiplicity(0, 1))
    }
)
distanceVar73: BinaryAssociation = BinaryAssociation(
    name="distanceVar73",
    ends={
        Property(name="drn_Parametre74", type=drn_DepXYZ, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_DepXYZ", type=drn_Parametre, multiplicity=Multiplicity(0, 1))
    }
)
angleVAR78: BinaryAssociation = BinaryAssociation(
    name="angleVAR78",
    ends={
        Property(name="drn_Parametre80", type=drn_Rotate, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_Rotate79", type=drn_Parametre, multiplicity=Multiplicity(0, 1))
    }
)
tempsVAR81: BinaryAssociation = BinaryAssociation(
    name="tempsVAR81",
    ends={
        Property(name="drn_Parametre83", type=drn_Rotate, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_Rotate82", type=drn_Parametre, multiplicity=Multiplicity(0, 1))
    }
)
tempsVAR84: BinaryAssociation = BinaryAssociation(
    name="tempsVAR84",
    ends={
        Property(name="drn_Parametre85", type=drn_Wait, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_Wait", type=drn_Parametre, multiplicity=Multiplicity(0, 1))
    }
)
option86: BinaryAssociation = BinaryAssociation(
    name="option86",
    ends={
        Property(name="drn_Option", type=drn_With, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_With87", type=drn_Option, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blink_per_secVAR88: BinaryAssociation = BinaryAssociation(
    name="blink_per_secVAR88",
    ends={
        Property(name="drn_Parametre89", type=drn_LedBlink, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_LedBlink", type=drn_Parametre, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_drn_Hmax_Limit = Generalization(general=Limit, specific=drn_Hmax)
gen_drn_Vmax_Limit = Generalization(general=Limit, specific=drn_Vmax)
gen_drn_DepY_Impl_Expression = Generalization(general=Expression, specific=drn_DepY_Impl)
gen_drn_RefPart_Expression = Generalization(general=Expression, specific=drn_RefPart)
gen_drn_And_Expression = Generalization(general=Expression, specific=drn_And)
gen_drn_UP_DepZ_Impl = Generalization(general=DepZ_Impl, specific=drn_UP)
gen_drn_DOWN_DepZ_Impl = Generalization(general=DepZ_Impl, specific=drn_DOWN)
gen_drn_DepXY_IMPL_Expression = Generalization(general=Expression, specific=drn_DepXY_IMPL)
gen_drn_DepXY_DepXY_IMPL = Generalization(general=DepXY_IMPL, specific=drn_DepXY)
gen_drn_FORWARD_DepY_Impl = Generalization(general=DepY_Impl, specific=drn_FORWARD)
gen_drn_BACKWARD_DepY_Impl = Generalization(general=DepY_Impl, specific=drn_BACKWARD)
gen_drn_DepX_Impl_Expression = Generalization(general=Expression, specific=drn_DepX_Impl)
gen_drn_LEFT_DepX_Impl = Generalization(general=DepX_Impl, specific=drn_LEFT)
gen_drn_RIGHT_DepX_Impl = Generalization(general=DepX_Impl, specific=drn_RIGHT)
gen_drn_DepZ_Impl_Expression = Generalization(general=Expression, specific=drn_DepZ_Impl)
gen_drn_CERCLEYZ_DepYZ_IMPL = Generalization(general=DepYZ_IMPL, specific=drn_CERCLEYZ)
gen_drn_CARREYZ_DepYZ_IMPL = Generalization(general=DepYZ_IMPL, specific=drn_CARREYZ)
gen_drn_CERCLEXY_DepXY_IMPL = Generalization(general=DepXY_IMPL, specific=drn_CERCLEXY)
gen_drn_CARREXY_DepXY_IMPL = Generalization(general=DepXY_IMPL, specific=drn_CARREXY)
gen_drn_DepYZ_IMPL_Expression = Generalization(general=Expression, specific=drn_DepYZ_IMPL)
gen_drn_DepYZ_DepYZ_IMPL = Generalization(general=DepYZ_IMPL, specific=drn_DepYZ)
gen_drn_Flip_DepXYZ_IMPL = Generalization(general=DepXYZ_IMPL, specific=drn_Flip)
gen_drn_Rotate_Expression = Generalization(general=Expression, specific=drn_Rotate)
gen_drn_DepXZ_IMPL_Expression = Generalization(general=Expression, specific=drn_DepXZ_IMPL)
gen_drn_DepXZ_DepXZ_IMPL = Generalization(general=DepXZ_IMPL, specific=drn_DepXZ)
gen_drn_DepXYZ_IMPL_Expression = Generalization(general=Expression, specific=drn_DepXYZ_IMPL)
gen_drn_DepXYZ_DepXYZ_IMPL = Generalization(general=DepXYZ_IMPL, specific=drn_DepXYZ)
gen_drn_Land_Expression = Generalization(general=Expression, specific=drn_Land)
gen_drn_Wait_Expression = Generalization(general=Expression, specific=drn_Wait)
gen_drn_TakeOff_Expression = Generalization(general=Expression, specific=drn_TakeOff)
gen_drn_Led_Impl_Option = Generalization(general=Option, specific=drn_Led_Impl)
gen_drn_LedBlink_Option = Generalization(general=Option, specific=drn_LedBlink)
gen_drn_CameraFront_Option = Generalization(general=Option, specific=drn_CameraFront)
gen_drn_CameraBottom_Option = Generalization(general=Option, specific=drn_CameraBottom)

# Domain Model
domain_model = DomainModel(
    name="drn",
    types={drn_Hmax, drn_Parametre, drn_Expression, drn_Model, drn_Context, drn_Assignement, drn_RefPart, drn_Limit, drn_Vmax, Limit, drn_DepZ_Impl, drn_With, Expression, drn_And, drn_Rotate, drn_DepX_Impl, drn_DepY_Impl, drn_DepXZ_IMPL, drn_DepXY_IMPL, drn_UP, DepZ_Impl, drn_DOWN, drn_DepXY, DepXY_IMPL, drn_FORWARD, DepY_Impl, drn_BACKWARD, drn_LEFT, DepX_Impl, drn_RIGHT, drn_CERCLEYZ, drn_CARREYZ, drn_CERCLEXY, drn_CARREXY, drn_DepYZ_IMPL, drn_DepYZ, DepYZ_IMPL, drn_Flip, drn_DepXZ, DepXZ_IMPL, drn_DepXYZ_IMPL, drn_DepXYZ, DepXYZ_IMPL, drn_Land, drn_Option, drn_Wait, drn_TakeOff, drn_Led_Impl, Option, drn_LedBlink, drn_CameraFront, drn_CameraBottom, ColorLed, Mode, EBool},
    associations={parametre7, operandes9, context0, assignement1, main3, limit5, depxy29, depz31, distanceVar33, repeatVAR11, with_14, then17, variable_partie19, rotate22, depx23, depy25, depxz27, tempsVAR51, tempsVAR36, distanceVar39, tempsVAR42, distanceVar45, tempsVAR48, rayonVar64, coteVAR66, distanceVar54, rayonVar56, coteVAR58, tempsVAR60, distanceVar62, tempsVAR75, distanceVar68, tempsVAR70, distanceVar73, angleVAR78, tempsVAR81, tempsVAR84, option86, blink_per_secVAR88},
    generalizations={gen_drn_Hmax_Limit, gen_drn_Vmax_Limit, gen_drn_DepY_Impl_Expression, gen_drn_RefPart_Expression, gen_drn_And_Expression, gen_drn_UP_DepZ_Impl, gen_drn_DOWN_DepZ_Impl, gen_drn_DepXY_IMPL_Expression, gen_drn_DepXY_DepXY_IMPL, gen_drn_FORWARD_DepY_Impl, gen_drn_BACKWARD_DepY_Impl, gen_drn_DepX_Impl_Expression, gen_drn_LEFT_DepX_Impl, gen_drn_RIGHT_DepX_Impl, gen_drn_DepZ_Impl_Expression, gen_drn_CERCLEYZ_DepYZ_IMPL, gen_drn_CARREYZ_DepYZ_IMPL, gen_drn_CERCLEXY_DepXY_IMPL, gen_drn_CARREXY_DepXY_IMPL, gen_drn_DepYZ_IMPL_Expression, gen_drn_DepYZ_DepYZ_IMPL, gen_drn_Flip_DepXYZ_IMPL, gen_drn_Rotate_Expression, gen_drn_DepXZ_IMPL_Expression, gen_drn_DepXZ_DepXZ_IMPL, gen_drn_DepXYZ_IMPL_Expression, gen_drn_DepXYZ_DepXYZ_IMPL, gen_drn_Land_Expression, gen_drn_Wait_Expression, gen_drn_TakeOff_Expression, gen_drn_Led_Impl_Option, gen_drn_LedBlink_Option, gen_drn_CameraFront_Option, gen_drn_CameraBottom_Option},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)