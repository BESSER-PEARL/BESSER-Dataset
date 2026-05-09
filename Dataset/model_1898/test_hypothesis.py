import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    EReference,
    emig::Reference,
    EAttribute,
    emig::Attribute,
    EClass,
    emig::Class,
    EPackage,
    emig::Package,
    emig::EObject,
    Migrator,
    emig::MigratorDX,
    emig::MigratorSX,
    emig::EStructuralFeature,
    emig::EReference,
    emig::EAttribute,
    emig::EClass,
    OpDef,
    emig::EReferenceOpDef,
    emig::EClassOpDef,
    emig::EAttributeOpDef,
    emig::EPackageOpDef,
    emig::EPackage,
    LocatedElement,
    emig::setterDef,
    emig::Artifact,
    emig::RewritingRule,
    emig::Migrator,
    emig::DotNavigationObjSX,
    emig::Parameter,
    emig::OpDef,
    emig::FilterMigrator,
    emig::DotNavigationObjDX,
    emig::LocatedElement,
    emig::Rule,
    emig::MigrationProgram,
    emig::MigrationLibrary,
    emig::MyModel,
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



def test_emig::reference_is_not_abstract():
    assert not inspect.isabstract(emig::Reference)


def test_emig::reference_constructor_exists():
    assert callable(emig::Reference.__init__)


def test_emig::reference_constructor_args():
    sig = inspect.signature(emig::Reference.__init__)
    params = list(sig.parameters.keys())



def test_eattribute_is_not_abstract():
    assert not inspect.isabstract(EAttribute)


def test_eattribute_constructor_exists():
    assert callable(EAttribute.__init__)


