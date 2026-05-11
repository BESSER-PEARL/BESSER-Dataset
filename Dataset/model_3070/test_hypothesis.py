import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    myDsl::BaseException,
    myDsl::RestException,
    myDsl::DataModelMethodConclusion,
    myDsl::RestExceptionList,
    myDsl::RestModelMethodConclusion,
    myDsl::Block,
    myDsl::ValidationService,
    myDsl::Transformation,
    myDsl::Service,
    myDsl::Resource,
    myDsl::RestAPI,
    myDsl::Type,
    myDsl::DomainModel,
    myDsl::Feature,
    Type,
    myDsl::DataModel,
    myDsl::ModelMapper,
    myDsl::RestModel,
    myDsl::PrimitiveType,
    myDsl::ExceptionMapper,
    myDsl::DataAccessObject,
    RestStatusCode,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl::baseexception_is_not_abstract():
    assert not inspect.isabstract(myDsl::BaseException)


def test_mydsl::baseexception_constructor_exists():
    assert callable(myDsl::BaseException.__init__)


def test_mydsl::baseexception_constructor_args():
    sig = inspect.signature(myDsl::BaseException.__init__)
    params = list(sig.parameters.keys())
    assert "errorCode" in params, "Missing parameter 'errorCode'"
    assert "message" in params, "Missing parameter 'message'"

