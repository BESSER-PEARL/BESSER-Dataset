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
activityecorelua_EAttribute = Class(name="activityecorelua::EAttribute")
EStructuralFeature = Class(name="EStructuralFeature")
activityecorelua_EDataType = Class(name="activityecorelua::EDataType")
activityecorelua_EAnnotation = Class(name="activityecorelua::EAnnotation")
EModelElement = Class(name="EModelElement")
activityecorelua_EStringToStringMapEntry = Class(name="activityecorelua::EStringToStringMapEntry")
activityecorelua_EModelElement = Class(name="activityecorelua::EModelElement", is_abstract=True)
activityecorelua_EObject = Class(name="activityecorelua::EObject")
activityecorelua_EClass = Class(name="activityecorelua::EClass")
EClassifier = Class(name="EClassifier")
activityecorelua_EStructuralFeature = Class(name="activityecorelua::EStructuralFeature", is_abstract=True)
activityecorelua_EOperation = Class(name="activityecorelua::EOperation")
activityecorelua_EReference = Class(name="activityecorelua::EReference")
activityecorelua_EEnum = Class(name="activityecorelua::EEnum")
EDataType = Class(name="EDataType")
activityecorelua_EGenericType = Class(name="activityecorelua::EGenericType")
activityecorelua_EClassifier = Class(name="activityecorelua::EClassifier", is_abstract=True)
ENamedElement = Class(name="ENamedElement")
activityecorelua_EPackage = Class(name="activityecorelua::EPackage")
activityecorelua_ETypeParameter = Class(name="activityecorelua::ETypeParameter")
activityecorelua_EEnumLiteral = Class(name="activityecorelua::EEnumLiteral")
activityecorelua_EFactory = Class(name="activityecorelua::EFactory")
activityecorelua_ENamedElement = Class(name="activityecorelua::ENamedElement", is_abstract=True)
ETypedElement = Class(name="ETypedElement")
activityecorelua_EParameter = Class(name="activityecorelua::EParameter")
activityecorelua_Activity = Class(name="activityecorelua::Activity")
activityecorelua_ETypedElement = Class(name="activityecorelua::ETypedElement", is_abstract=True)
activityecorelua_Variable = Class(name="activityecorelua::Variable", is_abstract=True)
NamedElement = Class(name="NamedElement")
activityecorelua_ActivityNode = Class(name="activityecorelua::ActivityNode", is_abstract=True)
activityecorelua_ActivityEdge = Class(name="activityecorelua::ActivityEdge", is_abstract=True)
activityecorelua_Value = Class(name="activityecorelua::Value", is_abstract=True)
activityecorelua_ControlFlow = Class(name="activityecorelua::ControlFlow")
ActivityEdge = Class(name="ActivityEdge")
activityecorelua_BooleanVariable = Class(name="activityecorelua::BooleanVariable")
activityecorelua_ControlNode = Class(name="activityecorelua::ControlNode", is_abstract=True)
ActivityNode = Class(name="ActivityNode")
activityecorelua_ExecutableNode = Class(name="activityecorelua::ExecutableNode", is_abstract=True)
activityecorelua_Action = Class(name="activityecorelua::Action", is_abstract=True)
ExecutableNode = Class(name="ExecutableNode")
activityecorelua_OpaqueAction = Class(name="activityecorelua::OpaqueAction")
Action = Class(name="Action")
activityecorelua_Expression = Class(name="activityecorelua::Expression")
activityecorelua_NamedElement = Class(name="activityecorelua::NamedElement", is_abstract=True)
activityecorelua_InitialNode = Class(name="activityecorelua::InitialNode")
ControlNode = Class(name="ControlNode")
activityecorelua_FinalNode = Class(name="activityecorelua::FinalNode", is_abstract=True)
activityecorelua_ActivityFinalNode = Class(name="activityecorelua::ActivityFinalNode")
FinalNode = Class(name="FinalNode")
activityecorelua_ForkNode = Class(name="activityecorelua::ForkNode")
activityecorelua_JoinNode = Class(name="activityecorelua::JoinNode")
activityecorelua_MergeNode = Class(name="activityecorelua::MergeNode")
activityecorelua_DecisionNode = Class(name="activityecorelua::DecisionNode")
activityecorelua_Statement_Repeat = Class(name="activityecorelua::Statement::Repeat")
activityecorelua_IntegerVariable = Class(name="activityecorelua::IntegerVariable")
Variable = Class(name="Variable")
activityecorelua_BooleanValue = Class(name="activityecorelua::BooleanValue")
Value = Class(name="Value")
activityecorelua_IntegerValue = Class(name="activityecorelua::IntegerValue")
activityecorelua_InputValue = Class(name="activityecorelua::InputValue")
activityecorelua_Input = Class(name="activityecorelua::Input")
activityecorelua_Chunk = Class(name="activityecorelua::Chunk")
activityecorelua_Block = Class(name="activityecorelua::Block")
Chunk = Class(name="Chunk")
activityecorelua_Statement = Class(name="activityecorelua::Statement")
activityecorelua_LastStatement = Class(name="activityecorelua::LastStatement")
activityecorelua_LastStatement_Return = Class(name="activityecorelua::LastStatement::Return")
LastStatement = Class(name="LastStatement")
activityecorelua_LastStatement_Break = Class(name="activityecorelua::LastStatement::Break")
activityecorelua_Statement_Block = Class(name="activityecorelua::Statement::Block")
Statement = Class(name="Statement")
activityecorelua_Statement_While = Class(name="activityecorelua::Statement::While")
activityecorelua_Statement_If_Then_Else = Class(name="activityecorelua::Statement::If::Then::Else")
activityecorelua_Statement_If_Then_Else_ElseIfPart = Class(name="activityecorelua::Statement::If::Then::Else::ElseIfPart")
activityecorelua_Statement_For_Numeric = Class(name="activityecorelua::Statement::For::Numeric")
activityecorelua_Statement_For_Generic = Class(name="activityecorelua::Statement::For::Generic")
activityecorelua_Statement_GlobalFunction_Declaration = Class(name="activityecorelua::Statement::GlobalFunction::Declaration")
activityecorelua_Function = Class(name="activityecorelua::Function")
activityecorelua_Statement_LocalFunction_Declaration = Class(name="activityecorelua::Statement::LocalFunction::Declaration")
activityecorelua_Statement_Local_Variable_Declaration = Class(name="activityecorelua::Statement::Local::Variable::Declaration")
activityecorelua_Statement_FunctioncallOrAssignment = Class(name="activityecorelua::Statement::FunctioncallOrAssignment")
Statement_FunctioncallOrAssignment = Class(name="Statement::FunctioncallOrAssignment")
activityecorelua_Expression_Nil = Class(name="activityecorelua::Expression::Nil")
Expression = Class(name="Expression")
activityecorelua_Expression_True = Class(name="activityecorelua::Expression::True")
activityecorelua_Expression_False = Class(name="activityecorelua::Expression::False")
activityecorelua_Expression_Number = Class(name="activityecorelua::Expression::Number")
activityecorelua_Expression_VarArgs = Class(name="activityecorelua::Expression::VarArgs")
activityecorelua_Expression_String = Class(name="activityecorelua::Expression::String")
activityecorelua_Expression_Function = Class(name="activityecorelua::Expression::Function")
activityecorelua_Expression_TableConstructor = Class(name="activityecorelua::Expression::TableConstructor")
activityecorelua_Field = Class(name="activityecorelua::Field")
activityecorelua_Functioncall_Arguments = Class(name="activityecorelua::Functioncall::Arguments")
activityecorelua_Field_AddEntryToTable_Brackets = Class(name="activityecorelua::Field::AddEntryToTable::Brackets")
Field = Class(name="Field")
activityecorelua_Field_AddEntryToTable = Class(name="activityecorelua::Field::AddEntryToTable")
activityecorelua_Field_AppendEntryToTable = Class(name="activityecorelua::Field::AppendEntryToTable")
activityecorelua_LastStatement_ReturnWithValue = Class(name="activityecorelua::LastStatement::ReturnWithValue")
LastStatement_Return = Class(name="LastStatement::Return")
activityecorelua_Statement_Assignment = Class(name="activityecorelua::Statement::Assignment")
activityecorelua_Statement_CallMemberFunction = Class(name="activityecorelua::Statement::CallMemberFunction")
activityecorelua_Statement_CallFunction = Class(name="activityecorelua::Statement::CallFunction")
activityecorelua_Expression_Or = Class(name="activityecorelua::Expression::Or")
activityecorelua_Expression_And = Class(name="activityecorelua::Expression::And")
activityecorelua_Expression_Larger = Class(name="activityecorelua::Expression::Larger")
activityecorelua_Expression_Larger_Equal = Class(name="activityecorelua::Expression::Larger::Equal")
activityecorelua_Expression_Smaller = Class(name="activityecorelua::Expression::Smaller")
activityecorelua_Expression_Smaller_Equal = Class(name="activityecorelua::Expression::Smaller::Equal")
activityecorelua_Expression_Equal = Class(name="activityecorelua::Expression::Equal")
activityecorelua_Expression_Not_Equal = Class(name="activityecorelua::Expression::Not::Equal")
activityecorelua_Expression_Concatenation = Class(name="activityecorelua::Expression::Concatenation")
activityecorelua_Expression_Plus = Class(name="activityecorelua::Expression::Plus")
activityecorelua_Expression_Minus = Class(name="activityecorelua::Expression::Minus")
activityecorelua_Expression_Invert = Class(name="activityecorelua::Expression::Invert")
activityecorelua_Expression_Exponentiation = Class(name="activityecorelua::Expression::Exponentiation")
activityecorelua_Expression_Multiplication = Class(name="activityecorelua::Expression::Multiplication")
activityecorelua_Expression_Division = Class(name="activityecorelua::Expression::Division")
activityecorelua_Expression_Modulo = Class(name="activityecorelua::Expression::Modulo")
activityecorelua_Expression_Negate = Class(name="activityecorelua::Expression::Negate")
activityecorelua_Expression_Length = Class(name="activityecorelua::Expression::Length")
activityecorelua_Expression_AccessArray = Class(name="activityecorelua::Expression::AccessArray")
activityecorelua_Expression_CallMemberFunction = Class(name="activityecorelua::Expression::CallMemberFunction")
activityecorelua_Expression_CallFunction = Class(name="activityecorelua::Expression::CallFunction")
activityecorelua_Expression_AccessMember = Class(name="activityecorelua::Expression::AccessMember")
activityecorelua_Expression_VariableName = Class(name="activityecorelua::Expression::VariableName")

# activityecorelua_EAttribute class attributes and methods
activityecorelua_EAttribute_iD: Property = Property(name="iD", type=BooleanType)
activityecorelua_EAttribute.attributes={activityecorelua_EAttribute_iD}

