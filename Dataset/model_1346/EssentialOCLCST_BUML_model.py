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
essentialOCLCST_ArrowCallArgumentsCS = Class(name="essentialOCLCST_ArrowCallArgumentsCS")
CallArgumentsCS = Class(name="CallArgumentsCS")
essentialOCLCST_VariableCS = Class(name="essentialOCLCST_VariableCS")
essentialOCLCST_OclExpressionCS = Class(name="essentialOCLCST_OclExpressionCS")
essentialOCLCST_BinaryExpressionCS = Class(name="essentialOCLCST_BinaryExpressionCS")
essentialOCLCST_CallExpCS = Class(name="essentialOCLCST_CallExpCS")
essentialOCLCST_CollectionLiteralExpCS = Class(name="essentialOCLCST_CollectionLiteralExpCS")
LiteralExpCS = Class(name="LiteralExpCS")
essentialOCLCST_CollectionLiteralPartCS = Class(name="essentialOCLCST_CollectionLiteralPartCS")
essentialOCLCST_CollectionTypeCS = Class(name="essentialOCLCST_CollectionTypeCS")
TypeCS = Class(name="TypeCS")
CollectionLiteralExpCS = Class(name="CollectionLiteralExpCS")
TypeLiteralExpCS = Class(name="TypeLiteralExpCS")
essentialOCLCST_SimpleNameCS = Class(name="essentialOCLCST_SimpleNameCS")
essentialOCLCST_TypeCS = Class(name="essentialOCLCST_TypeCS")
essentialOCLCST_DotIndexArgumentsCS = Class(name="essentialOCLCST_DotIndexArgumentsCS")
essentialOCLCST_IfExpCS = Class(name="essentialOCLCST_IfExpCS")
essentialOCLCST_IntegerLiteralExpCS = Class(name="essentialOCLCST_IntegerLiteralExpCS")
essentialOCLCST_InvalidLiteralExpCS = Class(name="essentialOCLCST_InvalidLiteralExpCS")
essentialOCLCST_LetExpCS = Class(name="essentialOCLCST_LetExpCS")
OclExpressionCS = Class(name="OclExpressionCS")
essentialOCLCST_BooleanLiteralExpCS = Class(name="essentialOCLCST_BooleanLiteralExpCS")
PrimitiveLiteralExpCS = Class(name="PrimitiveLiteralExpCS")
essentialOCLCST_CallArgumentsCS = Class(name="essentialOCLCST_CallArgumentsCS")
essentialOCLCST_PathNameCS = Class(name="essentialOCLCST_PathNameCS")
essentialOCLCST_PrimitiveLiteralExpCS = Class(name="essentialOCLCST_PrimitiveLiteralExpCS")
essentialOCLCST_RealLiteralExpCS = Class(name="essentialOCLCST_RealLiteralExpCS")
VariableExpCS = Class(name="VariableExpCS")
essentialOCLCST_StringLiteralExpCS = Class(name="essentialOCLCST_StringLiteralExpCS")
essentialOCLCST_TupleLiteralExpCS = Class(name="essentialOCLCST_TupleLiteralExpCS")
essentialOCLCST_TupleTypeCS = Class(name="essentialOCLCST_TupleTypeCS")
essentialOCLCST_TypeLiteralExpCS = Class(name="essentialOCLCST_TypeLiteralExpCS")
essentialOCLCST_UnaryExpressionCS = Class(name="essentialOCLCST_UnaryExpressionCS")
essentialOCLCST_UnlimitedNaturalLiteralExpCS = Class(name="essentialOCLCST_UnlimitedNaturalLiteralExpCS")
essentialOCLCST_VariableExpCS = Class(name="essentialOCLCST_VariableExpCS")
essentialOCLCST_LiteralExpCS = Class(name="essentialOCLCST_LiteralExpCS")
essentialOCLCST_NullLiteralExpCS = Class(name="essentialOCLCST_NullLiteralExpCS")

# essentialOCLCST_ArrowCallArgumentsCS class attributes and methods

# CallArgumentsCS class attributes and methods

# essentialOCLCST_VariableCS class attributes and methods

# essentialOCLCST_OclExpressionCS class attributes and methods

# essentialOCLCST_BinaryExpressionCS class attributes and methods
essentialOCLCST_BinaryExpressionCS_op: Property = Property(name="op", type=StringType)
essentialOCLCST_BinaryExpressionCS.attributes={essentialOCLCST_BinaryExpressionCS_op}