def test_mydsl::baseexception_has_errorCode():
    assert hasattr(myDsl::BaseException, "errorCode")
    descriptor = None
    for klass in myDsl::BaseException.__mro__:
        if "errorCode" in klass.__dict__:
            descriptor = klass.__dict__["errorCode"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::baseexception_has_message():
    assert hasattr(myDsl::BaseException, "message")
    descriptor = None
    for klass in myDsl::BaseException.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::restexception_is_not_abstract():
    assert not inspect.isabstract(myDsl::RestException)


def test_mydsl::restexception_constructor_exists():
    assert callable(myDsl::RestException.__init__)


def test_mydsl::restexception_constructor_args():
    sig = inspect.signature(myDsl::RestException.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"
    assert "statusCode" in params, "Missing parameter 'statusCode'"

def test_mydsl::restexception_has_message():
    assert hasattr(myDsl::RestException, "message")
    descriptor = None
    for klass in myDsl::RestException.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::restexception_has_statusCode():
    assert hasattr(myDsl::RestException, "statusCode")
    descriptor = None
    for klass in myDsl::RestException.__mro__:
        if "statusCode" in klass.__dict__:
            descriptor = klass.__dict__["statusCode"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::datamodelmethodconclusion_is_not_abstract():
    assert not inspect.isabstract(myDsl::DataModelMethodConclusion)


def test_mydsl::datamodelmethodconclusion_constructor_exists():
    assert callable(myDsl::DataModelMethodConclusion.__init__)


def test_mydsl::datamodelmethodconclusion_constructor_args():
    sig = inspect.signature(myDsl::DataModelMethodConclusion.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::restexceptionlist_is_not_abstract():
    assert not inspect.isabstract(myDsl::RestExceptionList)


def test_mydsl::restexceptionlist_constructor_exists():
    assert callable(myDsl::RestExceptionList.__init__)


def test_mydsl::restexceptionlist_constructor_args():
    sig = inspect.signature(myDsl::RestExceptionList.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::restmodelmethodconclusion_is_not_abstract():
    assert not inspect.isabstract(myDsl::RestModelMethodConclusion)


def test_mydsl::restmodelmethodconclusion_constructor_exists():
    assert callable(myDsl::RestModelMethodConclusion.__init__)


def test_mydsl::restmodelmethodconclusion_constructor_args():
    sig = inspect.signature(myDsl::RestModelMethodConclusion.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::block_is_not_abstract():
    assert not inspect.isabstract(myDsl::Block)


def test_mydsl::block_constructor_exists():
    assert callable(myDsl::Block.__init__)


def test_mydsl::block_constructor_args():
    sig = inspect.signature(myDsl::Block.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_mydsl::block_has_code():
    assert hasattr(myDsl::Block, "code")
    descriptor = None
    for klass in myDsl::Block.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::validationservice_is_not_abstract():
    assert not inspect.isabstract(myDsl::ValidationService)


def test_mydsl::validationservice_constructor_exists():
    assert callable(myDsl::ValidationService.__init__)


def test_mydsl::validationservice_constructor_args():
    sig = inspect.signature(myDsl::ValidationService.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::transformation_is_not_abstract():
    assert not inspect.isabstract(myDsl::Transformation)


def test_mydsl::transformation_constructor_exists():
    assert callable(myDsl::Transformation.__init__)


def test_mydsl::transformation_constructor_args():
    sig = inspect.signature(myDsl::Transformation.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::service_is_not_abstract():
    assert not inspect.isabstract(myDsl::Service)


def test_mydsl::service_constructor_exists():
    assert callable(myDsl::Service.__init__)


def test_mydsl::service_constructor_args():
    sig = inspect.signature(myDsl::Service.__init__)
    params = list(sig.parameters.keys())
    assert "updateby" in params, "Missing parameter 'updateby'"
    assert "name" in params, "Missing parameter 'name'"
    assert "deleteby" in params, "Missing parameter 'deleteby'"
    assert "findby" in params, "Missing parameter 'findby'"

def test_mydsl::service_has_updateby():
    assert hasattr(myDsl::Service, "updateby")
    descriptor = None
    for klass in myDsl::Service.__mro__:
        if "updateby" in klass.__dict__:
            descriptor = klass.__dict__["updateby"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::service_has_name():
    assert hasattr(myDsl::Service, "name")
    descriptor = None
    for klass in myDsl::Service.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::service_has_deleteby():
    assert hasattr(myDsl::Service, "deleteby")
    descriptor = None
    for klass in myDsl::Service.__mro__:
        if "deleteby" in klass.__dict__:
            descriptor = klass.__dict__["deleteby"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::service_has_findby():
    assert hasattr(myDsl::Service, "findby")
    descriptor = None
    for klass in myDsl::Service.__mro__:
        if "findby" in klass.__dict__:
            descriptor = klass.__dict__["findby"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::resource_is_not_abstract():
    assert not inspect.isabstract(myDsl::Resource)


def test_mydsl::resource_constructor_exists():
    assert callable(myDsl::Resource.__init__)


def test_mydsl::resource_constructor_args():
    sig = inspect.signature(myDsl::Resource.__init__)
    params = list(sig.parameters.keys())
    assert "updateby" in params, "Missing parameter 'updateby'"
    assert "findby" in params, "Missing parameter 'findby'"
    assert "name" in params, "Missing parameter 'name'"
    assert "deleteby" in params, "Missing parameter 'deleteby'"

def test_mydsl::resource_has_updateby():
    assert hasattr(myDsl::Resource, "updateby")
    descriptor = None
    for klass in myDsl::Resource.__mro__:
        if "updateby" in klass.__dict__:
            descriptor = klass.__dict__["updateby"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::resource_has_findby():
    assert hasattr(myDsl::Resource, "findby")
    descriptor = None
    for klass in myDsl::Resource.__mro__:
        if "findby" in klass.__dict__:
            descriptor = klass.__dict__["findby"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::resource_has_name():
    assert hasattr(myDsl::Resource, "name")
    descriptor = None
    for klass in myDsl::Resource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::resource_has_deleteby():
    assert hasattr(myDsl::Resource, "deleteby")
    descriptor = None
    for klass in myDsl::Resource.__mro__:
        if "deleteby" in klass.__dict__:
            descriptor = klass.__dict__["deleteby"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::restapi_is_not_abstract():
    assert not inspect.isabstract(myDsl::RestAPI)


def test_mydsl::restapi_constructor_exists():
    assert callable(myDsl::RestAPI.__init__)


def test_mydsl::restapi_constructor_args():
    sig = inspect.signature(myDsl::RestAPI.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::type_is_not_abstract():
    assert not inspect.isabstract(myDsl::Type)


def test_mydsl::type_constructor_exists():
    assert callable(myDsl::Type.__init__)


def test_mydsl::type_constructor_args():
    sig = inspect.signature(myDsl::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::type_has_name():
    assert hasattr(myDsl::Type, "name")
    descriptor = None
    for klass in myDsl::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::domainmodel_is_not_abstract():
    assert not inspect.isabstract(myDsl::DomainModel)


def test_mydsl::domainmodel_constructor_exists():
    assert callable(myDsl::DomainModel.__init__)


def test_mydsl::domainmodel_constructor_args():
    sig = inspect.signature(myDsl::DomainModel.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::feature_is_not_abstract():
    assert not inspect.isabstract(myDsl::Feature)


def test_mydsl::feature_constructor_exists():
    assert callable(myDsl::Feature.__init__)


def test_mydsl::feature_constructor_args():
    sig = inspect.signature(myDsl::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::feature_has_many():
    assert hasattr(myDsl::Feature, "many")
    descriptor = None
    for klass in myDsl::Feature.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::feature_has_name():
    assert hasattr(myDsl::Feature, "name")
    descriptor = None
    for klass in myDsl::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::datamodel_is_not_abstract():
    assert not inspect.isabstract(myDsl::DataModel)


def test_mydsl::datamodel_constructor_exists():
    assert callable(myDsl::DataModel.__init__)


def test_mydsl::datamodel_constructor_args():
    sig = inspect.signature(myDsl::DataModel.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mydsl::datamodel_has_id():
    assert hasattr(myDsl::DataModel, "id")
    descriptor = None
    for klass in myDsl::DataModel.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::modelmapper_is_not_abstract():
    assert not inspect.isabstract(myDsl::ModelMapper)


def test_mydsl::modelmapper_constructor_exists():
    assert callable(myDsl::ModelMapper.__init__)


def test_mydsl::modelmapper_constructor_args():
    sig = inspect.signature(myDsl::ModelMapper.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::restmodel_is_not_abstract():
    assert not inspect.isabstract(myDsl::RestModel)


def test_mydsl::restmodel_constructor_exists():
    assert callable(myDsl::RestModel.__init__)


def test_mydsl::restmodel_constructor_args():
    sig = inspect.signature(myDsl::RestModel.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "self" in params, "Missing parameter 'self'"

def test_mydsl::restmodel_has_id():
    assert hasattr(myDsl::RestModel, "id")
    descriptor = None
    for klass in myDsl::RestModel.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::restmodel_has_self():
    assert hasattr(myDsl::RestModel, "self")
    descriptor = None
    for klass in myDsl::RestModel.__mro__:
        if "self" in klass.__dict__:
            descriptor = klass.__dict__["self"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::primitivetype_is_not_abstract():
    assert not inspect.isabstract(myDsl::PrimitiveType)


def test_mydsl::primitivetype_constructor_exists():
    assert callable(myDsl::PrimitiveType.__init__)


def test_mydsl::primitivetype_constructor_args():
    sig = inspect.signature(myDsl::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::exceptionmapper_is_not_abstract():
    assert not inspect.isabstract(myDsl::ExceptionMapper)


def test_mydsl::exceptionmapper_constructor_exists():
    assert callable(myDsl::ExceptionMapper.__init__)


def test_mydsl::exceptionmapper_constructor_args():
    sig = inspect.signature(myDsl::ExceptionMapper.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::exceptionmapper_has_name():
    assert hasattr(myDsl::ExceptionMapper, "name")
    descriptor = None
    for klass in myDsl::ExceptionMapper.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::dataaccessobject_is_not_abstract():
    assert not inspect.isabstract(myDsl::DataAccessObject)


def test_mydsl::dataaccessobject_constructor_exists():
    assert callable(myDsl::DataAccessObject.__init__)


def test_mydsl::dataaccessobject_constructor_args():
    sig = inspect.signature(myDsl::DataAccessObject.__init__)
    params = list(sig.parameters.keys())
    assert "updateby" in params, "Missing parameter 'updateby'"
    assert "deleteby" in params, "Missing parameter 'deleteby'"
    assert "name" in params, "Missing parameter 'name'"
    assert "findby" in params, "Missing parameter 'findby'"

def test_mydsl::dataaccessobject_has_updateby():
    assert hasattr(myDsl::DataAccessObject, "updateby")
    descriptor = None
    for klass in myDsl::DataAccessObject.__mro__:
        if "updateby" in klass.__dict__:
            descriptor = klass.__dict__["updateby"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::dataaccessobject_has_deleteby():
    assert hasattr(myDsl::DataAccessObject, "deleteby")
    descriptor = None
    for klass in myDsl::DataAccessObject.__mro__:
        if "deleteby" in klass.__dict__:
            descriptor = klass.__dict__["deleteby"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::dataaccessobject_has_name():
    assert hasattr(myDsl::DataAccessObject, "name")
    descriptor = None
    for klass in myDsl::DataAccessObject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::dataaccessobject_has_findby():
    assert hasattr(myDsl::DataAccessObject, "findby")
    descriptor = None
    for klass in myDsl::DataAccessObject.__mro__:
        if "findby" in klass.__dict__:
            descriptor = klass.__dict__["findby"]
            break
    assert isinstance(descriptor, property)

def test_reststatuscode_exists():
    # Check that the Enumeration exists
    assert RestStatusCode is not None

def test_reststatuscode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RestStatusCode]
    expected_literals = [
        "CLIENT_ERROR",
        "INFORMATIONAL",
        "SUCCESS",
        "SERVER_ERROR",
        "REDIRECTION",
        "NETWORK_ERROR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RestStatusCode"


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
myDsl::BaseException_strategy = st.builds(
    myDsl::BaseException,
    errorCode=
        safe_text,
    message=
        safe_text
)
myDsl::RestException_strategy = st.builds(
    myDsl::RestException,
    message=
        safe_text,
    statusCode=
        safe_text
)
myDsl::DataModelMethodConclusion_strategy = st.builds(
    myDsl::DataModelMethodConclusion,
)
myDsl::RestExceptionList_strategy = st.builds(
    myDsl::RestExceptionList,
)
myDsl::RestModelMethodConclusion_strategy = st.builds(
    myDsl::RestModelMethodConclusion,
)
myDsl::Block_strategy = st.builds(
    myDsl::Block,
    code=
        safe_text
)
myDsl::ValidationService_strategy = st.builds(
    myDsl::ValidationService,
)
myDsl::Transformation_strategy = st.builds(
    myDsl::Transformation,
)
myDsl::Service_strategy = st.builds(
    myDsl::Service,
    updateby=
        safe_text,
    name=
        safe_text,
    deleteby=
        safe_text,
    findby=
        safe_text
)
myDsl::Resource_strategy = st.builds(
    myDsl::Resource,
    updateby=
        safe_text,
    findby=
        safe_text,
    name=
        safe_text,
    deleteby=
        safe_text
)
myDsl::RestAPI_strategy = st.builds(
    myDsl::RestAPI,
)
myDsl::Type_strategy = st.builds(
    myDsl::Type,
    name=
        safe_text
)
myDsl::DomainModel_strategy = st.builds(
    myDsl::DomainModel,
)
myDsl::Feature_strategy = st.builds(
    myDsl::Feature,
    many=
        st.booleans(),
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
myDsl::DataModel_strategy = st.builds(
    myDsl::DataModel,
    id=
        safe_text
)
myDsl::ModelMapper_strategy = st.builds(
    myDsl::ModelMapper,
)
myDsl::RestModel_strategy = st.builds(
    myDsl::RestModel,
    id=
        safe_text,
    self=
        safe_text
)
myDsl::PrimitiveType_strategy = st.builds(
    myDsl::PrimitiveType,
)
myDsl::ExceptionMapper_strategy = st.builds(
    myDsl::ExceptionMapper,
    name=
        safe_text
)
myDsl::DataAccessObject_strategy = st.builds(
    myDsl::DataAccessObject,
    updateby=
        safe_text,
    deleteby=
        safe_text,
    name=
        safe_text,
    findby=
        safe_text
)

@given(instance=myDsl::BaseException_strategy)
@settings(max_examples=50)
def test_mydsl::baseexception_instantiation(instance):
    assert isinstance(instance, myDsl::BaseException)

@given(instance=myDsl::BaseException_strategy)
def test_mydsl::baseexception_errorCode_type(instance):
    assert isinstance(instance.errorCode, str)


@given(instance=myDsl::BaseException_strategy)
def test_mydsl::baseexception_errorCode_setter(instance):
    original = instance.errorCode
    instance.errorCode = original
    assert instance.errorCode == original

@given(instance=myDsl::BaseException_strategy)
def test_mydsl::baseexception_message_type(instance):
    assert isinstance(instance.message, str)


@given(instance=myDsl::BaseException_strategy)
def test_mydsl::baseexception_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=myDsl::RestException_strategy)
@settings(max_examples=50)
def test_mydsl::restexception_instantiation(instance):
    assert isinstance(instance, myDsl::RestException)

@given(instance=myDsl::RestException_strategy)
def test_mydsl::restexception_message_type(instance):
    assert isinstance(instance.message, str)


@given(instance=myDsl::RestException_strategy)
def test_mydsl::restexception_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=myDsl::RestException_strategy)
def test_mydsl::restexception_statusCode_type(instance):
    assert isinstance(instance.statusCode, str)


@given(instance=myDsl::RestException_strategy)
def test_mydsl::restexception_statusCode_setter(instance):
    original = instance.statusCode
    instance.statusCode = original
    assert instance.statusCode == original

@given(instance=myDsl::DataModelMethodConclusion_strategy)
@settings(max_examples=50)
def test_mydsl::datamodelmethodconclusion_instantiation(instance):
    assert isinstance(instance, myDsl::DataModelMethodConclusion)

@given(instance=myDsl::RestExceptionList_strategy)
@settings(max_examples=50)
def test_mydsl::restexceptionlist_instantiation(instance):
    assert isinstance(instance, myDsl::RestExceptionList)

@given(instance=myDsl::RestModelMethodConclusion_strategy)
@settings(max_examples=50)
def test_mydsl::restmodelmethodconclusion_instantiation(instance):
    assert isinstance(instance, myDsl::RestModelMethodConclusion)

@given(instance=myDsl::Block_strategy)
@settings(max_examples=50)
def test_mydsl::block_instantiation(instance):
    assert isinstance(instance, myDsl::Block)

@given(instance=myDsl::Block_strategy)
def test_mydsl::block_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=myDsl::Block_strategy)
def test_mydsl::block_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=myDsl::ValidationService_strategy)
@settings(max_examples=50)
def test_mydsl::validationservice_instantiation(instance):
    assert isinstance(instance, myDsl::ValidationService)

@given(instance=myDsl::Transformation_strategy)
@settings(max_examples=50)
def test_mydsl::transformation_instantiation(instance):
    assert isinstance(instance, myDsl::Transformation)

@given(instance=myDsl::Service_strategy)
@settings(max_examples=50)
def test_mydsl::service_instantiation(instance):
    assert isinstance(instance, myDsl::Service)

@given(instance=myDsl::Service_strategy)
def test_mydsl::service_updateby_type(instance):
    assert isinstance(instance.updateby, str)


@given(instance=myDsl::Service_strategy)
def test_mydsl::service_updateby_setter(instance):
    original = instance.updateby
    instance.updateby = original
    assert instance.updateby == original

@given(instance=myDsl::Service_strategy)
def test_mydsl::service_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Service_strategy)
def test_mydsl::service_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Service_strategy)
def test_mydsl::service_deleteby_type(instance):
    assert isinstance(instance.deleteby, str)


@given(instance=myDsl::Service_strategy)
def test_mydsl::service_deleteby_setter(instance):
    original = instance.deleteby
    instance.deleteby = original
    assert instance.deleteby == original

@given(instance=myDsl::Service_strategy)
def test_mydsl::service_findby_type(instance):
    assert isinstance(instance.findby, str)


@given(instance=myDsl::Service_strategy)
def test_mydsl::service_findby_setter(instance):
    original = instance.findby
    instance.findby = original
    assert instance.findby == original

@given(instance=myDsl::Resource_strategy)
@settings(max_examples=50)
def test_mydsl::resource_instantiation(instance):
    assert isinstance(instance, myDsl::Resource)

@given(instance=myDsl::Resource_strategy)
def test_mydsl::resource_updateby_type(instance):
    assert isinstance(instance.updateby, str)


@given(instance=myDsl::Resource_strategy)
def test_mydsl::resource_updateby_setter(instance):
    original = instance.updateby
    instance.updateby = original
    assert instance.updateby == original

@given(instance=myDsl::Resource_strategy)
def test_mydsl::resource_findby_type(instance):
    assert isinstance(instance.findby, str)


@given(instance=myDsl::Resource_strategy)
def test_mydsl::resource_findby_setter(instance):
    original = instance.findby
    instance.findby = original
    assert instance.findby == original

@given(instance=myDsl::Resource_strategy)
def test_mydsl::resource_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Resource_strategy)
def test_mydsl::resource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Resource_strategy)
def test_mydsl::resource_deleteby_type(instance):
    assert isinstance(instance.deleteby, str)


@given(instance=myDsl::Resource_strategy)
def test_mydsl::resource_deleteby_setter(instance):
    original = instance.deleteby
    instance.deleteby = original
    assert instance.deleteby == original

@given(instance=myDsl::RestAPI_strategy)
@settings(max_examples=50)
def test_mydsl::restapi_instantiation(instance):
    assert isinstance(instance, myDsl::RestAPI)

@given(instance=myDsl::Type_strategy)
@settings(max_examples=50)
def test_mydsl::type_instantiation(instance):
    assert isinstance(instance, myDsl::Type)

@given(instance=myDsl::Type_strategy)
def test_mydsl::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Type_strategy)
def test_mydsl::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::DomainModel_strategy)
@settings(max_examples=50)
def test_mydsl::domainmodel_instantiation(instance):
    assert isinstance(instance, myDsl::DomainModel)

@given(instance=myDsl::Feature_strategy)
@settings(max_examples=50)
def test_mydsl::feature_instantiation(instance):
    assert isinstance(instance, myDsl::Feature)

@given(instance=myDsl::Feature_strategy)
def test_mydsl::feature_many_type(instance):
    assert isinstance(instance.many, bool)


@given(instance=myDsl::Feature_strategy)
def test_mydsl::feature_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=myDsl::Feature_strategy)
def test_mydsl::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Feature_strategy)
def test_mydsl::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=myDsl::DataModel_strategy)
@settings(max_examples=50)
def test_mydsl::datamodel_instantiation(instance):
    assert isinstance(instance, myDsl::DataModel)

@given(instance=myDsl::DataModel_strategy)
def test_mydsl::datamodel_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=myDsl::DataModel_strategy)
def test_mydsl::datamodel_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=myDsl::ModelMapper_strategy)
@settings(max_examples=50)
def test_mydsl::modelmapper_instantiation(instance):
    assert isinstance(instance, myDsl::ModelMapper)

@given(instance=myDsl::RestModel_strategy)
@settings(max_examples=50)
def test_mydsl::restmodel_instantiation(instance):
    assert isinstance(instance, myDsl::RestModel)

@given(instance=myDsl::RestModel_strategy)
def test_mydsl::restmodel_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=myDsl::RestModel_strategy)
def test_mydsl::restmodel_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=myDsl::RestModel_strategy)
def test_mydsl::restmodel_self_type(instance):
    assert isinstance(instance.self, str)


@given(instance=myDsl::RestModel_strategy)
def test_mydsl::restmodel_self_setter(instance):
    original = instance.self
    instance.self = original
    assert instance.self == original

@given(instance=myDsl::PrimitiveType_strategy)
@settings(max_examples=50)
def test_mydsl::primitivetype_instantiation(instance):
    assert isinstance(instance, myDsl::PrimitiveType)

@given(instance=myDsl::ExceptionMapper_strategy)
@settings(max_examples=50)
def test_mydsl::exceptionmapper_instantiation(instance):
    assert isinstance(instance, myDsl::ExceptionMapper)

@given(instance=myDsl::ExceptionMapper_strategy)
def test_mydsl::exceptionmapper_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::ExceptionMapper_strategy)
def test_mydsl::exceptionmapper_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::DataAccessObject_strategy)
@settings(max_examples=50)
def test_mydsl::dataaccessobject_instantiation(instance):
    assert isinstance(instance, myDsl::DataAccessObject)

@given(instance=myDsl::DataAccessObject_strategy)
def test_mydsl::dataaccessobject_updateby_type(instance):
    assert isinstance(instance.updateby, str)


@given(instance=myDsl::DataAccessObject_strategy)
def test_mydsl::dataaccessobject_updateby_setter(instance):
    original = instance.updateby
    instance.updateby = original
    assert instance.updateby == original

@given(instance=myDsl::DataAccessObject_strategy)
def test_mydsl::dataaccessobject_deleteby_type(instance):
    assert isinstance(instance.deleteby, str)


@given(instance=myDsl::DataAccessObject_strategy)
def test_mydsl::dataaccessobject_deleteby_setter(instance):
    original = instance.deleteby
    instance.deleteby = original
    assert instance.deleteby == original

@given(instance=myDsl::DataAccessObject_strategy)
def test_mydsl::dataaccessobject_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::DataAccessObject_strategy)
def test_mydsl::dataaccessobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::DataAccessObject_strategy)
def test_mydsl::dataaccessobject_findby_type(instance):
    assert isinstance(instance.findby, str)


@given(instance=myDsl::DataAccessObject_strategy)
def test_mydsl::dataaccessobject_findby_setter(instance):
    original = instance.findby
    instance.findby = original
    assert instance.findby == original
