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
operators: Enumeration = Enumeration(
    name="operators",
    literals={
            EnumerationLiteral(name="equal"),
			EnumerationLiteral(name="dis"),
			EnumerationLiteral(name="l"),
			EnumerationLiteral(name="g"),
			EnumerationLiteral(name="le"),
			EnumerationLiteral(name="ge"),
			EnumerationLiteral(name="or"),
			EnumerationLiteral(name="xor"),
			EnumerationLiteral(name="xnor"),
			EnumerationLiteral(name="and"),
			EnumerationLiteral(name="u"),
			EnumerationLiteral(name="v"),
			EnumerationLiteral(name="s"),
			EnumerationLiteral(name="t")
    }
)

# Classes
nuSMV_NuSmvModel = Class(name="nuSMV::NuSmvModel")
nuSMV_Module = Class(name="nuSMV::Module")
nuSMV_FormalParameter = Class(name="nuSMV::FormalParameter")
nuSMV_ModuleElement = Class(name="nuSMV::ModuleElement")
nuSMV_VariableDeclaration = Class(name="nuSMV::VariableDeclaration")
ModuleElement = Class(name="ModuleElement")
nuSMV_VarBody = Class(name="nuSMV::VarBody")
nuSMV_Type = Class(name="nuSMV::Type")
nuSMV_DefineDeclaration = Class(name="nuSMV::DefineDeclaration")
nuSMV_DefineBody = Class(name="nuSMV::DefineBody")
nuSMV_SimpleExpression = Class(name="nuSMV::SimpleExpression")
nuSMV_ConstantsDeclaration = Class(name="nuSMV::ConstantsDeclaration")
nuSMV_IVariableDeclaration = Class(name="nuSMV::IVariableDeclaration")
nuSMV_FrozenVariableDeclaration = Class(name="nuSMV::FrozenVariableDeclaration")
nuSMV_AssignBody = Class(name="nuSMV::AssignBody")
nuSMV_EObject = Class(name="nuSMV::EObject")
nuSMV_VarBodyAssign = Class(name="nuSMV::VarBodyAssign")
AssignBody = Class(name="AssignBody")
nuSMV_InitBody = Class(name="nuSMV::InitBody")
nuSMV_NextBody = Class(name="nuSMV::NextBody")
nuSMV_NextExpression = Class(name="nuSMV::NextExpression")
nuSMV_TransConstraint = Class(name="nuSMV::TransConstraint")
nuSMV_AssignConstraintElement = Class(name="nuSMV::AssignConstraintElement")
nuSMV_InvarConstraint = Class(name="nuSMV::InvarConstraint")
nuSMV_FairnessConstraint = Class(name="nuSMV::FairnessConstraint")
nuSMV_FairnessExpression = Class(name="nuSMV::FairnessExpression")
FairnessConstraint = Class(name="FairnessConstraint")
nuSMV_JusticeExpression = Class(name="nuSMV::JusticeExpression")
nuSMV_CompassionExpression = Class(name="nuSMV::CompassionExpression")
nuSMV_CtlSpecification = Class(name="nuSMV::CtlSpecification")
nuSMV_CTLExpression = Class(name="nuSMV::CTLExpression")
nuSMV_InvarSpecification = Class(name="nuSMV::InvarSpecification")
nuSMV_InitConstraint = Class(name="nuSMV::InitConstraint")
nuSMV_IsaDeclaration = Class(name="nuSMV::IsaDeclaration")
nuSMV_LtlSpecification = Class(name="nuSMV::LtlSpecification")
nuSMV_LTLExpression = Class(name="nuSMV::LTLExpression")
nuSMV_SimpleType = Class(name="nuSMV::SimpleType")
Type = Class(name="Type")
nuSMV_ModuleType = Class(name="nuSMV::ModuleType")
nuSMV_Val = Class(name="nuSMV::Val")
nuSMV_CaseSimpleExpression = Class(name="nuSMV::CaseSimpleExpression")
SimpleExpression = Class(name="SimpleExpression")
nuSMV_CaseSimpleAssignementExpression = Class(name="nuSMV::CaseSimpleAssignementExpression")
nuSMV_RangeExpression = Class(name="nuSMV::RangeExpression")
nuSMV_RTCTLExpression = Class(name="nuSMV::RTCTLExpression")
nuSMV_ComputeSpecification = Class(name="nuSMV::ComputeSpecification")
nuSMV_BooleanType = Class(name="nuSMV::BooleanType")
SimpleType = Class(name="SimpleType")
nuSMV_WordType = Class(name="nuSMV::WordType")
nuSMV_UnsignedWordType = Class(name="nuSMV::UnsignedWordType")
nuSMV_SignedWordType = Class(name="nuSMV::SignedWordType")
nuSMV_EnumType = Class(name="nuSMV::EnumType")
nuSMV_IntervalType = Class(name="nuSMV::IntervalType")
nuSMV_ArrayType = Class(name="nuSMV::ArrayType")
nuSMV_Not = Class(name="nuSMV::Not")
nuSMV_ParsExpression = Class(name="nuSMV::ParsExpression")
nuSMV_UnaryExpression = Class(name="nuSMV::UnaryExpression")
nuSMV_AsyncrProcessType = Class(name="nuSMV::AsyncrProcessType")
ModuleType = Class(name="ModuleType")
nuSMV_SyncrProcessType = Class(name="nuSMV::SyncrProcessType")
nuSMV_BinaryExpression = Class(name="nuSMV::BinaryExpression")
nuSMV_SetElementExpression = Class(name="nuSMV::SetElementExpression")
nuSMV_SetValueParameter = Class(name="nuSMV::SetValueParameter")
nuSMV_SetExpression = Class(name="nuSMV::SetExpression")
nuSMV_WordExpression = Class(name="nuSMV::WordExpression")
nuSMV_IntervalExpression = Class(name="nuSMV::IntervalExpression")
nuSMV_ValueExpression = Class(name="nuSMV::ValueExpression")
nuSMV_Var = Class(name="nuSMV::Var")
nuSMV_UnaryFunctionExpression = Class(name="nuSMV::UnaryFunctionExpression")
nuSMV_SingleRTCTLExpression = Class(name="nuSMV::SingleRTCTLExpression")
RTCTLExpression = Class(name="RTCTLExpression")
nuSMV_UnaryRTCTLExpression = Class(name="nuSMV::UnaryRTCTLExpression")
nuSMV_UntilCTLexpression = Class(name="nuSMV::UntilCTLexpression")

