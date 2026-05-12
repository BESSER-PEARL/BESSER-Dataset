import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SingleEntityValue,
    instances_AggregateValue,
    core_Instance,
    express_instances_LISTValue,
    LogicalValue,
    express_instances_BooleanValue,
    NumberValue,
    express_instances_RealValue,
    express_instances_Population,
    express_instances_ArrayMember,
    instances_ConcreteValue,
    instances_TypedInstance,
    BagMember,
    LISTValue,
    express_instances_GenericAggregate,
    express_instances_SingleEntityValue,
    express_instances_BagMember,
    express_instances_ListMember,
    EntityValue,
    TypedInstance,
    express_instances_SpecializedValue,
    express_instances_EntityInstance,
    StringValue,
    express_instances_TypeName,
    express_instances_RoleName,
    ArrayMember,
    AggregateValue,
    express_instances_BAGValue,
    express_instances_SETValue,
    express_instances_ARRAYValue,
    express_instances_AttributeValue,
    core_GenericType,
    algorithms_Parameter,
    ConcreteValue,
    express_instances_SimpleValue,
    express_instances_AggregateValue,
    RealValue,
    express_instances_IntegerValue,
    AGGREGATEType,
    express_algorithms_ActualStructureConstraint,
    ActualStructure,
    express_algorithms_VARVariable,
    core_ActualType,
    EscapeStatement,
    SkipStatement,
    StatementBlock,
    express_algorithms_Statement,
    ActualType,
    express_algorithms_ActualAGGREGATEType,
    express_algorithms_ActualGenericType,
    core_AGGREGATEType,
    algorithms_GenericElement,
    express_algorithms_ActualDataType,
    express_algorithms_ActualStructure,
    InVariable,
    ActualDataType,
    GenericType,
    ActualAggregationType,
    express_algorithms_ActualLISTType,
    express_algorithms_ActualBAGType,
    express_algorithms_ActualSETType,
    express_algorithms_ActualARRAYType,
    InParameter,
    RepeatStatement,
    core_AnonymousType,
    AlgorithmScope,
    Algorithm,
    express_algorithms_Procedure,
    express_algorithms_Function,
    express_algorithms_ActualTypeConstraint,
    express_core_AggregationType,
    express_core_ScopedId,
    DomainRule,
    SelectType,
    core_CommonElement,
    core_Scope,
    express_core_Relationship,
    express_core_ParameterType,
    express_core_Scope,
    express_core_Role,
    express_core_Remark,
    ArrayBound,
    ConcreteType,
    LocalScope,
    express_core_AlgorithmScope,
    AnonymousType,
    express_core_SimpleType,
    LengthConstraint,
    ActualTypeConstraint,
    NumericType,
    express_core_RealType,
    DomainConstraint,
    express_core_SizeConstraint,
    express_core_LengthConstraint,
    express_core_AttributeType,
    express_core_Instance,
    express_core_NamedElement,
    core_VariableType,
    express_core_DomainConstraint,
    TypeElement,
    express_core_UniqueRule,
    core_ConcreteType,
    SimpleType,
    express_core_StringType,
    express_core_BinaryType,
    express_core_LogicType,
    express_core_NumericType,
    express_core_Attribute,
    Relationship,
    InverseAttribute,
    SchemaElement,
    express_core_CommonElement,
    InterfacedElement,
    Remark,
    express_core_DataType,
    Schema,
    express_core_InterfacedElement,
    core_ParameterType,
    express_core_InstantiableType,
    core_InstantiableType,
    express_core_AnonymousType,
    core_NamedType,
    express_core_DefinedType,
    express_core_EntityType,
    Role,
    express_core_RangeRole,
    express_core_DomainRole,
    Redeclaration,
    AttributeType,
    express_core_Redeclaration,
    IndexOperation,
    express_expressions_BinaryIndex,
    SimpleValue,
    express_instances_NumberValue,
    express_instances_BinaryValue,
    express_instances_LogicalValue,
    express_instances_StringValue,
    EnumerationItem,
    Primary,
    express_expressions_Literal,
    express_expressions_EnumItemRef,
    express_expressions_RepeatCount,
    express_expressions_SELFRef,
    Indeterminate,
    CaseAction,
    Variable,
    express_algorithms_FunctionResult,
    express_algorithms_InVariable,
    express_algorithms_LocalVariable,
    SingleEntityType,
    ControlVariable,
    ExplicitAttribute,
    express_core_InvertibleAttribute,
    express_statements_VARExpression,
    VARVariable,
    algorithms_VARVariable,
    express_algorithms_VARParameter,
    algorithms_NamedVariable,
    express_statements_AliasVariable,
    NamedVariable,
    express_algorithms_Variable,
    express_statements_ControlVariable,
    AliasVariable,
    VARExpression,
    express_statements_AttributeCell,
    express_statements_GroupCell,
    express_statements_MemberCell,
    express_statements_VARCell,
    express_statements_VariableCell,
    core_LocalScope,
    algorithms_Statement,
    express_statements_RepeatStatement,
    express_statements_AliasStatement,
    ControlStatement,
    express_statements_ReturnStatement,
    express_statements_EscapeStatement,
    express_statements_NullStatement,
    express_statements_SkipStatement,
    express_statements_CaseAction,
    LocalElement,
    express_algorithms_GenericElement,
    express_algorithms_NamedVariable,
    express_algorithms_Parameter,
    express_rules_NamedRule,
    NamedRule,
    Statement,
    express_statements_IfStatement,
    express_statements_Assignment,
    express_statements_StatementBlock,
    express_statements_CaseStatement,
    express_statements_ControlStatement,
    core_AlgorithmScope,
    express_algorithms_Algorithm,
    core_SchemaElement,
    express_rules_GlobalRule,
    ScopedId,
    GlobalRule,
    Population,
    EntityInstance,
    express_instances_SingleLeafInstance,
    express_instances_MultiLeafInstance,
    SETValue,
    express_rules_Extent,
    SupertypeRule,
    Expression,
    express_expressions_IndexOperation,
    express_expressions_Selector,
    Extent,
    express_rules_SubtypeConstraint,
    ActualParameter,
    Procedure,
    express_statements_ProcedureCall,
    EntityType,
    CommonElement,
    express_instances_Constant,
    express_rules_SupertypeRule,
    SubtypeConstraint,
    express_rules_ANDConstraint,
    express_rules_TOTAL_OVERConstraint,
    express_rules_ONEOFConstraint,
    ConcreteAggregationType,
    express_core_ARRAYType,
    express_core_SETType,
    express_core_BAGType,
    express_core_LISTType,
    UniqueRule,
    RangeRole,
    DefinedType,
    express_core_SpecializedType,
    express_core_SelectType,
    express_core_EnumerationType,
    InvertibleAttribute,
    DomainRole,
    DataType,
    express_core_PartialEntityType,
    Scope,
    express_core_LocalScope,
    express_core_Schema,
    Instance,
    express_instances_PartialEntityValue,
    express_instances_Indeterminate,
    express_instances_TypedInstance,
    express_instances_ConcreteValue,
    express_core_Expression,
    InstantiableType,
    express_core_ConcreteType,
    core_AggregationType,
    express_core_ConcreteAggregationType,
    express_algorithms_ActualAggregationType,
    core_GeneralizedType,
    express_core_GeneralAggregationType,
    core_TypeElement,
    express_instances_EnumerationItem,
    core_DomainConstraint,
    express_core_DomainRule,
    GeneralAggregationType,
    express_core_GeneralSETType,
    express_core_GeneralARRAYType,
    express_core_GeneralLISTType,
    express_core_GeneralBAGType,
    ActualStructureConstraint,
    ParameterType,
    express_core_ArrayBound,
    core_AttributeType,
    express_core_NamedType,
    express_core_GeneralizedType,
    core_DataType,
    express_core_VariableType,
    EnumerationType,
    express_expressions_VariableRef,
    NamedType,
    express_expressions_ExtentRef,
    ListMember,
    RepeatCount,
    express_expressions_MemberBinding,
    FunctionResult,
    Function,
    express_expressions_FunctionCall,
    SizeConstraint,
    GeneralizedType,
    express_core_GenericType,
    express_core_AGGREGATEType,
    PartialEntityType,
    express_core_SingleEntityType,
    NamedElement,
    express_core_SchemaElement,
    express_core_LocalElement,
    express_core_TypeElement,
    core_Expression,
    express_expressions_QueryExpression,
    Constant,
    express_expressions_ConstantRef,
    express_expressions_AggregateIndex,
    Attribute,
    express_core_InverseAttribute,
    express_core_ExplicitAttribute,
    express_core_DerivedAttribute,
    Selector,
    express_expressions_UsedInRef,
    express_expressions_GroupRef,
    express_expressions_AttributeRef,
    AttributeValue,
    express_expressions_AttributeBinding,
    express_expressions_Operation,
    express_expressions_QueryVariable,
    QueryVariable,
    express_expressions_Primary,
    VariableType,
    express_core_ActualType,
    AttributeBinding,
    PartialEntityValue,
    express_instances_EntityValue,
    express_expressions_PartialEntityConstructor,
    express_expressions_StringIndex,
    MemberBinding,
    GenericAggregate,
    express_expressions_AggregateInitializer,
    express_expressions_ParameterRef,
    Operation,
    express_expressions_UnaryOperation,
    express_expressions_Coercion,
    express_expressions_BinaryOperation,
    Parameter,
    express_algorithms_InParameter,
    FunctionCall,
    ProcedureCall,
    express_expressions_IndeterminateRef,
    express_expressions_ActualParameter,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_singleentityvalue_is_not_abstract():
    assert not inspect.isabstract(SingleEntityValue)


def test_singleentityvalue_constructor_exists():
    assert callable(SingleEntityValue.__init__)


def test_singleentityvalue_constructor_args():
    sig = inspect.signature(SingleEntityValue.__init__)
    params = list(sig.parameters.keys())



def test_instances_aggregatevalue_is_not_abstract():
    assert not inspect.isabstract(instances_AggregateValue)


def test_instances_aggregatevalue_constructor_exists():
    assert callable(instances_AggregateValue.__init__)


def test_instances_aggregatevalue_constructor_args():
    sig = inspect.signature(instances_AggregateValue.__init__)
    params = list(sig.parameters.keys())



def test_core_instance_is_not_abstract():
    assert not inspect.isabstract(core_Instance)


def test_core_instance_constructor_exists():
    assert callable(core_Instance.__init__)


def test_core_instance_constructor_args():
    sig = inspect.signature(core_Instance.__init__)
    params = list(sig.parameters.keys())



def test_express_instances_listvalue_is_not_abstract():
    assert not inspect.isabstract(express_instances_LISTValue)


def test_express_instances_listvalue_constructor_exists():
    assert callable(express_instances_LISTValue.__init__)


def test_express_instances_listvalue_constructor_args():
    sig = inspect.signature(express_instances_LISTValue.__init__)
    params = list(sig.parameters.keys())



def test_logicalvalue_is_not_abstract():
    assert not inspect.isabstract(LogicalValue)


def test_logicalvalue_constructor_exists():
    assert callable(LogicalValue.__init__)


def test_logicalvalue_constructor_args():
    sig = inspect.signature(LogicalValue.__init__)
    params = list(sig.parameters.keys())



def test_express_instances_booleanvalue_is_not_abstract():
    assert not inspect.isabstract(express_instances_BooleanValue)


def test_express_instances_booleanvalue_constructor_exists():
    assert callable(express_instances_BooleanValue.__init__)


def test_express_instances_booleanvalue_constructor_args():
    sig = inspect.signature(express_instances_BooleanValue.__init__)
    params = list(sig.parameters.keys())



def test_numbervalue_is_not_abstract():
    assert not inspect.isabstract(NumberValue)


def test_numbervalue_constructor_exists():
    assert callable(NumberValue.__init__)


def test_numbervalue_constructor_args():
    sig = inspect.signature(NumberValue.__init__)
    params = list(sig.parameters.keys())



def test_express_instances_realvalue_is_not_abstract():
    assert not inspect.isabstract(express_instances_RealValue)


def test_express_instances_realvalue_constructor_exists():
    assert callable(express_instances_RealValue.__init__)


def test_express_instances_realvalue_constructor_args():
    sig = inspect.signature(express_instances_RealValue.__init__)
    params = list(sig.parameters.keys())



def test_express_instances_population_is_not_abstract():
    assert not inspect.isabstract(express_instances_Population)


def test_express_instances_population_constructor_exists():
    assert callable(express_instances_Population.__init__)


def test_express_instances_population_constructor_args():
    sig = inspect.signature(express_instances_Population.__init__)
    params = list(sig.parameters.keys())



def test_express_instances_arraymember_is_not_abstract():
    assert not inspect.isabstract(express_instances_ArrayMember)


def test_express_instances_arraymember_constructor_exists():
    assert callable(express_instances_ArrayMember.__init__)


def test_express_instances_arraymember_constructor_args():
    sig = inspect.signature(express_instances_ArrayMember.__init__)
    params = list(sig.parameters.keys())
    assert "index" in params, "Missing parameter 'index'"

def test_express_instances_arraymember_has_index():
    assert hasattr(express_instances_ArrayMember, "index")
    descriptor = None
    for klass in express_instances_ArrayMember.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)



def test_instances_concretevalue_is_not_abstract():
    assert not inspect.isabstract(instances_ConcreteValue)


def test_instances_concretevalue_constructor_exists():
    assert callable(instances_ConcreteValue.__init__)


def test_instances_concretevalue_constructor_args():
    sig = inspect.signature(instances_ConcreteValue.__init__)
    params = list(sig.parameters.keys())



def test_instances_typedinstance_is_not_abstract():
    assert not inspect.isabstract(instances_TypedInstance)


def test_instances_typedinstance_constructor_exists():
    assert callable(instances_TypedInstance.__init__)


def test_instances_typedinstance_constructor_args():
    sig = inspect.signature(instances_TypedInstance.__init__)
    params = list(sig.parameters.keys())



def test_bagmember_is_not_abstract():
    assert not inspect.isabstract(BagMember)


def test_bagmember_constructor_exists():
    assert callable(BagMember.__init__)


def test_bagmember_constructor_args():
    sig = inspect.signature(BagMember.__init__)
    params = list(sig.parameters.keys())



def test_listvalue_is_not_abstract():
    assert not inspect.isabstract(LISTValue)


def test_listvalue_constructor_exists():
    assert callable(LISTValue.__init__)


def test_listvalue_constructor_args():
    sig = inspect.signature(LISTValue.__init__)
    params = list(sig.parameters.keys())



def test_express_instances_genericaggregate_is_not_abstract():
    assert not inspect.isabstract(express_instances_GenericAggregate)


def test_express_instances_genericaggregate_constructor_exists():
    assert callable(express_instances_GenericAggregate.__init__)


def test_express_instances_genericaggregate_constructor_args():
    sig = inspect.signature(express_instances_GenericAggregate.__init__)
    params = list(sig.parameters.keys())



def test_express_instances_singleentityvalue_is_not_abstract():
    assert not inspect.isabstract(express_instances_SingleEntityValue)


def test_express_instances_singleentityvalue_constructor_exists():
    assert callable(express_instances_SingleEntityValue.__init__)


def test_express_instances_singleentityvalue_constructor_args():
    sig = inspect.signature(express_instances_SingleEntityValue.__init__)
    params = list(sig.parameters.keys())



def test_express_instances_bagmember_is_not_abstract():
    assert not inspect.isabstract(express_instances_BagMember)


def test_express_instances_bagmember_constructor_exists():
    assert callable(express_instances_BagMember.__init__)


def test_express_instances_bagmember_constructor_args():
    sig = inspect.signature(express_instances_BagMember.__init__)
    params = list(sig.parameters.keys())
    assert "count" in params, "Missing parameter 'count'"

def test_express_instances_bagmember_has_count():
    assert hasattr(express_instances_BagMember, "count")
    descriptor = None
    for klass in express_instances_BagMember.__mro__:
        if "count" in klass.__dict__:
            descriptor = klass.__dict__["count"]
            break
    assert isinstance(descriptor, property)



def test_express_instances_listmember_is_not_abstract():
    assert not inspect.isabstract(express_instances_ListMember)


def test_express_instances_listmember_constructor_exists():
    assert callable(express_instances_ListMember.__init__)


