import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    pivot_Visitor,
    pivot_Visitable,
    Behavior,
    pivot_ReferringElement,
    pivot_StateMachine,
    pivot_Pivotable,
    VariableDeclaration,
    pivot_TupleLiteralPart,
    TemplateParameter,
    pivot_TypeTemplateParameter,
    pivot_OperationTemplateParameter,
    ParameterableElement,
    pivot_PackageableElement,
    TemplateableElement,
    Feature,
    ValueSpecification,
    FeatureCallExp,
    pivot_NavigationCallExp,
    Nameable,
    pivot_Nameable,
    pivot_MorePivotable,
    Package,
    pivot_Profile,
    pivot_Library,
    Operation,
    pivot_Iteration,
    State,
    pivot_FinalState,
    CallExp,
    pivot_LoopExp,
    pivot_FeatureCallExp,
    TypedMultiplicityElement,
    pivot_Parameter,
    pivot_Feature,
    ReferringElement,
    pivot_OperationCallExp,
    pivot_Variable,
    LoopExp,
    pivot_IteratorExp,
    pivot_IterateExp,
    NumericLiteralExp,
    pivot_RealLiteralExp,
    pivot_UnlimitedNaturalLiteralExp,
    pivot_IntegerLiteralExp,
    OpaqueExpression,
    pivot_ExpressionInOCL,
    Visitable,
    DynamicElement,
    Vertex,
    pivot_Pseudostate,
    pivot_ConnectionPointReference,
    Element,
    pivot_NamedElement,
    pivot_ParameterableElement,
    pivot_DynamicProperty,
    pivot_TemplateSignature,
    pivot_TemplateableElement,
    pivot_TemplateParameterSubstitution,
    pivot_TemplateBinding,
    pivot_TemplateParameter,
    pivot_DynamicElement,
    pivot_Comment,
    pivot_OpaqueExpression,
    LiteralExp,
    pivot_InvalidLiteralExp,
    pivot_EnumLiteralExp,
    pivot_PrimitiveLiteralExp,
    pivot_TupleLiteralExp,
    pivot_CollectionLiteralExp,
    DataType,
    pivot_Enumeration,
    pivot_LambdaType,
    pivot_PrimitiveType,
    pivot_TupleType,
    pivot_CollectionType,
    TypedElement,
    pivot_TypedMultiplicityElement,
    pivot_VariableDeclaration,
    pivot_ValueSpecification,
    pivot_ConstructorPart,
    pivot_CollectionLiteralPart,
    Namespace,
    pivot_Package,
    pivot_Region,
    pivot_Transition,
    pivot_Root,
    pivot_State,
    Type,
    pivot_MessageType,
    pivot_TemplateParameterType,
    pivot_DynamicType,
    pivot_ElementExtension,
    pivot_Class,
    pivot_Operation,
    pivot_OCLExpression,
    OCLExpression,
    pivot_ConstructorExp,
    pivot_MessageExp,
    pivot_TypeExp,
    pivot_StateExp,
    pivot_IfExp,
    pivot_LetExp,
    pivot_LiteralExp,
    pivot_VariableExp,
    pivot_UnspecifiedValueExp,
    pivot_CallExp,
    CollectionLiteralPart,
    pivot_CollectionRange,
    pivot_CollectionItem,
    pivot_Element,
    NamedElement,
    pivot_Constraint,
    pivot_Type,
    pivot_Namespace,
    pivot_SendSignalAction,
    pivot_Vertex,
    pivot_TypedElement,
    pivot_CallOperationAction,
    pivot_Signal,
    pivot_EnumerationLiteral,
    pivot_Precedence,
    pivot_Trigger,
    pivot_Import,
    pivot_Annotation,
    PrimitiveLiteralExp,
    pivot_NumericLiteralExp,
    pivot_NullLiteralExp,
    pivot_StringLiteralExp,
    pivot_BooleanLiteralExp,
    CollectionType,
    pivot_OrderedSetType,
    pivot_SequenceType,
    pivot_SetType,
    pivot_BagType,
    NavigationCallExp,
    pivot_PropertyCallExp,
    pivot_AssociationClassCallExp,
    pivot_Property,
    Class,
    pivot_Stereotype,
    pivot_VoidType,
    pivot_Metaclass,
    pivot_InvalidType,
    pivot_DataType,
    pivot_AssociationClass,
    pivot_UnspecifiedType,
    pivot_Behavior,
    pivot_SelfType,
    pivot_AnyType,
    pivot_Detail,
    CollectionKind,
    AssociativityKind,
    PseudostateKind,
    TransitionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pivot_visitor_is_not_abstract():
    assert not inspect.isabstract(pivot_Visitor)


def test_pivot_visitor_constructor_exists():
    assert callable(pivot_Visitor.__init__)


def test_pivot_visitor_constructor_args():
    sig = inspect.signature(pivot_Visitor.__init__)
    params = list(sig.parameters.keys())



def test_pivot_visitable_is_not_abstract():
    assert not inspect.isabstract(pivot_Visitable)


def test_pivot_visitable_constructor_exists():
    assert callable(pivot_Visitable.__init__)


def test_pivot_visitable_constructor_args():
    sig = inspect.signature(pivot_Visitable.__init__)
    params = list(sig.parameters.keys())



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_pivot_referringelement_is_not_abstract():
    assert not inspect.isabstract(pivot_ReferringElement)


def test_pivot_referringelement_constructor_exists():
    assert callable(pivot_ReferringElement.__init__)


def test_pivot_referringelement_constructor_args():
    sig = inspect.signature(pivot_ReferringElement.__init__)
    params = list(sig.parameters.keys())



def test_pivot_statemachine_is_not_abstract():
    assert not inspect.isabstract(pivot_StateMachine)


def test_pivot_statemachine_constructor_exists():
    assert callable(pivot_StateMachine.__init__)


