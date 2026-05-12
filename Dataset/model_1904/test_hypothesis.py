import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ConnectionType,
    drn_Wifi,
    drn_Bluetooth,
    drn_RefDevice,
    drn_Element,
    drn_Definition,
    drn_Declaration,
    DepXYZ_IMPL,
    drn_Flip,
    DepXZ_IMPL,
    drn_CARREXZ,
    drn_CERCLEXZ,
    DepYZ_IMPL,
    drn_CARREYZ,
    drn_CERCLEYZ,
    DepXY_IMPL,
    drn_CARREXY,
    drn_CERCLEXY,
    DepZ_Impl,
    drn_DOWN,
    drn_UP,
    DepX_Impl,
    drn_RIGHT,
    drn_LEFT,
    DepY_Impl,
    drn_BACKWARD,
    drn_FORWARD,
    Movement,
    drn_DepX_Impl,
    drn_And,
    drn_TakeOff,
    drn_DepXZ_IMPL,
    drn_DepZ_Impl,
    drn_RefPartLib,
    drn_DepXYZ_IMPL,
    drn_DepYZ_IMPL,
    drn_Rotate,
    drn_DepY_Impl,
    drn_Land,
    drn_Wait,
    drn_DepXY_IMPL,
    drn_Movement,
    drn_Expression,
    Surface,
    drn_MaxHeight,
    drn_MaxWidth,
    drn_MaxLength,
    InitialPosition,
    drn_InitialPositionY,
    drn_InitialPositionX,
    drn_InitialDirection,
    Limit,
    drn_InitialPosition,
    drn_MaxSpeed,
    drn_Surface,
    drn_Limit,
    drn_ConnectionType,
    drn_Device,
    drn_TypeGeneric,
    drn_RefPart,
    drn_Context,
    drn_With,
    drn_Assignement,
    Root,
    drn_Configuration,
    drn_Library,
    drn_Model,
    drn_Root,
    EBool,
    Mode,
    TypePrimitif,
    Where,
    DirectionType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_connectiontype_is_not_abstract():
    assert not inspect.isabstract(ConnectionType)


def test_connectiontype_constructor_exists():
    assert callable(ConnectionType.__init__)


def test_connectiontype_constructor_args():
    sig = inspect.signature(ConnectionType.__init__)
    params = list(sig.parameters.keys())



def test_drn_wifi_is_not_abstract():
    assert not inspect.isabstract(drn_Wifi)


def test_drn_wifi_constructor_exists():
    assert callable(drn_Wifi.__init__)


def test_drn_wifi_constructor_args():
    sig = inspect.signature(drn_Wifi.__init__)
    params = list(sig.parameters.keys())



def test_drn_bluetooth_is_not_abstract():
    assert not inspect.isabstract(drn_Bluetooth)


def test_drn_bluetooth_constructor_exists():
    assert callable(drn_Bluetooth.__init__)


def test_drn_bluetooth_constructor_args():
    sig = inspect.signature(drn_Bluetooth.__init__)
    params = list(sig.parameters.keys())



def test_drn_refdevice_is_not_abstract():
    assert not inspect.isabstract(drn_RefDevice)


def test_drn_refdevice_constructor_exists():
    assert callable(drn_RefDevice.__init__)


