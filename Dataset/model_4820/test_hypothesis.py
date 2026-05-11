import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    model::analytical::AnalyticalModel,
    model::behavioural::BehaviouralModel,
    VirtualCubeDimension,
    VirtualCubeMeasure,
    Level,
    olap::model::Model,
    Hierarchy,
    NamedSet,
    CalculatedMember,
    Measure,
    Dimension,
    VirtualCube,
    Cube,
    BusinessColumnSet,
    business::model::Model,
    model::business::BusinessView,
    model::business::BusinessTable,
    BusinessColumn,
    model::business::CalculatedBusinessColumn,
    model::business::SimpleBusinessColumn,
    BusinessViewInnerJoinRelationship,
    BusinessDomain,
    BusinessIdentifier,
    BusinessRelationship,
    PhysicalColumn,
    model::ModelObject,
    model::ModelPropertyMapEntry,
    PhysicalForeignKey,
    PhysicalPrimaryKey,
    PhysicalTable,
    physical::model::Model,
    OlapModel,
    BusinessModel,
    PhysicalModel,
    ModelObject,
    model::physical::PhysicalTable,
    model::olap::VirtualCubeDimension,
    model::olap::VirtualCube,
    model::business::BusinessColumn,
    model::physical::PhysicalForeignKey,
    model::physical::PhysicalColumn,
    model::olap::Cube,
    model::business::BusinessColumnSet,
    model::olap::NamedSet,
    model::physical::PhysicalPrimaryKey,
    model::business::BusinessIdentifier,
    model::business::BusinessViewInnerJoinRelationship,
    model::business::BusinessRelationship,
    model::olap::Level,
    model::physical::PhysicalModel,
    model::olap::Measure,
    model::olap::OlapModel,
    model::olap::VirtualCubeMeasure,
    model::business::BusinessModel,
    model::business::BusinessDomain,
    model::olap::CalculatedMember,
    model::olap::Hierarchy,
    model::olap::Dimension,
    model::Model,
    model::ModelProperty,
    model::ModelPropertyType,
    model::ModelPropertyCategory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model::analytical::analyticalmodel_is_not_abstract():
    assert not inspect.isabstract(model::analytical::AnalyticalModel)


def test_model::analytical::analyticalmodel_constructor_exists():
    assert callable(model::analytical::AnalyticalModel.__init__)


def test_model::analytical::analyticalmodel_constructor_args():
    sig = inspect.signature(model::analytical::AnalyticalModel.__init__)
    params = list(sig.parameters.keys())



def test_model::behavioural::behaviouralmodel_is_not_abstract():
    assert not inspect.isabstract(model::behavioural::BehaviouralModel)


def test_model::behavioural::behaviouralmodel_constructor_exists():
    assert callable(model::behavioural::BehaviouralModel.__init__)


def test_model::behavioural::behaviouralmodel_constructor_args():
    sig = inspect.signature(model::behavioural::BehaviouralModel.__init__)
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



def test_olap::model::model_is_not_abstract():
    assert not inspect.isabstract(olap::model::Model)


def test_olap::model::model_constructor_exists():
    assert callable(olap::model::Model.__init__)


def test_olap::model::model_constructor_args():
    sig = inspect.signature(olap::model::Model.__init__)
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



def test_business::model::model_is_not_abstract():
    assert not inspect.isabstract(business::model::Model)


def test_business::model::model_constructor_exists():
    assert callable(business::model::Model.__init__)


def test_business::model::model_constructor_args():
    sig = inspect.signature(business::model::Model.__init__)
    params = list(sig.parameters.keys())



def test_model::business::businessview_is_not_abstract():
    assert not inspect.isabstract(model::business::BusinessView)


def test_model::business::businessview_constructor_exists():
    assert callable(model::business::BusinessView.__init__)


def test_model::business::businessview_constructor_args():
    sig = inspect.signature(model::business::BusinessView.__init__)
    params = list(sig.parameters.keys())



def test_model::business::businesstable_is_not_abstract():
    assert not inspect.isabstract(model::business::BusinessTable)


def test_model::business::businesstable_constructor_exists():
    assert callable(model::business::BusinessTable.__init__)


def test_model::business::businesstable_constructor_args():
    sig = inspect.signature(model::business::BusinessTable.__init__)
    params = list(sig.parameters.keys())



def test_businesscolumn_is_not_abstract():
    assert not inspect.isabstract(BusinessColumn)


def test_businesscolumn_constructor_exists():
    assert callable(BusinessColumn.__init__)


def test_businesscolumn_constructor_args():
    sig = inspect.signature(BusinessColumn.__init__)
    params = list(sig.parameters.keys())



def test_model::business::calculatedbusinesscolumn_is_not_abstract():
    assert not inspect.isabstract(model::business::CalculatedBusinessColumn)


def test_model::business::calculatedbusinesscolumn_constructor_exists():
    assert callable(model::business::CalculatedBusinessColumn.__init__)


def test_model::business::calculatedbusinesscolumn_constructor_args():
    sig = inspect.signature(model::business::CalculatedBusinessColumn.__init__)
    params = list(sig.parameters.keys())



def test_model::business::simplebusinesscolumn_is_not_abstract():
    assert not inspect.isabstract(model::business::SimpleBusinessColumn)


def test_model::business::simplebusinesscolumn_constructor_exists():
    assert callable(model::business::SimpleBusinessColumn.__init__)


def test_model::business::simplebusinesscolumn_constructor_args():
    sig = inspect.signature(model::business::SimpleBusinessColumn.__init__)
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



def test_model::modelobject_is_not_abstract():
    assert not inspect.isabstract(model::ModelObject)


def test_model::modelobject_constructor_exists():
    assert callable(model::ModelObject.__init__)


