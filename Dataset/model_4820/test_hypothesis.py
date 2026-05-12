import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    model_analytical_AnalyticalModel,
    model_behavioural_BehaviouralModel,
    VirtualCubeDimension,
    VirtualCubeMeasure,
    Level,
    olap_model_Model,
    Hierarchy,
    NamedSet,
    CalculatedMember,
    Measure,
    Dimension,
    VirtualCube,
    Cube,
    BusinessColumnSet,
    business_model_Model,
    model_business_BusinessView,
    model_business_BusinessTable,
    BusinessColumn,
    model_business_SimpleBusinessColumn,
    model_business_CalculatedBusinessColumn,
    BusinessViewInnerJoinRelationship,
    BusinessDomain,
    BusinessIdentifier,
    BusinessRelationship,
    PhysicalColumn,
    model_ModelObject,
    model_ModelPropertyMapEntry,
    PhysicalForeignKey,
    PhysicalPrimaryKey,
    PhysicalTable,
    physical_model_Model,
    OlapModel,
    BusinessModel,
    PhysicalModel,
    ModelObject,
    model_physical_PhysicalPrimaryKey,
    model_physical_PhysicalModel,
    model_olap_CalculatedMember,
    model_business_BusinessColumn,
    model_business_BusinessColumnSet,
    model_business_BusinessIdentifier,
    model_olap_Dimension,
    model_physical_PhysicalForeignKey,
    model_business_BusinessModel,
    model_business_BusinessViewInnerJoinRelationship,
    model_olap_VirtualCubeMeasure,
    model_physical_PhysicalColumn,
    model_olap_OlapModel,
    model_olap_VirtualCubeDimension,
    model_business_BusinessDomain,
    model_physical_PhysicalTable,
    model_olap_Hierarchy,
    model_olap_Measure,
    model_business_BusinessRelationship,
    model_olap_VirtualCube,
    model_olap_Cube,
    model_olap_NamedSet,
    model_olap_Level,
    model_Model,
    model_ModelProperty,
    model_ModelPropertyType,
    model_ModelPropertyCategory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model_analytical_analyticalmodel_is_not_abstract():
    assert not inspect.isabstract(model_analytical_AnalyticalModel)


def test_model_analytical_analyticalmodel_constructor_exists():
    assert callable(model_analytical_AnalyticalModel.__init__)


def test_model_analytical_analyticalmodel_constructor_args():
    sig = inspect.signature(model_analytical_AnalyticalModel.__init__)
    params = list(sig.parameters.keys())



def test_model_behavioural_behaviouralmodel_is_not_abstract():
    assert not inspect.isabstract(model_behavioural_BehaviouralModel)


def test_model_behavioural_behaviouralmodel_constructor_exists():
    assert callable(model_behavioural_BehaviouralModel.__init__)


def test_model_behavioural_behaviouralmodel_constructor_args():
    sig = inspect.signature(model_behavioural_BehaviouralModel.__init__)
    params = list(sig.parameters.keys())



def test_virtualcubedimension_is_not_abstract():
    assert not inspect.isabstract(VirtualCubeDimension)


def test_virtualcubedimension_constructor_exists():
    assert callable(VirtualCubeDimension.__init__)


def test_virtualcubedimension_constructor_args():
    sig = inspect.signature(VirtualCubeDimension.__init__)
    params = list(sig.parameters.keys())



def test_virtualcubemeasure_is_not_abstract():
    assert not inspect.isabstract(VirtualCubeMeasure)


def test_virtualcubemeasure_constructor_exists():
    assert callable(VirtualCubeMeasure.__init__)


def test_virtualcubemeasure_constructor_args():
    sig = inspect.signature(VirtualCubeMeasure.__init__)
    params = list(sig.parameters.keys())



def test_level_is_not_abstract():
    assert not inspect.isabstract(Level)


def test_level_constructor_exists():
    assert callable(Level.__init__)


def test_level_constructor_args():
    sig = inspect.signature(Level.__init__)
    params = list(sig.parameters.keys())



def test_olap_model_model_is_not_abstract():
    assert not inspect.isabstract(olap_model_Model)


def test_olap_model_model_constructor_exists():
    assert callable(olap_model_Model.__init__)


def test_olap_model_model_constructor_args():
    sig = inspect.signature(olap_model_Model.__init__)
    params = list(sig.parameters.keys())



def test_hierarchy_is_not_abstract():
    assert not inspect.isabstract(Hierarchy)


def test_hierarchy_constructor_exists():
    assert callable(Hierarchy.__init__)


def test_hierarchy_constructor_args():
    sig = inspect.signature(Hierarchy.__init__)
    params = list(sig.parameters.keys())



def test_namedset_is_not_abstract():
    assert not inspect.isabstract(NamedSet)


def test_namedset_constructor_exists():
    assert callable(NamedSet.__init__)


def test_namedset_constructor_args():
    sig = inspect.signature(NamedSet.__init__)
    params = list(sig.parameters.keys())



def test_calculatedmember_is_not_abstract():
    assert not inspect.isabstract(CalculatedMember)


def test_calculatedmember_constructor_exists():
    assert callable(CalculatedMember.__init__)


def test_calculatedmember_constructor_args():
    sig = inspect.signature(CalculatedMember.__init__)
    params = list(sig.parameters.keys())



def test_measure_is_not_abstract():
    assert not inspect.isabstract(Measure)


def test_measure_constructor_exists():
    assert callable(Measure.__init__)


def test_measure_constructor_args():
    sig = inspect.signature(Measure.__init__)
    params = list(sig.parameters.keys())



def test_dimension_is_not_abstract():
    assert not inspect.isabstract(Dimension)


def test_dimension_constructor_exists():
    assert callable(Dimension.__init__)


def test_dimension_constructor_args():
    sig = inspect.signature(Dimension.__init__)
    params = list(sig.parameters.keys())



def test_virtualcube_is_not_abstract():
    assert not inspect.isabstract(VirtualCube)


def test_virtualcube_constructor_exists():
    assert callable(VirtualCube.__init__)


def test_virtualcube_constructor_args():
    sig = inspect.signature(VirtualCube.__init__)
    params = list(sig.parameters.keys())



def test_cube_is_not_abstract():
    assert not inspect.isabstract(Cube)


def test_cube_constructor_exists():
    assert callable(Cube.__init__)


def test_cube_constructor_args():
    sig = inspect.signature(Cube.__init__)
    params = list(sig.parameters.keys())



def test_businesscolumnset_is_not_abstract():
    assert not inspect.isabstract(BusinessColumnSet)


def test_businesscolumnset_constructor_exists():
    assert callable(BusinessColumnSet.__init__)


def test_businesscolumnset_constructor_args():
    sig = inspect.signature(BusinessColumnSet.__init__)
    params = list(sig.parameters.keys())



def test_business_model_model_is_not_abstract():
    assert not inspect.isabstract(business_model_Model)


def test_business_model_model_constructor_exists():
    assert callable(business_model_Model.__init__)