def test_express_instances_listmember_constructor_args():
    sig = inspect.signature(express_instances_ListMember.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_express_instances_listmember_has_position():
    assert hasattr(express_instances_ListMember, "position")
    descriptor = None
    for klass in express_instances_ListMember.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_entityvalue_is_not_abstract():
    assert not inspect.isabstract(EntityValue)


def test_entityvalue_constructor_exists():
    assert callable(EntityValue.__init__)


def test_entityvalue_constructor_args():
    sig = inspect.signature(EntityValue.__init__)
    params = list(sig.parameters.keys())



def test_typedinstance_is_not_abstract():
    assert not inspect.isabstract(TypedInstance)


def test_typedinstance_constructor_exists():
    assert callable(TypedInstance.__init__)


def test_typedinstance_constructor_args():
    sig = inspect.signature(TypedInstance.__init__)
    params = list(sig.parameters.keys())



def test_express_instances_specializedvalue_is_not_abstract():
    assert not inspect.isabstract(express_instances_SpecializedValue)


def test_express_instances_specializedvalue_constructor_exists():
    assert callable(express_instances_SpecializedValue.__init__)


def test_express_instances_specializedvalue_constructor_args():
    sig = inspect.signature(express_instances_SpecializedValue.__init__)
    params = list(sig.parameters.keys())



def test_express_instances_entityinstance_is_not_abstract():
    assert not inspect.isabstract(express_instances_EntityInstance)


def test_express_instances_entityinstance_constructor_exists():
    assert callable(express_instances_EntityInstance.__init__)


def test_express_instances_entityinstance_constructor_args():
    sig = inspect.signature(express_instances_EntityInstance.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_express_instances_entityinstance_has_id():
    assert hasattr(express_instances_EntityInstance, "id")
    descriptor = None
    for klass in express_instances_EntityInstance.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_stringvalue_is_not_abstract():
    assert not inspect.isabstract(StringValue)


def test_stringvalue_constructor_exists():
    assert callable(StringValue.__init__)


def test_stringvalue_constructor_args():
    sig = inspect.signature(StringValue.__init__)
    params = list(sig.parameters.keys())



def test_express_instances_typename_is_not_abstract():
    assert not inspect.isabstract(express_instances_TypeName)


def test_express_instances_typename_constructor_exists():
    assert callable(express_instances_TypeName.__init__)


def test_express_instances_typename_constructor_args():
    sig = inspect.signature(express_instances_TypeName.__init__)
    params = list(sig.parameters.keys())



def test_express_instances_rolename_is_not_abstract():
    assert not inspect.isabstract(express_instances_RoleName)


def test_express_instances_rolename_constructor_exists():
    assert callable(express_instances_RoleName.__init__)


def test_express_instances_rolename_constructor_args():
    sig = inspect.signature(express_instances_RoleName.__init__)
    params = list(sig.parameters.keys())



def test_arraymember_is_not_abstract():
    assert not inspect.isabstract(ArrayMember)


def test_arraymember_constructor_exists():
    assert callable(ArrayMember.__init__)


def test_arraymember_constructor_args():
    sig = inspect.signature(ArrayMember.__init__)
    params = list(sig.parameters.keys())



def test_aggregatevalue_is_not_abstract():
    assert not inspect.isabstract(AggregateValue)


def test_aggregatevalue_constructor_exists():
    assert callable(AggregateValue.__init__)


def test_aggregatevalue_constructor_args():
    sig = inspect.signature(AggregateValue.__init__)
    params = list(sig.parameters.keys())



def test_express_instances_bagvalue_is_not_abstract():
    assert not inspect.isabstract(express_instances_BAGValue)


def test_express_instances_bagvalue_constructor_exists():
    assert callable(express_instances_BAGValue.__init__)


def test_express_instances_bagvalue_constructor_args():
    sig = inspect.signature(express_instances_BAGValue.__init__)
    params = list(sig.parameters.keys())



def test_express_instances_setvalue_is_not_abstract():
    assert not inspect.isabstract(express_instances_SETValue)


def test_express_instances_setvalue_constructor_exists():
    assert callable(express_instances_SETValue.__init__)


def test_express_instances_setvalue_constructor_args():
    sig = inspect.signature(express_instances_SETValue.__init__)
    params = list(sig.parameters.keys())



def test_express_instances_arrayvalue_is_not_abstract():
    assert not inspect.isabstract(express_instances_ARRAYValue)


def test_express_instances_arrayvalue_constructor_exists():
    assert callable(express_instances_ARRAYValue.__init__)


def test_express_instances_arrayvalue_constructor_args():
    sig = inspect.signature(express_instances_ARRAYValue.__init__)
    params = list(sig.parameters.keys())



def test_express_instances_attributevalue_is_not_abstract():
    assert not inspect.isabstract(express_instances_AttributeValue)


def test_express_instances_attributevalue_constructor_exists():
    assert callable(express_instances_AttributeValue.__init__)


def test_express_instances_attributevalue_constructor_args():
    sig = inspect.signature(express_instances_AttributeValue.__init__)
    params = list(sig.parameters.keys())



def test_core_generictype_is_not_abstract():
    assert not inspect.isabstract(core_GenericType)


def test_core_generictype_constructor_exists():
    assert callable(core_GenericType.__init__)


def test_core_generictype_constructor_args():
    sig = inspect.signature(core_GenericType.__init__)
    params = list(sig.parameters.keys())



def test_algorithms_parameter_is_not_abstract():
    assert not inspect.isabstract(algorithms_Parameter)


def test_algorithms_parameter_constructor_exists():
    assert callable(algorithms_Parameter.__init__)


def test_algorithms_parameter_constructor_args():
    sig = inspect.signature(algorithms_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_concretevalue_is_not_abstract():
    assert not inspect.isabstract(ConcreteValue)


def test_concretevalue_constructor_exists():
    assert callable(ConcreteValue.__init__)


def test_concretevalue_constructor_args():
    sig = inspect.signature(ConcreteValue.__init__)
    params = list(sig.parameters.keys())



def test_express_instances_simplevalue_is_not_abstract():
    assert not inspect.isabstract(express_instances_SimpleValue)


def test_express_instances_simplevalue_constructor_exists():
    assert callable(express_instances_SimpleValue.__init__)


def test_express_instances_simplevalue_constructor_args():
    sig = inspect.signature(express_instances_SimpleValue.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_express_instances_simplevalue_has_name():
    assert hasattr(express_instances_SimpleValue, "name")
    descriptor = None
    for klass in express_instances_SimpleValue.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_express_instances_aggregatevalue_is_not_abstract():
    assert not inspect.isabstract(express_instances_AggregateValue)


def test_express_instances_aggregatevalue_constructor_exists():
    assert callable(express_instances_AggregateValue.__init__)


def test_express_instances_aggregatevalue_constructor_args():
    sig = inspect.signature(express_instances_AggregateValue.__init__)
    params = list(sig.parameters.keys())



def test_realvalue_is_not_abstract():
    assert not inspect.isabstract(RealValue)


def test_realvalue_constructor_exists():
    assert callable(RealValue.__init__)


def test_realvalue_constructor_args():
    sig = inspect.signature(RealValue.__init__)
    params = list(sig.parameters.keys())



def test_express_instances_integervalue_is_not_abstract():
    assert not inspect.isabstract(express_instances_IntegerValue)


def test_express_instances_integervalue_constructor_exists():
    assert callable(express_instances_IntegerValue.__init__)


def test_express_instances_integervalue_constructor_args():
    sig = inspect.signature(express_instances_IntegerValue.__init__)
    params = list(sig.parameters.keys())



def test_aggregatetype_is_not_abstract():
    assert not inspect.isabstract(AGGREGATEType)


def test_aggregatetype_constructor_exists():
    assert callable(AGGREGATEType.__init__)


def test_aggregatetype_constructor_args():
    sig = inspect.signature(AGGREGATEType.__init__)
    params = list(sig.parameters.keys())



def test_express_algorithms_actualstructureconstraint_is_not_abstract():
    assert not inspect.isabstract(express_algorithms_ActualStructureConstraint)


def test_express_algorithms_actualstructureconstraint_constructor_exists():
    assert callable(express_algorithms_ActualStructureConstraint.__init__)


def test_express_algorithms_actualstructureconstraint_constructor_args():
    sig = inspect.signature(express_algorithms_ActualStructureConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_express_algorithms_actualstructureconstraint_has_label():
    assert hasattr(express_algorithms_ActualStructureConstraint, "label")
    descriptor = None
    for klass in express_algorithms_ActualStructureConstraint.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_actualstructure_is_not_abstract():
    assert not inspect.isabstract(ActualStructure)


def test_actualstructure_constructor_exists():
    assert callable(ActualStructure.__init__)


def test_actualstructure_constructor_args():
    sig = inspect.signature(ActualStructure.__init__)
    params = list(sig.parameters.keys())



def test_express_algorithms_varvariable_is_not_abstract():
    assert not inspect.isabstract(express_algorithms_VARVariable)


def test_express_algorithms_varvariable_constructor_exists():
    assert callable(express_algorithms_VARVariable.__init__)


def test_express_algorithms_varvariable_constructor_args():
    sig = inspect.signature(express_algorithms_VARVariable.__init__)
    params = list(sig.parameters.keys())



def test_core_actualtype_is_not_abstract():
    assert not inspect.isabstract(core_ActualType)


def test_core_actualtype_constructor_exists():
    assert callable(core_ActualType.__init__)


def test_core_actualtype_constructor_args():
    sig = inspect.signature(core_ActualType.__init__)
    params = list(sig.parameters.keys())



def test_escapestatement_is_not_abstract():
    assert not inspect.isabstract(EscapeStatement)


def test_escapestatement_constructor_exists():
    assert callable(EscapeStatement.__init__)


def test_escapestatement_constructor_args():
    sig = inspect.signature(EscapeStatement.__init__)
    params = list(sig.parameters.keys())



def test_skipstatement_is_not_abstract():
    assert not inspect.isabstract(SkipStatement)


def test_skipstatement_constructor_exists():
    assert callable(SkipStatement.__init__)


def test_skipstatement_constructor_args():
    sig = inspect.signature(SkipStatement.__init__)
    params = list(sig.parameters.keys())



def test_statementblock_is_not_abstract():
    assert not inspect.isabstract(StatementBlock)


def test_statementblock_constructor_exists():
    assert callable(StatementBlock.__init__)


def test_statementblock_constructor_args():
    sig = inspect.signature(StatementBlock.__init__)
    params = list(sig.parameters.keys())



def test_express_algorithms_statement_is_not_abstract():
    assert not inspect.isabstract(express_algorithms_Statement)


def test_express_algorithms_statement_constructor_exists():
    assert callable(express_algorithms_Statement.__init__)


def test_express_algorithms_statement_constructor_args():
    sig = inspect.signature(express_algorithms_Statement.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_express_algorithms_statement_has_text():
    assert hasattr(express_algorithms_Statement, "text")
    descriptor = None
    for klass in express_algorithms_Statement.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_actualtype_is_not_abstract():
    assert not inspect.isabstract(ActualType)


def test_actualtype_constructor_exists():
    assert callable(ActualType.__init__)


def test_actualtype_constructor_args():
    sig = inspect.signature(ActualType.__init__)
    params = list(sig.parameters.keys())



def test_express_algorithms_actualaggregatetype_is_not_abstract():
    assert not inspect.isabstract(express_algorithms_ActualAGGREGATEType)


def test_express_algorithms_actualaggregatetype_constructor_exists():
    assert callable(express_algorithms_ActualAGGREGATEType.__init__)


def test_express_algorithms_actualaggregatetype_constructor_args():
    sig = inspect.signature(express_algorithms_ActualAGGREGATEType.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_express_algorithms_actualaggregatetype_has_label():
    assert hasattr(express_algorithms_ActualAGGREGATEType, "label")
    descriptor = None
    for klass in express_algorithms_ActualAGGREGATEType.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_express_algorithms_actualgenerictype_is_not_abstract():
    assert not inspect.isabstract(express_algorithms_ActualGenericType)


def test_express_algorithms_actualgenerictype_constructor_exists():
    assert callable(express_algorithms_ActualGenericType.__init__)


def test_express_algorithms_actualgenerictype_constructor_args():
    sig = inspect.signature(express_algorithms_ActualGenericType.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "isEntity" in params, "Missing parameter 'isEntity'"

def test_express_algorithms_actualgenerictype_has_label():
    assert hasattr(express_algorithms_ActualGenericType, "label")
    descriptor = None
    for klass in express_algorithms_ActualGenericType.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_express_algorithms_actualgenerictype_has_isEntity():
    assert hasattr(express_algorithms_ActualGenericType, "isEntity")
    descriptor = None
    for klass in express_algorithms_ActualGenericType.__mro__:
        if "isEntity" in klass.__dict__:
            descriptor = klass.__dict__["isEntity"]
            break
    assert isinstance(descriptor, property)



def test_core_aggregatetype_is_not_abstract():
    assert not inspect.isabstract(core_AGGREGATEType)


def test_core_aggregatetype_constructor_exists():
    assert callable(core_AGGREGATEType.__init__)


def test_core_aggregatetype_constructor_args():
    sig = inspect.signature(core_AGGREGATEType.__init__)
    params = list(sig.parameters.keys())



def test_algorithms_genericelement_is_not_abstract():
    assert not inspect.isabstract(algorithms_GenericElement)


def test_algorithms_genericelement_constructor_exists():
    assert callable(algorithms_GenericElement.__init__)


def test_algorithms_genericelement_constructor_args():
    sig = inspect.signature(algorithms_GenericElement.__init__)
    params = list(sig.parameters.keys())



def test_express_algorithms_actualdatatype_is_not_abstract():
    assert not inspect.isabstract(express_algorithms_ActualDataType)


def test_express_algorithms_actualdatatype_constructor_exists():
    assert callable(express_algorithms_ActualDataType.__init__)


def test_express_algorithms_actualdatatype_constructor_args():
    sig = inspect.signature(express_algorithms_ActualDataType.__init__)
    params = list(sig.parameters.keys())



def test_express_algorithms_actualstructure_is_not_abstract():
    assert not inspect.isabstract(express_algorithms_ActualStructure)


def test_express_algorithms_actualstructure_constructor_exists():
    assert callable(express_algorithms_ActualStructure.__init__)


def test_express_algorithms_actualstructure_constructor_args():
    sig = inspect.signature(express_algorithms_ActualStructure.__init__)
    params = list(sig.parameters.keys())



def test_invariable_is_not_abstract():
    assert not inspect.isabstract(InVariable)


def test_invariable_constructor_exists():
    assert callable(InVariable.__init__)


def test_invariable_constructor_args():
    sig = inspect.signature(InVariable.__init__)
    params = list(sig.parameters.keys())



def test_actualdatatype_is_not_abstract():
    assert not inspect.isabstract(ActualDataType)


def test_actualdatatype_constructor_exists():
    assert callable(ActualDataType.__init__)


def test_actualdatatype_constructor_args():
    sig = inspect.signature(ActualDataType.__init__)
    params = list(sig.parameters.keys())



def test_generictype_is_not_abstract():
    assert not inspect.isabstract(GenericType)


def test_generictype_constructor_exists():
    assert callable(GenericType.__init__)


def test_generictype_constructor_args():
    sig = inspect.signature(GenericType.__init__)
    params = list(sig.parameters.keys())



def test_actualaggregationtype_is_not_abstract():
    assert not inspect.isabstract(ActualAggregationType)


def test_actualaggregationtype_constructor_exists():
    assert callable(ActualAggregationType.__init__)


def test_actualaggregationtype_constructor_args():
    sig = inspect.signature(ActualAggregationType.__init__)
    params = list(sig.parameters.keys())



def test_express_algorithms_actuallisttype_is_not_abstract():
    assert not inspect.isabstract(express_algorithms_ActualLISTType)


def test_express_algorithms_actuallisttype_constructor_exists():
    assert callable(express_algorithms_ActualLISTType.__init__)


def test_express_algorithms_actuallisttype_constructor_args():
    sig = inspect.signature(express_algorithms_ActualLISTType.__init__)
    params = list(sig.parameters.keys())



def test_express_algorithms_actualbagtype_is_not_abstract():
    assert not inspect.isabstract(express_algorithms_ActualBAGType)


def test_express_algorithms_actualbagtype_constructor_exists():
    assert callable(express_algorithms_ActualBAGType.__init__)


def test_express_algorithms_actualbagtype_constructor_args():
    sig = inspect.signature(express_algorithms_ActualBAGType.__init__)
    params = list(sig.parameters.keys())



def test_express_algorithms_actualsettype_is_not_abstract():
    assert not inspect.isabstract(express_algorithms_ActualSETType)


def test_express_algorithms_actualsettype_constructor_exists():
    assert callable(express_algorithms_ActualSETType.__init__)


def test_express_algorithms_actualsettype_constructor_args():
    sig = inspect.signature(express_algorithms_ActualSETType.__init__)
    params = list(sig.parameters.keys())



def test_express_algorithms_actualarraytype_is_not_abstract():
    assert not inspect.isabstract(express_algorithms_ActualARRAYType)


def test_express_algorithms_actualarraytype_constructor_exists():
    assert callable(express_algorithms_ActualARRAYType.__init__)


def test_express_algorithms_actualarraytype_constructor_args():
    sig = inspect.signature(express_algorithms_ActualARRAYType.__init__)
    params = list(sig.parameters.keys())
    assert "isOptional" in params, "Missing parameter 'isOptional'"

def test_express_algorithms_actualarraytype_has_isOptional():
    assert hasattr(express_algorithms_ActualARRAYType, "isOptional")
    descriptor = None
    for klass in express_algorithms_ActualARRAYType.__mro__:
        if "isOptional" in klass.__dict__:
            descriptor = klass.__dict__["isOptional"]
            break
    assert isinstance(descriptor, property)



def test_inparameter_is_not_abstract():
    assert not inspect.isabstract(InParameter)


def test_inparameter_constructor_exists():
    assert callable(InParameter.__init__)


def test_inparameter_constructor_args():
    sig = inspect.signature(InParameter.__init__)
    params = list(sig.parameters.keys())



def test_repeatstatement_is_not_abstract():
    assert not inspect.isabstract(RepeatStatement)


def test_repeatstatement_constructor_exists():
    assert callable(RepeatStatement.__init__)


def test_repeatstatement_constructor_args():
    sig = inspect.signature(RepeatStatement.__init__)
    params = list(sig.parameters.keys())



def test_core_anonymoustype_is_not_abstract():
    assert not inspect.isabstract(core_AnonymousType)


def test_core_anonymoustype_constructor_exists():
    assert callable(core_AnonymousType.__init__)


def test_core_anonymoustype_constructor_args():
    sig = inspect.signature(core_AnonymousType.__init__)
    params = list(sig.parameters.keys())



def test_algorithmscope_is_not_abstract():
    assert not inspect.isabstract(AlgorithmScope)


def test_algorithmscope_constructor_exists():
    assert callable(AlgorithmScope.__init__)


def test_algorithmscope_constructor_args():
    sig = inspect.signature(AlgorithmScope.__init__)
    params = list(sig.parameters.keys())



def test_algorithm_is_not_abstract():
    assert not inspect.isabstract(Algorithm)


def test_algorithm_constructor_exists():
    assert callable(Algorithm.__init__)


def test_algorithm_constructor_args():
    sig = inspect.signature(Algorithm.__init__)
    params = list(sig.parameters.keys())



def test_express_algorithms_procedure_is_not_abstract():
    assert not inspect.isabstract(express_algorithms_Procedure)


def test_express_algorithms_procedure_constructor_exists():
    assert callable(express_algorithms_Procedure.__init__)


def test_express_algorithms_procedure_constructor_args():
    sig = inspect.signature(express_algorithms_Procedure.__init__)
    params = list(sig.parameters.keys())



def test_express_algorithms_function_is_not_abstract():
    assert not inspect.isabstract(express_algorithms_Function)


def test_express_algorithms_function_constructor_exists():
    assert callable(express_algorithms_Function.__init__)


def test_express_algorithms_function_constructor_args():
    sig = inspect.signature(express_algorithms_Function.__init__)
    params = list(sig.parameters.keys())



def test_express_algorithms_actualtypeconstraint_is_not_abstract():
    assert not inspect.isabstract(express_algorithms_ActualTypeConstraint)


def test_express_algorithms_actualtypeconstraint_constructor_exists():
    assert callable(express_algorithms_ActualTypeConstraint.__init__)


def test_express_algorithms_actualtypeconstraint_constructor_args():
    sig = inspect.signature(express_algorithms_ActualTypeConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_express_algorithms_actualtypeconstraint_has_label():
    assert hasattr(express_algorithms_ActualTypeConstraint, "label")
    descriptor = None
    for klass in express_algorithms_ActualTypeConstraint.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_express_core_aggregationtype_is_not_abstract():
    assert not inspect.isabstract(express_core_AggregationType)


def test_express_core_aggregationtype_constructor_exists():
    assert callable(express_core_AggregationType.__init__)


def test_express_core_aggregationtype_constructor_args():
    sig = inspect.signature(express_core_AggregationType.__init__)
    params = list(sig.parameters.keys())
    assert "ordering" in params, "Missing parameter 'ordering'"
    assert "isUnique" in params, "Missing parameter 'isUnique'"

def test_express_core_aggregationtype_has_ordering():
    assert hasattr(express_core_AggregationType, "ordering")
    descriptor = None
    for klass in express_core_AggregationType.__mro__:
        if "ordering" in klass.__dict__:
            descriptor = klass.__dict__["ordering"]
            break
    assert isinstance(descriptor, property)

def test_express_core_aggregationtype_has_isUnique():
    assert hasattr(express_core_AggregationType, "isUnique")
    descriptor = None
    for klass in express_core_AggregationType.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)



def test_express_core_scopedid_is_not_abstract():
    assert not inspect.isabstract(express_core_ScopedId)


def test_express_core_scopedid_constructor_exists():
    assert callable(express_core_ScopedId.__init__)


def test_express_core_scopedid_constructor_args():
    sig = inspect.signature(express_core_ScopedId.__init__)
    params = list(sig.parameters.keys())
    assert "localName" in params, "Missing parameter 'localName'"

def test_express_core_scopedid_has_localName():
    assert hasattr(express_core_ScopedId, "localName")
    descriptor = None
    for klass in express_core_ScopedId.__mro__:
        if "localName" in klass.__dict__:
            descriptor = klass.__dict__["localName"]
            break
    assert isinstance(descriptor, property)



def test_domainrule_is_not_abstract():
    assert not inspect.isabstract(DomainRule)


def test_domainrule_constructor_exists():
    assert callable(DomainRule.__init__)


def test_domainrule_constructor_args():
    sig = inspect.signature(DomainRule.__init__)
    params = list(sig.parameters.keys())



def test_selecttype_is_not_abstract():
    assert not inspect.isabstract(SelectType)


def test_selecttype_constructor_exists():
    assert callable(SelectType.__init__)


def test_selecttype_constructor_args():
    sig = inspect.signature(SelectType.__init__)
    params = list(sig.parameters.keys())



def test_core_commonelement_is_not_abstract():
    assert not inspect.isabstract(core_CommonElement)


def test_core_commonelement_constructor_exists():
    assert callable(core_CommonElement.__init__)


def test_core_commonelement_constructor_args():
    sig = inspect.signature(core_CommonElement.__init__)
    params = list(sig.parameters.keys())



def test_core_scope_is_not_abstract():
    assert not inspect.isabstract(core_Scope)


def test_core_scope_constructor_exists():
    assert callable(core_Scope.__init__)


def test_core_scope_constructor_args():
    sig = inspect.signature(core_Scope.__init__)
    params = list(sig.parameters.keys())



def test_express_core_relationship_is_not_abstract():
    assert not inspect.isabstract(express_core_Relationship)


def test_express_core_relationship_constructor_exists():
    assert callable(express_core_Relationship.__init__)


def test_express_core_relationship_constructor_args():
    sig = inspect.signature(express_core_Relationship.__init__)
    params = list(sig.parameters.keys())



def test_express_core_parametertype_is_not_abstract():
    assert not inspect.isabstract(express_core_ParameterType)


def test_express_core_parametertype_constructor_exists():
    assert callable(express_core_ParameterType.__init__)


def test_express_core_parametertype_constructor_args():
    sig = inspect.signature(express_core_ParameterType.__init__)
    params = list(sig.parameters.keys())



def test_express_core_scope_is_not_abstract():
    assert not inspect.isabstract(express_core_Scope)


def test_express_core_scope_constructor_exists():
    assert callable(express_core_Scope.__init__)


def test_express_core_scope_constructor_args():
    sig = inspect.signature(express_core_Scope.__init__)
    params = list(sig.parameters.keys())



def test_express_core_role_is_not_abstract():
    assert not inspect.isabstract(express_core_Role)


def test_express_core_role_constructor_exists():
    assert callable(express_core_Role.__init__)


def test_express_core_role_constructor_args():
    sig = inspect.signature(express_core_Role.__init__)
    params = list(sig.parameters.keys())



def test_express_core_remark_is_not_abstract():
    assert not inspect.isabstract(express_core_Remark)


def test_express_core_remark_constructor_exists():
    assert callable(express_core_Remark.__init__)


def test_express_core_remark_constructor_args():
    sig = inspect.signature(express_core_Remark.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "isTagged" in params, "Missing parameter 'isTagged'"
    assert "isTail" in params, "Missing parameter 'isTail'"

def test_express_core_remark_has_text():
    assert hasattr(express_core_Remark, "text")
    descriptor = None
    for klass in express_core_Remark.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_express_core_remark_has_isTagged():
    assert hasattr(express_core_Remark, "isTagged")
    descriptor = None
    for klass in express_core_Remark.__mro__:
        if "isTagged" in klass.__dict__:
            descriptor = klass.__dict__["isTagged"]
            break
    assert isinstance(descriptor, property)

def test_express_core_remark_has_isTail():
    assert hasattr(express_core_Remark, "isTail")
    descriptor = None
    for klass in express_core_Remark.__mro__:
        if "isTail" in klass.__dict__:
            descriptor = klass.__dict__["isTail"]
            break
    assert isinstance(descriptor, property)



def test_arraybound_is_not_abstract():
    assert not inspect.isabstract(ArrayBound)


def test_arraybound_constructor_exists():
    assert callable(ArrayBound.__init__)


def test_arraybound_constructor_args():
    sig = inspect.signature(ArrayBound.__init__)
    params = list(sig.parameters.keys())



def test_concretetype_is_not_abstract():
    assert not inspect.isabstract(ConcreteType)


def test_concretetype_constructor_exists():
    assert callable(ConcreteType.__init__)


def test_concretetype_constructor_args():
    sig = inspect.signature(ConcreteType.__init__)
    params = list(sig.parameters.keys())



def test_localscope_is_not_abstract():
    assert not inspect.isabstract(LocalScope)


def test_localscope_constructor_exists():
    assert callable(LocalScope.__init__)


def test_localscope_constructor_args():
    sig = inspect.signature(LocalScope.__init__)
    params = list(sig.parameters.keys())



def test_express_core_algorithmscope_is_not_abstract():
    assert not inspect.isabstract(express_core_AlgorithmScope)


def test_express_core_algorithmscope_constructor_exists():
    assert callable(express_core_AlgorithmScope.__init__)


def test_express_core_algorithmscope_constructor_args():
    sig = inspect.signature(express_core_AlgorithmScope.__init__)
    params = list(sig.parameters.keys())



def test_anonymoustype_is_not_abstract():
    assert not inspect.isabstract(AnonymousType)


def test_anonymoustype_constructor_exists():
    assert callable(AnonymousType.__init__)


def test_anonymoustype_constructor_args():
    sig = inspect.signature(AnonymousType.__init__)
    params = list(sig.parameters.keys())



def test_express_core_simpletype_is_not_abstract():
    assert not inspect.isabstract(express_core_SimpleType)


def test_express_core_simpletype_constructor_exists():
    assert callable(express_core_SimpleType.__init__)


def test_express_core_simpletype_constructor_args():
    sig = inspect.signature(express_core_SimpleType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_express_core_simpletype_has_id():
    assert hasattr(express_core_SimpleType, "id")
    descriptor = None
    for klass in express_core_SimpleType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_lengthconstraint_is_not_abstract():
    assert not inspect.isabstract(LengthConstraint)


def test_lengthconstraint_constructor_exists():
    assert callable(LengthConstraint.__init__)


def test_lengthconstraint_constructor_args():
    sig = inspect.signature(LengthConstraint.__init__)
    params = list(sig.parameters.keys())



def test_actualtypeconstraint_is_not_abstract():
    assert not inspect.isabstract(ActualTypeConstraint)


def test_actualtypeconstraint_constructor_exists():
    assert callable(ActualTypeConstraint.__init__)


def test_actualtypeconstraint_constructor_args():
    sig = inspect.signature(ActualTypeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_numerictype_is_not_abstract():
    assert not inspect.isabstract(NumericType)


def test_numerictype_constructor_exists():
    assert callable(NumericType.__init__)


def test_numerictype_constructor_args():
    sig = inspect.signature(NumericType.__init__)
    params = list(sig.parameters.keys())



def test_express_core_realtype_is_not_abstract():
    assert not inspect.isabstract(express_core_RealType)


def test_express_core_realtype_constructor_exists():
    assert callable(express_core_RealType.__init__)


def test_express_core_realtype_constructor_args():
    sig = inspect.signature(express_core_RealType.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_express_core_realtype_has_precision():
    assert hasattr(express_core_RealType, "precision")
    descriptor = None
    for klass in express_core_RealType.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_domainconstraint_is_not_abstract():
    assert not inspect.isabstract(DomainConstraint)


def test_domainconstraint_constructor_exists():
    assert callable(DomainConstraint.__init__)


def test_domainconstraint_constructor_args():
    sig = inspect.signature(DomainConstraint.__init__)
    params = list(sig.parameters.keys())



def test_express_core_sizeconstraint_is_not_abstract():
    assert not inspect.isabstract(express_core_SizeConstraint)


def test_express_core_sizeconstraint_constructor_exists():
    assert callable(express_core_SizeConstraint.__init__)


def test_express_core_sizeconstraint_constructor_args():
    sig = inspect.signature(express_core_SizeConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "bound" in params, "Missing parameter 'bound'"

def test_express_core_sizeconstraint_has_bound():
    assert hasattr(express_core_SizeConstraint, "bound")
    descriptor = None
    for klass in express_core_SizeConstraint.__mro__:
        if "bound" in klass.__dict__:
            descriptor = klass.__dict__["bound"]
            break
    assert isinstance(descriptor, property)



def test_express_core_lengthconstraint_is_not_abstract():
    assert not inspect.isabstract(express_core_LengthConstraint)


def test_express_core_lengthconstraint_constructor_exists():
    assert callable(express_core_LengthConstraint.__init__)


def test_express_core_lengthconstraint_constructor_args():
    sig = inspect.signature(express_core_LengthConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "maxLength" in params, "Missing parameter 'maxLength'"
    assert "isFixed" in params, "Missing parameter 'isFixed'"

def test_express_core_lengthconstraint_has_maxLength():
    assert hasattr(express_core_LengthConstraint, "maxLength")
    descriptor = None
    for klass in express_core_LengthConstraint.__mro__:
        if "maxLength" in klass.__dict__:
            descriptor = klass.__dict__["maxLength"]
            break
    assert isinstance(descriptor, property)

def test_express_core_lengthconstraint_has_isFixed():
    assert hasattr(express_core_LengthConstraint, "isFixed")
    descriptor = None
    for klass in express_core_LengthConstraint.__mro__:
        if "isFixed" in klass.__dict__:
            descriptor = klass.__dict__["isFixed"]
            break
    assert isinstance(descriptor, property)



def test_express_core_attributetype_is_not_abstract():
    assert not inspect.isabstract(express_core_AttributeType)


def test_express_core_attributetype_constructor_exists():
    assert callable(express_core_AttributeType.__init__)


def test_express_core_attributetype_constructor_args():
    sig = inspect.signature(express_core_AttributeType.__init__)
    params = list(sig.parameters.keys())



def test_express_core_instance_is_not_abstract():
    assert not inspect.isabstract(express_core_Instance)


def test_express_core_instance_constructor_exists():
    assert callable(express_core_Instance.__init__)


def test_express_core_instance_constructor_args():
    sig = inspect.signature(express_core_Instance.__init__)
    params = list(sig.parameters.keys())



def test_express_core_namedelement_is_not_abstract():
    assert not inspect.isabstract(express_core_NamedElement)


def test_express_core_namedelement_constructor_exists():
    assert callable(express_core_NamedElement.__init__)


def test_express_core_namedelement_constructor_args():
    sig = inspect.signature(express_core_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_core_variabletype_is_not_abstract():
    assert not inspect.isabstract(core_VariableType)


def test_core_variabletype_constructor_exists():
    assert callable(core_VariableType.__init__)


def test_core_variabletype_constructor_args():
    sig = inspect.signature(core_VariableType.__init__)
    params = list(sig.parameters.keys())



def test_express_core_domainconstraint_is_not_abstract():
    assert not inspect.isabstract(express_core_DomainConstraint)


def test_express_core_domainconstraint_constructor_exists():
    assert callable(express_core_DomainConstraint.__init__)


def test_express_core_domainconstraint_constructor_args():
    sig = inspect.signature(express_core_DomainConstraint.__init__)
    params = list(sig.parameters.keys())



def test_typeelement_is_not_abstract():
    assert not inspect.isabstract(TypeElement)


def test_typeelement_constructor_exists():
    assert callable(TypeElement.__init__)


def test_typeelement_constructor_args():
    sig = inspect.signature(TypeElement.__init__)
    params = list(sig.parameters.keys())



def test_express_core_uniquerule_is_not_abstract():
    assert not inspect.isabstract(express_core_UniqueRule)


def test_express_core_uniquerule_constructor_exists():
    assert callable(express_core_UniqueRule.__init__)


def test_express_core_uniquerule_constructor_args():
    sig = inspect.signature(express_core_UniqueRule.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_express_core_uniquerule_has_position():
    assert hasattr(express_core_UniqueRule, "position")
    descriptor = None
    for klass in express_core_UniqueRule.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_core_concretetype_is_not_abstract():
    assert not inspect.isabstract(core_ConcreteType)


def test_core_concretetype_constructor_exists():
    assert callable(core_ConcreteType.__init__)


def test_core_concretetype_constructor_args():
    sig = inspect.signature(core_ConcreteType.__init__)
    params = list(sig.parameters.keys())



def test_simpletype_is_not_abstract():
    assert not inspect.isabstract(SimpleType)


def test_simpletype_constructor_exists():
    assert callable(SimpleType.__init__)


def test_simpletype_constructor_args():
    sig = inspect.signature(SimpleType.__init__)
    params = list(sig.parameters.keys())



def test_express_core_stringtype_is_not_abstract():
    assert not inspect.isabstract(express_core_StringType)


def test_express_core_stringtype_constructor_exists():
    assert callable(express_core_StringType.__init__)


def test_express_core_stringtype_constructor_args():
    sig = inspect.signature(express_core_StringType.__init__)
    params = list(sig.parameters.keys())



def test_express_core_binarytype_is_not_abstract():
    assert not inspect.isabstract(express_core_BinaryType)


def test_express_core_binarytype_constructor_exists():
    assert callable(express_core_BinaryType.__init__)


def test_express_core_binarytype_constructor_args():
    sig = inspect.signature(express_core_BinaryType.__init__)
    params = list(sig.parameters.keys())



def test_express_core_logictype_is_not_abstract():
    assert not inspect.isabstract(express_core_LogicType)


def test_express_core_logictype_constructor_exists():
    assert callable(express_core_LogicType.__init__)


def test_express_core_logictype_constructor_args():
    sig = inspect.signature(express_core_LogicType.__init__)
    params = list(sig.parameters.keys())



def test_express_core_numerictype_is_not_abstract():
    assert not inspect.isabstract(express_core_NumericType)


def test_express_core_numerictype_constructor_exists():
    assert callable(express_core_NumericType.__init__)


def test_express_core_numerictype_constructor_args():
    sig = inspect.signature(express_core_NumericType.__init__)
    params = list(sig.parameters.keys())



def test_express_core_attribute_is_not_abstract():
    assert not inspect.isabstract(express_core_Attribute)


def test_express_core_attribute_constructor_exists():
    assert callable(express_core_Attribute.__init__)


def test_express_core_attribute_constructor_args():
    sig = inspect.signature(express_core_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_express_core_attribute_has_position():
    assert hasattr(express_core_Attribute, "position")
    descriptor = None
    for klass in express_core_Attribute.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_express_core_attribute_has_isAbstract():
    assert hasattr(express_core_Attribute, "isAbstract")
    descriptor = None
    for klass in express_core_Attribute.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_relationship_is_not_abstract():
    assert not inspect.isabstract(Relationship)


def test_relationship_constructor_exists():
    assert callable(Relationship.__init__)


def test_relationship_constructor_args():
    sig = inspect.signature(Relationship.__init__)
    params = list(sig.parameters.keys())



def test_inverseattribute_is_not_abstract():
    assert not inspect.isabstract(InverseAttribute)


def test_inverseattribute_constructor_exists():
    assert callable(InverseAttribute.__init__)


def test_inverseattribute_constructor_args():
    sig = inspect.signature(InverseAttribute.__init__)
    params = list(sig.parameters.keys())



def test_schemaelement_is_not_abstract():
    assert not inspect.isabstract(SchemaElement)


def test_schemaelement_constructor_exists():
    assert callable(SchemaElement.__init__)


def test_schemaelement_constructor_args():
    sig = inspect.signature(SchemaElement.__init__)
    params = list(sig.parameters.keys())



def test_express_core_commonelement_is_not_abstract():
    assert not inspect.isabstract(express_core_CommonElement)


def test_express_core_commonelement_constructor_exists():
    assert callable(express_core_CommonElement.__init__)


def test_express_core_commonelement_constructor_args():
    sig = inspect.signature(express_core_CommonElement.__init__)
    params = list(sig.parameters.keys())



def test_interfacedelement_is_not_abstract():
    assert not inspect.isabstract(InterfacedElement)


def test_interfacedelement_constructor_exists():
    assert callable(InterfacedElement.__init__)


def test_interfacedelement_constructor_args():
    sig = inspect.signature(InterfacedElement.__init__)
    params = list(sig.parameters.keys())



def test_remark_is_not_abstract():
    assert not inspect.isabstract(Remark)


def test_remark_constructor_exists():
    assert callable(Remark.__init__)


def test_remark_constructor_args():
    sig = inspect.signature(Remark.__init__)
    params = list(sig.parameters.keys())



def test_express_core_datatype_is_not_abstract():
    assert not inspect.isabstract(express_core_DataType)


def test_express_core_datatype_constructor_exists():
    assert callable(express_core_DataType.__init__)


def test_express_core_datatype_constructor_args():
    sig = inspect.signature(express_core_DataType.__init__)
    params = list(sig.parameters.keys())



def test_schema_is_not_abstract():
    assert not inspect.isabstract(Schema)


def test_schema_constructor_exists():
    assert callable(Schema.__init__)


def test_schema_constructor_args():
    sig = inspect.signature(Schema.__init__)
    params = list(sig.parameters.keys())



def test_express_core_interfacedelement_is_not_abstract():
    assert not inspect.isabstract(express_core_InterfacedElement)


def test_express_core_interfacedelement_constructor_exists():
    assert callable(express_core_InterfacedElement.__init__)


def test_express_core_interfacedelement_constructor_args():
    sig = inspect.signature(express_core_InterfacedElement.__init__)
    params = list(sig.parameters.keys())
    assert "isUSE" in params, "Missing parameter 'isUSE'"

def test_express_core_interfacedelement_has_isUSE():
    assert hasattr(express_core_InterfacedElement, "isUSE")
    descriptor = None
    for klass in express_core_InterfacedElement.__mro__:
        if "isUSE" in klass.__dict__:
            descriptor = klass.__dict__["isUSE"]
            break
    assert isinstance(descriptor, property)



def test_core_parametertype_is_not_abstract():
    assert not inspect.isabstract(core_ParameterType)


def test_core_parametertype_constructor_exists():
    assert callable(core_ParameterType.__init__)


def test_core_parametertype_constructor_args():
    sig = inspect.signature(core_ParameterType.__init__)
    params = list(sig.parameters.keys())



def test_express_core_instantiabletype_is_not_abstract():
    assert not inspect.isabstract(express_core_InstantiableType)


def test_express_core_instantiabletype_constructor_exists():
    assert callable(express_core_InstantiableType.__init__)


def test_express_core_instantiabletype_constructor_args():
    sig = inspect.signature(express_core_InstantiableType.__init__)
    params = list(sig.parameters.keys())



def test_core_instantiabletype_is_not_abstract():
    assert not inspect.isabstract(core_InstantiableType)


def test_core_instantiabletype_constructor_exists():
    assert callable(core_InstantiableType.__init__)


def test_core_instantiabletype_constructor_args():
    sig = inspect.signature(core_InstantiableType.__init__)
    params = list(sig.parameters.keys())



def test_express_core_anonymoustype_is_not_abstract():
    assert not inspect.isabstract(express_core_AnonymousType)


def test_express_core_anonymoustype_constructor_exists():
    assert callable(express_core_AnonymousType.__init__)


def test_express_core_anonymoustype_constructor_args():
    sig = inspect.signature(express_core_AnonymousType.__init__)
    params = list(sig.parameters.keys())



def test_core_namedtype_is_not_abstract():
    assert not inspect.isabstract(core_NamedType)


def test_core_namedtype_constructor_exists():
    assert callable(core_NamedType.__init__)


def test_core_namedtype_constructor_args():
    sig = inspect.signature(core_NamedType.__init__)
    params = list(sig.parameters.keys())



def test_express_core_definedtype_is_not_abstract():
    assert not inspect.isabstract(express_core_DefinedType)


def test_express_core_definedtype_constructor_exists():
    assert callable(express_core_DefinedType.__init__)


def test_express_core_definedtype_constructor_args():
    sig = inspect.signature(express_core_DefinedType.__init__)
    params = list(sig.parameters.keys())



def test_express_core_entitytype_is_not_abstract():
    assert not inspect.isabstract(express_core_EntityType)


def test_express_core_entitytype_constructor_exists():
    assert callable(express_core_EntityType.__init__)


def test_express_core_entitytype_constructor_args():
    sig = inspect.signature(express_core_EntityType.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_express_core_entitytype_has_isAbstract():
    assert hasattr(express_core_EntityType, "isAbstract")
    descriptor = None
    for klass in express_core_EntityType.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_role_is_not_abstract():
    assert not inspect.isabstract(Role)


def test_role_constructor_exists():
    assert callable(Role.__init__)


def test_role_constructor_args():
    sig = inspect.signature(Role.__init__)
    params = list(sig.parameters.keys())



def test_express_core_rangerole_is_not_abstract():
    assert not inspect.isabstract(express_core_RangeRole)


def test_express_core_rangerole_constructor_exists():
    assert callable(express_core_RangeRole.__init__)


def test_express_core_rangerole_constructor_args():
    sig = inspect.signature(express_core_RangeRole.__init__)
    params = list(sig.parameters.keys())



def test_express_core_domainrole_is_not_abstract():
    assert not inspect.isabstract(express_core_DomainRole)


def test_express_core_domainrole_constructor_exists():
    assert callable(express_core_DomainRole.__init__)


def test_express_core_domainrole_constructor_args():
    sig = inspect.signature(express_core_DomainRole.__init__)
    params = list(sig.parameters.keys())



def test_redeclaration_is_not_abstract():
    assert not inspect.isabstract(Redeclaration)


def test_redeclaration_constructor_exists():
    assert callable(Redeclaration.__init__)


def test_redeclaration_constructor_args():
    sig = inspect.signature(Redeclaration.__init__)
    params = list(sig.parameters.keys())



def test_attributetype_is_not_abstract():
    assert not inspect.isabstract(AttributeType)


def test_attributetype_constructor_exists():
    assert callable(AttributeType.__init__)


def test_attributetype_constructor_args():
    sig = inspect.signature(AttributeType.__init__)
    params = list(sig.parameters.keys())



def test_express_core_redeclaration_is_not_abstract():
    assert not inspect.isabstract(express_core_Redeclaration)


def test_express_core_redeclaration_constructor_exists():
    assert callable(express_core_Redeclaration.__init__)


def test_express_core_redeclaration_constructor_args():
    sig = inspect.signature(express_core_Redeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"
    assert "position" in params, "Missing parameter 'position'"

def test_express_core_redeclaration_has_isMandatory():
    assert hasattr(express_core_Redeclaration, "isMandatory")
    descriptor = None
    for klass in express_core_Redeclaration.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)

def test_express_core_redeclaration_has_position():
    assert hasattr(express_core_Redeclaration, "position")
    descriptor = None
    for klass in express_core_Redeclaration.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_indexoperation_is_not_abstract():
    assert not inspect.isabstract(IndexOperation)


def test_indexoperation_constructor_exists():
    assert callable(IndexOperation.__init__)


def test_indexoperation_constructor_args():
    sig = inspect.signature(IndexOperation.__init__)
    params = list(sig.parameters.keys())



def test_express_expressions_binaryindex_is_not_abstract():
    assert not inspect.isabstract(express_expressions_BinaryIndex)


def test_express_expressions_binaryindex_constructor_exists():
    assert callable(express_expressions_BinaryIndex.__init__)


def test_express_expressions_binaryindex_constructor_args():
    sig = inspect.signature(express_expressions_BinaryIndex.__init__)
    params = list(sig.parameters.keys())



def test_simplevalue_is_not_abstract():
    assert not inspect.isabstract(SimpleValue)


def test_simplevalue_constructor_exists():
    assert callable(SimpleValue.__init__)


def test_simplevalue_constructor_args():
    sig = inspect.signature(SimpleValue.__init__)
    params = list(sig.parameters.keys())



def test_express_instances_numbervalue_is_not_abstract():
    assert not inspect.isabstract(express_instances_NumberValue)


def test_express_instances_numbervalue_constructor_exists():
    assert callable(express_instances_NumberValue.__init__)


def test_express_instances_numbervalue_constructor_args():
    sig = inspect.signature(express_instances_NumberValue.__init__)
    params = list(sig.parameters.keys())



def test_express_instances_binaryvalue_is_not_abstract():
    assert not inspect.isabstract(express_instances_BinaryValue)


def test_express_instances_binaryvalue_constructor_exists():
    assert callable(express_instances_BinaryValue.__init__)


def test_express_instances_binaryvalue_constructor_args():
    sig = inspect.signature(express_instances_BinaryValue.__init__)
    params = list(sig.parameters.keys())



def test_express_instances_logicalvalue_is_not_abstract():
    assert not inspect.isabstract(express_instances_LogicalValue)


def test_express_instances_logicalvalue_constructor_exists():
    assert callable(express_instances_LogicalValue.__init__)


def test_express_instances_logicalvalue_constructor_args():
    sig = inspect.signature(express_instances_LogicalValue.__init__)
    params = list(sig.parameters.keys())



def test_express_instances_stringvalue_is_not_abstract():
    assert not inspect.isabstract(express_instances_StringValue)


def test_express_instances_stringvalue_constructor_exists():
    assert callable(express_instances_StringValue.__init__)


def test_express_instances_stringvalue_constructor_args():
    sig = inspect.signature(express_instances_StringValue.__init__)
    params = list(sig.parameters.keys())



def test_enumerationitem_is_not_abstract():
    assert not inspect.isabstract(EnumerationItem)


def test_enumerationitem_constructor_exists():
    assert callable(EnumerationItem.__init__)


def test_enumerationitem_constructor_args():
    sig = inspect.signature(EnumerationItem.__init__)
    params = list(sig.parameters.keys())



def test_primary_is_not_abstract():
    assert not inspect.isabstract(Primary)


def test_primary_constructor_exists():
    assert callable(Primary.__init__)


def test_primary_constructor_args():
    sig = inspect.signature(Primary.__init__)
    params = list(sig.parameters.keys())



def test_express_expressions_literal_is_not_abstract():
    assert not inspect.isabstract(express_expressions_Literal)


def test_express_expressions_literal_constructor_exists():
    assert callable(express_expressions_Literal.__init__)


def test_express_expressions_literal_constructor_args():
    sig = inspect.signature(express_expressions_Literal.__init__)
    params = list(sig.parameters.keys())



def test_express_expressions_enumitemref_is_not_abstract():
    assert not inspect.isabstract(express_expressions_EnumItemRef)


def test_express_expressions_enumitemref_constructor_exists():
    assert callable(express_expressions_EnumItemRef.__init__)


def test_express_expressions_enumitemref_constructor_args():
    sig = inspect.signature(express_expressions_EnumItemRef.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_express_expressions_enumitemref_has_id():
    assert hasattr(express_expressions_EnumItemRef, "id")
    descriptor = None
    for klass in express_expressions_EnumItemRef.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_express_expressions_repeatcount_is_not_abstract():
    assert not inspect.isabstract(express_expressions_RepeatCount)


def test_express_expressions_repeatcount_constructor_exists():
    assert callable(express_expressions_RepeatCount.__init__)


def test_express_expressions_repeatcount_constructor_args():
    sig = inspect.signature(express_expressions_RepeatCount.__init__)
    params = list(sig.parameters.keys())



def test_express_expressions_selfref_is_not_abstract():
    assert not inspect.isabstract(express_expressions_SELFRef)


def test_express_expressions_selfref_constructor_exists():
    assert callable(express_expressions_SELFRef.__init__)


def test_express_expressions_selfref_constructor_args():
    sig = inspect.signature(express_expressions_SELFRef.__init__)
    params = list(sig.parameters.keys())



def test_indeterminate_is_not_abstract():
    assert not inspect.isabstract(Indeterminate)


def test_indeterminate_constructor_exists():
    assert callable(Indeterminate.__init__)


def test_indeterminate_constructor_args():
    sig = inspect.signature(Indeterminate.__init__)
    params = list(sig.parameters.keys())



def test_caseaction_is_not_abstract():
    assert not inspect.isabstract(CaseAction)


def test_caseaction_constructor_exists():
    assert callable(CaseAction.__init__)


def test_caseaction_constructor_args():
    sig = inspect.signature(CaseAction.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_express_algorithms_functionresult_is_not_abstract():
    assert not inspect.isabstract(express_algorithms_FunctionResult)


def test_express_algorithms_functionresult_constructor_exists():
    assert callable(express_algorithms_FunctionResult.__init__)


def test_express_algorithms_functionresult_constructor_args():
    sig = inspect.signature(express_algorithms_FunctionResult.__init__)
    params = list(sig.parameters.keys())



def test_express_algorithms_invariable_is_not_abstract():
    assert not inspect.isabstract(express_algorithms_InVariable)


def test_express_algorithms_invariable_constructor_exists():
    assert callable(express_algorithms_InVariable.__init__)


def test_express_algorithms_invariable_constructor_args():
    sig = inspect.signature(express_algorithms_InVariable.__init__)
    params = list(sig.parameters.keys())



def test_express_algorithms_localvariable_is_not_abstract():
    assert not inspect.isabstract(express_algorithms_LocalVariable)


def test_express_algorithms_localvariable_constructor_exists():
    assert callable(express_algorithms_LocalVariable.__init__)


def test_express_algorithms_localvariable_constructor_args():
    sig = inspect.signature(express_algorithms_LocalVariable.__init__)
    params = list(sig.parameters.keys())



def test_singleentitytype_is_not_abstract():
    assert not inspect.isabstract(SingleEntityType)


def test_singleentitytype_constructor_exists():
    assert callable(SingleEntityType.__init__)


def test_singleentitytype_constructor_args():
    sig = inspect.signature(SingleEntityType.__init__)
    params = list(sig.parameters.keys())



def test_controlvariable_is_not_abstract():
    assert not inspect.isabstract(ControlVariable)


def test_controlvariable_constructor_exists():
    assert callable(ControlVariable.__init__)


def test_controlvariable_constructor_args():
    sig = inspect.signature(ControlVariable.__init__)
    params = list(sig.parameters.keys())



def test_explicitattribute_is_not_abstract():
    assert not inspect.isabstract(ExplicitAttribute)


def test_explicitattribute_constructor_exists():
    assert callable(ExplicitAttribute.__init__)


def test_explicitattribute_constructor_args():
    sig = inspect.signature(ExplicitAttribute.__init__)
    params = list(sig.parameters.keys())



def test_express_core_invertibleattribute_is_not_abstract():
    assert not inspect.isabstract(express_core_InvertibleAttribute)


def test_express_core_invertibleattribute_constructor_exists():
    assert callable(express_core_InvertibleAttribute.__init__)


def test_express_core_invertibleattribute_constructor_args():
    sig = inspect.signature(express_core_InvertibleAttribute.__init__)
    params = list(sig.parameters.keys())



def test_express_statements_varexpression_is_not_abstract():
    assert not inspect.isabstract(express_statements_VARExpression)


def test_express_statements_varexpression_constructor_exists():
    assert callable(express_statements_VARExpression.__init__)


def test_express_statements_varexpression_constructor_args():
    sig = inspect.signature(express_statements_VARExpression.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_express_statements_varexpression_has_text():
    assert hasattr(express_statements_VARExpression, "text")
    descriptor = None
    for klass in express_statements_VARExpression.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_varvariable_is_not_abstract():
    assert not inspect.isabstract(VARVariable)


def test_varvariable_constructor_exists():
    assert callable(VARVariable.__init__)


def test_varvariable_constructor_args():
    sig = inspect.signature(VARVariable.__init__)
    params = list(sig.parameters.keys())



def test_algorithms_varvariable_is_not_abstract():
    assert not inspect.isabstract(algorithms_VARVariable)


def test_algorithms_varvariable_constructor_exists():
    assert callable(algorithms_VARVariable.__init__)


def test_algorithms_varvariable_constructor_args():
    sig = inspect.signature(algorithms_VARVariable.__init__)
    params = list(sig.parameters.keys())



def test_express_algorithms_varparameter_is_not_abstract():
    assert not inspect.isabstract(express_algorithms_VARParameter)


def test_express_algorithms_varparameter_constructor_exists():
    assert callable(express_algorithms_VARParameter.__init__)


def test_express_algorithms_varparameter_constructor_args():
    sig = inspect.signature(express_algorithms_VARParameter.__init__)
    params = list(sig.parameters.keys())



def test_algorithms_namedvariable_is_not_abstract():
    assert not inspect.isabstract(algorithms_NamedVariable)


def test_algorithms_namedvariable_constructor_exists():
    assert callable(algorithms_NamedVariable.__init__)


def test_algorithms_namedvariable_constructor_args():
    sig = inspect.signature(algorithms_NamedVariable.__init__)
    params = list(sig.parameters.keys())



def test_express_statements_aliasvariable_is_not_abstract():
    assert not inspect.isabstract(express_statements_AliasVariable)


def test_express_statements_aliasvariable_constructor_exists():
    assert callable(express_statements_AliasVariable.__init__)


def test_express_statements_aliasvariable_constructor_args():
    sig = inspect.signature(express_statements_AliasVariable.__init__)
    params = list(sig.parameters.keys())



def test_namedvariable_is_not_abstract():
    assert not inspect.isabstract(NamedVariable)


def test_namedvariable_constructor_exists():
    assert callable(NamedVariable.__init__)


def test_namedvariable_constructor_args():
    sig = inspect.signature(NamedVariable.__init__)
    params = list(sig.parameters.keys())



def test_express_algorithms_variable_is_not_abstract():
    assert not inspect.isabstract(express_algorithms_Variable)


def test_express_algorithms_variable_constructor_exists():
    assert callable(express_algorithms_Variable.__init__)


def test_express_algorithms_variable_constructor_args():
    sig = inspect.signature(express_algorithms_Variable.__init__)
    params = list(sig.parameters.keys())



def test_express_statements_controlvariable_is_not_abstract():
    assert not inspect.isabstract(express_statements_ControlVariable)


def test_express_statements_controlvariable_constructor_exists():
    assert callable(express_statements_ControlVariable.__init__)


def test_express_statements_controlvariable_constructor_args():
    sig = inspect.signature(express_statements_ControlVariable.__init__)
    params = list(sig.parameters.keys())



def test_aliasvariable_is_not_abstract():
    assert not inspect.isabstract(AliasVariable)


def test_aliasvariable_constructor_exists():
    assert callable(AliasVariable.__init__)


def test_aliasvariable_constructor_args():
    sig = inspect.signature(AliasVariable.__init__)
    params = list(sig.parameters.keys())



def test_varexpression_is_not_abstract():
    assert not inspect.isabstract(VARExpression)


def test_varexpression_constructor_exists():
    assert callable(VARExpression.__init__)


def test_varexpression_constructor_args():
    sig = inspect.signature(VARExpression.__init__)
    params = list(sig.parameters.keys())



def test_express_statements_attributecell_is_not_abstract():
    assert not inspect.isabstract(express_statements_AttributeCell)


def test_express_statements_attributecell_constructor_exists():
    assert callable(express_statements_AttributeCell.__init__)


def test_express_statements_attributecell_constructor_args():
    sig = inspect.signature(express_statements_AttributeCell.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_express_statements_attributecell_has_id():
    assert hasattr(express_statements_AttributeCell, "id")
    descriptor = None
    for klass in express_statements_AttributeCell.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_express_statements_groupcell_is_not_abstract():
    assert not inspect.isabstract(express_statements_GroupCell)


def test_express_statements_groupcell_constructor_exists():
    assert callable(express_statements_GroupCell.__init__)


def test_express_statements_groupcell_constructor_args():
    sig = inspect.signature(express_statements_GroupCell.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_express_statements_groupcell_has_id():
    assert hasattr(express_statements_GroupCell, "id")
    descriptor = None
    for klass in express_statements_GroupCell.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_express_statements_membercell_is_not_abstract():
    assert not inspect.isabstract(express_statements_MemberCell)


def test_express_statements_membercell_constructor_exists():
    assert callable(express_statements_MemberCell.__init__)


def test_express_statements_membercell_constructor_args():
    sig = inspect.signature(express_statements_MemberCell.__init__)
    params = list(sig.parameters.keys())



def test_express_statements_varcell_is_not_abstract():
    assert not inspect.isabstract(express_statements_VARCell)


def test_express_statements_varcell_constructor_exists():
    assert callable(express_statements_VARCell.__init__)


def test_express_statements_varcell_constructor_args():
    sig = inspect.signature(express_statements_VARCell.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_express_statements_varcell_has_id():
    assert hasattr(express_statements_VARCell, "id")
    descriptor = None
    for klass in express_statements_VARCell.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_express_statements_variablecell_is_not_abstract():
    assert not inspect.isabstract(express_statements_VariableCell)


def test_express_statements_variablecell_constructor_exists():
    assert callable(express_statements_VariableCell.__init__)


def test_express_statements_variablecell_constructor_args():
    sig = inspect.signature(express_statements_VariableCell.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_express_statements_variablecell_has_id():
    assert hasattr(express_statements_VariableCell, "id")
    descriptor = None
    for klass in express_statements_VariableCell.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_core_localscope_is_not_abstract():
    assert not inspect.isabstract(core_LocalScope)


def test_core_localscope_constructor_exists():
    assert callable(core_LocalScope.__init__)


def test_core_localscope_constructor_args():
    sig = inspect.signature(core_LocalScope.__init__)
    params = list(sig.parameters.keys())



def test_algorithms_statement_is_not_abstract():
    assert not inspect.isabstract(algorithms_Statement)


def test_algorithms_statement_constructor_exists():
    assert callable(algorithms_Statement.__init__)


def test_algorithms_statement_constructor_args():
    sig = inspect.signature(algorithms_Statement.__init__)
    params = list(sig.parameters.keys())



def test_express_statements_repeatstatement_is_not_abstract():
    assert not inspect.isabstract(express_statements_RepeatStatement)


def test_express_statements_repeatstatement_constructor_exists():
    assert callable(express_statements_RepeatStatement.__init__)


def test_express_statements_repeatstatement_constructor_args():
    sig = inspect.signature(express_statements_RepeatStatement.__init__)
    params = list(sig.parameters.keys())



def test_express_statements_aliasstatement_is_not_abstract():
    assert not inspect.isabstract(express_statements_AliasStatement)


def test_express_statements_aliasstatement_constructor_exists():
    assert callable(express_statements_AliasStatement.__init__)


def test_express_statements_aliasstatement_constructor_args():
    sig = inspect.signature(express_statements_AliasStatement.__init__)
    params = list(sig.parameters.keys())



def test_controlstatement_is_not_abstract():
    assert not inspect.isabstract(ControlStatement)


def test_controlstatement_constructor_exists():
    assert callable(ControlStatement.__init__)


def test_controlstatement_constructor_args():
    sig = inspect.signature(ControlStatement.__init__)
    params = list(sig.parameters.keys())



def test_express_statements_returnstatement_is_not_abstract():
    assert not inspect.isabstract(express_statements_ReturnStatement)


def test_express_statements_returnstatement_constructor_exists():
    assert callable(express_statements_ReturnStatement.__init__)


def test_express_statements_returnstatement_constructor_args():
    sig = inspect.signature(express_statements_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_express_statements_escapestatement_is_not_abstract():
    assert not inspect.isabstract(express_statements_EscapeStatement)


def test_express_statements_escapestatement_constructor_exists():
    assert callable(express_statements_EscapeStatement.__init__)


def test_express_statements_escapestatement_constructor_args():
    sig = inspect.signature(express_statements_EscapeStatement.__init__)
    params = list(sig.parameters.keys())



def test_express_statements_nullstatement_is_not_abstract():
    assert not inspect.isabstract(express_statements_NullStatement)


def test_express_statements_nullstatement_constructor_exists():
    assert callable(express_statements_NullStatement.__init__)


def test_express_statements_nullstatement_constructor_args():
    sig = inspect.signature(express_statements_NullStatement.__init__)
    params = list(sig.parameters.keys())



def test_express_statements_skipstatement_is_not_abstract():
    assert not inspect.isabstract(express_statements_SkipStatement)


def test_express_statements_skipstatement_constructor_exists():
    assert callable(express_statements_SkipStatement.__init__)


def test_express_statements_skipstatement_constructor_args():
    sig = inspect.signature(express_statements_SkipStatement.__init__)
    params = list(sig.parameters.keys())



def test_express_statements_caseaction_is_not_abstract():
    assert not inspect.isabstract(express_statements_CaseAction)


def test_express_statements_caseaction_constructor_exists():
    assert callable(express_statements_CaseAction.__init__)


def test_express_statements_caseaction_constructor_args():
    sig = inspect.signature(express_statements_CaseAction.__init__)
    params = list(sig.parameters.keys())
    assert "isDefault" in params, "Missing parameter 'isDefault'"

def test_express_statements_caseaction_has_isDefault():
    assert hasattr(express_statements_CaseAction, "isDefault")
    descriptor = None
    for klass in express_statements_CaseAction.__mro__:
        if "isDefault" in klass.__dict__:
            descriptor = klass.__dict__["isDefault"]
            break
    assert isinstance(descriptor, property)



def test_localelement_is_not_abstract():
    assert not inspect.isabstract(LocalElement)


def test_localelement_constructor_exists():
    assert callable(LocalElement.__init__)


def test_localelement_constructor_args():
    sig = inspect.signature(LocalElement.__init__)
    params = list(sig.parameters.keys())



def test_express_algorithms_genericelement_is_not_abstract():
    assert not inspect.isabstract(express_algorithms_GenericElement)


def test_express_algorithms_genericelement_constructor_exists():
    assert callable(express_algorithms_GenericElement.__init__)


def test_express_algorithms_genericelement_constructor_args():
    sig = inspect.signature(express_algorithms_GenericElement.__init__)
    params = list(sig.parameters.keys())



def test_express_algorithms_namedvariable_is_not_abstract():
    assert not inspect.isabstract(express_algorithms_NamedVariable)


def test_express_algorithms_namedvariable_constructor_exists():
    assert callable(express_algorithms_NamedVariable.__init__)


def test_express_algorithms_namedvariable_constructor_args():
    sig = inspect.signature(express_algorithms_NamedVariable.__init__)
    params = list(sig.parameters.keys())



def test_express_algorithms_parameter_is_not_abstract():
    assert not inspect.isabstract(express_algorithms_Parameter)


def test_express_algorithms_parameter_constructor_exists():
    assert callable(express_algorithms_Parameter.__init__)


def test_express_algorithms_parameter_constructor_args():
    sig = inspect.signature(express_algorithms_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "inout" in params, "Missing parameter 'inout'"
    assert "position" in params, "Missing parameter 'position'"

def test_express_algorithms_parameter_has_inout():
    assert hasattr(express_algorithms_Parameter, "inout")
    descriptor = None
    for klass in express_algorithms_Parameter.__mro__:
        if "inout" in klass.__dict__:
            descriptor = klass.__dict__["inout"]
            break
    assert isinstance(descriptor, property)

def test_express_algorithms_parameter_has_position():
    assert hasattr(express_algorithms_Parameter, "position")
    descriptor = None
    for klass in express_algorithms_Parameter.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_express_rules_namedrule_is_not_abstract():
    assert not inspect.isabstract(express_rules_NamedRule)


def test_express_rules_namedrule_constructor_exists():
    assert callable(express_rules_NamedRule.__init__)


def test_express_rules_namedrule_constructor_args():
    sig = inspect.signature(express_rules_NamedRule.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_express_rules_namedrule_has_position():
    assert hasattr(express_rules_NamedRule, "position")
    descriptor = None
    for klass in express_rules_NamedRule.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_namedrule_is_not_abstract():
    assert not inspect.isabstract(NamedRule)


def test_namedrule_constructor_exists():
    assert callable(NamedRule.__init__)


def test_namedrule_constructor_args():
    sig = inspect.signature(NamedRule.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_express_statements_ifstatement_is_not_abstract():
    assert not inspect.isabstract(express_statements_IfStatement)


def test_express_statements_ifstatement_constructor_exists():
    assert callable(express_statements_IfStatement.__init__)


def test_express_statements_ifstatement_constructor_args():
    sig = inspect.signature(express_statements_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_express_statements_assignment_is_not_abstract():
    assert not inspect.isabstract(express_statements_Assignment)


def test_express_statements_assignment_constructor_exists():
    assert callable(express_statements_Assignment.__init__)


def test_express_statements_assignment_constructor_args():
    sig = inspect.signature(express_statements_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_express_statements_statementblock_is_not_abstract():
    assert not inspect.isabstract(express_statements_StatementBlock)


def test_express_statements_statementblock_constructor_exists():
    assert callable(express_statements_StatementBlock.__init__)


def test_express_statements_statementblock_constructor_args():
    sig = inspect.signature(express_statements_StatementBlock.__init__)
    params = list(sig.parameters.keys())
    assert "delimited" in params, "Missing parameter 'delimited'"

def test_express_statements_statementblock_has_delimited():
    assert hasattr(express_statements_StatementBlock, "delimited")
    descriptor = None
    for klass in express_statements_StatementBlock.__mro__:
        if "delimited" in klass.__dict__:
            descriptor = klass.__dict__["delimited"]
            break
    assert isinstance(descriptor, property)



def test_express_statements_casestatement_is_not_abstract():
    assert not inspect.isabstract(express_statements_CaseStatement)


def test_express_statements_casestatement_constructor_exists():
    assert callable(express_statements_CaseStatement.__init__)


def test_express_statements_casestatement_constructor_args():
    sig = inspect.signature(express_statements_CaseStatement.__init__)
    params = list(sig.parameters.keys())



def test_express_statements_controlstatement_is_not_abstract():
    assert not inspect.isabstract(express_statements_ControlStatement)


def test_express_statements_controlstatement_constructor_exists():
    assert callable(express_statements_ControlStatement.__init__)


def test_express_statements_controlstatement_constructor_args():
    sig = inspect.signature(express_statements_ControlStatement.__init__)
    params = list(sig.parameters.keys())



def test_core_algorithmscope_is_not_abstract():
    assert not inspect.isabstract(core_AlgorithmScope)


def test_core_algorithmscope_constructor_exists():
    assert callable(core_AlgorithmScope.__init__)


def test_core_algorithmscope_constructor_args():
    sig = inspect.signature(core_AlgorithmScope.__init__)
    params = list(sig.parameters.keys())



def test_express_algorithms_algorithm_is_not_abstract():
    assert not inspect.isabstract(express_algorithms_Algorithm)


def test_express_algorithms_algorithm_constructor_exists():
    assert callable(express_algorithms_Algorithm.__init__)


def test_express_algorithms_algorithm_constructor_args():
    sig = inspect.signature(express_algorithms_Algorithm.__init__)
    params = list(sig.parameters.keys())



def test_core_schemaelement_is_not_abstract():
    assert not inspect.isabstract(core_SchemaElement)


def test_core_schemaelement_constructor_exists():
    assert callable(core_SchemaElement.__init__)


def test_core_schemaelement_constructor_args():
    sig = inspect.signature(core_SchemaElement.__init__)
    params = list(sig.parameters.keys())



def test_express_rules_globalrule_is_not_abstract():
    assert not inspect.isabstract(express_rules_GlobalRule)


def test_express_rules_globalrule_constructor_exists():
    assert callable(express_rules_GlobalRule.__init__)


def test_express_rules_globalrule_constructor_args():
    sig = inspect.signature(express_rules_GlobalRule.__init__)
    params = list(sig.parameters.keys())



def test_scopedid_is_not_abstract():
    assert not inspect.isabstract(ScopedId)


def test_scopedid_constructor_exists():
    assert callable(ScopedId.__init__)


def test_scopedid_constructor_args():
    sig = inspect.signature(ScopedId.__init__)
    params = list(sig.parameters.keys())



def test_globalrule_is_not_abstract():
    assert not inspect.isabstract(GlobalRule)


def test_globalrule_constructor_exists():
    assert callable(GlobalRule.__init__)


def test_globalrule_constructor_args():
    sig = inspect.signature(GlobalRule.__init__)
    params = list(sig.parameters.keys())



def test_population_is_not_abstract():
    assert not inspect.isabstract(Population)


def test_population_constructor_exists():
    assert callable(Population.__init__)


def test_population_constructor_args():
    sig = inspect.signature(Population.__init__)
    params = list(sig.parameters.keys())



def test_entityinstance_is_not_abstract():
    assert not inspect.isabstract(EntityInstance)


def test_entityinstance_constructor_exists():
    assert callable(EntityInstance.__init__)


def test_entityinstance_constructor_args():
    sig = inspect.signature(EntityInstance.__init__)
    params = list(sig.parameters.keys())



def test_express_instances_singleleafinstance_is_not_abstract():
    assert not inspect.isabstract(express_instances_SingleLeafInstance)


def test_express_instances_singleleafinstance_constructor_exists():
    assert callable(express_instances_SingleLeafInstance.__init__)


def test_express_instances_singleleafinstance_constructor_args():
    sig = inspect.signature(express_instances_SingleLeafInstance.__init__)
    params = list(sig.parameters.keys())



def test_express_instances_multileafinstance_is_not_abstract():
    assert not inspect.isabstract(express_instances_MultiLeafInstance)


def test_express_instances_multileafinstance_constructor_exists():
    assert callable(express_instances_MultiLeafInstance.__init__)


def test_express_instances_multileafinstance_constructor_args():
    sig = inspect.signature(express_instances_MultiLeafInstance.__init__)
    params = list(sig.parameters.keys())



def test_setvalue_is_not_abstract():
    assert not inspect.isabstract(SETValue)


def test_setvalue_constructor_exists():
    assert callable(SETValue.__init__)


def test_setvalue_constructor_args():
    sig = inspect.signature(SETValue.__init__)
    params = list(sig.parameters.keys())



def test_express_rules_extent_is_not_abstract():
    assert not inspect.isabstract(express_rules_Extent)


def test_express_rules_extent_constructor_exists():
    assert callable(express_rules_Extent.__init__)


def test_express_rules_extent_constructor_args():
    sig = inspect.signature(express_rules_Extent.__init__)
    params = list(sig.parameters.keys())



def test_supertyperule_is_not_abstract():
    assert not inspect.isabstract(SupertypeRule)


def test_supertyperule_constructor_exists():
    assert callable(SupertypeRule.__init__)


def test_supertyperule_constructor_args():
    sig = inspect.signature(SupertypeRule.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_express_expressions_indexoperation_is_not_abstract():
    assert not inspect.isabstract(express_expressions_IndexOperation)


def test_express_expressions_indexoperation_constructor_exists():
    assert callable(express_expressions_IndexOperation.__init__)


def test_express_expressions_indexoperation_constructor_args():
    sig = inspect.signature(express_expressions_IndexOperation.__init__)
    params = list(sig.parameters.keys())



def test_express_expressions_selector_is_not_abstract():
    assert not inspect.isabstract(express_expressions_Selector)


def test_express_expressions_selector_constructor_exists():
    assert callable(express_expressions_Selector.__init__)


def test_express_expressions_selector_constructor_args():
    sig = inspect.signature(express_expressions_Selector.__init__)
    params = list(sig.parameters.keys())



def test_extent_is_not_abstract():
    assert not inspect.isabstract(Extent)


def test_extent_constructor_exists():
    assert callable(Extent.__init__)


def test_extent_constructor_args():
    sig = inspect.signature(Extent.__init__)
    params = list(sig.parameters.keys())



def test_express_rules_subtypeconstraint_is_not_abstract():
    assert not inspect.isabstract(express_rules_SubtypeConstraint)


def test_express_rules_subtypeconstraint_constructor_exists():
    assert callable(express_rules_SubtypeConstraint.__init__)


def test_express_rules_subtypeconstraint_constructor_args():
    sig = inspect.signature(express_rules_SubtypeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_actualparameter_is_not_abstract():
    assert not inspect.isabstract(ActualParameter)


def test_actualparameter_constructor_exists():
    assert callable(ActualParameter.__init__)


def test_actualparameter_constructor_args():
    sig = inspect.signature(ActualParameter.__init__)
    params = list(sig.parameters.keys())



def test_procedure_is_not_abstract():
    assert not inspect.isabstract(Procedure)


def test_procedure_constructor_exists():
    assert callable(Procedure.__init__)


def test_procedure_constructor_args():
    sig = inspect.signature(Procedure.__init__)
    params = list(sig.parameters.keys())



def test_express_statements_procedurecall_is_not_abstract():
    assert not inspect.isabstract(express_statements_ProcedureCall)


def test_express_statements_procedurecall_constructor_exists():
    assert callable(express_statements_ProcedureCall.__init__)


def test_express_statements_procedurecall_constructor_args():
    sig = inspect.signature(express_statements_ProcedureCall.__init__)
    params = list(sig.parameters.keys())



def test_entitytype_is_not_abstract():
    assert not inspect.isabstract(EntityType)


def test_entitytype_constructor_exists():
    assert callable(EntityType.__init__)


def test_entitytype_constructor_args():
    sig = inspect.signature(EntityType.__init__)
    params = list(sig.parameters.keys())



def test_commonelement_is_not_abstract():
    assert not inspect.isabstract(CommonElement)


def test_commonelement_constructor_exists():
    assert callable(CommonElement.__init__)


def test_commonelement_constructor_args():
    sig = inspect.signature(CommonElement.__init__)
    params = list(sig.parameters.keys())



def test_express_instances_constant_is_not_abstract():
    assert not inspect.isabstract(express_instances_Constant)


def test_express_instances_constant_constructor_exists():
    assert callable(express_instances_Constant.__init__)


def test_express_instances_constant_constructor_args():
    sig = inspect.signature(express_instances_Constant.__init__)
    params = list(sig.parameters.keys())



def test_express_rules_supertyperule_is_not_abstract():
    assert not inspect.isabstract(express_rules_SupertypeRule)


def test_express_rules_supertyperule_constructor_exists():
    assert callable(express_rules_SupertypeRule.__init__)


def test_express_rules_supertyperule_constructor_args():
    sig = inspect.signature(express_rules_SupertypeRule.__init__)
    params = list(sig.parameters.keys())
    assert "assertsAbstract" in params, "Missing parameter 'assertsAbstract'"

def test_express_rules_supertyperule_has_assertsAbstract():
    assert hasattr(express_rules_SupertypeRule, "assertsAbstract")
    descriptor = None
    for klass in express_rules_SupertypeRule.__mro__:
        if "assertsAbstract" in klass.__dict__:
            descriptor = klass.__dict__["assertsAbstract"]
            break
    assert isinstance(descriptor, property)



def test_subtypeconstraint_is_not_abstract():
    assert not inspect.isabstract(SubtypeConstraint)


def test_subtypeconstraint_constructor_exists():
    assert callable(SubtypeConstraint.__init__)


def test_subtypeconstraint_constructor_args():
    sig = inspect.signature(SubtypeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_express_rules_andconstraint_is_not_abstract():
    assert not inspect.isabstract(express_rules_ANDConstraint)


def test_express_rules_andconstraint_constructor_exists():
    assert callable(express_rules_ANDConstraint.__init__)


def test_express_rules_andconstraint_constructor_args():
    sig = inspect.signature(express_rules_ANDConstraint.__init__)
    params = list(sig.parameters.keys())



def test_express_rules_total_overconstraint_is_not_abstract():
    assert not inspect.isabstract(express_rules_TOTAL_OVERConstraint)


def test_express_rules_total_overconstraint_constructor_exists():
    assert callable(express_rules_TOTAL_OVERConstraint.__init__)


def test_express_rules_total_overconstraint_constructor_args():
    sig = inspect.signature(express_rules_TOTAL_OVERConstraint.__init__)
    params = list(sig.parameters.keys())



def test_express_rules_oneofconstraint_is_not_abstract():
    assert not inspect.isabstract(express_rules_ONEOFConstraint)


def test_express_rules_oneofconstraint_constructor_exists():
    assert callable(express_rules_ONEOFConstraint.__init__)


def test_express_rules_oneofconstraint_constructor_args():
    sig = inspect.signature(express_rules_ONEOFConstraint.__init__)
    params = list(sig.parameters.keys())



def test_concreteaggregationtype_is_not_abstract():
    assert not inspect.isabstract(ConcreteAggregationType)


def test_concreteaggregationtype_constructor_exists():
    assert callable(ConcreteAggregationType.__init__)


def test_concreteaggregationtype_constructor_args():
    sig = inspect.signature(ConcreteAggregationType.__init__)
    params = list(sig.parameters.keys())



def test_express_core_arraytype_is_not_abstract():
    assert not inspect.isabstract(express_core_ARRAYType)


def test_express_core_arraytype_constructor_exists():
    assert callable(express_core_ARRAYType.__init__)


def test_express_core_arraytype_constructor_args():
    sig = inspect.signature(express_core_ARRAYType.__init__)
    params = list(sig.parameters.keys())
    assert "isOptional" in params, "Missing parameter 'isOptional'"

def test_express_core_arraytype_has_isOptional():
    assert hasattr(express_core_ARRAYType, "isOptional")
    descriptor = None
    for klass in express_core_ARRAYType.__mro__:
        if "isOptional" in klass.__dict__:
            descriptor = klass.__dict__["isOptional"]
            break
    assert isinstance(descriptor, property)



def test_express_core_settype_is_not_abstract():
    assert not inspect.isabstract(express_core_SETType)


def test_express_core_settype_constructor_exists():
    assert callable(express_core_SETType.__init__)


def test_express_core_settype_constructor_args():
    sig = inspect.signature(express_core_SETType.__init__)
    params = list(sig.parameters.keys())



def test_express_core_bagtype_is_not_abstract():
    assert not inspect.isabstract(express_core_BAGType)


def test_express_core_bagtype_constructor_exists():
    assert callable(express_core_BAGType.__init__)


def test_express_core_bagtype_constructor_args():
    sig = inspect.signature(express_core_BAGType.__init__)
    params = list(sig.parameters.keys())



def test_express_core_listtype_is_not_abstract():
    assert not inspect.isabstract(express_core_LISTType)


def test_express_core_listtype_constructor_exists():
    assert callable(express_core_LISTType.__init__)


def test_express_core_listtype_constructor_args():
    sig = inspect.signature(express_core_LISTType.__init__)
    params = list(sig.parameters.keys())



def test_uniquerule_is_not_abstract():
    assert not inspect.isabstract(UniqueRule)


def test_uniquerule_constructor_exists():
    assert callable(UniqueRule.__init__)


def test_uniquerule_constructor_args():
    sig = inspect.signature(UniqueRule.__init__)
    params = list(sig.parameters.keys())



def test_rangerole_is_not_abstract():
    assert not inspect.isabstract(RangeRole)


def test_rangerole_constructor_exists():
    assert callable(RangeRole.__init__)


def test_rangerole_constructor_args():
    sig = inspect.signature(RangeRole.__init__)
    params = list(sig.parameters.keys())



def test_definedtype_is_not_abstract():
    assert not inspect.isabstract(DefinedType)


def test_definedtype_constructor_exists():
    assert callable(DefinedType.__init__)


def test_definedtype_constructor_args():
    sig = inspect.signature(DefinedType.__init__)
    params = list(sig.parameters.keys())



def test_express_core_specializedtype_is_not_abstract():
    assert not inspect.isabstract(express_core_SpecializedType)


def test_express_core_specializedtype_constructor_exists():
    assert callable(express_core_SpecializedType.__init__)


def test_express_core_specializedtype_constructor_args():
    sig = inspect.signature(express_core_SpecializedType.__init__)
    params = list(sig.parameters.keys())



def test_express_core_selecttype_is_not_abstract():
    assert not inspect.isabstract(express_core_SelectType)


def test_express_core_selecttype_constructor_exists():
    assert callable(express_core_SelectType.__init__)


def test_express_core_selecttype_constructor_args():
    sig = inspect.signature(express_core_SelectType.__init__)
    params = list(sig.parameters.keys())
    assert "isEntity" in params, "Missing parameter 'isEntity'"
    assert "isExtensible" in params, "Missing parameter 'isExtensible'"

def test_express_core_selecttype_has_isEntity():
    assert hasattr(express_core_SelectType, "isEntity")
    descriptor = None
    for klass in express_core_SelectType.__mro__:
        if "isEntity" in klass.__dict__:
            descriptor = klass.__dict__["isEntity"]
            break
    assert isinstance(descriptor, property)

def test_express_core_selecttype_has_isExtensible():
    assert hasattr(express_core_SelectType, "isExtensible")
    descriptor = None
    for klass in express_core_SelectType.__mro__:
        if "isExtensible" in klass.__dict__:
            descriptor = klass.__dict__["isExtensible"]
            break
    assert isinstance(descriptor, property)



def test_express_core_enumerationtype_is_not_abstract():
    assert not inspect.isabstract(express_core_EnumerationType)


def test_express_core_enumerationtype_constructor_exists():
    assert callable(express_core_EnumerationType.__init__)


def test_express_core_enumerationtype_constructor_args():
    sig = inspect.signature(express_core_EnumerationType.__init__)
    params = list(sig.parameters.keys())
    assert "isExtensible" in params, "Missing parameter 'isExtensible'"

def test_express_core_enumerationtype_has_isExtensible():
    assert hasattr(express_core_EnumerationType, "isExtensible")
    descriptor = None
    for klass in express_core_EnumerationType.__mro__:
        if "isExtensible" in klass.__dict__:
            descriptor = klass.__dict__["isExtensible"]
            break
    assert isinstance(descriptor, property)



def test_invertibleattribute_is_not_abstract():
    assert not inspect.isabstract(InvertibleAttribute)


def test_invertibleattribute_constructor_exists():
    assert callable(InvertibleAttribute.__init__)


def test_invertibleattribute_constructor_args():
    sig = inspect.signature(InvertibleAttribute.__init__)
    params = list(sig.parameters.keys())



def test_domainrole_is_not_abstract():
    assert not inspect.isabstract(DomainRole)


def test_domainrole_constructor_exists():
    assert callable(DomainRole.__init__)


def test_domainrole_constructor_args():
    sig = inspect.signature(DomainRole.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_express_core_partialentitytype_is_not_abstract():
    assert not inspect.isabstract(express_core_PartialEntityType)


def test_express_core_partialentitytype_constructor_exists():
    assert callable(express_core_PartialEntityType.__init__)


def test_express_core_partialentitytype_constructor_args():
    sig = inspect.signature(express_core_PartialEntityType.__init__)
    params = list(sig.parameters.keys())



def test_scope_is_not_abstract():
    assert not inspect.isabstract(Scope)


def test_scope_constructor_exists():
    assert callable(Scope.__init__)


def test_scope_constructor_args():
    sig = inspect.signature(Scope.__init__)
    params = list(sig.parameters.keys())



def test_express_core_localscope_is_not_abstract():
    assert not inspect.isabstract(express_core_LocalScope)


def test_express_core_localscope_constructor_exists():
    assert callable(express_core_LocalScope.__init__)


def test_express_core_localscope_constructor_args():
    sig = inspect.signature(express_core_LocalScope.__init__)
    params = list(sig.parameters.keys())



def test_express_core_schema_is_not_abstract():
    assert not inspect.isabstract(express_core_Schema)


def test_express_core_schema_constructor_exists():
    assert callable(express_core_Schema.__init__)


def test_express_core_schema_constructor_args():
    sig = inspect.signature(express_core_Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "version" in params, "Missing parameter 'version'"

def test_express_core_schema_has_name():
    assert hasattr(express_core_Schema, "name")
    descriptor = None
    for klass in express_core_Schema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_express_core_schema_has_version():
    assert hasattr(express_core_Schema, "version")
    descriptor = None
    for klass in express_core_Schema.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_instance_is_not_abstract():
    assert not inspect.isabstract(Instance)


def test_instance_constructor_exists():
    assert callable(Instance.__init__)


def test_instance_constructor_args():
    sig = inspect.signature(Instance.__init__)
    params = list(sig.parameters.keys())



def test_express_instances_partialentityvalue_is_not_abstract():
    assert not inspect.isabstract(express_instances_PartialEntityValue)


def test_express_instances_partialentityvalue_constructor_exists():
    assert callable(express_instances_PartialEntityValue.__init__)


def test_express_instances_partialentityvalue_constructor_args():
    sig = inspect.signature(express_instances_PartialEntityValue.__init__)
    params = list(sig.parameters.keys())



def test_express_instances_indeterminate_is_not_abstract():
    assert not inspect.isabstract(express_instances_Indeterminate)


def test_express_instances_indeterminate_constructor_exists():
    assert callable(express_instances_Indeterminate.__init__)


def test_express_instances_indeterminate_constructor_args():
    sig = inspect.signature(express_instances_Indeterminate.__init__)
    params = list(sig.parameters.keys())



def test_express_instances_typedinstance_is_not_abstract():
    assert not inspect.isabstract(express_instances_TypedInstance)


def test_express_instances_typedinstance_constructor_exists():
    assert callable(express_instances_TypedInstance.__init__)


def test_express_instances_typedinstance_constructor_args():
    sig = inspect.signature(express_instances_TypedInstance.__init__)
    params = list(sig.parameters.keys())



def test_express_instances_concretevalue_is_not_abstract():
    assert not inspect.isabstract(express_instances_ConcreteValue)


def test_express_instances_concretevalue_constructor_exists():
    assert callable(express_instances_ConcreteValue.__init__)


def test_express_instances_concretevalue_constructor_args():
    sig = inspect.signature(express_instances_ConcreteValue.__init__)
    params = list(sig.parameters.keys())



def test_express_core_expression_is_not_abstract():
    assert not inspect.isabstract(express_core_Expression)


def test_express_core_expression_constructor_exists():
    assert callable(express_core_Expression.__init__)


def test_express_core_expression_constructor_args():
    sig = inspect.signature(express_core_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_express_core_expression_has_text():
    assert hasattr(express_core_Expression, "text")
    descriptor = None
    for klass in express_core_Expression.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_instantiabletype_is_not_abstract():
    assert not inspect.isabstract(InstantiableType)


def test_instantiabletype_constructor_exists():
    assert callable(InstantiableType.__init__)


def test_instantiabletype_constructor_args():
    sig = inspect.signature(InstantiableType.__init__)
    params = list(sig.parameters.keys())



def test_express_core_concretetype_is_not_abstract():
    assert not inspect.isabstract(express_core_ConcreteType)


def test_express_core_concretetype_constructor_exists():
    assert callable(express_core_ConcreteType.__init__)


def test_express_core_concretetype_constructor_args():
    sig = inspect.signature(express_core_ConcreteType.__init__)
    params = list(sig.parameters.keys())



def test_core_aggregationtype_is_not_abstract():
    assert not inspect.isabstract(core_AggregationType)


def test_core_aggregationtype_constructor_exists():
    assert callable(core_AggregationType.__init__)


def test_core_aggregationtype_constructor_args():
    sig = inspect.signature(core_AggregationType.__init__)
    params = list(sig.parameters.keys())



def test_express_core_concreteaggregationtype_is_not_abstract():
    assert not inspect.isabstract(express_core_ConcreteAggregationType)


def test_express_core_concreteaggregationtype_constructor_exists():
    assert callable(express_core_ConcreteAggregationType.__init__)


def test_express_core_concreteaggregationtype_constructor_args():
    sig = inspect.signature(express_core_ConcreteAggregationType.__init__)
    params = list(sig.parameters.keys())



def test_express_algorithms_actualaggregationtype_is_not_abstract():
    assert not inspect.isabstract(express_algorithms_ActualAggregationType)


def test_express_algorithms_actualaggregationtype_constructor_exists():
    assert callable(express_algorithms_ActualAggregationType.__init__)


def test_express_algorithms_actualaggregationtype_constructor_args():
    sig = inspect.signature(express_algorithms_ActualAggregationType.__init__)
    params = list(sig.parameters.keys())



def test_core_generalizedtype_is_not_abstract():
    assert not inspect.isabstract(core_GeneralizedType)


def test_core_generalizedtype_constructor_exists():
    assert callable(core_GeneralizedType.__init__)


def test_core_generalizedtype_constructor_args():
    sig = inspect.signature(core_GeneralizedType.__init__)
    params = list(sig.parameters.keys())



def test_express_core_generalaggregationtype_is_not_abstract():
    assert not inspect.isabstract(express_core_GeneralAggregationType)


def test_express_core_generalaggregationtype_constructor_exists():
    assert callable(express_core_GeneralAggregationType.__init__)


def test_express_core_generalaggregationtype_constructor_args():
    sig = inspect.signature(express_core_GeneralAggregationType.__init__)
    params = list(sig.parameters.keys())



def test_core_typeelement_is_not_abstract():
    assert not inspect.isabstract(core_TypeElement)


def test_core_typeelement_constructor_exists():
    assert callable(core_TypeElement.__init__)


def test_core_typeelement_constructor_args():
    sig = inspect.signature(core_TypeElement.__init__)
    params = list(sig.parameters.keys())



def test_express_instances_enumerationitem_is_not_abstract():
    assert not inspect.isabstract(express_instances_EnumerationItem)


def test_express_instances_enumerationitem_constructor_exists():
    assert callable(express_instances_EnumerationItem.__init__)


def test_express_instances_enumerationitem_constructor_args():
    sig = inspect.signature(express_instances_EnumerationItem.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_express_instances_enumerationitem_has_position():
    assert hasattr(express_instances_EnumerationItem, "position")
    descriptor = None
    for klass in express_instances_EnumerationItem.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_core_domainconstraint_is_not_abstract():
    assert not inspect.isabstract(core_DomainConstraint)


def test_core_domainconstraint_constructor_exists():
    assert callable(core_DomainConstraint.__init__)


def test_core_domainconstraint_constructor_args():
    sig = inspect.signature(core_DomainConstraint.__init__)
    params = list(sig.parameters.keys())



def test_express_core_domainrule_is_not_abstract():
    assert not inspect.isabstract(express_core_DomainRule)


def test_express_core_domainrule_constructor_exists():
    assert callable(express_core_DomainRule.__init__)


def test_express_core_domainrule_constructor_args():
    sig = inspect.signature(express_core_DomainRule.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_express_core_domainrule_has_position():
    assert hasattr(express_core_DomainRule, "position")
    descriptor = None
    for klass in express_core_DomainRule.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_generalaggregationtype_is_not_abstract():
    assert not inspect.isabstract(GeneralAggregationType)


def test_generalaggregationtype_constructor_exists():
    assert callable(GeneralAggregationType.__init__)


def test_generalaggregationtype_constructor_args():
    sig = inspect.signature(GeneralAggregationType.__init__)
    params = list(sig.parameters.keys())



def test_express_core_generalsettype_is_not_abstract():
    assert not inspect.isabstract(express_core_GeneralSETType)


def test_express_core_generalsettype_constructor_exists():
    assert callable(express_core_GeneralSETType.__init__)


def test_express_core_generalsettype_constructor_args():
    sig = inspect.signature(express_core_GeneralSETType.__init__)
    params = list(sig.parameters.keys())



def test_express_core_generalarraytype_is_not_abstract():
    assert not inspect.isabstract(express_core_GeneralARRAYType)


def test_express_core_generalarraytype_constructor_exists():
    assert callable(express_core_GeneralARRAYType.__init__)


def test_express_core_generalarraytype_constructor_args():
    sig = inspect.signature(express_core_GeneralARRAYType.__init__)
    params = list(sig.parameters.keys())
    assert "isOptional" in params, "Missing parameter 'isOptional'"

def test_express_core_generalarraytype_has_isOptional():
    assert hasattr(express_core_GeneralARRAYType, "isOptional")
    descriptor = None
    for klass in express_core_GeneralARRAYType.__mro__:
        if "isOptional" in klass.__dict__:
            descriptor = klass.__dict__["isOptional"]
            break
    assert isinstance(descriptor, property)



def test_express_core_generallisttype_is_not_abstract():
    assert not inspect.isabstract(express_core_GeneralLISTType)


def test_express_core_generallisttype_constructor_exists():
    assert callable(express_core_GeneralLISTType.__init__)


def test_express_core_generallisttype_constructor_args():
    sig = inspect.signature(express_core_GeneralLISTType.__init__)
    params = list(sig.parameters.keys())



def test_express_core_generalbagtype_is_not_abstract():
    assert not inspect.isabstract(express_core_GeneralBAGType)


def test_express_core_generalbagtype_constructor_exists():
    assert callable(express_core_GeneralBAGType.__init__)


def test_express_core_generalbagtype_constructor_args():
    sig = inspect.signature(express_core_GeneralBAGType.__init__)
    params = list(sig.parameters.keys())



def test_actualstructureconstraint_is_not_abstract():
    assert not inspect.isabstract(ActualStructureConstraint)


def test_actualstructureconstraint_constructor_exists():
    assert callable(ActualStructureConstraint.__init__)


def test_actualstructureconstraint_constructor_args():
    sig = inspect.signature(ActualStructureConstraint.__init__)
    params = list(sig.parameters.keys())



def test_parametertype_is_not_abstract():
    assert not inspect.isabstract(ParameterType)


def test_parametertype_constructor_exists():
    assert callable(ParameterType.__init__)


def test_parametertype_constructor_args():
    sig = inspect.signature(ParameterType.__init__)
    params = list(sig.parameters.keys())



def test_express_core_arraybound_is_not_abstract():
    assert not inspect.isabstract(express_core_ArrayBound)


def test_express_core_arraybound_constructor_exists():
    assert callable(express_core_ArrayBound.__init__)


def test_express_core_arraybound_constructor_args():
    sig = inspect.signature(express_core_ArrayBound.__init__)
    params = list(sig.parameters.keys())
    assert "bound" in params, "Missing parameter 'bound'"

def test_express_core_arraybound_has_bound():
    assert hasattr(express_core_ArrayBound, "bound")
    descriptor = None
    for klass in express_core_ArrayBound.__mro__:
        if "bound" in klass.__dict__:
            descriptor = klass.__dict__["bound"]
            break
    assert isinstance(descriptor, property)



def test_core_attributetype_is_not_abstract():
    assert not inspect.isabstract(core_AttributeType)


def test_core_attributetype_constructor_exists():
    assert callable(core_AttributeType.__init__)


def test_core_attributetype_constructor_args():
    sig = inspect.signature(core_AttributeType.__init__)
    params = list(sig.parameters.keys())



def test_express_core_namedtype_is_not_abstract():
    assert not inspect.isabstract(express_core_NamedType)


def test_express_core_namedtype_constructor_exists():
    assert callable(express_core_NamedType.__init__)


def test_express_core_namedtype_constructor_args():
    sig = inspect.signature(express_core_NamedType.__init__)
    params = list(sig.parameters.keys())



def test_express_core_generalizedtype_is_not_abstract():
    assert not inspect.isabstract(express_core_GeneralizedType)


def test_express_core_generalizedtype_constructor_exists():
    assert callable(express_core_GeneralizedType.__init__)


def test_express_core_generalizedtype_constructor_args():
    sig = inspect.signature(express_core_GeneralizedType.__init__)
    params = list(sig.parameters.keys())



def test_core_datatype_is_not_abstract():
    assert not inspect.isabstract(core_DataType)


def test_core_datatype_constructor_exists():
    assert callable(core_DataType.__init__)


def test_core_datatype_constructor_args():
    sig = inspect.signature(core_DataType.__init__)
    params = list(sig.parameters.keys())



def test_express_core_variabletype_is_not_abstract():
    assert not inspect.isabstract(express_core_VariableType)


def test_express_core_variabletype_constructor_exists():
    assert callable(express_core_VariableType.__init__)


def test_express_core_variabletype_constructor_args():
    sig = inspect.signature(express_core_VariableType.__init__)
    params = list(sig.parameters.keys())



def test_enumerationtype_is_not_abstract():
    assert not inspect.isabstract(EnumerationType)


def test_enumerationtype_constructor_exists():
    assert callable(EnumerationType.__init__)


def test_enumerationtype_constructor_args():
    sig = inspect.signature(EnumerationType.__init__)
    params = list(sig.parameters.keys())



def test_express_expressions_variableref_is_not_abstract():
    assert not inspect.isabstract(express_expressions_VariableRef)


def test_express_expressions_variableref_constructor_exists():
    assert callable(express_expressions_VariableRef.__init__)


def test_express_expressions_variableref_constructor_args():
    sig = inspect.signature(express_expressions_VariableRef.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_express_expressions_variableref_has_id():
    assert hasattr(express_expressions_VariableRef, "id")
    descriptor = None
    for klass in express_expressions_VariableRef.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_namedtype_is_not_abstract():
    assert not inspect.isabstract(NamedType)


def test_namedtype_constructor_exists():
    assert callable(NamedType.__init__)


def test_namedtype_constructor_args():
    sig = inspect.signature(NamedType.__init__)
    params = list(sig.parameters.keys())



def test_express_expressions_extentref_is_not_abstract():
    assert not inspect.isabstract(express_expressions_ExtentRef)


def test_express_expressions_extentref_constructor_exists():
    assert callable(express_expressions_ExtentRef.__init__)


def test_express_expressions_extentref_constructor_args():
    sig = inspect.signature(express_expressions_ExtentRef.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_express_expressions_extentref_has_id():
    assert hasattr(express_expressions_ExtentRef, "id")
    descriptor = None
    for klass in express_expressions_ExtentRef.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_listmember_is_not_abstract():
    assert not inspect.isabstract(ListMember)


def test_listmember_constructor_exists():
    assert callable(ListMember.__init__)


def test_listmember_constructor_args():
    sig = inspect.signature(ListMember.__init__)
    params = list(sig.parameters.keys())



def test_repeatcount_is_not_abstract():
    assert not inspect.isabstract(RepeatCount)


def test_repeatcount_constructor_exists():
    assert callable(RepeatCount.__init__)


def test_repeatcount_constructor_args():
    sig = inspect.signature(RepeatCount.__init__)
    params = list(sig.parameters.keys())



def test_express_expressions_memberbinding_is_not_abstract():
    assert not inspect.isabstract(express_expressions_MemberBinding)


def test_express_expressions_memberbinding_constructor_exists():
    assert callable(express_expressions_MemberBinding.__init__)


def test_express_expressions_memberbinding_constructor_args():
    sig = inspect.signature(express_expressions_MemberBinding.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_express_expressions_memberbinding_has_position():
    assert hasattr(express_expressions_MemberBinding, "position")
    descriptor = None
    for klass in express_expressions_MemberBinding.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_functionresult_is_not_abstract():
    assert not inspect.isabstract(FunctionResult)


def test_functionresult_constructor_exists():
    assert callable(FunctionResult.__init__)


def test_functionresult_constructor_args():
    sig = inspect.signature(FunctionResult.__init__)
    params = list(sig.parameters.keys())



def test_function_is_not_abstract():
    assert not inspect.isabstract(Function)


def test_function_constructor_exists():
    assert callable(Function.__init__)


def test_function_constructor_args():
    sig = inspect.signature(Function.__init__)
    params = list(sig.parameters.keys())



def test_express_expressions_functioncall_is_not_abstract():
    assert not inspect.isabstract(express_expressions_FunctionCall)


def test_express_expressions_functioncall_constructor_exists():
    assert callable(express_expressions_FunctionCall.__init__)


def test_express_expressions_functioncall_constructor_args():
    sig = inspect.signature(express_expressions_FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_sizeconstraint_is_not_abstract():
    assert not inspect.isabstract(SizeConstraint)


def test_sizeconstraint_constructor_exists():
    assert callable(SizeConstraint.__init__)


def test_sizeconstraint_constructor_args():
    sig = inspect.signature(SizeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_generalizedtype_is_not_abstract():
    assert not inspect.isabstract(GeneralizedType)


def test_generalizedtype_constructor_exists():
    assert callable(GeneralizedType.__init__)


def test_generalizedtype_constructor_args():
    sig = inspect.signature(GeneralizedType.__init__)
    params = list(sig.parameters.keys())



def test_express_core_generictype_is_not_abstract():
    assert not inspect.isabstract(express_core_GenericType)


def test_express_core_generictype_constructor_exists():
    assert callable(express_core_GenericType.__init__)


def test_express_core_generictype_constructor_args():
    sig = inspect.signature(express_core_GenericType.__init__)
    params = list(sig.parameters.keys())
    assert "isEntity" in params, "Missing parameter 'isEntity'"

def test_express_core_generictype_has_isEntity():
    assert hasattr(express_core_GenericType, "isEntity")
    descriptor = None
    for klass in express_core_GenericType.__mro__:
        if "isEntity" in klass.__dict__:
            descriptor = klass.__dict__["isEntity"]
            break
    assert isinstance(descriptor, property)



def test_express_core_aggregatetype_is_not_abstract():
    assert not inspect.isabstract(express_core_AGGREGATEType)


def test_express_core_aggregatetype_constructor_exists():
    assert callable(express_core_AGGREGATEType.__init__)


def test_express_core_aggregatetype_constructor_args():
    sig = inspect.signature(express_core_AGGREGATEType.__init__)
    params = list(sig.parameters.keys())



def test_partialentitytype_is_not_abstract():
    assert not inspect.isabstract(PartialEntityType)


def test_partialentitytype_constructor_exists():
    assert callable(PartialEntityType.__init__)


def test_partialentitytype_constructor_args():
    sig = inspect.signature(PartialEntityType.__init__)
    params = list(sig.parameters.keys())



def test_express_core_singleentitytype_is_not_abstract():
    assert not inspect.isabstract(express_core_SingleEntityType)


def test_express_core_singleentitytype_constructor_exists():
    assert callable(express_core_SingleEntityType.__init__)


def test_express_core_singleentitytype_constructor_args():
    sig = inspect.signature(express_core_SingleEntityType.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_express_core_schemaelement_is_not_abstract():
    assert not inspect.isabstract(express_core_SchemaElement)


def test_express_core_schemaelement_constructor_exists():
    assert callable(express_core_SchemaElement.__init__)


def test_express_core_schemaelement_constructor_args():
    sig = inspect.signature(express_core_SchemaElement.__init__)
    params = list(sig.parameters.keys())



def test_express_core_localelement_is_not_abstract():
    assert not inspect.isabstract(express_core_LocalElement)


def test_express_core_localelement_constructor_exists():
    assert callable(express_core_LocalElement.__init__)


def test_express_core_localelement_constructor_args():
    sig = inspect.signature(express_core_LocalElement.__init__)
    params = list(sig.parameters.keys())



def test_express_core_typeelement_is_not_abstract():
    assert not inspect.isabstract(express_core_TypeElement)


def test_express_core_typeelement_constructor_exists():
    assert callable(express_core_TypeElement.__init__)


def test_express_core_typeelement_constructor_args():
    sig = inspect.signature(express_core_TypeElement.__init__)
    params = list(sig.parameters.keys())



def test_core_expression_is_not_abstract():
    assert not inspect.isabstract(core_Expression)


def test_core_expression_constructor_exists():
    assert callable(core_Expression.__init__)


def test_core_expression_constructor_args():
    sig = inspect.signature(core_Expression.__init__)
    params = list(sig.parameters.keys())



def test_express_expressions_queryexpression_is_not_abstract():
    assert not inspect.isabstract(express_expressions_QueryExpression)


def test_express_expressions_queryexpression_constructor_exists():
    assert callable(express_expressions_QueryExpression.__init__)


def test_express_expressions_queryexpression_constructor_args():
    sig = inspect.signature(express_expressions_QueryExpression.__init__)
    params = list(sig.parameters.keys())



def test_constant_is_not_abstract():
    assert not inspect.isabstract(Constant)


def test_constant_constructor_exists():
    assert callable(Constant.__init__)


def test_constant_constructor_args():
    sig = inspect.signature(Constant.__init__)
    params = list(sig.parameters.keys())



def test_express_expressions_constantref_is_not_abstract():
    assert not inspect.isabstract(express_expressions_ConstantRef)


def test_express_expressions_constantref_constructor_exists():
    assert callable(express_expressions_ConstantRef.__init__)


def test_express_expressions_constantref_constructor_args():
    sig = inspect.signature(express_expressions_ConstantRef.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_express_expressions_constantref_has_id():
    assert hasattr(express_expressions_ConstantRef, "id")
    descriptor = None
    for klass in express_expressions_ConstantRef.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_express_expressions_aggregateindex_is_not_abstract():
    assert not inspect.isabstract(express_expressions_AggregateIndex)


def test_express_expressions_aggregateindex_constructor_exists():
    assert callable(express_expressions_AggregateIndex.__init__)


def test_express_expressions_aggregateindex_constructor_args():
    sig = inspect.signature(express_expressions_AggregateIndex.__init__)
    params = list(sig.parameters.keys())



def test_attribute_is_not_abstract():
    assert not inspect.isabstract(Attribute)


def test_attribute_constructor_exists():
    assert callable(Attribute.__init__)


def test_attribute_constructor_args():
    sig = inspect.signature(Attribute.__init__)
    params = list(sig.parameters.keys())



def test_express_core_inverseattribute_is_not_abstract():
    assert not inspect.isabstract(express_core_InverseAttribute)


def test_express_core_inverseattribute_constructor_exists():
    assert callable(express_core_InverseAttribute.__init__)


def test_express_core_inverseattribute_constructor_args():
    sig = inspect.signature(express_core_InverseAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "isUnique" in params, "Missing parameter 'isUnique'"

def test_express_core_inverseattribute_has_isUnique():
    assert hasattr(express_core_InverseAttribute, "isUnique")
    descriptor = None
    for klass in express_core_InverseAttribute.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)



def test_express_core_explicitattribute_is_not_abstract():
    assert not inspect.isabstract(express_core_ExplicitAttribute)


def test_express_core_explicitattribute_constructor_exists():
    assert callable(express_core_ExplicitAttribute.__init__)


def test_express_core_explicitattribute_constructor_args():
    sig = inspect.signature(express_core_ExplicitAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "isOptional" in params, "Missing parameter 'isOptional'"

def test_express_core_explicitattribute_has_isOptional():
    assert hasattr(express_core_ExplicitAttribute, "isOptional")
    descriptor = None
    for klass in express_core_ExplicitAttribute.__mro__:
        if "isOptional" in klass.__dict__:
            descriptor = klass.__dict__["isOptional"]
            break
    assert isinstance(descriptor, property)



def test_express_core_derivedattribute_is_not_abstract():
    assert not inspect.isabstract(express_core_DerivedAttribute)


def test_express_core_derivedattribute_constructor_exists():
    assert callable(express_core_DerivedAttribute.__init__)


def test_express_core_derivedattribute_constructor_args():
    sig = inspect.signature(express_core_DerivedAttribute.__init__)
    params = list(sig.parameters.keys())



def test_selector_is_not_abstract():
    assert not inspect.isabstract(Selector)


def test_selector_constructor_exists():
    assert callable(Selector.__init__)


def test_selector_constructor_args():
    sig = inspect.signature(Selector.__init__)
    params = list(sig.parameters.keys())



def test_express_expressions_usedinref_is_not_abstract():
    assert not inspect.isabstract(express_expressions_UsedInRef)


def test_express_expressions_usedinref_constructor_exists():
    assert callable(express_expressions_UsedInRef.__init__)


def test_express_expressions_usedinref_constructor_args():
    sig = inspect.signature(express_expressions_UsedInRef.__init__)
    params = list(sig.parameters.keys())



def test_express_expressions_groupref_is_not_abstract():
    assert not inspect.isabstract(express_expressions_GroupRef)


def test_express_expressions_groupref_constructor_exists():
    assert callable(express_expressions_GroupRef.__init__)


def test_express_expressions_groupref_constructor_args():
    sig = inspect.signature(express_expressions_GroupRef.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_express_expressions_groupref_has_id():
    assert hasattr(express_expressions_GroupRef, "id")
    descriptor = None
    for klass in express_expressions_GroupRef.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_express_expressions_attributeref_is_not_abstract():
    assert not inspect.isabstract(express_expressions_AttributeRef)


def test_express_expressions_attributeref_constructor_exists():
    assert callable(express_expressions_AttributeRef.__init__)


def test_express_expressions_attributeref_constructor_args():
    sig = inspect.signature(express_expressions_AttributeRef.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_express_expressions_attributeref_has_id():
    assert hasattr(express_expressions_AttributeRef, "id")
    descriptor = None
    for klass in express_expressions_AttributeRef.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_attributevalue_is_not_abstract():
    assert not inspect.isabstract(AttributeValue)


def test_attributevalue_constructor_exists():
    assert callable(AttributeValue.__init__)


def test_attributevalue_constructor_args():
    sig = inspect.signature(AttributeValue.__init__)
    params = list(sig.parameters.keys())



def test_express_expressions_attributebinding_is_not_abstract():
    assert not inspect.isabstract(express_expressions_AttributeBinding)


def test_express_expressions_attributebinding_constructor_exists():
    assert callable(express_expressions_AttributeBinding.__init__)


def test_express_expressions_attributebinding_constructor_args():
    sig = inspect.signature(express_expressions_AttributeBinding.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_express_expressions_attributebinding_has_position():
    assert hasattr(express_expressions_AttributeBinding, "position")
    descriptor = None
    for klass in express_expressions_AttributeBinding.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_express_expressions_operation_is_not_abstract():
    assert not inspect.isabstract(express_expressions_Operation)


def test_express_expressions_operation_constructor_exists():
    assert callable(express_expressions_Operation.__init__)


def test_express_expressions_operation_constructor_args():
    sig = inspect.signature(express_expressions_Operation.__init__)
    params = list(sig.parameters.keys())



def test_express_expressions_queryvariable_is_not_abstract():
    assert not inspect.isabstract(express_expressions_QueryVariable)


def test_express_expressions_queryvariable_constructor_exists():
    assert callable(express_expressions_QueryVariable.__init__)


def test_express_expressions_queryvariable_constructor_args():
    sig = inspect.signature(express_expressions_QueryVariable.__init__)
    params = list(sig.parameters.keys())



def test_queryvariable_is_not_abstract():
    assert not inspect.isabstract(QueryVariable)


def test_queryvariable_constructor_exists():
    assert callable(QueryVariable.__init__)


def test_queryvariable_constructor_args():
    sig = inspect.signature(QueryVariable.__init__)
    params = list(sig.parameters.keys())



def test_express_expressions_primary_is_not_abstract():
    assert not inspect.isabstract(express_expressions_Primary)


def test_express_expressions_primary_constructor_exists():
    assert callable(express_expressions_Primary.__init__)


def test_express_expressions_primary_constructor_args():
    sig = inspect.signature(express_expressions_Primary.__init__)
    params = list(sig.parameters.keys())



def test_variabletype_is_not_abstract():
    assert not inspect.isabstract(VariableType)


def test_variabletype_constructor_exists():
    assert callable(VariableType.__init__)


def test_variabletype_constructor_args():
    sig = inspect.signature(VariableType.__init__)
    params = list(sig.parameters.keys())



def test_express_core_actualtype_is_not_abstract():
    assert not inspect.isabstract(express_core_ActualType)


def test_express_core_actualtype_constructor_exists():
    assert callable(express_core_ActualType.__init__)


def test_express_core_actualtype_constructor_args():
    sig = inspect.signature(express_core_ActualType.__init__)
    params = list(sig.parameters.keys())



def test_attributebinding_is_not_abstract():
    assert not inspect.isabstract(AttributeBinding)


def test_attributebinding_constructor_exists():
    assert callable(AttributeBinding.__init__)


def test_attributebinding_constructor_args():
    sig = inspect.signature(AttributeBinding.__init__)
    params = list(sig.parameters.keys())



def test_partialentityvalue_is_not_abstract():
    assert not inspect.isabstract(PartialEntityValue)


def test_partialentityvalue_constructor_exists():
    assert callable(PartialEntityValue.__init__)


def test_partialentityvalue_constructor_args():
    sig = inspect.signature(PartialEntityValue.__init__)
    params = list(sig.parameters.keys())



def test_express_instances_entityvalue_is_not_abstract():
    assert not inspect.isabstract(express_instances_EntityValue)


def test_express_instances_entityvalue_constructor_exists():
    assert callable(express_instances_EntityValue.__init__)


def test_express_instances_entityvalue_constructor_args():
    sig = inspect.signature(express_instances_EntityValue.__init__)
    params = list(sig.parameters.keys())



def test_express_expressions_partialentityconstructor_is_not_abstract():
    assert not inspect.isabstract(express_expressions_PartialEntityConstructor)


def test_express_expressions_partialentityconstructor_constructor_exists():
    assert callable(express_expressions_PartialEntityConstructor.__init__)


def test_express_expressions_partialentityconstructor_constructor_args():
    sig = inspect.signature(express_expressions_PartialEntityConstructor.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_express_expressions_partialentityconstructor_has_id():
    assert hasattr(express_expressions_PartialEntityConstructor, "id")
    descriptor = None
    for klass in express_expressions_PartialEntityConstructor.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_express_expressions_stringindex_is_not_abstract():
    assert not inspect.isabstract(express_expressions_StringIndex)


def test_express_expressions_stringindex_constructor_exists():
    assert callable(express_expressions_StringIndex.__init__)


def test_express_expressions_stringindex_constructor_args():
    sig = inspect.signature(express_expressions_StringIndex.__init__)
    params = list(sig.parameters.keys())



def test_memberbinding_is_not_abstract():
    assert not inspect.isabstract(MemberBinding)


def test_memberbinding_constructor_exists():
    assert callable(MemberBinding.__init__)


def test_memberbinding_constructor_args():
    sig = inspect.signature(MemberBinding.__init__)
    params = list(sig.parameters.keys())



def test_genericaggregate_is_not_abstract():
    assert not inspect.isabstract(GenericAggregate)


def test_genericaggregate_constructor_exists():
    assert callable(GenericAggregate.__init__)


def test_genericaggregate_constructor_args():
    sig = inspect.signature(GenericAggregate.__init__)
    params = list(sig.parameters.keys())



def test_express_expressions_aggregateinitializer_is_not_abstract():
    assert not inspect.isabstract(express_expressions_AggregateInitializer)


def test_express_expressions_aggregateinitializer_constructor_exists():
    assert callable(express_expressions_AggregateInitializer.__init__)


def test_express_expressions_aggregateinitializer_constructor_args():
    sig = inspect.signature(express_expressions_AggregateInitializer.__init__)
    params = list(sig.parameters.keys())



def test_express_expressions_parameterref_is_not_abstract():
    assert not inspect.isabstract(express_expressions_ParameterRef)


def test_express_expressions_parameterref_constructor_exists():
    assert callable(express_expressions_ParameterRef.__init__)


def test_express_expressions_parameterref_constructor_args():
    sig = inspect.signature(express_expressions_ParameterRef.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_express_expressions_parameterref_has_id():
    assert hasattr(express_expressions_ParameterRef, "id")
    descriptor = None
    for klass in express_expressions_ParameterRef.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_express_expressions_unaryoperation_is_not_abstract():
    assert not inspect.isabstract(express_expressions_UnaryOperation)


def test_express_expressions_unaryoperation_constructor_exists():
    assert callable(express_expressions_UnaryOperation.__init__)


def test_express_expressions_unaryoperation_constructor_args():
    sig = inspect.signature(express_expressions_UnaryOperation.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_express_expressions_unaryoperation_has_operator():
    assert hasattr(express_expressions_UnaryOperation, "operator")
    descriptor = None
    for klass in express_expressions_UnaryOperation.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_express_expressions_coercion_is_not_abstract():
    assert not inspect.isabstract(express_expressions_Coercion)


def test_express_expressions_coercion_constructor_exists():
    assert callable(express_expressions_Coercion.__init__)


def test_express_expressions_coercion_constructor_args():
    sig = inspect.signature(express_expressions_Coercion.__init__)
    params = list(sig.parameters.keys())



def test_express_expressions_binaryoperation_is_not_abstract():
    assert not inspect.isabstract(express_expressions_BinaryOperation)


def test_express_expressions_binaryoperation_constructor_exists():
    assert callable(express_expressions_BinaryOperation.__init__)


def test_express_expressions_binaryoperation_constructor_args():
    sig = inspect.signature(express_expressions_BinaryOperation.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_express_expressions_binaryoperation_has_operator():
    assert hasattr(express_expressions_BinaryOperation, "operator")
    descriptor = None
    for klass in express_expressions_BinaryOperation.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_express_algorithms_inparameter_is_not_abstract():
    assert not inspect.isabstract(express_algorithms_InParameter)


def test_express_algorithms_inparameter_constructor_exists():
    assert callable(express_algorithms_InParameter.__init__)


def test_express_algorithms_inparameter_constructor_args():
    sig = inspect.signature(express_algorithms_InParameter.__init__)
    params = list(sig.parameters.keys())



def test_functioncall_is_not_abstract():
    assert not inspect.isabstract(FunctionCall)


def test_functioncall_constructor_exists():
    assert callable(FunctionCall.__init__)


def test_functioncall_constructor_args():
    sig = inspect.signature(FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_procedurecall_is_not_abstract():
    assert not inspect.isabstract(ProcedureCall)


def test_procedurecall_constructor_exists():
    assert callable(ProcedureCall.__init__)


def test_procedurecall_constructor_args():
    sig = inspect.signature(ProcedureCall.__init__)
    params = list(sig.parameters.keys())



def test_express_expressions_indeterminateref_is_not_abstract():
    assert not inspect.isabstract(express_expressions_IndeterminateRef)


def test_express_expressions_indeterminateref_constructor_exists():
    assert callable(express_expressions_IndeterminateRef.__init__)


def test_express_expressions_indeterminateref_constructor_args():
    sig = inspect.signature(express_expressions_IndeterminateRef.__init__)
    params = list(sig.parameters.keys())



def test_express_expressions_actualparameter_is_not_abstract():
    assert not inspect.isabstract(express_expressions_ActualParameter)


def test_express_expressions_actualparameter_constructor_exists():
    assert callable(express_expressions_ActualParameter.__init__)


def test_express_expressions_actualparameter_constructor_args():
    sig = inspect.signature(express_expressions_ActualParameter.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_express_expressions_actualparameter_has_position():
    assert hasattr(express_expressions_ActualParameter, "position")
    descriptor = None
    for klass in express_expressions_ActualParameter.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)


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
SingleEntityValue_strategy = st.builds(
    SingleEntityValue,
)
instances_AggregateValue_strategy = st.builds(
    instances_AggregateValue,
)
core_Instance_strategy = st.builds(
    core_Instance,
)
express_instances_LISTValue_strategy = st.builds(
    express_instances_LISTValue,
)
LogicalValue_strategy = st.builds(
    LogicalValue,
)
express_instances_BooleanValue_strategy = st.builds(
    express_instances_BooleanValue,
)
NumberValue_strategy = st.builds(
    NumberValue,
)
express_instances_RealValue_strategy = st.builds(
    express_instances_RealValue,
)
express_instances_Population_strategy = st.builds(
    express_instances_Population,
)
express_instances_ArrayMember_strategy = st.builds(
    express_instances_ArrayMember,
    index=
        safe_text
)
instances_ConcreteValue_strategy = st.builds(
    instances_ConcreteValue,
)
instances_TypedInstance_strategy = st.builds(
    instances_TypedInstance,
)
BagMember_strategy = st.builds(
    BagMember,
)
LISTValue_strategy = st.builds(
    LISTValue,
)
express_instances_GenericAggregate_strategy = st.builds(
    express_instances_GenericAggregate,
)
express_instances_SingleEntityValue_strategy = st.builds(
    express_instances_SingleEntityValue,
)
express_instances_BagMember_strategy = st.builds(
    express_instances_BagMember,
    count=
        safe_text
)
express_instances_ListMember_strategy = st.builds(
    express_instances_ListMember,
    position=
        safe_text
)
EntityValue_strategy = st.builds(
    EntityValue,
)
TypedInstance_strategy = st.builds(
    TypedInstance,
)
express_instances_SpecializedValue_strategy = st.builds(
    express_instances_SpecializedValue,
)
express_instances_EntityInstance_strategy = st.builds(
    express_instances_EntityInstance,
    id=
        safe_text
)
StringValue_strategy = st.builds(
    StringValue,
)
express_instances_TypeName_strategy = st.builds(
    express_instances_TypeName,
)
express_instances_RoleName_strategy = st.builds(
    express_instances_RoleName,
)
ArrayMember_strategy = st.builds(
    ArrayMember,
)
AggregateValue_strategy = st.builds(
    AggregateValue,
)
express_instances_BAGValue_strategy = st.builds(
    express_instances_BAGValue,
)
express_instances_SETValue_strategy = st.builds(
    express_instances_SETValue,
)
express_instances_ARRAYValue_strategy = st.builds(
    express_instances_ARRAYValue,
)
express_instances_AttributeValue_strategy = st.builds(
    express_instances_AttributeValue,
)
core_GenericType_strategy = st.builds(
    core_GenericType,
)
algorithms_Parameter_strategy = st.builds(
    algorithms_Parameter,
)
ConcreteValue_strategy = st.builds(
    ConcreteValue,
)
express_instances_SimpleValue_strategy = st.builds(
    express_instances_SimpleValue,
    name=
        safe_text
)
express_instances_AggregateValue_strategy = st.builds(
    express_instances_AggregateValue,
)
RealValue_strategy = st.builds(
    RealValue,
)
express_instances_IntegerValue_strategy = st.builds(
    express_instances_IntegerValue,
)
AGGREGATEType_strategy = st.builds(
    AGGREGATEType,
)
express_algorithms_ActualStructureConstraint_strategy = st.builds(
    express_algorithms_ActualStructureConstraint,
    label=
        safe_text
)
ActualStructure_strategy = st.builds(
    ActualStructure,
)
express_algorithms_VARVariable_strategy = st.builds(
    express_algorithms_VARVariable,
)
core_ActualType_strategy = st.builds(
    core_ActualType,
)
EscapeStatement_strategy = st.builds(
    EscapeStatement,
)
SkipStatement_strategy = st.builds(
    SkipStatement,
)
StatementBlock_strategy = st.builds(
    StatementBlock,
)
express_algorithms_Statement_strategy = st.builds(
    express_algorithms_Statement,
    text=
        safe_text
)
ActualType_strategy = st.builds(
    ActualType,
)
express_algorithms_ActualAGGREGATEType_strategy = st.builds(
    express_algorithms_ActualAGGREGATEType,
    label=
        safe_text
)
express_algorithms_ActualGenericType_strategy = st.builds(
    express_algorithms_ActualGenericType,
    label=
        safe_text,
    isEntity=
        safe_text
)
core_AGGREGATEType_strategy = st.builds(
    core_AGGREGATEType,
)
algorithms_GenericElement_strategy = st.builds(
    algorithms_GenericElement,
)
express_algorithms_ActualDataType_strategy = st.builds(
    express_algorithms_ActualDataType,
)
express_algorithms_ActualStructure_strategy = st.builds(
    express_algorithms_ActualStructure,
)
InVariable_strategy = st.builds(
    InVariable,
)
ActualDataType_strategy = st.builds(
    ActualDataType,
)
GenericType_strategy = st.builds(
    GenericType,
)
ActualAggregationType_strategy = st.builds(
    ActualAggregationType,
)
express_algorithms_ActualLISTType_strategy = st.builds(
    express_algorithms_ActualLISTType,
)
express_algorithms_ActualBAGType_strategy = st.builds(
    express_algorithms_ActualBAGType,
)
express_algorithms_ActualSETType_strategy = st.builds(
    express_algorithms_ActualSETType,
)
express_algorithms_ActualARRAYType_strategy = st.builds(
    express_algorithms_ActualARRAYType,
    isOptional=
        safe_text
)
InParameter_strategy = st.builds(
    InParameter,
)
RepeatStatement_strategy = st.builds(
    RepeatStatement,
)
core_AnonymousType_strategy = st.builds(
    core_AnonymousType,
)
AlgorithmScope_strategy = st.builds(
    AlgorithmScope,
)
Algorithm_strategy = st.builds(
    Algorithm,
)
express_algorithms_Procedure_strategy = st.builds(
    express_algorithms_Procedure,
)
express_algorithms_Function_strategy = st.builds(
    express_algorithms_Function,
)
express_algorithms_ActualTypeConstraint_strategy = st.builds(
    express_algorithms_ActualTypeConstraint,
    label=
        safe_text
)
express_core_AggregationType_strategy = st.builds(
    express_core_AggregationType,
    ordering=
        safe_text,
    isUnique=
        safe_text
)
express_core_ScopedId_strategy = st.builds(
    express_core_ScopedId,
    localName=
        safe_text
)
DomainRule_strategy = st.builds(
    DomainRule,
)
SelectType_strategy = st.builds(
    SelectType,
)
core_CommonElement_strategy = st.builds(
    core_CommonElement,
)
core_Scope_strategy = st.builds(
    core_Scope,
)
express_core_Relationship_strategy = st.builds(
    express_core_Relationship,
)
express_core_ParameterType_strategy = st.builds(
    express_core_ParameterType,
)
express_core_Scope_strategy = st.builds(
    express_core_Scope,
)
express_core_Role_strategy = st.builds(
    express_core_Role,
)
express_core_Remark_strategy = st.builds(
    express_core_Remark,
    text=
        safe_text,
    isTagged=
        safe_text,
    isTail=
        safe_text
)
ArrayBound_strategy = st.builds(
    ArrayBound,
)
ConcreteType_strategy = st.builds(
    ConcreteType,
)
LocalScope_strategy = st.builds(
    LocalScope,
)
express_core_AlgorithmScope_strategy = st.builds(
    express_core_AlgorithmScope,
)
AnonymousType_strategy = st.builds(
    AnonymousType,
)
express_core_SimpleType_strategy = st.builds(
    express_core_SimpleType,
    id=
        safe_text
)
LengthConstraint_strategy = st.builds(
    LengthConstraint,
)
ActualTypeConstraint_strategy = st.builds(
    ActualTypeConstraint,
)
NumericType_strategy = st.builds(
    NumericType,
)
express_core_RealType_strategy = st.builds(
    express_core_RealType,
    precision=
        safe_text
)
DomainConstraint_strategy = st.builds(
    DomainConstraint,
)
express_core_SizeConstraint_strategy = st.builds(
    express_core_SizeConstraint,
    bound=
        safe_text
)
express_core_LengthConstraint_strategy = st.builds(
    express_core_LengthConstraint,
    maxLength=
        safe_text,
    isFixed=
        safe_text
)
express_core_AttributeType_strategy = st.builds(
    express_core_AttributeType,
)
express_core_Instance_strategy = st.builds(
    express_core_Instance,
)
express_core_NamedElement_strategy = st.builds(
    express_core_NamedElement,
)
core_VariableType_strategy = st.builds(
    core_VariableType,
)
express_core_DomainConstraint_strategy = st.builds(
    express_core_DomainConstraint,
)
TypeElement_strategy = st.builds(
    TypeElement,
)
express_core_UniqueRule_strategy = st.builds(
    express_core_UniqueRule,
    position=
        safe_text
)
core_ConcreteType_strategy = st.builds(
    core_ConcreteType,
)
SimpleType_strategy = st.builds(
    SimpleType,
)
express_core_StringType_strategy = st.builds(
    express_core_StringType,
)
express_core_BinaryType_strategy = st.builds(
    express_core_BinaryType,
)
express_core_LogicType_strategy = st.builds(
    express_core_LogicType,
)
express_core_NumericType_strategy = st.builds(
    express_core_NumericType,
)
express_core_Attribute_strategy = st.builds(
    express_core_Attribute,
    position=
        safe_text,
    isAbstract=
        safe_text
)
Relationship_strategy = st.builds(
    Relationship,
)
InverseAttribute_strategy = st.builds(
    InverseAttribute,
)
SchemaElement_strategy = st.builds(
    SchemaElement,
)
express_core_CommonElement_strategy = st.builds(
    express_core_CommonElement,
)
InterfacedElement_strategy = st.builds(
    InterfacedElement,
)
Remark_strategy = st.builds(
    Remark,
)
express_core_DataType_strategy = st.builds(
    express_core_DataType,
)
Schema_strategy = st.builds(
    Schema,
)
express_core_InterfacedElement_strategy = st.builds(
    express_core_InterfacedElement,
    isUSE=
        safe_text
)
core_ParameterType_strategy = st.builds(
    core_ParameterType,
)
express_core_InstantiableType_strategy = st.builds(
    express_core_InstantiableType,
)
core_InstantiableType_strategy = st.builds(
    core_InstantiableType,
)
express_core_AnonymousType_strategy = st.builds(
    express_core_AnonymousType,
)
core_NamedType_strategy = st.builds(
    core_NamedType,
)
express_core_DefinedType_strategy = st.builds(
    express_core_DefinedType,
)
express_core_EntityType_strategy = st.builds(
    express_core_EntityType,
    isAbstract=
        safe_text
)
Role_strategy = st.builds(
    Role,
)
express_core_RangeRole_strategy = st.builds(
    express_core_RangeRole,
)
express_core_DomainRole_strategy = st.builds(
    express_core_DomainRole,
)
Redeclaration_strategy = st.builds(
    Redeclaration,
)
AttributeType_strategy = st.builds(
    AttributeType,
)
express_core_Redeclaration_strategy = st.builds(
    express_core_Redeclaration,
    isMandatory=
        safe_text,
    position=
        safe_text
)
IndexOperation_strategy = st.builds(
    IndexOperation,
)
express_expressions_BinaryIndex_strategy = st.builds(
    express_expressions_BinaryIndex,
)
SimpleValue_strategy = st.builds(
    SimpleValue,
)
express_instances_NumberValue_strategy = st.builds(
    express_instances_NumberValue,
)
express_instances_BinaryValue_strategy = st.builds(
    express_instances_BinaryValue,
)
express_instances_LogicalValue_strategy = st.builds(
    express_instances_LogicalValue,
)
express_instances_StringValue_strategy = st.builds(
    express_instances_StringValue,
)
EnumerationItem_strategy = st.builds(
    EnumerationItem,
)
Primary_strategy = st.builds(
    Primary,
)
express_expressions_Literal_strategy = st.builds(
    express_expressions_Literal,
)
express_expressions_EnumItemRef_strategy = st.builds(
    express_expressions_EnumItemRef,
    id=
        safe_text
)
express_expressions_RepeatCount_strategy = st.builds(
    express_expressions_RepeatCount,
)
express_expressions_SELFRef_strategy = st.builds(
    express_expressions_SELFRef,
)
Indeterminate_strategy = st.builds(
    Indeterminate,
)
CaseAction_strategy = st.builds(
    CaseAction,
)
Variable_strategy = st.builds(
    Variable,
)
express_algorithms_FunctionResult_strategy = st.builds(
    express_algorithms_FunctionResult,
)
express_algorithms_InVariable_strategy = st.builds(
    express_algorithms_InVariable,
)
express_algorithms_LocalVariable_strategy = st.builds(
    express_algorithms_LocalVariable,
)
SingleEntityType_strategy = st.builds(
    SingleEntityType,
)
ControlVariable_strategy = st.builds(
    ControlVariable,
)
ExplicitAttribute_strategy = st.builds(
    ExplicitAttribute,
)
express_core_InvertibleAttribute_strategy = st.builds(
    express_core_InvertibleAttribute,
)
express_statements_VARExpression_strategy = st.builds(
    express_statements_VARExpression,
    text=
        safe_text
)
VARVariable_strategy = st.builds(
    VARVariable,
)
algorithms_VARVariable_strategy = st.builds(
    algorithms_VARVariable,
)
express_algorithms_VARParameter_strategy = st.builds(
    express_algorithms_VARParameter,
)
algorithms_NamedVariable_strategy = st.builds(
    algorithms_NamedVariable,
)
express_statements_AliasVariable_strategy = st.builds(
    express_statements_AliasVariable,
)
NamedVariable_strategy = st.builds(
    NamedVariable,
)
express_algorithms_Variable_strategy = st.builds(
    express_algorithms_Variable,
)
express_statements_ControlVariable_strategy = st.builds(
    express_statements_ControlVariable,
)
AliasVariable_strategy = st.builds(
    AliasVariable,
)
VARExpression_strategy = st.builds(
    VARExpression,
)
express_statements_AttributeCell_strategy = st.builds(
    express_statements_AttributeCell,
    id=
        safe_text
)
express_statements_GroupCell_strategy = st.builds(
    express_statements_GroupCell,
    id=
        safe_text
)
express_statements_MemberCell_strategy = st.builds(
    express_statements_MemberCell,
)
express_statements_VARCell_strategy = st.builds(
    express_statements_VARCell,
    id=
        safe_text
)
express_statements_VariableCell_strategy = st.builds(
    express_statements_VariableCell,
    id=
        safe_text
)
core_LocalScope_strategy = st.builds(
    core_LocalScope,
)
algorithms_Statement_strategy = st.builds(
    algorithms_Statement,
)
express_statements_RepeatStatement_strategy = st.builds(
    express_statements_RepeatStatement,
)
express_statements_AliasStatement_strategy = st.builds(
    express_statements_AliasStatement,
)
ControlStatement_strategy = st.builds(
    ControlStatement,
)
express_statements_ReturnStatement_strategy = st.builds(
    express_statements_ReturnStatement,
)
express_statements_EscapeStatement_strategy = st.builds(
    express_statements_EscapeStatement,
)
express_statements_NullStatement_strategy = st.builds(
    express_statements_NullStatement,
)
express_statements_SkipStatement_strategy = st.builds(
    express_statements_SkipStatement,
)
express_statements_CaseAction_strategy = st.builds(
    express_statements_CaseAction,
    isDefault=
        safe_text
)
LocalElement_strategy = st.builds(
    LocalElement,
)
express_algorithms_GenericElement_strategy = st.builds(
    express_algorithms_GenericElement,
)
express_algorithms_NamedVariable_strategy = st.builds(
    express_algorithms_NamedVariable,
)
express_algorithms_Parameter_strategy = st.builds(
    express_algorithms_Parameter,
    inout=
        safe_text,
    position=
        safe_text
)
express_rules_NamedRule_strategy = st.builds(
    express_rules_NamedRule,
    position=
        safe_text
)
NamedRule_strategy = st.builds(
    NamedRule,
)
Statement_strategy = st.builds(
    Statement,
)
express_statements_IfStatement_strategy = st.builds(
    express_statements_IfStatement,
)
express_statements_Assignment_strategy = st.builds(
    express_statements_Assignment,
)
express_statements_StatementBlock_strategy = st.builds(
    express_statements_StatementBlock,
    delimited=
        safe_text
)
express_statements_CaseStatement_strategy = st.builds(
    express_statements_CaseStatement,
)
express_statements_ControlStatement_strategy = st.builds(
    express_statements_ControlStatement,
)
core_AlgorithmScope_strategy = st.builds(
    core_AlgorithmScope,
)
express_algorithms_Algorithm_strategy = st.builds(
    express_algorithms_Algorithm,
)
core_SchemaElement_strategy = st.builds(
    core_SchemaElement,
)
express_rules_GlobalRule_strategy = st.builds(
    express_rules_GlobalRule,
)
ScopedId_strategy = st.builds(
    ScopedId,
)
GlobalRule_strategy = st.builds(
    GlobalRule,
)
Population_strategy = st.builds(
    Population,
)
EntityInstance_strategy = st.builds(
    EntityInstance,
)
express_instances_SingleLeafInstance_strategy = st.builds(
    express_instances_SingleLeafInstance,
)
express_instances_MultiLeafInstance_strategy = st.builds(
    express_instances_MultiLeafInstance,
)
SETValue_strategy = st.builds(
    SETValue,
)
express_rules_Extent_strategy = st.builds(
    express_rules_Extent,
)
SupertypeRule_strategy = st.builds(
    SupertypeRule,
)
Expression_strategy = st.builds(
    Expression,
)
express_expressions_IndexOperation_strategy = st.builds(
    express_expressions_IndexOperation,
)
express_expressions_Selector_strategy = st.builds(
    express_expressions_Selector,
)
Extent_strategy = st.builds(
    Extent,
)
express_rules_SubtypeConstraint_strategy = st.builds(
    express_rules_SubtypeConstraint,
)
ActualParameter_strategy = st.builds(
    ActualParameter,
)
Procedure_strategy = st.builds(
    Procedure,
)
express_statements_ProcedureCall_strategy = st.builds(
    express_statements_ProcedureCall,
)
EntityType_strategy = st.builds(
    EntityType,
)
CommonElement_strategy = st.builds(
    CommonElement,
)
express_instances_Constant_strategy = st.builds(
    express_instances_Constant,
)
express_rules_SupertypeRule_strategy = st.builds(
    express_rules_SupertypeRule,
    assertsAbstract=
        safe_text
)
SubtypeConstraint_strategy = st.builds(
    SubtypeConstraint,
)
express_rules_ANDConstraint_strategy = st.builds(
    express_rules_ANDConstraint,
)
express_rules_TOTAL_OVERConstraint_strategy = st.builds(
    express_rules_TOTAL_OVERConstraint,
)
express_rules_ONEOFConstraint_strategy = st.builds(
    express_rules_ONEOFConstraint,
)
ConcreteAggregationType_strategy = st.builds(
    ConcreteAggregationType,
)
express_core_ARRAYType_strategy = st.builds(
    express_core_ARRAYType,
    isOptional=
        safe_text
)
express_core_SETType_strategy = st.builds(
    express_core_SETType,
)
express_core_BAGType_strategy = st.builds(
    express_core_BAGType,
)
express_core_LISTType_strategy = st.builds(
    express_core_LISTType,
)
UniqueRule_strategy = st.builds(
    UniqueRule,
)
RangeRole_strategy = st.builds(
    RangeRole,
)
DefinedType_strategy = st.builds(
    DefinedType,
)
express_core_SpecializedType_strategy = st.builds(
    express_core_SpecializedType,
)
express_core_SelectType_strategy = st.builds(
    express_core_SelectType,
    isEntity=
        safe_text,
    isExtensible=
        safe_text
)
express_core_EnumerationType_strategy = st.builds(
    express_core_EnumerationType,
    isExtensible=
        safe_text
)
InvertibleAttribute_strategy = st.builds(
    InvertibleAttribute,
)
DomainRole_strategy = st.builds(
    DomainRole,
)
DataType_strategy = st.builds(
    DataType,
)
express_core_PartialEntityType_strategy = st.builds(
    express_core_PartialEntityType,
)
Scope_strategy = st.builds(
    Scope,
)
express_core_LocalScope_strategy = st.builds(
    express_core_LocalScope,
)
express_core_Schema_strategy = st.builds(
    express_core_Schema,
    name=
        safe_text,
    version=
        safe_text
)
Instance_strategy = st.builds(
    Instance,
)
express_instances_PartialEntityValue_strategy = st.builds(
    express_instances_PartialEntityValue,
)
express_instances_Indeterminate_strategy = st.builds(
    express_instances_Indeterminate,
)
express_instances_TypedInstance_strategy = st.builds(
    express_instances_TypedInstance,
)
express_instances_ConcreteValue_strategy = st.builds(
    express_instances_ConcreteValue,
)
express_core_Expression_strategy = st.builds(
    express_core_Expression,
    text=
        safe_text
)
InstantiableType_strategy = st.builds(
    InstantiableType,
)
express_core_ConcreteType_strategy = st.builds(
    express_core_ConcreteType,
)
core_AggregationType_strategy = st.builds(
    core_AggregationType,
)
express_core_ConcreteAggregationType_strategy = st.builds(
    express_core_ConcreteAggregationType,
)
express_algorithms_ActualAggregationType_strategy = st.builds(
    express_algorithms_ActualAggregationType,
)
core_GeneralizedType_strategy = st.builds(
    core_GeneralizedType,
)
express_core_GeneralAggregationType_strategy = st.builds(
    express_core_GeneralAggregationType,
)
core_TypeElement_strategy = st.builds(
    core_TypeElement,
)
express_instances_EnumerationItem_strategy = st.builds(
    express_instances_EnumerationItem,
    position=
        safe_text
)
core_DomainConstraint_strategy = st.builds(
    core_DomainConstraint,
)
express_core_DomainRule_strategy = st.builds(
    express_core_DomainRule,
    position=
        safe_text
)
GeneralAggregationType_strategy = st.builds(
    GeneralAggregationType,
)
express_core_GeneralSETType_strategy = st.builds(
    express_core_GeneralSETType,
)
express_core_GeneralARRAYType_strategy = st.builds(
    express_core_GeneralARRAYType,
    isOptional=
        safe_text
)
express_core_GeneralLISTType_strategy = st.builds(
    express_core_GeneralLISTType,
)
express_core_GeneralBAGType_strategy = st.builds(
    express_core_GeneralBAGType,
)
ActualStructureConstraint_strategy = st.builds(
    ActualStructureConstraint,
)
ParameterType_strategy = st.builds(
    ParameterType,
)
express_core_ArrayBound_strategy = st.builds(
    express_core_ArrayBound,
    bound=
        safe_text
)
core_AttributeType_strategy = st.builds(
    core_AttributeType,
)
express_core_NamedType_strategy = st.builds(
    express_core_NamedType,
)
express_core_GeneralizedType_strategy = st.builds(
    express_core_GeneralizedType,
)
core_DataType_strategy = st.builds(
    core_DataType,
)
express_core_VariableType_strategy = st.builds(
    express_core_VariableType,
)
EnumerationType_strategy = st.builds(
    EnumerationType,
)
express_expressions_VariableRef_strategy = st.builds(
    express_expressions_VariableRef,
    id=
        safe_text
)
NamedType_strategy = st.builds(
    NamedType,
)
express_expressions_ExtentRef_strategy = st.builds(
    express_expressions_ExtentRef,
    id=
        safe_text
)
ListMember_strategy = st.builds(
    ListMember,
)
RepeatCount_strategy = st.builds(
    RepeatCount,
)
express_expressions_MemberBinding_strategy = st.builds(
    express_expressions_MemberBinding,
    position=
        safe_text
)
FunctionResult_strategy = st.builds(
    FunctionResult,
)
Function_strategy = st.builds(
    Function,
)
express_expressions_FunctionCall_strategy = st.builds(
    express_expressions_FunctionCall,
)
SizeConstraint_strategy = st.builds(
    SizeConstraint,
)
GeneralizedType_strategy = st.builds(
    GeneralizedType,
)
express_core_GenericType_strategy = st.builds(
    express_core_GenericType,
    isEntity=
        safe_text
)
express_core_AGGREGATEType_strategy = st.builds(
    express_core_AGGREGATEType,
)
PartialEntityType_strategy = st.builds(
    PartialEntityType,
)
express_core_SingleEntityType_strategy = st.builds(
    express_core_SingleEntityType,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
express_core_SchemaElement_strategy = st.builds(
    express_core_SchemaElement,
)
express_core_LocalElement_strategy = st.builds(
    express_core_LocalElement,
)
express_core_TypeElement_strategy = st.builds(
    express_core_TypeElement,
)
core_Expression_strategy = st.builds(
    core_Expression,
)
express_expressions_QueryExpression_strategy = st.builds(
    express_expressions_QueryExpression,
)
Constant_strategy = st.builds(
    Constant,
)
express_expressions_ConstantRef_strategy = st.builds(
    express_expressions_ConstantRef,
    id=
        safe_text
)
express_expressions_AggregateIndex_strategy = st.builds(
    express_expressions_AggregateIndex,
)
Attribute_strategy = st.builds(
    Attribute,
)
express_core_InverseAttribute_strategy = st.builds(
    express_core_InverseAttribute,
    isUnique=
        safe_text
)
express_core_ExplicitAttribute_strategy = st.builds(
    express_core_ExplicitAttribute,
    isOptional=
        safe_text
)
express_core_DerivedAttribute_strategy = st.builds(
    express_core_DerivedAttribute,
)
Selector_strategy = st.builds(
    Selector,
)
express_expressions_UsedInRef_strategy = st.builds(
    express_expressions_UsedInRef,
)
express_expressions_GroupRef_strategy = st.builds(
    express_expressions_GroupRef,
    id=
        safe_text
)
express_expressions_AttributeRef_strategy = st.builds(
    express_expressions_AttributeRef,
    id=
        safe_text
)
AttributeValue_strategy = st.builds(
    AttributeValue,
)
express_expressions_AttributeBinding_strategy = st.builds(
    express_expressions_AttributeBinding,
    position=
        safe_text
)
express_expressions_Operation_strategy = st.builds(
    express_expressions_Operation,
)
express_expressions_QueryVariable_strategy = st.builds(
    express_expressions_QueryVariable,
)
QueryVariable_strategy = st.builds(
    QueryVariable,
)
express_expressions_Primary_strategy = st.builds(
    express_expressions_Primary,
)
VariableType_strategy = st.builds(
    VariableType,
)
express_core_ActualType_strategy = st.builds(
    express_core_ActualType,
)
AttributeBinding_strategy = st.builds(
    AttributeBinding,
)
PartialEntityValue_strategy = st.builds(
    PartialEntityValue,
)
express_instances_EntityValue_strategy = st.builds(
    express_instances_EntityValue,
)
express_expressions_PartialEntityConstructor_strategy = st.builds(
    express_expressions_PartialEntityConstructor,
    id=
        safe_text
)
express_expressions_StringIndex_strategy = st.builds(
    express_expressions_StringIndex,
)
MemberBinding_strategy = st.builds(
    MemberBinding,
)
GenericAggregate_strategy = st.builds(
    GenericAggregate,
)
express_expressions_AggregateInitializer_strategy = st.builds(
    express_expressions_AggregateInitializer,
)
express_expressions_ParameterRef_strategy = st.builds(
    express_expressions_ParameterRef,
    id=
        safe_text
)
Operation_strategy = st.builds(
    Operation,
)
express_expressions_UnaryOperation_strategy = st.builds(
    express_expressions_UnaryOperation,
    operator=
        safe_text
)
express_expressions_Coercion_strategy = st.builds(
    express_expressions_Coercion,
)
express_expressions_BinaryOperation_strategy = st.builds(
    express_expressions_BinaryOperation,
    operator=
        safe_text
)
Parameter_strategy = st.builds(
    Parameter,
)
express_algorithms_InParameter_strategy = st.builds(
    express_algorithms_InParameter,
)
FunctionCall_strategy = st.builds(
    FunctionCall,
)
ProcedureCall_strategy = st.builds(
    ProcedureCall,
)
express_expressions_IndeterminateRef_strategy = st.builds(
    express_expressions_IndeterminateRef,
)
express_expressions_ActualParameter_strategy = st.builds(
    express_expressions_ActualParameter,
    position=
        safe_text
)

@given(instance=SingleEntityValue_strategy)
@settings(max_examples=50)
def test_singleentityvalue_instantiation(instance):
    assert isinstance(instance, SingleEntityValue)

@given(instance=instances_AggregateValue_strategy)
@settings(max_examples=50)
def test_instances_aggregatevalue_instantiation(instance):
    assert isinstance(instance, instances_AggregateValue)

@given(instance=core_Instance_strategy)
@settings(max_examples=50)
def test_core_instance_instantiation(instance):
    assert isinstance(instance, core_Instance)

@given(instance=express_instances_LISTValue_strategy)
@settings(max_examples=50)
def test_express_instances_listvalue_instantiation(instance):
    assert isinstance(instance, express_instances_LISTValue)

@given(instance=LogicalValue_strategy)
@settings(max_examples=50)
def test_logicalvalue_instantiation(instance):
    assert isinstance(instance, LogicalValue)

@given(instance=express_instances_BooleanValue_strategy)
@settings(max_examples=50)
def test_express_instances_booleanvalue_instantiation(instance):
    assert isinstance(instance, express_instances_BooleanValue)

@given(instance=NumberValue_strategy)
@settings(max_examples=50)
def test_numbervalue_instantiation(instance):
    assert isinstance(instance, NumberValue)

@given(instance=express_instances_RealValue_strategy)
@settings(max_examples=50)
def test_express_instances_realvalue_instantiation(instance):
    assert isinstance(instance, express_instances_RealValue)

@given(instance=express_instances_Population_strategy)
@settings(max_examples=50)
def test_express_instances_population_instantiation(instance):
    assert isinstance(instance, express_instances_Population)

@given(instance=express_instances_ArrayMember_strategy)
@settings(max_examples=50)
def test_express_instances_arraymember_instantiation(instance):
    assert isinstance(instance, express_instances_ArrayMember)



@given(instance=express_instances_ArrayMember_strategy)
def test_express_instances_arraymember_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=instances_ConcreteValue_strategy)
@settings(max_examples=50)
def test_instances_concretevalue_instantiation(instance):
    assert isinstance(instance, instances_ConcreteValue)

@given(instance=instances_TypedInstance_strategy)
@settings(max_examples=50)
def test_instances_typedinstance_instantiation(instance):
    assert isinstance(instance, instances_TypedInstance)

@given(instance=BagMember_strategy)
@settings(max_examples=50)
def test_bagmember_instantiation(instance):
    assert isinstance(instance, BagMember)

@given(instance=LISTValue_strategy)
@settings(max_examples=50)
def test_listvalue_instantiation(instance):
    assert isinstance(instance, LISTValue)

@given(instance=express_instances_GenericAggregate_strategy)
@settings(max_examples=50)
def test_express_instances_genericaggregate_instantiation(instance):
    assert isinstance(instance, express_instances_GenericAggregate)

@given(instance=express_instances_SingleEntityValue_strategy)
@settings(max_examples=50)
def test_express_instances_singleentityvalue_instantiation(instance):
    assert isinstance(instance, express_instances_SingleEntityValue)

@given(instance=express_instances_BagMember_strategy)
@settings(max_examples=50)
def test_express_instances_bagmember_instantiation(instance):
    assert isinstance(instance, express_instances_BagMember)



@given(instance=express_instances_BagMember_strategy)
def test_express_instances_bagmember_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original

@given(instance=express_instances_ListMember_strategy)
@settings(max_examples=50)
def test_express_instances_listmember_instantiation(instance):
    assert isinstance(instance, express_instances_ListMember)



@given(instance=express_instances_ListMember_strategy)
def test_express_instances_listmember_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=EntityValue_strategy)
@settings(max_examples=50)
def test_entityvalue_instantiation(instance):
    assert isinstance(instance, EntityValue)

@given(instance=TypedInstance_strategy)
@settings(max_examples=50)
def test_typedinstance_instantiation(instance):
    assert isinstance(instance, TypedInstance)

@given(instance=express_instances_SpecializedValue_strategy)
@settings(max_examples=50)
def test_express_instances_specializedvalue_instantiation(instance):
    assert isinstance(instance, express_instances_SpecializedValue)

@given(instance=express_instances_EntityInstance_strategy)
@settings(max_examples=50)
def test_express_instances_entityinstance_instantiation(instance):
    assert isinstance(instance, express_instances_EntityInstance)



@given(instance=express_instances_EntityInstance_strategy)
def test_express_instances_entityinstance_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=StringValue_strategy)
@settings(max_examples=50)
def test_stringvalue_instantiation(instance):
    assert isinstance(instance, StringValue)

@given(instance=express_instances_TypeName_strategy)
@settings(max_examples=50)
def test_express_instances_typename_instantiation(instance):
    assert isinstance(instance, express_instances_TypeName)

@given(instance=express_instances_RoleName_strategy)
@settings(max_examples=50)
def test_express_instances_rolename_instantiation(instance):
    assert isinstance(instance, express_instances_RoleName)

@given(instance=ArrayMember_strategy)
@settings(max_examples=50)
def test_arraymember_instantiation(instance):
    assert isinstance(instance, ArrayMember)

@given(instance=AggregateValue_strategy)
@settings(max_examples=50)
def test_aggregatevalue_instantiation(instance):
    assert isinstance(instance, AggregateValue)

@given(instance=express_instances_BAGValue_strategy)
@settings(max_examples=50)
def test_express_instances_bagvalue_instantiation(instance):
    assert isinstance(instance, express_instances_BAGValue)

@given(instance=express_instances_SETValue_strategy)
@settings(max_examples=50)
def test_express_instances_setvalue_instantiation(instance):
    assert isinstance(instance, express_instances_SETValue)

@given(instance=express_instances_ARRAYValue_strategy)
@settings(max_examples=50)
def test_express_instances_arrayvalue_instantiation(instance):
    assert isinstance(instance, express_instances_ARRAYValue)

@given(instance=express_instances_AttributeValue_strategy)
@settings(max_examples=50)
def test_express_instances_attributevalue_instantiation(instance):
    assert isinstance(instance, express_instances_AttributeValue)

@given(instance=core_GenericType_strategy)
@settings(max_examples=50)
def test_core_generictype_instantiation(instance):
    assert isinstance(instance, core_GenericType)

@given(instance=algorithms_Parameter_strategy)
@settings(max_examples=50)
def test_algorithms_parameter_instantiation(instance):
    assert isinstance(instance, algorithms_Parameter)

@given(instance=ConcreteValue_strategy)
@settings(max_examples=50)
def test_concretevalue_instantiation(instance):
    assert isinstance(instance, ConcreteValue)

@given(instance=express_instances_SimpleValue_strategy)
@settings(max_examples=50)
def test_express_instances_simplevalue_instantiation(instance):
    assert isinstance(instance, express_instances_SimpleValue)



@given(instance=express_instances_SimpleValue_strategy)
def test_express_instances_simplevalue_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=express_instances_AggregateValue_strategy)
@settings(max_examples=50)
def test_express_instances_aggregatevalue_instantiation(instance):
    assert isinstance(instance, express_instances_AggregateValue)

@given(instance=RealValue_strategy)
@settings(max_examples=50)
def test_realvalue_instantiation(instance):
    assert isinstance(instance, RealValue)

@given(instance=express_instances_IntegerValue_strategy)
@settings(max_examples=50)
def test_express_instances_integervalue_instantiation(instance):
    assert isinstance(instance, express_instances_IntegerValue)

@given(instance=AGGREGATEType_strategy)
@settings(max_examples=50)
def test_aggregatetype_instantiation(instance):
    assert isinstance(instance, AGGREGATEType)

@given(instance=express_algorithms_ActualStructureConstraint_strategy)
@settings(max_examples=50)
def test_express_algorithms_actualstructureconstraint_instantiation(instance):
    assert isinstance(instance, express_algorithms_ActualStructureConstraint)



@given(instance=express_algorithms_ActualStructureConstraint_strategy)
def test_express_algorithms_actualstructureconstraint_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=ActualStructure_strategy)
@settings(max_examples=50)
def test_actualstructure_instantiation(instance):
    assert isinstance(instance, ActualStructure)

@given(instance=express_algorithms_VARVariable_strategy)
@settings(max_examples=50)
def test_express_algorithms_varvariable_instantiation(instance):
    assert isinstance(instance, express_algorithms_VARVariable)

@given(instance=core_ActualType_strategy)
@settings(max_examples=50)
def test_core_actualtype_instantiation(instance):
    assert isinstance(instance, core_ActualType)

@given(instance=EscapeStatement_strategy)
@settings(max_examples=50)
def test_escapestatement_instantiation(instance):
    assert isinstance(instance, EscapeStatement)

@given(instance=SkipStatement_strategy)
@settings(max_examples=50)
def test_skipstatement_instantiation(instance):
    assert isinstance(instance, SkipStatement)

@given(instance=StatementBlock_strategy)
@settings(max_examples=50)
def test_statementblock_instantiation(instance):
    assert isinstance(instance, StatementBlock)

@given(instance=express_algorithms_Statement_strategy)
@settings(max_examples=50)
def test_express_algorithms_statement_instantiation(instance):
    assert isinstance(instance, express_algorithms_Statement)



@given(instance=express_algorithms_Statement_strategy)
def test_express_algorithms_statement_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=ActualType_strategy)
@settings(max_examples=50)
def test_actualtype_instantiation(instance):
    assert isinstance(instance, ActualType)

@given(instance=express_algorithms_ActualAGGREGATEType_strategy)
@settings(max_examples=50)
def test_express_algorithms_actualaggregatetype_instantiation(instance):
    assert isinstance(instance, express_algorithms_ActualAGGREGATEType)



@given(instance=express_algorithms_ActualAGGREGATEType_strategy)
def test_express_algorithms_actualaggregatetype_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=express_algorithms_ActualGenericType_strategy)
@settings(max_examples=50)
def test_express_algorithms_actualgenerictype_instantiation(instance):
    assert isinstance(instance, express_algorithms_ActualGenericType)



@given(instance=express_algorithms_ActualGenericType_strategy)
def test_express_algorithms_actualgenerictype_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=express_algorithms_ActualGenericType_strategy)
def test_express_algorithms_actualgenerictype_isEntity_setter(instance):
    original = instance.isEntity
    instance.isEntity = original
    assert instance.isEntity == original

@given(instance=core_AGGREGATEType_strategy)
@settings(max_examples=50)
def test_core_aggregatetype_instantiation(instance):
    assert isinstance(instance, core_AGGREGATEType)

@given(instance=algorithms_GenericElement_strategy)
@settings(max_examples=50)
def test_algorithms_genericelement_instantiation(instance):
    assert isinstance(instance, algorithms_GenericElement)

@given(instance=express_algorithms_ActualDataType_strategy)
@settings(max_examples=50)
def test_express_algorithms_actualdatatype_instantiation(instance):
    assert isinstance(instance, express_algorithms_ActualDataType)

@given(instance=express_algorithms_ActualStructure_strategy)
@settings(max_examples=50)
def test_express_algorithms_actualstructure_instantiation(instance):
    assert isinstance(instance, express_algorithms_ActualStructure)

@given(instance=InVariable_strategy)
@settings(max_examples=50)
def test_invariable_instantiation(instance):
    assert isinstance(instance, InVariable)

@given(instance=ActualDataType_strategy)
@settings(max_examples=50)
def test_actualdatatype_instantiation(instance):
    assert isinstance(instance, ActualDataType)

@given(instance=GenericType_strategy)
@settings(max_examples=50)
def test_generictype_instantiation(instance):
    assert isinstance(instance, GenericType)

@given(instance=ActualAggregationType_strategy)
@settings(max_examples=50)
def test_actualaggregationtype_instantiation(instance):
    assert isinstance(instance, ActualAggregationType)

@given(instance=express_algorithms_ActualLISTType_strategy)
@settings(max_examples=50)
def test_express_algorithms_actuallisttype_instantiation(instance):
    assert isinstance(instance, express_algorithms_ActualLISTType)

@given(instance=express_algorithms_ActualBAGType_strategy)
@settings(max_examples=50)
def test_express_algorithms_actualbagtype_instantiation(instance):
    assert isinstance(instance, express_algorithms_ActualBAGType)

@given(instance=express_algorithms_ActualSETType_strategy)
@settings(max_examples=50)
def test_express_algorithms_actualsettype_instantiation(instance):
    assert isinstance(instance, express_algorithms_ActualSETType)

@given(instance=express_algorithms_ActualARRAYType_strategy)
@settings(max_examples=50)
def test_express_algorithms_actualarraytype_instantiation(instance):
    assert isinstance(instance, express_algorithms_ActualARRAYType)



@given(instance=express_algorithms_ActualARRAYType_strategy)
def test_express_algorithms_actualarraytype_isOptional_setter(instance):
    original = instance.isOptional
    instance.isOptional = original
    assert instance.isOptional == original

@given(instance=InParameter_strategy)
@settings(max_examples=50)
def test_inparameter_instantiation(instance):
    assert isinstance(instance, InParameter)

@given(instance=RepeatStatement_strategy)
@settings(max_examples=50)
def test_repeatstatement_instantiation(instance):
    assert isinstance(instance, RepeatStatement)

@given(instance=core_AnonymousType_strategy)
@settings(max_examples=50)
def test_core_anonymoustype_instantiation(instance):
    assert isinstance(instance, core_AnonymousType)

@given(instance=AlgorithmScope_strategy)
@settings(max_examples=50)
def test_algorithmscope_instantiation(instance):
    assert isinstance(instance, AlgorithmScope)

@given(instance=Algorithm_strategy)
@settings(max_examples=50)
def test_algorithm_instantiation(instance):
    assert isinstance(instance, Algorithm)

@given(instance=express_algorithms_Procedure_strategy)
@settings(max_examples=50)
def test_express_algorithms_procedure_instantiation(instance):
    assert isinstance(instance, express_algorithms_Procedure)

@given(instance=express_algorithms_Function_strategy)
@settings(max_examples=50)
def test_express_algorithms_function_instantiation(instance):
    assert isinstance(instance, express_algorithms_Function)

@given(instance=express_algorithms_ActualTypeConstraint_strategy)
@settings(max_examples=50)
def test_express_algorithms_actualtypeconstraint_instantiation(instance):
    assert isinstance(instance, express_algorithms_ActualTypeConstraint)



@given(instance=express_algorithms_ActualTypeConstraint_strategy)
def test_express_algorithms_actualtypeconstraint_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=express_core_AggregationType_strategy)
@settings(max_examples=50)
def test_express_core_aggregationtype_instantiation(instance):
    assert isinstance(instance, express_core_AggregationType)



@given(instance=express_core_AggregationType_strategy)
def test_express_core_aggregationtype_ordering_setter(instance):
    original = instance.ordering
    instance.ordering = original
    assert instance.ordering == original



@given(instance=express_core_AggregationType_strategy)
def test_express_core_aggregationtype_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=express_core_ScopedId_strategy)
@settings(max_examples=50)
def test_express_core_scopedid_instantiation(instance):
    assert isinstance(instance, express_core_ScopedId)



@given(instance=express_core_ScopedId_strategy)
def test_express_core_scopedid_localName_setter(instance):
    original = instance.localName
    instance.localName = original
    assert instance.localName == original

@given(instance=DomainRule_strategy)
@settings(max_examples=50)
def test_domainrule_instantiation(instance):
    assert isinstance(instance, DomainRule)

@given(instance=SelectType_strategy)
@settings(max_examples=50)
def test_selecttype_instantiation(instance):
    assert isinstance(instance, SelectType)

@given(instance=core_CommonElement_strategy)
@settings(max_examples=50)
def test_core_commonelement_instantiation(instance):
    assert isinstance(instance, core_CommonElement)

@given(instance=core_Scope_strategy)
@settings(max_examples=50)
def test_core_scope_instantiation(instance):
    assert isinstance(instance, core_Scope)

@given(instance=express_core_Relationship_strategy)
@settings(max_examples=50)
def test_express_core_relationship_instantiation(instance):
    assert isinstance(instance, express_core_Relationship)

@given(instance=express_core_ParameterType_strategy)
@settings(max_examples=50)
def test_express_core_parametertype_instantiation(instance):
    assert isinstance(instance, express_core_ParameterType)

@given(instance=express_core_Scope_strategy)
@settings(max_examples=50)
def test_express_core_scope_instantiation(instance):
    assert isinstance(instance, express_core_Scope)

@given(instance=express_core_Role_strategy)
@settings(max_examples=50)
def test_express_core_role_instantiation(instance):
    assert isinstance(instance, express_core_Role)

@given(instance=express_core_Remark_strategy)
@settings(max_examples=50)
def test_express_core_remark_instantiation(instance):
    assert isinstance(instance, express_core_Remark)



@given(instance=express_core_Remark_strategy)
def test_express_core_remark_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=express_core_Remark_strategy)
def test_express_core_remark_isTagged_setter(instance):
    original = instance.isTagged
    instance.isTagged = original
    assert instance.isTagged == original



@given(instance=express_core_Remark_strategy)
def test_express_core_remark_isTail_setter(instance):
    original = instance.isTail
    instance.isTail = original
    assert instance.isTail == original

@given(instance=ArrayBound_strategy)
@settings(max_examples=50)
def test_arraybound_instantiation(instance):
    assert isinstance(instance, ArrayBound)

@given(instance=ConcreteType_strategy)
@settings(max_examples=50)
def test_concretetype_instantiation(instance):
    assert isinstance(instance, ConcreteType)

@given(instance=LocalScope_strategy)
@settings(max_examples=50)
def test_localscope_instantiation(instance):
    assert isinstance(instance, LocalScope)

@given(instance=express_core_AlgorithmScope_strategy)
@settings(max_examples=50)
def test_express_core_algorithmscope_instantiation(instance):
    assert isinstance(instance, express_core_AlgorithmScope)

@given(instance=AnonymousType_strategy)
@settings(max_examples=50)
def test_anonymoustype_instantiation(instance):
    assert isinstance(instance, AnonymousType)

@given(instance=express_core_SimpleType_strategy)
@settings(max_examples=50)
def test_express_core_simpletype_instantiation(instance):
    assert isinstance(instance, express_core_SimpleType)



@given(instance=express_core_SimpleType_strategy)
def test_express_core_simpletype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=LengthConstraint_strategy)
@settings(max_examples=50)
def test_lengthconstraint_instantiation(instance):
    assert isinstance(instance, LengthConstraint)

@given(instance=ActualTypeConstraint_strategy)
@settings(max_examples=50)
def test_actualtypeconstraint_instantiation(instance):
    assert isinstance(instance, ActualTypeConstraint)

@given(instance=NumericType_strategy)
@settings(max_examples=50)
def test_numerictype_instantiation(instance):
    assert isinstance(instance, NumericType)

@given(instance=express_core_RealType_strategy)
@settings(max_examples=50)
def test_express_core_realtype_instantiation(instance):
    assert isinstance(instance, express_core_RealType)



@given(instance=express_core_RealType_strategy)
def test_express_core_realtype_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=DomainConstraint_strategy)
@settings(max_examples=50)
def test_domainconstraint_instantiation(instance):
    assert isinstance(instance, DomainConstraint)

@given(instance=express_core_SizeConstraint_strategy)
@settings(max_examples=50)
def test_express_core_sizeconstraint_instantiation(instance):
    assert isinstance(instance, express_core_SizeConstraint)



@given(instance=express_core_SizeConstraint_strategy)
def test_express_core_sizeconstraint_bound_setter(instance):
    original = instance.bound
    instance.bound = original
    assert instance.bound == original

@given(instance=express_core_LengthConstraint_strategy)
@settings(max_examples=50)
def test_express_core_lengthconstraint_instantiation(instance):
    assert isinstance(instance, express_core_LengthConstraint)



@given(instance=express_core_LengthConstraint_strategy)
def test_express_core_lengthconstraint_maxLength_setter(instance):
    original = instance.maxLength
    instance.maxLength = original
    assert instance.maxLength == original



@given(instance=express_core_LengthConstraint_strategy)
def test_express_core_lengthconstraint_isFixed_setter(instance):
    original = instance.isFixed
    instance.isFixed = original
    assert instance.isFixed == original

@given(instance=express_core_AttributeType_strategy)
@settings(max_examples=50)
def test_express_core_attributetype_instantiation(instance):
    assert isinstance(instance, express_core_AttributeType)

@given(instance=express_core_Instance_strategy)
@settings(max_examples=50)
def test_express_core_instance_instantiation(instance):
    assert isinstance(instance, express_core_Instance)

@given(instance=express_core_NamedElement_strategy)
@settings(max_examples=50)
def test_express_core_namedelement_instantiation(instance):
    assert isinstance(instance, express_core_NamedElement)

@given(instance=core_VariableType_strategy)
@settings(max_examples=50)
def test_core_variabletype_instantiation(instance):
    assert isinstance(instance, core_VariableType)

@given(instance=express_core_DomainConstraint_strategy)
@settings(max_examples=50)
def test_express_core_domainconstraint_instantiation(instance):
    assert isinstance(instance, express_core_DomainConstraint)

@given(instance=TypeElement_strategy)
@settings(max_examples=50)
def test_typeelement_instantiation(instance):
    assert isinstance(instance, TypeElement)

@given(instance=express_core_UniqueRule_strategy)
@settings(max_examples=50)
def test_express_core_uniquerule_instantiation(instance):
    assert isinstance(instance, express_core_UniqueRule)



@given(instance=express_core_UniqueRule_strategy)
def test_express_core_uniquerule_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=core_ConcreteType_strategy)
@settings(max_examples=50)
def test_core_concretetype_instantiation(instance):
    assert isinstance(instance, core_ConcreteType)

@given(instance=SimpleType_strategy)
@settings(max_examples=50)
def test_simpletype_instantiation(instance):
    assert isinstance(instance, SimpleType)

@given(instance=express_core_StringType_strategy)
@settings(max_examples=50)
def test_express_core_stringtype_instantiation(instance):
    assert isinstance(instance, express_core_StringType)

@given(instance=express_core_BinaryType_strategy)
@settings(max_examples=50)
def test_express_core_binarytype_instantiation(instance):
    assert isinstance(instance, express_core_BinaryType)

@given(instance=express_core_LogicType_strategy)
@settings(max_examples=50)
def test_express_core_logictype_instantiation(instance):
    assert isinstance(instance, express_core_LogicType)

@given(instance=express_core_NumericType_strategy)
@settings(max_examples=50)
def test_express_core_numerictype_instantiation(instance):
    assert isinstance(instance, express_core_NumericType)

@given(instance=express_core_Attribute_strategy)
@settings(max_examples=50)
def test_express_core_attribute_instantiation(instance):
    assert isinstance(instance, express_core_Attribute)



@given(instance=express_core_Attribute_strategy)
def test_express_core_attribute_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original



@given(instance=express_core_Attribute_strategy)
def test_express_core_attribute_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=Relationship_strategy)
@settings(max_examples=50)
def test_relationship_instantiation(instance):
    assert isinstance(instance, Relationship)

@given(instance=InverseAttribute_strategy)
@settings(max_examples=50)
def test_inverseattribute_instantiation(instance):
    assert isinstance(instance, InverseAttribute)

@given(instance=SchemaElement_strategy)
@settings(max_examples=50)
def test_schemaelement_instantiation(instance):
    assert isinstance(instance, SchemaElement)

@given(instance=express_core_CommonElement_strategy)
@settings(max_examples=50)
def test_express_core_commonelement_instantiation(instance):
    assert isinstance(instance, express_core_CommonElement)

@given(instance=InterfacedElement_strategy)
@settings(max_examples=50)
def test_interfacedelement_instantiation(instance):
    assert isinstance(instance, InterfacedElement)

@given(instance=Remark_strategy)
@settings(max_examples=50)
def test_remark_instantiation(instance):
    assert isinstance(instance, Remark)

@given(instance=express_core_DataType_strategy)
@settings(max_examples=50)
def test_express_core_datatype_instantiation(instance):
    assert isinstance(instance, express_core_DataType)

@given(instance=Schema_strategy)
@settings(max_examples=50)
def test_schema_instantiation(instance):
    assert isinstance(instance, Schema)

@given(instance=express_core_InterfacedElement_strategy)
@settings(max_examples=50)
def test_express_core_interfacedelement_instantiation(instance):
    assert isinstance(instance, express_core_InterfacedElement)



@given(instance=express_core_InterfacedElement_strategy)
def test_express_core_interfacedelement_isUSE_setter(instance):
    original = instance.isUSE
    instance.isUSE = original
    assert instance.isUSE == original

@given(instance=core_ParameterType_strategy)
@settings(max_examples=50)
def test_core_parametertype_instantiation(instance):
    assert isinstance(instance, core_ParameterType)

@given(instance=express_core_InstantiableType_strategy)
@settings(max_examples=50)
def test_express_core_instantiabletype_instantiation(instance):
    assert isinstance(instance, express_core_InstantiableType)

@given(instance=core_InstantiableType_strategy)
@settings(max_examples=50)
def test_core_instantiabletype_instantiation(instance):
    assert isinstance(instance, core_InstantiableType)

@given(instance=express_core_AnonymousType_strategy)
@settings(max_examples=50)
def test_express_core_anonymoustype_instantiation(instance):
    assert isinstance(instance, express_core_AnonymousType)

@given(instance=core_NamedType_strategy)
@settings(max_examples=50)
def test_core_namedtype_instantiation(instance):
    assert isinstance(instance, core_NamedType)

@given(instance=express_core_DefinedType_strategy)
@settings(max_examples=50)
def test_express_core_definedtype_instantiation(instance):
    assert isinstance(instance, express_core_DefinedType)

@given(instance=express_core_EntityType_strategy)
@settings(max_examples=50)
def test_express_core_entitytype_instantiation(instance):
    assert isinstance(instance, express_core_EntityType)



@given(instance=express_core_EntityType_strategy)
def test_express_core_entitytype_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=Role_strategy)
@settings(max_examples=50)
def test_role_instantiation(instance):
    assert isinstance(instance, Role)

@given(instance=express_core_RangeRole_strategy)
@settings(max_examples=50)
def test_express_core_rangerole_instantiation(instance):
    assert isinstance(instance, express_core_RangeRole)

@given(instance=express_core_DomainRole_strategy)
@settings(max_examples=50)
def test_express_core_domainrole_instantiation(instance):
    assert isinstance(instance, express_core_DomainRole)

@given(instance=Redeclaration_strategy)
@settings(max_examples=50)
def test_redeclaration_instantiation(instance):
    assert isinstance(instance, Redeclaration)

@given(instance=AttributeType_strategy)
@settings(max_examples=50)
def test_attributetype_instantiation(instance):
    assert isinstance(instance, AttributeType)

@given(instance=express_core_Redeclaration_strategy)
@settings(max_examples=50)
def test_express_core_redeclaration_instantiation(instance):
    assert isinstance(instance, express_core_Redeclaration)



@given(instance=express_core_Redeclaration_strategy)
def test_express_core_redeclaration_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original



@given(instance=express_core_Redeclaration_strategy)
def test_express_core_redeclaration_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=IndexOperation_strategy)
@settings(max_examples=50)
def test_indexoperation_instantiation(instance):
    assert isinstance(instance, IndexOperation)

@given(instance=express_expressions_BinaryIndex_strategy)
@settings(max_examples=50)
def test_express_expressions_binaryindex_instantiation(instance):
    assert isinstance(instance, express_expressions_BinaryIndex)

@given(instance=SimpleValue_strategy)
@settings(max_examples=50)
def test_simplevalue_instantiation(instance):
    assert isinstance(instance, SimpleValue)

@given(instance=express_instances_NumberValue_strategy)
@settings(max_examples=50)
def test_express_instances_numbervalue_instantiation(instance):
    assert isinstance(instance, express_instances_NumberValue)

@given(instance=express_instances_BinaryValue_strategy)
@settings(max_examples=50)
def test_express_instances_binaryvalue_instantiation(instance):
    assert isinstance(instance, express_instances_BinaryValue)

@given(instance=express_instances_LogicalValue_strategy)
@settings(max_examples=50)
def test_express_instances_logicalvalue_instantiation(instance):
    assert isinstance(instance, express_instances_LogicalValue)

@given(instance=express_instances_StringValue_strategy)
@settings(max_examples=50)
def test_express_instances_stringvalue_instantiation(instance):
    assert isinstance(instance, express_instances_StringValue)

@given(instance=EnumerationItem_strategy)
@settings(max_examples=50)
def test_enumerationitem_instantiation(instance):
    assert isinstance(instance, EnumerationItem)

@given(instance=Primary_strategy)
@settings(max_examples=50)
def test_primary_instantiation(instance):
    assert isinstance(instance, Primary)

@given(instance=express_expressions_Literal_strategy)
@settings(max_examples=50)
def test_express_expressions_literal_instantiation(instance):
    assert isinstance(instance, express_expressions_Literal)

@given(instance=express_expressions_EnumItemRef_strategy)
@settings(max_examples=50)
def test_express_expressions_enumitemref_instantiation(instance):
    assert isinstance(instance, express_expressions_EnumItemRef)



@given(instance=express_expressions_EnumItemRef_strategy)
def test_express_expressions_enumitemref_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=express_expressions_RepeatCount_strategy)
@settings(max_examples=50)
def test_express_expressions_repeatcount_instantiation(instance):
    assert isinstance(instance, express_expressions_RepeatCount)

@given(instance=express_expressions_SELFRef_strategy)
@settings(max_examples=50)
def test_express_expressions_selfref_instantiation(instance):
    assert isinstance(instance, express_expressions_SELFRef)

@given(instance=Indeterminate_strategy)
@settings(max_examples=50)
def test_indeterminate_instantiation(instance):
    assert isinstance(instance, Indeterminate)

@given(instance=CaseAction_strategy)
@settings(max_examples=50)
def test_caseaction_instantiation(instance):
    assert isinstance(instance, CaseAction)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=express_algorithms_FunctionResult_strategy)
@settings(max_examples=50)
def test_express_algorithms_functionresult_instantiation(instance):
    assert isinstance(instance, express_algorithms_FunctionResult)

@given(instance=express_algorithms_InVariable_strategy)
@settings(max_examples=50)
def test_express_algorithms_invariable_instantiation(instance):
    assert isinstance(instance, express_algorithms_InVariable)

@given(instance=express_algorithms_LocalVariable_strategy)
@settings(max_examples=50)
def test_express_algorithms_localvariable_instantiation(instance):
    assert isinstance(instance, express_algorithms_LocalVariable)

@given(instance=SingleEntityType_strategy)
@settings(max_examples=50)
def test_singleentitytype_instantiation(instance):
    assert isinstance(instance, SingleEntityType)

@given(instance=ControlVariable_strategy)
@settings(max_examples=50)
def test_controlvariable_instantiation(instance):
    assert isinstance(instance, ControlVariable)

@given(instance=ExplicitAttribute_strategy)
@settings(max_examples=50)
def test_explicitattribute_instantiation(instance):
    assert isinstance(instance, ExplicitAttribute)

@given(instance=express_core_InvertibleAttribute_strategy)
@settings(max_examples=50)
def test_express_core_invertibleattribute_instantiation(instance):
    assert isinstance(instance, express_core_InvertibleAttribute)

@given(instance=express_statements_VARExpression_strategy)
@settings(max_examples=50)
def test_express_statements_varexpression_instantiation(instance):
    assert isinstance(instance, express_statements_VARExpression)



@given(instance=express_statements_VARExpression_strategy)
def test_express_statements_varexpression_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=VARVariable_strategy)
@settings(max_examples=50)
def test_varvariable_instantiation(instance):
    assert isinstance(instance, VARVariable)

@given(instance=algorithms_VARVariable_strategy)
@settings(max_examples=50)
def test_algorithms_varvariable_instantiation(instance):
    assert isinstance(instance, algorithms_VARVariable)

@given(instance=express_algorithms_VARParameter_strategy)
@settings(max_examples=50)
def test_express_algorithms_varparameter_instantiation(instance):
    assert isinstance(instance, express_algorithms_VARParameter)

@given(instance=algorithms_NamedVariable_strategy)
@settings(max_examples=50)
def test_algorithms_namedvariable_instantiation(instance):
    assert isinstance(instance, algorithms_NamedVariable)

@given(instance=express_statements_AliasVariable_strategy)
@settings(max_examples=50)
def test_express_statements_aliasvariable_instantiation(instance):
    assert isinstance(instance, express_statements_AliasVariable)

@given(instance=NamedVariable_strategy)
@settings(max_examples=50)
def test_namedvariable_instantiation(instance):
    assert isinstance(instance, NamedVariable)

@given(instance=express_algorithms_Variable_strategy)
@settings(max_examples=50)
def test_express_algorithms_variable_instantiation(instance):
    assert isinstance(instance, express_algorithms_Variable)

@given(instance=express_statements_ControlVariable_strategy)
@settings(max_examples=50)
def test_express_statements_controlvariable_instantiation(instance):
    assert isinstance(instance, express_statements_ControlVariable)

@given(instance=AliasVariable_strategy)
@settings(max_examples=50)
def test_aliasvariable_instantiation(instance):
    assert isinstance(instance, AliasVariable)

@given(instance=VARExpression_strategy)
@settings(max_examples=50)
def test_varexpression_instantiation(instance):
    assert isinstance(instance, VARExpression)

@given(instance=express_statements_AttributeCell_strategy)
@settings(max_examples=50)
def test_express_statements_attributecell_instantiation(instance):
    assert isinstance(instance, express_statements_AttributeCell)



@given(instance=express_statements_AttributeCell_strategy)
def test_express_statements_attributecell_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=express_statements_GroupCell_strategy)
@settings(max_examples=50)
def test_express_statements_groupcell_instantiation(instance):
    assert isinstance(instance, express_statements_GroupCell)



@given(instance=express_statements_GroupCell_strategy)
def test_express_statements_groupcell_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=express_statements_MemberCell_strategy)
@settings(max_examples=50)
def test_express_statements_membercell_instantiation(instance):
    assert isinstance(instance, express_statements_MemberCell)

@given(instance=express_statements_VARCell_strategy)
@settings(max_examples=50)
def test_express_statements_varcell_instantiation(instance):
    assert isinstance(instance, express_statements_VARCell)



@given(instance=express_statements_VARCell_strategy)
def test_express_statements_varcell_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=express_statements_VariableCell_strategy)
@settings(max_examples=50)
def test_express_statements_variablecell_instantiation(instance):
    assert isinstance(instance, express_statements_VariableCell)



@given(instance=express_statements_VariableCell_strategy)
def test_express_statements_variablecell_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=core_LocalScope_strategy)
@settings(max_examples=50)
def test_core_localscope_instantiation(instance):
    assert isinstance(instance, core_LocalScope)

@given(instance=algorithms_Statement_strategy)
@settings(max_examples=50)
def test_algorithms_statement_instantiation(instance):
    assert isinstance(instance, algorithms_Statement)

@given(instance=express_statements_RepeatStatement_strategy)
@settings(max_examples=50)
def test_express_statements_repeatstatement_instantiation(instance):
    assert isinstance(instance, express_statements_RepeatStatement)

@given(instance=express_statements_AliasStatement_strategy)
@settings(max_examples=50)
def test_express_statements_aliasstatement_instantiation(instance):
    assert isinstance(instance, express_statements_AliasStatement)

@given(instance=ControlStatement_strategy)
@settings(max_examples=50)
def test_controlstatement_instantiation(instance):
    assert isinstance(instance, ControlStatement)

@given(instance=express_statements_ReturnStatement_strategy)
@settings(max_examples=50)
def test_express_statements_returnstatement_instantiation(instance):
    assert isinstance(instance, express_statements_ReturnStatement)

@given(instance=express_statements_EscapeStatement_strategy)
@settings(max_examples=50)
def test_express_statements_escapestatement_instantiation(instance):
    assert isinstance(instance, express_statements_EscapeStatement)

@given(instance=express_statements_NullStatement_strategy)
@settings(max_examples=50)
def test_express_statements_nullstatement_instantiation(instance):
    assert isinstance(instance, express_statements_NullStatement)

@given(instance=express_statements_SkipStatement_strategy)
@settings(max_examples=50)
def test_express_statements_skipstatement_instantiation(instance):
    assert isinstance(instance, express_statements_SkipStatement)

@given(instance=express_statements_CaseAction_strategy)
@settings(max_examples=50)
def test_express_statements_caseaction_instantiation(instance):
    assert isinstance(instance, express_statements_CaseAction)



@given(instance=express_statements_CaseAction_strategy)
def test_express_statements_caseaction_isDefault_setter(instance):
    original = instance.isDefault
    instance.isDefault = original
    assert instance.isDefault == original

@given(instance=LocalElement_strategy)
@settings(max_examples=50)
def test_localelement_instantiation(instance):
    assert isinstance(instance, LocalElement)

@given(instance=express_algorithms_GenericElement_strategy)
@settings(max_examples=50)
def test_express_algorithms_genericelement_instantiation(instance):
    assert isinstance(instance, express_algorithms_GenericElement)

@given(instance=express_algorithms_NamedVariable_strategy)
@settings(max_examples=50)
def test_express_algorithms_namedvariable_instantiation(instance):
    assert isinstance(instance, express_algorithms_NamedVariable)

@given(instance=express_algorithms_Parameter_strategy)
@settings(max_examples=50)
def test_express_algorithms_parameter_instantiation(instance):
    assert isinstance(instance, express_algorithms_Parameter)



@given(instance=express_algorithms_Parameter_strategy)
def test_express_algorithms_parameter_inout_setter(instance):
    original = instance.inout
    instance.inout = original
    assert instance.inout == original



@given(instance=express_algorithms_Parameter_strategy)
def test_express_algorithms_parameter_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=express_rules_NamedRule_strategy)
@settings(max_examples=50)
def test_express_rules_namedrule_instantiation(instance):
    assert isinstance(instance, express_rules_NamedRule)



@given(instance=express_rules_NamedRule_strategy)
def test_express_rules_namedrule_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=NamedRule_strategy)
@settings(max_examples=50)
def test_namedrule_instantiation(instance):
    assert isinstance(instance, NamedRule)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=express_statements_IfStatement_strategy)
@settings(max_examples=50)
def test_express_statements_ifstatement_instantiation(instance):
    assert isinstance(instance, express_statements_IfStatement)

@given(instance=express_statements_Assignment_strategy)
@settings(max_examples=50)
def test_express_statements_assignment_instantiation(instance):
    assert isinstance(instance, express_statements_Assignment)

@given(instance=express_statements_StatementBlock_strategy)
@settings(max_examples=50)
def test_express_statements_statementblock_instantiation(instance):
    assert isinstance(instance, express_statements_StatementBlock)



@given(instance=express_statements_StatementBlock_strategy)
def test_express_statements_statementblock_delimited_setter(instance):
    original = instance.delimited
    instance.delimited = original
    assert instance.delimited == original

@given(instance=express_statements_CaseStatement_strategy)
@settings(max_examples=50)
def test_express_statements_casestatement_instantiation(instance):
    assert isinstance(instance, express_statements_CaseStatement)

@given(instance=express_statements_ControlStatement_strategy)
@settings(max_examples=50)
def test_express_statements_controlstatement_instantiation(instance):
    assert isinstance(instance, express_statements_ControlStatement)

@given(instance=core_AlgorithmScope_strategy)
@settings(max_examples=50)
def test_core_algorithmscope_instantiation(instance):
    assert isinstance(instance, core_AlgorithmScope)

@given(instance=express_algorithms_Algorithm_strategy)
@settings(max_examples=50)
def test_express_algorithms_algorithm_instantiation(instance):
    assert isinstance(instance, express_algorithms_Algorithm)

@given(instance=core_SchemaElement_strategy)
@settings(max_examples=50)
def test_core_schemaelement_instantiation(instance):
    assert isinstance(instance, core_SchemaElement)

@given(instance=express_rules_GlobalRule_strategy)
@settings(max_examples=50)
def test_express_rules_globalrule_instantiation(instance):
    assert isinstance(instance, express_rules_GlobalRule)

@given(instance=ScopedId_strategy)
@settings(max_examples=50)
def test_scopedid_instantiation(instance):
    assert isinstance(instance, ScopedId)

@given(instance=GlobalRule_strategy)
@settings(max_examples=50)
def test_globalrule_instantiation(instance):
    assert isinstance(instance, GlobalRule)

@given(instance=Population_strategy)
@settings(max_examples=50)
def test_population_instantiation(instance):
    assert isinstance(instance, Population)

@given(instance=EntityInstance_strategy)
@settings(max_examples=50)
def test_entityinstance_instantiation(instance):
    assert isinstance(instance, EntityInstance)

@given(instance=express_instances_SingleLeafInstance_strategy)
@settings(max_examples=50)
def test_express_instances_singleleafinstance_instantiation(instance):
    assert isinstance(instance, express_instances_SingleLeafInstance)

@given(instance=express_instances_MultiLeafInstance_strategy)
@settings(max_examples=50)
def test_express_instances_multileafinstance_instantiation(instance):
    assert isinstance(instance, express_instances_MultiLeafInstance)

@given(instance=SETValue_strategy)
@settings(max_examples=50)
def test_setvalue_instantiation(instance):
    assert isinstance(instance, SETValue)

@given(instance=express_rules_Extent_strategy)
@settings(max_examples=50)
def test_express_rules_extent_instantiation(instance):
    assert isinstance(instance, express_rules_Extent)

@given(instance=SupertypeRule_strategy)
@settings(max_examples=50)
def test_supertyperule_instantiation(instance):
    assert isinstance(instance, SupertypeRule)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=express_expressions_IndexOperation_strategy)
@settings(max_examples=50)
def test_express_expressions_indexoperation_instantiation(instance):
    assert isinstance(instance, express_expressions_IndexOperation)

@given(instance=express_expressions_Selector_strategy)
@settings(max_examples=50)
def test_express_expressions_selector_instantiation(instance):
    assert isinstance(instance, express_expressions_Selector)

@given(instance=Extent_strategy)
@settings(max_examples=50)
def test_extent_instantiation(instance):
    assert isinstance(instance, Extent)

@given(instance=express_rules_SubtypeConstraint_strategy)
@settings(max_examples=50)
def test_express_rules_subtypeconstraint_instantiation(instance):
    assert isinstance(instance, express_rules_SubtypeConstraint)

@given(instance=ActualParameter_strategy)
@settings(max_examples=50)
def test_actualparameter_instantiation(instance):
    assert isinstance(instance, ActualParameter)

@given(instance=Procedure_strategy)
@settings(max_examples=50)
def test_procedure_instantiation(instance):
    assert isinstance(instance, Procedure)

@given(instance=express_statements_ProcedureCall_strategy)
@settings(max_examples=50)
def test_express_statements_procedurecall_instantiation(instance):
    assert isinstance(instance, express_statements_ProcedureCall)

@given(instance=EntityType_strategy)
@settings(max_examples=50)
def test_entitytype_instantiation(instance):
    assert isinstance(instance, EntityType)

@given(instance=CommonElement_strategy)
@settings(max_examples=50)
def test_commonelement_instantiation(instance):
    assert isinstance(instance, CommonElement)

@given(instance=express_instances_Constant_strategy)
@settings(max_examples=50)
def test_express_instances_constant_instantiation(instance):
    assert isinstance(instance, express_instances_Constant)

@given(instance=express_rules_SupertypeRule_strategy)
@settings(max_examples=50)
def test_express_rules_supertyperule_instantiation(instance):
    assert isinstance(instance, express_rules_SupertypeRule)



@given(instance=express_rules_SupertypeRule_strategy)
def test_express_rules_supertyperule_assertsAbstract_setter(instance):
    original = instance.assertsAbstract
    instance.assertsAbstract = original
    assert instance.assertsAbstract == original

@given(instance=SubtypeConstraint_strategy)
@settings(max_examples=50)
def test_subtypeconstraint_instantiation(instance):
    assert isinstance(instance, SubtypeConstraint)

@given(instance=express_rules_ANDConstraint_strategy)
@settings(max_examples=50)
def test_express_rules_andconstraint_instantiation(instance):
    assert isinstance(instance, express_rules_ANDConstraint)

@given(instance=express_rules_TOTAL_OVERConstraint_strategy)
@settings(max_examples=50)
def test_express_rules_total_overconstraint_instantiation(instance):
    assert isinstance(instance, express_rules_TOTAL_OVERConstraint)

@given(instance=express_rules_ONEOFConstraint_strategy)
@settings(max_examples=50)
def test_express_rules_oneofconstraint_instantiation(instance):
    assert isinstance(instance, express_rules_ONEOFConstraint)

@given(instance=ConcreteAggregationType_strategy)
@settings(max_examples=50)
def test_concreteaggregationtype_instantiation(instance):
    assert isinstance(instance, ConcreteAggregationType)

@given(instance=express_core_ARRAYType_strategy)
@settings(max_examples=50)
def test_express_core_arraytype_instantiation(instance):
    assert isinstance(instance, express_core_ARRAYType)



@given(instance=express_core_ARRAYType_strategy)
def test_express_core_arraytype_isOptional_setter(instance):
    original = instance.isOptional
    instance.isOptional = original
    assert instance.isOptional == original

@given(instance=express_core_SETType_strategy)
@settings(max_examples=50)
def test_express_core_settype_instantiation(instance):
    assert isinstance(instance, express_core_SETType)

@given(instance=express_core_BAGType_strategy)
@settings(max_examples=50)
def test_express_core_bagtype_instantiation(instance):
    assert isinstance(instance, express_core_BAGType)

@given(instance=express_core_LISTType_strategy)
@settings(max_examples=50)
def test_express_core_listtype_instantiation(instance):
    assert isinstance(instance, express_core_LISTType)

@given(instance=UniqueRule_strategy)
@settings(max_examples=50)
def test_uniquerule_instantiation(instance):
    assert isinstance(instance, UniqueRule)

@given(instance=RangeRole_strategy)
@settings(max_examples=50)
def test_rangerole_instantiation(instance):
    assert isinstance(instance, RangeRole)

@given(instance=DefinedType_strategy)
@settings(max_examples=50)
def test_definedtype_instantiation(instance):
    assert isinstance(instance, DefinedType)

@given(instance=express_core_SpecializedType_strategy)
@settings(max_examples=50)
def test_express_core_specializedtype_instantiation(instance):
    assert isinstance(instance, express_core_SpecializedType)

@given(instance=express_core_SelectType_strategy)
@settings(max_examples=50)
def test_express_core_selecttype_instantiation(instance):
    assert isinstance(instance, express_core_SelectType)



@given(instance=express_core_SelectType_strategy)
def test_express_core_selecttype_isEntity_setter(instance):
    original = instance.isEntity
    instance.isEntity = original
    assert instance.isEntity == original



@given(instance=express_core_SelectType_strategy)
def test_express_core_selecttype_isExtensible_setter(instance):
    original = instance.isExtensible
    instance.isExtensible = original
    assert instance.isExtensible == original

@given(instance=express_core_EnumerationType_strategy)
@settings(max_examples=50)
def test_express_core_enumerationtype_instantiation(instance):
    assert isinstance(instance, express_core_EnumerationType)



@given(instance=express_core_EnumerationType_strategy)
def test_express_core_enumerationtype_isExtensible_setter(instance):
    original = instance.isExtensible
    instance.isExtensible = original
    assert instance.isExtensible == original

@given(instance=InvertibleAttribute_strategy)
@settings(max_examples=50)
def test_invertibleattribute_instantiation(instance):
    assert isinstance(instance, InvertibleAttribute)

@given(instance=DomainRole_strategy)
@settings(max_examples=50)
def test_domainrole_instantiation(instance):
    assert isinstance(instance, DomainRole)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=express_core_PartialEntityType_strategy)
@settings(max_examples=50)
def test_express_core_partialentitytype_instantiation(instance):
    assert isinstance(instance, express_core_PartialEntityType)

@given(instance=Scope_strategy)
@settings(max_examples=50)
def test_scope_instantiation(instance):
    assert isinstance(instance, Scope)

@given(instance=express_core_LocalScope_strategy)
@settings(max_examples=50)
def test_express_core_localscope_instantiation(instance):
    assert isinstance(instance, express_core_LocalScope)

@given(instance=express_core_Schema_strategy)
@settings(max_examples=50)
def test_express_core_schema_instantiation(instance):
    assert isinstance(instance, express_core_Schema)



@given(instance=express_core_Schema_strategy)
def test_express_core_schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=express_core_Schema_strategy)
def test_express_core_schema_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=Instance_strategy)
@settings(max_examples=50)
def test_instance_instantiation(instance):
    assert isinstance(instance, Instance)

@given(instance=express_instances_PartialEntityValue_strategy)
@settings(max_examples=50)
def test_express_instances_partialentityvalue_instantiation(instance):
    assert isinstance(instance, express_instances_PartialEntityValue)

@given(instance=express_instances_Indeterminate_strategy)
@settings(max_examples=50)
def test_express_instances_indeterminate_instantiation(instance):
    assert isinstance(instance, express_instances_Indeterminate)

@given(instance=express_instances_TypedInstance_strategy)
@settings(max_examples=50)
def test_express_instances_typedinstance_instantiation(instance):
    assert isinstance(instance, express_instances_TypedInstance)

@given(instance=express_instances_ConcreteValue_strategy)
@settings(max_examples=50)
def test_express_instances_concretevalue_instantiation(instance):
    assert isinstance(instance, express_instances_ConcreteValue)

@given(instance=express_core_Expression_strategy)
@settings(max_examples=50)
def test_express_core_expression_instantiation(instance):
    assert isinstance(instance, express_core_Expression)



@given(instance=express_core_Expression_strategy)
def test_express_core_expression_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=InstantiableType_strategy)
@settings(max_examples=50)
def test_instantiabletype_instantiation(instance):
    assert isinstance(instance, InstantiableType)

@given(instance=express_core_ConcreteType_strategy)
@settings(max_examples=50)
def test_express_core_concretetype_instantiation(instance):
    assert isinstance(instance, express_core_ConcreteType)

@given(instance=core_AggregationType_strategy)
@settings(max_examples=50)
def test_core_aggregationtype_instantiation(instance):
    assert isinstance(instance, core_AggregationType)

@given(instance=express_core_ConcreteAggregationType_strategy)
@settings(max_examples=50)
def test_express_core_concreteaggregationtype_instantiation(instance):
    assert isinstance(instance, express_core_ConcreteAggregationType)

@given(instance=express_algorithms_ActualAggregationType_strategy)
@settings(max_examples=50)
def test_express_algorithms_actualaggregationtype_instantiation(instance):
    assert isinstance(instance, express_algorithms_ActualAggregationType)

@given(instance=core_GeneralizedType_strategy)
@settings(max_examples=50)
def test_core_generalizedtype_instantiation(instance):
    assert isinstance(instance, core_GeneralizedType)

@given(instance=express_core_GeneralAggregationType_strategy)
@settings(max_examples=50)
def test_express_core_generalaggregationtype_instantiation(instance):
    assert isinstance(instance, express_core_GeneralAggregationType)

@given(instance=core_TypeElement_strategy)
@settings(max_examples=50)
def test_core_typeelement_instantiation(instance):
    assert isinstance(instance, core_TypeElement)

@given(instance=express_instances_EnumerationItem_strategy)
@settings(max_examples=50)
def test_express_instances_enumerationitem_instantiation(instance):
    assert isinstance(instance, express_instances_EnumerationItem)



@given(instance=express_instances_EnumerationItem_strategy)
def test_express_instances_enumerationitem_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=core_DomainConstraint_strategy)
@settings(max_examples=50)
def test_core_domainconstraint_instantiation(instance):
    assert isinstance(instance, core_DomainConstraint)

@given(instance=express_core_DomainRule_strategy)
@settings(max_examples=50)
def test_express_core_domainrule_instantiation(instance):
    assert isinstance(instance, express_core_DomainRule)



@given(instance=express_core_DomainRule_strategy)
def test_express_core_domainrule_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=GeneralAggregationType_strategy)
@settings(max_examples=50)
def test_generalaggregationtype_instantiation(instance):
    assert isinstance(instance, GeneralAggregationType)

@given(instance=express_core_GeneralSETType_strategy)
@settings(max_examples=50)
def test_express_core_generalsettype_instantiation(instance):
    assert isinstance(instance, express_core_GeneralSETType)

@given(instance=express_core_GeneralARRAYType_strategy)
@settings(max_examples=50)
def test_express_core_generalarraytype_instantiation(instance):
    assert isinstance(instance, express_core_GeneralARRAYType)



@given(instance=express_core_GeneralARRAYType_strategy)
def test_express_core_generalarraytype_isOptional_setter(instance):
    original = instance.isOptional
    instance.isOptional = original
    assert instance.isOptional == original

@given(instance=express_core_GeneralLISTType_strategy)
@settings(max_examples=50)
def test_express_core_generallisttype_instantiation(instance):
    assert isinstance(instance, express_core_GeneralLISTType)

@given(instance=express_core_GeneralBAGType_strategy)
@settings(max_examples=50)
def test_express_core_generalbagtype_instantiation(instance):
    assert isinstance(instance, express_core_GeneralBAGType)

@given(instance=ActualStructureConstraint_strategy)
@settings(max_examples=50)
def test_actualstructureconstraint_instantiation(instance):
    assert isinstance(instance, ActualStructureConstraint)

@given(instance=ParameterType_strategy)
@settings(max_examples=50)
def test_parametertype_instantiation(instance):
    assert isinstance(instance, ParameterType)

@given(instance=express_core_ArrayBound_strategy)
@settings(max_examples=50)
def test_express_core_arraybound_instantiation(instance):
    assert isinstance(instance, express_core_ArrayBound)



@given(instance=express_core_ArrayBound_strategy)
def test_express_core_arraybound_bound_setter(instance):
    original = instance.bound
    instance.bound = original
    assert instance.bound == original

@given(instance=core_AttributeType_strategy)
@settings(max_examples=50)
def test_core_attributetype_instantiation(instance):
    assert isinstance(instance, core_AttributeType)

@given(instance=express_core_NamedType_strategy)
@settings(max_examples=50)
def test_express_core_namedtype_instantiation(instance):
    assert isinstance(instance, express_core_NamedType)

@given(instance=express_core_GeneralizedType_strategy)
@settings(max_examples=50)
def test_express_core_generalizedtype_instantiation(instance):
    assert isinstance(instance, express_core_GeneralizedType)

@given(instance=core_DataType_strategy)
@settings(max_examples=50)
def test_core_datatype_instantiation(instance):
    assert isinstance(instance, core_DataType)

@given(instance=express_core_VariableType_strategy)
@settings(max_examples=50)
def test_express_core_variabletype_instantiation(instance):
    assert isinstance(instance, express_core_VariableType)

@given(instance=EnumerationType_strategy)
@settings(max_examples=50)
def test_enumerationtype_instantiation(instance):
    assert isinstance(instance, EnumerationType)

@given(instance=express_expressions_VariableRef_strategy)
@settings(max_examples=50)
def test_express_expressions_variableref_instantiation(instance):
    assert isinstance(instance, express_expressions_VariableRef)



@given(instance=express_expressions_VariableRef_strategy)
def test_express_expressions_variableref_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=NamedType_strategy)
@settings(max_examples=50)
def test_namedtype_instantiation(instance):
    assert isinstance(instance, NamedType)

@given(instance=express_expressions_ExtentRef_strategy)
@settings(max_examples=50)
def test_express_expressions_extentref_instantiation(instance):
    assert isinstance(instance, express_expressions_ExtentRef)



@given(instance=express_expressions_ExtentRef_strategy)
def test_express_expressions_extentref_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=ListMember_strategy)
@settings(max_examples=50)
def test_listmember_instantiation(instance):
    assert isinstance(instance, ListMember)

@given(instance=RepeatCount_strategy)
@settings(max_examples=50)
def test_repeatcount_instantiation(instance):
    assert isinstance(instance, RepeatCount)

@given(instance=express_expressions_MemberBinding_strategy)
@settings(max_examples=50)
def test_express_expressions_memberbinding_instantiation(instance):
    assert isinstance(instance, express_expressions_MemberBinding)



@given(instance=express_expressions_MemberBinding_strategy)
def test_express_expressions_memberbinding_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=FunctionResult_strategy)
@settings(max_examples=50)
def test_functionresult_instantiation(instance):
    assert isinstance(instance, FunctionResult)

@given(instance=Function_strategy)
@settings(max_examples=50)
def test_function_instantiation(instance):
    assert isinstance(instance, Function)

@given(instance=express_expressions_FunctionCall_strategy)
@settings(max_examples=50)
def test_express_expressions_functioncall_instantiation(instance):
    assert isinstance(instance, express_expressions_FunctionCall)

@given(instance=SizeConstraint_strategy)
@settings(max_examples=50)
def test_sizeconstraint_instantiation(instance):
    assert isinstance(instance, SizeConstraint)

@given(instance=GeneralizedType_strategy)
@settings(max_examples=50)
def test_generalizedtype_instantiation(instance):
    assert isinstance(instance, GeneralizedType)

@given(instance=express_core_GenericType_strategy)
@settings(max_examples=50)
def test_express_core_generictype_instantiation(instance):
    assert isinstance(instance, express_core_GenericType)



@given(instance=express_core_GenericType_strategy)
def test_express_core_generictype_isEntity_setter(instance):
    original = instance.isEntity
    instance.isEntity = original
    assert instance.isEntity == original

@given(instance=express_core_AGGREGATEType_strategy)
@settings(max_examples=50)
def test_express_core_aggregatetype_instantiation(instance):
    assert isinstance(instance, express_core_AGGREGATEType)

@given(instance=PartialEntityType_strategy)
@settings(max_examples=50)
def test_partialentitytype_instantiation(instance):
    assert isinstance(instance, PartialEntityType)

@given(instance=express_core_SingleEntityType_strategy)
@settings(max_examples=50)
def test_express_core_singleentitytype_instantiation(instance):
    assert isinstance(instance, express_core_SingleEntityType)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=express_core_SchemaElement_strategy)
@settings(max_examples=50)
def test_express_core_schemaelement_instantiation(instance):
    assert isinstance(instance, express_core_SchemaElement)

@given(instance=express_core_LocalElement_strategy)
@settings(max_examples=50)
def test_express_core_localelement_instantiation(instance):
    assert isinstance(instance, express_core_LocalElement)

@given(instance=express_core_TypeElement_strategy)
@settings(max_examples=50)
def test_express_core_typeelement_instantiation(instance):
    assert isinstance(instance, express_core_TypeElement)

@given(instance=core_Expression_strategy)
@settings(max_examples=50)
def test_core_expression_instantiation(instance):
    assert isinstance(instance, core_Expression)

@given(instance=express_expressions_QueryExpression_strategy)
@settings(max_examples=50)
def test_express_expressions_queryexpression_instantiation(instance):
    assert isinstance(instance, express_expressions_QueryExpression)

@given(instance=Constant_strategy)
@settings(max_examples=50)
def test_constant_instantiation(instance):
    assert isinstance(instance, Constant)

@given(instance=express_expressions_ConstantRef_strategy)
@settings(max_examples=50)
def test_express_expressions_constantref_instantiation(instance):
    assert isinstance(instance, express_expressions_ConstantRef)



@given(instance=express_expressions_ConstantRef_strategy)
def test_express_expressions_constantref_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=express_expressions_AggregateIndex_strategy)
@settings(max_examples=50)
def test_express_expressions_aggregateindex_instantiation(instance):
    assert isinstance(instance, express_expressions_AggregateIndex)

@given(instance=Attribute_strategy)
@settings(max_examples=50)
def test_attribute_instantiation(instance):
    assert isinstance(instance, Attribute)

@given(instance=express_core_InverseAttribute_strategy)
@settings(max_examples=50)
def test_express_core_inverseattribute_instantiation(instance):
    assert isinstance(instance, express_core_InverseAttribute)



@given(instance=express_core_InverseAttribute_strategy)
def test_express_core_inverseattribute_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=express_core_ExplicitAttribute_strategy)
@settings(max_examples=50)
def test_express_core_explicitattribute_instantiation(instance):
    assert isinstance(instance, express_core_ExplicitAttribute)



@given(instance=express_core_ExplicitAttribute_strategy)
def test_express_core_explicitattribute_isOptional_setter(instance):
    original = instance.isOptional
    instance.isOptional = original
    assert instance.isOptional == original

@given(instance=express_core_DerivedAttribute_strategy)
@settings(max_examples=50)
def test_express_core_derivedattribute_instantiation(instance):
    assert isinstance(instance, express_core_DerivedAttribute)

@given(instance=Selector_strategy)
@settings(max_examples=50)
def test_selector_instantiation(instance):
    assert isinstance(instance, Selector)

@given(instance=express_expressions_UsedInRef_strategy)
@settings(max_examples=50)
def test_express_expressions_usedinref_instantiation(instance):
    assert isinstance(instance, express_expressions_UsedInRef)

@given(instance=express_expressions_GroupRef_strategy)
@settings(max_examples=50)
def test_express_expressions_groupref_instantiation(instance):
    assert isinstance(instance, express_expressions_GroupRef)



@given(instance=express_expressions_GroupRef_strategy)
def test_express_expressions_groupref_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=express_expressions_AttributeRef_strategy)
@settings(max_examples=50)
def test_express_expressions_attributeref_instantiation(instance):
    assert isinstance(instance, express_expressions_AttributeRef)



@given(instance=express_expressions_AttributeRef_strategy)
def test_express_expressions_attributeref_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=AttributeValue_strategy)
@settings(max_examples=50)
def test_attributevalue_instantiation(instance):
    assert isinstance(instance, AttributeValue)

@given(instance=express_expressions_AttributeBinding_strategy)
@settings(max_examples=50)
def test_express_expressions_attributebinding_instantiation(instance):
    assert isinstance(instance, express_expressions_AttributeBinding)



@given(instance=express_expressions_AttributeBinding_strategy)
def test_express_expressions_attributebinding_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=express_expressions_Operation_strategy)
@settings(max_examples=50)
def test_express_expressions_operation_instantiation(instance):
    assert isinstance(instance, express_expressions_Operation)

@given(instance=express_expressions_QueryVariable_strategy)
@settings(max_examples=50)
def test_express_expressions_queryvariable_instantiation(instance):
    assert isinstance(instance, express_expressions_QueryVariable)

@given(instance=QueryVariable_strategy)
@settings(max_examples=50)
def test_queryvariable_instantiation(instance):
    assert isinstance(instance, QueryVariable)

@given(instance=express_expressions_Primary_strategy)
@settings(max_examples=50)
def test_express_expressions_primary_instantiation(instance):
    assert isinstance(instance, express_expressions_Primary)

@given(instance=VariableType_strategy)
@settings(max_examples=50)
def test_variabletype_instantiation(instance):
    assert isinstance(instance, VariableType)

@given(instance=express_core_ActualType_strategy)
@settings(max_examples=50)
def test_express_core_actualtype_instantiation(instance):
    assert isinstance(instance, express_core_ActualType)

@given(instance=AttributeBinding_strategy)
@settings(max_examples=50)
def test_attributebinding_instantiation(instance):
    assert isinstance(instance, AttributeBinding)

@given(instance=PartialEntityValue_strategy)
@settings(max_examples=50)
def test_partialentityvalue_instantiation(instance):
    assert isinstance(instance, PartialEntityValue)

@given(instance=express_instances_EntityValue_strategy)
@settings(max_examples=50)
def test_express_instances_entityvalue_instantiation(instance):
    assert isinstance(instance, express_instances_EntityValue)

@given(instance=express_expressions_PartialEntityConstructor_strategy)
@settings(max_examples=50)
def test_express_expressions_partialentityconstructor_instantiation(instance):
    assert isinstance(instance, express_expressions_PartialEntityConstructor)



@given(instance=express_expressions_PartialEntityConstructor_strategy)
def test_express_expressions_partialentityconstructor_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=express_expressions_StringIndex_strategy)
@settings(max_examples=50)
def test_express_expressions_stringindex_instantiation(instance):
    assert isinstance(instance, express_expressions_StringIndex)

@given(instance=MemberBinding_strategy)
@settings(max_examples=50)
def test_memberbinding_instantiation(instance):
    assert isinstance(instance, MemberBinding)

@given(instance=GenericAggregate_strategy)
@settings(max_examples=50)
def test_genericaggregate_instantiation(instance):
    assert isinstance(instance, GenericAggregate)

@given(instance=express_expressions_AggregateInitializer_strategy)
@settings(max_examples=50)
def test_express_expressions_aggregateinitializer_instantiation(instance):
    assert isinstance(instance, express_expressions_AggregateInitializer)

@given(instance=express_expressions_ParameterRef_strategy)
@settings(max_examples=50)
def test_express_expressions_parameterref_instantiation(instance):
    assert isinstance(instance, express_expressions_ParameterRef)



@given(instance=express_expressions_ParameterRef_strategy)
def test_express_expressions_parameterref_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=express_expressions_UnaryOperation_strategy)
@settings(max_examples=50)
def test_express_expressions_unaryoperation_instantiation(instance):
    assert isinstance(instance, express_expressions_UnaryOperation)



@given(instance=express_expressions_UnaryOperation_strategy)
def test_express_expressions_unaryoperation_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=express_expressions_Coercion_strategy)
@settings(max_examples=50)
def test_express_expressions_coercion_instantiation(instance):
    assert isinstance(instance, express_expressions_Coercion)

@given(instance=express_expressions_BinaryOperation_strategy)
@settings(max_examples=50)
def test_express_expressions_binaryoperation_instantiation(instance):
    assert isinstance(instance, express_expressions_BinaryOperation)



@given(instance=express_expressions_BinaryOperation_strategy)
def test_express_expressions_binaryoperation_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=express_algorithms_InParameter_strategy)
@settings(max_examples=50)
def test_express_algorithms_inparameter_instantiation(instance):
    assert isinstance(instance, express_algorithms_InParameter)

@given(instance=FunctionCall_strategy)
@settings(max_examples=50)
def test_functioncall_instantiation(instance):
    assert isinstance(instance, FunctionCall)

@given(instance=ProcedureCall_strategy)
@settings(max_examples=50)
def test_procedurecall_instantiation(instance):
    assert isinstance(instance, ProcedureCall)

@given(instance=express_expressions_IndeterminateRef_strategy)
@settings(max_examples=50)
def test_express_expressions_indeterminateref_instantiation(instance):
    assert isinstance(instance, express_expressions_IndeterminateRef)

@given(instance=express_expressions_ActualParameter_strategy)
@settings(max_examples=50)
def test_express_expressions_actualparameter_instantiation(instance):
    assert isinstance(instance, express_expressions_ActualParameter)



@given(instance=express_expressions_ActualParameter_strategy)
def test_express_expressions_actualparameter_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original
