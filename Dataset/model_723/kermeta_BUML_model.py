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
ConstraintLanguage: Enumeration = Enumeration(
    name="ConstraintLanguage",
    literals={
            EnumerationLiteral(name="kermeta"),
			EnumerationLiteral(name="ocl")
    }
)

ConstraintType: Enumeration = Enumeration(
    name="ConstraintType",
    literals={
            EnumerationLiteral(name="inv"),
			EnumerationLiteral(name="pre"),
			EnumerationLiteral(name="post")
    }
)

# Classes
Expression = Class(name="Expression")
behavior_CallExpression = Class(name="behavior::CallExpression")
behavior_Expression = Class(name="behavior::Expression")
org_behavior_Expression = Class(name="org::behavior::Expression", is_abstract=True)
structure_KermetaModelElement = Class(name="structure::KermetaModelElement")
structure_TypeContainer = Class(name="structure::TypeContainer")
structure_Type = Class(name="structure::Type")
org_behavior_Assignment = Class(name="org::behavior::Assignment")
org_behavior_CallExpression = Class(name="org::behavior::CallExpression", is_abstract=True)
org_behavior_Block = Class(name="org::behavior::Block")
behavior_Rescue = Class(name="behavior::Rescue")
org_behavior_CallVariable = Class(name="org::behavior::CallVariable")
CallExpression = Class(name="CallExpression")
org_behavior_CallFeature = Class(name="org::behavior::CallFeature", is_abstract=True)
org_behavior_CallSuperOperation = Class(name="org::behavior::CallSuperOperation")
CallOperation = Class(name="CallOperation")
org_behavior_CallResult = Class(name="org::behavior::CallResult")
CallVariable = Class(name="CallVariable")
org_behavior_CallValue = Class(name="org::behavior::CallValue")
org_behavior_Conditional = Class(name="org::behavior::Conditional")
org_behavior_Raise = Class(name="org::behavior::Raise")
org_behavior_Rescue = Class(name="org::behavior::Rescue")
KermetaModelElement = Class(name="KermetaModelElement")
behavior_TypeReference = Class(name="behavior::TypeReference")
org_behavior_TypeReference = Class(name="org::behavior::TypeReference")
MultiplicityElement = Class(name="MultiplicityElement")
org_behavior_Literal = Class(name="org::behavior::Literal", is_abstract=True)
org_behavior_EmptyExpression = Class(name="org::behavior::EmptyExpression")
org_behavior_JavaStaticCall = Class(name="org::behavior::JavaStaticCall")
org_behavior_LambdaExpression = Class(name="org::behavior::LambdaExpression")
behavior_LambdaParameter = Class(name="behavior::LambdaParameter")
org_behavior_LambdaParameter = Class(name="org::behavior::LambdaParameter")
org_behavior_IntegerLiteral = Class(name="org::behavior::IntegerLiteral")
Literal = Class(name="Literal")
org_behavior_StringLiteral = Class(name="org::behavior::StringLiteral")
org_behavior_BooleanLiteral = Class(name="org::behavior::BooleanLiteral")
org_behavior_CallTypeLiteral = Class(name="org::behavior::CallTypeLiteral")
org_behavior_VoidLiteral = Class(name="org::behavior::VoidLiteral")
org_behavior_Loop = Class(name="org::behavior::Loop")
org_behavior_SelfExpression = Class(name="org::behavior::SelfExpression")
org_behavior_VariableDecl = Class(name="org::behavior::VariableDecl")
org_behavior_UnresolvedCall = Class(name="org::behavior::UnresolvedCall")
structure_UnresolvedReference = Class(name="structure::UnresolvedReference")
structure_Using = Class(name="structure::Using")
org_behavior_CallOperation = Class(name="org::behavior::CallOperation")
CallFeature = Class(name="CallFeature")
structure_Operation = Class(name="structure::Operation")
org_behavior_CallProperty = Class(name="org::behavior::CallProperty")
structure_Property = Class(name="structure::Property")
org_behavior_CallEnumLiteral = Class(name="org::behavior::CallEnumLiteral")
structure_EnumerationLiteral = Class(name="structure::EnumerationLiteral")
org_behavior_CallModelTransformation = Class(name="org::behavior::CallModelTransformation")
structure_ModelTransformation = Class(name="structure::ModelTransformation")
org_structure_KermetaModelElement = Class(name="org::structure::KermetaModelElement", is_abstract=True)
structure_Tag = Class(name="structure::Tag")
org_structure_Operation = Class(name="org::structure::Operation")
structure_MultiplicityElement = Class(name="structure::MultiplicityElement")
structure_AbstractOperation = Class(name="structure::AbstractOperation")
structure_Parameter = Class(name="structure::Parameter")
structure_Constraint = Class(name="structure::Constraint")
structure_UnresolvedOperation = Class(name="structure::UnresolvedOperation")
structure_ClassDefinition = Class(name="structure::ClassDefinition")
structure_TypeVariable = Class(name="structure::TypeVariable")
structure_UnresolvedProperty = Class(name="structure::UnresolvedProperty")
org_structure_Property = Class(name="org::structure::Property")
structure_AbstractProperty = Class(name="structure::AbstractProperty")
org_structure_Type = Class(name="org::structure::Type", is_abstract=True)
org_structure_TypeContainer = Class(name="org::structure::TypeContainer", is_abstract=True)
org_structure_EnumerationLiteral = Class(name="org::structure::EnumerationLiteral")
NamedElement = Class(name="NamedElement")
structure_Enumeration = Class(name="structure::Enumeration")
org_structure_TypeVariableBinding = Class(name="org::structure::TypeVariableBinding")
org_structure_MultiplicityElement = Class(name="org::structure::MultiplicityElement", is_abstract=True)
TypedElement = Class(name="TypedElement")
org_structure_TypeDefinition = Class(name="org::structure::TypeDefinition")
structure_NamedElement = Class(name="structure::NamedElement")
org_structure_Class = Class(name="org::structure::Class")
ParameterizedType = Class(name="ParameterizedType")
structure_Class = Class(name="structure::Class")
org_structure_DataType = Class(name="org::structure::DataType", is_abstract=True)
structure_ModelElementTypeDefinition = Class(name="structure::ModelElementTypeDefinition")
org_structure_Enumeration = Class(name="org::structure::Enumeration")
DataType = Class(name="DataType")
org_structure_NamedElement = Class(name="org::structure::NamedElement", is_abstract=True)
org_structure_Package = Class(name="org::structure::Package")
structure_ModelElementTypeDefinitionContainer = Class(name="structure::ModelElementTypeDefinitionContainer")
structure_Package = Class(name="structure::Package")
structure_AdaptationOperator = Class(name="structure::AdaptationOperator")
org_structure_Parameter = Class(name="org::structure::Parameter")
org_structure_PrimitiveType = Class(name="org::structure::PrimitiveType")
org_structure_TypedElement = Class(name="org::structure::TypedElement", is_abstract=True)
org_structure_Tag = Class(name="org::structure::Tag")
org_structure_AbstractProperty = Class(name="org::structure::AbstractProperty", is_abstract=True)
org_structure_Constraint = Class(name="org::structure::Constraint")
org_structure_ClassDefinition = Class(name="org::structure::ClassDefinition")
GenericTypeDefinition = Class(name="GenericTypeDefinition")
org_structure_Metamodel = Class(name="org::structure::Metamodel")
structure_ModelTypeDefinitionContainer = Class(name="structure::ModelTypeDefinitionContainer")
structure_FilteredMetamodelReference = Class(name="structure::FilteredMetamodelReference")
org_structure_ModelElementTypeDefinitionContainer = Class(name="org::structure::ModelElementTypeDefinitionContainer", is_abstract=True)
org_structure_GenericTypeDefinition = Class(name="org::structure::GenericTypeDefinition", is_abstract=True)
ModelElementTypeDefinition = Class(name="ModelElementTypeDefinition")
org_structure_ParameterizedType = Class(name="org::structure::ParameterizedType", is_abstract=True)
Type = Class(name="Type")
structure_TypeVariableBinding = Class(name="structure::TypeVariableBinding")
structure_GenericTypeDefinition = Class(name="structure::GenericTypeDefinition")
org_structure_TypeVariable = Class(name="org::structure::TypeVariable", is_abstract=True)
org_structure_ObjectTypeVariable = Class(name="org::structure::ObjectTypeVariable")
TypeVariable = Class(name="TypeVariable")
org_structure_ModelTypeVariable = Class(name="org::structure::ModelTypeVariable")
structure_VirtualType = Class(name="structure::VirtualType")
org_structure_UnresolvedReference = Class(name="org::structure::UnresolvedReference", is_abstract=True)
org_structure_VirtualType = Class(name="org::structure::VirtualType")
ObjectTypeVariable = Class(name="ObjectTypeVariable")
structure_ModelTypeVariable = Class(name="structure::ModelTypeVariable")
org_structure_Model = Class(name="org::structure::Model")
org_structure_AbstractOperation = Class(name="org::structure::AbstractOperation", is_abstract=True)
org_structure_UnresolvedType = Class(name="org::structure::UnresolvedType")
org_structure_UnresolvedProperty = Class(name="org::structure::UnresolvedProperty")
org_structure_UnresolvedOperation = Class(name="org::structure::UnresolvedOperation")
org_structure_Using = Class(name="org::structure::Using")
org_structure_ProductType = Class(name="org::structure::ProductType")
org_structure_FunctionType = Class(name="org::structure::FunctionType")
org_structure_VoidType = Class(name="org::structure::VoidType")
org_structure_UnresolvedInferredType = Class(name="org::structure::UnresolvedInferredType")
org_structure_UnresolvedTypeVariable = Class(name="org::structure::UnresolvedTypeVariable")
org_structure_ModelTypeDefinitionBinding = Class(name="org::structure::ModelTypeDefinitionBinding")
structure_ClassDefinitionBinding = Class(name="structure::ClassDefinitionBinding")
structure_UseAdaptationOperator = Class(name="structure::UseAdaptationOperator")
structure_EnumerationBinding = Class(name="structure::EnumerationBinding")
structure_ModelTypeDefinition = Class(name="structure::ModelTypeDefinition")
org_structure_ClassDefinitionBinding = Class(name="org::structure::ClassDefinitionBinding")
structure_PropertyBinding = Class(name="structure::PropertyBinding")
structure_OperationBinding = Class(name="structure::OperationBinding")
org_structure_EnumerationBinding = Class(name="org::structure::EnumerationBinding")
org_structure_PropertyBinding = Class(name="org::structure::PropertyBinding")
org_structure_OperationBinding = Class(name="org::structure::OperationBinding")
org_structure_AdaptationOperator = Class(name="org::structure::AdaptationOperator")
structure_AdaptationParameter = Class(name="structure::AdaptationParameter")
org_structure_UseAdaptationOperator = Class(name="org::structure::UseAdaptationOperator")
org_structure_PropertyAdaptationOperator = Class(name="org::structure::PropertyAdaptationOperator")
AdaptationOperator = Class(name="AdaptationOperator")
org_structure_UnresolvedAdaptationOperator = Class(name="org::structure::UnresolvedAdaptationOperator")
org_structure_AdaptationParameter = Class(name="org::structure::AdaptationParameter")
org_structure_OperationAdaptationOperator = Class(name="org::structure::OperationAdaptationOperator")
org_structure_ModelElementTypeDefinition = Class(name="org::structure::ModelElementTypeDefinition", is_abstract=True)
TypeDefinition = Class(name="TypeDefinition")
org_structure_ModelType = Class(name="org::structure::ModelType")
org_structure_FilteredMetamodelReference = Class(name="org::structure::FilteredMetamodelReference")
structure_Metamodel = Class(name="structure::Metamodel")
org_structure_ModelTypeDefinition = Class(name="org::structure::ModelTypeDefinition")
structure_ModelTypeDefinitionBinding = Class(name="structure::ModelTypeDefinitionBinding")
org_structure_ModelTransformation = Class(name="org::structure::ModelTransformation")
org_structure_UnresolvedModelTypeDefinition = Class(name="org::structure::UnresolvedModelTypeDefinition")
org_structure_UnresolvedModelTransformation = Class(name="org::structure::UnresolvedModelTransformation")
org_structure_ModelTypeDefinitionContainer = Class(name="org::structure::ModelTypeDefinitionContainer", is_abstract=True)

