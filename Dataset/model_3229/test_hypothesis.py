import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    pascal::variable::parameter::section,
    pascal::value::parameter::section,
    pascal::formal::parameter::section,
    pascal::formal::parameter::list,
    abstraction::declaration,
    pascal::bound::specification,
    pascal::unpacked::conformant::array::schema,
    pascal::packed::conformant::array::schema,
    pascal::conformant::array::schema,
    pascal::parameter::type,
    pascal::variant::part,
    pascal::fixed::part,
    pascal::variant,
    pascal::tag::field,
    pascal::abstraction::declaration,
    pascal::variable::section,
    pascal::variable::identifier::list,
    pascal::record::section,
    pascal::abstraction::heading,
    pascal::enumerated::type,
    pascal::subrange::type,
    pascal::pointer::type,
    pascal::structured::type,
    pascal::field::list,
    pascal::index::type,
    pascal::file::type,
    pascal::set::type,
    pascal::record::type,
    pascal::dynamic::array::type,
    pascal::array::type,
    pascal::unpacked::structured::type,
    pascal::case::label::list,
    pascal::case::limb,
    pascal::simple::type,
    pascal::type,
    pascal::type::definition,
    pascal::constant::definition,
    pascal::constant,
    pascal::compound::statement,
    pascal::case::statement,
    pascal::if::statement,
    pascal::for::statement,
    pascal::repeat::statement,
    pascal::while::statement,
    pascal::with::statement,
    pascal::conditional::statement,
    pascal::repetitive::statement,
    pascal::expression::list,
    pascal::any::number,
    pascal::set,
    pascal::number,
    pascal::factor,
    pascal::term,
    pascal::EObject,
    pascal::simple::expression,
    pascal::variable::declaration::part,
    pascal::type::definition::part,
    pascal::var::,
    pascal::expression,
    pascal::variable,
    pascal::goto::statement,
    pascal::function::designator,
    pascal::assignment::statement,
    pascal::structured::statement,
    pascal::simple::statement,
    pascal::label,
    pascal::statement,
    pascal::statement::sequence,
    pascal::statement::part,
    pascal::procedure::and::function::declaration::part,
    pascal::constant::definition::part,
    pascal::label::declaration::part,
    pascal::identifier::list,
    pascal::block,
    pascal::program::heading::block,
    pascal::program,
    pascal::pascal,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pascal::variable::parameter::section_is_not_abstract():
    assert not inspect.isabstract(pascal::variable::parameter::section)


def test_pascal::variable::parameter::section_constructor_exists():
    assert callable(pascal::variable::parameter::section.__init__)


def test_pascal::variable::parameter::section_constructor_args():
    sig = inspect.signature(pascal::variable::parameter::section.__init__)
    params = list(sig.parameters.keys())



def test_pascal::value::parameter::section_is_not_abstract():
    assert not inspect.isabstract(pascal::value::parameter::section)


def test_pascal::value::parameter::section_constructor_exists():
    assert callable(pascal::value::parameter::section.__init__)


def test_pascal::value::parameter::section_constructor_args():
    sig = inspect.signature(pascal::value::parameter::section.__init__)
    params = list(sig.parameters.keys())



def test_pascal::formal::parameter::section_is_not_abstract():
    assert not inspect.isabstract(pascal::formal::parameter::section)


def test_pascal::formal::parameter::section_constructor_exists():
    assert callable(pascal::formal::parameter::section.__init__)


def test_pascal::formal::parameter::section_constructor_args():
    sig = inspect.signature(pascal::formal::parameter::section.__init__)
    params = list(sig.parameters.keys())



def test_pascal::formal::parameter::list_is_not_abstract():
    assert not inspect.isabstract(pascal::formal::parameter::list)


def test_pascal::formal::parameter::list_constructor_exists():
    assert callable(pascal::formal::parameter::list.__init__)


def test_pascal::formal::parameter::list_constructor_args():
    sig = inspect.signature(pascal::formal::parameter::list.__init__)
    params = list(sig.parameters.keys())



def test_abstraction::declaration_is_not_abstract():
    assert not inspect.isabstract(abstraction::declaration)


def test_abstraction::declaration_constructor_exists():
    assert callable(abstraction::declaration.__init__)


def test_abstraction::declaration_constructor_args():
    sig = inspect.signature(abstraction::declaration.__init__)
    params = list(sig.parameters.keys())



def test_pascal::bound::specification_is_not_abstract():
    assert not inspect.isabstract(pascal::bound::specification)


def test_pascal::bound::specification_constructor_exists():
    assert callable(pascal::bound::specification.__init__)


def test_pascal::bound::specification_constructor_args():
    sig = inspect.signature(pascal::bound::specification.__init__)
    params = list(sig.parameters.keys())
    assert "final" in params, "Missing parameter 'final'"
    assert "initial" in params, "Missing parameter 'initial'"
    assert "name" in params, "Missing parameter 'name'"

def test_pascal::bound::specification_has_final():
    assert hasattr(pascal::bound::specification, "final")
    descriptor = None
    for klass in pascal::bound::specification.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)

def test_pascal::bound::specification_has_initial():
    assert hasattr(pascal::bound::specification, "initial")
    descriptor = None
    for klass in pascal::bound::specification.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)

def test_pascal::bound::specification_has_name():
    assert hasattr(pascal::bound::specification, "name")
    descriptor = None
    for klass in pascal::bound::specification.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pascal::unpacked::conformant::array::schema_is_not_abstract():
    assert not inspect.isabstract(pascal::unpacked::conformant::array::schema)


def test_pascal::unpacked::conformant::array::schema_constructor_exists():
    assert callable(pascal::unpacked::conformant::array::schema.__init__)


def test_pascal::unpacked::conformant::array::schema_constructor_args():
    sig = inspect.signature(pascal::unpacked::conformant::array::schema.__init__)
    params = list(sig.parameters.keys())



def test_pascal::packed::conformant::array::schema_is_not_abstract():
    assert not inspect.isabstract(pascal::packed::conformant::array::schema)


def test_pascal::packed::conformant::array::schema_constructor_exists():
    assert callable(pascal::packed::conformant::array::schema.__init__)