# essentialOCLCST_CallExpCS class attributes and methods

# essentialOCLCST_CollectionLiteralExpCS class attributes and methods

# LiteralExpCS class attributes and methods

# essentialOCLCST_CollectionLiteralPartCS class attributes and methods

# essentialOCLCST_CollectionTypeCS class attributes and methods

# TypeCS class attributes and methods

# CollectionLiteralExpCS class attributes and methods

# TypeLiteralExpCS class attributes and methods

# essentialOCLCST_SimpleNameCS class attributes and methods
essentialOCLCST_SimpleNameCS_value: Property = Property(name="value", type=StringType)
essentialOCLCST_SimpleNameCS.attributes={essentialOCLCST_SimpleNameCS_value}

# essentialOCLCST_TypeCS class attributes and methods

# essentialOCLCST_DotIndexArgumentsCS class attributes and methods
essentialOCLCST_DotIndexArgumentsCS_isPre: Property = Property(name="isPre", type=BooleanType)
essentialOCLCST_DotIndexArgumentsCS.attributes={essentialOCLCST_DotIndexArgumentsCS_isPre}

# essentialOCLCST_IfExpCS class attributes and methods

# essentialOCLCST_IntegerLiteralExpCS class attributes and methods
essentialOCLCST_IntegerLiteralExpCS_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
essentialOCLCST_IntegerLiteralExpCS.attributes={essentialOCLCST_IntegerLiteralExpCS_integerSymbol}

# essentialOCLCST_InvalidLiteralExpCS class attributes and methods

# essentialOCLCST_LetExpCS class attributes and methods

# OclExpressionCS class attributes and methods

# essentialOCLCST_BooleanLiteralExpCS class attributes and methods
essentialOCLCST_BooleanLiteralExpCS_value: Property = Property(name="value", type=StringType)
essentialOCLCST_BooleanLiteralExpCS.attributes={essentialOCLCST_BooleanLiteralExpCS_value}

# PrimitiveLiteralExpCS class attributes and methods

# essentialOCLCST_CallArgumentsCS class attributes and methods

# essentialOCLCST_PathNameCS class attributes and methods

# essentialOCLCST_PrimitiveLiteralExpCS class attributes and methods

# essentialOCLCST_RealLiteralExpCS class attributes and methods
essentialOCLCST_RealLiteralExpCS_realSymbol: Property = Property(name="realSymbol", type=StringType)
essentialOCLCST_RealLiteralExpCS.attributes={essentialOCLCST_RealLiteralExpCS_realSymbol}

# VariableExpCS class attributes and methods

# essentialOCLCST_StringLiteralExpCS class attributes and methods
essentialOCLCST_StringLiteralExpCS_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
essentialOCLCST_StringLiteralExpCS.attributes={essentialOCLCST_StringLiteralExpCS_stringSymbol}

# essentialOCLCST_TupleLiteralExpCS class attributes and methods

# essentialOCLCST_TupleTypeCS class attributes and methods
essentialOCLCST_TupleTypeCS_value: Property = Property(name="value", type=StringType)
essentialOCLCST_TupleTypeCS.attributes={essentialOCLCST_TupleTypeCS_value}

# essentialOCLCST_TypeLiteralExpCS class attributes and methods

# essentialOCLCST_UnaryExpressionCS class attributes and methods
essentialOCLCST_UnaryExpressionCS_op: Property = Property(name="op", type=StringType)
essentialOCLCST_UnaryExpressionCS.attributes={essentialOCLCST_UnaryExpressionCS_op}

# essentialOCLCST_UnlimitedNaturalLiteralExpCS class attributes and methods

# essentialOCLCST_VariableExpCS class attributes and methods

# essentialOCLCST_LiteralExpCS class attributes and methods

# essentialOCLCST_NullLiteralExpCS class attributes and methods

