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

EnforcementMode: Enumeration = Enumeration(
    name="EnforcementMode",
    literals={
            EnumerationLiteral(name="Creation"),
			EnumerationLiteral(name="Deletion")
    }
)

SeverityKind: Enumeration = Enumeration(
    name="SeverityKind",
    literals={
            EnumerationLiteral(name="error"),
			EnumerationLiteral(name="warning"),
			EnumerationLiteral(name="fatal")
    }
)

DirectionKind: Enumeration = Enumeration(
    name="DirectionKind",
    literals={
            EnumerationLiteral(name="in"),
			EnumerationLiteral(name="inout"),
			EnumerationLiteral(name="out")
    }
)

ImportKind: Enumeration = Enumeration(
    name="ImportKind",
    literals={
            EnumerationLiteral(name="extension"),
			EnumerationLiteral(name="access")
    }
)

# Classes
Class_ = Class(name="Class")
EMOF_Comment = Class(name="EMOF::Comment")
Element = Class(name="Element")
NamedElement = Class(name="NamedElement")
EMOF_DataType = Class(name="EMOF::DataType")
EMOF_Element = Class(name="EMOF::Element", is_abstract=True)
Object = Class(name="Object")
EMOF_Class = Class(name="EMOF::Class")
Type = Class(name="Type")
Property_ = Class(name="Property")
Operation = Class(name="Operation")
Enumeration_ = Class(name="Enumeration")
EMOF_Extent = Class(name="EMOF::Extent")
EMOF_Factory = Class(name="EMOF::Factory")
Package = Class(name="Package")
Comment = Class(name="Comment")
EMOF_Enumeration = Class(name="EMOF::Enumeration")
DataType = Class(name="DataType")
EnumerationLiteral = Class(name="EnumerationLiteral")
EMOF_EnumerationLiteral = Class(name="EMOF::EnumerationLiteral")
EMOF_Package = Class(name="EMOF::Package")
EMOF_Parameter = Class(name="EMOF::Parameter")
EMOF_MultiplicityElement = Class(name="EMOF::MultiplicityElement", is_abstract=True)
EMOF_NamedElement = Class(name="EMOF::NamedElement", is_abstract=True)
EMOF_Object = Class(name="EMOF::Object")
EMOF_Operation = Class(name="EMOF::Operation")
TypedElement = Class(name="TypedElement")
MultiplicityElement = Class(name="MultiplicityElement")
Parameter_ = Class(name="Parameter")
EMOF_ReflectiveSequence = Class(name="EMOF::ReflectiveSequence")
ReflectiveCollection = Class(name="ReflectiveCollection")
EMOF_Tag = Class(name="EMOF::Tag")
EMOF_PrimitiveType = Class(name="EMOF::PrimitiveType")
EMOF_Property = Class(name="EMOF::Property")
EMOF_ReflectiveCollection = Class(name="EMOF::ReflectiveCollection")
EssentialOCL_BooleanLiteralExp = Class(name="EssentialOCL::BooleanLiteralExp")
PrimitiveLiteralExp = Class(name="PrimitiveLiteralExp")
EssentialOCL_CallExp = Class(name="EssentialOCL::CallExp", is_abstract=True)
OclExpression = Class(name="OclExpression")
EssentialOCL_CollectionItem = Class(name="EssentialOCL::CollectionItem")
CollectionLiteralPart = Class(name="CollectionLiteralPart")
EMOF_Type = Class(name="EMOF::Type", is_abstract=True)
EMOF_TypedElement = Class(name="EMOF::TypedElement", is_abstract=True)
EMOF_URIExtent = Class(name="EMOF::URIExtent")
Extent = Class(name="Extent")
EssentialOCL_AnyType = Class(name="EssentialOCL::AnyType")
EssentialOCL_BagType = Class(name="EssentialOCL::BagType")
CollectionType = Class(name="CollectionType")
EssentialOCL_CollectionType = Class(name="EssentialOCL::CollectionType")
EssentialOCL_CollectionLiteralExp = Class(name="EssentialOCL::CollectionLiteralExp")
LiteralExp = Class(name="LiteralExp")
EssentialOCL_CollectionLiteralPart = Class(name="EssentialOCL::CollectionLiteralPart", is_abstract=True)
CollectionLiteralExp = Class(name="CollectionLiteralExp")
EssentialOCL_CollectionRange = Class(name="EssentialOCL::CollectionRange")
EssentialOCL_FeatureCallExp = Class(name="EssentialOCL::FeatureCallExp", is_abstract=True)
CallExp = Class(name="CallExp")
EssentialOCL_IfExp = Class(name="EssentialOCL::IfExp")
EssentialOCL_EnumLiteralExp = Class(name="EssentialOCL::EnumLiteralExp")
EssentialOCL_ExpressionInOcl = Class(name="EssentialOCL::ExpressionInOcl")
Variable = Class(name="Variable")
EssentialOCL_LoopExp = Class(name="EssentialOCL::LoopExp", is_abstract=True)
EssentialOCL_NavigationCallExp = Class(name="EssentialOCL::NavigationCallExp")
FeatureCallExp = Class(name="FeatureCallExp")
EssentialOCL_NullLiteralExp = Class(name="EssentialOCL::NullLiteralExp")
EssentialOCL_NumericLiteralExp = Class(name="EssentialOCL::NumericLiteralExp", is_abstract=True)
EssentialOCL_OclExpression = Class(name="EssentialOCL::OclExpression", is_abstract=True)
EssentialOCL_OperationCallExp = Class(name="EssentialOCL::OperationCallExp")
EssentialOCL_IntegerLiteralExp = Class(name="EssentialOCL::IntegerLiteralExp")
NumericLiteralExp = Class(name="NumericLiteralExp")
EssentialOCL_InvalidLiteralExp = Class(name="EssentialOCL::InvalidLiteralExp")
EssentialOCL_InvalidType = Class(name="EssentialOCL::InvalidType")
EssentialOCL_IterateExp = Class(name="EssentialOCL::IterateExp")
LoopExp = Class(name="LoopExp")
EssentialOCL_IteratorExp = Class(name="EssentialOCL::IteratorExp")
EssentialOCL_LetExp = Class(name="EssentialOCL::LetExp")
EssentialOCL_LiteralExp = Class(name="EssentialOCL::LiteralExp", is_abstract=True)
TupleLiteralExp = Class(name="TupleLiteralExp")
EssentialOCL_TupleType = Class(name="EssentialOCL::TupleType")
EssentialOCL_TypeExp = Class(name="EssentialOCL::TypeExp")
EssentialOCL_UnlimitedNaturalExp = Class(name="EssentialOCL::UnlimitedNaturalExp")
EssentialOCL_Variable = Class(name="EssentialOCL::Variable")
EssentialOCL_OrderedSetType = Class(name="EssentialOCL::OrderedSetType")
EssentialOCL_PrimitiveLiteralExp = Class(name="EssentialOCL::PrimitiveLiteralExp", is_abstract=True)
EssentialOCL_PropertyCallExp = Class(name="EssentialOCL::PropertyCallExp")
NavigationCallExp = Class(name="NavigationCallExp")
EssentialOCL_RealLiteralExp = Class(name="EssentialOCL::RealLiteralExp")
EssentialOCL_SequenceType = Class(name="EssentialOCL::SequenceType")
EssentialOCL_SetType = Class(name="EssentialOCL::SetType")
EssentialOCL_StringLiteralExp = Class(name="EssentialOCL::StringLiteralExp")
EssentialOCL_TemplateParameterType = Class(name="EssentialOCL::TemplateParameterType")
EssentialOCL_TupleLiteralExp = Class(name="EssentialOCL::TupleLiteralExp")
TupleLiteralPart = Class(name="TupleLiteralPart")
EssentialOCL_TupleLiteralPart = Class(name="EssentialOCL::TupleLiteralPart")
TypedModel = Class(name="TypedModel")
QVTBase_Function = Class(name="QVTBase::Function")
QVTBase_FunctionParameter = Class(name="QVTBase::FunctionParameter")
QVTBase_Pattern = Class(name="QVTBase::Pattern")
LetExp = Class(name="LetExp")
EssentialOCL_VariableExp = Class(name="EssentialOCL::VariableExp")
EssentialOCL_VoidType = Class(name="EssentialOCL::VoidType")
QVTBase_Domain = Class(name="QVTBase::Domain", is_abstract=True)
Rule = Class(name="Rule")
Transformation = Class(name="Transformation")
QVTBase_Transformation = Class(name="QVTBase::Transformation")
Predicate = Class(name="Predicate")
QVTBase_Predicate = Class(name="QVTBase::Predicate")
Pattern = Class(name="Pattern")
QVTBase_Rule = Class(name="QVTBase::Rule", is_abstract=True)
Domain = Class(name="Domain")
QVTCore_Area = Class(name="QVTCore::Area", is_abstract=True)
BottomPattern = Class(name="BottomPattern")
GuardPattern = Class(name="GuardPattern")
QVTCore_Assignment = Class(name="QVTCore::Assignment", is_abstract=True)
Tag = Class(name="Tag")
QVTBase_TypedModel = Class(name="QVTBase::TypedModel")
QVTCore_EnforcementOperation = Class(name="QVTCore::EnforcementOperation")
OperationCallExp = Class(name="OperationCallExp")
QVTCore_GuardPattern = Class(name="QVTCore::GuardPattern")
QVTCore_BottomPattern = Class(name="QVTCore::BottomPattern")
CorePattern = Class(name="CorePattern")
Area = Class(name="Area")
Assignment = Class(name="Assignment")
EnforcementOperation = Class(name="EnforcementOperation")
RealizedVariable = Class(name="RealizedVariable")
QVTCore_CoreDomain = Class(name="QVTCore::CoreDomain")
QVTCore_CorePattern = Class(name="QVTCore::CorePattern")
QVTCore_RealizedVariable = Class(name="QVTCore::RealizedVariable")
QVTCore_VariableAssignment = Class(name="QVTCore::VariableAssignment")
QVTCore_Mapping = Class(name="QVTCore::Mapping")
Mapping = Class(name="Mapping")
QVTCore_PropertyAssignment = Class(name="QVTCore::PropertyAssignment")
QVTTemplate_PropertyTemplateItem = Class(name="QVTTemplate::PropertyTemplateItem")
ObjectTemplateExp = Class(name="ObjectTemplateExp")
QVTTemplate_CollectionTemplateExp = Class(name="QVTTemplate::CollectionTemplateExp")
TemplateExp = Class(name="TemplateExp")
QVTTemplate_ObjectTemplateExp = Class(name="QVTTemplate::ObjectTemplateExp")
PropertyTemplateItem = Class(name="PropertyTemplateItem")
QVTRelation_Key = Class(name="QVTRelation::Key")
RelationalTransformation = Class(name="RelationalTransformation")
QVTTemplate_TemplateExp = Class(name="QVTTemplate::TemplateExp", is_abstract=True)
QVTRelation_DomainPattern = Class(name="QVTRelation::DomainPattern")
RelationDomain = Class(name="RelationDomain")
QVTRelation_RelationCallExp = Class(name="QVTRelation::RelationCallExp")
Relation = Class(name="Relation")
QVTRelation_RelationDomain = Class(name="QVTRelation::RelationDomain")
QVTRelation_OppositePropertyCallExp = Class(name="QVTRelation::OppositePropertyCallExp")
PropertyCallExp = Class(name="PropertyCallExp")
QVTRelation_Relation = Class(name="QVTRelation::Relation")
RelationImplementation = Class(name="RelationImplementation")
QVTRelation_RelationImplementation = Class(name="QVTRelation::RelationImplementation")
RelationDomainAssignment = Class(name="RelationDomainAssignment")
DomainPattern = Class(name="DomainPattern")
QVTRelation_RelationDomainAssignment = Class(name="QVTRelation::RelationDomainAssignment")
LogExp = Class(name="LogExp")
ImperativeOCL_AssignExp = Class(name="ImperativeOCL::AssignExp")
QVTRelation_RelationalTransformation = Class(name="QVTRelation::RelationalTransformation")
Key = Class(name="Key")
ImperativeOCL_AltExp = Class(name="ImperativeOCL::AltExp")
ImperativeExpression = Class(name="ImperativeExpression")
ImperativeOCL_AssertExp = Class(name="ImperativeOCL::AssertExp")
ImperativeOCL_BreakExp = Class(name="ImperativeOCL::BreakExp")
ImperativeOCL_CatchExp = Class(name="ImperativeOCL::CatchExp")
ImperativeOCL_BlockExp = Class(name="ImperativeOCL::BlockExp")
DictLiteralExp = Class(name="DictLiteralExp")
ImperativeOCL_DictionaryType = Class(name="ImperativeOCL::DictionaryType")
ImperativeOCL_ComputeExp = Class(name="ImperativeOCL::ComputeExp")
ImperativeOCL_ContinueExp = Class(name="ImperativeOCL::ContinueExp")
ImperativeOCL_DictLiteralExp = Class(name="ImperativeOCL::DictLiteralExp")
DictLiteralPart = Class(name="DictLiteralPart")
ImperativeOCL_DictLiteralPart = Class(name="ImperativeOCL::DictLiteralPart")
ImperativeOCL_InstantiationExp = Class(name="ImperativeOCL::InstantiationExp")
ImperativeOCL_ForExp = Class(name="ImperativeOCL::ForExp")
ImperativeLoopExp = Class(name="ImperativeLoopExp")
ImperativeOCL_ImperativeExpression = Class(name="ImperativeOCL::ImperativeExpression", is_abstract=True)
ImperativeOCL_ImperativeIterateExp = Class(name="ImperativeOCL::ImperativeIterateExp")
ImperativeOCL_ImperativeLoopExp = Class(name="ImperativeOCL::ImperativeLoopExp", is_abstract=True)
ImperativeOCL_LogExp = Class(name="ImperativeOCL::LogExp")
ImperativeOCL_ListLiteralExp = Class(name="ImperativeOCL::ListLiteralExp")
ImperativeOCL_ListType = Class(name="ImperativeOCL::ListType")
ImperativeOCL_SwitchExp = Class(name="ImperativeOCL::SwitchExp")
AltExp = Class(name="AltExp")
ImperativeOCL_RaiseExp = Class(name="ImperativeOCL::RaiseExp")
ImperativeOCL_ReturnExp = Class(name="ImperativeOCL::ReturnExp")
CatchExp = Class(name="CatchExp")
ImperativeOCL_Typedef = Class(name="ImperativeOCL::Typedef")
ImperativeOCL_TryExp = Class(name="ImperativeOCL::TryExp")
ImperativeOCL_VariableInitExp = Class(name="ImperativeOCL::VariableInitExp")
ImperativeOCL_WhileExp = Class(name="ImperativeOCL::WhileExp")
ImperativeOCL_UnlinkExp = Class(name="ImperativeOCL::UnlinkExp")
QVTOperational_Constructor = Class(name="QVTOperational::Constructor")
ImperativeOperation = Class(name="ImperativeOperation")
QVTOperational_ConstructorBody = Class(name="QVTOperational::ConstructorBody")
OperationBody = Class(name="OperationBody")
QVTOperational_ContextualProperty = Class(name="QVTOperational::ContextualProperty")
QVTOperational_Helper = Class(name="QVTOperational::Helper")
QVTOperational_ImperativeCallExp = Class(name="QVTOperational::ImperativeCallExp")
QVTOperational_EntryOperation = Class(name="QVTOperational::EntryOperation")
QVTOperational_ImperativeOperation = Class(name="QVTOperational::ImperativeOperation")
VarParameter = Class(name="VarParameter")
QVTOperational_MappingCallExp = Class(name="QVTOperational::MappingCallExp")
ImperativeCallExp = Class(name="ImperativeCallExp")
QVTOperational_MappingOperation = Class(name="QVTOperational::MappingOperation")
MappingOperation = Class(name="MappingOperation")
QVTOperational_Library = Class(name="QVTOperational::Library")
Module = Class(name="Module")
QVTOperational_MappingBody = Class(name="QVTOperational::MappingBody")
QVTOperational_MappingParameter = Class(name="QVTOperational::MappingParameter")
ModelParameter = Class(name="ModelParameter")
QVTOperational_Module = Class(name="QVTOperational::Module")
QVTOperational_ModelParameter = Class(name="QVTOperational::ModelParameter")
OperationalTransformation = Class(name="OperationalTransformation")
QVTOperational_ModelType = Class(name="QVTOperational::ModelType")
ModelType = Class(name="ModelType")
QVTOperational_ModuleImport = Class(name="QVTOperational::ModuleImport")
EntryOperation = Class(name="EntryOperation")
ModuleImport = Class(name="ModuleImport")
QVTOperational_OperationBody = Class(name="QVTOperational::OperationBody")
QVTOperational_ObjectExp = Class(name="QVTOperational::ObjectExp")
InstantiationExp = Class(name="InstantiationExp")
ConstructorBody = Class(name="ConstructorBody")
QVTOperational_OperationalTransformation = Class(name="QVTOperational::OperationalTransformation")
QVTOperational_ResolveInExp = Class(name="QVTOperational::ResolveInExp")
ResolveExp = Class(name="ResolveExp")
QVTOperational_VarParameter = Class(name="QVTOperational::VarParameter")
QVTOperational_ResolveExp = Class(name="QVTOperational::ResolveExp")