def test_pascal::packed::conformant::array::schema_constructor_args():
    sig = inspect.signature(pascal::packed::conformant::array::schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pascal::packed::conformant::array::schema_has_name():
    assert hasattr(pascal::packed::conformant::array::schema, "name")
    descriptor = None
    for klass in pascal::packed::conformant::array::schema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pascal::conformant::array::schema_is_not_abstract():
    assert not inspect.isabstract(pascal::conformant::array::schema)


def test_pascal::conformant::array::schema_constructor_exists():
    assert callable(pascal::conformant::array::schema.__init__)


def test_pascal::conformant::array::schema_constructor_args():
    sig = inspect.signature(pascal::conformant::array::schema.__init__)
    params = list(sig.parameters.keys())



def test_pascal::parameter::type_is_not_abstract():
    assert not inspect.isabstract(pascal::parameter::type)


def test_pascal::parameter::type_constructor_exists():
    assert callable(pascal::parameter::type.__init__)


def test_pascal::parameter::type_constructor_args():
    sig = inspect.signature(pascal::parameter::type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pascal::parameter::type_has_name():
    assert hasattr(pascal::parameter::type, "name")
    descriptor = None
    for klass in pascal::parameter::type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pascal::variant::part_is_not_abstract():
    assert not inspect.isabstract(pascal::variant::part)


def test_pascal::variant::part_constructor_exists():
    assert callable(pascal::variant::part.__init__)


def test_pascal::variant::part_constructor_args():
    sig = inspect.signature(pascal::variant::part.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pascal::variant::part_has_name():
    assert hasattr(pascal::variant::part, "name")
    descriptor = None
    for klass in pascal::variant::part.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pascal::fixed::part_is_not_abstract():
    assert not inspect.isabstract(pascal::fixed::part)


def test_pascal::fixed::part_constructor_exists():
    assert callable(pascal::fixed::part.__init__)


def test_pascal::fixed::part_constructor_args():
    sig = inspect.signature(pascal::fixed::part.__init__)
    params = list(sig.parameters.keys())



def test_pascal::variant_is_not_abstract():
    assert not inspect.isabstract(pascal::variant)


def test_pascal::variant_constructor_exists():
    assert callable(pascal::variant.__init__)


def test_pascal::variant_constructor_args():
    sig = inspect.signature(pascal::variant.__init__)
    params = list(sig.parameters.keys())



def test_pascal::tag::field_is_not_abstract():
    assert not inspect.isabstract(pascal::tag::field)


def test_pascal::tag::field_constructor_exists():
    assert callable(pascal::tag::field.__init__)


def test_pascal::tag::field_constructor_args():
    sig = inspect.signature(pascal::tag::field.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pascal::tag::field_has_name():
    assert hasattr(pascal::tag::field, "name")
    descriptor = None
    for klass in pascal::tag::field.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pascal::abstraction::declaration_is_not_abstract():
    assert not inspect.isabstract(pascal::abstraction::declaration)


def test_pascal::abstraction::declaration_constructor_exists():
    assert callable(pascal::abstraction::declaration.__init__)


def test_pascal::abstraction::declaration_constructor_args():
    sig = inspect.signature(pascal::abstraction::declaration.__init__)
    params = list(sig.parameters.keys())
    assert "forward" in params, "Missing parameter 'forward'"

def test_pascal::abstraction::declaration_has_forward():
    assert hasattr(pascal::abstraction::declaration, "forward")
    descriptor = None
    for klass in pascal::abstraction::declaration.__mro__:
        if "forward" in klass.__dict__:
            descriptor = klass.__dict__["forward"]
            break
    assert isinstance(descriptor, property)



def test_pascal::variable::section_is_not_abstract():
    assert not inspect.isabstract(pascal::variable::section)


def test_pascal::variable::section_constructor_exists():
    assert callable(pascal::variable::section.__init__)


def test_pascal::variable::section_constructor_args():
    sig = inspect.signature(pascal::variable::section.__init__)
    params = list(sig.parameters.keys())



def test_pascal::variable::identifier::list_is_not_abstract():
    assert not inspect.isabstract(pascal::variable::identifier::list)


def test_pascal::variable::identifier::list_constructor_exists():
    assert callable(pascal::variable::identifier::list.__init__)


def test_pascal::variable::identifier::list_constructor_args():
    sig = inspect.signature(pascal::variable::identifier::list.__init__)
    params = list(sig.parameters.keys())
    assert "names" in params, "Missing parameter 'names'"

def test_pascal::variable::identifier::list_has_names():
    assert hasattr(pascal::variable::identifier::list, "names")
    descriptor = None
    for klass in pascal::variable::identifier::list.__mro__:
        if "names" in klass.__dict__:
            descriptor = klass.__dict__["names"]
            break
    assert isinstance(descriptor, property)



def test_pascal::record::section_is_not_abstract():
    assert not inspect.isabstract(pascal::record::section)


def test_pascal::record::section_constructor_exists():
    assert callable(pascal::record::section.__init__)


def test_pascal::record::section_constructor_args():
    sig = inspect.signature(pascal::record::section.__init__)
    params = list(sig.parameters.keys())



def test_pascal::abstraction::heading_is_not_abstract():
    assert not inspect.isabstract(pascal::abstraction::heading)


def test_pascal::abstraction::heading_constructor_exists():
    assert callable(pascal::abstraction::heading.__init__)


def test_pascal::abstraction::heading_constructor_args():
    sig = inspect.signature(pascal::abstraction::heading.__init__)
    params = list(sig.parameters.keys())
    assert "returnType" in params, "Missing parameter 'returnType'"
    assert "name" in params, "Missing parameter 'name'"

def test_pascal::abstraction::heading_has_returnType():
    assert hasattr(pascal::abstraction::heading, "returnType")
    descriptor = None
    for klass in pascal::abstraction::heading.__mro__:
        if "returnType" in klass.__dict__:
            descriptor = klass.__dict__["returnType"]
            break
    assert isinstance(descriptor, property)

def test_pascal::abstraction::heading_has_name():
    assert hasattr(pascal::abstraction::heading, "name")
    descriptor = None
    for klass in pascal::abstraction::heading.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pascal::enumerated::type_is_not_abstract():
    assert not inspect.isabstract(pascal::enumerated::type)


def test_pascal::enumerated::type_constructor_exists():
    assert callable(pascal::enumerated::type.__init__)


def test_pascal::enumerated::type_constructor_args():
    sig = inspect.signature(pascal::enumerated::type.__init__)
    params = list(sig.parameters.keys())



def test_pascal::subrange::type_is_not_abstract():
    assert not inspect.isabstract(pascal::subrange::type)


def test_pascal::subrange::type_constructor_exists():
    assert callable(pascal::subrange::type.__init__)


def test_pascal::subrange::type_constructor_args():
    sig = inspect.signature(pascal::subrange::type.__init__)
    params = list(sig.parameters.keys())
    assert "subrange" in params, "Missing parameter 'subrange'"

def test_pascal::subrange::type_has_subrange():
    assert hasattr(pascal::subrange::type, "subrange")
    descriptor = None
    for klass in pascal::subrange::type.__mro__:
        if "subrange" in klass.__dict__:
            descriptor = klass.__dict__["subrange"]
            break
    assert isinstance(descriptor, property)



def test_pascal::pointer::type_is_not_abstract():
    assert not inspect.isabstract(pascal::pointer::type)


def test_pascal::pointer::type_constructor_exists():
    assert callable(pascal::pointer::type.__init__)


def test_pascal::pointer::type_constructor_args():
    sig = inspect.signature(pascal::pointer::type.__init__)
    params = list(sig.parameters.keys())



def test_pascal::structured::type_is_not_abstract():
    assert not inspect.isabstract(pascal::structured::type)


def test_pascal::structured::type_constructor_exists():
    assert callable(pascal::structured::type.__init__)


def test_pascal::structured::type_constructor_args():
    sig = inspect.signature(pascal::structured::type.__init__)
    params = list(sig.parameters.keys())
    assert "packed" in params, "Missing parameter 'packed'"

def test_pascal::structured::type_has_packed():
    assert hasattr(pascal::structured::type, "packed")
    descriptor = None
    for klass in pascal::structured::type.__mro__:
        if "packed" in klass.__dict__:
            descriptor = klass.__dict__["packed"]
            break
    assert isinstance(descriptor, property)



def test_pascal::field::list_is_not_abstract():
    assert not inspect.isabstract(pascal::field::list)


def test_pascal::field::list_constructor_exists():
    assert callable(pascal::field::list.__init__)


def test_pascal::field::list_constructor_args():
    sig = inspect.signature(pascal::field::list.__init__)
    params = list(sig.parameters.keys())



def test_pascal::index::type_is_not_abstract():
    assert not inspect.isabstract(pascal::index::type)


def test_pascal::index::type_constructor_exists():
    assert callable(pascal::index::type.__init__)


def test_pascal::index::type_constructor_args():
    sig = inspect.signature(pascal::index::type.__init__)
    params = list(sig.parameters.keys())



def test_pascal::file::type_is_not_abstract():
    assert not inspect.isabstract(pascal::file::type)


def test_pascal::file::type_constructor_exists():
    assert callable(pascal::file::type.__init__)


def test_pascal::file::type_constructor_args():
    sig = inspect.signature(pascal::file::type.__init__)
    params = list(sig.parameters.keys())



def test_pascal::set::type_is_not_abstract():
    assert not inspect.isabstract(pascal::set::type)


def test_pascal::set::type_constructor_exists():
    assert callable(pascal::set::type.__init__)


def test_pascal::set::type_constructor_args():
    sig = inspect.signature(pascal::set::type.__init__)
    params = list(sig.parameters.keys())



def test_pascal::record::type_is_not_abstract():
    assert not inspect.isabstract(pascal::record::type)


def test_pascal::record::type_constructor_exists():
    assert callable(pascal::record::type.__init__)


def test_pascal::record::type_constructor_args():
    sig = inspect.signature(pascal::record::type.__init__)
    params = list(sig.parameters.keys())
    assert "recordKeyword" in params, "Missing parameter 'recordKeyword'"
    assert "endKeyword" in params, "Missing parameter 'endKeyword'"

def test_pascal::record::type_has_recordKeyword():
    assert hasattr(pascal::record::type, "recordKeyword")
    descriptor = None
    for klass in pascal::record::type.__mro__:
        if "recordKeyword" in klass.__dict__:
            descriptor = klass.__dict__["recordKeyword"]
            break
    assert isinstance(descriptor, property)

def test_pascal::record::type_has_endKeyword():
    assert hasattr(pascal::record::type, "endKeyword")
    descriptor = None
    for klass in pascal::record::type.__mro__:
        if "endKeyword" in klass.__dict__:
            descriptor = klass.__dict__["endKeyword"]
            break
    assert isinstance(descriptor, property)



def test_pascal::dynamic::array::type_is_not_abstract():
    assert not inspect.isabstract(pascal::dynamic::array::type)


def test_pascal::dynamic::array::type_constructor_exists():
    assert callable(pascal::dynamic::array::type.__init__)


def test_pascal::dynamic::array::type_constructor_args():
    sig = inspect.signature(pascal::dynamic::array::type.__init__)
    params = list(sig.parameters.keys())



def test_pascal::array::type_is_not_abstract():
    assert not inspect.isabstract(pascal::array::type)


def test_pascal::array::type_constructor_exists():
    assert callable(pascal::array::type.__init__)


def test_pascal::array::type_constructor_args():
    sig = inspect.signature(pascal::array::type.__init__)
    params = list(sig.parameters.keys())



def test_pascal::unpacked::structured::type_is_not_abstract():
    assert not inspect.isabstract(pascal::unpacked::structured::type)


def test_pascal::unpacked::structured::type_constructor_exists():
    assert callable(pascal::unpacked::structured::type.__init__)


def test_pascal::unpacked::structured::type_constructor_args():
    sig = inspect.signature(pascal::unpacked::structured::type.__init__)
    params = list(sig.parameters.keys())



def test_pascal::case::label::list_is_not_abstract():
    assert not inspect.isabstract(pascal::case::label::list)


def test_pascal::case::label::list_constructor_exists():
    assert callable(pascal::case::label::list.__init__)


def test_pascal::case::label::list_constructor_args():
    sig = inspect.signature(pascal::case::label::list.__init__)
    params = list(sig.parameters.keys())



def test_pascal::case::limb_is_not_abstract():
    assert not inspect.isabstract(pascal::case::limb)


def test_pascal::case::limb_constructor_exists():
    assert callable(pascal::case::limb.__init__)


def test_pascal::case::limb_constructor_args():
    sig = inspect.signature(pascal::case::limb.__init__)
    params = list(sig.parameters.keys())



def test_pascal::simple::type_is_not_abstract():
    assert not inspect.isabstract(pascal::simple::type)


def test_pascal::simple::type_constructor_exists():
    assert callable(pascal::simple::type.__init__)


def test_pascal::simple::type_constructor_args():
    sig = inspect.signature(pascal::simple::type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pascal::simple::type_has_name():
    assert hasattr(pascal::simple::type, "name")
    descriptor = None
    for klass in pascal::simple::type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pascal::type_is_not_abstract():
    assert not inspect.isabstract(pascal::type)


def test_pascal::type_constructor_exists():
    assert callable(pascal::type.__init__)


def test_pascal::type_constructor_args():
    sig = inspect.signature(pascal::type.__init__)
    params = list(sig.parameters.keys())



def test_pascal::type::definition_is_not_abstract():
    assert not inspect.isabstract(pascal::type::definition)


def test_pascal::type::definition_constructor_exists():
    assert callable(pascal::type::definition.__init__)


def test_pascal::type::definition_constructor_args():
    sig = inspect.signature(pascal::type::definition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pascal::type::definition_has_name():
    assert hasattr(pascal::type::definition, "name")
    descriptor = None
    for klass in pascal::type::definition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pascal::constant::definition_is_not_abstract():
    assert not inspect.isabstract(pascal::constant::definition)


def test_pascal::constant::definition_constructor_exists():
    assert callable(pascal::constant::definition.__init__)


def test_pascal::constant::definition_constructor_args():
    sig = inspect.signature(pascal::constant::definition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pascal::constant::definition_has_name():
    assert hasattr(pascal::constant::definition, "name")
    descriptor = None
    for klass in pascal::constant::definition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pascal::constant_is_not_abstract():
    assert not inspect.isabstract(pascal::constant)


def test_pascal::constant_constructor_exists():
    assert callable(pascal::constant.__init__)


def test_pascal::constant_constructor_args():
    sig = inspect.signature(pascal::constant.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "boolLiteral" in params, "Missing parameter 'boolLiteral'"
    assert "string" in params, "Missing parameter 'string'"
    assert "nil" in params, "Missing parameter 'nil'"
    assert "opterator" in params, "Missing parameter 'opterator'"

def test_pascal::constant_has_name():
    assert hasattr(pascal::constant, "name")
    descriptor = None
    for klass in pascal::constant.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_pascal::constant_has_boolLiteral():
    assert hasattr(pascal::constant, "boolLiteral")
    descriptor = None
    for klass in pascal::constant.__mro__:
        if "boolLiteral" in klass.__dict__:
            descriptor = klass.__dict__["boolLiteral"]
            break
    assert isinstance(descriptor, property)

def test_pascal::constant_has_string():
    assert hasattr(pascal::constant, "string")
    descriptor = None
    for klass in pascal::constant.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)

def test_pascal::constant_has_nil():
    assert hasattr(pascal::constant, "nil")
    descriptor = None
    for klass in pascal::constant.__mro__:
        if "nil" in klass.__dict__:
            descriptor = klass.__dict__["nil"]
            break
    assert isinstance(descriptor, property)

def test_pascal::constant_has_opterator():
    assert hasattr(pascal::constant, "opterator")
    descriptor = None
    for klass in pascal::constant.__mro__:
        if "opterator" in klass.__dict__:
            descriptor = klass.__dict__["opterator"]
            break
    assert isinstance(descriptor, property)



def test_pascal::compound::statement_is_not_abstract():
    assert not inspect.isabstract(pascal::compound::statement)


def test_pascal::compound::statement_constructor_exists():
    assert callable(pascal::compound::statement.__init__)


def test_pascal::compound::statement_constructor_args():
    sig = inspect.signature(pascal::compound::statement.__init__)
    params = list(sig.parameters.keys())



def test_pascal::case::statement_is_not_abstract():
    assert not inspect.isabstract(pascal::case::statement)


def test_pascal::case::statement_constructor_exists():
    assert callable(pascal::case::statement.__init__)


def test_pascal::case::statement_constructor_args():
    sig = inspect.signature(pascal::case::statement.__init__)
    params = list(sig.parameters.keys())



def test_pascal::if::statement_is_not_abstract():
    assert not inspect.isabstract(pascal::if::statement)


def test_pascal::if::statement_constructor_exists():
    assert callable(pascal::if::statement.__init__)


def test_pascal::if::statement_constructor_args():
    sig = inspect.signature(pascal::if::statement.__init__)
    params = list(sig.parameters.keys())



def test_pascal::for::statement_is_not_abstract():
    assert not inspect.isabstract(pascal::for::statement)


def test_pascal::for::statement_constructor_exists():
    assert callable(pascal::for::statement.__init__)


def test_pascal::for::statement_constructor_args():
    sig = inspect.signature(pascal::for::statement.__init__)
    params = list(sig.parameters.keys())



def test_pascal::repeat::statement_is_not_abstract():
    assert not inspect.isabstract(pascal::repeat::statement)


def test_pascal::repeat::statement_constructor_exists():
    assert callable(pascal::repeat::statement.__init__)


def test_pascal::repeat::statement_constructor_args():
    sig = inspect.signature(pascal::repeat::statement.__init__)
    params = list(sig.parameters.keys())



def test_pascal::while::statement_is_not_abstract():
    assert not inspect.isabstract(pascal::while::statement)


def test_pascal::while::statement_constructor_exists():
    assert callable(pascal::while::statement.__init__)


def test_pascal::while::statement_constructor_args():
    sig = inspect.signature(pascal::while::statement.__init__)
    params = list(sig.parameters.keys())



def test_pascal::with::statement_is_not_abstract():
    assert not inspect.isabstract(pascal::with::statement)


def test_pascal::with::statement_constructor_exists():
    assert callable(pascal::with::statement.__init__)


def test_pascal::with::statement_constructor_args():
    sig = inspect.signature(pascal::with::statement.__init__)
    params = list(sig.parameters.keys())



def test_pascal::conditional::statement_is_not_abstract():
    assert not inspect.isabstract(pascal::conditional::statement)


def test_pascal::conditional::statement_constructor_exists():
    assert callable(pascal::conditional::statement.__init__)


def test_pascal::conditional::statement_constructor_args():
    sig = inspect.signature(pascal::conditional::statement.__init__)
    params = list(sig.parameters.keys())



def test_pascal::repetitive::statement_is_not_abstract():
    assert not inspect.isabstract(pascal::repetitive::statement)


def test_pascal::repetitive::statement_constructor_exists():
    assert callable(pascal::repetitive::statement.__init__)


def test_pascal::repetitive::statement_constructor_args():
    sig = inspect.signature(pascal::repetitive::statement.__init__)
    params = list(sig.parameters.keys())



def test_pascal::expression::list_is_not_abstract():
    assert not inspect.isabstract(pascal::expression::list)


def test_pascal::expression::list_constructor_exists():
    assert callable(pascal::expression::list.__init__)


def test_pascal::expression::list_constructor_args():
    sig = inspect.signature(pascal::expression::list.__init__)
    params = list(sig.parameters.keys())



def test_pascal::any::number_is_not_abstract():
    assert not inspect.isabstract(pascal::any::number)


def test_pascal::any::number_constructor_exists():
    assert callable(pascal::any::number.__init__)


def test_pascal::any::number_constructor_args():
    sig = inspect.signature(pascal::any::number.__init__)
    params = list(sig.parameters.keys())
    assert "real" in params, "Missing parameter 'real'"
    assert "integer" in params, "Missing parameter 'integer'"

def test_pascal::any::number_has_real():
    assert hasattr(pascal::any::number, "real")
    descriptor = None
    for klass in pascal::any::number.__mro__:
        if "real" in klass.__dict__:
            descriptor = klass.__dict__["real"]
            break
    assert isinstance(descriptor, property)

def test_pascal::any::number_has_integer():
    assert hasattr(pascal::any::number, "integer")
    descriptor = None
    for klass in pascal::any::number.__mro__:
        if "integer" in klass.__dict__:
            descriptor = klass.__dict__["integer"]
            break
    assert isinstance(descriptor, property)



def test_pascal::set_is_not_abstract():
    assert not inspect.isabstract(pascal::set)


def test_pascal::set_constructor_exists():
    assert callable(pascal::set.__init__)


def test_pascal::set_constructor_args():
    sig = inspect.signature(pascal::set.__init__)
    params = list(sig.parameters.keys())
    assert "brackets" in params, "Missing parameter 'brackets'"

def test_pascal::set_has_brackets():
    assert hasattr(pascal::set, "brackets")
    descriptor = None
    for klass in pascal::set.__mro__:
        if "brackets" in klass.__dict__:
            descriptor = klass.__dict__["brackets"]
            break
    assert isinstance(descriptor, property)



def test_pascal::number_is_not_abstract():
    assert not inspect.isabstract(pascal::number)


def test_pascal::number_constructor_exists():
    assert callable(pascal::number.__init__)


def test_pascal::number_constructor_args():
    sig = inspect.signature(pascal::number.__init__)
    params = list(sig.parameters.keys())



def test_pascal::factor_is_not_abstract():
    assert not inspect.isabstract(pascal::factor)


def test_pascal::factor_constructor_exists():
    assert callable(pascal::factor.__init__)


def test_pascal::factor_constructor_args():
    sig = inspect.signature(pascal::factor.__init__)
    params = list(sig.parameters.keys())
    assert "string" in params, "Missing parameter 'string'"
    assert "nil" in params, "Missing parameter 'nil'"
    assert "boolean" in params, "Missing parameter 'boolean'"

def test_pascal::factor_has_string():
    assert hasattr(pascal::factor, "string")
    descriptor = None
    for klass in pascal::factor.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)

def test_pascal::factor_has_nil():
    assert hasattr(pascal::factor, "nil")
    descriptor = None
    for klass in pascal::factor.__mro__:
        if "nil" in klass.__dict__:
            descriptor = klass.__dict__["nil"]
            break
    assert isinstance(descriptor, property)

def test_pascal::factor_has_boolean():
    assert hasattr(pascal::factor, "boolean")
    descriptor = None
    for klass in pascal::factor.__mro__:
        if "boolean" in klass.__dict__:
            descriptor = klass.__dict__["boolean"]
            break
    assert isinstance(descriptor, property)



def test_pascal::term_is_not_abstract():
    assert not inspect.isabstract(pascal::term)


def test_pascal::term_constructor_exists():
    assert callable(pascal::term.__init__)


def test_pascal::term_constructor_args():
    sig = inspect.signature(pascal::term.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"

def test_pascal::term_has_operators():
    assert hasattr(pascal::term, "operators")
    descriptor = None
    for klass in pascal::term.__mro__:
        if "operators" in klass.__dict__:
            descriptor = klass.__dict__["operators"]
            break
    assert isinstance(descriptor, property)



def test_pascal::eobject_is_not_abstract():
    assert not inspect.isabstract(pascal::EObject)


def test_pascal::eobject_constructor_exists():
    assert callable(pascal::EObject.__init__)


def test_pascal::eobject_constructor_args():
    sig = inspect.signature(pascal::EObject.__init__)
    params = list(sig.parameters.keys())



def test_pascal::simple::expression_is_not_abstract():
    assert not inspect.isabstract(pascal::simple::expression)


def test_pascal::simple::expression_constructor_exists():
    assert callable(pascal::simple::expression.__init__)


def test_pascal::simple::expression_constructor_args():
    sig = inspect.signature(pascal::simple::expression.__init__)
    params = list(sig.parameters.keys())
    assert "prefixOperator" in params, "Missing parameter 'prefixOperator'"
    assert "operators" in params, "Missing parameter 'operators'"

def test_pascal::simple::expression_has_prefixOperator():
    assert hasattr(pascal::simple::expression, "prefixOperator")
    descriptor = None
    for klass in pascal::simple::expression.__mro__:
        if "prefixOperator" in klass.__dict__:
            descriptor = klass.__dict__["prefixOperator"]
            break
    assert isinstance(descriptor, property)

def test_pascal::simple::expression_has_operators():
    assert hasattr(pascal::simple::expression, "operators")
    descriptor = None
    for klass in pascal::simple::expression.__mro__:
        if "operators" in klass.__dict__:
            descriptor = klass.__dict__["operators"]
            break
    assert isinstance(descriptor, property)



def test_pascal::variable::declaration::part_is_not_abstract():
    assert not inspect.isabstract(pascal::variable::declaration::part)


def test_pascal::variable::declaration::part_constructor_exists():
    assert callable(pascal::variable::declaration::part.__init__)


def test_pascal::variable::declaration::part_constructor_args():
    sig = inspect.signature(pascal::variable::declaration::part.__init__)
    params = list(sig.parameters.keys())



def test_pascal::type::definition::part_is_not_abstract():
    assert not inspect.isabstract(pascal::type::definition::part)


def test_pascal::type::definition::part_constructor_exists():
    assert callable(pascal::type::definition::part.__init__)


def test_pascal::type::definition::part_constructor_args():
    sig = inspect.signature(pascal::type::definition::part.__init__)
    params = list(sig.parameters.keys())



def test_pascal::var::_is_not_abstract():
    assert not inspect.isabstract(pascal::var::)


def test_pascal::var::_constructor_exists():
    assert callable(pascal::var::.__init__)


def test_pascal::var::_constructor_args():
    sig = inspect.signature(pascal::var::.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "accessor" in params, "Missing parameter 'accessor'"

def test_pascal::var::_has_name():
    assert hasattr(pascal::var::, "name")
    descriptor = None
    for klass in pascal::var::.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_pascal::var::_has_accessor():
    assert hasattr(pascal::var::, "accessor")
    descriptor = None
    for klass in pascal::var::.__mro__:
        if "accessor" in klass.__dict__:
            descriptor = klass.__dict__["accessor"]
            break
    assert isinstance(descriptor, property)



def test_pascal::expression_is_not_abstract():
    assert not inspect.isabstract(pascal::expression)


def test_pascal::expression_constructor_exists():
    assert callable(pascal::expression.__init__)


def test_pascal::expression_constructor_args():
    sig = inspect.signature(pascal::expression.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"

def test_pascal::expression_has_operators():
    assert hasattr(pascal::expression, "operators")
    descriptor = None
    for klass in pascal::expression.__mro__:
        if "operators" in klass.__dict__:
            descriptor = klass.__dict__["operators"]
            break
    assert isinstance(descriptor, property)



def test_pascal::variable_is_not_abstract():
    assert not inspect.isabstract(pascal::variable)


def test_pascal::variable_constructor_exists():
    assert callable(pascal::variable.__init__)


def test_pascal::variable_constructor_args():
    sig = inspect.signature(pascal::variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pascal::variable_has_name():
    assert hasattr(pascal::variable, "name")
    descriptor = None
    for klass in pascal::variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pascal::goto::statement_is_not_abstract():
    assert not inspect.isabstract(pascal::goto::statement)


def test_pascal::goto::statement_constructor_exists():
    assert callable(pascal::goto::statement.__init__)


def test_pascal::goto::statement_constructor_args():
    sig = inspect.signature(pascal::goto::statement.__init__)
    params = list(sig.parameters.keys())



def test_pascal::function::designator_is_not_abstract():
    assert not inspect.isabstract(pascal::function::designator)


def test_pascal::function::designator_constructor_exists():
    assert callable(pascal::function::designator.__init__)


def test_pascal::function::designator_constructor_args():
    sig = inspect.signature(pascal::function::designator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pascal::function::designator_has_name():
    assert hasattr(pascal::function::designator, "name")
    descriptor = None
    for klass in pascal::function::designator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pascal::assignment::statement_is_not_abstract():
    assert not inspect.isabstract(pascal::assignment::statement)


def test_pascal::assignment::statement_constructor_exists():
    assert callable(pascal::assignment::statement.__init__)


def test_pascal::assignment::statement_constructor_args():
    sig = inspect.signature(pascal::assignment::statement.__init__)
    params = list(sig.parameters.keys())



def test_pascal::structured::statement_is_not_abstract():
    assert not inspect.isabstract(pascal::structured::statement)


def test_pascal::structured::statement_constructor_exists():
    assert callable(pascal::structured::statement.__init__)


def test_pascal::structured::statement_constructor_args():
    sig = inspect.signature(pascal::structured::statement.__init__)
    params = list(sig.parameters.keys())



def test_pascal::simple::statement_is_not_abstract():
    assert not inspect.isabstract(pascal::simple::statement)


def test_pascal::simple::statement_constructor_exists():
    assert callable(pascal::simple::statement.__init__)


def test_pascal::simple::statement_constructor_args():
    sig = inspect.signature(pascal::simple::statement.__init__)
    params = list(sig.parameters.keys())
    assert "function_noargs" in params, "Missing parameter 'function_noargs'"

def test_pascal::simple::statement_has_function_noargs():
    assert hasattr(pascal::simple::statement, "function_noargs")
    descriptor = None
    for klass in pascal::simple::statement.__mro__:
        if "function_noargs" in klass.__dict__:
            descriptor = klass.__dict__["function_noargs"]
            break
    assert isinstance(descriptor, property)



def test_pascal::label_is_not_abstract():
    assert not inspect.isabstract(pascal::label)


def test_pascal::label_constructor_exists():
    assert callable(pascal::label.__init__)


def test_pascal::label_constructor_args():
    sig = inspect.signature(pascal::label.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"

def test_pascal::label_has_number():
    assert hasattr(pascal::label, "number")
    descriptor = None
    for klass in pascal::label.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_pascal::statement_is_not_abstract():
    assert not inspect.isabstract(pascal::statement)


def test_pascal::statement_constructor_exists():
    assert callable(pascal::statement.__init__)


def test_pascal::statement_constructor_args():
    sig = inspect.signature(pascal::statement.__init__)
    params = list(sig.parameters.keys())



def test_pascal::statement::sequence_is_not_abstract():
    assert not inspect.isabstract(pascal::statement::sequence)


def test_pascal::statement::sequence_constructor_exists():
    assert callable(pascal::statement::sequence.__init__)


def test_pascal::statement::sequence_constructor_args():
    sig = inspect.signature(pascal::statement::sequence.__init__)
    params = list(sig.parameters.keys())



def test_pascal::statement::part_is_not_abstract():
    assert not inspect.isabstract(pascal::statement::part)


def test_pascal::statement::part_constructor_exists():
    assert callable(pascal::statement::part.__init__)


def test_pascal::statement::part_constructor_args():
    sig = inspect.signature(pascal::statement::part.__init__)
    params = list(sig.parameters.keys())



def test_pascal::procedure::and::function::declaration::part_is_not_abstract():
    assert not inspect.isabstract(pascal::procedure::and::function::declaration::part)


def test_pascal::procedure::and::function::declaration::part_constructor_exists():
    assert callable(pascal::procedure::and::function::declaration::part.__init__)


def test_pascal::procedure::and::function::declaration::part_constructor_args():
    sig = inspect.signature(pascal::procedure::and::function::declaration::part.__init__)
    params = list(sig.parameters.keys())



def test_pascal::constant::definition::part_is_not_abstract():
    assert not inspect.isabstract(pascal::constant::definition::part)


def test_pascal::constant::definition::part_constructor_exists():
    assert callable(pascal::constant::definition::part.__init__)


def test_pascal::constant::definition::part_constructor_args():
    sig = inspect.signature(pascal::constant::definition::part.__init__)
    params = list(sig.parameters.keys())



def test_pascal::label::declaration::part_is_not_abstract():
    assert not inspect.isabstract(pascal::label::declaration::part)


def test_pascal::label::declaration::part_constructor_exists():
    assert callable(pascal::label::declaration::part.__init__)


def test_pascal::label::declaration::part_constructor_args():
    sig = inspect.signature(pascal::label::declaration::part.__init__)
    params = list(sig.parameters.keys())



def test_pascal::identifier::list_is_not_abstract():
    assert not inspect.isabstract(pascal::identifier::list)


def test_pascal::identifier::list_constructor_exists():
    assert callable(pascal::identifier::list.__init__)


def test_pascal::identifier::list_constructor_args():
    sig = inspect.signature(pascal::identifier::list.__init__)
    params = list(sig.parameters.keys())
    assert "names" in params, "Missing parameter 'names'"

def test_pascal::identifier::list_has_names():
    assert hasattr(pascal::identifier::list, "names")
    descriptor = None
    for klass in pascal::identifier::list.__mro__:
        if "names" in klass.__dict__:
            descriptor = klass.__dict__["names"]
            break
    assert isinstance(descriptor, property)



def test_pascal::block_is_not_abstract():
    assert not inspect.isabstract(pascal::block)


def test_pascal::block_constructor_exists():
    assert callable(pascal::block.__init__)


def test_pascal::block_constructor_args():
    sig = inspect.signature(pascal::block.__init__)
    params = list(sig.parameters.keys())



def test_pascal::program::heading::block_is_not_abstract():
    assert not inspect.isabstract(pascal::program::heading::block)


def test_pascal::program::heading::block_constructor_exists():
    assert callable(pascal::program::heading::block.__init__)


def test_pascal::program::heading::block_constructor_args():
    sig = inspect.signature(pascal::program::heading::block.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pascal::program::heading::block_has_name():
    assert hasattr(pascal::program::heading::block, "name")
    descriptor = None
    for klass in pascal::program::heading::block.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pascal::program_is_not_abstract():
    assert not inspect.isabstract(pascal::program)


def test_pascal::program_constructor_exists():
    assert callable(pascal::program.__init__)


def test_pascal::program_constructor_args():
    sig = inspect.signature(pascal::program.__init__)
    params = list(sig.parameters.keys())



def test_pascal::pascal_is_not_abstract():
    assert not inspect.isabstract(pascal::pascal)


def test_pascal::pascal_constructor_exists():
    assert callable(pascal::pascal.__init__)


def test_pascal::pascal_constructor_args():
    sig = inspect.signature(pascal::pascal.__init__)
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
pascal::variable::parameter::section_strategy = st.builds(
    pascal::variable::parameter::section,
)
pascal::value::parameter::section_strategy = st.builds(
    pascal::value::parameter::section,
)
pascal::formal::parameter::section_strategy = st.builds(
    pascal::formal::parameter::section,
)
pascal::formal::parameter::list_strategy = st.builds(
    pascal::formal::parameter::list,
)
abstraction::declaration_strategy = st.builds(
    abstraction::declaration,
)
pascal::bound::specification_strategy = st.builds(
    pascal::bound::specification,
    final=
        safe_text,
    initial=
        safe_text,
    name=
        safe_text
)
pascal::unpacked::conformant::array::schema_strategy = st.builds(
    pascal::unpacked::conformant::array::schema,
)
pascal::packed::conformant::array::schema_strategy = st.builds(
    pascal::packed::conformant::array::schema,
    name=
        safe_text
)
pascal::conformant::array::schema_strategy = st.builds(
    pascal::conformant::array::schema,
)
pascal::parameter::type_strategy = st.builds(
    pascal::parameter::type,
    name=
        safe_text
)
pascal::variant::part_strategy = st.builds(
    pascal::variant::part,
    name=
        safe_text
)
pascal::fixed::part_strategy = st.builds(
    pascal::fixed::part,
)
pascal::variant_strategy = st.builds(
    pascal::variant,
)
pascal::tag::field_strategy = st.builds(
    pascal::tag::field,
    name=
        safe_text
)
pascal::abstraction::declaration_strategy = st.builds(
    pascal::abstraction::declaration,
    forward=
        st.booleans()
)
pascal::variable::section_strategy = st.builds(
    pascal::variable::section,
)
pascal::variable::identifier::list_strategy = st.builds(
    pascal::variable::identifier::list,
    names=
        safe_text
)
pascal::record::section_strategy = st.builds(
    pascal::record::section,
)
pascal::abstraction::heading_strategy = st.builds(
    pascal::abstraction::heading,
    returnType=
        safe_text,
    name=
        safe_text
)
pascal::enumerated::type_strategy = st.builds(
    pascal::enumerated::type,
)
pascal::subrange::type_strategy = st.builds(
    pascal::subrange::type,
    subrange=
        safe_text
)
pascal::pointer::type_strategy = st.builds(
    pascal::pointer::type,
)
pascal::structured::type_strategy = st.builds(
    pascal::structured::type,
    packed=
        st.booleans()
)
pascal::field::list_strategy = st.builds(
    pascal::field::list,
)
pascal::index::type_strategy = st.builds(
    pascal::index::type,
)
pascal::file::type_strategy = st.builds(
    pascal::file::type,
)
pascal::set::type_strategy = st.builds(
    pascal::set::type,
)
pascal::record::type_strategy = st.builds(
    pascal::record::type,
    recordKeyword=
        safe_text,
    endKeyword=
        safe_text
)
pascal::dynamic::array::type_strategy = st.builds(
    pascal::dynamic::array::type,
)
pascal::array::type_strategy = st.builds(
    pascal::array::type,
)
pascal::unpacked::structured::type_strategy = st.builds(
    pascal::unpacked::structured::type,
)
pascal::case::label::list_strategy = st.builds(
    pascal::case::label::list,
)
pascal::case::limb_strategy = st.builds(
    pascal::case::limb,
)
pascal::simple::type_strategy = st.builds(
    pascal::simple::type,
    name=
        safe_text
)
pascal::type_strategy = st.builds(
    pascal::type,
)
pascal::type::definition_strategy = st.builds(
    pascal::type::definition,
    name=
        safe_text
)
pascal::constant::definition_strategy = st.builds(
    pascal::constant::definition,
    name=
        safe_text
)
pascal::constant_strategy = st.builds(
    pascal::constant,
    name=
        safe_text,
    boolLiteral=
        safe_text,
    string=
        safe_text,
    nil=
        safe_text,
    opterator=
        safe_text
)
pascal::compound::statement_strategy = st.builds(
    pascal::compound::statement,
)
pascal::case::statement_strategy = st.builds(
    pascal::case::statement,
)
pascal::if::statement_strategy = st.builds(
    pascal::if::statement,
)
pascal::for::statement_strategy = st.builds(
    pascal::for::statement,
)
pascal::repeat::statement_strategy = st.builds(
    pascal::repeat::statement,
)
pascal::while::statement_strategy = st.builds(
    pascal::while::statement,
)
pascal::with::statement_strategy = st.builds(
    pascal::with::statement,
)
pascal::conditional::statement_strategy = st.builds(
    pascal::conditional::statement,
)
pascal::repetitive::statement_strategy = st.builds(
    pascal::repetitive::statement,
)
pascal::expression::list_strategy = st.builds(
    pascal::expression::list,
)
pascal::any::number_strategy = st.builds(
    pascal::any::number,
    real=
        safe_text,
    integer=
        safe_text
)
pascal::set_strategy = st.builds(
    pascal::set,
    brackets=
        safe_text
)
pascal::number_strategy = st.builds(
    pascal::number,
)
pascal::factor_strategy = st.builds(
    pascal::factor,
    string=
        safe_text,
    nil=
        st.booleans(),
    boolean=
        safe_text
)
pascal::term_strategy = st.builds(
    pascal::term,
    operators=
        safe_text
)
pascal::EObject_strategy = st.builds(
    pascal::EObject,
)
pascal::simple::expression_strategy = st.builds(
    pascal::simple::expression,
    prefixOperator=
        safe_text,
    operators=
        safe_text
)
pascal::variable::declaration::part_strategy = st.builds(
    pascal::variable::declaration::part,
)
pascal::type::definition::part_strategy = st.builds(
    pascal::type::definition::part,
)
pascal::var::_strategy = st.builds(
    pascal::var::,
    name=
        safe_text,
    accessor=
        st.booleans()
)
pascal::expression_strategy = st.builds(
    pascal::expression,
    operators=
        safe_text
)
pascal::variable_strategy = st.builds(
    pascal::variable,
    name=
        safe_text
)
pascal::goto::statement_strategy = st.builds(
    pascal::goto::statement,
)
pascal::function::designator_strategy = st.builds(
    pascal::function::designator,
    name=
        safe_text
)
pascal::assignment::statement_strategy = st.builds(
    pascal::assignment::statement,
)
pascal::structured::statement_strategy = st.builds(
    pascal::structured::statement,
)
pascal::simple::statement_strategy = st.builds(
    pascal::simple::statement,
    function_noargs=
        safe_text
)
pascal::label_strategy = st.builds(
    pascal::label,
    number=
        safe_text
)
pascal::statement_strategy = st.builds(
    pascal::statement,
)
pascal::statement::sequence_strategy = st.builds(
    pascal::statement::sequence,
)
pascal::statement::part_strategy = st.builds(
    pascal::statement::part,
)
pascal::procedure::and::function::declaration::part_strategy = st.builds(
    pascal::procedure::and::function::declaration::part,
)
pascal::constant::definition::part_strategy = st.builds(
    pascal::constant::definition::part,
)
pascal::label::declaration::part_strategy = st.builds(
    pascal::label::declaration::part,
)
pascal::identifier::list_strategy = st.builds(
    pascal::identifier::list,
    names=
        safe_text
)
pascal::block_strategy = st.builds(
    pascal::block,
)
pascal::program::heading::block_strategy = st.builds(
    pascal::program::heading::block,
    name=
        safe_text
)
pascal::program_strategy = st.builds(
    pascal::program,
)
pascal::pascal_strategy = st.builds(
    pascal::pascal,
)

@given(instance=pascal::variable::parameter::section_strategy)
@settings(max_examples=50)
def test_pascal::variable::parameter::section_instantiation(instance):
    assert isinstance(instance, pascal::variable::parameter::section)

@given(instance=pascal::value::parameter::section_strategy)
@settings(max_examples=50)
def test_pascal::value::parameter::section_instantiation(instance):
    assert isinstance(instance, pascal::value::parameter::section)

@given(instance=pascal::formal::parameter::section_strategy)
@settings(max_examples=50)
def test_pascal::formal::parameter::section_instantiation(instance):
    assert isinstance(instance, pascal::formal::parameter::section)

@given(instance=pascal::formal::parameter::list_strategy)
@settings(max_examples=50)
def test_pascal::formal::parameter::list_instantiation(instance):
    assert isinstance(instance, pascal::formal::parameter::list)

@given(instance=abstraction::declaration_strategy)
@settings(max_examples=50)
def test_abstraction::declaration_instantiation(instance):
    assert isinstance(instance, abstraction::declaration)

@given(instance=pascal::bound::specification_strategy)
@settings(max_examples=50)
def test_pascal::bound::specification_instantiation(instance):
    assert isinstance(instance, pascal::bound::specification)

@given(instance=pascal::bound::specification_strategy)
def test_pascal::bound::specification_final_type(instance):
    assert isinstance(instance.final, str)


@given(instance=pascal::bound::specification_strategy)
def test_pascal::bound::specification_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original

@given(instance=pascal::bound::specification_strategy)
def test_pascal::bound::specification_initial_type(instance):
    assert isinstance(instance.initial, str)


@given(instance=pascal::bound::specification_strategy)
def test_pascal::bound::specification_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original

@given(instance=pascal::bound::specification_strategy)
def test_pascal::bound::specification_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=pascal::bound::specification_strategy)
def test_pascal::bound::specification_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pascal::unpacked::conformant::array::schema_strategy)
@settings(max_examples=50)
def test_pascal::unpacked::conformant::array::schema_instantiation(instance):
    assert isinstance(instance, pascal::unpacked::conformant::array::schema)

@given(instance=pascal::packed::conformant::array::schema_strategy)
@settings(max_examples=50)
def test_pascal::packed::conformant::array::schema_instantiation(instance):
    assert isinstance(instance, pascal::packed::conformant::array::schema)

@given(instance=pascal::packed::conformant::array::schema_strategy)
def test_pascal::packed::conformant::array::schema_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=pascal::packed::conformant::array::schema_strategy)
def test_pascal::packed::conformant::array::schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pascal::conformant::array::schema_strategy)
@settings(max_examples=50)
def test_pascal::conformant::array::schema_instantiation(instance):
    assert isinstance(instance, pascal::conformant::array::schema)

@given(instance=pascal::parameter::type_strategy)
@settings(max_examples=50)
def test_pascal::parameter::type_instantiation(instance):
    assert isinstance(instance, pascal::parameter::type)

@given(instance=pascal::parameter::type_strategy)
def test_pascal::parameter::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=pascal::parameter::type_strategy)
def test_pascal::parameter::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pascal::variant::part_strategy)
@settings(max_examples=50)
def test_pascal::variant::part_instantiation(instance):
    assert isinstance(instance, pascal::variant::part)

@given(instance=pascal::variant::part_strategy)
def test_pascal::variant::part_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=pascal::variant::part_strategy)
def test_pascal::variant::part_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pascal::fixed::part_strategy)
@settings(max_examples=50)
def test_pascal::fixed::part_instantiation(instance):
    assert isinstance(instance, pascal::fixed::part)

@given(instance=pascal::variant_strategy)
@settings(max_examples=50)
def test_pascal::variant_instantiation(instance):
    assert isinstance(instance, pascal::variant)

@given(instance=pascal::tag::field_strategy)
@settings(max_examples=50)
def test_pascal::tag::field_instantiation(instance):
    assert isinstance(instance, pascal::tag::field)

@given(instance=pascal::tag::field_strategy)
def test_pascal::tag::field_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=pascal::tag::field_strategy)
def test_pascal::tag::field_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pascal::abstraction::declaration_strategy)
@settings(max_examples=50)
def test_pascal::abstraction::declaration_instantiation(instance):
    assert isinstance(instance, pascal::abstraction::declaration)

@given(instance=pascal::abstraction::declaration_strategy)
def test_pascal::abstraction::declaration_forward_type(instance):
    assert isinstance(instance.forward, bool)


@given(instance=pascal::abstraction::declaration_strategy)
def test_pascal::abstraction::declaration_forward_setter(instance):
    original = instance.forward
    instance.forward = original
    assert instance.forward == original

@given(instance=pascal::variable::section_strategy)
@settings(max_examples=50)
def test_pascal::variable::section_instantiation(instance):
    assert isinstance(instance, pascal::variable::section)

@given(instance=pascal::variable::identifier::list_strategy)
@settings(max_examples=50)
def test_pascal::variable::identifier::list_instantiation(instance):
    assert isinstance(instance, pascal::variable::identifier::list)

@given(instance=pascal::variable::identifier::list_strategy)
def test_pascal::variable::identifier::list_names_type(instance):
    assert isinstance(instance.names, str)


@given(instance=pascal::variable::identifier::list_strategy)
def test_pascal::variable::identifier::list_names_setter(instance):
    original = instance.names
    instance.names = original
    assert instance.names == original

@given(instance=pascal::record::section_strategy)
@settings(max_examples=50)
def test_pascal::record::section_instantiation(instance):
    assert isinstance(instance, pascal::record::section)

@given(instance=pascal::abstraction::heading_strategy)
@settings(max_examples=50)
def test_pascal::abstraction::heading_instantiation(instance):
    assert isinstance(instance, pascal::abstraction::heading)

@given(instance=pascal::abstraction::heading_strategy)
def test_pascal::abstraction::heading_returnType_type(instance):
    assert isinstance(instance.returnType, str)


@given(instance=pascal::abstraction::heading_strategy)
def test_pascal::abstraction::heading_returnType_setter(instance):
    original = instance.returnType
    instance.returnType = original
    assert instance.returnType == original

@given(instance=pascal::abstraction::heading_strategy)
def test_pascal::abstraction::heading_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=pascal::abstraction::heading_strategy)
def test_pascal::abstraction::heading_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pascal::enumerated::type_strategy)
@settings(max_examples=50)
def test_pascal::enumerated::type_instantiation(instance):
    assert isinstance(instance, pascal::enumerated::type)

@given(instance=pascal::subrange::type_strategy)
@settings(max_examples=50)
def test_pascal::subrange::type_instantiation(instance):
    assert isinstance(instance, pascal::subrange::type)

@given(instance=pascal::subrange::type_strategy)
def test_pascal::subrange::type_subrange_type(instance):
    assert isinstance(instance.subrange, str)


@given(instance=pascal::subrange::type_strategy)
def test_pascal::subrange::type_subrange_setter(instance):
    original = instance.subrange
    instance.subrange = original
    assert instance.subrange == original

@given(instance=pascal::pointer::type_strategy)
@settings(max_examples=50)
def test_pascal::pointer::type_instantiation(instance):
    assert isinstance(instance, pascal::pointer::type)

@given(instance=pascal::structured::type_strategy)
@settings(max_examples=50)
def test_pascal::structured::type_instantiation(instance):
    assert isinstance(instance, pascal::structured::type)

@given(instance=pascal::structured::type_strategy)
def test_pascal::structured::type_packed_type(instance):
    assert isinstance(instance.packed, bool)


@given(instance=pascal::structured::type_strategy)
def test_pascal::structured::type_packed_setter(instance):
    original = instance.packed
    instance.packed = original
    assert instance.packed == original

@given(instance=pascal::field::list_strategy)
@settings(max_examples=50)
def test_pascal::field::list_instantiation(instance):
    assert isinstance(instance, pascal::field::list)

@given(instance=pascal::index::type_strategy)
@settings(max_examples=50)
def test_pascal::index::type_instantiation(instance):
    assert isinstance(instance, pascal::index::type)

@given(instance=pascal::file::type_strategy)
@settings(max_examples=50)
def test_pascal::file::type_instantiation(instance):
    assert isinstance(instance, pascal::file::type)

@given(instance=pascal::set::type_strategy)
@settings(max_examples=50)
def test_pascal::set::type_instantiation(instance):
    assert isinstance(instance, pascal::set::type)

@given(instance=pascal::record::type_strategy)
@settings(max_examples=50)
def test_pascal::record::type_instantiation(instance):
    assert isinstance(instance, pascal::record::type)

@given(instance=pascal::record::type_strategy)
def test_pascal::record::type_recordKeyword_type(instance):
    assert isinstance(instance.recordKeyword, str)


@given(instance=pascal::record::type_strategy)
def test_pascal::record::type_recordKeyword_setter(instance):
    original = instance.recordKeyword
    instance.recordKeyword = original
    assert instance.recordKeyword == original

@given(instance=pascal::record::type_strategy)
def test_pascal::record::type_endKeyword_type(instance):
    assert isinstance(instance.endKeyword, str)


@given(instance=pascal::record::type_strategy)
def test_pascal::record::type_endKeyword_setter(instance):
    original = instance.endKeyword
    instance.endKeyword = original
    assert instance.endKeyword == original

@given(instance=pascal::dynamic::array::type_strategy)
@settings(max_examples=50)
def test_pascal::dynamic::array::type_instantiation(instance):
    assert isinstance(instance, pascal::dynamic::array::type)

@given(instance=pascal::array::type_strategy)
@settings(max_examples=50)
def test_pascal::array::type_instantiation(instance):
    assert isinstance(instance, pascal::array::type)

@given(instance=pascal::unpacked::structured::type_strategy)
@settings(max_examples=50)
def test_pascal::unpacked::structured::type_instantiation(instance):
    assert isinstance(instance, pascal::unpacked::structured::type)

@given(instance=pascal::case::label::list_strategy)
@settings(max_examples=50)
def test_pascal::case::label::list_instantiation(instance):
    assert isinstance(instance, pascal::case::label::list)

@given(instance=pascal::case::limb_strategy)
@settings(max_examples=50)
def test_pascal::case::limb_instantiation(instance):
    assert isinstance(instance, pascal::case::limb)

@given(instance=pascal::simple::type_strategy)
@settings(max_examples=50)
def test_pascal::simple::type_instantiation(instance):
    assert isinstance(instance, pascal::simple::type)

@given(instance=pascal::simple::type_strategy)
def test_pascal::simple::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=pascal::simple::type_strategy)
def test_pascal::simple::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pascal::type_strategy)
@settings(max_examples=50)
def test_pascal::type_instantiation(instance):
    assert isinstance(instance, pascal::type)

