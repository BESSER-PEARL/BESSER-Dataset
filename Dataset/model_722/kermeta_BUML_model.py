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
org_behavior_Assignment = Class(name="org_behavior_Assignment")
Expression = Class(name="Expression")
behavior_Rescue = Class(name="behavior_Rescue")
org_behavior_CallVariable = Class(name="org_behavior_CallVariable")
CallExpression = Class(name="CallExpression")
behavior_CallExpression = Class(name="behavior_CallExpression")
behavior_Expression = Class(name="behavior_Expression")
org_behavior_Expression = Class(name="org_behavior_Expression", is_abstract=True)
structure_KermetaModelElement = Class(name="structure_KermetaModelElement")
structure_TypeContainer = Class(name="structure_TypeContainer")
structure_Type = Class(name="structure_Type")
org_behavior_CallExpression = Class(name="org_behavior_CallExpression", is_abstract=True)
org_behavior_Block = Class(name="org_behavior_Block")
org_behavior_Rescue = Class(name="org_behavior_Rescue")
KermetaModelElement = Class(name="KermetaModelElement")
behavior_TypeReference = Class(name="behavior_TypeReference")
org_behavior_CallFeature = Class(name="org_behavior_CallFeature", is_abstract=True)
org_behavior_CallSuperOperation = Class(name="org_behavior_CallSuperOperation")
CallOperation = Class(name="CallOperation")
org_behavior_CallResult = Class(name="org_behavior_CallResult")
CallVariable = Class(name="CallVariable")
org_behavior_CallValue = Class(name="org_behavior_CallValue")
org_behavior_Conditional = Class(name="org_behavior_Conditional")
org_behavior_Raise = Class(name="org_behavior_Raise")
org_behavior_StringLiteral = Class(name="org_behavior_StringLiteral")
org_behavior_BooleanLiteral = Class(name="org_behavior_BooleanLiteral")
org_behavior_CallTypeLiteral = Class(name="org_behavior_CallTypeLiteral")
org_behavior_TypeReference = Class(name="org_behavior_TypeReference")
MultiplicityElement = Class(name="MultiplicityElement")
org_behavior_Literal = Class(name="org_behavior_Literal", is_abstract=True)
org_behavior_EmptyExpression = Class(name="org_behavior_EmptyExpression")
org_behavior_JavaStaticCall = Class(name="org_behavior_JavaStaticCall")
org_behavior_LambdaExpression = Class(name="org_behavior_LambdaExpression")
behavior_LambdaParameter = Class(name="behavior_LambdaParameter")
org_behavior_LambdaParameter = Class(name="org_behavior_LambdaParameter")
org_behavior_IntegerLiteral = Class(name="org_behavior_IntegerLiteral")
Literal = Class(name="Literal")
org_behavior_VoidLiteral = Class(name="org_behavior_VoidLiteral")
org_behavior_Loop = Class(name="org_behavior_Loop")
org_behavior_SelfExpression = Class(name="org_behavior_SelfExpression")
org_behavior_VariableDecl = Class(name="org_behavior_VariableDecl")
org_behavior_UnresolvedCall = Class(name="org_behavior_UnresolvedCall")
structure_UnresolvedReference = Class(name="structure_UnresolvedReference")
structure_Using = Class(name="structure_Using")
structure_UnresolvedOperation = Class(name="structure_UnresolvedOperation")
org_behavior_CallOperation = Class(name="org_behavior_CallOperation")
CallFeature = Class(name="CallFeature")
structure_Operation = Class(name="structure_Operation")
org_behavior_CallProperty = Class(name="org_behavior_CallProperty")
structure_Property = Class(name="structure_Property")
org_behavior_CallEnumLiteral = Class(name="org_behavior_CallEnumLiteral")
structure_EnumerationLiteral = Class(name="structure_EnumerationLiteral")
org_behavior_CallModelTransformation = Class(name="org_behavior_CallModelTransformation")
structure_ModelTransformation = Class(name="structure_ModelTransformation")
org_structure_KermetaModelElement = Class(name="org_structure_KermetaModelElement", is_abstract=True)
structure_Tag = Class(name="structure_Tag")
org_structure_Operation = Class(name="org_structure_Operation")
structure_MultiplicityElement = Class(name="structure_MultiplicityElement")
structure_AbstractOperation = Class(name="structure_AbstractOperation")
structure_Parameter = Class(name="structure_Parameter")
structure_Constraint = Class(name="structure_Constraint")
org_structure_Type = Class(name="org_structure_Type", is_abstract=True)
structure_ClassDefinition = Class(name="structure_ClassDefinition")
structure_TypeVariable = Class(name="structure_TypeVariable")
org_structure_Property = Class(name="org_structure_Property")
structure_AbstractProperty = Class(name="structure_AbstractProperty")
structure_UnresolvedProperty = Class(name="structure_UnresolvedProperty")
org_structure_Class = Class(name="org_structure_Class")
ParameterizedType = Class(name="ParameterizedType")
org_structure_TypeContainer = Class(name="org_structure_TypeContainer", is_abstract=True)
org_structure_EnumerationLiteral = Class(name="org_structure_EnumerationLiteral")
NamedElement = Class(name="NamedElement")
structure_Enumeration = Class(name="structure_Enumeration")
org_structure_TypeVariableBinding = Class(name="org_structure_TypeVariableBinding")
org_structure_MultiplicityElement = Class(name="org_structure_MultiplicityElement", is_abstract=True)
TypedElement = Class(name="TypedElement")
org_structure_TypeDefinition = Class(name="org_structure_TypeDefinition")
structure_NamedElement = Class(name="structure_NamedElement")
structure_AdaptationOperator = Class(name="structure_AdaptationOperator")
structure_Class = Class(name="structure_Class")
org_structure_DataType = Class(name="org_structure_DataType", is_abstract=True)
structure_ModelElementTypeDefinition = Class(name="structure_ModelElementTypeDefinition")
org_structure_Enumeration = Class(name="org_structure_Enumeration")
DataType = Class(name="DataType")
org_structure_NamedElement = Class(name="org_structure_NamedElement", is_abstract=True)
org_structure_Package = Class(name="org_structure_Package")
structure_ModelElementTypeDefinitionContainer = Class(name="structure_ModelElementTypeDefinitionContainer")
structure_Package = Class(name="structure_Package")
org_structure_Parameter = Class(name="org_structure_Parameter")
org_structure_PrimitiveType = Class(name="org_structure_PrimitiveType")
org_structure_TypedElement = Class(name="org_structure_TypedElement", is_abstract=True)
org_structure_Tag = Class(name="org_structure_Tag")
org_structure_AbstractProperty = Class(name="org_structure_AbstractProperty", is_abstract=True)
org_structure_Constraint = Class(name="org_structure_Constraint")
org_structure_GenericTypeDefinition = Class(name="org_structure_GenericTypeDefinition", is_abstract=True)
ModelElementTypeDefinition = Class(name="ModelElementTypeDefinition")
org_structure_ClassDefinition = Class(name="org_structure_ClassDefinition")
GenericTypeDefinition = Class(name="GenericTypeDefinition")
org_structure_Metamodel = Class(name="org_structure_Metamodel")
structure_ModelTypeDefinitionContainer = Class(name="structure_ModelTypeDefinitionContainer")
structure_FilteredMetamodelReference = Class(name="structure_FilteredMetamodelReference")
org_structure_ModelElementTypeDefinitionContainer = Class(name="org_structure_ModelElementTypeDefinitionContainer", is_abstract=True)
org_structure_Model = Class(name="org_structure_Model")
org_structure_AbstractOperation = Class(name="org_structure_AbstractOperation", is_abstract=True)
org_structure_UnresolvedType = Class(name="org_structure_UnresolvedType")
org_structure_ParameterizedType = Class(name="org_structure_ParameterizedType", is_abstract=True)
Type = Class(name="Type")
structure_TypeVariableBinding = Class(name="structure_TypeVariableBinding")
structure_GenericTypeDefinition = Class(name="structure_GenericTypeDefinition")
org_structure_TypeVariable = Class(name="org_structure_TypeVariable", is_abstract=True)
org_structure_ObjectTypeVariable = Class(name="org_structure_ObjectTypeVariable")
TypeVariable = Class(name="TypeVariable")
org_structure_ModelTypeVariable = Class(name="org_structure_ModelTypeVariable")
structure_VirtualType = Class(name="structure_VirtualType")
org_structure_VirtualType = Class(name="org_structure_VirtualType")
ObjectTypeVariable = Class(name="ObjectTypeVariable")
structure_ModelTypeVariable = Class(name="structure_ModelTypeVariable")
org_structure_VoidType = Class(name="org_structure_VoidType")
org_structure_UnresolvedInferredType = Class(name="org_structure_UnresolvedInferredType")
org_structure_UnresolvedTypeVariable = Class(name="org_structure_UnresolvedTypeVariable")
org_structure_UnresolvedReference = Class(name="org_structure_UnresolvedReference", is_abstract=True)
org_structure_UnresolvedProperty = Class(name="org_structure_UnresolvedProperty")
org_structure_UnresolvedOperation = Class(name="org_structure_UnresolvedOperation")
org_structure_Using = Class(name="org_structure_Using")
org_structure_ProductType = Class(name="org_structure_ProductType")
org_structure_FunctionType = Class(name="org_structure_FunctionType")
org_structure_PropertyAdaptationOperator = Class(name="org_structure_PropertyAdaptationOperator")
AdaptationOperator = Class(name="AdaptationOperator")
org_structure_ModelTypeDefinitionBinding = Class(name="org_structure_ModelTypeDefinitionBinding")
structure_ClassDefinitionBinding = Class(name="structure_ClassDefinitionBinding")
structure_UseAdaptationOperator = Class(name="structure_UseAdaptationOperator")
structure_EnumerationBinding = Class(name="structure_EnumerationBinding")
structure_ModelTypeDefinition = Class(name="structure_ModelTypeDefinition")
org_structure_ClassDefinitionBinding = Class(name="org_structure_ClassDefinitionBinding")
structure_PropertyBinding = Class(name="structure_PropertyBinding")
structure_OperationBinding = Class(name="structure_OperationBinding")
org_structure_EnumerationBinding = Class(name="org_structure_EnumerationBinding")
org_structure_PropertyBinding = Class(name="org_structure_PropertyBinding")
org_structure_OperationBinding = Class(name="org_structure_OperationBinding")
org_structure_AdaptationOperator = Class(name="org_structure_AdaptationOperator")
structure_AdaptationParameter = Class(name="structure_AdaptationParameter")
org_structure_UseAdaptationOperator = Class(name="org_structure_UseAdaptationOperator")
org_structure_UnresolvedModelTypeDefinition = Class(name="org_structure_UnresolvedModelTypeDefinition")
org_structure_UnresolvedModelTransformation = Class(name="org_structure_UnresolvedModelTransformation")
org_structure_ModelTypeDefinitionContainer = Class(name="org_structure_ModelTypeDefinitionContainer", is_abstract=True)
org_structure_UnresolvedAdaptationOperator = Class(name="org_structure_UnresolvedAdaptationOperator")
org_structure_AdaptationParameter = Class(name="org_structure_AdaptationParameter")
org_structure_OperationAdaptationOperator = Class(name="org_structure_OperationAdaptationOperator")
org_structure_ModelElementTypeDefinition = Class(name="org_structure_ModelElementTypeDefinition", is_abstract=True)
TypeDefinition = Class(name="TypeDefinition")
org_structure_ModelType = Class(name="org_structure_ModelType")
org_structure_FilteredMetamodelReference = Class(name="org_structure_FilteredMetamodelReference")
structure_Metamodel = Class(name="structure_Metamodel")
org_structure_ModelTypeDefinition = Class(name="org_structure_ModelTypeDefinition")
structure_ModelTypeDefinitionBinding = Class(name="structure_ModelTypeDefinitionBinding")
org_structure_ModelTransformation = Class(name="org_structure_ModelTransformation")