def test_eattribute_constructor_args():
    sig = inspect.signature(EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_emig::attribute_is_not_abstract():
    assert not inspect.isabstract(emig::Attribute)


def test_emig::attribute_constructor_exists():
    assert callable(emig::Attribute.__init__)


def test_emig::attribute_constructor_args():
    sig = inspect.signature(emig::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_eclass_is_not_abstract():
    assert not inspect.isabstract(EClass)


def test_eclass_constructor_exists():
    assert callable(EClass.__init__)


def test_eclass_constructor_args():
    sig = inspect.signature(EClass.__init__)
    params = list(sig.parameters.keys())



def test_emig::class_is_not_abstract():
    assert not inspect.isabstract(emig::Class)


def test_emig::class_constructor_exists():
    assert callable(emig::Class.__init__)


def test_emig::class_constructor_args():
    sig = inspect.signature(emig::Class.__init__)
    params = list(sig.parameters.keys())



def test_epackage_is_not_abstract():
    assert not inspect.isabstract(EPackage)


def test_epackage_constructor_exists():
    assert callable(EPackage.__init__)


def test_epackage_constructor_args():
    sig = inspect.signature(EPackage.__init__)
    params = list(sig.parameters.keys())



def test_emig::package_is_not_abstract():
    assert not inspect.isabstract(emig::Package)


def test_emig::package_constructor_exists():
    assert callable(emig::Package.__init__)


def test_emig::package_constructor_args():
    sig = inspect.signature(emig::Package.__init__)
    params = list(sig.parameters.keys())



def test_emig::eobject_is_not_abstract():
    assert not inspect.isabstract(emig::EObject)


def test_emig::eobject_constructor_exists():
    assert callable(emig::EObject.__init__)


def test_emig::eobject_constructor_args():
    sig = inspect.signature(emig::EObject.__init__)
    params = list(sig.parameters.keys())



def test_migrator_is_not_abstract():
    assert not inspect.isabstract(Migrator)


def test_migrator_constructor_exists():
    assert callable(Migrator.__init__)


def test_migrator_constructor_args():
    sig = inspect.signature(Migrator.__init__)
    params = list(sig.parameters.keys())



def test_emig::migratordx_is_not_abstract():
    assert not inspect.isabstract(emig::MigratorDX)


def test_emig::migratordx_constructor_exists():
    assert callable(emig::MigratorDX.__init__)


def test_emig::migratordx_constructor_args():
    sig = inspect.signature(emig::MigratorDX.__init__)
    params = list(sig.parameters.keys())



def test_emig::migratorsx_is_not_abstract():
    assert not inspect.isabstract(emig::MigratorSX)


def test_emig::migratorsx_constructor_exists():
    assert callable(emig::MigratorSX.__init__)


def test_emig::migratorsx_constructor_args():
    sig = inspect.signature(emig::MigratorSX.__init__)
    params = list(sig.parameters.keys())



def test_emig::estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(emig::EStructuralFeature)


def test_emig::estructuralfeature_constructor_exists():
    assert callable(emig::EStructuralFeature.__init__)


def test_emig::estructuralfeature_constructor_args():
    sig = inspect.signature(emig::EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_emig::ereference_is_not_abstract():
    assert not inspect.isabstract(emig::EReference)


def test_emig::ereference_constructor_exists():
    assert callable(emig::EReference.__init__)


def test_emig::ereference_constructor_args():
    sig = inspect.signature(emig::EReference.__init__)
    params = list(sig.parameters.keys())



def test_emig::eattribute_is_not_abstract():
    assert not inspect.isabstract(emig::EAttribute)


def test_emig::eattribute_constructor_exists():
    assert callable(emig::EAttribute.__init__)


def test_emig::eattribute_constructor_args():
    sig = inspect.signature(emig::EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_emig::eclass_is_not_abstract():
    assert not inspect.isabstract(emig::EClass)


def test_emig::eclass_constructor_exists():
    assert callable(emig::EClass.__init__)


def test_emig::eclass_constructor_args():
    sig = inspect.signature(emig::EClass.__init__)
    params = list(sig.parameters.keys())



def test_opdef_is_not_abstract():
    assert not inspect.isabstract(OpDef)


def test_opdef_constructor_exists():
    assert callable(OpDef.__init__)


def test_opdef_constructor_args():
    sig = inspect.signature(OpDef.__init__)
    params = list(sig.parameters.keys())



def test_emig::ereferenceopdef_is_not_abstract():
    assert not inspect.isabstract(emig::EReferenceOpDef)


def test_emig::ereferenceopdef_constructor_exists():
    assert callable(emig::EReferenceOpDef.__init__)


def test_emig::ereferenceopdef_constructor_args():
    sig = inspect.signature(emig::EReferenceOpDef.__init__)
    params = list(sig.parameters.keys())



def test_emig::eclassopdef_is_not_abstract():
    assert not inspect.isabstract(emig::EClassOpDef)


def test_emig::eclassopdef_constructor_exists():
    assert callable(emig::EClassOpDef.__init__)


def test_emig::eclassopdef_constructor_args():
    sig = inspect.signature(emig::EClassOpDef.__init__)
    params = list(sig.parameters.keys())



def test_emig::eattributeopdef_is_not_abstract():
    assert not inspect.isabstract(emig::EAttributeOpDef)


def test_emig::eattributeopdef_constructor_exists():
    assert callable(emig::EAttributeOpDef.__init__)


def test_emig::eattributeopdef_constructor_args():
    sig = inspect.signature(emig::EAttributeOpDef.__init__)
    params = list(sig.parameters.keys())



def test_emig::epackageopdef_is_not_abstract():
    assert not inspect.isabstract(emig::EPackageOpDef)


def test_emig::epackageopdef_constructor_exists():
    assert callable(emig::EPackageOpDef.__init__)


def test_emig::epackageopdef_constructor_args():
    sig = inspect.signature(emig::EPackageOpDef.__init__)
    params = list(sig.parameters.keys())



def test_emig::epackage_is_not_abstract():
    assert not inspect.isabstract(emig::EPackage)


def test_emig::epackage_constructor_exists():
    assert callable(emig::EPackage.__init__)


def test_emig::epackage_constructor_args():
    sig = inspect.signature(emig::EPackage.__init__)
    params = list(sig.parameters.keys())



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_emig::setterdef_is_not_abstract():
    assert not inspect.isabstract(emig::setterDef)


def test_emig::setterdef_constructor_exists():
    assert callable(emig::setterDef.__init__)


def test_emig::setterdef_constructor_args():
    sig = inspect.signature(emig::setterDef.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_emig::setterdef_has_operator():
    assert hasattr(emig::setterDef, "operator")
    descriptor = None
    for klass in emig::setterDef.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_emig::artifact_is_not_abstract():
    assert not inspect.isabstract(emig::Artifact)


def test_emig::artifact_constructor_exists():
    assert callable(emig::Artifact.__init__)


def test_emig::artifact_constructor_args():
    sig = inspect.signature(emig::Artifact.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_emig::artifact_has_type():
    assert hasattr(emig::Artifact, "type")
    descriptor = None
    for klass in emig::Artifact.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_emig::rewritingrule_is_not_abstract():
    assert not inspect.isabstract(emig::RewritingRule)


def test_emig::rewritingrule_constructor_exists():
    assert callable(emig::RewritingRule.__init__)


def test_emig::rewritingrule_constructor_args():
    sig = inspect.signature(emig::RewritingRule.__init__)
    params = list(sig.parameters.keys())



def test_emig::migrator_is_not_abstract():
    assert not inspect.isabstract(emig::Migrator)


def test_emig::migrator_constructor_exists():
    assert callable(emig::Migrator.__init__)


def test_emig::migrator_constructor_args():
    sig = inspect.signature(emig::Migrator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emig::migrator_has_name():
    assert hasattr(emig::Migrator, "name")
    descriptor = None
    for klass in emig::Migrator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emig::dotnavigationobjsx_is_not_abstract():
    assert not inspect.isabstract(emig::DotNavigationObjSX)


def test_emig::dotnavigationobjsx_constructor_exists():
    assert callable(emig::DotNavigationObjSX.__init__)


def test_emig::dotnavigationobjsx_constructor_args():
    sig = inspect.signature(emig::DotNavigationObjSX.__init__)
    params = list(sig.parameters.keys())



def test_emig::parameter_is_not_abstract():
    assert not inspect.isabstract(emig::Parameter)


def test_emig::parameter_constructor_exists():
    assert callable(emig::Parameter.__init__)


def test_emig::parameter_constructor_args():
    sig = inspect.signature(emig::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emig::parameter_has_name():
    assert hasattr(emig::Parameter, "name")
    descriptor = None
    for klass in emig::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emig::opdef_is_not_abstract():
    assert not inspect.isabstract(emig::OpDef)


def test_emig::opdef_constructor_exists():
    assert callable(emig::OpDef.__init__)


def test_emig::opdef_constructor_args():
    sig = inspect.signature(emig::OpDef.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_emig::opdef_has_op():
    assert hasattr(emig::OpDef, "op")
    descriptor = None
    for klass in emig::OpDef.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_emig::filtermigrator_is_not_abstract():
    assert not inspect.isabstract(emig::FilterMigrator)


def test_emig::filtermigrator_constructor_exists():
    assert callable(emig::FilterMigrator.__init__)


def test_emig::filtermigrator_constructor_args():
    sig = inspect.signature(emig::FilterMigrator.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_emig::filtermigrator_has_op():
    assert hasattr(emig::FilterMigrator, "op")
    descriptor = None
    for klass in emig::FilterMigrator.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_emig::dotnavigationobjdx_is_not_abstract():
    assert not inspect.isabstract(emig::DotNavigationObjDX)


def test_emig::dotnavigationobjdx_constructor_exists():
    assert callable(emig::DotNavigationObjDX.__init__)


def test_emig::dotnavigationobjdx_constructor_args():
    sig = inspect.signature(emig::DotNavigationObjDX.__init__)
    params = list(sig.parameters.keys())



def test_emig::locatedelement_is_not_abstract():
    assert not inspect.isabstract(emig::LocatedElement)


def test_emig::locatedelement_constructor_exists():
    assert callable(emig::LocatedElement.__init__)


def test_emig::locatedelement_constructor_args():
    sig = inspect.signature(emig::LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "line" in params, "Missing parameter 'line'"
    assert "endoffset" in params, "Missing parameter 'endoffset'"
    assert "endline" in params, "Missing parameter 'endline'"
    assert "offset" in params, "Missing parameter 'offset'"

def test_emig::locatedelement_has_line():
    assert hasattr(emig::LocatedElement, "line")
    descriptor = None
    for klass in emig::LocatedElement.__mro__:
        if "line" in klass.__dict__:
            descriptor = klass.__dict__["line"]
            break
    assert isinstance(descriptor, property)

def test_emig::locatedelement_has_endoffset():
    assert hasattr(emig::LocatedElement, "endoffset")
    descriptor = None
    for klass in emig::LocatedElement.__mro__:
        if "endoffset" in klass.__dict__:
            descriptor = klass.__dict__["endoffset"]
            break
    assert isinstance(descriptor, property)

def test_emig::locatedelement_has_endline():
    assert hasattr(emig::LocatedElement, "endline")
    descriptor = None
    for klass in emig::LocatedElement.__mro__:
        if "endline" in klass.__dict__:
            descriptor = klass.__dict__["endline"]
            break
    assert isinstance(descriptor, property)

def test_emig::locatedelement_has_offset():
    assert hasattr(emig::LocatedElement, "offset")
    descriptor = None
    for klass in emig::LocatedElement.__mro__:
        if "offset" in klass.__dict__:
            descriptor = klass.__dict__["offset"]
            break
    assert isinstance(descriptor, property)



def test_emig::rule_is_not_abstract():
    assert not inspect.isabstract(emig::Rule)


def test_emig::rule_constructor_exists():
    assert callable(emig::Rule.__init__)


def test_emig::rule_constructor_args():
    sig = inspect.signature(emig::Rule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emig::rule_has_name():
    assert hasattr(emig::Rule, "name")
    descriptor = None
    for klass in emig::Rule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emig::migrationprogram_is_not_abstract():
    assert not inspect.isabstract(emig::MigrationProgram)


def test_emig::migrationprogram_constructor_exists():
    assert callable(emig::MigrationProgram.__init__)


def test_emig::migrationprogram_constructor_args():
    sig = inspect.signature(emig::MigrationProgram.__init__)
    params = list(sig.parameters.keys())
    assert "delta" in params, "Missing parameter 'delta'"
    assert "name" in params, "Missing parameter 'name'"
    assert "libs" in params, "Missing parameter 'libs'"
    assert "artifact" in params, "Missing parameter 'artifact'"
    assert "migr" in params, "Missing parameter 'migr'"

def test_emig::migrationprogram_has_delta():
    assert hasattr(emig::MigrationProgram, "delta")
    descriptor = None
    for klass in emig::MigrationProgram.__mro__:
        if "delta" in klass.__dict__:
            descriptor = klass.__dict__["delta"]
            break
    assert isinstance(descriptor, property)

def test_emig::migrationprogram_has_name():
    assert hasattr(emig::MigrationProgram, "name")
    descriptor = None
    for klass in emig::MigrationProgram.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_emig::migrationprogram_has_libs():
    assert hasattr(emig::MigrationProgram, "libs")
    descriptor = None
    for klass in emig::MigrationProgram.__mro__:
        if "libs" in klass.__dict__:
            descriptor = klass.__dict__["libs"]
            break
    assert isinstance(descriptor, property)

def test_emig::migrationprogram_has_artifact():
    assert hasattr(emig::MigrationProgram, "artifact")
    descriptor = None
    for klass in emig::MigrationProgram.__mro__:
        if "artifact" in klass.__dict__:
            descriptor = klass.__dict__["artifact"]
            break
    assert isinstance(descriptor, property)

def test_emig::migrationprogram_has_migr():
    assert hasattr(emig::MigrationProgram, "migr")
    descriptor = None
    for klass in emig::MigrationProgram.__mro__:
        if "migr" in klass.__dict__:
            descriptor = klass.__dict__["migr"]
            break
    assert isinstance(descriptor, property)



def test_emig::migrationlibrary_is_not_abstract():
    assert not inspect.isabstract(emig::MigrationLibrary)


def test_emig::migrationlibrary_constructor_exists():
    assert callable(emig::MigrationLibrary.__init__)


def test_emig::migrationlibrary_constructor_args():
    sig = inspect.signature(emig::MigrationLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emig::migrationlibrary_has_name():
    assert hasattr(emig::MigrationLibrary, "name")
    descriptor = None
    for klass in emig::MigrationLibrary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emig::mymodel_is_not_abstract():
    assert not inspect.isabstract(emig::MyModel)


def test_emig::mymodel_constructor_exists():
    assert callable(emig::MyModel.__init__)


def test_emig::mymodel_constructor_args():
    sig = inspect.signature(emig::MyModel.__init__)
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
emig::Reference_strategy = st.builds(
    emig::Reference,
)
EAttribute_strategy = st.builds(
    EAttribute,
)
emig::Attribute_strategy = st.builds(
    emig::Attribute,
)
EClass_strategy = st.builds(
    EClass,
)
emig::Class_strategy = st.builds(
    emig::Class,
)
EPackage_strategy = st.builds(
    EPackage,
)
emig::Package_strategy = st.builds(
    emig::Package,
)
emig::EObject_strategy = st.builds(
    emig::EObject,
)
Migrator_strategy = st.builds(
    Migrator,
)
emig::MigratorDX_strategy = st.builds(
    emig::MigratorDX,
)
emig::MigratorSX_strategy = st.builds(
    emig::MigratorSX,
)
emig::EStructuralFeature_strategy = st.builds(
    emig::EStructuralFeature,
)
emig::EReference_strategy = st.builds(
    emig::EReference,
)
emig::EAttribute_strategy = st.builds(
    emig::EAttribute,
)
emig::EClass_strategy = st.builds(
    emig::EClass,
)
OpDef_strategy = st.builds(
    OpDef,
)
emig::EReferenceOpDef_strategy = st.builds(
    emig::EReferenceOpDef,
)
emig::EClassOpDef_strategy = st.builds(
    emig::EClassOpDef,
)
emig::EAttributeOpDef_strategy = st.builds(
    emig::EAttributeOpDef,
)
emig::EPackageOpDef_strategy = st.builds(
    emig::EPackageOpDef,
)
emig::EPackage_strategy = st.builds(
    emig::EPackage,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
emig::setterDef_strategy = st.builds(
    emig::setterDef,
    operator=
        safe_text
)
emig::Artifact_strategy = st.builds(
    emig::Artifact,
    type=
        safe_text
)
emig::RewritingRule_strategy = st.builds(
    emig::RewritingRule,
)
emig::Migrator_strategy = st.builds(
    emig::Migrator,
    name=
        safe_text
)
emig::DotNavigationObjSX_strategy = st.builds(
    emig::DotNavigationObjSX,
)
emig::Parameter_strategy = st.builds(
    emig::Parameter,
    name=
        safe_text
)
emig::OpDef_strategy = st.builds(
    emig::OpDef,
    op=
        safe_text
)
emig::FilterMigrator_strategy = st.builds(
    emig::FilterMigrator,
    op=
        safe_text
)
emig::DotNavigationObjDX_strategy = st.builds(
    emig::DotNavigationObjDX,
)
emig::LocatedElement_strategy = st.builds(
    emig::LocatedElement,
    line=
        st.integers(),
    endoffset=
        st.integers(),
    endline=
        st.integers(),
    offset=
        st.integers()
)
emig::Rule_strategy = st.builds(
    emig::Rule,
    name=
        safe_text
)
emig::MigrationProgram_strategy = st.builds(
    emig::MigrationProgram,
    delta=
        safe_text,
    name=
        safe_text,
    libs=
        safe_text,
    artifact=
        safe_text,
    migr=
        safe_text
)
emig::MigrationLibrary_strategy = st.builds(
    emig::MigrationLibrary,
    name=
        safe_text
)
emig::MyModel_strategy = st.builds(
    emig::MyModel,
)

@given(instance=EReference_strategy)
@settings(max_examples=50)
def test_ereference_instantiation(instance):
    assert isinstance(instance, EReference)

@given(instance=emig::Reference_strategy)
@settings(max_examples=50)
def test_emig::reference_instantiation(instance):
    assert isinstance(instance, emig::Reference)

@given(instance=EAttribute_strategy)
@settings(max_examples=50)
def test_eattribute_instantiation(instance):
    assert isinstance(instance, EAttribute)

@given(instance=emig::Attribute_strategy)
@settings(max_examples=50)
def test_emig::attribute_instantiation(instance):
    assert isinstance(instance, emig::Attribute)

@given(instance=EClass_strategy)
@settings(max_examples=50)
def test_eclass_instantiation(instance):
    assert isinstance(instance, EClass)

@given(instance=emig::Class_strategy)
@settings(max_examples=50)
def test_emig::class_instantiation(instance):
    assert isinstance(instance, emig::Class)

@given(instance=EPackage_strategy)
@settings(max_examples=50)
def test_epackage_instantiation(instance):
    assert isinstance(instance, EPackage)

@given(instance=emig::Package_strategy)
@settings(max_examples=50)
def test_emig::package_instantiation(instance):
    assert isinstance(instance, emig::Package)

@given(instance=emig::EObject_strategy)
@settings(max_examples=50)
def test_emig::eobject_instantiation(instance):
    assert isinstance(instance, emig::EObject)

@given(instance=Migrator_strategy)
@settings(max_examples=50)
def test_migrator_instantiation(instance):
    assert isinstance(instance, Migrator)

@given(instance=emig::MigratorDX_strategy)
@settings(max_examples=50)
def test_emig::migratordx_instantiation(instance):
    assert isinstance(instance, emig::MigratorDX)

@given(instance=emig::MigratorSX_strategy)
@settings(max_examples=50)
def test_emig::migratorsx_instantiation(instance):
    assert isinstance(instance, emig::MigratorSX)

@given(instance=emig::EStructuralFeature_strategy)
@settings(max_examples=50)
def test_emig::estructuralfeature_instantiation(instance):
    assert isinstance(instance, emig::EStructuralFeature)

@given(instance=emig::EReference_strategy)
@settings(max_examples=50)
def test_emig::ereference_instantiation(instance):
    assert isinstance(instance, emig::EReference)

@given(instance=emig::EAttribute_strategy)
@settings(max_examples=50)
def test_emig::eattribute_instantiation(instance):
    assert isinstance(instance, emig::EAttribute)

@given(instance=emig::EClass_strategy)
@settings(max_examples=50)
def test_emig::eclass_instantiation(instance):
    assert isinstance(instance, emig::EClass)

@given(instance=OpDef_strategy)
@settings(max_examples=50)
def test_opdef_instantiation(instance):
    assert isinstance(instance, OpDef)

@given(instance=emig::EReferenceOpDef_strategy)
@settings(max_examples=50)
def test_emig::ereferenceopdef_instantiation(instance):
    assert isinstance(instance, emig::EReferenceOpDef)

@given(instance=emig::EClassOpDef_strategy)
@settings(max_examples=50)
def test_emig::eclassopdef_instantiation(instance):
    assert isinstance(instance, emig::EClassOpDef)

@given(instance=emig::EAttributeOpDef_strategy)
@settings(max_examples=50)
def test_emig::eattributeopdef_instantiation(instance):
    assert isinstance(instance, emig::EAttributeOpDef)

@given(instance=emig::EPackageOpDef_strategy)
@settings(max_examples=50)
def test_emig::epackageopdef_instantiation(instance):
    assert isinstance(instance, emig::EPackageOpDef)

@given(instance=emig::EPackage_strategy)
@settings(max_examples=50)
def test_emig::epackage_instantiation(instance):
    assert isinstance(instance, emig::EPackage)

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=emig::setterDef_strategy)
@settings(max_examples=50)
def test_emig::setterdef_instantiation(instance):
    assert isinstance(instance, emig::setterDef)

@given(instance=emig::setterDef_strategy)
def test_emig::setterdef_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=emig::setterDef_strategy)
def test_emig::setterdef_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=emig::Artifact_strategy)
@settings(max_examples=50)
def test_emig::artifact_instantiation(instance):
    assert isinstance(instance, emig::Artifact)

@given(instance=emig::Artifact_strategy)
def test_emig::artifact_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=emig::Artifact_strategy)
def test_emig::artifact_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=emig::RewritingRule_strategy)
@settings(max_examples=50)
def test_emig::rewritingrule_instantiation(instance):
    assert isinstance(instance, emig::RewritingRule)

@given(instance=emig::Migrator_strategy)
@settings(max_examples=50)
def test_emig::migrator_instantiation(instance):
    assert isinstance(instance, emig::Migrator)

@given(instance=emig::Migrator_strategy)
def test_emig::migrator_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=emig::Migrator_strategy)
def test_emig::migrator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=emig::DotNavigationObjSX_strategy)
@settings(max_examples=50)
def test_emig::dotnavigationobjsx_instantiation(instance):
    assert isinstance(instance, emig::DotNavigationObjSX)

@given(instance=emig::Parameter_strategy)
@settings(max_examples=50)
def test_emig::parameter_instantiation(instance):
    assert isinstance(instance, emig::Parameter)

@given(instance=emig::Parameter_strategy)
def test_emig::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=emig::Parameter_strategy)
def test_emig::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=emig::OpDef_strategy)
@settings(max_examples=50)
def test_emig::opdef_instantiation(instance):
    assert isinstance(instance, emig::OpDef)

@given(instance=emig::OpDef_strategy)
def test_emig::opdef_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=emig::OpDef_strategy)
def test_emig::opdef_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=emig::FilterMigrator_strategy)
@settings(max_examples=50)
def test_emig::filtermigrator_instantiation(instance):
    assert isinstance(instance, emig::FilterMigrator)

@given(instance=emig::FilterMigrator_strategy)
def test_emig::filtermigrator_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=emig::FilterMigrator_strategy)
def test_emig::filtermigrator_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=emig::DotNavigationObjDX_strategy)
@settings(max_examples=50)
def test_emig::dotnavigationobjdx_instantiation(instance):
    assert isinstance(instance, emig::DotNavigationObjDX)

@given(instance=emig::LocatedElement_strategy)
@settings(max_examples=50)
def test_emig::locatedelement_instantiation(instance):
    assert isinstance(instance, emig::LocatedElement)

@given(instance=emig::LocatedElement_strategy)
def test_emig::locatedelement_line_type(instance):
    assert isinstance(instance.line, int)


@given(instance=emig::LocatedElement_strategy)
def test_emig::locatedelement_line_setter(instance):
    original = instance.line
    instance.line = original
    assert instance.line == original

@given(instance=emig::LocatedElement_strategy)
def test_emig::locatedelement_endoffset_type(instance):
    assert isinstance(instance.endoffset, int)


@given(instance=emig::LocatedElement_strategy)
def test_emig::locatedelement_endoffset_setter(instance):
    original = instance.endoffset
    instance.endoffset = original
    assert instance.endoffset == original

@given(instance=emig::LocatedElement_strategy)
def test_emig::locatedelement_endline_type(instance):
    assert isinstance(instance.endline, int)


@given(instance=emig::LocatedElement_strategy)
def test_emig::locatedelement_endline_setter(instance):
    original = instance.endline
    instance.endline = original
    assert instance.endline == original

@given(instance=emig::LocatedElement_strategy)
def test_emig::locatedelement_offset_type(instance):
    assert isinstance(instance.offset, int)


@given(instance=emig::LocatedElement_strategy)
def test_emig::locatedelement_offset_setter(instance):
    original = instance.offset
    instance.offset = original
    assert instance.offset == original

@given(instance=emig::Rule_strategy)
@settings(max_examples=50)
def test_emig::rule_instantiation(instance):
    assert isinstance(instance, emig::Rule)

@given(instance=emig::Rule_strategy)
def test_emig::rule_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=emig::Rule_strategy)
def test_emig::rule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=emig::MigrationProgram_strategy)
@settings(max_examples=50)
def test_emig::migrationprogram_instantiation(instance):
    assert isinstance(instance, emig::MigrationProgram)

