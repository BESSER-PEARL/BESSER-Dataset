import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Legolang::controlflow::Program,
    opUnaire,
    Legolang::controlflow::not,
    opBinaire,
    Legolang::controlflow::and,
    operator,
    Legolang::controlflow::opBinaire,
    controlflow::ExprBool,
    controlflow::operator,
    Legolang::controlflow::opUnaire,
    Legolang::controlflow::operator,
    tantqueue,
    Legolang::controlflow::Expr,
    ExprBool,
    OrderRobot,
    Legolang::Robot::display,
    Legolang::Robot::bip,
    Legolang::Robot::turn,
    Legolang::Robot::stopEngine,
    Legolang::Robot::turnAngle,
    Legolang::Robot::obstacle,
    Legolang::Robot::hasTurned,
    Legolang::Robot::move,
    Expr,
    Legolang::controlflow::si,
    Legolang::controlflow::tantqueue,
    Legolang::controlflow::ExprBool,
    Legolang::Robot::OrderRobot,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_legolang::controlflow::program_is_not_abstract():
    assert not inspect.isabstract(Legolang::controlflow::Program)


def test_legolang::controlflow::program_constructor_exists():
    assert callable(Legolang::controlflow::Program.__init__)


def test_legolang::controlflow::program_constructor_args():
    sig = inspect.signature(Legolang::controlflow::Program.__init__)
    params = list(sig.parameters.keys())



def test_opunaire_is_not_abstract():
    assert not inspect.isabstract(opUnaire)


def test_opunaire_constructor_exists():
    assert callable(opUnaire.__init__)


def test_opunaire_constructor_args():
    sig = inspect.signature(opUnaire.__init__)
    params = list(sig.parameters.keys())



def test_legolang::controlflow::not_is_not_abstract():
    assert not inspect.isabstract(Legolang::controlflow::not)


def test_legolang::controlflow::not_constructor_exists():
    assert callable(Legolang::controlflow::not.__init__)


def test_legolang::controlflow::not_constructor_args():
    sig = inspect.signature(Legolang::controlflow::not.__init__)
    params = list(sig.parameters.keys())



def test_opbinaire_is_not_abstract():
    assert not inspect.isabstract(opBinaire)


def test_opbinaire_constructor_exists():
    assert callable(opBinaire.__init__)


def test_opbinaire_constructor_args():
    sig = inspect.signature(opBinaire.__init__)
    params = list(sig.parameters.keys())



def test_legolang::controlflow::and_is_not_abstract():
    assert not inspect.isabstract(Legolang::controlflow::and)


def test_legolang::controlflow::and_constructor_exists():
    assert callable(Legolang::controlflow::and.__init__)


def test_legolang::controlflow::and_constructor_args():
    sig = inspect.signature(Legolang::controlflow::and.__init__)
    params = list(sig.parameters.keys())



def test_operator_is_not_abstract():
    assert not inspect.isabstract(operator)


def test_operator_constructor_exists():
    assert callable(operator.__init__)


def test_operator_constructor_args():
    sig = inspect.signature(operator.__init__)
    params = list(sig.parameters.keys())



def test_legolang::controlflow::opbinaire_is_not_abstract():
    assert not inspect.isabstract(Legolang::controlflow::opBinaire)


def test_legolang::controlflow::opbinaire_constructor_exists():
    assert callable(Legolang::controlflow::opBinaire.__init__)


def test_legolang::controlflow::opbinaire_constructor_args():
    sig = inspect.signature(Legolang::controlflow::opBinaire.__init__)
    params = list(sig.parameters.keys())



def test_controlflow::exprbool_is_not_abstract():
    assert not inspect.isabstract(controlflow::ExprBool)


def test_controlflow::exprbool_constructor_exists():
    assert callable(controlflow::ExprBool.__init__)


def test_controlflow::exprbool_constructor_args():
    sig = inspect.signature(controlflow::ExprBool.__init__)
    params = list(sig.parameters.keys())



