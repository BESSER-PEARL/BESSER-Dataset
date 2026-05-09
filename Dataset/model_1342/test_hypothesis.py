import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    MorePivotable,
    ModelElementCS,
    completeoclcs::PathNameDeclCS,
    completeoclcs::Package,
    completeoclcs::Operation,
    completeoclcs::VariableCS,
    FeatureContextDeclCS,
    ExpCS,
    completeoclcs::OCLMessageArgCS,
    completeoclcs::TypedRefCS,
    completeoclcs::ExpSpecificationCS,
    TypedElementCS,
    PathNameDeclCS,
    completeoclcs::PackageDeclarationCS,
    completeoclcs::ContextDeclCS,
    RootCS,
    NamespaceCS,
    completeoclcs::CompleteOCLDocumentCS,
    completeoclcs::Class,
    completeoclcs::ConstraintCS,
    completeoclcs::DefCS,
    TemplateableElementCS,
    completeoclcs::OperationContextDeclCS,
    ContextDeclCS,
    completeoclcs::FeatureContextDeclCS,
    completeoclcs::ClassifierContextDeclCS,
    completeoclcs::ParameterCS,
    DefCS,
    completeoclcs::DefPropertyCS,
    completeoclcs::DefOperationCS,
    completeoclcs::Property,
    completeoclcs::PropertyContextDeclCS,
    completeoclcs::PathNameCS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_morepivotable_is_not_abstract():
    assert not inspect.isabstract(MorePivotable)


def test_morepivotable_constructor_exists():
    assert callable(MorePivotable.__init__)


def test_morepivotable_constructor_args():
    sig = inspect.signature(MorePivotable.__init__)
    params = list(sig.parameters.keys())



def test_modelelementcs_is_not_abstract():
    assert not inspect.isabstract(ModelElementCS)


def test_modelelementcs_constructor_exists():
    assert callable(ModelElementCS.__init__)


def test_modelelementcs_constructor_args():
    sig = inspect.signature(ModelElementCS.__init__)
    params = list(sig.parameters.keys())



def test_completeoclcs::pathnamedeclcs_is_not_abstract():
    assert not inspect.isabstract(completeoclcs::PathNameDeclCS)


def test_completeoclcs::pathnamedeclcs_constructor_exists():
    assert callable(completeoclcs::PathNameDeclCS.__init__)


def test_completeoclcs::pathnamedeclcs_constructor_args():
    sig = inspect.signature(completeoclcs::PathNameDeclCS.__init__)
    params = list(sig.parameters.keys())



def test_completeoclcs::package_is_not_abstract():
    assert not inspect.isabstract(completeoclcs::Package)


def test_completeoclcs::package_constructor_exists():
    assert callable(completeoclcs::Package.__init__)


def test_completeoclcs::package_constructor_args():
    sig = inspect.signature(completeoclcs::Package.__init__)
    params = list(sig.parameters.keys())



def test_completeoclcs::operation_is_not_abstract():
    assert not inspect.isabstract(completeoclcs::Operation)


def test_completeoclcs::operation_constructor_exists():
    assert callable(completeoclcs::Operation.__init__)


def test_completeoclcs::operation_constructor_args():
    sig = inspect.signature(completeoclcs::Operation.__init__)
    params = list(sig.parameters.keys())



def test_completeoclcs::variablecs_is_not_abstract():
    assert not inspect.isabstract(completeoclcs::VariableCS)


def test_completeoclcs::variablecs_constructor_exists():
    assert callable(completeoclcs::VariableCS.__init__)


def test_completeoclcs::variablecs_constructor_args():
    sig = inspect.signature(completeoclcs::VariableCS.__init__)
    params = list(sig.parameters.keys())



def test_featurecontextdeclcs_is_not_abstract():
    assert not inspect.isabstract(FeatureContextDeclCS)


def test_featurecontextdeclcs_constructor_exists():
    assert callable(FeatureContextDeclCS.__init__)


def test_featurecontextdeclcs_constructor_args():
    sig = inspect.signature(FeatureContextDeclCS.__init__)
    params = list(sig.parameters.keys())



def test_expcs_is_not_abstract():
    assert not inspect.isabstract(ExpCS)


def test_expcs_constructor_exists():
    assert callable(ExpCS.__init__)