def test_model::modelobject_constructor_args():
    sig = inspect.signature(model::ModelObject.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "uniqueName" in params, "Missing parameter 'uniqueName'"

def test_model::modelobject_has_description():
    assert hasattr(model::ModelObject, "description")
    descriptor = None
    for klass in model::ModelObject.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_model::modelobject_has_name():
    assert hasattr(model::ModelObject, "name")
    descriptor = None
    for klass in model::ModelObject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model::modelobject_has_id():
    assert hasattr(model::ModelObject, "id")
    descriptor = None
    for klass in model::ModelObject.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_model::modelobject_has_uniqueName():
    assert hasattr(model::ModelObject, "uniqueName")
    descriptor = None
    for klass in model::ModelObject.__mro__:
        if "uniqueName" in klass.__dict__:
            descriptor = klass.__dict__["uniqueName"]
            break
    assert isinstance(descriptor, property)



def test_model::modelpropertymapentry_is_not_abstract():
    assert not inspect.isabstract(model::ModelPropertyMapEntry)


def test_model::modelpropertymapentry_constructor_exists():
    assert callable(model::ModelPropertyMapEntry.__init__)


def test_model::modelpropertymapentry_constructor_args():
    sig = inspect.signature(model::ModelPropertyMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_model::modelpropertymapentry_has_key():
    assert hasattr(model::ModelPropertyMapEntry, "key")
    descriptor = None
    for klass in model::ModelPropertyMapEntry.__mro__:
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



def test_physical::model::model_is_not_abstract():
    assert not inspect.isabstract(physical::model::Model)


def test_physical::model::model_constructor_exists():
    assert callable(physical::model::Model.__init__)


def test_physical::model::model_constructor_args():
    sig = inspect.signature(physical::model::Model.__init__)
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



def test_model::physical::physicaltable_is_not_abstract():
    assert not inspect.isabstract(model::physical::PhysicalTable)


def test_model::physical::physicaltable_constructor_exists():
    assert callable(model::physical::PhysicalTable.__init__)


def test_model::physical::physicaltable_constructor_args():
    sig = inspect.signature(model::physical::PhysicalTable.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "type" in params, "Missing parameter 'type'"

def test_model::physical::physicaltable_has_comment():
    assert hasattr(model::physical::PhysicalTable, "comment")
    descriptor = None
    for klass in model::physical::PhysicalTable.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_model::physical::physicaltable_has_type():
    assert hasattr(model::physical::PhysicalTable, "type")
    descriptor = None
    for klass in model::physical::PhysicalTable.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_model::olap::virtualcubedimension_is_not_abstract():
    assert not inspect.isabstract(model::olap::VirtualCubeDimension)


def test_model::olap::virtualcubedimension_constructor_exists():
    assert callable(model::olap::VirtualCubeDimension.__init__)


def test_model::olap::virtualcubedimension_constructor_args():
    sig = inspect.signature(model::olap::VirtualCubeDimension.__init__)
    params = list(sig.parameters.keys())



def test_model::olap::virtualcube_is_not_abstract():
    assert not inspect.isabstract(model::olap::VirtualCube)


def test_model::olap::virtualcube_constructor_exists():
    assert callable(model::olap::VirtualCube.__init__)


def test_model::olap::virtualcube_constructor_args():
    sig = inspect.signature(model::olap::VirtualCube.__init__)
    params = list(sig.parameters.keys())



def test_model::business::businesscolumn_is_not_abstract():
    assert not inspect.isabstract(model::business::BusinessColumn)


def test_model::business::businesscolumn_constructor_exists():
    assert callable(model::business::BusinessColumn.__init__)


def test_model::business::businesscolumn_constructor_args():
    sig = inspect.signature(model::business::BusinessColumn.__init__)
    params = list(sig.parameters.keys())



def test_model::physical::physicalforeignkey_is_not_abstract():
    assert not inspect.isabstract(model::physical::PhysicalForeignKey)


def test_model::physical::physicalforeignkey_constructor_exists():
    assert callable(model::physical::PhysicalForeignKey.__init__)


def test_model::physical::physicalforeignkey_constructor_args():
    sig = inspect.signature(model::physical::PhysicalForeignKey.__init__)
    params = list(sig.parameters.keys())
    assert "destinationName" in params, "Missing parameter 'destinationName'"
    assert "sourceName" in params, "Missing parameter 'sourceName'"

def test_model::physical::physicalforeignkey_has_destinationName():
    assert hasattr(model::physical::PhysicalForeignKey, "destinationName")
    descriptor = None
    for klass in model::physical::PhysicalForeignKey.__mro__:
        if "destinationName" in klass.__dict__:
            descriptor = klass.__dict__["destinationName"]
            break
    assert isinstance(descriptor, property)

def test_model::physical::physicalforeignkey_has_sourceName():
    assert hasattr(model::physical::PhysicalForeignKey, "sourceName")
    descriptor = None
    for klass in model::physical::PhysicalForeignKey.__mro__:
        if "sourceName" in klass.__dict__:
            descriptor = klass.__dict__["sourceName"]
            break
    assert isinstance(descriptor, property)



def test_model::physical::physicalcolumn_is_not_abstract():
    assert not inspect.isabstract(model::physical::PhysicalColumn)


def test_model::physical::physicalcolumn_constructor_exists():
    assert callable(model::physical::PhysicalColumn.__init__)


def test_model::physical::physicalcolumn_constructor_args():
    sig = inspect.signature(model::physical::PhysicalColumn.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"
    assert "decimalDigits" in params, "Missing parameter 'decimalDigits'"
    assert "size" in params, "Missing parameter 'size'"
    assert "octectLength" in params, "Missing parameter 'octectLength'"
    assert "nullable" in params, "Missing parameter 'nullable'"
    assert "typeName" in params, "Missing parameter 'typeName'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "radix" in params, "Missing parameter 'radix'"
    assert "dataType" in params, "Missing parameter 'dataType'"

def test_model::physical::physicalcolumn_has_position():
    assert hasattr(model::physical::PhysicalColumn, "position")
    descriptor = None
    for klass in model::physical::PhysicalColumn.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_model::physical::physicalcolumn_has_decimalDigits():
    assert hasattr(model::physical::PhysicalColumn, "decimalDigits")
    descriptor = None
    for klass in model::physical::PhysicalColumn.__mro__:
        if "decimalDigits" in klass.__dict__:
            descriptor = klass.__dict__["decimalDigits"]
            break
    assert isinstance(descriptor, property)

def test_model::physical::physicalcolumn_has_size():
    assert hasattr(model::physical::PhysicalColumn, "size")
    descriptor = None
    for klass in model::physical::PhysicalColumn.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_model::physical::physicalcolumn_has_octectLength():
    assert hasattr(model::physical::PhysicalColumn, "octectLength")
    descriptor = None
    for klass in model::physical::PhysicalColumn.__mro__:
        if "octectLength" in klass.__dict__:
            descriptor = klass.__dict__["octectLength"]
            break
    assert isinstance(descriptor, property)

def test_model::physical::physicalcolumn_has_nullable():
    assert hasattr(model::physical::PhysicalColumn, "nullable")
    descriptor = None
    for klass in model::physical::PhysicalColumn.__mro__:
        if "nullable" in klass.__dict__:
            descriptor = klass.__dict__["nullable"]
            break
    assert isinstance(descriptor, property)

def test_model::physical::physicalcolumn_has_typeName():
    assert hasattr(model::physical::PhysicalColumn, "typeName")
    descriptor = None
    for klass in model::physical::PhysicalColumn.__mro__:
        if "typeName" in klass.__dict__:
            descriptor = klass.__dict__["typeName"]
            break
    assert isinstance(descriptor, property)

def test_model::physical::physicalcolumn_has_comment():
    assert hasattr(model::physical::PhysicalColumn, "comment")
    descriptor = None
    for klass in model::physical::PhysicalColumn.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_model::physical::physicalcolumn_has_defaultValue():
    assert hasattr(model::physical::PhysicalColumn, "defaultValue")
    descriptor = None
    for klass in model::physical::PhysicalColumn.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_model::physical::physicalcolumn_has_radix():
    assert hasattr(model::physical::PhysicalColumn, "radix")
    descriptor = None
    for klass in model::physical::PhysicalColumn.__mro__:
        if "radix" in klass.__dict__:
            descriptor = klass.__dict__["radix"]
            break
    assert isinstance(descriptor, property)

def test_model::physical::physicalcolumn_has_dataType():
    assert hasattr(model::physical::PhysicalColumn, "dataType")
    descriptor = None
    for klass in model::physical::PhysicalColumn.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
            break
    assert isinstance(descriptor, property)



def test_model::olap::cube_is_not_abstract():
    assert not inspect.isabstract(model::olap::Cube)


def test_model::olap::cube_constructor_exists():
    assert callable(model::olap::Cube.__init__)


def test_model::olap::cube_constructor_args():
    sig = inspect.signature(model::olap::Cube.__init__)
    params = list(sig.parameters.keys())



def test_model::business::businesscolumnset_is_not_abstract():
    assert not inspect.isabstract(model::business::BusinessColumnSet)


def test_model::business::businesscolumnset_constructor_exists():
    assert callable(model::business::BusinessColumnSet.__init__)


def test_model::business::businesscolumnset_constructor_args():
    sig = inspect.signature(model::business::BusinessColumnSet.__init__)
    params = list(sig.parameters.keys())



def test_model::olap::namedset_is_not_abstract():
    assert not inspect.isabstract(model::olap::NamedSet)


def test_model::olap::namedset_constructor_exists():
    assert callable(model::olap::NamedSet.__init__)


def test_model::olap::namedset_constructor_args():
    sig = inspect.signature(model::olap::NamedSet.__init__)
    params = list(sig.parameters.keys())



def test_model::physical::physicalprimarykey_is_not_abstract():
    assert not inspect.isabstract(model::physical::PhysicalPrimaryKey)


def test_model::physical::physicalprimarykey_constructor_exists():
    assert callable(model::physical::PhysicalPrimaryKey.__init__)


def test_model::physical::physicalprimarykey_constructor_args():
    sig = inspect.signature(model::physical::PhysicalPrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_model::business::businessidentifier_is_not_abstract():
    assert not inspect.isabstract(model::business::BusinessIdentifier)


def test_model::business::businessidentifier_constructor_exists():
    assert callable(model::business::BusinessIdentifier.__init__)


def test_model::business::businessidentifier_constructor_args():
    sig = inspect.signature(model::business::BusinessIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_model::business::businessviewinnerjoinrelationship_is_not_abstract():
    assert not inspect.isabstract(model::business::BusinessViewInnerJoinRelationship)


def test_model::business::businessviewinnerjoinrelationship_constructor_exists():
    assert callable(model::business::BusinessViewInnerJoinRelationship.__init__)


def test_model::business::businessviewinnerjoinrelationship_constructor_args():
    sig = inspect.signature(model::business::BusinessViewInnerJoinRelationship.__init__)
    params = list(sig.parameters.keys())



def test_model::business::businessrelationship_is_not_abstract():
    assert not inspect.isabstract(model::business::BusinessRelationship)


def test_model::business::businessrelationship_constructor_exists():
    assert callable(model::business::BusinessRelationship.__init__)


def test_model::business::businessrelationship_constructor_args():
    sig = inspect.signature(model::business::BusinessRelationship.__init__)
    params = list(sig.parameters.keys())



def test_model::olap::level_is_not_abstract():
    assert not inspect.isabstract(model::olap::Level)


def test_model::olap::level_constructor_exists():
    assert callable(model::olap::Level.__init__)


def test_model::olap::level_constructor_args():
    sig = inspect.signature(model::olap::Level.__init__)
    params = list(sig.parameters.keys())



def test_model::physical::physicalmodel_is_not_abstract():
    assert not inspect.isabstract(model::physical::PhysicalModel)


def test_model::physical::physicalmodel_constructor_exists():
    assert callable(model::physical::PhysicalModel.__init__)


def test_model::physical::physicalmodel_constructor_args():
    sig = inspect.signature(model::physical::PhysicalModel.__init__)
    params = list(sig.parameters.keys())
    assert "databaseName" in params, "Missing parameter 'databaseName'"
    assert "schema" in params, "Missing parameter 'schema'"
    assert "catalog" in params, "Missing parameter 'catalog'"
    assert "databaseVersion" in params, "Missing parameter 'databaseVersion'"

def test_model::physical::physicalmodel_has_databaseName():
    assert hasattr(model::physical::PhysicalModel, "databaseName")
    descriptor = None
    for klass in model::physical::PhysicalModel.__mro__:
        if "databaseName" in klass.__dict__:
            descriptor = klass.__dict__["databaseName"]
            break
    assert isinstance(descriptor, property)

def test_model::physical::physicalmodel_has_schema():
    assert hasattr(model::physical::PhysicalModel, "schema")
    descriptor = None
    for klass in model::physical::PhysicalModel.__mro__:
        if "schema" in klass.__dict__:
            descriptor = klass.__dict__["schema"]
            break
    assert isinstance(descriptor, property)

def test_model::physical::physicalmodel_has_catalog():
    assert hasattr(model::physical::PhysicalModel, "catalog")
    descriptor = None
    for klass in model::physical::PhysicalModel.__mro__:
        if "catalog" in klass.__dict__:
            descriptor = klass.__dict__["catalog"]
            break
    assert isinstance(descriptor, property)

def test_model::physical::physicalmodel_has_databaseVersion():
    assert hasattr(model::physical::PhysicalModel, "databaseVersion")
    descriptor = None
    for klass in model::physical::PhysicalModel.__mro__:
        if "databaseVersion" in klass.__dict__:
            descriptor = klass.__dict__["databaseVersion"]
            break
    assert isinstance(descriptor, property)



def test_model::olap::measure_is_not_abstract():
    assert not inspect.isabstract(model::olap::Measure)


def test_model::olap::measure_constructor_exists():
    assert callable(model::olap::Measure.__init__)


def test_model::olap::measure_constructor_args():
    sig = inspect.signature(model::olap::Measure.__init__)
    params = list(sig.parameters.keys())



def test_model::olap::olapmodel_is_not_abstract():
    assert not inspect.isabstract(model::olap::OlapModel)


def test_model::olap::olapmodel_constructor_exists():
    assert callable(model::olap::OlapModel.__init__)


def test_model::olap::olapmodel_constructor_args():
    sig = inspect.signature(model::olap::OlapModel.__init__)
    params = list(sig.parameters.keys())



def test_model::olap::virtualcubemeasure_is_not_abstract():
    assert not inspect.isabstract(model::olap::VirtualCubeMeasure)


def test_model::olap::virtualcubemeasure_constructor_exists():
    assert callable(model::olap::VirtualCubeMeasure.__init__)


def test_model::olap::virtualcubemeasure_constructor_args():
    sig = inspect.signature(model::olap::VirtualCubeMeasure.__init__)
    params = list(sig.parameters.keys())



def test_model::business::businessmodel_is_not_abstract():
    assert not inspect.isabstract(model::business::BusinessModel)


def test_model::business::businessmodel_constructor_exists():
    assert callable(model::business::BusinessModel.__init__)


def test_model::business::businessmodel_constructor_args():
    sig = inspect.signature(model::business::BusinessModel.__init__)
    params = list(sig.parameters.keys())



def test_model::business::businessdomain_is_not_abstract():
    assert not inspect.isabstract(model::business::BusinessDomain)


def test_model::business::businessdomain_constructor_exists():
    assert callable(model::business::BusinessDomain.__init__)


def test_model::business::businessdomain_constructor_args():
    sig = inspect.signature(model::business::BusinessDomain.__init__)
    params = list(sig.parameters.keys())



def test_model::olap::calculatedmember_is_not_abstract():
    assert not inspect.isabstract(model::olap::CalculatedMember)


def test_model::olap::calculatedmember_constructor_exists():
    assert callable(model::olap::CalculatedMember.__init__)


def test_model::olap::calculatedmember_constructor_args():
    sig = inspect.signature(model::olap::CalculatedMember.__init__)
    params = list(sig.parameters.keys())



def test_model::olap::hierarchy_is_not_abstract():
    assert not inspect.isabstract(model::olap::Hierarchy)


def test_model::olap::hierarchy_constructor_exists():
    assert callable(model::olap::Hierarchy.__init__)


def test_model::olap::hierarchy_constructor_args():
    sig = inspect.signature(model::olap::Hierarchy.__init__)
    params = list(sig.parameters.keys())



def test_model::olap::dimension_is_not_abstract():
    assert not inspect.isabstract(model::olap::Dimension)


def test_model::olap::dimension_constructor_exists():
    assert callable(model::olap::Dimension.__init__)


def test_model::olap::dimension_constructor_args():
    sig = inspect.signature(model::olap::Dimension.__init__)
    params = list(sig.parameters.keys())



def test_model::model_is_not_abstract():
    assert not inspect.isabstract(model::Model)


def test_model::model_constructor_exists():
    assert callable(model::Model.__init__)


def test_model::model_constructor_args():
    sig = inspect.signature(model::Model.__init__)
    params = list(sig.parameters.keys())



def test_model::modelproperty_is_not_abstract():
    assert not inspect.isabstract(model::ModelProperty)


def test_model::modelproperty_constructor_exists():
    assert callable(model::ModelProperty.__init__)


def test_model::modelproperty_constructor_args():
    sig = inspect.signature(model::ModelProperty.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_model::modelproperty_has_value():
    assert hasattr(model::ModelProperty, "value")
    descriptor = None
    for klass in model::ModelProperty.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_model::modelpropertytype_is_not_abstract():
    assert not inspect.isabstract(model::ModelPropertyType)


def test_model::modelpropertytype_constructor_exists():
    assert callable(model::ModelPropertyType.__init__)


def test_model::modelpropertytype_constructor_args():
    sig = inspect.signature(model::ModelPropertyType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "admissibleValues" in params, "Missing parameter 'admissibleValues'"

def test_model::modelpropertytype_has_id():
    assert hasattr(model::ModelPropertyType, "id")
    descriptor = None
    for klass in model::ModelPropertyType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_model::modelpropertytype_has_name():
    assert hasattr(model::ModelPropertyType, "name")
    descriptor = None
    for klass in model::ModelPropertyType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model::modelpropertytype_has_description():
    assert hasattr(model::ModelPropertyType, "description")
    descriptor = None
    for klass in model::ModelPropertyType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_model::modelpropertytype_has_defaultValue():
    assert hasattr(model::ModelPropertyType, "defaultValue")
    descriptor = None
    for klass in model::ModelPropertyType.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_model::modelpropertytype_has_admissibleValues():
    assert hasattr(model::ModelPropertyType, "admissibleValues")
    descriptor = None
    for klass in model::ModelPropertyType.__mro__:
        if "admissibleValues" in klass.__dict__:
            descriptor = klass.__dict__["admissibleValues"]
            break
    assert isinstance(descriptor, property)



def test_model::modelpropertycategory_is_not_abstract():
    assert not inspect.isabstract(model::ModelPropertyCategory)


def test_model::modelpropertycategory_constructor_exists():
    assert callable(model::ModelPropertyCategory.__init__)


def test_model::modelpropertycategory_constructor_args():
    sig = inspect.signature(model::ModelPropertyCategory.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_model::modelpropertycategory_has_name():
    assert hasattr(model::ModelPropertyCategory, "name")
    descriptor = None
    for klass in model::ModelPropertyCategory.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model::modelpropertycategory_has_description():
    assert hasattr(model::ModelPropertyCategory, "description")
    descriptor = None
    for klass in model::ModelPropertyCategory.__mro__:
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
model::analytical::AnalyticalModel_strategy = st.builds(
    model::analytical::AnalyticalModel,
)
model::behavioural::BehaviouralModel_strategy = st.builds(
    model::behavioural::BehaviouralModel,
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
olap::model::Model_strategy = st.builds(
    olap::model::Model,
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
business::model::Model_strategy = st.builds(
    business::model::Model,
)
model::business::BusinessView_strategy = st.builds(
    model::business::BusinessView,
)
model::business::BusinessTable_strategy = st.builds(
    model::business::BusinessTable,
)
BusinessColumn_strategy = st.builds(
    BusinessColumn,
)
model::business::CalculatedBusinessColumn_strategy = st.builds(
    model::business::CalculatedBusinessColumn,
)
model::business::SimpleBusinessColumn_strategy = st.builds(
    model::business::SimpleBusinessColumn,
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
model::ModelObject_strategy = st.builds(
    model::ModelObject,
    description=
        safe_text,
    name=
        safe_text,
    id=
        safe_text,
    uniqueName=
        safe_text
)
model::ModelPropertyMapEntry_strategy = st.builds(
    model::ModelPropertyMapEntry,
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
physical::model::Model_strategy = st.builds(
    physical::model::Model,
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
model::physical::PhysicalTable_strategy = st.builds(
    model::physical::PhysicalTable,
    comment=
        safe_text,
    type=
        safe_text
)
model::olap::VirtualCubeDimension_strategy = st.builds(
    model::olap::VirtualCubeDimension,
)
model::olap::VirtualCube_strategy = st.builds(
    model::olap::VirtualCube,
)
model::business::BusinessColumn_strategy = st.builds(
    model::business::BusinessColumn,
)
model::physical::PhysicalForeignKey_strategy = st.builds(
    model::physical::PhysicalForeignKey,
    destinationName=
        safe_text,
    sourceName=
        safe_text
)
model::physical::PhysicalColumn_strategy = st.builds(
    model::physical::PhysicalColumn,
    position=
        st.integers(),
    decimalDigits=
        st.integers(),
    size=
        st.integers(),
    octectLength=
        st.integers(),
    nullable=
        st.booleans(),
    typeName=
        safe_text,
    comment=
        safe_text,
    defaultValue=
        safe_text,
    radix=
        st.integers(),
    dataType=
        safe_text
)
model::olap::Cube_strategy = st.builds(
    model::olap::Cube,
)
model::business::BusinessColumnSet_strategy = st.builds(
    model::business::BusinessColumnSet,
)
model::olap::NamedSet_strategy = st.builds(
    model::olap::NamedSet,
)
model::physical::PhysicalPrimaryKey_strategy = st.builds(
    model::physical::PhysicalPrimaryKey,
)
model::business::BusinessIdentifier_strategy = st.builds(
    model::business::BusinessIdentifier,
)
model::business::BusinessViewInnerJoinRelationship_strategy = st.builds(
    model::business::BusinessViewInnerJoinRelationship,
)
model::business::BusinessRelationship_strategy = st.builds(
    model::business::BusinessRelationship,
)
model::olap::Level_strategy = st.builds(
    model::olap::Level,
)
model::physical::PhysicalModel_strategy = st.builds(
    model::physical::PhysicalModel,
    databaseName=
        safe_text,
    schema=
        safe_text,
    catalog=
        safe_text,
    databaseVersion=
        safe_text
)
model::olap::Measure_strategy = st.builds(
    model::olap::Measure,
)
model::olap::OlapModel_strategy = st.builds(
    model::olap::OlapModel,
)
model::olap::VirtualCubeMeasure_strategy = st.builds(
    model::olap::VirtualCubeMeasure,
)
model::business::BusinessModel_strategy = st.builds(
    model::business::BusinessModel,
)
model::business::BusinessDomain_strategy = st.builds(
    model::business::BusinessDomain,
)
model::olap::CalculatedMember_strategy = st.builds(
    model::olap::CalculatedMember,
)
model::olap::Hierarchy_strategy = st.builds(
    model::olap::Hierarchy,
)
model::olap::Dimension_strategy = st.builds(
    model::olap::Dimension,
)
model::Model_strategy = st.builds(
    model::Model,
)
model::ModelProperty_strategy = st.builds(
    model::ModelProperty,
    value=
        safe_text
)
model::ModelPropertyType_strategy = st.builds(
    model::ModelPropertyType,
    id=
        safe_text,
    name=
        safe_text,
    description=
        safe_text,
    defaultValue=
        safe_text,
    admissibleValues=
        safe_text
)
model::ModelPropertyCategory_strategy = st.builds(
    model::ModelPropertyCategory,
    name=
        safe_text,
    description=
        safe_text
)

@given(instance=model::analytical::AnalyticalModel_strategy)
@settings(max_examples=50)
def test_model::analytical::analyticalmodel_instantiation(instance):
    assert isinstance(instance, model::analytical::AnalyticalModel)

@given(instance=model::behavioural::BehaviouralModel_strategy)
@settings(max_examples=50)
def test_model::behavioural::behaviouralmodel_instantiation(instance):
    assert isinstance(instance, model::behavioural::BehaviouralModel)

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

@given(instance=olap::model::Model_strategy)
@settings(max_examples=50)
def test_olap::model::model_instantiation(instance):
    assert isinstance(instance, olap::model::Model)

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

@given(instance=business::model::Model_strategy)
@settings(max_examples=50)
def test_business::model::model_instantiation(instance):
    assert isinstance(instance, business::model::Model)

@given(instance=model::business::BusinessView_strategy)
@settings(max_examples=50)
def test_model::business::businessview_instantiation(instance):
    assert isinstance(instance, model::business::BusinessView)

@given(instance=model::business::BusinessTable_strategy)
@settings(max_examples=50)
def test_model::business::businesstable_instantiation(instance):
    assert isinstance(instance, model::business::BusinessTable)

@given(instance=BusinessColumn_strategy)
@settings(max_examples=50)
def test_businesscolumn_instantiation(instance):
    assert isinstance(instance, BusinessColumn)

@given(instance=model::business::CalculatedBusinessColumn_strategy)
@settings(max_examples=50)
def test_model::business::calculatedbusinesscolumn_instantiation(instance):
    assert isinstance(instance, model::business::CalculatedBusinessColumn)

@given(instance=model::business::SimpleBusinessColumn_strategy)
@settings(max_examples=50)
def test_model::business::simplebusinesscolumn_instantiation(instance):
    assert isinstance(instance, model::business::SimpleBusinessColumn)

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

@given(instance=model::ModelObject_strategy)
@settings(max_examples=50)
def test_model::modelobject_instantiation(instance):
    assert isinstance(instance, model::ModelObject)

@given(instance=model::ModelObject_strategy)
def test_model::modelobject_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=model::ModelObject_strategy)
def test_model::modelobject_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=model::ModelObject_strategy)
def test_model::modelobject_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::ModelObject_strategy)
def test_model::modelobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::ModelObject_strategy)
def test_model::modelobject_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=model::ModelObject_strategy)
def test_model::modelobject_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=model::ModelObject_strategy)
def test_model::modelobject_uniqueName_type(instance):
    assert isinstance(instance.uniqueName, str)


@given(instance=model::ModelObject_strategy)
def test_model::modelobject_uniqueName_setter(instance):
    original = instance.uniqueName
    instance.uniqueName = original
    assert instance.uniqueName == original

@given(instance=model::ModelPropertyMapEntry_strategy)
@settings(max_examples=50)
def test_model::modelpropertymapentry_instantiation(instance):
    assert isinstance(instance, model::ModelPropertyMapEntry)

@given(instance=model::ModelPropertyMapEntry_strategy)
def test_model::modelpropertymapentry_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=model::ModelPropertyMapEntry_strategy)
def test_model::modelpropertymapentry_key_setter(instance):
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

@given(instance=physical::model::Model_strategy)
@settings(max_examples=50)
def test_physical::model::model_instantiation(instance):
    assert isinstance(instance, physical::model::Model)

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

@given(instance=model::physical::PhysicalTable_strategy)
@settings(max_examples=50)
def test_model::physical::physicaltable_instantiation(instance):
    assert isinstance(instance, model::physical::PhysicalTable)

@given(instance=model::physical::PhysicalTable_strategy)
def test_model::physical::physicaltable_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=model::physical::PhysicalTable_strategy)
def test_model::physical::physicaltable_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=model::physical::PhysicalTable_strategy)
def test_model::physical::physicaltable_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=model::physical::PhysicalTable_strategy)
def test_model::physical::physicaltable_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=model::olap::VirtualCubeDimension_strategy)
@settings(max_examples=50)
def test_model::olap::virtualcubedimension_instantiation(instance):
    assert isinstance(instance, model::olap::VirtualCubeDimension)

@given(instance=model::olap::VirtualCube_strategy)
@settings(max_examples=50)
def test_model::olap::virtualcube_instantiation(instance):
    assert isinstance(instance, model::olap::VirtualCube)

@given(instance=model::business::BusinessColumn_strategy)
@settings(max_examples=50)
def test_model::business::businesscolumn_instantiation(instance):
    assert isinstance(instance, model::business::BusinessColumn)

@given(instance=model::physical::PhysicalForeignKey_strategy)
@settings(max_examples=50)
def test_model::physical::physicalforeignkey_instantiation(instance):
    assert isinstance(instance, model::physical::PhysicalForeignKey)

@given(instance=model::physical::PhysicalForeignKey_strategy)
def test_model::physical::physicalforeignkey_destinationName_type(instance):
    assert isinstance(instance.destinationName, str)


@given(instance=model::physical::PhysicalForeignKey_strategy)
def test_model::physical::physicalforeignkey_destinationName_setter(instance):
    original = instance.destinationName
    instance.destinationName = original
    assert instance.destinationName == original

@given(instance=model::physical::PhysicalForeignKey_strategy)
def test_model::physical::physicalforeignkey_sourceName_type(instance):
    assert isinstance(instance.sourceName, str)


@given(instance=model::physical::PhysicalForeignKey_strategy)
def test_model::physical::physicalforeignkey_sourceName_setter(instance):
    original = instance.sourceName
    instance.sourceName = original
    assert instance.sourceName == original

@given(instance=model::physical::PhysicalColumn_strategy)
@settings(max_examples=50)
def test_model::physical::physicalcolumn_instantiation(instance):
    assert isinstance(instance, model::physical::PhysicalColumn)

@given(instance=model::physical::PhysicalColumn_strategy)
def test_model::physical::physicalcolumn_position_type(instance):
    assert isinstance(instance.position, int)


@given(instance=model::physical::PhysicalColumn_strategy)
def test_model::physical::physicalcolumn_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=model::physical::PhysicalColumn_strategy)
def test_model::physical::physicalcolumn_decimalDigits_type(instance):
    assert isinstance(instance.decimalDigits, int)


@given(instance=model::physical::PhysicalColumn_strategy)
def test_model::physical::physicalcolumn_decimalDigits_setter(instance):
    original = instance.decimalDigits
    instance.decimalDigits = original
    assert instance.decimalDigits == original

@given(instance=model::physical::PhysicalColumn_strategy)
def test_model::physical::physicalcolumn_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=model::physical::PhysicalColumn_strategy)
def test_model::physical::physicalcolumn_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=model::physical::PhysicalColumn_strategy)
def test_model::physical::physicalcolumn_octectLength_type(instance):
    assert isinstance(instance.octectLength, int)