@given(instance=pascal::type::definition_strategy)
@settings(max_examples=50)
def test_pascal::type::definition_instantiation(instance):
    assert isinstance(instance, pascal::type::definition)

@given(instance=pascal::type::definition_strategy)
def test_pascal::type::definition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=pascal::type::definition_strategy)
def test_pascal::type::definition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pascal::constant::definition_strategy)
@settings(max_examples=50)
def test_pascal::constant::definition_instantiation(instance):
    assert isinstance(instance, pascal::constant::definition)

@given(instance=pascal::constant::definition_strategy)
def test_pascal::constant::definition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=pascal::constant::definition_strategy)
def test_pascal::constant::definition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pascal::constant_strategy)
@settings(max_examples=50)
def test_pascal::constant_instantiation(instance):
    assert isinstance(instance, pascal::constant)

@given(instance=pascal::constant_strategy)
def test_pascal::constant_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=pascal::constant_strategy)
def test_pascal::constant_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pascal::constant_strategy)
def test_pascal::constant_boolLiteral_type(instance):
    assert isinstance(instance.boolLiteral, str)


@given(instance=pascal::constant_strategy)
def test_pascal::constant_boolLiteral_setter(instance):
    original = instance.boolLiteral
    instance.boolLiteral = original
    assert instance.boolLiteral == original

