import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    pascal::actual::parameter::list,
    pascal::identifier,
    pascal::Begin,
    pascal::label,
    pascal::statement,
    pascal::statement::sequence,
    pascal::function::block,
    pascal::statement::part,
    pascal::declaration::part,
    pascal::procedure::block,
    pascal::identifier::list,
    pascal::block,
    pascal::program::heading,
    pascal::program,
    pascal::bound::specification,
    pascal::unpacked::conformant::array::schema,
    pascal::packed::conformant::array::schema,
    pascal::conformant::array::schema,
    output::list,
    pascal::output::value,
    pascal::output::list,
    pascal::ordinal::type::identifier,
    pascal::formal::parameter::section,
    pascal::formal::parameter::list,
    pascal::parameter::type,
    pascal::result::type,
    pascal::function::parameter::section,
    pascal::procedure::parameter::section,
    pascal::variable::parameter::section,
    pascal::value::parameter::section,
    pascal::subrange::type,
    pascal::element::type,
    pascal::index::type,
    pascal::compiler::defined::directives,
    pascal::variable::declaration,
    pascal::upper::bound,
    pascal::lower::bound,
    pascal::enumerated::type,
    pascal::file::component::type,
    pascal::file::type,
    pascal::set::type,
    pascal::record::type,
    pascal::array::type,
    pascal::unpacked::structured::type,
    pascal::variant,
    pascal::tag::field,
    pascal::record::section,
    pascal::variant::part,
    pascal::fixed::part,
    pascal::field::list,
    pascal::base::type,
    pascal::function::identification,
    pascal::function::body,
    pascal::function::heading,
    pascal::procedure::identification,
    pascal::directive,
    pascal::type::identifier,
    pascal::pointer::type,
    pascal::structured::type,
    pascal::simple::type,
    pascal::type,
    pascal::type::definition,
    pascal::constant::definition,
    pascal::for::statement,
    pascal::repeat::statement,
    pascal::while::statement,
    pascal::procedure::body,
    pascal::procedure::heading,
    pascal::variable::declaration::part,
    pascal::type::definition::part,
    pascal::constant::definition::part,
    pascal::label::declaration::part,
    pascal::final::expression,
    pascal::initial::expression,
    pascal::expression::list,
    pascal::entire::variable,
    pascal::constant,
    pascal::case::label::list,
    pascal::case::limb,
    pascal::case::statement,
    pascal::if::statement,
    pascal::with::statement,
    pascal::conditional::statement,
    pascal::repetitive::statement,
    pascal::compound::statement,
    pascal::factor,
    pascal::addition::operator,
    pascal::term,
    pascal::simple::expression,
    pascal::scale::factor,
    pascal::digit::sequence,
    pascal::real::number,
    pascal::integer::number,
    pascal::element::list,
    pascal::function::designator,
    pascal::set,
    pascal::number,
    pascal::goto::statement,
    pascal::procedure::statement,
    pascal::assignment::statement,
    pascal::structured::statement,
    pascal::simple::statement,
    output::value,
    pascal::expression,
    pascal::variable,
    pascal::actual::function,
    pascal::actual::procedure,
    pascal::actual::variable,
    pascal::actual::value,
    pascal::actual::parameter,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pascal::actual::parameter::list_is_not_abstract():
    assert not inspect.isabstract(pascal::actual::parameter::list)


def test_pascal::actual::parameter::list_constructor_exists():
    assert callable(pascal::actual::parameter::list.__init__)


def test_pascal::actual::parameter::list_constructor_args():
    sig = inspect.signature(pascal::actual::parameter::list.__init__)
    params = list(sig.parameters.keys())



def test_pascal::identifier_is_not_abstract():
    assert not inspect.isabstract(pascal::identifier)


def test_pascal::identifier_constructor_exists():
    assert callable(pascal::identifier.__init__)


