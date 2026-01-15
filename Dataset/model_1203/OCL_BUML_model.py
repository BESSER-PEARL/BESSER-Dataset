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
CollectionKind: Enumeration = Enumeration(
    name="CollectionKind",
    literals={
            EnumerationLiteral(name="collection"),
			EnumerationLiteral(name="set"),
			EnumerationLiteral(name="orderedSet"),
			EnumerationLiteral(name="bag"),
			EnumerationLiteral(name="sequence")
    }
)

# Classes
ocl_types_AnyType = Class(name="ocl::types::AnyType")
EClassifier = Class(name="EClassifier")
utilities_PredefinedType = Class(name="utilities::PredefinedType")
ocl_types_BagType = Class(name="ocl::types::BagType")
CollectionType = Class(name="CollectionType")
ocl_types_CollectionType = Class(name="ocl::types::CollectionType")
EDataType = Class(name="EDataType")
utilities_TypedASTNode = Class(name="utilities::TypedASTNode")
types_ocl_EClassifier = Class(name="types::ocl::EClassifier")
ocl_types_ElementType = Class(name="ocl::types::ElementType")
EClass = Class(name="EClass")
ocl_types_InvalidType = Class(name="ocl::types::InvalidType")
ocl_types_MessageType = Class(name="ocl::types::MessageType")
types_ocl_EOperation = Class(name="types::ocl::EOperation")
ocl_types_PrimitiveBoolean = Class(name="ocl::types::PrimitiveBoolean")
PrimitiveType = Class(name="PrimitiveType")
ocl_types_PrimitiveInteger = Class(name="ocl::types::PrimitiveInteger")
PrimitiveReal = Class(name="PrimitiveReal")
ocl_types_PrimitiveReal = Class(name="ocl::types::PrimitiveReal")
ocl_types_PrimitiveString = Class(name="ocl::types::PrimitiveString")
ocl_types_PrimitiveType = Class(name="ocl::types::PrimitiveType", is_abstract=True)
ocl_types_SequenceType = Class(name="ocl::types::SequenceType")
ocl_types_SetType = Class(name="ocl::types::SetType")
ocl_types_TupleType = Class(name="ocl::types::TupleType")
ocl_types_TypeType = Class(name="ocl::types::TypeType")
ocl_types_VoidType = Class(name="ocl::types::VoidType")
ocl_expressions_AssociationClassCallExp = Class(name="ocl::expressions::AssociationClassCallExp")
NavigationCallExp = Class(name="NavigationCallExp")
expressions_ocl_EClass = Class(name="expressions::ocl::EClass")
ocl_expressions_BooleanLiteralExp = Class(name="ocl::expressions::BooleanLiteralExp")
PrimitiveLiteralExp = Class(name="PrimitiveLiteralExp")
ocl_expressions_CallExp = Class(name="ocl::expressions::CallExp", is_abstract=True)
expressions_OCLExpression = Class(name="expressions::OCLExpression")
utilities_CallingASTNode = Class(name="utilities::CallingASTNode")
OCLExpression = Class(name="OCLExpression")
ocl_expressions_CollectionItem = Class(name="ocl::expressions::CollectionItem")
CollectionLiteralPart = Class(name="CollectionLiteralPart")
types_ocl_EClass = Class(name="types::ocl::EClass")
ocl_expressions_CollectionLiteralExp = Class(name="ocl::expressions::CollectionLiteralExp")
LiteralExp = Class(name="LiteralExp")
ocl_types_OrderedSetType = Class(name="ocl::types::OrderedSetType")
ocl_expressions_CollectionLiteralPart = Class(name="ocl::expressions::CollectionLiteralPart")
TypedElement = Class(name="TypedElement")
ocl_expressions_CollectionRange = Class(name="ocl::expressions::CollectionRange")
ocl_expressions_EnumLiteralExp = Class(name="ocl::expressions::EnumLiteralExp")
expressions_ocl_EEnumLiteral = Class(name="expressions::ocl::EEnumLiteral")
ocl_expressions_FeatureCallExp = Class(name="ocl::expressions::FeatureCallExp", is_abstract=True)
CallExp = Class(name="CallExp")
ocl_expressions_IfExp = Class(name="ocl::expressions::IfExp")
ocl_expressions_IntegerLiteralExp = Class(name="ocl::expressions::IntegerLiteralExp")
NumericLiteralExp = Class(name="NumericLiteralExp")
ocl_expressions_InvalidLiteralExp = Class(name="ocl::expressions::InvalidLiteralExp")
ocl_expressions_IterateExp = Class(name="ocl::expressions::IterateExp")
LoopExp = Class(name="LoopExp")
Variable = Class(name="Variable")
ocl_expressions_IteratorExp = Class(name="ocl::expressions::IteratorExp")
ocl_expressions_LetExp = Class(name="ocl::expressions::LetExp")
ocl_expressions_LiteralExp = Class(name="ocl::expressions::LiteralExp", is_abstract=True)
ocl_expressions_LoopExp = Class(name="ocl::expressions::LoopExp")
ocl_expressions_MessageExp = Class(name="ocl::expressions::MessageExp")
CallOperationAction = Class(name="CallOperationAction")
SendSignalAction = Class(name="SendSignalAction")
ocl_expressions_NavigationCallExp = Class(name="ocl::expressions::NavigationCallExp", is_abstract=True)
FeatureCallExp = Class(name="FeatureCallExp")
expressions_ocl_EStructuralFeature = Class(name="expressions::ocl::EStructuralFeature")
ocl_expressions_NullLiteralExp = Class(name="ocl::expressions::NullLiteralExp")
ocl_expressions_NumericLiteralExp = Class(name="ocl::expressions::NumericLiteralExp", is_abstract=True)
ocl_expressions_OCLExpression = Class(name="ocl::expressions::OCLExpression", is_abstract=True)
uml_TypedElement = Class(name="uml::TypedElement")
utilities_Visitable = Class(name="utilities::Visitable")
utilities_ASTNode = Class(name="utilities::ASTNode")
ocl_expressions_OperationCallExp = Class(name="ocl::expressions::OperationCallExp")
ocl_expressions_PropertyCallExp = Class(name="ocl::expressions::PropertyCallExp")
ocl_expressions_RealLiteralExp = Class(name="ocl::expressions::RealLiteralExp")
ocl_expressions_StateExp = Class(name="ocl::expressions::StateExp")
expressions_ocl_EObject = Class(name="expressions::ocl::EObject")
ocl_expressions_StringLiteralExp = Class(name="ocl::expressions::StringLiteralExp")
ocl_expressions_TupleLiteralExp = Class(name="ocl::expressions::TupleLiteralExp")
TupleLiteralPart = Class(name="TupleLiteralPart")
ocl_expressions_TupleLiteralPart = Class(name="ocl::expressions::TupleLiteralPart")
ocl_expressions_TypeExp = Class(name="ocl::expressions::TypeExp")
expressions_ocl_EClassifier = Class(name="expressions::ocl::EClassifier")
ocl_expressions_UnspecifiedValueExp = Class(name="ocl::expressions::UnspecifiedValueExp")
ocl_expressions_Variable = Class(name="ocl::expressions::Variable")
expressions_ocl_EParameter = Class(name="expressions::ocl::EParameter")
expressions_ocl_EOperation = Class(name="expressions::ocl::EOperation")
ocl_expressions_PrimitiveLiteralExp = Class(name="ocl::expressions::PrimitiveLiteralExp", is_abstract=True)
ocl_uml_CallOperationAction = Class(name="ocl::uml::CallOperationAction")
uml_ocl_EOperation = Class(name="uml::ocl::EOperation")
ocl_uml_Constraint = Class(name="ocl::uml::Constraint")
ENamedElement = Class(name="ENamedElement")
uml_ocl_ENamedElement = Class(name="uml::ocl::ENamedElement")
ocl_uml_SendSignalAction = Class(name="ocl::uml::SendSignalAction")
uml_ocl_EClass = Class(name="uml::ocl::EClass")
ocl_uml_TypedElement = Class(name="ocl::uml::TypedElement", is_abstract=True)
uml_ocl_EClassifier = Class(name="uml::ocl::EClassifier")
ocl_utilities_ASTNode = Class(name="ocl::utilities::ASTNode", is_abstract=True)
ocl_utilities_CallingASTNode = Class(name="ocl::utilities::CallingASTNode", is_abstract=True)
ASTNode = Class(name="ASTNode")
ocl_utilities_PredefinedType = Class(name="ocl::utilities::PredefinedType", is_abstract=True)
ocl_expressions_VariableExp = Class(name="ocl::expressions::VariableExp")
ocl_utilities_TypedASTNode = Class(name="ocl::utilities::TypedASTNode", is_abstract=True)
ocl_utilities_Visitable = Class(name="ocl::utilities::Visitable")
ocl_query_Query = Class(name="ocl::query::Query")