@given(instance=model::physical::PhysicalColumn_strategy)
def test_model::physical::physicalcolumn_octectLength_setter(instance):
    original = instance.octectLength
    instance.octectLength = original
    assert instance.octectLength == original

@given(instance=model::physical::PhysicalColumn_strategy)
def test_model::physical::physicalcolumn_nullable_type(instance):
    assert isinstance(instance.nullable, bool)


@given(instance=model::physical::PhysicalColumn_strategy)
def test_model::physical::physicalcolumn_nullable_setter(instance):
    original = instance.nullable
    instance.nullable = original
    assert instance.nullable == original

@given(instance=model::physical::PhysicalColumn_strategy)
def test_model::physical::physicalcolumn_typeName_type(instance):
    assert isinstance(instance.typeName, str)


@given(instance=model::physical::PhysicalColumn_strategy)
def test_model::physical::physicalcolumn_typeName_setter(instance):
    original = instance.typeName
    instance.typeName = original
    assert instance.typeName == original

@given(instance=model::physical::PhysicalColumn_strategy)
def test_model::physical::physicalcolumn_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=model::physical::PhysicalColumn_strategy)
def test_model::physical::physicalcolumn_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=model::physical::PhysicalColumn_strategy)
def test_model::physical::physicalcolumn_defaultValue_type(instance):
    assert isinstance(instance.defaultValue, str)


