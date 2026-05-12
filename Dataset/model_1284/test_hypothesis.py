import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    morel_PrimitiveConstraint,
    AdditionalConstraint,
    morel_AllDifferentConstraint,
    morel_OrderConstraint,
    morel_Executable,
    morel_EAttribute,
    PrimitiveConstraint,
    morel_ValueRangeConstraint,
    morel_MultiValueConstraint,
    RuleElement,
    morel_RuleGroup,
    morel_Rule,
    Statement,
    morel_DeclarativeStatement,
    CollectionType,
    morel_SequenceType,
    morel_SetType,
    morel_BagType,
    morel_OrderedSetType,
    EDataType,
    morel_CollectionType,
    morel_ImperativeStatement,
    ImperativeStatement,
    morel_BlockStatement,
    morel_ForStatement,
    morel_IfStatement,
    BooleanAndExpChild,
    morel_RelationalExpChild,
    morel_RelationalExp,
    BooleanOrExpChild,
    morel_BooleanAndExpChild,
    morel_BooleanAndExp,
    BooleanImpliesExpChild,
    morel_BooleanOrExpChild,
    morel_BooleanOrExp,
    MultiplicativeExpChild,
    morel_UnaryExpChild,
    morel_UnaryExp,
    AdditiveExpChild,
    morel_MultiplicativeExpChild,
    morel_MultiplicativeExp,
    RelationalExpChild,
    morel_AdditiveExpChild,
    morel_AdditiveExp,
    ImperativeExp,
    morel_BindExp,
    morel_PredefinedBindExp,
    Expression,
    morel_ImperativeExp,
    morel_BooleanImpliesExpChild,
    morel_ReflectiveVariableExp,
    morel_LetExp,
    LoopPathExp,
    morel_IteratorPathExp,
    morel_BooleanImpliesExp,
    morel_ConditionExp,
    PrimitiveVariable,
    VariableWithInit,
    morel_PrimitiveVariableWithInit,
    ObjectVariable,
    morel_ObjectVariableWithInit,
    morel_EClassifier,
    morel_EEnumLiteral,
    morel_EEnum,
    CallPathExp,
    morel_LoopPathExp,
    morel_OperationPathExp,
    morel_FeaturePathExp,
    morel_Unit,
    Executable,
    Pattern,
    morel_EPackage,
    Unit,
    morel_QueryModel,
    LiteralExp,
    morel_RealLiteralExp,
    morel_UndefinedLiteralExp,
    morel_CollectionLiteralExp,
    morel_BooleanLiteralExp,
    morel_IntegerLiteralExp,
    morel_ArrayLiteralExp,
    morel_EnumLiteralExp,
    morel_TypeLiteralExp,
    morel_StringLiteralExp,
    AtomicExp,
    morel_VariableExp,
    morel_PredefinedVariableExp,
    morel_NestedExp,
    morel_LiteralExp,
    morel_CallPathExp,
    UnaryExpChild,
    morel_AtomicExp,
    morel_EDataType,
    morel_EClass,
    Variable,
    morel_PrimitiveVariable,
    morel_VariableWithInit,
    NamedElement,
    morel_RuleElement,
    morel_TypedModel,
    morel_TransformationModel,
    morel_Query,
    morel_Variable,
    morel_AdditionalConstraint,
    morel_Statement,
    morel_EReference,
    morel_Expression,
    LinkConstraint,
    morel_EnclosureLinkConstraint,
    morel_PathConstraint,
    morel_SimpleLinkConstraint,
    morel_LinkConstraint,
    morel_ObjectVariable,
    Section,
    morel_Clause,
    morel_Pattern,
    morel_Section,
    morel_NamedElement,
    SectionType,
    IterationType,
    IteratorType,
    RepetitionType,
    AdditiveOperator,
    RelationalOperator,
    UndefinedLiteral,
    BooleanOperator,
    ScopeType,
    MultiplicativeOperator,
    UnaryOperator,
    OrderType,
    TypedModelAction,
    PredefinedVariable,
    OperationSeparator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_morel_primitiveconstraint_is_not_abstract():
    assert not inspect.isabstract(morel_PrimitiveConstraint)


def test_morel_primitiveconstraint_constructor_exists():
    assert callable(morel_PrimitiveConstraint.__init__)


def test_morel_primitiveconstraint_constructor_args():
    sig = inspect.signature(morel_PrimitiveConstraint.__init__)
    params = list(sig.parameters.keys())



def test_additionalconstraint_is_not_abstract():
    assert not inspect.isabstract(AdditionalConstraint)


def test_additionalconstraint_constructor_exists():
    assert callable(AdditionalConstraint.__init__)


