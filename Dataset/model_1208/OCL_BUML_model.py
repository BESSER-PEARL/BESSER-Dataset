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
            EnumerationLiteral(name="Set"),
			EnumerationLiteral(name="OrderedSet"),
			EnumerationLiteral(name="Bag"),
			EnumerationLiteral(name="Sequence"),
			EnumerationLiteral(name="Collection")
    }
)

# Classes
ocl_types_AnyType = Class(name="ocl::types::AnyType")
ocl_types_BagType = Class(name="ocl::types::BagType")
ocl_types_ElementType = Class(name="ocl::types::ElementType")
ocl_types_InvalidType = Class(name="ocl::types::InvalidType")
ocl_types_MessageType = Class(name="ocl::types::MessageType")
ocl_types_CollectionType = Class(name="ocl::types::CollectionType")
ocl_types_PrimitiveType = Class(name="ocl::types::PrimitiveType")
ocl_types_SequenceType = Class(name="ocl::types::SequenceType")
ocl_types_SetType = Class(name="ocl::types::SetType")
ocl_types_OrderedSetType = Class(name="ocl::types::OrderedSetType")
ocl_types_TypeType = Class(name="ocl::types::TypeType")
ocl_types_TemplateParameterType = Class(name="ocl::types::TemplateParameterType")
ocl_types_TupleType = Class(name="ocl::types::TupleType")
ocl_utilities_Visitor = Class(name="ocl::utilities::Visitor", is_abstract=True)
ocl_types_VoidType = Class(name="ocl::types::VoidType")
ocl_utilities_ASTNode = Class(name="ocl::utilities::ASTNode", is_abstract=True)
ocl_utilities_CallingASTNode = Class(name="ocl::utilities::CallingASTNode", is_abstract=True)
ASTNode = Class(name="ASTNode")
ocl_utilities_TypedASTNode = Class(name="ocl::utilities::TypedASTNode", is_abstract=True)
ocl_utilities_Visitable = Class(name="ocl::utilities::Visitable", is_abstract=True)
ocl_utilities_TypedElement = Class(name="ocl::utilities::TypedElement", is_abstract=True)
ocl_expressions_AssociationClassCallExp = Class(name="ocl::expressions::AssociationClassCallExp")
ocl_expressions_NavigationCallExp = Class(name="ocl::expressions::NavigationCallExp", is_abstract=True)
ocl_expressions_FeatureCallExp = Class(name="ocl::expressions::FeatureCallExp", is_abstract=True)
ocl_expressions_CallExp = Class(name="ocl::expressions::CallExp", is_abstract=True)
ocl_utilities_ExpressionInOCL = Class(name="ocl::utilities::ExpressionInOCL", is_abstract=True)
Visitable = Class(name="Visitable")
ocl_utilities_PredefinedType = Class(name="ocl::utilities::PredefinedType", is_abstract=True)
ocl_expressions_CollectionLiteralPart = Class(name="ocl::expressions::CollectionLiteralPart", is_abstract=True)
ocl_expressions_CollectionLiteralExp = Class(name="ocl::expressions::CollectionLiteralExp")
ocl_expressions_OCLExpression = Class(name="ocl::expressions::OCLExpression", is_abstract=True)
ocl_expressions_BooleanLiteralExp = Class(name="ocl::expressions::BooleanLiteralExp")
ocl_expressions_PrimitiveLiteralExp = Class(name="ocl::expressions::PrimitiveLiteralExp", is_abstract=True)
ocl_expressions_LiteralExp = Class(name="ocl::expressions::LiteralExp", is_abstract=True)
ocl_expressions_CollectionItem = Class(name="ocl::expressions::CollectionItem")
ocl_expressions_EnumLiteralExp = Class(name="ocl::expressions::EnumLiteralExp")
ocl_expressions_CollectionRange = Class(name="ocl::expressions::CollectionRange")
ocl_expressions_IntegerLiteralExp = Class(name="ocl::expressions::IntegerLiteralExp")
ocl_expressions_NumericLiteralExp = Class(name="ocl::expressions::NumericLiteralExp", is_abstract=True)
ocl_expressions_UnlimitedNaturalLiteralExp = Class(name="ocl::expressions::UnlimitedNaturalLiteralExp")
ocl_expressions_IfExp = Class(name="ocl::expressions::IfExp")
ocl_expressions_LoopExp = Class(name="ocl::expressions::LoopExp", is_abstract=True)
ocl_expressions_InvalidLiteralExp = Class(name="ocl::expressions::InvalidLiteralExp")
ocl_expressions_IterateExp = Class(name="ocl::expressions::IterateExp")
ocl_expressions_Variable = Class(name="ocl::expressions::Variable")
ocl_expressions_IteratorExp = Class(name="ocl::expressions::IteratorExp")
ocl_expressions_LetExp = Class(name="ocl::expressions::LetExp")
ocl_expressions_MessageExp = Class(name="ocl::expressions::MessageExp")
ocl_expressions_PropertyCallExp = Class(name="ocl::expressions::PropertyCallExp")
ocl_expressions_NullLiteralExp = Class(name="ocl::expressions::NullLiteralExp")
ocl_expressions_OperationCallExp = Class(name="ocl::expressions::OperationCallExp")
ocl_expressions_StateExp = Class(name="ocl::expressions::StateExp")
ocl_expressions_StringLiteralExp = Class(name="ocl::expressions::StringLiteralExp")
ocl_expressions_TupleLiteralExp = Class(name="ocl::expressions::TupleLiteralExp")
ocl_expressions_RealLiteralExp = Class(name="ocl::expressions::RealLiteralExp")
ocl_expressions_TypeExp = Class(name="ocl::expressions::TypeExp")
ocl_expressions_UnspecifiedValueExp = Class(name="ocl::expressions::UnspecifiedValueExp")
ocl_expressions_VariableExp = Class(name="ocl::expressions::VariableExp")
ocl_expressions_TupleLiteralPart = Class(name="ocl::expressions::TupleLiteralPart")