@given(instance=model::physical::PhysicalColumn_strategy)
def test_model::physical::physicalcolumn_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=model::physical::PhysicalColumn_strategy)
def test_model::physical::physicalcolumn_radix_type(instance):
    assert isinstance(instance.radix, int)


@given(instance=model::physical::PhysicalColumn_strategy)
def test_model::physical::physicalcolumn_radix_setter(instance):
    original = instance.radix
    instance.radix = original
    assert instance.radix == original

@given(instance=model::physical::PhysicalColumn_strategy)
def test_model::physical::physicalcolumn_dataType_type(instance):
    assert isinstance(instance.dataType, str)


@given(instance=model::physical::PhysicalColumn_strategy)
def test_model::physical::physicalcolumn_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original

@given(instance=model::olap::Cube_strategy)
@settings(max_examples=50)
def test_model::olap::cube_instantiation(instance):
    assert isinstance(instance, model::olap::Cube)

@given(instance=model::business::BusinessColumnSet_strategy)
@settings(max_examples=50)
def test_model::business::businesscolumnset_instantiation(instance):
    assert isinstance(instance, model::business::BusinessColumnSet)

@given(instance=model::olap::NamedSet_strategy)
@settings(max_examples=50)
def test_model::olap::namedset_instantiation(instance):
    assert isinstance(instance, model::olap::NamedSet)

