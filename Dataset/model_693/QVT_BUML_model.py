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
EMOF_Comment = Class(name="EMOF::Comment")
Element = Class(name="Element")
EMOF_DataType = Class(name="EMOF::DataType")
EMOF_Element = Class(name="EMOF::Element", is_abstract=True)
Object = Class(name="Object")
EMOF_Class = Class(name="EMOF::Class")
Type = Class(name="Type")
EMOF_Enumeration = Class(name="EMOF::Enumeration")
DataType = Class(name="DataType")
EMOF_EnumerationLiteral = Class(name="EMOF::EnumerationLiteral")
NamedElement = Class(name="NamedElement")
EMOF_Extent = Class(name="EMOF::Extent")
EMOF_Factory = Class(name="EMOF::Factory")
EMOF_MultiplicityElement = Class(name="EMOF::MultiplicityElement", is_abstract=True)
EMOF_Object = Class(name="EMOF::Object")
EMOF_Operation = Class(name="EMOF::Operation")
TypedElement = Class(name="TypedElement")
MultiplicityElement = Class(name="MultiplicityElement")
EMOF_Package = Class(name="EMOF::Package")
EMOF_Parameter = Class(name="EMOF::Parameter")
EMOF_PrimitiveType = Class(name="EMOF::PrimitiveType")
EMOF_Property = Class(name="EMOF::Property")
EMOF_NamedElement = Class(name="EMOF::NamedElement", is_abstract=True)
EMOF_ReflectiveCollection = Class(name="EMOF::ReflectiveCollection")
EMOF_ReflectiveSequence = Class(name="EMOF::ReflectiveSequence")
ReflectiveCollection = Class(name="ReflectiveCollection")
EMOF_Tag = Class(name="EMOF::Tag")
EMOF_Type = Class(name="EMOF::Type", is_abstract=True)
EMOF_TypedElement = Class(name="EMOF::TypedElement", is_abstract=True)
EMOF_URIExtent = Class(name="EMOF::URIExtent")
Extent = Class(name="Extent")
EssentialOCL_AnyType = Class(name="EssentialOCL::AnyType")
EssentialOCL_BagType = Class(name="EssentialOCL::BagType")
CollectionType = Class(name="CollectionType")
EssentialOCL_BooleanLiteralExp = Class(name="EssentialOCL::BooleanLiteralExp")
PrimitiveLiteralExp = Class(name="PrimitiveLiteralExp")
EssentialOCL_CallExp = Class(name="EssentialOCL::CallExp", is_abstract=True)
OclExpression = Class(name="OclExpression")
EssentialOCL_CollectionLiteralExp = Class(name="EssentialOCL::CollectionLiteralExp")
LiteralExp = Class(name="LiteralExp")
EssentialOCL_CollectionLiteralPart = Class(name="EssentialOCL::CollectionLiteralPart", is_abstract=True)
EssentialOCL_CollectionRange = Class(name="EssentialOCL::CollectionRange")
EssentialOCL_CollectionType = Class(name="EssentialOCL::CollectionType")
EssentialOCL_EnumLiteralExp = Class(name="EssentialOCL::EnumLiteralExp")
EssentialOCL_CollectionItem = Class(name="EssentialOCL::CollectionItem")
CollectionLiteralPart = Class(name="CollectionLiteralPart")
EssentialOCL_FeatureCallExp = Class(name="EssentialOCL::FeatureCallExp", is_abstract=True)
CallExp = Class(name="CallExp")
EssentialOCL_IfExp = Class(name="EssentialOCL::IfExp")
EssentialOCL_IntegerLiteralExp = Class(name="EssentialOCL::IntegerLiteralExp")
NumericLiteralExp = Class(name="NumericLiteralExp")
EssentialOCL_InvalidLiteralExp = Class(name="EssentialOCL::InvalidLiteralExp")
EssentialOCL_ExpressionInOcl = Class(name="EssentialOCL::ExpressionInOcl")
EssentialOCL_IteratorExp = Class(name="EssentialOCL::IteratorExp")
EssentialOCL_LetExp = Class(name="EssentialOCL::LetExp")
EssentialOCL_LiteralExp = Class(name="EssentialOCL::LiteralExp", is_abstract=True)
EssentialOCL_LoopExp = Class(name="EssentialOCL::LoopExp", is_abstract=True)
EssentialOCL_NavigationCallExp = Class(name="EssentialOCL::NavigationCallExp")
FeatureCallExp = Class(name="FeatureCallExp")
EssentialOCL_NullLiteralExp = Class(name="EssentialOCL::NullLiteralExp")
EssentialOCL_NumericLiteralExp = Class(name="EssentialOCL::NumericLiteralExp", is_abstract=True)
EssentialOCL_OclExpression = Class(name="EssentialOCL::OclExpression", is_abstract=True)
EssentialOCL_OperationCallExp = Class(name="EssentialOCL::OperationCallExp")
EssentialOCL_InvalidType = Class(name="EssentialOCL::InvalidType")
EssentialOCL_IterateExp = Class(name="EssentialOCL::IterateExp")
LoopExp = Class(name="LoopExp")
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
EssentialOCL_TupleLiteralPart = Class(name="EssentialOCL::TupleLiteralPart")
EssentialOCL_TupleType = Class(name="EssentialOCL::TupleType")
Class_ = Class(name="Class")
EssentialOCL_TypeExp = Class(name="EssentialOCL::TypeExp")
EssentialOCL_UnlimitedNaturalExp = Class(name="EssentialOCL::UnlimitedNaturalExp")
EssentialOCL_Variable = Class(name="EssentialOCL::Variable")
EssentialOCL_VariableExp = Class(name="EssentialOCL::VariableExp")
EssentialOCL_VoidType = Class(name="EssentialOCL::VoidType")
QVTBase_Domain = Class(name="QVTBase::Domain", is_abstract=True)
QVTBase_FunctionParameter = Class(name="QVTBase::FunctionParameter")
Variable = Class(name="Variable")
Parameter_ = Class(name="Parameter")
QVTBase_Pattern = Class(name="QVTBase::Pattern")
QVTBase_Predicate = Class(name="QVTBase::Predicate")
QVTBase_Rule = Class(name="QVTBase::Rule", is_abstract=True)
QVTBase_Transformation = Class(name="QVTBase::Transformation")
Package = Class(name="Package")
QVTBase_Function = Class(name="QVTBase::Function")
Operation = Class(name="Operation")
QVTBase_TypedModel = Class(name="QVTBase::TypedModel")
QVTCore_Area = Class(name="QVTCore::Area", is_abstract=True)
QVTCore_Assignment = Class(name="QVTCore::Assignment", is_abstract=True)
QVTCore_BottomPattern = Class(name="QVTCore::BottomPattern")
CorePattern = Class(name="CorePattern")
QVTCore_CoreDomain = Class(name="QVTCore::CoreDomain")
Domain = Class(name="Domain")
Area = Class(name="Area")
QVTCore_CorePattern = Class(name="QVTCore::CorePattern")
Pattern = Class(name="Pattern")
QVTCore_EnforcementOperation = Class(name="QVTCore::EnforcementOperation")
QVTCore_GuardPattern = Class(name="QVTCore::GuardPattern")
QVTCore_Mapping = Class(name="QVTCore::Mapping")
Rule = Class(name="Rule")
QVTCore_PropertyAssignment = Class(name="QVTCore::PropertyAssignment")
Assignment = Class(name="Assignment")
QVTCore_RealizedVariable = Class(name="QVTCore::RealizedVariable")
QVTCore_VariableAssignment = Class(name="QVTCore::VariableAssignment")
QVTTemplate_CollectionTemplateExp = Class(name="QVTTemplate::CollectionTemplateExp")
TemplateExp = Class(name="TemplateExp")
QVTTemplate_PropertyTemplateItem = Class(name="QVTTemplate::PropertyTemplateItem")
QVTTemplate_TemplateExp = Class(name="QVTTemplate::TemplateExp", is_abstract=True)
QVTRelation_DomainPattern = Class(name="QVTRelation::DomainPattern")
QVTRelation_Key = Class(name="QVTRelation::Key")
QVTTemplate_ObjectTemplateExp = Class(name="QVTTemplate::ObjectTemplateExp")
QVTRelation_OppositePropertyCallExp = Class(name="QVTRelation::OppositePropertyCallExp")
PropertyCallExp = Class(name="PropertyCallExp")
QVTRelation_Relation = Class(name="QVTRelation::Relation")
QVTRelation_RelationCallExp = Class(name="QVTRelation::RelationCallExp")
QVTRelation_RelationDomain = Class(name="QVTRelation::RelationDomain")
QVTRelation_RelationDomainAssignment = Class(name="QVTRelation::RelationDomainAssignment")
QVTRelation_RelationImplementation = Class(name="QVTRelation::RelationImplementation")
QVTRelation_RelationalTransformation = Class(name="QVTRelation::RelationalTransformation")
Transformation = Class(name="Transformation")
ImperativeOCL_AltExp = Class(name="ImperativeOCL::AltExp")
ImperativeExpression = Class(name="ImperativeExpression")
ImperativeOCL_AssertExp = Class(name="ImperativeOCL::AssertExp")
ImperativeOCL_ComputeExp = Class(name="ImperativeOCL::ComputeExp")
ImperativeOCL_AssignExp = Class(name="ImperativeOCL::AssignExp")
ImperativeOCL_BlockExp = Class(name="ImperativeOCL::BlockExp")
ImperativeOCL_BreakExp = Class(name="ImperativeOCL::BreakExp")
ImperativeOCL_CatchExp = Class(name="ImperativeOCL::CatchExp")
ImperativeOCL_DictionaryType = Class(name="ImperativeOCL::DictionaryType")
ImperativeOCL_ForExp = Class(name="ImperativeOCL::ForExp")
ImperativeLoopExp = Class(name="ImperativeLoopExp")
ImperativeOCL_ImperativeExpression = Class(name="ImperativeOCL::ImperativeExpression", is_abstract=True)
ImperativeOCL_ImperativeIterateExp = Class(name="ImperativeOCL::ImperativeIterateExp")
ImperativeOCL_ContinueExp = Class(name="ImperativeOCL::ContinueExp")
ImperativeOCL_DictLiteralExp = Class(name="ImperativeOCL::DictLiteralExp")
ImperativeOCL_DictLiteralPart = Class(name="ImperativeOCL::DictLiteralPart")
ImperativeOCL_ListLiteralExp = Class(name="ImperativeOCL::ListLiteralExp")
ImperativeOCL_ListType = Class(name="ImperativeOCL::ListType")
ImperativeOCL_LogExp = Class(name="ImperativeOCL::LogExp")
OperationCallExp = Class(name="OperationCallExp")
ImperativeOCL_ImperativeLoopExp = Class(name="ImperativeOCL::ImperativeLoopExp", is_abstract=True)
ImperativeOCL_InstantiationExp = Class(name="ImperativeOCL::InstantiationExp")
ImperativeOCL_Typedef = Class(name="ImperativeOCL::Typedef")
ImperativeOCL_UnlinkExp = Class(name="ImperativeOCL::UnlinkExp")
ImperativeOCL_RaiseExp = Class(name="ImperativeOCL::RaiseExp")
ImperativeOCL_ReturnExp = Class(name="ImperativeOCL::ReturnExp")
ImperativeOCL_SwitchExp = Class(name="ImperativeOCL::SwitchExp")
ImperativeOCL_TryExp = Class(name="ImperativeOCL::TryExp")
QVTOperational_Constructor = Class(name="QVTOperational::Constructor")
ImperativeOperation = Class(name="ImperativeOperation")
QVTOperational_ConstructorBody = Class(name="QVTOperational::ConstructorBody")
OperationBody = Class(name="OperationBody")
QVTOperational_ContextualProperty = Class(name="QVTOperational::ContextualProperty")
Property_ = Class(name="Property")
ImperativeOCL_VariableInitExp = Class(name="ImperativeOCL::VariableInitExp")
ImperativeOCL_WhileExp = Class(name="ImperativeOCL::WhileExp")
QVTOperational_Library = Class(name="QVTOperational::Library")
Module = Class(name="Module")
QVTOperational_MappingBody = Class(name="QVTOperational::MappingBody")
QVTOperational_EntryOperation = Class(name="QVTOperational::EntryOperation")
QVTOperational_Helper = Class(name="QVTOperational::Helper")
QVTOperational_ImperativeCallExp = Class(name="QVTOperational::ImperativeCallExp")
QVTOperational_ImperativeOperation = Class(name="QVTOperational::ImperativeOperation")
QVTOperational_MappingParameter = Class(name="QVTOperational::MappingParameter")
VarParameter = Class(name="VarParameter")
QVTOperational_MappingCallExp = Class(name="QVTOperational::MappingCallExp")
ImperativeCallExp = Class(name="ImperativeCallExp")
QVTOperational_MappingOperation = Class(name="QVTOperational::MappingOperation")
QVTOperational_ModelParameter = Class(name="QVTOperational::ModelParameter")
QVTOperational_ModelType = Class(name="QVTOperational::ModelType")
QVTOperational_Module = Class(name="QVTOperational::Module")
QVTOperational_OperationBody = Class(name="QVTOperational::OperationBody")
QVTOperational_OperationalTransformation = Class(name="QVTOperational::OperationalTransformation")
QVTOperational_ModuleImport = Class(name="QVTOperational::ModuleImport")
QVTOperational_ObjectExp = Class(name="QVTOperational::ObjectExp")
InstantiationExp = Class(name="InstantiationExp")
QVTOperational_ResolveInExp = Class(name="QVTOperational::ResolveInExp")
ResolveExp = Class(name="ResolveExp")
QVTOperational_VarParameter = Class(name="QVTOperational::VarParameter")
QVTOperational_ResolveExp = Class(name="QVTOperational::ResolveExp")

