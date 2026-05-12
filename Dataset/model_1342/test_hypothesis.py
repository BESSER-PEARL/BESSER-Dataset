import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    completeoclcs_ParameterCS,
    DefCS,
    completeoclcs_DefPropertyCS,
    completeoclcs_Property,
    completeoclcs_PathNameCS,
    MorePivotable,
    ModelElementCS,
    completeoclcs_PathNameDeclCS,
    completeoclcs_Package,
    completeoclcs_Operation,
    completeoclcs_VariableCS,
    FeatureContextDeclCS,
    completeoclcs_PropertyContextDeclCS,
    ExpCS,
    completeoclcs_OCLMessageArgCS,
    completeoclcs_TypedRefCS,
    completeoclcs_ExpSpecificationCS,
    TypedElementCS,
    PathNameDeclCS,
    completeoclcs_PackageDeclarationCS,
    completeoclcs_ContextDeclCS,
    RootCS,
    NamespaceCS,
    completeoclcs_CompleteOCLDocumentCS,
    completeoclcs_Class,
    completeoclcs_ConstraintCS,
    completeoclcs_DefCS,
    TemplateableElementCS,
    completeoclcs_DefOperationCS,
    completeoclcs_OperationContextDeclCS,
    ContextDeclCS,
    completeoclcs_FeatureContextDeclCS,
    completeoclcs_ClassifierContextDeclCS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_completeoclcs_parametercs_is_not_abstract():
    assert not inspect.isabstract(completeoclcs_ParameterCS)


def test_completeoclcs_parametercs_constructor_exists():
    assert callable(completeoclcs_ParameterCS.__init__)


def test_completeoclcs_parametercs_constructor_args():
    sig = inspect.signature(completeoclcs_ParameterCS.__init__)
    params = list(sig.parameters.keys())



def test_defcs_is_not_abstract():
    assert not inspect.isabstract(DefCS)


def test_defcs_constructor_exists():
    assert callable(DefCS.__init__)


def test_defcs_constructor_args():
    sig = inspect.signature(DefCS.__init__)
    params = list(sig.parameters.keys())



def test_completeoclcs_defpropertycs_is_not_abstract():
    assert not inspect.isabstract(completeoclcs_DefPropertyCS)


def test_completeoclcs_defpropertycs_constructor_exists():
    assert callable(completeoclcs_DefPropertyCS.__init__)


def test_completeoclcs_defpropertycs_constructor_args():
    sig = inspect.signature(completeoclcs_DefPropertyCS.__init__)
    params = list(sig.parameters.keys())



def test_completeoclcs_property_is_not_abstract():
    assert not inspect.isabstract(completeoclcs_Property)


def test_completeoclcs_property_constructor_exists():
    assert callable(completeoclcs_Property.__init__)


def test_completeoclcs_property_constructor_args():
    sig = inspect.signature(completeoclcs_Property.__init__)
    params = list(sig.parameters.keys())



def test_completeoclcs_pathnamecs_is_not_abstract():
    assert not inspect.isabstract(completeoclcs_PathNameCS)


def test_completeoclcs_pathnamecs_constructor_exists():
    assert callable(completeoclcs_PathNameCS.__init__)


def test_completeoclcs_pathnamecs_constructor_args():
    sig = inspect.signature(completeoclcs_PathNameCS.__init__)
    params = list(sig.parameters.keys())



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



def test_completeoclcs_pathnamedeclcs_is_not_abstract():
    assert not inspect.isabstract(completeoclcs_PathNameDeclCS)


def test_completeoclcs_pathnamedeclcs_constructor_exists():
    assert callable(completeoclcs_PathNameDeclCS.__init__)


def test_completeoclcs_pathnamedeclcs_constructor_args():
    sig = inspect.signature(completeoclcs_PathNameDeclCS.__init__)
    params = list(sig.parameters.keys())



def test_completeoclcs_package_is_not_abstract():
    assert not inspect.isabstract(completeoclcs_Package)