def test_controlflow::operator_is_not_abstract():
    assert not inspect.isabstract(controlflow::operator)


def test_controlflow::operator_constructor_exists():
    assert callable(controlflow::operator.__init__)


def test_controlflow::operator_constructor_args():
    sig = inspect.signature(controlflow::operator.__init__)
    params = list(sig.parameters.keys())



def test_legolang::controlflow::opunaire_is_not_abstract():
    assert not inspect.isabstract(Legolang::controlflow::opUnaire)


def test_legolang::controlflow::opunaire_constructor_exists():
    assert callable(Legolang::controlflow::opUnaire.__init__)


def test_legolang::controlflow::opunaire_constructor_args():
    sig = inspect.signature(Legolang::controlflow::opUnaire.__init__)
    params = list(sig.parameters.keys())



def test_legolang::controlflow::operator_is_not_abstract():
    assert not inspect.isabstract(Legolang::controlflow::operator)


def test_legolang::controlflow::operator_constructor_exists():
    assert callable(Legolang::controlflow::operator.__init__)


def test_legolang::controlflow::operator_constructor_args():
    sig = inspect.signature(Legolang::controlflow::operator.__init__)
    params = list(sig.parameters.keys())



def test_tantqueue_is_not_abstract():
    assert not inspect.isabstract(tantqueue)


def test_tantqueue_constructor_exists():
    assert callable(tantqueue.__init__)


def test_tantqueue_constructor_args():
    sig = inspect.signature(tantqueue.__init__)
    params = list(sig.parameters.keys())



def test_legolang::controlflow::expr_is_not_abstract():
    assert not inspect.isabstract(Legolang::controlflow::Expr)


def test_legolang::controlflow::expr_constructor_exists():
    assert callable(Legolang::controlflow::Expr.__init__)


def test_legolang::controlflow::expr_constructor_args():
    sig = inspect.signature(Legolang::controlflow::Expr.__init__)
    params = list(sig.parameters.keys())



def test_exprbool_is_not_abstract():
    assert not inspect.isabstract(ExprBool)


def test_exprbool_constructor_exists():
    assert callable(ExprBool.__init__)


def test_exprbool_constructor_args():
    sig = inspect.signature(ExprBool.__init__)
    params = list(sig.parameters.keys())



def test_orderrobot_is_not_abstract():
    assert not inspect.isabstract(OrderRobot)


def test_orderrobot_constructor_exists():
    assert callable(OrderRobot.__init__)


def test_orderrobot_constructor_args():
    sig = inspect.signature(OrderRobot.__init__)
    params = list(sig.parameters.keys())



def test_legolang::robot::display_is_not_abstract():
    assert not inspect.isabstract(Legolang::Robot::display)


def test_legolang::robot::display_constructor_exists():
    assert callable(Legolang::Robot::display.__init__)


def test_legolang::robot::display_constructor_args():
    sig = inspect.signature(Legolang::Robot::display.__init__)
    params = list(sig.parameters.keys())



def test_legolang::robot::bip_is_not_abstract():
    assert not inspect.isabstract(Legolang::Robot::bip)


def test_legolang::robot::bip_constructor_exists():
    assert callable(Legolang::Robot::bip.__init__)


def test_legolang::robot::bip_constructor_args():
    sig = inspect.signature(Legolang::Robot::bip.__init__)
    params = list(sig.parameters.keys())



def test_legolang::robot::turn_is_not_abstract():
    assert not inspect.isabstract(Legolang::Robot::turn)


def test_legolang::robot::turn_constructor_exists():
    assert callable(Legolang::Robot::turn.__init__)


def test_legolang::robot::turn_constructor_args():
    sig = inspect.signature(Legolang::Robot::turn.__init__)
    params = list(sig.parameters.keys())



def test_legolang::robot::stopengine_is_not_abstract():
    assert not inspect.isabstract(Legolang::Robot::stopEngine)


def test_legolang::robot::stopengine_constructor_exists():
    assert callable(Legolang::Robot::stopEngine.__init__)