@given(instance=model::physical::PhysicalPrimaryKey_strategy)
@settings(max_examples=50)
def test_model::physical::physicalprimarykey_instantiation(instance):
    assert isinstance(instance, model::physical::PhysicalPrimaryKey)

@given(instance=model::business::BusinessIdentifier_strategy)
@settings(max_examples=50)
def test_model::business::businessidentifier_instantiation(instance):
    assert isinstance(instance, model::business::BusinessIdentifier)

@given(instance=model::business::BusinessViewInnerJoinRelationship_strategy)
@settings(max_examples=50)
def test_model::business::businessviewinnerjoinrelationship_instantiation(instance):
    assert isinstance(instance, model::business::BusinessViewInnerJoinRelationship)

@given(instance=model::business::BusinessRelationship_strategy)
@settings(max_examples=50)
def test_model::business::businessrelationship_instantiation(instance):
    assert isinstance(instance, model::business::BusinessRelationship)

@given(instance=model::olap::Level_strategy)
@settings(max_examples=50)
def test_model::olap::level_instantiation(instance):
    assert isinstance(instance, model::olap::Level)

@given(instance=model::physical::PhysicalModel_strategy)
@settings(max_examples=50)
def test_model::physical::physicalmodel_instantiation(instance):
    assert isinstance(instance, model::physical::PhysicalModel)

