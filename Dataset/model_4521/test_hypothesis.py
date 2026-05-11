import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    tortugaDSL::BOOLEAN::EXPRESSION,
    FontStyleValues,
    tortugaDSL::ITALIC,
    tortugaDSL::PLAIN,
    tortugaDSL::BOLD,
    BOOLEAN::EXPRESSION,
    tortugaDSL::GREATER::THAN,
    tortugaDSL::LESSER::THAN,
    tortugaDSL::EQUALS,
    EXPRESSION,
    tortugaDSL::VALUE,
    CONTROL::SENTENCES,
    tortugaDSL::TO,
    tortugaDSL::IF,
    tortugaDSL::REPEAT,
    OPERATION,
    tortugaDSL::MULTIPLY,
    tortugaDSL::DIVIDE,
    tortugaDSL::SUBTRACT,
    tortugaDSL::SUM,
    COLOREABLE,
    tortugaDSL::CANVAS::COLOR,
    tortugaDSL::PENCOLOR,
    tortugaDSL::VARIABLE::REF,
    tortugaDSL::COLOR::SPEC,
    REFERENCIABLE,
    tortugaDSL::PARAM,
    tortugaDSL::REFERENCIABLE,
    tortugaDSL::FontStyleValues,
    FONT::SPEC,
    tortugaDSL::FONT::STYLE,
    tortugaDSL::FONT::SIZE,
    tortugaDSL::TortugaProgram,
    DRAWING::SENTENCE,
    tortugaDSL::DRAW::STRING,
    tortugaDSL::FONT::SPEC,
    tortugaDSL::HOME,
    tortugaDSL::PENUP,
    tortugaDSL::COLOREABLE,
    tortugaDSL::CLEAR,
    tortugaDSL::PENDOWN,
    MOVE,
    tortugaDSL::SET::Y,
    tortugaDSL::LEFT,
    tortugaDSL::RIGHT,
    tortugaDSL::SET::X,
    tortugaDSL::FORWARD,
    tortugaDSL::EXPRESSION,
    SENTENCE,
    tortugaDSL::CONTROL::SENTENCES,
    tortugaDSL::MAKE,
    tortugaDSL::PROCEDURE::CALL,
    tortugaDSL::DRAWING::SENTENCE,
    tortugaDSL::CONTENT,
    tortugaDSL::OPERATION,
    tortugaDSL::MOVE,
    tortugaDSL::SENTENCE,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tortugadsl::boolean::expression_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::BOOLEAN::EXPRESSION)


def test_tortugadsl::boolean::expression_constructor_exists():
    assert callable(tortugaDSL::BOOLEAN::EXPRESSION.__init__)


def test_tortugadsl::boolean::expression_constructor_args():
    sig = inspect.signature(tortugaDSL::BOOLEAN::EXPRESSION.__init__)
    params = list(sig.parameters.keys())



def test_fontstylevalues_is_not_abstract():
    assert not inspect.isabstract(FontStyleValues)


def test_fontstylevalues_constructor_exists():
    assert callable(FontStyleValues.__init__)


def test_fontstylevalues_constructor_args():
    sig = inspect.signature(FontStyleValues.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::italic_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::ITALIC)


def test_tortugadsl::italic_constructor_exists():
    assert callable(tortugaDSL::ITALIC.__init__)


def test_tortugadsl::italic_constructor_args():
    sig = inspect.signature(tortugaDSL::ITALIC.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::plain_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::PLAIN)


def test_tortugadsl::plain_constructor_exists():
    assert callable(tortugaDSL::PLAIN.__init__)


def test_tortugadsl::plain_constructor_args():
    sig = inspect.signature(tortugaDSL::PLAIN.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::bold_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::BOLD)


def test_tortugadsl::bold_constructor_exists():
    assert callable(tortugaDSL::BOLD.__init__)


def test_tortugadsl::bold_constructor_args():
    sig = inspect.signature(tortugaDSL::BOLD.__init__)
    params = list(sig.parameters.keys())



def test_boolean::expression_is_not_abstract():
    assert not inspect.isabstract(BOOLEAN::EXPRESSION)


def test_boolean::expression_constructor_exists():
    assert callable(BOOLEAN::EXPRESSION.__init__)


def test_boolean::expression_constructor_args():
    sig = inspect.signature(BOOLEAN::EXPRESSION.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::greater::than_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::GREATER::THAN)


def test_tortugadsl::greater::than_constructor_exists():
    assert callable(tortugaDSL::GREATER::THAN.__init__)


def test_tortugadsl::greater::than_constructor_args():
    sig = inspect.signature(tortugaDSL::GREATER::THAN.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::lesser::than_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::LESSER::THAN)


def test_tortugadsl::lesser::than_constructor_exists():
    assert callable(tortugaDSL::LESSER::THAN.__init__)


