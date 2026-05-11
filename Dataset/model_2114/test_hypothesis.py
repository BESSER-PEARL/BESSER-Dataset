import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    securityTest::WebComponent,
    securityTest::AuthSetting,
    securityTest::Note,
    securityTest::Attack,
    securityTest::TargetOfEvaluation,
    securityTest::Input,
    securityTest::Test,
    ESeverity,
    EAttackMethod,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_securitytest::webcomponent_is_not_abstract():
    assert not inspect.isabstract(securityTest::WebComponent)


def test_securitytest::webcomponent_constructor_exists():
    assert callable(securityTest::WebComponent.__init__)


def test_securitytest::webcomponent_constructor_args():
    sig = inspect.signature(securityTest::WebComponent.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"

def test_securitytest::webcomponent_has_path():
    assert hasattr(securityTest::WebComponent, "path")
    descriptor = None
    for klass in securityTest::WebComponent.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)



def test_securitytest::authsetting_is_not_abstract():
    assert not inspect.isabstract(securityTest::AuthSetting)


def test_securitytest::authsetting_constructor_exists():
    assert callable(securityTest::AuthSetting.__init__)


def test_securitytest::authsetting_constructor_args():
    sig = inspect.signature(securityTest::AuthSetting.__init__)
    params = list(sig.parameters.keys())
    assert "loginTargetURL" in params, "Missing parameter 'loginTargetURL'"
    assert "usernameParam" in params, "Missing parameter 'usernameParam'"
    assert "passwordParam" in params, "Missing parameter 'passwordParam'"
    assert "roles" in params, "Missing parameter 'roles'"
    assert "loginMessagePattern" in params, "Missing parameter 'loginMessagePattern'"
    assert "logoutMessagePattern" in params, "Missing parameter 'logoutMessagePattern'"

def test_securitytest::authsetting_has_loginTargetURL():
    assert hasattr(securityTest::AuthSetting, "loginTargetURL")
    descriptor = None
    for klass in securityTest::AuthSetting.__mro__:
        if "loginTargetURL" in klass.__dict__:
            descriptor = klass.__dict__["loginTargetURL"]
            break
    assert isinstance(descriptor, property)

def test_securitytest::authsetting_has_usernameParam():
    assert hasattr(securityTest::AuthSetting, "usernameParam")
    descriptor = None
    for klass in securityTest::AuthSetting.__mro__:
        if "usernameParam" in klass.__dict__:
            descriptor = klass.__dict__["usernameParam"]
            break
    assert isinstance(descriptor, property)

def test_securitytest::authsetting_has_passwordParam():
    assert hasattr(securityTest::AuthSetting, "passwordParam")
    descriptor = None
    for klass in securityTest::AuthSetting.__mro__:
        if "passwordParam" in klass.__dict__:
            descriptor = klass.__dict__["passwordParam"]
            break
    assert isinstance(descriptor, property)

def test_securitytest::authsetting_has_roles():
    assert hasattr(securityTest::AuthSetting, "roles")
    descriptor = None
    for klass in securityTest::AuthSetting.__mro__:
        if "roles" in klass.__dict__:
            descriptor = klass.__dict__["roles"]
            break
    assert isinstance(descriptor, property)

def test_securitytest::authsetting_has_loginMessagePattern():
    assert hasattr(securityTest::AuthSetting, "loginMessagePattern")
    descriptor = None
    for klass in securityTest::AuthSetting.__mro__:
        if "loginMessagePattern" in klass.__dict__:
            descriptor = klass.__dict__["loginMessagePattern"]
            break
    assert isinstance(descriptor, property)

def test_securitytest::authsetting_has_logoutMessagePattern():
    assert hasattr(securityTest::AuthSetting, "logoutMessagePattern")
    descriptor = None
    for klass in securityTest::AuthSetting.__mro__:
        if "logoutMessagePattern" in klass.__dict__:
            descriptor = klass.__dict__["logoutMessagePattern"]
            break
    assert isinstance(descriptor, property)



def test_securitytest::note_is_not_abstract():
    assert not inspect.isabstract(securityTest::Note)


def test_securitytest::note_constructor_exists():
    assert callable(securityTest::Note.__init__)


def test_securitytest::note_constructor_args():
    sig = inspect.signature(securityTest::Note.__init__)
    params = list(sig.parameters.keys())
    assert "noteText" in params, "Missing parameter 'noteText'"

