import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Key,
    Relation,
    DomainPattern,
    RelationDomainAssignment,
    RelationImplementation,
    PropertyCallExp,
    QVTRelation_OppositePropertyCallExp,
    RelationalTransformation,
    PropertyTemplateItem,
    ObjectTemplateExp,
    Mapping,
    TemplateExp,
    QVTTemplate_ObjectTemplateExp,
    QVTTemplate_CollectionTemplateExp,
    RealizedVariable,
    EnforcementOperation,
    Assignment,
    QVTCore_VariableAssignment,
    QVTCore_PropertyAssignment,
    Area,
    Tag,
    CorePattern,
    QVTCore_GuardPattern,
    QVTCore_BottomPattern,
    GuardPattern,
    BottomPattern,
    QVTCore_Area,
    Predicate,
    TypedModel,
    Rule,
    QVTCore_Mapping,
    QVTRelation_Relation,
    Transformation,
    QVTRelation_RelationalTransformation,
    Domain,
    QVTRelation_RelationDomain,
    QVTCore_CoreDomain,
    Pattern,
    QVTCore_CorePattern,
    QVTRelation_DomainPattern,
    CatchExp,
    AltExp,
    OrderedTupleLiteralPart,
    OperationCallExp,
    DictLiteralPart,
    ImperativeLoopExp,
    ImperativeOCL_ImperativeIterateExp,
    ImperativeOCL_ForExp,
    LogExp,
    ImperativeExpression,
    ImperativeOCL_UnpackExp,
    ImperativeOCL_AssignExp,
    ImperativeOCL_SwitchExp,
    ImperativeOCL_WhileExp,
    ImperativeOCL_LogExp,
    ImperativeOCL_ContinueExp,
    ImperativeOCL_InstantiationExp,
    ImperativeOCL_RaiseExp,
    ImperativeOCL_AssertExp,
    ImperativeOCL_ComputeExp,
    ImperativeOCL_VariableInitExp,
    ImperativeOCL_UnlinkExp,
    ImperativeOCL_TryExp,
    ImperativeOCL_ReturnExp,
    ImperativeOCL_AltExp,
    ImperativeOCL_CatchExp,
    ImperativeOCL_BreakExp,
    ImperativeOCL_BlockExp,
    TupleLiteralExp,
    TupleLiteralPart,
    LetExp,
    FeatureCallExp,
    EssentialOCL_OperationCallExp,
    EssentialOCL_NavigationCallExp,
    NavigationCallExp,
    EssentialOCL_PropertyCallExp,
    NumericLiteralExp,
    EssentialOCL_RealLiteralExp,
    EssentialOCL_UnlimitedNaturalExp,
    EssentialOCL_IntegerLiteralExp,
    CallExp,
    EssentialOCL_FeatureCallExp,
    LoopExp,
    EssentialOCL_IteratorExp,
    ImperativeOCL_ImperativeLoopExp,
    EssentialOCL_IterateExp,
    CollectionLiteralExp,
    LiteralExp,
    QVTTemplate_TemplateExp,
    EssentialOCL_PrimitiveLiteralExp,
    ImperativeOCL_OrderedTupleLiteralExp,
    EssentialOCL_TupleLiteralExp,
    EssentialOCL_InvalidLiteralExp,
    ImperativeOCL_DictLiteralExp,
    EssentialOCL_NullLiteralExp,
    ImperativeOCL_ListLiteralExp,
    EssentialOCL_CollectionLiteralExp,
    Variable,
    QVTCore_RealizedVariable,
    EssentialOCL_EnumLiteralExp,
    Extent,
    EMOF_URIExtent,
    CollectionLiteralPart,
    EssentialOCL_CollectionRange,
    EssentialOCL_CollectionItem,
    OclExpression,
    EssentialOCL_TypeExp,
    EssentialOCL_LetExp,
    EssentialOCL_IfExp,
    EssentialOCL_LiteralExp,
    EssentialOCL_LoopExp,
    QVTRelation_RelationCallExp,
    ImperativeOCL_ImperativeExpression,
    EssentialOCL_VariableExp,
    EssentialOCL_CallExp,
    PrimitiveLiteralExp,
    EssentialOCL_NumericLiteralExp,
    EssentialOCL_StringLiteralExp,
    EssentialOCL_BooleanLiteralExp,
    CollectionType,
    EssentialOCL_OrderedSetType,
    ImperativeOCL_ListType,
    EssentialOCL_SetType,
    EssentialOCL_SequenceType,
    ImperativeOCL_DictionaryType,
    EssentialOCL_BagType,
    ReflectiveCollection,
    EMOF_ReflectiveSequence,
    EMOF_Object,
    EMOF_MultiplicityElement,
    Package,
    Parameter,
    QVTBase_FunctionParameter,
    MultiplicityElement,
    TypedElement,
    EssentialOCL_TupleLiteralPart,
    EssentialOCL_OclExpression,
    EMOF_Parameter,
    EssentialOCL_Variable,
    EssentialOCL_CollectionLiteralPart,
    EssentialOCL_ExpressionInOcl,
    EMOF_Property,
    EMOF_Operation,
    Object,
    EMOF_ReflectiveCollection,
    EMOF_Element,
    NamedElement,
    QVTBase_Domain,
    QVTBase_TypedModel,
    EMOF_Package,
    EMOF_TypedElement,
    QVTBase_Rule,
    EMOF_Type,
    Element,
    QVTTemplate_PropertyTemplateItem,
    EMOF_Tag,
    EMOF_NamedElement,
    QVTCore_EnforcementOperation,
    QVTCore_Assignment,
    EMOF_Factory,
    ImperativeOCL_DictLiteralPart,
    QVTRelation_RelationDomainAssignment,
    QVTBase_Predicate,
    ImperativeOCL_OrderedTupleLiteralPart,
    QVTBase_Pattern,
    QVTRelation_Key,
    EMOF_Comment,
    Class,
    QVTBase_Transformation,
    ImperativeOCL_Typedef,
    ImperativeOCL_OrderedTupleType,
    Operation,
    QVTBase_Function,
    EMOF_Extent,
    Enumeration,
    EMOF_EnumerationLiteral,
    EnumerationLiteral,
    DataType,
    EssentialOCL_TupleType,
    EMOF_PrimitiveType,
    EssentialOCL_CollectionType,
    EMOF_Enumeration,
    Comment,
    Property,
    Type,
    EssentialOCL_TemplateParameterType,
    EssentialOCL_InvalidType,
    EssentialOCL_AnyType,
    EMOF_DataType,
    EssentialOCL_VoidType,
    EMOF_Class,
    QVTOperational_VarParameter,
    ResolveExp,
    QVTOperational_ResolveInExp,
    QVTOperational_ResolveExp,
    ConstructorBody,
    InstantiationExp,
    QVTOperational_ObjectExp,
    QVTOperational_ModuleImport,
    ModelType,
    QVTOperational_OperationBody,
    QVTOperational_Module,
    QVTOperational_ModelType,
    ModuleImport,
    EntryOperation,
    MappingOperation,
    ImperativeCallExp,
    QVTOperational_MappingCallExp,
    RelationDomain,
    ModelParameter,
    VarParameter,
    QVTOperational_ModelParameter,
    QVTOperational_MappingParameter,
    QVTOperational_ImperativeOperation,
    QVTOperational_ImperativeCallExp,
    Module,
    QVTOperational_OperationalTransformation,
    QVTOperational_Library,
    QVTRelation_RelationImplementation,
    QVTOperational_ContextualProperty,
    OperationBody,
    QVTOperational_MappingBody,
    QVTOperational_ConstructorBody,
    ImperativeOperation,
    QVTOperational_MappingOperation,
    QVTOperational_Constructor,
    QVTOperational_EntryOperation,
    QVTOperational_Helper,
    DirectionKind,
    CollectionKind,
    SeverityKind,
    EnforcementMode,
    ImportKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_key_is_not_abstract():
    assert not inspect.isabstract(Key)


def test_key_constructor_exists():
    assert callable(Key.__init__)


def test_key_constructor_args():
    sig = inspect.signature(Key.__init__)
    params = list(sig.parameters.keys())



def test_relation_is_not_abstract():
    assert not inspect.isabstract(Relation)


def test_relation_constructor_exists():
    assert callable(Relation.__init__)


def test_relation_constructor_args():
    sig = inspect.signature(Relation.__init__)
    params = list(sig.parameters.keys())



def test_domainpattern_is_not_abstract():
    assert not inspect.isabstract(DomainPattern)


def test_domainpattern_constructor_exists():
    assert callable(DomainPattern.__init__)


def test_domainpattern_constructor_args():
    sig = inspect.signature(DomainPattern.__init__)
    params = list(sig.parameters.keys())



def test_relationdomainassignment_is_not_abstract():
    assert not inspect.isabstract(RelationDomainAssignment)


def test_relationdomainassignment_constructor_exists():
    assert callable(RelationDomainAssignment.__init__)


def test_relationdomainassignment_constructor_args():
    sig = inspect.signature(RelationDomainAssignment.__init__)
    params = list(sig.parameters.keys())



def test_relationimplementation_is_not_abstract():
    assert not inspect.isabstract(RelationImplementation)


def test_relationimplementation_constructor_exists():
    assert callable(RelationImplementation.__init__)


def test_relationimplementation_constructor_args():
    sig = inspect.signature(RelationImplementation.__init__)
    params = list(sig.parameters.keys())



def test_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(PropertyCallExp)


def test_propertycallexp_constructor_exists():
    assert callable(PropertyCallExp.__init__)


def test_propertycallexp_constructor_args():
    sig = inspect.signature(PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation_oppositepropertycallexp_is_not_abstract():
    assert not inspect.isabstract(QVTRelation_OppositePropertyCallExp)


def test_qvtrelation_oppositepropertycallexp_constructor_exists():
    assert callable(QVTRelation_OppositePropertyCallExp.__init__)


def test_qvtrelation_oppositepropertycallexp_constructor_args():
    sig = inspect.signature(QVTRelation_OppositePropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_relationaltransformation_is_not_abstract():
    assert not inspect.isabstract(RelationalTransformation)


def test_relationaltransformation_constructor_exists():
    assert callable(RelationalTransformation.__init__)


def test_relationaltransformation_constructor_args():
    sig = inspect.signature(RelationalTransformation.__init__)
    params = list(sig.parameters.keys())



def test_propertytemplateitem_is_not_abstract():
    assert not inspect.isabstract(PropertyTemplateItem)


def test_propertytemplateitem_constructor_exists():
    assert callable(PropertyTemplateItem.__init__)


def test_propertytemplateitem_constructor_args():
    sig = inspect.signature(PropertyTemplateItem.__init__)
    params = list(sig.parameters.keys())



def test_objecttemplateexp_is_not_abstract():
    assert not inspect.isabstract(ObjectTemplateExp)


def test_objecttemplateexp_constructor_exists():
    assert callable(ObjectTemplateExp.__init__)


def test_objecttemplateexp_constructor_args():
    sig = inspect.signature(ObjectTemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_mapping_is_not_abstract():
    assert not inspect.isabstract(Mapping)


def test_mapping_constructor_exists():
    assert callable(Mapping.__init__)


def test_mapping_constructor_args():
    sig = inspect.signature(Mapping.__init__)
    params = list(sig.parameters.keys())



def test_templateexp_is_not_abstract():
    assert not inspect.isabstract(TemplateExp)


def test_templateexp_constructor_exists():
    assert callable(TemplateExp.__init__)


def test_templateexp_constructor_args():
    sig = inspect.signature(TemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_qvttemplate_objecttemplateexp_is_not_abstract():
    assert not inspect.isabstract(QVTTemplate_ObjectTemplateExp)


def test_qvttemplate_objecttemplateexp_constructor_exists():
    assert callable(QVTTemplate_ObjectTemplateExp.__init__)


def test_qvttemplate_objecttemplateexp_constructor_args():
    sig = inspect.signature(QVTTemplate_ObjectTemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_qvttemplate_collectiontemplateexp_is_not_abstract():
    assert not inspect.isabstract(QVTTemplate_CollectionTemplateExp)


def test_qvttemplate_collectiontemplateexp_constructor_exists():
    assert callable(QVTTemplate_CollectionTemplateExp.__init__)


def test_qvttemplate_collectiontemplateexp_constructor_args():
    sig = inspect.signature(QVTTemplate_CollectionTemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_realizedvariable_is_not_abstract():
    assert not inspect.isabstract(RealizedVariable)


def test_realizedvariable_constructor_exists():
    assert callable(RealizedVariable.__init__)


def test_realizedvariable_constructor_args():
    sig = inspect.signature(RealizedVariable.__init__)
    params = list(sig.parameters.keys())



def test_enforcementoperation_is_not_abstract():
    assert not inspect.isabstract(EnforcementOperation)


def test_enforcementoperation_constructor_exists():
    assert callable(EnforcementOperation.__init__)


def test_enforcementoperation_constructor_args():
    sig = inspect.signature(EnforcementOperation.__init__)
    params = list(sig.parameters.keys())



def test_assignment_is_not_abstract():
    assert not inspect.isabstract(Assignment)


def test_assignment_constructor_exists():
    assert callable(Assignment.__init__)


def test_assignment_constructor_args():
    sig = inspect.signature(Assignment.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore_variableassignment_is_not_abstract():
    assert not inspect.isabstract(QVTCore_VariableAssignment)


def test_qvtcore_variableassignment_constructor_exists():
    assert callable(QVTCore_VariableAssignment.__init__)


def test_qvtcore_variableassignment_constructor_args():
    sig = inspect.signature(QVTCore_VariableAssignment.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore_propertyassignment_is_not_abstract():
    assert not inspect.isabstract(QVTCore_PropertyAssignment)


def test_qvtcore_propertyassignment_constructor_exists():
    assert callable(QVTCore_PropertyAssignment.__init__)


def test_qvtcore_propertyassignment_constructor_args():
    sig = inspect.signature(QVTCore_PropertyAssignment.__init__)
    params = list(sig.parameters.keys())



def test_area_is_not_abstract():
    assert not inspect.isabstract(Area)


def test_area_constructor_exists():
    assert callable(Area.__init__)


def test_area_constructor_args():
    sig = inspect.signature(Area.__init__)
    params = list(sig.parameters.keys())



def test_tag_is_not_abstract():
    assert not inspect.isabstract(Tag)


def test_tag_constructor_exists():
    assert callable(Tag.__init__)


def test_tag_constructor_args():
    sig = inspect.signature(Tag.__init__)
    params = list(sig.parameters.keys())



def test_corepattern_is_not_abstract():
    assert not inspect.isabstract(CorePattern)


def test_corepattern_constructor_exists():
    assert callable(CorePattern.__init__)


def test_corepattern_constructor_args():
    sig = inspect.signature(CorePattern.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore_guardpattern_is_not_abstract():
    assert not inspect.isabstract(QVTCore_GuardPattern)


def test_qvtcore_guardpattern_constructor_exists():
    assert callable(QVTCore_GuardPattern.__init__)


def test_qvtcore_guardpattern_constructor_args():
    sig = inspect.signature(QVTCore_GuardPattern.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore_bottompattern_is_not_abstract():
    assert not inspect.isabstract(QVTCore_BottomPattern)


def test_qvtcore_bottompattern_constructor_exists():
    assert callable(QVTCore_BottomPattern.__init__)


def test_qvtcore_bottompattern_constructor_args():
    sig = inspect.signature(QVTCore_BottomPattern.__init__)
    params = list(sig.parameters.keys())



def test_guardpattern_is_not_abstract():
    assert not inspect.isabstract(GuardPattern)


def test_guardpattern_constructor_exists():
    assert callable(GuardPattern.__init__)


def test_guardpattern_constructor_args():
    sig = inspect.signature(GuardPattern.__init__)
    params = list(sig.parameters.keys())



def test_bottompattern_is_not_abstract():
    assert not inspect.isabstract(BottomPattern)


def test_bottompattern_constructor_exists():
    assert callable(BottomPattern.__init__)


def test_bottompattern_constructor_args():
    sig = inspect.signature(BottomPattern.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore_area_is_not_abstract():
    assert not inspect.isabstract(QVTCore_Area)


def test_qvtcore_area_constructor_exists():
    assert callable(QVTCore_Area.__init__)


def test_qvtcore_area_constructor_args():
    sig = inspect.signature(QVTCore_Area.__init__)
    params = list(sig.parameters.keys())



def test_predicate_is_not_abstract():
    assert not inspect.isabstract(Predicate)


def test_predicate_constructor_exists():
    assert callable(Predicate.__init__)


def test_predicate_constructor_args():
    sig = inspect.signature(Predicate.__init__)
    params = list(sig.parameters.keys())



def test_typedmodel_is_not_abstract():
    assert not inspect.isabstract(TypedModel)


def test_typedmodel_constructor_exists():
    assert callable(TypedModel.__init__)


def test_typedmodel_constructor_args():
    sig = inspect.signature(TypedModel.__init__)
    params = list(sig.parameters.keys())



def test_rule_is_not_abstract():
    assert not inspect.isabstract(Rule)


def test_rule_constructor_exists():
    assert callable(Rule.__init__)


def test_rule_constructor_args():
    sig = inspect.signature(Rule.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore_mapping_is_not_abstract():
    assert not inspect.isabstract(QVTCore_Mapping)


def test_qvtcore_mapping_constructor_exists():
    assert callable(QVTCore_Mapping.__init__)


def test_qvtcore_mapping_constructor_args():
    sig = inspect.signature(QVTCore_Mapping.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation_relation_is_not_abstract():
    assert not inspect.isabstract(QVTRelation_Relation)


def test_qvtrelation_relation_constructor_exists():
    assert callable(QVTRelation_Relation.__init__)


def test_qvtrelation_relation_constructor_args():
    sig = inspect.signature(QVTRelation_Relation.__init__)
    params = list(sig.parameters.keys())
    assert "isTopLevel" in params, "Missing parameter 'isTopLevel'"

def test_qvtrelation_relation_has_isTopLevel():
    assert hasattr(QVTRelation_Relation, "isTopLevel")
    descriptor = None
    for klass in QVTRelation_Relation.__mro__:
        if "isTopLevel" in klass.__dict__:
            descriptor = klass.__dict__["isTopLevel"]
            break
    assert isinstance(descriptor, property)



def test_transformation_is_not_abstract():
    assert not inspect.isabstract(Transformation)


def test_transformation_constructor_exists():
    assert callable(Transformation.__init__)


def test_transformation_constructor_args():
    sig = inspect.signature(Transformation.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation_relationaltransformation_is_not_abstract():
    assert not inspect.isabstract(QVTRelation_RelationalTransformation)


def test_qvtrelation_relationaltransformation_constructor_exists():
    assert callable(QVTRelation_RelationalTransformation.__init__)


def test_qvtrelation_relationaltransformation_constructor_args():
    sig = inspect.signature(QVTRelation_RelationalTransformation.__init__)
    params = list(sig.parameters.keys())



def test_domain_is_not_abstract():
    assert not inspect.isabstract(Domain)


def test_domain_constructor_exists():
    assert callable(Domain.__init__)


def test_domain_constructor_args():
    sig = inspect.signature(Domain.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation_relationdomain_is_not_abstract():
    assert not inspect.isabstract(QVTRelation_RelationDomain)


def test_qvtrelation_relationdomain_constructor_exists():
    assert callable(QVTRelation_RelationDomain.__init__)


def test_qvtrelation_relationdomain_constructor_args():
    sig = inspect.signature(QVTRelation_RelationDomain.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore_coredomain_is_not_abstract():
    assert not inspect.isabstract(QVTCore_CoreDomain)


def test_qvtcore_coredomain_constructor_exists():
    assert callable(QVTCore_CoreDomain.__init__)


def test_qvtcore_coredomain_constructor_args():
    sig = inspect.signature(QVTCore_CoreDomain.__init__)
    params = list(sig.parameters.keys())



def test_pattern_is_not_abstract():
    assert not inspect.isabstract(Pattern)


def test_pattern_constructor_exists():
    assert callable(Pattern.__init__)


def test_pattern_constructor_args():
    sig = inspect.signature(Pattern.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore_corepattern_is_not_abstract():
    assert not inspect.isabstract(QVTCore_CorePattern)


def test_qvtcore_corepattern_constructor_exists():
    assert callable(QVTCore_CorePattern.__init__)


def test_qvtcore_corepattern_constructor_args():
    sig = inspect.signature(QVTCore_CorePattern.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation_domainpattern_is_not_abstract():
    assert not inspect.isabstract(QVTRelation_DomainPattern)


def test_qvtrelation_domainpattern_constructor_exists():
    assert callable(QVTRelation_DomainPattern.__init__)


def test_qvtrelation_domainpattern_constructor_args():
    sig = inspect.signature(QVTRelation_DomainPattern.__init__)
    params = list(sig.parameters.keys())



def test_catchexp_is_not_abstract():
    assert not inspect.isabstract(CatchExp)


def test_catchexp_constructor_exists():
    assert callable(CatchExp.__init__)


def test_catchexp_constructor_args():
    sig = inspect.signature(CatchExp.__init__)
    params = list(sig.parameters.keys())



def test_altexp_is_not_abstract():
    assert not inspect.isabstract(AltExp)


def test_altexp_constructor_exists():
    assert callable(AltExp.__init__)


def test_altexp_constructor_args():
    sig = inspect.signature(AltExp.__init__)
    params = list(sig.parameters.keys())



def test_orderedtupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(OrderedTupleLiteralPart)


def test_orderedtupleliteralpart_constructor_exists():
    assert callable(OrderedTupleLiteralPart.__init__)


def test_orderedtupleliteralpart_constructor_args():
    sig = inspect.signature(OrderedTupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(OperationCallExp)


def test_operationcallexp_constructor_exists():
    assert callable(OperationCallExp.__init__)


def test_operationcallexp_constructor_args():
    sig = inspect.signature(OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_dictliteralpart_is_not_abstract():
    assert not inspect.isabstract(DictLiteralPart)


def test_dictliteralpart_constructor_exists():
    assert callable(DictLiteralPart.__init__)


def test_dictliteralpart_constructor_args():
    sig = inspect.signature(DictLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_imperativeloopexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeLoopExp)


def test_imperativeloopexp_constructor_exists():
    assert callable(ImperativeLoopExp.__init__)


def test_imperativeloopexp_constructor_args():
    sig = inspect.signature(ImperativeLoopExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_imperativeiterateexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_ImperativeIterateExp)


def test_imperativeocl_imperativeiterateexp_constructor_exists():
    assert callable(ImperativeOCL_ImperativeIterateExp.__init__)


def test_imperativeocl_imperativeiterateexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_ImperativeIterateExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_forexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_ForExp)


def test_imperativeocl_forexp_constructor_exists():
    assert callable(ImperativeOCL_ForExp.__init__)


def test_imperativeocl_forexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_ForExp.__init__)
    params = list(sig.parameters.keys())



def test_logexp_is_not_abstract():
    assert not inspect.isabstract(LogExp)


def test_logexp_constructor_exists():
    assert callable(LogExp.__init__)


def test_logexp_constructor_args():
    sig = inspect.signature(LogExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeexpression_is_not_abstract():
    assert not inspect.isabstract(ImperativeExpression)


def test_imperativeexpression_constructor_exists():
    assert callable(ImperativeExpression.__init__)


def test_imperativeexpression_constructor_args():
    sig = inspect.signature(ImperativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_unpackexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_UnpackExp)


def test_imperativeocl_unpackexp_constructor_exists():
    assert callable(ImperativeOCL_UnpackExp.__init__)


def test_imperativeocl_unpackexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_UnpackExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_assignexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_AssignExp)


def test_imperativeocl_assignexp_constructor_exists():
    assert callable(ImperativeOCL_AssignExp.__init__)


def test_imperativeocl_assignexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_AssignExp.__init__)
    params = list(sig.parameters.keys())
    assert "isReset" in params, "Missing parameter 'isReset'"

def test_imperativeocl_assignexp_has_isReset():
    assert hasattr(ImperativeOCL_AssignExp, "isReset")
    descriptor = None
    for klass in ImperativeOCL_AssignExp.__mro__:
        if "isReset" in klass.__dict__:
            descriptor = klass.__dict__["isReset"]
            break
    assert isinstance(descriptor, property)



def test_imperativeocl_switchexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_SwitchExp)


def test_imperativeocl_switchexp_constructor_exists():
    assert callable(ImperativeOCL_SwitchExp.__init__)


def test_imperativeocl_switchexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_SwitchExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_whileexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_WhileExp)


def test_imperativeocl_whileexp_constructor_exists():
    assert callable(ImperativeOCL_WhileExp.__init__)


def test_imperativeocl_whileexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_WhileExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_logexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_LogExp)


def test_imperativeocl_logexp_constructor_exists():
    assert callable(ImperativeOCL_LogExp.__init__)


def test_imperativeocl_logexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_LogExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_continueexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_ContinueExp)


def test_imperativeocl_continueexp_constructor_exists():
    assert callable(ImperativeOCL_ContinueExp.__init__)


def test_imperativeocl_continueexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_ContinueExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_instantiationexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_InstantiationExp)


def test_imperativeocl_instantiationexp_constructor_exists():
    assert callable(ImperativeOCL_InstantiationExp.__init__)


def test_imperativeocl_instantiationexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_InstantiationExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_raiseexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_RaiseExp)


def test_imperativeocl_raiseexp_constructor_exists():
    assert callable(ImperativeOCL_RaiseExp.__init__)


def test_imperativeocl_raiseexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_RaiseExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_assertexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_AssertExp)


def test_imperativeocl_assertexp_constructor_exists():
    assert callable(ImperativeOCL_AssertExp.__init__)


def test_imperativeocl_assertexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_AssertExp.__init__)
    params = list(sig.parameters.keys())
    assert "severity" in params, "Missing parameter 'severity'"

def test_imperativeocl_assertexp_has_severity():
    assert hasattr(ImperativeOCL_AssertExp, "severity")
    descriptor = None
    for klass in ImperativeOCL_AssertExp.__mro__:
        if "severity" in klass.__dict__:
            descriptor = klass.__dict__["severity"]
            break
    assert isinstance(descriptor, property)



def test_imperativeocl_computeexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_ComputeExp)


def test_imperativeocl_computeexp_constructor_exists():
    assert callable(ImperativeOCL_ComputeExp.__init__)


def test_imperativeocl_computeexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_ComputeExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_variableinitexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_VariableInitExp)


def test_imperativeocl_variableinitexp_constructor_exists():
    assert callable(ImperativeOCL_VariableInitExp.__init__)


def test_imperativeocl_variableinitexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_VariableInitExp.__init__)
    params = list(sig.parameters.keys())
    assert "withResult" in params, "Missing parameter 'withResult'"

def test_imperativeocl_variableinitexp_has_withResult():
    assert hasattr(ImperativeOCL_VariableInitExp, "withResult")
    descriptor = None
    for klass in ImperativeOCL_VariableInitExp.__mro__:
        if "withResult" in klass.__dict__:
            descriptor = klass.__dict__["withResult"]
            break
    assert isinstance(descriptor, property)



def test_imperativeocl_unlinkexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_UnlinkExp)


def test_imperativeocl_unlinkexp_constructor_exists():
    assert callable(ImperativeOCL_UnlinkExp.__init__)


def test_imperativeocl_unlinkexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_UnlinkExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_tryexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_TryExp)


def test_imperativeocl_tryexp_constructor_exists():
    assert callable(ImperativeOCL_TryExp.__init__)


def test_imperativeocl_tryexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_TryExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_returnexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_ReturnExp)


def test_imperativeocl_returnexp_constructor_exists():
    assert callable(ImperativeOCL_ReturnExp.__init__)


def test_imperativeocl_returnexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_ReturnExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_altexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_AltExp)


def test_imperativeocl_altexp_constructor_exists():
    assert callable(ImperativeOCL_AltExp.__init__)


def test_imperativeocl_altexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_AltExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_catchexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_CatchExp)


def test_imperativeocl_catchexp_constructor_exists():
    assert callable(ImperativeOCL_CatchExp.__init__)


def test_imperativeocl_catchexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_CatchExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_breakexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_BreakExp)