# ocl_types_AnyType class attributes and methods

# EClassifier class attributes and methods

# utilities_PredefinedType class attributes and methods

# ocl_types_BagType class attributes and methods

# CollectionType class attributes and methods

# ocl_types_CollectionType class attributes and methods
ocl_types_CollectionType_kind: Property = Property(name="kind", type=StringType)
ocl_types_CollectionType.attributes={ocl_types_CollectionType_kind}

# EDataType class attributes and methods

# utilities_TypedASTNode class attributes and methods

# types_ocl_EClassifier class attributes and methods

# ocl_types_ElementType class attributes and methods

# EClass class attributes and methods

# ocl_types_InvalidType class attributes and methods

# ocl_types_MessageType class attributes and methods

# types_ocl_EOperation class attributes and methods

# ocl_types_PrimitiveBoolean class attributes and methods

# PrimitiveType class attributes and methods

# ocl_types_PrimitiveInteger class attributes and methods

# PrimitiveReal class attributes and methods

# ocl_types_PrimitiveReal class attributes and methods

# ocl_types_PrimitiveString class attributes and methods

# ocl_types_PrimitiveType class attributes and methods

# ocl_types_SequenceType class attributes and methods

# ocl_types_SetType class attributes and methods

# ocl_types_TupleType class attributes and methods

# ocl_types_TypeType class attributes and methods

# ocl_types_VoidType class attributes and methods

# ocl_expressions_AssociationClassCallExp class attributes and methods

# NavigationCallExp class attributes and methods

# expressions_ocl_EClass class attributes and methods

# ocl_expressions_BooleanLiteralExp class attributes and methods
ocl_expressions_BooleanLiteralExp_booleanSymbol: Property = Property(name="booleanSymbol", type=StringType)
ocl_expressions_BooleanLiteralExp.attributes={ocl_expressions_BooleanLiteralExp_booleanSymbol}

# PrimitiveLiteralExp class attributes and methods

# ocl_expressions_CallExp class attributes and methods

# expressions_OCLExpression class attributes and methods

# utilities_CallingASTNode class attributes and methods

# OCLExpression class attributes and methods

# ocl_expressions_CollectionItem class attributes and methods

# CollectionLiteralPart class attributes and methods

# types_ocl_EClass class attributes and methods

# ocl_expressions_CollectionLiteralExp class attributes and methods
ocl_expressions_CollectionLiteralExp_kind: Property = Property(name="kind", type=StringType)
ocl_expressions_CollectionLiteralExp.attributes={ocl_expressions_CollectionLiteralExp_kind}

# LiteralExp class attributes and methods

# ocl_types_OrderedSetType class attributes and methods

# ocl_expressions_CollectionLiteralPart class attributes and methods

# TypedElement class attributes and methods

# ocl_expressions_CollectionRange class attributes and methods

# ocl_expressions_EnumLiteralExp class attributes and methods

# expressions_ocl_EEnumLiteral class attributes and methods

# ocl_expressions_FeatureCallExp class attributes and methods
ocl_expressions_FeatureCallExp_markedPre: Property = Property(name="markedPre", type=BooleanType)
ocl_expressions_FeatureCallExp.attributes={ocl_expressions_FeatureCallExp_markedPre}

# CallExp class attributes and methods

