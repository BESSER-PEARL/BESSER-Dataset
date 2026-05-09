import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    method::Method,
    variable::FieldVariable,
    import::ImportStatement,
    complexType::JInterface,
    ccsl::elements::Element,
    InjectionStrategy,
    InjectionAction,
    ccsl::Root,
    Variable,
    ccsl::variable::InitializableVariable,
    InitializableVariable,
    ccsl::variable::LocalVariable,
    annotation::AnnotableElement,
    variable::Variable,
    ccsl::variable::ParameterVariable,
    datatype::DataType,
    NamedElement,
    ccsl::variable::Variable,
    complexType::DeclaredType,
    import::ImportableElement,
    namedElements::NamedElement,
    ccsl::namedElements::Package,
    Context,
    Element,
    ccsl::complexType::ComplexType,
    ccsl::namedElements::NamedElement,
    Rule,
    ccsl::AtomicRule,
    ccsl::CompositeRule,
    Root,
    ccsl::FaultTypeDescription,
    ccsl::Rule,
    statements::Access,
    CcslNumberFunction,
    ccsl::numberFunctions::GetIndexOf,
    ccsl::numberFunctions::CcslIntegerLiteral,
    numberFunctions::CcslNumberFunction,
    ccsl::filters::EquationFilter,
    AtomicFilter,
    ccsl::filters::TemplateFilter,
    ccsl::filters::FromClosureFilter,
    ccsl::filters::SameNameFilter,
    ccsl::filters::SuperClassClosureFilter,
    ccsl::filters::ChildClosureComplexTypeFilter,
    ccsl::filters::IsStringFilter,
    ccsl::filters::SuperMethodClosureFilter,
    ccsl::filters::HasSameReferenceFilter,
    ccsl::filters::IsKindOfFilter,
    ccsl::filters::BlockLastStatementFilter,
    ccsl::filters::IsTypeOfFilter,
    ccsl::filters::PropertyFilter,
    Filter,
    ccsl::filters::CompositeFilter,
    ccsl::filters::AtomicFilter,
    CcslBooleanFunction,
    ccsl::filters::Filter,
    CcslFunction,
    ccsl::numberFunctions::CcslNumberFunction,
    ccsl::booleanFunctions::CcslBooleanFunction,
    ccsl::filters::ImplicityContainerFilter,
    expressions::OperatorExpression,
    TemplateFilter,
    ccsl::filters::ImplicityOperandFilter,
    ccsl::filters::RegexMatch,
    ccsl::filters::CountFilter,
    ccsl::faultTypeDescription::InjectionAction,
    filters::Filter,
    ccsl::context::Context,
    ObjectType,
    ccsl::datatype::ArrayType,
    ccsl::datatype::ParameterizedType,
    ccsl::functions::CcslFunction,
    ccsl::strategy::AllStrategy,
    ccsl::action::ArithmeticOperatorMap,
    action::ArithmeticOperatorMap,
    ccsl::action::ReplaceArithmeticOperatorAction,
    ccsl::action::ReplaceVariableAccessAction,
    ccsl::action::DeleteRandomStatementAction,
    ccsl::action::ChangeLiteralValueAction,
    ccsl::action::DeleteInfixOperatorAction,
    ccsl::action::MoveScopeUpAction,
    ccsl::action::DeleteAction,
    ccsl::faultTypeDescription::InjectionStrategy,
    ccsl::import::ImportableElement,
    Invocation,
    ccsl::invocation::SimpleMethodInvocation,
    ccsl::invocation::ConstructorInvocation,
    SimpleMethodInvocation,
    ccsl::invocation::SuperMethodInvocation,
    ccsl::invocation::MethodInvocation,
    PrimitiveType,
    ccsl::datatype::BooleanPrimitiveType,
    ccsl::datatype::IntPrimitiveType,
    ccsl::datatype::ShortPrimitiveType,
    ccsl::datatype::VoidType,
    ccsl::datatype::StringPrimitiveType,
    DataType,
    ccsl::datatype::ObjectType,
    ccsl::datatype::PrimitiveType,
    ccsl::datatype::DataType,
    annotation::Annotation,
    ccsl::annotation::AnnotableElement,
    complexType::AnnotationType,
    statements::Block,
    tryCatch::CatchClause,
    UnaryAssignment,
    ccsl::assignment::PostfixUnaryAssignment,
    ccsl::assignment::PrefixUnaryAssignment,
    AbstractAssignment,
    ccsl::assignment::UnaryAssignment,
    ccsl::assignment::Assignment,
    OperatorExpression,
    ccsl::expressions::ArithmeticExpression,
    ccsl::expressions::BooleanExpression,
    ccsl::expressions::InfixExpression,
    ccsl::expressions::StringConcatenation,
    Block,
    ccsl::controlFlow::SwitchCaseBlock,
    controlFlow::SwitchCaseBlock,
    ControlFlow,
    ccsl::controlFlow::IfStatement,
    ccsl::controlFlow::LoopStatement,
    ccsl::controlFlow::SwitchStatement,
    LiteralValue,
    ccsl::literalValues::StringLiteral,
    ccsl::literalValues::CharacterLiteral,
    ccsl::literalValues::NumberLiteral,
    ccsl::literalValues::BooleanLiteral,
    ccsl::literalValues::NullLiteral,
    ccsl::statements::ThrowStatement,
    Statement,
    ccsl::statements::ReturnStatement,
    ccsl::statements::InstanceOf,
    ccsl::tryCatch::CatchClause,
    ccsl::literalValues::LiteralValue,
    ccsl::annotation::Annotation,
    ccsl::import::ImportStatement,
    ccsl::statements::ArrayCreation,
    ccsl::statements::BreakStatement,
    ccsl::statements::ThisStatement,
    ccsl::statements::ContinueStatement,
    ccsl::assignment::AbstractAssignment,
    ccsl::tryCatch::TryStatement,
    ccsl::expressions::ParenthesizedExpression,
    ccsl::statements::SynchronizedBlock,
    ccsl::statements::Access,
    ccsl::invocation::Invocation,
    ccsl::expressions::OperatorExpression,
    ccsl::statements::EmptyStatement,
    ccsl::statements::NamedElementAccess,
    ccsl::statements::Statement,
    method::SimpleMethod,
    ccsl::method::Method,
    variable::ParameterVariable,
    elements::Element,
    ccsl::method::SimpleMethod,
    SimpleMethod,
    ccsl::method::Constructor,
    ccsl::statements::InstanceCreation,
    ccsl::statements::VarDeclaration,
    ccsl::statements::Block,
    ccsl::statements::ControlFlow,
    Access,
    ccsl::statements::DataTypeAccess,
    ccsl::statements::VariableAccess,
    complexType::JClass,
    method::Constructor,
    datatype::ObjectType,
    ccsl::complexType::DeclaredType,
    ComplexType,
    ccsl::datatype::GenericType,
    ccsl::complexType::AnonymousClass,
    complexType::ComplexType,
    ccsl::complexType::JClass,
    ccsl::complexType::JInterface,
    variable::InitializableVariable,
    ccsl::variable::FieldVariable,
    statements::Statement,
    DeclaredType,
    ccsl::complexType::AnnotationType,
    UnaryAssignmentOperator,
    LogicOperator,
    EquationOperator,
    AssignmentOperator,
    Inheritance,
    BooleanOperator,
    ArithmeticOperator,
    Visibility,
    CollectionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_method::method_is_not_abstract():
    assert not inspect.isabstract(method::Method)


def test_method::method_constructor_exists():
    assert callable(method::Method.__init__)


def test_method::method_constructor_args():
    sig = inspect.signature(method::Method.__init__)
    params = list(sig.parameters.keys())



def test_variable::fieldvariable_is_not_abstract():
    assert not inspect.isabstract(variable::FieldVariable)


def test_variable::fieldvariable_constructor_exists():
    assert callable(variable::FieldVariable.__init__)


def test_variable::fieldvariable_constructor_args():
    sig = inspect.signature(variable::FieldVariable.__init__)
    params = list(sig.parameters.keys())



def test_import::importstatement_is_not_abstract():
    assert not inspect.isabstract(import::ImportStatement)


def test_import::importstatement_constructor_exists():
    assert callable(import::ImportStatement.__init__)


def test_import::importstatement_constructor_args():
    sig = inspect.signature(import::ImportStatement.__init__)
    params = list(sig.parameters.keys())



def test_complextype::jinterface_is_not_abstract():
    assert not inspect.isabstract(complexType::JInterface)


def test_complextype::jinterface_constructor_exists():
    assert callable(complexType::JInterface.__init__)