def test_pascal::identifier_constructor_args():
    sig = inspect.signature(pascal::identifier.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_pascal::identifier_has_identifier():
    assert hasattr(pascal::identifier, "identifier")
    descriptor = None
    for klass in pascal::identifier.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_pascal::begin_is_not_abstract():
    assert not inspect.isabstract(pascal::Begin)


def test_pascal::begin_constructor_exists():
    assert callable(pascal::Begin.__init__)


def test_pascal::begin_constructor_args():
    sig = inspect.signature(pascal::Begin.__init__)
    params = list(sig.parameters.keys())



def test_pascal::label_is_not_abstract():
    assert not inspect.isabstract(pascal::label)


def test_pascal::label_constructor_exists():
    assert callable(pascal::label.__init__)


def test_pascal::label_constructor_args():
    sig = inspect.signature(pascal::label.__init__)
    params = list(sig.parameters.keys())



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



def test_pascal::function::block_is_not_abstract():
    assert not inspect.isabstract(pascal::function::block)


def test_pascal::function::block_constructor_exists():
    assert callable(pascal::function::block.__init__)


def test_pascal::function::block_constructor_args():
    sig = inspect.signature(pascal::function::block.__init__)
    params = list(sig.parameters.keys())



def test_pascal::statement::part_is_not_abstract():
    assert not inspect.isabstract(pascal::statement::part)


def test_pascal::statement::part_constructor_exists():
    assert callable(pascal::statement::part.__init__)


def test_pascal::statement::part_constructor_args():
    sig = inspect.signature(pascal::statement::part.__init__)
    params = list(sig.parameters.keys())



def test_pascal::declaration::part_is_not_abstract():
    assert not inspect.isabstract(pascal::declaration::part)


def test_pascal::declaration::part_constructor_exists():
    assert callable(pascal::declaration::part.__init__)


def test_pascal::declaration::part_constructor_args():
    sig = inspect.signature(pascal::declaration::part.__init__)
    params = list(sig.parameters.keys())



def test_pascal::procedure::block_is_not_abstract():
    assert not inspect.isabstract(pascal::procedure::block)


def test_pascal::procedure::block_constructor_exists():
    assert callable(pascal::procedure::block.__init__)


def test_pascal::procedure::block_constructor_args():
    sig = inspect.signature(pascal::procedure::block.__init__)
    params = list(sig.parameters.keys())



def test_pascal::identifier::list_is_not_abstract():
    assert not inspect.isabstract(pascal::identifier::list)


def test_pascal::identifier::list_constructor_exists():
    assert callable(pascal::identifier::list.__init__)


def test_pascal::identifier::list_constructor_args():
    sig = inspect.signature(pascal::identifier::list.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_pascal::identifier::list_has_identifier():
    assert hasattr(pascal::identifier::list, "identifier")
    descriptor = None
    for klass in pascal::identifier::list.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_pascal::block_is_not_abstract():
    assert not inspect.isabstract(pascal::block)


def test_pascal::block_constructor_exists():
    assert callable(pascal::block.__init__)


def test_pascal::block_constructor_args():
    sig = inspect.signature(pascal::block.__init__)
    params = list(sig.parameters.keys())



def test_pascal::program::heading_is_not_abstract():
    assert not inspect.isabstract(pascal::program::heading)


def test_pascal::program::heading_constructor_exists():
    assert callable(pascal::program::heading.__init__)


def test_pascal::program::heading_constructor_args():
    sig = inspect.signature(pascal::program::heading.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_pascal::program::heading_has_identifier():
    assert hasattr(pascal::program::heading, "identifier")
    descriptor = None
    for klass in pascal::program::heading.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_pascal::program_is_not_abstract():
    assert not inspect.isabstract(pascal::program)


def test_pascal::program_constructor_exists():
    assert callable(pascal::program.__init__)


def test_pascal::program_constructor_args():
    sig = inspect.signature(pascal::program.__init__)
    params = list(sig.parameters.keys())



def test_pascal::bound::specification_is_not_abstract():
    assert not inspect.isabstract(pascal::bound::specification)


def test_pascal::bound::specification_constructor_exists():
    assert callable(pascal::bound::specification.__init__)


def test_pascal::bound::specification_constructor_args():
    sig = inspect.signature(pascal::bound::specification.__init__)
    params = list(sig.parameters.keys())



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



def test_pascal::conformant::array::schema_is_not_abstract():
    assert not inspect.isabstract(pascal::conformant::array::schema)


def test_pascal::conformant::array::schema_constructor_exists():
    assert callable(pascal::conformant::array::schema.__init__)


def test_pascal::conformant::array::schema_constructor_args():
    sig = inspect.signature(pascal::conformant::array::schema.__init__)
    params = list(sig.parameters.keys())



def test_output::list_is_not_abstract():
    assert not inspect.isabstract(output::list)


def test_output::list_constructor_exists():
    assert callable(output::list.__init__)


def test_output::list_constructor_args():
    sig = inspect.signature(output::list.__init__)
    params = list(sig.parameters.keys())



def test_pascal::output::value_is_not_abstract():
    assert not inspect.isabstract(pascal::output::value)


def test_pascal::output::value_constructor_exists():
    assert callable(pascal::output::value.__init__)


def test_pascal::output::value_constructor_args():
    sig = inspect.signature(pascal::output::value.__init__)
    params = list(sig.parameters.keys())



def test_pascal::output::list_is_not_abstract():
    assert not inspect.isabstract(pascal::output::list)


def test_pascal::output::list_constructor_exists():
    assert callable(pascal::output::list.__init__)


def test_pascal::output::list_constructor_args():
    sig = inspect.signature(pascal::output::list.__init__)
    params = list(sig.parameters.keys())



def test_pascal::ordinal::type::identifier_is_not_abstract():
    assert not inspect.isabstract(pascal::ordinal::type::identifier)


def test_pascal::ordinal::type::identifier_constructor_exists():
    assert callable(pascal::ordinal::type::identifier.__init__)


def test_pascal::ordinal::type::identifier_constructor_args():
    sig = inspect.signature(pascal::ordinal::type::identifier.__init__)
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



def test_pascal::parameter::type_is_not_abstract():
    assert not inspect.isabstract(pascal::parameter::type)


def test_pascal::parameter::type_constructor_exists():
    assert callable(pascal::parameter::type.__init__)


def test_pascal::parameter::type_constructor_args():
    sig = inspect.signature(pascal::parameter::type.__init__)
    params = list(sig.parameters.keys())



def test_pascal::result::type_is_not_abstract():
    assert not inspect.isabstract(pascal::result::type)


def test_pascal::result::type_constructor_exists():
    assert callable(pascal::result::type.__init__)


def test_pascal::result::type_constructor_args():
    sig = inspect.signature(pascal::result::type.__init__)
    params = list(sig.parameters.keys())



def test_pascal::function::parameter::section_is_not_abstract():
    assert not inspect.isabstract(pascal::function::parameter::section)


def test_pascal::function::parameter::section_constructor_exists():
    assert callable(pascal::function::parameter::section.__init__)


def test_pascal::function::parameter::section_constructor_args():
    sig = inspect.signature(pascal::function::parameter::section.__init__)
    params = list(sig.parameters.keys())



def test_pascal::procedure::parameter::section_is_not_abstract():
    assert not inspect.isabstract(pascal::procedure::parameter::section)


def test_pascal::procedure::parameter::section_constructor_exists():
    assert callable(pascal::procedure::parameter::section.__init__)


def test_pascal::procedure::parameter::section_constructor_args():
    sig = inspect.signature(pascal::procedure::parameter::section.__init__)
    params = list(sig.parameters.keys())



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



def test_pascal::subrange::type_is_not_abstract():
    assert not inspect.isabstract(pascal::subrange::type)


def test_pascal::subrange::type_constructor_exists():
    assert callable(pascal::subrange::type.__init__)


def test_pascal::subrange::type_constructor_args():
    sig = inspect.signature(pascal::subrange::type.__init__)
    params = list(sig.parameters.keys())



def test_pascal::element::type_is_not_abstract():
    assert not inspect.isabstract(pascal::element::type)


def test_pascal::element::type_constructor_exists():
    assert callable(pascal::element::type.__init__)


def test_pascal::element::type_constructor_args():
    sig = inspect.signature(pascal::element::type.__init__)
    params = list(sig.parameters.keys())



def test_pascal::index::type_is_not_abstract():
    assert not inspect.isabstract(pascal::index::type)


def test_pascal::index::type_constructor_exists():
    assert callable(pascal::index::type.__init__)


def test_pascal::index::type_constructor_args():
    sig = inspect.signature(pascal::index::type.__init__)
    params = list(sig.parameters.keys())



def test_pascal::compiler::defined::directives_is_not_abstract():
    assert not inspect.isabstract(pascal::compiler::defined::directives)


def test_pascal::compiler::defined::directives_constructor_exists():
    assert callable(pascal::compiler::defined::directives.__init__)


def test_pascal::compiler::defined::directives_constructor_args():
    sig = inspect.signature(pascal::compiler::defined::directives.__init__)
    params = list(sig.parameters.keys())



def test_pascal::variable::declaration_is_not_abstract():
    assert not inspect.isabstract(pascal::variable::declaration)


def test_pascal::variable::declaration_constructor_exists():
    assert callable(pascal::variable::declaration.__init__)


def test_pascal::variable::declaration_constructor_args():
    sig = inspect.signature(pascal::variable::declaration.__init__)
    params = list(sig.parameters.keys())



def test_pascal::upper::bound_is_not_abstract():
    assert not inspect.isabstract(pascal::upper::bound)


def test_pascal::upper::bound_constructor_exists():
    assert callable(pascal::upper::bound.__init__)


def test_pascal::upper::bound_constructor_args():
    sig = inspect.signature(pascal::upper::bound.__init__)
    params = list(sig.parameters.keys())



def test_pascal::lower::bound_is_not_abstract():
    assert not inspect.isabstract(pascal::lower::bound)


def test_pascal::lower::bound_constructor_exists():
    assert callable(pascal::lower::bound.__init__)


def test_pascal::lower::bound_constructor_args():
    sig = inspect.signature(pascal::lower::bound.__init__)
    params = list(sig.parameters.keys())



def test_pascal::enumerated::type_is_not_abstract():
    assert not inspect.isabstract(pascal::enumerated::type)


def test_pascal::enumerated::type_constructor_exists():
    assert callable(pascal::enumerated::type.__init__)


def test_pascal::enumerated::type_constructor_args():
    sig = inspect.signature(pascal::enumerated::type.__init__)
    params = list(sig.parameters.keys())



def test_pascal::file::component::type_is_not_abstract():
    assert not inspect.isabstract(pascal::file::component::type)


def test_pascal::file::component::type_constructor_exists():
    assert callable(pascal::file::component::type.__init__)


def test_pascal::file::component::type_constructor_args():
    sig = inspect.signature(pascal::file::component::type.__init__)
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



def test_pascal::record::section_is_not_abstract():
    assert not inspect.isabstract(pascal::record::section)


def test_pascal::record::section_constructor_exists():
    assert callable(pascal::record::section.__init__)


def test_pascal::record::section_constructor_args():
    sig = inspect.signature(pascal::record::section.__init__)
    params = list(sig.parameters.keys())



def test_pascal::variant::part_is_not_abstract():
    assert not inspect.isabstract(pascal::variant::part)


def test_pascal::variant::part_constructor_exists():
    assert callable(pascal::variant::part.__init__)


def test_pascal::variant::part_constructor_args():
    sig = inspect.signature(pascal::variant::part.__init__)
    params = list(sig.parameters.keys())



def test_pascal::fixed::part_is_not_abstract():
    assert not inspect.isabstract(pascal::fixed::part)


def test_pascal::fixed::part_constructor_exists():
    assert callable(pascal::fixed::part.__init__)


def test_pascal::fixed::part_constructor_args():
    sig = inspect.signature(pascal::fixed::part.__init__)
    params = list(sig.parameters.keys())



def test_pascal::field::list_is_not_abstract():
    assert not inspect.isabstract(pascal::field::list)


def test_pascal::field::list_constructor_exists():
    assert callable(pascal::field::list.__init__)


def test_pascal::field::list_constructor_args():
    sig = inspect.signature(pascal::field::list.__init__)
    params = list(sig.parameters.keys())



def test_pascal::base::type_is_not_abstract():
    assert not inspect.isabstract(pascal::base::type)


def test_pascal::base::type_constructor_exists():
    assert callable(pascal::base::type.__init__)


def test_pascal::base::type_constructor_args():
    sig = inspect.signature(pascal::base::type.__init__)
    params = list(sig.parameters.keys())



def test_pascal::function::identification_is_not_abstract():
    assert not inspect.isabstract(pascal::function::identification)


def test_pascal::function::identification_constructor_exists():
    assert callable(pascal::function::identification.__init__)


def test_pascal::function::identification_constructor_args():
    sig = inspect.signature(pascal::function::identification.__init__)
    params = list(sig.parameters.keys())



def test_pascal::function::body_is_not_abstract():
    assert not inspect.isabstract(pascal::function::body)


def test_pascal::function::body_constructor_exists():
    assert callable(pascal::function::body.__init__)


def test_pascal::function::body_constructor_args():
    sig = inspect.signature(pascal::function::body.__init__)
    params = list(sig.parameters.keys())



def test_pascal::function::heading_is_not_abstract():
    assert not inspect.isabstract(pascal::function::heading)


def test_pascal::function::heading_constructor_exists():
    assert callable(pascal::function::heading.__init__)


def test_pascal::function::heading_constructor_args():
    sig = inspect.signature(pascal::function::heading.__init__)
    params = list(sig.parameters.keys())



def test_pascal::procedure::identification_is_not_abstract():
    assert not inspect.isabstract(pascal::procedure::identification)


def test_pascal::procedure::identification_constructor_exists():
    assert callable(pascal::procedure::identification.__init__)


def test_pascal::procedure::identification_constructor_args():
    sig = inspect.signature(pascal::procedure::identification.__init__)
    params = list(sig.parameters.keys())



def test_pascal::directive_is_not_abstract():
    assert not inspect.isabstract(pascal::directive)


def test_pascal::directive_constructor_exists():
    assert callable(pascal::directive.__init__)


def test_pascal::directive_constructor_args():
    sig = inspect.signature(pascal::directive.__init__)
    params = list(sig.parameters.keys())



def test_pascal::type::identifier_is_not_abstract():
    assert not inspect.isabstract(pascal::type::identifier)


def test_pascal::type::identifier_constructor_exists():
    assert callable(pascal::type::identifier.__init__)


def test_pascal::type::identifier_constructor_args():
    sig = inspect.signature(pascal::type::identifier.__init__)
    params = list(sig.parameters.keys())



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



def test_pascal::simple::type_is_not_abstract():
    assert not inspect.isabstract(pascal::simple::type)


def test_pascal::simple::type_constructor_exists():
    assert callable(pascal::simple::type.__init__)


def test_pascal::simple::type_constructor_args():
    sig = inspect.signature(pascal::simple::type.__init__)
    params = list(sig.parameters.keys())



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



def test_pascal::constant::definition_is_not_abstract():
    assert not inspect.isabstract(pascal::constant::definition)


def test_pascal::constant::definition_constructor_exists():
    assert callable(pascal::constant::definition.__init__)


def test_pascal::constant::definition_constructor_args():
    sig = inspect.signature(pascal::constant::definition.__init__)
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



def test_pascal::procedure::body_is_not_abstract():
    assert not inspect.isabstract(pascal::procedure::body)


def test_pascal::procedure::body_constructor_exists():
    assert callable(pascal::procedure::body.__init__)


def test_pascal::procedure::body_constructor_args():
    sig = inspect.signature(pascal::procedure::body.__init__)
    params = list(sig.parameters.keys())



def test_pascal::procedure::heading_is_not_abstract():
    assert not inspect.isabstract(pascal::procedure::heading)


def test_pascal::procedure::heading_constructor_exists():
    assert callable(pascal::procedure::heading.__init__)


def test_pascal::procedure::heading_constructor_args():
    sig = inspect.signature(pascal::procedure::heading.__init__)
    params = list(sig.parameters.keys())



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



def test_pascal::final::expression_is_not_abstract():
    assert not inspect.isabstract(pascal::final::expression)


def test_pascal::final::expression_constructor_exists():
    assert callable(pascal::final::expression.__init__)


def test_pascal::final::expression_constructor_args():
    sig = inspect.signature(pascal::final::expression.__init__)
    params = list(sig.parameters.keys())



def test_pascal::initial::expression_is_not_abstract():
    assert not inspect.isabstract(pascal::initial::expression)


def test_pascal::initial::expression_constructor_exists():
    assert callable(pascal::initial::expression.__init__)


def test_pascal::initial::expression_constructor_args():
    sig = inspect.signature(pascal::initial::expression.__init__)
    params = list(sig.parameters.keys())



def test_pascal::expression::list_is_not_abstract():
    assert not inspect.isabstract(pascal::expression::list)


def test_pascal::expression::list_constructor_exists():
    assert callable(pascal::expression::list.__init__)


def test_pascal::expression::list_constructor_args():
    sig = inspect.signature(pascal::expression::list.__init__)
    params = list(sig.parameters.keys())



def test_pascal::entire::variable_is_not_abstract():
    assert not inspect.isabstract(pascal::entire::variable)


def test_pascal::entire::variable_constructor_exists():
    assert callable(pascal::entire::variable.__init__)


def test_pascal::entire::variable_constructor_args():
    sig = inspect.signature(pascal::entire::variable.__init__)
    params = list(sig.parameters.keys())



def test_pascal::constant_is_not_abstract():
    assert not inspect.isabstract(pascal::constant)


def test_pascal::constant_constructor_exists():
    assert callable(pascal::constant.__init__)


def test_pascal::constant_constructor_args():
    sig = inspect.signature(pascal::constant.__init__)
    params = list(sig.parameters.keys())
    assert "strings" in params, "Missing parameter 'strings'"
    assert "boolean" in params, "Missing parameter 'boolean'"
    assert "sign" in params, "Missing parameter 'sign'"

def test_pascal::constant_has_strings():
    assert hasattr(pascal::constant, "strings")
    descriptor = None
    for klass in pascal::constant.__mro__:
        if "strings" in klass.__dict__:
            descriptor = klass.__dict__["strings"]
            break
    assert isinstance(descriptor, property)

def test_pascal::constant_has_boolean():
    assert hasattr(pascal::constant, "boolean")
    descriptor = None
    for klass in pascal::constant.__mro__:
        if "boolean" in klass.__dict__:
            descriptor = klass.__dict__["boolean"]
            break
    assert isinstance(descriptor, property)

def test_pascal::constant_has_sign():
    assert hasattr(pascal::constant, "sign")
    descriptor = None
    for klass in pascal::constant.__mro__:
        if "sign" in klass.__dict__:
            descriptor = klass.__dict__["sign"]
            break
    assert isinstance(descriptor, property)



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



def test_pascal::compound::statement_is_not_abstract():
    assert not inspect.isabstract(pascal::compound::statement)


def test_pascal::compound::statement_constructor_exists():
    assert callable(pascal::compound::statement.__init__)


def test_pascal::compound::statement_constructor_args():
    sig = inspect.signature(pascal::compound::statement.__init__)
    params = list(sig.parameters.keys())



def test_pascal::factor_is_not_abstract():
    assert not inspect.isabstract(pascal::factor)


def test_pascal::factor_constructor_exists():
    assert callable(pascal::factor.__init__)


def test_pascal::factor_constructor_args():
    sig = inspect.signature(pascal::factor.__init__)
    params = list(sig.parameters.keys())
    assert "boolean" in params, "Missing parameter 'boolean'"
    assert "strings" in params, "Missing parameter 'strings'"

def test_pascal::factor_has_boolean():
    assert hasattr(pascal::factor, "boolean")
    descriptor = None
    for klass in pascal::factor.__mro__:
        if "boolean" in klass.__dict__:
            descriptor = klass.__dict__["boolean"]
            break
    assert isinstance(descriptor, property)

def test_pascal::factor_has_strings():
    assert hasattr(pascal::factor, "strings")
    descriptor = None
    for klass in pascal::factor.__mro__:
        if "strings" in klass.__dict__:
            descriptor = klass.__dict__["strings"]
            break
    assert isinstance(descriptor, property)



def test_pascal::addition::operator_is_not_abstract():
    assert not inspect.isabstract(pascal::addition::operator)


def test_pascal::addition::operator_constructor_exists():
    assert callable(pascal::addition::operator.__init__)


def test_pascal::addition::operator_constructor_args():
    sig = inspect.signature(pascal::addition::operator.__init__)
    params = list(sig.parameters.keys())
    assert "sign" in params, "Missing parameter 'sign'"

def test_pascal::addition::operator_has_sign():
    assert hasattr(pascal::addition::operator, "sign")
    descriptor = None
    for klass in pascal::addition::operator.__mro__:
        if "sign" in klass.__dict__:
            descriptor = klass.__dict__["sign"]
            break
    assert isinstance(descriptor, property)



def test_pascal::term_is_not_abstract():
    assert not inspect.isabstract(pascal::term)


def test_pascal::term_constructor_exists():
    assert callable(pascal::term.__init__)


def test_pascal::term_constructor_args():
    sig = inspect.signature(pascal::term.__init__)
    params = list(sig.parameters.keys())
    assert "multiplication_operator" in params, "Missing parameter 'multiplication_operator'"

def test_pascal::term_has_multiplication_operator():
    assert hasattr(pascal::term, "multiplication_operator")
    descriptor = None
    for klass in pascal::term.__mro__:
        if "multiplication_operator" in klass.__dict__:
            descriptor = klass.__dict__["multiplication_operator"]
            break
    assert isinstance(descriptor, property)



def test_pascal::simple::expression_is_not_abstract():
    assert not inspect.isabstract(pascal::simple::expression)


def test_pascal::simple::expression_constructor_exists():
    assert callable(pascal::simple::expression.__init__)


def test_pascal::simple::expression_constructor_args():
    sig = inspect.signature(pascal::simple::expression.__init__)
    params = list(sig.parameters.keys())
    assert "sign" in params, "Missing parameter 'sign'"

def test_pascal::simple::expression_has_sign():
    assert hasattr(pascal::simple::expression, "sign")
    descriptor = None
    for klass in pascal::simple::expression.__mro__:
        if "sign" in klass.__dict__:
            descriptor = klass.__dict__["sign"]
            break
    assert isinstance(descriptor, property)



def test_pascal::scale::factor_is_not_abstract():
    assert not inspect.isabstract(pascal::scale::factor)


def test_pascal::scale::factor_constructor_exists():
    assert callable(pascal::scale::factor.__init__)


def test_pascal::scale::factor_constructor_args():
    sig = inspect.signature(pascal::scale::factor.__init__)
    params = list(sig.parameters.keys())
    assert "sign" in params, "Missing parameter 'sign'"

def test_pascal::scale::factor_has_sign():
    assert hasattr(pascal::scale::factor, "sign")
    descriptor = None
    for klass in pascal::scale::factor.__mro__:
        if "sign" in klass.__dict__:
            descriptor = klass.__dict__["sign"]
            break
    assert isinstance(descriptor, property)



def test_pascal::digit::sequence_is_not_abstract():
    assert not inspect.isabstract(pascal::digit::sequence)


def test_pascal::digit::sequence_constructor_exists():
    assert callable(pascal::digit::sequence.__init__)


def test_pascal::digit::sequence_constructor_args():
    sig = inspect.signature(pascal::digit::sequence.__init__)
    params = list(sig.parameters.keys())
    assert "sign" in params, "Missing parameter 'sign'"
    assert "unsigned_digit_sequence" in params, "Missing parameter 'unsigned_digit_sequence'"

def test_pascal::digit::sequence_has_sign():
    assert hasattr(pascal::digit::sequence, "sign")
    descriptor = None
    for klass in pascal::digit::sequence.__mro__:
        if "sign" in klass.__dict__:
            descriptor = klass.__dict__["sign"]
            break
    assert isinstance(descriptor, property)

def test_pascal::digit::sequence_has_unsigned_digit_sequence():
    assert hasattr(pascal::digit::sequence, "unsigned_digit_sequence")
    descriptor = None
    for klass in pascal::digit::sequence.__mro__:
        if "unsigned_digit_sequence" in klass.__dict__:
            descriptor = klass.__dict__["unsigned_digit_sequence"]
            break
    assert isinstance(descriptor, property)



def test_pascal::real::number_is_not_abstract():
    assert not inspect.isabstract(pascal::real::number)


def test_pascal::real::number_constructor_exists():
    assert callable(pascal::real::number.__init__)


def test_pascal::real::number_constructor_args():
    sig = inspect.signature(pascal::real::number.__init__)
    params = list(sig.parameters.keys())



def test_pascal::integer::number_is_not_abstract():
    assert not inspect.isabstract(pascal::integer::number)


def test_pascal::integer::number_constructor_exists():
    assert callable(pascal::integer::number.__init__)


def test_pascal::integer::number_constructor_args():
    sig = inspect.signature(pascal::integer::number.__init__)
    params = list(sig.parameters.keys())



def test_pascal::element::list_is_not_abstract():
    assert not inspect.isabstract(pascal::element::list)


def test_pascal::element::list_constructor_exists():
    assert callable(pascal::element::list.__init__)


def test_pascal::element::list_constructor_args():
    sig = inspect.signature(pascal::element::list.__init__)
    params = list(sig.parameters.keys())



def test_pascal::function::designator_is_not_abstract():
    assert not inspect.isabstract(pascal::function::designator)


def test_pascal::function::designator_constructor_exists():
    assert callable(pascal::function::designator.__init__)


def test_pascal::function::designator_constructor_args():
    sig = inspect.signature(pascal::function::designator.__init__)
    params = list(sig.parameters.keys())



def test_pascal::set_is_not_abstract():
    assert not inspect.isabstract(pascal::set)


def test_pascal::set_constructor_exists():
    assert callable(pascal::set.__init__)


def test_pascal::set_constructor_args():
    sig = inspect.signature(pascal::set.__init__)
    params = list(sig.parameters.keys())



def test_pascal::number_is_not_abstract():
    assert not inspect.isabstract(pascal::number)


def test_pascal::number_constructor_exists():
    assert callable(pascal::number.__init__)


def test_pascal::number_constructor_args():
    sig = inspect.signature(pascal::number.__init__)
    params = list(sig.parameters.keys())



def test_pascal::goto::statement_is_not_abstract():
    assert not inspect.isabstract(pascal::goto::statement)


def test_pascal::goto::statement_constructor_exists():
    assert callable(pascal::goto::statement.__init__)


def test_pascal::goto::statement_constructor_args():
    sig = inspect.signature(pascal::goto::statement.__init__)
    params = list(sig.parameters.keys())



def test_pascal::procedure::statement_is_not_abstract():
    assert not inspect.isabstract(pascal::procedure::statement)


def test_pascal::procedure::statement_constructor_exists():
    assert callable(pascal::procedure::statement.__init__)


def test_pascal::procedure::statement_constructor_args():
    sig = inspect.signature(pascal::procedure::statement.__init__)
    params = list(sig.parameters.keys())



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



def test_output::value_is_not_abstract():
    assert not inspect.isabstract(output::value)


def test_output::value_constructor_exists():
    assert callable(output::value.__init__)


def test_output::value_constructor_args():
    sig = inspect.signature(output::value.__init__)
    params = list(sig.parameters.keys())



def test_pascal::expression_is_not_abstract():
    assert not inspect.isabstract(pascal::expression)


def test_pascal::expression_constructor_exists():
    assert callable(pascal::expression.__init__)


def test_pascal::expression_constructor_args():
    sig = inspect.signature(pascal::expression.__init__)
    params = list(sig.parameters.keys())
    assert "relational_operator" in params, "Missing parameter 'relational_operator'"

def test_pascal::expression_has_relational_operator():
    assert hasattr(pascal::expression, "relational_operator")
    descriptor = None
    for klass in pascal::expression.__mro__:
        if "relational_operator" in klass.__dict__:
            descriptor = klass.__dict__["relational_operator"]
            break
    assert isinstance(descriptor, property)



def test_pascal::variable_is_not_abstract():
    assert not inspect.isabstract(pascal::variable)


def test_pascal::variable_constructor_exists():
    assert callable(pascal::variable.__init__)


def test_pascal::variable_constructor_args():
    sig = inspect.signature(pascal::variable.__init__)
    params = list(sig.parameters.keys())



def test_pascal::actual::function_is_not_abstract():
    assert not inspect.isabstract(pascal::actual::function)


def test_pascal::actual::function_constructor_exists():
    assert callable(pascal::actual::function.__init__)


def test_pascal::actual::function_constructor_args():
    sig = inspect.signature(pascal::actual::function.__init__)
    params = list(sig.parameters.keys())



def test_pascal::actual::procedure_is_not_abstract():
    assert not inspect.isabstract(pascal::actual::procedure)


def test_pascal::actual::procedure_constructor_exists():
    assert callable(pascal::actual::procedure.__init__)


def test_pascal::actual::procedure_constructor_args():
    sig = inspect.signature(pascal::actual::procedure.__init__)
    params = list(sig.parameters.keys())



def test_pascal::actual::variable_is_not_abstract():
    assert not inspect.isabstract(pascal::actual::variable)


def test_pascal::actual::variable_constructor_exists():
    assert callable(pascal::actual::variable.__init__)


def test_pascal::actual::variable_constructor_args():
    sig = inspect.signature(pascal::actual::variable.__init__)
    params = list(sig.parameters.keys())



def test_pascal::actual::value_is_not_abstract():
    assert not inspect.isabstract(pascal::actual::value)


def test_pascal::actual::value_constructor_exists():
    assert callable(pascal::actual::value.__init__)


def test_pascal::actual::value_constructor_args():
    sig = inspect.signature(pascal::actual::value.__init__)
    params = list(sig.parameters.keys())



def test_pascal::actual::parameter_is_not_abstract():
    assert not inspect.isabstract(pascal::actual::parameter)


def test_pascal::actual::parameter_constructor_exists():
    assert callable(pascal::actual::parameter.__init__)


def test_pascal::actual::parameter_constructor_args():
    sig = inspect.signature(pascal::actual::parameter.__init__)
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
pascal::actual::parameter::list_strategy = st.builds(
    pascal::actual::parameter::list,
)
pascal::identifier_strategy = st.builds(
    pascal::identifier,
    identifier=
        safe_text
)
pascal::Begin_strategy = st.builds(
    pascal::Begin,
)
pascal::label_strategy = st.builds(
    pascal::label,
)
pascal::statement_strategy = st.builds(
    pascal::statement,
)
pascal::statement::sequence_strategy = st.builds(
    pascal::statement::sequence,
)
pascal::function::block_strategy = st.builds(
    pascal::function::block,
)
pascal::statement::part_strategy = st.builds(
    pascal::statement::part,
)
pascal::declaration::part_strategy = st.builds(
    pascal::declaration::part,
)
pascal::procedure::block_strategy = st.builds(
    pascal::procedure::block,
)
pascal::identifier::list_strategy = st.builds(
    pascal::identifier::list,
    identifier=
        safe_text
)
pascal::block_strategy = st.builds(
    pascal::block,
)
pascal::program::heading_strategy = st.builds(
    pascal::program::heading,
    identifier=
        safe_text
)
pascal::program_strategy = st.builds(
    pascal::program,
)
pascal::bound::specification_strategy = st.builds(
    pascal::bound::specification,
)
pascal::unpacked::conformant::array::schema_strategy = st.builds(
    pascal::unpacked::conformant::array::schema,
)
pascal::packed::conformant::array::schema_strategy = st.builds(
    pascal::packed::conformant::array::schema,
)
pascal::conformant::array::schema_strategy = st.builds(
    pascal::conformant::array::schema,
)
output::list_strategy = st.builds(
    output::list,
)
pascal::output::value_strategy = st.builds(
    pascal::output::value,
)
pascal::output::list_strategy = st.builds(
    pascal::output::list,
)
pascal::ordinal::type::identifier_strategy = st.builds(
    pascal::ordinal::type::identifier,
)
pascal::formal::parameter::section_strategy = st.builds(
    pascal::formal::parameter::section,
)
pascal::formal::parameter::list_strategy = st.builds(
    pascal::formal::parameter::list,
)
pascal::parameter::type_strategy = st.builds(
    pascal::parameter::type,
)
pascal::result::type_strategy = st.builds(
    pascal::result::type,
)
pascal::function::parameter::section_strategy = st.builds(
    pascal::function::parameter::section,
)
pascal::procedure::parameter::section_strategy = st.builds(
    pascal::procedure::parameter::section,
)
pascal::variable::parameter::section_strategy = st.builds(
    pascal::variable::parameter::section,
)
pascal::value::parameter::section_strategy = st.builds(
    pascal::value::parameter::section,
)
pascal::subrange::type_strategy = st.builds(
    pascal::subrange::type,
)
pascal::element::type_strategy = st.builds(
    pascal::element::type,
)
pascal::index::type_strategy = st.builds(
    pascal::index::type,
)
pascal::compiler::defined::directives_strategy = st.builds(
    pascal::compiler::defined::directives,
)
pascal::variable::declaration_strategy = st.builds(
    pascal::variable::declaration,
)
pascal::upper::bound_strategy = st.builds(
    pascal::upper::bound,
)
pascal::lower::bound_strategy = st.builds(
    pascal::lower::bound,
)
pascal::enumerated::type_strategy = st.builds(
    pascal::enumerated::type,
)
pascal::file::component::type_strategy = st.builds(
    pascal::file::component::type,
)
pascal::file::type_strategy = st.builds(
    pascal::file::type,
)
pascal::set::type_strategy = st.builds(
    pascal::set::type,
)
pascal::record::type_strategy = st.builds(
    pascal::record::type,
)
pascal::array::type_strategy = st.builds(
    pascal::array::type,
)
pascal::unpacked::structured::type_strategy = st.builds(
    pascal::unpacked::structured::type,
)
pascal::variant_strategy = st.builds(
    pascal::variant,
)
pascal::tag::field_strategy = st.builds(
    pascal::tag::field,
)
pascal::record::section_strategy = st.builds(
    pascal::record::section,
)
pascal::variant::part_strategy = st.builds(
    pascal::variant::part,
)
pascal::fixed::part_strategy = st.builds(
    pascal::fixed::part,
)
pascal::field::list_strategy = st.builds(
    pascal::field::list,
)
pascal::base::type_strategy = st.builds(
    pascal::base::type,
)
pascal::function::identification_strategy = st.builds(
    pascal::function::identification,
)
pascal::function::body_strategy = st.builds(
    pascal::function::body,
)
pascal::function::heading_strategy = st.builds(
    pascal::function::heading,
)
pascal::procedure::identification_strategy = st.builds(
    pascal::procedure::identification,
)
pascal::directive_strategy = st.builds(
    pascal::directive,
)
pascal::type::identifier_strategy = st.builds(
    pascal::type::identifier,
)
pascal::pointer::type_strategy = st.builds(
    pascal::pointer::type,
)
pascal::structured::type_strategy = st.builds(
    pascal::structured::type,
)
pascal::simple::type_strategy = st.builds(
    pascal::simple::type,
)
pascal::type_strategy = st.builds(
    pascal::type,
)
pascal::type::definition_strategy = st.builds(
    pascal::type::definition,
)
pascal::constant::definition_strategy = st.builds(
    pascal::constant::definition,
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
pascal::procedure::body_strategy = st.builds(
    pascal::procedure::body,
)
pascal::procedure::heading_strategy = st.builds(
    pascal::procedure::heading,
)
pascal::variable::declaration::part_strategy = st.builds(
    pascal::variable::declaration::part,
)
pascal::type::definition::part_strategy = st.builds(
    pascal::type::definition::part,
)
pascal::constant::definition::part_strategy = st.builds(
    pascal::constant::definition::part,
)
pascal::label::declaration::part_strategy = st.builds(
    pascal::label::declaration::part,
)
pascal::final::expression_strategy = st.builds(
    pascal::final::expression,
)
pascal::initial::expression_strategy = st.builds(
    pascal::initial::expression,
)
pascal::expression::list_strategy = st.builds(
    pascal::expression::list,
)
pascal::entire::variable_strategy = st.builds(
    pascal::entire::variable,
)
pascal::constant_strategy = st.builds(
    pascal::constant,
    strings=
        safe_text,
    boolean=
        safe_text,
    sign=
        safe_text
)
pascal::case::label::list_strategy = st.builds(
    pascal::case::label::list,
)
pascal::case::limb_strategy = st.builds(
    pascal::case::limb,
)
pascal::case::statement_strategy = st.builds(
    pascal::case::statement,
)
pascal::if::statement_strategy = st.builds(
    pascal::if::statement,
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
pascal::compound::statement_strategy = st.builds(
    pascal::compound::statement,
)
pascal::factor_strategy = st.builds(
    pascal::factor,
    boolean=
        safe_text,
    strings=
        safe_text
)
pascal::addition::operator_strategy = st.builds(
    pascal::addition::operator,
    sign=
        safe_text
)
pascal::term_strategy = st.builds(
    pascal::term,
    multiplication_operator=
        safe_text
)
pascal::simple::expression_strategy = st.builds(
    pascal::simple::expression,
    sign=
        safe_text
)
pascal::scale::factor_strategy = st.builds(
    pascal::scale::factor,
    sign=
        safe_text
)
pascal::digit::sequence_strategy = st.builds(
    pascal::digit::sequence,
    sign=
        safe_text,
    unsigned_digit_sequence=
        safe_text
)
pascal::real::number_strategy = st.builds(
    pascal::real::number,
)
pascal::integer::number_strategy = st.builds(
    pascal::integer::number,
)
pascal::element::list_strategy = st.builds(
    pascal::element::list,
)
pascal::function::designator_strategy = st.builds(
    pascal::function::designator,
)
pascal::set_strategy = st.builds(
    pascal::set,
)
pascal::number_strategy = st.builds(
    pascal::number,
)
pascal::goto::statement_strategy = st.builds(
    pascal::goto::statement,
)
pascal::procedure::statement_strategy = st.builds(
    pascal::procedure::statement,
)
pascal::assignment::statement_strategy = st.builds(
    pascal::assignment::statement,
)
pascal::structured::statement_strategy = st.builds(
    pascal::structured::statement,
)
pascal::simple::statement_strategy = st.builds(
    pascal::simple::statement,
)
output::value_strategy = st.builds(
    output::value,
)
pascal::expression_strategy = st.builds(
    pascal::expression,
    relational_operator=
        safe_text
)
pascal::variable_strategy = st.builds(
    pascal::variable,
)
pascal::actual::function_strategy = st.builds(
    pascal::actual::function,
)
pascal::actual::procedure_strategy = st.builds(
    pascal::actual::procedure,
)
pascal::actual::variable_strategy = st.builds(
    pascal::actual::variable,
)
pascal::actual::value_strategy = st.builds(
    pascal::actual::value,
)
pascal::actual::parameter_strategy = st.builds(
    pascal::actual::parameter,
)

@given(instance=pascal::actual::parameter::list_strategy)
@settings(max_examples=50)
def test_pascal::actual::parameter::list_instantiation(instance):
    assert isinstance(instance, pascal::actual::parameter::list)

@given(instance=pascal::identifier_strategy)
@settings(max_examples=50)
def test_pascal::identifier_instantiation(instance):
    assert isinstance(instance, pascal::identifier)

@given(instance=pascal::identifier_strategy)
def test_pascal::identifier_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=pascal::identifier_strategy)
def test_pascal::identifier_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=pascal::Begin_strategy)
@settings(max_examples=50)
def test_pascal::begin_instantiation(instance):
    assert isinstance(instance, pascal::Begin)

@given(instance=pascal::label_strategy)
@settings(max_examples=50)
def test_pascal::label_instantiation(instance):
    assert isinstance(instance, pascal::label)

@given(instance=pascal::statement_strategy)
@settings(max_examples=50)
def test_pascal::statement_instantiation(instance):
    assert isinstance(instance, pascal::statement)

@given(instance=pascal::statement::sequence_strategy)
@settings(max_examples=50)
def test_pascal::statement::sequence_instantiation(instance):
    assert isinstance(instance, pascal::statement::sequence)

@given(instance=pascal::function::block_strategy)
@settings(max_examples=50)
def test_pascal::function::block_instantiation(instance):
    assert isinstance(instance, pascal::function::block)

@given(instance=pascal::statement::part_strategy)
@settings(max_examples=50)
def test_pascal::statement::part_instantiation(instance):
    assert isinstance(instance, pascal::statement::part)

@given(instance=pascal::declaration::part_strategy)
@settings(max_examples=50)
def test_pascal::declaration::part_instantiation(instance):
    assert isinstance(instance, pascal::declaration::part)

@given(instance=pascal::procedure::block_strategy)
@settings(max_examples=50)
def test_pascal::procedure::block_instantiation(instance):
    assert isinstance(instance, pascal::procedure::block)

@given(instance=pascal::identifier::list_strategy)
@settings(max_examples=50)
def test_pascal::identifier::list_instantiation(instance):
    assert isinstance(instance, pascal::identifier::list)

@given(instance=pascal::identifier::list_strategy)
def test_pascal::identifier::list_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=pascal::identifier::list_strategy)
def test_pascal::identifier::list_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=pascal::block_strategy)
@settings(max_examples=50)
def test_pascal::block_instantiation(instance):
    assert isinstance(instance, pascal::block)

@given(instance=pascal::program::heading_strategy)
@settings(max_examples=50)
def test_pascal::program::heading_instantiation(instance):
    assert isinstance(instance, pascal::program::heading)

@given(instance=pascal::program::heading_strategy)
def test_pascal::program::heading_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=pascal::program::heading_strategy)
def test_pascal::program::heading_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=pascal::program_strategy)
@settings(max_examples=50)
def test_pascal::program_instantiation(instance):
    assert isinstance(instance, pascal::program)

