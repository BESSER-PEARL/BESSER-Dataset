import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    morel::PrimitiveConstraint,
    AdditionalConstraint,
    morel::AllDifferentConstraint,
    morel::OrderConstraint,
    morel::Executable,
    morel::EAttribute,
    PrimitiveConstraint,
    morel::ValueRangeConstraint,
    morel::MultiValueConstraint,
    RuleElement,
    morel::RuleGroup,
    morel::Rule,
    Statement,
    morel::DeclarativeStatement,
    CollectionType,
    morel::BagType,
    morel::SetType,
    morel::SequenceType,
    morel::OrderedSetType,
    EDataType,
    morel::CollectionType,
    morel::ImperativeStatement,
    ImperativeStatement,
    morel::ForStatement,
    morel::BlockStatement,
    morel::IfStatement,
    BooleanAndExpChild,
    morel::RelationalExpChild,
    morel::RelationalExp,
    BooleanOrExpChild,
    morel::BooleanAndExpChild,
    morel::BooleanAndExp,
    BooleanImpliesExpChild,
    morel::BooleanOrExpChild,
    morel::BooleanOrExp,
    MultiplicativeExpChild,
    morel::UnaryExpChild,
    morel::UnaryExp,
    AdditiveExpChild,
    morel::MultiplicativeExpChild,
    morel::MultiplicativeExp,
    RelationalExpChild,
    morel::AdditiveExpChild,
    morel::AdditiveExp,
    ImperativeExp,
    morel::PredefinedBindExp,
    morel::BindExp,
    Expression,
    morel::BooleanImpliesExpChild,
    morel::ReflectiveVariableExp,
    morel::ImperativeExp,
    morel::LetExp,
    LoopPathExp,
    morel::IteratorPathExp,
    morel::BooleanImpliesExp,
    morel::ConditionExp,
    PrimitiveVariable,
    VariableWithInit,
    morel::PrimitiveVariableWithInit,
    ObjectVariable,
    morel::ObjectVariableWithInit,
    morel::EClassifier,
    morel::EEnumLiteral,
    morel::EEnum,
    CallPathExp,
    morel::OperationPathExp,
    morel::LoopPathExp,
    morel::FeaturePathExp,
    morel::Unit,
    Executable,
    Pattern,
    morel::EPackage,
    Unit,
    morel::QueryModel,
    LiteralExp,
    morel::IntegerLiteralExp,
    morel::TypeLiteralExp,
    morel::EnumLiteralExp,
    morel::UndefinedLiteralExp,
    morel::BooleanLiteralExp,
    morel::CollectionLiteralExp,
    morel::RealLiteralExp,
    morel::ArrayLiteralExp,
    morel::StringLiteralExp,
    AtomicExp,
    morel::VariableExp,
    morel::NestedExp,
    morel::PredefinedVariableExp,
    morel::LiteralExp,
    morel::CallPathExp,
    UnaryExpChild,
    morel::AtomicExp,
    morel::EDataType,
    morel::EClass,
    Variable,
    morel::PrimitiveVariable,
    morel::VariableWithInit,
    NamedElement,
    morel::TransformationModel,
    morel::Query,
    morel::RuleElement,
    morel::TypedModel,
    morel::Variable,
    morel::AdditionalConstraint,
    morel::Statement,
    morel::EReference,
    morel::Expression,
    LinkConstraint,
    morel::PathConstraint,
    morel::EnclosureLinkConstraint,
    morel::SimpleLinkConstraint,
    morel::LinkConstraint,
    morel::ObjectVariable,
    Section,
    morel::Clause,
    morel::Pattern,
    morel::Section,
    morel::NamedElement,
    IteratorType,
    UnaryOperator,
    BooleanOperator,
    RepetitionType,
    RelationalOperator,
    OrderType,
    ScopeType,
    TypedModelAction,
    SectionType,
    IterationType,
    AdditiveOperator,
    UndefinedLiteral,
    PredefinedVariable,
    MultiplicativeOperator,
    OperationSeparator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_morel::primitiveconstraint_is_not_abstract():
    assert not inspect.isabstract(morel::PrimitiveConstraint)


def test_morel::primitiveconstraint_constructor_exists():
    assert callable(morel::PrimitiveConstraint.__init__)


def test_morel::primitiveconstraint_constructor_args():
    sig = inspect.signature(morel::PrimitiveConstraint.__init__)
    params = list(sig.parameters.keys())



def test_additionalconstraint_is_not_abstract():
    assert not inspect.isabstract(AdditionalConstraint)


def test_additionalconstraint_constructor_exists():
    assert callable(AdditionalConstraint.__init__)


