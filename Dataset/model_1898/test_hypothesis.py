import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    EReference,
    emig_Reference,
    EAttribute,
    emig_Attribute,
    EClass,
    emig_Class,
    EPackage,
    emig_Package,
    emig_EObject,
    Migrator,
    emig_MigratorDX,
    emig_MigratorSX,
    emig_EStructuralFeature,
    emig_EReference,
    emig_EAttribute,
    emig_EClass,
    OpDef,
    emig_EAttributeOpDef,
    emig_EClassOpDef,
    emig_EReferenceOpDef,
    emig_EPackageOpDef,
    emig_EPackage,
    LocatedElement,
    emig_DotNavigationObjSX,
    emig_setterDef,
    emig_Artifact,
    emig_Migrator,
    emig_FilterMigrator,
    emig_OpDef,
    emig_DotNavigationObjDX,
    emig_RewritingRule,
    emig_Parameter,
    emig_LocatedElement,
    emig_Rule,
    emig_MigrationProgram,
    emig_MigrationLibrary,
    emig_MyModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ereference_is_not_abstract():
    assert not inspect.isabstract(EReference)


def test_ereference_constructor_exists():
    assert callable(EReference.__init__)


def test_ereference_constructor_args():
    sig = inspect.signature(EReference.__init__)
    params = list(sig.parameters.keys())



def test_emig_reference_is_not_abstract():
    assert not inspect.isabstract(emig_Reference)


def test_emig_reference_constructor_exists():
    assert callable(emig_Reference.__init__)


def test_emig_reference_constructor_args():
    sig = inspect.signature(emig_Reference.__init__)
    params = list(sig.parameters.keys())



def test_eattribute_is_not_abstract():
    assert not inspect.isabstract(EAttribute)


def test_eattribute_constructor_exists():
    assert callable(EAttribute.__init__)


