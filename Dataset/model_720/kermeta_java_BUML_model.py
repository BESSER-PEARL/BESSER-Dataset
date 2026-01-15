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
kermeta_behavior_Expression = Class(name="kermeta::behavior::Expression", is_abstract=True)
structure_Object = Class(name="structure::Object")
structure_TypeContainer = Class(name="structure::TypeContainer")
structure_Type = Class(name="structure::Type")
kermeta_DummyClass = Class(name="kermeta::DummyClass", is_abstract=True)
kermeta_language_DummyClass = Class(name="kermeta::language::DummyClass", is_abstract=True)
kermeta_behavior_Assignment = Class(name="kermeta::behavior::Assignment")
Expression = Class(name="Expression")
behavior_CallExpression = Class(name="behavior::CallExpression")
behavior_Expression = Class(name="behavior::Expression")
kermeta_behavior_CallExpression = Class(name="kermeta::behavior::CallExpression", is_abstract=True)
kermeta_behavior_Block = Class(name="kermeta::behavior::Block")
behavior_Rescue = Class(name="behavior::Rescue")
structure_Operation = Class(name="structure::Operation")
kermeta_behavior_CallVariable = Class(name="kermeta::behavior::CallVariable")
CallExpression = Class(name="CallExpression")
kermeta_behavior_CallFeature = Class(name="kermeta::behavior::CallFeature")
structure_Property = Class(name="structure::Property")
kermeta_behavior_Raise = Class(name="kermeta::behavior::Raise")
structure_EnumerationLiteral = Class(name="structure::EnumerationLiteral")
kermeta_behavior_CallSuperOperation = Class(name="kermeta::behavior::CallSuperOperation")
kermeta_behavior_CallResult = Class(name="kermeta::behavior::CallResult")
CallVariable = Class(name="CallVariable")
kermeta_behavior_CallValue = Class(name="kermeta::behavior::CallValue")
kermeta_behavior_Conditional = Class(name="kermeta::behavior::Conditional")
kermeta_behavior_EmptyExpression = Class(name="kermeta::behavior::EmptyExpression")
kermeta_behavior_Rescue = Class(name="kermeta::behavior::Rescue")
Object = Class(name="Object")
behavior_TypeReference = Class(name="behavior::TypeReference")
kermeta_behavior_TypeReference = Class(name="kermeta::behavior::TypeReference")
MultiplicityElement = Class(name="MultiplicityElement")
kermeta_behavior_Literal = Class(name="kermeta::behavior::Literal", is_abstract=True)
kermeta_behavior_LambdaExpression = Class(name="kermeta::behavior::LambdaExpression")
kermeta_behavior_JavaStaticCall = Class(name="kermeta::behavior::JavaStaticCall")
behavior_LambdaParameter = Class(name="behavior::LambdaParameter")
kermeta_behavior_LambdaParameter = Class(name="kermeta::behavior::LambdaParameter")
kermeta_behavior_IntegerLiteral = Class(name="kermeta::behavior::IntegerLiteral")
Literal = Class(name="Literal")
kermeta_behavior_StringLiteral = Class(name="kermeta::behavior::StringLiteral")
kermeta_behavior_BooleanLiteral = Class(name="kermeta::behavior::BooleanLiteral")
kermeta_behavior_TypeLiteral = Class(name="kermeta::behavior::TypeLiteral")
kermeta_behavior_VoidLiteral = Class(name="kermeta::behavior::VoidLiteral")
kermeta_behavior_Loop = Class(name="kermeta::behavior::Loop")
kermeta_behavior_SelfExpression = Class(name="kermeta::behavior::SelfExpression")
kermeta_behavior_VariableDecl = Class(name="kermeta::behavior::VariableDecl")
kermeta_structure_Class = Class(name="kermeta::structure::Class")
ParameterizedType = Class(name="ParameterizedType")
structure_Class = Class(name="structure::Class")
kermeta_structure_ModelType = Class(name="kermeta::structure::ModelType")
kermeta_structure_Object = Class(name="kermeta::structure::Object")
structure_Tag = Class(name="structure::Tag")
kermeta_structure_Model = Class(name="kermeta::structure::Model")
structure_Constraint = Class(name="structure::Constraint")
structure_TypeDefinition = Class(name="structure::TypeDefinition")
kermeta_structure_Operation = Class(name="kermeta::structure::Operation")
structure_Parameter = Class(name="structure::Parameter")
structure_ClassDefinition = Class(name="structure::ClassDefinition")
structure_TypeVariable = Class(name="structure::TypeVariable")
kermeta_structure_Property = Class(name="kermeta::structure::Property")
kermeta_structure_Type = Class(name="kermeta::structure::Type")
kermeta_structure_TypeContainer = Class(name="kermeta::structure::TypeContainer", is_abstract=True)
kermeta_structure_EnumerationLiteral = Class(name="kermeta::structure::EnumerationLiteral")
NamedElement = Class(name="NamedElement")
structure_Enumeration = Class(name="structure::Enumeration")
kermeta_structure_TypeVariableBinding = Class(name="kermeta::structure::TypeVariableBinding")
kermeta_structure_MultiplicityElement = Class(name="kermeta::structure::MultiplicityElement")
TypedElement = Class(name="TypedElement")
kermeta_structure_TypeDefinition = Class(name="kermeta::structure::TypeDefinition")
structure_Package = Class(name="structure::Package")
kermeta_structure_DataType = Class(name="kermeta::structure::DataType", is_abstract=True)
kermeta_structure_Enumeration = Class(name="kermeta::structure::Enumeration")
DataType = Class(name="DataType")
kermeta_structure_NamedElement = Class(name="kermeta::structure::NamedElement", is_abstract=True)
kermeta_structure_Package = Class(name="kermeta::structure::Package")
structure_NamedElement = Class(name="structure::NamedElement")
structure_TypeDefinitionContainer = Class(name="structure::TypeDefinitionContainer")
kermeta_structure_Parameter = Class(name="kermeta::structure::Parameter")
kermeta_structure_PrimitiveType = Class(name="kermeta::structure::PrimitiveType")
structure_DataType = Class(name="structure::DataType")
kermeta_structure_TypedElement = Class(name="kermeta::structure::TypedElement", is_abstract=True)
kermeta_structure_Tag = Class(name="kermeta::structure::Tag")
kermeta_structure_Constraint = Class(name="kermeta::structure::Constraint")
kermeta_structure_ClassDefinition = Class(name="kermeta::structure::ClassDefinition")
structure_GenericTypeDefinition = Class(name="structure::GenericTypeDefinition")
kermeta_structure_ModelingUnit = Class(name="kermeta::structure::ModelingUnit")
structure_Require = Class(name="structure::Require")
structure_Using = Class(name="structure::Using")
structure_ModelingUnit = Class(name="structure::ModelingUnit")
structure_Filter = Class(name="structure::Filter")
kermeta_structure_Require = Class(name="kermeta::structure::Require")
kermeta_structure_Using = Class(name="kermeta::structure::Using")
kermeta_structure_Filter = Class(name="kermeta::structure::Filter")
kermeta_structure_GenericTypeDefinition = Class(name="kermeta::structure::GenericTypeDefinition", is_abstract=True)
TypeDefinition = Class(name="TypeDefinition")
kermeta_structure_ParameterizedType = Class(name="kermeta::structure::ParameterizedType", is_abstract=True)
Type = Class(name="Type")
structure_TypeVariableBinding = Class(name="structure::TypeVariableBinding")
kermeta_structure_TypeVariable = Class(name="kermeta::structure::TypeVariable", is_abstract=True)
kermeta_structure_ObjectTypeVariable = Class(name="kermeta::structure::ObjectTypeVariable")
TypeVariable = Class(name="TypeVariable")
kermeta_structure_ModelTypeVariable = Class(name="kermeta::structure::ModelTypeVariable")
structure_VirtualType = Class(name="structure::VirtualType")
kermeta_structure_VirtualType = Class(name="kermeta::structure::VirtualType")
ObjectTypeVariable = Class(name="ObjectTypeVariable")
structure_ModelTypeVariable = Class(name="structure::ModelTypeVariable")
kermeta_structure_ProductType = Class(name="kermeta::structure::ProductType")
kermeta_structure_FunctionType = Class(name="kermeta::structure::FunctionType")
kermeta_structure_VoidType = Class(name="kermeta::structure::VoidType")
kermeta_structure_TypeDefinitionContainer = Class(name="kermeta::structure::TypeDefinitionContainer", is_abstract=True)