def test_expcs_constructor_args():
    sig = inspect.signature(ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_completeoclcs::oclmessageargcs_is_not_abstract():
    assert not inspect.isabstract(completeoclcs::OCLMessageArgCS)


def test_completeoclcs::oclmessageargcs_constructor_exists():
    assert callable(completeoclcs::OCLMessageArgCS.__init__)


def test_completeoclcs::oclmessageargcs_constructor_args():
    sig = inspect.signature(completeoclcs::OCLMessageArgCS.__init__)
    params = list(sig.parameters.keys())



def test_completeoclcs::typedrefcs_is_not_abstract():
    assert not inspect.isabstract(completeoclcs::TypedRefCS)


def test_completeoclcs::typedrefcs_constructor_exists():
    assert callable(completeoclcs::TypedRefCS.__init__)


def test_completeoclcs::typedrefcs_constructor_args():
    sig = inspect.signature(completeoclcs::TypedRefCS.__init__)
    params = list(sig.parameters.keys())



def test_completeoclcs::expspecificationcs_is_not_abstract():
    assert not inspect.isabstract(completeoclcs::ExpSpecificationCS)


def test_completeoclcs::expspecificationcs_constructor_exists():
    assert callable(completeoclcs::ExpSpecificationCS.__init__)


def test_completeoclcs::expspecificationcs_constructor_args():
    sig = inspect.signature(completeoclcs::ExpSpecificationCS.__init__)
    params = list(sig.parameters.keys())



def test_typedelementcs_is_not_abstract():
    assert not inspect.isabstract(TypedElementCS)


def test_typedelementcs_constructor_exists():
    assert callable(TypedElementCS.__init__)


def test_typedelementcs_constructor_args():
    sig = inspect.signature(TypedElementCS.__init__)
    params = list(sig.parameters.keys())



def test_pathnamedeclcs_is_not_abstract():
    assert not inspect.isabstract(PathNameDeclCS)


def test_pathnamedeclcs_constructor_exists():
    assert callable(PathNameDeclCS.__init__)


def test_pathnamedeclcs_constructor_args():
    sig = inspect.signature(PathNameDeclCS.__init__)
    params = list(sig.parameters.keys())



def test_completeoclcs::packagedeclarationcs_is_not_abstract():
    assert not inspect.isabstract(completeoclcs::PackageDeclarationCS)


def test_completeoclcs::packagedeclarationcs_constructor_exists():
    assert callable(completeoclcs::PackageDeclarationCS.__init__)


def test_completeoclcs::packagedeclarationcs_constructor_args():
    sig = inspect.signature(completeoclcs::PackageDeclarationCS.__init__)
    params = list(sig.parameters.keys())



def test_completeoclcs::contextdeclcs_is_not_abstract():
    assert not inspect.isabstract(completeoclcs::ContextDeclCS)


def test_completeoclcs::contextdeclcs_constructor_exists():
    assert callable(completeoclcs::ContextDeclCS.__init__)


def test_completeoclcs::contextdeclcs_constructor_args():
    sig = inspect.signature(completeoclcs::ContextDeclCS.__init__)
    params = list(sig.parameters.keys())



def test_rootcs_is_not_abstract():
    assert not inspect.isabstract(RootCS)


def test_rootcs_constructor_exists():
    assert callable(RootCS.__init__)


def test_rootcs_constructor_args():
    sig = inspect.signature(RootCS.__init__)
    params = list(sig.parameters.keys())



def test_namespacecs_is_not_abstract():
    assert not inspect.isabstract(NamespaceCS)


def test_namespacecs_constructor_exists():
    assert callable(NamespaceCS.__init__)


def test_namespacecs_constructor_args():
    sig = inspect.signature(NamespaceCS.__init__)
    params = list(sig.parameters.keys())



def test_completeoclcs::completeocldocumentcs_is_not_abstract():
    assert not inspect.isabstract(completeoclcs::CompleteOCLDocumentCS)


def test_completeoclcs::completeocldocumentcs_constructor_exists():
    assert callable(completeoclcs::CompleteOCLDocumentCS.__init__)


def test_completeoclcs::completeocldocumentcs_constructor_args():
    sig = inspect.signature(completeoclcs::CompleteOCLDocumentCS.__init__)
    params = list(sig.parameters.keys())



def test_completeoclcs::class_is_not_abstract():
    assert not inspect.isabstract(completeoclcs::Class)


def test_completeoclcs::class_constructor_exists():
    assert callable(completeoclcs::Class.__init__)


def test_completeoclcs::class_constructor_args():
    sig = inspect.signature(completeoclcs::Class.__init__)
    params = list(sig.parameters.keys())



def test_completeoclcs::constraintcs_is_not_abstract():
    assert not inspect.isabstract(completeoclcs::ConstraintCS)


def test_completeoclcs::constraintcs_constructor_exists():
    assert callable(completeoclcs::ConstraintCS.__init__)


def test_completeoclcs::constraintcs_constructor_args():
    sig = inspect.signature(completeoclcs::ConstraintCS.__init__)
    params = list(sig.parameters.keys())



def test_completeoclcs::defcs_is_not_abstract():
    assert not inspect.isabstract(completeoclcs::DefCS)


def test_completeoclcs::defcs_constructor_exists():
    assert callable(completeoclcs::DefCS.__init__)


def test_completeoclcs::defcs_constructor_args():
    sig = inspect.signature(completeoclcs::DefCS.__init__)
    params = list(sig.parameters.keys())
    assert "isStatic" in params, "Missing parameter 'isStatic'"

def test_completeoclcs::defcs_has_isStatic():
    assert hasattr(completeoclcs::DefCS, "isStatic")
    descriptor = None
    for klass in completeoclcs::DefCS.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)