# EMOF_Comment class attributes and methods

# Element class attributes and methods

# EMOF_DataType class attributes and methods

# EMOF_Element class attributes and methods
EMOF_Element_m_container: Method = Method(name="container", parameters={}, type=StringType)
EMOF_Element_m_equals: Method = Method(name="equals", parameters={Parameter(name='object')}, type=StringType)
EMOF_Element_m_get: Method = Method(name="get", parameters={Parameter(name='property')}, type=StringType)
EMOF_Element_m_getMetaClass: Method = Method(name="getMetaClass", parameters={}, type=StringType)
EMOF_Element_m_isSet: Method = Method(name="isSet", parameters={Parameter(name='property')}, type=StringType)
EMOF_Element_m_set: Method = Method(name="set", parameters={Parameter(name='property'), Parameter(name='object')})
EMOF_Element_m_unset: Method = Method(name="unset", parameters={Parameter(name='property')})
EMOF_Element.methods={EMOF_Element_m_getMetaClass, EMOF_Element_m_set, EMOF_Element_m_isSet, EMOF_Element_m_container, EMOF_Element_m_get, EMOF_Element_m_unset, EMOF_Element_m_equals}

# Object class attributes and methods

# EMOF_Class class attributes and methods

# Type class attributes and methods

# EMOF_Enumeration class attributes and methods