# ocl_expressions_IfExp class attributes and methods

# ocl_expressions_IntegerLiteralExp class attributes and methods
ocl_expressions_IntegerLiteralExp_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
ocl_expressions_IntegerLiteralExp.attributes={ocl_expressions_IntegerLiteralExp_integerSymbol}

# NumericLiteralExp class attributes and methods

# ocl_expressions_InvalidLiteralExp class attributes and methods

# ocl_expressions_IterateExp class attributes and methods

# LoopExp class attributes and methods

# Variable class attributes and methods

# ocl_expressions_IteratorExp class attributes and methods

# ocl_expressions_LetExp class attributes and methods

# ocl_expressions_LiteralExp class attributes and methods

# ocl_expressions_LoopExp class attributes and methods

# ocl_expressions_MessageExp class attributes and methods

# CallOperationAction class attributes and methods

# SendSignalAction class attributes and methods

# ocl_expressions_NavigationCallExp class attributes and methods

# FeatureCallExp class attributes and methods

# expressions_ocl_EStructuralFeature class attributes and methods

# ocl_expressions_NullLiteralExp class attributes and methods

# ocl_expressions_NumericLiteralExp class attributes and methods

# ocl_expressions_OCLExpression class attributes and methods

# uml_TypedElement class attributes and methods

# utilities_Visitable class attributes and methods

# utilities_ASTNode class attributes and methods

# ocl_expressions_OperationCallExp class attributes and methods

# ocl_expressions_PropertyCallExp class attributes and methods

# ocl_expressions_RealLiteralExp class attributes and methods
ocl_expressions_RealLiteralExp_realSymbol: Property = Property(name="realSymbol", type=StringType)
ocl_expressions_RealLiteralExp.attributes={ocl_expressions_RealLiteralExp_realSymbol}

# ocl_expressions_StateExp class attributes and methods

# expressions_ocl_EObject class attributes and methods

# ocl_expressions_StringLiteralExp class attributes and methods
ocl_expressions_StringLiteralExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
ocl_expressions_StringLiteralExp.attributes={ocl_expressions_StringLiteralExp_stringSymbol}

# ocl_expressions_TupleLiteralExp class attributes and methods

# TupleLiteralPart class attributes and methods

# ocl_expressions_TupleLiteralPart class attributes and methods

# ocl_expressions_TypeExp class attributes and methods

# expressions_ocl_EClassifier class attributes and methods

# ocl_expressions_UnspecifiedValueExp class attributes and methods

# ocl_expressions_Variable class attributes and methods

# expressions_ocl_EParameter class attributes and methods

# expressions_ocl_EOperation class attributes and methods

# ocl_expressions_PrimitiveLiteralExp class attributes and methods

# ocl_uml_CallOperationAction class attributes and methods

# uml_ocl_EOperation class attributes and methods

# ocl_uml_Constraint class attributes and methods
ocl_uml_Constraint_instanceVarName: Property = Property(name="instanceVarName", type=StringType)
ocl_uml_Constraint_stereotype: Property = Property(name="stereotype", type=StringType)
ocl_uml_Constraint.attributes={ocl_uml_Constraint_stereotype, ocl_uml_Constraint_instanceVarName}

# ENamedElement class attributes and methods

# uml_ocl_ENamedElement class attributes and methods

# ocl_uml_SendSignalAction class attributes and methods

# uml_ocl_EClass class attributes and methods

# ocl_uml_TypedElement class attributes and methods

# uml_ocl_EClassifier class attributes and methods

# ocl_utilities_ASTNode class attributes and methods
ocl_utilities_ASTNode_startPosition: Property = Property(name="startPosition", type=IntegerType)
ocl_utilities_ASTNode_endPosition: Property = Property(name="endPosition", type=IntegerType)
ocl_utilities_ASTNode.attributes={ocl_utilities_ASTNode_startPosition, ocl_utilities_ASTNode_endPosition}

# ocl_utilities_CallingASTNode class attributes and methods
ocl_utilities_CallingASTNode_propertyStartPosition: Property = Property(name="propertyStartPosition", type=IntegerType)
ocl_utilities_CallingASTNode_propertyEndPosition: Property = Property(name="propertyEndPosition", type=IntegerType)
ocl_utilities_CallingASTNode.attributes={ocl_utilities_CallingASTNode_propertyStartPosition, ocl_utilities_CallingASTNode_propertyEndPosition}

# ASTNode class attributes and methods

# ocl_utilities_PredefinedType class attributes and methods
ocl_utilities_PredefinedType_m_getResultTypeFor: Method = Method(name="getResultTypeFor", parameters={Parameter(name='opcode'), Parameter(name='args'), Parameter(name='ownerType')}, type=EClassifier)
ocl_utilities_PredefinedType_m_getOperations: Method = Method(name="getOperations", parameters={}, type=StringType)
ocl_utilities_PredefinedType_m_getOperationNameFor: Method = Method(name="getOperationNameFor", parameters={Parameter(name='opcode')}, type=StringType)
ocl_utilities_PredefinedType_m_getOperationCodeFor: Method = Method(name="getOperationCodeFor", parameters={Parameter(name='operName')}, type=IntegerType)
ocl_utilities_PredefinedType_m_getRelationshipTo: Method = Method(name="getRelationshipTo", parameters={Parameter(name='type')}, type=IntegerType)
ocl_utilities_PredefinedType_m_getCommonSupertype: Method = Method(name="getCommonSupertype", parameters={Parameter(name='type')}, type=EClassifier)
ocl_utilities_PredefinedType.methods={ocl_utilities_PredefinedType_m_getOperations, ocl_utilities_PredefinedType_m_getCommonSupertype, ocl_utilities_PredefinedType_m_getRelationshipTo, ocl_utilities_PredefinedType_m_getOperationCodeFor, ocl_utilities_PredefinedType_m_getResultTypeFor, ocl_utilities_PredefinedType_m_getOperationNameFor}

# ocl_expressions_VariableExp class attributes and methods