@given(instance=emig::MigrationProgram_strategy)
def test_emig::migrationprogram_delta_type(instance):
    assert isinstance(instance.delta, str)


@given(instance=emig::MigrationProgram_strategy)
def test_emig::migrationprogram_delta_setter(instance):
    original = instance.delta
    instance.delta = original
    assert instance.delta == original

@given(instance=emig::MigrationProgram_strategy)
def test_emig::migrationprogram_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=emig::MigrationProgram_strategy)
def test_emig::migrationprogram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=emig::MigrationProgram_strategy)
def test_emig::migrationprogram_libs_type(instance):
    assert isinstance(instance.libs, str)


@given(instance=emig::MigrationProgram_strategy)
def test_emig::migrationprogram_libs_setter(instance):
    original = instance.libs
    instance.libs = original
    assert instance.libs == original

@given(instance=emig::MigrationProgram_strategy)
def test_emig::migrationprogram_artifact_type(instance):
    assert isinstance(instance.artifact, str)


@given(instance=emig::MigrationProgram_strategy)
def test_emig::migrationprogram_artifact_setter(instance):
    original = instance.artifact
    instance.artifact = original
    assert instance.artifact == original

@given(instance=emig::MigrationProgram_strategy)
def test_emig::migrationprogram_migr_type(instance):
    assert isinstance(instance.migr, str)


@given(instance=emig::MigrationProgram_strategy)
def test_emig::migrationprogram_migr_setter(instance):
    original = instance.migr
    instance.migr = original
    assert instance.migr == original

@given(instance=emig::MigrationLibrary_strategy)
@settings(max_examples=50)
def test_emig::migrationlibrary_instantiation(instance):
    assert isinstance(instance, emig::MigrationLibrary)

@given(instance=emig::MigrationLibrary_strategy)
def test_emig::migrationlibrary_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=emig::MigrationLibrary_strategy)
def test_emig::migrationlibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=emig::MyModel_strategy)
@settings(max_examples=50)
def test_emig::mymodel_instantiation(instance):
    assert isinstance(instance, emig::MyModel)