def test_additionalconstraint_constructor_args():
    sig = inspect.signature(AdditionalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_morel::alldifferentconstraint_is_not_abstract():
    assert not inspect.isabstract(morel::AllDifferentConstraint)


def test_morel::alldifferentconstraint_constructor_exists():
    assert callable(morel::AllDifferentConstraint.__init__)


def test_morel::alldifferentconstraint_constructor_args():
    sig = inspect.signature(morel::AllDifferentConstraint.__init__)
    params = list(sig.parameters.keys())



def test_morel::orderconstraint_is_not_abstract():
    assert not inspect.isabstract(morel::OrderConstraint)


def test_morel::orderconstraint_constructor_exists():
    assert callable(morel::OrderConstraint.__init__)


def test_morel::orderconstraint_constructor_args():
    sig = inspect.signature(morel::OrderConstraint.__init__)
    params = list(sig.parameters.keys())



def test_morel::executable_is_not_abstract():
    assert not inspect.isabstract(morel::Executable)


def test_morel::executable_constructor_exists():
    assert callable(morel::Executable.__init__)


def test_morel::executable_constructor_args():
    sig = inspect.signature(morel::Executable.__init__)
    params = list(sig.parameters.keys())
    assert "active" in params, "Missing parameter 'active'"
    assert "parameters" in params, "Missing parameter 'parameters'"

def test_morel::executable_has_active():
    assert hasattr(morel::Executable, "active")
    descriptor = None
    for klass in morel::Executable.__mro__:
        if "active" in klass.__dict__:
            descriptor = klass.__dict__["active"]
            break
    assert isinstance(descriptor, property)

def test_morel::executable_has_parameters():
    assert hasattr(morel::Executable, "parameters")
    descriptor = None
    for klass in morel::Executable.__mro__:
        if "parameters" in klass.__dict__:
            descriptor = klass.__dict__["parameters"]
            break
    assert isinstance(descriptor, property)



def test_morel::eattribute_is_not_abstract():
    assert not inspect.isabstract(morel::EAttribute)


def test_morel::eattribute_constructor_exists():
    assert callable(morel::EAttribute.__init__)


def test_morel::eattribute_constructor_args():
    sig = inspect.signature(morel::EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_primitiveconstraint_is_not_abstract():
    assert not inspect.isabstract(PrimitiveConstraint)


def test_primitiveconstraint_constructor_exists():
    assert callable(PrimitiveConstraint.__init__)


def test_primitiveconstraint_constructor_args():
    sig = inspect.signature(PrimitiveConstraint.__init__)
    params = list(sig.parameters.keys())



def test_morel::valuerangeconstraint_is_not_abstract():
    assert not inspect.isabstract(morel::ValueRangeConstraint)


def test_morel::valuerangeconstraint_constructor_exists():
    assert callable(morel::ValueRangeConstraint.__init__)


def test_morel::valuerangeconstraint_constructor_args():
    sig = inspect.signature(morel::ValueRangeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_morel::multivalueconstraint_is_not_abstract():
    assert not inspect.isabstract(morel::MultiValueConstraint)


def test_morel::multivalueconstraint_constructor_exists():
    assert callable(morel::MultiValueConstraint.__init__)


def test_morel::multivalueconstraint_constructor_args():
    sig = inspect.signature(morel::MultiValueConstraint.__init__)
    params = list(sig.parameters.keys())



def test_ruleelement_is_not_abstract():
    assert not inspect.isabstract(RuleElement)


def test_ruleelement_constructor_exists():
    assert callable(RuleElement.__init__)


def test_ruleelement_constructor_args():
    sig = inspect.signature(RuleElement.__init__)
    params = list(sig.parameters.keys())



def test_morel::rulegroup_is_not_abstract():
    assert not inspect.isabstract(morel::RuleGroup)


def test_morel::rulegroup_constructor_exists():
    assert callable(morel::RuleGroup.__init__)


def test_morel::rulegroup_constructor_args():
    sig = inspect.signature(morel::RuleGroup.__init__)
    params = list(sig.parameters.keys())
    assert "scope" in params, "Missing parameter 'scope'"
    assert "scopeSize" in params, "Missing parameter 'scopeSize'"
    assert "repetition" in params, "Missing parameter 'repetition'"
    assert "maxIteration" in params, "Missing parameter 'maxIteration'"
    assert "order" in params, "Missing parameter 'order'"
    assert "iteration" in params, "Missing parameter 'iteration'"

def test_morel::rulegroup_has_scope():
    assert hasattr(morel::RuleGroup, "scope")
    descriptor = None
    for klass in morel::RuleGroup.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)

def test_morel::rulegroup_has_scopeSize():
    assert hasattr(morel::RuleGroup, "scopeSize")
    descriptor = None
    for klass in morel::RuleGroup.__mro__:
        if "scopeSize" in klass.__dict__:
            descriptor = klass.__dict__["scopeSize"]
            break
    assert isinstance(descriptor, property)

def test_morel::rulegroup_has_repetition():
    assert hasattr(morel::RuleGroup, "repetition")
    descriptor = None
    for klass in morel::RuleGroup.__mro__:
        if "repetition" in klass.__dict__:
            descriptor = klass.__dict__["repetition"]
            break
    assert isinstance(descriptor, property)

def test_morel::rulegroup_has_maxIteration():
    assert hasattr(morel::RuleGroup, "maxIteration")
    descriptor = None
    for klass in morel::RuleGroup.__mro__:
        if "maxIteration" in klass.__dict__:
            descriptor = klass.__dict__["maxIteration"]
            break
    assert isinstance(descriptor, property)

def test_morel::rulegroup_has_order():
    assert hasattr(morel::RuleGroup, "order")
    descriptor = None
    for klass in morel::RuleGroup.__mro__:
        if "order" in klass.__dict__:
            descriptor = klass.__dict__["order"]
            break
    assert isinstance(descriptor, property)

def test_morel::rulegroup_has_iteration():
    assert hasattr(morel::RuleGroup, "iteration")
    descriptor = None
    for klass in morel::RuleGroup.__mro__:
        if "iteration" in klass.__dict__:
            descriptor = klass.__dict__["iteration"]
            break
    assert isinstance(descriptor, property)



def test_morel::rule_is_not_abstract():
    assert not inspect.isabstract(morel::Rule)


def test_morel::rule_constructor_exists():
    assert callable(morel::Rule.__init__)


def test_morel::rule_constructor_args():
    sig = inspect.signature(morel::Rule.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_morel::declarativestatement_is_not_abstract():
    assert not inspect.isabstract(morel::DeclarativeStatement)


def test_morel::declarativestatement_constructor_exists():
    assert callable(morel::DeclarativeStatement.__init__)


def test_morel::declarativestatement_constructor_args():
    sig = inspect.signature(morel::DeclarativeStatement.__init__)
    params = list(sig.parameters.keys())



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_morel::bagtype_is_not_abstract():
    assert not inspect.isabstract(morel::BagType)


def test_morel::bagtype_constructor_exists():
    assert callable(morel::BagType.__init__)


def test_morel::bagtype_constructor_args():
    sig = inspect.signature(morel::BagType.__init__)
    params = list(sig.parameters.keys())



def test_morel::settype_is_not_abstract():
    assert not inspect.isabstract(morel::SetType)


def test_morel::settype_constructor_exists():
    assert callable(morel::SetType.__init__)


def test_morel::settype_constructor_args():
    sig = inspect.signature(morel::SetType.__init__)
    params = list(sig.parameters.keys())



def test_morel::sequencetype_is_not_abstract():
    assert not inspect.isabstract(morel::SequenceType)


def test_morel::sequencetype_constructor_exists():
    assert callable(morel::SequenceType.__init__)


def test_morel::sequencetype_constructor_args():
    sig = inspect.signature(morel::SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_morel::orderedsettype_is_not_abstract():
    assert not inspect.isabstract(morel::OrderedSetType)


def test_morel::orderedsettype_constructor_exists():
    assert callable(morel::OrderedSetType.__init__)


def test_morel::orderedsettype_constructor_args():
    sig = inspect.signature(morel::OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_edatatype_is_not_abstract():
    assert not inspect.isabstract(EDataType)


def test_edatatype_constructor_exists():
    assert callable(EDataType.__init__)


def test_edatatype_constructor_args():
    sig = inspect.signature(EDataType.__init__)
    params = list(sig.parameters.keys())



def test_morel::collectiontype_is_not_abstract():
    assert not inspect.isabstract(morel::CollectionType)


def test_morel::collectiontype_constructor_exists():
    assert callable(morel::CollectionType.__init__)


def test_morel::collectiontype_constructor_args():
    sig = inspect.signature(morel::CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_morel::imperativestatement_is_not_abstract():
    assert not inspect.isabstract(morel::ImperativeStatement)


def test_morel::imperativestatement_constructor_exists():
    assert callable(morel::ImperativeStatement.__init__)


def test_morel::imperativestatement_constructor_args():
    sig = inspect.signature(morel::ImperativeStatement.__init__)
    params = list(sig.parameters.keys())



def test_imperativestatement_is_not_abstract():
    assert not inspect.isabstract(ImperativeStatement)


def test_imperativestatement_constructor_exists():
    assert callable(ImperativeStatement.__init__)


def test_imperativestatement_constructor_args():
    sig = inspect.signature(ImperativeStatement.__init__)
    params = list(sig.parameters.keys())



def test_morel::forstatement_is_not_abstract():
    assert not inspect.isabstract(morel::ForStatement)


def test_morel::forstatement_constructor_exists():
    assert callable(morel::ForStatement.__init__)


def test_morel::forstatement_constructor_args():
    sig = inspect.signature(morel::ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_morel::blockstatement_is_not_abstract():
    assert not inspect.isabstract(morel::BlockStatement)


def test_morel::blockstatement_constructor_exists():
    assert callable(morel::BlockStatement.__init__)


def test_morel::blockstatement_constructor_args():
    sig = inspect.signature(morel::BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_morel::ifstatement_is_not_abstract():
    assert not inspect.isabstract(morel::IfStatement)


def test_morel::ifstatement_constructor_exists():
    assert callable(morel::IfStatement.__init__)


def test_morel::ifstatement_constructor_args():
    sig = inspect.signature(morel::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_booleanandexpchild_is_not_abstract():
    assert not inspect.isabstract(BooleanAndExpChild)


def test_booleanandexpchild_constructor_exists():
    assert callable(BooleanAndExpChild.__init__)


def test_booleanandexpchild_constructor_args():
    sig = inspect.signature(BooleanAndExpChild.__init__)
    params = list(sig.parameters.keys())



def test_morel::relationalexpchild_is_not_abstract():
    assert not inspect.isabstract(morel::RelationalExpChild)


def test_morel::relationalexpchild_constructor_exists():
    assert callable(morel::RelationalExpChild.__init__)


def test_morel::relationalexpchild_constructor_args():
    sig = inspect.signature(morel::RelationalExpChild.__init__)
    params = list(sig.parameters.keys())



def test_morel::relationalexp_is_not_abstract():
    assert not inspect.isabstract(morel::RelationalExp)


def test_morel::relationalexp_constructor_exists():
    assert callable(morel::RelationalExp.__init__)


def test_morel::relationalexp_constructor_args():
    sig = inspect.signature(morel::RelationalExp.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_morel::relationalexp_has_operator():
    assert hasattr(morel::RelationalExp, "operator")
    descriptor = None
    for klass in morel::RelationalExp.__mro__:
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



def test_morel::booleanandexpchild_is_not_abstract():
    assert not inspect.isabstract(morel::BooleanAndExpChild)


def test_morel::booleanandexpchild_constructor_exists():
    assert callable(morel::BooleanAndExpChild.__init__)


def test_morel::booleanandexpchild_constructor_args():
    sig = inspect.signature(morel::BooleanAndExpChild.__init__)
    params = list(sig.parameters.keys())



def test_morel::booleanandexp_is_not_abstract():
    assert not inspect.isabstract(morel::BooleanAndExp)


def test_morel::booleanandexp_constructor_exists():
    assert callable(morel::BooleanAndExp.__init__)


def test_morel::booleanandexp_constructor_args():
    sig = inspect.signature(morel::BooleanAndExp.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"

def test_morel::booleanandexp_has_operators():
    assert hasattr(morel::BooleanAndExp, "operators")
    descriptor = None
    for klass in morel::BooleanAndExp.__mro__:
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



def test_morel::booleanorexpchild_is_not_abstract():
    assert not inspect.isabstract(morel::BooleanOrExpChild)


def test_morel::booleanorexpchild_constructor_exists():
    assert callable(morel::BooleanOrExpChild.__init__)


def test_morel::booleanorexpchild_constructor_args():
    sig = inspect.signature(morel::BooleanOrExpChild.__init__)
    params = list(sig.parameters.keys())



def test_morel::booleanorexp_is_not_abstract():
    assert not inspect.isabstract(morel::BooleanOrExp)


def test_morel::booleanorexp_constructor_exists():
    assert callable(morel::BooleanOrExp.__init__)


def test_morel::booleanorexp_constructor_args():
    sig = inspect.signature(morel::BooleanOrExp.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"

def test_morel::booleanorexp_has_operators():
    assert hasattr(morel::BooleanOrExp, "operators")
    descriptor = None
    for klass in morel::BooleanOrExp.__mro__:
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



def test_morel::unaryexpchild_is_not_abstract():
    assert not inspect.isabstract(morel::UnaryExpChild)


def test_morel::unaryexpchild_constructor_exists():
    assert callable(morel::UnaryExpChild.__init__)


def test_morel::unaryexpchild_constructor_args():
    sig = inspect.signature(morel::UnaryExpChild.__init__)
    params = list(sig.parameters.keys())



def test_morel::unaryexp_is_not_abstract():
    assert not inspect.isabstract(morel::UnaryExp)


def test_morel::unaryexp_constructor_exists():
    assert callable(morel::UnaryExp.__init__)


def test_morel::unaryexp_constructor_args():
    sig = inspect.signature(morel::UnaryExp.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_morel::unaryexp_has_operator():
    assert hasattr(morel::UnaryExp, "operator")
    descriptor = None
    for klass in morel::UnaryExp.__mro__:
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



def test_morel::multiplicativeexpchild_is_not_abstract():
    assert not inspect.isabstract(morel::MultiplicativeExpChild)


def test_morel::multiplicativeexpchild_constructor_exists():
    assert callable(morel::MultiplicativeExpChild.__init__)


def test_morel::multiplicativeexpchild_constructor_args():
    sig = inspect.signature(morel::MultiplicativeExpChild.__init__)
    params = list(sig.parameters.keys())



def test_morel::multiplicativeexp_is_not_abstract():
    assert not inspect.isabstract(morel::MultiplicativeExp)


def test_morel::multiplicativeexp_constructor_exists():
    assert callable(morel::MultiplicativeExp.__init__)


def test_morel::multiplicativeexp_constructor_args():
    sig = inspect.signature(morel::MultiplicativeExp.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"

def test_morel::multiplicativeexp_has_operators():
    assert hasattr(morel::MultiplicativeExp, "operators")
    descriptor = None
    for klass in morel::MultiplicativeExp.__mro__:
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



def test_morel::additiveexpchild_is_not_abstract():
    assert not inspect.isabstract(morel::AdditiveExpChild)


def test_morel::additiveexpchild_constructor_exists():
    assert callable(morel::AdditiveExpChild.__init__)


def test_morel::additiveexpchild_constructor_args():
    sig = inspect.signature(morel::AdditiveExpChild.__init__)
    params = list(sig.parameters.keys())



def test_morel::additiveexp_is_not_abstract():
    assert not inspect.isabstract(morel::AdditiveExp)


def test_morel::additiveexp_constructor_exists():
    assert callable(morel::AdditiveExp.__init__)


def test_morel::additiveexp_constructor_args():
    sig = inspect.signature(morel::AdditiveExp.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"

def test_morel::additiveexp_has_operators():
    assert hasattr(morel::AdditiveExp, "operators")
    descriptor = None
    for klass in morel::AdditiveExp.__mro__:
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



def test_morel::predefinedbindexp_is_not_abstract():
    assert not inspect.isabstract(morel::PredefinedBindExp)


def test_morel::predefinedbindexp_constructor_exists():
    assert callable(morel::PredefinedBindExp.__init__)


def test_morel::predefinedbindexp_constructor_args():
    sig = inspect.signature(morel::PredefinedBindExp.__init__)
    params = list(sig.parameters.keys())



def test_morel::bindexp_is_not_abstract():
    assert not inspect.isabstract(morel::BindExp)


def test_morel::bindexp_constructor_exists():
    assert callable(morel::BindExp.__init__)


def test_morel::bindexp_constructor_args():
    sig = inspect.signature(morel::BindExp.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_morel::booleanimpliesexpchild_is_not_abstract():
    assert not inspect.isabstract(morel::BooleanImpliesExpChild)


def test_morel::booleanimpliesexpchild_constructor_exists():
    assert callable(morel::BooleanImpliesExpChild.__init__)


def test_morel::booleanimpliesexpchild_constructor_args():
    sig = inspect.signature(morel::BooleanImpliesExpChild.__init__)
    params = list(sig.parameters.keys())



def test_morel::reflectivevariableexp_is_not_abstract():
    assert not inspect.isabstract(morel::ReflectiveVariableExp)


def test_morel::reflectivevariableexp_constructor_exists():
    assert callable(morel::ReflectiveVariableExp.__init__)


def test_morel::reflectivevariableexp_constructor_args():
    sig = inspect.signature(morel::ReflectiveVariableExp.__init__)
    params = list(sig.parameters.keys())



def test_morel::imperativeexp_is_not_abstract():
    assert not inspect.isabstract(morel::ImperativeExp)


def test_morel::imperativeexp_constructor_exists():
    assert callable(morel::ImperativeExp.__init__)


def test_morel::imperativeexp_constructor_args():
    sig = inspect.signature(morel::ImperativeExp.__init__)
    params = list(sig.parameters.keys())



def test_morel::letexp_is_not_abstract():
    assert not inspect.isabstract(morel::LetExp)


def test_morel::letexp_constructor_exists():
    assert callable(morel::LetExp.__init__)


def test_morel::letexp_constructor_args():
    sig = inspect.signature(morel::LetExp.__init__)
    params = list(sig.parameters.keys())



def test_looppathexp_is_not_abstract():
    assert not inspect.isabstract(LoopPathExp)


def test_looppathexp_constructor_exists():
    assert callable(LoopPathExp.__init__)


def test_looppathexp_constructor_args():
    sig = inspect.signature(LoopPathExp.__init__)
    params = list(sig.parameters.keys())



def test_morel::iteratorpathexp_is_not_abstract():
    assert not inspect.isabstract(morel::IteratorPathExp)


def test_morel::iteratorpathexp_constructor_exists():
    assert callable(morel::IteratorPathExp.__init__)


def test_morel::iteratorpathexp_constructor_args():
    sig = inspect.signature(morel::IteratorPathExp.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_morel::iteratorpathexp_has_type():
    assert hasattr(morel::IteratorPathExp, "type")
    descriptor = None
    for klass in morel::IteratorPathExp.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_morel::booleanimpliesexp_is_not_abstract():
    assert not inspect.isabstract(morel::BooleanImpliesExp)


def test_morel::booleanimpliesexp_constructor_exists():
    assert callable(morel::BooleanImpliesExp.__init__)


def test_morel::booleanimpliesexp_constructor_args():
    sig = inspect.signature(morel::BooleanImpliesExp.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_morel::booleanimpliesexp_has_operator():
    assert hasattr(morel::BooleanImpliesExp, "operator")
    descriptor = None
    for klass in morel::BooleanImpliesExp.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_morel::conditionexp_is_not_abstract():
    assert not inspect.isabstract(morel::ConditionExp)


def test_morel::conditionexp_constructor_exists():
    assert callable(morel::ConditionExp.__init__)


def test_morel::conditionexp_constructor_args():
    sig = inspect.signature(morel::ConditionExp.__init__)
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



def test_morel::primitivevariablewithinit_is_not_abstract():
    assert not inspect.isabstract(morel::PrimitiveVariableWithInit)


def test_morel::primitivevariablewithinit_constructor_exists():
    assert callable(morel::PrimitiveVariableWithInit.__init__)


def test_morel::primitivevariablewithinit_constructor_args():
    sig = inspect.signature(morel::PrimitiveVariableWithInit.__init__)
    params = list(sig.parameters.keys())



def test_objectvariable_is_not_abstract():
    assert not inspect.isabstract(ObjectVariable)


def test_objectvariable_constructor_exists():
    assert callable(ObjectVariable.__init__)


def test_objectvariable_constructor_args():
    sig = inspect.signature(ObjectVariable.__init__)
    params = list(sig.parameters.keys())



def test_morel::objectvariablewithinit_is_not_abstract():
    assert not inspect.isabstract(morel::ObjectVariableWithInit)


def test_morel::objectvariablewithinit_constructor_exists():
    assert callable(morel::ObjectVariableWithInit.__init__)


def test_morel::objectvariablewithinit_constructor_args():
    sig = inspect.signature(morel::ObjectVariableWithInit.__init__)
    params = list(sig.parameters.keys())



def test_morel::eclassifier_is_not_abstract():
    assert not inspect.isabstract(morel::EClassifier)


def test_morel::eclassifier_constructor_exists():
    assert callable(morel::EClassifier.__init__)


def test_morel::eclassifier_constructor_args():
    sig = inspect.signature(morel::EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_morel::eenumliteral_is_not_abstract():
    assert not inspect.isabstract(morel::EEnumLiteral)


def test_morel::eenumliteral_constructor_exists():
    assert callable(morel::EEnumLiteral.__init__)


def test_morel::eenumliteral_constructor_args():
    sig = inspect.signature(morel::EEnumLiteral.__init__)
    params = list(sig.parameters.keys())



def test_morel::eenum_is_not_abstract():
    assert not inspect.isabstract(morel::EEnum)


def test_morel::eenum_constructor_exists():
    assert callable(morel::EEnum.__init__)


def test_morel::eenum_constructor_args():
    sig = inspect.signature(morel::EEnum.__init__)
    params = list(sig.parameters.keys())



def test_callpathexp_is_not_abstract():
    assert not inspect.isabstract(CallPathExp)


def test_callpathexp_constructor_exists():
    assert callable(CallPathExp.__init__)


def test_callpathexp_constructor_args():
    sig = inspect.signature(CallPathExp.__init__)
    params = list(sig.parameters.keys())



def test_morel::operationpathexp_is_not_abstract():
    assert not inspect.isabstract(morel::OperationPathExp)


def test_morel::operationpathexp_constructor_exists():
    assert callable(morel::OperationPathExp.__init__)


def test_morel::operationpathexp_constructor_args():
    sig = inspect.signature(morel::OperationPathExp.__init__)
    params = list(sig.parameters.keys())
    assert "separator" in params, "Missing parameter 'separator'"
    assert "operation" in params, "Missing parameter 'operation'"

def test_morel::operationpathexp_has_separator():
    assert hasattr(morel::OperationPathExp, "separator")
    descriptor = None
    for klass in morel::OperationPathExp.__mro__:
        if "separator" in klass.__dict__:
            descriptor = klass.__dict__["separator"]
            break
    assert isinstance(descriptor, property)

def test_morel::operationpathexp_has_operation():
    assert hasattr(morel::OperationPathExp, "operation")
    descriptor = None
    for klass in morel::OperationPathExp.__mro__:
        if "operation" in klass.__dict__:
            descriptor = klass.__dict__["operation"]
            break
    assert isinstance(descriptor, property)



def test_morel::looppathexp_is_not_abstract():
    assert not inspect.isabstract(morel::LoopPathExp)


def test_morel::looppathexp_constructor_exists():
    assert callable(morel::LoopPathExp.__init__)


def test_morel::looppathexp_constructor_args():
    sig = inspect.signature(morel::LoopPathExp.__init__)
    params = list(sig.parameters.keys())



def test_morel::featurepathexp_is_not_abstract():
    assert not inspect.isabstract(morel::FeaturePathExp)


def test_morel::featurepathexp_constructor_exists():
    assert callable(morel::FeaturePathExp.__init__)


def test_morel::featurepathexp_constructor_args():
    sig = inspect.signature(morel::FeaturePathExp.__init__)
    params = list(sig.parameters.keys())
    assert "feature" in params, "Missing parameter 'feature'"

def test_morel::featurepathexp_has_feature():
    assert hasattr(morel::FeaturePathExp, "feature")
    descriptor = None
    for klass in morel::FeaturePathExp.__mro__:
        if "feature" in klass.__dict__:
            descriptor = klass.__dict__["feature"]
            break
    assert isinstance(descriptor, property)



def test_morel::unit_is_not_abstract():
    assert not inspect.isabstract(morel::Unit)


def test_morel::unit_constructor_exists():
    assert callable(morel::Unit.__init__)


def test_morel::unit_constructor_args():
    sig = inspect.signature(morel::Unit.__init__)
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



def test_morel::epackage_is_not_abstract():
    assert not inspect.isabstract(morel::EPackage)


def test_morel::epackage_constructor_exists():
    assert callable(morel::EPackage.__init__)


def test_morel::epackage_constructor_args():
    sig = inspect.signature(morel::EPackage.__init__)
    params = list(sig.parameters.keys())



def test_unit_is_not_abstract():
    assert not inspect.isabstract(Unit)


def test_unit_constructor_exists():
    assert callable(Unit.__init__)


def test_unit_constructor_args():
    sig = inspect.signature(Unit.__init__)
    params = list(sig.parameters.keys())



def test_morel::querymodel_is_not_abstract():
    assert not inspect.isabstract(morel::QueryModel)


def test_morel::querymodel_constructor_exists():
    assert callable(morel::QueryModel.__init__)


def test_morel::querymodel_constructor_args():
    sig = inspect.signature(morel::QueryModel.__init__)
    params = list(sig.parameters.keys())



def test_literalexp_is_not_abstract():
    assert not inspect.isabstract(LiteralExp)


def test_literalexp_constructor_exists():
    assert callable(LiteralExp.__init__)


def test_literalexp_constructor_args():
    sig = inspect.signature(LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_morel::integerliteralexp_is_not_abstract():
    assert not inspect.isabstract(morel::IntegerLiteralExp)


def test_morel::integerliteralexp_constructor_exists():
    assert callable(morel::IntegerLiteralExp.__init__)


def test_morel::integerliteralexp_constructor_args():
    sig = inspect.signature(morel::IntegerLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_morel::integerliteralexp_has_integerSymbol():
    assert hasattr(morel::IntegerLiteralExp, "integerSymbol")
    descriptor = None
    for klass in morel::IntegerLiteralExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_morel::typeliteralexp_is_not_abstract():
    assert not inspect.isabstract(morel::TypeLiteralExp)


def test_morel::typeliteralexp_constructor_exists():
    assert callable(morel::TypeLiteralExp.__init__)


def test_morel::typeliteralexp_constructor_args():
    sig = inspect.signature(morel::TypeLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_morel::enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(morel::EnumLiteralExp)


def test_morel::enumliteralexp_constructor_exists():
    assert callable(morel::EnumLiteralExp.__init__)


def test_morel::enumliteralexp_constructor_args():
    sig = inspect.signature(morel::EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_morel::undefinedliteralexp_is_not_abstract():
    assert not inspect.isabstract(morel::UndefinedLiteralExp)


def test_morel::undefinedliteralexp_constructor_exists():
    assert callable(morel::UndefinedLiteralExp.__init__)


def test_morel::undefinedliteralexp_constructor_args():
    sig = inspect.signature(morel::UndefinedLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_morel::undefinedliteralexp_has_value():
    assert hasattr(morel::UndefinedLiteralExp, "value")
    descriptor = None
    for klass in morel::UndefinedLiteralExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_morel::booleanliteralexp_is_not_abstract():
    assert not inspect.isabstract(morel::BooleanLiteralExp)


def test_morel::booleanliteralexp_constructor_exists():
    assert callable(morel::BooleanLiteralExp.__init__)


def test_morel::booleanliteralexp_constructor_args():
    sig = inspect.signature(morel::BooleanLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "boolSymbol" in params, "Missing parameter 'boolSymbol'"

def test_morel::booleanliteralexp_has_boolSymbol():
    assert hasattr(morel::BooleanLiteralExp, "boolSymbol")
    descriptor = None
    for klass in morel::BooleanLiteralExp.__mro__:
        if "boolSymbol" in klass.__dict__:
            descriptor = klass.__dict__["boolSymbol"]
            break
    assert isinstance(descriptor, property)



def test_morel::collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(morel::CollectionLiteralExp)


def test_morel::collectionliteralexp_constructor_exists():
    assert callable(morel::CollectionLiteralExp.__init__)


def test_morel::collectionliteralexp_constructor_args():
    sig = inspect.signature(morel::CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_morel::collectionliteralexp_has_type():
    assert hasattr(morel::CollectionLiteralExp, "type")
    descriptor = None
    for klass in morel::CollectionLiteralExp.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_morel::realliteralexp_is_not_abstract():
    assert not inspect.isabstract(morel::RealLiteralExp)


def test_morel::realliteralexp_constructor_exists():
    assert callable(morel::RealLiteralExp.__init__)


def test_morel::realliteralexp_constructor_args():
    sig = inspect.signature(morel::RealLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_morel::realliteralexp_has_realSymbol():
    assert hasattr(morel::RealLiteralExp, "realSymbol")
    descriptor = None
    for klass in morel::RealLiteralExp.__mro__:
        if "realSymbol" in klass.__dict__:
            descriptor = klass.__dict__["realSymbol"]
            break
    assert isinstance(descriptor, property)



def test_morel::arrayliteralexp_is_not_abstract():
    assert not inspect.isabstract(morel::ArrayLiteralExp)


def test_morel::arrayliteralexp_constructor_exists():
    assert callable(morel::ArrayLiteralExp.__init__)


def test_morel::arrayliteralexp_constructor_args():
    sig = inspect.signature(morel::ArrayLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_morel::stringliteralexp_is_not_abstract():
    assert not inspect.isabstract(morel::StringLiteralExp)


def test_morel::stringliteralexp_constructor_exists():
    assert callable(morel::StringLiteralExp.__init__)


def test_morel::stringliteralexp_constructor_args():
    sig = inspect.signature(morel::StringLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_morel::stringliteralexp_has_stringSymbol():
    assert hasattr(morel::StringLiteralExp, "stringSymbol")
    descriptor = None
    for klass in morel::StringLiteralExp.__mro__:
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



def test_morel::variableexp_is_not_abstract():
    assert not inspect.isabstract(morel::VariableExp)


def test_morel::variableexp_constructor_exists():
    assert callable(morel::VariableExp.__init__)


def test_morel::variableexp_constructor_args():
    sig = inspect.signature(morel::VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_morel::nestedexp_is_not_abstract():
    assert not inspect.isabstract(morel::NestedExp)


def test_morel::nestedexp_constructor_exists():
    assert callable(morel::NestedExp.__init__)


def test_morel::nestedexp_constructor_args():
    sig = inspect.signature(morel::NestedExp.__init__)
    params = list(sig.parameters.keys())



def test_morel::predefinedvariableexp_is_not_abstract():
    assert not inspect.isabstract(morel::PredefinedVariableExp)


def test_morel::predefinedvariableexp_constructor_exists():
    assert callable(morel::PredefinedVariableExp.__init__)


def test_morel::predefinedvariableexp_constructor_args():
    sig = inspect.signature(morel::PredefinedVariableExp.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"

def test_morel::predefinedvariableexp_has_variable():
    assert hasattr(morel::PredefinedVariableExp, "variable")
    descriptor = None
    for klass in morel::PredefinedVariableExp.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_morel::literalexp_is_not_abstract():
    assert not inspect.isabstract(morel::LiteralExp)


def test_morel::literalexp_constructor_exists():
    assert callable(morel::LiteralExp.__init__)


def test_morel::literalexp_constructor_args():
    sig = inspect.signature(morel::LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_morel::callpathexp_is_not_abstract():
    assert not inspect.isabstract(morel::CallPathExp)


def test_morel::callpathexp_constructor_exists():
    assert callable(morel::CallPathExp.__init__)


def test_morel::callpathexp_constructor_args():
    sig = inspect.signature(morel::CallPathExp.__init__)
    params = list(sig.parameters.keys())



def test_unaryexpchild_is_not_abstract():
    assert not inspect.isabstract(UnaryExpChild)


def test_unaryexpchild_constructor_exists():
    assert callable(UnaryExpChild.__init__)


def test_unaryexpchild_constructor_args():
    sig = inspect.signature(UnaryExpChild.__init__)
    params = list(sig.parameters.keys())



def test_morel::atomicexp_is_not_abstract():
    assert not inspect.isabstract(morel::AtomicExp)


def test_morel::atomicexp_constructor_exists():
    assert callable(morel::AtomicExp.__init__)


def test_morel::atomicexp_constructor_args():
    sig = inspect.signature(morel::AtomicExp.__init__)
    params = list(sig.parameters.keys())



def test_morel::edatatype_is_not_abstract():
    assert not inspect.isabstract(morel::EDataType)


def test_morel::edatatype_constructor_exists():
    assert callable(morel::EDataType.__init__)


def test_morel::edatatype_constructor_args():
    sig = inspect.signature(morel::EDataType.__init__)
    params = list(sig.parameters.keys())



def test_morel::eclass_is_not_abstract():
    assert not inspect.isabstract(morel::EClass)


def test_morel::eclass_constructor_exists():
    assert callable(morel::EClass.__init__)


def test_morel::eclass_constructor_args():
    sig = inspect.signature(morel::EClass.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_morel::primitivevariable_is_not_abstract():
    assert not inspect.isabstract(morel::PrimitiveVariable)


def test_morel::primitivevariable_constructor_exists():
    assert callable(morel::PrimitiveVariable.__init__)


def test_morel::primitivevariable_constructor_args():
    sig = inspect.signature(morel::PrimitiveVariable.__init__)
    params = list(sig.parameters.keys())



def test_morel::variablewithinit_is_not_abstract():
    assert not inspect.isabstract(morel::VariableWithInit)


def test_morel::variablewithinit_constructor_exists():
    assert callable(morel::VariableWithInit.__init__)


def test_morel::variablewithinit_constructor_args():
    sig = inspect.signature(morel::VariableWithInit.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_morel::transformationmodel_is_not_abstract():
    assert not inspect.isabstract(morel::TransformationModel)


def test_morel::transformationmodel_constructor_exists():
    assert callable(morel::TransformationModel.__init__)


def test_morel::transformationmodel_constructor_args():
    sig = inspect.signature(morel::TransformationModel.__init__)
    params = list(sig.parameters.keys())



def test_morel::query_is_not_abstract():
    assert not inspect.isabstract(morel::Query)


def test_morel::query_constructor_exists():
    assert callable(morel::Query.__init__)


def test_morel::query_constructor_args():
    sig = inspect.signature(morel::Query.__init__)
    params = list(sig.parameters.keys())



def test_morel::ruleelement_is_not_abstract():
    assert not inspect.isabstract(morel::RuleElement)


def test_morel::ruleelement_constructor_exists():
    assert callable(morel::RuleElement.__init__)


def test_morel::ruleelement_constructor_args():
    sig = inspect.signature(morel::RuleElement.__init__)
    params = list(sig.parameters.keys())



def test_morel::typedmodel_is_not_abstract():
    assert not inspect.isabstract(morel::TypedModel)


def test_morel::typedmodel_constructor_exists():
    assert callable(morel::TypedModel.__init__)


def test_morel::typedmodel_constructor_args():
    sig = inspect.signature(morel::TypedModel.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_morel::typedmodel_has_type():
    assert hasattr(morel::TypedModel, "type")
    descriptor = None
    for klass in morel::TypedModel.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_morel::variable_is_not_abstract():
    assert not inspect.isabstract(morel::Variable)


def test_morel::variable_constructor_exists():
    assert callable(morel::Variable.__init__)


def test_morel::variable_constructor_args():
    sig = inspect.signature(morel::Variable.__init__)
    params = list(sig.parameters.keys())



def test_morel::additionalconstraint_is_not_abstract():
    assert not inspect.isabstract(morel::AdditionalConstraint)


def test_morel::additionalconstraint_constructor_exists():
    assert callable(morel::AdditionalConstraint.__init__)


def test_morel::additionalconstraint_constructor_args():
    sig = inspect.signature(morel::AdditionalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_morel::statement_is_not_abstract():
    assert not inspect.isabstract(morel::Statement)


def test_morel::statement_constructor_exists():
    assert callable(morel::Statement.__init__)


def test_morel::statement_constructor_args():
    sig = inspect.signature(morel::Statement.__init__)
    params = list(sig.parameters.keys())



def test_morel::ereference_is_not_abstract():
    assert not inspect.isabstract(morel::EReference)


def test_morel::ereference_constructor_exists():
    assert callable(morel::EReference.__init__)


def test_morel::ereference_constructor_args():
    sig = inspect.signature(morel::EReference.__init__)
    params = list(sig.parameters.keys())



def test_morel::expression_is_not_abstract():
    assert not inspect.isabstract(morel::Expression)


def test_morel::expression_constructor_exists():
    assert callable(morel::Expression.__init__)


def test_morel::expression_constructor_args():
    sig = inspect.signature(morel::Expression.__init__)
    params = list(sig.parameters.keys())



def test_linkconstraint_is_not_abstract():
    assert not inspect.isabstract(LinkConstraint)


def test_linkconstraint_constructor_exists():
    assert callable(LinkConstraint.__init__)


def test_linkconstraint_constructor_args():
    sig = inspect.signature(LinkConstraint.__init__)
    params = list(sig.parameters.keys())



def test_morel::pathconstraint_is_not_abstract():
    assert not inspect.isabstract(morel::PathConstraint)


def test_morel::pathconstraint_constructor_exists():
    assert callable(morel::PathConstraint.__init__)


def test_morel::pathconstraint_constructor_args():
    sig = inspect.signature(morel::PathConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "maxLength" in params, "Missing parameter 'maxLength'"
    assert "minLength" in params, "Missing parameter 'minLength'"

def test_morel::pathconstraint_has_maxLength():
    assert hasattr(morel::PathConstraint, "maxLength")
    descriptor = None
    for klass in morel::PathConstraint.__mro__:
        if "maxLength" in klass.__dict__:
            descriptor = klass.__dict__["maxLength"]
            break
    assert isinstance(descriptor, property)

def test_morel::pathconstraint_has_minLength():
    assert hasattr(morel::PathConstraint, "minLength")
    descriptor = None
    for klass in morel::PathConstraint.__mro__:
        if "minLength" in klass.__dict__:
            descriptor = klass.__dict__["minLength"]
            break
    assert isinstance(descriptor, property)



def test_morel::enclosurelinkconstraint_is_not_abstract():
    assert not inspect.isabstract(morel::EnclosureLinkConstraint)


def test_morel::enclosurelinkconstraint_constructor_exists():
    assert callable(morel::EnclosureLinkConstraint.__init__)


def test_morel::enclosurelinkconstraint_constructor_args():
    sig = inspect.signature(morel::EnclosureLinkConstraint.__init__)
    params = list(sig.parameters.keys())



def test_morel::simplelinkconstraint_is_not_abstract():
    assert not inspect.isabstract(morel::SimpleLinkConstraint)


def test_morel::simplelinkconstraint_constructor_exists():
    assert callable(morel::SimpleLinkConstraint.__init__)


def test_morel::simplelinkconstraint_constructor_args():
    sig = inspect.signature(morel::SimpleLinkConstraint.__init__)
    params = list(sig.parameters.keys())



def test_morel::linkconstraint_is_not_abstract():
    assert not inspect.isabstract(morel::LinkConstraint)


def test_morel::linkconstraint_constructor_exists():
    assert callable(morel::LinkConstraint.__init__)


def test_morel::linkconstraint_constructor_args():
    sig = inspect.signature(morel::LinkConstraint.__init__)
    params = list(sig.parameters.keys())



def test_morel::objectvariable_is_not_abstract():
    assert not inspect.isabstract(morel::ObjectVariable)


def test_morel::objectvariable_constructor_exists():
    assert callable(morel::ObjectVariable.__init__)


def test_morel::objectvariable_constructor_args():
    sig = inspect.signature(morel::ObjectVariable.__init__)
    params = list(sig.parameters.keys())



def test_section_is_not_abstract():
    assert not inspect.isabstract(Section)


def test_section_constructor_exists():
    assert callable(Section.__init__)


def test_section_constructor_args():
    sig = inspect.signature(Section.__init__)
    params = list(sig.parameters.keys())



def test_morel::clause_is_not_abstract():
    assert not inspect.isabstract(morel::Clause)


def test_morel::clause_constructor_exists():
    assert callable(morel::Clause.__init__)


def test_morel::clause_constructor_args():
    sig = inspect.signature(morel::Clause.__init__)
    params = list(sig.parameters.keys())



def test_morel::pattern_is_not_abstract():
    assert not inspect.isabstract(morel::Pattern)


def test_morel::pattern_constructor_exists():
    assert callable(morel::Pattern.__init__)


def test_morel::pattern_constructor_args():
    sig = inspect.signature(morel::Pattern.__init__)
    params = list(sig.parameters.keys())



def test_morel::section_is_not_abstract():
    assert not inspect.isabstract(morel::Section)


def test_morel::section_constructor_exists():
    assert callable(morel::Section.__init__)


def test_morel::section_constructor_args():
    sig = inspect.signature(morel::Section.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_morel::section_has_type():
    assert hasattr(morel::Section, "type")
    descriptor = None
    for klass in morel::Section.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_morel::namedelement_is_not_abstract():
    assert not inspect.isabstract(morel::NamedElement)


def test_morel::namedelement_constructor_exists():
    assert callable(morel::NamedElement.__init__)


def test_morel::namedelement_constructor_args():
    sig = inspect.signature(morel::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_morel::namedelement_has_name():
    assert hasattr(morel::NamedElement, "name")
    descriptor = None
    for klass in morel::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_iteratortype_exists():
    # Check that the Enumeration exists
    assert IteratorType is not None

def test_iteratortype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IteratorType]
    expected_literals = [
        "select",
        "forAll",
        "closure",
        "exists",
        "reject",
        "collect",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IteratorType"

def test_unaryoperator_exists():
    # Check that the Enumeration exists
    assert UnaryOperator is not None

def test_unaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryOperator]
    expected_literals = [
        "plus",
        "not_",
        "minus",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryOperator"

def test_booleanoperator_exists():
    # Check that the Enumeration exists
    assert BooleanOperator is not None

def test_booleanoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanOperator]
    expected_literals = [
        "or_",
        "not_",
        "implies",
        "and_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BooleanOperator"

def test_repetitiontype_exists():
    # Check that the Enumeration exists
    assert RepetitionType is not None

def test_repetitiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RepetitionType]
    expected_literals = [
        "randomOne",
        "allMatches",
        "first",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RepetitionType"

def test_relationaloperator_exists():
    # Check that the Enumeration exists
    assert RelationalOperator is not None

def test_relationaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationalOperator]
    expected_literals = [
        "lessOrEq",
        "equal",
        "greaterOrEq",
        "greater",
        "less",
        "notEqual",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationalOperator"

def test_ordertype_exists():
    # Check that the Enumeration exists
    assert OrderType is not None

def test_ordertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OrderType]
    expected_literals = [
        "parallel",
        "default",
        "sequential",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OrderType"

def test_scopetype_exists():
    # Check that the Enumeration exists
    assert ScopeType is not None

def test_scopetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ScopeType]
    expected_literals = [
        "all",
        "dynamicRandom",
        "staticRandom",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ScopeType"

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

def test_sectiontype_exists():
    # Check that the Enumeration exists
    assert SectionType is not None

def test_sectiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SectionType]
    expected_literals = [
        "NAC",
        "POST",
        "PRE",
        "RHS",
        "LHS",
        "PAC",
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
        "shuffle",
        "default",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IterationType"

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

def test_multiplicativeoperator_exists():
    # Check that the Enumeration exists
    assert MultiplicativeOperator is not None

def test_multiplicativeoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MultiplicativeOperator]
    expected_literals = [
        "div",
        "multi",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MultiplicativeOperator"

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
morel::PrimitiveConstraint_strategy = st.builds(
    morel::PrimitiveConstraint,
)
AdditionalConstraint_strategy = st.builds(
    AdditionalConstraint,
)
morel::AllDifferentConstraint_strategy = st.builds(
    morel::AllDifferentConstraint,
)
morel::OrderConstraint_strategy = st.builds(
    morel::OrderConstraint,
)
morel::Executable_strategy = st.builds(
    morel::Executable,
    active=
        st.booleans(),
    parameters=
        safe_text
)
morel::EAttribute_strategy = st.builds(
    morel::EAttribute,
)
PrimitiveConstraint_strategy = st.builds(
    PrimitiveConstraint,
)
morel::ValueRangeConstraint_strategy = st.builds(
    morel::ValueRangeConstraint,
)
morel::MultiValueConstraint_strategy = st.builds(
    morel::MultiValueConstraint,
)
RuleElement_strategy = st.builds(
    RuleElement,
)
morel::RuleGroup_strategy = st.builds(
    morel::RuleGroup,
    scope=
        safe_text,
    scopeSize=
        st.integers(),
    repetition=
        safe_text,
    maxIteration=
        st.integers(),
    order=
        safe_text,
    iteration=
        safe_text
)
morel::Rule_strategy = st.builds(
    morel::Rule,
)
Statement_strategy = st.builds(
    Statement,
)
morel::DeclarativeStatement_strategy = st.builds(
    morel::DeclarativeStatement,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
morel::BagType_strategy = st.builds(
    morel::BagType,
)
morel::SetType_strategy = st.builds(
    morel::SetType,
)
morel::SequenceType_strategy = st.builds(
    morel::SequenceType,
)
morel::OrderedSetType_strategy = st.builds(
    morel::OrderedSetType,
)
EDataType_strategy = st.builds(
    EDataType,
)
morel::CollectionType_strategy = st.builds(
    morel::CollectionType,
)
morel::ImperativeStatement_strategy = st.builds(
    morel::ImperativeStatement,
)
ImperativeStatement_strategy = st.builds(
    ImperativeStatement,
)
morel::ForStatement_strategy = st.builds(
    morel::ForStatement,
)
morel::BlockStatement_strategy = st.builds(
    morel::BlockStatement,
)
morel::IfStatement_strategy = st.builds(
    morel::IfStatement,
)
BooleanAndExpChild_strategy = st.builds(
    BooleanAndExpChild,
)
morel::RelationalExpChild_strategy = st.builds(
    morel::RelationalExpChild,
)
morel::RelationalExp_strategy = st.builds(
    morel::RelationalExp,
    operator=
        safe_text
)
BooleanOrExpChild_strategy = st.builds(
    BooleanOrExpChild,
)
morel::BooleanAndExpChild_strategy = st.builds(
    morel::BooleanAndExpChild,
)
morel::BooleanAndExp_strategy = st.builds(
    morel::BooleanAndExp,
    operators=
        safe_text
)
BooleanImpliesExpChild_strategy = st.builds(
    BooleanImpliesExpChild,
)
morel::BooleanOrExpChild_strategy = st.builds(
    morel::BooleanOrExpChild,
)
morel::BooleanOrExp_strategy = st.builds(
    morel::BooleanOrExp,
    operators=
        safe_text
)
MultiplicativeExpChild_strategy = st.builds(
    MultiplicativeExpChild,
)
morel::UnaryExpChild_strategy = st.builds(
    morel::UnaryExpChild,
)
morel::UnaryExp_strategy = st.builds(
    morel::UnaryExp,
    operator=
        safe_text
)
AdditiveExpChild_strategy = st.builds(
    AdditiveExpChild,
)
morel::MultiplicativeExpChild_strategy = st.builds(
    morel::MultiplicativeExpChild,
)
morel::MultiplicativeExp_strategy = st.builds(
    morel::MultiplicativeExp,
    operators=
        safe_text
)
RelationalExpChild_strategy = st.builds(
    RelationalExpChild,
)
morel::AdditiveExpChild_strategy = st.builds(
    morel::AdditiveExpChild,
)
morel::AdditiveExp_strategy = st.builds(
    morel::AdditiveExp,
    operators=
        safe_text
)
ImperativeExp_strategy = st.builds(
    ImperativeExp,
)
morel::PredefinedBindExp_strategy = st.builds(
    morel::PredefinedBindExp,
)
morel::BindExp_strategy = st.builds(
    morel::BindExp,
)
Expression_strategy = st.builds(
    Expression,
)
morel::BooleanImpliesExpChild_strategy = st.builds(
    morel::BooleanImpliesExpChild,
)
morel::ReflectiveVariableExp_strategy = st.builds(
    morel::ReflectiveVariableExp,
)
morel::ImperativeExp_strategy = st.builds(
    morel::ImperativeExp,
)
morel::LetExp_strategy = st.builds(
    morel::LetExp,
)
LoopPathExp_strategy = st.builds(
    LoopPathExp,
)
morel::IteratorPathExp_strategy = st.builds(
    morel::IteratorPathExp,
    type=
        safe_text
)
morel::BooleanImpliesExp_strategy = st.builds(
    morel::BooleanImpliesExp,
    operator=
        safe_text
)
morel::ConditionExp_strategy = st.builds(
    morel::ConditionExp,
)
PrimitiveVariable_strategy = st.builds(
    PrimitiveVariable,
)
VariableWithInit_strategy = st.builds(
    VariableWithInit,
)
morel::PrimitiveVariableWithInit_strategy = st.builds(
    morel::PrimitiveVariableWithInit,
)
ObjectVariable_strategy = st.builds(
    ObjectVariable,
)
morel::ObjectVariableWithInit_strategy = st.builds(
    morel::ObjectVariableWithInit,
)
morel::EClassifier_strategy = st.builds(
    morel::EClassifier,
)
morel::EEnumLiteral_strategy = st.builds(
    morel::EEnumLiteral,
)
morel::EEnum_strategy = st.builds(
    morel::EEnum,
)
CallPathExp_strategy = st.builds(
    CallPathExp,
)
morel::OperationPathExp_strategy = st.builds(
    morel::OperationPathExp,
    separator=
        safe_text,
    operation=
        safe_text
)
morel::LoopPathExp_strategy = st.builds(
    morel::LoopPathExp,
)
morel::FeaturePathExp_strategy = st.builds(
    morel::FeaturePathExp,
    feature=
        safe_text
)
morel::Unit_strategy = st.builds(
    morel::Unit,
)
Executable_strategy = st.builds(
    Executable,
)
Pattern_strategy = st.builds(
    Pattern,
)
morel::EPackage_strategy = st.builds(
    morel::EPackage,
)
Unit_strategy = st.builds(
    Unit,
)
morel::QueryModel_strategy = st.builds(
    morel::QueryModel,
)
LiteralExp_strategy = st.builds(
    LiteralExp,
)
morel::IntegerLiteralExp_strategy = st.builds(
    morel::IntegerLiteralExp,
    integerSymbol=
        st.integers()
)
morel::TypeLiteralExp_strategy = st.builds(
    morel::TypeLiteralExp,
)
morel::EnumLiteralExp_strategy = st.builds(
    morel::EnumLiteralExp,
)
morel::UndefinedLiteralExp_strategy = st.builds(
    morel::UndefinedLiteralExp,
    value=
        safe_text
)
morel::BooleanLiteralExp_strategy = st.builds(
    morel::BooleanLiteralExp,
    boolSymbol=
        st.booleans()
)
morel::CollectionLiteralExp_strategy = st.builds(
    morel::CollectionLiteralExp,
    type=
        safe_text
)
morel::RealLiteralExp_strategy = st.builds(
    morel::RealLiteralExp,
    realSymbol=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
morel::ArrayLiteralExp_strategy = st.builds(
    morel::ArrayLiteralExp,
)
morel::StringLiteralExp_strategy = st.builds(
    morel::StringLiteralExp,
    stringSymbol=
        safe_text
)
AtomicExp_strategy = st.builds(
    AtomicExp,
)
morel::VariableExp_strategy = st.builds(
    morel::VariableExp,
)
morel::NestedExp_strategy = st.builds(
    morel::NestedExp,
)
morel::PredefinedVariableExp_strategy = st.builds(
    morel::PredefinedVariableExp,
    variable=
        safe_text
)
morel::LiteralExp_strategy = st.builds(
    morel::LiteralExp,
)
morel::CallPathExp_strategy = st.builds(
    morel::CallPathExp,
)
UnaryExpChild_strategy = st.builds(
    UnaryExpChild,
)
morel::AtomicExp_strategy = st.builds(
    morel::AtomicExp,
)
morel::EDataType_strategy = st.builds(
    morel::EDataType,
)
morel::EClass_strategy = st.builds(
    morel::EClass,
)
Variable_strategy = st.builds(
    Variable,
)
morel::PrimitiveVariable_strategy = st.builds(
    morel::PrimitiveVariable,
)
morel::VariableWithInit_strategy = st.builds(
    morel::VariableWithInit,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
morel::TransformationModel_strategy = st.builds(
    morel::TransformationModel,
)
morel::Query_strategy = st.builds(
    morel::Query,
)
morel::RuleElement_strategy = st.builds(
    morel::RuleElement,
)
morel::TypedModel_strategy = st.builds(
    morel::TypedModel,
    type=
        safe_text
)
morel::Variable_strategy = st.builds(
    morel::Variable,
)
morel::AdditionalConstraint_strategy = st.builds(
    morel::AdditionalConstraint,
)
morel::Statement_strategy = st.builds(
    morel::Statement,
)
morel::EReference_strategy = st.builds(
    morel::EReference,
)
morel::Expression_strategy = st.builds(
    morel::Expression,
)
LinkConstraint_strategy = st.builds(
    LinkConstraint,
)
morel::PathConstraint_strategy = st.builds(
    morel::PathConstraint,
    maxLength=
        st.integers(),
    minLength=
        st.integers()
)
morel::EnclosureLinkConstraint_strategy = st.builds(
    morel::EnclosureLinkConstraint,
)
morel::SimpleLinkConstraint_strategy = st.builds(
    morel::SimpleLinkConstraint,
)
morel::LinkConstraint_strategy = st.builds(
    morel::LinkConstraint,
)
morel::ObjectVariable_strategy = st.builds(
    morel::ObjectVariable,
)
Section_strategy = st.builds(
    Section,
)
morel::Clause_strategy = st.builds(
    morel::Clause,
)
morel::Pattern_strategy = st.builds(
    morel::Pattern,
)
morel::Section_strategy = st.builds(
    morel::Section,
    type=
        safe_text
)
morel::NamedElement_strategy = st.builds(
    morel::NamedElement,
    name=
        safe_text
)

@given(instance=morel::PrimitiveConstraint_strategy)
@settings(max_examples=50)
def test_morel::primitiveconstraint_instantiation(instance):
    assert isinstance(instance, morel::PrimitiveConstraint)

@given(instance=AdditionalConstraint_strategy)
@settings(max_examples=50)
def test_additionalconstraint_instantiation(instance):
    assert isinstance(instance, AdditionalConstraint)

@given(instance=morel::AllDifferentConstraint_strategy)
@settings(max_examples=50)
def test_morel::alldifferentconstraint_instantiation(instance):
    assert isinstance(instance, morel::AllDifferentConstraint)

@given(instance=morel::OrderConstraint_strategy)
@settings(max_examples=50)
def test_morel::orderconstraint_instantiation(instance):
    assert isinstance(instance, morel::OrderConstraint)

@given(instance=morel::Executable_strategy)
@settings(max_examples=50)
def test_morel::executable_instantiation(instance):
    assert isinstance(instance, morel::Executable)

@given(instance=morel::Executable_strategy)
def test_morel::executable_active_type(instance):
    assert isinstance(instance.active, bool)


@given(instance=morel::Executable_strategy)
def test_morel::executable_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original

@given(instance=morel::Executable_strategy)
def test_morel::executable_parameters_type(instance):
    assert isinstance(instance.parameters, str)


@given(instance=morel::Executable_strategy)
def test_morel::executable_parameters_setter(instance):
    original = instance.parameters
    instance.parameters = original
    assert instance.parameters == original

@given(instance=morel::EAttribute_strategy)
@settings(max_examples=50)
def test_morel::eattribute_instantiation(instance):
    assert isinstance(instance, morel::EAttribute)

@given(instance=PrimitiveConstraint_strategy)
@settings(max_examples=50)
def test_primitiveconstraint_instantiation(instance):
    assert isinstance(instance, PrimitiveConstraint)

@given(instance=morel::ValueRangeConstraint_strategy)
@settings(max_examples=50)
def test_morel::valuerangeconstraint_instantiation(instance):
    assert isinstance(instance, morel::ValueRangeConstraint)

@given(instance=morel::MultiValueConstraint_strategy)
@settings(max_examples=50)
def test_morel::multivalueconstraint_instantiation(instance):
    assert isinstance(instance, morel::MultiValueConstraint)

@given(instance=RuleElement_strategy)
@settings(max_examples=50)
def test_ruleelement_instantiation(instance):
    assert isinstance(instance, RuleElement)

@given(instance=morel::RuleGroup_strategy)
@settings(max_examples=50)
def test_morel::rulegroup_instantiation(instance):
    assert isinstance(instance, morel::RuleGroup)

@given(instance=morel::RuleGroup_strategy)
def test_morel::rulegroup_scope_type(instance):
    assert isinstance(instance.scope, str)


@given(instance=morel::RuleGroup_strategy)
def test_morel::rulegroup_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original

@given(instance=morel::RuleGroup_strategy)
def test_morel::rulegroup_scopeSize_type(instance):
    assert isinstance(instance.scopeSize, int)


@given(instance=morel::RuleGroup_strategy)
def test_morel::rulegroup_scopeSize_setter(instance):
    original = instance.scopeSize
    instance.scopeSize = original
    assert instance.scopeSize == original

@given(instance=morel::RuleGroup_strategy)
def test_morel::rulegroup_repetition_type(instance):
    assert isinstance(instance.repetition, str)


@given(instance=morel::RuleGroup_strategy)
def test_morel::rulegroup_repetition_setter(instance):
    original = instance.repetition
    instance.repetition = original
    assert instance.repetition == original

@given(instance=morel::RuleGroup_strategy)
def test_morel::rulegroup_maxIteration_type(instance):
    assert isinstance(instance.maxIteration, int)


@given(instance=morel::RuleGroup_strategy)
def test_morel::rulegroup_maxIteration_setter(instance):
    original = instance.maxIteration
    instance.maxIteration = original
    assert instance.maxIteration == original

@given(instance=morel::RuleGroup_strategy)
def test_morel::rulegroup_order_type(instance):
    assert isinstance(instance.order, str)


@given(instance=morel::RuleGroup_strategy)
def test_morel::rulegroup_order_setter(instance):
    original = instance.order
    instance.order = original
    assert instance.order == original

@given(instance=morel::RuleGroup_strategy)
def test_morel::rulegroup_iteration_type(instance):
    assert isinstance(instance.iteration, str)


@given(instance=morel::RuleGroup_strategy)
def test_morel::rulegroup_iteration_setter(instance):
    original = instance.iteration
    instance.iteration = original
    assert instance.iteration == original

@given(instance=morel::Rule_strategy)
@settings(max_examples=50)
def test_morel::rule_instantiation(instance):
    assert isinstance(instance, morel::Rule)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=morel::DeclarativeStatement_strategy)
@settings(max_examples=50)
def test_morel::declarativestatement_instantiation(instance):
    assert isinstance(instance, morel::DeclarativeStatement)

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=morel::BagType_strategy)
@settings(max_examples=50)
def test_morel::bagtype_instantiation(instance):
    assert isinstance(instance, morel::BagType)

@given(instance=morel::SetType_strategy)
@settings(max_examples=50)
def test_morel::settype_instantiation(instance):
    assert isinstance(instance, morel::SetType)

@given(instance=morel::SequenceType_strategy)
@settings(max_examples=50)
def test_morel::sequencetype_instantiation(instance):
    assert isinstance(instance, morel::SequenceType)

@given(instance=morel::OrderedSetType_strategy)
@settings(max_examples=50)
def test_morel::orderedsettype_instantiation(instance):
    assert isinstance(instance, morel::OrderedSetType)

@given(instance=EDataType_strategy)
@settings(max_examples=50)
def test_edatatype_instantiation(instance):
    assert isinstance(instance, EDataType)

@given(instance=morel::CollectionType_strategy)
@settings(max_examples=50)
def test_morel::collectiontype_instantiation(instance):
    assert isinstance(instance, morel::CollectionType)

@given(instance=morel::ImperativeStatement_strategy)
@settings(max_examples=50)
def test_morel::imperativestatement_instantiation(instance):
    assert isinstance(instance, morel::ImperativeStatement)

@given(instance=ImperativeStatement_strategy)
@settings(max_examples=50)
def test_imperativestatement_instantiation(instance):
    assert isinstance(instance, ImperativeStatement)

@given(instance=morel::ForStatement_strategy)
@settings(max_examples=50)
def test_morel::forstatement_instantiation(instance):
    assert isinstance(instance, morel::ForStatement)

@given(instance=morel::BlockStatement_strategy)
@settings(max_examples=50)
def test_morel::blockstatement_instantiation(instance):
    assert isinstance(instance, morel::BlockStatement)

@given(instance=morel::IfStatement_strategy)
@settings(max_examples=50)
def test_morel::ifstatement_instantiation(instance):
    assert isinstance(instance, morel::IfStatement)

@given(instance=BooleanAndExpChild_strategy)
@settings(max_examples=50)
def test_booleanandexpchild_instantiation(instance):
    assert isinstance(instance, BooleanAndExpChild)

@given(instance=morel::RelationalExpChild_strategy)
@settings(max_examples=50)
def test_morel::relationalexpchild_instantiation(instance):
    assert isinstance(instance, morel::RelationalExpChild)

@given(instance=morel::RelationalExp_strategy)
@settings(max_examples=50)
def test_morel::relationalexp_instantiation(instance):
    assert isinstance(instance, morel::RelationalExp)

@given(instance=morel::RelationalExp_strategy)
def test_morel::relationalexp_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=morel::RelationalExp_strategy)
def test_morel::relationalexp_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=BooleanOrExpChild_strategy)
@settings(max_examples=50)
def test_booleanorexpchild_instantiation(instance):
    assert isinstance(instance, BooleanOrExpChild)

@given(instance=morel::BooleanAndExpChild_strategy)
@settings(max_examples=50)
def test_morel::booleanandexpchild_instantiation(instance):
    assert isinstance(instance, morel::BooleanAndExpChild)

@given(instance=morel::BooleanAndExp_strategy)
@settings(max_examples=50)
def test_morel::booleanandexp_instantiation(instance):
    assert isinstance(instance, morel::BooleanAndExp)

@given(instance=morel::BooleanAndExp_strategy)
def test_morel::booleanandexp_operators_type(instance):
    assert isinstance(instance.operators, str)


@given(instance=morel::BooleanAndExp_strategy)
def test_morel::booleanandexp_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original

@given(instance=BooleanImpliesExpChild_strategy)
@settings(max_examples=50)
def test_booleanimpliesexpchild_instantiation(instance):
    assert isinstance(instance, BooleanImpliesExpChild)

@given(instance=morel::BooleanOrExpChild_strategy)
@settings(max_examples=50)
def test_morel::booleanorexpchild_instantiation(instance):
    assert isinstance(instance, morel::BooleanOrExpChild)

@given(instance=morel::BooleanOrExp_strategy)
@settings(max_examples=50)
def test_morel::booleanorexp_instantiation(instance):
    assert isinstance(instance, morel::BooleanOrExp)

@given(instance=morel::BooleanOrExp_strategy)
def test_morel::booleanorexp_operators_type(instance):
    assert isinstance(instance.operators, str)


@given(instance=morel::BooleanOrExp_strategy)
def test_morel::booleanorexp_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original

@given(instance=MultiplicativeExpChild_strategy)
@settings(max_examples=50)
def test_multiplicativeexpchild_instantiation(instance):
    assert isinstance(instance, MultiplicativeExpChild)

@given(instance=morel::UnaryExpChild_strategy)
@settings(max_examples=50)
def test_morel::unaryexpchild_instantiation(instance):
    assert isinstance(instance, morel::UnaryExpChild)

@given(instance=morel::UnaryExp_strategy)
@settings(max_examples=50)
def test_morel::unaryexp_instantiation(instance):
    assert isinstance(instance, morel::UnaryExp)

@given(instance=morel::UnaryExp_strategy)
def test_morel::unaryexp_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=morel::UnaryExp_strategy)
def test_morel::unaryexp_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=AdditiveExpChild_strategy)
@settings(max_examples=50)
def test_additiveexpchild_instantiation(instance):
    assert isinstance(instance, AdditiveExpChild)

@given(instance=morel::MultiplicativeExpChild_strategy)
@settings(max_examples=50)
def test_morel::multiplicativeexpchild_instantiation(instance):
    assert isinstance(instance, morel::MultiplicativeExpChild)

@given(instance=morel::MultiplicativeExp_strategy)
@settings(max_examples=50)
def test_morel::multiplicativeexp_instantiation(instance):
    assert isinstance(instance, morel::MultiplicativeExp)

@given(instance=morel::MultiplicativeExp_strategy)
def test_morel::multiplicativeexp_operators_type(instance):
    assert isinstance(instance.operators, str)


@given(instance=morel::MultiplicativeExp_strategy)
def test_morel::multiplicativeexp_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original

@given(instance=RelationalExpChild_strategy)
@settings(max_examples=50)
def test_relationalexpchild_instantiation(instance):
    assert isinstance(instance, RelationalExpChild)

@given(instance=morel::AdditiveExpChild_strategy)
@settings(max_examples=50)
def test_morel::additiveexpchild_instantiation(instance):
    assert isinstance(instance, morel::AdditiveExpChild)

@given(instance=morel::AdditiveExp_strategy)
@settings(max_examples=50)
def test_morel::additiveexp_instantiation(instance):
    assert isinstance(instance, morel::AdditiveExp)

@given(instance=morel::AdditiveExp_strategy)
def test_morel::additiveexp_operators_type(instance):
    assert isinstance(instance.operators, str)


@given(instance=morel::AdditiveExp_strategy)
def test_morel::additiveexp_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original

@given(instance=ImperativeExp_strategy)
@settings(max_examples=50)
def test_imperativeexp_instantiation(instance):
    assert isinstance(instance, ImperativeExp)

@given(instance=morel::PredefinedBindExp_strategy)
@settings(max_examples=50)
def test_morel::predefinedbindexp_instantiation(instance):
    assert isinstance(instance, morel::PredefinedBindExp)

@given(instance=morel::BindExp_strategy)
@settings(max_examples=50)
def test_morel::bindexp_instantiation(instance):
    assert isinstance(instance, morel::BindExp)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=morel::BooleanImpliesExpChild_strategy)
@settings(max_examples=50)
def test_morel::booleanimpliesexpchild_instantiation(instance):
    assert isinstance(instance, morel::BooleanImpliesExpChild)

@given(instance=morel::ReflectiveVariableExp_strategy)
@settings(max_examples=50)
def test_morel::reflectivevariableexp_instantiation(instance):
    assert isinstance(instance, morel::ReflectiveVariableExp)

@given(instance=morel::ImperativeExp_strategy)
@settings(max_examples=50)
def test_morel::imperativeexp_instantiation(instance):
    assert isinstance(instance, morel::ImperativeExp)

@given(instance=morel::LetExp_strategy)
@settings(max_examples=50)
def test_morel::letexp_instantiation(instance):
    assert isinstance(instance, morel::LetExp)

@given(instance=LoopPathExp_strategy)
@settings(max_examples=50)
def test_looppathexp_instantiation(instance):
    assert isinstance(instance, LoopPathExp)

@given(instance=morel::IteratorPathExp_strategy)
@settings(max_examples=50)
def test_morel::iteratorpathexp_instantiation(instance):
    assert isinstance(instance, morel::IteratorPathExp)

@given(instance=morel::IteratorPathExp_strategy)
def test_morel::iteratorpathexp_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=morel::IteratorPathExp_strategy)
def test_morel::iteratorpathexp_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=morel::BooleanImpliesExp_strategy)
@settings(max_examples=50)
def test_morel::booleanimpliesexp_instantiation(instance):
    assert isinstance(instance, morel::BooleanImpliesExp)

@given(instance=morel::BooleanImpliesExp_strategy)
def test_morel::booleanimpliesexp_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=morel::BooleanImpliesExp_strategy)
def test_morel::booleanimpliesexp_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=morel::ConditionExp_strategy)
@settings(max_examples=50)
def test_morel::conditionexp_instantiation(instance):
    assert isinstance(instance, morel::ConditionExp)

@given(instance=PrimitiveVariable_strategy)
@settings(max_examples=50)
def test_primitivevariable_instantiation(instance):
    assert isinstance(instance, PrimitiveVariable)

@given(instance=VariableWithInit_strategy)
@settings(max_examples=50)
def test_variablewithinit_instantiation(instance):
    assert isinstance(instance, VariableWithInit)

@given(instance=morel::PrimitiveVariableWithInit_strategy)
@settings(max_examples=50)
def test_morel::primitivevariablewithinit_instantiation(instance):
    assert isinstance(instance, morel::PrimitiveVariableWithInit)

@given(instance=ObjectVariable_strategy)
@settings(max_examples=50)
def test_objectvariable_instantiation(instance):
    assert isinstance(instance, ObjectVariable)

@given(instance=morel::ObjectVariableWithInit_strategy)
@settings(max_examples=50)
def test_morel::objectvariablewithinit_instantiation(instance):
    assert isinstance(instance, morel::ObjectVariableWithInit)

@given(instance=morel::EClassifier_strategy)
@settings(max_examples=50)
def test_morel::eclassifier_instantiation(instance):
    assert isinstance(instance, morel::EClassifier)

@given(instance=morel::EEnumLiteral_strategy)
@settings(max_examples=50)
def test_morel::eenumliteral_instantiation(instance):
    assert isinstance(instance, morel::EEnumLiteral)

@given(instance=morel::EEnum_strategy)
@settings(max_examples=50)
def test_morel::eenum_instantiation(instance):
    assert isinstance(instance, morel::EEnum)

@given(instance=CallPathExp_strategy)
@settings(max_examples=50)
def test_callpathexp_instantiation(instance):
    assert isinstance(instance, CallPathExp)

@given(instance=morel::OperationPathExp_strategy)
@settings(max_examples=50)
def test_morel::operationpathexp_instantiation(instance):
    assert isinstance(instance, morel::OperationPathExp)

@given(instance=morel::OperationPathExp_strategy)
def test_morel::operationpathexp_separator_type(instance):
    assert isinstance(instance.separator, str)


@given(instance=morel::OperationPathExp_strategy)
def test_morel::operationpathexp_separator_setter(instance):
    original = instance.separator
    instance.separator = original
    assert instance.separator == original

@given(instance=morel::OperationPathExp_strategy)
def test_morel::operationpathexp_operation_type(instance):
    assert isinstance(instance.operation, str)


@given(instance=morel::OperationPathExp_strategy)
def test_morel::operationpathexp_operation_setter(instance):
    original = instance.operation
    instance.operation = original
    assert instance.operation == original

@given(instance=morel::LoopPathExp_strategy)
@settings(max_examples=50)
def test_morel::looppathexp_instantiation(instance):
    assert isinstance(instance, morel::LoopPathExp)

@given(instance=morel::FeaturePathExp_strategy)
@settings(max_examples=50)
def test_morel::featurepathexp_instantiation(instance):
    assert isinstance(instance, morel::FeaturePathExp)

@given(instance=morel::FeaturePathExp_strategy)
def test_morel::featurepathexp_feature_type(instance):
    assert isinstance(instance.feature, str)


@given(instance=morel::FeaturePathExp_strategy)
def test_morel::featurepathexp_feature_setter(instance):
    original = instance.feature
    instance.feature = original
    assert instance.feature == original

@given(instance=morel::Unit_strategy)
@settings(max_examples=50)
def test_morel::unit_instantiation(instance):
    assert isinstance(instance, morel::Unit)

@given(instance=Executable_strategy)
@settings(max_examples=50)
def test_executable_instantiation(instance):
    assert isinstance(instance, Executable)

@given(instance=Pattern_strategy)
@settings(max_examples=50)
def test_pattern_instantiation(instance):
    assert isinstance(instance, Pattern)

@given(instance=morel::EPackage_strategy)
@settings(max_examples=50)
def test_morel::epackage_instantiation(instance):
    assert isinstance(instance, morel::EPackage)

@given(instance=Unit_strategy)
@settings(max_examples=50)
def test_unit_instantiation(instance):
    assert isinstance(instance, Unit)

@given(instance=morel::QueryModel_strategy)
@settings(max_examples=50)
def test_morel::querymodel_instantiation(instance):
    assert isinstance(instance, morel::QueryModel)

@given(instance=LiteralExp_strategy)
@settings(max_examples=50)
def test_literalexp_instantiation(instance):
    assert isinstance(instance, LiteralExp)

@given(instance=morel::IntegerLiteralExp_strategy)
@settings(max_examples=50)
def test_morel::integerliteralexp_instantiation(instance):
    assert isinstance(instance, morel::IntegerLiteralExp)

@given(instance=morel::IntegerLiteralExp_strategy)
def test_morel::integerliteralexp_integerSymbol_type(instance):
    assert isinstance(instance.integerSymbol, int)


@given(instance=morel::IntegerLiteralExp_strategy)
def test_morel::integerliteralexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=morel::TypeLiteralExp_strategy)
@settings(max_examples=50)
def test_morel::typeliteralexp_instantiation(instance):
    assert isinstance(instance, morel::TypeLiteralExp)

@given(instance=morel::EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_morel::enumliteralexp_instantiation(instance):
    assert isinstance(instance, morel::EnumLiteralExp)

@given(instance=morel::UndefinedLiteralExp_strategy)
@settings(max_examples=50)
def test_morel::undefinedliteralexp_instantiation(instance):
    assert isinstance(instance, morel::UndefinedLiteralExp)

@given(instance=morel::UndefinedLiteralExp_strategy)
def test_morel::undefinedliteralexp_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=morel::UndefinedLiteralExp_strategy)
def test_morel::undefinedliteralexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=morel::BooleanLiteralExp_strategy)
@settings(max_examples=50)
def test_morel::booleanliteralexp_instantiation(instance):
    assert isinstance(instance, morel::BooleanLiteralExp)

@given(instance=morel::BooleanLiteralExp_strategy)
def test_morel::booleanliteralexp_boolSymbol_type(instance):
    assert isinstance(instance.boolSymbol, bool)


@given(instance=morel::BooleanLiteralExp_strategy)
def test_morel::booleanliteralexp_boolSymbol_setter(instance):
    original = instance.boolSymbol
    instance.boolSymbol = original
    assert instance.boolSymbol == original

@given(instance=morel::CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_morel::collectionliteralexp_instantiation(instance):
    assert isinstance(instance, morel::CollectionLiteralExp)

@given(instance=morel::CollectionLiteralExp_strategy)
def test_morel::collectionliteralexp_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=morel::CollectionLiteralExp_strategy)
def test_morel::collectionliteralexp_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=morel::RealLiteralExp_strategy)
@settings(max_examples=50)
def test_morel::realliteralexp_instantiation(instance):
    assert isinstance(instance, morel::RealLiteralExp)

@given(instance=morel::RealLiteralExp_strategy)
def test_morel::realliteralexp_realSymbol_type(instance):
    assert isinstance(instance.realSymbol, float)


@given(instance=morel::RealLiteralExp_strategy)
def test_morel::realliteralexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=morel::ArrayLiteralExp_strategy)
@settings(max_examples=50)
def test_morel::arrayliteralexp_instantiation(instance):
    assert isinstance(instance, morel::ArrayLiteralExp)

@given(instance=morel::StringLiteralExp_strategy)
@settings(max_examples=50)
def test_morel::stringliteralexp_instantiation(instance):
    assert isinstance(instance, morel::StringLiteralExp)

@given(instance=morel::StringLiteralExp_strategy)
def test_morel::stringliteralexp_stringSymbol_type(instance):
    assert isinstance(instance.stringSymbol, str)


@given(instance=morel::StringLiteralExp_strategy)
def test_morel::stringliteralexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=AtomicExp_strategy)
@settings(max_examples=50)
def test_atomicexp_instantiation(instance):
    assert isinstance(instance, AtomicExp)

@given(instance=morel::VariableExp_strategy)
@settings(max_examples=50)
def test_morel::variableexp_instantiation(instance):
    assert isinstance(instance, morel::VariableExp)

@given(instance=morel::NestedExp_strategy)
@settings(max_examples=50)
def test_morel::nestedexp_instantiation(instance):
    assert isinstance(instance, morel::NestedExp)

@given(instance=morel::PredefinedVariableExp_strategy)
@settings(max_examples=50)
def test_morel::predefinedvariableexp_instantiation(instance):
    assert isinstance(instance, morel::PredefinedVariableExp)

@given(instance=morel::PredefinedVariableExp_strategy)
def test_morel::predefinedvariableexp_variable_type(instance):
    assert isinstance(instance.variable, str)


@given(instance=morel::PredefinedVariableExp_strategy)
def test_morel::predefinedvariableexp_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=morel::LiteralExp_strategy)
@settings(max_examples=50)
def test_morel::literalexp_instantiation(instance):
    assert isinstance(instance, morel::LiteralExp)

@given(instance=morel::CallPathExp_strategy)
@settings(max_examples=50)
def test_morel::callpathexp_instantiation(instance):
    assert isinstance(instance, morel::CallPathExp)

@given(instance=UnaryExpChild_strategy)
@settings(max_examples=50)
def test_unaryexpchild_instantiation(instance):
    assert isinstance(instance, UnaryExpChild)

@given(instance=morel::AtomicExp_strategy)
@settings(max_examples=50)
def test_morel::atomicexp_instantiation(instance):
    assert isinstance(instance, morel::AtomicExp)

@given(instance=morel::EDataType_strategy)
@settings(max_examples=50)
def test_morel::edatatype_instantiation(instance):
    assert isinstance(instance, morel::EDataType)

@given(instance=morel::EClass_strategy)
@settings(max_examples=50)
def test_morel::eclass_instantiation(instance):
    assert isinstance(instance, morel::EClass)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=morel::PrimitiveVariable_strategy)
@settings(max_examples=50)
def test_morel::primitivevariable_instantiation(instance):
    assert isinstance(instance, morel::PrimitiveVariable)

@given(instance=morel::VariableWithInit_strategy)
@settings(max_examples=50)
def test_morel::variablewithinit_instantiation(instance):
    assert isinstance(instance, morel::VariableWithInit)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=morel::TransformationModel_strategy)
@settings(max_examples=50)
def test_morel::transformationmodel_instantiation(instance):
    assert isinstance(instance, morel::TransformationModel)

@given(instance=morel::Query_strategy)
@settings(max_examples=50)
def test_morel::query_instantiation(instance):
    assert isinstance(instance, morel::Query)

@given(instance=morel::RuleElement_strategy)
@settings(max_examples=50)
def test_morel::ruleelement_instantiation(instance):
    assert isinstance(instance, morel::RuleElement)

@given(instance=morel::TypedModel_strategy)
@settings(max_examples=50)
def test_morel::typedmodel_instantiation(instance):
    assert isinstance(instance, morel::TypedModel)

@given(instance=morel::TypedModel_strategy)
def test_morel::typedmodel_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=morel::TypedModel_strategy)
def test_morel::typedmodel_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=morel::Variable_strategy)
@settings(max_examples=50)
def test_morel::variable_instantiation(instance):
    assert isinstance(instance, morel::Variable)

@given(instance=morel::AdditionalConstraint_strategy)
@settings(max_examples=50)
def test_morel::additionalconstraint_instantiation(instance):
    assert isinstance(instance, morel::AdditionalConstraint)

@given(instance=morel::Statement_strategy)
@settings(max_examples=50)
def test_morel::statement_instantiation(instance):
    assert isinstance(instance, morel::Statement)

@given(instance=morel::EReference_strategy)
@settings(max_examples=50)
def test_morel::ereference_instantiation(instance):
    assert isinstance(instance, morel::EReference)

@given(instance=morel::Expression_strategy)
@settings(max_examples=50)
def test_morel::expression_instantiation(instance):
    assert isinstance(instance, morel::Expression)

@given(instance=LinkConstraint_strategy)
@settings(max_examples=50)
def test_linkconstraint_instantiation(instance):
    assert isinstance(instance, LinkConstraint)

@given(instance=morel::PathConstraint_strategy)
@settings(max_examples=50)
def test_morel::pathconstraint_instantiation(instance):
    assert isinstance(instance, morel::PathConstraint)

@given(instance=morel::PathConstraint_strategy)
def test_morel::pathconstraint_maxLength_type(instance):
    assert isinstance(instance.maxLength, int)


@given(instance=morel::PathConstraint_strategy)
def test_morel::pathconstraint_maxLength_setter(instance):
    original = instance.maxLength
    instance.maxLength = original
    assert instance.maxLength == original

@given(instance=morel::PathConstraint_strategy)
def test_morel::pathconstraint_minLength_type(instance):
    assert isinstance(instance.minLength, int)


@given(instance=morel::PathConstraint_strategy)
def test_morel::pathconstraint_minLength_setter(instance):
    original = instance.minLength
    instance.minLength = original
    assert instance.minLength == original

@given(instance=morel::EnclosureLinkConstraint_strategy)
@settings(max_examples=50)
def test_morel::enclosurelinkconstraint_instantiation(instance):
    assert isinstance(instance, morel::EnclosureLinkConstraint)

@given(instance=morel::SimpleLinkConstraint_strategy)
@settings(max_examples=50)
def test_morel::simplelinkconstraint_instantiation(instance):
    assert isinstance(instance, morel::SimpleLinkConstraint)

@given(instance=morel::LinkConstraint_strategy)
@settings(max_examples=50)
def test_morel::linkconstraint_instantiation(instance):
    assert isinstance(instance, morel::LinkConstraint)

@given(instance=morel::ObjectVariable_strategy)
@settings(max_examples=50)
def test_morel::objectvariable_instantiation(instance):
    assert isinstance(instance, morel::ObjectVariable)

@given(instance=Section_strategy)
@settings(max_examples=50)
def test_section_instantiation(instance):
    assert isinstance(instance, Section)

@given(instance=morel::Clause_strategy)
@settings(max_examples=50)
def test_morel::clause_instantiation(instance):
    assert isinstance(instance, morel::Clause)

@given(instance=morel::Pattern_strategy)
@settings(max_examples=50)
def test_morel::pattern_instantiation(instance):
    assert isinstance(instance, morel::Pattern)

@given(instance=morel::Section_strategy)
@settings(max_examples=50)
def test_morel::section_instantiation(instance):
    assert isinstance(instance, morel::Section)

@given(instance=morel::Section_strategy)
def test_morel::section_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=morel::Section_strategy)
def test_morel::section_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=morel::NamedElement_strategy)
@settings(max_examples=50)
def test_morel::namedelement_instantiation(instance):
    assert isinstance(instance, morel::NamedElement)

@given(instance=morel::NamedElement_strategy)
def test_morel::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=morel::NamedElement_strategy)
def test_morel::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