# Relationships
variable10: BinaryAssociation = BinaryAssociation(
    name="variable10",
    ends={
        Property(name="essentialOCLCST_VariableCS", type=essentialOCLCST_ArrowCallArgumentsCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialOCLCST_ArrowCallArgumentsCS", type=essentialOCLCST_VariableCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable21: BinaryAssociation = BinaryAssociation(
    name="variable21",
    ends={
        Property(name="essentialOCLCST_VariableCS3", type=essentialOCLCST_ArrowCallArgumentsCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialOCLCST_ArrowCallArgumentsCS2", type=essentialOCLCST_VariableCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body4: BinaryAssociation = BinaryAssociation(
    name="body4",
    ends={
        Property(name="essentialOCLCST_OclExpressionCS", type=essentialOCLCST_ArrowCallArgumentsCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialOCLCST_ArrowCallArgumentsCS5", type=essentialOCLCST_OclExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source15: BinaryAssociation = BinaryAssociation(
    name="source15",
    ends={
        Property(name="essentialOCLCST_OclExpressionCS16", type=essentialOCLCST_CallExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialOCLCST_CallExpCS", type=essentialOCLCST_OclExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
callArguments17: BinaryAssociation = BinaryAssociation(
    name="callArguments17",
    ends={
        Property(name="essentialOCLCST_CallArgumentsCS19", type=essentialOCLCST_CallExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialOCLCST_CallExpCS18", type=essentialOCLCST_CallArgumentsCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressionCS20: BinaryAssociation = BinaryAssociation(
    name="expressionCS20",
    ends={
        Property(name="essentialOCLCST_OclExpressionCS21", type=essentialOCLCST_CollectionLiteralPartCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialOCLCST_CollectionLiteralPartCS", type=essentialOCLCST_OclExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lastExpressionCS22: BinaryAssociation = BinaryAssociation(
    name="lastExpressionCS22",
    ends={
        Property(name="essentialOCLCST_OclExpressionCS24", type=essentialOCLCST_CollectionLiteralPartCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialOCLCST_CollectionLiteralPartCS23", type=essentialOCLCST_OclExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value25: BinaryAssociation = BinaryAssociation(
    name="value25",
    ends={
        Property(name="essentialOCLCST_SimpleNameCS", type=essentialOCLCST_CollectionTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialOCLCST_CollectionTypeCS", type=essentialOCLCST_SimpleNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeCS26: BinaryAssociation = BinaryAssociation(
    name="typeCS26",
    ends={
        Property(name="essentialOCLCST_TypeCS", type=essentialOCLCST_CollectionTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialOCLCST_CollectionTypeCS27", type=essentialOCLCST_TypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
collectionLiteralParts28: BinaryAssociation = BinaryAssociation(
    name="collectionLiteralParts28",
    ends={
        Property(name="essentialOCLCST_CollectionLiteralPartCS30", type=essentialOCLCST_CollectionTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialOCLCST_CollectionTypeCS29", type=essentialOCLCST_CollectionLiteralPartCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
indexes31: BinaryAssociation = BinaryAssociation(
    name="indexes31",
    ends={
        Property(name="essentialOCLCST_OclExpressionCS32", type=essentialOCLCST_DotIndexArgumentsCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialOCLCST_DotIndexArgumentsCS", type=essentialOCLCST_OclExpressionCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition33: BinaryAssociation = BinaryAssociation(
    name="condition33",
    ends={
        Property(name="essentialOCLCST_OclExpressionCS34", type=essentialOCLCST_IfExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialOCLCST_IfExpCS", type=essentialOCLCST_OclExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenExpression35: BinaryAssociation = BinaryAssociation(
    name="thenExpression35",
    ends={
        Property(name="essentialOCLCST_OclExpressionCS37", type=essentialOCLCST_IfExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialOCLCST_IfExpCS36", type=essentialOCLCST_OclExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseExpression38: BinaryAssociation = BinaryAssociation(
    name="elseExpression38",
    ends={
        Property(name="essentialOCLCST_OclExpressionCS40", type=essentialOCLCST_IfExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialOCLCST_IfExpCS39", type=essentialOCLCST_OclExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left6: BinaryAssociation = BinaryAssociation(
    name="left6",
    ends={
        Property(name="essentialOCLCST_OclExpressionCS7", type=essentialOCLCST_BinaryExpressionCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialOCLCST_BinaryExpressionCS", type=essentialOCLCST_OclExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right8: BinaryAssociation = BinaryAssociation(
    name="right8",
    ends={
        Property(name="essentialOCLCST_OclExpressionCS10", type=essentialOCLCST_BinaryExpressionCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialOCLCST_BinaryExpressionCS9", type=essentialOCLCST_OclExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pathName11: BinaryAssociation = BinaryAssociation(
    name="pathName11",
    ends={
        Property(name="essentialOCLCST_PathNameCS", type=essentialOCLCST_CallArgumentsCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialOCLCST_CallArgumentsCS", type=essentialOCLCST_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments12: BinaryAssociation = BinaryAssociation(
    name="arguments12",
    ends={
        Property(name="essentialOCLCST_OclExpressionCS14", type=essentialOCLCST_CallArgumentsCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialOCLCST_CallArgumentsCS13", type=essentialOCLCST_OclExpressionCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collectionLiteralParts49: BinaryAssociation = BinaryAssociation(
    name="collectionLiteralParts49",
    ends={
        Property(name="essentialOCLCST_CollectionLiteralPartCS51", type=essentialOCLCST_SimpleNameCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialOCLCST_SimpleNameCS50", type=essentialOCLCST_CollectionLiteralPartCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
part52: BinaryAssociation = BinaryAssociation(
    name="part52",
    ends={
        Property(name="essentialOCLCST_VariableCS53", type=essentialOCLCST_TupleLiteralExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialOCLCST_TupleLiteralExpCS", type=essentialOCLCST_VariableCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
part54: BinaryAssociation = BinaryAssociation(
    name="part54",
    ends={
        Property(name="essentialOCLCST_VariableCS55", type=essentialOCLCST_TupleTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialOCLCST_TupleTypeCS", type=essentialOCLCST_VariableCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source56: BinaryAssociation = BinaryAssociation(
    name="source56",
    ends={
        Property(name="essentialOCLCST_OclExpressionCS57", type=essentialOCLCST_UnaryExpressionCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialOCLCST_UnaryExpressionCS", type=essentialOCLCST_OclExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name58: BinaryAssociation = BinaryAssociation(
    name="name58",
    ends={
        Property(name="essentialOCLCST_SimpleNameCS60", type=essentialOCLCST_VariableCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialOCLCST_VariableCS59", type=essentialOCLCST_SimpleNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type61: BinaryAssociation = BinaryAssociation(
    name="type61",
    ends={
        Property(name="essentialOCLCST_TypeCS63", type=essentialOCLCST_VariableCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialOCLCST_VariableCS62", type=essentialOCLCST_TypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initExpression64: BinaryAssociation = BinaryAssociation(
    name="initExpression64",
    ends={
        Property(name="essentialOCLCST_OclExpressionCS66", type=essentialOCLCST_VariableCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialOCLCST_VariableCS65", type=essentialOCLCST_OclExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable41: BinaryAssociation = BinaryAssociation(
    name="variable41",
    ends={
        Property(name="essentialOCLCST_VariableCS42", type=essentialOCLCST_LetExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialOCLCST_LetExpCS", type=essentialOCLCST_VariableCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
in_43: BinaryAssociation = BinaryAssociation(
    name="in_43",
    ends={
        Property(name="essentialOCLCST_OclExpressionCS45", type=essentialOCLCST_LetExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialOCLCST_LetExpCS44", type=essentialOCLCST_OclExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleNames46: BinaryAssociation = BinaryAssociation(
    name="simpleNames46",
    ends={
        Property(name="essentialOCLCST_SimpleNameCS48", type=essentialOCLCST_PathNameCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialOCLCST_PathNameCS47", type=essentialOCLCST_SimpleNameCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_essentialOCLCST_ArrowCallArgumentsCS_CallArgumentsCS = Generalization(general=CallArgumentsCS, specific=essentialOCLCST_ArrowCallArgumentsCS)
gen_essentialOCLCST_CallExpCS_OclExpressionCS = Generalization(general=OclExpressionCS, specific=essentialOCLCST_CallExpCS)
gen_essentialOCLCST_CollectionLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=essentialOCLCST_CollectionLiteralExpCS)
gen_essentialOCLCST_CollectionTypeCS_TypeCS = Generalization(general=TypeCS, specific=essentialOCLCST_CollectionTypeCS)
gen_essentialOCLCST_CollectionTypeCS_CollectionLiteralExpCS = Generalization(general=CollectionLiteralExpCS, specific=essentialOCLCST_CollectionTypeCS)
gen_essentialOCLCST_CollectionTypeCS_TypeLiteralExpCS = Generalization(general=TypeLiteralExpCS, specific=essentialOCLCST_CollectionTypeCS)
gen_essentialOCLCST_DotIndexArgumentsCS_CallArgumentsCS = Generalization(general=CallArgumentsCS, specific=essentialOCLCST_DotIndexArgumentsCS)
gen_essentialOCLCST_IfExpCS_OclExpressionCS = Generalization(general=OclExpressionCS, specific=essentialOCLCST_IfExpCS)
gen_essentialOCLCST_IntegerLiteralExpCS_PrimitiveLiteralExpCS = Generalization(general=PrimitiveLiteralExpCS, specific=essentialOCLCST_IntegerLiteralExpCS)
gen_essentialOCLCST_InvalidLiteralExpCS_PrimitiveLiteralExpCS = Generalization(general=PrimitiveLiteralExpCS, specific=essentialOCLCST_InvalidLiteralExpCS)
gen_essentialOCLCST_LetExpCS_OclExpressionCS = Generalization(general=OclExpressionCS, specific=essentialOCLCST_LetExpCS)
gen_essentialOCLCST_BinaryExpressionCS_OclExpressionCS = Generalization(general=OclExpressionCS, specific=essentialOCLCST_BinaryExpressionCS)
gen_essentialOCLCST_BooleanLiteralExpCS_PrimitiveLiteralExpCS = Generalization(general=PrimitiveLiteralExpCS, specific=essentialOCLCST_BooleanLiteralExpCS)
gen_essentialOCLCST_PrimitiveLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=essentialOCLCST_PrimitiveLiteralExpCS)
gen_essentialOCLCST_RealLiteralExpCS_PrimitiveLiteralExpCS = Generalization(general=PrimitiveLiteralExpCS, specific=essentialOCLCST_RealLiteralExpCS)
gen_essentialOCLCST_SimpleNameCS_TypeCS = Generalization(general=TypeCS, specific=essentialOCLCST_SimpleNameCS)
gen_essentialOCLCST_SimpleNameCS_CollectionLiteralExpCS = Generalization(general=CollectionLiteralExpCS, specific=essentialOCLCST_SimpleNameCS)
gen_essentialOCLCST_SimpleNameCS_TypeLiteralExpCS = Generalization(general=TypeLiteralExpCS, specific=essentialOCLCST_SimpleNameCS)
gen_essentialOCLCST_SimpleNameCS_VariableExpCS = Generalization(general=VariableExpCS, specific=essentialOCLCST_SimpleNameCS)
gen_essentialOCLCST_StringLiteralExpCS_PrimitiveLiteralExpCS = Generalization(general=PrimitiveLiteralExpCS, specific=essentialOCLCST_StringLiteralExpCS)
gen_essentialOCLCST_TupleLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=essentialOCLCST_TupleLiteralExpCS)
gen_essentialOCLCST_TupleTypeCS_TypeCS = Generalization(general=TypeCS, specific=essentialOCLCST_TupleTypeCS)
gen_essentialOCLCST_TupleTypeCS_TypeLiteralExpCS = Generalization(general=TypeLiteralExpCS, specific=essentialOCLCST_TupleTypeCS)
gen_essentialOCLCST_TypeLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=essentialOCLCST_TypeLiteralExpCS)
gen_essentialOCLCST_UnaryExpressionCS_OclExpressionCS = Generalization(general=OclExpressionCS, specific=essentialOCLCST_UnaryExpressionCS)
gen_essentialOCLCST_UnlimitedNaturalLiteralExpCS_PrimitiveLiteralExpCS = Generalization(general=PrimitiveLiteralExpCS, specific=essentialOCLCST_UnlimitedNaturalLiteralExpCS)
gen_essentialOCLCST_VariableExpCS_OclExpressionCS = Generalization(general=OclExpressionCS, specific=essentialOCLCST_VariableExpCS)
gen_essentialOCLCST_LiteralExpCS_OclExpressionCS = Generalization(general=OclExpressionCS, specific=essentialOCLCST_LiteralExpCS)
gen_essentialOCLCST_NullLiteralExpCS_PrimitiveLiteralExpCS = Generalization(general=PrimitiveLiteralExpCS, specific=essentialOCLCST_NullLiteralExpCS)
gen_essentialOCLCST_PathNameCS_TypeCS = Generalization(general=TypeCS, specific=essentialOCLCST_PathNameCS)
gen_essentialOCLCST_PathNameCS_TypeLiteralExpCS = Generalization(general=TypeLiteralExpCS, specific=essentialOCLCST_PathNameCS)

# Domain Model
domain_model = DomainModel(
    name="essentialOCLCST",
    types={essentialOCLCST_ArrowCallArgumentsCS, CallArgumentsCS, essentialOCLCST_VariableCS, essentialOCLCST_OclExpressionCS, essentialOCLCST_BinaryExpressionCS, essentialOCLCST_CallExpCS, essentialOCLCST_CollectionLiteralExpCS, LiteralExpCS, essentialOCLCST_CollectionLiteralPartCS, essentialOCLCST_CollectionTypeCS, TypeCS, CollectionLiteralExpCS, TypeLiteralExpCS, essentialOCLCST_SimpleNameCS, essentialOCLCST_TypeCS, essentialOCLCST_DotIndexArgumentsCS, essentialOCLCST_IfExpCS, essentialOCLCST_IntegerLiteralExpCS, essentialOCLCST_InvalidLiteralExpCS, essentialOCLCST_LetExpCS, OclExpressionCS, essentialOCLCST_BooleanLiteralExpCS, PrimitiveLiteralExpCS, essentialOCLCST_CallArgumentsCS, essentialOCLCST_PathNameCS, essentialOCLCST_PrimitiveLiteralExpCS, essentialOCLCST_RealLiteralExpCS, VariableExpCS, essentialOCLCST_StringLiteralExpCS, essentialOCLCST_TupleLiteralExpCS, essentialOCLCST_TupleTypeCS, essentialOCLCST_TypeLiteralExpCS, essentialOCLCST_UnaryExpressionCS, essentialOCLCST_UnlimitedNaturalLiteralExpCS, essentialOCLCST_VariableExpCS, essentialOCLCST_LiteralExpCS, essentialOCLCST_NullLiteralExpCS},
    associations={variable10, variable21, body4, source15, callArguments17, expressionCS20, lastExpressionCS22, value25, typeCS26, collectionLiteralParts28, indexes31, condition33, thenExpression35, elseExpression38, left6, right8, pathName11, arguments12, collectionLiteralParts49, part52, part54, source56, name58, type61, initExpression64, variable41, in_43, simpleNames46},
    generalizations={gen_essentialOCLCST_ArrowCallArgumentsCS_CallArgumentsCS, gen_essentialOCLCST_CallExpCS_OclExpressionCS, gen_essentialOCLCST_CollectionLiteralExpCS_LiteralExpCS, gen_essentialOCLCST_CollectionTypeCS_TypeCS, gen_essentialOCLCST_CollectionTypeCS_CollectionLiteralExpCS, gen_essentialOCLCST_CollectionTypeCS_TypeLiteralExpCS, gen_essentialOCLCST_DotIndexArgumentsCS_CallArgumentsCS, gen_essentialOCLCST_IfExpCS_OclExpressionCS, gen_essentialOCLCST_IntegerLiteralExpCS_PrimitiveLiteralExpCS, gen_essentialOCLCST_InvalidLiteralExpCS_PrimitiveLiteralExpCS, gen_essentialOCLCST_LetExpCS_OclExpressionCS, gen_essentialOCLCST_BinaryExpressionCS_OclExpressionCS, gen_essentialOCLCST_BooleanLiteralExpCS_PrimitiveLiteralExpCS, gen_essentialOCLCST_PrimitiveLiteralExpCS_LiteralExpCS, gen_essentialOCLCST_RealLiteralExpCS_PrimitiveLiteralExpCS, gen_essentialOCLCST_SimpleNameCS_TypeCS, gen_essentialOCLCST_SimpleNameCS_CollectionLiteralExpCS, gen_essentialOCLCST_SimpleNameCS_TypeLiteralExpCS, gen_essentialOCLCST_SimpleNameCS_VariableExpCS, gen_essentialOCLCST_StringLiteralExpCS_PrimitiveLiteralExpCS, gen_essentialOCLCST_TupleLiteralExpCS_LiteralExpCS, gen_essentialOCLCST_TupleTypeCS_TypeCS, gen_essentialOCLCST_TupleTypeCS_TypeLiteralExpCS, gen_essentialOCLCST_TypeLiteralExpCS_LiteralExpCS, gen_essentialOCLCST_UnaryExpressionCS_OclExpressionCS, gen_essentialOCLCST_UnlimitedNaturalLiteralExpCS_PrimitiveLiteralExpCS, gen_essentialOCLCST_VariableExpCS_OclExpressionCS, gen_essentialOCLCST_LiteralExpCS_OclExpressionCS, gen_essentialOCLCST_NullLiteralExpCS_PrimitiveLiteralExpCS, gen_essentialOCLCST_PathNameCS_TypeCS, gen_essentialOCLCST_PathNameCS_TypeLiteralExpCS},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)