def test_templateableelementcs_is_not_abstract():
    assert not inspect.isabstract(TemplateableElementCS)


def test_templateableelementcs_constructor_exists():
    assert callable(TemplateableElementCS.__init__)


def test_templateableelementcs_constructor_args():
    sig = inspect.signature(TemplateableElementCS.__init__)
    params = list(sig.parameters.keys())



def test_completeoclcs::operationcontextdeclcs_is_not_abstract():
    assert not inspect.isabstract(completeoclcs::OperationContextDeclCS)


def test_completeoclcs::operationcontextdeclcs_constructor_exists():
    assert callable(completeoclcs::OperationContextDeclCS.__init__)


def test_completeoclcs::operationcontextdeclcs_constructor_args():
    sig = inspect.signature(completeoclcs::OperationContextDeclCS.__init__)
    params = list(sig.parameters.keys())



def test_contextdeclcs_is_not_abstract():
    assert not inspect.isabstract(ContextDeclCS)


def test_contextdeclcs_constructor_exists():
    assert callable(ContextDeclCS.__init__)


def test_contextdeclcs_constructor_args():
    sig = inspect.signature(ContextDeclCS.__init__)
    params = list(sig.parameters.keys())



def test_completeoclcs::featurecontextdeclcs_is_not_abstract():
    assert not inspect.isabstract(completeoclcs::FeatureContextDeclCS)


def test_completeoclcs::featurecontextdeclcs_constructor_exists():
    assert callable(completeoclcs::FeatureContextDeclCS.__init__)


def test_completeoclcs::featurecontextdeclcs_constructor_args():
    sig = inspect.signature(completeoclcs::FeatureContextDeclCS.__init__)
    params = list(sig.parameters.keys())



def test_completeoclcs::classifiercontextdeclcs_is_not_abstract():
    assert not inspect.isabstract(completeoclcs::ClassifierContextDeclCS)


def test_completeoclcs::classifiercontextdeclcs_constructor_exists():
    assert callable(completeoclcs::ClassifierContextDeclCS.__init__)


def test_completeoclcs::classifiercontextdeclcs_constructor_args():
    sig = inspect.signature(completeoclcs::ClassifierContextDeclCS.__init__)
    params = list(sig.parameters.keys())
    assert "selfName" in params, "Missing parameter 'selfName'"

def test_completeoclcs::classifiercontextdeclcs_has_selfName():
    assert hasattr(completeoclcs::ClassifierContextDeclCS, "selfName")
    descriptor = None
    for klass in completeoclcs::ClassifierContextDeclCS.__mro__:
        if "selfName" in klass.__dict__:
            descriptor = klass.__dict__["selfName"]
            break
    assert isinstance(descriptor, property)



def test_completeoclcs::parametercs_is_not_abstract():
    assert not inspect.isabstract(completeoclcs::ParameterCS)


def test_completeoclcs::parametercs_constructor_exists():
    assert callable(completeoclcs::ParameterCS.__init__)


def test_completeoclcs::parametercs_constructor_args():
    sig = inspect.signature(completeoclcs::ParameterCS.__init__)
    params = list(sig.parameters.keys())



def test_defcs_is_not_abstract():
    assert not inspect.isabstract(DefCS)


def test_defcs_constructor_exists():
    assert callable(DefCS.__init__)


def test_defcs_constructor_args():
    sig = inspect.signature(DefCS.__init__)
    params = list(sig.parameters.keys())