@given(instance=pascal::bound::specification_strategy)
@settings(max_examples=50)
def test_pascal::bound::specification_instantiation(instance):
    assert isinstance(instance, pascal::bound::specification)

@given(instance=pascal::unpacked::conformant::array::schema_strategy)
@settings(max_examples=50)
def test_pascal::unpacked::conformant::array::schema_instantiation(instance):
    assert isinstance(instance, pascal::unpacked::conformant::array::schema)

@given(instance=pascal::packed::conformant::array::schema_strategy)
@settings(max_examples=50)
def test_pascal::packed::conformant::array::schema_instantiation(instance):
    assert isinstance(instance, pascal::packed::conformant::array::schema)

@given(instance=pascal::conformant::array::schema_strategy)
@settings(max_examples=50)
def test_pascal::conformant::array::schema_instantiation(instance):
    assert isinstance(instance, pascal::conformant::array::schema)

@given(instance=output::list_strategy)
@settings(max_examples=50)
def test_output::list_instantiation(instance):
    assert isinstance(instance, output::list)

@given(instance=pascal::output::value_strategy)
@settings(max_examples=50)
def test_pascal::output::value_instantiation(instance):
    assert isinstance(instance, pascal::output::value)

@given(instance=pascal::output::list_strategy)
@settings(max_examples=50)
def test_pascal::output::list_instantiation(instance):
    assert isinstance(instance, pascal::output::list)

