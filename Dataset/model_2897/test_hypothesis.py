import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    index_moba_MobaApplication,
    moba_index_MobaIndexEntry,
    MobaIndexEntry,
    MobaExternalModule,
    moba_MobaNFCModule,
    moba_MobaPushModule,
    moba_MobaBluetoothModule,
    MobaPropertiesAble,
    moba_MobaFriendsAble,
    moba_MobaFriend,
    moba_index_MobaIndex,
    moba_MobaEnumLiteral,
    MobaTrigger,
    moba_MobaSMSTrigger,
    moba_MobaTimerTrigger,
    moba_MobaPushTrigger,
    moba_MobaGeofenceTrigger,
    moba_MobaDeviceStartupTrigger,
    moba_MobaEmailTrigger,
    moba_MobaAppUpdateTrigger,
    moba_MobaAppInstallTrigger,
    MobaConstraint,
    moba_MobaMaxLengthConstraint,
    moba_MobaDigitsConstraint,
    moba_MobaRegexpConstraint,
    moba_MobaConstraint,
    moba_MobaConstraintable,
    MobaQueueFeature,
    moba_MobaQueueReference,
    moba_MobaMinLengthConstraint,
    moba_MobaNullConstraint,
    moba_MobaNotNullConstraint,
    moba_MobaPastConstraint,
    moba_MobaFutureConstraint,
    moba_MobaMaxConstraint,
    moba_MobaMinConstraint,
    moba_MobaMuliplicity,
    moba_MobaMultiplicityAble,
    MobaEntityFeature,
    MobaDtoFeature,
    MobaRESTAbstractAttribute,
    moba_MobaRESTDtoAttribute,
    moba_MobaRESTAttribute,
    moba_MobaRESTAbstractAttribute,
    MobaREST,
    moba_MobaRESTCrud,
    moba_MobaRESTWorkflow,
    moba_MobaRESTCustomService,
    moba_MobaRESTPayloadDefinition,
    moba_MobaEntityIndex,
    moba_MobaRESTHeader,
    MobaMultiplicityAble,
    moba_MobaEntityReference,
    moba_MobaDtoReference,
    moba_MobaDtoEmbeddable,
    moba_MobaEntityEmbeddable,
    MobaSettingsFeature,
    MobaFeature,
    moba_MobaQueueFeature,
    moba_MobaEntityFeature,
    moba_MobaDtoFeature,
    moba_MobaSettingsFeature,
    MobaData,
    moba_MobaDto,
    moba_MobaQueue,
    moba_MobaEntity,
    moba_MobaConstantValue,
    moba_MobaProperty,
    moba_MobaPropertiesAble,
    moba_MobaGeneratorFeature,
    MobaApplicationFeature,
    moba_MobaExternalModule,
    moba_MobaConstant,
    moba_MobaSettings,
    moba_MobaAuthorization,
    moba_MobaPersistenceType,
    moba_MobaServer,
    moba_MobaData,
    moba_MobaGenerator,
    moba_MobaTransportSerializationType,
    moba_MobaEnum,
    moba_MobaREST,
    moba_MobaTrigger,
    moba_MobaTemplate,
    MobaConstraintable,
    moba_MobaSettingsEntityReference,
    moba_MobaSettingsAttribute,
    moba_MobaDtoAttribute,
    moba_MobaEntityAttribute,
    moba_MobaDataType,
    moba_MobaGeneratorSlot,
    MobaGeneratorFeature,
    moba_MobaGeneratorIDFeature,
    moba_MobaGeneratorMixinFeature,
    MobaFriendsAble,
    moba_MobaFeature,
    moba_MobaApplicationFeature,
    moba_MobaModel,
    moba_MobaCache,
    MobaModelFeature,
    moba_MobaApplication,
    moba_MobaProject,
    moba_MobaModelFeature,
    MobaBlueToothModuleType,
    MobaConstantValueFunction,
    MobaNFCModuleType,
    MobaUpperBound,
    MobaLowerBound,
    MobaGeofenceEvent,
    MobaRESTMethods,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_index_moba_mobaapplication_is_not_abstract():
    assert not inspect.isabstract(index_moba_MobaApplication)


def test_index_moba_mobaapplication_constructor_exists():
    assert callable(index_moba_MobaApplication.__init__)


def test_index_moba_mobaapplication_constructor_args():
    sig = inspect.signature(index_moba_MobaApplication.__init__)
    params = list(sig.parameters.keys())



def test_moba_index_mobaindexentry_is_not_abstract():
    assert not inspect.isabstract(moba_index_MobaIndexEntry)


def test_moba_index_mobaindexentry_constructor_exists():
    assert callable(moba_index_MobaIndexEntry.__init__)


def test_moba_index_mobaindexentry_constructor_args():
    sig = inspect.signature(moba_index_MobaIndexEntry.__init__)
    params = list(sig.parameters.keys())
    assert "templateId" in params, "Missing parameter 'templateId'"
    assert "templateVersion" in params, "Missing parameter 'templateVersion'"
    assert "relativePath" in params, "Missing parameter 'relativePath'"
    assert "filename" in params, "Missing parameter 'filename'"
    assert "templateDescription" in params, "Missing parameter 'templateDescription'"
    assert "templateName" in params, "Missing parameter 'templateName'"

def test_moba_index_mobaindexentry_has_templateId():
    assert hasattr(moba_index_MobaIndexEntry, "templateId")
    descriptor = None
    for klass in moba_index_MobaIndexEntry.__mro__:
        if "templateId" in klass.__dict__:
            descriptor = klass.__dict__["templateId"]
            break
    assert isinstance(descriptor, property)

def test_moba_index_mobaindexentry_has_templateVersion():
    assert hasattr(moba_index_MobaIndexEntry, "templateVersion")
    descriptor = None
    for klass in moba_index_MobaIndexEntry.__mro__:
        if "templateVersion" in klass.__dict__:
            descriptor = klass.__dict__["templateVersion"]
            break
    assert isinstance(descriptor, property)

def test_moba_index_mobaindexentry_has_relativePath():
    assert hasattr(moba_index_MobaIndexEntry, "relativePath")
    descriptor = None
    for klass in moba_index_MobaIndexEntry.__mro__:
        if "relativePath" in klass.__dict__:
            descriptor = klass.__dict__["relativePath"]
            break
    assert isinstance(descriptor, property)

def test_moba_index_mobaindexentry_has_filename():
    assert hasattr(moba_index_MobaIndexEntry, "filename")
    descriptor = None
    for klass in moba_index_MobaIndexEntry.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)

def test_moba_index_mobaindexentry_has_templateDescription():
    assert hasattr(moba_index_MobaIndexEntry, "templateDescription")
    descriptor = None
    for klass in moba_index_MobaIndexEntry.__mro__:
        if "templateDescription" in klass.__dict__:
            descriptor = klass.__dict__["templateDescription"]
            break
    assert isinstance(descriptor, property)

def test_moba_index_mobaindexentry_has_templateName():
    assert hasattr(moba_index_MobaIndexEntry, "templateName")
    descriptor = None
    for klass in moba_index_MobaIndexEntry.__mro__:
        if "templateName" in klass.__dict__:
            descriptor = klass.__dict__["templateName"]
            break
    assert isinstance(descriptor, property)



def test_mobaindexentry_is_not_abstract():
    assert not inspect.isabstract(MobaIndexEntry)


def test_mobaindexentry_constructor_exists():
    assert callable(MobaIndexEntry.__init__)


def test_mobaindexentry_constructor_args():
    sig = inspect.signature(MobaIndexEntry.__init__)
    params = list(sig.parameters.keys())



def test_mobaexternalmodule_is_not_abstract():
    assert not inspect.isabstract(MobaExternalModule)


def test_mobaexternalmodule_constructor_exists():
    assert callable(MobaExternalModule.__init__)