def test_completeoclcs_package_constructor_exists():
    assert callable(completeoclcs_Package.__init__)


def test_completeoclcs_package_constructor_args():
    sig = inspect.signature(completeoclcs_Package.__init__)
    params = list(sig.parameters.keys())



def test_completeoclcs_operation_is_not_abstract():
    assert not inspect.isabstract(completeoclcs_Operation)


def test_completeoclcs_operation_constructor_exists():
    assert callable(completeoclcs_Operation.__init__)


def test_completeoclcs_operation_constructor_args():
    sig = inspect.signature(completeoclcs_Operation.__init__)
    params = list(sig.parameters.keys())



def test_completeoclcs_variablecs_is_not_abstract():
    assert not inspect.isabstract(completeoclcs_VariableCS)


def test_completeoclcs_variablecs_constructor_exists():
    assert callable(completeoclcs_VariableCS.__init__)


def test_completeoclcs_variablecs_constructor_args():
    sig = inspect.signature(completeoclcs_VariableCS.__init__)
    params = list(sig.parameters.keys())



def test_featurecontextdeclcs_is_not_abstract():
    assert not inspect.isabstract(FeatureContextDeclCS)


def test_featurecontextdeclcs_constructor_exists():
    assert callable(FeatureContextDeclCS.__init__)


def test_featurecontextdeclcs_constructor_args():
    sig = inspect.signature(FeatureContextDeclCS.__init__)
    params = list(sig.parameters.keys())



def test_completeoclcs_propertycontextdeclcs_is_not_abstract():
    assert not inspect.isabstract(completeoclcs_PropertyContextDeclCS)


def test_completeoclcs_propertycontextdeclcs_constructor_exists():
    assert callable(completeoclcs_PropertyContextDeclCS.__init__)


def test_completeoclcs_propertycontextdeclcs_constructor_args():
    sig = inspect.signature(completeoclcs_PropertyContextDeclCS.__init__)
    params = list(sig.parameters.keys())



def test_expcs_is_not_abstract():
    assert not inspect.isabstract(ExpCS)


def test_expcs_constructor_exists():
    assert callable(ExpCS.__init__)