def test_tortugadsl::lesser::than_constructor_args():
    sig = inspect.signature(tortugaDSL::LESSER::THAN.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::equals_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::EQUALS)


def test_tortugadsl::equals_constructor_exists():
    assert callable(tortugaDSL::EQUALS.__init__)


def test_tortugadsl::equals_constructor_args():
    sig = inspect.signature(tortugaDSL::EQUALS.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(EXPRESSION)


def test_expression_constructor_exists():
    assert callable(EXPRESSION.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(EXPRESSION.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::value_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::VALUE)


def test_tortugadsl::value_constructor_exists():
    assert callable(tortugaDSL::VALUE.__init__)


def test_tortugadsl::value_constructor_args():
    sig = inspect.signature(tortugaDSL::VALUE.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_tortugadsl::value_has_val():
    assert hasattr(tortugaDSL::VALUE, "val")
    descriptor = None
    for klass in tortugaDSL::VALUE.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_control::sentences_is_not_abstract():
    assert not inspect.isabstract(CONTROL::SENTENCES)


def test_control::sentences_constructor_exists():
    assert callable(CONTROL::SENTENCES.__init__)


def test_control::sentences_constructor_args():
    sig = inspect.signature(CONTROL::SENTENCES.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::to_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::TO)


def test_tortugadsl::to_constructor_exists():
    assert callable(tortugaDSL::TO.__init__)


def test_tortugadsl::to_constructor_args():
    sig = inspect.signature(tortugaDSL::TO.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tortugadsl::to_has_name():
    assert hasattr(tortugaDSL::TO, "name")
    descriptor = None
    for klass in tortugaDSL::TO.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tortugadsl::if_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::IF)


def test_tortugadsl::if_constructor_exists():
    assert callable(tortugaDSL::IF.__init__)


def test_tortugadsl::if_constructor_args():
    sig = inspect.signature(tortugaDSL::IF.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::repeat_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::REPEAT)


def test_tortugadsl::repeat_constructor_exists():
    assert callable(tortugaDSL::REPEAT.__init__)


def test_tortugadsl::repeat_constructor_args():
    sig = inspect.signature(tortugaDSL::REPEAT.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(OPERATION)


def test_operation_constructor_exists():
    assert callable(OPERATION.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(OPERATION.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::multiply_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::MULTIPLY)


def test_tortugadsl::multiply_constructor_exists():
    assert callable(tortugaDSL::MULTIPLY.__init__)


def test_tortugadsl::multiply_constructor_args():
    sig = inspect.signature(tortugaDSL::MULTIPLY.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::divide_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::DIVIDE)


def test_tortugadsl::divide_constructor_exists():
    assert callable(tortugaDSL::DIVIDE.__init__)


def test_tortugadsl::divide_constructor_args():
    sig = inspect.signature(tortugaDSL::DIVIDE.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::subtract_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::SUBTRACT)


def test_tortugadsl::subtract_constructor_exists():
    assert callable(tortugaDSL::SUBTRACT.__init__)


def test_tortugadsl::subtract_constructor_args():
    sig = inspect.signature(tortugaDSL::SUBTRACT.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::sum_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::SUM)


def test_tortugadsl::sum_constructor_exists():
    assert callable(tortugaDSL::SUM.__init__)


def test_tortugadsl::sum_constructor_args():
    sig = inspect.signature(tortugaDSL::SUM.__init__)
    params = list(sig.parameters.keys())



def test_coloreable_is_not_abstract():
    assert not inspect.isabstract(COLOREABLE)


def test_coloreable_constructor_exists():
    assert callable(COLOREABLE.__init__)


def test_coloreable_constructor_args():
    sig = inspect.signature(COLOREABLE.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::canvas::color_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::CANVAS::COLOR)


def test_tortugadsl::canvas::color_constructor_exists():
    assert callable(tortugaDSL::CANVAS::COLOR.__init__)


def test_tortugadsl::canvas::color_constructor_args():
    sig = inspect.signature(tortugaDSL::CANVAS::COLOR.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::pencolor_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::PENCOLOR)


def test_tortugadsl::pencolor_constructor_exists():
    assert callable(tortugaDSL::PENCOLOR.__init__)


def test_tortugadsl::pencolor_constructor_args():
    sig = inspect.signature(tortugaDSL::PENCOLOR.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::variable::ref_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::VARIABLE::REF)


def test_tortugadsl::variable::ref_constructor_exists():
    assert callable(tortugaDSL::VARIABLE::REF.__init__)


def test_tortugadsl::variable::ref_constructor_args():
    sig = inspect.signature(tortugaDSL::VARIABLE::REF.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::color::spec_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::COLOR::SPEC)


def test_tortugadsl::color::spec_constructor_exists():
    assert callable(tortugaDSL::COLOR::SPEC.__init__)


def test_tortugadsl::color::spec_constructor_args():
    sig = inspect.signature(tortugaDSL::COLOR::SPEC.__init__)
    params = list(sig.parameters.keys())



def test_referenciable_is_not_abstract():
    assert not inspect.isabstract(REFERENCIABLE)


def test_referenciable_constructor_exists():
    assert callable(REFERENCIABLE.__init__)


def test_referenciable_constructor_args():
    sig = inspect.signature(REFERENCIABLE.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::param_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::PARAM)


def test_tortugadsl::param_constructor_exists():
    assert callable(tortugaDSL::PARAM.__init__)


def test_tortugadsl::param_constructor_args():
    sig = inspect.signature(tortugaDSL::PARAM.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::referenciable_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::REFERENCIABLE)


def test_tortugadsl::referenciable_constructor_exists():
    assert callable(tortugaDSL::REFERENCIABLE.__init__)


def test_tortugadsl::referenciable_constructor_args():
    sig = inspect.signature(tortugaDSL::REFERENCIABLE.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tortugadsl::referenciable_has_name():
    assert hasattr(tortugaDSL::REFERENCIABLE, "name")
    descriptor = None
    for klass in tortugaDSL::REFERENCIABLE.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tortugadsl::fontstylevalues_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::FontStyleValues)


def test_tortugadsl::fontstylevalues_constructor_exists():
    assert callable(tortugaDSL::FontStyleValues.__init__)


def test_tortugadsl::fontstylevalues_constructor_args():
    sig = inspect.signature(tortugaDSL::FontStyleValues.__init__)
    params = list(sig.parameters.keys())



def test_font::spec_is_not_abstract():
    assert not inspect.isabstract(FONT::SPEC)


def test_font::spec_constructor_exists():
    assert callable(FONT::SPEC.__init__)


def test_font::spec_constructor_args():
    sig = inspect.signature(FONT::SPEC.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::font::style_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::FONT::STYLE)


def test_tortugadsl::font::style_constructor_exists():
    assert callable(tortugaDSL::FONT::STYLE.__init__)


def test_tortugadsl::font::style_constructor_args():
    sig = inspect.signature(tortugaDSL::FONT::STYLE.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::font::size_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::FONT::SIZE)


def test_tortugadsl::font::size_constructor_exists():
    assert callable(tortugaDSL::FONT::SIZE.__init__)


def test_tortugadsl::font::size_constructor_args():
    sig = inspect.signature(tortugaDSL::FONT::SIZE.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::tortugaprogram_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::TortugaProgram)


def test_tortugadsl::tortugaprogram_constructor_exists():
    assert callable(tortugaDSL::TortugaProgram.__init__)


def test_tortugadsl::tortugaprogram_constructor_args():
    sig = inspect.signature(tortugaDSL::TortugaProgram.__init__)
    params = list(sig.parameters.keys())



def test_drawing::sentence_is_not_abstract():
    assert not inspect.isabstract(DRAWING::SENTENCE)


def test_drawing::sentence_constructor_exists():
    assert callable(DRAWING::SENTENCE.__init__)


def test_drawing::sentence_constructor_args():
    sig = inspect.signature(DRAWING::SENTENCE.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::draw::string_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::DRAW::STRING)


def test_tortugadsl::draw::string_constructor_exists():
    assert callable(tortugaDSL::DRAW::STRING.__init__)


def test_tortugadsl::draw::string_constructor_args():
    sig = inspect.signature(tortugaDSL::DRAW::STRING.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_tortugadsl::draw::string_has_text():
    assert hasattr(tortugaDSL::DRAW::STRING, "text")
    descriptor = None
    for klass in tortugaDSL::DRAW::STRING.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_tortugadsl::font::spec_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::FONT::SPEC)


def test_tortugadsl::font::spec_constructor_exists():
    assert callable(tortugaDSL::FONT::SPEC.__init__)


def test_tortugadsl::font::spec_constructor_args():
    sig = inspect.signature(tortugaDSL::FONT::SPEC.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::home_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::HOME)


def test_tortugadsl::home_constructor_exists():
    assert callable(tortugaDSL::HOME.__init__)


def test_tortugadsl::home_constructor_args():
    sig = inspect.signature(tortugaDSL::HOME.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::penup_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::PENUP)


def test_tortugadsl::penup_constructor_exists():
    assert callable(tortugaDSL::PENUP.__init__)


def test_tortugadsl::penup_constructor_args():
    sig = inspect.signature(tortugaDSL::PENUP.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::coloreable_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::COLOREABLE)


def test_tortugadsl::coloreable_constructor_exists():
    assert callable(tortugaDSL::COLOREABLE.__init__)


def test_tortugadsl::coloreable_constructor_args():
    sig = inspect.signature(tortugaDSL::COLOREABLE.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"

def test_tortugadsl::coloreable_has_color():
    assert hasattr(tortugaDSL::COLOREABLE, "color")
    descriptor = None
    for klass in tortugaDSL::COLOREABLE.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_tortugadsl::clear_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::CLEAR)


def test_tortugadsl::clear_constructor_exists():
    assert callable(tortugaDSL::CLEAR.__init__)


def test_tortugadsl::clear_constructor_args():
    sig = inspect.signature(tortugaDSL::CLEAR.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::pendown_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::PENDOWN)


def test_tortugadsl::pendown_constructor_exists():
    assert callable(tortugaDSL::PENDOWN.__init__)


def test_tortugadsl::pendown_constructor_args():
    sig = inspect.signature(tortugaDSL::PENDOWN.__init__)
    params = list(sig.parameters.keys())



def test_move_is_not_abstract():
    assert not inspect.isabstract(MOVE)


def test_move_constructor_exists():
    assert callable(MOVE.__init__)


def test_move_constructor_args():
    sig = inspect.signature(MOVE.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::set::y_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::SET::Y)


def test_tortugadsl::set::y_constructor_exists():
    assert callable(tortugaDSL::SET::Y.__init__)


def test_tortugadsl::set::y_constructor_args():
    sig = inspect.signature(tortugaDSL::SET::Y.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::left_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::LEFT)


def test_tortugadsl::left_constructor_exists():
    assert callable(tortugaDSL::LEFT.__init__)


def test_tortugadsl::left_constructor_args():
    sig = inspect.signature(tortugaDSL::LEFT.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::right_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::RIGHT)


def test_tortugadsl::right_constructor_exists():
    assert callable(tortugaDSL::RIGHT.__init__)


def test_tortugadsl::right_constructor_args():
    sig = inspect.signature(tortugaDSL::RIGHT.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::set::x_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::SET::X)


def test_tortugadsl::set::x_constructor_exists():
    assert callable(tortugaDSL::SET::X.__init__)


def test_tortugadsl::set::x_constructor_args():
    sig = inspect.signature(tortugaDSL::SET::X.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::forward_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::FORWARD)


def test_tortugadsl::forward_constructor_exists():
    assert callable(tortugaDSL::FORWARD.__init__)


def test_tortugadsl::forward_constructor_args():
    sig = inspect.signature(tortugaDSL::FORWARD.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::expression_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::EXPRESSION)


def test_tortugadsl::expression_constructor_exists():
    assert callable(tortugaDSL::EXPRESSION.__init__)


def test_tortugadsl::expression_constructor_args():
    sig = inspect.signature(tortugaDSL::EXPRESSION.__init__)
    params = list(sig.parameters.keys())



def test_sentence_is_not_abstract():
    assert not inspect.isabstract(SENTENCE)


def test_sentence_constructor_exists():
    assert callable(SENTENCE.__init__)


def test_sentence_constructor_args():
    sig = inspect.signature(SENTENCE.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::control::sentences_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::CONTROL::SENTENCES)


def test_tortugadsl::control::sentences_constructor_exists():
    assert callable(tortugaDSL::CONTROL::SENTENCES.__init__)


def test_tortugadsl::control::sentences_constructor_args():
    sig = inspect.signature(tortugaDSL::CONTROL::SENTENCES.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::make_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::MAKE)


def test_tortugadsl::make_constructor_exists():
    assert callable(tortugaDSL::MAKE.__init__)


def test_tortugadsl::make_constructor_args():
    sig = inspect.signature(tortugaDSL::MAKE.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::procedure::call_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::PROCEDURE::CALL)


def test_tortugadsl::procedure::call_constructor_exists():
    assert callable(tortugaDSL::PROCEDURE::CALL.__init__)


def test_tortugadsl::procedure::call_constructor_args():
    sig = inspect.signature(tortugaDSL::PROCEDURE::CALL.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::drawing::sentence_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::DRAWING::SENTENCE)


def test_tortugadsl::drawing::sentence_constructor_exists():
    assert callable(tortugaDSL::DRAWING::SENTENCE.__init__)


def test_tortugadsl::drawing::sentence_constructor_args():
    sig = inspect.signature(tortugaDSL::DRAWING::SENTENCE.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::content_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::CONTENT)


def test_tortugadsl::content_constructor_exists():
    assert callable(tortugaDSL::CONTENT.__init__)


def test_tortugadsl::content_constructor_args():
    sig = inspect.signature(tortugaDSL::CONTENT.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::operation_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::OPERATION)


def test_tortugadsl::operation_constructor_exists():
    assert callable(tortugaDSL::OPERATION.__init__)


def test_tortugadsl::operation_constructor_args():
    sig = inspect.signature(tortugaDSL::OPERATION.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::move_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::MOVE)


def test_tortugadsl::move_constructor_exists():
    assert callable(tortugaDSL::MOVE.__init__)


def test_tortugadsl::move_constructor_args():
    sig = inspect.signature(tortugaDSL::MOVE.__init__)
    params = list(sig.parameters.keys())



def test_tortugadsl::sentence_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL::SENTENCE)


def test_tortugadsl::sentence_constructor_exists():
    assert callable(tortugaDSL::SENTENCE.__init__)


def test_tortugadsl::sentence_constructor_args():
    sig = inspect.signature(tortugaDSL::SENTENCE.__init__)
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
tortugaDSL::BOOLEAN::EXPRESSION_strategy = st.builds(
    tortugaDSL::BOOLEAN::EXPRESSION,
)
FontStyleValues_strategy = st.builds(
    FontStyleValues,
)
tortugaDSL::ITALIC_strategy = st.builds(
    tortugaDSL::ITALIC,
)
tortugaDSL::PLAIN_strategy = st.builds(
    tortugaDSL::PLAIN,
)
tortugaDSL::BOLD_strategy = st.builds(
    tortugaDSL::BOLD,
)
BOOLEAN::EXPRESSION_strategy = st.builds(
    BOOLEAN::EXPRESSION,
)
tortugaDSL::GREATER::THAN_strategy = st.builds(
    tortugaDSL::GREATER::THAN,
)
tortugaDSL::LESSER::THAN_strategy = st.builds(
    tortugaDSL::LESSER::THAN,
)
tortugaDSL::EQUALS_strategy = st.builds(
    tortugaDSL::EQUALS,
)
EXPRESSION_strategy = st.builds(
    EXPRESSION,
)
tortugaDSL::VALUE_strategy = st.builds(
    tortugaDSL::VALUE,
    val=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
CONTROL::SENTENCES_strategy = st.builds(
    CONTROL::SENTENCES,
)
tortugaDSL::TO_strategy = st.builds(
    tortugaDSL::TO,
    name=
        safe_text
)
tortugaDSL::IF_strategy = st.builds(
    tortugaDSL::IF,
)
tortugaDSL::REPEAT_strategy = st.builds(
    tortugaDSL::REPEAT,
)
OPERATION_strategy = st.builds(
    OPERATION,
)
tortugaDSL::MULTIPLY_strategy = st.builds(
    tortugaDSL::MULTIPLY,
)
tortugaDSL::DIVIDE_strategy = st.builds(
    tortugaDSL::DIVIDE,
)
tortugaDSL::SUBTRACT_strategy = st.builds(
    tortugaDSL::SUBTRACT,
)
tortugaDSL::SUM_strategy = st.builds(
    tortugaDSL::SUM,
)
COLOREABLE_strategy = st.builds(
    COLOREABLE,
)
tortugaDSL::CANVAS::COLOR_strategy = st.builds(
    tortugaDSL::CANVAS::COLOR,
)
tortugaDSL::PENCOLOR_strategy = st.builds(
    tortugaDSL::PENCOLOR,
)
tortugaDSL::VARIABLE::REF_strategy = st.builds(
    tortugaDSL::VARIABLE::REF,
)
tortugaDSL::COLOR::SPEC_strategy = st.builds(
    tortugaDSL::COLOR::SPEC,
)
REFERENCIABLE_strategy = st.builds(
    REFERENCIABLE,
)
tortugaDSL::PARAM_strategy = st.builds(
    tortugaDSL::PARAM,
)
tortugaDSL::REFERENCIABLE_strategy = st.builds(
    tortugaDSL::REFERENCIABLE,
    name=
        safe_text
)
tortugaDSL::FontStyleValues_strategy = st.builds(
    tortugaDSL::FontStyleValues,
)
FONT::SPEC_strategy = st.builds(
    FONT::SPEC,
)
tortugaDSL::FONT::STYLE_strategy = st.builds(
    tortugaDSL::FONT::STYLE,
)
tortugaDSL::FONT::SIZE_strategy = st.builds(
    tortugaDSL::FONT::SIZE,
)
tortugaDSL::TortugaProgram_strategy = st.builds(
    tortugaDSL::TortugaProgram,
)
DRAWING::SENTENCE_strategy = st.builds(
    DRAWING::SENTENCE,
)
tortugaDSL::DRAW::STRING_strategy = st.builds(
    tortugaDSL::DRAW::STRING,
    text=
        safe_text
)
tortugaDSL::FONT::SPEC_strategy = st.builds(
    tortugaDSL::FONT::SPEC,
)
tortugaDSL::HOME_strategy = st.builds(
    tortugaDSL::HOME,
)
tortugaDSL::PENUP_strategy = st.builds(
    tortugaDSL::PENUP,
)
tortugaDSL::COLOREABLE_strategy = st.builds(
    tortugaDSL::COLOREABLE,
    color=
        safe_text
)
tortugaDSL::CLEAR_strategy = st.builds(
    tortugaDSL::CLEAR,
)
tortugaDSL::PENDOWN_strategy = st.builds(
    tortugaDSL::PENDOWN,
)
MOVE_strategy = st.builds(
    MOVE,
)
tortugaDSL::SET::Y_strategy = st.builds(
    tortugaDSL::SET::Y,
)
tortugaDSL::LEFT_strategy = st.builds(
    tortugaDSL::LEFT,
)
tortugaDSL::RIGHT_strategy = st.builds(
    tortugaDSL::RIGHT,
)
tortugaDSL::SET::X_strategy = st.builds(
    tortugaDSL::SET::X,
)
tortugaDSL::FORWARD_strategy = st.builds(
    tortugaDSL::FORWARD,
)
tortugaDSL::EXPRESSION_strategy = st.builds(
    tortugaDSL::EXPRESSION,
)
SENTENCE_strategy = st.builds(
    SENTENCE,
)
tortugaDSL::CONTROL::SENTENCES_strategy = st.builds(
    tortugaDSL::CONTROL::SENTENCES,
)
tortugaDSL::MAKE_strategy = st.builds(
    tortugaDSL::MAKE,
)
tortugaDSL::PROCEDURE::CALL_strategy = st.builds(
    tortugaDSL::PROCEDURE::CALL,
)
tortugaDSL::DRAWING::SENTENCE_strategy = st.builds(
    tortugaDSL::DRAWING::SENTENCE,
)
tortugaDSL::CONTENT_strategy = st.builds(
    tortugaDSL::CONTENT,
)
tortugaDSL::OPERATION_strategy = st.builds(
    tortugaDSL::OPERATION,
)
tortugaDSL::MOVE_strategy = st.builds(
    tortugaDSL::MOVE,
)
tortugaDSL::SENTENCE_strategy = st.builds(
    tortugaDSL::SENTENCE,
)

@given(instance=tortugaDSL::BOOLEAN::EXPRESSION_strategy)
@settings(max_examples=50)
def test_tortugadsl::boolean::expression_instantiation(instance):
    assert isinstance(instance, tortugaDSL::BOOLEAN::EXPRESSION)

@given(instance=FontStyleValues_strategy)
@settings(max_examples=50)
def test_fontstylevalues_instantiation(instance):
    assert isinstance(instance, FontStyleValues)

@given(instance=tortugaDSL::ITALIC_strategy)
@settings(max_examples=50)
def test_tortugadsl::italic_instantiation(instance):
    assert isinstance(instance, tortugaDSL::ITALIC)

@given(instance=tortugaDSL::PLAIN_strategy)
@settings(max_examples=50)
def test_tortugadsl::plain_instantiation(instance):
    assert isinstance(instance, tortugaDSL::PLAIN)

@given(instance=tortugaDSL::BOLD_strategy)
@settings(max_examples=50)
def test_tortugadsl::bold_instantiation(instance):
    assert isinstance(instance, tortugaDSL::BOLD)

@given(instance=BOOLEAN::EXPRESSION_strategy)
@settings(max_examples=50)
def test_boolean::expression_instantiation(instance):
    assert isinstance(instance, BOOLEAN::EXPRESSION)

@given(instance=tortugaDSL::GREATER::THAN_strategy)
@settings(max_examples=50)
def test_tortugadsl::greater::than_instantiation(instance):
    assert isinstance(instance, tortugaDSL::GREATER::THAN)

@given(instance=tortugaDSL::LESSER::THAN_strategy)
@settings(max_examples=50)
def test_tortugadsl::lesser::than_instantiation(instance):
    assert isinstance(instance, tortugaDSL::LESSER::THAN)

@given(instance=tortugaDSL::EQUALS_strategy)
@settings(max_examples=50)
def test_tortugadsl::equals_instantiation(instance):
    assert isinstance(instance, tortugaDSL::EQUALS)

@given(instance=EXPRESSION_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, EXPRESSION)

@given(instance=tortugaDSL::VALUE_strategy)
@settings(max_examples=50)
def test_tortugadsl::value_instantiation(instance):
    assert isinstance(instance, tortugaDSL::VALUE)

@given(instance=tortugaDSL::VALUE_strategy)
def test_tortugadsl::value_val_type(instance):
    assert isinstance(instance.val, float)


@given(instance=tortugaDSL::VALUE_strategy)
def test_tortugadsl::value_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=CONTROL::SENTENCES_strategy)
@settings(max_examples=50)
def test_control::sentences_instantiation(instance):
    assert isinstance(instance, CONTROL::SENTENCES)

@given(instance=tortugaDSL::TO_strategy)
@settings(max_examples=50)
def test_tortugadsl::to_instantiation(instance):
    assert isinstance(instance, tortugaDSL::TO)

@given(instance=tortugaDSL::TO_strategy)
def test_tortugadsl::to_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tortugaDSL::TO_strategy)
def test_tortugadsl::to_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tortugaDSL::IF_strategy)
@settings(max_examples=50)
def test_tortugadsl::if_instantiation(instance):
    assert isinstance(instance, tortugaDSL::IF)

@given(instance=tortugaDSL::REPEAT_strategy)
@settings(max_examples=50)
def test_tortugadsl::repeat_instantiation(instance):
    assert isinstance(instance, tortugaDSL::REPEAT)

@given(instance=OPERATION_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, OPERATION)

@given(instance=tortugaDSL::MULTIPLY_strategy)
@settings(max_examples=50)
def test_tortugadsl::multiply_instantiation(instance):
    assert isinstance(instance, tortugaDSL::MULTIPLY)

@given(instance=tortugaDSL::DIVIDE_strategy)
@settings(max_examples=50)
def test_tortugadsl::divide_instantiation(instance):
    assert isinstance(instance, tortugaDSL::DIVIDE)

@given(instance=tortugaDSL::SUBTRACT_strategy)
@settings(max_examples=50)
def test_tortugadsl::subtract_instantiation(instance):
    assert isinstance(instance, tortugaDSL::SUBTRACT)

@given(instance=tortugaDSL::SUM_strategy)
@settings(max_examples=50)
def test_tortugadsl::sum_instantiation(instance):
    assert isinstance(instance, tortugaDSL::SUM)

@given(instance=COLOREABLE_strategy)
@settings(max_examples=50)
def test_coloreable_instantiation(instance):
    assert isinstance(instance, COLOREABLE)

@given(instance=tortugaDSL::CANVAS::COLOR_strategy)
@settings(max_examples=50)
def test_tortugadsl::canvas::color_instantiation(instance):
    assert isinstance(instance, tortugaDSL::CANVAS::COLOR)

@given(instance=tortugaDSL::PENCOLOR_strategy)
@settings(max_examples=50)
def test_tortugadsl::pencolor_instantiation(instance):
    assert isinstance(instance, tortugaDSL::PENCOLOR)

@given(instance=tortugaDSL::VARIABLE::REF_strategy)
@settings(max_examples=50)
def test_tortugadsl::variable::ref_instantiation(instance):
    assert isinstance(instance, tortugaDSL::VARIABLE::REF)

@given(instance=tortugaDSL::COLOR::SPEC_strategy)
@settings(max_examples=50)
def test_tortugadsl::color::spec_instantiation(instance):
    assert isinstance(instance, tortugaDSL::COLOR::SPEC)

@given(instance=REFERENCIABLE_strategy)
@settings(max_examples=50)
def test_referenciable_instantiation(instance):
    assert isinstance(instance, REFERENCIABLE)

@given(instance=tortugaDSL::PARAM_strategy)
@settings(max_examples=50)
def test_tortugadsl::param_instantiation(instance):
    assert isinstance(instance, tortugaDSL::PARAM)

@given(instance=tortugaDSL::REFERENCIABLE_strategy)
@settings(max_examples=50)
def test_tortugadsl::referenciable_instantiation(instance):
    assert isinstance(instance, tortugaDSL::REFERENCIABLE)

@given(instance=tortugaDSL::REFERENCIABLE_strategy)
def test_tortugadsl::referenciable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tortugaDSL::REFERENCIABLE_strategy)
def test_tortugadsl::referenciable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tortugaDSL::FontStyleValues_strategy)
@settings(max_examples=50)
def test_tortugadsl::fontstylevalues_instantiation(instance):
    assert isinstance(instance, tortugaDSL::FontStyleValues)