# Expression class attributes and methods

# behavior_CallExpression class attributes and methods

# behavior_Expression class attributes and methods

# org_behavior_Expression class attributes and methods

# structure_KermetaModelElement class attributes and methods

# structure_TypeContainer class attributes and methods

# structure_Type class attributes and methods

# org_behavior_Assignment class attributes and methods
org_behavior_Assignment_isCast: Property = Property(name="isCast", type=StringType)
org_behavior_Assignment.attributes={org_behavior_Assignment_isCast}

# org_behavior_CallExpression class attributes and methods
org_behavior_CallExpression_name: Property = Property(name="name", type=StringType)
org_behavior_CallExpression.attributes={org_behavior_CallExpression_name}

# org_behavior_Block class attributes and methods

# behavior_Rescue class attributes and methods

# org_behavior_CallVariable class attributes and methods
org_behavior_CallVariable_isAtpre: Property = Property(name="isAtpre", type=StringType)
org_behavior_CallVariable.attributes={org_behavior_CallVariable_isAtpre}

# CallExpression class attributes and methods

# org_behavior_CallFeature class attributes and methods
org_behavior_CallFeature_isAtpre: Property = Property(name="isAtpre", type=StringType)
org_behavior_CallFeature.attributes={org_behavior_CallFeature_isAtpre}

# org_behavior_CallSuperOperation class attributes and methods

# CallOperation class attributes and methods

# org_behavior_CallResult class attributes and methods

# CallVariable class attributes and methods

# org_behavior_CallValue class attributes and methods

# org_behavior_Conditional class attributes and methods

# org_behavior_Raise class attributes and methods

# org_behavior_Rescue class attributes and methods
org_behavior_Rescue_exceptionName: Property = Property(name="exceptionName", type=StringType)
org_behavior_Rescue.attributes={org_behavior_Rescue_exceptionName}

# KermetaModelElement class attributes and methods

# behavior_TypeReference class attributes and methods

# org_behavior_TypeReference class attributes and methods

# MultiplicityElement class attributes and methods

# org_behavior_Literal class attributes and methods

# org_behavior_EmptyExpression class attributes and methods

# org_behavior_JavaStaticCall class attributes and methods
org_behavior_JavaStaticCall_jclass: Property = Property(name="jclass", type=StringType)
org_behavior_JavaStaticCall_jmethod: Property = Property(name="jmethod", type=StringType)
org_behavior_JavaStaticCall.attributes={org_behavior_JavaStaticCall_jmethod, org_behavior_JavaStaticCall_jclass}

# org_behavior_LambdaExpression class attributes and methods

# behavior_LambdaParameter class attributes and methods

# org_behavior_LambdaParameter class attributes and methods
org_behavior_LambdaParameter_name: Property = Property(name="name", type=StringType)
org_behavior_LambdaParameter.attributes={org_behavior_LambdaParameter_name}

# org_behavior_IntegerLiteral class attributes and methods
org_behavior_IntegerLiteral_value: Property = Property(name="value", type=StringType)
org_behavior_IntegerLiteral.attributes={org_behavior_IntegerLiteral_value}

# Literal class attributes and methods

# org_behavior_StringLiteral class attributes and methods
org_behavior_StringLiteral_value: Property = Property(name="value", type=StringType)
org_behavior_StringLiteral.attributes={org_behavior_StringLiteral_value}

# org_behavior_BooleanLiteral class attributes and methods
org_behavior_BooleanLiteral_value: Property = Property(name="value", type=StringType)
org_behavior_BooleanLiteral.attributes={org_behavior_BooleanLiteral_value}

# org_behavior_CallTypeLiteral class attributes and methods

# org_behavior_VoidLiteral class attributes and methods

# org_behavior_Loop class attributes and methods

# org_behavior_SelfExpression class attributes and methods

# org_behavior_VariableDecl class attributes and methods
org_behavior_VariableDecl_identifier: Property = Property(name="identifier", type=StringType)
org_behavior_VariableDecl.attributes={org_behavior_VariableDecl_identifier}

# org_behavior_UnresolvedCall class attributes and methods
org_behavior_UnresolvedCall_isAtpre: Property = Property(name="isAtpre", type=StringType)
org_behavior_UnresolvedCall_isCalledWithParenthesis: Property = Property(name="isCalledWithParenthesis", type=StringType)
org_behavior_UnresolvedCall.attributes={org_behavior_UnresolvedCall_isCalledWithParenthesis, org_behavior_UnresolvedCall_isAtpre}

# structure_UnresolvedReference class attributes and methods

# structure_Using class attributes and methods

# org_behavior_CallOperation class attributes and methods

# CallFeature class attributes and methods

# structure_Operation class attributes and methods

# org_behavior_CallProperty class attributes and methods

# structure_Property class attributes and methods

# org_behavior_CallEnumLiteral class attributes and methods

# structure_EnumerationLiteral class attributes and methods

# org_behavior_CallModelTransformation class attributes and methods

# structure_ModelTransformation class attributes and methods

# org_structure_KermetaModelElement class attributes and methods

# structure_Tag class attributes and methods

# org_structure_Operation class attributes and methods
org_structure_Operation_isAbstract: Property = Property(name="isAbstract", type=StringType)
org_structure_Operation_uniqueName: Property = Property(name="uniqueName", type=StringType)
org_structure_Operation.attributes={org_structure_Operation_uniqueName, org_structure_Operation_isAbstract}

# structure_MultiplicityElement class attributes and methods

# structure_AbstractOperation class attributes and methods

# structure_Parameter class attributes and methods

# structure_Constraint class attributes and methods

# structure_UnresolvedOperation class attributes and methods

# structure_ClassDefinition class attributes and methods

# structure_TypeVariable class attributes and methods

# structure_UnresolvedProperty class attributes and methods

# org_structure_Property class attributes and methods
org_structure_Property_isReadOnly: Property = Property(name="isReadOnly", type=StringType)
org_structure_Property_default: Property = Property(name="default", type=StringType)
org_structure_Property_isComposite: Property = Property(name="isComposite", type=StringType)
org_structure_Property_isDerived: Property = Property(name="isDerived", type=StringType)
org_structure_Property_isID: Property = Property(name="isID", type=StringType)
org_structure_Property_isGetterAbstract: Property = Property(name="isGetterAbstract", type=StringType)
org_structure_Property_isSetterAbstract: Property = Property(name="isSetterAbstract", type=StringType)
org_structure_Property.attributes={org_structure_Property_default, org_structure_Property_isSetterAbstract, org_structure_Property_isDerived, org_structure_Property_isID, org_structure_Property_isComposite, org_structure_Property_isReadOnly, org_structure_Property_isGetterAbstract}

# structure_AbstractProperty class attributes and methods

# org_structure_Type class attributes and methods

# org_structure_TypeContainer class attributes and methods

# org_structure_EnumerationLiteral class attributes and methods

# NamedElement class attributes and methods

# structure_Enumeration class attributes and methods

# org_structure_TypeVariableBinding class attributes and methods

# org_structure_MultiplicityElement class attributes and methods
org_structure_MultiplicityElement_isOrdered: Property = Property(name="isOrdered", type=StringType)
org_structure_MultiplicityElement_isUnique: Property = Property(name="isUnique", type=StringType)
org_structure_MultiplicityElement_lower: Property = Property(name="lower", type=StringType)
org_structure_MultiplicityElement_upper: Property = Property(name="upper", type=StringType)
org_structure_MultiplicityElement.attributes={org_structure_MultiplicityElement_isOrdered, org_structure_MultiplicityElement_lower, org_structure_MultiplicityElement_upper, org_structure_MultiplicityElement_isUnique}

# TypedElement class attributes and methods

# org_structure_TypeDefinition class attributes and methods
org_structure_TypeDefinition_isAspect: Property = Property(name="isAspect", type=StringType)
org_structure_TypeDefinition.attributes={org_structure_TypeDefinition_isAspect}

# structure_NamedElement class attributes and methods

# org_structure_Class class attributes and methods
org_structure_Class_isAbstract: Property = Property(name="isAbstract", type=StringType)
org_structure_Class_name: Property = Property(name="name", type=StringType)
org_structure_Class.attributes={org_structure_Class_name, org_structure_Class_isAbstract}

# ParameterizedType class attributes and methods

# structure_Class class attributes and methods

# org_structure_DataType class attributes and methods

# structure_ModelElementTypeDefinition class attributes and methods

# org_structure_Enumeration class attributes and methods

# DataType class attributes and methods

# org_structure_NamedElement class attributes and methods
org_structure_NamedElement_name: Property = Property(name="name", type=StringType)
org_structure_NamedElement.attributes={org_structure_NamedElement_name}

# org_structure_Package class attributes and methods
org_structure_Package_uri: Property = Property(name="uri", type=StringType)
org_structure_Package.attributes={org_structure_Package_uri}

# structure_ModelElementTypeDefinitionContainer class attributes and methods

# structure_Package class attributes and methods

# structure_AdaptationOperator class attributes and methods

# org_structure_Parameter class attributes and methods

# org_structure_PrimitiveType class attributes and methods

# org_structure_TypedElement class attributes and methods

# org_structure_Tag class attributes and methods
org_structure_Tag_name: Property = Property(name="name", type=StringType)
org_structure_Tag_value: Property = Property(name="value", type=StringType)
org_structure_Tag.attributes={org_structure_Tag_name, org_structure_Tag_value}

# org_structure_AbstractProperty class attributes and methods

# org_structure_Constraint class attributes and methods
org_structure_Constraint_stereotype: Property = Property(name="stereotype", type=StringType)
org_structure_Constraint_language: Property = Property(name="language", type=StringType)
org_structure_Constraint.attributes={org_structure_Constraint_language, org_structure_Constraint_stereotype}