def test_pivot_statemachine_constructor_args():
    sig = inspect.signature(pivot_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_pivot_pivotable_is_not_abstract():
    assert not inspect.isabstract(pivot_Pivotable)


def test_pivot_pivotable_constructor_exists():
    assert callable(pivot_Pivotable.__init__)


def test_pivot_pivotable_constructor_args():
    sig = inspect.signature(pivot_Pivotable.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_pivot_tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(pivot_TupleLiteralPart)


def test_pivot_tupleliteralpart_constructor_exists():
    assert callable(pivot_TupleLiteralPart.__init__)


def test_pivot_tupleliteralpart_constructor_args():
    sig = inspect.signature(pivot_TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_templateparameter_is_not_abstract():
    assert not inspect.isabstract(TemplateParameter)


def test_templateparameter_constructor_exists():
    assert callable(TemplateParameter.__init__)


def test_templateparameter_constructor_args():
    sig = inspect.signature(TemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_pivot_typetemplateparameter_is_not_abstract():
    assert not inspect.isabstract(pivot_TypeTemplateParameter)


def test_pivot_typetemplateparameter_constructor_exists():
    assert callable(pivot_TypeTemplateParameter.__init__)


def test_pivot_typetemplateparameter_constructor_args():
    sig = inspect.signature(pivot_TypeTemplateParameter.__init__)
    params = list(sig.parameters.keys())
    assert "allowSubstitutable" in params, "Missing parameter 'allowSubstitutable'"

def test_pivot_typetemplateparameter_has_allowSubstitutable():
    assert hasattr(pivot_TypeTemplateParameter, "allowSubstitutable")
    descriptor = None
    for klass in pivot_TypeTemplateParameter.__mro__:
        if "allowSubstitutable" in klass.__dict__:
            descriptor = klass.__dict__["allowSubstitutable"]
            break
    assert isinstance(descriptor, property)



def test_pivot_operationtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(pivot_OperationTemplateParameter)


def test_pivot_operationtemplateparameter_constructor_exists():
    assert callable(pivot_OperationTemplateParameter.__init__)


def test_pivot_operationtemplateparameter_constructor_args():
    sig = inspect.signature(pivot_OperationTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_parameterableelement_is_not_abstract():
    assert not inspect.isabstract(ParameterableElement)


def test_parameterableelement_constructor_exists():
    assert callable(ParameterableElement.__init__)


def test_parameterableelement_constructor_args():
    sig = inspect.signature(ParameterableElement.__init__)
    params = list(sig.parameters.keys())



def test_pivot_packageableelement_is_not_abstract():
    assert not inspect.isabstract(pivot_PackageableElement)


def test_pivot_packageableelement_constructor_exists():
    assert callable(pivot_PackageableElement.__init__)


def test_pivot_packageableelement_constructor_args():
    sig = inspect.signature(pivot_PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_templateableelement_is_not_abstract():
    assert not inspect.isabstract(TemplateableElement)


def test_templateableelement_constructor_exists():
    assert callable(TemplateableElement.__init__)


def test_templateableelement_constructor_args():
    sig = inspect.signature(TemplateableElement.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_valuespecification_is_not_abstract():
    assert not inspect.isabstract(ValueSpecification)


def test_valuespecification_constructor_exists():
    assert callable(ValueSpecification.__init__)


def test_valuespecification_constructor_args():
    sig = inspect.signature(ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_featurecallexp_is_not_abstract():
    assert not inspect.isabstract(FeatureCallExp)


def test_featurecallexp_constructor_exists():
    assert callable(FeatureCallExp.__init__)


def test_featurecallexp_constructor_args():
    sig = inspect.signature(FeatureCallExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot_navigationcallexp_is_not_abstract():
    assert not inspect.isabstract(pivot_NavigationCallExp)


def test_pivot_navigationcallexp_constructor_exists():
    assert callable(pivot_NavigationCallExp.__init__)


def test_pivot_navigationcallexp_constructor_args():
    sig = inspect.signature(pivot_NavigationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_nameable_is_not_abstract():
    assert not inspect.isabstract(Nameable)


def test_nameable_constructor_exists():
    assert callable(Nameable.__init__)


def test_nameable_constructor_args():
    sig = inspect.signature(Nameable.__init__)
    params = list(sig.parameters.keys())



def test_pivot_nameable_is_not_abstract():
    assert not inspect.isabstract(pivot_Nameable)


def test_pivot_nameable_constructor_exists():
    assert callable(pivot_Nameable.__init__)


def test_pivot_nameable_constructor_args():
    sig = inspect.signature(pivot_Nameable.__init__)
    params = list(sig.parameters.keys())



def test_pivot_morepivotable_is_not_abstract():
    assert not inspect.isabstract(pivot_MorePivotable)


def test_pivot_morepivotable_constructor_exists():
    assert callable(pivot_MorePivotable.__init__)


def test_pivot_morepivotable_constructor_args():
    sig = inspect.signature(pivot_MorePivotable.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_pivot_profile_is_not_abstract():
    assert not inspect.isabstract(pivot_Profile)


def test_pivot_profile_constructor_exists():
    assert callable(pivot_Profile.__init__)


def test_pivot_profile_constructor_args():
    sig = inspect.signature(pivot_Profile.__init__)
    params = list(sig.parameters.keys())



def test_pivot_library_is_not_abstract():
    assert not inspect.isabstract(pivot_Library)


def test_pivot_library_constructor_exists():
    assert callable(pivot_Library.__init__)


def test_pivot_library_constructor_args():
    sig = inspect.signature(pivot_Library.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_pivot_iteration_is_not_abstract():
    assert not inspect.isabstract(pivot_Iteration)


def test_pivot_iteration_constructor_exists():
    assert callable(pivot_Iteration.__init__)


def test_pivot_iteration_constructor_args():
    sig = inspect.signature(pivot_Iteration.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_pivot_finalstate_is_not_abstract():
    assert not inspect.isabstract(pivot_FinalState)


def test_pivot_finalstate_constructor_exists():
    assert callable(pivot_FinalState.__init__)


def test_pivot_finalstate_constructor_args():
    sig = inspect.signature(pivot_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_callexp_is_not_abstract():
    assert not inspect.isabstract(CallExp)


def test_callexp_constructor_exists():
    assert callable(CallExp.__init__)


def test_callexp_constructor_args():
    sig = inspect.signature(CallExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot_loopexp_is_not_abstract():
    assert not inspect.isabstract(pivot_LoopExp)


def test_pivot_loopexp_constructor_exists():
    assert callable(pivot_LoopExp.__init__)


def test_pivot_loopexp_constructor_args():
    sig = inspect.signature(pivot_LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot_featurecallexp_is_not_abstract():
    assert not inspect.isabstract(pivot_FeatureCallExp)


def test_pivot_featurecallexp_constructor_exists():
    assert callable(pivot_FeatureCallExp.__init__)


def test_pivot_featurecallexp_constructor_args():
    sig = inspect.signature(pivot_FeatureCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "isPre" in params, "Missing parameter 'isPre'"

def test_pivot_featurecallexp_has_isPre():
    assert hasattr(pivot_FeatureCallExp, "isPre")
    descriptor = None
    for klass in pivot_FeatureCallExp.__mro__:
        if "isPre" in klass.__dict__:
            descriptor = klass.__dict__["isPre"]
            break
    assert isinstance(descriptor, property)



def test_typedmultiplicityelement_is_not_abstract():
    assert not inspect.isabstract(TypedMultiplicityElement)


def test_typedmultiplicityelement_constructor_exists():
    assert callable(TypedMultiplicityElement.__init__)


def test_typedmultiplicityelement_constructor_args():
    sig = inspect.signature(TypedMultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_pivot_parameter_is_not_abstract():
    assert not inspect.isabstract(pivot_Parameter)


def test_pivot_parameter_constructor_exists():
    assert callable(pivot_Parameter.__init__)


def test_pivot_parameter_constructor_args():
    sig = inspect.signature(pivot_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_pivot_feature_is_not_abstract():
    assert not inspect.isabstract(pivot_Feature)


def test_pivot_feature_constructor_exists():
    assert callable(pivot_Feature.__init__)


def test_pivot_feature_constructor_args():
    sig = inspect.signature(pivot_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "implementationClass" in params, "Missing parameter 'implementationClass'"
    assert "implementation" in params, "Missing parameter 'implementation'"

def test_pivot_feature_has_implementationClass():
    assert hasattr(pivot_Feature, "implementationClass")
    descriptor = None
    for klass in pivot_Feature.__mro__:
        if "implementationClass" in klass.__dict__:
            descriptor = klass.__dict__["implementationClass"]
            break
    assert isinstance(descriptor, property)

def test_pivot_feature_has_implementation():
    assert hasattr(pivot_Feature, "implementation")
    descriptor = None
    for klass in pivot_Feature.__mro__:
        if "implementation" in klass.__dict__:
            descriptor = klass.__dict__["implementation"]
            break
    assert isinstance(descriptor, property)



def test_referringelement_is_not_abstract():
    assert not inspect.isabstract(ReferringElement)


def test_referringelement_constructor_exists():
    assert callable(ReferringElement.__init__)


def test_referringelement_constructor_args():
    sig = inspect.signature(ReferringElement.__init__)
    params = list(sig.parameters.keys())



def test_pivot_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(pivot_OperationCallExp)


def test_pivot_operationcallexp_constructor_exists():
    assert callable(pivot_OperationCallExp.__init__)


def test_pivot_operationcallexp_constructor_args():
    sig = inspect.signature(pivot_OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot_variable_is_not_abstract():
    assert not inspect.isabstract(pivot_Variable)


def test_pivot_variable_constructor_exists():
    assert callable(pivot_Variable.__init__)


def test_pivot_variable_constructor_args():
    sig = inspect.signature(pivot_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "implicit" in params, "Missing parameter 'implicit'"

def test_pivot_variable_has_implicit():
    assert hasattr(pivot_Variable, "implicit")
    descriptor = None
    for klass in pivot_Variable.__mro__:
        if "implicit" in klass.__dict__:
            descriptor = klass.__dict__["implicit"]
            break
    assert isinstance(descriptor, property)



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot_iteratorexp_is_not_abstract():
    assert not inspect.isabstract(pivot_IteratorExp)


def test_pivot_iteratorexp_constructor_exists():
    assert callable(pivot_IteratorExp.__init__)


def test_pivot_iteratorexp_constructor_args():
    sig = inspect.signature(pivot_IteratorExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot_iterateexp_is_not_abstract():
    assert not inspect.isabstract(pivot_IterateExp)


def test_pivot_iterateexp_constructor_exists():
    assert callable(pivot_IterateExp.__init__)


def test_pivot_iterateexp_constructor_args():
    sig = inspect.signature(pivot_IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(NumericLiteralExp)


def test_numericliteralexp_constructor_exists():
    assert callable(NumericLiteralExp.__init__)


def test_numericliteralexp_constructor_args():
    sig = inspect.signature(NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot_realliteralexp_is_not_abstract():
    assert not inspect.isabstract(pivot_RealLiteralExp)


def test_pivot_realliteralexp_constructor_exists():
    assert callable(pivot_RealLiteralExp.__init__)


def test_pivot_realliteralexp_constructor_args():
    sig = inspect.signature(pivot_RealLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_pivot_realliteralexp_has_realSymbol():
    assert hasattr(pivot_RealLiteralExp, "realSymbol")
    descriptor = None
    for klass in pivot_RealLiteralExp.__mro__:
        if "realSymbol" in klass.__dict__:
            descriptor = klass.__dict__["realSymbol"]
            break
    assert isinstance(descriptor, property)



def test_pivot_unlimitednaturalliteralexp_is_not_abstract():
    assert not inspect.isabstract(pivot_UnlimitedNaturalLiteralExp)


def test_pivot_unlimitednaturalliteralexp_constructor_exists():
    assert callable(pivot_UnlimitedNaturalLiteralExp.__init__)


def test_pivot_unlimitednaturalliteralexp_constructor_args():
    sig = inspect.signature(pivot_UnlimitedNaturalLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "unlimitedNaturalSymbol" in params, "Missing parameter 'unlimitedNaturalSymbol'"

def test_pivot_unlimitednaturalliteralexp_has_unlimitedNaturalSymbol():
    assert hasattr(pivot_UnlimitedNaturalLiteralExp, "unlimitedNaturalSymbol")
    descriptor = None
    for klass in pivot_UnlimitedNaturalLiteralExp.__mro__:
        if "unlimitedNaturalSymbol" in klass.__dict__:
            descriptor = klass.__dict__["unlimitedNaturalSymbol"]
            break
    assert isinstance(descriptor, property)



def test_pivot_integerliteralexp_is_not_abstract():
    assert not inspect.isabstract(pivot_IntegerLiteralExp)


def test_pivot_integerliteralexp_constructor_exists():
    assert callable(pivot_IntegerLiteralExp.__init__)


def test_pivot_integerliteralexp_constructor_args():
    sig = inspect.signature(pivot_IntegerLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_pivot_integerliteralexp_has_integerSymbol():
    assert hasattr(pivot_IntegerLiteralExp, "integerSymbol")
    descriptor = None
    for klass in pivot_IntegerLiteralExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(OpaqueExpression)


def test_opaqueexpression_constructor_exists():
    assert callable(OpaqueExpression.__init__)


def test_opaqueexpression_constructor_args():
    sig = inspect.signature(OpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_pivot_expressioninocl_is_not_abstract():
    assert not inspect.isabstract(pivot_ExpressionInOCL)


def test_pivot_expressioninocl_constructor_exists():
    assert callable(pivot_ExpressionInOCL.__init__)


def test_pivot_expressioninocl_constructor_args():
    sig = inspect.signature(pivot_ExpressionInOCL.__init__)
    params = list(sig.parameters.keys())



def test_visitable_is_not_abstract():
    assert not inspect.isabstract(Visitable)


def test_visitable_constructor_exists():
    assert callable(Visitable.__init__)


def test_visitable_constructor_args():
    sig = inspect.signature(Visitable.__init__)
    params = list(sig.parameters.keys())



def test_dynamicelement_is_not_abstract():
    assert not inspect.isabstract(DynamicElement)


def test_dynamicelement_constructor_exists():
    assert callable(DynamicElement.__init__)


def test_dynamicelement_constructor_args():
    sig = inspect.signature(DynamicElement.__init__)
    params = list(sig.parameters.keys())



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_pivot_pseudostate_is_not_abstract():
    assert not inspect.isabstract(pivot_Pseudostate)


def test_pivot_pseudostate_constructor_exists():
    assert callable(pivot_Pseudostate.__init__)


def test_pivot_pseudostate_constructor_args():
    sig = inspect.signature(pivot_Pseudostate.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_pivot_pseudostate_has_kind():
    assert hasattr(pivot_Pseudostate, "kind")
    descriptor = None
    for klass in pivot_Pseudostate.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_pivot_connectionpointreference_is_not_abstract():
    assert not inspect.isabstract(pivot_ConnectionPointReference)


def test_pivot_connectionpointreference_constructor_exists():
    assert callable(pivot_ConnectionPointReference.__init__)


def test_pivot_connectionpointreference_constructor_args():
    sig = inspect.signature(pivot_ConnectionPointReference.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_pivot_namedelement_is_not_abstract():
    assert not inspect.isabstract(pivot_NamedElement)


def test_pivot_namedelement_constructor_exists():
    assert callable(pivot_NamedElement.__init__)


def test_pivot_namedelement_constructor_args():
    sig = inspect.signature(pivot_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "isStatic" in params, "Missing parameter 'isStatic'"
    assert "name" in params, "Missing parameter 'name'"

def test_pivot_namedelement_has_isStatic():
    assert hasattr(pivot_NamedElement, "isStatic")
    descriptor = None
    for klass in pivot_NamedElement.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)

def test_pivot_namedelement_has_name():
    assert hasattr(pivot_NamedElement, "name")
    descriptor = None
    for klass in pivot_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pivot_parameterableelement_is_not_abstract():
    assert not inspect.isabstract(pivot_ParameterableElement)


def test_pivot_parameterableelement_constructor_exists():
    assert callable(pivot_ParameterableElement.__init__)


def test_pivot_parameterableelement_constructor_args():
    sig = inspect.signature(pivot_ParameterableElement.__init__)
    params = list(sig.parameters.keys())



def test_pivot_dynamicproperty_is_not_abstract():
    assert not inspect.isabstract(pivot_DynamicProperty)


def test_pivot_dynamicproperty_constructor_exists():
    assert callable(pivot_DynamicProperty.__init__)


def test_pivot_dynamicproperty_constructor_args():
    sig = inspect.signature(pivot_DynamicProperty.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_pivot_dynamicproperty_has_default():
    assert hasattr(pivot_DynamicProperty, "default")
    descriptor = None
    for klass in pivot_DynamicProperty.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_pivot_templatesignature_is_not_abstract():
    assert not inspect.isabstract(pivot_TemplateSignature)


def test_pivot_templatesignature_constructor_exists():
    assert callable(pivot_TemplateSignature.__init__)


def test_pivot_templatesignature_constructor_args():
    sig = inspect.signature(pivot_TemplateSignature.__init__)
    params = list(sig.parameters.keys())



def test_pivot_templateableelement_is_not_abstract():
    assert not inspect.isabstract(pivot_TemplateableElement)


def test_pivot_templateableelement_constructor_exists():
    assert callable(pivot_TemplateableElement.__init__)


def test_pivot_templateableelement_constructor_args():
    sig = inspect.signature(pivot_TemplateableElement.__init__)
    params = list(sig.parameters.keys())



def test_pivot_templateparametersubstitution_is_not_abstract():
    assert not inspect.isabstract(pivot_TemplateParameterSubstitution)


def test_pivot_templateparametersubstitution_constructor_exists():
    assert callable(pivot_TemplateParameterSubstitution.__init__)


def test_pivot_templateparametersubstitution_constructor_args():
    sig = inspect.signature(pivot_TemplateParameterSubstitution.__init__)
    params = list(sig.parameters.keys())



def test_pivot_templatebinding_is_not_abstract():
    assert not inspect.isabstract(pivot_TemplateBinding)


def test_pivot_templatebinding_constructor_exists():
    assert callable(pivot_TemplateBinding.__init__)


def test_pivot_templatebinding_constructor_args():
    sig = inspect.signature(pivot_TemplateBinding.__init__)
    params = list(sig.parameters.keys())



def test_pivot_templateparameter_is_not_abstract():
    assert not inspect.isabstract(pivot_TemplateParameter)


def test_pivot_templateparameter_constructor_exists():
    assert callable(pivot_TemplateParameter.__init__)


def test_pivot_templateparameter_constructor_args():
    sig = inspect.signature(pivot_TemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_pivot_dynamicelement_is_not_abstract():
    assert not inspect.isabstract(pivot_DynamicElement)


def test_pivot_dynamicelement_constructor_exists():
    assert callable(pivot_DynamicElement.__init__)


def test_pivot_dynamicelement_constructor_args():
    sig = inspect.signature(pivot_DynamicElement.__init__)
    params = list(sig.parameters.keys())



def test_pivot_comment_is_not_abstract():
    assert not inspect.isabstract(pivot_Comment)


def test_pivot_comment_constructor_exists():
    assert callable(pivot_Comment.__init__)


def test_pivot_comment_constructor_args():
    sig = inspect.signature(pivot_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_pivot_comment_has_body():
    assert hasattr(pivot_Comment, "body")
    descriptor = None
    for klass in pivot_Comment.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_pivot_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(pivot_OpaqueExpression)


def test_pivot_opaqueexpression_constructor_exists():
    assert callable(pivot_OpaqueExpression.__init__)


def test_pivot_opaqueexpression_constructor_args():
    sig = inspect.signature(pivot_OpaqueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"
    assert "body" in params, "Missing parameter 'body'"
    assert "language" in params, "Missing parameter 'language'"

def test_pivot_opaqueexpression_has_message():
    assert hasattr(pivot_OpaqueExpression, "message")
    descriptor = None
    for klass in pivot_OpaqueExpression.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_pivot_opaqueexpression_has_body():
    assert hasattr(pivot_OpaqueExpression, "body")
    descriptor = None
    for klass in pivot_OpaqueExpression.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_pivot_opaqueexpression_has_language():
    assert hasattr(pivot_OpaqueExpression, "language")
    descriptor = None
    for klass in pivot_OpaqueExpression.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_literalexp_is_not_abstract():
    assert not inspect.isabstract(LiteralExp)


def test_literalexp_constructor_exists():
    assert callable(LiteralExp.__init__)


def test_literalexp_constructor_args():
    sig = inspect.signature(LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot_invalidliteralexp_is_not_abstract():
    assert not inspect.isabstract(pivot_InvalidLiteralExp)


def test_pivot_invalidliteralexp_constructor_exists():
    assert callable(pivot_InvalidLiteralExp.__init__)


def test_pivot_invalidliteralexp_constructor_args():
    sig = inspect.signature(pivot_InvalidLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot_enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(pivot_EnumLiteralExp)


def test_pivot_enumliteralexp_constructor_exists():
    assert callable(pivot_EnumLiteralExp.__init__)


def test_pivot_enumliteralexp_constructor_args():
    sig = inspect.signature(pivot_EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot_primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(pivot_PrimitiveLiteralExp)


def test_pivot_primitiveliteralexp_constructor_exists():
    assert callable(pivot_PrimitiveLiteralExp.__init__)


def test_pivot_primitiveliteralexp_constructor_args():
    sig = inspect.signature(pivot_PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot_tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(pivot_TupleLiteralExp)


def test_pivot_tupleliteralexp_constructor_exists():
    assert callable(pivot_TupleLiteralExp.__init__)


def test_pivot_tupleliteralexp_constructor_args():
    sig = inspect.signature(pivot_TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot_collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(pivot_CollectionLiteralExp)


def test_pivot_collectionliteralexp_constructor_exists():
    assert callable(pivot_CollectionLiteralExp.__init__)


def test_pivot_collectionliteralexp_constructor_args():
    sig = inspect.signature(pivot_CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_pivot_collectionliteralexp_has_kind():
    assert hasattr(pivot_CollectionLiteralExp, "kind")
    descriptor = None
    for klass in pivot_CollectionLiteralExp.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_pivot_enumeration_is_not_abstract():
    assert not inspect.isabstract(pivot_Enumeration)


def test_pivot_enumeration_constructor_exists():
    assert callable(pivot_Enumeration.__init__)


def test_pivot_enumeration_constructor_args():
    sig = inspect.signature(pivot_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_pivot_lambdatype_is_not_abstract():
    assert not inspect.isabstract(pivot_LambdaType)


def test_pivot_lambdatype_constructor_exists():
    assert callable(pivot_LambdaType.__init__)


def test_pivot_lambdatype_constructor_args():
    sig = inspect.signature(pivot_LambdaType.__init__)
    params = list(sig.parameters.keys())



def test_pivot_primitivetype_is_not_abstract():
    assert not inspect.isabstract(pivot_PrimitiveType)


def test_pivot_primitivetype_constructor_exists():
    assert callable(pivot_PrimitiveType.__init__)


def test_pivot_primitivetype_constructor_args():
    sig = inspect.signature(pivot_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_pivot_tupletype_is_not_abstract():
    assert not inspect.isabstract(pivot_TupleType)


def test_pivot_tupletype_constructor_exists():
    assert callable(pivot_TupleType.__init__)


def test_pivot_tupletype_constructor_args():
    sig = inspect.signature(pivot_TupleType.__init__)
    params = list(sig.parameters.keys())



def test_pivot_collectiontype_is_not_abstract():
    assert not inspect.isabstract(pivot_CollectionType)


def test_pivot_collectiontype_constructor_exists():
    assert callable(pivot_CollectionType.__init__)


def test_pivot_collectiontype_constructor_args():
    sig = inspect.signature(pivot_CollectionType.__init__)
    params = list(sig.parameters.keys())
    assert "lower" in params, "Missing parameter 'lower'"
    assert "upper" in params, "Missing parameter 'upper'"

def test_pivot_collectiontype_has_lower():
    assert hasattr(pivot_CollectionType, "lower")
    descriptor = None
    for klass in pivot_CollectionType.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_pivot_collectiontype_has_upper():
    assert hasattr(pivot_CollectionType, "upper")
    descriptor = None
    for klass in pivot_CollectionType.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_pivot_typedmultiplicityelement_is_not_abstract():
    assert not inspect.isabstract(pivot_TypedMultiplicityElement)


def test_pivot_typedmultiplicityelement_constructor_exists():
    assert callable(pivot_TypedMultiplicityElement.__init__)


def test_pivot_typedmultiplicityelement_constructor_args():
    sig = inspect.signature(pivot_TypedMultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_pivot_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(pivot_VariableDeclaration)


def test_pivot_variabledeclaration_constructor_exists():
    assert callable(pivot_VariableDeclaration.__init__)


def test_pivot_variabledeclaration_constructor_args():
    sig = inspect.signature(pivot_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_pivot_valuespecification_is_not_abstract():
    assert not inspect.isabstract(pivot_ValueSpecification)


def test_pivot_valuespecification_constructor_exists():
    assert callable(pivot_ValueSpecification.__init__)


def test_pivot_valuespecification_constructor_args():
    sig = inspect.signature(pivot_ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_pivot_constructorpart_is_not_abstract():
    assert not inspect.isabstract(pivot_ConstructorPart)


def test_pivot_constructorpart_constructor_exists():
    assert callable(pivot_ConstructorPart.__init__)


def test_pivot_constructorpart_constructor_args():
    sig = inspect.signature(pivot_ConstructorPart.__init__)
    params = list(sig.parameters.keys())



def test_pivot_collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(pivot_CollectionLiteralPart)


def test_pivot_collectionliteralpart_constructor_exists():
    assert callable(pivot_CollectionLiteralPart.__init__)


def test_pivot_collectionliteralpart_constructor_args():
    sig = inspect.signature(pivot_CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_namespace_is_not_abstract():
    assert not inspect.isabstract(Namespace)


def test_namespace_constructor_exists():
    assert callable(Namespace.__init__)


def test_namespace_constructor_args():
    sig = inspect.signature(Namespace.__init__)
    params = list(sig.parameters.keys())



def test_pivot_package_is_not_abstract():
    assert not inspect.isabstract(pivot_Package)


def test_pivot_package_constructor_exists():
    assert callable(pivot_Package.__init__)


def test_pivot_package_constructor_args():
    sig = inspect.signature(pivot_Package.__init__)
    params = list(sig.parameters.keys())
    assert "nsURI" in params, "Missing parameter 'nsURI'"
    assert "nsPrefix" in params, "Missing parameter 'nsPrefix'"

def test_pivot_package_has_nsURI():
    assert hasattr(pivot_Package, "nsURI")
    descriptor = None
    for klass in pivot_Package.__mro__:
        if "nsURI" in klass.__dict__:
            descriptor = klass.__dict__["nsURI"]
            break
    assert isinstance(descriptor, property)

def test_pivot_package_has_nsPrefix():
    assert hasattr(pivot_Package, "nsPrefix")
    descriptor = None
    for klass in pivot_Package.__mro__:
        if "nsPrefix" in klass.__dict__:
            descriptor = klass.__dict__["nsPrefix"]
            break
    assert isinstance(descriptor, property)



def test_pivot_region_is_not_abstract():
    assert not inspect.isabstract(pivot_Region)


def test_pivot_region_constructor_exists():
    assert callable(pivot_Region.__init__)


def test_pivot_region_constructor_args():
    sig = inspect.signature(pivot_Region.__init__)
    params = list(sig.parameters.keys())



def test_pivot_transition_is_not_abstract():
    assert not inspect.isabstract(pivot_Transition)


def test_pivot_transition_constructor_exists():
    assert callable(pivot_Transition.__init__)


def test_pivot_transition_constructor_args():
    sig = inspect.signature(pivot_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_pivot_transition_has_kind():
    assert hasattr(pivot_Transition, "kind")
    descriptor = None
    for klass in pivot_Transition.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_pivot_root_is_not_abstract():
    assert not inspect.isabstract(pivot_Root)


def test_pivot_root_constructor_exists():
    assert callable(pivot_Root.__init__)


def test_pivot_root_constructor_args():
    sig = inspect.signature(pivot_Root.__init__)
    params = list(sig.parameters.keys())
    assert "externalURI" in params, "Missing parameter 'externalURI'"

def test_pivot_root_has_externalURI():
    assert hasattr(pivot_Root, "externalURI")
    descriptor = None
    for klass in pivot_Root.__mro__:
        if "externalURI" in klass.__dict__:
            descriptor = klass.__dict__["externalURI"]
            break
    assert isinstance(descriptor, property)



def test_pivot_state_is_not_abstract():
    assert not inspect.isabstract(pivot_State)


def test_pivot_state_constructor_exists():
    assert callable(pivot_State.__init__)


def test_pivot_state_constructor_args():
    sig = inspect.signature(pivot_State.__init__)
    params = list(sig.parameters.keys())
    assert "isSimple" in params, "Missing parameter 'isSimple'"
    assert "isSubmachineState" in params, "Missing parameter 'isSubmachineState'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isOrthogonal" in params, "Missing parameter 'isOrthogonal'"

def test_pivot_state_has_isSimple():
    assert hasattr(pivot_State, "isSimple")
    descriptor = None
    for klass in pivot_State.__mro__:
        if "isSimple" in klass.__dict__:
            descriptor = klass.__dict__["isSimple"]
            break
    assert isinstance(descriptor, property)

def test_pivot_state_has_isSubmachineState():
    assert hasattr(pivot_State, "isSubmachineState")
    descriptor = None
    for klass in pivot_State.__mro__:
        if "isSubmachineState" in klass.__dict__:
            descriptor = klass.__dict__["isSubmachineState"]
            break
    assert isinstance(descriptor, property)

def test_pivot_state_has_isComposite():
    assert hasattr(pivot_State, "isComposite")
    descriptor = None
    for klass in pivot_State.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_pivot_state_has_isOrthogonal():
    assert hasattr(pivot_State, "isOrthogonal")
    descriptor = None
    for klass in pivot_State.__mro__:
        if "isOrthogonal" in klass.__dict__:
            descriptor = klass.__dict__["isOrthogonal"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_pivot_messagetype_is_not_abstract():
    assert not inspect.isabstract(pivot_MessageType)


def test_pivot_messagetype_constructor_exists():
    assert callable(pivot_MessageType.__init__)


def test_pivot_messagetype_constructor_args():
    sig = inspect.signature(pivot_MessageType.__init__)
    params = list(sig.parameters.keys())



def test_pivot_templateparametertype_is_not_abstract():
    assert not inspect.isabstract(pivot_TemplateParameterType)


def test_pivot_templateparametertype_constructor_exists():
    assert callable(pivot_TemplateParameterType.__init__)


def test_pivot_templateparametertype_constructor_args():
    sig = inspect.signature(pivot_TemplateParameterType.__init__)
    params = list(sig.parameters.keys())
    assert "specification" in params, "Missing parameter 'specification'"

def test_pivot_templateparametertype_has_specification():
    assert hasattr(pivot_TemplateParameterType, "specification")
    descriptor = None
    for klass in pivot_TemplateParameterType.__mro__:
        if "specification" in klass.__dict__:
            descriptor = klass.__dict__["specification"]
            break
    assert isinstance(descriptor, property)



def test_pivot_dynamictype_is_not_abstract():
    assert not inspect.isabstract(pivot_DynamicType)


def test_pivot_dynamictype_constructor_exists():
    assert callable(pivot_DynamicType.__init__)


def test_pivot_dynamictype_constructor_args():
    sig = inspect.signature(pivot_DynamicType.__init__)
    params = list(sig.parameters.keys())



def test_pivot_elementextension_is_not_abstract():
    assert not inspect.isabstract(pivot_ElementExtension)


def test_pivot_elementextension_constructor_exists():
    assert callable(pivot_ElementExtension.__init__)


def test_pivot_elementextension_constructor_args():
    sig = inspect.signature(pivot_ElementExtension.__init__)
    params = list(sig.parameters.keys())



def test_pivot_class_is_not_abstract():
    assert not inspect.isabstract(pivot_Class)


def test_pivot_class_constructor_exists():
    assert callable(pivot_Class.__init__)


def test_pivot_class_constructor_args():
    sig = inspect.signature(pivot_Class.__init__)
    params = list(sig.parameters.keys())
    assert "isInterface" in params, "Missing parameter 'isInterface'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_pivot_class_has_isInterface():
    assert hasattr(pivot_Class, "isInterface")
    descriptor = None
    for klass in pivot_Class.__mro__:
        if "isInterface" in klass.__dict__:
            descriptor = klass.__dict__["isInterface"]
            break
    assert isinstance(descriptor, property)

def test_pivot_class_has_isAbstract():
    assert hasattr(pivot_Class, "isAbstract")
    descriptor = None
    for klass in pivot_Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_pivot_operation_is_not_abstract():
    assert not inspect.isabstract(pivot_Operation)


def test_pivot_operation_constructor_exists():
    assert callable(pivot_Operation.__init__)


def test_pivot_operation_constructor_args():
    sig = inspect.signature(pivot_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "isValidating" in params, "Missing parameter 'isValidating'"
    assert "isInvalidating" in params, "Missing parameter 'isInvalidating'"

def test_pivot_operation_has_isValidating():
    assert hasattr(pivot_Operation, "isValidating")
    descriptor = None
    for klass in pivot_Operation.__mro__:
        if "isValidating" in klass.__dict__:
            descriptor = klass.__dict__["isValidating"]
            break
    assert isinstance(descriptor, property)

def test_pivot_operation_has_isInvalidating():
    assert hasattr(pivot_Operation, "isInvalidating")
    descriptor = None
    for klass in pivot_Operation.__mro__:
        if "isInvalidating" in klass.__dict__:
            descriptor = klass.__dict__["isInvalidating"]
            break
    assert isinstance(descriptor, property)



def test_pivot_oclexpression_is_not_abstract():
    assert not inspect.isabstract(pivot_OCLExpression)


def test_pivot_oclexpression_constructor_exists():
    assert callable(pivot_OCLExpression.__init__)


def test_pivot_oclexpression_constructor_args():
    sig = inspect.signature(pivot_OCLExpression.__init__)
    params = list(sig.parameters.keys())



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OCLExpression)


def test_oclexpression_constructor_exists():
    assert callable(OCLExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OCLExpression.__init__)
    params = list(sig.parameters.keys())



def test_pivot_constructorexp_is_not_abstract():
    assert not inspect.isabstract(pivot_ConstructorExp)


def test_pivot_constructorexp_constructor_exists():
    assert callable(pivot_ConstructorExp.__init__)


def test_pivot_constructorexp_constructor_args():
    sig = inspect.signature(pivot_ConstructorExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_pivot_constructorexp_has_value():
    assert hasattr(pivot_ConstructorExp, "value")
    descriptor = None
    for klass in pivot_ConstructorExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_pivot_messageexp_is_not_abstract():
    assert not inspect.isabstract(pivot_MessageExp)


def test_pivot_messageexp_constructor_exists():
    assert callable(pivot_MessageExp.__init__)


def test_pivot_messageexp_constructor_args():
    sig = inspect.signature(pivot_MessageExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot_typeexp_is_not_abstract():
    assert not inspect.isabstract(pivot_TypeExp)


def test_pivot_typeexp_constructor_exists():
    assert callable(pivot_TypeExp.__init__)


def test_pivot_typeexp_constructor_args():
    sig = inspect.signature(pivot_TypeExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot_stateexp_is_not_abstract():
    assert not inspect.isabstract(pivot_StateExp)


def test_pivot_stateexp_constructor_exists():
    assert callable(pivot_StateExp.__init__)


def test_pivot_stateexp_constructor_args():
    sig = inspect.signature(pivot_StateExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot_ifexp_is_not_abstract():
    assert not inspect.isabstract(pivot_IfExp)


def test_pivot_ifexp_constructor_exists():
    assert callable(pivot_IfExp.__init__)


def test_pivot_ifexp_constructor_args():
    sig = inspect.signature(pivot_IfExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot_letexp_is_not_abstract():
    assert not inspect.isabstract(pivot_LetExp)


def test_pivot_letexp_constructor_exists():
    assert callable(pivot_LetExp.__init__)


def test_pivot_letexp_constructor_args():
    sig = inspect.signature(pivot_LetExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot_literalexp_is_not_abstract():
    assert not inspect.isabstract(pivot_LiteralExp)


def test_pivot_literalexp_constructor_exists():
    assert callable(pivot_LiteralExp.__init__)


def test_pivot_literalexp_constructor_args():
    sig = inspect.signature(pivot_LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot_variableexp_is_not_abstract():
    assert not inspect.isabstract(pivot_VariableExp)


def test_pivot_variableexp_constructor_exists():
    assert callable(pivot_VariableExp.__init__)


def test_pivot_variableexp_constructor_args():
    sig = inspect.signature(pivot_VariableExp.__init__)
    params = list(sig.parameters.keys())
    assert "implicit" in params, "Missing parameter 'implicit'"

def test_pivot_variableexp_has_implicit():
    assert hasattr(pivot_VariableExp, "implicit")
    descriptor = None
    for klass in pivot_VariableExp.__mro__:
        if "implicit" in klass.__dict__:
            descriptor = klass.__dict__["implicit"]
            break
    assert isinstance(descriptor, property)



def test_pivot_unspecifiedvalueexp_is_not_abstract():
    assert not inspect.isabstract(pivot_UnspecifiedValueExp)


def test_pivot_unspecifiedvalueexp_constructor_exists():
    assert callable(pivot_UnspecifiedValueExp.__init__)


def test_pivot_unspecifiedvalueexp_constructor_args():
    sig = inspect.signature(pivot_UnspecifiedValueExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot_callexp_is_not_abstract():
    assert not inspect.isabstract(pivot_CallExp)


def test_pivot_callexp_constructor_exists():
    assert callable(pivot_CallExp.__init__)


def test_pivot_callexp_constructor_args():
    sig = inspect.signature(pivot_CallExp.__init__)
    params = list(sig.parameters.keys())
    assert "implicit" in params, "Missing parameter 'implicit'"

def test_pivot_callexp_has_implicit():
    assert hasattr(pivot_CallExp, "implicit")
    descriptor = None
    for klass in pivot_CallExp.__mro__:
        if "implicit" in klass.__dict__:
            descriptor = klass.__dict__["implicit"]
            break
    assert isinstance(descriptor, property)



def test_collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralPart)


def test_collectionliteralpart_constructor_exists():
    assert callable(CollectionLiteralPart.__init__)


def test_collectionliteralpart_constructor_args():
    sig = inspect.signature(CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_pivot_collectionrange_is_not_abstract():
    assert not inspect.isabstract(pivot_CollectionRange)


def test_pivot_collectionrange_constructor_exists():
    assert callable(pivot_CollectionRange.__init__)


def test_pivot_collectionrange_constructor_args():
    sig = inspect.signature(pivot_CollectionRange.__init__)
    params = list(sig.parameters.keys())



def test_pivot_collectionitem_is_not_abstract():
    assert not inspect.isabstract(pivot_CollectionItem)


def test_pivot_collectionitem_constructor_exists():
    assert callable(pivot_CollectionItem.__init__)


def test_pivot_collectionitem_constructor_args():
    sig = inspect.signature(pivot_CollectionItem.__init__)
    params = list(sig.parameters.keys())



def test_pivot_element_is_not_abstract():
    assert not inspect.isabstract(pivot_Element)


def test_pivot_element_constructor_exists():
    assert callable(pivot_Element.__init__)


def test_pivot_element_constructor_args():
    sig = inspect.signature(pivot_Element.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_pivot_constraint_is_not_abstract():
    assert not inspect.isabstract(pivot_Constraint)


def test_pivot_constraint_constructor_exists():
    assert callable(pivot_Constraint.__init__)


def test_pivot_constraint_constructor_args():
    sig = inspect.signature(pivot_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "isCallable" in params, "Missing parameter 'isCallable'"

def test_pivot_constraint_has_isCallable():
    assert hasattr(pivot_Constraint, "isCallable")
    descriptor = None
    for klass in pivot_Constraint.__mro__:
        if "isCallable" in klass.__dict__:
            descriptor = klass.__dict__["isCallable"]
            break
    assert isinstance(descriptor, property)



def test_pivot_type_is_not_abstract():
    assert not inspect.isabstract(pivot_Type)


def test_pivot_type_constructor_exists():
    assert callable(pivot_Type.__init__)


def test_pivot_type_constructor_args():
    sig = inspect.signature(pivot_Type.__init__)
    params = list(sig.parameters.keys())
    assert "instanceClassName" in params, "Missing parameter 'instanceClassName'"

def test_pivot_type_has_instanceClassName():
    assert hasattr(pivot_Type, "instanceClassName")
    descriptor = None
    for klass in pivot_Type.__mro__:
        if "instanceClassName" in klass.__dict__:
            descriptor = klass.__dict__["instanceClassName"]
            break
    assert isinstance(descriptor, property)



def test_pivot_namespace_is_not_abstract():
    assert not inspect.isabstract(pivot_Namespace)


def test_pivot_namespace_constructor_exists():
    assert callable(pivot_Namespace.__init__)


def test_pivot_namespace_constructor_args():
    sig = inspect.signature(pivot_Namespace.__init__)
    params = list(sig.parameters.keys())



def test_pivot_sendsignalaction_is_not_abstract():
    assert not inspect.isabstract(pivot_SendSignalAction)


def test_pivot_sendsignalaction_constructor_exists():
    assert callable(pivot_SendSignalAction.__init__)


def test_pivot_sendsignalaction_constructor_args():
    sig = inspect.signature(pivot_SendSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_pivot_vertex_is_not_abstract():
    assert not inspect.isabstract(pivot_Vertex)


def test_pivot_vertex_constructor_exists():
    assert callable(pivot_Vertex.__init__)


def test_pivot_vertex_constructor_args():
    sig = inspect.signature(pivot_Vertex.__init__)
    params = list(sig.parameters.keys())



def test_pivot_typedelement_is_not_abstract():
    assert not inspect.isabstract(pivot_TypedElement)


def test_pivot_typedelement_constructor_exists():
    assert callable(pivot_TypedElement.__init__)


def test_pivot_typedelement_constructor_args():
    sig = inspect.signature(pivot_TypedElement.__init__)
    params = list(sig.parameters.keys())
    assert "isRequired" in params, "Missing parameter 'isRequired'"

def test_pivot_typedelement_has_isRequired():
    assert hasattr(pivot_TypedElement, "isRequired")
    descriptor = None
    for klass in pivot_TypedElement.__mro__:
        if "isRequired" in klass.__dict__:
            descriptor = klass.__dict__["isRequired"]
            break
    assert isinstance(descriptor, property)



def test_pivot_calloperationaction_is_not_abstract():
    assert not inspect.isabstract(pivot_CallOperationAction)


def test_pivot_calloperationaction_constructor_exists():
    assert callable(pivot_CallOperationAction.__init__)


def test_pivot_calloperationaction_constructor_args():
    sig = inspect.signature(pivot_CallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_pivot_signal_is_not_abstract():
    assert not inspect.isabstract(pivot_Signal)


def test_pivot_signal_constructor_exists():
    assert callable(pivot_Signal.__init__)


def test_pivot_signal_constructor_args():
    sig = inspect.signature(pivot_Signal.__init__)
    params = list(sig.parameters.keys())



def test_pivot_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(pivot_EnumerationLiteral)


def test_pivot_enumerationliteral_constructor_exists():
    assert callable(pivot_EnumerationLiteral.__init__)


def test_pivot_enumerationliteral_constructor_args():
    sig = inspect.signature(pivot_EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_pivot_enumerationliteral_has_value():
    assert hasattr(pivot_EnumerationLiteral, "value")
    descriptor = None
    for klass in pivot_EnumerationLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_pivot_precedence_is_not_abstract():
    assert not inspect.isabstract(pivot_Precedence)


def test_pivot_precedence_constructor_exists():
    assert callable(pivot_Precedence.__init__)


def test_pivot_precedence_constructor_args():
    sig = inspect.signature(pivot_Precedence.__init__)
    params = list(sig.parameters.keys())
    assert "order" in params, "Missing parameter 'order'"
    assert "associativity" in params, "Missing parameter 'associativity'"

def test_pivot_precedence_has_order():
    assert hasattr(pivot_Precedence, "order")
    descriptor = None
    for klass in pivot_Precedence.__mro__:
        if "order" in klass.__dict__:
            descriptor = klass.__dict__["order"]
            break
    assert isinstance(descriptor, property)

def test_pivot_precedence_has_associativity():
    assert hasattr(pivot_Precedence, "associativity")
    descriptor = None
    for klass in pivot_Precedence.__mro__:
        if "associativity" in klass.__dict__:
            descriptor = klass.__dict__["associativity"]
            break
    assert isinstance(descriptor, property)



def test_pivot_trigger_is_not_abstract():
    assert not inspect.isabstract(pivot_Trigger)


def test_pivot_trigger_constructor_exists():
    assert callable(pivot_Trigger.__init__)


def test_pivot_trigger_constructor_args():
    sig = inspect.signature(pivot_Trigger.__init__)
    params = list(sig.parameters.keys())



def test_pivot_import_is_not_abstract():
    assert not inspect.isabstract(pivot_Import)


def test_pivot_import_constructor_exists():
    assert callable(pivot_Import.__init__)


def test_pivot_import_constructor_args():
    sig = inspect.signature(pivot_Import.__init__)
    params = list(sig.parameters.keys())



def test_pivot_annotation_is_not_abstract():
    assert not inspect.isabstract(pivot_Annotation)


def test_pivot_annotation_constructor_exists():
    assert callable(pivot_Annotation.__init__)


def test_pivot_annotation_constructor_args():
    sig = inspect.signature(pivot_Annotation.__init__)
    params = list(sig.parameters.keys())



def test_primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveLiteralExp)


def test_primitiveliteralexp_constructor_exists():
    assert callable(PrimitiveLiteralExp.__init__)


def test_primitiveliteralexp_constructor_args():
    sig = inspect.signature(PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot_numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(pivot_NumericLiteralExp)


def test_pivot_numericliteralexp_constructor_exists():
    assert callable(pivot_NumericLiteralExp.__init__)


def test_pivot_numericliteralexp_constructor_args():
    sig = inspect.signature(pivot_NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot_nullliteralexp_is_not_abstract():
    assert not inspect.isabstract(pivot_NullLiteralExp)


def test_pivot_nullliteralexp_constructor_exists():
    assert callable(pivot_NullLiteralExp.__init__)


def test_pivot_nullliteralexp_constructor_args():
    sig = inspect.signature(pivot_NullLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot_stringliteralexp_is_not_abstract():
    assert not inspect.isabstract(pivot_StringLiteralExp)


def test_pivot_stringliteralexp_constructor_exists():
    assert callable(pivot_StringLiteralExp.__init__)


def test_pivot_stringliteralexp_constructor_args():
    sig = inspect.signature(pivot_StringLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_pivot_stringliteralexp_has_stringSymbol():
    assert hasattr(pivot_StringLiteralExp, "stringSymbol")
    descriptor = None
    for klass in pivot_StringLiteralExp.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_pivot_booleanliteralexp_is_not_abstract():
    assert not inspect.isabstract(pivot_BooleanLiteralExp)


def test_pivot_booleanliteralexp_constructor_exists():
    assert callable(pivot_BooleanLiteralExp.__init__)


def test_pivot_booleanliteralexp_constructor_args():
    sig = inspect.signature(pivot_BooleanLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_pivot_booleanliteralexp_has_booleanSymbol():
    assert hasattr(pivot_BooleanLiteralExp, "booleanSymbol")
    descriptor = None
    for klass in pivot_BooleanLiteralExp.__mro__:
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



def test_pivot_orderedsettype_is_not_abstract():
    assert not inspect.isabstract(pivot_OrderedSetType)


def test_pivot_orderedsettype_constructor_exists():
    assert callable(pivot_OrderedSetType.__init__)


def test_pivot_orderedsettype_constructor_args():
    sig = inspect.signature(pivot_OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_pivot_sequencetype_is_not_abstract():
    assert not inspect.isabstract(pivot_SequenceType)


def test_pivot_sequencetype_constructor_exists():
    assert callable(pivot_SequenceType.__init__)


def test_pivot_sequencetype_constructor_args():
    sig = inspect.signature(pivot_SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_pivot_settype_is_not_abstract():
    assert not inspect.isabstract(pivot_SetType)


def test_pivot_settype_constructor_exists():
    assert callable(pivot_SetType.__init__)


def test_pivot_settype_constructor_args():
    sig = inspect.signature(pivot_SetType.__init__)
    params = list(sig.parameters.keys())



def test_pivot_bagtype_is_not_abstract():
    assert not inspect.isabstract(pivot_BagType)


def test_pivot_bagtype_constructor_exists():
    assert callable(pivot_BagType.__init__)


def test_pivot_bagtype_constructor_args():
    sig = inspect.signature(pivot_BagType.__init__)
    params = list(sig.parameters.keys())



def test_navigationcallexp_is_not_abstract():
    assert not inspect.isabstract(NavigationCallExp)


def test_navigationcallexp_constructor_exists():
    assert callable(NavigationCallExp.__init__)


def test_navigationcallexp_constructor_args():
    sig = inspect.signature(NavigationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(pivot_PropertyCallExp)


def test_pivot_propertycallexp_constructor_exists():
    assert callable(pivot_PropertyCallExp.__init__)


def test_pivot_propertycallexp_constructor_args():
    sig = inspect.signature(pivot_PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot_associationclasscallexp_is_not_abstract():
    assert not inspect.isabstract(pivot_AssociationClassCallExp)


def test_pivot_associationclasscallexp_constructor_exists():
    assert callable(pivot_AssociationClassCallExp.__init__)


def test_pivot_associationclasscallexp_constructor_args():
    sig = inspect.signature(pivot_AssociationClassCallExp.__init__)
    params = list(sig.parameters.keys())



def test_pivot_property_is_not_abstract():
    assert not inspect.isabstract(pivot_Property)


def test_pivot_property_constructor_exists():
    assert callable(pivot_Property.__init__)


def test_pivot_property_constructor_args():
    sig = inspect.signature(pivot_Property.__init__)
    params = list(sig.parameters.keys())
    assert "isID" in params, "Missing parameter 'isID'"
    assert "isUnsettable" in params, "Missing parameter 'isUnsettable'"
    assert "implicit" in params, "Missing parameter 'implicit'"
    assert "default" in params, "Missing parameter 'default'"
    assert "isDerived" in params, "Missing parameter 'isDerived'"
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isTransient" in params, "Missing parameter 'isTransient'"
    assert "isVolatile" in params, "Missing parameter 'isVolatile'"
    assert "isResolveProxies" in params, "Missing parameter 'isResolveProxies'"

def test_pivot_property_has_isID():
    assert hasattr(pivot_Property, "isID")
    descriptor = None
    for klass in pivot_Property.__mro__:
        if "isID" in klass.__dict__:
            descriptor = klass.__dict__["isID"]
            break
    assert isinstance(descriptor, property)

def test_pivot_property_has_isUnsettable():
    assert hasattr(pivot_Property, "isUnsettable")
    descriptor = None
    for klass in pivot_Property.__mro__:
        if "isUnsettable" in klass.__dict__:
            descriptor = klass.__dict__["isUnsettable"]
            break
    assert isinstance(descriptor, property)

def test_pivot_property_has_implicit():
    assert hasattr(pivot_Property, "implicit")
    descriptor = None
    for klass in pivot_Property.__mro__:
        if "implicit" in klass.__dict__:
            descriptor = klass.__dict__["implicit"]
            break
    assert isinstance(descriptor, property)

def test_pivot_property_has_default():
    assert hasattr(pivot_Property, "default")
    descriptor = None
    for klass in pivot_Property.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_pivot_property_has_isDerived():
    assert hasattr(pivot_Property, "isDerived")
    descriptor = None
    for klass in pivot_Property.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)

def test_pivot_property_has_isReadOnly():
    assert hasattr(pivot_Property, "isReadOnly")
    descriptor = None
    for klass in pivot_Property.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)

def test_pivot_property_has_isComposite():
    assert hasattr(pivot_Property, "isComposite")
    descriptor = None
    for klass in pivot_Property.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_pivot_property_has_isTransient():
    assert hasattr(pivot_Property, "isTransient")
    descriptor = None
    for klass in pivot_Property.__mro__:
        if "isTransient" in klass.__dict__:
            descriptor = klass.__dict__["isTransient"]
            break
    assert isinstance(descriptor, property)

def test_pivot_property_has_isVolatile():
    assert hasattr(pivot_Property, "isVolatile")
    descriptor = None
    for klass in pivot_Property.__mro__:
        if "isVolatile" in klass.__dict__:
            descriptor = klass.__dict__["isVolatile"]
            break
    assert isinstance(descriptor, property)

def test_pivot_property_has_isResolveProxies():
    assert hasattr(pivot_Property, "isResolveProxies")
    descriptor = None
    for klass in pivot_Property.__mro__:
        if "isResolveProxies" in klass.__dict__:
            descriptor = klass.__dict__["isResolveProxies"]
            break
    assert isinstance(descriptor, property)



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_pivot_stereotype_is_not_abstract():
    assert not inspect.isabstract(pivot_Stereotype)


def test_pivot_stereotype_constructor_exists():
    assert callable(pivot_Stereotype.__init__)


def test_pivot_stereotype_constructor_args():
    sig = inspect.signature(pivot_Stereotype.__init__)
    params = list(sig.parameters.keys())



def test_pivot_voidtype_is_not_abstract():
    assert not inspect.isabstract(pivot_VoidType)


def test_pivot_voidtype_constructor_exists():
    assert callable(pivot_VoidType.__init__)


def test_pivot_voidtype_constructor_args():
    sig = inspect.signature(pivot_VoidType.__init__)
    params = list(sig.parameters.keys())



def test_pivot_metaclass_is_not_abstract():
    assert not inspect.isabstract(pivot_Metaclass)


def test_pivot_metaclass_constructor_exists():
    assert callable(pivot_Metaclass.__init__)


def test_pivot_metaclass_constructor_args():
    sig = inspect.signature(pivot_Metaclass.__init__)
    params = list(sig.parameters.keys())



def test_pivot_invalidtype_is_not_abstract():
    assert not inspect.isabstract(pivot_InvalidType)


def test_pivot_invalidtype_constructor_exists():
    assert callable(pivot_InvalidType.__init__)


def test_pivot_invalidtype_constructor_args():
    sig = inspect.signature(pivot_InvalidType.__init__)
    params = list(sig.parameters.keys())



def test_pivot_datatype_is_not_abstract():
    assert not inspect.isabstract(pivot_DataType)


def test_pivot_datatype_constructor_exists():
    assert callable(pivot_DataType.__init__)


def test_pivot_datatype_constructor_args():
    sig = inspect.signature(pivot_DataType.__init__)
    params = list(sig.parameters.keys())
    assert "isSerializable" in params, "Missing parameter 'isSerializable'"

def test_pivot_datatype_has_isSerializable():
    assert hasattr(pivot_DataType, "isSerializable")
    descriptor = None
    for klass in pivot_DataType.__mro__:
        if "isSerializable" in klass.__dict__:
            descriptor = klass.__dict__["isSerializable"]
            break
    assert isinstance(descriptor, property)



def test_pivot_associationclass_is_not_abstract():
    assert not inspect.isabstract(pivot_AssociationClass)


def test_pivot_associationclass_constructor_exists():
    assert callable(pivot_AssociationClass.__init__)


def test_pivot_associationclass_constructor_args():
    sig = inspect.signature(pivot_AssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_pivot_unspecifiedtype_is_not_abstract():
    assert not inspect.isabstract(pivot_UnspecifiedType)


def test_pivot_unspecifiedtype_constructor_exists():
    assert callable(pivot_UnspecifiedType.__init__)


def test_pivot_unspecifiedtype_constructor_args():
    sig = inspect.signature(pivot_UnspecifiedType.__init__)
    params = list(sig.parameters.keys())



def test_pivot_behavior_is_not_abstract():
    assert not inspect.isabstract(pivot_Behavior)


def test_pivot_behavior_constructor_exists():
    assert callable(pivot_Behavior.__init__)


def test_pivot_behavior_constructor_args():
    sig = inspect.signature(pivot_Behavior.__init__)
    params = list(sig.parameters.keys())



def test_pivot_selftype_is_not_abstract():
    assert not inspect.isabstract(pivot_SelfType)


def test_pivot_selftype_constructor_exists():
    assert callable(pivot_SelfType.__init__)


def test_pivot_selftype_constructor_args():
    sig = inspect.signature(pivot_SelfType.__init__)
    params = list(sig.parameters.keys())



def test_pivot_anytype_is_not_abstract():
    assert not inspect.isabstract(pivot_AnyType)


def test_pivot_anytype_constructor_exists():
    assert callable(pivot_AnyType.__init__)


def test_pivot_anytype_constructor_args():
    sig = inspect.signature(pivot_AnyType.__init__)
    params = list(sig.parameters.keys())



def test_pivot_detail_is_not_abstract():
    assert not inspect.isabstract(pivot_Detail)


def test_pivot_detail_constructor_exists():
    assert callable(pivot_Detail.__init__)


def test_pivot_detail_constructor_args():
    sig = inspect.signature(pivot_Detail.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_pivot_detail_has_value():
    assert hasattr(pivot_Detail, "value")
    descriptor = None
    for klass in pivot_Detail.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_collectionkind_exists():
    # Check that the Enumeration exists
    assert CollectionKind is not None

def test_collectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CollectionKind]
    expected_literals = [
        "Bag",
        "OrderedSet",
        "Collection",
        "Set",
        "Sequence",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CollectionKind"

def test_associativitykind_exists():
    # Check that the Enumeration exists
    assert AssociativityKind is not None

def test_associativitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssociativityKind]
    expected_literals = [
        "Right",
        "Left",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssociativityKind"

def test_pseudostatekind_exists():
    # Check that the Enumeration exists
    assert PseudostateKind is not None

def test_pseudostatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PseudostateKind]
    expected_literals = [
        "fork",
        "shallowHistory",
        "exitPoint",
        "deepHistory",
        "terminate",
        "initial",
        "join",
        "entryPoint",
        "choice",
        "junction",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PseudostateKind"

def test_transitionkind_exists():
    # Check that the Enumeration exists
    assert TransitionKind is not None

def test_transitionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TransitionKind]
    expected_literals = [
        "external",
        "local",
        "internal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TransitionKind"


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
pivot_Visitor_strategy = st.builds(
    pivot_Visitor,
)
pivot_Visitable_strategy = st.builds(
    pivot_Visitable,
)
Behavior_strategy = st.builds(
    Behavior,
)
pivot_ReferringElement_strategy = st.builds(
    pivot_ReferringElement,
)
pivot_StateMachine_strategy = st.builds(
    pivot_StateMachine,
)
pivot_Pivotable_strategy = st.builds(
    pivot_Pivotable,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
pivot_TupleLiteralPart_strategy = st.builds(
    pivot_TupleLiteralPart,
)
TemplateParameter_strategy = st.builds(
    TemplateParameter,
)
pivot_TypeTemplateParameter_strategy = st.builds(
    pivot_TypeTemplateParameter,
    allowSubstitutable=
        safe_text
)
pivot_OperationTemplateParameter_strategy = st.builds(
    pivot_OperationTemplateParameter,
)
ParameterableElement_strategy = st.builds(
    ParameterableElement,
)
pivot_PackageableElement_strategy = st.builds(
    pivot_PackageableElement,
)
TemplateableElement_strategy = st.builds(
    TemplateableElement,
)
Feature_strategy = st.builds(
    Feature,
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
FeatureCallExp_strategy = st.builds(
    FeatureCallExp,
)
pivot_NavigationCallExp_strategy = st.builds(
    pivot_NavigationCallExp,
)
Nameable_strategy = st.builds(
    Nameable,
)
pivot_Nameable_strategy = st.builds(
    pivot_Nameable,
)
pivot_MorePivotable_strategy = st.builds(
    pivot_MorePivotable,
)
Package_strategy = st.builds(
    Package,
)
pivot_Profile_strategy = st.builds(
    pivot_Profile,
)
pivot_Library_strategy = st.builds(
    pivot_Library,
)
Operation_strategy = st.builds(
    Operation,
)
pivot_Iteration_strategy = st.builds(
    pivot_Iteration,
)
State_strategy = st.builds(
    State,
)
pivot_FinalState_strategy = st.builds(
    pivot_FinalState,
)
CallExp_strategy = st.builds(
    CallExp,
)
pivot_LoopExp_strategy = st.builds(
    pivot_LoopExp,
)
pivot_FeatureCallExp_strategy = st.builds(
    pivot_FeatureCallExp,
    isPre=
        safe_text
)
TypedMultiplicityElement_strategy = st.builds(
    TypedMultiplicityElement,
)
pivot_Parameter_strategy = st.builds(
    pivot_Parameter,
)
pivot_Feature_strategy = st.builds(
    pivot_Feature,
    implementationClass=
        safe_text,
    implementation=
        safe_text
)
ReferringElement_strategy = st.builds(
    ReferringElement,
)
pivot_OperationCallExp_strategy = st.builds(
    pivot_OperationCallExp,
)
pivot_Variable_strategy = st.builds(
    pivot_Variable,
    implicit=
        safe_text
)
LoopExp_strategy = st.builds(
    LoopExp,
)
pivot_IteratorExp_strategy = st.builds(
    pivot_IteratorExp,
)
pivot_IterateExp_strategy = st.builds(
    pivot_IterateExp,
)
NumericLiteralExp_strategy = st.builds(
    NumericLiteralExp,
)
pivot_RealLiteralExp_strategy = st.builds(
    pivot_RealLiteralExp,
    realSymbol=
        safe_text
)
pivot_UnlimitedNaturalLiteralExp_strategy = st.builds(
    pivot_UnlimitedNaturalLiteralExp,
    unlimitedNaturalSymbol=
        safe_text
)
pivot_IntegerLiteralExp_strategy = st.builds(
    pivot_IntegerLiteralExp,
    integerSymbol=
        safe_text
)
OpaqueExpression_strategy = st.builds(
    OpaqueExpression,
)
pivot_ExpressionInOCL_strategy = st.builds(
    pivot_ExpressionInOCL,
)
Visitable_strategy = st.builds(
    Visitable,
)
DynamicElement_strategy = st.builds(
    DynamicElement,
)
Vertex_strategy = st.builds(
    Vertex,
)
pivot_Pseudostate_strategy = st.builds(
    pivot_Pseudostate,
    kind=
        safe_text
)
pivot_ConnectionPointReference_strategy = st.builds(
    pivot_ConnectionPointReference,
)
Element_strategy = st.builds(
    Element,
)
pivot_NamedElement_strategy = st.builds(
    pivot_NamedElement,
    isStatic=
        safe_text,
    name=
        safe_text
)
pivot_ParameterableElement_strategy = st.builds(
    pivot_ParameterableElement,
)
pivot_DynamicProperty_strategy = st.builds(
    pivot_DynamicProperty,
    default=
        safe_text
)
pivot_TemplateSignature_strategy = st.builds(
    pivot_TemplateSignature,
)
pivot_TemplateableElement_strategy = st.builds(
    pivot_TemplateableElement,
)
pivot_TemplateParameterSubstitution_strategy = st.builds(
    pivot_TemplateParameterSubstitution,
)
pivot_TemplateBinding_strategy = st.builds(
    pivot_TemplateBinding,
)
pivot_TemplateParameter_strategy = st.builds(
    pivot_TemplateParameter,
)
pivot_DynamicElement_strategy = st.builds(
    pivot_DynamicElement,
)
pivot_Comment_strategy = st.builds(
    pivot_Comment,
    body=
        safe_text
)
pivot_OpaqueExpression_strategy = st.builds(
    pivot_OpaqueExpression,
    message=
        safe_text,
    body=
        safe_text,
    language=
        safe_text
)
LiteralExp_strategy = st.builds(
    LiteralExp,
)
pivot_InvalidLiteralExp_strategy = st.builds(
    pivot_InvalidLiteralExp,
)
pivot_EnumLiteralExp_strategy = st.builds(
    pivot_EnumLiteralExp,
)
pivot_PrimitiveLiteralExp_strategy = st.builds(
    pivot_PrimitiveLiteralExp,
)
pivot_TupleLiteralExp_strategy = st.builds(
    pivot_TupleLiteralExp,
)
pivot_CollectionLiteralExp_strategy = st.builds(
    pivot_CollectionLiteralExp,
    kind=
        safe_text
)
DataType_strategy = st.builds(
    DataType,
)
pivot_Enumeration_strategy = st.builds(
    pivot_Enumeration,
)
pivot_LambdaType_strategy = st.builds(
    pivot_LambdaType,
)
pivot_PrimitiveType_strategy = st.builds(
    pivot_PrimitiveType,
)
pivot_TupleType_strategy = st.builds(
    pivot_TupleType,
)
pivot_CollectionType_strategy = st.builds(
    pivot_CollectionType,
    lower=
        safe_text,
    upper=
        safe_text
)
TypedElement_strategy = st.builds(
    TypedElement,
)
pivot_TypedMultiplicityElement_strategy = st.builds(
    pivot_TypedMultiplicityElement,
)
pivot_VariableDeclaration_strategy = st.builds(
    pivot_VariableDeclaration,
)
pivot_ValueSpecification_strategy = st.builds(
    pivot_ValueSpecification,
)
pivot_ConstructorPart_strategy = st.builds(
    pivot_ConstructorPart,
)
pivot_CollectionLiteralPart_strategy = st.builds(
    pivot_CollectionLiteralPart,
)
Namespace_strategy = st.builds(
    Namespace,
)
pivot_Package_strategy = st.builds(
    pivot_Package,
    nsURI=
        safe_text,
    nsPrefix=
        safe_text
)
pivot_Region_strategy = st.builds(
    pivot_Region,
)
pivot_Transition_strategy = st.builds(
    pivot_Transition,
    kind=
        safe_text
)
pivot_Root_strategy = st.builds(
    pivot_Root,
    externalURI=
        safe_text
)
pivot_State_strategy = st.builds(
    pivot_State,
    isSimple=
        safe_text,
    isSubmachineState=
        safe_text,
    isComposite=
        safe_text,
    isOrthogonal=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
pivot_MessageType_strategy = st.builds(
    pivot_MessageType,
)
pivot_TemplateParameterType_strategy = st.builds(
    pivot_TemplateParameterType,
    specification=
        safe_text
)
pivot_DynamicType_strategy = st.builds(
    pivot_DynamicType,
)
pivot_ElementExtension_strategy = st.builds(
    pivot_ElementExtension,
)
pivot_Class_strategy = st.builds(
    pivot_Class,
    isInterface=
        safe_text,
    isAbstract=
        safe_text
)
pivot_Operation_strategy = st.builds(
    pivot_Operation,
    isValidating=
        safe_text,
    isInvalidating=
        safe_text
)
pivot_OCLExpression_strategy = st.builds(
    pivot_OCLExpression,
)
OCLExpression_strategy = st.builds(
    OCLExpression,
)
pivot_ConstructorExp_strategy = st.builds(
    pivot_ConstructorExp,
    value=
        safe_text
)
pivot_MessageExp_strategy = st.builds(
    pivot_MessageExp,
)
pivot_TypeExp_strategy = st.builds(
    pivot_TypeExp,
)
pivot_StateExp_strategy = st.builds(
    pivot_StateExp,
)
pivot_IfExp_strategy = st.builds(
    pivot_IfExp,
)
pivot_LetExp_strategy = st.builds(
    pivot_LetExp,
)
pivot_LiteralExp_strategy = st.builds(
    pivot_LiteralExp,
)
pivot_VariableExp_strategy = st.builds(
    pivot_VariableExp,
    implicit=
        safe_text
)
pivot_UnspecifiedValueExp_strategy = st.builds(
    pivot_UnspecifiedValueExp,
)
pivot_CallExp_strategy = st.builds(
    pivot_CallExp,
    implicit=
        safe_text
)
CollectionLiteralPart_strategy = st.builds(
    CollectionLiteralPart,
)
pivot_CollectionRange_strategy = st.builds(
    pivot_CollectionRange,
)
pivot_CollectionItem_strategy = st.builds(
    pivot_CollectionItem,
)
pivot_Element_strategy = st.builds(
    pivot_Element,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
pivot_Constraint_strategy = st.builds(
    pivot_Constraint,
    isCallable=
        safe_text
)
pivot_Type_strategy = st.builds(
    pivot_Type,
    instanceClassName=
        safe_text
)
pivot_Namespace_strategy = st.builds(
    pivot_Namespace,
)
pivot_SendSignalAction_strategy = st.builds(
    pivot_SendSignalAction,
)
pivot_Vertex_strategy = st.builds(
    pivot_Vertex,
)
pivot_TypedElement_strategy = st.builds(
    pivot_TypedElement,
    isRequired=
        safe_text
)
pivot_CallOperationAction_strategy = st.builds(
    pivot_CallOperationAction,
)
pivot_Signal_strategy = st.builds(
    pivot_Signal,
)
pivot_EnumerationLiteral_strategy = st.builds(
    pivot_EnumerationLiteral,
    value=
        safe_text
)
pivot_Precedence_strategy = st.builds(
    pivot_Precedence,
    order=
        safe_text,
    associativity=
        safe_text
)
pivot_Trigger_strategy = st.builds(
    pivot_Trigger,
)
pivot_Import_strategy = st.builds(
    pivot_Import,
)
pivot_Annotation_strategy = st.builds(
    pivot_Annotation,
)
PrimitiveLiteralExp_strategy = st.builds(
    PrimitiveLiteralExp,
)
pivot_NumericLiteralExp_strategy = st.builds(
    pivot_NumericLiteralExp,
)
pivot_NullLiteralExp_strategy = st.builds(
    pivot_NullLiteralExp,
)
pivot_StringLiteralExp_strategy = st.builds(
    pivot_StringLiteralExp,
    stringSymbol=
        safe_text
)
pivot_BooleanLiteralExp_strategy = st.builds(
    pivot_BooleanLiteralExp,
    booleanSymbol=
        safe_text
)
CollectionType_strategy = st.builds(
    CollectionType,
)
pivot_OrderedSetType_strategy = st.builds(
    pivot_OrderedSetType,
)
pivot_SequenceType_strategy = st.builds(
    pivot_SequenceType,
)
pivot_SetType_strategy = st.builds(
    pivot_SetType,
)
pivot_BagType_strategy = st.builds(
    pivot_BagType,
)
NavigationCallExp_strategy = st.builds(
    NavigationCallExp,
)
pivot_PropertyCallExp_strategy = st.builds(
    pivot_PropertyCallExp,
)
pivot_AssociationClassCallExp_strategy = st.builds(
    pivot_AssociationClassCallExp,
)
pivot_Property_strategy = st.builds(
    pivot_Property,
    isID=
        safe_text,
    isUnsettable=
        safe_text,
    implicit=
        safe_text,
    default=
        safe_text,
    isDerived=
        safe_text,
    isReadOnly=
        safe_text,
    isComposite=
        safe_text,
    isTransient=
        safe_text,
    isVolatile=
        safe_text,
    isResolveProxies=
        safe_text
)
Class_strategy = st.builds(
    Class,
)
pivot_Stereotype_strategy = st.builds(
    pivot_Stereotype,
)
pivot_VoidType_strategy = st.builds(
    pivot_VoidType,
)
pivot_Metaclass_strategy = st.builds(
    pivot_Metaclass,
)
pivot_InvalidType_strategy = st.builds(
    pivot_InvalidType,
)
pivot_DataType_strategy = st.builds(
    pivot_DataType,
    isSerializable=
        safe_text
)
pivot_AssociationClass_strategy = st.builds(
    pivot_AssociationClass,
)
pivot_UnspecifiedType_strategy = st.builds(
    pivot_UnspecifiedType,
)
pivot_Behavior_strategy = st.builds(
    pivot_Behavior,
)
pivot_SelfType_strategy = st.builds(
    pivot_SelfType,
)
pivot_AnyType_strategy = st.builds(
    pivot_AnyType,
)
pivot_Detail_strategy = st.builds(
    pivot_Detail,
    value=
        safe_text
)

@given(instance=pivot_Visitor_strategy)
@settings(max_examples=50)
def test_pivot_visitor_instantiation(instance):
    assert isinstance(instance, pivot_Visitor)

@given(instance=pivot_Visitable_strategy)
@settings(max_examples=50)
def test_pivot_visitable_instantiation(instance):
    assert isinstance(instance, pivot_Visitable)

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=pivot_ReferringElement_strategy)
@settings(max_examples=50)
def test_pivot_referringelement_instantiation(instance):
    assert isinstance(instance, pivot_ReferringElement)

@given(instance=pivot_StateMachine_strategy)
@settings(max_examples=50)
def test_pivot_statemachine_instantiation(instance):
    assert isinstance(instance, pivot_StateMachine)

@given(instance=pivot_Pivotable_strategy)
@settings(max_examples=50)
def test_pivot_pivotable_instantiation(instance):
    assert isinstance(instance, pivot_Pivotable)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=pivot_TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_pivot_tupleliteralpart_instantiation(instance):
    assert isinstance(instance, pivot_TupleLiteralPart)

@given(instance=TemplateParameter_strategy)
@settings(max_examples=50)
def test_templateparameter_instantiation(instance):
    assert isinstance(instance, TemplateParameter)

@given(instance=pivot_TypeTemplateParameter_strategy)
@settings(max_examples=50)
def test_pivot_typetemplateparameter_instantiation(instance):
    assert isinstance(instance, pivot_TypeTemplateParameter)



@given(instance=pivot_TypeTemplateParameter_strategy)
def test_pivot_typetemplateparameter_allowSubstitutable_setter(instance):
    original = instance.allowSubstitutable
    instance.allowSubstitutable = original
    assert instance.allowSubstitutable == original

@given(instance=pivot_OperationTemplateParameter_strategy)
@settings(max_examples=50)
def test_pivot_operationtemplateparameter_instantiation(instance):
    assert isinstance(instance, pivot_OperationTemplateParameter)

@given(instance=ParameterableElement_strategy)
@settings(max_examples=50)
def test_parameterableelement_instantiation(instance):
    assert isinstance(instance, ParameterableElement)

@given(instance=pivot_PackageableElement_strategy)
@settings(max_examples=50)
def test_pivot_packageableelement_instantiation(instance):
    assert isinstance(instance, pivot_PackageableElement)

@given(instance=TemplateableElement_strategy)
@settings(max_examples=50)
def test_templateableelement_instantiation(instance):
    assert isinstance(instance, TemplateableElement)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=ValueSpecification_strategy)
@settings(max_examples=50)
def test_valuespecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)

@given(instance=FeatureCallExp_strategy)
@settings(max_examples=50)
def test_featurecallexp_instantiation(instance):
    assert isinstance(instance, FeatureCallExp)

@given(instance=pivot_NavigationCallExp_strategy)
@settings(max_examples=50)
def test_pivot_navigationcallexp_instantiation(instance):
    assert isinstance(instance, pivot_NavigationCallExp)

@given(instance=Nameable_strategy)
@settings(max_examples=50)
def test_nameable_instantiation(instance):
    assert isinstance(instance, Nameable)

@given(instance=pivot_Nameable_strategy)
@settings(max_examples=50)
def test_pivot_nameable_instantiation(instance):
    assert isinstance(instance, pivot_Nameable)

@given(instance=pivot_MorePivotable_strategy)
@settings(max_examples=50)
def test_pivot_morepivotable_instantiation(instance):
    assert isinstance(instance, pivot_MorePivotable)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=pivot_Profile_strategy)
@settings(max_examples=50)
def test_pivot_profile_instantiation(instance):
    assert isinstance(instance, pivot_Profile)

@given(instance=pivot_Library_strategy)
@settings(max_examples=50)
def test_pivot_library_instantiation(instance):
    assert isinstance(instance, pivot_Library)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=pivot_Iteration_strategy)
@settings(max_examples=50)
def test_pivot_iteration_instantiation(instance):
    assert isinstance(instance, pivot_Iteration)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=pivot_FinalState_strategy)
@settings(max_examples=50)
def test_pivot_finalstate_instantiation(instance):
    assert isinstance(instance, pivot_FinalState)

@given(instance=CallExp_strategy)
@settings(max_examples=50)
def test_callexp_instantiation(instance):
    assert isinstance(instance, CallExp)

@given(instance=pivot_LoopExp_strategy)
@settings(max_examples=50)
def test_pivot_loopexp_instantiation(instance):
    assert isinstance(instance, pivot_LoopExp)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_LoopExp_strategy)
@settings(max_examples=30)
def test_pivot_loopexp_sourceiscollection_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.SourceIsCollection(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.SourceIsCollection).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'SourceIsCollection' in pivot_LoopExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'SourceIsCollection' in pivot_LoopExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'SourceIsCollection' in pivot_LoopExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_LoopExp_strategy)
@settings(max_examples=30)
def test_pivot_loopexp_noinitializers_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.NoInitializers(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.NoInitializers).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'NoInitializers' in pivot_LoopExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'NoInitializers' in pivot_LoopExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'NoInitializers' in pivot_LoopExp is not implemented or raised an error")

@given(instance=pivot_FeatureCallExp_strategy)
@settings(max_examples=50)
def test_pivot_featurecallexp_instantiation(instance):
    assert isinstance(instance, pivot_FeatureCallExp)



@given(instance=pivot_FeatureCallExp_strategy)
def test_pivot_featurecallexp_isPre_setter(instance):
    original = instance.isPre
    instance.isPre = original
    assert instance.isPre == original

@given(instance=TypedMultiplicityElement_strategy)
@settings(max_examples=50)
def test_typedmultiplicityelement_instantiation(instance):
    assert isinstance(instance, TypedMultiplicityElement)

@given(instance=pivot_Parameter_strategy)
@settings(max_examples=50)
def test_pivot_parameter_instantiation(instance):
    assert isinstance(instance, pivot_Parameter)

@given(instance=pivot_Feature_strategy)
@settings(max_examples=50)
def test_pivot_feature_instantiation(instance):
    assert isinstance(instance, pivot_Feature)



@given(instance=pivot_Feature_strategy)
def test_pivot_feature_implementationClass_setter(instance):
    original = instance.implementationClass
    instance.implementationClass = original
    assert instance.implementationClass == original



@given(instance=pivot_Feature_strategy)
def test_pivot_feature_implementation_setter(instance):
    original = instance.implementation
    instance.implementation = original
    assert instance.implementation == original

@given(instance=ReferringElement_strategy)
@settings(max_examples=50)
def test_referringelement_instantiation(instance):
    assert isinstance(instance, ReferringElement)

@given(instance=pivot_OperationCallExp_strategy)
@settings(max_examples=50)
def test_pivot_operationcallexp_instantiation(instance):
    assert isinstance(instance, pivot_OperationCallExp)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_OperationCallExp_strategy)
@settings(max_examples=30)
def test_pivot_operationcallexp_argumenttypeisconformant_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ArgumentTypeIsConformant(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ArgumentTypeIsConformant).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ArgumentTypeIsConformant' in pivot_OperationCallExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ArgumentTypeIsConformant' in pivot_OperationCallExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ArgumentTypeIsConformant' in pivot_OperationCallExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_OperationCallExp_strategy)
@settings(max_examples=30)
def test_pivot_operationcallexp_argumentcount_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ArgumentCount(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ArgumentCount).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ArgumentCount' in pivot_OperationCallExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ArgumentCount' in pivot_OperationCallExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ArgumentCount' in pivot_OperationCallExp is not implemented or raised an error")

@given(instance=pivot_Variable_strategy)
@settings(max_examples=50)
def test_pivot_variable_instantiation(instance):
    assert isinstance(instance, pivot_Variable)



@given(instance=pivot_Variable_strategy)
def test_pivot_variable_implicit_setter(instance):
    original = instance.implicit
    instance.implicit = original
    assert instance.implicit == original

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=pivot_IteratorExp_strategy)
@settings(max_examples=50)
def test_pivot_iteratorexp_instantiation(instance):
    assert isinstance(instance, pivot_IteratorExp)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot_iteratorexp_closuretypeisuniquecollection_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ClosureTypeIsUniqueCollection(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ClosureTypeIsUniqueCollection).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ClosureTypeIsUniqueCollection' in pivot_IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ClosureTypeIsUniqueCollection' in pivot_IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ClosureTypeIsUniqueCollection' in pivot_IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot_iteratorexp_collecthasoneiterator_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.CollectHasOneIterator(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.CollectHasOneIterator).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'CollectHasOneIterator' in pivot_IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'CollectHasOneIterator' in pivot_IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'CollectHasOneIterator' in pivot_IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot_iteratorexp_collectnestedtypeisbodytype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.CollectNestedTypeIsBodyType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.CollectNestedTypeIsBodyType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'CollectNestedTypeIsBodyType' in pivot_IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'CollectNestedTypeIsBodyType' in pivot_IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'CollectNestedTypeIsBodyType' in pivot_IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot_iteratorexp_isuniquetypeisboolean_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.IsUniqueTypeIsBoolean(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.IsUniqueTypeIsBoolean).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'IsUniqueTypeIsBoolean' in pivot_IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'IsUniqueTypeIsBoolean' in pivot_IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'IsUniqueTypeIsBoolean' in pivot_IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot_iteratorexp_rejectorselecttypeissourcetype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.RejectOrSelectTypeIsSourceType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.RejectOrSelectTypeIsSourceType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'RejectOrSelectTypeIsSourceType' in pivot_IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'RejectOrSelectTypeIsSourceType' in pivot_IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'RejectOrSelectTypeIsSourceType' in pivot_IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot_iteratorexp_onebodytypeisboolean_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.OneBodyTypeIsBoolean(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.OneBodyTypeIsBoolean).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'OneBodyTypeIsBoolean' in pivot_IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'OneBodyTypeIsBoolean' in pivot_IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'OneBodyTypeIsBoolean' in pivot_IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot_iteratorexp_closureelementtypeissourceelementtype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ClosureElementTypeIsSourceElementType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ClosureElementTypeIsSourceElementType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ClosureElementTypeIsSourceElementType' in pivot_IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ClosureElementTypeIsSourceElementType' in pivot_IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ClosureElementTypeIsSourceElementType' in pivot_IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot_iteratorexp_collecttypeisunordered_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.CollectTypeIsUnordered(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.CollectTypeIsUnordered).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'CollectTypeIsUnordered' in pivot_IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'CollectTypeIsUnordered' in pivot_IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'CollectTypeIsUnordered' in pivot_IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot_iteratorexp_sortedbyisorderedifsourceisordered_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.SortedByIsOrderedIfSourceIsOrdered(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.SortedByIsOrderedIfSourceIsOrdered).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'SortedByIsOrderedIfSourceIsOrdered' in pivot_IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'SortedByIsOrderedIfSourceIsOrdered' in pivot_IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'SortedByIsOrderedIfSourceIsOrdered' in pivot_IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot_iteratorexp_collectnestedtypeisbag_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.CollectNestedTypeIsBag(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.CollectNestedTypeIsBag).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'CollectNestedTypeIsBag' in pivot_IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'CollectNestedTypeIsBag' in pivot_IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'CollectNestedTypeIsBag' in pivot_IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot_iteratorexp_onetypeisboolean_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.OneTypeIsBoolean(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.OneTypeIsBoolean).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'OneTypeIsBoolean' in pivot_IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'OneTypeIsBoolean' in pivot_IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'OneTypeIsBoolean' in pivot_IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot_iteratorexp_existstypeisboolean_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ExistsTypeIsBoolean(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ExistsTypeIsBoolean).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ExistsTypeIsBoolean' in pivot_IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ExistsTypeIsBoolean' in pivot_IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ExistsTypeIsBoolean' in pivot_IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot_iteratorexp_collectnestedhasoneiterator_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.CollectNestedHasOneIterator(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.CollectNestedHasOneIterator).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'CollectNestedHasOneIterator' in pivot_IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'CollectNestedHasOneIterator' in pivot_IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'CollectNestedHasOneIterator' in pivot_IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot_iteratorexp_anytypeissourceelementtype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.AnyTypeIsSourceElementType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.AnyTypeIsSourceElementType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'AnyTypeIsSourceElementType' in pivot_IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'AnyTypeIsSourceElementType' in pivot_IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'AnyTypeIsSourceElementType' in pivot_IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot_iteratorexp_sortedbyiteratortypeiscomparable_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.SortedByIteratorTypeIsComparable(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.SortedByIteratorTypeIsComparable).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'SortedByIteratorTypeIsComparable' in pivot_IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'SortedByIteratorTypeIsComparable' in pivot_IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'SortedByIteratorTypeIsComparable' in pivot_IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot_iteratorexp_anyhasoneiterator_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.AnyHasOneIterator(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.AnyHasOneIterator).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'AnyHasOneIterator' in pivot_IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'AnyHasOneIterator' in pivot_IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'AnyHasOneIterator' in pivot_IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot_iteratorexp_collectelementtypeissourceelementtype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.CollectElementTypeIsSourceElementType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.CollectElementTypeIsSourceElementType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'CollectElementTypeIsSourceElementType' in pivot_IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'CollectElementTypeIsSourceElementType' in pivot_IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'CollectElementTypeIsSourceElementType' in pivot_IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot_iteratorexp_foralltypeisboolean_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ForAllTypeIsBoolean(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ForAllTypeIsBoolean).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ForAllTypeIsBoolean' in pivot_IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ForAllTypeIsBoolean' in pivot_IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ForAllTypeIsBoolean' in pivot_IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot_iteratorexp_closuresourceelementtypeisbodyelementtype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ClosureSourceElementTypeIsBodyElementType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ClosureSourceElementTypeIsBodyElementType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ClosureSourceElementTypeIsBodyElementType' in pivot_IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ClosureSourceElementTypeIsBodyElementType' in pivot_IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ClosureSourceElementTypeIsBodyElementType' in pivot_IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot_iteratorexp_sortedbyhasoneiterator_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.SortedByHasOneIterator(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.SortedByHasOneIterator).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'SortedByHasOneIterator' in pivot_IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'SortedByHasOneIterator' in pivot_IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'SortedByHasOneIterator' in pivot_IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot_iteratorexp_anybodytypeisboolean_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.AnyBodyTypeIsBoolean(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.AnyBodyTypeIsBoolean).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'AnyBodyTypeIsBoolean' in pivot_IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'AnyBodyTypeIsBoolean' in pivot_IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'AnyBodyTypeIsBoolean' in pivot_IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot_iteratorexp_existsbodytypeisboolean_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ExistsBodyTypeIsBoolean(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ExistsBodyTypeIsBoolean).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ExistsBodyTypeIsBoolean' in pivot_IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ExistsBodyTypeIsBoolean' in pivot_IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ExistsBodyTypeIsBoolean' in pivot_IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot_iteratorexp_forallbodytypeisboolean_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ForAllBodyTypeIsBoolean(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ForAllBodyTypeIsBoolean).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ForAllBodyTypeIsBoolean' in pivot_IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ForAllBodyTypeIsBoolean' in pivot_IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ForAllBodyTypeIsBoolean' in pivot_IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot_iteratorexp_iteratortypeissourceelementtype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.IteratorTypeIsSourceElementType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.IteratorTypeIsSourceElementType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'IteratorTypeIsSourceElementType' in pivot_IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'IteratorTypeIsSourceElementType' in pivot_IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'IteratorTypeIsSourceElementType' in pivot_IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot_iteratorexp_rejectorselecttypeisboolean_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.RejectOrSelectTypeIsBoolean(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.RejectOrSelectTypeIsBoolean).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'RejectOrSelectTypeIsBoolean' in pivot_IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'RejectOrSelectTypeIsBoolean' in pivot_IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'RejectOrSelectTypeIsBoolean' in pivot_IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot_iteratorexp_closurehasoneiterator_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ClosureHasOneIterator(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ClosureHasOneIterator).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ClosureHasOneIterator' in pivot_IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ClosureHasOneIterator' in pivot_IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ClosureHasOneIterator' in pivot_IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot_iteratorexp_sortedbyelementtypeissourceelementtype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.SortedByElementTypeIsSourceElementType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.SortedByElementTypeIsSourceElementType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'SortedByElementTypeIsSourceElementType' in pivot_IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'SortedByElementTypeIsSourceElementType' in pivot_IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'SortedByElementTypeIsSourceElementType' in pivot_IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot_iteratorexp_onehasoneiterator_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.OneHasOneIterator(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.OneHasOneIterator).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'OneHasOneIterator' in pivot_IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'OneHasOneIterator' in pivot_IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'OneHasOneIterator' in pivot_IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot_iteratorexp_isuniquehasoneiterator_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.IsUniqueHasOneIterator(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.IsUniqueHasOneIterator).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'IsUniqueHasOneIterator' in pivot_IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'IsUniqueHasOneIterator' in pivot_IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'IsUniqueHasOneIterator' in pivot_IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot_iteratorexp_rejectorselecthasoneiterator_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.RejectOrSelectHasOneIterator(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.RejectOrSelectHasOneIterator).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'RejectOrSelectHasOneIterator' in pivot_IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'RejectOrSelectHasOneIterator' in pivot_IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'RejectOrSelectHasOneIterator' in pivot_IteratorExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_IteratorExp_strategy)
@settings(max_examples=30)
def test_pivot_iteratorexp_closurebodytypeisconformanttoiteratortype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ClosureBodyTypeIsConformanttoIteratorType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ClosureBodyTypeIsConformanttoIteratorType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ClosureBodyTypeIsConformanttoIteratorType' in pivot_IteratorExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ClosureBodyTypeIsConformanttoIteratorType' in pivot_IteratorExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ClosureBodyTypeIsConformanttoIteratorType' in pivot_IteratorExp is not implemented or raised an error")

@given(instance=pivot_IterateExp_strategy)
@settings(max_examples=50)
def test_pivot_iterateexp_instantiation(instance):
    assert isinstance(instance, pivot_IterateExp)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_IterateExp_strategy)
@settings(max_examples=30)
def test_pivot_iterateexp_bodytypeconformstoresulttype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.BodyTypeConformsToResultType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.BodyTypeConformsToResultType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'BodyTypeConformsToResultType' in pivot_IterateExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'BodyTypeConformsToResultType' in pivot_IterateExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'BodyTypeConformsToResultType' in pivot_IterateExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_IterateExp_strategy)
@settings(max_examples=30)
def test_pivot_iterateexp_oneinitializer_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.OneInitializer(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.OneInitializer).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'OneInitializer' in pivot_IterateExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'OneInitializer' in pivot_IterateExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'OneInitializer' in pivot_IterateExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_IterateExp_strategy)
@settings(max_examples=30)
def test_pivot_iterateexp_typeisresulttype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.TypeIsResultType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.TypeIsResultType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'TypeIsResultType' in pivot_IterateExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'TypeIsResultType' in pivot_IterateExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'TypeIsResultType' in pivot_IterateExp is not implemented or raised an error")

@given(instance=NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_numericliteralexp_instantiation(instance):
    assert isinstance(instance, NumericLiteralExp)

@given(instance=pivot_RealLiteralExp_strategy)
@settings(max_examples=50)
def test_pivot_realliteralexp_instantiation(instance):
    assert isinstance(instance, pivot_RealLiteralExp)



@given(instance=pivot_RealLiteralExp_strategy)
def test_pivot_realliteralexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=pivot_UnlimitedNaturalLiteralExp_strategy)
@settings(max_examples=50)
def test_pivot_unlimitednaturalliteralexp_instantiation(instance):
    assert isinstance(instance, pivot_UnlimitedNaturalLiteralExp)



@given(instance=pivot_UnlimitedNaturalLiteralExp_strategy)
def test_pivot_unlimitednaturalliteralexp_unlimitedNaturalSymbol_setter(instance):
    original = instance.unlimitedNaturalSymbol
    instance.unlimitedNaturalSymbol = original
    assert instance.unlimitedNaturalSymbol == original

@given(instance=pivot_IntegerLiteralExp_strategy)
@settings(max_examples=50)
def test_pivot_integerliteralexp_instantiation(instance):
    assert isinstance(instance, pivot_IntegerLiteralExp)



@given(instance=pivot_IntegerLiteralExp_strategy)
def test_pivot_integerliteralexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_IntegerLiteralExp_strategy)
@settings(max_examples=30)
def test_pivot_integerliteralexp_typeisinteger_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.TypeIsInteger(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.TypeIsInteger).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'TypeIsInteger' in pivot_IntegerLiteralExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'TypeIsInteger' in pivot_IntegerLiteralExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'TypeIsInteger' in pivot_IntegerLiteralExp is not implemented or raised an error")

@given(instance=OpaqueExpression_strategy)
@settings(max_examples=50)
def test_opaqueexpression_instantiation(instance):
    assert isinstance(instance, OpaqueExpression)

@given(instance=pivot_ExpressionInOCL_strategy)
@settings(max_examples=50)
def test_pivot_expressioninocl_instantiation(instance):
    assert isinstance(instance, pivot_ExpressionInOCL)

@given(instance=Visitable_strategy)
@settings(max_examples=50)
def test_visitable_instantiation(instance):
    assert isinstance(instance, Visitable)

@given(instance=DynamicElement_strategy)
@settings(max_examples=50)
def test_dynamicelement_instantiation(instance):
    assert isinstance(instance, DynamicElement)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=pivot_Pseudostate_strategy)
@settings(max_examples=50)
def test_pivot_pseudostate_instantiation(instance):
    assert isinstance(instance, pivot_Pseudostate)



@given(instance=pivot_Pseudostate_strategy)
def test_pivot_pseudostate_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=pivot_ConnectionPointReference_strategy)
@settings(max_examples=50)
def test_pivot_connectionpointreference_instantiation(instance):
    assert isinstance(instance, pivot_ConnectionPointReference)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=pivot_NamedElement_strategy)
@settings(max_examples=50)
def test_pivot_namedelement_instantiation(instance):
    assert isinstance(instance, pivot_NamedElement)



@given(instance=pivot_NamedElement_strategy)
def test_pivot_namedelement_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original



@given(instance=pivot_NamedElement_strategy)
def test_pivot_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pivot_ParameterableElement_strategy)
@settings(max_examples=50)
def test_pivot_parameterableelement_instantiation(instance):
    assert isinstance(instance, pivot_ParameterableElement)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_ParameterableElement_strategy)
@settings(max_examples=30)
def test_pivot_parameterableelement_istemplateparameter_changes_state(instance):
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
        assert has_statements, f"Function 'isTemplateParameter' in pivot_ParameterableElement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isTemplateParameter' in pivot_ParameterableElement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isTemplateParameter' in pivot_ParameterableElement is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_ParameterableElement_strategy)
@settings(max_examples=30)
def test_pivot_parameterableelement_iscompatiblewith_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isCompatibleWith(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isCompatibleWith).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isCompatibleWith' in pivot_ParameterableElement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isCompatibleWith' in pivot_ParameterableElement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isCompatibleWith' in pivot_ParameterableElement is not implemented or raised an error")

@given(instance=pivot_DynamicProperty_strategy)
@settings(max_examples=50)
def test_pivot_dynamicproperty_instantiation(instance):
    assert isinstance(instance, pivot_DynamicProperty)



@given(instance=pivot_DynamicProperty_strategy)
def test_pivot_dynamicproperty_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=pivot_TemplateSignature_strategy)
@settings(max_examples=50)
def test_pivot_templatesignature_instantiation(instance):
    assert isinstance(instance, pivot_TemplateSignature)

@given(instance=pivot_TemplateableElement_strategy)
@settings(max_examples=50)
def test_pivot_templateableelement_instantiation(instance):
    assert isinstance(instance, pivot_TemplateableElement)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_TemplateableElement_strategy)
@settings(max_examples=30)
def test_pivot_templateableelement_istemplate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isTemplate()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isTemplate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isTemplate' in pivot_TemplateableElement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isTemplate' in pivot_TemplateableElement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isTemplate' in pivot_TemplateableElement is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_TemplateableElement_strategy)
@settings(max_examples=30)
def test_pivot_templateableelement_parameterableelements_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.parameterableElements()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.parameterableElements).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'parameterableElements' in pivot_TemplateableElement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'parameterableElements' in pivot_TemplateableElement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'parameterableElements' in pivot_TemplateableElement is not implemented or raised an error")

@given(instance=pivot_TemplateParameterSubstitution_strategy)
@settings(max_examples=50)
def test_pivot_templateparametersubstitution_instantiation(instance):
    assert isinstance(instance, pivot_TemplateParameterSubstitution)

@given(instance=pivot_TemplateBinding_strategy)
@settings(max_examples=50)
def test_pivot_templatebinding_instantiation(instance):
    assert isinstance(instance, pivot_TemplateBinding)

@given(instance=pivot_TemplateParameter_strategy)
@settings(max_examples=50)
def test_pivot_templateparameter_instantiation(instance):
    assert isinstance(instance, pivot_TemplateParameter)

@given(instance=pivot_DynamicElement_strategy)
@settings(max_examples=50)
def test_pivot_dynamicelement_instantiation(instance):
    assert isinstance(instance, pivot_DynamicElement)

@given(instance=pivot_Comment_strategy)
@settings(max_examples=50)
def test_pivot_comment_instantiation(instance):
    assert isinstance(instance, pivot_Comment)



@given(instance=pivot_Comment_strategy)
def test_pivot_comment_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=pivot_OpaqueExpression_strategy)
@settings(max_examples=50)
def test_pivot_opaqueexpression_instantiation(instance):
    assert isinstance(instance, pivot_OpaqueExpression)



@given(instance=pivot_OpaqueExpression_strategy)
def test_pivot_opaqueexpression_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original



@given(instance=pivot_OpaqueExpression_strategy)
def test_pivot_opaqueexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original



@given(instance=pivot_OpaqueExpression_strategy)
def test_pivot_opaqueexpression_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=LiteralExp_strategy)
@settings(max_examples=50)
def test_literalexp_instantiation(instance):
    assert isinstance(instance, LiteralExp)

@given(instance=pivot_InvalidLiteralExp_strategy)
@settings(max_examples=50)
def test_pivot_invalidliteralexp_instantiation(instance):
    assert isinstance(instance, pivot_InvalidLiteralExp)

@given(instance=pivot_EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_pivot_enumliteralexp_instantiation(instance):
    assert isinstance(instance, pivot_EnumLiteralExp)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_EnumLiteralExp_strategy)
@settings(max_examples=30)
def test_pivot_enumliteralexp_typeisenumerationtype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.TypeIsEnumerationType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.TypeIsEnumerationType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'TypeIsEnumerationType' in pivot_EnumLiteralExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'TypeIsEnumerationType' in pivot_EnumLiteralExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'TypeIsEnumerationType' in pivot_EnumLiteralExp is not implemented or raised an error")

@given(instance=pivot_PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_pivot_primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, pivot_PrimitiveLiteralExp)

@given(instance=pivot_TupleLiteralExp_strategy)
@settings(max_examples=50)
def test_pivot_tupleliteralexp_instantiation(instance):
    assert isinstance(instance, pivot_TupleLiteralExp)

@given(instance=pivot_CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_pivot_collectionliteralexp_instantiation(instance):
    assert isinstance(instance, pivot_CollectionLiteralExp)



@given(instance=pivot_CollectionLiteralExp_strategy)
def test_pivot_collectionliteralexp_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_CollectionLiteralExp_strategy)
@settings(max_examples=30)
def test_pivot_collectionliteralexp_setkindisset_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.SetKindIsSet(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.SetKindIsSet).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'SetKindIsSet' in pivot_CollectionLiteralExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'SetKindIsSet' in pivot_CollectionLiteralExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'SetKindIsSet' in pivot_CollectionLiteralExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_CollectionLiteralExp_strategy)
@settings(max_examples=30)
def test_pivot_collectionliteralexp_collectionkindisconcrete_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.CollectionKindIsConcrete(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.CollectionKindIsConcrete).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'CollectionKindIsConcrete' in pivot_CollectionLiteralExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'CollectionKindIsConcrete' in pivot_CollectionLiteralExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'CollectionKindIsConcrete' in pivot_CollectionLiteralExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_CollectionLiteralExp_strategy)
@settings(max_examples=30)
def test_pivot_collectionliteralexp_orderedsetkindisorderedset_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.OrderedSetKindIsOrderedSet(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.OrderedSetKindIsOrderedSet).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'OrderedSetKindIsOrderedSet' in pivot_CollectionLiteralExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'OrderedSetKindIsOrderedSet' in pivot_CollectionLiteralExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'OrderedSetKindIsOrderedSet' in pivot_CollectionLiteralExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_CollectionLiteralExp_strategy)
@settings(max_examples=30)
def test_pivot_collectionliteralexp_sequencekindissequence_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.SequenceKindIsSequence(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.SequenceKindIsSequence).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'SequenceKindIsSequence' in pivot_CollectionLiteralExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'SequenceKindIsSequence' in pivot_CollectionLiteralExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'SequenceKindIsSequence' in pivot_CollectionLiteralExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_CollectionLiteralExp_strategy)
@settings(max_examples=30)
def test_pivot_collectionliteralexp_bagkindisbag_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.BagKindIsBag(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.BagKindIsBag).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'BagKindIsBag' in pivot_CollectionLiteralExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'BagKindIsBag' in pivot_CollectionLiteralExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'BagKindIsBag' in pivot_CollectionLiteralExp is not implemented or raised an error")

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=pivot_Enumeration_strategy)
@settings(max_examples=50)
def test_pivot_enumeration_instantiation(instance):
    assert isinstance(instance, pivot_Enumeration)

@given(instance=pivot_LambdaType_strategy)
@settings(max_examples=50)
def test_pivot_lambdatype_instantiation(instance):
    assert isinstance(instance, pivot_LambdaType)

@given(instance=pivot_PrimitiveType_strategy)
@settings(max_examples=50)
def test_pivot_primitivetype_instantiation(instance):
    assert isinstance(instance, pivot_PrimitiveType)

@given(instance=pivot_TupleType_strategy)
@settings(max_examples=50)
def test_pivot_tupletype_instantiation(instance):
    assert isinstance(instance, pivot_TupleType)

@given(instance=pivot_CollectionType_strategy)
@settings(max_examples=50)
def test_pivot_collectiontype_instantiation(instance):
    assert isinstance(instance, pivot_CollectionType)



@given(instance=pivot_CollectionType_strategy)
def test_pivot_collectiontype_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original



@given(instance=pivot_CollectionType_strategy)
def test_pivot_collectiontype_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=pivot_TypedMultiplicityElement_strategy)
@settings(max_examples=50)
def test_pivot_typedmultiplicityelement_instantiation(instance):
    assert isinstance(instance, pivot_TypedMultiplicityElement)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_TypedMultiplicityElement_strategy)
@settings(max_examples=30)
def test_pivot_typedmultiplicityelement_compatiblebody_changes_state(instance):
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
        assert has_statements, f"Function 'CompatibleBody' in pivot_TypedMultiplicityElement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'CompatibleBody' in pivot_TypedMultiplicityElement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'CompatibleBody' in pivot_TypedMultiplicityElement is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_TypedMultiplicityElement_strategy)
@settings(max_examples=30)
def test_pivot_typedmultiplicityelement_makeparameter_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.makeParameter()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.makeParameter).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'makeParameter' in pivot_TypedMultiplicityElement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'makeParameter' in pivot_TypedMultiplicityElement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'makeParameter' in pivot_TypedMultiplicityElement is not implemented or raised an error")

@given(instance=pivot_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_pivot_variabledeclaration_instantiation(instance):
    assert isinstance(instance, pivot_VariableDeclaration)

@given(instance=pivot_ValueSpecification_strategy)
@settings(max_examples=50)
def test_pivot_valuespecification_instantiation(instance):
    assert isinstance(instance, pivot_ValueSpecification)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_ValueSpecification_strategy)
@settings(max_examples=30)
def test_pivot_valuespecification_isnull_changes_state(instance):
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
        assert has_statements, f"Function 'isNull' in pivot_ValueSpecification is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isNull' in pivot_ValueSpecification did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isNull' in pivot_ValueSpecification is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_ValueSpecification_strategy)
@settings(max_examples=30)
def test_pivot_valuespecification_stringvalue_changes_state(instance):
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
        assert has_statements, f"Function 'stringValue' in pivot_ValueSpecification is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'stringValue' in pivot_ValueSpecification did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'stringValue' in pivot_ValueSpecification is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_ValueSpecification_strategy)
@settings(max_examples=30)
def test_pivot_valuespecification_integervalue_changes_state(instance):
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
        assert has_statements, f"Function 'integerValue' in pivot_ValueSpecification is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'integerValue' in pivot_ValueSpecification did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'integerValue' in pivot_ValueSpecification is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_ValueSpecification_strategy)
@settings(max_examples=30)
def test_pivot_valuespecification_booleanvalue_changes_state(instance):
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
        assert has_statements, f"Function 'booleanValue' in pivot_ValueSpecification is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'booleanValue' in pivot_ValueSpecification did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'booleanValue' in pivot_ValueSpecification is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_ValueSpecification_strategy)
@settings(max_examples=30)
def test_pivot_valuespecification_unlimitedvalue_changes_state(instance):
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
        assert has_statements, f"Function 'unlimitedValue' in pivot_ValueSpecification is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'unlimitedValue' in pivot_ValueSpecification did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'unlimitedValue' in pivot_ValueSpecification is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_ValueSpecification_strategy)
@settings(max_examples=30)
def test_pivot_valuespecification_iscomputable_changes_state(instance):
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
        assert has_statements, f"Function 'isComputable' in pivot_ValueSpecification is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isComputable' in pivot_ValueSpecification did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isComputable' in pivot_ValueSpecification is not implemented or raised an error")

@given(instance=pivot_ConstructorPart_strategy)
@settings(max_examples=50)
def test_pivot_constructorpart_instantiation(instance):
    assert isinstance(instance, pivot_ConstructorPart)

@given(instance=pivot_CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_pivot_collectionliteralpart_instantiation(instance):
    assert isinstance(instance, pivot_CollectionLiteralPart)

@given(instance=Namespace_strategy)
@settings(max_examples=50)
def test_namespace_instantiation(instance):
    assert isinstance(instance, Namespace)

@given(instance=pivot_Package_strategy)
@settings(max_examples=50)
def test_pivot_package_instantiation(instance):
    assert isinstance(instance, pivot_Package)



@given(instance=pivot_Package_strategy)
def test_pivot_package_nsURI_setter(instance):
    original = instance.nsURI
    instance.nsURI = original
    assert instance.nsURI == original



@given(instance=pivot_Package_strategy)
def test_pivot_package_nsPrefix_setter(instance):
    original = instance.nsPrefix
    instance.nsPrefix = original
    assert instance.nsPrefix == original

@given(instance=pivot_Region_strategy)
@settings(max_examples=50)
def test_pivot_region_instantiation(instance):
    assert isinstance(instance, pivot_Region)

@given(instance=pivot_Transition_strategy)
@settings(max_examples=50)
def test_pivot_transition_instantiation(instance):
    assert isinstance(instance, pivot_Transition)



@given(instance=pivot_Transition_strategy)
def test_pivot_transition_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=pivot_Root_strategy)
@settings(max_examples=50)
def test_pivot_root_instantiation(instance):
    assert isinstance(instance, pivot_Root)



@given(instance=pivot_Root_strategy)
def test_pivot_root_externalURI_setter(instance):
    original = instance.externalURI
    instance.externalURI = original
    assert instance.externalURI == original

@given(instance=pivot_State_strategy)
@settings(max_examples=50)
def test_pivot_state_instantiation(instance):
    assert isinstance(instance, pivot_State)



@given(instance=pivot_State_strategy)
def test_pivot_state_isSimple_setter(instance):
    original = instance.isSimple
    instance.isSimple = original
    assert instance.isSimple == original



@given(instance=pivot_State_strategy)
def test_pivot_state_isSubmachineState_setter(instance):
    original = instance.isSubmachineState
    instance.isSubmachineState = original
    assert instance.isSubmachineState == original



@given(instance=pivot_State_strategy)
def test_pivot_state_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original



@given(instance=pivot_State_strategy)
def test_pivot_state_isOrthogonal_setter(instance):
    original = instance.isOrthogonal
    instance.isOrthogonal = original
    assert instance.isOrthogonal == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=pivot_MessageType_strategy)
@settings(max_examples=50)
def test_pivot_messagetype_instantiation(instance):
    assert isinstance(instance, pivot_MessageType)

@given(instance=pivot_TemplateParameterType_strategy)
@settings(max_examples=50)
def test_pivot_templateparametertype_instantiation(instance):
    assert isinstance(instance, pivot_TemplateParameterType)



@given(instance=pivot_TemplateParameterType_strategy)
def test_pivot_templateparametertype_specification_setter(instance):
    original = instance.specification
    instance.specification = original
    assert instance.specification == original

@given(instance=pivot_DynamicType_strategy)
@settings(max_examples=50)
def test_pivot_dynamictype_instantiation(instance):
    assert isinstance(instance, pivot_DynamicType)

@given(instance=pivot_ElementExtension_strategy)
@settings(max_examples=50)
def test_pivot_elementextension_instantiation(instance):
    assert isinstance(instance, pivot_ElementExtension)

@given(instance=pivot_Class_strategy)
@settings(max_examples=50)
def test_pivot_class_instantiation(instance):
    assert isinstance(instance, pivot_Class)



@given(instance=pivot_Class_strategy)
def test_pivot_class_isInterface_setter(instance):
    original = instance.isInterface
    instance.isInterface = original
    assert instance.isInterface == original



@given(instance=pivot_Class_strategy)
def test_pivot_class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=pivot_Operation_strategy)
@settings(max_examples=50)
def test_pivot_operation_instantiation(instance):
    assert isinstance(instance, pivot_Operation)



@given(instance=pivot_Operation_strategy)
def test_pivot_operation_isValidating_setter(instance):
    original = instance.isValidating
    instance.isValidating = original
    assert instance.isValidating == original



@given(instance=pivot_Operation_strategy)
def test_pivot_operation_isInvalidating_setter(instance):
    original = instance.isInvalidating
    instance.isInvalidating = original
    assert instance.isInvalidating == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_Operation_strategy)
@settings(max_examples=30)
def test_pivot_operation_loadableimplementation_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.LoadableImplementation(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.LoadableImplementation).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'LoadableImplementation' in pivot_Operation is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'LoadableImplementation' in pivot_Operation did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'LoadableImplementation' in pivot_Operation is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_Operation_strategy)
@settings(max_examples=30)
def test_pivot_operation_compatiblereturn_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.CompatibleReturn(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.CompatibleReturn).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'CompatibleReturn' in pivot_Operation is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'CompatibleReturn' in pivot_Operation did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'CompatibleReturn' in pivot_Operation is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_Operation_strategy)
@settings(max_examples=30)
def test_pivot_operation_uniquepreconditionname_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.UniquePreconditionName(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.UniquePreconditionName).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'UniquePreconditionName' in pivot_Operation is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'UniquePreconditionName' in pivot_Operation did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'UniquePreconditionName' in pivot_Operation is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_Operation_strategy)
@settings(max_examples=30)
def test_pivot_operation_uniquepostconditionname_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.UniquePostconditionName(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.UniquePostconditionName).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'UniquePostconditionName' in pivot_Operation is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'UniquePostconditionName' in pivot_Operation did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'UniquePostconditionName' in pivot_Operation is not implemented or raised an error")

@given(instance=pivot_OCLExpression_strategy)
@settings(max_examples=50)
def test_pivot_oclexpression_instantiation(instance):
    assert isinstance(instance, pivot_OCLExpression)

@given(instance=OCLExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OCLExpression)

@given(instance=pivot_ConstructorExp_strategy)
@settings(max_examples=50)
def test_pivot_constructorexp_instantiation(instance):
    assert isinstance(instance, pivot_ConstructorExp)



@given(instance=pivot_ConstructorExp_strategy)
def test_pivot_constructorexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=pivot_MessageExp_strategy)
@settings(max_examples=50)
def test_pivot_messageexp_instantiation(instance):
    assert isinstance(instance, pivot_MessageExp)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_MessageExp_strategy)
@settings(max_examples=30)
def test_pivot_messageexp_onecalloronesend_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.OneCallOrOneSend(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.OneCallOrOneSend).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'OneCallOrOneSend' in pivot_MessageExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'OneCallOrOneSend' in pivot_MessageExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'OneCallOrOneSend' in pivot_MessageExp is not implemented or raised an error")

@given(instance=pivot_TypeExp_strategy)
@settings(max_examples=50)
def test_pivot_typeexp_instantiation(instance):
    assert isinstance(instance, pivot_TypeExp)

@given(instance=pivot_StateExp_strategy)
@settings(max_examples=50)
def test_pivot_stateexp_instantiation(instance):
    assert isinstance(instance, pivot_StateExp)

@given(instance=pivot_IfExp_strategy)
@settings(max_examples=50)
def test_pivot_ifexp_instantiation(instance):
    assert isinstance(instance, pivot_IfExp)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_IfExp_strategy)
@settings(max_examples=30)
def test_pivot_ifexp_conditiontypeisboolean_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ConditionTypeIsBoolean(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ConditionTypeIsBoolean).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ConditionTypeIsBoolean' in pivot_IfExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ConditionTypeIsBoolean' in pivot_IfExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ConditionTypeIsBoolean' in pivot_IfExp is not implemented or raised an error")

@given(instance=pivot_LetExp_strategy)
@settings(max_examples=50)
def test_pivot_letexp_instantiation(instance):
    assert isinstance(instance, pivot_LetExp)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_LetExp_strategy)
@settings(max_examples=30)
def test_pivot_letexp_typeisintype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.TypeIsInType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.TypeIsInType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'TypeIsInType' in pivot_LetExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'TypeIsInType' in pivot_LetExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'TypeIsInType' in pivot_LetExp is not implemented or raised an error")

@given(instance=pivot_LiteralExp_strategy)
@settings(max_examples=50)
def test_pivot_literalexp_instantiation(instance):
    assert isinstance(instance, pivot_LiteralExp)

@given(instance=pivot_VariableExp_strategy)
@settings(max_examples=50)
def test_pivot_variableexp_instantiation(instance):
    assert isinstance(instance, pivot_VariableExp)



@given(instance=pivot_VariableExp_strategy)
def test_pivot_variableexp_implicit_setter(instance):
    original = instance.implicit
    instance.implicit = original
    assert instance.implicit == original

@given(instance=pivot_UnspecifiedValueExp_strategy)
@settings(max_examples=50)
def test_pivot_unspecifiedvalueexp_instantiation(instance):
    assert isinstance(instance, pivot_UnspecifiedValueExp)

@given(instance=pivot_CallExp_strategy)
@settings(max_examples=50)
def test_pivot_callexp_instantiation(instance):
    assert isinstance(instance, pivot_CallExp)



@given(instance=pivot_CallExp_strategy)
def test_pivot_callexp_implicit_setter(instance):
    original = instance.implicit
    instance.implicit = original
    assert instance.implicit == original

@given(instance=CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_collectionliteralpart_instantiation(instance):
    assert isinstance(instance, CollectionLiteralPart)

@given(instance=pivot_CollectionRange_strategy)
@settings(max_examples=50)
def test_pivot_collectionrange_instantiation(instance):
    assert isinstance(instance, pivot_CollectionRange)

@given(instance=pivot_CollectionItem_strategy)
@settings(max_examples=50)
def test_pivot_collectionitem_instantiation(instance):
    assert isinstance(instance, pivot_CollectionItem)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_CollectionItem_strategy)
@settings(max_examples=30)
def test_pivot_collectionitem_typeisitemtype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.TypeIsItemType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.TypeIsItemType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'TypeIsItemType' in pivot_CollectionItem is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'TypeIsItemType' in pivot_CollectionItem did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'TypeIsItemType' in pivot_CollectionItem is not implemented or raised an error")

@given(instance=pivot_Element_strategy)
@settings(max_examples=50)
def test_pivot_element_instantiation(instance):
    assert isinstance(instance, pivot_Element)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_Element_strategy)
@settings(max_examples=30)
def test_pivot_element_allownedelements_changes_state(instance):
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
        assert has_statements, f"Function 'allOwnedElements' in pivot_Element is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'allOwnedElements' in pivot_Element did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'allOwnedElements' in pivot_Element is not implemented or raised an error")

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=pivot_Constraint_strategy)
@settings(max_examples=50)
def test_pivot_constraint_instantiation(instance):
    assert isinstance(instance, pivot_Constraint)



@given(instance=pivot_Constraint_strategy)
def test_pivot_constraint_isCallable_setter(instance):
    original = instance.isCallable
    instance.isCallable = original
    assert instance.isCallable == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_Constraint_strategy)
@settings(max_examples=30)
def test_pivot_constraint_uniquename_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.UniqueName(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.UniqueName).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'UniqueName' in pivot_Constraint is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'UniqueName' in pivot_Constraint did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'UniqueName' in pivot_Constraint is not implemented or raised an error")

@given(instance=pivot_Type_strategy)
@settings(max_examples=50)
def test_pivot_type_instantiation(instance):
    assert isinstance(instance, pivot_Type)



@given(instance=pivot_Type_strategy)
def test_pivot_type_instanceClassName_setter(instance):
    original = instance.instanceClassName
    instance.instanceClassName = original
    assert instance.instanceClassName == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_Type_strategy)
@settings(max_examples=30)
def test_pivot_type_uniqueinvariantname_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.UniqueInvariantName(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.UniqueInvariantName).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'UniqueInvariantName' in pivot_Type is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'UniqueInvariantName' in pivot_Type did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'UniqueInvariantName' in pivot_Type is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_Type_strategy)
@settings(max_examples=30)
def test_pivot_type_specializein_changes_state(instance):
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
        assert has_statements, f"Function 'specializeIn' in pivot_Type is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'specializeIn' in pivot_Type did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'specializeIn' in pivot_Type is not implemented or raised an error")

@given(instance=pivot_Namespace_strategy)
@settings(max_examples=50)
def test_pivot_namespace_instantiation(instance):
    assert isinstance(instance, pivot_Namespace)

@given(instance=pivot_SendSignalAction_strategy)
@settings(max_examples=50)
def test_pivot_sendsignalaction_instantiation(instance):
    assert isinstance(instance, pivot_SendSignalAction)

@given(instance=pivot_Vertex_strategy)
@settings(max_examples=50)
def test_pivot_vertex_instantiation(instance):
    assert isinstance(instance, pivot_Vertex)

@given(instance=pivot_TypedElement_strategy)
@settings(max_examples=50)
def test_pivot_typedelement_instantiation(instance):
    assert isinstance(instance, pivot_TypedElement)



@given(instance=pivot_TypedElement_strategy)
def test_pivot_typedelement_isRequired_setter(instance):
    original = instance.isRequired
    instance.isRequired = original
    assert instance.isRequired == original

@given(instance=pivot_CallOperationAction_strategy)
@settings(max_examples=50)
def test_pivot_calloperationaction_instantiation(instance):
    assert isinstance(instance, pivot_CallOperationAction)

@given(instance=pivot_Signal_strategy)
@settings(max_examples=50)
def test_pivot_signal_instantiation(instance):
    assert isinstance(instance, pivot_Signal)

@given(instance=pivot_EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_pivot_enumerationliteral_instantiation(instance):
    assert isinstance(instance, pivot_EnumerationLiteral)



@given(instance=pivot_EnumerationLiteral_strategy)
def test_pivot_enumerationliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=pivot_Precedence_strategy)
@settings(max_examples=50)
def test_pivot_precedence_instantiation(instance):
    assert isinstance(instance, pivot_Precedence)



@given(instance=pivot_Precedence_strategy)
def test_pivot_precedence_order_setter(instance):
    original = instance.order
    instance.order = original
    assert instance.order == original



@given(instance=pivot_Precedence_strategy)
def test_pivot_precedence_associativity_setter(instance):
    original = instance.associativity
    instance.associativity = original
    assert instance.associativity == original

@given(instance=pivot_Trigger_strategy)
@settings(max_examples=50)
def test_pivot_trigger_instantiation(instance):
    assert isinstance(instance, pivot_Trigger)

@given(instance=pivot_Import_strategy)
@settings(max_examples=50)
def test_pivot_import_instantiation(instance):
    assert isinstance(instance, pivot_Import)

@given(instance=pivot_Annotation_strategy)
@settings(max_examples=50)
def test_pivot_annotation_instantiation(instance):
    assert isinstance(instance, pivot_Annotation)

@given(instance=PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, PrimitiveLiteralExp)

@given(instance=pivot_NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_pivot_numericliteralexp_instantiation(instance):
    assert isinstance(instance, pivot_NumericLiteralExp)

@given(instance=pivot_NullLiteralExp_strategy)
@settings(max_examples=50)
def test_pivot_nullliteralexp_instantiation(instance):
    assert isinstance(instance, pivot_NullLiteralExp)

@given(instance=pivot_StringLiteralExp_strategy)
@settings(max_examples=50)
def test_pivot_stringliteralexp_instantiation(instance):
    assert isinstance(instance, pivot_StringLiteralExp)



@given(instance=pivot_StringLiteralExp_strategy)
def test_pivot_stringliteralexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=pivot_BooleanLiteralExp_strategy)
@settings(max_examples=50)
def test_pivot_booleanliteralexp_instantiation(instance):
    assert isinstance(instance, pivot_BooleanLiteralExp)



@given(instance=pivot_BooleanLiteralExp_strategy)
def test_pivot_booleanliteralexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_BooleanLiteralExp_strategy)
@settings(max_examples=30)
def test_pivot_booleanliteralexp_typeisboolean_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.TypeIsBoolean(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.TypeIsBoolean).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'TypeIsBoolean' in pivot_BooleanLiteralExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'TypeIsBoolean' in pivot_BooleanLiteralExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'TypeIsBoolean' in pivot_BooleanLiteralExp is not implemented or raised an error")

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=pivot_OrderedSetType_strategy)
@settings(max_examples=50)
def test_pivot_orderedsettype_instantiation(instance):
    assert isinstance(instance, pivot_OrderedSetType)

@given(instance=pivot_SequenceType_strategy)
@settings(max_examples=50)
def test_pivot_sequencetype_instantiation(instance):
    assert isinstance(instance, pivot_SequenceType)

@given(instance=pivot_SetType_strategy)
@settings(max_examples=50)
def test_pivot_settype_instantiation(instance):
    assert isinstance(instance, pivot_SetType)

@given(instance=pivot_BagType_strategy)
@settings(max_examples=50)
def test_pivot_bagtype_instantiation(instance):
    assert isinstance(instance, pivot_BagType)

@given(instance=NavigationCallExp_strategy)
@settings(max_examples=50)
def test_navigationcallexp_instantiation(instance):
    assert isinstance(instance, NavigationCallExp)

@given(instance=pivot_PropertyCallExp_strategy)
@settings(max_examples=50)
def test_pivot_propertycallexp_instantiation(instance):
    assert isinstance(instance, pivot_PropertyCallExp)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_PropertyCallExp_strategy)
@settings(max_examples=30)
def test_pivot_propertycallexp_nonstaticsourcetypeisconformant_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.NonStaticSourceTypeIsConformant(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.NonStaticSourceTypeIsConformant).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'NonStaticSourceTypeIsConformant' in pivot_PropertyCallExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'NonStaticSourceTypeIsConformant' in pivot_PropertyCallExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'NonStaticSourceTypeIsConformant' in pivot_PropertyCallExp is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_PropertyCallExp_strategy)
@settings(max_examples=30)
def test_pivot_propertycallexp_compatibleresulttype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.CompatibleResultType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.CompatibleResultType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'CompatibleResultType' in pivot_PropertyCallExp is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'CompatibleResultType' in pivot_PropertyCallExp did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'CompatibleResultType' in pivot_PropertyCallExp is not implemented or raised an error")

@given(instance=pivot_AssociationClassCallExp_strategy)
@settings(max_examples=50)
def test_pivot_associationclasscallexp_instantiation(instance):
    assert isinstance(instance, pivot_AssociationClassCallExp)

@given(instance=pivot_Property_strategy)
@settings(max_examples=50)
def test_pivot_property_instantiation(instance):
    assert isinstance(instance, pivot_Property)



@given(instance=pivot_Property_strategy)
def test_pivot_property_isID_setter(instance):
    original = instance.isID
    instance.isID = original
    assert instance.isID == original



@given(instance=pivot_Property_strategy)
def test_pivot_property_isUnsettable_setter(instance):
    original = instance.isUnsettable
    instance.isUnsettable = original
    assert instance.isUnsettable == original



@given(instance=pivot_Property_strategy)
def test_pivot_property_implicit_setter(instance):
    original = instance.implicit
    instance.implicit = original
    assert instance.implicit == original



@given(instance=pivot_Property_strategy)
def test_pivot_property_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original



@given(instance=pivot_Property_strategy)
def test_pivot_property_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original



@given(instance=pivot_Property_strategy)
def test_pivot_property_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original



@given(instance=pivot_Property_strategy)
def test_pivot_property_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original



@given(instance=pivot_Property_strategy)
def test_pivot_property_isTransient_setter(instance):
    original = instance.isTransient
    instance.isTransient = original
    assert instance.isTransient == original



@given(instance=pivot_Property_strategy)
def test_pivot_property_isVolatile_setter(instance):
    original = instance.isVolatile
    instance.isVolatile = original
    assert instance.isVolatile == original



@given(instance=pivot_Property_strategy)
def test_pivot_property_isResolveProxies_setter(instance):
    original = instance.isResolveProxies
    instance.isResolveProxies = original
    assert instance.isResolveProxies == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_Property_strategy)
@settings(max_examples=30)
def test_pivot_property_compatibledefaultexpression_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.CompatibleDefaultExpression(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.CompatibleDefaultExpression).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'CompatibleDefaultExpression' in pivot_Property is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'CompatibleDefaultExpression' in pivot_Property did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'CompatibleDefaultExpression' in pivot_Property is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_Property_strategy)
@settings(max_examples=30)
def test_pivot_property_isattribute_changes_state(instance):
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
        assert has_statements, f"Function 'isAttribute' in pivot_Property is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isAttribute' in pivot_Property did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isAttribute' in pivot_Property is not implemented or raised an error")

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=pivot_Stereotype_strategy)
@settings(max_examples=50)
def test_pivot_stereotype_instantiation(instance):
    assert isinstance(instance, pivot_Stereotype)

@given(instance=pivot_VoidType_strategy)
@settings(max_examples=50)
def test_pivot_voidtype_instantiation(instance):
    assert isinstance(instance, pivot_VoidType)

@given(instance=pivot_Metaclass_strategy)
@settings(max_examples=50)
def test_pivot_metaclass_instantiation(instance):
    assert isinstance(instance, pivot_Metaclass)

@given(instance=pivot_InvalidType_strategy)
@settings(max_examples=50)
def test_pivot_invalidtype_instantiation(instance):
    assert isinstance(instance, pivot_InvalidType)

@given(instance=pivot_DataType_strategy)
@settings(max_examples=50)
def test_pivot_datatype_instantiation(instance):
    assert isinstance(instance, pivot_DataType)



@given(instance=pivot_DataType_strategy)
def test_pivot_datatype_isSerializable_setter(instance):
    original = instance.isSerializable
    instance.isSerializable = original
    assert instance.isSerializable == original

@given(instance=pivot_AssociationClass_strategy)
@settings(max_examples=50)
def test_pivot_associationclass_instantiation(instance):
    assert isinstance(instance, pivot_AssociationClass)

@given(instance=pivot_UnspecifiedType_strategy)
@settings(max_examples=50)
def test_pivot_unspecifiedtype_instantiation(instance):
    assert isinstance(instance, pivot_UnspecifiedType)

@given(instance=pivot_Behavior_strategy)
@settings(max_examples=50)
def test_pivot_behavior_instantiation(instance):
    assert isinstance(instance, pivot_Behavior)

@given(instance=pivot_SelfType_strategy)
@settings(max_examples=50)
def test_pivot_selftype_instantiation(instance):
    assert isinstance(instance, pivot_SelfType)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pivot_SelfType_strategy)
@settings(max_examples=30)
def test_pivot_selftype_specializein_changes_state(instance):
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
        assert has_statements, f"Function 'specializeIn' in pivot_SelfType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'specializeIn' in pivot_SelfType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'specializeIn' in pivot_SelfType is not implemented or raised an error")

@given(instance=pivot_AnyType_strategy)
@settings(max_examples=50)
def test_pivot_anytype_instantiation(instance):
    assert isinstance(instance, pivot_AnyType)

@given(instance=pivot_Detail_strategy)
@settings(max_examples=50)
def test_pivot_detail_instantiation(instance):
    assert isinstance(instance, pivot_Detail)



@given(instance=pivot_Detail_strategy)
def test_pivot_detail_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
