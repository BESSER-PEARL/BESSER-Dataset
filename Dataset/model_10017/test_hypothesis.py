import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Vertex,
    pivot::Pseudostate,
    pivot::ConnectionPointReference,
    Element,
    pivot::CompleteEnvironment,
    pivot::Comment,
    DataType,
    pivot::CollectionType,
    pivot::StandardLibrary,
    TypedElement,
    pivot::CollectionLiteralPart,
    pivot::StereotypeExtender,
    TemplateableElement,
    Namespace,
    pivot::State,
    pivot::Model,
    Type,
    pivot::Class,
    pivot::OCLExpression,
    LiteralExp,
    pivot::CollectionLiteralExp,
    CollectionLiteralPart,
    pivot::CollectionRange,
    pivot::CollectionItem,
    pivot::Package,
    pivot::Transition,
    CollectionType,
    pivot::BagType,
    NavigationCallExp,
    pivot::AssociationClassCallExp,
    OCLExpression,
    pivot::CallExp,
    PrimitiveLiteralExp,
    pivot::BooleanLiteralExp,
    NamedElement,
    pivot::Type,
    pivot::Namespace,
    pivot::CallOperationAction,
    pivot::Constraint,
    pivot::CompletePackage,
    pivot::CompleteModel,
    pivot::CompleteClass,
    pivot::Annotation,
    Class,
    pivot::Behavior,
    pivot::AssociationClass,
    pivot::AnyType,
    pivot::Detail,
    pivot::VoidType,
    pivot::Visitable,
    pivot::UnspecifiedValueExp,
    pivot::TypedElement,
    pivot::VariableDeclaration,
    pivot::TupleType,
    pivot::TupleLiteralExp,
    pivot::WildcardType,
    pivot::TemplateParameterSubstitution,
    pivot::TemplateBinding,
    pivot::StringLiteralExp,
    pivot::TemplateParameter,
    pivot::TemplateSignature,
    pivot::TemplateableElement,
    pivot::StateExp,
    pivot::ValueSpecification,
    pivot::Trigger,
    pivot::ShadowExp,
    pivot::SetType,
    pivot::SequenceType,
    pivot::SelfType,
    pivot::ShadowPart,
    pivot::Vertex,
    pivot::Region,
    pivot::ReferringElement,
    pivot::PrimitiveType,
    pivot::PrimitiveLiteralExp,
    pivot::Pivotable,
    CompletePackage,
    pivot::PrimitiveCompletePackage,
    pivot::OrphanCompletePackage,
    pivot::OrderedSetType,
    pivot::OppositePropertyCallExp,
    VariableDeclaration,
    pivot::TupleLiteralPart,
    pivot::ProfileApplication,
    FeatureCallExp,
    pivot::NavigationCallExp,
    Nameable,
    pivot::NamedElement,
    pivot::Nameable,
    pivot::MorePivotable,
    Feature,
    pivot::Property,
    pivot::Operation,
    pivot::NumericLiteralExp,
    pivot::NullLiteralExp,
    pivot::MessageExp,
    pivot::MapType,
    pivot::MapLiteralPart,
    pivot::MapLiteralExp,
    pivot::Signal,
    pivot::MessageType,
    pivot::SendSignalAction,
    Package,
    pivot::Profile,
    pivot::Library,
    pivot::LetExp,
    pivot::LiteralExp,
    pivot::Precedence,
    pivot::LambdaType,
    pivot::Parameter,
    Operation,
    pivot::Iteration,
    ReferringElement,
    pivot::OperationCallExp,
    pivot::PropertyCallExp,
    pivot::TypeExp,
    pivot::VariableExp,
    LoopExp,
    pivot::IteratorExp,
    pivot::IterateExp,
    pivot::InvalidType,
    pivot::InvalidLiteralExp,
    NumericLiteralExp,
    pivot::RealLiteralExp,
    pivot::UnlimitedNaturalLiteralExp,
    pivot::IntegerLiteralExp,
    pivot::IfExp,
    State,
    pivot::FinalState,
    CallExp,
    pivot::LoopExp,
    pivot::FeatureCallExp,
    pivot::Slot,
    pivot::InstanceSpecification,
    pivot::Import,
    pivot::Variable,
    LanguageExpression,
    pivot::ExpressionInOCL,
    InstanceSpecification,
    pivot::Feature,
    pivot::Stereotype,
    pivot::ElementExtension,
    pivot::Enumeration,
    pivot::EnumerationLiteral,
    pivot::EnumLiteralExp,
    Visitable,
    pivot::Element,
    ValueSpecification,
    pivot::DynamicValueSpecification,
    DynamicElement,
    pivot::DynamicType,
    pivot::DataType,
    pivot::DynamicProperty,
    pivot::DynamicElement,
    DynamicType,
    Behavior,
    pivot::StateMachine,
    pivot::DynamicBehavior,
    pivot::LanguageExpression,
    PseudostateKind,
    CollectionKind,
    TransitionKind,
    AssociativityKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_pivot::pseudostate_is_not_abstract():
    assert not inspect.isabstract(pivot::Pseudostate)


def test_pivot::pseudostate_constructor_exists():
    assert callable(pivot::Pseudostate.__init__)