# Class class attributes and methods

# EMOF_Comment class attributes and methods
EMOF_Comment_body: Property = Property(name="body", type=StringType)
EMOF_Comment.attributes={EMOF_Comment_body}

# Element class attributes and methods

# NamedElement class attributes and methods

# EMOF_DataType class attributes and methods

# EMOF_Element class attributes and methods
EMOF_Element_m_container: Method = Method(name="container", parameters={}, type=StringType)
EMOF_Element_m_equals: Method = Method(name="equals", parameters={Parameter(name='object')}, type=StringType)
EMOF_Element_m_get: Method = Method(name="get", parameters={Parameter(name='property')}, type=StringType)
EMOF_Element_m_getMetaClass: Method = Method(name="getMetaClass", parameters={}, type=StringType)
EMOF_Element_m_isSet: Method = Method(name="isSet", parameters={Parameter(name='property')}, type=StringType)
EMOF_Element_m_set: Method = Method(name="set", parameters={Parameter(name='property'), Parameter(name='object')})
EMOF_Element_m_unset: Method = Method(name="unset", parameters={Parameter(name='property')})
EMOF_Element.methods={EMOF_Element_m_set, EMOF_Element_m_unset, EMOF_Element_m_getMetaClass, EMOF_Element_m_isSet, EMOF_Element_m_equals, EMOF_Element_m_get, EMOF_Element_m_container}

# Object class attributes and methods

# EMOF_Class class attributes and methods
EMOF_Class_isAbstract: Property = Property(name="isAbstract", type=StringType)
EMOF_Class.attributes={EMOF_Class_isAbstract}

# Type class attributes and methods

# Property class attributes and methods

# Operation class attributes and methods

# Enumeration class attributes and methods

# EMOF_Extent class attributes and methods
EMOF_Extent_m_elements: Method = Method(name="elements", parameters={}, type=StringType)
EMOF_Extent_m_useContainment: Method = Method(name="useContainment", parameters={}, type=StringType)
EMOF_Extent.methods={EMOF_Extent_m_useContainment, EMOF_Extent_m_elements}

# EMOF_Factory class attributes and methods
EMOF_Factory_m_convertToString: Method = Method(name="convertToString", parameters={Parameter(name='dataType'), Parameter(name='object')}, type=StringType)
EMOF_Factory_m_create: Method = Method(name="create", parameters={Parameter(name='metaClass')}, type=StringType)
EMOF_Factory_m_createFromString: Method = Method(name="createFromString", parameters={Parameter(name='string'), Parameter(name='dataType')}, type=StringType)
EMOF_Factory.methods={EMOF_Factory_m_createFromString, EMOF_Factory_m_create, EMOF_Factory_m_convertToString}

# Package class attributes and methods

# Comment class attributes and methods

# EMOF_Enumeration class attributes and methods

# DataType class attributes and methods

# EnumerationLiteral class attributes and methods

# EMOF_EnumerationLiteral class attributes and methods

# EMOF_Package class attributes and methods
EMOF_Package_uri: Property = Property(name="uri", type=StringType)
EMOF_Package.attributes={EMOF_Package_uri}

# EMOF_Parameter class attributes and methods

# EMOF_MultiplicityElement class attributes and methods
EMOF_MultiplicityElement_isOrdered: Property = Property(name="isOrdered", type=StringType)
EMOF_MultiplicityElement_isUnique: Property = Property(name="isUnique", type=StringType)
EMOF_MultiplicityElement_lower: Property = Property(name="lower", type=StringType)
EMOF_MultiplicityElement_upper: Property = Property(name="upper", type=StringType)
EMOF_MultiplicityElement.attributes={EMOF_MultiplicityElement_isOrdered, EMOF_MultiplicityElement_isUnique, EMOF_MultiplicityElement_upper, EMOF_MultiplicityElement_lower}

# EMOF_NamedElement class attributes and methods
EMOF_NamedElement_name: Property = Property(name="name", type=StringType)
EMOF_NamedElement.attributes={EMOF_NamedElement_name}

# EMOF_Object class attributes and methods

# EMOF_Operation class attributes and methods

# TypedElement class attributes and methods

# MultiplicityElement class attributes and methods

# Parameter class attributes and methods

# EMOF_ReflectiveSequence class attributes and methods
EMOF_ReflectiveSequence_m_add: Method = Method(name="add", parameters={Parameter(name='object'), Parameter(name='index')})
EMOF_ReflectiveSequence_m_get: Method = Method(name="get", parameters={Parameter(name='index')}, type=StringType)
EMOF_ReflectiveSequence_m_remove: Method = Method(name="remove", parameters={Parameter(name='index')}, type=StringType)
EMOF_ReflectiveSequence_m_set: Method = Method(name="set", parameters={Parameter(name='index'), Parameter(name='object')}, type=StringType)
EMOF_ReflectiveSequence.methods={EMOF_ReflectiveSequence_m_remove, EMOF_ReflectiveSequence_m_get, EMOF_ReflectiveSequence_m_add, EMOF_ReflectiveSequence_m_set}

# ReflectiveCollection class attributes and methods

# EMOF_Tag class attributes and methods
EMOF_Tag_name: Property = Property(name="name", type=StringType)
EMOF_Tag_value: Property = Property(name="value", type=StringType)
EMOF_Tag.attributes={EMOF_Tag_name, EMOF_Tag_value}

# EMOF_PrimitiveType class attributes and methods

# EMOF_Property class attributes and methods
EMOF_Property_default: Property = Property(name="default", type=StringType)
EMOF_Property_isComposite: Property = Property(name="isComposite", type=StringType)
EMOF_Property_isDerived: Property = Property(name="isDerived", type=StringType)
EMOF_Property_isID: Property = Property(name="isID", type=StringType)
EMOF_Property_isReadOnly: Property = Property(name="isReadOnly", type=StringType)
EMOF_Property.attributes={EMOF_Property_isComposite, EMOF_Property_isReadOnly, EMOF_Property_isID, EMOF_Property_isDerived, EMOF_Property_default}

# EMOF_ReflectiveCollection class attributes and methods
EMOF_ReflectiveCollection_m_add: Method = Method(name="add", parameters={Parameter(name='object')}, type=StringType)
EMOF_ReflectiveCollection_m_addAll: Method = Method(name="addAll", parameters={Parameter(name='objects')}, type=StringType)
EMOF_ReflectiveCollection_m_clear: Method = Method(name="clear", parameters={})
EMOF_ReflectiveCollection_m_remove: Method = Method(name="remove", parameters={Parameter(name='object')}, type=StringType)
EMOF_ReflectiveCollection_m_size: Method = Method(name="size", parameters={}, type=StringType)
EMOF_ReflectiveCollection.methods={EMOF_ReflectiveCollection_m_add, EMOF_ReflectiveCollection_m_addAll, EMOF_ReflectiveCollection_m_clear, EMOF_ReflectiveCollection_m_remove, EMOF_ReflectiveCollection_m_size}

# EssentialOCL_BooleanLiteralExp class attributes and methods
EssentialOCL_BooleanLiteralExp_booleanSymbol: Property = Property(name="booleanSymbol", type=StringType)
EssentialOCL_BooleanLiteralExp.attributes={EssentialOCL_BooleanLiteralExp_booleanSymbol}

# PrimitiveLiteralExp class attributes and methods

# EssentialOCL_CallExp class attributes and methods

# OclExpression class attributes and methods

# EssentialOCL_CollectionItem class attributes and methods

# CollectionLiteralPart class attributes and methods

# EMOF_Type class attributes and methods
EMOF_Type_m_isInstance: Method = Method(name="isInstance", parameters={Parameter(name='object')}, type=StringType)
EMOF_Type.methods={EMOF_Type_m_isInstance}

# EMOF_TypedElement class attributes and methods

# EMOF_URIExtent class attributes and methods
EMOF_URIExtent_m_contextURI: Method = Method(name="contextURI", parameters={}, type=StringType)
EMOF_URIExtent_m_element: Method = Method(name="element", parameters={Parameter(name='uri')}, type=StringType)
EMOF_URIExtent_m_uri: Method = Method(name="uri", parameters={Parameter(name='element')}, type=StringType)
EMOF_URIExtent.methods={EMOF_URIExtent_m_uri, EMOF_URIExtent_m_contextURI, EMOF_URIExtent_m_element}

# Extent class attributes and methods

# EssentialOCL_AnyType class attributes and methods

# EssentialOCL_BagType class attributes and methods

# CollectionType class attributes and methods

# EssentialOCL_CollectionType class attributes and methods

# EssentialOCL_CollectionLiteralExp class attributes and methods
EssentialOCL_CollectionLiteralExp_kind: Property = Property(name="kind", type=StringType)
EssentialOCL_CollectionLiteralExp.attributes={EssentialOCL_CollectionLiteralExp_kind}

# LiteralExp class attributes and methods

# EssentialOCL_CollectionLiteralPart class attributes and methods

# CollectionLiteralExp class attributes and methods

# EssentialOCL_CollectionRange class attributes and methods

# EssentialOCL_FeatureCallExp class attributes and methods

# CallExp class attributes and methods

# EssentialOCL_IfExp class attributes and methods

# EssentialOCL_EnumLiteralExp class attributes and methods

# EssentialOCL_ExpressionInOcl class attributes and methods

# Variable class attributes and methods

# EssentialOCL_LoopExp class attributes and methods

# EssentialOCL_NavigationCallExp class attributes and methods

# FeatureCallExp class attributes and methods

# EssentialOCL_NullLiteralExp class attributes and methods

# EssentialOCL_NumericLiteralExp class attributes and methods

# EssentialOCL_OclExpression class attributes and methods

# EssentialOCL_OperationCallExp class attributes and methods

# EssentialOCL_IntegerLiteralExp class attributes and methods
EssentialOCL_IntegerLiteralExp_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
EssentialOCL_IntegerLiteralExp.attributes={EssentialOCL_IntegerLiteralExp_integerSymbol}

# NumericLiteralExp class attributes and methods

# EssentialOCL_InvalidLiteralExp class attributes and methods

# EssentialOCL_InvalidType class attributes and methods

# EssentialOCL_IterateExp class attributes and methods

# LoopExp class attributes and methods

# EssentialOCL_IteratorExp class attributes and methods

# EssentialOCL_LetExp class attributes and methods

# EssentialOCL_LiteralExp class attributes and methods

# TupleLiteralExp class attributes and methods

# EssentialOCL_TupleType class attributes and methods

# EssentialOCL_TypeExp class attributes and methods

# EssentialOCL_UnlimitedNaturalExp class attributes and methods
EssentialOCL_UnlimitedNaturalExp_symbol: Property = Property(name="symbol", type=StringType)
EssentialOCL_UnlimitedNaturalExp.attributes={EssentialOCL_UnlimitedNaturalExp_symbol}

# EssentialOCL_Variable class attributes and methods

# EssentialOCL_OrderedSetType class attributes and methods

# EssentialOCL_PrimitiveLiteralExp class attributes and methods

# EssentialOCL_PropertyCallExp class attributes and methods

# NavigationCallExp class attributes and methods

# EssentialOCL_RealLiteralExp class attributes and methods
EssentialOCL_RealLiteralExp_realSymbol: Property = Property(name="realSymbol", type=StringType)
EssentialOCL_RealLiteralExp.attributes={EssentialOCL_RealLiteralExp_realSymbol}

# EssentialOCL_SequenceType class attributes and methods

# EssentialOCL_SetType class attributes and methods

# EssentialOCL_StringLiteralExp class attributes and methods
EssentialOCL_StringLiteralExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
EssentialOCL_StringLiteralExp.attributes={EssentialOCL_StringLiteralExp_stringSymbol}

