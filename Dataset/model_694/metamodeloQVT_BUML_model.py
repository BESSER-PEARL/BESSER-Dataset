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
            EnumerationLiteral(name="in_"),
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
Comment = Class(name="Comment")
EMOF_Class = Class(name="EMOF_Class")
Type = Class(name="Type")
Property_ = Class(name="Property")
Operation = Class(name="Operation")
Class_ = Class(name="Class")
EMOF_Comment = Class(name="EMOF_Comment")
Element = Class(name="Element")
NamedElement = Class(name="NamedElement")
EMOF_DataType = Class(name="EMOF_DataType")
EMOF_Element = Class(name="EMOF_Element", is_abstract=True)
Object = Class(name="Object")
Parameter_ = Class(name="Parameter")
EMOF_Package = Class(name="EMOF_Package")
EMOF_Enumeration = Class(name="EMOF_Enumeration")
DataType = Class(name="DataType")
EnumerationLiteral = Class(name="EnumerationLiteral")
EMOF_EnumerationLiteral = Class(name="EMOF_EnumerationLiteral")
Enumeration_ = Class(name="Enumeration")
EMOF_Extent = Class(name="EMOF_Extent")
EMOF_Factory = Class(name="EMOF_Factory")
Package = Class(name="Package")
EMOF_MultiplicityElement = Class(name="EMOF_MultiplicityElement", is_abstract=True)
EMOF_NamedElement = Class(name="EMOF_NamedElement", is_abstract=True)
EMOF_Object = Class(name="EMOF_Object")
EMOF_Operation = Class(name="EMOF_Operation")
TypedElement = Class(name="TypedElement")
MultiplicityElement = Class(name="MultiplicityElement")
EMOF_Tag = Class(name="EMOF_Tag")
EMOF_Type = Class(name="EMOF_Type", is_abstract=True)
EMOF_TypedElement = Class(name="EMOF_TypedElement", is_abstract=True)
EMOF_Parameter = Class(name="EMOF_Parameter")
EMOF_PrimitiveType = Class(name="EMOF_PrimitiveType")
EMOF_Property = Class(name="EMOF_Property")
EMOF_ReflectiveCollection = Class(name="EMOF_ReflectiveCollection")
EMOF_ReflectiveSequence = Class(name="EMOF_ReflectiveSequence")
ReflectiveCollection = Class(name="ReflectiveCollection")
EssentialOCL_CollectionLiteralPart = Class(name="EssentialOCL_CollectionLiteralPart", is_abstract=True)
CollectionLiteralExp = Class(name="CollectionLiteralExp")
EssentialOCL_CollectionRange = Class(name="EssentialOCL_CollectionRange")
EMOF_URIExtent = Class(name="EMOF_URIExtent")
Extent = Class(name="Extent")
EssentialOCL_AnyType = Class(name="EssentialOCL_AnyType")
EssentialOCL_BagType = Class(name="EssentialOCL_BagType")
CollectionType = Class(name="CollectionType")
EssentialOCL_BooleanLiteralExp = Class(name="EssentialOCL_BooleanLiteralExp")
PrimitiveLiteralExp = Class(name="PrimitiveLiteralExp")
EssentialOCL_CallExp = Class(name="EssentialOCL_CallExp", is_abstract=True)
OclExpression = Class(name="OclExpression")
EssentialOCL_CollectionItem = Class(name="EssentialOCL_CollectionItem")
CollectionLiteralPart = Class(name="CollectionLiteralPart")
EssentialOCL_CollectionLiteralExp = Class(name="EssentialOCL_CollectionLiteralExp")
LiteralExp = Class(name="LiteralExp")
EssentialOCL_FeatureCallExp = Class(name="EssentialOCL_FeatureCallExp", is_abstract=True)
CallExp = Class(name="CallExp")
EssentialOCL_IfExp = Class(name="EssentialOCL_IfExp")
EssentialOCL_CollectionType = Class(name="EssentialOCL_CollectionType")
EssentialOCL_EnumLiteralExp = Class(name="EssentialOCL_EnumLiteralExp")
EssentialOCL_ExpressionInOcl = Class(name="EssentialOCL_ExpressionInOcl")
Variable = Class(name="Variable")
EssentialOCL_NavigationCallExp = Class(name="EssentialOCL_NavigationCallExp")
FeatureCallExp = Class(name="FeatureCallExp")
EssentialOCL_NullLiteralExp = Class(name="EssentialOCL_NullLiteralExp")
EssentialOCL_NumericLiteralExp = Class(name="EssentialOCL_NumericLiteralExp", is_abstract=True)
EssentialOCL_OclExpression = Class(name="EssentialOCL_OclExpression", is_abstract=True)
EssentialOCL_OperationCallExp = Class(name="EssentialOCL_OperationCallExp")
EssentialOCL_IntegerLiteralExp = Class(name="EssentialOCL_IntegerLiteralExp")
NumericLiteralExp = Class(name="NumericLiteralExp")
EssentialOCL_InvalidLiteralExp = Class(name="EssentialOCL_InvalidLiteralExp")
EssentialOCL_InvalidType = Class(name="EssentialOCL_InvalidType")
EssentialOCL_IterateExp = Class(name="EssentialOCL_IterateExp")
LoopExp = Class(name="LoopExp")
EssentialOCL_IteratorExp = Class(name="EssentialOCL_IteratorExp")
EssentialOCL_LetExp = Class(name="EssentialOCL_LetExp")
EssentialOCL_LiteralExp = Class(name="EssentialOCL_LiteralExp", is_abstract=True)
EssentialOCL_LoopExp = Class(name="EssentialOCL_LoopExp", is_abstract=True)
EssentialOCL_TupleLiteralPart = Class(name="EssentialOCL_TupleLiteralPart")
TupleLiteralExp = Class(name="TupleLiteralExp")
EssentialOCL_TupleType = Class(name="EssentialOCL_TupleType")
EssentialOCL_OrderedSetType = Class(name="EssentialOCL_OrderedSetType")
EssentialOCL_PrimitiveLiteralExp = Class(name="EssentialOCL_PrimitiveLiteralExp", is_abstract=True)
EssentialOCL_PropertyCallExp = Class(name="EssentialOCL_PropertyCallExp")
NavigationCallExp = Class(name="NavigationCallExp")
EssentialOCL_RealLiteralExp = Class(name="EssentialOCL_RealLiteralExp")
EssentialOCL_SequenceType = Class(name="EssentialOCL_SequenceType")
EssentialOCL_SetType = Class(name="EssentialOCL_SetType")
EssentialOCL_StringLiteralExp = Class(name="EssentialOCL_StringLiteralExp")
EssentialOCL_TemplateParameterType = Class(name="EssentialOCL_TemplateParameterType")
EssentialOCL_TupleLiteralExp = Class(name="EssentialOCL_TupleLiteralExp")
TupleLiteralPart = Class(name="TupleLiteralPart")
Rule = Class(name="Rule")
TypedModel = Class(name="TypedModel")
QVTBase_Function = Class(name="QVTBase_Function")
QVTBase_FunctionParameter = Class(name="QVTBase_FunctionParameter")
EssentialOCL_TypeExp = Class(name="EssentialOCL_TypeExp")
EssentialOCL_UnlimitedNaturalExp = Class(name="EssentialOCL_UnlimitedNaturalExp")
EssentialOCL_Variable = Class(name="EssentialOCL_Variable")
LetExp = Class(name="LetExp")
EssentialOCL_VariableExp = Class(name="EssentialOCL_VariableExp")
EssentialOCL_VoidType = Class(name="EssentialOCL_VoidType")
QVTBase_Domain = Class(name="QVTBase_Domain", is_abstract=True)
Tag = Class(name="Tag")
QVTBase_TypedModel = Class(name="QVTBase_TypedModel")
QVTBase_Pattern = Class(name="QVTBase_Pattern")
Predicate = Class(name="Predicate")
QVTBase_Predicate = Class(name="QVTBase_Predicate")
Pattern = Class(name="Pattern")
QVTBase_Rule = Class(name="QVTBase_Rule", is_abstract=True)
Domain = Class(name="Domain")
Transformation = Class(name="Transformation")
QVTBase_Transformation = Class(name="QVTBase_Transformation")
QVTCore_BottomPattern = Class(name="QVTCore_BottomPattern")
CorePattern = Class(name="CorePattern")
Area = Class(name="Area")
Assignment = Class(name="Assignment")
EnforcementOperation = Class(name="EnforcementOperation")
QVTCore_Area = Class(name="QVTCore_Area", is_abstract=True)
BottomPattern = Class(name="BottomPattern")
GuardPattern = Class(name="GuardPattern")
QVTCore_Assignment = Class(name="QVTCore_Assignment", is_abstract=True)
Mapping = Class(name="Mapping")
QVTCore_PropertyAssignment = Class(name="QVTCore_PropertyAssignment")
RealizedVariable = Class(name="RealizedVariable")
QVTCore_CoreDomain = Class(name="QVTCore_CoreDomain")
QVTCore_CorePattern = Class(name="QVTCore_CorePattern")
QVTCore_EnforcementOperation = Class(name="QVTCore_EnforcementOperation")
OperationCallExp = Class(name="OperationCallExp")
QVTCore_GuardPattern = Class(name="QVTCore_GuardPattern")
QVTCore_Mapping = Class(name="QVTCore_Mapping")
QVTTemplate_ObjectTemplateExp = Class(name="QVTTemplate_ObjectTemplateExp")
PropertyTemplateItem = Class(name="PropertyTemplateItem")
QVTTemplate_PropertyTemplateItem = Class(name="QVTTemplate_PropertyTemplateItem")
ObjectTemplateExp = Class(name="ObjectTemplateExp")
QVTCore_RealizedVariable = Class(name="QVTCore_RealizedVariable")
QVTCore_VariableAssignment = Class(name="QVTCore_VariableAssignment")
QVTTemplate_CollectionTemplateExp = Class(name="QVTTemplate_CollectionTemplateExp")
TemplateExp = Class(name="TemplateExp")
RelationalTransformation = Class(name="RelationalTransformation")
QVTRelation_OppositePropertyCallExp = Class(name="QVTRelation_OppositePropertyCallExp")
PropertyCallExp = Class(name="PropertyCallExp")
QVTRelation_Relation = Class(name="QVTRelation_Relation")
QVTTemplate_TemplateExp = Class(name="QVTTemplate_TemplateExp", is_abstract=True)
QVTRelation_DomainPattern = Class(name="QVTRelation_DomainPattern")
RelationDomain = Class(name="RelationDomain")
QVTRelation_Key = Class(name="QVTRelation_Key")
QVTRelation_RelationDomainAssignment = Class(name="QVTRelation_RelationDomainAssignment")
QVTRelation_RelationImplementation = Class(name="QVTRelation_RelationImplementation")
RelationImplementation = Class(name="RelationImplementation")
QVTRelation_RelationCallExp = Class(name="QVTRelation_RelationCallExp")
Relation = Class(name="Relation")
QVTRelation_RelationDomain = Class(name="QVTRelation_RelationDomain")
RelationDomainAssignment = Class(name="RelationDomainAssignment")
DomainPattern = Class(name="DomainPattern")
ImperativeOCL_AssignExp = Class(name="ImperativeOCL_AssignExp")
QVTRelation_RelationalTransformation = Class(name="QVTRelation_RelationalTransformation")
Key = Class(name="Key")
ImperativeOCL_AltExp = Class(name="ImperativeOCL_AltExp")
ImperativeExpression = Class(name="ImperativeExpression")
ImperativeOCL_AssertExp = Class(name="ImperativeOCL_AssertExp")
LogExp = Class(name="LogExp")
ImperativeOCL_ContinueExp = Class(name="ImperativeOCL_ContinueExp")
ImperativeOCL_DictLiteralExp = Class(name="ImperativeOCL_DictLiteralExp")
DictLiteralPart = Class(name="DictLiteralPart")
ImperativeOCL_DictLiteralPart = Class(name="ImperativeOCL_DictLiteralPart")
ImperativeOCL_BlockExp = Class(name="ImperativeOCL_BlockExp")
ImperativeOCL_BreakExp = Class(name="ImperativeOCL_BreakExp")
ImperativeOCL_CatchExp = Class(name="ImperativeOCL_CatchExp")
ImperativeOCL_ComputeExp = Class(name="ImperativeOCL_ComputeExp")
DictLiteralExp = Class(name="DictLiteralExp")
ImperativeOCL_DictionaryType = Class(name="ImperativeOCL_DictionaryType")
ImperativeOCL_ForExp = Class(name="ImperativeOCL_ForExp")
ImperativeLoopExp = Class(name="ImperativeLoopExp")
ImperativeOCL_ImperativeExpression = Class(name="ImperativeOCL_ImperativeExpression", is_abstract=True)
ImperativeOCL_ImperativeIterateExp = Class(name="ImperativeOCL_ImperativeIterateExp")
ImperativeOCL_ImperativeLoopExp = Class(name="ImperativeOCL_ImperativeLoopExp", is_abstract=True)
ImperativeOCL_InstantiationExp = Class(name="ImperativeOCL_InstantiationExp")
ImperativeOCL_SwitchExp = Class(name="ImperativeOCL_SwitchExp")
AltExp = Class(name="AltExp")
ImperativeOCL_ListLiteralExp = Class(name="ImperativeOCL_ListLiteralExp")
ImperativeOCL_ListType = Class(name="ImperativeOCL_ListType")
ImperativeOCL_LogExp = Class(name="ImperativeOCL_LogExp")
ImperativeOCL_RaiseExp = Class(name="ImperativeOCL_RaiseExp")
ImperativeOCL_ReturnExp = Class(name="ImperativeOCL_ReturnExp")
ImperativeOCL_VariableInitExp = Class(name="ImperativeOCL_VariableInitExp")
ImperativeOCL_WhileExp = Class(name="ImperativeOCL_WhileExp")
ImperativeOCL_TryExp = Class(name="ImperativeOCL_TryExp")
CatchExp = Class(name="CatchExp")
ImperativeOCL_Typedef = Class(name="ImperativeOCL_Typedef")
ImperativeOCL_UnlinkExp = Class(name="ImperativeOCL_UnlinkExp")
QVTOperational_EntryOperation = Class(name="QVTOperational_EntryOperation")
QVTOperational_Helper = Class(name="QVTOperational_Helper")
QVTOperational_ImperativeCallExp = Class(name="QVTOperational_ImperativeCallExp")
QVTOperational_Constructor = Class(name="QVTOperational_Constructor")
ImperativeOperation = Class(name="ImperativeOperation")
QVTOperational_ConstructorBody = Class(name="QVTOperational_ConstructorBody")
OperationBody = Class(name="OperationBody")
QVTOperational_ContextualProperty = Class(name="QVTOperational_ContextualProperty")
QVTOperational_MappingCallExp = Class(name="QVTOperational_MappingCallExp")
ImperativeCallExp = Class(name="ImperativeCallExp")
QVTOperational_MappingOperation = Class(name="QVTOperational_MappingOperation")
MappingOperation = Class(name="MappingOperation")
QVTOperational_ImperativeOperation = Class(name="QVTOperational_ImperativeOperation")
VarParameter = Class(name="VarParameter")
QVTOperational_Library = Class(name="QVTOperational_Library")
Module = Class(name="Module")
QVTOperational_MappingBody = Class(name="QVTOperational_MappingBody")
QVTOperational_MappingParameter = Class(name="QVTOperational_MappingParameter")
ModelParameter = Class(name="ModelParameter")
QVTOperational_ModelParameter = Class(name="QVTOperational_ModelParameter")
OperationalTransformation = Class(name="OperationalTransformation")
QVTOperational_ModelType = Class(name="QVTOperational_ModelType")
ModelType = Class(name="ModelType")
QVTOperational_ModuleImport = Class(name="QVTOperational_ModuleImport")
QVTOperational_Module = Class(name="QVTOperational_Module")
EntryOperation = Class(name="EntryOperation")
ModuleImport = Class(name="ModuleImport")
QVTOperational_OperationalTransformation = Class(name="QVTOperational_OperationalTransformation")
QVTOperational_ObjectExp = Class(name="QVTOperational_ObjectExp")
InstantiationExp = Class(name="InstantiationExp")
ConstructorBody = Class(name="ConstructorBody")
QVTOperational_OperationBody = Class(name="QVTOperational_OperationBody")
QVTOperational_ResolveInExp = Class(name="QVTOperational_ResolveInExp")
ResolveExp = Class(name="ResolveExp")
QVTOperational_VarParameter = Class(name="QVTOperational_VarParameter")
QVTOperational_ResolveExp = Class(name="QVTOperational_ResolveExp")