@given(instance=FONT::SPEC_strategy)
@settings(max_examples=50)
def test_font::spec_instantiation(instance):
    assert isinstance(instance, FONT::SPEC)

@given(instance=tortugaDSL::FONT::STYLE_strategy)
@settings(max_examples=50)
def test_tortugadsl::font::style_instantiation(instance):
    assert isinstance(instance, tortugaDSL::FONT::STYLE)

@given(instance=tortugaDSL::FONT::SIZE_strategy)
@settings(max_examples=50)
def test_tortugadsl::font::size_instantiation(instance):
    assert isinstance(instance, tortugaDSL::FONT::SIZE)

@given(instance=tortugaDSL::TortugaProgram_strategy)
@settings(max_examples=50)
def test_tortugadsl::tortugaprogram_instantiation(instance):
    assert isinstance(instance, tortugaDSL::TortugaProgram)

@given(instance=DRAWING::SENTENCE_strategy)
@settings(max_examples=50)
def test_drawing::sentence_instantiation(instance):
    assert isinstance(instance, DRAWING::SENTENCE)

@given(instance=tortugaDSL::DRAW::STRING_strategy)
@settings(max_examples=50)
def test_tortugadsl::draw::string_instantiation(instance):
    assert isinstance(instance, tortugaDSL::DRAW::STRING)