# ocl_utilities_TypedASTNode class attributes and methods
ocl_utilities_TypedASTNode_typeStartPosition: Property = Property(name="typeStartPosition", type=IntegerType)
ocl_utilities_TypedASTNode_typeEndPosition: Property = Property(name="typeEndPosition", type=IntegerType)
ocl_utilities_TypedASTNode.attributes={ocl_utilities_TypedASTNode_typeStartPosition, ocl_utilities_TypedASTNode_typeEndPosition}

# ocl_utilities_Visitable class attributes and methods
ocl_utilities_Visitable_m_accept: Method = Method(name="accept", parameters={Parameter(name='v')}, type=StringType)
ocl_utilities_Visitable.methods={ocl_utilities_Visitable_m_accept}

# ocl_query_Query class attributes and methods
ocl_query_Query_extentMap: Property = Property(name="extentMap", type=StringType)
ocl_query_Query_m_evaluate: Method = Method(name="evaluate", parameters={Parameter(name='obj')}, type=StringType)
ocl_query_Query_m_evaluate: Method = Method(name="evaluate", parameters={}, type=StringType)
ocl_query_Query_m_check: Method = Method(name="check", parameters={Parameter(name='obj')}, type=BooleanType)
ocl_query_Query_m_evaluate: Method = Method(name="evaluate", parameters={Parameter(name='objects')}, type=StringType)
ocl_query_Query_m_check: Method = Method(name="check", parameters={Parameter(name='objects')}, type=BooleanType)
ocl_query_Query_m_select: Method = Method(name="select", parameters={Parameter(name='objects')}, type=StringType)
ocl_query_Query_m_reject: Method = Method(name="reject", parameters={Parameter(name='objects')}, type=StringType)
ocl_query_Query_m_resultType: Method = Method(name="resultType", parameters={}, type=EClassifier)
ocl_query_Query_m_queryText: Method = Method(name="queryText", parameters={}, type=StringType)
ocl_query_Query.attributes={ocl_query_Query_extentMap}
ocl_query_Query.methods={ocl_query_Query_m_reject, ocl_query_Query_m_select, ocl_query_Query_m_evaluate, ocl_query_Query_m_resultType, ocl_query_Query_m_evaluate, ocl_query_Query_m_check, ocl_query_Query_m_evaluate, ocl_query_Query_m_queryText, ocl_query_Query_m_check}