# nuSMV_NuSmvModel class attributes and methods

# nuSMV_Module class attributes and methods
nuSMV_Module_name: Property = Property(name="name", type=StringType)
nuSMV_Module.attributes={nuSMV_Module_name}

# nuSMV_FormalParameter class attributes and methods
nuSMV_FormalParameter_name: Property = Property(name="name", type=StringType)
nuSMV_FormalParameter.attributes={nuSMV_FormalParameter_name}

# nuSMV_ModuleElement class attributes and methods

# nuSMV_VariableDeclaration class attributes and methods

# ModuleElement class attributes and methods

# nuSMV_VarBody class attributes and methods
nuSMV_VarBody_name: Property = Property(name="name", type=StringType)
nuSMV_VarBody_semicolon: Property = Property(name="semicolon", type=BooleanType)
nuSMV_VarBody.attributes={nuSMV_VarBody_name, nuSMV_VarBody_semicolon}

# nuSMV_Type class attributes and methods

# nuSMV_DefineDeclaration class attributes and methods
nuSMV_DefineDeclaration_define: Property = Property(name="define", type=StringType)
nuSMV_DefineDeclaration.attributes={nuSMV_DefineDeclaration_define}

# nuSMV_DefineBody class attributes and methods
nuSMV_DefineBody_var: Property = Property(name="var", type=StringType)
nuSMV_DefineBody_semicolon: Property = Property(name="semicolon", type=BooleanType)
nuSMV_DefineBody.attributes={nuSMV_DefineBody_var, nuSMV_DefineBody_semicolon}

# nuSMV_SimpleExpression class attributes and methods

# nuSMV_ConstantsDeclaration class attributes and methods
nuSMV_ConstantsDeclaration_constants: Property = Property(name="constants", type=StringType)
nuSMV_ConstantsDeclaration_semicolon: Property = Property(name="semicolon", type=BooleanType)
nuSMV_ConstantsDeclaration.attributes={nuSMV_ConstantsDeclaration_constants, nuSMV_ConstantsDeclaration_semicolon}

# nuSMV_IVariableDeclaration class attributes and methods

# nuSMV_FrozenVariableDeclaration class attributes and methods

# nuSMV_AssignBody class attributes and methods
nuSMV_AssignBody_array: Property = Property(name="array", type=StringType)
nuSMV_AssignBody_semicolon: Property = Property(name="semicolon", type=BooleanType)
nuSMV_AssignBody.attributes={nuSMV_AssignBody_semicolon, nuSMV_AssignBody_array}

# nuSMV_EObject class attributes and methods

# nuSMV_VarBodyAssign class attributes and methods

# AssignBody class attributes and methods

# nuSMV_InitBody class attributes and methods

# nuSMV_NextBody class attributes and methods

# nuSMV_NextExpression class attributes and methods

# nuSMV_TransConstraint class attributes and methods
nuSMV_TransConstraint_semicolon: Property = Property(name="semicolon", type=BooleanType)
nuSMV_TransConstraint.attributes={nuSMV_TransConstraint_semicolon}

# nuSMV_AssignConstraintElement class attributes and methods
nuSMV_AssignConstraintElement_assign: Property = Property(name="assign", type=StringType)
nuSMV_AssignConstraintElement.attributes={nuSMV_AssignConstraintElement_assign}

# nuSMV_InvarConstraint class attributes and methods
nuSMV_InvarConstraint_semicolon: Property = Property(name="semicolon", type=BooleanType)
nuSMV_InvarConstraint.attributes={nuSMV_InvarConstraint_semicolon}

# nuSMV_FairnessConstraint class attributes and methods
nuSMV_FairnessConstraint_semicolon: Property = Property(name="semicolon", type=BooleanType)
nuSMV_FairnessConstraint.attributes={nuSMV_FairnessConstraint_semicolon}

# nuSMV_FairnessExpression class attributes and methods

# FairnessConstraint class attributes and methods

# nuSMV_JusticeExpression class attributes and methods

# nuSMV_CompassionExpression class attributes and methods

# nuSMV_CtlSpecification class attributes and methods
nuSMV_CtlSpecification_specKeyWord: Property = Property(name="specKeyWord", type=StringType)
nuSMV_CtlSpecification_nameKeyWord: Property = Property(name="nameKeyWord", type=BooleanType)
nuSMV_CtlSpecification_name: Property = Property(name="name", type=StringType)
nuSMV_CtlSpecification_semicolon: Property = Property(name="semicolon", type=BooleanType)
nuSMV_CtlSpecification.attributes={nuSMV_CtlSpecification_nameKeyWord, nuSMV_CtlSpecification_semicolon, nuSMV_CtlSpecification_name, nuSMV_CtlSpecification_specKeyWord}