@given(instance=pascal::ordinal::type::identifier_strategy)
@settings(max_examples=50)
def test_pascal::ordinal::type::identifier_instantiation(instance):
    assert isinstance(instance, pascal::ordinal::type::identifier)

@given(instance=pascal::formal::parameter::section_strategy)
@settings(max_examples=50)
def test_pascal::formal::parameter::section_instantiation(instance):
    assert isinstance(instance, pascal::formal::parameter::section)

@given(instance=pascal::formal::parameter::list_strategy)
@settings(max_examples=50)
def test_pascal::formal::parameter::list_instantiation(instance):
    assert isinstance(instance, pascal::formal::parameter::list)

@given(instance=pascal::parameter::type_strategy)
@settings(max_examples=50)
def test_pascal::parameter::type_instantiation(instance):
    assert isinstance(instance, pascal::parameter::type)

@given(instance=pascal::result::type_strategy)
@settings(max_examples=50)
def test_pascal::result::type_instantiation(instance):
    assert isinstance(instance, pascal::result::type)

@given(instance=pascal::function::parameter::section_strategy)
@settings(max_examples=50)
def test_pascal::function::parameter::section_instantiation(instance):
    assert isinstance(instance, pascal::function::parameter::section)

@given(instance=pascal::procedure::parameter::section_strategy)
@settings(max_examples=50)
def test_pascal::procedure::parameter::section_instantiation(instance):
    assert isinstance(instance, pascal::procedure::parameter::section)

