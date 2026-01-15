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

SeverityKind: Enumeration = Enumeration(
    name="SeverityKind",
    literals={
            EnumerationLiteral(name="error"),
			EnumerationLiteral(name="warning"),
			EnumerationLiteral(name="fatal")
    }
)

EnforcementMode: Enumeration = Enumeration(
    name="EnforcementMode",
    literals={
            EnumerationLiteral(name="Creation"),
			EnumerationLiteral(name="Deletion")
    }
)

ImportKind: Enumeration = Enumeration(
    name="ImportKind",
    literals={
            EnumerationLiteral(name="extension"),
			EnumerationLiteral(name="access")
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

# Classes
Operation = Class(name="Operation")
Class_ = Class(name="Class")
EMOF_Comment = Class(name="EMOF::Comment")
Element = Class(name="Element")
NamedElement = Class(name="NamedElement")
EMOF_Class = Class(name="EMOF::Class")
Type = Class(name="Type")
Property_ = Class(name="Property")
Comment = Class(name="Comment")
EMOF_Enumeration = Class(name="EMOF::Enumeration")
DataType = Class(name="DataType")
EnumerationLiteral = Class(name="EnumerationLiteral")
EMOF_EnumerationLiteral = Class(name="EMOF::EnumerationLiteral")
EMOF_DataType = Class(name="EMOF::DataType")
EMOF_Element = Class(name="EMOF::Element", is_abstract=True)
Object = Class(name="Object")
Package = Class(name="Package")
Enumeration_ = Class(name="Enumeration")
EMOF_Extent = Class(name="EMOF::Extent")
EMOF_Factory = Class(name="EMOF::Factory")
EMOF_Object = Class(name="EMOF::Object")
EMOF_Operation = Class(name="EMOF::Operation")
TypedElement = Class(name="TypedElement")
MultiplicityElement = Class(name="MultiplicityElement")
Parameter_ = Class(name="Parameter")
EMOF_MultiplicityElement = Class(name="EMOF::MultiplicityElement", is_abstract=True)
EMOF_NamedElement = Class(name="EMOF::NamedElement", is_abstract=True)
EMOF_Package = Class(name="EMOF::Package")
EMOF_Parameter = Class(name="EMOF::Parameter")
EMOF_PrimitiveType = Class(name="EMOF::PrimitiveType")
EMOF_ReflectiveCollection = Class(name="EMOF::ReflectiveCollection")
EMOF_Property = Class(name="EMOF::Property")
EMOF_Tag = Class(name="EMOF::Tag")
EMOF_ReflectiveSequence = Class(name="EMOF::ReflectiveSequence")
ReflectiveCollection = Class(name="ReflectiveCollection")
EMOF_TypedElement = Class(name="EMOF::TypedElement", is_abstract=True)
EMOF_URIExtent = Class(name="EMOF::URIExtent")
Extent = Class(name="Extent")
EMOF_Type = Class(name="EMOF::Type", is_abstract=True)
EssentialOCL_AnyType = Class(name="EssentialOCL::AnyType")
EssentialOCL_BagType = Class(name="EssentialOCL::BagType")
CollectionType = Class(name="CollectionType")
EssentialOCL_BooleanLiteralExp = Class(name="EssentialOCL::BooleanLiteralExp")
PrimitiveLiteralExp = Class(name="PrimitiveLiteralExp")
EssentialOCL_CallExp = Class(name="EssentialOCL::CallExp", is_abstract=True)
OclExpression = Class(name="OclExpression")
CollectionLiteralPart = Class(name="CollectionLiteralPart")
EssentialOCL_CollectionItem = Class(name="EssentialOCL::CollectionItem")
EssentialOCL_CollectionLiteralPart = Class(name="EssentialOCL::CollectionLiteralPart", is_abstract=True)
CollectionLiteralExp = Class(name="CollectionLiteralExp")
EssentialOCL_CollectionRange = Class(name="EssentialOCL::CollectionRange")
EssentialOCL_CollectionLiteralExp = Class(name="EssentialOCL::CollectionLiteralExp")
LiteralExp = Class(name="LiteralExp")
EssentialOCL_CollectionType = Class(name="EssentialOCL::CollectionType")
EssentialOCL_EnumLiteralExp = Class(name="EssentialOCL::EnumLiteralExp")
EssentialOCL_ExpressionInOcl = Class(name="EssentialOCL::ExpressionInOcl")
Variable = Class(name="Variable")
EssentialOCL_FeatureCallExp = Class(name="EssentialOCL::FeatureCallExp", is_abstract=True)
CallExp = Class(name="CallExp")
EssentialOCL_IfExp = Class(name="EssentialOCL::IfExp")
EssentialOCL_LetExp = Class(name="EssentialOCL::LetExp")
EssentialOCL_IntegerLiteralExp = Class(name="EssentialOCL::IntegerLiteralExp")
NumericLiteralExp = Class(name="NumericLiteralExp")
EssentialOCL_InvalidLiteralExp = Class(name="EssentialOCL::InvalidLiteralExp")
EssentialOCL_InvalidType = Class(name="EssentialOCL::InvalidType")
EssentialOCL_IterateExp = Class(name="EssentialOCL::IterateExp")
LoopExp = Class(name="LoopExp")
EssentialOCL_IteratorExp = Class(name="EssentialOCL::IteratorExp")
EssentialOCL_NavigationCallExp = Class(name="EssentialOCL::NavigationCallExp")
FeatureCallExp = Class(name="FeatureCallExp")
EssentialOCL_NullLiteralExp = Class(name="EssentialOCL::NullLiteralExp")
EssentialOCL_NumericLiteralExp = Class(name="EssentialOCL::NumericLiteralExp", is_abstract=True)
EssentialOCL_LiteralExp = Class(name="EssentialOCL::LiteralExp", is_abstract=True)
EssentialOCL_LoopExp = Class(name="EssentialOCL::LoopExp", is_abstract=True)
EssentialOCL_PropertyCallExp = Class(name="EssentialOCL::PropertyCallExp")
NavigationCallExp = Class(name="NavigationCallExp")
EssentialOCL_RealLiteralExp = Class(name="EssentialOCL::RealLiteralExp")
EssentialOCL_OclExpression = Class(name="EssentialOCL::OclExpression", is_abstract=True)
EssentialOCL_OperationCallExp = Class(name="EssentialOCL::OperationCallExp")
EssentialOCL_OrderedSetType = Class(name="EssentialOCL::OrderedSetType")
EssentialOCL_PrimitiveLiteralExp = Class(name="EssentialOCL::PrimitiveLiteralExp", is_abstract=True)
EssentialOCL_TupleLiteralPart = Class(name="EssentialOCL::TupleLiteralPart")
TupleLiteralExp = Class(name="TupleLiteralExp")
EssentialOCL_SequenceType = Class(name="EssentialOCL::SequenceType")
EssentialOCL_SetType = Class(name="EssentialOCL::SetType")
EssentialOCL_StringLiteralExp = Class(name="EssentialOCL::StringLiteralExp")
EssentialOCL_TemplateParameterType = Class(name="EssentialOCL::TemplateParameterType")
EssentialOCL_TupleLiteralExp = Class(name="EssentialOCL::TupleLiteralExp")
TupleLiteralPart = Class(name="TupleLiteralPart")
LetExp = Class(name="LetExp")
EssentialOCL_TupleType = Class(name="EssentialOCL::TupleType")
EssentialOCL_TypeExp = Class(name="EssentialOCL::TypeExp")
EssentialOCL_UnlimitedNaturalExp = Class(name="EssentialOCL::UnlimitedNaturalExp")
EssentialOCL_Variable = Class(name="EssentialOCL::Variable")
EssentialOCL_VariableExp = Class(name="EssentialOCL::VariableExp")
EssentialOCL_VoidType = Class(name="EssentialOCL::VoidType")
ImperativeOCL_AltExp = Class(name="ImperativeOCL::AltExp")
ImperativeExpression = Class(name="ImperativeExpression")
LogExp = Class(name="LogExp")
ImperativeOCL_AssignExp = Class(name="ImperativeOCL::AssignExp")
ImperativeOCL_AssertExp = Class(name="ImperativeOCL::AssertExp")
ImperativeOCL_BlockExp = Class(name="ImperativeOCL::BlockExp")
ImperativeOCL_BreakExp = Class(name="ImperativeOCL::BreakExp")
ImperativeOCL_CatchExp = Class(name="ImperativeOCL::CatchExp")
ImperativeOCL_ContinueExp = Class(name="ImperativeOCL::ContinueExp")
ImperativeOCL_DictLiteralExp = Class(name="ImperativeOCL::DictLiteralExp")
DictLiteralPart = Class(name="DictLiteralPart")
ImperativeOCL_ComputeExp = Class(name="ImperativeOCL::ComputeExp")
ImperativeOCL_DictionaryType = Class(name="ImperativeOCL::DictionaryType")
ImperativeOCL_ForExp = Class(name="ImperativeOCL::ForExp")
ImperativeLoopExp = Class(name="ImperativeLoopExp")
ImperativeOCL_ImperativeExpression = Class(name="ImperativeOCL::ImperativeExpression", is_abstract=True)
ImperativeOCL_DictLiteralPart = Class(name="ImperativeOCL::DictLiteralPart")
ImperativeOCL_ImperativeLoopExp = Class(name="ImperativeOCL::ImperativeLoopExp", is_abstract=True)
ImperativeOCL_InstantiationExp = Class(name="ImperativeOCL::InstantiationExp")
ImperativeOCL_ImperativeIterateExp = Class(name="ImperativeOCL::ImperativeIterateExp")
ImperativeOCL_ListType = Class(name="ImperativeOCL::ListType")
ImperativeOCL_LogExp = Class(name="ImperativeOCL::LogExp")
OperationCallExp = Class(name="OperationCallExp")
ImperativeOCL_OrderedTupleLiteralExp = Class(name="ImperativeOCL::OrderedTupleLiteralExp")
OrderedTupleLiteralPart = Class(name="OrderedTupleLiteralPart")
ImperativeOCL_ListLiteralExp = Class(name="ImperativeOCL::ListLiteralExp")
ImperativeOCL_OrderedTupleType = Class(name="ImperativeOCL::OrderedTupleType")
ImperativeOCL_RaiseExp = Class(name="ImperativeOCL::RaiseExp")
ImperativeOCL_OrderedTupleLiteralPart = Class(name="ImperativeOCL::OrderedTupleLiteralPart")
ImperativeOCL_ReturnExp = Class(name="ImperativeOCL::ReturnExp")
ImperativeOCL_SwitchExp = Class(name="ImperativeOCL::SwitchExp")
AltExp = Class(name="AltExp")
ImperativeOCL_TryExp = Class(name="ImperativeOCL::TryExp")
CatchExp = Class(name="CatchExp")
ImperativeOCL_Typedef = Class(name="ImperativeOCL::Typedef")
ImperativeOCL_UnlinkExp = Class(name="ImperativeOCL::UnlinkExp")
ImperativeOCL_UnpackExp = Class(name="ImperativeOCL::UnpackExp")
ImperativeOCL_VariableInitExp = Class(name="ImperativeOCL::VariableInitExp")
ImperativeOCL_WhileExp = Class(name="ImperativeOCL::WhileExp")
QVTBase_Domain = Class(name="QVTBase::Domain", is_abstract=True)
Rule = Class(name="Rule")
TypedModel = Class(name="TypedModel")
QVTBase_Function = Class(name="QVTBase::Function")
QVTBase_Pattern = Class(name="QVTBase::Pattern")
Predicate = Class(name="Predicate")
QVTBase_Predicate = Class(name="QVTBase::Predicate")
Pattern = Class(name="Pattern")
QVTBase_FunctionParameter = Class(name="QVTBase::FunctionParameter")
Transformation = Class(name="Transformation")
QVTBase_Transformation = Class(name="QVTBase::Transformation")
Tag = Class(name="Tag")
QVTBase_Rule = Class(name="QVTBase::Rule", is_abstract=True)
Domain = Class(name="Domain")
QVTBase_TypedModel = Class(name="QVTBase::TypedModel")
QVTCore_Area = Class(name="QVTCore::Area", is_abstract=True)
BottomPattern = Class(name="BottomPattern")
GuardPattern = Class(name="GuardPattern")
QVTCore_Assignment = Class(name="QVTCore::Assignment", is_abstract=True)
Assignment = Class(name="Assignment")
EnforcementOperation = Class(name="EnforcementOperation")
RealizedVariable = Class(name="RealizedVariable")
QVTCore_CoreDomain = Class(name="QVTCore::CoreDomain")
QVTCore_CorePattern = Class(name="QVTCore::CorePattern")
QVTCore_BottomPattern = Class(name="QVTCore::BottomPattern")
CorePattern = Class(name="CorePattern")
Area = Class(name="Area")
QVTCore_EnforcementOperation = Class(name="QVTCore::EnforcementOperation")
QVTCore_GuardPattern = Class(name="QVTCore::GuardPattern")
QVTCore_Mapping = Class(name="QVTCore::Mapping")
QVTCore_PropertyAssignment = Class(name="QVTCore::PropertyAssignment")
Mapping = Class(name="Mapping")
QVTCore_VariableAssignment = Class(name="QVTCore::VariableAssignment")
QVTCore_RealizedVariable = Class(name="QVTCore::RealizedVariable")
QVTTemplate_CollectionTemplateExp = Class(name="QVTTemplate::CollectionTemplateExp")
TemplateExp = Class(name="TemplateExp")
PropertyTemplateItem = Class(name="PropertyTemplateItem")
QVTTemplate_ObjectTemplateExp = Class(name="QVTTemplate::ObjectTemplateExp")
QVTTemplate_PropertyTemplateItem = Class(name="QVTTemplate::PropertyTemplateItem")
ObjectTemplateExp = Class(name="ObjectTemplateExp")
QVTTemplate_TemplateExp = Class(name="QVTTemplate::TemplateExp", is_abstract=True)
QVTRelation_DomainPattern = Class(name="QVTRelation::DomainPattern")
RelationalTransformation = Class(name="RelationalTransformation")
QVTRelation_OppositePropertyCallExp = Class(name="QVTRelation::OppositePropertyCallExp")
PropertyCallExp = Class(name="PropertyCallExp")
QVTRelation_Relation = Class(name="QVTRelation::Relation")
QVTRelation_Key = Class(name="QVTRelation::Key")
QVTRelation_RelationCallExp = Class(name="QVTRelation::RelationCallExp")
RelationImplementation = Class(name="RelationImplementation")
QVTRelation_RelationDomain = Class(name="QVTRelation::RelationDomain")
RelationDomainAssignment = Class(name="RelationDomainAssignment")
DomainPattern = Class(name="DomainPattern")
QVTRelation_RelationDomainAssignment = Class(name="QVTRelation::RelationDomainAssignment")
Relation = Class(name="Relation")
QVTRelation_RelationImplementation = Class(name="QVTRelation::RelationImplementation")
QVTRelation_RelationalTransformation = Class(name="QVTRelation::RelationalTransformation")
Key = Class(name="Key")
QVTOperational_Constructor = Class(name="QVTOperational::Constructor")
ImperativeOperation = Class(name="ImperativeOperation")
QVTOperational_ConstructorBody = Class(name="QVTOperational::ConstructorBody")
OperationBody = Class(name="OperationBody")
QVTOperational_ContextualProperty = Class(name="QVTOperational::ContextualProperty")
QVTOperational_Helper = Class(name="QVTOperational::Helper")
QVTOperational_ImperativeCallExp = Class(name="QVTOperational::ImperativeCallExp")
QVTOperational_ImperativeOperation = Class(name="QVTOperational::ImperativeOperation")
VarParameter = Class(name="VarParameter")
QVTOperational_Library = Class(name="QVTOperational::Library")
Module = Class(name="Module")
QVTOperational_EntryOperation = Class(name="QVTOperational::EntryOperation")
QVTOperational_MappingCallExp = Class(name="QVTOperational::MappingCallExp")
ImperativeCallExp = Class(name="ImperativeCallExp")
QVTOperational_MappingOperation = Class(name="QVTOperational::MappingOperation")
MappingOperation = Class(name="MappingOperation")
QVTOperational_MappingBody = Class(name="QVTOperational::MappingBody")
ModelParameter = Class(name="ModelParameter")
RelationDomain = Class(name="RelationDomain")
QVTOperational_ModelParameter = Class(name="QVTOperational::ModelParameter")
QVTOperational_ModelType = Class(name="QVTOperational::ModelType")
QVTOperational_MappingParameter = Class(name="QVTOperational::MappingParameter")
QVTOperational_Module = Class(name="QVTOperational::Module")
EntryOperation = Class(name="EntryOperation")
ModuleImport = Class(name="ModuleImport")
ModelType = Class(name="ModelType")
QVTOperational_ModuleImport = Class(name="QVTOperational::ModuleImport")
QVTOperational_ObjectExp = Class(name="QVTOperational::ObjectExp")
InstantiationExp = Class(name="InstantiationExp")
ConstructorBody = Class(name="ConstructorBody")
QVTOperational_OperationBody = Class(name="QVTOperational::OperationBody")
QVTOperational_OperationalTransformation = Class(name="QVTOperational::OperationalTransformation")
QVTOperational_ResolveExp = Class(name="QVTOperational::ResolveExp")
QVTOperational_ResolveInExp = Class(name="QVTOperational::ResolveInExp")
ResolveExp = Class(name="ResolveExp")
QVTOperational_VarParameter = Class(name="QVTOperational::VarParameter")

# Operation class attributes and methods

# Class class attributes and methods

# EMOF_Comment class attributes and methods
EMOF_Comment_body: Property = Property(name="body", type=StringType)
EMOF_Comment.attributes={EMOF_Comment_body}

# Element class attributes and methods

# NamedElement class attributes and methods

# EMOF_Class class attributes and methods
EMOF_Class_isAbstract: Property = Property(name="isAbstract", type=StringType)
EMOF_Class.attributes={EMOF_Class_isAbstract}

# Type class attributes and methods

# Property class attributes and methods

# Comment class attributes and methods

# EMOF_Enumeration class attributes and methods

# DataType class attributes and methods

# EnumerationLiteral class attributes and methods

# EMOF_EnumerationLiteral class attributes and methods

# EMOF_DataType class attributes and methods

# EMOF_Element class attributes and methods
EMOF_Element_m_getMetaClass: Method = Method(name="getMetaClass", parameters={}, type=StringType)
EMOF_Element_m_isSet: Method = Method(name="isSet", parameters={Parameter(name='property')}, type=StringType)
EMOF_Element_m_set: Method = Method(name="set", parameters={Parameter(name='object'), Parameter(name='property')})
EMOF_Element_m_unset: Method = Method(name="unset", parameters={Parameter(name='property')})
EMOF_Element_m_container: Method = Method(name="container", parameters={}, type=StringType)
EMOF_Element_m_equals: Method = Method(name="equals", parameters={Parameter(name='object')}, type=StringType)
EMOF_Element_m_get: Method = Method(name="get", parameters={Parameter(name='property')}, type=StringType)
EMOF_Element.methods={EMOF_Element_m_getMetaClass, EMOF_Element_m_get, EMOF_Element_m_container, EMOF_Element_m_equals, EMOF_Element_m_set, EMOF_Element_m_unset, EMOF_Element_m_isSet}

# Object class attributes and methods

# Package class attributes and methods

# Enumeration class attributes and methods

# EMOF_Extent class attributes and methods
EMOF_Extent_m_elements: Method = Method(name="elements", parameters={}, type=StringType)
EMOF_Extent_m_useContainment: Method = Method(name="useContainment", parameters={}, type=StringType)
EMOF_Extent.methods={EMOF_Extent_m_useContainment, EMOF_Extent_m_elements}

# EMOF_Factory class attributes and methods
EMOF_Factory_m_convertToString: Method = Method(name="convertToString", parameters={Parameter(name='object'), Parameter(name='dataType')}, type=StringType)
EMOF_Factory_m_create: Method = Method(name="create", parameters={Parameter(name='metaClass')}, type=StringType)
EMOF_Factory_m_createFromString: Method = Method(name="createFromString", parameters={Parameter(name='dataType'), Parameter(name='string')}, type=StringType)
EMOF_Factory.methods={EMOF_Factory_m_create, EMOF_Factory_m_createFromString, EMOF_Factory_m_convertToString}

# EMOF_Object class attributes and methods

# EMOF_Operation class attributes and methods

# TypedElement class attributes and methods

# MultiplicityElement class attributes and methods

# Parameter class attributes and methods

# EMOF_MultiplicityElement class attributes and methods
EMOF_MultiplicityElement_isOrdered: Property = Property(name="isOrdered", type=StringType)
EMOF_MultiplicityElement_isUnique: Property = Property(name="isUnique", type=StringType)
EMOF_MultiplicityElement_lower: Property = Property(name="lower", type=StringType)
EMOF_MultiplicityElement_upper: Property = Property(name="upper", type=StringType)
EMOF_MultiplicityElement.attributes={EMOF_MultiplicityElement_isOrdered, EMOF_MultiplicityElement_lower, EMOF_MultiplicityElement_isUnique, EMOF_MultiplicityElement_upper}

# EMOF_NamedElement class attributes and methods
EMOF_NamedElement_name: Property = Property(name="name", type=StringType)
EMOF_NamedElement.attributes={EMOF_NamedElement_name}

# EMOF_Package class attributes and methods
EMOF_Package_uri: Property = Property(name="uri", type=StringType)
EMOF_Package.attributes={EMOF_Package_uri}

# EMOF_Parameter class attributes and methods

# EMOF_PrimitiveType class attributes and methods

# EMOF_ReflectiveCollection class attributes and methods
EMOF_ReflectiveCollection_m_add: Method = Method(name="add", parameters={Parameter(name='object')}, type=StringType)
EMOF_ReflectiveCollection_m_addAll: Method = Method(name="addAll", parameters={Parameter(name='objects')}, type=StringType)
EMOF_ReflectiveCollection_m_clear: Method = Method(name="clear", parameters={})
EMOF_ReflectiveCollection_m_remove: Method = Method(name="remove", parameters={Parameter(name='object')}, type=StringType)
EMOF_ReflectiveCollection_m_size: Method = Method(name="size", parameters={}, type=StringType)
EMOF_ReflectiveCollection.methods={EMOF_ReflectiveCollection_m_size, EMOF_ReflectiveCollection_m_remove, EMOF_ReflectiveCollection_m_add, EMOF_ReflectiveCollection_m_addAll, EMOF_ReflectiveCollection_m_clear}

# EMOF_Property class attributes and methods
EMOF_Property_isComposite: Property = Property(name="isComposite", type=StringType)
EMOF_Property_isDerived: Property = Property(name="isDerived", type=StringType)
EMOF_Property_isID: Property = Property(name="isID", type=StringType)
EMOF_Property_isReadOnly: Property = Property(name="isReadOnly", type=StringType)
EMOF_Property_default: Property = Property(name="default", type=StringType)
EMOF_Property.attributes={EMOF_Property_isComposite, EMOF_Property_isReadOnly, EMOF_Property_isDerived, EMOF_Property_default, EMOF_Property_isID}

# EMOF_Tag class attributes and methods
EMOF_Tag_name: Property = Property(name="name", type=StringType)
EMOF_Tag_value: Property = Property(name="value", type=StringType)
EMOF_Tag.attributes={EMOF_Tag_name, EMOF_Tag_value}

# EMOF_ReflectiveSequence class attributes and methods
EMOF_ReflectiveSequence_m_get: Method = Method(name="get", parameters={Parameter(name='index')}, type=StringType)
EMOF_ReflectiveSequence_m_remove: Method = Method(name="remove", parameters={Parameter(name='index')}, type=StringType)
EMOF_ReflectiveSequence_m_set: Method = Method(name="set", parameters={Parameter(name='object'), Parameter(name='index')}, type=StringType)
EMOF_ReflectiveSequence_m_add: Method = Method(name="add", parameters={Parameter(name='index'), Parameter(name='object')})
EMOF_ReflectiveSequence.methods={EMOF_ReflectiveSequence_m_set, EMOF_ReflectiveSequence_m_get, EMOF_ReflectiveSequence_m_add, EMOF_ReflectiveSequence_m_remove}

# ReflectiveCollection class attributes and methods

# EMOF_TypedElement class attributes and methods

# EMOF_URIExtent class attributes and methods
EMOF_URIExtent_m_contextURI: Method = Method(name="contextURI", parameters={}, type=StringType)
EMOF_URIExtent_m_element: Method = Method(name="element", parameters={Parameter(name='uri')}, type=StringType)
EMOF_URIExtent_m_uri: Method = Method(name="uri", parameters={Parameter(name='element')}, type=StringType)
EMOF_URIExtent.methods={EMOF_URIExtent_m_element, EMOF_URIExtent_m_uri, EMOF_URIExtent_m_contextURI}

# Extent class attributes and methods

# EMOF_Type class attributes and methods
EMOF_Type_m_isInstance: Method = Method(name="isInstance", parameters={Parameter(name='object')}, type=StringType)
EMOF_Type.methods={EMOF_Type_m_isInstance}

# EssentialOCL_AnyType class attributes and methods

# EssentialOCL_BagType class attributes and methods

# CollectionType class attributes and methods

# EssentialOCL_BooleanLiteralExp class attributes and methods
EssentialOCL_BooleanLiteralExp_booleanSymbol: Property = Property(name="booleanSymbol", type=StringType)
EssentialOCL_BooleanLiteralExp.attributes={EssentialOCL_BooleanLiteralExp_booleanSymbol}

# PrimitiveLiteralExp class attributes and methods

# EssentialOCL_CallExp class attributes and methods

# OclExpression class attributes and methods

# CollectionLiteralPart class attributes and methods

# EssentialOCL_CollectionItem class attributes and methods

# EssentialOCL_CollectionLiteralPart class attributes and methods

# CollectionLiteralExp class attributes and methods

# EssentialOCL_CollectionRange class attributes and methods

# EssentialOCL_CollectionLiteralExp class attributes and methods
EssentialOCL_CollectionLiteralExp_kind: Property = Property(name="kind", type=StringType)
EssentialOCL_CollectionLiteralExp.attributes={EssentialOCL_CollectionLiteralExp_kind}

# LiteralExp class attributes and methods

# EssentialOCL_CollectionType class attributes and methods

# EssentialOCL_EnumLiteralExp class attributes and methods

# EssentialOCL_ExpressionInOcl class attributes and methods

# Variable class attributes and methods

# EssentialOCL_FeatureCallExp class attributes and methods

# CallExp class attributes and methods

# EssentialOCL_IfExp class attributes and methods

# EssentialOCL_LetExp class attributes and methods

# EssentialOCL_IntegerLiteralExp class attributes and methods
EssentialOCL_IntegerLiteralExp_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
EssentialOCL_IntegerLiteralExp.attributes={EssentialOCL_IntegerLiteralExp_integerSymbol}

# NumericLiteralExp class attributes and methods

# EssentialOCL_InvalidLiteralExp class attributes and methods

# EssentialOCL_InvalidType class attributes and methods

# EssentialOCL_IterateExp class attributes and methods

# LoopExp class attributes and methods

# EssentialOCL_IteratorExp class attributes and methods

# EssentialOCL_NavigationCallExp class attributes and methods

# FeatureCallExp class attributes and methods

# EssentialOCL_NullLiteralExp class attributes and methods

# EssentialOCL_NumericLiteralExp class attributes and methods

# EssentialOCL_LiteralExp class attributes and methods

# EssentialOCL_LoopExp class attributes and methods

# EssentialOCL_PropertyCallExp class attributes and methods

# NavigationCallExp class attributes and methods

# EssentialOCL_RealLiteralExp class attributes and methods
EssentialOCL_RealLiteralExp_realSymbol: Property = Property(name="realSymbol", type=StringType)
EssentialOCL_RealLiteralExp.attributes={EssentialOCL_RealLiteralExp_realSymbol}

# EssentialOCL_OclExpression class attributes and methods

# EssentialOCL_OperationCallExp class attributes and methods

# EssentialOCL_OrderedSetType class attributes and methods

# EssentialOCL_PrimitiveLiteralExp class attributes and methods

# EssentialOCL_TupleLiteralPart class attributes and methods

# TupleLiteralExp class attributes and methods

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

# LetExp class attributes and methods

# EssentialOCL_TupleType class attributes and methods

# EssentialOCL_TypeExp class attributes and methods

# EssentialOCL_UnlimitedNaturalExp class attributes and methods
EssentialOCL_UnlimitedNaturalExp_symbol: Property = Property(name="symbol", type=StringType)
EssentialOCL_UnlimitedNaturalExp.attributes={EssentialOCL_UnlimitedNaturalExp_symbol}

# EssentialOCL_Variable class attributes and methods

# EssentialOCL_VariableExp class attributes and methods

# EssentialOCL_VoidType class attributes and methods

# ImperativeOCL_AltExp class attributes and methods

# ImperativeExpression class attributes and methods

# LogExp class attributes and methods

# ImperativeOCL_AssignExp class attributes and methods
ImperativeOCL_AssignExp_isReset: Property = Property(name="isReset", type=StringType)
ImperativeOCL_AssignExp.attributes={ImperativeOCL_AssignExp_isReset}

# ImperativeOCL_AssertExp class attributes and methods
ImperativeOCL_AssertExp_severity: Property = Property(name="severity", type=StringType)
ImperativeOCL_AssertExp.attributes={ImperativeOCL_AssertExp_severity}

# ImperativeOCL_BlockExp class attributes and methods

# ImperativeOCL_BreakExp class attributes and methods

# ImperativeOCL_CatchExp class attributes and methods

# ImperativeOCL_ContinueExp class attributes and methods

# ImperativeOCL_DictLiteralExp class attributes and methods

# DictLiteralPart class attributes and methods

# ImperativeOCL_ComputeExp class attributes and methods

# ImperativeOCL_DictionaryType class attributes and methods

# ImperativeOCL_ForExp class attributes and methods

# ImperativeLoopExp class attributes and methods

# ImperativeOCL_ImperativeExpression class attributes and methods

# ImperativeOCL_DictLiteralPart class attributes and methods

# ImperativeOCL_ImperativeLoopExp class attributes and methods

# ImperativeOCL_InstantiationExp class attributes and methods

# ImperativeOCL_ImperativeIterateExp class attributes and methods

# ImperativeOCL_ListType class attributes and methods

# ImperativeOCL_LogExp class attributes and methods

# OperationCallExp class attributes and methods

# ImperativeOCL_OrderedTupleLiteralExp class attributes and methods

# OrderedTupleLiteralPart class attributes and methods

# ImperativeOCL_ListLiteralExp class attributes and methods

# ImperativeOCL_OrderedTupleType class attributes and methods

# ImperativeOCL_RaiseExp class attributes and methods

# ImperativeOCL_OrderedTupleLiteralPart class attributes and methods

# ImperativeOCL_ReturnExp class attributes and methods

# ImperativeOCL_SwitchExp class attributes and methods

# AltExp class attributes and methods

# ImperativeOCL_TryExp class attributes and methods

# CatchExp class attributes and methods

# ImperativeOCL_Typedef class attributes and methods

# ImperativeOCL_UnlinkExp class attributes and methods

# ImperativeOCL_UnpackExp class attributes and methods

# ImperativeOCL_VariableInitExp class attributes and methods
ImperativeOCL_VariableInitExp_withResult: Property = Property(name="withResult", type=StringType)
ImperativeOCL_VariableInitExp.attributes={ImperativeOCL_VariableInitExp_withResult}

# ImperativeOCL_WhileExp class attributes and methods

# QVTBase_Domain class attributes and methods
QVTBase_Domain_isCheckable: Property = Property(name="isCheckable", type=StringType)
QVTBase_Domain_isEnforceable: Property = Property(name="isEnforceable", type=StringType)
QVTBase_Domain.attributes={QVTBase_Domain_isCheckable, QVTBase_Domain_isEnforceable}

# Rule class attributes and methods

# TypedModel class attributes and methods

# QVTBase_Function class attributes and methods

# QVTBase_Pattern class attributes and methods

# Predicate class attributes and methods

# QVTBase_Predicate class attributes and methods

# Pattern class attributes and methods

# QVTBase_FunctionParameter class attributes and methods

# Transformation class attributes and methods

# QVTBase_Transformation class attributes and methods

# Tag class attributes and methods

# QVTBase_Rule class attributes and methods

# Domain class attributes and methods

# QVTBase_TypedModel class attributes and methods

# QVTCore_Area class attributes and methods

# BottomPattern class attributes and methods

# GuardPattern class attributes and methods

# QVTCore_Assignment class attributes and methods
QVTCore_Assignment_isDefault: Property = Property(name="isDefault", type=StringType)
QVTCore_Assignment.attributes={QVTCore_Assignment_isDefault}

# Assignment class attributes and methods

# EnforcementOperation class attributes and methods

# RealizedVariable class attributes and methods

# QVTCore_CoreDomain class attributes and methods

# QVTCore_CorePattern class attributes and methods

# QVTCore_BottomPattern class attributes and methods

# CorePattern class attributes and methods

# Area class attributes and methods

# QVTCore_EnforcementOperation class attributes and methods
QVTCore_EnforcementOperation_enforcementMode: Property = Property(name="enforcementMode", type=StringType)
QVTCore_EnforcementOperation.attributes={QVTCore_EnforcementOperation_enforcementMode}

# QVTCore_GuardPattern class attributes and methods

# QVTCore_Mapping class attributes and methods

# QVTCore_PropertyAssignment class attributes and methods

# Mapping class attributes and methods

# QVTCore_VariableAssignment class attributes and methods

# QVTCore_RealizedVariable class attributes and methods

# QVTTemplate_CollectionTemplateExp class attributes and methods

# TemplateExp class attributes and methods

# PropertyTemplateItem class attributes and methods

# QVTTemplate_ObjectTemplateExp class attributes and methods

# QVTTemplate_PropertyTemplateItem class attributes and methods
QVTTemplate_PropertyTemplateItem_isOpposite: Property = Property(name="isOpposite", type=StringType)
QVTTemplate_PropertyTemplateItem.attributes={QVTTemplate_PropertyTemplateItem_isOpposite}

# ObjectTemplateExp class attributes and methods

# QVTTemplate_TemplateExp class attributes and methods

# QVTRelation_DomainPattern class attributes and methods

# RelationalTransformation class attributes and methods

# QVTRelation_OppositePropertyCallExp class attributes and methods

# PropertyCallExp class attributes and methods

# QVTRelation_Relation class attributes and methods
QVTRelation_Relation_isTopLevel: Property = Property(name="isTopLevel", type=StringType)
QVTRelation_Relation.attributes={QVTRelation_Relation_isTopLevel}

# QVTRelation_Key class attributes and methods

# QVTRelation_RelationCallExp class attributes and methods

# RelationImplementation class attributes and methods

# QVTRelation_RelationDomain class attributes and methods

# RelationDomainAssignment class attributes and methods

# DomainPattern class attributes and methods

# QVTRelation_RelationDomainAssignment class attributes and methods

# Relation class attributes and methods

# QVTRelation_RelationImplementation class attributes and methods

# QVTRelation_RelationalTransformation class attributes and methods

# Key class attributes and methods

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

# QVTOperational_ImperativeOperation class attributes and methods
QVTOperational_ImperativeOperation_isBlackbox: Property = Property(name="isBlackbox", type=StringType)
QVTOperational_ImperativeOperation.attributes={QVTOperational_ImperativeOperation_isBlackbox}

# VarParameter class attributes and methods

# QVTOperational_Library class attributes and methods

# Module class attributes and methods

# QVTOperational_EntryOperation class attributes and methods

# QVTOperational_MappingCallExp class attributes and methods
QVTOperational_MappingCallExp_isStrict: Property = Property(name="isStrict", type=StringType)
QVTOperational_MappingCallExp.attributes={QVTOperational_MappingCallExp_isStrict}

# ImperativeCallExp class attributes and methods

# QVTOperational_MappingOperation class attributes and methods

# MappingOperation class attributes and methods

# QVTOperational_MappingBody class attributes and methods

# ModelParameter class attributes and methods

# RelationDomain class attributes and methods

# QVTOperational_ModelParameter class attributes and methods

# QVTOperational_ModelType class attributes and methods
QVTOperational_ModelType_conformanceKind: Property = Property(name="conformanceKind", type=StringType)
QVTOperational_ModelType.attributes={QVTOperational_ModelType_conformanceKind}

# QVTOperational_MappingParameter class attributes and methods

# QVTOperational_Module class attributes and methods
QVTOperational_Module_isBlackbox: Property = Property(name="isBlackbox", type=StringType)
QVTOperational_Module.attributes={QVTOperational_Module_isBlackbox}

# EntryOperation class attributes and methods

# ModuleImport class attributes and methods

# ModelType class attributes and methods

# QVTOperational_ModuleImport class attributes and methods
QVTOperational_ModuleImport_kind: Property = Property(name="kind", type=StringType)
QVTOperational_ModuleImport.attributes={QVTOperational_ModuleImport_kind}

# QVTOperational_ObjectExp class attributes and methods

# InstantiationExp class attributes and methods

# ConstructorBody class attributes and methods

# QVTOperational_OperationBody class attributes and methods

# QVTOperational_OperationalTransformation class attributes and methods

# QVTOperational_ResolveExp class attributes and methods
QVTOperational_ResolveExp_isDeferred: Property = Property(name="isDeferred", type=StringType)
QVTOperational_ResolveExp_isInverse: Property = Property(name="isInverse", type=StringType)
QVTOperational_ResolveExp_one: Property = Property(name="one", type=StringType)
QVTOperational_ResolveExp.attributes={QVTOperational_ResolveExp_isDeferred, QVTOperational_ResolveExp_isInverse, QVTOperational_ResolveExp_one}

# QVTOperational_ResolveInExp class attributes and methods

# ResolveExp class attributes and methods

# QVTOperational_VarParameter class attributes and methods
QVTOperational_VarParameter_kind: Property = Property(name="kind", type=StringType)
QVTOperational_VarParameter.attributes={QVTOperational_VarParameter_kind}

# Relationships
ownedAttribute0: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute0",
    ends={
        Property(name="EMOF_Class", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="Property", type=EMOF_Class, multiplicity=Multiplicity(1, 1))
    }
)
ownedOperation1: BinaryAssociation = BinaryAssociation(
    name="ownedOperation1",
    ends={
        Property(name="Operation", type=EMOF_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Class2", type=Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass3: BinaryAssociation = BinaryAssociation(
    name="superClass3",
    ends={
        Property(name="Class", type=EMOF_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Class4", type=Class_, multiplicity=Multiplicity(0, 9999))
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
        Property(name="EnumerationLiteral", type=EMOF_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Enumeration", type=EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotatedElement5: BinaryAssociation = BinaryAssociation(
    name="annotatedElement5",
    ends={
        Property(name="NamedElement", type=EMOF_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Comment", type=NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
package9: BinaryAssociation = BinaryAssociation(
    name="package9",
    ends={
        Property(name="Package", type=EMOF_Factory, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Factory", type=Package, multiplicity=Multiplicity(1, 1))
    }
)
enumeration8: BinaryAssociation = BinaryAssociation(
    name="enumeration8",
    ends={
        Property(name="Enumeration", type=EMOF_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_EnumerationLiteral", type=Enumeration_, multiplicity=Multiplicity(0, 1))
    }
)
class10: BinaryAssociation = BinaryAssociation(
    name="class10",
    ends={
        Property(name="Class11", type=EMOF_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Operation", type=Class_, multiplicity=Multiplicity(0, 1))
    }
)
nestedPackage16: BinaryAssociation = BinaryAssociation(
    name="nestedPackage16",
    ends={
        Property(name="Package17", type=EMOF_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Package", type=Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestingPackage18: BinaryAssociation = BinaryAssociation(
    name="nestingPackage18",
    ends={
        Property(name="Package20", type=EMOF_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Package19", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
ownedType21: BinaryAssociation = BinaryAssociation(
    name="ownedType21",
    ends={
        Property(name="Type23", type=EMOF_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Package22", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operation24: BinaryAssociation = BinaryAssociation(
    name="operation24",
    ends={
        Property(name="Operation25", type=EMOF_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Parameter", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
ownedParameter12: BinaryAssociation = BinaryAssociation(
    name="ownedParameter12",
    ends={
        Property(name="Parameter", type=EMOF_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Operation13", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
raisedException14: BinaryAssociation = BinaryAssociation(
    name="raisedException14",
    ends={
        Property(name="Type", type=EMOF_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Operation15", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
opposite28: BinaryAssociation = BinaryAssociation(
    name="opposite28",
    ends={
        Property(name="Property30", type=EMOF_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Property29", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
class26: BinaryAssociation = BinaryAssociation(
    name="class26",
    ends={
        Property(name="Class27", type=EMOF_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Property", type=Class_, multiplicity=Multiplicity(0, 1))
    }
)
element31: BinaryAssociation = BinaryAssociation(
    name="element31",
    ends={
        Property(name="Element", type=EMOF_Tag, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Tag", type=Element, multiplicity=Multiplicity(0, 9999))
    }
)
type34: BinaryAssociation = BinaryAssociation(
    name="type34",
    ends={
        Property(name="Type35", type=EMOF_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_TypedElement", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
package32: BinaryAssociation = BinaryAssociation(
    name="package32",
    ends={
        Property(name="Package33", type=EMOF_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Type", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
item37: BinaryAssociation = BinaryAssociation(
    name="item37",
    ends={
        Property(name="OclExpression38", type=EssentialOCL_CollectionItem, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_CollectionItem", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source36: BinaryAssociation = BinaryAssociation(
    name="source36",
    ends={
        Property(name="OclExpression", type=EssentialOCL_CallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_CallExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
part39: BinaryAssociation = BinaryAssociation(
    name="part39",
    ends={
        Property(name="CollectionLiteralPart", type=EssentialOCL_CollectionLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_CollectionLiteralExp", type=CollectionLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collectionLiteralExp40: BinaryAssociation = BinaryAssociation(
    name="collectionLiteralExp40",
    ends={
        Property(name="CollectionLiteralExp", type=EssentialOCL_CollectionLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_CollectionLiteralPart", type=CollectionLiteralExp, multiplicity=Multiplicity(1, 1))
    }
)
first41: BinaryAssociation = BinaryAssociation(
    name="first41",
    ends={
        Property(name="OclExpression42", type=EssentialOCL_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_CollectionRange", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
last43: BinaryAssociation = BinaryAssociation(
    name="last43",
    ends={
        Property(name="OclExpression45", type=EssentialOCL_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_CollectionRange44", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referredEnumLiteral48: BinaryAssociation = BinaryAssociation(
    name="referredEnumLiteral48",
    ends={
        Property(name="EnumerationLiteral49", type=EssentialOCL_EnumLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_EnumLiteralExp", type=EnumerationLiteral, multiplicity=Multiplicity(0, 1))
    }
)
bodyExpression50: BinaryAssociation = BinaryAssociation(
    name="bodyExpression50",
    ends={
        Property(name="OclExpression51", type=EssentialOCL_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_ExpressionInOcl", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
contextVariable52: BinaryAssociation = BinaryAssociation(
    name="contextVariable52",
    ends={
        Property(name="Variable", type=EssentialOCL_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_ExpressionInOcl53", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
generatedType54: BinaryAssociation = BinaryAssociation(
    name="generatedType54",
    ends={
        Property(name="Type56", type=EssentialOCL_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_ExpressionInOcl55", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elementType46: BinaryAssociation = BinaryAssociation(
    name="elementType46",
    ends={
        Property(name="Type47", type=EssentialOCL_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_CollectionType", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
elseExpression65: BinaryAssociation = BinaryAssociation(
    name="elseExpression65",
    ends={
        Property(name="EssentialOCL_IfExp66", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="OclExpression67", type=EssentialOCL_IfExp, multiplicity=Multiplicity(1, 1))
    }
)
thenExpression68: BinaryAssociation = BinaryAssociation(
    name="thenExpression68",
    ends={
        Property(name="OclExpression70", type=EssentialOCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_IfExp69", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameterVariable57: BinaryAssociation = BinaryAssociation(
    name="parameterVariable57",
    ends={
        Property(name="Variable59", type=EssentialOCL_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_ExpressionInOcl58", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resultVariable60: BinaryAssociation = BinaryAssociation(
    name="resultVariable60",
    ends={
        Property(name="Variable62", type=EssentialOCL_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_ExpressionInOcl61", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition63: BinaryAssociation = BinaryAssociation(
    name="condition63",
    ends={
        Property(name="OclExpression64", type=EssentialOCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_IfExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in73: BinaryAssociation = BinaryAssociation(
    name="in73",
    ends={
        Property(name="OclExpression74", type=EssentialOCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_LetExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result71: BinaryAssociation = BinaryAssociation(
    name="result71",
    ends={
        Property(name="Variable72", type=EssentialOCL_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_IterateExp", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
iterator80: BinaryAssociation = BinaryAssociation(
    name="iterator80",
    ends={
        Property(name="Variable82", type=EssentialOCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_LoopExp81", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable75: BinaryAssociation = BinaryAssociation(
    name="variable75",
    ends={
        Property(name="Variable77", type=EssentialOCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_LetExp76", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body78: BinaryAssociation = BinaryAssociation(
    name="body78",
    ends={
        Property(name="OclExpression79", type=EssentialOCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_LoopExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referredProperty88: BinaryAssociation = BinaryAssociation(
    name="referredProperty88",
    ends={
        Property(name="Property89", type=EssentialOCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_PropertyCallExp", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
argument83: BinaryAssociation = BinaryAssociation(
    name="argument83",
    ends={
        Property(name="OclExpression84", type=EssentialOCL_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_OperationCallExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredOperation85: BinaryAssociation = BinaryAssociation(
    name="referredOperation85",
    ends={
        Property(name="Operation87", type=EssentialOCL_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_OperationCallExp86", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
attribute91: BinaryAssociation = BinaryAssociation(
    name="attribute91",
    ends={
        Property(name="Property92", type=EssentialOCL_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_TupleLiteralPart", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
tupleLiteralExp93: BinaryAssociation = BinaryAssociation(
    name="tupleLiteralExp93",
    ends={
        Property(name="TupleLiteralExp", type=EssentialOCL_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_TupleLiteralPart94", type=TupleLiteralExp, multiplicity=Multiplicity(0, 1))
    }
)
value95: BinaryAssociation = BinaryAssociation(
    name="value95",
    ends={
        Property(name="OclExpression97", type=EssentialOCL_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_TupleLiteralPart96", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
part90: BinaryAssociation = BinaryAssociation(
    name="part90",
    ends={
        Property(name="TupleLiteralPart", type=EssentialOCL_TupleLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_TupleLiteralExp", type=TupleLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initExpression100: BinaryAssociation = BinaryAssociation(
    name="initExpression100",
    ends={
        Property(name="EssentialOCL_Variable", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="OclExpression101", type=EssentialOCL_Variable, multiplicity=Multiplicity(1, 1))
    }
)
letExp102: BinaryAssociation = BinaryAssociation(
    name="letExp102",
    ends={
        Property(name="LetExp", type=EssentialOCL_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_Variable103", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
representedParameter104: BinaryAssociation = BinaryAssociation(
    name="representedParameter104",
    ends={
        Property(name="Parameter106", type=EssentialOCL_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_Variable105", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
referredType98: BinaryAssociation = BinaryAssociation(
    name="referredType98",
    ends={
        Property(name="Type99", type=EssentialOCL_TypeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_TypeExp", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
body109: BinaryAssociation = BinaryAssociation(
    name="body109",
    ends={
        Property(name="OclExpression110", type=ImperativeOCL_AltExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_AltExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition111: BinaryAssociation = BinaryAssociation(
    name="condition111",
    ends={
        Property(name="OclExpression113", type=ImperativeOCL_AltExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_AltExp112", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referredVariable107: BinaryAssociation = BinaryAssociation(
    name="referredVariable107",
    ends={
        Property(name="Variable108", type=EssentialOCL_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_VariableExp", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
log116: BinaryAssociation = BinaryAssociation(
    name="log116",
    ends={
        Property(name="LogExp", type=ImperativeOCL_AssertExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_AssertExp117", type=LogExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultValue118: BinaryAssociation = BinaryAssociation(
    name="defaultValue118",
    ends={
        Property(name="OclExpression119", type=ImperativeOCL_AssignExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_AssignExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left120: BinaryAssociation = BinaryAssociation(
    name="left120",
    ends={
        Property(name="OclExpression122", type=ImperativeOCL_AssignExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_AssignExp121", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
assertion114: BinaryAssociation = BinaryAssociation(
    name="assertion114",
    ends={
        Property(name="OclExpression115", type=ImperativeOCL_AssertExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_AssertExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body126: BinaryAssociation = BinaryAssociation(
    name="body126",
    ends={
        Property(name="OclExpression127", type=ImperativeOCL_BlockExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_BlockExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body128: BinaryAssociation = BinaryAssociation(
    name="body128",
    ends={
        Property(name="OclExpression129", type=ImperativeOCL_CatchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_CatchExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exception130: BinaryAssociation = BinaryAssociation(
    name="exception130",
    ends={
        Property(name="Type132", type=ImperativeOCL_CatchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_CatchExp131", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
value123: BinaryAssociation = BinaryAssociation(
    name="value123",
    ends={
        Property(name="OclExpression125", type=ImperativeOCL_AssignExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_AssignExp124", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body133: BinaryAssociation = BinaryAssociation(
    name="body133",
    ends={
        Property(name="OclExpression134", type=ImperativeOCL_ComputeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_ComputeExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnedElement135: BinaryAssociation = BinaryAssociation(
    name="returnedElement135",
    ends={
        Property(name="Variable137", type=ImperativeOCL_ComputeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_ComputeExp136", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
part138: BinaryAssociation = BinaryAssociation(
    name="part138",
    ends={
        Property(name="DictLiteralPart", type=ImperativeOCL_DictLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_DictLiteralExp", type=DictLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value141: BinaryAssociation = BinaryAssociation(
    name="value141",
    ends={
        Property(name="OclExpression143", type=ImperativeOCL_DictLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_DictLiteralPart142", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
keyType144: BinaryAssociation = BinaryAssociation(
    name="keyType144",
    ends={
        Property(name="Type145", type=ImperativeOCL_DictionaryType, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_DictionaryType", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
key139: BinaryAssociation = BinaryAssociation(
    name="key139",
    ends={
        Property(name="OclExpression140", type=ImperativeOCL_DictLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_DictLiteralPart", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition148: BinaryAssociation = BinaryAssociation(
    name="condition148",
    ends={
        Property(name="OclExpression149", type=ImperativeOCL_ImperativeLoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_ImperativeLoopExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
argument150: BinaryAssociation = BinaryAssociation(
    name="argument150",
    ends={
        Property(name="OclExpression151", type=ImperativeOCL_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_InstantiationExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extent152: BinaryAssociation = BinaryAssociation(
    name="extent152",
    ends={
        Property(name="Variable154", type=ImperativeOCL_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_InstantiationExp153", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
target146: BinaryAssociation = BinaryAssociation(
    name="target146",
    ends={
        Property(name="Variable147", type=ImperativeOCL_ImperativeIterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_ImperativeIterateExp", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
element158: BinaryAssociation = BinaryAssociation(
    name="element158",
    ends={
        Property(name="ImperativeOCL_ListLiteralExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="OclExpression159", type=ImperativeOCL_ListLiteralExp, multiplicity=Multiplicity(1, 1))
    }
)
condition160: BinaryAssociation = BinaryAssociation(
    name="condition160",
    ends={
        Property(name="OclExpression161", type=ImperativeOCL_LogExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_LogExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
part162: BinaryAssociation = BinaryAssociation(
    name="part162",
    ends={
        Property(name="OrderedTupleLiteralPart", type=ImperativeOCL_OrderedTupleLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_OrderedTupleLiteralExp", type=OrderedTupleLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instantiatedClass155: BinaryAssociation = BinaryAssociation(
    name="instantiatedClass155",
    ends={
        Property(name="Class157", type=ImperativeOCL_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_InstantiationExp156", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
elementType165: BinaryAssociation = BinaryAssociation(
    name="elementType165",
    ends={
        Property(name="Type166", type=ImperativeOCL_OrderedTupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_OrderedTupleType", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
argument167: BinaryAssociation = BinaryAssociation(
    name="argument167",
    ends={
        Property(name="OclExpression168", type=ImperativeOCL_RaiseExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_RaiseExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value163: BinaryAssociation = BinaryAssociation(
    name="value163",
    ends={
        Property(name="OclExpression164", type=ImperativeOCL_OrderedTupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_OrderedTupleLiteralPart", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value172: BinaryAssociation = BinaryAssociation(
    name="value172",
    ends={
        Property(name="OclExpression173", type=ImperativeOCL_ReturnExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_ReturnExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exception169: BinaryAssociation = BinaryAssociation(
    name="exception169",
    ends={
        Property(name="Type171", type=ImperativeOCL_RaiseExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_RaiseExp170", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
exceptClause178: BinaryAssociation = BinaryAssociation(
    name="exceptClause178",
    ends={
        Property(name="CatchExp", type=ImperativeOCL_TryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_TryExp", type=CatchExp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tryBody179: BinaryAssociation = BinaryAssociation(
    name="tryBody179",
    ends={
        Property(name="OclExpression181", type=ImperativeOCL_TryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_TryExp180", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
alternativePart174: BinaryAssociation = BinaryAssociation(
    name="alternativePart174",
    ends={
        Property(name="AltExp", type=ImperativeOCL_SwitchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_SwitchExp", type=AltExp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elsePart175: BinaryAssociation = BinaryAssociation(
    name="elsePart175",
    ends={
        Property(name="OclExpression177", type=ImperativeOCL_SwitchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_SwitchExp176", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition184: BinaryAssociation = BinaryAssociation(
    name="condition184",
    ends={
        Property(name="ImperativeOCL_Typedef185", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="OclExpression186", type=ImperativeOCL_Typedef, multiplicity=Multiplicity(1, 1))
    }
)
item187: BinaryAssociation = BinaryAssociation(
    name="item187",
    ends={
        Property(name="OclExpression188", type=ImperativeOCL_UnlinkExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_UnlinkExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target189: BinaryAssociation = BinaryAssociation(
    name="target189",
    ends={
        Property(name="OclExpression191", type=ImperativeOCL_UnlinkExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_UnlinkExp190", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
base182: BinaryAssociation = BinaryAssociation(
    name="base182",
    ends={
        Property(name="Type183", type=ImperativeOCL_Typedef, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_Typedef", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
targetVariable194: BinaryAssociation = BinaryAssociation(
    name="targetVariable194",
    ends={
        Property(name="Variable196", type=ImperativeOCL_UnpackExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_UnpackExp195", type=Variable, multiplicity=Multiplicity(1, 9999))
    }
)
referredVariable197: BinaryAssociation = BinaryAssociation(
    name="referredVariable197",
    ends={
        Property(name="Variable198", type=ImperativeOCL_VariableInitExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_VariableInitExp", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body199: BinaryAssociation = BinaryAssociation(
    name="body199",
    ends={
        Property(name="OclExpression200", type=ImperativeOCL_WhileExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_WhileExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source192: BinaryAssociation = BinaryAssociation(
    name="source192",
    ends={
        Property(name="OclExpression193", type=ImperativeOCL_UnpackExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_UnpackExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rule204: BinaryAssociation = BinaryAssociation(
    name="rule204",
    ends={
        Property(name="Rule", type=QVTBase_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTBase_Domain", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
typedModel205: BinaryAssociation = BinaryAssociation(
    name="typedModel205",
    ends={
        Property(name="TypedModel", type=QVTBase_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTBase_Domain206", type=TypedModel, multiplicity=Multiplicity(0, 1))
    }
)
queryExpression207: BinaryAssociation = BinaryAssociation(
    name="queryExpression207",
    ends={
        Property(name="OclExpression208", type=QVTBase_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTBase_Function", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition201: BinaryAssociation = BinaryAssociation(
    name="condition201",
    ends={
        Property(name="OclExpression203", type=ImperativeOCL_WhileExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_WhileExp202", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bindsTo209: BinaryAssociation = BinaryAssociation(
    name="bindsTo209",
    ends={
        Property(name="Variable210", type=QVTBase_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTBase_Pattern", type=Variable, multiplicity=Multiplicity(0, 9999))
    }
)
predicate211: BinaryAssociation = BinaryAssociation(
    name="predicate211",
    ends={
        Property(name="Predicate", type=QVTBase_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTBase_Pattern212", type=Predicate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conditionExpression213: BinaryAssociation = BinaryAssociation(
    name="conditionExpression213",
    ends={
        Property(name="OclExpression214", type=QVTBase_Predicate, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTBase_Predicate", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
pattern215: BinaryAssociation = BinaryAssociation(
    name="pattern215",
    ends={
        Property(name="Pattern", type=QVTBase_Predicate, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTBase_Predicate216", type=Pattern, multiplicity=Multiplicity(1, 1))
    }
)
overrides218: BinaryAssociation = BinaryAssociation(
    name="overrides218",
    ends={
        Property(name="Rule220", type=QVTBase_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTBase_Rule219", type=Rule, multiplicity=Multiplicity(0, 1))
    }
)
transformation221: BinaryAssociation = BinaryAssociation(
    name="transformation221",
    ends={
        Property(name="Transformation", type=QVTBase_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTBase_Rule222", type=Transformation, multiplicity=Multiplicity(0, 1))
    }
)
extends223: BinaryAssociation = BinaryAssociation(
    name="extends223",
    ends={
        Property(name="Transformation224", type=QVTBase_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTBase_Transformation", type=Transformation, multiplicity=Multiplicity(0, 1))
    }
)
modelParameter225: BinaryAssociation = BinaryAssociation(
    name="modelParameter225",
    ends={
        Property(name="TypedModel227", type=QVTBase_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTBase_Transformation226", type=TypedModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTag228: BinaryAssociation = BinaryAssociation(
    name="ownedTag228",
    ends={
        Property(name="Tag", type=QVTBase_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTBase_Transformation229", type=Tag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
domain217: BinaryAssociation = BinaryAssociation(
    name="domain217",
    ends={
        Property(name="Domain", type=QVTBase_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTBase_Rule", type=Domain, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependsOn233: BinaryAssociation = BinaryAssociation(
    name="dependsOn233",
    ends={
        Property(name="TypedModel234", type=QVTBase_TypedModel, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTBase_TypedModel", type=TypedModel, multiplicity=Multiplicity(0, 9999))
    }
)
transformation235: BinaryAssociation = BinaryAssociation(
    name="transformation235",
    ends={
        Property(name="Transformation237", type=QVTBase_TypedModel, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTBase_TypedModel236", type=Transformation, multiplicity=Multiplicity(1, 1))
    }
)
usedPackage238: BinaryAssociation = BinaryAssociation(
    name="usedPackage238",
    ends={
        Property(name="Package240", type=QVTBase_TypedModel, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTBase_TypedModel239", type=Package, multiplicity=Multiplicity(1, 9999))
    }
)
bottomPattern241: BinaryAssociation = BinaryAssociation(
    name="bottomPattern241",
    ends={
        Property(name="BottomPattern", type=QVTCore_Area, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTCore_Area", type=BottomPattern, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rule230: BinaryAssociation = BinaryAssociation(
    name="rule230",
    ends={
        Property(name="Rule232", type=QVTBase_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTBase_Transformation231", type=Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guardPattern242: BinaryAssociation = BinaryAssociation(
    name="guardPattern242",
    ends={
        Property(name="GuardPattern", type=QVTCore_Area, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTCore_Area243", type=GuardPattern, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bottomPattern244: BinaryAssociation = BinaryAssociation(
    name="bottomPattern244",
    ends={
        Property(name="BottomPattern245", type=QVTCore_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTCore_Assignment", type=BottomPattern, multiplicity=Multiplicity(1, 1))
    }
)
value246: BinaryAssociation = BinaryAssociation(
    name="value246",
    ends={
        Property(name="OclExpression248", type=QVTCore_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTCore_Assignment247", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
assignment250: BinaryAssociation = BinaryAssociation(
    name="assignment250",
    ends={
        Property(name="Assignment", type=QVTCore_BottomPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTCore_BottomPattern251", type=Assignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enforcementOperation252: BinaryAssociation = BinaryAssociation(
    name="enforcementOperation252",
    ends={
        Property(name="EnforcementOperation", type=QVTCore_BottomPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTCore_BottomPattern253", type=EnforcementOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
realizedVariable254: BinaryAssociation = BinaryAssociation(
    name="realizedVariable254",
    ends={
        Property(name="RealizedVariable", type=QVTCore_BottomPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTCore_BottomPattern255", type=RealizedVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
area249: BinaryAssociation = BinaryAssociation(
    name="area249",
    ends={
        Property(name="Area", type=QVTCore_BottomPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTCore_BottomPattern", type=Area, multiplicity=Multiplicity(1, 1))
    }
)
bottomPattern258: BinaryAssociation = BinaryAssociation(
    name="bottomPattern258",
    ends={
        Property(name="BottomPattern259", type=QVTCore_EnforcementOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTCore_EnforcementOperation", type=BottomPattern, multiplicity=Multiplicity(0, 1))
    }
)
operationCallExp260: BinaryAssociation = BinaryAssociation(
    name="operationCallExp260",
    ends={
        Property(name="OperationCallExp", type=QVTCore_EnforcementOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTCore_EnforcementOperation261", type=OperationCallExp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
area262: BinaryAssociation = BinaryAssociation(
    name="area262",
    ends={
        Property(name="Area263", type=QVTCore_GuardPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTCore_GuardPattern", type=Area, multiplicity=Multiplicity(1, 1))
    }
)
variable256: BinaryAssociation = BinaryAssociation(
    name="variable256",
    ends={
        Property(name="Variable257", type=QVTCore_CorePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTCore_CorePattern", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
local265: BinaryAssociation = BinaryAssociation(
    name="local265",
    ends={
        Property(name="Mapping267", type=QVTCore_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTCore_Mapping266", type=Mapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refinement268: BinaryAssociation = BinaryAssociation(
    name="refinement268",
    ends={
        Property(name="Mapping270", type=QVTCore_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTCore_Mapping269", type=Mapping, multiplicity=Multiplicity(0, 9999))
    }
)
specification271: BinaryAssociation = BinaryAssociation(
    name="specification271",
    ends={
        Property(name="Mapping273", type=QVTCore_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTCore_Mapping272", type=Mapping, multiplicity=Multiplicity(0, 9999))
    }
)
slotExpression274: BinaryAssociation = BinaryAssociation(
    name="slotExpression274",
    ends={
        Property(name="OclExpression275", type=QVTCore_PropertyAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTCore_PropertyAssignment", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context264: BinaryAssociation = BinaryAssociation(
    name="context264",
    ends={
        Property(name="Mapping", type=QVTCore_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTCore_Mapping", type=Mapping, multiplicity=Multiplicity(0, 1))
    }
)
targetVariable279: BinaryAssociation = BinaryAssociation(
    name="targetVariable279",
    ends={
        Property(name="Variable280", type=QVTCore_VariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTCore_VariableAssignment", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
targetProperty276: BinaryAssociation = BinaryAssociation(
    name="targetProperty276",
    ends={
        Property(name="Property278", type=QVTCore_PropertyAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTCore_PropertyAssignment277", type=Property_, multiplicity=Multiplicity(1, 1))
    }
)
member281: BinaryAssociation = BinaryAssociation(
    name="member281",
    ends={
        Property(name="OclExpression282", type=QVTTemplate_CollectionTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTTemplate_CollectionTemplateExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredCollectionType283: BinaryAssociation = BinaryAssociation(
    name="referredCollectionType283",
    ends={
        Property(name="QVTTemplate_CollectionTemplateExp284", type=CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="CollectionType", type=QVTTemplate_CollectionTemplateExp, multiplicity=Multiplicity(1, 1))
    }
)
rest285: BinaryAssociation = BinaryAssociation(
    name="rest285",
    ends={
        Property(name="Variable287", type=QVTTemplate_CollectionTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTTemplate_CollectionTemplateExp286", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
part288: BinaryAssociation = BinaryAssociation(
    name="part288",
    ends={
        Property(name="PropertyTemplateItem", type=QVTTemplate_ObjectTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTTemplate_ObjectTemplateExp", type=PropertyTemplateItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredClass289: BinaryAssociation = BinaryAssociation(
    name="referredClass289",
    ends={
        Property(name="Class291", type=QVTTemplate_ObjectTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTTemplate_ObjectTemplateExp290", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
objContainer292: BinaryAssociation = BinaryAssociation(
    name="objContainer292",
    ends={
        Property(name="ObjectTemplateExp", type=QVTTemplate_PropertyTemplateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTTemplate_PropertyTemplateItem", type=ObjectTemplateExp, multiplicity=Multiplicity(1, 1))
    }
)
referredProperty293: BinaryAssociation = BinaryAssociation(
    name="referredProperty293",
    ends={
        Property(name="Property295", type=QVTTemplate_PropertyTemplateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTTemplate_PropertyTemplateItem294", type=Property_, multiplicity=Multiplicity(1, 1))
    }
)
value296: BinaryAssociation = BinaryAssociation(
    name="value296",
    ends={
        Property(name="OclExpression298", type=QVTTemplate_PropertyTemplateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTTemplate_PropertyTemplateItem297", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bindsTo299: BinaryAssociation = BinaryAssociation(
    name="bindsTo299",
    ends={
        Property(name="Variable300", type=QVTTemplate_TemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTTemplate_TemplateExp", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
where301: BinaryAssociation = BinaryAssociation(
    name="where301",
    ends={
        Property(name="OclExpression303", type=QVTTemplate_TemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTTemplate_TemplateExp302", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifies305: BinaryAssociation = BinaryAssociation(
    name="identifies305",
    ends={
        Property(name="Class306", type=QVTRelation_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_Key", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
oppositePart307: BinaryAssociation = BinaryAssociation(
    name="oppositePart307",
    ends={
        Property(name="Property309", type=QVTRelation_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_Key308", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)
part310: BinaryAssociation = BinaryAssociation(
    name="part310",
    ends={
        Property(name="Property312", type=QVTRelation_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_Key311", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)
transformation313: BinaryAssociation = BinaryAssociation(
    name="transformation313",
    ends={
        Property(name="RelationalTransformation", type=QVTRelation_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_Key314", type=RelationalTransformation, multiplicity=Multiplicity(0, 1))
    }
)
templateExpression304: BinaryAssociation = BinaryAssociation(
    name="templateExpression304",
    ends={
        Property(name="TemplateExp", type=QVTRelation_DomainPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_DomainPattern", type=TemplateExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable316: BinaryAssociation = BinaryAssociation(
    name="variable316",
    ends={
        Property(name="Variable318", type=QVTRelation_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_Relation317", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
when319: BinaryAssociation = BinaryAssociation(
    name="when319",
    ends={
        Property(name="Pattern321", type=QVTRelation_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_Relation320", type=Pattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
where322: BinaryAssociation = BinaryAssociation(
    name="where322",
    ends={
        Property(name="Pattern324", type=QVTRelation_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_Relation323", type=Pattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
argument325: BinaryAssociation = BinaryAssociation(
    name="argument325",
    ends={
        Property(name="OclExpression326", type=QVTRelation_RelationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_RelationCallExp", type=OclExpression, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
operationalImpl315: BinaryAssociation = BinaryAssociation(
    name="operationalImpl315",
    ends={
        Property(name="RelationImplementation", type=QVTRelation_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_Relation", type=RelationImplementation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultAssignment329: BinaryAssociation = BinaryAssociation(
    name="defaultAssignment329",
    ends={
        Property(name="RelationDomainAssignment", type=QVTRelation_RelationDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_RelationDomain", type=RelationDomainAssignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pattern330: BinaryAssociation = BinaryAssociation(
    name="pattern330",
    ends={
        Property(name="DomainPattern", type=QVTRelation_RelationDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_RelationDomain331", type=DomainPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rootVariable332: BinaryAssociation = BinaryAssociation(
    name="rootVariable332",
    ends={
        Property(name="Variable334", type=QVTRelation_RelationDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_RelationDomain333", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
referredRelation327: BinaryAssociation = BinaryAssociation(
    name="referredRelation327",
    ends={
        Property(name="Relation", type=QVTRelation_RelationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_RelationCallExp328", type=Relation, multiplicity=Multiplicity(1, 1))
    }
)
variable337: BinaryAssociation = BinaryAssociation(
    name="variable337",
    ends={
        Property(name="Variable339", type=QVTRelation_RelationDomainAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_RelationDomainAssignment338", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
impl340: BinaryAssociation = BinaryAssociation(
    name="impl340",
    ends={
        Property(name="Operation341", type=QVTRelation_RelationImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_RelationImplementation", type=Operation, multiplicity=Multiplicity(1, 1))
    }
)
inDirectionOf342: BinaryAssociation = BinaryAssociation(
    name="inDirectionOf342",
    ends={
        Property(name="TypedModel344", type=QVTRelation_RelationImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_RelationImplementation343", type=TypedModel, multiplicity=Multiplicity(1, 1))
    }
)
relation345: BinaryAssociation = BinaryAssociation(
    name="relation345",
    ends={
        Property(name="Relation347", type=QVTRelation_RelationImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_RelationImplementation346", type=Relation, multiplicity=Multiplicity(0, 1))
    }
)
valueExp335: BinaryAssociation = BinaryAssociation(
    name="valueExp335",
    ends={
        Property(name="OclExpression336", type=QVTRelation_RelationDomainAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_RelationDomainAssignment", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context349: BinaryAssociation = BinaryAssociation(
    name="context349",
    ends={
        Property(name="Class350", type=QVTOperational_ContextualProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ContextualProperty", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
initExpression351: BinaryAssociation = BinaryAssociation(
    name="initExpression351",
    ends={
        Property(name="OclExpression353", type=QVTOperational_ContextualProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ContextualProperty352", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedKey348: BinaryAssociation = BinaryAssociation(
    name="ownedKey348",
    ends={
        Property(name="Key", type=QVTRelation_RelationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_RelationalTransformation", type=Key, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body357: BinaryAssociation = BinaryAssociation(
    name="body357",
    ends={
        Property(name="OperationBody", type=QVTOperational_ImperativeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ImperativeOperation", type=OperationBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
context358: BinaryAssociation = BinaryAssociation(
    name="context358",
    ends={
        Property(name="VarParameter", type=QVTOperational_ImperativeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ImperativeOperation359", type=VarParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
overridden360: BinaryAssociation = BinaryAssociation(
    name="overridden360",
    ends={
        Property(name="ImperativeOperation", type=QVTOperational_ImperativeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ImperativeOperation361", type=ImperativeOperation, multiplicity=Multiplicity(0, 1))
    }
)
result362: BinaryAssociation = BinaryAssociation(
    name="result362",
    ends={
        Property(name="VarParameter364", type=QVTOperational_ImperativeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ImperativeOperation363", type=VarParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
overridden354: BinaryAssociation = BinaryAssociation(
    name="overridden354",
    ends={
        Property(name="Property356", type=QVTOperational_ContextualProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ContextualProperty355", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
initSection367: BinaryAssociation = BinaryAssociation(
    name="initSection367",
    ends={
        Property(name="OclExpression369", type=QVTOperational_MappingBody, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingBody368", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
disjunct370: BinaryAssociation = BinaryAssociation(
    name="disjunct370",
    ends={
        Property(name="MappingOperation", type=QVTOperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingOperation", type=MappingOperation, multiplicity=Multiplicity(0, 9999))
    }
)
inherited371: BinaryAssociation = BinaryAssociation(
    name="inherited371",
    ends={
        Property(name="MappingOperation373", type=QVTOperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingOperation372", type=MappingOperation, multiplicity=Multiplicity(0, 9999))
    }
)
endSection365: BinaryAssociation = BinaryAssociation(
    name="endSection365",
    ends={
        Property(name="OclExpression366", type=QVTOperational_MappingBody, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingBody", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refinedRelation377: BinaryAssociation = BinaryAssociation(
    name="refinedRelation377",
    ends={
        Property(name="Relation379", type=QVTOperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingOperation378", type=Relation, multiplicity=Multiplicity(0, 1))
    }
)
when380: BinaryAssociation = BinaryAssociation(
    name="when380",
    ends={
        Property(name="OclExpression382", type=QVTOperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingOperation381", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
where383: BinaryAssociation = BinaryAssociation(
    name="where383",
    ends={
        Property(name="OclExpression385", type=QVTOperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingOperation384", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
merged374: BinaryAssociation = BinaryAssociation(
    name="merged374",
    ends={
        Property(name="MappingOperation376", type=QVTOperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingOperation375", type=MappingOperation, multiplicity=Multiplicity(0, 9999))
    }
)
extent386: BinaryAssociation = BinaryAssociation(
    name="extent386",
    ends={
        Property(name="ModelParameter", type=QVTOperational_MappingParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingParameter", type=ModelParameter, multiplicity=Multiplicity(0, 1))
    }
)
referredDomain387: BinaryAssociation = BinaryAssociation(
    name="referredDomain387",
    ends={
        Property(name="RelationDomain", type=QVTOperational_MappingParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingParameter388", type=RelationDomain, multiplicity=Multiplicity(0, 1))
    }
)
additionalCondition389: BinaryAssociation = BinaryAssociation(
    name="additionalCondition389",
    ends={
        Property(name="OclExpression390", type=QVTOperational_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ModelType", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metamodel391: BinaryAssociation = BinaryAssociation(
    name="metamodel391",
    ends={
        Property(name="Package393", type=QVTOperational_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ModelType392", type=Package, multiplicity=Multiplicity(1, 9999))
    }
)
configProperty394: BinaryAssociation = BinaryAssociation(
    name="configProperty394",
    ends={
        Property(name="Property395", type=QVTOperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_Module", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)
entry396: BinaryAssociation = BinaryAssociation(
    name="entry396",
    ends={
        Property(name="EntryOperation", type=QVTOperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_Module397", type=EntryOperation, multiplicity=Multiplicity(0, 1))
    }
)
ownedVariable403: BinaryAssociation = BinaryAssociation(
    name="ownedVariable403",
    ends={
        Property(name="Variable405", type=QVTOperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_Module404", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usedModelType406: BinaryAssociation = BinaryAssociation(
    name="usedModelType406",
    ends={
        Property(name="ModelType", type=QVTOperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_Module407", type=ModelType, multiplicity=Multiplicity(0, 9999))
    }
)
binding408: BinaryAssociation = BinaryAssociation(
    name="binding408",
    ends={
        Property(name="ModelType409", type=QVTOperational_ModuleImport, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ModuleImport", type=ModelType, multiplicity=Multiplicity(0, 9999))
    }
)
importedModule410: BinaryAssociation = BinaryAssociation(
    name="importedModule410",
    ends={
        Property(name="Module", type=QVTOperational_ModuleImport, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ModuleImport411", type=Module, multiplicity=Multiplicity(1, 1))
    }
)
moduleImport398: BinaryAssociation = BinaryAssociation(
    name="moduleImport398",
    ends={
        Property(name="ModuleImport", type=QVTOperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_Module399", type=ModuleImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTag400: BinaryAssociation = BinaryAssociation(
    name="ownedTag400",
    ends={
        Property(name="Tag402", type=QVTOperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_Module401", type=Tag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
module412: BinaryAssociation = BinaryAssociation(
    name="module412",
    ends={
        Property(name="Module414", type=QVTOperational_ModuleImport, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ModuleImport413", type=Module, multiplicity=Multiplicity(0, 1))
    }
)
body415: BinaryAssociation = BinaryAssociation(
    name="body415",
    ends={
        Property(name="ConstructorBody", type=QVTOperational_ObjectExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ObjectExp", type=ConstructorBody, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referredObject416: BinaryAssociation = BinaryAssociation(
    name="referredObject416",
    ends={
        Property(name="Variable418", type=QVTOperational_ObjectExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ObjectExp417", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
content419: BinaryAssociation = BinaryAssociation(
    name="content419",
    ends={
        Property(name="OclExpression420", type=QVTOperational_OperationBody, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_OperationBody", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable424: BinaryAssociation = BinaryAssociation(
    name="variable424",
    ends={
        Property(name="Variable426", type=QVTOperational_OperationBody, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_OperationBody425", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateClass427: BinaryAssociation = BinaryAssociation(
    name="intermediateClass427",
    ends={
        Property(name="Class428", type=QVTOperational_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_OperationalTransformation", type=Class_, multiplicity=Multiplicity(0, 9999))
    }
)
intermediateProperty429: BinaryAssociation = BinaryAssociation(
    name="intermediateProperty429",
    ends={
        Property(name="Property431", type=QVTOperational_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_OperationalTransformation430", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)
operation421: BinaryAssociation = BinaryAssociation(
    name="operation421",
    ends={
        Property(name="ImperativeOperation423", type=QVTOperational_OperationBody, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_OperationBody422", type=ImperativeOperation, multiplicity=Multiplicity(0, 1))
    }
)
refined435: BinaryAssociation = BinaryAssociation(
    name="refined435",
    ends={
        Property(name="RelationalTransformation437", type=QVTOperational_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_OperationalTransformation436", type=RelationalTransformation, multiplicity=Multiplicity(0, 1))
    }
)
relation438: BinaryAssociation = BinaryAssociation(
    name="relation438",
    ends={
        Property(name="Relation440", type=QVTOperational_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_OperationalTransformation439", type=Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modelParameter432: BinaryAssociation = BinaryAssociation(
    name="modelParameter432",
    ends={
        Property(name="ModelParameter434", type=QVTOperational_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_OperationalTransformation433", type=ModelParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target443: BinaryAssociation = BinaryAssociation(
    name="target443",
    ends={
        Property(name="Variable445", type=QVTOperational_ResolveExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ResolveExp444", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inMapping446: BinaryAssociation = BinaryAssociation(
    name="inMapping446",
    ends={
        Property(name="MappingOperation447", type=QVTOperational_ResolveInExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ResolveInExp", type=MappingOperation, multiplicity=Multiplicity(0, 1))
    }
)
condition441: BinaryAssociation = BinaryAssociation(
    name="condition441",
    ends={
        Property(name="OclExpression442", type=QVTOperational_ResolveExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ResolveExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ctxOwner448: BinaryAssociation = BinaryAssociation(
    name="ctxOwner448",
    ends={
        Property(name="ImperativeOperation449", type=QVTOperational_VarParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_VarParameter", type=ImperativeOperation, multiplicity=Multiplicity(0, 1))
    }
)
resOwner450: BinaryAssociation = BinaryAssociation(
    name="resOwner450",
    ends={
        Property(name="ImperativeOperation452", type=QVTOperational_VarParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_VarParameter451", type=ImperativeOperation, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_EMOF_Comment_Element = Generalization(general=Element, specific=EMOF_Comment)
gen_EMOF_Class_Type = Generalization(general=Type, specific=EMOF_Class)
gen_EMOF_Enumeration_DataType = Generalization(general=DataType, specific=EMOF_Enumeration)
gen_EMOF_EnumerationLiteral_NamedElement = Generalization(general=NamedElement, specific=EMOF_EnumerationLiteral)
gen_EMOF_DataType_Type = Generalization(general=Type, specific=EMOF_DataType)
gen_EMOF_Element_Object = Generalization(general=Object, specific=EMOF_Element)
gen_EMOF_Extent_Object = Generalization(general=Object, specific=EMOF_Extent)
gen_EMOF_Factory_Element = Generalization(general=Element, specific=EMOF_Factory)
gen_EMOF_Operation_TypedElement = Generalization(general=TypedElement, specific=EMOF_Operation)
gen_EMOF_Operation_MultiplicityElement = Generalization(general=MultiplicityElement, specific=EMOF_Operation)
gen_EMOF_NamedElement_Element = Generalization(general=Element, specific=EMOF_NamedElement)
gen_EMOF_Package_NamedElement = Generalization(general=NamedElement, specific=EMOF_Package)
gen_EMOF_Parameter_TypedElement = Generalization(general=TypedElement, specific=EMOF_Parameter)
gen_EMOF_Parameter_MultiplicityElement = Generalization(general=MultiplicityElement, specific=EMOF_Parameter)
gen_EMOF_PrimitiveType_DataType = Generalization(general=DataType, specific=EMOF_PrimitiveType)
gen_EMOF_ReflectiveCollection_Object = Generalization(general=Object, specific=EMOF_ReflectiveCollection)
gen_EMOF_Property_TypedElement = Generalization(general=TypedElement, specific=EMOF_Property)
gen_EMOF_Property_MultiplicityElement = Generalization(general=MultiplicityElement, specific=EMOF_Property)
gen_EMOF_Tag_Element = Generalization(general=Element, specific=EMOF_Tag)
gen_EMOF_ReflectiveSequence_ReflectiveCollection = Generalization(general=ReflectiveCollection, specific=EMOF_ReflectiveSequence)
gen_EMOF_TypedElement_NamedElement = Generalization(general=NamedElement, specific=EMOF_TypedElement)
gen_EMOF_URIExtent_Extent = Generalization(general=Extent, specific=EMOF_URIExtent)
gen_EMOF_Type_NamedElement = Generalization(general=NamedElement, specific=EMOF_Type)
gen_EssentialOCL_AnyType_Type = Generalization(general=Type, specific=EssentialOCL_AnyType)
gen_EssentialOCL_BagType_CollectionType = Generalization(general=CollectionType, specific=EssentialOCL_BagType)
gen_EssentialOCL_BooleanLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=EssentialOCL_BooleanLiteralExp)
gen_EssentialOCL_CallExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_CallExp)
gen_EssentialOCL_CollectionItem_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=EssentialOCL_CollectionItem)
gen_EssentialOCL_CollectionLiteralPart_TypedElement = Generalization(general=TypedElement, specific=EssentialOCL_CollectionLiteralPart)
gen_EssentialOCL_CollectionRange_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=EssentialOCL_CollectionRange)
gen_EssentialOCL_CollectionLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=EssentialOCL_CollectionLiteralExp)
gen_EssentialOCL_CollectionType_DataType = Generalization(general=DataType, specific=EssentialOCL_CollectionType)
gen_EssentialOCL_EnumLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=EssentialOCL_EnumLiteralExp)
gen_EssentialOCL_ExpressionInOcl_TypedElement = Generalization(general=TypedElement, specific=EssentialOCL_ExpressionInOcl)
gen_EssentialOCL_FeatureCallExp_CallExp = Generalization(general=CallExp, specific=EssentialOCL_FeatureCallExp)
gen_EssentialOCL_IfExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_IfExp)
gen_EssentialOCL_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=EssentialOCL_IteratorExp)
gen_EssentialOCL_LetExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_LetExp)
gen_EssentialOCL_IntegerLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=EssentialOCL_IntegerLiteralExp)
gen_EssentialOCL_InvalidLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=EssentialOCL_InvalidLiteralExp)
gen_EssentialOCL_InvalidType_Type = Generalization(general=Type, specific=EssentialOCL_InvalidType)
gen_EssentialOCL_IterateExp_LoopExp = Generalization(general=LoopExp, specific=EssentialOCL_IterateExp)
gen_EssentialOCL_NavigationCallExp_FeatureCallExp = Generalization(general=FeatureCallExp, specific=EssentialOCL_NavigationCallExp)
gen_EssentialOCL_NullLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=EssentialOCL_NullLiteralExp)
gen_EssentialOCL_NumericLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=EssentialOCL_NumericLiteralExp)
gen_EssentialOCL_LiteralExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_LiteralExp)
gen_EssentialOCL_LoopExp_CallExp = Generalization(general=CallExp, specific=EssentialOCL_LoopExp)
gen_EssentialOCL_LoopExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_LoopExp)
gen_EssentialOCL_PropertyCallExp_NavigationCallExp = Generalization(general=NavigationCallExp, specific=EssentialOCL_PropertyCallExp)
gen_EssentialOCL_RealLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=EssentialOCL_RealLiteralExp)
gen_EssentialOCL_OclExpression_TypedElement = Generalization(general=TypedElement, specific=EssentialOCL_OclExpression)
gen_EssentialOCL_OperationCallExp_FeatureCallExp = Generalization(general=FeatureCallExp, specific=EssentialOCL_OperationCallExp)
gen_EssentialOCL_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=EssentialOCL_OrderedSetType)
gen_EssentialOCL_PrimitiveLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=EssentialOCL_PrimitiveLiteralExp)
gen_EssentialOCL_TupleLiteralPart_TypedElement = Generalization(general=TypedElement, specific=EssentialOCL_TupleLiteralPart)
gen_EssentialOCL_SequenceType_CollectionType = Generalization(general=CollectionType, specific=EssentialOCL_SequenceType)
gen_EssentialOCL_SetType_CollectionType = Generalization(general=CollectionType, specific=EssentialOCL_SetType)
gen_EssentialOCL_StringLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=EssentialOCL_StringLiteralExp)
gen_EssentialOCL_TemplateParameterType_Type = Generalization(general=Type, specific=EssentialOCL_TemplateParameterType)
gen_EssentialOCL_TupleLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=EssentialOCL_TupleLiteralExp)
gen_EssentialOCL_TupleType_Class = Generalization(general=Class_, specific=EssentialOCL_TupleType)
gen_EssentialOCL_TupleType_DataType = Generalization(general=DataType, specific=EssentialOCL_TupleType)
gen_EssentialOCL_TypeExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_TypeExp)
gen_EssentialOCL_UnlimitedNaturalExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=EssentialOCL_UnlimitedNaturalExp)
gen_EssentialOCL_Variable_TypedElement = Generalization(general=TypedElement, specific=EssentialOCL_Variable)
gen_EssentialOCL_VariableExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_VariableExp)
gen_EssentialOCL_VoidType_Type = Generalization(general=Type, specific=EssentialOCL_VoidType)
gen_ImperativeOCL_AltExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_AltExp)
gen_ImperativeOCL_AssignExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_AssignExp)
gen_ImperativeOCL_AssertExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_AssertExp)
gen_ImperativeOCL_BlockExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_BlockExp)
gen_ImperativeOCL_BreakExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_BreakExp)
gen_ImperativeOCL_CatchExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_CatchExp)
gen_ImperativeOCL_ContinueExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_ContinueExp)
gen_ImperativeOCL_DictLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=ImperativeOCL_DictLiteralExp)
gen_ImperativeOCL_ComputeExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_ComputeExp)
gen_ImperativeOCL_DictionaryType_CollectionType = Generalization(general=CollectionType, specific=ImperativeOCL_DictionaryType)
gen_ImperativeOCL_ForExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=ImperativeOCL_ForExp)
gen_ImperativeOCL_ImperativeExpression_OclExpression = Generalization(general=OclExpression, specific=ImperativeOCL_ImperativeExpression)
gen_ImperativeOCL_DictLiteralPart_Element = Generalization(general=Element, specific=ImperativeOCL_DictLiteralPart)
gen_ImperativeOCL_ImperativeLoopExp_LoopExp = Generalization(general=LoopExp, specific=ImperativeOCL_ImperativeLoopExp)
gen_ImperativeOCL_ImperativeLoopExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_ImperativeLoopExp)
gen_ImperativeOCL_InstantiationExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_InstantiationExp)
gen_ImperativeOCL_ImperativeIterateExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=ImperativeOCL_ImperativeIterateExp)
gen_ImperativeOCL_ListType_CollectionType = Generalization(general=CollectionType, specific=ImperativeOCL_ListType)
gen_ImperativeOCL_LogExp_OperationCallExp = Generalization(general=OperationCallExp, specific=ImperativeOCL_LogExp)
gen_ImperativeOCL_LogExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_LogExp)
gen_ImperativeOCL_OrderedTupleLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=ImperativeOCL_OrderedTupleLiteralExp)
gen_ImperativeOCL_ListLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=ImperativeOCL_ListLiteralExp)
gen_ImperativeOCL_OrderedTupleType_Class = Generalization(general=Class_, specific=ImperativeOCL_OrderedTupleType)
gen_ImperativeOCL_RaiseExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_RaiseExp)
gen_ImperativeOCL_OrderedTupleLiteralPart_Element = Generalization(general=Element, specific=ImperativeOCL_OrderedTupleLiteralPart)
gen_ImperativeOCL_ReturnExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_ReturnExp)
gen_ImperativeOCL_SwitchExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_SwitchExp)
gen_ImperativeOCL_TryExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_TryExp)
gen_ImperativeOCL_Typedef_Class = Generalization(general=Class_, specific=ImperativeOCL_Typedef)
gen_ImperativeOCL_UnlinkExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_UnlinkExp)
gen_ImperativeOCL_UnpackExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_UnpackExp)
gen_ImperativeOCL_VariableInitExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_VariableInitExp)
gen_ImperativeOCL_WhileExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_WhileExp)
gen_QVTBase_Domain_NamedElement = Generalization(general=NamedElement, specific=QVTBase_Domain)
gen_QVTBase_Function_Operation = Generalization(general=Operation, specific=QVTBase_Function)
gen_QVTBase_Pattern_Element = Generalization(general=Element, specific=QVTBase_Pattern)
gen_QVTBase_Predicate_Element = Generalization(general=Element, specific=QVTBase_Predicate)
gen_QVTBase_FunctionParameter_Variable = Generalization(general=Variable, specific=QVTBase_FunctionParameter)
gen_QVTBase_FunctionParameter_Parameter = Generalization(general=Parameter_, specific=QVTBase_FunctionParameter)
gen_QVTBase_Transformation_Class = Generalization(general=Class_, specific=QVTBase_Transformation)
gen_QVTBase_Transformation_Package = Generalization(general=Package, specific=QVTBase_Transformation)
gen_QVTBase_Rule_NamedElement = Generalization(general=NamedElement, specific=QVTBase_Rule)
gen_QVTBase_TypedModel_NamedElement = Generalization(general=NamedElement, specific=QVTBase_TypedModel)
gen_QVTCore_Assignment_Element = Generalization(general=Element, specific=QVTCore_Assignment)
gen_QVTCore_CoreDomain_Domain = Generalization(general=Domain, specific=QVTCore_CoreDomain)
gen_QVTCore_CoreDomain_Area = Generalization(general=Area, specific=QVTCore_CoreDomain)
gen_QVTCore_CorePattern_Pattern = Generalization(general=Pattern, specific=QVTCore_CorePattern)
gen_QVTCore_BottomPattern_CorePattern = Generalization(general=CorePattern, specific=QVTCore_BottomPattern)
gen_QVTCore_EnforcementOperation_Element = Generalization(general=Element, specific=QVTCore_EnforcementOperation)
gen_QVTCore_GuardPattern_CorePattern = Generalization(general=CorePattern, specific=QVTCore_GuardPattern)
gen_QVTCore_Mapping_Rule = Generalization(general=Rule, specific=QVTCore_Mapping)
gen_QVTCore_Mapping_Area = Generalization(general=Area, specific=QVTCore_Mapping)
gen_QVTCore_PropertyAssignment_Assignment = Generalization(general=Assignment, specific=QVTCore_PropertyAssignment)
gen_QVTCore_VariableAssignment_Assignment = Generalization(general=Assignment, specific=QVTCore_VariableAssignment)
gen_QVTCore_RealizedVariable_Variable = Generalization(general=Variable, specific=QVTCore_RealizedVariable)
gen_QVTTemplate_CollectionTemplateExp_TemplateExp = Generalization(general=TemplateExp, specific=QVTTemplate_CollectionTemplateExp)
gen_QVTTemplate_ObjectTemplateExp_TemplateExp = Generalization(general=TemplateExp, specific=QVTTemplate_ObjectTemplateExp)
gen_QVTTemplate_PropertyTemplateItem_Element = Generalization(general=Element, specific=QVTTemplate_PropertyTemplateItem)
gen_QVTTemplate_TemplateExp_LiteralExp = Generalization(general=LiteralExp, specific=QVTTemplate_TemplateExp)
gen_QVTRelation_DomainPattern_Pattern = Generalization(general=Pattern, specific=QVTRelation_DomainPattern)
gen_QVTRelation_OppositePropertyCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=QVTRelation_OppositePropertyCallExp)
gen_QVTRelation_Relation_Rule = Generalization(general=Rule, specific=QVTRelation_Relation)
gen_QVTRelation_Key_Element = Generalization(general=Element, specific=QVTRelation_Key)
gen_QVTRelation_RelationCallExp_OclExpression = Generalization(general=OclExpression, specific=QVTRelation_RelationCallExp)
gen_QVTRelation_RelationDomain_Domain = Generalization(general=Domain, specific=QVTRelation_RelationDomain)
gen_QVTRelation_RelationDomainAssignment_Element = Generalization(general=Element, specific=QVTRelation_RelationDomainAssignment)
gen_QVTRelation_RelationImplementation_Element = Generalization(general=Element, specific=QVTRelation_RelationImplementation)
gen_QVTRelation_RelationalTransformation_Transformation = Generalization(general=Transformation, specific=QVTRelation_RelationalTransformation)
gen_QVTOperational_Constructor_ImperativeOperation = Generalization(general=ImperativeOperation, specific=QVTOperational_Constructor)
gen_QVTOperational_ConstructorBody_OperationBody = Generalization(general=OperationBody, specific=QVTOperational_ConstructorBody)
gen_QVTOperational_ContextualProperty_Property = Generalization(general=Property_, specific=QVTOperational_ContextualProperty)
gen_QVTOperational_Helper_ImperativeOperation = Generalization(general=ImperativeOperation, specific=QVTOperational_Helper)
gen_QVTOperational_ImperativeCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=QVTOperational_ImperativeCallExp)
gen_QVTOperational_ImperativeCallExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=QVTOperational_ImperativeCallExp)
gen_QVTOperational_ImperativeOperation_Operation = Generalization(general=Operation, specific=QVTOperational_ImperativeOperation)
gen_QVTOperational_Library_Module = Generalization(general=Module, specific=QVTOperational_Library)
gen_QVTOperational_EntryOperation_ImperativeOperation = Generalization(general=ImperativeOperation, specific=QVTOperational_EntryOperation)
gen_QVTOperational_MappingCallExp_ImperativeCallExp = Generalization(general=ImperativeCallExp, specific=QVTOperational_MappingCallExp)
gen_QVTOperational_MappingOperation_ImperativeOperation = Generalization(general=ImperativeOperation, specific=QVTOperational_MappingOperation)
gen_QVTOperational_MappingBody_OperationBody = Generalization(general=OperationBody, specific=QVTOperational_MappingBody)
gen_QVTOperational_MappingParameter_VarParameter = Generalization(general=VarParameter, specific=QVTOperational_MappingParameter)
gen_QVTOperational_ModelParameter_VarParameter = Generalization(general=VarParameter, specific=QVTOperational_ModelParameter)
gen_QVTOperational_ModelType_Class = Generalization(general=Class_, specific=QVTOperational_ModelType)
gen_QVTOperational_Module_Class = Generalization(general=Class_, specific=QVTOperational_Module)
gen_QVTOperational_Module_Package = Generalization(general=Package, specific=QVTOperational_Module)
gen_QVTOperational_ModuleImport_Element = Generalization(general=Element, specific=QVTOperational_ModuleImport)
gen_QVTOperational_ObjectExp_InstantiationExp = Generalization(general=InstantiationExp, specific=QVTOperational_ObjectExp)
gen_QVTOperational_OperationBody_Element = Generalization(general=Element, specific=QVTOperational_OperationBody)
gen_QVTOperational_OperationalTransformation_Module = Generalization(general=Module, specific=QVTOperational_OperationalTransformation)
gen_QVTOperational_ResolveExp_CallExp = Generalization(general=CallExp, specific=QVTOperational_ResolveExp)
gen_QVTOperational_ResolveInExp_ResolveExp = Generalization(general=ResolveExp, specific=QVTOperational_ResolveInExp)
gen_QVTOperational_ResolveExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=QVTOperational_ResolveExp)
gen_QVTOperational_VarParameter_Variable = Generalization(general=Variable, specific=QVTOperational_VarParameter)
gen_QVTOperational_VarParameter_Parameter = Generalization(general=Parameter_, specific=QVTOperational_VarParameter)

# Domain Model
domain_model = DomainModel(
    name="QVTOperational",
    types={Operation, Class_, EMOF_Comment, Element, NamedElement, EMOF_Class, Type, Property_, Comment, EMOF_Enumeration, DataType, EnumerationLiteral, EMOF_EnumerationLiteral, EMOF_DataType, EMOF_Element, Object, Package, Enumeration_, EMOF_Extent, EMOF_Factory, EMOF_Object, EMOF_Operation, TypedElement, MultiplicityElement, Parameter_, EMOF_MultiplicityElement, EMOF_NamedElement, EMOF_Package, EMOF_Parameter, EMOF_PrimitiveType, EMOF_ReflectiveCollection, EMOF_Property, EMOF_Tag, EMOF_ReflectiveSequence, ReflectiveCollection, EMOF_TypedElement, EMOF_URIExtent, Extent, EMOF_Type, EssentialOCL_AnyType, EssentialOCL_BagType, CollectionType, EssentialOCL_BooleanLiteralExp, PrimitiveLiteralExp, EssentialOCL_CallExp, OclExpression, CollectionLiteralPart, EssentialOCL_CollectionItem, EssentialOCL_CollectionLiteralPart, CollectionLiteralExp, EssentialOCL_CollectionRange, EssentialOCL_CollectionLiteralExp, LiteralExp, EssentialOCL_CollectionType, EssentialOCL_EnumLiteralExp, EssentialOCL_ExpressionInOcl, Variable, EssentialOCL_FeatureCallExp, CallExp, EssentialOCL_IfExp, EssentialOCL_LetExp, EssentialOCL_IntegerLiteralExp, NumericLiteralExp, EssentialOCL_InvalidLiteralExp, EssentialOCL_InvalidType, EssentialOCL_IterateExp, LoopExp, EssentialOCL_IteratorExp, EssentialOCL_NavigationCallExp, FeatureCallExp, EssentialOCL_NullLiteralExp, EssentialOCL_NumericLiteralExp, EssentialOCL_LiteralExp, EssentialOCL_LoopExp, EssentialOCL_PropertyCallExp, NavigationCallExp, EssentialOCL_RealLiteralExp, EssentialOCL_OclExpression, EssentialOCL_OperationCallExp, EssentialOCL_OrderedSetType, EssentialOCL_PrimitiveLiteralExp, EssentialOCL_TupleLiteralPart, TupleLiteralExp, EssentialOCL_SequenceType, EssentialOCL_SetType, EssentialOCL_StringLiteralExp, EssentialOCL_TemplateParameterType, EssentialOCL_TupleLiteralExp, TupleLiteralPart, LetExp, EssentialOCL_TupleType, EssentialOCL_TypeExp, EssentialOCL_UnlimitedNaturalExp, EssentialOCL_Variable, EssentialOCL_VariableExp, EssentialOCL_VoidType, ImperativeOCL_AltExp, ImperativeExpression, LogExp, ImperativeOCL_AssignExp, ImperativeOCL_AssertExp, ImperativeOCL_BlockExp, ImperativeOCL_BreakExp, ImperativeOCL_CatchExp, ImperativeOCL_ContinueExp, ImperativeOCL_DictLiteralExp, DictLiteralPart, ImperativeOCL_ComputeExp, ImperativeOCL_DictionaryType, ImperativeOCL_ForExp, ImperativeLoopExp, ImperativeOCL_ImperativeExpression, ImperativeOCL_DictLiteralPart, ImperativeOCL_ImperativeLoopExp, ImperativeOCL_InstantiationExp, ImperativeOCL_ImperativeIterateExp, ImperativeOCL_ListType, ImperativeOCL_LogExp, OperationCallExp, ImperativeOCL_OrderedTupleLiteralExp, OrderedTupleLiteralPart, ImperativeOCL_ListLiteralExp, ImperativeOCL_OrderedTupleType, ImperativeOCL_RaiseExp, ImperativeOCL_OrderedTupleLiteralPart, ImperativeOCL_ReturnExp, ImperativeOCL_SwitchExp, AltExp, ImperativeOCL_TryExp, CatchExp, ImperativeOCL_Typedef, ImperativeOCL_UnlinkExp, ImperativeOCL_UnpackExp, ImperativeOCL_VariableInitExp, ImperativeOCL_WhileExp, QVTBase_Domain, Rule, TypedModel, QVTBase_Function, QVTBase_Pattern, Predicate, QVTBase_Predicate, Pattern, QVTBase_FunctionParameter, Transformation, QVTBase_Transformation, Tag, QVTBase_Rule, Domain, QVTBase_TypedModel, QVTCore_Area, BottomPattern, GuardPattern, QVTCore_Assignment, Assignment, EnforcementOperation, RealizedVariable, QVTCore_CoreDomain, QVTCore_CorePattern, QVTCore_BottomPattern, CorePattern, Area, QVTCore_EnforcementOperation, QVTCore_GuardPattern, QVTCore_Mapping, QVTCore_PropertyAssignment, Mapping, QVTCore_VariableAssignment, QVTCore_RealizedVariable, QVTTemplate_CollectionTemplateExp, TemplateExp, PropertyTemplateItem, QVTTemplate_ObjectTemplateExp, QVTTemplate_PropertyTemplateItem, ObjectTemplateExp, QVTTemplate_TemplateExp, QVTRelation_DomainPattern, RelationalTransformation, QVTRelation_OppositePropertyCallExp, PropertyCallExp, QVTRelation_Relation, QVTRelation_Key, QVTRelation_RelationCallExp, RelationImplementation, QVTRelation_RelationDomain, RelationDomainAssignment, DomainPattern, QVTRelation_RelationDomainAssignment, Relation, QVTRelation_RelationImplementation, QVTRelation_RelationalTransformation, Key, QVTOperational_Constructor, ImperativeOperation, QVTOperational_ConstructorBody, OperationBody, QVTOperational_ContextualProperty, QVTOperational_Helper, QVTOperational_ImperativeCallExp, QVTOperational_ImperativeOperation, VarParameter, QVTOperational_Library, Module, QVTOperational_EntryOperation, QVTOperational_MappingCallExp, ImperativeCallExp, QVTOperational_MappingOperation, MappingOperation, QVTOperational_MappingBody, ModelParameter, RelationDomain, QVTOperational_ModelParameter, QVTOperational_ModelType, QVTOperational_MappingParameter, QVTOperational_Module, EntryOperation, ModuleImport, ModelType, QVTOperational_ModuleImport, QVTOperational_ObjectExp, InstantiationExp, ConstructorBody, QVTOperational_OperationBody, QVTOperational_OperationalTransformation, QVTOperational_ResolveExp, QVTOperational_ResolveInExp, ResolveExp, QVTOperational_VarParameter, CollectionKind, SeverityKind, EnforcementMode, ImportKind, DirectionKind},
    associations={ownedAttribute0, ownedOperation1, superClass3, ownedComment6, ownedLiteral7, annotatedElement5, package9, enumeration8, class10, nestedPackage16, nestingPackage18, ownedType21, operation24, ownedParameter12, raisedException14, opposite28, class26, element31, type34, package32, item37, source36, part39, collectionLiteralExp40, first41, last43, referredEnumLiteral48, bodyExpression50, contextVariable52, generatedType54, elementType46, elseExpression65, thenExpression68, parameterVariable57, resultVariable60, condition63, in73, result71, iterator80, variable75, body78, referredProperty88, argument83, referredOperation85, attribute91, tupleLiteralExp93, value95, part90, initExpression100, letExp102, representedParameter104, referredType98, body109, condition111, referredVariable107, log116, defaultValue118, left120, assertion114, body126, body128, exception130, value123, body133, returnedElement135, part138, value141, keyType144, key139, condition148, argument150, extent152, target146, element158, condition160, part162, instantiatedClass155, elementType165, argument167, value163, value172, exception169, exceptClause178, tryBody179, alternativePart174, elsePart175, condition184, item187, target189, base182, targetVariable194, referredVariable197, body199, source192, rule204, typedModel205, queryExpression207, condition201, bindsTo209, predicate211, conditionExpression213, pattern215, overrides218, transformation221, extends223, modelParameter225, ownedTag228, domain217, dependsOn233, transformation235, usedPackage238, bottomPattern241, rule230, guardPattern242, bottomPattern244, value246, assignment250, enforcementOperation252, realizedVariable254, area249, bottomPattern258, operationCallExp260, area262, variable256, local265, refinement268, specification271, slotExpression274, context264, targetVariable279, targetProperty276, member281, referredCollectionType283, rest285, part288, referredClass289, objContainer292, referredProperty293, value296, bindsTo299, where301, identifies305, oppositePart307, part310, transformation313, templateExpression304, variable316, when319, where322, argument325, operationalImpl315, defaultAssignment329, pattern330, rootVariable332, referredRelation327, variable337, impl340, inDirectionOf342, relation345, valueExp335, context349, initExpression351, ownedKey348, body357, context358, overridden360, result362, overridden354, initSection367, disjunct370, inherited371, endSection365, refinedRelation377, when380, where383, merged374, extent386, referredDomain387, additionalCondition389, metamodel391, configProperty394, entry396, ownedVariable403, usedModelType406, binding408, importedModule410, moduleImport398, ownedTag400, module412, body415, referredObject416, content419, variable424, intermediateClass427, intermediateProperty429, operation421, refined435, relation438, modelParameter432, target443, inMapping446, condition441, ctxOwner448, resOwner450},
    generalizations={gen_EMOF_Comment_Element, gen_EMOF_Class_Type, gen_EMOF_Enumeration_DataType, gen_EMOF_EnumerationLiteral_NamedElement, gen_EMOF_DataType_Type, gen_EMOF_Element_Object, gen_EMOF_Extent_Object, gen_EMOF_Factory_Element, gen_EMOF_Operation_TypedElement, gen_EMOF_Operation_MultiplicityElement, gen_EMOF_NamedElement_Element, gen_EMOF_Package_NamedElement, gen_EMOF_Parameter_TypedElement, gen_EMOF_Parameter_MultiplicityElement, gen_EMOF_PrimitiveType_DataType, gen_EMOF_ReflectiveCollection_Object, gen_EMOF_Property_TypedElement, gen_EMOF_Property_MultiplicityElement, gen_EMOF_Tag_Element, gen_EMOF_ReflectiveSequence_ReflectiveCollection, gen_EMOF_TypedElement_NamedElement, gen_EMOF_URIExtent_Extent, gen_EMOF_Type_NamedElement, gen_EssentialOCL_AnyType_Type, gen_EssentialOCL_BagType_CollectionType, gen_EssentialOCL_BooleanLiteralExp_PrimitiveLiteralExp, gen_EssentialOCL_CallExp_OclExpression, gen_EssentialOCL_CollectionItem_CollectionLiteralPart, gen_EssentialOCL_CollectionLiteralPart_TypedElement, gen_EssentialOCL_CollectionRange_CollectionLiteralPart, gen_EssentialOCL_CollectionLiteralExp_LiteralExp, gen_EssentialOCL_CollectionType_DataType, gen_EssentialOCL_EnumLiteralExp_LiteralExp, gen_EssentialOCL_ExpressionInOcl_TypedElement, gen_EssentialOCL_FeatureCallExp_CallExp, gen_EssentialOCL_IfExp_OclExpression, gen_EssentialOCL_IteratorExp_LoopExp, gen_EssentialOCL_LetExp_OclExpression, gen_EssentialOCL_IntegerLiteralExp_NumericLiteralExp, gen_EssentialOCL_InvalidLiteralExp_LiteralExp, gen_EssentialOCL_InvalidType_Type, gen_EssentialOCL_IterateExp_LoopExp, gen_EssentialOCL_NavigationCallExp_FeatureCallExp, gen_EssentialOCL_NullLiteralExp_LiteralExp, gen_EssentialOCL_NumericLiteralExp_PrimitiveLiteralExp, gen_EssentialOCL_LiteralExp_OclExpression, gen_EssentialOCL_LoopExp_CallExp, gen_EssentialOCL_LoopExp_OclExpression, gen_EssentialOCL_PropertyCallExp_NavigationCallExp, gen_EssentialOCL_RealLiteralExp_NumericLiteralExp, gen_EssentialOCL_OclExpression_TypedElement, gen_EssentialOCL_OperationCallExp_FeatureCallExp, gen_EssentialOCL_OrderedSetType_CollectionType, gen_EssentialOCL_PrimitiveLiteralExp_LiteralExp, gen_EssentialOCL_TupleLiteralPart_TypedElement, gen_EssentialOCL_SequenceType_CollectionType, gen_EssentialOCL_SetType_CollectionType, gen_EssentialOCL_StringLiteralExp_PrimitiveLiteralExp, gen_EssentialOCL_TemplateParameterType_Type, gen_EssentialOCL_TupleLiteralExp_LiteralExp, gen_EssentialOCL_TupleType_Class, gen_EssentialOCL_TupleType_DataType, gen_EssentialOCL_TypeExp_OclExpression, gen_EssentialOCL_UnlimitedNaturalExp_NumericLiteralExp, gen_EssentialOCL_Variable_TypedElement, gen_EssentialOCL_VariableExp_OclExpression, gen_EssentialOCL_VoidType_Type, gen_ImperativeOCL_AltExp_ImperativeExpression, gen_ImperativeOCL_AssignExp_ImperativeExpression, gen_ImperativeOCL_AssertExp_ImperativeExpression, gen_ImperativeOCL_BlockExp_ImperativeExpression, gen_ImperativeOCL_BreakExp_ImperativeExpression, gen_ImperativeOCL_CatchExp_ImperativeExpression, gen_ImperativeOCL_ContinueExp_ImperativeExpression, gen_ImperativeOCL_DictLiteralExp_LiteralExp, gen_ImperativeOCL_ComputeExp_ImperativeExpression, gen_ImperativeOCL_DictionaryType_CollectionType, gen_ImperativeOCL_ForExp_ImperativeLoopExp, gen_ImperativeOCL_ImperativeExpression_OclExpression, gen_ImperativeOCL_DictLiteralPart_Element, gen_ImperativeOCL_ImperativeLoopExp_LoopExp, gen_ImperativeOCL_ImperativeLoopExp_ImperativeExpression, gen_ImperativeOCL_InstantiationExp_ImperativeExpression, gen_ImperativeOCL_ImperativeIterateExp_ImperativeLoopExp, gen_ImperativeOCL_ListType_CollectionType, gen_ImperativeOCL_LogExp_OperationCallExp, gen_ImperativeOCL_LogExp_ImperativeExpression, gen_ImperativeOCL_OrderedTupleLiteralExp_LiteralExp, gen_ImperativeOCL_ListLiteralExp_LiteralExp, gen_ImperativeOCL_OrderedTupleType_Class, gen_ImperativeOCL_RaiseExp_ImperativeExpression, gen_ImperativeOCL_OrderedTupleLiteralPart_Element, gen_ImperativeOCL_ReturnExp_ImperativeExpression, gen_ImperativeOCL_SwitchExp_ImperativeExpression, gen_ImperativeOCL_TryExp_ImperativeExpression, gen_ImperativeOCL_Typedef_Class, gen_ImperativeOCL_UnlinkExp_ImperativeExpression, gen_ImperativeOCL_UnpackExp_ImperativeExpression, gen_ImperativeOCL_VariableInitExp_ImperativeExpression, gen_ImperativeOCL_WhileExp_ImperativeExpression, gen_QVTBase_Domain_NamedElement, gen_QVTBase_Function_Operation, gen_QVTBase_Pattern_Element, gen_QVTBase_Predicate_Element, gen_QVTBase_FunctionParameter_Variable, gen_QVTBase_FunctionParameter_Parameter, gen_QVTBase_Transformation_Class, gen_QVTBase_Transformation_Package, gen_QVTBase_Rule_NamedElement, gen_QVTBase_TypedModel_NamedElement, gen_QVTCore_Assignment_Element, gen_QVTCore_CoreDomain_Domain, gen_QVTCore_CoreDomain_Area, gen_QVTCore_CorePattern_Pattern, gen_QVTCore_BottomPattern_CorePattern, gen_QVTCore_EnforcementOperation_Element, gen_QVTCore_GuardPattern_CorePattern, gen_QVTCore_Mapping_Rule, gen_QVTCore_Mapping_Area, gen_QVTCore_PropertyAssignment_Assignment, gen_QVTCore_VariableAssignment_Assignment, gen_QVTCore_RealizedVariable_Variable, gen_QVTTemplate_CollectionTemplateExp_TemplateExp, gen_QVTTemplate_ObjectTemplateExp_TemplateExp, gen_QVTTemplate_PropertyTemplateItem_Element, gen_QVTTemplate_TemplateExp_LiteralExp, gen_QVTRelation_DomainPattern_Pattern, gen_QVTRelation_OppositePropertyCallExp_PropertyCallExp, gen_QVTRelation_Relation_Rule, gen_QVTRelation_Key_Element, gen_QVTRelation_RelationCallExp_OclExpression, gen_QVTRelation_RelationDomain_Domain, gen_QVTRelation_RelationDomainAssignment_Element, gen_QVTRelation_RelationImplementation_Element, gen_QVTRelation_RelationalTransformation_Transformation, gen_QVTOperational_Constructor_ImperativeOperation, gen_QVTOperational_ConstructorBody_OperationBody, gen_QVTOperational_ContextualProperty_Property, gen_QVTOperational_Helper_ImperativeOperation, gen_QVTOperational_ImperativeCallExp_OperationCallExp, gen_QVTOperational_ImperativeCallExp_ImperativeExpression, gen_QVTOperational_ImperativeOperation_Operation, gen_QVTOperational_Library_Module, gen_QVTOperational_EntryOperation_ImperativeOperation, gen_QVTOperational_MappingCallExp_ImperativeCallExp, gen_QVTOperational_MappingOperation_ImperativeOperation, gen_QVTOperational_MappingBody_OperationBody, gen_QVTOperational_MappingParameter_VarParameter, gen_QVTOperational_ModelParameter_VarParameter, gen_QVTOperational_ModelType_Class, gen_QVTOperational_Module_Class, gen_QVTOperational_Module_Package, gen_QVTOperational_ModuleImport_Element, gen_QVTOperational_ObjectExp_InstantiationExp, gen_QVTOperational_OperationBody_Element, gen_QVTOperational_OperationalTransformation_Module, gen_QVTOperational_ResolveExp_CallExp, gen_QVTOperational_ResolveInExp_ResolveExp, gen_QVTOperational_ResolveExp_ImperativeExpression, gen_QVTOperational_VarParameter_Variable, gen_QVTOperational_VarParameter_Parameter},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)