def test_legolang::robot::stopengine_constructor_args():
    sig = inspect.signature(Legolang::Robot::stopEngine.__init__)
    params = list(sig.parameters.keys())



def test_legolang::robot::turnangle_is_not_abstract():
    assert not inspect.isabstract(Legolang::Robot::turnAngle)


def test_legolang::robot::turnangle_constructor_exists():
    assert callable(Legolang::Robot::turnAngle.__init__)


def test_legolang::robot::turnangle_constructor_args():
    sig = inspect.signature(Legolang::Robot::turnAngle.__init__)
    params = list(sig.parameters.keys())



def test_legolang::robot::obstacle_is_not_abstract():
    assert not inspect.isabstract(Legolang::Robot::obstacle)


def test_legolang::robot::obstacle_constructor_exists():
    assert callable(Legolang::Robot::obstacle.__init__)


def test_legolang::robot::obstacle_constructor_args():
    sig = inspect.signature(Legolang::Robot::obstacle.__init__)
    params = list(sig.parameters.keys())



def test_legolang::robot::hasturned_is_not_abstract():
    assert not inspect.isabstract(Legolang::Robot::hasTurned)


def test_legolang::robot::hasturned_constructor_exists():
    assert callable(Legolang::Robot::hasTurned.__init__)


def test_legolang::robot::hasturned_constructor_args():
    sig = inspect.signature(Legolang::Robot::hasTurned.__init__)
    params = list(sig.parameters.keys())



def test_legolang::robot::move_is_not_abstract():
    assert not inspect.isabstract(Legolang::Robot::move)


def test_legolang::robot::move_constructor_exists():
    assert callable(Legolang::Robot::move.__init__)


def test_legolang::robot::move_constructor_args():
    sig = inspect.signature(Legolang::Robot::move.__init__)
    params = list(sig.parameters.keys())



def test_expr_is_not_abstract():
    assert not inspect.isabstract(Expr)


def test_expr_constructor_exists():
    assert callable(Expr.__init__)


def test_expr_constructor_args():
    sig = inspect.signature(Expr.__init__)
    params = list(sig.parameters.keys())



def test_legolang::controlflow::si_is_not_abstract():
    assert not inspect.isabstract(Legolang::controlflow::si)


def test_legolang::controlflow::si_constructor_exists():
    assert callable(Legolang::controlflow::si.__init__)


def test_legolang::controlflow::si_constructor_args():
    sig = inspect.signature(Legolang::controlflow::si.__init__)
    params = list(sig.parameters.keys())



def test_legolang::controlflow::tantqueue_is_not_abstract():
    assert not inspect.isabstract(Legolang::controlflow::tantqueue)


def test_legolang::controlflow::tantqueue_constructor_exists():
    assert callable(Legolang::controlflow::tantqueue.__init__)


def test_legolang::controlflow::tantqueue_constructor_args():
    sig = inspect.signature(Legolang::controlflow::tantqueue.__init__)
    params = list(sig.parameters.keys())



def test_legolang::controlflow::exprbool_is_not_abstract():
    assert not inspect.isabstract(Legolang::controlflow::ExprBool)


def test_legolang::controlflow::exprbool_constructor_exists():
    assert callable(Legolang::controlflow::ExprBool.__init__)


def test_legolang::controlflow::exprbool_constructor_args():
    sig = inspect.signature(Legolang::controlflow::ExprBool.__init__)
    params = list(sig.parameters.keys())



def test_legolang::robot::orderrobot_is_not_abstract():
    assert not inspect.isabstract(Legolang::Robot::OrderRobot)


def test_legolang::robot::orderrobot_constructor_exists():
    assert callable(Legolang::Robot::OrderRobot.__init__)