def test_securitytest::note_has_noteText():
    assert hasattr(securityTest::Note, "noteText")
    descriptor = None
    for klass in securityTest::Note.__mro__:
        if "noteText" in klass.__dict__:
            descriptor = klass.__dict__["noteText"]
            break
    assert isinstance(descriptor, property)



def test_securitytest::attack_is_not_abstract():
    assert not inspect.isabstract(securityTest::Attack)


def test_securitytest::attack_constructor_exists():
    assert callable(securityTest::Attack.__init__)


def test_securitytest::attack_constructor_args():
    sig = inspect.signature(securityTest::Attack.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "severity" in params, "Missing parameter 'severity'"

def test_securitytest::attack_has_name():
    assert hasattr(securityTest::Attack, "name")
    descriptor = None
    for klass in securityTest::Attack.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_securitytest::attack_has_severity():
    assert hasattr(securityTest::Attack, "severity")
    descriptor = None
    for klass in securityTest::Attack.__mro__:
        if "severity" in klass.__dict__:
            descriptor = klass.__dict__["severity"]
            break
    assert isinstance(descriptor, property)



def test_securitytest::targetofevaluation_is_not_abstract():
    assert not inspect.isabstract(securityTest::TargetOfEvaluation)


def test_securitytest::targetofevaluation_constructor_exists():
    assert callable(securityTest::TargetOfEvaluation.__init__)


def test_securitytest::targetofevaluation_constructor_args():
    sig = inspect.signature(securityTest::TargetOfEvaluation.__init__)
    params = list(sig.parameters.keys())
    assert "port" in params, "Missing parameter 'port'"
    assert "protocol" in params, "Missing parameter 'protocol'"
    assert "domain" in params, "Missing parameter 'domain'"
    assert "ip" in params, "Missing parameter 'ip'"

def test_securitytest::targetofevaluation_has_port():
    assert hasattr(securityTest::TargetOfEvaluation, "port")
    descriptor = None
    for klass in securityTest::TargetOfEvaluation.__mro__:
        if "port" in klass.__dict__:
            descriptor = klass.__dict__["port"]
            break
    assert isinstance(descriptor, property)

def test_securitytest::targetofevaluation_has_protocol():
    assert hasattr(securityTest::TargetOfEvaluation, "protocol")
    descriptor = None
    for klass in securityTest::TargetOfEvaluation.__mro__:
        if "protocol" in klass.__dict__:
            descriptor = klass.__dict__["protocol"]
            break
    assert isinstance(descriptor, property)

def test_securitytest::targetofevaluation_has_domain():
    assert hasattr(securityTest::TargetOfEvaluation, "domain")
    descriptor = None
    for klass in securityTest::TargetOfEvaluation.__mro__:
        if "domain" in klass.__dict__:
            descriptor = klass.__dict__["domain"]
            break
    assert isinstance(descriptor, property)

def test_securitytest::targetofevaluation_has_ip():
    assert hasattr(securityTest::TargetOfEvaluation, "ip")
    descriptor = None
    for klass in securityTest::TargetOfEvaluation.__mro__:
        if "ip" in klass.__dict__:
            descriptor = klass.__dict__["ip"]
            break
    assert isinstance(descriptor, property)



def test_securitytest::input_is_not_abstract():
    assert not inspect.isabstract(securityTest::Input)


def test_securitytest::input_constructor_exists():
    assert callable(securityTest::Input.__init__)


def test_securitytest::input_constructor_args():
    sig = inspect.signature(securityTest::Input.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_securitytest::input_has_name():
    assert hasattr(securityTest::Input, "name")
    descriptor = None
    for klass in securityTest::Input.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_securitytest::test_is_not_abstract():
    assert not inspect.isabstract(securityTest::Test)


def test_securitytest::test_constructor_exists():
    assert callable(securityTest::Test.__init__)


def test_securitytest::test_constructor_args():
    sig = inspect.signature(securityTest::Test.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"
    assert "name" in params, "Missing parameter 'name'"
    assert "severity" in params, "Missing parameter 'severity'"
    assert "id" in params, "Missing parameter 'id'"

def test_securitytest::test_has_date():
    assert hasattr(securityTest::Test, "date")
    descriptor = None
    for klass in securityTest::Test.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_securitytest::test_has_name():
    assert hasattr(securityTest::Test, "name")
    descriptor = None
    for klass in securityTest::Test.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_securitytest::test_has_severity():
    assert hasattr(securityTest::Test, "severity")
    descriptor = None
    for klass in securityTest::Test.__mro__:
        if "severity" in klass.__dict__:
            descriptor = klass.__dict__["severity"]
            break
    assert isinstance(descriptor, property)

def test_securitytest::test_has_id():
    assert hasattr(securityTest::Test, "id")
    descriptor = None
    for klass in securityTest::Test.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_eseverity_exists():
    # Check that the Enumeration exists
    assert ESeverity is not None

def test_eseverity_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ESeverity]
    expected_literals = [
        "High",
        "Low",
        "Medium",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ESeverity"

def test_eattackmethod_exists():
    # Check that the Enumeration exists
    assert EAttackMethod is not None

def test_eattackmethod_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EAttackMethod]
    expected_literals = [
        "Authentication",
        "PrivilegeScalation",
        "XSS",
        "SQLInjection",
        "Authorization",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EAttackMethod"


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
securityTest::WebComponent_strategy = st.builds(
    securityTest::WebComponent,
    path=
        safe_text
)
securityTest::AuthSetting_strategy = st.builds(
    securityTest::AuthSetting,
    loginTargetURL=
        safe_text,
    usernameParam=
        safe_text,
    passwordParam=
        safe_text,
    roles=
        safe_text,
    loginMessagePattern=
        safe_text,
    logoutMessagePattern=
        safe_text
)
securityTest::Note_strategy = st.builds(
    securityTest::Note,
    noteText=
        safe_text
)
securityTest::Attack_strategy = st.builds(
    securityTest::Attack,
    name=
        safe_text,
    severity=
        safe_text
)
securityTest::TargetOfEvaluation_strategy = st.builds(
    securityTest::TargetOfEvaluation,
    port=
        safe_text,
    protocol=
        safe_text,
    domain=
        safe_text,
    ip=
        safe_text
)
securityTest::Input_strategy = st.builds(
    securityTest::Input,
    name=
        safe_text
)
securityTest::Test_strategy = st.builds(
    securityTest::Test,
    date=
        st.dates(),
    name=
        safe_text,
    severity=
        safe_text,
    id=
        safe_text
)

@given(instance=securityTest::WebComponent_strategy)
@settings(max_examples=50)
def test_securitytest::webcomponent_instantiation(instance):
    assert isinstance(instance, securityTest::WebComponent)

@given(instance=securityTest::WebComponent_strategy)
def test_securitytest::webcomponent_path_type(instance):
    assert isinstance(instance.path, str)


@given(instance=securityTest::WebComponent_strategy)
def test_securitytest::webcomponent_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=securityTest::AuthSetting_strategy)
@settings(max_examples=50)
def test_securitytest::authsetting_instantiation(instance):
    assert isinstance(instance, securityTest::AuthSetting)

@given(instance=securityTest::AuthSetting_strategy)
def test_securitytest::authsetting_loginTargetURL_type(instance):
    assert isinstance(instance.loginTargetURL, str)


@given(instance=securityTest::AuthSetting_strategy)
def test_securitytest::authsetting_loginTargetURL_setter(instance):
    original = instance.loginTargetURL
    instance.loginTargetURL = original
    assert instance.loginTargetURL == original

@given(instance=securityTest::AuthSetting_strategy)
def test_securitytest::authsetting_usernameParam_type(instance):
    assert isinstance(instance.usernameParam, str)


@given(instance=securityTest::AuthSetting_strategy)
def test_securitytest::authsetting_usernameParam_setter(instance):
    original = instance.usernameParam
    instance.usernameParam = original
    assert instance.usernameParam == original

@given(instance=securityTest::AuthSetting_strategy)
def test_securitytest::authsetting_passwordParam_type(instance):
    assert isinstance(instance.passwordParam, str)


@given(instance=securityTest::AuthSetting_strategy)
def test_securitytest::authsetting_passwordParam_setter(instance):
    original = instance.passwordParam
    instance.passwordParam = original
    assert instance.passwordParam == original

@given(instance=securityTest::AuthSetting_strategy)
def test_securitytest::authsetting_roles_type(instance):
    assert isinstance(instance.roles, str)


@given(instance=securityTest::AuthSetting_strategy)
def test_securitytest::authsetting_roles_setter(instance):
    original = instance.roles
    instance.roles = original
    assert instance.roles == original

@given(instance=securityTest::AuthSetting_strategy)
def test_securitytest::authsetting_loginMessagePattern_type(instance):
    assert isinstance(instance.loginMessagePattern, str)


@given(instance=securityTest::AuthSetting_strategy)
def test_securitytest::authsetting_loginMessagePattern_setter(instance):
    original = instance.loginMessagePattern
    instance.loginMessagePattern = original
    assert instance.loginMessagePattern == original

@given(instance=securityTest::AuthSetting_strategy)
def test_securitytest::authsetting_logoutMessagePattern_type(instance):
    assert isinstance(instance.logoutMessagePattern, str)


@given(instance=securityTest::AuthSetting_strategy)
def test_securitytest::authsetting_logoutMessagePattern_setter(instance):
    original = instance.logoutMessagePattern
    instance.logoutMessagePattern = original
    assert instance.logoutMessagePattern == original

@given(instance=securityTest::Note_strategy)
@settings(max_examples=50)
def test_securitytest::note_instantiation(instance):
    assert isinstance(instance, securityTest::Note)

@given(instance=securityTest::Note_strategy)
def test_securitytest::note_noteText_type(instance):
    assert isinstance(instance.noteText, str)


@given(instance=securityTest::Note_strategy)
def test_securitytest::note_noteText_setter(instance):
    original = instance.noteText
    instance.noteText = original
    assert instance.noteText == original

@given(instance=securityTest::Attack_strategy)
@settings(max_examples=50)
def test_securitytest::attack_instantiation(instance):
    assert isinstance(instance, securityTest::Attack)

@given(instance=securityTest::Attack_strategy)
def test_securitytest::attack_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=securityTest::Attack_strategy)
def test_securitytest::attack_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=securityTest::Attack_strategy)
def test_securitytest::attack_severity_type(instance):
    assert isinstance(instance.severity, str)