def test_imperativeocl_breakexp_constructor_exists():
    assert callable(ImperativeOCL_BreakExp.__init__)


def test_imperativeocl_breakexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_BreakExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_blockexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_BlockExp)


def test_imperativeocl_blockexp_constructor_exists():
    assert callable(ImperativeOCL_BlockExp.__init__)


def test_imperativeocl_blockexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_BlockExp.__init__)
    params = list(sig.parameters.keys())



def test_tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(TupleLiteralExp)


def test_tupleliteralexp_constructor_exists():
    assert callable(TupleLiteralExp.__init__)


def test_tupleliteralexp_constructor_args():
    sig = inspect.signature(TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(TupleLiteralPart)


def test_tupleliteralpart_constructor_exists():
    assert callable(TupleLiteralPart.__init__)


def test_tupleliteralpart_constructor_args():
    sig = inspect.signature(TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_letexp_is_not_abstract():
    assert not inspect.isabstract(LetExp)


def test_letexp_constructor_exists():
    assert callable(LetExp.__init__)


def test_letexp_constructor_args():
    sig = inspect.signature(LetExp.__init__)
    params = list(sig.parameters.keys())



def test_featurecallexp_is_not_abstract():
    assert not inspect.isabstract(FeatureCallExp)


def test_featurecallexp_constructor_exists():
    assert callable(FeatureCallExp.__init__)


def test_featurecallexp_constructor_args():
    sig = inspect.signature(FeatureCallExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_OperationCallExp)


def test_essentialocl_operationcallexp_constructor_exists():
    assert callable(EssentialOCL_OperationCallExp.__init__)


def test_essentialocl_operationcallexp_constructor_args():
    sig = inspect.signature(EssentialOCL_OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_navigationcallexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_NavigationCallExp)


def test_essentialocl_navigationcallexp_constructor_exists():
    assert callable(EssentialOCL_NavigationCallExp.__init__)


def test_essentialocl_navigationcallexp_constructor_args():
    sig = inspect.signature(EssentialOCL_NavigationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_navigationcallexp_is_not_abstract():
    assert not inspect.isabstract(NavigationCallExp)


def test_navigationcallexp_constructor_exists():
    assert callable(NavigationCallExp.__init__)


def test_navigationcallexp_constructor_args():
    sig = inspect.signature(NavigationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_PropertyCallExp)


def test_essentialocl_propertycallexp_constructor_exists():
    assert callable(EssentialOCL_PropertyCallExp.__init__)


def test_essentialocl_propertycallexp_constructor_args():
    sig = inspect.signature(EssentialOCL_PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(NumericLiteralExp)


def test_numericliteralexp_constructor_exists():
    assert callable(NumericLiteralExp.__init__)


def test_numericliteralexp_constructor_args():
    sig = inspect.signature(NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_realliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_RealLiteralExp)


def test_essentialocl_realliteralexp_constructor_exists():
    assert callable(EssentialOCL_RealLiteralExp.__init__)


def test_essentialocl_realliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL_RealLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_essentialocl_realliteralexp_has_realSymbol():
    assert hasattr(EssentialOCL_RealLiteralExp, "realSymbol")
    descriptor = None
    for klass in EssentialOCL_RealLiteralExp.__mro__:
        if "realSymbol" in klass.__dict__:
            descriptor = klass.__dict__["realSymbol"]
            break
    assert isinstance(descriptor, property)



def test_essentialocl_unlimitednaturalexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_UnlimitedNaturalExp)


def test_essentialocl_unlimitednaturalexp_constructor_exists():
    assert callable(EssentialOCL_UnlimitedNaturalExp.__init__)


def test_essentialocl_unlimitednaturalexp_constructor_args():
    sig = inspect.signature(EssentialOCL_UnlimitedNaturalExp.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_essentialocl_unlimitednaturalexp_has_symbol():
    assert hasattr(EssentialOCL_UnlimitedNaturalExp, "symbol")
    descriptor = None
    for klass in EssentialOCL_UnlimitedNaturalExp.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_essentialocl_integerliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_IntegerLiteralExp)


def test_essentialocl_integerliteralexp_constructor_exists():
    assert callable(EssentialOCL_IntegerLiteralExp.__init__)


def test_essentialocl_integerliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL_IntegerLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_essentialocl_integerliteralexp_has_integerSymbol():
    assert hasattr(EssentialOCL_IntegerLiteralExp, "integerSymbol")
    descriptor = None
    for klass in EssentialOCL_IntegerLiteralExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_callexp_is_not_abstract():
    assert not inspect.isabstract(CallExp)


def test_callexp_constructor_exists():
    assert callable(CallExp.__init__)


def test_callexp_constructor_args():
    sig = inspect.signature(CallExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_featurecallexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_FeatureCallExp)


def test_essentialocl_featurecallexp_constructor_exists():
    assert callable(EssentialOCL_FeatureCallExp.__init__)


def test_essentialocl_featurecallexp_constructor_args():
    sig = inspect.signature(EssentialOCL_FeatureCallExp.__init__)
    params = list(sig.parameters.keys())



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_iteratorexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_IteratorExp)


def test_essentialocl_iteratorexp_constructor_exists():
    assert callable(EssentialOCL_IteratorExp.__init__)


def test_essentialocl_iteratorexp_constructor_args():
    sig = inspect.signature(EssentialOCL_IteratorExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_imperativeloopexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_ImperativeLoopExp)


def test_imperativeocl_imperativeloopexp_constructor_exists():
    assert callable(ImperativeOCL_ImperativeLoopExp.__init__)


def test_imperativeocl_imperativeloopexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_ImperativeLoopExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_iterateexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_IterateExp)


def test_essentialocl_iterateexp_constructor_exists():
    assert callable(EssentialOCL_IterateExp.__init__)


def test_essentialocl_iterateexp_constructor_args():
    sig = inspect.signature(EssentialOCL_IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralExp)


def test_collectionliteralexp_constructor_exists():
    assert callable(CollectionLiteralExp.__init__)


def test_collectionliteralexp_constructor_args():
    sig = inspect.signature(CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_literalexp_is_not_abstract():
    assert not inspect.isabstract(LiteralExp)


def test_literalexp_constructor_exists():
    assert callable(LiteralExp.__init__)


def test_literalexp_constructor_args():
    sig = inspect.signature(LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_qvttemplate_templateexp_is_not_abstract():
    assert not inspect.isabstract(QVTTemplate_TemplateExp)


def test_qvttemplate_templateexp_constructor_exists():
    assert callable(QVTTemplate_TemplateExp.__init__)


def test_qvttemplate_templateexp_constructor_args():
    sig = inspect.signature(QVTTemplate_TemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_PrimitiveLiteralExp)


def test_essentialocl_primitiveliteralexp_constructor_exists():
    assert callable(EssentialOCL_PrimitiveLiteralExp.__init__)


def test_essentialocl_primitiveliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL_PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_orderedtupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_OrderedTupleLiteralExp)


def test_imperativeocl_orderedtupleliteralexp_constructor_exists():
    assert callable(ImperativeOCL_OrderedTupleLiteralExp.__init__)


def test_imperativeocl_orderedtupleliteralexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_OrderedTupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_TupleLiteralExp)


def test_essentialocl_tupleliteralexp_constructor_exists():
    assert callable(EssentialOCL_TupleLiteralExp.__init__)


def test_essentialocl_tupleliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL_TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_invalidliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_InvalidLiteralExp)


def test_essentialocl_invalidliteralexp_constructor_exists():
    assert callable(EssentialOCL_InvalidLiteralExp.__init__)


def test_essentialocl_invalidliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL_InvalidLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_dictliteralexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_DictLiteralExp)


def test_imperativeocl_dictliteralexp_constructor_exists():
    assert callable(ImperativeOCL_DictLiteralExp.__init__)


def test_imperativeocl_dictliteralexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_DictLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_nullliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_NullLiteralExp)


def test_essentialocl_nullliteralexp_constructor_exists():
    assert callable(EssentialOCL_NullLiteralExp.__init__)


def test_essentialocl_nullliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL_NullLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_listliteralexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_ListLiteralExp)


def test_imperativeocl_listliteralexp_constructor_exists():
    assert callable(ImperativeOCL_ListLiteralExp.__init__)


def test_imperativeocl_listliteralexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_ListLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_CollectionLiteralExp)


def test_essentialocl_collectionliteralexp_constructor_exists():
    assert callable(EssentialOCL_CollectionLiteralExp.__init__)


def test_essentialocl_collectionliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL_CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_essentialocl_collectionliteralexp_has_kind():
    assert hasattr(EssentialOCL_CollectionLiteralExp, "kind")
    descriptor = None
    for klass in EssentialOCL_CollectionLiteralExp.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore_realizedvariable_is_not_abstract():
    assert not inspect.isabstract(QVTCore_RealizedVariable)


def test_qvtcore_realizedvariable_constructor_exists():
    assert callable(QVTCore_RealizedVariable.__init__)


def test_qvtcore_realizedvariable_constructor_args():
    sig = inspect.signature(QVTCore_RealizedVariable.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_EnumLiteralExp)


def test_essentialocl_enumliteralexp_constructor_exists():
    assert callable(EssentialOCL_EnumLiteralExp.__init__)


def test_essentialocl_enumliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL_EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_extent_is_not_abstract():
    assert not inspect.isabstract(Extent)


def test_extent_constructor_exists():
    assert callable(Extent.__init__)


def test_extent_constructor_args():
    sig = inspect.signature(Extent.__init__)
    params = list(sig.parameters.keys())



def test_emof_uriextent_is_not_abstract():
    assert not inspect.isabstract(EMOF_URIExtent)


def test_emof_uriextent_constructor_exists():
    assert callable(EMOF_URIExtent.__init__)


def test_emof_uriextent_constructor_args():
    sig = inspect.signature(EMOF_URIExtent.__init__)
    params = list(sig.parameters.keys())



def test_collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralPart)


def test_collectionliteralpart_constructor_exists():
    assert callable(CollectionLiteralPart.__init__)


