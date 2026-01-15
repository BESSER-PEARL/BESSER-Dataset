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
DmxBaseType: Enumeration = Enumeration(
    name="DmxBaseType",
    literals={
            EnumerationLiteral(name="UNDEFINED"),
			EnumerationLiteral(name="AMBIGUOUS"),
			EnumerationLiteral(name="VOID"),
			EnumerationLiteral(name="BOOLEAN"),
			EnumerationLiteral(name="NUMBER"),
			EnumerationLiteral(name="TEXT"),
			EnumerationLiteral(name="IDENTIFIER"),
			EnumerationLiteral(name="TIMEPOINT"),
			EnumerationLiteral(name="ENUM"),
			EnumerationLiteral(name="STATE"),
			EnumerationLiteral(name="STATE_EVENT"),
			EnumerationLiteral(name="COMPLEX"),
			EnumerationLiteral(name="AGGREGATE"),
			EnumerationLiteral(name="NOTIFICATION"),
			EnumerationLiteral(name="SERVICE")
    }
)

DmxBinaryOperator: Enumeration = Enumeration(
    name="DmxBinaryOperator",
    literals={
            EnumerationLiteral(name="ADD"),
			EnumerationLiteral(name="SUBTRACT"),
			EnumerationLiteral(name="MULTIPLY"),
			EnumerationLiteral(name="DIVIDE"),
			EnumerationLiteral(name="POWER"),
			EnumerationLiteral(name="MODULO"),
			EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="XOR"),
			EnumerationLiteral(name="EQUAL"),
			EnumerationLiteral(name="NOT_EQUAL"),
			EnumerationLiteral(name="LESS"),
			EnumerationLiteral(name="LESS_OR_EQUAL"),
			EnumerationLiteral(name="GREATER_OR_EQUAL"),
			EnumerationLiteral(name="GREATER"),
			EnumerationLiteral(name="IN"),
			EnumerationLiteral(name="UNTIL"),
			EnumerationLiteral(name="SINGLE_ARROW"),
			EnumerationLiteral(name="DOUBLE_ARROW")
    }
)

DmxUnaryOperator: Enumeration = Enumeration(
    name="DmxUnaryOperator",
    literals={
            EnumerationLiteral(name="PLUS"),
			EnumerationLiteral(name="MINUS"),
			EnumerationLiteral(name="NOT")
    }
)

# Classes
dmx_DmxModel = Class(name="dmx::DmxModel")
DModel = Class(name="DModel")
ITypeContainer = Class(name="ITypeContainer")
dmx_DmxFilter = Class(name="dmx::DmxFilter")
dmx_DmxTest = Class(name="dmx::DmxTest")
INavigableMemberContainer = Class(name="INavigableMemberContainer")
dmx_DmxTestContext = Class(name="dmx::DmxTestContext")
dmx_DExpression = Class(name="dmx::DExpression")
DContext = Class(name="DContext")
dmx_DmxBaseTypeSet = Class(name="dmx::DmxBaseTypeSet")
dmx_DmxArchetype = Class(name="dmx::DmxArchetype")
DPrimitive = Class(name="DPrimitive")
DNavigableMember = Class(name="DNavigableMember")
dmx_DmxFilterParameter = Class(name="dmx::DmxFilterParameter")
dmx_DmxFilterTypeDescriptor = Class(name="dmx::DmxFilterTypeDescriptor")
dmx_DmxPredicateWithCorrelationVariable = Class(name="dmx::DmxPredicateWithCorrelationVariable")
dmx_DmxCorrelationVariable = Class(name="dmx::DmxCorrelationVariable")
dmx_DmxMemberNavigation = Class(name="dmx::DmxMemberNavigation")
dmx_DmxAssignment = Class(name="dmx::DmxAssignment")
DExpression = Class(name="DExpression")
dmx_DNavigableMember = Class(name="dmx::DNavigableMember")
dmx_DmxBinaryOperation = Class(name="dmx::DmxBinaryOperation")
dmx_DmxCallArguments = Class(name="dmx::DmxCallArguments")
dmx_DmxFunctionCall = Class(name="dmx::DmxFunctionCall")
dmx_DType = Class(name="dmx::DType")
dmx_DmxUnaryOperation = Class(name="dmx::DmxUnaryOperation")
dmx_DmxInstanceOfExpression = Class(name="dmx::DmxInstanceOfExpression")
dmx_DmxContextReference = Class(name="dmx::DmxContextReference")
dmx_DNamedElement = Class(name="dmx::DNamedElement")
dmx_DmxCastExpression = Class(name="dmx::DmxCastExpression")
dmx_DmxListExpression = Class(name="dmx::DmxListExpression")
dmx_DmxStaticReference = Class(name="dmx::DmxStaticReference")
dmx_IStaticReferenceTarget = Class(name="dmx::IStaticReferenceTarget")
dmx_DmxNaturalLiteral = Class(name="dmx::DmxNaturalLiteral")
dmx_DmxDecimalLiteral = Class(name="dmx::DmxDecimalLiteral")
dmx_DmxDateLiteral = Class(name="dmx::DmxDateLiteral")
dmx_DmxUrlLiteral = Class(name="dmx::DmxUrlLiteral")
dmx_DmxIfExpression = Class(name="dmx::DmxIfExpression")
dmx_DmxBooleanLiteral = Class(name="dmx::DmxBooleanLiteral")
dmx_DmxStringLiteral = Class(name="dmx::DmxStringLiteral")
dmx_DFeature = Class(name="dmx::DFeature")
dmx_DmxEntity = Class(name="dmx::DmxEntity")
DmxComplexObject = Class(name="DmxComplexObject")
dmx_DmxDetail = Class(name="dmx::DmxDetail")
dmx_DmxUndefinedLiteral = Class(name="dmx::DmxUndefinedLiteral")
dmx_DmxComplexObject = Class(name="dmx::DmxComplexObject")
dmx_DComplexType = Class(name="dmx::DComplexType")
dmx_DmxField = Class(name="dmx::DmxField")