def test_drn_refdevice_constructor_args():
    sig = inspect.signature(drn_RefDevice.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"

def test_drn_refdevice_has_mode():
    assert hasattr(drn_RefDevice, "mode")
    descriptor = None
    for klass in drn_RefDevice.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_drn_element_is_not_abstract():
    assert not inspect.isabstract(drn_Element)


def test_drn_element_constructor_exists():
    assert callable(drn_Element.__init__)


def test_drn_element_constructor_args():
    sig = inspect.signature(drn_Element.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_drn_element_has_name():
    assert hasattr(drn_Element, "name")
    descriptor = None
    for klass in drn_Element.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_drn_definition_is_not_abstract():
    assert not inspect.isabstract(drn_Definition)


def test_drn_definition_constructor_exists():
    assert callable(drn_Definition.__init__)


def test_drn_definition_constructor_args():
    sig = inspect.signature(drn_Definition.__init__)
    params = list(sig.parameters.keys())
    assert "int" in params, "Missing parameter 'int'"
    assert "real" in params, "Missing parameter 'real'"
    assert "bool" in params, "Missing parameter 'bool'"
    assert "text" in params, "Missing parameter 'text'"

def test_drn_definition_has_int():
    assert hasattr(drn_Definition, "int")
    descriptor = None
    for klass in drn_Definition.__mro__:
        if "int" in klass.__dict__:
            descriptor = klass.__dict__["int"]
            break
    assert isinstance(descriptor, property)

def test_drn_definition_has_real():
    assert hasattr(drn_Definition, "real")
    descriptor = None
    for klass in drn_Definition.__mro__:
        if "real" in klass.__dict__:
            descriptor = klass.__dict__["real"]
            break
    assert isinstance(descriptor, property)

def test_drn_definition_has_bool():
    assert hasattr(drn_Definition, "bool")
    descriptor = None
    for klass in drn_Definition.__mro__:
        if "bool" in klass.__dict__:
            descriptor = klass.__dict__["bool"]
            break
    assert isinstance(descriptor, property)

def test_drn_definition_has_text():
    assert hasattr(drn_Definition, "text")
    descriptor = None
    for klass in drn_Definition.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_drn_declaration_is_not_abstract():
    assert not inspect.isabstract(drn_Declaration)


def test_drn_declaration_constructor_exists():
    assert callable(drn_Declaration.__init__)


def test_drn_declaration_constructor_args():
    sig = inspect.signature(drn_Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "typePrimitif" in params, "Missing parameter 'typePrimitif'"

def test_drn_declaration_has_name():
    assert hasattr(drn_Declaration, "name")
    descriptor = None
    for klass in drn_Declaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_drn_declaration_has_typePrimitif():
    assert hasattr(drn_Declaration, "typePrimitif")
    descriptor = None
    for klass in drn_Declaration.__mro__:
        if "typePrimitif" in klass.__dict__:
            descriptor = klass.__dict__["typePrimitif"]
            break
    assert isinstance(descriptor, property)



def test_depxyz_impl_is_not_abstract():
    assert not inspect.isabstract(DepXYZ_IMPL)


def test_depxyz_impl_constructor_exists():
    assert callable(DepXYZ_IMPL.__init__)


def test_depxyz_impl_constructor_args():
    sig = inspect.signature(DepXYZ_IMPL.__init__)
    params = list(sig.parameters.keys())



def test_drn_flip_is_not_abstract():
    assert not inspect.isabstract(drn_Flip)


def test_drn_flip_constructor_exists():
    assert callable(drn_Flip.__init__)


def test_drn_flip_constructor_args():
    sig = inspect.signature(drn_Flip.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_drn_flip_has_name():
    assert hasattr(drn_Flip, "name")
    descriptor = None
    for klass in drn_Flip.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_depxz_impl_is_not_abstract():
    assert not inspect.isabstract(DepXZ_IMPL)


def test_depxz_impl_constructor_exists():
    assert callable(DepXZ_IMPL.__init__)


def test_depxz_impl_constructor_args():
    sig = inspect.signature(DepXZ_IMPL.__init__)
    params = list(sig.parameters.keys())



def test_drn_carrexz_is_not_abstract():
    assert not inspect.isabstract(drn_CARREXZ)


def test_drn_carrexz_constructor_exists():
    assert callable(drn_CARREXZ.__init__)


def test_drn_carrexz_constructor_args():
    sig = inspect.signature(drn_CARREXZ.__init__)
    params = list(sig.parameters.keys())
    assert "coteCST" in params, "Missing parameter 'coteCST'"

def test_drn_carrexz_has_coteCST():
    assert hasattr(drn_CARREXZ, "coteCST")
    descriptor = None
    for klass in drn_CARREXZ.__mro__:
        if "coteCST" in klass.__dict__:
            descriptor = klass.__dict__["coteCST"]
            break
    assert isinstance(descriptor, property)



def test_drn_cerclexz_is_not_abstract():
    assert not inspect.isabstract(drn_CERCLEXZ)


def test_drn_cerclexz_constructor_exists():
    assert callable(drn_CERCLEXZ.__init__)


def test_drn_cerclexz_constructor_args():
    sig = inspect.signature(drn_CERCLEXZ.__init__)
    params = list(sig.parameters.keys())
    assert "rayonCST" in params, "Missing parameter 'rayonCST'"

def test_drn_cerclexz_has_rayonCST():
    assert hasattr(drn_CERCLEXZ, "rayonCST")
    descriptor = None
    for klass in drn_CERCLEXZ.__mro__:
        if "rayonCST" in klass.__dict__:
            descriptor = klass.__dict__["rayonCST"]
            break
    assert isinstance(descriptor, property)



def test_depyz_impl_is_not_abstract():
    assert not inspect.isabstract(DepYZ_IMPL)


def test_depyz_impl_constructor_exists():
    assert callable(DepYZ_IMPL.__init__)


def test_depyz_impl_constructor_args():
    sig = inspect.signature(DepYZ_IMPL.__init__)
    params = list(sig.parameters.keys())



def test_drn_carreyz_is_not_abstract():
    assert not inspect.isabstract(drn_CARREYZ)


def test_drn_carreyz_constructor_exists():
    assert callable(drn_CARREYZ.__init__)


def test_drn_carreyz_constructor_args():
    sig = inspect.signature(drn_CARREYZ.__init__)
    params = list(sig.parameters.keys())
    assert "coteCST" in params, "Missing parameter 'coteCST'"

def test_drn_carreyz_has_coteCST():
    assert hasattr(drn_CARREYZ, "coteCST")
    descriptor = None
    for klass in drn_CARREYZ.__mro__:
        if "coteCST" in klass.__dict__:
            descriptor = klass.__dict__["coteCST"]
            break
    assert isinstance(descriptor, property)



def test_drn_cercleyz_is_not_abstract():
    assert not inspect.isabstract(drn_CERCLEYZ)


def test_drn_cercleyz_constructor_exists():
    assert callable(drn_CERCLEYZ.__init__)


def test_drn_cercleyz_constructor_args():
    sig = inspect.signature(drn_CERCLEYZ.__init__)
    params = list(sig.parameters.keys())
    assert "rayonCST" in params, "Missing parameter 'rayonCST'"

def test_drn_cercleyz_has_rayonCST():
    assert hasattr(drn_CERCLEYZ, "rayonCST")
    descriptor = None
    for klass in drn_CERCLEYZ.__mro__:
        if "rayonCST" in klass.__dict__:
            descriptor = klass.__dict__["rayonCST"]
            break
    assert isinstance(descriptor, property)



def test_depxy_impl_is_not_abstract():
    assert not inspect.isabstract(DepXY_IMPL)


def test_depxy_impl_constructor_exists():
    assert callable(DepXY_IMPL.__init__)


def test_depxy_impl_constructor_args():
    sig = inspect.signature(DepXY_IMPL.__init__)
    params = list(sig.parameters.keys())



def test_drn_carrexy_is_not_abstract():
    assert not inspect.isabstract(drn_CARREXY)


def test_drn_carrexy_constructor_exists():
    assert callable(drn_CARREXY.__init__)


def test_drn_carrexy_constructor_args():
    sig = inspect.signature(drn_CARREXY.__init__)
    params = list(sig.parameters.keys())
    assert "coteCST" in params, "Missing parameter 'coteCST'"

def test_drn_carrexy_has_coteCST():
    assert hasattr(drn_CARREXY, "coteCST")
    descriptor = None
    for klass in drn_CARREXY.__mro__:
        if "coteCST" in klass.__dict__:
            descriptor = klass.__dict__["coteCST"]
            break
    assert isinstance(descriptor, property)



def test_drn_cerclexy_is_not_abstract():
    assert not inspect.isabstract(drn_CERCLEXY)


def test_drn_cerclexy_constructor_exists():
    assert callable(drn_CERCLEXY.__init__)


def test_drn_cerclexy_constructor_args():
    sig = inspect.signature(drn_CERCLEXY.__init__)
    params = list(sig.parameters.keys())
    assert "rayonCST" in params, "Missing parameter 'rayonCST'"

def test_drn_cerclexy_has_rayonCST():
    assert hasattr(drn_CERCLEXY, "rayonCST")
    descriptor = None
    for klass in drn_CERCLEXY.__mro__:
        if "rayonCST" in klass.__dict__:
            descriptor = klass.__dict__["rayonCST"]
            break
    assert isinstance(descriptor, property)



def test_depz_impl_is_not_abstract():
    assert not inspect.isabstract(DepZ_Impl)


def test_depz_impl_constructor_exists():
    assert callable(DepZ_Impl.__init__)


def test_depz_impl_constructor_args():
    sig = inspect.signature(DepZ_Impl.__init__)
    params = list(sig.parameters.keys())



def test_drn_down_is_not_abstract():
    assert not inspect.isabstract(drn_DOWN)


def test_drn_down_constructor_exists():
    assert callable(drn_DOWN.__init__)


def test_drn_down_constructor_args():
    sig = inspect.signature(drn_DOWN.__init__)
    params = list(sig.parameters.keys())



def test_drn_up_is_not_abstract():
    assert not inspect.isabstract(drn_UP)


def test_drn_up_constructor_exists():
    assert callable(drn_UP.__init__)


def test_drn_up_constructor_args():
    sig = inspect.signature(drn_UP.__init__)
    params = list(sig.parameters.keys())



def test_depx_impl_is_not_abstract():
    assert not inspect.isabstract(DepX_Impl)


def test_depx_impl_constructor_exists():
    assert callable(DepX_Impl.__init__)


def test_depx_impl_constructor_args():
    sig = inspect.signature(DepX_Impl.__init__)
    params = list(sig.parameters.keys())



def test_drn_right_is_not_abstract():
    assert not inspect.isabstract(drn_RIGHT)


def test_drn_right_constructor_exists():
    assert callable(drn_RIGHT.__init__)


def test_drn_right_constructor_args():
    sig = inspect.signature(drn_RIGHT.__init__)
    params = list(sig.parameters.keys())



def test_drn_left_is_not_abstract():
    assert not inspect.isabstract(drn_LEFT)


def test_drn_left_constructor_exists():
    assert callable(drn_LEFT.__init__)


def test_drn_left_constructor_args():
    sig = inspect.signature(drn_LEFT.__init__)
    params = list(sig.parameters.keys())



def test_depy_impl_is_not_abstract():
    assert not inspect.isabstract(DepY_Impl)


def test_depy_impl_constructor_exists():
    assert callable(DepY_Impl.__init__)


def test_depy_impl_constructor_args():
    sig = inspect.signature(DepY_Impl.__init__)
    params = list(sig.parameters.keys())



def test_drn_backward_is_not_abstract():
    assert not inspect.isabstract(drn_BACKWARD)


def test_drn_backward_constructor_exists():
    assert callable(drn_BACKWARD.__init__)


def test_drn_backward_constructor_args():
    sig = inspect.signature(drn_BACKWARD.__init__)
    params = list(sig.parameters.keys())



def test_drn_forward_is_not_abstract():
    assert not inspect.isabstract(drn_FORWARD)


def test_drn_forward_constructor_exists():
    assert callable(drn_FORWARD.__init__)


def test_drn_forward_constructor_args():
    sig = inspect.signature(drn_FORWARD.__init__)
    params = list(sig.parameters.keys())



def test_movement_is_not_abstract():
    assert not inspect.isabstract(Movement)


def test_movement_constructor_exists():
    assert callable(Movement.__init__)


def test_movement_constructor_args():
    sig = inspect.signature(Movement.__init__)
    params = list(sig.parameters.keys())



def test_drn_depx_impl_is_not_abstract():
    assert not inspect.isabstract(drn_DepX_Impl)


def test_drn_depx_impl_constructor_exists():
    assert callable(drn_DepX_Impl.__init__)


def test_drn_depx_impl_constructor_args():
    sig = inspect.signature(drn_DepX_Impl.__init__)
    params = list(sig.parameters.keys())
    assert "distanceCST" in params, "Missing parameter 'distanceCST'"
    assert "tempsCST" in params, "Missing parameter 'tempsCST'"
    assert "name" in params, "Missing parameter 'name'"

def test_drn_depx_impl_has_distanceCST():
    assert hasattr(drn_DepX_Impl, "distanceCST")
    descriptor = None
    for klass in drn_DepX_Impl.__mro__:
        if "distanceCST" in klass.__dict__:
            descriptor = klass.__dict__["distanceCST"]
            break
    assert isinstance(descriptor, property)

def test_drn_depx_impl_has_tempsCST():
    assert hasattr(drn_DepX_Impl, "tempsCST")
    descriptor = None
    for klass in drn_DepX_Impl.__mro__:
        if "tempsCST" in klass.__dict__:
            descriptor = klass.__dict__["tempsCST"]
            break
    assert isinstance(descriptor, property)

def test_drn_depx_impl_has_name():
    assert hasattr(drn_DepX_Impl, "name")
    descriptor = None
    for klass in drn_DepX_Impl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_drn_and_is_not_abstract():
    assert not inspect.isabstract(drn_And)


def test_drn_and_constructor_exists():
    assert callable(drn_And.__init__)


def test_drn_and_constructor_args():
    sig = inspect.signature(drn_And.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_drn_and_has_name():
    assert hasattr(drn_And, "name")
    descriptor = None
    for klass in drn_And.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_drn_takeoff_is_not_abstract():
    assert not inspect.isabstract(drn_TakeOff)


def test_drn_takeoff_constructor_exists():
    assert callable(drn_TakeOff.__init__)


def test_drn_takeoff_constructor_args():
    sig = inspect.signature(drn_TakeOff.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_drn_takeoff_has_name():
    assert hasattr(drn_TakeOff, "name")
    descriptor = None
    for klass in drn_TakeOff.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_drn_depxz_impl_is_not_abstract():
    assert not inspect.isabstract(drn_DepXZ_IMPL)


def test_drn_depxz_impl_constructor_exists():
    assert callable(drn_DepXZ_IMPL.__init__)


def test_drn_depxz_impl_constructor_args():
    sig = inspect.signature(drn_DepXZ_IMPL.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "tempsCST" in params, "Missing parameter 'tempsCST'"

def test_drn_depxz_impl_has_name():
    assert hasattr(drn_DepXZ_IMPL, "name")
    descriptor = None
    for klass in drn_DepXZ_IMPL.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_drn_depxz_impl_has_tempsCST():
    assert hasattr(drn_DepXZ_IMPL, "tempsCST")
    descriptor = None
    for klass in drn_DepXZ_IMPL.__mro__:
        if "tempsCST" in klass.__dict__:
            descriptor = klass.__dict__["tempsCST"]
            break
    assert isinstance(descriptor, property)



def test_drn_depz_impl_is_not_abstract():
    assert not inspect.isabstract(drn_DepZ_Impl)


def test_drn_depz_impl_constructor_exists():
    assert callable(drn_DepZ_Impl.__init__)


def test_drn_depz_impl_constructor_args():
    sig = inspect.signature(drn_DepZ_Impl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "distanceCST" in params, "Missing parameter 'distanceCST'"
    assert "tempsCST" in params, "Missing parameter 'tempsCST'"

def test_drn_depz_impl_has_name():
    assert hasattr(drn_DepZ_Impl, "name")
    descriptor = None
    for klass in drn_DepZ_Impl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_drn_depz_impl_has_distanceCST():
    assert hasattr(drn_DepZ_Impl, "distanceCST")
    descriptor = None
    for klass in drn_DepZ_Impl.__mro__:
        if "distanceCST" in klass.__dict__:
            descriptor = klass.__dict__["distanceCST"]
            break
    assert isinstance(descriptor, property)

def test_drn_depz_impl_has_tempsCST():
    assert hasattr(drn_DepZ_Impl, "tempsCST")
    descriptor = None
    for klass in drn_DepZ_Impl.__mro__:
        if "tempsCST" in klass.__dict__:
            descriptor = klass.__dict__["tempsCST"]
            break
    assert isinstance(descriptor, property)



def test_drn_refpartlib_is_not_abstract():
    assert not inspect.isabstract(drn_RefPartLib)


def test_drn_refpartlib_constructor_exists():
    assert callable(drn_RefPartLib.__init__)


def test_drn_refpartlib_constructor_args():
    sig = inspect.signature(drn_RefPartLib.__init__)
    params = list(sig.parameters.keys())



def test_drn_depxyz_impl_is_not_abstract():
    assert not inspect.isabstract(drn_DepXYZ_IMPL)


def test_drn_depxyz_impl_constructor_exists():
    assert callable(drn_DepXYZ_IMPL.__init__)


def test_drn_depxyz_impl_constructor_args():
    sig = inspect.signature(drn_DepXYZ_IMPL.__init__)
    params = list(sig.parameters.keys())



def test_drn_depyz_impl_is_not_abstract():
    assert not inspect.isabstract(drn_DepYZ_IMPL)


def test_drn_depyz_impl_constructor_exists():
    assert callable(drn_DepYZ_IMPL.__init__)


def test_drn_depyz_impl_constructor_args():
    sig = inspect.signature(drn_DepYZ_IMPL.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "tempsCST" in params, "Missing parameter 'tempsCST'"

def test_drn_depyz_impl_has_name():
    assert hasattr(drn_DepYZ_IMPL, "name")
    descriptor = None
    for klass in drn_DepYZ_IMPL.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_drn_depyz_impl_has_tempsCST():
    assert hasattr(drn_DepYZ_IMPL, "tempsCST")
    descriptor = None
    for klass in drn_DepYZ_IMPL.__mro__:
        if "tempsCST" in klass.__dict__:
            descriptor = klass.__dict__["tempsCST"]
            break
    assert isinstance(descriptor, property)



def test_drn_rotate_is_not_abstract():
    assert not inspect.isabstract(drn_Rotate)


def test_drn_rotate_constructor_exists():
    assert callable(drn_Rotate.__init__)


def test_drn_rotate_constructor_args():
    sig = inspect.signature(drn_Rotate.__init__)
    params = list(sig.parameters.keys())
    assert "angleCST" in params, "Missing parameter 'angleCST'"
    assert "name" in params, "Missing parameter 'name'"
    assert "tempsCST" in params, "Missing parameter 'tempsCST'"

def test_drn_rotate_has_angleCST():
    assert hasattr(drn_Rotate, "angleCST")
    descriptor = None
    for klass in drn_Rotate.__mro__:
        if "angleCST" in klass.__dict__:
            descriptor = klass.__dict__["angleCST"]
            break
    assert isinstance(descriptor, property)

def test_drn_rotate_has_name():
    assert hasattr(drn_Rotate, "name")
    descriptor = None
    for klass in drn_Rotate.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_drn_rotate_has_tempsCST():
    assert hasattr(drn_Rotate, "tempsCST")
    descriptor = None
    for klass in drn_Rotate.__mro__:
        if "tempsCST" in klass.__dict__:
            descriptor = klass.__dict__["tempsCST"]
            break
    assert isinstance(descriptor, property)



def test_drn_depy_impl_is_not_abstract():
    assert not inspect.isabstract(drn_DepY_Impl)


def test_drn_depy_impl_constructor_exists():
    assert callable(drn_DepY_Impl.__init__)


def test_drn_depy_impl_constructor_args():
    sig = inspect.signature(drn_DepY_Impl.__init__)
    params = list(sig.parameters.keys())
    assert "tempsCST" in params, "Missing parameter 'tempsCST'"
    assert "name" in params, "Missing parameter 'name'"
    assert "distanceCST" in params, "Missing parameter 'distanceCST'"

def test_drn_depy_impl_has_tempsCST():
    assert hasattr(drn_DepY_Impl, "tempsCST")
    descriptor = None
    for klass in drn_DepY_Impl.__mro__:
        if "tempsCST" in klass.__dict__:
            descriptor = klass.__dict__["tempsCST"]
            break
    assert isinstance(descriptor, property)

def test_drn_depy_impl_has_name():
    assert hasattr(drn_DepY_Impl, "name")
    descriptor = None
    for klass in drn_DepY_Impl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_drn_depy_impl_has_distanceCST():
    assert hasattr(drn_DepY_Impl, "distanceCST")
    descriptor = None
    for klass in drn_DepY_Impl.__mro__:
        if "distanceCST" in klass.__dict__:
            descriptor = klass.__dict__["distanceCST"]
            break
    assert isinstance(descriptor, property)



def test_drn_land_is_not_abstract():
    assert not inspect.isabstract(drn_Land)


def test_drn_land_constructor_exists():
    assert callable(drn_Land.__init__)


def test_drn_land_constructor_args():
    sig = inspect.signature(drn_Land.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_drn_land_has_name():
    assert hasattr(drn_Land, "name")
    descriptor = None
    for klass in drn_Land.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_drn_wait_is_not_abstract():
    assert not inspect.isabstract(drn_Wait)


def test_drn_wait_constructor_exists():
    assert callable(drn_Wait.__init__)


def test_drn_wait_constructor_args():
    sig = inspect.signature(drn_Wait.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "tempsCST" in params, "Missing parameter 'tempsCST'"

def test_drn_wait_has_name():
    assert hasattr(drn_Wait, "name")
    descriptor = None
    for klass in drn_Wait.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_drn_wait_has_tempsCST():
    assert hasattr(drn_Wait, "tempsCST")
    descriptor = None
    for klass in drn_Wait.__mro__:
        if "tempsCST" in klass.__dict__:
            descriptor = klass.__dict__["tempsCST"]
            break
    assert isinstance(descriptor, property)



def test_drn_depxy_impl_is_not_abstract():
    assert not inspect.isabstract(drn_DepXY_IMPL)


def test_drn_depxy_impl_constructor_exists():
    assert callable(drn_DepXY_IMPL.__init__)


def test_drn_depxy_impl_constructor_args():
    sig = inspect.signature(drn_DepXY_IMPL.__init__)
    params = list(sig.parameters.keys())
    assert "tempsCST" in params, "Missing parameter 'tempsCST'"
    assert "name" in params, "Missing parameter 'name'"

def test_drn_depxy_impl_has_tempsCST():
    assert hasattr(drn_DepXY_IMPL, "tempsCST")
    descriptor = None
    for klass in drn_DepXY_IMPL.__mro__:
        if "tempsCST" in klass.__dict__:
            descriptor = klass.__dict__["tempsCST"]
            break
    assert isinstance(descriptor, property)

def test_drn_depxy_impl_has_name():
    assert hasattr(drn_DepXY_IMPL, "name")
    descriptor = None
    for klass in drn_DepXY_IMPL.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_drn_movement_is_not_abstract():
    assert not inspect.isabstract(drn_Movement)


def test_drn_movement_constructor_exists():
    assert callable(drn_Movement.__init__)


def test_drn_movement_constructor_args():
    sig = inspect.signature(drn_Movement.__init__)
    params = list(sig.parameters.keys())



def test_drn_expression_is_not_abstract():
    assert not inspect.isabstract(drn_Expression)


def test_drn_expression_constructor_exists():
    assert callable(drn_Expression.__init__)


def test_drn_expression_constructor_args():
    sig = inspect.signature(drn_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "repeatCST" in params, "Missing parameter 'repeatCST'"

def test_drn_expression_has_repeatCST():
    assert hasattr(drn_Expression, "repeatCST")
    descriptor = None
    for klass in drn_Expression.__mro__:
        if "repeatCST" in klass.__dict__:
            descriptor = klass.__dict__["repeatCST"]
            break
    assert isinstance(descriptor, property)



def test_surface_is_not_abstract():
    assert not inspect.isabstract(Surface)


def test_surface_constructor_exists():
    assert callable(Surface.__init__)


def test_surface_constructor_args():
    sig = inspect.signature(Surface.__init__)
    params = list(sig.parameters.keys())



def test_drn_maxheight_is_not_abstract():
    assert not inspect.isabstract(drn_MaxHeight)


def test_drn_maxheight_constructor_exists():
    assert callable(drn_MaxHeight.__init__)


def test_drn_maxheight_constructor_args():
    sig = inspect.signature(drn_MaxHeight.__init__)
    params = list(sig.parameters.keys())



def test_drn_maxwidth_is_not_abstract():
    assert not inspect.isabstract(drn_MaxWidth)


def test_drn_maxwidth_constructor_exists():
    assert callable(drn_MaxWidth.__init__)


def test_drn_maxwidth_constructor_args():
    sig = inspect.signature(drn_MaxWidth.__init__)
    params = list(sig.parameters.keys())



def test_drn_maxlength_is_not_abstract():
    assert not inspect.isabstract(drn_MaxLength)


def test_drn_maxlength_constructor_exists():
    assert callable(drn_MaxLength.__init__)


def test_drn_maxlength_constructor_args():
    sig = inspect.signature(drn_MaxLength.__init__)
    params = list(sig.parameters.keys())



def test_initialposition_is_not_abstract():
    assert not inspect.isabstract(InitialPosition)


def test_initialposition_constructor_exists():
    assert callable(InitialPosition.__init__)


def test_initialposition_constructor_args():
    sig = inspect.signature(InitialPosition.__init__)
    params = list(sig.parameters.keys())



def test_drn_initialpositiony_is_not_abstract():
    assert not inspect.isabstract(drn_InitialPositionY)


def test_drn_initialpositiony_constructor_exists():
    assert callable(drn_InitialPositionY.__init__)


def test_drn_initialpositiony_constructor_args():
    sig = inspect.signature(drn_InitialPositionY.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_drn_initialpositiony_has_value():
    assert hasattr(drn_InitialPositionY, "value")
    descriptor = None
    for klass in drn_InitialPositionY.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_drn_initialpositionx_is_not_abstract():
    assert not inspect.isabstract(drn_InitialPositionX)


def test_drn_initialpositionx_constructor_exists():
    assert callable(drn_InitialPositionX.__init__)


def test_drn_initialpositionx_constructor_args():
    sig = inspect.signature(drn_InitialPositionX.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_drn_initialpositionx_has_value():
    assert hasattr(drn_InitialPositionX, "value")
    descriptor = None
    for klass in drn_InitialPositionX.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_drn_initialdirection_is_not_abstract():
    assert not inspect.isabstract(drn_InitialDirection)


def test_drn_initialdirection_constructor_exists():
    assert callable(drn_InitialDirection.__init__)


def test_drn_initialdirection_constructor_args():
    sig = inspect.signature(drn_InitialDirection.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_drn_initialdirection_has_value():
    assert hasattr(drn_InitialDirection, "value")
    descriptor = None
    for klass in drn_InitialDirection.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_limit_is_not_abstract():
    assert not inspect.isabstract(Limit)


def test_limit_constructor_exists():
    assert callable(Limit.__init__)


def test_limit_constructor_args():
    sig = inspect.signature(Limit.__init__)
    params = list(sig.parameters.keys())



def test_drn_initialposition_is_not_abstract():
    assert not inspect.isabstract(drn_InitialPosition)


def test_drn_initialposition_constructor_exists():
    assert callable(drn_InitialPosition.__init__)


def test_drn_initialposition_constructor_args():
    sig = inspect.signature(drn_InitialPosition.__init__)
    params = list(sig.parameters.keys())



def test_drn_maxspeed_is_not_abstract():
    assert not inspect.isabstract(drn_MaxSpeed)


def test_drn_maxspeed_constructor_exists():
    assert callable(drn_MaxSpeed.__init__)


def test_drn_maxspeed_constructor_args():
    sig = inspect.signature(drn_MaxSpeed.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_drn_maxspeed_has_value():
    assert hasattr(drn_MaxSpeed, "value")
    descriptor = None
    for klass in drn_MaxSpeed.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_drn_surface_is_not_abstract():
    assert not inspect.isabstract(drn_Surface)


def test_drn_surface_constructor_exists():
    assert callable(drn_Surface.__init__)


def test_drn_surface_constructor_args():
    sig = inspect.signature(drn_Surface.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_drn_surface_has_value():
    assert hasattr(drn_Surface, "value")
    descriptor = None
    for klass in drn_Surface.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_drn_limit_is_not_abstract():
    assert not inspect.isabstract(drn_Limit)


def test_drn_limit_constructor_exists():
    assert callable(drn_Limit.__init__)


def test_drn_limit_constructor_args():
    sig = inspect.signature(drn_Limit.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_drn_limit_has_name():
    assert hasattr(drn_Limit, "name")
    descriptor = None
    for klass in drn_Limit.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_drn_connectiontype_is_not_abstract():
    assert not inspect.isabstract(drn_ConnectionType)


def test_drn_connectiontype_constructor_exists():
    assert callable(drn_ConnectionType.__init__)


def test_drn_connectiontype_constructor_args():
    sig = inspect.signature(drn_ConnectionType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "adress" in params, "Missing parameter 'adress'"

def test_drn_connectiontype_has_name():
    assert hasattr(drn_ConnectionType, "name")
    descriptor = None
    for klass in drn_ConnectionType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_drn_connectiontype_has_adress():
    assert hasattr(drn_ConnectionType, "adress")
    descriptor = None
    for klass in drn_ConnectionType.__mro__:
        if "adress" in klass.__dict__:
            descriptor = klass.__dict__["adress"]
            break
    assert isinstance(descriptor, property)



def test_drn_device_is_not_abstract():
    assert not inspect.isabstract(drn_Device)


def test_drn_device_constructor_exists():
    assert callable(drn_Device.__init__)


def test_drn_device_constructor_args():
    sig = inspect.signature(drn_Device.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_drn_device_has_name():
    assert hasattr(drn_Device, "name")
    descriptor = None
    for klass in drn_Device.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_drn_typegeneric_is_not_abstract():
    assert not inspect.isabstract(drn_TypeGeneric)


def test_drn_typegeneric_constructor_exists():
    assert callable(drn_TypeGeneric.__init__)


def test_drn_typegeneric_constructor_args():
    sig = inspect.signature(drn_TypeGeneric.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_drn_typegeneric_has_name():
    assert hasattr(drn_TypeGeneric, "name")
    descriptor = None
    for klass in drn_TypeGeneric.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_drn_refpart_is_not_abstract():
    assert not inspect.isabstract(drn_RefPart)


def test_drn_refpart_constructor_exists():
    assert callable(drn_RefPart.__init__)


def test_drn_refpart_constructor_args():
    sig = inspect.signature(drn_RefPart.__init__)
    params = list(sig.parameters.keys())



def test_drn_context_is_not_abstract():
    assert not inspect.isabstract(drn_Context)


def test_drn_context_constructor_exists():
    assert callable(drn_Context.__init__)


def test_drn_context_constructor_args():
    sig = inspect.signature(drn_Context.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "where" in params, "Missing parameter 'where'"

def test_drn_context_has_name():
    assert hasattr(drn_Context, "name")
    descriptor = None
    for klass in drn_Context.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_drn_context_has_where():
    assert hasattr(drn_Context, "where")
    descriptor = None
    for klass in drn_Context.__mro__:
        if "where" in klass.__dict__:
            descriptor = klass.__dict__["where"]
            break
    assert isinstance(descriptor, property)



def test_drn_with_is_not_abstract():
    assert not inspect.isabstract(drn_With)


def test_drn_with_constructor_exists():
    assert callable(drn_With.__init__)


def test_drn_with_constructor_args():
    sig = inspect.signature(drn_With.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_drn_with_has_name():
    assert hasattr(drn_With, "name")
    descriptor = None
    for klass in drn_With.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_drn_assignement_is_not_abstract():
    assert not inspect.isabstract(drn_Assignement)


def test_drn_assignement_constructor_exists():
    assert callable(drn_Assignement.__init__)


def test_drn_assignement_constructor_args():
    sig = inspect.signature(drn_Assignement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_drn_assignement_has_name():
    assert hasattr(drn_Assignement, "name")
    descriptor = None
    for klass in drn_Assignement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_root_is_not_abstract():
    assert not inspect.isabstract(Root)


def test_root_constructor_exists():
    assert callable(Root.__init__)


def test_root_constructor_args():
    sig = inspect.signature(Root.__init__)
    params = list(sig.parameters.keys())



def test_drn_configuration_is_not_abstract():
    assert not inspect.isabstract(drn_Configuration)


def test_drn_configuration_constructor_exists():
    assert callable(drn_Configuration.__init__)


def test_drn_configuration_constructor_args():
    sig = inspect.signature(drn_Configuration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_drn_configuration_has_name():
    assert hasattr(drn_Configuration, "name")
    descriptor = None
    for klass in drn_Configuration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_drn_library_is_not_abstract():
    assert not inspect.isabstract(drn_Library)


def test_drn_library_constructor_exists():
    assert callable(drn_Library.__init__)


def test_drn_library_constructor_args():
    sig = inspect.signature(drn_Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_drn_library_has_name():
    assert hasattr(drn_Library, "name")
    descriptor = None
    for klass in drn_Library.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_drn_model_is_not_abstract():
    assert not inspect.isabstract(drn_Model)


def test_drn_model_constructor_exists():
    assert callable(drn_Model.__init__)


def test_drn_model_constructor_args():
    sig = inspect.signature(drn_Model.__init__)
    params = list(sig.parameters.keys())



def test_drn_root_is_not_abstract():
    assert not inspect.isabstract(drn_Root)


def test_drn_root_constructor_exists():
    assert callable(drn_Root.__init__)


def test_drn_root_constructor_args():
    sig = inspect.signature(drn_Root.__init__)
    params = list(sig.parameters.keys())

def test_ebool_exists():
    # Check that the Enumeration exists
    assert EBool is not None

def test_ebool_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EBool]
    expected_literals = [
        "TRUE",
        "FALSE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EBool"

def test_mode_exists():
    # Check that the Enumeration exists
    assert Mode is not None

def test_mode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Mode]
    expected_literals = [
        "ON",
        "OFF",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Mode"

def test_typeprimitif_exists():
    # Check that the Enumeration exists
    assert TypePrimitif is not None

def test_typeprimitif_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypePrimitif]
    expected_literals = [
        "realType",
        "boolType",
        "intType",
        "stringType",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypePrimitif"

def test_where_exists():
    # Check that the Enumeration exists
    assert Where is not None

def test_where_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Where]
    expected_literals = [
        "OUTDOOR",
        "INDOOR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Where"

def test_directiontype_exists():
    # Check that the Enumeration exists
    assert DirectionType is not None

def test_directiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DirectionType]
    expected_literals = [
        "RIGHT",
        "LEFT",
        "BEHIND",
        "FRONT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DirectionType"


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
ConnectionType_strategy = st.builds(
    ConnectionType,
)
drn_Wifi_strategy = st.builds(
    drn_Wifi,
)
drn_Bluetooth_strategy = st.builds(
    drn_Bluetooth,
)
drn_RefDevice_strategy = st.builds(
    drn_RefDevice,
    mode=
        safe_text
)
drn_Element_strategy = st.builds(
    drn_Element,
    name=
        safe_text
)
drn_Definition_strategy = st.builds(
    drn_Definition,
    int=
        safe_text,
    real=
        safe_text,
    bool=
        safe_text,
    text=
        safe_text
)
drn_Declaration_strategy = st.builds(
    drn_Declaration,
    name=
        safe_text,
    typePrimitif=
        safe_text
)
DepXYZ_IMPL_strategy = st.builds(
    DepXYZ_IMPL,
)
drn_Flip_strategy = st.builds(
    drn_Flip,
    name=
        safe_text
)
DepXZ_IMPL_strategy = st.builds(
    DepXZ_IMPL,
)
drn_CARREXZ_strategy = st.builds(
    drn_CARREXZ,
    coteCST=
        st.integers()
)
drn_CERCLEXZ_strategy = st.builds(
    drn_CERCLEXZ,
    rayonCST=
        st.integers()
)
DepYZ_IMPL_strategy = st.builds(
    DepYZ_IMPL,
)
drn_CARREYZ_strategy = st.builds(
    drn_CARREYZ,
    coteCST=
        st.integers()
)
drn_CERCLEYZ_strategy = st.builds(
    drn_CERCLEYZ,
    rayonCST=
        st.integers()
)
DepXY_IMPL_strategy = st.builds(
    DepXY_IMPL,
)
drn_CARREXY_strategy = st.builds(
    drn_CARREXY,
    coteCST=
        st.integers()
)
drn_CERCLEXY_strategy = st.builds(
    drn_CERCLEXY,
    rayonCST=
        st.integers()
)
DepZ_Impl_strategy = st.builds(
    DepZ_Impl,
)
drn_DOWN_strategy = st.builds(
    drn_DOWN,
)
drn_UP_strategy = st.builds(
    drn_UP,
)
DepX_Impl_strategy = st.builds(
    DepX_Impl,
)
drn_RIGHT_strategy = st.builds(
    drn_RIGHT,
)
drn_LEFT_strategy = st.builds(
    drn_LEFT,
)
DepY_Impl_strategy = st.builds(
    DepY_Impl,
)
drn_BACKWARD_strategy = st.builds(
    drn_BACKWARD,
)
drn_FORWARD_strategy = st.builds(
    drn_FORWARD,
)
Movement_strategy = st.builds(
    Movement,
)
drn_DepX_Impl_strategy = st.builds(
    drn_DepX_Impl,
    distanceCST=
        st.integers(),
    tempsCST=
        st.integers(),
    name=
        safe_text
)
drn_And_strategy = st.builds(
    drn_And,
    name=
        safe_text
)
drn_TakeOff_strategy = st.builds(
    drn_TakeOff,
    name=
        safe_text
)
drn_DepXZ_IMPL_strategy = st.builds(
    drn_DepXZ_IMPL,
    name=
        safe_text,
    tempsCST=
        st.integers()
)
drn_DepZ_Impl_strategy = st.builds(
    drn_DepZ_Impl,
    name=
        safe_text,
    distanceCST=
        st.integers(),
    tempsCST=
        st.integers()
)
drn_RefPartLib_strategy = st.builds(
    drn_RefPartLib,
)
drn_DepXYZ_IMPL_strategy = st.builds(
    drn_DepXYZ_IMPL,
)
drn_DepYZ_IMPL_strategy = st.builds(
    drn_DepYZ_IMPL,
    name=
        safe_text,
    tempsCST=
        st.integers()
)
drn_Rotate_strategy = st.builds(
    drn_Rotate,
    angleCST=
        safe_text,
    name=
        safe_text,
    tempsCST=
        st.integers()
)
drn_DepY_Impl_strategy = st.builds(
    drn_DepY_Impl,
    tempsCST=
        st.integers(),
    name=
        safe_text,
    distanceCST=
        st.integers()
)
drn_Land_strategy = st.builds(
    drn_Land,
    name=
        safe_text
)
drn_Wait_strategy = st.builds(
    drn_Wait,
    name=
        safe_text,
    tempsCST=
        st.integers()
)
drn_DepXY_IMPL_strategy = st.builds(
    drn_DepXY_IMPL,
    tempsCST=
        st.integers(),
    name=
        safe_text
)
drn_Movement_strategy = st.builds(
    drn_Movement,
)
drn_Expression_strategy = st.builds(
    drn_Expression,
    repeatCST=
        st.integers()
)
Surface_strategy = st.builds(
    Surface,
)
drn_MaxHeight_strategy = st.builds(
    drn_MaxHeight,
)
drn_MaxWidth_strategy = st.builds(
    drn_MaxWidth,
)
drn_MaxLength_strategy = st.builds(
    drn_MaxLength,
)
InitialPosition_strategy = st.builds(
    InitialPosition,
)
drn_InitialPositionY_strategy = st.builds(
    drn_InitialPositionY,
    value=
        st.integers()
)
drn_InitialPositionX_strategy = st.builds(
    drn_InitialPositionX,
    value=
        st.integers()
)
drn_InitialDirection_strategy = st.builds(
    drn_InitialDirection,
    value=
        safe_text
)
Limit_strategy = st.builds(
    Limit,
)
drn_InitialPosition_strategy = st.builds(
    drn_InitialPosition,
)
drn_MaxSpeed_strategy = st.builds(
    drn_MaxSpeed,
    value=
        st.integers()
)
drn_Surface_strategy = st.builds(
    drn_Surface,
    value=
        st.integers()
)
drn_Limit_strategy = st.builds(
    drn_Limit,
    name=
        safe_text
)
drn_ConnectionType_strategy = st.builds(
    drn_ConnectionType,
    name=
        safe_text,
    adress=
        safe_text
)
drn_Device_strategy = st.builds(
    drn_Device,
    name=
        safe_text
)
drn_TypeGeneric_strategy = st.builds(
    drn_TypeGeneric,
    name=
        safe_text
)
drn_RefPart_strategy = st.builds(
    drn_RefPart,
)
drn_Context_strategy = st.builds(
    drn_Context,
    name=
        safe_text,
    where=
        safe_text
)
drn_With_strategy = st.builds(
    drn_With,
    name=
        safe_text
)
drn_Assignement_strategy = st.builds(
    drn_Assignement,
    name=
        safe_text
)
Root_strategy = st.builds(
    Root,
)
drn_Configuration_strategy = st.builds(
    drn_Configuration,
    name=
        safe_text
)
drn_Library_strategy = st.builds(
    drn_Library,
    name=
        safe_text
)
drn_Model_strategy = st.builds(
    drn_Model,
)
drn_Root_strategy = st.builds(
    drn_Root,
)

@given(instance=ConnectionType_strategy)
@settings(max_examples=50)
def test_connectiontype_instantiation(instance):
    assert isinstance(instance, ConnectionType)

@given(instance=drn_Wifi_strategy)
@settings(max_examples=50)
def test_drn_wifi_instantiation(instance):
    assert isinstance(instance, drn_Wifi)

@given(instance=drn_Bluetooth_strategy)
@settings(max_examples=50)
def test_drn_bluetooth_instantiation(instance):
    assert isinstance(instance, drn_Bluetooth)

@given(instance=drn_RefDevice_strategy)
@settings(max_examples=50)
def test_drn_refdevice_instantiation(instance):
    assert isinstance(instance, drn_RefDevice)



@given(instance=drn_RefDevice_strategy)
def test_drn_refdevice_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=drn_Element_strategy)
@settings(max_examples=50)
def test_drn_element_instantiation(instance):
    assert isinstance(instance, drn_Element)



@given(instance=drn_Element_strategy)
def test_drn_element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=drn_Definition_strategy)
@settings(max_examples=50)
def test_drn_definition_instantiation(instance):
    assert isinstance(instance, drn_Definition)



@given(instance=drn_Definition_strategy)
def test_drn_definition_int_setter(instance):
    original = instance.int
    instance.int = original
    assert instance.int == original



@given(instance=drn_Definition_strategy)
def test_drn_definition_real_setter(instance):
    original = instance.real
    instance.real = original
    assert instance.real == original



@given(instance=drn_Definition_strategy)
def test_drn_definition_bool_setter(instance):
    original = instance.bool
    instance.bool = original
    assert instance.bool == original



@given(instance=drn_Definition_strategy)
def test_drn_definition_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=drn_Declaration_strategy)
@settings(max_examples=50)
def test_drn_declaration_instantiation(instance):
    assert isinstance(instance, drn_Declaration)



@given(instance=drn_Declaration_strategy)
def test_drn_declaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=drn_Declaration_strategy)
def test_drn_declaration_typePrimitif_setter(instance):
    original = instance.typePrimitif
    instance.typePrimitif = original
    assert instance.typePrimitif == original

@given(instance=DepXYZ_IMPL_strategy)
@settings(max_examples=50)
def test_depxyz_impl_instantiation(instance):
    assert isinstance(instance, DepXYZ_IMPL)

@given(instance=drn_Flip_strategy)
@settings(max_examples=50)
def test_drn_flip_instantiation(instance):
    assert isinstance(instance, drn_Flip)



@given(instance=drn_Flip_strategy)
def test_drn_flip_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DepXZ_IMPL_strategy)
@settings(max_examples=50)
def test_depxz_impl_instantiation(instance):
    assert isinstance(instance, DepXZ_IMPL)

@given(instance=drn_CARREXZ_strategy)
@settings(max_examples=50)
def test_drn_carrexz_instantiation(instance):
    assert isinstance(instance, drn_CARREXZ)



@given(instance=drn_CARREXZ_strategy)
def test_drn_carrexz_coteCST_setter(instance):
    original = instance.coteCST
    instance.coteCST = original
    assert instance.coteCST == original

@given(instance=drn_CERCLEXZ_strategy)
@settings(max_examples=50)
def test_drn_cerclexz_instantiation(instance):
    assert isinstance(instance, drn_CERCLEXZ)



@given(instance=drn_CERCLEXZ_strategy)
def test_drn_cerclexz_rayonCST_setter(instance):
    original = instance.rayonCST
    instance.rayonCST = original
    assert instance.rayonCST == original

@given(instance=DepYZ_IMPL_strategy)
@settings(max_examples=50)
def test_depyz_impl_instantiation(instance):
    assert isinstance(instance, DepYZ_IMPL)

@given(instance=drn_CARREYZ_strategy)
@settings(max_examples=50)
def test_drn_carreyz_instantiation(instance):
    assert isinstance(instance, drn_CARREYZ)



@given(instance=drn_CARREYZ_strategy)
def test_drn_carreyz_coteCST_setter(instance):
    original = instance.coteCST
    instance.coteCST = original
    assert instance.coteCST == original

@given(instance=drn_CERCLEYZ_strategy)
@settings(max_examples=50)
def test_drn_cercleyz_instantiation(instance):
    assert isinstance(instance, drn_CERCLEYZ)



@given(instance=drn_CERCLEYZ_strategy)
def test_drn_cercleyz_rayonCST_setter(instance):
    original = instance.rayonCST
    instance.rayonCST = original
    assert instance.rayonCST == original

@given(instance=DepXY_IMPL_strategy)
@settings(max_examples=50)
def test_depxy_impl_instantiation(instance):
    assert isinstance(instance, DepXY_IMPL)

@given(instance=drn_CARREXY_strategy)
@settings(max_examples=50)
def test_drn_carrexy_instantiation(instance):
    assert isinstance(instance, drn_CARREXY)



@given(instance=drn_CARREXY_strategy)
def test_drn_carrexy_coteCST_setter(instance):
    original = instance.coteCST
    instance.coteCST = original
    assert instance.coteCST == original

@given(instance=drn_CERCLEXY_strategy)
@settings(max_examples=50)
def test_drn_cerclexy_instantiation(instance):
    assert isinstance(instance, drn_CERCLEXY)



@given(instance=drn_CERCLEXY_strategy)
def test_drn_cerclexy_rayonCST_setter(instance):
    original = instance.rayonCST
    instance.rayonCST = original
    assert instance.rayonCST == original

@given(instance=DepZ_Impl_strategy)
@settings(max_examples=50)
def test_depz_impl_instantiation(instance):
    assert isinstance(instance, DepZ_Impl)

@given(instance=drn_DOWN_strategy)
@settings(max_examples=50)
def test_drn_down_instantiation(instance):
    assert isinstance(instance, drn_DOWN)

@given(instance=drn_UP_strategy)
@settings(max_examples=50)
def test_drn_up_instantiation(instance):
    assert isinstance(instance, drn_UP)

@given(instance=DepX_Impl_strategy)
@settings(max_examples=50)
def test_depx_impl_instantiation(instance):
    assert isinstance(instance, DepX_Impl)

@given(instance=drn_RIGHT_strategy)
@settings(max_examples=50)
def test_drn_right_instantiation(instance):
    assert isinstance(instance, drn_RIGHT)

@given(instance=drn_LEFT_strategy)
@settings(max_examples=50)
def test_drn_left_instantiation(instance):
    assert isinstance(instance, drn_LEFT)

@given(instance=DepY_Impl_strategy)
@settings(max_examples=50)
def test_depy_impl_instantiation(instance):
    assert isinstance(instance, DepY_Impl)

@given(instance=drn_BACKWARD_strategy)
@settings(max_examples=50)
def test_drn_backward_instantiation(instance):
    assert isinstance(instance, drn_BACKWARD)

@given(instance=drn_FORWARD_strategy)
@settings(max_examples=50)
def test_drn_forward_instantiation(instance):
    assert isinstance(instance, drn_FORWARD)

@given(instance=Movement_strategy)
@settings(max_examples=50)
def test_movement_instantiation(instance):
    assert isinstance(instance, Movement)

@given(instance=drn_DepX_Impl_strategy)
@settings(max_examples=50)
def test_drn_depx_impl_instantiation(instance):
    assert isinstance(instance, drn_DepX_Impl)



@given(instance=drn_DepX_Impl_strategy)
def test_drn_depx_impl_distanceCST_setter(instance):
    original = instance.distanceCST
    instance.distanceCST = original
    assert instance.distanceCST == original



@given(instance=drn_DepX_Impl_strategy)
def test_drn_depx_impl_tempsCST_setter(instance):
    original = instance.tempsCST
    instance.tempsCST = original
    assert instance.tempsCST == original



@given(instance=drn_DepX_Impl_strategy)
def test_drn_depx_impl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=drn_And_strategy)
@settings(max_examples=50)
def test_drn_and_instantiation(instance):
    assert isinstance(instance, drn_And)



@given(instance=drn_And_strategy)
def test_drn_and_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=drn_TakeOff_strategy)
@settings(max_examples=50)
def test_drn_takeoff_instantiation(instance):
    assert isinstance(instance, drn_TakeOff)



@given(instance=drn_TakeOff_strategy)
def test_drn_takeoff_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=drn_DepXZ_IMPL_strategy)
@settings(max_examples=50)
def test_drn_depxz_impl_instantiation(instance):
    assert isinstance(instance, drn_DepXZ_IMPL)



@given(instance=drn_DepXZ_IMPL_strategy)
def test_drn_depxz_impl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=drn_DepXZ_IMPL_strategy)
def test_drn_depxz_impl_tempsCST_setter(instance):
    original = instance.tempsCST
    instance.tempsCST = original
    assert instance.tempsCST == original

@given(instance=drn_DepZ_Impl_strategy)
@settings(max_examples=50)
def test_drn_depz_impl_instantiation(instance):
    assert isinstance(instance, drn_DepZ_Impl)



@given(instance=drn_DepZ_Impl_strategy)
def test_drn_depz_impl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=drn_DepZ_Impl_strategy)
def test_drn_depz_impl_distanceCST_setter(instance):
    original = instance.distanceCST
    instance.distanceCST = original
    assert instance.distanceCST == original



@given(instance=drn_DepZ_Impl_strategy)
def test_drn_depz_impl_tempsCST_setter(instance):
    original = instance.tempsCST
    instance.tempsCST = original
    assert instance.tempsCST == original

@given(instance=drn_RefPartLib_strategy)
@settings(max_examples=50)
def test_drn_refpartlib_instantiation(instance):
    assert isinstance(instance, drn_RefPartLib)

@given(instance=drn_DepXYZ_IMPL_strategy)
@settings(max_examples=50)
def test_drn_depxyz_impl_instantiation(instance):
    assert isinstance(instance, drn_DepXYZ_IMPL)

@given(instance=drn_DepYZ_IMPL_strategy)
@settings(max_examples=50)
def test_drn_depyz_impl_instantiation(instance):
    assert isinstance(instance, drn_DepYZ_IMPL)



@given(instance=drn_DepYZ_IMPL_strategy)
def test_drn_depyz_impl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=drn_DepYZ_IMPL_strategy)
def test_drn_depyz_impl_tempsCST_setter(instance):
    original = instance.tempsCST
    instance.tempsCST = original
    assert instance.tempsCST == original

@given(instance=drn_Rotate_strategy)
@settings(max_examples=50)
def test_drn_rotate_instantiation(instance):
    assert isinstance(instance, drn_Rotate)



@given(instance=drn_Rotate_strategy)
def test_drn_rotate_angleCST_setter(instance):
    original = instance.angleCST
    instance.angleCST = original
    assert instance.angleCST == original



@given(instance=drn_Rotate_strategy)
def test_drn_rotate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=drn_Rotate_strategy)
def test_drn_rotate_tempsCST_setter(instance):
    original = instance.tempsCST
    instance.tempsCST = original
    assert instance.tempsCST == original

@given(instance=drn_DepY_Impl_strategy)
@settings(max_examples=50)
def test_drn_depy_impl_instantiation(instance):
    assert isinstance(instance, drn_DepY_Impl)



@given(instance=drn_DepY_Impl_strategy)
def test_drn_depy_impl_tempsCST_setter(instance):
    original = instance.tempsCST
    instance.tempsCST = original
    assert instance.tempsCST == original



@given(instance=drn_DepY_Impl_strategy)
def test_drn_depy_impl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=drn_DepY_Impl_strategy)
def test_drn_depy_impl_distanceCST_setter(instance):
    original = instance.distanceCST
    instance.distanceCST = original
    assert instance.distanceCST == original

@given(instance=drn_Land_strategy)
@settings(max_examples=50)
def test_drn_land_instantiation(instance):
    assert isinstance(instance, drn_Land)



@given(instance=drn_Land_strategy)
def test_drn_land_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=drn_Wait_strategy)
@settings(max_examples=50)
def test_drn_wait_instantiation(instance):
    assert isinstance(instance, drn_Wait)



@given(instance=drn_Wait_strategy)
def test_drn_wait_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=drn_Wait_strategy)
def test_drn_wait_tempsCST_setter(instance):
    original = instance.tempsCST
    instance.tempsCST = original
    assert instance.tempsCST == original

@given(instance=drn_DepXY_IMPL_strategy)
@settings(max_examples=50)
def test_drn_depxy_impl_instantiation(instance):
    assert isinstance(instance, drn_DepXY_IMPL)



@given(instance=drn_DepXY_IMPL_strategy)
def test_drn_depxy_impl_tempsCST_setter(instance):
    original = instance.tempsCST
    instance.tempsCST = original
    assert instance.tempsCST == original



@given(instance=drn_DepXY_IMPL_strategy)
def test_drn_depxy_impl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=drn_Movement_strategy)
@settings(max_examples=50)
def test_drn_movement_instantiation(instance):
    assert isinstance(instance, drn_Movement)

@given(instance=drn_Expression_strategy)
@settings(max_examples=50)
def test_drn_expression_instantiation(instance):
    assert isinstance(instance, drn_Expression)



@given(instance=drn_Expression_strategy)
def test_drn_expression_repeatCST_setter(instance):
    original = instance.repeatCST
    instance.repeatCST = original
    assert instance.repeatCST == original

@given(instance=Surface_strategy)
@settings(max_examples=50)
def test_surface_instantiation(instance):
    assert isinstance(instance, Surface)

@given(instance=drn_MaxHeight_strategy)
@settings(max_examples=50)
def test_drn_maxheight_instantiation(instance):
    assert isinstance(instance, drn_MaxHeight)

@given(instance=drn_MaxWidth_strategy)
@settings(max_examples=50)
def test_drn_maxwidth_instantiation(instance):
    assert isinstance(instance, drn_MaxWidth)

@given(instance=drn_MaxLength_strategy)
@settings(max_examples=50)
def test_drn_maxlength_instantiation(instance):
    assert isinstance(instance, drn_MaxLength)

@given(instance=InitialPosition_strategy)
@settings(max_examples=50)
def test_initialposition_instantiation(instance):
    assert isinstance(instance, InitialPosition)

@given(instance=drn_InitialPositionY_strategy)
@settings(max_examples=50)
def test_drn_initialpositiony_instantiation(instance):
    assert isinstance(instance, drn_InitialPositionY)



@given(instance=drn_InitialPositionY_strategy)
def test_drn_initialpositiony_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=drn_InitialPositionX_strategy)
@settings(max_examples=50)
def test_drn_initialpositionx_instantiation(instance):
    assert isinstance(instance, drn_InitialPositionX)



@given(instance=drn_InitialPositionX_strategy)
def test_drn_initialpositionx_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=drn_InitialDirection_strategy)
@settings(max_examples=50)
def test_drn_initialdirection_instantiation(instance):
    assert isinstance(instance, drn_InitialDirection)



@given(instance=drn_InitialDirection_strategy)
def test_drn_initialdirection_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Limit_strategy)
@settings(max_examples=50)
def test_limit_instantiation(instance):
    assert isinstance(instance, Limit)

@given(instance=drn_InitialPosition_strategy)
@settings(max_examples=50)
def test_drn_initialposition_instantiation(instance):
    assert isinstance(instance, drn_InitialPosition)

@given(instance=drn_MaxSpeed_strategy)
@settings(max_examples=50)
def test_drn_maxspeed_instantiation(instance):
    assert isinstance(instance, drn_MaxSpeed)



@given(instance=drn_MaxSpeed_strategy)
def test_drn_maxspeed_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=drn_Surface_strategy)
@settings(max_examples=50)
def test_drn_surface_instantiation(instance):
    assert isinstance(instance, drn_Surface)



@given(instance=drn_Surface_strategy)
def test_drn_surface_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=drn_Limit_strategy)
@settings(max_examples=50)
def test_drn_limit_instantiation(instance):
    assert isinstance(instance, drn_Limit)



@given(instance=drn_Limit_strategy)
def test_drn_limit_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=drn_ConnectionType_strategy)
@settings(max_examples=50)
def test_drn_connectiontype_instantiation(instance):
    assert isinstance(instance, drn_ConnectionType)



@given(instance=drn_ConnectionType_strategy)
def test_drn_connectiontype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=drn_ConnectionType_strategy)
def test_drn_connectiontype_adress_setter(instance):
    original = instance.adress
    instance.adress = original
    assert instance.adress == original

@given(instance=drn_Device_strategy)
@settings(max_examples=50)
def test_drn_device_instantiation(instance):
    assert isinstance(instance, drn_Device)



@given(instance=drn_Device_strategy)
def test_drn_device_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=drn_TypeGeneric_strategy)
@settings(max_examples=50)
def test_drn_typegeneric_instantiation(instance):
    assert isinstance(instance, drn_TypeGeneric)



@given(instance=drn_TypeGeneric_strategy)
def test_drn_typegeneric_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=drn_RefPart_strategy)
@settings(max_examples=50)
def test_drn_refpart_instantiation(instance):
    assert isinstance(instance, drn_RefPart)

@given(instance=drn_Context_strategy)
@settings(max_examples=50)
def test_drn_context_instantiation(instance):
    assert isinstance(instance, drn_Context)



@given(instance=drn_Context_strategy)
def test_drn_context_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=drn_Context_strategy)
def test_drn_context_where_setter(instance):
    original = instance.where
    instance.where = original
    assert instance.where == original