@given(instance=model::physical::PhysicalModel_strategy)
def test_model::physical::physicalmodel_databaseName_type(instance):
    assert isinstance(instance.databaseName, str)


@given(instance=model::physical::PhysicalModel_strategy)
def test_model::physical::physicalmodel_databaseName_setter(instance):
    original = instance.databaseName
    instance.databaseName = original
    assert instance.databaseName == original

@given(instance=model::physical::PhysicalModel_strategy)
def test_model::physical::physicalmodel_schema_type(instance):
    assert isinstance(instance.schema, str)


@given(instance=model::physical::PhysicalModel_strategy)
def test_model::physical::physicalmodel_schema_setter(instance):
    original = instance.schema
    instance.schema = original
    assert instance.schema == original

@given(instance=model::physical::PhysicalModel_strategy)
def test_model::physical::physicalmodel_catalog_type(instance):
    assert isinstance(instance.catalog, str)


@given(instance=model::physical::PhysicalModel_strategy)
def test_model::physical::physicalmodel_catalog_setter(instance):
    original = instance.catalog
    instance.catalog = original
    assert instance.catalog == original

@given(instance=model::physical::PhysicalModel_strategy)
def test_model::physical::physicalmodel_databaseVersion_type(instance):
    assert isinstance(instance.databaseVersion, str)