def test_additionalconstraint_constructor_args():
    sig = inspect.signature(AdditionalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_morel_alldifferentconstraint_is_not_abstract():
    assert not inspect.isabstract(morel_AllDifferentConstraint)


def test_morel_alldifferentconstraint_constructor_exists():
    assert callable(morel_AllDifferentConstraint.__init__)


def test_morel_alldifferentconstraint_constructor_args():
    sig = inspect.signature(morel_AllDifferentConstraint.__init__)
    params = list(sig.parameters.keys())



def test_morel_orderconstraint_is_not_abstract():
    assert not inspect.isabstract(morel_OrderConstraint)


def test_morel_orderconstraint_constructor_exists():
    assert callable(morel_OrderConstraint.__init__)


def test_morel_orderconstraint_constructor_args():
    sig = inspect.signature(morel_OrderConstraint.__init__)
    params = list(sig.parameters.keys())



def test_morel_executable_is_not_abstract():
    assert not inspect.isabstract(morel_Executable)


def test_morel_executable_constructor_exists():
    assert callable(morel_Executable.__init__)


def test_morel_executable_constructor_args():
    sig = inspect.signature(morel_Executable.__init__)
    params = list(sig.parameters.keys())
    assert "parameters" in params, "Missing parameter 'parameters'"
    assert "active" in params, "Missing parameter 'active'"

def test_morel_executable_has_parameters():
    assert hasattr(morel_Executable, "parameters")
    descriptor = None
    for klass in morel_Executable.__mro__:
        if "parameters" in klass.__dict__:
            descriptor = klass.__dict__["parameters"]
            break
    assert isinstance(descriptor, property)

def test_morel_executable_has_active():
    assert hasattr(morel_Executable, "active")
    descriptor = None
    for klass in morel_Executable.__mro__:
        if "active" in klass.__dict__:
            descriptor = klass.__dict__["active"]
            break
    assert isinstance(descriptor, property)



def test_morel_eattribute_is_not_abstract():
    assert not inspect.isabstract(morel_EAttribute)


def test_morel_eattribute_constructor_exists():
    assert callable(morel_EAttribute.__init__)


def test_morel_eattribute_constructor_args():
    sig = inspect.signature(morel_EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_primitiveconstraint_is_not_abstract():
    assert not inspect.isabstract(PrimitiveConstraint)


def test_primitiveconstraint_constructor_exists():
    assert callable(PrimitiveConstraint.__init__)


def test_primitiveconstraint_constructor_args():
    sig = inspect.signature(PrimitiveConstraint.__init__)
    params = list(sig.parameters.keys())



def test_morel_valuerangeconstraint_is_not_abstract():
    assert not inspect.isabstract(morel_ValueRangeConstraint)


def test_morel_valuerangeconstraint_constructor_exists():
    assert callable(morel_ValueRangeConstraint.__init__)


def test_morel_valuerangeconstraint_constructor_args():
    sig = inspect.signature(morel_ValueRangeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_morel_multivalueconstraint_is_not_abstract():
    assert not inspect.isabstract(morel_MultiValueConstraint)


def test_morel_multivalueconstraint_constructor_exists():
    assert callable(morel_MultiValueConstraint.__init__)


def test_morel_multivalueconstraint_constructor_args():
    sig = inspect.signature(morel_MultiValueConstraint.__init__)
    params = list(sig.parameters.keys())



def test_ruleelement_is_not_abstract():
    assert not inspect.isabstract(RuleElement)


def test_ruleelement_constructor_exists():
    assert callable(RuleElement.__init__)


def test_ruleelement_constructor_args():
    sig = inspect.signature(RuleElement.__init__)
    params = list(sig.parameters.keys())



def test_morel_rulegroup_is_not_abstract():
    assert not inspect.isabstract(morel_RuleGroup)


def test_morel_rulegroup_constructor_exists():
    assert callable(morel_RuleGroup.__init__)


def test_morel_rulegroup_constructor_args():
    sig = inspect.signature(morel_RuleGroup.__init__)
    params = list(sig.parameters.keys())
    assert "iteration" in params, "Missing parameter 'iteration'"
    assert "maxIteration" in params, "Missing parameter 'maxIteration'"
    assert "order" in params, "Missing parameter 'order'"
    assert "repetition" in params, "Missing parameter 'repetition'"
    assert "scopeSize" in params, "Missing parameter 'scopeSize'"
    assert "scope" in params, "Missing parameter 'scope'"

def test_morel_rulegroup_has_iteration():
    assert hasattr(morel_RuleGroup, "iteration")
    descriptor = None
    for klass in morel_RuleGroup.__mro__:
        if "iteration" in klass.__dict__:
            descriptor = klass.__dict__["iteration"]
            break
    assert isinstance(descriptor, property)

def test_morel_rulegroup_has_maxIteration():
    assert hasattr(morel_RuleGroup, "maxIteration")
    descriptor = None
    for klass in morel_RuleGroup.__mro__:
        if "maxIteration" in klass.__dict__:
            descriptor = klass.__dict__["maxIteration"]
            break
    assert isinstance(descriptor, property)

def test_morel_rulegroup_has_order():
    assert hasattr(morel_RuleGroup, "order")
    descriptor = None
    for klass in morel_RuleGroup.__mro__:
        if "order" in klass.__dict__:
            descriptor = klass.__dict__["order"]
            break
    assert isinstance(descriptor, property)

def test_morel_rulegroup_has_repetition():
    assert hasattr(morel_RuleGroup, "repetition")
    descriptor = None
    for klass in morel_RuleGroup.__mro__:
        if "repetition" in klass.__dict__:
            descriptor = klass.__dict__["repetition"]
            break
    assert isinstance(descriptor, property)

def test_morel_rulegroup_has_scopeSize():
    assert hasattr(morel_RuleGroup, "scopeSize")
    descriptor = None
    for klass in morel_RuleGroup.__mro__:
        if "scopeSize" in klass.__dict__:
            descriptor = klass.__dict__["scopeSize"]
            break
    assert isinstance(descriptor, property)

def test_morel_rulegroup_has_scope():
    assert hasattr(morel_RuleGroup, "scope")
    descriptor = None
    for klass in morel_RuleGroup.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)



def test_morel_rule_is_not_abstract():
    assert not inspect.isabstract(morel_Rule)


def test_morel_rule_constructor_exists():
    assert callable(morel_Rule.__init__)


def test_morel_rule_constructor_args():
    sig = inspect.signature(morel_Rule.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_morel_declarativestatement_is_not_abstract():
    assert not inspect.isabstract(morel_DeclarativeStatement)


def test_morel_declarativestatement_constructor_exists():
    assert callable(morel_DeclarativeStatement.__init__)


def test_morel_declarativestatement_constructor_args():
    sig = inspect.signature(morel_DeclarativeStatement.__init__)
    params = list(sig.parameters.keys())



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_morel_sequencetype_is_not_abstract():
    assert not inspect.isabstract(morel_SequenceType)


def test_morel_sequencetype_constructor_exists():
    assert callable(morel_SequenceType.__init__)


def test_morel_sequencetype_constructor_args():
    sig = inspect.signature(morel_SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_morel_settype_is_not_abstract():
    assert not inspect.isabstract(morel_SetType)


def test_morel_settype_constructor_exists():
    assert callable(morel_SetType.__init__)


def test_morel_settype_constructor_args():
    sig = inspect.signature(morel_SetType.__init__)
    params = list(sig.parameters.keys())



def test_morel_bagtype_is_not_abstract():
    assert not inspect.isabstract(morel_BagType)


def test_morel_bagtype_constructor_exists():
    assert callable(morel_BagType.__init__)


def test_morel_bagtype_constructor_args():
    sig = inspect.signature(morel_BagType.__init__)
    params = list(sig.parameters.keys())



def test_morel_orderedsettype_is_not_abstract():
    assert not inspect.isabstract(morel_OrderedSetType)


def test_morel_orderedsettype_constructor_exists():
    assert callable(morel_OrderedSetType.__init__)


def test_morel_orderedsettype_constructor_args():
    sig = inspect.signature(morel_OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_edatatype_is_not_abstract():
    assert not inspect.isabstract(EDataType)


def test_edatatype_constructor_exists():
    assert callable(EDataType.__init__)


def test_edatatype_constructor_args():
    sig = inspect.signature(EDataType.__init__)
    params = list(sig.parameters.keys())



def test_morel_collectiontype_is_not_abstract():
    assert not inspect.isabstract(morel_CollectionType)


def test_morel_collectiontype_constructor_exists():
    assert callable(morel_CollectionType.__init__)


def test_morel_collectiontype_constructor_args():
    sig = inspect.signature(morel_CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_morel_imperativestatement_is_not_abstract():
    assert not inspect.isabstract(morel_ImperativeStatement)


def test_morel_imperativestatement_constructor_exists():
    assert callable(morel_ImperativeStatement.__init__)


def test_morel_imperativestatement_constructor_args():
    sig = inspect.signature(morel_ImperativeStatement.__init__)
    params = list(sig.parameters.keys())



def test_imperativestatement_is_not_abstract():
    assert not inspect.isabstract(ImperativeStatement)


def test_imperativestatement_constructor_exists():
    assert callable(ImperativeStatement.__init__)


def test_imperativestatement_constructor_args():
    sig = inspect.signature(ImperativeStatement.__init__)
    params = list(sig.parameters.keys())



def test_morel_blockstatement_is_not_abstract():
    assert not inspect.isabstract(morel_BlockStatement)


def test_morel_blockstatement_constructor_exists():
    assert callable(morel_BlockStatement.__init__)


def test_morel_blockstatement_constructor_args():
    sig = inspect.signature(morel_BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_morel_forstatement_is_not_abstract():
    assert not inspect.isabstract(morel_ForStatement)


def test_morel_forstatement_constructor_exists():
    assert callable(morel_ForStatement.__init__)


def test_morel_forstatement_constructor_args():
    sig = inspect.signature(morel_ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_morel_ifstatement_is_not_abstract():
    assert not inspect.isabstract(morel_IfStatement)


def test_morel_ifstatement_constructor_exists():
    assert callable(morel_IfStatement.__init__)


def test_morel_ifstatement_constructor_args():
    sig = inspect.signature(morel_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_booleanandexpchild_is_not_abstract():
    assert not inspect.isabstract(BooleanAndExpChild)


def test_booleanandexpchild_constructor_exists():
    assert callable(BooleanAndExpChild.__init__)


def test_booleanandexpchild_constructor_args():
    sig = inspect.signature(BooleanAndExpChild.__init__)
    params = list(sig.parameters.keys())



def test_morel_relationalexpchild_is_not_abstract():
    assert not inspect.isabstract(morel_RelationalExpChild)


def test_morel_relationalexpchild_constructor_exists():
    assert callable(morel_RelationalExpChild.__init__)


def test_morel_relationalexpchild_constructor_args():
    sig = inspect.signature(morel_RelationalExpChild.__init__)
    params = list(sig.parameters.keys())



def test_morel_relationalexp_is_not_abstract():
    assert not inspect.isabstract(morel_RelationalExp)


def test_morel_relationalexp_constructor_exists():
    assert callable(morel_RelationalExp.__init__)


def test_morel_relationalexp_constructor_args():
    sig = inspect.signature(morel_RelationalExp.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_morel_relationalexp_has_operator():
    assert hasattr(morel_RelationalExp, "operator")
    descriptor = None
    for klass in morel_RelationalExp.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_booleanorexpchild_is_not_abstract():
    assert not inspect.isabstract(BooleanOrExpChild)


def test_booleanorexpchild_constructor_exists():
    assert callable(BooleanOrExpChild.__init__)


def test_booleanorexpchild_constructor_args():
    sig = inspect.signature(BooleanOrExpChild.__init__)
    params = list(sig.parameters.keys())



def test_morel_booleanandexpchild_is_not_abstract():
    assert not inspect.isabstract(morel_BooleanAndExpChild)


def test_morel_booleanandexpchild_constructor_exists():
    assert callable(morel_BooleanAndExpChild.__init__)


def test_morel_booleanandexpchild_constructor_args():
    sig = inspect.signature(morel_BooleanAndExpChild.__init__)
    params = list(sig.parameters.keys())



def test_morel_booleanandexp_is_not_abstract():
    assert not inspect.isabstract(morel_BooleanAndExp)


def test_morel_booleanandexp_constructor_exists():
    assert callable(morel_BooleanAndExp.__init__)


def test_morel_booleanandexp_constructor_args():
    sig = inspect.signature(morel_BooleanAndExp.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"

def test_morel_booleanandexp_has_operators():
    assert hasattr(morel_BooleanAndExp, "operators")
    descriptor = None
    for klass in morel_BooleanAndExp.__mro__:
        if "operators" in klass.__dict__:
            descriptor = klass.__dict__["operators"]
            break
    assert isinstance(descriptor, property)



def test_booleanimpliesexpchild_is_not_abstract():
    assert not inspect.isabstract(BooleanImpliesExpChild)


def test_booleanimpliesexpchild_constructor_exists():
    assert callable(BooleanImpliesExpChild.__init__)


def test_booleanimpliesexpchild_constructor_args():
    sig = inspect.signature(BooleanImpliesExpChild.__init__)
    params = list(sig.parameters.keys())



def test_morel_booleanorexpchild_is_not_abstract():
    assert not inspect.isabstract(morel_BooleanOrExpChild)


def test_morel_booleanorexpchild_constructor_exists():
    assert callable(morel_BooleanOrExpChild.__init__)


def test_morel_booleanorexpchild_constructor_args():
    sig = inspect.signature(morel_BooleanOrExpChild.__init__)
    params = list(sig.parameters.keys())



def test_morel_booleanorexp_is_not_abstract():
    assert not inspect.isabstract(morel_BooleanOrExp)


def test_morel_booleanorexp_constructor_exists():
    assert callable(morel_BooleanOrExp.__init__)


def test_morel_booleanorexp_constructor_args():
    sig = inspect.signature(morel_BooleanOrExp.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"

def test_morel_booleanorexp_has_operators():
    assert hasattr(morel_BooleanOrExp, "operators")
    descriptor = None
    for klass in morel_BooleanOrExp.__mro__:
        if "operators" in klass.__dict__:
            descriptor = klass.__dict__["operators"]
            break
    assert isinstance(descriptor, property)



def test_multiplicativeexpchild_is_not_abstract():
    assert not inspect.isabstract(MultiplicativeExpChild)


def test_multiplicativeexpchild_constructor_exists():
    assert callable(MultiplicativeExpChild.__init__)


def test_multiplicativeexpchild_constructor_args():
    sig = inspect.signature(MultiplicativeExpChild.__init__)
    params = list(sig.parameters.keys())



def test_morel_unaryexpchild_is_not_abstract():
    assert not inspect.isabstract(morel_UnaryExpChild)


def test_morel_unaryexpchild_constructor_exists():
    assert callable(morel_UnaryExpChild.__init__)


def test_morel_unaryexpchild_constructor_args():
    sig = inspect.signature(morel_UnaryExpChild.__init__)
    params = list(sig.parameters.keys())



def test_morel_unaryexp_is_not_abstract():
    assert not inspect.isabstract(morel_UnaryExp)


def test_morel_unaryexp_constructor_exists():
    assert callable(morel_UnaryExp.__init__)


def test_morel_unaryexp_constructor_args():
    sig = inspect.signature(morel_UnaryExp.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_morel_unaryexp_has_operator():
    assert hasattr(morel_UnaryExp, "operator")
    descriptor = None
    for klass in morel_UnaryExp.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_additiveexpchild_is_not_abstract():
    assert not inspect.isabstract(AdditiveExpChild)


def test_additiveexpchild_constructor_exists():
    assert callable(AdditiveExpChild.__init__)


def test_additiveexpchild_constructor_args():
    sig = inspect.signature(AdditiveExpChild.__init__)
    params = list(sig.parameters.keys())



def test_morel_multiplicativeexpchild_is_not_abstract():
    assert not inspect.isabstract(morel_MultiplicativeExpChild)


def test_morel_multiplicativeexpchild_constructor_exists():
    assert callable(morel_MultiplicativeExpChild.__init__)


def test_morel_multiplicativeexpchild_constructor_args():
    sig = inspect.signature(morel_MultiplicativeExpChild.__init__)
    params = list(sig.parameters.keys())



def test_morel_multiplicativeexp_is_not_abstract():
    assert not inspect.isabstract(morel_MultiplicativeExp)


def test_morel_multiplicativeexp_constructor_exists():
    assert callable(morel_MultiplicativeExp.__init__)


def test_morel_multiplicativeexp_constructor_args():
    sig = inspect.signature(morel_MultiplicativeExp.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"

def test_morel_multiplicativeexp_has_operators():
    assert hasattr(morel_MultiplicativeExp, "operators")
    descriptor = None
    for klass in morel_MultiplicativeExp.__mro__:
        if "operators" in klass.__dict__:
            descriptor = klass.__dict__["operators"]
            break
    assert isinstance(descriptor, property)



def test_relationalexpchild_is_not_abstract():
    assert not inspect.isabstract(RelationalExpChild)


def test_relationalexpchild_constructor_exists():
    assert callable(RelationalExpChild.__init__)


def test_relationalexpchild_constructor_args():
    sig = inspect.signature(RelationalExpChild.__init__)
    params = list(sig.parameters.keys())



def test_morel_additiveexpchild_is_not_abstract():
    assert not inspect.isabstract(morel_AdditiveExpChild)


def test_morel_additiveexpchild_constructor_exists():
    assert callable(morel_AdditiveExpChild.__init__)


def test_morel_additiveexpchild_constructor_args():
    sig = inspect.signature(morel_AdditiveExpChild.__init__)
    params = list(sig.parameters.keys())



def test_morel_additiveexp_is_not_abstract():
    assert not inspect.isabstract(morel_AdditiveExp)


def test_morel_additiveexp_constructor_exists():
    assert callable(morel_AdditiveExp.__init__)


def test_morel_additiveexp_constructor_args():
    sig = inspect.signature(morel_AdditiveExp.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"

def test_morel_additiveexp_has_operators():
    assert hasattr(morel_AdditiveExp, "operators")
    descriptor = None
    for klass in morel_AdditiveExp.__mro__:
        if "operators" in klass.__dict__:
            descriptor = klass.__dict__["operators"]
            break
    assert isinstance(descriptor, property)



def test_imperativeexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeExp)


def test_imperativeexp_constructor_exists():
    assert callable(ImperativeExp.__init__)


def test_imperativeexp_constructor_args():
    sig = inspect.signature(ImperativeExp.__init__)
    params = list(sig.parameters.keys())



def test_morel_bindexp_is_not_abstract():
    assert not inspect.isabstract(morel_BindExp)


def test_morel_bindexp_constructor_exists():
    assert callable(morel_BindExp.__init__)


def test_morel_bindexp_constructor_args():
    sig = inspect.signature(morel_BindExp.__init__)
    params = list(sig.parameters.keys())



def test_morel_predefinedbindexp_is_not_abstract():
    assert not inspect.isabstract(morel_PredefinedBindExp)


def test_morel_predefinedbindexp_constructor_exists():
    assert callable(morel_PredefinedBindExp.__init__)


def test_morel_predefinedbindexp_constructor_args():
    sig = inspect.signature(morel_PredefinedBindExp.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_morel_imperativeexp_is_not_abstract():
    assert not inspect.isabstract(morel_ImperativeExp)


def test_morel_imperativeexp_constructor_exists():
    assert callable(morel_ImperativeExp.__init__)


def test_morel_imperativeexp_constructor_args():
    sig = inspect.signature(morel_ImperativeExp.__init__)
    params = list(sig.parameters.keys())



def test_morel_booleanimpliesexpchild_is_not_abstract():
    assert not inspect.isabstract(morel_BooleanImpliesExpChild)


def test_morel_booleanimpliesexpchild_constructor_exists():
    assert callable(morel_BooleanImpliesExpChild.__init__)


def test_morel_booleanimpliesexpchild_constructor_args():
    sig = inspect.signature(morel_BooleanImpliesExpChild.__init__)
    params = list(sig.parameters.keys())



def test_morel_reflectivevariableexp_is_not_abstract():
    assert not inspect.isabstract(morel_ReflectiveVariableExp)


def test_morel_reflectivevariableexp_constructor_exists():
    assert callable(morel_ReflectiveVariableExp.__init__)


def test_morel_reflectivevariableexp_constructor_args():
    sig = inspect.signature(morel_ReflectiveVariableExp.__init__)
    params = list(sig.parameters.keys())



def test_morel_letexp_is_not_abstract():
    assert not inspect.isabstract(morel_LetExp)


def test_morel_letexp_constructor_exists():
    assert callable(morel_LetExp.__init__)


def test_morel_letexp_constructor_args():
    sig = inspect.signature(morel_LetExp.__init__)
    params = list(sig.parameters.keys())



def test_looppathexp_is_not_abstract():
    assert not inspect.isabstract(LoopPathExp)


def test_looppathexp_constructor_exists():
    assert callable(LoopPathExp.__init__)


def test_looppathexp_constructor_args():
    sig = inspect.signature(LoopPathExp.__init__)
    params = list(sig.parameters.keys())



def test_morel_iteratorpathexp_is_not_abstract():
    assert not inspect.isabstract(morel_IteratorPathExp)


def test_morel_iteratorpathexp_constructor_exists():
    assert callable(morel_IteratorPathExp.__init__)


def test_morel_iteratorpathexp_constructor_args():
    sig = inspect.signature(morel_IteratorPathExp.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_morel_iteratorpathexp_has_type():
    assert hasattr(morel_IteratorPathExp, "type")
    descriptor = None
    for klass in morel_IteratorPathExp.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_morel_booleanimpliesexp_is_not_abstract():
    assert not inspect.isabstract(morel_BooleanImpliesExp)


def test_morel_booleanimpliesexp_constructor_exists():
    assert callable(morel_BooleanImpliesExp.__init__)


def test_morel_booleanimpliesexp_constructor_args():
    sig = inspect.signature(morel_BooleanImpliesExp.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_morel_booleanimpliesexp_has_operator():
    assert hasattr(morel_BooleanImpliesExp, "operator")
    descriptor = None
    for klass in morel_BooleanImpliesExp.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_morel_conditionexp_is_not_abstract():
    assert not inspect.isabstract(morel_ConditionExp)


def test_morel_conditionexp_constructor_exists():
    assert callable(morel_ConditionExp.__init__)


def test_morel_conditionexp_constructor_args():
    sig = inspect.signature(morel_ConditionExp.__init__)
    params = list(sig.parameters.keys())



def test_primitivevariable_is_not_abstract():
    assert not inspect.isabstract(PrimitiveVariable)


def test_primitivevariable_constructor_exists():
    assert callable(PrimitiveVariable.__init__)


def test_primitivevariable_constructor_args():
    sig = inspect.signature(PrimitiveVariable.__init__)
    params = list(sig.parameters.keys())



def test_variablewithinit_is_not_abstract():
    assert not inspect.isabstract(VariableWithInit)


def test_variablewithinit_constructor_exists():
    assert callable(VariableWithInit.__init__)


def test_variablewithinit_constructor_args():
    sig = inspect.signature(VariableWithInit.__init__)
    params = list(sig.parameters.keys())



def test_morel_primitivevariablewithinit_is_not_abstract():
    assert not inspect.isabstract(morel_PrimitiveVariableWithInit)


def test_morel_primitivevariablewithinit_constructor_exists():
    assert callable(morel_PrimitiveVariableWithInit.__init__)


def test_morel_primitivevariablewithinit_constructor_args():
    sig = inspect.signature(morel_PrimitiveVariableWithInit.__init__)
    params = list(sig.parameters.keys())



def test_objectvariable_is_not_abstract():
    assert not inspect.isabstract(ObjectVariable)


def test_objectvariable_constructor_exists():
    assert callable(ObjectVariable.__init__)


def test_objectvariable_constructor_args():
    sig = inspect.signature(ObjectVariable.__init__)
    params = list(sig.parameters.keys())



def test_morel_objectvariablewithinit_is_not_abstract():
    assert not inspect.isabstract(morel_ObjectVariableWithInit)


def test_morel_objectvariablewithinit_constructor_exists():
    assert callable(morel_ObjectVariableWithInit.__init__)


def test_morel_objectvariablewithinit_constructor_args():
    sig = inspect.signature(morel_ObjectVariableWithInit.__init__)
    params = list(sig.parameters.keys())



def test_morel_eclassifier_is_not_abstract():
    assert not inspect.isabstract(morel_EClassifier)


def test_morel_eclassifier_constructor_exists():
    assert callable(morel_EClassifier.__init__)


def test_morel_eclassifier_constructor_args():
    sig = inspect.signature(morel_EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_morel_eenumliteral_is_not_abstract():
    assert not inspect.isabstract(morel_EEnumLiteral)


def test_morel_eenumliteral_constructor_exists():
    assert callable(morel_EEnumLiteral.__init__)


def test_morel_eenumliteral_constructor_args():
    sig = inspect.signature(morel_EEnumLiteral.__init__)
    params = list(sig.parameters.keys())



def test_morel_eenum_is_not_abstract():
    assert not inspect.isabstract(morel_EEnum)


def test_morel_eenum_constructor_exists():
    assert callable(morel_EEnum.__init__)


def test_morel_eenum_constructor_args():
    sig = inspect.signature(morel_EEnum.__init__)
    params = list(sig.parameters.keys())



def test_callpathexp_is_not_abstract():
    assert not inspect.isabstract(CallPathExp)


def test_callpathexp_constructor_exists():
    assert callable(CallPathExp.__init__)


def test_callpathexp_constructor_args():
    sig = inspect.signature(CallPathExp.__init__)
    params = list(sig.parameters.keys())



def test_morel_looppathexp_is_not_abstract():
    assert not inspect.isabstract(morel_LoopPathExp)


def test_morel_looppathexp_constructor_exists():
    assert callable(morel_LoopPathExp.__init__)


def test_morel_looppathexp_constructor_args():
    sig = inspect.signature(morel_LoopPathExp.__init__)
    params = list(sig.parameters.keys())



def test_morel_operationpathexp_is_not_abstract():
    assert not inspect.isabstract(morel_OperationPathExp)


def test_morel_operationpathexp_constructor_exists():
    assert callable(morel_OperationPathExp.__init__)


def test_morel_operationpathexp_constructor_args():
    sig = inspect.signature(morel_OperationPathExp.__init__)
    params = list(sig.parameters.keys())
    assert "separator" in params, "Missing parameter 'separator'"
    assert "operation" in params, "Missing parameter 'operation'"

def test_morel_operationpathexp_has_separator():
    assert hasattr(morel_OperationPathExp, "separator")
    descriptor = None
    for klass in morel_OperationPathExp.__mro__:
        if "separator" in klass.__dict__:
            descriptor = klass.__dict__["separator"]
            break
    assert isinstance(descriptor, property)

def test_morel_operationpathexp_has_operation():
    assert hasattr(morel_OperationPathExp, "operation")
    descriptor = None
    for klass in morel_OperationPathExp.__mro__:
        if "operation" in klass.__dict__:
            descriptor = klass.__dict__["operation"]
            break
    assert isinstance(descriptor, property)



def test_morel_featurepathexp_is_not_abstract():
    assert not inspect.isabstract(morel_FeaturePathExp)


def test_morel_featurepathexp_constructor_exists():
    assert callable(morel_FeaturePathExp.__init__)


def test_morel_featurepathexp_constructor_args():
    sig = inspect.signature(morel_FeaturePathExp.__init__)
    params = list(sig.parameters.keys())
    assert "feature" in params, "Missing parameter 'feature'"

def test_morel_featurepathexp_has_feature():
    assert hasattr(morel_FeaturePathExp, "feature")
    descriptor = None
    for klass in morel_FeaturePathExp.__mro__:
        if "feature" in klass.__dict__:
            descriptor = klass.__dict__["feature"]
            break
    assert isinstance(descriptor, property)



def test_morel_unit_is_not_abstract():
    assert not inspect.isabstract(morel_Unit)


def test_morel_unit_constructor_exists():
    assert callable(morel_Unit.__init__)


def test_morel_unit_constructor_args():
    sig = inspect.signature(morel_Unit.__init__)
    params = list(sig.parameters.keys())



def test_executable_is_not_abstract():
    assert not inspect.isabstract(Executable)


def test_executable_constructor_exists():
    assert callable(Executable.__init__)


def test_executable_constructor_args():
    sig = inspect.signature(Executable.__init__)
    params = list(sig.parameters.keys())



def test_pattern_is_not_abstract():
    assert not inspect.isabstract(Pattern)


def test_pattern_constructor_exists():
    assert callable(Pattern.__init__)


def test_pattern_constructor_args():
    sig = inspect.signature(Pattern.__init__)
    params = list(sig.parameters.keys())



def test_morel_epackage_is_not_abstract():
    assert not inspect.isabstract(morel_EPackage)


def test_morel_epackage_constructor_exists():
    assert callable(morel_EPackage.__init__)


def test_morel_epackage_constructor_args():
    sig = inspect.signature(morel_EPackage.__init__)
    params = list(sig.parameters.keys())



def test_unit_is_not_abstract():
    assert not inspect.isabstract(Unit)


def test_unit_constructor_exists():
    assert callable(Unit.__init__)


def test_unit_constructor_args():
    sig = inspect.signature(Unit.__init__)
    params = list(sig.parameters.keys())



def test_morel_querymodel_is_not_abstract():
    assert not inspect.isabstract(morel_QueryModel)


def test_morel_querymodel_constructor_exists():
    assert callable(morel_QueryModel.__init__)


def test_morel_querymodel_constructor_args():
    sig = inspect.signature(morel_QueryModel.__init__)
    params = list(sig.parameters.keys())



def test_literalexp_is_not_abstract():
    assert not inspect.isabstract(LiteralExp)


def test_literalexp_constructor_exists():
    assert callable(LiteralExp.__init__)


def test_literalexp_constructor_args():
    sig = inspect.signature(LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_morel_realliteralexp_is_not_abstract():
    assert not inspect.isabstract(morel_RealLiteralExp)


def test_morel_realliteralexp_constructor_exists():
    assert callable(morel_RealLiteralExp.__init__)


def test_morel_realliteralexp_constructor_args():
    sig = inspect.signature(morel_RealLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_morel_realliteralexp_has_realSymbol():
    assert hasattr(morel_RealLiteralExp, "realSymbol")
    descriptor = None
    for klass in morel_RealLiteralExp.__mro__:
        if "realSymbol" in klass.__dict__:
            descriptor = klass.__dict__["realSymbol"]
            break
    assert isinstance(descriptor, property)



def test_morel_undefinedliteralexp_is_not_abstract():
    assert not inspect.isabstract(morel_UndefinedLiteralExp)


def test_morel_undefinedliteralexp_constructor_exists():
    assert callable(morel_UndefinedLiteralExp.__init__)


def test_morel_undefinedliteralexp_constructor_args():
    sig = inspect.signature(morel_UndefinedLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_morel_undefinedliteralexp_has_value():
    assert hasattr(morel_UndefinedLiteralExp, "value")
    descriptor = None
    for klass in morel_UndefinedLiteralExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_morel_collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(morel_CollectionLiteralExp)


def test_morel_collectionliteralexp_constructor_exists():
    assert callable(morel_CollectionLiteralExp.__init__)


def test_morel_collectionliteralexp_constructor_args():
    sig = inspect.signature(morel_CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_morel_collectionliteralexp_has_type():
    assert hasattr(morel_CollectionLiteralExp, "type")
    descriptor = None
    for klass in morel_CollectionLiteralExp.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_morel_booleanliteralexp_is_not_abstract():
    assert not inspect.isabstract(morel_BooleanLiteralExp)


def test_morel_booleanliteralexp_constructor_exists():
    assert callable(morel_BooleanLiteralExp.__init__)


def test_morel_booleanliteralexp_constructor_args():
    sig = inspect.signature(morel_BooleanLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "boolSymbol" in params, "Missing parameter 'boolSymbol'"

def test_morel_booleanliteralexp_has_boolSymbol():
    assert hasattr(morel_BooleanLiteralExp, "boolSymbol")
    descriptor = None
    for klass in morel_BooleanLiteralExp.__mro__:
        if "boolSymbol" in klass.__dict__:
            descriptor = klass.__dict__["boolSymbol"]
            break
    assert isinstance(descriptor, property)



def test_morel_integerliteralexp_is_not_abstract():
    assert not inspect.isabstract(morel_IntegerLiteralExp)


def test_morel_integerliteralexp_constructor_exists():
    assert callable(morel_IntegerLiteralExp.__init__)


def test_morel_integerliteralexp_constructor_args():
    sig = inspect.signature(morel_IntegerLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_morel_integerliteralexp_has_integerSymbol():
    assert hasattr(morel_IntegerLiteralExp, "integerSymbol")
    descriptor = None
    for klass in morel_IntegerLiteralExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_morel_arrayliteralexp_is_not_abstract():
    assert not inspect.isabstract(morel_ArrayLiteralExp)


def test_morel_arrayliteralexp_constructor_exists():
    assert callable(morel_ArrayLiteralExp.__init__)


def test_morel_arrayliteralexp_constructor_args():
    sig = inspect.signature(morel_ArrayLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_morel_enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(morel_EnumLiteralExp)


def test_morel_enumliteralexp_constructor_exists():
    assert callable(morel_EnumLiteralExp.__init__)


def test_morel_enumliteralexp_constructor_args():
    sig = inspect.signature(morel_EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_morel_typeliteralexp_is_not_abstract():
    assert not inspect.isabstract(morel_TypeLiteralExp)


def test_morel_typeliteralexp_constructor_exists():
    assert callable(morel_TypeLiteralExp.__init__)


def test_morel_typeliteralexp_constructor_args():
    sig = inspect.signature(morel_TypeLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_morel_stringliteralexp_is_not_abstract():
    assert not inspect.isabstract(morel_StringLiteralExp)


def test_morel_stringliteralexp_constructor_exists():
    assert callable(morel_StringLiteralExp.__init__)


def test_morel_stringliteralexp_constructor_args():
    sig = inspect.signature(morel_StringLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_morel_stringliteralexp_has_stringSymbol():
    assert hasattr(morel_StringLiteralExp, "stringSymbol")
    descriptor = None
    for klass in morel_StringLiteralExp.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_atomicexp_is_not_abstract():
    assert not inspect.isabstract(AtomicExp)


def test_atomicexp_constructor_exists():
    assert callable(AtomicExp.__init__)


def test_atomicexp_constructor_args():
    sig = inspect.signature(AtomicExp.__init__)
    params = list(sig.parameters.keys())



def test_morel_variableexp_is_not_abstract():
    assert not inspect.isabstract(morel_VariableExp)


def test_morel_variableexp_constructor_exists():
    assert callable(morel_VariableExp.__init__)


def test_morel_variableexp_constructor_args():
    sig = inspect.signature(morel_VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_morel_predefinedvariableexp_is_not_abstract():
    assert not inspect.isabstract(morel_PredefinedVariableExp)


def test_morel_predefinedvariableexp_constructor_exists():
    assert callable(morel_PredefinedVariableExp.__init__)


def test_morel_predefinedvariableexp_constructor_args():
    sig = inspect.signature(morel_PredefinedVariableExp.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"

def test_morel_predefinedvariableexp_has_variable():
    assert hasattr(morel_PredefinedVariableExp, "variable")
    descriptor = None
    for klass in morel_PredefinedVariableExp.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_morel_nestedexp_is_not_abstract():
    assert not inspect.isabstract(morel_NestedExp)


def test_morel_nestedexp_constructor_exists():
    assert callable(morel_NestedExp.__init__)


def test_morel_nestedexp_constructor_args():
    sig = inspect.signature(morel_NestedExp.__init__)
    params = list(sig.parameters.keys())



def test_morel_literalexp_is_not_abstract():
    assert not inspect.isabstract(morel_LiteralExp)


def test_morel_literalexp_constructor_exists():
    assert callable(morel_LiteralExp.__init__)


def test_morel_literalexp_constructor_args():
    sig = inspect.signature(morel_LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_morel_callpathexp_is_not_abstract():
    assert not inspect.isabstract(morel_CallPathExp)


def test_morel_callpathexp_constructor_exists():
    assert callable(morel_CallPathExp.__init__)


def test_morel_callpathexp_constructor_args():
    sig = inspect.signature(morel_CallPathExp.__init__)
    params = list(sig.parameters.keys())



def test_unaryexpchild_is_not_abstract():
    assert not inspect.isabstract(UnaryExpChild)


def test_unaryexpchild_constructor_exists():
    assert callable(UnaryExpChild.__init__)


def test_unaryexpchild_constructor_args():
    sig = inspect.signature(UnaryExpChild.__init__)
    params = list(sig.parameters.keys())



def test_morel_atomicexp_is_not_abstract():
    assert not inspect.isabstract(morel_AtomicExp)


def test_morel_atomicexp_constructor_exists():
    assert callable(morel_AtomicExp.__init__)


def test_morel_atomicexp_constructor_args():
    sig = inspect.signature(morel_AtomicExp.__init__)
    params = list(sig.parameters.keys())



def test_morel_edatatype_is_not_abstract():
    assert not inspect.isabstract(morel_EDataType)


def test_morel_edatatype_constructor_exists():
    assert callable(morel_EDataType.__init__)


def test_morel_edatatype_constructor_args():
    sig = inspect.signature(morel_EDataType.__init__)
    params = list(sig.parameters.keys())



def test_morel_eclass_is_not_abstract():
    assert not inspect.isabstract(morel_EClass)


def test_morel_eclass_constructor_exists():
    assert callable(morel_EClass.__init__)


def test_morel_eclass_constructor_args():
    sig = inspect.signature(morel_EClass.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_morel_primitivevariable_is_not_abstract():
    assert not inspect.isabstract(morel_PrimitiveVariable)


def test_morel_primitivevariable_constructor_exists():
    assert callable(morel_PrimitiveVariable.__init__)


def test_morel_primitivevariable_constructor_args():
    sig = inspect.signature(morel_PrimitiveVariable.__init__)
    params = list(sig.parameters.keys())



def test_morel_variablewithinit_is_not_abstract():
    assert not inspect.isabstract(morel_VariableWithInit)


def test_morel_variablewithinit_constructor_exists():
    assert callable(morel_VariableWithInit.__init__)


def test_morel_variablewithinit_constructor_args():
    sig = inspect.signature(morel_VariableWithInit.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_morel_ruleelement_is_not_abstract():
    assert not inspect.isabstract(morel_RuleElement)


def test_morel_ruleelement_constructor_exists():
    assert callable(morel_RuleElement.__init__)


def test_morel_ruleelement_constructor_args():
    sig = inspect.signature(morel_RuleElement.__init__)
    params = list(sig.parameters.keys())



def test_morel_typedmodel_is_not_abstract():
    assert not inspect.isabstract(morel_TypedModel)


def test_morel_typedmodel_constructor_exists():
    assert callable(morel_TypedModel.__init__)


def test_morel_typedmodel_constructor_args():
    sig = inspect.signature(morel_TypedModel.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_morel_typedmodel_has_type():
    assert hasattr(morel_TypedModel, "type")
    descriptor = None
    for klass in morel_TypedModel.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_morel_transformationmodel_is_not_abstract():
    assert not inspect.isabstract(morel_TransformationModel)


def test_morel_transformationmodel_constructor_exists():
    assert callable(morel_TransformationModel.__init__)


def test_morel_transformationmodel_constructor_args():
    sig = inspect.signature(morel_TransformationModel.__init__)
    params = list(sig.parameters.keys())



def test_morel_query_is_not_abstract():
    assert not inspect.isabstract(morel_Query)


def test_morel_query_constructor_exists():
    assert callable(morel_Query.__init__)


def test_morel_query_constructor_args():
    sig = inspect.signature(morel_Query.__init__)
    params = list(sig.parameters.keys())



def test_morel_variable_is_not_abstract():
    assert not inspect.isabstract(morel_Variable)


def test_morel_variable_constructor_exists():
    assert callable(morel_Variable.__init__)


def test_morel_variable_constructor_args():
    sig = inspect.signature(morel_Variable.__init__)
    params = list(sig.parameters.keys())



def test_morel_additionalconstraint_is_not_abstract():
    assert not inspect.isabstract(morel_AdditionalConstraint)


def test_morel_additionalconstraint_constructor_exists():
    assert callable(morel_AdditionalConstraint.__init__)


def test_morel_additionalconstraint_constructor_args():
    sig = inspect.signature(morel_AdditionalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_morel_statement_is_not_abstract():
    assert not inspect.isabstract(morel_Statement)


def test_morel_statement_constructor_exists():
    assert callable(morel_Statement.__init__)


def test_morel_statement_constructor_args():
    sig = inspect.signature(morel_Statement.__init__)
    params = list(sig.parameters.keys())



def test_morel_ereference_is_not_abstract():
    assert not inspect.isabstract(morel_EReference)


def test_morel_ereference_constructor_exists():
    assert callable(morel_EReference.__init__)


def test_morel_ereference_constructor_args():
    sig = inspect.signature(morel_EReference.__init__)
    params = list(sig.parameters.keys())



def test_morel_expression_is_not_abstract():
    assert not inspect.isabstract(morel_Expression)


def test_morel_expression_constructor_exists():
    assert callable(morel_Expression.__init__)


def test_morel_expression_constructor_args():
    sig = inspect.signature(morel_Expression.__init__)
    params = list(sig.parameters.keys())



def test_linkconstraint_is_not_abstract():
    assert not inspect.isabstract(LinkConstraint)


def test_linkconstraint_constructor_exists():
    assert callable(LinkConstraint.__init__)


def test_linkconstraint_constructor_args():
    sig = inspect.signature(LinkConstraint.__init__)
    params = list(sig.parameters.keys())



def test_morel_enclosurelinkconstraint_is_not_abstract():
    assert not inspect.isabstract(morel_EnclosureLinkConstraint)


def test_morel_enclosurelinkconstraint_constructor_exists():
    assert callable(morel_EnclosureLinkConstraint.__init__)


def test_morel_enclosurelinkconstraint_constructor_args():
    sig = inspect.signature(morel_EnclosureLinkConstraint.__init__)
    params = list(sig.parameters.keys())



def test_morel_pathconstraint_is_not_abstract():
    assert not inspect.isabstract(morel_PathConstraint)


def test_morel_pathconstraint_constructor_exists():
    assert callable(morel_PathConstraint.__init__)


def test_morel_pathconstraint_constructor_args():
    sig = inspect.signature(morel_PathConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "minLength" in params, "Missing parameter 'minLength'"
    assert "maxLength" in params, "Missing parameter 'maxLength'"

def test_morel_pathconstraint_has_minLength():
    assert hasattr(morel_PathConstraint, "minLength")
    descriptor = None
    for klass in morel_PathConstraint.__mro__:
        if "minLength" in klass.__dict__:
            descriptor = klass.__dict__["minLength"]
            break
    assert isinstance(descriptor, property)

def test_morel_pathconstraint_has_maxLength():
    assert hasattr(morel_PathConstraint, "maxLength")
    descriptor = None
    for klass in morel_PathConstraint.__mro__:
        if "maxLength" in klass.__dict__:
            descriptor = klass.__dict__["maxLength"]
            break
    assert isinstance(descriptor, property)



def test_morel_simplelinkconstraint_is_not_abstract():
    assert not inspect.isabstract(morel_SimpleLinkConstraint)


def test_morel_simplelinkconstraint_constructor_exists():
    assert callable(morel_SimpleLinkConstraint.__init__)


def test_morel_simplelinkconstraint_constructor_args():
    sig = inspect.signature(morel_SimpleLinkConstraint.__init__)
    params = list(sig.parameters.keys())



def test_morel_linkconstraint_is_not_abstract():
    assert not inspect.isabstract(morel_LinkConstraint)


def test_morel_linkconstraint_constructor_exists():
    assert callable(morel_LinkConstraint.__init__)


def test_morel_linkconstraint_constructor_args():
    sig = inspect.signature(morel_LinkConstraint.__init__)
    params = list(sig.parameters.keys())



def test_morel_objectvariable_is_not_abstract():
    assert not inspect.isabstract(morel_ObjectVariable)


def test_morel_objectvariable_constructor_exists():
    assert callable(morel_ObjectVariable.__init__)


def test_morel_objectvariable_constructor_args():
    sig = inspect.signature(morel_ObjectVariable.__init__)
    params = list(sig.parameters.keys())



def test_section_is_not_abstract():
    assert not inspect.isabstract(Section)


def test_section_constructor_exists():
    assert callable(Section.__init__)


def test_section_constructor_args():
    sig = inspect.signature(Section.__init__)
    params = list(sig.parameters.keys())



def test_morel_clause_is_not_abstract():
    assert not inspect.isabstract(morel_Clause)


def test_morel_clause_constructor_exists():
    assert callable(morel_Clause.__init__)


def test_morel_clause_constructor_args():
    sig = inspect.signature(morel_Clause.__init__)
    params = list(sig.parameters.keys())



def test_morel_pattern_is_not_abstract():
    assert not inspect.isabstract(morel_Pattern)


def test_morel_pattern_constructor_exists():
    assert callable(morel_Pattern.__init__)


def test_morel_pattern_constructor_args():
    sig = inspect.signature(morel_Pattern.__init__)
    params = list(sig.parameters.keys())



def test_morel_section_is_not_abstract():
    assert not inspect.isabstract(morel_Section)


def test_morel_section_constructor_exists():
    assert callable(morel_Section.__init__)


def test_morel_section_constructor_args():
    sig = inspect.signature(morel_Section.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_morel_section_has_type():
    assert hasattr(morel_Section, "type")
    descriptor = None
    for klass in morel_Section.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_morel_namedelement_is_not_abstract():
    assert not inspect.isabstract(morel_NamedElement)


def test_morel_namedelement_constructor_exists():
    assert callable(morel_NamedElement.__init__)


def test_morel_namedelement_constructor_args():
    sig = inspect.signature(morel_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_morel_namedelement_has_name():
    assert hasattr(morel_NamedElement, "name")
    descriptor = None
    for klass in morel_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sectiontype_exists():
    # Check that the Enumeration exists
    assert SectionType is not None

def test_sectiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SectionType]
    expected_literals = [
        "NAC",
        "RHS",
        "PRE",
        "PAC",
        "LHS",
        "POST",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SectionType"

def test_iterationtype_exists():
    # Check that the Enumeration exists
    assert IterationType is not None

def test_iterationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IterationType]
    expected_literals = [
        "default",
        "shuffle",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IterationType"

def test_iteratortype_exists():
    # Check that the Enumeration exists
    assert IteratorType is not None

def test_iteratortype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IteratorType]
    expected_literals = [
        "select",
        "forAll",
        "exists",
        "collect",
        "reject",
        "closure",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IteratorType"

def test_repetitiontype_exists():
    # Check that the Enumeration exists
    assert RepetitionType is not None

def test_repetitiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RepetitionType]
    expected_literals = [
        "randomOne",
        "first",
        "allMatches",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RepetitionType"

def test_additiveoperator_exists():
    # Check that the Enumeration exists
    assert AdditiveOperator is not None

def test_additiveoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AdditiveOperator]
    expected_literals = [
        "plus",
        "minus",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AdditiveOperator"

def test_relationaloperator_exists():
    # Check that the Enumeration exists
    assert RelationalOperator is not None

def test_relationaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationalOperator]
    expected_literals = [
        "less",
        "lessOrEq",
        "equal",
        "greaterOrEq",
        "notEqual",
        "greater",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationalOperator"

def test_undefinedliteral_exists():
    # Check that the Enumeration exists
    assert UndefinedLiteral is not None

def test_undefinedliteral_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UndefinedLiteral]
    expected_literals = [
        "NULL",
        "INVALID",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UndefinedLiteral"

def test_booleanoperator_exists():
    # Check that the Enumeration exists
    assert BooleanOperator is not None

def test_booleanoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanOperator]
    expected_literals = [
        "implies",
        "and_",
        "not_",
        "or_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BooleanOperator"

def test_scopetype_exists():
    # Check that the Enumeration exists
    assert ScopeType is not None

def test_scopetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ScopeType]
    expected_literals = [
        "dynamicRandom",
        "all",
        "staticRandom",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ScopeType"

def test_multiplicativeoperator_exists():
    # Check that the Enumeration exists
    assert MultiplicativeOperator is not None

def test_multiplicativeoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MultiplicativeOperator]
    expected_literals = [
        "multi",
        "div",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MultiplicativeOperator"

def test_unaryoperator_exists():
    # Check that the Enumeration exists
    assert UnaryOperator is not None

def test_unaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryOperator]
    expected_literals = [
        "plus",
        "minus",
        "not_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryOperator"

def test_ordertype_exists():
    # Check that the Enumeration exists
    assert OrderType is not None

def test_ordertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OrderType]
    expected_literals = [
        "sequential",
        "default",
        "parallel",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OrderType"

def test_typedmodelaction_exists():
    # Check that the Enumeration exists
    assert TypedModelAction is not None

def test_typedmodelaction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypedModelAction]
    expected_literals = [
        "transient",
        "createOnly",
        "normal",
        "viewOnly",
        "readOnly",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypedModelAction"

def test_predefinedvariable_exists():
    # Check that the Enumeration exists
    assert PredefinedVariable is not None

def test_predefinedvariable_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PredefinedVariable]
    expected_literals = [
        "id",
        "this",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PredefinedVariable"

def test_operationseparator_exists():
    # Check that the Enumeration exists
    assert OperationSeparator is not None

def test_operationseparator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OperationSeparator]
    expected_literals = [
        "arrow",
        "dot",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OperationSeparator"


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
morel_PrimitiveConstraint_strategy = st.builds(
    morel_PrimitiveConstraint,
)
AdditionalConstraint_strategy = st.builds(
    AdditionalConstraint,
)
morel_AllDifferentConstraint_strategy = st.builds(
    morel_AllDifferentConstraint,
)
morel_OrderConstraint_strategy = st.builds(
    morel_OrderConstraint,
)
morel_Executable_strategy = st.builds(
    morel_Executable,
    parameters=
        safe_text,
    active=
        st.booleans()
)
morel_EAttribute_strategy = st.builds(
    morel_EAttribute,
)
PrimitiveConstraint_strategy = st.builds(
    PrimitiveConstraint,
)
morel_ValueRangeConstraint_strategy = st.builds(
    morel_ValueRangeConstraint,
)
morel_MultiValueConstraint_strategy = st.builds(
    morel_MultiValueConstraint,
)
RuleElement_strategy = st.builds(
    RuleElement,
)
morel_RuleGroup_strategy = st.builds(
    morel_RuleGroup,
    iteration=
        safe_text,
    maxIteration=
        st.integers(),
    order=
        safe_text,
    repetition=
        safe_text,
    scopeSize=
        st.integers(),
    scope=
        safe_text
)
morel_Rule_strategy = st.builds(
    morel_Rule,
)
Statement_strategy = st.builds(
    Statement,
)
morel_DeclarativeStatement_strategy = st.builds(
    morel_DeclarativeStatement,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
morel_SequenceType_strategy = st.builds(
    morel_SequenceType,
)
morel_SetType_strategy = st.builds(
    morel_SetType,
)
morel_BagType_strategy = st.builds(
    morel_BagType,
)
morel_OrderedSetType_strategy = st.builds(
    morel_OrderedSetType,
)
EDataType_strategy = st.builds(
    EDataType,
)
morel_CollectionType_strategy = st.builds(
    morel_CollectionType,
)
morel_ImperativeStatement_strategy = st.builds(
    morel_ImperativeStatement,
)
ImperativeStatement_strategy = st.builds(
    ImperativeStatement,
)
morel_BlockStatement_strategy = st.builds(
    morel_BlockStatement,
)
morel_ForStatement_strategy = st.builds(
    morel_ForStatement,
)
morel_IfStatement_strategy = st.builds(
    morel_IfStatement,
)
BooleanAndExpChild_strategy = st.builds(
    BooleanAndExpChild,
)
morel_RelationalExpChild_strategy = st.builds(
    morel_RelationalExpChild,
)
morel_RelationalExp_strategy = st.builds(
    morel_RelationalExp,
    operator=
        safe_text
)
BooleanOrExpChild_strategy = st.builds(
    BooleanOrExpChild,
)
morel_BooleanAndExpChild_strategy = st.builds(
    morel_BooleanAndExpChild,
)
morel_BooleanAndExp_strategy = st.builds(
    morel_BooleanAndExp,
    operators=
        safe_text
)
BooleanImpliesExpChild_strategy = st.builds(
    BooleanImpliesExpChild,
)
morel_BooleanOrExpChild_strategy = st.builds(
    morel_BooleanOrExpChild,
)
morel_BooleanOrExp_strategy = st.builds(
    morel_BooleanOrExp,
    operators=
        safe_text
)
MultiplicativeExpChild_strategy = st.builds(
    MultiplicativeExpChild,
)
morel_UnaryExpChild_strategy = st.builds(
    morel_UnaryExpChild,
)
morel_UnaryExp_strategy = st.builds(
    morel_UnaryExp,
    operator=
        safe_text
)
AdditiveExpChild_strategy = st.builds(
    AdditiveExpChild,
)
morel_MultiplicativeExpChild_strategy = st.builds(
    morel_MultiplicativeExpChild,
)
morel_MultiplicativeExp_strategy = st.builds(
    morel_MultiplicativeExp,
    operators=
        safe_text
)
RelationalExpChild_strategy = st.builds(
    RelationalExpChild,
)
morel_AdditiveExpChild_strategy = st.builds(
    morel_AdditiveExpChild,
)
morel_AdditiveExp_strategy = st.builds(
    morel_AdditiveExp,
    operators=
        safe_text
)
ImperativeExp_strategy = st.builds(
    ImperativeExp,
)
morel_BindExp_strategy = st.builds(
    morel_BindExp,
)
morel_PredefinedBindExp_strategy = st.builds(
    morel_PredefinedBindExp,
)
Expression_strategy = st.builds(
    Expression,
)
morel_ImperativeExp_strategy = st.builds(
    morel_ImperativeExp,
)
morel_BooleanImpliesExpChild_strategy = st.builds(
    morel_BooleanImpliesExpChild,
)
morel_ReflectiveVariableExp_strategy = st.builds(
    morel_ReflectiveVariableExp,
)
morel_LetExp_strategy = st.builds(
    morel_LetExp,
)
LoopPathExp_strategy = st.builds(
    LoopPathExp,
)
morel_IteratorPathExp_strategy = st.builds(
    morel_IteratorPathExp,
    type=
        safe_text
)
morel_BooleanImpliesExp_strategy = st.builds(
    morel_BooleanImpliesExp,
    operator=
        safe_text
)
morel_ConditionExp_strategy = st.builds(
    morel_ConditionExp,
)
PrimitiveVariable_strategy = st.builds(
    PrimitiveVariable,
)
VariableWithInit_strategy = st.builds(
    VariableWithInit,
)
morel_PrimitiveVariableWithInit_strategy = st.builds(
    morel_PrimitiveVariableWithInit,
)
ObjectVariable_strategy = st.builds(
    ObjectVariable,
)
morel_ObjectVariableWithInit_strategy = st.builds(
    morel_ObjectVariableWithInit,
)
morel_EClassifier_strategy = st.builds(
    morel_EClassifier,
)
morel_EEnumLiteral_strategy = st.builds(
    morel_EEnumLiteral,
)
morel_EEnum_strategy = st.builds(
    morel_EEnum,
)
CallPathExp_strategy = st.builds(
    CallPathExp,
)
morel_LoopPathExp_strategy = st.builds(
    morel_LoopPathExp,
)
morel_OperationPathExp_strategy = st.builds(
    morel_OperationPathExp,
    separator=
        safe_text,
    operation=
        safe_text
)
morel_FeaturePathExp_strategy = st.builds(
    morel_FeaturePathExp,
    feature=
        safe_text
)
morel_Unit_strategy = st.builds(
    morel_Unit,
)
Executable_strategy = st.builds(
    Executable,
)
Pattern_strategy = st.builds(
    Pattern,
)
morel_EPackage_strategy = st.builds(
    morel_EPackage,
)
Unit_strategy = st.builds(
    Unit,
)
morel_QueryModel_strategy = st.builds(
    morel_QueryModel,
)
LiteralExp_strategy = st.builds(
    LiteralExp,
)
morel_RealLiteralExp_strategy = st.builds(
    morel_RealLiteralExp,
    realSymbol=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
morel_UndefinedLiteralExp_strategy = st.builds(
    morel_UndefinedLiteralExp,
    value=
        safe_text
)
morel_CollectionLiteralExp_strategy = st.builds(
    morel_CollectionLiteralExp,
    type=
        safe_text
)
morel_BooleanLiteralExp_strategy = st.builds(
    morel_BooleanLiteralExp,
    boolSymbol=
        st.booleans()
)
morel_IntegerLiteralExp_strategy = st.builds(
    morel_IntegerLiteralExp,
    integerSymbol=
        st.integers()
)
morel_ArrayLiteralExp_strategy = st.builds(
    morel_ArrayLiteralExp,
)
morel_EnumLiteralExp_strategy = st.builds(
    morel_EnumLiteralExp,
)
morel_TypeLiteralExp_strategy = st.builds(
    morel_TypeLiteralExp,
)
morel_StringLiteralExp_strategy = st.builds(
    morel_StringLiteralExp,
    stringSymbol=
        safe_text
)
AtomicExp_strategy = st.builds(
    AtomicExp,
)
morel_VariableExp_strategy = st.builds(
    morel_VariableExp,
)
morel_PredefinedVariableExp_strategy = st.builds(
    morel_PredefinedVariableExp,
    variable=
        safe_text
)
morel_NestedExp_strategy = st.builds(
    morel_NestedExp,
)
morel_LiteralExp_strategy = st.builds(
    morel_LiteralExp,
)
morel_CallPathExp_strategy = st.builds(
    morel_CallPathExp,
)
UnaryExpChild_strategy = st.builds(
    UnaryExpChild,
)
morel_AtomicExp_strategy = st.builds(
    morel_AtomicExp,
)
morel_EDataType_strategy = st.builds(
    morel_EDataType,
)
morel_EClass_strategy = st.builds(
    morel_EClass,
)
Variable_strategy = st.builds(
    Variable,
)
morel_PrimitiveVariable_strategy = st.builds(
    morel_PrimitiveVariable,
)
morel_VariableWithInit_strategy = st.builds(
    morel_VariableWithInit,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
morel_RuleElement_strategy = st.builds(
    morel_RuleElement,
)
morel_TypedModel_strategy = st.builds(
    morel_TypedModel,
    type=
        safe_text
)
morel_TransformationModel_strategy = st.builds(
    morel_TransformationModel,
)
morel_Query_strategy = st.builds(
    morel_Query,
)
morel_Variable_strategy = st.builds(
    morel_Variable,
)
morel_AdditionalConstraint_strategy = st.builds(
    morel_AdditionalConstraint,
)
morel_Statement_strategy = st.builds(
    morel_Statement,
)
morel_EReference_strategy = st.builds(
    morel_EReference,
)
morel_Expression_strategy = st.builds(
    morel_Expression,
)
LinkConstraint_strategy = st.builds(
    LinkConstraint,
)
morel_EnclosureLinkConstraint_strategy = st.builds(
    morel_EnclosureLinkConstraint,
)
morel_PathConstraint_strategy = st.builds(
    morel_PathConstraint,
    minLength=
        st.integers(),
    maxLength=
        st.integers()
)
morel_SimpleLinkConstraint_strategy = st.builds(
    morel_SimpleLinkConstraint,
)
morel_LinkConstraint_strategy = st.builds(
    morel_LinkConstraint,
)
morel_ObjectVariable_strategy = st.builds(
    morel_ObjectVariable,
)
Section_strategy = st.builds(
    Section,
)
morel_Clause_strategy = st.builds(
    morel_Clause,
)
morel_Pattern_strategy = st.builds(
    morel_Pattern,
)
morel_Section_strategy = st.builds(
    morel_Section,
    type=
        safe_text
)
morel_NamedElement_strategy = st.builds(
    morel_NamedElement,
    name=
        safe_text
)

@given(instance=morel_PrimitiveConstraint_strategy)
@settings(max_examples=50)
def test_morel_primitiveconstraint_instantiation(instance):
    assert isinstance(instance, morel_PrimitiveConstraint)

@given(instance=AdditionalConstraint_strategy)
@settings(max_examples=50)
def test_additionalconstraint_instantiation(instance):
    assert isinstance(instance, AdditionalConstraint)

@given(instance=morel_AllDifferentConstraint_strategy)
@settings(max_examples=50)
def test_morel_alldifferentconstraint_instantiation(instance):
    assert isinstance(instance, morel_AllDifferentConstraint)

@given(instance=morel_OrderConstraint_strategy)
@settings(max_examples=50)
def test_morel_orderconstraint_instantiation(instance):
    assert isinstance(instance, morel_OrderConstraint)

@given(instance=morel_Executable_strategy)
@settings(max_examples=50)
def test_morel_executable_instantiation(instance):
    assert isinstance(instance, morel_Executable)



@given(instance=morel_Executable_strategy)
def test_morel_executable_parameters_setter(instance):
    original = instance.parameters
    instance.parameters = original
    assert instance.parameters == original



@given(instance=morel_Executable_strategy)
def test_morel_executable_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original

@given(instance=morel_EAttribute_strategy)
@settings(max_examples=50)
def test_morel_eattribute_instantiation(instance):
    assert isinstance(instance, morel_EAttribute)

@given(instance=PrimitiveConstraint_strategy)
@settings(max_examples=50)
def test_primitiveconstraint_instantiation(instance):
    assert isinstance(instance, PrimitiveConstraint)

@given(instance=morel_ValueRangeConstraint_strategy)
@settings(max_examples=50)
def test_morel_valuerangeconstraint_instantiation(instance):
    assert isinstance(instance, morel_ValueRangeConstraint)

@given(instance=morel_MultiValueConstraint_strategy)
@settings(max_examples=50)
def test_morel_multivalueconstraint_instantiation(instance):
    assert isinstance(instance, morel_MultiValueConstraint)

@given(instance=RuleElement_strategy)
@settings(max_examples=50)
def test_ruleelement_instantiation(instance):
    assert isinstance(instance, RuleElement)

@given(instance=morel_RuleGroup_strategy)
@settings(max_examples=50)
def test_morel_rulegroup_instantiation(instance):
    assert isinstance(instance, morel_RuleGroup)



@given(instance=morel_RuleGroup_strategy)
def test_morel_rulegroup_iteration_setter(instance):
    original = instance.iteration
    instance.iteration = original
    assert instance.iteration == original



@given(instance=morel_RuleGroup_strategy)
def test_morel_rulegroup_maxIteration_setter(instance):
    original = instance.maxIteration
    instance.maxIteration = original
    assert instance.maxIteration == original



@given(instance=morel_RuleGroup_strategy)
def test_morel_rulegroup_order_setter(instance):
    original = instance.order
    instance.order = original
    assert instance.order == original



@given(instance=morel_RuleGroup_strategy)
def test_morel_rulegroup_repetition_setter(instance):
    original = instance.repetition
    instance.repetition = original
    assert instance.repetition == original



@given(instance=morel_RuleGroup_strategy)
def test_morel_rulegroup_scopeSize_setter(instance):
    original = instance.scopeSize
    instance.scopeSize = original
    assert instance.scopeSize == original



@given(instance=morel_RuleGroup_strategy)
def test_morel_rulegroup_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original

@given(instance=morel_Rule_strategy)
@settings(max_examples=50)
def test_morel_rule_instantiation(instance):
    assert isinstance(instance, morel_Rule)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=morel_DeclarativeStatement_strategy)
@settings(max_examples=50)
def test_morel_declarativestatement_instantiation(instance):
    assert isinstance(instance, morel_DeclarativeStatement)

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=morel_SequenceType_strategy)
@settings(max_examples=50)
def test_morel_sequencetype_instantiation(instance):
    assert isinstance(instance, morel_SequenceType)

@given(instance=morel_SetType_strategy)
@settings(max_examples=50)
def test_morel_settype_instantiation(instance):
    assert isinstance(instance, morel_SetType)

@given(instance=morel_BagType_strategy)
@settings(max_examples=50)
def test_morel_bagtype_instantiation(instance):
    assert isinstance(instance, morel_BagType)

@given(instance=morel_OrderedSetType_strategy)
@settings(max_examples=50)
def test_morel_orderedsettype_instantiation(instance):
    assert isinstance(instance, morel_OrderedSetType)

@given(instance=EDataType_strategy)
@settings(max_examples=50)
def test_edatatype_instantiation(instance):
    assert isinstance(instance, EDataType)

@given(instance=morel_CollectionType_strategy)
@settings(max_examples=50)
def test_morel_collectiontype_instantiation(instance):
    assert isinstance(instance, morel_CollectionType)

@given(instance=morel_ImperativeStatement_strategy)
@settings(max_examples=50)
def test_morel_imperativestatement_instantiation(instance):
    assert isinstance(instance, morel_ImperativeStatement)

@given(instance=ImperativeStatement_strategy)
@settings(max_examples=50)
def test_imperativestatement_instantiation(instance):
    assert isinstance(instance, ImperativeStatement)

@given(instance=morel_BlockStatement_strategy)
@settings(max_examples=50)
def test_morel_blockstatement_instantiation(instance):
    assert isinstance(instance, morel_BlockStatement)

@given(instance=morel_ForStatement_strategy)
@settings(max_examples=50)
def test_morel_forstatement_instantiation(instance):
    assert isinstance(instance, morel_ForStatement)

@given(instance=morel_IfStatement_strategy)
@settings(max_examples=50)
def test_morel_ifstatement_instantiation(instance):
    assert isinstance(instance, morel_IfStatement)

@given(instance=BooleanAndExpChild_strategy)
@settings(max_examples=50)
def test_booleanandexpchild_instantiation(instance):
    assert isinstance(instance, BooleanAndExpChild)

@given(instance=morel_RelationalExpChild_strategy)
@settings(max_examples=50)
def test_morel_relationalexpchild_instantiation(instance):
    assert isinstance(instance, morel_RelationalExpChild)

@given(instance=morel_RelationalExp_strategy)
@settings(max_examples=50)
def test_morel_relationalexp_instantiation(instance):
    assert isinstance(instance, morel_RelationalExp)



@given(instance=morel_RelationalExp_strategy)
def test_morel_relationalexp_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=BooleanOrExpChild_strategy)
@settings(max_examples=50)
def test_booleanorexpchild_instantiation(instance):
    assert isinstance(instance, BooleanOrExpChild)

@given(instance=morel_BooleanAndExpChild_strategy)
@settings(max_examples=50)
def test_morel_booleanandexpchild_instantiation(instance):
    assert isinstance(instance, morel_BooleanAndExpChild)

@given(instance=morel_BooleanAndExp_strategy)
@settings(max_examples=50)
def test_morel_booleanandexp_instantiation(instance):
    assert isinstance(instance, morel_BooleanAndExp)



@given(instance=morel_BooleanAndExp_strategy)
def test_morel_booleanandexp_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original

@given(instance=BooleanImpliesExpChild_strategy)
@settings(max_examples=50)
def test_booleanimpliesexpchild_instantiation(instance):
    assert isinstance(instance, BooleanImpliesExpChild)

@given(instance=morel_BooleanOrExpChild_strategy)
@settings(max_examples=50)
def test_morel_booleanorexpchild_instantiation(instance):
    assert isinstance(instance, morel_BooleanOrExpChild)

@given(instance=morel_BooleanOrExp_strategy)
@settings(max_examples=50)
def test_morel_booleanorexp_instantiation(instance):
    assert isinstance(instance, morel_BooleanOrExp)



@given(instance=morel_BooleanOrExp_strategy)
def test_morel_booleanorexp_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original

@given(instance=MultiplicativeExpChild_strategy)
@settings(max_examples=50)
def test_multiplicativeexpchild_instantiation(instance):
    assert isinstance(instance, MultiplicativeExpChild)

@given(instance=morel_UnaryExpChild_strategy)
@settings(max_examples=50)
def test_morel_unaryexpchild_instantiation(instance):
    assert isinstance(instance, morel_UnaryExpChild)

@given(instance=morel_UnaryExp_strategy)
@settings(max_examples=50)
def test_morel_unaryexp_instantiation(instance):
    assert isinstance(instance, morel_UnaryExp)



@given(instance=morel_UnaryExp_strategy)
def test_morel_unaryexp_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=AdditiveExpChild_strategy)
@settings(max_examples=50)
def test_additiveexpchild_instantiation(instance):
    assert isinstance(instance, AdditiveExpChild)

@given(instance=morel_MultiplicativeExpChild_strategy)
@settings(max_examples=50)
def test_morel_multiplicativeexpchild_instantiation(instance):
    assert isinstance(instance, morel_MultiplicativeExpChild)

@given(instance=morel_MultiplicativeExp_strategy)
@settings(max_examples=50)
def test_morel_multiplicativeexp_instantiation(instance):
    assert isinstance(instance, morel_MultiplicativeExp)



@given(instance=morel_MultiplicativeExp_strategy)
def test_morel_multiplicativeexp_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original

@given(instance=RelationalExpChild_strategy)
@settings(max_examples=50)
def test_relationalexpchild_instantiation(instance):
    assert isinstance(instance, RelationalExpChild)

@given(instance=morel_AdditiveExpChild_strategy)
@settings(max_examples=50)
def test_morel_additiveexpchild_instantiation(instance):
    assert isinstance(instance, morel_AdditiveExpChild)

@given(instance=morel_AdditiveExp_strategy)
@settings(max_examples=50)
def test_morel_additiveexp_instantiation(instance):
    assert isinstance(instance, morel_AdditiveExp)



@given(instance=morel_AdditiveExp_strategy)
def test_morel_additiveexp_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original

@given(instance=ImperativeExp_strategy)
@settings(max_examples=50)
def test_imperativeexp_instantiation(instance):
    assert isinstance(instance, ImperativeExp)

@given(instance=morel_BindExp_strategy)
@settings(max_examples=50)
def test_morel_bindexp_instantiation(instance):
    assert isinstance(instance, morel_BindExp)

@given(instance=morel_PredefinedBindExp_strategy)
@settings(max_examples=50)
def test_morel_predefinedbindexp_instantiation(instance):
    assert isinstance(instance, morel_PredefinedBindExp)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=morel_ImperativeExp_strategy)
@settings(max_examples=50)
def test_morel_imperativeexp_instantiation(instance):
    assert isinstance(instance, morel_ImperativeExp)

@given(instance=morel_BooleanImpliesExpChild_strategy)
@settings(max_examples=50)
def test_morel_booleanimpliesexpchild_instantiation(instance):
    assert isinstance(instance, morel_BooleanImpliesExpChild)

@given(instance=morel_ReflectiveVariableExp_strategy)
@settings(max_examples=50)
def test_morel_reflectivevariableexp_instantiation(instance):
    assert isinstance(instance, morel_ReflectiveVariableExp)

@given(instance=morel_LetExp_strategy)
@settings(max_examples=50)
def test_morel_letexp_instantiation(instance):
    assert isinstance(instance, morel_LetExp)

@given(instance=LoopPathExp_strategy)
@settings(max_examples=50)
def test_looppathexp_instantiation(instance):
    assert isinstance(instance, LoopPathExp)

@given(instance=morel_IteratorPathExp_strategy)
@settings(max_examples=50)
def test_morel_iteratorpathexp_instantiation(instance):
    assert isinstance(instance, morel_IteratorPathExp)



@given(instance=morel_IteratorPathExp_strategy)
def test_morel_iteratorpathexp_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=morel_BooleanImpliesExp_strategy)
@settings(max_examples=50)
def test_morel_booleanimpliesexp_instantiation(instance):
    assert isinstance(instance, morel_BooleanImpliesExp)



@given(instance=morel_BooleanImpliesExp_strategy)
def test_morel_booleanimpliesexp_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=morel_ConditionExp_strategy)
@settings(max_examples=50)
def test_morel_conditionexp_instantiation(instance):
    assert isinstance(instance, morel_ConditionExp)

@given(instance=PrimitiveVariable_strategy)
@settings(max_examples=50)
def test_primitivevariable_instantiation(instance):
    assert isinstance(instance, PrimitiveVariable)

@given(instance=VariableWithInit_strategy)
@settings(max_examples=50)
def test_variablewithinit_instantiation(instance):
    assert isinstance(instance, VariableWithInit)

@given(instance=morel_PrimitiveVariableWithInit_strategy)
@settings(max_examples=50)
def test_morel_primitivevariablewithinit_instantiation(instance):
    assert isinstance(instance, morel_PrimitiveVariableWithInit)

@given(instance=ObjectVariable_strategy)
@settings(max_examples=50)
def test_objectvariable_instantiation(instance):
    assert isinstance(instance, ObjectVariable)

@given(instance=morel_ObjectVariableWithInit_strategy)
@settings(max_examples=50)
def test_morel_objectvariablewithinit_instantiation(instance):
    assert isinstance(instance, morel_ObjectVariableWithInit)

@given(instance=morel_EClassifier_strategy)
@settings(max_examples=50)
def test_morel_eclassifier_instantiation(instance):
    assert isinstance(instance, morel_EClassifier)

@given(instance=morel_EEnumLiteral_strategy)
@settings(max_examples=50)
def test_morel_eenumliteral_instantiation(instance):
    assert isinstance(instance, morel_EEnumLiteral)

@given(instance=morel_EEnum_strategy)
@settings(max_examples=50)
def test_morel_eenum_instantiation(instance):
    assert isinstance(instance, morel_EEnum)

@given(instance=CallPathExp_strategy)
@settings(max_examples=50)
def test_callpathexp_instantiation(instance):
    assert isinstance(instance, CallPathExp)

@given(instance=morel_LoopPathExp_strategy)
@settings(max_examples=50)
def test_morel_looppathexp_instantiation(instance):
    assert isinstance(instance, morel_LoopPathExp)

@given(instance=morel_OperationPathExp_strategy)
@settings(max_examples=50)
def test_morel_operationpathexp_instantiation(instance):
    assert isinstance(instance, morel_OperationPathExp)



@given(instance=morel_OperationPathExp_strategy)
def test_morel_operationpathexp_separator_setter(instance):
    original = instance.separator
    instance.separator = original
    assert instance.separator == original



@given(instance=morel_OperationPathExp_strategy)
def test_morel_operationpathexp_operation_setter(instance):
    original = instance.operation
    instance.operation = original
    assert instance.operation == original

@given(instance=morel_FeaturePathExp_strategy)
@settings(max_examples=50)
def test_morel_featurepathexp_instantiation(instance):
    assert isinstance(instance, morel_FeaturePathExp)



@given(instance=morel_FeaturePathExp_strategy)
def test_morel_featurepathexp_feature_setter(instance):
    original = instance.feature
    instance.feature = original
    assert instance.feature == original

@given(instance=morel_Unit_strategy)
@settings(max_examples=50)
def test_morel_unit_instantiation(instance):
    assert isinstance(instance, morel_Unit)

@given(instance=Executable_strategy)
@settings(max_examples=50)
def test_executable_instantiation(instance):
    assert isinstance(instance, Executable)

@given(instance=Pattern_strategy)
@settings(max_examples=50)
def test_pattern_instantiation(instance):
    assert isinstance(instance, Pattern)

@given(instance=morel_EPackage_strategy)
@settings(max_examples=50)
def test_morel_epackage_instantiation(instance):
    assert isinstance(instance, morel_EPackage)

@given(instance=Unit_strategy)
@settings(max_examples=50)
def test_unit_instantiation(instance):
    assert isinstance(instance, Unit)

@given(instance=morel_QueryModel_strategy)
@settings(max_examples=50)
def test_morel_querymodel_instantiation(instance):
    assert isinstance(instance, morel_QueryModel)

@given(instance=LiteralExp_strategy)
@settings(max_examples=50)
def test_literalexp_instantiation(instance):
    assert isinstance(instance, LiteralExp)

@given(instance=morel_RealLiteralExp_strategy)
@settings(max_examples=50)
def test_morel_realliteralexp_instantiation(instance):
    assert isinstance(instance, morel_RealLiteralExp)



@given(instance=morel_RealLiteralExp_strategy)
def test_morel_realliteralexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=morel_UndefinedLiteralExp_strategy)
@settings(max_examples=50)
def test_morel_undefinedliteralexp_instantiation(instance):
    assert isinstance(instance, morel_UndefinedLiteralExp)



@given(instance=morel_UndefinedLiteralExp_strategy)
def test_morel_undefinedliteralexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=morel_CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_morel_collectionliteralexp_instantiation(instance):
    assert isinstance(instance, morel_CollectionLiteralExp)



@given(instance=morel_CollectionLiteralExp_strategy)
def test_morel_collectionliteralexp_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=morel_BooleanLiteralExp_strategy)
@settings(max_examples=50)
def test_morel_booleanliteralexp_instantiation(instance):
    assert isinstance(instance, morel_BooleanLiteralExp)



@given(instance=morel_BooleanLiteralExp_strategy)
def test_morel_booleanliteralexp_boolSymbol_setter(instance):
    original = instance.boolSymbol
    instance.boolSymbol = original
    assert instance.boolSymbol == original

@given(instance=morel_IntegerLiteralExp_strategy)
@settings(max_examples=50)
def test_morel_integerliteralexp_instantiation(instance):
    assert isinstance(instance, morel_IntegerLiteralExp)



@given(instance=morel_IntegerLiteralExp_strategy)
def test_morel_integerliteralexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=morel_ArrayLiteralExp_strategy)
@settings(max_examples=50)
def test_morel_arrayliteralexp_instantiation(instance):
    assert isinstance(instance, morel_ArrayLiteralExp)

@given(instance=morel_EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_morel_enumliteralexp_instantiation(instance):
    assert isinstance(instance, morel_EnumLiteralExp)

@given(instance=morel_TypeLiteralExp_strategy)
@settings(max_examples=50)
def test_morel_typeliteralexp_instantiation(instance):
    assert isinstance(instance, morel_TypeLiteralExp)

@given(instance=morel_StringLiteralExp_strategy)
@settings(max_examples=50)
def test_morel_stringliteralexp_instantiation(instance):
    assert isinstance(instance, morel_StringLiteralExp)



@given(instance=morel_StringLiteralExp_strategy)
def test_morel_stringliteralexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=AtomicExp_strategy)
@settings(max_examples=50)
def test_atomicexp_instantiation(instance):
    assert isinstance(instance, AtomicExp)

@given(instance=morel_VariableExp_strategy)
@settings(max_examples=50)
def test_morel_variableexp_instantiation(instance):
    assert isinstance(instance, morel_VariableExp)

@given(instance=morel_PredefinedVariableExp_strategy)
@settings(max_examples=50)
def test_morel_predefinedvariableexp_instantiation(instance):
    assert isinstance(instance, morel_PredefinedVariableExp)



@given(instance=morel_PredefinedVariableExp_strategy)
def test_morel_predefinedvariableexp_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=morel_NestedExp_strategy)
@settings(max_examples=50)
def test_morel_nestedexp_instantiation(instance):
    assert isinstance(instance, morel_NestedExp)

@given(instance=morel_LiteralExp_strategy)
@settings(max_examples=50)
def test_morel_literalexp_instantiation(instance):
    assert isinstance(instance, morel_LiteralExp)

@given(instance=morel_CallPathExp_strategy)
@settings(max_examples=50)
def test_morel_callpathexp_instantiation(instance):
    assert isinstance(instance, morel_CallPathExp)

@given(instance=UnaryExpChild_strategy)
@settings(max_examples=50)
def test_unaryexpchild_instantiation(instance):
    assert isinstance(instance, UnaryExpChild)

@given(instance=morel_AtomicExp_strategy)
@settings(max_examples=50)
def test_morel_atomicexp_instantiation(instance):
    assert isinstance(instance, morel_AtomicExp)

@given(instance=morel_EDataType_strategy)
@settings(max_examples=50)
def test_morel_edatatype_instantiation(instance):
    assert isinstance(instance, morel_EDataType)

@given(instance=morel_EClass_strategy)
@settings(max_examples=50)
def test_morel_eclass_instantiation(instance):
    assert isinstance(instance, morel_EClass)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=morel_PrimitiveVariable_strategy)
@settings(max_examples=50)
def test_morel_primitivevariable_instantiation(instance):
    assert isinstance(instance, morel_PrimitiveVariable)

@given(instance=morel_VariableWithInit_strategy)
@settings(max_examples=50)
def test_morel_variablewithinit_instantiation(instance):
    assert isinstance(instance, morel_VariableWithInit)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=morel_RuleElement_strategy)
@settings(max_examples=50)
def test_morel_ruleelement_instantiation(instance):
    assert isinstance(instance, morel_RuleElement)

@given(instance=morel_TypedModel_strategy)
@settings(max_examples=50)
def test_morel_typedmodel_instantiation(instance):
    assert isinstance(instance, morel_TypedModel)



@given(instance=morel_TypedModel_strategy)
def test_morel_typedmodel_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=morel_TransformationModel_strategy)
@settings(max_examples=50)
def test_morel_transformationmodel_instantiation(instance):
    assert isinstance(instance, morel_TransformationModel)

@given(instance=morel_Query_strategy)
@settings(max_examples=50)
def test_morel_query_instantiation(instance):
    assert isinstance(instance, morel_Query)

@given(instance=morel_Variable_strategy)
@settings(max_examples=50)
def test_morel_variable_instantiation(instance):
    assert isinstance(instance, morel_Variable)

@given(instance=morel_AdditionalConstraint_strategy)
@settings(max_examples=50)
def test_morel_additionalconstraint_instantiation(instance):
    assert isinstance(instance, morel_AdditionalConstraint)

@given(instance=morel_Statement_strategy)
@settings(max_examples=50)
def test_morel_statement_instantiation(instance):
    assert isinstance(instance, morel_Statement)

@given(instance=morel_EReference_strategy)
@settings(max_examples=50)
def test_morel_ereference_instantiation(instance):
    assert isinstance(instance, morel_EReference)

@given(instance=morel_Expression_strategy)
@settings(max_examples=50)
def test_morel_expression_instantiation(instance):
    assert isinstance(instance, morel_Expression)

@given(instance=LinkConstraint_strategy)
@settings(max_examples=50)
def test_linkconstraint_instantiation(instance):
    assert isinstance(instance, LinkConstraint)

@given(instance=morel_EnclosureLinkConstraint_strategy)
@settings(max_examples=50)
def test_morel_enclosurelinkconstraint_instantiation(instance):
    assert isinstance(instance, morel_EnclosureLinkConstraint)

@given(instance=morel_PathConstraint_strategy)
@settings(max_examples=50)
def test_morel_pathconstraint_instantiation(instance):
    assert isinstance(instance, morel_PathConstraint)



@given(instance=morel_PathConstraint_strategy)
def test_morel_pathconstraint_minLength_setter(instance):
    original = instance.minLength
    instance.minLength = original
    assert instance.minLength == original



@given(instance=morel_PathConstraint_strategy)
def test_morel_pathconstraint_maxLength_setter(instance):
    original = instance.maxLength
    instance.maxLength = original
    assert instance.maxLength == original

@given(instance=morel_SimpleLinkConstraint_strategy)
@settings(max_examples=50)
def test_morel_simplelinkconstraint_instantiation(instance):
    assert isinstance(instance, morel_SimpleLinkConstraint)

@given(instance=morel_LinkConstraint_strategy)
@settings(max_examples=50)
def test_morel_linkconstraint_instantiation(instance):
    assert isinstance(instance, morel_LinkConstraint)

@given(instance=morel_ObjectVariable_strategy)
@settings(max_examples=50)
def test_morel_objectvariable_instantiation(instance):
    assert isinstance(instance, morel_ObjectVariable)

@given(instance=Section_strategy)
@settings(max_examples=50)
def test_section_instantiation(instance):
    assert isinstance(instance, Section)

@given(instance=morel_Clause_strategy)
@settings(max_examples=50)
def test_morel_clause_instantiation(instance):
    assert isinstance(instance, morel_Clause)

@given(instance=morel_Pattern_strategy)
@settings(max_examples=50)
def test_morel_pattern_instantiation(instance):
    assert isinstance(instance, morel_Pattern)

@given(instance=morel_Section_strategy)
@settings(max_examples=50)
def test_morel_section_instantiation(instance):
    assert isinstance(instance, morel_Section)



@given(instance=morel_Section_strategy)
def test_morel_section_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=morel_NamedElement_strategy)
@settings(max_examples=50)
def test_morel_namedelement_instantiation(instance):
    assert isinstance(instance, morel_NamedElement)



@given(instance=morel_NamedElement_strategy)
def test_morel_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
