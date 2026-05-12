import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    myDsl_BaseException,
    myDsl_RestException,
    myDsl_DataModelMethodConclusion,
    myDsl_RestExceptionList,
    myDsl_RestModelMethodConclusion,
    myDsl_Block,
    myDsl_ValidationService,
    myDsl_Transformation,
    myDsl_Service,
    myDsl_Resource,
    myDsl_RestAPI,
    myDsl_Type,
    myDsl_DomainModel,
    myDsl_Feature,
    Type,
    myDsl_ModelMapper,
    myDsl_RestModel,
    myDsl_DataModel,
    myDsl_PrimitiveType,
    myDsl_ExceptionMapper,
    myDsl_DataAccessObject,
    RestStatusCode,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl_baseexception_is_not_abstract():
    assert not inspect.isabstract(myDsl_BaseException)


def test_mydsl_baseexception_constructor_exists():
    assert callable(myDsl_BaseException.__init__)


def test_mydsl_baseexception_constructor_args():
    sig = inspect.signature(myDsl_BaseException.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"
    assert "errorCode" in params, "Missing parameter 'errorCode'"

def test_mydsl_baseexception_has_message():
    assert hasattr(myDsl_BaseException, "message")
    descriptor = None
    for klass in myDsl_BaseException.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_baseexception_has_errorCode():
    assert hasattr(myDsl_BaseException, "errorCode")
    descriptor = None
    for klass in myDsl_BaseException.__mro__:
        if "errorCode" in klass.__dict__:
            descriptor = klass.__dict__["errorCode"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_restexception_is_not_abstract():
    assert not inspect.isabstract(myDsl_RestException)


def test_mydsl_restexception_constructor_exists():
    assert callable(myDsl_RestException.__init__)


def test_mydsl_restexception_constructor_args():
    sig = inspect.signature(myDsl_RestException.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"
    assert "statusCode" in params, "Missing parameter 'statusCode'"

def test_mydsl_restexception_has_message():
    assert hasattr(myDsl_RestException, "message")
    descriptor = None
    for klass in myDsl_RestException.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_restexception_has_statusCode():
    assert hasattr(myDsl_RestException, "statusCode")
    descriptor = None
    for klass in myDsl_RestException.__mro__:
        if "statusCode" in klass.__dict__:
            descriptor = klass.__dict__["statusCode"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_datamodelmethodconclusion_is_not_abstract():
    assert not inspect.isabstract(myDsl_DataModelMethodConclusion)


def test_mydsl_datamodelmethodconclusion_constructor_exists():
    assert callable(myDsl_DataModelMethodConclusion.__init__)


def test_mydsl_datamodelmethodconclusion_constructor_args():
    sig = inspect.signature(myDsl_DataModelMethodConclusion.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_restexceptionlist_is_not_abstract():
    assert not inspect.isabstract(myDsl_RestExceptionList)


def test_mydsl_restexceptionlist_constructor_exists():
    assert callable(myDsl_RestExceptionList.__init__)


def test_mydsl_restexceptionlist_constructor_args():
    sig = inspect.signature(myDsl_RestExceptionList.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_restmodelmethodconclusion_is_not_abstract():
    assert not inspect.isabstract(myDsl_RestModelMethodConclusion)


def test_mydsl_restmodelmethodconclusion_constructor_exists():
    assert callable(myDsl_RestModelMethodConclusion.__init__)


def test_mydsl_restmodelmethodconclusion_constructor_args():
    sig = inspect.signature(myDsl_RestModelMethodConclusion.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_block_is_not_abstract():
    assert not inspect.isabstract(myDsl_Block)


def test_mydsl_block_constructor_exists():
    assert callable(myDsl_Block.__init__)


def test_mydsl_block_constructor_args():
    sig = inspect.signature(myDsl_Block.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_mydsl_block_has_code():
    assert hasattr(myDsl_Block, "code")
    descriptor = None
    for klass in myDsl_Block.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_validationservice_is_not_abstract():
    assert not inspect.isabstract(myDsl_ValidationService)


def test_mydsl_validationservice_constructor_exists():
    assert callable(myDsl_ValidationService.__init__)


def test_mydsl_validationservice_constructor_args():
    sig = inspect.signature(myDsl_ValidationService.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_transformation_is_not_abstract():
    assert not inspect.isabstract(myDsl_Transformation)


def test_mydsl_transformation_constructor_exists():
    assert callable(myDsl_Transformation.__init__)


def test_mydsl_transformation_constructor_args():
    sig = inspect.signature(myDsl_Transformation.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_service_is_not_abstract():
    assert not inspect.isabstract(myDsl_Service)


def test_mydsl_service_constructor_exists():
    assert callable(myDsl_Service.__init__)


def test_mydsl_service_constructor_args():
    sig = inspect.signature(myDsl_Service.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "findby" in params, "Missing parameter 'findby'"
    assert "deleteby" in params, "Missing parameter 'deleteby'"
    assert "updateby" in params, "Missing parameter 'updateby'"

def test_mydsl_service_has_name():
    assert hasattr(myDsl_Service, "name")
    descriptor = None
    for klass in myDsl_Service.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_service_has_findby():
    assert hasattr(myDsl_Service, "findby")
    descriptor = None
    for klass in myDsl_Service.__mro__:
        if "findby" in klass.__dict__:
            descriptor = klass.__dict__["findby"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_service_has_deleteby():
    assert hasattr(myDsl_Service, "deleteby")
    descriptor = None
    for klass in myDsl_Service.__mro__:
        if "deleteby" in klass.__dict__:
            descriptor = klass.__dict__["deleteby"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_service_has_updateby():
    assert hasattr(myDsl_Service, "updateby")
    descriptor = None
    for klass in myDsl_Service.__mro__:
        if "updateby" in klass.__dict__:
            descriptor = klass.__dict__["updateby"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_resource_is_not_abstract():
    assert not inspect.isabstract(myDsl_Resource)


def test_mydsl_resource_constructor_exists():
    assert callable(myDsl_Resource.__init__)


def test_mydsl_resource_constructor_args():
    sig = inspect.signature(myDsl_Resource.__init__)
    params = list(sig.parameters.keys())
    assert "deleteby" in params, "Missing parameter 'deleteby'"
    assert "updateby" in params, "Missing parameter 'updateby'"
    assert "name" in params, "Missing parameter 'name'"
    assert "findby" in params, "Missing parameter 'findby'"

def test_mydsl_resource_has_deleteby():
    assert hasattr(myDsl_Resource, "deleteby")
    descriptor = None
    for klass in myDsl_Resource.__mro__:
        if "deleteby" in klass.__dict__:
            descriptor = klass.__dict__["deleteby"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_resource_has_updateby():
    assert hasattr(myDsl_Resource, "updateby")
    descriptor = None
    for klass in myDsl_Resource.__mro__:
        if "updateby" in klass.__dict__:
            descriptor = klass.__dict__["updateby"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_resource_has_name():
    assert hasattr(myDsl_Resource, "name")
    descriptor = None
    for klass in myDsl_Resource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_resource_has_findby():
    assert hasattr(myDsl_Resource, "findby")
    descriptor = None
    for klass in myDsl_Resource.__mro__:
        if "findby" in klass.__dict__:
            descriptor = klass.__dict__["findby"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_restapi_is_not_abstract():
    assert not inspect.isabstract(myDsl_RestAPI)


def test_mydsl_restapi_constructor_exists():
    assert callable(myDsl_RestAPI.__init__)


def test_mydsl_restapi_constructor_args():
    sig = inspect.signature(myDsl_RestAPI.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_type_is_not_abstract():
    assert not inspect.isabstract(myDsl_Type)


def test_mydsl_type_constructor_exists():
    assert callable(myDsl_Type.__init__)


def test_mydsl_type_constructor_args():
    sig = inspect.signature(myDsl_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_type_has_name():
    assert hasattr(myDsl_Type, "name")
    descriptor = None
    for klass in myDsl_Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_domainmodel_is_not_abstract():
    assert not inspect.isabstract(myDsl_DomainModel)


def test_mydsl_domainmodel_constructor_exists():
    assert callable(myDsl_DomainModel.__init__)


def test_mydsl_domainmodel_constructor_args():
    sig = inspect.signature(myDsl_DomainModel.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_feature_is_not_abstract():
    assert not inspect.isabstract(myDsl_Feature)


def test_mydsl_feature_constructor_exists():
    assert callable(myDsl_Feature.__init__)


def test_mydsl_feature_constructor_args():
    sig = inspect.signature(myDsl_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "many" in params, "Missing parameter 'many'"

def test_mydsl_feature_has_name():
    assert hasattr(myDsl_Feature, "name")
    descriptor = None
    for klass in myDsl_Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_feature_has_many():
    assert hasattr(myDsl_Feature, "many")
    descriptor = None
    for klass in myDsl_Feature.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_modelmapper_is_not_abstract():
    assert not inspect.isabstract(myDsl_ModelMapper)


def test_mydsl_modelmapper_constructor_exists():
    assert callable(myDsl_ModelMapper.__init__)


def test_mydsl_modelmapper_constructor_args():
    sig = inspect.signature(myDsl_ModelMapper.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_restmodel_is_not_abstract():
    assert not inspect.isabstract(myDsl_RestModel)


def test_mydsl_restmodel_constructor_exists():
    assert callable(myDsl_RestModel.__init__)


def test_mydsl_restmodel_constructor_args():
    sig = inspect.signature(myDsl_RestModel.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "self" in params, "Missing parameter 'self'"

def test_mydsl_restmodel_has_id():
    assert hasattr(myDsl_RestModel, "id")
    descriptor = None
    for klass in myDsl_RestModel.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_restmodel_has_self():
    assert hasattr(myDsl_RestModel, "self")
    descriptor = None
    for klass in myDsl_RestModel.__mro__:
        if "self" in klass.__dict__:
            descriptor = klass.__dict__["self"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_datamodel_is_not_abstract():
    assert not inspect.isabstract(myDsl_DataModel)


def test_mydsl_datamodel_constructor_exists():
    assert callable(myDsl_DataModel.__init__)


def test_mydsl_datamodel_constructor_args():
    sig = inspect.signature(myDsl_DataModel.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mydsl_datamodel_has_id():
    assert hasattr(myDsl_DataModel, "id")
    descriptor = None
    for klass in myDsl_DataModel.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_primitivetype_is_not_abstract():
    assert not inspect.isabstract(myDsl_PrimitiveType)


def test_mydsl_primitivetype_constructor_exists():
    assert callable(myDsl_PrimitiveType.__init__)


def test_mydsl_primitivetype_constructor_args():
    sig = inspect.signature(myDsl_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_exceptionmapper_is_not_abstract():
    assert not inspect.isabstract(myDsl_ExceptionMapper)


def test_mydsl_exceptionmapper_constructor_exists():
    assert callable(myDsl_ExceptionMapper.__init__)


def test_mydsl_exceptionmapper_constructor_args():
    sig = inspect.signature(myDsl_ExceptionMapper.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_exceptionmapper_has_name():
    assert hasattr(myDsl_ExceptionMapper, "name")
    descriptor = None
    for klass in myDsl_ExceptionMapper.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_dataaccessobject_is_not_abstract():
    assert not inspect.isabstract(myDsl_DataAccessObject)


def test_mydsl_dataaccessobject_constructor_exists():
    assert callable(myDsl_DataAccessObject.__init__)


def test_mydsl_dataaccessobject_constructor_args():
    sig = inspect.signature(myDsl_DataAccessObject.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "updateby" in params, "Missing parameter 'updateby'"
    assert "findby" in params, "Missing parameter 'findby'"
    assert "deleteby" in params, "Missing parameter 'deleteby'"

def test_mydsl_dataaccessobject_has_name():
    assert hasattr(myDsl_DataAccessObject, "name")
    descriptor = None
    for klass in myDsl_DataAccessObject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_dataaccessobject_has_updateby():
    assert hasattr(myDsl_DataAccessObject, "updateby")
    descriptor = None
    for klass in myDsl_DataAccessObject.__mro__:
        if "updateby" in klass.__dict__:
            descriptor = klass.__dict__["updateby"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_dataaccessobject_has_findby():
    assert hasattr(myDsl_DataAccessObject, "findby")
    descriptor = None
    for klass in myDsl_DataAccessObject.__mro__:
        if "findby" in klass.__dict__:
            descriptor = klass.__dict__["findby"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_dataaccessobject_has_deleteby():
    assert hasattr(myDsl_DataAccessObject, "deleteby")
    descriptor = None
    for klass in myDsl_DataAccessObject.__mro__:
        if "deleteby" in klass.__dict__:
            descriptor = klass.__dict__["deleteby"]
            break
    assert isinstance(descriptor, property)

def test_reststatuscode_exists():
    # Check that the Enumeration exists
    assert RestStatusCode is not None

def test_reststatuscode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RestStatusCode]
    expected_literals = [
        "SUCCESS",
        "REDIRECTION",
        "INFORMATIONAL",
        "CLIENT_ERROR",
        "NETWORK_ERROR",
        "SERVER_ERROR",
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
myDsl_BaseException_strategy = st.builds(
    myDsl_BaseException,
    message=
        safe_text,
    errorCode=
        safe_text
)
myDsl_RestException_strategy = st.builds(
    myDsl_RestException,
    message=
        safe_text,
    statusCode=
        safe_text
)
myDsl_DataModelMethodConclusion_strategy = st.builds(
    myDsl_DataModelMethodConclusion,
)
myDsl_RestExceptionList_strategy = st.builds(
    myDsl_RestExceptionList,
)
myDsl_RestModelMethodConclusion_strategy = st.builds(
    myDsl_RestModelMethodConclusion,
)
myDsl_Block_strategy = st.builds(
    myDsl_Block,
    code=
        safe_text
)
myDsl_ValidationService_strategy = st.builds(
    myDsl_ValidationService,
)
myDsl_Transformation_strategy = st.builds(
    myDsl_Transformation,
)
myDsl_Service_strategy = st.builds(
    myDsl_Service,
    name=
        safe_text,
    findby=
        safe_text,
    deleteby=
        safe_text,
    updateby=
        safe_text
)
myDsl_Resource_strategy = st.builds(
    myDsl_Resource,
    deleteby=
        safe_text,
    updateby=
        safe_text,
    name=
        safe_text,
    findby=
        safe_text
)
myDsl_RestAPI_strategy = st.builds(
    myDsl_RestAPI,
)
myDsl_Type_strategy = st.builds(
    myDsl_Type,
    name=
        safe_text
)
myDsl_DomainModel_strategy = st.builds(
    myDsl_DomainModel,
)
myDsl_Feature_strategy = st.builds(
    myDsl_Feature,
    name=
        safe_text,
    many=
        st.booleans()
)
Type_strategy = st.builds(
    Type,
)
myDsl_ModelMapper_strategy = st.builds(
    myDsl_ModelMapper,
)
myDsl_RestModel_strategy = st.builds(
    myDsl_RestModel,
    id=
        safe_text,
    self=
        safe_text
)
myDsl_DataModel_strategy = st.builds(
    myDsl_DataModel,
    id=
        safe_text
)
myDsl_PrimitiveType_strategy = st.builds(
    myDsl_PrimitiveType,
)
myDsl_ExceptionMapper_strategy = st.builds(
    myDsl_ExceptionMapper,
    name=
        safe_text
)
myDsl_DataAccessObject_strategy = st.builds(
    myDsl_DataAccessObject,
    name=
        safe_text,
    updateby=
        safe_text,
    findby=
        safe_text,
    deleteby=
        safe_text
)

@given(instance=myDsl_BaseException_strategy)
@settings(max_examples=50)
def test_mydsl_baseexception_instantiation(instance):
    assert isinstance(instance, myDsl_BaseException)



@given(instance=myDsl_BaseException_strategy)
def test_mydsl_baseexception_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original



@given(instance=myDsl_BaseException_strategy)
def test_mydsl_baseexception_errorCode_setter(instance):
    original = instance.errorCode
    instance.errorCode = original
    assert instance.errorCode == original

@given(instance=myDsl_RestException_strategy)
@settings(max_examples=50)
def test_mydsl_restexception_instantiation(instance):
    assert isinstance(instance, myDsl_RestException)



@given(instance=myDsl_RestException_strategy)
def test_mydsl_restexception_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original



@given(instance=myDsl_RestException_strategy)
def test_mydsl_restexception_statusCode_setter(instance):
    original = instance.statusCode
    instance.statusCode = original
    assert instance.statusCode == original

@given(instance=myDsl_DataModelMethodConclusion_strategy)
@settings(max_examples=50)
def test_mydsl_datamodelmethodconclusion_instantiation(instance):
    assert isinstance(instance, myDsl_DataModelMethodConclusion)

@given(instance=myDsl_RestExceptionList_strategy)
@settings(max_examples=50)
def test_mydsl_restexceptionlist_instantiation(instance):
    assert isinstance(instance, myDsl_RestExceptionList)

@given(instance=myDsl_RestModelMethodConclusion_strategy)
@settings(max_examples=50)
def test_mydsl_restmodelmethodconclusion_instantiation(instance):
    assert isinstance(instance, myDsl_RestModelMethodConclusion)

@given(instance=myDsl_Block_strategy)
@settings(max_examples=50)
def test_mydsl_block_instantiation(instance):
    assert isinstance(instance, myDsl_Block)



@given(instance=myDsl_Block_strategy)
def test_mydsl_block_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=myDsl_ValidationService_strategy)
@settings(max_examples=50)
def test_mydsl_validationservice_instantiation(instance):
    assert isinstance(instance, myDsl_ValidationService)

@given(instance=myDsl_Transformation_strategy)
@settings(max_examples=50)
def test_mydsl_transformation_instantiation(instance):
    assert isinstance(instance, myDsl_Transformation)

@given(instance=myDsl_Service_strategy)
@settings(max_examples=50)
def test_mydsl_service_instantiation(instance):
    assert isinstance(instance, myDsl_Service)



@given(instance=myDsl_Service_strategy)
def test_mydsl_service_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=myDsl_Service_strategy)
def test_mydsl_service_findby_setter(instance):
    original = instance.findby
    instance.findby = original
    assert instance.findby == original



@given(instance=myDsl_Service_strategy)
def test_mydsl_service_deleteby_setter(instance):
    original = instance.deleteby
    instance.deleteby = original
    assert instance.deleteby == original



@given(instance=myDsl_Service_strategy)
def test_mydsl_service_updateby_setter(instance):
    original = instance.updateby
    instance.updateby = original
    assert instance.updateby == original

@given(instance=myDsl_Resource_strategy)
@settings(max_examples=50)
def test_mydsl_resource_instantiation(instance):
    assert isinstance(instance, myDsl_Resource)



@given(instance=myDsl_Resource_strategy)
def test_mydsl_resource_deleteby_setter(instance):
    original = instance.deleteby
    instance.deleteby = original
    assert instance.deleteby == original



@given(instance=myDsl_Resource_strategy)
def test_mydsl_resource_updateby_setter(instance):
    original = instance.updateby
    instance.updateby = original
    assert instance.updateby == original



@given(instance=myDsl_Resource_strategy)
def test_mydsl_resource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=myDsl_Resource_strategy)
def test_mydsl_resource_findby_setter(instance):
    original = instance.findby
    instance.findby = original
    assert instance.findby == original

@given(instance=myDsl_RestAPI_strategy)
@settings(max_examples=50)
def test_mydsl_restapi_instantiation(instance):
    assert isinstance(instance, myDsl_RestAPI)

@given(instance=myDsl_Type_strategy)
@settings(max_examples=50)
def test_mydsl_type_instantiation(instance):
    assert isinstance(instance, myDsl_Type)



@given(instance=myDsl_Type_strategy)
def test_mydsl_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_DomainModel_strategy)
@settings(max_examples=50)
def test_mydsl_domainmodel_instantiation(instance):
    assert isinstance(instance, myDsl_DomainModel)

@given(instance=myDsl_Feature_strategy)
@settings(max_examples=50)
def test_mydsl_feature_instantiation(instance):
    assert isinstance(instance, myDsl_Feature)



@given(instance=myDsl_Feature_strategy)
def test_mydsl_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=myDsl_Feature_strategy)
def test_mydsl_feature_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=myDsl_ModelMapper_strategy)
@settings(max_examples=50)
def test_mydsl_modelmapper_instantiation(instance):
    assert isinstance(instance, myDsl_ModelMapper)

@given(instance=myDsl_RestModel_strategy)
@settings(max_examples=50)
def test_mydsl_restmodel_instantiation(instance):
    assert isinstance(instance, myDsl_RestModel)



@given(instance=myDsl_RestModel_strategy)
def test_mydsl_restmodel_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=myDsl_RestModel_strategy)
def test_mydsl_restmodel_self_setter(instance):
    original = instance.self
    instance.self = original
    assert instance.self == original

@given(instance=myDsl_DataModel_strategy)
@settings(max_examples=50)
def test_mydsl_datamodel_instantiation(instance):
    assert isinstance(instance, myDsl_DataModel)



@given(instance=myDsl_DataModel_strategy)
def test_mydsl_datamodel_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=myDsl_PrimitiveType_strategy)
@settings(max_examples=50)
def test_mydsl_primitivetype_instantiation(instance):
    assert isinstance(instance, myDsl_PrimitiveType)

@given(instance=myDsl_ExceptionMapper_strategy)
@settings(max_examples=50)
def test_mydsl_exceptionmapper_instantiation(instance):
    assert isinstance(instance, myDsl_ExceptionMapper)



@given(instance=myDsl_ExceptionMapper_strategy)
def test_mydsl_exceptionmapper_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_DataAccessObject_strategy)
@settings(max_examples=50)
def test_mydsl_dataaccessobject_instantiation(instance):
    assert isinstance(instance, myDsl_DataAccessObject)



@given(instance=myDsl_DataAccessObject_strategy)
def test_mydsl_dataaccessobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=myDsl_DataAccessObject_strategy)
def test_mydsl_dataaccessobject_updateby_setter(instance):
    original = instance.updateby
    instance.updateby = original
    assert instance.updateby == original



@given(instance=myDsl_DataAccessObject_strategy)
def test_mydsl_dataaccessobject_findby_setter(instance):
    original = instance.findby
    instance.findby = original
    assert instance.findby == original



@given(instance=myDsl_DataAccessObject_strategy)
def test_mydsl_dataaccessobject_deleteby_setter(instance):
    original = instance.deleteby
    instance.deleteby = original
    assert instance.deleteby == original