@given(instance=pascal::variable::parameter::section_strategy)
@settings(max_examples=50)
def test_pascal::variable::parameter::section_instantiation(instance):
    assert isinstance(instance, pascal::variable::parameter::section)

@given(instance=pascal::value::parameter::section_strategy)
@settings(max_examples=50)
def test_pascal::value::parameter::section_instantiation(instance):
    assert isinstance(instance, pascal::value::parameter::section)

@given(instance=pascal::subrange::type_strategy)
@settings(max_examples=50)
def test_pascal::subrange::type_instantiation(instance):
    assert isinstance(instance, pascal::subrange::type)

@given(instance=pascal::element::type_strategy)
@settings(max_examples=50)
def test_pascal::element::type_instantiation(instance):
    assert isinstance(instance, pascal::element::type)

@given(instance=pascal::index::type_strategy)
@settings(max_examples=50)
def test_pascal::index::type_instantiation(instance):
    assert isinstance(instance, pascal::index::type)

@given(instance=pascal::compiler::defined::directives_strategy)
@settings(max_examples=50)
def test_pascal::compiler::defined::directives_instantiation(instance):
    assert isinstance(instance, pascal::compiler::defined::directives)

@given(instance=pascal::variable::declaration_strategy)
@settings(max_examples=50)
def test_pascal::variable::declaration_instantiation(instance):
    assert isinstance(instance, pascal::variable::declaration)