def test_legolang::robot::orderrobot_constructor_args():
    sig = inspect.signature(Legolang::Robot::OrderRobot.__init__)
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
Legolang::controlflow::Program_strategy = st.builds(
    Legolang::controlflow::Program,
)
opUnaire_strategy = st.builds(
    opUnaire,
)
Legolang::controlflow::not_strategy = st.builds(
    Legolang::controlflow::not,
)
opBinaire_strategy = st.builds(
    opBinaire,
)
Legolang::controlflow::and_strategy = st.builds(
    Legolang::controlflow::and,
)
operator_strategy = st.builds(
    operator,
)
Legolang::controlflow::opBinaire_strategy = st.builds(
    Legolang::controlflow::opBinaire,
)
controlflow::ExprBool_strategy = st.builds(
    controlflow::ExprBool,
)
controlflow::operator_strategy = st.builds(
    controlflow::operator,
)
Legolang::controlflow::opUnaire_strategy = st.builds(
    Legolang::controlflow::opUnaire,
)
Legolang::controlflow::operator_strategy = st.builds(
    Legolang::controlflow::operator,
)
tantqueue_strategy = st.builds(
    tantqueue,
)
Legolang::controlflow::Expr_strategy = st.builds(
    Legolang::controlflow::Expr,
)
ExprBool_strategy = st.builds(
    ExprBool,
)
OrderRobot_strategy = st.builds(
    OrderRobot,
)
Legolang::Robot::display_strategy = st.builds(
    Legolang::Robot::display,
)
Legolang::Robot::bip_strategy = st.builds(
    Legolang::Robot::bip,
)
Legolang::Robot::turn_strategy = st.builds(
    Legolang::Robot::turn,
)
Legolang::Robot::stopEngine_strategy = st.builds(
    Legolang::Robot::stopEngine,
)
Legolang::Robot::turnAngle_strategy = st.builds(
    Legolang::Robot::turnAngle,
)
Legolang::Robot::obstacle_strategy = st.builds(
    Legolang::Robot::obstacle,
)
Legolang::Robot::hasTurned_strategy = st.builds(
    Legolang::Robot::hasTurned,
)
Legolang::Robot::move_strategy = st.builds(
    Legolang::Robot::move,
)
Expr_strategy = st.builds(
    Expr,
)
Legolang::controlflow::si_strategy = st.builds(
    Legolang::controlflow::si,
)
Legolang::controlflow::tantqueue_strategy = st.builds(
    Legolang::controlflow::tantqueue,
)
Legolang::controlflow::ExprBool_strategy = st.builds(
    Legolang::controlflow::ExprBool,
)
Legolang::Robot::OrderRobot_strategy = st.builds(
    Legolang::Robot::OrderRobot,
)

@given(instance=Legolang::controlflow::Program_strategy)
@settings(max_examples=50)
def test_legolang::controlflow::program_instantiation(instance):
    assert isinstance(instance, Legolang::controlflow::Program)

@given(instance=opUnaire_strategy)
@settings(max_examples=50)
def test_opunaire_instantiation(instance):
    assert isinstance(instance, opUnaire)

@given(instance=Legolang::controlflow::not_strategy)
@settings(max_examples=50)
def test_legolang::controlflow::not_instantiation(instance):
    assert isinstance(instance, Legolang::controlflow::not)

@given(instance=opBinaire_strategy)
@settings(max_examples=50)
def test_opbinaire_instantiation(instance):
    assert isinstance(instance, opBinaire)

@given(instance=Legolang::controlflow::and_strategy)
@settings(max_examples=50)
def test_legolang::controlflow::and_instantiation(instance):
    assert isinstance(instance, Legolang::controlflow::and)

@given(instance=operator_strategy)
@settings(max_examples=50)
def test_operator_instantiation(instance):
    assert isinstance(instance, operator)

@given(instance=Legolang::controlflow::opBinaire_strategy)
@settings(max_examples=50)
def test_legolang::controlflow::opbinaire_instantiation(instance):
    assert isinstance(instance, Legolang::controlflow::opBinaire)

@given(instance=controlflow::ExprBool_strategy)
@settings(max_examples=50)
def test_controlflow::exprbool_instantiation(instance):
    assert isinstance(instance, controlflow::ExprBool)