# org_structure_ClassDefinition class attributes and methods
org_structure_ClassDefinition_isAbstract: Property = Property(name="isAbstract", type=StringType)
org_structure_ClassDefinition_isSingleton: Property = Property(name="isSingleton", type=StringType)
org_structure_ClassDefinition_isFinal: Property = Property(name="isFinal", type=StringType)
org_structure_ClassDefinition.attributes={org_structure_ClassDefinition_isAbstract, org_structure_ClassDefinition_isSingleton, org_structure_ClassDefinition_isFinal}

# GenericTypeDefinition class attributes and methods

# org_structure_Metamodel class attributes and methods
org_structure_Metamodel_uri: Property = Property(name="uri", type=StringType)
org_structure_Metamodel_isResolved: Property = Property(name="isResolved", type=BooleanType)
org_structure_Metamodel.attributes={org_structure_Metamodel_uri, org_structure_Metamodel_isResolved}

# structure_ModelTypeDefinitionContainer class attributes and methods

# structure_FilteredMetamodelReference class attributes and methods

# org_structure_ModelElementTypeDefinitionContainer class attributes and methods

# org_structure_GenericTypeDefinition class attributes and methods

# ModelElementTypeDefinition class attributes and methods

# org_structure_ParameterizedType class attributes and methods

# Type class attributes and methods

# structure_TypeVariableBinding class attributes and methods

# structure_GenericTypeDefinition class attributes and methods

# org_structure_TypeVariable class attributes and methods

# org_structure_ObjectTypeVariable class attributes and methods

# TypeVariable class attributes and methods

# org_structure_ModelTypeVariable class attributes and methods

# structure_VirtualType class attributes and methods

# org_structure_UnresolvedReference class attributes and methods

# org_structure_VirtualType class attributes and methods

# ObjectTypeVariable class attributes and methods

# structure_ModelTypeVariable class attributes and methods

# org_structure_Model class attributes and methods

# org_structure_AbstractOperation class attributes and methods

# org_structure_UnresolvedType class attributes and methods
org_structure_UnresolvedType_typeIdentifier: Property = Property(name="typeIdentifier", type=StringType)
org_structure_UnresolvedType.attributes={org_structure_UnresolvedType_typeIdentifier}

# org_structure_UnresolvedProperty class attributes and methods
org_structure_UnresolvedProperty_propertyIdentifier: Property = Property(name="propertyIdentifier", type=StringType)
org_structure_UnresolvedProperty.attributes={org_structure_UnresolvedProperty_propertyIdentifier}

# org_structure_UnresolvedOperation class attributes and methods
org_structure_UnresolvedOperation_operationIdentifier: Property = Property(name="operationIdentifier", type=StringType)
org_structure_UnresolvedOperation.attributes={org_structure_UnresolvedOperation_operationIdentifier}

# org_structure_Using class attributes and methods
org_structure_Using_fromQName: Property = Property(name="fromQName", type=StringType)
org_structure_Using_toName: Property = Property(name="toName", type=StringType)
org_structure_Using.attributes={org_structure_Using_toName, org_structure_Using_fromQName}

# org_structure_ProductType class attributes and methods

# org_structure_FunctionType class attributes and methods

# org_structure_VoidType class attributes and methods

# org_structure_UnresolvedInferredType class attributes and methods

# org_structure_UnresolvedTypeVariable class attributes and methods

# org_structure_ModelTypeDefinitionBinding class attributes and methods

# structure_ClassDefinitionBinding class attributes and methods

# structure_UseAdaptationOperator class attributes and methods

# structure_EnumerationBinding class attributes and methods

# structure_ModelTypeDefinition class attributes and methods

# org_structure_ClassDefinitionBinding class attributes and methods

# structure_PropertyBinding class attributes and methods

# structure_OperationBinding class attributes and methods

# org_structure_EnumerationBinding class attributes and methods

# org_structure_PropertyBinding class attributes and methods

# org_structure_OperationBinding class attributes and methods

# org_structure_AdaptationOperator class attributes and methods

# structure_AdaptationParameter class attributes and methods

# org_structure_UseAdaptationOperator class attributes and methods

# org_structure_PropertyAdaptationOperator class attributes and methods
org_structure_PropertyAdaptationOperator_getter: Property = Property(name="getter", type=StringType)
org_structure_PropertyAdaptationOperator_setter: Property = Property(name="setter", type=StringType)
org_structure_PropertyAdaptationOperator_adder: Property = Property(name="adder", type=StringType)
org_structure_PropertyAdaptationOperator_remover: Property = Property(name="remover", type=StringType)
org_structure_PropertyAdaptationOperator.attributes={org_structure_PropertyAdaptationOperator_setter, org_structure_PropertyAdaptationOperator_getter, org_structure_PropertyAdaptationOperator_adder, org_structure_PropertyAdaptationOperator_remover}

# AdaptationOperator class attributes and methods

# org_structure_UnresolvedAdaptationOperator class attributes and methods

# org_structure_AdaptationParameter class attributes and methods

# org_structure_OperationAdaptationOperator class attributes and methods
org_structure_OperationAdaptationOperator_body: Property = Property(name="body", type=StringType)
org_structure_OperationAdaptationOperator.attributes={org_structure_OperationAdaptationOperator_body}

# org_structure_ModelElementTypeDefinition class attributes and methods

# TypeDefinition class attributes and methods

# org_structure_ModelType class attributes and methods

# org_structure_FilteredMetamodelReference class attributes and methods

# structure_Metamodel class attributes and methods

# org_structure_ModelTypeDefinition class attributes and methods

# structure_ModelTypeDefinitionBinding class attributes and methods

# org_structure_ModelTransformation class attributes and methods
org_structure_ModelTransformation_isAbstract: Property = Property(name="isAbstract", type=StringType)
org_structure_ModelTransformation.attributes={org_structure_ModelTransformation_isAbstract}

# org_structure_UnresolvedModelTypeDefinition class attributes and methods

# org_structure_UnresolvedModelTransformation class attributes and methods

# org_structure_ModelTypeDefinitionContainer class attributes and methods