@given(instance=securityTest::Attack_strategy)
def test_securitytest::attack_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original

@given(instance=securityTest::TargetOfEvaluation_strategy)
@settings(max_examples=50)
def test_securitytest::targetofevaluation_instantiation(instance):
    assert isinstance(instance, securityTest::TargetOfEvaluation)

@given(instance=securityTest::TargetOfEvaluation_strategy)
def test_securitytest::targetofevaluation_port_type(instance):
    assert isinstance(instance.port, str)


@given(instance=securityTest::TargetOfEvaluation_strategy)
def test_securitytest::targetofevaluation_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original

@given(instance=securityTest::TargetOfEvaluation_strategy)
def test_securitytest::targetofevaluation_protocol_type(instance):
    assert isinstance(instance.protocol, str)


@given(instance=securityTest::TargetOfEvaluation_strategy)
def test_securitytest::targetofevaluation_protocol_setter(instance):
    original = instance.protocol
    instance.protocol = original
    assert instance.protocol == original

@given(instance=securityTest::TargetOfEvaluation_strategy)
def test_securitytest::targetofevaluation_domain_type(instance):
    assert isinstance(instance.domain, str)


@given(instance=securityTest::TargetOfEvaluation_strategy)
def test_securitytest::targetofevaluation_domain_setter(instance):
    original = instance.domain
    instance.domain = original
    assert instance.domain == original