@given(instance=tortugaDSL::DRAW::STRING_strategy)
def test_tortugadsl::draw::string_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=tortugaDSL::DRAW::STRING_strategy)
def test_tortugadsl::draw::string_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=tortugaDSL::FONT::SPEC_strategy)
@settings(max_examples=50)
def test_tortugadsl::font::spec_instantiation(instance):
    assert isinstance(instance, tortugaDSL::FONT::SPEC)

@given(instance=tortugaDSL::HOME_strategy)
@settings(max_examples=50)
def test_tortugadsl::home_instantiation(instance):
    assert isinstance(instance, tortugaDSL::HOME)

@given(instance=tortugaDSL::PENUP_strategy)
@settings(max_examples=50)
def test_tortugadsl::penup_instantiation(instance):
    assert isinstance(instance, tortugaDSL::PENUP)

@given(instance=tortugaDSL::COLOREABLE_strategy)
@settings(max_examples=50)
def test_tortugadsl::coloreable_instantiation(instance):
    assert isinstance(instance, tortugaDSL::COLOREABLE)

@given(instance=tortugaDSL::COLOREABLE_strategy)
def test_tortugadsl::coloreable_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=tortugaDSL::COLOREABLE_strategy)
def test_tortugadsl::coloreable_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=tortugaDSL::CLEAR_strategy)
@settings(max_examples=50)
def test_tortugadsl::clear_instantiation(instance):
    assert isinstance(instance, tortugaDSL::CLEAR)