# kermeta_behavior_Expression class attributes and methods

# structure_Object class attributes and methods

# structure_TypeContainer class attributes and methods

# structure_Type class attributes and methods

# kermeta_DummyClass class attributes and methods

# kermeta_language_DummyClass class attributes and methods

# kermeta_behavior_Assignment class attributes and methods
kermeta_behavior_Assignment_isCast: Property = Property(name="isCast", type=StringType)
kermeta_behavior_Assignment.attributes={kermeta_behavior_Assignment_isCast}

# Expression class attributes and methods

# behavior_CallExpression class attributes and methods

# behavior_Expression class attributes and methods

# kermeta_behavior_CallExpression class attributes and methods
kermeta_behavior_CallExpression_name: Property = Property(name="name", type=StringType)
kermeta_behavior_CallExpression.attributes={kermeta_behavior_CallExpression_name}

# kermeta_behavior_Block class attributes and methods

# behavior_Rescue class attributes and methods

# structure_Operation class attributes and methods

# kermeta_behavior_CallVariable class attributes and methods
kermeta_behavior_CallVariable_isAtpre: Property = Property(name="isAtpre", type=StringType)
kermeta_behavior_CallVariable.attributes={kermeta_behavior_CallVariable_isAtpre}

# CallExpression class attributes and methods

# kermeta_behavior_CallFeature class attributes and methods
kermeta_behavior_CallFeature_isAtpre: Property = Property(name="isAtpre", type=StringType)
kermeta_behavior_CallFeature.attributes={kermeta_behavior_CallFeature_isAtpre}

# structure_Property class attributes and methods

# kermeta_behavior_Raise class attributes and methods

# structure_EnumerationLiteral class attributes and methods

# kermeta_behavior_CallSuperOperation class attributes and methods

# kermeta_behavior_CallResult class attributes and methods

# CallVariable class attributes and methods

# kermeta_behavior_CallValue class attributes and methods

# kermeta_behavior_Conditional class attributes and methods

# kermeta_behavior_EmptyExpression class attributes and methods

# kermeta_behavior_Rescue class attributes and methods
kermeta_behavior_Rescue_exceptionName: Property = Property(name="exceptionName", type=StringType)
kermeta_behavior_Rescue.attributes={kermeta_behavior_Rescue_exceptionName}

# Object class attributes and methods

# behavior_TypeReference class attributes and methods

# kermeta_behavior_TypeReference class attributes and methods

# MultiplicityElement class attributes and methods

# kermeta_behavior_Literal class attributes and methods

# kermeta_behavior_LambdaExpression class attributes and methods

# kermeta_behavior_JavaStaticCall class attributes and methods
kermeta_behavior_JavaStaticCall_jclass: Property = Property(name="jclass", type=StringType)
kermeta_behavior_JavaStaticCall_jmethod: Property = Property(name="jmethod", type=StringType)
kermeta_behavior_JavaStaticCall.attributes={kermeta_behavior_JavaStaticCall_jmethod, kermeta_behavior_JavaStaticCall_jclass}

# behavior_LambdaParameter class attributes and methods

# kermeta_behavior_LambdaParameter class attributes and methods
kermeta_behavior_LambdaParameter_name: Property = Property(name="name", type=StringType)
kermeta_behavior_LambdaParameter.attributes={kermeta_behavior_LambdaParameter_name}

# kermeta_behavior_IntegerLiteral class attributes and methods
kermeta_behavior_IntegerLiteral_value: Property = Property(name="value", type=StringType)
kermeta_behavior_IntegerLiteral.attributes={kermeta_behavior_IntegerLiteral_value}

# Literal class attributes and methods

# kermeta_behavior_StringLiteral class attributes and methods
kermeta_behavior_StringLiteral_value: Property = Property(name="value", type=StringType)
kermeta_behavior_StringLiteral.attributes={kermeta_behavior_StringLiteral_value}

# kermeta_behavior_BooleanLiteral class attributes and methods
kermeta_behavior_BooleanLiteral_value: Property = Property(name="value", type=StringType)
kermeta_behavior_BooleanLiteral.attributes={kermeta_behavior_BooleanLiteral_value}

# kermeta_behavior_TypeLiteral class attributes and methods

# kermeta_behavior_VoidLiteral class attributes and methods

# kermeta_behavior_Loop class attributes and methods

# kermeta_behavior_SelfExpression class attributes and methods

# kermeta_behavior_VariableDecl class attributes and methods
kermeta_behavior_VariableDecl_identifier: Property = Property(name="identifier", type=StringType)
kermeta_behavior_VariableDecl.attributes={kermeta_behavior_VariableDecl_identifier}

# kermeta_structure_Class class attributes and methods
kermeta_structure_Class_isAbstract: Property = Property(name="isAbstract", type=StringType)
kermeta_structure_Class_name: Property = Property(name="name", type=StringType)
kermeta_structure_Class_m__new: Method = Method(name="_new", parameters={}, type=StringType)
kermeta_structure_Class.attributes={kermeta_structure_Class_isAbstract, kermeta_structure_Class_name}
kermeta_structure_Class.methods={kermeta_structure_Class_m__new}

# ParameterizedType class attributes and methods

# structure_Class class attributes and methods

# kermeta_structure_ModelType class attributes and methods
kermeta_structure_ModelType_m__new: Method = Method(name="_new", parameters={}, type=StringType)
kermeta_structure_ModelType.methods={kermeta_structure_ModelType_m__new}

# kermeta_structure_Object class attributes and methods

# structure_Tag class attributes and methods

# kermeta_structure_Model class attributes and methods

# structure_Constraint class attributes and methods

# structure_TypeDefinition class attributes and methods

# kermeta_structure_Operation class attributes and methods
kermeta_structure_Operation_isAbstract: Property = Property(name="isAbstract", type=StringType)
kermeta_structure_Operation.attributes={kermeta_structure_Operation_isAbstract}

# structure_Parameter class attributes and methods

# structure_ClassDefinition class attributes and methods

# structure_TypeVariable class attributes and methods