@given(instance=model::physical::PhysicalModel_strategy)
def test_model::physical::physicalmodel_databaseVersion_setter(instance):
    original = instance.databaseVersion
    instance.databaseVersion = original
    assert instance.databaseVersion == original

@given(instance=model::olap::Measure_strategy)
@settings(max_examples=50)
def test_model::olap::measure_instantiation(instance):
    assert isinstance(instance, model::olap::Measure)

@given(instance=model::olap::OlapModel_strategy)
@settings(max_examples=50)
def test_model::olap::olapmodel_instantiation(instance):
    assert isinstance(instance, model::olap::OlapModel)

@given(instance=model::olap::VirtualCubeMeasure_strategy)
@settings(max_examples=50)
def test_model::olap::virtualcubemeasure_instantiation(instance):
    assert isinstance(instance, model::olap::VirtualCubeMeasure)

@given(instance=model::business::BusinessModel_strategy)
@settings(max_examples=50)
def test_model::business::businessmodel_instantiation(instance):
    assert isinstance(instance, model::business::BusinessModel)

@given(instance=model::business::BusinessDomain_strategy)
@settings(max_examples=50)
def test_model::business::businessdomain_instantiation(instance):
    assert isinstance(instance, model::business::BusinessDomain)

@given(instance=model::olap::CalculatedMember_strategy)
@settings(max_examples=50)
def test_model::olap::calculatedmember_instantiation(instance):
    assert isinstance(instance, model::olap::CalculatedMember)