# dmx_DmxModel class attributes and methods

# DModel class attributes and methods

# ITypeContainer class attributes and methods

# dmx_DmxFilter class attributes and methods

# dmx_DmxTest class attributes and methods
dmx_DmxTest_name: Property = Property(name="name", type=StringType)
dmx_DmxTest.attributes={dmx_DmxTest_name}

# INavigableMemberContainer class attributes and methods

# dmx_DmxTestContext class attributes and methods

# dmx_DExpression class attributes and methods

# DContext class attributes and methods

# dmx_DmxBaseTypeSet class attributes and methods
dmx_DmxBaseTypeSet_name: Property = Property(name="name", type=StringType)
dmx_DmxBaseTypeSet_members: Property = Property(name="members", type=StringType)
dmx_DmxBaseTypeSet.attributes={dmx_DmxBaseTypeSet_members, dmx_DmxBaseTypeSet_name}

# dmx_DmxArchetype class attributes and methods
dmx_DmxArchetype_baseType: Property = Property(name="baseType", type=StringType)
dmx_DmxArchetype.attributes={dmx_DmxArchetype_baseType}

# DPrimitive class attributes and methods

# DNavigableMember class attributes and methods

# dmx_DmxFilterParameter class attributes and methods
dmx_DmxFilterParameter_name: Property = Property(name="name", type=StringType)
dmx_DmxFilterParameter.attributes={dmx_DmxFilterParameter_name}

# dmx_DmxFilterTypeDescriptor class attributes and methods
dmx_DmxFilterTypeDescriptor_single: Property = Property(name="single", type=StringType)
dmx_DmxFilterTypeDescriptor_collection: Property = Property(name="collection", type=BooleanType)
dmx_DmxFilterTypeDescriptor_multiTyped: Property = Property(name="multiTyped", type=BooleanType)
dmx_DmxFilterTypeDescriptor_m_isCompatible: Method = Method(name="isCompatible", parameters={Parameter(name='type'), Parameter(name='collection')}, type=BooleanType)
dmx_DmxFilterTypeDescriptor_m_isCompatible: Method = Method(name="isCompatible", parameters={Parameter(name='type')}, type=BooleanType)
dmx_DmxFilterTypeDescriptor.attributes={dmx_DmxFilterTypeDescriptor_multiTyped, dmx_DmxFilterTypeDescriptor_single, dmx_DmxFilterTypeDescriptor_collection}
dmx_DmxFilterTypeDescriptor.methods={dmx_DmxFilterTypeDescriptor_m_isCompatible, dmx_DmxFilterTypeDescriptor_m_isCompatible}

# dmx_DmxPredicateWithCorrelationVariable class attributes and methods

# dmx_DmxCorrelationVariable class attributes and methods