# nuSMV_CTLExpression class attributes and methods

# nuSMV_InvarSpecification class attributes and methods
nuSMV_InvarSpecification_name: Property = Property(name="name", type=StringType)
nuSMV_InvarSpecification_semicolon: Property = Property(name="semicolon", type=BooleanType)
nuSMV_InvarSpecification.attributes={nuSMV_InvarSpecification_name, nuSMV_InvarSpecification_semicolon}

# nuSMV_InitConstraint class attributes and methods
nuSMV_InitConstraint_semicolon: Property = Property(name="semicolon", type=BooleanType)
nuSMV_InitConstraint.attributes={nuSMV_InitConstraint_semicolon}

# nuSMV_IsaDeclaration class attributes and methods
nuSMV_IsaDeclaration_id: Property = Property(name="id", type=StringType)
nuSMV_IsaDeclaration.attributes={nuSMV_IsaDeclaration_id}

# nuSMV_LtlSpecification class attributes and methods
nuSMV_LtlSpecification_nameId: Property = Property(name="nameId", type=BooleanType)
nuSMV_LtlSpecification_name: Property = Property(name="name", type=StringType)
nuSMV_LtlSpecification_semicolon: Property = Property(name="semicolon", type=BooleanType)
nuSMV_LtlSpecification.attributes={nuSMV_LtlSpecification_semicolon, nuSMV_LtlSpecification_name, nuSMV_LtlSpecification_nameId}

# nuSMV_LTLExpression class attributes and methods

# nuSMV_SimpleType class attributes and methods

# Type class attributes and methods

# nuSMV_ModuleType class attributes and methods

# nuSMV_Val class attributes and methods
nuSMV_Val_name: Property = Property(name="name", type=StringType)
nuSMV_Val_num: Property = Property(name="num", type=StringType)
nuSMV_Val.attributes={nuSMV_Val_name, nuSMV_Val_num}

# nuSMV_CaseSimpleExpression class attributes and methods

# SimpleExpression class attributes and methods

# nuSMV_CaseSimpleAssignementExpression class attributes and methods

# nuSMV_RangeExpression class attributes and methods
nuSMV_RangeExpression_lower: Property = Property(name="lower", type=StringType)
nuSMV_RangeExpression_upper: Property = Property(name="upper", type=StringType)
nuSMV_RangeExpression.attributes={nuSMV_RangeExpression_upper, nuSMV_RangeExpression_lower}

# nuSMV_RTCTLExpression class attributes and methods

# nuSMV_ComputeSpecification class attributes and methods
nuSMV_ComputeSpecification_minMax: Property = Property(name="minMax", type=StringType)
nuSMV_ComputeSpecification.attributes={nuSMV_ComputeSpecification_minMax}

# nuSMV_BooleanType class attributes and methods

# SimpleType class attributes and methods

# nuSMV_WordType class attributes and methods
nuSMV_WordType_wordNumber: Property = Property(name="wordNumber", type=StringType)
nuSMV_WordType.attributes={nuSMV_WordType_wordNumber}

# nuSMV_UnsignedWordType class attributes and methods
nuSMV_UnsignedWordType_uWordNumber: Property = Property(name="uWordNumber", type=StringType)
nuSMV_UnsignedWordType.attributes={nuSMV_UnsignedWordType_uWordNumber}

# nuSMV_SignedWordType class attributes and methods
nuSMV_SignedWordType_signedNumber: Property = Property(name="signedNumber", type=StringType)
nuSMV_SignedWordType.attributes={nuSMV_SignedWordType_signedNumber}

# nuSMV_EnumType class attributes and methods

# nuSMV_IntervalType class attributes and methods
nuSMV_IntervalType_low: Property = Property(name="low", type=StringType)
nuSMV_IntervalType_high: Property = Property(name="high", type=StringType)
nuSMV_IntervalType.attributes={nuSMV_IntervalType_low, nuSMV_IntervalType_high}

# nuSMV_ArrayType class attributes and methods
nuSMV_ArrayType_lowerBound: Property = Property(name="lowerBound", type=StringType)
nuSMV_ArrayType_upperBound: Property = Property(name="upperBound", type=StringType)
nuSMV_ArrayType.attributes={nuSMV_ArrayType_upperBound, nuSMV_ArrayType_lowerBound}

# nuSMV_Not class attributes and methods

# nuSMV_ParsExpression class attributes and methods
nuSMV_ParsExpression_isNext: Property = Property(name="isNext", type=BooleanType)
nuSMV_ParsExpression.attributes={nuSMV_ParsExpression_isNext}

# nuSMV_UnaryExpression class attributes and methods
nuSMV_UnaryExpression_operator: Property = Property(name="operator", type=StringType)
nuSMV_UnaryExpression.attributes={nuSMV_UnaryExpression_operator}

# nuSMV_AsyncrProcessType class attributes and methods

# ModuleType class attributes and methods

# nuSMV_SyncrProcessType class attributes and methods

# nuSMV_BinaryExpression class attributes and methods
nuSMV_BinaryExpression_operator: Property = Property(name="operator", type=StringType)
nuSMV_BinaryExpression_op: Property = Property(name="op", type=StringType)
nuSMV_BinaryExpression.attributes={nuSMV_BinaryExpression_operator, nuSMV_BinaryExpression_op}