def test_business_model_model_constructor_args():
    sig = inspect.signature(business_model_Model.__init__)
    params = list(sig.parameters.keys())



def test_model_business_businessview_is_not_abstract():
    assert not inspect.isabstract(model_business_BusinessView)


def test_model_business_businessview_constructor_exists():
    assert callable(model_business_BusinessView.__init__)


def test_model_business_businessview_constructor_args():
    sig = inspect.signature(model_business_BusinessView.__init__)
    params = list(sig.parameters.keys())



def test_model_business_businesstable_is_not_abstract():
    assert not inspect.isabstract(model_business_BusinessTable)


def test_model_business_businesstable_constructor_exists():
    assert callable(model_business_BusinessTable.__init__)


def test_model_business_businesstable_constructor_args():
    sig = inspect.signature(model_business_BusinessTable.__init__)
    params = list(sig.parameters.keys())



def test_businesscolumn_is_not_abstract():
    assert not inspect.isabstract(BusinessColumn)


def test_businesscolumn_constructor_exists():
    assert callable(BusinessColumn.__init__)


def test_businesscolumn_constructor_args():
    sig = inspect.signature(BusinessColumn.__init__)
    params = list(sig.parameters.keys())



def test_model_business_simplebusinesscolumn_is_not_abstract():
    assert not inspect.isabstract(model_business_SimpleBusinessColumn)


def test_model_business_simplebusinesscolumn_constructor_exists():
    assert callable(model_business_SimpleBusinessColumn.__init__)


def test_model_business_simplebusinesscolumn_constructor_args():
    sig = inspect.signature(model_business_SimpleBusinessColumn.__init__)
    params = list(sig.parameters.keys())



def test_model_business_calculatedbusinesscolumn_is_not_abstract():
    assert not inspect.isabstract(model_business_CalculatedBusinessColumn)


def test_model_business_calculatedbusinesscolumn_constructor_exists():
    assert callable(model_business_CalculatedBusinessColumn.__init__)


def test_model_business_calculatedbusinesscolumn_constructor_args():
    sig = inspect.signature(model_business_CalculatedBusinessColumn.__init__)
    params = list(sig.parameters.keys())



def test_businessviewinnerjoinrelationship_is_not_abstract():
    assert not inspect.isabstract(BusinessViewInnerJoinRelationship)


def test_businessviewinnerjoinrelationship_constructor_exists():
    assert callable(BusinessViewInnerJoinRelationship.__init__)


def test_businessviewinnerjoinrelationship_constructor_args():
    sig = inspect.signature(BusinessViewInnerJoinRelationship.__init__)
    params = list(sig.parameters.keys())



def test_businessdomain_is_not_abstract():
    assert not inspect.isabstract(BusinessDomain)


def test_businessdomain_constructor_exists():
    assert callable(BusinessDomain.__init__)


def test_businessdomain_constructor_args():
    sig = inspect.signature(BusinessDomain.__init__)
    params = list(sig.parameters.keys())



def test_businessidentifier_is_not_abstract():
    assert not inspect.isabstract(BusinessIdentifier)


def test_businessidentifier_constructor_exists():
    assert callable(BusinessIdentifier.__init__)


