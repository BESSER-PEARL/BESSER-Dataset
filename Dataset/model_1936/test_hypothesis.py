import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    OclUndefinedExp,
    emig::OclUndefinedExp,
    MapExp,
    emig::MapExp,
    TupleExp,
    emig::TupleExp,
    SetExp,
    emig::SetExp,
    SequenceExp,
    emig::SequenceExp,
    OrderedSetExp,
    emig::OrderedSetExp,
    BagExp,
    emig::BagExp,
    SuperExp,
    emig::VariableDeclaration,
    Migrator,
    emig::Migrator,
    emig::MigratorDX,
    emig::MigratorSX,
    emig::Parameter,
    emig::SuperExp,
    VariableExp,
    emig::VariableExp,
    OclExpression,
    emig::NavigationOrAttributeCallExp,
    EReference,
    emig::Reference,
    EAttribute,
    emig::Attribute,
    EClass,
    emig::Class,
    EPackage,
    emig::Package,
    emig::DotNavigationObjDX,
    emig::EObject,
    emig::DotNavigationObjSX,
    emig::OclExpression,
    emig::FilterMigrator,
    emig::RewritingRule,
    emig::OpDef,
    emig::EPackage,
    emig::EStructuralFeature,
    emig::EReference,
    emig::EAttribute,
    emig::EClass,
    OpDef,
    emig::EClassOpDef,
    emig::EReferenceOpDef,
    emig::EAttributeOpDef,
    emig::EPackageOpDef,
    emig::setterDef,
    emig::Artifact,
    emig::Rule,
    emig::MigrationProgram,
    emig::MigrationLibrary,
    emig::MyModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_oclundefinedexp_is_not_abstract():
    assert not inspect.isabstract(OclUndefinedExp)


def test_oclundefinedexp_constructor_exists():
    assert callable(OclUndefinedExp.__init__)


def test_oclundefinedexp_constructor_args():
    sig = inspect.signature(OclUndefinedExp.__init__)
    params = list(sig.parameters.keys())



def test_emig::oclundefinedexp_is_not_abstract():
    assert not inspect.isabstract(emig::OclUndefinedExp)


def test_emig::oclundefinedexp_constructor_exists():
    assert callable(emig::OclUndefinedExp.__init__)


def test_emig::oclundefinedexp_constructor_args():
    sig = inspect.signature(emig::OclUndefinedExp.__init__)
    params = list(sig.parameters.keys())



def test_mapexp_is_not_abstract():
    assert not inspect.isabstract(MapExp)


def test_mapexp_constructor_exists():
    assert callable(MapExp.__init__)


def test_mapexp_constructor_args():
    sig = inspect.signature(MapExp.__init__)
    params = list(sig.parameters.keys())



def test_emig::mapexp_is_not_abstract():
    assert not inspect.isabstract(emig::MapExp)


def test_emig::mapexp_constructor_exists():
    assert callable(emig::MapExp.__init__)


def test_emig::mapexp_constructor_args():
    sig = inspect.signature(emig::MapExp.__init__)
    params = list(sig.parameters.keys())



def test_tupleexp_is_not_abstract():
    assert not inspect.isabstract(TupleExp)


def test_tupleexp_constructor_exists():
    assert callable(TupleExp.__init__)


