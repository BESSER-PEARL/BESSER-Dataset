import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    OclUndefinedExp,
    emig_OclUndefinedExp,
    MapExp,
    emig_MapExp,
    TupleExp,
    emig_TupleExp,
    SetExp,
    emig_SetExp,
    SequenceExp,
    emig_SequenceExp,
    OrderedSetExp,
    emig_OrderedSetExp,
    BagExp,
    emig_BagExp,
    SuperExp,
    emig_VariableDeclaration,
    Migrator,
    emig_Migrator,
    emig_MigratorDX,
    emig_MigratorSX,
    emig_Parameter,
    emig_SuperExp,
    VariableExp,
    emig_VariableExp,
    OclExpression,
    emig_NavigationOrAttributeCallExp,
    EReference,
    emig_Reference,
    EAttribute,
    emig_Attribute,
    EClass,
    emig_Class,
    EPackage,
    emig_Package,
    emig_DotNavigationObjDX,
    emig_EObject,
    emig_DotNavigationObjSX,
    emig_OclExpression,
    emig_FilterMigrator,
    emig_RewritingRule,
    emig_OpDef,
    emig_EPackage,
    emig_EStructuralFeature,
    emig_EReference,
    emig_EAttribute,
    emig_EClass,
    OpDef,
    emig_EAttributeOpDef,
    emig_EClassOpDef,
    emig_EReferenceOpDef,
    emig_EPackageOpDef,
    emig_setterDef,
    emig_Artifact,
    emig_Rule,
    emig_MigrationProgram,
    emig_MigrationLibrary,
    emig_MyModel,
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



def test_emig_oclundefinedexp_is_not_abstract():
    assert not inspect.isabstract(emig_OclUndefinedExp)


def test_emig_oclundefinedexp_constructor_exists():
    assert callable(emig_OclUndefinedExp.__init__)


def test_emig_oclundefinedexp_constructor_args():
    sig = inspect.signature(emig_OclUndefinedExp.__init__)
    params = list(sig.parameters.keys())



def test_mapexp_is_not_abstract():
    assert not inspect.isabstract(MapExp)


def test_mapexp_constructor_exists():
    assert callable(MapExp.__init__)


def test_mapexp_constructor_args():
    sig = inspect.signature(MapExp.__init__)
    params = list(sig.parameters.keys())



def test_emig_mapexp_is_not_abstract():
    assert not inspect.isabstract(emig_MapExp)


def test_emig_mapexp_constructor_exists():
    assert callable(emig_MapExp.__init__)


def test_emig_mapexp_constructor_args():
    sig = inspect.signature(emig_MapExp.__init__)
    params = list(sig.parameters.keys())



def test_tupleexp_is_not_abstract():
    assert not inspect.isabstract(TupleExp)


def test_tupleexp_constructor_exists():
    assert callable(TupleExp.__init__)