# EssentialOCL_TemplateParameterType class attributes and methods
EssentialOCL_TemplateParameterType_specification: Property = Property(name="specification", type=StringType)
EssentialOCL_TemplateParameterType.attributes={EssentialOCL_TemplateParameterType_specification}

# EssentialOCL_TupleLiteralExp class attributes and methods

# TupleLiteralPart class attributes and methods

# EssentialOCL_TupleLiteralPart class attributes and methods

# TypedModel class attributes and methods

# QVTBase_Function class attributes and methods

# QVTBase_FunctionParameter class attributes and methods

# QVTBase_Pattern class attributes and methods

# LetExp class attributes and methods

# EssentialOCL_VariableExp class attributes and methods

# EssentialOCL_VoidType class attributes and methods

# QVTBase_Domain class attributes and methods
QVTBase_Domain_isCheckable: Property = Property(name="isCheckable", type=StringType)
QVTBase_Domain_isEnforceable: Property = Property(name="isEnforceable", type=StringType)
QVTBase_Domain.attributes={QVTBase_Domain_isCheckable, QVTBase_Domain_isEnforceable}

# Rule class attributes and methods

# Transformation class attributes and methods

# QVTBase_Transformation class attributes and methods

# Predicate class attributes and methods

# QVTBase_Predicate class attributes and methods

# Pattern class attributes and methods

# QVTBase_Rule class attributes and methods

# Domain class attributes and methods

# QVTCore_Area class attributes and methods

# BottomPattern class attributes and methods

# GuardPattern class attributes and methods

# QVTCore_Assignment class attributes and methods
QVTCore_Assignment_isDefault: Property = Property(name="isDefault", type=StringType)
QVTCore_Assignment.attributes={QVTCore_Assignment_isDefault}

# Tag class attributes and methods

# QVTBase_TypedModel class attributes and methods

# QVTCore_EnforcementOperation class attributes and methods
QVTCore_EnforcementOperation_enforcementMode: Property = Property(name="enforcementMode", type=StringType)
QVTCore_EnforcementOperation.attributes={QVTCore_EnforcementOperation_enforcementMode}

# OperationCallExp class attributes and methods

# QVTCore_GuardPattern class attributes and methods

# QVTCore_BottomPattern class attributes and methods

# CorePattern class attributes and methods

# Area class attributes and methods

# Assignment class attributes and methods

# EnforcementOperation class attributes and methods

# RealizedVariable class attributes and methods

# QVTCore_CoreDomain class attributes and methods

# QVTCore_CorePattern class attributes and methods

# QVTCore_RealizedVariable class attributes and methods

# QVTCore_VariableAssignment class attributes and methods

# QVTCore_Mapping class attributes and methods

# Mapping class attributes and methods

# QVTCore_PropertyAssignment class attributes and methods

# QVTTemplate_PropertyTemplateItem class attributes and methods
QVTTemplate_PropertyTemplateItem_isOpposite: Property = Property(name="isOpposite", type=StringType)
QVTTemplate_PropertyTemplateItem.attributes={QVTTemplate_PropertyTemplateItem_isOpposite}

# ObjectTemplateExp class attributes and methods

# QVTTemplate_CollectionTemplateExp class attributes and methods

# TemplateExp class attributes and methods

# QVTTemplate_ObjectTemplateExp class attributes and methods

# PropertyTemplateItem class attributes and methods

# QVTRelation_Key class attributes and methods

# RelationalTransformation class attributes and methods

# QVTTemplate_TemplateExp class attributes and methods

# QVTRelation_DomainPattern class attributes and methods

# RelationDomain class attributes and methods

# QVTRelation_RelationCallExp class attributes and methods

# Relation class attributes and methods

# QVTRelation_RelationDomain class attributes and methods

# QVTRelation_OppositePropertyCallExp class attributes and methods

# PropertyCallExp class attributes and methods

# QVTRelation_Relation class attributes and methods
QVTRelation_Relation_isTopLevel: Property = Property(name="isTopLevel", type=StringType)
QVTRelation_Relation.attributes={QVTRelation_Relation_isTopLevel}

# RelationImplementation class attributes and methods

# QVTRelation_RelationImplementation class attributes and methods

# RelationDomainAssignment class attributes and methods

# DomainPattern class attributes and methods

# QVTRelation_RelationDomainAssignment class attributes and methods

# LogExp class attributes and methods

# ImperativeOCL_AssignExp class attributes and methods
ImperativeOCL_AssignExp_isReset: Property = Property(name="isReset", type=StringType)
ImperativeOCL_AssignExp.attributes={ImperativeOCL_AssignExp_isReset}

# QVTRelation_RelationalTransformation class attributes and methods

# Key class attributes and methods

# ImperativeOCL_AltExp class attributes and methods

# ImperativeExpression class attributes and methods

# ImperativeOCL_AssertExp class attributes and methods
ImperativeOCL_AssertExp_severity: Property = Property(name="severity", type=StringType)
ImperativeOCL_AssertExp.attributes={ImperativeOCL_AssertExp_severity}

# ImperativeOCL_BreakExp class attributes and methods

# ImperativeOCL_CatchExp class attributes and methods

# ImperativeOCL_BlockExp class attributes and methods

# DictLiteralExp class attributes and methods

# ImperativeOCL_DictionaryType class attributes and methods

# ImperativeOCL_ComputeExp class attributes and methods

# ImperativeOCL_ContinueExp class attributes and methods

# ImperativeOCL_DictLiteralExp class attributes and methods

# DictLiteralPart class attributes and methods

# ImperativeOCL_DictLiteralPart class attributes and methods

# ImperativeOCL_InstantiationExp class attributes and methods

# ImperativeOCL_ForExp class attributes and methods

# ImperativeLoopExp class attributes and methods

# ImperativeOCL_ImperativeExpression class attributes and methods

# ImperativeOCL_ImperativeIterateExp class attributes and methods

# ImperativeOCL_ImperativeLoopExp class attributes and methods

# ImperativeOCL_LogExp class attributes and methods

# ImperativeOCL_ListLiteralExp class attributes and methods

# ImperativeOCL_ListType class attributes and methods

# ImperativeOCL_SwitchExp class attributes and methods

# AltExp class attributes and methods

# ImperativeOCL_RaiseExp class attributes and methods

# ImperativeOCL_ReturnExp class attributes and methods

# CatchExp class attributes and methods

# ImperativeOCL_Typedef class attributes and methods

# ImperativeOCL_TryExp class attributes and methods

# ImperativeOCL_VariableInitExp class attributes and methods
ImperativeOCL_VariableInitExp_withResult: Property = Property(name="withResult", type=StringType)
ImperativeOCL_VariableInitExp.attributes={ImperativeOCL_VariableInitExp_withResult}

# ImperativeOCL_WhileExp class attributes and methods

# ImperativeOCL_UnlinkExp class attributes and methods

# QVTOperational_Constructor class attributes and methods

# ImperativeOperation class attributes and methods

# QVTOperational_ConstructorBody class attributes and methods

# OperationBody class attributes and methods

# QVTOperational_ContextualProperty class attributes and methods

# QVTOperational_Helper class attributes and methods
QVTOperational_Helper_isQuery: Property = Property(name="isQuery", type=StringType)
QVTOperational_Helper.attributes={QVTOperational_Helper_isQuery}

# QVTOperational_ImperativeCallExp class attributes and methods
QVTOperational_ImperativeCallExp_isVirtual: Property = Property(name="isVirtual", type=StringType)
QVTOperational_ImperativeCallExp.attributes={QVTOperational_ImperativeCallExp_isVirtual}

# QVTOperational_EntryOperation class attributes and methods

# QVTOperational_ImperativeOperation class attributes and methods
QVTOperational_ImperativeOperation_isBlackbox: Property = Property(name="isBlackbox", type=StringType)
QVTOperational_ImperativeOperation.attributes={QVTOperational_ImperativeOperation_isBlackbox}

# VarParameter class attributes and methods

# QVTOperational_MappingCallExp class attributes and methods
QVTOperational_MappingCallExp_isStrict: Property = Property(name="isStrict", type=StringType)
QVTOperational_MappingCallExp.attributes={QVTOperational_MappingCallExp_isStrict}

# ImperativeCallExp class attributes and methods

# QVTOperational_MappingOperation class attributes and methods

# MappingOperation class attributes and methods

# QVTOperational_Library class attributes and methods

# Module class attributes and methods

# QVTOperational_MappingBody class attributes and methods

# QVTOperational_MappingParameter class attributes and methods

# ModelParameter class attributes and methods

# QVTOperational_Module class attributes and methods
QVTOperational_Module_isBlackbox: Property = Property(name="isBlackbox", type=StringType)
QVTOperational_Module.attributes={QVTOperational_Module_isBlackbox}

# QVTOperational_ModelParameter class attributes and methods

# OperationalTransformation class attributes and methods

# QVTOperational_ModelType class attributes and methods
QVTOperational_ModelType_conformanceKind: Property = Property(name="conformanceKind", type=StringType)
QVTOperational_ModelType.attributes={QVTOperational_ModelType_conformanceKind}

# ModelType class attributes and methods

# QVTOperational_ModuleImport class attributes and methods
QVTOperational_ModuleImport_kind: Property = Property(name="kind", type=StringType)
QVTOperational_ModuleImport.attributes={QVTOperational_ModuleImport_kind}

# EntryOperation class attributes and methods

# ModuleImport class attributes and methods

# QVTOperational_OperationBody class attributes and methods

# QVTOperational_ObjectExp class attributes and methods

# InstantiationExp class attributes and methods

# ConstructorBody class attributes and methods

# QVTOperational_OperationalTransformation class attributes and methods

# QVTOperational_ResolveInExp class attributes and methods

# ResolveExp class attributes and methods

# QVTOperational_VarParameter class attributes and methods
QVTOperational_VarParameter_kind: Property = Property(name="kind", type=StringType)
QVTOperational_VarParameter.attributes={QVTOperational_VarParameter_kind}

# QVTOperational_ResolveExp class attributes and methods
QVTOperational_ResolveExp_isDeferred: Property = Property(name="isDeferred", type=StringType)
QVTOperational_ResolveExp_isInverse: Property = Property(name="isInverse", type=StringType)
QVTOperational_ResolveExp_one: Property = Property(name="one", type=StringType)
QVTOperational_ResolveExp.attributes={QVTOperational_ResolveExp_isDeferred, QVTOperational_ResolveExp_one, QVTOperational_ResolveExp_isInverse}