# dmx_DmxMemberNavigation class attributes and methods
dmx_DmxMemberNavigation_explicitOperationCall: Property = Property(name="explicitOperationCall", type=BooleanType)
dmx_DmxMemberNavigation_before: Property = Property(name="before", type=BooleanType)
dmx_DmxMemberNavigation.attributes={dmx_DmxMemberNavigation_before, dmx_DmxMemberNavigation_explicitOperationCall}

# dmx_DmxAssignment class attributes and methods

# DExpression class attributes and methods

# dmx_DNavigableMember class attributes and methods

# dmx_DmxBinaryOperation class attributes and methods
dmx_DmxBinaryOperation_operator: Property = Property(name="operator", type=StringType)
dmx_DmxBinaryOperation.attributes={dmx_DmxBinaryOperation_operator}

# dmx_DmxCallArguments class attributes and methods

# dmx_DmxFunctionCall class attributes and methods

# dmx_DType class attributes and methods

# dmx_DmxUnaryOperation class attributes and methods
dmx_DmxUnaryOperation_operator: Property = Property(name="operator", type=StringType)
dmx_DmxUnaryOperation.attributes={dmx_DmxUnaryOperation_operator}

# dmx_DmxInstanceOfExpression class attributes and methods

# dmx_DmxContextReference class attributes and methods
dmx_DmxContextReference_all: Property = Property(name="all", type=BooleanType)
dmx_DmxContextReference_before: Property = Property(name="before", type=BooleanType)
dmx_DmxContextReference.attributes={dmx_DmxContextReference_all, dmx_DmxContextReference_before}

# dmx_DNamedElement class attributes and methods

# dmx_DmxCastExpression class attributes and methods

# dmx_DmxListExpression class attributes and methods

# dmx_DmxStaticReference class attributes and methods
dmx_DmxStaticReference_displayName: Property = Property(name="displayName", type=StringType)
dmx_DmxStaticReference_plural: Property = Property(name="plural", type=BooleanType)
dmx_DmxStaticReference.attributes={dmx_DmxStaticReference_displayName, dmx_DmxStaticReference_plural}

# dmx_IStaticReferenceTarget class attributes and methods

# dmx_DmxNaturalLiteral class attributes and methods
dmx_DmxNaturalLiteral_value: Property = Property(name="value", type=IntegerType)
dmx_DmxNaturalLiteral.attributes={dmx_DmxNaturalLiteral_value}

# dmx_DmxDecimalLiteral class attributes and methods
dmx_DmxDecimalLiteral_value: Property = Property(name="value", type=StringType)
dmx_DmxDecimalLiteral.attributes={dmx_DmxDecimalLiteral_value}

# dmx_DmxDateLiteral class attributes and methods
dmx_DmxDateLiteral_value: Property = Property(name="value", type=DateType)
dmx_DmxDateLiteral.attributes={dmx_DmxDateLiteral_value}

# dmx_DmxUrlLiteral class attributes and methods
dmx_DmxUrlLiteral_value: Property = Property(name="value", type=StringType)
dmx_DmxUrlLiteral_display: Property = Property(name="display", type=StringType)
dmx_DmxUrlLiteral.attributes={dmx_DmxUrlLiteral_value, dmx_DmxUrlLiteral_display}

# dmx_DmxIfExpression class attributes and methods

# dmx_DmxBooleanLiteral class attributes and methods
dmx_DmxBooleanLiteral_value: Property = Property(name="value", type=BooleanType)
dmx_DmxBooleanLiteral.attributes={dmx_DmxBooleanLiteral_value}

# dmx_DmxStringLiteral class attributes and methods
dmx_DmxStringLiteral_value: Property = Property(name="value", type=StringType)
dmx_DmxStringLiteral.attributes={dmx_DmxStringLiteral_value}

# dmx_DFeature class attributes and methods

# dmx_DmxEntity class attributes and methods

# DmxComplexObject class attributes and methods

# dmx_DmxDetail class attributes and methods

# dmx_DmxUndefinedLiteral class attributes and methods

# dmx_DmxComplexObject class attributes and methods

# dmx_DComplexType class attributes and methods

# dmx_DmxField class attributes and methods