# kermeta_structure_Property class attributes and methods
kermeta_structure_Property_isReadOnly: Property = Property(name="isReadOnly", type=StringType)
kermeta_structure_Property_default: Property = Property(name="default", type=StringType)
kermeta_structure_Property_isComposite: Property = Property(name="isComposite", type=StringType)
kermeta_structure_Property_isDerived: Property = Property(name="isDerived", type=StringType)
kermeta_structure_Property_isID: Property = Property(name="isID", type=StringType)
kermeta_structure_Property_isGetterAbstract: Property = Property(name="isGetterAbstract", type=StringType)
kermeta_structure_Property_isSetterAbstract: Property = Property(name="isSetterAbstract", type=StringType)
kermeta_structure_Property.attributes={kermeta_structure_Property_isID, kermeta_structure_Property_default, kermeta_structure_Property_isReadOnly, kermeta_structure_Property_isSetterAbstract, kermeta_structure_Property_isDerived, kermeta_structure_Property_isGetterAbstract, kermeta_structure_Property_isComposite}

# kermeta_structure_Type class attributes and methods

# kermeta_structure_TypeContainer class attributes and methods

# kermeta_structure_EnumerationLiteral class attributes and methods

# NamedElement class attributes and methods

# structure_Enumeration class attributes and methods

# kermeta_structure_TypeVariableBinding class attributes and methods

# kermeta_structure_MultiplicityElement class attributes and methods
kermeta_structure_MultiplicityElement_isOrdered: Property = Property(name="isOrdered", type=StringType)
kermeta_structure_MultiplicityElement_isUnique: Property = Property(name="isUnique", type=StringType)
kermeta_structure_MultiplicityElement_lower: Property = Property(name="lower", type=StringType)
kermeta_structure_MultiplicityElement_upper: Property = Property(name="upper", type=StringType)
kermeta_structure_MultiplicityElement.attributes={kermeta_structure_MultiplicityElement_upper, kermeta_structure_MultiplicityElement_isUnique, kermeta_structure_MultiplicityElement_isOrdered, kermeta_structure_MultiplicityElement_lower}

# TypedElement class attributes and methods

# kermeta_structure_TypeDefinition class attributes and methods
kermeta_structure_TypeDefinition_isAspect: Property = Property(name="isAspect", type=StringType)
kermeta_structure_TypeDefinition.attributes={kermeta_structure_TypeDefinition_isAspect}

# structure_Package class attributes and methods

# kermeta_structure_DataType class attributes and methods

# kermeta_structure_Enumeration class attributes and methods

# DataType class attributes and methods

# kermeta_structure_NamedElement class attributes and methods
kermeta_structure_NamedElement_name: Property = Property(name="name", type=StringType)
kermeta_structure_NamedElement.attributes={kermeta_structure_NamedElement_name}

# kermeta_structure_Package class attributes and methods
kermeta_structure_Package_uri: Property = Property(name="uri", type=StringType)
kermeta_structure_Package.attributes={kermeta_structure_Package_uri}

# structure_NamedElement class attributes and methods

# structure_TypeDefinitionContainer class attributes and methods

# kermeta_structure_Parameter class attributes and methods

# kermeta_structure_PrimitiveType class attributes and methods

# structure_DataType class attributes and methods

# kermeta_structure_TypedElement class attributes and methods

# kermeta_structure_Tag class attributes and methods
kermeta_structure_Tag_name: Property = Property(name="name", type=StringType)
kermeta_structure_Tag_value: Property = Property(name="value", type=StringType)
kermeta_structure_Tag.attributes={kermeta_structure_Tag_name, kermeta_structure_Tag_value}

# kermeta_structure_Constraint class attributes and methods
kermeta_structure_Constraint_stereotype: Property = Property(name="stereotype", type=StringType)
kermeta_structure_Constraint_language: Property = Property(name="language", type=StringType)
kermeta_structure_Constraint.attributes={kermeta_structure_Constraint_language, kermeta_structure_Constraint_stereotype}

# kermeta_structure_ClassDefinition class attributes and methods
kermeta_structure_ClassDefinition_isAbstract: Property = Property(name="isAbstract", type=StringType)
kermeta_structure_ClassDefinition.attributes={kermeta_structure_ClassDefinition_isAbstract}

# structure_GenericTypeDefinition class attributes and methods

# kermeta_structure_ModelingUnit class attributes and methods

# structure_Require class attributes and methods

# structure_Using class attributes and methods

# structure_ModelingUnit class attributes and methods

# structure_Filter class attributes and methods

# kermeta_structure_Require class attributes and methods
kermeta_structure_Require_uri: Property = Property(name="uri", type=StringType)
kermeta_structure_Require.attributes={kermeta_structure_Require_uri}

# kermeta_structure_Using class attributes and methods
kermeta_structure_Using_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
kermeta_structure_Using.attributes={kermeta_structure_Using_qualifiedName}

# kermeta_structure_Filter class attributes and methods
kermeta_structure_Filter_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
kermeta_structure_Filter.attributes={kermeta_structure_Filter_qualifiedName}

# kermeta_structure_GenericTypeDefinition class attributes and methods

# TypeDefinition class attributes and methods

# kermeta_structure_ParameterizedType class attributes and methods

# Type class attributes and methods

# structure_TypeVariableBinding class attributes and methods

# kermeta_structure_TypeVariable class attributes and methods

# kermeta_structure_ObjectTypeVariable class attributes and methods

# TypeVariable class attributes and methods

# kermeta_structure_ModelTypeVariable class attributes and methods

# structure_VirtualType class attributes and methods

# kermeta_structure_VirtualType class attributes and methods

# ObjectTypeVariable class attributes and methods

# structure_ModelTypeVariable class attributes and methods

# kermeta_structure_ProductType class attributes and methods

# kermeta_structure_FunctionType class attributes and methods

# kermeta_structure_VoidType class attributes and methods

# kermeta_structure_TypeDefinitionContainer class attributes and methods