@given(instance=pascal::upper::bound_strategy)
@settings(max_examples=50)
def test_pascal::upper::bound_instantiation(instance):
    assert isinstance(instance, pascal::upper::bound)

@given(instance=pascal::lower::bound_strategy)
@settings(max_examples=50)
def test_pascal::lower::bound_instantiation(instance):
    assert isinstance(instance, pascal::lower::bound)

@given(instance=pascal::enumerated::type_strategy)
@settings(max_examples=50)
def test_pascal::enumerated::type_instantiation(instance):
    assert isinstance(instance, pascal::enumerated::type)

@given(instance=pascal::file::component::type_strategy)
@settings(max_examples=50)
def test_pascal::file::component::type_instantiation(instance):
    assert isinstance(instance, pascal::file::component::type)

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

@given(instance=pascal::array::type_strategy)
@settings(max_examples=50)
def test_pascal::array::type_instantiation(instance):
    assert isinstance(instance, pascal::array::type)

@given(instance=pascal::unpacked::structured::type_strategy)
@settings(max_examples=50)
def test_pascal::unpacked::structured::type_instantiation(instance):
    assert isinstance(instance, pascal::unpacked::structured::type)

@given(instance=pascal::variant_strategy)
@settings(max_examples=50)
def test_pascal::variant_instantiation(instance):
    assert isinstance(instance, pascal::variant)