def test_completeoclcs::defpropertycs_is_not_abstract():
    assert not inspect.isabstract(completeoclcs::DefPropertyCS)


def test_completeoclcs::defpropertycs_constructor_exists():
    assert callable(completeoclcs::DefPropertyCS.__init__)


def test_completeoclcs::defpropertycs_constructor_args():
    sig = inspect.signature(completeoclcs::DefPropertyCS.__init__)
    params = list(sig.parameters.keys())



def test_completeoclcs::defoperationcs_is_not_abstract():
    assert not inspect.isabstract(completeoclcs::DefOperationCS)


def test_completeoclcs::defoperationcs_constructor_exists():
    assert callable(completeoclcs::DefOperationCS.__init__)


def test_completeoclcs::defoperationcs_constructor_args():
    sig = inspect.signature(completeoclcs::DefOperationCS.__init__)
    params = list(sig.parameters.keys())



def test_completeoclcs::property_is_not_abstract():
    assert not inspect.isabstract(completeoclcs::Property)


def test_completeoclcs::property_constructor_exists():
    assert callable(completeoclcs::Property.__init__)


def test_completeoclcs::property_constructor_args():
    sig = inspect.signature(completeoclcs::Property.__init__)
    params = list(sig.parameters.keys())



def test_completeoclcs::propertycontextdeclcs_is_not_abstract():
    assert not inspect.isabstract(completeoclcs::PropertyContextDeclCS)


def test_completeoclcs::propertycontextdeclcs_constructor_exists():
    assert callable(completeoclcs::PropertyContextDeclCS.__init__)


def test_completeoclcs::propertycontextdeclcs_constructor_args():
    sig = inspect.signature(completeoclcs::PropertyContextDeclCS.__init__)
    params = list(sig.parameters.keys())



def test_completeoclcs::pathnamecs_is_not_abstract():
    assert not inspect.isabstract(completeoclcs::PathNameCS)


def test_completeoclcs::pathnamecs_constructor_exists():
    assert callable(completeoclcs::PathNameCS.__init__)


def test_completeoclcs::pathnamecs_constructor_args():
    sig = inspect.signature(completeoclcs::PathNameCS.__init__)
    params = list(sig.parameters.keys())


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
MorePivotable_strategy = st.builds(
    MorePivotable,
)
ModelElementCS_strategy = st.builds(
    ModelElementCS,
)
completeoclcs::PathNameDeclCS_strategy = st.builds(
    completeoclcs::PathNameDeclCS,
)
completeoclcs::Package_strategy = st.builds(
    completeoclcs::Package,
)
completeoclcs::Operation_strategy = st.builds(
    completeoclcs::Operation,
)
completeoclcs::VariableCS_strategy = st.builds(
    completeoclcs::VariableCS,
)
FeatureContextDeclCS_strategy = st.builds(
    FeatureContextDeclCS,
)
ExpCS_strategy = st.builds(
    ExpCS,
)
completeoclcs::OCLMessageArgCS_strategy = st.builds(
    completeoclcs::OCLMessageArgCS,
)
completeoclcs::TypedRefCS_strategy = st.builds(
    completeoclcs::TypedRefCS,
)
completeoclcs::ExpSpecificationCS_strategy = st.builds(
    completeoclcs::ExpSpecificationCS,
)
TypedElementCS_strategy = st.builds(
    TypedElementCS,
)
PathNameDeclCS_strategy = st.builds(
    PathNameDeclCS,
)
completeoclcs::PackageDeclarationCS_strategy = st.builds(
    completeoclcs::PackageDeclarationCS,
)
completeoclcs::ContextDeclCS_strategy = st.builds(
    completeoclcs::ContextDeclCS,
)
RootCS_strategy = st.builds(
    RootCS,
)
NamespaceCS_strategy = st.builds(
    NamespaceCS,
)
completeoclcs::CompleteOCLDocumentCS_strategy = st.builds(
    completeoclcs::CompleteOCLDocumentCS,
)
completeoclcs::Class_strategy = st.builds(
    completeoclcs::Class,
)
completeoclcs::ConstraintCS_strategy = st.builds(
    completeoclcs::ConstraintCS,
)
completeoclcs::DefCS_strategy = st.builds(
    completeoclcs::DefCS,
    isStatic=
        st.booleans()
)
TemplateableElementCS_strategy = st.builds(
    TemplateableElementCS,
)
completeoclcs::OperationContextDeclCS_strategy = st.builds(
    completeoclcs::OperationContextDeclCS,
)
ContextDeclCS_strategy = st.builds(
    ContextDeclCS,
)
completeoclcs::FeatureContextDeclCS_strategy = st.builds(
    completeoclcs::FeatureContextDeclCS,
)
completeoclcs::ClassifierContextDeclCS_strategy = st.builds(
    completeoclcs::ClassifierContextDeclCS,
    selfName=
        safe_text
)
completeoclcs::ParameterCS_strategy = st.builds(
    completeoclcs::ParameterCS,
)
DefCS_strategy = st.builds(
    DefCS,
)
completeoclcs::DefPropertyCS_strategy = st.builds(
    completeoclcs::DefPropertyCS,
)
completeoclcs::DefOperationCS_strategy = st.builds(
    completeoclcs::DefOperationCS,
)
completeoclcs::Property_strategy = st.builds(
    completeoclcs::Property,
)
completeoclcs::PropertyContextDeclCS_strategy = st.builds(
    completeoclcs::PropertyContextDeclCS,
)
completeoclcs::PathNameCS_strategy = st.builds(
    completeoclcs::PathNameCS,
)