# EStructuralFeature class attributes and methods

# activityecorelua_EDataType class attributes and methods
activityecorelua_EDataType_serializable: Property = Property(name="serializable", type=BooleanType)
activityecorelua_EDataType.attributes={activityecorelua_EDataType_serializable}

# activityecorelua_EAnnotation class attributes and methods
activityecorelua_EAnnotation_source: Property = Property(name="source", type=StringType)
activityecorelua_EAnnotation.attributes={activityecorelua_EAnnotation_source}

# EModelElement class attributes and methods

# activityecorelua_EStringToStringMapEntry class attributes and methods
activityecorelua_EStringToStringMapEntry_key: Property = Property(name="key", type=StringType)
activityecorelua_EStringToStringMapEntry_value: Property = Property(name="value", type=StringType)
activityecorelua_EStringToStringMapEntry.attributes={activityecorelua_EStringToStringMapEntry_key, activityecorelua_EStringToStringMapEntry_value}

# activityecorelua_EModelElement class attributes and methods
activityecorelua_EModelElement_m_getEAnnotation: Method = Method(name="getEAnnotation", parameters={Parameter(name='source')}, type=StringType)
activityecorelua_EModelElement.methods={activityecorelua_EModelElement_m_getEAnnotation}

# activityecorelua_EObject class attributes and methods
activityecorelua_EObject_m_eeClass: Method = Method(name="eeClass", parameters={}, type=StringType)
activityecorelua_EObject.methods={activityecorelua_EObject_m_eeClass}

# activityecorelua_EClass class attributes and methods
activityecorelua_EClass_abstract: Property = Property(name="abstract", type=BooleanType)
activityecorelua_EClass_interface: Property = Property(name="interface", type=BooleanType)
activityecorelua_EClass_m_getFeatureCount: Method = Method(name="getFeatureCount", parameters={}, type=IntegerType)
activityecorelua_EClass_m_isSuperTypeOf: Method = Method(name="isSuperTypeOf", parameters={Parameter(name='someClass')}, type=BooleanType)
activityecorelua_EClass_m_getEStructuralFeature: Method = Method(name="getEStructuralFeature", parameters={Parameter(name='featureID')}, type=EStructuralFeature)
activityecorelua_EClass_m_getFeatureID: Method = Method(name="getFeatureID", parameters={Parameter(name='feature')}, type=IntegerType)
activityecorelua_EClass_m_getEStructuralFeature: Method = Method(name="getEStructuralFeature", parameters={Parameter(name='featureName')}, type=EStructuralFeature)
activityecorelua_EClass_m_getOperationCount: Method = Method(name="getOperationCount", parameters={}, type=IntegerType)
activityecorelua_EClass_m_getEOperation: Method = Method(name="getEOperation", parameters={Parameter(name='operationID')}, type=StringType)
activityecorelua_EClass_m_getOperationID: Method = Method(name="getOperationID", parameters={Parameter(name='operation')}, type=IntegerType)
activityecorelua_EClass_m_getOverride: Method = Method(name="getOverride", parameters={Parameter(name='operation')}, type=StringType)
activityecorelua_EClass.attributes={activityecorelua_EClass_abstract, activityecorelua_EClass_interface}
activityecorelua_EClass.methods={activityecorelua_EClass_m_getEStructuralFeature, activityecorelua_EClass_m_getFeatureID, activityecorelua_EClass_m_getFeatureCount, activityecorelua_EClass_m_isSuperTypeOf, activityecorelua_EClass_m_getEOperation, activityecorelua_EClass_m_getEStructuralFeature, activityecorelua_EClass_m_getOverride, activityecorelua_EClass_m_getOperationCount, activityecorelua_EClass_m_getOperationID}

# EClassifier class attributes and methods

# activityecorelua_EStructuralFeature class attributes and methods
activityecorelua_EStructuralFeature_changeable: Property = Property(name="changeable", type=BooleanType)
activityecorelua_EStructuralFeature_volatile: Property = Property(name="volatile", type=BooleanType)
activityecorelua_EStructuralFeature_transient: Property = Property(name="transient", type=BooleanType)
activityecorelua_EStructuralFeature_defaultValueLiteral: Property = Property(name="defaultValueLiteral", type=StringType)
activityecorelua_EStructuralFeature_defaultValue: Property = Property(name="defaultValue", type=StringType)
activityecorelua_EStructuralFeature_unsettable: Property = Property(name="unsettable", type=BooleanType)
activityecorelua_EStructuralFeature_derived: Property = Property(name="derived", type=BooleanType)
activityecorelua_EStructuralFeature_m_getFeatureID: Method = Method(name="getFeatureID", parameters={}, type=IntegerType)
activityecorelua_EStructuralFeature_m_getContainerClass: Method = Method(name="getContainerClass", parameters={})
activityecorelua_EStructuralFeature.attributes={activityecorelua_EStructuralFeature_defaultValue, activityecorelua_EStructuralFeature_unsettable, activityecorelua_EStructuralFeature_derived, activityecorelua_EStructuralFeature_defaultValueLiteral, activityecorelua_EStructuralFeature_changeable, activityecorelua_EStructuralFeature_transient, activityecorelua_EStructuralFeature_volatile}
activityecorelua_EStructuralFeature.methods={activityecorelua_EStructuralFeature_m_getContainerClass, activityecorelua_EStructuralFeature_m_getFeatureID}

# activityecorelua_EOperation class attributes and methods
activityecorelua_EOperation_m_getOperationID: Method = Method(name="getOperationID", parameters={}, type=IntegerType)
activityecorelua_EOperation_m_isOverrideOf: Method = Method(name="isOverrideOf", parameters={Parameter(name='someOperation')}, type=BooleanType)
activityecorelua_EOperation.methods={activityecorelua_EOperation_m_isOverrideOf, activityecorelua_EOperation_m_getOperationID}

# activityecorelua_EReference class attributes and methods
activityecorelua_EReference_containment: Property = Property(name="containment", type=BooleanType)
activityecorelua_EReference_container: Property = Property(name="container", type=BooleanType)
activityecorelua_EReference_resolveProxies: Property = Property(name="resolveProxies", type=BooleanType)
activityecorelua_EReference.attributes={activityecorelua_EReference_containment, activityecorelua_EReference_container, activityecorelua_EReference_resolveProxies}

# activityecorelua_EEnum class attributes and methods
activityecorelua_EEnum_m_getEEnumLiteral: Method = Method(name="getEEnumLiteral", parameters={Parameter(name='name')}, type=StringType)
activityecorelua_EEnum_m_getEEnumLiteral: Method = Method(name="getEEnumLiteral", parameters={Parameter(name='value')}, type=StringType)
activityecorelua_EEnum_m_getEEnumLiteralByLiteral: Method = Method(name="getEEnumLiteralByLiteral", parameters={Parameter(name='literal')}, type=StringType)
activityecorelua_EEnum.methods={activityecorelua_EEnum_m_getEEnumLiteralByLiteral, activityecorelua_EEnum_m_getEEnumLiteral, activityecorelua_EEnum_m_getEEnumLiteral}

# EDataType class attributes and methods

# activityecorelua_EGenericType class attributes and methods

# activityecorelua_EClassifier class attributes and methods
activityecorelua_EClassifier_instanceClassName: Property = Property(name="instanceClassName", type=StringType)
activityecorelua_EClassifier_instanceClass: Property = Property(name="instanceClass", type=StringType)
activityecorelua_EClassifier_defaultValue: Property = Property(name="defaultValue", type=StringType)
activityecorelua_EClassifier_instanceTypeName: Property = Property(name="instanceTypeName", type=StringType)
activityecorelua_EClassifier_m_isInstance: Method = Method(name="isInstance", parameters={Parameter(name='object')}, type=BooleanType)
activityecorelua_EClassifier_m_getClassifierID: Method = Method(name="getClassifierID", parameters={}, type=IntegerType)
activityecorelua_EClassifier.attributes={activityecorelua_EClassifier_defaultValue, activityecorelua_EClassifier_instanceClassName, activityecorelua_EClassifier_instanceTypeName, activityecorelua_EClassifier_instanceClass}
activityecorelua_EClassifier.methods={activityecorelua_EClassifier_m_isInstance, activityecorelua_EClassifier_m_getClassifierID}

# ENamedElement class attributes and methods

# activityecorelua_EPackage class attributes and methods
activityecorelua_EPackage_nsURI: Property = Property(name="nsURI", type=StringType)
activityecorelua_EPackage_nsPrefix: Property = Property(name="nsPrefix", type=StringType)
activityecorelua_EPackage_m_getEClassifier: Method = Method(name="getEClassifier", parameters={Parameter(name='name')}, type=EClassifier)
activityecorelua_EPackage.attributes={activityecorelua_EPackage_nsPrefix, activityecorelua_EPackage_nsURI}
activityecorelua_EPackage.methods={activityecorelua_EPackage_m_getEClassifier}

# activityecorelua_ETypeParameter class attributes and methods

# activityecorelua_EEnumLiteral class attributes and methods
activityecorelua_EEnumLiteral_value: Property = Property(name="value", type=IntegerType)
activityecorelua_EEnumLiteral_instance: Property = Property(name="instance", type=StringType)
activityecorelua_EEnumLiteral_literal: Property = Property(name="literal", type=StringType)
activityecorelua_EEnumLiteral.attributes={activityecorelua_EEnumLiteral_literal, activityecorelua_EEnumLiteral_instance, activityecorelua_EEnumLiteral_value}

# activityecorelua_EFactory class attributes and methods
activityecorelua_EFactory_m_create: Method = Method(name="create", parameters={Parameter(name='eClass')}, type=StringType)
activityecorelua_EFactory_m_createFromString: Method = Method(name="createFromString", parameters={Parameter(name='literalValue'), Parameter(name='eDataType')}, type=StringType)
activityecorelua_EFactory_m_convertToString: Method = Method(name="convertToString", parameters={Parameter(name='instanceValue'), Parameter(name='eDataType')}, type=StringType)
activityecorelua_EFactory.methods={activityecorelua_EFactory_m_createFromString, activityecorelua_EFactory_m_convertToString, activityecorelua_EFactory_m_create}

# activityecorelua_ENamedElement class attributes and methods
activityecorelua_ENamedElement_name: Property = Property(name="name", type=StringType)
activityecorelua_ENamedElement.attributes={activityecorelua_ENamedElement_name}

# ETypedElement class attributes and methods

# activityecorelua_EParameter class attributes and methods

# activityecorelua_Activity class attributes and methods