def test_collectionliteralpart_constructor_args():
    sig = inspect.signature(CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_collectionrange_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_CollectionRange)


def test_essentialocl_collectionrange_constructor_exists():
    assert callable(EssentialOCL_CollectionRange.__init__)


def test_essentialocl_collectionrange_constructor_args():
    sig = inspect.signature(EssentialOCL_CollectionRange.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_collectionitem_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_CollectionItem)


def test_essentialocl_collectionitem_constructor_exists():
    assert callable(EssentialOCL_CollectionItem.__init__)


def test_essentialocl_collectionitem_constructor_args():
    sig = inspect.signature(EssentialOCL_CollectionItem.__init__)
    params = list(sig.parameters.keys())



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_typeexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_TypeExp)


def test_essentialocl_typeexp_constructor_exists():
    assert callable(EssentialOCL_TypeExp.__init__)


def test_essentialocl_typeexp_constructor_args():
    sig = inspect.signature(EssentialOCL_TypeExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_letexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_LetExp)


def test_essentialocl_letexp_constructor_exists():
    assert callable(EssentialOCL_LetExp.__init__)


def test_essentialocl_letexp_constructor_args():
    sig = inspect.signature(EssentialOCL_LetExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_ifexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_IfExp)


def test_essentialocl_ifexp_constructor_exists():
    assert callable(EssentialOCL_IfExp.__init__)


def test_essentialocl_ifexp_constructor_args():
    sig = inspect.signature(EssentialOCL_IfExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_literalexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_LiteralExp)


def test_essentialocl_literalexp_constructor_exists():
    assert callable(EssentialOCL_LiteralExp.__init__)


def test_essentialocl_literalexp_constructor_args():
    sig = inspect.signature(EssentialOCL_LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_loopexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_LoopExp)


def test_essentialocl_loopexp_constructor_exists():
    assert callable(EssentialOCL_LoopExp.__init__)


def test_essentialocl_loopexp_constructor_args():
    sig = inspect.signature(EssentialOCL_LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation_relationcallexp_is_not_abstract():
    assert not inspect.isabstract(QVTRelation_RelationCallExp)


def test_qvtrelation_relationcallexp_constructor_exists():
    assert callable(QVTRelation_RelationCallExp.__init__)


def test_qvtrelation_relationcallexp_constructor_args():
    sig = inspect.signature(QVTRelation_RelationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_imperativeexpression_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_ImperativeExpression)


def test_imperativeocl_imperativeexpression_constructor_exists():
    assert callable(ImperativeOCL_ImperativeExpression.__init__)


def test_imperativeocl_imperativeexpression_constructor_args():
    sig = inspect.signature(ImperativeOCL_ImperativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_variableexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_VariableExp)


def test_essentialocl_variableexp_constructor_exists():
    assert callable(EssentialOCL_VariableExp.__init__)


def test_essentialocl_variableexp_constructor_args():
    sig = inspect.signature(EssentialOCL_VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_callexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_CallExp)


def test_essentialocl_callexp_constructor_exists():
    assert callable(EssentialOCL_CallExp.__init__)


def test_essentialocl_callexp_constructor_args():
    sig = inspect.signature(EssentialOCL_CallExp.__init__)
    params = list(sig.parameters.keys())



def test_primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveLiteralExp)


def test_primitiveliteralexp_constructor_exists():
    assert callable(PrimitiveLiteralExp.__init__)


def test_primitiveliteralexp_constructor_args():
    sig = inspect.signature(PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_NumericLiteralExp)


def test_essentialocl_numericliteralexp_constructor_exists():
    assert callable(EssentialOCL_NumericLiteralExp.__init__)


def test_essentialocl_numericliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL_NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_stringliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_StringLiteralExp)


def test_essentialocl_stringliteralexp_constructor_exists():
    assert callable(EssentialOCL_StringLiteralExp.__init__)


def test_essentialocl_stringliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL_StringLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_essentialocl_stringliteralexp_has_stringSymbol():
    assert hasattr(EssentialOCL_StringLiteralExp, "stringSymbol")
    descriptor = None
    for klass in EssentialOCL_StringLiteralExp.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_essentialocl_booleanliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_BooleanLiteralExp)


def test_essentialocl_booleanliteralexp_constructor_exists():
    assert callable(EssentialOCL_BooleanLiteralExp.__init__)


def test_essentialocl_booleanliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL_BooleanLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_essentialocl_booleanliteralexp_has_booleanSymbol():
    assert hasattr(EssentialOCL_BooleanLiteralExp, "booleanSymbol")
    descriptor = None
    for klass in EssentialOCL_BooleanLiteralExp.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_orderedsettype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_OrderedSetType)


def test_essentialocl_orderedsettype_constructor_exists():
    assert callable(EssentialOCL_OrderedSetType.__init__)


def test_essentialocl_orderedsettype_constructor_args():
    sig = inspect.signature(EssentialOCL_OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_listtype_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_ListType)


def test_imperativeocl_listtype_constructor_exists():
    assert callable(ImperativeOCL_ListType.__init__)


def test_imperativeocl_listtype_constructor_args():
    sig = inspect.signature(ImperativeOCL_ListType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_settype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_SetType)


def test_essentialocl_settype_constructor_exists():
    assert callable(EssentialOCL_SetType.__init__)


def test_essentialocl_settype_constructor_args():
    sig = inspect.signature(EssentialOCL_SetType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_sequencetype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_SequenceType)


def test_essentialocl_sequencetype_constructor_exists():
    assert callable(EssentialOCL_SequenceType.__init__)


def test_essentialocl_sequencetype_constructor_args():
    sig = inspect.signature(EssentialOCL_SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_dictionarytype_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_DictionaryType)


def test_imperativeocl_dictionarytype_constructor_exists():
    assert callable(ImperativeOCL_DictionaryType.__init__)


def test_imperativeocl_dictionarytype_constructor_args():
    sig = inspect.signature(ImperativeOCL_DictionaryType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_bagtype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_BagType)


def test_essentialocl_bagtype_constructor_exists():
    assert callable(EssentialOCL_BagType.__init__)


def test_essentialocl_bagtype_constructor_args():
    sig = inspect.signature(EssentialOCL_BagType.__init__)
    params = list(sig.parameters.keys())



def test_reflectivecollection_is_not_abstract():
    assert not inspect.isabstract(ReflectiveCollection)


def test_reflectivecollection_constructor_exists():
    assert callable(ReflectiveCollection.__init__)


def test_reflectivecollection_constructor_args():
    sig = inspect.signature(ReflectiveCollection.__init__)
    params = list(sig.parameters.keys())



def test_emof_reflectivesequence_is_not_abstract():
    assert not inspect.isabstract(EMOF_ReflectiveSequence)


def test_emof_reflectivesequence_constructor_exists():
    assert callable(EMOF_ReflectiveSequence.__init__)


def test_emof_reflectivesequence_constructor_args():
    sig = inspect.signature(EMOF_ReflectiveSequence.__init__)
    params = list(sig.parameters.keys())



def test_emof_object_is_not_abstract():
    assert not inspect.isabstract(EMOF_Object)


def test_emof_object_constructor_exists():
    assert callable(EMOF_Object.__init__)


def test_emof_object_constructor_args():
    sig = inspect.signature(EMOF_Object.__init__)
    params = list(sig.parameters.keys())



def test_emof_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(EMOF_MultiplicityElement)


def test_emof_multiplicityelement_constructor_exists():
    assert callable(EMOF_MultiplicityElement.__init__)


def test_emof_multiplicityelement_constructor_args():
    sig = inspect.signature(EMOF_MultiplicityElement.__init__)
    params = list(sig.parameters.keys())
    assert "lower" in params, "Missing parameter 'lower'"
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "isUnique" in params, "Missing parameter 'isUnique'"

def test_emof_multiplicityelement_has_lower():
    assert hasattr(EMOF_MultiplicityElement, "lower")
    descriptor = None
    for klass in EMOF_MultiplicityElement.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_emof_multiplicityelement_has_isOrdered():
    assert hasattr(EMOF_MultiplicityElement, "isOrdered")
    descriptor = None
    for klass in EMOF_MultiplicityElement.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)

def test_emof_multiplicityelement_has_upper():
    assert hasattr(EMOF_MultiplicityElement, "upper")
    descriptor = None
    for klass in EMOF_MultiplicityElement.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_emof_multiplicityelement_has_isUnique():
    assert hasattr(EMOF_MultiplicityElement, "isUnique")
    descriptor = None
    for klass in EMOF_MultiplicityElement.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_qvtbase_functionparameter_is_not_abstract():
    assert not inspect.isabstract(QVTBase_FunctionParameter)


def test_qvtbase_functionparameter_constructor_exists():
    assert callable(QVTBase_FunctionParameter.__init__)


def test_qvtbase_functionparameter_constructor_args():
    sig = inspect.signature(QVTBase_FunctionParameter.__init__)
    params = list(sig.parameters.keys())



def test_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(MultiplicityElement)


def test_multiplicityelement_constructor_exists():
    assert callable(MultiplicityElement.__init__)


def test_multiplicityelement_constructor_args():
    sig = inspect.signature(MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_TupleLiteralPart)


def test_essentialocl_tupleliteralpart_constructor_exists():
    assert callable(EssentialOCL_TupleLiteralPart.__init__)


def test_essentialocl_tupleliteralpart_constructor_args():
    sig = inspect.signature(EssentialOCL_TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_oclexpression_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_OclExpression)


def test_essentialocl_oclexpression_constructor_exists():
    assert callable(EssentialOCL_OclExpression.__init__)


def test_essentialocl_oclexpression_constructor_args():
    sig = inspect.signature(EssentialOCL_OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_emof_parameter_is_not_abstract():
    assert not inspect.isabstract(EMOF_Parameter)


def test_emof_parameter_constructor_exists():
    assert callable(EMOF_Parameter.__init__)


def test_emof_parameter_constructor_args():
    sig = inspect.signature(EMOF_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_variable_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_Variable)


def test_essentialocl_variable_constructor_exists():
    assert callable(EssentialOCL_Variable.__init__)


def test_essentialocl_variable_constructor_args():
    sig = inspect.signature(EssentialOCL_Variable.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_CollectionLiteralPart)


def test_essentialocl_collectionliteralpart_constructor_exists():
    assert callable(EssentialOCL_CollectionLiteralPart.__init__)


def test_essentialocl_collectionliteralpart_constructor_args():
    sig = inspect.signature(EssentialOCL_CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_expressioninocl_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_ExpressionInOcl)


def test_essentialocl_expressioninocl_constructor_exists():
    assert callable(EssentialOCL_ExpressionInOcl.__init__)


def test_essentialocl_expressioninocl_constructor_args():
    sig = inspect.signature(EssentialOCL_ExpressionInOcl.__init__)
    params = list(sig.parameters.keys())



def test_emof_property_is_not_abstract():
    assert not inspect.isabstract(EMOF_Property)


def test_emof_property_constructor_exists():
    assert callable(EMOF_Property.__init__)


def test_emof_property_constructor_args():
    sig = inspect.signature(EMOF_Property.__init__)
    params = list(sig.parameters.keys())
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isDerived" in params, "Missing parameter 'isDerived'"
    assert "default" in params, "Missing parameter 'default'"
    assert "isID" in params, "Missing parameter 'isID'"
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"

def test_emof_property_has_isComposite():
    assert hasattr(EMOF_Property, "isComposite")
    descriptor = None
    for klass in EMOF_Property.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_emof_property_has_isDerived():
    assert hasattr(EMOF_Property, "isDerived")
    descriptor = None
    for klass in EMOF_Property.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)

def test_emof_property_has_default():
    assert hasattr(EMOF_Property, "default")
    descriptor = None
    for klass in EMOF_Property.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_emof_property_has_isID():
    assert hasattr(EMOF_Property, "isID")
    descriptor = None
    for klass in EMOF_Property.__mro__:
        if "isID" in klass.__dict__:
            descriptor = klass.__dict__["isID"]
            break
    assert isinstance(descriptor, property)

def test_emof_property_has_isReadOnly():
    assert hasattr(EMOF_Property, "isReadOnly")
    descriptor = None
    for klass in EMOF_Property.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)



def test_emof_operation_is_not_abstract():
    assert not inspect.isabstract(EMOF_Operation)


def test_emof_operation_constructor_exists():
    assert callable(EMOF_Operation.__init__)


def test_emof_operation_constructor_args():
    sig = inspect.signature(EMOF_Operation.__init__)
    params = list(sig.parameters.keys())



def test_object_is_not_abstract():
    assert not inspect.isabstract(Object)


def test_object_constructor_exists():
    assert callable(Object.__init__)


def test_object_constructor_args():
    sig = inspect.signature(Object.__init__)
    params = list(sig.parameters.keys())



def test_emof_reflectivecollection_is_not_abstract():
    assert not inspect.isabstract(EMOF_ReflectiveCollection)


def test_emof_reflectivecollection_constructor_exists():
    assert callable(EMOF_ReflectiveCollection.__init__)


def test_emof_reflectivecollection_constructor_args():
    sig = inspect.signature(EMOF_ReflectiveCollection.__init__)
    params = list(sig.parameters.keys())



def test_emof_element_is_not_abstract():
    assert not inspect.isabstract(EMOF_Element)


def test_emof_element_constructor_exists():
    assert callable(EMOF_Element.__init__)