# DataType class attributes and methods

# EMOF_EnumerationLiteral class attributes and methods

# NamedElement class attributes and methods

# EMOF_Extent class attributes and methods
EMOF_Extent_m_elements: Method = Method(name="elements", parameters={}, type=StringType)
EMOF_Extent_m_useContainment: Method = Method(name="useContainment", parameters={}, type=StringType)
EMOF_Extent.methods={EMOF_Extent_m_elements, EMOF_Extent_m_useContainment}

# EMOF_Factory class attributes and methods
EMOF_Factory_m_convertToString: Method = Method(name="convertToString", parameters={Parameter(name='object'), Parameter(name='dataType')}, type=StringType)
EMOF_Factory_m_create: Method = Method(name="create", parameters={Parameter(name='metaClass')}, type=StringType)
EMOF_Factory_m_createFromString: Method = Method(name="createFromString", parameters={Parameter(name='dataType'), Parameter(name='string')}, type=StringType)
EMOF_Factory.methods={EMOF_Factory_m_createFromString, EMOF_Factory_m_create, EMOF_Factory_m_convertToString}

# EMOF_MultiplicityElement class attributes and methods

# EMOF_Object class attributes and methods

# EMOF_Operation class attributes and methods

# TypedElement class attributes and methods

# MultiplicityElement class attributes and methods

# EMOF_Package class attributes and methods

# EMOF_Parameter class attributes and methods

# EMOF_PrimitiveType class attributes and methods

# EMOF_Property class attributes and methods

# EMOF_NamedElement class attributes and methods

# EMOF_ReflectiveCollection class attributes and methods
EMOF_ReflectiveCollection_m_add: Method = Method(name="add", parameters={Parameter(name='object')}, type=StringType)
EMOF_ReflectiveCollection_m_addAll: Method = Method(name="addAll", parameters={Parameter(name='objects')}, type=StringType)
EMOF_ReflectiveCollection_m_clear: Method = Method(name="clear", parameters={})
EMOF_ReflectiveCollection_m_remove: Method = Method(name="remove", parameters={Parameter(name='object')}, type=StringType)
EMOF_ReflectiveCollection_m_size: Method = Method(name="size", parameters={}, type=StringType)
EMOF_ReflectiveCollection.methods={EMOF_ReflectiveCollection_m_add, EMOF_ReflectiveCollection_m_addAll, EMOF_ReflectiveCollection_m_size, EMOF_ReflectiveCollection_m_clear, EMOF_ReflectiveCollection_m_remove}

# EMOF_ReflectiveSequence class attributes and methods
EMOF_ReflectiveSequence_m_add: Method = Method(name="add", parameters={Parameter(name='index'), Parameter(name='object')})
EMOF_ReflectiveSequence_m_get: Method = Method(name="get", parameters={Parameter(name='index')}, type=StringType)
EMOF_ReflectiveSequence_m_remove: Method = Method(name="remove", parameters={Parameter(name='index')}, type=StringType)
EMOF_ReflectiveSequence_m_set: Method = Method(name="set", parameters={Parameter(name='object'), Parameter(name='index')}, type=StringType)
EMOF_ReflectiveSequence.methods={EMOF_ReflectiveSequence_m_remove, EMOF_ReflectiveSequence_m_add, EMOF_ReflectiveSequence_m_get, EMOF_ReflectiveSequence_m_set}

# ReflectiveCollection class attributes and methods

# EMOF_Tag class attributes and methods

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

# EssentialOCL_BooleanLiteralExp class attributes and methods

# PrimitiveLiteralExp class attributes and methods

# EssentialOCL_CallExp class attributes and methods

# OclExpression class attributes and methods

# EssentialOCL_CollectionLiteralExp class attributes and methods

# LiteralExp class attributes and methods

# EssentialOCL_CollectionLiteralPart class attributes and methods

# EssentialOCL_CollectionRange class attributes and methods

# EssentialOCL_CollectionType class attributes and methods

# EssentialOCL_EnumLiteralExp class attributes and methods

# EssentialOCL_CollectionItem class attributes and methods

# CollectionLiteralPart class attributes and methods

# EssentialOCL_FeatureCallExp class attributes and methods

# CallExp class attributes and methods

# EssentialOCL_IfExp class attributes and methods

# EssentialOCL_IntegerLiteralExp class attributes and methods

# NumericLiteralExp class attributes and methods

# EssentialOCL_InvalidLiteralExp class attributes and methods

# EssentialOCL_ExpressionInOcl class attributes and methods

# EssentialOCL_IteratorExp class attributes and methods

# EssentialOCL_LetExp class attributes and methods

# EssentialOCL_LiteralExp class attributes and methods

# EssentialOCL_LoopExp class attributes and methods

# EssentialOCL_NavigationCallExp class attributes and methods

# FeatureCallExp class attributes and methods

# EssentialOCL_NullLiteralExp class attributes and methods

# EssentialOCL_NumericLiteralExp class attributes and methods

# EssentialOCL_OclExpression class attributes and methods

# EssentialOCL_OperationCallExp class attributes and methods

# EssentialOCL_InvalidType class attributes and methods

# EssentialOCL_IterateExp class attributes and methods

# LoopExp class attributes and methods

# EssentialOCL_OrderedSetType class attributes and methods

# EssentialOCL_PrimitiveLiteralExp class attributes and methods

# EssentialOCL_PropertyCallExp class attributes and methods

# NavigationCallExp class attributes and methods

# EssentialOCL_RealLiteralExp class attributes and methods

# EssentialOCL_SequenceType class attributes and methods

# EssentialOCL_SetType class attributes and methods

# EssentialOCL_StringLiteralExp class attributes and methods

# EssentialOCL_TemplateParameterType class attributes and methods

# EssentialOCL_TupleLiteralExp class attributes and methods

# EssentialOCL_TupleLiteralPart class attributes and methods

# EssentialOCL_TupleType class attributes and methods

# Class class attributes and methods

# EssentialOCL_TypeExp class attributes and methods

# EssentialOCL_UnlimitedNaturalExp class attributes and methods

# EssentialOCL_Variable class attributes and methods

# EssentialOCL_VariableExp class attributes and methods

# EssentialOCL_VoidType class attributes and methods

# QVTBase_Domain class attributes and methods

# QVTBase_FunctionParameter class attributes and methods

# Variable class attributes and methods

# Parameter class attributes and methods

# QVTBase_Pattern class attributes and methods

# QVTBase_Predicate class attributes and methods

# QVTBase_Rule class attributes and methods

# QVTBase_Transformation class attributes and methods

# Package class attributes and methods