@given(instance=securityTest::TargetOfEvaluation_strategy)
def test_securitytest::targetofevaluation_ip_type(instance):
    assert isinstance(instance.ip, str)


@given(instance=securityTest::TargetOfEvaluation_strategy)
def test_securitytest::targetofevaluation_ip_setter(instance):
    original = instance.ip
    instance.ip = original
    assert instance.ip == original

@given(instance=securityTest::Input_strategy)
@settings(max_examples=50)
def test_securitytest::input_instantiation(instance):
    assert isinstance(instance, securityTest::Input)

@given(instance=securityTest::Input_strategy)
def test_securitytest::input_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=securityTest::Input_strategy)
def test_securitytest::input_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=securityTest::Test_strategy)
@settings(max_examples=50)
def test_securitytest::test_instantiation(instance):
    assert isinstance(instance, securityTest::Test)

@given(instance=securityTest::Test_strategy)
def test_securitytest::test_date_type(instance):
    assert isinstance(instance.date, date)


@given(instance=securityTest::Test_strategy)
def test_securitytest::test_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=securityTest::Test_strategy)
def test_securitytest::test_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=securityTest::Test_strategy)
def test_securitytest::test_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=securityTest::Test_strategy)
def test_securitytest::test_severity_type(instance):
    assert isinstance(instance.severity, str)


@given(instance=securityTest::Test_strategy)
def test_securitytest::test_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original

@given(instance=securityTest::Test_strategy)
def test_securitytest::test_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=securityTest::Test_strategy)
def test_securitytest::test_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