# nuSMV_SetElementExpression class attributes and methods

# nuSMV_SetValueParameter class attributes and methods

# nuSMV_SetExpression class attributes and methods

# nuSMV_WordExpression class attributes and methods
nuSMV_WordExpression_value: Property = Property(name="value", type=StringType)
nuSMV_WordExpression.attributes={nuSMV_WordExpression_value}

# nuSMV_IntervalExpression class attributes and methods
nuSMV_IntervalExpression_lowerBound: Property = Property(name="lowerBound", type=StringType)
nuSMV_IntervalExpression_upperBound: Property = Property(name="upperBound", type=StringType)
nuSMV_IntervalExpression.attributes={nuSMV_IntervalExpression_upperBound, nuSMV_IntervalExpression_lowerBound}

# nuSMV_ValueExpression class attributes and methods
nuSMV_ValueExpression_value: Property = Property(name="value", type=StringType)
nuSMV_ValueExpression.attributes={nuSMV_ValueExpression_value}

# nuSMV_Var class attributes and methods

# nuSMV_UnaryFunctionExpression class attributes and methods
nuSMV_UnaryFunctionExpression_function: Property = Property(name="function", type=StringType)
nuSMV_UnaryFunctionExpression.attributes={nuSMV_UnaryFunctionExpression_function}

# nuSMV_SingleRTCTLExpression class attributes and methods

# RTCTLExpression class attributes and methods

# nuSMV_UnaryRTCTLExpression class attributes and methods
nuSMV_UnaryRTCTLExpression_unary: Property = Property(name="unary", type=StringType)
nuSMV_UnaryRTCTLExpression.attributes={nuSMV_UnaryRTCTLExpression_unary}

# nuSMV_UntilCTLexpression class attributes and methods
nuSMV_UntilCTLexpression_ea: Property = Property(name="ea", type=StringType)
nuSMV_UntilCTLexpression.attributes={nuSMV_UntilCTLexpression_ea}