@given(instance=pascal::constant_strategy)
def test_pascal::constant_string_type(instance):
    assert isinstance(instance.string, str)


@given(instance=pascal::constant_strategy)
def test_pascal::constant_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original

@given(instance=pascal::constant_strategy)
def test_pascal::constant_nil_type(instance):
    assert isinstance(instance.nil, str)


@given(instance=pascal::constant_strategy)
def test_pascal::constant_nil_setter(instance):
    original = instance.nil
    instance.nil = original
    assert instance.nil == original

@given(instance=pascal::constant_strategy)
def test_pascal::constant_opterator_type(instance):
    assert isinstance(instance.opterator, str)


@given(instance=pascal::constant_strategy)
def test_pascal::constant_opterator_setter(instance):
    original = instance.opterator
    instance.opterator = original
    assert instance.opterator == original

@given(instance=pascal::compound::statement_strategy)
@settings(max_examples=50)
def test_pascal::compound::statement_instantiation(instance):
    assert isinstance(instance, pascal::compound::statement)

@given(instance=pascal::case::statement_strategy)
@settings(max_examples=50)
def test_pascal::case::statement_instantiation(instance):
    assert isinstance(instance, pascal::case::statement)

@given(instance=pascal::if::statement_strategy)
@settings(max_examples=50)
def test_pascal::if::statement_instantiation(instance):
    assert isinstance(instance, pascal::if::statement)