# activityecorelua_ETypedElement class attributes and methods
activityecorelua_ETypedElement_ordered: Property = Property(name="ordered", type=BooleanType)
activityecorelua_ETypedElement_unique: Property = Property(name="unique", type=BooleanType)
activityecorelua_ETypedElement_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
activityecorelua_ETypedElement_upperBound: Property = Property(name="upperBound", type=IntegerType)
activityecorelua_ETypedElement_many: Property = Property(name="many", type=BooleanType)
activityecorelua_ETypedElement_required: Property = Property(name="required", type=BooleanType)
activityecorelua_ETypedElement.attributes={activityecorelua_ETypedElement_required, activityecorelua_ETypedElement_unique, activityecorelua_ETypedElement_many, activityecorelua_ETypedElement_ordered, activityecorelua_ETypedElement_upperBound, activityecorelua_ETypedElement_lowerBound}

# activityecorelua_Variable class attributes and methods
activityecorelua_Variable_name: Property = Property(name="name", type=StringType)
activityecorelua_Variable.attributes={activityecorelua_Variable_name}

# NamedElement class attributes and methods

# activityecorelua_ActivityNode class attributes and methods
activityecorelua_ActivityNode_running: Property = Property(name="running", type=BooleanType)
activityecorelua_ActivityNode.attributes={activityecorelua_ActivityNode_running}

# activityecorelua_ActivityEdge class attributes and methods

# activityecorelua_Value class attributes and methods

# activityecorelua_ControlFlow class attributes and methods

# ActivityEdge class attributes and methods

# activityecorelua_BooleanVariable class attributes and methods

# activityecorelua_ControlNode class attributes and methods

# ActivityNode class attributes and methods

# activityecorelua_ExecutableNode class attributes and methods

# activityecorelua_Action class attributes and methods

# ExecutableNode class attributes and methods

# activityecorelua_OpaqueAction class attributes and methods

# Action class attributes and methods

# activityecorelua_Expression class attributes and methods

# activityecorelua_NamedElement class attributes and methods
activityecorelua_NamedElement_name: Property = Property(name="name", type=StringType)
activityecorelua_NamedElement.attributes={activityecorelua_NamedElement_name}

# activityecorelua_InitialNode class attributes and methods

# ControlNode class attributes and methods

# activityecorelua_FinalNode class attributes and methods

# activityecorelua_ActivityFinalNode class attributes and methods

# FinalNode class attributes and methods

# activityecorelua_ForkNode class attributes and methods

# activityecorelua_JoinNode class attributes and methods

# activityecorelua_MergeNode class attributes and methods

# activityecorelua_DecisionNode class attributes and methods

# activityecorelua_Statement_Repeat class attributes and methods

# activityecorelua_IntegerVariable class attributes and methods

# Variable class attributes and methods

# activityecorelua_BooleanValue class attributes and methods
activityecorelua_BooleanValue_value: Property = Property(name="value", type=BooleanType)
activityecorelua_BooleanValue.attributes={activityecorelua_BooleanValue_value}

# Value class attributes and methods

# activityecorelua_IntegerValue class attributes and methods
activityecorelua_IntegerValue_value: Property = Property(name="value", type=IntegerType)
activityecorelua_IntegerValue.attributes={activityecorelua_IntegerValue_value}

# activityecorelua_InputValue class attributes and methods

# activityecorelua_Input class attributes and methods

# activityecorelua_Chunk class attributes and methods

# activityecorelua_Block class attributes and methods

# Chunk class attributes and methods

# activityecorelua_Statement class attributes and methods

# activityecorelua_LastStatement class attributes and methods

# activityecorelua_LastStatement_Return class attributes and methods

# LastStatement class attributes and methods

# activityecorelua_LastStatement_Break class attributes and methods

# activityecorelua_Statement_Block class attributes and methods

# Statement class attributes and methods

# activityecorelua_Statement_While class attributes and methods

# activityecorelua_Statement_If_Then_Else class attributes and methods

# activityecorelua_Statement_If_Then_Else_ElseIfPart class attributes and methods

# activityecorelua_Statement_For_Numeric class attributes and methods
activityecorelua_Statement_For_Numeric_iteratorName: Property = Property(name="iteratorName", type=StringType)
activityecorelua_Statement_For_Numeric.attributes={activityecorelua_Statement_For_Numeric_iteratorName}

# activityecorelua_Statement_For_Generic class attributes and methods
activityecorelua_Statement_For_Generic_names: Property = Property(name="names", type=StringType)
activityecorelua_Statement_For_Generic.attributes={activityecorelua_Statement_For_Generic_names}

# activityecorelua_Statement_GlobalFunction_Declaration class attributes and methods
activityecorelua_Statement_GlobalFunction_Declaration_prefix: Property = Property(name="prefix", type=StringType)
activityecorelua_Statement_GlobalFunction_Declaration_functionName: Property = Property(name="functionName", type=StringType)
activityecorelua_Statement_GlobalFunction_Declaration.attributes={activityecorelua_Statement_GlobalFunction_Declaration_prefix, activityecorelua_Statement_GlobalFunction_Declaration_functionName}

# activityecorelua_Function class attributes and methods
activityecorelua_Function_parameters: Property = Property(name="parameters", type=StringType)
activityecorelua_Function_varArgs: Property = Property(name="varArgs", type=BooleanType)
activityecorelua_Function.attributes={activityecorelua_Function_varArgs, activityecorelua_Function_parameters}

# activityecorelua_Statement_LocalFunction_Declaration class attributes and methods
activityecorelua_Statement_LocalFunction_Declaration_functionName: Property = Property(name="functionName", type=StringType)
activityecorelua_Statement_LocalFunction_Declaration.attributes={activityecorelua_Statement_LocalFunction_Declaration_functionName}

# activityecorelua_Statement_Local_Variable_Declaration class attributes and methods
activityecorelua_Statement_Local_Variable_Declaration_variableNames: Property = Property(name="variableNames", type=StringType)
activityecorelua_Statement_Local_Variable_Declaration.attributes={activityecorelua_Statement_Local_Variable_Declaration_variableNames}

# activityecorelua_Statement_FunctioncallOrAssignment class attributes and methods

# Statement_FunctioncallOrAssignment class attributes and methods

# activityecorelua_Expression_Nil class attributes and methods

# Expression class attributes and methods

# activityecorelua_Expression_True class attributes and methods

# activityecorelua_Expression_False class attributes and methods

# activityecorelua_Expression_Number class attributes and methods
activityecorelua_Expression_Number_value: Property = Property(name="value", type=FloatType)
activityecorelua_Expression_Number.attributes={activityecorelua_Expression_Number_value}

# activityecorelua_Expression_VarArgs class attributes and methods

# activityecorelua_Expression_String class attributes and methods
activityecorelua_Expression_String_value: Property = Property(name="value", type=StringType)
activityecorelua_Expression_String.attributes={activityecorelua_Expression_String_value}

# activityecorelua_Expression_Function class attributes and methods

# activityecorelua_Expression_TableConstructor class attributes and methods

# activityecorelua_Field class attributes and methods

# activityecorelua_Functioncall_Arguments class attributes and methods

# activityecorelua_Field_AddEntryToTable_Brackets class attributes and methods

# Field class attributes and methods

# activityecorelua_Field_AddEntryToTable class attributes and methods
activityecorelua_Field_AddEntryToTable_key: Property = Property(name="key", type=StringType)
activityecorelua_Field_AddEntryToTable.attributes={activityecorelua_Field_AddEntryToTable_key}

# activityecorelua_Field_AppendEntryToTable class attributes and methods

# activityecorelua_LastStatement_ReturnWithValue class attributes and methods

# LastStatement_Return class attributes and methods

# activityecorelua_Statement_Assignment class attributes and methods

# activityecorelua_Statement_CallMemberFunction class attributes and methods
activityecorelua_Statement_CallMemberFunction_memberFunctionName: Property = Property(name="memberFunctionName", type=StringType)
activityecorelua_Statement_CallMemberFunction.attributes={activityecorelua_Statement_CallMemberFunction_memberFunctionName}

# activityecorelua_Statement_CallFunction class attributes and methods

# activityecorelua_Expression_Or class attributes and methods

# activityecorelua_Expression_And class attributes and methods

# activityecorelua_Expression_Larger class attributes and methods

# activityecorelua_Expression_Larger_Equal class attributes and methods

# activityecorelua_Expression_Smaller class attributes and methods

# activityecorelua_Expression_Smaller_Equal class attributes and methods

# activityecorelua_Expression_Equal class attributes and methods

# activityecorelua_Expression_Not_Equal class attributes and methods

# activityecorelua_Expression_Concatenation class attributes and methods

# activityecorelua_Expression_Plus class attributes and methods

# activityecorelua_Expression_Minus class attributes and methods

# activityecorelua_Expression_Invert class attributes and methods

# activityecorelua_Expression_Exponentiation class attributes and methods

# activityecorelua_Expression_Multiplication class attributes and methods

# activityecorelua_Expression_Division class attributes and methods

# activityecorelua_Expression_Modulo class attributes and methods

# activityecorelua_Expression_Negate class attributes and methods

# activityecorelua_Expression_Length class attributes and methods

# activityecorelua_Expression_AccessArray class attributes and methods

# activityecorelua_Expression_CallMemberFunction class attributes and methods
activityecorelua_Expression_CallMemberFunction_memberFunctionName: Property = Property(name="memberFunctionName", type=StringType)
activityecorelua_Expression_CallMemberFunction.attributes={activityecorelua_Expression_CallMemberFunction_memberFunctionName}

# activityecorelua_Expression_CallFunction class attributes and methods

# activityecorelua_Expression_AccessMember class attributes and methods
activityecorelua_Expression_AccessMember_memberName: Property = Property(name="memberName", type=StringType)
activityecorelua_Expression_AccessMember.attributes={activityecorelua_Expression_AccessMember_memberName}

# activityecorelua_Expression_VariableName class attributes and methods
activityecorelua_Expression_VariableName_variable: Property = Property(name="variable", type=StringType)
activityecorelua_Expression_VariableName.attributes={activityecorelua_Expression_VariableName_variable}