# Comment class attributes and methods

# EMOF_Class class attributes and methods
EMOF_Class_isAbstract: Property = Property(name="isAbstract", type=StringType)
EMOF_Class.attributes={EMOF_Class_isAbstract}

# Type class attributes and methods

# Property class attributes and methods

# Operation class attributes and methods

# Class class attributes and methods

# EMOF_Comment class attributes and methods
EMOF_Comment_body: Property = Property(name="body", type=StringType)
EMOF_Comment.attributes={EMOF_Comment_body}

# Element class attributes and methods

# NamedElement class attributes and methods

# EMOF_DataType class attributes and methods

# EMOF_Element class attributes and methods
EMOF_Element_m_container: Method = Method(name="container", parameters={}, type=StringType)
EMOF_Element_m_equals: Method = Method(name="equals", parameters={Parameter(name='EMOF_object', type=StringType)}, type=StringType)
EMOF_Element_m_get: Method = Method(name="get", parameters={Parameter(name='EMOF_property', type=StringType)}, type=StringType)
EMOF_Element_m_getMetaClass: Method = Method(name="getMetaClass", parameters={}, type=StringType)
EMOF_Element_m_isSet: Method = Method(name="isSet", parameters={Parameter(name='EMOF_property', type=StringType)}, type=StringType)
EMOF_Element_m_set: Method = Method(name="set", parameters={Parameter(name='EMOF_object', type=StringType), Parameter(name='EMOF_property', type=StringType)})
EMOF_Element_m_unset: Method = Method(name="unset", parameters={Parameter(name='EMOF_property', type=StringType)})
EMOF_Element.methods={EMOF_Element_m_unset, EMOF_Element_m_isSet, EMOF_Element_m_getMetaClass, EMOF_Element_m_container, EMOF_Element_m_equals, EMOF_Element_m_set, EMOF_Element_m_get}

# Object class attributes and methods

# Parameter class attributes and methods

# EMOF_Package class attributes and methods
EMOF_Package_uri: Property = Property(name="uri", type=StringType)
EMOF_Package.attributes={EMOF_Package_uri}

# EMOF_Enumeration class attributes and methods

# DataType class attributes and methods

# EnumerationLiteral class attributes and methods

# EMOF_EnumerationLiteral class attributes and methods

# Enumeration class attributes and methods

# EMOF_Extent class attributes and methods
EMOF_Extent_m_elements: Method = Method(name="elements", parameters={}, type=StringType)
EMOF_Extent_m_useContainment: Method = Method(name="useContainment", parameters={}, type=StringType)
EMOF_Extent.methods={EMOF_Extent_m_useContainment, EMOF_Extent_m_elements}

# EMOF_Factory class attributes and methods
EMOF_Factory_m_convertToString: Method = Method(name="convertToString", parameters={Parameter(name='EMOF_dataType', type=StringType), Parameter(name='EMOF_object', type=StringType)}, type=StringType)
EMOF_Factory_m_create: Method = Method(name="create", parameters={Parameter(name='EMOF_metaClass', type=StringType)}, type=StringType)
EMOF_Factory_m_createFromString: Method = Method(name="createFromString", parameters={Parameter(name='EMOF_string', type=StringType), Parameter(name='EMOF_dataType', type=StringType)}, type=StringType)
EMOF_Factory.methods={EMOF_Factory_m_convertToString, EMOF_Factory_m_create, EMOF_Factory_m_createFromString}

# Package class attributes and methods

# EMOF_MultiplicityElement class attributes and methods
EMOF_MultiplicityElement_isOrdered: Property = Property(name="isOrdered", type=StringType)
EMOF_MultiplicityElement_isUnique: Property = Property(name="isUnique", type=StringType)
EMOF_MultiplicityElement_lower: Property = Property(name="lower", type=StringType)
EMOF_MultiplicityElement_upper: Property = Property(name="upper", type=StringType)
EMOF_MultiplicityElement.attributes={EMOF_MultiplicityElement_upper, EMOF_MultiplicityElement_lower, EMOF_MultiplicityElement_isUnique, EMOF_MultiplicityElement_isOrdered}

# EMOF_NamedElement class attributes and methods
EMOF_NamedElement_name: Property = Property(name="name", type=StringType)
EMOF_NamedElement.attributes={EMOF_NamedElement_name}

# EMOF_Object class attributes and methods

# EMOF_Operation class attributes and methods

# TypedElement class attributes and methods

# MultiplicityElement class attributes and methods

# EMOF_Tag class attributes and methods
EMOF_Tag_name: Property = Property(name="name", type=StringType)
EMOF_Tag_value: Property = Property(name="value", type=StringType)
EMOF_Tag.attributes={EMOF_Tag_value, EMOF_Tag_name}

# EMOF_Type class attributes and methods
EMOF_Type_m_isInstance: Method = Method(name="isInstance", parameters={Parameter(name='EMOF_object', type=StringType)}, type=StringType)
EMOF_Type.methods={EMOF_Type_m_isInstance}

# EMOF_TypedElement class attributes and methods

# EMOF_Parameter class attributes and methods

# EMOF_PrimitiveType class attributes and methods

# EMOF_Property class attributes and methods
EMOF_Property_default: Property = Property(name="default", type=StringType)
EMOF_Property_isComposite: Property = Property(name="isComposite", type=StringType)
EMOF_Property_isDerived: Property = Property(name="isDerived", type=StringType)
EMOF_Property_isID: Property = Property(name="isID", type=StringType)
EMOF_Property_isReadOnly: Property = Property(name="isReadOnly", type=StringType)
EMOF_Property.attributes={EMOF_Property_default, EMOF_Property_isReadOnly, EMOF_Property_isComposite, EMOF_Property_isDerived, EMOF_Property_isID}

# EMOF_ReflectiveCollection class attributes and methods
EMOF_ReflectiveCollection_m_add: Method = Method(name="add", parameters={Parameter(name='EMOF_object', type=StringType)}, type=StringType)
EMOF_ReflectiveCollection_m_addAll: Method = Method(name="addAll", parameters={Parameter(name='EMOF_objects', type=StringType)}, type=StringType)
EMOF_ReflectiveCollection_m_clear: Method = Method(name="clear", parameters={})
EMOF_ReflectiveCollection_m_remove: Method = Method(name="remove", parameters={Parameter(name='EMOF_object', type=StringType)}, type=StringType)
EMOF_ReflectiveCollection_m_size: Method = Method(name="size", parameters={}, type=StringType)
EMOF_ReflectiveCollection.methods={EMOF_ReflectiveCollection_m_addAll, EMOF_ReflectiveCollection_m_remove, EMOF_ReflectiveCollection_m_clear, EMOF_ReflectiveCollection_m_add, EMOF_ReflectiveCollection_m_size}

# EMOF_ReflectiveSequence class attributes and methods
EMOF_ReflectiveSequence_m_add: Method = Method(name="add", parameters={Parameter(name='EMOF_index', type=StringType), Parameter(name='EMOF_object', type=StringType)})
EMOF_ReflectiveSequence_m_get: Method = Method(name="get", parameters={Parameter(name='EMOF_index', type=StringType)}, type=StringType)
EMOF_ReflectiveSequence_m_remove: Method = Method(name="remove", parameters={Parameter(name='EMOF_index', type=StringType)}, type=StringType)
EMOF_ReflectiveSequence_m_set: Method = Method(name="set", parameters={Parameter(name='EMOF_index', type=StringType), Parameter(name='EMOF_object', type=StringType)}, type=StringType)
EMOF_ReflectiveSequence.methods={EMOF_ReflectiveSequence_m_get, EMOF_ReflectiveSequence_m_add, EMOF_ReflectiveSequence_m_remove, EMOF_ReflectiveSequence_m_set}

# ReflectiveCollection class attributes and methods

# EssentialOCL_CollectionLiteralPart class attributes and methods

# CollectionLiteralExp class attributes and methods

# EssentialOCL_CollectionRange class attributes and methods

# EMOF_URIExtent class attributes and methods
EMOF_URIExtent_m_contextURI: Method = Method(name="contextURI", parameters={}, type=StringType)
EMOF_URIExtent_m_element: Method = Method(name="element", parameters={Parameter(name='EMOF_uri', type=StringType)}, type=StringType)
EMOF_URIExtent_m_uri: Method = Method(name="uri", parameters={Parameter(name='EMOF_element', type=StringType)}, type=StringType)
EMOF_URIExtent.methods={EMOF_URIExtent_m_element, EMOF_URIExtent_m_uri, EMOF_URIExtent_m_contextURI}

# Extent class attributes and methods

# EssentialOCL_AnyType class attributes and methods

# EssentialOCL_BagType class attributes and methods

# CollectionType class attributes and methods

# EssentialOCL_BooleanLiteralExp class attributes and methods
EssentialOCL_BooleanLiteralExp_booleanSymbol: Property = Property(name="booleanSymbol", type=StringType)
EssentialOCL_BooleanLiteralExp.attributes={EssentialOCL_BooleanLiteralExp_booleanSymbol}

# PrimitiveLiteralExp class attributes and methods

# EssentialOCL_CallExp class attributes and methods

# OclExpression class attributes and methods

# EssentialOCL_CollectionItem class attributes and methods

# CollectionLiteralPart class attributes and methods

# EssentialOCL_CollectionLiteralExp class attributes and methods
EssentialOCL_CollectionLiteralExp_kind: Property = Property(name="kind", type=StringType)
EssentialOCL_CollectionLiteralExp.attributes={EssentialOCL_CollectionLiteralExp_kind}

# LiteralExp class attributes and methods

# EssentialOCL_FeatureCallExp class attributes and methods

# CallExp class attributes and methods

# EssentialOCL_IfExp class attributes and methods

# EssentialOCL_CollectionType class attributes and methods

# EssentialOCL_EnumLiteralExp class attributes and methods

# EssentialOCL_ExpressionInOcl class attributes and methods

# Variable class attributes and methods

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

# EssentialOCL_LoopExp class attributes and methods

# EssentialOCL_TupleLiteralPart class attributes and methods

# TupleLiteralExp class attributes and methods

# EssentialOCL_TupleType class attributes and methods

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

# Rule class attributes and methods

# TypedModel class attributes and methods

# QVTBase_Function class attributes and methods

# QVTBase_FunctionParameter class attributes and methods

# EssentialOCL_TypeExp class attributes and methods

# EssentialOCL_UnlimitedNaturalExp class attributes and methods
EssentialOCL_UnlimitedNaturalExp_symbol: Property = Property(name="symbol", type=StringType)
EssentialOCL_UnlimitedNaturalExp.attributes={EssentialOCL_UnlimitedNaturalExp_symbol}

# EssentialOCL_Variable class attributes and methods

# LetExp class attributes and methods

# EssentialOCL_VariableExp class attributes and methods

# EssentialOCL_VoidType class attributes and methods

# QVTBase_Domain class attributes and methods
QVTBase_Domain_isCheckable: Property = Property(name="isCheckable", type=StringType)
QVTBase_Domain_isEnforceable: Property = Property(name="isEnforceable", type=StringType)
QVTBase_Domain.attributes={QVTBase_Domain_isCheckable, QVTBase_Domain_isEnforceable}

# Tag class attributes and methods

# QVTBase_TypedModel class attributes and methods

# QVTBase_Pattern class attributes and methods

# Predicate class attributes and methods

# QVTBase_Predicate class attributes and methods

# Pattern class attributes and methods

# QVTBase_Rule class attributes and methods

# Domain class attributes and methods

# Transformation class attributes and methods