@given(instance=pascal::for::statement_strategy)
@settings(max_examples=50)
def test_pascal::for::statement_instantiation(instance):
    assert isinstance(instance, pascal::for::statement)

@given(instance=pascal::repeat::statement_strategy)
@settings(max_examples=50)
def test_pascal::repeat::statement_instantiation(instance):
    assert isinstance(instance, pascal::repeat::statement)

@given(instance=pascal::while::statement_strategy)
@settings(max_examples=50)
def test_pascal::while::statement_instantiation(instance):
    assert isinstance(instance, pascal::while::statement)

@given(instance=pascal::with::statement_strategy)
@settings(max_examples=50)
def test_pascal::with::statement_instantiation(instance):
    assert isinstance(instance, pascal::with::statement)

@given(instance=pascal::conditional::statement_strategy)
@settings(max_examples=50)
def test_pascal::conditional::statement_instantiation(instance):
    assert isinstance(instance, pascal::conditional::statement)

@given(instance=pascal::repetitive::statement_strategy)
@settings(max_examples=50)
def test_pascal::repetitive::statement_instantiation(instance):
    assert isinstance(instance, pascal::repetitive::statement)

@given(instance=pascal::expression::list_strategy)
@settings(max_examples=50)
def test_pascal::expression::list_instantiation(instance):
    assert isinstance(instance, pascal::expression::list)

