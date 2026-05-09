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

DirectionKind: Enumeration = Enumeration(
    name="DirectionKind",
    literals={
            EnumerationLiteral(name="in_"),
			EnumerationLiteral(name="inout"),
			EnumerationLiteral(name="out")
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

SeverityKind: Enumeration = Enumeration(
    name="SeverityKind",
    literals={
            EnumerationLiteral(name="error"),
			EnumerationLiteral(name="warning"),
			EnumerationLiteral(name="fatal")
    }
)

# Classes
FlatQVT_AltExp = Class(name="FlatQVT_AltExp")
ImperativeExpression = Class(name="ImperativeExpression")
FlatQVT_AnyType = Class(name="FlatQVT_AnyType")
Type = Class(name="Type")
FlatQVT_Area = Class(name="FlatQVT_Area", is_abstract=True)
FlatQVT_AssertExp = Class(name="FlatQVT_AssertExp")
FlatQVT_AssignExp = Class(name="FlatQVT_AssignExp")
FlatQVT_Assignment = Class(name="FlatQVT_Assignment", is_abstract=True)
Element = Class(name="Element")
FlatQVT_BagType = Class(name="FlatQVT_BagType")
CollectionType = Class(name="CollectionType")
FlatQVT_BlockExp = Class(name="FlatQVT_BlockExp")
FlatQVT_BooleanLiteralExp = Class(name="FlatQVT_BooleanLiteralExp")
PrimitiveLiteralExp = Class(name="PrimitiveLiteralExp")
FlatQVT_BottomPattern = Class(name="FlatQVT_BottomPattern")
CorePattern = Class(name="CorePattern")
FlatQVT_BreakExp = Class(name="FlatQVT_BreakExp")
FlatQVT_CallExp = Class(name="FlatQVT_CallExp", is_abstract=True)
OclExpression = Class(name="OclExpression")
FlatQVT_CatchExp = Class(name="FlatQVT_CatchExp")
FlatQVT_Class = Class(name="FlatQVT_Class")
FlatQVT_CollectionItem = Class(name="FlatQVT_CollectionItem")
CollectionLiteralPart = Class(name="CollectionLiteralPart")
FlatQVT_CollectionLiteralExp = Class(name="FlatQVT_CollectionLiteralExp")
LiteralExp = Class(name="LiteralExp")
FlatQVT_CollectionLiteralPart = Class(name="FlatQVT_CollectionLiteralPart", is_abstract=True)
TypedElement = Class(name="TypedElement")
FlatQVT_CollectionRange = Class(name="FlatQVT_CollectionRange")
FlatQVT_CollectionTemplateExp = Class(name="FlatQVT_CollectionTemplateExp")
TemplateExp = Class(name="TemplateExp")
FlatQVT_CollectionType = Class(name="FlatQVT_CollectionType")
DataType = Class(name="DataType")
FlatQVT_Comment = Class(name="FlatQVT_Comment")
FlatQVT_ComputeExp = Class(name="FlatQVT_ComputeExp")
FlatQVT_Constructor = Class(name="FlatQVT_Constructor")
ImperativeOperation = Class(name="ImperativeOperation")
FlatQVT_ConstructorBody = Class(name="FlatQVT_ConstructorBody")
OperationBody = Class(name="OperationBody")
FlatQVT_ContextualProperty = Class(name="FlatQVT_ContextualProperty")
Property_ = Class(name="Property")
FlatQVT_ContinueExp = Class(name="FlatQVT_ContinueExp")
FlatQVT_CoreDomain = Class(name="FlatQVT_CoreDomain")
Domain = Class(name="Domain")
Area = Class(name="Area")
FlatQVT_CorePattern = Class(name="FlatQVT_CorePattern")
Pattern = Class(name="Pattern")
FlatQVT_DataType = Class(name="FlatQVT_DataType")
FlatQVT_DictLiteralExp = Class(name="FlatQVT_DictLiteralExp")
FlatQVT_DictLiteralPart = Class(name="FlatQVT_DictLiteralPart")
FlatQVT_DictionaryType = Class(name="FlatQVT_DictionaryType")
FlatQVT_Domain = Class(name="FlatQVT_Domain", is_abstract=True)
NamedElement = Class(name="NamedElement")
FlatQVT_DomainPattern = Class(name="FlatQVT_DomainPattern")
FlatQVT_Element = Class(name="FlatQVT_Element", is_abstract=True)
Object = Class(name="Object")
FlatQVT_EnforcementOperation = Class(name="FlatQVT_EnforcementOperation")
FlatQVT_EntryOperation = Class(name="FlatQVT_EntryOperation")
FlatQVT_EnumLiteralExp = Class(name="FlatQVT_EnumLiteralExp")
FlatQVT_Enumeration = Class(name="FlatQVT_Enumeration")
FlatQVT_EnumerationLiteral = Class(name="FlatQVT_EnumerationLiteral")
FlatQVT_ExpressionInOcl = Class(name="FlatQVT_ExpressionInOcl")
FlatQVT_Extent = Class(name="FlatQVT_Extent")
FlatQVT_Factory = Class(name="FlatQVT_Factory")
FlatQVT_FeatureCallExp = Class(name="FlatQVT_FeatureCallExp", is_abstract=True)
CallExp = Class(name="CallExp")
FlatQVT_ForExp = Class(name="FlatQVT_ForExp")
ImperativeLoopExp = Class(name="ImperativeLoopExp")
FlatQVT_Function = Class(name="FlatQVT_Function")
Operation = Class(name="Operation")
FlatQVT_FunctionParameter = Class(name="FlatQVT_FunctionParameter")
Variable = Class(name="Variable")
Parameter_ = Class(name="Parameter")
FlatQVT_GuardPattern = Class(name="FlatQVT_GuardPattern")
FlatQVT_Helper = Class(name="FlatQVT_Helper")
FlatQVT_IfExp = Class(name="FlatQVT_IfExp")
FlatQVT_ImperativeCallExp = Class(name="FlatQVT_ImperativeCallExp")
OperationCallExp = Class(name="OperationCallExp")
FlatQVT_ImperativeExpression = Class(name="FlatQVT_ImperativeExpression", is_abstract=True)
FlatQVT_ImperativeIterateExp = Class(name="FlatQVT_ImperativeIterateExp")
FlatQVT_ImperativeLoopExp = Class(name="FlatQVT_ImperativeLoopExp", is_abstract=True)
LoopExp = Class(name="LoopExp")
FlatQVT_ImperativeOperation = Class(name="FlatQVT_ImperativeOperation")
FlatQVT_InstantiationExp = Class(name="FlatQVT_InstantiationExp")
FlatQVT_IntegerLiteralExp = Class(name="FlatQVT_IntegerLiteralExp")
NumericLiteralExp = Class(name="NumericLiteralExp")
FlatQVT_InvalidType = Class(name="FlatQVT_InvalidType")
FlatQVT_IterateExp = Class(name="FlatQVT_IterateExp")
FlatQVT_IteratorExp = Class(name="FlatQVT_IteratorExp")
FlatQVT_Key = Class(name="FlatQVT_Key")
FlatQVT_LetExp = Class(name="FlatQVT_LetExp")
FlatQVT_Library = Class(name="FlatQVT_Library")
Module = Class(name="Module")
FlatQVT_ListLiteralExp = Class(name="FlatQVT_ListLiteralExp")
FlatQVT_ListType = Class(name="FlatQVT_ListType")
FlatQVT_LiteralExp = Class(name="FlatQVT_LiteralExp", is_abstract=True)
FlatQVT_LogExp = Class(name="FlatQVT_LogExp")
FlatQVT_LoopExp = Class(name="FlatQVT_LoopExp", is_abstract=True)
FlatQVT_Mapping = Class(name="FlatQVT_Mapping")
Rule = Class(name="Rule")
FlatQVT_MappingBody = Class(name="FlatQVT_MappingBody")
FlatQVT_MappingCallExp = Class(name="FlatQVT_MappingCallExp")
ImperativeCallExp = Class(name="ImperativeCallExp")
FlatQVT_InvalidLiteralExp = Class(name="FlatQVT_InvalidLiteralExp")
FlatQVT_MappingOperation = Class(name="FlatQVT_MappingOperation")
FlatQVT_MappingParameter = Class(name="FlatQVT_MappingParameter")
VarParameter = Class(name="VarParameter")
FlatQVT_ModelParameter = Class(name="FlatQVT_ModelParameter")
FlatQVT_ModelType = Class(name="FlatQVT_ModelType")
Class_ = Class(name="Class")
FlatQVT_Module = Class(name="FlatQVT_Module")
Package = Class(name="Package")
FlatQVT_ModuleImport = Class(name="FlatQVT_ModuleImport")
FlatQVT_MultiplicityElement = Class(name="FlatQVT_MultiplicityElement", is_abstract=True)
FlatQVT_NamedElement = Class(name="FlatQVT_NamedElement", is_abstract=True)
FlatQVT_NavigationCallExp = Class(name="FlatQVT_NavigationCallExp")
FeatureCallExp = Class(name="FeatureCallExp")
FlatQVT_NullLiteralExp = Class(name="FlatQVT_NullLiteralExp")
FlatQVT_NumericLiteralExp = Class(name="FlatQVT_NumericLiteralExp", is_abstract=True)
FlatQVT_Object = Class(name="FlatQVT_Object")
FlatQVT_ObjectExp = Class(name="FlatQVT_ObjectExp")
InstantiationExp = Class(name="InstantiationExp")
FlatQVT_ObjectTemplateExp = Class(name="FlatQVT_ObjectTemplateExp")
FlatQVT_OclExpression = Class(name="FlatQVT_OclExpression", is_abstract=True)
FlatQVT_Operation = Class(name="FlatQVT_Operation")
MultiplicityElement = Class(name="MultiplicityElement")
FlatQVT_OperationBody = Class(name="FlatQVT_OperationBody")
FlatQVT_OperationCallExp = Class(name="FlatQVT_OperationCallExp")
FlatQVT_OperationalTransformation = Class(name="FlatQVT_OperationalTransformation")
FlatQVT_OppositePropertyCallExp = Class(name="FlatQVT_OppositePropertyCallExp")
PropertyCallExp = Class(name="PropertyCallExp")
FlatQVT_Package = Class(name="FlatQVT_Package")
FlatQVT_Parameter = Class(name="FlatQVT_Parameter")
FlatQVT_Pattern = Class(name="FlatQVT_Pattern")
FlatQVT_Predicate = Class(name="FlatQVT_Predicate")
FlatQVT_PrimitiveLiteralExp = Class(name="FlatQVT_PrimitiveLiteralExp", is_abstract=True)
FlatQVT_PrimitiveType = Class(name="FlatQVT_PrimitiveType")
FlatQVT_Property = Class(name="FlatQVT_Property")
FlatQVT_PropertyAssignment = Class(name="FlatQVT_PropertyAssignment")
Assignment = Class(name="Assignment")
FlatQVT_PropertyCallExp = Class(name="FlatQVT_PropertyCallExp")
NavigationCallExp = Class(name="NavigationCallExp")
FlatQVT_PropertyTemplateItem = Class(name="FlatQVT_PropertyTemplateItem")
FlatQVT_RaiseExp = Class(name="FlatQVT_RaiseExp")
FlatQVT_RealLiteralExp = Class(name="FlatQVT_RealLiteralExp")
FlatQVT_OrderedSetType = Class(name="FlatQVT_OrderedSetType")
FlatQVT_ReflectiveCollection = Class(name="FlatQVT_ReflectiveCollection")
FlatQVT_ReflectiveSequence = Class(name="FlatQVT_ReflectiveSequence")
ReflectiveCollection = Class(name="ReflectiveCollection")
FlatQVT_Relation = Class(name="FlatQVT_Relation")
FlatQVT_RelationCallExp = Class(name="FlatQVT_RelationCallExp")
FlatQVT_RelationDomain = Class(name="FlatQVT_RelationDomain")
FlatQVT_RelationDomainAssignment = Class(name="FlatQVT_RelationDomainAssignment")
FlatQVT_RelationImplementation = Class(name="FlatQVT_RelationImplementation")
FlatQVT_RealizedVariable = Class(name="FlatQVT_RealizedVariable")
FlatQVT_ResolveExp = Class(name="FlatQVT_ResolveExp")
FlatQVT_ResolveInExp = Class(name="FlatQVT_ResolveInExp")
ResolveExp = Class(name="ResolveExp")
FlatQVT_ReturnExp = Class(name="FlatQVT_ReturnExp")
FlatQVT_Rule = Class(name="FlatQVT_Rule", is_abstract=True)
FlatQVT_SequenceType = Class(name="FlatQVT_SequenceType")
FlatQVT_SetType = Class(name="FlatQVT_SetType")
FlatQVT_StringLiteralExp = Class(name="FlatQVT_StringLiteralExp")
FlatQVT_SwitchExp = Class(name="FlatQVT_SwitchExp")
FlatQVT_Tag = Class(name="FlatQVT_Tag")
FlatQVT_TemplateExp = Class(name="FlatQVT_TemplateExp", is_abstract=True)
FlatQVT_TemplateParameterType = Class(name="FlatQVT_TemplateParameterType")
FlatQVT_Transformation = Class(name="FlatQVT_Transformation")
FlatQVT_RelationalTransformation = Class(name="FlatQVT_RelationalTransformation")
Transformation = Class(name="Transformation")
FlatQVT_TryExp = Class(name="FlatQVT_TryExp")
FlatQVT_TupleLiteralExp = Class(name="FlatQVT_TupleLiteralExp")
FlatQVT_TupleLiteralPart = Class(name="FlatQVT_TupleLiteralPart")
FlatQVT_TupleType = Class(name="FlatQVT_TupleType")
FlatQVT_Type = Class(name="FlatQVT_Type", is_abstract=True)
FlatQVT_TypeExp = Class(name="FlatQVT_TypeExp")
FlatQVT_TypedElement = Class(name="FlatQVT_TypedElement", is_abstract=True)
FlatQVT_TypedModel = Class(name="FlatQVT_TypedModel")
FlatQVT_Typedef = Class(name="FlatQVT_Typedef")
FlatQVT_URIExtent = Class(name="FlatQVT_URIExtent")
Extent = Class(name="Extent")
FlatQVT_UnlimitedNaturalExp = Class(name="FlatQVT_UnlimitedNaturalExp")
FlatQVT_UnlinkExp = Class(name="FlatQVT_UnlinkExp")
FlatQVT_VarParameter = Class(name="FlatQVT_VarParameter")
FlatQVT_Variable = Class(name="FlatQVT_Variable")
FlatQVT_VariableExp = Class(name="FlatQVT_VariableExp")
FlatQVT_VariableInitExp = Class(name="FlatQVT_VariableInitExp")
FlatQVT_VoidType = Class(name="FlatQVT_VoidType")
FlatQVT_WhileExp = Class(name="FlatQVT_WhileExp")
FlatQVT_VariableAssignment = Class(name="FlatQVT_VariableAssignment")

# FlatQVT_AltExp class attributes and methods

# ImperativeExpression class attributes and methods

# FlatQVT_AnyType class attributes and methods

# Type class attributes and methods

# FlatQVT_Area class attributes and methods

# FlatQVT_AssertExp class attributes and methods

# FlatQVT_AssignExp class attributes and methods

# FlatQVT_Assignment class attributes and methods

# Element class attributes and methods

# FlatQVT_BagType class attributes and methods

# CollectionType class attributes and methods

# FlatQVT_BlockExp class attributes and methods

# FlatQVT_BooleanLiteralExp class attributes and methods

# PrimitiveLiteralExp class attributes and methods

# FlatQVT_BottomPattern class attributes and methods

# CorePattern class attributes and methods

# FlatQVT_BreakExp class attributes and methods

# FlatQVT_CallExp class attributes and methods

# OclExpression class attributes and methods

# FlatQVT_CatchExp class attributes and methods

# FlatQVT_Class class attributes and methods

# FlatQVT_CollectionItem class attributes and methods

# CollectionLiteralPart class attributes and methods

# FlatQVT_CollectionLiteralExp class attributes and methods

# LiteralExp class attributes and methods

# FlatQVT_CollectionLiteralPart class attributes and methods

# TypedElement class attributes and methods

# FlatQVT_CollectionRange class attributes and methods

# FlatQVT_CollectionTemplateExp class attributes and methods

# TemplateExp class attributes and methods

# FlatQVT_CollectionType class attributes and methods

# DataType class attributes and methods

# FlatQVT_Comment class attributes and methods

# FlatQVT_ComputeExp class attributes and methods

# FlatQVT_Constructor class attributes and methods

# ImperativeOperation class attributes and methods

# FlatQVT_ConstructorBody class attributes and methods

# OperationBody class attributes and methods

# FlatQVT_ContextualProperty class attributes and methods

# Property class attributes and methods

# FlatQVT_ContinueExp class attributes and methods

# FlatQVT_CoreDomain class attributes and methods

# Domain class attributes and methods

# Area class attributes and methods

# FlatQVT_CorePattern class attributes and methods

# Pattern class attributes and methods

# FlatQVT_DataType class attributes and methods

# FlatQVT_DictLiteralExp class attributes and methods

# FlatQVT_DictLiteralPart class attributes and methods

# FlatQVT_DictionaryType class attributes and methods

# FlatQVT_Domain class attributes and methods

# NamedElement class attributes and methods

# FlatQVT_DomainPattern class attributes and methods

# FlatQVT_Element class attributes and methods
FlatQVT_Element_m_equals: Method = Method(name="equals", parameters={Parameter(name='FlatQVT_object', type=StringType)}, type=StringType)
FlatQVT_Element_m_get: Method = Method(name="get", parameters={Parameter(name='FlatQVT_property', type=StringType)}, type=Object)
FlatQVT_Element_m_getMetaClass: Method = Method(name="getMetaClass", parameters={}, type=StringType)
FlatQVT_Element_m_isSet: Method = Method(name="isSet", parameters={Parameter(name='FlatQVT_property', type=StringType)}, type=StringType)
FlatQVT_Element_m_set: Method = Method(name="set", parameters={Parameter(name='FlatQVT_object', type=StringType), Parameter(name='FlatQVT_property', type=StringType)})
FlatQVT_Element_m_unset: Method = Method(name="unset", parameters={Parameter(name='FlatQVT_property', type=StringType)})
FlatQVT_Element_m_container: Method = Method(name="container", parameters={}, type=Element)
FlatQVT_Element.methods={FlatQVT_Element_m_getMetaClass, FlatQVT_Element_m_get, FlatQVT_Element_m_unset, FlatQVT_Element_m_equals, FlatQVT_Element_m_container, FlatQVT_Element_m_isSet, FlatQVT_Element_m_set}

# Object class attributes and methods

# FlatQVT_EnforcementOperation class attributes and methods

# FlatQVT_EntryOperation class attributes and methods

# FlatQVT_EnumLiteralExp class attributes and methods

# FlatQVT_Enumeration class attributes and methods

# FlatQVT_EnumerationLiteral class attributes and methods

# FlatQVT_ExpressionInOcl class attributes and methods

# FlatQVT_Extent class attributes and methods
FlatQVT_Extent_m_elements: Method = Method(name="elements", parameters={}, type=StringType)
FlatQVT_Extent_m_useContainment: Method = Method(name="useContainment", parameters={}, type=StringType)
FlatQVT_Extent.methods={FlatQVT_Extent_m_elements, FlatQVT_Extent_m_useContainment}

# FlatQVT_Factory class attributes and methods
FlatQVT_Factory_m_convertToString: Method = Method(name="convertToString", parameters={Parameter(name='FlatQVT_object', type=StringType), Parameter(name='FlatQVT_dataType', type=StringType)}, type=StringType)
FlatQVT_Factory_m_create: Method = Method(name="create", parameters={Parameter(name='FlatQVT_metaClass', type=StringType)}, type=Element)
FlatQVT_Factory_m_createFromString: Method = Method(name="createFromString", parameters={Parameter(name='FlatQVT_dataType', type=StringType), Parameter(name='FlatQVT_string', type=StringType)}, type=Object)
FlatQVT_Factory.methods={FlatQVT_Factory_m_createFromString, FlatQVT_Factory_m_convertToString, FlatQVT_Factory_m_create}

# FlatQVT_FeatureCallExp class attributes and methods

# CallExp class attributes and methods

# FlatQVT_ForExp class attributes and methods

# ImperativeLoopExp class attributes and methods

# FlatQVT_Function class attributes and methods

# Operation class attributes and methods

# FlatQVT_FunctionParameter class attributes and methods

# Variable class attributes and methods

# Parameter class attributes and methods

# FlatQVT_GuardPattern class attributes and methods

# FlatQVT_Helper class attributes and methods

# FlatQVT_IfExp class attributes and methods

# FlatQVT_ImperativeCallExp class attributes and methods

# OperationCallExp class attributes and methods

# FlatQVT_ImperativeExpression class attributes and methods

# FlatQVT_ImperativeIterateExp class attributes and methods

# FlatQVT_ImperativeLoopExp class attributes and methods

# LoopExp class attributes and methods

# FlatQVT_ImperativeOperation class attributes and methods

# FlatQVT_InstantiationExp class attributes and methods

# FlatQVT_IntegerLiteralExp class attributes and methods

# NumericLiteralExp class attributes and methods

# FlatQVT_InvalidType class attributes and methods

# FlatQVT_IterateExp class attributes and methods

# FlatQVT_IteratorExp class attributes and methods

# FlatQVT_Key class attributes and methods

# FlatQVT_LetExp class attributes and methods

# FlatQVT_Library class attributes and methods

# Module class attributes and methods

# FlatQVT_ListLiteralExp class attributes and methods

# FlatQVT_ListType class attributes and methods

# FlatQVT_LiteralExp class attributes and methods

# FlatQVT_LogExp class attributes and methods

# FlatQVT_LoopExp class attributes and methods

# FlatQVT_Mapping class attributes and methods

# Rule class attributes and methods

# FlatQVT_MappingBody class attributes and methods

# FlatQVT_MappingCallExp class attributes and methods

# ImperativeCallExp class attributes and methods

# FlatQVT_InvalidLiteralExp class attributes and methods

# FlatQVT_MappingOperation class attributes and methods

# FlatQVT_MappingParameter class attributes and methods

# VarParameter class attributes and methods

# FlatQVT_ModelParameter class attributes and methods

# FlatQVT_ModelType class attributes and methods

# Class class attributes and methods

# FlatQVT_Module class attributes and methods

# Package class attributes and methods

# FlatQVT_ModuleImport class attributes and methods

# FlatQVT_MultiplicityElement class attributes and methods

# FlatQVT_NamedElement class attributes and methods

# FlatQVT_NavigationCallExp class attributes and methods

# FeatureCallExp class attributes and methods

# FlatQVT_NullLiteralExp class attributes and methods

# FlatQVT_NumericLiteralExp class attributes and methods

# FlatQVT_Object class attributes and methods

# FlatQVT_ObjectExp class attributes and methods

# InstantiationExp class attributes and methods

# FlatQVT_ObjectTemplateExp class attributes and methods

# FlatQVT_OclExpression class attributes and methods

# FlatQVT_Operation class attributes and methods

# MultiplicityElement class attributes and methods

# FlatQVT_OperationBody class attributes and methods

# FlatQVT_OperationCallExp class attributes and methods

# FlatQVT_OperationalTransformation class attributes and methods

# FlatQVT_OppositePropertyCallExp class attributes and methods

# PropertyCallExp class attributes and methods

# FlatQVT_Package class attributes and methods

# FlatQVT_Parameter class attributes and methods

# FlatQVT_Pattern class attributes and methods

# FlatQVT_Predicate class attributes and methods

# FlatQVT_PrimitiveLiteralExp class attributes and methods

# FlatQVT_PrimitiveType class attributes and methods

# FlatQVT_Property class attributes and methods

# FlatQVT_PropertyAssignment class attributes and methods

# Assignment class attributes and methods

# FlatQVT_PropertyCallExp class attributes and methods

# NavigationCallExp class attributes and methods

# FlatQVT_PropertyTemplateItem class attributes and methods

# FlatQVT_RaiseExp class attributes and methods

# FlatQVT_RealLiteralExp class attributes and methods

# FlatQVT_OrderedSetType class attributes and methods

# FlatQVT_ReflectiveCollection class attributes and methods
FlatQVT_ReflectiveCollection_m_add: Method = Method(name="add", parameters={Parameter(name='FlatQVT_object', type=StringType)}, type=StringType)
FlatQVT_ReflectiveCollection_m_addAll: Method = Method(name="addAll", parameters={Parameter(name='FlatQVT_objects', type=StringType)}, type=StringType)
FlatQVT_ReflectiveCollection_m_clear: Method = Method(name="clear", parameters={})
FlatQVT_ReflectiveCollection_m_remove: Method = Method(name="remove", parameters={Parameter(name='FlatQVT_object', type=StringType)}, type=StringType)
FlatQVT_ReflectiveCollection_m_size: Method = Method(name="size", parameters={}, type=StringType)
FlatQVT_ReflectiveCollection.methods={FlatQVT_ReflectiveCollection_m_add, FlatQVT_ReflectiveCollection_m_remove, FlatQVT_ReflectiveCollection_m_addAll, FlatQVT_ReflectiveCollection_m_size, FlatQVT_ReflectiveCollection_m_clear}

# FlatQVT_ReflectiveSequence class attributes and methods
FlatQVT_ReflectiveSequence_m_add: Method = Method(name="add", parameters={Parameter(name='FlatQVT_object', type=StringType), Parameter(name='FlatQVT_index', type=StringType)})
FlatQVT_ReflectiveSequence_m_get: Method = Method(name="get", parameters={Parameter(name='FlatQVT_index', type=StringType)}, type=Object)
FlatQVT_ReflectiveSequence_m_remove: Method = Method(name="remove", parameters={Parameter(name='FlatQVT_index', type=StringType)}, type=Object)
FlatQVT_ReflectiveSequence_m_set: Method = Method(name="set", parameters={Parameter(name='FlatQVT_object', type=StringType), Parameter(name='FlatQVT_index', type=StringType)}, type=Object)
FlatQVT_ReflectiveSequence.methods={FlatQVT_ReflectiveSequence_m_set, FlatQVT_ReflectiveSequence_m_add, FlatQVT_ReflectiveSequence_m_remove, FlatQVT_ReflectiveSequence_m_get}

# ReflectiveCollection class attributes and methods

# FlatQVT_Relation class attributes and methods

# FlatQVT_RelationCallExp class attributes and methods

# FlatQVT_RelationDomain class attributes and methods

# FlatQVT_RelationDomainAssignment class attributes and methods

# FlatQVT_RelationImplementation class attributes and methods

# FlatQVT_RealizedVariable class attributes and methods

# FlatQVT_ResolveExp class attributes and methods

# FlatQVT_ResolveInExp class attributes and methods

# ResolveExp class attributes and methods

# FlatQVT_ReturnExp class attributes and methods

# FlatQVT_Rule class attributes and methods

# FlatQVT_SequenceType class attributes and methods

# FlatQVT_SetType class attributes and methods

# FlatQVT_StringLiteralExp class attributes and methods

# FlatQVT_SwitchExp class attributes and methods

# FlatQVT_Tag class attributes and methods

# FlatQVT_TemplateExp class attributes and methods

# FlatQVT_TemplateParameterType class attributes and methods

# FlatQVT_Transformation class attributes and methods

# FlatQVT_RelationalTransformation class attributes and methods

# Transformation class attributes and methods

# FlatQVT_TryExp class attributes and methods

# FlatQVT_TupleLiteralExp class attributes and methods

# FlatQVT_TupleLiteralPart class attributes and methods

# FlatQVT_TupleType class attributes and methods

# FlatQVT_Type class attributes and methods
FlatQVT_Type_m_isInstance: Method = Method(name="isInstance", parameters={Parameter(name='FlatQVT_object', type=StringType)}, type=StringType)
FlatQVT_Type.methods={FlatQVT_Type_m_isInstance}

# FlatQVT_TypeExp class attributes and methods

# FlatQVT_TypedElement class attributes and methods

# FlatQVT_TypedModel class attributes and methods

# FlatQVT_Typedef class attributes and methods

# FlatQVT_URIExtent class attributes and methods
FlatQVT_URIExtent_m_contextURI: Method = Method(name="contextURI", parameters={}, type=StringType)
FlatQVT_URIExtent_m_element: Method = Method(name="element", parameters={Parameter(name='FlatQVT_uri', type=StringType)}, type=Element)
FlatQVT_URIExtent_m_uri: Method = Method(name="uri", parameters={Parameter(name='FlatQVT_element', type=StringType)}, type=StringType)
FlatQVT_URIExtent.methods={FlatQVT_URIExtent_m_element, FlatQVT_URIExtent_m_contextURI, FlatQVT_URIExtent_m_uri}

# Extent class attributes and methods

# FlatQVT_UnlimitedNaturalExp class attributes and methods

# FlatQVT_UnlinkExp class attributes and methods

# FlatQVT_VarParameter class attributes and methods

# FlatQVT_Variable class attributes and methods

# FlatQVT_VariableExp class attributes and methods

# FlatQVT_VariableInitExp class attributes and methods

# FlatQVT_VoidType class attributes and methods

# FlatQVT_WhileExp class attributes and methods

# FlatQVT_VariableAssignment class attributes and methods

# Generalizations
gen_FlatQVT_AltExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_AltExp)
gen_FlatQVT_AnyType_Type = Generalization(general=Type, specific=FlatQVT_AnyType)
gen_FlatQVT_AssertExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_AssertExp)
gen_FlatQVT_AssignExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_AssignExp)
gen_FlatQVT_Assignment_Element = Generalization(general=Element, specific=FlatQVT_Assignment)
gen_FlatQVT_BagType_CollectionType = Generalization(general=CollectionType, specific=FlatQVT_BagType)
gen_FlatQVT_BlockExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_BlockExp)
gen_FlatQVT_BooleanLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=FlatQVT_BooleanLiteralExp)
gen_FlatQVT_BottomPattern_CorePattern = Generalization(general=CorePattern, specific=FlatQVT_BottomPattern)
gen_FlatQVT_BreakExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_BreakExp)
gen_FlatQVT_CallExp_OclExpression = Generalization(general=OclExpression, specific=FlatQVT_CallExp)
gen_FlatQVT_CatchExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_CatchExp)
gen_FlatQVT_Class_Type = Generalization(general=Type, specific=FlatQVT_Class)
gen_FlatQVT_CollectionItem_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=FlatQVT_CollectionItem)
gen_FlatQVT_CollectionLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=FlatQVT_CollectionLiteralExp)
gen_FlatQVT_CollectionLiteralPart_TypedElement = Generalization(general=TypedElement, specific=FlatQVT_CollectionLiteralPart)
gen_FlatQVT_CollectionRange_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=FlatQVT_CollectionRange)
gen_FlatQVT_CollectionTemplateExp_TemplateExp = Generalization(general=TemplateExp, specific=FlatQVT_CollectionTemplateExp)
gen_FlatQVT_CollectionType_DataType = Generalization(general=DataType, specific=FlatQVT_CollectionType)
gen_FlatQVT_Comment_Element = Generalization(general=Element, specific=FlatQVT_Comment)
gen_FlatQVT_ComputeExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_ComputeExp)
gen_FlatQVT_Constructor_ImperativeOperation = Generalization(general=ImperativeOperation, specific=FlatQVT_Constructor)
gen_FlatQVT_ConstructorBody_OperationBody = Generalization(general=OperationBody, specific=FlatQVT_ConstructorBody)
gen_FlatQVT_ContextualProperty_Property = Generalization(general=Property_, specific=FlatQVT_ContextualProperty)
gen_FlatQVT_ContinueExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_ContinueExp)
gen_FlatQVT_CoreDomain_Domain = Generalization(general=Domain, specific=FlatQVT_CoreDomain)
gen_FlatQVT_CoreDomain_Area = Generalization(general=Area, specific=FlatQVT_CoreDomain)
gen_FlatQVT_CorePattern_Pattern = Generalization(general=Pattern, specific=FlatQVT_CorePattern)
gen_FlatQVT_DataType_Type = Generalization(general=Type, specific=FlatQVT_DataType)
gen_FlatQVT_DictLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=FlatQVT_DictLiteralExp)
gen_FlatQVT_DictLiteralPart_Element = Generalization(general=Element, specific=FlatQVT_DictLiteralPart)
gen_FlatQVT_DictionaryType_CollectionType = Generalization(general=CollectionType, specific=FlatQVT_DictionaryType)
gen_FlatQVT_Domain_NamedElement = Generalization(general=NamedElement, specific=FlatQVT_Domain)
gen_FlatQVT_DomainPattern_Pattern = Generalization(general=Pattern, specific=FlatQVT_DomainPattern)
gen_FlatQVT_EnforcementOperation_Element = Generalization(general=Element, specific=FlatQVT_EnforcementOperation)
gen_FlatQVT_EntryOperation_ImperativeOperation = Generalization(general=ImperativeOperation, specific=FlatQVT_EntryOperation)
gen_FlatQVT_EnumLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=FlatQVT_EnumLiteralExp)
gen_FlatQVT_Enumeration_DataType = Generalization(general=DataType, specific=FlatQVT_Enumeration)
gen_FlatQVT_EnumerationLiteral_NamedElement = Generalization(general=NamedElement, specific=FlatQVT_EnumerationLiteral)
gen_FlatQVT_ExpressionInOcl_TypedElement = Generalization(general=TypedElement, specific=FlatQVT_ExpressionInOcl)
gen_FlatQVT_Extent_Object = Generalization(general=Object, specific=FlatQVT_Extent)
gen_FlatQVT_Factory_Element = Generalization(general=Element, specific=FlatQVT_Factory)
gen_FlatQVT_Element_Object = Generalization(general=Object, specific=FlatQVT_Element)
gen_FlatQVT_FeatureCallExp_CallExp = Generalization(general=CallExp, specific=FlatQVT_FeatureCallExp)
gen_FlatQVT_ForExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=FlatQVT_ForExp)
gen_FlatQVT_Function_Operation = Generalization(general=Operation, specific=FlatQVT_Function)
gen_FlatQVT_FunctionParameter_Variable = Generalization(general=Variable, specific=FlatQVT_FunctionParameter)
gen_FlatQVT_FunctionParameter_Parameter = Generalization(general=Parameter_, specific=FlatQVT_FunctionParameter)
gen_FlatQVT_GuardPattern_CorePattern = Generalization(general=CorePattern, specific=FlatQVT_GuardPattern)
gen_FlatQVT_Helper_ImperativeOperation = Generalization(general=ImperativeOperation, specific=FlatQVT_Helper)
gen_FlatQVT_IfExp_OclExpression = Generalization(general=OclExpression, specific=FlatQVT_IfExp)
gen_FlatQVT_ImperativeCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=FlatQVT_ImperativeCallExp)
gen_FlatQVT_ImperativeCallExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_ImperativeCallExp)
gen_FlatQVT_ImperativeExpression_OclExpression = Generalization(general=OclExpression, specific=FlatQVT_ImperativeExpression)
gen_FlatQVT_ImperativeIterateExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=FlatQVT_ImperativeIterateExp)
gen_FlatQVT_ImperativeLoopExp_LoopExp = Generalization(general=LoopExp, specific=FlatQVT_ImperativeLoopExp)
gen_FlatQVT_ImperativeLoopExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_ImperativeLoopExp)
gen_FlatQVT_ImperativeOperation_Operation = Generalization(general=Operation, specific=FlatQVT_ImperativeOperation)
gen_FlatQVT_InstantiationExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_InstantiationExp)
gen_FlatQVT_IntegerLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=FlatQVT_IntegerLiteralExp)
gen_FlatQVT_InvalidType_Type = Generalization(general=Type, specific=FlatQVT_InvalidType)
gen_FlatQVT_IterateExp_LoopExp = Generalization(general=LoopExp, specific=FlatQVT_IterateExp)
gen_FlatQVT_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=FlatQVT_IteratorExp)
gen_FlatQVT_Key_Element = Generalization(general=Element, specific=FlatQVT_Key)
gen_FlatQVT_LetExp_OclExpression = Generalization(general=OclExpression, specific=FlatQVT_LetExp)
gen_FlatQVT_Library_Module = Generalization(general=Module, specific=FlatQVT_Library)
gen_FlatQVT_ListLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=FlatQVT_ListLiteralExp)
gen_FlatQVT_ListType_CollectionType = Generalization(general=CollectionType, specific=FlatQVT_ListType)
gen_FlatQVT_LiteralExp_OclExpression = Generalization(general=OclExpression, specific=FlatQVT_LiteralExp)
gen_FlatQVT_LogExp_OperationCallExp = Generalization(general=OperationCallExp, specific=FlatQVT_LogExp)
gen_FlatQVT_LogExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_LogExp)
gen_FlatQVT_LoopExp_CallExp = Generalization(general=CallExp, specific=FlatQVT_LoopExp)
gen_FlatQVT_LoopExp_OclExpression = Generalization(general=OclExpression, specific=FlatQVT_LoopExp)
gen_FlatQVT_Mapping_Rule = Generalization(general=Rule, specific=FlatQVT_Mapping)
gen_FlatQVT_Mapping_Area = Generalization(general=Area, specific=FlatQVT_Mapping)
gen_FlatQVT_MappingBody_OperationBody = Generalization(general=OperationBody, specific=FlatQVT_MappingBody)
gen_FlatQVT_InvalidLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=FlatQVT_InvalidLiteralExp)
gen_FlatQVT_MappingOperation_ImperativeOperation = Generalization(general=ImperativeOperation, specific=FlatQVT_MappingOperation)
gen_FlatQVT_MappingParameter_VarParameter = Generalization(general=VarParameter, specific=FlatQVT_MappingParameter)
gen_FlatQVT_ModelParameter_VarParameter = Generalization(general=VarParameter, specific=FlatQVT_ModelParameter)
gen_FlatQVT_ModelType_Class = Generalization(general=Class_, specific=FlatQVT_ModelType)
gen_FlatQVT_Module_Class = Generalization(general=Class_, specific=FlatQVT_Module)
gen_FlatQVT_Module_Package = Generalization(general=Package, specific=FlatQVT_Module)
gen_FlatQVT_ModuleImport_Element = Generalization(general=Element, specific=FlatQVT_ModuleImport)
gen_FlatQVT_MappingCallExp_ImperativeCallExp = Generalization(general=ImperativeCallExp, specific=FlatQVT_MappingCallExp)
gen_FlatQVT_NamedElement_Element = Generalization(general=Element, specific=FlatQVT_NamedElement)
gen_FlatQVT_NavigationCallExp_FeatureCallExp = Generalization(general=FeatureCallExp, specific=FlatQVT_NavigationCallExp)
gen_FlatQVT_NullLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=FlatQVT_NullLiteralExp)
gen_FlatQVT_NumericLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=FlatQVT_NumericLiteralExp)
gen_FlatQVT_ObjectExp_InstantiationExp = Generalization(general=InstantiationExp, specific=FlatQVT_ObjectExp)
gen_FlatQVT_ObjectTemplateExp_TemplateExp = Generalization(general=TemplateExp, specific=FlatQVT_ObjectTemplateExp)
gen_FlatQVT_OclExpression_TypedElement = Generalization(general=TypedElement, specific=FlatQVT_OclExpression)
gen_FlatQVT_Operation_TypedElement = Generalization(general=TypedElement, specific=FlatQVT_Operation)
gen_FlatQVT_Operation_MultiplicityElement = Generalization(general=MultiplicityElement, specific=FlatQVT_Operation)
gen_FlatQVT_OperationBody_Element = Generalization(general=Element, specific=FlatQVT_OperationBody)
gen_FlatQVT_OperationCallExp_FeatureCallExp = Generalization(general=FeatureCallExp, specific=FlatQVT_OperationCallExp)
gen_FlatQVT_OperationalTransformation_Module = Generalization(general=Module, specific=FlatQVT_OperationalTransformation)
gen_FlatQVT_OppositePropertyCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=FlatQVT_OppositePropertyCallExp)
gen_FlatQVT_Package_NamedElement = Generalization(general=NamedElement, specific=FlatQVT_Package)
gen_FlatQVT_Parameter_TypedElement = Generalization(general=TypedElement, specific=FlatQVT_Parameter)
gen_FlatQVT_Parameter_MultiplicityElement = Generalization(general=MultiplicityElement, specific=FlatQVT_Parameter)
gen_FlatQVT_Pattern_Element = Generalization(general=Element, specific=FlatQVT_Pattern)
gen_FlatQVT_Predicate_Element = Generalization(general=Element, specific=FlatQVT_Predicate)
gen_FlatQVT_PrimitiveLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=FlatQVT_PrimitiveLiteralExp)
gen_FlatQVT_PrimitiveType_DataType = Generalization(general=DataType, specific=FlatQVT_PrimitiveType)
gen_FlatQVT_Property_TypedElement = Generalization(general=TypedElement, specific=FlatQVT_Property)
gen_FlatQVT_Property_MultiplicityElement = Generalization(general=MultiplicityElement, specific=FlatQVT_Property)
gen_FlatQVT_PropertyAssignment_Assignment = Generalization(general=Assignment, specific=FlatQVT_PropertyAssignment)
gen_FlatQVT_PropertyCallExp_NavigationCallExp = Generalization(general=NavigationCallExp, specific=FlatQVT_PropertyCallExp)
gen_FlatQVT_PropertyTemplateItem_Element = Generalization(general=Element, specific=FlatQVT_PropertyTemplateItem)
gen_FlatQVT_RaiseExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_RaiseExp)
gen_FlatQVT_RealLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=FlatQVT_RealLiteralExp)
gen_FlatQVT_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=FlatQVT_OrderedSetType)
gen_FlatQVT_RealizedVariable_Variable = Generalization(general=Variable, specific=FlatQVT_RealizedVariable)
gen_FlatQVT_ReflectiveCollection_Object = Generalization(general=Object, specific=FlatQVT_ReflectiveCollection)
gen_FlatQVT_ReflectiveSequence_ReflectiveCollection = Generalization(general=ReflectiveCollection, specific=FlatQVT_ReflectiveSequence)
gen_FlatQVT_Relation_Rule = Generalization(general=Rule, specific=FlatQVT_Relation)
gen_FlatQVT_RelationCallExp_OclExpression = Generalization(general=OclExpression, specific=FlatQVT_RelationCallExp)
gen_FlatQVT_RelationDomain_Domain = Generalization(general=Domain, specific=FlatQVT_RelationDomain)
gen_FlatQVT_RelationDomainAssignment_Element = Generalization(general=Element, specific=FlatQVT_RelationDomainAssignment)
gen_FlatQVT_RelationImplementation_Element = Generalization(general=Element, specific=FlatQVT_RelationImplementation)
gen_FlatQVT_ResolveExp_CallExp = Generalization(general=CallExp, specific=FlatQVT_ResolveExp)
gen_FlatQVT_ResolveExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_ResolveExp)
gen_FlatQVT_ResolveInExp_ResolveExp = Generalization(general=ResolveExp, specific=FlatQVT_ResolveInExp)
gen_FlatQVT_ReturnExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_ReturnExp)
gen_FlatQVT_Rule_NamedElement = Generalization(general=NamedElement, specific=FlatQVT_Rule)
gen_FlatQVT_SequenceType_CollectionType = Generalization(general=CollectionType, specific=FlatQVT_SequenceType)
gen_FlatQVT_SetType_CollectionType = Generalization(general=CollectionType, specific=FlatQVT_SetType)
gen_FlatQVT_StringLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=FlatQVT_StringLiteralExp)
gen_FlatQVT_SwitchExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_SwitchExp)
gen_FlatQVT_Tag_Element = Generalization(general=Element, specific=FlatQVT_Tag)
gen_FlatQVT_TemplateExp_LiteralExp = Generalization(general=LiteralExp, specific=FlatQVT_TemplateExp)
gen_FlatQVT_TemplateParameterType_Type = Generalization(general=Type, specific=FlatQVT_TemplateParameterType)
gen_FlatQVT_Transformation_Class = Generalization(general=Class_, specific=FlatQVT_Transformation)
gen_FlatQVT_Transformation_Package = Generalization(general=Package, specific=FlatQVT_Transformation)
gen_FlatQVT_RelationalTransformation_Transformation = Generalization(general=Transformation, specific=FlatQVT_RelationalTransformation)
gen_FlatQVT_TryExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_TryExp)
gen_FlatQVT_TupleLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=FlatQVT_TupleLiteralExp)
gen_FlatQVT_TupleLiteralPart_TypedElement = Generalization(general=TypedElement, specific=FlatQVT_TupleLiteralPart)
gen_FlatQVT_TupleType_Class = Generalization(general=Class_, specific=FlatQVT_TupleType)
gen_FlatQVT_TupleType_DataType = Generalization(general=DataType, specific=FlatQVT_TupleType)
gen_FlatQVT_Type_NamedElement = Generalization(general=NamedElement, specific=FlatQVT_Type)
gen_FlatQVT_TypeExp_OclExpression = Generalization(general=OclExpression, specific=FlatQVT_TypeExp)
gen_FlatQVT_TypedElement_NamedElement = Generalization(general=NamedElement, specific=FlatQVT_TypedElement)
gen_FlatQVT_TypedModel_NamedElement = Generalization(general=NamedElement, specific=FlatQVT_TypedModel)
gen_FlatQVT_Typedef_Class = Generalization(general=Class_, specific=FlatQVT_Typedef)
gen_FlatQVT_URIExtent_Extent = Generalization(general=Extent, specific=FlatQVT_URIExtent)
gen_FlatQVT_UnlimitedNaturalExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=FlatQVT_UnlimitedNaturalExp)
gen_FlatQVT_UnlinkExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_UnlinkExp)
gen_FlatQVT_VarParameter_Variable = Generalization(general=Variable, specific=FlatQVT_VarParameter)
gen_FlatQVT_VarParameter_Parameter = Generalization(general=Parameter_, specific=FlatQVT_VarParameter)
gen_FlatQVT_Variable_TypedElement = Generalization(general=TypedElement, specific=FlatQVT_Variable)
gen_FlatQVT_VariableExp_OclExpression = Generalization(general=OclExpression, specific=FlatQVT_VariableExp)
gen_FlatQVT_VariableInitExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_VariableInitExp)
gen_FlatQVT_VoidType_Type = Generalization(general=Type, specific=FlatQVT_VoidType)
gen_FlatQVT_WhileExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_WhileExp)
gen_FlatQVT_VariableAssignment_Assignment = Generalization(general=Assignment, specific=FlatQVT_VariableAssignment)