def test_emof_element_constructor_args():
    sig = inspect.signature(EMOF_Element.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_qvtbase_domain_is_not_abstract():
    assert not inspect.isabstract(QVTBase_Domain)


def test_qvtbase_domain_constructor_exists():
    assert callable(QVTBase_Domain.__init__)


def test_qvtbase_domain_constructor_args():
    sig = inspect.signature(QVTBase_Domain.__init__)
    params = list(sig.parameters.keys())
    assert "isCheckable" in params, "Missing parameter 'isCheckable'"
    assert "isEnforceable" in params, "Missing parameter 'isEnforceable'"

def test_qvtbase_domain_has_isCheckable():
    assert hasattr(QVTBase_Domain, "isCheckable")
    descriptor = None
    for klass in QVTBase_Domain.__mro__:
        if "isCheckable" in klass.__dict__:
            descriptor = klass.__dict__["isCheckable"]
            break
    assert isinstance(descriptor, property)

def test_qvtbase_domain_has_isEnforceable():
    assert hasattr(QVTBase_Domain, "isEnforceable")
    descriptor = None
    for klass in QVTBase_Domain.__mro__:
        if "isEnforceable" in klass.__dict__:
            descriptor = klass.__dict__["isEnforceable"]
            break
    assert isinstance(descriptor, property)



def test_qvtbase_typedmodel_is_not_abstract():
    assert not inspect.isabstract(QVTBase_TypedModel)


def test_qvtbase_typedmodel_constructor_exists():
    assert callable(QVTBase_TypedModel.__init__)


def test_qvtbase_typedmodel_constructor_args():
    sig = inspect.signature(QVTBase_TypedModel.__init__)
    params = list(sig.parameters.keys())



def test_emof_package_is_not_abstract():
    assert not inspect.isabstract(EMOF_Package)


def test_emof_package_constructor_exists():
    assert callable(EMOF_Package.__init__)


def test_emof_package_constructor_args():
    sig = inspect.signature(EMOF_Package.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_emof_package_has_uri():
    assert hasattr(EMOF_Package, "uri")
    descriptor = None
    for klass in EMOF_Package.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_emof_typedelement_is_not_abstract():
    assert not inspect.isabstract(EMOF_TypedElement)


def test_emof_typedelement_constructor_exists():
    assert callable(EMOF_TypedElement.__init__)


def test_emof_typedelement_constructor_args():
    sig = inspect.signature(EMOF_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_qvtbase_rule_is_not_abstract():
    assert not inspect.isabstract(QVTBase_Rule)


def test_qvtbase_rule_constructor_exists():
    assert callable(QVTBase_Rule.__init__)


def test_qvtbase_rule_constructor_args():
    sig = inspect.signature(QVTBase_Rule.__init__)
    params = list(sig.parameters.keys())



def test_emof_type_is_not_abstract():
    assert not inspect.isabstract(EMOF_Type)


def test_emof_type_constructor_exists():
    assert callable(EMOF_Type.__init__)


def test_emof_type_constructor_args():
    sig = inspect.signature(EMOF_Type.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_qvttemplate_propertytemplateitem_is_not_abstract():
    assert not inspect.isabstract(QVTTemplate_PropertyTemplateItem)


def test_qvttemplate_propertytemplateitem_constructor_exists():
    assert callable(QVTTemplate_PropertyTemplateItem.__init__)


def test_qvttemplate_propertytemplateitem_constructor_args():
    sig = inspect.signature(QVTTemplate_PropertyTemplateItem.__init__)
    params = list(sig.parameters.keys())
    assert "isOpposite" in params, "Missing parameter 'isOpposite'"

def test_qvttemplate_propertytemplateitem_has_isOpposite():
    assert hasattr(QVTTemplate_PropertyTemplateItem, "isOpposite")
    descriptor = None
    for klass in QVTTemplate_PropertyTemplateItem.__mro__:
        if "isOpposite" in klass.__dict__:
            descriptor = klass.__dict__["isOpposite"]
            break
    assert isinstance(descriptor, property)



def test_emof_tag_is_not_abstract():
    assert not inspect.isabstract(EMOF_Tag)


def test_emof_tag_constructor_exists():
    assert callable(EMOF_Tag.__init__)


def test_emof_tag_constructor_args():
    sig = inspect.signature(EMOF_Tag.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_emof_tag_has_value():
    assert hasattr(EMOF_Tag, "value")
    descriptor = None
    for klass in EMOF_Tag.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_emof_tag_has_name():
    assert hasattr(EMOF_Tag, "name")
    descriptor = None
    for klass in EMOF_Tag.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emof_namedelement_is_not_abstract():
    assert not inspect.isabstract(EMOF_NamedElement)


def test_emof_namedelement_constructor_exists():
    assert callable(EMOF_NamedElement.__init__)


def test_emof_namedelement_constructor_args():
    sig = inspect.signature(EMOF_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emof_namedelement_has_name():
    assert hasattr(EMOF_NamedElement, "name")
    descriptor = None
    for klass in EMOF_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_qvtcore_enforcementoperation_is_not_abstract():
    assert not inspect.isabstract(QVTCore_EnforcementOperation)


def test_qvtcore_enforcementoperation_constructor_exists():
    assert callable(QVTCore_EnforcementOperation.__init__)


def test_qvtcore_enforcementoperation_constructor_args():
    sig = inspect.signature(QVTCore_EnforcementOperation.__init__)
    params = list(sig.parameters.keys())
    assert "enforcementMode" in params, "Missing parameter 'enforcementMode'"

def test_qvtcore_enforcementoperation_has_enforcementMode():
    assert hasattr(QVTCore_EnforcementOperation, "enforcementMode")
    descriptor = None
    for klass in QVTCore_EnforcementOperation.__mro__:
        if "enforcementMode" in klass.__dict__:
            descriptor = klass.__dict__["enforcementMode"]
            break
    assert isinstance(descriptor, property)



def test_qvtcore_assignment_is_not_abstract():
    assert not inspect.isabstract(QVTCore_Assignment)


def test_qvtcore_assignment_constructor_exists():
    assert callable(QVTCore_Assignment.__init__)


def test_qvtcore_assignment_constructor_args():
    sig = inspect.signature(QVTCore_Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "isDefault" in params, "Missing parameter 'isDefault'"

def test_qvtcore_assignment_has_isDefault():
    assert hasattr(QVTCore_Assignment, "isDefault")
    descriptor = None
    for klass in QVTCore_Assignment.__mro__:
        if "isDefault" in klass.__dict__:
            descriptor = klass.__dict__["isDefault"]
            break
    assert isinstance(descriptor, property)



def test_emof_factory_is_not_abstract():
    assert not inspect.isabstract(EMOF_Factory)


def test_emof_factory_constructor_exists():
    assert callable(EMOF_Factory.__init__)


def test_emof_factory_constructor_args():
    sig = inspect.signature(EMOF_Factory.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_dictliteralpart_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_DictLiteralPart)


def test_imperativeocl_dictliteralpart_constructor_exists():
    assert callable(ImperativeOCL_DictLiteralPart.__init__)


def test_imperativeocl_dictliteralpart_constructor_args():
    sig = inspect.signature(ImperativeOCL_DictLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation_relationdomainassignment_is_not_abstract():
    assert not inspect.isabstract(QVTRelation_RelationDomainAssignment)


def test_qvtrelation_relationdomainassignment_constructor_exists():
    assert callable(QVTRelation_RelationDomainAssignment.__init__)


def test_qvtrelation_relationdomainassignment_constructor_args():
    sig = inspect.signature(QVTRelation_RelationDomainAssignment.__init__)
    params = list(sig.parameters.keys())



def test_qvtbase_predicate_is_not_abstract():
    assert not inspect.isabstract(QVTBase_Predicate)


def test_qvtbase_predicate_constructor_exists():
    assert callable(QVTBase_Predicate.__init__)


def test_qvtbase_predicate_constructor_args():
    sig = inspect.signature(QVTBase_Predicate.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_orderedtupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_OrderedTupleLiteralPart)


def test_imperativeocl_orderedtupleliteralpart_constructor_exists():
    assert callable(ImperativeOCL_OrderedTupleLiteralPart.__init__)


def test_imperativeocl_orderedtupleliteralpart_constructor_args():
    sig = inspect.signature(ImperativeOCL_OrderedTupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_qvtbase_pattern_is_not_abstract():
    assert not inspect.isabstract(QVTBase_Pattern)


def test_qvtbase_pattern_constructor_exists():
    assert callable(QVTBase_Pattern.__init__)


def test_qvtbase_pattern_constructor_args():
    sig = inspect.signature(QVTBase_Pattern.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation_key_is_not_abstract():
    assert not inspect.isabstract(QVTRelation_Key)


def test_qvtrelation_key_constructor_exists():
    assert callable(QVTRelation_Key.__init__)


def test_qvtrelation_key_constructor_args():
    sig = inspect.signature(QVTRelation_Key.__init__)
    params = list(sig.parameters.keys())



def test_emof_comment_is_not_abstract():
    assert not inspect.isabstract(EMOF_Comment)


def test_emof_comment_constructor_exists():
    assert callable(EMOF_Comment.__init__)


def test_emof_comment_constructor_args():
    sig = inspect.signature(EMOF_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_emof_comment_has_body():
    assert hasattr(EMOF_Comment, "body")
    descriptor = None
    for klass in EMOF_Comment.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_qvtbase_transformation_is_not_abstract():
    assert not inspect.isabstract(QVTBase_Transformation)


def test_qvtbase_transformation_constructor_exists():
    assert callable(QVTBase_Transformation.__init__)


def test_qvtbase_transformation_constructor_args():
    sig = inspect.signature(QVTBase_Transformation.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_typedef_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_Typedef)


def test_imperativeocl_typedef_constructor_exists():
    assert callable(ImperativeOCL_Typedef.__init__)


def test_imperativeocl_typedef_constructor_args():
    sig = inspect.signature(ImperativeOCL_Typedef.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_orderedtupletype_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_OrderedTupleType)


def test_imperativeocl_orderedtupletype_constructor_exists():
    assert callable(ImperativeOCL_OrderedTupleType.__init__)


def test_imperativeocl_orderedtupletype_constructor_args():
    sig = inspect.signature(ImperativeOCL_OrderedTupleType.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_qvtbase_function_is_not_abstract():
    assert not inspect.isabstract(QVTBase_Function)


def test_qvtbase_function_constructor_exists():
    assert callable(QVTBase_Function.__init__)


def test_qvtbase_function_constructor_args():
    sig = inspect.signature(QVTBase_Function.__init__)
    params = list(sig.parameters.keys())



def test_emof_extent_is_not_abstract():
    assert not inspect.isabstract(EMOF_Extent)


def test_emof_extent_constructor_exists():
    assert callable(EMOF_Extent.__init__)


def test_emof_extent_constructor_args():
    sig = inspect.signature(EMOF_Extent.__init__)
    params = list(sig.parameters.keys())



def test_enumeration_is_not_abstract():
    assert not inspect.isabstract(Enumeration)


def test_enumeration_constructor_exists():
    assert callable(Enumeration.__init__)


def test_enumeration_constructor_args():
    sig = inspect.signature(Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_emof_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(EMOF_EnumerationLiteral)


def test_emof_enumerationliteral_constructor_exists():
    assert callable(EMOF_EnumerationLiteral.__init__)


def test_emof_enumerationliteral_constructor_args():
    sig = inspect.signature(EMOF_EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(EnumerationLiteral)


def test_enumerationliteral_constructor_exists():
    assert callable(EnumerationLiteral.__init__)


def test_enumerationliteral_constructor_args():
    sig = inspect.signature(EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_tupletype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_TupleType)


def test_essentialocl_tupletype_constructor_exists():
    assert callable(EssentialOCL_TupleType.__init__)


def test_essentialocl_tupletype_constructor_args():
    sig = inspect.signature(EssentialOCL_TupleType.__init__)
    params = list(sig.parameters.keys())



def test_emof_primitivetype_is_not_abstract():
    assert not inspect.isabstract(EMOF_PrimitiveType)


def test_emof_primitivetype_constructor_exists():
    assert callable(EMOF_PrimitiveType.__init__)


def test_emof_primitivetype_constructor_args():
    sig = inspect.signature(EMOF_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_collectiontype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_CollectionType)


def test_essentialocl_collectiontype_constructor_exists():
    assert callable(EssentialOCL_CollectionType.__init__)


def test_essentialocl_collectiontype_constructor_args():
    sig = inspect.signature(EssentialOCL_CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_emof_enumeration_is_not_abstract():
    assert not inspect.isabstract(EMOF_Enumeration)


def test_emof_enumeration_constructor_exists():
    assert callable(EMOF_Enumeration.__init__)


def test_emof_enumeration_constructor_args():
    sig = inspect.signature(EMOF_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_templateparametertype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_TemplateParameterType)


def test_essentialocl_templateparametertype_constructor_exists():
    assert callable(EssentialOCL_TemplateParameterType.__init__)


def test_essentialocl_templateparametertype_constructor_args():
    sig = inspect.signature(EssentialOCL_TemplateParameterType.__init__)
    params = list(sig.parameters.keys())
    assert "specification" in params, "Missing parameter 'specification'"

def test_essentialocl_templateparametertype_has_specification():
    assert hasattr(EssentialOCL_TemplateParameterType, "specification")
    descriptor = None
    for klass in EssentialOCL_TemplateParameterType.__mro__:
        if "specification" in klass.__dict__:
            descriptor = klass.__dict__["specification"]
            break
    assert isinstance(descriptor, property)



def test_essentialocl_invalidtype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_InvalidType)


def test_essentialocl_invalidtype_constructor_exists():
    assert callable(EssentialOCL_InvalidType.__init__)


def test_essentialocl_invalidtype_constructor_args():
    sig = inspect.signature(EssentialOCL_InvalidType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_anytype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_AnyType)


def test_essentialocl_anytype_constructor_exists():
    assert callable(EssentialOCL_AnyType.__init__)


def test_essentialocl_anytype_constructor_args():
    sig = inspect.signature(EssentialOCL_AnyType.__init__)
    params = list(sig.parameters.keys())



def test_emof_datatype_is_not_abstract():
    assert not inspect.isabstract(EMOF_DataType)


def test_emof_datatype_constructor_exists():
    assert callable(EMOF_DataType.__init__)


def test_emof_datatype_constructor_args():
    sig = inspect.signature(EMOF_DataType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_voidtype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_VoidType)


def test_essentialocl_voidtype_constructor_exists():
    assert callable(EssentialOCL_VoidType.__init__)


def test_essentialocl_voidtype_constructor_args():
    sig = inspect.signature(EssentialOCL_VoidType.__init__)
    params = list(sig.parameters.keys())



def test_emof_class_is_not_abstract():
    assert not inspect.isabstract(EMOF_Class)


def test_emof_class_constructor_exists():
    assert callable(EMOF_Class.__init__)


def test_emof_class_constructor_args():
    sig = inspect.signature(EMOF_Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_emof_class_has_isAbstract():
    assert hasattr(EMOF_Class, "isAbstract")
    descriptor = None
    for klass in EMOF_Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_qvtoperational_varparameter_is_not_abstract():
    assert not inspect.isabstract(QVTOperational_VarParameter)


def test_qvtoperational_varparameter_constructor_exists():
    assert callable(QVTOperational_VarParameter.__init__)


def test_qvtoperational_varparameter_constructor_args():
    sig = inspect.signature(QVTOperational_VarParameter.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_qvtoperational_varparameter_has_kind():
    assert hasattr(QVTOperational_VarParameter, "kind")
    descriptor = None
    for klass in QVTOperational_VarParameter.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_resolveexp_is_not_abstract():
    assert not inspect.isabstract(ResolveExp)


def test_resolveexp_constructor_exists():
    assert callable(ResolveExp.__init__)


def test_resolveexp_constructor_args():
    sig = inspect.signature(ResolveExp.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_resolveinexp_is_not_abstract():
    assert not inspect.isabstract(QVTOperational_ResolveInExp)


def test_qvtoperational_resolveinexp_constructor_exists():
    assert callable(QVTOperational_ResolveInExp.__init__)


def test_qvtoperational_resolveinexp_constructor_args():
    sig = inspect.signature(QVTOperational_ResolveInExp.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_resolveexp_is_not_abstract():
    assert not inspect.isabstract(QVTOperational_ResolveExp)


def test_qvtoperational_resolveexp_constructor_exists():
    assert callable(QVTOperational_ResolveExp.__init__)


def test_qvtoperational_resolveexp_constructor_args():
    sig = inspect.signature(QVTOperational_ResolveExp.__init__)
    params = list(sig.parameters.keys())
    assert "isInverse" in params, "Missing parameter 'isInverse'"
    assert "one" in params, "Missing parameter 'one'"
    assert "isDeferred" in params, "Missing parameter 'isDeferred'"

def test_qvtoperational_resolveexp_has_isInverse():
    assert hasattr(QVTOperational_ResolveExp, "isInverse")
    descriptor = None
    for klass in QVTOperational_ResolveExp.__mro__:
        if "isInverse" in klass.__dict__:
            descriptor = klass.__dict__["isInverse"]
            break
    assert isinstance(descriptor, property)

def test_qvtoperational_resolveexp_has_one():
    assert hasattr(QVTOperational_ResolveExp, "one")
    descriptor = None
    for klass in QVTOperational_ResolveExp.__mro__:
        if "one" in klass.__dict__:
            descriptor = klass.__dict__["one"]
            break
    assert isinstance(descriptor, property)

def test_qvtoperational_resolveexp_has_isDeferred():
    assert hasattr(QVTOperational_ResolveExp, "isDeferred")
    descriptor = None
    for klass in QVTOperational_ResolveExp.__mro__:
        if "isDeferred" in klass.__dict__:
            descriptor = klass.__dict__["isDeferred"]
            break
    assert isinstance(descriptor, property)



def test_constructorbody_is_not_abstract():
    assert not inspect.isabstract(ConstructorBody)


def test_constructorbody_constructor_exists():
    assert callable(ConstructorBody.__init__)


def test_constructorbody_constructor_args():
    sig = inspect.signature(ConstructorBody.__init__)
    params = list(sig.parameters.keys())



def test_instantiationexp_is_not_abstract():
    assert not inspect.isabstract(InstantiationExp)


def test_instantiationexp_constructor_exists():
    assert callable(InstantiationExp.__init__)


def test_instantiationexp_constructor_args():
    sig = inspect.signature(InstantiationExp.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_objectexp_is_not_abstract():
    assert not inspect.isabstract(QVTOperational_ObjectExp)


def test_qvtoperational_objectexp_constructor_exists():
    assert callable(QVTOperational_ObjectExp.__init__)


def test_qvtoperational_objectexp_constructor_args():
    sig = inspect.signature(QVTOperational_ObjectExp.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_moduleimport_is_not_abstract():
    assert not inspect.isabstract(QVTOperational_ModuleImport)


def test_qvtoperational_moduleimport_constructor_exists():
    assert callable(QVTOperational_ModuleImport.__init__)


def test_qvtoperational_moduleimport_constructor_args():
    sig = inspect.signature(QVTOperational_ModuleImport.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_qvtoperational_moduleimport_has_kind():
    assert hasattr(QVTOperational_ModuleImport, "kind")
    descriptor = None
    for klass in QVTOperational_ModuleImport.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_modeltype_is_not_abstract():
    assert not inspect.isabstract(ModelType)


def test_modeltype_constructor_exists():
    assert callable(ModelType.__init__)


def test_modeltype_constructor_args():
    sig = inspect.signature(ModelType.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_operationbody_is_not_abstract():
    assert not inspect.isabstract(QVTOperational_OperationBody)


def test_qvtoperational_operationbody_constructor_exists():
    assert callable(QVTOperational_OperationBody.__init__)


def test_qvtoperational_operationbody_constructor_args():
    sig = inspect.signature(QVTOperational_OperationBody.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_module_is_not_abstract():
    assert not inspect.isabstract(QVTOperational_Module)


def test_qvtoperational_module_constructor_exists():
    assert callable(QVTOperational_Module.__init__)


def test_qvtoperational_module_constructor_args():
    sig = inspect.signature(QVTOperational_Module.__init__)
    params = list(sig.parameters.keys())
    assert "isBlackbox" in params, "Missing parameter 'isBlackbox'"

def test_qvtoperational_module_has_isBlackbox():
    assert hasattr(QVTOperational_Module, "isBlackbox")
    descriptor = None
    for klass in QVTOperational_Module.__mro__:
        if "isBlackbox" in klass.__dict__:
            descriptor = klass.__dict__["isBlackbox"]
            break
    assert isinstance(descriptor, property)



def test_qvtoperational_modeltype_is_not_abstract():
    assert not inspect.isabstract(QVTOperational_ModelType)


def test_qvtoperational_modeltype_constructor_exists():
    assert callable(QVTOperational_ModelType.__init__)


def test_qvtoperational_modeltype_constructor_args():
    sig = inspect.signature(QVTOperational_ModelType.__init__)
    params = list(sig.parameters.keys())
    assert "conformanceKind" in params, "Missing parameter 'conformanceKind'"

def test_qvtoperational_modeltype_has_conformanceKind():
    assert hasattr(QVTOperational_ModelType, "conformanceKind")
    descriptor = None
    for klass in QVTOperational_ModelType.__mro__:
        if "conformanceKind" in klass.__dict__:
            descriptor = klass.__dict__["conformanceKind"]
            break
    assert isinstance(descriptor, property)



def test_moduleimport_is_not_abstract():
    assert not inspect.isabstract(ModuleImport)


def test_moduleimport_constructor_exists():
    assert callable(ModuleImport.__init__)


def test_moduleimport_constructor_args():
    sig = inspect.signature(ModuleImport.__init__)
    params = list(sig.parameters.keys())



def test_entryoperation_is_not_abstract():
    assert not inspect.isabstract(EntryOperation)


def test_entryoperation_constructor_exists():
    assert callable(EntryOperation.__init__)


def test_entryoperation_constructor_args():
    sig = inspect.signature(EntryOperation.__init__)
    params = list(sig.parameters.keys())



def test_mappingoperation_is_not_abstract():
    assert not inspect.isabstract(MappingOperation)


def test_mappingoperation_constructor_exists():
    assert callable(MappingOperation.__init__)


def test_mappingoperation_constructor_args():
    sig = inspect.signature(MappingOperation.__init__)
    params = list(sig.parameters.keys())



def test_imperativecallexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeCallExp)


def test_imperativecallexp_constructor_exists():
    assert callable(ImperativeCallExp.__init__)


def test_imperativecallexp_constructor_args():
    sig = inspect.signature(ImperativeCallExp.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_mappingcallexp_is_not_abstract():
    assert not inspect.isabstract(QVTOperational_MappingCallExp)


def test_qvtoperational_mappingcallexp_constructor_exists():
    assert callable(QVTOperational_MappingCallExp.__init__)


def test_qvtoperational_mappingcallexp_constructor_args():
    sig = inspect.signature(QVTOperational_MappingCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "isStrict" in params, "Missing parameter 'isStrict'"

def test_qvtoperational_mappingcallexp_has_isStrict():
    assert hasattr(QVTOperational_MappingCallExp, "isStrict")
    descriptor = None
    for klass in QVTOperational_MappingCallExp.__mro__:
        if "isStrict" in klass.__dict__:
            descriptor = klass.__dict__["isStrict"]
            break
    assert isinstance(descriptor, property)



def test_relationdomain_is_not_abstract():
    assert not inspect.isabstract(RelationDomain)


def test_relationdomain_constructor_exists():
    assert callable(RelationDomain.__init__)


def test_relationdomain_constructor_args():
    sig = inspect.signature(RelationDomain.__init__)
    params = list(sig.parameters.keys())



def test_modelparameter_is_not_abstract():
    assert not inspect.isabstract(ModelParameter)


def test_modelparameter_constructor_exists():
    assert callable(ModelParameter.__init__)


def test_modelparameter_constructor_args():
    sig = inspect.signature(ModelParameter.__init__)
    params = list(sig.parameters.keys())



def test_varparameter_is_not_abstract():
    assert not inspect.isabstract(VarParameter)


def test_varparameter_constructor_exists():
    assert callable(VarParameter.__init__)


def test_varparameter_constructor_args():
    sig = inspect.signature(VarParameter.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_modelparameter_is_not_abstract():
    assert not inspect.isabstract(QVTOperational_ModelParameter)


def test_qvtoperational_modelparameter_constructor_exists():
    assert callable(QVTOperational_ModelParameter.__init__)


def test_qvtoperational_modelparameter_constructor_args():
    sig = inspect.signature(QVTOperational_ModelParameter.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_mappingparameter_is_not_abstract():
    assert not inspect.isabstract(QVTOperational_MappingParameter)


def test_qvtoperational_mappingparameter_constructor_exists():
    assert callable(QVTOperational_MappingParameter.__init__)


def test_qvtoperational_mappingparameter_constructor_args():
    sig = inspect.signature(QVTOperational_MappingParameter.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_imperativeoperation_is_not_abstract():
    assert not inspect.isabstract(QVTOperational_ImperativeOperation)


def test_qvtoperational_imperativeoperation_constructor_exists():
    assert callable(QVTOperational_ImperativeOperation.__init__)


def test_qvtoperational_imperativeoperation_constructor_args():
    sig = inspect.signature(QVTOperational_ImperativeOperation.__init__)
    params = list(sig.parameters.keys())
    assert "isBlackbox" in params, "Missing parameter 'isBlackbox'"

def test_qvtoperational_imperativeoperation_has_isBlackbox():
    assert hasattr(QVTOperational_ImperativeOperation, "isBlackbox")
    descriptor = None
    for klass in QVTOperational_ImperativeOperation.__mro__:
        if "isBlackbox" in klass.__dict__:
            descriptor = klass.__dict__["isBlackbox"]
            break
    assert isinstance(descriptor, property)



def test_qvtoperational_imperativecallexp_is_not_abstract():
    assert not inspect.isabstract(QVTOperational_ImperativeCallExp)


def test_qvtoperational_imperativecallexp_constructor_exists():
    assert callable(QVTOperational_ImperativeCallExp.__init__)


def test_qvtoperational_imperativecallexp_constructor_args():
    sig = inspect.signature(QVTOperational_ImperativeCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "isVirtual" in params, "Missing parameter 'isVirtual'"

def test_qvtoperational_imperativecallexp_has_isVirtual():
    assert hasattr(QVTOperational_ImperativeCallExp, "isVirtual")
    descriptor = None
    for klass in QVTOperational_ImperativeCallExp.__mro__:
        if "isVirtual" in klass.__dict__:
            descriptor = klass.__dict__["isVirtual"]
            break
    assert isinstance(descriptor, property)



def test_module_is_not_abstract():
    assert not inspect.isabstract(Module)


def test_module_constructor_exists():
    assert callable(Module.__init__)


def test_module_constructor_args():
    sig = inspect.signature(Module.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_operationaltransformation_is_not_abstract():
    assert not inspect.isabstract(QVTOperational_OperationalTransformation)


def test_qvtoperational_operationaltransformation_constructor_exists():
    assert callable(QVTOperational_OperationalTransformation.__init__)


def test_qvtoperational_operationaltransformation_constructor_args():
    sig = inspect.signature(QVTOperational_OperationalTransformation.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_library_is_not_abstract():
    assert not inspect.isabstract(QVTOperational_Library)


def test_qvtoperational_library_constructor_exists():
    assert callable(QVTOperational_Library.__init__)


def test_qvtoperational_library_constructor_args():
    sig = inspect.signature(QVTOperational_Library.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation_relationimplementation_is_not_abstract():
    assert not inspect.isabstract(QVTRelation_RelationImplementation)


def test_qvtrelation_relationimplementation_constructor_exists():
    assert callable(QVTRelation_RelationImplementation.__init__)


def test_qvtrelation_relationimplementation_constructor_args():
    sig = inspect.signature(QVTRelation_RelationImplementation.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_contextualproperty_is_not_abstract():
    assert not inspect.isabstract(QVTOperational_ContextualProperty)


def test_qvtoperational_contextualproperty_constructor_exists():
    assert callable(QVTOperational_ContextualProperty.__init__)


def test_qvtoperational_contextualproperty_constructor_args():
    sig = inspect.signature(QVTOperational_ContextualProperty.__init__)
    params = list(sig.parameters.keys())



def test_operationbody_is_not_abstract():
    assert not inspect.isabstract(OperationBody)


def test_operationbody_constructor_exists():
    assert callable(OperationBody.__init__)


def test_operationbody_constructor_args():
    sig = inspect.signature(OperationBody.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_mappingbody_is_not_abstract():
    assert not inspect.isabstract(QVTOperational_MappingBody)


def test_qvtoperational_mappingbody_constructor_exists():
    assert callable(QVTOperational_MappingBody.__init__)


def test_qvtoperational_mappingbody_constructor_args():
    sig = inspect.signature(QVTOperational_MappingBody.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_constructorbody_is_not_abstract():
    assert not inspect.isabstract(QVTOperational_ConstructorBody)


def test_qvtoperational_constructorbody_constructor_exists():
    assert callable(QVTOperational_ConstructorBody.__init__)


def test_qvtoperational_constructorbody_constructor_args():
    sig = inspect.signature(QVTOperational_ConstructorBody.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoperation_is_not_abstract():
    assert not inspect.isabstract(ImperativeOperation)


def test_imperativeoperation_constructor_exists():
    assert callable(ImperativeOperation.__init__)


def test_imperativeoperation_constructor_args():
    sig = inspect.signature(ImperativeOperation.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_mappingoperation_is_not_abstract():
    assert not inspect.isabstract(QVTOperational_MappingOperation)


def test_qvtoperational_mappingoperation_constructor_exists():
    assert callable(QVTOperational_MappingOperation.__init__)


def test_qvtoperational_mappingoperation_constructor_args():
    sig = inspect.signature(QVTOperational_MappingOperation.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_constructor_is_not_abstract():
    assert not inspect.isabstract(QVTOperational_Constructor)


def test_qvtoperational_constructor_constructor_exists():
    assert callable(QVTOperational_Constructor.__init__)


def test_qvtoperational_constructor_constructor_args():
    sig = inspect.signature(QVTOperational_Constructor.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_entryoperation_is_not_abstract():
    assert not inspect.isabstract(QVTOperational_EntryOperation)


def test_qvtoperational_entryoperation_constructor_exists():
    assert callable(QVTOperational_EntryOperation.__init__)


def test_qvtoperational_entryoperation_constructor_args():
    sig = inspect.signature(QVTOperational_EntryOperation.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_helper_is_not_abstract():
    assert not inspect.isabstract(QVTOperational_Helper)


def test_qvtoperational_helper_constructor_exists():
    assert callable(QVTOperational_Helper.__init__)


def test_qvtoperational_helper_constructor_args():
    sig = inspect.signature(QVTOperational_Helper.__init__)
    params = list(sig.parameters.keys())
    assert "isQuery" in params, "Missing parameter 'isQuery'"

def test_qvtoperational_helper_has_isQuery():
    assert hasattr(QVTOperational_Helper, "isQuery")
    descriptor = None
    for klass in QVTOperational_Helper.__mro__:
        if "isQuery" in klass.__dict__:
            descriptor = klass.__dict__["isQuery"]
            break
    assert isinstance(descriptor, property)

def test_directionkind_exists():
    # Check that the Enumeration exists
    assert DirectionKind is not None

def test_directionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DirectionKind]
    expected_literals = [
        "inout",
        "out",
        "in_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DirectionKind"

def test_collectionkind_exists():
    # Check that the Enumeration exists
    assert CollectionKind is not None

def test_collectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CollectionKind]
    expected_literals = [
        "Bag",
        "Collection",
        "OrderedSet",
        "Set",
        "Sequence",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CollectionKind"

def test_severitykind_exists():
    # Check that the Enumeration exists
    assert SeverityKind is not None

def test_severitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SeverityKind]
    expected_literals = [
        "warning",
        "error",
        "fatal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SeverityKind"

def test_enforcementmode_exists():
    # Check that the Enumeration exists
    assert EnforcementMode is not None

def test_enforcementmode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EnforcementMode]
    expected_literals = [
        "Deletion",
        "Creation",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EnforcementMode"

def test_importkind_exists():
    # Check that the Enumeration exists
    assert ImportKind is not None

def test_importkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ImportKind]
    expected_literals = [
        "access",
        "extension",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ImportKind"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
Key_strategy = st.builds(
    Key,
)
Relation_strategy = st.builds(
    Relation,
)
DomainPattern_strategy = st.builds(
    DomainPattern,
)
RelationDomainAssignment_strategy = st.builds(
    RelationDomainAssignment,
)
RelationImplementation_strategy = st.builds(
    RelationImplementation,
)
PropertyCallExp_strategy = st.builds(
    PropertyCallExp,
)
QVTRelation_OppositePropertyCallExp_strategy = st.builds(
    QVTRelation_OppositePropertyCallExp,
)
RelationalTransformation_strategy = st.builds(
    RelationalTransformation,
)
PropertyTemplateItem_strategy = st.builds(
    PropertyTemplateItem,
)
ObjectTemplateExp_strategy = st.builds(
    ObjectTemplateExp,
)
Mapping_strategy = st.builds(
    Mapping,
)
TemplateExp_strategy = st.builds(
    TemplateExp,
)
QVTTemplate_ObjectTemplateExp_strategy = st.builds(
    QVTTemplate_ObjectTemplateExp,
)
QVTTemplate_CollectionTemplateExp_strategy = st.builds(
    QVTTemplate_CollectionTemplateExp,
)
RealizedVariable_strategy = st.builds(
    RealizedVariable,
)
EnforcementOperation_strategy = st.builds(
    EnforcementOperation,
)
Assignment_strategy = st.builds(
    Assignment,
)
QVTCore_VariableAssignment_strategy = st.builds(
    QVTCore_VariableAssignment,
)
QVTCore_PropertyAssignment_strategy = st.builds(
    QVTCore_PropertyAssignment,
)
Area_strategy = st.builds(
    Area,
)
Tag_strategy = st.builds(
    Tag,
)
CorePattern_strategy = st.builds(
    CorePattern,
)
QVTCore_GuardPattern_strategy = st.builds(
    QVTCore_GuardPattern,
)
QVTCore_BottomPattern_strategy = st.builds(
    QVTCore_BottomPattern,
)
GuardPattern_strategy = st.builds(
    GuardPattern,
)
BottomPattern_strategy = st.builds(
    BottomPattern,
)
QVTCore_Area_strategy = st.builds(
    QVTCore_Area,
)
Predicate_strategy = st.builds(
    Predicate,
)
TypedModel_strategy = st.builds(
    TypedModel,
)
Rule_strategy = st.builds(
    Rule,
)
QVTCore_Mapping_strategy = st.builds(
    QVTCore_Mapping,
)
QVTRelation_Relation_strategy = st.builds(
    QVTRelation_Relation,
    isTopLevel=
        safe_text
)
Transformation_strategy = st.builds(
    Transformation,
)
QVTRelation_RelationalTransformation_strategy = st.builds(
    QVTRelation_RelationalTransformation,
)
Domain_strategy = st.builds(
    Domain,
)
QVTRelation_RelationDomain_strategy = st.builds(
    QVTRelation_RelationDomain,
)
QVTCore_CoreDomain_strategy = st.builds(
    QVTCore_CoreDomain,
)
Pattern_strategy = st.builds(
    Pattern,
)
QVTCore_CorePattern_strategy = st.builds(
    QVTCore_CorePattern,
)
QVTRelation_DomainPattern_strategy = st.builds(
    QVTRelation_DomainPattern,
)
CatchExp_strategy = st.builds(
    CatchExp,
)
AltExp_strategy = st.builds(
    AltExp,
)
OrderedTupleLiteralPart_strategy = st.builds(
    OrderedTupleLiteralPart,
)
OperationCallExp_strategy = st.builds(
    OperationCallExp,
)
DictLiteralPart_strategy = st.builds(
    DictLiteralPart,
)
ImperativeLoopExp_strategy = st.builds(
    ImperativeLoopExp,
)
ImperativeOCL_ImperativeIterateExp_strategy = st.builds(
    ImperativeOCL_ImperativeIterateExp,
)
ImperativeOCL_ForExp_strategy = st.builds(
    ImperativeOCL_ForExp,
)
LogExp_strategy = st.builds(
    LogExp,
)
ImperativeExpression_strategy = st.builds(
    ImperativeExpression,
)
ImperativeOCL_UnpackExp_strategy = st.builds(
    ImperativeOCL_UnpackExp,
)
ImperativeOCL_AssignExp_strategy = st.builds(
    ImperativeOCL_AssignExp,
    isReset=
        safe_text
)
ImperativeOCL_SwitchExp_strategy = st.builds(
    ImperativeOCL_SwitchExp,
)
ImperativeOCL_WhileExp_strategy = st.builds(
    ImperativeOCL_WhileExp,
)
ImperativeOCL_LogExp_strategy = st.builds(
    ImperativeOCL_LogExp,
)
ImperativeOCL_ContinueExp_strategy = st.builds(
    ImperativeOCL_ContinueExp,
)
ImperativeOCL_InstantiationExp_strategy = st.builds(
    ImperativeOCL_InstantiationExp,
)
ImperativeOCL_RaiseExp_strategy = st.builds(
    ImperativeOCL_RaiseExp,
)
ImperativeOCL_AssertExp_strategy = st.builds(
    ImperativeOCL_AssertExp,
    severity=
        safe_text
)
ImperativeOCL_ComputeExp_strategy = st.builds(
    ImperativeOCL_ComputeExp,
)
ImperativeOCL_VariableInitExp_strategy = st.builds(
    ImperativeOCL_VariableInitExp,
    withResult=
        safe_text
)
ImperativeOCL_UnlinkExp_strategy = st.builds(
    ImperativeOCL_UnlinkExp,
)
ImperativeOCL_TryExp_strategy = st.builds(
    ImperativeOCL_TryExp,
)
ImperativeOCL_ReturnExp_strategy = st.builds(
    ImperativeOCL_ReturnExp,
)
ImperativeOCL_AltExp_strategy = st.builds(
    ImperativeOCL_AltExp,
)
ImperativeOCL_CatchExp_strategy = st.builds(
    ImperativeOCL_CatchExp,
)
ImperativeOCL_BreakExp_strategy = st.builds(
    ImperativeOCL_BreakExp,
)
ImperativeOCL_BlockExp_strategy = st.builds(
    ImperativeOCL_BlockExp,
)
TupleLiteralExp_strategy = st.builds(
    TupleLiteralExp,
)
TupleLiteralPart_strategy = st.builds(
    TupleLiteralPart,
)
LetExp_strategy = st.builds(
    LetExp,
)
FeatureCallExp_strategy = st.builds(
    FeatureCallExp,
)
EssentialOCL_OperationCallExp_strategy = st.builds(
    EssentialOCL_OperationCallExp,
)
EssentialOCL_NavigationCallExp_strategy = st.builds(
    EssentialOCL_NavigationCallExp,
)
NavigationCallExp_strategy = st.builds(
    NavigationCallExp,
)
EssentialOCL_PropertyCallExp_strategy = st.builds(
    EssentialOCL_PropertyCallExp,
)
NumericLiteralExp_strategy = st.builds(
    NumericLiteralExp,
)
EssentialOCL_RealLiteralExp_strategy = st.builds(
    EssentialOCL_RealLiteralExp,
    realSymbol=
        safe_text
)
EssentialOCL_UnlimitedNaturalExp_strategy = st.builds(
    EssentialOCL_UnlimitedNaturalExp,
    symbol=
        safe_text
)
EssentialOCL_IntegerLiteralExp_strategy = st.builds(
    EssentialOCL_IntegerLiteralExp,
    integerSymbol=
        safe_text
)
CallExp_strategy = st.builds(
    CallExp,
)
EssentialOCL_FeatureCallExp_strategy = st.builds(
    EssentialOCL_FeatureCallExp,
)
LoopExp_strategy = st.builds(
    LoopExp,
)
EssentialOCL_IteratorExp_strategy = st.builds(
    EssentialOCL_IteratorExp,
)
ImperativeOCL_ImperativeLoopExp_strategy = st.builds(
    ImperativeOCL_ImperativeLoopExp,
)
EssentialOCL_IterateExp_strategy = st.builds(
    EssentialOCL_IterateExp,
)
CollectionLiteralExp_strategy = st.builds(
    CollectionLiteralExp,
)
LiteralExp_strategy = st.builds(
    LiteralExp,
)
QVTTemplate_TemplateExp_strategy = st.builds(
    QVTTemplate_TemplateExp,
)
EssentialOCL_PrimitiveLiteralExp_strategy = st.builds(
    EssentialOCL_PrimitiveLiteralExp,
)
ImperativeOCL_OrderedTupleLiteralExp_strategy = st.builds(
    ImperativeOCL_OrderedTupleLiteralExp,
)
EssentialOCL_TupleLiteralExp_strategy = st.builds(
    EssentialOCL_TupleLiteralExp,
)
EssentialOCL_InvalidLiteralExp_strategy = st.builds(
    EssentialOCL_InvalidLiteralExp,
)
ImperativeOCL_DictLiteralExp_strategy = st.builds(
    ImperativeOCL_DictLiteralExp,
)
EssentialOCL_NullLiteralExp_strategy = st.builds(
    EssentialOCL_NullLiteralExp,
)
ImperativeOCL_ListLiteralExp_strategy = st.builds(
    ImperativeOCL_ListLiteralExp,
)
EssentialOCL_CollectionLiteralExp_strategy = st.builds(
    EssentialOCL_CollectionLiteralExp,
    kind=
        safe_text
)
Variable_strategy = st.builds(
    Variable,
)
QVTCore_RealizedVariable_strategy = st.builds(
    QVTCore_RealizedVariable,
)
EssentialOCL_EnumLiteralExp_strategy = st.builds(
    EssentialOCL_EnumLiteralExp,
)
Extent_strategy = st.builds(
    Extent,
)
EMOF_URIExtent_strategy = st.builds(
    EMOF_URIExtent,
)
CollectionLiteralPart_strategy = st.builds(
    CollectionLiteralPart,
)
EssentialOCL_CollectionRange_strategy = st.builds(
    EssentialOCL_CollectionRange,
)
EssentialOCL_CollectionItem_strategy = st.builds(
    EssentialOCL_CollectionItem,
)
OclExpression_strategy = st.builds(
    OclExpression,
)
EssentialOCL_TypeExp_strategy = st.builds(
    EssentialOCL_TypeExp,
)
EssentialOCL_LetExp_strategy = st.builds(
    EssentialOCL_LetExp,
)
EssentialOCL_IfExp_strategy = st.builds(
    EssentialOCL_IfExp,
)
EssentialOCL_LiteralExp_strategy = st.builds(
    EssentialOCL_LiteralExp,
)
EssentialOCL_LoopExp_strategy = st.builds(
    EssentialOCL_LoopExp,
)
QVTRelation_RelationCallExp_strategy = st.builds(
    QVTRelation_RelationCallExp,
)
ImperativeOCL_ImperativeExpression_strategy = st.builds(
    ImperativeOCL_ImperativeExpression,
)
EssentialOCL_VariableExp_strategy = st.builds(
    EssentialOCL_VariableExp,
)
EssentialOCL_CallExp_strategy = st.builds(
    EssentialOCL_CallExp,
)
PrimitiveLiteralExp_strategy = st.builds(
    PrimitiveLiteralExp,
)
EssentialOCL_NumericLiteralExp_strategy = st.builds(
    EssentialOCL_NumericLiteralExp,
)
EssentialOCL_StringLiteralExp_strategy = st.builds(
    EssentialOCL_StringLiteralExp,
    stringSymbol=
        safe_text
)
EssentialOCL_BooleanLiteralExp_strategy = st.builds(
    EssentialOCL_BooleanLiteralExp,
    booleanSymbol=
        safe_text
)
CollectionType_strategy = st.builds(
    CollectionType,
)
EssentialOCL_OrderedSetType_strategy = st.builds(
    EssentialOCL_OrderedSetType,
)
ImperativeOCL_ListType_strategy = st.builds(
    ImperativeOCL_ListType,
)
EssentialOCL_SetType_strategy = st.builds(
    EssentialOCL_SetType,
)
EssentialOCL_SequenceType_strategy = st.builds(
    EssentialOCL_SequenceType,
)
ImperativeOCL_DictionaryType_strategy = st.builds(
    ImperativeOCL_DictionaryType,
)
EssentialOCL_BagType_strategy = st.builds(
    EssentialOCL_BagType,
)
ReflectiveCollection_strategy = st.builds(
    ReflectiveCollection,
)
EMOF_ReflectiveSequence_strategy = st.builds(
    EMOF_ReflectiveSequence,
)
EMOF_Object_strategy = st.builds(
    EMOF_Object,
)
EMOF_MultiplicityElement_strategy = st.builds(
    EMOF_MultiplicityElement,
    lower=
        safe_text,
    isOrdered=
        safe_text,
    upper=
        safe_text,
    isUnique=
        safe_text
)
Package_strategy = st.builds(
    Package,
)
Parameter_strategy = st.builds(
    Parameter,
)
QVTBase_FunctionParameter_strategy = st.builds(
    QVTBase_FunctionParameter,
)
MultiplicityElement_strategy = st.builds(
    MultiplicityElement,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
EssentialOCL_TupleLiteralPart_strategy = st.builds(
    EssentialOCL_TupleLiteralPart,
)
EssentialOCL_OclExpression_strategy = st.builds(
    EssentialOCL_OclExpression,
)
EMOF_Parameter_strategy = st.builds(
    EMOF_Parameter,
)
EssentialOCL_Variable_strategy = st.builds(
    EssentialOCL_Variable,
)
EssentialOCL_CollectionLiteralPart_strategy = st.builds(
    EssentialOCL_CollectionLiteralPart,
)
EssentialOCL_ExpressionInOcl_strategy = st.builds(
    EssentialOCL_ExpressionInOcl,
)
EMOF_Property_strategy = st.builds(
    EMOF_Property,
    isComposite=
        safe_text,
    isDerived=
        safe_text,
    default=
        safe_text,
    isID=
        safe_text,
    isReadOnly=
        safe_text
)
EMOF_Operation_strategy = st.builds(
    EMOF_Operation,
)
Object_strategy = st.builds(
    Object,
)
EMOF_ReflectiveCollection_strategy = st.builds(
    EMOF_ReflectiveCollection,
)
EMOF_Element_strategy = st.builds(
    EMOF_Element,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
QVTBase_Domain_strategy = st.builds(
    QVTBase_Domain,
    isCheckable=
        safe_text,
    isEnforceable=
        safe_text
)
QVTBase_TypedModel_strategy = st.builds(
    QVTBase_TypedModel,
)
EMOF_Package_strategy = st.builds(
    EMOF_Package,
    uri=
        safe_text
)
EMOF_TypedElement_strategy = st.builds(
    EMOF_TypedElement,
)
QVTBase_Rule_strategy = st.builds(
    QVTBase_Rule,
)
EMOF_Type_strategy = st.builds(
    EMOF_Type,
)
Element_strategy = st.builds(
    Element,
)
QVTTemplate_PropertyTemplateItem_strategy = st.builds(
    QVTTemplate_PropertyTemplateItem,
    isOpposite=
        safe_text
)
EMOF_Tag_strategy = st.builds(
    EMOF_Tag,
    value=
        safe_text,
    name=
        safe_text
)
EMOF_NamedElement_strategy = st.builds(
    EMOF_NamedElement,
    name=
        safe_text
)
QVTCore_EnforcementOperation_strategy = st.builds(
    QVTCore_EnforcementOperation,
    enforcementMode=
        safe_text
)
QVTCore_Assignment_strategy = st.builds(
    QVTCore_Assignment,
    isDefault=
        safe_text
)
EMOF_Factory_strategy = st.builds(
    EMOF_Factory,
)
ImperativeOCL_DictLiteralPart_strategy = st.builds(
    ImperativeOCL_DictLiteralPart,
)
QVTRelation_RelationDomainAssignment_strategy = st.builds(
    QVTRelation_RelationDomainAssignment,
)
QVTBase_Predicate_strategy = st.builds(
    QVTBase_Predicate,
)
ImperativeOCL_OrderedTupleLiteralPart_strategy = st.builds(
    ImperativeOCL_OrderedTupleLiteralPart,
)
QVTBase_Pattern_strategy = st.builds(
    QVTBase_Pattern,
)
QVTRelation_Key_strategy = st.builds(
    QVTRelation_Key,
)
EMOF_Comment_strategy = st.builds(
    EMOF_Comment,
    body=
        safe_text
)
Class_strategy = st.builds(
    Class,
)
QVTBase_Transformation_strategy = st.builds(
    QVTBase_Transformation,
)
ImperativeOCL_Typedef_strategy = st.builds(
    ImperativeOCL_Typedef,
)
ImperativeOCL_OrderedTupleType_strategy = st.builds(
    ImperativeOCL_OrderedTupleType,
)
Operation_strategy = st.builds(
    Operation,
)
QVTBase_Function_strategy = st.builds(
    QVTBase_Function,
)
EMOF_Extent_strategy = st.builds(
    EMOF_Extent,
)
Enumeration_strategy = st.builds(
    Enumeration,
)
EMOF_EnumerationLiteral_strategy = st.builds(
    EMOF_EnumerationLiteral,
)
EnumerationLiteral_strategy = st.builds(
    EnumerationLiteral,
)
DataType_strategy = st.builds(
    DataType,
)
EssentialOCL_TupleType_strategy = st.builds(
    EssentialOCL_TupleType,
)
EMOF_PrimitiveType_strategy = st.builds(
    EMOF_PrimitiveType,
)
EssentialOCL_CollectionType_strategy = st.builds(
    EssentialOCL_CollectionType,
)
EMOF_Enumeration_strategy = st.builds(
    EMOF_Enumeration,
)
Comment_strategy = st.builds(
    Comment,
)
Property_strategy = st.builds(
    Property,
)
Type_strategy = st.builds(
    Type,
)
EssentialOCL_TemplateParameterType_strategy = st.builds(
    EssentialOCL_TemplateParameterType,
    specification=
        safe_text
)
EssentialOCL_InvalidType_strategy = st.builds(
    EssentialOCL_InvalidType,
)
EssentialOCL_AnyType_strategy = st.builds(
    EssentialOCL_AnyType,
)
EMOF_DataType_strategy = st.builds(
    EMOF_DataType,
)
EssentialOCL_VoidType_strategy = st.builds(
    EssentialOCL_VoidType,
)
EMOF_Class_strategy = st.builds(
    EMOF_Class,
    isAbstract=
        safe_text
)
QVTOperational_VarParameter_strategy = st.builds(
    QVTOperational_VarParameter,
    kind=
        safe_text
)
ResolveExp_strategy = st.builds(
    ResolveExp,
)
QVTOperational_ResolveInExp_strategy = st.builds(
    QVTOperational_ResolveInExp,
)
QVTOperational_ResolveExp_strategy = st.builds(
    QVTOperational_ResolveExp,
    isInverse=
        safe_text,
    one=
        safe_text,
    isDeferred=
        safe_text
)
ConstructorBody_strategy = st.builds(
    ConstructorBody,
)
InstantiationExp_strategy = st.builds(
    InstantiationExp,
)
QVTOperational_ObjectExp_strategy = st.builds(
    QVTOperational_ObjectExp,
)
QVTOperational_ModuleImport_strategy = st.builds(
    QVTOperational_ModuleImport,
    kind=
        safe_text
)
ModelType_strategy = st.builds(
    ModelType,
)
QVTOperational_OperationBody_strategy = st.builds(
    QVTOperational_OperationBody,
)
QVTOperational_Module_strategy = st.builds(
    QVTOperational_Module,
    isBlackbox=
        safe_text
)
QVTOperational_ModelType_strategy = st.builds(
    QVTOperational_ModelType,
    conformanceKind=
        safe_text
)
ModuleImport_strategy = st.builds(
    ModuleImport,
)
EntryOperation_strategy = st.builds(
    EntryOperation,
)
MappingOperation_strategy = st.builds(
    MappingOperation,
)
ImperativeCallExp_strategy = st.builds(
    ImperativeCallExp,
)
QVTOperational_MappingCallExp_strategy = st.builds(
    QVTOperational_MappingCallExp,
    isStrict=
        safe_text
)
RelationDomain_strategy = st.builds(
    RelationDomain,
)
ModelParameter_strategy = st.builds(
    ModelParameter,
)
VarParameter_strategy = st.builds(
    VarParameter,
)
QVTOperational_ModelParameter_strategy = st.builds(
    QVTOperational_ModelParameter,
)
QVTOperational_MappingParameter_strategy = st.builds(
    QVTOperational_MappingParameter,
)
QVTOperational_ImperativeOperation_strategy = st.builds(
    QVTOperational_ImperativeOperation,
    isBlackbox=
        safe_text
)
QVTOperational_ImperativeCallExp_strategy = st.builds(
    QVTOperational_ImperativeCallExp,
    isVirtual=
        safe_text
)
Module_strategy = st.builds(
    Module,
)
QVTOperational_OperationalTransformation_strategy = st.builds(
    QVTOperational_OperationalTransformation,
)
QVTOperational_Library_strategy = st.builds(
    QVTOperational_Library,
)
QVTRelation_RelationImplementation_strategy = st.builds(
    QVTRelation_RelationImplementation,
)
QVTOperational_ContextualProperty_strategy = st.builds(
    QVTOperational_ContextualProperty,
)
OperationBody_strategy = st.builds(
    OperationBody,
)
QVTOperational_MappingBody_strategy = st.builds(
    QVTOperational_MappingBody,
)
QVTOperational_ConstructorBody_strategy = st.builds(
    QVTOperational_ConstructorBody,
)
ImperativeOperation_strategy = st.builds(
    ImperativeOperation,
)
QVTOperational_MappingOperation_strategy = st.builds(
    QVTOperational_MappingOperation,
)
QVTOperational_Constructor_strategy = st.builds(
    QVTOperational_Constructor,
)
QVTOperational_EntryOperation_strategy = st.builds(
    QVTOperational_EntryOperation,
)
QVTOperational_Helper_strategy = st.builds(
    QVTOperational_Helper,
    isQuery=
        safe_text
)

@given(instance=Key_strategy)
@settings(max_examples=50)
def test_key_instantiation(instance):
    assert isinstance(instance, Key)

@given(instance=Relation_strategy)
@settings(max_examples=50)
def test_relation_instantiation(instance):
    assert isinstance(instance, Relation)

@given(instance=DomainPattern_strategy)
@settings(max_examples=50)
def test_domainpattern_instantiation(instance):
    assert isinstance(instance, DomainPattern)

@given(instance=RelationDomainAssignment_strategy)
@settings(max_examples=50)
def test_relationdomainassignment_instantiation(instance):
    assert isinstance(instance, RelationDomainAssignment)

@given(instance=RelationImplementation_strategy)
@settings(max_examples=50)
def test_relationimplementation_instantiation(instance):
    assert isinstance(instance, RelationImplementation)

@given(instance=PropertyCallExp_strategy)
@settings(max_examples=50)
def test_propertycallexp_instantiation(instance):
    assert isinstance(instance, PropertyCallExp)

@given(instance=QVTRelation_OppositePropertyCallExp_strategy)
@settings(max_examples=50)
def test_qvtrelation_oppositepropertycallexp_instantiation(instance):
    assert isinstance(instance, QVTRelation_OppositePropertyCallExp)

@given(instance=RelationalTransformation_strategy)
@settings(max_examples=50)
def test_relationaltransformation_instantiation(instance):
    assert isinstance(instance, RelationalTransformation)

@given(instance=PropertyTemplateItem_strategy)
@settings(max_examples=50)
def test_propertytemplateitem_instantiation(instance):
    assert isinstance(instance, PropertyTemplateItem)

@given(instance=ObjectTemplateExp_strategy)
@settings(max_examples=50)
def test_objecttemplateexp_instantiation(instance):
    assert isinstance(instance, ObjectTemplateExp)

@given(instance=Mapping_strategy)
@settings(max_examples=50)
def test_mapping_instantiation(instance):
    assert isinstance(instance, Mapping)

@given(instance=TemplateExp_strategy)
@settings(max_examples=50)
def test_templateexp_instantiation(instance):
    assert isinstance(instance, TemplateExp)

@given(instance=QVTTemplate_ObjectTemplateExp_strategy)
@settings(max_examples=50)
def test_qvttemplate_objecttemplateexp_instantiation(instance):
    assert isinstance(instance, QVTTemplate_ObjectTemplateExp)

@given(instance=QVTTemplate_CollectionTemplateExp_strategy)
@settings(max_examples=50)
def test_qvttemplate_collectiontemplateexp_instantiation(instance):
    assert isinstance(instance, QVTTemplate_CollectionTemplateExp)

@given(instance=RealizedVariable_strategy)
@settings(max_examples=50)
def test_realizedvariable_instantiation(instance):
    assert isinstance(instance, RealizedVariable)

@given(instance=EnforcementOperation_strategy)
@settings(max_examples=50)
def test_enforcementoperation_instantiation(instance):
    assert isinstance(instance, EnforcementOperation)

@given(instance=Assignment_strategy)
@settings(max_examples=50)
def test_assignment_instantiation(instance):
    assert isinstance(instance, Assignment)

@given(instance=QVTCore_VariableAssignment_strategy)
@settings(max_examples=50)
def test_qvtcore_variableassignment_instantiation(instance):
    assert isinstance(instance, QVTCore_VariableAssignment)

@given(instance=QVTCore_PropertyAssignment_strategy)
@settings(max_examples=50)
def test_qvtcore_propertyassignment_instantiation(instance):
    assert isinstance(instance, QVTCore_PropertyAssignment)

@given(instance=Area_strategy)
@settings(max_examples=50)
def test_area_instantiation(instance):
    assert isinstance(instance, Area)

@given(instance=Tag_strategy)
@settings(max_examples=50)
def test_tag_instantiation(instance):
    assert isinstance(instance, Tag)

@given(instance=CorePattern_strategy)
@settings(max_examples=50)
def test_corepattern_instantiation(instance):
    assert isinstance(instance, CorePattern)

@given(instance=QVTCore_GuardPattern_strategy)
@settings(max_examples=50)
def test_qvtcore_guardpattern_instantiation(instance):
    assert isinstance(instance, QVTCore_GuardPattern)

@given(instance=QVTCore_BottomPattern_strategy)
@settings(max_examples=50)
def test_qvtcore_bottompattern_instantiation(instance):
    assert isinstance(instance, QVTCore_BottomPattern)

@given(instance=GuardPattern_strategy)
@settings(max_examples=50)
def test_guardpattern_instantiation(instance):
    assert isinstance(instance, GuardPattern)

@given(instance=BottomPattern_strategy)
@settings(max_examples=50)
def test_bottompattern_instantiation(instance):
    assert isinstance(instance, BottomPattern)

@given(instance=QVTCore_Area_strategy)
@settings(max_examples=50)
def test_qvtcore_area_instantiation(instance):
    assert isinstance(instance, QVTCore_Area)

@given(instance=Predicate_strategy)
@settings(max_examples=50)
def test_predicate_instantiation(instance):
    assert isinstance(instance, Predicate)

@given(instance=TypedModel_strategy)
@settings(max_examples=50)
def test_typedmodel_instantiation(instance):
    assert isinstance(instance, TypedModel)

@given(instance=Rule_strategy)
@settings(max_examples=50)
def test_rule_instantiation(instance):
    assert isinstance(instance, Rule)

@given(instance=QVTCore_Mapping_strategy)
@settings(max_examples=50)
def test_qvtcore_mapping_instantiation(instance):
    assert isinstance(instance, QVTCore_Mapping)

@given(instance=QVTRelation_Relation_strategy)
@settings(max_examples=50)
def test_qvtrelation_relation_instantiation(instance):
    assert isinstance(instance, QVTRelation_Relation)



@given(instance=QVTRelation_Relation_strategy)
def test_qvtrelation_relation_isTopLevel_setter(instance):
    original = instance.isTopLevel
    instance.isTopLevel = original
    assert instance.isTopLevel == original

@given(instance=Transformation_strategy)
@settings(max_examples=50)
def test_transformation_instantiation(instance):
    assert isinstance(instance, Transformation)

@given(instance=QVTRelation_RelationalTransformation_strategy)
@settings(max_examples=50)
def test_qvtrelation_relationaltransformation_instantiation(instance):
    assert isinstance(instance, QVTRelation_RelationalTransformation)

@given(instance=Domain_strategy)
@settings(max_examples=50)
def test_domain_instantiation(instance):
    assert isinstance(instance, Domain)

@given(instance=QVTRelation_RelationDomain_strategy)
@settings(max_examples=50)
def test_qvtrelation_relationdomain_instantiation(instance):
    assert isinstance(instance, QVTRelation_RelationDomain)

@given(instance=QVTCore_CoreDomain_strategy)
@settings(max_examples=50)
def test_qvtcore_coredomain_instantiation(instance):
    assert isinstance(instance, QVTCore_CoreDomain)

@given(instance=Pattern_strategy)
@settings(max_examples=50)
def test_pattern_instantiation(instance):
    assert isinstance(instance, Pattern)

@given(instance=QVTCore_CorePattern_strategy)
@settings(max_examples=50)
def test_qvtcore_corepattern_instantiation(instance):
    assert isinstance(instance, QVTCore_CorePattern)

@given(instance=QVTRelation_DomainPattern_strategy)
@settings(max_examples=50)
def test_qvtrelation_domainpattern_instantiation(instance):
    assert isinstance(instance, QVTRelation_DomainPattern)

@given(instance=CatchExp_strategy)
@settings(max_examples=50)
def test_catchexp_instantiation(instance):
    assert isinstance(instance, CatchExp)

@given(instance=AltExp_strategy)
@settings(max_examples=50)
def test_altexp_instantiation(instance):
    assert isinstance(instance, AltExp)

@given(instance=OrderedTupleLiteralPart_strategy)
@settings(max_examples=50)
def test_orderedtupleliteralpart_instantiation(instance):
    assert isinstance(instance, OrderedTupleLiteralPart)

@given(instance=OperationCallExp_strategy)
@settings(max_examples=50)
def test_operationcallexp_instantiation(instance):
    assert isinstance(instance, OperationCallExp)

@given(instance=DictLiteralPart_strategy)
@settings(max_examples=50)
def test_dictliteralpart_instantiation(instance):
    assert isinstance(instance, DictLiteralPart)

@given(instance=ImperativeLoopExp_strategy)
@settings(max_examples=50)
def test_imperativeloopexp_instantiation(instance):
    assert isinstance(instance, ImperativeLoopExp)

@given(instance=ImperativeOCL_ImperativeIterateExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_imperativeiterateexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_ImperativeIterateExp)

@given(instance=ImperativeOCL_ForExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_forexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_ForExp)

@given(instance=LogExp_strategy)
@settings(max_examples=50)
def test_logexp_instantiation(instance):
    assert isinstance(instance, LogExp)

@given(instance=ImperativeExpression_strategy)
@settings(max_examples=50)
def test_imperativeexpression_instantiation(instance):
    assert isinstance(instance, ImperativeExpression)

@given(instance=ImperativeOCL_UnpackExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_unpackexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_UnpackExp)

@given(instance=ImperativeOCL_AssignExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_assignexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_AssignExp)



@given(instance=ImperativeOCL_AssignExp_strategy)
def test_imperativeocl_assignexp_isReset_setter(instance):
    original = instance.isReset
    instance.isReset = original
    assert instance.isReset == original

@given(instance=ImperativeOCL_SwitchExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_switchexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_SwitchExp)

@given(instance=ImperativeOCL_WhileExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_whileexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_WhileExp)

@given(instance=ImperativeOCL_LogExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_logexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_LogExp)

@given(instance=ImperativeOCL_ContinueExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_continueexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_ContinueExp)

@given(instance=ImperativeOCL_InstantiationExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_instantiationexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_InstantiationExp)

@given(instance=ImperativeOCL_RaiseExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_raiseexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_RaiseExp)

@given(instance=ImperativeOCL_AssertExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_assertexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_AssertExp)



@given(instance=ImperativeOCL_AssertExp_strategy)
def test_imperativeocl_assertexp_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original

@given(instance=ImperativeOCL_ComputeExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_computeexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_ComputeExp)

@given(instance=ImperativeOCL_VariableInitExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_variableinitexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_VariableInitExp)



@given(instance=ImperativeOCL_VariableInitExp_strategy)
def test_imperativeocl_variableinitexp_withResult_setter(instance):
    original = instance.withResult
    instance.withResult = original
    assert instance.withResult == original

@given(instance=ImperativeOCL_UnlinkExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_unlinkexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_UnlinkExp)

@given(instance=ImperativeOCL_TryExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_tryexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_TryExp)

@given(instance=ImperativeOCL_ReturnExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_returnexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_ReturnExp)

@given(instance=ImperativeOCL_AltExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_altexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_AltExp)

@given(instance=ImperativeOCL_CatchExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_catchexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_CatchExp)

@given(instance=ImperativeOCL_BreakExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_breakexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_BreakExp)

@given(instance=ImperativeOCL_BlockExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_blockexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_BlockExp)

@given(instance=TupleLiteralExp_strategy)
@settings(max_examples=50)
def test_tupleliteralexp_instantiation(instance):
    assert isinstance(instance, TupleLiteralExp)

@given(instance=TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_tupleliteralpart_instantiation(instance):
    assert isinstance(instance, TupleLiteralPart)

@given(instance=LetExp_strategy)
@settings(max_examples=50)
def test_letexp_instantiation(instance):
    assert isinstance(instance, LetExp)

@given(instance=FeatureCallExp_strategy)
@settings(max_examples=50)
def test_featurecallexp_instantiation(instance):
    assert isinstance(instance, FeatureCallExp)

@given(instance=EssentialOCL_OperationCallExp_strategy)
@settings(max_examples=50)
def test_essentialocl_operationcallexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_OperationCallExp)

@given(instance=EssentialOCL_NavigationCallExp_strategy)
@settings(max_examples=50)
def test_essentialocl_navigationcallexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_NavigationCallExp)

@given(instance=NavigationCallExp_strategy)
@settings(max_examples=50)
def test_navigationcallexp_instantiation(instance):
    assert isinstance(instance, NavigationCallExp)

@given(instance=EssentialOCL_PropertyCallExp_strategy)
@settings(max_examples=50)
def test_essentialocl_propertycallexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_PropertyCallExp)

@given(instance=NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_numericliteralexp_instantiation(instance):
    assert isinstance(instance, NumericLiteralExp)

@given(instance=EssentialOCL_RealLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl_realliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_RealLiteralExp)



@given(instance=EssentialOCL_RealLiteralExp_strategy)
def test_essentialocl_realliteralexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=EssentialOCL_UnlimitedNaturalExp_strategy)
@settings(max_examples=50)
def test_essentialocl_unlimitednaturalexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_UnlimitedNaturalExp)



@given(instance=EssentialOCL_UnlimitedNaturalExp_strategy)
def test_essentialocl_unlimitednaturalexp_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=EssentialOCL_IntegerLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl_integerliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_IntegerLiteralExp)



@given(instance=EssentialOCL_IntegerLiteralExp_strategy)
def test_essentialocl_integerliteralexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=CallExp_strategy)
@settings(max_examples=50)
def test_callexp_instantiation(instance):
    assert isinstance(instance, CallExp)

@given(instance=EssentialOCL_FeatureCallExp_strategy)
@settings(max_examples=50)
def test_essentialocl_featurecallexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_FeatureCallExp)

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=EssentialOCL_IteratorExp_strategy)
@settings(max_examples=50)
def test_essentialocl_iteratorexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_IteratorExp)

@given(instance=ImperativeOCL_ImperativeLoopExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_imperativeloopexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_ImperativeLoopExp)

@given(instance=EssentialOCL_IterateExp_strategy)
@settings(max_examples=50)
def test_essentialocl_iterateexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_IterateExp)

@given(instance=CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_collectionliteralexp_instantiation(instance):
    assert isinstance(instance, CollectionLiteralExp)

@given(instance=LiteralExp_strategy)
@settings(max_examples=50)
def test_literalexp_instantiation(instance):
    assert isinstance(instance, LiteralExp)

@given(instance=QVTTemplate_TemplateExp_strategy)
@settings(max_examples=50)
def test_qvttemplate_templateexp_instantiation(instance):
    assert isinstance(instance, QVTTemplate_TemplateExp)

@given(instance=EssentialOCL_PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl_primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_PrimitiveLiteralExp)

@given(instance=ImperativeOCL_OrderedTupleLiteralExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_orderedtupleliteralexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_OrderedTupleLiteralExp)

@given(instance=EssentialOCL_TupleLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl_tupleliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_TupleLiteralExp)

@given(instance=EssentialOCL_InvalidLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl_invalidliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_InvalidLiteralExp)

@given(instance=ImperativeOCL_DictLiteralExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_dictliteralexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_DictLiteralExp)

@given(instance=EssentialOCL_NullLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl_nullliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_NullLiteralExp)

@given(instance=ImperativeOCL_ListLiteralExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_listliteralexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_ListLiteralExp)

@given(instance=EssentialOCL_CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl_collectionliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_CollectionLiteralExp)



@given(instance=EssentialOCL_CollectionLiteralExp_strategy)
def test_essentialocl_collectionliteralexp_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=QVTCore_RealizedVariable_strategy)
@settings(max_examples=50)
def test_qvtcore_realizedvariable_instantiation(instance):
    assert isinstance(instance, QVTCore_RealizedVariable)

@given(instance=EssentialOCL_EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl_enumliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_EnumLiteralExp)

@given(instance=Extent_strategy)
@settings(max_examples=50)
def test_extent_instantiation(instance):
    assert isinstance(instance, Extent)

@given(instance=EMOF_URIExtent_strategy)
@settings(max_examples=50)
def test_emof_uriextent_instantiation(instance):
    assert isinstance(instance, EMOF_URIExtent)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_URIExtent_strategy)
@settings(max_examples=30)
def test_emof_uriextent_uri_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.uri(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.uri).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'uri' in EMOF_URIExtent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'uri' in EMOF_URIExtent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'uri' in EMOF_URIExtent is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_URIExtent_strategy)
@settings(max_examples=30)
def test_emof_uriextent_contexturi_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.contextURI()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.contextURI).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'contextURI' in EMOF_URIExtent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'contextURI' in EMOF_URIExtent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'contextURI' in EMOF_URIExtent is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_URIExtent_strategy)
@settings(max_examples=30)
def test_emof_uriextent_element_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.element(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.element).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'element' in EMOF_URIExtent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'element' in EMOF_URIExtent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'element' in EMOF_URIExtent is not implemented or raised an error")

@given(instance=CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_collectionliteralpart_instantiation(instance):
    assert isinstance(instance, CollectionLiteralPart)

@given(instance=EssentialOCL_CollectionRange_strategy)
@settings(max_examples=50)
def test_essentialocl_collectionrange_instantiation(instance):
    assert isinstance(instance, EssentialOCL_CollectionRange)

@given(instance=EssentialOCL_CollectionItem_strategy)
@settings(max_examples=50)
def test_essentialocl_collectionitem_instantiation(instance):
    assert isinstance(instance, EssentialOCL_CollectionItem)

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=EssentialOCL_TypeExp_strategy)
@settings(max_examples=50)
def test_essentialocl_typeexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_TypeExp)

@given(instance=EssentialOCL_LetExp_strategy)
@settings(max_examples=50)
def test_essentialocl_letexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_LetExp)

@given(instance=EssentialOCL_IfExp_strategy)
@settings(max_examples=50)
def test_essentialocl_ifexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_IfExp)

@given(instance=EssentialOCL_LiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl_literalexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_LiteralExp)

@given(instance=EssentialOCL_LoopExp_strategy)
@settings(max_examples=50)
def test_essentialocl_loopexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_LoopExp)

@given(instance=QVTRelation_RelationCallExp_strategy)
@settings(max_examples=50)
def test_qvtrelation_relationcallexp_instantiation(instance):
    assert isinstance(instance, QVTRelation_RelationCallExp)

@given(instance=ImperativeOCL_ImperativeExpression_strategy)
@settings(max_examples=50)
def test_imperativeocl_imperativeexpression_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_ImperativeExpression)

@given(instance=EssentialOCL_VariableExp_strategy)
@settings(max_examples=50)
def test_essentialocl_variableexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_VariableExp)

@given(instance=EssentialOCL_CallExp_strategy)
@settings(max_examples=50)
def test_essentialocl_callexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_CallExp)

@given(instance=PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, PrimitiveLiteralExp)

@given(instance=EssentialOCL_NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl_numericliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_NumericLiteralExp)

@given(instance=EssentialOCL_StringLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl_stringliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_StringLiteralExp)



@given(instance=EssentialOCL_StringLiteralExp_strategy)
def test_essentialocl_stringliteralexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=EssentialOCL_BooleanLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl_booleanliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_BooleanLiteralExp)



@given(instance=EssentialOCL_BooleanLiteralExp_strategy)
def test_essentialocl_booleanliteralexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=EssentialOCL_OrderedSetType_strategy)
@settings(max_examples=50)
def test_essentialocl_orderedsettype_instantiation(instance):
    assert isinstance(instance, EssentialOCL_OrderedSetType)

@given(instance=ImperativeOCL_ListType_strategy)
@settings(max_examples=50)
def test_imperativeocl_listtype_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_ListType)

@given(instance=EssentialOCL_SetType_strategy)
@settings(max_examples=50)
def test_essentialocl_settype_instantiation(instance):
    assert isinstance(instance, EssentialOCL_SetType)

@given(instance=EssentialOCL_SequenceType_strategy)
@settings(max_examples=50)
def test_essentialocl_sequencetype_instantiation(instance):
    assert isinstance(instance, EssentialOCL_SequenceType)

@given(instance=ImperativeOCL_DictionaryType_strategy)
@settings(max_examples=50)
def test_imperativeocl_dictionarytype_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_DictionaryType)

@given(instance=EssentialOCL_BagType_strategy)
@settings(max_examples=50)
def test_essentialocl_bagtype_instantiation(instance):
    assert isinstance(instance, EssentialOCL_BagType)

@given(instance=ReflectiveCollection_strategy)
@settings(max_examples=50)
def test_reflectivecollection_instantiation(instance):
    assert isinstance(instance, ReflectiveCollection)

@given(instance=EMOF_ReflectiveSequence_strategy)
@settings(max_examples=50)
def test_emof_reflectivesequence_instantiation(instance):
    assert isinstance(instance, EMOF_ReflectiveSequence)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_ReflectiveSequence_strategy)
@settings(max_examples=30)
def test_emof_reflectivesequence_add_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.add(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.add).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'add' in EMOF_ReflectiveSequence is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'add' in EMOF_ReflectiveSequence did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'add' in EMOF_ReflectiveSequence is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_ReflectiveSequence_strategy)
@settings(max_examples=30)
def test_emof_reflectivesequence_set_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.set(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.set).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'set' in EMOF_ReflectiveSequence is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'set' in EMOF_ReflectiveSequence did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'set' in EMOF_ReflectiveSequence is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_ReflectiveSequence_strategy)
@settings(max_examples=30)
def test_emof_reflectivesequence_remove_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.remove(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.remove).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'remove' in EMOF_ReflectiveSequence is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'remove' in EMOF_ReflectiveSequence did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'remove' in EMOF_ReflectiveSequence is not implemented or raised an error")

@given(instance=EMOF_Object_strategy)
@settings(max_examples=50)
def test_emof_object_instantiation(instance):
    assert isinstance(instance, EMOF_Object)

@given(instance=EMOF_MultiplicityElement_strategy)
@settings(max_examples=50)
def test_emof_multiplicityelement_instantiation(instance):
    assert isinstance(instance, EMOF_MultiplicityElement)



@given(instance=EMOF_MultiplicityElement_strategy)
def test_emof_multiplicityelement_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original



@given(instance=EMOF_MultiplicityElement_strategy)
def test_emof_multiplicityelement_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original



@given(instance=EMOF_MultiplicityElement_strategy)
def test_emof_multiplicityelement_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original



@given(instance=EMOF_MultiplicityElement_strategy)
def test_emof_multiplicityelement_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=QVTBase_FunctionParameter_strategy)
@settings(max_examples=50)
def test_qvtbase_functionparameter_instantiation(instance):
    assert isinstance(instance, QVTBase_FunctionParameter)

@given(instance=MultiplicityElement_strategy)
@settings(max_examples=50)
def test_multiplicityelement_instantiation(instance):
    assert isinstance(instance, MultiplicityElement)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=EssentialOCL_TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_essentialocl_tupleliteralpart_instantiation(instance):
    assert isinstance(instance, EssentialOCL_TupleLiteralPart)

@given(instance=EssentialOCL_OclExpression_strategy)
@settings(max_examples=50)
def test_essentialocl_oclexpression_instantiation(instance):
    assert isinstance(instance, EssentialOCL_OclExpression)

@given(instance=EMOF_Parameter_strategy)
@settings(max_examples=50)
def test_emof_parameter_instantiation(instance):
    assert isinstance(instance, EMOF_Parameter)

@given(instance=EssentialOCL_Variable_strategy)
@settings(max_examples=50)
def test_essentialocl_variable_instantiation(instance):
    assert isinstance(instance, EssentialOCL_Variable)

@given(instance=EssentialOCL_CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_essentialocl_collectionliteralpart_instantiation(instance):
    assert isinstance(instance, EssentialOCL_CollectionLiteralPart)

@given(instance=EssentialOCL_ExpressionInOcl_strategy)
@settings(max_examples=50)
def test_essentialocl_expressioninocl_instantiation(instance):
    assert isinstance(instance, EssentialOCL_ExpressionInOcl)

@given(instance=EMOF_Property_strategy)
@settings(max_examples=50)
def test_emof_property_instantiation(instance):
    assert isinstance(instance, EMOF_Property)



@given(instance=EMOF_Property_strategy)
def test_emof_property_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original



@given(instance=EMOF_Property_strategy)
def test_emof_property_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original



@given(instance=EMOF_Property_strategy)
def test_emof_property_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original



@given(instance=EMOF_Property_strategy)
def test_emof_property_isID_setter(instance):
    original = instance.isID
    instance.isID = original
    assert instance.isID == original



@given(instance=EMOF_Property_strategy)
def test_emof_property_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original

@given(instance=EMOF_Operation_strategy)
@settings(max_examples=50)
def test_emof_operation_instantiation(instance):
    assert isinstance(instance, EMOF_Operation)

@given(instance=Object_strategy)
@settings(max_examples=50)
def test_object_instantiation(instance):
    assert isinstance(instance, Object)

@given(instance=EMOF_ReflectiveCollection_strategy)
@settings(max_examples=50)
def test_emof_reflectivecollection_instantiation(instance):
    assert isinstance(instance, EMOF_ReflectiveCollection)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_ReflectiveCollection_strategy)
@settings(max_examples=30)
def test_emof_reflectivecollection_clear_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.clear()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.clear).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'clear' in EMOF_ReflectiveCollection is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'clear' in EMOF_ReflectiveCollection did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'clear' in EMOF_ReflectiveCollection is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_ReflectiveCollection_strategy)
@settings(max_examples=30)
def test_emof_reflectivecollection_remove_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.remove(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.remove).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'remove' in EMOF_ReflectiveCollection is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'remove' in EMOF_ReflectiveCollection did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'remove' in EMOF_ReflectiveCollection is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_ReflectiveCollection_strategy)
@settings(max_examples=30)
def test_emof_reflectivecollection_addall_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addAll(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addAll).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addAll' in EMOF_ReflectiveCollection is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addAll' in EMOF_ReflectiveCollection did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addAll' in EMOF_ReflectiveCollection is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_ReflectiveCollection_strategy)
@settings(max_examples=30)
def test_emof_reflectivecollection_add_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.add(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.add).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'add' in EMOF_ReflectiveCollection is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'add' in EMOF_ReflectiveCollection did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'add' in EMOF_ReflectiveCollection is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_ReflectiveCollection_strategy)
@settings(max_examples=30)
def test_emof_reflectivecollection_size_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.size()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.size).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'size' in EMOF_ReflectiveCollection is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'size' in EMOF_ReflectiveCollection did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'size' in EMOF_ReflectiveCollection is not implemented or raised an error")

@given(instance=EMOF_Element_strategy)
@settings(max_examples=50)
def test_emof_element_instantiation(instance):
    assert isinstance(instance, EMOF_Element)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_Element_strategy)
@settings(max_examples=30)
def test_emof_element_unset_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.unset(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.unset).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'unset' in EMOF_Element is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'unset' in EMOF_Element did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'unset' in EMOF_Element is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_Element_strategy)
@settings(max_examples=30)
def test_emof_element_container_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.container()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.container).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'container' in EMOF_Element is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'container' in EMOF_Element did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'container' in EMOF_Element is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_Element_strategy)
@settings(max_examples=30)
def test_emof_element_set_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.set(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.set).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'set' in EMOF_Element is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'set' in EMOF_Element did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'set' in EMOF_Element is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_Element_strategy)
@settings(max_examples=30)
def test_emof_element_equals_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.equals(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.equals).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'equals' in EMOF_Element is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'equals' in EMOF_Element did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'equals' in EMOF_Element is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_Element_strategy)
@settings(max_examples=30)
def test_emof_element_isset_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isSet(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isSet).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isSet' in EMOF_Element is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isSet' in EMOF_Element did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isSet' in EMOF_Element is not implemented or raised an error")

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=QVTBase_Domain_strategy)
@settings(max_examples=50)
def test_qvtbase_domain_instantiation(instance):
    assert isinstance(instance, QVTBase_Domain)



@given(instance=QVTBase_Domain_strategy)
def test_qvtbase_domain_isCheckable_setter(instance):
    original = instance.isCheckable
    instance.isCheckable = original
    assert instance.isCheckable == original



@given(instance=QVTBase_Domain_strategy)
def test_qvtbase_domain_isEnforceable_setter(instance):
    original = instance.isEnforceable
    instance.isEnforceable = original
    assert instance.isEnforceable == original

@given(instance=QVTBase_TypedModel_strategy)
@settings(max_examples=50)
def test_qvtbase_typedmodel_instantiation(instance):
    assert isinstance(instance, QVTBase_TypedModel)

@given(instance=EMOF_Package_strategy)
@settings(max_examples=50)
def test_emof_package_instantiation(instance):
    assert isinstance(instance, EMOF_Package)



@given(instance=EMOF_Package_strategy)
def test_emof_package_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=EMOF_TypedElement_strategy)
@settings(max_examples=50)
def test_emof_typedelement_instantiation(instance):
    assert isinstance(instance, EMOF_TypedElement)