def test_tupleexp_constructor_args():
    sig = inspect.signature(TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_emig_tupleexp_is_not_abstract():
    assert not inspect.isabstract(emig_TupleExp)


def test_emig_tupleexp_constructor_exists():
    assert callable(emig_TupleExp.__init__)


def test_emig_tupleexp_constructor_args():
    sig = inspect.signature(emig_TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_setexp_is_not_abstract():
    assert not inspect.isabstract(SetExp)


def test_setexp_constructor_exists():
    assert callable(SetExp.__init__)


def test_setexp_constructor_args():
    sig = inspect.signature(SetExp.__init__)
    params = list(sig.parameters.keys())



def test_emig_setexp_is_not_abstract():
    assert not inspect.isabstract(emig_SetExp)


def test_emig_setexp_constructor_exists():
    assert callable(emig_SetExp.__init__)


def test_emig_setexp_constructor_args():
    sig = inspect.signature(emig_SetExp.__init__)
    params = list(sig.parameters.keys())



def test_sequenceexp_is_not_abstract():
    assert not inspect.isabstract(SequenceExp)


def test_sequenceexp_constructor_exists():
    assert callable(SequenceExp.__init__)


def test_sequenceexp_constructor_args():
    sig = inspect.signature(SequenceExp.__init__)
    params = list(sig.parameters.keys())



def test_emig_sequenceexp_is_not_abstract():
    assert not inspect.isabstract(emig_SequenceExp)


def test_emig_sequenceexp_constructor_exists():
    assert callable(emig_SequenceExp.__init__)


def test_emig_sequenceexp_constructor_args():
    sig = inspect.signature(emig_SequenceExp.__init__)
    params = list(sig.parameters.keys())



def test_orderedsetexp_is_not_abstract():
    assert not inspect.isabstract(OrderedSetExp)


def test_orderedsetexp_constructor_exists():
    assert callable(OrderedSetExp.__init__)


def test_orderedsetexp_constructor_args():
    sig = inspect.signature(OrderedSetExp.__init__)
    params = list(sig.parameters.keys())



def test_emig_orderedsetexp_is_not_abstract():
    assert not inspect.isabstract(emig_OrderedSetExp)


def test_emig_orderedsetexp_constructor_exists():
    assert callable(emig_OrderedSetExp.__init__)


def test_emig_orderedsetexp_constructor_args():
    sig = inspect.signature(emig_OrderedSetExp.__init__)
    params = list(sig.parameters.keys())



def test_bagexp_is_not_abstract():
    assert not inspect.isabstract(BagExp)


def test_bagexp_constructor_exists():
    assert callable(BagExp.__init__)


def test_bagexp_constructor_args():
    sig = inspect.signature(BagExp.__init__)
    params = list(sig.parameters.keys())



def test_emig_bagexp_is_not_abstract():
    assert not inspect.isabstract(emig_BagExp)


def test_emig_bagexp_constructor_exists():
    assert callable(emig_BagExp.__init__)


def test_emig_bagexp_constructor_args():
    sig = inspect.signature(emig_BagExp.__init__)
    params = list(sig.parameters.keys())



def test_superexp_is_not_abstract():
    assert not inspect.isabstract(SuperExp)


def test_superexp_constructor_exists():
    assert callable(SuperExp.__init__)


def test_superexp_constructor_args():
    sig = inspect.signature(SuperExp.__init__)
    params = list(sig.parameters.keys())



def test_emig_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(emig_VariableDeclaration)


def test_emig_variabledeclaration_constructor_exists():
    assert callable(emig_VariableDeclaration.__init__)


def test_emig_variabledeclaration_constructor_args():
    sig = inspect.signature(emig_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_migrator_is_not_abstract():
    assert not inspect.isabstract(Migrator)


def test_migrator_constructor_exists():
    assert callable(Migrator.__init__)


def test_migrator_constructor_args():
    sig = inspect.signature(Migrator.__init__)
    params = list(sig.parameters.keys())



def test_emig_migrator_is_not_abstract():
    assert not inspect.isabstract(emig_Migrator)


def test_emig_migrator_constructor_exists():
    assert callable(emig_Migrator.__init__)


def test_emig_migrator_constructor_args():
    sig = inspect.signature(emig_Migrator.__init__)
    params = list(sig.parameters.keys())



def test_emig_migratordx_is_not_abstract():
    assert not inspect.isabstract(emig_MigratorDX)


def test_emig_migratordx_constructor_exists():
    assert callable(emig_MigratorDX.__init__)


def test_emig_migratordx_constructor_args():
    sig = inspect.signature(emig_MigratorDX.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emig_migratordx_has_name():
    assert hasattr(emig_MigratorDX, "name")
    descriptor = None
    for klass in emig_MigratorDX.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emig_migratorsx_is_not_abstract():
    assert not inspect.isabstract(emig_MigratorSX)


def test_emig_migratorsx_constructor_exists():
    assert callable(emig_MigratorSX.__init__)


def test_emig_migratorsx_constructor_args():
    sig = inspect.signature(emig_MigratorSX.__init__)
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



def test_emig_superexp_is_not_abstract():
    assert not inspect.isabstract(emig_SuperExp)


def test_emig_superexp_constructor_exists():
    assert callable(emig_SuperExp.__init__)


def test_emig_superexp_constructor_args():
    sig = inspect.signature(emig_SuperExp.__init__)
    params = list(sig.parameters.keys())



def test_variableexp_is_not_abstract():
    assert not inspect.isabstract(VariableExp)


def test_variableexp_constructor_exists():
    assert callable(VariableExp.__init__)


def test_variableexp_constructor_args():
    sig = inspect.signature(VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_emig_variableexp_is_not_abstract():
    assert not inspect.isabstract(emig_VariableExp)


def test_emig_variableexp_constructor_exists():
    assert callable(emig_VariableExp.__init__)


def test_emig_variableexp_constructor_args():
    sig = inspect.signature(emig_VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_emig_navigationorattributecallexp_is_not_abstract():
    assert not inspect.isabstract(emig_NavigationOrAttributeCallExp)


def test_emig_navigationorattributecallexp_constructor_exists():
    assert callable(emig_NavigationOrAttributeCallExp.__init__)


def test_emig_navigationorattributecallexp_constructor_args():
    sig = inspect.signature(emig_NavigationOrAttributeCallExp.__init__)
    params = list(sig.parameters.keys())



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



def test_emig_dotnavigationobjdx_is_not_abstract():
    assert not inspect.isabstract(emig_DotNavigationObjDX)


def test_emig_dotnavigationobjdx_constructor_exists():
    assert callable(emig_DotNavigationObjDX.__init__)


def test_emig_dotnavigationobjdx_constructor_args():
    sig = inspect.signature(emig_DotNavigationObjDX.__init__)
    params = list(sig.parameters.keys())



def test_emig_eobject_is_not_abstract():
    assert not inspect.isabstract(emig_EObject)


def test_emig_eobject_constructor_exists():
    assert callable(emig_EObject.__init__)


def test_emig_eobject_constructor_args():
    sig = inspect.signature(emig_EObject.__init__)
    params = list(sig.parameters.keys())



def test_emig_dotnavigationobjsx_is_not_abstract():
    assert not inspect.isabstract(emig_DotNavigationObjSX)


def test_emig_dotnavigationobjsx_constructor_exists():
    assert callable(emig_DotNavigationObjSX.__init__)


def test_emig_dotnavigationobjsx_constructor_args():
    sig = inspect.signature(emig_DotNavigationObjSX.__init__)
    params = list(sig.parameters.keys())



def test_emig_oclexpression_is_not_abstract():
    assert not inspect.isabstract(emig_OclExpression)


def test_emig_oclexpression_constructor_exists():
    assert callable(emig_OclExpression.__init__)


def test_emig_oclexpression_constructor_args():
    sig = inspect.signature(emig_OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_emig_filtermigrator_is_not_abstract():
    assert not inspect.isabstract(emig_FilterMigrator)


def test_emig_filtermigrator_constructor_exists():
    assert callable(emig_FilterMigrator.__init__)


def test_emig_filtermigrator_constructor_args():
    sig = inspect.signature(emig_FilterMigrator.__init__)
    params = list(sig.parameters.keys())



def test_emig_rewritingrule_is_not_abstract():
    assert not inspect.isabstract(emig_RewritingRule)


def test_emig_rewritingrule_constructor_exists():
    assert callable(emig_RewritingRule.__init__)


def test_emig_rewritingrule_constructor_args():
    sig = inspect.signature(emig_RewritingRule.__init__)
    params = list(sig.parameters.keys())



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



def test_emig_epackage_is_not_abstract():
    assert not inspect.isabstract(emig_EPackage)


def test_emig_epackage_constructor_exists():
    assert callable(emig_EPackage.__init__)


def test_emig_epackage_constructor_args():
    sig = inspect.signature(emig_EPackage.__init__)
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
    assert "delta" in params, "Missing parameter 'delta'"
    assert "name" in params, "Missing parameter 'name'"

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

def test_emig_migrationprogram_has_delta():
    assert hasattr(emig_MigrationProgram, "delta")
    descriptor = None
    for klass in emig_MigrationProgram.__mro__:
        if "delta" in klass.__dict__:
            descriptor = klass.__dict__["delta"]
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



def test_emig_migrationlibrary_is_not_abstract():
    assert not inspect.isabstract(emig_MigrationLibrary)


def test_emig_migrationlibrary_constructor_exists():
    assert callable(emig_MigrationLibrary.__init__)


def test_emig_migrationlibrary_constructor_args():
    sig = inspect.signature(emig_MigrationLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_emig_migrationlibrary_has_title():
    assert hasattr(emig_MigrationLibrary, "title")
    descriptor = None
    for klass in emig_MigrationLibrary.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
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
OclUndefinedExp_strategy = st.builds(
    OclUndefinedExp,
)
emig_OclUndefinedExp_strategy = st.builds(
    emig_OclUndefinedExp,
)
MapExp_strategy = st.builds(
    MapExp,
)
emig_MapExp_strategy = st.builds(
    emig_MapExp,
)
TupleExp_strategy = st.builds(
    TupleExp,
)
emig_TupleExp_strategy = st.builds(
    emig_TupleExp,
)
SetExp_strategy = st.builds(
    SetExp,
)
emig_SetExp_strategy = st.builds(
    emig_SetExp,
)
SequenceExp_strategy = st.builds(
    SequenceExp,
)
emig_SequenceExp_strategy = st.builds(
    emig_SequenceExp,
)
OrderedSetExp_strategy = st.builds(
    OrderedSetExp,
)
emig_OrderedSetExp_strategy = st.builds(
    emig_OrderedSetExp,
)
BagExp_strategy = st.builds(
    BagExp,
)
emig_BagExp_strategy = st.builds(
    emig_BagExp,
)
SuperExp_strategy = st.builds(
    SuperExp,
)
emig_VariableDeclaration_strategy = st.builds(
    emig_VariableDeclaration,
)
Migrator_strategy = st.builds(
    Migrator,
)
emig_Migrator_strategy = st.builds(
    emig_Migrator,
)
emig_MigratorDX_strategy = st.builds(
    emig_MigratorDX,
    name=
        safe_text
)
emig_MigratorSX_strategy = st.builds(
    emig_MigratorSX,
)
emig_Parameter_strategy = st.builds(
    emig_Parameter,
    name=
        safe_text
)
emig_SuperExp_strategy = st.builds(
    emig_SuperExp,
)
VariableExp_strategy = st.builds(
    VariableExp,
)
emig_VariableExp_strategy = st.builds(
    emig_VariableExp,
)
OclExpression_strategy = st.builds(
    OclExpression,
)
emig_NavigationOrAttributeCallExp_strategy = st.builds(
    emig_NavigationOrAttributeCallExp,
)
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
emig_DotNavigationObjDX_strategy = st.builds(
    emig_DotNavigationObjDX,
)
emig_EObject_strategy = st.builds(
    emig_EObject,
)
emig_DotNavigationObjSX_strategy = st.builds(
    emig_DotNavigationObjSX,
)
emig_OclExpression_strategy = st.builds(
    emig_OclExpression,
)
emig_FilterMigrator_strategy = st.builds(
    emig_FilterMigrator,
)
emig_RewritingRule_strategy = st.builds(
    emig_RewritingRule,
)
emig_OpDef_strategy = st.builds(
    emig_OpDef,
    op=
        safe_text
)
emig_EPackage_strategy = st.builds(
    emig_EPackage,
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
    delta=
        safe_text,
    name=
        safe_text
)
emig_MigrationLibrary_strategy = st.builds(
    emig_MigrationLibrary,
    title=
        safe_text
)
emig_MyModel_strategy = st.builds(
    emig_MyModel,
)

@given(instance=OclUndefinedExp_strategy)
@settings(max_examples=50)
def test_oclundefinedexp_instantiation(instance):
    assert isinstance(instance, OclUndefinedExp)

@given(instance=emig_OclUndefinedExp_strategy)
@settings(max_examples=50)
def test_emig_oclundefinedexp_instantiation(instance):
    assert isinstance(instance, emig_OclUndefinedExp)

@given(instance=MapExp_strategy)
@settings(max_examples=50)
def test_mapexp_instantiation(instance):
    assert isinstance(instance, MapExp)

@given(instance=emig_MapExp_strategy)
@settings(max_examples=50)
def test_emig_mapexp_instantiation(instance):
    assert isinstance(instance, emig_MapExp)

@given(instance=TupleExp_strategy)
@settings(max_examples=50)
def test_tupleexp_instantiation(instance):
    assert isinstance(instance, TupleExp)

@given(instance=emig_TupleExp_strategy)
@settings(max_examples=50)
def test_emig_tupleexp_instantiation(instance):
    assert isinstance(instance, emig_TupleExp)

@given(instance=SetExp_strategy)
@settings(max_examples=50)
def test_setexp_instantiation(instance):
    assert isinstance(instance, SetExp)

@given(instance=emig_SetExp_strategy)
@settings(max_examples=50)
def test_emig_setexp_instantiation(instance):
    assert isinstance(instance, emig_SetExp)

@given(instance=SequenceExp_strategy)
@settings(max_examples=50)
def test_sequenceexp_instantiation(instance):
    assert isinstance(instance, SequenceExp)

@given(instance=emig_SequenceExp_strategy)
@settings(max_examples=50)
def test_emig_sequenceexp_instantiation(instance):
    assert isinstance(instance, emig_SequenceExp)

@given(instance=OrderedSetExp_strategy)
@settings(max_examples=50)
def test_orderedsetexp_instantiation(instance):
    assert isinstance(instance, OrderedSetExp)

@given(instance=emig_OrderedSetExp_strategy)
@settings(max_examples=50)
def test_emig_orderedsetexp_instantiation(instance):
    assert isinstance(instance, emig_OrderedSetExp)

@given(instance=BagExp_strategy)
@settings(max_examples=50)
def test_bagexp_instantiation(instance):
    assert isinstance(instance, BagExp)

@given(instance=emig_BagExp_strategy)
@settings(max_examples=50)
def test_emig_bagexp_instantiation(instance):
    assert isinstance(instance, emig_BagExp)

@given(instance=SuperExp_strategy)
@settings(max_examples=50)
def test_superexp_instantiation(instance):
    assert isinstance(instance, SuperExp)

@given(instance=emig_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_emig_variabledeclaration_instantiation(instance):
    assert isinstance(instance, emig_VariableDeclaration)

@given(instance=Migrator_strategy)
@settings(max_examples=50)
def test_migrator_instantiation(instance):
    assert isinstance(instance, Migrator)

@given(instance=emig_Migrator_strategy)
@settings(max_examples=50)
def test_emig_migrator_instantiation(instance):
    assert isinstance(instance, emig_Migrator)

@given(instance=emig_MigratorDX_strategy)
@settings(max_examples=50)
def test_emig_migratordx_instantiation(instance):
    assert isinstance(instance, emig_MigratorDX)



@given(instance=emig_MigratorDX_strategy)
def test_emig_migratordx_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=emig_MigratorSX_strategy)
@settings(max_examples=50)
def test_emig_migratorsx_instantiation(instance):
    assert isinstance(instance, emig_MigratorSX)

@given(instance=emig_Parameter_strategy)
@settings(max_examples=50)
def test_emig_parameter_instantiation(instance):
    assert isinstance(instance, emig_Parameter)



@given(instance=emig_Parameter_strategy)
def test_emig_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=emig_SuperExp_strategy)
@settings(max_examples=50)
def test_emig_superexp_instantiation(instance):
    assert isinstance(instance, emig_SuperExp)

@given(instance=VariableExp_strategy)
@settings(max_examples=50)
def test_variableexp_instantiation(instance):
    assert isinstance(instance, VariableExp)

@given(instance=emig_VariableExp_strategy)
@settings(max_examples=50)
def test_emig_variableexp_instantiation(instance):
    assert isinstance(instance, emig_VariableExp)

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=emig_NavigationOrAttributeCallExp_strategy)
@settings(max_examples=50)
def test_emig_navigationorattributecallexp_instantiation(instance):
    assert isinstance(instance, emig_NavigationOrAttributeCallExp)

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

@given(instance=emig_DotNavigationObjDX_strategy)
@settings(max_examples=50)
def test_emig_dotnavigationobjdx_instantiation(instance):
    assert isinstance(instance, emig_DotNavigationObjDX)

@given(instance=emig_EObject_strategy)
@settings(max_examples=50)
def test_emig_eobject_instantiation(instance):
    assert isinstance(instance, emig_EObject)

@given(instance=emig_DotNavigationObjSX_strategy)
@settings(max_examples=50)
def test_emig_dotnavigationobjsx_instantiation(instance):
    assert isinstance(instance, emig_DotNavigationObjSX)

@given(instance=emig_OclExpression_strategy)
@settings(max_examples=50)
def test_emig_oclexpression_instantiation(instance):
    assert isinstance(instance, emig_OclExpression)

@given(instance=emig_FilterMigrator_strategy)
@settings(max_examples=50)
def test_emig_filtermigrator_instantiation(instance):
    assert isinstance(instance, emig_FilterMigrator)

@given(instance=emig_RewritingRule_strategy)
@settings(max_examples=50)
def test_emig_rewritingrule_instantiation(instance):
    assert isinstance(instance, emig_RewritingRule)

@given(instance=emig_OpDef_strategy)
@settings(max_examples=50)
def test_emig_opdef_instantiation(instance):
    assert isinstance(instance, emig_OpDef)



@given(instance=emig_OpDef_strategy)
def test_emig_opdef_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=emig_EPackage_strategy)
@settings(max_examples=50)
def test_emig_epackage_instantiation(instance):
    assert isinstance(instance, emig_EPackage)

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
def test_emig_migrationprogram_delta_setter(instance):
    original = instance.delta
    instance.delta = original
    assert instance.delta == original



@given(instance=emig_MigrationProgram_strategy)
def test_emig_migrationprogram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=emig_MigrationLibrary_strategy)
@settings(max_examples=50)
def test_emig_migrationlibrary_instantiation(instance):
    assert isinstance(instance, emig_MigrationLibrary)



@given(instance=emig_MigrationLibrary_strategy)
def test_emig_migrationlibrary_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=emig_MyModel_strategy)
@settings(max_examples=50)
def test_emig_mymodel_instantiation(instance):
    assert isinstance(instance, emig_MyModel)