# org_behavior_Assignment class attributes and methods
org_behavior_Assignment_isCast: Property = Property(name="isCast", type=StringType)
org_behavior_Assignment.attributes={org_behavior_Assignment_isCast}

# Expression class attributes and methods

# behavior_Rescue class attributes and methods

# org_behavior_CallVariable class attributes and methods
org_behavior_CallVariable_isAtpre: Property = Property(name="isAtpre", type=StringType)
org_behavior_CallVariable.attributes={org_behavior_CallVariable_isAtpre}

# CallExpression class attributes and methods

# behavior_CallExpression class attributes and methods

# behavior_Expression class attributes and methods

# org_behavior_Expression class attributes and methods

# structure_KermetaModelElement class attributes and methods

# structure_TypeContainer class attributes and methods

# structure_Type class attributes and methods

# org_behavior_CallExpression class attributes and methods
org_behavior_CallExpression_name: Property = Property(name="name", type=StringType)
org_behavior_CallExpression.attributes={org_behavior_CallExpression_name}

# org_behavior_Block class attributes and methods

# org_behavior_Rescue class attributes and methods
org_behavior_Rescue_exceptionName: Property = Property(name="exceptionName", type=StringType)
org_behavior_Rescue.attributes={org_behavior_Rescue_exceptionName}

# KermetaModelElement class attributes and methods

# behavior_TypeReference class attributes and methods

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

# org_behavior_StringLiteral class attributes and methods
org_behavior_StringLiteral_value: Property = Property(name="value", type=StringType)
org_behavior_StringLiteral.attributes={org_behavior_StringLiteral_value}

# org_behavior_BooleanLiteral class attributes and methods
org_behavior_BooleanLiteral_value: Property = Property(name="value", type=StringType)
org_behavior_BooleanLiteral.attributes={org_behavior_BooleanLiteral_value}

# org_behavior_CallTypeLiteral class attributes and methods

# org_behavior_TypeReference class attributes and methods

# MultiplicityElement class attributes and methods

# org_behavior_Literal class attributes and methods

# org_behavior_EmptyExpression class attributes and methods

# org_behavior_JavaStaticCall class attributes and methods
org_behavior_JavaStaticCall_jclass: Property = Property(name="jclass", type=StringType)
org_behavior_JavaStaticCall_jmethod: Property = Property(name="jmethod", type=StringType)
org_behavior_JavaStaticCall.attributes={org_behavior_JavaStaticCall_jclass, org_behavior_JavaStaticCall_jmethod}

# org_behavior_LambdaExpression class attributes and methods

# behavior_LambdaParameter class attributes and methods

# org_behavior_LambdaParameter class attributes and methods
org_behavior_LambdaParameter_name: Property = Property(name="name", type=StringType)
org_behavior_LambdaParameter.attributes={org_behavior_LambdaParameter_name}

# org_behavior_IntegerLiteral class attributes and methods
org_behavior_IntegerLiteral_value: Property = Property(name="value", type=StringType)
org_behavior_IntegerLiteral.attributes={org_behavior_IntegerLiteral_value}

# Literal class attributes and methods

# org_behavior_VoidLiteral class attributes and methods

# org_behavior_Loop class attributes and methods

# org_behavior_SelfExpression class attributes and methods

# org_behavior_VariableDecl class attributes and methods
org_behavior_VariableDecl_identifier: Property = Property(name="identifier", type=StringType)
org_behavior_VariableDecl.attributes={org_behavior_VariableDecl_identifier}

# org_behavior_UnresolvedCall class attributes and methods
org_behavior_UnresolvedCall_isAtpre: Property = Property(name="isAtpre", type=StringType)
org_behavior_UnresolvedCall_isCalledWithParenthesis: Property = Property(name="isCalledWithParenthesis", type=StringType)
org_behavior_UnresolvedCall.attributes={org_behavior_UnresolvedCall_isAtpre, org_behavior_UnresolvedCall_isCalledWithParenthesis}

# structure_UnresolvedReference class attributes and methods

# structure_Using class attributes and methods

# structure_UnresolvedOperation class attributes and methods

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

# org_structure_Type class attributes and methods

# structure_ClassDefinition class attributes and methods

# structure_TypeVariable class attributes and methods

# org_structure_Property class attributes and methods
org_structure_Property_isReadOnly: Property = Property(name="isReadOnly", type=StringType)
org_structure_Property_default: Property = Property(name="default", type=StringType)
org_structure_Property_isComposite: Property = Property(name="isComposite", type=StringType)
org_structure_Property_isDerived: Property = Property(name="isDerived", type=StringType)
org_structure_Property_isID: Property = Property(name="isID", type=StringType)
org_structure_Property_isGetterAbstract: Property = Property(name="isGetterAbstract", type=StringType)
org_structure_Property_isSetterAbstract: Property = Property(name="isSetterAbstract", type=StringType)
org_structure_Property.attributes={org_structure_Property_default, org_structure_Property_isReadOnly, org_structure_Property_isGetterAbstract, org_structure_Property_isID, org_structure_Property_isSetterAbstract, org_structure_Property_isDerived, org_structure_Property_isComposite}

# structure_AbstractProperty class attributes and methods

# structure_UnresolvedProperty class attributes and methods

# org_structure_Class class attributes and methods
org_structure_Class_isAbstract: Property = Property(name="isAbstract", type=StringType)
org_structure_Class_name: Property = Property(name="name", type=StringType)
org_structure_Class.attributes={org_structure_Class_name, org_structure_Class_isAbstract}