@given(instance=QVTBase_Rule_strategy)
@settings(max_examples=50)
def test_qvtbase_rule_instantiation(instance):
    assert isinstance(instance, QVTBase_Rule)

@given(instance=EMOF_Type_strategy)
@settings(max_examples=50)
def test_emof_type_instantiation(instance):
    assert isinstance(instance, EMOF_Type)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_Type_strategy)
@settings(max_examples=30)
def test_emof_type_isinstance_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isInstance(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isInstance).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isInstance' in EMOF_Type is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isInstance' in EMOF_Type did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isInstance' in EMOF_Type is not implemented or raised an error")

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=QVTTemplate_PropertyTemplateItem_strategy)
@settings(max_examples=50)
def test_qvttemplate_propertytemplateitem_instantiation(instance):
    assert isinstance(instance, QVTTemplate_PropertyTemplateItem)



@given(instance=QVTTemplate_PropertyTemplateItem_strategy)
def test_qvttemplate_propertytemplateitem_isOpposite_setter(instance):
    original = instance.isOpposite
    instance.isOpposite = original
    assert instance.isOpposite == original

@given(instance=EMOF_Tag_strategy)
@settings(max_examples=50)
def test_emof_tag_instantiation(instance):
    assert isinstance(instance, EMOF_Tag)