# Relationships
staticType3: BinaryAssociation = BinaryAssociation(
    name="staticType3",
    ends={
        Property(name="structure_Type", type=kermeta_behavior_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_behavior_Expression", type=structure_Type, multiplicity=Multiplicity(0, 1))
    }
)
target0: BinaryAssociation = BinaryAssociation(
    name="target0",
    ends={
        Property(name="behavior_CallExpression", type=kermeta_behavior_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_behavior_Assignment", type=behavior_CallExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value1: BinaryAssociation = BinaryAssociation(
    name="value1",
    ends={
        Property(name="behavior_Expression", type=kermeta_behavior_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_behavior_Assignment2", type=behavior_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters4: BinaryAssociation = BinaryAssociation(
    name="parameters4",
    ends={
        Property(name="behavior_Expression5", type=kermeta_behavior_CallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_behavior_CallExpression", type=behavior_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
staticTypeVariableBindings6: BinaryAssociation = BinaryAssociation(
    name="staticTypeVariableBindings6",
    ends={
        Property(name="structure_Type8", type=kermeta_behavior_CallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_behavior_CallExpression7", type=structure_Type, multiplicity=Multiplicity(0, 9999))
    }
)
statement9: BinaryAssociation = BinaryAssociation(
    name="statement9",
    ends={
        Property(name="behavior_Expression10", type=kermeta_behavior_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_behavior_Block", type=behavior_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
staticOperation17: BinaryAssociation = BinaryAssociation(
    name="staticOperation17",
    ends={
        Property(name="structure_Operation", type=kermeta_behavior_CallFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_behavior_CallFeature18", type=structure_Operation, multiplicity=Multiplicity(0, 1))
    }
)
rescueBlock11: BinaryAssociation = BinaryAssociation(
    name="rescueBlock11",
    ends={
        Property(name="behavior_Rescue", type=kermeta_behavior_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_behavior_Block12", type=behavior_Rescue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target13: BinaryAssociation = BinaryAssociation(
    name="target13",
    ends={
        Property(name="behavior_Expression14", type=kermeta_behavior_CallFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_behavior_CallFeature", type=behavior_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
staticProperty15: BinaryAssociation = BinaryAssociation(
    name="staticProperty15",
    ends={
        Property(name="structure_Property", type=kermeta_behavior_CallFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_behavior_CallFeature16", type=structure_Property, multiplicity=Multiplicity(0, 1))
    }
)
staticEnumLiteral19: BinaryAssociation = BinaryAssociation(
    name="staticEnumLiteral19",
    ends={
        Property(name="structure_EnumerationLiteral", type=kermeta_behavior_CallFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_behavior_CallFeature20", type=structure_EnumerationLiteral, multiplicity=Multiplicity(0, 1))
    }
)
thenBody21: BinaryAssociation = BinaryAssociation(
    name="thenBody21",
    ends={
        Property(name="behavior_Expression22", type=kermeta_behavior_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_behavior_Conditional", type=behavior_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseBody23: BinaryAssociation = BinaryAssociation(
    name="elseBody23",
    ends={
        Property(name="behavior_Expression25", type=kermeta_behavior_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_behavior_Conditional24", type=behavior_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition26: BinaryAssociation = BinaryAssociation(
    name="condition26",
    ends={
        Property(name="behavior_Expression28", type=kermeta_behavior_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_behavior_Conditional27", type=behavior_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression29: BinaryAssociation = BinaryAssociation(
    name="expression29",
    ends={
        Property(name="behavior_Expression30", type=kermeta_behavior_Raise, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_behavior_Raise", type=behavior_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body31: BinaryAssociation = BinaryAssociation(
    name="body31",
    ends={
        Property(name="behavior_Expression32", type=kermeta_behavior_Rescue, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_behavior_Rescue", type=behavior_Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
exceptionType33: BinaryAssociation = BinaryAssociation(
    name="exceptionType33",
    ends={
        Property(name="behavior_TypeReference", type=kermeta_behavior_Rescue, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_behavior_Rescue34", type=behavior_TypeReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters35: BinaryAssociation = BinaryAssociation(
    name="parameters35",
    ends={
        Property(name="behavior_Expression36", type=kermeta_behavior_JavaStaticCall, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_behavior_JavaStaticCall", type=behavior_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type41: BinaryAssociation = BinaryAssociation(
    name="type41",
    ends={
        Property(name="behavior_TypeReference42", type=kermeta_behavior_LambdaParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_behavior_LambdaParameter", type=behavior_TypeReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters37: BinaryAssociation = BinaryAssociation(
    name="parameters37",
    ends={
        Property(name="behavior_LambdaParameter", type=kermeta_behavior_LambdaExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_behavior_LambdaExpression", type=behavior_LambdaParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body38: BinaryAssociation = BinaryAssociation(
    name="body38",
    ends={
        Property(name="behavior_Expression40", type=kermeta_behavior_LambdaExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_behavior_LambdaExpression39", type=behavior_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeref43: BinaryAssociation = BinaryAssociation(
    name="typeref43",
    ends={
        Property(name="behavior_TypeReference44", type=kermeta_behavior_TypeLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_behavior_TypeLiteral", type=behavior_TypeReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialization45: BinaryAssociation = BinaryAssociation(
    name="initialization45",
    ends={
        Property(name="behavior_Expression46", type=kermeta_behavior_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_behavior_Loop", type=behavior_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body47: BinaryAssociation = BinaryAssociation(
    name="body47",
    ends={
        Property(name="behavior_Expression49", type=kermeta_behavior_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_behavior_Loop48", type=behavior_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stopCondition50: BinaryAssociation = BinaryAssociation(
    name="stopCondition50",
    ends={
        Property(name="behavior_Expression52", type=kermeta_behavior_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_behavior_Loop51", type=behavior_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialization53: BinaryAssociation = BinaryAssociation(
    name="initialization53",
    ends={
        Property(name="behavior_Expression54", type=kermeta_behavior_VariableDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_behavior_VariableDecl", type=behavior_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
superClass63: BinaryAssociation = BinaryAssociation(
    name="superClass63",
    ends={
        Property(name="structure_Class", type=kermeta_structure_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_structure_Class64", type=structure_Class, multiplicity=Multiplicity(0, 9999))
    }
)
type55: BinaryAssociation = BinaryAssociation(
    name="type55",
    ends={
        Property(name="behavior_TypeReference57", type=kermeta_behavior_VariableDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_behavior_VariableDecl56", type=behavior_TypeReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedAttribute58: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute58",
    ends={
        Property(name="structure_Property59", type=kermeta_structure_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_structure_Class", type=structure_Property, multiplicity=Multiplicity(0, 9999))
    }
)
ownedOperation60: BinaryAssociation = BinaryAssociation(
    name="ownedOperation60",
    ends={
        Property(name="structure_Operation62", type=kermeta_structure_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_structure_Class61", type=structure_Operation, multiplicity=Multiplicity(0, 9999))
    }
)
tag65: BinaryAssociation = BinaryAssociation(
    name="tag65",
    ends={
        Property(name="language", type=kermeta_structure_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="structure", type=structure_Tag, multiplicity=Multiplicity(0, 9999))
    }
)
ownedTags66: BinaryAssociation = BinaryAssociation(
    name="ownedTags66",
    ends={
        Property(name="structure_Tag", type=kermeta_structure_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_structure_Object", type=structure_Tag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contents67: BinaryAssociation = BinaryAssociation(
    name="contents67",
    ends={
        Property(name="structure_Object", type=kermeta_structure_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_structure_Model", type=structure_Object, multiplicity=Multiplicity(0, 9999))
    }
)
includedTypeDefinition68: BinaryAssociation = BinaryAssociation(
    name="includedTypeDefinition68",
    ends={
        Property(name="structure_TypeDefinition", type=kermeta_structure_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_structure_ModelType", type=structure_TypeDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
raisedException69: BinaryAssociation = BinaryAssociation(
    name="raisedException69",
    ends={
        Property(name="structure_Type70", type=kermeta_structure_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_structure_Operation", type=structure_Type, multiplicity=Multiplicity(0, 9999))
    }
)
ownedParameter71: BinaryAssociation = BinaryAssociation(
    name="ownedParameter71",
    ends={
        Property(name="language73", type=kermeta_structure_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="structure72", type=structure_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pre74: BinaryAssociation = BinaryAssociation(
    name="pre74",
    ends={
        Property(name="language76", type=kermeta_structure_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="structure75", type=structure_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
post77: BinaryAssociation = BinaryAssociation(
    name="post77",
    ends={
        Property(name="language79", type=kermeta_structure_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="structure78", type=structure_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body80: BinaryAssociation = BinaryAssociation(
    name="body80",
    ends={
        Property(name="behavior_Expression82", type=kermeta_structure_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_structure_Operation81", type=behavior_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
superOperation83: BinaryAssociation = BinaryAssociation(
    name="superOperation83",
    ends={
        Property(name="structure_Operation85", type=kermeta_structure_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_structure_Operation84", type=structure_Operation, multiplicity=Multiplicity(0, 1))
    }
)
owningClass86: BinaryAssociation = BinaryAssociation(
    name="owningClass86",
    ends={
        Property(name="language88", type=kermeta_structure_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="structure87", type=structure_ClassDefinition, multiplicity=Multiplicity(0, 1))
    }
)
typeParameter89: BinaryAssociation = BinaryAssociation(
    name="typeParameter89",
    ends={
        Property(name="structure_TypeVariable", type=kermeta_structure_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_structure_Operation90", type=structure_TypeVariable, multiplicity=Multiplicity(0, 9999))
    }
)
getterBody93: BinaryAssociation = BinaryAssociation(
    name="getterBody93",
    ends={
        Property(name="behavior_Expression95", type=kermeta_structure_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_structure_Property94", type=behavior_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opposite91: BinaryAssociation = BinaryAssociation(
    name="opposite91",
    ends={
        Property(name="structure_Property92", type=kermeta_structure_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_structure_Property", type=structure_Property, multiplicity=Multiplicity(0, 1))
    }
)
typeContainer102: BinaryAssociation = BinaryAssociation(
    name="typeContainer102",
    ends={
        Property(name="language104", type=kermeta_structure_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="structure103", type=structure_TypeContainer, multiplicity=Multiplicity(0, 1))
    }
)
setterBody96: BinaryAssociation = BinaryAssociation(
    name="setterBody96",
    ends={
        Property(name="behavior_Expression98", type=kermeta_structure_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_structure_Property97", type=behavior_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owningClass99: BinaryAssociation = BinaryAssociation(
    name="owningClass99",
    ends={
        Property(name="language101", type=kermeta_structure_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="structure100", type=structure_ClassDefinition, multiplicity=Multiplicity(0, 1))
    }
)
variable111: BinaryAssociation = BinaryAssociation(
    name="variable111",
    ends={
        Property(name="structure_TypeVariable112", type=kermeta_structure_TypeVariableBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_structure_TypeVariableBinding", type=structure_TypeVariable, multiplicity=Multiplicity(1, 1))
    }
)
containedType105: BinaryAssociation = BinaryAssociation(
    name="containedType105",
    ends={
        Property(name="language107", type=kermeta_structure_TypeContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="structure106", type=structure_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumeration108: BinaryAssociation = BinaryAssociation(
    name="enumeration108",
    ends={
        Property(name="language110", type=kermeta_structure_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="structure109", type=structure_Enumeration, multiplicity=Multiplicity(0, 1))
    }
)
type113: BinaryAssociation = BinaryAssociation(
    name="type113",
    ends={
        Property(name="structure_Type115", type=kermeta_structure_TypeVariableBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_structure_TypeVariableBinding114", type=structure_Type, multiplicity=Multiplicity(1, 1))
    }
)
nestedPackage119: BinaryAssociation = BinaryAssociation(
    name="nestedPackage119",
    ends={
        Property(name="language121", type=kermeta_structure_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="structure120", type=structure_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedLiteral116: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral116",
    ends={
        Property(name="language118", type=kermeta_structure_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="structure117", type=structure_EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestingPackage122: BinaryAssociation = BinaryAssociation(
    name="nestingPackage122",
    ends={
        Property(name="language124", type=kermeta_structure_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="structure123", type=structure_Package, multiplicity=Multiplicity(0, 1))
    }
)
operation125: BinaryAssociation = BinaryAssociation(
    name="operation125",
    ends={
        Property(name="language127", type=kermeta_structure_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="structure126", type=structure_Operation, multiplicity=Multiplicity(0, 1))
    }
)
instanceType128: BinaryAssociation = BinaryAssociation(
    name="instanceType128",
    ends={
        Property(name="structure_Type129", type=kermeta_structure_PrimitiveType, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_structure_PrimitiveType", type=structure_Type, multiplicity=Multiplicity(0, 1))
    }
)
type130: BinaryAssociation = BinaryAssociation(
    name="type130",
    ends={
        Property(name="structure_Type131", type=kermeta_structure_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_structure_TypedElement", type=structure_Type, multiplicity=Multiplicity(0, 1))
    }
)
object132: BinaryAssociation = BinaryAssociation(
    name="object132",
    ends={
        Property(name="language134", type=kermeta_structure_Tag, multiplicity=Multiplicity(1, 1)),
        Property(name="structure133", type=structure_Object, multiplicity=Multiplicity(1, 9999))
    }
)
body135: BinaryAssociation = BinaryAssociation(
    name="body135",
    ends={
        Property(name="behavior_Expression136", type=kermeta_structure_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_structure_Constraint", type=behavior_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
invOwner137: BinaryAssociation = BinaryAssociation(
    name="invOwner137",
    ends={
        Property(name="language139", type=kermeta_structure_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="structure138", type=structure_ClassDefinition, multiplicity=Multiplicity(0, 1))
    }
)
preOwner140: BinaryAssociation = BinaryAssociation(
    name="preOwner140",
    ends={
        Property(name="language142", type=kermeta_structure_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="structure141", type=structure_Operation, multiplicity=Multiplicity(0, 1))
    }
)
postOwner143: BinaryAssociation = BinaryAssociation(
    name="postOwner143",
    ends={
        Property(name="language145", type=kermeta_structure_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="structure144", type=structure_Operation, multiplicity=Multiplicity(0, 1))
    }
)
inv146: BinaryAssociation = BinaryAssociation(
    name="inv146",
    ends={
        Property(name="language148", type=kermeta_structure_ClassDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="structure147", type=structure_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute149: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute149",
    ends={
        Property(name="language151", type=kermeta_structure_ClassDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="structure150", type=structure_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation152: BinaryAssociation = BinaryAssociation(
    name="ownedOperation152",
    ends={
        Property(name="language154", type=kermeta_structure_ClassDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="structure153", type=structure_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superType155: BinaryAssociation = BinaryAssociation(
    name="superType155",
    ends={
        Property(name="structure_Type156", type=kermeta_structure_ClassDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_structure_ClassDefinition", type=structure_Type, multiplicity=Multiplicity(0, 9999))
    }
)
packages157: BinaryAssociation = BinaryAssociation(
    name="packages157",
    ends={
        Property(name="structure_Package", type=kermeta_structure_ModelingUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_structure_ModelingUnit", type=structure_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requires158: BinaryAssociation = BinaryAssociation(
    name="requires158",
    ends={
        Property(name="structure_Require", type=kermeta_structure_ModelingUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_structure_ModelingUnit159", type=structure_Require, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usings160: BinaryAssociation = BinaryAssociation(
    name="usings160",
    ends={
        Property(name="structure_Using", type=kermeta_structure_ModelingUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_structure_ModelingUnit161", type=structure_Using, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referencedModelingUnits162: BinaryAssociation = BinaryAssociation(
    name="referencedModelingUnits162",
    ends={
        Property(name="structure_ModelingUnit", type=kermeta_structure_ModelingUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_structure_ModelingUnit163", type=structure_ModelingUnit, multiplicity=Multiplicity(0, 9999))
    }
)
includeFilters164: BinaryAssociation = BinaryAssociation(
    name="includeFilters164",
    ends={
        Property(name="structure_Filter", type=kermeta_structure_ModelingUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_structure_ModelingUnit165", type=structure_Filter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
excludeFilters166: BinaryAssociation = BinaryAssociation(
    name="excludeFilters166",
    ends={
        Property(name="structure_Filter168", type=kermeta_structure_ModelingUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_structure_ModelingUnit167", type=structure_Filter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameter169: BinaryAssociation = BinaryAssociation(
    name="typeParameter169",
    ends={
        Property(name="structure_TypeVariable170", type=kermeta_structure_GenericTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_structure_GenericTypeDefinition", type=structure_TypeVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
virtualTypeBinding171: BinaryAssociation = BinaryAssociation(
    name="virtualTypeBinding171",
    ends={
        Property(name="structure_TypeVariableBinding", type=kermeta_structure_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_structure_ParameterizedType", type=structure_TypeVariableBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParamBinding172: BinaryAssociation = BinaryAssociation(
    name="typeParamBinding172",
    ends={
        Property(name="structure_TypeVariableBinding174", type=kermeta_structure_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_structure_ParameterizedType173", type=structure_TypeVariableBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeDefinition175: BinaryAssociation = BinaryAssociation(
    name="typeDefinition175",
    ends={
        Property(name="structure_GenericTypeDefinition", type=kermeta_structure_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_structure_ParameterizedType176", type=structure_GenericTypeDefinition, multiplicity=Multiplicity(1, 1))
    }
)
supertype177: BinaryAssociation = BinaryAssociation(
    name="supertype177",
    ends={
        Property(name="structure_Type178", type=kermeta_structure_TypeVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_structure_TypeVariable", type=structure_Type, multiplicity=Multiplicity(0, 1))
    }
)
virtualType179: BinaryAssociation = BinaryAssociation(
    name="virtualType179",
    ends={
        Property(name="language181", type=kermeta_structure_ModelTypeVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="structure180", type=structure_VirtualType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classDefinition182: BinaryAssociation = BinaryAssociation(
    name="classDefinition182",
    ends={
        Property(name="structure_ClassDefinition", type=kermeta_structure_VirtualType, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_structure_VirtualType", type=structure_ClassDefinition, multiplicity=Multiplicity(1, 1))
    }
)
modelType183: BinaryAssociation = BinaryAssociation(
    name="modelType183",
    ends={
        Property(name="language185", type=kermeta_structure_VirtualType, multiplicity=Multiplicity(1, 1)),
        Property(name="structure184", type=structure_ModelTypeVariable, multiplicity=Multiplicity(1, 1))
    }
)
typeParamBinding186: BinaryAssociation = BinaryAssociation(
    name="typeParamBinding186",
    ends={
        Property(name="structure_TypeVariableBinding188", type=kermeta_structure_VirtualType, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_structure_VirtualType187", type=structure_TypeVariableBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type189: BinaryAssociation = BinaryAssociation(
    name="type189",
    ends={
        Property(name="structure_Type190", type=kermeta_structure_ProductType, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_structure_ProductType", type=structure_Type, multiplicity=Multiplicity(0, 9999))
    }
)
left191: BinaryAssociation = BinaryAssociation(
    name="left191",
    ends={
        Property(name="structure_Type192", type=kermeta_structure_FunctionType, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_structure_FunctionType", type=structure_Type, multiplicity=Multiplicity(0, 1))
    }
)
right193: BinaryAssociation = BinaryAssociation(
    name="right193",
    ends={
        Property(name="structure_Type195", type=kermeta_structure_FunctionType, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_structure_FunctionType194", type=structure_Type, multiplicity=Multiplicity(0, 1))
    }
)
ownedTypeDefinition196: BinaryAssociation = BinaryAssociation(
    name="ownedTypeDefinition196",
    ends={
        Property(name="structure_TypeDefinition197", type=kermeta_structure_TypeDefinitionContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="kermeta_structure_TypeDefinitionContainer", type=structure_TypeDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_kermeta_behavior_Expression_structure_Object = Generalization(general=structure_Object, specific=kermeta_behavior_Expression)
gen_kermeta_behavior_Expression_structure_TypeContainer = Generalization(general=structure_TypeContainer, specific=kermeta_behavior_Expression)
gen_kermeta_behavior_Assignment_Expression = Generalization(general=Expression, specific=kermeta_behavior_Assignment)
gen_kermeta_behavior_CallExpression_Expression = Generalization(general=Expression, specific=kermeta_behavior_CallExpression)
gen_kermeta_behavior_Block_Expression = Generalization(general=Expression, specific=kermeta_behavior_Block)
gen_kermeta_behavior_CallVariable_CallExpression = Generalization(general=CallExpression, specific=kermeta_behavior_CallVariable)
gen_kermeta_behavior_CallFeature_CallExpression = Generalization(general=CallExpression, specific=kermeta_behavior_CallFeature)
gen_kermeta_behavior_Raise_Expression = Generalization(general=Expression, specific=kermeta_behavior_Raise)
gen_kermeta_behavior_CallSuperOperation_CallExpression = Generalization(general=CallExpression, specific=kermeta_behavior_CallSuperOperation)
gen_kermeta_behavior_CallResult_CallVariable = Generalization(general=CallVariable, specific=kermeta_behavior_CallResult)
gen_kermeta_behavior_CallValue_CallExpression = Generalization(general=CallExpression, specific=kermeta_behavior_CallValue)
gen_kermeta_behavior_Conditional_Expression = Generalization(general=Expression, specific=kermeta_behavior_Conditional)
gen_kermeta_behavior_Rescue_Object = Generalization(general=Object, specific=kermeta_behavior_Rescue)
gen_kermeta_behavior_TypeReference_MultiplicityElement = Generalization(general=MultiplicityElement, specific=kermeta_behavior_TypeReference)
gen_kermeta_behavior_Literal_Expression = Generalization(general=Expression, specific=kermeta_behavior_Literal)
gen_kermeta_behavior_LambdaExpression_Expression = Generalization(general=Expression, specific=kermeta_behavior_LambdaExpression)
gen_kermeta_behavior_EmptyExpression_Expression = Generalization(general=Expression, specific=kermeta_behavior_EmptyExpression)
gen_kermeta_behavior_JavaStaticCall_Expression = Generalization(general=Expression, specific=kermeta_behavior_JavaStaticCall)
gen_kermeta_behavior_LambdaParameter_Object = Generalization(general=Object, specific=kermeta_behavior_LambdaParameter)
gen_kermeta_behavior_IntegerLiteral_Literal = Generalization(general=Literal, specific=kermeta_behavior_IntegerLiteral)
gen_kermeta_behavior_StringLiteral_Literal = Generalization(general=Literal, specific=kermeta_behavior_StringLiteral)
gen_kermeta_behavior_BooleanLiteral_Literal = Generalization(general=Literal, specific=kermeta_behavior_BooleanLiteral)
gen_kermeta_behavior_TypeLiteral_Literal = Generalization(general=Literal, specific=kermeta_behavior_TypeLiteral)
gen_kermeta_behavior_VoidLiteral_Literal = Generalization(general=Literal, specific=kermeta_behavior_VoidLiteral)
gen_kermeta_behavior_Loop_Expression = Generalization(general=Expression, specific=kermeta_behavior_Loop)
gen_kermeta_behavior_SelfExpression_Expression = Generalization(general=Expression, specific=kermeta_behavior_SelfExpression)
gen_kermeta_behavior_VariableDecl_Expression = Generalization(general=Expression, specific=kermeta_behavior_VariableDecl)
gen_kermeta_structure_Class_ParameterizedType = Generalization(general=ParameterizedType, specific=kermeta_structure_Class)
gen_kermeta_structure_Model_Object = Generalization(general=Object, specific=kermeta_structure_Model)
gen_kermeta_structure_ModelType_structure_Type = Generalization(general=structure_Type, specific=kermeta_structure_ModelType)
gen_kermeta_structure_ModelType_structure_TypeDefinition = Generalization(general=structure_TypeDefinition, specific=kermeta_structure_ModelType)
gen_kermeta_structure_Operation_MultiplicityElement = Generalization(general=MultiplicityElement, specific=kermeta_structure_Operation)
gen_kermeta_structure_Property_MultiplicityElement = Generalization(general=MultiplicityElement, specific=kermeta_structure_Property)
gen_kermeta_structure_Type_Object = Generalization(general=Object, specific=kermeta_structure_Type)
gen_kermeta_structure_TypeContainer_Object = Generalization(general=Object, specific=kermeta_structure_TypeContainer)
gen_kermeta_structure_EnumerationLiteral_NamedElement = Generalization(general=NamedElement, specific=kermeta_structure_EnumerationLiteral)
gen_kermeta_structure_TypeVariableBinding_structure_TypeContainer = Generalization(general=structure_TypeContainer, specific=kermeta_structure_TypeVariableBinding)
gen_kermeta_structure_TypeVariableBinding_structure_Object = Generalization(general=structure_Object, specific=kermeta_structure_TypeVariableBinding)
gen_kermeta_structure_MultiplicityElement_TypedElement = Generalization(general=TypedElement, specific=kermeta_structure_MultiplicityElement)
gen_kermeta_structure_TypeDefinition_NamedElement = Generalization(general=NamedElement, specific=kermeta_structure_TypeDefinition)
gen_kermeta_structure_DataType_structure_Type = Generalization(general=structure_Type, specific=kermeta_structure_DataType)
gen_kermeta_structure_DataType_structure_TypeDefinition = Generalization(general=structure_TypeDefinition, specific=kermeta_structure_DataType)
gen_kermeta_structure_Enumeration_DataType = Generalization(general=DataType, specific=kermeta_structure_Enumeration)
gen_kermeta_structure_NamedElement_Object = Generalization(general=Object, specific=kermeta_structure_NamedElement)
gen_kermeta_structure_Package_structure_NamedElement = Generalization(general=structure_NamedElement, specific=kermeta_structure_Package)
gen_kermeta_structure_Package_structure_TypeDefinitionContainer = Generalization(general=structure_TypeDefinitionContainer, specific=kermeta_structure_Package)
gen_kermeta_structure_Parameter_MultiplicityElement = Generalization(general=MultiplicityElement, specific=kermeta_structure_Parameter)
gen_kermeta_structure_PrimitiveType_structure_DataType = Generalization(general=structure_DataType, specific=kermeta_structure_PrimitiveType)
gen_kermeta_structure_PrimitiveType_structure_TypeContainer = Generalization(general=structure_TypeContainer, specific=kermeta_structure_PrimitiveType)
gen_kermeta_structure_TypedElement_structure_TypeContainer = Generalization(general=structure_TypeContainer, specific=kermeta_structure_TypedElement)
gen_kermeta_structure_TypedElement_structure_NamedElement = Generalization(general=structure_NamedElement, specific=kermeta_structure_TypedElement)
gen_kermeta_structure_Tag_Object = Generalization(general=Object, specific=kermeta_structure_Tag)
gen_kermeta_structure_Constraint_NamedElement = Generalization(general=NamedElement, specific=kermeta_structure_Constraint)
gen_kermeta_structure_ClassDefinition_structure_GenericTypeDefinition = Generalization(general=structure_GenericTypeDefinition, specific=kermeta_structure_ClassDefinition)
gen_kermeta_structure_ClassDefinition_structure_TypeContainer = Generalization(general=structure_TypeContainer, specific=kermeta_structure_ClassDefinition)
gen_kermeta_structure_ModelingUnit_Object = Generalization(general=Object, specific=kermeta_structure_ModelingUnit)
gen_kermeta_structure_Require_Object = Generalization(general=Object, specific=kermeta_structure_Require)
gen_kermeta_structure_Using_Object = Generalization(general=Object, specific=kermeta_structure_Using)
gen_kermeta_structure_Filter_Object = Generalization(general=Object, specific=kermeta_structure_Filter)
gen_kermeta_structure_GenericTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=kermeta_structure_GenericTypeDefinition)
gen_kermeta_structure_ParameterizedType_Type = Generalization(general=Type, specific=kermeta_structure_ParameterizedType)
gen_kermeta_structure_TypeVariable_structure_TypeContainer = Generalization(general=structure_TypeContainer, specific=kermeta_structure_TypeVariable)
gen_kermeta_structure_TypeVariable_structure_Type = Generalization(general=structure_Type, specific=kermeta_structure_TypeVariable)
gen_kermeta_structure_TypeVariable_structure_NamedElement = Generalization(general=structure_NamedElement, specific=kermeta_structure_TypeVariable)
gen_kermeta_structure_ObjectTypeVariable_TypeVariable = Generalization(general=TypeVariable, specific=kermeta_structure_ObjectTypeVariable)
gen_kermeta_structure_ModelTypeVariable_TypeVariable = Generalization(general=TypeVariable, specific=kermeta_structure_ModelTypeVariable)
gen_kermeta_structure_VirtualType_ObjectTypeVariable = Generalization(general=ObjectTypeVariable, specific=kermeta_structure_VirtualType)
gen_kermeta_structure_ProductType_structure_TypeContainer = Generalization(general=structure_TypeContainer, specific=kermeta_structure_ProductType)
gen_kermeta_structure_ProductType_structure_Type = Generalization(general=structure_Type, specific=kermeta_structure_ProductType)
gen_kermeta_structure_FunctionType_structure_TypeContainer = Generalization(general=structure_TypeContainer, specific=kermeta_structure_FunctionType)
gen_kermeta_structure_FunctionType_structure_Type = Generalization(general=structure_Type, specific=kermeta_structure_FunctionType)
gen_kermeta_structure_VoidType_Type = Generalization(general=Type, specific=kermeta_structure_VoidType)
gen_kermeta_structure_TypeDefinitionContainer_NamedElement = Generalization(general=NamedElement, specific=kermeta_structure_TypeDefinitionContainer)

# Domain Model
domain_model = DomainModel(
    name="kermeta",
    types={kermeta_behavior_Expression, structure_Object, structure_TypeContainer, structure_Type, kermeta_DummyClass, kermeta_language_DummyClass, kermeta_behavior_Assignment, Expression, behavior_CallExpression, behavior_Expression, kermeta_behavior_CallExpression, kermeta_behavior_Block, behavior_Rescue, structure_Operation, kermeta_behavior_CallVariable, CallExpression, kermeta_behavior_CallFeature, structure_Property, kermeta_behavior_Raise, structure_EnumerationLiteral, kermeta_behavior_CallSuperOperation, kermeta_behavior_CallResult, CallVariable, kermeta_behavior_CallValue, kermeta_behavior_Conditional, kermeta_behavior_EmptyExpression, kermeta_behavior_Rescue, Object, behavior_TypeReference, kermeta_behavior_TypeReference, MultiplicityElement, kermeta_behavior_Literal, kermeta_behavior_LambdaExpression, kermeta_behavior_JavaStaticCall, behavior_LambdaParameter, kermeta_behavior_LambdaParameter, kermeta_behavior_IntegerLiteral, Literal, kermeta_behavior_StringLiteral, kermeta_behavior_BooleanLiteral, kermeta_behavior_TypeLiteral, kermeta_behavior_VoidLiteral, kermeta_behavior_Loop, kermeta_behavior_SelfExpression, kermeta_behavior_VariableDecl, kermeta_structure_Class, ParameterizedType, structure_Class, kermeta_structure_ModelType, kermeta_structure_Object, structure_Tag, kermeta_structure_Model, structure_Constraint, structure_TypeDefinition, kermeta_structure_Operation, structure_Parameter, structure_ClassDefinition, structure_TypeVariable, kermeta_structure_Property, kermeta_structure_Type, kermeta_structure_TypeContainer, kermeta_structure_EnumerationLiteral, NamedElement, structure_Enumeration, kermeta_structure_TypeVariableBinding, kermeta_structure_MultiplicityElement, TypedElement, kermeta_structure_TypeDefinition, structure_Package, kermeta_structure_DataType, kermeta_structure_Enumeration, DataType, kermeta_structure_NamedElement, kermeta_structure_Package, structure_NamedElement, structure_TypeDefinitionContainer, kermeta_structure_Parameter, kermeta_structure_PrimitiveType, structure_DataType, kermeta_structure_TypedElement, kermeta_structure_Tag, kermeta_structure_Constraint, kermeta_structure_ClassDefinition, structure_GenericTypeDefinition, kermeta_structure_ModelingUnit, structure_Require, structure_Using, structure_ModelingUnit, structure_Filter, kermeta_structure_Require, kermeta_structure_Using, kermeta_structure_Filter, kermeta_structure_GenericTypeDefinition, TypeDefinition, kermeta_structure_ParameterizedType, Type, structure_TypeVariableBinding, kermeta_structure_TypeVariable, kermeta_structure_ObjectTypeVariable, TypeVariable, kermeta_structure_ModelTypeVariable, structure_VirtualType, kermeta_structure_VirtualType, ObjectTypeVariable, structure_ModelTypeVariable, kermeta_structure_ProductType, kermeta_structure_FunctionType, kermeta_structure_VoidType, kermeta_structure_TypeDefinitionContainer, ConstraintLanguage, ConstraintType},
    associations={staticType3, target0, value1, parameters4, staticTypeVariableBindings6, statement9, staticOperation17, rescueBlock11, target13, staticProperty15, staticEnumLiteral19, thenBody21, elseBody23, condition26, expression29, body31, exceptionType33, parameters35, type41, parameters37, body38, typeref43, initialization45, body47, stopCondition50, initialization53, superClass63, type55, ownedAttribute58, ownedOperation60, tag65, ownedTags66, contents67, includedTypeDefinition68, raisedException69, ownedParameter71, pre74, post77, body80, superOperation83, owningClass86, typeParameter89, getterBody93, opposite91, typeContainer102, setterBody96, owningClass99, variable111, containedType105, enumeration108, type113, nestedPackage119, ownedLiteral116, nestingPackage122, operation125, instanceType128, type130, object132, body135, invOwner137, preOwner140, postOwner143, inv146, ownedAttribute149, ownedOperation152, superType155, packages157, requires158, usings160, referencedModelingUnits162, includeFilters164, excludeFilters166, typeParameter169, virtualTypeBinding171, typeParamBinding172, typeDefinition175, supertype177, virtualType179, classDefinition182, modelType183, typeParamBinding186, type189, left191, right193, ownedTypeDefinition196},
    generalizations={gen_kermeta_behavior_Expression_structure_Object, gen_kermeta_behavior_Expression_structure_TypeContainer, gen_kermeta_behavior_Assignment_Expression, gen_kermeta_behavior_CallExpression_Expression, gen_kermeta_behavior_Block_Expression, gen_kermeta_behavior_CallVariable_CallExpression, gen_kermeta_behavior_CallFeature_CallExpression, gen_kermeta_behavior_Raise_Expression, gen_kermeta_behavior_CallSuperOperation_CallExpression, gen_kermeta_behavior_CallResult_CallVariable, gen_kermeta_behavior_CallValue_CallExpression, gen_kermeta_behavior_Conditional_Expression, gen_kermeta_behavior_Rescue_Object, gen_kermeta_behavior_TypeReference_MultiplicityElement, gen_kermeta_behavior_Literal_Expression, gen_kermeta_behavior_LambdaExpression_Expression, gen_kermeta_behavior_EmptyExpression_Expression, gen_kermeta_behavior_JavaStaticCall_Expression, gen_kermeta_behavior_LambdaParameter_Object, gen_kermeta_behavior_IntegerLiteral_Literal, gen_kermeta_behavior_StringLiteral_Literal, gen_kermeta_behavior_BooleanLiteral_Literal, gen_kermeta_behavior_TypeLiteral_Literal, gen_kermeta_behavior_VoidLiteral_Literal, gen_kermeta_behavior_Loop_Expression, gen_kermeta_behavior_SelfExpression_Expression, gen_kermeta_behavior_VariableDecl_Expression, gen_kermeta_structure_Class_ParameterizedType, gen_kermeta_structure_Model_Object, gen_kermeta_structure_ModelType_structure_Type, gen_kermeta_structure_ModelType_structure_TypeDefinition, gen_kermeta_structure_Operation_MultiplicityElement, gen_kermeta_structure_Property_MultiplicityElement, gen_kermeta_structure_Type_Object, gen_kermeta_structure_TypeContainer_Object, gen_kermeta_structure_EnumerationLiteral_NamedElement, gen_kermeta_structure_TypeVariableBinding_structure_TypeContainer, gen_kermeta_structure_TypeVariableBinding_structure_Object, gen_kermeta_structure_MultiplicityElement_TypedElement, gen_kermeta_structure_TypeDefinition_NamedElement, gen_kermeta_structure_DataType_structure_Type, gen_kermeta_structure_DataType_structure_TypeDefinition, gen_kermeta_structure_Enumeration_DataType, gen_kermeta_structure_NamedElement_Object, gen_kermeta_structure_Package_structure_NamedElement, gen_kermeta_structure_Package_structure_TypeDefinitionContainer, gen_kermeta_structure_Parameter_MultiplicityElement, gen_kermeta_structure_PrimitiveType_structure_DataType, gen_kermeta_structure_PrimitiveType_structure_TypeContainer, gen_kermeta_structure_TypedElement_structure_TypeContainer, gen_kermeta_structure_TypedElement_structure_NamedElement, gen_kermeta_structure_Tag_Object, gen_kermeta_structure_Constraint_NamedElement, gen_kermeta_structure_ClassDefinition_structure_GenericTypeDefinition, gen_kermeta_structure_ClassDefinition_structure_TypeContainer, gen_kermeta_structure_ModelingUnit_Object, gen_kermeta_structure_Require_Object, gen_kermeta_structure_Using_Object, gen_kermeta_structure_Filter_Object, gen_kermeta_structure_GenericTypeDefinition_TypeDefinition, gen_kermeta_structure_ParameterizedType_Type, gen_kermeta_structure_TypeVariable_structure_TypeContainer, gen_kermeta_structure_TypeVariable_structure_Type, gen_kermeta_structure_TypeVariable_structure_NamedElement, gen_kermeta_structure_ObjectTypeVariable_TypeVariable, gen_kermeta_structure_ModelTypeVariable_TypeVariable, gen_kermeta_structure_VirtualType_ObjectTypeVariable, gen_kermeta_structure_ProductType_structure_TypeContainer, gen_kermeta_structure_ProductType_structure_Type, gen_kermeta_structure_FunctionType_structure_TypeContainer, gen_kermeta_structure_FunctionType_structure_Type, gen_kermeta_structure_VoidType_Type, gen_kermeta_structure_TypeDefinitionContainer_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)