@given(instance=pascal::any::number_strategy)
@settings(max_examples=50)
def test_pascal::any::number_instantiation(instance):
    assert isinstance(instance, pascal::any::number)

@given(instance=pascal::any::number_strategy)
def test_pascal::any::number_real_type(instance):
    assert isinstance(instance.real, str)


@given(instance=pascal::any::number_strategy)
def test_pascal::any::number_real_setter(instance):
    original = instance.real
    instance.real = original
    assert instance.real == original

@given(instance=pascal::any::number_strategy)
def test_pascal::any::number_integer_type(instance):
    assert isinstance(instance.integer, str)


@given(instance=pascal::any::number_strategy)
def test_pascal::any::number_integer_setter(instance):
    original = instance.integer
    instance.integer = original
    assert instance.integer == original

@given(instance=pascal::set_strategy)
@settings(max_examples=50)
def test_pascal::set_instantiation(instance):
    assert isinstance(instance, pascal::set)

@given(instance=pascal::set_strategy)
def test_pascal::set_brackets_type(instance):
    assert isinstance(instance.brackets, str)


@given(instance=pascal::set_strategy)
def test_pascal::set_brackets_setter(instance):
    original = instance.brackets
    instance.brackets = original
    assert instance.brackets == original

@given(instance=pascal::number_strategy)
@settings(max_examples=50)
def test_pascal::number_instantiation(instance):
    assert isinstance(instance, pascal::number)