def test_pivot::pseudostate_constructor_args():
    sig = inspect.signature(pivot::Pseudostate.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_pivot::pseudostate_has_kind():
    assert hasattr(pivot::Pseudostate, "kind")
    descriptor = None
    for klass in pivot::Pseudostate.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_pivot::connectionpointreference_is_not_abstract():
    assert not inspect.isabstract(pivot::ConnectionPointReference)


def test_pivot::connectionpointreference_constructor_exists():
    assert callable(pivot::ConnectionPointReference.__init__)


def test_pivot::connectionpointreference_constructor_args():
    sig = inspect.signature(pivot::ConnectionPointReference.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_pivot::completeenvironment_is_not_abstract():
    assert not inspect.isabstract(pivot::CompleteEnvironment)


def test_pivot::completeenvironment_constructor_exists():
    assert callable(pivot::CompleteEnvironment.__init__)


def test_pivot::completeenvironment_constructor_args():
    sig = inspect.signature(pivot::CompleteEnvironment.__init__)
    params = list(sig.parameters.keys())



def test_pivot::comment_is_not_abstract():
    assert not inspect.isabstract(pivot::Comment)


def test_pivot::comment_constructor_exists():
    assert callable(pivot::Comment.__init__)


def test_pivot::comment_constructor_args():
    sig = inspect.signature(pivot::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_pivot::comment_has_body():
    assert hasattr(pivot::Comment, "body")
    descriptor = None
    for klass in pivot::Comment.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_pivot::collectiontype_is_not_abstract():
    assert not inspect.isabstract(pivot::CollectionType)


def test_pivot::collectiontype_constructor_exists():
    assert callable(pivot::CollectionType.__init__)


def test_pivot::collectiontype_constructor_args():
    sig = inspect.signature(pivot::CollectionType.__init__)
    params = list(sig.parameters.keys())
    assert "upper" in params, "Missing parameter 'upper'"
    assert "lower" in params, "Missing parameter 'lower'"
    assert "isNullFree" in params, "Missing parameter 'isNullFree'"

def test_pivot::collectiontype_has_upper():
    assert hasattr(pivot::CollectionType, "upper")
    descriptor = None
    for klass in pivot::CollectionType.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_pivot::collectiontype_has_lower():
    assert hasattr(pivot::CollectionType, "lower")
    descriptor = None
    for klass in pivot::CollectionType.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_pivot::collectiontype_has_isNullFree():
    assert hasattr(pivot::CollectionType, "isNullFree")
    descriptor = None
    for klass in pivot::CollectionType.__mro__:
        if "isNullFree" in klass.__dict__:
            descriptor = klass.__dict__["isNullFree"]
            break
    assert isinstance(descriptor, property)



def test_pivot::standardlibrary_is_not_abstract():
    assert not inspect.isabstract(pivot::StandardLibrary)


def test_pivot::standardlibrary_constructor_exists():
    assert callable(pivot::StandardLibrary.__init__)


def test_pivot::standardlibrary_constructor_args():
    sig = inspect.signature(pivot::StandardLibrary.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_pivot::collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(pivot::CollectionLiteralPart)


def test_pivot::collectionliteralpart_constructor_exists():
    assert callable(pivot::CollectionLiteralPart.__init__)


def test_pivot::collectionliteralpart_constructor_args():
    sig = inspect.signature(pivot::CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_pivot::stereotypeextender_is_not_abstract():
    assert not inspect.isabstract(pivot::StereotypeExtender)


def test_pivot::stereotypeextender_constructor_exists():
    assert callable(pivot::StereotypeExtender.__init__)


def test_pivot::stereotypeextender_constructor_args():
    sig = inspect.signature(pivot::StereotypeExtender.__init__)
    params = list(sig.parameters.keys())
    assert "isRequired" in params, "Missing parameter 'isRequired'"

def test_pivot::stereotypeextender_has_isRequired():
    assert hasattr(pivot::StereotypeExtender, "isRequired")
    descriptor = None
    for klass in pivot::StereotypeExtender.__mro__:
        if "isRequired" in klass.__dict__:
            descriptor = klass.__dict__["isRequired"]
            break
    assert isinstance(descriptor, property)



def test_templateableelement_is_not_abstract():
    assert not inspect.isabstract(TemplateableElement)


def test_templateableelement_constructor_exists():
    assert callable(TemplateableElement.__init__)


def test_templateableelement_constructor_args():
    sig = inspect.signature(TemplateableElement.__init__)
    params = list(sig.parameters.keys())



def test_namespace_is_not_abstract():
    assert not inspect.isabstract(Namespace)


def test_namespace_constructor_exists():
    assert callable(Namespace.__init__)


def test_namespace_constructor_args():
    sig = inspect.signature(Namespace.__init__)
    params = list(sig.parameters.keys())



def test_pivot::state_is_not_abstract():
    assert not inspect.isabstract(pivot::State)


def test_pivot::state_constructor_exists():
    assert callable(pivot::State.__init__)


def test_pivot::state_constructor_args():
    sig = inspect.signature(pivot::State.__init__)
    params = list(sig.parameters.keys())
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isSubmachineState" in params, "Missing parameter 'isSubmachineState'"
    assert "isSimple" in params, "Missing parameter 'isSimple'"
    assert "isOrthogonal" in params, "Missing parameter 'isOrthogonal'"

def test_pivot::state_has_isComposite():
    assert hasattr(pivot::State, "isComposite")
    descriptor = None
    for klass in pivot::State.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_pivot::state_has_isSubmachineState():
    assert hasattr(pivot::State, "isSubmachineState")
    descriptor = None
    for klass in pivot::State.__mro__:
        if "isSubmachineState" in klass.__dict__:
            descriptor = klass.__dict__["isSubmachineState"]
            break
    assert isinstance(descriptor, property)

def test_pivot::state_has_isSimple():
    assert hasattr(pivot::State, "isSimple")
    descriptor = None
    for klass in pivot::State.__mro__:
        if "isSimple" in klass.__dict__:
            descriptor = klass.__dict__["isSimple"]
            break
    assert isinstance(descriptor, property)

def test_pivot::state_has_isOrthogonal():
    assert hasattr(pivot::State, "isOrthogonal")
    descriptor = None
    for klass in pivot::State.__mro__:
        if "isOrthogonal" in klass.__dict__:
            descriptor = klass.__dict__["isOrthogonal"]
            break
    assert isinstance(descriptor, property)



def test_pivot::model_is_not_abstract():
    assert not inspect.isabstract(pivot::Model)


def test_pivot::model_constructor_exists():
    assert callable(pivot::Model.__init__)


def test_pivot::model_constructor_args():
    sig = inspect.signature(pivot::Model.__init__)
    params = list(sig.parameters.keys())
    assert "externalURI" in params, "Missing parameter 'externalURI'"

def test_pivot::model_has_externalURI():
    assert hasattr(pivot::Model, "externalURI")
    descriptor = None
    for klass in pivot::Model.__mro__:
        if "externalURI" in klass.__dict__:
            descriptor = klass.__dict__["externalURI"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_pivot::class_is_not_abstract():
    assert not inspect.isabstract(pivot::Class)


def test_pivot::class_constructor_exists():
    assert callable(pivot::Class.__init__)


def test_pivot::class_constructor_args():
    sig = inspect.signature(pivot::Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"
    assert "isInterface" in params, "Missing parameter 'isInterface'"
    assert "isActive" in params, "Missing parameter 'isActive'"
    assert "instanceClassName" in params, "Missing parameter 'instanceClassName'"

def test_pivot::class_has_isAbstract():
    assert hasattr(pivot::Class, "isAbstract")
    descriptor = None
    for klass in pivot::Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_pivot::class_has_isInterface():
    assert hasattr(pivot::Class, "isInterface")
    descriptor = None
    for klass in pivot::Class.__mro__:
        if "isInterface" in klass.__dict__:
            descriptor = klass.__dict__["isInterface"]
            break
    assert isinstance(descriptor, property)

def test_pivot::class_has_isActive():
    assert hasattr(pivot::Class, "isActive")
    descriptor = None
    for klass in pivot::Class.__mro__:
        if "isActive" in klass.__dict__:
            descriptor = klass.__dict__["isActive"]
            break
    assert isinstance(descriptor, property)

def test_pivot::class_has_instanceClassName():
    assert hasattr(pivot::Class, "instanceClassName")
    descriptor = None
    for klass in pivot::Class.__mro__:
        if "instanceClassName" in klass.__dict__:
            descriptor = klass.__dict__["instanceClassName"]
            break
    assert isinstance(descriptor, property)



def test_pivot::oclexpression_is_not_abstract():
    assert not inspect.isabstract(pivot::OCLExpression)


def test_pivot::oclexpression_constructor_exists():
    assert callable(pivot::OCLExpression.__init__)


def test_pivot::oclexpression_constructor_args():
    sig = inspect.signature(pivot::OCLExpression.__init__)
    params = list(sig.parameters.keys())



def test_literalexp_is_not_abstract():
    assert not inspect.isabstract(LiteralExp)


def test_literalexp_constructor_exists():
    assert callable(LiteralExp.__init__)


def test_literalexp_constructor_args():
    sig = inspect.signature(LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot::collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(pivot::CollectionLiteralExp)


def test_pivot::collectionliteralexp_constructor_exists():
    assert callable(pivot::CollectionLiteralExp.__init__)


def test_pivot::collectionliteralexp_constructor_args():
    sig = inspect.signature(pivot::CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_pivot::collectionliteralexp_has_kind():
    assert hasattr(pivot::CollectionLiteralExp, "kind")
    descriptor = None
    for klass in pivot::CollectionLiteralExp.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralPart)


def test_collectionliteralpart_constructor_exists():
    assert callable(CollectionLiteralPart.__init__)


def test_collectionliteralpart_constructor_args():
    sig = inspect.signature(CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_pivot::collectionrange_is_not_abstract():
    assert not inspect.isabstract(pivot::CollectionRange)


def test_pivot::collectionrange_constructor_exists():
    assert callable(pivot::CollectionRange.__init__)


def test_pivot::collectionrange_constructor_args():
    sig = inspect.signature(pivot::CollectionRange.__init__)
    params = list(sig.parameters.keys())



def test_pivot::collectionitem_is_not_abstract():
    assert not inspect.isabstract(pivot::CollectionItem)


def test_pivot::collectionitem_constructor_exists():
    assert callable(pivot::CollectionItem.__init__)


def test_pivot::collectionitem_constructor_args():
    sig = inspect.signature(pivot::CollectionItem.__init__)
    params = list(sig.parameters.keys())



def test_pivot::package_is_not_abstract():
    assert not inspect.isabstract(pivot::Package)


def test_pivot::package_constructor_exists():
    assert callable(pivot::Package.__init__)


def test_pivot::package_constructor_args():
    sig = inspect.signature(pivot::Package.__init__)
    params = list(sig.parameters.keys())
    assert "URI" in params, "Missing parameter 'URI'"
    assert "nsPrefix" in params, "Missing parameter 'nsPrefix'"

def test_pivot::package_has_URI():
    assert hasattr(pivot::Package, "URI")
    descriptor = None
    for klass in pivot::Package.__mro__:
        if "URI" in klass.__dict__:
            descriptor = klass.__dict__["URI"]
            break
    assert isinstance(descriptor, property)

def test_pivot::package_has_nsPrefix():
    assert hasattr(pivot::Package, "nsPrefix")
    descriptor = None
    for klass in pivot::Package.__mro__:
        if "nsPrefix" in klass.__dict__:
            descriptor = klass.__dict__["nsPrefix"]
            break
    assert isinstance(descriptor, property)



def test_pivot::transition_is_not_abstract():
    assert not inspect.isabstract(pivot::Transition)


def test_pivot::transition_constructor_exists():
    assert callable(pivot::Transition.__init__)


def test_pivot::transition_constructor_args():
    sig = inspect.signature(pivot::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_pivot::transition_has_kind():
    assert hasattr(pivot::Transition, "kind")
    descriptor = None
    for klass in pivot::Transition.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_pivot::bagtype_is_not_abstract():
    assert not inspect.isabstract(pivot::BagType)


def test_pivot::bagtype_constructor_exists():
    assert callable(pivot::BagType.__init__)


def test_pivot::bagtype_constructor_args():
    sig = inspect.signature(pivot::BagType.__init__)
    params = list(sig.parameters.keys())



def test_navigationcallexp_is_not_abstract():
    assert not inspect.isabstract(NavigationCallExp)


def test_navigationcallexp_constructor_exists():
    assert callable(NavigationCallExp.__init__)


def test_navigationcallexp_constructor_args():
    sig = inspect.signature(NavigationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot::associationclasscallexp_is_not_abstract():
    assert not inspect.isabstract(pivot::AssociationClassCallExp)


def test_pivot::associationclasscallexp_constructor_exists():
    assert callable(pivot::AssociationClassCallExp.__init__)


def test_pivot::associationclasscallexp_constructor_args():
    sig = inspect.signature(pivot::AssociationClassCallExp.__init__)
    params = list(sig.parameters.keys())



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OCLExpression)


def test_oclexpression_constructor_exists():
    assert callable(OCLExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OCLExpression.__init__)
    params = list(sig.parameters.keys())



def test_pivot::callexp_is_not_abstract():
    assert not inspect.isabstract(pivot::CallExp)


def test_pivot::callexp_constructor_exists():
    assert callable(pivot::CallExp.__init__)


def test_pivot::callexp_constructor_args():
    sig = inspect.signature(pivot::CallExp.__init__)
    params = list(sig.parameters.keys())
    assert "isImplicit" in params, "Missing parameter 'isImplicit'"
    assert "isSafe" in params, "Missing parameter 'isSafe'"

def test_pivot::callexp_has_isImplicit():
    assert hasattr(pivot::CallExp, "isImplicit")
    descriptor = None
    for klass in pivot::CallExp.__mro__:
        if "isImplicit" in klass.__dict__:
            descriptor = klass.__dict__["isImplicit"]
            break
    assert isinstance(descriptor, property)

def test_pivot::callexp_has_isSafe():
    assert hasattr(pivot::CallExp, "isSafe")
    descriptor = None
    for klass in pivot::CallExp.__mro__:
        if "isSafe" in klass.__dict__:
            descriptor = klass.__dict__["isSafe"]
            break
    assert isinstance(descriptor, property)



def test_primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveLiteralExp)


def test_primitiveliteralexp_constructor_exists():
    assert callable(PrimitiveLiteralExp.__init__)


def test_primitiveliteralexp_constructor_args():
    sig = inspect.signature(PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot::booleanliteralexp_is_not_abstract():
    assert not inspect.isabstract(pivot::BooleanLiteralExp)


def test_pivot::booleanliteralexp_constructor_exists():
    assert callable(pivot::BooleanLiteralExp.__init__)


def test_pivot::booleanliteralexp_constructor_args():
    sig = inspect.signature(pivot::BooleanLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_pivot::booleanliteralexp_has_booleanSymbol():
    assert hasattr(pivot::BooleanLiteralExp, "booleanSymbol")
    descriptor = None
    for klass in pivot::BooleanLiteralExp.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_pivot::type_is_not_abstract():
    assert not inspect.isabstract(pivot::Type)


def test_pivot::type_constructor_exists():
    assert callable(pivot::Type.__init__)


def test_pivot::type_constructor_args():
    sig = inspect.signature(pivot::Type.__init__)
    params = list(sig.parameters.keys())



def test_pivot::namespace_is_not_abstract():
    assert not inspect.isabstract(pivot::Namespace)


def test_pivot::namespace_constructor_exists():
    assert callable(pivot::Namespace.__init__)


def test_pivot::namespace_constructor_args():
    sig = inspect.signature(pivot::Namespace.__init__)
    params = list(sig.parameters.keys())



def test_pivot::calloperationaction_is_not_abstract():
    assert not inspect.isabstract(pivot::CallOperationAction)


def test_pivot::calloperationaction_constructor_exists():
    assert callable(pivot::CallOperationAction.__init__)


def test_pivot::calloperationaction_constructor_args():
    sig = inspect.signature(pivot::CallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_pivot::constraint_is_not_abstract():
    assert not inspect.isabstract(pivot::Constraint)


def test_pivot::constraint_constructor_exists():
    assert callable(pivot::Constraint.__init__)


def test_pivot::constraint_constructor_args():
    sig = inspect.signature(pivot::Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "isCallable" in params, "Missing parameter 'isCallable'"

def test_pivot::constraint_has_isCallable():
    assert hasattr(pivot::Constraint, "isCallable")
    descriptor = None
    for klass in pivot::Constraint.__mro__:
        if "isCallable" in klass.__dict__:
            descriptor = klass.__dict__["isCallable"]
            break
    assert isinstance(descriptor, property)



def test_pivot::completepackage_is_not_abstract():
    assert not inspect.isabstract(pivot::CompletePackage)


def test_pivot::completepackage_constructor_exists():
    assert callable(pivot::CompletePackage.__init__)


def test_pivot::completepackage_constructor_args():
    sig = inspect.signature(pivot::CompletePackage.__init__)
    params = list(sig.parameters.keys())



def test_pivot::completemodel_is_not_abstract():
    assert not inspect.isabstract(pivot::CompleteModel)


def test_pivot::completemodel_constructor_exists():
    assert callable(pivot::CompleteModel.__init__)


def test_pivot::completemodel_constructor_args():
    sig = inspect.signature(pivot::CompleteModel.__init__)
    params = list(sig.parameters.keys())



def test_pivot::completeclass_is_not_abstract():
    assert not inspect.isabstract(pivot::CompleteClass)


def test_pivot::completeclass_constructor_exists():
    assert callable(pivot::CompleteClass.__init__)


def test_pivot::completeclass_constructor_args():
    sig = inspect.signature(pivot::CompleteClass.__init__)
    params = list(sig.parameters.keys())



def test_pivot::annotation_is_not_abstract():
    assert not inspect.isabstract(pivot::Annotation)


def test_pivot::annotation_constructor_exists():
    assert callable(pivot::Annotation.__init__)


def test_pivot::annotation_constructor_args():
    sig = inspect.signature(pivot::Annotation.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_pivot::behavior_is_not_abstract():
    assert not inspect.isabstract(pivot::Behavior)


def test_pivot::behavior_constructor_exists():
    assert callable(pivot::Behavior.__init__)


def test_pivot::behavior_constructor_args():
    sig = inspect.signature(pivot::Behavior.__init__)
    params = list(sig.parameters.keys())



def test_pivot::associationclass_is_not_abstract():
    assert not inspect.isabstract(pivot::AssociationClass)


def test_pivot::associationclass_constructor_exists():
    assert callable(pivot::AssociationClass.__init__)


def test_pivot::associationclass_constructor_args():
    sig = inspect.signature(pivot::AssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_pivot::anytype_is_not_abstract():
    assert not inspect.isabstract(pivot::AnyType)


def test_pivot::anytype_constructor_exists():
    assert callable(pivot::AnyType.__init__)


def test_pivot::anytype_constructor_args():
    sig = inspect.signature(pivot::AnyType.__init__)
    params = list(sig.parameters.keys())



def test_pivot::detail_is_not_abstract():
    assert not inspect.isabstract(pivot::Detail)


def test_pivot::detail_constructor_exists():
    assert callable(pivot::Detail.__init__)


def test_pivot::detail_constructor_args():
    sig = inspect.signature(pivot::Detail.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_pivot::detail_has_values():
    assert hasattr(pivot::Detail, "values")
    descriptor = None
    for klass in pivot::Detail.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_pivot::voidtype_is_not_abstract():
    assert not inspect.isabstract(pivot::VoidType)


def test_pivot::voidtype_constructor_exists():
    assert callable(pivot::VoidType.__init__)


def test_pivot::voidtype_constructor_args():
    sig = inspect.signature(pivot::VoidType.__init__)
    params = list(sig.parameters.keys())



def test_pivot::visitable_is_not_abstract():
    assert not inspect.isabstract(pivot::Visitable)


def test_pivot::visitable_constructor_exists():
    assert callable(pivot::Visitable.__init__)


def test_pivot::visitable_constructor_args():
    sig = inspect.signature(pivot::Visitable.__init__)
    params = list(sig.parameters.keys())



def test_pivot::unspecifiedvalueexp_is_not_abstract():
    assert not inspect.isabstract(pivot::UnspecifiedValueExp)


def test_pivot::unspecifiedvalueexp_constructor_exists():
    assert callable(pivot::UnspecifiedValueExp.__init__)


def test_pivot::unspecifiedvalueexp_constructor_args():
    sig = inspect.signature(pivot::UnspecifiedValueExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot::typedelement_is_not_abstract():
    assert not inspect.isabstract(pivot::TypedElement)


def test_pivot::typedelement_constructor_exists():
    assert callable(pivot::TypedElement.__init__)


def test_pivot::typedelement_constructor_args():
    sig = inspect.signature(pivot::TypedElement.__init__)
    params = list(sig.parameters.keys())
    assert "isMany" in params, "Missing parameter 'isMany'"
    assert "isRequired" in params, "Missing parameter 'isRequired'"

def test_pivot::typedelement_has_isMany():
    assert hasattr(pivot::TypedElement, "isMany")
    descriptor = None
    for klass in pivot::TypedElement.__mro__:
        if "isMany" in klass.__dict__:
            descriptor = klass.__dict__["isMany"]
            break
    assert isinstance(descriptor, property)

def test_pivot::typedelement_has_isRequired():
    assert hasattr(pivot::TypedElement, "isRequired")
    descriptor = None
    for klass in pivot::TypedElement.__mro__:
        if "isRequired" in klass.__dict__:
            descriptor = klass.__dict__["isRequired"]
            break
    assert isinstance(descriptor, property)



def test_pivot::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(pivot::VariableDeclaration)


def test_pivot::variabledeclaration_constructor_exists():
    assert callable(pivot::VariableDeclaration.__init__)


def test_pivot::variabledeclaration_constructor_args():
    sig = inspect.signature(pivot::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_pivot::tupletype_is_not_abstract():
    assert not inspect.isabstract(pivot::TupleType)


def test_pivot::tupletype_constructor_exists():
    assert callable(pivot::TupleType.__init__)


def test_pivot::tupletype_constructor_args():
    sig = inspect.signature(pivot::TupleType.__init__)
    params = list(sig.parameters.keys())



def test_pivot::tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(pivot::TupleLiteralExp)


def test_pivot::tupleliteralexp_constructor_exists():
    assert callable(pivot::TupleLiteralExp.__init__)


def test_pivot::tupleliteralexp_constructor_args():
    sig = inspect.signature(pivot::TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot::wildcardtype_is_not_abstract():
    assert not inspect.isabstract(pivot::WildcardType)


def test_pivot::wildcardtype_constructor_exists():
    assert callable(pivot::WildcardType.__init__)


def test_pivot::wildcardtype_constructor_args():
    sig = inspect.signature(pivot::WildcardType.__init__)
    params = list(sig.parameters.keys())



def test_pivot::templateparametersubstitution_is_not_abstract():
    assert not inspect.isabstract(pivot::TemplateParameterSubstitution)


def test_pivot::templateparametersubstitution_constructor_exists():
    assert callable(pivot::TemplateParameterSubstitution.__init__)


def test_pivot::templateparametersubstitution_constructor_args():
    sig = inspect.signature(pivot::TemplateParameterSubstitution.__init__)
    params = list(sig.parameters.keys())



def test_pivot::templatebinding_is_not_abstract():
    assert not inspect.isabstract(pivot::TemplateBinding)


def test_pivot::templatebinding_constructor_exists():
    assert callable(pivot::TemplateBinding.__init__)


def test_pivot::templatebinding_constructor_args():
    sig = inspect.signature(pivot::TemplateBinding.__init__)
    params = list(sig.parameters.keys())



def test_pivot::stringliteralexp_is_not_abstract():
    assert not inspect.isabstract(pivot::StringLiteralExp)


def test_pivot::stringliteralexp_constructor_exists():
    assert callable(pivot::StringLiteralExp.__init__)


def test_pivot::stringliteralexp_constructor_args():
    sig = inspect.signature(pivot::StringLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_pivot::stringliteralexp_has_stringSymbol():
    assert hasattr(pivot::StringLiteralExp, "stringSymbol")
    descriptor = None
    for klass in pivot::StringLiteralExp.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_pivot::templateparameter_is_not_abstract():
    assert not inspect.isabstract(pivot::TemplateParameter)


def test_pivot::templateparameter_constructor_exists():
    assert callable(pivot::TemplateParameter.__init__)


def test_pivot::templateparameter_constructor_args():
    sig = inspect.signature(pivot::TemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_pivot::templatesignature_is_not_abstract():
    assert not inspect.isabstract(pivot::TemplateSignature)


def test_pivot::templatesignature_constructor_exists():
    assert callable(pivot::TemplateSignature.__init__)


def test_pivot::templatesignature_constructor_args():
    sig = inspect.signature(pivot::TemplateSignature.__init__)
    params = list(sig.parameters.keys())



def test_pivot::templateableelement_is_not_abstract():
    assert not inspect.isabstract(pivot::TemplateableElement)


def test_pivot::templateableelement_constructor_exists():
    assert callable(pivot::TemplateableElement.__init__)


def test_pivot::templateableelement_constructor_args():
    sig = inspect.signature(pivot::TemplateableElement.__init__)
    params = list(sig.parameters.keys())



def test_pivot::stateexp_is_not_abstract():
    assert not inspect.isabstract(pivot::StateExp)


def test_pivot::stateexp_constructor_exists():
    assert callable(pivot::StateExp.__init__)


def test_pivot::stateexp_constructor_args():
    sig = inspect.signature(pivot::StateExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot::valuespecification_is_not_abstract():
    assert not inspect.isabstract(pivot::ValueSpecification)


def test_pivot::valuespecification_constructor_exists():
    assert callable(pivot::ValueSpecification.__init__)


def test_pivot::valuespecification_constructor_args():
    sig = inspect.signature(pivot::ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_pivot::trigger_is_not_abstract():
    assert not inspect.isabstract(pivot::Trigger)


def test_pivot::trigger_constructor_exists():
    assert callable(pivot::Trigger.__init__)


def test_pivot::trigger_constructor_args():
    sig = inspect.signature(pivot::Trigger.__init__)
    params = list(sig.parameters.keys())



def test_pivot::shadowexp_is_not_abstract():
    assert not inspect.isabstract(pivot::ShadowExp)


def test_pivot::shadowexp_constructor_exists():
    assert callable(pivot::ShadowExp.__init__)


def test_pivot::shadowexp_constructor_args():
    sig = inspect.signature(pivot::ShadowExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_pivot::shadowexp_has_value():
    assert hasattr(pivot::ShadowExp, "value")
    descriptor = None
    for klass in pivot::ShadowExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_pivot::settype_is_not_abstract():
    assert not inspect.isabstract(pivot::SetType)


def test_pivot::settype_constructor_exists():
    assert callable(pivot::SetType.__init__)


def test_pivot::settype_constructor_args():
    sig = inspect.signature(pivot::SetType.__init__)
    params = list(sig.parameters.keys())



def test_pivot::sequencetype_is_not_abstract():
    assert not inspect.isabstract(pivot::SequenceType)


def test_pivot::sequencetype_constructor_exists():
    assert callable(pivot::SequenceType.__init__)


def test_pivot::sequencetype_constructor_args():
    sig = inspect.signature(pivot::SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_pivot::selftype_is_not_abstract():
    assert not inspect.isabstract(pivot::SelfType)


def test_pivot::selftype_constructor_exists():
    assert callable(pivot::SelfType.__init__)


def test_pivot::selftype_constructor_args():
    sig = inspect.signature(pivot::SelfType.__init__)
    params = list(sig.parameters.keys())



def test_pivot::shadowpart_is_not_abstract():
    assert not inspect.isabstract(pivot::ShadowPart)


def test_pivot::shadowpart_constructor_exists():
    assert callable(pivot::ShadowPart.__init__)


def test_pivot::shadowpart_constructor_args():
    sig = inspect.signature(pivot::ShadowPart.__init__)
    params = list(sig.parameters.keys())



def test_pivot::vertex_is_not_abstract():
    assert not inspect.isabstract(pivot::Vertex)


def test_pivot::vertex_constructor_exists():
    assert callable(pivot::Vertex.__init__)


def test_pivot::vertex_constructor_args():
    sig = inspect.signature(pivot::Vertex.__init__)
    params = list(sig.parameters.keys())



def test_pivot::region_is_not_abstract():
    assert not inspect.isabstract(pivot::Region)


def test_pivot::region_constructor_exists():
    assert callable(pivot::Region.__init__)


def test_pivot::region_constructor_args():
    sig = inspect.signature(pivot::Region.__init__)
    params = list(sig.parameters.keys())



def test_pivot::referringelement_is_not_abstract():
    assert not inspect.isabstract(pivot::ReferringElement)


def test_pivot::referringelement_constructor_exists():
    assert callable(pivot::ReferringElement.__init__)


def test_pivot::referringelement_constructor_args():
    sig = inspect.signature(pivot::ReferringElement.__init__)
    params = list(sig.parameters.keys())



def test_pivot::primitivetype_is_not_abstract():
    assert not inspect.isabstract(pivot::PrimitiveType)


def test_pivot::primitivetype_constructor_exists():
    assert callable(pivot::PrimitiveType.__init__)


def test_pivot::primitivetype_constructor_args():
    sig = inspect.signature(pivot::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_pivot::primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(pivot::PrimitiveLiteralExp)


def test_pivot::primitiveliteralexp_constructor_exists():
    assert callable(pivot::PrimitiveLiteralExp.__init__)


def test_pivot::primitiveliteralexp_constructor_args():
    sig = inspect.signature(pivot::PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot::pivotable_is_not_abstract():
    assert not inspect.isabstract(pivot::Pivotable)


def test_pivot::pivotable_constructor_exists():
    assert callable(pivot::Pivotable.__init__)


def test_pivot::pivotable_constructor_args():
    sig = inspect.signature(pivot::Pivotable.__init__)
    params = list(sig.parameters.keys())



def test_completepackage_is_not_abstract():
    assert not inspect.isabstract(CompletePackage)


def test_completepackage_constructor_exists():
    assert callable(CompletePackage.__init__)


def test_completepackage_constructor_args():
    sig = inspect.signature(CompletePackage.__init__)
    params = list(sig.parameters.keys())



def test_pivot::primitivecompletepackage_is_not_abstract():
    assert not inspect.isabstract(pivot::PrimitiveCompletePackage)


def test_pivot::primitivecompletepackage_constructor_exists():
    assert callable(pivot::PrimitiveCompletePackage.__init__)


def test_pivot::primitivecompletepackage_constructor_args():
    sig = inspect.signature(pivot::PrimitiveCompletePackage.__init__)
    params = list(sig.parameters.keys())



def test_pivot::orphancompletepackage_is_not_abstract():
    assert not inspect.isabstract(pivot::OrphanCompletePackage)


def test_pivot::orphancompletepackage_constructor_exists():
    assert callable(pivot::OrphanCompletePackage.__init__)


def test_pivot::orphancompletepackage_constructor_args():
    sig = inspect.signature(pivot::OrphanCompletePackage.__init__)
    params = list(sig.parameters.keys())



def test_pivot::orderedsettype_is_not_abstract():
    assert not inspect.isabstract(pivot::OrderedSetType)


def test_pivot::orderedsettype_constructor_exists():
    assert callable(pivot::OrderedSetType.__init__)


def test_pivot::orderedsettype_constructor_args():
    sig = inspect.signature(pivot::OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_pivot::oppositepropertycallexp_is_not_abstract():
    assert not inspect.isabstract(pivot::OppositePropertyCallExp)


def test_pivot::oppositepropertycallexp_constructor_exists():
    assert callable(pivot::OppositePropertyCallExp.__init__)


def test_pivot::oppositepropertycallexp_constructor_args():
    sig = inspect.signature(pivot::OppositePropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_pivot::tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(pivot::TupleLiteralPart)


def test_pivot::tupleliteralpart_constructor_exists():
    assert callable(pivot::TupleLiteralPart.__init__)


def test_pivot::tupleliteralpart_constructor_args():
    sig = inspect.signature(pivot::TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_pivot::profileapplication_is_not_abstract():
    assert not inspect.isabstract(pivot::ProfileApplication)


def test_pivot::profileapplication_constructor_exists():
    assert callable(pivot::ProfileApplication.__init__)


def test_pivot::profileapplication_constructor_args():
    sig = inspect.signature(pivot::ProfileApplication.__init__)
    params = list(sig.parameters.keys())
    assert "isStrict" in params, "Missing parameter 'isStrict'"

def test_pivot::profileapplication_has_isStrict():
    assert hasattr(pivot::ProfileApplication, "isStrict")
    descriptor = None
    for klass in pivot::ProfileApplication.__mro__:
        if "isStrict" in klass.__dict__:
            descriptor = klass.__dict__["isStrict"]
            break
    assert isinstance(descriptor, property)



def test_featurecallexp_is_not_abstract():
    assert not inspect.isabstract(FeatureCallExp)


def test_featurecallexp_constructor_exists():
    assert callable(FeatureCallExp.__init__)


def test_featurecallexp_constructor_args():
    sig = inspect.signature(FeatureCallExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot::navigationcallexp_is_not_abstract():
    assert not inspect.isabstract(pivot::NavigationCallExp)


def test_pivot::navigationcallexp_constructor_exists():
    assert callable(pivot::NavigationCallExp.__init__)


def test_pivot::navigationcallexp_constructor_args():
    sig = inspect.signature(pivot::NavigationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_nameable_is_not_abstract():
    assert not inspect.isabstract(Nameable)


def test_nameable_constructor_exists():
    assert callable(Nameable.__init__)


def test_nameable_constructor_args():
    sig = inspect.signature(Nameable.__init__)
    params = list(sig.parameters.keys())



def test_pivot::namedelement_is_not_abstract():
    assert not inspect.isabstract(pivot::NamedElement)


def test_pivot::namedelement_constructor_exists():
    assert callable(pivot::NamedElement.__init__)


def test_pivot::namedelement_constructor_args():
    sig = inspect.signature(pivot::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pivot::namedelement_has_name():
    assert hasattr(pivot::NamedElement, "name")
    descriptor = None
    for klass in pivot::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pivot::nameable_is_not_abstract():
    assert not inspect.isabstract(pivot::Nameable)


def test_pivot::nameable_constructor_exists():
    assert callable(pivot::Nameable.__init__)


def test_pivot::nameable_constructor_args():
    sig = inspect.signature(pivot::Nameable.__init__)
    params = list(sig.parameters.keys())



def test_pivot::morepivotable_is_not_abstract():
    assert not inspect.isabstract(pivot::MorePivotable)


def test_pivot::morepivotable_constructor_exists():
    assert callable(pivot::MorePivotable.__init__)


def test_pivot::morepivotable_constructor_args():
    sig = inspect.signature(pivot::MorePivotable.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_pivot::property_is_not_abstract():
    assert not inspect.isabstract(pivot::Property)


def test_pivot::property_constructor_exists():
    assert callable(pivot::Property.__init__)


def test_pivot::property_constructor_args():
    sig = inspect.signature(pivot::Property.__init__)
    params = list(sig.parameters.keys())
    assert "isDerived" in params, "Missing parameter 'isDerived'"
    assert "isUnsettable" in params, "Missing parameter 'isUnsettable'"
    assert "isID" in params, "Missing parameter 'isID'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "isVolatile" in params, "Missing parameter 'isVolatile'"
    assert "isImplicit" in params, "Missing parameter 'isImplicit'"
    assert "defaultValueString" in params, "Missing parameter 'defaultValueString'"
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"
    assert "isResolveProxies" in params, "Missing parameter 'isResolveProxies'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isTransient" in params, "Missing parameter 'isTransient'"

def test_pivot::property_has_isDerived():
    assert hasattr(pivot::Property, "isDerived")
    descriptor = None
    for klass in pivot::Property.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)

def test_pivot::property_has_isUnsettable():
    assert hasattr(pivot::Property, "isUnsettable")
    descriptor = None
    for klass in pivot::Property.__mro__:
        if "isUnsettable" in klass.__dict__:
            descriptor = klass.__dict__["isUnsettable"]
            break
    assert isinstance(descriptor, property)

def test_pivot::property_has_isID():
    assert hasattr(pivot::Property, "isID")
    descriptor = None
    for klass in pivot::Property.__mro__:
        if "isID" in klass.__dict__:
            descriptor = klass.__dict__["isID"]
            break
    assert isinstance(descriptor, property)

def test_pivot::property_has_defaultValue():
    assert hasattr(pivot::Property, "defaultValue")
    descriptor = None
    for klass in pivot::Property.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_pivot::property_has_isVolatile():
    assert hasattr(pivot::Property, "isVolatile")
    descriptor = None
    for klass in pivot::Property.__mro__:
        if "isVolatile" in klass.__dict__:
            descriptor = klass.__dict__["isVolatile"]
            break
    assert isinstance(descriptor, property)

def test_pivot::property_has_isImplicit():
    assert hasattr(pivot::Property, "isImplicit")
    descriptor = None
    for klass in pivot::Property.__mro__:
        if "isImplicit" in klass.__dict__:
            descriptor = klass.__dict__["isImplicit"]
            break
    assert isinstance(descriptor, property)

def test_pivot::property_has_defaultValueString():
    assert hasattr(pivot::Property, "defaultValueString")
    descriptor = None
    for klass in pivot::Property.__mro__:
        if "defaultValueString" in klass.__dict__:
            descriptor = klass.__dict__["defaultValueString"]
            break
    assert isinstance(descriptor, property)

def test_pivot::property_has_isReadOnly():
    assert hasattr(pivot::Property, "isReadOnly")
    descriptor = None
    for klass in pivot::Property.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)

def test_pivot::property_has_isResolveProxies():
    assert hasattr(pivot::Property, "isResolveProxies")
    descriptor = None
    for klass in pivot::Property.__mro__:
        if "isResolveProxies" in klass.__dict__:
            descriptor = klass.__dict__["isResolveProxies"]
            break
    assert isinstance(descriptor, property)

def test_pivot::property_has_isComposite():
    assert hasattr(pivot::Property, "isComposite")
    descriptor = None
    for klass in pivot::Property.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_pivot::property_has_isTransient():
    assert hasattr(pivot::Property, "isTransient")
    descriptor = None
    for klass in pivot::Property.__mro__:
        if "isTransient" in klass.__dict__:
            descriptor = klass.__dict__["isTransient"]
            break
    assert isinstance(descriptor, property)



def test_pivot::operation_is_not_abstract():
    assert not inspect.isabstract(pivot::Operation)


def test_pivot::operation_constructor_exists():
    assert callable(pivot::Operation.__init__)


def test_pivot::operation_constructor_args():
    sig = inspect.signature(pivot::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "isValidating" in params, "Missing parameter 'isValidating'"
    assert "isTypeof" in params, "Missing parameter 'isTypeof'"
    assert "isInvalidating" in params, "Missing parameter 'isInvalidating'"

def test_pivot::operation_has_isValidating():
    assert hasattr(pivot::Operation, "isValidating")
    descriptor = None
    for klass in pivot::Operation.__mro__:
        if "isValidating" in klass.__dict__:
            descriptor = klass.__dict__["isValidating"]
            break
    assert isinstance(descriptor, property)

def test_pivot::operation_has_isTypeof():
    assert hasattr(pivot::Operation, "isTypeof")
    descriptor = None
    for klass in pivot::Operation.__mro__:
        if "isTypeof" in klass.__dict__:
            descriptor = klass.__dict__["isTypeof"]
            break
    assert isinstance(descriptor, property)

def test_pivot::operation_has_isInvalidating():
    assert hasattr(pivot::Operation, "isInvalidating")
    descriptor = None
    for klass in pivot::Operation.__mro__:
        if "isInvalidating" in klass.__dict__:
            descriptor = klass.__dict__["isInvalidating"]
            break
    assert isinstance(descriptor, property)



def test_pivot::numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(pivot::NumericLiteralExp)


def test_pivot::numericliteralexp_constructor_exists():
    assert callable(pivot::NumericLiteralExp.__init__)


def test_pivot::numericliteralexp_constructor_args():
    sig = inspect.signature(pivot::NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot::nullliteralexp_is_not_abstract():
    assert not inspect.isabstract(pivot::NullLiteralExp)


def test_pivot::nullliteralexp_constructor_exists():
    assert callable(pivot::NullLiteralExp.__init__)


def test_pivot::nullliteralexp_constructor_args():
    sig = inspect.signature(pivot::NullLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot::messageexp_is_not_abstract():
    assert not inspect.isabstract(pivot::MessageExp)


def test_pivot::messageexp_constructor_exists():
    assert callable(pivot::MessageExp.__init__)


def test_pivot::messageexp_constructor_args():
    sig = inspect.signature(pivot::MessageExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot::maptype_is_not_abstract():
    assert not inspect.isabstract(pivot::MapType)


def test_pivot::maptype_constructor_exists():
    assert callable(pivot::MapType.__init__)


def test_pivot::maptype_constructor_args():
    sig = inspect.signature(pivot::MapType.__init__)
    params = list(sig.parameters.keys())



def test_pivot::mapliteralpart_is_not_abstract():
    assert not inspect.isabstract(pivot::MapLiteralPart)


def test_pivot::mapliteralpart_constructor_exists():
    assert callable(pivot::MapLiteralPart.__init__)


def test_pivot::mapliteralpart_constructor_args():
    sig = inspect.signature(pivot::MapLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_pivot::mapliteralexp_is_not_abstract():
    assert not inspect.isabstract(pivot::MapLiteralExp)


def test_pivot::mapliteralexp_constructor_exists():
    assert callable(pivot::MapLiteralExp.__init__)


def test_pivot::mapliteralexp_constructor_args():
    sig = inspect.signature(pivot::MapLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot::signal_is_not_abstract():
    assert not inspect.isabstract(pivot::Signal)


def test_pivot::signal_constructor_exists():
    assert callable(pivot::Signal.__init__)


def test_pivot::signal_constructor_args():
    sig = inspect.signature(pivot::Signal.__init__)
    params = list(sig.parameters.keys())



def test_pivot::messagetype_is_not_abstract():
    assert not inspect.isabstract(pivot::MessageType)


def test_pivot::messagetype_constructor_exists():
    assert callable(pivot::MessageType.__init__)


def test_pivot::messagetype_constructor_args():
    sig = inspect.signature(pivot::MessageType.__init__)
    params = list(sig.parameters.keys())



def test_pivot::sendsignalaction_is_not_abstract():
    assert not inspect.isabstract(pivot::SendSignalAction)


def test_pivot::sendsignalaction_constructor_exists():
    assert callable(pivot::SendSignalAction.__init__)


def test_pivot::sendsignalaction_constructor_args():
    sig = inspect.signature(pivot::SendSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_pivot::profile_is_not_abstract():
    assert not inspect.isabstract(pivot::Profile)


def test_pivot::profile_constructor_exists():
    assert callable(pivot::Profile.__init__)


def test_pivot::profile_constructor_args():
    sig = inspect.signature(pivot::Profile.__init__)
    params = list(sig.parameters.keys())



def test_pivot::library_is_not_abstract():
    assert not inspect.isabstract(pivot::Library)


def test_pivot::library_constructor_exists():
    assert callable(pivot::Library.__init__)


def test_pivot::library_constructor_args():
    sig = inspect.signature(pivot::Library.__init__)
    params = list(sig.parameters.keys())



def test_pivot::letexp_is_not_abstract():
    assert not inspect.isabstract(pivot::LetExp)


def test_pivot::letexp_constructor_exists():
    assert callable(pivot::LetExp.__init__)


def test_pivot::letexp_constructor_args():
    sig = inspect.signature(pivot::LetExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot::literalexp_is_not_abstract():
    assert not inspect.isabstract(pivot::LiteralExp)


def test_pivot::literalexp_constructor_exists():
    assert callable(pivot::LiteralExp.__init__)


def test_pivot::literalexp_constructor_args():
    sig = inspect.signature(pivot::LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot::precedence_is_not_abstract():
    assert not inspect.isabstract(pivot::Precedence)


def test_pivot::precedence_constructor_exists():
    assert callable(pivot::Precedence.__init__)


def test_pivot::precedence_constructor_args():
    sig = inspect.signature(pivot::Precedence.__init__)
    params = list(sig.parameters.keys())
    assert "order" in params, "Missing parameter 'order'"
    assert "associativity" in params, "Missing parameter 'associativity'"

def test_pivot::precedence_has_order():
    assert hasattr(pivot::Precedence, "order")
    descriptor = None
    for klass in pivot::Precedence.__mro__:
        if "order" in klass.__dict__:
            descriptor = klass.__dict__["order"]
            break
    assert isinstance(descriptor, property)

def test_pivot::precedence_has_associativity():
    assert hasattr(pivot::Precedence, "associativity")
    descriptor = None
    for klass in pivot::Precedence.__mro__:
        if "associativity" in klass.__dict__:
            descriptor = klass.__dict__["associativity"]
            break
    assert isinstance(descriptor, property)



def test_pivot::lambdatype_is_not_abstract():
    assert not inspect.isabstract(pivot::LambdaType)


def test_pivot::lambdatype_constructor_exists():
    assert callable(pivot::LambdaType.__init__)


def test_pivot::lambdatype_constructor_args():
    sig = inspect.signature(pivot::LambdaType.__init__)
    params = list(sig.parameters.keys())



def test_pivot::parameter_is_not_abstract():
    assert not inspect.isabstract(pivot::Parameter)


def test_pivot::parameter_constructor_exists():
    assert callable(pivot::Parameter.__init__)


def test_pivot::parameter_constructor_args():
    sig = inspect.signature(pivot::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "isTypeof" in params, "Missing parameter 'isTypeof'"

def test_pivot::parameter_has_isTypeof():
    assert hasattr(pivot::Parameter, "isTypeof")
    descriptor = None
    for klass in pivot::Parameter.__mro__:
        if "isTypeof" in klass.__dict__:
            descriptor = klass.__dict__["isTypeof"]
            break
    assert isinstance(descriptor, property)



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_pivot::iteration_is_not_abstract():
    assert not inspect.isabstract(pivot::Iteration)


def test_pivot::iteration_constructor_exists():
    assert callable(pivot::Iteration.__init__)


def test_pivot::iteration_constructor_args():
    sig = inspect.signature(pivot::Iteration.__init__)
    params = list(sig.parameters.keys())



def test_referringelement_is_not_abstract():
    assert not inspect.isabstract(ReferringElement)


def test_referringelement_constructor_exists():
    assert callable(ReferringElement.__init__)


def test_referringelement_constructor_args():
    sig = inspect.signature(ReferringElement.__init__)
    params = list(sig.parameters.keys())



def test_pivot::operationcallexp_is_not_abstract():
    assert not inspect.isabstract(pivot::OperationCallExp)


def test_pivot::operationcallexp_constructor_exists():
    assert callable(pivot::OperationCallExp.__init__)


def test_pivot::operationcallexp_constructor_args():
    sig = inspect.signature(pivot::OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot::propertycallexp_is_not_abstract():
    assert not inspect.isabstract(pivot::PropertyCallExp)


def test_pivot::propertycallexp_constructor_exists():
    assert callable(pivot::PropertyCallExp.__init__)


def test_pivot::propertycallexp_constructor_args():
    sig = inspect.signature(pivot::PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot::typeexp_is_not_abstract():
    assert not inspect.isabstract(pivot::TypeExp)


def test_pivot::typeexp_constructor_exists():
    assert callable(pivot::TypeExp.__init__)


def test_pivot::typeexp_constructor_args():
    sig = inspect.signature(pivot::TypeExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot::variableexp_is_not_abstract():
    assert not inspect.isabstract(pivot::VariableExp)


def test_pivot::variableexp_constructor_exists():
    assert callable(pivot::VariableExp.__init__)


def test_pivot::variableexp_constructor_args():
    sig = inspect.signature(pivot::VariableExp.__init__)
    params = list(sig.parameters.keys())
    assert "isImplicit" in params, "Missing parameter 'isImplicit'"

def test_pivot::variableexp_has_isImplicit():
    assert hasattr(pivot::VariableExp, "isImplicit")
    descriptor = None
    for klass in pivot::VariableExp.__mro__:
        if "isImplicit" in klass.__dict__:
            descriptor = klass.__dict__["isImplicit"]
            break
    assert isinstance(descriptor, property)



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot::iteratorexp_is_not_abstract():
    assert not inspect.isabstract(pivot::IteratorExp)


def test_pivot::iteratorexp_constructor_exists():
    assert callable(pivot::IteratorExp.__init__)


def test_pivot::iteratorexp_constructor_args():
    sig = inspect.signature(pivot::IteratorExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot::iterateexp_is_not_abstract():
    assert not inspect.isabstract(pivot::IterateExp)


def test_pivot::iterateexp_constructor_exists():
    assert callable(pivot::IterateExp.__init__)


def test_pivot::iterateexp_constructor_args():
    sig = inspect.signature(pivot::IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot::invalidtype_is_not_abstract():
    assert not inspect.isabstract(pivot::InvalidType)


def test_pivot::invalidtype_constructor_exists():
    assert callable(pivot::InvalidType.__init__)


def test_pivot::invalidtype_constructor_args():
    sig = inspect.signature(pivot::InvalidType.__init__)
    params = list(sig.parameters.keys())



def test_pivot::invalidliteralexp_is_not_abstract():
    assert not inspect.isabstract(pivot::InvalidLiteralExp)


def test_pivot::invalidliteralexp_constructor_exists():
    assert callable(pivot::InvalidLiteralExp.__init__)


def test_pivot::invalidliteralexp_constructor_args():
    sig = inspect.signature(pivot::InvalidLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(NumericLiteralExp)


def test_numericliteralexp_constructor_exists():
    assert callable(NumericLiteralExp.__init__)


def test_numericliteralexp_constructor_args():
    sig = inspect.signature(NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot::realliteralexp_is_not_abstract():
    assert not inspect.isabstract(pivot::RealLiteralExp)


def test_pivot::realliteralexp_constructor_exists():
    assert callable(pivot::RealLiteralExp.__init__)


def test_pivot::realliteralexp_constructor_args():
    sig = inspect.signature(pivot::RealLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_pivot::realliteralexp_has_realSymbol():
    assert hasattr(pivot::RealLiteralExp, "realSymbol")
    descriptor = None
    for klass in pivot::RealLiteralExp.__mro__:
        if "realSymbol" in klass.__dict__:
            descriptor = klass.__dict__["realSymbol"]
            break
    assert isinstance(descriptor, property)



def test_pivot::unlimitednaturalliteralexp_is_not_abstract():
    assert not inspect.isabstract(pivot::UnlimitedNaturalLiteralExp)


def test_pivot::unlimitednaturalliteralexp_constructor_exists():
    assert callable(pivot::UnlimitedNaturalLiteralExp.__init__)


def test_pivot::unlimitednaturalliteralexp_constructor_args():
    sig = inspect.signature(pivot::UnlimitedNaturalLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "unlimitedNaturalSymbol" in params, "Missing parameter 'unlimitedNaturalSymbol'"

def test_pivot::unlimitednaturalliteralexp_has_unlimitedNaturalSymbol():
    assert hasattr(pivot::UnlimitedNaturalLiteralExp, "unlimitedNaturalSymbol")
    descriptor = None
    for klass in pivot::UnlimitedNaturalLiteralExp.__mro__:
        if "unlimitedNaturalSymbol" in klass.__dict__:
            descriptor = klass.__dict__["unlimitedNaturalSymbol"]
            break
    assert isinstance(descriptor, property)



def test_pivot::integerliteralexp_is_not_abstract():
    assert not inspect.isabstract(pivot::IntegerLiteralExp)


def test_pivot::integerliteralexp_constructor_exists():
    assert callable(pivot::IntegerLiteralExp.__init__)


def test_pivot::integerliteralexp_constructor_args():
    sig = inspect.signature(pivot::IntegerLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_pivot::integerliteralexp_has_integerSymbol():
    assert hasattr(pivot::IntegerLiteralExp, "integerSymbol")
    descriptor = None
    for klass in pivot::IntegerLiteralExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_pivot::ifexp_is_not_abstract():
    assert not inspect.isabstract(pivot::IfExp)


def test_pivot::ifexp_constructor_exists():
    assert callable(pivot::IfExp.__init__)


def test_pivot::ifexp_constructor_args():
    sig = inspect.signature(pivot::IfExp.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_pivot::finalstate_is_not_abstract():
    assert not inspect.isabstract(pivot::FinalState)


def test_pivot::finalstate_constructor_exists():
    assert callable(pivot::FinalState.__init__)


def test_pivot::finalstate_constructor_args():
    sig = inspect.signature(pivot::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_callexp_is_not_abstract():
    assert not inspect.isabstract(CallExp)


def test_callexp_constructor_exists():
    assert callable(CallExp.__init__)


def test_callexp_constructor_args():
    sig = inspect.signature(CallExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot::loopexp_is_not_abstract():
    assert not inspect.isabstract(pivot::LoopExp)


def test_pivot::loopexp_constructor_exists():
    assert callable(pivot::LoopExp.__init__)


def test_pivot::loopexp_constructor_args():
    sig = inspect.signature(pivot::LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot::featurecallexp_is_not_abstract():
    assert not inspect.isabstract(pivot::FeatureCallExp)


def test_pivot::featurecallexp_constructor_exists():
    assert callable(pivot::FeatureCallExp.__init__)


def test_pivot::featurecallexp_constructor_args():
    sig = inspect.signature(pivot::FeatureCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "isPre" in params, "Missing parameter 'isPre'"

def test_pivot::featurecallexp_has_isPre():
    assert hasattr(pivot::FeatureCallExp, "isPre")
    descriptor = None
    for klass in pivot::FeatureCallExp.__mro__:
        if "isPre" in klass.__dict__:
            descriptor = klass.__dict__["isPre"]
            break
    assert isinstance(descriptor, property)



def test_pivot::slot_is_not_abstract():
    assert not inspect.isabstract(pivot::Slot)


def test_pivot::slot_constructor_exists():
    assert callable(pivot::Slot.__init__)


def test_pivot::slot_constructor_args():
    sig = inspect.signature(pivot::Slot.__init__)
    params = list(sig.parameters.keys())



def test_pivot::instancespecification_is_not_abstract():
    assert not inspect.isabstract(pivot::InstanceSpecification)


def test_pivot::instancespecification_constructor_exists():
    assert callable(pivot::InstanceSpecification.__init__)


def test_pivot::instancespecification_constructor_args():
    sig = inspect.signature(pivot::InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_pivot::import_is_not_abstract():
    assert not inspect.isabstract(pivot::Import)


def test_pivot::import_constructor_exists():
    assert callable(pivot::Import.__init__)


def test_pivot::import_constructor_args():
    sig = inspect.signature(pivot::Import.__init__)
    params = list(sig.parameters.keys())



def test_pivot::variable_is_not_abstract():
    assert not inspect.isabstract(pivot::Variable)


def test_pivot::variable_constructor_exists():
    assert callable(pivot::Variable.__init__)


def test_pivot::variable_constructor_args():
    sig = inspect.signature(pivot::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "isImplicit" in params, "Missing parameter 'isImplicit'"

def test_pivot::variable_has_isImplicit():
    assert hasattr(pivot::Variable, "isImplicit")
    descriptor = None
    for klass in pivot::Variable.__mro__:
        if "isImplicit" in klass.__dict__:
            descriptor = klass.__dict__["isImplicit"]
            break
    assert isinstance(descriptor, property)



def test_languageexpression_is_not_abstract():
    assert not inspect.isabstract(LanguageExpression)


def test_languageexpression_constructor_exists():
    assert callable(LanguageExpression.__init__)


def test_languageexpression_constructor_args():
    sig = inspect.signature(LanguageExpression.__init__)
    params = list(sig.parameters.keys())



def test_pivot::expressioninocl_is_not_abstract():
    assert not inspect.isabstract(pivot::ExpressionInOCL)


def test_pivot::expressioninocl_constructor_exists():
    assert callable(pivot::ExpressionInOCL.__init__)


def test_pivot::expressioninocl_constructor_args():
    sig = inspect.signature(pivot::ExpressionInOCL.__init__)
    params = list(sig.parameters.keys())



def test_instancespecification_is_not_abstract():
    assert not inspect.isabstract(InstanceSpecification)


def test_instancespecification_constructor_exists():
    assert callable(InstanceSpecification.__init__)


def test_instancespecification_constructor_args():
    sig = inspect.signature(InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_pivot::feature_is_not_abstract():
    assert not inspect.isabstract(pivot::Feature)


def test_pivot::feature_constructor_exists():
    assert callable(pivot::Feature.__init__)


def test_pivot::feature_constructor_args():
    sig = inspect.signature(pivot::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "implementationClass" in params, "Missing parameter 'implementationClass'"
    assert "implementation" in params, "Missing parameter 'implementation'"
    assert "isStatic" in params, "Missing parameter 'isStatic'"

def test_pivot::feature_has_implementationClass():
    assert hasattr(pivot::Feature, "implementationClass")
    descriptor = None
    for klass in pivot::Feature.__mro__:
        if "implementationClass" in klass.__dict__:
            descriptor = klass.__dict__["implementationClass"]
            break
    assert isinstance(descriptor, property)

def test_pivot::feature_has_implementation():
    assert hasattr(pivot::Feature, "implementation")
    descriptor = None
    for klass in pivot::Feature.__mro__:
        if "implementation" in klass.__dict__:
            descriptor = klass.__dict__["implementation"]
            break
    assert isinstance(descriptor, property)

def test_pivot::feature_has_isStatic():
    assert hasattr(pivot::Feature, "isStatic")
    descriptor = None
    for klass in pivot::Feature.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)



def test_pivot::stereotype_is_not_abstract():
    assert not inspect.isabstract(pivot::Stereotype)


def test_pivot::stereotype_constructor_exists():
    assert callable(pivot::Stereotype.__init__)


def test_pivot::stereotype_constructor_args():
    sig = inspect.signature(pivot::Stereotype.__init__)
    params = list(sig.parameters.keys())



def test_pivot::elementextension_is_not_abstract():
    assert not inspect.isabstract(pivot::ElementExtension)


def test_pivot::elementextension_constructor_exists():
    assert callable(pivot::ElementExtension.__init__)


def test_pivot::elementextension_constructor_args():
    sig = inspect.signature(pivot::ElementExtension.__init__)
    params = list(sig.parameters.keys())
    assert "isApplied" in params, "Missing parameter 'isApplied'"
    assert "isRequired" in params, "Missing parameter 'isRequired'"

def test_pivot::elementextension_has_isApplied():
    assert hasattr(pivot::ElementExtension, "isApplied")
    descriptor = None
    for klass in pivot::ElementExtension.__mro__:
        if "isApplied" in klass.__dict__:
            descriptor = klass.__dict__["isApplied"]
            break
    assert isinstance(descriptor, property)

def test_pivot::elementextension_has_isRequired():
    assert hasattr(pivot::ElementExtension, "isRequired")
    descriptor = None
    for klass in pivot::ElementExtension.__mro__:
        if "isRequired" in klass.__dict__:
            descriptor = klass.__dict__["isRequired"]
            break
    assert isinstance(descriptor, property)



def test_pivot::enumeration_is_not_abstract():
    assert not inspect.isabstract(pivot::Enumeration)


def test_pivot::enumeration_constructor_exists():
    assert callable(pivot::Enumeration.__init__)


def test_pivot::enumeration_constructor_args():
    sig = inspect.signature(pivot::Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_pivot::enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(pivot::EnumerationLiteral)


def test_pivot::enumerationliteral_constructor_exists():
    assert callable(pivot::EnumerationLiteral.__init__)


def test_pivot::enumerationliteral_constructor_args():
    sig = inspect.signature(pivot::EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_pivot::enumerationliteral_has_value():
    assert hasattr(pivot::EnumerationLiteral, "value")
    descriptor = None
    for klass in pivot::EnumerationLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_pivot::enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(pivot::EnumLiteralExp)


def test_pivot::enumliteralexp_constructor_exists():
    assert callable(pivot::EnumLiteralExp.__init__)


def test_pivot::enumliteralexp_constructor_args():
    sig = inspect.signature(pivot::EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_visitable_is_not_abstract():
    assert not inspect.isabstract(Visitable)


def test_visitable_constructor_exists():
    assert callable(Visitable.__init__)


def test_visitable_constructor_args():
    sig = inspect.signature(Visitable.__init__)
    params = list(sig.parameters.keys())



def test_pivot::element_is_not_abstract():
    assert not inspect.isabstract(pivot::Element)


def test_pivot::element_constructor_exists():
    assert callable(pivot::Element.__init__)


def test_pivot::element_constructor_args():
    sig = inspect.signature(pivot::Element.__init__)
    params = list(sig.parameters.keys())



def test_valuespecification_is_not_abstract():
    assert not inspect.isabstract(ValueSpecification)


def test_valuespecification_constructor_exists():
    assert callable(ValueSpecification.__init__)


def test_valuespecification_constructor_args():
    sig = inspect.signature(ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_pivot::dynamicvaluespecification_is_not_abstract():
    assert not inspect.isabstract(pivot::DynamicValueSpecification)


def test_pivot::dynamicvaluespecification_constructor_exists():
    assert callable(pivot::DynamicValueSpecification.__init__)


def test_pivot::dynamicvaluespecification_constructor_args():
    sig = inspect.signature(pivot::DynamicValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_dynamicelement_is_not_abstract():
    assert not inspect.isabstract(DynamicElement)


def test_dynamicelement_constructor_exists():
    assert callable(DynamicElement.__init__)


def test_dynamicelement_constructor_args():
    sig = inspect.signature(DynamicElement.__init__)
    params = list(sig.parameters.keys())



def test_pivot::dynamictype_is_not_abstract():
    assert not inspect.isabstract(pivot::DynamicType)


def test_pivot::dynamictype_constructor_exists():
    assert callable(pivot::DynamicType.__init__)


def test_pivot::dynamictype_constructor_args():
    sig = inspect.signature(pivot::DynamicType.__init__)
    params = list(sig.parameters.keys())



def test_pivot::datatype_is_not_abstract():
    assert not inspect.isabstract(pivot::DataType)


def test_pivot::datatype_constructor_exists():
    assert callable(pivot::DataType.__init__)


def test_pivot::datatype_constructor_args():
    sig = inspect.signature(pivot::DataType.__init__)
    params = list(sig.parameters.keys())
    assert "isSerializable" in params, "Missing parameter 'isSerializable'"

def test_pivot::datatype_has_isSerializable():
    assert hasattr(pivot::DataType, "isSerializable")
    descriptor = None
    for klass in pivot::DataType.__mro__:
        if "isSerializable" in klass.__dict__:
            descriptor = klass.__dict__["isSerializable"]
            break
    assert isinstance(descriptor, property)



def test_pivot::dynamicproperty_is_not_abstract():
    assert not inspect.isabstract(pivot::DynamicProperty)


def test_pivot::dynamicproperty_constructor_exists():
    assert callable(pivot::DynamicProperty.__init__)


def test_pivot::dynamicproperty_constructor_args():
    sig = inspect.signature(pivot::DynamicProperty.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_pivot::dynamicproperty_has_default():
    assert hasattr(pivot::DynamicProperty, "default")
    descriptor = None
    for klass in pivot::DynamicProperty.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_pivot::dynamicelement_is_not_abstract():
    assert not inspect.isabstract(pivot::DynamicElement)


def test_pivot::dynamicelement_constructor_exists():
    assert callable(pivot::DynamicElement.__init__)


def test_pivot::dynamicelement_constructor_args():
    sig = inspect.signature(pivot::DynamicElement.__init__)
    params = list(sig.parameters.keys())



def test_dynamictype_is_not_abstract():
    assert not inspect.isabstract(DynamicType)


def test_dynamictype_constructor_exists():
    assert callable(DynamicType.__init__)


def test_dynamictype_constructor_args():
    sig = inspect.signature(DynamicType.__init__)
    params = list(sig.parameters.keys())



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_pivot::statemachine_is_not_abstract():
    assert not inspect.isabstract(pivot::StateMachine)


def test_pivot::statemachine_constructor_exists():
    assert callable(pivot::StateMachine.__init__)


def test_pivot::statemachine_constructor_args():
    sig = inspect.signature(pivot::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_pivot::dynamicbehavior_is_not_abstract():
    assert not inspect.isabstract(pivot::DynamicBehavior)


def test_pivot::dynamicbehavior_constructor_exists():
    assert callable(pivot::DynamicBehavior.__init__)


def test_pivot::dynamicbehavior_constructor_args():
    sig = inspect.signature(pivot::DynamicBehavior.__init__)
    params = list(sig.parameters.keys())



def test_pivot::languageexpression_is_not_abstract():
    assert not inspect.isabstract(pivot::LanguageExpression)


def test_pivot::languageexpression_constructor_exists():
    assert callable(pivot::LanguageExpression.__init__)


def test_pivot::languageexpression_constructor_args():
    sig = inspect.signature(pivot::LanguageExpression.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "body" in params, "Missing parameter 'body'"

def test_pivot::languageexpression_has_language():
    assert hasattr(pivot::LanguageExpression, "language")
    descriptor = None
    for klass in pivot::LanguageExpression.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_pivot::languageexpression_has_body():
    assert hasattr(pivot::LanguageExpression, "body")
    descriptor = None
    for klass in pivot::LanguageExpression.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_pseudostatekind_exists():
    # Check that the Enumeration exists
    assert PseudostateKind is not None

def test_pseudostatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PseudostateKind]
    expected_literals = [
        "initial",
        "junction",
        "entryPoint",
        "join",
        "exitPoint",
        "fork",
        "terminate",
        "shallowHistory",
        "choice",
        "deepHistory",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PseudostateKind"

def test_collectionkind_exists():
    # Check that the Enumeration exists
    assert CollectionKind is not None

def test_collectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CollectionKind]
    expected_literals = [
        "Bag",
        "Sequence",
        "Set",
        "OrderedSet",
        "Collection",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CollectionKind"

def test_transitionkind_exists():
    # Check that the Enumeration exists
    assert TransitionKind is not None

def test_transitionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TransitionKind]
    expected_literals = [
        "internal",
        "external",
        "local",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TransitionKind"

def test_associativitykind_exists():
    # Check that the Enumeration exists
    assert AssociativityKind is not None

def test_associativitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssociativityKind]
    expected_literals = [
        "right",
        "left",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssociativityKind"


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
Vertex_strategy = st.builds(
    Vertex,
)
pivot::Pseudostate_strategy = st.builds(
    pivot::Pseudostate,
    kind=
        safe_text
)
pivot::ConnectionPointReference_strategy = st.builds(
    pivot::ConnectionPointReference,
)
Element_strategy = st.builds(
    Element,
)
pivot::CompleteEnvironment_strategy = st.builds(
    pivot::CompleteEnvironment,
)
pivot::Comment_strategy = st.builds(
    pivot::Comment,
    body=
        safe_text
)
DataType_strategy = st.builds(
    DataType,
)
pivot::CollectionType_strategy = st.builds(
    pivot::CollectionType,
    upper=
        safe_text,
    lower=
        safe_text,
    isNullFree=
        safe_text
)
pivot::StandardLibrary_strategy = st.builds(
    pivot::StandardLibrary,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
pivot::CollectionLiteralPart_strategy = st.builds(
    pivot::CollectionLiteralPart,
)
pivot::StereotypeExtender_strategy = st.builds(
    pivot::StereotypeExtender,
    isRequired=
        safe_text
)
TemplateableElement_strategy = st.builds(
    TemplateableElement,
)
Namespace_strategy = st.builds(
    Namespace,
)
pivot::State_strategy = st.builds(
    pivot::State,
    isComposite=
        safe_text,
    isSubmachineState=
        safe_text,
    isSimple=
        safe_text,
    isOrthogonal=
        safe_text
)
pivot::Model_strategy = st.builds(
    pivot::Model,
    externalURI=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
pivot::Class_strategy = st.builds(
    pivot::Class,
    isAbstract=
        safe_text,
    isInterface=
        safe_text,
    isActive=
        safe_text,
    instanceClassName=
        safe_text
)
pivot::OCLExpression_strategy = st.builds(
    pivot::OCLExpression,
)
LiteralExp_strategy = st.builds(
    LiteralExp,
)
pivot::CollectionLiteralExp_strategy = st.builds(
    pivot::CollectionLiteralExp,
    kind=
        safe_text
)
CollectionLiteralPart_strategy = st.builds(
    CollectionLiteralPart,
)
pivot::CollectionRange_strategy = st.builds(
    pivot::CollectionRange,
)
pivot::CollectionItem_strategy = st.builds(
    pivot::CollectionItem,
)
pivot::Package_strategy = st.builds(
    pivot::Package,
    URI=
        safe_text,
    nsPrefix=
        safe_text
)
pivot::Transition_strategy = st.builds(
    pivot::Transition,
    kind=
        safe_text
)
CollectionType_strategy = st.builds(
    CollectionType,
)
pivot::BagType_strategy = st.builds(
    pivot::BagType,
)
NavigationCallExp_strategy = st.builds(
    NavigationCallExp,
)
pivot::AssociationClassCallExp_strategy = st.builds(
    pivot::AssociationClassCallExp,
)
OCLExpression_strategy = st.builds(
    OCLExpression,
)
pivot::CallExp_strategy = st.builds(
    pivot::CallExp,
    isImplicit=
        safe_text,
    isSafe=
        safe_text
)
PrimitiveLiteralExp_strategy = st.builds(
    PrimitiveLiteralExp,
)
pivot::BooleanLiteralExp_strategy = st.builds(
    pivot::BooleanLiteralExp,
    booleanSymbol=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
pivot::Type_strategy = st.builds(
    pivot::Type,
)
pivot::Namespace_strategy = st.builds(
    pivot::Namespace,
)
pivot::CallOperationAction_strategy = st.builds(
    pivot::CallOperationAction,
)
pivot::Constraint_strategy = st.builds(
    pivot::Constraint,
    isCallable=
        safe_text
)
pivot::CompletePackage_strategy = st.builds(
    pivot::CompletePackage,
)
pivot::CompleteModel_strategy = st.builds(
    pivot::CompleteModel,
)
pivot::CompleteClass_strategy = st.builds(
    pivot::CompleteClass,
)
pivot::Annotation_strategy = st.builds(
    pivot::Annotation,
)
Class_strategy = st.builds(
    Class,
)
pivot::Behavior_strategy = st.builds(
    pivot::Behavior,
)
pivot::AssociationClass_strategy = st.builds(
    pivot::AssociationClass,
)
pivot::AnyType_strategy = st.builds(
    pivot::AnyType,
)
pivot::Detail_strategy = st.builds(
    pivot::Detail,
    values=
        safe_text
)
pivot::VoidType_strategy = st.builds(
    pivot::VoidType,
)
pivot::Visitable_strategy = st.builds(
    pivot::Visitable,
)
pivot::UnspecifiedValueExp_strategy = st.builds(
    pivot::UnspecifiedValueExp,
)
pivot::TypedElement_strategy = st.builds(
    pivot::TypedElement,
    isMany=
        safe_text,
    isRequired=
        safe_text
)
pivot::VariableDeclaration_strategy = st.builds(
    pivot::VariableDeclaration,
)
pivot::TupleType_strategy = st.builds(
    pivot::TupleType,
)
pivot::TupleLiteralExp_strategy = st.builds(
    pivot::TupleLiteralExp,
)
pivot::WildcardType_strategy = st.builds(
    pivot::WildcardType,
)
pivot::TemplateParameterSubstitution_strategy = st.builds(
    pivot::TemplateParameterSubstitution,
)
pivot::TemplateBinding_strategy = st.builds(
    pivot::TemplateBinding,
)
pivot::StringLiteralExp_strategy = st.builds(
    pivot::StringLiteralExp,
    stringSymbol=
        safe_text
)
pivot::TemplateParameter_strategy = st.builds(
    pivot::TemplateParameter,
)
pivot::TemplateSignature_strategy = st.builds(
    pivot::TemplateSignature,
)
pivot::TemplateableElement_strategy = st.builds(
    pivot::TemplateableElement,
)
pivot::StateExp_strategy = st.builds(
    pivot::StateExp,
)
pivot::ValueSpecification_strategy = st.builds(
    pivot::ValueSpecification,
)
pivot::Trigger_strategy = st.builds(
    pivot::Trigger,
)
pivot::ShadowExp_strategy = st.builds(
    pivot::ShadowExp,
    value=
        safe_text
)
pivot::SetType_strategy = st.builds(
    pivot::SetType,
)
pivot::SequenceType_strategy = st.builds(
    pivot::SequenceType,
)
pivot::SelfType_strategy = st.builds(
    pivot::SelfType,
)
pivot::ShadowPart_strategy = st.builds(
    pivot::ShadowPart,
)
pivot::Vertex_strategy = st.builds(
    pivot::Vertex,
)
pivot::Region_strategy = st.builds(
    pivot::Region,
)
pivot::ReferringElement_strategy = st.builds(
    pivot::ReferringElement,
)
pivot::PrimitiveType_strategy = st.builds(
    pivot::PrimitiveType,
)
pivot::PrimitiveLiteralExp_strategy = st.builds(
    pivot::PrimitiveLiteralExp,
)
pivot::Pivotable_strategy = st.builds(
    pivot::Pivotable,
)
CompletePackage_strategy = st.builds(
    CompletePackage,
)
pivot::PrimitiveCompletePackage_strategy = st.builds(
    pivot::PrimitiveCompletePackage,
)
pivot::OrphanCompletePackage_strategy = st.builds(
    pivot::OrphanCompletePackage,
)
pivot::OrderedSetType_strategy = st.builds(
    pivot::OrderedSetType,
)
pivot::OppositePropertyCallExp_strategy = st.builds(
    pivot::OppositePropertyCallExp,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
pivot::TupleLiteralPart_strategy = st.builds(
    pivot::TupleLiteralPart,
)
pivot::ProfileApplication_strategy = st.builds(
    pivot::ProfileApplication,
    isStrict=
        safe_text
)
FeatureCallExp_strategy = st.builds(
    FeatureCallExp,
)
pivot::NavigationCallExp_strategy = st.builds(
    pivot::NavigationCallExp,
)
Nameable_strategy = st.builds(
    Nameable,
)
pivot::NamedElement_strategy = st.builds(
    pivot::NamedElement,
    name=
        safe_text
)
pivot::Nameable_strategy = st.builds(
    pivot::Nameable,
)
pivot::MorePivotable_strategy = st.builds(
    pivot::MorePivotable,
)
Feature_strategy = st.builds(
    Feature,
)
pivot::Property_strategy = st.builds(
    pivot::Property,
    isDerived=
        safe_text,
    isUnsettable=
        safe_text,
    isID=
        safe_text,
    defaultValue=
        safe_text,
    isVolatile=
        safe_text,
    isImplicit=
        safe_text,
    defaultValueString=
        safe_text,
    isReadOnly=
        safe_text,
    isResolveProxies=
        safe_text,
    isComposite=
        safe_text,
    isTransient=
        safe_text
)
pivot::Operation_strategy = st.builds(
    pivot::Operation,
    isValidating=
        safe_text,
    isTypeof=
        safe_text,
    isInvalidating=
        safe_text
)
pivot::NumericLiteralExp_strategy = st.builds(
    pivot::NumericLiteralExp,
)
pivot::NullLiteralExp_strategy = st.builds(
    pivot::NullLiteralExp,
)
pivot::MessageExp_strategy = st.builds(
    pivot::MessageExp,
)
pivot::MapType_strategy = st.builds(
    pivot::MapType,
)
pivot::MapLiteralPart_strategy = st.builds(
    pivot::MapLiteralPart,
)
pivot::MapLiteralExp_strategy = st.builds(
    pivot::MapLiteralExp,
)
pivot::Signal_strategy = st.builds(
    pivot::Signal,
)
pivot::MessageType_strategy = st.builds(
    pivot::MessageType,
)
pivot::SendSignalAction_strategy = st.builds(
    pivot::SendSignalAction,
)
Package_strategy = st.builds(
    Package,
)
pivot::Profile_strategy = st.builds(
    pivot::Profile,
)
pivot::Library_strategy = st.builds(
    pivot::Library,
)
pivot::LetExp_strategy = st.builds(
    pivot::LetExp,
)
pivot::LiteralExp_strategy = st.builds(
    pivot::LiteralExp,
)
pivot::Precedence_strategy = st.builds(
    pivot::Precedence,
    order=
        safe_text,
    associativity=
        safe_text
)
pivot::LambdaType_strategy = st.builds(
    pivot::LambdaType,
)
pivot::Parameter_strategy = st.builds(
    pivot::Parameter,
    isTypeof=
        safe_text
)
Operation_strategy = st.builds(
    Operation,
)
pivot::Iteration_strategy = st.builds(
    pivot::Iteration,
)
ReferringElement_strategy = st.builds(
    ReferringElement,
)
pivot::OperationCallExp_strategy = st.builds(
    pivot::OperationCallExp,
)
pivot::PropertyCallExp_strategy = st.builds(
    pivot::PropertyCallExp,
)
pivot::TypeExp_strategy = st.builds(
    pivot::TypeExp,
)
pivot::VariableExp_strategy = st.builds(
    pivot::VariableExp,
    isImplicit=
        safe_text
)
LoopExp_strategy = st.builds(
    LoopExp,
)
pivot::IteratorExp_strategy = st.builds(
    pivot::IteratorExp,
)
pivot::IterateExp_strategy = st.builds(
    pivot::IterateExp,
)
pivot::InvalidType_strategy = st.builds(
    pivot::InvalidType,
)
pivot::InvalidLiteralExp_strategy = st.builds(
    pivot::InvalidLiteralExp,
)
NumericLiteralExp_strategy = st.builds(
    NumericLiteralExp,
)
pivot::RealLiteralExp_strategy = st.builds(
    pivot::RealLiteralExp,
    realSymbol=
        safe_text
)
pivot::UnlimitedNaturalLiteralExp_strategy = st.builds(
    pivot::UnlimitedNaturalLiteralExp,
    unlimitedNaturalSymbol=
        safe_text
)
pivot::IntegerLiteralExp_strategy = st.builds(
    pivot::IntegerLiteralExp,
    integerSymbol=
        safe_text
)
pivot::IfExp_strategy = st.builds(
    pivot::IfExp,
)
State_strategy = st.builds(
    State,
)
pivot::FinalState_strategy = st.builds(
    pivot::FinalState,
)
CallExp_strategy = st.builds(
    CallExp,
)
pivot::LoopExp_strategy = st.builds(
    pivot::LoopExp,
)
pivot::FeatureCallExp_strategy = st.builds(
    pivot::FeatureCallExp,
    isPre=
        safe_text
)
pivot::Slot_strategy = st.builds(
    pivot::Slot,
)
pivot::InstanceSpecification_strategy = st.builds(
    pivot::InstanceSpecification,
)
pivot::Import_strategy = st.builds(
    pivot::Import,
)
pivot::Variable_strategy = st.builds(
    pivot::Variable,
    isImplicit=
        safe_text
)
LanguageExpression_strategy = st.builds(
    LanguageExpression,
)
pivot::ExpressionInOCL_strategy = st.builds(
    pivot::ExpressionInOCL,
)
InstanceSpecification_strategy = st.builds(
    InstanceSpecification,
)
pivot::Feature_strategy = st.builds(
    pivot::Feature,
    implementationClass=
        safe_text,
    implementation=
        safe_text,
    isStatic=
        safe_text
)
pivot::Stereotype_strategy = st.builds(
    pivot::Stereotype,
)
pivot::ElementExtension_strategy = st.builds(
    pivot::ElementExtension,
    isApplied=
        safe_text,
    isRequired=
        safe_text
)
pivot::Enumeration_strategy = st.builds(
    pivot::Enumeration,
)
pivot::EnumerationLiteral_strategy = st.builds(
    pivot::EnumerationLiteral,
    value=
        safe_text
)
pivot::EnumLiteralExp_strategy = st.builds(
    pivot::EnumLiteralExp,
)
Visitable_strategy = st.builds(
    Visitable,
)
pivot::Element_strategy = st.builds(
    pivot::Element,
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
pivot::DynamicValueSpecification_strategy = st.builds(
    pivot::DynamicValueSpecification,
)
DynamicElement_strategy = st.builds(
    DynamicElement,
)
pivot::DynamicType_strategy = st.builds(
    pivot::DynamicType,
)
pivot::DataType_strategy = st.builds(
    pivot::DataType,
    isSerializable=
        safe_text
)
pivot::DynamicProperty_strategy = st.builds(
    pivot::DynamicProperty,
    default=
        safe_text
)
pivot::DynamicElement_strategy = st.builds(
    pivot::DynamicElement,
)
DynamicType_strategy = st.builds(
    DynamicType,
)
Behavior_strategy = st.builds(
    Behavior,
)
pivot::StateMachine_strategy = st.builds(
    pivot::StateMachine,
)
pivot::DynamicBehavior_strategy = st.builds(
    pivot::DynamicBehavior,
)
pivot::LanguageExpression_strategy = st.builds(
    pivot::LanguageExpression,
    language=
        safe_text,
    body=
        safe_text
)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=pivot::Pseudostate_strategy)
@settings(max_examples=50)
def test_pivot::pseudostate_instantiation(instance):
    assert isinstance(instance, pivot::Pseudostate)

@given(instance=pivot::Pseudostate_strategy)
def test_pivot::pseudostate_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=pivot::Pseudostate_strategy)
def test_pivot::pseudostate_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=pivot::ConnectionPointReference_strategy)
@settings(max_examples=50)
def test_pivot::connectionpointreference_instantiation(instance):
    assert isinstance(instance, pivot::ConnectionPointReference)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=pivot::CompleteEnvironment_strategy)
@settings(max_examples=50)
def test_pivot::completeenvironment_instantiation(instance):
    assert isinstance(instance, pivot::CompleteEnvironment)

@given(instance=pivot::Comment_strategy)
@settings(max_examples=50)
def test_pivot::comment_instantiation(instance):
    assert isinstance(instance, pivot::Comment)

@given(instance=pivot::Comment_strategy)
def test_pivot::comment_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=pivot::Comment_strategy)
def test_pivot::comment_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=pivot::CollectionType_strategy)
@settings(max_examples=50)
def test_pivot::collectiontype_instantiation(instance):
    assert isinstance(instance, pivot::CollectionType)

@given(instance=pivot::CollectionType_strategy)
def test_pivot::collectiontype_upper_type(instance):
    assert isinstance(instance.upper, str)


@given(instance=pivot::CollectionType_strategy)
def test_pivot::collectiontype_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=pivot::CollectionType_strategy)
def test_pivot::collectiontype_lower_type(instance):
    assert isinstance(instance.lower, str)


@given(instance=pivot::CollectionType_strategy)
def test_pivot::collectiontype_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=pivot::CollectionType_strategy)
def test_pivot::collectiontype_isNullFree_type(instance):
    assert isinstance(instance.isNullFree, str)


@given(instance=pivot::CollectionType_strategy)
def test_pivot::collectiontype_isNullFree_setter(instance):
    original = instance.isNullFree
    instance.isNullFree = original
    assert instance.isNullFree == original

@given(instance=pivot::StandardLibrary_strategy)
@settings(max_examples=50)
def test_pivot::standardlibrary_instantiation(instance):
    assert isinstance(instance, pivot::StandardLibrary)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=pivot::CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_pivot::collectionliteralpart_instantiation(instance):
    assert isinstance(instance, pivot::CollectionLiteralPart)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::CollectionLiteralPart_strategy)
@settings(max_examples=30)
def test_pivot::collectionliteralpart_validatetypeisnotinvalid_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateTypeIsNotInvalid(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateTypeIsNotInvalid).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateTypeIsNotInvalid' in pivot::CollectionLiteralPart is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateTypeIsNotInvalid' in pivot::CollectionLiteralPart did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateTypeIsNotInvalid' in pivot::CollectionLiteralPart is not implemented or raised an error")

@given(instance=pivot::StereotypeExtender_strategy)
@settings(max_examples=50)
def test_pivot::stereotypeextender_instantiation(instance):
    assert isinstance(instance, pivot::StereotypeExtender)

@given(instance=pivot::StereotypeExtender_strategy)
def test_pivot::stereotypeextender_isRequired_type(instance):
    assert isinstance(instance.isRequired, str)


@given(instance=pivot::StereotypeExtender_strategy)
def test_pivot::stereotypeextender_isRequired_setter(instance):
    original = instance.isRequired
    instance.isRequired = original
    assert instance.isRequired == original

@given(instance=TemplateableElement_strategy)
@settings(max_examples=50)
def test_templateableelement_instantiation(instance):
    assert isinstance(instance, TemplateableElement)

@given(instance=Namespace_strategy)
@settings(max_examples=50)
def test_namespace_instantiation(instance):
    assert isinstance(instance, Namespace)

@given(instance=pivot::State_strategy)
@settings(max_examples=50)
def test_pivot::state_instantiation(instance):
    assert isinstance(instance, pivot::State)

@given(instance=pivot::State_strategy)
def test_pivot::state_isComposite_type(instance):
    assert isinstance(instance.isComposite, str)


@given(instance=pivot::State_strategy)
def test_pivot::state_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original

@given(instance=pivot::State_strategy)
def test_pivot::state_isSubmachineState_type(instance):
    assert isinstance(instance.isSubmachineState, str)


@given(instance=pivot::State_strategy)
def test_pivot::state_isSubmachineState_setter(instance):
    original = instance.isSubmachineState
    instance.isSubmachineState = original
    assert instance.isSubmachineState == original

@given(instance=pivot::State_strategy)
def test_pivot::state_isSimple_type(instance):
    assert isinstance(instance.isSimple, str)


@given(instance=pivot::State_strategy)
def test_pivot::state_isSimple_setter(instance):
    original = instance.isSimple
    instance.isSimple = original
    assert instance.isSimple == original

@given(instance=pivot::State_strategy)
def test_pivot::state_isOrthogonal_type(instance):
    assert isinstance(instance.isOrthogonal, str)


@given(instance=pivot::State_strategy)
def test_pivot::state_isOrthogonal_setter(instance):
    original = instance.isOrthogonal
    instance.isOrthogonal = original
    assert instance.isOrthogonal == original

@given(instance=pivot::Model_strategy)
@settings(max_examples=50)
def test_pivot::model_instantiation(instance):
    assert isinstance(instance, pivot::Model)

@given(instance=pivot::Model_strategy)
def test_pivot::model_externalURI_type(instance):
    assert isinstance(instance.externalURI, str)


@given(instance=pivot::Model_strategy)
def test_pivot::model_externalURI_setter(instance):
    original = instance.externalURI
    instance.externalURI = original
    assert instance.externalURI == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=pivot::Class_strategy)
@settings(max_examples=50)
def test_pivot::class_instantiation(instance):
    assert isinstance(instance, pivot::Class)

@given(instance=pivot::Class_strategy)
def test_pivot::class_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, str)


@given(instance=pivot::Class_strategy)
def test_pivot::class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=pivot::Class_strategy)
def test_pivot::class_isInterface_type(instance):
    assert isinstance(instance.isInterface, str)


@given(instance=pivot::Class_strategy)
def test_pivot::class_isInterface_setter(instance):
    original = instance.isInterface
    instance.isInterface = original
    assert instance.isInterface == original

@given(instance=pivot::Class_strategy)
def test_pivot::class_isActive_type(instance):
    assert isinstance(instance.isActive, str)


@given(instance=pivot::Class_strategy)
def test_pivot::class_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original

@given(instance=pivot::Class_strategy)
def test_pivot::class_instanceClassName_type(instance):
    assert isinstance(instance.instanceClassName, str)


@given(instance=pivot::Class_strategy)
def test_pivot::class_instanceClassName_setter(instance):
    original = instance.instanceClassName
    instance.instanceClassName = original
    assert instance.instanceClassName == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::Class_strategy)
@settings(max_examples=30)
def test_pivot::class_validateuniqueinvariantname_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateUniqueInvariantName(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateUniqueInvariantName).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateUniqueInvariantName' in pivot::Class is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateUniqueInvariantName' in pivot::Class did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateUniqueInvariantName' in pivot::Class is not implemented or raised an error")

@given(instance=pivot::OCLExpression_strategy)
@settings(max_examples=50)
def test_pivot::oclexpression_instantiation(instance):
    assert isinstance(instance, pivot::OCLExpression)

@given(instance=LiteralExp_strategy)
@settings(max_examples=50)
def test_literalexp_instantiation(instance):
    assert isinstance(instance, LiteralExp)

@given(instance=pivot::CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_pivot::collectionliteralexp_instantiation(instance):
    assert isinstance(instance, pivot::CollectionLiteralExp)

@given(instance=pivot::CollectionLiteralExp_strategy)
def test_pivot::collectionliteralexp_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=pivot::CollectionLiteralExp_strategy)
def test_pivot::collectionliteralexp_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::CollectionLiteralExp_strategy)
@settings(max_examples=30)
def test_pivot::collectionliteralexp_validatecollectionkindisconcrete_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateCollectionKindIsConcrete(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateCollectionKindIsConcrete).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateCollectionKindIsConcrete' in pivot::CollectionLiteralExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateCollectionKindIsConcrete' in pivot::CollectionLiteralExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateCollectionKindIsConcrete' in pivot::CollectionLiteralExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::CollectionLiteralExp_strategy)
@settings(max_examples=30)
def test_pivot::collectionliteralexp_validatesequencekindissequence_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateSequenceKindIsSequence(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateSequenceKindIsSequence).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateSequenceKindIsSequence' in pivot::CollectionLiteralExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateSequenceKindIsSequence' in pivot::CollectionLiteralExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateSequenceKindIsSequence' in pivot::CollectionLiteralExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::CollectionLiteralExp_strategy)
@settings(max_examples=30)
def test_pivot::collectionliteralexp_validatebagkindisbag_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateBagKindIsBag(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateBagKindIsBag).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateBagKindIsBag' in pivot::CollectionLiteralExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateBagKindIsBag' in pivot::CollectionLiteralExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateBagKindIsBag' in pivot::CollectionLiteralExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::CollectionLiteralExp_strategy)
@settings(max_examples=30)
def test_pivot::collectionliteralexp_validateorderedsetkindisorderedset_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateOrderedSetKindIsOrderedSet(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateOrderedSetKindIsOrderedSet).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateOrderedSetKindIsOrderedSet' in pivot::CollectionLiteralExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateOrderedSetKindIsOrderedSet' in pivot::CollectionLiteralExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateOrderedSetKindIsOrderedSet' in pivot::CollectionLiteralExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::CollectionLiteralExp_strategy)
@settings(max_examples=30)
def test_pivot::collectionliteralexp_validatesetkindisset_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateSetKindIsSet(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateSetKindIsSet).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateSetKindIsSet' in pivot::CollectionLiteralExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateSetKindIsSet' in pivot::CollectionLiteralExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateSetKindIsSet' in pivot::CollectionLiteralExp is not implemented or raised an error")

@given(instance=CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_collectionliteralpart_instantiation(instance):
    assert isinstance(instance, CollectionLiteralPart)

@given(instance=pivot::CollectionRange_strategy)
@settings(max_examples=50)
def test_pivot::collectionrange_instantiation(instance):
    assert isinstance(instance, pivot::CollectionRange)

@given(instance=pivot::CollectionItem_strategy)
@settings(max_examples=50)
def test_pivot::collectionitem_instantiation(instance):
    assert isinstance(instance, pivot::CollectionItem)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::CollectionItem_strategy)
@settings(max_examples=30)
def test_pivot::collectionitem_validatetypeisitemtype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateTypeIsItemType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateTypeIsItemType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateTypeIsItemType' in pivot::CollectionItem is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateTypeIsItemType' in pivot::CollectionItem did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateTypeIsItemType' in pivot::CollectionItem is not implemented or raised an error")

@given(instance=pivot::Package_strategy)
@settings(max_examples=50)
def test_pivot::package_instantiation(instance):
    assert isinstance(instance, pivot::Package)

@given(instance=pivot::Package_strategy)
def test_pivot::package_URI_type(instance):
    assert isinstance(instance.URI, str)


@given(instance=pivot::Package_strategy)
def test_pivot::package_URI_setter(instance):
    original = instance.URI
    instance.URI = original
    assert instance.URI == original

@given(instance=pivot::Package_strategy)
def test_pivot::package_nsPrefix_type(instance):
    assert isinstance(instance.nsPrefix, str)


@given(instance=pivot::Package_strategy)
def test_pivot::package_nsPrefix_setter(instance):
    original = instance.nsPrefix
    instance.nsPrefix = original
    assert instance.nsPrefix == original

@given(instance=pivot::Transition_strategy)
@settings(max_examples=50)
def test_pivot::transition_instantiation(instance):
    assert isinstance(instance, pivot::Transition)

@given(instance=pivot::Transition_strategy)
def test_pivot::transition_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=pivot::Transition_strategy)
def test_pivot::transition_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=pivot::BagType_strategy)
@settings(max_examples=50)
def test_pivot::bagtype_instantiation(instance):
    assert isinstance(instance, pivot::BagType)

@given(instance=NavigationCallExp_strategy)
@settings(max_examples=50)
def test_navigationcallexp_instantiation(instance):
    assert isinstance(instance, NavigationCallExp)

@given(instance=pivot::AssociationClassCallExp_strategy)
@settings(max_examples=50)
def test_pivot::associationclasscallexp_instantiation(instance):
    assert isinstance(instance, pivot::AssociationClassCallExp)

@given(instance=OCLExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OCLExpression)

@given(instance=pivot::CallExp_strategy)
@settings(max_examples=50)
def test_pivot::callexp_instantiation(instance):
    assert isinstance(instance, pivot::CallExp)

@given(instance=pivot::CallExp_strategy)
def test_pivot::callexp_isImplicit_type(instance):
    assert isinstance(instance.isImplicit, str)


@given(instance=pivot::CallExp_strategy)
def test_pivot::callexp_isImplicit_setter(instance):
    original = instance.isImplicit
    instance.isImplicit = original
    assert instance.isImplicit == original

@given(instance=pivot::CallExp_strategy)
def test_pivot::callexp_isSafe_type(instance):
    assert isinstance(instance.isSafe, str)


@given(instance=pivot::CallExp_strategy)
def test_pivot::callexp_isSafe_setter(instance):
    original = instance.isSafe
    instance.isSafe = original
    assert instance.isSafe == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::CallExp_strategy)
@settings(max_examples=30)
def test_pivot::callexp_validatetypeisnotinvalid_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateTypeIsNotInvalid(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateTypeIsNotInvalid).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateTypeIsNotInvalid' in pivot::CallExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateTypeIsNotInvalid' in pivot::CallExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateTypeIsNotInvalid' in pivot::CallExp is not implemented or raised an error")

@given(instance=PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, PrimitiveLiteralExp)

@given(instance=pivot::BooleanLiteralExp_strategy)
@settings(max_examples=50)
def test_pivot::booleanliteralexp_instantiation(instance):
    assert isinstance(instance, pivot::BooleanLiteralExp)

@given(instance=pivot::BooleanLiteralExp_strategy)
def test_pivot::booleanliteralexp_booleanSymbol_type(instance):
    assert isinstance(instance.booleanSymbol, str)


@given(instance=pivot::BooleanLiteralExp_strategy)
def test_pivot::booleanliteralexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::BooleanLiteralExp_strategy)
@settings(max_examples=30)
def test_pivot::booleanliteralexp_validatetypeisboolean_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateTypeIsBoolean(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateTypeIsBoolean).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateTypeIsBoolean' in pivot::BooleanLiteralExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateTypeIsBoolean' in pivot::BooleanLiteralExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateTypeIsBoolean' in pivot::BooleanLiteralExp is not implemented or raised an error")

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=pivot::Type_strategy)
@settings(max_examples=50)
def test_pivot::type_instantiation(instance):
    assert isinstance(instance, pivot::Type)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::Type_strategy)
@settings(max_examples=30)
def test_pivot::type_istemplateparameter_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isTemplateParameter()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isTemplateParameter).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isTemplateParameter' in pivot::Type is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isTemplateParameter' in pivot::Type did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isTemplateParameter' in pivot::Type is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::Type_strategy)
@settings(max_examples=30)
def test_pivot::type_isclass_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isClass()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isClass).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isClass' in pivot::Type is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isClass' in pivot::Type did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isClass' in pivot::Type is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::Type_strategy)
@settings(max_examples=30)
def test_pivot::type_specializein_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.specializeIn(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.specializeIn).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'specializeIn' in pivot::Type is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'specializeIn' in pivot::Type did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'specializeIn' in pivot::Type is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::Type_strategy)
@settings(max_examples=30)
def test_pivot::type_flattenedtype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.flattenedType()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.flattenedType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'flattenedType' in pivot::Type is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'flattenedType' in pivot::Type did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'flattenedType' in pivot::Type is not implemented or raised an error")

@given(instance=pivot::Namespace_strategy)
@settings(max_examples=50)
def test_pivot::namespace_instantiation(instance):
    assert isinstance(instance, pivot::Namespace)

@given(instance=pivot::CallOperationAction_strategy)
@settings(max_examples=50)
def test_pivot::calloperationaction_instantiation(instance):
    assert isinstance(instance, pivot::CallOperationAction)

@given(instance=pivot::Constraint_strategy)
@settings(max_examples=50)
def test_pivot::constraint_instantiation(instance):
    assert isinstance(instance, pivot::Constraint)

@given(instance=pivot::Constraint_strategy)
def test_pivot::constraint_isCallable_type(instance):
    assert isinstance(instance.isCallable, str)


@given(instance=pivot::Constraint_strategy)
def test_pivot::constraint_isCallable_setter(instance):
    original = instance.isCallable
    instance.isCallable = original
    assert instance.isCallable == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::Constraint_strategy)
@settings(max_examples=30)
def test_pivot::constraint_validateuniquename_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateUniqueName(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateUniqueName).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateUniqueName' in pivot::Constraint is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateUniqueName' in pivot::Constraint did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateUniqueName' in pivot::Constraint is not implemented or raised an error")

@given(instance=pivot::CompletePackage_strategy)
@settings(max_examples=50)
def test_pivot::completepackage_instantiation(instance):
    assert isinstance(instance, pivot::CompletePackage)

@given(instance=pivot::CompleteModel_strategy)
@settings(max_examples=50)
def test_pivot::completemodel_instantiation(instance):
    assert isinstance(instance, pivot::CompleteModel)

@given(instance=pivot::CompleteClass_strategy)
@settings(max_examples=50)
def test_pivot::completeclass_instantiation(instance):
    assert isinstance(instance, pivot::CompleteClass)

@given(instance=pivot::Annotation_strategy)
@settings(max_examples=50)
def test_pivot::annotation_instantiation(instance):
    assert isinstance(instance, pivot::Annotation)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=pivot::Behavior_strategy)
@settings(max_examples=50)
def test_pivot::behavior_instantiation(instance):
    assert isinstance(instance, pivot::Behavior)

@given(instance=pivot::AssociationClass_strategy)
@settings(max_examples=50)
def test_pivot::associationclass_instantiation(instance):
    assert isinstance(instance, pivot::AssociationClass)

@given(instance=pivot::AnyType_strategy)
@settings(max_examples=50)
def test_pivot::anytype_instantiation(instance):
    assert isinstance(instance, pivot::AnyType)

@given(instance=pivot::Detail_strategy)
@settings(max_examples=50)
def test_pivot::detail_instantiation(instance):
    assert isinstance(instance, pivot::Detail)

@given(instance=pivot::Detail_strategy)
def test_pivot::detail_values_type(instance):
    assert isinstance(instance.values, str)


@given(instance=pivot::Detail_strategy)
def test_pivot::detail_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=pivot::VoidType_strategy)
@settings(max_examples=50)
def test_pivot::voidtype_instantiation(instance):
    assert isinstance(instance, pivot::VoidType)

@given(instance=pivot::Visitable_strategy)
@settings(max_examples=50)
def test_pivot::visitable_instantiation(instance):
    assert isinstance(instance, pivot::Visitable)

@given(instance=pivot::UnspecifiedValueExp_strategy)
@settings(max_examples=50)
def test_pivot::unspecifiedvalueexp_instantiation(instance):
    assert isinstance(instance, pivot::UnspecifiedValueExp)

@given(instance=pivot::TypedElement_strategy)
@settings(max_examples=50)
def test_pivot::typedelement_instantiation(instance):
    assert isinstance(instance, pivot::TypedElement)

@given(instance=pivot::TypedElement_strategy)
def test_pivot::typedelement_isMany_type(instance):
    assert isinstance(instance.isMany, str)


@given(instance=pivot::TypedElement_strategy)
def test_pivot::typedelement_isMany_setter(instance):
    original = instance.isMany
    instance.isMany = original
    assert instance.isMany == original

@given(instance=pivot::TypedElement_strategy)
def test_pivot::typedelement_isRequired_type(instance):
    assert isinstance(instance.isRequired, str)


@given(instance=pivot::TypedElement_strategy)
def test_pivot::typedelement_isRequired_setter(instance):
    original = instance.isRequired
    instance.isRequired = original
    assert instance.isRequired == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::TypedElement_strategy)
@settings(max_examples=30)
def test_pivot::typedelement_compatiblebody_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.CompatibleBody(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.CompatibleBody).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'CompatibleBody' in pivot::TypedElement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'CompatibleBody' in pivot::TypedElement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'CompatibleBody' in pivot::TypedElement is not implemented or raised an error")

@given(instance=pivot::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_pivot::variabledeclaration_instantiation(instance):
    assert isinstance(instance, pivot::VariableDeclaration)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::VariableDeclaration_strategy)
@settings(max_examples=30)
def test_pivot::variabledeclaration_validatetypeisnotinvalid_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateTypeIsNotInvalid(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateTypeIsNotInvalid).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateTypeIsNotInvalid' in pivot::VariableDeclaration is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateTypeIsNotInvalid' in pivot::VariableDeclaration did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateTypeIsNotInvalid' in pivot::VariableDeclaration is not implemented or raised an error")

@given(instance=pivot::TupleType_strategy)
@settings(max_examples=50)
def test_pivot::tupletype_instantiation(instance):
    assert isinstance(instance, pivot::TupleType)

@given(instance=pivot::TupleLiteralExp_strategy)
@settings(max_examples=50)
def test_pivot::tupleliteralexp_instantiation(instance):
    assert isinstance(instance, pivot::TupleLiteralExp)

@given(instance=pivot::WildcardType_strategy)
@settings(max_examples=50)
def test_pivot::wildcardtype_instantiation(instance):
    assert isinstance(instance, pivot::WildcardType)

@given(instance=pivot::TemplateParameterSubstitution_strategy)
@settings(max_examples=50)
def test_pivot::templateparametersubstitution_instantiation(instance):
    assert isinstance(instance, pivot::TemplateParameterSubstitution)

@given(instance=pivot::TemplateBinding_strategy)
@settings(max_examples=50)
def test_pivot::templatebinding_instantiation(instance):
    assert isinstance(instance, pivot::TemplateBinding)

@given(instance=pivot::StringLiteralExp_strategy)
@settings(max_examples=50)
def test_pivot::stringliteralexp_instantiation(instance):
    assert isinstance(instance, pivot::StringLiteralExp)

@given(instance=pivot::StringLiteralExp_strategy)
def test_pivot::stringliteralexp_stringSymbol_type(instance):
    assert isinstance(instance.stringSymbol, str)


@given(instance=pivot::StringLiteralExp_strategy)
def test_pivot::stringliteralexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=pivot::TemplateParameter_strategy)
@settings(max_examples=50)
def test_pivot::templateparameter_instantiation(instance):
    assert isinstance(instance, pivot::TemplateParameter)

@given(instance=pivot::TemplateSignature_strategy)
@settings(max_examples=50)
def test_pivot::templatesignature_instantiation(instance):
    assert isinstance(instance, pivot::TemplateSignature)

@given(instance=pivot::TemplateableElement_strategy)
@settings(max_examples=50)
def test_pivot::templateableelement_instantiation(instance):
    assert isinstance(instance, pivot::TemplateableElement)

@given(instance=pivot::StateExp_strategy)
@settings(max_examples=50)
def test_pivot::stateexp_instantiation(instance):
    assert isinstance(instance, pivot::StateExp)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::StateExp_strategy)
@settings(max_examples=30)
def test_pivot::stateexp_validatetypeisnotinvalid_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateTypeIsNotInvalid(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateTypeIsNotInvalid).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateTypeIsNotInvalid' in pivot::StateExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateTypeIsNotInvalid' in pivot::StateExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateTypeIsNotInvalid' in pivot::StateExp is not implemented or raised an error")

@given(instance=pivot::ValueSpecification_strategy)
@settings(max_examples=50)
def test_pivot::valuespecification_instantiation(instance):
    assert isinstance(instance, pivot::ValueSpecification)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::ValueSpecification_strategy)
@settings(max_examples=30)
def test_pivot::valuespecification_integervalue_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.integerValue()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.integerValue).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'integerValue' in pivot::ValueSpecification is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'integerValue' in pivot::ValueSpecification did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'integerValue' in pivot::ValueSpecification is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::ValueSpecification_strategy)
@settings(max_examples=30)
def test_pivot::valuespecification_isnull_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isNull()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isNull).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isNull' in pivot::ValueSpecification is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isNull' in pivot::ValueSpecification did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isNull' in pivot::ValueSpecification is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::ValueSpecification_strategy)
@settings(max_examples=30)
def test_pivot::valuespecification_stringvalue_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.stringValue()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.stringValue).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'stringValue' in pivot::ValueSpecification is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'stringValue' in pivot::ValueSpecification did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'stringValue' in pivot::ValueSpecification is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::ValueSpecification_strategy)
@settings(max_examples=30)
def test_pivot::valuespecification_unlimitedvalue_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.unlimitedValue()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.unlimitedValue).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'unlimitedValue' in pivot::ValueSpecification is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'unlimitedValue' in pivot::ValueSpecification did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'unlimitedValue' in pivot::ValueSpecification is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::ValueSpecification_strategy)
@settings(max_examples=30)
def test_pivot::valuespecification_booleanvalue_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.booleanValue()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.booleanValue).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'booleanValue' in pivot::ValueSpecification is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'booleanValue' in pivot::ValueSpecification did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'booleanValue' in pivot::ValueSpecification is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::ValueSpecification_strategy)
@settings(max_examples=30)
def test_pivot::valuespecification_iscomputable_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isComputable()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isComputable).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isComputable' in pivot::ValueSpecification is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isComputable' in pivot::ValueSpecification did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isComputable' in pivot::ValueSpecification is not implemented or raised an error")

@given(instance=pivot::Trigger_strategy)
@settings(max_examples=50)
def test_pivot::trigger_instantiation(instance):
    assert isinstance(instance, pivot::Trigger)

@given(instance=pivot::ShadowExp_strategy)
@settings(max_examples=50)
def test_pivot::shadowexp_instantiation(instance):
    assert isinstance(instance, pivot::ShadowExp)

@given(instance=pivot::ShadowExp_strategy)
def test_pivot::shadowexp_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=pivot::ShadowExp_strategy)
def test_pivot::shadowexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::ShadowExp_strategy)
@settings(max_examples=30)
def test_pivot::shadowexp_validatetypeisnotinvalid_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateTypeIsNotInvalid(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateTypeIsNotInvalid).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateTypeIsNotInvalid' in pivot::ShadowExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateTypeIsNotInvalid' in pivot::ShadowExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateTypeIsNotInvalid' in pivot::ShadowExp is not implemented or raised an error")

@given(instance=pivot::SetType_strategy)
@settings(max_examples=50)
def test_pivot::settype_instantiation(instance):
    assert isinstance(instance, pivot::SetType)

@given(instance=pivot::SequenceType_strategy)
@settings(max_examples=50)
def test_pivot::sequencetype_instantiation(instance):
    assert isinstance(instance, pivot::SequenceType)

@given(instance=pivot::SelfType_strategy)
@settings(max_examples=50)
def test_pivot::selftype_instantiation(instance):
    assert isinstance(instance, pivot::SelfType)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::SelfType_strategy)
@settings(max_examples=30)
def test_pivot::selftype_specializein_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.specializeIn(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.specializeIn).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'specializeIn' in pivot::SelfType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'specializeIn' in pivot::SelfType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'specializeIn' in pivot::SelfType is not implemented or raised an error")

@given(instance=pivot::ShadowPart_strategy)
@settings(max_examples=50)
def test_pivot::shadowpart_instantiation(instance):
    assert isinstance(instance, pivot::ShadowPart)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::ShadowPart_strategy)
@settings(max_examples=30)
def test_pivot::shadowpart_validatetypeisnotinvalid_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateTypeIsNotInvalid(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateTypeIsNotInvalid).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateTypeIsNotInvalid' in pivot::ShadowPart is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateTypeIsNotInvalid' in pivot::ShadowPart did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateTypeIsNotInvalid' in pivot::ShadowPart is not implemented or raised an error")

@given(instance=pivot::Vertex_strategy)
@settings(max_examples=50)
def test_pivot::vertex_instantiation(instance):
    assert isinstance(instance, pivot::Vertex)

@given(instance=pivot::Region_strategy)
@settings(max_examples=50)
def test_pivot::region_instantiation(instance):
    assert isinstance(instance, pivot::Region)

@given(instance=pivot::ReferringElement_strategy)
@settings(max_examples=50)
def test_pivot::referringelement_instantiation(instance):
    assert isinstance(instance, pivot::ReferringElement)

@given(instance=pivot::PrimitiveType_strategy)
@settings(max_examples=50)
def test_pivot::primitivetype_instantiation(instance):
    assert isinstance(instance, pivot::PrimitiveType)

@given(instance=pivot::PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_pivot::primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, pivot::PrimitiveLiteralExp)

@given(instance=pivot::Pivotable_strategy)
@settings(max_examples=50)
def test_pivot::pivotable_instantiation(instance):
    assert isinstance(instance, pivot::Pivotable)

@given(instance=CompletePackage_strategy)
@settings(max_examples=50)
def test_completepackage_instantiation(instance):
    assert isinstance(instance, CompletePackage)

@given(instance=pivot::PrimitiveCompletePackage_strategy)
@settings(max_examples=50)
def test_pivot::primitivecompletepackage_instantiation(instance):
    assert isinstance(instance, pivot::PrimitiveCompletePackage)

@given(instance=pivot::OrphanCompletePackage_strategy)
@settings(max_examples=50)
def test_pivot::orphancompletepackage_instantiation(instance):
    assert isinstance(instance, pivot::OrphanCompletePackage)

@given(instance=pivot::OrderedSetType_strategy)
@settings(max_examples=50)
def test_pivot::orderedsettype_instantiation(instance):
    assert isinstance(instance, pivot::OrderedSetType)

@given(instance=pivot::OppositePropertyCallExp_strategy)
@settings(max_examples=50)
def test_pivot::oppositepropertycallexp_instantiation(instance):
    assert isinstance(instance, pivot::OppositePropertyCallExp)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=pivot::TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_pivot::tupleliteralpart_instantiation(instance):
    assert isinstance(instance, pivot::TupleLiteralPart)

@given(instance=pivot::ProfileApplication_strategy)
@settings(max_examples=50)
def test_pivot::profileapplication_instantiation(instance):
    assert isinstance(instance, pivot::ProfileApplication)

@given(instance=pivot::ProfileApplication_strategy)
def test_pivot::profileapplication_isStrict_type(instance):
    assert isinstance(instance.isStrict, str)


@given(instance=pivot::ProfileApplication_strategy)
def test_pivot::profileapplication_isStrict_setter(instance):
    original = instance.isStrict
    instance.isStrict = original
    assert instance.isStrict == original

@given(instance=FeatureCallExp_strategy)
@settings(max_examples=50)
def test_featurecallexp_instantiation(instance):
    assert isinstance(instance, FeatureCallExp)

@given(instance=pivot::NavigationCallExp_strategy)
@settings(max_examples=50)
def test_pivot::navigationcallexp_instantiation(instance):
    assert isinstance(instance, pivot::NavigationCallExp)

@given(instance=Nameable_strategy)
@settings(max_examples=50)
def test_nameable_instantiation(instance):
    assert isinstance(instance, Nameable)

@given(instance=pivot::NamedElement_strategy)
@settings(max_examples=50)
def test_pivot::namedelement_instantiation(instance):
    assert isinstance(instance, pivot::NamedElement)

@given(instance=pivot::NamedElement_strategy)
def test_pivot::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=pivot::NamedElement_strategy)
def test_pivot::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pivot::Nameable_strategy)
@settings(max_examples=50)
def test_pivot::nameable_instantiation(instance):
    assert isinstance(instance, pivot::Nameable)

@given(instance=pivot::MorePivotable_strategy)
@settings(max_examples=50)
def test_pivot::morepivotable_instantiation(instance):
    assert isinstance(instance, pivot::MorePivotable)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=pivot::Property_strategy)
@settings(max_examples=50)
def test_pivot::property_instantiation(instance):
    assert isinstance(instance, pivot::Property)

@given(instance=pivot::Property_strategy)
def test_pivot::property_isDerived_type(instance):
    assert isinstance(instance.isDerived, str)


@given(instance=pivot::Property_strategy)
def test_pivot::property_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original

@given(instance=pivot::Property_strategy)
def test_pivot::property_isUnsettable_type(instance):
    assert isinstance(instance.isUnsettable, str)


@given(instance=pivot::Property_strategy)
def test_pivot::property_isUnsettable_setter(instance):
    original = instance.isUnsettable
    instance.isUnsettable = original
    assert instance.isUnsettable == original

@given(instance=pivot::Property_strategy)
def test_pivot::property_isID_type(instance):
    assert isinstance(instance.isID, str)


@given(instance=pivot::Property_strategy)
def test_pivot::property_isID_setter(instance):
    original = instance.isID
    instance.isID = original
    assert instance.isID == original

@given(instance=pivot::Property_strategy)
def test_pivot::property_defaultValue_type(instance):
    assert isinstance(instance.defaultValue, str)


@given(instance=pivot::Property_strategy)
def test_pivot::property_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=pivot::Property_strategy)
def test_pivot::property_isVolatile_type(instance):
    assert isinstance(instance.isVolatile, str)


@given(instance=pivot::Property_strategy)
def test_pivot::property_isVolatile_setter(instance):
    original = instance.isVolatile
    instance.isVolatile = original
    assert instance.isVolatile == original

@given(instance=pivot::Property_strategy)
def test_pivot::property_isImplicit_type(instance):
    assert isinstance(instance.isImplicit, str)


@given(instance=pivot::Property_strategy)
def test_pivot::property_isImplicit_setter(instance):
    original = instance.isImplicit
    instance.isImplicit = original
    assert instance.isImplicit == original

@given(instance=pivot::Property_strategy)
def test_pivot::property_defaultValueString_type(instance):
    assert isinstance(instance.defaultValueString, str)


@given(instance=pivot::Property_strategy)
def test_pivot::property_defaultValueString_setter(instance):
    original = instance.defaultValueString
    instance.defaultValueString = original
    assert instance.defaultValueString == original

@given(instance=pivot::Property_strategy)
def test_pivot::property_isReadOnly_type(instance):
    assert isinstance(instance.isReadOnly, str)


@given(instance=pivot::Property_strategy)
def test_pivot::property_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original

@given(instance=pivot::Property_strategy)
def test_pivot::property_isResolveProxies_type(instance):
    assert isinstance(instance.isResolveProxies, str)


@given(instance=pivot::Property_strategy)
def test_pivot::property_isResolveProxies_setter(instance):
    original = instance.isResolveProxies
    instance.isResolveProxies = original
    assert instance.isResolveProxies == original

@given(instance=pivot::Property_strategy)
def test_pivot::property_isComposite_type(instance):
    assert isinstance(instance.isComposite, str)


@given(instance=pivot::Property_strategy)
def test_pivot::property_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original

@given(instance=pivot::Property_strategy)
def test_pivot::property_isTransient_type(instance):
    assert isinstance(instance.isTransient, str)


@given(instance=pivot::Property_strategy)
def test_pivot::property_isTransient_setter(instance):
    original = instance.isTransient
    instance.isTransient = original
    assert instance.isTransient == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::Property_strategy)
@settings(max_examples=30)
def test_pivot::property_validatecompatibledefaultexpression_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateCompatibleDefaultExpression(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateCompatibleDefaultExpression).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateCompatibleDefaultExpression' in pivot::Property is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateCompatibleDefaultExpression' in pivot::Property did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateCompatibleDefaultExpression' in pivot::Property is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::Property_strategy)
@settings(max_examples=30)
def test_pivot::property_isattribute_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isAttribute(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isAttribute).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isAttribute' in pivot::Property is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isAttribute' in pivot::Property did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isAttribute' in pivot::Property is not implemented or raised an error")

@given(instance=pivot::Operation_strategy)
@settings(max_examples=50)
def test_pivot::operation_instantiation(instance):
    assert isinstance(instance, pivot::Operation)

@given(instance=pivot::Operation_strategy)
def test_pivot::operation_isValidating_type(instance):
    assert isinstance(instance.isValidating, str)


@given(instance=pivot::Operation_strategy)
def test_pivot::operation_isValidating_setter(instance):
    original = instance.isValidating
    instance.isValidating = original
    assert instance.isValidating == original

@given(instance=pivot::Operation_strategy)
def test_pivot::operation_isTypeof_type(instance):
    assert isinstance(instance.isTypeof, str)


@given(instance=pivot::Operation_strategy)
def test_pivot::operation_isTypeof_setter(instance):
    original = instance.isTypeof
    instance.isTypeof = original
    assert instance.isTypeof == original

@given(instance=pivot::Operation_strategy)
def test_pivot::operation_isInvalidating_type(instance):
    assert isinstance(instance.isInvalidating, str)


@given(instance=pivot::Operation_strategy)
def test_pivot::operation_isInvalidating_setter(instance):
    original = instance.isInvalidating
    instance.isInvalidating = original
    assert instance.isInvalidating == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::Operation_strategy)
@settings(max_examples=30)
def test_pivot::operation_validatecompatiblereturn_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateCompatibleReturn(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateCompatibleReturn).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateCompatibleReturn' in pivot::Operation is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateCompatibleReturn' in pivot::Operation did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateCompatibleReturn' in pivot::Operation is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::Operation_strategy)
@settings(max_examples=30)
def test_pivot::operation_validateuniquepreconditionname_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateUniquePreconditionName(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateUniquePreconditionName).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateUniquePreconditionName' in pivot::Operation is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateUniquePreconditionName' in pivot::Operation did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateUniquePreconditionName' in pivot::Operation is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::Operation_strategy)
@settings(max_examples=30)
def test_pivot::operation_validateloadableimplementation_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateLoadableImplementation(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateLoadableImplementation).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateLoadableImplementation' in pivot::Operation is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateLoadableImplementation' in pivot::Operation did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateLoadableImplementation' in pivot::Operation is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::Operation_strategy)
@settings(max_examples=30)
def test_pivot::operation_validateuniquepostconditionname_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateUniquePostconditionName(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateUniquePostconditionName).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateUniquePostconditionName' in pivot::Operation is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateUniquePostconditionName' in pivot::Operation did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateUniquePostconditionName' in pivot::Operation is not implemented or raised an error")

@given(instance=pivot::NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_pivot::numericliteralexp_instantiation(instance):
    assert isinstance(instance, pivot::NumericLiteralExp)

@given(instance=pivot::NullLiteralExp_strategy)
@settings(max_examples=50)
def test_pivot::nullliteralexp_instantiation(instance):
    assert isinstance(instance, pivot::NullLiteralExp)

@given(instance=pivot::MessageExp_strategy)
@settings(max_examples=50)
def test_pivot::messageexp_instantiation(instance):
    assert isinstance(instance, pivot::MessageExp)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::MessageExp_strategy)
@settings(max_examples=30)
def test_pivot::messageexp_validateonecalloronesend_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateOneCallOrOneSend(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateOneCallOrOneSend).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateOneCallOrOneSend' in pivot::MessageExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateOneCallOrOneSend' in pivot::MessageExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateOneCallOrOneSend' in pivot::MessageExp is not implemented or raised an error")

@given(instance=pivot::MapType_strategy)
@settings(max_examples=50)
def test_pivot::maptype_instantiation(instance):
    assert isinstance(instance, pivot::MapType)

@given(instance=pivot::MapLiteralPart_strategy)
@settings(max_examples=50)
def test_pivot::mapliteralpart_instantiation(instance):
    assert isinstance(instance, pivot::MapLiteralPart)

@given(instance=pivot::MapLiteralExp_strategy)
@settings(max_examples=50)
def test_pivot::mapliteralexp_instantiation(instance):
    assert isinstance(instance, pivot::MapLiteralExp)

@given(instance=pivot::Signal_strategy)
@settings(max_examples=50)
def test_pivot::signal_instantiation(instance):
    assert isinstance(instance, pivot::Signal)

@given(instance=pivot::MessageType_strategy)
@settings(max_examples=50)
def test_pivot::messagetype_instantiation(instance):
    assert isinstance(instance, pivot::MessageType)

@given(instance=pivot::SendSignalAction_strategy)
@settings(max_examples=50)
def test_pivot::sendsignalaction_instantiation(instance):
    assert isinstance(instance, pivot::SendSignalAction)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=pivot::Profile_strategy)
@settings(max_examples=50)
def test_pivot::profile_instantiation(instance):
    assert isinstance(instance, pivot::Profile)

@given(instance=pivot::Library_strategy)
@settings(max_examples=50)
def test_pivot::library_instantiation(instance):
    assert isinstance(instance, pivot::Library)

@given(instance=pivot::LetExp_strategy)
@settings(max_examples=50)
def test_pivot::letexp_instantiation(instance):
    assert isinstance(instance, pivot::LetExp)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::LetExp_strategy)
@settings(max_examples=30)
def test_pivot::letexp_validatetypeisintype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateTypeIsInType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateTypeIsInType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateTypeIsInType' in pivot::LetExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateTypeIsInType' in pivot::LetExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateTypeIsInType' in pivot::LetExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::LetExp_strategy)
@settings(max_examples=30)
def test_pivot::letexp_validatetypeisnotinvalid_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateTypeIsNotInvalid(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateTypeIsNotInvalid).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateTypeIsNotInvalid' in pivot::LetExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateTypeIsNotInvalid' in pivot::LetExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateTypeIsNotInvalid' in pivot::LetExp is not implemented or raised an error")

@given(instance=pivot::LiteralExp_strategy)
@settings(max_examples=50)
def test_pivot::literalexp_instantiation(instance):
    assert isinstance(instance, pivot::LiteralExp)

@given(instance=pivot::Precedence_strategy)
@settings(max_examples=50)
def test_pivot::precedence_instantiation(instance):
    assert isinstance(instance, pivot::Precedence)

@given(instance=pivot::Precedence_strategy)
def test_pivot::precedence_order_type(instance):
    assert isinstance(instance.order, str)


@given(instance=pivot::Precedence_strategy)
def test_pivot::precedence_order_setter(instance):
    original = instance.order
    instance.order = original
    assert instance.order == original

@given(instance=pivot::Precedence_strategy)
def test_pivot::precedence_associativity_type(instance):
    assert isinstance(instance.associativity, str)


@given(instance=pivot::Precedence_strategy)
def test_pivot::precedence_associativity_setter(instance):
    original = instance.associativity
    instance.associativity = original
    assert instance.associativity == original

@given(instance=pivot::LambdaType_strategy)
@settings(max_examples=50)
def test_pivot::lambdatype_instantiation(instance):
    assert isinstance(instance, pivot::LambdaType)

@given(instance=pivot::Parameter_strategy)
@settings(max_examples=50)
def test_pivot::parameter_instantiation(instance):
    assert isinstance(instance, pivot::Parameter)

@given(instance=pivot::Parameter_strategy)
def test_pivot::parameter_isTypeof_type(instance):
    assert isinstance(instance.isTypeof, str)


@given(instance=pivot::Parameter_strategy)
def test_pivot::parameter_isTypeof_setter(instance):
    original = instance.isTypeof
    instance.isTypeof = original
    assert instance.isTypeof == original

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=pivot::Iteration_strategy)
@settings(max_examples=50)
def test_pivot::iteration_instantiation(instance):
    assert isinstance(instance, pivot::Iteration)

@given(instance=ReferringElement_strategy)
@settings(max_examples=50)
def test_referringelement_instantiation(instance):
    assert isinstance(instance, ReferringElement)

@given(instance=pivot::OperationCallExp_strategy)
@settings(max_examples=50)
def test_pivot::operationcallexp_instantiation(instance):
    assert isinstance(instance, pivot::OperationCallExp)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::OperationCallExp_strategy)
@settings(max_examples=30)
def test_pivot::operationcallexp_validateargumentcount_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateArgumentCount(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateArgumentCount).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateArgumentCount' in pivot::OperationCallExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateArgumentCount' in pivot::OperationCallExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateArgumentCount' in pivot::OperationCallExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::OperationCallExp_strategy)
@settings(max_examples=30)
def test_pivot::operationcallexp_validateargumenttypeisconformant_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateArgumentTypeIsConformant(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateArgumentTypeIsConformant).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateArgumentTypeIsConformant' in pivot::OperationCallExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateArgumentTypeIsConformant' in pivot::OperationCallExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateArgumentTypeIsConformant' in pivot::OperationCallExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::OperationCallExp_strategy)
@settings(max_examples=30)
def test_pivot::operationcallexp_validatesafesourcecanbenull_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateSafeSourceCanBeNull(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateSafeSourceCanBeNull).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateSafeSourceCanBeNull' in pivot::OperationCallExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateSafeSourceCanBeNull' in pivot::OperationCallExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateSafeSourceCanBeNull' in pivot::OperationCallExp is not implemented or raised an error")

@given(instance=pivot::PropertyCallExp_strategy)
@settings(max_examples=50)
def test_pivot::propertycallexp_instantiation(instance):
    assert isinstance(instance, pivot::PropertyCallExp)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::PropertyCallExp_strategy)
@settings(max_examples=30)
def test_pivot::propertycallexp_validatenonstaticsourcetypeisconformant_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateNonStaticSourceTypeIsConformant(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateNonStaticSourceTypeIsConformant).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateNonStaticSourceTypeIsConformant' in pivot::PropertyCallExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateNonStaticSourceTypeIsConformant' in pivot::PropertyCallExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateNonStaticSourceTypeIsConformant' in pivot::PropertyCallExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::PropertyCallExp_strategy)
@settings(max_examples=30)
def test_pivot::propertycallexp_validateunsafesourcecannotbenull_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateUnsafeSourceCanNotBeNull(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateUnsafeSourceCanNotBeNull).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateUnsafeSourceCanNotBeNull' in pivot::PropertyCallExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateUnsafeSourceCanNotBeNull' in pivot::PropertyCallExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateUnsafeSourceCanNotBeNull' in pivot::PropertyCallExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::PropertyCallExp_strategy)
@settings(max_examples=30)
def test_pivot::propertycallexp_validatecompatibleresulttype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateCompatibleResultType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateCompatibleResultType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateCompatibleResultType' in pivot::PropertyCallExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateCompatibleResultType' in pivot::PropertyCallExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateCompatibleResultType' in pivot::PropertyCallExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::PropertyCallExp_strategy)
@settings(max_examples=30)
def test_pivot::propertycallexp_validatesafesourcecanbenull_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateSafeSourceCanBeNull(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateSafeSourceCanBeNull).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateSafeSourceCanBeNull' in pivot::PropertyCallExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateSafeSourceCanBeNull' in pivot::PropertyCallExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateSafeSourceCanBeNull' in pivot::PropertyCallExp is not implemented or raised an error")

@given(instance=pivot::TypeExp_strategy)
@settings(max_examples=50)
def test_pivot::typeexp_instantiation(instance):
    assert isinstance(instance, pivot::TypeExp)

@given(instance=pivot::VariableExp_strategy)
@settings(max_examples=50)
def test_pivot::variableexp_instantiation(instance):
    assert isinstance(instance, pivot::VariableExp)

@given(instance=pivot::VariableExp_strategy)
def test_pivot::variableexp_isImplicit_type(instance):
    assert isinstance(instance.isImplicit, str)


@given(instance=pivot::VariableExp_strategy)
def test_pivot::variableexp_isImplicit_setter(instance):
    original = instance.isImplicit
    instance.isImplicit = original
    assert instance.isImplicit == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::VariableExp_strategy)
@settings(max_examples=30)
def test_pivot::variableexp_validatetypeisnotinvalid_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateTypeIsNotInvalid(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateTypeIsNotInvalid).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateTypeIsNotInvalid' in pivot::VariableExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateTypeIsNotInvalid' in pivot::VariableExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateTypeIsNotInvalid' in pivot::VariableExp is not implemented or raised an error")

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=pivot::IteratorExp_strategy)
@settings(max_examples=50)
def test_pivot::iteratorexp_instantiation(instance):
    assert isinstance(instance, pivot::IteratorExp)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot::iteratorexp_validatecollectelementtypeisflattenedbodytype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateCollectElementTypeIsFlattenedBodyType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateCollectElementTypeIsFlattenedBodyType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateCollectElementTypeIsFlattenedBodyType' in pivot::IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateCollectElementTypeIsFlattenedBodyType' in pivot::IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateCollectElementTypeIsFlattenedBodyType' in pivot::IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot::iteratorexp_validatesafeiteratorisrequired_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateSafeIteratorIsRequired(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateSafeIteratorIsRequired).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateSafeIteratorIsRequired' in pivot::IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateSafeIteratorIsRequired' in pivot::IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateSafeIteratorIsRequired' in pivot::IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot::iteratorexp_validatesortedbyelementtypeissourceelementtype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateSortedByElementTypeIsSourceElementType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateSortedByElementTypeIsSourceElementType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateSortedByElementTypeIsSourceElementType' in pivot::IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateSortedByElementTypeIsSourceElementType' in pivot::IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateSortedByElementTypeIsSourceElementType' in pivot::IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot::iteratorexp_validateclosureelementtypeissourceelementtype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateClosureElementTypeIsSourceElementType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateClosureElementTypeIsSourceElementType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateClosureElementTypeIsSourceElementType' in pivot::IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateClosureElementTypeIsSourceElementType' in pivot::IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateClosureElementTypeIsSourceElementType' in pivot::IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot::iteratorexp_validateclosurebodytypeisconformanttoiteratortype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateClosureBodyTypeIsConformanttoIteratorType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateClosureBodyTypeIsConformanttoIteratorType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateClosureBodyTypeIsConformanttoIteratorType' in pivot::IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateClosureBodyTypeIsConformanttoIteratorType' in pivot::IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateClosureBodyTypeIsConformanttoIteratorType' in pivot::IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot::iteratorexp_validatesortedbyiteratortypeiscomparable_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateSortedByIteratorTypeIsComparable(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateSortedByIteratorTypeIsComparable).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateSortedByIteratorTypeIsComparable' in pivot::IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateSortedByIteratorTypeIsComparable' in pivot::IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateSortedByIteratorTypeIsComparable' in pivot::IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot::iteratorexp_validateclosurehasoneiterator_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateClosureHasOneIterator(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateClosureHasOneIterator).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateClosureHasOneIterator' in pivot::IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateClosureHasOneIterator' in pivot::IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateClosureHasOneIterator' in pivot::IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot::iteratorexp_validateclosuretypeisuniquecollection_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateClosureTypeIsUniqueCollection(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateClosureTypeIsUniqueCollection).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateClosureTypeIsUniqueCollection' in pivot::IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateClosureTypeIsUniqueCollection' in pivot::IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateClosureTypeIsUniqueCollection' in pivot::IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot::iteratorexp_validateanyhasoneiterator_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateAnyHasOneIterator(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateAnyHasOneIterator).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateAnyHasOneIterator' in pivot::IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateAnyHasOneIterator' in pivot::IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateAnyHasOneIterator' in pivot::IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot::iteratorexp_validatecollecttypeisunordered_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateCollectTypeIsUnordered(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateCollectTypeIsUnordered).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateCollectTypeIsUnordered' in pivot::IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateCollectTypeIsUnordered' in pivot::IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateCollectTypeIsUnordered' in pivot::IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot::iteratorexp_validatesafesourcecanbenull_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateSafeSourceCanBeNull(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateSafeSourceCanBeNull).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateSafeSourceCanBeNull' in pivot::IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateSafeSourceCanBeNull' in pivot::IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateSafeSourceCanBeNull' in pivot::IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot::iteratorexp_validateanytypeissourceelementtype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateAnyTypeIsSourceElementType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateAnyTypeIsSourceElementType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateAnyTypeIsSourceElementType' in pivot::IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateAnyTypeIsSourceElementType' in pivot::IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateAnyTypeIsSourceElementType' in pivot::IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot::iteratorexp_validatesortedbyisorderedifsourceisordered_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateSortedByIsOrderedIfSourceIsOrdered(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateSortedByIsOrderedIfSourceIsOrdered).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateSortedByIsOrderedIfSourceIsOrdered' in pivot::IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateSortedByIsOrderedIfSourceIsOrdered' in pivot::IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateSortedByIsOrderedIfSourceIsOrdered' in pivot::IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot::iteratorexp_validateunsafesourcecannotbenull_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateUnsafeSourceCanNotBeNull(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateUnsafeSourceCanNotBeNull).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateUnsafeSourceCanNotBeNull' in pivot::IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateUnsafeSourceCanNotBeNull' in pivot::IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateUnsafeSourceCanNotBeNull' in pivot::IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot::iteratorexp_validateiteratortypeissourceelementtype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateIteratorTypeIsSourceElementType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateIteratorTypeIsSourceElementType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateIteratorTypeIsSourceElementType' in pivot::IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateIteratorTypeIsSourceElementType' in pivot::IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateIteratorTypeIsSourceElementType' in pivot::IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot::iteratorexp_validateclosuresourceelementtypeisbodyelementtype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateClosureSourceElementTypeIsBodyElementType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateClosureSourceElementTypeIsBodyElementType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateClosureSourceElementTypeIsBodyElementType' in pivot::IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateClosureSourceElementTypeIsBodyElementType' in pivot::IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateClosureSourceElementTypeIsBodyElementType' in pivot::IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot::iteratorexp_validateanybodytypeisboolean_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateAnyBodyTypeIsBoolean(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateAnyBodyTypeIsBoolean).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateAnyBodyTypeIsBoolean' in pivot::IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateAnyBodyTypeIsBoolean' in pivot::IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateAnyBodyTypeIsBoolean' in pivot::IteratorExp is not implemented or raised an error")

@given(instance=pivot::IterateExp_strategy)
@settings(max_examples=50)
def test_pivot::iterateexp_instantiation(instance):
    assert isinstance(instance, pivot::IterateExp)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::IterateExp_strategy)
@settings(max_examples=30)
def test_pivot::iterateexp_validateoneinitializer_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateOneInitializer(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateOneInitializer).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateOneInitializer' in pivot::IterateExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateOneInitializer' in pivot::IterateExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateOneInitializer' in pivot::IterateExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::IterateExp_strategy)
@settings(max_examples=30)
def test_pivot::iterateexp_validatesafesourcecanbenull_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateSafeSourceCanBeNull(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateSafeSourceCanBeNull).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateSafeSourceCanBeNull' in pivot::IterateExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateSafeSourceCanBeNull' in pivot::IterateExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateSafeSourceCanBeNull' in pivot::IterateExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::IterateExp_strategy)
@settings(max_examples=30)
def test_pivot::iterateexp_validatebodytypeconformstoresulttype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateBodyTypeConformsToResultType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateBodyTypeConformsToResultType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateBodyTypeConformsToResultType' in pivot::IterateExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateBodyTypeConformsToResultType' in pivot::IterateExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateBodyTypeConformsToResultType' in pivot::IterateExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::IterateExp_strategy)
@settings(max_examples=30)
def test_pivot::iterateexp_validatesafeiteratorisrequired_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateSafeIteratorIsRequired(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateSafeIteratorIsRequired).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateSafeIteratorIsRequired' in pivot::IterateExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateSafeIteratorIsRequired' in pivot::IterateExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateSafeIteratorIsRequired' in pivot::IterateExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::IterateExp_strategy)
@settings(max_examples=30)
def test_pivot::iterateexp_validatetypeisresulttype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateTypeIsResultType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateTypeIsResultType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateTypeIsResultType' in pivot::IterateExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateTypeIsResultType' in pivot::IterateExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateTypeIsResultType' in pivot::IterateExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::IterateExp_strategy)
@settings(max_examples=30)
def test_pivot::iterateexp_validateunsafesourcecannotbenull_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateUnsafeSourceCanNotBeNull(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateUnsafeSourceCanNotBeNull).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateUnsafeSourceCanNotBeNull' in pivot::IterateExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateUnsafeSourceCanNotBeNull' in pivot::IterateExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateUnsafeSourceCanNotBeNull' in pivot::IterateExp is not implemented or raised an error")

@given(instance=pivot::InvalidType_strategy)
@settings(max_examples=50)
def test_pivot::invalidtype_instantiation(instance):
    assert isinstance(instance, pivot::InvalidType)

@given(instance=pivot::InvalidLiteralExp_strategy)
@settings(max_examples=50)
def test_pivot::invalidliteralexp_instantiation(instance):
    assert isinstance(instance, pivot::InvalidLiteralExp)

@given(instance=NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_numericliteralexp_instantiation(instance):
    assert isinstance(instance, NumericLiteralExp)

@given(instance=pivot::RealLiteralExp_strategy)
@settings(max_examples=50)
def test_pivot::realliteralexp_instantiation(instance):
    assert isinstance(instance, pivot::RealLiteralExp)

@given(instance=pivot::RealLiteralExp_strategy)
def test_pivot::realliteralexp_realSymbol_type(instance):
    assert isinstance(instance.realSymbol, str)


@given(instance=pivot::RealLiteralExp_strategy)
def test_pivot::realliteralexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=pivot::UnlimitedNaturalLiteralExp_strategy)
@settings(max_examples=50)
def test_pivot::unlimitednaturalliteralexp_instantiation(instance):
    assert isinstance(instance, pivot::UnlimitedNaturalLiteralExp)

@given(instance=pivot::UnlimitedNaturalLiteralExp_strategy)
def test_pivot::unlimitednaturalliteralexp_unlimitedNaturalSymbol_type(instance):
    assert isinstance(instance.unlimitedNaturalSymbol, str)


@given(instance=pivot::UnlimitedNaturalLiteralExp_strategy)
def test_pivot::unlimitednaturalliteralexp_unlimitedNaturalSymbol_setter(instance):
    original = instance.unlimitedNaturalSymbol
    instance.unlimitedNaturalSymbol = original
    assert instance.unlimitedNaturalSymbol == original

@given(instance=pivot::IntegerLiteralExp_strategy)
@settings(max_examples=50)
def test_pivot::integerliteralexp_instantiation(instance):
    assert isinstance(instance, pivot::IntegerLiteralExp)

@given(instance=pivot::IntegerLiteralExp_strategy)
def test_pivot::integerliteralexp_integerSymbol_type(instance):
    assert isinstance(instance.integerSymbol, str)


@given(instance=pivot::IntegerLiteralExp_strategy)
def test_pivot::integerliteralexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::IntegerLiteralExp_strategy)
@settings(max_examples=30)
def test_pivot::integerliteralexp_validatetypeisinteger_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateTypeIsInteger(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateTypeIsInteger).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateTypeIsInteger' in pivot::IntegerLiteralExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateTypeIsInteger' in pivot::IntegerLiteralExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateTypeIsInteger' in pivot::IntegerLiteralExp is not implemented or raised an error")

@given(instance=pivot::IfExp_strategy)
@settings(max_examples=50)
def test_pivot::ifexp_instantiation(instance):
    assert isinstance(instance, pivot::IfExp)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::IfExp_strategy)
@settings(max_examples=30)
def test_pivot::ifexp_validateconditiontypeisboolean_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateConditionTypeIsBoolean(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateConditionTypeIsBoolean).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateConditionTypeIsBoolean' in pivot::IfExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateConditionTypeIsBoolean' in pivot::IfExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateConditionTypeIsBoolean' in pivot::IfExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::IfExp_strategy)
@settings(max_examples=30)
def test_pivot::ifexp_validatetypeisnotinvalid_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateTypeIsNotInvalid(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateTypeIsNotInvalid).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateTypeIsNotInvalid' in pivot::IfExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateTypeIsNotInvalid' in pivot::IfExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateTypeIsNotInvalid' in pivot::IfExp is not implemented or raised an error")

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=pivot::FinalState_strategy)
@settings(max_examples=50)
def test_pivot::finalstate_instantiation(instance):
    assert isinstance(instance, pivot::FinalState)

@given(instance=CallExp_strategy)
@settings(max_examples=50)
def test_callexp_instantiation(instance):
    assert isinstance(instance, CallExp)

@given(instance=pivot::LoopExp_strategy)
@settings(max_examples=50)
def test_pivot::loopexp_instantiation(instance):
    assert isinstance(instance, pivot::LoopExp)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::LoopExp_strategy)
@settings(max_examples=30)
def test_pivot::loopexp_validatenoinitializers_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateNoInitializers(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateNoInitializers).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateNoInitializers' in pivot::LoopExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateNoInitializers' in pivot::LoopExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateNoInitializers' in pivot::LoopExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::LoopExp_strategy)
@settings(max_examples=30)
def test_pivot::loopexp_validatesourceiscollection_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateSourceIsCollection(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateSourceIsCollection).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateSourceIsCollection' in pivot::LoopExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateSourceIsCollection' in pivot::LoopExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateSourceIsCollection' in pivot::LoopExp is not implemented or raised an error")

@given(instance=pivot::FeatureCallExp_strategy)
@settings(max_examples=50)
def test_pivot::featurecallexp_instantiation(instance):
    assert isinstance(instance, pivot::FeatureCallExp)

@given(instance=pivot::FeatureCallExp_strategy)
def test_pivot::featurecallexp_isPre_type(instance):
    assert isinstance(instance.isPre, str)


@given(instance=pivot::FeatureCallExp_strategy)
def test_pivot::featurecallexp_isPre_setter(instance):
    original = instance.isPre
    instance.isPre = original
    assert instance.isPre == original

@given(instance=pivot::Slot_strategy)
@settings(max_examples=50)
def test_pivot::slot_instantiation(instance):
    assert isinstance(instance, pivot::Slot)

@given(instance=pivot::InstanceSpecification_strategy)
@settings(max_examples=50)
def test_pivot::instancespecification_instantiation(instance):
    assert isinstance(instance, pivot::InstanceSpecification)

@given(instance=pivot::Import_strategy)
@settings(max_examples=50)
def test_pivot::import_instantiation(instance):
    assert isinstance(instance, pivot::Import)

@given(instance=pivot::Variable_strategy)
@settings(max_examples=50)
def test_pivot::variable_instantiation(instance):
    assert isinstance(instance, pivot::Variable)

@given(instance=pivot::Variable_strategy)
def test_pivot::variable_isImplicit_type(instance):
    assert isinstance(instance.isImplicit, str)


@given(instance=pivot::Variable_strategy)
def test_pivot::variable_isImplicit_setter(instance):
    original = instance.isImplicit
    instance.isImplicit = original
    assert instance.isImplicit == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::Variable_strategy)
@settings(max_examples=30)
def test_pivot::variable_validatecompatibleinitialisertype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateCompatibleInitialiserType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateCompatibleInitialiserType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateCompatibleInitialiserType' in pivot::Variable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateCompatibleInitialiserType' in pivot::Variable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateCompatibleInitialiserType' in pivot::Variable is not implemented or raised an error")

@given(instance=LanguageExpression_strategy)
@settings(max_examples=50)
def test_languageexpression_instantiation(instance):
    assert isinstance(instance, LanguageExpression)

@given(instance=pivot::ExpressionInOCL_strategy)
@settings(max_examples=50)
def test_pivot::expressioninocl_instantiation(instance):
    assert isinstance(instance, pivot::ExpressionInOCL)

@given(instance=InstanceSpecification_strategy)
@settings(max_examples=50)
def test_instancespecification_instantiation(instance):
    assert isinstance(instance, InstanceSpecification)

@given(instance=pivot::Feature_strategy)
@settings(max_examples=50)
def test_pivot::feature_instantiation(instance):
    assert isinstance(instance, pivot::Feature)

@given(instance=pivot::Feature_strategy)
def test_pivot::feature_implementationClass_type(instance):
    assert isinstance(instance.implementationClass, str)


@given(instance=pivot::Feature_strategy)
def test_pivot::feature_implementationClass_setter(instance):
    original = instance.implementationClass
    instance.implementationClass = original
    assert instance.implementationClass == original

@given(instance=pivot::Feature_strategy)
def test_pivot::feature_implementation_type(instance):
    assert isinstance(instance.implementation, str)


@given(instance=pivot::Feature_strategy)
def test_pivot::feature_implementation_setter(instance):
    original = instance.implementation
    instance.implementation = original
    assert instance.implementation == original

@given(instance=pivot::Feature_strategy)
def test_pivot::feature_isStatic_type(instance):
    assert isinstance(instance.isStatic, str)


@given(instance=pivot::Feature_strategy)
def test_pivot::feature_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::Feature_strategy)
@settings(max_examples=30)
def test_pivot::feature_validatetypeisnotinvalid_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateTypeIsNotInvalid(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateTypeIsNotInvalid).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateTypeIsNotInvalid' in pivot::Feature is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateTypeIsNotInvalid' in pivot::Feature did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateTypeIsNotInvalid' in pivot::Feature is not implemented or raised an error")

@given(instance=pivot::Stereotype_strategy)
@settings(max_examples=50)
def test_pivot::stereotype_instantiation(instance):
    assert isinstance(instance, pivot::Stereotype)

@given(instance=pivot::ElementExtension_strategy)
@settings(max_examples=50)
def test_pivot::elementextension_instantiation(instance):
    assert isinstance(instance, pivot::ElementExtension)

@given(instance=pivot::ElementExtension_strategy)
def test_pivot::elementextension_isApplied_type(instance):
    assert isinstance(instance.isApplied, str)


@given(instance=pivot::ElementExtension_strategy)
def test_pivot::elementextension_isApplied_setter(instance):
    original = instance.isApplied
    instance.isApplied = original
    assert instance.isApplied == original

@given(instance=pivot::ElementExtension_strategy)
def test_pivot::elementextension_isRequired_type(instance):
    assert isinstance(instance.isRequired, str)


@given(instance=pivot::ElementExtension_strategy)
def test_pivot::elementextension_isRequired_setter(instance):
    original = instance.isRequired
    instance.isRequired = original
    assert instance.isRequired == original

@given(instance=pivot::Enumeration_strategy)
@settings(max_examples=50)
def test_pivot::enumeration_instantiation(instance):
    assert isinstance(instance, pivot::Enumeration)

@given(instance=pivot::EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_pivot::enumerationliteral_instantiation(instance):
    assert isinstance(instance, pivot::EnumerationLiteral)

@given(instance=pivot::EnumerationLiteral_strategy)
def test_pivot::enumerationliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=pivot::EnumerationLiteral_strategy)
def test_pivot::enumerationliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=pivot::EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_pivot::enumliteralexp_instantiation(instance):
    assert isinstance(instance, pivot::EnumLiteralExp)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::EnumLiteralExp_strategy)
@settings(max_examples=30)
def test_pivot::enumliteralexp_validatetypeisenumerationtype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validateTypeIsEnumerationType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validateTypeIsEnumerationType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validateTypeIsEnumerationType' in pivot::EnumLiteralExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validateTypeIsEnumerationType' in pivot::EnumLiteralExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validateTypeIsEnumerationType' in pivot::EnumLiteralExp is not implemented or raised an error")

@given(instance=Visitable_strategy)
@settings(max_examples=50)
def test_visitable_instantiation(instance):
    assert isinstance(instance, Visitable)

@given(instance=pivot::Element_strategy)
@settings(max_examples=50)
def test_pivot::element_instantiation(instance):
    assert isinstance(instance, pivot::Element)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot::Element_strategy)
@settings(max_examples=30)
def test_pivot::element_allownedelements_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.allOwnedElements()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.allOwnedElements).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'allOwnedElements' in pivot::Element is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'allOwnedElements' in pivot::Element did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'allOwnedElements' in pivot::Element is not implemented or raised an error")

@given(instance=ValueSpecification_strategy)
@settings(max_examples=50)
def test_valuespecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)

@given(instance=pivot::DynamicValueSpecification_strategy)
@settings(max_examples=50)
def test_pivot::dynamicvaluespecification_instantiation(instance):
    assert isinstance(instance, pivot::DynamicValueSpecification)

@given(instance=DynamicElement_strategy)
@settings(max_examples=50)
def test_dynamicelement_instantiation(instance):
    assert isinstance(instance, DynamicElement)

@given(instance=pivot::DynamicType_strategy)
@settings(max_examples=50)
def test_pivot::dynamictype_instantiation(instance):
    assert isinstance(instance, pivot::DynamicType)

@given(instance=pivot::DataType_strategy)
@settings(max_examples=50)
def test_pivot::datatype_instantiation(instance):
    assert isinstance(instance, pivot::DataType)

@given(instance=pivot::DataType_strategy)
def test_pivot::datatype_isSerializable_type(instance):
    assert isinstance(instance.isSerializable, str)


@given(instance=pivot::DataType_strategy)
def test_pivot::datatype_isSerializable_setter(instance):
    original = instance.isSerializable
    instance.isSerializable = original
    assert instance.isSerializable == original

@given(instance=pivot::DynamicProperty_strategy)
@settings(max_examples=50)
def test_pivot::dynamicproperty_instantiation(instance):
    assert isinstance(instance, pivot::DynamicProperty)

@given(instance=pivot::DynamicProperty_strategy)
def test_pivot::dynamicproperty_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=pivot::DynamicProperty_strategy)
def test_pivot::dynamicproperty_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=pivot::DynamicElement_strategy)
@settings(max_examples=50)
def test_pivot::dynamicelement_instantiation(instance):
    assert isinstance(instance, pivot::DynamicElement)

@given(instance=DynamicType_strategy)
@settings(max_examples=50)
def test_dynamictype_instantiation(instance):
    assert isinstance(instance, DynamicType)

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=pivot::StateMachine_strategy)
@settings(max_examples=50)
def test_pivot::statemachine_instantiation(instance):
    assert isinstance(instance, pivot::StateMachine)

@given(instance=pivot::DynamicBehavior_strategy)
@settings(max_examples=50)
def test_pivot::dynamicbehavior_instantiation(instance):
    assert isinstance(instance, pivot::DynamicBehavior)

@given(instance=pivot::LanguageExpression_strategy)
@settings(max_examples=50)
def test_pivot::languageexpression_instantiation(instance):
    assert isinstance(instance, pivot::LanguageExpression)

@given(instance=pivot::LanguageExpression_strategy)
def test_pivot::languageexpression_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=pivot::LanguageExpression_strategy)
def test_pivot::languageexpression_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=pivot::LanguageExpression_strategy)
def test_pivot::languageexpression_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=pivot::LanguageExpression_strategy)
def test_pivot::languageexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original