@given(instance=drn_With_strategy)
@settings(max_examples=50)
def test_drn_with_instantiation(instance):
    assert isinstance(instance, drn_With)



@given(instance=drn_With_strategy)
def test_drn_with_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=drn_Assignement_strategy)
@settings(max_examples=50)
def test_drn_assignement_instantiation(instance):
    assert isinstance(instance, drn_Assignement)



@given(instance=drn_Assignement_strategy)
def test_drn_assignement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Root_strategy)
@settings(max_examples=50)
def test_root_instantiation(instance):
    assert isinstance(instance, Root)

@given(instance=drn_Configuration_strategy)
@settings(max_examples=50)
def test_drn_configuration_instantiation(instance):
    assert isinstance(instance, drn_Configuration)



@given(instance=drn_Configuration_strategy)
def test_drn_configuration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=drn_Library_strategy)
@settings(max_examples=50)
def test_drn_library_instantiation(instance):
    assert isinstance(instance, drn_Library)



@given(instance=drn_Library_strategy)
def test_drn_library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=drn_Model_strategy)
@settings(max_examples=50)
def test_drn_model_instantiation(instance):
    assert isinstance(instance, drn_Model)

@given(instance=drn_Root_strategy)
@settings(max_examples=50)
def test_drn_root_instantiation(instance):
    assert isinstance(instance, drn_Root)