# Relationships
elementType0: BinaryAssociation = BinaryAssociation(
    name="elementType0",
    ends={
        Property(name="types_ocl_EClassifier", type=ocl_types_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_types_CollectionType", type=types_ocl_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
referredOperation1: BinaryAssociation = BinaryAssociation(
    name="referredOperation1",
    ends={
        Property(name="types_ocl_EOperation", type=ocl_types_MessageType, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_types_MessageType", type=types_ocl_EOperation, multiplicity=Multiplicity(0, 1))
    }
)
part8: BinaryAssociation = BinaryAssociation(
    name="part8",
    ends={
        Property(name="CollectionLiteralPart", type=ocl_expressions_CollectionLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_expressions_CollectionLiteralExp", type=CollectionLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredAssociationClass4: BinaryAssociation = BinaryAssociation(
    name="referredAssociationClass4",
    ends={
        Property(name="expressions_ocl_EClass", type=ocl_expressions_AssociationClassCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_expressions_AssociationClassCallExp", type=expressions_ocl_EClass, multiplicity=Multiplicity(0, 1))
    }
)
source5: BinaryAssociation = BinaryAssociation(
    name="source5",
    ends={
        Property(name="OCLExpression", type=ocl_expressions_CallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_expressions_CallExp", type=OCLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
item6: BinaryAssociation = BinaryAssociation(
    name="item6",
    ends={
        Property(name="OCLExpression7", type=ocl_expressions_CollectionItem, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_expressions_CollectionItem", type=OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referredSignal2: BinaryAssociation = BinaryAssociation(
    name="referredSignal2",
    ends={
        Property(name="types_ocl_EClass", type=ocl_types_MessageType, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_types_MessageType3", type=types_ocl_EClass, multiplicity=Multiplicity(0, 1))
    }
)
first9: BinaryAssociation = BinaryAssociation(
    name="first9",
    ends={
        Property(name="OCLExpression10", type=ocl_expressions_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_expressions_CollectionRange", type=OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
last11: BinaryAssociation = BinaryAssociation(
    name="last11",
    ends={
        Property(name="OCLExpression13", type=ocl_expressions_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_expressions_CollectionRange12", type=OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referredEnumLiteral14: BinaryAssociation = BinaryAssociation(
    name="referredEnumLiteral14",
    ends={
        Property(name="expressions_ocl_EEnumLiteral", type=ocl_expressions_EnumLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_expressions_EnumLiteralExp", type=expressions_ocl_EEnumLiteral, multiplicity=Multiplicity(0, 1))
    }
)
condition15: BinaryAssociation = BinaryAssociation(
    name="condition15",
    ends={
        Property(name="OCLExpression16", type=ocl_expressions_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_expressions_IfExp", type=OCLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenExpression17: BinaryAssociation = BinaryAssociation(
    name="thenExpression17",
    ends={
        Property(name="OCLExpression19", type=ocl_expressions_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_expressions_IfExp18", type=OCLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseExpression20: BinaryAssociation = BinaryAssociation(
    name="elseExpression20",
    ends={
        Property(name="OCLExpression22", type=ocl_expressions_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_expressions_IfExp21", type=OCLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result23: BinaryAssociation = BinaryAssociation(
    name="result23",
    ends={
        Property(name="Variable", type=ocl_expressions_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_expressions_IterateExp", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
in24: BinaryAssociation = BinaryAssociation(
    name="in24",
    ends={
        Property(name="OCLExpression25", type=ocl_expressions_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_expressions_LetExp", type=OCLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body29: BinaryAssociation = BinaryAssociation(
    name="body29",
    ends={
        Property(name="OCLExpression30", type=ocl_expressions_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_expressions_LoopExp", type=OCLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
iterator31: BinaryAssociation = BinaryAssociation(
    name="iterator31",
    ends={
        Property(name="Variable33", type=ocl_expressions_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_expressions_LoopExp32", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target34: BinaryAssociation = BinaryAssociation(
    name="target34",
    ends={
        Property(name="OCLExpression35", type=ocl_expressions_MessageExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_expressions_MessageExp", type=OCLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
argument36: BinaryAssociation = BinaryAssociation(
    name="argument36",
    ends={
        Property(name="OCLExpression38", type=ocl_expressions_MessageExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_expressions_MessageExp37", type=OCLExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calledOperation39: BinaryAssociation = BinaryAssociation(
    name="calledOperation39",
    ends={
        Property(name="CallOperationAction", type=ocl_expressions_MessageExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_expressions_MessageExp40", type=CallOperationAction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sentSignal41: BinaryAssociation = BinaryAssociation(
    name="sentSignal41",
    ends={
        Property(name="SendSignalAction", type=ocl_expressions_MessageExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_expressions_MessageExp42", type=SendSignalAction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifier43: BinaryAssociation = BinaryAssociation(
    name="qualifier43",
    ends={
        Property(name="OCLExpression44", type=ocl_expressions_NavigationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_expressions_NavigationCallExp", type=OCLExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
navigationSource45: BinaryAssociation = BinaryAssociation(
    name="navigationSource45",
    ends={
        Property(name="expressions_ocl_EStructuralFeature", type=ocl_expressions_NavigationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_expressions_NavigationCallExp46", type=expressions_ocl_EStructuralFeature, multiplicity=Multiplicity(0, 1))
    }
)
argument47: BinaryAssociation = BinaryAssociation(
    name="argument47",
    ends={
        Property(name="OCLExpression48", type=ocl_expressions_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_expressions_OperationCallExp", type=OCLExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable26: BinaryAssociation = BinaryAssociation(
    name="variable26",
    ends={
        Property(name="Variable28", type=ocl_expressions_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_expressions_LetExp27", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referredProperty51: BinaryAssociation = BinaryAssociation(
    name="referredProperty51",
    ends={
        Property(name="expressions_ocl_EStructuralFeature52", type=ocl_expressions_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_expressions_PropertyCallExp", type=expressions_ocl_EStructuralFeature, multiplicity=Multiplicity(0, 1))
    }
)
referredState53: BinaryAssociation = BinaryAssociation(
    name="referredState53",
    ends={
        Property(name="expressions_ocl_EObject", type=ocl_expressions_StateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_expressions_StateExp", type=expressions_ocl_EObject, multiplicity=Multiplicity(0, 1))
    }
)
part54: BinaryAssociation = BinaryAssociation(
    name="part54",
    ends={
        Property(name="TupleLiteralPart", type=ocl_expressions_TupleLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_expressions_TupleLiteralExp", type=TupleLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value55: BinaryAssociation = BinaryAssociation(
    name="value55",
    ends={
        Property(name="OCLExpression56", type=ocl_expressions_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_expressions_TupleLiteralPart", type=OCLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attribute57: BinaryAssociation = BinaryAssociation(
    name="attribute57",
    ends={
        Property(name="expressions_ocl_EStructuralFeature59", type=ocl_expressions_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_expressions_TupleLiteralPart58", type=expressions_ocl_EStructuralFeature, multiplicity=Multiplicity(0, 1))
    }
)
referredType60: BinaryAssociation = BinaryAssociation(
    name="referredType60",
    ends={
        Property(name="expressions_ocl_EClassifier", type=ocl_expressions_TypeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_expressions_TypeExp", type=expressions_ocl_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
initExpression61: BinaryAssociation = BinaryAssociation(
    name="initExpression61",
    ends={
        Property(name="OCLExpression62", type=ocl_expressions_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_expressions_Variable", type=OCLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
representedParameter63: BinaryAssociation = BinaryAssociation(
    name="representedParameter63",
    ends={
        Property(name="expressions_ocl_EParameter", type=ocl_expressions_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_expressions_Variable64", type=expressions_ocl_EParameter, multiplicity=Multiplicity(0, 1))
    }
)
referredOperation49: BinaryAssociation = BinaryAssociation(
    name="referredOperation49",
    ends={
        Property(name="expressions_ocl_EOperation", type=ocl_expressions_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_expressions_OperationCallExp50", type=expressions_ocl_EOperation, multiplicity=Multiplicity(0, 1))
    }
)
operation67: BinaryAssociation = BinaryAssociation(
    name="operation67",
    ends={
        Property(name="uml_ocl_EOperation", type=ocl_uml_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_uml_CallOperationAction", type=uml_ocl_EOperation, multiplicity=Multiplicity(1, 1))
    }
)
body68: BinaryAssociation = BinaryAssociation(
    name="body68",
    ends={
        Property(name="OCLExpression69", type=ocl_uml_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_uml_Constraint", type=OCLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constrainedElement70: BinaryAssociation = BinaryAssociation(
    name="constrainedElement70",
    ends={
        Property(name="uml_ocl_ENamedElement", type=ocl_uml_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_uml_Constraint71", type=uml_ocl_ENamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
signal72: BinaryAssociation = BinaryAssociation(
    name="signal72",
    ends={
        Property(name="uml_ocl_EClass", type=ocl_uml_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_uml_SendSignalAction", type=uml_ocl_EClass, multiplicity=Multiplicity(1, 1))
    }
)
type73: BinaryAssociation = BinaryAssociation(
    name="type73",
    ends={
        Property(name="uml_ocl_EClassifier", type=ocl_uml_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_uml_TypedElement", type=uml_ocl_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
referredVariable65: BinaryAssociation = BinaryAssociation(
    name="referredVariable65",
    ends={
        Property(name="Variable66", type=ocl_expressions_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_expressions_VariableExp", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
expression74: BinaryAssociation = BinaryAssociation(
    name="expression74",
    ends={
        Property(name="OCLExpression75", type=ocl_query_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_query_Query", type=OCLExpression, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_ocl_types_AnyType_EClassifier = Generalization(general=EClassifier, specific=ocl_types_AnyType)
gen_ocl_types_AnyType_utilities_PredefinedType = Generalization(general=utilities_PredefinedType, specific=ocl_types_AnyType)
gen_ocl_types_BagType_CollectionType = Generalization(general=CollectionType, specific=ocl_types_BagType)
gen_ocl_types_CollectionType_EDataType = Generalization(general=EDataType, specific=ocl_types_CollectionType)
gen_ocl_types_CollectionType_utilities_TypedASTNode = Generalization(general=utilities_TypedASTNode, specific=ocl_types_CollectionType)
gen_ocl_types_CollectionType_utilities_PredefinedType = Generalization(general=utilities_PredefinedType, specific=ocl_types_CollectionType)
gen_ocl_types_ElementType_EClass = Generalization(general=EClass, specific=ocl_types_ElementType)
gen_ocl_types_InvalidType_EClassifier = Generalization(general=EClassifier, specific=ocl_types_InvalidType)
gen_ocl_types_InvalidType_utilities_PredefinedType = Generalization(general=utilities_PredefinedType, specific=ocl_types_InvalidType)
gen_ocl_types_MessageType_EClass = Generalization(general=EClass, specific=ocl_types_MessageType)
gen_ocl_types_MessageType_utilities_PredefinedType = Generalization(general=utilities_PredefinedType, specific=ocl_types_MessageType)
gen_ocl_types_PrimitiveBoolean_PrimitiveType = Generalization(general=PrimitiveType, specific=ocl_types_PrimitiveBoolean)
gen_ocl_types_PrimitiveInteger_PrimitiveReal = Generalization(general=PrimitiveReal, specific=ocl_types_PrimitiveInteger)
gen_ocl_types_PrimitiveReal_PrimitiveType = Generalization(general=PrimitiveType, specific=ocl_types_PrimitiveReal)
gen_ocl_types_PrimitiveString_PrimitiveType = Generalization(general=PrimitiveType, specific=ocl_types_PrimitiveString)
gen_ocl_types_PrimitiveType_EDataType = Generalization(general=EDataType, specific=ocl_types_PrimitiveType)
gen_ocl_types_PrimitiveType_utilities_PredefinedType = Generalization(general=utilities_PredefinedType, specific=ocl_types_PrimitiveType)
gen_ocl_types_SequenceType_CollectionType = Generalization(general=CollectionType, specific=ocl_types_SequenceType)
gen_ocl_types_SetType_CollectionType = Generalization(general=CollectionType, specific=ocl_types_SetType)
gen_ocl_types_TupleType_EClass = Generalization(general=EClass, specific=ocl_types_TupleType)
gen_ocl_types_TypeType_EClassifier = Generalization(general=EClassifier, specific=ocl_types_TypeType)
gen_ocl_types_TypeType_utilities_PredefinedType = Generalization(general=utilities_PredefinedType, specific=ocl_types_TypeType)
gen_ocl_types_VoidType_EClassifier = Generalization(general=EClassifier, specific=ocl_types_VoidType)
gen_ocl_types_VoidType_utilities_PredefinedType = Generalization(general=utilities_PredefinedType, specific=ocl_types_VoidType)
gen_ocl_expressions_AssociationClassCallExp_NavigationCallExp = Generalization(general=NavigationCallExp, specific=ocl_expressions_AssociationClassCallExp)
gen_ocl_expressions_BooleanLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=ocl_expressions_BooleanLiteralExp)
gen_ocl_expressions_CallExp_expressions_OCLExpression = Generalization(general=expressions_OCLExpression, specific=ocl_expressions_CallExp)
gen_ocl_expressions_CallExp_utilities_CallingASTNode = Generalization(general=utilities_CallingASTNode, specific=ocl_expressions_CallExp)
gen_ocl_expressions_CollectionItem_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=ocl_expressions_CollectionItem)
gen_ocl_expressions_CollectionLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=ocl_expressions_CollectionLiteralExp)
gen_ocl_types_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=ocl_types_OrderedSetType)
gen_ocl_expressions_CollectionLiteralPart_TypedElement = Generalization(general=TypedElement, specific=ocl_expressions_CollectionLiteralPart)
gen_ocl_expressions_CollectionRange_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=ocl_expressions_CollectionRange)
gen_ocl_expressions_EnumLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=ocl_expressions_EnumLiteralExp)
gen_ocl_expressions_FeatureCallExp_CallExp = Generalization(general=CallExp, specific=ocl_expressions_FeatureCallExp)
gen_ocl_expressions_IfExp_OCLExpression = Generalization(general=OCLExpression, specific=ocl_expressions_IfExp)
gen_ocl_expressions_IntegerLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=ocl_expressions_IntegerLiteralExp)
gen_ocl_expressions_InvalidLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=ocl_expressions_InvalidLiteralExp)
gen_ocl_expressions_IterateExp_LoopExp = Generalization(general=LoopExp, specific=ocl_expressions_IterateExp)
gen_ocl_expressions_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=ocl_expressions_IteratorExp)
gen_ocl_expressions_LetExp_OCLExpression = Generalization(general=OCLExpression, specific=ocl_expressions_LetExp)
gen_ocl_expressions_LiteralExp_OCLExpression = Generalization(general=OCLExpression, specific=ocl_expressions_LiteralExp)
gen_ocl_expressions_LoopExp_CallExp = Generalization(general=CallExp, specific=ocl_expressions_LoopExp)
gen_ocl_expressions_MessageExp_expressions_OCLExpression = Generalization(general=expressions_OCLExpression, specific=ocl_expressions_MessageExp)
gen_ocl_expressions_MessageExp_utilities_CallingASTNode = Generalization(general=utilities_CallingASTNode, specific=ocl_expressions_MessageExp)
gen_ocl_expressions_NavigationCallExp_FeatureCallExp = Generalization(general=FeatureCallExp, specific=ocl_expressions_NavigationCallExp)
gen_ocl_expressions_NullLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=ocl_expressions_NullLiteralExp)
gen_ocl_expressions_NumericLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=ocl_expressions_NumericLiteralExp)
gen_ocl_expressions_OCLExpression_uml_TypedElement = Generalization(general=uml_TypedElement, specific=ocl_expressions_OCLExpression)
gen_ocl_expressions_OCLExpression_utilities_Visitable = Generalization(general=utilities_Visitable, specific=ocl_expressions_OCLExpression)
gen_ocl_expressions_OCLExpression_utilities_ASTNode = Generalization(general=utilities_ASTNode, specific=ocl_expressions_OCLExpression)
gen_ocl_expressions_OperationCallExp_FeatureCallExp = Generalization(general=FeatureCallExp, specific=ocl_expressions_OperationCallExp)
gen_ocl_expressions_PrimitiveLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=ocl_expressions_PrimitiveLiteralExp)
gen_ocl_expressions_PropertyCallExp_NavigationCallExp = Generalization(general=NavigationCallExp, specific=ocl_expressions_PropertyCallExp)
gen_ocl_expressions_RealLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=ocl_expressions_RealLiteralExp)
gen_ocl_expressions_StateExp_OCLExpression = Generalization(general=OCLExpression, specific=ocl_expressions_StateExp)
gen_ocl_expressions_StringLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=ocl_expressions_StringLiteralExp)
gen_ocl_expressions_TupleLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=ocl_expressions_TupleLiteralExp)
gen_ocl_expressions_TupleLiteralPart_uml_TypedElement = Generalization(general=uml_TypedElement, specific=ocl_expressions_TupleLiteralPart)
gen_ocl_expressions_TupleLiteralPart_utilities_Visitable = Generalization(general=utilities_Visitable, specific=ocl_expressions_TupleLiteralPart)
gen_ocl_expressions_TupleLiteralPart_utilities_TypedASTNode = Generalization(general=utilities_TypedASTNode, specific=ocl_expressions_TupleLiteralPart)
gen_ocl_expressions_TypeExp_OCLExpression = Generalization(general=OCLExpression, specific=ocl_expressions_TypeExp)
gen_ocl_expressions_UnspecifiedValueExp_expressions_OCLExpression = Generalization(general=expressions_OCLExpression, specific=ocl_expressions_UnspecifiedValueExp)
gen_ocl_expressions_UnspecifiedValueExp_utilities_TypedASTNode = Generalization(general=utilities_TypedASTNode, specific=ocl_expressions_UnspecifiedValueExp)
gen_ocl_expressions_Variable_uml_TypedElement = Generalization(general=uml_TypedElement, specific=ocl_expressions_Variable)
gen_ocl_expressions_Variable_utilities_Visitable = Generalization(general=utilities_Visitable, specific=ocl_expressions_Variable)
gen_ocl_expressions_Variable_utilities_TypedASTNode = Generalization(general=utilities_TypedASTNode, specific=ocl_expressions_Variable)
gen_ocl_uml_Constraint_ENamedElement = Generalization(general=ENamedElement, specific=ocl_uml_Constraint)
gen_ocl_uml_Constraint_utilities_Visitable = Generalization(general=utilities_Visitable, specific=ocl_uml_Constraint)
gen_ocl_uml_TypedElement_ENamedElement = Generalization(general=ENamedElement, specific=ocl_uml_TypedElement)
gen_ocl_utilities_CallingASTNode_ASTNode = Generalization(general=ASTNode, specific=ocl_utilities_CallingASTNode)
gen_ocl_expressions_VariableExp_OCLExpression = Generalization(general=OCLExpression, specific=ocl_expressions_VariableExp)
gen_ocl_utilities_TypedASTNode_ASTNode = Generalization(general=ASTNode, specific=ocl_utilities_TypedASTNode)

# Domain Model
domain_model = DomainModel(
    name="ocl",
    types={ocl_types_AnyType, EClassifier, utilities_PredefinedType, ocl_types_BagType, CollectionType, ocl_types_CollectionType, EDataType, utilities_TypedASTNode, types_ocl_EClassifier, ocl_types_ElementType, EClass, ocl_types_InvalidType, ocl_types_MessageType, types_ocl_EOperation, ocl_types_PrimitiveBoolean, PrimitiveType, ocl_types_PrimitiveInteger, PrimitiveReal, ocl_types_PrimitiveReal, ocl_types_PrimitiveString, ocl_types_PrimitiveType, ocl_types_SequenceType, ocl_types_SetType, ocl_types_TupleType, ocl_types_TypeType, ocl_types_VoidType, ocl_expressions_AssociationClassCallExp, NavigationCallExp, expressions_ocl_EClass, ocl_expressions_BooleanLiteralExp, PrimitiveLiteralExp, ocl_expressions_CallExp, expressions_OCLExpression, utilities_CallingASTNode, OCLExpression, ocl_expressions_CollectionItem, CollectionLiteralPart, types_ocl_EClass, ocl_expressions_CollectionLiteralExp, LiteralExp, ocl_types_OrderedSetType, ocl_expressions_CollectionLiteralPart, TypedElement, ocl_expressions_CollectionRange, ocl_expressions_EnumLiteralExp, expressions_ocl_EEnumLiteral, ocl_expressions_FeatureCallExp, CallExp, ocl_expressions_IfExp, ocl_expressions_IntegerLiteralExp, NumericLiteralExp, ocl_expressions_InvalidLiteralExp, ocl_expressions_IterateExp, LoopExp, Variable, ocl_expressions_IteratorExp, ocl_expressions_LetExp, ocl_expressions_LiteralExp, ocl_expressions_LoopExp, ocl_expressions_MessageExp, CallOperationAction, SendSignalAction, ocl_expressions_NavigationCallExp, FeatureCallExp, expressions_ocl_EStructuralFeature, ocl_expressions_NullLiteralExp, ocl_expressions_NumericLiteralExp, ocl_expressions_OCLExpression, uml_TypedElement, utilities_Visitable, utilities_ASTNode, ocl_expressions_OperationCallExp, ocl_expressions_PropertyCallExp, ocl_expressions_RealLiteralExp, ocl_expressions_StateExp, expressions_ocl_EObject, ocl_expressions_StringLiteralExp, ocl_expressions_TupleLiteralExp, TupleLiteralPart, ocl_expressions_TupleLiteralPart, ocl_expressions_TypeExp, expressions_ocl_EClassifier, ocl_expressions_UnspecifiedValueExp, ocl_expressions_Variable, expressions_ocl_EParameter, expressions_ocl_EOperation, ocl_expressions_PrimitiveLiteralExp, ocl_uml_CallOperationAction, uml_ocl_EOperation, ocl_uml_Constraint, ENamedElement, uml_ocl_ENamedElement, ocl_uml_SendSignalAction, uml_ocl_EClass, ocl_uml_TypedElement, uml_ocl_EClassifier, ocl_utilities_ASTNode, ocl_utilities_CallingASTNode, ASTNode, ocl_utilities_PredefinedType, ocl_expressions_VariableExp, ocl_utilities_TypedASTNode, ocl_utilities_Visitable, ocl_query_Query, CollectionKind},
    associations={elementType0, referredOperation1, part8, referredAssociationClass4, source5, item6, referredSignal2, first9, last11, referredEnumLiteral14, condition15, thenExpression17, elseExpression20, result23, in24, body29, iterator31, target34, argument36, calledOperation39, sentSignal41, qualifier43, navigationSource45, argument47, variable26, referredProperty51, referredState53, part54, value55, attribute57, referredType60, initExpression61, representedParameter63, referredOperation49, operation67, body68, constrainedElement70, signal72, type73, referredVariable65, expression74},
    generalizations={gen_ocl_types_AnyType_EClassifier, gen_ocl_types_AnyType_utilities_PredefinedType, gen_ocl_types_BagType_CollectionType, gen_ocl_types_CollectionType_EDataType, gen_ocl_types_CollectionType_utilities_TypedASTNode, gen_ocl_types_CollectionType_utilities_PredefinedType, gen_ocl_types_ElementType_EClass, gen_ocl_types_InvalidType_EClassifier, gen_ocl_types_InvalidType_utilities_PredefinedType, gen_ocl_types_MessageType_EClass, gen_ocl_types_MessageType_utilities_PredefinedType, gen_ocl_types_PrimitiveBoolean_PrimitiveType, gen_ocl_types_PrimitiveInteger_PrimitiveReal, gen_ocl_types_PrimitiveReal_PrimitiveType, gen_ocl_types_PrimitiveString_PrimitiveType, gen_ocl_types_PrimitiveType_EDataType, gen_ocl_types_PrimitiveType_utilities_PredefinedType, gen_ocl_types_SequenceType_CollectionType, gen_ocl_types_SetType_CollectionType, gen_ocl_types_TupleType_EClass, gen_ocl_types_TypeType_EClassifier, gen_ocl_types_TypeType_utilities_PredefinedType, gen_ocl_types_VoidType_EClassifier, gen_ocl_types_VoidType_utilities_PredefinedType, gen_ocl_expressions_AssociationClassCallExp_NavigationCallExp, gen_ocl_expressions_BooleanLiteralExp_PrimitiveLiteralExp, gen_ocl_expressions_CallExp_expressions_OCLExpression, gen_ocl_expressions_CallExp_utilities_CallingASTNode, gen_ocl_expressions_CollectionItem_CollectionLiteralPart, gen_ocl_expressions_CollectionLiteralExp_LiteralExp, gen_ocl_types_OrderedSetType_CollectionType, gen_ocl_expressions_CollectionLiteralPart_TypedElement, gen_ocl_expressions_CollectionRange_CollectionLiteralPart, gen_ocl_expressions_EnumLiteralExp_LiteralExp, gen_ocl_expressions_FeatureCallExp_CallExp, gen_ocl_expressions_IfExp_OCLExpression, gen_ocl_expressions_IntegerLiteralExp_NumericLiteralExp, gen_ocl_expressions_InvalidLiteralExp_LiteralExp, gen_ocl_expressions_IterateExp_LoopExp, gen_ocl_expressions_IteratorExp_LoopExp, gen_ocl_expressions_LetExp_OCLExpression, gen_ocl_expressions_LiteralExp_OCLExpression, gen_ocl_expressions_LoopExp_CallExp, gen_ocl_expressions_MessageExp_expressions_OCLExpression, gen_ocl_expressions_MessageExp_utilities_CallingASTNode, gen_ocl_expressions_NavigationCallExp_FeatureCallExp, gen_ocl_expressions_NullLiteralExp_LiteralExp, gen_ocl_expressions_NumericLiteralExp_PrimitiveLiteralExp, gen_ocl_expressions_OCLExpression_uml_TypedElement, gen_ocl_expressions_OCLExpression_utilities_Visitable, gen_ocl_expressions_OCLExpression_utilities_ASTNode, gen_ocl_expressions_OperationCallExp_FeatureCallExp, gen_ocl_expressions_PrimitiveLiteralExp_LiteralExp, gen_ocl_expressions_PropertyCallExp_NavigationCallExp, gen_ocl_expressions_RealLiteralExp_NumericLiteralExp, gen_ocl_expressions_StateExp_OCLExpression, gen_ocl_expressions_StringLiteralExp_PrimitiveLiteralExp, gen_ocl_expressions_TupleLiteralExp_LiteralExp, gen_ocl_expressions_TupleLiteralPart_uml_TypedElement, gen_ocl_expressions_TupleLiteralPart_utilities_Visitable, gen_ocl_expressions_TupleLiteralPart_utilities_TypedASTNode, gen_ocl_expressions_TypeExp_OCLExpression, gen_ocl_expressions_UnspecifiedValueExp_expressions_OCLExpression, gen_ocl_expressions_UnspecifiedValueExp_utilities_TypedASTNode, gen_ocl_expressions_Variable_uml_TypedElement, gen_ocl_expressions_Variable_utilities_Visitable, gen_ocl_expressions_Variable_utilities_TypedASTNode, gen_ocl_uml_Constraint_ENamedElement, gen_ocl_uml_Constraint_utilities_Visitable, gen_ocl_uml_TypedElement_ENamedElement, gen_ocl_utilities_CallingASTNode_ASTNode, gen_ocl_expressions_VariableExp_OCLExpression, gen_ocl_utilities_TypedASTNode_ASTNode},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)