# QVTBase_Function class attributes and methods

# Operation class attributes and methods

# QVTBase_TypedModel class attributes and methods

# QVTCore_Area class attributes and methods

# QVTCore_Assignment class attributes and methods

# QVTCore_BottomPattern class attributes and methods

# CorePattern class attributes and methods

# QVTCore_CoreDomain class attributes and methods

# Domain class attributes and methods

# Area class attributes and methods

# QVTCore_CorePattern class attributes and methods

# Pattern class attributes and methods

# QVTCore_EnforcementOperation class attributes and methods

# QVTCore_GuardPattern class attributes and methods

# QVTCore_Mapping class attributes and methods

# Rule class attributes and methods

# QVTCore_PropertyAssignment class attributes and methods

# Assignment class attributes and methods

# QVTCore_RealizedVariable class attributes and methods

# QVTCore_VariableAssignment class attributes and methods

# QVTTemplate_CollectionTemplateExp class attributes and methods

# TemplateExp class attributes and methods

# QVTTemplate_PropertyTemplateItem class attributes and methods

# QVTTemplate_TemplateExp class attributes and methods

# QVTRelation_DomainPattern class attributes and methods

# QVTRelation_Key class attributes and methods

# QVTTemplate_ObjectTemplateExp class attributes and methods

# QVTRelation_OppositePropertyCallExp class attributes and methods

# PropertyCallExp class attributes and methods

# QVTRelation_Relation class attributes and methods

# QVTRelation_RelationCallExp class attributes and methods

# QVTRelation_RelationDomain class attributes and methods

# QVTRelation_RelationDomainAssignment class attributes and methods

# QVTRelation_RelationImplementation class attributes and methods

# QVTRelation_RelationalTransformation class attributes and methods

# Transformation class attributes and methods

# ImperativeOCL_AltExp class attributes and methods

# ImperativeExpression class attributes and methods

# ImperativeOCL_AssertExp class attributes and methods

# ImperativeOCL_ComputeExp class attributes and methods

# ImperativeOCL_AssignExp class attributes and methods

# ImperativeOCL_BlockExp class attributes and methods

# ImperativeOCL_BreakExp class attributes and methods

# ImperativeOCL_CatchExp class attributes and methods

# ImperativeOCL_DictionaryType class attributes and methods

# ImperativeOCL_ForExp class attributes and methods

# ImperativeLoopExp class attributes and methods

# ImperativeOCL_ImperativeExpression class attributes and methods

# ImperativeOCL_ImperativeIterateExp class attributes and methods

# ImperativeOCL_ContinueExp class attributes and methods

# ImperativeOCL_DictLiteralExp class attributes and methods

# ImperativeOCL_DictLiteralPart class attributes and methods

# ImperativeOCL_ListLiteralExp class attributes and methods

# ImperativeOCL_ListType class attributes and methods

# ImperativeOCL_LogExp class attributes and methods

# OperationCallExp class attributes and methods

# ImperativeOCL_ImperativeLoopExp class attributes and methods

# ImperativeOCL_InstantiationExp class attributes and methods

# ImperativeOCL_Typedef class attributes and methods

# ImperativeOCL_UnlinkExp class attributes and methods

# ImperativeOCL_RaiseExp class attributes and methods

# ImperativeOCL_ReturnExp class attributes and methods

# ImperativeOCL_SwitchExp class attributes and methods

# ImperativeOCL_TryExp class attributes and methods

# QVTOperational_Constructor class attributes and methods

# ImperativeOperation class attributes and methods

# QVTOperational_ConstructorBody class attributes and methods

# OperationBody class attributes and methods

# QVTOperational_ContextualProperty class attributes and methods

# Property class attributes and methods

# ImperativeOCL_VariableInitExp class attributes and methods

# ImperativeOCL_WhileExp class attributes and methods

# QVTOperational_Library class attributes and methods

# Module class attributes and methods

# QVTOperational_MappingBody class attributes and methods

# QVTOperational_EntryOperation class attributes and methods

# QVTOperational_Helper class attributes and methods

# QVTOperational_ImperativeCallExp class attributes and methods

# QVTOperational_ImperativeOperation class attributes and methods

# QVTOperational_MappingParameter class attributes and methods

# VarParameter class attributes and methods

# QVTOperational_MappingCallExp class attributes and methods

# ImperativeCallExp class attributes and methods

# QVTOperational_MappingOperation class attributes and methods

# QVTOperational_ModelParameter class attributes and methods

# QVTOperational_ModelType class attributes and methods

# QVTOperational_Module class attributes and methods

# QVTOperational_OperationBody class attributes and methods

# QVTOperational_OperationalTransformation class attributes and methods

# QVTOperational_ModuleImport class attributes and methods

# QVTOperational_ObjectExp class attributes and methods

# InstantiationExp class attributes and methods

# QVTOperational_ResolveInExp class attributes and methods

# ResolveExp class attributes and methods

# QVTOperational_VarParameter class attributes and methods

# QVTOperational_ResolveExp class attributes and methods