# Relationships
filters0: BinaryAssociation = BinaryAssociation(
    name="filters0",
    ends={
        Property(name="dmx_DmxFilter", type=dmx_DmxModel, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxModel", type=dmx_DmxFilter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tests1: BinaryAssociation = BinaryAssociation(
    name="tests1",
    ends={
        Property(name="dmx_DmxTest", type=dmx_DmxModel, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxModel2", type=dmx_DmxTest, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
context3: BinaryAssociation = BinaryAssociation(
    name="context3",
    ends={
        Property(name="dmx_DmxTestContext", type=dmx_DmxTest, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxTest4", type=dmx_DmxTestContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr5: BinaryAssociation = BinaryAssociation(
    name="expr5",
    ends={
        Property(name="dmx_DExpression", type=dmx_DmxTest, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxTest6", type=dmx_DExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value7: BinaryAssociation = BinaryAssociation(
    name="value7",
    ends={
        Property(name="dmx_DExpression9", type=dmx_DmxTestContext, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxTestContext8", type=dmx_DExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
withTypeSet14: BinaryAssociation = BinaryAssociation(
    name="withTypeSet14",
    ends={
        Property(name="dmx_DmxBaseTypeSet", type=dmx_DmxFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxFilter15", type=dmx_DmxBaseTypeSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters10: BinaryAssociation = BinaryAssociation(
    name="parameters10",
    ends={
        Property(name="dmx_DmxFilterParameter", type=dmx_DmxFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxFilter11", type=dmx_DmxFilterParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeDesc12: BinaryAssociation = BinaryAssociation(
    name="typeDesc12",
    ends={
        Property(name="dmx_DmxFilterTypeDescriptor", type=dmx_DmxFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxFilter13", type=dmx_DmxFilterTypeDescriptor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
correlationVariable29: BinaryAssociation = BinaryAssociation(
    name="correlationVariable29",
    ends={
        Property(name="dmx_DmxCorrelationVariable", type=dmx_DmxPredicateWithCorrelationVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxPredicateWithCorrelationVariable", type=dmx_DmxCorrelationVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
predicate30: BinaryAssociation = BinaryAssociation(
    name="predicate30",
    ends={
        Property(name="dmx_DExpression32", type=dmx_DmxPredicateWithCorrelationVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxPredicateWithCorrelationVariable31", type=dmx_DExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multiple16: BinaryAssociation = BinaryAssociation(
    name="multiple16",
    ends={
        Property(name="dmx_DmxBaseTypeSet18", type=dmx_DmxFilterTypeDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxFilterTypeDescriptor17", type=dmx_DmxBaseTypeSet, multiplicity=Multiplicity(0, 1))
    }
)
typeDesc19: BinaryAssociation = BinaryAssociation(
    name="typeDesc19",
    ends={
        Property(name="dmx_DmxFilterTypeDescriptor21", type=dmx_DmxFilterParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxFilterParameter20", type=dmx_DmxFilterTypeDescriptor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
precedingNavigationSegment22: BinaryAssociation = BinaryAssociation(
    name="precedingNavigationSegment22",
    ends={
        Property(name="dmx_DExpression23", type=dmx_DmxAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxAssignment", type=dmx_DExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignToMember24: BinaryAssociation = BinaryAssociation(
    name="assignToMember24",
    ends={
        Property(name="dmx_DNavigableMember", type=dmx_DmxAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxAssignment25", type=dmx_DNavigableMember, multiplicity=Multiplicity(0, 1))
    }
)
value26: BinaryAssociation = BinaryAssociation(
    name="value26",
    ends={
        Property(name="dmx_DExpression28", type=dmx_DmxAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxAssignment27", type=dmx_DExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
callArguments45: BinaryAssociation = BinaryAssociation(
    name="callArguments45",
    ends={
        Property(name="dmx_DmxCallArguments47", type=dmx_DmxFunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxFunctionCall46", type=dmx_DmxCallArguments, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand48: BinaryAssociation = BinaryAssociation(
    name="leftOperand48",
    ends={
        Property(name="dmx_DExpression49", type=dmx_DmxBinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxBinaryOperation", type=dmx_DExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand50: BinaryAssociation = BinaryAssociation(
    name="rightOperand50",
    ends={
        Property(name="dmx_DExpression52", type=dmx_DmxBinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxBinaryOperation51", type=dmx_DExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
member33: BinaryAssociation = BinaryAssociation(
    name="member33",
    ends={
        Property(name="dmx_DNavigableMember34", type=dmx_DmxMemberNavigation, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxMemberNavigation", type=dmx_DNavigableMember, multiplicity=Multiplicity(0, 1))
    }
)
precedingNavigationSegment35: BinaryAssociation = BinaryAssociation(
    name="precedingNavigationSegment35",
    ends={
        Property(name="dmx_DExpression37", type=dmx_DmxMemberNavigation, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxMemberNavigation36", type=dmx_DExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
callArguments38: BinaryAssociation = BinaryAssociation(
    name="callArguments38",
    ends={
        Property(name="dmx_DmxCallArguments", type=dmx_DmxMemberNavigation, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxMemberNavigation39", type=dmx_DmxCallArguments, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments40: BinaryAssociation = BinaryAssociation(
    name="arguments40",
    ends={
        Property(name="dmx_DExpression42", type=dmx_DmxCallArguments, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxCallArguments41", type=dmx_DExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
function43: BinaryAssociation = BinaryAssociation(
    name="function43",
    ends={
        Property(name="dmx_DmxFilter44", type=dmx_DmxFunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxFunctionCall", type=dmx_DmxFilter, multiplicity=Multiplicity(0, 1))
    }
)
expression53: BinaryAssociation = BinaryAssociation(
    name="expression53",
    ends={
        Property(name="dmx_DExpression54", type=dmx_DmxInstanceOfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxInstanceOfExpression", type=dmx_DExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type55: BinaryAssociation = BinaryAssociation(
    name="type55",
    ends={
        Property(name="dmx_DType", type=dmx_DmxInstanceOfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxInstanceOfExpression56", type=dmx_DType, multiplicity=Multiplicity(0, 1))
    }
)
operand57: BinaryAssociation = BinaryAssociation(
    name="operand57",
    ends={
        Property(name="dmx_DExpression58", type=dmx_DmxUnaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxUnaryOperation", type=dmx_DExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
member67: BinaryAssociation = BinaryAssociation(
    name="member67",
    ends={
        Property(name="dmx_DNavigableMember69", type=dmx_DmxStaticReference, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxStaticReference68", type=dmx_DNavigableMember, multiplicity=Multiplicity(0, 1))
    }
)
target70: BinaryAssociation = BinaryAssociation(
    name="target70",
    ends={
        Property(name="dmx_DNamedElement", type=dmx_DmxContextReference, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxContextReference", type=dmx_DNamedElement, multiplicity=Multiplicity(0, 1))
    }
)
target59: BinaryAssociation = BinaryAssociation(
    name="target59",
    ends={
        Property(name="dmx_DExpression60", type=dmx_DmxCastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxCastExpression", type=dmx_DExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type61: BinaryAssociation = BinaryAssociation(
    name="type61",
    ends={
        Property(name="dmx_DType63", type=dmx_DmxCastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxCastExpression62", type=dmx_DType, multiplicity=Multiplicity(0, 1))
    }
)
elements64: BinaryAssociation = BinaryAssociation(
    name="elements64",
    ends={
        Property(name="dmx_DExpression65", type=dmx_DmxListExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxListExpression", type=dmx_DExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target66: BinaryAssociation = BinaryAssociation(
    name="target66",
    ends={
        Property(name="dmx_IStaticReferenceTarget", type=dmx_DmxStaticReference, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxStaticReference", type=dmx_IStaticReferenceTarget, multiplicity=Multiplicity(0, 1))
    }
)
if71: BinaryAssociation = BinaryAssociation(
    name="if71",
    ends={
        Property(name="dmx_DExpression72", type=dmx_DmxIfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxIfExpression", type=dmx_DExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then73: BinaryAssociation = BinaryAssociation(
    name="then73",
    ends={
        Property(name="dmx_DExpression75", type=dmx_DmxIfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxIfExpression74", type=dmx_DExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
else76: BinaryAssociation = BinaryAssociation(
    name="else76",
    ends={
        Property(name="dmx_DExpression78", type=dmx_DmxIfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxIfExpression77", type=dmx_DExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
feature82: BinaryAssociation = BinaryAssociation(
    name="feature82",
    ends={
        Property(name="dmx_DFeature", type=dmx_DmxField, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxField83", type=dmx_DFeature, multiplicity=Multiplicity(0, 1))
    }
)
value84: BinaryAssociation = BinaryAssociation(
    name="value84",
    ends={
        Property(name="dmx_DExpression86", type=dmx_DmxField, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxField85", type=dmx_DExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type79: BinaryAssociation = BinaryAssociation(
    name="type79",
    ends={
        Property(name="dmx_DComplexType", type=dmx_DmxComplexObject, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxComplexObject", type=dmx_DComplexType, multiplicity=Multiplicity(0, 1))
    }
)
fields80: BinaryAssociation = BinaryAssociation(
    name="fields80",
    ends={
        Property(name="dmx_DmxField", type=dmx_DmxComplexObject, multiplicity=Multiplicity(1, 1)),
        Property(name="dmx_DmxComplexObject81", type=dmx_DmxField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_dmx_DmxModel_DModel = Generalization(general=DModel, specific=dmx_DmxModel)
gen_dmx_DmxModel_ITypeContainer = Generalization(general=ITypeContainer, specific=dmx_DmxModel)
gen_dmx_DmxTest_INavigableMemberContainer = Generalization(general=INavigableMemberContainer, specific=dmx_DmxTest)
gen_dmx_DmxTestContext_DContext = Generalization(general=DContext, specific=dmx_DmxTestContext)
gen_dmx_DmxArchetype_DPrimitive = Generalization(general=DPrimitive, specific=dmx_DmxArchetype)
gen_dmx_DmxFilter_DNavigableMember = Generalization(general=DNavigableMember, specific=dmx_DmxFilter)
gen_dmx_DmxPredicateWithCorrelationVariable_DExpression = Generalization(general=DExpression, specific=dmx_DmxPredicateWithCorrelationVariable)
gen_dmx_DmxPredicateWithCorrelationVariable_INavigableMemberContainer = Generalization(general=INavigableMemberContainer, specific=dmx_DmxPredicateWithCorrelationVariable)
gen_dmx_DmxCorrelationVariable_DNavigableMember = Generalization(general=DNavigableMember, specific=dmx_DmxCorrelationVariable)
gen_dmx_DmxMemberNavigation_DExpression = Generalization(general=DExpression, specific=dmx_DmxMemberNavigation)
gen_dmx_DmxAssignment_DExpression = Generalization(general=DExpression, specific=dmx_DmxAssignment)
gen_dmx_DmxBinaryOperation_DExpression = Generalization(general=DExpression, specific=dmx_DmxBinaryOperation)
gen_dmx_DmxFunctionCall_DExpression = Generalization(general=DExpression, specific=dmx_DmxFunctionCall)
gen_dmx_DmxUnaryOperation_DExpression = Generalization(general=DExpression, specific=dmx_DmxUnaryOperation)
gen_dmx_DmxInstanceOfExpression_DExpression = Generalization(general=DExpression, specific=dmx_DmxInstanceOfExpression)
gen_dmx_DmxContextReference_DExpression = Generalization(general=DExpression, specific=dmx_DmxContextReference)
gen_dmx_DmxCastExpression_DExpression = Generalization(general=DExpression, specific=dmx_DmxCastExpression)
gen_dmx_DmxListExpression_DExpression = Generalization(general=DExpression, specific=dmx_DmxListExpression)
gen_dmx_DmxStaticReference_DExpression = Generalization(general=DExpression, specific=dmx_DmxStaticReference)
gen_dmx_DmxNaturalLiteral_DExpression = Generalization(general=DExpression, specific=dmx_DmxNaturalLiteral)
gen_dmx_DmxDecimalLiteral_DExpression = Generalization(general=DExpression, specific=dmx_DmxDecimalLiteral)
gen_dmx_DmxDateLiteral_DExpression = Generalization(general=DExpression, specific=dmx_DmxDateLiteral)
gen_dmx_DmxIfExpression_DExpression = Generalization(general=DExpression, specific=dmx_DmxIfExpression)
gen_dmx_DmxBooleanLiteral_DExpression = Generalization(general=DExpression, specific=dmx_DmxBooleanLiteral)
gen_dmx_DmxStringLiteral_DExpression = Generalization(general=DExpression, specific=dmx_DmxStringLiteral)
gen_dmx_DmxEntity_DmxComplexObject = Generalization(general=DmxComplexObject, specific=dmx_DmxEntity)
gen_dmx_DmxDetail_DmxComplexObject = Generalization(general=DmxComplexObject, specific=dmx_DmxDetail)
gen_dmx_DmxUrlLiteral_DExpression = Generalization(general=DExpression, specific=dmx_DmxUrlLiteral)
gen_dmx_DmxUndefinedLiteral_DExpression = Generalization(general=DExpression, specific=dmx_DmxUndefinedLiteral)
gen_dmx_DmxComplexObject_INavigableMemberContainer = Generalization(general=INavigableMemberContainer, specific=dmx_DmxComplexObject)
gen_dmx_DmxComplexObject_DExpression = Generalization(general=DExpression, specific=dmx_DmxComplexObject)
gen_dmx_DmxField_DNavigableMember = Generalization(general=DNavigableMember, specific=dmx_DmxField)

# Domain Model
domain_model = DomainModel(
    name="dmx",
    types={dmx_DmxModel, DModel, ITypeContainer, dmx_DmxFilter, dmx_DmxTest, INavigableMemberContainer, dmx_DmxTestContext, dmx_DExpression, DContext, dmx_DmxBaseTypeSet, dmx_DmxArchetype, DPrimitive, DNavigableMember, dmx_DmxFilterParameter, dmx_DmxFilterTypeDescriptor, dmx_DmxPredicateWithCorrelationVariable, dmx_DmxCorrelationVariable, dmx_DmxMemberNavigation, dmx_DmxAssignment, DExpression, dmx_DNavigableMember, dmx_DmxBinaryOperation, dmx_DmxCallArguments, dmx_DmxFunctionCall, dmx_DType, dmx_DmxUnaryOperation, dmx_DmxInstanceOfExpression, dmx_DmxContextReference, dmx_DNamedElement, dmx_DmxCastExpression, dmx_DmxListExpression, dmx_DmxStaticReference, dmx_IStaticReferenceTarget, dmx_DmxNaturalLiteral, dmx_DmxDecimalLiteral, dmx_DmxDateLiteral, dmx_DmxUrlLiteral, dmx_DmxIfExpression, dmx_DmxBooleanLiteral, dmx_DmxStringLiteral, dmx_DFeature, dmx_DmxEntity, DmxComplexObject, dmx_DmxDetail, dmx_DmxUndefinedLiteral, dmx_DmxComplexObject, dmx_DComplexType, dmx_DmxField, DmxBaseType, DmxBinaryOperator, DmxUnaryOperator},
    associations={filters0, tests1, context3, expr5, value7, withTypeSet14, parameters10, typeDesc12, correlationVariable29, predicate30, multiple16, typeDesc19, precedingNavigationSegment22, assignToMember24, value26, callArguments45, leftOperand48, rightOperand50, member33, precedingNavigationSegment35, callArguments38, arguments40, function43, expression53, type55, operand57, member67, target70, target59, type61, elements64, target66, if71, then73, else76, feature82, value84, type79, fields80},
    generalizations={gen_dmx_DmxModel_DModel, gen_dmx_DmxModel_ITypeContainer, gen_dmx_DmxTest_INavigableMemberContainer, gen_dmx_DmxTestContext_DContext, gen_dmx_DmxArchetype_DPrimitive, gen_dmx_DmxFilter_DNavigableMember, gen_dmx_DmxPredicateWithCorrelationVariable_DExpression, gen_dmx_DmxPredicateWithCorrelationVariable_INavigableMemberContainer, gen_dmx_DmxCorrelationVariable_DNavigableMember, gen_dmx_DmxMemberNavigation_DExpression, gen_dmx_DmxAssignment_DExpression, gen_dmx_DmxBinaryOperation_DExpression, gen_dmx_DmxFunctionCall_DExpression, gen_dmx_DmxUnaryOperation_DExpression, gen_dmx_DmxInstanceOfExpression_DExpression, gen_dmx_DmxContextReference_DExpression, gen_dmx_DmxCastExpression_DExpression, gen_dmx_DmxListExpression_DExpression, gen_dmx_DmxStaticReference_DExpression, gen_dmx_DmxNaturalLiteral_DExpression, gen_dmx_DmxDecimalLiteral_DExpression, gen_dmx_DmxDateLiteral_DExpression, gen_dmx_DmxIfExpression_DExpression, gen_dmx_DmxBooleanLiteral_DExpression, gen_dmx_DmxStringLiteral_DExpression, gen_dmx_DmxEntity_DmxComplexObject, gen_dmx_DmxDetail_DmxComplexObject, gen_dmx_DmxUrlLiteral_DExpression, gen_dmx_DmxUndefinedLiteral_DExpression, gen_dmx_DmxComplexObject_INavigableMemberContainer, gen_dmx_DmxComplexObject_DExpression, gen_dmx_DmxField_DNavigableMember},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)