# Relationships
target0: BinaryAssociation = BinaryAssociation(
    name="target0",
    ends={
        Property(name="behavior_CallExpression", type=org_behavior_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="org_behavior_Assignment", type=behavior_CallExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value1: BinaryAssociation = BinaryAssociation(
    name="value1",
    ends={
        Property(name="behavior_Expression", type=org_behavior_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="org_behavior_Assignment2", type=behavior_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
staticType3: BinaryAssociation = BinaryAssociation(
    name="staticType3",
    ends={
        Property(name="structure_Type", type=org_behavior_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="org_behavior_Expression", type=structure_Type, multiplicity=Multiplicity(0, 1))
    }
)
parameters4: BinaryAssociation = BinaryAssociation(
    name="parameters4",
    ends={
        Property(name="behavior_Expression5", type=org_behavior_CallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="org_behavior_CallExpression", type=behavior_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
staticTypeVariableBindings6: BinaryAssociation = BinaryAssociation(
    name="staticTypeVariableBindings6",
    ends={
        Property(name="structure_Type8", type=org_behavior_CallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="org_behavior_CallExpression7", type=structure_Type, multiplicity=Multiplicity(0, 9999))
    }
)
statement9: BinaryAssociation = BinaryAssociation(
    name="statement9",
    ends={
        Property(name="behavior_Expression10", type=org_behavior_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="org_behavior_Block", type=behavior_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rescueBlock11: BinaryAssociation = BinaryAssociation(
    name="rescueBlock11",
    ends={
        Property(name="behavior_Rescue", type=org_behavior_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="org_behavior_Block12", type=behavior_Rescue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target13: BinaryAssociation = BinaryAssociation(
    name="target13",
    ends={
        Property(name="behavior_Expression14", type=org_behavior_CallFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="org_behavior_CallFeature", type=behavior_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
superType15: BinaryAssociation = BinaryAssociation(
    name="superType15",
    ends={
        Property(name="structure_Type16", type=org_behavior_CallSuperOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="org_behavior_CallSuperOperation", type=structure_Type, multiplicity=Multiplicity(0, 1))
    }
)
thenBody17: BinaryAssociation = BinaryAssociation(
    name="thenBody17",
    ends={
        Property(name="behavior_Expression18", type=org_behavior_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="org_behavior_Conditional", type=behavior_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseBody19: BinaryAssociation = BinaryAssociation(
    name="elseBody19",
    ends={
        Property(name="behavior_Expression21", type=org_behavior_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="org_behavior_Conditional20", type=behavior_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition22: BinaryAssociation = BinaryAssociation(
    name="condition22",
    ends={
        Property(name="behavior_Expression24", type=org_behavior_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="org_behavior_Conditional23", type=behavior_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression25: BinaryAssociation = BinaryAssociation(
    name="expression25",
    ends={
        Property(name="behavior_Expression26", type=org_behavior_Raise, multiplicity=Multiplicity(1, 1)),
        Property(name="org_behavior_Raise", type=behavior_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body27: BinaryAssociation = BinaryAssociation(
    name="body27",
    ends={
        Property(name="behavior_Expression28", type=org_behavior_Rescue, multiplicity=Multiplicity(1, 1)),
        Property(name="org_behavior_Rescue", type=behavior_Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
exceptionType29: BinaryAssociation = BinaryAssociation(
    name="exceptionType29",
    ends={
        Property(name="behavior_TypeReference", type=org_behavior_Rescue, multiplicity=Multiplicity(1, 1)),
        Property(name="org_behavior_Rescue30", type=behavior_TypeReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters31: BinaryAssociation = BinaryAssociation(
    name="parameters31",
    ends={
        Property(name="behavior_Expression32", type=org_behavior_JavaStaticCall, multiplicity=Multiplicity(1, 1)),
        Property(name="org_behavior_JavaStaticCall", type=behavior_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters33: BinaryAssociation = BinaryAssociation(
    name="parameters33",
    ends={
        Property(name="behavior_LambdaParameter", type=org_behavior_LambdaExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="org_behavior_LambdaExpression", type=behavior_LambdaParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body34: BinaryAssociation = BinaryAssociation(
    name="body34",
    ends={
        Property(name="behavior_Expression36", type=org_behavior_LambdaExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="org_behavior_LambdaExpression35", type=behavior_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type37: BinaryAssociation = BinaryAssociation(
    name="type37",
    ends={
        Property(name="behavior_TypeReference38", type=org_behavior_LambdaParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="org_behavior_LambdaParameter", type=behavior_TypeReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeref39: BinaryAssociation = BinaryAssociation(
    name="typeref39",
    ends={
        Property(name="behavior_TypeReference40", type=org_behavior_CallTypeLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="org_behavior_CallTypeLiteral", type=behavior_TypeReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
targetParent58: BinaryAssociation = BinaryAssociation(
    name="targetParent58",
    ends={
        Property(name="structure_Type60", type=org_behavior_UnresolvedCall, multiplicity=Multiplicity(1, 1)),
        Property(name="org_behavior_UnresolvedCall59", type=structure_Type, multiplicity=Multiplicity(0, 1))
    }
)
initialization41: BinaryAssociation = BinaryAssociation(
    name="initialization41",
    ends={
        Property(name="behavior_Expression42", type=org_behavior_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="org_behavior_Loop", type=behavior_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body43: BinaryAssociation = BinaryAssociation(
    name="body43",
    ends={
        Property(name="behavior_Expression45", type=org_behavior_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="org_behavior_Loop44", type=behavior_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stopCondition46: BinaryAssociation = BinaryAssociation(
    name="stopCondition46",
    ends={
        Property(name="behavior_Expression48", type=org_behavior_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="org_behavior_Loop47", type=behavior_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialization49: BinaryAssociation = BinaryAssociation(
    name="initialization49",
    ends={
        Property(name="behavior_Expression50", type=org_behavior_VariableDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="org_behavior_VariableDecl", type=behavior_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type51: BinaryAssociation = BinaryAssociation(
    name="type51",
    ends={
        Property(name="behavior_TypeReference53", type=org_behavior_VariableDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="org_behavior_VariableDecl52", type=behavior_TypeReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
usings54: BinaryAssociation = BinaryAssociation(
    name="usings54",
    ends={
        Property(name="structure_Using", type=org_behavior_UnresolvedCall, multiplicity=Multiplicity(1, 1)),
        Property(name="org_behavior_UnresolvedCall", type=structure_Using, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target55: BinaryAssociation = BinaryAssociation(
    name="target55",
    ends={
        Property(name="behavior_Expression57", type=org_behavior_UnresolvedCall, multiplicity=Multiplicity(1, 1)),
        Property(name="org_behavior_UnresolvedCall56", type=behavior_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
generics61: BinaryAssociation = BinaryAssociation(
    name="generics61",
    ends={
        Property(name="structure_Type63", type=org_behavior_UnresolvedCall, multiplicity=Multiplicity(1, 1)),
        Property(name="org_behavior_UnresolvedCall62", type=structure_Type, multiplicity=Multiplicity(0, 9999))
    }
)
staticOperation64: BinaryAssociation = BinaryAssociation(
    name="staticOperation64",
    ends={
        Property(name="structure_Operation", type=org_behavior_CallOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="org_behavior_CallOperation", type=structure_Operation, multiplicity=Multiplicity(0, 1))
    }
)
staticProperty65: BinaryAssociation = BinaryAssociation(
    name="staticProperty65",
    ends={
        Property(name="structure_Property", type=org_behavior_CallProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="org_behavior_CallProperty", type=structure_Property, multiplicity=Multiplicity(0, 1))
    }
)
staticEnumLiteral66: BinaryAssociation = BinaryAssociation(
    name="staticEnumLiteral66",
    ends={
        Property(name="structure_EnumerationLiteral", type=org_behavior_CallEnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="org_behavior_CallEnumLiteral", type=structure_EnumerationLiteral, multiplicity=Multiplicity(0, 1))
    }
)
staticTransformation67: BinaryAssociation = BinaryAssociation(
    name="staticTransformation67",
    ends={
        Property(name="structure_ModelTransformation", type=org_behavior_CallModelTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="org_behavior_CallModelTransformation", type=structure_ModelTransformation, multiplicity=Multiplicity(0, 1))
    }
)
kTag68: BinaryAssociation = BinaryAssociation(
    name="kTag68",
    ends={
        Property(name="kermeta", type=org_structure_KermetaModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="language", type=structure_Tag, multiplicity=Multiplicity(0, 9999))
    }
)
kOwnedTags69: BinaryAssociation = BinaryAssociation(
    name="kOwnedTags69",
    ends={
        Property(name="structure_Tag", type=org_structure_KermetaModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_KermetaModelElement", type=structure_Tag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
raisedException70: BinaryAssociation = BinaryAssociation(
    name="raisedException70",
    ends={
        Property(name="structure_Type71", type=org_structure_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_Operation", type=structure_Type, multiplicity=Multiplicity(0, 9999))
    }
)
ownedParameter72: BinaryAssociation = BinaryAssociation(
    name="ownedParameter72",
    ends={
        Property(name="kermeta74", type=org_structure_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="language73", type=structure_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pre75: BinaryAssociation = BinaryAssociation(
    name="pre75",
    ends={
        Property(name="kermeta77", type=org_structure_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="language76", type=structure_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
post78: BinaryAssociation = BinaryAssociation(
    name="post78",
    ends={
        Property(name="kermeta80", type=org_structure_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="language79", type=structure_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body81: BinaryAssociation = BinaryAssociation(
    name="body81",
    ends={
        Property(name="behavior_Expression83", type=org_structure_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_Operation82", type=behavior_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedUnresolvedOperations84: BinaryAssociation = BinaryAssociation(
    name="ownedUnresolvedOperations84",
    ends={
        Property(name="structure_UnresolvedOperation", type=org_structure_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_Operation85", type=structure_UnresolvedOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningClass86: BinaryAssociation = BinaryAssociation(
    name="owningClass86",
    ends={
        Property(name="kermeta88", type=org_structure_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="language87", type=structure_ClassDefinition, multiplicity=Multiplicity(0, 1))
    }
)
typeParameter89: BinaryAssociation = BinaryAssociation(
    name="typeParameter89",
    ends={
        Property(name="structure_TypeVariable", type=org_structure_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_Operation90", type=structure_TypeVariable, multiplicity=Multiplicity(0, 9999))
    }
)
opposite91: BinaryAssociation = BinaryAssociation(
    name="opposite91",
    ends={
        Property(name="structure_AbstractProperty", type=org_structure_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_Property", type=structure_AbstractProperty, multiplicity=Multiplicity(0, 1))
    }
)
getterBody92: BinaryAssociation = BinaryAssociation(
    name="getterBody92",
    ends={
        Property(name="behavior_Expression94", type=org_structure_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_Property93", type=behavior_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
setterBody95: BinaryAssociation = BinaryAssociation(
    name="setterBody95",
    ends={
        Property(name="behavior_Expression97", type=org_structure_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_Property96", type=behavior_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedUnresolvedProperties98: BinaryAssociation = BinaryAssociation(
    name="ownedUnresolvedProperties98",
    ends={
        Property(name="structure_UnresolvedProperty", type=org_structure_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_Property99", type=structure_UnresolvedProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningClass100: BinaryAssociation = BinaryAssociation(
    name="owningClass100",
    ends={
        Property(name="kermeta102", type=org_structure_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="language101", type=structure_ClassDefinition, multiplicity=Multiplicity(0, 1))
    }
)
typeContainer103: BinaryAssociation = BinaryAssociation(
    name="typeContainer103",
    ends={
        Property(name="kermeta105", type=org_structure_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="language104", type=structure_TypeContainer, multiplicity=Multiplicity(0, 1))
    }
)
containedType106: BinaryAssociation = BinaryAssociation(
    name="containedType106",
    ends={
        Property(name="kermeta108", type=org_structure_TypeContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="language107", type=structure_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumeration109: BinaryAssociation = BinaryAssociation(
    name="enumeration109",
    ends={
        Property(name="kermeta111", type=org_structure_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="language110", type=structure_Enumeration, multiplicity=Multiplicity(0, 1))
    }
)
variable112: BinaryAssociation = BinaryAssociation(
    name="variable112",
    ends={
        Property(name="structure_TypeVariable113", type=org_structure_TypeVariableBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_TypeVariableBinding", type=structure_TypeVariable, multiplicity=Multiplicity(1, 1))
    }
)
type114: BinaryAssociation = BinaryAssociation(
    name="type114",
    ends={
        Property(name="structure_Type116", type=org_structure_TypeVariableBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_TypeVariableBinding115", type=structure_Type, multiplicity=Multiplicity(1, 1))
    }
)
superType117: BinaryAssociation = BinaryAssociation(
    name="superType117",
    ends={
        Property(name="structure_Type118", type=org_structure_TypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_TypeDefinition", type=structure_Type, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAttribute119: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute119",
    ends={
        Property(name="structure_Property120", type=org_structure_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_Class", type=structure_Property, multiplicity=Multiplicity(0, 9999))
    }
)
ownedOperation121: BinaryAssociation = BinaryAssociation(
    name="ownedOperation121",
    ends={
        Property(name="structure_Operation123", type=org_structure_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_Class122", type=structure_Operation, multiplicity=Multiplicity(0, 9999))
    }
)
superClass124: BinaryAssociation = BinaryAssociation(
    name="superClass124",
    ends={
        Property(name="structure_Class", type=org_structure_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_Class125", type=structure_Class, multiplicity=Multiplicity(0, 9999))
    }
)
ownedLiteral126: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral126",
    ends={
        Property(name="kermeta128", type=org_structure_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="language127", type=structure_EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedPackage129: BinaryAssociation = BinaryAssociation(
    name="nestedPackage129",
    ends={
        Property(name="kermeta131", type=org_structure_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="language130", type=structure_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestingPackage132: BinaryAssociation = BinaryAssociation(
    name="nestingPackage132",
    ends={
        Property(name="kermeta134", type=org_structure_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="language133", type=structure_Package, multiplicity=Multiplicity(0, 1))
    }
)
ownedAdaptationOperators135: BinaryAssociation = BinaryAssociation(
    name="ownedAdaptationOperators135",
    ends={
        Property(name="structure_AdaptationOperator", type=org_structure_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_Package", type=structure_AdaptationOperator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operation136: BinaryAssociation = BinaryAssociation(
    name="operation136",
    ends={
        Property(name="kermeta138", type=org_structure_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="language137", type=structure_Operation, multiplicity=Multiplicity(0, 1))
    }
)
instanceType139: BinaryAssociation = BinaryAssociation(
    name="instanceType139",
    ends={
        Property(name="structure_Type140", type=org_structure_PrimitiveType, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_PrimitiveType", type=structure_Type, multiplicity=Multiplicity(0, 1))
    }
)
type141: BinaryAssociation = BinaryAssociation(
    name="type141",
    ends={
        Property(name="structure_Type142", type=org_structure_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_TypedElement", type=structure_Type, multiplicity=Multiplicity(0, 1))
    }
)
object143: BinaryAssociation = BinaryAssociation(
    name="object143",
    ends={
        Property(name="kermeta145", type=org_structure_Tag, multiplicity=Multiplicity(1, 1)),
        Property(name="language144", type=structure_KermetaModelElement, multiplicity=Multiplicity(1, 9999))
    }
)
ownedOperation163: BinaryAssociation = BinaryAssociation(
    name="ownedOperation163",
    ends={
        Property(name="kermeta165", type=org_structure_ClassDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="language164", type=structure_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body146: BinaryAssociation = BinaryAssociation(
    name="body146",
    ends={
        Property(name="behavior_Expression147", type=org_structure_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_Constraint", type=behavior_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
invOwner148: BinaryAssociation = BinaryAssociation(
    name="invOwner148",
    ends={
        Property(name="kermeta150", type=org_structure_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="language149", type=structure_ClassDefinition, multiplicity=Multiplicity(0, 1))
    }
)
preOwner151: BinaryAssociation = BinaryAssociation(
    name="preOwner151",
    ends={
        Property(name="kermeta153", type=org_structure_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="language152", type=structure_Operation, multiplicity=Multiplicity(0, 1))
    }
)
postOwner154: BinaryAssociation = BinaryAssociation(
    name="postOwner154",
    ends={
        Property(name="kermeta156", type=org_structure_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="language155", type=structure_Operation, multiplicity=Multiplicity(0, 1))
    }
)
inv157: BinaryAssociation = BinaryAssociation(
    name="inv157",
    ends={
        Property(name="kermeta159", type=org_structure_ClassDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="language158", type=structure_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute160: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute160",
    ends={
        Property(name="kermeta162", type=org_structure_ClassDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="language161", type=structure_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packages166: BinaryAssociation = BinaryAssociation(
    name="packages166",
    ends={
        Property(name="structure_Package", type=org_structure_Metamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_Metamodel", type=structure_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referencedMetamodels167: BinaryAssociation = BinaryAssociation(
    name="referencedMetamodels167",
    ends={
        Property(name="structure_FilteredMetamodelReference", type=org_structure_Metamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_Metamodel168", type=structure_FilteredMetamodelReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTypeDefinition169: BinaryAssociation = BinaryAssociation(
    name="ownedTypeDefinition169",
    ends={
        Property(name="structure_ModelElementTypeDefinition", type=org_structure_ModelElementTypeDefinitionContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ModelElementTypeDefinitionContainer", type=structure_ModelElementTypeDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameter170: BinaryAssociation = BinaryAssociation(
    name="typeParameter170",
    ends={
        Property(name="structure_TypeVariable171", type=org_structure_GenericTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_GenericTypeDefinition", type=structure_TypeVariable, multiplicity=Multiplicity(0, 9999))
    }
)
virtualTypeBinding172: BinaryAssociation = BinaryAssociation(
    name="virtualTypeBinding172",
    ends={
        Property(name="structure_TypeVariableBinding", type=org_structure_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ParameterizedType", type=structure_TypeVariableBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParamBinding173: BinaryAssociation = BinaryAssociation(
    name="typeParamBinding173",
    ends={
        Property(name="structure_TypeVariableBinding175", type=org_structure_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ParameterizedType174", type=structure_TypeVariableBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeDefinition176: BinaryAssociation = BinaryAssociation(
    name="typeDefinition176",
    ends={
        Property(name="structure_GenericTypeDefinition", type=org_structure_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ParameterizedType177", type=structure_GenericTypeDefinition, multiplicity=Multiplicity(1, 1))
    }
)
supertype178: BinaryAssociation = BinaryAssociation(
    name="supertype178",
    ends={
        Property(name="structure_Type179", type=org_structure_TypeVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_TypeVariable", type=structure_Type, multiplicity=Multiplicity(0, 1))
    }
)
virtualType180: BinaryAssociation = BinaryAssociation(
    name="virtualType180",
    ends={
        Property(name="kermeta182", type=org_structure_ModelTypeVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="language181", type=structure_VirtualType, multiplicity=Multiplicity(0, 9999))
    }
)
typeDefinition183: BinaryAssociation = BinaryAssociation(
    name="typeDefinition183",
    ends={
        Property(name="structure_ModelElementTypeDefinition184", type=org_structure_VirtualType, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_VirtualType", type=structure_ModelElementTypeDefinition, multiplicity=Multiplicity(1, 1))
    }
)
modelTypeVariable185: BinaryAssociation = BinaryAssociation(
    name="modelTypeVariable185",
    ends={
        Property(name="kermeta187", type=org_structure_VirtualType, multiplicity=Multiplicity(1, 1)),
        Property(name="language186", type=structure_ModelTypeVariable, multiplicity=Multiplicity(1, 1))
    }
)
typeParamBinding188: BinaryAssociation = BinaryAssociation(
    name="typeParamBinding188",
    ends={
        Property(name="structure_TypeVariableBinding190", type=org_structure_VirtualType, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_VirtualType189", type=structure_TypeVariableBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contents191: BinaryAssociation = BinaryAssociation(
    name="contents191",
    ends={
        Property(name="structure_KermetaModelElement", type=org_structure_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_Model", type=structure_KermetaModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
usings192: BinaryAssociation = BinaryAssociation(
    name="usings192",
    ends={
        Property(name="structure_Using193", type=org_structure_UnresolvedType, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_UnresolvedType", type=structure_Using, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generics194: BinaryAssociation = BinaryAssociation(
    name="generics194",
    ends={
        Property(name="structure_Type196", type=org_structure_UnresolvedType, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_UnresolvedType195", type=structure_Type, multiplicity=Multiplicity(0, 9999))
    }
)
type197: BinaryAssociation = BinaryAssociation(
    name="type197",
    ends={
        Property(name="structure_Type198", type=org_structure_ProductType, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ProductType", type=structure_Type, multiplicity=Multiplicity(0, 9999))
    }
)
left199: BinaryAssociation = BinaryAssociation(
    name="left199",
    ends={
        Property(name="structure_Type200", type=org_structure_FunctionType, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_FunctionType", type=structure_Type, multiplicity=Multiplicity(0, 1))
    }
)
right201: BinaryAssociation = BinaryAssociation(
    name="right201",
    ends={
        Property(name="structure_Type203", type=org_structure_FunctionType, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_FunctionType202", type=structure_Type, multiplicity=Multiplicity(0, 1))
    }
)
ownedClassDefinitionBindings204: BinaryAssociation = BinaryAssociation(
    name="ownedClassDefinitionBindings204",
    ends={
        Property(name="structure_ClassDefinitionBinding", type=org_structure_ModelTypeDefinitionBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ModelTypeDefinitionBinding", type=structure_ClassDefinitionBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usedAdaptationOperators205: BinaryAssociation = BinaryAssociation(
    name="usedAdaptationOperators205",
    ends={
        Property(name="structure_UseAdaptationOperator", type=org_structure_ModelTypeDefinitionBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ModelTypeDefinitionBinding206", type=structure_UseAdaptationOperator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEnumerationBindings207: BinaryAssociation = BinaryAssociation(
    name="ownedEnumerationBindings207",
    ends={
        Property(name="structure_EnumerationBinding", type=org_structure_ModelTypeDefinitionBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ModelTypeDefinitionBinding208", type=structure_EnumerationBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
boundModelTypeDefinition209: BinaryAssociation = BinaryAssociation(
    name="boundModelTypeDefinition209",
    ends={
        Property(name="structure_ModelTypeDefinition", type=org_structure_ModelTypeDefinitionBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ModelTypeDefinitionBinding210", type=structure_ModelTypeDefinition, multiplicity=Multiplicity(1, 1))
    }
)
targetedTransformations211: BinaryAssociation = BinaryAssociation(
    name="targetedTransformations211",
    ends={
        Property(name="structure_ModelTransformation213", type=org_structure_ModelTypeDefinitionBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ModelTypeDefinitionBinding212", type=structure_ModelTransformation, multiplicity=Multiplicity(0, 9999))
    }
)
ownedPropertyBindings214: BinaryAssociation = BinaryAssociation(
    name="ownedPropertyBindings214",
    ends={
        Property(name="structure_PropertyBinding", type=org_structure_ClassDefinitionBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ClassDefinitionBinding", type=structure_PropertyBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperationBindings215: BinaryAssociation = BinaryAssociation(
    name="ownedOperationBindings215",
    ends={
        Property(name="structure_OperationBinding", type=org_structure_ClassDefinitionBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ClassDefinitionBinding216", type=structure_OperationBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source217: BinaryAssociation = BinaryAssociation(
    name="source217",
    ends={
        Property(name="structure_ClassDefinition", type=org_structure_ClassDefinitionBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ClassDefinitionBinding218", type=structure_ClassDefinition, multiplicity=Multiplicity(1, 1))
    }
)
target219: BinaryAssociation = BinaryAssociation(
    name="target219",
    ends={
        Property(name="structure_ClassDefinition221", type=org_structure_ClassDefinitionBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ClassDefinitionBinding220", type=structure_ClassDefinition, multiplicity=Multiplicity(1, 1))
    }
)
source222: BinaryAssociation = BinaryAssociation(
    name="source222",
    ends={
        Property(name="structure_Enumeration", type=org_structure_EnumerationBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_EnumerationBinding", type=structure_Enumeration, multiplicity=Multiplicity(1, 1))
    }
)
target223: BinaryAssociation = BinaryAssociation(
    name="target223",
    ends={
        Property(name="structure_Enumeration225", type=org_structure_EnumerationBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_EnumerationBinding224", type=structure_Enumeration, multiplicity=Multiplicity(1, 1))
    }
)
source226: BinaryAssociation = BinaryAssociation(
    name="source226",
    ends={
        Property(name="structure_Property227", type=org_structure_PropertyBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_PropertyBinding", type=structure_Property, multiplicity=Multiplicity(1, 1))
    }
)
target228: BinaryAssociation = BinaryAssociation(
    name="target228",
    ends={
        Property(name="structure_Property230", type=org_structure_PropertyBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_PropertyBinding229", type=structure_Property, multiplicity=Multiplicity(1, 1))
    }
)
source231: BinaryAssociation = BinaryAssociation(
    name="source231",
    ends={
        Property(name="structure_Operation232", type=org_structure_OperationBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_OperationBinding", type=structure_Operation, multiplicity=Multiplicity(1, 1))
    }
)
target233: BinaryAssociation = BinaryAssociation(
    name="target233",
    ends={
        Property(name="structure_Operation235", type=org_structure_OperationBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_OperationBinding234", type=structure_Operation, multiplicity=Multiplicity(1, 1))
    }
)
parameters236: BinaryAssociation = BinaryAssociation(
    name="parameters236",
    ends={
        Property(name="structure_AdaptationParameter", type=org_structure_AdaptationOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_AdaptationOperator", type=structure_AdaptationParameter, multiplicity=Multiplicity(0, 9999))
    }
)
parameters237: BinaryAssociation = BinaryAssociation(
    name="parameters237",
    ends={
        Property(name="structure_KermetaModelElement238", type=org_structure_UseAdaptationOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_UseAdaptationOperator", type=structure_KermetaModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedUnresolved239: BinaryAssociation = BinaryAssociation(
    name="ownedUnresolved239",
    ends={
        Property(name="structure_UnresolvedReference", type=org_structure_UseAdaptationOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_UseAdaptationOperator240", type=structure_UnresolvedReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usedOperator241: BinaryAssociation = BinaryAssociation(
    name="usedOperator241",
    ends={
        Property(name="structure_AdaptationOperator243", type=org_structure_UseAdaptationOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_UseAdaptationOperator242", type=structure_AdaptationOperator, multiplicity=Multiplicity(1, 1))
    }
)
target244: BinaryAssociation = BinaryAssociation(
    name="target244",
    ends={
        Property(name="structure_Property245", type=org_structure_PropertyAdaptationOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_PropertyAdaptationOperator", type=structure_Property, multiplicity=Multiplicity(1, 1))
    }
)
target246: BinaryAssociation = BinaryAssociation(
    name="target246",
    ends={
        Property(name="structure_Operation247", type=org_structure_OperationAdaptationOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_OperationAdaptationOperator", type=structure_Operation, multiplicity=Multiplicity(1, 1))
    }
)
typeDefinition248: BinaryAssociation = BinaryAssociation(
    name="typeDefinition248",
    ends={
        Property(name="structure_ModelTypeDefinition249", type=org_structure_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ModelType", type=structure_ModelTypeDefinition, multiplicity=Multiplicity(1, 1))
    }
)
metamodel250: BinaryAssociation = BinaryAssociation(
    name="metamodel250",
    ends={
        Property(name="structure_Metamodel", type=org_structure_FilteredMetamodelReference, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_FilteredMetamodelReference", type=structure_Metamodel, multiplicity=Multiplicity(1, 1))
    }
)
metamodel251: BinaryAssociation = BinaryAssociation(
    name="metamodel251",
    ends={
        Property(name="structure_Metamodel252", type=org_structure_ModelTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ModelTypeDefinition", type=structure_Metamodel, multiplicity=Multiplicity(1, 1))
    }
)
ownedBindings253: BinaryAssociation = BinaryAssociation(
    name="ownedBindings253",
    ends={
        Property(name="structure_ModelTypeDefinitionBinding", type=org_structure_ModelTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ModelTypeDefinition254", type=structure_ModelTypeDefinitionBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTransformations255: BinaryAssociation = BinaryAssociation(
    name="ownedTransformations255",
    ends={
        Property(name="kermeta257", type=org_structure_ModelTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="language256", type=structure_ModelTransformation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeDefinitions258: BinaryAssociation = BinaryAssociation(
    name="typeDefinitions258",
    ends={
        Property(name="structure_ModelElementTypeDefinition260", type=org_structure_ModelTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ModelTypeDefinition259", type=structure_ModelElementTypeDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
typeParameters261: BinaryAssociation = BinaryAssociation(
    name="typeParameters261",
    ends={
        Property(name="structure_ModelTypeVariable", type=org_structure_ModelTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ModelTransformation", type=structure_ModelTypeVariable, multiplicity=Multiplicity(0, 9999))
    }
)
body262: BinaryAssociation = BinaryAssociation(
    name="body262",
    ends={
        Property(name="behavior_Expression264", type=org_structure_ModelTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ModelTransformation263", type=behavior_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rules265: BinaryAssociation = BinaryAssociation(
    name="rules265",
    ends={
        Property(name="structure_Operation267", type=org_structure_ModelTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ModelTransformation266", type=structure_Operation, multiplicity=Multiplicity(0, 9999))
    }
)
owningModelTypeDefinition268: BinaryAssociation = BinaryAssociation(
    name="owningModelTypeDefinition268",
    ends={
        Property(name="kermeta270", type=org_structure_ModelTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="language269", type=structure_ModelTypeDefinition, multiplicity=Multiplicity(0, 1))
    }
)
ownedParameter271: BinaryAssociation = BinaryAssociation(
    name="ownedParameter271",
    ends={
        Property(name="structure_Parameter", type=org_structure_ModelTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ModelTransformation272", type=structure_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedModelTypeDefinitions273: BinaryAssociation = BinaryAssociation(
    name="ownedModelTypeDefinitions273",
    ends={
        Property(name="structure_ModelTypeDefinition274", type=org_structure_ModelTypeDefinitionContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ModelTypeDefinitionContainer", type=structure_ModelTypeDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_org_behavior_Assignment_Expression = Generalization(general=Expression, specific=org_behavior_Assignment)
gen_org_behavior_Expression_structure_KermetaModelElement = Generalization(general=structure_KermetaModelElement, specific=org_behavior_Expression)
gen_org_behavior_Expression_structure_TypeContainer = Generalization(general=structure_TypeContainer, specific=org_behavior_Expression)
gen_org_behavior_CallExpression_Expression = Generalization(general=Expression, specific=org_behavior_CallExpression)
gen_org_behavior_Block_Expression = Generalization(general=Expression, specific=org_behavior_Block)
gen_org_behavior_CallVariable_CallExpression = Generalization(general=CallExpression, specific=org_behavior_CallVariable)
gen_org_behavior_CallFeature_CallExpression = Generalization(general=CallExpression, specific=org_behavior_CallFeature)
gen_org_behavior_CallSuperOperation_CallOperation = Generalization(general=CallOperation, specific=org_behavior_CallSuperOperation)
gen_org_behavior_CallResult_CallVariable = Generalization(general=CallVariable, specific=org_behavior_CallResult)
gen_org_behavior_CallValue_CallExpression = Generalization(general=CallExpression, specific=org_behavior_CallValue)
gen_org_behavior_Conditional_Expression = Generalization(general=Expression, specific=org_behavior_Conditional)
gen_org_behavior_Raise_Expression = Generalization(general=Expression, specific=org_behavior_Raise)
gen_org_behavior_Rescue_KermetaModelElement = Generalization(general=KermetaModelElement, specific=org_behavior_Rescue)
gen_org_behavior_TypeReference_MultiplicityElement = Generalization(general=MultiplicityElement, specific=org_behavior_TypeReference)
gen_org_behavior_Literal_Expression = Generalization(general=Expression, specific=org_behavior_Literal)
gen_org_behavior_EmptyExpression_Expression = Generalization(general=Expression, specific=org_behavior_EmptyExpression)
gen_org_behavior_JavaStaticCall_Expression = Generalization(general=Expression, specific=org_behavior_JavaStaticCall)
gen_org_behavior_LambdaExpression_Expression = Generalization(general=Expression, specific=org_behavior_LambdaExpression)
gen_org_behavior_LambdaParameter_KermetaModelElement = Generalization(general=KermetaModelElement, specific=org_behavior_LambdaParameter)
gen_org_behavior_IntegerLiteral_Literal = Generalization(general=Literal, specific=org_behavior_IntegerLiteral)
gen_org_behavior_StringLiteral_Literal = Generalization(general=Literal, specific=org_behavior_StringLiteral)
gen_org_behavior_BooleanLiteral_Literal = Generalization(general=Literal, specific=org_behavior_BooleanLiteral)
gen_org_behavior_CallTypeLiteral_Literal = Generalization(general=Literal, specific=org_behavior_CallTypeLiteral)
gen_org_behavior_VoidLiteral_Literal = Generalization(general=Literal, specific=org_behavior_VoidLiteral)
gen_org_behavior_Loop_Expression = Generalization(general=Expression, specific=org_behavior_Loop)
gen_org_behavior_SelfExpression_Expression = Generalization(general=Expression, specific=org_behavior_SelfExpression)
gen_org_behavior_VariableDecl_Expression = Generalization(general=Expression, specific=org_behavior_VariableDecl)
gen_org_behavior_UnresolvedCall_structure_UnresolvedReference = Generalization(general=structure_UnresolvedReference, specific=org_behavior_UnresolvedCall)
gen_org_behavior_UnresolvedCall_behavior_CallExpression = Generalization(general=behavior_CallExpression, specific=org_behavior_UnresolvedCall)
gen_org_behavior_UnresolvedCall_structure_TypeContainer = Generalization(general=structure_TypeContainer, specific=org_behavior_UnresolvedCall)
gen_org_behavior_CallOperation_CallFeature = Generalization(general=CallFeature, specific=org_behavior_CallOperation)
gen_org_behavior_CallProperty_CallFeature = Generalization(general=CallFeature, specific=org_behavior_CallProperty)
gen_org_behavior_CallEnumLiteral_CallExpression = Generalization(general=CallExpression, specific=org_behavior_CallEnumLiteral)
gen_org_behavior_CallModelTransformation_CallFeature = Generalization(general=CallFeature, specific=org_behavior_CallModelTransformation)
gen_org_structure_Operation_structure_MultiplicityElement = Generalization(general=structure_MultiplicityElement, specific=org_structure_Operation)
gen_org_structure_Operation_structure_AbstractOperation = Generalization(general=structure_AbstractOperation, specific=org_structure_Operation)
gen_org_structure_Property_structure_MultiplicityElement = Generalization(general=structure_MultiplicityElement, specific=org_structure_Property)
gen_org_structure_Property_structure_AbstractProperty = Generalization(general=structure_AbstractProperty, specific=org_structure_Property)
gen_org_structure_Type_KermetaModelElement = Generalization(general=KermetaModelElement, specific=org_structure_Type)
gen_org_structure_TypeContainer_KermetaModelElement = Generalization(general=KermetaModelElement, specific=org_structure_TypeContainer)
gen_org_structure_EnumerationLiteral_NamedElement = Generalization(general=NamedElement, specific=org_structure_EnumerationLiteral)
gen_org_structure_TypeVariableBinding_structure_TypeContainer = Generalization(general=structure_TypeContainer, specific=org_structure_TypeVariableBinding)
gen_org_structure_TypeVariableBinding_structure_KermetaModelElement = Generalization(general=structure_KermetaModelElement, specific=org_structure_TypeVariableBinding)
gen_org_structure_MultiplicityElement_TypedElement = Generalization(general=TypedElement, specific=org_structure_MultiplicityElement)
gen_org_structure_TypeDefinition_structure_NamedElement = Generalization(general=structure_NamedElement, specific=org_structure_TypeDefinition)
gen_org_structure_TypeDefinition_structure_TypeContainer = Generalization(general=structure_TypeContainer, specific=org_structure_TypeDefinition)
gen_org_structure_Class_ParameterizedType = Generalization(general=ParameterizedType, specific=org_structure_Class)
gen_org_structure_DataType_structure_Type = Generalization(general=structure_Type, specific=org_structure_DataType)
gen_org_structure_DataType_structure_ModelElementTypeDefinition = Generalization(general=structure_ModelElementTypeDefinition, specific=org_structure_DataType)
gen_org_structure_Enumeration_DataType = Generalization(general=DataType, specific=org_structure_Enumeration)
gen_org_structure_NamedElement_KermetaModelElement = Generalization(general=KermetaModelElement, specific=org_structure_NamedElement)
gen_org_structure_Package_structure_NamedElement = Generalization(general=structure_NamedElement, specific=org_structure_Package)
gen_org_structure_Package_structure_ModelElementTypeDefinitionContainer = Generalization(general=structure_ModelElementTypeDefinitionContainer, specific=org_structure_Package)
gen_org_structure_Parameter_MultiplicityElement = Generalization(general=MultiplicityElement, specific=org_structure_Parameter)
gen_org_structure_PrimitiveType_DataType = Generalization(general=DataType, specific=org_structure_PrimitiveType)
gen_org_structure_TypedElement_structure_TypeContainer = Generalization(general=structure_TypeContainer, specific=org_structure_TypedElement)
gen_org_structure_TypedElement_structure_NamedElement = Generalization(general=structure_NamedElement, specific=org_structure_TypedElement)
gen_org_structure_Tag_KermetaModelElement = Generalization(general=KermetaModelElement, specific=org_structure_Tag)
gen_org_structure_AbstractProperty_KermetaModelElement = Generalization(general=KermetaModelElement, specific=org_structure_AbstractProperty)
gen_org_structure_Constraint_NamedElement = Generalization(general=NamedElement, specific=org_structure_Constraint)
gen_org_structure_ClassDefinition_GenericTypeDefinition = Generalization(general=GenericTypeDefinition, specific=org_structure_ClassDefinition)
gen_org_structure_Metamodel_structure_KermetaModelElement = Generalization(general=structure_KermetaModelElement, specific=org_structure_Metamodel)
gen_org_structure_Metamodel_structure_NamedElement = Generalization(general=structure_NamedElement, specific=org_structure_Metamodel)
gen_org_structure_Metamodel_structure_ModelTypeDefinitionContainer = Generalization(general=structure_ModelTypeDefinitionContainer, specific=org_structure_Metamodel)
gen_org_structure_ModelElementTypeDefinitionContainer_NamedElement = Generalization(general=NamedElement, specific=org_structure_ModelElementTypeDefinitionContainer)
gen_org_structure_GenericTypeDefinition_ModelElementTypeDefinition = Generalization(general=ModelElementTypeDefinition, specific=org_structure_GenericTypeDefinition)
gen_org_structure_ParameterizedType_Type = Generalization(general=Type, specific=org_structure_ParameterizedType)
gen_org_structure_TypeVariable_structure_TypeContainer = Generalization(general=structure_TypeContainer, specific=org_structure_TypeVariable)
gen_org_structure_TypeVariable_structure_Type = Generalization(general=structure_Type, specific=org_structure_TypeVariable)
gen_org_structure_TypeVariable_structure_NamedElement = Generalization(general=structure_NamedElement, specific=org_structure_TypeVariable)
gen_org_structure_ObjectTypeVariable_TypeVariable = Generalization(general=TypeVariable, specific=org_structure_ObjectTypeVariable)
gen_org_structure_ModelTypeVariable_TypeVariable = Generalization(general=TypeVariable, specific=org_structure_ModelTypeVariable)
gen_org_structure_VirtualType_ObjectTypeVariable = Generalization(general=ObjectTypeVariable, specific=org_structure_VirtualType)
gen_org_structure_Model_KermetaModelElement = Generalization(general=KermetaModelElement, specific=org_structure_Model)
gen_org_structure_AbstractOperation_KermetaModelElement = Generalization(general=KermetaModelElement, specific=org_structure_AbstractOperation)
gen_org_structure_UnresolvedType_structure_Type = Generalization(general=structure_Type, specific=org_structure_UnresolvedType)
gen_org_structure_UnresolvedType_structure_UnresolvedReference = Generalization(general=structure_UnresolvedReference, specific=org_structure_UnresolvedType)
gen_org_structure_UnresolvedType_structure_TypeContainer = Generalization(general=structure_TypeContainer, specific=org_structure_UnresolvedType)
gen_org_structure_UnresolvedReference_KermetaModelElement = Generalization(general=KermetaModelElement, specific=org_structure_UnresolvedReference)
gen_org_structure_UnresolvedProperty_structure_AbstractProperty = Generalization(general=structure_AbstractProperty, specific=org_structure_UnresolvedProperty)
gen_org_structure_UnresolvedProperty_structure_UnresolvedReference = Generalization(general=structure_UnresolvedReference, specific=org_structure_UnresolvedProperty)
gen_org_structure_UnresolvedOperation_structure_AbstractOperation = Generalization(general=structure_AbstractOperation, specific=org_structure_UnresolvedOperation)
gen_org_structure_UnresolvedOperation_structure_UnresolvedReference = Generalization(general=structure_UnresolvedReference, specific=org_structure_UnresolvedOperation)
gen_org_structure_UnresolvedOperation_structure_TypeContainer = Generalization(general=structure_TypeContainer, specific=org_structure_UnresolvedOperation)
gen_org_structure_Using_KermetaModelElement = Generalization(general=KermetaModelElement, specific=org_structure_Using)
gen_org_structure_ProductType_structure_TypeContainer = Generalization(general=structure_TypeContainer, specific=org_structure_ProductType)
gen_org_structure_ProductType_structure_Type = Generalization(general=structure_Type, specific=org_structure_ProductType)
gen_org_structure_FunctionType_structure_TypeContainer = Generalization(general=structure_TypeContainer, specific=org_structure_FunctionType)
gen_org_structure_FunctionType_structure_Type = Generalization(general=structure_Type, specific=org_structure_FunctionType)
gen_org_structure_VoidType_Type = Generalization(general=Type, specific=org_structure_VoidType)
gen_org_structure_UnresolvedInferredType_structure_UnresolvedReference = Generalization(general=structure_UnresolvedReference, specific=org_structure_UnresolvedInferredType)
gen_org_structure_UnresolvedInferredType_structure_Type = Generalization(general=structure_Type, specific=org_structure_UnresolvedInferredType)
gen_org_structure_UnresolvedTypeVariable_structure_UnresolvedReference = Generalization(general=structure_UnresolvedReference, specific=org_structure_UnresolvedTypeVariable)
gen_org_structure_UnresolvedTypeVariable_structure_TypeVariable = Generalization(general=structure_TypeVariable, specific=org_structure_UnresolvedTypeVariable)
gen_org_structure_ModelTypeDefinitionBinding_structure_KermetaModelElement = Generalization(general=structure_KermetaModelElement, specific=org_structure_ModelTypeDefinitionBinding)
gen_org_structure_ModelTypeDefinitionBinding_structure_ModelTypeDefinitionContainer = Generalization(general=structure_ModelTypeDefinitionContainer, specific=org_structure_ModelTypeDefinitionBinding)
gen_org_structure_ClassDefinitionBinding_KermetaModelElement = Generalization(general=KermetaModelElement, specific=org_structure_ClassDefinitionBinding)
gen_org_structure_EnumerationBinding_KermetaModelElement = Generalization(general=KermetaModelElement, specific=org_structure_EnumerationBinding)
gen_org_structure_PropertyBinding_KermetaModelElement = Generalization(general=KermetaModelElement, specific=org_structure_PropertyBinding)
gen_org_structure_OperationBinding_KermetaModelElement = Generalization(general=KermetaModelElement, specific=org_structure_OperationBinding)
gen_org_structure_AdaptationOperator_NamedElement = Generalization(general=NamedElement, specific=org_structure_AdaptationOperator)
gen_org_structure_UseAdaptationOperator_KermetaModelElement = Generalization(general=KermetaModelElement, specific=org_structure_UseAdaptationOperator)
gen_org_structure_PropertyAdaptationOperator_AdaptationOperator = Generalization(general=AdaptationOperator, specific=org_structure_PropertyAdaptationOperator)
gen_org_structure_UnresolvedAdaptationOperator_structure_AdaptationOperator = Generalization(general=structure_AdaptationOperator, specific=org_structure_UnresolvedAdaptationOperator)
gen_org_structure_UnresolvedAdaptationOperator_structure_UnresolvedReference = Generalization(general=structure_UnresolvedReference, specific=org_structure_UnresolvedAdaptationOperator)
gen_org_structure_AdaptationParameter_TypedElement = Generalization(general=TypedElement, specific=org_structure_AdaptationParameter)
gen_org_structure_OperationAdaptationOperator_AdaptationOperator = Generalization(general=AdaptationOperator, specific=org_structure_OperationAdaptationOperator)
gen_org_structure_ModelElementTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=org_structure_ModelElementTypeDefinition)
gen_org_structure_ModelType_Type = Generalization(general=Type, specific=org_structure_ModelType)
gen_org_structure_FilteredMetamodelReference_KermetaModelElement = Generalization(general=KermetaModelElement, specific=org_structure_FilteredMetamodelReference)
gen_org_structure_ModelTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=org_structure_ModelTypeDefinition)
gen_org_structure_ModelTransformation_MultiplicityElement = Generalization(general=MultiplicityElement, specific=org_structure_ModelTransformation)
gen_org_structure_UnresolvedModelTypeDefinition_structure_ModelTypeDefinition = Generalization(general=structure_ModelTypeDefinition, specific=org_structure_UnresolvedModelTypeDefinition)
gen_org_structure_UnresolvedModelTypeDefinition_structure_UnresolvedReference = Generalization(general=structure_UnresolvedReference, specific=org_structure_UnresolvedModelTypeDefinition)
gen_org_structure_UnresolvedModelTransformation_structure_ModelTransformation = Generalization(general=structure_ModelTransformation, specific=org_structure_UnresolvedModelTransformation)
gen_org_structure_UnresolvedModelTransformation_structure_UnresolvedReference = Generalization(general=structure_UnresolvedReference, specific=org_structure_UnresolvedModelTransformation)
gen_org_structure_ModelTypeDefinitionContainer_KermetaModelElement = Generalization(general=KermetaModelElement, specific=org_structure_ModelTypeDefinitionContainer)

# Domain Model
domain_model = DomainModel(
    name="org",
    types={Expression, behavior_CallExpression, behavior_Expression, org_behavior_Expression, structure_KermetaModelElement, structure_TypeContainer, structure_Type, org_behavior_Assignment, org_behavior_CallExpression, org_behavior_Block, behavior_Rescue, org_behavior_CallVariable, CallExpression, org_behavior_CallFeature, org_behavior_CallSuperOperation, CallOperation, org_behavior_CallResult, CallVariable, org_behavior_CallValue, org_behavior_Conditional, org_behavior_Raise, org_behavior_Rescue, KermetaModelElement, behavior_TypeReference, org_behavior_TypeReference, MultiplicityElement, org_behavior_Literal, org_behavior_EmptyExpression, org_behavior_JavaStaticCall, org_behavior_LambdaExpression, behavior_LambdaParameter, org_behavior_LambdaParameter, org_behavior_IntegerLiteral, Literal, org_behavior_StringLiteral, org_behavior_BooleanLiteral, org_behavior_CallTypeLiteral, org_behavior_VoidLiteral, org_behavior_Loop, org_behavior_SelfExpression, org_behavior_VariableDecl, org_behavior_UnresolvedCall, structure_UnresolvedReference, structure_Using, org_behavior_CallOperation, CallFeature, structure_Operation, org_behavior_CallProperty, structure_Property, org_behavior_CallEnumLiteral, structure_EnumerationLiteral, org_behavior_CallModelTransformation, structure_ModelTransformation, org_structure_KermetaModelElement, structure_Tag, org_structure_Operation, structure_MultiplicityElement, structure_AbstractOperation, structure_Parameter, structure_Constraint, structure_UnresolvedOperation, structure_ClassDefinition, structure_TypeVariable, structure_UnresolvedProperty, org_structure_Property, structure_AbstractProperty, org_structure_Type, org_structure_TypeContainer, org_structure_EnumerationLiteral, NamedElement, structure_Enumeration, org_structure_TypeVariableBinding, org_structure_MultiplicityElement, TypedElement, org_structure_TypeDefinition, structure_NamedElement, org_structure_Class, ParameterizedType, structure_Class, org_structure_DataType, structure_ModelElementTypeDefinition, org_structure_Enumeration, DataType, org_structure_NamedElement, org_structure_Package, structure_ModelElementTypeDefinitionContainer, structure_Package, structure_AdaptationOperator, org_structure_Parameter, org_structure_PrimitiveType, org_structure_TypedElement, org_structure_Tag, org_structure_AbstractProperty, org_structure_Constraint, org_structure_ClassDefinition, GenericTypeDefinition, org_structure_Metamodel, structure_ModelTypeDefinitionContainer, structure_FilteredMetamodelReference, org_structure_ModelElementTypeDefinitionContainer, org_structure_GenericTypeDefinition, ModelElementTypeDefinition, org_structure_ParameterizedType, Type, structure_TypeVariableBinding, structure_GenericTypeDefinition, org_structure_TypeVariable, org_structure_ObjectTypeVariable, TypeVariable, org_structure_ModelTypeVariable, structure_VirtualType, org_structure_UnresolvedReference, org_structure_VirtualType, ObjectTypeVariable, structure_ModelTypeVariable, org_structure_Model, org_structure_AbstractOperation, org_structure_UnresolvedType, org_structure_UnresolvedProperty, org_structure_UnresolvedOperation, org_structure_Using, org_structure_ProductType, org_structure_FunctionType, org_structure_VoidType, org_structure_UnresolvedInferredType, org_structure_UnresolvedTypeVariable, org_structure_ModelTypeDefinitionBinding, structure_ClassDefinitionBinding, structure_UseAdaptationOperator, structure_EnumerationBinding, structure_ModelTypeDefinition, org_structure_ClassDefinitionBinding, structure_PropertyBinding, structure_OperationBinding, org_structure_EnumerationBinding, org_structure_PropertyBinding, org_structure_OperationBinding, org_structure_AdaptationOperator, structure_AdaptationParameter, org_structure_UseAdaptationOperator, org_structure_PropertyAdaptationOperator, AdaptationOperator, org_structure_UnresolvedAdaptationOperator, org_structure_AdaptationParameter, org_structure_OperationAdaptationOperator, org_structure_ModelElementTypeDefinition, TypeDefinition, org_structure_ModelType, org_structure_FilteredMetamodelReference, structure_Metamodel, org_structure_ModelTypeDefinition, structure_ModelTypeDefinitionBinding, org_structure_ModelTransformation, org_structure_UnresolvedModelTypeDefinition, org_structure_UnresolvedModelTransformation, org_structure_ModelTypeDefinitionContainer, ConstraintLanguage, ConstraintType},
    associations={target0, value1, staticType3, parameters4, staticTypeVariableBindings6, statement9, rescueBlock11, target13, superType15, thenBody17, elseBody19, condition22, expression25, body27, exceptionType29, parameters31, parameters33, body34, type37, typeref39, targetParent58, initialization41, body43, stopCondition46, initialization49, type51, usings54, target55, generics61, staticOperation64, staticProperty65, staticEnumLiteral66, staticTransformation67, kTag68, kOwnedTags69, raisedException70, ownedParameter72, pre75, post78, body81, ownedUnresolvedOperations84, owningClass86, typeParameter89, opposite91, getterBody92, setterBody95, ownedUnresolvedProperties98, owningClass100, typeContainer103, containedType106, enumeration109, variable112, type114, superType117, ownedAttribute119, ownedOperation121, superClass124, ownedLiteral126, nestedPackage129, nestingPackage132, ownedAdaptationOperators135, operation136, instanceType139, type141, object143, ownedOperation163, body146, invOwner148, preOwner151, postOwner154, inv157, ownedAttribute160, packages166, referencedMetamodels167, ownedTypeDefinition169, typeParameter170, virtualTypeBinding172, typeParamBinding173, typeDefinition176, supertype178, virtualType180, typeDefinition183, modelTypeVariable185, typeParamBinding188, contents191, usings192, generics194, type197, left199, right201, ownedClassDefinitionBindings204, usedAdaptationOperators205, ownedEnumerationBindings207, boundModelTypeDefinition209, targetedTransformations211, ownedPropertyBindings214, ownedOperationBindings215, source217, target219, source222, target223, source226, target228, source231, target233, parameters236, parameters237, ownedUnresolved239, usedOperator241, target244, target246, typeDefinition248, metamodel250, metamodel251, ownedBindings253, ownedTransformations255, typeDefinitions258, typeParameters261, body262, rules265, owningModelTypeDefinition268, ownedParameter271, ownedModelTypeDefinitions273},
    generalizations={gen_org_behavior_Assignment_Expression, gen_org_behavior_Expression_structure_KermetaModelElement, gen_org_behavior_Expression_structure_TypeContainer, gen_org_behavior_CallExpression_Expression, gen_org_behavior_Block_Expression, gen_org_behavior_CallVariable_CallExpression, gen_org_behavior_CallFeature_CallExpression, gen_org_behavior_CallSuperOperation_CallOperation, gen_org_behavior_CallResult_CallVariable, gen_org_behavior_CallValue_CallExpression, gen_org_behavior_Conditional_Expression, gen_org_behavior_Raise_Expression, gen_org_behavior_Rescue_KermetaModelElement, gen_org_behavior_TypeReference_MultiplicityElement, gen_org_behavior_Literal_Expression, gen_org_behavior_EmptyExpression_Expression, gen_org_behavior_JavaStaticCall_Expression, gen_org_behavior_LambdaExpression_Expression, gen_org_behavior_LambdaParameter_KermetaModelElement, gen_org_behavior_IntegerLiteral_Literal, gen_org_behavior_StringLiteral_Literal, gen_org_behavior_BooleanLiteral_Literal, gen_org_behavior_CallTypeLiteral_Literal, gen_org_behavior_VoidLiteral_Literal, gen_org_behavior_Loop_Expression, gen_org_behavior_SelfExpression_Expression, gen_org_behavior_VariableDecl_Expression, gen_org_behavior_UnresolvedCall_structure_UnresolvedReference, gen_org_behavior_UnresolvedCall_behavior_CallExpression, gen_org_behavior_UnresolvedCall_structure_TypeContainer, gen_org_behavior_CallOperation_CallFeature, gen_org_behavior_CallProperty_CallFeature, gen_org_behavior_CallEnumLiteral_CallExpression, gen_org_behavior_CallModelTransformation_CallFeature, gen_org_structure_Operation_structure_MultiplicityElement, gen_org_structure_Operation_structure_AbstractOperation, gen_org_structure_Property_structure_MultiplicityElement, gen_org_structure_Property_structure_AbstractProperty, gen_org_structure_Type_KermetaModelElement, gen_org_structure_TypeContainer_KermetaModelElement, gen_org_structure_EnumerationLiteral_NamedElement, gen_org_structure_TypeVariableBinding_structure_TypeContainer, gen_org_structure_TypeVariableBinding_structure_KermetaModelElement, gen_org_structure_MultiplicityElement_TypedElement, gen_org_structure_TypeDefinition_structure_NamedElement, gen_org_structure_TypeDefinition_structure_TypeContainer, gen_org_structure_Class_ParameterizedType, gen_org_structure_DataType_structure_Type, gen_org_structure_DataType_structure_ModelElementTypeDefinition, gen_org_structure_Enumeration_DataType, gen_org_structure_NamedElement_KermetaModelElement, gen_org_structure_Package_structure_NamedElement, gen_org_structure_Package_structure_ModelElementTypeDefinitionContainer, gen_org_structure_Parameter_MultiplicityElement, gen_org_structure_PrimitiveType_DataType, gen_org_structure_TypedElement_structure_TypeContainer, gen_org_structure_TypedElement_structure_NamedElement, gen_org_structure_Tag_KermetaModelElement, gen_org_structure_AbstractProperty_KermetaModelElement, gen_org_structure_Constraint_NamedElement, gen_org_structure_ClassDefinition_GenericTypeDefinition, gen_org_structure_Metamodel_structure_KermetaModelElement, gen_org_structure_Metamodel_structure_NamedElement, gen_org_structure_Metamodel_structure_ModelTypeDefinitionContainer, gen_org_structure_ModelElementTypeDefinitionContainer_NamedElement, gen_org_structure_GenericTypeDefinition_ModelElementTypeDefinition, gen_org_structure_ParameterizedType_Type, gen_org_structure_TypeVariable_structure_TypeContainer, gen_org_structure_TypeVariable_structure_Type, gen_org_structure_TypeVariable_structure_NamedElement, gen_org_structure_ObjectTypeVariable_TypeVariable, gen_org_structure_ModelTypeVariable_TypeVariable, gen_org_structure_VirtualType_ObjectTypeVariable, gen_org_structure_Model_KermetaModelElement, gen_org_structure_AbstractOperation_KermetaModelElement, gen_org_structure_UnresolvedType_structure_Type, gen_org_structure_UnresolvedType_structure_UnresolvedReference, gen_org_structure_UnresolvedType_structure_TypeContainer, gen_org_structure_UnresolvedReference_KermetaModelElement, gen_org_structure_UnresolvedProperty_structure_AbstractProperty, gen_org_structure_UnresolvedProperty_structure_UnresolvedReference, gen_org_structure_UnresolvedOperation_structure_AbstractOperation, gen_org_structure_UnresolvedOperation_structure_UnresolvedReference, gen_org_structure_UnresolvedOperation_structure_TypeContainer, gen_org_structure_Using_KermetaModelElement, gen_org_structure_ProductType_structure_TypeContainer, gen_org_structure_ProductType_structure_Type, gen_org_structure_FunctionType_structure_TypeContainer, gen_org_structure_FunctionType_structure_Type, gen_org_structure_VoidType_Type, gen_org_structure_UnresolvedInferredType_structure_UnresolvedReference, gen_org_structure_UnresolvedInferredType_structure_Type, gen_org_structure_UnresolvedTypeVariable_structure_UnresolvedReference, gen_org_structure_UnresolvedTypeVariable_structure_TypeVariable, gen_org_structure_ModelTypeDefinitionBinding_structure_KermetaModelElement, gen_org_structure_ModelTypeDefinitionBinding_structure_ModelTypeDefinitionContainer, gen_org_structure_ClassDefinitionBinding_KermetaModelElement, gen_org_structure_EnumerationBinding_KermetaModelElement, gen_org_structure_PropertyBinding_KermetaModelElement, gen_org_structure_OperationBinding_KermetaModelElement, gen_org_structure_AdaptationOperator_NamedElement, gen_org_structure_UseAdaptationOperator_KermetaModelElement, gen_org_structure_PropertyAdaptationOperator_AdaptationOperator, gen_org_structure_UnresolvedAdaptationOperator_structure_AdaptationOperator, gen_org_structure_UnresolvedAdaptationOperator_structure_UnresolvedReference, gen_org_structure_AdaptationParameter_TypedElement, gen_org_structure_OperationAdaptationOperator_AdaptationOperator, gen_org_structure_ModelElementTypeDefinition_TypeDefinition, gen_org_structure_ModelType_Type, gen_org_structure_FilteredMetamodelReference_KermetaModelElement, gen_org_structure_ModelTypeDefinition_TypeDefinition, gen_org_structure_ModelTransformation_MultiplicityElement, gen_org_structure_UnresolvedModelTypeDefinition_structure_ModelTypeDefinition, gen_org_structure_UnresolvedModelTypeDefinition_structure_UnresolvedReference, gen_org_structure_UnresolvedModelTransformation_structure_ModelTransformation, gen_org_structure_UnresolvedModelTransformation_structure_UnresolvedReference, gen_org_structure_ModelTypeDefinitionContainer_KermetaModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)