@given(instance=MorePivotable_strategy)
@settings(max_examples=50)
def test_morepivotable_instantiation(instance):
    assert isinstance(instance, MorePivotable)

@given(instance=ModelElementCS_strategy)
@settings(max_examples=50)
def test_modelelementcs_instantiation(instance):
    assert isinstance(instance, ModelElementCS)

@given(instance=completeoclcs::PathNameDeclCS_strategy)
@settings(max_examples=50)
def test_completeoclcs::pathnamedeclcs_instantiation(instance):
    assert isinstance(instance, completeoclcs::PathNameDeclCS)

@given(instance=completeoclcs::Package_strategy)
@settings(max_examples=50)
def test_completeoclcs::package_instantiation(instance):
    assert isinstance(instance, completeoclcs::Package)

@given(instance=completeoclcs::Operation_strategy)
@settings(max_examples=50)
def test_completeoclcs::operation_instantiation(instance):
    assert isinstance(instance, completeoclcs::Operation)

@given(instance=completeoclcs::VariableCS_strategy)
@settings(max_examples=50)
def test_completeoclcs::variablecs_instantiation(instance):
    assert isinstance(instance, completeoclcs::VariableCS)

@given(instance=FeatureContextDeclCS_strategy)
@settings(max_examples=50)
def test_featurecontextdeclcs_instantiation(instance):
    assert isinstance(instance, FeatureContextDeclCS)

@given(instance=ExpCS_strategy)
@settings(max_examples=50)
def test_expcs_instantiation(instance):
    assert isinstance(instance, ExpCS)

@given(instance=completeoclcs::OCLMessageArgCS_strategy)
@settings(max_examples=50)
def test_completeoclcs::oclmessageargcs_instantiation(instance):
    assert isinstance(instance, completeoclcs::OCLMessageArgCS)

@given(instance=completeoclcs::TypedRefCS_strategy)
@settings(max_examples=50)
def test_completeoclcs::typedrefcs_instantiation(instance):
    assert isinstance(instance, completeoclcs::TypedRefCS)

@given(instance=completeoclcs::ExpSpecificationCS_strategy)
@settings(max_examples=50)
def test_completeoclcs::expspecificationcs_instantiation(instance):
    assert isinstance(instance, completeoclcs::ExpSpecificationCS)

@given(instance=TypedElementCS_strategy)
@settings(max_examples=50)
def test_typedelementcs_instantiation(instance):
    assert isinstance(instance, TypedElementCS)

@given(instance=PathNameDeclCS_strategy)
@settings(max_examples=50)
def test_pathnamedeclcs_instantiation(instance):
    assert isinstance(instance, PathNameDeclCS)

@given(instance=completeoclcs::PackageDeclarationCS_strategy)
@settings(max_examples=50)
def test_completeoclcs::packagedeclarationcs_instantiation(instance):
    assert isinstance(instance, completeoclcs::PackageDeclarationCS)

@given(instance=completeoclcs::ContextDeclCS_strategy)
@settings(max_examples=50)
def test_completeoclcs::contextdeclcs_instantiation(instance):
    assert isinstance(instance, completeoclcs::ContextDeclCS)

@given(instance=RootCS_strategy)
@settings(max_examples=50)
def test_rootcs_instantiation(instance):
    assert isinstance(instance, RootCS)