# Relationships
superClass4: BinaryAssociation = BinaryAssociation(
    name="superClass4",
    ends={
        Property(name="Class", type=EMOF_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Class", type=Class_, multiplicity=Multiplicity(0, 9999))
    }
)
annotatedElement5: BinaryAssociation = BinaryAssociation(
    name="annotatedElement5",
    ends={
        Property(name="NamedElement", type=EMOF_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Comment", type=NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAttribute0: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute0",
    ends={
        Property(name="#", type=EMOF_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="1", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation1: BinaryAssociation = BinaryAssociation(
    name="ownedOperation1",
    ends={
        Property(name="#3", type=EMOF_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="12", type=Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumeration10: BinaryAssociation = BinaryAssociation(
    name="enumeration10",
    ends={
        Property(name="#12", type=EMOF_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="111", type=Enumeration_, multiplicity=Multiplicity(0, 1))
    }
)
package13: BinaryAssociation = BinaryAssociation(
    name="package13",
    ends={
        Property(name="Package", type=EMOF_Factory, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Factory", type=Package, multiplicity=Multiplicity(1, 1))
    }
)
ownedComment6: BinaryAssociation = BinaryAssociation(
    name="ownedComment6",
    ends={
        Property(name="Comment", type=EMOF_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Element", type=Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedLiteral7: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral7",
    ends={
        Property(name="#9", type=EMOF_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="18", type=EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
raisedException20: BinaryAssociation = BinaryAssociation(
    name="raisedException20",
    ends={
        Property(name="Type", type=EMOF_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Operation", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
nestedPackage21: BinaryAssociation = BinaryAssociation(
    name="nestedPackage21",
    ends={
        Property(name="#23", type=EMOF_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="122", type=Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestingPackage24: BinaryAssociation = BinaryAssociation(
    name="nestingPackage24",
    ends={
        Property(name="#26", type=EMOF_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="125", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
ownedType27: BinaryAssociation = BinaryAssociation(
    name="ownedType27",
    ends={
        Property(name="#29", type=EMOF_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="128", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class14: BinaryAssociation = BinaryAssociation(
    name="class14",
    ends={
        Property(name="#16", type=EMOF_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="115", type=Class_, multiplicity=Multiplicity(0, 1))
    }
)
ownedParameter17: BinaryAssociation = BinaryAssociation(
    name="ownedParameter17",
    ends={
        Property(name="#19", type=EMOF_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="118", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element37: BinaryAssociation = BinaryAssociation(
    name="element37",
    ends={
        Property(name="Element", type=EMOF_Tag, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Tag", type=Element, multiplicity=Multiplicity(0, 9999))
    }
)
operation30: BinaryAssociation = BinaryAssociation(
    name="operation30",
    ends={
        Property(name="#32", type=EMOF_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="131", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
class33: BinaryAssociation = BinaryAssociation(
    name="class33",
    ends={
        Property(name="#35", type=EMOF_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="134", type=Class_, multiplicity=Multiplicity(0, 1))
    }
)
opposite36: BinaryAssociation = BinaryAssociation(
    name="opposite36",
    ends={
        Property(name="Property", type=EMOF_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Property", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
source43: BinaryAssociation = BinaryAssociation(
    name="source43",
    ends={
        Property(name="OclExpression", type=EssentialOCL_CallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_CallExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
item44: BinaryAssociation = BinaryAssociation(
    name="item44",
    ends={
        Property(name="OclExpression45", type=EssentialOCL_CollectionItem, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_CollectionItem", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
package38: BinaryAssociation = BinaryAssociation(
    name="package38",
    ends={
        Property(name="#40", type=EMOF_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="139", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
type41: BinaryAssociation = BinaryAssociation(
    name="type41",
    ends={
        Property(name="Type42", type=EMOF_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_TypedElement", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
last53: BinaryAssociation = BinaryAssociation(
    name="last53",
    ends={
        Property(name="OclExpression55", type=EssentialOCL_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_CollectionRange54", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementType56: BinaryAssociation = BinaryAssociation(
    name="elementType56",
    ends={
        Property(name="Type57", type=EssentialOCL_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_CollectionType", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
part46: BinaryAssociation = BinaryAssociation(
    name="part46",
    ends={
        Property(name="#47", type=EssentialOCL_CollectionLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="2", type=CollectionLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collectionLiteralExp48: BinaryAssociation = BinaryAssociation(
    name="collectionLiteralExp48",
    ends={
        Property(name="#50", type=EssentialOCL_CollectionLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="249", type=CollectionLiteralExp, multiplicity=Multiplicity(1, 1))
    }
)
first51: BinaryAssociation = BinaryAssociation(
    name="first51",
    ends={
        Property(name="OclExpression52", type=EssentialOCL_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_CollectionRange", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameterVariable66: BinaryAssociation = BinaryAssociation(
    name="parameterVariable66",
    ends={
        Property(name="Variable68", type=EssentialOCL_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_ExpressionInOcl67", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resultVariable69: BinaryAssociation = BinaryAssociation(
    name="resultVariable69",
    ends={
        Property(name="Variable71", type=EssentialOCL_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_ExpressionInOcl70", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition72: BinaryAssociation = BinaryAssociation(
    name="condition72",
    ends={
        Property(name="OclExpression73", type=EssentialOCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_IfExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression74: BinaryAssociation = BinaryAssociation(
    name="elseExpression74",
    ends={
        Property(name="OclExpression76", type=EssentialOCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_IfExp75", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referredEnumLiteral58: BinaryAssociation = BinaryAssociation(
    name="referredEnumLiteral58",
    ends={
        Property(name="EnumerationLiteral", type=EssentialOCL_EnumLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_EnumLiteralExp", type=EnumerationLiteral, multiplicity=Multiplicity(0, 1))
    }
)
bodyExpression59: BinaryAssociation = BinaryAssociation(
    name="bodyExpression59",
    ends={
        Property(name="OclExpression60", type=EssentialOCL_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_ExpressionInOcl", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
contextVariable61: BinaryAssociation = BinaryAssociation(
    name="contextVariable61",
    ends={
        Property(name="Variable", type=EssentialOCL_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_ExpressionInOcl62", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
generatedType63: BinaryAssociation = BinaryAssociation(
    name="generatedType63",
    ends={
        Property(name="Type65", type=EssentialOCL_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_ExpressionInOcl64", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body87: BinaryAssociation = BinaryAssociation(
    name="body87",
    ends={
        Property(name="OclExpression88", type=EssentialOCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_LoopExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterator89: BinaryAssociation = BinaryAssociation(
    name="iterator89",
    ends={
        Property(name="Variable91", type=EssentialOCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_LoopExp90", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument92: BinaryAssociation = BinaryAssociation(
    name="argument92",
    ends={
        Property(name="OclExpression93", type=EssentialOCL_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_OperationCallExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredOperation94: BinaryAssociation = BinaryAssociation(
    name="referredOperation94",
    ends={
        Property(name="Operation", type=EssentialOCL_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_OperationCallExp95", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
thenExpression77: BinaryAssociation = BinaryAssociation(
    name="thenExpression77",
    ends={
        Property(name="OclExpression79", type=EssentialOCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_IfExp78", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result80: BinaryAssociation = BinaryAssociation(
    name="result80",
    ends={
        Property(name="Variable81", type=EssentialOCL_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_IterateExp", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
in82: BinaryAssociation = BinaryAssociation(
    name="in82",
    ends={
        Property(name="OclExpression83", type=EssentialOCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_LetExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable84: BinaryAssociation = BinaryAssociation(
    name="variable84",
    ends={
        Property(name="#86", type=EssentialOCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="285", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tupleLiteralExp103: BinaryAssociation = BinaryAssociation(
    name="tupleLiteralExp103",
    ends={
        Property(name="#105", type=EssentialOCL_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="2104", type=TupleLiteralExp, multiplicity=Multiplicity(0, 1))
    }
)
value106: BinaryAssociation = BinaryAssociation(
    name="value106",
    ends={
        Property(name="OclExpression108", type=EssentialOCL_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_TupleLiteralPart107", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referredType109: BinaryAssociation = BinaryAssociation(
    name="referredType109",
    ends={
        Property(name="Type110", type=EssentialOCL_TypeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_TypeExp", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
initExpression111: BinaryAssociation = BinaryAssociation(
    name="initExpression111",
    ends={
        Property(name="OclExpression112", type=EssentialOCL_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_Variable", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referredProperty96: BinaryAssociation = BinaryAssociation(
    name="referredProperty96",
    ends={
        Property(name="Property97", type=EssentialOCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_PropertyCallExp", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
part98: BinaryAssociation = BinaryAssociation(
    name="part98",
    ends={
        Property(name="#100", type=EssentialOCL_TupleLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="299", type=TupleLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute101: BinaryAssociation = BinaryAssociation(
    name="attribute101",
    ends={
        Property(name="Property102", type=EssentialOCL_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_TupleLiteralPart", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
typedModel122: BinaryAssociation = BinaryAssociation(
    name="typedModel122",
    ends={
        Property(name="TypedModel", type=QVTBase_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTBase_Domain", type=TypedModel, multiplicity=Multiplicity(0, 1))
    }
)
queryExpression123: BinaryAssociation = BinaryAssociation(
    name="queryExpression123",
    ends={
        Property(name="OclExpression124", type=QVTBase_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTBase_Function", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bindsTo125: BinaryAssociation = BinaryAssociation(
    name="bindsTo125",
    ends={
        Property(name="Variable126", type=QVTBase_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTBase_Pattern", type=Variable, multiplicity=Multiplicity(0, 9999))
    }
)
letExp113: BinaryAssociation = BinaryAssociation(
    name="letExp113",
    ends={
        Property(name="#115", type=EssentialOCL_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="2114", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
representedParameter116: BinaryAssociation = BinaryAssociation(
    name="representedParameter116",
    ends={
        Property(name="Parameter", type=EssentialOCL_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_Variable117", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
referredVariable118: BinaryAssociation = BinaryAssociation(
    name="referredVariable118",
    ends={
        Property(name="Variable119", type=EssentialOCL_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_VariableExp", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
rule120: BinaryAssociation = BinaryAssociation(
    name="rule120",
    ends={
        Property(name="#121", type=QVTBase_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="3", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
overrides138: BinaryAssociation = BinaryAssociation(
    name="overrides138",
    ends={
        Property(name="Rule", type=QVTBase_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTBase_Rule", type=Rule, multiplicity=Multiplicity(0, 1))
    }
)
transformation139: BinaryAssociation = BinaryAssociation(
    name="transformation139",
    ends={
        Property(name="#141", type=QVTBase_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="3140", type=Transformation, multiplicity=Multiplicity(0, 1))
    }
)
extends142: BinaryAssociation = BinaryAssociation(
    name="extends142",
    ends={
        Property(name="Transformation", type=QVTBase_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTBase_Transformation", type=Transformation, multiplicity=Multiplicity(0, 1))
    }
)
modelParameter143: BinaryAssociation = BinaryAssociation(
    name="modelParameter143",
    ends={
        Property(name="#145", type=QVTBase_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="3144", type=TypedModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predicate127: BinaryAssociation = BinaryAssociation(
    name="predicate127",
    ends={
        Property(name="#129", type=QVTBase_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="3128", type=Predicate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conditionExpression130: BinaryAssociation = BinaryAssociation(
    name="conditionExpression130",
    ends={
        Property(name="OclExpression131", type=QVTBase_Predicate, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTBase_Predicate", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
pattern132: BinaryAssociation = BinaryAssociation(
    name="pattern132",
    ends={
        Property(name="#134", type=QVTBase_Predicate, multiplicity=Multiplicity(1, 1)),
        Property(name="3133", type=Pattern, multiplicity=Multiplicity(1, 1))
    }
)
domain135: BinaryAssociation = BinaryAssociation(
    name="domain135",
    ends={
        Property(name="#137", type=QVTBase_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="3136", type=Domain, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bottomPattern159: BinaryAssociation = BinaryAssociation(
    name="bottomPattern159",
    ends={
        Property(name="#160", type=QVTCore_Area, multiplicity=Multiplicity(1, 1)),
        Property(name="4", type=BottomPattern, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
guardPattern161: BinaryAssociation = BinaryAssociation(
    name="guardPattern161",
    ends={
        Property(name="#163", type=QVTCore_Area, multiplicity=Multiplicity(1, 1)),
        Property(name="4162", type=GuardPattern, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bottomPattern164: BinaryAssociation = BinaryAssociation(
    name="bottomPattern164",
    ends={
        Property(name="#166", type=QVTCore_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="4165", type=BottomPattern, multiplicity=Multiplicity(1, 1))
    }
)
value167: BinaryAssociation = BinaryAssociation(
    name="value167",
    ends={
        Property(name="OclExpression168", type=QVTCore_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTCore_Assignment", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedTag146: BinaryAssociation = BinaryAssociation(
    name="ownedTag146",
    ends={
        Property(name="Tag", type=QVTBase_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTBase_Transformation147", type=Tag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rule148: BinaryAssociation = BinaryAssociation(
    name="rule148",
    ends={
        Property(name="#150", type=QVTBase_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="3149", type=Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependsOn151: BinaryAssociation = BinaryAssociation(
    name="dependsOn151",
    ends={
        Property(name="TypedModel152", type=QVTBase_TypedModel, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTBase_TypedModel", type=TypedModel, multiplicity=Multiplicity(0, 9999))
    }
)
transformation153: BinaryAssociation = BinaryAssociation(
    name="transformation153",
    ends={
        Property(name="#155", type=QVTBase_TypedModel, multiplicity=Multiplicity(1, 1)),
        Property(name="3154", type=Transformation, multiplicity=Multiplicity(1, 1))
    }
)
usedPackage156: BinaryAssociation = BinaryAssociation(
    name="usedPackage156",
    ends={
        Property(name="Package158", type=QVTBase_TypedModel, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTBase_TypedModel157", type=Package, multiplicity=Multiplicity(1, 9999))
    }
)
variable181: BinaryAssociation = BinaryAssociation(
    name="variable181",
    ends={
        Property(name="Variable182", type=QVTCore_CorePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTCore_CorePattern", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bottomPattern183: BinaryAssociation = BinaryAssociation(
    name="bottomPattern183",
    ends={
        Property(name="#185", type=QVTCore_EnforcementOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="4184", type=BottomPattern, multiplicity=Multiplicity(1, 1))
    }
)
operationCallExp186: BinaryAssociation = BinaryAssociation(
    name="operationCallExp186",
    ends={
        Property(name="OperationCallExp", type=QVTCore_EnforcementOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTCore_EnforcementOperation", type=OperationCallExp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
area169: BinaryAssociation = BinaryAssociation(
    name="area169",
    ends={
        Property(name="#171", type=QVTCore_BottomPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="4170", type=Area, multiplicity=Multiplicity(1, 1))
    }
)
assignment172: BinaryAssociation = BinaryAssociation(
    name="assignment172",
    ends={
        Property(name="#174", type=QVTCore_BottomPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="4173", type=Assignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enforcementOperation175: BinaryAssociation = BinaryAssociation(
    name="enforcementOperation175",
    ends={
        Property(name="#177", type=QVTCore_BottomPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="4176", type=EnforcementOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
realizedVariable178: BinaryAssociation = BinaryAssociation(
    name="realizedVariable178",
    ends={
        Property(name="#180", type=QVTCore_BottomPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="4179", type=RealizedVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetProperty204: BinaryAssociation = BinaryAssociation(
    name="targetProperty204",
    ends={
        Property(name="Property206", type=QVTCore_PropertyAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTCore_PropertyAssignment205", type=Property_, multiplicity=Multiplicity(1, 1))
    }
)
bottomPattern207: BinaryAssociation = BinaryAssociation(
    name="bottomPattern207",
    ends={
        Property(name="#209", type=QVTCore_RealizedVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="4208", type=BottomPattern, multiplicity=Multiplicity(1, 1))
    }
)
targetVariable210: BinaryAssociation = BinaryAssociation(
    name="targetVariable210",
    ends={
        Property(name="Variable211", type=QVTCore_VariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTCore_VariableAssignment", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
area187: BinaryAssociation = BinaryAssociation(
    name="area187",
    ends={
        Property(name="#189", type=QVTCore_GuardPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="4188", type=Area, multiplicity=Multiplicity(1, 1))
    }
)
context190: BinaryAssociation = BinaryAssociation(
    name="context190",
    ends={
        Property(name="#192", type=QVTCore_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="4191", type=Mapping, multiplicity=Multiplicity(0, 1))
    }
)
local193: BinaryAssociation = BinaryAssociation(
    name="local193",
    ends={
        Property(name="#195", type=QVTCore_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="4194", type=Mapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refinement196: BinaryAssociation = BinaryAssociation(
    name="refinement196",
    ends={
        Property(name="#198", type=QVTCore_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="4197", type=Mapping, multiplicity=Multiplicity(0, 9999))
    }
)
specification199: BinaryAssociation = BinaryAssociation(
    name="specification199",
    ends={
        Property(name="#201", type=QVTCore_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="4200", type=Mapping, multiplicity=Multiplicity(0, 9999))
    }
)
slotExpression202: BinaryAssociation = BinaryAssociation(
    name="slotExpression202",
    ends={
        Property(name="OclExpression203", type=QVTCore_PropertyAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTCore_PropertyAssignment", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referredClass221: BinaryAssociation = BinaryAssociation(
    name="referredClass221",
    ends={
        Property(name="Class222", type=QVTTemplate_ObjectTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTTemplate_ObjectTemplateExp", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
objContainer223: BinaryAssociation = BinaryAssociation(
    name="objContainer223",
    ends={
        Property(name="#225", type=QVTTemplate_PropertyTemplateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="5224", type=ObjectTemplateExp, multiplicity=Multiplicity(1, 1))
    }
)
referredProperty226: BinaryAssociation = BinaryAssociation(
    name="referredProperty226",
    ends={
        Property(name="Property227", type=QVTTemplate_PropertyTemplateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTTemplate_PropertyTemplateItem", type=Property_, multiplicity=Multiplicity(1, 1))
    }
)
value228: BinaryAssociation = BinaryAssociation(
    name="value228",
    ends={
        Property(name="OclExpression230", type=QVTTemplate_PropertyTemplateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTTemplate_PropertyTemplateItem229", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
member212: BinaryAssociation = BinaryAssociation(
    name="member212",
    ends={
        Property(name="OclExpression213", type=QVTTemplate_CollectionTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTTemplate_CollectionTemplateExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredCollectionType214: BinaryAssociation = BinaryAssociation(
    name="referredCollectionType214",
    ends={
        Property(name="CollectionType", type=QVTTemplate_CollectionTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTTemplate_CollectionTemplateExp215", type=CollectionType, multiplicity=Multiplicity(1, 1))
    }
)
rest216: BinaryAssociation = BinaryAssociation(
    name="rest216",
    ends={
        Property(name="Variable218", type=QVTTemplate_CollectionTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTTemplate_CollectionTemplateExp217", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
part219: BinaryAssociation = BinaryAssociation(
    name="part219",
    ends={
        Property(name="#220", type=QVTTemplate_ObjectTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="5", type=PropertyTemplateItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identifies239: BinaryAssociation = BinaryAssociation(
    name="identifies239",
    ends={
        Property(name="Class240", type=QVTRelation_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_Key", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
oppositePart241: BinaryAssociation = BinaryAssociation(
    name="oppositePart241",
    ends={
        Property(name="Property243", type=QVTRelation_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_Key242", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)
part244: BinaryAssociation = BinaryAssociation(
    name="part244",
    ends={
        Property(name="Property246", type=QVTRelation_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_Key245", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)
bindsTo231: BinaryAssociation = BinaryAssociation(
    name="bindsTo231",
    ends={
        Property(name="Variable232", type=QVTTemplate_TemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTTemplate_TemplateExp", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
where233: BinaryAssociation = BinaryAssociation(
    name="where233",
    ends={
        Property(name="OclExpression235", type=QVTTemplate_TemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTTemplate_TemplateExp234", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
relationDomain236: BinaryAssociation = BinaryAssociation(
    name="relationDomain236",
    ends={
        Property(name="#237", type=QVTRelation_DomainPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="6", type=RelationDomain, multiplicity=Multiplicity(1, 1))
    }
)
templateExpression238: BinaryAssociation = BinaryAssociation(
    name="templateExpression238",
    ends={
        Property(name="TemplateExp", type=QVTRelation_DomainPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_DomainPattern", type=TemplateExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
argument260: BinaryAssociation = BinaryAssociation(
    name="argument260",
    ends={
        Property(name="OclExpression261", type=QVTRelation_RelationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_RelationCallExp", type=OclExpression, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
referredRelation262: BinaryAssociation = BinaryAssociation(
    name="referredRelation262",
    ends={
        Property(name="Relation", type=QVTRelation_RelationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_RelationCallExp263", type=Relation, multiplicity=Multiplicity(1, 1))
    }
)
transformation247: BinaryAssociation = BinaryAssociation(
    name="transformation247",
    ends={
        Property(name="#249", type=QVTRelation_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="6248", type=RelationalTransformation, multiplicity=Multiplicity(0, 1))
    }
)
operationalImpl250: BinaryAssociation = BinaryAssociation(
    name="operationalImpl250",
    ends={
        Property(name="#252", type=QVTRelation_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="6251", type=RelationImplementation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable253: BinaryAssociation = BinaryAssociation(
    name="variable253",
    ends={
        Property(name="Variable254", type=QVTRelation_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_Relation", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
when255: BinaryAssociation = BinaryAssociation(
    name="when255",
    ends={
        Property(name="Pattern", type=QVTRelation_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_Relation256", type=Pattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
where257: BinaryAssociation = BinaryAssociation(
    name="where257",
    ends={
        Property(name="Pattern259", type=QVTRelation_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_Relation258", type=Pattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
impl280: BinaryAssociation = BinaryAssociation(
    name="impl280",
    ends={
        Property(name="Operation281", type=QVTRelation_RelationImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_RelationImplementation", type=Operation, multiplicity=Multiplicity(1, 1))
    }
)
inDirectionOf282: BinaryAssociation = BinaryAssociation(
    name="inDirectionOf282",
    ends={
        Property(name="TypedModel284", type=QVTRelation_RelationImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_RelationImplementation283", type=TypedModel, multiplicity=Multiplicity(1, 1))
    }
)
defaultAssignment264: BinaryAssociation = BinaryAssociation(
    name="defaultAssignment264",
    ends={
        Property(name="#266", type=QVTRelation_RelationDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="6265", type=RelationDomainAssignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pattern267: BinaryAssociation = BinaryAssociation(
    name="pattern267",
    ends={
        Property(name="#269", type=QVTRelation_RelationDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="6268", type=DomainPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rootVariable270: BinaryAssociation = BinaryAssociation(
    name="rootVariable270",
    ends={
        Property(name="Variable271", type=QVTRelation_RelationDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_RelationDomain", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
owner272: BinaryAssociation = BinaryAssociation(
    name="owner272",
    ends={
        Property(name="#274", type=QVTRelation_RelationDomainAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="6273", type=RelationDomain, multiplicity=Multiplicity(1, 1))
    }
)
valueExp275: BinaryAssociation = BinaryAssociation(
    name="valueExp275",
    ends={
        Property(name="OclExpression276", type=QVTRelation_RelationDomainAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_RelationDomainAssignment", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable277: BinaryAssociation = BinaryAssociation(
    name="variable277",
    ends={
        Property(name="Variable279", type=QVTRelation_RelationDomainAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_RelationDomainAssignment278", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
assertion296: BinaryAssociation = BinaryAssociation(
    name="assertion296",
    ends={
        Property(name="OclExpression297", type=ImperativeOCL_AssertExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_AssertExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
log298: BinaryAssociation = BinaryAssociation(
    name="log298",
    ends={
        Property(name="LogExp", type=ImperativeOCL_AssertExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_AssertExp299", type=LogExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultValue300: BinaryAssociation = BinaryAssociation(
    name="defaultValue300",
    ends={
        Property(name="OclExpression301", type=ImperativeOCL_AssignExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_AssignExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
relation285: BinaryAssociation = BinaryAssociation(
    name="relation285",
    ends={
        Property(name="#287", type=QVTRelation_RelationImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="6286", type=Relation, multiplicity=Multiplicity(1, 1))
    }
)
ownedKey288: BinaryAssociation = BinaryAssociation(
    name="ownedKey288",
    ends={
        Property(name="#290", type=QVTRelation_RelationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="6289", type=Key, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body291: BinaryAssociation = BinaryAssociation(
    name="body291",
    ends={
        Property(name="OclExpression292", type=ImperativeOCL_AltExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_AltExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition293: BinaryAssociation = BinaryAssociation(
    name="condition293",
    ends={
        Property(name="OclExpression295", type=ImperativeOCL_AltExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_AltExp294", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body310: BinaryAssociation = BinaryAssociation(
    name="body310",
    ends={
        Property(name="OclExpression311", type=ImperativeOCL_CatchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_CatchExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exception312: BinaryAssociation = BinaryAssociation(
    name="exception312",
    ends={
        Property(name="Type314", type=ImperativeOCL_CatchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_CatchExp313", type=Type, multiplicity=Multiplicity(1, 9999))
    }
)
exceptionVariable315: BinaryAssociation = BinaryAssociation(
    name="exceptionVariable315",
    ends={
        Property(name="Variable317", type=ImperativeOCL_CatchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_CatchExp316", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left302: BinaryAssociation = BinaryAssociation(
    name="left302",
    ends={
        Property(name="OclExpression304", type=ImperativeOCL_AssignExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_AssignExp303", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value305: BinaryAssociation = BinaryAssociation(
    name="value305",
    ends={
        Property(name="OclExpression307", type=ImperativeOCL_AssignExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_AssignExp306", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body308: BinaryAssociation = BinaryAssociation(
    name="body308",
    ends={
        Property(name="OclExpression309", type=ImperativeOCL_BlockExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_BlockExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key325: BinaryAssociation = BinaryAssociation(
    name="key325",
    ends={
        Property(name="ImperativeOCL_DictLiteralPart", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="OclExpression326", type=ImperativeOCL_DictLiteralPart, multiplicity=Multiplicity(1, 1))
    }
)
value327: BinaryAssociation = BinaryAssociation(
    name="value327",
    ends={
        Property(name="OclExpression329", type=ImperativeOCL_DictLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_DictLiteralPart328", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
partOwner330: BinaryAssociation = BinaryAssociation(
    name="partOwner330",
    ends={
        Property(name="#332", type=ImperativeOCL_DictLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="7331", type=DictLiteralExp, multiplicity=Multiplicity(1, 1))
    }
)
keyType333: BinaryAssociation = BinaryAssociation(
    name="keyType333",
    ends={
        Property(name="Type334", type=ImperativeOCL_DictionaryType, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_DictionaryType", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
body318: BinaryAssociation = BinaryAssociation(
    name="body318",
    ends={
        Property(name="OclExpression319", type=ImperativeOCL_ComputeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_ComputeExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnedElement320: BinaryAssociation = BinaryAssociation(
    name="returnedElement320",
    ends={
        Property(name="Variable322", type=ImperativeOCL_ComputeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_ComputeExp321", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
part323: BinaryAssociation = BinaryAssociation(
    name="part323",
    ends={
        Property(name="#324", type=ImperativeOCL_DictLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="7", type=DictLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument339: BinaryAssociation = BinaryAssociation(
    name="argument339",
    ends={
        Property(name="OclExpression340", type=ImperativeOCL_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_InstantiationExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extent341: BinaryAssociation = BinaryAssociation(
    name="extent341",
    ends={
        Property(name="Variable343", type=ImperativeOCL_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_InstantiationExp342", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
instantiatedClass344: BinaryAssociation = BinaryAssociation(
    name="instantiatedClass344",
    ends={
        Property(name="Class346", type=ImperativeOCL_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_InstantiationExp345", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
target335: BinaryAssociation = BinaryAssociation(
    name="target335",
    ends={
        Property(name="Variable336", type=ImperativeOCL_ImperativeIterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_ImperativeIterateExp", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition337: BinaryAssociation = BinaryAssociation(
    name="condition337",
    ends={
        Property(name="OclExpression338", type=ImperativeOCL_ImperativeLoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_ImperativeLoopExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition352: BinaryAssociation = BinaryAssociation(
    name="condition352",
    ends={
        Property(name="OclExpression353", type=ImperativeOCL_LogExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_LogExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initializationOperation347: BinaryAssociation = BinaryAssociation(
    name="initializationOperation347",
    ends={
        Property(name="Operation349", type=ImperativeOCL_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_InstantiationExp348", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
element350: BinaryAssociation = BinaryAssociation(
    name="element350",
    ends={
        Property(name="OclExpression351", type=ImperativeOCL_ListLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_ListLiteralExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
alternativePart361: BinaryAssociation = BinaryAssociation(
    name="alternativePart361",
    ends={
        Property(name="AltExp", type=ImperativeOCL_SwitchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_SwitchExp", type=AltExp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument354: BinaryAssociation = BinaryAssociation(
    name="argument354",
    ends={
        Property(name="OclExpression355", type=ImperativeOCL_RaiseExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_RaiseExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exception356: BinaryAssociation = BinaryAssociation(
    name="exception356",
    ends={
        Property(name="Type358", type=ImperativeOCL_RaiseExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_RaiseExp357", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
value359: BinaryAssociation = BinaryAssociation(
    name="value359",
    ends={
        Property(name="OclExpression360", type=ImperativeOCL_ReturnExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_ReturnExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exceptClause365: BinaryAssociation = BinaryAssociation(
    name="exceptClause365",
    ends={
        Property(name="CatchExp", type=ImperativeOCL_TryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_TryExp", type=CatchExp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tryBody366: BinaryAssociation = BinaryAssociation(
    name="tryBody366",
    ends={
        Property(name="OclExpression368", type=ImperativeOCL_TryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_TryExp367", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
base369: BinaryAssociation = BinaryAssociation(
    name="base369",
    ends={
        Property(name="Type370", type=ImperativeOCL_Typedef, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_Typedef", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
elsePart362: BinaryAssociation = BinaryAssociation(
    name="elsePart362",
    ends={
        Property(name="OclExpression364", type=ImperativeOCL_SwitchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_SwitchExp363", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target376: BinaryAssociation = BinaryAssociation(
    name="target376",
    ends={
        Property(name="OclExpression378", type=ImperativeOCL_UnlinkExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_UnlinkExp377", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referredVariable379: BinaryAssociation = BinaryAssociation(
    name="referredVariable379",
    ends={
        Property(name="Variable380", type=ImperativeOCL_VariableInitExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_VariableInitExp", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition371: BinaryAssociation = BinaryAssociation(
    name="condition371",
    ends={
        Property(name="OclExpression373", type=ImperativeOCL_Typedef, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_Typedef372", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
item374: BinaryAssociation = BinaryAssociation(
    name="item374",
    ends={
        Property(name="OclExpression375", type=ImperativeOCL_UnlinkExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_UnlinkExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context386: BinaryAssociation = BinaryAssociation(
    name="context386",
    ends={
        Property(name="Class387", type=QVTOperational_ContextualProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ContextualProperty", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
initExpression388: BinaryAssociation = BinaryAssociation(
    name="initExpression388",
    ends={
        Property(name="OclExpression390", type=QVTOperational_ContextualProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ContextualProperty389", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body381: BinaryAssociation = BinaryAssociation(
    name="body381",
    ends={
        Property(name="OclExpression382", type=ImperativeOCL_WhileExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_WhileExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition383: BinaryAssociation = BinaryAssociation(
    name="condition383",
    ends={
        Property(name="OclExpression385", type=ImperativeOCL_WhileExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_WhileExp384", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
overridden391: BinaryAssociation = BinaryAssociation(
    name="overridden391",
    ends={
        Property(name="Property393", type=QVTOperational_ContextualProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ContextualProperty392", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
overridden399: BinaryAssociation = BinaryAssociation(
    name="overridden399",
    ends={
        Property(name="ImperativeOperation", type=QVTOperational_ImperativeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ImperativeOperation", type=ImperativeOperation, multiplicity=Multiplicity(0, 1))
    }
)
result400: BinaryAssociation = BinaryAssociation(
    name="result400",
    ends={
        Property(name="#402", type=QVTOperational_ImperativeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="8401", type=VarParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body394: BinaryAssociation = BinaryAssociation(
    name="body394",
    ends={
        Property(name="#395", type=QVTOperational_ImperativeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="8", type=OperationBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
context396: BinaryAssociation = BinaryAssociation(
    name="context396",
    ends={
        Property(name="#398", type=QVTOperational_ImperativeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="8397", type=VarParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
disjunct408: BinaryAssociation = BinaryAssociation(
    name="disjunct408",
    ends={
        Property(name="MappingOperation", type=QVTOperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingOperation", type=MappingOperation, multiplicity=Multiplicity(0, 9999))
    }
)
inherited409: BinaryAssociation = BinaryAssociation(
    name="inherited409",
    ends={
        Property(name="MappingOperation411", type=QVTOperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingOperation410", type=MappingOperation, multiplicity=Multiplicity(0, 9999))
    }
)
endSection403: BinaryAssociation = BinaryAssociation(
    name="endSection403",
    ends={
        Property(name="OclExpression404", type=QVTOperational_MappingBody, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingBody", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initSection405: BinaryAssociation = BinaryAssociation(
    name="initSection405",
    ends={
        Property(name="OclExpression407", type=QVTOperational_MappingBody, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingBody406", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extent424: BinaryAssociation = BinaryAssociation(
    name="extent424",
    ends={
        Property(name="ModelParameter", type=QVTOperational_MappingParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingParameter", type=ModelParameter, multiplicity=Multiplicity(0, 1))
    }
)
merged412: BinaryAssociation = BinaryAssociation(
    name="merged412",
    ends={
        Property(name="MappingOperation414", type=QVTOperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingOperation413", type=MappingOperation, multiplicity=Multiplicity(0, 9999))
    }
)
refinedRelation415: BinaryAssociation = BinaryAssociation(
    name="refinedRelation415",
    ends={
        Property(name="Relation417", type=QVTOperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingOperation416", type=Relation, multiplicity=Multiplicity(0, 1))
    }
)
when418: BinaryAssociation = BinaryAssociation(
    name="when418",
    ends={
        Property(name="OclExpression420", type=QVTOperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingOperation419", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
where421: BinaryAssociation = BinaryAssociation(
    name="where421",
    ends={
        Property(name="OclExpression423", type=QVTOperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingOperation422", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
metamodel432: BinaryAssociation = BinaryAssociation(
    name="metamodel432",
    ends={
        Property(name="Package434", type=QVTOperational_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ModelType433", type=Package, multiplicity=Multiplicity(1, 9999))
    }
)
configProperty435: BinaryAssociation = BinaryAssociation(
    name="configProperty435",
    ends={
        Property(name="Property436", type=QVTOperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_Module", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)
referredDomain425: BinaryAssociation = BinaryAssociation(
    name="referredDomain425",
    ends={
        Property(name="RelationDomain", type=QVTOperational_MappingParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingParameter426", type=RelationDomain, multiplicity=Multiplicity(0, 1))
    }
)
module427: BinaryAssociation = BinaryAssociation(
    name="module427",
    ends={
        Property(name="#429", type=QVTOperational_ModelParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="8428", type=OperationalTransformation, multiplicity=Multiplicity(1, 1))
    }
)
additionalCondition430: BinaryAssociation = BinaryAssociation(
    name="additionalCondition430",
    ends={
        Property(name="OclExpression431", type=QVTOperational_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ModelType", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usedModelType448: BinaryAssociation = BinaryAssociation(
    name="usedModelType448",
    ends={
        Property(name="ModelType", type=QVTOperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_Module449", type=ModelType, multiplicity=Multiplicity(0, 9999))
    }
)
binding450: BinaryAssociation = BinaryAssociation(
    name="binding450",
    ends={
        Property(name="ModelType451", type=QVTOperational_ModuleImport, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ModuleImport", type=ModelType, multiplicity=Multiplicity(0, 9999))
    }
)
entry437: BinaryAssociation = BinaryAssociation(
    name="entry437",
    ends={
        Property(name="EntryOperation", type=QVTOperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_Module438", type=EntryOperation, multiplicity=Multiplicity(0, 1))
    }
)
moduleImport439: BinaryAssociation = BinaryAssociation(
    name="moduleImport439",
    ends={
        Property(name="#441", type=QVTOperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="8440", type=ModuleImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTag442: BinaryAssociation = BinaryAssociation(
    name="ownedTag442",
    ends={
        Property(name="Tag444", type=QVTOperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_Module443", type=Tag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVariable445: BinaryAssociation = BinaryAssociation(
    name="ownedVariable445",
    ends={
        Property(name="Variable447", type=QVTOperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_Module446", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredObject458: BinaryAssociation = BinaryAssociation(
    name="referredObject458",
    ends={
        Property(name="QVTOperational_ObjectExp459", type=Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="Variable460", type=QVTOperational_ObjectExp, multiplicity=Multiplicity(1, 1))
    }
)
content461: BinaryAssociation = BinaryAssociation(
    name="content461",
    ends={
        Property(name="OclExpression462", type=QVTOperational_OperationBody, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_OperationBody", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operation463: BinaryAssociation = BinaryAssociation(
    name="operation463",
    ends={
        Property(name="#465", type=QVTOperational_OperationBody, multiplicity=Multiplicity(1, 1)),
        Property(name="8464", type=ImperativeOperation, multiplicity=Multiplicity(0, 1))
    }
)
importedModule452: BinaryAssociation = BinaryAssociation(
    name="importedModule452",
    ends={
        Property(name="Module", type=QVTOperational_ModuleImport, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ModuleImport453", type=Module, multiplicity=Multiplicity(1, 1))
    }
)
module454: BinaryAssociation = BinaryAssociation(
    name="module454",
    ends={
        Property(name="#456", type=QVTOperational_ModuleImport, multiplicity=Multiplicity(1, 1)),
        Property(name="8455", type=Module, multiplicity=Multiplicity(0, 1))
    }
)
body457: BinaryAssociation = BinaryAssociation(
    name="body457",
    ends={
        Property(name="ConstructorBody", type=QVTOperational_ObjectExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ObjectExp", type=ConstructorBody, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
modelParameter474: BinaryAssociation = BinaryAssociation(
    name="modelParameter474",
    ends={
        Property(name="#476", type=QVTOperational_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="8475", type=ModelParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refined477: BinaryAssociation = BinaryAssociation(
    name="refined477",
    ends={
        Property(name="RelationalTransformation", type=QVTOperational_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_OperationalTransformation478", type=RelationalTransformation, multiplicity=Multiplicity(0, 1))
    }
)
relation479: BinaryAssociation = BinaryAssociation(
    name="relation479",
    ends={
        Property(name="Relation481", type=QVTOperational_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_OperationalTransformation480", type=Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable466: BinaryAssociation = BinaryAssociation(
    name="variable466",
    ends={
        Property(name="Variable468", type=QVTOperational_OperationBody, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_OperationBody467", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateClass469: BinaryAssociation = BinaryAssociation(
    name="intermediateClass469",
    ends={
        Property(name="Class470", type=QVTOperational_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_OperationalTransformation", type=Class_, multiplicity=Multiplicity(0, 9999))
    }
)
intermediateProperty471: BinaryAssociation = BinaryAssociation(
    name="intermediateProperty471",
    ends={
        Property(name="Property473", type=QVTOperational_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_OperationalTransformation472", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)
inMapping487: BinaryAssociation = BinaryAssociation(
    name="inMapping487",
    ends={
        Property(name="MappingOperation488", type=QVTOperational_ResolveInExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ResolveInExp", type=MappingOperation, multiplicity=Multiplicity(0, 1))
    }
)
ctxOwner489: BinaryAssociation = BinaryAssociation(
    name="ctxOwner489",
    ends={
        Property(name="#491", type=QVTOperational_VarParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="8490", type=ImperativeOperation, multiplicity=Multiplicity(0, 1))
    }
)
condition482: BinaryAssociation = BinaryAssociation(
    name="condition482",
    ends={
        Property(name="OclExpression483", type=QVTOperational_ResolveExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ResolveExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target484: BinaryAssociation = BinaryAssociation(
    name="target484",
    ends={
        Property(name="Variable486", type=QVTOperational_ResolveExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ResolveExp485", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resOwner492: BinaryAssociation = BinaryAssociation(
    name="resOwner492",
    ends={
        Property(name="#494", type=QVTOperational_VarParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="8493", type=ImperativeOperation, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_EMOF_Comment_Element = Generalization(general=Element, specific=EMOF_Comment)
gen_EMOF_DataType_Type = Generalization(general=Type, specific=EMOF_DataType)
gen_EMOF_Element_Object = Generalization(general=Object, specific=EMOF_Element)
gen_EMOF_Class_Type = Generalization(general=Type, specific=EMOF_Class)
gen_EMOF_EnumerationLiteral_NamedElement = Generalization(general=NamedElement, specific=EMOF_EnumerationLiteral)
gen_EMOF_Extent_Object = Generalization(general=Object, specific=EMOF_Extent)
gen_EMOF_Factory_Element = Generalization(general=Element, specific=EMOF_Factory)
gen_EMOF_Enumeration_DataType = Generalization(general=DataType, specific=EMOF_Enumeration)
gen_EMOF_Package_NamedElement = Generalization(general=NamedElement, specific=EMOF_Package)
gen_EMOF_Parameter_TypedElement = Generalization(general=TypedElement, specific=EMOF_Parameter)
gen_EMOF_NamedElement_Element = Generalization(general=Element, specific=EMOF_NamedElement)
gen_EMOF_Operation_TypedElement = Generalization(general=TypedElement, specific=EMOF_Operation)
gen_EMOF_Operation_MultiplicityElement = Generalization(general=MultiplicityElement, specific=EMOF_Operation)
gen_EMOF_ReflectiveSequence_ReflectiveCollection = Generalization(general=ReflectiveCollection, specific=EMOF_ReflectiveSequence)
gen_EMOF_Tag_Element = Generalization(general=Element, specific=EMOF_Tag)
gen_EMOF_Parameter_MultiplicityElement = Generalization(general=MultiplicityElement, specific=EMOF_Parameter)
gen_EMOF_PrimitiveType_DataType = Generalization(general=DataType, specific=EMOF_PrimitiveType)
gen_EMOF_Property_TypedElement = Generalization(general=TypedElement, specific=EMOF_Property)
gen_EMOF_Property_MultiplicityElement = Generalization(general=MultiplicityElement, specific=EMOF_Property)
gen_EMOF_ReflectiveCollection_Object = Generalization(general=Object, specific=EMOF_ReflectiveCollection)
gen_EssentialOCL_BooleanLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=EssentialOCL_BooleanLiteralExp)
gen_EssentialOCL_CallExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_CallExp)
gen_EssentialOCL_CollectionItem_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=EssentialOCL_CollectionItem)
gen_EMOF_Type_NamedElement = Generalization(general=NamedElement, specific=EMOF_Type)
gen_EMOF_TypedElement_NamedElement = Generalization(general=NamedElement, specific=EMOF_TypedElement)
gen_EMOF_URIExtent_Extent = Generalization(general=Extent, specific=EMOF_URIExtent)
gen_EssentialOCL_AnyType_Type = Generalization(general=Type, specific=EssentialOCL_AnyType)
gen_EssentialOCL_BagType_CollectionType = Generalization(general=CollectionType, specific=EssentialOCL_BagType)
gen_EssentialOCL_CollectionType_DataType = Generalization(general=DataType, specific=EssentialOCL_CollectionType)
gen_EssentialOCL_CollectionLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=EssentialOCL_CollectionLiteralExp)
gen_EssentialOCL_CollectionLiteralPart_TypedElement = Generalization(general=TypedElement, specific=EssentialOCL_CollectionLiteralPart)
gen_EssentialOCL_CollectionRange_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=EssentialOCL_CollectionRange)
gen_EssentialOCL_FeatureCallExp_CallExp = Generalization(general=CallExp, specific=EssentialOCL_FeatureCallExp)
gen_EssentialOCL_IfExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_IfExp)
gen_EssentialOCL_EnumLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=EssentialOCL_EnumLiteralExp)
gen_EssentialOCL_ExpressionInOcl_TypedElement = Generalization(general=TypedElement, specific=EssentialOCL_ExpressionInOcl)
gen_EssentialOCL_LoopExp_CallExp = Generalization(general=CallExp, specific=EssentialOCL_LoopExp)
gen_EssentialOCL_LoopExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_LoopExp)
gen_EssentialOCL_NavigationCallExp_FeatureCallExp = Generalization(general=FeatureCallExp, specific=EssentialOCL_NavigationCallExp)
gen_EssentialOCL_NullLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=EssentialOCL_NullLiteralExp)
gen_EssentialOCL_NumericLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=EssentialOCL_NumericLiteralExp)
gen_EssentialOCL_OclExpression_TypedElement = Generalization(general=TypedElement, specific=EssentialOCL_OclExpression)
gen_EssentialOCL_OperationCallExp_FeatureCallExp = Generalization(general=FeatureCallExp, specific=EssentialOCL_OperationCallExp)
gen_EssentialOCL_IntegerLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=EssentialOCL_IntegerLiteralExp)
gen_EssentialOCL_InvalidLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=EssentialOCL_InvalidLiteralExp)
gen_EssentialOCL_InvalidType_Type = Generalization(general=Type, specific=EssentialOCL_InvalidType)
gen_EssentialOCL_IterateExp_LoopExp = Generalization(general=LoopExp, specific=EssentialOCL_IterateExp)
gen_EssentialOCL_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=EssentialOCL_IteratorExp)
gen_EssentialOCL_LetExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_LetExp)
gen_EssentialOCL_LiteralExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_LiteralExp)
gen_EssentialOCL_TupleType_Class = Generalization(general=Class_, specific=EssentialOCL_TupleType)
gen_EssentialOCL_TupleType_DataType = Generalization(general=DataType, specific=EssentialOCL_TupleType)
gen_EssentialOCL_TypeExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_TypeExp)
gen_EssentialOCL_UnlimitedNaturalExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=EssentialOCL_UnlimitedNaturalExp)
gen_EssentialOCL_Variable_TypedElement = Generalization(general=TypedElement, specific=EssentialOCL_Variable)
gen_EssentialOCL_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=EssentialOCL_OrderedSetType)
gen_EssentialOCL_PrimitiveLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=EssentialOCL_PrimitiveLiteralExp)
gen_EssentialOCL_PropertyCallExp_NavigationCallExp = Generalization(general=NavigationCallExp, specific=EssentialOCL_PropertyCallExp)
gen_EssentialOCL_RealLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=EssentialOCL_RealLiteralExp)
gen_EssentialOCL_SequenceType_CollectionType = Generalization(general=CollectionType, specific=EssentialOCL_SequenceType)
gen_EssentialOCL_SetType_CollectionType = Generalization(general=CollectionType, specific=EssentialOCL_SetType)
gen_EssentialOCL_StringLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=EssentialOCL_StringLiteralExp)
gen_EssentialOCL_TemplateParameterType_Type = Generalization(general=Type, specific=EssentialOCL_TemplateParameterType)
gen_EssentialOCL_TupleLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=EssentialOCL_TupleLiteralExp)
gen_EssentialOCL_TupleLiteralPart_TypedElement = Generalization(general=TypedElement, specific=EssentialOCL_TupleLiteralPart)
gen_QVTBase_Function_Operation = Generalization(general=Operation, specific=QVTBase_Function)
gen_QVTBase_FunctionParameter_Variable = Generalization(general=Variable, specific=QVTBase_FunctionParameter)
gen_QVTBase_FunctionParameter_Parameter = Generalization(general=Parameter_, specific=QVTBase_FunctionParameter)
gen_QVTBase_Pattern_Element = Generalization(general=Element, specific=QVTBase_Pattern)
gen_EssentialOCL_VariableExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_VariableExp)
gen_EssentialOCL_VoidType_Type = Generalization(general=Type, specific=EssentialOCL_VoidType)
gen_QVTBase_Domain_NamedElement = Generalization(general=NamedElement, specific=QVTBase_Domain)
gen_QVTBase_Transformation_Class = Generalization(general=Class_, specific=QVTBase_Transformation)
gen_QVTBase_Transformation_Package = Generalization(general=Package, specific=QVTBase_Transformation)
gen_QVTBase_Predicate_Element = Generalization(general=Element, specific=QVTBase_Predicate)
gen_QVTBase_Rule_NamedElement = Generalization(general=NamedElement, specific=QVTBase_Rule)
gen_QVTCore_Assignment_Element = Generalization(general=Element, specific=QVTCore_Assignment)
gen_QVTBase_TypedModel_NamedElement = Generalization(general=NamedElement, specific=QVTBase_TypedModel)
gen_QVTCore_EnforcementOperation_Element = Generalization(general=Element, specific=QVTCore_EnforcementOperation)
gen_QVTCore_BottomPattern_CorePattern = Generalization(general=CorePattern, specific=QVTCore_BottomPattern)
gen_QVTCore_CoreDomain_Domain = Generalization(general=Domain, specific=QVTCore_CoreDomain)
gen_QVTCore_CoreDomain_Area = Generalization(general=Area, specific=QVTCore_CoreDomain)
gen_QVTCore_CorePattern_Pattern = Generalization(general=Pattern, specific=QVTCore_CorePattern)
gen_QVTCore_RealizedVariable_Variable = Generalization(general=Variable, specific=QVTCore_RealizedVariable)
gen_QVTCore_VariableAssignment_Assignment = Generalization(general=Assignment, specific=QVTCore_VariableAssignment)
gen_QVTCore_GuardPattern_CorePattern = Generalization(general=CorePattern, specific=QVTCore_GuardPattern)
gen_QVTCore_Mapping_Rule = Generalization(general=Rule, specific=QVTCore_Mapping)
gen_QVTCore_Mapping_Area = Generalization(general=Area, specific=QVTCore_Mapping)
gen_QVTCore_PropertyAssignment_Assignment = Generalization(general=Assignment, specific=QVTCore_PropertyAssignment)
gen_QVTTemplate_PropertyTemplateItem_Element = Generalization(general=Element, specific=QVTTemplate_PropertyTemplateItem)
gen_QVTTemplate_CollectionTemplateExp_TemplateExp = Generalization(general=TemplateExp, specific=QVTTemplate_CollectionTemplateExp)
gen_QVTTemplate_ObjectTemplateExp_TemplateExp = Generalization(general=TemplateExp, specific=QVTTemplate_ObjectTemplateExp)
gen_QVTRelation_Key_Element = Generalization(general=Element, specific=QVTRelation_Key)
gen_QVTTemplate_TemplateExp_LiteralExp = Generalization(general=LiteralExp, specific=QVTTemplate_TemplateExp)
gen_QVTRelation_DomainPattern_Pattern = Generalization(general=Pattern, specific=QVTRelation_DomainPattern)
gen_QVTRelation_RelationCallExp_OclExpression = Generalization(general=OclExpression, specific=QVTRelation_RelationCallExp)
gen_QVTRelation_RelationDomain_Domain = Generalization(general=Domain, specific=QVTRelation_RelationDomain)
gen_QVTRelation_OppositePropertyCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=QVTRelation_OppositePropertyCallExp)
gen_QVTRelation_Relation_Rule = Generalization(general=Rule, specific=QVTRelation_Relation)
gen_QVTRelation_RelationImplementation_Element = Generalization(general=Element, specific=QVTRelation_RelationImplementation)
gen_QVTRelation_RelationDomainAssignment_Element = Generalization(general=Element, specific=QVTRelation_RelationDomainAssignment)
gen_ImperativeOCL_AssignExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_AssignExp)
gen_QVTRelation_RelationalTransformation_Transformation = Generalization(general=Transformation, specific=QVTRelation_RelationalTransformation)
gen_ImperativeOCL_AltExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_AltExp)
gen_ImperativeOCL_AssertExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_AssertExp)
gen_ImperativeOCL_BreakExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_BreakExp)
gen_ImperativeOCL_CatchExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_CatchExp)
gen_ImperativeOCL_BlockExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_BlockExp)
gen_ImperativeOCL_DictionaryType_CollectionType = Generalization(general=CollectionType, specific=ImperativeOCL_DictionaryType)
gen_ImperativeOCL_ComputeExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_ComputeExp)
gen_ImperativeOCL_ContinueExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_ContinueExp)
gen_ImperativeOCL_DictLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=ImperativeOCL_DictLiteralExp)
gen_ImperativeOCL_DictLiteralPart_Element = Generalization(general=Element, specific=ImperativeOCL_DictLiteralPart)
gen_ImperativeOCL_InstantiationExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_InstantiationExp)
gen_ImperativeOCL_ForExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=ImperativeOCL_ForExp)
gen_ImperativeOCL_ImperativeExpression_OclExpression = Generalization(general=OclExpression, specific=ImperativeOCL_ImperativeExpression)
gen_ImperativeOCL_ImperativeIterateExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=ImperativeOCL_ImperativeIterateExp)
gen_ImperativeOCL_ImperativeLoopExp_LoopExp = Generalization(general=LoopExp, specific=ImperativeOCL_ImperativeLoopExp)
gen_ImperativeOCL_ImperativeLoopExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_ImperativeLoopExp)
gen_ImperativeOCL_LogExp_OperationCallExp = Generalization(general=OperationCallExp, specific=ImperativeOCL_LogExp)
gen_ImperativeOCL_LogExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_LogExp)
gen_ImperativeOCL_ListLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=ImperativeOCL_ListLiteralExp)
gen_ImperativeOCL_ListType_CollectionType = Generalization(general=CollectionType, specific=ImperativeOCL_ListType)
gen_ImperativeOCL_SwitchExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_SwitchExp)
gen_ImperativeOCL_RaiseExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_RaiseExp)
gen_ImperativeOCL_ReturnExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_ReturnExp)
gen_ImperativeOCL_Typedef_Class = Generalization(general=Class_, specific=ImperativeOCL_Typedef)
gen_ImperativeOCL_TryExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_TryExp)
gen_ImperativeOCL_VariableInitExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_VariableInitExp)
gen_ImperativeOCL_WhileExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_WhileExp)
gen_ImperativeOCL_UnlinkExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_UnlinkExp)
gen_QVTOperational_Constructor_ImperativeOperation = Generalization(general=ImperativeOperation, specific=QVTOperational_Constructor)
gen_QVTOperational_ConstructorBody_OperationBody = Generalization(general=OperationBody, specific=QVTOperational_ConstructorBody)
gen_QVTOperational_ContextualProperty_Property = Generalization(general=Property_, specific=QVTOperational_ContextualProperty)
gen_QVTOperational_Helper_ImperativeOperation = Generalization(general=ImperativeOperation, specific=QVTOperational_Helper)
gen_QVTOperational_ImperativeCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=QVTOperational_ImperativeCallExp)
gen_QVTOperational_ImperativeCallExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=QVTOperational_ImperativeCallExp)
gen_QVTOperational_EntryOperation_ImperativeOperation = Generalization(general=ImperativeOperation, specific=QVTOperational_EntryOperation)
gen_QVTOperational_ImperativeOperation_Operation = Generalization(general=Operation, specific=QVTOperational_ImperativeOperation)
gen_QVTOperational_MappingCallExp_ImperativeCallExp = Generalization(general=ImperativeCallExp, specific=QVTOperational_MappingCallExp)
gen_QVTOperational_MappingOperation_ImperativeOperation = Generalization(general=ImperativeOperation, specific=QVTOperational_MappingOperation)
gen_QVTOperational_Library_Module = Generalization(general=Module, specific=QVTOperational_Library)
gen_QVTOperational_MappingBody_OperationBody = Generalization(general=OperationBody, specific=QVTOperational_MappingBody)
gen_QVTOperational_MappingParameter_VarParameter = Generalization(general=VarParameter, specific=QVTOperational_MappingParameter)
gen_QVTOperational_Module_Class = Generalization(general=Class_, specific=QVTOperational_Module)
gen_QVTOperational_Module_Package = Generalization(general=Package, specific=QVTOperational_Module)
gen_QVTOperational_ModelParameter_VarParameter = Generalization(general=VarParameter, specific=QVTOperational_ModelParameter)
gen_QVTOperational_ModelType_Class = Generalization(general=Class_, specific=QVTOperational_ModelType)
gen_QVTOperational_ModuleImport_Element = Generalization(general=Element, specific=QVTOperational_ModuleImport)
gen_QVTOperational_OperationBody_Element = Generalization(general=Element, specific=QVTOperational_OperationBody)
gen_QVTOperational_ObjectExp_InstantiationExp = Generalization(general=InstantiationExp, specific=QVTOperational_ObjectExp)
gen_QVTOperational_OperationalTransformation_Module = Generalization(general=Module, specific=QVTOperational_OperationalTransformation)
gen_QVTOperational_ResolveInExp_ResolveExp = Generalization(general=ResolveExp, specific=QVTOperational_ResolveInExp)
gen_QVTOperational_VarParameter_Variable = Generalization(general=Variable, specific=QVTOperational_VarParameter)
gen_QVTOperational_VarParameter_Parameter = Generalization(general=Parameter_, specific=QVTOperational_VarParameter)
gen_QVTOperational_ResolveExp_CallExp = Generalization(general=CallExp, specific=QVTOperational_ResolveExp)
gen_QVTOperational_ResolveExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=QVTOperational_ResolveExp)

# Domain Model
domain_model = DomainModel(
    name="QVTOperational",
    types={Class_, EMOF_Comment, Element, NamedElement, EMOF_DataType, EMOF_Element, Object, EMOF_Class, Type, Property_, Operation, Enumeration_, EMOF_Extent, EMOF_Factory, Package, Comment, EMOF_Enumeration, DataType, EnumerationLiteral, EMOF_EnumerationLiteral, EMOF_Package, EMOF_Parameter, EMOF_MultiplicityElement, EMOF_NamedElement, EMOF_Object, EMOF_Operation, TypedElement, MultiplicityElement, Parameter_, EMOF_ReflectiveSequence, ReflectiveCollection, EMOF_Tag, EMOF_PrimitiveType, EMOF_Property, EMOF_ReflectiveCollection, EssentialOCL_BooleanLiteralExp, PrimitiveLiteralExp, EssentialOCL_CallExp, OclExpression, EssentialOCL_CollectionItem, CollectionLiteralPart, EMOF_Type, EMOF_TypedElement, EMOF_URIExtent, Extent, EssentialOCL_AnyType, EssentialOCL_BagType, CollectionType, EssentialOCL_CollectionType, EssentialOCL_CollectionLiteralExp, LiteralExp, EssentialOCL_CollectionLiteralPart, CollectionLiteralExp, EssentialOCL_CollectionRange, EssentialOCL_FeatureCallExp, CallExp, EssentialOCL_IfExp, EssentialOCL_EnumLiteralExp, EssentialOCL_ExpressionInOcl, Variable, EssentialOCL_LoopExp, EssentialOCL_NavigationCallExp, FeatureCallExp, EssentialOCL_NullLiteralExp, EssentialOCL_NumericLiteralExp, EssentialOCL_OclExpression, EssentialOCL_OperationCallExp, EssentialOCL_IntegerLiteralExp, NumericLiteralExp, EssentialOCL_InvalidLiteralExp, EssentialOCL_InvalidType, EssentialOCL_IterateExp, LoopExp, EssentialOCL_IteratorExp, EssentialOCL_LetExp, EssentialOCL_LiteralExp, TupleLiteralExp, EssentialOCL_TupleType, EssentialOCL_TypeExp, EssentialOCL_UnlimitedNaturalExp, EssentialOCL_Variable, EssentialOCL_OrderedSetType, EssentialOCL_PrimitiveLiteralExp, EssentialOCL_PropertyCallExp, NavigationCallExp, EssentialOCL_RealLiteralExp, EssentialOCL_SequenceType, EssentialOCL_SetType, EssentialOCL_StringLiteralExp, EssentialOCL_TemplateParameterType, EssentialOCL_TupleLiteralExp, TupleLiteralPart, EssentialOCL_TupleLiteralPart, TypedModel, QVTBase_Function, QVTBase_FunctionParameter, QVTBase_Pattern, LetExp, EssentialOCL_VariableExp, EssentialOCL_VoidType, QVTBase_Domain, Rule, Transformation, QVTBase_Transformation, Predicate, QVTBase_Predicate, Pattern, QVTBase_Rule, Domain, QVTCore_Area, BottomPattern, GuardPattern, QVTCore_Assignment, Tag, QVTBase_TypedModel, QVTCore_EnforcementOperation, OperationCallExp, QVTCore_GuardPattern, QVTCore_BottomPattern, CorePattern, Area, Assignment, EnforcementOperation, RealizedVariable, QVTCore_CoreDomain, QVTCore_CorePattern, QVTCore_RealizedVariable, QVTCore_VariableAssignment, QVTCore_Mapping, Mapping, QVTCore_PropertyAssignment, QVTTemplate_PropertyTemplateItem, ObjectTemplateExp, QVTTemplate_CollectionTemplateExp, TemplateExp, QVTTemplate_ObjectTemplateExp, PropertyTemplateItem, QVTRelation_Key, RelationalTransformation, QVTTemplate_TemplateExp, QVTRelation_DomainPattern, RelationDomain, QVTRelation_RelationCallExp, Relation, QVTRelation_RelationDomain, QVTRelation_OppositePropertyCallExp, PropertyCallExp, QVTRelation_Relation, RelationImplementation, QVTRelation_RelationImplementation, RelationDomainAssignment, DomainPattern, QVTRelation_RelationDomainAssignment, LogExp, ImperativeOCL_AssignExp, QVTRelation_RelationalTransformation, Key, ImperativeOCL_AltExp, ImperativeExpression, ImperativeOCL_AssertExp, ImperativeOCL_BreakExp, ImperativeOCL_CatchExp, ImperativeOCL_BlockExp, DictLiteralExp, ImperativeOCL_DictionaryType, ImperativeOCL_ComputeExp, ImperativeOCL_ContinueExp, ImperativeOCL_DictLiteralExp, DictLiteralPart, ImperativeOCL_DictLiteralPart, ImperativeOCL_InstantiationExp, ImperativeOCL_ForExp, ImperativeLoopExp, ImperativeOCL_ImperativeExpression, ImperativeOCL_ImperativeIterateExp, ImperativeOCL_ImperativeLoopExp, ImperativeOCL_LogExp, ImperativeOCL_ListLiteralExp, ImperativeOCL_ListType, ImperativeOCL_SwitchExp, AltExp, ImperativeOCL_RaiseExp, ImperativeOCL_ReturnExp, CatchExp, ImperativeOCL_Typedef, ImperativeOCL_TryExp, ImperativeOCL_VariableInitExp, ImperativeOCL_WhileExp, ImperativeOCL_UnlinkExp, QVTOperational_Constructor, ImperativeOperation, QVTOperational_ConstructorBody, OperationBody, QVTOperational_ContextualProperty, QVTOperational_Helper, QVTOperational_ImperativeCallExp, QVTOperational_EntryOperation, QVTOperational_ImperativeOperation, VarParameter, QVTOperational_MappingCallExp, ImperativeCallExp, QVTOperational_MappingOperation, MappingOperation, QVTOperational_Library, Module, QVTOperational_MappingBody, QVTOperational_MappingParameter, ModelParameter, QVTOperational_Module, QVTOperational_ModelParameter, OperationalTransformation, QVTOperational_ModelType, ModelType, QVTOperational_ModuleImport, EntryOperation, ModuleImport, QVTOperational_OperationBody, QVTOperational_ObjectExp, InstantiationExp, ConstructorBody, QVTOperational_OperationalTransformation, QVTOperational_ResolveInExp, ResolveExp, QVTOperational_VarParameter, QVTOperational_ResolveExp, CollectionKind, EnforcementMode, SeverityKind, DirectionKind, ImportKind},
    associations={superClass4, annotatedElement5, ownedAttribute0, ownedOperation1, enumeration10, package13, ownedComment6, ownedLiteral7, raisedException20, nestedPackage21, nestingPackage24, ownedType27, class14, ownedParameter17, element37, operation30, class33, opposite36, source43, item44, package38, type41, last53, elementType56, part46, collectionLiteralExp48, first51, parameterVariable66, resultVariable69, condition72, elseExpression74, referredEnumLiteral58, bodyExpression59, contextVariable61, generatedType63, body87, iterator89, argument92, referredOperation94, thenExpression77, result80, in82, variable84, tupleLiteralExp103, value106, referredType109, initExpression111, referredProperty96, part98, attribute101, typedModel122, queryExpression123, bindsTo125, letExp113, representedParameter116, referredVariable118, rule120, overrides138, transformation139, extends142, modelParameter143, predicate127, conditionExpression130, pattern132, domain135, bottomPattern159, guardPattern161, bottomPattern164, value167, ownedTag146, rule148, dependsOn151, transformation153, usedPackage156, variable181, bottomPattern183, operationCallExp186, area169, assignment172, enforcementOperation175, realizedVariable178, targetProperty204, bottomPattern207, targetVariable210, area187, context190, local193, refinement196, specification199, slotExpression202, referredClass221, objContainer223, referredProperty226, value228, member212, referredCollectionType214, rest216, part219, identifies239, oppositePart241, part244, bindsTo231, where233, relationDomain236, templateExpression238, argument260, referredRelation262, transformation247, operationalImpl250, variable253, when255, where257, impl280, inDirectionOf282, defaultAssignment264, pattern267, rootVariable270, owner272, valueExp275, variable277, assertion296, log298, defaultValue300, relation285, ownedKey288, body291, condition293, body310, exception312, exceptionVariable315, left302, value305, body308, key325, value327, partOwner330, keyType333, body318, returnedElement320, part323, argument339, extent341, instantiatedClass344, target335, condition337, condition352, initializationOperation347, element350, alternativePart361, argument354, exception356, value359, exceptClause365, tryBody366, base369, elsePart362, target376, referredVariable379, condition371, item374, context386, initExpression388, body381, condition383, overridden391, overridden399, result400, body394, context396, disjunct408, inherited409, endSection403, initSection405, extent424, merged412, refinedRelation415, when418, where421, metamodel432, configProperty435, referredDomain425, module427, additionalCondition430, usedModelType448, binding450, entry437, moduleImport439, ownedTag442, ownedVariable445, referredObject458, content461, operation463, importedModule452, module454, body457, modelParameter474, refined477, relation479, variable466, intermediateClass469, intermediateProperty471, inMapping487, ctxOwner489, condition482, target484, resOwner492},
    generalizations={gen_EMOF_Comment_Element, gen_EMOF_DataType_Type, gen_EMOF_Element_Object, gen_EMOF_Class_Type, gen_EMOF_EnumerationLiteral_NamedElement, gen_EMOF_Extent_Object, gen_EMOF_Factory_Element, gen_EMOF_Enumeration_DataType, gen_EMOF_Package_NamedElement, gen_EMOF_Parameter_TypedElement, gen_EMOF_NamedElement_Element, gen_EMOF_Operation_TypedElement, gen_EMOF_Operation_MultiplicityElement, gen_EMOF_ReflectiveSequence_ReflectiveCollection, gen_EMOF_Tag_Element, gen_EMOF_Parameter_MultiplicityElement, gen_EMOF_PrimitiveType_DataType, gen_EMOF_Property_TypedElement, gen_EMOF_Property_MultiplicityElement, gen_EMOF_ReflectiveCollection_Object, gen_EssentialOCL_BooleanLiteralExp_PrimitiveLiteralExp, gen_EssentialOCL_CallExp_OclExpression, gen_EssentialOCL_CollectionItem_CollectionLiteralPart, gen_EMOF_Type_NamedElement, gen_EMOF_TypedElement_NamedElement, gen_EMOF_URIExtent_Extent, gen_EssentialOCL_AnyType_Type, gen_EssentialOCL_BagType_CollectionType, gen_EssentialOCL_CollectionType_DataType, gen_EssentialOCL_CollectionLiteralExp_LiteralExp, gen_EssentialOCL_CollectionLiteralPart_TypedElement, gen_EssentialOCL_CollectionRange_CollectionLiteralPart, gen_EssentialOCL_FeatureCallExp_CallExp, gen_EssentialOCL_IfExp_OclExpression, gen_EssentialOCL_EnumLiteralExp_LiteralExp, gen_EssentialOCL_ExpressionInOcl_TypedElement, gen_EssentialOCL_LoopExp_CallExp, gen_EssentialOCL_LoopExp_OclExpression, gen_EssentialOCL_NavigationCallExp_FeatureCallExp, gen_EssentialOCL_NullLiteralExp_LiteralExp, gen_EssentialOCL_NumericLiteralExp_PrimitiveLiteralExp, gen_EssentialOCL_OclExpression_TypedElement, gen_EssentialOCL_OperationCallExp_FeatureCallExp, gen_EssentialOCL_IntegerLiteralExp_NumericLiteralExp, gen_EssentialOCL_InvalidLiteralExp_LiteralExp, gen_EssentialOCL_InvalidType_Type, gen_EssentialOCL_IterateExp_LoopExp, gen_EssentialOCL_IteratorExp_LoopExp, gen_EssentialOCL_LetExp_OclExpression, gen_EssentialOCL_LiteralExp_OclExpression, gen_EssentialOCL_TupleType_Class, gen_EssentialOCL_TupleType_DataType, gen_EssentialOCL_TypeExp_OclExpression, gen_EssentialOCL_UnlimitedNaturalExp_NumericLiteralExp, gen_EssentialOCL_Variable_TypedElement, gen_EssentialOCL_OrderedSetType_CollectionType, gen_EssentialOCL_PrimitiveLiteralExp_LiteralExp, gen_EssentialOCL_PropertyCallExp_NavigationCallExp, gen_EssentialOCL_RealLiteralExp_NumericLiteralExp, gen_EssentialOCL_SequenceType_CollectionType, gen_EssentialOCL_SetType_CollectionType, gen_EssentialOCL_StringLiteralExp_PrimitiveLiteralExp, gen_EssentialOCL_TemplateParameterType_Type, gen_EssentialOCL_TupleLiteralExp_LiteralExp, gen_EssentialOCL_TupleLiteralPart_TypedElement, gen_QVTBase_Function_Operation, gen_QVTBase_FunctionParameter_Variable, gen_QVTBase_FunctionParameter_Parameter, gen_QVTBase_Pattern_Element, gen_EssentialOCL_VariableExp_OclExpression, gen_EssentialOCL_VoidType_Type, gen_QVTBase_Domain_NamedElement, gen_QVTBase_Transformation_Class, gen_QVTBase_Transformation_Package, gen_QVTBase_Predicate_Element, gen_QVTBase_Rule_NamedElement, gen_QVTCore_Assignment_Element, gen_QVTBase_TypedModel_NamedElement, gen_QVTCore_EnforcementOperation_Element, gen_QVTCore_BottomPattern_CorePattern, gen_QVTCore_CoreDomain_Domain, gen_QVTCore_CoreDomain_Area, gen_QVTCore_CorePattern_Pattern, gen_QVTCore_RealizedVariable_Variable, gen_QVTCore_VariableAssignment_Assignment, gen_QVTCore_GuardPattern_CorePattern, gen_QVTCore_Mapping_Rule, gen_QVTCore_Mapping_Area, gen_QVTCore_PropertyAssignment_Assignment, gen_QVTTemplate_PropertyTemplateItem_Element, gen_QVTTemplate_CollectionTemplateExp_TemplateExp, gen_QVTTemplate_ObjectTemplateExp_TemplateExp, gen_QVTRelation_Key_Element, gen_QVTTemplate_TemplateExp_LiteralExp, gen_QVTRelation_DomainPattern_Pattern, gen_QVTRelation_RelationCallExp_OclExpression, gen_QVTRelation_RelationDomain_Domain, gen_QVTRelation_OppositePropertyCallExp_PropertyCallExp, gen_QVTRelation_Relation_Rule, gen_QVTRelation_RelationImplementation_Element, gen_QVTRelation_RelationDomainAssignment_Element, gen_ImperativeOCL_AssignExp_ImperativeExpression, gen_QVTRelation_RelationalTransformation_Transformation, gen_ImperativeOCL_AltExp_ImperativeExpression, gen_ImperativeOCL_AssertExp_ImperativeExpression, gen_ImperativeOCL_BreakExp_ImperativeExpression, gen_ImperativeOCL_CatchExp_ImperativeExpression, gen_ImperativeOCL_BlockExp_ImperativeExpression, gen_ImperativeOCL_DictionaryType_CollectionType, gen_ImperativeOCL_ComputeExp_ImperativeExpression, gen_ImperativeOCL_ContinueExp_ImperativeExpression, gen_ImperativeOCL_DictLiteralExp_LiteralExp, gen_ImperativeOCL_DictLiteralPart_Element, gen_ImperativeOCL_InstantiationExp_ImperativeExpression, gen_ImperativeOCL_ForExp_ImperativeLoopExp, gen_ImperativeOCL_ImperativeExpression_OclExpression, gen_ImperativeOCL_ImperativeIterateExp_ImperativeLoopExp, gen_ImperativeOCL_ImperativeLoopExp_LoopExp, gen_ImperativeOCL_ImperativeLoopExp_ImperativeExpression, gen_ImperativeOCL_LogExp_OperationCallExp, gen_ImperativeOCL_LogExp_ImperativeExpression, gen_ImperativeOCL_ListLiteralExp_LiteralExp, gen_ImperativeOCL_ListType_CollectionType, gen_ImperativeOCL_SwitchExp_ImperativeExpression, gen_ImperativeOCL_RaiseExp_ImperativeExpression, gen_ImperativeOCL_ReturnExp_ImperativeExpression, gen_ImperativeOCL_Typedef_Class, gen_ImperativeOCL_TryExp_ImperativeExpression, gen_ImperativeOCL_VariableInitExp_ImperativeExpression, gen_ImperativeOCL_WhileExp_ImperativeExpression, gen_ImperativeOCL_UnlinkExp_ImperativeExpression, gen_QVTOperational_Constructor_ImperativeOperation, gen_QVTOperational_ConstructorBody_OperationBody, gen_QVTOperational_ContextualProperty_Property, gen_QVTOperational_Helper_ImperativeOperation, gen_QVTOperational_ImperativeCallExp_OperationCallExp, gen_QVTOperational_ImperativeCallExp_ImperativeExpression, gen_QVTOperational_EntryOperation_ImperativeOperation, gen_QVTOperational_ImperativeOperation_Operation, gen_QVTOperational_MappingCallExp_ImperativeCallExp, gen_QVTOperational_MappingOperation_ImperativeOperation, gen_QVTOperational_Library_Module, gen_QVTOperational_MappingBody_OperationBody, gen_QVTOperational_MappingParameter_VarParameter, gen_QVTOperational_Module_Class, gen_QVTOperational_Module_Package, gen_QVTOperational_ModelParameter_VarParameter, gen_QVTOperational_ModelType_Class, gen_QVTOperational_ModuleImport_Element, gen_QVTOperational_OperationBody_Element, gen_QVTOperational_ObjectExp_InstantiationExp, gen_QVTOperational_OperationalTransformation_Module, gen_QVTOperational_ResolveInExp_ResolveExp, gen_QVTOperational_VarParameter_Variable, gen_QVTOperational_VarParameter_Parameter, gen_QVTOperational_ResolveExp_CallExp, gen_QVTOperational_ResolveExp_ImperativeExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)