@given(instance=controlflow::operator_strategy)
@settings(max_examples=50)
def test_controlflow::operator_instantiation(instance):
    assert isinstance(instance, controlflow::operator)

@given(instance=Legolang::controlflow::opUnaire_strategy)
@settings(max_examples=50)
def test_legolang::controlflow::opunaire_instantiation(instance):
    assert isinstance(instance, Legolang::controlflow::opUnaire)

@given(instance=Legolang::controlflow::operator_strategy)
@settings(max_examples=50)
def test_legolang::controlflow::operator_instantiation(instance):
    assert isinstance(instance, Legolang::controlflow::operator)

@given(instance=tantqueue_strategy)
@settings(max_examples=50)
def test_tantqueue_instantiation(instance):
    assert isinstance(instance, tantqueue)

@given(instance=Legolang::controlflow::Expr_strategy)
@settings(max_examples=50)
def test_legolang::controlflow::expr_instantiation(instance):
    assert isinstance(instance, Legolang::controlflow::Expr)

@given(instance=ExprBool_strategy)
@settings(max_examples=50)
def test_exprbool_instantiation(instance):
    assert isinstance(instance, ExprBool)

@given(instance=OrderRobot_strategy)
@settings(max_examples=50)
def test_orderrobot_instantiation(instance):
    assert isinstance(instance, OrderRobot)

@given(instance=Legolang::Robot::display_strategy)
@settings(max_examples=50)
def test_legolang::robot::display_instantiation(instance):
    assert isinstance(instance, Legolang::Robot::display)

@given(instance=Legolang::Robot::bip_strategy)
@settings(max_examples=50)
def test_legolang::robot::bip_instantiation(instance):
    assert isinstance(instance, Legolang::Robot::bip)

@given(instance=Legolang::Robot::turn_strategy)
@settings(max_examples=50)
def test_legolang::robot::turn_instantiation(instance):
    assert isinstance(instance, Legolang::Robot::turn)

@given(instance=Legolang::Robot::stopEngine_strategy)
@settings(max_examples=50)
def test_legolang::robot::stopengine_instantiation(instance):
    assert isinstance(instance, Legolang::Robot::stopEngine)

@given(instance=Legolang::Robot::turnAngle_strategy)
@settings(max_examples=50)
def test_legolang::robot::turnangle_instantiation(instance):
    assert isinstance(instance, Legolang::Robot::turnAngle)

@given(instance=Legolang::Robot::obstacle_strategy)
@settings(max_examples=50)
def test_legolang::robot::obstacle_instantiation(instance):
    assert isinstance(instance, Legolang::Robot::obstacle)

@given(instance=Legolang::Robot::hasTurned_strategy)
@settings(max_examples=50)
def test_legolang::robot::hasturned_instantiation(instance):
    assert isinstance(instance, Legolang::Robot::hasTurned)

@given(instance=Legolang::Robot::move_strategy)
@settings(max_examples=50)
def test_legolang::robot::move_instantiation(instance):
    assert isinstance(instance, Legolang::Robot::move)

@given(instance=Expr_strategy)
@settings(max_examples=50)
def test_expr_instantiation(instance):
    assert isinstance(instance, Expr)

@given(instance=Legolang::controlflow::si_strategy)
@settings(max_examples=50)
def test_legolang::controlflow::si_instantiation(instance):
    assert isinstance(instance, Legolang::controlflow::si)

@given(instance=Legolang::controlflow::tantqueue_strategy)
@settings(max_examples=50)
def test_legolang::controlflow::tantqueue_instantiation(instance):
    assert isinstance(instance, Legolang::controlflow::tantqueue)

@given(instance=Legolang::controlflow::ExprBool_strategy)
@settings(max_examples=50)
def test_legolang::controlflow::exprbool_instantiation(instance):
    assert isinstance(instance, Legolang::controlflow::ExprBool)

@given(instance=Legolang::Robot::OrderRobot_strategy)
@settings(max_examples=50)
def test_legolang::robot::orderrobot_instantiation(instance):
    assert isinstance(instance, Legolang::Robot::OrderRobot)