@given(instance=tortugaDSL::PENDOWN_strategy)
@settings(max_examples=50)
def test_tortugadsl::pendown_instantiation(instance):
    assert isinstance(instance, tortugaDSL::PENDOWN)

@given(instance=MOVE_strategy)
@settings(max_examples=50)
def test_move_instantiation(instance):
    assert isinstance(instance, MOVE)

@given(instance=tortugaDSL::SET::Y_strategy)
@settings(max_examples=50)
def test_tortugadsl::set::y_instantiation(instance):
    assert isinstance(instance, tortugaDSL::SET::Y)

@given(instance=tortugaDSL::LEFT_strategy)
@settings(max_examples=50)
def test_tortugadsl::left_instantiation(instance):
    assert isinstance(instance, tortugaDSL::LEFT)

@given(instance=tortugaDSL::RIGHT_strategy)
@settings(max_examples=50)
def test_tortugadsl::right_instantiation(instance):
    assert isinstance(instance, tortugaDSL::RIGHT)

@given(instance=tortugaDSL::SET::X_strategy)
@settings(max_examples=50)
def test_tortugadsl::set::x_instantiation(instance):
    assert isinstance(instance, tortugaDSL::SET::X)

@given(instance=tortugaDSL::FORWARD_strategy)
@settings(max_examples=50)
def test_tortugadsl::forward_instantiation(instance):
    assert isinstance(instance, tortugaDSL::FORWARD)