# Domain Model
domain_model = DomainModel(
    name="FlatQVT",
    types={FlatQVT_AltExp, ImperativeExpression, FlatQVT_AnyType, Type, FlatQVT_Area, FlatQVT_AssertExp, FlatQVT_AssignExp, FlatQVT_Assignment, Element, FlatQVT_BagType, CollectionType, FlatQVT_BlockExp, FlatQVT_BooleanLiteralExp, PrimitiveLiteralExp, FlatQVT_BottomPattern, CorePattern, FlatQVT_BreakExp, FlatQVT_CallExp, OclExpression, FlatQVT_CatchExp, FlatQVT_Class, FlatQVT_CollectionItem, CollectionLiteralPart, FlatQVT_CollectionLiteralExp, LiteralExp, FlatQVT_CollectionLiteralPart, TypedElement, FlatQVT_CollectionRange, FlatQVT_CollectionTemplateExp, TemplateExp, FlatQVT_CollectionType, DataType, FlatQVT_Comment, FlatQVT_ComputeExp, FlatQVT_Constructor, ImperativeOperation, FlatQVT_ConstructorBody, OperationBody, FlatQVT_ContextualProperty, Property_, FlatQVT_ContinueExp, FlatQVT_CoreDomain, Domain, Area, FlatQVT_CorePattern, Pattern, FlatQVT_DataType, FlatQVT_DictLiteralExp, FlatQVT_DictLiteralPart, FlatQVT_DictionaryType, FlatQVT_Domain, NamedElement, FlatQVT_DomainPattern, FlatQVT_Element, Object, FlatQVT_EnforcementOperation, FlatQVT_EntryOperation, FlatQVT_EnumLiteralExp, FlatQVT_Enumeration, FlatQVT_EnumerationLiteral, FlatQVT_ExpressionInOcl, FlatQVT_Extent, FlatQVT_Factory, FlatQVT_FeatureCallExp, CallExp, FlatQVT_ForExp, ImperativeLoopExp, FlatQVT_Function, Operation, FlatQVT_FunctionParameter, Variable, Parameter_, FlatQVT_GuardPattern, FlatQVT_Helper, FlatQVT_IfExp, FlatQVT_ImperativeCallExp, OperationCallExp, FlatQVT_ImperativeExpression, FlatQVT_ImperativeIterateExp, FlatQVT_ImperativeLoopExp, LoopExp, FlatQVT_ImperativeOperation, FlatQVT_InstantiationExp, FlatQVT_IntegerLiteralExp, NumericLiteralExp, FlatQVT_InvalidType, FlatQVT_IterateExp, FlatQVT_IteratorExp, FlatQVT_Key, FlatQVT_LetExp, FlatQVT_Library, Module, FlatQVT_ListLiteralExp, FlatQVT_ListType, FlatQVT_LiteralExp, FlatQVT_LogExp, FlatQVT_LoopExp, FlatQVT_Mapping, Rule, FlatQVT_MappingBody, FlatQVT_MappingCallExp, ImperativeCallExp, FlatQVT_InvalidLiteralExp, FlatQVT_MappingOperation, FlatQVT_MappingParameter, VarParameter, FlatQVT_ModelParameter, FlatQVT_ModelType, Class_, FlatQVT_Module, Package, FlatQVT_ModuleImport, FlatQVT_MultiplicityElement, FlatQVT_NamedElement, FlatQVT_NavigationCallExp, FeatureCallExp, FlatQVT_NullLiteralExp, FlatQVT_NumericLiteralExp, FlatQVT_Object, FlatQVT_ObjectExp, InstantiationExp, FlatQVT_ObjectTemplateExp, FlatQVT_OclExpression, FlatQVT_Operation, MultiplicityElement, FlatQVT_OperationBody, FlatQVT_OperationCallExp, FlatQVT_OperationalTransformation, FlatQVT_OppositePropertyCallExp, PropertyCallExp, FlatQVT_Package, FlatQVT_Parameter, FlatQVT_Pattern, FlatQVT_Predicate, FlatQVT_PrimitiveLiteralExp, FlatQVT_PrimitiveType, FlatQVT_Property, FlatQVT_PropertyAssignment, Assignment, FlatQVT_PropertyCallExp, NavigationCallExp, FlatQVT_PropertyTemplateItem, FlatQVT_RaiseExp, FlatQVT_RealLiteralExp, FlatQVT_OrderedSetType, FlatQVT_ReflectiveCollection, FlatQVT_ReflectiveSequence, ReflectiveCollection, FlatQVT_Relation, FlatQVT_RelationCallExp, FlatQVT_RelationDomain, FlatQVT_RelationDomainAssignment, FlatQVT_RelationImplementation, FlatQVT_RealizedVariable, FlatQVT_ResolveExp, FlatQVT_ResolveInExp, ResolveExp, FlatQVT_ReturnExp, FlatQVT_Rule, FlatQVT_SequenceType, FlatQVT_SetType, FlatQVT_StringLiteralExp, FlatQVT_SwitchExp, FlatQVT_Tag, FlatQVT_TemplateExp, FlatQVT_TemplateParameterType, FlatQVT_Transformation, FlatQVT_RelationalTransformation, Transformation, FlatQVT_TryExp, FlatQVT_TupleLiteralExp, FlatQVT_TupleLiteralPart, FlatQVT_TupleType, FlatQVT_Type, FlatQVT_TypeExp, FlatQVT_TypedElement, FlatQVT_TypedModel, FlatQVT_Typedef, FlatQVT_URIExtent, Extent, FlatQVT_UnlimitedNaturalExp, FlatQVT_UnlinkExp, FlatQVT_VarParameter, FlatQVT_Variable, FlatQVT_VariableExp, FlatQVT_VariableInitExp, FlatQVT_VoidType, FlatQVT_WhileExp, FlatQVT_VariableAssignment, CollectionKind, DirectionKind, EnforcementMode, ImportKind, SeverityKind},
    associations={},
    generalizations={gen_FlatQVT_AltExp_ImperativeExpression, gen_FlatQVT_AnyType_Type, gen_FlatQVT_AssertExp_ImperativeExpression, gen_FlatQVT_AssignExp_ImperativeExpression, gen_FlatQVT_Assignment_Element, gen_FlatQVT_BagType_CollectionType, gen_FlatQVT_BlockExp_ImperativeExpression, gen_FlatQVT_BooleanLiteralExp_PrimitiveLiteralExp, gen_FlatQVT_BottomPattern_CorePattern, gen_FlatQVT_BreakExp_ImperativeExpression, gen_FlatQVT_CallExp_OclExpression, gen_FlatQVT_CatchExp_ImperativeExpression, gen_FlatQVT_Class_Type, gen_FlatQVT_CollectionItem_CollectionLiteralPart, gen_FlatQVT_CollectionLiteralExp_LiteralExp, gen_FlatQVT_CollectionLiteralPart_TypedElement, gen_FlatQVT_CollectionRange_CollectionLiteralPart, gen_FlatQVT_CollectionTemplateExp_TemplateExp, gen_FlatQVT_CollectionType_DataType, gen_FlatQVT_Comment_Element, gen_FlatQVT_ComputeExp_ImperativeExpression, gen_FlatQVT_Constructor_ImperativeOperation, gen_FlatQVT_ConstructorBody_OperationBody, gen_FlatQVT_ContextualProperty_Property, gen_FlatQVT_ContinueExp_ImperativeExpression, gen_FlatQVT_CoreDomain_Domain, gen_FlatQVT_CoreDomain_Area, gen_FlatQVT_CorePattern_Pattern, gen_FlatQVT_DataType_Type, gen_FlatQVT_DictLiteralExp_LiteralExp, gen_FlatQVT_DictLiteralPart_Element, gen_FlatQVT_DictionaryType_CollectionType, gen_FlatQVT_Domain_NamedElement, gen_FlatQVT_DomainPattern_Pattern, gen_FlatQVT_EnforcementOperation_Element, gen_FlatQVT_EntryOperation_ImperativeOperation, gen_FlatQVT_EnumLiteralExp_LiteralExp, gen_FlatQVT_Enumeration_DataType, gen_FlatQVT_EnumerationLiteral_NamedElement, gen_FlatQVT_ExpressionInOcl_TypedElement, gen_FlatQVT_Extent_Object, gen_FlatQVT_Factory_Element, gen_FlatQVT_Element_Object, gen_FlatQVT_FeatureCallExp_CallExp, gen_FlatQVT_ForExp_ImperativeLoopExp, gen_FlatQVT_Function_Operation, gen_FlatQVT_FunctionParameter_Variable, gen_FlatQVT_FunctionParameter_Parameter, gen_FlatQVT_GuardPattern_CorePattern, gen_FlatQVT_Helper_ImperativeOperation, gen_FlatQVT_IfExp_OclExpression, gen_FlatQVT_ImperativeCallExp_OperationCallExp, gen_FlatQVT_ImperativeCallExp_ImperativeExpression, gen_FlatQVT_ImperativeExpression_OclExpression, gen_FlatQVT_ImperativeIterateExp_ImperativeLoopExp, gen_FlatQVT_ImperativeLoopExp_LoopExp, gen_FlatQVT_ImperativeLoopExp_ImperativeExpression, gen_FlatQVT_ImperativeOperation_Operation, gen_FlatQVT_InstantiationExp_ImperativeExpression, gen_FlatQVT_IntegerLiteralExp_NumericLiteralExp, gen_FlatQVT_InvalidType_Type, gen_FlatQVT_IterateExp_LoopExp, gen_FlatQVT_IteratorExp_LoopExp, gen_FlatQVT_Key_Element, gen_FlatQVT_LetExp_OclExpression, gen_FlatQVT_Library_Module, gen_FlatQVT_ListLiteralExp_LiteralExp, gen_FlatQVT_ListType_CollectionType, gen_FlatQVT_LiteralExp_OclExpression, gen_FlatQVT_LogExp_OperationCallExp, gen_FlatQVT_LogExp_ImperativeExpression, gen_FlatQVT_LoopExp_CallExp, gen_FlatQVT_LoopExp_OclExpression, gen_FlatQVT_Mapping_Rule, gen_FlatQVT_Mapping_Area, gen_FlatQVT_MappingBody_OperationBody, gen_FlatQVT_InvalidLiteralExp_LiteralExp, gen_FlatQVT_MappingOperation_ImperativeOperation, gen_FlatQVT_MappingParameter_VarParameter, gen_FlatQVT_ModelParameter_VarParameter, gen_FlatQVT_ModelType_Class, gen_FlatQVT_Module_Class, gen_FlatQVT_Module_Package, gen_FlatQVT_ModuleImport_Element, gen_FlatQVT_MappingCallExp_ImperativeCallExp, gen_FlatQVT_NamedElement_Element, gen_FlatQVT_NavigationCallExp_FeatureCallExp, gen_FlatQVT_NullLiteralExp_LiteralExp, gen_FlatQVT_NumericLiteralExp_PrimitiveLiteralExp, gen_FlatQVT_ObjectExp_InstantiationExp, gen_FlatQVT_ObjectTemplateExp_TemplateExp, gen_FlatQVT_OclExpression_TypedElement, gen_FlatQVT_Operation_TypedElement, gen_FlatQVT_Operation_MultiplicityElement, gen_FlatQVT_OperationBody_Element, gen_FlatQVT_OperationCallExp_FeatureCallExp, gen_FlatQVT_OperationalTransformation_Module, gen_FlatQVT_OppositePropertyCallExp_PropertyCallExp, gen_FlatQVT_Package_NamedElement, gen_FlatQVT_Parameter_TypedElement, gen_FlatQVT_Parameter_MultiplicityElement, gen_FlatQVT_Pattern_Element, gen_FlatQVT_Predicate_Element, gen_FlatQVT_PrimitiveLiteralExp_LiteralExp, gen_FlatQVT_PrimitiveType_DataType, gen_FlatQVT_Property_TypedElement, gen_FlatQVT_Property_MultiplicityElement, gen_FlatQVT_PropertyAssignment_Assignment, gen_FlatQVT_PropertyCallExp_NavigationCallExp, gen_FlatQVT_PropertyTemplateItem_Element, gen_FlatQVT_RaiseExp_ImperativeExpression, gen_FlatQVT_RealLiteralExp_NumericLiteralExp, gen_FlatQVT_OrderedSetType_CollectionType, gen_FlatQVT_RealizedVariable_Variable, gen_FlatQVT_ReflectiveCollection_Object, gen_FlatQVT_ReflectiveSequence_ReflectiveCollection, gen_FlatQVT_Relation_Rule, gen_FlatQVT_RelationCallExp_OclExpression, gen_FlatQVT_RelationDomain_Domain, gen_FlatQVT_RelationDomainAssignment_Element, gen_FlatQVT_RelationImplementation_Element, gen_FlatQVT_ResolveExp_CallExp, gen_FlatQVT_ResolveExp_ImperativeExpression, gen_FlatQVT_ResolveInExp_ResolveExp, gen_FlatQVT_ReturnExp_ImperativeExpression, gen_FlatQVT_Rule_NamedElement, gen_FlatQVT_SequenceType_CollectionType, gen_FlatQVT_SetType_CollectionType, gen_FlatQVT_StringLiteralExp_PrimitiveLiteralExp, gen_FlatQVT_SwitchExp_ImperativeExpression, gen_FlatQVT_Tag_Element, gen_FlatQVT_TemplateExp_LiteralExp, gen_FlatQVT_TemplateParameterType_Type, gen_FlatQVT_Transformation_Class, gen_FlatQVT_Transformation_Package, gen_FlatQVT_RelationalTransformation_Transformation, gen_FlatQVT_TryExp_ImperativeExpression, gen_FlatQVT_TupleLiteralExp_LiteralExp, gen_FlatQVT_TupleLiteralPart_TypedElement, gen_FlatQVT_TupleType_Class, gen_FlatQVT_TupleType_DataType, gen_FlatQVT_Type_NamedElement, gen_FlatQVT_TypeExp_OclExpression, gen_FlatQVT_TypedElement_NamedElement, gen_FlatQVT_TypedModel_NamedElement, gen_FlatQVT_Typedef_Class, gen_FlatQVT_URIExtent_Extent, gen_FlatQVT_UnlimitedNaturalExp_NumericLiteralExp, gen_FlatQVT_UnlinkExp_ImperativeExpression, gen_FlatQVT_VarParameter_Variable, gen_FlatQVT_VarParameter_Parameter, gen_FlatQVT_Variable_TypedElement, gen_FlatQVT_VariableExp_OclExpression, gen_FlatQVT_VariableInitExp_ImperativeExpression, gen_FlatQVT_VoidType_Type, gen_FlatQVT_WhileExp_ImperativeExpression, gen_FlatQVT_VariableAssignment_Assignment},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)