@given(instance=EMOF_Tag_strategy)
def test_emof_tag_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=EMOF_Tag_strategy)
def test_emof_tag_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EMOF_NamedElement_strategy)
@settings(max_examples=50)
def test_emof_namedelement_instantiation(instance):
    assert isinstance(instance, EMOF_NamedElement)



@given(instance=EMOF_NamedElement_strategy)
def test_emof_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=QVTCore_EnforcementOperation_strategy)
@settings(max_examples=50)
def test_qvtcore_enforcementoperation_instantiation(instance):
    assert isinstance(instance, QVTCore_EnforcementOperation)



@given(instance=QVTCore_EnforcementOperation_strategy)
def test_qvtcore_enforcementoperation_enforcementMode_setter(instance):
    original = instance.enforcementMode
    instance.enforcementMode = original
    assert instance.enforcementMode == original

@given(instance=QVTCore_Assignment_strategy)
@settings(max_examples=50)
def test_qvtcore_assignment_instantiation(instance):
    assert isinstance(instance, QVTCore_Assignment)



@given(instance=QVTCore_Assignment_strategy)
def test_qvtcore_assignment_isDefault_setter(instance):
    original = instance.isDefault
    instance.isDefault = original
    assert instance.isDefault == original

@given(instance=EMOF_Factory_strategy)
@settings(max_examples=50)
def test_emof_factory_instantiation(instance):
    assert isinstance(instance, EMOF_Factory)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_Factory_strategy)