@given(instance=NamespaceCS_strategy)
@settings(max_examples=50)
def test_namespacecs_instantiation(instance):
    assert isinstance(instance, NamespaceCS)

@given(instance=completeoclcs::CompleteOCLDocumentCS_strategy)
@settings(max_examples=50)
def test_completeoclcs::completeocldocumentcs_instantiation(instance):
    assert isinstance(instance, completeoclcs::CompleteOCLDocumentCS)

@given(instance=completeoclcs::Class_strategy)
@settings(max_examples=50)
def test_completeoclcs::class_instantiation(instance):
    assert isinstance(instance, completeoclcs::Class)

@given(instance=completeoclcs::ConstraintCS_strategy)
@settings(max_examples=50)
def test_completeoclcs::constraintcs_instantiation(instance):
    assert isinstance(instance, completeoclcs::ConstraintCS)

@given(instance=completeoclcs::DefCS_strategy)
@settings(max_examples=50)
def test_completeoclcs::defcs_instantiation(instance):
    assert isinstance(instance, completeoclcs::DefCS)

@given(instance=completeoclcs::DefCS_strategy)
def test_completeoclcs::defcs_isStatic_type(instance):
    assert isinstance(instance.isStatic, bool)


@given(instance=completeoclcs::DefCS_strategy)
def test_completeoclcs::defcs_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=TemplateableElementCS_strategy)
@settings(max_examples=50)
def test_templateableelementcs_instantiation(instance):
    assert isinstance(instance, TemplateableElementCS)

@given(instance=completeoclcs::OperationContextDeclCS_strategy)
@settings(max_examples=50)
def test_completeoclcs::operationcontextdeclcs_instantiation(instance):
    assert isinstance(instance, completeoclcs::OperationContextDeclCS)

@given(instance=ContextDeclCS_strategy)
@settings(max_examples=50)
def test_contextdeclcs_instantiation(instance):
    assert isinstance(instance, ContextDeclCS)

@given(instance=completeoclcs::FeatureContextDeclCS_strategy)
@settings(max_examples=50)
def test_completeoclcs::featurecontextdeclcs_instantiation(instance):
    assert isinstance(instance, completeoclcs::FeatureContextDeclCS)

@given(instance=completeoclcs::ClassifierContextDeclCS_strategy)
@settings(max_examples=50)
def test_completeoclcs::classifiercontextdeclcs_instantiation(instance):
    assert isinstance(instance, completeoclcs::ClassifierContextDeclCS)

@given(instance=completeoclcs::ClassifierContextDeclCS_strategy)
def test_completeoclcs::classifiercontextdeclcs_selfName_type(instance):
    assert isinstance(instance.selfName, str)


@given(instance=completeoclcs::ClassifierContextDeclCS_strategy)
def test_completeoclcs::classifiercontextdeclcs_selfName_setter(instance):
    original = instance.selfName
    instance.selfName = original
    assert instance.selfName == original

@given(instance=completeoclcs::ParameterCS_strategy)
@settings(max_examples=50)
def test_completeoclcs::parametercs_instantiation(instance):
    assert isinstance(instance, completeoclcs::ParameterCS)

@given(instance=DefCS_strategy)
@settings(max_examples=50)
def test_defcs_instantiation(instance):
    assert isinstance(instance, DefCS)

@given(instance=completeoclcs::DefPropertyCS_strategy)
@settings(max_examples=50)
def test_completeoclcs::defpropertycs_instantiation(instance):
    assert isinstance(instance, completeoclcs::DefPropertyCS)

@given(instance=completeoclcs::DefOperationCS_strategy)
@settings(max_examples=50)
def test_completeoclcs::defoperationcs_instantiation(instance):
    assert isinstance(instance, completeoclcs::DefOperationCS)

@given(instance=completeoclcs::Property_strategy)
@settings(max_examples=50)
def test_completeoclcs::property_instantiation(instance):
    assert isinstance(instance, completeoclcs::Property)

@given(instance=completeoclcs::PropertyContextDeclCS_strategy)
@settings(max_examples=50)
def test_completeoclcs::propertycontextdeclcs_instantiation(instance):
    assert isinstance(instance, completeoclcs::PropertyContextDeclCS)

@given(instance=completeoclcs::PathNameCS_strategy)
@settings(max_examples=50)
def test_completeoclcs::pathnamecs_instantiation(instance):
    assert isinstance(instance, completeoclcs::PathNameCS)