def test_expcs_constructor_args():
    sig = inspect.signature(ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_completeoclcs_oclmessageargcs_is_not_abstract():
    assert not inspect.isabstract(completeoclcs_OCLMessageArgCS)


def test_completeoclcs_oclmessageargcs_constructor_exists():
    assert callable(completeoclcs_OCLMessageArgCS.__init__)


def test_completeoclcs_oclmessageargcs_constructor_args():
    sig = inspect.signature(completeoclcs_OCLMessageArgCS.__init__)
    params = list(sig.parameters.keys())



def test_completeoclcs_typedrefcs_is_not_abstract():
    assert not inspect.isabstract(completeoclcs_TypedRefCS)


def test_completeoclcs_typedrefcs_constructor_exists():
    assert callable(completeoclcs_TypedRefCS.__init__)


def test_completeoclcs_typedrefcs_constructor_args():
    sig = inspect.signature(completeoclcs_TypedRefCS.__init__)
    params = list(sig.parameters.keys())



def test_completeoclcs_expspecificationcs_is_not_abstract():
    assert not inspect.isabstract(completeoclcs_ExpSpecificationCS)


def test_completeoclcs_expspecificationcs_constructor_exists():
    assert callable(completeoclcs_ExpSpecificationCS.__init__)


def test_completeoclcs_expspecificationcs_constructor_args():
    sig = inspect.signature(completeoclcs_ExpSpecificationCS.__init__)
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



def test_completeoclcs_packagedeclarationcs_is_not_abstract():
    assert not inspect.isabstract(completeoclcs_PackageDeclarationCS)


def test_completeoclcs_packagedeclarationcs_constructor_exists():
    assert callable(completeoclcs_PackageDeclarationCS.__init__)


def test_completeoclcs_packagedeclarationcs_constructor_args():
    sig = inspect.signature(completeoclcs_PackageDeclarationCS.__init__)
    params = list(sig.parameters.keys())



def test_completeoclcs_contextdeclcs_is_not_abstract():
    assert not inspect.isabstract(completeoclcs_ContextDeclCS)


def test_completeoclcs_contextdeclcs_constructor_exists():
    assert callable(completeoclcs_ContextDeclCS.__init__)


def test_completeoclcs_contextdeclcs_constructor_args():
    sig = inspect.signature(completeoclcs_ContextDeclCS.__init__)
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



def test_completeoclcs_completeocldocumentcs_is_not_abstract():
    assert not inspect.isabstract(completeoclcs_CompleteOCLDocumentCS)


def test_completeoclcs_completeocldocumentcs_constructor_exists():
    assert callable(completeoclcs_CompleteOCLDocumentCS.__init__)


def test_completeoclcs_completeocldocumentcs_constructor_args():
    sig = inspect.signature(completeoclcs_CompleteOCLDocumentCS.__init__)
    params = list(sig.parameters.keys())



def test_completeoclcs_class_is_not_abstract():
    assert not inspect.isabstract(completeoclcs_Class)


def test_completeoclcs_class_constructor_exists():
    assert callable(completeoclcs_Class.__init__)


def test_completeoclcs_class_constructor_args():
    sig = inspect.signature(completeoclcs_Class.__init__)
    params = list(sig.parameters.keys())



def test_completeoclcs_constraintcs_is_not_abstract():
    assert not inspect.isabstract(completeoclcs_ConstraintCS)


def test_completeoclcs_constraintcs_constructor_exists():
    assert callable(completeoclcs_ConstraintCS.__init__)


def test_completeoclcs_constraintcs_constructor_args():
    sig = inspect.signature(completeoclcs_ConstraintCS.__init__)
    params = list(sig.parameters.keys())



def test_completeoclcs_defcs_is_not_abstract():
    assert not inspect.isabstract(completeoclcs_DefCS)


def test_completeoclcs_defcs_constructor_exists():
    assert callable(completeoclcs_DefCS.__init__)


def test_completeoclcs_defcs_constructor_args():
    sig = inspect.signature(completeoclcs_DefCS.__init__)
    params = list(sig.parameters.keys())
    assert "isStatic" in params, "Missing parameter 'isStatic'"

def test_completeoclcs_defcs_has_isStatic():
    assert hasattr(completeoclcs_DefCS, "isStatic")
    descriptor = None
    for klass in completeoclcs_DefCS.__mro__:
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



def test_completeoclcs_defoperationcs_is_not_abstract():
    assert not inspect.isabstract(completeoclcs_DefOperationCS)


def test_completeoclcs_defoperationcs_constructor_exists():
    assert callable(completeoclcs_DefOperationCS.__init__)


def test_completeoclcs_defoperationcs_constructor_args():
    sig = inspect.signature(completeoclcs_DefOperationCS.__init__)
    params = list(sig.parameters.keys())



def test_completeoclcs_operationcontextdeclcs_is_not_abstract():
    assert not inspect.isabstract(completeoclcs_OperationContextDeclCS)


def test_completeoclcs_operationcontextdeclcs_constructor_exists():
    assert callable(completeoclcs_OperationContextDeclCS.__init__)


def test_completeoclcs_operationcontextdeclcs_constructor_args():
    sig = inspect.signature(completeoclcs_OperationContextDeclCS.__init__)
    params = list(sig.parameters.keys())



def test_contextdeclcs_is_not_abstract():
    assert not inspect.isabstract(ContextDeclCS)


def test_contextdeclcs_constructor_exists():
    assert callable(ContextDeclCS.__init__)


def test_contextdeclcs_constructor_args():
    sig = inspect.signature(ContextDeclCS.__init__)
    params = list(sig.parameters.keys())



def test_completeoclcs_featurecontextdeclcs_is_not_abstract():
    assert not inspect.isabstract(completeoclcs_FeatureContextDeclCS)


def test_completeoclcs_featurecontextdeclcs_constructor_exists():
    assert callable(completeoclcs_FeatureContextDeclCS.__init__)


def test_completeoclcs_featurecontextdeclcs_constructor_args():
    sig = inspect.signature(completeoclcs_FeatureContextDeclCS.__init__)
    params = list(sig.parameters.keys())



def test_completeoclcs_classifiercontextdeclcs_is_not_abstract():
    assert not inspect.isabstract(completeoclcs_ClassifierContextDeclCS)


def test_completeoclcs_classifiercontextdeclcs_constructor_exists():
    assert callable(completeoclcs_ClassifierContextDeclCS.__init__)


def test_completeoclcs_classifiercontextdeclcs_constructor_args():
    sig = inspect.signature(completeoclcs_ClassifierContextDeclCS.__init__)
    params = list(sig.parameters.keys())
    assert "selfName" in params, "Missing parameter 'selfName'"

def test_completeoclcs_classifiercontextdeclcs_has_selfName():
    assert hasattr(completeoclcs_ClassifierContextDeclCS, "selfName")
    descriptor = None
    for klass in completeoclcs_ClassifierContextDeclCS.__mro__:
        if "selfName" in klass.__dict__:
            descriptor = klass.__dict__["selfName"]
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
completeoclcs_ParameterCS_strategy = st.builds(
    completeoclcs_ParameterCS,
)
DefCS_strategy = st.builds(
    DefCS,
)
completeoclcs_DefPropertyCS_strategy = st.builds(
    completeoclcs_DefPropertyCS,
)
completeoclcs_Property_strategy = st.builds(
    completeoclcs_Property,
)
completeoclcs_PathNameCS_strategy = st.builds(
    completeoclcs_PathNameCS,
)
MorePivotable_strategy = st.builds(
    MorePivotable,
)
ModelElementCS_strategy = st.builds(
    ModelElementCS,
)
completeoclcs_PathNameDeclCS_strategy = st.builds(
    completeoclcs_PathNameDeclCS,
)
completeoclcs_Package_strategy = st.builds(
    completeoclcs_Package,
)
completeoclcs_Operation_strategy = st.builds(
    completeoclcs_Operation,
)
completeoclcs_VariableCS_strategy = st.builds(
    completeoclcs_VariableCS,
)
FeatureContextDeclCS_strategy = st.builds(
    FeatureContextDeclCS,
)
completeoclcs_PropertyContextDeclCS_strategy = st.builds(
    completeoclcs_PropertyContextDeclCS,
)
ExpCS_strategy = st.builds(
    ExpCS,
)
completeoclcs_OCLMessageArgCS_strategy = st.builds(
    completeoclcs_OCLMessageArgCS,
)
completeoclcs_TypedRefCS_strategy = st.builds(
    completeoclcs_TypedRefCS,
)
completeoclcs_ExpSpecificationCS_strategy = st.builds(
    completeoclcs_ExpSpecificationCS,
)
TypedElementCS_strategy = st.builds(
    TypedElementCS,
)
PathNameDeclCS_strategy = st.builds(
    PathNameDeclCS,
)
completeoclcs_PackageDeclarationCS_strategy = st.builds(
    completeoclcs_PackageDeclarationCS,
)
completeoclcs_ContextDeclCS_strategy = st.builds(
    completeoclcs_ContextDeclCS,
)
RootCS_strategy = st.builds(
    RootCS,
)
NamespaceCS_strategy = st.builds(
    NamespaceCS,
)
completeoclcs_CompleteOCLDocumentCS_strategy = st.builds(
    completeoclcs_CompleteOCLDocumentCS,
)
completeoclcs_Class_strategy = st.builds(
    completeoclcs_Class,
)
completeoclcs_ConstraintCS_strategy = st.builds(
    completeoclcs_ConstraintCS,
)
completeoclcs_DefCS_strategy = st.builds(
    completeoclcs_DefCS,
    isStatic=
        st.booleans()
)
TemplateableElementCS_strategy = st.builds(
    TemplateableElementCS,
)
completeoclcs_DefOperationCS_strategy = st.builds(
    completeoclcs_DefOperationCS,
)
completeoclcs_OperationContextDeclCS_strategy = st.builds(
    completeoclcs_OperationContextDeclCS,
)
ContextDeclCS_strategy = st.builds(
    ContextDeclCS,
)
completeoclcs_FeatureContextDeclCS_strategy = st.builds(
    completeoclcs_FeatureContextDeclCS,
)
completeoclcs_ClassifierContextDeclCS_strategy = st.builds(
    completeoclcs_ClassifierContextDeclCS,
    selfName=
        safe_text
)

@given(instance=completeoclcs_ParameterCS_strategy)
@settings(max_examples=50)
def test_completeoclcs_parametercs_instantiation(instance):
    assert isinstance(instance, completeoclcs_ParameterCS)

@given(instance=DefCS_strategy)
@settings(max_examples=50)
def test_defcs_instantiation(instance):
    assert isinstance(instance, DefCS)

@given(instance=completeoclcs_DefPropertyCS_strategy)
@settings(max_examples=50)
def test_completeoclcs_defpropertycs_instantiation(instance):
    assert isinstance(instance, completeoclcs_DefPropertyCS)

@given(instance=completeoclcs_Property_strategy)
@settings(max_examples=50)
def test_completeoclcs_property_instantiation(instance):
    assert isinstance(instance, completeoclcs_Property)

@given(instance=completeoclcs_PathNameCS_strategy)
@settings(max_examples=50)
def test_completeoclcs_pathnamecs_instantiation(instance):
    assert isinstance(instance, completeoclcs_PathNameCS)

@given(instance=MorePivotable_strategy)
@settings(max_examples=50)
def test_morepivotable_instantiation(instance):
    assert isinstance(instance, MorePivotable)

@given(instance=ModelElementCS_strategy)
@settings(max_examples=50)
def test_modelelementcs_instantiation(instance):
    assert isinstance(instance, ModelElementCS)

@given(instance=completeoclcs_PathNameDeclCS_strategy)
@settings(max_examples=50)
def test_completeoclcs_pathnamedeclcs_instantiation(instance):
    assert isinstance(instance, completeoclcs_PathNameDeclCS)

@given(instance=completeoclcs_Package_strategy)
@settings(max_examples=50)
def test_completeoclcs_package_instantiation(instance):
    assert isinstance(instance, completeoclcs_Package)

@given(instance=completeoclcs_Operation_strategy)
@settings(max_examples=50)
def test_completeoclcs_operation_instantiation(instance):
    assert isinstance(instance, completeoclcs_Operation)

@given(instance=completeoclcs_VariableCS_strategy)
@settings(max_examples=50)
def test_completeoclcs_variablecs_instantiation(instance):
    assert isinstance(instance, completeoclcs_VariableCS)

@given(instance=FeatureContextDeclCS_strategy)
@settings(max_examples=50)
def test_featurecontextdeclcs_instantiation(instance):
    assert isinstance(instance, FeatureContextDeclCS)

@given(instance=completeoclcs_PropertyContextDeclCS_strategy)
@settings(max_examples=50)
def test_completeoclcs_propertycontextdeclcs_instantiation(instance):
    assert isinstance(instance, completeoclcs_PropertyContextDeclCS)

@given(instance=ExpCS_strategy)
@settings(max_examples=50)
def test_expcs_instantiation(instance):
    assert isinstance(instance, ExpCS)

@given(instance=completeoclcs_OCLMessageArgCS_strategy)
@settings(max_examples=50)
def test_completeoclcs_oclmessageargcs_instantiation(instance):
    assert isinstance(instance, completeoclcs_OCLMessageArgCS)

@given(instance=completeoclcs_TypedRefCS_strategy)
@settings(max_examples=50)
def test_completeoclcs_typedrefcs_instantiation(instance):
    assert isinstance(instance, completeoclcs_TypedRefCS)

@given(instance=completeoclcs_ExpSpecificationCS_strategy)
@settings(max_examples=50)
def test_completeoclcs_expspecificationcs_instantiation(instance):
    assert isinstance(instance, completeoclcs_ExpSpecificationCS)

@given(instance=TypedElementCS_strategy)
@settings(max_examples=50)
def test_typedelementcs_instantiation(instance):
    assert isinstance(instance, TypedElementCS)

@given(instance=PathNameDeclCS_strategy)
@settings(max_examples=50)
def test_pathnamedeclcs_instantiation(instance):
    assert isinstance(instance, PathNameDeclCS)

@given(instance=completeoclcs_PackageDeclarationCS_strategy)
@settings(max_examples=50)
def test_completeoclcs_packagedeclarationcs_instantiation(instance):
    assert isinstance(instance, completeoclcs_PackageDeclarationCS)

@given(instance=completeoclcs_ContextDeclCS_strategy)
@settings(max_examples=50)
def test_completeoclcs_contextdeclcs_instantiation(instance):
    assert isinstance(instance, completeoclcs_ContextDeclCS)

@given(instance=RootCS_strategy)
@settings(max_examples=50)
def test_rootcs_instantiation(instance):
    assert isinstance(instance, RootCS)

@given(instance=NamespaceCS_strategy)
@settings(max_examples=50)
def test_namespacecs_instantiation(instance):
    assert isinstance(instance, NamespaceCS)

@given(instance=completeoclcs_CompleteOCLDocumentCS_strategy)
@settings(max_examples=50)
def test_completeoclcs_completeocldocumentcs_instantiation(instance):
    assert isinstance(instance, completeoclcs_CompleteOCLDocumentCS)

@given(instance=completeoclcs_Class_strategy)
@settings(max_examples=50)
def test_completeoclcs_class_instantiation(instance):
    assert isinstance(instance, completeoclcs_Class)

@given(instance=completeoclcs_ConstraintCS_strategy)
@settings(max_examples=50)
def test_completeoclcs_constraintcs_instantiation(instance):
    assert isinstance(instance, completeoclcs_ConstraintCS)

@given(instance=completeoclcs_DefCS_strategy)
@settings(max_examples=50)
def test_completeoclcs_defcs_instantiation(instance):
    assert isinstance(instance, completeoclcs_DefCS)



@given(instance=completeoclcs_DefCS_strategy)
def test_completeoclcs_defcs_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=TemplateableElementCS_strategy)
@settings(max_examples=50)
def test_templateableelementcs_instantiation(instance):
    assert isinstance(instance, TemplateableElementCS)