# ocl_types_AnyType class attributes and methods

# ocl_types_BagType class attributes and methods

# ocl_types_ElementType class attributes and methods

# ocl_types_InvalidType class attributes and methods

# ocl_types_MessageType class attributes and methods
ocl_types_MessageType_m_exclusive_signature: Method = Method(name="exclusive_signature", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
ocl_types_MessageType_m_operation_parameters: Method = Method(name="operation_parameters", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
ocl_types_MessageType_m_signal_attributes: Method = Method(name="signal_attributes", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
ocl_types_MessageType_m_oclProperties: Method = Method(name="oclProperties", parameters={})
ocl_types_MessageType.methods={ocl_types_MessageType_m_oclProperties, ocl_types_MessageType_m_operation_parameters, ocl_types_MessageType_m_signal_attributes, ocl_types_MessageType_m_exclusive_signature}

# ocl_types_CollectionType class attributes and methods
ocl_types_CollectionType_kind: Property = Property(name="kind", type=StringType)
ocl_types_CollectionType_m_collection_type_name: Method = Method(name="collection_type_name", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
ocl_types_CollectionType_m_no_invalid_values: Method = Method(name="no_invalid_values", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
ocl_types_CollectionType_m_oclIterators: Method = Method(name="oclIterators", parameters={})
ocl_types_CollectionType.attributes={ocl_types_CollectionType_kind}
ocl_types_CollectionType.methods={ocl_types_CollectionType_m_collection_type_name, ocl_types_CollectionType_m_oclIterators, ocl_types_CollectionType_m_no_invalid_values}

# ocl_types_PrimitiveType class attributes and methods

# ocl_types_SequenceType class attributes and methods

# ocl_types_SetType class attributes and methods

# ocl_types_OrderedSetType class attributes and methods

# ocl_types_TypeType class attributes and methods

# ocl_types_TemplateParameterType class attributes and methods
ocl_types_TemplateParameterType_specification: Property = Property(name="specification", type=StringType)
ocl_types_TemplateParameterType.attributes={ocl_types_TemplateParameterType_specification}

# ocl_types_TupleType class attributes and methods
ocl_types_TupleType_m_features_only_properties: Method = Method(name="features_only_properties", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
ocl_types_TupleType_m_oclProperties: Method = Method(name="oclProperties", parameters={})
ocl_types_TupleType_m_tuple_type_name: Method = Method(name="tuple_type_name", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
ocl_types_TupleType_m_part_names_unique: Method = Method(name="part_names_unique", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
ocl_types_TupleType.methods={ocl_types_TupleType_m_part_names_unique, ocl_types_TupleType_m_features_only_properties, ocl_types_TupleType_m_tuple_type_name, ocl_types_TupleType_m_oclProperties}

# ocl_utilities_Visitor class attributes and methods
ocl_utilities_Visitor_m_visitVariableExp: Method = Method(name="visitVariableExp", parameters={Parameter(name='variableExp')})
ocl_utilities_Visitor_m_visitLetExp: Method = Method(name="visitLetExp", parameters={Parameter(name='letExp')})
ocl_utilities_Visitor_m_visitIfExp: Method = Method(name="visitIfExp", parameters={Parameter(name='ifExp')})
ocl_utilities_Visitor_m_visitIntegerLiteralExp: Method = Method(name="visitIntegerLiteralExp", parameters={Parameter(name='literalExp')})
ocl_utilities_Visitor_m_visitUnlimitedNaturalLiteralExp: Method = Method(name="visitUnlimitedNaturalLiteralExp", parameters={Parameter(name='literalExp')})
ocl_utilities_Visitor_m_visitRealLiteralExp: Method = Method(name="visitRealLiteralExp", parameters={Parameter(name='literalExp')})
ocl_utilities_Visitor_m_visitStringLiteralExp: Method = Method(name="visitStringLiteralExp", parameters={Parameter(name='literalExp')})
ocl_utilities_Visitor_m_visitBooleanLiteralExp: Method = Method(name="visitBooleanLiteralExp", parameters={Parameter(name='literalExp')})
ocl_utilities_Visitor_m_visitEnumLiteralExp: Method = Method(name="visitEnumLiteralExp", parameters={Parameter(name='literalExp')})
ocl_utilities_Visitor_m_visitTypeExp: Method = Method(name="visitTypeExp", parameters={Parameter(name='typeExp')})
ocl_utilities_Visitor_m_visitPropertyCallExp: Method = Method(name="visitPropertyCallExp", parameters={Parameter(name='callExp')})
ocl_utilities_Visitor_m_visitOperationCallExp: Method = Method(name="visitOperationCallExp", parameters={Parameter(name='callExp')})
ocl_utilities_Visitor_m_visitAssociationClassCallExp: Method = Method(name="visitAssociationClassCallExp", parameters={Parameter(name='callExp')})
ocl_utilities_Visitor_m_visitIteratorExp: Method = Method(name="visitIteratorExp", parameters={Parameter(name='callExp')})
ocl_utilities_Visitor_m_visitIterateExp: Method = Method(name="visitIterateExp", parameters={Parameter(name='callExp')})
ocl_utilities_Visitor_m_visitUnspecifiedValueExp: Method = Method(name="visitUnspecifiedValueExp", parameters={Parameter(name='unspecExp')})
ocl_utilities_Visitor_m_visitMessageExp: Method = Method(name="visitMessageExp", parameters={Parameter(name='messageExp')})
ocl_utilities_Visitor_m_visitVariable: Method = Method(name="visitVariable", parameters={Parameter(name='variable')})
ocl_utilities_Visitor_m_visitExpressionInOCL: Method = Method(name="visitExpressionInOCL", parameters={Parameter(name='expression')})
ocl_utilities_Visitor_m_visitConstraint: Method = Method(name="visitConstraint", parameters={Parameter(name='constraint')})
ocl_utilities_Visitor_m_visitCollectionLiteralExp: Method = Method(name="visitCollectionLiteralExp", parameters={Parameter(name='literalExp')})
ocl_utilities_Visitor_m_visitCollectionItem: Method = Method(name="visitCollectionItem", parameters={Parameter(name='item')})
ocl_utilities_Visitor_m_visitCollectionRange: Method = Method(name="visitCollectionRange", parameters={Parameter(name='range')})
ocl_utilities_Visitor_m_visitTupleLiteralExp: Method = Method(name="visitTupleLiteralExp", parameters={Parameter(name='literalExp')})
ocl_utilities_Visitor_m_visitTupleLiteralPart: Method = Method(name="visitTupleLiteralPart", parameters={Parameter(name='part')})
ocl_utilities_Visitor_m_visitInvalidLiteralExp: Method = Method(name="visitInvalidLiteralExp", parameters={Parameter(name='literalExp')})
ocl_utilities_Visitor_m_visitNullLiteralExp: Method = Method(name="visitNullLiteralExp", parameters={Parameter(name='literalExp')})
ocl_utilities_Visitor_m_visitStateExp: Method = Method(name="visitStateExp", parameters={Parameter(name='stateExp')})
ocl_utilities_Visitor.methods={ocl_utilities_Visitor_m_visitCollectionRange, ocl_utilities_Visitor_m_visitIteratorExp, ocl_utilities_Visitor_m_visitUnlimitedNaturalLiteralExp, ocl_utilities_Visitor_m_visitUnspecifiedValueExp, ocl_utilities_Visitor_m_visitConstraint, ocl_utilities_Visitor_m_visitOperationCallExp, ocl_utilities_Visitor_m_visitIfExp, ocl_utilities_Visitor_m_visitPropertyCallExp, ocl_utilities_Visitor_m_visitTypeExp, ocl_utilities_Visitor_m_visitBooleanLiteralExp, ocl_utilities_Visitor_m_visitVariableExp, ocl_utilities_Visitor_m_visitStateExp, ocl_utilities_Visitor_m_visitNullLiteralExp, ocl_utilities_Visitor_m_visitEnumLiteralExp, ocl_utilities_Visitor_m_visitVariable, ocl_utilities_Visitor_m_visitIntegerLiteralExp, ocl_utilities_Visitor_m_visitInvalidLiteralExp, ocl_utilities_Visitor_m_visitCollectionItem, ocl_utilities_Visitor_m_visitRealLiteralExp, ocl_utilities_Visitor_m_visitStringLiteralExp, ocl_utilities_Visitor_m_visitTupleLiteralExp, ocl_utilities_Visitor_m_visitLetExp, ocl_utilities_Visitor_m_visitAssociationClassCallExp, ocl_utilities_Visitor_m_visitIterateExp, ocl_utilities_Visitor_m_visitCollectionLiteralExp, ocl_utilities_Visitor_m_visitTupleLiteralPart, ocl_utilities_Visitor_m_visitExpressionInOCL, ocl_utilities_Visitor_m_visitMessageExp}

# ocl_types_VoidType class attributes and methods

# ocl_utilities_ASTNode class attributes and methods
ocl_utilities_ASTNode_startPosition: Property = Property(name="startPosition", type=IntegerType)
ocl_utilities_ASTNode_endPosition: Property = Property(name="endPosition", type=IntegerType)
ocl_utilities_ASTNode.attributes={ocl_utilities_ASTNode_startPosition, ocl_utilities_ASTNode_endPosition}

# ocl_utilities_CallingASTNode class attributes and methods
ocl_utilities_CallingASTNode_propertyStartPosition: Property = Property(name="propertyStartPosition", type=IntegerType)
ocl_utilities_CallingASTNode_propertyEndPosition: Property = Property(name="propertyEndPosition", type=IntegerType)
ocl_utilities_CallingASTNode.attributes={ocl_utilities_CallingASTNode_propertyEndPosition, ocl_utilities_CallingASTNode_propertyStartPosition}

# ASTNode class attributes and methods

# ocl_utilities_TypedASTNode class attributes and methods
ocl_utilities_TypedASTNode_typeStartPosition: Property = Property(name="typeStartPosition", type=IntegerType)
ocl_utilities_TypedASTNode_typeEndPosition: Property = Property(name="typeEndPosition", type=IntegerType)
ocl_utilities_TypedASTNode.attributes={ocl_utilities_TypedASTNode_typeEndPosition, ocl_utilities_TypedASTNode_typeStartPosition}

# ocl_utilities_Visitable class attributes and methods
ocl_utilities_Visitable_m_accept: Method = Method(name="accept", parameters={Parameter(name='v')})
ocl_utilities_Visitable.methods={ocl_utilities_Visitable_m_accept}

# ocl_utilities_TypedElement class attributes and methods
ocl_utilities_TypedElement_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
ocl_utilities_TypedElement_m_getType: Method = Method(name="getType", parameters={})
ocl_utilities_TypedElement_m_setName: Method = Method(name="setName", parameters={Parameter(name='name')})
ocl_utilities_TypedElement_m_setType: Method = Method(name="setType", parameters={Parameter(name='type')})
ocl_utilities_TypedElement.methods={ocl_utilities_TypedElement_m_getName, ocl_utilities_TypedElement_m_setType, ocl_utilities_TypedElement_m_getType, ocl_utilities_TypedElement_m_setName}

# ocl_expressions_AssociationClassCallExp class attributes and methods

# ocl_expressions_NavigationCallExp class attributes and methods

# ocl_expressions_FeatureCallExp class attributes and methods
ocl_expressions_FeatureCallExp_markedPre: Property = Property(name="markedPre", type=BooleanType)
ocl_expressions_FeatureCallExp.attributes={ocl_expressions_FeatureCallExp_markedPre}

# ocl_expressions_CallExp class attributes and methods

# ocl_utilities_ExpressionInOCL class attributes and methods

# Visitable class attributes and methods

# ocl_utilities_PredefinedType class attributes and methods
ocl_utilities_PredefinedType_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
ocl_utilities_PredefinedType_m_oclOperations: Method = Method(name="oclOperations", parameters={})
ocl_utilities_PredefinedType.methods={ocl_utilities_PredefinedType_m_oclOperations, ocl_utilities_PredefinedType_m_getName}

# ocl_expressions_CollectionLiteralPart class attributes and methods

# ocl_expressions_CollectionLiteralExp class attributes and methods
ocl_expressions_CollectionLiteralExp_kind: Property = Property(name="kind", type=StringType)
ocl_expressions_CollectionLiteralExp_simpleRange: Property = Property(name="simpleRange", type=BooleanType)
ocl_expressions_CollectionLiteralExp_m_no_collection_instances: Method = Method(name="no_collection_instances", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
ocl_expressions_CollectionLiteralExp_m_bag_kind: Method = Method(name="bag_kind", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
ocl_expressions_CollectionLiteralExp_m_set_kind: Method = Method(name="set_kind", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
ocl_expressions_CollectionLiteralExp_m_sequence_kind: Method = Method(name="sequence_kind", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
ocl_expressions_CollectionLiteralExp_m_element_type: Method = Method(name="element_type", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
ocl_expressions_CollectionLiteralExp.attributes={ocl_expressions_CollectionLiteralExp_simpleRange, ocl_expressions_CollectionLiteralExp_kind}
ocl_expressions_CollectionLiteralExp.methods={ocl_expressions_CollectionLiteralExp_m_sequence_kind, ocl_expressions_CollectionLiteralExp_m_no_collection_instances, ocl_expressions_CollectionLiteralExp_m_bag_kind, ocl_expressions_CollectionLiteralExp_m_set_kind, ocl_expressions_CollectionLiteralExp_m_element_type}

# ocl_expressions_OCLExpression class attributes and methods

# ocl_expressions_BooleanLiteralExp class attributes and methods
ocl_expressions_BooleanLiteralExp_booleanSymbol: Property = Property(name="booleanSymbol", type=StringType)
ocl_expressions_BooleanLiteralExp_m_boolean_type: Method = Method(name="boolean_type", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
ocl_expressions_BooleanLiteralExp.attributes={ocl_expressions_BooleanLiteralExp_booleanSymbol}
ocl_expressions_BooleanLiteralExp.methods={ocl_expressions_BooleanLiteralExp_m_boolean_type}

# ocl_expressions_PrimitiveLiteralExp class attributes and methods

# ocl_expressions_LiteralExp class attributes and methods

# ocl_expressions_CollectionItem class attributes and methods
ocl_expressions_CollectionItem_m_item_type: Method = Method(name="item_type", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
ocl_expressions_CollectionItem.methods={ocl_expressions_CollectionItem_m_item_type}

# ocl_expressions_EnumLiteralExp class attributes and methods
ocl_expressions_EnumLiteralExp_m_enum_type: Method = Method(name="enum_type", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
ocl_expressions_EnumLiteralExp.methods={ocl_expressions_EnumLiteralExp_m_enum_type}

# ocl_expressions_CollectionRange class attributes and methods
ocl_expressions_CollectionRange_m_range_type: Method = Method(name="range_type", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
ocl_expressions_CollectionRange.methods={ocl_expressions_CollectionRange_m_range_type}

# ocl_expressions_IntegerLiteralExp class attributes and methods
ocl_expressions_IntegerLiteralExp_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
ocl_expressions_IntegerLiteralExp_m_integer_type: Method = Method(name="integer_type", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
ocl_expressions_IntegerLiteralExp.attributes={ocl_expressions_IntegerLiteralExp_integerSymbol}
ocl_expressions_IntegerLiteralExp.methods={ocl_expressions_IntegerLiteralExp_m_integer_type}

# ocl_expressions_NumericLiteralExp class attributes and methods

# ocl_expressions_UnlimitedNaturalLiteralExp class attributes and methods
ocl_expressions_UnlimitedNaturalLiteralExp_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
ocl_expressions_UnlimitedNaturalLiteralExp_unlimited: Property = Property(name="unlimited", type=BooleanType)
ocl_expressions_UnlimitedNaturalLiteralExp_m_natural_type: Method = Method(name="natural_type", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
ocl_expressions_UnlimitedNaturalLiteralExp.attributes={ocl_expressions_UnlimitedNaturalLiteralExp_unlimited, ocl_expressions_UnlimitedNaturalLiteralExp_integerSymbol}
ocl_expressions_UnlimitedNaturalLiteralExp.methods={ocl_expressions_UnlimitedNaturalLiteralExp_m_natural_type}

# ocl_expressions_IfExp class attributes and methods
ocl_expressions_IfExp_m_boolean_condition: Method = Method(name="boolean_condition", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
ocl_expressions_IfExp_m_if_type: Method = Method(name="if_type", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
ocl_expressions_IfExp.methods={ocl_expressions_IfExp_m_boolean_condition, ocl_expressions_IfExp_m_if_type}

# ocl_expressions_LoopExp class attributes and methods
ocl_expressions_LoopExp_m_source_collection: Method = Method(name="source_collection", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
ocl_expressions_LoopExp_m_loop_variable_init: Method = Method(name="loop_variable_init", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
ocl_expressions_LoopExp_m_loop_variable_type: Method = Method(name="loop_variable_type", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
ocl_expressions_LoopExp.methods={ocl_expressions_LoopExp_m_loop_variable_init, ocl_expressions_LoopExp_m_source_collection, ocl_expressions_LoopExp_m_loop_variable_type}

# ocl_expressions_InvalidLiteralExp class attributes and methods

# ocl_expressions_IterateExp class attributes and methods
ocl_expressions_IterateExp_m_result_init: Method = Method(name="result_init", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
ocl_expressions_IterateExp_m_iterate_type: Method = Method(name="iterate_type", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
ocl_expressions_IterateExp_m_body_type: Method = Method(name="body_type", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
ocl_expressions_IterateExp.methods={ocl_expressions_IterateExp_m_iterate_type, ocl_expressions_IterateExp_m_body_type, ocl_expressions_IterateExp_m_result_init}

# ocl_expressions_Variable class attributes and methods
ocl_expressions_Variable_m_init_type: Method = Method(name="init_type", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
ocl_expressions_Variable.methods={ocl_expressions_Variable_m_init_type}

# ocl_expressions_IteratorExp class attributes and methods
ocl_expressions_IteratorExp_m_boolean_body_type: Method = Method(name="boolean_body_type", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
ocl_expressions_IteratorExp_m_boolean_type: Method = Method(name="boolean_type", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
ocl_expressions_IteratorExp_m_collect_type: Method = Method(name="collect_type", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
ocl_expressions_IteratorExp_m_select_reject_type: Method = Method(name="select_reject_type", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
ocl_expressions_IteratorExp.methods={ocl_expressions_IteratorExp_m_boolean_body_type, ocl_expressions_IteratorExp_m_select_reject_type, ocl_expressions_IteratorExp_m_boolean_type, ocl_expressions_IteratorExp_m_collect_type}

# ocl_expressions_LetExp class attributes and methods
ocl_expressions_LetExp_m_let_type: Method = Method(name="let_type", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
ocl_expressions_LetExp.methods={ocl_expressions_LetExp_m_let_type}

# ocl_expressions_MessageExp class attributes and methods
ocl_expressions_MessageExp_m_target_defines_operation: Method = Method(name="target_defines_operation", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
ocl_expressions_MessageExp_m_has_operation_or_signal: Method = Method(name="has_operation_or_signal", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
ocl_expressions_MessageExp_m_operation_arguments: Method = Method(name="operation_arguments", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
ocl_expressions_MessageExp_m_signal_arguments: Method = Method(name="signal_arguments", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
ocl_expressions_MessageExp_m_target_not_collection: Method = Method(name="target_not_collection", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
ocl_expressions_MessageExp.methods={ocl_expressions_MessageExp_m_has_operation_or_signal, ocl_expressions_MessageExp_m_target_not_collection, ocl_expressions_MessageExp_m_operation_arguments, ocl_expressions_MessageExp_m_signal_arguments, ocl_expressions_MessageExp_m_target_defines_operation}

# ocl_expressions_PropertyCallExp class attributes and methods
ocl_expressions_PropertyCallExp_m_property_type: Method = Method(name="property_type", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
ocl_expressions_PropertyCallExp.methods={ocl_expressions_PropertyCallExp_m_property_type}

# ocl_expressions_NullLiteralExp class attributes and methods

# ocl_expressions_OperationCallExp class attributes and methods
ocl_expressions_OperationCallExp_operationCode: Property = Property(name="operationCode", type=IntegerType)
ocl_expressions_OperationCallExp_m_argument_count: Method = Method(name="argument_count", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
ocl_expressions_OperationCallExp_m_arguments_conform: Method = Method(name="arguments_conform", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
ocl_expressions_OperationCallExp.attributes={ocl_expressions_OperationCallExp_operationCode}
ocl_expressions_OperationCallExp.methods={ocl_expressions_OperationCallExp_m_argument_count, ocl_expressions_OperationCallExp_m_arguments_conform}

# ocl_expressions_StateExp class attributes and methods

# ocl_expressions_StringLiteralExp class attributes and methods
ocl_expressions_StringLiteralExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
ocl_expressions_StringLiteralExp_m_string_type: Method = Method(name="string_type", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
ocl_expressions_StringLiteralExp.attributes={ocl_expressions_StringLiteralExp_stringSymbol}
ocl_expressions_StringLiteralExp.methods={ocl_expressions_StringLiteralExp_m_string_type}

# ocl_expressions_TupleLiteralExp class attributes and methods
ocl_expressions_TupleLiteralExp_m_tuple_type: Method = Method(name="tuple_type", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
ocl_expressions_TupleLiteralExp_m_parts_unique: Method = Method(name="parts_unique", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
ocl_expressions_TupleLiteralExp.methods={ocl_expressions_TupleLiteralExp_m_tuple_type, ocl_expressions_TupleLiteralExp_m_parts_unique}

# ocl_expressions_RealLiteralExp class attributes and methods
ocl_expressions_RealLiteralExp_realSymbol: Property = Property(name="realSymbol", type=StringType)
ocl_expressions_RealLiteralExp_m_real_type: Method = Method(name="real_type", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
ocl_expressions_RealLiteralExp.attributes={ocl_expressions_RealLiteralExp_realSymbol}
ocl_expressions_RealLiteralExp.methods={ocl_expressions_RealLiteralExp_m_real_type}

# ocl_expressions_TypeExp class attributes and methods

# ocl_expressions_UnspecifiedValueExp class attributes and methods

# ocl_expressions_VariableExp class attributes and methods
ocl_expressions_VariableExp_m_var_type: Method = Method(name="var_type", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
ocl_expressions_VariableExp.methods={ocl_expressions_VariableExp_m_var_type}

# ocl_expressions_TupleLiteralPart class attributes and methods
ocl_expressions_TupleLiteralPart_m_value_type: Method = Method(name="value_type", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
ocl_expressions_TupleLiteralPart.methods={ocl_expressions_TupleLiteralPart_m_value_type}

# Generalizations
gen_ocl_utilities_CallingASTNode_ASTNode = Generalization(general=ASTNode, specific=ocl_utilities_CallingASTNode)
gen_ocl_utilities_TypedASTNode_ASTNode = Generalization(general=ASTNode, specific=ocl_utilities_TypedASTNode)
gen_ocl_utilities_ExpressionInOCL_Visitable = Generalization(general=Visitable, specific=ocl_utilities_ExpressionInOCL)

# Domain Model
domain_model = DomainModel(
    name="ocl",
    types={ocl_types_AnyType, ocl_types_BagType, ocl_types_ElementType, ocl_types_InvalidType, ocl_types_MessageType, ocl_types_CollectionType, ocl_types_PrimitiveType, ocl_types_SequenceType, ocl_types_SetType, ocl_types_OrderedSetType, ocl_types_TypeType, ocl_types_TemplateParameterType, ocl_types_TupleType, ocl_utilities_Visitor, ocl_types_VoidType, ocl_utilities_ASTNode, ocl_utilities_CallingASTNode, ASTNode, ocl_utilities_TypedASTNode, ocl_utilities_Visitable, ocl_utilities_TypedElement, ocl_expressions_AssociationClassCallExp, ocl_expressions_NavigationCallExp, ocl_expressions_FeatureCallExp, ocl_expressions_CallExp, ocl_utilities_ExpressionInOCL, Visitable, ocl_utilities_PredefinedType, ocl_expressions_CollectionLiteralPart, ocl_expressions_CollectionLiteralExp, ocl_expressions_OCLExpression, ocl_expressions_BooleanLiteralExp, ocl_expressions_PrimitiveLiteralExp, ocl_expressions_LiteralExp, ocl_expressions_CollectionItem, ocl_expressions_EnumLiteralExp, ocl_expressions_CollectionRange, ocl_expressions_IntegerLiteralExp, ocl_expressions_NumericLiteralExp, ocl_expressions_UnlimitedNaturalLiteralExp, ocl_expressions_IfExp, ocl_expressions_LoopExp, ocl_expressions_InvalidLiteralExp, ocl_expressions_IterateExp, ocl_expressions_Variable, ocl_expressions_IteratorExp, ocl_expressions_LetExp, ocl_expressions_MessageExp, ocl_expressions_PropertyCallExp, ocl_expressions_NullLiteralExp, ocl_expressions_OperationCallExp, ocl_expressions_StateExp, ocl_expressions_StringLiteralExp, ocl_expressions_TupleLiteralExp, ocl_expressions_RealLiteralExp, ocl_expressions_TypeExp, ocl_expressions_UnspecifiedValueExp, ocl_expressions_VariableExp, ocl_expressions_TupleLiteralPart, CollectionKind},
    associations={},
    generalizations={gen_ocl_utilities_CallingASTNode_ASTNode, gen_ocl_utilities_TypedASTNode_ASTNode, gen_ocl_utilities_ExpressionInOCL_Visitable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)