@given(instance=pascal::factor_strategy)
@settings(max_examples=50)
def test_pascal::factor_instantiation(instance):
    assert isinstance(instance, pascal::factor)

@given(instance=pascal::factor_strategy)
def test_pascal::factor_string_type(instance):
    assert isinstance(instance.string, str)


@given(instance=pascal::factor_strategy)
def test_pascal::factor_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original

@given(instance=pascal::factor_strategy)
def test_pascal::factor_nil_type(instance):
    assert isinstance(instance.nil, bool)


@given(instance=pascal::factor_strategy)
def test_pascal::factor_nil_setter(instance):
    original = instance.nil
    instance.nil = original
    assert instance.nil == original

@given(instance=pascal::factor_strategy)
def test_pascal::factor_boolean_type(instance):
    assert isinstance(instance.boolean, str)


@given(instance=pascal::factor_strategy)
def test_pascal::factor_boolean_setter(instance):
    original = instance.boolean
    instance.boolean = original
    assert instance.boolean == original

@given(instance=pascal::term_strategy)
@settings(max_examples=50)
def test_pascal::term_instantiation(instance):
    assert isinstance(instance, pascal::term)

@given(instance=pascal::term_strategy)
def test_pascal::term_operators_type(instance):
    assert isinstance(instance.operators, str)