# Generalizations
gen_EMOF_Comment_Element = Generalization(general=Element, specific=EMOF_Comment)
gen_EMOF_DataType_Type = Generalization(general=Type, specific=EMOF_DataType)
gen_EMOF_Element_Object = Generalization(general=Object, specific=EMOF_Element)
gen_EMOF_Class_Type = Generalization(general=Type, specific=EMOF_Class)
gen_EMOF_Enumeration_DataType = Generalization(general=DataType, specific=EMOF_Enumeration)
gen_EMOF_EnumerationLiteral_NamedElement = Generalization(general=NamedElement, specific=EMOF_EnumerationLiteral)
gen_EMOF_Extent_Object = Generalization(general=Object, specific=EMOF_Extent)
gen_EMOF_Factory_Element = Generalization(general=Element, specific=EMOF_Factory)
gen_EMOF_Operation_TypedElement = Generalization(general=TypedElement, specific=EMOF_Operation)
gen_EMOF_Operation_MultiplicityElement = Generalization(general=MultiplicityElement, specific=EMOF_Operation)
gen_EMOF_Package_NamedElement = Generalization(general=NamedElement, specific=EMOF_Package)
gen_EMOF_Parameter_TypedElement = Generalization(general=TypedElement, specific=EMOF_Parameter)
gen_EMOF_Parameter_MultiplicityElement = Generalization(general=MultiplicityElement, specific=EMOF_Parameter)
gen_EMOF_PrimitiveType_DataType = Generalization(general=DataType, specific=EMOF_PrimitiveType)
gen_EMOF_Property_TypedElement = Generalization(general=TypedElement, specific=EMOF_Property)
gen_EMOF_Property_MultiplicityElement = Generalization(general=MultiplicityElement, specific=EMOF_Property)
gen_EMOF_NamedElement_Element = Generalization(general=Element, specific=EMOF_NamedElement)
gen_EMOF_ReflectiveCollection_Object = Generalization(general=Object, specific=EMOF_ReflectiveCollection)
gen_EMOF_ReflectiveSequence_ReflectiveCollection = Generalization(general=ReflectiveCollection, specific=EMOF_ReflectiveSequence)
gen_EMOF_Tag_Element = Generalization(general=Element, specific=EMOF_Tag)
gen_EMOF_Type_NamedElement = Generalization(general=NamedElement, specific=EMOF_Type)
gen_EMOF_TypedElement_NamedElement = Generalization(general=NamedElement, specific=EMOF_TypedElement)
gen_EMOF_URIExtent_Extent = Generalization(general=Extent, specific=EMOF_URIExtent)
gen_EssentialOCL_AnyType_Type = Generalization(general=Type, specific=EssentialOCL_AnyType)
gen_EssentialOCL_BagType_CollectionType = Generalization(general=CollectionType, specific=EssentialOCL_BagType)
gen_EssentialOCL_BooleanLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=EssentialOCL_BooleanLiteralExp)
gen_EssentialOCL_CallExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_CallExp)
gen_EssentialOCL_CollectionLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=EssentialOCL_CollectionLiteralExp)
gen_EssentialOCL_CollectionLiteralPart_TypedElement = Generalization(general=TypedElement, specific=EssentialOCL_CollectionLiteralPart)
gen_EssentialOCL_CollectionRange_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=EssentialOCL_CollectionRange)
gen_EssentialOCL_CollectionType_DataType = Generalization(general=DataType, specific=EssentialOCL_CollectionType)
gen_EssentialOCL_EnumLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=EssentialOCL_EnumLiteralExp)
gen_EssentialOCL_CollectionItem_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=EssentialOCL_CollectionItem)
gen_EssentialOCL_FeatureCallExp_CallExp = Generalization(general=CallExp, specific=EssentialOCL_FeatureCallExp)
gen_EssentialOCL_IfExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_IfExp)
gen_EssentialOCL_IntegerLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=EssentialOCL_IntegerLiteralExp)
gen_EssentialOCL_ExpressionInOcl_TypedElement = Generalization(general=TypedElement, specific=EssentialOCL_ExpressionInOcl)
gen_EssentialOCL_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=EssentialOCL_IteratorExp)
gen_EssentialOCL_LetExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_LetExp)
gen_EssentialOCL_LiteralExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_LiteralExp)
gen_EssentialOCL_LoopExp_CallExp = Generalization(general=CallExp, specific=EssentialOCL_LoopExp)
gen_EssentialOCL_LoopExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_LoopExp)
gen_EssentialOCL_NavigationCallExp_FeatureCallExp = Generalization(general=FeatureCallExp, specific=EssentialOCL_NavigationCallExp)
gen_EssentialOCL_NullLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=EssentialOCL_NullLiteralExp)
gen_EssentialOCL_NumericLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=EssentialOCL_NumericLiteralExp)
gen_EssentialOCL_OclExpression_TypedElement = Generalization(general=TypedElement, specific=EssentialOCL_OclExpression)
gen_EssentialOCL_OperationCallExp_FeatureCallExp = Generalization(general=FeatureCallExp, specific=EssentialOCL_OperationCallExp)
gen_EssentialOCL_InvalidLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=EssentialOCL_InvalidLiteralExp)
gen_EssentialOCL_InvalidType_Type = Generalization(general=Type, specific=EssentialOCL_InvalidType)
gen_EssentialOCL_IterateExp_LoopExp = Generalization(general=LoopExp, specific=EssentialOCL_IterateExp)
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
gen_EssentialOCL_TupleType_Class = Generalization(general=Class_, specific=EssentialOCL_TupleType)
gen_EssentialOCL_TupleType_DataType = Generalization(general=DataType, specific=EssentialOCL_TupleType)
gen_EssentialOCL_TypeExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_TypeExp)
gen_EssentialOCL_UnlimitedNaturalExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=EssentialOCL_UnlimitedNaturalExp)
gen_EssentialOCL_Variable_TypedElement = Generalization(general=TypedElement, specific=EssentialOCL_Variable)
gen_EssentialOCL_VariableExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_VariableExp)
gen_EssentialOCL_VoidType_Type = Generalization(general=Type, specific=EssentialOCL_VoidType)
gen_QVTBase_Domain_NamedElement = Generalization(general=NamedElement, specific=QVTBase_Domain)
gen_QVTBase_FunctionParameter_Variable = Generalization(general=Variable, specific=QVTBase_FunctionParameter)
gen_QVTBase_FunctionParameter_Parameter = Generalization(general=Parameter_, specific=QVTBase_FunctionParameter)
gen_QVTBase_Pattern_Element = Generalization(general=Element, specific=QVTBase_Pattern)
gen_QVTBase_Predicate_Element = Generalization(general=Element, specific=QVTBase_Predicate)
gen_QVTBase_Rule_NamedElement = Generalization(general=NamedElement, specific=QVTBase_Rule)
gen_QVTBase_Transformation_Class = Generalization(general=Class_, specific=QVTBase_Transformation)
gen_QVTBase_Transformation_Package = Generalization(general=Package, specific=QVTBase_Transformation)
gen_QVTBase_Function_Operation = Generalization(general=Operation, specific=QVTBase_Function)
gen_QVTBase_TypedModel_NamedElement = Generalization(general=NamedElement, specific=QVTBase_TypedModel)
gen_QVTCore_Assignment_Element = Generalization(general=Element, specific=QVTCore_Assignment)
gen_QVTCore_BottomPattern_CorePattern = Generalization(general=CorePattern, specific=QVTCore_BottomPattern)
gen_QVTCore_CoreDomain_Domain = Generalization(general=Domain, specific=QVTCore_CoreDomain)
gen_QVTCore_CoreDomain_Area = Generalization(general=Area, specific=QVTCore_CoreDomain)
gen_QVTCore_CorePattern_Pattern = Generalization(general=Pattern, specific=QVTCore_CorePattern)
gen_QVTCore_EnforcementOperation_Element = Generalization(general=Element, specific=QVTCore_EnforcementOperation)
gen_QVTCore_GuardPattern_CorePattern = Generalization(general=CorePattern, specific=QVTCore_GuardPattern)
gen_QVTCore_Mapping_Rule = Generalization(general=Rule, specific=QVTCore_Mapping)
gen_QVTCore_Mapping_Area = Generalization(general=Area, specific=QVTCore_Mapping)
gen_QVTCore_PropertyAssignment_Assignment = Generalization(general=Assignment, specific=QVTCore_PropertyAssignment)
gen_QVTCore_RealizedVariable_Variable = Generalization(general=Variable, specific=QVTCore_RealizedVariable)
gen_QVTCore_VariableAssignment_Assignment = Generalization(general=Assignment, specific=QVTCore_VariableAssignment)
gen_QVTTemplate_CollectionTemplateExp_TemplateExp = Generalization(general=TemplateExp, specific=QVTTemplate_CollectionTemplateExp)
gen_QVTTemplate_PropertyTemplateItem_Element = Generalization(general=Element, specific=QVTTemplate_PropertyTemplateItem)
gen_QVTTemplate_TemplateExp_LiteralExp = Generalization(general=LiteralExp, specific=QVTTemplate_TemplateExp)
gen_QVTRelation_DomainPattern_Pattern = Generalization(general=Pattern, specific=QVTRelation_DomainPattern)
gen_QVTRelation_Key_Element = Generalization(general=Element, specific=QVTRelation_Key)
gen_QVTTemplate_ObjectTemplateExp_TemplateExp = Generalization(general=TemplateExp, specific=QVTTemplate_ObjectTemplateExp)
gen_QVTRelation_OppositePropertyCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=QVTRelation_OppositePropertyCallExp)
gen_QVTRelation_Relation_Rule = Generalization(general=Rule, specific=QVTRelation_Relation)
gen_QVTRelation_RelationCallExp_OclExpression = Generalization(general=OclExpression, specific=QVTRelation_RelationCallExp)
gen_QVTRelation_RelationDomain_Domain = Generalization(general=Domain, specific=QVTRelation_RelationDomain)
gen_QVTRelation_RelationDomainAssignment_Element = Generalization(general=Element, specific=QVTRelation_RelationDomainAssignment)
gen_QVTRelation_RelationImplementation_Element = Generalization(general=Element, specific=QVTRelation_RelationImplementation)
gen_QVTRelation_RelationalTransformation_Transformation = Generalization(general=Transformation, specific=QVTRelation_RelationalTransformation)
gen_ImperativeOCL_AltExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_AltExp)
gen_ImperativeOCL_AssertExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_AssertExp)
gen_ImperativeOCL_ComputeExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_ComputeExp)
gen_ImperativeOCL_AssignExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_AssignExp)
gen_ImperativeOCL_BlockExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_BlockExp)
gen_ImperativeOCL_BreakExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_BreakExp)
gen_ImperativeOCL_CatchExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_CatchExp)
gen_ImperativeOCL_DictionaryType_CollectionType = Generalization(general=CollectionType, specific=ImperativeOCL_DictionaryType)
gen_ImperativeOCL_ForExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=ImperativeOCL_ForExp)
gen_ImperativeOCL_ImperativeExpression_OclExpression = Generalization(general=OclExpression, specific=ImperativeOCL_ImperativeExpression)
gen_ImperativeOCL_ImperativeIterateExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=ImperativeOCL_ImperativeIterateExp)
gen_ImperativeOCL_ContinueExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_ContinueExp)
gen_ImperativeOCL_DictLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=ImperativeOCL_DictLiteralExp)
gen_ImperativeOCL_DictLiteralPart_Element = Generalization(general=Element, specific=ImperativeOCL_DictLiteralPart)
gen_ImperativeOCL_ListLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=ImperativeOCL_ListLiteralExp)
gen_ImperativeOCL_ListType_CollectionType = Generalization(general=CollectionType, specific=ImperativeOCL_ListType)
gen_ImperativeOCL_LogExp_OperationCallExp = Generalization(general=OperationCallExp, specific=ImperativeOCL_LogExp)
gen_ImperativeOCL_LogExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_LogExp)
gen_ImperativeOCL_ImperativeLoopExp_LoopExp = Generalization(general=LoopExp, specific=ImperativeOCL_ImperativeLoopExp)
gen_ImperativeOCL_ImperativeLoopExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_ImperativeLoopExp)
gen_ImperativeOCL_InstantiationExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_InstantiationExp)
gen_ImperativeOCL_Typedef_Class = Generalization(general=Class_, specific=ImperativeOCL_Typedef)
gen_ImperativeOCL_UnlinkExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_UnlinkExp)
gen_ImperativeOCL_RaiseExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_RaiseExp)
gen_ImperativeOCL_ReturnExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_ReturnExp)
gen_ImperativeOCL_SwitchExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_SwitchExp)
gen_ImperativeOCL_TryExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_TryExp)
gen_QVTOperational_Constructor_ImperativeOperation = Generalization(general=ImperativeOperation, specific=QVTOperational_Constructor)
gen_QVTOperational_ConstructorBody_OperationBody = Generalization(general=OperationBody, specific=QVTOperational_ConstructorBody)
gen_QVTOperational_ContextualProperty_Property = Generalization(general=Property_, specific=QVTOperational_ContextualProperty)
gen_ImperativeOCL_VariableInitExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_VariableInitExp)
gen_ImperativeOCL_WhileExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_WhileExp)
gen_QVTOperational_Library_Module = Generalization(general=Module, specific=QVTOperational_Library)
gen_QVTOperational_EntryOperation_ImperativeOperation = Generalization(general=ImperativeOperation, specific=QVTOperational_EntryOperation)
gen_QVTOperational_Helper_ImperativeOperation = Generalization(general=ImperativeOperation, specific=QVTOperational_Helper)
gen_QVTOperational_ImperativeCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=QVTOperational_ImperativeCallExp)
gen_QVTOperational_ImperativeCallExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=QVTOperational_ImperativeCallExp)
gen_QVTOperational_ImperativeOperation_Operation = Generalization(general=Operation, specific=QVTOperational_ImperativeOperation)
gen_QVTOperational_MappingParameter_VarParameter = Generalization(general=VarParameter, specific=QVTOperational_MappingParameter)
gen_QVTOperational_MappingBody_OperationBody = Generalization(general=OperationBody, specific=QVTOperational_MappingBody)
gen_QVTOperational_MappingCallExp_ImperativeCallExp = Generalization(general=ImperativeCallExp, specific=QVTOperational_MappingCallExp)
gen_QVTOperational_MappingOperation_ImperativeOperation = Generalization(general=ImperativeOperation, specific=QVTOperational_MappingOperation)
gen_QVTOperational_ModelParameter_VarParameter = Generalization(general=VarParameter, specific=QVTOperational_ModelParameter)
gen_QVTOperational_ModelType_Class = Generalization(general=Class_, specific=QVTOperational_ModelType)
gen_QVTOperational_Module_Class = Generalization(general=Class_, specific=QVTOperational_Module)
gen_QVTOperational_Module_Package = Generalization(general=Package, specific=QVTOperational_Module)
gen_QVTOperational_OperationBody_Element = Generalization(general=Element, specific=QVTOperational_OperationBody)
gen_QVTOperational_OperationalTransformation_Module = Generalization(general=Module, specific=QVTOperational_OperationalTransformation)
gen_QVTOperational_ModuleImport_Element = Generalization(general=Element, specific=QVTOperational_ModuleImport)
gen_QVTOperational_ObjectExp_InstantiationExp = Generalization(general=InstantiationExp, specific=QVTOperational_ObjectExp)
gen_QVTOperational_ResolveInExp_ResolveExp = Generalization(general=ResolveExp, specific=QVTOperational_ResolveInExp)
gen_QVTOperational_VarParameter_Variable = Generalization(general=Variable, specific=QVTOperational_VarParameter)
gen_QVTOperational_VarParameter_Parameter = Generalization(general=Parameter_, specific=QVTOperational_VarParameter)
gen_QVTOperational_ResolveExp_CallExp = Generalization(general=CallExp, specific=QVTOperational_ResolveExp)
gen_QVTOperational_ResolveExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=QVTOperational_ResolveExp)