# QVTBase_Transformation class attributes and methods

# QVTCore_BottomPattern class attributes and methods

# CorePattern class attributes and methods

# Area class attributes and methods

# Assignment class attributes and methods

# EnforcementOperation class attributes and methods

# QVTCore_Area class attributes and methods

# BottomPattern class attributes and methods

# GuardPattern class attributes and methods

# QVTCore_Assignment class attributes and methods
QVTCore_Assignment_isDefault: Property = Property(name="isDefault", type=StringType)
QVTCore_Assignment.attributes={QVTCore_Assignment_isDefault}

# Mapping class attributes and methods

# QVTCore_PropertyAssignment class attributes and methods

# RealizedVariable class attributes and methods

# QVTCore_CoreDomain class attributes and methods

# QVTCore_CorePattern class attributes and methods

# QVTCore_EnforcementOperation class attributes and methods
QVTCore_EnforcementOperation_enforcementMode: Property = Property(name="enforcementMode", type=StringType)
QVTCore_EnforcementOperation.attributes={QVTCore_EnforcementOperation_enforcementMode}

# OperationCallExp class attributes and methods

# QVTCore_GuardPattern class attributes and methods

# QVTCore_Mapping class attributes and methods

# QVTTemplate_ObjectTemplateExp class attributes and methods

# PropertyTemplateItem class attributes and methods

# QVTTemplate_PropertyTemplateItem class attributes and methods
QVTTemplate_PropertyTemplateItem_isOpposite: Property = Property(name="isOpposite", type=StringType)
QVTTemplate_PropertyTemplateItem.attributes={QVTTemplate_PropertyTemplateItem_isOpposite}

# ObjectTemplateExp class attributes and methods

# QVTCore_RealizedVariable class attributes and methods

# QVTCore_VariableAssignment class attributes and methods

# QVTTemplate_CollectionTemplateExp class attributes and methods

# TemplateExp class attributes and methods

# RelationalTransformation class attributes and methods

# QVTRelation_OppositePropertyCallExp class attributes and methods

# PropertyCallExp class attributes and methods

# QVTRelation_Relation class attributes and methods
QVTRelation_Relation_isTopLevel: Property = Property(name="isTopLevel", type=StringType)
QVTRelation_Relation.attributes={QVTRelation_Relation_isTopLevel}

# QVTTemplate_TemplateExp class attributes and methods

# QVTRelation_DomainPattern class attributes and methods

# RelationDomain class attributes and methods

# QVTRelation_Key class attributes and methods

# QVTRelation_RelationDomainAssignment class attributes and methods

# QVTRelation_RelationImplementation class attributes and methods

# RelationImplementation class attributes and methods

# QVTRelation_RelationCallExp class attributes and methods

# Relation class attributes and methods

# QVTRelation_RelationDomain class attributes and methods

# RelationDomainAssignment class attributes and methods

# DomainPattern class attributes and methods

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

# LogExp class attributes and methods

# ImperativeOCL_ContinueExp class attributes and methods

# ImperativeOCL_DictLiteralExp class attributes and methods

# DictLiteralPart class attributes and methods

# ImperativeOCL_DictLiteralPart class attributes and methods

# ImperativeOCL_BlockExp class attributes and methods

# ImperativeOCL_BreakExp class attributes and methods

# ImperativeOCL_CatchExp class attributes and methods

# ImperativeOCL_ComputeExp class attributes and methods

# DictLiteralExp class attributes and methods

# ImperativeOCL_DictionaryType class attributes and methods

# ImperativeOCL_ForExp class attributes and methods

# ImperativeLoopExp class attributes and methods

# ImperativeOCL_ImperativeExpression class attributes and methods

# ImperativeOCL_ImperativeIterateExp class attributes and methods

# ImperativeOCL_ImperativeLoopExp class attributes and methods

# ImperativeOCL_InstantiationExp class attributes and methods

# ImperativeOCL_SwitchExp class attributes and methods

# AltExp class attributes and methods

# ImperativeOCL_ListLiteralExp class attributes and methods

# ImperativeOCL_ListType class attributes and methods

# ImperativeOCL_LogExp class attributes and methods

# ImperativeOCL_RaiseExp class attributes and methods

# ImperativeOCL_ReturnExp class attributes and methods

# ImperativeOCL_VariableInitExp class attributes and methods
ImperativeOCL_VariableInitExp_withResult: Property = Property(name="withResult", type=StringType)
ImperativeOCL_VariableInitExp.attributes={ImperativeOCL_VariableInitExp_withResult}

# ImperativeOCL_WhileExp class attributes and methods

# ImperativeOCL_TryExp class attributes and methods

# CatchExp class attributes and methods

# ImperativeOCL_Typedef class attributes and methods

# ImperativeOCL_UnlinkExp class attributes and methods

# QVTOperational_EntryOperation class attributes and methods

# QVTOperational_Helper class attributes and methods
QVTOperational_Helper_isQuery: Property = Property(name="isQuery", type=StringType)
QVTOperational_Helper.attributes={QVTOperational_Helper_isQuery}

# QVTOperational_ImperativeCallExp class attributes and methods
QVTOperational_ImperativeCallExp_isVirtual: Property = Property(name="isVirtual", type=StringType)
QVTOperational_ImperativeCallExp.attributes={QVTOperational_ImperativeCallExp_isVirtual}

# QVTOperational_Constructor class attributes and methods

# ImperativeOperation class attributes and methods

# QVTOperational_ConstructorBody class attributes and methods

# OperationBody class attributes and methods

# QVTOperational_ContextualProperty class attributes and methods

# QVTOperational_MappingCallExp class attributes and methods
QVTOperational_MappingCallExp_isStrict: Property = Property(name="isStrict", type=StringType)
QVTOperational_MappingCallExp.attributes={QVTOperational_MappingCallExp_isStrict}

# ImperativeCallExp class attributes and methods

# QVTOperational_MappingOperation class attributes and methods

# MappingOperation class attributes and methods

# QVTOperational_ImperativeOperation class attributes and methods
QVTOperational_ImperativeOperation_isBlackbox: Property = Property(name="isBlackbox", type=StringType)
QVTOperational_ImperativeOperation.attributes={QVTOperational_ImperativeOperation_isBlackbox}

# VarParameter class attributes and methods

# QVTOperational_Library class attributes and methods

# Module class attributes and methods

# QVTOperational_MappingBody class attributes and methods

# QVTOperational_MappingParameter class attributes and methods

# ModelParameter class attributes and methods

# QVTOperational_ModelParameter class attributes and methods

# OperationalTransformation class attributes and methods

# QVTOperational_ModelType class attributes and methods
QVTOperational_ModelType_conformanceKind: Property = Property(name="conformanceKind", type=StringType)
QVTOperational_ModelType.attributes={QVTOperational_ModelType_conformanceKind}

# ModelType class attributes and methods

# QVTOperational_ModuleImport class attributes and methods
QVTOperational_ModuleImport_kind: Property = Property(name="kind", type=StringType)
QVTOperational_ModuleImport.attributes={QVTOperational_ModuleImport_kind}

# QVTOperational_Module class attributes and methods
QVTOperational_Module_isBlackbox: Property = Property(name="isBlackbox", type=StringType)
QVTOperational_Module.attributes={QVTOperational_Module_isBlackbox}

# EntryOperation class attributes and methods

# ModuleImport class attributes and methods

# QVTOperational_OperationalTransformation class attributes and methods

# QVTOperational_ObjectExp class attributes and methods

# InstantiationExp class attributes and methods

# ConstructorBody class attributes and methods

# QVTOperational_OperationBody class attributes and methods

# QVTOperational_ResolveInExp class attributes and methods

# ResolveExp class attributes and methods

# QVTOperational_VarParameter class attributes and methods
QVTOperational_VarParameter_kind: Property = Property(name="kind", type=StringType)
QVTOperational_VarParameter.attributes={QVTOperational_VarParameter_kind}

# QVTOperational_ResolveExp class attributes and methods
QVTOperational_ResolveExp_isDeferred: Property = Property(name="isDeferred", type=StringType)
QVTOperational_ResolveExp_isInverse: Property = Property(name="isInverse", type=StringType)
QVTOperational_ResolveExp_one: Property = Property(name="one", type=StringType)
QVTOperational_ResolveExp.attributes={QVTOperational_ResolveExp_isInverse, QVTOperational_ResolveExp_one, QVTOperational_ResolveExp_isDeferred}