@given(instance=pascal::term_strategy)
def test_pascal::term_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original

@given(instance=pascal::EObject_strategy)
@settings(max_examples=50)
def test_pascal::eobject_instantiation(instance):
    assert isinstance(instance, pascal::EObject)

@given(instance=pascal::simple::expression_strategy)
@settings(max_examples=50)
def test_pascal::simple::expression_instantiation(instance):
    assert isinstance(instance, pascal::simple::expression)

@given(instance=pascal::simple::expression_strategy)
def test_pascal::simple::expression_prefixOperator_type(instance):
    assert isinstance(instance.prefixOperator, str)


@given(instance=pascal::simple::expression_strategy)
def test_pascal::simple::expression_prefixOperator_setter(instance):
    original = instance.prefixOperator
    instance.prefixOperator = original
    assert instance.prefixOperator == original

@given(instance=pascal::simple::expression_strategy)
def test_pascal::simple::expression_operators_type(instance):
    assert isinstance(instance.operators, str)


@given(instance=pascal::simple::expression_strategy)
def test_pascal::simple::expression_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original

@given(instance=pascal::variable::declaration::part_strategy)
@settings(max_examples=50)
def test_pascal::variable::declaration::part_instantiation(instance):
    assert isinstance(instance, pascal::variable::declaration::part)

@given(instance=pascal::type::definition::part_strategy)
@settings(max_examples=50)
def test_pascal::type::definition::part_instantiation(instance):
    assert isinstance(instance, pascal::type::definition::part)

@given(instance=pascal::var::_strategy)
@settings(max_examples=50)
def test_pascal::var::_instantiation(instance):
    assert isinstance(instance, pascal::var::)

@given(instance=pascal::var::_strategy)
def test_pascal::var::_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=pascal::var::_strategy)
def test_pascal::var::_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pascal::var::_strategy)
def test_pascal::var::_accessor_type(instance):
    assert isinstance(instance.accessor, bool)


@given(instance=pascal::var::_strategy)
def test_pascal::var::_accessor_setter(instance):
    original = instance.accessor
    instance.accessor = original
    assert instance.accessor == original

@given(instance=pascal::expression_strategy)
@settings(max_examples=50)
def test_pascal::expression_instantiation(instance):
    assert isinstance(instance, pascal::expression)

@given(instance=pascal::expression_strategy)
def test_pascal::expression_operators_type(instance):
    assert isinstance(instance.operators, str)


@given(instance=pascal::expression_strategy)
def test_pascal::expression_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original

@given(instance=pascal::variable_strategy)
@settings(max_examples=50)
def test_pascal::variable_instantiation(instance):
    assert isinstance(instance, pascal::variable)

@given(instance=pascal::variable_strategy)
def test_pascal::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=pascal::variable_strategy)
def test_pascal::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pascal::goto::statement_strategy)
@settings(max_examples=50)
def test_pascal::goto::statement_instantiation(instance):
    assert isinstance(instance, pascal::goto::statement)

@given(instance=pascal::function::designator_strategy)
@settings(max_examples=50)
def test_pascal::function::designator_instantiation(instance):
    assert isinstance(instance, pascal::function::designator)

@given(instance=pascal::function::designator_strategy)
def test_pascal::function::designator_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=pascal::function::designator_strategy)
def test_pascal::function::designator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pascal::assignment::statement_strategy)
@settings(max_examples=50)
def test_pascal::assignment::statement_instantiation(instance):
    assert isinstance(instance, pascal::assignment::statement)

@given(instance=pascal::structured::statement_strategy)
@settings(max_examples=50)
def test_pascal::structured::statement_instantiation(instance):
    assert isinstance(instance, pascal::structured::statement)

@given(instance=pascal::simple::statement_strategy)
@settings(max_examples=50)
def test_pascal::simple::statement_instantiation(instance):
    assert isinstance(instance, pascal::simple::statement)

@given(instance=pascal::simple::statement_strategy)
def test_pascal::simple::statement_function_noargs_type(instance):
    assert isinstance(instance.function_noargs, str)


@given(instance=pascal::simple::statement_strategy)
def test_pascal::simple::statement_function_noargs_setter(instance):
    original = instance.function_noargs
    instance.function_noargs = original
    assert instance.function_noargs == original

@given(instance=pascal::label_strategy)
@settings(max_examples=50)
def test_pascal::label_instantiation(instance):
    assert isinstance(instance, pascal::label)

@given(instance=pascal::label_strategy)
def test_pascal::label_number_type(instance):
    assert isinstance(instance.number, str)


@given(instance=pascal::label_strategy)
def test_pascal::label_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=pascal::statement_strategy)
@settings(max_examples=50)
def test_pascal::statement_instantiation(instance):
    assert isinstance(instance, pascal::statement)

@given(instance=pascal::statement::sequence_strategy)
@settings(max_examples=50)
def test_pascal::statement::sequence_instantiation(instance):
    assert isinstance(instance, pascal::statement::sequence)

@given(instance=pascal::statement::part_strategy)
@settings(max_examples=50)
def test_pascal::statement::part_instantiation(instance):
    assert isinstance(instance, pascal::statement::part)

@given(instance=pascal::procedure::and::function::declaration::part_strategy)
@settings(max_examples=50)
def test_pascal::procedure::and::function::declaration::part_instantiation(instance):
    assert isinstance(instance, pascal::procedure::and::function::declaration::part)

@given(instance=pascal::constant::definition::part_strategy)
@settings(max_examples=50)
def test_pascal::constant::definition::part_instantiation(instance):
    assert isinstance(instance, pascal::constant::definition::part)

@given(instance=pascal::label::declaration::part_strategy)
@settings(max_examples=50)
def test_pascal::label::declaration::part_instantiation(instance):
    assert isinstance(instance, pascal::label::declaration::part)

@given(instance=pascal::identifier::list_strategy)
@settings(max_examples=50)
def test_pascal::identifier::list_instantiation(instance):
    assert isinstance(instance, pascal::identifier::list)

@given(instance=pascal::identifier::list_strategy)
def test_pascal::identifier::list_names_type(instance):
    assert isinstance(instance.names, str)


@given(instance=pascal::identifier::list_strategy)
def test_pascal::identifier::list_names_setter(instance):
    original = instance.names
    instance.names = original
    assert instance.names == original

@given(instance=pascal::block_strategy)
@settings(max_examples=50)
def test_pascal::block_instantiation(instance):
    assert isinstance(instance, pascal::block)

@given(instance=pascal::program::heading::block_strategy)
@settings(max_examples=50)
def test_pascal::program::heading::block_instantiation(instance):
    assert isinstance(instance, pascal::program::heading::block)

@given(instance=pascal::program::heading::block_strategy)
def test_pascal::program::heading::block_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=pascal::program::heading::block_strategy)
def test_pascal::program::heading::block_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pascal::program_strategy)
@settings(max_examples=50)
def test_pascal::program_instantiation(instance):
    assert isinstance(instance, pascal::program)

@given(instance=pascal::pascal_strategy)
@settings(max_examples=50)
def test_pascal::pascal_instantiation(instance):
    assert isinstance(instance, pascal::pascal)