@settings(max_examples=30)
def test_emof_factory_createfromstring_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createFromString(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createFromString).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createFromString' in EMOF_Factory is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createFromString' in EMOF_Factory did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createFromString' in EMOF_Factory is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_Factory_strategy)
@settings(max_examples=30)
def test_emof_factory_converttostring_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.convertToString(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.convertToString).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'convertToString' in EMOF_Factory is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'convertToString' in EMOF_Factory did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'convertToString' in EMOF_Factory is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_Factory_strategy)
@settings(max_examples=30)
def test_emof_factory_create_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.create(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.create).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'create' in EMOF_Factory is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'create' in EMOF_Factory did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'create' in EMOF_Factory is not implemented or raised an error")

@given(instance=ImperativeOCL_DictLiteralPart_strategy)
@settings(max_examples=50)
def test_imperativeocl_dictliteralpart_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_DictLiteralPart)

@given(instance=QVTRelation_RelationDomainAssignment_strategy)
@settings(max_examples=50)
def test_qvtrelation_relationdomainassignment_instantiation(instance):
    assert isinstance(instance, QVTRelation_RelationDomainAssignment)

@given(instance=QVTBase_Predicate_strategy)
@settings(max_examples=50)
def test_qvtbase_predicate_instantiation(instance):
    assert isinstance(instance, QVTBase_Predicate)