# ParameterizedType class attributes and methods

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
org_structure_MultiplicityElement.attributes={org_structure_MultiplicityElement_isOrdered, org_structure_MultiplicityElement_upper, org_structure_MultiplicityElement_isUnique, org_structure_MultiplicityElement_lower}

# TypedElement class attributes and methods

# org_structure_TypeDefinition class attributes and methods
org_structure_TypeDefinition_isAspect: Property = Property(name="isAspect", type=StringType)
org_structure_TypeDefinition.attributes={org_structure_TypeDefinition_isAspect}

# structure_NamedElement class attributes and methods

# structure_AdaptationOperator class attributes and methods

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

# org_structure_GenericTypeDefinition class attributes and methods

# ModelElementTypeDefinition class attributes and methods

# org_structure_ClassDefinition class attributes and methods
org_structure_ClassDefinition_isAbstract: Property = Property(name="isAbstract", type=StringType)
org_structure_ClassDefinition_isSingleton: Property = Property(name="isSingleton", type=StringType)
org_structure_ClassDefinition_isFinal: Property = Property(name="isFinal", type=StringType)
org_structure_ClassDefinition.attributes={org_structure_ClassDefinition_isAbstract, org_structure_ClassDefinition_isSingleton, org_structure_ClassDefinition_isFinal}

# GenericTypeDefinition class attributes and methods

# org_structure_Metamodel class attributes and methods
org_structure_Metamodel_uri: Property = Property(name="uri", type=StringType)
org_structure_Metamodel_isResolved: Property = Property(name="isResolved", type=BooleanType)
org_structure_Metamodel.attributes={org_structure_Metamodel_isResolved, org_structure_Metamodel_uri}

# structure_ModelTypeDefinitionContainer class attributes and methods

# structure_FilteredMetamodelReference class attributes and methods

# org_structure_ModelElementTypeDefinitionContainer class attributes and methods

# org_structure_Model class attributes and methods

# org_structure_AbstractOperation class attributes and methods

# org_structure_UnresolvedType class attributes and methods
org_structure_UnresolvedType_typeIdentifier: Property = Property(name="typeIdentifier", type=StringType)
org_structure_UnresolvedType.attributes={org_structure_UnresolvedType_typeIdentifier}

# org_structure_ParameterizedType class attributes and methods

# Type class attributes and methods

# structure_TypeVariableBinding class attributes and methods

# structure_GenericTypeDefinition class attributes and methods

# org_structure_TypeVariable class attributes and methods

# org_structure_ObjectTypeVariable class attributes and methods

# TypeVariable class attributes and methods

# org_structure_ModelTypeVariable class attributes and methods

# structure_VirtualType class attributes and methods

# org_structure_VirtualType class attributes and methods

# ObjectTypeVariable class attributes and methods

# structure_ModelTypeVariable class attributes and methods

# org_structure_VoidType class attributes and methods

# org_structure_UnresolvedInferredType class attributes and methods

# org_structure_UnresolvedTypeVariable class attributes and methods

# org_structure_UnresolvedReference class attributes and methods

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

# org_structure_PropertyAdaptationOperator class attributes and methods
org_structure_PropertyAdaptationOperator_getter: Property = Property(name="getter", type=StringType)
org_structure_PropertyAdaptationOperator_setter: Property = Property(name="setter", type=StringType)
org_structure_PropertyAdaptationOperator_adder: Property = Property(name="adder", type=StringType)
org_structure_PropertyAdaptationOperator_remover: Property = Property(name="remover", type=StringType)
org_structure_PropertyAdaptationOperator.attributes={org_structure_PropertyAdaptationOperator_remover, org_structure_PropertyAdaptationOperator_setter, org_structure_PropertyAdaptationOperator_getter, org_structure_PropertyAdaptationOperator_adder}

# AdaptationOperator class attributes and methods

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

# org_structure_UnresolvedModelTypeDefinition class attributes and methods

# org_structure_UnresolvedModelTransformation class attributes and methods

# org_structure_ModelTypeDefinitionContainer class attributes and methods

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