@given(instance=model::olap::Hierarchy_strategy)
@settings(max_examples=50)
def test_model::olap::hierarchy_instantiation(instance):
    assert isinstance(instance, model::olap::Hierarchy)

@given(instance=model::olap::Dimension_strategy)
@settings(max_examples=50)
def test_model::olap::dimension_instantiation(instance):
    assert isinstance(instance, model::olap::Dimension)

@given(instance=model::Model_strategy)
@settings(max_examples=50)
def test_model::model_instantiation(instance):
    assert isinstance(instance, model::Model)

@given(instance=model::ModelProperty_strategy)
@settings(max_examples=50)
def test_model::modelproperty_instantiation(instance):
    assert isinstance(instance, model::ModelProperty)

@given(instance=model::ModelProperty_strategy)
def test_model::modelproperty_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=model::ModelProperty_strategy)
def test_model::modelproperty_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=model::ModelPropertyType_strategy)
@settings(max_examples=50)
def test_model::modelpropertytype_instantiation(instance):
    assert isinstance(instance, model::ModelPropertyType)

@given(instance=model::ModelPropertyType_strategy)
def test_model::modelpropertytype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=model::ModelPropertyType_strategy)
def test_model::modelpropertytype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=model::ModelPropertyType_strategy)
def test_model::modelpropertytype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::ModelPropertyType_strategy)
def test_model::modelpropertytype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::ModelPropertyType_strategy)
def test_model::modelpropertytype_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=model::ModelPropertyType_strategy)
def test_model::modelpropertytype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=model::ModelPropertyType_strategy)
def test_model::modelpropertytype_defaultValue_type(instance):
    assert isinstance(instance.defaultValue, str)


@given(instance=model::ModelPropertyType_strategy)
def test_model::modelpropertytype_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=model::ModelPropertyType_strategy)
def test_model::modelpropertytype_admissibleValues_type(instance):
    assert isinstance(instance.admissibleValues, str)


@given(instance=model::ModelPropertyType_strategy)
def test_model::modelpropertytype_admissibleValues_setter(instance):
    original = instance.admissibleValues
    instance.admissibleValues = original
    assert instance.admissibleValues == original

@given(instance=model::ModelPropertyCategory_strategy)
@settings(max_examples=50)
def test_model::modelpropertycategory_instantiation(instance):
    assert isinstance(instance, model::ModelPropertyCategory)

@given(instance=model::ModelPropertyCategory_strategy)
def test_model::modelpropertycategory_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::ModelPropertyCategory_strategy)
def test_model::modelpropertycategory_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::ModelPropertyCategory_strategy)
def test_model::modelpropertycategory_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=model::ModelPropertyCategory_strategy)
def test_model::modelpropertycategory_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original