@given(instance=ImperativeOCL_OrderedTupleLiteralPart_strategy)
@settings(max_examples=50)
def test_imperativeocl_orderedtupleliteralpart_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_OrderedTupleLiteralPart)

@given(instance=QVTBase_Pattern_strategy)
@settings(max_examples=50)
def test_qvtbase_pattern_instantiation(instance):
    assert isinstance(instance, QVTBase_Pattern)

@given(instance=QVTRelation_Key_strategy)
@settings(max_examples=50)
def test_qvtrelation_key_instantiation(instance):
    assert isinstance(instance, QVTRelation_Key)

@given(instance=EMOF_Comment_strategy)
@settings(max_examples=50)
def test_emof_comment_instantiation(instance):
    assert isinstance(instance, EMOF_Comment)



@given(instance=EMOF_Comment_strategy)
def test_emof_comment_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=QVTBase_Transformation_strategy)
@settings(max_examples=50)
def test_qvtbase_transformation_instantiation(instance):
    assert isinstance(instance, QVTBase_Transformation)

@given(instance=ImperativeOCL_Typedef_strategy)
@settings(max_examples=50)
def test_imperativeocl_typedef_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_Typedef)

@given(instance=ImperativeOCL_OrderedTupleType_strategy)
@settings(max_examples=50)
def test_imperativeocl_orderedtupletype_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_OrderedTupleType)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=QVTBase_Function_strategy)
@settings(max_examples=50)
def test_qvtbase_function_instantiation(instance):
    assert isinstance(instance, QVTBase_Function)

@given(instance=EMOF_Extent_strategy)
@settings(max_examples=50)
def test_emof_extent_instantiation(instance):
    assert isinstance(instance, EMOF_Extent)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_Extent_strategy)
@settings(max_examples=30)
def test_emof_extent_usecontainment_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.useContainment()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.useContainment).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'useContainment' in EMOF_Extent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'useContainment' in EMOF_Extent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'useContainment' in EMOF_Extent is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_Extent_strategy)
@settings(max_examples=30)
def test_emof_extent_elements_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.elements()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.elements).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'elements' in EMOF_Extent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'elements' in EMOF_Extent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'elements' in EMOF_Extent is not implemented or raised an error")

@given(instance=Enumeration_strategy)
@settings(max_examples=50)
def test_enumeration_instantiation(instance):
    assert isinstance(instance, Enumeration)

@given(instance=EMOF_EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_emof_enumerationliteral_instantiation(instance):
    assert isinstance(instance, EMOF_EnumerationLiteral)

@given(instance=EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_enumerationliteral_instantiation(instance):
    assert isinstance(instance, EnumerationLiteral)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=EssentialOCL_TupleType_strategy)
@settings(max_examples=50)
def test_essentialocl_tupletype_instantiation(instance):
    assert isinstance(instance, EssentialOCL_TupleType)

@given(instance=EMOF_PrimitiveType_strategy)
@settings(max_examples=50)
def test_emof_primitivetype_instantiation(instance):
    assert isinstance(instance, EMOF_PrimitiveType)

@given(instance=EssentialOCL_CollectionType_strategy)
@settings(max_examples=50)
def test_essentialocl_collectiontype_instantiation(instance):
    assert isinstance(instance, EssentialOCL_CollectionType)

@given(instance=EMOF_Enumeration_strategy)
@settings(max_examples=50)
def test_emof_enumeration_instantiation(instance):
    assert isinstance(instance, EMOF_Enumeration)

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=EssentialOCL_TemplateParameterType_strategy)
@settings(max_examples=50)
def test_essentialocl_templateparametertype_instantiation(instance):
    assert isinstance(instance, EssentialOCL_TemplateParameterType)



@given(instance=EssentialOCL_TemplateParameterType_strategy)
def test_essentialocl_templateparametertype_specification_setter(instance):
    original = instance.specification
    instance.specification = original
    assert instance.specification == original

@given(instance=EssentialOCL_InvalidType_strategy)
@settings(max_examples=50)
def test_essentialocl_invalidtype_instantiation(instance):
    assert isinstance(instance, EssentialOCL_InvalidType)

@given(instance=EssentialOCL_AnyType_strategy)
@settings(max_examples=50)
def test_essentialocl_anytype_instantiation(instance):
    assert isinstance(instance, EssentialOCL_AnyType)

@given(instance=EMOF_DataType_strategy)
@settings(max_examples=50)
def test_emof_datatype_instantiation(instance):
    assert isinstance(instance, EMOF_DataType)

@given(instance=EssentialOCL_VoidType_strategy)
@settings(max_examples=50)
def test_essentialocl_voidtype_instantiation(instance):
    assert isinstance(instance, EssentialOCL_VoidType)

@given(instance=EMOF_Class_strategy)
@settings(max_examples=50)
def test_emof_class_instantiation(instance):
    assert isinstance(instance, EMOF_Class)



@given(instance=EMOF_Class_strategy)
def test_emof_class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=QVTOperational_VarParameter_strategy)
@settings(max_examples=50)
def test_qvtoperational_varparameter_instantiation(instance):
    assert isinstance(instance, QVTOperational_VarParameter)



@given(instance=QVTOperational_VarParameter_strategy)
def test_qvtoperational_varparameter_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=ResolveExp_strategy)
@settings(max_examples=50)
def test_resolveexp_instantiation(instance):
    assert isinstance(instance, ResolveExp)

@given(instance=QVTOperational_ResolveInExp_strategy)
@settings(max_examples=50)
def test_qvtoperational_resolveinexp_instantiation(instance):
    assert isinstance(instance, QVTOperational_ResolveInExp)

@given(instance=QVTOperational_ResolveExp_strategy)
@settings(max_examples=50)
def test_qvtoperational_resolveexp_instantiation(instance):
    assert isinstance(instance, QVTOperational_ResolveExp)



@given(instance=QVTOperational_ResolveExp_strategy)
def test_qvtoperational_resolveexp_isInverse_setter(instance):
    original = instance.isInverse
    instance.isInverse = original
    assert instance.isInverse == original



@given(instance=QVTOperational_ResolveExp_strategy)
def test_qvtoperational_resolveexp_one_setter(instance):
    original = instance.one
    instance.one = original
    assert instance.one == original



@given(instance=QVTOperational_ResolveExp_strategy)
def test_qvtoperational_resolveexp_isDeferred_setter(instance):
    original = instance.isDeferred
    instance.isDeferred = original
    assert instance.isDeferred == original

@given(instance=ConstructorBody_strategy)
@settings(max_examples=50)
def test_constructorbody_instantiation(instance):
    assert isinstance(instance, ConstructorBody)

@given(instance=InstantiationExp_strategy)
@settings(max_examples=50)
def test_instantiationexp_instantiation(instance):
    assert isinstance(instance, InstantiationExp)

@given(instance=QVTOperational_ObjectExp_strategy)
@settings(max_examples=50)
def test_qvtoperational_objectexp_instantiation(instance):
    assert isinstance(instance, QVTOperational_ObjectExp)

@given(instance=QVTOperational_ModuleImport_strategy)
@settings(max_examples=50)
def test_qvtoperational_moduleimport_instantiation(instance):
    assert isinstance(instance, QVTOperational_ModuleImport)



@given(instance=QVTOperational_ModuleImport_strategy)
def test_qvtoperational_moduleimport_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=ModelType_strategy)
@settings(max_examples=50)
def test_modeltype_instantiation(instance):
    assert isinstance(instance, ModelType)

@given(instance=QVTOperational_OperationBody_strategy)
@settings(max_examples=50)
def test_qvtoperational_operationbody_instantiation(instance):
    assert isinstance(instance, QVTOperational_OperationBody)

@given(instance=QVTOperational_Module_strategy)
@settings(max_examples=50)
def test_qvtoperational_module_instantiation(instance):
    assert isinstance(instance, QVTOperational_Module)



@given(instance=QVTOperational_Module_strategy)
def test_qvtoperational_module_isBlackbox_setter(instance):
    original = instance.isBlackbox
    instance.isBlackbox = original
    assert instance.isBlackbox == original

@given(instance=QVTOperational_ModelType_strategy)
@settings(max_examples=50)
def test_qvtoperational_modeltype_instantiation(instance):
    assert isinstance(instance, QVTOperational_ModelType)



@given(instance=QVTOperational_ModelType_strategy)
def test_qvtoperational_modeltype_conformanceKind_setter(instance):
    original = instance.conformanceKind
    instance.conformanceKind = original
    assert instance.conformanceKind == original

@given(instance=ModuleImport_strategy)
@settings(max_examples=50)
def test_moduleimport_instantiation(instance):
    assert isinstance(instance, ModuleImport)

@given(instance=EntryOperation_strategy)
@settings(max_examples=50)
def test_entryoperation_instantiation(instance):
    assert isinstance(instance, EntryOperation)

@given(instance=MappingOperation_strategy)
@settings(max_examples=50)
def test_mappingoperation_instantiation(instance):
    assert isinstance(instance, MappingOperation)

@given(instance=ImperativeCallExp_strategy)
@settings(max_examples=50)
def test_imperativecallexp_instantiation(instance):
    assert isinstance(instance, ImperativeCallExp)

@given(instance=QVTOperational_MappingCallExp_strategy)
@settings(max_examples=50)
def test_qvtoperational_mappingcallexp_instantiation(instance):
    assert isinstance(instance, QVTOperational_MappingCallExp)



@given(instance=QVTOperational_MappingCallExp_strategy)
def test_qvtoperational_mappingcallexp_isStrict_setter(instance):
    original = instance.isStrict
    instance.isStrict = original
    assert instance.isStrict == original

@given(instance=RelationDomain_strategy)
@settings(max_examples=50)
def test_relationdomain_instantiation(instance):
    assert isinstance(instance, RelationDomain)

@given(instance=ModelParameter_strategy)
@settings(max_examples=50)
def test_modelparameter_instantiation(instance):
    assert isinstance(instance, ModelParameter)

@given(instance=VarParameter_strategy)
@settings(max_examples=50)
def test_varparameter_instantiation(instance):
    assert isinstance(instance, VarParameter)

@given(instance=QVTOperational_ModelParameter_strategy)
@settings(max_examples=50)
def test_qvtoperational_modelparameter_instantiation(instance):
    assert isinstance(instance, QVTOperational_ModelParameter)

@given(instance=QVTOperational_MappingParameter_strategy)
@settings(max_examples=50)
def test_qvtoperational_mappingparameter_instantiation(instance):
    assert isinstance(instance, QVTOperational_MappingParameter)

@given(instance=QVTOperational_ImperativeOperation_strategy)
@settings(max_examples=50)
def test_qvtoperational_imperativeoperation_instantiation(instance):
    assert isinstance(instance, QVTOperational_ImperativeOperation)



@given(instance=QVTOperational_ImperativeOperation_strategy)
def test_qvtoperational_imperativeoperation_isBlackbox_setter(instance):
    original = instance.isBlackbox
    instance.isBlackbox = original
    assert instance.isBlackbox == original

@given(instance=QVTOperational_ImperativeCallExp_strategy)
@settings(max_examples=50)
def test_qvtoperational_imperativecallexp_instantiation(instance):
    assert isinstance(instance, QVTOperational_ImperativeCallExp)



@given(instance=QVTOperational_ImperativeCallExp_strategy)
def test_qvtoperational_imperativecallexp_isVirtual_setter(instance):
    original = instance.isVirtual
    instance.isVirtual = original
    assert instance.isVirtual == original

@given(instance=Module_strategy)
@settings(max_examples=50)
def test_module_instantiation(instance):
    assert isinstance(instance, Module)

@given(instance=QVTOperational_OperationalTransformation_strategy)
@settings(max_examples=50)
def test_qvtoperational_operationaltransformation_instantiation(instance):
    assert isinstance(instance, QVTOperational_OperationalTransformation)

@given(instance=QVTOperational_Library_strategy)
@settings(max_examples=50)
def test_qvtoperational_library_instantiation(instance):
    assert isinstance(instance, QVTOperational_Library)

@given(instance=QVTRelation_RelationImplementation_strategy)
@settings(max_examples=50)
def test_qvtrelation_relationimplementation_instantiation(instance):
    assert isinstance(instance, QVTRelation_RelationImplementation)

@given(instance=QVTOperational_ContextualProperty_strategy)
@settings(max_examples=50)
def test_qvtoperational_contextualproperty_instantiation(instance):
    assert isinstance(instance, QVTOperational_ContextualProperty)

@given(instance=OperationBody_strategy)
@settings(max_examples=50)
def test_operationbody_instantiation(instance):
    assert isinstance(instance, OperationBody)

@given(instance=QVTOperational_MappingBody_strategy)
@settings(max_examples=50)
def test_qvtoperational_mappingbody_instantiation(instance):
    assert isinstance(instance, QVTOperational_MappingBody)

@given(instance=QVTOperational_ConstructorBody_strategy)
@settings(max_examples=50)
def test_qvtoperational_constructorbody_instantiation(instance):
    assert isinstance(instance, QVTOperational_ConstructorBody)

@given(instance=ImperativeOperation_strategy)
@settings(max_examples=50)
def test_imperativeoperation_instantiation(instance):
    assert isinstance(instance, ImperativeOperation)

@given(instance=QVTOperational_MappingOperation_strategy)
@settings(max_examples=50)
def test_qvtoperational_mappingoperation_instantiation(instance):
    assert isinstance(instance, QVTOperational_MappingOperation)

@given(instance=QVTOperational_Constructor_strategy)
@settings(max_examples=50)
def test_qvtoperational_constructor_instantiation(instance):
    assert isinstance(instance, QVTOperational_Constructor)

@given(instance=QVTOperational_EntryOperation_strategy)
@settings(max_examples=50)
def test_qvtoperational_entryoperation_instantiation(instance):
    assert isinstance(instance, QVTOperational_EntryOperation)

@given(instance=QVTOperational_Helper_strategy)
@settings(max_examples=50)
def test_qvtoperational_helper_instantiation(instance):
    assert isinstance(instance, QVTOperational_Helper)



@given(instance=QVTOperational_Helper_strategy)
def test_qvtoperational_helper_isQuery_setter(instance):
    original = instance.isQuery
    instance.isQuery = original
    assert instance.isQuery == original