def test_tupleexp_constructor_args():
    sig = inspect.signature(TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_emig::tupleexp_is_not_abstract():
    assert not inspect.isabstract(emig::TupleExp)


def test_emig::tupleexp_constructor_exists():
    assert callable(emig::TupleExp.__init__)


def test_emig::tupleexp_constructor_args():
    sig = inspect.signature(emig::TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_setexp_is_not_abstract():
    assert not inspect.isabstract(SetExp)


def test_setexp_constructor_exists():
    assert callable(SetExp.__init__)


def test_setexp_constructor_args():
    sig = inspect.signature(SetExp.__init__)
    params = list(sig.parameters.keys())



def test_emig::setexp_is_not_abstract():
    assert not inspect.isabstract(emig::SetExp)


def test_emig::setexp_constructor_exists():
    assert callable(emig::SetExp.__init__)


def test_emig::setexp_constructor_args():
    sig = inspect.signature(emig::SetExp.__init__)
    params = list(sig.parameters.keys())



def test_sequenceexp_is_not_abstract():
    assert not inspect.isabstract(SequenceExp)


def test_sequenceexp_constructor_exists():
    assert callable(SequenceExp.__init__)


def test_sequenceexp_constructor_args():
    sig = inspect.signature(SequenceExp.__init__)
    params = list(sig.parameters.keys())



def test_emig::sequenceexp_is_not_abstract():
    assert not inspect.isabstract(emig::SequenceExp)


def test_emig::sequenceexp_constructor_exists():
    assert callable(emig::SequenceExp.__init__)


def test_emig::sequenceexp_constructor_args():
    sig = inspect.signature(emig::SequenceExp.__init__)
    params = list(sig.parameters.keys())



def test_orderedsetexp_is_not_abstract():
    assert not inspect.isabstract(OrderedSetExp)


def test_orderedsetexp_constructor_exists():
    assert callable(OrderedSetExp.__init__)


def test_orderedsetexp_constructor_args():
    sig = inspect.signature(OrderedSetExp.__init__)
    params = list(sig.parameters.keys())



def test_emig::orderedsetexp_is_not_abstract():
    assert not inspect.isabstract(emig::OrderedSetExp)


def test_emig::orderedsetexp_constructor_exists():
    assert callable(emig::OrderedSetExp.__init__)


def test_emig::orderedsetexp_constructor_args():
    sig = inspect.signature(emig::OrderedSetExp.__init__)
    params = list(sig.parameters.keys())



def test_bagexp_is_not_abstract():
    assert not inspect.isabstract(BagExp)


def test_bagexp_constructor_exists():
    assert callable(BagExp.__init__)


def test_bagexp_constructor_args():
    sig = inspect.signature(BagExp.__init__)
    params = list(sig.parameters.keys())



def test_emig::bagexp_is_not_abstract():
    assert not inspect.isabstract(emig::BagExp)


def test_emig::bagexp_constructor_exists():
    assert callable(emig::BagExp.__init__)


def test_emig::bagexp_constructor_args():
    sig = inspect.signature(emig::BagExp.__init__)
    params = list(sig.parameters.keys())



def test_superexp_is_not_abstract():
    assert not inspect.isabstract(SuperExp)


def test_superexp_constructor_exists():
    assert callable(SuperExp.__init__)


def test_superexp_constructor_args():
    sig = inspect.signature(SuperExp.__init__)
    params = list(sig.parameters.keys())



def test_emig::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(emig::VariableDeclaration)


def test_emig::variabledeclaration_constructor_exists():
    assert callable(emig::VariableDeclaration.__init__)


def test_emig::variabledeclaration_constructor_args():
    sig = inspect.signature(emig::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_migrator_is_not_abstract():
    assert not inspect.isabstract(Migrator)


def test_migrator_constructor_exists():
    assert callable(Migrator.__init__)


def test_migrator_constructor_args():
    sig = inspect.signature(Migrator.__init__)
    params = list(sig.parameters.keys())



def test_emig::migrator_is_not_abstract():
    assert not inspect.isabstract(emig::Migrator)


def test_emig::migrator_constructor_exists():
    assert callable(emig::Migrator.__init__)


def test_emig::migrator_constructor_args():
    sig = inspect.signature(emig::Migrator.__init__)
    params = list(sig.parameters.keys())



def test_emig::migratordx_is_not_abstract():
    assert not inspect.isabstract(emig::MigratorDX)


def test_emig::migratordx_constructor_exists():
    assert callable(emig::MigratorDX.__init__)


def test_emig::migratordx_constructor_args():
    sig = inspect.signature(emig::MigratorDX.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emig::migratordx_has_name():
    assert hasattr(emig::MigratorDX, "name")
    descriptor = None
    for klass in emig::MigratorDX.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emig::migratorsx_is_not_abstract():
    assert not inspect.isabstract(emig::MigratorSX)


def test_emig::migratorsx_constructor_exists():
    assert callable(emig::MigratorSX.__init__)


def test_emig::migratorsx_constructor_args():
    sig = inspect.signature(emig::MigratorSX.__init__)
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



def test_emig::superexp_is_not_abstract():
    assert not inspect.isabstract(emig::SuperExp)


def test_emig::superexp_constructor_exists():
    assert callable(emig::SuperExp.__init__)


def test_emig::superexp_constructor_args():
    sig = inspect.signature(emig::SuperExp.__init__)
    params = list(sig.parameters.keys())



def test_variableexp_is_not_abstract():
    assert not inspect.isabstract(VariableExp)


def test_variableexp_constructor_exists():
    assert callable(VariableExp.__init__)


def test_variableexp_constructor_args():
    sig = inspect.signature(VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_emig::variableexp_is_not_abstract():
    assert not inspect.isabstract(emig::VariableExp)


def test_emig::variableexp_constructor_exists():
    assert callable(emig::VariableExp.__init__)


def test_emig::variableexp_constructor_args():
    sig = inspect.signature(emig::VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_emig::navigationorattributecallexp_is_not_abstract():
    assert not inspect.isabstract(emig::NavigationOrAttributeCallExp)


def test_emig::navigationorattributecallexp_constructor_exists():
    assert callable(emig::NavigationOrAttributeCallExp.__init__)


def test_emig::navigationorattributecallexp_constructor_args():
    sig = inspect.signature(emig::NavigationOrAttributeCallExp.__init__)
    params = list(sig.parameters.keys())



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



def test_emig::dotnavigationobjdx_is_not_abstract():
    assert not inspect.isabstract(emig::DotNavigationObjDX)


def test_emig::dotnavigationobjdx_constructor_exists():
    assert callable(emig::DotNavigationObjDX.__init__)


def test_emig::dotnavigationobjdx_constructor_args():
    sig = inspect.signature(emig::DotNavigationObjDX.__init__)
    params = list(sig.parameters.keys())



def test_emig::eobject_is_not_abstract():
    assert not inspect.isabstract(emig::EObject)


def test_emig::eobject_constructor_exists():
    assert callable(emig::EObject.__init__)


def test_emig::eobject_constructor_args():
    sig = inspect.signature(emig::EObject.__init__)
    params = list(sig.parameters.keys())



def test_emig::dotnavigationobjsx_is_not_abstract():
    assert not inspect.isabstract(emig::DotNavigationObjSX)


def test_emig::dotnavigationobjsx_constructor_exists():
    assert callable(emig::DotNavigationObjSX.__init__)


def test_emig::dotnavigationobjsx_constructor_args():
    sig = inspect.signature(emig::DotNavigationObjSX.__init__)
    params = list(sig.parameters.keys())



def test_emig::oclexpression_is_not_abstract():
    assert not inspect.isabstract(emig::OclExpression)


def test_emig::oclexpression_constructor_exists():
    assert callable(emig::OclExpression.__init__)


def test_emig::oclexpression_constructor_args():
    sig = inspect.signature(emig::OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_emig::filtermigrator_is_not_abstract():
    assert not inspect.isabstract(emig::FilterMigrator)


def test_emig::filtermigrator_constructor_exists():
    assert callable(emig::FilterMigrator.__init__)


def test_emig::filtermigrator_constructor_args():
    sig = inspect.signature(emig::FilterMigrator.__init__)
    params = list(sig.parameters.keys())



def test_emig::rewritingrule_is_not_abstract():
    assert not inspect.isabstract(emig::RewritingRule)


def test_emig::rewritingrule_constructor_exists():
    assert callable(emig::RewritingRule.__init__)


def test_emig::rewritingrule_constructor_args():
    sig = inspect.signature(emig::RewritingRule.__init__)
    params = list(sig.parameters.keys())



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



def test_emig::epackage_is_not_abstract():
    assert not inspect.isabstract(emig::EPackage)


def test_emig::epackage_constructor_exists():
    assert callable(emig::EPackage.__init__)


def test_emig::epackage_constructor_args():
    sig = inspect.signature(emig::EPackage.__init__)
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



def test_emig::eclassopdef_is_not_abstract():
    assert not inspect.isabstract(emig::EClassOpDef)


def test_emig::eclassopdef_constructor_exists():
    assert callable(emig::EClassOpDef.__init__)


def test_emig::eclassopdef_constructor_args():
    sig = inspect.signature(emig::EClassOpDef.__init__)
    params = list(sig.parameters.keys())



def test_emig::ereferenceopdef_is_not_abstract():
    assert not inspect.isabstract(emig::EReferenceOpDef)


def test_emig::ereferenceopdef_constructor_exists():
    assert callable(emig::EReferenceOpDef.__init__)


def test_emig::ereferenceopdef_constructor_args():
    sig = inspect.signature(emig::EReferenceOpDef.__init__)
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
    assert "libs" in params, "Missing parameter 'libs'"
    assert "migr" in params, "Missing parameter 'migr'"
    assert "name" in params, "Missing parameter 'name'"
    assert "delta" in params, "Missing parameter 'delta'"

def test_emig::migrationprogram_has_libs():
    assert hasattr(emig::MigrationProgram, "libs")
    descriptor = None
    for klass in emig::MigrationProgram.__mro__:
        if "libs" in klass.__dict__:
            descriptor = klass.__dict__["libs"]
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

def test_emig::migrationprogram_has_name():
    assert hasattr(emig::MigrationProgram, "name")
    descriptor = None
    for klass in emig::MigrationProgram.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_emig::migrationprogram_has_delta():
    assert hasattr(emig::MigrationProgram, "delta")
    descriptor = None
    for klass in emig::MigrationProgram.__mro__:
        if "delta" in klass.__dict__:
            descriptor = klass.__dict__["delta"]
            break
    assert isinstance(descriptor, property)



def test_emig::migrationlibrary_is_not_abstract():
    assert not inspect.isabstract(emig::MigrationLibrary)


def test_emig::migrationlibrary_constructor_exists():
    assert callable(emig::MigrationLibrary.__init__)


def test_emig::migrationlibrary_constructor_args():
    sig = inspect.signature(emig::MigrationLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_emig::migrationlibrary_has_title():
    assert hasattr(emig::MigrationLibrary, "title")
    descriptor = None
    for klass in emig::MigrationLibrary.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
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
OclUndefinedExp_strategy = st.builds(
    OclUndefinedExp,
)
emig::OclUndefinedExp_strategy = st.builds(
    emig::OclUndefinedExp,
)
MapExp_strategy = st.builds(
    MapExp,
)
emig::MapExp_strategy = st.builds(
    emig::MapExp,
)
TupleExp_strategy = st.builds(
    TupleExp,
)
emig::TupleExp_strategy = st.builds(
    emig::TupleExp,
)
SetExp_strategy = st.builds(
    SetExp,
)
emig::SetExp_strategy = st.builds(
    emig::SetExp,
)
SequenceExp_strategy = st.builds(
    SequenceExp,
)
emig::SequenceExp_strategy = st.builds(
    emig::SequenceExp,
)
OrderedSetExp_strategy = st.builds(
    OrderedSetExp,
)
emig::OrderedSetExp_strategy = st.builds(
    emig::OrderedSetExp,
)
BagExp_strategy = st.builds(
    BagExp,
)
emig::BagExp_strategy = st.builds(
    emig::BagExp,
)
SuperExp_strategy = st.builds(
    SuperExp,
)
emig::VariableDeclaration_strategy = st.builds(
    emig::VariableDeclaration,
)
Migrator_strategy = st.builds(
    Migrator,
)
emig::Migrator_strategy = st.builds(
    emig::Migrator,
)
emig::MigratorDX_strategy = st.builds(
    emig::MigratorDX,
    name=
        safe_text
)
emig::MigratorSX_strategy = st.builds(
    emig::MigratorSX,
)
emig::Parameter_strategy = st.builds(
    emig::Parameter,
    name=
        safe_text
)
emig::SuperExp_strategy = st.builds(
    emig::SuperExp,
)
VariableExp_strategy = st.builds(
    VariableExp,
)
emig::VariableExp_strategy = st.builds(
    emig::VariableExp,
)
OclExpression_strategy = st.builds(
    OclExpression,
)
emig::NavigationOrAttributeCallExp_strategy = st.builds(
    emig::NavigationOrAttributeCallExp,
)
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
emig::DotNavigationObjDX_strategy = st.builds(
    emig::DotNavigationObjDX,
)
emig::EObject_strategy = st.builds(
    emig::EObject,
)
emig::DotNavigationObjSX_strategy = st.builds(
    emig::DotNavigationObjSX,
)
emig::OclExpression_strategy = st.builds(
    emig::OclExpression,
)
emig::FilterMigrator_strategy = st.builds(
    emig::FilterMigrator,
)
emig::RewritingRule_strategy = st.builds(
    emig::RewritingRule,
)
emig::OpDef_strategy = st.builds(
    emig::OpDef,
    op=
        safe_text
)
emig::EPackage_strategy = st.builds(
    emig::EPackage,
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
emig::EClassOpDef_strategy = st.builds(
    emig::EClassOpDef,
)
emig::EReferenceOpDef_strategy = st.builds(
    emig::EReferenceOpDef,
)
emig::EAttributeOpDef_strategy = st.builds(
    emig::EAttributeOpDef,
)
emig::EPackageOpDef_strategy = st.builds(
    emig::EPackageOpDef,
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
emig::Rule_strategy = st.builds(
    emig::Rule,
    name=
        safe_text
)
emig::MigrationProgram_strategy = st.builds(
    emig::MigrationProgram,
    libs=
        safe_text,
    migr=
        safe_text,
    name=
        safe_text,
    delta=
        safe_text
)
emig::MigrationLibrary_strategy = st.builds(
    emig::MigrationLibrary,
    title=
        safe_text
)
emig::MyModel_strategy = st.builds(
    emig::MyModel,
)

@given(instance=OclUndefinedExp_strategy)
@settings(max_examples=50)
def test_oclundefinedexp_instantiation(instance):
    assert isinstance(instance, OclUndefinedExp)

@given(instance=emig::OclUndefinedExp_strategy)
@settings(max_examples=50)
def test_emig::oclundefinedexp_instantiation(instance):
    assert isinstance(instance, emig::OclUndefinedExp)

@given(instance=MapExp_strategy)
@settings(max_examples=50)
def test_mapexp_instantiation(instance):
    assert isinstance(instance, MapExp)

@given(instance=emig::MapExp_strategy)
@settings(max_examples=50)
def test_emig::mapexp_instantiation(instance):
    assert isinstance(instance, emig::MapExp)

@given(instance=TupleExp_strategy)
@settings(max_examples=50)
def test_tupleexp_instantiation(instance):
    assert isinstance(instance, TupleExp)

@given(instance=emig::TupleExp_strategy)
@settings(max_examples=50)
def test_emig::tupleexp_instantiation(instance):
    assert isinstance(instance, emig::TupleExp)

@given(instance=SetExp_strategy)
@settings(max_examples=50)
def test_setexp_instantiation(instance):
    assert isinstance(instance, SetExp)

@given(instance=emig::SetExp_strategy)
@settings(max_examples=50)
def test_emig::setexp_instantiation(instance):
    assert isinstance(instance, emig::SetExp)

@given(instance=SequenceExp_strategy)
@settings(max_examples=50)
def test_sequenceexp_instantiation(instance):
    assert isinstance(instance, SequenceExp)

@given(instance=emig::SequenceExp_strategy)
@settings(max_examples=50)
def test_emig::sequenceexp_instantiation(instance):
    assert isinstance(instance, emig::SequenceExp)

@given(instance=OrderedSetExp_strategy)
@settings(max_examples=50)
def test_orderedsetexp_instantiation(instance):
    assert isinstance(instance, OrderedSetExp)

@given(instance=emig::OrderedSetExp_strategy)
@settings(max_examples=50)
def test_emig::orderedsetexp_instantiation(instance):
    assert isinstance(instance, emig::OrderedSetExp)

@given(instance=BagExp_strategy)
@settings(max_examples=50)
def test_bagexp_instantiation(instance):
    assert isinstance(instance, BagExp)

@given(instance=emig::BagExp_strategy)
@settings(max_examples=50)
def test_emig::bagexp_instantiation(instance):
    assert isinstance(instance, emig::BagExp)

@given(instance=SuperExp_strategy)
@settings(max_examples=50)
def test_superexp_instantiation(instance):
    assert isinstance(instance, SuperExp)

@given(instance=emig::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_emig::variabledeclaration_instantiation(instance):
    assert isinstance(instance, emig::VariableDeclaration)

@given(instance=Migrator_strategy)
@settings(max_examples=50)
def test_migrator_instantiation(instance):
    assert isinstance(instance, Migrator)

@given(instance=emig::Migrator_strategy)
@settings(max_examples=50)
def test_emig::migrator_instantiation(instance):
    assert isinstance(instance, emig::Migrator)

@given(instance=emig::MigratorDX_strategy)
@settings(max_examples=50)
def test_emig::migratordx_instantiation(instance):
    assert isinstance(instance, emig::MigratorDX)

@given(instance=emig::MigratorDX_strategy)
def test_emig::migratordx_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=emig::MigratorDX_strategy)
def test_emig::migratordx_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=emig::MigratorSX_strategy)
@settings(max_examples=50)
def test_emig::migratorsx_instantiation(instance):
    assert isinstance(instance, emig::MigratorSX)

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

@given(instance=emig::SuperExp_strategy)
@settings(max_examples=50)
def test_emig::superexp_instantiation(instance):
    assert isinstance(instance, emig::SuperExp)

@given(instance=VariableExp_strategy)
@settings(max_examples=50)
def test_variableexp_instantiation(instance):
    assert isinstance(instance, VariableExp)

@given(instance=emig::VariableExp_strategy)
@settings(max_examples=50)
def test_emig::variableexp_instantiation(instance):
    assert isinstance(instance, emig::VariableExp)

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=emig::NavigationOrAttributeCallExp_strategy)
@settings(max_examples=50)
def test_emig::navigationorattributecallexp_instantiation(instance):
    assert isinstance(instance, emig::NavigationOrAttributeCallExp)

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

@given(instance=emig::DotNavigationObjDX_strategy)
@settings(max_examples=50)
def test_emig::dotnavigationobjdx_instantiation(instance):
    assert isinstance(instance, emig::DotNavigationObjDX)

@given(instance=emig::EObject_strategy)
@settings(max_examples=50)
def test_emig::eobject_instantiation(instance):
    assert isinstance(instance, emig::EObject)

@given(instance=emig::DotNavigationObjSX_strategy)
@settings(max_examples=50)
def test_emig::dotnavigationobjsx_instantiation(instance):
    assert isinstance(instance, emig::DotNavigationObjSX)

@given(instance=emig::OclExpression_strategy)
@settings(max_examples=50)
def test_emig::oclexpression_instantiation(instance):
    assert isinstance(instance, emig::OclExpression)

@given(instance=emig::FilterMigrator_strategy)
@settings(max_examples=50)
def test_emig::filtermigrator_instantiation(instance):
    assert isinstance(instance, emig::FilterMigrator)

@given(instance=emig::RewritingRule_strategy)
@settings(max_examples=50)
def test_emig::rewritingrule_instantiation(instance):
    assert isinstance(instance, emig::RewritingRule)

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

@given(instance=emig::EPackage_strategy)
@settings(max_examples=50)
def test_emig::epackage_instantiation(instance):
    assert isinstance(instance, emig::EPackage)

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

@given(instance=emig::EClassOpDef_strategy)
@settings(max_examples=50)
def test_emig::eclassopdef_instantiation(instance):
    assert isinstance(instance, emig::EClassOpDef)

@given(instance=emig::EReferenceOpDef_strategy)
@settings(max_examples=50)
def test_emig::ereferenceopdef_instantiation(instance):
    assert isinstance(instance, emig::EReferenceOpDef)

@given(instance=emig::EAttributeOpDef_strategy)
@settings(max_examples=50)
def test_emig::eattributeopdef_instantiation(instance):
    assert isinstance(instance, emig::EAttributeOpDef)

@given(instance=emig::EPackageOpDef_strategy)
@settings(max_examples=50)
def test_emig::epackageopdef_instantiation(instance):
    assert isinstance(instance, emig::EPackageOpDef)

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
def test_emig::migrationprogram_libs_type(instance):
    assert isinstance(instance.libs, str)


@given(instance=emig::MigrationProgram_strategy)
def test_emig::migrationprogram_libs_setter(instance):
    original = instance.libs
    instance.libs = original
    assert instance.libs == original

@given(instance=emig::MigrationProgram_strategy)
def test_emig::migrationprogram_migr_type(instance):
    assert isinstance(instance.migr, str)


@given(instance=emig::MigrationProgram_strategy)
def test_emig::migrationprogram_migr_setter(instance):
    original = instance.migr
    instance.migr = original
    assert instance.migr == original

@given(instance=emig::MigrationProgram_strategy)
def test_emig::migrationprogram_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=emig::MigrationProgram_strategy)
def test_emig::migrationprogram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=emig::MigrationProgram_strategy)
def test_emig::migrationprogram_delta_type(instance):
    assert isinstance(instance.delta, str)


@given(instance=emig::MigrationProgram_strategy)
def test_emig::migrationprogram_delta_setter(instance):
    original = instance.delta
    instance.delta = original
    assert instance.delta == original

@given(instance=emig::MigrationLibrary_strategy)
@settings(max_examples=50)
def test_emig::migrationlibrary_instantiation(instance):
    assert isinstance(instance, emig::MigrationLibrary)

@given(instance=emig::MigrationLibrary_strategy)
def test_emig::migrationlibrary_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=emig::MigrationLibrary_strategy)
def test_emig::migrationlibrary_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=emig::MyModel_strategy)
@settings(max_examples=50)
def test_emig::mymodel_instantiation(instance):
    assert isinstance(instance, emig::MyModel)