# Relationships
eAttributeType0: BinaryAssociation = BinaryAssociation(
    name="eAttributeType0",
    ends={
        Property(name="activityecorelua_EDataType", type=activityecorelua_EAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_EAttribute", type=activityecorelua_EDataType, multiplicity=Multiplicity(1, 1))
    }
)
details1: BinaryAssociation = BinaryAssociation(
    name="details1",
    ends={
        Property(name="activityecorelua_EStringToStringMapEntry", type=activityecorelua_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_EAnnotation", type=activityecorelua_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eModelElement2: BinaryAssociation = BinaryAssociation(
    name="eModelElement2",
    ends={
        Property(name="EModelElement", type=activityecorelua_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="eAnnotations", type=activityecorelua_EModelElement, multiplicity=Multiplicity(0, 1))
    }
)
contents3: BinaryAssociation = BinaryAssociation(
    name="contents3",
    ends={
        Property(name="activityecorelua_EObject", type=activityecorelua_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_EAnnotation4", type=activityecorelua_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references5: BinaryAssociation = BinaryAssociation(
    name="references5",
    ends={
        Property(name="activityecorelua_EObject7", type=activityecorelua_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_EAnnotation6", type=activityecorelua_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
eAllStructuralFeatures27: BinaryAssociation = BinaryAssociation(
    name="eAllStructuralFeatures27",
    ends={
        Property(name="activityecorelua_EStructuralFeature", type=activityecorelua_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_EClass28", type=activityecorelua_EStructuralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
eSuperTypes9: BinaryAssociation = BinaryAssociation(
    name="eSuperTypes9",
    ends={
        Property(name="activityecorelua_EClass", type=activityecorelua_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_EClass8", type=activityecorelua_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
eOperations10: BinaryAssociation = BinaryAssociation(
    name="eOperations10",
    ends={
        Property(name="EOperation", type=activityecorelua_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="eContainingClass", type=activityecorelua_EOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eAllAttributes11: BinaryAssociation = BinaryAssociation(
    name="eAllAttributes11",
    ends={
        Property(name="activityecorelua_EAttribute13", type=activityecorelua_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_EClass12", type=activityecorelua_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eAllReferences14: BinaryAssociation = BinaryAssociation(
    name="eAllReferences14",
    ends={
        Property(name="activityecorelua_EReference", type=activityecorelua_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_EClass15", type=activityecorelua_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eReferences16: BinaryAssociation = BinaryAssociation(
    name="eReferences16",
    ends={
        Property(name="activityecorelua_EReference18", type=activityecorelua_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_EClass17", type=activityecorelua_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eAttributes19: BinaryAssociation = BinaryAssociation(
    name="eAttributes19",
    ends={
        Property(name="activityecorelua_EAttribute21", type=activityecorelua_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_EClass20", type=activityecorelua_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eAllContainments22: BinaryAssociation = BinaryAssociation(
    name="eAllContainments22",
    ends={
        Property(name="activityecorelua_EReference24", type=activityecorelua_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_EClass23", type=activityecorelua_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eAllOperations25: BinaryAssociation = BinaryAssociation(
    name="eAllOperations25",
    ends={
        Property(name="activityecorelua_EOperation", type=activityecorelua_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_EClass26", type=activityecorelua_EOperation, multiplicity=Multiplicity(0, 9999))
    }
)
eAllSuperTypes30: BinaryAssociation = BinaryAssociation(
    name="eAllSuperTypes30",
    ends={
        Property(name="activityecorelua_EClass31", type=activityecorelua_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_EClass29", type=activityecorelua_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
eIDAttribute32: BinaryAssociation = BinaryAssociation(
    name="eIDAttribute32",
    ends={
        Property(name="activityecorelua_EAttribute34", type=activityecorelua_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_EClass33", type=activityecorelua_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
eStructuralFeatures35: BinaryAssociation = BinaryAssociation(
    name="eStructuralFeatures35",
    ends={
        Property(name="EStructuralFeature", type=activityecorelua_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="eContainingClass36", type=activityecorelua_EStructuralFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eGenericSuperTypes37: BinaryAssociation = BinaryAssociation(
    name="eGenericSuperTypes37",
    ends={
        Property(name="activityecorelua_EGenericType", type=activityecorelua_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_EClass38", type=activityecorelua_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eAllGenericSuperTypes39: BinaryAssociation = BinaryAssociation(
    name="eAllGenericSuperTypes39",
    ends={
        Property(name="activityecorelua_EGenericType41", type=activityecorelua_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_EClass40", type=activityecorelua_EGenericType, multiplicity=Multiplicity(0, 9999))
    }
)
ePackage42: BinaryAssociation = BinaryAssociation(
    name="ePackage42",
    ends={
        Property(name="EPackage", type=activityecorelua_EClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="eClassifiers", type=activityecorelua_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
eTypeParameters43: BinaryAssociation = BinaryAssociation(
    name="eTypeParameters43",
    ends={
        Property(name="activityecorelua_ETypeParameter", type=activityecorelua_EClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_EClassifier", type=activityecorelua_ETypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eLiterals44: BinaryAssociation = BinaryAssociation(
    name="eLiterals44",
    ends={
        Property(name="EEnumLiteral", type=activityecorelua_EEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="eEnum", type=activityecorelua_EEnumLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eEnum45: BinaryAssociation = BinaryAssociation(
    name="eEnum45",
    ends={
        Property(name="EEnum", type=activityecorelua_EEnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="eLiterals", type=activityecorelua_EEnum, multiplicity=Multiplicity(0, 1))
    }
)
ePackage46: BinaryAssociation = BinaryAssociation(
    name="ePackage46",
    ends={
        Property(name="EPackage47", type=activityecorelua_EFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="eFactoryInstance", type=activityecorelua_EPackage, multiplicity=Multiplicity(1, 1))
    }
)
eAnnotations48: BinaryAssociation = BinaryAssociation(
    name="eAnnotations48",
    ends={
        Property(name="EAnnotation", type=activityecorelua_EModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="eModelElement", type=activityecorelua_EAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eContainingClass49: BinaryAssociation = BinaryAssociation(
    name="eContainingClass49",
    ends={
        Property(name="EClass", type=activityecorelua_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="eOperations", type=activityecorelua_EClass, multiplicity=Multiplicity(0, 1))
    }
)
eTypeParameters50: BinaryAssociation = BinaryAssociation(
    name="eTypeParameters50",
    ends={
        Property(name="activityecorelua_ETypeParameter52", type=activityecorelua_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_EOperation51", type=activityecorelua_ETypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eParameters53: BinaryAssociation = BinaryAssociation(
    name="eParameters53",
    ends={
        Property(name="EParameter", type=activityecorelua_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="eOperation", type=activityecorelua_EParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activity54: BinaryAssociation = BinaryAssociation(
    name="activity54",
    ends={
        Property(name="activityecorelua_Activity", type=activityecorelua_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_EOperation55", type=activityecorelua_Activity, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
eExceptions56: BinaryAssociation = BinaryAssociation(
    name="eExceptions56",
    ends={
        Property(name="activityecorelua_EClassifier58", type=activityecorelua_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_EOperation57", type=activityecorelua_EClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
eGenericExceptions59: BinaryAssociation = BinaryAssociation(
    name="eGenericExceptions59",
    ends={
        Property(name="activityecorelua_EGenericType61", type=activityecorelua_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_EOperation60", type=activityecorelua_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eFactoryInstance62: BinaryAssociation = BinaryAssociation(
    name="eFactoryInstance62",
    ends={
        Property(name="EFactory", type=activityecorelua_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ePackage", type=activityecorelua_EFactory, multiplicity=Multiplicity(1, 1))
    }
)
eClassifiers63: BinaryAssociation = BinaryAssociation(
    name="eClassifiers63",
    ends={
        Property(name="EClassifier", type=activityecorelua_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ePackage64", type=activityecorelua_EClassifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eSubpackages66: BinaryAssociation = BinaryAssociation(
    name="eSubpackages66",
    ends={
        Property(name="EPackage67", type=activityecorelua_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="eSuperPackage", type=activityecorelua_EPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eSuperPackage69: BinaryAssociation = BinaryAssociation(
    name="eSuperPackage69",
    ends={
        Property(name="EPackage70", type=activityecorelua_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="eSubpackages", type=activityecorelua_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
eOperation71: BinaryAssociation = BinaryAssociation(
    name="eOperation71",
    ends={
        Property(name="EOperation72", type=activityecorelua_EParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="eParameters", type=activityecorelua_EOperation, multiplicity=Multiplicity(0, 1))
    }
)
eOpposite74: BinaryAssociation = BinaryAssociation(
    name="eOpposite74",
    ends={
        Property(name="activityecorelua_EReference75", type=activityecorelua_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_EReference73", type=activityecorelua_EReference, multiplicity=Multiplicity(0, 1))
    }
)
eReferenceType76: BinaryAssociation = BinaryAssociation(
    name="eReferenceType76",
    ends={
        Property(name="activityecorelua_EClass78", type=activityecorelua_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_EReference77", type=activityecorelua_EClass, multiplicity=Multiplicity(1, 1))
    }
)
eKeys79: BinaryAssociation = BinaryAssociation(
    name="eKeys79",
    ends={
        Property(name="activityecorelua_EAttribute81", type=activityecorelua_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_EReference80", type=activityecorelua_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eContainingClass82: BinaryAssociation = BinaryAssociation(
    name="eContainingClass82",
    ends={
        Property(name="EClass83", type=activityecorelua_EStructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="eStructuralFeatures", type=activityecorelua_EClass, multiplicity=Multiplicity(0, 1))
    }
)
eType84: BinaryAssociation = BinaryAssociation(
    name="eType84",
    ends={
        Property(name="activityecorelua_EClassifier85", type=activityecorelua_ETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_ETypedElement", type=activityecorelua_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
eGenericType86: BinaryAssociation = BinaryAssociation(
    name="eGenericType86",
    ends={
        Property(name="activityecorelua_EGenericType88", type=activityecorelua_ETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_ETypedElement87", type=activityecorelua_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eUpperBound90: BinaryAssociation = BinaryAssociation(
    name="eUpperBound90",
    ends={
        Property(name="activityecorelua_EGenericType91", type=activityecorelua_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_EGenericType89", type=activityecorelua_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eTypeArguments93: BinaryAssociation = BinaryAssociation(
    name="eTypeArguments93",
    ends={
        Property(name="activityecorelua_EGenericType94", type=activityecorelua_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_EGenericType92", type=activityecorelua_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eRawType95: BinaryAssociation = BinaryAssociation(
    name="eRawType95",
    ends={
        Property(name="activityecorelua_EClassifier97", type=activityecorelua_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_EGenericType96", type=activityecorelua_EClassifier, multiplicity=Multiplicity(1, 1))
    }
)
eLowerBound99: BinaryAssociation = BinaryAssociation(
    name="eLowerBound99",
    ends={
        Property(name="activityecorelua_EGenericType100", type=activityecorelua_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_EGenericType98", type=activityecorelua_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eTypeParameter101: BinaryAssociation = BinaryAssociation(
    name="eTypeParameter101",
    ends={
        Property(name="activityecorelua_ETypeParameter103", type=activityecorelua_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_EGenericType102", type=activityecorelua_ETypeParameter, multiplicity=Multiplicity(0, 1))
    }
)
eClassifier104: BinaryAssociation = BinaryAssociation(
    name="eClassifier104",
    ends={
        Property(name="activityecorelua_EClassifier106", type=activityecorelua_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_EGenericType105", type=activityecorelua_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
eBounds107: BinaryAssociation = BinaryAssociation(
    name="eBounds107",
    ends={
        Property(name="activityecorelua_EGenericType109", type=activityecorelua_ETypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_ETypeParameter108", type=activityecorelua_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodes110: BinaryAssociation = BinaryAssociation(
    name="nodes110",
    ends={
        Property(name="ActivityNode", type=activityecorelua_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activity", type=activityecorelua_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges111: BinaryAssociation = BinaryAssociation(
    name="edges111",
    ends={
        Property(name="activityecorelua_ActivityEdge", type=activityecorelua_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Activity112", type=activityecorelua_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locals113: BinaryAssociation = BinaryAssociation(
    name="locals113",
    ends={
        Property(name="activityecorelua_Variable", type=activityecorelua_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Activity114", type=activityecorelua_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputs115: BinaryAssociation = BinaryAssociation(
    name="inputs115",
    ends={
        Property(name="activityecorelua_Variable117", type=activityecorelua_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Activity116", type=activityecorelua_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing118: BinaryAssociation = BinaryAssociation(
    name="outgoing118",
    ends={
        Property(name="ActivityEdge", type=activityecorelua_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=activityecorelua_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
incoming119: BinaryAssociation = BinaryAssociation(
    name="incoming119",
    ends={
        Property(name="ActivityEdge120", type=activityecorelua_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=activityecorelua_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
activity121: BinaryAssociation = BinaryAssociation(
    name="activity121",
    ends={
        Property(name="Activity", type=activityecorelua_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=activityecorelua_Activity, multiplicity=Multiplicity(1, 1))
    }
)
source122: BinaryAssociation = BinaryAssociation(
    name="source122",
    ends={
        Property(name="ActivityNode123", type=activityecorelua_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=activityecorelua_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
target124: BinaryAssociation = BinaryAssociation(
    name="target124",
    ends={
        Property(name="ActivityNode125", type=activityecorelua_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=activityecorelua_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
guard126: BinaryAssociation = BinaryAssociation(
    name="guard126",
    ends={
        Property(name="activityecorelua_BooleanVariable", type=activityecorelua_ControlFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_ControlFlow", type=activityecorelua_BooleanVariable, multiplicity=Multiplicity(0, 1))
    }
)
expressions127: BinaryAssociation = BinaryAssociation(
    name="expressions127",
    ends={
        Property(name="activityecorelua_Expression", type=activityecorelua_OpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_OpaqueAction", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialValue128: BinaryAssociation = BinaryAssociation(
    name="initialValue128",
    ends={
        Property(name="activityecorelua_Value", type=activityecorelua_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Variable129", type=activityecorelua_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
currentValue130: BinaryAssociation = BinaryAssociation(
    name="currentValue130",
    ends={
        Property(name="activityecorelua_Value132", type=activityecorelua_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Variable131", type=activityecorelua_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value133: BinaryAssociation = BinaryAssociation(
    name="value133",
    ends={
        Property(name="activityecorelua_Value134", type=activityecorelua_InputValue, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_InputValue", type=activityecorelua_Value, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable135: BinaryAssociation = BinaryAssociation(
    name="variable135",
    ends={
        Property(name="activityecorelua_Variable137", type=activityecorelua_InputValue, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_InputValue136", type=activityecorelua_Variable, multiplicity=Multiplicity(1, 1))
    }
)
inputValues138: BinaryAssociation = BinaryAssociation(
    name="inputValues138",
    ends={
        Property(name="activityecorelua_InputValue139", type=activityecorelua_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Input", type=activityecorelua_InputValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements140: BinaryAssociation = BinaryAssociation(
    name="statements140",
    ends={
        Property(name="activityecorelua_Statement", type=activityecorelua_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Block", type=activityecorelua_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnValue141: BinaryAssociation = BinaryAssociation(
    name="returnValue141",
    ends={
        Property(name="activityecorelua_LastStatement", type=activityecorelua_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Block142", type=activityecorelua_LastStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block143: BinaryAssociation = BinaryAssociation(
    name="block143",
    ends={
        Property(name="activityecorelua_Block144", type=activityecorelua_Statement_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Statement_Block", type=activityecorelua_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression145: BinaryAssociation = BinaryAssociation(
    name="expression145",
    ends={
        Property(name="activityecorelua_Expression146", type=activityecorelua_Statement_While, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Statement_While", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block147: BinaryAssociation = BinaryAssociation(
    name="block147",
    ends={
        Property(name="activityecorelua_Block149", type=activityecorelua_Statement_While, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Statement_While148", type=activityecorelua_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block150: BinaryAssociation = BinaryAssociation(
    name="block150",
    ends={
        Property(name="activityecorelua_Block151", type=activityecorelua_Statement_Repeat, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Statement_Repeat", type=activityecorelua_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression152: BinaryAssociation = BinaryAssociation(
    name="expression152",
    ends={
        Property(name="activityecorelua_Expression154", type=activityecorelua_Statement_Repeat, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Statement_Repeat153", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifExpression155: BinaryAssociation = BinaryAssociation(
    name="ifExpression155",
    ends={
        Property(name="activityecorelua_Expression156", type=activityecorelua_Statement_If_Then_Else, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Statement_If_Then_Else", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifBlock157: BinaryAssociation = BinaryAssociation(
    name="ifBlock157",
    ends={
        Property(name="activityecorelua_Block159", type=activityecorelua_Statement_If_Then_Else, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Statement_If_Then_Else158", type=activityecorelua_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseIf160: BinaryAssociation = BinaryAssociation(
    name="elseIf160",
    ends={
        Property(name="activityecorelua_Statement_If_Then_Else_ElseIfPart", type=activityecorelua_Statement_If_Then_Else, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Statement_If_Then_Else161", type=activityecorelua_Statement_If_Then_Else_ElseIfPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseBlock162: BinaryAssociation = BinaryAssociation(
    name="elseBlock162",
    ends={
        Property(name="activityecorelua_Block164", type=activityecorelua_Statement_If_Then_Else, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Statement_If_Then_Else163", type=activityecorelua_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseifExpression165: BinaryAssociation = BinaryAssociation(
    name="elseifExpression165",
    ends={
        Property(name="activityecorelua_Expression167", type=activityecorelua_Statement_If_Then_Else_ElseIfPart, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Statement_If_Then_Else_ElseIfPart166", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseifBlock168: BinaryAssociation = BinaryAssociation(
    name="elseifBlock168",
    ends={
        Property(name="activityecorelua_Block170", type=activityecorelua_Statement_If_Then_Else_ElseIfPart, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Statement_If_Then_Else_ElseIfPart169", type=activityecorelua_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
startExpr171: BinaryAssociation = BinaryAssociation(
    name="startExpr171",
    ends={
        Property(name="activityecorelua_Expression172", type=activityecorelua_Statement_For_Numeric, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Statement_For_Numeric", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
untilExpr173: BinaryAssociation = BinaryAssociation(
    name="untilExpr173",
    ends={
        Property(name="activityecorelua_Expression175", type=activityecorelua_Statement_For_Numeric, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Statement_For_Numeric174", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stepExpr176: BinaryAssociation = BinaryAssociation(
    name="stepExpr176",
    ends={
        Property(name="activityecorelua_Expression178", type=activityecorelua_Statement_For_Numeric, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Statement_For_Numeric177", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block179: BinaryAssociation = BinaryAssociation(
    name="block179",
    ends={
        Property(name="activityecorelua_Block181", type=activityecorelua_Statement_For_Numeric, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Statement_For_Numeric180", type=activityecorelua_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions182: BinaryAssociation = BinaryAssociation(
    name="expressions182",
    ends={
        Property(name="activityecorelua_Expression183", type=activityecorelua_Statement_For_Generic, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Statement_For_Generic", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block184: BinaryAssociation = BinaryAssociation(
    name="block184",
    ends={
        Property(name="activityecorelua_Block186", type=activityecorelua_Statement_For_Generic, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Statement_For_Generic185", type=activityecorelua_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function187: BinaryAssociation = BinaryAssociation(
    name="function187",
    ends={
        Property(name="activityecorelua_Function", type=activityecorelua_Statement_GlobalFunction_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Statement_GlobalFunction_Declaration", type=activityecorelua_Function, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function188: BinaryAssociation = BinaryAssociation(
    name="function188",
    ends={
        Property(name="activityecorelua_Function189", type=activityecorelua_Statement_LocalFunction_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Statement_LocalFunction_Declaration", type=activityecorelua_Function, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initialValue190: BinaryAssociation = BinaryAssociation(
    name="initialValue190",
    ends={
        Property(name="activityecorelua_Expression191", type=activityecorelua_Statement_Local_Variable_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Statement_Local_Variable_Declaration", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
function192: BinaryAssociation = BinaryAssociation(
    name="function192",
    ends={
        Property(name="activityecorelua_Function193", type=activityecorelua_Expression_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_Function", type=activityecorelua_Function, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fields194: BinaryAssociation = BinaryAssociation(
    name="fields194",
    ends={
        Property(name="activityecorelua_Field", type=activityecorelua_Expression_TableConstructor, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_TableConstructor", type=activityecorelua_Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body195: BinaryAssociation = BinaryAssociation(
    name="body195",
    ends={
        Property(name="activityecorelua_Block197", type=activityecorelua_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Function196", type=activityecorelua_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments219: BinaryAssociation = BinaryAssociation(
    name="arguments219",
    ends={
        Property(name="activityecorelua_Statement_CallFunction220", type=activityecorelua_Functioncall_Arguments, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="activityecorelua_Functioncall_Arguments221", type=activityecorelua_Statement_CallFunction, multiplicity=Multiplicity(1, 1))
    }
)
arguments198: BinaryAssociation = BinaryAssociation(
    name="arguments198",
    ends={
        Property(name="activityecorelua_Expression199", type=activityecorelua_Functioncall_Arguments, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Functioncall_Arguments", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value200: BinaryAssociation = BinaryAssociation(
    name="value200",
    ends={
        Property(name="activityecorelua_Expression202", type=activityecorelua_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Field201", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
indexExpression203: BinaryAssociation = BinaryAssociation(
    name="indexExpression203",
    ends={
        Property(name="activityecorelua_Expression204", type=activityecorelua_Field_AddEntryToTable_Brackets, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Field_AddEntryToTable_Brackets", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnValues205: BinaryAssociation = BinaryAssociation(
    name="returnValues205",
    ends={
        Property(name="activityecorelua_Expression206", type=activityecorelua_LastStatement_ReturnWithValue, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_LastStatement_ReturnWithValue", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable207: BinaryAssociation = BinaryAssociation(
    name="variable207",
    ends={
        Property(name="activityecorelua_Expression208", type=activityecorelua_Statement_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Statement_Assignment", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values209: BinaryAssociation = BinaryAssociation(
    name="values209",
    ends={
        Property(name="activityecorelua_Expression211", type=activityecorelua_Statement_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Statement_Assignment210", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
object212: BinaryAssociation = BinaryAssociation(
    name="object212",
    ends={
        Property(name="activityecorelua_Expression213", type=activityecorelua_Statement_CallMemberFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Statement_CallMemberFunction", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments214: BinaryAssociation = BinaryAssociation(
    name="arguments214",
    ends={
        Property(name="activityecorelua_Functioncall_Arguments216", type=activityecorelua_Statement_CallMemberFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Statement_CallMemberFunction215", type=activityecorelua_Functioncall_Arguments, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object217: BinaryAssociation = BinaryAssociation(
    name="object217",
    ends={
        Property(name="activityecorelua_Expression218", type=activityecorelua_Statement_CallFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Statement_CallFunction", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right249: BinaryAssociation = BinaryAssociation(
    name="right249",
    ends={
        Property(name="activityecorelua_Expression_Smaller_Equal250", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="activityecorelua_Expression251", type=activityecorelua_Expression_Smaller_Equal, multiplicity=Multiplicity(1, 1))
    }
)
left222: BinaryAssociation = BinaryAssociation(
    name="left222",
    ends={
        Property(name="activityecorelua_Expression223", type=activityecorelua_Expression_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_Or", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right224: BinaryAssociation = BinaryAssociation(
    name="right224",
    ends={
        Property(name="activityecorelua_Expression226", type=activityecorelua_Expression_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_Or225", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left227: BinaryAssociation = BinaryAssociation(
    name="left227",
    ends={
        Property(name="activityecorelua_Expression228", type=activityecorelua_Expression_And, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_And", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right229: BinaryAssociation = BinaryAssociation(
    name="right229",
    ends={
        Property(name="activityecorelua_Expression231", type=activityecorelua_Expression_And, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_And230", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left232: BinaryAssociation = BinaryAssociation(
    name="left232",
    ends={
        Property(name="activityecorelua_Expression233", type=activityecorelua_Expression_Larger, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_Larger", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right234: BinaryAssociation = BinaryAssociation(
    name="right234",
    ends={
        Property(name="activityecorelua_Expression236", type=activityecorelua_Expression_Larger, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_Larger235", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left237: BinaryAssociation = BinaryAssociation(
    name="left237",
    ends={
        Property(name="activityecorelua_Expression238", type=activityecorelua_Expression_Larger_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_Larger_Equal", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right239: BinaryAssociation = BinaryAssociation(
    name="right239",
    ends={
        Property(name="activityecorelua_Expression241", type=activityecorelua_Expression_Larger_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_Larger_Equal240", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left242: BinaryAssociation = BinaryAssociation(
    name="left242",
    ends={
        Property(name="activityecorelua_Expression243", type=activityecorelua_Expression_Smaller, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_Smaller", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right244: BinaryAssociation = BinaryAssociation(
    name="right244",
    ends={
        Property(name="activityecorelua_Expression246", type=activityecorelua_Expression_Smaller, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_Smaller245", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left247: BinaryAssociation = BinaryAssociation(
    name="left247",
    ends={
        Property(name="activityecorelua_Expression248", type=activityecorelua_Expression_Smaller_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_Smaller_Equal", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left252: BinaryAssociation = BinaryAssociation(
    name="left252",
    ends={
        Property(name="activityecorelua_Expression253", type=activityecorelua_Expression_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_Equal", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right254: BinaryAssociation = BinaryAssociation(
    name="right254",
    ends={
        Property(name="activityecorelua_Expression256", type=activityecorelua_Expression_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_Equal255", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left257: BinaryAssociation = BinaryAssociation(
    name="left257",
    ends={
        Property(name="activityecorelua_Expression258", type=activityecorelua_Expression_Not_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_Not_Equal", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right259: BinaryAssociation = BinaryAssociation(
    name="right259",
    ends={
        Property(name="activityecorelua_Expression261", type=activityecorelua_Expression_Not_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_Not_Equal260", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left262: BinaryAssociation = BinaryAssociation(
    name="left262",
    ends={
        Property(name="activityecorelua_Expression263", type=activityecorelua_Expression_Concatenation, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_Concatenation", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right264: BinaryAssociation = BinaryAssociation(
    name="right264",
    ends={
        Property(name="activityecorelua_Expression266", type=activityecorelua_Expression_Concatenation, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_Concatenation265", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left267: BinaryAssociation = BinaryAssociation(
    name="left267",
    ends={
        Property(name="activityecorelua_Expression268", type=activityecorelua_Expression_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_Plus", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right269: BinaryAssociation = BinaryAssociation(
    name="right269",
    ends={
        Property(name="activityecorelua_Expression271", type=activityecorelua_Expression_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_Plus270", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left272: BinaryAssociation = BinaryAssociation(
    name="left272",
    ends={
        Property(name="activityecorelua_Expression273", type=activityecorelua_Expression_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_Minus", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right274: BinaryAssociation = BinaryAssociation(
    name="right274",
    ends={
        Property(name="activityecorelua_Expression276", type=activityecorelua_Expression_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_Minus275", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp296: BinaryAssociation = BinaryAssociation(
    name="exp296",
    ends={
        Property(name="activityecorelua_Expression297", type=activityecorelua_Expression_Invert, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_Invert", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left298: BinaryAssociation = BinaryAssociation(
    name="left298",
    ends={
        Property(name="activityecorelua_Expression299", type=activityecorelua_Expression_Exponentiation, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_Exponentiation", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left277: BinaryAssociation = BinaryAssociation(
    name="left277",
    ends={
        Property(name="activityecorelua_Expression278", type=activityecorelua_Expression_Multiplication, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_Multiplication", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right300: BinaryAssociation = BinaryAssociation(
    name="right300",
    ends={
        Property(name="activityecorelua_Expression302", type=activityecorelua_Expression_Exponentiation, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_Exponentiation301", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right279: BinaryAssociation = BinaryAssociation(
    name="right279",
    ends={
        Property(name="activityecorelua_Expression281", type=activityecorelua_Expression_Multiplication, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_Multiplication280", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left282: BinaryAssociation = BinaryAssociation(
    name="left282",
    ends={
        Property(name="activityecorelua_Expression283", type=activityecorelua_Expression_Division, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_Division", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right284: BinaryAssociation = BinaryAssociation(
    name="right284",
    ends={
        Property(name="activityecorelua_Expression286", type=activityecorelua_Expression_Division, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_Division285", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left287: BinaryAssociation = BinaryAssociation(
    name="left287",
    ends={
        Property(name="activityecorelua_Expression288", type=activityecorelua_Expression_Modulo, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_Modulo", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right289: BinaryAssociation = BinaryAssociation(
    name="right289",
    ends={
        Property(name="activityecorelua_Expression291", type=activityecorelua_Expression_Modulo, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_Modulo290", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp292: BinaryAssociation = BinaryAssociation(
    name="exp292",
    ends={
        Property(name="activityecorelua_Expression293", type=activityecorelua_Expression_Negate, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_Negate", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp294: BinaryAssociation = BinaryAssociation(
    name="exp294",
    ends={
        Property(name="activityecorelua_Expression295", type=activityecorelua_Expression_Length, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_Length", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments310: BinaryAssociation = BinaryAssociation(
    name="arguments310",
    ends={
        Property(name="activityecorelua_Functioncall_Arguments312", type=activityecorelua_Expression_CallFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_CallFunction311", type=activityecorelua_Functioncall_Arguments, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
array313: BinaryAssociation = BinaryAssociation(
    name="array313",
    ends={
        Property(name="activityecorelua_Expression314", type=activityecorelua_Expression_AccessArray, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_AccessArray", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
index315: BinaryAssociation = BinaryAssociation(
    name="index315",
    ends={
        Property(name="activityecorelua_Expression317", type=activityecorelua_Expression_AccessArray, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_AccessArray316", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object303: BinaryAssociation = BinaryAssociation(
    name="object303",
    ends={
        Property(name="activityecorelua_Expression304", type=activityecorelua_Expression_CallMemberFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_CallMemberFunction", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments305: BinaryAssociation = BinaryAssociation(
    name="arguments305",
    ends={
        Property(name="activityecorelua_Functioncall_Arguments307", type=activityecorelua_Expression_CallMemberFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_CallMemberFunction306", type=activityecorelua_Functioncall_Arguments, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object308: BinaryAssociation = BinaryAssociation(
    name="object308",
    ends={
        Property(name="activityecorelua_Expression309", type=activityecorelua_Expression_CallFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_CallFunction", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object318: BinaryAssociation = BinaryAssociation(
    name="object318",
    ends={
        Property(name="activityecorelua_Expression319", type=activityecorelua_Expression_AccessMember, multiplicity=Multiplicity(1, 1)),
        Property(name="activityecorelua_Expression_AccessMember", type=activityecorelua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_activityecorelua_EAttribute_EStructuralFeature = Generalization(general=EStructuralFeature, specific=activityecorelua_EAttribute)
gen_activityecorelua_EAnnotation_EModelElement = Generalization(general=EModelElement, specific=activityecorelua_EAnnotation)
gen_activityecorelua_EClass_EClassifier = Generalization(general=EClassifier, specific=activityecorelua_EClass)
gen_activityecorelua_EEnum_EDataType = Generalization(general=EDataType, specific=activityecorelua_EEnum)
gen_activityecorelua_EClassifier_ENamedElement = Generalization(general=ENamedElement, specific=activityecorelua_EClassifier)
gen_activityecorelua_EDataType_EClassifier = Generalization(general=EClassifier, specific=activityecorelua_EDataType)
gen_activityecorelua_EEnumLiteral_ENamedElement = Generalization(general=ENamedElement, specific=activityecorelua_EEnumLiteral)
gen_activityecorelua_EFactory_EModelElement = Generalization(general=EModelElement, specific=activityecorelua_EFactory)
gen_activityecorelua_ENamedElement_EModelElement = Generalization(general=EModelElement, specific=activityecorelua_ENamedElement)
gen_activityecorelua_EOperation_ETypedElement = Generalization(general=ETypedElement, specific=activityecorelua_EOperation)
gen_activityecorelua_EPackage_ENamedElement = Generalization(general=ENamedElement, specific=activityecorelua_EPackage)
gen_activityecorelua_EParameter_ETypedElement = Generalization(general=ETypedElement, specific=activityecorelua_EParameter)
gen_activityecorelua_EReference_EStructuralFeature = Generalization(general=EStructuralFeature, specific=activityecorelua_EReference)
gen_activityecorelua_EStructuralFeature_ETypedElement = Generalization(general=ETypedElement, specific=activityecorelua_EStructuralFeature)
gen_activityecorelua_ETypedElement_ENamedElement = Generalization(general=ENamedElement, specific=activityecorelua_ETypedElement)
gen_activityecorelua_ETypeParameter_ENamedElement = Generalization(general=ENamedElement, specific=activityecorelua_ETypeParameter)
gen_activityecorelua_Activity_NamedElement = Generalization(general=NamedElement, specific=activityecorelua_Activity)
gen_activityecorelua_ActivityNode_NamedElement = Generalization(general=NamedElement, specific=activityecorelua_ActivityNode)
gen_activityecorelua_ActivityEdge_NamedElement = Generalization(general=NamedElement, specific=activityecorelua_ActivityEdge)
gen_activityecorelua_ControlFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=activityecorelua_ControlFlow)
gen_activityecorelua_ControlNode_ActivityNode = Generalization(general=ActivityNode, specific=activityecorelua_ControlNode)
gen_activityecorelua_ExecutableNode_ActivityNode = Generalization(general=ActivityNode, specific=activityecorelua_ExecutableNode)
gen_activityecorelua_Action_ExecutableNode = Generalization(general=ExecutableNode, specific=activityecorelua_Action)
gen_activityecorelua_OpaqueAction_Action = Generalization(general=Action, specific=activityecorelua_OpaqueAction)
gen_activityecorelua_InitialNode_ControlNode = Generalization(general=ControlNode, specific=activityecorelua_InitialNode)
gen_activityecorelua_FinalNode_ControlNode = Generalization(general=ControlNode, specific=activityecorelua_FinalNode)
gen_activityecorelua_ActivityFinalNode_FinalNode = Generalization(general=FinalNode, specific=activityecorelua_ActivityFinalNode)
gen_activityecorelua_ForkNode_ControlNode = Generalization(general=ControlNode, specific=activityecorelua_ForkNode)
gen_activityecorelua_JoinNode_ControlNode = Generalization(general=ControlNode, specific=activityecorelua_JoinNode)
gen_activityecorelua_MergeNode_ControlNode = Generalization(general=ControlNode, specific=activityecorelua_MergeNode)
gen_activityecorelua_DecisionNode_ControlNode = Generalization(general=ControlNode, specific=activityecorelua_DecisionNode)
gen_activityecorelua_Statement_Repeat_Statement = Generalization(general=Statement, specific=activityecorelua_Statement_Repeat)
gen_activityecorelua_IntegerVariable_Variable = Generalization(general=Variable, specific=activityecorelua_IntegerVariable)
gen_activityecorelua_BooleanVariable_Variable = Generalization(general=Variable, specific=activityecorelua_BooleanVariable)
gen_activityecorelua_BooleanValue_Value = Generalization(general=Value, specific=activityecorelua_BooleanValue)
gen_activityecorelua_IntegerValue_Value = Generalization(general=Value, specific=activityecorelua_IntegerValue)
gen_activityecorelua_Block_Chunk = Generalization(general=Chunk, specific=activityecorelua_Block)
gen_activityecorelua_LastStatement_Return_LastStatement = Generalization(general=LastStatement, specific=activityecorelua_LastStatement_Return)
gen_activityecorelua_LastStatement_Break_LastStatement = Generalization(general=LastStatement, specific=activityecorelua_LastStatement_Break)
gen_activityecorelua_Statement_Block_Statement = Generalization(general=Statement, specific=activityecorelua_Statement_Block)
gen_activityecorelua_Statement_While_Statement = Generalization(general=Statement, specific=activityecorelua_Statement_While)
gen_activityecorelua_Statement_If_Then_Else_Statement = Generalization(general=Statement, specific=activityecorelua_Statement_If_Then_Else)
gen_activityecorelua_Statement_For_Numeric_Statement = Generalization(general=Statement, specific=activityecorelua_Statement_For_Numeric)
gen_activityecorelua_Statement_For_Generic_Statement = Generalization(general=Statement, specific=activityecorelua_Statement_For_Generic)
gen_activityecorelua_Statement_GlobalFunction_Declaration_Statement = Generalization(general=Statement, specific=activityecorelua_Statement_GlobalFunction_Declaration)
gen_activityecorelua_Statement_LocalFunction_Declaration_Statement = Generalization(general=Statement, specific=activityecorelua_Statement_LocalFunction_Declaration)
gen_activityecorelua_Statement_Local_Variable_Declaration_Statement = Generalization(general=Statement, specific=activityecorelua_Statement_Local_Variable_Declaration)
gen_activityecorelua_Statement_FunctioncallOrAssignment_Statement = Generalization(general=Statement, specific=activityecorelua_Statement_FunctioncallOrAssignment)
gen_activityecorelua_Expression_Statement_FunctioncallOrAssignment = Generalization(general=Statement_FunctioncallOrAssignment, specific=activityecorelua_Expression)
gen_activityecorelua_Expression_Nil_Expression = Generalization(general=Expression, specific=activityecorelua_Expression_Nil)
gen_activityecorelua_Expression_True_Expression = Generalization(general=Expression, specific=activityecorelua_Expression_True)
gen_activityecorelua_Expression_False_Expression = Generalization(general=Expression, specific=activityecorelua_Expression_False)
gen_activityecorelua_Expression_Number_Expression = Generalization(general=Expression, specific=activityecorelua_Expression_Number)
gen_activityecorelua_Expression_VarArgs_Expression = Generalization(general=Expression, specific=activityecorelua_Expression_VarArgs)
gen_activityecorelua_Expression_String_Expression = Generalization(general=Expression, specific=activityecorelua_Expression_String)
gen_activityecorelua_Expression_Function_Expression = Generalization(general=Expression, specific=activityecorelua_Expression_Function)
gen_activityecorelua_Expression_TableConstructor_Expression = Generalization(general=Expression, specific=activityecorelua_Expression_TableConstructor)
gen_activityecorelua_Field_AddEntryToTable_Brackets_Field = Generalization(general=Field, specific=activityecorelua_Field_AddEntryToTable_Brackets)
gen_activityecorelua_Field_AddEntryToTable_Field = Generalization(general=Field, specific=activityecorelua_Field_AddEntryToTable)
gen_activityecorelua_Field_AppendEntryToTable_Field = Generalization(general=Field, specific=activityecorelua_Field_AppendEntryToTable)
gen_activityecorelua_LastStatement_ReturnWithValue_LastStatement_Return = Generalization(general=LastStatement_Return, specific=activityecorelua_LastStatement_ReturnWithValue)
gen_activityecorelua_Statement_Assignment_Statement_FunctioncallOrAssignment = Generalization(general=Statement_FunctioncallOrAssignment, specific=activityecorelua_Statement_Assignment)
gen_activityecorelua_Statement_CallMemberFunction_Statement_FunctioncallOrAssignment = Generalization(general=Statement_FunctioncallOrAssignment, specific=activityecorelua_Statement_CallMemberFunction)
gen_activityecorelua_Statement_CallFunction_Statement_FunctioncallOrAssignment = Generalization(general=Statement_FunctioncallOrAssignment, specific=activityecorelua_Statement_CallFunction)
gen_activityecorelua_Expression_Or_Expression = Generalization(general=Expression, specific=activityecorelua_Expression_Or)
gen_activityecorelua_Expression_And_Expression = Generalization(general=Expression, specific=activityecorelua_Expression_And)
gen_activityecorelua_Expression_Larger_Expression = Generalization(general=Expression, specific=activityecorelua_Expression_Larger)
gen_activityecorelua_Expression_Larger_Equal_Expression = Generalization(general=Expression, specific=activityecorelua_Expression_Larger_Equal)
gen_activityecorelua_Expression_Smaller_Expression = Generalization(general=Expression, specific=activityecorelua_Expression_Smaller)
gen_activityecorelua_Expression_Smaller_Equal_Expression = Generalization(general=Expression, specific=activityecorelua_Expression_Smaller_Equal)
gen_activityecorelua_Expression_Equal_Expression = Generalization(general=Expression, specific=activityecorelua_Expression_Equal)
gen_activityecorelua_Expression_Not_Equal_Expression = Generalization(general=Expression, specific=activityecorelua_Expression_Not_Equal)
gen_activityecorelua_Expression_Concatenation_Expression = Generalization(general=Expression, specific=activityecorelua_Expression_Concatenation)
gen_activityecorelua_Expression_Plus_Expression = Generalization(general=Expression, specific=activityecorelua_Expression_Plus)
gen_activityecorelua_Expression_Minus_Expression = Generalization(general=Expression, specific=activityecorelua_Expression_Minus)
gen_activityecorelua_Expression_Invert_Expression = Generalization(general=Expression, specific=activityecorelua_Expression_Invert)
gen_activityecorelua_Expression_Exponentiation_Expression = Generalization(general=Expression, specific=activityecorelua_Expression_Exponentiation)
gen_activityecorelua_Expression_Multiplication_Expression = Generalization(general=Expression, specific=activityecorelua_Expression_Multiplication)
gen_activityecorelua_Expression_Division_Expression = Generalization(general=Expression, specific=activityecorelua_Expression_Division)
gen_activityecorelua_Expression_Modulo_Expression = Generalization(general=Expression, specific=activityecorelua_Expression_Modulo)
gen_activityecorelua_Expression_Negate_Expression = Generalization(general=Expression, specific=activityecorelua_Expression_Negate)
gen_activityecorelua_Expression_Length_Expression = Generalization(general=Expression, specific=activityecorelua_Expression_Length)
gen_activityecorelua_Expression_AccessArray_Expression = Generalization(general=Expression, specific=activityecorelua_Expression_AccessArray)
gen_activityecorelua_Expression_CallMemberFunction_Expression = Generalization(general=Expression, specific=activityecorelua_Expression_CallMemberFunction)
gen_activityecorelua_Expression_CallFunction_Expression = Generalization(general=Expression, specific=activityecorelua_Expression_CallFunction)
gen_activityecorelua_Expression_AccessMember_Expression = Generalization(general=Expression, specific=activityecorelua_Expression_AccessMember)
gen_activityecorelua_Expression_VariableName_Expression = Generalization(general=Expression, specific=activityecorelua_Expression_VariableName)

# Domain Model
domain_model = DomainModel(
    name="activityecorelua",
    types={activityecorelua_EAttribute, EStructuralFeature, activityecorelua_EDataType, activityecorelua_EAnnotation, EModelElement, activityecorelua_EStringToStringMapEntry, activityecorelua_EModelElement, activityecorelua_EObject, activityecorelua_EClass, EClassifier, activityecorelua_EStructuralFeature, activityecorelua_EOperation, activityecorelua_EReference, activityecorelua_EEnum, EDataType, activityecorelua_EGenericType, activityecorelua_EClassifier, ENamedElement, activityecorelua_EPackage, activityecorelua_ETypeParameter, activityecorelua_EEnumLiteral, activityecorelua_EFactory, activityecorelua_ENamedElement, ETypedElement, activityecorelua_EParameter, activityecorelua_Activity, activityecorelua_ETypedElement, activityecorelua_Variable, NamedElement, activityecorelua_ActivityNode, activityecorelua_ActivityEdge, activityecorelua_Value, activityecorelua_ControlFlow, ActivityEdge, activityecorelua_BooleanVariable, activityecorelua_ControlNode, ActivityNode, activityecorelua_ExecutableNode, activityecorelua_Action, ExecutableNode, activityecorelua_OpaqueAction, Action, activityecorelua_Expression, activityecorelua_NamedElement, activityecorelua_InitialNode, ControlNode, activityecorelua_FinalNode, activityecorelua_ActivityFinalNode, FinalNode, activityecorelua_ForkNode, activityecorelua_JoinNode, activityecorelua_MergeNode, activityecorelua_DecisionNode, activityecorelua_Statement_Repeat, activityecorelua_IntegerVariable, Variable, activityecorelua_BooleanValue, Value, activityecorelua_IntegerValue, activityecorelua_InputValue, activityecorelua_Input, activityecorelua_Chunk, activityecorelua_Block, Chunk, activityecorelua_Statement, activityecorelua_LastStatement, activityecorelua_LastStatement_Return, LastStatement, activityecorelua_LastStatement_Break, activityecorelua_Statement_Block, Statement, activityecorelua_Statement_While, activityecorelua_Statement_If_Then_Else, activityecorelua_Statement_If_Then_Else_ElseIfPart, activityecorelua_Statement_For_Numeric, activityecorelua_Statement_For_Generic, activityecorelua_Statement_GlobalFunction_Declaration, activityecorelua_Function, activityecorelua_Statement_LocalFunction_Declaration, activityecorelua_Statement_Local_Variable_Declaration, activityecorelua_Statement_FunctioncallOrAssignment, Statement_FunctioncallOrAssignment, activityecorelua_Expression_Nil, Expression, activityecorelua_Expression_True, activityecorelua_Expression_False, activityecorelua_Expression_Number, activityecorelua_Expression_VarArgs, activityecorelua_Expression_String, activityecorelua_Expression_Function, activityecorelua_Expression_TableConstructor, activityecorelua_Field, activityecorelua_Functioncall_Arguments, activityecorelua_Field_AddEntryToTable_Brackets, Field, activityecorelua_Field_AddEntryToTable, activityecorelua_Field_AppendEntryToTable, activityecorelua_LastStatement_ReturnWithValue, LastStatement_Return, activityecorelua_Statement_Assignment, activityecorelua_Statement_CallMemberFunction, activityecorelua_Statement_CallFunction, activityecorelua_Expression_Or, activityecorelua_Expression_And, activityecorelua_Expression_Larger, activityecorelua_Expression_Larger_Equal, activityecorelua_Expression_Smaller, activityecorelua_Expression_Smaller_Equal, activityecorelua_Expression_Equal, activityecorelua_Expression_Not_Equal, activityecorelua_Expression_Concatenation, activityecorelua_Expression_Plus, activityecorelua_Expression_Minus, activityecorelua_Expression_Invert, activityecorelua_Expression_Exponentiation, activityecorelua_Expression_Multiplication, activityecorelua_Expression_Division, activityecorelua_Expression_Modulo, activityecorelua_Expression_Negate, activityecorelua_Expression_Length, activityecorelua_Expression_AccessArray, activityecorelua_Expression_CallMemberFunction, activityecorelua_Expression_CallFunction, activityecorelua_Expression_AccessMember, activityecorelua_Expression_VariableName},
    associations={eAttributeType0, details1, eModelElement2, contents3, references5, eAllStructuralFeatures27, eSuperTypes9, eOperations10, eAllAttributes11, eAllReferences14, eReferences16, eAttributes19, eAllContainments22, eAllOperations25, eAllSuperTypes30, eIDAttribute32, eStructuralFeatures35, eGenericSuperTypes37, eAllGenericSuperTypes39, ePackage42, eTypeParameters43, eLiterals44, eEnum45, ePackage46, eAnnotations48, eContainingClass49, eTypeParameters50, eParameters53, activity54, eExceptions56, eGenericExceptions59, eFactoryInstance62, eClassifiers63, eSubpackages66, eSuperPackage69, eOperation71, eOpposite74, eReferenceType76, eKeys79, eContainingClass82, eType84, eGenericType86, eUpperBound90, eTypeArguments93, eRawType95, eLowerBound99, eTypeParameter101, eClassifier104, eBounds107, nodes110, edges111, locals113, inputs115, outgoing118, incoming119, activity121, source122, target124, guard126, expressions127, initialValue128, currentValue130, value133, variable135, inputValues138, statements140, returnValue141, block143, expression145, block147, block150, expression152, ifExpression155, ifBlock157, elseIf160, elseBlock162, elseifExpression165, elseifBlock168, startExpr171, untilExpr173, stepExpr176, block179, expressions182, block184, function187, function188, initialValue190, function192, fields194, body195, arguments219, arguments198, value200, indexExpression203, returnValues205, variable207, values209, object212, arguments214, object217, right249, left222, right224, left227, right229, left232, right234, left237, right239, left242, right244, left247, left252, right254, left257, right259, left262, right264, left267, right269, left272, right274, exp296, left298, left277, right300, right279, left282, right284, left287, right289, exp292, exp294, arguments310, array313, index315, object303, arguments305, object308, object318},
    generalizations={gen_activityecorelua_EAttribute_EStructuralFeature, gen_activityecorelua_EAnnotation_EModelElement, gen_activityecorelua_EClass_EClassifier, gen_activityecorelua_EEnum_EDataType, gen_activityecorelua_EClassifier_ENamedElement, gen_activityecorelua_EDataType_EClassifier, gen_activityecorelua_EEnumLiteral_ENamedElement, gen_activityecorelua_EFactory_EModelElement, gen_activityecorelua_ENamedElement_EModelElement, gen_activityecorelua_EOperation_ETypedElement, gen_activityecorelua_EPackage_ENamedElement, gen_activityecorelua_EParameter_ETypedElement, gen_activityecorelua_EReference_EStructuralFeature, gen_activityecorelua_EStructuralFeature_ETypedElement, gen_activityecorelua_ETypedElement_ENamedElement, gen_activityecorelua_ETypeParameter_ENamedElement, gen_activityecorelua_Activity_NamedElement, gen_activityecorelua_ActivityNode_NamedElement, gen_activityecorelua_ActivityEdge_NamedElement, gen_activityecorelua_ControlFlow_ActivityEdge, gen_activityecorelua_ControlNode_ActivityNode, gen_activityecorelua_ExecutableNode_ActivityNode, gen_activityecorelua_Action_ExecutableNode, gen_activityecorelua_OpaqueAction_Action, gen_activityecorelua_InitialNode_ControlNode, gen_activityecorelua_FinalNode_ControlNode, gen_activityecorelua_ActivityFinalNode_FinalNode, gen_activityecorelua_ForkNode_ControlNode, gen_activityecorelua_JoinNode_ControlNode, gen_activityecorelua_MergeNode_ControlNode, gen_activityecorelua_DecisionNode_ControlNode, gen_activityecorelua_Statement_Repeat_Statement, gen_activityecorelua_IntegerVariable_Variable, gen_activityecorelua_BooleanVariable_Variable, gen_activityecorelua_BooleanValue_Value, gen_activityecorelua_IntegerValue_Value, gen_activityecorelua_Block_Chunk, gen_activityecorelua_LastStatement_Return_LastStatement, gen_activityecorelua_LastStatement_Break_LastStatement, gen_activityecorelua_Statement_Block_Statement, gen_activityecorelua_Statement_While_Statement, gen_activityecorelua_Statement_If_Then_Else_Statement, gen_activityecorelua_Statement_For_Numeric_Statement, gen_activityecorelua_Statement_For_Generic_Statement, gen_activityecorelua_Statement_GlobalFunction_Declaration_Statement, gen_activityecorelua_Statement_LocalFunction_Declaration_Statement, gen_activityecorelua_Statement_Local_Variable_Declaration_Statement, gen_activityecorelua_Statement_FunctioncallOrAssignment_Statement, gen_activityecorelua_Expression_Statement_FunctioncallOrAssignment, gen_activityecorelua_Expression_Nil_Expression, gen_activityecorelua_Expression_True_Expression, gen_activityecorelua_Expression_False_Expression, gen_activityecorelua_Expression_Number_Expression, gen_activityecorelua_Expression_VarArgs_Expression, gen_activityecorelua_Expression_String_Expression, gen_activityecorelua_Expression_Function_Expression, gen_activityecorelua_Expression_TableConstructor_Expression, gen_activityecorelua_Field_AddEntryToTable_Brackets_Field, gen_activityecorelua_Field_AddEntryToTable_Field, gen_activityecorelua_Field_AppendEntryToTable_Field, gen_activityecorelua_LastStatement_ReturnWithValue_LastStatement_Return, gen_activityecorelua_Statement_Assignment_Statement_FunctioncallOrAssignment, gen_activityecorelua_Statement_CallMemberFunction_Statement_FunctioncallOrAssignment, gen_activityecorelua_Statement_CallFunction_Statement_FunctioncallOrAssignment, gen_activityecorelua_Expression_Or_Expression, gen_activityecorelua_Expression_And_Expression, gen_activityecorelua_Expression_Larger_Expression, gen_activityecorelua_Expression_Larger_Equal_Expression, gen_activityecorelua_Expression_Smaller_Expression, gen_activityecorelua_Expression_Smaller_Equal_Expression, gen_activityecorelua_Expression_Equal_Expression, gen_activityecorelua_Expression_Not_Equal_Expression, gen_activityecorelua_Expression_Concatenation_Expression, gen_activityecorelua_Expression_Plus_Expression, gen_activityecorelua_Expression_Minus_Expression, gen_activityecorelua_Expression_Invert_Expression, gen_activityecorelua_Expression_Exponentiation_Expression, gen_activityecorelua_Expression_Multiplication_Expression, gen_activityecorelua_Expression_Division_Expression, gen_activityecorelua_Expression_Modulo_Expression, gen_activityecorelua_Expression_Negate_Expression, gen_activityecorelua_Expression_Length_Expression, gen_activityecorelua_Expression_AccessArray_Expression, gen_activityecorelua_Expression_CallMemberFunction_Expression, gen_activityecorelua_Expression_CallFunction_Expression, gen_activityecorelua_Expression_AccessMember_Expression, gen_activityecorelua_Expression_VariableName_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)