def test_businessidentifier_constructor_args():
    sig = inspect.signature(BusinessIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_businessrelationship_is_not_abstract():
    assert not inspect.isabstract(BusinessRelationship)


def test_businessrelationship_constructor_exists():
    assert callable(BusinessRelationship.__init__)


def test_businessrelationship_constructor_args():
    sig = inspect.signature(BusinessRelationship.__init__)
    params = list(sig.parameters.keys())



def test_physicalcolumn_is_not_abstract():
    assert not inspect.isabstract(PhysicalColumn)


def test_physicalcolumn_constructor_exists():
    assert callable(PhysicalColumn.__init__)


def test_physicalcolumn_constructor_args():
    sig = inspect.signature(PhysicalColumn.__init__)
    params = list(sig.parameters.keys())



def test_model_modelobject_is_not_abstract():
    assert not inspect.isabstract(model_ModelObject)


def test_model_modelobject_constructor_exists():
    assert callable(model_ModelObject.__init__)


def test_model_modelobject_constructor_args():
    sig = inspect.signature(model_ModelObject.__init__)
    params = list(sig.parameters.keys())
    assert "uniqueName" in params, "Missing parameter 'uniqueName'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_model_modelobject_has_uniqueName():
    assert hasattr(model_ModelObject, "uniqueName")
    descriptor = None
    for klass in model_ModelObject.__mro__:
        if "uniqueName" in klass.__dict__:
            descriptor = klass.__dict__["uniqueName"]
            break
    assert isinstance(descriptor, property)

def test_model_modelobject_has_description():
    assert hasattr(model_ModelObject, "description")
    descriptor = None
    for klass in model_ModelObject.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_model_modelobject_has_name():
    assert hasattr(model_ModelObject, "name")
    descriptor = None
    for klass in model_ModelObject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model_modelobject_has_id():
    assert hasattr(model_ModelObject, "id")
    descriptor = None
    for klass in model_ModelObject.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_model_modelpropertymapentry_is_not_abstract():
    assert not inspect.isabstract(model_ModelPropertyMapEntry)


def test_model_modelpropertymapentry_constructor_exists():
    assert callable(model_ModelPropertyMapEntry.__init__)


def test_model_modelpropertymapentry_constructor_args():
    sig = inspect.signature(model_ModelPropertyMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_model_modelpropertymapentry_has_key():
    assert hasattr(model_ModelPropertyMapEntry, "key")
    descriptor = None
    for klass in model_ModelPropertyMapEntry.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_physicalforeignkey_is_not_abstract():
    assert not inspect.isabstract(PhysicalForeignKey)


def test_physicalforeignkey_constructor_exists():
    assert callable(PhysicalForeignKey.__init__)


def test_physicalforeignkey_constructor_args():
    sig = inspect.signature(PhysicalForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_physicalprimarykey_is_not_abstract():
    assert not inspect.isabstract(PhysicalPrimaryKey)


def test_physicalprimarykey_constructor_exists():
    assert callable(PhysicalPrimaryKey.__init__)


def test_physicalprimarykey_constructor_args():
    sig = inspect.signature(PhysicalPrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_physicaltable_is_not_abstract():
    assert not inspect.isabstract(PhysicalTable)


def test_physicaltable_constructor_exists():
    assert callable(PhysicalTable.__init__)


def test_physicaltable_constructor_args():
    sig = inspect.signature(PhysicalTable.__init__)
    params = list(sig.parameters.keys())



def test_physical_model_model_is_not_abstract():
    assert not inspect.isabstract(physical_model_Model)


def test_physical_model_model_constructor_exists():
    assert callable(physical_model_Model.__init__)


def test_physical_model_model_constructor_args():
    sig = inspect.signature(physical_model_Model.__init__)
    params = list(sig.parameters.keys())



def test_olapmodel_is_not_abstract():
    assert not inspect.isabstract(OlapModel)


def test_olapmodel_constructor_exists():
    assert callable(OlapModel.__init__)


def test_olapmodel_constructor_args():
    sig = inspect.signature(OlapModel.__init__)
    params = list(sig.parameters.keys())



def test_businessmodel_is_not_abstract():
    assert not inspect.isabstract(BusinessModel)


def test_businessmodel_constructor_exists():
    assert callable(BusinessModel.__init__)


def test_businessmodel_constructor_args():
    sig = inspect.signature(BusinessModel.__init__)
    params = list(sig.parameters.keys())



def test_physicalmodel_is_not_abstract():
    assert not inspect.isabstract(PhysicalModel)


def test_physicalmodel_constructor_exists():
    assert callable(PhysicalModel.__init__)


def test_physicalmodel_constructor_args():
    sig = inspect.signature(PhysicalModel.__init__)
    params = list(sig.parameters.keys())



def test_modelobject_is_not_abstract():
    assert not inspect.isabstract(ModelObject)


def test_modelobject_constructor_exists():
    assert callable(ModelObject.__init__)


def test_modelobject_constructor_args():
    sig = inspect.signature(ModelObject.__init__)
    params = list(sig.parameters.keys())



def test_model_physical_physicalprimarykey_is_not_abstract():
    assert not inspect.isabstract(model_physical_PhysicalPrimaryKey)


def test_model_physical_physicalprimarykey_constructor_exists():
    assert callable(model_physical_PhysicalPrimaryKey.__init__)


def test_model_physical_physicalprimarykey_constructor_args():
    sig = inspect.signature(model_physical_PhysicalPrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_model_physical_physicalmodel_is_not_abstract():
    assert not inspect.isabstract(model_physical_PhysicalModel)


def test_model_physical_physicalmodel_constructor_exists():
    assert callable(model_physical_PhysicalModel.__init__)


def test_model_physical_physicalmodel_constructor_args():
    sig = inspect.signature(model_physical_PhysicalModel.__init__)
    params = list(sig.parameters.keys())
    assert "databaseVersion" in params, "Missing parameter 'databaseVersion'"
    assert "databaseName" in params, "Missing parameter 'databaseName'"
    assert "schema" in params, "Missing parameter 'schema'"
    assert "catalog" in params, "Missing parameter 'catalog'"

def test_model_physical_physicalmodel_has_databaseVersion():
    assert hasattr(model_physical_PhysicalModel, "databaseVersion")
    descriptor = None
    for klass in model_physical_PhysicalModel.__mro__:
        if "databaseVersion" in klass.__dict__:
            descriptor = klass.__dict__["databaseVersion"]
            break
    assert isinstance(descriptor, property)

def test_model_physical_physicalmodel_has_databaseName():
    assert hasattr(model_physical_PhysicalModel, "databaseName")
    descriptor = None
    for klass in model_physical_PhysicalModel.__mro__:
        if "databaseName" in klass.__dict__:
            descriptor = klass.__dict__["databaseName"]
            break
    assert isinstance(descriptor, property)

def test_model_physical_physicalmodel_has_schema():
    assert hasattr(model_physical_PhysicalModel, "schema")
    descriptor = None
    for klass in model_physical_PhysicalModel.__mro__:
        if "schema" in klass.__dict__:
            descriptor = klass.__dict__["schema"]
            break
    assert isinstance(descriptor, property)

def test_model_physical_physicalmodel_has_catalog():
    assert hasattr(model_physical_PhysicalModel, "catalog")
    descriptor = None
    for klass in model_physical_PhysicalModel.__mro__:
        if "catalog" in klass.__dict__:
            descriptor = klass.__dict__["catalog"]
            break
    assert isinstance(descriptor, property)



def test_model_olap_calculatedmember_is_not_abstract():
    assert not inspect.isabstract(model_olap_CalculatedMember)


def test_model_olap_calculatedmember_constructor_exists():
    assert callable(model_olap_CalculatedMember.__init__)


def test_model_olap_calculatedmember_constructor_args():
    sig = inspect.signature(model_olap_CalculatedMember.__init__)
    params = list(sig.parameters.keys())



def test_model_business_businesscolumn_is_not_abstract():
    assert not inspect.isabstract(model_business_BusinessColumn)


def test_model_business_businesscolumn_constructor_exists():
    assert callable(model_business_BusinessColumn.__init__)


def test_model_business_businesscolumn_constructor_args():
    sig = inspect.signature(model_business_BusinessColumn.__init__)
    params = list(sig.parameters.keys())



def test_model_business_businesscolumnset_is_not_abstract():
    assert not inspect.isabstract(model_business_BusinessColumnSet)


def test_model_business_businesscolumnset_constructor_exists():
    assert callable(model_business_BusinessColumnSet.__init__)


def test_model_business_businesscolumnset_constructor_args():
    sig = inspect.signature(model_business_BusinessColumnSet.__init__)
    params = list(sig.parameters.keys())



def test_model_business_businessidentifier_is_not_abstract():
    assert not inspect.isabstract(model_business_BusinessIdentifier)


def test_model_business_businessidentifier_constructor_exists():
    assert callable(model_business_BusinessIdentifier.__init__)


def test_model_business_businessidentifier_constructor_args():
    sig = inspect.signature(model_business_BusinessIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_model_olap_dimension_is_not_abstract():
    assert not inspect.isabstract(model_olap_Dimension)


def test_model_olap_dimension_constructor_exists():
    assert callable(model_olap_Dimension.__init__)


def test_model_olap_dimension_constructor_args():
    sig = inspect.signature(model_olap_Dimension.__init__)
    params = list(sig.parameters.keys())



def test_model_physical_physicalforeignkey_is_not_abstract():
    assert not inspect.isabstract(model_physical_PhysicalForeignKey)


def test_model_physical_physicalforeignkey_constructor_exists():
    assert callable(model_physical_PhysicalForeignKey.__init__)


def test_model_physical_physicalforeignkey_constructor_args():
    sig = inspect.signature(model_physical_PhysicalForeignKey.__init__)
    params = list(sig.parameters.keys())
    assert "destinationName" in params, "Missing parameter 'destinationName'"
    assert "sourceName" in params, "Missing parameter 'sourceName'"

def test_model_physical_physicalforeignkey_has_destinationName():
    assert hasattr(model_physical_PhysicalForeignKey, "destinationName")
    descriptor = None
    for klass in model_physical_PhysicalForeignKey.__mro__:
        if "destinationName" in klass.__dict__:
            descriptor = klass.__dict__["destinationName"]
            break
    assert isinstance(descriptor, property)

def test_model_physical_physicalforeignkey_has_sourceName():
    assert hasattr(model_physical_PhysicalForeignKey, "sourceName")
    descriptor = None
    for klass in model_physical_PhysicalForeignKey.__mro__:
        if "sourceName" in klass.__dict__:
            descriptor = klass.__dict__["sourceName"]
            break
    assert isinstance(descriptor, property)



def test_model_business_businessmodel_is_not_abstract():
    assert not inspect.isabstract(model_business_BusinessModel)


def test_model_business_businessmodel_constructor_exists():
    assert callable(model_business_BusinessModel.__init__)


def test_model_business_businessmodel_constructor_args():
    sig = inspect.signature(model_business_BusinessModel.__init__)
    params = list(sig.parameters.keys())



def test_model_business_businessviewinnerjoinrelationship_is_not_abstract():
    assert not inspect.isabstract(model_business_BusinessViewInnerJoinRelationship)


def test_model_business_businessviewinnerjoinrelationship_constructor_exists():
    assert callable(model_business_BusinessViewInnerJoinRelationship.__init__)


def test_model_business_businessviewinnerjoinrelationship_constructor_args():
    sig = inspect.signature(model_business_BusinessViewInnerJoinRelationship.__init__)
    params = list(sig.parameters.keys())



def test_model_olap_virtualcubemeasure_is_not_abstract():
    assert not inspect.isabstract(model_olap_VirtualCubeMeasure)


def test_model_olap_virtualcubemeasure_constructor_exists():
    assert callable(model_olap_VirtualCubeMeasure.__init__)


def test_model_olap_virtualcubemeasure_constructor_args():
    sig = inspect.signature(model_olap_VirtualCubeMeasure.__init__)
    params = list(sig.parameters.keys())



def test_model_physical_physicalcolumn_is_not_abstract():
    assert not inspect.isabstract(model_physical_PhysicalColumn)


def test_model_physical_physicalcolumn_constructor_exists():
    assert callable(model_physical_PhysicalColumn.__init__)


def test_model_physical_physicalcolumn_constructor_args():
    sig = inspect.signature(model_physical_PhysicalColumn.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "dataType" in params, "Missing parameter 'dataType'"
    assert "decimalDigits" in params, "Missing parameter 'decimalDigits'"
    assert "position" in params, "Missing parameter 'position'"
    assert "size" in params, "Missing parameter 'size'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "radix" in params, "Missing parameter 'radix'"
    assert "nullable" in params, "Missing parameter 'nullable'"
    assert "octectLength" in params, "Missing parameter 'octectLength'"
    assert "typeName" in params, "Missing parameter 'typeName'"

def test_model_physical_physicalcolumn_has_comment():
    assert hasattr(model_physical_PhysicalColumn, "comment")
    descriptor = None
    for klass in model_physical_PhysicalColumn.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_model_physical_physicalcolumn_has_dataType():
    assert hasattr(model_physical_PhysicalColumn, "dataType")
    descriptor = None
    for klass in model_physical_PhysicalColumn.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
            break
    assert isinstance(descriptor, property)

def test_model_physical_physicalcolumn_has_decimalDigits():
    assert hasattr(model_physical_PhysicalColumn, "decimalDigits")
    descriptor = None
    for klass in model_physical_PhysicalColumn.__mro__:
        if "decimalDigits" in klass.__dict__:
            descriptor = klass.__dict__["decimalDigits"]
            break
    assert isinstance(descriptor, property)

def test_model_physical_physicalcolumn_has_position():
    assert hasattr(model_physical_PhysicalColumn, "position")
    descriptor = None
    for klass in model_physical_PhysicalColumn.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_model_physical_physicalcolumn_has_size():
    assert hasattr(model_physical_PhysicalColumn, "size")
    descriptor = None
    for klass in model_physical_PhysicalColumn.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_model_physical_physicalcolumn_has_defaultValue():
    assert hasattr(model_physical_PhysicalColumn, "defaultValue")
    descriptor = None
    for klass in model_physical_PhysicalColumn.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_model_physical_physicalcolumn_has_radix():
    assert hasattr(model_physical_PhysicalColumn, "radix")
    descriptor = None
    for klass in model_physical_PhysicalColumn.__mro__:
        if "radix" in klass.__dict__:
            descriptor = klass.__dict__["radix"]
            break
    assert isinstance(descriptor, property)

def test_model_physical_physicalcolumn_has_nullable():
    assert hasattr(model_physical_PhysicalColumn, "nullable")
    descriptor = None
    for klass in model_physical_PhysicalColumn.__mro__:
        if "nullable" in klass.__dict__:
            descriptor = klass.__dict__["nullable"]
            break
    assert isinstance(descriptor, property)

def test_model_physical_physicalcolumn_has_octectLength():
    assert hasattr(model_physical_PhysicalColumn, "octectLength")
    descriptor = None
    for klass in model_physical_PhysicalColumn.__mro__:
        if "octectLength" in klass.__dict__:
            descriptor = klass.__dict__["octectLength"]
            break
    assert isinstance(descriptor, property)

def test_model_physical_physicalcolumn_has_typeName():
    assert hasattr(model_physical_PhysicalColumn, "typeName")
    descriptor = None
    for klass in model_physical_PhysicalColumn.__mro__:
        if "typeName" in klass.__dict__:
            descriptor = klass.__dict__["typeName"]
            break
    assert isinstance(descriptor, property)



def test_model_olap_olapmodel_is_not_abstract():
    assert not inspect.isabstract(model_olap_OlapModel)


def test_model_olap_olapmodel_constructor_exists():
    assert callable(model_olap_OlapModel.__init__)


def test_model_olap_olapmodel_constructor_args():
    sig = inspect.signature(model_olap_OlapModel.__init__)
    params = list(sig.parameters.keys())



def test_model_olap_virtualcubedimension_is_not_abstract():
    assert not inspect.isabstract(model_olap_VirtualCubeDimension)


def test_model_olap_virtualcubedimension_constructor_exists():
    assert callable(model_olap_VirtualCubeDimension.__init__)


def test_model_olap_virtualcubedimension_constructor_args():
    sig = inspect.signature(model_olap_VirtualCubeDimension.__init__)
    params = list(sig.parameters.keys())



def test_model_business_businessdomain_is_not_abstract():
    assert not inspect.isabstract(model_business_BusinessDomain)


def test_model_business_businessdomain_constructor_exists():
    assert callable(model_business_BusinessDomain.__init__)


def test_model_business_businessdomain_constructor_args():
    sig = inspect.signature(model_business_BusinessDomain.__init__)
    params = list(sig.parameters.keys())



def test_model_physical_physicaltable_is_not_abstract():
    assert not inspect.isabstract(model_physical_PhysicalTable)


def test_model_physical_physicaltable_constructor_exists():
    assert callable(model_physical_PhysicalTable.__init__)


def test_model_physical_physicaltable_constructor_args():
    sig = inspect.signature(model_physical_PhysicalTable.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "type" in params, "Missing parameter 'type'"

def test_model_physical_physicaltable_has_comment():
    assert hasattr(model_physical_PhysicalTable, "comment")
    descriptor = None
    for klass in model_physical_PhysicalTable.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_model_physical_physicaltable_has_type():
    assert hasattr(model_physical_PhysicalTable, "type")
    descriptor = None
    for klass in model_physical_PhysicalTable.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_model_olap_hierarchy_is_not_abstract():
    assert not inspect.isabstract(model_olap_Hierarchy)


def test_model_olap_hierarchy_constructor_exists():
    assert callable(model_olap_Hierarchy.__init__)


def test_model_olap_hierarchy_constructor_args():
    sig = inspect.signature(model_olap_Hierarchy.__init__)
    params = list(sig.parameters.keys())



def test_model_olap_measure_is_not_abstract():
    assert not inspect.isabstract(model_olap_Measure)


def test_model_olap_measure_constructor_exists():
    assert callable(model_olap_Measure.__init__)


def test_model_olap_measure_constructor_args():
    sig = inspect.signature(model_olap_Measure.__init__)
    params = list(sig.parameters.keys())



def test_model_business_businessrelationship_is_not_abstract():
    assert not inspect.isabstract(model_business_BusinessRelationship)


def test_model_business_businessrelationship_constructor_exists():
    assert callable(model_business_BusinessRelationship.__init__)


def test_model_business_businessrelationship_constructor_args():
    sig = inspect.signature(model_business_BusinessRelationship.__init__)
    params = list(sig.parameters.keys())



def test_model_olap_virtualcube_is_not_abstract():
    assert not inspect.isabstract(model_olap_VirtualCube)


def test_model_olap_virtualcube_constructor_exists():
    assert callable(model_olap_VirtualCube.__init__)


def test_model_olap_virtualcube_constructor_args():
    sig = inspect.signature(model_olap_VirtualCube.__init__)
    params = list(sig.parameters.keys())



def test_model_olap_cube_is_not_abstract():
    assert not inspect.isabstract(model_olap_Cube)


def test_model_olap_cube_constructor_exists():
    assert callable(model_olap_Cube.__init__)


def test_model_olap_cube_constructor_args():
    sig = inspect.signature(model_olap_Cube.__init__)
    params = list(sig.parameters.keys())



def test_model_olap_namedset_is_not_abstract():
    assert not inspect.isabstract(model_olap_NamedSet)


def test_model_olap_namedset_constructor_exists():
    assert callable(model_olap_NamedSet.__init__)


def test_model_olap_namedset_constructor_args():
    sig = inspect.signature(model_olap_NamedSet.__init__)
    params = list(sig.parameters.keys())



def test_model_olap_level_is_not_abstract():
    assert not inspect.isabstract(model_olap_Level)


def test_model_olap_level_constructor_exists():
    assert callable(model_olap_Level.__init__)


def test_model_olap_level_constructor_args():
    sig = inspect.signature(model_olap_Level.__init__)
    params = list(sig.parameters.keys())



def test_model_model_is_not_abstract():
    assert not inspect.isabstract(model_Model)


def test_model_model_constructor_exists():
    assert callable(model_Model.__init__)


def test_model_model_constructor_args():
    sig = inspect.signature(model_Model.__init__)
    params = list(sig.parameters.keys())



def test_model_modelproperty_is_not_abstract():
    assert not inspect.isabstract(model_ModelProperty)


def test_model_modelproperty_constructor_exists():
    assert callable(model_ModelProperty.__init__)


def test_model_modelproperty_constructor_args():
    sig = inspect.signature(model_ModelProperty.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_model_modelproperty_has_value():
    assert hasattr(model_ModelProperty, "value")
    descriptor = None
    for klass in model_ModelProperty.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_model_modelpropertytype_is_not_abstract():
    assert not inspect.isabstract(model_ModelPropertyType)


def test_model_modelpropertytype_constructor_exists():
    assert callable(model_ModelPropertyType.__init__)


def test_model_modelpropertytype_constructor_args():
    sig = inspect.signature(model_ModelPropertyType.__init__)
    params = list(sig.parameters.keys())
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"
    assert "admissibleValues" in params, "Missing parameter 'admissibleValues'"
    assert "id" in params, "Missing parameter 'id'"

def test_model_modelpropertytype_has_defaultValue():
    assert hasattr(model_ModelPropertyType, "defaultValue")
    descriptor = None
    for klass in model_ModelPropertyType.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_model_modelpropertytype_has_name():
    assert hasattr(model_ModelPropertyType, "name")
    descriptor = None
    for klass in model_ModelPropertyType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model_modelpropertytype_has_description():
    assert hasattr(model_ModelPropertyType, "description")
    descriptor = None
    for klass in model_ModelPropertyType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_model_modelpropertytype_has_admissibleValues():
    assert hasattr(model_ModelPropertyType, "admissibleValues")
    descriptor = None
    for klass in model_ModelPropertyType.__mro__:
        if "admissibleValues" in klass.__dict__:
            descriptor = klass.__dict__["admissibleValues"]
            break
    assert isinstance(descriptor, property)

def test_model_modelpropertytype_has_id():
    assert hasattr(model_ModelPropertyType, "id")
    descriptor = None
    for klass in model_ModelPropertyType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_model_modelpropertycategory_is_not_abstract():
    assert not inspect.isabstract(model_ModelPropertyCategory)


def test_model_modelpropertycategory_constructor_exists():
    assert callable(model_ModelPropertyCategory.__init__)


def test_model_modelpropertycategory_constructor_args():
    sig = inspect.signature(model_ModelPropertyCategory.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_model_modelpropertycategory_has_name():
    assert hasattr(model_ModelPropertyCategory, "name")
    descriptor = None
    for klass in model_ModelPropertyCategory.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model_modelpropertycategory_has_description():
    assert hasattr(model_ModelPropertyCategory, "description")
    descriptor = None
    for klass in model_ModelPropertyCategory.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
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
model_analytical_AnalyticalModel_strategy = st.builds(
    model_analytical_AnalyticalModel,
)
model_behavioural_BehaviouralModel_strategy = st.builds(
    model_behavioural_BehaviouralModel,
)
VirtualCubeDimension_strategy = st.builds(
    VirtualCubeDimension,
)
VirtualCubeMeasure_strategy = st.builds(
    VirtualCubeMeasure,
)
Level_strategy = st.builds(
    Level,
)
olap_model_Model_strategy = st.builds(
    olap_model_Model,
)
Hierarchy_strategy = st.builds(
    Hierarchy,
)
NamedSet_strategy = st.builds(
    NamedSet,
)
CalculatedMember_strategy = st.builds(
    CalculatedMember,
)
Measure_strategy = st.builds(
    Measure,
)
Dimension_strategy = st.builds(
    Dimension,
)
VirtualCube_strategy = st.builds(
    VirtualCube,
)
Cube_strategy = st.builds(
    Cube,
)
BusinessColumnSet_strategy = st.builds(
    BusinessColumnSet,
)
business_model_Model_strategy = st.builds(
    business_model_Model,
)
model_business_BusinessView_strategy = st.builds(
    model_business_BusinessView,
)
model_business_BusinessTable_strategy = st.builds(
    model_business_BusinessTable,
)
BusinessColumn_strategy = st.builds(
    BusinessColumn,
)
model_business_SimpleBusinessColumn_strategy = st.builds(
    model_business_SimpleBusinessColumn,
)
model_business_CalculatedBusinessColumn_strategy = st.builds(
    model_business_CalculatedBusinessColumn,
)
BusinessViewInnerJoinRelationship_strategy = st.builds(
    BusinessViewInnerJoinRelationship,
)
BusinessDomain_strategy = st.builds(
    BusinessDomain,
)
BusinessIdentifier_strategy = st.builds(
    BusinessIdentifier,
)
BusinessRelationship_strategy = st.builds(
    BusinessRelationship,
)
PhysicalColumn_strategy = st.builds(
    PhysicalColumn,
)
model_ModelObject_strategy = st.builds(
    model_ModelObject,
    uniqueName=
        safe_text,
    description=
        safe_text,
    name=
        safe_text,
    id=
        safe_text
)
model_ModelPropertyMapEntry_strategy = st.builds(
    model_ModelPropertyMapEntry,
    key=
        safe_text
)
PhysicalForeignKey_strategy = st.builds(
    PhysicalForeignKey,
)
PhysicalPrimaryKey_strategy = st.builds(
    PhysicalPrimaryKey,
)
PhysicalTable_strategy = st.builds(
    PhysicalTable,
)
physical_model_Model_strategy = st.builds(
    physical_model_Model,
)
OlapModel_strategy = st.builds(
    OlapModel,
)
BusinessModel_strategy = st.builds(
    BusinessModel,
)
PhysicalModel_strategy = st.builds(
    PhysicalModel,
)
ModelObject_strategy = st.builds(
    ModelObject,
)
model_physical_PhysicalPrimaryKey_strategy = st.builds(
    model_physical_PhysicalPrimaryKey,
)
model_physical_PhysicalModel_strategy = st.builds(
    model_physical_PhysicalModel,
    databaseVersion=
        safe_text,
    databaseName=
        safe_text,
    schema=
        safe_text,
    catalog=
        safe_text
)
model_olap_CalculatedMember_strategy = st.builds(
    model_olap_CalculatedMember,
)
model_business_BusinessColumn_strategy = st.builds(
    model_business_BusinessColumn,
)
model_business_BusinessColumnSet_strategy = st.builds(
    model_business_BusinessColumnSet,
)
model_business_BusinessIdentifier_strategy = st.builds(
    model_business_BusinessIdentifier,
)
model_olap_Dimension_strategy = st.builds(
    model_olap_Dimension,
)
model_physical_PhysicalForeignKey_strategy = st.builds(
    model_physical_PhysicalForeignKey,
    destinationName=
        safe_text,
    sourceName=
        safe_text
)
model_business_BusinessModel_strategy = st.builds(
    model_business_BusinessModel,
)
model_business_BusinessViewInnerJoinRelationship_strategy = st.builds(
    model_business_BusinessViewInnerJoinRelationship,
)
model_olap_VirtualCubeMeasure_strategy = st.builds(
    model_olap_VirtualCubeMeasure,
)
model_physical_PhysicalColumn_strategy = st.builds(
    model_physical_PhysicalColumn,
    comment=
        safe_text,
    dataType=
        safe_text,
    decimalDigits=
        st.integers(),
    position=
        st.integers(),
    size=
        st.integers(),
    defaultValue=
        safe_text,
    radix=
        st.integers(),
    nullable=
        st.booleans(),
    octectLength=
        st.integers(),
    typeName=
        safe_text
)
model_olap_OlapModel_strategy = st.builds(
    model_olap_OlapModel,
)
model_olap_VirtualCubeDimension_strategy = st.builds(
    model_olap_VirtualCubeDimension,
)
model_business_BusinessDomain_strategy = st.builds(
    model_business_BusinessDomain,
)
model_physical_PhysicalTable_strategy = st.builds(
    model_physical_PhysicalTable,
    comment=
        safe_text,
    type=
        safe_text
)
model_olap_Hierarchy_strategy = st.builds(
    model_olap_Hierarchy,
)
model_olap_Measure_strategy = st.builds(
    model_olap_Measure,
)
model_business_BusinessRelationship_strategy = st.builds(
    model_business_BusinessRelationship,
)
model_olap_VirtualCube_strategy = st.builds(
    model_olap_VirtualCube,
)
model_olap_Cube_strategy = st.builds(
    model_olap_Cube,
)
model_olap_NamedSet_strategy = st.builds(
    model_olap_NamedSet,
)
model_olap_Level_strategy = st.builds(
    model_olap_Level,
)
model_Model_strategy = st.builds(
    model_Model,
)
model_ModelProperty_strategy = st.builds(
    model_ModelProperty,
    value=
        safe_text
)
model_ModelPropertyType_strategy = st.builds(
    model_ModelPropertyType,
    defaultValue=
        safe_text,
    name=
        safe_text,
    description=
        safe_text,
    admissibleValues=
        safe_text,
    id=
        safe_text
)
model_ModelPropertyCategory_strategy = st.builds(
    model_ModelPropertyCategory,
    name=
        safe_text,
    description=
        safe_text
)

@given(instance=model_analytical_AnalyticalModel_strategy)
@settings(max_examples=50)
def test_model_analytical_analyticalmodel_instantiation(instance):
    assert isinstance(instance, model_analytical_AnalyticalModel)

@given(instance=model_behavioural_BehaviouralModel_strategy)
@settings(max_examples=50)
def test_model_behavioural_behaviouralmodel_instantiation(instance):
    assert isinstance(instance, model_behavioural_BehaviouralModel)

@given(instance=VirtualCubeDimension_strategy)
@settings(max_examples=50)
def test_virtualcubedimension_instantiation(instance):
    assert isinstance(instance, VirtualCubeDimension)

@given(instance=VirtualCubeMeasure_strategy)
@settings(max_examples=50)
def test_virtualcubemeasure_instantiation(instance):
    assert isinstance(instance, VirtualCubeMeasure)

@given(instance=Level_strategy)
@settings(max_examples=50)
def test_level_instantiation(instance):
    assert isinstance(instance, Level)

@given(instance=olap_model_Model_strategy)
@settings(max_examples=50)
def test_olap_model_model_instantiation(instance):
    assert isinstance(instance, olap_model_Model)

@given(instance=Hierarchy_strategy)
@settings(max_examples=50)
def test_hierarchy_instantiation(instance):
    assert isinstance(instance, Hierarchy)

@given(instance=NamedSet_strategy)
@settings(max_examples=50)
def test_namedset_instantiation(instance):
    assert isinstance(instance, NamedSet)

@given(instance=CalculatedMember_strategy)
@settings(max_examples=50)
def test_calculatedmember_instantiation(instance):
    assert isinstance(instance, CalculatedMember)

@given(instance=Measure_strategy)
@settings(max_examples=50)
def test_measure_instantiation(instance):
    assert isinstance(instance, Measure)

@given(instance=Dimension_strategy)
@settings(max_examples=50)
def test_dimension_instantiation(instance):
    assert isinstance(instance, Dimension)

@given(instance=VirtualCube_strategy)
@settings(max_examples=50)
def test_virtualcube_instantiation(instance):
    assert isinstance(instance, VirtualCube)

@given(instance=Cube_strategy)
@settings(max_examples=50)
def test_cube_instantiation(instance):
    assert isinstance(instance, Cube)

@given(instance=BusinessColumnSet_strategy)
@settings(max_examples=50)
def test_businesscolumnset_instantiation(instance):
    assert isinstance(instance, BusinessColumnSet)

@given(instance=business_model_Model_strategy)
@settings(max_examples=50)
def test_business_model_model_instantiation(instance):
    assert isinstance(instance, business_model_Model)

@given(instance=model_business_BusinessView_strategy)
@settings(max_examples=50)
def test_model_business_businessview_instantiation(instance):
    assert isinstance(instance, model_business_BusinessView)

@given(instance=model_business_BusinessTable_strategy)
@settings(max_examples=50)
def test_model_business_businesstable_instantiation(instance):
    assert isinstance(instance, model_business_BusinessTable)

@given(instance=BusinessColumn_strategy)
@settings(max_examples=50)
def test_businesscolumn_instantiation(instance):
    assert isinstance(instance, BusinessColumn)

@given(instance=model_business_SimpleBusinessColumn_strategy)
@settings(max_examples=50)
def test_model_business_simplebusinesscolumn_instantiation(instance):
    assert isinstance(instance, model_business_SimpleBusinessColumn)

@given(instance=model_business_CalculatedBusinessColumn_strategy)
@settings(max_examples=50)
def test_model_business_calculatedbusinesscolumn_instantiation(instance):
    assert isinstance(instance, model_business_CalculatedBusinessColumn)

@given(instance=BusinessViewInnerJoinRelationship_strategy)
@settings(max_examples=50)
def test_businessviewinnerjoinrelationship_instantiation(instance):
    assert isinstance(instance, BusinessViewInnerJoinRelationship)

@given(instance=BusinessDomain_strategy)
@settings(max_examples=50)
def test_businessdomain_instantiation(instance):
    assert isinstance(instance, BusinessDomain)

@given(instance=BusinessIdentifier_strategy)
@settings(max_examples=50)
def test_businessidentifier_instantiation(instance):
    assert isinstance(instance, BusinessIdentifier)

@given(instance=BusinessRelationship_strategy)
@settings(max_examples=50)
def test_businessrelationship_instantiation(instance):
    assert isinstance(instance, BusinessRelationship)

@given(instance=PhysicalColumn_strategy)
@settings(max_examples=50)
def test_physicalcolumn_instantiation(instance):
    assert isinstance(instance, PhysicalColumn)

@given(instance=model_ModelObject_strategy)
@settings(max_examples=50)
def test_model_modelobject_instantiation(instance):
    assert isinstance(instance, model_ModelObject)



@given(instance=model_ModelObject_strategy)
def test_model_modelobject_uniqueName_setter(instance):
    original = instance.uniqueName
    instance.uniqueName = original
    assert instance.uniqueName == original



@given(instance=model_ModelObject_strategy)
def test_model_modelobject_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=model_ModelObject_strategy)
def test_model_modelobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=model_ModelObject_strategy)
def test_model_modelobject_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=model_ModelPropertyMapEntry_strategy)
@settings(max_examples=50)
def test_model_modelpropertymapentry_instantiation(instance):
    assert isinstance(instance, model_ModelPropertyMapEntry)



@given(instance=model_ModelPropertyMapEntry_strategy)
def test_model_modelpropertymapentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=PhysicalForeignKey_strategy)
@settings(max_examples=50)
def test_physicalforeignkey_instantiation(instance):
    assert isinstance(instance, PhysicalForeignKey)

@given(instance=PhysicalPrimaryKey_strategy)
@settings(max_examples=50)
def test_physicalprimarykey_instantiation(instance):
    assert isinstance(instance, PhysicalPrimaryKey)

@given(instance=PhysicalTable_strategy)
@settings(max_examples=50)
def test_physicaltable_instantiation(instance):
    assert isinstance(instance, PhysicalTable)

@given(instance=physical_model_Model_strategy)
@settings(max_examples=50)
def test_physical_model_model_instantiation(instance):
    assert isinstance(instance, physical_model_Model)

@given(instance=OlapModel_strategy)
@settings(max_examples=50)
def test_olapmodel_instantiation(instance):
    assert isinstance(instance, OlapModel)

@given(instance=BusinessModel_strategy)
@settings(max_examples=50)
def test_businessmodel_instantiation(instance):
    assert isinstance(instance, BusinessModel)

@given(instance=PhysicalModel_strategy)
@settings(max_examples=50)
def test_physicalmodel_instantiation(instance):
    assert isinstance(instance, PhysicalModel)

@given(instance=ModelObject_strategy)
@settings(max_examples=50)
def test_modelobject_instantiation(instance):
    assert isinstance(instance, ModelObject)

@given(instance=model_physical_PhysicalPrimaryKey_strategy)
@settings(max_examples=50)
def test_model_physical_physicalprimarykey_instantiation(instance):
    assert isinstance(instance, model_physical_PhysicalPrimaryKey)

@given(instance=model_physical_PhysicalModel_strategy)
@settings(max_examples=50)
def test_model_physical_physicalmodel_instantiation(instance):
    assert isinstance(instance, model_physical_PhysicalModel)



@given(instance=model_physical_PhysicalModel_strategy)
def test_model_physical_physicalmodel_databaseVersion_setter(instance):
    original = instance.databaseVersion
    instance.databaseVersion = original
    assert instance.databaseVersion == original



@given(instance=model_physical_PhysicalModel_strategy)
def test_model_physical_physicalmodel_databaseName_setter(instance):
    original = instance.databaseName
    instance.databaseName = original
    assert instance.databaseName == original



@given(instance=model_physical_PhysicalModel_strategy)
def test_model_physical_physicalmodel_schema_setter(instance):
    original = instance.schema
    instance.schema = original
    assert instance.schema == original



@given(instance=model_physical_PhysicalModel_strategy)
def test_model_physical_physicalmodel_catalog_setter(instance):
    original = instance.catalog
    instance.catalog = original
    assert instance.catalog == original

@given(instance=model_olap_CalculatedMember_strategy)
@settings(max_examples=50)
def test_model_olap_calculatedmember_instantiation(instance):
    assert isinstance(instance, model_olap_CalculatedMember)

@given(instance=model_business_BusinessColumn_strategy)
@settings(max_examples=50)
def test_model_business_businesscolumn_instantiation(instance):
    assert isinstance(instance, model_business_BusinessColumn)

@given(instance=model_business_BusinessColumnSet_strategy)
@settings(max_examples=50)
def test_model_business_businesscolumnset_instantiation(instance):
    assert isinstance(instance, model_business_BusinessColumnSet)

@given(instance=model_business_BusinessIdentifier_strategy)
@settings(max_examples=50)
def test_model_business_businessidentifier_instantiation(instance):
    assert isinstance(instance, model_business_BusinessIdentifier)

@given(instance=model_olap_Dimension_strategy)
@settings(max_examples=50)
def test_model_olap_dimension_instantiation(instance):
    assert isinstance(instance, model_olap_Dimension)

@given(instance=model_physical_PhysicalForeignKey_strategy)
@settings(max_examples=50)
def test_model_physical_physicalforeignkey_instantiation(instance):
    assert isinstance(instance, model_physical_PhysicalForeignKey)



@given(instance=model_physical_PhysicalForeignKey_strategy)
def test_model_physical_physicalforeignkey_destinationName_setter(instance):
    original = instance.destinationName
    instance.destinationName = original
    assert instance.destinationName == original



@given(instance=model_physical_PhysicalForeignKey_strategy)
def test_model_physical_physicalforeignkey_sourceName_setter(instance):
    original = instance.sourceName
    instance.sourceName = original
    assert instance.sourceName == original

@given(instance=model_business_BusinessModel_strategy)
@settings(max_examples=50)
def test_model_business_businessmodel_instantiation(instance):
    assert isinstance(instance, model_business_BusinessModel)

@given(instance=model_business_BusinessViewInnerJoinRelationship_strategy)
@settings(max_examples=50)
def test_model_business_businessviewinnerjoinrelationship_instantiation(instance):
    assert isinstance(instance, model_business_BusinessViewInnerJoinRelationship)

@given(instance=model_olap_VirtualCubeMeasure_strategy)
@settings(max_examples=50)
def test_model_olap_virtualcubemeasure_instantiation(instance):
    assert isinstance(instance, model_olap_VirtualCubeMeasure)

@given(instance=model_physical_PhysicalColumn_strategy)
@settings(max_examples=50)
def test_model_physical_physicalcolumn_instantiation(instance):
    assert isinstance(instance, model_physical_PhysicalColumn)



@given(instance=model_physical_PhysicalColumn_strategy)
def test_model_physical_physicalcolumn_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=model_physical_PhysicalColumn_strategy)
def test_model_physical_physicalcolumn_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original



@given(instance=model_physical_PhysicalColumn_strategy)
def test_model_physical_physicalcolumn_decimalDigits_setter(instance):
    original = instance.decimalDigits
    instance.decimalDigits = original
    assert instance.decimalDigits == original



@given(instance=model_physical_PhysicalColumn_strategy)
def test_model_physical_physicalcolumn_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original



@given(instance=model_physical_PhysicalColumn_strategy)
def test_model_physical_physicalcolumn_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=model_physical_PhysicalColumn_strategy)
def test_model_physical_physicalcolumn_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original



@given(instance=model_physical_PhysicalColumn_strategy)
def test_model_physical_physicalcolumn_radix_setter(instance):
    original = instance.radix
    instance.radix = original
    assert instance.radix == original



@given(instance=model_physical_PhysicalColumn_strategy)
def test_model_physical_physicalcolumn_nullable_setter(instance):
    original = instance.nullable
    instance.nullable = original
    assert instance.nullable == original



@given(instance=model_physical_PhysicalColumn_strategy)
def test_model_physical_physicalcolumn_octectLength_setter(instance):
    original = instance.octectLength
    instance.octectLength = original
    assert instance.octectLength == original



@given(instance=model_physical_PhysicalColumn_strategy)
def test_model_physical_physicalcolumn_typeName_setter(instance):
    original = instance.typeName
    instance.typeName = original
    assert instance.typeName == original

@given(instance=model_olap_OlapModel_strategy)
@settings(max_examples=50)
def test_model_olap_olapmodel_instantiation(instance):
    assert isinstance(instance, model_olap_OlapModel)

@given(instance=model_olap_VirtualCubeDimension_strategy)
@settings(max_examples=50)
def test_model_olap_virtualcubedimension_instantiation(instance):
    assert isinstance(instance, model_olap_VirtualCubeDimension)

@given(instance=model_business_BusinessDomain_strategy)
@settings(max_examples=50)
def test_model_business_businessdomain_instantiation(instance):
    assert isinstance(instance, model_business_BusinessDomain)

@given(instance=model_physical_PhysicalTable_strategy)
@settings(max_examples=50)
def test_model_physical_physicaltable_instantiation(instance):
    assert isinstance(instance, model_physical_PhysicalTable)



@given(instance=model_physical_PhysicalTable_strategy)
def test_model_physical_physicaltable_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=model_physical_PhysicalTable_strategy)
def test_model_physical_physicaltable_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=model_olap_Hierarchy_strategy)
@settings(max_examples=50)
def test_model_olap_hierarchy_instantiation(instance):
    assert isinstance(instance, model_olap_Hierarchy)

@given(instance=model_olap_Measure_strategy)
@settings(max_examples=50)
def test_model_olap_measure_instantiation(instance):
    assert isinstance(instance, model_olap_Measure)

@given(instance=model_business_BusinessRelationship_strategy)
@settings(max_examples=50)
def test_model_business_businessrelationship_instantiation(instance):
    assert isinstance(instance, model_business_BusinessRelationship)

@given(instance=model_olap_VirtualCube_strategy)
@settings(max_examples=50)
def test_model_olap_virtualcube_instantiation(instance):
    assert isinstance(instance, model_olap_VirtualCube)

@given(instance=model_olap_Cube_strategy)
@settings(max_examples=50)
def test_model_olap_cube_instantiation(instance):
    assert isinstance(instance, model_olap_Cube)

@given(instance=model_olap_NamedSet_strategy)
@settings(max_examples=50)
def test_model_olap_namedset_instantiation(instance):
    assert isinstance(instance, model_olap_NamedSet)

@given(instance=model_olap_Level_strategy)
@settings(max_examples=50)
def test_model_olap_level_instantiation(instance):
    assert isinstance(instance, model_olap_Level)

@given(instance=model_Model_strategy)
@settings(max_examples=50)
def test_model_model_instantiation(instance):
    assert isinstance(instance, model_Model)

@given(instance=model_ModelProperty_strategy)
@settings(max_examples=50)
def test_model_modelproperty_instantiation(instance):
    assert isinstance(instance, model_ModelProperty)



@given(instance=model_ModelProperty_strategy)
def test_model_modelproperty_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=model_ModelPropertyType_strategy)
@settings(max_examples=50)
def test_model_modelpropertytype_instantiation(instance):
    assert isinstance(instance, model_ModelPropertyType)



@given(instance=model_ModelPropertyType_strategy)
def test_model_modelpropertytype_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original



@given(instance=model_ModelPropertyType_strategy)
def test_model_modelpropertytype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=model_ModelPropertyType_strategy)
def test_model_modelpropertytype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=model_ModelPropertyType_strategy)
def test_model_modelpropertytype_admissibleValues_setter(instance):
    original = instance.admissibleValues
    instance.admissibleValues = original
    assert instance.admissibleValues == original



@given(instance=model_ModelPropertyType_strategy)
def test_model_modelpropertytype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=model_ModelPropertyCategory_strategy)
@settings(max_examples=50)
def test_model_modelpropertycategory_instantiation(instance):
    assert isinstance(instance, model_ModelPropertyCategory)



@given(instance=model_ModelPropertyCategory_strategy)
def test_model_modelpropertycategory_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=model_ModelPropertyCategory_strategy)
def test_model_modelpropertycategory_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original