# Relationships
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
targetParent58: BinaryAssociation = BinaryAssociation(
    name="targetParent58",
    ends={
        Property(name="structure_Type60", type=org_behavior_UnresolvedCall, multiplicity=Multiplicity(1, 1)),
        Property(name="org_behavior_UnresolvedCall59", type=structure_Type, multiplicity=Multiplicity(0, 1))
    }
)
generics61: BinaryAssociation = BinaryAssociation(
    name="generics61",
    ends={
        Property(name="structure_Type63", type=org_behavior_UnresolvedCall, multiplicity=Multiplicity(1, 1)),
        Property(name="org_behavior_UnresolvedCall62", type=structure_Type, multiplicity=Multiplicity(0, 9999))
    }
)
typeref39: BinaryAssociation = BinaryAssociation(
    name="typeref39",
    ends={
        Property(name="behavior_TypeReference40", type=org_behavior_CallTypeLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="org_behavior_CallTypeLiteral", type=behavior_TypeReference, multiplicity=Multiplicity(1, 1), is_composite=True)
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
post74: BinaryAssociation = BinaryAssociation(
    name="post74",
    ends={
        Property(name="Constraint75", type=org_structure_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="postOwner", type=structure_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body76: BinaryAssociation = BinaryAssociation(
    name="body76",
    ends={
        Property(name="behavior_Expression78", type=org_structure_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_Operation77", type=behavior_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedUnresolvedOperations79: BinaryAssociation = BinaryAssociation(
    name="ownedUnresolvedOperations79",
    ends={
        Property(name="structure_UnresolvedOperation", type=org_structure_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_Operation80", type=structure_UnresolvedOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
        Property(name="Tag", type=org_structure_KermetaModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="object", type=structure_Tag, multiplicity=Multiplicity(0, 9999))
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
        Property(name="Parameter", type=org_structure_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation", type=structure_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pre73: BinaryAssociation = BinaryAssociation(
    name="pre73",
    ends={
        Property(name="Constraint", type=org_structure_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="preOwner", type=structure_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeContainer95: BinaryAssociation = BinaryAssociation(
    name="typeContainer95",
    ends={
        Property(name="TypeContainer", type=org_structure_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="containedType", type=structure_TypeContainer, multiplicity=Multiplicity(0, 1))
    }
)
owningClass81: BinaryAssociation = BinaryAssociation(
    name="owningClass81",
    ends={
        Property(name="ClassDefinition", type=org_structure_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedOperation", type=structure_ClassDefinition, multiplicity=Multiplicity(0, 1))
    }
)
typeParameter82: BinaryAssociation = BinaryAssociation(
    name="typeParameter82",
    ends={
        Property(name="structure_TypeVariable", type=org_structure_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_Operation83", type=structure_TypeVariable, multiplicity=Multiplicity(0, 9999))
    }
)
opposite84: BinaryAssociation = BinaryAssociation(
    name="opposite84",
    ends={
        Property(name="structure_AbstractProperty", type=org_structure_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_Property", type=structure_AbstractProperty, multiplicity=Multiplicity(0, 1))
    }
)
getterBody85: BinaryAssociation = BinaryAssociation(
    name="getterBody85",
    ends={
        Property(name="behavior_Expression87", type=org_structure_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_Property86", type=behavior_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
setterBody88: BinaryAssociation = BinaryAssociation(
    name="setterBody88",
    ends={
        Property(name="behavior_Expression90", type=org_structure_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_Property89", type=behavior_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedUnresolvedProperties91: BinaryAssociation = BinaryAssociation(
    name="ownedUnresolvedProperties91",
    ends={
        Property(name="structure_UnresolvedProperty", type=org_structure_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_Property92", type=structure_UnresolvedProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningClass93: BinaryAssociation = BinaryAssociation(
    name="owningClass93",
    ends={
        Property(name="ClassDefinition94", type=org_structure_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedAttribute", type=structure_ClassDefinition, multiplicity=Multiplicity(0, 1))
    }
)
ownedAttribute105: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute105",
    ends={
        Property(name="structure_Property106", type=org_structure_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_Class", type=structure_Property, multiplicity=Multiplicity(0, 9999))
    }
)
ownedOperation107: BinaryAssociation = BinaryAssociation(
    name="ownedOperation107",
    ends={
        Property(name="structure_Operation109", type=org_structure_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_Class108", type=structure_Operation, multiplicity=Multiplicity(0, 9999))
    }
)
containedType96: BinaryAssociation = BinaryAssociation(
    name="containedType96",
    ends={
        Property(name="Type", type=org_structure_TypeContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="typeContainer", type=structure_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumeration97: BinaryAssociation = BinaryAssociation(
    name="enumeration97",
    ends={
        Property(name="Enumeration", type=org_structure_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedLiteral", type=structure_Enumeration, multiplicity=Multiplicity(0, 1))
    }
)
variable98: BinaryAssociation = BinaryAssociation(
    name="variable98",
    ends={
        Property(name="structure_TypeVariable99", type=org_structure_TypeVariableBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_TypeVariableBinding", type=structure_TypeVariable, multiplicity=Multiplicity(1, 1))
    }
)
type100: BinaryAssociation = BinaryAssociation(
    name="type100",
    ends={
        Property(name="structure_Type102", type=org_structure_TypeVariableBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_TypeVariableBinding101", type=structure_Type, multiplicity=Multiplicity(1, 1))
    }
)
superType103: BinaryAssociation = BinaryAssociation(
    name="superType103",
    ends={
        Property(name="structure_Type104", type=org_structure_TypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_TypeDefinition", type=structure_Type, multiplicity=Multiplicity(0, 9999))
    }
)
nestingPackage114: BinaryAssociation = BinaryAssociation(
    name="nestingPackage114",
    ends={
        Property(name="Package115", type=org_structure_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="nestedPackage", type=structure_Package, multiplicity=Multiplicity(0, 1))
    }
)
ownedAdaptationOperators116: BinaryAssociation = BinaryAssociation(
    name="ownedAdaptationOperators116",
    ends={
        Property(name="structure_AdaptationOperator", type=org_structure_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_Package", type=structure_AdaptationOperator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass110: BinaryAssociation = BinaryAssociation(
    name="superClass110",
    ends={
        Property(name="structure_Class", type=org_structure_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_Class111", type=structure_Class, multiplicity=Multiplicity(0, 9999))
    }
)
ownedLiteral112: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral112",
    ends={
        Property(name="EnumerationLiteral", type=org_structure_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="enumeration", type=structure_EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedPackage113: BinaryAssociation = BinaryAssociation(
    name="nestedPackage113",
    ends={
        Property(name="Package", type=org_structure_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="nestingPackage", type=structure_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
preOwner127: BinaryAssociation = BinaryAssociation(
    name="preOwner127",
    ends={
        Property(name="Operation128", type=org_structure_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="pre", type=structure_Operation, multiplicity=Multiplicity(0, 1))
    }
)
postOwner129: BinaryAssociation = BinaryAssociation(
    name="postOwner129",
    ends={
        Property(name="Operation130", type=org_structure_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="post", type=structure_Operation, multiplicity=Multiplicity(0, 1))
    }
)
operation117: BinaryAssociation = BinaryAssociation(
    name="operation117",
    ends={
        Property(name="Operation", type=org_structure_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedParameter", type=structure_Operation, multiplicity=Multiplicity(0, 1))
    }
)
instanceType118: BinaryAssociation = BinaryAssociation(
    name="instanceType118",
    ends={
        Property(name="structure_Type119", type=org_structure_PrimitiveType, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_PrimitiveType", type=structure_Type, multiplicity=Multiplicity(0, 1))
    }
)
type120: BinaryAssociation = BinaryAssociation(
    name="type120",
    ends={
        Property(name="structure_Type121", type=org_structure_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_TypedElement", type=structure_Type, multiplicity=Multiplicity(0, 1))
    }
)
object122: BinaryAssociation = BinaryAssociation(
    name="object122",
    ends={
        Property(name="KermetaModelElement", type=org_structure_Tag, multiplicity=Multiplicity(1, 1)),
        Property(name="kTag", type=structure_KermetaModelElement, multiplicity=Multiplicity(1, 9999))
    }
)
body123: BinaryAssociation = BinaryAssociation(
    name="body123",
    ends={
        Property(name="behavior_Expression124", type=org_structure_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_Constraint", type=behavior_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
invOwner125: BinaryAssociation = BinaryAssociation(
    name="invOwner125",
    ends={
        Property(name="ClassDefinition126", type=org_structure_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="inv", type=structure_ClassDefinition, multiplicity=Multiplicity(0, 1))
    }
)
ownedTypeDefinition140: BinaryAssociation = BinaryAssociation(
    name="ownedTypeDefinition140",
    ends={
        Property(name="structure_ModelElementTypeDefinition", type=org_structure_ModelElementTypeDefinitionContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ModelElementTypeDefinitionContainer", type=structure_ModelElementTypeDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameter141: BinaryAssociation = BinaryAssociation(
    name="typeParameter141",
    ends={
        Property(name="structure_TypeVariable142", type=org_structure_GenericTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_GenericTypeDefinition", type=structure_TypeVariable, multiplicity=Multiplicity(0, 9999))
    }
)
inv131: BinaryAssociation = BinaryAssociation(
    name="inv131",
    ends={
        Property(name="Constraint132", type=org_structure_ClassDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="invOwner", type=structure_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute133: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute133",
    ends={
        Property(name="Property", type=org_structure_ClassDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="owningClass", type=structure_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation134: BinaryAssociation = BinaryAssociation(
    name="ownedOperation134",
    ends={
        Property(name="Operation136", type=org_structure_ClassDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="owningClass135", type=structure_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packages137: BinaryAssociation = BinaryAssociation(
    name="packages137",
    ends={
        Property(name="structure_Package", type=org_structure_Metamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_Metamodel", type=structure_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referencedMetamodels138: BinaryAssociation = BinaryAssociation(
    name="referencedMetamodels138",
    ends={
        Property(name="structure_FilteredMetamodelReference", type=org_structure_Metamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_Metamodel139", type=structure_FilteredMetamodelReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contents158: BinaryAssociation = BinaryAssociation(
    name="contents158",
    ends={
        Property(name="structure_KermetaModelElement", type=org_structure_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_Model", type=structure_KermetaModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
virtualTypeBinding143: BinaryAssociation = BinaryAssociation(
    name="virtualTypeBinding143",
    ends={
        Property(name="structure_TypeVariableBinding", type=org_structure_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ParameterizedType", type=structure_TypeVariableBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParamBinding144: BinaryAssociation = BinaryAssociation(
    name="typeParamBinding144",
    ends={
        Property(name="structure_TypeVariableBinding146", type=org_structure_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ParameterizedType145", type=structure_TypeVariableBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeDefinition147: BinaryAssociation = BinaryAssociation(
    name="typeDefinition147",
    ends={
        Property(name="structure_GenericTypeDefinition", type=org_structure_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ParameterizedType148", type=structure_GenericTypeDefinition, multiplicity=Multiplicity(1, 1))
    }
)
supertype149: BinaryAssociation = BinaryAssociation(
    name="supertype149",
    ends={
        Property(name="structure_Type150", type=org_structure_TypeVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_TypeVariable", type=structure_Type, multiplicity=Multiplicity(0, 1))
    }
)
virtualType151: BinaryAssociation = BinaryAssociation(
    name="virtualType151",
    ends={
        Property(name="VirtualType", type=org_structure_ModelTypeVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="modelTypeVariable", type=structure_VirtualType, multiplicity=Multiplicity(0, 9999))
    }
)
typeDefinition152: BinaryAssociation = BinaryAssociation(
    name="typeDefinition152",
    ends={
        Property(name="structure_ModelElementTypeDefinition153", type=org_structure_VirtualType, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_VirtualType", type=structure_ModelElementTypeDefinition, multiplicity=Multiplicity(1, 1))
    }
)
modelTypeVariable154: BinaryAssociation = BinaryAssociation(
    name="modelTypeVariable154",
    ends={
        Property(name="ModelTypeVariable", type=org_structure_VirtualType, multiplicity=Multiplicity(1, 1)),
        Property(name="virtualType", type=structure_ModelTypeVariable, multiplicity=Multiplicity(1, 1))
    }
)
typeParamBinding155: BinaryAssociation = BinaryAssociation(
    name="typeParamBinding155",
    ends={
        Property(name="structure_TypeVariableBinding157", type=org_structure_VirtualType, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_VirtualType156", type=structure_TypeVariableBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usings159: BinaryAssociation = BinaryAssociation(
    name="usings159",
    ends={
        Property(name="structure_Using160", type=org_structure_UnresolvedType, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_UnresolvedType", type=structure_Using, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generics161: BinaryAssociation = BinaryAssociation(
    name="generics161",
    ends={
        Property(name="structure_Type163", type=org_structure_UnresolvedType, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_UnresolvedType162", type=structure_Type, multiplicity=Multiplicity(0, 9999))
    }
)
type164: BinaryAssociation = BinaryAssociation(
    name="type164",
    ends={
        Property(name="structure_Type165", type=org_structure_ProductType, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ProductType", type=structure_Type, multiplicity=Multiplicity(0, 9999))
    }
)
left166: BinaryAssociation = BinaryAssociation(
    name="left166",
    ends={
        Property(name="structure_Type167", type=org_structure_FunctionType, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_FunctionType", type=structure_Type, multiplicity=Multiplicity(0, 1))
    }
)
right168: BinaryAssociation = BinaryAssociation(
    name="right168",
    ends={
        Property(name="structure_Type170", type=org_structure_FunctionType, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_FunctionType169", type=structure_Type, multiplicity=Multiplicity(0, 1))
    }
)
parameters204: BinaryAssociation = BinaryAssociation(
    name="parameters204",
    ends={
        Property(name="structure_KermetaModelElement205", type=org_structure_UseAdaptationOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_UseAdaptationOperator", type=structure_KermetaModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedUnresolved206: BinaryAssociation = BinaryAssociation(
    name="ownedUnresolved206",
    ends={
        Property(name="structure_UnresolvedReference", type=org_structure_UseAdaptationOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_UseAdaptationOperator207", type=structure_UnresolvedReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usedOperator208: BinaryAssociation = BinaryAssociation(
    name="usedOperator208",
    ends={
        Property(name="structure_AdaptationOperator210", type=org_structure_UseAdaptationOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_UseAdaptationOperator209", type=structure_AdaptationOperator, multiplicity=Multiplicity(1, 1))
    }
)
ownedClassDefinitionBindings171: BinaryAssociation = BinaryAssociation(
    name="ownedClassDefinitionBindings171",
    ends={
        Property(name="structure_ClassDefinitionBinding", type=org_structure_ModelTypeDefinitionBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ModelTypeDefinitionBinding", type=structure_ClassDefinitionBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usedAdaptationOperators172: BinaryAssociation = BinaryAssociation(
    name="usedAdaptationOperators172",
    ends={
        Property(name="structure_UseAdaptationOperator", type=org_structure_ModelTypeDefinitionBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ModelTypeDefinitionBinding173", type=structure_UseAdaptationOperator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEnumerationBindings174: BinaryAssociation = BinaryAssociation(
    name="ownedEnumerationBindings174",
    ends={
        Property(name="structure_EnumerationBinding", type=org_structure_ModelTypeDefinitionBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ModelTypeDefinitionBinding175", type=structure_EnumerationBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
boundModelTypeDefinition176: BinaryAssociation = BinaryAssociation(
    name="boundModelTypeDefinition176",
    ends={
        Property(name="structure_ModelTypeDefinition", type=org_structure_ModelTypeDefinitionBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ModelTypeDefinitionBinding177", type=structure_ModelTypeDefinition, multiplicity=Multiplicity(1, 1))
    }
)
targetedTransformations178: BinaryAssociation = BinaryAssociation(
    name="targetedTransformations178",
    ends={
        Property(name="structure_ModelTransformation180", type=org_structure_ModelTypeDefinitionBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ModelTypeDefinitionBinding179", type=structure_ModelTransformation, multiplicity=Multiplicity(0, 9999))
    }
)
ownedPropertyBindings181: BinaryAssociation = BinaryAssociation(
    name="ownedPropertyBindings181",
    ends={
        Property(name="structure_PropertyBinding", type=org_structure_ClassDefinitionBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ClassDefinitionBinding", type=structure_PropertyBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperationBindings182: BinaryAssociation = BinaryAssociation(
    name="ownedOperationBindings182",
    ends={
        Property(name="structure_OperationBinding", type=org_structure_ClassDefinitionBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ClassDefinitionBinding183", type=structure_OperationBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source184: BinaryAssociation = BinaryAssociation(
    name="source184",
    ends={
        Property(name="structure_ClassDefinition", type=org_structure_ClassDefinitionBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ClassDefinitionBinding185", type=structure_ClassDefinition, multiplicity=Multiplicity(1, 1))
    }
)
target186: BinaryAssociation = BinaryAssociation(
    name="target186",
    ends={
        Property(name="structure_ClassDefinition188", type=org_structure_ClassDefinitionBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ClassDefinitionBinding187", type=structure_ClassDefinition, multiplicity=Multiplicity(1, 1))
    }
)
source189: BinaryAssociation = BinaryAssociation(
    name="source189",
    ends={
        Property(name="structure_Enumeration", type=org_structure_EnumerationBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_EnumerationBinding", type=structure_Enumeration, multiplicity=Multiplicity(1, 1))
    }
)
target190: BinaryAssociation = BinaryAssociation(
    name="target190",
    ends={
        Property(name="structure_Enumeration192", type=org_structure_EnumerationBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_EnumerationBinding191", type=structure_Enumeration, multiplicity=Multiplicity(1, 1))
    }
)
source193: BinaryAssociation = BinaryAssociation(
    name="source193",
    ends={
        Property(name="structure_Property194", type=org_structure_PropertyBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_PropertyBinding", type=structure_Property, multiplicity=Multiplicity(1, 1))
    }
)
target195: BinaryAssociation = BinaryAssociation(
    name="target195",
    ends={
        Property(name="structure_Property197", type=org_structure_PropertyBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_PropertyBinding196", type=structure_Property, multiplicity=Multiplicity(1, 1))
    }
)
source198: BinaryAssociation = BinaryAssociation(
    name="source198",
    ends={
        Property(name="structure_Operation199", type=org_structure_OperationBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_OperationBinding", type=structure_Operation, multiplicity=Multiplicity(1, 1))
    }
)
target200: BinaryAssociation = BinaryAssociation(
    name="target200",
    ends={
        Property(name="structure_Operation202", type=org_structure_OperationBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_OperationBinding201", type=structure_Operation, multiplicity=Multiplicity(1, 1))
    }
)
parameters203: BinaryAssociation = BinaryAssociation(
    name="parameters203",
    ends={
        Property(name="structure_AdaptationParameter", type=org_structure_AdaptationOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_AdaptationOperator", type=structure_AdaptationParameter, multiplicity=Multiplicity(0, 9999))
    }
)
owningModelTypeDefinition233: BinaryAssociation = BinaryAssociation(
    name="owningModelTypeDefinition233",
    ends={
        Property(name="ModelTypeDefinition", type=org_structure_ModelTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedTransformations", type=structure_ModelTypeDefinition, multiplicity=Multiplicity(0, 1))
    }
)
ownedParameter234: BinaryAssociation = BinaryAssociation(
    name="ownedParameter234",
    ends={
        Property(name="structure_Parameter", type=org_structure_ModelTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ModelTransformation235", type=structure_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target211: BinaryAssociation = BinaryAssociation(
    name="target211",
    ends={
        Property(name="structure_Property212", type=org_structure_PropertyAdaptationOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_PropertyAdaptationOperator", type=structure_Property, multiplicity=Multiplicity(1, 1))
    }
)
target213: BinaryAssociation = BinaryAssociation(
    name="target213",
    ends={
        Property(name="structure_Operation214", type=org_structure_OperationAdaptationOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_OperationAdaptationOperator", type=structure_Operation, multiplicity=Multiplicity(1, 1))
    }
)
typeDefinition215: BinaryAssociation = BinaryAssociation(
    name="typeDefinition215",
    ends={
        Property(name="structure_ModelTypeDefinition216", type=org_structure_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ModelType", type=structure_ModelTypeDefinition, multiplicity=Multiplicity(1, 1))
    }
)
metamodel217: BinaryAssociation = BinaryAssociation(
    name="metamodel217",
    ends={
        Property(name="structure_Metamodel", type=org_structure_FilteredMetamodelReference, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_FilteredMetamodelReference", type=structure_Metamodel, multiplicity=Multiplicity(1, 1))
    }
)
metamodel218: BinaryAssociation = BinaryAssociation(
    name="metamodel218",
    ends={
        Property(name="structure_Metamodel219", type=org_structure_ModelTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ModelTypeDefinition", type=structure_Metamodel, multiplicity=Multiplicity(1, 1))
    }
)
ownedBindings220: BinaryAssociation = BinaryAssociation(
    name="ownedBindings220",
    ends={
        Property(name="structure_ModelTypeDefinitionBinding", type=org_structure_ModelTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ModelTypeDefinition221", type=structure_ModelTypeDefinitionBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTransformations222: BinaryAssociation = BinaryAssociation(
    name="ownedTransformations222",
    ends={
        Property(name="ModelTransformation", type=org_structure_ModelTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="owningModelTypeDefinition", type=structure_ModelTransformation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeDefinitions223: BinaryAssociation = BinaryAssociation(
    name="typeDefinitions223",
    ends={
        Property(name="structure_ModelElementTypeDefinition225", type=org_structure_ModelTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ModelTypeDefinition224", type=structure_ModelElementTypeDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
typeParameters226: BinaryAssociation = BinaryAssociation(
    name="typeParameters226",
    ends={
        Property(name="structure_ModelTypeVariable", type=org_structure_ModelTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ModelTransformation", type=structure_ModelTypeVariable, multiplicity=Multiplicity(0, 9999))
    }
)
body227: BinaryAssociation = BinaryAssociation(
    name="body227",
    ends={
        Property(name="behavior_Expression229", type=org_structure_ModelTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ModelTransformation228", type=behavior_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rules230: BinaryAssociation = BinaryAssociation(
    name="rules230",
    ends={
        Property(name="structure_Operation232", type=org_structure_ModelTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ModelTransformation231", type=structure_Operation, multiplicity=Multiplicity(0, 9999))
    }
)
ownedModelTypeDefinitions236: BinaryAssociation = BinaryAssociation(
    name="ownedModelTypeDefinitions236",
    ends={
        Property(name="structure_ModelTypeDefinition237", type=org_structure_ModelTypeDefinitionContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="org_structure_ModelTypeDefinitionContainer", type=structure_ModelTypeDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_org_behavior_Assignment_Expression = Generalization(general=Expression, specific=org_behavior_Assignment)
gen_org_behavior_CallVariable_CallExpression = Generalization(general=CallExpression, specific=org_behavior_CallVariable)
gen_org_behavior_Expression_structure_KermetaModelElement = Generalization(general=structure_KermetaModelElement, specific=org_behavior_Expression)
gen_org_behavior_Expression_structure_TypeContainer = Generalization(general=structure_TypeContainer, specific=org_behavior_Expression)
gen_org_behavior_CallExpression_Expression = Generalization(general=Expression, specific=org_behavior_CallExpression)
gen_org_behavior_Block_Expression = Generalization(general=Expression, specific=org_behavior_Block)
gen_org_behavior_Rescue_KermetaModelElement = Generalization(general=KermetaModelElement, specific=org_behavior_Rescue)
gen_org_behavior_CallFeature_CallExpression = Generalization(general=CallExpression, specific=org_behavior_CallFeature)
gen_org_behavior_CallSuperOperation_CallOperation = Generalization(general=CallOperation, specific=org_behavior_CallSuperOperation)
gen_org_behavior_CallResult_CallVariable = Generalization(general=CallVariable, specific=org_behavior_CallResult)
gen_org_behavior_CallValue_CallExpression = Generalization(general=CallExpression, specific=org_behavior_CallValue)
gen_org_behavior_Conditional_Expression = Generalization(general=Expression, specific=org_behavior_Conditional)
gen_org_behavior_Raise_Expression = Generalization(general=Expression, specific=org_behavior_Raise)
gen_org_behavior_StringLiteral_Literal = Generalization(general=Literal, specific=org_behavior_StringLiteral)
gen_org_behavior_BooleanLiteral_Literal = Generalization(general=Literal, specific=org_behavior_BooleanLiteral)
gen_org_behavior_CallTypeLiteral_Literal = Generalization(general=Literal, specific=org_behavior_CallTypeLiteral)
gen_org_behavior_TypeReference_MultiplicityElement = Generalization(general=MultiplicityElement, specific=org_behavior_TypeReference)
gen_org_behavior_Literal_Expression = Generalization(general=Expression, specific=org_behavior_Literal)
gen_org_behavior_EmptyExpression_Expression = Generalization(general=Expression, specific=org_behavior_EmptyExpression)
gen_org_behavior_JavaStaticCall_Expression = Generalization(general=Expression, specific=org_behavior_JavaStaticCall)
gen_org_behavior_LambdaExpression_Expression = Generalization(general=Expression, specific=org_behavior_LambdaExpression)
gen_org_behavior_LambdaParameter_KermetaModelElement = Generalization(general=KermetaModelElement, specific=org_behavior_LambdaParameter)
gen_org_behavior_IntegerLiteral_Literal = Generalization(general=Literal, specific=org_behavior_IntegerLiteral)
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
gen_org_structure_Type_KermetaModelElement = Generalization(general=KermetaModelElement, specific=org_structure_Type)
gen_org_structure_Property_structure_MultiplicityElement = Generalization(general=structure_MultiplicityElement, specific=org_structure_Property)
gen_org_structure_Property_structure_AbstractProperty = Generalization(general=structure_AbstractProperty, specific=org_structure_Property)
gen_org_structure_Class_ParameterizedType = Generalization(general=ParameterizedType, specific=org_structure_Class)
gen_org_structure_TypeContainer_KermetaModelElement = Generalization(general=KermetaModelElement, specific=org_structure_TypeContainer)
gen_org_structure_EnumerationLiteral_NamedElement = Generalization(general=NamedElement, specific=org_structure_EnumerationLiteral)
gen_org_structure_TypeVariableBinding_structure_TypeContainer = Generalization(general=structure_TypeContainer, specific=org_structure_TypeVariableBinding)
gen_org_structure_TypeVariableBinding_structure_KermetaModelElement = Generalization(general=structure_KermetaModelElement, specific=org_structure_TypeVariableBinding)
gen_org_structure_MultiplicityElement_TypedElement = Generalization(general=TypedElement, specific=org_structure_MultiplicityElement)
gen_org_structure_TypeDefinition_structure_NamedElement = Generalization(general=structure_NamedElement, specific=org_structure_TypeDefinition)
gen_org_structure_TypeDefinition_structure_TypeContainer = Generalization(general=structure_TypeContainer, specific=org_structure_TypeDefinition)
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
gen_org_structure_GenericTypeDefinition_ModelElementTypeDefinition = Generalization(general=ModelElementTypeDefinition, specific=org_structure_GenericTypeDefinition)
gen_org_structure_ClassDefinition_GenericTypeDefinition = Generalization(general=GenericTypeDefinition, specific=org_structure_ClassDefinition)
gen_org_structure_Metamodel_structure_KermetaModelElement = Generalization(general=structure_KermetaModelElement, specific=org_structure_Metamodel)
gen_org_structure_Metamodel_structure_NamedElement = Generalization(general=structure_NamedElement, specific=org_structure_Metamodel)
gen_org_structure_Metamodel_structure_ModelTypeDefinitionContainer = Generalization(general=structure_ModelTypeDefinitionContainer, specific=org_structure_Metamodel)
gen_org_structure_ModelElementTypeDefinitionContainer_NamedElement = Generalization(general=NamedElement, specific=org_structure_ModelElementTypeDefinitionContainer)
gen_org_structure_Model_KermetaModelElement = Generalization(general=KermetaModelElement, specific=org_structure_Model)
gen_org_structure_AbstractOperation_KermetaModelElement = Generalization(general=KermetaModelElement, specific=org_structure_AbstractOperation)
gen_org_structure_UnresolvedType_structure_Type = Generalization(general=structure_Type, specific=org_structure_UnresolvedType)
gen_org_structure_ParameterizedType_Type = Generalization(general=Type, specific=org_structure_ParameterizedType)
gen_org_structure_TypeVariable_structure_TypeContainer = Generalization(general=structure_TypeContainer, specific=org_structure_TypeVariable)
gen_org_structure_TypeVariable_structure_Type = Generalization(general=structure_Type, specific=org_structure_TypeVariable)
gen_org_structure_TypeVariable_structure_NamedElement = Generalization(general=structure_NamedElement, specific=org_structure_TypeVariable)
gen_org_structure_ObjectTypeVariable_TypeVariable = Generalization(general=TypeVariable, specific=org_structure_ObjectTypeVariable)
gen_org_structure_ModelTypeVariable_TypeVariable = Generalization(general=TypeVariable, specific=org_structure_ModelTypeVariable)
gen_org_structure_VirtualType_ObjectTypeVariable = Generalization(general=ObjectTypeVariable, specific=org_structure_VirtualType)
gen_org_structure_VoidType_Type = Generalization(general=Type, specific=org_structure_VoidType)
gen_org_structure_UnresolvedInferredType_structure_UnresolvedReference = Generalization(general=structure_UnresolvedReference, specific=org_structure_UnresolvedInferredType)
gen_org_structure_UnresolvedInferredType_structure_Type = Generalization(general=structure_Type, specific=org_structure_UnresolvedInferredType)
gen_org_structure_UnresolvedTypeVariable_structure_UnresolvedReference = Generalization(general=structure_UnresolvedReference, specific=org_structure_UnresolvedTypeVariable)
gen_org_structure_UnresolvedTypeVariable_structure_TypeVariable = Generalization(general=structure_TypeVariable, specific=org_structure_UnresolvedTypeVariable)
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
gen_org_structure_PropertyAdaptationOperator_AdaptationOperator = Generalization(general=AdaptationOperator, specific=org_structure_PropertyAdaptationOperator)
gen_org_structure_ModelTypeDefinitionBinding_structure_KermetaModelElement = Generalization(general=structure_KermetaModelElement, specific=org_structure_ModelTypeDefinitionBinding)
gen_org_structure_ModelTypeDefinitionBinding_structure_ModelTypeDefinitionContainer = Generalization(general=structure_ModelTypeDefinitionContainer, specific=org_structure_ModelTypeDefinitionBinding)
gen_org_structure_ClassDefinitionBinding_KermetaModelElement = Generalization(general=KermetaModelElement, specific=org_structure_ClassDefinitionBinding)
gen_org_structure_EnumerationBinding_KermetaModelElement = Generalization(general=KermetaModelElement, specific=org_structure_EnumerationBinding)
gen_org_structure_PropertyBinding_KermetaModelElement = Generalization(general=KermetaModelElement, specific=org_structure_PropertyBinding)
gen_org_structure_OperationBinding_KermetaModelElement = Generalization(general=KermetaModelElement, specific=org_structure_OperationBinding)
gen_org_structure_AdaptationOperator_NamedElement = Generalization(general=NamedElement, specific=org_structure_AdaptationOperator)
gen_org_structure_UseAdaptationOperator_KermetaModelElement = Generalization(general=KermetaModelElement, specific=org_structure_UseAdaptationOperator)
gen_org_structure_UnresolvedModelTypeDefinition_structure_ModelTypeDefinition = Generalization(general=structure_ModelTypeDefinition, specific=org_structure_UnresolvedModelTypeDefinition)
gen_org_structure_UnresolvedModelTypeDefinition_structure_UnresolvedReference = Generalization(general=structure_UnresolvedReference, specific=org_structure_UnresolvedModelTypeDefinition)
gen_org_structure_UnresolvedModelTransformation_structure_ModelTransformation = Generalization(general=structure_ModelTransformation, specific=org_structure_UnresolvedModelTransformation)
gen_org_structure_UnresolvedModelTransformation_structure_UnresolvedReference = Generalization(general=structure_UnresolvedReference, specific=org_structure_UnresolvedModelTransformation)
gen_org_structure_ModelTypeDefinitionContainer_KermetaModelElement = Generalization(general=KermetaModelElement, specific=org_structure_ModelTypeDefinitionContainer)
gen_org_structure_UnresolvedAdaptationOperator_structure_AdaptationOperator = Generalization(general=structure_AdaptationOperator, specific=org_structure_UnresolvedAdaptationOperator)
gen_org_structure_UnresolvedAdaptationOperator_structure_UnresolvedReference = Generalization(general=structure_UnresolvedReference, specific=org_structure_UnresolvedAdaptationOperator)
gen_org_structure_AdaptationParameter_TypedElement = Generalization(general=TypedElement, specific=org_structure_AdaptationParameter)
gen_org_structure_OperationAdaptationOperator_AdaptationOperator = Generalization(general=AdaptationOperator, specific=org_structure_OperationAdaptationOperator)
gen_org_structure_ModelElementTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=org_structure_ModelElementTypeDefinition)
gen_org_structure_ModelType_Type = Generalization(general=Type, specific=org_structure_ModelType)
gen_org_structure_FilteredMetamodelReference_KermetaModelElement = Generalization(general=KermetaModelElement, specific=org_structure_FilteredMetamodelReference)
gen_org_structure_ModelTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=org_structure_ModelTypeDefinition)
gen_org_structure_ModelTransformation_MultiplicityElement = Generalization(general=MultiplicityElement, specific=org_structure_ModelTransformation)

# Domain Model
domain_model = DomainModel(
    name="org",
    types={org_behavior_Assignment, Expression, behavior_Rescue, org_behavior_CallVariable, CallExpression, behavior_CallExpression, behavior_Expression, org_behavior_Expression, structure_KermetaModelElement, structure_TypeContainer, structure_Type, org_behavior_CallExpression, org_behavior_Block, org_behavior_Rescue, KermetaModelElement, behavior_TypeReference, org_behavior_CallFeature, org_behavior_CallSuperOperation, CallOperation, org_behavior_CallResult, CallVariable, org_behavior_CallValue, org_behavior_Conditional, org_behavior_Raise, org_behavior_StringLiteral, org_behavior_BooleanLiteral, org_behavior_CallTypeLiteral, org_behavior_TypeReference, MultiplicityElement, org_behavior_Literal, org_behavior_EmptyExpression, org_behavior_JavaStaticCall, org_behavior_LambdaExpression, behavior_LambdaParameter, org_behavior_LambdaParameter, org_behavior_IntegerLiteral, Literal, org_behavior_VoidLiteral, org_behavior_Loop, org_behavior_SelfExpression, org_behavior_VariableDecl, org_behavior_UnresolvedCall, structure_UnresolvedReference, structure_Using, structure_UnresolvedOperation, org_behavior_CallOperation, CallFeature, structure_Operation, org_behavior_CallProperty, structure_Property, org_behavior_CallEnumLiteral, structure_EnumerationLiteral, org_behavior_CallModelTransformation, structure_ModelTransformation, org_structure_KermetaModelElement, structure_Tag, org_structure_Operation, structure_MultiplicityElement, structure_AbstractOperation, structure_Parameter, structure_Constraint, org_structure_Type, structure_ClassDefinition, structure_TypeVariable, org_structure_Property, structure_AbstractProperty, structure_UnresolvedProperty, org_structure_Class, ParameterizedType, org_structure_TypeContainer, org_structure_EnumerationLiteral, NamedElement, structure_Enumeration, org_structure_TypeVariableBinding, org_structure_MultiplicityElement, TypedElement, org_structure_TypeDefinition, structure_NamedElement, structure_AdaptationOperator, structure_Class, org_structure_DataType, structure_ModelElementTypeDefinition, org_structure_Enumeration, DataType, org_structure_NamedElement, org_structure_Package, structure_ModelElementTypeDefinitionContainer, structure_Package, org_structure_Parameter, org_structure_PrimitiveType, org_structure_TypedElement, org_structure_Tag, org_structure_AbstractProperty, org_structure_Constraint, org_structure_GenericTypeDefinition, ModelElementTypeDefinition, org_structure_ClassDefinition, GenericTypeDefinition, org_structure_Metamodel, structure_ModelTypeDefinitionContainer, structure_FilteredMetamodelReference, org_structure_ModelElementTypeDefinitionContainer, org_structure_Model, org_structure_AbstractOperation, org_structure_UnresolvedType, org_structure_ParameterizedType, Type, structure_TypeVariableBinding, structure_GenericTypeDefinition, org_structure_TypeVariable, org_structure_ObjectTypeVariable, TypeVariable, org_structure_ModelTypeVariable, structure_VirtualType, org_structure_VirtualType, ObjectTypeVariable, structure_ModelTypeVariable, org_structure_VoidType, org_structure_UnresolvedInferredType, org_structure_UnresolvedTypeVariable, org_structure_UnresolvedReference, org_structure_UnresolvedProperty, org_structure_UnresolvedOperation, org_structure_Using, org_structure_ProductType, org_structure_FunctionType, org_structure_PropertyAdaptationOperator, AdaptationOperator, org_structure_ModelTypeDefinitionBinding, structure_ClassDefinitionBinding, structure_UseAdaptationOperator, structure_EnumerationBinding, structure_ModelTypeDefinition, org_structure_ClassDefinitionBinding, structure_PropertyBinding, structure_OperationBinding, org_structure_EnumerationBinding, org_structure_PropertyBinding, org_structure_OperationBinding, org_structure_AdaptationOperator, structure_AdaptationParameter, org_structure_UseAdaptationOperator, org_structure_UnresolvedModelTypeDefinition, org_structure_UnresolvedModelTransformation, org_structure_ModelTypeDefinitionContainer, org_structure_UnresolvedAdaptationOperator, org_structure_AdaptationParameter, org_structure_OperationAdaptationOperator, org_structure_ModelElementTypeDefinition, TypeDefinition, org_structure_ModelType, org_structure_FilteredMetamodelReference, structure_Metamodel, org_structure_ModelTypeDefinition, structure_ModelTypeDefinitionBinding, org_structure_ModelTransformation, ConstraintLanguage, ConstraintType},
    associations={statement9, rescueBlock11, target0, value1, staticType3, parameters4, staticTypeVariableBindings6, body27, exceptionType29, target13, superType15, thenBody17, elseBody19, condition22, expression25, parameters31, parameters33, body34, type37, targetParent58, generics61, typeref39, initialization41, body43, stopCondition46, initialization49, type51, usings54, target55, post74, body76, ownedUnresolvedOperations79, staticOperation64, staticProperty65, staticEnumLiteral66, staticTransformation67, kTag68, kOwnedTags69, raisedException70, ownedParameter72, pre73, typeContainer95, owningClass81, typeParameter82, opposite84, getterBody85, setterBody88, ownedUnresolvedProperties91, owningClass93, ownedAttribute105, ownedOperation107, containedType96, enumeration97, variable98, type100, superType103, nestingPackage114, ownedAdaptationOperators116, superClass110, ownedLiteral112, nestedPackage113, preOwner127, postOwner129, operation117, instanceType118, type120, object122, body123, invOwner125, ownedTypeDefinition140, typeParameter141, inv131, ownedAttribute133, ownedOperation134, packages137, referencedMetamodels138, contents158, virtualTypeBinding143, typeParamBinding144, typeDefinition147, supertype149, virtualType151, typeDefinition152, modelTypeVariable154, typeParamBinding155, usings159, generics161, type164, left166, right168, parameters204, ownedUnresolved206, usedOperator208, ownedClassDefinitionBindings171, usedAdaptationOperators172, ownedEnumerationBindings174, boundModelTypeDefinition176, targetedTransformations178, ownedPropertyBindings181, ownedOperationBindings182, source184, target186, source189, target190, source193, target195, source198, target200, parameters203, owningModelTypeDefinition233, ownedParameter234, target211, target213, typeDefinition215, metamodel217, metamodel218, ownedBindings220, ownedTransformations222, typeDefinitions223, typeParameters226, body227, rules230, ownedModelTypeDefinitions236},
    generalizations={gen_org_behavior_Assignment_Expression, gen_org_behavior_CallVariable_CallExpression, gen_org_behavior_Expression_structure_KermetaModelElement, gen_org_behavior_Expression_structure_TypeContainer, gen_org_behavior_CallExpression_Expression, gen_org_behavior_Block_Expression, gen_org_behavior_Rescue_KermetaModelElement, gen_org_behavior_CallFeature_CallExpression, gen_org_behavior_CallSuperOperation_CallOperation, gen_org_behavior_CallResult_CallVariable, gen_org_behavior_CallValue_CallExpression, gen_org_behavior_Conditional_Expression, gen_org_behavior_Raise_Expression, gen_org_behavior_StringLiteral_Literal, gen_org_behavior_BooleanLiteral_Literal, gen_org_behavior_CallTypeLiteral_Literal, gen_org_behavior_TypeReference_MultiplicityElement, gen_org_behavior_Literal_Expression, gen_org_behavior_EmptyExpression_Expression, gen_org_behavior_JavaStaticCall_Expression, gen_org_behavior_LambdaExpression_Expression, gen_org_behavior_LambdaParameter_KermetaModelElement, gen_org_behavior_IntegerLiteral_Literal, gen_org_behavior_VoidLiteral_Literal, gen_org_behavior_Loop_Expression, gen_org_behavior_SelfExpression_Expression, gen_org_behavior_VariableDecl_Expression, gen_org_behavior_UnresolvedCall_structure_UnresolvedReference, gen_org_behavior_UnresolvedCall_behavior_CallExpression, gen_org_behavior_UnresolvedCall_structure_TypeContainer, gen_org_behavior_CallOperation_CallFeature, gen_org_behavior_CallProperty_CallFeature, gen_org_behavior_CallEnumLiteral_CallExpression, gen_org_behavior_CallModelTransformation_CallFeature, gen_org_structure_Operation_structure_MultiplicityElement, gen_org_structure_Operation_structure_AbstractOperation, gen_org_structure_Type_KermetaModelElement, gen_org_structure_Property_structure_MultiplicityElement, gen_org_structure_Property_structure_AbstractProperty, gen_org_structure_Class_ParameterizedType, gen_org_structure_TypeContainer_KermetaModelElement, gen_org_structure_EnumerationLiteral_NamedElement, gen_org_structure_TypeVariableBinding_structure_TypeContainer, gen_org_structure_TypeVariableBinding_structure_KermetaModelElement, gen_org_structure_MultiplicityElement_TypedElement, gen_org_structure_TypeDefinition_structure_NamedElement, gen_org_structure_TypeDefinition_structure_TypeContainer, gen_org_structure_DataType_structure_Type, gen_org_structure_DataType_structure_ModelElementTypeDefinition, gen_org_structure_Enumeration_DataType, gen_org_structure_NamedElement_KermetaModelElement, gen_org_structure_Package_structure_NamedElement, gen_org_structure_Package_structure_ModelElementTypeDefinitionContainer, gen_org_structure_Parameter_MultiplicityElement, gen_org_structure_PrimitiveType_DataType, gen_org_structure_TypedElement_structure_TypeContainer, gen_org_structure_TypedElement_structure_NamedElement, gen_org_structure_Tag_KermetaModelElement, gen_org_structure_AbstractProperty_KermetaModelElement, gen_org_structure_Constraint_NamedElement, gen_org_structure_GenericTypeDefinition_ModelElementTypeDefinition, gen_org_structure_ClassDefinition_GenericTypeDefinition, gen_org_structure_Metamodel_structure_KermetaModelElement, gen_org_structure_Metamodel_structure_NamedElement, gen_org_structure_Metamodel_structure_ModelTypeDefinitionContainer, gen_org_structure_ModelElementTypeDefinitionContainer_NamedElement, gen_org_structure_Model_KermetaModelElement, gen_org_structure_AbstractOperation_KermetaModelElement, gen_org_structure_UnresolvedType_structure_Type, gen_org_structure_ParameterizedType_Type, gen_org_structure_TypeVariable_structure_TypeContainer, gen_org_structure_TypeVariable_structure_Type, gen_org_structure_TypeVariable_structure_NamedElement, gen_org_structure_ObjectTypeVariable_TypeVariable, gen_org_structure_ModelTypeVariable_TypeVariable, gen_org_structure_VirtualType_ObjectTypeVariable, gen_org_structure_VoidType_Type, gen_org_structure_UnresolvedInferredType_structure_UnresolvedReference, gen_org_structure_UnresolvedInferredType_structure_Type, gen_org_structure_UnresolvedTypeVariable_structure_UnresolvedReference, gen_org_structure_UnresolvedTypeVariable_structure_TypeVariable, gen_org_structure_UnresolvedType_structure_UnresolvedReference, gen_org_structure_UnresolvedType_structure_TypeContainer, gen_org_structure_UnresolvedReference_KermetaModelElement, gen_org_structure_UnresolvedProperty_structure_AbstractProperty, gen_org_structure_UnresolvedProperty_structure_UnresolvedReference, gen_org_structure_UnresolvedOperation_structure_AbstractOperation, gen_org_structure_UnresolvedOperation_structure_UnresolvedReference, gen_org_structure_UnresolvedOperation_structure_TypeContainer, gen_org_structure_Using_KermetaModelElement, gen_org_structure_ProductType_structure_TypeContainer, gen_org_structure_ProductType_structure_Type, gen_org_structure_FunctionType_structure_TypeContainer, gen_org_structure_FunctionType_structure_Type, gen_org_structure_PropertyAdaptationOperator_AdaptationOperator, gen_org_structure_ModelTypeDefinitionBinding_structure_KermetaModelElement, gen_org_structure_ModelTypeDefinitionBinding_structure_ModelTypeDefinitionContainer, gen_org_structure_ClassDefinitionBinding_KermetaModelElement, gen_org_structure_EnumerationBinding_KermetaModelElement, gen_org_structure_PropertyBinding_KermetaModelElement, gen_org_structure_OperationBinding_KermetaModelElement, gen_org_structure_AdaptationOperator_NamedElement, gen_org_structure_UseAdaptationOperator_KermetaModelElement, gen_org_structure_UnresolvedModelTypeDefinition_structure_ModelTypeDefinition, gen_org_structure_UnresolvedModelTypeDefinition_structure_UnresolvedReference, gen_org_structure_UnresolvedModelTransformation_structure_ModelTransformation, gen_org_structure_UnresolvedModelTransformation_structure_UnresolvedReference, gen_org_structure_ModelTypeDefinitionContainer_KermetaModelElement, gen_org_structure_UnresolvedAdaptationOperator_structure_AdaptationOperator, gen_org_structure_UnresolvedAdaptationOperator_structure_UnresolvedReference, gen_org_structure_AdaptationParameter_TypedElement, gen_org_structure_OperationAdaptationOperator_AdaptationOperator, gen_org_structure_ModelElementTypeDefinition_TypeDefinition, gen_org_structure_ModelType_Type, gen_org_structure_FilteredMetamodelReference_KermetaModelElement, gen_org_structure_ModelTypeDefinition_TypeDefinition, gen_org_structure_ModelTransformation_MultiplicityElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)