# Domain Model
domain_model = DomainModel(
    name="QVTOperational",
    types={EMOF_Comment, Element, EMOF_DataType, EMOF_Element, Object, EMOF_Class, Type, EMOF_Enumeration, DataType, EMOF_EnumerationLiteral, NamedElement, EMOF_Extent, EMOF_Factory, EMOF_MultiplicityElement, EMOF_Object, EMOF_Operation, TypedElement, MultiplicityElement, EMOF_Package, EMOF_Parameter, EMOF_PrimitiveType, EMOF_Property, EMOF_NamedElement, EMOF_ReflectiveCollection, EMOF_ReflectiveSequence, ReflectiveCollection, EMOF_Tag, EMOF_Type, EMOF_TypedElement, EMOF_URIExtent, Extent, EssentialOCL_AnyType, EssentialOCL_BagType, CollectionType, EssentialOCL_BooleanLiteralExp, PrimitiveLiteralExp, EssentialOCL_CallExp, OclExpression, EssentialOCL_CollectionLiteralExp, LiteralExp, EssentialOCL_CollectionLiteralPart, EssentialOCL_CollectionRange, EssentialOCL_CollectionType, EssentialOCL_EnumLiteralExp, EssentialOCL_CollectionItem, CollectionLiteralPart, EssentialOCL_FeatureCallExp, CallExp, EssentialOCL_IfExp, EssentialOCL_IntegerLiteralExp, NumericLiteralExp, EssentialOCL_InvalidLiteralExp, EssentialOCL_ExpressionInOcl, EssentialOCL_IteratorExp, EssentialOCL_LetExp, EssentialOCL_LiteralExp, EssentialOCL_LoopExp, EssentialOCL_NavigationCallExp, FeatureCallExp, EssentialOCL_NullLiteralExp, EssentialOCL_NumericLiteralExp, EssentialOCL_OclExpression, EssentialOCL_OperationCallExp, EssentialOCL_InvalidType, EssentialOCL_IterateExp, LoopExp, EssentialOCL_OrderedSetType, EssentialOCL_PrimitiveLiteralExp, EssentialOCL_PropertyCallExp, NavigationCallExp, EssentialOCL_RealLiteralExp, EssentialOCL_SequenceType, EssentialOCL_SetType, EssentialOCL_StringLiteralExp, EssentialOCL_TemplateParameterType, EssentialOCL_TupleLiteralExp, EssentialOCL_TupleLiteralPart, EssentialOCL_TupleType, Class_, EssentialOCL_TypeExp, EssentialOCL_UnlimitedNaturalExp, EssentialOCL_Variable, EssentialOCL_VariableExp, EssentialOCL_VoidType, QVTBase_Domain, QVTBase_FunctionParameter, Variable, Parameter_, QVTBase_Pattern, QVTBase_Predicate, QVTBase_Rule, QVTBase_Transformation, Package, QVTBase_Function, Operation, QVTBase_TypedModel, QVTCore_Area, QVTCore_Assignment, QVTCore_BottomPattern, CorePattern, QVTCore_CoreDomain, Domain, Area, QVTCore_CorePattern, Pattern, QVTCore_EnforcementOperation, QVTCore_GuardPattern, QVTCore_Mapping, Rule, QVTCore_PropertyAssignment, Assignment, QVTCore_RealizedVariable, QVTCore_VariableAssignment, QVTTemplate_CollectionTemplateExp, TemplateExp, QVTTemplate_PropertyTemplateItem, QVTTemplate_TemplateExp, QVTRelation_DomainPattern, QVTRelation_Key, QVTTemplate_ObjectTemplateExp, QVTRelation_OppositePropertyCallExp, PropertyCallExp, QVTRelation_Relation, QVTRelation_RelationCallExp, QVTRelation_RelationDomain, QVTRelation_RelationDomainAssignment, QVTRelation_RelationImplementation, QVTRelation_RelationalTransformation, Transformation, ImperativeOCL_AltExp, ImperativeExpression, ImperativeOCL_AssertExp, ImperativeOCL_ComputeExp, ImperativeOCL_AssignExp, ImperativeOCL_BlockExp, ImperativeOCL_BreakExp, ImperativeOCL_CatchExp, ImperativeOCL_DictionaryType, ImperativeOCL_ForExp, ImperativeLoopExp, ImperativeOCL_ImperativeExpression, ImperativeOCL_ImperativeIterateExp, ImperativeOCL_ContinueExp, ImperativeOCL_DictLiteralExp, ImperativeOCL_DictLiteralPart, ImperativeOCL_ListLiteralExp, ImperativeOCL_ListType, ImperativeOCL_LogExp, OperationCallExp, ImperativeOCL_ImperativeLoopExp, ImperativeOCL_InstantiationExp, ImperativeOCL_Typedef, ImperativeOCL_UnlinkExp, ImperativeOCL_RaiseExp, ImperativeOCL_ReturnExp, ImperativeOCL_SwitchExp, ImperativeOCL_TryExp, QVTOperational_Constructor, ImperativeOperation, QVTOperational_ConstructorBody, OperationBody, QVTOperational_ContextualProperty, Property_, ImperativeOCL_VariableInitExp, ImperativeOCL_WhileExp, QVTOperational_Library, Module, QVTOperational_MappingBody, QVTOperational_EntryOperation, QVTOperational_Helper, QVTOperational_ImperativeCallExp, QVTOperational_ImperativeOperation, QVTOperational_MappingParameter, VarParameter, QVTOperational_MappingCallExp, ImperativeCallExp, QVTOperational_MappingOperation, QVTOperational_ModelParameter, QVTOperational_ModelType, QVTOperational_Module, QVTOperational_OperationBody, QVTOperational_OperationalTransformation, QVTOperational_ModuleImport, QVTOperational_ObjectExp, InstantiationExp, QVTOperational_ResolveInExp, ResolveExp, QVTOperational_VarParameter, QVTOperational_ResolveExp, CollectionKind, EnforcementMode, SeverityKind, ImportKind, DirectionKind},
    associations={},
    generalizations={gen_EMOF_Comment_Element, gen_EMOF_DataType_Type, gen_EMOF_Element_Object, gen_EMOF_Class_Type, gen_EMOF_Enumeration_DataType, gen_EMOF_EnumerationLiteral_NamedElement, gen_EMOF_Extent_Object, gen_EMOF_Factory_Element, gen_EMOF_Operation_TypedElement, gen_EMOF_Operation_MultiplicityElement, gen_EMOF_Package_NamedElement, gen_EMOF_Parameter_TypedElement, gen_EMOF_Parameter_MultiplicityElement, gen_EMOF_PrimitiveType_DataType, gen_EMOF_Property_TypedElement, gen_EMOF_Property_MultiplicityElement, gen_EMOF_NamedElement_Element, gen_EMOF_ReflectiveCollection_Object, gen_EMOF_ReflectiveSequence_ReflectiveCollection, gen_EMOF_Tag_Element, gen_EMOF_Type_NamedElement, gen_EMOF_TypedElement_NamedElement, gen_EMOF_URIExtent_Extent, gen_EssentialOCL_AnyType_Type, gen_EssentialOCL_BagType_CollectionType, gen_EssentialOCL_BooleanLiteralExp_PrimitiveLiteralExp, gen_EssentialOCL_CallExp_OclExpression, gen_EssentialOCL_CollectionLiteralExp_LiteralExp, gen_EssentialOCL_CollectionLiteralPart_TypedElement, gen_EssentialOCL_CollectionRange_CollectionLiteralPart, gen_EssentialOCL_CollectionType_DataType, gen_EssentialOCL_EnumLiteralExp_LiteralExp, gen_EssentialOCL_CollectionItem_CollectionLiteralPart, gen_EssentialOCL_FeatureCallExp_CallExp, gen_EssentialOCL_IfExp_OclExpression, gen_EssentialOCL_IntegerLiteralExp_NumericLiteralExp, gen_EssentialOCL_ExpressionInOcl_TypedElement, gen_EssentialOCL_IteratorExp_LoopExp, gen_EssentialOCL_LetExp_OclExpression, gen_EssentialOCL_LiteralExp_OclExpression, gen_EssentialOCL_LoopExp_CallExp, gen_EssentialOCL_LoopExp_OclExpression, gen_EssentialOCL_NavigationCallExp_FeatureCallExp, gen_EssentialOCL_NullLiteralExp_LiteralExp, gen_EssentialOCL_NumericLiteralExp_PrimitiveLiteralExp, gen_EssentialOCL_OclExpression_TypedElement, gen_EssentialOCL_OperationCallExp_FeatureCallExp, gen_EssentialOCL_InvalidLiteralExp_LiteralExp, gen_EssentialOCL_InvalidType_Type, gen_EssentialOCL_IterateExp_LoopExp, gen_EssentialOCL_OrderedSetType_CollectionType, gen_EssentialOCL_PrimitiveLiteralExp_LiteralExp, gen_EssentialOCL_PropertyCallExp_NavigationCallExp, gen_EssentialOCL_RealLiteralExp_NumericLiteralExp, gen_EssentialOCL_SequenceType_CollectionType, gen_EssentialOCL_SetType_CollectionType, gen_EssentialOCL_StringLiteralExp_PrimitiveLiteralExp, gen_EssentialOCL_TemplateParameterType_Type, gen_EssentialOCL_TupleLiteralExp_LiteralExp, gen_EssentialOCL_TupleLiteralPart_TypedElement, gen_EssentialOCL_TupleType_Class, gen_EssentialOCL_TupleType_DataType, gen_EssentialOCL_TypeExp_OclExpression, gen_EssentialOCL_UnlimitedNaturalExp_NumericLiteralExp, gen_EssentialOCL_Variable_TypedElement, gen_EssentialOCL_VariableExp_OclExpression, gen_EssentialOCL_VoidType_Type, gen_QVTBase_Domain_NamedElement, gen_QVTBase_FunctionParameter_Variable, gen_QVTBase_FunctionParameter_Parameter, gen_QVTBase_Pattern_Element, gen_QVTBase_Predicate_Element, gen_QVTBase_Rule_NamedElement, gen_QVTBase_Transformation_Class, gen_QVTBase_Transformation_Package, gen_QVTBase_Function_Operation, gen_QVTBase_TypedModel_NamedElement, gen_QVTCore_Assignment_Element, gen_QVTCore_BottomPattern_CorePattern, gen_QVTCore_CoreDomain_Domain, gen_QVTCore_CoreDomain_Area, gen_QVTCore_CorePattern_Pattern, gen_QVTCore_EnforcementOperation_Element, gen_QVTCore_GuardPattern_CorePattern, gen_QVTCore_Mapping_Rule, gen_QVTCore_Mapping_Area, gen_QVTCore_PropertyAssignment_Assignment, gen_QVTCore_RealizedVariable_Variable, gen_QVTCore_VariableAssignment_Assignment, gen_QVTTemplate_CollectionTemplateExp_TemplateExp, gen_QVTTemplate_PropertyTemplateItem_Element, gen_QVTTemplate_TemplateExp_LiteralExp, gen_QVTRelation_DomainPattern_Pattern, gen_QVTRelation_Key_Element, gen_QVTTemplate_ObjectTemplateExp_TemplateExp, gen_QVTRelation_OppositePropertyCallExp_PropertyCallExp, gen_QVTRelation_Relation_Rule, gen_QVTRelation_RelationCallExp_OclExpression, gen_QVTRelation_RelationDomain_Domain, gen_QVTRelation_RelationDomainAssignment_Element, gen_QVTRelation_RelationImplementation_Element, gen_QVTRelation_RelationalTransformation_Transformation, gen_ImperativeOCL_AltExp_ImperativeExpression, gen_ImperativeOCL_AssertExp_ImperativeExpression, gen_ImperativeOCL_ComputeExp_ImperativeExpression, gen_ImperativeOCL_AssignExp_ImperativeExpression, gen_ImperativeOCL_BlockExp_ImperativeExpression, gen_ImperativeOCL_BreakExp_ImperativeExpression, gen_ImperativeOCL_CatchExp_ImperativeExpression, gen_ImperativeOCL_DictionaryType_CollectionType, gen_ImperativeOCL_ForExp_ImperativeLoopExp, gen_ImperativeOCL_ImperativeExpression_OclExpression, gen_ImperativeOCL_ImperativeIterateExp_ImperativeLoopExp, gen_ImperativeOCL_ContinueExp_ImperativeExpression, gen_ImperativeOCL_DictLiteralExp_LiteralExp, gen_ImperativeOCL_DictLiteralPart_Element, gen_ImperativeOCL_ListLiteralExp_LiteralExp, gen_ImperativeOCL_ListType_CollectionType, gen_ImperativeOCL_LogExp_OperationCallExp, gen_ImperativeOCL_LogExp_ImperativeExpression, gen_ImperativeOCL_ImperativeLoopExp_LoopExp, gen_ImperativeOCL_ImperativeLoopExp_ImperativeExpression, gen_ImperativeOCL_InstantiationExp_ImperativeExpression, gen_ImperativeOCL_Typedef_Class, gen_ImperativeOCL_UnlinkExp_ImperativeExpression, gen_ImperativeOCL_RaiseExp_ImperativeExpression, gen_ImperativeOCL_ReturnExp_ImperativeExpression, gen_ImperativeOCL_SwitchExp_ImperativeExpression, gen_ImperativeOCL_TryExp_ImperativeExpression, gen_QVTOperational_Constructor_ImperativeOperation, gen_QVTOperational_ConstructorBody_OperationBody, gen_QVTOperational_ContextualProperty_Property, gen_ImperativeOCL_VariableInitExp_ImperativeExpression, gen_ImperativeOCL_WhileExp_ImperativeExpression, gen_QVTOperational_Library_Module, gen_QVTOperational_EntryOperation_ImperativeOperation, gen_QVTOperational_Helper_ImperativeOperation, gen_QVTOperational_ImperativeCallExp_OperationCallExp, gen_QVTOperational_ImperativeCallExp_ImperativeExpression, gen_QVTOperational_ImperativeOperation_Operation, gen_QVTOperational_MappingParameter_VarParameter, gen_QVTOperational_MappingBody_OperationBody, gen_QVTOperational_MappingCallExp_ImperativeCallExp, gen_QVTOperational_MappingOperation_ImperativeOperation, gen_QVTOperational_ModelParameter_VarParameter, gen_QVTOperational_ModelType_Class, gen_QVTOperational_Module_Class, gen_QVTOperational_Module_Package, gen_QVTOperational_OperationBody_Element, gen_QVTOperational_OperationalTransformation_Module, gen_QVTOperational_ModuleImport_Element, gen_QVTOperational_ObjectExp_InstantiationExp, gen_QVTOperational_ResolveInExp_ResolveExp, gen_QVTOperational_VarParameter_Variable, gen_QVTOperational_VarParameter_Parameter, gen_QVTOperational_ResolveExp_CallExp, gen_QVTOperational_ResolveExp_ImperativeExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)