@given(instance=tortugaDSL::EXPRESSION_strategy)
@settings(max_examples=50)
def test_tortugadsl::expression_instantiation(instance):
    assert isinstance(instance, tortugaDSL::EXPRESSION)

@given(instance=SENTENCE_strategy)
@settings(max_examples=50)
def test_sentence_instantiation(instance):
    assert isinstance(instance, SENTENCE)

@given(instance=tortugaDSL::CONTROL::SENTENCES_strategy)
@settings(max_examples=50)
def test_tortugadsl::control::sentences_instantiation(instance):
    assert isinstance(instance, tortugaDSL::CONTROL::SENTENCES)

@given(instance=tortugaDSL::MAKE_strategy)
@settings(max_examples=50)
def test_tortugadsl::make_instantiation(instance):
    assert isinstance(instance, tortugaDSL::MAKE)

@given(instance=tortugaDSL::PROCEDURE::CALL_strategy)
@settings(max_examples=50)
def test_tortugadsl::procedure::call_instantiation(instance):
    assert isinstance(instance, tortugaDSL::PROCEDURE::CALL)

@given(instance=tortugaDSL::DRAWING::SENTENCE_strategy)
@settings(max_examples=50)
def test_tortugadsl::drawing::sentence_instantiation(instance):
    assert isinstance(instance, tortugaDSL::DRAWING::SENTENCE)

@given(instance=tortugaDSL::CONTENT_strategy)
@settings(max_examples=50)
def test_tortugadsl::content_instantiation(instance):
    assert isinstance(instance, tortugaDSL::CONTENT)

@given(instance=tortugaDSL::OPERATION_strategy)
@settings(max_examples=50)
def test_tortugadsl::operation_instantiation(instance):
    assert isinstance(instance, tortugaDSL::OPERATION)

@given(instance=tortugaDSL::MOVE_strategy)
@settings(max_examples=50)
def test_tortugadsl::move_instantiation(instance):
    assert isinstance(instance, tortugaDSL::MOVE)

@given(instance=tortugaDSL::SENTENCE_strategy)
@settings(max_examples=50)
def test_tortugadsl::sentence_instantiation(instance):
    assert isinstance(instance, tortugaDSL::SENTENCE)