def test_complextype::jinterface_constructor_args():
    sig = inspect.signature(complexType::JInterface.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::elements::element_is_not_abstract():
    assert not inspect.isabstract(ccsl::elements::Element)


def test_ccsl::elements::element_constructor_exists():
    assert callable(ccsl::elements::Element.__init__)


def test_ccsl::elements::element_constructor_args():
    sig = inspect.signature(ccsl::elements::Element.__init__)
    params = list(sig.parameters.keys())
    assert "uniqueName" in params, "Missing parameter 'uniqueName'"

def test_ccsl::elements::element_has_uniqueName():
    assert hasattr(ccsl::elements::Element, "uniqueName")
    descriptor = None
    for klass in ccsl::elements::Element.__mro__:
        if "uniqueName" in klass.__dict__:
            descriptor = klass.__dict__["uniqueName"]
            break
    assert isinstance(descriptor, property)



def test_injectionstrategy_is_not_abstract():
    assert not inspect.isabstract(InjectionStrategy)


def test_injectionstrategy_constructor_exists():
    assert callable(InjectionStrategy.__init__)


def test_injectionstrategy_constructor_args():
    sig = inspect.signature(InjectionStrategy.__init__)
    params = list(sig.parameters.keys())



def test_injectionaction_is_not_abstract():
    assert not inspect.isabstract(InjectionAction)


def test_injectionaction_constructor_exists():
    assert callable(InjectionAction.__init__)


def test_injectionaction_constructor_args():
    sig = inspect.signature(InjectionAction.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::root_is_not_abstract():
    assert not inspect.isabstract(ccsl::Root)


def test_ccsl::root_constructor_exists():
    assert callable(ccsl::Root.__init__)


def test_ccsl::root_constructor_args():
    sig = inspect.signature(ccsl::Root.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::variable::initializablevariable_is_not_abstract():
    assert not inspect.isabstract(ccsl::variable::InitializableVariable)


def test_ccsl::variable::initializablevariable_constructor_exists():
    assert callable(ccsl::variable::InitializableVariable.__init__)


def test_ccsl::variable::initializablevariable_constructor_args():
    sig = inspect.signature(ccsl::variable::InitializableVariable.__init__)
    params = list(sig.parameters.keys())



def test_initializablevariable_is_not_abstract():
    assert not inspect.isabstract(InitializableVariable)


def test_initializablevariable_constructor_exists():
    assert callable(InitializableVariable.__init__)


def test_initializablevariable_constructor_args():
    sig = inspect.signature(InitializableVariable.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::variable::localvariable_is_not_abstract():
    assert not inspect.isabstract(ccsl::variable::LocalVariable)


def test_ccsl::variable::localvariable_constructor_exists():
    assert callable(ccsl::variable::LocalVariable.__init__)


def test_ccsl::variable::localvariable_constructor_args():
    sig = inspect.signature(ccsl::variable::LocalVariable.__init__)
    params = list(sig.parameters.keys())



def test_annotation::annotableelement_is_not_abstract():
    assert not inspect.isabstract(annotation::AnnotableElement)


def test_annotation::annotableelement_constructor_exists():
    assert callable(annotation::AnnotableElement.__init__)


def test_annotation::annotableelement_constructor_args():
    sig = inspect.signature(annotation::AnnotableElement.__init__)
    params = list(sig.parameters.keys())



def test_variable::variable_is_not_abstract():
    assert not inspect.isabstract(variable::Variable)


def test_variable::variable_constructor_exists():
    assert callable(variable::Variable.__init__)


def test_variable::variable_constructor_args():
    sig = inspect.signature(variable::Variable.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::variable::parametervariable_is_not_abstract():
    assert not inspect.isabstract(ccsl::variable::ParameterVariable)


def test_ccsl::variable::parametervariable_constructor_exists():
    assert callable(ccsl::variable::ParameterVariable.__init__)


def test_ccsl::variable::parametervariable_constructor_args():
    sig = inspect.signature(ccsl::variable::ParameterVariable.__init__)
    params = list(sig.parameters.keys())



def test_datatype::datatype_is_not_abstract():
    assert not inspect.isabstract(datatype::DataType)


def test_datatype::datatype_constructor_exists():
    assert callable(datatype::DataType.__init__)


def test_datatype::datatype_constructor_args():
    sig = inspect.signature(datatype::DataType.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::variable::variable_is_not_abstract():
    assert not inspect.isabstract(ccsl::variable::Variable)


def test_ccsl::variable::variable_constructor_exists():
    assert callable(ccsl::variable::Variable.__init__)


def test_ccsl::variable::variable_constructor_args():
    sig = inspect.signature(ccsl::variable::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "final" in params, "Missing parameter 'final'"

def test_ccsl::variable::variable_has_final():
    assert hasattr(ccsl::variable::Variable, "final")
    descriptor = None
    for klass in ccsl::variable::Variable.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)



def test_complextype::declaredtype_is_not_abstract():
    assert not inspect.isabstract(complexType::DeclaredType)


def test_complextype::declaredtype_constructor_exists():
    assert callable(complexType::DeclaredType.__init__)


def test_complextype::declaredtype_constructor_args():
    sig = inspect.signature(complexType::DeclaredType.__init__)
    params = list(sig.parameters.keys())



def test_import::importableelement_is_not_abstract():
    assert not inspect.isabstract(import::ImportableElement)


def test_import::importableelement_constructor_exists():
    assert callable(import::ImportableElement.__init__)


def test_import::importableelement_constructor_args():
    sig = inspect.signature(import::ImportableElement.__init__)
    params = list(sig.parameters.keys())



def test_namedelements::namedelement_is_not_abstract():
    assert not inspect.isabstract(namedElements::NamedElement)


def test_namedelements::namedelement_constructor_exists():
    assert callable(namedElements::NamedElement.__init__)


def test_namedelements::namedelement_constructor_args():
    sig = inspect.signature(namedElements::NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::namedelements::package_is_not_abstract():
    assert not inspect.isabstract(ccsl::namedElements::Package)


def test_ccsl::namedelements::package_constructor_exists():
    assert callable(ccsl::namedElements::Package.__init__)


def test_ccsl::namedelements::package_constructor_args():
    sig = inspect.signature(ccsl::namedElements::Package.__init__)
    params = list(sig.parameters.keys())



def test_context_is_not_abstract():
    assert not inspect.isabstract(Context)


def test_context_constructor_exists():
    assert callable(Context.__init__)


def test_context_constructor_args():
    sig = inspect.signature(Context.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::complextype::complextype_is_not_abstract():
    assert not inspect.isabstract(ccsl::complexType::ComplexType)


def test_ccsl::complextype::complextype_constructor_exists():
    assert callable(ccsl::complexType::ComplexType.__init__)


def test_ccsl::complextype::complextype_constructor_args():
    sig = inspect.signature(ccsl::complexType::ComplexType.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::namedelements::namedelement_is_not_abstract():
    assert not inspect.isabstract(ccsl::namedElements::NamedElement)


def test_ccsl::namedelements::namedelement_constructor_exists():
    assert callable(ccsl::namedElements::NamedElement.__init__)


def test_ccsl::namedelements::namedelement_constructor_args():
    sig = inspect.signature(ccsl::namedElements::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "avaliableInSourceCode" in params, "Missing parameter 'avaliableInSourceCode'"
    assert "name" in params, "Missing parameter 'name'"

def test_ccsl::namedelements::namedelement_has_avaliableInSourceCode():
    assert hasattr(ccsl::namedElements::NamedElement, "avaliableInSourceCode")
    descriptor = None
    for klass in ccsl::namedElements::NamedElement.__mro__:
        if "avaliableInSourceCode" in klass.__dict__:
            descriptor = klass.__dict__["avaliableInSourceCode"]
            break
    assert isinstance(descriptor, property)

def test_ccsl::namedelements::namedelement_has_name():
    assert hasattr(ccsl::namedElements::NamedElement, "name")
    descriptor = None
    for klass in ccsl::namedElements::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rule_is_not_abstract():
    assert not inspect.isabstract(Rule)


def test_rule_constructor_exists():
    assert callable(Rule.__init__)


def test_rule_constructor_args():
    sig = inspect.signature(Rule.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::atomicrule_is_not_abstract():
    assert not inspect.isabstract(ccsl::AtomicRule)


def test_ccsl::atomicrule_constructor_exists():
    assert callable(ccsl::AtomicRule.__init__)


def test_ccsl::atomicrule_constructor_args():
    sig = inspect.signature(ccsl::AtomicRule.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::compositerule_is_not_abstract():
    assert not inspect.isabstract(ccsl::CompositeRule)


def test_ccsl::compositerule_constructor_exists():
    assert callable(ccsl::CompositeRule.__init__)


def test_ccsl::compositerule_constructor_args():
    sig = inspect.signature(ccsl::CompositeRule.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ccsl::compositerule_has_operator():
    assert hasattr(ccsl::CompositeRule, "operator")
    descriptor = None
    for klass in ccsl::CompositeRule.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_root_is_not_abstract():
    assert not inspect.isabstract(Root)


def test_root_constructor_exists():
    assert callable(Root.__init__)


def test_root_constructor_args():
    sig = inspect.signature(Root.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::faulttypedescription_is_not_abstract():
    assert not inspect.isabstract(ccsl::FaultTypeDescription)


def test_ccsl::faulttypedescription_constructor_exists():
    assert callable(ccsl::FaultTypeDescription.__init__)


def test_ccsl::faulttypedescription_constructor_args():
    sig = inspect.signature(ccsl::FaultTypeDescription.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ccsl::faulttypedescription_has_name():
    assert hasattr(ccsl::FaultTypeDescription, "name")
    descriptor = None
    for klass in ccsl::FaultTypeDescription.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ccsl::rule_is_not_abstract():
    assert not inspect.isabstract(ccsl::Rule)


def test_ccsl::rule_constructor_exists():
    assert callable(ccsl::Rule.__init__)


def test_ccsl::rule_constructor_args():
    sig = inspect.signature(ccsl::Rule.__init__)
    params = list(sig.parameters.keys())
    assert "negated" in params, "Missing parameter 'negated'"

def test_ccsl::rule_has_negated():
    assert hasattr(ccsl::Rule, "negated")
    descriptor = None
    for klass in ccsl::Rule.__mro__:
        if "negated" in klass.__dict__:
            descriptor = klass.__dict__["negated"]
            break
    assert isinstance(descriptor, property)



def test_statements::access_is_not_abstract():
    assert not inspect.isabstract(statements::Access)


def test_statements::access_constructor_exists():
    assert callable(statements::Access.__init__)


def test_statements::access_constructor_args():
    sig = inspect.signature(statements::Access.__init__)
    params = list(sig.parameters.keys())



def test_ccslnumberfunction_is_not_abstract():
    assert not inspect.isabstract(CcslNumberFunction)


def test_ccslnumberfunction_constructor_exists():
    assert callable(CcslNumberFunction.__init__)


def test_ccslnumberfunction_constructor_args():
    sig = inspect.signature(CcslNumberFunction.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::numberfunctions::getindexof_is_not_abstract():
    assert not inspect.isabstract(ccsl::numberFunctions::GetIndexOf)


def test_ccsl::numberfunctions::getindexof_constructor_exists():
    assert callable(ccsl::numberFunctions::GetIndexOf.__init__)


def test_ccsl::numberfunctions::getindexof_constructor_args():
    sig = inspect.signature(ccsl::numberFunctions::GetIndexOf.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::numberfunctions::ccslintegerliteral_is_not_abstract():
    assert not inspect.isabstract(ccsl::numberFunctions::CcslIntegerLiteral)


def test_ccsl::numberfunctions::ccslintegerliteral_constructor_exists():
    assert callable(ccsl::numberFunctions::CcslIntegerLiteral.__init__)


def test_ccsl::numberfunctions::ccslintegerliteral_constructor_args():
    sig = inspect.signature(ccsl::numberFunctions::CcslIntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ccsl::numberfunctions::ccslintegerliteral_has_value():
    assert hasattr(ccsl::numberFunctions::CcslIntegerLiteral, "value")
    descriptor = None
    for klass in ccsl::numberFunctions::CcslIntegerLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_numberfunctions::ccslnumberfunction_is_not_abstract():
    assert not inspect.isabstract(numberFunctions::CcslNumberFunction)


def test_numberfunctions::ccslnumberfunction_constructor_exists():
    assert callable(numberFunctions::CcslNumberFunction.__init__)


def test_numberfunctions::ccslnumberfunction_constructor_args():
    sig = inspect.signature(numberFunctions::CcslNumberFunction.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::filters::equationfilter_is_not_abstract():
    assert not inspect.isabstract(ccsl::filters::EquationFilter)


def test_ccsl::filters::equationfilter_constructor_exists():
    assert callable(ccsl::filters::EquationFilter.__init__)


def test_ccsl::filters::equationfilter_constructor_args():
    sig = inspect.signature(ccsl::filters::EquationFilter.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ccsl::filters::equationfilter_has_operator():
    assert hasattr(ccsl::filters::EquationFilter, "operator")
    descriptor = None
    for klass in ccsl::filters::EquationFilter.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_atomicfilter_is_not_abstract():
    assert not inspect.isabstract(AtomicFilter)


def test_atomicfilter_constructor_exists():
    assert callable(AtomicFilter.__init__)


def test_atomicfilter_constructor_args():
    sig = inspect.signature(AtomicFilter.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::filters::templatefilter_is_not_abstract():
    assert not inspect.isabstract(ccsl::filters::TemplateFilter)


def test_ccsl::filters::templatefilter_constructor_exists():
    assert callable(ccsl::filters::TemplateFilter.__init__)


def test_ccsl::filters::templatefilter_constructor_args():
    sig = inspect.signature(ccsl::filters::TemplateFilter.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::filters::fromclosurefilter_is_not_abstract():
    assert not inspect.isabstract(ccsl::filters::FromClosureFilter)


def test_ccsl::filters::fromclosurefilter_constructor_exists():
    assert callable(ccsl::filters::FromClosureFilter.__init__)


def test_ccsl::filters::fromclosurefilter_constructor_args():
    sig = inspect.signature(ccsl::filters::FromClosureFilter.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::filters::samenamefilter_is_not_abstract():
    assert not inspect.isabstract(ccsl::filters::SameNameFilter)


def test_ccsl::filters::samenamefilter_constructor_exists():
    assert callable(ccsl::filters::SameNameFilter.__init__)


def test_ccsl::filters::samenamefilter_constructor_args():
    sig = inspect.signature(ccsl::filters::SameNameFilter.__init__)
    params = list(sig.parameters.keys())
    assert "ignoreCase" in params, "Missing parameter 'ignoreCase'"

def test_ccsl::filters::samenamefilter_has_ignoreCase():
    assert hasattr(ccsl::filters::SameNameFilter, "ignoreCase")
    descriptor = None
    for klass in ccsl::filters::SameNameFilter.__mro__:
        if "ignoreCase" in klass.__dict__:
            descriptor = klass.__dict__["ignoreCase"]
            break
    assert isinstance(descriptor, property)



def test_ccsl::filters::superclassclosurefilter_is_not_abstract():
    assert not inspect.isabstract(ccsl::filters::SuperClassClosureFilter)


def test_ccsl::filters::superclassclosurefilter_constructor_exists():
    assert callable(ccsl::filters::SuperClassClosureFilter.__init__)


def test_ccsl::filters::superclassclosurefilter_constructor_args():
    sig = inspect.signature(ccsl::filters::SuperClassClosureFilter.__init__)
    params = list(sig.parameters.keys())
    assert "includesSubClass" in params, "Missing parameter 'includesSubClass'"

def test_ccsl::filters::superclassclosurefilter_has_includesSubClass():
    assert hasattr(ccsl::filters::SuperClassClosureFilter, "includesSubClass")
    descriptor = None
    for klass in ccsl::filters::SuperClassClosureFilter.__mro__:
        if "includesSubClass" in klass.__dict__:
            descriptor = klass.__dict__["includesSubClass"]
            break
    assert isinstance(descriptor, property)



def test_ccsl::filters::childclosurecomplextypefilter_is_not_abstract():
    assert not inspect.isabstract(ccsl::filters::ChildClosureComplexTypeFilter)


def test_ccsl::filters::childclosurecomplextypefilter_constructor_exists():
    assert callable(ccsl::filters::ChildClosureComplexTypeFilter.__init__)


def test_ccsl::filters::childclosurecomplextypefilter_constructor_args():
    sig = inspect.signature(ccsl::filters::ChildClosureComplexTypeFilter.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::filters::isstringfilter_is_not_abstract():
    assert not inspect.isabstract(ccsl::filters::IsStringFilter)


def test_ccsl::filters::isstringfilter_constructor_exists():
    assert callable(ccsl::filters::IsStringFilter.__init__)


def test_ccsl::filters::isstringfilter_constructor_args():
    sig = inspect.signature(ccsl::filters::IsStringFilter.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::filters::supermethodclosurefilter_is_not_abstract():
    assert not inspect.isabstract(ccsl::filters::SuperMethodClosureFilter)


def test_ccsl::filters::supermethodclosurefilter_constructor_exists():
    assert callable(ccsl::filters::SuperMethodClosureFilter.__init__)


def test_ccsl::filters::supermethodclosurefilter_constructor_args():
    sig = inspect.signature(ccsl::filters::SuperMethodClosureFilter.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::filters::hassamereferencefilter_is_not_abstract():
    assert not inspect.isabstract(ccsl::filters::HasSameReferenceFilter)


def test_ccsl::filters::hassamereferencefilter_constructor_exists():
    assert callable(ccsl::filters::HasSameReferenceFilter.__init__)


def test_ccsl::filters::hassamereferencefilter_constructor_args():
    sig = inspect.signature(ccsl::filters::HasSameReferenceFilter.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::filters::iskindoffilter_is_not_abstract():
    assert not inspect.isabstract(ccsl::filters::IsKindOfFilter)


def test_ccsl::filters::iskindoffilter_constructor_exists():
    assert callable(ccsl::filters::IsKindOfFilter.__init__)


def test_ccsl::filters::iskindoffilter_constructor_args():
    sig = inspect.signature(ccsl::filters::IsKindOfFilter.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::filters::blocklaststatementfilter_is_not_abstract():
    assert not inspect.isabstract(ccsl::filters::BlockLastStatementFilter)


def test_ccsl::filters::blocklaststatementfilter_constructor_exists():
    assert callable(ccsl::filters::BlockLastStatementFilter.__init__)


def test_ccsl::filters::blocklaststatementfilter_constructor_args():
    sig = inspect.signature(ccsl::filters::BlockLastStatementFilter.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::filters::istypeoffilter_is_not_abstract():
    assert not inspect.isabstract(ccsl::filters::IsTypeOfFilter)


def test_ccsl::filters::istypeoffilter_constructor_exists():
    assert callable(ccsl::filters::IsTypeOfFilter.__init__)


def test_ccsl::filters::istypeoffilter_constructor_args():
    sig = inspect.signature(ccsl::filters::IsTypeOfFilter.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::filters::propertyfilter_is_not_abstract():
    assert not inspect.isabstract(ccsl::filters::PropertyFilter)


def test_ccsl::filters::propertyfilter_constructor_exists():
    assert callable(ccsl::filters::PropertyFilter.__init__)


def test_ccsl::filters::propertyfilter_constructor_args():
    sig = inspect.signature(ccsl::filters::PropertyFilter.__init__)
    params = list(sig.parameters.keys())



def test_filter_is_not_abstract():
    assert not inspect.isabstract(Filter)


def test_filter_constructor_exists():
    assert callable(Filter.__init__)


def test_filter_constructor_args():
    sig = inspect.signature(Filter.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::filters::compositefilter_is_not_abstract():
    assert not inspect.isabstract(ccsl::filters::CompositeFilter)


def test_ccsl::filters::compositefilter_constructor_exists():
    assert callable(ccsl::filters::CompositeFilter.__init__)


def test_ccsl::filters::compositefilter_constructor_args():
    sig = inspect.signature(ccsl::filters::CompositeFilter.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ccsl::filters::compositefilter_has_operator():
    assert hasattr(ccsl::filters::CompositeFilter, "operator")
    descriptor = None
    for klass in ccsl::filters::CompositeFilter.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_ccsl::filters::atomicfilter_is_not_abstract():
    assert not inspect.isabstract(ccsl::filters::AtomicFilter)


def test_ccsl::filters::atomicfilter_constructor_exists():
    assert callable(ccsl::filters::AtomicFilter.__init__)


def test_ccsl::filters::atomicfilter_constructor_args():
    sig = inspect.signature(ccsl::filters::AtomicFilter.__init__)
    params = list(sig.parameters.keys())



def test_ccslbooleanfunction_is_not_abstract():
    assert not inspect.isabstract(CcslBooleanFunction)


def test_ccslbooleanfunction_constructor_exists():
    assert callable(CcslBooleanFunction.__init__)


def test_ccslbooleanfunction_constructor_args():
    sig = inspect.signature(CcslBooleanFunction.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::filters::filter_is_not_abstract():
    assert not inspect.isabstract(ccsl::filters::Filter)


def test_ccsl::filters::filter_constructor_exists():
    assert callable(ccsl::filters::Filter.__init__)


def test_ccsl::filters::filter_constructor_args():
    sig = inspect.signature(ccsl::filters::Filter.__init__)
    params = list(sig.parameters.keys())
    assert "negated" in params, "Missing parameter 'negated'"

def test_ccsl::filters::filter_has_negated():
    assert hasattr(ccsl::filters::Filter, "negated")
    descriptor = None
    for klass in ccsl::filters::Filter.__mro__:
        if "negated" in klass.__dict__:
            descriptor = klass.__dict__["negated"]
            break
    assert isinstance(descriptor, property)



def test_ccslfunction_is_not_abstract():
    assert not inspect.isabstract(CcslFunction)


def test_ccslfunction_constructor_exists():
    assert callable(CcslFunction.__init__)


def test_ccslfunction_constructor_args():
    sig = inspect.signature(CcslFunction.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::numberfunctions::ccslnumberfunction_is_not_abstract():
    assert not inspect.isabstract(ccsl::numberFunctions::CcslNumberFunction)


def test_ccsl::numberfunctions::ccslnumberfunction_constructor_exists():
    assert callable(ccsl::numberFunctions::CcslNumberFunction.__init__)


def test_ccsl::numberfunctions::ccslnumberfunction_constructor_args():
    sig = inspect.signature(ccsl::numberFunctions::CcslNumberFunction.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::booleanfunctions::ccslbooleanfunction_is_not_abstract():
    assert not inspect.isabstract(ccsl::booleanFunctions::CcslBooleanFunction)


def test_ccsl::booleanfunctions::ccslbooleanfunction_constructor_exists():
    assert callable(ccsl::booleanFunctions::CcslBooleanFunction.__init__)


def test_ccsl::booleanfunctions::ccslbooleanfunction_constructor_args():
    sig = inspect.signature(ccsl::booleanFunctions::CcslBooleanFunction.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::filters::implicitycontainerfilter_is_not_abstract():
    assert not inspect.isabstract(ccsl::filters::ImplicityContainerFilter)


def test_ccsl::filters::implicitycontainerfilter_constructor_exists():
    assert callable(ccsl::filters::ImplicityContainerFilter.__init__)


def test_ccsl::filters::implicitycontainerfilter_constructor_args():
    sig = inspect.signature(ccsl::filters::ImplicityContainerFilter.__init__)
    params = list(sig.parameters.keys())



def test_expressions::operatorexpression_is_not_abstract():
    assert not inspect.isabstract(expressions::OperatorExpression)


def test_expressions::operatorexpression_constructor_exists():
    assert callable(expressions::OperatorExpression.__init__)


def test_expressions::operatorexpression_constructor_args():
    sig = inspect.signature(expressions::OperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_templatefilter_is_not_abstract():
    assert not inspect.isabstract(TemplateFilter)


def test_templatefilter_constructor_exists():
    assert callable(TemplateFilter.__init__)


def test_templatefilter_constructor_args():
    sig = inspect.signature(TemplateFilter.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::filters::implicityoperandfilter_is_not_abstract():
    assert not inspect.isabstract(ccsl::filters::ImplicityOperandFilter)


def test_ccsl::filters::implicityoperandfilter_constructor_exists():
    assert callable(ccsl::filters::ImplicityOperandFilter.__init__)


def test_ccsl::filters::implicityoperandfilter_constructor_args():
    sig = inspect.signature(ccsl::filters::ImplicityOperandFilter.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::filters::regexmatch_is_not_abstract():
    assert not inspect.isabstract(ccsl::filters::RegexMatch)


def test_ccsl::filters::regexmatch_constructor_exists():
    assert callable(ccsl::filters::RegexMatch.__init__)


def test_ccsl::filters::regexmatch_constructor_args():
    sig = inspect.signature(ccsl::filters::RegexMatch.__init__)
    params = list(sig.parameters.keys())
    assert "regex" in params, "Missing parameter 'regex'"

def test_ccsl::filters::regexmatch_has_regex():
    assert hasattr(ccsl::filters::RegexMatch, "regex")
    descriptor = None
    for klass in ccsl::filters::RegexMatch.__mro__:
        if "regex" in klass.__dict__:
            descriptor = klass.__dict__["regex"]
            break
    assert isinstance(descriptor, property)



def test_ccsl::filters::countfilter_is_not_abstract():
    assert not inspect.isabstract(ccsl::filters::CountFilter)


def test_ccsl::filters::countfilter_constructor_exists():
    assert callable(ccsl::filters::CountFilter.__init__)


def test_ccsl::filters::countfilter_constructor_args():
    sig = inspect.signature(ccsl::filters::CountFilter.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "min" in params, "Missing parameter 'min'"

def test_ccsl::filters::countfilter_has_max():
    assert hasattr(ccsl::filters::CountFilter, "max")
    descriptor = None
    for klass in ccsl::filters::CountFilter.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_ccsl::filters::countfilter_has_min():
    assert hasattr(ccsl::filters::CountFilter, "min")
    descriptor = None
    for klass in ccsl::filters::CountFilter.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)



def test_ccsl::faulttypedescription::injectionaction_is_not_abstract():
    assert not inspect.isabstract(ccsl::faultTypeDescription::InjectionAction)


def test_ccsl::faulttypedescription::injectionaction_constructor_exists():
    assert callable(ccsl::faultTypeDescription::InjectionAction.__init__)


def test_ccsl::faulttypedescription::injectionaction_constructor_args():
    sig = inspect.signature(ccsl::faultTypeDescription::InjectionAction.__init__)
    params = list(sig.parameters.keys())



def test_filters::filter_is_not_abstract():
    assert not inspect.isabstract(filters::Filter)


def test_filters::filter_constructor_exists():
    assert callable(filters::Filter.__init__)


def test_filters::filter_constructor_args():
    sig = inspect.signature(filters::Filter.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::context::context_is_not_abstract():
    assert not inspect.isabstract(ccsl::context::Context)


def test_ccsl::context::context_constructor_exists():
    assert callable(ccsl::context::Context.__init__)


def test_ccsl::context::context_constructor_args():
    sig = inspect.signature(ccsl::context::Context.__init__)
    params = list(sig.parameters.keys())



def test_objecttype_is_not_abstract():
    assert not inspect.isabstract(ObjectType)


def test_objecttype_constructor_exists():
    assert callable(ObjectType.__init__)


def test_objecttype_constructor_args():
    sig = inspect.signature(ObjectType.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::datatype::arraytype_is_not_abstract():
    assert not inspect.isabstract(ccsl::datatype::ArrayType)


def test_ccsl::datatype::arraytype_constructor_exists():
    assert callable(ccsl::datatype::ArrayType.__init__)


def test_ccsl::datatype::arraytype_constructor_args():
    sig = inspect.signature(ccsl::datatype::ArrayType.__init__)
    params = list(sig.parameters.keys())
    assert "dimensions" in params, "Missing parameter 'dimensions'"

def test_ccsl::datatype::arraytype_has_dimensions():
    assert hasattr(ccsl::datatype::ArrayType, "dimensions")
    descriptor = None
    for klass in ccsl::datatype::ArrayType.__mro__:
        if "dimensions" in klass.__dict__:
            descriptor = klass.__dict__["dimensions"]
            break
    assert isinstance(descriptor, property)



def test_ccsl::datatype::parameterizedtype_is_not_abstract():
    assert not inspect.isabstract(ccsl::datatype::ParameterizedType)


def test_ccsl::datatype::parameterizedtype_constructor_exists():
    assert callable(ccsl::datatype::ParameterizedType.__init__)


def test_ccsl::datatype::parameterizedtype_constructor_args():
    sig = inspect.signature(ccsl::datatype::ParameterizedType.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::functions::ccslfunction_is_not_abstract():
    assert not inspect.isabstract(ccsl::functions::CcslFunction)


def test_ccsl::functions::ccslfunction_constructor_exists():
    assert callable(ccsl::functions::CcslFunction.__init__)


def test_ccsl::functions::ccslfunction_constructor_args():
    sig = inspect.signature(ccsl::functions::CcslFunction.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::strategy::allstrategy_is_not_abstract():
    assert not inspect.isabstract(ccsl::strategy::AllStrategy)


def test_ccsl::strategy::allstrategy_constructor_exists():
    assert callable(ccsl::strategy::AllStrategy.__init__)


def test_ccsl::strategy::allstrategy_constructor_args():
    sig = inspect.signature(ccsl::strategy::AllStrategy.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::action::arithmeticoperatormap_is_not_abstract():
    assert not inspect.isabstract(ccsl::action::ArithmeticOperatorMap)


def test_ccsl::action::arithmeticoperatormap_constructor_exists():
    assert callable(ccsl::action::ArithmeticOperatorMap.__init__)


def test_ccsl::action::arithmeticoperatormap_constructor_args():
    sig = inspect.signature(ccsl::action::ArithmeticOperatorMap.__init__)
    params = list(sig.parameters.keys())
    assert "newArithmeticOperator" in params, "Missing parameter 'newArithmeticOperator'"
    assert "oldArithmeticOperator" in params, "Missing parameter 'oldArithmeticOperator'"

def test_ccsl::action::arithmeticoperatormap_has_newArithmeticOperator():
    assert hasattr(ccsl::action::ArithmeticOperatorMap, "newArithmeticOperator")
    descriptor = None
    for klass in ccsl::action::ArithmeticOperatorMap.__mro__:
        if "newArithmeticOperator" in klass.__dict__:
            descriptor = klass.__dict__["newArithmeticOperator"]
            break
    assert isinstance(descriptor, property)

def test_ccsl::action::arithmeticoperatormap_has_oldArithmeticOperator():
    assert hasattr(ccsl::action::ArithmeticOperatorMap, "oldArithmeticOperator")
    descriptor = None
    for klass in ccsl::action::ArithmeticOperatorMap.__mro__:
        if "oldArithmeticOperator" in klass.__dict__:
            descriptor = klass.__dict__["oldArithmeticOperator"]
            break
    assert isinstance(descriptor, property)



def test_action::arithmeticoperatormap_is_not_abstract():
    assert not inspect.isabstract(action::ArithmeticOperatorMap)


def test_action::arithmeticoperatormap_constructor_exists():
    assert callable(action::ArithmeticOperatorMap.__init__)


def test_action::arithmeticoperatormap_constructor_args():
    sig = inspect.signature(action::ArithmeticOperatorMap.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::action::replacearithmeticoperatoraction_is_not_abstract():
    assert not inspect.isabstract(ccsl::action::ReplaceArithmeticOperatorAction)


def test_ccsl::action::replacearithmeticoperatoraction_constructor_exists():
    assert callable(ccsl::action::ReplaceArithmeticOperatorAction.__init__)


def test_ccsl::action::replacearithmeticoperatoraction_constructor_args():
    sig = inspect.signature(ccsl::action::ReplaceArithmeticOperatorAction.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::action::replacevariableaccessaction_is_not_abstract():
    assert not inspect.isabstract(ccsl::action::ReplaceVariableAccessAction)


def test_ccsl::action::replacevariableaccessaction_constructor_exists():
    assert callable(ccsl::action::ReplaceVariableAccessAction.__init__)


def test_ccsl::action::replacevariableaccessaction_constructor_args():
    sig = inspect.signature(ccsl::action::ReplaceVariableAccessAction.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::action::deleterandomstatementaction_is_not_abstract():
    assert not inspect.isabstract(ccsl::action::DeleteRandomStatementAction)


def test_ccsl::action::deleterandomstatementaction_constructor_exists():
    assert callable(ccsl::action::DeleteRandomStatementAction.__init__)


def test_ccsl::action::deleterandomstatementaction_constructor_args():
    sig = inspect.signature(ccsl::action::DeleteRandomStatementAction.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::action::changeliteralvalueaction_is_not_abstract():
    assert not inspect.isabstract(ccsl::action::ChangeLiteralValueAction)


def test_ccsl::action::changeliteralvalueaction_constructor_exists():
    assert callable(ccsl::action::ChangeLiteralValueAction.__init__)


def test_ccsl::action::changeliteralvalueaction_constructor_args():
    sig = inspect.signature(ccsl::action::ChangeLiteralValueAction.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::action::deleteinfixoperatoraction_is_not_abstract():
    assert not inspect.isabstract(ccsl::action::DeleteInfixOperatorAction)


def test_ccsl::action::deleteinfixoperatoraction_constructor_exists():
    assert callable(ccsl::action::DeleteInfixOperatorAction.__init__)


def test_ccsl::action::deleteinfixoperatoraction_constructor_args():
    sig = inspect.signature(ccsl::action::DeleteInfixOperatorAction.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::action::movescopeupaction_is_not_abstract():
    assert not inspect.isabstract(ccsl::action::MoveScopeUpAction)


def test_ccsl::action::movescopeupaction_constructor_exists():
    assert callable(ccsl::action::MoveScopeUpAction.__init__)


def test_ccsl::action::movescopeupaction_constructor_args():
    sig = inspect.signature(ccsl::action::MoveScopeUpAction.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::action::deleteaction_is_not_abstract():
    assert not inspect.isabstract(ccsl::action::DeleteAction)


def test_ccsl::action::deleteaction_constructor_exists():
    assert callable(ccsl::action::DeleteAction.__init__)


def test_ccsl::action::deleteaction_constructor_args():
    sig = inspect.signature(ccsl::action::DeleteAction.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::faulttypedescription::injectionstrategy_is_not_abstract():
    assert not inspect.isabstract(ccsl::faultTypeDescription::InjectionStrategy)


def test_ccsl::faulttypedescription::injectionstrategy_constructor_exists():
    assert callable(ccsl::faultTypeDescription::InjectionStrategy.__init__)


def test_ccsl::faulttypedescription::injectionstrategy_constructor_args():
    sig = inspect.signature(ccsl::faultTypeDescription::InjectionStrategy.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::import::importableelement_is_not_abstract():
    assert not inspect.isabstract(ccsl::import::ImportableElement)


def test_ccsl::import::importableelement_constructor_exists():
    assert callable(ccsl::import::ImportableElement.__init__)


def test_ccsl::import::importableelement_constructor_args():
    sig = inspect.signature(ccsl::import::ImportableElement.__init__)
    params = list(sig.parameters.keys())



def test_invocation_is_not_abstract():
    assert not inspect.isabstract(Invocation)


def test_invocation_constructor_exists():
    assert callable(Invocation.__init__)


def test_invocation_constructor_args():
    sig = inspect.signature(Invocation.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::invocation::simplemethodinvocation_is_not_abstract():
    assert not inspect.isabstract(ccsl::invocation::SimpleMethodInvocation)


def test_ccsl::invocation::simplemethodinvocation_constructor_exists():
    assert callable(ccsl::invocation::SimpleMethodInvocation.__init__)


def test_ccsl::invocation::simplemethodinvocation_constructor_args():
    sig = inspect.signature(ccsl::invocation::SimpleMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::invocation::constructorinvocation_is_not_abstract():
    assert not inspect.isabstract(ccsl::invocation::ConstructorInvocation)


def test_ccsl::invocation::constructorinvocation_constructor_exists():
    assert callable(ccsl::invocation::ConstructorInvocation.__init__)


def test_ccsl::invocation::constructorinvocation_constructor_args():
    sig = inspect.signature(ccsl::invocation::ConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_simplemethodinvocation_is_not_abstract():
    assert not inspect.isabstract(SimpleMethodInvocation)


def test_simplemethodinvocation_constructor_exists():
    assert callable(SimpleMethodInvocation.__init__)


def test_simplemethodinvocation_constructor_args():
    sig = inspect.signature(SimpleMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::invocation::supermethodinvocation_is_not_abstract():
    assert not inspect.isabstract(ccsl::invocation::SuperMethodInvocation)


def test_ccsl::invocation::supermethodinvocation_constructor_exists():
    assert callable(ccsl::invocation::SuperMethodInvocation.__init__)


def test_ccsl::invocation::supermethodinvocation_constructor_args():
    sig = inspect.signature(ccsl::invocation::SuperMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::invocation::methodinvocation_is_not_abstract():
    assert not inspect.isabstract(ccsl::invocation::MethodInvocation)


def test_ccsl::invocation::methodinvocation_constructor_exists():
    assert callable(ccsl::invocation::MethodInvocation.__init__)


def test_ccsl::invocation::methodinvocation_constructor_args():
    sig = inspect.signature(ccsl::invocation::MethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::datatype::booleanprimitivetype_is_not_abstract():
    assert not inspect.isabstract(ccsl::datatype::BooleanPrimitiveType)


def test_ccsl::datatype::booleanprimitivetype_constructor_exists():
    assert callable(ccsl::datatype::BooleanPrimitiveType.__init__)


def test_ccsl::datatype::booleanprimitivetype_constructor_args():
    sig = inspect.signature(ccsl::datatype::BooleanPrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::datatype::intprimitivetype_is_not_abstract():
    assert not inspect.isabstract(ccsl::datatype::IntPrimitiveType)


def test_ccsl::datatype::intprimitivetype_constructor_exists():
    assert callable(ccsl::datatype::IntPrimitiveType.__init__)


def test_ccsl::datatype::intprimitivetype_constructor_args():
    sig = inspect.signature(ccsl::datatype::IntPrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::datatype::shortprimitivetype_is_not_abstract():
    assert not inspect.isabstract(ccsl::datatype::ShortPrimitiveType)


def test_ccsl::datatype::shortprimitivetype_constructor_exists():
    assert callable(ccsl::datatype::ShortPrimitiveType.__init__)


def test_ccsl::datatype::shortprimitivetype_constructor_args():
    sig = inspect.signature(ccsl::datatype::ShortPrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::datatype::voidtype_is_not_abstract():
    assert not inspect.isabstract(ccsl::datatype::VoidType)


def test_ccsl::datatype::voidtype_constructor_exists():
    assert callable(ccsl::datatype::VoidType.__init__)


def test_ccsl::datatype::voidtype_constructor_args():
    sig = inspect.signature(ccsl::datatype::VoidType.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::datatype::stringprimitivetype_is_not_abstract():
    assert not inspect.isabstract(ccsl::datatype::StringPrimitiveType)


def test_ccsl::datatype::stringprimitivetype_constructor_exists():
    assert callable(ccsl::datatype::StringPrimitiveType.__init__)


def test_ccsl::datatype::stringprimitivetype_constructor_args():
    sig = inspect.signature(ccsl::datatype::StringPrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::datatype::objecttype_is_not_abstract():
    assert not inspect.isabstract(ccsl::datatype::ObjectType)


def test_ccsl::datatype::objecttype_constructor_exists():
    assert callable(ccsl::datatype::ObjectType.__init__)


def test_ccsl::datatype::objecttype_constructor_args():
    sig = inspect.signature(ccsl::datatype::ObjectType.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::datatype::primitivetype_is_not_abstract():
    assert not inspect.isabstract(ccsl::datatype::PrimitiveType)


def test_ccsl::datatype::primitivetype_constructor_exists():
    assert callable(ccsl::datatype::PrimitiveType.__init__)


def test_ccsl::datatype::primitivetype_constructor_args():
    sig = inspect.signature(ccsl::datatype::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::datatype::datatype_is_not_abstract():
    assert not inspect.isabstract(ccsl::datatype::DataType)


def test_ccsl::datatype::datatype_constructor_exists():
    assert callable(ccsl::datatype::DataType.__init__)


def test_ccsl::datatype::datatype_constructor_args():
    sig = inspect.signature(ccsl::datatype::DataType.__init__)
    params = list(sig.parameters.keys())



def test_annotation::annotation_is_not_abstract():
    assert not inspect.isabstract(annotation::Annotation)


def test_annotation::annotation_constructor_exists():
    assert callable(annotation::Annotation.__init__)


def test_annotation::annotation_constructor_args():
    sig = inspect.signature(annotation::Annotation.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::annotation::annotableelement_is_not_abstract():
    assert not inspect.isabstract(ccsl::annotation::AnnotableElement)


def test_ccsl::annotation::annotableelement_constructor_exists():
    assert callable(ccsl::annotation::AnnotableElement.__init__)


def test_ccsl::annotation::annotableelement_constructor_args():
    sig = inspect.signature(ccsl::annotation::AnnotableElement.__init__)
    params = list(sig.parameters.keys())
    assert "annotationsKind" in params, "Missing parameter 'annotationsKind'"

def test_ccsl::annotation::annotableelement_has_annotationsKind():
    assert hasattr(ccsl::annotation::AnnotableElement, "annotationsKind")
    descriptor = None
    for klass in ccsl::annotation::AnnotableElement.__mro__:
        if "annotationsKind" in klass.__dict__:
            descriptor = klass.__dict__["annotationsKind"]
            break
    assert isinstance(descriptor, property)



def test_complextype::annotationtype_is_not_abstract():
    assert not inspect.isabstract(complexType::AnnotationType)


def test_complextype::annotationtype_constructor_exists():
    assert callable(complexType::AnnotationType.__init__)


def test_complextype::annotationtype_constructor_args():
    sig = inspect.signature(complexType::AnnotationType.__init__)
    params = list(sig.parameters.keys())



def test_statements::block_is_not_abstract():
    assert not inspect.isabstract(statements::Block)


def test_statements::block_constructor_exists():
    assert callable(statements::Block.__init__)


def test_statements::block_constructor_args():
    sig = inspect.signature(statements::Block.__init__)
    params = list(sig.parameters.keys())



def test_trycatch::catchclause_is_not_abstract():
    assert not inspect.isabstract(tryCatch::CatchClause)


def test_trycatch::catchclause_constructor_exists():
    assert callable(tryCatch::CatchClause.__init__)


def test_trycatch::catchclause_constructor_args():
    sig = inspect.signature(tryCatch::CatchClause.__init__)
    params = list(sig.parameters.keys())



def test_unaryassignment_is_not_abstract():
    assert not inspect.isabstract(UnaryAssignment)


def test_unaryassignment_constructor_exists():
    assert callable(UnaryAssignment.__init__)


def test_unaryassignment_constructor_args():
    sig = inspect.signature(UnaryAssignment.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::assignment::postfixunaryassignment_is_not_abstract():
    assert not inspect.isabstract(ccsl::assignment::PostfixUnaryAssignment)


def test_ccsl::assignment::postfixunaryassignment_constructor_exists():
    assert callable(ccsl::assignment::PostfixUnaryAssignment.__init__)


def test_ccsl::assignment::postfixunaryassignment_constructor_args():
    sig = inspect.signature(ccsl::assignment::PostfixUnaryAssignment.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::assignment::prefixunaryassignment_is_not_abstract():
    assert not inspect.isabstract(ccsl::assignment::PrefixUnaryAssignment)


def test_ccsl::assignment::prefixunaryassignment_constructor_exists():
    assert callable(ccsl::assignment::PrefixUnaryAssignment.__init__)


def test_ccsl::assignment::prefixunaryassignment_constructor_args():
    sig = inspect.signature(ccsl::assignment::PrefixUnaryAssignment.__init__)
    params = list(sig.parameters.keys())



def test_abstractassignment_is_not_abstract():
    assert not inspect.isabstract(AbstractAssignment)


def test_abstractassignment_constructor_exists():
    assert callable(AbstractAssignment.__init__)


def test_abstractassignment_constructor_args():
    sig = inspect.signature(AbstractAssignment.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::assignment::unaryassignment_is_not_abstract():
    assert not inspect.isabstract(ccsl::assignment::UnaryAssignment)


def test_ccsl::assignment::unaryassignment_constructor_exists():
    assert callable(ccsl::assignment::UnaryAssignment.__init__)


def test_ccsl::assignment::unaryassignment_constructor_args():
    sig = inspect.signature(ccsl::assignment::UnaryAssignment.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ccsl::assignment::unaryassignment_has_operator():
    assert hasattr(ccsl::assignment::UnaryAssignment, "operator")
    descriptor = None
    for klass in ccsl::assignment::UnaryAssignment.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_ccsl::assignment::assignment_is_not_abstract():
    assert not inspect.isabstract(ccsl::assignment::Assignment)


def test_ccsl::assignment::assignment_constructor_exists():
    assert callable(ccsl::assignment::Assignment.__init__)


def test_ccsl::assignment::assignment_constructor_args():
    sig = inspect.signature(ccsl::assignment::Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ccsl::assignment::assignment_has_operator():
    assert hasattr(ccsl::assignment::Assignment, "operator")
    descriptor = None
    for klass in ccsl::assignment::Assignment.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_operatorexpression_is_not_abstract():
    assert not inspect.isabstract(OperatorExpression)


def test_operatorexpression_constructor_exists():
    assert callable(OperatorExpression.__init__)


def test_operatorexpression_constructor_args():
    sig = inspect.signature(OperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::expressions::arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(ccsl::expressions::ArithmeticExpression)


def test_ccsl::expressions::arithmeticexpression_constructor_exists():
    assert callable(ccsl::expressions::ArithmeticExpression.__init__)


def test_ccsl::expressions::arithmeticexpression_constructor_args():
    sig = inspect.signature(ccsl::expressions::ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())
    assert "arithmeticOperator" in params, "Missing parameter 'arithmeticOperator'"

def test_ccsl::expressions::arithmeticexpression_has_arithmeticOperator():
    assert hasattr(ccsl::expressions::ArithmeticExpression, "arithmeticOperator")
    descriptor = None
    for klass in ccsl::expressions::ArithmeticExpression.__mro__:
        if "arithmeticOperator" in klass.__dict__:
            descriptor = klass.__dict__["arithmeticOperator"]
            break
    assert isinstance(descriptor, property)



def test_ccsl::expressions::booleanexpression_is_not_abstract():
    assert not inspect.isabstract(ccsl::expressions::BooleanExpression)


def test_ccsl::expressions::booleanexpression_constructor_exists():
    assert callable(ccsl::expressions::BooleanExpression.__init__)


def test_ccsl::expressions::booleanexpression_constructor_args():
    sig = inspect.signature(ccsl::expressions::BooleanExpression.__init__)
    params = list(sig.parameters.keys())
    assert "booleanOperator" in params, "Missing parameter 'booleanOperator'"

def test_ccsl::expressions::booleanexpression_has_booleanOperator():
    assert hasattr(ccsl::expressions::BooleanExpression, "booleanOperator")
    descriptor = None
    for klass in ccsl::expressions::BooleanExpression.__mro__:
        if "booleanOperator" in klass.__dict__:
            descriptor = klass.__dict__["booleanOperator"]
            break
    assert isinstance(descriptor, property)



def test_ccsl::expressions::infixexpression_is_not_abstract():
    assert not inspect.isabstract(ccsl::expressions::InfixExpression)


def test_ccsl::expressions::infixexpression_constructor_exists():
    assert callable(ccsl::expressions::InfixExpression.__init__)


def test_ccsl::expressions::infixexpression_constructor_args():
    sig = inspect.signature(ccsl::expressions::InfixExpression.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::expressions::stringconcatenation_is_not_abstract():
    assert not inspect.isabstract(ccsl::expressions::StringConcatenation)


def test_ccsl::expressions::stringconcatenation_constructor_exists():
    assert callable(ccsl::expressions::StringConcatenation.__init__)


def test_ccsl::expressions::stringconcatenation_constructor_args():
    sig = inspect.signature(ccsl::expressions::StringConcatenation.__init__)
    params = list(sig.parameters.keys())



def test_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_block_constructor_exists():
    assert callable(Block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::controlflow::switchcaseblock_is_not_abstract():
    assert not inspect.isabstract(ccsl::controlFlow::SwitchCaseBlock)


def test_ccsl::controlflow::switchcaseblock_constructor_exists():
    assert callable(ccsl::controlFlow::SwitchCaseBlock.__init__)


def test_ccsl::controlflow::switchcaseblock_constructor_args():
    sig = inspect.signature(ccsl::controlFlow::SwitchCaseBlock.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_ccsl::controlflow::switchcaseblock_has_default():
    assert hasattr(ccsl::controlFlow::SwitchCaseBlock, "default")
    descriptor = None
    for klass in ccsl::controlFlow::SwitchCaseBlock.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_controlflow::switchcaseblock_is_not_abstract():
    assert not inspect.isabstract(controlFlow::SwitchCaseBlock)


def test_controlflow::switchcaseblock_constructor_exists():
    assert callable(controlFlow::SwitchCaseBlock.__init__)


def test_controlflow::switchcaseblock_constructor_args():
    sig = inspect.signature(controlFlow::SwitchCaseBlock.__init__)
    params = list(sig.parameters.keys())



def test_controlflow_is_not_abstract():
    assert not inspect.isabstract(ControlFlow)


def test_controlflow_constructor_exists():
    assert callable(ControlFlow.__init__)


def test_controlflow_constructor_args():
    sig = inspect.signature(ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::controlflow::ifstatement_is_not_abstract():
    assert not inspect.isabstract(ccsl::controlFlow::IfStatement)


def test_ccsl::controlflow::ifstatement_constructor_exists():
    assert callable(ccsl::controlFlow::IfStatement.__init__)


def test_ccsl::controlflow::ifstatement_constructor_args():
    sig = inspect.signature(ccsl::controlFlow::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::controlflow::loopstatement_is_not_abstract():
    assert not inspect.isabstract(ccsl::controlFlow::LoopStatement)


def test_ccsl::controlflow::loopstatement_constructor_exists():
    assert callable(ccsl::controlFlow::LoopStatement.__init__)


def test_ccsl::controlflow::loopstatement_constructor_args():
    sig = inspect.signature(ccsl::controlFlow::LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::controlflow::switchstatement_is_not_abstract():
    assert not inspect.isabstract(ccsl::controlFlow::SwitchStatement)


def test_ccsl::controlflow::switchstatement_constructor_exists():
    assert callable(ccsl::controlFlow::SwitchStatement.__init__)


def test_ccsl::controlflow::switchstatement_constructor_args():
    sig = inspect.signature(ccsl::controlFlow::SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_literalvalue_is_not_abstract():
    assert not inspect.isabstract(LiteralValue)


def test_literalvalue_constructor_exists():
    assert callable(LiteralValue.__init__)


def test_literalvalue_constructor_args():
    sig = inspect.signature(LiteralValue.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::literalvalues::stringliteral_is_not_abstract():
    assert not inspect.isabstract(ccsl::literalValues::StringLiteral)


def test_ccsl::literalvalues::stringliteral_constructor_exists():
    assert callable(ccsl::literalValues::StringLiteral.__init__)


def test_ccsl::literalvalues::stringliteral_constructor_args():
    sig = inspect.signature(ccsl::literalValues::StringLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::literalvalues::characterliteral_is_not_abstract():
    assert not inspect.isabstract(ccsl::literalValues::CharacterLiteral)


def test_ccsl::literalvalues::characterliteral_constructor_exists():
    assert callable(ccsl::literalValues::CharacterLiteral.__init__)


def test_ccsl::literalvalues::characterliteral_constructor_args():
    sig = inspect.signature(ccsl::literalValues::CharacterLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::literalvalues::numberliteral_is_not_abstract():
    assert not inspect.isabstract(ccsl::literalValues::NumberLiteral)


def test_ccsl::literalvalues::numberliteral_constructor_exists():
    assert callable(ccsl::literalValues::NumberLiteral.__init__)


def test_ccsl::literalvalues::numberliteral_constructor_args():
    sig = inspect.signature(ccsl::literalValues::NumberLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::literalvalues::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(ccsl::literalValues::BooleanLiteral)


def test_ccsl::literalvalues::booleanliteral_constructor_exists():
    assert callable(ccsl::literalValues::BooleanLiteral.__init__)


def test_ccsl::literalvalues::booleanliteral_constructor_args():
    sig = inspect.signature(ccsl::literalValues::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::literalvalues::nullliteral_is_not_abstract():
    assert not inspect.isabstract(ccsl::literalValues::NullLiteral)


def test_ccsl::literalvalues::nullliteral_constructor_exists():
    assert callable(ccsl::literalValues::NullLiteral.__init__)


def test_ccsl::literalvalues::nullliteral_constructor_args():
    sig = inspect.signature(ccsl::literalValues::NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::statements::throwstatement_is_not_abstract():
    assert not inspect.isabstract(ccsl::statements::ThrowStatement)


def test_ccsl::statements::throwstatement_constructor_exists():
    assert callable(ccsl::statements::ThrowStatement.__init__)


def test_ccsl::statements::throwstatement_constructor_args():
    sig = inspect.signature(ccsl::statements::ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::statements::returnstatement_is_not_abstract():
    assert not inspect.isabstract(ccsl::statements::ReturnStatement)


def test_ccsl::statements::returnstatement_constructor_exists():
    assert callable(ccsl::statements::ReturnStatement.__init__)


def test_ccsl::statements::returnstatement_constructor_args():
    sig = inspect.signature(ccsl::statements::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::statements::instanceof_is_not_abstract():
    assert not inspect.isabstract(ccsl::statements::InstanceOf)


def test_ccsl::statements::instanceof_constructor_exists():
    assert callable(ccsl::statements::InstanceOf.__init__)


def test_ccsl::statements::instanceof_constructor_args():
    sig = inspect.signature(ccsl::statements::InstanceOf.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::trycatch::catchclause_is_not_abstract():
    assert not inspect.isabstract(ccsl::tryCatch::CatchClause)


def test_ccsl::trycatch::catchclause_constructor_exists():
    assert callable(ccsl::tryCatch::CatchClause.__init__)


def test_ccsl::trycatch::catchclause_constructor_args():
    sig = inspect.signature(ccsl::tryCatch::CatchClause.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::literalvalues::literalvalue_is_not_abstract():
    assert not inspect.isabstract(ccsl::literalValues::LiteralValue)


def test_ccsl::literalvalues::literalvalue_constructor_exists():
    assert callable(ccsl::literalValues::LiteralValue.__init__)


def test_ccsl::literalvalues::literalvalue_constructor_args():
    sig = inspect.signature(ccsl::literalValues::LiteralValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ccsl::literalvalues::literalvalue_has_value():
    assert hasattr(ccsl::literalValues::LiteralValue, "value")
    descriptor = None
    for klass in ccsl::literalValues::LiteralValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ccsl::annotation::annotation_is_not_abstract():
    assert not inspect.isabstract(ccsl::annotation::Annotation)


def test_ccsl::annotation::annotation_constructor_exists():
    assert callable(ccsl::annotation::Annotation.__init__)


def test_ccsl::annotation::annotation_constructor_args():
    sig = inspect.signature(ccsl::annotation::Annotation.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::import::importstatement_is_not_abstract():
    assert not inspect.isabstract(ccsl::import::ImportStatement)


def test_ccsl::import::importstatement_constructor_exists():
    assert callable(ccsl::import::ImportStatement.__init__)


def test_ccsl::import::importstatement_constructor_args():
    sig = inspect.signature(ccsl::import::ImportStatement.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::statements::arraycreation_is_not_abstract():
    assert not inspect.isabstract(ccsl::statements::ArrayCreation)


def test_ccsl::statements::arraycreation_constructor_exists():
    assert callable(ccsl::statements::ArrayCreation.__init__)


def test_ccsl::statements::arraycreation_constructor_args():
    sig = inspect.signature(ccsl::statements::ArrayCreation.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::statements::breakstatement_is_not_abstract():
    assert not inspect.isabstract(ccsl::statements::BreakStatement)


def test_ccsl::statements::breakstatement_constructor_exists():
    assert callable(ccsl::statements::BreakStatement.__init__)


def test_ccsl::statements::breakstatement_constructor_args():
    sig = inspect.signature(ccsl::statements::BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::statements::thisstatement_is_not_abstract():
    assert not inspect.isabstract(ccsl::statements::ThisStatement)


def test_ccsl::statements::thisstatement_constructor_exists():
    assert callable(ccsl::statements::ThisStatement.__init__)


def test_ccsl::statements::thisstatement_constructor_args():
    sig = inspect.signature(ccsl::statements::ThisStatement.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::statements::continuestatement_is_not_abstract():
    assert not inspect.isabstract(ccsl::statements::ContinueStatement)


def test_ccsl::statements::continuestatement_constructor_exists():
    assert callable(ccsl::statements::ContinueStatement.__init__)


def test_ccsl::statements::continuestatement_constructor_args():
    sig = inspect.signature(ccsl::statements::ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::assignment::abstractassignment_is_not_abstract():
    assert not inspect.isabstract(ccsl::assignment::AbstractAssignment)


def test_ccsl::assignment::abstractassignment_constructor_exists():
    assert callable(ccsl::assignment::AbstractAssignment.__init__)


def test_ccsl::assignment::abstractassignment_constructor_args():
    sig = inspect.signature(ccsl::assignment::AbstractAssignment.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::trycatch::trystatement_is_not_abstract():
    assert not inspect.isabstract(ccsl::tryCatch::TryStatement)


def test_ccsl::trycatch::trystatement_constructor_exists():
    assert callable(ccsl::tryCatch::TryStatement.__init__)


def test_ccsl::trycatch::trystatement_constructor_args():
    sig = inspect.signature(ccsl::tryCatch::TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::expressions::parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(ccsl::expressions::ParenthesizedExpression)


def test_ccsl::expressions::parenthesizedexpression_constructor_exists():
    assert callable(ccsl::expressions::ParenthesizedExpression.__init__)


def test_ccsl::expressions::parenthesizedexpression_constructor_args():
    sig = inspect.signature(ccsl::expressions::ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::statements::synchronizedblock_is_not_abstract():
    assert not inspect.isabstract(ccsl::statements::SynchronizedBlock)


def test_ccsl::statements::synchronizedblock_constructor_exists():
    assert callable(ccsl::statements::SynchronizedBlock.__init__)


def test_ccsl::statements::synchronizedblock_constructor_args():
    sig = inspect.signature(ccsl::statements::SynchronizedBlock.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::statements::access_is_not_abstract():
    assert not inspect.isabstract(ccsl::statements::Access)


def test_ccsl::statements::access_constructor_exists():
    assert callable(ccsl::statements::Access.__init__)


def test_ccsl::statements::access_constructor_args():
    sig = inspect.signature(ccsl::statements::Access.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::invocation::invocation_is_not_abstract():
    assert not inspect.isabstract(ccsl::invocation::Invocation)


def test_ccsl::invocation::invocation_constructor_exists():
    assert callable(ccsl::invocation::Invocation.__init__)


def test_ccsl::invocation::invocation_constructor_args():
    sig = inspect.signature(ccsl::invocation::Invocation.__init__)
    params = list(sig.parameters.keys())
    assert "argsKind" in params, "Missing parameter 'argsKind'"

def test_ccsl::invocation::invocation_has_argsKind():
    assert hasattr(ccsl::invocation::Invocation, "argsKind")
    descriptor = None
    for klass in ccsl::invocation::Invocation.__mro__:
        if "argsKind" in klass.__dict__:
            descriptor = klass.__dict__["argsKind"]
            break
    assert isinstance(descriptor, property)



def test_ccsl::expressions::operatorexpression_is_not_abstract():
    assert not inspect.isabstract(ccsl::expressions::OperatorExpression)


def test_ccsl::expressions::operatorexpression_constructor_exists():
    assert callable(ccsl::expressions::OperatorExpression.__init__)


def test_ccsl::expressions::operatorexpression_constructor_args():
    sig = inspect.signature(ccsl::expressions::OperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::statements::emptystatement_is_not_abstract():
    assert not inspect.isabstract(ccsl::statements::EmptyStatement)


def test_ccsl::statements::emptystatement_constructor_exists():
    assert callable(ccsl::statements::EmptyStatement.__init__)


def test_ccsl::statements::emptystatement_constructor_args():
    sig = inspect.signature(ccsl::statements::EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::statements::namedelementaccess_is_not_abstract():
    assert not inspect.isabstract(ccsl::statements::NamedElementAccess)


def test_ccsl::statements::namedelementaccess_constructor_exists():
    assert callable(ccsl::statements::NamedElementAccess.__init__)


def test_ccsl::statements::namedelementaccess_constructor_args():
    sig = inspect.signature(ccsl::statements::NamedElementAccess.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::statements::statement_is_not_abstract():
    assert not inspect.isabstract(ccsl::statements::Statement)


def test_ccsl::statements::statement_constructor_exists():
    assert callable(ccsl::statements::Statement.__init__)


def test_ccsl::statements::statement_constructor_args():
    sig = inspect.signature(ccsl::statements::Statement.__init__)
    params = list(sig.parameters.keys())



def test_method::simplemethod_is_not_abstract():
    assert not inspect.isabstract(method::SimpleMethod)


def test_method::simplemethod_constructor_exists():
    assert callable(method::SimpleMethod.__init__)


def test_method::simplemethod_constructor_args():
    sig = inspect.signature(method::SimpleMethod.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::method::method_is_not_abstract():
    assert not inspect.isabstract(ccsl::method::Method)


def test_ccsl::method::method_constructor_exists():
    assert callable(ccsl::method::Method.__init__)


def test_ccsl::method::method_constructor_args():
    sig = inspect.signature(ccsl::method::Method.__init__)
    params = list(sig.parameters.keys())
    assert "inheritance" in params, "Missing parameter 'inheritance'"
    assert "final" in params, "Missing parameter 'final'"
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "static" in params, "Missing parameter 'static'"

def test_ccsl::method::method_has_inheritance():
    assert hasattr(ccsl::method::Method, "inheritance")
    descriptor = None
    for klass in ccsl::method::Method.__mro__:
        if "inheritance" in klass.__dict__:
            descriptor = klass.__dict__["inheritance"]
            break
    assert isinstance(descriptor, property)

def test_ccsl::method::method_has_final():
    assert hasattr(ccsl::method::Method, "final")
    descriptor = None
    for klass in ccsl::method::Method.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)

def test_ccsl::method::method_has_abstract():
    assert hasattr(ccsl::method::Method, "abstract")
    descriptor = None
    for klass in ccsl::method::Method.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)

def test_ccsl::method::method_has_static():
    assert hasattr(ccsl::method::Method, "static")
    descriptor = None
    for klass in ccsl::method::Method.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_variable::parametervariable_is_not_abstract():
    assert not inspect.isabstract(variable::ParameterVariable)


def test_variable::parametervariable_constructor_exists():
    assert callable(variable::ParameterVariable.__init__)


def test_variable::parametervariable_constructor_args():
    sig = inspect.signature(variable::ParameterVariable.__init__)
    params = list(sig.parameters.keys())



def test_elements::element_is_not_abstract():
    assert not inspect.isabstract(elements::Element)


def test_elements::element_constructor_exists():
    assert callable(elements::Element.__init__)


def test_elements::element_constructor_args():
    sig = inspect.signature(elements::Element.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::method::simplemethod_is_not_abstract():
    assert not inspect.isabstract(ccsl::method::SimpleMethod)


def test_ccsl::method::simplemethod_constructor_exists():
    assert callable(ccsl::method::SimpleMethod.__init__)


def test_ccsl::method::simplemethod_constructor_args():
    sig = inspect.signature(ccsl::method::SimpleMethod.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "paramsKind" in params, "Missing parameter 'paramsKind'"

def test_ccsl::method::simplemethod_has_visibility():
    assert hasattr(ccsl::method::SimpleMethod, "visibility")
    descriptor = None
    for klass in ccsl::method::SimpleMethod.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_ccsl::method::simplemethod_has_paramsKind():
    assert hasattr(ccsl::method::SimpleMethod, "paramsKind")
    descriptor = None
    for klass in ccsl::method::SimpleMethod.__mro__:
        if "paramsKind" in klass.__dict__:
            descriptor = klass.__dict__["paramsKind"]
            break
    assert isinstance(descriptor, property)



def test_simplemethod_is_not_abstract():
    assert not inspect.isabstract(SimpleMethod)


def test_simplemethod_constructor_exists():
    assert callable(SimpleMethod.__init__)


def test_simplemethod_constructor_args():
    sig = inspect.signature(SimpleMethod.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::method::constructor_is_not_abstract():
    assert not inspect.isabstract(ccsl::method::Constructor)


def test_ccsl::method::constructor_constructor_exists():
    assert callable(ccsl::method::Constructor.__init__)


def test_ccsl::method::constructor_constructor_args():
    sig = inspect.signature(ccsl::method::Constructor.__init__)
    params = list(sig.parameters.keys())
    assert "avaliableInSourceCode" in params, "Missing parameter 'avaliableInSourceCode'"

def test_ccsl::method::constructor_has_avaliableInSourceCode():
    assert hasattr(ccsl::method::Constructor, "avaliableInSourceCode")
    descriptor = None
    for klass in ccsl::method::Constructor.__mro__:
        if "avaliableInSourceCode" in klass.__dict__:
            descriptor = klass.__dict__["avaliableInSourceCode"]
            break
    assert isinstance(descriptor, property)



def test_ccsl::statements::instancecreation_is_not_abstract():
    assert not inspect.isabstract(ccsl::statements::InstanceCreation)


def test_ccsl::statements::instancecreation_constructor_exists():
    assert callable(ccsl::statements::InstanceCreation.__init__)


def test_ccsl::statements::instancecreation_constructor_args():
    sig = inspect.signature(ccsl::statements::InstanceCreation.__init__)
    params = list(sig.parameters.keys())
    assert "argsKind" in params, "Missing parameter 'argsKind'"

def test_ccsl::statements::instancecreation_has_argsKind():
    assert hasattr(ccsl::statements::InstanceCreation, "argsKind")
    descriptor = None
    for klass in ccsl::statements::InstanceCreation.__mro__:
        if "argsKind" in klass.__dict__:
            descriptor = klass.__dict__["argsKind"]
            break
    assert isinstance(descriptor, property)



def test_ccsl::statements::vardeclaration_is_not_abstract():
    assert not inspect.isabstract(ccsl::statements::VarDeclaration)


def test_ccsl::statements::vardeclaration_constructor_exists():
    assert callable(ccsl::statements::VarDeclaration.__init__)


def test_ccsl::statements::vardeclaration_constructor_args():
    sig = inspect.signature(ccsl::statements::VarDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::statements::block_is_not_abstract():
    assert not inspect.isabstract(ccsl::statements::Block)


def test_ccsl::statements::block_constructor_exists():
    assert callable(ccsl::statements::Block.__init__)


def test_ccsl::statements::block_constructor_args():
    sig = inspect.signature(ccsl::statements::Block.__init__)
    params = list(sig.parameters.keys())
    assert "statementsKind" in params, "Missing parameter 'statementsKind'"

def test_ccsl::statements::block_has_statementsKind():
    assert hasattr(ccsl::statements::Block, "statementsKind")
    descriptor = None
    for klass in ccsl::statements::Block.__mro__:
        if "statementsKind" in klass.__dict__:
            descriptor = klass.__dict__["statementsKind"]
            break
    assert isinstance(descriptor, property)



def test_ccsl::statements::controlflow_is_not_abstract():
    assert not inspect.isabstract(ccsl::statements::ControlFlow)


def test_ccsl::statements::controlflow_constructor_exists():
    assert callable(ccsl::statements::ControlFlow.__init__)


def test_ccsl::statements::controlflow_constructor_args():
    sig = inspect.signature(ccsl::statements::ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_access_is_not_abstract():
    assert not inspect.isabstract(Access)


def test_access_constructor_exists():
    assert callable(Access.__init__)


def test_access_constructor_args():
    sig = inspect.signature(Access.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::statements::datatypeaccess_is_not_abstract():
    assert not inspect.isabstract(ccsl::statements::DataTypeAccess)


def test_ccsl::statements::datatypeaccess_constructor_exists():
    assert callable(ccsl::statements::DataTypeAccess.__init__)


def test_ccsl::statements::datatypeaccess_constructor_args():
    sig = inspect.signature(ccsl::statements::DataTypeAccess.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::statements::variableaccess_is_not_abstract():
    assert not inspect.isabstract(ccsl::statements::VariableAccess)


def test_ccsl::statements::variableaccess_constructor_exists():
    assert callable(ccsl::statements::VariableAccess.__init__)


def test_ccsl::statements::variableaccess_constructor_args():
    sig = inspect.signature(ccsl::statements::VariableAccess.__init__)
    params = list(sig.parameters.keys())



def test_complextype::jclass_is_not_abstract():
    assert not inspect.isabstract(complexType::JClass)


def test_complextype::jclass_constructor_exists():
    assert callable(complexType::JClass.__init__)


def test_complextype::jclass_constructor_args():
    sig = inspect.signature(complexType::JClass.__init__)
    params = list(sig.parameters.keys())



def test_method::constructor_is_not_abstract():
    assert not inspect.isabstract(method::Constructor)


def test_method::constructor_constructor_exists():
    assert callable(method::Constructor.__init__)


def test_method::constructor_constructor_args():
    sig = inspect.signature(method::Constructor.__init__)
    params = list(sig.parameters.keys())



def test_datatype::objecttype_is_not_abstract():
    assert not inspect.isabstract(datatype::ObjectType)


def test_datatype::objecttype_constructor_exists():
    assert callable(datatype::ObjectType.__init__)


def test_datatype::objecttype_constructor_args():
    sig = inspect.signature(datatype::ObjectType.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::complextype::declaredtype_is_not_abstract():
    assert not inspect.isabstract(ccsl::complexType::DeclaredType)


def test_ccsl::complextype::declaredtype_constructor_exists():
    assert callable(ccsl::complexType::DeclaredType.__init__)


def test_ccsl::complextype::declaredtype_constructor_args():
    sig = inspect.signature(ccsl::complexType::DeclaredType.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "static" in params, "Missing parameter 'static'"

def test_ccsl::complextype::declaredtype_has_visibility():
    assert hasattr(ccsl::complexType::DeclaredType, "visibility")
    descriptor = None
    for klass in ccsl::complexType::DeclaredType.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_ccsl::complextype::declaredtype_has_static():
    assert hasattr(ccsl::complexType::DeclaredType, "static")
    descriptor = None
    for klass in ccsl::complexType::DeclaredType.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_complextype_is_not_abstract():
    assert not inspect.isabstract(ComplexType)


def test_complextype_constructor_exists():
    assert callable(ComplexType.__init__)


def test_complextype_constructor_args():
    sig = inspect.signature(ComplexType.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::datatype::generictype_is_not_abstract():
    assert not inspect.isabstract(ccsl::datatype::GenericType)


def test_ccsl::datatype::generictype_constructor_exists():
    assert callable(ccsl::datatype::GenericType.__init__)


def test_ccsl::datatype::generictype_constructor_args():
    sig = inspect.signature(ccsl::datatype::GenericType.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::complextype::anonymousclass_is_not_abstract():
    assert not inspect.isabstract(ccsl::complexType::AnonymousClass)


def test_ccsl::complextype::anonymousclass_constructor_exists():
    assert callable(ccsl::complexType::AnonymousClass.__init__)


def test_ccsl::complextype::anonymousclass_constructor_args():
    sig = inspect.signature(ccsl::complexType::AnonymousClass.__init__)
    params = list(sig.parameters.keys())



def test_complextype::complextype_is_not_abstract():
    assert not inspect.isabstract(complexType::ComplexType)


def test_complextype::complextype_constructor_exists():
    assert callable(complexType::ComplexType.__init__)


def test_complextype::complextype_constructor_args():
    sig = inspect.signature(complexType::ComplexType.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::complextype::jclass_is_not_abstract():
    assert not inspect.isabstract(ccsl::complexType::JClass)


def test_ccsl::complextype::jclass_constructor_exists():
    assert callable(ccsl::complexType::JClass.__init__)


def test_ccsl::complextype::jclass_constructor_args():
    sig = inspect.signature(ccsl::complexType::JClass.__init__)
    params = list(sig.parameters.keys())
    assert "inheritance" in params, "Missing parameter 'inheritance'"

def test_ccsl::complextype::jclass_has_inheritance():
    assert hasattr(ccsl::complexType::JClass, "inheritance")
    descriptor = None
    for klass in ccsl::complexType::JClass.__mro__:
        if "inheritance" in klass.__dict__:
            descriptor = klass.__dict__["inheritance"]
            break
    assert isinstance(descriptor, property)



def test_ccsl::complextype::jinterface_is_not_abstract():
    assert not inspect.isabstract(ccsl::complexType::JInterface)


def test_ccsl::complextype::jinterface_constructor_exists():
    assert callable(ccsl::complexType::JInterface.__init__)


def test_ccsl::complextype::jinterface_constructor_args():
    sig = inspect.signature(ccsl::complexType::JInterface.__init__)
    params = list(sig.parameters.keys())



def test_variable::initializablevariable_is_not_abstract():
    assert not inspect.isabstract(variable::InitializableVariable)


def test_variable::initializablevariable_constructor_exists():
    assert callable(variable::InitializableVariable.__init__)


def test_variable::initializablevariable_constructor_args():
    sig = inspect.signature(variable::InitializableVariable.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::variable::fieldvariable_is_not_abstract():
    assert not inspect.isabstract(ccsl::variable::FieldVariable)


def test_ccsl::variable::fieldvariable_constructor_exists():
    assert callable(ccsl::variable::FieldVariable.__init__)


def test_ccsl::variable::fieldvariable_constructor_args():
    sig = inspect.signature(ccsl::variable::FieldVariable.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "static" in params, "Missing parameter 'static'"

def test_ccsl::variable::fieldvariable_has_visibility():
    assert hasattr(ccsl::variable::FieldVariable, "visibility")
    descriptor = None
    for klass in ccsl::variable::FieldVariable.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_ccsl::variable::fieldvariable_has_static():
    assert hasattr(ccsl::variable::FieldVariable, "static")
    descriptor = None
    for klass in ccsl::variable::FieldVariable.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_statements::statement_is_not_abstract():
    assert not inspect.isabstract(statements::Statement)


def test_statements::statement_constructor_exists():
    assert callable(statements::Statement.__init__)


def test_statements::statement_constructor_args():
    sig = inspect.signature(statements::Statement.__init__)
    params = list(sig.parameters.keys())



def test_declaredtype_is_not_abstract():
    assert not inspect.isabstract(DeclaredType)


def test_declaredtype_constructor_exists():
    assert callable(DeclaredType.__init__)


def test_declaredtype_constructor_args():
    sig = inspect.signature(DeclaredType.__init__)
    params = list(sig.parameters.keys())



def test_ccsl::complextype::annotationtype_is_not_abstract():
    assert not inspect.isabstract(ccsl::complexType::AnnotationType)


def test_ccsl::complextype::annotationtype_constructor_exists():
    assert callable(ccsl::complexType::AnnotationType.__init__)


def test_ccsl::complextype::annotationtype_constructor_args():
    sig = inspect.signature(ccsl::complexType::AnnotationType.__init__)
    params = list(sig.parameters.keys())

def test_unaryassignmentoperator_exists():
    # Check that the Enumeration exists
    assert UnaryAssignmentOperator is not None

def test_unaryassignmentoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryAssignmentOperator]
    expected_literals = [
        "ANY",
        "DECREMENT",
        "INCREMENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryAssignmentOperator"

def test_logicoperator_exists():
    # Check that the Enumeration exists
    assert LogicOperator is not None

def test_logicoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LogicOperator]
    expected_literals = [
        "OR",
        "IF_THEN",
        "AND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LogicOperator"

def test_equationoperator_exists():
    # Check that the Enumeration exists
    assert EquationOperator is not None

def test_equationoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EquationOperator]
    expected_literals = [
        "PLUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EquationOperator"

def test_assignmentoperator_exists():
    # Check that the Enumeration exists
    assert AssignmentOperator is not None

def test_assignmentoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentOperator]
    expected_literals = [
        "PLUS_ASSIGN",
        "ANY",
        "ASSIGN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentOperator"

def test_inheritance_exists():
    # Check that the Enumeration exists
    assert Inheritance is not None

def test_inheritance_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Inheritance]
    expected_literals = [
        "ANY",
        "ABSTRACT",
        "NONE",
        "FINAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Inheritance"

def test_booleanoperator_exists():
    # Check that the Enumeration exists
    assert BooleanOperator is not None

def test_booleanoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanOperator]
    expected_literals = [
        "AND",
        "NOT",
        "LESS_THAN_OR_EQUAL_TO",
        "NOT_EQUAL_TO",
        "EQUAL_TO",
        "GREATER_THAN_OR_EQUAL_TO",
        "OR",
        "LESS_THAN",
        "GREATER_THAN",
        "ANY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BooleanOperator"

def test_arithmeticoperator_exists():
    # Check that the Enumeration exists
    assert ArithmeticOperator is not None

def test_arithmeticoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArithmeticOperator]
    expected_literals = [
        "MULTIPLICATION",
        "DIVISION",
        "SUBTRACTION",
        "ADDITION",
        "UNDEFINED",
        "MODULUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArithmeticOperator"

def test_visibility_exists():
    # Check that the Enumeration exists
    assert Visibility is not None

def test_visibility_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Visibility]
    expected_literals = [
        "ANY",
        "PRIVATE",
        "PROTECTED",
        "PUBLIC",
        "PACKAGE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Visibility"

def test_collectionkind_exists():
    # Check that the Enumeration exists
    assert CollectionKind is not None

def test_collectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CollectionKind]
    expected_literals = [
        "IMMEDIATE",
        "SEQUENCE",
        "EXACT",
        "ANY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CollectionKind"


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
method::Method_strategy = st.builds(
    method::Method,
)
variable::FieldVariable_strategy = st.builds(
    variable::FieldVariable,
)
import::ImportStatement_strategy = st.builds(
    import::ImportStatement,
)
complexType::JInterface_strategy = st.builds(
    complexType::JInterface,
)
ccsl::elements::Element_strategy = st.builds(
    ccsl::elements::Element,
    uniqueName=
        safe_text
)
InjectionStrategy_strategy = st.builds(
    InjectionStrategy,
)
InjectionAction_strategy = st.builds(
    InjectionAction,
)
ccsl::Root_strategy = st.builds(
    ccsl::Root,
)
Variable_strategy = st.builds(
    Variable,
)
ccsl::variable::InitializableVariable_strategy = st.builds(
    ccsl::variable::InitializableVariable,
)
InitializableVariable_strategy = st.builds(
    InitializableVariable,
)
ccsl::variable::LocalVariable_strategy = st.builds(
    ccsl::variable::LocalVariable,
)
annotation::AnnotableElement_strategy = st.builds(
    annotation::AnnotableElement,
)
variable::Variable_strategy = st.builds(
    variable::Variable,
)
ccsl::variable::ParameterVariable_strategy = st.builds(
    ccsl::variable::ParameterVariable,
)
datatype::DataType_strategy = st.builds(
    datatype::DataType,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
ccsl::variable::Variable_strategy = st.builds(
    ccsl::variable::Variable,
    final=
        safe_text
)
complexType::DeclaredType_strategy = st.builds(
    complexType::DeclaredType,
)
import::ImportableElement_strategy = st.builds(
    import::ImportableElement,
)
namedElements::NamedElement_strategy = st.builds(
    namedElements::NamedElement,
)
ccsl::namedElements::Package_strategy = st.builds(
    ccsl::namedElements::Package,
)
Context_strategy = st.builds(
    Context,
)
Element_strategy = st.builds(
    Element,
)
ccsl::complexType::ComplexType_strategy = st.builds(
    ccsl::complexType::ComplexType,
)
ccsl::namedElements::NamedElement_strategy = st.builds(
    ccsl::namedElements::NamedElement,
    avaliableInSourceCode=
        safe_text,
    name=
        safe_text
)
Rule_strategy = st.builds(
    Rule,
)
ccsl::AtomicRule_strategy = st.builds(
    ccsl::AtomicRule,
)
ccsl::CompositeRule_strategy = st.builds(
    ccsl::CompositeRule,
    operator=
        safe_text
)
Root_strategy = st.builds(
    Root,
)
ccsl::FaultTypeDescription_strategy = st.builds(
    ccsl::FaultTypeDescription,
    name=
        safe_text
)
ccsl::Rule_strategy = st.builds(
    ccsl::Rule,
    negated=
        safe_text
)
statements::Access_strategy = st.builds(
    statements::Access,
)
CcslNumberFunction_strategy = st.builds(
    CcslNumberFunction,
)
ccsl::numberFunctions::GetIndexOf_strategy = st.builds(
    ccsl::numberFunctions::GetIndexOf,
)
ccsl::numberFunctions::CcslIntegerLiteral_strategy = st.builds(
    ccsl::numberFunctions::CcslIntegerLiteral,
    value=
        safe_text
)
numberFunctions::CcslNumberFunction_strategy = st.builds(
    numberFunctions::CcslNumberFunction,
)
ccsl::filters::EquationFilter_strategy = st.builds(
    ccsl::filters::EquationFilter,
    operator=
        safe_text
)
AtomicFilter_strategy = st.builds(
    AtomicFilter,
)
ccsl::filters::TemplateFilter_strategy = st.builds(
    ccsl::filters::TemplateFilter,
)
ccsl::filters::FromClosureFilter_strategy = st.builds(
    ccsl::filters::FromClosureFilter,
)
ccsl::filters::SameNameFilter_strategy = st.builds(
    ccsl::filters::SameNameFilter,
    ignoreCase=
        safe_text
)
ccsl::filters::SuperClassClosureFilter_strategy = st.builds(
    ccsl::filters::SuperClassClosureFilter,
    includesSubClass=
        safe_text
)
ccsl::filters::ChildClosureComplexTypeFilter_strategy = st.builds(
    ccsl::filters::ChildClosureComplexTypeFilter,
)
ccsl::filters::IsStringFilter_strategy = st.builds(
    ccsl::filters::IsStringFilter,
)
ccsl::filters::SuperMethodClosureFilter_strategy = st.builds(
    ccsl::filters::SuperMethodClosureFilter,
)
ccsl::filters::HasSameReferenceFilter_strategy = st.builds(
    ccsl::filters::HasSameReferenceFilter,
)
ccsl::filters::IsKindOfFilter_strategy = st.builds(
    ccsl::filters::IsKindOfFilter,
)
ccsl::filters::BlockLastStatementFilter_strategy = st.builds(
    ccsl::filters::BlockLastStatementFilter,
)
ccsl::filters::IsTypeOfFilter_strategy = st.builds(
    ccsl::filters::IsTypeOfFilter,
)
ccsl::filters::PropertyFilter_strategy = st.builds(
    ccsl::filters::PropertyFilter,
)
Filter_strategy = st.builds(
    Filter,
)
ccsl::filters::CompositeFilter_strategy = st.builds(
    ccsl::filters::CompositeFilter,
    operator=
        safe_text
)
ccsl::filters::AtomicFilter_strategy = st.builds(
    ccsl::filters::AtomicFilter,
)
CcslBooleanFunction_strategy = st.builds(
    CcslBooleanFunction,
)
ccsl::filters::Filter_strategy = st.builds(
    ccsl::filters::Filter,
    negated=
        safe_text
)
CcslFunction_strategy = st.builds(
    CcslFunction,
)
ccsl::numberFunctions::CcslNumberFunction_strategy = st.builds(
    ccsl::numberFunctions::CcslNumberFunction,
)
ccsl::booleanFunctions::CcslBooleanFunction_strategy = st.builds(
    ccsl::booleanFunctions::CcslBooleanFunction,
)
ccsl::filters::ImplicityContainerFilter_strategy = st.builds(
    ccsl::filters::ImplicityContainerFilter,
)
expressions::OperatorExpression_strategy = st.builds(
    expressions::OperatorExpression,
)
TemplateFilter_strategy = st.builds(
    TemplateFilter,
)
ccsl::filters::ImplicityOperandFilter_strategy = st.builds(
    ccsl::filters::ImplicityOperandFilter,
)
ccsl::filters::RegexMatch_strategy = st.builds(
    ccsl::filters::RegexMatch,
    regex=
        safe_text
)
ccsl::filters::CountFilter_strategy = st.builds(
    ccsl::filters::CountFilter,
    max=
        safe_text,
    min=
        safe_text
)
ccsl::faultTypeDescription::InjectionAction_strategy = st.builds(
    ccsl::faultTypeDescription::InjectionAction,
)
filters::Filter_strategy = st.builds(
    filters::Filter,
)
ccsl::context::Context_strategy = st.builds(
    ccsl::context::Context,
)
ObjectType_strategy = st.builds(
    ObjectType,
)
ccsl::datatype::ArrayType_strategy = st.builds(
    ccsl::datatype::ArrayType,
    dimensions=
        safe_text
)
ccsl::datatype::ParameterizedType_strategy = st.builds(
    ccsl::datatype::ParameterizedType,
)
ccsl::functions::CcslFunction_strategy = st.builds(
    ccsl::functions::CcslFunction,
)
ccsl::strategy::AllStrategy_strategy = st.builds(
    ccsl::strategy::AllStrategy,
)
ccsl::action::ArithmeticOperatorMap_strategy = st.builds(
    ccsl::action::ArithmeticOperatorMap,
    newArithmeticOperator=
        safe_text,
    oldArithmeticOperator=
        safe_text
)
action::ArithmeticOperatorMap_strategy = st.builds(
    action::ArithmeticOperatorMap,
)
ccsl::action::ReplaceArithmeticOperatorAction_strategy = st.builds(
    ccsl::action::ReplaceArithmeticOperatorAction,
)
ccsl::action::ReplaceVariableAccessAction_strategy = st.builds(
    ccsl::action::ReplaceVariableAccessAction,
)
ccsl::action::DeleteRandomStatementAction_strategy = st.builds(
    ccsl::action::DeleteRandomStatementAction,
)
ccsl::action::ChangeLiteralValueAction_strategy = st.builds(
    ccsl::action::ChangeLiteralValueAction,
)
ccsl::action::DeleteInfixOperatorAction_strategy = st.builds(
    ccsl::action::DeleteInfixOperatorAction,
)
ccsl::action::MoveScopeUpAction_strategy = st.builds(
    ccsl::action::MoveScopeUpAction,
)
ccsl::action::DeleteAction_strategy = st.builds(
    ccsl::action::DeleteAction,
)
ccsl::faultTypeDescription::InjectionStrategy_strategy = st.builds(
    ccsl::faultTypeDescription::InjectionStrategy,
)
ccsl::import::ImportableElement_strategy = st.builds(
    ccsl::import::ImportableElement,
)
Invocation_strategy = st.builds(
    Invocation,
)
ccsl::invocation::SimpleMethodInvocation_strategy = st.builds(
    ccsl::invocation::SimpleMethodInvocation,
)
ccsl::invocation::ConstructorInvocation_strategy = st.builds(
    ccsl::invocation::ConstructorInvocation,
)
SimpleMethodInvocation_strategy = st.builds(
    SimpleMethodInvocation,
)
ccsl::invocation::SuperMethodInvocation_strategy = st.builds(
    ccsl::invocation::SuperMethodInvocation,
)
ccsl::invocation::MethodInvocation_strategy = st.builds(
    ccsl::invocation::MethodInvocation,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
ccsl::datatype::BooleanPrimitiveType_strategy = st.builds(
    ccsl::datatype::BooleanPrimitiveType,
)
ccsl::datatype::IntPrimitiveType_strategy = st.builds(
    ccsl::datatype::IntPrimitiveType,
)
ccsl::datatype::ShortPrimitiveType_strategy = st.builds(
    ccsl::datatype::ShortPrimitiveType,
)
ccsl::datatype::VoidType_strategy = st.builds(
    ccsl::datatype::VoidType,
)
ccsl::datatype::StringPrimitiveType_strategy = st.builds(
    ccsl::datatype::StringPrimitiveType,
)
DataType_strategy = st.builds(
    DataType,
)
ccsl::datatype::ObjectType_strategy = st.builds(
    ccsl::datatype::ObjectType,
)
ccsl::datatype::PrimitiveType_strategy = st.builds(
    ccsl::datatype::PrimitiveType,
)
ccsl::datatype::DataType_strategy = st.builds(
    ccsl::datatype::DataType,
)
annotation::Annotation_strategy = st.builds(
    annotation::Annotation,
)
ccsl::annotation::AnnotableElement_strategy = st.builds(
    ccsl::annotation::AnnotableElement,
    annotationsKind=
        safe_text
)
complexType::AnnotationType_strategy = st.builds(
    complexType::AnnotationType,
)
statements::Block_strategy = st.builds(
    statements::Block,
)
tryCatch::CatchClause_strategy = st.builds(
    tryCatch::CatchClause,
)
UnaryAssignment_strategy = st.builds(
    UnaryAssignment,
)
ccsl::assignment::PostfixUnaryAssignment_strategy = st.builds(
    ccsl::assignment::PostfixUnaryAssignment,
)
ccsl::assignment::PrefixUnaryAssignment_strategy = st.builds(
    ccsl::assignment::PrefixUnaryAssignment,
)
AbstractAssignment_strategy = st.builds(
    AbstractAssignment,
)
ccsl::assignment::UnaryAssignment_strategy = st.builds(
    ccsl::assignment::UnaryAssignment,
    operator=
        safe_text
)
ccsl::assignment::Assignment_strategy = st.builds(
    ccsl::assignment::Assignment,
    operator=
        safe_text
)
OperatorExpression_strategy = st.builds(
    OperatorExpression,
)
ccsl::expressions::ArithmeticExpression_strategy = st.builds(
    ccsl::expressions::ArithmeticExpression,
    arithmeticOperator=
        safe_text
)
ccsl::expressions::BooleanExpression_strategy = st.builds(
    ccsl::expressions::BooleanExpression,
    booleanOperator=
        safe_text
)
ccsl::expressions::InfixExpression_strategy = st.builds(
    ccsl::expressions::InfixExpression,
)
ccsl::expressions::StringConcatenation_strategy = st.builds(
    ccsl::expressions::StringConcatenation,
)
Block_strategy = st.builds(
    Block,
)
ccsl::controlFlow::SwitchCaseBlock_strategy = st.builds(
    ccsl::controlFlow::SwitchCaseBlock,
    default=
        safe_text
)
controlFlow::SwitchCaseBlock_strategy = st.builds(
    controlFlow::SwitchCaseBlock,
)
ControlFlow_strategy = st.builds(
    ControlFlow,
)
ccsl::controlFlow::IfStatement_strategy = st.builds(
    ccsl::controlFlow::IfStatement,
)
ccsl::controlFlow::LoopStatement_strategy = st.builds(
    ccsl::controlFlow::LoopStatement,
)
ccsl::controlFlow::SwitchStatement_strategy = st.builds(
    ccsl::controlFlow::SwitchStatement,
)
LiteralValue_strategy = st.builds(
    LiteralValue,
)
ccsl::literalValues::StringLiteral_strategy = st.builds(
    ccsl::literalValues::StringLiteral,
)
ccsl::literalValues::CharacterLiteral_strategy = st.builds(
    ccsl::literalValues::CharacterLiteral,
)
ccsl::literalValues::NumberLiteral_strategy = st.builds(
    ccsl::literalValues::NumberLiteral,
)
ccsl::literalValues::BooleanLiteral_strategy = st.builds(
    ccsl::literalValues::BooleanLiteral,
)
ccsl::literalValues::NullLiteral_strategy = st.builds(
    ccsl::literalValues::NullLiteral,
)
ccsl::statements::ThrowStatement_strategy = st.builds(
    ccsl::statements::ThrowStatement,
)
Statement_strategy = st.builds(
    Statement,
)
ccsl::statements::ReturnStatement_strategy = st.builds(
    ccsl::statements::ReturnStatement,
)
ccsl::statements::InstanceOf_strategy = st.builds(
    ccsl::statements::InstanceOf,
)
ccsl::tryCatch::CatchClause_strategy = st.builds(
    ccsl::tryCatch::CatchClause,
)
ccsl::literalValues::LiteralValue_strategy = st.builds(
    ccsl::literalValues::LiteralValue,
    value=
        safe_text
)
ccsl::annotation::Annotation_strategy = st.builds(
    ccsl::annotation::Annotation,
)
ccsl::import::ImportStatement_strategy = st.builds(
    ccsl::import::ImportStatement,
)
ccsl::statements::ArrayCreation_strategy = st.builds(
    ccsl::statements::ArrayCreation,
)
ccsl::statements::BreakStatement_strategy = st.builds(
    ccsl::statements::BreakStatement,
)
ccsl::statements::ThisStatement_strategy = st.builds(
    ccsl::statements::ThisStatement,
)
ccsl::statements::ContinueStatement_strategy = st.builds(
    ccsl::statements::ContinueStatement,
)
ccsl::assignment::AbstractAssignment_strategy = st.builds(
    ccsl::assignment::AbstractAssignment,
)
ccsl::tryCatch::TryStatement_strategy = st.builds(
    ccsl::tryCatch::TryStatement,
)
ccsl::expressions::ParenthesizedExpression_strategy = st.builds(
    ccsl::expressions::ParenthesizedExpression,
)
ccsl::statements::SynchronizedBlock_strategy = st.builds(
    ccsl::statements::SynchronizedBlock,
)
ccsl::statements::Access_strategy = st.builds(
    ccsl::statements::Access,
)
ccsl::invocation::Invocation_strategy = st.builds(
    ccsl::invocation::Invocation,
    argsKind=
        safe_text
)
ccsl::expressions::OperatorExpression_strategy = st.builds(
    ccsl::expressions::OperatorExpression,
)
ccsl::statements::EmptyStatement_strategy = st.builds(
    ccsl::statements::EmptyStatement,
)
ccsl::statements::NamedElementAccess_strategy = st.builds(
    ccsl::statements::NamedElementAccess,
)
ccsl::statements::Statement_strategy = st.builds(
    ccsl::statements::Statement,
)
method::SimpleMethod_strategy = st.builds(
    method::SimpleMethod,
)
ccsl::method::Method_strategy = st.builds(
    ccsl::method::Method,
    inheritance=
        safe_text,
    final=
        safe_text,
    abstract=
        safe_text,
    static=
        safe_text
)
variable::ParameterVariable_strategy = st.builds(
    variable::ParameterVariable,
)
elements::Element_strategy = st.builds(
    elements::Element,
)
ccsl::method::SimpleMethod_strategy = st.builds(
    ccsl::method::SimpleMethod,
    visibility=
        safe_text,
    paramsKind=
        safe_text
)
SimpleMethod_strategy = st.builds(
    SimpleMethod,
)
ccsl::method::Constructor_strategy = st.builds(
    ccsl::method::Constructor,
    avaliableInSourceCode=
        safe_text
)
ccsl::statements::InstanceCreation_strategy = st.builds(
    ccsl::statements::InstanceCreation,
    argsKind=
        safe_text
)
ccsl::statements::VarDeclaration_strategy = st.builds(
    ccsl::statements::VarDeclaration,
)
ccsl::statements::Block_strategy = st.builds(
    ccsl::statements::Block,
    statementsKind=
        safe_text
)
ccsl::statements::ControlFlow_strategy = st.builds(
    ccsl::statements::ControlFlow,
)
Access_strategy = st.builds(
    Access,
)
ccsl::statements::DataTypeAccess_strategy = st.builds(
    ccsl::statements::DataTypeAccess,
)
ccsl::statements::VariableAccess_strategy = st.builds(
    ccsl::statements::VariableAccess,
)
complexType::JClass_strategy = st.builds(
    complexType::JClass,
)
method::Constructor_strategy = st.builds(
    method::Constructor,
)
datatype::ObjectType_strategy = st.builds(
    datatype::ObjectType,
)
ccsl::complexType::DeclaredType_strategy = st.builds(
    ccsl::complexType::DeclaredType,
    visibility=
        safe_text,
    static=
        safe_text
)
ComplexType_strategy = st.builds(
    ComplexType,
)
ccsl::datatype::GenericType_strategy = st.builds(
    ccsl::datatype::GenericType,
)
ccsl::complexType::AnonymousClass_strategy = st.builds(
    ccsl::complexType::AnonymousClass,
)
complexType::ComplexType_strategy = st.builds(
    complexType::ComplexType,
)
ccsl::complexType::JClass_strategy = st.builds(
    ccsl::complexType::JClass,
    inheritance=
        safe_text
)
ccsl::complexType::JInterface_strategy = st.builds(
    ccsl::complexType::JInterface,
)
variable::InitializableVariable_strategy = st.builds(
    variable::InitializableVariable,
)
ccsl::variable::FieldVariable_strategy = st.builds(
    ccsl::variable::FieldVariable,
    visibility=
        safe_text,
    static=
        safe_text
)
statements::Statement_strategy = st.builds(
    statements::Statement,
)
DeclaredType_strategy = st.builds(
    DeclaredType,
)
ccsl::complexType::AnnotationType_strategy = st.builds(
    ccsl::complexType::AnnotationType,
)

@given(instance=method::Method_strategy)
@settings(max_examples=50)
def test_method::method_instantiation(instance):
    assert isinstance(instance, method::Method)

@given(instance=variable::FieldVariable_strategy)
@settings(max_examples=50)
def test_variable::fieldvariable_instantiation(instance):
    assert isinstance(instance, variable::FieldVariable)

@given(instance=import::ImportStatement_strategy)
@settings(max_examples=50)
def test_import::importstatement_instantiation(instance):
    assert isinstance(instance, import::ImportStatement)

@given(instance=complexType::JInterface_strategy)
@settings(max_examples=50)
def test_complextype::jinterface_instantiation(instance):
    assert isinstance(instance, complexType::JInterface)

@given(instance=ccsl::elements::Element_strategy)
@settings(max_examples=50)
def test_ccsl::elements::element_instantiation(instance):
    assert isinstance(instance, ccsl::elements::Element)

@given(instance=ccsl::elements::Element_strategy)
def test_ccsl::elements::element_uniqueName_type(instance):
    assert isinstance(instance.uniqueName, str)


@given(instance=ccsl::elements::Element_strategy)
def test_ccsl::elements::element_uniqueName_setter(instance):
    original = instance.uniqueName
    instance.uniqueName = original
    assert instance.uniqueName == original

@given(instance=InjectionStrategy_strategy)
@settings(max_examples=50)
def test_injectionstrategy_instantiation(instance):
    assert isinstance(instance, InjectionStrategy)

@given(instance=InjectionAction_strategy)
@settings(max_examples=50)
def test_injectionaction_instantiation(instance):
    assert isinstance(instance, InjectionAction)

@given(instance=ccsl::Root_strategy)
@settings(max_examples=50)
def test_ccsl::root_instantiation(instance):
    assert isinstance(instance, ccsl::Root)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=ccsl::variable::InitializableVariable_strategy)
@settings(max_examples=50)
def test_ccsl::variable::initializablevariable_instantiation(instance):
    assert isinstance(instance, ccsl::variable::InitializableVariable)

@given(instance=InitializableVariable_strategy)
@settings(max_examples=50)
def test_initializablevariable_instantiation(instance):
    assert isinstance(instance, InitializableVariable)

@given(instance=ccsl::variable::LocalVariable_strategy)
@settings(max_examples=50)
def test_ccsl::variable::localvariable_instantiation(instance):
    assert isinstance(instance, ccsl::variable::LocalVariable)

@given(instance=annotation::AnnotableElement_strategy)
@settings(max_examples=50)
def test_annotation::annotableelement_instantiation(instance):
    assert isinstance(instance, annotation::AnnotableElement)

@given(instance=variable::Variable_strategy)
@settings(max_examples=50)
def test_variable::variable_instantiation(instance):
    assert isinstance(instance, variable::Variable)

@given(instance=ccsl::variable::ParameterVariable_strategy)
@settings(max_examples=50)
def test_ccsl::variable::parametervariable_instantiation(instance):
    assert isinstance(instance, ccsl::variable::ParameterVariable)

@given(instance=datatype::DataType_strategy)
@settings(max_examples=50)
def test_datatype::datatype_instantiation(instance):
    assert isinstance(instance, datatype::DataType)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=ccsl::variable::Variable_strategy)
@settings(max_examples=50)
def test_ccsl::variable::variable_instantiation(instance):
    assert isinstance(instance, ccsl::variable::Variable)

@given(instance=ccsl::variable::Variable_strategy)
def test_ccsl::variable::variable_final_type(instance):
    assert isinstance(instance.final, str)


@given(instance=ccsl::variable::Variable_strategy)
def test_ccsl::variable::variable_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original

@given(instance=complexType::DeclaredType_strategy)
@settings(max_examples=50)
def test_complextype::declaredtype_instantiation(instance):
    assert isinstance(instance, complexType::DeclaredType)

@given(instance=import::ImportableElement_strategy)
@settings(max_examples=50)
def test_import::importableelement_instantiation(instance):
    assert isinstance(instance, import::ImportableElement)

@given(instance=namedElements::NamedElement_strategy)
@settings(max_examples=50)
def test_namedelements::namedelement_instantiation(instance):
    assert isinstance(instance, namedElements::NamedElement)

@given(instance=ccsl::namedElements::Package_strategy)
@settings(max_examples=50)
def test_ccsl::namedelements::package_instantiation(instance):
    assert isinstance(instance, ccsl::namedElements::Package)

@given(instance=Context_strategy)
@settings(max_examples=50)
def test_context_instantiation(instance):
    assert isinstance(instance, Context)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=ccsl::complexType::ComplexType_strategy)
@settings(max_examples=50)
def test_ccsl::complextype::complextype_instantiation(instance):
    assert isinstance(instance, ccsl::complexType::ComplexType)

@given(instance=ccsl::namedElements::NamedElement_strategy)
@settings(max_examples=50)
def test_ccsl::namedelements::namedelement_instantiation(instance):
    assert isinstance(instance, ccsl::namedElements::NamedElement)

@given(instance=ccsl::namedElements::NamedElement_strategy)
def test_ccsl::namedelements::namedelement_avaliableInSourceCode_type(instance):
    assert isinstance(instance.avaliableInSourceCode, str)


@given(instance=ccsl::namedElements::NamedElement_strategy)
def test_ccsl::namedelements::namedelement_avaliableInSourceCode_setter(instance):
    original = instance.avaliableInSourceCode
    instance.avaliableInSourceCode = original
    assert instance.avaliableInSourceCode == original

@given(instance=ccsl::namedElements::NamedElement_strategy)
def test_ccsl::namedelements::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ccsl::namedElements::NamedElement_strategy)
def test_ccsl::namedelements::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Rule_strategy)
@settings(max_examples=50)
def test_rule_instantiation(instance):
    assert isinstance(instance, Rule)

@given(instance=ccsl::AtomicRule_strategy)
@settings(max_examples=50)
def test_ccsl::atomicrule_instantiation(instance):
    assert isinstance(instance, ccsl::AtomicRule)

@given(instance=ccsl::CompositeRule_strategy)
@settings(max_examples=50)
def test_ccsl::compositerule_instantiation(instance):
    assert isinstance(instance, ccsl::CompositeRule)

@given(instance=ccsl::CompositeRule_strategy)
def test_ccsl::compositerule_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=ccsl::CompositeRule_strategy)
def test_ccsl::compositerule_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Root_strategy)
@settings(max_examples=50)
def test_root_instantiation(instance):
    assert isinstance(instance, Root)

@given(instance=ccsl::FaultTypeDescription_strategy)
@settings(max_examples=50)
def test_ccsl::faulttypedescription_instantiation(instance):
    assert isinstance(instance, ccsl::FaultTypeDescription)

@given(instance=ccsl::FaultTypeDescription_strategy)
def test_ccsl::faulttypedescription_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ccsl::FaultTypeDescription_strategy)
def test_ccsl::faulttypedescription_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ccsl::Rule_strategy)
@settings(max_examples=50)
def test_ccsl::rule_instantiation(instance):
    assert isinstance(instance, ccsl::Rule)

@given(instance=ccsl::Rule_strategy)
def test_ccsl::rule_negated_type(instance):
    assert isinstance(instance.negated, str)


@given(instance=ccsl::Rule_strategy)
def test_ccsl::rule_negated_setter(instance):
    original = instance.negated
    instance.negated = original
    assert instance.negated == original

@given(instance=statements::Access_strategy)
@settings(max_examples=50)
def test_statements::access_instantiation(instance):
    assert isinstance(instance, statements::Access)

@given(instance=CcslNumberFunction_strategy)
@settings(max_examples=50)
def test_ccslnumberfunction_instantiation(instance):
    assert isinstance(instance, CcslNumberFunction)

@given(instance=ccsl::numberFunctions::GetIndexOf_strategy)
@settings(max_examples=50)
def test_ccsl::numberfunctions::getindexof_instantiation(instance):
    assert isinstance(instance, ccsl::numberFunctions::GetIndexOf)

@given(instance=ccsl::numberFunctions::CcslIntegerLiteral_strategy)
@settings(max_examples=50)
def test_ccsl::numberfunctions::ccslintegerliteral_instantiation(instance):
    assert isinstance(instance, ccsl::numberFunctions::CcslIntegerLiteral)

@given(instance=ccsl::numberFunctions::CcslIntegerLiteral_strategy)
def test_ccsl::numberfunctions::ccslintegerliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ccsl::numberFunctions::CcslIntegerLiteral_strategy)
def test_ccsl::numberfunctions::ccslintegerliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=numberFunctions::CcslNumberFunction_strategy)
@settings(max_examples=50)
def test_numberfunctions::ccslnumberfunction_instantiation(instance):
    assert isinstance(instance, numberFunctions::CcslNumberFunction)

@given(instance=ccsl::filters::EquationFilter_strategy)
@settings(max_examples=50)
def test_ccsl::filters::equationfilter_instantiation(instance):
    assert isinstance(instance, ccsl::filters::EquationFilter)

@given(instance=ccsl::filters::EquationFilter_strategy)
def test_ccsl::filters::equationfilter_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=ccsl::filters::EquationFilter_strategy)
def test_ccsl::filters::equationfilter_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=AtomicFilter_strategy)
@settings(max_examples=50)
def test_atomicfilter_instantiation(instance):
    assert isinstance(instance, AtomicFilter)

@given(instance=ccsl::filters::TemplateFilter_strategy)
@settings(max_examples=50)
def test_ccsl::filters::templatefilter_instantiation(instance):
    assert isinstance(instance, ccsl::filters::TemplateFilter)

@given(instance=ccsl::filters::FromClosureFilter_strategy)
@settings(max_examples=50)
def test_ccsl::filters::fromclosurefilter_instantiation(instance):
    assert isinstance(instance, ccsl::filters::FromClosureFilter)

@given(instance=ccsl::filters::SameNameFilter_strategy)
@settings(max_examples=50)
def test_ccsl::filters::samenamefilter_instantiation(instance):
    assert isinstance(instance, ccsl::filters::SameNameFilter)

@given(instance=ccsl::filters::SameNameFilter_strategy)
def test_ccsl::filters::samenamefilter_ignoreCase_type(instance):
    assert isinstance(instance.ignoreCase, str)


@given(instance=ccsl::filters::SameNameFilter_strategy)
def test_ccsl::filters::samenamefilter_ignoreCase_setter(instance):
    original = instance.ignoreCase
    instance.ignoreCase = original
    assert instance.ignoreCase == original

@given(instance=ccsl::filters::SuperClassClosureFilter_strategy)
@settings(max_examples=50)
def test_ccsl::filters::superclassclosurefilter_instantiation(instance):
    assert isinstance(instance, ccsl::filters::SuperClassClosureFilter)

@given(instance=ccsl::filters::SuperClassClosureFilter_strategy)
def test_ccsl::filters::superclassclosurefilter_includesSubClass_type(instance):
    assert isinstance(instance.includesSubClass, str)


@given(instance=ccsl::filters::SuperClassClosureFilter_strategy)
def test_ccsl::filters::superclassclosurefilter_includesSubClass_setter(instance):
    original = instance.includesSubClass
    instance.includesSubClass = original
    assert instance.includesSubClass == original

@given(instance=ccsl::filters::ChildClosureComplexTypeFilter_strategy)
@settings(max_examples=50)
def test_ccsl::filters::childclosurecomplextypefilter_instantiation(instance):
    assert isinstance(instance, ccsl::filters::ChildClosureComplexTypeFilter)

@given(instance=ccsl::filters::IsStringFilter_strategy)
@settings(max_examples=50)
def test_ccsl::filters::isstringfilter_instantiation(instance):
    assert isinstance(instance, ccsl::filters::IsStringFilter)

@given(instance=ccsl::filters::SuperMethodClosureFilter_strategy)
@settings(max_examples=50)
def test_ccsl::filters::supermethodclosurefilter_instantiation(instance):
    assert isinstance(instance, ccsl::filters::SuperMethodClosureFilter)

@given(instance=ccsl::filters::HasSameReferenceFilter_strategy)
@settings(max_examples=50)
def test_ccsl::filters::hassamereferencefilter_instantiation(instance):
    assert isinstance(instance, ccsl::filters::HasSameReferenceFilter)

@given(instance=ccsl::filters::IsKindOfFilter_strategy)
@settings(max_examples=50)
def test_ccsl::filters::iskindoffilter_instantiation(instance):
    assert isinstance(instance, ccsl::filters::IsKindOfFilter)

@given(instance=ccsl::filters::BlockLastStatementFilter_strategy)
@settings(max_examples=50)
def test_ccsl::filters::blocklaststatementfilter_instantiation(instance):
    assert isinstance(instance, ccsl::filters::BlockLastStatementFilter)

@given(instance=ccsl::filters::IsTypeOfFilter_strategy)
@settings(max_examples=50)
def test_ccsl::filters::istypeoffilter_instantiation(instance):
    assert isinstance(instance, ccsl::filters::IsTypeOfFilter)

@given(instance=ccsl::filters::PropertyFilter_strategy)
@settings(max_examples=50)
def test_ccsl::filters::propertyfilter_instantiation(instance):
    assert isinstance(instance, ccsl::filters::PropertyFilter)

@given(instance=Filter_strategy)
@settings(max_examples=50)
def test_filter_instantiation(instance):
    assert isinstance(instance, Filter)

@given(instance=ccsl::filters::CompositeFilter_strategy)
@settings(max_examples=50)
def test_ccsl::filters::compositefilter_instantiation(instance):
    assert isinstance(instance, ccsl::filters::CompositeFilter)

@given(instance=ccsl::filters::CompositeFilter_strategy)
def test_ccsl::filters::compositefilter_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=ccsl::filters::CompositeFilter_strategy)
def test_ccsl::filters::compositefilter_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ccsl::filters::AtomicFilter_strategy)
@settings(max_examples=50)
def test_ccsl::filters::atomicfilter_instantiation(instance):
    assert isinstance(instance, ccsl::filters::AtomicFilter)

@given(instance=CcslBooleanFunction_strategy)
@settings(max_examples=50)
def test_ccslbooleanfunction_instantiation(instance):
    assert isinstance(instance, CcslBooleanFunction)

@given(instance=ccsl::filters::Filter_strategy)
@settings(max_examples=50)
def test_ccsl::filters::filter_instantiation(instance):
    assert isinstance(instance, ccsl::filters::Filter)

@given(instance=ccsl::filters::Filter_strategy)
def test_ccsl::filters::filter_negated_type(instance):
    assert isinstance(instance.negated, str)


@given(instance=ccsl::filters::Filter_strategy)
def test_ccsl::filters::filter_negated_setter(instance):
    original = instance.negated
    instance.negated = original
    assert instance.negated == original

@given(instance=CcslFunction_strategy)
@settings(max_examples=50)
def test_ccslfunction_instantiation(instance):
    assert isinstance(instance, CcslFunction)

@given(instance=ccsl::numberFunctions::CcslNumberFunction_strategy)
@settings(max_examples=50)
def test_ccsl::numberfunctions::ccslnumberfunction_instantiation(instance):
    assert isinstance(instance, ccsl::numberFunctions::CcslNumberFunction)

@given(instance=ccsl::booleanFunctions::CcslBooleanFunction_strategy)
@settings(max_examples=50)
def test_ccsl::booleanfunctions::ccslbooleanfunction_instantiation(instance):
    assert isinstance(instance, ccsl::booleanFunctions::CcslBooleanFunction)

@given(instance=ccsl::filters::ImplicityContainerFilter_strategy)
@settings(max_examples=50)
def test_ccsl::filters::implicitycontainerfilter_instantiation(instance):
    assert isinstance(instance, ccsl::filters::ImplicityContainerFilter)

@given(instance=expressions::OperatorExpression_strategy)
@settings(max_examples=50)
def test_expressions::operatorexpression_instantiation(instance):
    assert isinstance(instance, expressions::OperatorExpression)

@given(instance=TemplateFilter_strategy)
@settings(max_examples=50)
def test_templatefilter_instantiation(instance):
    assert isinstance(instance, TemplateFilter)

@given(instance=ccsl::filters::ImplicityOperandFilter_strategy)
@settings(max_examples=50)
def test_ccsl::filters::implicityoperandfilter_instantiation(instance):
    assert isinstance(instance, ccsl::filters::ImplicityOperandFilter)

@given(instance=ccsl::filters::RegexMatch_strategy)
@settings(max_examples=50)
def test_ccsl::filters::regexmatch_instantiation(instance):
    assert isinstance(instance, ccsl::filters::RegexMatch)

@given(instance=ccsl::filters::RegexMatch_strategy)
def test_ccsl::filters::regexmatch_regex_type(instance):
    assert isinstance(instance.regex, str)


@given(instance=ccsl::filters::RegexMatch_strategy)
def test_ccsl::filters::regexmatch_regex_setter(instance):
    original = instance.regex
    instance.regex = original
    assert instance.regex == original

@given(instance=ccsl::filters::CountFilter_strategy)
@settings(max_examples=50)
def test_ccsl::filters::countfilter_instantiation(instance):
    assert isinstance(instance, ccsl::filters::CountFilter)

@given(instance=ccsl::filters::CountFilter_strategy)
def test_ccsl::filters::countfilter_max_type(instance):
    assert isinstance(instance.max, str)


@given(instance=ccsl::filters::CountFilter_strategy)
def test_ccsl::filters::countfilter_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=ccsl::filters::CountFilter_strategy)
def test_ccsl::filters::countfilter_min_type(instance):
    assert isinstance(instance.min, str)


@given(instance=ccsl::filters::CountFilter_strategy)
def test_ccsl::filters::countfilter_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=ccsl::faultTypeDescription::InjectionAction_strategy)
@settings(max_examples=50)
def test_ccsl::faulttypedescription::injectionaction_instantiation(instance):
    assert isinstance(instance, ccsl::faultTypeDescription::InjectionAction)

@given(instance=filters::Filter_strategy)
@settings(max_examples=50)
def test_filters::filter_instantiation(instance):
    assert isinstance(instance, filters::Filter)

@given(instance=ccsl::context::Context_strategy)
@settings(max_examples=50)
def test_ccsl::context::context_instantiation(instance):
    assert isinstance(instance, ccsl::context::Context)

@given(instance=ObjectType_strategy)
@settings(max_examples=50)
def test_objecttype_instantiation(instance):
    assert isinstance(instance, ObjectType)

@given(instance=ccsl::datatype::ArrayType_strategy)
@settings(max_examples=50)
def test_ccsl::datatype::arraytype_instantiation(instance):
    assert isinstance(instance, ccsl::datatype::ArrayType)

@given(instance=ccsl::datatype::ArrayType_strategy)
def test_ccsl::datatype::arraytype_dimensions_type(instance):
    assert isinstance(instance.dimensions, str)


@given(instance=ccsl::datatype::ArrayType_strategy)
def test_ccsl::datatype::arraytype_dimensions_setter(instance):
    original = instance.dimensions
    instance.dimensions = original
    assert instance.dimensions == original

@given(instance=ccsl::datatype::ParameterizedType_strategy)
@settings(max_examples=50)
def test_ccsl::datatype::parameterizedtype_instantiation(instance):
    assert isinstance(instance, ccsl::datatype::ParameterizedType)

@given(instance=ccsl::functions::CcslFunction_strategy)
@settings(max_examples=50)
def test_ccsl::functions::ccslfunction_instantiation(instance):
    assert isinstance(instance, ccsl::functions::CcslFunction)

@given(instance=ccsl::strategy::AllStrategy_strategy)
@settings(max_examples=50)
def test_ccsl::strategy::allstrategy_instantiation(instance):
    assert isinstance(instance, ccsl::strategy::AllStrategy)

@given(instance=ccsl::action::ArithmeticOperatorMap_strategy)
@settings(max_examples=50)
def test_ccsl::action::arithmeticoperatormap_instantiation(instance):
    assert isinstance(instance, ccsl::action::ArithmeticOperatorMap)

@given(instance=ccsl::action::ArithmeticOperatorMap_strategy)
def test_ccsl::action::arithmeticoperatormap_newArithmeticOperator_type(instance):
    assert isinstance(instance.newArithmeticOperator, str)


@given(instance=ccsl::action::ArithmeticOperatorMap_strategy)
def test_ccsl::action::arithmeticoperatormap_newArithmeticOperator_setter(instance):
    original = instance.newArithmeticOperator
    instance.newArithmeticOperator = original
    assert instance.newArithmeticOperator == original

@given(instance=ccsl::action::ArithmeticOperatorMap_strategy)
def test_ccsl::action::arithmeticoperatormap_oldArithmeticOperator_type(instance):
    assert isinstance(instance.oldArithmeticOperator, str)


@given(instance=ccsl::action::ArithmeticOperatorMap_strategy)
def test_ccsl::action::arithmeticoperatormap_oldArithmeticOperator_setter(instance):
    original = instance.oldArithmeticOperator
    instance.oldArithmeticOperator = original
    assert instance.oldArithmeticOperator == original

@given(instance=action::ArithmeticOperatorMap_strategy)
@settings(max_examples=50)
def test_action::arithmeticoperatormap_instantiation(instance):
    assert isinstance(instance, action::ArithmeticOperatorMap)

@given(instance=ccsl::action::ReplaceArithmeticOperatorAction_strategy)
@settings(max_examples=50)
def test_ccsl::action::replacearithmeticoperatoraction_instantiation(instance):
    assert isinstance(instance, ccsl::action::ReplaceArithmeticOperatorAction)

@given(instance=ccsl::action::ReplaceVariableAccessAction_strategy)
@settings(max_examples=50)
def test_ccsl::action::replacevariableaccessaction_instantiation(instance):
    assert isinstance(instance, ccsl::action::ReplaceVariableAccessAction)

@given(instance=ccsl::action::DeleteRandomStatementAction_strategy)
@settings(max_examples=50)
def test_ccsl::action::deleterandomstatementaction_instantiation(instance):
    assert isinstance(instance, ccsl::action::DeleteRandomStatementAction)

@given(instance=ccsl::action::ChangeLiteralValueAction_strategy)
@settings(max_examples=50)
def test_ccsl::action::changeliteralvalueaction_instantiation(instance):
    assert isinstance(instance, ccsl::action::ChangeLiteralValueAction)

@given(instance=ccsl::action::DeleteInfixOperatorAction_strategy)
@settings(max_examples=50)
def test_ccsl::action::deleteinfixoperatoraction_instantiation(instance):
    assert isinstance(instance, ccsl::action::DeleteInfixOperatorAction)

@given(instance=ccsl::action::MoveScopeUpAction_strategy)
@settings(max_examples=50)
def test_ccsl::action::movescopeupaction_instantiation(instance):
    assert isinstance(instance, ccsl::action::MoveScopeUpAction)

@given(instance=ccsl::action::DeleteAction_strategy)
@settings(max_examples=50)
def test_ccsl::action::deleteaction_instantiation(instance):
    assert isinstance(instance, ccsl::action::DeleteAction)

@given(instance=ccsl::faultTypeDescription::InjectionStrategy_strategy)
@settings(max_examples=50)
def test_ccsl::faulttypedescription::injectionstrategy_instantiation(instance):
    assert isinstance(instance, ccsl::faultTypeDescription::InjectionStrategy)

@given(instance=ccsl::import::ImportableElement_strategy)
@settings(max_examples=50)
def test_ccsl::import::importableelement_instantiation(instance):
    assert isinstance(instance, ccsl::import::ImportableElement)

@given(instance=Invocation_strategy)
@settings(max_examples=50)
def test_invocation_instantiation(instance):
    assert isinstance(instance, Invocation)

@given(instance=ccsl::invocation::SimpleMethodInvocation_strategy)
@settings(max_examples=50)
def test_ccsl::invocation::simplemethodinvocation_instantiation(instance):
    assert isinstance(instance, ccsl::invocation::SimpleMethodInvocation)

@given(instance=ccsl::invocation::ConstructorInvocation_strategy)
@settings(max_examples=50)
def test_ccsl::invocation::constructorinvocation_instantiation(instance):
    assert isinstance(instance, ccsl::invocation::ConstructorInvocation)

@given(instance=SimpleMethodInvocation_strategy)
@settings(max_examples=50)
def test_simplemethodinvocation_instantiation(instance):
    assert isinstance(instance, SimpleMethodInvocation)

@given(instance=ccsl::invocation::SuperMethodInvocation_strategy)
@settings(max_examples=50)
def test_ccsl::invocation::supermethodinvocation_instantiation(instance):
    assert isinstance(instance, ccsl::invocation::SuperMethodInvocation)

@given(instance=ccsl::invocation::MethodInvocation_strategy)
@settings(max_examples=50)
def test_ccsl::invocation::methodinvocation_instantiation(instance):
    assert isinstance(instance, ccsl::invocation::MethodInvocation)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=ccsl::datatype::BooleanPrimitiveType_strategy)
@settings(max_examples=50)
def test_ccsl::datatype::booleanprimitivetype_instantiation(instance):
    assert isinstance(instance, ccsl::datatype::BooleanPrimitiveType)

@given(instance=ccsl::datatype::IntPrimitiveType_strategy)
@settings(max_examples=50)
def test_ccsl::datatype::intprimitivetype_instantiation(instance):
    assert isinstance(instance, ccsl::datatype::IntPrimitiveType)

@given(instance=ccsl::datatype::ShortPrimitiveType_strategy)
@settings(max_examples=50)
def test_ccsl::datatype::shortprimitivetype_instantiation(instance):
    assert isinstance(instance, ccsl::datatype::ShortPrimitiveType)

@given(instance=ccsl::datatype::VoidType_strategy)
@settings(max_examples=50)
def test_ccsl::datatype::voidtype_instantiation(instance):
    assert isinstance(instance, ccsl::datatype::VoidType)

@given(instance=ccsl::datatype::StringPrimitiveType_strategy)
@settings(max_examples=50)
def test_ccsl::datatype::stringprimitivetype_instantiation(instance):
    assert isinstance(instance, ccsl::datatype::StringPrimitiveType)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=ccsl::datatype::ObjectType_strategy)
@settings(max_examples=50)
def test_ccsl::datatype::objecttype_instantiation(instance):
    assert isinstance(instance, ccsl::datatype::ObjectType)

@given(instance=ccsl::datatype::PrimitiveType_strategy)
@settings(max_examples=50)
def test_ccsl::datatype::primitivetype_instantiation(instance):
    assert isinstance(instance, ccsl::datatype::PrimitiveType)

@given(instance=ccsl::datatype::DataType_strategy)
@settings(max_examples=50)
def test_ccsl::datatype::datatype_instantiation(instance):
    assert isinstance(instance, ccsl::datatype::DataType)

@given(instance=annotation::Annotation_strategy)
@settings(max_examples=50)
def test_annotation::annotation_instantiation(instance):
    assert isinstance(instance, annotation::Annotation)

@given(instance=ccsl::annotation::AnnotableElement_strategy)
@settings(max_examples=50)
def test_ccsl::annotation::annotableelement_instantiation(instance):
    assert isinstance(instance, ccsl::annotation::AnnotableElement)

@given(instance=ccsl::annotation::AnnotableElement_strategy)
def test_ccsl::annotation::annotableelement_annotationsKind_type(instance):
    assert isinstance(instance.annotationsKind, str)


@given(instance=ccsl::annotation::AnnotableElement_strategy)
def test_ccsl::annotation::annotableelement_annotationsKind_setter(instance):
    original = instance.annotationsKind
    instance.annotationsKind = original
    assert instance.annotationsKind == original

@given(instance=complexType::AnnotationType_strategy)
@settings(max_examples=50)
def test_complextype::annotationtype_instantiation(instance):
    assert isinstance(instance, complexType::AnnotationType)

@given(instance=statements::Block_strategy)
@settings(max_examples=50)
def test_statements::block_instantiation(instance):
    assert isinstance(instance, statements::Block)

@given(instance=tryCatch::CatchClause_strategy)
@settings(max_examples=50)
def test_trycatch::catchclause_instantiation(instance):
    assert isinstance(instance, tryCatch::CatchClause)

@given(instance=UnaryAssignment_strategy)
@settings(max_examples=50)
def test_unaryassignment_instantiation(instance):
    assert isinstance(instance, UnaryAssignment)

@given(instance=ccsl::assignment::PostfixUnaryAssignment_strategy)
@settings(max_examples=50)
def test_ccsl::assignment::postfixunaryassignment_instantiation(instance):
    assert isinstance(instance, ccsl::assignment::PostfixUnaryAssignment)

@given(instance=ccsl::assignment::PrefixUnaryAssignment_strategy)
@settings(max_examples=50)
def test_ccsl::assignment::prefixunaryassignment_instantiation(instance):
    assert isinstance(instance, ccsl::assignment::PrefixUnaryAssignment)

@given(instance=AbstractAssignment_strategy)
@settings(max_examples=50)
def test_abstractassignment_instantiation(instance):
    assert isinstance(instance, AbstractAssignment)

@given(instance=ccsl::assignment::UnaryAssignment_strategy)
@settings(max_examples=50)
def test_ccsl::assignment::unaryassignment_instantiation(instance):
    assert isinstance(instance, ccsl::assignment::UnaryAssignment)

@given(instance=ccsl::assignment::UnaryAssignment_strategy)
def test_ccsl::assignment::unaryassignment_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=ccsl::assignment::UnaryAssignment_strategy)
def test_ccsl::assignment::unaryassignment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ccsl::assignment::Assignment_strategy)
@settings(max_examples=50)
def test_ccsl::assignment::assignment_instantiation(instance):
    assert isinstance(instance, ccsl::assignment::Assignment)

@given(instance=ccsl::assignment::Assignment_strategy)
def test_ccsl::assignment::assignment_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=ccsl::assignment::Assignment_strategy)
def test_ccsl::assignment::assignment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=OperatorExpression_strategy)
@settings(max_examples=50)
def test_operatorexpression_instantiation(instance):
    assert isinstance(instance, OperatorExpression)

@given(instance=ccsl::expressions::ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_ccsl::expressions::arithmeticexpression_instantiation(instance):
    assert isinstance(instance, ccsl::expressions::ArithmeticExpression)

@given(instance=ccsl::expressions::ArithmeticExpression_strategy)
def test_ccsl::expressions::arithmeticexpression_arithmeticOperator_type(instance):
    assert isinstance(instance.arithmeticOperator, str)


@given(instance=ccsl::expressions::ArithmeticExpression_strategy)
def test_ccsl::expressions::arithmeticexpression_arithmeticOperator_setter(instance):
    original = instance.arithmeticOperator
    instance.arithmeticOperator = original
    assert instance.arithmeticOperator == original

@given(instance=ccsl::expressions::BooleanExpression_strategy)
@settings(max_examples=50)
def test_ccsl::expressions::booleanexpression_instantiation(instance):
    assert isinstance(instance, ccsl::expressions::BooleanExpression)

@given(instance=ccsl::expressions::BooleanExpression_strategy)
def test_ccsl::expressions::booleanexpression_booleanOperator_type(instance):
    assert isinstance(instance.booleanOperator, str)


@given(instance=ccsl::expressions::BooleanExpression_strategy)
def test_ccsl::expressions::booleanexpression_booleanOperator_setter(instance):
    original = instance.booleanOperator
    instance.booleanOperator = original
    assert instance.booleanOperator == original

@given(instance=ccsl::expressions::InfixExpression_strategy)
@settings(max_examples=50)
def test_ccsl::expressions::infixexpression_instantiation(instance):
    assert isinstance(instance, ccsl::expressions::InfixExpression)

@given(instance=ccsl::expressions::StringConcatenation_strategy)
@settings(max_examples=50)
def test_ccsl::expressions::stringconcatenation_instantiation(instance):
    assert isinstance(instance, ccsl::expressions::StringConcatenation)

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=ccsl::controlFlow::SwitchCaseBlock_strategy)
@settings(max_examples=50)
def test_ccsl::controlflow::switchcaseblock_instantiation(instance):
    assert isinstance(instance, ccsl::controlFlow::SwitchCaseBlock)

@given(instance=ccsl::controlFlow::SwitchCaseBlock_strategy)
def test_ccsl::controlflow::switchcaseblock_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=ccsl::controlFlow::SwitchCaseBlock_strategy)
def test_ccsl::controlflow::switchcaseblock_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=controlFlow::SwitchCaseBlock_strategy)
@settings(max_examples=50)
def test_controlflow::switchcaseblock_instantiation(instance):
    assert isinstance(instance, controlFlow::SwitchCaseBlock)

@given(instance=ControlFlow_strategy)
@settings(max_examples=50)
def test_controlflow_instantiation(instance):
    assert isinstance(instance, ControlFlow)

@given(instance=ccsl::controlFlow::IfStatement_strategy)
@settings(max_examples=50)
def test_ccsl::controlflow::ifstatement_instantiation(instance):
    assert isinstance(instance, ccsl::controlFlow::IfStatement)

@given(instance=ccsl::controlFlow::LoopStatement_strategy)
@settings(max_examples=50)
def test_ccsl::controlflow::loopstatement_instantiation(instance):
    assert isinstance(instance, ccsl::controlFlow::LoopStatement)

@given(instance=ccsl::controlFlow::SwitchStatement_strategy)
@settings(max_examples=50)
def test_ccsl::controlflow::switchstatement_instantiation(instance):
    assert isinstance(instance, ccsl::controlFlow::SwitchStatement)

@given(instance=LiteralValue_strategy)
@settings(max_examples=50)
def test_literalvalue_instantiation(instance):
    assert isinstance(instance, LiteralValue)

@given(instance=ccsl::literalValues::StringLiteral_strategy)
@settings(max_examples=50)
def test_ccsl::literalvalues::stringliteral_instantiation(instance):
    assert isinstance(instance, ccsl::literalValues::StringLiteral)

@given(instance=ccsl::literalValues::CharacterLiteral_strategy)
@settings(max_examples=50)
def test_ccsl::literalvalues::characterliteral_instantiation(instance):
    assert isinstance(instance, ccsl::literalValues::CharacterLiteral)

@given(instance=ccsl::literalValues::NumberLiteral_strategy)
@settings(max_examples=50)
def test_ccsl::literalvalues::numberliteral_instantiation(instance):
    assert isinstance(instance, ccsl::literalValues::NumberLiteral)

@given(instance=ccsl::literalValues::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_ccsl::literalvalues::booleanliteral_instantiation(instance):
    assert isinstance(instance, ccsl::literalValues::BooleanLiteral)

@given(instance=ccsl::literalValues::NullLiteral_strategy)
@settings(max_examples=50)
def test_ccsl::literalvalues::nullliteral_instantiation(instance):
    assert isinstance(instance, ccsl::literalValues::NullLiteral)

@given(instance=ccsl::statements::ThrowStatement_strategy)
@settings(max_examples=50)
def test_ccsl::statements::throwstatement_instantiation(instance):
    assert isinstance(instance, ccsl::statements::ThrowStatement)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=ccsl::statements::ReturnStatement_strategy)
@settings(max_examples=50)
def test_ccsl::statements::returnstatement_instantiation(instance):
    assert isinstance(instance, ccsl::statements::ReturnStatement)

@given(instance=ccsl::statements::InstanceOf_strategy)
@settings(max_examples=50)
def test_ccsl::statements::instanceof_instantiation(instance):
    assert isinstance(instance, ccsl::statements::InstanceOf)

@given(instance=ccsl::tryCatch::CatchClause_strategy)
@settings(max_examples=50)
def test_ccsl::trycatch::catchclause_instantiation(instance):
    assert isinstance(instance, ccsl::tryCatch::CatchClause)

@given(instance=ccsl::literalValues::LiteralValue_strategy)
@settings(max_examples=50)
def test_ccsl::literalvalues::literalvalue_instantiation(instance):
    assert isinstance(instance, ccsl::literalValues::LiteralValue)

@given(instance=ccsl::literalValues::LiteralValue_strategy)
def test_ccsl::literalvalues::literalvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ccsl::literalValues::LiteralValue_strategy)
def test_ccsl::literalvalues::literalvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ccsl::annotation::Annotation_strategy)
@settings(max_examples=50)
def test_ccsl::annotation::annotation_instantiation(instance):
    assert isinstance(instance, ccsl::annotation::Annotation)

@given(instance=ccsl::import::ImportStatement_strategy)
@settings(max_examples=50)
def test_ccsl::import::importstatement_instantiation(instance):
    assert isinstance(instance, ccsl::import::ImportStatement)

@given(instance=ccsl::statements::ArrayCreation_strategy)
@settings(max_examples=50)
def test_ccsl::statements::arraycreation_instantiation(instance):
    assert isinstance(instance, ccsl::statements::ArrayCreation)

@given(instance=ccsl::statements::BreakStatement_strategy)
@settings(max_examples=50)
def test_ccsl::statements::breakstatement_instantiation(instance):
    assert isinstance(instance, ccsl::statements::BreakStatement)

@given(instance=ccsl::statements::ThisStatement_strategy)
@settings(max_examples=50)
def test_ccsl::statements::thisstatement_instantiation(instance):
    assert isinstance(instance, ccsl::statements::ThisStatement)

@given(instance=ccsl::statements::ContinueStatement_strategy)
@settings(max_examples=50)
def test_ccsl::statements::continuestatement_instantiation(instance):
    assert isinstance(instance, ccsl::statements::ContinueStatement)

@given(instance=ccsl::assignment::AbstractAssignment_strategy)
@settings(max_examples=50)
def test_ccsl::assignment::abstractassignment_instantiation(instance):
    assert isinstance(instance, ccsl::assignment::AbstractAssignment)

@given(instance=ccsl::tryCatch::TryStatement_strategy)
@settings(max_examples=50)
def test_ccsl::trycatch::trystatement_instantiation(instance):
    assert isinstance(instance, ccsl::tryCatch::TryStatement)

@given(instance=ccsl::expressions::ParenthesizedExpression_strategy)
@settings(max_examples=50)
def test_ccsl::expressions::parenthesizedexpression_instantiation(instance):
    assert isinstance(instance, ccsl::expressions::ParenthesizedExpression)

@given(instance=ccsl::statements::SynchronizedBlock_strategy)
@settings(max_examples=50)
def test_ccsl::statements::synchronizedblock_instantiation(instance):
    assert isinstance(instance, ccsl::statements::SynchronizedBlock)

@given(instance=ccsl::statements::Access_strategy)
@settings(max_examples=50)
def test_ccsl::statements::access_instantiation(instance):
    assert isinstance(instance, ccsl::statements::Access)

@given(instance=ccsl::invocation::Invocation_strategy)
@settings(max_examples=50)
def test_ccsl::invocation::invocation_instantiation(instance):
    assert isinstance(instance, ccsl::invocation::Invocation)

@given(instance=ccsl::invocation::Invocation_strategy)
def test_ccsl::invocation::invocation_argsKind_type(instance):
    assert isinstance(instance.argsKind, str)


@given(instance=ccsl::invocation::Invocation_strategy)
def test_ccsl::invocation::invocation_argsKind_setter(instance):
    original = instance.argsKind
    instance.argsKind = original
    assert instance.argsKind == original

@given(instance=ccsl::expressions::OperatorExpression_strategy)
@settings(max_examples=50)
def test_ccsl::expressions::operatorexpression_instantiation(instance):
    assert isinstance(instance, ccsl::expressions::OperatorExpression)

@given(instance=ccsl::statements::EmptyStatement_strategy)
@settings(max_examples=50)
def test_ccsl::statements::emptystatement_instantiation(instance):
    assert isinstance(instance, ccsl::statements::EmptyStatement)

@given(instance=ccsl::statements::NamedElementAccess_strategy)
@settings(max_examples=50)
def test_ccsl::statements::namedelementaccess_instantiation(instance):
    assert isinstance(instance, ccsl::statements::NamedElementAccess)

@given(instance=ccsl::statements::Statement_strategy)
@settings(max_examples=50)
def test_ccsl::statements::statement_instantiation(instance):
    assert isinstance(instance, ccsl::statements::Statement)

@given(instance=method::SimpleMethod_strategy)
@settings(max_examples=50)
def test_method::simplemethod_instantiation(instance):
    assert isinstance(instance, method::SimpleMethod)

@given(instance=ccsl::method::Method_strategy)
@settings(max_examples=50)
def test_ccsl::method::method_instantiation(instance):
    assert isinstance(instance, ccsl::method::Method)

@given(instance=ccsl::method::Method_strategy)
def test_ccsl::method::method_inheritance_type(instance):
    assert isinstance(instance.inheritance, str)


@given(instance=ccsl::method::Method_strategy)
def test_ccsl::method::method_inheritance_setter(instance):
    original = instance.inheritance
    instance.inheritance = original
    assert instance.inheritance == original

@given(instance=ccsl::method::Method_strategy)
def test_ccsl::method::method_final_type(instance):
    assert isinstance(instance.final, str)


@given(instance=ccsl::method::Method_strategy)
def test_ccsl::method::method_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original

@given(instance=ccsl::method::Method_strategy)
def test_ccsl::method::method_abstract_type(instance):
    assert isinstance(instance.abstract, str)


@given(instance=ccsl::method::Method_strategy)
def test_ccsl::method::method_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=ccsl::method::Method_strategy)
def test_ccsl::method::method_static_type(instance):
    assert isinstance(instance.static, str)


@given(instance=ccsl::method::Method_strategy)
def test_ccsl::method::method_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=variable::ParameterVariable_strategy)
@settings(max_examples=50)
def test_variable::parametervariable_instantiation(instance):
    assert isinstance(instance, variable::ParameterVariable)

@given(instance=elements::Element_strategy)
@settings(max_examples=50)
def test_elements::element_instantiation(instance):
    assert isinstance(instance, elements::Element)

@given(instance=ccsl::method::SimpleMethod_strategy)
@settings(max_examples=50)
def test_ccsl::method::simplemethod_instantiation(instance):
    assert isinstance(instance, ccsl::method::SimpleMethod)

@given(instance=ccsl::method::SimpleMethod_strategy)
def test_ccsl::method::simplemethod_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=ccsl::method::SimpleMethod_strategy)
def test_ccsl::method::simplemethod_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=ccsl::method::SimpleMethod_strategy)
def test_ccsl::method::simplemethod_paramsKind_type(instance):
    assert isinstance(instance.paramsKind, str)


@given(instance=ccsl::method::SimpleMethod_strategy)
def test_ccsl::method::simplemethod_paramsKind_setter(instance):
    original = instance.paramsKind
    instance.paramsKind = original
    assert instance.paramsKind == original

@given(instance=SimpleMethod_strategy)
@settings(max_examples=50)
def test_simplemethod_instantiation(instance):
    assert isinstance(instance, SimpleMethod)

@given(instance=ccsl::method::Constructor_strategy)
@settings(max_examples=50)
def test_ccsl::method::constructor_instantiation(instance):
    assert isinstance(instance, ccsl::method::Constructor)

@given(instance=ccsl::method::Constructor_strategy)
def test_ccsl::method::constructor_avaliableInSourceCode_type(instance):
    assert isinstance(instance.avaliableInSourceCode, str)


@given(instance=ccsl::method::Constructor_strategy)
def test_ccsl::method::constructor_avaliableInSourceCode_setter(instance):
    original = instance.avaliableInSourceCode
    instance.avaliableInSourceCode = original
    assert instance.avaliableInSourceCode == original

@given(instance=ccsl::statements::InstanceCreation_strategy)
@settings(max_examples=50)
def test_ccsl::statements::instancecreation_instantiation(instance):
    assert isinstance(instance, ccsl::statements::InstanceCreation)

@given(instance=ccsl::statements::InstanceCreation_strategy)
def test_ccsl::statements::instancecreation_argsKind_type(instance):
    assert isinstance(instance.argsKind, str)


@given(instance=ccsl::statements::InstanceCreation_strategy)
def test_ccsl::statements::instancecreation_argsKind_setter(instance):
    original = instance.argsKind
    instance.argsKind = original
    assert instance.argsKind == original

@given(instance=ccsl::statements::VarDeclaration_strategy)
@settings(max_examples=50)
def test_ccsl::statements::vardeclaration_instantiation(instance):
    assert isinstance(instance, ccsl::statements::VarDeclaration)

@given(instance=ccsl::statements::Block_strategy)
@settings(max_examples=50)
def test_ccsl::statements::block_instantiation(instance):
    assert isinstance(instance, ccsl::statements::Block)

@given(instance=ccsl::statements::Block_strategy)
def test_ccsl::statements::block_statementsKind_type(instance):
    assert isinstance(instance.statementsKind, str)


@given(instance=ccsl::statements::Block_strategy)
def test_ccsl::statements::block_statementsKind_setter(instance):
    original = instance.statementsKind
    instance.statementsKind = original
    assert instance.statementsKind == original

@given(instance=ccsl::statements::ControlFlow_strategy)
@settings(max_examples=50)
def test_ccsl::statements::controlflow_instantiation(instance):
    assert isinstance(instance, ccsl::statements::ControlFlow)

@given(instance=Access_strategy)
@settings(max_examples=50)
def test_access_instantiation(instance):
    assert isinstance(instance, Access)

@given(instance=ccsl::statements::DataTypeAccess_strategy)
@settings(max_examples=50)
def test_ccsl::statements::datatypeaccess_instantiation(instance):
    assert isinstance(instance, ccsl::statements::DataTypeAccess)

@given(instance=ccsl::statements::VariableAccess_strategy)
@settings(max_examples=50)
def test_ccsl::statements::variableaccess_instantiation(instance):
    assert isinstance(instance, ccsl::statements::VariableAccess)

@given(instance=complexType::JClass_strategy)
@settings(max_examples=50)
def test_complextype::jclass_instantiation(instance):
    assert isinstance(instance, complexType::JClass)

@given(instance=method::Constructor_strategy)
@settings(max_examples=50)
def test_method::constructor_instantiation(instance):
    assert isinstance(instance, method::Constructor)

@given(instance=datatype::ObjectType_strategy)
@settings(max_examples=50)
def test_datatype::objecttype_instantiation(instance):
    assert isinstance(instance, datatype::ObjectType)

@given(instance=ccsl::complexType::DeclaredType_strategy)
@settings(max_examples=50)
def test_ccsl::complextype::declaredtype_instantiation(instance):
    assert isinstance(instance, ccsl::complexType::DeclaredType)

@given(instance=ccsl::complexType::DeclaredType_strategy)
def test_ccsl::complextype::declaredtype_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=ccsl::complexType::DeclaredType_strategy)
def test_ccsl::complextype::declaredtype_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=ccsl::complexType::DeclaredType_strategy)
def test_ccsl::complextype::declaredtype_static_type(instance):
    assert isinstance(instance.static, str)


@given(instance=ccsl::complexType::DeclaredType_strategy)
def test_ccsl::complextype::declaredtype_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=ComplexType_strategy)
@settings(max_examples=50)
def test_complextype_instantiation(instance):
    assert isinstance(instance, ComplexType)

@given(instance=ccsl::datatype::GenericType_strategy)
@settings(max_examples=50)
def test_ccsl::datatype::generictype_instantiation(instance):
    assert isinstance(instance, ccsl::datatype::GenericType)

@given(instance=ccsl::complexType::AnonymousClass_strategy)
@settings(max_examples=50)
def test_ccsl::complextype::anonymousclass_instantiation(instance):
    assert isinstance(instance, ccsl::complexType::AnonymousClass)

@given(instance=complexType::ComplexType_strategy)
@settings(max_examples=50)
def test_complextype::complextype_instantiation(instance):
    assert isinstance(instance, complexType::ComplexType)

@given(instance=ccsl::complexType::JClass_strategy)
@settings(max_examples=50)
def test_ccsl::complextype::jclass_instantiation(instance):
    assert isinstance(instance, ccsl::complexType::JClass)

@given(instance=ccsl::complexType::JClass_strategy)
def test_ccsl::complextype::jclass_inheritance_type(instance):
    assert isinstance(instance.inheritance, str)


@given(instance=ccsl::complexType::JClass_strategy)
def test_ccsl::complextype::jclass_inheritance_setter(instance):
    original = instance.inheritance
    instance.inheritance = original
    assert instance.inheritance == original

@given(instance=ccsl::complexType::JInterface_strategy)
@settings(max_examples=50)
def test_ccsl::complextype::jinterface_instantiation(instance):
    assert isinstance(instance, ccsl::complexType::JInterface)

@given(instance=variable::InitializableVariable_strategy)
@settings(max_examples=50)
def test_variable::initializablevariable_instantiation(instance):
    assert isinstance(instance, variable::InitializableVariable)

@given(instance=ccsl::variable::FieldVariable_strategy)
@settings(max_examples=50)
def test_ccsl::variable::fieldvariable_instantiation(instance):
    assert isinstance(instance, ccsl::variable::FieldVariable)

@given(instance=ccsl::variable::FieldVariable_strategy)
def test_ccsl::variable::fieldvariable_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=ccsl::variable::FieldVariable_strategy)
def test_ccsl::variable::fieldvariable_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=ccsl::variable::FieldVariable_strategy)
def test_ccsl::variable::fieldvariable_static_type(instance):
    assert isinstance(instance.static, str)


@given(instance=ccsl::variable::FieldVariable_strategy)
def test_ccsl::variable::fieldvariable_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=statements::Statement_strategy)
@settings(max_examples=50)
def test_statements::statement_instantiation(instance):
    assert isinstance(instance, statements::Statement)

@given(instance=DeclaredType_strategy)
@settings(max_examples=50)
def test_declaredtype_instantiation(instance):
    assert isinstance(instance, DeclaredType)

@given(instance=ccsl::complexType::AnnotationType_strategy)
@settings(max_examples=50)
def test_ccsl::complextype::annotationtype_instantiation(instance):
    assert isinstance(instance, ccsl::complexType::AnnotationType)