def test_mobaexternalmodule_constructor_args():
    sig = inspect.signature(MobaExternalModule.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobanfcmodule_is_not_abstract():
    assert not inspect.isabstract(moba_MobaNFCModule)


def test_moba_mobanfcmodule_constructor_exists():
    assert callable(moba_MobaNFCModule.__init__)


def test_moba_mobanfcmodule_constructor_args():
    sig = inspect.signature(moba_MobaNFCModule.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_moba_mobanfcmodule_has_type():
    assert hasattr(moba_MobaNFCModule, "type")
    descriptor = None
    for klass in moba_MobaNFCModule.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobapushmodule_is_not_abstract():
    assert not inspect.isabstract(moba_MobaPushModule)


def test_moba_mobapushmodule_constructor_exists():
    assert callable(moba_MobaPushModule.__init__)


def test_moba_mobapushmodule_constructor_args():
    sig = inspect.signature(moba_MobaPushModule.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobabluetoothmodule_is_not_abstract():
    assert not inspect.isabstract(moba_MobaBluetoothModule)


def test_moba_mobabluetoothmodule_constructor_exists():
    assert callable(moba_MobaBluetoothModule.__init__)


def test_moba_mobabluetoothmodule_constructor_args():
    sig = inspect.signature(moba_MobaBluetoothModule.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_moba_mobabluetoothmodule_has_type():
    assert hasattr(moba_MobaBluetoothModule, "type")
    descriptor = None
    for klass in moba_MobaBluetoothModule.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_mobapropertiesable_is_not_abstract():
    assert not inspect.isabstract(MobaPropertiesAble)


def test_mobapropertiesable_constructor_exists():
    assert callable(MobaPropertiesAble.__init__)


def test_mobapropertiesable_constructor_args():
    sig = inspect.signature(MobaPropertiesAble.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobafriendsable_is_not_abstract():
    assert not inspect.isabstract(moba_MobaFriendsAble)


def test_moba_mobafriendsable_constructor_exists():
    assert callable(moba_MobaFriendsAble.__init__)


def test_moba_mobafriendsable_constructor_args():
    sig = inspect.signature(moba_MobaFriendsAble.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobafriend_is_not_abstract():
    assert not inspect.isabstract(moba_MobaFriend)


def test_moba_mobafriend_constructor_exists():
    assert callable(moba_MobaFriend.__init__)


def test_moba_mobafriend_constructor_args():
    sig = inspect.signature(moba_MobaFriend.__init__)
    params = list(sig.parameters.keys())
    assert "valueString" in params, "Missing parameter 'valueString'"
    assert "value" in params, "Missing parameter 'value'"

def test_moba_mobafriend_has_valueString():
    assert hasattr(moba_MobaFriend, "valueString")
    descriptor = None
    for klass in moba_MobaFriend.__mro__:
        if "valueString" in klass.__dict__:
            descriptor = klass.__dict__["valueString"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobafriend_has_value():
    assert hasattr(moba_MobaFriend, "value")
    descriptor = None
    for klass in moba_MobaFriend.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_moba_index_mobaindex_is_not_abstract():
    assert not inspect.isabstract(moba_index_MobaIndex)


def test_moba_index_mobaindex_constructor_exists():
    assert callable(moba_index_MobaIndex.__init__)


def test_moba_index_mobaindex_constructor_args():
    sig = inspect.signature(moba_index_MobaIndex.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "id" in params, "Missing parameter 'id'"
    assert "version" in params, "Missing parameter 'version'"
    assert "name" in params, "Missing parameter 'name'"

def test_moba_index_mobaindex_has_description():
    assert hasattr(moba_index_MobaIndex, "description")
    descriptor = None
    for klass in moba_index_MobaIndex.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_moba_index_mobaindex_has_id():
    assert hasattr(moba_index_MobaIndex, "id")
    descriptor = None
    for klass in moba_index_MobaIndex.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_moba_index_mobaindex_has_version():
    assert hasattr(moba_index_MobaIndex, "version")
    descriptor = None
    for klass in moba_index_MobaIndex.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_moba_index_mobaindex_has_name():
    assert hasattr(moba_index_MobaIndex, "name")
    descriptor = None
    for klass in moba_index_MobaIndex.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobaenumliteral_is_not_abstract():
    assert not inspect.isabstract(moba_MobaEnumLiteral)


def test_moba_mobaenumliteral_constructor_exists():
    assert callable(moba_MobaEnumLiteral.__init__)


def test_moba_mobaenumliteral_constructor_args():
    sig = inspect.signature(moba_MobaEnumLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "undefined" in params, "Missing parameter 'undefined'"
    assert "literal" in params, "Missing parameter 'literal'"
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"
    assert "default" in params, "Missing parameter 'default'"
    assert "hidden" in params, "Missing parameter 'hidden'"

def test_moba_mobaenumliteral_has_undefined():
    assert hasattr(moba_MobaEnumLiteral, "undefined")
    descriptor = None
    for klass in moba_MobaEnumLiteral.__mro__:
        if "undefined" in klass.__dict__:
            descriptor = klass.__dict__["undefined"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobaenumliteral_has_literal():
    assert hasattr(moba_MobaEnumLiteral, "literal")
    descriptor = None
    for klass in moba_MobaEnumLiteral.__mro__:
        if "literal" in klass.__dict__:
            descriptor = klass.__dict__["literal"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobaenumliteral_has_value():
    assert hasattr(moba_MobaEnumLiteral, "value")
    descriptor = None
    for klass in moba_MobaEnumLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobaenumliteral_has_name():
    assert hasattr(moba_MobaEnumLiteral, "name")
    descriptor = None
    for klass in moba_MobaEnumLiteral.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobaenumliteral_has_default():
    assert hasattr(moba_MobaEnumLiteral, "default")
    descriptor = None
    for klass in moba_MobaEnumLiteral.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobaenumliteral_has_hidden():
    assert hasattr(moba_MobaEnumLiteral, "hidden")
    descriptor = None
    for klass in moba_MobaEnumLiteral.__mro__:
        if "hidden" in klass.__dict__:
            descriptor = klass.__dict__["hidden"]
            break
    assert isinstance(descriptor, property)



def test_mobatrigger_is_not_abstract():
    assert not inspect.isabstract(MobaTrigger)


def test_mobatrigger_constructor_exists():
    assert callable(MobaTrigger.__init__)


def test_mobatrigger_constructor_args():
    sig = inspect.signature(MobaTrigger.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobasmstrigger_is_not_abstract():
    assert not inspect.isabstract(moba_MobaSMSTrigger)


def test_moba_mobasmstrigger_constructor_exists():
    assert callable(moba_MobaSMSTrigger.__init__)


def test_moba_mobasmstrigger_constructor_args():
    sig = inspect.signature(moba_MobaSMSTrigger.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobatimertrigger_is_not_abstract():
    assert not inspect.isabstract(moba_MobaTimerTrigger)


def test_moba_mobatimertrigger_constructor_exists():
    assert callable(moba_MobaTimerTrigger.__init__)


def test_moba_mobatimertrigger_constructor_args():
    sig = inspect.signature(moba_MobaTimerTrigger.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobapushtrigger_is_not_abstract():
    assert not inspect.isabstract(moba_MobaPushTrigger)


def test_moba_mobapushtrigger_constructor_exists():
    assert callable(moba_MobaPushTrigger.__init__)


def test_moba_mobapushtrigger_constructor_args():
    sig = inspect.signature(moba_MobaPushTrigger.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobageofencetrigger_is_not_abstract():
    assert not inspect.isabstract(moba_MobaGeofenceTrigger)


def test_moba_mobageofencetrigger_constructor_exists():
    assert callable(moba_MobaGeofenceTrigger.__init__)


def test_moba_mobageofencetrigger_constructor_args():
    sig = inspect.signature(moba_MobaGeofenceTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "eventType" in params, "Missing parameter 'eventType'"

def test_moba_mobageofencetrigger_has_eventType():
    assert hasattr(moba_MobaGeofenceTrigger, "eventType")
    descriptor = None
    for klass in moba_MobaGeofenceTrigger.__mro__:
        if "eventType" in klass.__dict__:
            descriptor = klass.__dict__["eventType"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobadevicestartuptrigger_is_not_abstract():
    assert not inspect.isabstract(moba_MobaDeviceStartupTrigger)


def test_moba_mobadevicestartuptrigger_constructor_exists():
    assert callable(moba_MobaDeviceStartupTrigger.__init__)


def test_moba_mobadevicestartuptrigger_constructor_args():
    sig = inspect.signature(moba_MobaDeviceStartupTrigger.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobaemailtrigger_is_not_abstract():
    assert not inspect.isabstract(moba_MobaEmailTrigger)


def test_moba_mobaemailtrigger_constructor_exists():
    assert callable(moba_MobaEmailTrigger.__init__)


def test_moba_mobaemailtrigger_constructor_args():
    sig = inspect.signature(moba_MobaEmailTrigger.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobaappupdatetrigger_is_not_abstract():
    assert not inspect.isabstract(moba_MobaAppUpdateTrigger)


def test_moba_mobaappupdatetrigger_constructor_exists():
    assert callable(moba_MobaAppUpdateTrigger.__init__)


def test_moba_mobaappupdatetrigger_constructor_args():
    sig = inspect.signature(moba_MobaAppUpdateTrigger.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobaappinstalltrigger_is_not_abstract():
    assert not inspect.isabstract(moba_MobaAppInstallTrigger)


def test_moba_mobaappinstalltrigger_constructor_exists():
    assert callable(moba_MobaAppInstallTrigger.__init__)


def test_moba_mobaappinstalltrigger_constructor_args():
    sig = inspect.signature(moba_MobaAppInstallTrigger.__init__)
    params = list(sig.parameters.keys())



def test_mobaconstraint_is_not_abstract():
    assert not inspect.isabstract(MobaConstraint)


def test_mobaconstraint_constructor_exists():
    assert callable(MobaConstraint.__init__)


def test_mobaconstraint_constructor_args():
    sig = inspect.signature(MobaConstraint.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobamaxlengthconstraint_is_not_abstract():
    assert not inspect.isabstract(moba_MobaMaxLengthConstraint)


def test_moba_mobamaxlengthconstraint_constructor_exists():
    assert callable(moba_MobaMaxLengthConstraint.__init__)


def test_moba_mobamaxlengthconstraint_constructor_args():
    sig = inspect.signature(moba_MobaMaxLengthConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "filterValue" in params, "Missing parameter 'filterValue'"

def test_moba_mobamaxlengthconstraint_has_filterValue():
    assert hasattr(moba_MobaMaxLengthConstraint, "filterValue")
    descriptor = None
    for klass in moba_MobaMaxLengthConstraint.__mro__:
        if "filterValue" in klass.__dict__:
            descriptor = klass.__dict__["filterValue"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobadigitsconstraint_is_not_abstract():
    assert not inspect.isabstract(moba_MobaDigitsConstraint)


def test_moba_mobadigitsconstraint_constructor_exists():
    assert callable(moba_MobaDigitsConstraint.__init__)


def test_moba_mobadigitsconstraint_constructor_args():
    sig = inspect.signature(moba_MobaDigitsConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "filterIntegerValue" in params, "Missing parameter 'filterIntegerValue'"
    assert "filterFractionValue" in params, "Missing parameter 'filterFractionValue'"

def test_moba_mobadigitsconstraint_has_filterIntegerValue():
    assert hasattr(moba_MobaDigitsConstraint, "filterIntegerValue")
    descriptor = None
    for klass in moba_MobaDigitsConstraint.__mro__:
        if "filterIntegerValue" in klass.__dict__:
            descriptor = klass.__dict__["filterIntegerValue"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobadigitsconstraint_has_filterFractionValue():
    assert hasattr(moba_MobaDigitsConstraint, "filterFractionValue")
    descriptor = None
    for klass in moba_MobaDigitsConstraint.__mro__:
        if "filterFractionValue" in klass.__dict__:
            descriptor = klass.__dict__["filterFractionValue"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobaregexpconstraint_is_not_abstract():
    assert not inspect.isabstract(moba_MobaRegexpConstraint)


def test_moba_mobaregexpconstraint_constructor_exists():
    assert callable(moba_MobaRegexpConstraint.__init__)


def test_moba_mobaregexpconstraint_constructor_args():
    sig = inspect.signature(moba_MobaRegexpConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "filterString" in params, "Missing parameter 'filterString'"

def test_moba_mobaregexpconstraint_has_filterString():
    assert hasattr(moba_MobaRegexpConstraint, "filterString")
    descriptor = None
    for klass in moba_MobaRegexpConstraint.__mro__:
        if "filterString" in klass.__dict__:
            descriptor = klass.__dict__["filterString"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobaconstraint_is_not_abstract():
    assert not inspect.isabstract(moba_MobaConstraint)


def test_moba_mobaconstraint_constructor_exists():
    assert callable(moba_MobaConstraint.__init__)


def test_moba_mobaconstraint_constructor_args():
    sig = inspect.signature(moba_MobaConstraint.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobaconstraintable_is_not_abstract():
    assert not inspect.isabstract(moba_MobaConstraintable)


def test_moba_mobaconstraintable_constructor_exists():
    assert callable(moba_MobaConstraintable.__init__)


def test_moba_mobaconstraintable_constructor_args():
    sig = inspect.signature(moba_MobaConstraintable.__init__)
    params = list(sig.parameters.keys())



def test_mobaqueuefeature_is_not_abstract():
    assert not inspect.isabstract(MobaQueueFeature)


def test_mobaqueuefeature_constructor_exists():
    assert callable(MobaQueueFeature.__init__)


def test_mobaqueuefeature_constructor_args():
    sig = inspect.signature(MobaQueueFeature.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobaqueuereference_is_not_abstract():
    assert not inspect.isabstract(moba_MobaQueueReference)


def test_moba_mobaqueuereference_constructor_exists():
    assert callable(moba_MobaQueueReference.__init__)


def test_moba_mobaqueuereference_constructor_args():
    sig = inspect.signature(moba_MobaQueueReference.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobaminlengthconstraint_is_not_abstract():
    assert not inspect.isabstract(moba_MobaMinLengthConstraint)


def test_moba_mobaminlengthconstraint_constructor_exists():
    assert callable(moba_MobaMinLengthConstraint.__init__)


def test_moba_mobaminlengthconstraint_constructor_args():
    sig = inspect.signature(moba_MobaMinLengthConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "filterValue" in params, "Missing parameter 'filterValue'"

def test_moba_mobaminlengthconstraint_has_filterValue():
    assert hasattr(moba_MobaMinLengthConstraint, "filterValue")
    descriptor = None
    for klass in moba_MobaMinLengthConstraint.__mro__:
        if "filterValue" in klass.__dict__:
            descriptor = klass.__dict__["filterValue"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobanullconstraint_is_not_abstract():
    assert not inspect.isabstract(moba_MobaNullConstraint)


def test_moba_mobanullconstraint_constructor_exists():
    assert callable(moba_MobaNullConstraint.__init__)


def test_moba_mobanullconstraint_constructor_args():
    sig = inspect.signature(moba_MobaNullConstraint.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobanotnullconstraint_is_not_abstract():
    assert not inspect.isabstract(moba_MobaNotNullConstraint)


def test_moba_mobanotnullconstraint_constructor_exists():
    assert callable(moba_MobaNotNullConstraint.__init__)


def test_moba_mobanotnullconstraint_constructor_args():
    sig = inspect.signature(moba_MobaNotNullConstraint.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobapastconstraint_is_not_abstract():
    assert not inspect.isabstract(moba_MobaPastConstraint)


def test_moba_mobapastconstraint_constructor_exists():
    assert callable(moba_MobaPastConstraint.__init__)


def test_moba_mobapastconstraint_constructor_args():
    sig = inspect.signature(moba_MobaPastConstraint.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobafutureconstraint_is_not_abstract():
    assert not inspect.isabstract(moba_MobaFutureConstraint)


def test_moba_mobafutureconstraint_constructor_exists():
    assert callable(moba_MobaFutureConstraint.__init__)


def test_moba_mobafutureconstraint_constructor_args():
    sig = inspect.signature(moba_MobaFutureConstraint.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobamaxconstraint_is_not_abstract():
    assert not inspect.isabstract(moba_MobaMaxConstraint)


def test_moba_mobamaxconstraint_constructor_exists():
    assert callable(moba_MobaMaxConstraint.__init__)


def test_moba_mobamaxconstraint_constructor_args():
    sig = inspect.signature(moba_MobaMaxConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "filterValue" in params, "Missing parameter 'filterValue'"

def test_moba_mobamaxconstraint_has_filterValue():
    assert hasattr(moba_MobaMaxConstraint, "filterValue")
    descriptor = None
    for klass in moba_MobaMaxConstraint.__mro__:
        if "filterValue" in klass.__dict__:
            descriptor = klass.__dict__["filterValue"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobaminconstraint_is_not_abstract():
    assert not inspect.isabstract(moba_MobaMinConstraint)


def test_moba_mobaminconstraint_constructor_exists():
    assert callable(moba_MobaMinConstraint.__init__)


def test_moba_mobaminconstraint_constructor_args():
    sig = inspect.signature(moba_MobaMinConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "filterValue" in params, "Missing parameter 'filterValue'"

def test_moba_mobaminconstraint_has_filterValue():
    assert hasattr(moba_MobaMinConstraint, "filterValue")
    descriptor = None
    for klass in moba_MobaMinConstraint.__mro__:
        if "filterValue" in klass.__dict__:
            descriptor = klass.__dict__["filterValue"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobamuliplicity_is_not_abstract():
    assert not inspect.isabstract(moba_MobaMuliplicity)


def test_moba_mobamuliplicity_constructor_exists():
    assert callable(moba_MobaMuliplicity.__init__)


def test_moba_mobamuliplicity_constructor_args():
    sig = inspect.signature(moba_MobaMuliplicity.__init__)
    params = list(sig.parameters.keys())
    assert "upper" in params, "Missing parameter 'upper'"
    assert "lower" in params, "Missing parameter 'lower'"

def test_moba_mobamuliplicity_has_upper():
    assert hasattr(moba_MobaMuliplicity, "upper")
    descriptor = None
    for klass in moba_MobaMuliplicity.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobamuliplicity_has_lower():
    assert hasattr(moba_MobaMuliplicity, "lower")
    descriptor = None
    for klass in moba_MobaMuliplicity.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobamultiplicityable_is_not_abstract():
    assert not inspect.isabstract(moba_MobaMultiplicityAble)


def test_moba_mobamultiplicityable_constructor_exists():
    assert callable(moba_MobaMultiplicityAble.__init__)


def test_moba_mobamultiplicityable_constructor_args():
    sig = inspect.signature(moba_MobaMultiplicityAble.__init__)
    params = list(sig.parameters.keys())



def test_mobaentityfeature_is_not_abstract():
    assert not inspect.isabstract(MobaEntityFeature)


def test_mobaentityfeature_constructor_exists():
    assert callable(MobaEntityFeature.__init__)


def test_mobaentityfeature_constructor_args():
    sig = inspect.signature(MobaEntityFeature.__init__)
    params = list(sig.parameters.keys())



def test_mobadtofeature_is_not_abstract():
    assert not inspect.isabstract(MobaDtoFeature)


def test_mobadtofeature_constructor_exists():
    assert callable(MobaDtoFeature.__init__)


def test_mobadtofeature_constructor_args():
    sig = inspect.signature(MobaDtoFeature.__init__)
    params = list(sig.parameters.keys())



def test_mobarestabstractattribute_is_not_abstract():
    assert not inspect.isabstract(MobaRESTAbstractAttribute)


def test_mobarestabstractattribute_constructor_exists():
    assert callable(MobaRESTAbstractAttribute.__init__)


def test_mobarestabstractattribute_constructor_args():
    sig = inspect.signature(MobaRESTAbstractAttribute.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobarestdtoattribute_is_not_abstract():
    assert not inspect.isabstract(moba_MobaRESTDtoAttribute)


def test_moba_mobarestdtoattribute_constructor_exists():
    assert callable(moba_MobaRESTDtoAttribute.__init__)


def test_moba_mobarestdtoattribute_constructor_args():
    sig = inspect.signature(moba_MobaRESTDtoAttribute.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobarestattribute_is_not_abstract():
    assert not inspect.isabstract(moba_MobaRESTAttribute)


def test_moba_mobarestattribute_constructor_exists():
    assert callable(moba_MobaRESTAttribute.__init__)


def test_moba_mobarestattribute_constructor_args():
    sig = inspect.signature(moba_MobaRESTAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "formatString" in params, "Missing parameter 'formatString'"
    assert "valueDouble" in params, "Missing parameter 'valueDouble'"
    assert "valueString" in params, "Missing parameter 'valueString'"
    assert "valueInt" in params, "Missing parameter 'valueInt'"
    assert "key" in params, "Missing parameter 'key'"
    assert "keyString" in params, "Missing parameter 'keyString'"
    assert "value" in params, "Missing parameter 'value'"

def test_moba_mobarestattribute_has_formatString():
    assert hasattr(moba_MobaRESTAttribute, "formatString")
    descriptor = None
    for klass in moba_MobaRESTAttribute.__mro__:
        if "formatString" in klass.__dict__:
            descriptor = klass.__dict__["formatString"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobarestattribute_has_valueDouble():
    assert hasattr(moba_MobaRESTAttribute, "valueDouble")
    descriptor = None
    for klass in moba_MobaRESTAttribute.__mro__:
        if "valueDouble" in klass.__dict__:
            descriptor = klass.__dict__["valueDouble"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobarestattribute_has_valueString():
    assert hasattr(moba_MobaRESTAttribute, "valueString")
    descriptor = None
    for klass in moba_MobaRESTAttribute.__mro__:
        if "valueString" in klass.__dict__:
            descriptor = klass.__dict__["valueString"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobarestattribute_has_valueInt():
    assert hasattr(moba_MobaRESTAttribute, "valueInt")
    descriptor = None
    for klass in moba_MobaRESTAttribute.__mro__:
        if "valueInt" in klass.__dict__:
            descriptor = klass.__dict__["valueInt"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobarestattribute_has_key():
    assert hasattr(moba_MobaRESTAttribute, "key")
    descriptor = None
    for klass in moba_MobaRESTAttribute.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobarestattribute_has_keyString():
    assert hasattr(moba_MobaRESTAttribute, "keyString")
    descriptor = None
    for klass in moba_MobaRESTAttribute.__mro__:
        if "keyString" in klass.__dict__:
            descriptor = klass.__dict__["keyString"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobarestattribute_has_value():
    assert hasattr(moba_MobaRESTAttribute, "value")
    descriptor = None
    for klass in moba_MobaRESTAttribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobarestabstractattribute_is_not_abstract():
    assert not inspect.isabstract(moba_MobaRESTAbstractAttribute)


def test_moba_mobarestabstractattribute_constructor_exists():
    assert callable(moba_MobaRESTAbstractAttribute.__init__)


def test_moba_mobarestabstractattribute_constructor_args():
    sig = inspect.signature(moba_MobaRESTAbstractAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "attachment" in params, "Missing parameter 'attachment'"
    assert "aliasString" in params, "Missing parameter 'aliasString'"
    assert "alias" in params, "Missing parameter 'alias'"

def test_moba_mobarestabstractattribute_has_attachment():
    assert hasattr(moba_MobaRESTAbstractAttribute, "attachment")
    descriptor = None
    for klass in moba_MobaRESTAbstractAttribute.__mro__:
        if "attachment" in klass.__dict__:
            descriptor = klass.__dict__["attachment"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobarestabstractattribute_has_aliasString():
    assert hasattr(moba_MobaRESTAbstractAttribute, "aliasString")
    descriptor = None
    for klass in moba_MobaRESTAbstractAttribute.__mro__:
        if "aliasString" in klass.__dict__:
            descriptor = klass.__dict__["aliasString"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobarestabstractattribute_has_alias():
    assert hasattr(moba_MobaRESTAbstractAttribute, "alias")
    descriptor = None
    for klass in moba_MobaRESTAbstractAttribute.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_mobarest_is_not_abstract():
    assert not inspect.isabstract(MobaREST)


def test_mobarest_constructor_exists():
    assert callable(MobaREST.__init__)


def test_mobarest_constructor_args():
    sig = inspect.signature(MobaREST.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobarestcrud_is_not_abstract():
    assert not inspect.isabstract(moba_MobaRESTCrud)


def test_moba_mobarestcrud_constructor_exists():
    assert callable(moba_MobaRESTCrud.__init__)


def test_moba_mobarestcrud_constructor_args():
    sig = inspect.signature(moba_MobaRESTCrud.__init__)
    params = list(sig.parameters.keys())
    assert "operations" in params, "Missing parameter 'operations'"

def test_moba_mobarestcrud_has_operations():
    assert hasattr(moba_MobaRESTCrud, "operations")
    descriptor = None
    for klass in moba_MobaRESTCrud.__mro__:
        if "operations" in klass.__dict__:
            descriptor = klass.__dict__["operations"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobarestworkflow_is_not_abstract():
    assert not inspect.isabstract(moba_MobaRESTWorkflow)


def test_moba_mobarestworkflow_constructor_exists():
    assert callable(moba_MobaRESTWorkflow.__init__)


def test_moba_mobarestworkflow_constructor_args():
    sig = inspect.signature(moba_MobaRESTWorkflow.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobarestcustomservice_is_not_abstract():
    assert not inspect.isabstract(moba_MobaRESTCustomService)


def test_moba_mobarestcustomservice_constructor_exists():
    assert callable(moba_MobaRESTCustomService.__init__)


def test_moba_mobarestcustomservice_constructor_args():
    sig = inspect.signature(moba_MobaRESTCustomService.__init__)
    params = list(sig.parameters.keys())
    assert "operation" in params, "Missing parameter 'operation'"

def test_moba_mobarestcustomservice_has_operation():
    assert hasattr(moba_MobaRESTCustomService, "operation")
    descriptor = None
    for klass in moba_MobaRESTCustomService.__mro__:
        if "operation" in klass.__dict__:
            descriptor = klass.__dict__["operation"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobarestpayloaddefinition_is_not_abstract():
    assert not inspect.isabstract(moba_MobaRESTPayloadDefinition)


def test_moba_mobarestpayloaddefinition_constructor_exists():
    assert callable(moba_MobaRESTPayloadDefinition.__init__)


def test_moba_mobarestpayloaddefinition_constructor_args():
    sig = inspect.signature(moba_MobaRESTPayloadDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "array" in params, "Missing parameter 'array'"

def test_moba_mobarestpayloaddefinition_has_array():
    assert hasattr(moba_MobaRESTPayloadDefinition, "array")
    descriptor = None
    for klass in moba_MobaRESTPayloadDefinition.__mro__:
        if "array" in klass.__dict__:
            descriptor = klass.__dict__["array"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobaentityindex_is_not_abstract():
    assert not inspect.isabstract(moba_MobaEntityIndex)


def test_moba_mobaentityindex_constructor_exists():
    assert callable(moba_MobaEntityIndex.__init__)


def test_moba_mobaentityindex_constructor_args():
    sig = inspect.signature(moba_MobaEntityIndex.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "unique" in params, "Missing parameter 'unique'"

def test_moba_mobaentityindex_has_name():
    assert hasattr(moba_MobaEntityIndex, "name")
    descriptor = None
    for klass in moba_MobaEntityIndex.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobaentityindex_has_unique():
    assert hasattr(moba_MobaEntityIndex, "unique")
    descriptor = None
    for klass in moba_MobaEntityIndex.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobarestheader_is_not_abstract():
    assert not inspect.isabstract(moba_MobaRESTHeader)


def test_moba_mobarestheader_constructor_exists():
    assert callable(moba_MobaRESTHeader.__init__)


def test_moba_mobarestheader_constructor_args():
    sig = inspect.signature(moba_MobaRESTHeader.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"
    assert "valueString" in params, "Missing parameter 'valueString'"
    assert "contentTypeHeader" in params, "Missing parameter 'contentTypeHeader'"
    assert "rawHeader" in params, "Missing parameter 'rawHeader'"
    assert "keyString" in params, "Missing parameter 'keyString'"

def test_moba_mobarestheader_has_key():
    assert hasattr(moba_MobaRESTHeader, "key")
    descriptor = None
    for klass in moba_MobaRESTHeader.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobarestheader_has_value():
    assert hasattr(moba_MobaRESTHeader, "value")
    descriptor = None
    for klass in moba_MobaRESTHeader.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobarestheader_has_valueString():
    assert hasattr(moba_MobaRESTHeader, "valueString")
    descriptor = None
    for klass in moba_MobaRESTHeader.__mro__:
        if "valueString" in klass.__dict__:
            descriptor = klass.__dict__["valueString"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobarestheader_has_contentTypeHeader():
    assert hasattr(moba_MobaRESTHeader, "contentTypeHeader")
    descriptor = None
    for klass in moba_MobaRESTHeader.__mro__:
        if "contentTypeHeader" in klass.__dict__:
            descriptor = klass.__dict__["contentTypeHeader"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobarestheader_has_rawHeader():
    assert hasattr(moba_MobaRESTHeader, "rawHeader")
    descriptor = None
    for klass in moba_MobaRESTHeader.__mro__:
        if "rawHeader" in klass.__dict__:
            descriptor = klass.__dict__["rawHeader"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobarestheader_has_keyString():
    assert hasattr(moba_MobaRESTHeader, "keyString")
    descriptor = None
    for klass in moba_MobaRESTHeader.__mro__:
        if "keyString" in klass.__dict__:
            descriptor = klass.__dict__["keyString"]
            break
    assert isinstance(descriptor, property)



def test_mobamultiplicityable_is_not_abstract():
    assert not inspect.isabstract(MobaMultiplicityAble)


def test_mobamultiplicityable_constructor_exists():
    assert callable(MobaMultiplicityAble.__init__)


def test_mobamultiplicityable_constructor_args():
    sig = inspect.signature(MobaMultiplicityAble.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobaentityreference_is_not_abstract():
    assert not inspect.isabstract(moba_MobaEntityReference)


def test_moba_mobaentityreference_constructor_exists():
    assert callable(moba_MobaEntityReference.__init__)


def test_moba_mobaentityreference_constructor_args():
    sig = inspect.signature(moba_MobaEntityReference.__init__)
    params = list(sig.parameters.keys())
    assert "cascading" in params, "Missing parameter 'cascading'"
    assert "transient" in params, "Missing parameter 'transient'"
    assert "lazy" in params, "Missing parameter 'lazy'"

def test_moba_mobaentityreference_has_cascading():
    assert hasattr(moba_MobaEntityReference, "cascading")
    descriptor = None
    for klass in moba_MobaEntityReference.__mro__:
        if "cascading" in klass.__dict__:
            descriptor = klass.__dict__["cascading"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobaentityreference_has_transient():
    assert hasattr(moba_MobaEntityReference, "transient")
    descriptor = None
    for klass in moba_MobaEntityReference.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobaentityreference_has_lazy():
    assert hasattr(moba_MobaEntityReference, "lazy")
    descriptor = None
    for klass in moba_MobaEntityReference.__mro__:
        if "lazy" in klass.__dict__:
            descriptor = klass.__dict__["lazy"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobadtoreference_is_not_abstract():
    assert not inspect.isabstract(moba_MobaDtoReference)


def test_moba_mobadtoreference_constructor_exists():
    assert callable(moba_MobaDtoReference.__init__)


def test_moba_mobadtoreference_constructor_args():
    sig = inspect.signature(moba_MobaDtoReference.__init__)
    params = list(sig.parameters.keys())
    assert "cascading" in params, "Missing parameter 'cascading'"
    assert "alias" in params, "Missing parameter 'alias'"
    assert "lazy" in params, "Missing parameter 'lazy'"
    assert "transient" in params, "Missing parameter 'transient'"

def test_moba_mobadtoreference_has_cascading():
    assert hasattr(moba_MobaDtoReference, "cascading")
    descriptor = None
    for klass in moba_MobaDtoReference.__mro__:
        if "cascading" in klass.__dict__:
            descriptor = klass.__dict__["cascading"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobadtoreference_has_alias():
    assert hasattr(moba_MobaDtoReference, "alias")
    descriptor = None
    for klass in moba_MobaDtoReference.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobadtoreference_has_lazy():
    assert hasattr(moba_MobaDtoReference, "lazy")
    descriptor = None
    for klass in moba_MobaDtoReference.__mro__:
        if "lazy" in klass.__dict__:
            descriptor = klass.__dict__["lazy"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobadtoreference_has_transient():
    assert hasattr(moba_MobaDtoReference, "transient")
    descriptor = None
    for klass in moba_MobaDtoReference.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobadtoembeddable_is_not_abstract():
    assert not inspect.isabstract(moba_MobaDtoEmbeddable)


def test_moba_mobadtoembeddable_constructor_exists():
    assert callable(moba_MobaDtoEmbeddable.__init__)


def test_moba_mobadtoembeddable_constructor_args():
    sig = inspect.signature(moba_MobaDtoEmbeddable.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"
    assert "transient" in params, "Missing parameter 'transient'"

def test_moba_mobadtoembeddable_has_alias():
    assert hasattr(moba_MobaDtoEmbeddable, "alias")
    descriptor = None
    for klass in moba_MobaDtoEmbeddable.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobadtoembeddable_has_transient():
    assert hasattr(moba_MobaDtoEmbeddable, "transient")
    descriptor = None
    for klass in moba_MobaDtoEmbeddable.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobaentityembeddable_is_not_abstract():
    assert not inspect.isabstract(moba_MobaEntityEmbeddable)


def test_moba_mobaentityembeddable_constructor_exists():
    assert callable(moba_MobaEntityEmbeddable.__init__)


def test_moba_mobaentityembeddable_constructor_args():
    sig = inspect.signature(moba_MobaEntityEmbeddable.__init__)
    params = list(sig.parameters.keys())
    assert "transient" in params, "Missing parameter 'transient'"

def test_moba_mobaentityembeddable_has_transient():
    assert hasattr(moba_MobaEntityEmbeddable, "transient")
    descriptor = None
    for klass in moba_MobaEntityEmbeddable.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)



def test_mobasettingsfeature_is_not_abstract():
    assert not inspect.isabstract(MobaSettingsFeature)


def test_mobasettingsfeature_constructor_exists():
    assert callable(MobaSettingsFeature.__init__)


def test_mobasettingsfeature_constructor_args():
    sig = inspect.signature(MobaSettingsFeature.__init__)
    params = list(sig.parameters.keys())



def test_mobafeature_is_not_abstract():
    assert not inspect.isabstract(MobaFeature)


def test_mobafeature_constructor_exists():
    assert callable(MobaFeature.__init__)


def test_mobafeature_constructor_args():
    sig = inspect.signature(MobaFeature.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobaqueuefeature_is_not_abstract():
    assert not inspect.isabstract(moba_MobaQueueFeature)


def test_moba_mobaqueuefeature_constructor_exists():
    assert callable(moba_MobaQueueFeature.__init__)


def test_moba_mobaqueuefeature_constructor_args():
    sig = inspect.signature(moba_MobaQueueFeature.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobaentityfeature_is_not_abstract():
    assert not inspect.isabstract(moba_MobaEntityFeature)


def test_moba_mobaentityfeature_constructor_exists():
    assert callable(moba_MobaEntityFeature.__init__)


def test_moba_mobaentityfeature_constructor_args():
    sig = inspect.signature(moba_MobaEntityFeature.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobadtofeature_is_not_abstract():
    assert not inspect.isabstract(moba_MobaDtoFeature)


def test_moba_mobadtofeature_constructor_exists():
    assert callable(moba_MobaDtoFeature.__init__)


def test_moba_mobadtofeature_constructor_args():
    sig = inspect.signature(moba_MobaDtoFeature.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobasettingsfeature_is_not_abstract():
    assert not inspect.isabstract(moba_MobaSettingsFeature)


def test_moba_mobasettingsfeature_constructor_exists():
    assert callable(moba_MobaSettingsFeature.__init__)


def test_moba_mobasettingsfeature_constructor_args():
    sig = inspect.signature(moba_MobaSettingsFeature.__init__)
    params = list(sig.parameters.keys())



def test_mobadata_is_not_abstract():
    assert not inspect.isabstract(MobaData)


def test_mobadata_constructor_exists():
    assert callable(MobaData.__init__)


def test_mobadata_constructor_args():
    sig = inspect.signature(MobaData.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobadto_is_not_abstract():
    assert not inspect.isabstract(moba_MobaDto)


def test_moba_mobadto_constructor_exists():
    assert callable(moba_MobaDto.__init__)


def test_moba_mobadto_constructor_args():
    sig = inspect.signature(moba_MobaDto.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_moba_mobadto_has_name():
    assert hasattr(moba_MobaDto, "name")
    descriptor = None
    for klass in moba_MobaDto.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobaqueue_is_not_abstract():
    assert not inspect.isabstract(moba_MobaQueue)


def test_moba_mobaqueue_constructor_exists():
    assert callable(moba_MobaQueue.__init__)


def test_moba_mobaqueue_constructor_args():
    sig = inspect.signature(moba_MobaQueue.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_moba_mobaqueue_has_name():
    assert hasattr(moba_MobaQueue, "name")
    descriptor = None
    for klass in moba_MobaQueue.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobaentity_is_not_abstract():
    assert not inspect.isabstract(moba_MobaEntity)


def test_moba_mobaentity_constructor_exists():
    assert callable(moba_MobaEntity.__init__)


def test_moba_mobaentity_constructor_args():
    sig = inspect.signature(moba_MobaEntity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_moba_mobaentity_has_name():
    assert hasattr(moba_MobaEntity, "name")
    descriptor = None
    for klass in moba_MobaEntity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobaconstantvalue_is_not_abstract():
    assert not inspect.isabstract(moba_MobaConstantValue)


def test_moba_mobaconstantvalue_constructor_exists():
    assert callable(moba_MobaConstantValue.__init__)


def test_moba_mobaconstantvalue_constructor_args():
    sig = inspect.signature(moba_MobaConstantValue.__init__)
    params = list(sig.parameters.keys())
    assert "valueConstFunctions" in params, "Missing parameter 'valueConstFunctions'"
    assert "valueInt" in params, "Missing parameter 'valueInt'"
    assert "valueString" in params, "Missing parameter 'valueString'"
    assert "valueDouble" in params, "Missing parameter 'valueDouble'"
    assert "valueConstToLowerCase" in params, "Missing parameter 'valueConstToLowerCase'"

def test_moba_mobaconstantvalue_has_valueConstFunctions():
    assert hasattr(moba_MobaConstantValue, "valueConstFunctions")
    descriptor = None
    for klass in moba_MobaConstantValue.__mro__:
        if "valueConstFunctions" in klass.__dict__:
            descriptor = klass.__dict__["valueConstFunctions"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobaconstantvalue_has_valueInt():
    assert hasattr(moba_MobaConstantValue, "valueInt")
    descriptor = None
    for klass in moba_MobaConstantValue.__mro__:
        if "valueInt" in klass.__dict__:
            descriptor = klass.__dict__["valueInt"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobaconstantvalue_has_valueString():
    assert hasattr(moba_MobaConstantValue, "valueString")
    descriptor = None
    for klass in moba_MobaConstantValue.__mro__:
        if "valueString" in klass.__dict__:
            descriptor = klass.__dict__["valueString"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobaconstantvalue_has_valueDouble():
    assert hasattr(moba_MobaConstantValue, "valueDouble")
    descriptor = None
    for klass in moba_MobaConstantValue.__mro__:
        if "valueDouble" in klass.__dict__:
            descriptor = klass.__dict__["valueDouble"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobaconstantvalue_has_valueConstToLowerCase():
    assert hasattr(moba_MobaConstantValue, "valueConstToLowerCase")
    descriptor = None
    for klass in moba_MobaConstantValue.__mro__:
        if "valueConstToLowerCase" in klass.__dict__:
            descriptor = klass.__dict__["valueConstToLowerCase"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobaproperty_is_not_abstract():
    assert not inspect.isabstract(moba_MobaProperty)


def test_moba_mobaproperty_constructor_exists():
    assert callable(moba_MobaProperty.__init__)


def test_moba_mobaproperty_constructor_args():
    sig = inspect.signature(moba_MobaProperty.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"
    assert "keyString" in params, "Missing parameter 'keyString'"
    assert "valueString" in params, "Missing parameter 'valueString'"

def test_moba_mobaproperty_has_key():
    assert hasattr(moba_MobaProperty, "key")
    descriptor = None
    for klass in moba_MobaProperty.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobaproperty_has_value():
    assert hasattr(moba_MobaProperty, "value")
    descriptor = None
    for klass in moba_MobaProperty.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobaproperty_has_keyString():
    assert hasattr(moba_MobaProperty, "keyString")
    descriptor = None
    for klass in moba_MobaProperty.__mro__:
        if "keyString" in klass.__dict__:
            descriptor = klass.__dict__["keyString"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobaproperty_has_valueString():
    assert hasattr(moba_MobaProperty, "valueString")
    descriptor = None
    for klass in moba_MobaProperty.__mro__:
        if "valueString" in klass.__dict__:
            descriptor = klass.__dict__["valueString"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobapropertiesable_is_not_abstract():
    assert not inspect.isabstract(moba_MobaPropertiesAble)


def test_moba_mobapropertiesable_constructor_exists():
    assert callable(moba_MobaPropertiesAble.__init__)


def test_moba_mobapropertiesable_constructor_args():
    sig = inspect.signature(moba_MobaPropertiesAble.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobageneratorfeature_is_not_abstract():
    assert not inspect.isabstract(moba_MobaGeneratorFeature)


def test_moba_mobageneratorfeature_constructor_exists():
    assert callable(moba_MobaGeneratorFeature.__init__)


def test_moba_mobageneratorfeature_constructor_args():
    sig = inspect.signature(moba_MobaGeneratorFeature.__init__)
    params = list(sig.parameters.keys())



def test_mobaapplicationfeature_is_not_abstract():
    assert not inspect.isabstract(MobaApplicationFeature)


def test_mobaapplicationfeature_constructor_exists():
    assert callable(MobaApplicationFeature.__init__)


def test_mobaapplicationfeature_constructor_args():
    sig = inspect.signature(MobaApplicationFeature.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobaexternalmodule_is_not_abstract():
    assert not inspect.isabstract(moba_MobaExternalModule)


def test_moba_mobaexternalmodule_constructor_exists():
    assert callable(moba_MobaExternalModule.__init__)


def test_moba_mobaexternalmodule_constructor_args():
    sig = inspect.signature(moba_MobaExternalModule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_moba_mobaexternalmodule_has_name():
    assert hasattr(moba_MobaExternalModule, "name")
    descriptor = None
    for klass in moba_MobaExternalModule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobaconstant_is_not_abstract():
    assert not inspect.isabstract(moba_MobaConstant)


def test_moba_mobaconstant_constructor_exists():
    assert callable(moba_MobaConstant.__init__)


def test_moba_mobaconstant_constructor_args():
    sig = inspect.signature(moba_MobaConstant.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_moba_mobaconstant_has_name():
    assert hasattr(moba_MobaConstant, "name")
    descriptor = None
    for klass in moba_MobaConstant.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobasettings_is_not_abstract():
    assert not inspect.isabstract(moba_MobaSettings)


def test_moba_mobasettings_constructor_exists():
    assert callable(moba_MobaSettings.__init__)


def test_moba_mobasettings_constructor_args():
    sig = inspect.signature(moba_MobaSettings.__init__)
    params = list(sig.parameters.keys())
    assert "active" in params, "Missing parameter 'active'"
    assert "name" in params, "Missing parameter 'name'"

def test_moba_mobasettings_has_active():
    assert hasattr(moba_MobaSettings, "active")
    descriptor = None
    for klass in moba_MobaSettings.__mro__:
        if "active" in klass.__dict__:
            descriptor = klass.__dict__["active"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobasettings_has_name():
    assert hasattr(moba_MobaSettings, "name")
    descriptor = None
    for klass in moba_MobaSettings.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobaauthorization_is_not_abstract():
    assert not inspect.isabstract(moba_MobaAuthorization)


def test_moba_mobaauthorization_constructor_exists():
    assert callable(moba_MobaAuthorization.__init__)


def test_moba_mobaauthorization_constructor_args():
    sig = inspect.signature(moba_MobaAuthorization.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_moba_mobaauthorization_has_name():
    assert hasattr(moba_MobaAuthorization, "name")
    descriptor = None
    for klass in moba_MobaAuthorization.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobapersistencetype_is_not_abstract():
    assert not inspect.isabstract(moba_MobaPersistenceType)


def test_moba_mobapersistencetype_constructor_exists():
    assert callable(moba_MobaPersistenceType.__init__)


def test_moba_mobapersistencetype_constructor_args():
    sig = inspect.signature(moba_MobaPersistenceType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_moba_mobapersistencetype_has_name():
    assert hasattr(moba_MobaPersistenceType, "name")
    descriptor = None
    for klass in moba_MobaPersistenceType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobaserver_is_not_abstract():
    assert not inspect.isabstract(moba_MobaServer)


def test_moba_mobaserver_constructor_exists():
    assert callable(moba_MobaServer.__init__)


def test_moba_mobaserver_constructor_args():
    sig = inspect.signature(moba_MobaServer.__init__)
    params = list(sig.parameters.keys())
    assert "urlString" in params, "Missing parameter 'urlString'"
    assert "name" in params, "Missing parameter 'name'"

def test_moba_mobaserver_has_urlString():
    assert hasattr(moba_MobaServer, "urlString")
    descriptor = None
    for klass in moba_MobaServer.__mro__:
        if "urlString" in klass.__dict__:
            descriptor = klass.__dict__["urlString"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobaserver_has_name():
    assert hasattr(moba_MobaServer, "name")
    descriptor = None
    for klass in moba_MobaServer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobadata_is_not_abstract():
    assert not inspect.isabstract(moba_MobaData)


def test_moba_mobadata_constructor_exists():
    assert callable(moba_MobaData.__init__)


def test_moba_mobadata_constructor_args():
    sig = inspect.signature(moba_MobaData.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobagenerator_is_not_abstract():
    assert not inspect.isabstract(moba_MobaGenerator)


def test_moba_mobagenerator_constructor_exists():
    assert callable(moba_MobaGenerator.__init__)


def test_moba_mobagenerator_constructor_args():
    sig = inspect.signature(moba_MobaGenerator.__init__)
    params = list(sig.parameters.keys())
    assert "active" in params, "Missing parameter 'active'"
    assert "name" in params, "Missing parameter 'name'"

def test_moba_mobagenerator_has_active():
    assert hasattr(moba_MobaGenerator, "active")
    descriptor = None
    for klass in moba_MobaGenerator.__mro__:
        if "active" in klass.__dict__:
            descriptor = klass.__dict__["active"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobagenerator_has_name():
    assert hasattr(moba_MobaGenerator, "name")
    descriptor = None
    for klass in moba_MobaGenerator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobatransportserializationtype_is_not_abstract():
    assert not inspect.isabstract(moba_MobaTransportSerializationType)


def test_moba_mobatransportserializationtype_constructor_exists():
    assert callable(moba_MobaTransportSerializationType.__init__)


def test_moba_mobatransportserializationtype_constructor_args():
    sig = inspect.signature(moba_MobaTransportSerializationType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_moba_mobatransportserializationtype_has_name():
    assert hasattr(moba_MobaTransportSerializationType, "name")
    descriptor = None
    for klass in moba_MobaTransportSerializationType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobaenum_is_not_abstract():
    assert not inspect.isabstract(moba_MobaEnum)


def test_moba_mobaenum_constructor_exists():
    assert callable(moba_MobaEnum.__init__)


def test_moba_mobaenum_constructor_args():
    sig = inspect.signature(moba_MobaEnum.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobarest_is_not_abstract():
    assert not inspect.isabstract(moba_MobaREST)


def test_moba_mobarest_constructor_exists():
    assert callable(moba_MobaREST.__init__)


def test_moba_mobarest_constructor_args():
    sig = inspect.signature(moba_MobaREST.__init__)
    params = list(sig.parameters.keys())
    assert "url" in params, "Missing parameter 'url'"
    assert "path" in params, "Missing parameter 'path'"
    assert "name" in params, "Missing parameter 'name'"
    assert "bigData" in params, "Missing parameter 'bigData'"

def test_moba_mobarest_has_url():
    assert hasattr(moba_MobaREST, "url")
    descriptor = None
    for klass in moba_MobaREST.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobarest_has_path():
    assert hasattr(moba_MobaREST, "path")
    descriptor = None
    for klass in moba_MobaREST.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobarest_has_name():
    assert hasattr(moba_MobaREST, "name")
    descriptor = None
    for klass in moba_MobaREST.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobarest_has_bigData():
    assert hasattr(moba_MobaREST, "bigData")
    descriptor = None
    for klass in moba_MobaREST.__mro__:
        if "bigData" in klass.__dict__:
            descriptor = klass.__dict__["bigData"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobatrigger_is_not_abstract():
    assert not inspect.isabstract(moba_MobaTrigger)


def test_moba_mobatrigger_constructor_exists():
    assert callable(moba_MobaTrigger.__init__)


def test_moba_mobatrigger_constructor_args():
    sig = inspect.signature(moba_MobaTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_moba_mobatrigger_has_name():
    assert hasattr(moba_MobaTrigger, "name")
    descriptor = None
    for klass in moba_MobaTrigger.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobatemplate_is_not_abstract():
    assert not inspect.isabstract(moba_MobaTemplate)


def test_moba_mobatemplate_constructor_exists():
    assert callable(moba_MobaTemplate.__init__)


def test_moba_mobatemplate_constructor_args():
    sig = inspect.signature(moba_MobaTemplate.__init__)
    params = list(sig.parameters.keys())
    assert "downloadTemplate" in params, "Missing parameter 'downloadTemplate'"

def test_moba_mobatemplate_has_downloadTemplate():
    assert hasattr(moba_MobaTemplate, "downloadTemplate")
    descriptor = None
    for klass in moba_MobaTemplate.__mro__:
        if "downloadTemplate" in klass.__dict__:
            descriptor = klass.__dict__["downloadTemplate"]
            break
    assert isinstance(descriptor, property)



def test_mobaconstraintable_is_not_abstract():
    assert not inspect.isabstract(MobaConstraintable)


def test_mobaconstraintable_constructor_exists():
    assert callable(MobaConstraintable.__init__)


def test_mobaconstraintable_constructor_args():
    sig = inspect.signature(MobaConstraintable.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobasettingsentityreference_is_not_abstract():
    assert not inspect.isabstract(moba_MobaSettingsEntityReference)


def test_moba_mobasettingsentityreference_constructor_exists():
    assert callable(moba_MobaSettingsEntityReference.__init__)


def test_moba_mobasettingsentityreference_constructor_args():
    sig = inspect.signature(moba_MobaSettingsEntityReference.__init__)
    params = list(sig.parameters.keys())
    assert "lazy" in params, "Missing parameter 'lazy'"
    assert "cascading" in params, "Missing parameter 'cascading'"
    assert "transient" in params, "Missing parameter 'transient'"

def test_moba_mobasettingsentityreference_has_lazy():
    assert hasattr(moba_MobaSettingsEntityReference, "lazy")
    descriptor = None
    for klass in moba_MobaSettingsEntityReference.__mro__:
        if "lazy" in klass.__dict__:
            descriptor = klass.__dict__["lazy"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobasettingsentityreference_has_cascading():
    assert hasattr(moba_MobaSettingsEntityReference, "cascading")
    descriptor = None
    for klass in moba_MobaSettingsEntityReference.__mro__:
        if "cascading" in klass.__dict__:
            descriptor = klass.__dict__["cascading"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobasettingsentityreference_has_transient():
    assert hasattr(moba_MobaSettingsEntityReference, "transient")
    descriptor = None
    for klass in moba_MobaSettingsEntityReference.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobasettingsattribute_is_not_abstract():
    assert not inspect.isabstract(moba_MobaSettingsAttribute)


def test_moba_mobasettingsattribute_constructor_exists():
    assert callable(moba_MobaSettingsAttribute.__init__)


def test_moba_mobasettingsattribute_constructor_args():
    sig = inspect.signature(moba_MobaSettingsAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "formatString" in params, "Missing parameter 'formatString'"
    assert "domainDescription" in params, "Missing parameter 'domainDescription'"
    assert "lazy" in params, "Missing parameter 'lazy'"
    assert "domainKey" in params, "Missing parameter 'domainKey'"
    assert "transient" in params, "Missing parameter 'transient'"

def test_moba_mobasettingsattribute_has_formatString():
    assert hasattr(moba_MobaSettingsAttribute, "formatString")
    descriptor = None
    for klass in moba_MobaSettingsAttribute.__mro__:
        if "formatString" in klass.__dict__:
            descriptor = klass.__dict__["formatString"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobasettingsattribute_has_domainDescription():
    assert hasattr(moba_MobaSettingsAttribute, "domainDescription")
    descriptor = None
    for klass in moba_MobaSettingsAttribute.__mro__:
        if "domainDescription" in klass.__dict__:
            descriptor = klass.__dict__["domainDescription"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobasettingsattribute_has_lazy():
    assert hasattr(moba_MobaSettingsAttribute, "lazy")
    descriptor = None
    for klass in moba_MobaSettingsAttribute.__mro__:
        if "lazy" in klass.__dict__:
            descriptor = klass.__dict__["lazy"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobasettingsattribute_has_domainKey():
    assert hasattr(moba_MobaSettingsAttribute, "domainKey")
    descriptor = None
    for klass in moba_MobaSettingsAttribute.__mro__:
        if "domainKey" in klass.__dict__:
            descriptor = klass.__dict__["domainKey"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobasettingsattribute_has_transient():
    assert hasattr(moba_MobaSettingsAttribute, "transient")
    descriptor = None
    for klass in moba_MobaSettingsAttribute.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobadtoattribute_is_not_abstract():
    assert not inspect.isabstract(moba_MobaDtoAttribute)


def test_moba_mobadtoattribute_constructor_exists():
    assert callable(moba_MobaDtoAttribute.__init__)


def test_moba_mobadtoattribute_constructor_args():
    sig = inspect.signature(moba_MobaDtoAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "lazy" in params, "Missing parameter 'lazy'"
    assert "domainDescription" in params, "Missing parameter 'domainDescription'"
    assert "transient" in params, "Missing parameter 'transient'"
    assert "domainKey" in params, "Missing parameter 'domainKey'"
    assert "alias" in params, "Missing parameter 'alias'"
    assert "formatString" in params, "Missing parameter 'formatString'"

def test_moba_mobadtoattribute_has_lazy():
    assert hasattr(moba_MobaDtoAttribute, "lazy")
    descriptor = None
    for klass in moba_MobaDtoAttribute.__mro__:
        if "lazy" in klass.__dict__:
            descriptor = klass.__dict__["lazy"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobadtoattribute_has_domainDescription():
    assert hasattr(moba_MobaDtoAttribute, "domainDescription")
    descriptor = None
    for klass in moba_MobaDtoAttribute.__mro__:
        if "domainDescription" in klass.__dict__:
            descriptor = klass.__dict__["domainDescription"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobadtoattribute_has_transient():
    assert hasattr(moba_MobaDtoAttribute, "transient")
    descriptor = None
    for klass in moba_MobaDtoAttribute.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobadtoattribute_has_domainKey():
    assert hasattr(moba_MobaDtoAttribute, "domainKey")
    descriptor = None
    for klass in moba_MobaDtoAttribute.__mro__:
        if "domainKey" in klass.__dict__:
            descriptor = klass.__dict__["domainKey"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobadtoattribute_has_alias():
    assert hasattr(moba_MobaDtoAttribute, "alias")
    descriptor = None
    for klass in moba_MobaDtoAttribute.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobadtoattribute_has_formatString():
    assert hasattr(moba_MobaDtoAttribute, "formatString")
    descriptor = None
    for klass in moba_MobaDtoAttribute.__mro__:
        if "formatString" in klass.__dict__:
            descriptor = klass.__dict__["formatString"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobaentityattribute_is_not_abstract():
    assert not inspect.isabstract(moba_MobaEntityAttribute)


def test_moba_mobaentityattribute_constructor_exists():
    assert callable(moba_MobaEntityAttribute.__init__)


def test_moba_mobaentityattribute_constructor_args():
    sig = inspect.signature(moba_MobaEntityAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "formatString" in params, "Missing parameter 'formatString'"
    assert "domainKey" in params, "Missing parameter 'domainKey'"
    assert "lazy" in params, "Missing parameter 'lazy'"
    assert "transient" in params, "Missing parameter 'transient'"
    assert "domainDescription" in params, "Missing parameter 'domainDescription'"

def test_moba_mobaentityattribute_has_formatString():
    assert hasattr(moba_MobaEntityAttribute, "formatString")
    descriptor = None
    for klass in moba_MobaEntityAttribute.__mro__:
        if "formatString" in klass.__dict__:
            descriptor = klass.__dict__["formatString"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobaentityattribute_has_domainKey():
    assert hasattr(moba_MobaEntityAttribute, "domainKey")
    descriptor = None
    for klass in moba_MobaEntityAttribute.__mro__:
        if "domainKey" in klass.__dict__:
            descriptor = klass.__dict__["domainKey"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobaentityattribute_has_lazy():
    assert hasattr(moba_MobaEntityAttribute, "lazy")
    descriptor = None
    for klass in moba_MobaEntityAttribute.__mro__:
        if "lazy" in klass.__dict__:
            descriptor = klass.__dict__["lazy"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobaentityattribute_has_transient():
    assert hasattr(moba_MobaEntityAttribute, "transient")
    descriptor = None
    for klass in moba_MobaEntityAttribute.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobaentityattribute_has_domainDescription():
    assert hasattr(moba_MobaEntityAttribute, "domainDescription")
    descriptor = None
    for klass in moba_MobaEntityAttribute.__mro__:
        if "domainDescription" in klass.__dict__:
            descriptor = klass.__dict__["domainDescription"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobadatatype_is_not_abstract():
    assert not inspect.isabstract(moba_MobaDataType)


def test_moba_mobadatatype_constructor_exists():
    assert callable(moba_MobaDataType.__init__)


def test_moba_mobadatatype_constructor_args():
    sig = inspect.signature(moba_MobaDataType.__init__)
    params = list(sig.parameters.keys())
    assert "timestamp" in params, "Missing parameter 'timestamp'"
    assert "decimal" in params, "Missing parameter 'decimal'"
    assert "time" in params, "Missing parameter 'time'"
    assert "date" in params, "Missing parameter 'date'"
    assert "dateFormatString" in params, "Missing parameter 'dateFormatString'"
    assert "array" in params, "Missing parameter 'array'"
    assert "name" in params, "Missing parameter 'name'"
    assert "primitive" in params, "Missing parameter 'primitive'"
    assert "numeric" in params, "Missing parameter 'numeric'"
    assert "predefined" in params, "Missing parameter 'predefined'"
    assert "string" in params, "Missing parameter 'string'"
    assert "bool" in params, "Missing parameter 'bool'"

def test_moba_mobadatatype_has_timestamp():
    assert hasattr(moba_MobaDataType, "timestamp")
    descriptor = None
    for klass in moba_MobaDataType.__mro__:
        if "timestamp" in klass.__dict__:
            descriptor = klass.__dict__["timestamp"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobadatatype_has_decimal():
    assert hasattr(moba_MobaDataType, "decimal")
    descriptor = None
    for klass in moba_MobaDataType.__mro__:
        if "decimal" in klass.__dict__:
            descriptor = klass.__dict__["decimal"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobadatatype_has_time():
    assert hasattr(moba_MobaDataType, "time")
    descriptor = None
    for klass in moba_MobaDataType.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobadatatype_has_date():
    assert hasattr(moba_MobaDataType, "date")
    descriptor = None
    for klass in moba_MobaDataType.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobadatatype_has_dateFormatString():
    assert hasattr(moba_MobaDataType, "dateFormatString")
    descriptor = None
    for klass in moba_MobaDataType.__mro__:
        if "dateFormatString" in klass.__dict__:
            descriptor = klass.__dict__["dateFormatString"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobadatatype_has_array():
    assert hasattr(moba_MobaDataType, "array")
    descriptor = None
    for klass in moba_MobaDataType.__mro__:
        if "array" in klass.__dict__:
            descriptor = klass.__dict__["array"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobadatatype_has_name():
    assert hasattr(moba_MobaDataType, "name")
    descriptor = None
    for klass in moba_MobaDataType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobadatatype_has_primitive():
    assert hasattr(moba_MobaDataType, "primitive")
    descriptor = None
    for klass in moba_MobaDataType.__mro__:
        if "primitive" in klass.__dict__:
            descriptor = klass.__dict__["primitive"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobadatatype_has_numeric():
    assert hasattr(moba_MobaDataType, "numeric")
    descriptor = None
    for klass in moba_MobaDataType.__mro__:
        if "numeric" in klass.__dict__:
            descriptor = klass.__dict__["numeric"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobadatatype_has_predefined():
    assert hasattr(moba_MobaDataType, "predefined")
    descriptor = None
    for klass in moba_MobaDataType.__mro__:
        if "predefined" in klass.__dict__:
            descriptor = klass.__dict__["predefined"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobadatatype_has_string():
    assert hasattr(moba_MobaDataType, "string")
    descriptor = None
    for klass in moba_MobaDataType.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobadatatype_has_bool():
    assert hasattr(moba_MobaDataType, "bool")
    descriptor = None
    for klass in moba_MobaDataType.__mro__:
        if "bool" in klass.__dict__:
            descriptor = klass.__dict__["bool"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobageneratorslot_is_not_abstract():
    assert not inspect.isabstract(moba_MobaGeneratorSlot)


def test_moba_mobageneratorslot_constructor_exists():
    assert callable(moba_MobaGeneratorSlot.__init__)


def test_moba_mobageneratorslot_constructor_args():
    sig = inspect.signature(moba_MobaGeneratorSlot.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_moba_mobageneratorslot_has_name():
    assert hasattr(moba_MobaGeneratorSlot, "name")
    descriptor = None
    for klass in moba_MobaGeneratorSlot.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobageneratorslot_has_type():
    assert hasattr(moba_MobaGeneratorSlot, "type")
    descriptor = None
    for klass in moba_MobaGeneratorSlot.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_mobageneratorfeature_is_not_abstract():
    assert not inspect.isabstract(MobaGeneratorFeature)


def test_mobageneratorfeature_constructor_exists():
    assert callable(MobaGeneratorFeature.__init__)


def test_mobageneratorfeature_constructor_args():
    sig = inspect.signature(MobaGeneratorFeature.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobageneratoridfeature_is_not_abstract():
    assert not inspect.isabstract(moba_MobaGeneratorIDFeature)


def test_moba_mobageneratoridfeature_constructor_exists():
    assert callable(moba_MobaGeneratorIDFeature.__init__)


def test_moba_mobageneratoridfeature_constructor_args():
    sig = inspect.signature(moba_MobaGeneratorIDFeature.__init__)
    params = list(sig.parameters.keys())
    assert "generatorVersion" in params, "Missing parameter 'generatorVersion'"
    assert "generatorId" in params, "Missing parameter 'generatorId'"

def test_moba_mobageneratoridfeature_has_generatorVersion():
    assert hasattr(moba_MobaGeneratorIDFeature, "generatorVersion")
    descriptor = None
    for klass in moba_MobaGeneratorIDFeature.__mro__:
        if "generatorVersion" in klass.__dict__:
            descriptor = klass.__dict__["generatorVersion"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobageneratoridfeature_has_generatorId():
    assert hasattr(moba_MobaGeneratorIDFeature, "generatorId")
    descriptor = None
    for klass in moba_MobaGeneratorIDFeature.__mro__:
        if "generatorId" in klass.__dict__:
            descriptor = klass.__dict__["generatorId"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobageneratormixinfeature_is_not_abstract():
    assert not inspect.isabstract(moba_MobaGeneratorMixinFeature)


def test_moba_mobageneratormixinfeature_constructor_exists():
    assert callable(moba_MobaGeneratorMixinFeature.__init__)


def test_moba_mobageneratormixinfeature_constructor_args():
    sig = inspect.signature(moba_MobaGeneratorMixinFeature.__init__)
    params = list(sig.parameters.keys())



def test_mobafriendsable_is_not_abstract():
    assert not inspect.isabstract(MobaFriendsAble)


def test_mobafriendsable_constructor_exists():
    assert callable(MobaFriendsAble.__init__)


def test_mobafriendsable_constructor_args():
    sig = inspect.signature(MobaFriendsAble.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobafeature_is_not_abstract():
    assert not inspect.isabstract(moba_MobaFeature)


def test_moba_mobafeature_constructor_exists():
    assert callable(moba_MobaFeature.__init__)


def test_moba_mobafeature_constructor_args():
    sig = inspect.signature(moba_MobaFeature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_moba_mobafeature_has_name():
    assert hasattr(moba_MobaFeature, "name")
    descriptor = None
    for klass in moba_MobaFeature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobaapplicationfeature_is_not_abstract():
    assert not inspect.isabstract(moba_MobaApplicationFeature)


def test_moba_mobaapplicationfeature_constructor_exists():
    assert callable(moba_MobaApplicationFeature.__init__)


def test_moba_mobaapplicationfeature_constructor_args():
    sig = inspect.signature(moba_MobaApplicationFeature.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobamodel_is_not_abstract():
    assert not inspect.isabstract(moba_MobaModel)


def test_moba_mobamodel_constructor_exists():
    assert callable(moba_MobaModel.__init__)


def test_moba_mobamodel_constructor_args():
    sig = inspect.signature(moba_MobaModel.__init__)
    params = list(sig.parameters.keys())
    assert "copyright" in params, "Missing parameter 'copyright'"

def test_moba_mobamodel_has_copyright():
    assert hasattr(moba_MobaModel, "copyright")
    descriptor = None
    for klass in moba_MobaModel.__mro__:
        if "copyright" in klass.__dict__:
            descriptor = klass.__dict__["copyright"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobacache_is_not_abstract():
    assert not inspect.isabstract(moba_MobaCache)


def test_moba_mobacache_constructor_exists():
    assert callable(moba_MobaCache.__init__)


def test_moba_mobacache_constructor_args():
    sig = inspect.signature(moba_MobaCache.__init__)
    params = list(sig.parameters.keys())
    assert "cacheIntervalInt" in params, "Missing parameter 'cacheIntervalInt'"
    assert "cacheTypeString" in params, "Missing parameter 'cacheTypeString'"
    assert "name" in params, "Missing parameter 'name'"
    assert "cacheStrategyString" in params, "Missing parameter 'cacheStrategyString'"

def test_moba_mobacache_has_cacheIntervalInt():
    assert hasattr(moba_MobaCache, "cacheIntervalInt")
    descriptor = None
    for klass in moba_MobaCache.__mro__:
        if "cacheIntervalInt" in klass.__dict__:
            descriptor = klass.__dict__["cacheIntervalInt"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobacache_has_cacheTypeString():
    assert hasattr(moba_MobaCache, "cacheTypeString")
    descriptor = None
    for klass in moba_MobaCache.__mro__:
        if "cacheTypeString" in klass.__dict__:
            descriptor = klass.__dict__["cacheTypeString"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobacache_has_name():
    assert hasattr(moba_MobaCache, "name")
    descriptor = None
    for klass in moba_MobaCache.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobacache_has_cacheStrategyString():
    assert hasattr(moba_MobaCache, "cacheStrategyString")
    descriptor = None
    for klass in moba_MobaCache.__mro__:
        if "cacheStrategyString" in klass.__dict__:
            descriptor = klass.__dict__["cacheStrategyString"]
            break
    assert isinstance(descriptor, property)



def test_mobamodelfeature_is_not_abstract():
    assert not inspect.isabstract(MobaModelFeature)


def test_mobamodelfeature_constructor_exists():
    assert callable(MobaModelFeature.__init__)


def test_mobamodelfeature_constructor_args():
    sig = inspect.signature(MobaModelFeature.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobaapplication_is_not_abstract():
    assert not inspect.isabstract(moba_MobaApplication)


def test_moba_mobaapplication_constructor_exists():
    assert callable(moba_MobaApplication.__init__)


def test_moba_mobaapplication_constructor_args():
    sig = inspect.signature(moba_MobaApplication.__init__)
    params = list(sig.parameters.keys())
    assert "javaPackage" in params, "Missing parameter 'javaPackage'"

def test_moba_mobaapplication_has_javaPackage():
    assert hasattr(moba_MobaApplication, "javaPackage")
    descriptor = None
    for klass in moba_MobaApplication.__mro__:
        if "javaPackage" in klass.__dict__:
            descriptor = klass.__dict__["javaPackage"]
            break
    assert isinstance(descriptor, property)



def test_moba_mobaproject_is_not_abstract():
    assert not inspect.isabstract(moba_MobaProject)


def test_moba_mobaproject_constructor_exists():
    assert callable(moba_MobaProject.__init__)


def test_moba_mobaproject_constructor_args():
    sig = inspect.signature(moba_MobaProject.__init__)
    params = list(sig.parameters.keys())



def test_moba_mobamodelfeature_is_not_abstract():
    assert not inspect.isabstract(moba_MobaModelFeature)


def test_moba_mobamodelfeature_constructor_exists():
    assert callable(moba_MobaModelFeature.__init__)


def test_moba_mobamodelfeature_constructor_args():
    sig = inspect.signature(moba_MobaModelFeature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "version" in params, "Missing parameter 'version'"

def test_moba_mobamodelfeature_has_name():
    assert hasattr(moba_MobaModelFeature, "name")
    descriptor = None
    for klass in moba_MobaModelFeature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobamodelfeature_has_id():
    assert hasattr(moba_MobaModelFeature, "id")
    descriptor = None
    for klass in moba_MobaModelFeature.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_moba_mobamodelfeature_has_version():
    assert hasattr(moba_MobaModelFeature, "version")
    descriptor = None
    for klass in moba_MobaModelFeature.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_mobabluetoothmoduletype_exists():
    # Check that the Enumeration exists
    assert MobaBlueToothModuleType is not None

def test_mobabluetoothmoduletype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MobaBlueToothModuleType]
    expected_literals = [
        "BEACON",
        "SPP",
        "LE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MobaBlueToothModuleType"

def test_mobaconstantvaluefunction_exists():
    # Check that the Enumeration exists
    assert MobaConstantValueFunction is not None

def test_mobaconstantvaluefunction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MobaConstantValueFunction]
    expected_literals = [
        "TO_FIRST_LOWER_CASE",
        "TO_UPPER_CASE",
        "TO_FIRST_UPPER_CASE",
        "TO_LOWER_CASE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MobaConstantValueFunction"

def test_mobanfcmoduletype_exists():
    # Check that the Enumeration exists
    assert MobaNFCModuleType is not None

def test_mobanfcmoduletype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MobaNFCModuleType]
    expected_literals = [
        "ID",
        "CUSTOM",
        "TEXT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MobaNFCModuleType"

def test_mobaupperbound_exists():
    # Check that the Enumeration exists
    assert MobaUpperBound is not None

def test_mobaupperbound_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MobaUpperBound]
    expected_literals = [
        "ONE",
        "NULL",
        "MANY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MobaUpperBound"

def test_mobalowerbound_exists():
    # Check that the Enumeration exists
    assert MobaLowerBound is not None

def test_mobalowerbound_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MobaLowerBound]
    expected_literals = [
        "ONE",
        "MANY",
        "ATLEASTONE",
        "OPTIONAL",
        "ZERO",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MobaLowerBound"

def test_mobageofenceevent_exists():
    # Check that the Enumeration exists
    assert MobaGeofenceEvent is not None

def test_mobageofenceevent_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MobaGeofenceEvent]
    expected_literals = [
        "ENTER",
        "LEAVE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MobaGeofenceEvent"

def test_mobarestmethods_exists():
    # Check that the Enumeration exists
    assert MobaRESTMethods is not None

def test_mobarestmethods_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MobaRESTMethods]
    expected_literals = [
        "PUT",
        "GET",
        "DELETE",
        "POST",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MobaRESTMethods"


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
index_moba_MobaApplication_strategy = st.builds(
    index_moba_MobaApplication,
)
moba_index_MobaIndexEntry_strategy = st.builds(
    moba_index_MobaIndexEntry,
    templateId=
        safe_text,
    templateVersion=
        safe_text,
    relativePath=
        safe_text,
    filename=
        safe_text,
    templateDescription=
        safe_text,
    templateName=
        safe_text
)
MobaIndexEntry_strategy = st.builds(
    MobaIndexEntry,
)
MobaExternalModule_strategy = st.builds(
    MobaExternalModule,
)
moba_MobaNFCModule_strategy = st.builds(
    moba_MobaNFCModule,
    type=
        safe_text
)
moba_MobaPushModule_strategy = st.builds(
    moba_MobaPushModule,
)
moba_MobaBluetoothModule_strategy = st.builds(
    moba_MobaBluetoothModule,
    type=
        safe_text
)
MobaPropertiesAble_strategy = st.builds(
    MobaPropertiesAble,
)
moba_MobaFriendsAble_strategy = st.builds(
    moba_MobaFriendsAble,
)
moba_MobaFriend_strategy = st.builds(
    moba_MobaFriend,
    valueString=
        safe_text,
    value=
        safe_text
)
moba_index_MobaIndex_strategy = st.builds(
    moba_index_MobaIndex,
    description=
        safe_text,
    id=
        safe_text,
    version=
        safe_text,
    name=
        safe_text
)
moba_MobaEnumLiteral_strategy = st.builds(
    moba_MobaEnumLiteral,
    undefined=
        st.booleans(),
    literal=
        safe_text,
    value=
        st.integers(),
    name=
        safe_text,
    default=
        st.booleans(),
    hidden=
        st.booleans()
)
MobaTrigger_strategy = st.builds(
    MobaTrigger,
)
moba_MobaSMSTrigger_strategy = st.builds(
    moba_MobaSMSTrigger,
)
moba_MobaTimerTrigger_strategy = st.builds(
    moba_MobaTimerTrigger,
)
moba_MobaPushTrigger_strategy = st.builds(
    moba_MobaPushTrigger,
)
moba_MobaGeofenceTrigger_strategy = st.builds(
    moba_MobaGeofenceTrigger,
    eventType=
        safe_text
)
moba_MobaDeviceStartupTrigger_strategy = st.builds(
    moba_MobaDeviceStartupTrigger,
)
moba_MobaEmailTrigger_strategy = st.builds(
    moba_MobaEmailTrigger,
)
moba_MobaAppUpdateTrigger_strategy = st.builds(
    moba_MobaAppUpdateTrigger,
)
moba_MobaAppInstallTrigger_strategy = st.builds(
    moba_MobaAppInstallTrigger,
)
MobaConstraint_strategy = st.builds(
    MobaConstraint,
)
moba_MobaMaxLengthConstraint_strategy = st.builds(
    moba_MobaMaxLengthConstraint,
    filterValue=
        st.integers()
)
moba_MobaDigitsConstraint_strategy = st.builds(
    moba_MobaDigitsConstraint,
    filterIntegerValue=
        st.integers(),
    filterFractionValue=
        st.integers()
)
moba_MobaRegexpConstraint_strategy = st.builds(
    moba_MobaRegexpConstraint,
    filterString=
        safe_text
)
moba_MobaConstraint_strategy = st.builds(
    moba_MobaConstraint,
)
moba_MobaConstraintable_strategy = st.builds(
    moba_MobaConstraintable,
)
MobaQueueFeature_strategy = st.builds(
    MobaQueueFeature,
)
moba_MobaQueueReference_strategy = st.builds(
    moba_MobaQueueReference,
)
moba_MobaMinLengthConstraint_strategy = st.builds(
    moba_MobaMinLengthConstraint,
    filterValue=
        st.integers()
)
moba_MobaNullConstraint_strategy = st.builds(
    moba_MobaNullConstraint,
)
moba_MobaNotNullConstraint_strategy = st.builds(
    moba_MobaNotNullConstraint,
)
moba_MobaPastConstraint_strategy = st.builds(
    moba_MobaPastConstraint,
)
moba_MobaFutureConstraint_strategy = st.builds(
    moba_MobaFutureConstraint,
)
moba_MobaMaxConstraint_strategy = st.builds(
    moba_MobaMaxConstraint,
    filterValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
moba_MobaMinConstraint_strategy = st.builds(
    moba_MobaMinConstraint,
    filterValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
moba_MobaMuliplicity_strategy = st.builds(
    moba_MobaMuliplicity,
    upper=
        safe_text,
    lower=
        safe_text
)
moba_MobaMultiplicityAble_strategy = st.builds(
    moba_MobaMultiplicityAble,
)
MobaEntityFeature_strategy = st.builds(
    MobaEntityFeature,
)
MobaDtoFeature_strategy = st.builds(
    MobaDtoFeature,
)
MobaRESTAbstractAttribute_strategy = st.builds(
    MobaRESTAbstractAttribute,
)
moba_MobaRESTDtoAttribute_strategy = st.builds(
    moba_MobaRESTDtoAttribute,
)
moba_MobaRESTAttribute_strategy = st.builds(
    moba_MobaRESTAttribute,
    formatString=
        safe_text,
    valueDouble=
        safe_text,
    valueString=
        safe_text,
    valueInt=
        safe_text,
    key=
        safe_text,
    keyString=
        safe_text,
    value=
        safe_text
)
moba_MobaRESTAbstractAttribute_strategy = st.builds(
    moba_MobaRESTAbstractAttribute,
    attachment=
        st.booleans(),
    aliasString=
        safe_text,
    alias=
        safe_text
)
MobaREST_strategy = st.builds(
    MobaREST,
)
moba_MobaRESTCrud_strategy = st.builds(
    moba_MobaRESTCrud,
    operations=
        safe_text
)
moba_MobaRESTWorkflow_strategy = st.builds(
    moba_MobaRESTWorkflow,
)
moba_MobaRESTCustomService_strategy = st.builds(
    moba_MobaRESTCustomService,
    operation=
        safe_text
)
moba_MobaRESTPayloadDefinition_strategy = st.builds(
    moba_MobaRESTPayloadDefinition,
    array=
        st.booleans()
)
moba_MobaEntityIndex_strategy = st.builds(
    moba_MobaEntityIndex,
    name=
        safe_text,
    unique=
        st.booleans()
)
moba_MobaRESTHeader_strategy = st.builds(
    moba_MobaRESTHeader,
    key=
        safe_text,
    value=
        safe_text,
    valueString=
        safe_text,
    contentTypeHeader=
        st.booleans(),
    rawHeader=
        st.booleans(),
    keyString=
        safe_text
)
MobaMultiplicityAble_strategy = st.builds(
    MobaMultiplicityAble,
)
moba_MobaEntityReference_strategy = st.builds(
    moba_MobaEntityReference,
    cascading=
        st.booleans(),
    transient=
        st.booleans(),
    lazy=
        st.booleans()
)
moba_MobaDtoReference_strategy = st.builds(
    moba_MobaDtoReference,
    cascading=
        st.booleans(),
    alias=
        safe_text,
    lazy=
        st.booleans(),
    transient=
        st.booleans()
)
moba_MobaDtoEmbeddable_strategy = st.builds(
    moba_MobaDtoEmbeddable,
    alias=
        safe_text,
    transient=
        st.booleans()
)
moba_MobaEntityEmbeddable_strategy = st.builds(
    moba_MobaEntityEmbeddable,
    transient=
        st.booleans()
)
MobaSettingsFeature_strategy = st.builds(
    MobaSettingsFeature,
)
MobaFeature_strategy = st.builds(
    MobaFeature,
)
moba_MobaQueueFeature_strategy = st.builds(
    moba_MobaQueueFeature,
)
moba_MobaEntityFeature_strategy = st.builds(
    moba_MobaEntityFeature,
)
moba_MobaDtoFeature_strategy = st.builds(
    moba_MobaDtoFeature,
)
moba_MobaSettingsFeature_strategy = st.builds(
    moba_MobaSettingsFeature,
)
MobaData_strategy = st.builds(
    MobaData,
)
moba_MobaDto_strategy = st.builds(
    moba_MobaDto,
    name=
        safe_text
)
moba_MobaQueue_strategy = st.builds(
    moba_MobaQueue,
    name=
        safe_text
)
moba_MobaEntity_strategy = st.builds(
    moba_MobaEntity,
    name=
        safe_text
)
moba_MobaConstantValue_strategy = st.builds(
    moba_MobaConstantValue,
    valueConstFunctions=
        safe_text,
    valueInt=
        safe_text,
    valueString=
        safe_text,
    valueDouble=
        safe_text,
    valueConstToLowerCase=
        st.booleans()
)
moba_MobaProperty_strategy = st.builds(
    moba_MobaProperty,
    key=
        safe_text,
    value=
        safe_text,
    keyString=
        safe_text,
    valueString=
        safe_text
)
moba_MobaPropertiesAble_strategy = st.builds(
    moba_MobaPropertiesAble,
)
moba_MobaGeneratorFeature_strategy = st.builds(
    moba_MobaGeneratorFeature,
)
MobaApplicationFeature_strategy = st.builds(
    MobaApplicationFeature,
)
moba_MobaExternalModule_strategy = st.builds(
    moba_MobaExternalModule,
    name=
        safe_text
)
moba_MobaConstant_strategy = st.builds(
    moba_MobaConstant,
    name=
        safe_text
)
moba_MobaSettings_strategy = st.builds(
    moba_MobaSettings,
    active=
        st.booleans(),
    name=
        safe_text
)
moba_MobaAuthorization_strategy = st.builds(
    moba_MobaAuthorization,
    name=
        safe_text
)
moba_MobaPersistenceType_strategy = st.builds(
    moba_MobaPersistenceType,
    name=
        safe_text
)
moba_MobaServer_strategy = st.builds(
    moba_MobaServer,
    urlString=
        safe_text,
    name=
        safe_text
)
moba_MobaData_strategy = st.builds(
    moba_MobaData,
)
moba_MobaGenerator_strategy = st.builds(
    moba_MobaGenerator,
    active=
        st.booleans(),
    name=
        safe_text
)
moba_MobaTransportSerializationType_strategy = st.builds(
    moba_MobaTransportSerializationType,
    name=
        safe_text
)
moba_MobaEnum_strategy = st.builds(
    moba_MobaEnum,
)
moba_MobaREST_strategy = st.builds(
    moba_MobaREST,
    url=
        safe_text,
    path=
        safe_text,
    name=
        safe_text,
    bigData=
        st.booleans()
)
moba_MobaTrigger_strategy = st.builds(
    moba_MobaTrigger,
    name=
        safe_text
)
moba_MobaTemplate_strategy = st.builds(
    moba_MobaTemplate,
    downloadTemplate=
        safe_text
)
MobaConstraintable_strategy = st.builds(
    MobaConstraintable,
)
moba_MobaSettingsEntityReference_strategy = st.builds(
    moba_MobaSettingsEntityReference,
    lazy=
        st.booleans(),
    cascading=
        st.booleans(),
    transient=
        st.booleans()
)
moba_MobaSettingsAttribute_strategy = st.builds(
    moba_MobaSettingsAttribute,
    formatString=
        safe_text,
    domainDescription=
        st.booleans(),
    lazy=
        st.booleans(),
    domainKey=
        st.booleans(),
    transient=
        st.booleans()
)
moba_MobaDtoAttribute_strategy = st.builds(
    moba_MobaDtoAttribute,
    lazy=
        st.booleans(),
    domainDescription=
        st.booleans(),
    transient=
        st.booleans(),
    domainKey=
        st.booleans(),
    alias=
        safe_text,
    formatString=
        safe_text
)
moba_MobaEntityAttribute_strategy = st.builds(
    moba_MobaEntityAttribute,
    formatString=
        safe_text,
    domainKey=
        st.booleans(),
    lazy=
        st.booleans(),
    transient=
        st.booleans(),
    domainDescription=
        st.booleans()
)
moba_MobaDataType_strategy = st.builds(
    moba_MobaDataType,
    timestamp=
        st.booleans(),
    decimal=
        st.booleans(),
    time=
        st.booleans(),
    date=
        st.booleans(),
    dateFormatString=
        safe_text,
    array=
        st.booleans(),
    name=
        safe_text,
    primitive=
        st.booleans(),
    numeric=
        st.booleans(),
    predefined=
        st.booleans(),
    string=
        st.booleans(),
    bool=
        st.booleans()
)
moba_MobaGeneratorSlot_strategy = st.builds(
    moba_MobaGeneratorSlot,
    name=
        safe_text,
    type=
        safe_text
)
MobaGeneratorFeature_strategy = st.builds(
    MobaGeneratorFeature,
)
moba_MobaGeneratorIDFeature_strategy = st.builds(
    moba_MobaGeneratorIDFeature,
    generatorVersion=
        safe_text,
    generatorId=
        safe_text
)
moba_MobaGeneratorMixinFeature_strategy = st.builds(
    moba_MobaGeneratorMixinFeature,
)
MobaFriendsAble_strategy = st.builds(
    MobaFriendsAble,
)
moba_MobaFeature_strategy = st.builds(
    moba_MobaFeature,
    name=
        safe_text
)
moba_MobaApplicationFeature_strategy = st.builds(
    moba_MobaApplicationFeature,
)
moba_MobaModel_strategy = st.builds(
    moba_MobaModel,
    copyright=
        safe_text
)
moba_MobaCache_strategy = st.builds(
    moba_MobaCache,
    cacheIntervalInt=
        st.integers(),
    cacheTypeString=
        safe_text,
    name=
        safe_text,
    cacheStrategyString=
        safe_text
)
MobaModelFeature_strategy = st.builds(
    MobaModelFeature,
)
moba_MobaApplication_strategy = st.builds(
    moba_MobaApplication,
    javaPackage=
        safe_text
)
moba_MobaProject_strategy = st.builds(
    moba_MobaProject,
)
moba_MobaModelFeature_strategy = st.builds(
    moba_MobaModelFeature,
    name=
        safe_text,
    id=
        safe_text,
    version=
        safe_text
)

@given(instance=index_moba_MobaApplication_strategy)
@settings(max_examples=50)
def test_index_moba_mobaapplication_instantiation(instance):
    assert isinstance(instance, index_moba_MobaApplication)

@given(instance=moba_index_MobaIndexEntry_strategy)
@settings(max_examples=50)
def test_moba_index_mobaindexentry_instantiation(instance):
    assert isinstance(instance, moba_index_MobaIndexEntry)



@given(instance=moba_index_MobaIndexEntry_strategy)
def test_moba_index_mobaindexentry_templateId_setter(instance):
    original = instance.templateId
    instance.templateId = original
    assert instance.templateId == original



@given(instance=moba_index_MobaIndexEntry_strategy)
def test_moba_index_mobaindexentry_templateVersion_setter(instance):
    original = instance.templateVersion
    instance.templateVersion = original
    assert instance.templateVersion == original



@given(instance=moba_index_MobaIndexEntry_strategy)
def test_moba_index_mobaindexentry_relativePath_setter(instance):
    original = instance.relativePath
    instance.relativePath = original
    assert instance.relativePath == original



@given(instance=moba_index_MobaIndexEntry_strategy)
def test_moba_index_mobaindexentry_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original



@given(instance=moba_index_MobaIndexEntry_strategy)
def test_moba_index_mobaindexentry_templateDescription_setter(instance):
    original = instance.templateDescription
    instance.templateDescription = original
    assert instance.templateDescription == original



@given(instance=moba_index_MobaIndexEntry_strategy)
def test_moba_index_mobaindexentry_templateName_setter(instance):
    original = instance.templateName
    instance.templateName = original
    assert instance.templateName == original

@given(instance=MobaIndexEntry_strategy)
@settings(max_examples=50)
def test_mobaindexentry_instantiation(instance):
    assert isinstance(instance, MobaIndexEntry)

@given(instance=MobaExternalModule_strategy)
@settings(max_examples=50)
def test_mobaexternalmodule_instantiation(instance):
    assert isinstance(instance, MobaExternalModule)

@given(instance=moba_MobaNFCModule_strategy)
@settings(max_examples=50)
def test_moba_mobanfcmodule_instantiation(instance):
    assert isinstance(instance, moba_MobaNFCModule)



@given(instance=moba_MobaNFCModule_strategy)
def test_moba_mobanfcmodule_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=moba_MobaPushModule_strategy)
@settings(max_examples=50)
def test_moba_mobapushmodule_instantiation(instance):
    assert isinstance(instance, moba_MobaPushModule)

@given(instance=moba_MobaBluetoothModule_strategy)
@settings(max_examples=50)
def test_moba_mobabluetoothmodule_instantiation(instance):
    assert isinstance(instance, moba_MobaBluetoothModule)



@given(instance=moba_MobaBluetoothModule_strategy)
def test_moba_mobabluetoothmodule_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=MobaPropertiesAble_strategy)
@settings(max_examples=50)
def test_mobapropertiesable_instantiation(instance):
    assert isinstance(instance, MobaPropertiesAble)

@given(instance=moba_MobaFriendsAble_strategy)
@settings(max_examples=50)
def test_moba_mobafriendsable_instantiation(instance):
    assert isinstance(instance, moba_MobaFriendsAble)

@given(instance=moba_MobaFriend_strategy)
@settings(max_examples=50)
def test_moba_mobafriend_instantiation(instance):
    assert isinstance(instance, moba_MobaFriend)



@given(instance=moba_MobaFriend_strategy)
def test_moba_mobafriend_valueString_setter(instance):
    original = instance.valueString
    instance.valueString = original
    assert instance.valueString == original



@given(instance=moba_MobaFriend_strategy)
def test_moba_mobafriend_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=moba_index_MobaIndex_strategy)
@settings(max_examples=50)
def test_moba_index_mobaindex_instantiation(instance):
    assert isinstance(instance, moba_index_MobaIndex)



@given(instance=moba_index_MobaIndex_strategy)
def test_moba_index_mobaindex_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=moba_index_MobaIndex_strategy)
def test_moba_index_mobaindex_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=moba_index_MobaIndex_strategy)
def test_moba_index_mobaindex_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=moba_index_MobaIndex_strategy)
def test_moba_index_mobaindex_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=moba_MobaEnumLiteral_strategy)
@settings(max_examples=50)
def test_moba_mobaenumliteral_instantiation(instance):
    assert isinstance(instance, moba_MobaEnumLiteral)



@given(instance=moba_MobaEnumLiteral_strategy)
def test_moba_mobaenumliteral_undefined_setter(instance):
    original = instance.undefined
    instance.undefined = original
    assert instance.undefined == original



@given(instance=moba_MobaEnumLiteral_strategy)
def test_moba_mobaenumliteral_literal_setter(instance):
    original = instance.literal
    instance.literal = original
    assert instance.literal == original



@given(instance=moba_MobaEnumLiteral_strategy)
def test_moba_mobaenumliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=moba_MobaEnumLiteral_strategy)
def test_moba_mobaenumliteral_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=moba_MobaEnumLiteral_strategy)
def test_moba_mobaenumliteral_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original



@given(instance=moba_MobaEnumLiteral_strategy)
def test_moba_mobaenumliteral_hidden_setter(instance):
    original = instance.hidden
    instance.hidden = original
    assert instance.hidden == original

@given(instance=MobaTrigger_strategy)
@settings(max_examples=50)
def test_mobatrigger_instantiation(instance):
    assert isinstance(instance, MobaTrigger)

@given(instance=moba_MobaSMSTrigger_strategy)
@settings(max_examples=50)
def test_moba_mobasmstrigger_instantiation(instance):
    assert isinstance(instance, moba_MobaSMSTrigger)

@given(instance=moba_MobaTimerTrigger_strategy)
@settings(max_examples=50)
def test_moba_mobatimertrigger_instantiation(instance):
    assert isinstance(instance, moba_MobaTimerTrigger)

@given(instance=moba_MobaPushTrigger_strategy)
@settings(max_examples=50)
def test_moba_mobapushtrigger_instantiation(instance):
    assert isinstance(instance, moba_MobaPushTrigger)

@given(instance=moba_MobaGeofenceTrigger_strategy)
@settings(max_examples=50)
def test_moba_mobageofencetrigger_instantiation(instance):
    assert isinstance(instance, moba_MobaGeofenceTrigger)



@given(instance=moba_MobaGeofenceTrigger_strategy)
def test_moba_mobageofencetrigger_eventType_setter(instance):
    original = instance.eventType
    instance.eventType = original
    assert instance.eventType == original

@given(instance=moba_MobaDeviceStartupTrigger_strategy)
@settings(max_examples=50)
def test_moba_mobadevicestartuptrigger_instantiation(instance):
    assert isinstance(instance, moba_MobaDeviceStartupTrigger)

@given(instance=moba_MobaEmailTrigger_strategy)
@settings(max_examples=50)
def test_moba_mobaemailtrigger_instantiation(instance):
    assert isinstance(instance, moba_MobaEmailTrigger)

@given(instance=moba_MobaAppUpdateTrigger_strategy)
@settings(max_examples=50)
def test_moba_mobaappupdatetrigger_instantiation(instance):
    assert isinstance(instance, moba_MobaAppUpdateTrigger)

@given(instance=moba_MobaAppInstallTrigger_strategy)
@settings(max_examples=50)
def test_moba_mobaappinstalltrigger_instantiation(instance):
    assert isinstance(instance, moba_MobaAppInstallTrigger)

@given(instance=MobaConstraint_strategy)
@settings(max_examples=50)
def test_mobaconstraint_instantiation(instance):
    assert isinstance(instance, MobaConstraint)

@given(instance=moba_MobaMaxLengthConstraint_strategy)
@settings(max_examples=50)
def test_moba_mobamaxlengthconstraint_instantiation(instance):
    assert isinstance(instance, moba_MobaMaxLengthConstraint)



@given(instance=moba_MobaMaxLengthConstraint_strategy)
def test_moba_mobamaxlengthconstraint_filterValue_setter(instance):
    original = instance.filterValue
    instance.filterValue = original
    assert instance.filterValue == original

@given(instance=moba_MobaDigitsConstraint_strategy)
@settings(max_examples=50)
def test_moba_mobadigitsconstraint_instantiation(instance):
    assert isinstance(instance, moba_MobaDigitsConstraint)



@given(instance=moba_MobaDigitsConstraint_strategy)
def test_moba_mobadigitsconstraint_filterIntegerValue_setter(instance):
    original = instance.filterIntegerValue
    instance.filterIntegerValue = original
    assert instance.filterIntegerValue == original



@given(instance=moba_MobaDigitsConstraint_strategy)
def test_moba_mobadigitsconstraint_filterFractionValue_setter(instance):
    original = instance.filterFractionValue
    instance.filterFractionValue = original
    assert instance.filterFractionValue == original

@given(instance=moba_MobaRegexpConstraint_strategy)
@settings(max_examples=50)
def test_moba_mobaregexpconstraint_instantiation(instance):
    assert isinstance(instance, moba_MobaRegexpConstraint)



@given(instance=moba_MobaRegexpConstraint_strategy)
def test_moba_mobaregexpconstraint_filterString_setter(instance):
    original = instance.filterString
    instance.filterString = original
    assert instance.filterString == original

@given(instance=moba_MobaConstraint_strategy)
@settings(max_examples=50)
def test_moba_mobaconstraint_instantiation(instance):
    assert isinstance(instance, moba_MobaConstraint)

@given(instance=moba_MobaConstraintable_strategy)
@settings(max_examples=50)
def test_moba_mobaconstraintable_instantiation(instance):
    assert isinstance(instance, moba_MobaConstraintable)

@given(instance=MobaQueueFeature_strategy)
@settings(max_examples=50)
def test_mobaqueuefeature_instantiation(instance):
    assert isinstance(instance, MobaQueueFeature)

@given(instance=moba_MobaQueueReference_strategy)
@settings(max_examples=50)
def test_moba_mobaqueuereference_instantiation(instance):
    assert isinstance(instance, moba_MobaQueueReference)

@given(instance=moba_MobaMinLengthConstraint_strategy)
@settings(max_examples=50)
def test_moba_mobaminlengthconstraint_instantiation(instance):
    assert isinstance(instance, moba_MobaMinLengthConstraint)



@given(instance=moba_MobaMinLengthConstraint_strategy)
def test_moba_mobaminlengthconstraint_filterValue_setter(instance):
    original = instance.filterValue
    instance.filterValue = original
    assert instance.filterValue == original

@given(instance=moba_MobaNullConstraint_strategy)
@settings(max_examples=50)
def test_moba_mobanullconstraint_instantiation(instance):
    assert isinstance(instance, moba_MobaNullConstraint)

@given(instance=moba_MobaNotNullConstraint_strategy)
@settings(max_examples=50)
def test_moba_mobanotnullconstraint_instantiation(instance):
    assert isinstance(instance, moba_MobaNotNullConstraint)

@given(instance=moba_MobaPastConstraint_strategy)
@settings(max_examples=50)
def test_moba_mobapastconstraint_instantiation(instance):
    assert isinstance(instance, moba_MobaPastConstraint)

@given(instance=moba_MobaFutureConstraint_strategy)
@settings(max_examples=50)
def test_moba_mobafutureconstraint_instantiation(instance):
    assert isinstance(instance, moba_MobaFutureConstraint)

@given(instance=moba_MobaMaxConstraint_strategy)
@settings(max_examples=50)
def test_moba_mobamaxconstraint_instantiation(instance):
    assert isinstance(instance, moba_MobaMaxConstraint)



@given(instance=moba_MobaMaxConstraint_strategy)
def test_moba_mobamaxconstraint_filterValue_setter(instance):
    original = instance.filterValue
    instance.filterValue = original
    assert instance.filterValue == original

@given(instance=moba_MobaMinConstraint_strategy)
@settings(max_examples=50)
def test_moba_mobaminconstraint_instantiation(instance):
    assert isinstance(instance, moba_MobaMinConstraint)



@given(instance=moba_MobaMinConstraint_strategy)
def test_moba_mobaminconstraint_filterValue_setter(instance):
    original = instance.filterValue
    instance.filterValue = original
    assert instance.filterValue == original

@given(instance=moba_MobaMuliplicity_strategy)
@settings(max_examples=50)
def test_moba_mobamuliplicity_instantiation(instance):
    assert isinstance(instance, moba_MobaMuliplicity)



@given(instance=moba_MobaMuliplicity_strategy)
def test_moba_mobamuliplicity_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original



@given(instance=moba_MobaMuliplicity_strategy)
def test_moba_mobamuliplicity_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=moba_MobaMultiplicityAble_strategy)
@settings(max_examples=50)
def test_moba_mobamultiplicityable_instantiation(instance):
    assert isinstance(instance, moba_MobaMultiplicityAble)

@given(instance=MobaEntityFeature_strategy)
@settings(max_examples=50)
def test_mobaentityfeature_instantiation(instance):
    assert isinstance(instance, MobaEntityFeature)

@given(instance=MobaDtoFeature_strategy)
@settings(max_examples=50)
def test_mobadtofeature_instantiation(instance):
    assert isinstance(instance, MobaDtoFeature)

@given(instance=MobaRESTAbstractAttribute_strategy)
@settings(max_examples=50)
def test_mobarestabstractattribute_instantiation(instance):
    assert isinstance(instance, MobaRESTAbstractAttribute)

@given(instance=moba_MobaRESTDtoAttribute_strategy)
@settings(max_examples=50)
def test_moba_mobarestdtoattribute_instantiation(instance):
    assert isinstance(instance, moba_MobaRESTDtoAttribute)

@given(instance=moba_MobaRESTAttribute_strategy)
@settings(max_examples=50)
def test_moba_mobarestattribute_instantiation(instance):
    assert isinstance(instance, moba_MobaRESTAttribute)



@given(instance=moba_MobaRESTAttribute_strategy)
def test_moba_mobarestattribute_formatString_setter(instance):
    original = instance.formatString
    instance.formatString = original
    assert instance.formatString == original



@given(instance=moba_MobaRESTAttribute_strategy)
def test_moba_mobarestattribute_valueDouble_setter(instance):
    original = instance.valueDouble
    instance.valueDouble = original
    assert instance.valueDouble == original



@given(instance=moba_MobaRESTAttribute_strategy)
def test_moba_mobarestattribute_valueString_setter(instance):
    original = instance.valueString
    instance.valueString = original
    assert instance.valueString == original



@given(instance=moba_MobaRESTAttribute_strategy)
def test_moba_mobarestattribute_valueInt_setter(instance):
    original = instance.valueInt
    instance.valueInt = original
    assert instance.valueInt == original



@given(instance=moba_MobaRESTAttribute_strategy)
def test_moba_mobarestattribute_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=moba_MobaRESTAttribute_strategy)
def test_moba_mobarestattribute_keyString_setter(instance):
    original = instance.keyString
    instance.keyString = original
    assert instance.keyString == original



@given(instance=moba_MobaRESTAttribute_strategy)
def test_moba_mobarestattribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=moba_MobaRESTAbstractAttribute_strategy)
@settings(max_examples=50)
def test_moba_mobarestabstractattribute_instantiation(instance):
    assert isinstance(instance, moba_MobaRESTAbstractAttribute)



@given(instance=moba_MobaRESTAbstractAttribute_strategy)
def test_moba_mobarestabstractattribute_attachment_setter(instance):
    original = instance.attachment
    instance.attachment = original
    assert instance.attachment == original



@given(instance=moba_MobaRESTAbstractAttribute_strategy)
def test_moba_mobarestabstractattribute_aliasString_setter(instance):
    original = instance.aliasString
    instance.aliasString = original
    assert instance.aliasString == original



@given(instance=moba_MobaRESTAbstractAttribute_strategy)
def test_moba_mobarestabstractattribute_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=MobaREST_strategy)
@settings(max_examples=50)
def test_mobarest_instantiation(instance):
    assert isinstance(instance, MobaREST)

@given(instance=moba_MobaRESTCrud_strategy)
@settings(max_examples=50)
def test_moba_mobarestcrud_instantiation(instance):
    assert isinstance(instance, moba_MobaRESTCrud)



@given(instance=moba_MobaRESTCrud_strategy)
def test_moba_mobarestcrud_operations_setter(instance):
    original = instance.operations
    instance.operations = original
    assert instance.operations == original

@given(instance=moba_MobaRESTWorkflow_strategy)
@settings(max_examples=50)
def test_moba_mobarestworkflow_instantiation(instance):
    assert isinstance(instance, moba_MobaRESTWorkflow)

@given(instance=moba_MobaRESTCustomService_strategy)
@settings(max_examples=50)
def test_moba_mobarestcustomservice_instantiation(instance):
    assert isinstance(instance, moba_MobaRESTCustomService)



@given(instance=moba_MobaRESTCustomService_strategy)
def test_moba_mobarestcustomservice_operation_setter(instance):
    original = instance.operation
    instance.operation = original
    assert instance.operation == original

@given(instance=moba_MobaRESTPayloadDefinition_strategy)
@settings(max_examples=50)
def test_moba_mobarestpayloaddefinition_instantiation(instance):
    assert isinstance(instance, moba_MobaRESTPayloadDefinition)



@given(instance=moba_MobaRESTPayloadDefinition_strategy)
def test_moba_mobarestpayloaddefinition_array_setter(instance):
    original = instance.array
    instance.array = original
    assert instance.array == original

@given(instance=moba_MobaEntityIndex_strategy)
@settings(max_examples=50)
def test_moba_mobaentityindex_instantiation(instance):
    assert isinstance(instance, moba_MobaEntityIndex)



@given(instance=moba_MobaEntityIndex_strategy)
def test_moba_mobaentityindex_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=moba_MobaEntityIndex_strategy)
def test_moba_mobaentityindex_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original

@given(instance=moba_MobaRESTHeader_strategy)
@settings(max_examples=50)
def test_moba_mobarestheader_instantiation(instance):
    assert isinstance(instance, moba_MobaRESTHeader)



@given(instance=moba_MobaRESTHeader_strategy)
def test_moba_mobarestheader_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=moba_MobaRESTHeader_strategy)
def test_moba_mobarestheader_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=moba_MobaRESTHeader_strategy)
def test_moba_mobarestheader_valueString_setter(instance):
    original = instance.valueString
    instance.valueString = original
    assert instance.valueString == original



@given(instance=moba_MobaRESTHeader_strategy)
def test_moba_mobarestheader_contentTypeHeader_setter(instance):
    original = instance.contentTypeHeader
    instance.contentTypeHeader = original
    assert instance.contentTypeHeader == original



@given(instance=moba_MobaRESTHeader_strategy)
def test_moba_mobarestheader_rawHeader_setter(instance):
    original = instance.rawHeader
    instance.rawHeader = original
    assert instance.rawHeader == original



@given(instance=moba_MobaRESTHeader_strategy)
def test_moba_mobarestheader_keyString_setter(instance):
    original = instance.keyString
    instance.keyString = original
    assert instance.keyString == original

@given(instance=MobaMultiplicityAble_strategy)
@settings(max_examples=50)
def test_mobamultiplicityable_instantiation(instance):
    assert isinstance(instance, MobaMultiplicityAble)

@given(instance=moba_MobaEntityReference_strategy)
@settings(max_examples=50)
def test_moba_mobaentityreference_instantiation(instance):
    assert isinstance(instance, moba_MobaEntityReference)



@given(instance=moba_MobaEntityReference_strategy)
def test_moba_mobaentityreference_cascading_setter(instance):
    original = instance.cascading
    instance.cascading = original
    assert instance.cascading == original



@given(instance=moba_MobaEntityReference_strategy)
def test_moba_mobaentityreference_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original



@given(instance=moba_MobaEntityReference_strategy)
def test_moba_mobaentityreference_lazy_setter(instance):
    original = instance.lazy
    instance.lazy = original
    assert instance.lazy == original

@given(instance=moba_MobaDtoReference_strategy)
@settings(max_examples=50)
def test_moba_mobadtoreference_instantiation(instance):
    assert isinstance(instance, moba_MobaDtoReference)



@given(instance=moba_MobaDtoReference_strategy)
def test_moba_mobadtoreference_cascading_setter(instance):
    original = instance.cascading
    instance.cascading = original
    assert instance.cascading == original



@given(instance=moba_MobaDtoReference_strategy)
def test_moba_mobadtoreference_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original



@given(instance=moba_MobaDtoReference_strategy)
def test_moba_mobadtoreference_lazy_setter(instance):
    original = instance.lazy
    instance.lazy = original
    assert instance.lazy == original



@given(instance=moba_MobaDtoReference_strategy)
def test_moba_mobadtoreference_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original

@given(instance=moba_MobaDtoEmbeddable_strategy)
@settings(max_examples=50)
def test_moba_mobadtoembeddable_instantiation(instance):
    assert isinstance(instance, moba_MobaDtoEmbeddable)



@given(instance=moba_MobaDtoEmbeddable_strategy)
def test_moba_mobadtoembeddable_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original



@given(instance=moba_MobaDtoEmbeddable_strategy)
def test_moba_mobadtoembeddable_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original

@given(instance=moba_MobaEntityEmbeddable_strategy)
@settings(max_examples=50)
def test_moba_mobaentityembeddable_instantiation(instance):
    assert isinstance(instance, moba_MobaEntityEmbeddable)



@given(instance=moba_MobaEntityEmbeddable_strategy)
def test_moba_mobaentityembeddable_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original

@given(instance=MobaSettingsFeature_strategy)
@settings(max_examples=50)
def test_mobasettingsfeature_instantiation(instance):
    assert isinstance(instance, MobaSettingsFeature)

@given(instance=MobaFeature_strategy)
@settings(max_examples=50)
def test_mobafeature_instantiation(instance):
    assert isinstance(instance, MobaFeature)

@given(instance=moba_MobaQueueFeature_strategy)
@settings(max_examples=50)
def test_moba_mobaqueuefeature_instantiation(instance):
    assert isinstance(instance, moba_MobaQueueFeature)

@given(instance=moba_MobaEntityFeature_strategy)
@settings(max_examples=50)
def test_moba_mobaentityfeature_instantiation(instance):
    assert isinstance(instance, moba_MobaEntityFeature)

@given(instance=moba_MobaDtoFeature_strategy)
@settings(max_examples=50)
def test_moba_mobadtofeature_instantiation(instance):
    assert isinstance(instance, moba_MobaDtoFeature)

@given(instance=moba_MobaSettingsFeature_strategy)
@settings(max_examples=50)
def test_moba_mobasettingsfeature_instantiation(instance):
    assert isinstance(instance, moba_MobaSettingsFeature)

@given(instance=MobaData_strategy)
@settings(max_examples=50)
def test_mobadata_instantiation(instance):
    assert isinstance(instance, MobaData)

@given(instance=moba_MobaDto_strategy)
@settings(max_examples=50)
def test_moba_mobadto_instantiation(instance):
    assert isinstance(instance, moba_MobaDto)



@given(instance=moba_MobaDto_strategy)
def test_moba_mobadto_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=moba_MobaQueue_strategy)
@settings(max_examples=50)
def test_moba_mobaqueue_instantiation(instance):
    assert isinstance(instance, moba_MobaQueue)



@given(instance=moba_MobaQueue_strategy)
def test_moba_mobaqueue_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=moba_MobaEntity_strategy)
@settings(max_examples=50)
def test_moba_mobaentity_instantiation(instance):
    assert isinstance(instance, moba_MobaEntity)



@given(instance=moba_MobaEntity_strategy)
def test_moba_mobaentity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=moba_MobaConstantValue_strategy)
@settings(max_examples=50)
def test_moba_mobaconstantvalue_instantiation(instance):
    assert isinstance(instance, moba_MobaConstantValue)



@given(instance=moba_MobaConstantValue_strategy)
def test_moba_mobaconstantvalue_valueConstFunctions_setter(instance):
    original = instance.valueConstFunctions
    instance.valueConstFunctions = original
    assert instance.valueConstFunctions == original



@given(instance=moba_MobaConstantValue_strategy)
def test_moba_mobaconstantvalue_valueInt_setter(instance):
    original = instance.valueInt
    instance.valueInt = original
    assert instance.valueInt == original



@given(instance=moba_MobaConstantValue_strategy)
def test_moba_mobaconstantvalue_valueString_setter(instance):
    original = instance.valueString
    instance.valueString = original
    assert instance.valueString == original



@given(instance=moba_MobaConstantValue_strategy)
def test_moba_mobaconstantvalue_valueDouble_setter(instance):
    original = instance.valueDouble
    instance.valueDouble = original
    assert instance.valueDouble == original



@given(instance=moba_MobaConstantValue_strategy)
def test_moba_mobaconstantvalue_valueConstToLowerCase_setter(instance):
    original = instance.valueConstToLowerCase
    instance.valueConstToLowerCase = original
    assert instance.valueConstToLowerCase == original

@given(instance=moba_MobaProperty_strategy)
@settings(max_examples=50)
def test_moba_mobaproperty_instantiation(instance):
    assert isinstance(instance, moba_MobaProperty)



@given(instance=moba_MobaProperty_strategy)
def test_moba_mobaproperty_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=moba_MobaProperty_strategy)
def test_moba_mobaproperty_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=moba_MobaProperty_strategy)
def test_moba_mobaproperty_keyString_setter(instance):
    original = instance.keyString
    instance.keyString = original
    assert instance.keyString == original



@given(instance=moba_MobaProperty_strategy)
def test_moba_mobaproperty_valueString_setter(instance):
    original = instance.valueString
    instance.valueString = original
    assert instance.valueString == original

@given(instance=moba_MobaPropertiesAble_strategy)
@settings(max_examples=50)
def test_moba_mobapropertiesable_instantiation(instance):
    assert isinstance(instance, moba_MobaPropertiesAble)

@given(instance=moba_MobaGeneratorFeature_strategy)
@settings(max_examples=50)
def test_moba_mobageneratorfeature_instantiation(instance):
    assert isinstance(instance, moba_MobaGeneratorFeature)

@given(instance=MobaApplicationFeature_strategy)
@settings(max_examples=50)
def test_mobaapplicationfeature_instantiation(instance):
    assert isinstance(instance, MobaApplicationFeature)

@given(instance=moba_MobaExternalModule_strategy)
@settings(max_examples=50)
def test_moba_mobaexternalmodule_instantiation(instance):
    assert isinstance(instance, moba_MobaExternalModule)



@given(instance=moba_MobaExternalModule_strategy)
def test_moba_mobaexternalmodule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=moba_MobaConstant_strategy)
@settings(max_examples=50)
def test_moba_mobaconstant_instantiation(instance):
    assert isinstance(instance, moba_MobaConstant)



@given(instance=moba_MobaConstant_strategy)
def test_moba_mobaconstant_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=moba_MobaSettings_strategy)
@settings(max_examples=50)
def test_moba_mobasettings_instantiation(instance):
    assert isinstance(instance, moba_MobaSettings)



@given(instance=moba_MobaSettings_strategy)
def test_moba_mobasettings_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original



@given(instance=moba_MobaSettings_strategy)
def test_moba_mobasettings_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=moba_MobaAuthorization_strategy)
@settings(max_examples=50)
def test_moba_mobaauthorization_instantiation(instance):
    assert isinstance(instance, moba_MobaAuthorization)



@given(instance=moba_MobaAuthorization_strategy)
def test_moba_mobaauthorization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=moba_MobaPersistenceType_strategy)
@settings(max_examples=50)
def test_moba_mobapersistencetype_instantiation(instance):
    assert isinstance(instance, moba_MobaPersistenceType)



@given(instance=moba_MobaPersistenceType_strategy)
def test_moba_mobapersistencetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=moba_MobaServer_strategy)
@settings(max_examples=50)
def test_moba_mobaserver_instantiation(instance):
    assert isinstance(instance, moba_MobaServer)



@given(instance=moba_MobaServer_strategy)
def test_moba_mobaserver_urlString_setter(instance):
    original = instance.urlString
    instance.urlString = original
    assert instance.urlString == original



@given(instance=moba_MobaServer_strategy)
def test_moba_mobaserver_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=moba_MobaData_strategy)
@settings(max_examples=50)
def test_moba_mobadata_instantiation(instance):
    assert isinstance(instance, moba_MobaData)

@given(instance=moba_MobaGenerator_strategy)
@settings(max_examples=50)
def test_moba_mobagenerator_instantiation(instance):
    assert isinstance(instance, moba_MobaGenerator)



@given(instance=moba_MobaGenerator_strategy)
def test_moba_mobagenerator_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original



@given(instance=moba_MobaGenerator_strategy)
def test_moba_mobagenerator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=moba_MobaTransportSerializationType_strategy)
@settings(max_examples=50)
def test_moba_mobatransportserializationtype_instantiation(instance):
    assert isinstance(instance, moba_MobaTransportSerializationType)



@given(instance=moba_MobaTransportSerializationType_strategy)
def test_moba_mobatransportserializationtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=moba_MobaEnum_strategy)
@settings(max_examples=50)
def test_moba_mobaenum_instantiation(instance):
    assert isinstance(instance, moba_MobaEnum)

@given(instance=moba_MobaREST_strategy)
@settings(max_examples=50)
def test_moba_mobarest_instantiation(instance):
    assert isinstance(instance, moba_MobaREST)



@given(instance=moba_MobaREST_strategy)
def test_moba_mobarest_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original



@given(instance=moba_MobaREST_strategy)
def test_moba_mobarest_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original



@given(instance=moba_MobaREST_strategy)
def test_moba_mobarest_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=moba_MobaREST_strategy)
def test_moba_mobarest_bigData_setter(instance):
    original = instance.bigData
    instance.bigData = original
    assert instance.bigData == original

@given(instance=moba_MobaTrigger_strategy)
@settings(max_examples=50)
def test_moba_mobatrigger_instantiation(instance):
    assert isinstance(instance, moba_MobaTrigger)



@given(instance=moba_MobaTrigger_strategy)
def test_moba_mobatrigger_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=moba_MobaTemplate_strategy)
@settings(max_examples=50)
def test_moba_mobatemplate_instantiation(instance):
    assert isinstance(instance, moba_MobaTemplate)



@given(instance=moba_MobaTemplate_strategy)
def test_moba_mobatemplate_downloadTemplate_setter(instance):
    original = instance.downloadTemplate
    instance.downloadTemplate = original
    assert instance.downloadTemplate == original

@given(instance=MobaConstraintable_strategy)
@settings(max_examples=50)
def test_mobaconstraintable_instantiation(instance):
    assert isinstance(instance, MobaConstraintable)

@given(instance=moba_MobaSettingsEntityReference_strategy)
@settings(max_examples=50)
def test_moba_mobasettingsentityreference_instantiation(instance):
    assert isinstance(instance, moba_MobaSettingsEntityReference)



@given(instance=moba_MobaSettingsEntityReference_strategy)
def test_moba_mobasettingsentityreference_lazy_setter(instance):
    original = instance.lazy
    instance.lazy = original
    assert instance.lazy == original



@given(instance=moba_MobaSettingsEntityReference_strategy)
def test_moba_mobasettingsentityreference_cascading_setter(instance):
    original = instance.cascading
    instance.cascading = original
    assert instance.cascading == original



@given(instance=moba_MobaSettingsEntityReference_strategy)
def test_moba_mobasettingsentityreference_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original

@given(instance=moba_MobaSettingsAttribute_strategy)
@settings(max_examples=50)
def test_moba_mobasettingsattribute_instantiation(instance):
    assert isinstance(instance, moba_MobaSettingsAttribute)



@given(instance=moba_MobaSettingsAttribute_strategy)
def test_moba_mobasettingsattribute_formatString_setter(instance):
    original = instance.formatString
    instance.formatString = original
    assert instance.formatString == original



@given(instance=moba_MobaSettingsAttribute_strategy)
def test_moba_mobasettingsattribute_domainDescription_setter(instance):
    original = instance.domainDescription
    instance.domainDescription = original
    assert instance.domainDescription == original



@given(instance=moba_MobaSettingsAttribute_strategy)
def test_moba_mobasettingsattribute_lazy_setter(instance):
    original = instance.lazy
    instance.lazy = original
    assert instance.lazy == original



@given(instance=moba_MobaSettingsAttribute_strategy)
def test_moba_mobasettingsattribute_domainKey_setter(instance):
    original = instance.domainKey
    instance.domainKey = original
    assert instance.domainKey == original



@given(instance=moba_MobaSettingsAttribute_strategy)
def test_moba_mobasettingsattribute_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original

@given(instance=moba_MobaDtoAttribute_strategy)
@settings(max_examples=50)
def test_moba_mobadtoattribute_instantiation(instance):
    assert isinstance(instance, moba_MobaDtoAttribute)



@given(instance=moba_MobaDtoAttribute_strategy)
def test_moba_mobadtoattribute_lazy_setter(instance):
    original = instance.lazy
    instance.lazy = original
    assert instance.lazy == original



@given(instance=moba_MobaDtoAttribute_strategy)
def test_moba_mobadtoattribute_domainDescription_setter(instance):
    original = instance.domainDescription
    instance.domainDescription = original
    assert instance.domainDescription == original



@given(instance=moba_MobaDtoAttribute_strategy)
def test_moba_mobadtoattribute_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original



@given(instance=moba_MobaDtoAttribute_strategy)
def test_moba_mobadtoattribute_domainKey_setter(instance):
    original = instance.domainKey
    instance.domainKey = original
    assert instance.domainKey == original



@given(instance=moba_MobaDtoAttribute_strategy)
def test_moba_mobadtoattribute_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original



@given(instance=moba_MobaDtoAttribute_strategy)
def test_moba_mobadtoattribute_formatString_setter(instance):
    original = instance.formatString
    instance.formatString = original
    assert instance.formatString == original

@given(instance=moba_MobaEntityAttribute_strategy)
@settings(max_examples=50)
def test_moba_mobaentityattribute_instantiation(instance):
    assert isinstance(instance, moba_MobaEntityAttribute)



@given(instance=moba_MobaEntityAttribute_strategy)
def test_moba_mobaentityattribute_formatString_setter(instance):
    original = instance.formatString
    instance.formatString = original
    assert instance.formatString == original



@given(instance=moba_MobaEntityAttribute_strategy)
def test_moba_mobaentityattribute_domainKey_setter(instance):
    original = instance.domainKey
    instance.domainKey = original
    assert instance.domainKey == original



@given(instance=moba_MobaEntityAttribute_strategy)
def test_moba_mobaentityattribute_lazy_setter(instance):
    original = instance.lazy
    instance.lazy = original
    assert instance.lazy == original



@given(instance=moba_MobaEntityAttribute_strategy)
def test_moba_mobaentityattribute_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original



@given(instance=moba_MobaEntityAttribute_strategy)
def test_moba_mobaentityattribute_domainDescription_setter(instance):
    original = instance.domainDescription
    instance.domainDescription = original
    assert instance.domainDescription == original

@given(instance=moba_MobaDataType_strategy)
@settings(max_examples=50)
def test_moba_mobadatatype_instantiation(instance):
    assert isinstance(instance, moba_MobaDataType)



@given(instance=moba_MobaDataType_strategy)
def test_moba_mobadatatype_timestamp_setter(instance):
    original = instance.timestamp
    instance.timestamp = original
    assert instance.timestamp == original



@given(instance=moba_MobaDataType_strategy)
def test_moba_mobadatatype_decimal_setter(instance):
    original = instance.decimal
    instance.decimal = original
    assert instance.decimal == original



@given(instance=moba_MobaDataType_strategy)
def test_moba_mobadatatype_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=moba_MobaDataType_strategy)
def test_moba_mobadatatype_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=moba_MobaDataType_strategy)
def test_moba_mobadatatype_dateFormatString_setter(instance):
    original = instance.dateFormatString
    instance.dateFormatString = original
    assert instance.dateFormatString == original



@given(instance=moba_MobaDataType_strategy)
def test_moba_mobadatatype_array_setter(instance):
    original = instance.array
    instance.array = original
    assert instance.array == original



@given(instance=moba_MobaDataType_strategy)
def test_moba_mobadatatype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=moba_MobaDataType_strategy)
def test_moba_mobadatatype_primitive_setter(instance):
    original = instance.primitive
    instance.primitive = original
    assert instance.primitive == original



@given(instance=moba_MobaDataType_strategy)
def test_moba_mobadatatype_numeric_setter(instance):
    original = instance.numeric
    instance.numeric = original
    assert instance.numeric == original



@given(instance=moba_MobaDataType_strategy)
def test_moba_mobadatatype_predefined_setter(instance):
    original = instance.predefined
    instance.predefined = original
    assert instance.predefined == original



@given(instance=moba_MobaDataType_strategy)
def test_moba_mobadatatype_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original



@given(instance=moba_MobaDataType_strategy)
def test_moba_mobadatatype_bool_setter(instance):
    original = instance.bool
    instance.bool = original
    assert instance.bool == original

@given(instance=moba_MobaGeneratorSlot_strategy)
@settings(max_examples=50)
def test_moba_mobageneratorslot_instantiation(instance):
    assert isinstance(instance, moba_MobaGeneratorSlot)



@given(instance=moba_MobaGeneratorSlot_strategy)
def test_moba_mobageneratorslot_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=moba_MobaGeneratorSlot_strategy)
def test_moba_mobageneratorslot_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=MobaGeneratorFeature_strategy)
@settings(max_examples=50)
def test_mobageneratorfeature_instantiation(instance):
    assert isinstance(instance, MobaGeneratorFeature)

@given(instance=moba_MobaGeneratorIDFeature_strategy)
@settings(max_examples=50)
def test_moba_mobageneratoridfeature_instantiation(instance):
    assert isinstance(instance, moba_MobaGeneratorIDFeature)



@given(instance=moba_MobaGeneratorIDFeature_strategy)
def test_moba_mobageneratoridfeature_generatorVersion_setter(instance):
    original = instance.generatorVersion
    instance.generatorVersion = original
    assert instance.generatorVersion == original



@given(instance=moba_MobaGeneratorIDFeature_strategy)
def test_moba_mobageneratoridfeature_generatorId_setter(instance):
    original = instance.generatorId
    instance.generatorId = original
    assert instance.generatorId == original

@given(instance=moba_MobaGeneratorMixinFeature_strategy)
@settings(max_examples=50)
def test_moba_mobageneratormixinfeature_instantiation(instance):
    assert isinstance(instance, moba_MobaGeneratorMixinFeature)

@given(instance=MobaFriendsAble_strategy)
@settings(max_examples=50)
def test_mobafriendsable_instantiation(instance):
    assert isinstance(instance, MobaFriendsAble)

@given(instance=moba_MobaFeature_strategy)
@settings(max_examples=50)
def test_moba_mobafeature_instantiation(instance):
    assert isinstance(instance, moba_MobaFeature)



@given(instance=moba_MobaFeature_strategy)
def test_moba_mobafeature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=moba_MobaApplicationFeature_strategy)
@settings(max_examples=50)
def test_moba_mobaapplicationfeature_instantiation(instance):
    assert isinstance(instance, moba_MobaApplicationFeature)

@given(instance=moba_MobaModel_strategy)
@settings(max_examples=50)
def test_moba_mobamodel_instantiation(instance):
    assert isinstance(instance, moba_MobaModel)



@given(instance=moba_MobaModel_strategy)
def test_moba_mobamodel_copyright_setter(instance):
    original = instance.copyright
    instance.copyright = original
    assert instance.copyright == original

@given(instance=moba_MobaCache_strategy)
@settings(max_examples=50)
def test_moba_mobacache_instantiation(instance):
    assert isinstance(instance, moba_MobaCache)



@given(instance=moba_MobaCache_strategy)
def test_moba_mobacache_cacheIntervalInt_setter(instance):
    original = instance.cacheIntervalInt
    instance.cacheIntervalInt = original
    assert instance.cacheIntervalInt == original



@given(instance=moba_MobaCache_strategy)
def test_moba_mobacache_cacheTypeString_setter(instance):
    original = instance.cacheTypeString
    instance.cacheTypeString = original
    assert instance.cacheTypeString == original



@given(instance=moba_MobaCache_strategy)
def test_moba_mobacache_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=moba_MobaCache_strategy)
def test_moba_mobacache_cacheStrategyString_setter(instance):
    original = instance.cacheStrategyString
    instance.cacheStrategyString = original
    assert instance.cacheStrategyString == original

@given(instance=MobaModelFeature_strategy)
@settings(max_examples=50)
def test_mobamodelfeature_instantiation(instance):
    assert isinstance(instance, MobaModelFeature)

@given(instance=moba_MobaApplication_strategy)
@settings(max_examples=50)
def test_moba_mobaapplication_instantiation(instance):
    assert isinstance(instance, moba_MobaApplication)



@given(instance=moba_MobaApplication_strategy)
def test_moba_mobaapplication_javaPackage_setter(instance):
    original = instance.javaPackage
    instance.javaPackage = original
    assert instance.javaPackage == original

@given(instance=moba_MobaProject_strategy)
@settings(max_examples=50)
def test_moba_mobaproject_instantiation(instance):
    assert isinstance(instance, moba_MobaProject)

@given(instance=moba_MobaModelFeature_strategy)
@settings(max_examples=50)
def test_moba_mobamodelfeature_instantiation(instance):
    assert isinstance(instance, moba_MobaModelFeature)



@given(instance=moba_MobaModelFeature_strategy)
def test_moba_mobamodelfeature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=moba_MobaModelFeature_strategy)
def test_moba_mobamodelfeature_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=moba_MobaModelFeature_strategy)
def test_moba_mobamodelfeature_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original