def test_eattribute_constructor_args():
    sig = inspect.signature(EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_emig_attribute_is_not_abstract():
    assert not inspect.isabstract(emig_Attribute)


def test_emig_attribute_constructor_exists():
    assert callable(emig_Attribute.__init__)


def test_emig_attribute_constructor_args():
    sig = inspect.signature(emig_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_eclass_is_not_abstract():
    assert not inspect.isabstract(EClass)


def test_eclass_constructor_exists():
    assert callable(EClass.__init__)


def test_eclass_constructor_args():
    sig = inspect.signature(EClass.__init__)
    params = list(sig.parameters.keys())



def test_emig_class_is_not_abstract():
    assert not inspect.isabstract(emig_Class)


def test_emig_class_constructor_exists():
    assert callable(emig_Class.__init__)


def test_emig_class_constructor_args():
    sig = inspect.signature(emig_Class.__init__)
    params = list(sig.parameters.keys())



def test_epackage_is_not_abstract():
    assert not inspect.isabstract(EPackage)


def test_epackage_constructor_exists():
    assert callable(EPackage.__init__)


def test_epackage_constructor_args():
    sig = inspect.signature(EPackage.__init__)
    params = list(sig.parameters.keys())



def test_emig_package_is_not_abstract():
    assert not inspect.isabstract(emig_Package)


def test_emig_package_constructor_exists():
    assert callable(emig_Package.__init__)


def test_emig_package_constructor_args():
    sig = inspect.signature(emig_Package.__init__)
    params = list(sig.parameters.keys())



def test_emig_eobject_is_not_abstract():
    assert not inspect.isabstract(emig_EObject)


def test_emig_eobject_constructor_exists():
    assert callable(emig_EObject.__init__)


def test_emig_eobject_constructor_args():
    sig = inspect.signature(emig_EObject.__init__)
    params = list(sig.parameters.keys())



def test_migrator_is_not_abstract():
    assert not inspect.isabstract(Migrator)


def test_migrator_constructor_exists():
    assert callable(Migrator.__init__)


def test_migrator_constructor_args():
    sig = inspect.signature(Migrator.__init__)
    params = list(sig.parameters.keys())



def test_emig_migratordx_is_not_abstract():
    assert not inspect.isabstract(emig_MigratorDX)


def test_emig_migratordx_constructor_exists():
    assert callable(emig_MigratorDX.__init__)


def test_emig_migratordx_constructor_args():
    sig = inspect.signature(emig_MigratorDX.__init__)
    params = list(sig.parameters.keys())



def test_emig_migratorsx_is_not_abstract():
    assert not inspect.isabstract(emig_MigratorSX)


def test_emig_migratorsx_constructor_exists():
    assert callable(emig_MigratorSX.__init__)


def test_emig_migratorsx_constructor_args():
    sig = inspect.signature(emig_MigratorSX.__init__)
    params = list(sig.parameters.keys())



def test_emig_estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(emig_EStructuralFeature)


def test_emig_estructuralfeature_constructor_exists():
    assert callable(emig_EStructuralFeature.__init__)


def test_emig_estructuralfeature_constructor_args():
    sig = inspect.signature(emig_EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_emig_ereference_is_not_abstract():
    assert not inspect.isabstract(emig_EReference)


def test_emig_ereference_constructor_exists():
    assert callable(emig_EReference.__init__)


def test_emig_ereference_constructor_args():
    sig = inspect.signature(emig_EReference.__init__)
    params = list(sig.parameters.keys())



def test_emig_eattribute_is_not_abstract():
    assert not inspect.isabstract(emig_EAttribute)


def test_emig_eattribute_constructor_exists():
    assert callable(emig_EAttribute.__init__)


def test_emig_eattribute_constructor_args():
    sig = inspect.signature(emig_EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_emig_eclass_is_not_abstract():
    assert not inspect.isabstract(emig_EClass)


def test_emig_eclass_constructor_exists():
    assert callable(emig_EClass.__init__)


def test_emig_eclass_constructor_args():
    sig = inspect.signature(emig_EClass.__init__)
    params = list(sig.parameters.keys())



def test_opdef_is_not_abstract():
    assert not inspect.isabstract(OpDef)


def test_opdef_constructor_exists():
    assert callable(OpDef.__init__)


def test_opdef_constructor_args():
    sig = inspect.signature(OpDef.__init__)
    params = list(sig.parameters.keys())



def test_emig_eattributeopdef_is_not_abstract():
    assert not inspect.isabstract(emig_EAttributeOpDef)


def test_emig_eattributeopdef_constructor_exists():
    assert callable(emig_EAttributeOpDef.__init__)


def test_emig_eattributeopdef_constructor_args():
    sig = inspect.signature(emig_EAttributeOpDef.__init__)
    params = list(sig.parameters.keys())



def test_emig_eclassopdef_is_not_abstract():
    assert not inspect.isabstract(emig_EClassOpDef)


def test_emig_eclassopdef_constructor_exists():
    assert callable(emig_EClassOpDef.__init__)


def test_emig_eclassopdef_constructor_args():
    sig = inspect.signature(emig_EClassOpDef.__init__)
    params = list(sig.parameters.keys())



def test_emig_ereferenceopdef_is_not_abstract():
    assert not inspect.isabstract(emig_EReferenceOpDef)


def test_emig_ereferenceopdef_constructor_exists():
    assert callable(emig_EReferenceOpDef.__init__)


def test_emig_ereferenceopdef_constructor_args():
    sig = inspect.signature(emig_EReferenceOpDef.__init__)
    params = list(sig.parameters.keys())



def test_emig_epackageopdef_is_not_abstract():
    assert not inspect.isabstract(emig_EPackageOpDef)


def test_emig_epackageopdef_constructor_exists():
    assert callable(emig_EPackageOpDef.__init__)


def test_emig_epackageopdef_constructor_args():
    sig = inspect.signature(emig_EPackageOpDef.__init__)
    params = list(sig.parameters.keys())



def test_emig_epackage_is_not_abstract():
    assert not inspect.isabstract(emig_EPackage)


def test_emig_epackage_constructor_exists():
    assert callable(emig_EPackage.__init__)


def test_emig_epackage_constructor_args():
    sig = inspect.signature(emig_EPackage.__init__)
    params = list(sig.parameters.keys())



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_emig_dotnavigationobjsx_is_not_abstract():
    assert not inspect.isabstract(emig_DotNavigationObjSX)


def test_emig_dotnavigationobjsx_constructor_exists():
    assert callable(emig_DotNavigationObjSX.__init__)


def test_emig_dotnavigationobjsx_constructor_args():
    sig = inspect.signature(emig_DotNavigationObjSX.__init__)
    params = list(sig.parameters.keys())



def test_emig_setterdef_is_not_abstract():
    assert not inspect.isabstract(emig_setterDef)


def test_emig_setterdef_constructor_exists():
    assert callable(emig_setterDef.__init__)


def test_emig_setterdef_constructor_args():
    sig = inspect.signature(emig_setterDef.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_emig_setterdef_has_operator():
    assert hasattr(emig_setterDef, "operator")
    descriptor = None
    for klass in emig_setterDef.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_emig_artifact_is_not_abstract():
    assert not inspect.isabstract(emig_Artifact)


def test_emig_artifact_constructor_exists():
    assert callable(emig_Artifact.__init__)


def test_emig_artifact_constructor_args():
    sig = inspect.signature(emig_Artifact.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_emig_artifact_has_type():
    assert hasattr(emig_Artifact, "type")
    descriptor = None
    for klass in emig_Artifact.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_emig_migrator_is_not_abstract():
    assert not inspect.isabstract(emig_Migrator)


def test_emig_migrator_constructor_exists():
    assert callable(emig_Migrator.__init__)


def test_emig_migrator_constructor_args():
    sig = inspect.signature(emig_Migrator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emig_migrator_has_name():
    assert hasattr(emig_Migrator, "name")
    descriptor = None
    for klass in emig_Migrator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emig_filtermigrator_is_not_abstract():
    assert not inspect.isabstract(emig_FilterMigrator)


def test_emig_filtermigrator_constructor_exists():
    assert callable(emig_FilterMigrator.__init__)


def test_emig_filtermigrator_constructor_args():
    sig = inspect.signature(emig_FilterMigrator.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_emig_filtermigrator_has_op():
    assert hasattr(emig_FilterMigrator, "op")
    descriptor = None
    for klass in emig_FilterMigrator.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_emig_opdef_is_not_abstract():
    assert not inspect.isabstract(emig_OpDef)


def test_emig_opdef_constructor_exists():
    assert callable(emig_OpDef.__init__)


def test_emig_opdef_constructor_args():
    sig = inspect.signature(emig_OpDef.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_emig_opdef_has_op():
    assert hasattr(emig_OpDef, "op")
    descriptor = None
    for klass in emig_OpDef.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_emig_dotnavigationobjdx_is_not_abstract():
    assert not inspect.isabstract(emig_DotNavigationObjDX)


def test_emig_dotnavigationobjdx_constructor_exists():
    assert callable(emig_DotNavigationObjDX.__init__)


def test_emig_dotnavigationobjdx_constructor_args():
    sig = inspect.signature(emig_DotNavigationObjDX.__init__)
    params = list(sig.parameters.keys())



def test_emig_rewritingrule_is_not_abstract():
    assert not inspect.isabstract(emig_RewritingRule)


def test_emig_rewritingrule_constructor_exists():
    assert callable(emig_RewritingRule.__init__)


def test_emig_rewritingrule_constructor_args():
    sig = inspect.signature(emig_RewritingRule.__init__)
    params = list(sig.parameters.keys())



def test_emig_parameter_is_not_abstract():
    assert not inspect.isabstract(emig_Parameter)


def test_emig_parameter_constructor_exists():
    assert callable(emig_Parameter.__init__)


def test_emig_parameter_constructor_args():
    sig = inspect.signature(emig_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emig_parameter_has_name():
    assert hasattr(emig_Parameter, "name")
    descriptor = None
    for klass in emig_Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emig_locatedelement_is_not_abstract():
    assert not inspect.isabstract(emig_LocatedElement)


def test_emig_locatedelement_constructor_exists():
    assert callable(emig_LocatedElement.__init__)


def test_emig_locatedelement_constructor_args():
    sig = inspect.signature(emig_LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "endline" in params, "Missing parameter 'endline'"
    assert "endoffset" in params, "Missing parameter 'endoffset'"
    assert "line" in params, "Missing parameter 'line'"
    assert "offset" in params, "Missing parameter 'offset'"

def test_emig_locatedelement_has_endline():
    assert hasattr(emig_LocatedElement, "endline")
    descriptor = None
    for klass in emig_LocatedElement.__mro__:
        if "endline" in klass.__dict__:
            descriptor = klass.__dict__["endline"]
            break
    assert isinstance(descriptor, property)

def test_emig_locatedelement_has_endoffset():
    assert hasattr(emig_LocatedElement, "endoffset")
    descriptor = None
    for klass in emig_LocatedElement.__mro__:
        if "endoffset" in klass.__dict__:
            descriptor = klass.__dict__["endoffset"]
            break
    assert isinstance(descriptor, property)

def test_emig_locatedelement_has_line():
    assert hasattr(emig_LocatedElement, "line")
    descriptor = None
    for klass in emig_LocatedElement.__mro__:
        if "line" in klass.__dict__:
            descriptor = klass.__dict__["line"]
            break
    assert isinstance(descriptor, property)

def test_emig_locatedelement_has_offset():
    assert hasattr(emig_LocatedElement, "offset")
    descriptor = None
    for klass in emig_LocatedElement.__mro__:
        if "offset" in klass.__dict__:
            descriptor = klass.__dict__["offset"]
            break
    assert isinstance(descriptor, property)



def test_emig_rule_is_not_abstract():
    assert not inspect.isabstract(emig_Rule)


def test_emig_rule_constructor_exists():
    assert callable(emig_Rule.__init__)


def test_emig_rule_constructor_args():
    sig = inspect.signature(emig_Rule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emig_rule_has_name():
    assert hasattr(emig_Rule, "name")
    descriptor = None
    for klass in emig_Rule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emig_migrationprogram_is_not_abstract():
    assert not inspect.isabstract(emig_MigrationProgram)


def test_emig_migrationprogram_constructor_exists():
    assert callable(emig_MigrationProgram.__init__)


def test_emig_migrationprogram_constructor_args():
    sig = inspect.signature(emig_MigrationProgram.__init__)
    params = list(sig.parameters.keys())
    assert "migr" in params, "Missing parameter 'migr'"
    assert "libs" in params, "Missing parameter 'libs'"
    assert "artifact" in params, "Missing parameter 'artifact'"
    assert "name" in params, "Missing parameter 'name'"
    assert "delta" in params, "Missing parameter 'delta'"

def test_emig_migrationprogram_has_migr():
    assert hasattr(emig_MigrationProgram, "migr")
    descriptor = None
    for klass in emig_MigrationProgram.__mro__:
        if "migr" in klass.__dict__:
            descriptor = klass.__dict__["migr"]
            break
    assert isinstance(descriptor, property)

def test_emig_migrationprogram_has_libs():
    assert hasattr(emig_MigrationProgram, "libs")
    descriptor = None
    for klass in emig_MigrationProgram.__mro__:
        if "libs" in klass.__dict__:
            descriptor = klass.__dict__["libs"]
            break
    assert isinstance(descriptor, property)

def test_emig_migrationprogram_has_artifact():
    assert hasattr(emig_MigrationProgram, "artifact")
    descriptor = None
    for klass in emig_MigrationProgram.__mro__:
        if "artifact" in klass.__dict__:
            descriptor = klass.__dict__["artifact"]
            break
    assert isinstance(descriptor, property)

def test_emig_migrationprogram_has_name():
    assert hasattr(emig_MigrationProgram, "name")
    descriptor = None
    for klass in emig_MigrationProgram.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_emig_migrationprogram_has_delta():
    assert hasattr(emig_MigrationProgram, "delta")
    descriptor = None
    for klass in emig_MigrationProgram.__mro__:
        if "delta" in klass.__dict__:
            descriptor = klass.__dict__["delta"]
            break
    assert isinstance(descriptor, property)



def test_emig_migrationlibrary_is_not_abstract():
    assert not inspect.isabstract(emig_MigrationLibrary)


def test_emig_migrationlibrary_constructor_exists():
    assert callable(emig_MigrationLibrary.__init__)


def test_emig_migrationlibrary_constructor_args():
    sig = inspect.signature(emig_MigrationLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emig_migrationlibrary_has_name():
    assert hasattr(emig_MigrationLibrary, "name")
    descriptor = None
    for klass in emig_MigrationLibrary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emig_mymodel_is_not_abstract():
    assert not inspect.isabstract(emig_MyModel)


def test_emig_mymodel_constructor_exists():
    assert callable(emig_MyModel.__init__)


def test_emig_mymodel_constructor_args():
    sig = inspect.signature(emig_MyModel.__init__)
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
EReference_strategy = st.builds(
    EReference,
)
emig_Reference_strategy = st.builds(
    emig_Reference,
)
EAttribute_strategy = st.builds(
    EAttribute,
)
emig_Attribute_strategy = st.builds(
    emig_Attribute,
)
EClass_strategy = st.builds(
    EClass,
)
emig_Class_strategy = st.builds(
    emig_Class,
)
EPackage_strategy = st.builds(
    EPackage,
)
emig_Package_strategy = st.builds(
    emig_Package,
)
emig_EObject_strategy = st.builds(
    emig_EObject,
)
Migrator_strategy = st.builds(
    Migrator,
)
emig_MigratorDX_strategy = st.builds(
    emig_MigratorDX,
)
emig_MigratorSX_strategy = st.builds(
    emig_MigratorSX,
)
emig_EStructuralFeature_strategy = st.builds(
    emig_EStructuralFeature,
)
emig_EReference_strategy = st.builds(
    emig_EReference,
)
emig_EAttribute_strategy = st.builds(
    emig_EAttribute,
)
emig_EClass_strategy = st.builds(
    emig_EClass,
)
OpDef_strategy = st.builds(
    OpDef,
)
emig_EAttributeOpDef_strategy = st.builds(
    emig_EAttributeOpDef,
)
emig_EClassOpDef_strategy = st.builds(
    emig_EClassOpDef,
)
emig_EReferenceOpDef_strategy = st.builds(
    emig_EReferenceOpDef,
)
emig_EPackageOpDef_strategy = st.builds(
    emig_EPackageOpDef,
)
emig_EPackage_strategy = st.builds(
    emig_EPackage,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
emig_DotNavigationObjSX_strategy = st.builds(
    emig_DotNavigationObjSX,
)
emig_setterDef_strategy = st.builds(
    emig_setterDef,
    operator=
        safe_text
)
emig_Artifact_strategy = st.builds(
    emig_Artifact,
    type=
        safe_text
)
emig_Migrator_strategy = st.builds(
    emig_Migrator,
    name=
        safe_text
)
emig_FilterMigrator_strategy = st.builds(
    emig_FilterMigrator,
    op=
        safe_text
)
emig_OpDef_strategy = st.builds(
    emig_OpDef,
    op=
        safe_text
)
emig_DotNavigationObjDX_strategy = st.builds(
    emig_DotNavigationObjDX,
)
emig_RewritingRule_strategy = st.builds(
    emig_RewritingRule,
)
emig_Parameter_strategy = st.builds(
    emig_Parameter,
    name=
        safe_text
)
emig_LocatedElement_strategy = st.builds(
    emig_LocatedElement,
    endline=
        st.integers(),
    endoffset=
        st.integers(),
    line=
        st.integers(),
    offset=
        st.integers()
)
emig_Rule_strategy = st.builds(
    emig_Rule,
    name=
        safe_text
)
emig_MigrationProgram_strategy = st.builds(
    emig_MigrationProgram,
    migr=
        safe_text,
    libs=
        safe_text,
    artifact=
        safe_text,
    name=
        safe_text,
    delta=
        safe_text
)
emig_MigrationLibrary_strategy = st.builds(
    emig_MigrationLibrary,
    name=
        safe_text
)
emig_MyModel_strategy = st.builds(
    emig_MyModel,
)

@given(instance=EReference_strategy)
@settings(max_examples=50)
def test_ereference_instantiation(instance):
    assert isinstance(instance, EReference)

@given(instance=emig_Reference_strategy)
@settings(max_examples=50)
def test_emig_reference_instantiation(instance):
    assert isinstance(instance, emig_Reference)

@given(instance=EAttribute_strategy)
@settings(max_examples=50)
def test_eattribute_instantiation(instance):
    assert isinstance(instance, EAttribute)

@given(instance=emig_Attribute_strategy)
@settings(max_examples=50)
def test_emig_attribute_instantiation(instance):
    assert isinstance(instance, emig_Attribute)

@given(instance=EClass_strategy)
@settings(max_examples=50)
def test_eclass_instantiation(instance):
    assert isinstance(instance, EClass)

@given(instance=emig_Class_strategy)
@settings(max_examples=50)
def test_emig_class_instantiation(instance):
    assert isinstance(instance, emig_Class)

@given(instance=EPackage_strategy)
@settings(max_examples=50)
def test_epackage_instantiation(instance):
    assert isinstance(instance, EPackage)

@given(instance=emig_Package_strategy)
@settings(max_examples=50)
def test_emig_package_instantiation(instance):
    assert isinstance(instance, emig_Package)

@given(instance=emig_EObject_strategy)
@settings(max_examples=50)
def test_emig_eobject_instantiation(instance):
    assert isinstance(instance, emig_EObject)

@given(instance=Migrator_strategy)
@settings(max_examples=50)
def test_migrator_instantiation(instance):
    assert isinstance(instance, Migrator)

@given(instance=emig_MigratorDX_strategy)
@settings(max_examples=50)
def test_emig_migratordx_instantiation(instance):
    assert isinstance(instance, emig_MigratorDX)

@given(instance=emig_MigratorSX_strategy)
@settings(max_examples=50)
def test_emig_migratorsx_instantiation(instance):
    assert isinstance(instance, emig_MigratorSX)

@given(instance=emig_EStructuralFeature_strategy)
@settings(max_examples=50)
def test_emig_estructuralfeature_instantiation(instance):
    assert isinstance(instance, emig_EStructuralFeature)

@given(instance=emig_EReference_strategy)
@settings(max_examples=50)
def test_emig_ereference_instantiation(instance):
    assert isinstance(instance, emig_EReference)

@given(instance=emig_EAttribute_strategy)
@settings(max_examples=50)
def test_emig_eattribute_instantiation(instance):
    assert isinstance(instance, emig_EAttribute)

@given(instance=emig_EClass_strategy)
@settings(max_examples=50)
def test_emig_eclass_instantiation(instance):
    assert isinstance(instance, emig_EClass)

@given(instance=OpDef_strategy)
@settings(max_examples=50)
def test_opdef_instantiation(instance):
    assert isinstance(instance, OpDef)

@given(instance=emig_EAttributeOpDef_strategy)
@settings(max_examples=50)
def test_emig_eattributeopdef_instantiation(instance):
    assert isinstance(instance, emig_EAttributeOpDef)

@given(instance=emig_EClassOpDef_strategy)
@settings(max_examples=50)
def test_emig_eclassopdef_instantiation(instance):
    assert isinstance(instance, emig_EClassOpDef)

@given(instance=emig_EReferenceOpDef_strategy)
@settings(max_examples=50)
def test_emig_ereferenceopdef_instantiation(instance):
    assert isinstance(instance, emig_EReferenceOpDef)

@given(instance=emig_EPackageOpDef_strategy)
@settings(max_examples=50)
def test_emig_epackageopdef_instantiation(instance):
    assert isinstance(instance, emig_EPackageOpDef)

@given(instance=emig_EPackage_strategy)
@settings(max_examples=50)
def test_emig_epackage_instantiation(instance):
    assert isinstance(instance, emig_EPackage)

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=emig_DotNavigationObjSX_strategy)
@settings(max_examples=50)
def test_emig_dotnavigationobjsx_instantiation(instance):
    assert isinstance(instance, emig_DotNavigationObjSX)

@given(instance=emig_setterDef_strategy)
@settings(max_examples=50)
def test_emig_setterdef_instantiation(instance):
    assert isinstance(instance, emig_setterDef)



@given(instance=emig_setterDef_strategy)
def test_emig_setterdef_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=emig_Artifact_strategy)
@settings(max_examples=50)
def test_emig_artifact_instantiation(instance):
    assert isinstance(instance, emig_Artifact)



@given(instance=emig_Artifact_strategy)
def test_emig_artifact_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=emig_Migrator_strategy)
@settings(max_examples=50)
def test_emig_migrator_instantiation(instance):
    assert isinstance(instance, emig_Migrator)



@given(instance=emig_Migrator_strategy)
def test_emig_migrator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=emig_FilterMigrator_strategy)
@settings(max_examples=50)
def test_emig_filtermigrator_instantiation(instance):
    assert isinstance(instance, emig_FilterMigrator)



@given(instance=emig_FilterMigrator_strategy)
def test_emig_filtermigrator_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=emig_OpDef_strategy)
@settings(max_examples=50)
def test_emig_opdef_instantiation(instance):
    assert isinstance(instance, emig_OpDef)



@given(instance=emig_OpDef_strategy)
def test_emig_opdef_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=emig_DotNavigationObjDX_strategy)
@settings(max_examples=50)
def test_emig_dotnavigationobjdx_instantiation(instance):
    assert isinstance(instance, emig_DotNavigationObjDX)

@given(instance=emig_RewritingRule_strategy)
@settings(max_examples=50)
def test_emig_rewritingrule_instantiation(instance):
    assert isinstance(instance, emig_RewritingRule)

@given(instance=emig_Parameter_strategy)
@settings(max_examples=50)
def test_emig_parameter_instantiation(instance):
    assert isinstance(instance, emig_Parameter)



@given(instance=emig_Parameter_strategy)
def test_emig_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=emig_LocatedElement_strategy)
@settings(max_examples=50)
def test_emig_locatedelement_instantiation(instance):
    assert isinstance(instance, emig_LocatedElement)



@given(instance=emig_LocatedElement_strategy)
def test_emig_locatedelement_endline_setter(instance):
    original = instance.endline
    instance.endline = original
    assert instance.endline == original



@given(instance=emig_LocatedElement_strategy)
def test_emig_locatedelement_endoffset_setter(instance):
    original = instance.endoffset
    instance.endoffset = original
    assert instance.endoffset == original



@given(instance=emig_LocatedElement_strategy)
def test_emig_locatedelement_line_setter(instance):
    original = instance.line
    instance.line = original
    assert instance.line == original



@given(instance=emig_LocatedElement_strategy)
def test_emig_locatedelement_offset_setter(instance):
    original = instance.offset
    instance.offset = original
    assert instance.offset == original

@given(instance=emig_Rule_strategy)
@settings(max_examples=50)
def test_emig_rule_instantiation(instance):
    assert isinstance(instance, emig_Rule)



@given(instance=emig_Rule_strategy)
def test_emig_rule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=emig_MigrationProgram_strategy)
@settings(max_examples=50)
def test_emig_migrationprogram_instantiation(instance):
    assert isinstance(instance, emig_MigrationProgram)



@given(instance=emig_MigrationProgram_strategy)
def test_emig_migrationprogram_migr_setter(instance):
    original = instance.migr
    instance.migr = original
    assert instance.migr == original



@given(instance=emig_MigrationProgram_strategy)
def test_emig_migrationprogram_libs_setter(instance):
    original = instance.libs
    instance.libs = original
    assert instance.libs == original



@given(instance=emig_MigrationProgram_strategy)
def test_emig_migrationprogram_artifact_setter(instance):
    original = instance.artifact
    instance.artifact = original
    assert instance.artifact == original



@given(instance=emig_MigrationProgram_strategy)
def test_emig_migrationprogram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=emig_MigrationProgram_strategy)
def test_emig_migrationprogram_delta_setter(instance):
    original = instance.delta
    instance.delta = original
    assert instance.delta == original

@given(instance=emig_MigrationLibrary_strategy)
@settings(max_examples=50)
def test_emig_migrationlibrary_instantiation(instance):
    assert isinstance(instance, emig_MigrationLibrary)



@given(instance=emig_MigrationLibrary_strategy)
def test_emig_migrationlibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=emig_MyModel_strategy)
@settings(max_examples=50)
def test_emig_mymodel_instantiation(instance):
    assert isinstance(instance, emig_MyModel)
