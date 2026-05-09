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
TypePrimitif: Enumeration = Enumeration(
    name="TypePrimitif",
    literals={
            EnumerationLiteral(name="boolType"),
			EnumerationLiteral(name="realType"),
			EnumerationLiteral(name="intType"),
			EnumerationLiteral(name="stringType")
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

DirectionType: Enumeration = Enumeration(
    name="DirectionType",
    literals={
            EnumerationLiteral(name="FRONT"),
			EnumerationLiteral(name="BEHIND"),
			EnumerationLiteral(name="LEFT"),
			EnumerationLiteral(name="RIGHT")
    }
)

Where: Enumeration = Enumeration(
    name="Where",
    literals={
            EnumerationLiteral(name="INDOOR"),
			EnumerationLiteral(name="OUTDOOR")
    }
)

# Classes
drn_Root = Class(name="drn_Root")
drn_Model = Class(name="drn_Model")
Root = Class(name="Root")
drn_Configuration = Class(name="drn_Configuration")
drn_Library = Class(name="drn_Library")
drn_Assignement = Class(name="drn_Assignement")
drn_With = Class(name="drn_With")
drn_Context = Class(name="drn_Context")
drn_RefPart = Class(name="drn_RefPart")
drn_TypeGeneric = Class(name="drn_TypeGeneric")
drn_Device = Class(name="drn_Device")
drn_ConnectionType = Class(name="drn_ConnectionType")
drn_Limit = Class(name="drn_Limit")
drn_Surface = Class(name="drn_Surface")
Limit = Class(name="Limit")
drn_InitialPosition = Class(name="drn_InitialPosition")
drn_InitialDirection = Class(name="drn_InitialDirection")
InitialPosition = Class(name="InitialPosition")
drn_InitialPositionX = Class(name="drn_InitialPositionX")
drn_InitialPositionY = Class(name="drn_InitialPositionY")
drn_MaxLength = Class(name="drn_MaxLength")
Surface = Class(name="Surface")
drn_MaxWidth = Class(name="drn_MaxWidth")
drn_MaxSpeed = Class(name="drn_MaxSpeed")
drn_MaxHeight = Class(name="drn_MaxHeight")
drn_Expression = Class(name="drn_Expression")
drn_Movement = Class(name="drn_Movement")
Movement = Class(name="Movement")
drn_RefPartLib = Class(name="drn_RefPartLib")
drn_And = Class(name="drn_And")
drn_Rotate = Class(name="drn_Rotate")
drn_DepX_Impl = Class(name="drn_DepX_Impl")
drn_DepY_Impl = Class(name="drn_DepY_Impl")
drn_DepZ_Impl = Class(name="drn_DepZ_Impl")
drn_FORWARD = Class(name="drn_FORWARD")
DepY_Impl = Class(name="DepY_Impl")
drn_BACKWARD = Class(name="drn_BACKWARD")
drn_LEFT = Class(name="drn_LEFT")
DepX_Impl = Class(name="DepX_Impl")
drn_UP = Class(name="drn_UP")
drn_RIGHT = Class(name="drn_RIGHT")
DepZ_Impl = Class(name="DepZ_Impl")
drn_DOWN = Class(name="drn_DOWN")
drn_DepXY_IMPL = Class(name="drn_DepXY_IMPL")
drn_CERCLEXY = Class(name="drn_CERCLEXY")
DepXY_IMPL = Class(name="DepXY_IMPL")
drn_CARREXY = Class(name="drn_CARREXY")
drn_DepYZ_IMPL = Class(name="drn_DepYZ_IMPL")
drn_CERCLEYZ = Class(name="drn_CERCLEYZ")
DepYZ_IMPL = Class(name="DepYZ_IMPL")
drn_CARREYZ = Class(name="drn_CARREYZ")
drn_DepXZ_IMPL = Class(name="drn_DepXZ_IMPL")
drn_CERCLEXZ = Class(name="drn_CERCLEXZ")
DepXZ_IMPL = Class(name="DepXZ_IMPL")
drn_CARREXZ = Class(name="drn_CARREXZ")
drn_DepXYZ_IMPL = Class(name="drn_DepXYZ_IMPL")
drn_Flip = Class(name="drn_Flip")
DepXYZ_IMPL = Class(name="DepXYZ_IMPL")
drn_Wait = Class(name="drn_Wait")
drn_TakeOff = Class(name="drn_TakeOff")
drn_Land = Class(name="drn_Land")
drn_Declaration = Class(name="drn_Declaration")
drn_Definition = Class(name="drn_Definition")
drn_Element = Class(name="drn_Element")
drn_RefDevice = Class(name="drn_RefDevice")
drn_Bluetooth = Class(name="drn_Bluetooth")
ConnectionType = Class(name="ConnectionType")
drn_Wifi = Class(name="drn_Wifi")

# drn_Root class attributes and methods

# drn_Model class attributes and methods

# Root class attributes and methods

# drn_Configuration class attributes and methods
drn_Configuration_name: Property = Property(name="name", type=StringType)
drn_Configuration.attributes={drn_Configuration_name}

# drn_Library class attributes and methods
drn_Library_name: Property = Property(name="name", type=StringType)
drn_Library.attributes={drn_Library_name}

# drn_Assignement class attributes and methods
drn_Assignement_name: Property = Property(name="name", type=StringType)
drn_Assignement.attributes={drn_Assignement_name}

# drn_With class attributes and methods
drn_With_name: Property = Property(name="name", type=StringType)
drn_With.attributes={drn_With_name}

# drn_Context class attributes and methods
drn_Context_name: Property = Property(name="name", type=StringType)
drn_Context_where: Property = Property(name="where", type=StringType)
drn_Context.attributes={drn_Context_name, drn_Context_where}

# drn_RefPart class attributes and methods

# drn_TypeGeneric class attributes and methods
drn_TypeGeneric_name: Property = Property(name="name", type=StringType)
drn_TypeGeneric.attributes={drn_TypeGeneric_name}

# drn_Device class attributes and methods
drn_Device_name: Property = Property(name="name", type=StringType)
drn_Device.attributes={drn_Device_name}

# drn_ConnectionType class attributes and methods
drn_ConnectionType_name: Property = Property(name="name", type=StringType)
drn_ConnectionType_adress: Property = Property(name="adress", type=StringType)
drn_ConnectionType.attributes={drn_ConnectionType_adress, drn_ConnectionType_name}

# drn_Limit class attributes and methods
drn_Limit_name: Property = Property(name="name", type=StringType)
drn_Limit.attributes={drn_Limit_name}

# drn_Surface class attributes and methods
drn_Surface_value: Property = Property(name="value", type=IntegerType)
drn_Surface.attributes={drn_Surface_value}

# Limit class attributes and methods

# drn_InitialPosition class attributes and methods

# drn_InitialDirection class attributes and methods
drn_InitialDirection_value: Property = Property(name="value", type=StringType)
drn_InitialDirection.attributes={drn_InitialDirection_value}

# InitialPosition class attributes and methods

# drn_InitialPositionX class attributes and methods
drn_InitialPositionX_value: Property = Property(name="value", type=IntegerType)
drn_InitialPositionX.attributes={drn_InitialPositionX_value}

# drn_InitialPositionY class attributes and methods
drn_InitialPositionY_value: Property = Property(name="value", type=IntegerType)
drn_InitialPositionY.attributes={drn_InitialPositionY_value}

# drn_MaxLength class attributes and methods

# Surface class attributes and methods

# drn_MaxWidth class attributes and methods

# drn_MaxSpeed class attributes and methods
drn_MaxSpeed_value: Property = Property(name="value", type=IntegerType)
drn_MaxSpeed.attributes={drn_MaxSpeed_value}

# drn_MaxHeight class attributes and methods

# drn_Expression class attributes and methods
drn_Expression_repeatCST: Property = Property(name="repeatCST", type=IntegerType)
drn_Expression.attributes={drn_Expression_repeatCST}

# drn_Movement class attributes and methods

# Movement class attributes and methods

# drn_RefPartLib class attributes and methods

# drn_And class attributes and methods
drn_And_name: Property = Property(name="name", type=StringType)
drn_And.attributes={drn_And_name}

# drn_Rotate class attributes and methods
drn_Rotate_name: Property = Property(name="name", type=StringType)
drn_Rotate_angleCST: Property = Property(name="angleCST", type=StringType)
drn_Rotate_tempsCST: Property = Property(name="tempsCST", type=IntegerType)
drn_Rotate.attributes={drn_Rotate_tempsCST, drn_Rotate_name, drn_Rotate_angleCST}

# drn_DepX_Impl class attributes and methods
drn_DepX_Impl_name: Property = Property(name="name", type=StringType)
drn_DepX_Impl_distanceCST: Property = Property(name="distanceCST", type=IntegerType)
drn_DepX_Impl_tempsCST: Property = Property(name="tempsCST", type=IntegerType)
drn_DepX_Impl.attributes={drn_DepX_Impl_name, drn_DepX_Impl_tempsCST, drn_DepX_Impl_distanceCST}

# drn_DepY_Impl class attributes and methods
drn_DepY_Impl_name: Property = Property(name="name", type=StringType)
drn_DepY_Impl_distanceCST: Property = Property(name="distanceCST", type=IntegerType)
drn_DepY_Impl_tempsCST: Property = Property(name="tempsCST", type=IntegerType)
drn_DepY_Impl.attributes={drn_DepY_Impl_distanceCST, drn_DepY_Impl_tempsCST, drn_DepY_Impl_name}

# drn_DepZ_Impl class attributes and methods
drn_DepZ_Impl_name: Property = Property(name="name", type=StringType)
drn_DepZ_Impl_distanceCST: Property = Property(name="distanceCST", type=IntegerType)
drn_DepZ_Impl_tempsCST: Property = Property(name="tempsCST", type=IntegerType)
drn_DepZ_Impl.attributes={drn_DepZ_Impl_tempsCST, drn_DepZ_Impl_name, drn_DepZ_Impl_distanceCST}

# drn_FORWARD class attributes and methods

# DepY_Impl class attributes and methods

# drn_BACKWARD class attributes and methods

# drn_LEFT class attributes and methods

# DepX_Impl class attributes and methods

# drn_UP class attributes and methods

# drn_RIGHT class attributes and methods

# DepZ_Impl class attributes and methods

# drn_DOWN class attributes and methods

# drn_DepXY_IMPL class attributes and methods
drn_DepXY_IMPL_name: Property = Property(name="name", type=StringType)
drn_DepXY_IMPL_tempsCST: Property = Property(name="tempsCST", type=IntegerType)
drn_DepXY_IMPL.attributes={drn_DepXY_IMPL_tempsCST, drn_DepXY_IMPL_name}

# drn_CERCLEXY class attributes and methods
drn_CERCLEXY_rayonCST: Property = Property(name="rayonCST", type=IntegerType)
drn_CERCLEXY.attributes={drn_CERCLEXY_rayonCST}

# DepXY_IMPL class attributes and methods

# drn_CARREXY class attributes and methods
drn_CARREXY_coteCST: Property = Property(name="coteCST", type=IntegerType)
drn_CARREXY.attributes={drn_CARREXY_coteCST}

# drn_DepYZ_IMPL class attributes and methods
drn_DepYZ_IMPL_name: Property = Property(name="name", type=StringType)
drn_DepYZ_IMPL_tempsCST: Property = Property(name="tempsCST", type=IntegerType)
drn_DepYZ_IMPL.attributes={drn_DepYZ_IMPL_tempsCST, drn_DepYZ_IMPL_name}

# drn_CERCLEYZ class attributes and methods
drn_CERCLEYZ_rayonCST: Property = Property(name="rayonCST", type=IntegerType)
drn_CERCLEYZ.attributes={drn_CERCLEYZ_rayonCST}

# DepYZ_IMPL class attributes and methods

# drn_CARREYZ class attributes and methods
drn_CARREYZ_coteCST: Property = Property(name="coteCST", type=IntegerType)
drn_CARREYZ.attributes={drn_CARREYZ_coteCST}

# drn_DepXZ_IMPL class attributes and methods
drn_DepXZ_IMPL_name: Property = Property(name="name", type=StringType)
drn_DepXZ_IMPL_tempsCST: Property = Property(name="tempsCST", type=IntegerType)
drn_DepXZ_IMPL.attributes={drn_DepXZ_IMPL_tempsCST, drn_DepXZ_IMPL_name}

# drn_CERCLEXZ class attributes and methods
drn_CERCLEXZ_rayonCST: Property = Property(name="rayonCST", type=IntegerType)
drn_CERCLEXZ.attributes={drn_CERCLEXZ_rayonCST}

# DepXZ_IMPL class attributes and methods

# drn_CARREXZ class attributes and methods
drn_CARREXZ_coteCST: Property = Property(name="coteCST", type=IntegerType)
drn_CARREXZ.attributes={drn_CARREXZ_coteCST}

# drn_DepXYZ_IMPL class attributes and methods

# drn_Flip class attributes and methods
drn_Flip_name: Property = Property(name="name", type=StringType)
drn_Flip.attributes={drn_Flip_name}

# DepXYZ_IMPL class attributes and methods

# drn_Wait class attributes and methods
drn_Wait_name: Property = Property(name="name", type=StringType)
drn_Wait_tempsCST: Property = Property(name="tempsCST", type=IntegerType)
drn_Wait.attributes={drn_Wait_tempsCST, drn_Wait_name}

# drn_TakeOff class attributes and methods
drn_TakeOff_name: Property = Property(name="name", type=StringType)
drn_TakeOff.attributes={drn_TakeOff_name}

# drn_Land class attributes and methods
drn_Land_name: Property = Property(name="name", type=StringType)
drn_Land.attributes={drn_Land_name}

# drn_Declaration class attributes and methods
drn_Declaration_typePrimitif: Property = Property(name="typePrimitif", type=StringType)
drn_Declaration_name: Property = Property(name="name", type=StringType)
drn_Declaration.attributes={drn_Declaration_name, drn_Declaration_typePrimitif}

# drn_Definition class attributes and methods
drn_Definition_real: Property = Property(name="real", type=StringType)
drn_Definition_int: Property = Property(name="int", type=StringType)
drn_Definition_bool: Property = Property(name="bool", type=StringType)
drn_Definition_text: Property = Property(name="text", type=StringType)
drn_Definition.attributes={drn_Definition_bool, drn_Definition_text, drn_Definition_int, drn_Definition_real}

# drn_Element class attributes and methods
drn_Element_name: Property = Property(name="name", type=StringType)
drn_Element.attributes={drn_Element_name}

# drn_RefDevice class attributes and methods
drn_RefDevice_mode: Property = Property(name="mode", type=StringType)
drn_RefDevice.attributes={drn_RefDevice_mode}

# drn_Bluetooth class attributes and methods

# ConnectionType class attributes and methods

# drn_Wifi class attributes and methods

# Relationships
context3: BinaryAssociation = BinaryAssociation(
    name="context3",
    ends={
        Property(name="drn_Model4", type=drn_Context, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="drn_Context", type=drn_Model, multiplicity=Multiplicity(1, 1))
    }
)
config0: BinaryAssociation = BinaryAssociation(
    name="config0",
    ends={
        Property(name="drn_Configuration", type=drn_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_Model", type=drn_Configuration, multiplicity=Multiplicity(0, 1))
    }
)
move22: BinaryAssociation = BinaryAssociation(
    name="move22",
    ends={
        Property(name="drn_Movement", type=drn_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_Expression23", type=drn_Movement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
libraries1: BinaryAssociation = BinaryAssociation(
    name="libraries1",
    ends={
        Property(name="drn_Library", type=drn_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_Model2", type=drn_Library, multiplicity=Multiplicity(0, 9999))
    }
)
assignement5: BinaryAssociation = BinaryAssociation(
    name="assignement5",
    ends={
        Property(name="drn_Assignement", type=drn_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_Model6", type=drn_Assignement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
with_24: BinaryAssociation = BinaryAssociation(
    name="with_24",
    ends={
        Property(name="drn_With", type=drn_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_Expression25", type=drn_With, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
then27: BinaryAssociation = BinaryAssociation(
    name="then27",
    ends={
        Property(name="drn_Expression28", type=drn_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_Expression26", type=drn_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
main7: BinaryAssociation = BinaryAssociation(
    name="main7",
    ends={
        Property(name="drn_RefPart", type=drn_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_Model8", type=drn_RefPart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
types9: BinaryAssociation = BinaryAssociation(
    name="types9",
    ends={
        Property(name="drn_TypeGeneric", type=drn_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_Configuration10", type=drn_TypeGeneric, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
devices11: BinaryAssociation = BinaryAssociation(
    name="devices11",
    ends={
        Property(name="drn_Device", type=drn_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_Configuration12", type=drn_Device, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connection13: BinaryAssociation = BinaryAssociation(
    name="connection13",
    ends={
        Property(name="drn_ConnectionType", type=drn_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_Configuration14", type=drn_ConnectionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignement15: BinaryAssociation = BinaryAssociation(
    name="assignement15",
    ends={
        Property(name="drn_Assignement17", type=drn_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_Library16", type=drn_Assignement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
limit18: BinaryAssociation = BinaryAssociation(
    name="limit18",
    ends={
        Property(name="drn_Limit", type=drn_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_Context19", type=drn_Limit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operandes20: BinaryAssociation = BinaryAssociation(
    name="operandes20",
    ends={
        Property(name="drn_Expression", type=drn_Assignement, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_Assignement21", type=drn_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable_partie29: BinaryAssociation = BinaryAssociation(
    name="variable_partie29",
    ends={
        Property(name="drn_Assignement31", type=drn_RefPart, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_RefPart30", type=drn_Assignement, multiplicity=Multiplicity(0, 1))
    }
)
lib32: BinaryAssociation = BinaryAssociation(
    name="lib32",
    ends={
        Property(name="drn_Library33", type=drn_RefPartLib, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_RefPartLib", type=drn_Library, multiplicity=Multiplicity(0, 1))
    }
)
assignement34: BinaryAssociation = BinaryAssociation(
    name="assignement34",
    ends={
        Property(name="drn_Assignement36", type=drn_RefPartLib, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_RefPartLib35", type=drn_Assignement, multiplicity=Multiplicity(0, 1))
    }
)
rotate37: BinaryAssociation = BinaryAssociation(
    name="rotate37",
    ends={
        Property(name="drn_Rotate", type=drn_And, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_And", type=drn_Rotate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
depx38: BinaryAssociation = BinaryAssociation(
    name="depx38",
    ends={
        Property(name="drn_DepX_Impl", type=drn_And, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_And39", type=drn_DepX_Impl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
depy40: BinaryAssociation = BinaryAssociation(
    name="depy40",
    ends={
        Property(name="drn_DepY_Impl", type=drn_And, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_And41", type=drn_DepY_Impl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
depz42: BinaryAssociation = BinaryAssociation(
    name="depz42",
    ends={
        Property(name="drn_DepZ_Impl", type=drn_And, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_And43", type=drn_DepZ_Impl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declarations44: BinaryAssociation = BinaryAssociation(
    name="declarations44",
    ends={
        Property(name="drn_Declaration", type=drn_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_Device45", type=drn_Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type46: BinaryAssociation = BinaryAssociation(
    name="type46",
    ends={
        Property(name="drn_TypeGeneric48", type=drn_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_Declaration47", type=drn_TypeGeneric, multiplicity=Multiplicity(0, 1))
    }
)
left49: BinaryAssociation = BinaryAssociation(
    name="left49",
    ends={
        Property(name="drn_Declaration50", type=drn_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_Definition", type=drn_Declaration, multiplicity=Multiplicity(0, 1))
    }
)
right51: BinaryAssociation = BinaryAssociation(
    name="right51",
    ends={
        Property(name="drn_Element", type=drn_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_Definition52", type=drn_Element, multiplicity=Multiplicity(0, 1))
    }
)
option53: BinaryAssociation = BinaryAssociation(
    name="option53",
    ends={
        Property(name="drn_RefDevice", type=drn_With, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_With54", type=drn_RefDevice, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dev55: BinaryAssociation = BinaryAssociation(
    name="dev55",
    ends={
        Property(name="drn_Device57", type=drn_RefDevice, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_RefDevice56", type=drn_Device, multiplicity=Multiplicity(0, 1))
    }
)
definitions58: BinaryAssociation = BinaryAssociation(
    name="definitions58",
    ends={
        Property(name="drn_Definition60", type=drn_RefDevice, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_RefDevice59", type=drn_Definition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements61: BinaryAssociation = BinaryAssociation(
    name="elements61",
    ends={
        Property(name="drn_Element63", type=drn_TypeGeneric, multiplicity=Multiplicity(1, 1)),
        Property(name="drn_TypeGeneric62", type=drn_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_drn_Model_Root = Generalization(general=Root, specific=drn_Model)
gen_drn_Configuration_Root = Generalization(general=Root, specific=drn_Configuration)
gen_drn_Library_Root = Generalization(general=Root, specific=drn_Library)
gen_drn_Surface_Limit = Generalization(general=Limit, specific=drn_Surface)
gen_drn_InitialPosition_Limit = Generalization(general=Limit, specific=drn_InitialPosition)
gen_drn_InitialDirection_InitialPosition = Generalization(general=InitialPosition, specific=drn_InitialDirection)
gen_drn_InitialPositionX_InitialPosition = Generalization(general=InitialPosition, specific=drn_InitialPositionX)
gen_drn_InitialPositionY_InitialPosition = Generalization(general=InitialPosition, specific=drn_InitialPositionY)
gen_drn_MaxLength_Surface = Generalization(general=Surface, specific=drn_MaxLength)
gen_drn_MaxWidth_Surface = Generalization(general=Surface, specific=drn_MaxWidth)
gen_drn_MaxSpeed_Limit = Generalization(general=Limit, specific=drn_MaxSpeed)
gen_drn_MaxHeight_Surface = Generalization(general=Surface, specific=drn_MaxHeight)
gen_drn_RefPart_Movement = Generalization(general=Movement, specific=drn_RefPart)
gen_drn_RefPartLib_Movement = Generalization(general=Movement, specific=drn_RefPartLib)
gen_drn_And_Movement = Generalization(general=Movement, specific=drn_And)
gen_drn_DepY_Impl_Movement = Generalization(general=Movement, specific=drn_DepY_Impl)
gen_drn_FORWARD_DepY_Impl = Generalization(general=DepY_Impl, specific=drn_FORWARD)
gen_drn_BACKWARD_DepY_Impl = Generalization(general=DepY_Impl, specific=drn_BACKWARD)
gen_drn_DepX_Impl_Movement = Generalization(general=Movement, specific=drn_DepX_Impl)
gen_drn_LEFT_DepX_Impl = Generalization(general=DepX_Impl, specific=drn_LEFT)
gen_drn_RIGHT_DepX_Impl = Generalization(general=DepX_Impl, specific=drn_RIGHT)
gen_drn_UP_DepZ_Impl = Generalization(general=DepZ_Impl, specific=drn_UP)
gen_drn_DepZ_Impl_Movement = Generalization(general=Movement, specific=drn_DepZ_Impl)
gen_drn_DOWN_DepZ_Impl = Generalization(general=DepZ_Impl, specific=drn_DOWN)
gen_drn_DepXY_IMPL_Movement = Generalization(general=Movement, specific=drn_DepXY_IMPL)
gen_drn_CERCLEXY_DepXY_IMPL = Generalization(general=DepXY_IMPL, specific=drn_CERCLEXY)
gen_drn_CARREXY_DepXY_IMPL = Generalization(general=DepXY_IMPL, specific=drn_CARREXY)
gen_drn_DepYZ_IMPL_Movement = Generalization(general=Movement, specific=drn_DepYZ_IMPL)
gen_drn_CERCLEYZ_DepYZ_IMPL = Generalization(general=DepYZ_IMPL, specific=drn_CERCLEYZ)
gen_drn_CARREYZ_DepYZ_IMPL = Generalization(general=DepYZ_IMPL, specific=drn_CARREYZ)
gen_drn_DepXZ_IMPL_Movement = Generalization(general=Movement, specific=drn_DepXZ_IMPL)
gen_drn_CERCLEXZ_DepXZ_IMPL = Generalization(general=DepXZ_IMPL, specific=drn_CERCLEXZ)
gen_drn_CARREXZ_DepXZ_IMPL = Generalization(general=DepXZ_IMPL, specific=drn_CARREXZ)
gen_drn_DepXYZ_IMPL_Movement = Generalization(general=Movement, specific=drn_DepXYZ_IMPL)
gen_drn_Flip_DepXYZ_IMPL = Generalization(general=DepXYZ_IMPL, specific=drn_Flip)
gen_drn_Rotate_Movement = Generalization(general=Movement, specific=drn_Rotate)
gen_drn_Wait_Movement = Generalization(general=Movement, specific=drn_Wait)
gen_drn_TakeOff_Movement = Generalization(general=Movement, specific=drn_TakeOff)
gen_drn_Land_Movement = Generalization(general=Movement, specific=drn_Land)
gen_drn_Bluetooth_ConnectionType = Generalization(general=ConnectionType, specific=drn_Bluetooth)
gen_drn_Wifi_ConnectionType = Generalization(general=ConnectionType, specific=drn_Wifi)

# Domain Model
domain_model = DomainModel(
    name="drn",
    types={drn_Root, drn_Model, Root, drn_Configuration, drn_Library, drn_Assignement, drn_With, drn_Context, drn_RefPart, drn_TypeGeneric, drn_Device, drn_ConnectionType, drn_Limit, drn_Surface, Limit, drn_InitialPosition, drn_InitialDirection, InitialPosition, drn_InitialPositionX, drn_InitialPositionY, drn_MaxLength, Surface, drn_MaxWidth, drn_MaxSpeed, drn_MaxHeight, drn_Expression, drn_Movement, Movement, drn_RefPartLib, drn_And, drn_Rotate, drn_DepX_Impl, drn_DepY_Impl, drn_DepZ_Impl, drn_FORWARD, DepY_Impl, drn_BACKWARD, drn_LEFT, DepX_Impl, drn_UP, drn_RIGHT, DepZ_Impl, drn_DOWN, drn_DepXY_IMPL, drn_CERCLEXY, DepXY_IMPL, drn_CARREXY, drn_DepYZ_IMPL, drn_CERCLEYZ, DepYZ_IMPL, drn_CARREYZ, drn_DepXZ_IMPL, drn_CERCLEXZ, DepXZ_IMPL, drn_CARREXZ, drn_DepXYZ_IMPL, drn_Flip, DepXYZ_IMPL, drn_Wait, drn_TakeOff, drn_Land, drn_Declaration, drn_Definition, drn_Element, drn_RefDevice, drn_Bluetooth, ConnectionType, drn_Wifi, TypePrimitif, Mode, EBool, DirectionType, Where},
    associations={context3, config0, move22, libraries1, assignement5, with_24, then27, main7, types9, devices11, connection13, assignement15, limit18, operandes20, variable_partie29, lib32, assignement34, rotate37, depx38, depy40, depz42, declarations44, type46, left49, right51, option53, dev55, definitions58, elements61},
    generalizations={gen_drn_Model_Root, gen_drn_Configuration_Root, gen_drn_Library_Root, gen_drn_Surface_Limit, gen_drn_InitialPosition_Limit, gen_drn_InitialDirection_InitialPosition, gen_drn_InitialPositionX_InitialPosition, gen_drn_InitialPositionY_InitialPosition, gen_drn_MaxLength_Surface, gen_drn_MaxWidth_Surface, gen_drn_MaxSpeed_Limit, gen_drn_MaxHeight_Surface, gen_drn_RefPart_Movement, gen_drn_RefPartLib_Movement, gen_drn_And_Movement, gen_drn_DepY_Impl_Movement, gen_drn_FORWARD_DepY_Impl, gen_drn_BACKWARD_DepY_Impl, gen_drn_DepX_Impl_Movement, gen_drn_LEFT_DepX_Impl, gen_drn_RIGHT_DepX_Impl, gen_drn_UP_DepZ_Impl, gen_drn_DepZ_Impl_Movement, gen_drn_DOWN_DepZ_Impl, gen_drn_DepXY_IMPL_Movement, gen_drn_CERCLEXY_DepXY_IMPL, gen_drn_CARREXY_DepXY_IMPL, gen_drn_DepYZ_IMPL_Movement, gen_drn_CERCLEYZ_DepYZ_IMPL, gen_drn_CARREYZ_DepYZ_IMPL, gen_drn_DepXZ_IMPL_Movement, gen_drn_CERCLEXZ_DepXZ_IMPL, gen_drn_CARREXZ_DepXZ_IMPL, gen_drn_DepXYZ_IMPL_Movement, gen_drn_Flip_DepXYZ_IMPL, gen_drn_Rotate_Movement, gen_drn_Wait_Movement, gen_drn_TakeOff_Movement, gen_drn_Land_Movement, gen_drn_Bluetooth_ConnectionType, gen_drn_Wifi_ConnectionType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)