@given(instance=completeoclcs_DefOperationCS_strategy)
@settings(max_examples=50)
def test_completeoclcs_defoperationcs_instantiation(instance):
    assert isinstance(instance, completeoclcs_DefOperationCS)

@given(instance=completeoclcs_OperationContextDeclCS_strategy)
@settings(max_examples=50)
def test_completeoclcs_operationcontextdeclcs_instantiation(instance):
    assert isinstance(instance, completeoclcs_OperationContextDeclCS)

@given(instance=ContextDeclCS_strategy)
@settings(max_examples=50)
def test_contextdeclcs_instantiation(instance):
    assert isinstance(instance, ContextDeclCS)

@given(instance=completeoclcs_FeatureContextDeclCS_strategy)
@settings(max_examples=50)
def test_completeoclcs_featurecontextdeclcs_instantiation(instance):
    assert isinstance(instance, completeoclcs_FeatureContextDeclCS)

@given(instance=completeoclcs_ClassifierContextDeclCS_strategy)
@settings(max_examples=50)
def test_completeoclcs_classifiercontextdeclcs_instantiation(instance):
    assert isinstance(instance, completeoclcs_ClassifierContextDeclCS)



@given(instance=completeoclcs_ClassifierContextDeclCS_strategy)
def test_completeoclcs_classifiercontextdeclcs_selfName_setter(instance):
    original = instance.selfName
    instance.selfName = original
    assert instance.selfName == original