# Relationships
ownedComment5: BinaryAssociation = BinaryAssociation(
    name="ownedComment5",
    ends={
        Property(name="Comment", type=EMOF_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Element", type=Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute0: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute0",
    ends={
        Property(name="Property", type=EMOF_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class_", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation1: BinaryAssociation = BinaryAssociation(
    name="ownedOperation1",
    ends={
        Property(name="Operation", type=EMOF_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class_2", type=Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass3: BinaryAssociation = BinaryAssociation(
    name="superClass3",
    ends={
        Property(name="Class", type=EMOF_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Class", type=Class_, multiplicity=Multiplicity(0, 9999))
    }
)
annotatedElement4: BinaryAssociation = BinaryAssociation(
    name="annotatedElement4",
    ends={
        Property(name="NamedElement", type=EMOF_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Comment", type=NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
class_9: BinaryAssociation = BinaryAssociation(
    name="class_9",
    ends={
        Property(name="Class10", type=EMOF_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedOperation", type=Class_, multiplicity=Multiplicity(0, 1))
    }
)
ownedParameter11: BinaryAssociation = BinaryAssociation(
    name="ownedParameter11",
    ends={
        Property(name="Parameter", type=EMOF_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
raisedException12: BinaryAssociation = BinaryAssociation(
    name="raisedException12",
    ends={
        Property(name="Type", type=EMOF_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Operation", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
nestedPackage13: BinaryAssociation = BinaryAssociation(
    name="nestedPackage13",
    ends={
        Property(name="Package14", type=EMOF_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="nestingPackage", type=Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestingPackage15: BinaryAssociation = BinaryAssociation(
    name="nestingPackage15",
    ends={
        Property(name="Package16", type=EMOF_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="nestedPackage", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
ownedLiteral6: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral6",
    ends={
        Property(name="EnumerationLiteral", type=EMOF_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="enumeration", type=EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumeration7: BinaryAssociation = BinaryAssociation(
    name="enumeration7",
    ends={
        Property(name="Enumeration", type=EMOF_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedLiteral", type=Enumeration_, multiplicity=Multiplicity(0, 1))
    }
)
package8: BinaryAssociation = BinaryAssociation(
    name="package8",
    ends={
        Property(name="Package", type=EMOF_Factory, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Factory", type=Package, multiplicity=Multiplicity(1, 1))
    }
)
element25: BinaryAssociation = BinaryAssociation(
    name="element25",
    ends={
        Property(name="Element", type=EMOF_Tag, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Tag", type=Element, multiplicity=Multiplicity(0, 9999))
    }
)
package26: BinaryAssociation = BinaryAssociation(
    name="package26",
    ends={
        Property(name="Package27", type=EMOF_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedType", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
type28: BinaryAssociation = BinaryAssociation(
    name="type28",
    ends={
        Property(name="Type29", type=EMOF_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_TypedElement", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
ownedType17: BinaryAssociation = BinaryAssociation(
    name="ownedType17",
    ends={
        Property(name="Type18", type=EMOF_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operation19: BinaryAssociation = BinaryAssociation(
    name="operation19",
    ends={
        Property(name="Operation20", type=EMOF_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedParameter", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
class_21: BinaryAssociation = BinaryAssociation(
    name="class_21",
    ends={
        Property(name="Class22", type=EMOF_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedAttribute", type=Class_, multiplicity=Multiplicity(0, 1))
    }
)
opposite23: BinaryAssociation = BinaryAssociation(
    name="opposite23",
    ends={
        Property(name="Property24", type=EMOF_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Property", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
part33: BinaryAssociation = BinaryAssociation(
    name="part33",
    ends={
        Property(name="CollectionLiteralPart", type=EssentialOCL_CollectionLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="collectionLiteralExp", type=CollectionLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collectionLiteralExp34: BinaryAssociation = BinaryAssociation(
    name="collectionLiteralExp34",
    ends={
        Property(name="CollectionLiteralExp", type=EssentialOCL_CollectionLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="part", type=CollectionLiteralExp, multiplicity=Multiplicity(1, 1))
    }
)
first35: BinaryAssociation = BinaryAssociation(
    name="first35",
    ends={
        Property(name="OclExpression36", type=EssentialOCL_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_CollectionRange", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source30: BinaryAssociation = BinaryAssociation(
    name="source30",
    ends={
        Property(name="OclExpression", type=EssentialOCL_CallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_CallExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
item31: BinaryAssociation = BinaryAssociation(
    name="item31",
    ends={
        Property(name="OclExpression32", type=EssentialOCL_CollectionItem, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_CollectionItem", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
resultVariable54: BinaryAssociation = BinaryAssociation(
    name="resultVariable54",
    ends={
        Property(name="Variable56", type=EssentialOCL_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_ExpressionInOcl55", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition57: BinaryAssociation = BinaryAssociation(
    name="condition57",
    ends={
        Property(name="OclExpression58", type=EssentialOCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_IfExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression59: BinaryAssociation = BinaryAssociation(
    name="elseExpression59",
    ends={
        Property(name="OclExpression61", type=EssentialOCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_IfExp60", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression62: BinaryAssociation = BinaryAssociation(
    name="thenExpression62",
    ends={
        Property(name="OclExpression64", type=EssentialOCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_IfExp63", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
last37: BinaryAssociation = BinaryAssociation(
    name="last37",
    ends={
        Property(name="OclExpression39", type=EssentialOCL_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_CollectionRange38", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementType40: BinaryAssociation = BinaryAssociation(
    name="elementType40",
    ends={
        Property(name="Type41", type=EssentialOCL_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_CollectionType", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
referredEnumLiteral42: BinaryAssociation = BinaryAssociation(
    name="referredEnumLiteral42",
    ends={
        Property(name="EnumerationLiteral43", type=EssentialOCL_EnumLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_EnumLiteralExp", type=EnumerationLiteral, multiplicity=Multiplicity(0, 1))
    }
)
bodyExpression44: BinaryAssociation = BinaryAssociation(
    name="bodyExpression44",
    ends={
        Property(name="OclExpression45", type=EssentialOCL_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_ExpressionInOcl", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
contextVariable46: BinaryAssociation = BinaryAssociation(
    name="contextVariable46",
    ends={
        Property(name="Variable", type=EssentialOCL_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_ExpressionInOcl47", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
generatedType48: BinaryAssociation = BinaryAssociation(
    name="generatedType48",
    ends={
        Property(name="Type50", type=EssentialOCL_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_ExpressionInOcl49", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameterVariable51: BinaryAssociation = BinaryAssociation(
    name="parameterVariable51",
    ends={
        Property(name="Variable53", type=EssentialOCL_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_ExpressionInOcl52", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
iterator73: BinaryAssociation = BinaryAssociation(
    name="iterator73",
    ends={
        Property(name="Variable75", type=EssentialOCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_LoopExp74", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument76: BinaryAssociation = BinaryAssociation(
    name="argument76",
    ends={
        Property(name="OclExpression77", type=EssentialOCL_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_OperationCallExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
result65: BinaryAssociation = BinaryAssociation(
    name="result65",
    ends={
        Property(name="Variable66", type=EssentialOCL_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_IterateExp", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
in_67: BinaryAssociation = BinaryAssociation(
    name="in_67",
    ends={
        Property(name="OclExpression68", type=EssentialOCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_LetExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable69: BinaryAssociation = BinaryAssociation(
    name="variable69",
    ends={
        Property(name="Variable70", type=EssentialOCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="letExp", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body71: BinaryAssociation = BinaryAssociation(
    name="body71",
    ends={
        Property(name="OclExpression72", type=EssentialOCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_LoopExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
attribute84: BinaryAssociation = BinaryAssociation(
    name="attribute84",
    ends={
        Property(name="Property85", type=EssentialOCL_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_TupleLiteralPart", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
tupleLiteralExp86: BinaryAssociation = BinaryAssociation(
    name="tupleLiteralExp86",
    ends={
        Property(name="TupleLiteralExp", type=EssentialOCL_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="part87", type=TupleLiteralExp, multiplicity=Multiplicity(0, 1))
    }
)
value88: BinaryAssociation = BinaryAssociation(
    name="value88",
    ends={
        Property(name="OclExpression90", type=EssentialOCL_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_TupleLiteralPart89", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referredOperation78: BinaryAssociation = BinaryAssociation(
    name="referredOperation78",
    ends={
        Property(name="Operation80", type=EssentialOCL_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_OperationCallExp79", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
referredProperty81: BinaryAssociation = BinaryAssociation(
    name="referredProperty81",
    ends={
        Property(name="Property82", type=EssentialOCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_PropertyCallExp", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
part83: BinaryAssociation = BinaryAssociation(
    name="part83",
    ends={
        Property(name="TupleLiteralPart", type=EssentialOCL_TupleLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="tupleLiteralExp", type=TupleLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rule101: BinaryAssociation = BinaryAssociation(
    name="rule101",
    ends={
        Property(name="Rule", type=QVTBase_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="domain", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
typedModel102: BinaryAssociation = BinaryAssociation(
    name="typedModel102",
    ends={
        Property(name="TypedModel", type=QVTBase_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTBase_Domain", type=TypedModel, multiplicity=Multiplicity(0, 1))
    }
)
queryExpression103: BinaryAssociation = BinaryAssociation(
    name="queryExpression103",
    ends={
        Property(name="OclExpression104", type=QVTBase_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTBase_Function", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referredType91: BinaryAssociation = BinaryAssociation(
    name="referredType91",
    ends={
        Property(name="Type92", type=EssentialOCL_TypeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_TypeExp", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
initExpression93: BinaryAssociation = BinaryAssociation(
    name="initExpression93",
    ends={
        Property(name="OclExpression94", type=EssentialOCL_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_Variable", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
letExp95: BinaryAssociation = BinaryAssociation(
    name="letExp95",
    ends={
        Property(name="LetExp", type=EssentialOCL_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="variable", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
representedParameter96: BinaryAssociation = BinaryAssociation(
    name="representedParameter96",
    ends={
        Property(name="Parameter98", type=EssentialOCL_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_Variable97", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
referredVariable99: BinaryAssociation = BinaryAssociation(
    name="referredVariable99",
    ends={
        Property(name="Variable100", type=EssentialOCL_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_VariableExp", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
extends116: BinaryAssociation = BinaryAssociation(
    name="extends116",
    ends={
        Property(name="Transformation117", type=QVTBase_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTBase_Transformation", type=Transformation, multiplicity=Multiplicity(0, 1))
    }
)
modelParameter118: BinaryAssociation = BinaryAssociation(
    name="modelParameter118",
    ends={
        Property(name="TypedModel119", type=QVTBase_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation", type=TypedModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTag120: BinaryAssociation = BinaryAssociation(
    name="ownedTag120",
    ends={
        Property(name="Tag", type=QVTBase_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTBase_Transformation121", type=Tag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rule122: BinaryAssociation = BinaryAssociation(
    name="rule122",
    ends={
        Property(name="Rule124", type=QVTBase_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation123", type=Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindsTo105: BinaryAssociation = BinaryAssociation(
    name="bindsTo105",
    ends={
        Property(name="Variable106", type=QVTBase_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTBase_Pattern", type=Variable, multiplicity=Multiplicity(0, 9999))
    }
)
predicate107: BinaryAssociation = BinaryAssociation(
    name="predicate107",
    ends={
        Property(name="Predicate", type=QVTBase_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="pattern", type=Predicate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conditionExpression108: BinaryAssociation = BinaryAssociation(
    name="conditionExpression108",
    ends={
        Property(name="OclExpression109", type=QVTBase_Predicate, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTBase_Predicate", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
pattern110: BinaryAssociation = BinaryAssociation(
    name="pattern110",
    ends={
        Property(name="Pattern", type=QVTBase_Predicate, multiplicity=Multiplicity(1, 1)),
        Property(name="predicate", type=Pattern, multiplicity=Multiplicity(1, 1))
    }
)
domain111: BinaryAssociation = BinaryAssociation(
    name="domain111",
    ends={
        Property(name="Domain", type=QVTBase_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="rule", type=Domain, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
overrides112: BinaryAssociation = BinaryAssociation(
    name="overrides112",
    ends={
        Property(name="Rule113", type=QVTBase_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTBase_Rule", type=Rule, multiplicity=Multiplicity(0, 1))
    }
)
transformation114: BinaryAssociation = BinaryAssociation(
    name="transformation114",
    ends={
        Property(name="Transformation", type=QVTBase_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="rule115", type=Transformation, multiplicity=Multiplicity(0, 1))
    }
)
value137: BinaryAssociation = BinaryAssociation(
    name="value137",
    ends={
        Property(name="OclExpression138", type=QVTCore_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTCore_Assignment", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
area139: BinaryAssociation = BinaryAssociation(
    name="area139",
    ends={
        Property(name="Area", type=QVTCore_BottomPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="bottomPattern", type=Area, multiplicity=Multiplicity(1, 1))
    }
)
assignment140: BinaryAssociation = BinaryAssociation(
    name="assignment140",
    ends={
        Property(name="Assignment", type=QVTCore_BottomPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="bottomPattern141", type=Assignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enforcementOperation142: BinaryAssociation = BinaryAssociation(
    name="enforcementOperation142",
    ends={
        Property(name="EnforcementOperation", type=QVTCore_BottomPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="bottomPattern143", type=EnforcementOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependsOn125: BinaryAssociation = BinaryAssociation(
    name="dependsOn125",
    ends={
        Property(name="TypedModel126", type=QVTBase_TypedModel, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTBase_TypedModel", type=TypedModel, multiplicity=Multiplicity(0, 9999))
    }
)
transformation127: BinaryAssociation = BinaryAssociation(
    name="transformation127",
    ends={
        Property(name="Transformation128", type=QVTBase_TypedModel, multiplicity=Multiplicity(1, 1)),
        Property(name="modelParameter", type=Transformation, multiplicity=Multiplicity(1, 1))
    }
)
usedPackage129: BinaryAssociation = BinaryAssociation(
    name="usedPackage129",
    ends={
        Property(name="Package131", type=QVTBase_TypedModel, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTBase_TypedModel130", type=Package, multiplicity=Multiplicity(1, 9999))
    }
)
bottomPattern132: BinaryAssociation = BinaryAssociation(
    name="bottomPattern132",
    ends={
        Property(name="BottomPattern", type=QVTCore_Area, multiplicity=Multiplicity(1, 1)),
        Property(name="area", type=BottomPattern, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
guardPattern133: BinaryAssociation = BinaryAssociation(
    name="guardPattern133",
    ends={
        Property(name="GuardPattern", type=QVTCore_Area, multiplicity=Multiplicity(1, 1)),
        Property(name="area134", type=GuardPattern, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bottomPattern135: BinaryAssociation = BinaryAssociation(
    name="bottomPattern135",
    ends={
        Property(name="BottomPattern136", type=QVTCore_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="assignment", type=BottomPattern, multiplicity=Multiplicity(1, 1))
    }
)
context153: BinaryAssociation = BinaryAssociation(
    name="context153",
    ends={
        Property(name="Mapping", type=QVTCore_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="local", type=Mapping, multiplicity=Multiplicity(0, 1))
    }
)
local154: BinaryAssociation = BinaryAssociation(
    name="local154",
    ends={
        Property(name="Mapping155", type=QVTCore_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="context", type=Mapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refinement156: BinaryAssociation = BinaryAssociation(
    name="refinement156",
    ends={
        Property(name="Mapping157", type=QVTCore_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="specification", type=Mapping, multiplicity=Multiplicity(0, 9999))
    }
)
specification158: BinaryAssociation = BinaryAssociation(
    name="specification158",
    ends={
        Property(name="Mapping159", type=QVTCore_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="refinement", type=Mapping, multiplicity=Multiplicity(0, 9999))
    }
)
slotExpression160: BinaryAssociation = BinaryAssociation(
    name="slotExpression160",
    ends={
        Property(name="OclExpression161", type=QVTCore_PropertyAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTCore_PropertyAssignment", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
realizedVariable144: BinaryAssociation = BinaryAssociation(
    name="realizedVariable144",
    ends={
        Property(name="RealizedVariable", type=QVTCore_BottomPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="bottomPattern145", type=RealizedVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable146: BinaryAssociation = BinaryAssociation(
    name="variable146",
    ends={
        Property(name="Variable147", type=QVTCore_CorePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTCore_CorePattern", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bottomPattern148: BinaryAssociation = BinaryAssociation(
    name="bottomPattern148",
    ends={
        Property(name="BottomPattern149", type=QVTCore_EnforcementOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="enforcementOperation", type=BottomPattern, multiplicity=Multiplicity(1, 1))
    }
)
operationCallExp150: BinaryAssociation = BinaryAssociation(
    name="operationCallExp150",
    ends={
        Property(name="OperationCallExp", type=QVTCore_EnforcementOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTCore_EnforcementOperation", type=OperationCallExp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
area151: BinaryAssociation = BinaryAssociation(
    name="area151",
    ends={
        Property(name="Area152", type=QVTCore_GuardPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="guardPattern", type=Area, multiplicity=Multiplicity(1, 1))
    }
)
part176: BinaryAssociation = BinaryAssociation(
    name="part176",
    ends={
        Property(name="PropertyTemplateItem", type=QVTTemplate_ObjectTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="objContainer", type=PropertyTemplateItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredClass177: BinaryAssociation = BinaryAssociation(
    name="referredClass177",
    ends={
        Property(name="Class178", type=QVTTemplate_ObjectTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTTemplate_ObjectTemplateExp", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
objContainer179: BinaryAssociation = BinaryAssociation(
    name="objContainer179",
    ends={
        Property(name="ObjectTemplateExp", type=QVTTemplate_PropertyTemplateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="part180", type=ObjectTemplateExp, multiplicity=Multiplicity(1, 1))
    }
)
targetProperty162: BinaryAssociation = BinaryAssociation(
    name="targetProperty162",
    ends={
        Property(name="Property164", type=QVTCore_PropertyAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTCore_PropertyAssignment163", type=Property_, multiplicity=Multiplicity(1, 1))
    }
)
bottomPattern165: BinaryAssociation = BinaryAssociation(
    name="bottomPattern165",
    ends={
        Property(name="BottomPattern166", type=QVTCore_RealizedVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="realizedVariable", type=BottomPattern, multiplicity=Multiplicity(1, 1))
    }
)
targetVariable167: BinaryAssociation = BinaryAssociation(
    name="targetVariable167",
    ends={
        Property(name="Variable168", type=QVTCore_VariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTCore_VariableAssignment", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
member169: BinaryAssociation = BinaryAssociation(
    name="member169",
    ends={
        Property(name="OclExpression170", type=QVTTemplate_CollectionTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTTemplate_CollectionTemplateExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredCollectionType171: BinaryAssociation = BinaryAssociation(
    name="referredCollectionType171",
    ends={
        Property(name="CollectionType", type=QVTTemplate_CollectionTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTTemplate_CollectionTemplateExp172", type=CollectionType, multiplicity=Multiplicity(1, 1))
    }
)
rest173: BinaryAssociation = BinaryAssociation(
    name="rest173",
    ends={
        Property(name="Variable175", type=QVTTemplate_CollectionTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTTemplate_CollectionTemplateExp174", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
oppositePart196: BinaryAssociation = BinaryAssociation(
    name="oppositePart196",
    ends={
        Property(name="Property198", type=QVTRelation_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_Key197", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)
part199: BinaryAssociation = BinaryAssociation(
    name="part199",
    ends={
        Property(name="Property201", type=QVTRelation_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_Key200", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)
transformation202: BinaryAssociation = BinaryAssociation(
    name="transformation202",
    ends={
        Property(name="RelationalTransformation", type=QVTRelation_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedKey", type=RelationalTransformation, multiplicity=Multiplicity(0, 1))
    }
)
referredProperty181: BinaryAssociation = BinaryAssociation(
    name="referredProperty181",
    ends={
        Property(name="Property182", type=QVTTemplate_PropertyTemplateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTTemplate_PropertyTemplateItem", type=Property_, multiplicity=Multiplicity(1, 1))
    }
)
value183: BinaryAssociation = BinaryAssociation(
    name="value183",
    ends={
        Property(name="OclExpression185", type=QVTTemplate_PropertyTemplateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTTemplate_PropertyTemplateItem184", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bindsTo186: BinaryAssociation = BinaryAssociation(
    name="bindsTo186",
    ends={
        Property(name="Variable187", type=QVTTemplate_TemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTTemplate_TemplateExp", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
where188: BinaryAssociation = BinaryAssociation(
    name="where188",
    ends={
        Property(name="OclExpression190", type=QVTTemplate_TemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTTemplate_TemplateExp189", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
relationDomain191: BinaryAssociation = BinaryAssociation(
    name="relationDomain191",
    ends={
        Property(name="RelationDomain", type=QVTRelation_DomainPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="pattern192", type=RelationDomain, multiplicity=Multiplicity(1, 1))
    }
)
templateExpression193: BinaryAssociation = BinaryAssociation(
    name="templateExpression193",
    ends={
        Property(name="TemplateExp", type=QVTRelation_DomainPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_DomainPattern", type=TemplateExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifies194: BinaryAssociation = BinaryAssociation(
    name="identifies194",
    ends={
        Property(name="Class195", type=QVTRelation_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_Key", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
rootVariable218: BinaryAssociation = BinaryAssociation(
    name="rootVariable218",
    ends={
        Property(name="Variable219", type=QVTRelation_RelationDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_RelationDomain", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
owner220: BinaryAssociation = BinaryAssociation(
    name="owner220",
    ends={
        Property(name="RelationDomain221", type=QVTRelation_RelationDomainAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="defaultAssignment", type=RelationDomain, multiplicity=Multiplicity(1, 1))
    }
)
valueExp222: BinaryAssociation = BinaryAssociation(
    name="valueExp222",
    ends={
        Property(name="OclExpression223", type=QVTRelation_RelationDomainAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_RelationDomainAssignment", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable224: BinaryAssociation = BinaryAssociation(
    name="variable224",
    ends={
        Property(name="Variable226", type=QVTRelation_RelationDomainAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_RelationDomainAssignment225", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
operationalImpl203: BinaryAssociation = BinaryAssociation(
    name="operationalImpl203",
    ends={
        Property(name="RelationImplementation", type=QVTRelation_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="relation", type=RelationImplementation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable204: BinaryAssociation = BinaryAssociation(
    name="variable204",
    ends={
        Property(name="Variable205", type=QVTRelation_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_Relation", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
when206: BinaryAssociation = BinaryAssociation(
    name="when206",
    ends={
        Property(name="Pattern208", type=QVTRelation_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_Relation207", type=Pattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
where209: BinaryAssociation = BinaryAssociation(
    name="where209",
    ends={
        Property(name="Pattern211", type=QVTRelation_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_Relation210", type=Pattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
argument212: BinaryAssociation = BinaryAssociation(
    name="argument212",
    ends={
        Property(name="OclExpression213", type=QVTRelation_RelationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_RelationCallExp", type=OclExpression, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
referredRelation214: BinaryAssociation = BinaryAssociation(
    name="referredRelation214",
    ends={
        Property(name="Relation", type=QVTRelation_RelationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_RelationCallExp215", type=Relation, multiplicity=Multiplicity(1, 1))
    }
)
defaultAssignment216: BinaryAssociation = BinaryAssociation(
    name="defaultAssignment216",
    ends={
        Property(name="RelationDomainAssignment", type=QVTRelation_RelationDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=RelationDomainAssignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pattern217: BinaryAssociation = BinaryAssociation(
    name="pattern217",
    ends={
        Property(name="DomainPattern", type=QVTRelation_RelationDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="relationDomain", type=DomainPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultValue245: BinaryAssociation = BinaryAssociation(
    name="defaultValue245",
    ends={
        Property(name="OclExpression246", type=ImperativeOCL_AssignExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_AssignExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left247: BinaryAssociation = BinaryAssociation(
    name="left247",
    ends={
        Property(name="OclExpression249", type=ImperativeOCL_AssignExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_AssignExp248", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value250: BinaryAssociation = BinaryAssociation(
    name="value250",
    ends={
        Property(name="OclExpression252", type=ImperativeOCL_AssignExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_AssignExp251", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
impl227: BinaryAssociation = BinaryAssociation(
    name="impl227",
    ends={
        Property(name="Operation228", type=QVTRelation_RelationImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_RelationImplementation", type=Operation, multiplicity=Multiplicity(1, 1))
    }
)
inDirectionOf229: BinaryAssociation = BinaryAssociation(
    name="inDirectionOf229",
    ends={
        Property(name="TypedModel231", type=QVTRelation_RelationImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTRelation_RelationImplementation230", type=TypedModel, multiplicity=Multiplicity(1, 1))
    }
)
relation232: BinaryAssociation = BinaryAssociation(
    name="relation232",
    ends={
        Property(name="Relation233", type=QVTRelation_RelationImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="operationalImpl", type=Relation, multiplicity=Multiplicity(1, 1))
    }
)
ownedKey234: BinaryAssociation = BinaryAssociation(
    name="ownedKey234",
    ends={
        Property(name="Key", type=QVTRelation_RelationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation235", type=Key, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body236: BinaryAssociation = BinaryAssociation(
    name="body236",
    ends={
        Property(name="OclExpression237", type=ImperativeOCL_AltExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_AltExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition238: BinaryAssociation = BinaryAssociation(
    name="condition238",
    ends={
        Property(name="OclExpression240", type=ImperativeOCL_AltExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_AltExp239", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
assertion241: BinaryAssociation = BinaryAssociation(
    name="assertion241",
    ends={
        Property(name="OclExpression242", type=ImperativeOCL_AssertExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_AssertExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
log243: BinaryAssociation = BinaryAssociation(
    name="log243",
    ends={
        Property(name="LogExp", type=ImperativeOCL_AssertExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_AssertExp244", type=LogExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnedElement265: BinaryAssociation = BinaryAssociation(
    name="returnedElement265",
    ends={
        Property(name="Variable267", type=ImperativeOCL_ComputeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_ComputeExp266", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
part268: BinaryAssociation = BinaryAssociation(
    name="part268",
    ends={
        Property(name="DictLiteralPart", type=ImperativeOCL_DictLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="partOwner", type=DictLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key269: BinaryAssociation = BinaryAssociation(
    name="key269",
    ends={
        Property(name="OclExpression270", type=ImperativeOCL_DictLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_DictLiteralPart", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body253: BinaryAssociation = BinaryAssociation(
    name="body253",
    ends={
        Property(name="OclExpression254", type=ImperativeOCL_BlockExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_BlockExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body255: BinaryAssociation = BinaryAssociation(
    name="body255",
    ends={
        Property(name="OclExpression256", type=ImperativeOCL_CatchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_CatchExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exception257: BinaryAssociation = BinaryAssociation(
    name="exception257",
    ends={
        Property(name="Type259", type=ImperativeOCL_CatchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_CatchExp258", type=Type, multiplicity=Multiplicity(1, 9999))
    }
)
exceptionVariable260: BinaryAssociation = BinaryAssociation(
    name="exceptionVariable260",
    ends={
        Property(name="Variable262", type=ImperativeOCL_CatchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_CatchExp261", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body263: BinaryAssociation = BinaryAssociation(
    name="body263",
    ends={
        Property(name="OclExpression264", type=ImperativeOCL_ComputeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_ComputeExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
argument282: BinaryAssociation = BinaryAssociation(
    name="argument282",
    ends={
        Property(name="OclExpression283", type=ImperativeOCL_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_InstantiationExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extent284: BinaryAssociation = BinaryAssociation(
    name="extent284",
    ends={
        Property(name="Variable286", type=ImperativeOCL_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_InstantiationExp285", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
instantiatedClass287: BinaryAssociation = BinaryAssociation(
    name="instantiatedClass287",
    ends={
        Property(name="Class289", type=ImperativeOCL_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_InstantiationExp288", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
initializationOperation290: BinaryAssociation = BinaryAssociation(
    name="initializationOperation290",
    ends={
        Property(name="Operation292", type=ImperativeOCL_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_InstantiationExp291", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
value271: BinaryAssociation = BinaryAssociation(
    name="value271",
    ends={
        Property(name="OclExpression273", type=ImperativeOCL_DictLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_DictLiteralPart272", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
partOwner274: BinaryAssociation = BinaryAssociation(
    name="partOwner274",
    ends={
        Property(name="DictLiteralExp", type=ImperativeOCL_DictLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="part275", type=DictLiteralExp, multiplicity=Multiplicity(1, 1))
    }
)
keyType276: BinaryAssociation = BinaryAssociation(
    name="keyType276",
    ends={
        Property(name="Type277", type=ImperativeOCL_DictionaryType, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_DictionaryType", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
target278: BinaryAssociation = BinaryAssociation(
    name="target278",
    ends={
        Property(name="Variable279", type=ImperativeOCL_ImperativeIterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_ImperativeIterateExp", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition280: BinaryAssociation = BinaryAssociation(
    name="condition280",
    ends={
        Property(name="OclExpression281", type=ImperativeOCL_ImperativeLoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_ImperativeLoopExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alternativePart304: BinaryAssociation = BinaryAssociation(
    name="alternativePart304",
    ends={
        Property(name="AltExp", type=ImperativeOCL_SwitchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_SwitchExp", type=AltExp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elsePart305: BinaryAssociation = BinaryAssociation(
    name="elsePart305",
    ends={
        Property(name="OclExpression307", type=ImperativeOCL_SwitchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_SwitchExp306", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
element293: BinaryAssociation = BinaryAssociation(
    name="element293",
    ends={
        Property(name="OclExpression294", type=ImperativeOCL_ListLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_ListLiteralExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition295: BinaryAssociation = BinaryAssociation(
    name="condition295",
    ends={
        Property(name="OclExpression296", type=ImperativeOCL_LogExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_LogExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
argument297: BinaryAssociation = BinaryAssociation(
    name="argument297",
    ends={
        Property(name="OclExpression298", type=ImperativeOCL_RaiseExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_RaiseExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exception299: BinaryAssociation = BinaryAssociation(
    name="exception299",
    ends={
        Property(name="Type301", type=ImperativeOCL_RaiseExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_RaiseExp300", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
value302: BinaryAssociation = BinaryAssociation(
    name="value302",
    ends={
        Property(name="OclExpression303", type=ImperativeOCL_ReturnExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_ReturnExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referredVariable322: BinaryAssociation = BinaryAssociation(
    name="referredVariable322",
    ends={
        Property(name="Variable323", type=ImperativeOCL_VariableInitExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_VariableInitExp", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body324: BinaryAssociation = BinaryAssociation(
    name="body324",
    ends={
        Property(name="OclExpression325", type=ImperativeOCL_WhileExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_WhileExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exceptClause308: BinaryAssociation = BinaryAssociation(
    name="exceptClause308",
    ends={
        Property(name="CatchExp", type=ImperativeOCL_TryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_TryExp", type=CatchExp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tryBody309: BinaryAssociation = BinaryAssociation(
    name="tryBody309",
    ends={
        Property(name="OclExpression311", type=ImperativeOCL_TryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_TryExp310", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
base312: BinaryAssociation = BinaryAssociation(
    name="base312",
    ends={
        Property(name="Type313", type=ImperativeOCL_Typedef, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_Typedef", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
condition314: BinaryAssociation = BinaryAssociation(
    name="condition314",
    ends={
        Property(name="OclExpression316", type=ImperativeOCL_Typedef, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_Typedef315", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
item317: BinaryAssociation = BinaryAssociation(
    name="item317",
    ends={
        Property(name="OclExpression318", type=ImperativeOCL_UnlinkExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_UnlinkExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target319: BinaryAssociation = BinaryAssociation(
    name="target319",
    ends={
        Property(name="OclExpression321", type=ImperativeOCL_UnlinkExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_UnlinkExp320", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
overridden334: BinaryAssociation = BinaryAssociation(
    name="overridden334",
    ends={
        Property(name="Property336", type=QVTOperational_ContextualProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ContextualProperty335", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
condition326: BinaryAssociation = BinaryAssociation(
    name="condition326",
    ends={
        Property(name="OclExpression328", type=ImperativeOCL_WhileExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_WhileExp327", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context329: BinaryAssociation = BinaryAssociation(
    name="context329",
    ends={
        Property(name="Class330", type=QVTOperational_ContextualProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ContextualProperty", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
initExpression331: BinaryAssociation = BinaryAssociation(
    name="initExpression331",
    ends={
        Property(name="OclExpression333", type=QVTOperational_ContextualProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ContextualProperty332", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
disjunct348: BinaryAssociation = BinaryAssociation(
    name="disjunct348",
    ends={
        Property(name="MappingOperation", type=QVTOperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingOperation", type=MappingOperation, multiplicity=Multiplicity(0, 9999))
    }
)
body337: BinaryAssociation = BinaryAssociation(
    name="body337",
    ends={
        Property(name="OperationBody", type=QVTOperational_ImperativeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation338", type=OperationBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
context339: BinaryAssociation = BinaryAssociation(
    name="context339",
    ends={
        Property(name="VarParameter", type=QVTOperational_ImperativeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ctxOwner", type=VarParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
overridden340: BinaryAssociation = BinaryAssociation(
    name="overridden340",
    ends={
        Property(name="ImperativeOperation", type=QVTOperational_ImperativeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ImperativeOperation", type=ImperativeOperation, multiplicity=Multiplicity(0, 1))
    }
)
result341: BinaryAssociation = BinaryAssociation(
    name="result341",
    ends={
        Property(name="VarParameter342", type=QVTOperational_ImperativeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="resOwner", type=VarParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
endSection343: BinaryAssociation = BinaryAssociation(
    name="endSection343",
    ends={
        Property(name="OclExpression344", type=QVTOperational_MappingBody, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingBody", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initSection345: BinaryAssociation = BinaryAssociation(
    name="initSection345",
    ends={
        Property(name="OclExpression347", type=QVTOperational_MappingBody, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingBody346", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extent364: BinaryAssociation = BinaryAssociation(
    name="extent364",
    ends={
        Property(name="ModelParameter", type=QVTOperational_MappingParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingParameter", type=ModelParameter, multiplicity=Multiplicity(0, 1))
    }
)
referredDomain365: BinaryAssociation = BinaryAssociation(
    name="referredDomain365",
    ends={
        Property(name="RelationDomain367", type=QVTOperational_MappingParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingParameter366", type=RelationDomain, multiplicity=Multiplicity(0, 1))
    }
)
module368: BinaryAssociation = BinaryAssociation(
    name="module368",
    ends={
        Property(name="OperationalTransformation", type=QVTOperational_ModelParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="modelParameter369", type=OperationalTransformation, multiplicity=Multiplicity(1, 1))
    }
)
inherited349: BinaryAssociation = BinaryAssociation(
    name="inherited349",
    ends={
        Property(name="MappingOperation351", type=QVTOperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingOperation350", type=MappingOperation, multiplicity=Multiplicity(0, 9999))
    }
)
merged352: BinaryAssociation = BinaryAssociation(
    name="merged352",
    ends={
        Property(name="MappingOperation354", type=QVTOperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingOperation353", type=MappingOperation, multiplicity=Multiplicity(0, 9999))
    }
)
refinedRelation355: BinaryAssociation = BinaryAssociation(
    name="refinedRelation355",
    ends={
        Property(name="Relation357", type=QVTOperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingOperation356", type=Relation, multiplicity=Multiplicity(0, 1))
    }
)
when358: BinaryAssociation = BinaryAssociation(
    name="when358",
    ends={
        Property(name="OclExpression360", type=QVTOperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingOperation359", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
where361: BinaryAssociation = BinaryAssociation(
    name="where361",
    ends={
        Property(name="OclExpression363", type=QVTOperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingOperation362", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedTag380: BinaryAssociation = BinaryAssociation(
    name="ownedTag380",
    ends={
        Property(name="Tag382", type=QVTOperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_Module381", type=Tag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVariable383: BinaryAssociation = BinaryAssociation(
    name="ownedVariable383",
    ends={
        Property(name="Variable385", type=QVTOperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_Module384", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usedModelType386: BinaryAssociation = BinaryAssociation(
    name="usedModelType386",
    ends={
        Property(name="ModelType", type=QVTOperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_Module387", type=ModelType, multiplicity=Multiplicity(0, 9999))
    }
)
additionalCondition370: BinaryAssociation = BinaryAssociation(
    name="additionalCondition370",
    ends={
        Property(name="OclExpression371", type=QVTOperational_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ModelType", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metamodel372: BinaryAssociation = BinaryAssociation(
    name="metamodel372",
    ends={
        Property(name="Package374", type=QVTOperational_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ModelType373", type=Package, multiplicity=Multiplicity(1, 9999))
    }
)
configProperty375: BinaryAssociation = BinaryAssociation(
    name="configProperty375",
    ends={
        Property(name="Property376", type=QVTOperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_Module", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)
entry377: BinaryAssociation = BinaryAssociation(
    name="entry377",
    ends={
        Property(name="EntryOperation", type=QVTOperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_Module378", type=EntryOperation, multiplicity=Multiplicity(0, 1))
    }
)
moduleImport379: BinaryAssociation = BinaryAssociation(
    name="moduleImport379",
    ends={
        Property(name="ModuleImport", type=QVTOperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="module", type=ModuleImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operation400: BinaryAssociation = BinaryAssociation(
    name="operation400",
    ends={
        Property(name="ImperativeOperation401", type=QVTOperational_OperationBody, multiplicity=Multiplicity(1, 1)),
        Property(name="body", type=ImperativeOperation, multiplicity=Multiplicity(0, 1))
    }
)
variable402: BinaryAssociation = BinaryAssociation(
    name="variable402",
    ends={
        Property(name="Variable404", type=QVTOperational_OperationBody, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_OperationBody403", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateClass405: BinaryAssociation = BinaryAssociation(
    name="intermediateClass405",
    ends={
        Property(name="Class406", type=QVTOperational_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_OperationalTransformation", type=Class_, multiplicity=Multiplicity(0, 9999))
    }
)
intermediateProperty407: BinaryAssociation = BinaryAssociation(
    name="intermediateProperty407",
    ends={
        Property(name="Property409", type=QVTOperational_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_OperationalTransformation408", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)
binding388: BinaryAssociation = BinaryAssociation(
    name="binding388",
    ends={
        Property(name="ModelType389", type=QVTOperational_ModuleImport, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ModuleImport", type=ModelType, multiplicity=Multiplicity(0, 9999))
    }
)
importedModule390: BinaryAssociation = BinaryAssociation(
    name="importedModule390",
    ends={
        Property(name="Module", type=QVTOperational_ModuleImport, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ModuleImport391", type=Module, multiplicity=Multiplicity(1, 1))
    }
)
module392: BinaryAssociation = BinaryAssociation(
    name="module392",
    ends={
        Property(name="Module393", type=QVTOperational_ModuleImport, multiplicity=Multiplicity(1, 1)),
        Property(name="moduleImport", type=Module, multiplicity=Multiplicity(0, 1))
    }
)
body394: BinaryAssociation = BinaryAssociation(
    name="body394",
    ends={
        Property(name="ConstructorBody", type=QVTOperational_ObjectExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ObjectExp", type=ConstructorBody, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referredObject395: BinaryAssociation = BinaryAssociation(
    name="referredObject395",
    ends={
        Property(name="Variable397", type=QVTOperational_ObjectExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ObjectExp396", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
content398: BinaryAssociation = BinaryAssociation(
    name="content398",
    ends={
        Property(name="OclExpression399", type=QVTOperational_OperationBody, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_OperationBody", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inMapping424: BinaryAssociation = BinaryAssociation(
    name="inMapping424",
    ends={
        Property(name="MappingOperation425", type=QVTOperational_ResolveInExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ResolveInExp", type=MappingOperation, multiplicity=Multiplicity(0, 1))
    }
)
ctxOwner426: BinaryAssociation = BinaryAssociation(
    name="ctxOwner426",
    ends={
        Property(name="ImperativeOperation428", type=QVTOperational_VarParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="context427", type=ImperativeOperation, multiplicity=Multiplicity(0, 1))
    }
)
resOwner429: BinaryAssociation = BinaryAssociation(
    name="resOwner429",
    ends={
        Property(name="ImperativeOperation430", type=QVTOperational_VarParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="result", type=ImperativeOperation, multiplicity=Multiplicity(0, 1))
    }
)
modelParameter410: BinaryAssociation = BinaryAssociation(
    name="modelParameter410",
    ends={
        Property(name="ModelParameter412", type=QVTOperational_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="module411", type=ModelParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refined413: BinaryAssociation = BinaryAssociation(
    name="refined413",
    ends={
        Property(name="RelationalTransformation415", type=QVTOperational_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_OperationalTransformation414", type=RelationalTransformation, multiplicity=Multiplicity(0, 1))
    }
)
relation416: BinaryAssociation = BinaryAssociation(
    name="relation416",
    ends={
        Property(name="Relation418", type=QVTOperational_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_OperationalTransformation417", type=Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition419: BinaryAssociation = BinaryAssociation(
    name="condition419",
    ends={
        Property(name="OclExpression420", type=QVTOperational_ResolveExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ResolveExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target421: BinaryAssociation = BinaryAssociation(
    name="target421",
    ends={
        Property(name="Variable423", type=QVTOperational_ResolveExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ResolveExp422", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_EMOF_Class_Type = Generalization(general=Type, specific=EMOF_Class)
gen_EMOF_Comment_Element = Generalization(general=Element, specific=EMOF_Comment)
gen_EMOF_DataType_Type = Generalization(general=Type, specific=EMOF_DataType)
gen_EMOF_Element_Object = Generalization(general=Object, specific=EMOF_Element)
gen_EMOF_Operation_MultiplicityElement = Generalization(general=MultiplicityElement, specific=EMOF_Operation)
gen_EMOF_Package_NamedElement = Generalization(general=NamedElement, specific=EMOF_Package)
gen_EMOF_Enumeration_DataType = Generalization(general=DataType, specific=EMOF_Enumeration)
gen_EMOF_EnumerationLiteral_NamedElement = Generalization(general=NamedElement, specific=EMOF_EnumerationLiteral)
gen_EMOF_Extent_Object = Generalization(general=Object, specific=EMOF_Extent)
gen_EMOF_Factory_Element = Generalization(general=Element, specific=EMOF_Factory)
gen_EMOF_NamedElement_Element = Generalization(general=Element, specific=EMOF_NamedElement)
gen_EMOF_Operation_TypedElement = Generalization(general=TypedElement, specific=EMOF_Operation)
gen_EMOF_Tag_Element = Generalization(general=Element, specific=EMOF_Tag)
gen_EMOF_Type_NamedElement = Generalization(general=NamedElement, specific=EMOF_Type)
gen_EMOF_TypedElement_NamedElement = Generalization(general=NamedElement, specific=EMOF_TypedElement)
gen_EMOF_Parameter_TypedElement = Generalization(general=TypedElement, specific=EMOF_Parameter)
gen_EMOF_Parameter_MultiplicityElement = Generalization(general=MultiplicityElement, specific=EMOF_Parameter)
gen_EMOF_PrimitiveType_DataType = Generalization(general=DataType, specific=EMOF_PrimitiveType)
gen_EMOF_Property_TypedElement = Generalization(general=TypedElement, specific=EMOF_Property)
gen_EMOF_Property_MultiplicityElement = Generalization(general=MultiplicityElement, specific=EMOF_Property)
gen_EMOF_ReflectiveCollection_Object = Generalization(general=Object, specific=EMOF_ReflectiveCollection)
gen_EMOF_ReflectiveSequence_ReflectiveCollection = Generalization(general=ReflectiveCollection, specific=EMOF_ReflectiveSequence)
gen_EssentialOCL_CollectionLiteralPart_TypedElement = Generalization(general=TypedElement, specific=EssentialOCL_CollectionLiteralPart)
gen_EssentialOCL_CollectionRange_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=EssentialOCL_CollectionRange)
gen_EMOF_URIExtent_Extent = Generalization(general=Extent, specific=EMOF_URIExtent)
gen_EssentialOCL_AnyType_Type = Generalization(general=Type, specific=EssentialOCL_AnyType)
gen_EssentialOCL_BagType_CollectionType = Generalization(general=CollectionType, specific=EssentialOCL_BagType)
gen_EssentialOCL_BooleanLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=EssentialOCL_BooleanLiteralExp)
gen_EssentialOCL_CallExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_CallExp)
gen_EssentialOCL_CollectionItem_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=EssentialOCL_CollectionItem)
gen_EssentialOCL_CollectionLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=EssentialOCL_CollectionLiteralExp)
gen_EssentialOCL_FeatureCallExp_CallExp = Generalization(general=CallExp, specific=EssentialOCL_FeatureCallExp)
gen_EssentialOCL_IfExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_IfExp)
gen_EssentialOCL_CollectionType_DataType = Generalization(general=DataType, specific=EssentialOCL_CollectionType)
gen_EssentialOCL_EnumLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=EssentialOCL_EnumLiteralExp)
gen_EssentialOCL_ExpressionInOcl_TypedElement = Generalization(general=TypedElement, specific=EssentialOCL_ExpressionInOcl)
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
gen_EssentialOCL_LoopExp_CallExp = Generalization(general=CallExp, specific=EssentialOCL_LoopExp)
gen_EssentialOCL_LoopExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_LoopExp)
gen_EssentialOCL_TupleLiteralPart_TypedElement = Generalization(general=TypedElement, specific=EssentialOCL_TupleLiteralPart)
gen_EssentialOCL_TupleType_Class = Generalization(general=Class_, specific=EssentialOCL_TupleType)
gen_EssentialOCL_TupleType_DataType = Generalization(general=DataType, specific=EssentialOCL_TupleType)
gen_EssentialOCL_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=EssentialOCL_OrderedSetType)
gen_EssentialOCL_PrimitiveLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=EssentialOCL_PrimitiveLiteralExp)
gen_EssentialOCL_PropertyCallExp_NavigationCallExp = Generalization(general=NavigationCallExp, specific=EssentialOCL_PropertyCallExp)
gen_EssentialOCL_RealLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=EssentialOCL_RealLiteralExp)
gen_EssentialOCL_SequenceType_CollectionType = Generalization(general=CollectionType, specific=EssentialOCL_SequenceType)
gen_EssentialOCL_SetType_CollectionType = Generalization(general=CollectionType, specific=EssentialOCL_SetType)
gen_EssentialOCL_StringLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=EssentialOCL_StringLiteralExp)
gen_EssentialOCL_TemplateParameterType_Type = Generalization(general=Type, specific=EssentialOCL_TemplateParameterType)
gen_EssentialOCL_TupleLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=EssentialOCL_TupleLiteralExp)
gen_QVTBase_Function_Operation = Generalization(general=Operation, specific=QVTBase_Function)
gen_QVTBase_FunctionParameter_Variable = Generalization(general=Variable, specific=QVTBase_FunctionParameter)
gen_EssentialOCL_TypeExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_TypeExp)
gen_EssentialOCL_UnlimitedNaturalExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=EssentialOCL_UnlimitedNaturalExp)
gen_EssentialOCL_Variable_TypedElement = Generalization(general=TypedElement, specific=EssentialOCL_Variable)
gen_EssentialOCL_VariableExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_VariableExp)
gen_EssentialOCL_VoidType_Type = Generalization(general=Type, specific=EssentialOCL_VoidType)
gen_QVTBase_Domain_NamedElement = Generalization(general=NamedElement, specific=QVTBase_Domain)
gen_QVTBase_TypedModel_NamedElement = Generalization(general=NamedElement, specific=QVTBase_TypedModel)
gen_QVTBase_FunctionParameter_Parameter = Generalization(general=Parameter_, specific=QVTBase_FunctionParameter)
gen_QVTBase_Pattern_Element = Generalization(general=Element, specific=QVTBase_Pattern)
gen_QVTBase_Predicate_Element = Generalization(general=Element, specific=QVTBase_Predicate)
gen_QVTBase_Rule_NamedElement = Generalization(general=NamedElement, specific=QVTBase_Rule)
gen_QVTBase_Transformation_Class = Generalization(general=Class_, specific=QVTBase_Transformation)
gen_QVTBase_Transformation_Package = Generalization(general=Package, specific=QVTBase_Transformation)
gen_QVTCore_BottomPattern_CorePattern = Generalization(general=CorePattern, specific=QVTCore_BottomPattern)
gen_QVTCore_Assignment_Element = Generalization(general=Element, specific=QVTCore_Assignment)
gen_QVTCore_PropertyAssignment_Assignment = Generalization(general=Assignment, specific=QVTCore_PropertyAssignment)
gen_QVTCore_CoreDomain_Domain = Generalization(general=Domain, specific=QVTCore_CoreDomain)
gen_QVTCore_CoreDomain_Area = Generalization(general=Area, specific=QVTCore_CoreDomain)
gen_QVTCore_CorePattern_Pattern = Generalization(general=Pattern, specific=QVTCore_CorePattern)
gen_QVTCore_EnforcementOperation_Element = Generalization(general=Element, specific=QVTCore_EnforcementOperation)
gen_QVTCore_GuardPattern_CorePattern = Generalization(general=CorePattern, specific=QVTCore_GuardPattern)
gen_QVTCore_Mapping_Rule = Generalization(general=Rule, specific=QVTCore_Mapping)
gen_QVTCore_Mapping_Area = Generalization(general=Area, specific=QVTCore_Mapping)
gen_QVTTemplate_ObjectTemplateExp_TemplateExp = Generalization(general=TemplateExp, specific=QVTTemplate_ObjectTemplateExp)
gen_QVTTemplate_PropertyTemplateItem_Element = Generalization(general=Element, specific=QVTTemplate_PropertyTemplateItem)
gen_QVTCore_RealizedVariable_Variable = Generalization(general=Variable, specific=QVTCore_RealizedVariable)
gen_QVTCore_VariableAssignment_Assignment = Generalization(general=Assignment, specific=QVTCore_VariableAssignment)
gen_QVTTemplate_CollectionTemplateExp_TemplateExp = Generalization(general=TemplateExp, specific=QVTTemplate_CollectionTemplateExp)
gen_QVTRelation_OppositePropertyCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=QVTRelation_OppositePropertyCallExp)
gen_QVTRelation_Relation_Rule = Generalization(general=Rule, specific=QVTRelation_Relation)
gen_QVTTemplate_TemplateExp_LiteralExp = Generalization(general=LiteralExp, specific=QVTTemplate_TemplateExp)
gen_QVTRelation_DomainPattern_Pattern = Generalization(general=Pattern, specific=QVTRelation_DomainPattern)
gen_QVTRelation_Key_Element = Generalization(general=Element, specific=QVTRelation_Key)
gen_QVTRelation_RelationDomainAssignment_Element = Generalization(general=Element, specific=QVTRelation_RelationDomainAssignment)
gen_QVTRelation_RelationImplementation_Element = Generalization(general=Element, specific=QVTRelation_RelationImplementation)
gen_QVTRelation_RelationCallExp_OclExpression = Generalization(general=OclExpression, specific=QVTRelation_RelationCallExp)
gen_QVTRelation_RelationDomain_Domain = Generalization(general=Domain, specific=QVTRelation_RelationDomain)
gen_ImperativeOCL_AssignExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_AssignExp)
gen_QVTRelation_RelationalTransformation_Transformation = Generalization(general=Transformation, specific=QVTRelation_RelationalTransformation)
gen_ImperativeOCL_AltExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_AltExp)
gen_ImperativeOCL_AssertExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_AssertExp)
gen_ImperativeOCL_ContinueExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_ContinueExp)
gen_ImperativeOCL_DictLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=ImperativeOCL_DictLiteralExp)
gen_ImperativeOCL_DictLiteralPart_Element = Generalization(general=Element, specific=ImperativeOCL_DictLiteralPart)
gen_ImperativeOCL_BlockExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_BlockExp)
gen_ImperativeOCL_BreakExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_BreakExp)
gen_ImperativeOCL_CatchExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_CatchExp)
gen_ImperativeOCL_ComputeExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_ComputeExp)
gen_ImperativeOCL_DictionaryType_CollectionType = Generalization(general=CollectionType, specific=ImperativeOCL_DictionaryType)
gen_ImperativeOCL_ForExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=ImperativeOCL_ForExp)
gen_ImperativeOCL_ImperativeExpression_OclExpression = Generalization(general=OclExpression, specific=ImperativeOCL_ImperativeExpression)
gen_ImperativeOCL_ImperativeIterateExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=ImperativeOCL_ImperativeIterateExp)
gen_ImperativeOCL_ImperativeLoopExp_LoopExp = Generalization(general=LoopExp, specific=ImperativeOCL_ImperativeLoopExp)
gen_ImperativeOCL_ImperativeLoopExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_ImperativeLoopExp)
gen_ImperativeOCL_InstantiationExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_InstantiationExp)
gen_ImperativeOCL_SwitchExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_SwitchExp)
gen_ImperativeOCL_ListLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=ImperativeOCL_ListLiteralExp)
gen_ImperativeOCL_ListType_CollectionType = Generalization(general=CollectionType, specific=ImperativeOCL_ListType)
gen_ImperativeOCL_LogExp_OperationCallExp = Generalization(general=OperationCallExp, specific=ImperativeOCL_LogExp)
gen_ImperativeOCL_LogExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_LogExp)
gen_ImperativeOCL_RaiseExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_RaiseExp)
gen_ImperativeOCL_ReturnExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_ReturnExp)
gen_ImperativeOCL_VariableInitExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_VariableInitExp)
gen_ImperativeOCL_WhileExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_WhileExp)
gen_ImperativeOCL_TryExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_TryExp)
gen_ImperativeOCL_Typedef_Class = Generalization(general=Class_, specific=ImperativeOCL_Typedef)
gen_ImperativeOCL_UnlinkExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_UnlinkExp)
gen_QVTOperational_EntryOperation_ImperativeOperation = Generalization(general=ImperativeOperation, specific=QVTOperational_EntryOperation)
gen_QVTOperational_Helper_ImperativeOperation = Generalization(general=ImperativeOperation, specific=QVTOperational_Helper)
gen_QVTOperational_ImperativeCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=QVTOperational_ImperativeCallExp)
gen_QVTOperational_Constructor_ImperativeOperation = Generalization(general=ImperativeOperation, specific=QVTOperational_Constructor)
gen_QVTOperational_ConstructorBody_OperationBody = Generalization(general=OperationBody, specific=QVTOperational_ConstructorBody)
gen_QVTOperational_ContextualProperty_Property = Generalization(general=Property_, specific=QVTOperational_ContextualProperty)
gen_QVTOperational_MappingCallExp_ImperativeCallExp = Generalization(general=ImperativeCallExp, specific=QVTOperational_MappingCallExp)
gen_QVTOperational_MappingOperation_ImperativeOperation = Generalization(general=ImperativeOperation, specific=QVTOperational_MappingOperation)
gen_QVTOperational_ImperativeCallExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=QVTOperational_ImperativeCallExp)
gen_QVTOperational_ImperativeOperation_Operation = Generalization(general=Operation, specific=QVTOperational_ImperativeOperation)
gen_QVTOperational_Library_Module = Generalization(general=Module, specific=QVTOperational_Library)
gen_QVTOperational_MappingBody_OperationBody = Generalization(general=OperationBody, specific=QVTOperational_MappingBody)
gen_QVTOperational_MappingParameter_VarParameter = Generalization(general=VarParameter, specific=QVTOperational_MappingParameter)
gen_QVTOperational_ModelParameter_VarParameter = Generalization(general=VarParameter, specific=QVTOperational_ModelParameter)
gen_QVTOperational_ModelType_Class = Generalization(general=Class_, specific=QVTOperational_ModelType)
gen_QVTOperational_ModuleImport_Element = Generalization(general=Element, specific=QVTOperational_ModuleImport)
gen_QVTOperational_Module_Class = Generalization(general=Class_, specific=QVTOperational_Module)
gen_QVTOperational_Module_Package = Generalization(general=Package, specific=QVTOperational_Module)
gen_QVTOperational_OperationalTransformation_Module = Generalization(general=Module, specific=QVTOperational_OperationalTransformation)
gen_QVTOperational_ObjectExp_InstantiationExp = Generalization(general=InstantiationExp, specific=QVTOperational_ObjectExp)
gen_QVTOperational_OperationBody_Element = Generalization(general=Element, specific=QVTOperational_OperationBody)
gen_QVTOperational_ResolveInExp_ResolveExp = Generalization(general=ResolveExp, specific=QVTOperational_ResolveInExp)
gen_QVTOperational_VarParameter_Variable = Generalization(general=Variable, specific=QVTOperational_VarParameter)
gen_QVTOperational_VarParameter_Parameter = Generalization(general=Parameter_, specific=QVTOperational_VarParameter)
gen_QVTOperational_ResolveExp_CallExp = Generalization(general=CallExp, specific=QVTOperational_ResolveExp)
gen_QVTOperational_ResolveExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=QVTOperational_ResolveExp)

# Domain Model
domain_model = DomainModel(
    name="QVTOperational",
    types={Comment, EMOF_Class, Type, Property_, Operation, Class_, EMOF_Comment, Element, NamedElement, EMOF_DataType, EMOF_Element, Object, Parameter_, EMOF_Package, EMOF_Enumeration, DataType, EnumerationLiteral, EMOF_EnumerationLiteral, Enumeration_, EMOF_Extent, EMOF_Factory, Package, EMOF_MultiplicityElement, EMOF_NamedElement, EMOF_Object, EMOF_Operation, TypedElement, MultiplicityElement, EMOF_Tag, EMOF_Type, EMOF_TypedElement, EMOF_Parameter, EMOF_PrimitiveType, EMOF_Property, EMOF_ReflectiveCollection, EMOF_ReflectiveSequence, ReflectiveCollection, EssentialOCL_CollectionLiteralPart, CollectionLiteralExp, EssentialOCL_CollectionRange, EMOF_URIExtent, Extent, EssentialOCL_AnyType, EssentialOCL_BagType, CollectionType, EssentialOCL_BooleanLiteralExp, PrimitiveLiteralExp, EssentialOCL_CallExp, OclExpression, EssentialOCL_CollectionItem, CollectionLiteralPart, EssentialOCL_CollectionLiteralExp, LiteralExp, EssentialOCL_FeatureCallExp, CallExp, EssentialOCL_IfExp, EssentialOCL_CollectionType, EssentialOCL_EnumLiteralExp, EssentialOCL_ExpressionInOcl, Variable, EssentialOCL_NavigationCallExp, FeatureCallExp, EssentialOCL_NullLiteralExp, EssentialOCL_NumericLiteralExp, EssentialOCL_OclExpression, EssentialOCL_OperationCallExp, EssentialOCL_IntegerLiteralExp, NumericLiteralExp, EssentialOCL_InvalidLiteralExp, EssentialOCL_InvalidType, EssentialOCL_IterateExp, LoopExp, EssentialOCL_IteratorExp, EssentialOCL_LetExp, EssentialOCL_LiteralExp, EssentialOCL_LoopExp, EssentialOCL_TupleLiteralPart, TupleLiteralExp, EssentialOCL_TupleType, EssentialOCL_OrderedSetType, EssentialOCL_PrimitiveLiteralExp, EssentialOCL_PropertyCallExp, NavigationCallExp, EssentialOCL_RealLiteralExp, EssentialOCL_SequenceType, EssentialOCL_SetType, EssentialOCL_StringLiteralExp, EssentialOCL_TemplateParameterType, EssentialOCL_TupleLiteralExp, TupleLiteralPart, Rule, TypedModel, QVTBase_Function, QVTBase_FunctionParameter, EssentialOCL_TypeExp, EssentialOCL_UnlimitedNaturalExp, EssentialOCL_Variable, LetExp, EssentialOCL_VariableExp, EssentialOCL_VoidType, QVTBase_Domain, Tag, QVTBase_TypedModel, QVTBase_Pattern, Predicate, QVTBase_Predicate, Pattern, QVTBase_Rule, Domain, Transformation, QVTBase_Transformation, QVTCore_BottomPattern, CorePattern, Area, Assignment, EnforcementOperation, QVTCore_Area, BottomPattern, GuardPattern, QVTCore_Assignment, Mapping, QVTCore_PropertyAssignment, RealizedVariable, QVTCore_CoreDomain, QVTCore_CorePattern, QVTCore_EnforcementOperation, OperationCallExp, QVTCore_GuardPattern, QVTCore_Mapping, QVTTemplate_ObjectTemplateExp, PropertyTemplateItem, QVTTemplate_PropertyTemplateItem, ObjectTemplateExp, QVTCore_RealizedVariable, QVTCore_VariableAssignment, QVTTemplate_CollectionTemplateExp, TemplateExp, RelationalTransformation, QVTRelation_OppositePropertyCallExp, PropertyCallExp, QVTRelation_Relation, QVTTemplate_TemplateExp, QVTRelation_DomainPattern, RelationDomain, QVTRelation_Key, QVTRelation_RelationDomainAssignment, QVTRelation_RelationImplementation, RelationImplementation, QVTRelation_RelationCallExp, Relation, QVTRelation_RelationDomain, RelationDomainAssignment, DomainPattern, ImperativeOCL_AssignExp, QVTRelation_RelationalTransformation, Key, ImperativeOCL_AltExp, ImperativeExpression, ImperativeOCL_AssertExp, LogExp, ImperativeOCL_ContinueExp, ImperativeOCL_DictLiteralExp, DictLiteralPart, ImperativeOCL_DictLiteralPart, ImperativeOCL_BlockExp, ImperativeOCL_BreakExp, ImperativeOCL_CatchExp, ImperativeOCL_ComputeExp, DictLiteralExp, ImperativeOCL_DictionaryType, ImperativeOCL_ForExp, ImperativeLoopExp, ImperativeOCL_ImperativeExpression, ImperativeOCL_ImperativeIterateExp, ImperativeOCL_ImperativeLoopExp, ImperativeOCL_InstantiationExp, ImperativeOCL_SwitchExp, AltExp, ImperativeOCL_ListLiteralExp, ImperativeOCL_ListType, ImperativeOCL_LogExp, ImperativeOCL_RaiseExp, ImperativeOCL_ReturnExp, ImperativeOCL_VariableInitExp, ImperativeOCL_WhileExp, ImperativeOCL_TryExp, CatchExp, ImperativeOCL_Typedef, ImperativeOCL_UnlinkExp, QVTOperational_EntryOperation, QVTOperational_Helper, QVTOperational_ImperativeCallExp, QVTOperational_Constructor, ImperativeOperation, QVTOperational_ConstructorBody, OperationBody, QVTOperational_ContextualProperty, QVTOperational_MappingCallExp, ImperativeCallExp, QVTOperational_MappingOperation, MappingOperation, QVTOperational_ImperativeOperation, VarParameter, QVTOperational_Library, Module, QVTOperational_MappingBody, QVTOperational_MappingParameter, ModelParameter, QVTOperational_ModelParameter, OperationalTransformation, QVTOperational_ModelType, ModelType, QVTOperational_ModuleImport, QVTOperational_Module, EntryOperation, ModuleImport, QVTOperational_OperationalTransformation, QVTOperational_ObjectExp, InstantiationExp, ConstructorBody, QVTOperational_OperationBody, QVTOperational_ResolveInExp, ResolveExp, QVTOperational_VarParameter, QVTOperational_ResolveExp, CollectionKind, EnforcementMode, SeverityKind, DirectionKind, ImportKind},
    associations={ownedComment5, ownedAttribute0, ownedOperation1, superClass3, annotatedElement4, class_9, ownedParameter11, raisedException12, nestedPackage13, nestingPackage15, ownedLiteral6, enumeration7, package8, element25, package26, type28, ownedType17, operation19, class_21, opposite23, part33, collectionLiteralExp34, first35, source30, item31, resultVariable54, condition57, elseExpression59, thenExpression62, last37, elementType40, referredEnumLiteral42, bodyExpression44, contextVariable46, generatedType48, parameterVariable51, iterator73, argument76, result65, in_67, variable69, body71, attribute84, tupleLiteralExp86, value88, referredOperation78, referredProperty81, part83, rule101, typedModel102, queryExpression103, referredType91, initExpression93, letExp95, representedParameter96, referredVariable99, extends116, modelParameter118, ownedTag120, rule122, bindsTo105, predicate107, conditionExpression108, pattern110, domain111, overrides112, transformation114, value137, area139, assignment140, enforcementOperation142, dependsOn125, transformation127, usedPackage129, bottomPattern132, guardPattern133, bottomPattern135, context153, local154, refinement156, specification158, slotExpression160, realizedVariable144, variable146, bottomPattern148, operationCallExp150, area151, part176, referredClass177, objContainer179, targetProperty162, bottomPattern165, targetVariable167, member169, referredCollectionType171, rest173, oppositePart196, part199, transformation202, referredProperty181, value183, bindsTo186, where188, relationDomain191, templateExpression193, identifies194, rootVariable218, owner220, valueExp222, variable224, operationalImpl203, variable204, when206, where209, argument212, referredRelation214, defaultAssignment216, pattern217, defaultValue245, left247, value250, impl227, inDirectionOf229, relation232, ownedKey234, body236, condition238, assertion241, log243, returnedElement265, part268, key269, body253, body255, exception257, exceptionVariable260, body263, argument282, extent284, instantiatedClass287, initializationOperation290, value271, partOwner274, keyType276, target278, condition280, alternativePart304, elsePart305, element293, condition295, argument297, exception299, value302, referredVariable322, body324, exceptClause308, tryBody309, base312, condition314, item317, target319, overridden334, condition326, context329, initExpression331, disjunct348, body337, context339, overridden340, result341, endSection343, initSection345, extent364, referredDomain365, module368, inherited349, merged352, refinedRelation355, when358, where361, ownedTag380, ownedVariable383, usedModelType386, additionalCondition370, metamodel372, configProperty375, entry377, moduleImport379, operation400, variable402, intermediateClass405, intermediateProperty407, binding388, importedModule390, module392, body394, referredObject395, content398, inMapping424, ctxOwner426, resOwner429, modelParameter410, refined413, relation416, condition419, target421},
    generalizations={gen_EMOF_Class_Type, gen_EMOF_Comment_Element, gen_EMOF_DataType_Type, gen_EMOF_Element_Object, gen_EMOF_Operation_MultiplicityElement, gen_EMOF_Package_NamedElement, gen_EMOF_Enumeration_DataType, gen_EMOF_EnumerationLiteral_NamedElement, gen_EMOF_Extent_Object, gen_EMOF_Factory_Element, gen_EMOF_NamedElement_Element, gen_EMOF_Operation_TypedElement, gen_EMOF_Tag_Element, gen_EMOF_Type_NamedElement, gen_EMOF_TypedElement_NamedElement, gen_EMOF_Parameter_TypedElement, gen_EMOF_Parameter_MultiplicityElement, gen_EMOF_PrimitiveType_DataType, gen_EMOF_Property_TypedElement, gen_EMOF_Property_MultiplicityElement, gen_EMOF_ReflectiveCollection_Object, gen_EMOF_ReflectiveSequence_ReflectiveCollection, gen_EssentialOCL_CollectionLiteralPart_TypedElement, gen_EssentialOCL_CollectionRange_CollectionLiteralPart, gen_EMOF_URIExtent_Extent, gen_EssentialOCL_AnyType_Type, gen_EssentialOCL_BagType_CollectionType, gen_EssentialOCL_BooleanLiteralExp_PrimitiveLiteralExp, gen_EssentialOCL_CallExp_OclExpression, gen_EssentialOCL_CollectionItem_CollectionLiteralPart, gen_EssentialOCL_CollectionLiteralExp_LiteralExp, gen_EssentialOCL_FeatureCallExp_CallExp, gen_EssentialOCL_IfExp_OclExpression, gen_EssentialOCL_CollectionType_DataType, gen_EssentialOCL_EnumLiteralExp_LiteralExp, gen_EssentialOCL_ExpressionInOcl_TypedElement, gen_EssentialOCL_NavigationCallExp_FeatureCallExp, gen_EssentialOCL_NullLiteralExp_LiteralExp, gen_EssentialOCL_NumericLiteralExp_PrimitiveLiteralExp, gen_EssentialOCL_OclExpression_TypedElement, gen_EssentialOCL_OperationCallExp_FeatureCallExp, gen_EssentialOCL_IntegerLiteralExp_NumericLiteralExp, gen_EssentialOCL_InvalidLiteralExp_LiteralExp, gen_EssentialOCL_InvalidType_Type, gen_EssentialOCL_IterateExp_LoopExp, gen_EssentialOCL_IteratorExp_LoopExp, gen_EssentialOCL_LetExp_OclExpression, gen_EssentialOCL_LiteralExp_OclExpression, gen_EssentialOCL_LoopExp_CallExp, gen_EssentialOCL_LoopExp_OclExpression, gen_EssentialOCL_TupleLiteralPart_TypedElement, gen_EssentialOCL_TupleType_Class, gen_EssentialOCL_TupleType_DataType, gen_EssentialOCL_OrderedSetType_CollectionType, gen_EssentialOCL_PrimitiveLiteralExp_LiteralExp, gen_EssentialOCL_PropertyCallExp_NavigationCallExp, gen_EssentialOCL_RealLiteralExp_NumericLiteralExp, gen_EssentialOCL_SequenceType_CollectionType, gen_EssentialOCL_SetType_CollectionType, gen_EssentialOCL_StringLiteralExp_PrimitiveLiteralExp, gen_EssentialOCL_TemplateParameterType_Type, gen_EssentialOCL_TupleLiteralExp_LiteralExp, gen_QVTBase_Function_Operation, gen_QVTBase_FunctionParameter_Variable, gen_EssentialOCL_TypeExp_OclExpression, gen_EssentialOCL_UnlimitedNaturalExp_NumericLiteralExp, gen_EssentialOCL_Variable_TypedElement, gen_EssentialOCL_VariableExp_OclExpression, gen_EssentialOCL_VoidType_Type, gen_QVTBase_Domain_NamedElement, gen_QVTBase_TypedModel_NamedElement, gen_QVTBase_FunctionParameter_Parameter, gen_QVTBase_Pattern_Element, gen_QVTBase_Predicate_Element, gen_QVTBase_Rule_NamedElement, gen_QVTBase_Transformation_Class, gen_QVTBase_Transformation_Package, gen_QVTCore_BottomPattern_CorePattern, gen_QVTCore_Assignment_Element, gen_QVTCore_PropertyAssignment_Assignment, gen_QVTCore_CoreDomain_Domain, gen_QVTCore_CoreDomain_Area, gen_QVTCore_CorePattern_Pattern, gen_QVTCore_EnforcementOperation_Element, gen_QVTCore_GuardPattern_CorePattern, gen_QVTCore_Mapping_Rule, gen_QVTCore_Mapping_Area, gen_QVTTemplate_ObjectTemplateExp_TemplateExp, gen_QVTTemplate_PropertyTemplateItem_Element, gen_QVTCore_RealizedVariable_Variable, gen_QVTCore_VariableAssignment_Assignment, gen_QVTTemplate_CollectionTemplateExp_TemplateExp, gen_QVTRelation_OppositePropertyCallExp_PropertyCallExp, gen_QVTRelation_Relation_Rule, gen_QVTTemplate_TemplateExp_LiteralExp, gen_QVTRelation_DomainPattern_Pattern, gen_QVTRelation_Key_Element, gen_QVTRelation_RelationDomainAssignment_Element, gen_QVTRelation_RelationImplementation_Element, gen_QVTRelation_RelationCallExp_OclExpression, gen_QVTRelation_RelationDomain_Domain, gen_ImperativeOCL_AssignExp_ImperativeExpression, gen_QVTRelation_RelationalTransformation_Transformation, gen_ImperativeOCL_AltExp_ImperativeExpression, gen_ImperativeOCL_AssertExp_ImperativeExpression, gen_ImperativeOCL_ContinueExp_ImperativeExpression, gen_ImperativeOCL_DictLiteralExp_LiteralExp, gen_ImperativeOCL_DictLiteralPart_Element, gen_ImperativeOCL_BlockExp_ImperativeExpression, gen_ImperativeOCL_BreakExp_ImperativeExpression, gen_ImperativeOCL_CatchExp_ImperativeExpression, gen_ImperativeOCL_ComputeExp_ImperativeExpression, gen_ImperativeOCL_DictionaryType_CollectionType, gen_ImperativeOCL_ForExp_ImperativeLoopExp, gen_ImperativeOCL_ImperativeExpression_OclExpression, gen_ImperativeOCL_ImperativeIterateExp_ImperativeLoopExp, gen_ImperativeOCL_ImperativeLoopExp_LoopExp, gen_ImperativeOCL_ImperativeLoopExp_ImperativeExpression, gen_ImperativeOCL_InstantiationExp_ImperativeExpression, gen_ImperativeOCL_SwitchExp_ImperativeExpression, gen_ImperativeOCL_ListLiteralExp_LiteralExp, gen_ImperativeOCL_ListType_CollectionType, gen_ImperativeOCL_LogExp_OperationCallExp, gen_ImperativeOCL_LogExp_ImperativeExpression, gen_ImperativeOCL_RaiseExp_ImperativeExpression, gen_ImperativeOCL_ReturnExp_ImperativeExpression, gen_ImperativeOCL_VariableInitExp_ImperativeExpression, gen_ImperativeOCL_WhileExp_ImperativeExpression, gen_ImperativeOCL_TryExp_ImperativeExpression, gen_ImperativeOCL_Typedef_Class, gen_ImperativeOCL_UnlinkExp_ImperativeExpression, gen_QVTOperational_EntryOperation_ImperativeOperation, gen_QVTOperational_Helper_ImperativeOperation, gen_QVTOperational_ImperativeCallExp_OperationCallExp, gen_QVTOperational_Constructor_ImperativeOperation, gen_QVTOperational_ConstructorBody_OperationBody, gen_QVTOperational_ContextualProperty_Property, gen_QVTOperational_MappingCallExp_ImperativeCallExp, gen_QVTOperational_MappingOperation_ImperativeOperation, gen_QVTOperational_ImperativeCallExp_ImperativeExpression, gen_QVTOperational_ImperativeOperation_Operation, gen_QVTOperational_Library_Module, gen_QVTOperational_MappingBody_OperationBody, gen_QVTOperational_MappingParameter_VarParameter, gen_QVTOperational_ModelParameter_VarParameter, gen_QVTOperational_ModelType_Class, gen_QVTOperational_ModuleImport_Element, gen_QVTOperational_Module_Class, gen_QVTOperational_Module_Package, gen_QVTOperational_OperationalTransformation_Module, gen_QVTOperational_ObjectExp_InstantiationExp, gen_QVTOperational_OperationBody_Element, gen_QVTOperational_ResolveInExp_ResolveExp, gen_QVTOperational_VarParameter_Variable, gen_QVTOperational_VarParameter_Parameter, gen_QVTOperational_ResolveExp_CallExp, gen_QVTOperational_ResolveExp_ImperativeExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)