@given(instance=pascal::tag::field_strategy)
@settings(max_examples=50)
def test_pascal::tag::field_instantiation(instance):
    assert isinstance(instance, pascal::tag::field)

@given(instance=pascal::record::section_strategy)
@settings(max_examples=50)
def test_pascal::record::section_instantiation(instance):
    assert isinstance(instance, pascal::record::section)

@given(instance=pascal::variant::part_strategy)
@settings(max_examples=50)
def test_pascal::variant::part_instantiation(instance):
    assert isinstance(instance, pascal::variant::part)

@given(instance=pascal::fixed::part_strategy)
@settings(max_examples=50)
def test_pascal::fixed::part_instantiation(instance):
    assert isinstance(instance, pascal::fixed::part)

@given(instance=pascal::field::list_strategy)
@settings(max_examples=50)
def test_pascal::field::list_instantiation(instance):
    assert isinstance(instance, pascal::field::list)

@given(instance=pascal::base::type_strategy)
@settings(max_examples=50)
def test_pascal::base::type_instantiation(instance):
    assert isinstance(instance, pascal::base::type)

@given(instance=pascal::function::identification_strategy)
@settings(max_examples=50)
def test_pascal::function::identification_instantiation(instance):
    assert isinstance(instance, pascal::function::identification)

@given(instance=pascal::function::body_strategy)
@settings(max_examples=50)
def test_pascal::function::body_instantiation(instance):
    assert isinstance(instance, pascal::function::body)

@given(instance=pascal::function::heading_strategy)
@settings(max_examples=50)
def test_pascal::function::heading_instantiation(instance):
    assert isinstance(instance, pascal::function::heading)

@given(instance=pascal::procedure::identification_strategy)
@settings(max_examples=50)
def test_pascal::procedure::identification_instantiation(instance):
    assert isinstance(instance, pascal::procedure::identification)

@given(instance=pascal::directive_strategy)
@settings(max_examples=50)
def test_pascal::directive_instantiation(instance):
    assert isinstance(instance, pascal::directive)

@given(instance=pascal::type::identifier_strategy)
@settings(max_examples=50)
def test_pascal::type::identifier_instantiation(instance):
    assert isinstance(instance, pascal::type::identifier)

@given(instance=pascal::pointer::type_strategy)
@settings(max_examples=50)
def test_pascal::pointer::type_instantiation(instance):
    assert isinstance(instance, pascal::pointer::type)

@given(instance=pascal::structured::type_strategy)
@settings(max_examples=50)
def test_pascal::structured::type_instantiation(instance):
    assert isinstance(instance, pascal::structured::type)

@given(instance=pascal::simple::type_strategy)
@settings(max_examples=50)
def test_pascal::simple::type_instantiation(instance):
    assert isinstance(instance, pascal::simple::type)

@given(instance=pascal::type_strategy)
@settings(max_examples=50)
def test_pascal::type_instantiation(instance):
    assert isinstance(instance, pascal::type)

@given(instance=pascal::type::definition_strategy)
@settings(max_examples=50)
def test_pascal::type::definition_instantiation(instance):
    assert isinstance(instance, pascal::type::definition)

@given(instance=pascal::constant::definition_strategy)
@settings(max_examples=50)
def test_pascal::constant::definition_instantiation(instance):
    assert isinstance(instance, pascal::constant::definition)

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

@given(instance=pascal::procedure::body_strategy)
@settings(max_examples=50)
def test_pascal::procedure::body_instantiation(instance):
    assert isinstance(instance, pascal::procedure::body)

@given(instance=pascal::procedure::heading_strategy)
@settings(max_examples=50)
def test_pascal::procedure::heading_instantiation(instance):
    assert isinstance(instance, pascal::procedure::heading)

@given(instance=pascal::variable::declaration::part_strategy)
@settings(max_examples=50)
def test_pascal::variable::declaration::part_instantiation(instance):
    assert isinstance(instance, pascal::variable::declaration::part)

@given(instance=pascal::type::definition::part_strategy)
@settings(max_examples=50)
def test_pascal::type::definition::part_instantiation(instance):
    assert isinstance(instance, pascal::type::definition::part)

@given(instance=pascal::constant::definition::part_strategy)
@settings(max_examples=50)
def test_pascal::constant::definition::part_instantiation(instance):
    assert isinstance(instance, pascal::constant::definition::part)

@given(instance=pascal::label::declaration::part_strategy)
@settings(max_examples=50)
def test_pascal::label::declaration::part_instantiation(instance):
    assert isinstance(instance, pascal::label::declaration::part)

@given(instance=pascal::final::expression_strategy)
@settings(max_examples=50)
def test_pascal::final::expression_instantiation(instance):
    assert isinstance(instance, pascal::final::expression)

@given(instance=pascal::initial::expression_strategy)
@settings(max_examples=50)
def test_pascal::initial::expression_instantiation(instance):
    assert isinstance(instance, pascal::initial::expression)

@given(instance=pascal::expression::list_strategy)
@settings(max_examples=50)
def test_pascal::expression::list_instantiation(instance):
    assert isinstance(instance, pascal::expression::list)

@given(instance=pascal::entire::variable_strategy)
@settings(max_examples=50)
def test_pascal::entire::variable_instantiation(instance):
    assert isinstance(instance, pascal::entire::variable)

@given(instance=pascal::constant_strategy)
@settings(max_examples=50)
def test_pascal::constant_instantiation(instance):
    assert isinstance(instance, pascal::constant)

@given(instance=pascal::constant_strategy)
def test_pascal::constant_strings_type(instance):
    assert isinstance(instance.strings, str)


@given(instance=pascal::constant_strategy)
def test_pascal::constant_strings_setter(instance):
    original = instance.strings
    instance.strings = original
    assert instance.strings == original

@given(instance=pascal::constant_strategy)
def test_pascal::constant_boolean_type(instance):
    assert isinstance(instance.boolean, str)


@given(instance=pascal::constant_strategy)
def test_pascal::constant_boolean_setter(instance):
    original = instance.boolean
    instance.boolean = original
    assert instance.boolean == original