# Relationships
modules0: BinaryAssociation = BinaryAssociation(
    name="modules0",
    ends={
        Property(name="nuSMV_Module", type=nuSMV_NuSmvModel, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_NuSmvModel", type=nuSMV_Module, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
params1: BinaryAssociation = BinaryAssociation(
    name="params1",
    ends={
        Property(name="nuSMV_FormalParameter", type=nuSMV_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_Module2", type=nuSMV_FormalParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
moduleElement3: BinaryAssociation = BinaryAssociation(
    name="moduleElement3",
    ends={
        Property(name="nuSMV_ModuleElement", type=nuSMV_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_Module4", type=nuSMV_ModuleElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vars5: BinaryAssociation = BinaryAssociation(
    name="vars5",
    ends={
        Property(name="nuSMV_VarBody", type=nuSMV_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_VariableDeclaration", type=nuSMV_VarBody, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vars8: BinaryAssociation = BinaryAssociation(
    name="vars8",
    ends={
        Property(name="nuSMV_VarBody9", type=nuSMV_FrozenVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_FrozenVariableDeclaration", type=nuSMV_VarBody, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type10: BinaryAssociation = BinaryAssociation(
    name="type10",
    ends={
        Property(name="nuSMV_Type", type=nuSMV_VarBody, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_VarBody11", type=nuSMV_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defineBodies12: BinaryAssociation = BinaryAssociation(
    name="defineBodies12",
    ends={
        Property(name="nuSMV_DefineBody", type=nuSMV_DefineDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_DefineDeclaration", type=nuSMV_DefineBody, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assignment13: BinaryAssociation = BinaryAssociation(
    name="assignment13",
    ends={
        Property(name="nuSMV_SimpleExpression", type=nuSMV_DefineBody, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_DefineBody14", type=nuSMV_SimpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vars6: BinaryAssociation = BinaryAssociation(
    name="vars6",
    ends={
        Property(name="nuSMV_VarBody7", type=nuSMV_IVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_IVariableDeclaration", type=nuSMV_VarBody, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodies15: BinaryAssociation = BinaryAssociation(
    name="bodies15",
    ends={
        Property(name="nuSMV_AssignBody", type=nuSMV_AssignConstraintElement, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_AssignConstraintElement", type=nuSMV_AssignBody, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
var16: BinaryAssociation = BinaryAssociation(
    name="var16",
    ends={
        Property(name="nuSMV_EObject", type=nuSMV_AssignBody, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_AssignBody17", type=nuSMV_EObject, multiplicity=Multiplicity(0, 1))
    }
)
dotted18: BinaryAssociation = BinaryAssociation(
    name="dotted18",
    ends={
        Property(name="nuSMV_SimpleExpression20", type=nuSMV_AssignBody, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_AssignBody19", type=nuSMV_SimpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment21: BinaryAssociation = BinaryAssociation(
    name="assignment21",
    ends={
        Property(name="nuSMV_SimpleExpression22", type=nuSMV_VarBodyAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_VarBodyAssign", type=nuSMV_SimpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initial23: BinaryAssociation = BinaryAssociation(
    name="initial23",
    ends={
        Property(name="nuSMV_SimpleExpression24", type=nuSMV_InitBody, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_InitBody", type=nuSMV_SimpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
next25: BinaryAssociation = BinaryAssociation(
    name="next25",
    ends={
        Property(name="nuSMV_NextExpression", type=nuSMV_NextBody, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_NextBody", type=nuSMV_NextExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initExpression28: BinaryAssociation = BinaryAssociation(
    name="initExpression28",
    ends={
        Property(name="nuSMV_SimpleExpression29", type=nuSMV_InitConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_InitConstraint", type=nuSMV_SimpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
invarExpression30: BinaryAssociation = BinaryAssociation(
    name="invarExpression30",
    ends={
        Property(name="nuSMV_SimpleExpression31", type=nuSMV_InvarConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_InvarConstraint", type=nuSMV_SimpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fairnessExpr32: BinaryAssociation = BinaryAssociation(
    name="fairnessExpr32",
    ends={
        Property(name="nuSMV_SimpleExpression33", type=nuSMV_FairnessExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_FairnessExpression", type=nuSMV_SimpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
justiceExpr34: BinaryAssociation = BinaryAssociation(
    name="justiceExpr34",
    ends={
        Property(name="nuSMV_SimpleExpression35", type=nuSMV_JusticeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_JusticeExpression", type=nuSMV_SimpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
firstExpr36: BinaryAssociation = BinaryAssociation(
    name="firstExpr36",
    ends={
        Property(name="nuSMV_SimpleExpression37", type=nuSMV_CompassionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_CompassionExpression", type=nuSMV_SimpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
secondExpr38: BinaryAssociation = BinaryAssociation(
    name="secondExpr38",
    ends={
        Property(name="nuSMV_SimpleExpression40", type=nuSMV_CompassionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_CompassionExpression39", type=nuSMV_SimpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ctlExpression41: BinaryAssociation = BinaryAssociation(
    name="ctlExpression41",
    ends={
        Property(name="nuSMV_CTLExpression", type=nuSMV_CtlSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_CtlSpecification", type=nuSMV_CTLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transExpression26: BinaryAssociation = BinaryAssociation(
    name="transExpression26",
    ends={
        Property(name="nuSMV_SimpleExpression27", type=nuSMV_TransConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_TransConstraint", type=nuSMV_SimpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
invarSpec42: BinaryAssociation = BinaryAssociation(
    name="invarSpec42",
    ends={
        Property(name="nuSMV_NextExpression43", type=nuSMV_InvarSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_InvarSpecification", type=nuSMV_NextExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ltlExpression44: BinaryAssociation = BinaryAssociation(
    name="ltlExpression44",
    ends={
        Property(name="nuSMV_LTLExpression", type=nuSMV_LtlSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_LtlSpecification", type=nuSMV_LTLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
par50: BinaryAssociation = BinaryAssociation(
    name="par50",
    ends={
        Property(name="nuSMV_VarBody52", type=nuSMV_ModuleType, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_ModuleType51", type=nuSMV_VarBody, multiplicity=Multiplicity(0, 1))
    }
)
simpleExpression53: BinaryAssociation = BinaryAssociation(
    name="simpleExpression53",
    ends={
        Property(name="nuSMV_SimpleExpression55", type=nuSMV_NextExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_NextExpression54", type=nuSMV_SimpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
branches56: BinaryAssociation = BinaryAssociation(
    name="branches56",
    ends={
        Property(name="nuSMV_CaseSimpleAssignementExpression", type=nuSMV_CaseSimpleExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_CaseSimpleExpression", type=nuSMV_CaseSimpleAssignementExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
case57: BinaryAssociation = BinaryAssociation(
    name="case57",
    ends={
        Property(name="nuSMV_SimpleExpression59", type=nuSMV_CaseSimpleAssignementExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_CaseSimpleAssignementExpression58", type=nuSMV_SimpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment60: BinaryAssociation = BinaryAssociation(
    name="assignment60",
    ends={
        Property(name="nuSMV_SimpleExpression62", type=nuSMV_CaseSimpleAssignementExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_CaseSimpleAssignementExpression61", type=nuSMV_SimpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
module45: BinaryAssociation = BinaryAssociation(
    name="module45",
    ends={
        Property(name="nuSMV_Module46", type=nuSMV_ModuleType, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_ModuleType", type=nuSMV_Module, multiplicity=Multiplicity(0, 1))
    }
)
params47: BinaryAssociation = BinaryAssociation(
    name="params47",
    ends={
        Property(name="nuSMV_SimpleExpression49", type=nuSMV_ModuleType, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_ModuleType48", type=nuSMV_SimpleExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
simpleExpression66: BinaryAssociation = BinaryAssociation(
    name="simpleExpression66",
    ends={
        Property(name="nuSMV_SimpleExpression68", type=nuSMV_LTLExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_LTLExpression67", type=nuSMV_SimpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
first69: BinaryAssociation = BinaryAssociation(
    name="first69",
    ends={
        Property(name="nuSMV_RTCTLExpression", type=nuSMV_ComputeSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_ComputeSpecification", type=nuSMV_RTCTLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
second70: BinaryAssociation = BinaryAssociation(
    name="second70",
    ends={
        Property(name="nuSMV_RTCTLExpression72", type=nuSMV_ComputeSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_ComputeSpecification71", type=nuSMV_RTCTLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleExpression63: BinaryAssociation = BinaryAssociation(
    name="simpleExpression63",
    ends={
        Property(name="nuSMV_SimpleExpression65", type=nuSMV_CTLExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_CTLExpression64", type=nuSMV_SimpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
val73: BinaryAssociation = BinaryAssociation(
    name="val73",
    ends={
        Property(name="nuSMV_Val", type=nuSMV_EnumType, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_EnumType", type=nuSMV_Val, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left75: BinaryAssociation = BinaryAssociation(
    name="left75",
    ends={
        Property(name="nuSMV_SimpleExpression76", type=nuSMV_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_BinaryExpression", type=nuSMV_SimpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right77: BinaryAssociation = BinaryAssociation(
    name="right77",
    ends={
        Property(name="nuSMV_SimpleExpression79", type=nuSMV_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_BinaryExpression78", type=nuSMV_SimpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp80: BinaryAssociation = BinaryAssociation(
    name="exp80",
    ends={
        Property(name="nuSMV_SimpleExpression81", type=nuSMV_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_Not", type=nuSMV_SimpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleExpression82: BinaryAssociation = BinaryAssociation(
    name="simpleExpression82",
    ends={
        Property(name="nuSMV_SimpleExpression83", type=nuSMV_ParsExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_ParsExpression", type=nuSMV_SimpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleExpression84: BinaryAssociation = BinaryAssociation(
    name="simpleExpression84",
    ends={
        Property(name="nuSMV_SimpleExpression85", type=nuSMV_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_UnaryExpression", type=nuSMV_SimpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type74: BinaryAssociation = BinaryAssociation(
    name="type74",
    ends={
        Property(name="nuSMV_SimpleType", type=nuSMV_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_ArrayType", type=nuSMV_SimpleType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value86: BinaryAssociation = BinaryAssociation(
    name="value86",
    ends={
        Property(name="nuSMV_VarBody87", type=nuSMV_Var, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_Var", type=nuSMV_VarBody, multiplicity=Multiplicity(0, 1))
    }
)
dotted88: BinaryAssociation = BinaryAssociation(
    name="dotted88",
    ends={
        Property(name="nuSMV_SimpleExpression90", type=nuSMV_Var, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_Var89", type=nuSMV_SimpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
val91: BinaryAssociation = BinaryAssociation(
    name="val91",
    ends={
        Property(name="nuSMV_Val92", type=nuSMV_SetElementExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_SetElementExpression", type=nuSMV_Val, multiplicity=Multiplicity(0, 1))
    }
)
valparam93: BinaryAssociation = BinaryAssociation(
    name="valparam93",
    ends={
        Property(name="nuSMV_FormalParameter94", type=nuSMV_SetValueParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_SetValueParameter", type=nuSMV_FormalParameter, multiplicity=Multiplicity(0, 1))
    }
)
setElement95: BinaryAssociation = BinaryAssociation(
    name="setElement95",
    ends={
        Property(name="nuSMV_SimpleExpression96", type=nuSMV_SetExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_SetExpression", type=nuSMV_SimpleExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arg97: BinaryAssociation = BinaryAssociation(
    name="arg97",
    ends={
        Property(name="nuSMV_SimpleExpression98", type=nuSMV_UntilCTLexpression, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_UntilCTLexpression", type=nuSMV_SimpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arg99: BinaryAssociation = BinaryAssociation(
    name="arg99",
    ends={
        Property(name="nuSMV_SimpleExpression100", type=nuSMV_UnaryFunctionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_UnaryFunctionExpression", type=nuSMV_SimpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ctlExpression101: BinaryAssociation = BinaryAssociation(
    name="ctlExpression101",
    ends={
        Property(name="nuSMV_CTLExpression102", type=nuSMV_SingleRTCTLExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_SingleRTCTLExpression", type=nuSMV_CTLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
range103: BinaryAssociation = BinaryAssociation(
    name="range103",
    ends={
        Property(name="nuSMV_RangeExpression", type=nuSMV_UnaryRTCTLExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_UnaryRTCTLExpression", type=nuSMV_RangeExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rctl104: BinaryAssociation = BinaryAssociation(
    name="rctl104",
    ends={
        Property(name="nuSMV_RTCTLExpression106", type=nuSMV_UnaryRTCTLExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="nuSMV_UnaryRTCTLExpression105", type=nuSMV_RTCTLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_nuSMV_VariableDeclaration_ModuleElement = Generalization(general=ModuleElement, specific=nuSMV_VariableDeclaration)
gen_nuSMV_FrozenVariableDeclaration_ModuleElement = Generalization(general=ModuleElement, specific=nuSMV_FrozenVariableDeclaration)
gen_nuSMV_DefineDeclaration_ModuleElement = Generalization(general=ModuleElement, specific=nuSMV_DefineDeclaration)
gen_nuSMV_ConstantsDeclaration_ModuleElement = Generalization(general=ModuleElement, specific=nuSMV_ConstantsDeclaration)
gen_nuSMV_IVariableDeclaration_ModuleElement = Generalization(general=ModuleElement, specific=nuSMV_IVariableDeclaration)
gen_nuSMV_AssignConstraintElement_ModuleElement = Generalization(general=ModuleElement, specific=nuSMV_AssignConstraintElement)
gen_nuSMV_VarBodyAssign_AssignBody = Generalization(general=AssignBody, specific=nuSMV_VarBodyAssign)
gen_nuSMV_InitBody_AssignBody = Generalization(general=AssignBody, specific=nuSMV_InitBody)
gen_nuSMV_NextBody_AssignBody = Generalization(general=AssignBody, specific=nuSMV_NextBody)
gen_nuSMV_TransConstraint_ModuleElement = Generalization(general=ModuleElement, specific=nuSMV_TransConstraint)
gen_nuSMV_InvarConstraint_ModuleElement = Generalization(general=ModuleElement, specific=nuSMV_InvarConstraint)
gen_nuSMV_FairnessConstraint_ModuleElement = Generalization(general=ModuleElement, specific=nuSMV_FairnessConstraint)
gen_nuSMV_FairnessExpression_FairnessConstraint = Generalization(general=FairnessConstraint, specific=nuSMV_FairnessExpression)
gen_nuSMV_JusticeExpression_FairnessConstraint = Generalization(general=FairnessConstraint, specific=nuSMV_JusticeExpression)
gen_nuSMV_CompassionExpression_FairnessConstraint = Generalization(general=FairnessConstraint, specific=nuSMV_CompassionExpression)
gen_nuSMV_CtlSpecification_ModuleElement = Generalization(general=ModuleElement, specific=nuSMV_CtlSpecification)
gen_nuSMV_InvarSpecification_ModuleElement = Generalization(general=ModuleElement, specific=nuSMV_InvarSpecification)
gen_nuSMV_InitConstraint_ModuleElement = Generalization(general=ModuleElement, specific=nuSMV_InitConstraint)
gen_nuSMV_IsaDeclaration_ModuleElement = Generalization(general=ModuleElement, specific=nuSMV_IsaDeclaration)
gen_nuSMV_LtlSpecification_ModuleElement = Generalization(general=ModuleElement, specific=nuSMV_LtlSpecification)
gen_nuSMV_SimpleType_Type = Generalization(general=Type, specific=nuSMV_SimpleType)
gen_nuSMV_ModuleType_Type = Generalization(general=Type, specific=nuSMV_ModuleType)
gen_nuSMV_CaseSimpleExpression_SimpleExpression = Generalization(general=SimpleExpression, specific=nuSMV_CaseSimpleExpression)
gen_nuSMV_ComputeSpecification_ModuleElement = Generalization(general=ModuleElement, specific=nuSMV_ComputeSpecification)
gen_nuSMV_BooleanType_SimpleType = Generalization(general=SimpleType, specific=nuSMV_BooleanType)
gen_nuSMV_WordType_SimpleType = Generalization(general=SimpleType, specific=nuSMV_WordType)
gen_nuSMV_UnsignedWordType_SimpleType = Generalization(general=SimpleType, specific=nuSMV_UnsignedWordType)
gen_nuSMV_SignedWordType_SimpleType = Generalization(general=SimpleType, specific=nuSMV_SignedWordType)
gen_nuSMV_EnumType_SimpleType = Generalization(general=SimpleType, specific=nuSMV_EnumType)
gen_nuSMV_IntervalType_SimpleType = Generalization(general=SimpleType, specific=nuSMV_IntervalType)
gen_nuSMV_ArrayType_SimpleType = Generalization(general=SimpleType, specific=nuSMV_ArrayType)
gen_nuSMV_BinaryExpression_SimpleExpression = Generalization(general=SimpleExpression, specific=nuSMV_BinaryExpression)
gen_nuSMV_Not_SimpleExpression = Generalization(general=SimpleExpression, specific=nuSMV_Not)
gen_nuSMV_ParsExpression_SimpleExpression = Generalization(general=SimpleExpression, specific=nuSMV_ParsExpression)
gen_nuSMV_UnaryExpression_SimpleExpression = Generalization(general=SimpleExpression, specific=nuSMV_UnaryExpression)
gen_nuSMV_AsyncrProcessType_ModuleType = Generalization(general=ModuleType, specific=nuSMV_AsyncrProcessType)
gen_nuSMV_SyncrProcessType_ModuleType = Generalization(general=ModuleType, specific=nuSMV_SyncrProcessType)
gen_nuSMV_Var_SimpleExpression = Generalization(general=SimpleExpression, specific=nuSMV_Var)
gen_nuSMV_SetElementExpression_SimpleExpression = Generalization(general=SimpleExpression, specific=nuSMV_SetElementExpression)
gen_nuSMV_SetValueParameter_SimpleExpression = Generalization(general=SimpleExpression, specific=nuSMV_SetValueParameter)
gen_nuSMV_SetExpression_SimpleExpression = Generalization(general=SimpleExpression, specific=nuSMV_SetExpression)
gen_nuSMV_WordExpression_SimpleExpression = Generalization(general=SimpleExpression, specific=nuSMV_WordExpression)
gen_nuSMV_IntervalExpression_SimpleExpression = Generalization(general=SimpleExpression, specific=nuSMV_IntervalExpression)
gen_nuSMV_ValueExpression_SimpleExpression = Generalization(general=SimpleExpression, specific=nuSMV_ValueExpression)
gen_nuSMV_UnaryFunctionExpression_SimpleExpression = Generalization(general=SimpleExpression, specific=nuSMV_UnaryFunctionExpression)
gen_nuSMV_SingleRTCTLExpression_RTCTLExpression = Generalization(general=RTCTLExpression, specific=nuSMV_SingleRTCTLExpression)
gen_nuSMV_UnaryRTCTLExpression_RTCTLExpression = Generalization(general=RTCTLExpression, specific=nuSMV_UnaryRTCTLExpression)
gen_nuSMV_UntilCTLexpression_SimpleExpression = Generalization(general=SimpleExpression, specific=nuSMV_UntilCTLexpression)

# Domain Model
domain_model = DomainModel(
    name="nuSMV",
    types={nuSMV_NuSmvModel, nuSMV_Module, nuSMV_FormalParameter, nuSMV_ModuleElement, nuSMV_VariableDeclaration, ModuleElement, nuSMV_VarBody, nuSMV_Type, nuSMV_DefineDeclaration, nuSMV_DefineBody, nuSMV_SimpleExpression, nuSMV_ConstantsDeclaration, nuSMV_IVariableDeclaration, nuSMV_FrozenVariableDeclaration, nuSMV_AssignBody, nuSMV_EObject, nuSMV_VarBodyAssign, AssignBody, nuSMV_InitBody, nuSMV_NextBody, nuSMV_NextExpression, nuSMV_TransConstraint, nuSMV_AssignConstraintElement, nuSMV_InvarConstraint, nuSMV_FairnessConstraint, nuSMV_FairnessExpression, FairnessConstraint, nuSMV_JusticeExpression, nuSMV_CompassionExpression, nuSMV_CtlSpecification, nuSMV_CTLExpression, nuSMV_InvarSpecification, nuSMV_InitConstraint, nuSMV_IsaDeclaration, nuSMV_LtlSpecification, nuSMV_LTLExpression, nuSMV_SimpleType, Type, nuSMV_ModuleType, nuSMV_Val, nuSMV_CaseSimpleExpression, SimpleExpression, nuSMV_CaseSimpleAssignementExpression, nuSMV_RangeExpression, nuSMV_RTCTLExpression, nuSMV_ComputeSpecification, nuSMV_BooleanType, SimpleType, nuSMV_WordType, nuSMV_UnsignedWordType, nuSMV_SignedWordType, nuSMV_EnumType, nuSMV_IntervalType, nuSMV_ArrayType, nuSMV_Not, nuSMV_ParsExpression, nuSMV_UnaryExpression, nuSMV_AsyncrProcessType, ModuleType, nuSMV_SyncrProcessType, nuSMV_BinaryExpression, nuSMV_SetElementExpression, nuSMV_SetValueParameter, nuSMV_SetExpression, nuSMV_WordExpression, nuSMV_IntervalExpression, nuSMV_ValueExpression, nuSMV_Var, nuSMV_UnaryFunctionExpression, nuSMV_SingleRTCTLExpression, RTCTLExpression, nuSMV_UnaryRTCTLExpression, nuSMV_UntilCTLexpression, operators},
    associations={modules0, params1, moduleElement3, vars5, vars8, type10, defineBodies12, assignment13, vars6, bodies15, var16, dotted18, assignment21, initial23, next25, initExpression28, invarExpression30, fairnessExpr32, justiceExpr34, firstExpr36, secondExpr38, ctlExpression41, transExpression26, invarSpec42, ltlExpression44, par50, simpleExpression53, branches56, case57, assignment60, module45, params47, simpleExpression66, first69, second70, simpleExpression63, val73, left75, right77, exp80, simpleExpression82, simpleExpression84, type74, value86, dotted88, val91, valparam93, setElement95, arg97, arg99, ctlExpression101, range103, rctl104},
    generalizations={gen_nuSMV_VariableDeclaration_ModuleElement, gen_nuSMV_FrozenVariableDeclaration_ModuleElement, gen_nuSMV_DefineDeclaration_ModuleElement, gen_nuSMV_ConstantsDeclaration_ModuleElement, gen_nuSMV_IVariableDeclaration_ModuleElement, gen_nuSMV_AssignConstraintElement_ModuleElement, gen_nuSMV_VarBodyAssign_AssignBody, gen_nuSMV_InitBody_AssignBody, gen_nuSMV_NextBody_AssignBody, gen_nuSMV_TransConstraint_ModuleElement, gen_nuSMV_InvarConstraint_ModuleElement, gen_nuSMV_FairnessConstraint_ModuleElement, gen_nuSMV_FairnessExpression_FairnessConstraint, gen_nuSMV_JusticeExpression_FairnessConstraint, gen_nuSMV_CompassionExpression_FairnessConstraint, gen_nuSMV_CtlSpecification_ModuleElement, gen_nuSMV_InvarSpecification_ModuleElement, gen_nuSMV_InitConstraint_ModuleElement, gen_nuSMV_IsaDeclaration_ModuleElement, gen_nuSMV_LtlSpecification_ModuleElement, gen_nuSMV_SimpleType_Type, gen_nuSMV_ModuleType_Type, gen_nuSMV_CaseSimpleExpression_SimpleExpression, gen_nuSMV_ComputeSpecification_ModuleElement, gen_nuSMV_BooleanType_SimpleType, gen_nuSMV_WordType_SimpleType, gen_nuSMV_UnsignedWordType_SimpleType, gen_nuSMV_SignedWordType_SimpleType, gen_nuSMV_EnumType_SimpleType, gen_nuSMV_IntervalType_SimpleType, gen_nuSMV_ArrayType_SimpleType, gen_nuSMV_BinaryExpression_SimpleExpression, gen_nuSMV_Not_SimpleExpression, gen_nuSMV_ParsExpression_SimpleExpression, gen_nuSMV_UnaryExpression_SimpleExpression, gen_nuSMV_AsyncrProcessType_ModuleType, gen_nuSMV_SyncrProcessType_ModuleType, gen_nuSMV_Var_SimpleExpression, gen_nuSMV_SetElementExpression_SimpleExpression, gen_nuSMV_SetValueParameter_SimpleExpression, gen_nuSMV_SetExpression_SimpleExpression, gen_nuSMV_WordExpression_SimpleExpression, gen_nuSMV_IntervalExpression_SimpleExpression, gen_nuSMV_ValueExpression_SimpleExpression, gen_nuSMV_UnaryFunctionExpression_SimpleExpression, gen_nuSMV_SingleRTCTLExpression_RTCTLExpression, gen_nuSMV_UnaryRTCTLExpression_RTCTLExpression, gen_nuSMV_UntilCTLexpression_SimpleExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)