@given(instance=pascal::constant_strategy)
def test_pascal::constant_sign_type(instance):
    assert isinstance(instance.sign, str)


@given(instance=pascal::constant_strategy)
def test_pascal::constant_sign_setter(instance):
    original = instance.sign
    instance.sign = original
    assert instance.sign == original

@given(instance=pascal::case::label::list_strategy)
@settings(max_examples=50)
def test_pascal::case::label::list_instantiation(instance):
    assert isinstance(instance, pascal::case::label::list)

@given(instance=pascal::case::limb_strategy)
@settings(max_examples=50)
def test_pascal::case::limb_instantiation(instance):
    assert isinstance(instance, pascal::case::limb)

@given(instance=pascal::case::statement_strategy)
@settings(max_examples=50)
def test_pascal::case::statement_instantiation(instance):
    assert isinstance(instance, pascal::case::statement)

@given(instance=pascal::if::statement_strategy)
@settings(max_examples=50)
def test_pascal::if::statement_instantiation(instance):
    assert isinstance(instance, pascal::if::statement)

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

@given(instance=pascal::compound::statement_strategy)
@settings(max_examples=50)
def test_pascal::compound::statement_instantiation(instance):
    assert isinstance(instance, pascal::compound::statement)

@given(instance=pascal::factor_strategy)
@settings(max_examples=50)
def test_pascal::factor_instantiation(instance):
    assert isinstance(instance, pascal::factor)

@given(instance=pascal::factor_strategy)
def test_pascal::factor_boolean_type(instance):
    assert isinstance(instance.boolean, str)


@given(instance=pascal::factor_strategy)
def test_pascal::factor_boolean_setter(instance):
    original = instance.boolean
    instance.boolean = original
    assert instance.boolean == original

@given(instance=pascal::factor_strategy)
def test_pascal::factor_strings_type(instance):
    assert isinstance(instance.strings, str)


@given(instance=pascal::factor_strategy)
def test_pascal::factor_strings_setter(instance):
    original = instance.strings
    instance.strings = original
    assert instance.strings == original

@given(instance=pascal::addition::operator_strategy)
@settings(max_examples=50)
def test_pascal::addition::operator_instantiation(instance):
    assert isinstance(instance, pascal::addition::operator)

@given(instance=pascal::addition::operator_strategy)
def test_pascal::addition::operator_sign_type(instance):
    assert isinstance(instance.sign, str)


@given(instance=pascal::addition::operator_strategy)
def test_pascal::addition::operator_sign_setter(instance):
    original = instance.sign
    instance.sign = original
    assert instance.sign == original

@given(instance=pascal::term_strategy)
@settings(max_examples=50)
def test_pascal::term_instantiation(instance):
    assert isinstance(instance, pascal::term)

@given(instance=pascal::term_strategy)
def test_pascal::term_multiplication_operator_type(instance):
    assert isinstance(instance.multiplication_operator, str)


@given(instance=pascal::term_strategy)
def test_pascal::term_multiplication_operator_setter(instance):
    original = instance.multiplication_operator
    instance.multiplication_operator = original
    assert instance.multiplication_operator == original

@given(instance=pascal::simple::expression_strategy)
@settings(max_examples=50)
def test_pascal::simple::expression_instantiation(instance):
    assert isinstance(instance, pascal::simple::expression)

@given(instance=pascal::simple::expression_strategy)
def test_pascal::simple::expression_sign_type(instance):
    assert isinstance(instance.sign, str)


@given(instance=pascal::simple::expression_strategy)
def test_pascal::simple::expression_sign_setter(instance):
    original = instance.sign
    instance.sign = original
    assert instance.sign == original

@given(instance=pascal::scale::factor_strategy)
@settings(max_examples=50)
def test_pascal::scale::factor_instantiation(instance):
    assert isinstance(instance, pascal::scale::factor)

@given(instance=pascal::scale::factor_strategy)
def test_pascal::scale::factor_sign_type(instance):
    assert isinstance(instance.sign, str)


@given(instance=pascal::scale::factor_strategy)
def test_pascal::scale::factor_sign_setter(instance):
    original = instance.sign
    instance.sign = original
    assert instance.sign == original

@given(instance=pascal::digit::sequence_strategy)
@settings(max_examples=50)
def test_pascal::digit::sequence_instantiation(instance):
    assert isinstance(instance, pascal::digit::sequence)

@given(instance=pascal::digit::sequence_strategy)
def test_pascal::digit::sequence_sign_type(instance):
    assert isinstance(instance.sign, str)


@given(instance=pascal::digit::sequence_strategy)
def test_pascal::digit::sequence_sign_setter(instance):
    original = instance.sign
    instance.sign = original
    assert instance.sign == original

@given(instance=pascal::digit::sequence_strategy)
def test_pascal::digit::sequence_unsigned_digit_sequence_type(instance):
    assert isinstance(instance.unsigned_digit_sequence, str)


@given(instance=pascal::digit::sequence_strategy)
def test_pascal::digit::sequence_unsigned_digit_sequence_setter(instance):
    original = instance.unsigned_digit_sequence
    instance.unsigned_digit_sequence = original
    assert instance.unsigned_digit_sequence == original

@given(instance=pascal::real::number_strategy)
@settings(max_examples=50)
def test_pascal::real::number_instantiation(instance):
    assert isinstance(instance, pascal::real::number)

@given(instance=pascal::integer::number_strategy)
@settings(max_examples=50)
def test_pascal::integer::number_instantiation(instance):
    assert isinstance(instance, pascal::integer::number)

@given(instance=pascal::element::list_strategy)
@settings(max_examples=50)
def test_pascal::element::list_instantiation(instance):
    assert isinstance(instance, pascal::element::list)

@given(instance=pascal::function::designator_strategy)
@settings(max_examples=50)
def test_pascal::function::designator_instantiation(instance):
    assert isinstance(instance, pascal::function::designator)

@given(instance=pascal::set_strategy)
@settings(max_examples=50)
def test_pascal::set_instantiation(instance):
    assert isinstance(instance, pascal::set)

@given(instance=pascal::number_strategy)
@settings(max_examples=50)
def test_pascal::number_instantiation(instance):
    assert isinstance(instance, pascal::number)

@given(instance=pascal::goto::statement_strategy)
@settings(max_examples=50)
def test_pascal::goto::statement_instantiation(instance):
    assert isinstance(instance, pascal::goto::statement)

@given(instance=pascal::procedure::statement_strategy)
@settings(max_examples=50)
def test_pascal::procedure::statement_instantiation(instance):
    assert isinstance(instance, pascal::procedure::statement)

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

@given(instance=output::value_strategy)
@settings(max_examples=50)
def test_output::value_instantiation(instance):
    assert isinstance(instance, output::value)

@given(instance=pascal::expression_strategy)
@settings(max_examples=50)
def test_pascal::expression_instantiation(instance):
    assert isinstance(instance, pascal::expression)

@given(instance=pascal::expression_strategy)
def test_pascal::expression_relational_operator_type(instance):
    assert isinstance(instance.relational_operator, str)


@given(instance=pascal::expression_strategy)
def test_pascal::expression_relational_operator_setter(instance):
    original = instance.relational_operator
    instance.relational_operator = original
    assert instance.relational_operator == original

@given(instance=pascal::variable_strategy)
@settings(max_examples=50)
def test_pascal::variable_instantiation(instance):
    assert isinstance(instance, pascal::variable)

@given(instance=pascal::actual::function_strategy)
@settings(max_examples=50)
def test_pascal::actual::function_instantiation(instance):
    assert isinstance(instance, pascal::actual::function)

@given(instance=pascal::actual::procedure_strategy)
@settings(max_examples=50)
def test_pascal::actual::procedure_instantiation(instance):
    assert isinstance(instance, pascal::actual::procedure)

@given(instance=pascal::actual::variable_strategy)
@settings(max_examples=50)
def test_pascal::actual::variable_instantiation(instance):
    assert isinstance(instance, pascal::actual::variable)

@given(instance=pascal::actual::value_strategy)
@settings(max_examples=50)
def test_pascal::actual::value_instantiation(instance):
    assert isinstance(instance, pascal::actual::value)

@given(instance=pascal::actual::parameter_strategy)
@settings(max_examples=50)
def test_pascal::actual::parameter_instantiation(instance):
    assert isinstance(instance, pascal::actual::parameter)
