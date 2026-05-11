import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    index::moba::MobaApplication,
    moba::index::MobaIndexEntry,
    MobaIndexEntry,
    MobaExternalModule,
    moba::MobaNFCModule,
    moba::MobaPushModule,
    moba::MobaBluetoothModule,
    MobaPropertiesAble,
    moba::MobaFriendsAble,
    moba::MobaFriend,
    moba::index::MobaIndex,
    moba::MobaEnumLiteral,
    MobaTrigger,
    moba::MobaTimerTrigger,
    moba::MobaGeofenceTrigger,
    moba::MobaAppUpdateTrigger,
    moba::MobaEmailTrigger,
    moba::MobaSMSTrigger,
    moba::MobaDeviceStartupTrigger,
    moba::MobaPushTrigger,
    moba::MobaAppInstallTrigger,
    MobaConstraint,
    moba::MobaDigitsConstraint,
    moba::MobaMaxLengthConstraint,
    moba::MobaRegexpConstraint,
    moba::MobaConstraint,
    moba::MobaConstraintable,
    MobaQueueFeature,
    moba::MobaQueueReference,
    moba::MobaMinLengthConstraint,
    moba::MobaNullConstraint,
    moba::MobaNotNullConstraint,
    moba::MobaPastConstraint,
    moba::MobaFutureConstraint,
    moba::MobaMaxConstraint,
    moba::MobaMinConstraint,
    moba::MobaMuliplicity,
    moba::MobaMultiplicityAble,
    MobaEntityFeature,
    MobaDtoFeature,
    MobaRESTAbstractAttribute,
    moba::MobaRESTDtoAttribute,
    moba::MobaRESTAttribute,
    moba::MobaRESTAbstractAttribute,
    MobaREST,
    moba::MobaRESTWorkflow,
    moba::MobaRESTCrud,
    moba::MobaRESTCustomService,
    moba::MobaRESTPayloadDefinition,
    moba::MobaEntityIndex,
    moba::MobaRESTHeader,
    MobaMultiplicityAble,
    moba::MobaDtoEmbeddable,
    moba::MobaEntityEmbeddable,
    moba::MobaEntityReference,
    moba::MobaDtoReference,
    MobaSettingsFeature,
    MobaFeature,
    moba::MobaEntityFeature,
    moba::MobaDtoFeature,
    moba::MobaQueueFeature,
    moba::MobaSettingsFeature,
    MobaData,
    moba::MobaQueue,
    moba::MobaDto,
    moba::MobaEntity,
    moba::MobaConstantValue,
    moba::MobaProperty,
    moba::MobaPropertiesAble,
    moba::MobaGeneratorFeature,
    MobaApplicationFeature,
    moba::MobaSettings,
    moba::MobaTransportSerializationType,
    moba::MobaGenerator,
    moba::MobaServer,
    moba::MobaData,
    moba::MobaEnum,
    moba::MobaAuthorization,
    moba::MobaConstant,
    moba::MobaTrigger,
    moba::MobaExternalModule,
    moba::MobaPersistenceType,
    moba::MobaREST,
    moba::MobaTemplate,
    MobaConstraintable,
    moba::MobaEntityAttribute,
    moba::MobaSettingsAttribute,
    moba::MobaDtoAttribute,
    moba::MobaSettingsEntityReference,
    moba::MobaDataType,
    moba::MobaGeneratorSlot,
    MobaGeneratorFeature,
    moba::MobaGeneratorIDFeature,
    moba::MobaGeneratorMixinFeature,
    MobaFriendsAble,
    moba::MobaApplicationFeature,
    moba::MobaFeature,
    moba::MobaModel,
    moba::MobaCache,
    MobaModelFeature,
    moba::MobaApplication,
    moba::MobaProject,
    moba::MobaModelFeature,
    MobaLowerBound,
    MobaGeofenceEvent,
    MobaNFCModuleType,
    MobaBlueToothModuleType,
    MobaRESTMethods,
    MobaUpperBound,
    MobaConstantValueFunction,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_index::moba::mobaapplication_is_not_abstract():
    assert not inspect.isabstract(index::moba::MobaApplication)


def test_index::moba::mobaapplication_constructor_exists():
    assert callable(index::moba::MobaApplication.__init__)


def test_index::moba::mobaapplication_constructor_args():
    sig = inspect.signature(index::moba::MobaApplication.__init__)
    params = list(sig.parameters.keys())



def test_moba::index::mobaindexentry_is_not_abstract():
    assert not inspect.isabstract(moba::index::MobaIndexEntry)


def test_moba::index::mobaindexentry_constructor_exists():
    assert callable(moba::index::MobaIndexEntry.__init__)


def test_moba::index::mobaindexentry_constructor_args():
    sig = inspect.signature(moba::index::MobaIndexEntry.__init__)
    params = list(sig.parameters.keys())
    assert "templateId" in params, "Missing parameter 'templateId'"
    assert "relativePath" in params, "Missing parameter 'relativePath'"
    assert "templateName" in params, "Missing parameter 'templateName'"
    assert "filename" in params, "Missing parameter 'filename'"
    assert "templateDescription" in params, "Missing parameter 'templateDescription'"
    assert "templateVersion" in params, "Missing parameter 'templateVersion'"

def test_moba::index::mobaindexentry_has_templateId():
    assert hasattr(moba::index::MobaIndexEntry, "templateId")
    descriptor = None
    for klass in moba::index::MobaIndexEntry.__mro__:
        if "templateId" in klass.__dict__:
            descriptor = klass.__dict__["templateId"]
            break
    assert isinstance(descriptor, property)

def test_moba::index::mobaindexentry_has_relativePath():
    assert hasattr(moba::index::MobaIndexEntry, "relativePath")
    descriptor = None
    for klass in moba::index::MobaIndexEntry.__mro__:
        if "relativePath" in klass.__dict__:
            descriptor = klass.__dict__["relativePath"]
            break
    assert isinstance(descriptor, property)

def test_moba::index::mobaindexentry_has_templateName():
    assert hasattr(moba::index::MobaIndexEntry, "templateName")
    descriptor = None
    for klass in moba::index::MobaIndexEntry.__mro__:
        if "templateName" in klass.__dict__:
            descriptor = klass.__dict__["templateName"]
            break
    assert isinstance(descriptor, property)

def test_moba::index::mobaindexentry_has_filename():
    assert hasattr(moba::index::MobaIndexEntry, "filename")
    descriptor = None
    for klass in moba::index::MobaIndexEntry.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)

def test_moba::index::mobaindexentry_has_templateDescription():
    assert hasattr(moba::index::MobaIndexEntry, "templateDescription")
    descriptor = None
    for klass in moba::index::MobaIndexEntry.__mro__:
        if "templateDescription" in klass.__dict__:
            descriptor = klass.__dict__["templateDescription"]
            break
    assert isinstance(descriptor, property)

def test_moba::index::mobaindexentry_has_templateVersion():
    assert hasattr(moba::index::MobaIndexEntry, "templateVersion")
    descriptor = None
    for klass in moba::index::MobaIndexEntry.__mro__:
        if "templateVersion" in klass.__dict__:
            descriptor = klass.__dict__["templateVersion"]
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



def test_moba::mobanfcmodule_is_not_abstract():
    assert not inspect.isabstract(moba::MobaNFCModule)


def test_moba::mobanfcmodule_constructor_exists():
    assert callable(moba::MobaNFCModule.__init__)


def test_moba::mobanfcmodule_constructor_args():
    sig = inspect.signature(moba::MobaNFCModule.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_moba::mobanfcmodule_has_type():
    assert hasattr(moba::MobaNFCModule, "type")
    descriptor = None
    for klass in moba::MobaNFCModule.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobapushmodule_is_not_abstract():
    assert not inspect.isabstract(moba::MobaPushModule)


def test_moba::mobapushmodule_constructor_exists():
    assert callable(moba::MobaPushModule.__init__)


def test_moba::mobapushmodule_constructor_args():
    sig = inspect.signature(moba::MobaPushModule.__init__)
    params = list(sig.parameters.keys())



def test_moba::mobabluetoothmodule_is_not_abstract():
    assert not inspect.isabstract(moba::MobaBluetoothModule)


def test_moba::mobabluetoothmodule_constructor_exists():
    assert callable(moba::MobaBluetoothModule.__init__)


def test_moba::mobabluetoothmodule_constructor_args():
    sig = inspect.signature(moba::MobaBluetoothModule.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_moba::mobabluetoothmodule_has_type():
    assert hasattr(moba::MobaBluetoothModule, "type")
    descriptor = None
    for klass in moba::MobaBluetoothModule.__mro__:
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



def test_moba::mobafriendsable_is_not_abstract():
    assert not inspect.isabstract(moba::MobaFriendsAble)


def test_moba::mobafriendsable_constructor_exists():
    assert callable(moba::MobaFriendsAble.__init__)


def test_moba::mobafriendsable_constructor_args():
    sig = inspect.signature(moba::MobaFriendsAble.__init__)
    params = list(sig.parameters.keys())



def test_moba::mobafriend_is_not_abstract():
    assert not inspect.isabstract(moba::MobaFriend)


def test_moba::mobafriend_constructor_exists():
    assert callable(moba::MobaFriend.__init__)


def test_moba::mobafriend_constructor_args():
    sig = inspect.signature(moba::MobaFriend.__init__)
    params = list(sig.parameters.keys())
    assert "valueString" in params, "Missing parameter 'valueString'"
    assert "value" in params, "Missing parameter 'value'"

def test_moba::mobafriend_has_valueString():
    assert hasattr(moba::MobaFriend, "valueString")
    descriptor = None
    for klass in moba::MobaFriend.__mro__:
        if "valueString" in klass.__dict__:
            descriptor = klass.__dict__["valueString"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobafriend_has_value():
    assert hasattr(moba::MobaFriend, "value")
    descriptor = None
    for klass in moba::MobaFriend.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_moba::index::mobaindex_is_not_abstract():
    assert not inspect.isabstract(moba::index::MobaIndex)


def test_moba::index::mobaindex_constructor_exists():
    assert callable(moba::index::MobaIndex.__init__)


def test_moba::index::mobaindex_constructor_args():
    sig = inspect.signature(moba::index::MobaIndex.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "version" in params, "Missing parameter 'version'"
    assert "description" in params, "Missing parameter 'description'"
    assert "id" in params, "Missing parameter 'id'"

def test_moba::index::mobaindex_has_name():
    assert hasattr(moba::index::MobaIndex, "name")
    descriptor = None
    for klass in moba::index::MobaIndex.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_moba::index::mobaindex_has_version():
    assert hasattr(moba::index::MobaIndex, "version")
    descriptor = None
    for klass in moba::index::MobaIndex.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_moba::index::mobaindex_has_description():
    assert hasattr(moba::index::MobaIndex, "description")
    descriptor = None
    for klass in moba::index::MobaIndex.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_moba::index::mobaindex_has_id():
    assert hasattr(moba::index::MobaIndex, "id")
    descriptor = None
    for klass in moba::index::MobaIndex.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobaenumliteral_is_not_abstract():
    assert not inspect.isabstract(moba::MobaEnumLiteral)


def test_moba::mobaenumliteral_constructor_exists():
    assert callable(moba::MobaEnumLiteral.__init__)


def test_moba::mobaenumliteral_constructor_args():
    sig = inspect.signature(moba::MobaEnumLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "hidden" in params, "Missing parameter 'hidden'"
    assert "undefined" in params, "Missing parameter 'undefined'"
    assert "name" in params, "Missing parameter 'name'"
    assert "default" in params, "Missing parameter 'default'"
    assert "literal" in params, "Missing parameter 'literal'"
    assert "value" in params, "Missing parameter 'value'"

def test_moba::mobaenumliteral_has_hidden():
    assert hasattr(moba::MobaEnumLiteral, "hidden")
    descriptor = None
    for klass in moba::MobaEnumLiteral.__mro__:
        if "hidden" in klass.__dict__:
            descriptor = klass.__dict__["hidden"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobaenumliteral_has_undefined():
    assert hasattr(moba::MobaEnumLiteral, "undefined")
    descriptor = None
    for klass in moba::MobaEnumLiteral.__mro__:
        if "undefined" in klass.__dict__:
            descriptor = klass.__dict__["undefined"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobaenumliteral_has_name():
    assert hasattr(moba::MobaEnumLiteral, "name")
    descriptor = None
    for klass in moba::MobaEnumLiteral.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobaenumliteral_has_default():
    assert hasattr(moba::MobaEnumLiteral, "default")
    descriptor = None
    for klass in moba::MobaEnumLiteral.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobaenumliteral_has_literal():
    assert hasattr(moba::MobaEnumLiteral, "literal")
    descriptor = None
    for klass in moba::MobaEnumLiteral.__mro__:
        if "literal" in klass.__dict__:
            descriptor = klass.__dict__["literal"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobaenumliteral_has_value():
    assert hasattr(moba::MobaEnumLiteral, "value")
    descriptor = None
    for klass in moba::MobaEnumLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mobatrigger_is_not_abstract():
    assert not inspect.isabstract(MobaTrigger)


def test_mobatrigger_constructor_exists():
    assert callable(MobaTrigger.__init__)


def test_mobatrigger_constructor_args():
    sig = inspect.signature(MobaTrigger.__init__)
    params = list(sig.parameters.keys())



def test_moba::mobatimertrigger_is_not_abstract():
    assert not inspect.isabstract(moba::MobaTimerTrigger)


def test_moba::mobatimertrigger_constructor_exists():
    assert callable(moba::MobaTimerTrigger.__init__)


def test_moba::mobatimertrigger_constructor_args():
    sig = inspect.signature(moba::MobaTimerTrigger.__init__)
    params = list(sig.parameters.keys())



def test_moba::mobageofencetrigger_is_not_abstract():
    assert not inspect.isabstract(moba::MobaGeofenceTrigger)


def test_moba::mobageofencetrigger_constructor_exists():
    assert callable(moba::MobaGeofenceTrigger.__init__)


def test_moba::mobageofencetrigger_constructor_args():
    sig = inspect.signature(moba::MobaGeofenceTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "eventType" in params, "Missing parameter 'eventType'"

def test_moba::mobageofencetrigger_has_eventType():
    assert hasattr(moba::MobaGeofenceTrigger, "eventType")
    descriptor = None
    for klass in moba::MobaGeofenceTrigger.__mro__:
        if "eventType" in klass.__dict__:
            descriptor = klass.__dict__["eventType"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobaappupdatetrigger_is_not_abstract():
    assert not inspect.isabstract(moba::MobaAppUpdateTrigger)


def test_moba::mobaappupdatetrigger_constructor_exists():
    assert callable(moba::MobaAppUpdateTrigger.__init__)


def test_moba::mobaappupdatetrigger_constructor_args():
    sig = inspect.signature(moba::MobaAppUpdateTrigger.__init__)
    params = list(sig.parameters.keys())



def test_moba::mobaemailtrigger_is_not_abstract():
    assert not inspect.isabstract(moba::MobaEmailTrigger)


def test_moba::mobaemailtrigger_constructor_exists():
    assert callable(moba::MobaEmailTrigger.__init__)


def test_moba::mobaemailtrigger_constructor_args():
    sig = inspect.signature(moba::MobaEmailTrigger.__init__)
    params = list(sig.parameters.keys())



def test_moba::mobasmstrigger_is_not_abstract():
    assert not inspect.isabstract(moba::MobaSMSTrigger)


def test_moba::mobasmstrigger_constructor_exists():
    assert callable(moba::MobaSMSTrigger.__init__)


def test_moba::mobasmstrigger_constructor_args():
    sig = inspect.signature(moba::MobaSMSTrigger.__init__)
    params = list(sig.parameters.keys())



def test_moba::mobadevicestartuptrigger_is_not_abstract():
    assert not inspect.isabstract(moba::MobaDeviceStartupTrigger)


def test_moba::mobadevicestartuptrigger_constructor_exists():
    assert callable(moba::MobaDeviceStartupTrigger.__init__)


def test_moba::mobadevicestartuptrigger_constructor_args():
    sig = inspect.signature(moba::MobaDeviceStartupTrigger.__init__)
    params = list(sig.parameters.keys())



def test_moba::mobapushtrigger_is_not_abstract():
    assert not inspect.isabstract(moba::MobaPushTrigger)


def test_moba::mobapushtrigger_constructor_exists():
    assert callable(moba::MobaPushTrigger.__init__)


def test_moba::mobapushtrigger_constructor_args():
    sig = inspect.signature(moba::MobaPushTrigger.__init__)
    params = list(sig.parameters.keys())



def test_moba::mobaappinstalltrigger_is_not_abstract():
    assert not inspect.isabstract(moba::MobaAppInstallTrigger)


def test_moba::mobaappinstalltrigger_constructor_exists():
    assert callable(moba::MobaAppInstallTrigger.__init__)


def test_moba::mobaappinstalltrigger_constructor_args():
    sig = inspect.signature(moba::MobaAppInstallTrigger.__init__)
    params = list(sig.parameters.keys())



def test_mobaconstraint_is_not_abstract():
    assert not inspect.isabstract(MobaConstraint)


def test_mobaconstraint_constructor_exists():
    assert callable(MobaConstraint.__init__)


def test_mobaconstraint_constructor_args():
    sig = inspect.signature(MobaConstraint.__init__)
    params = list(sig.parameters.keys())



def test_moba::mobadigitsconstraint_is_not_abstract():
    assert not inspect.isabstract(moba::MobaDigitsConstraint)


def test_moba::mobadigitsconstraint_constructor_exists():
    assert callable(moba::MobaDigitsConstraint.__init__)


def test_moba::mobadigitsconstraint_constructor_args():
    sig = inspect.signature(moba::MobaDigitsConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "filterIntegerValue" in params, "Missing parameter 'filterIntegerValue'"
    assert "filterFractionValue" in params, "Missing parameter 'filterFractionValue'"

def test_moba::mobadigitsconstraint_has_filterIntegerValue():
    assert hasattr(moba::MobaDigitsConstraint, "filterIntegerValue")
    descriptor = None
    for klass in moba::MobaDigitsConstraint.__mro__:
        if "filterIntegerValue" in klass.__dict__:
            descriptor = klass.__dict__["filterIntegerValue"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobadigitsconstraint_has_filterFractionValue():
    assert hasattr(moba::MobaDigitsConstraint, "filterFractionValue")
    descriptor = None
    for klass in moba::MobaDigitsConstraint.__mro__:
        if "filterFractionValue" in klass.__dict__:
            descriptor = klass.__dict__["filterFractionValue"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobamaxlengthconstraint_is_not_abstract():
    assert not inspect.isabstract(moba::MobaMaxLengthConstraint)


def test_moba::mobamaxlengthconstraint_constructor_exists():
    assert callable(moba::MobaMaxLengthConstraint.__init__)


def test_moba::mobamaxlengthconstraint_constructor_args():
    sig = inspect.signature(moba::MobaMaxLengthConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "filterValue" in params, "Missing parameter 'filterValue'"

def test_moba::mobamaxlengthconstraint_has_filterValue():
    assert hasattr(moba::MobaMaxLengthConstraint, "filterValue")
    descriptor = None
    for klass in moba::MobaMaxLengthConstraint.__mro__:
        if "filterValue" in klass.__dict__:
            descriptor = klass.__dict__["filterValue"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobaregexpconstraint_is_not_abstract():
    assert not inspect.isabstract(moba::MobaRegexpConstraint)


def test_moba::mobaregexpconstraint_constructor_exists():
    assert callable(moba::MobaRegexpConstraint.__init__)


def test_moba::mobaregexpconstraint_constructor_args():
    sig = inspect.signature(moba::MobaRegexpConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "filterString" in params, "Missing parameter 'filterString'"

def test_moba::mobaregexpconstraint_has_filterString():
    assert hasattr(moba::MobaRegexpConstraint, "filterString")
    descriptor = None
    for klass in moba::MobaRegexpConstraint.__mro__:
        if "filterString" in klass.__dict__:
            descriptor = klass.__dict__["filterString"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobaconstraint_is_not_abstract():
    assert not inspect.isabstract(moba::MobaConstraint)


def test_moba::mobaconstraint_constructor_exists():
    assert callable(moba::MobaConstraint.__init__)


def test_moba::mobaconstraint_constructor_args():
    sig = inspect.signature(moba::MobaConstraint.__init__)
    params = list(sig.parameters.keys())



def test_moba::mobaconstraintable_is_not_abstract():
    assert not inspect.isabstract(moba::MobaConstraintable)


def test_moba::mobaconstraintable_constructor_exists():
    assert callable(moba::MobaConstraintable.__init__)


def test_moba::mobaconstraintable_constructor_args():
    sig = inspect.signature(moba::MobaConstraintable.__init__)
    params = list(sig.parameters.keys())



def test_mobaqueuefeature_is_not_abstract():
    assert not inspect.isabstract(MobaQueueFeature)


def test_mobaqueuefeature_constructor_exists():
    assert callable(MobaQueueFeature.__init__)


def test_mobaqueuefeature_constructor_args():
    sig = inspect.signature(MobaQueueFeature.__init__)
    params = list(sig.parameters.keys())



def test_moba::mobaqueuereference_is_not_abstract():
    assert not inspect.isabstract(moba::MobaQueueReference)


def test_moba::mobaqueuereference_constructor_exists():
    assert callable(moba::MobaQueueReference.__init__)


def test_moba::mobaqueuereference_constructor_args():
    sig = inspect.signature(moba::MobaQueueReference.__init__)
    params = list(sig.parameters.keys())



def test_moba::mobaminlengthconstraint_is_not_abstract():
    assert not inspect.isabstract(moba::MobaMinLengthConstraint)


def test_moba::mobaminlengthconstraint_constructor_exists():
    assert callable(moba::MobaMinLengthConstraint.__init__)


def test_moba::mobaminlengthconstraint_constructor_args():
    sig = inspect.signature(moba::MobaMinLengthConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "filterValue" in params, "Missing parameter 'filterValue'"

def test_moba::mobaminlengthconstraint_has_filterValue():
    assert hasattr(moba::MobaMinLengthConstraint, "filterValue")
    descriptor = None
    for klass in moba::MobaMinLengthConstraint.__mro__:
        if "filterValue" in klass.__dict__:
            descriptor = klass.__dict__["filterValue"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobanullconstraint_is_not_abstract():
    assert not inspect.isabstract(moba::MobaNullConstraint)


def test_moba::mobanullconstraint_constructor_exists():
    assert callable(moba::MobaNullConstraint.__init__)


def test_moba::mobanullconstraint_constructor_args():
    sig = inspect.signature(moba::MobaNullConstraint.__init__)
    params = list(sig.parameters.keys())



def test_moba::mobanotnullconstraint_is_not_abstract():
    assert not inspect.isabstract(moba::MobaNotNullConstraint)


def test_moba::mobanotnullconstraint_constructor_exists():
    assert callable(moba::MobaNotNullConstraint.__init__)


def test_moba::mobanotnullconstraint_constructor_args():
    sig = inspect.signature(moba::MobaNotNullConstraint.__init__)
    params = list(sig.parameters.keys())



def test_moba::mobapastconstraint_is_not_abstract():
    assert not inspect.isabstract(moba::MobaPastConstraint)


def test_moba::mobapastconstraint_constructor_exists():
    assert callable(moba::MobaPastConstraint.__init__)


def test_moba::mobapastconstraint_constructor_args():
    sig = inspect.signature(moba::MobaPastConstraint.__init__)
    params = list(sig.parameters.keys())



def test_moba::mobafutureconstraint_is_not_abstract():
    assert not inspect.isabstract(moba::MobaFutureConstraint)


def test_moba::mobafutureconstraint_constructor_exists():
    assert callable(moba::MobaFutureConstraint.__init__)


def test_moba::mobafutureconstraint_constructor_args():
    sig = inspect.signature(moba::MobaFutureConstraint.__init__)
    params = list(sig.parameters.keys())



def test_moba::mobamaxconstraint_is_not_abstract():
    assert not inspect.isabstract(moba::MobaMaxConstraint)


def test_moba::mobamaxconstraint_constructor_exists():
    assert callable(moba::MobaMaxConstraint.__init__)


def test_moba::mobamaxconstraint_constructor_args():
    sig = inspect.signature(moba::MobaMaxConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "filterValue" in params, "Missing parameter 'filterValue'"

def test_moba::mobamaxconstraint_has_filterValue():
    assert hasattr(moba::MobaMaxConstraint, "filterValue")
    descriptor = None
    for klass in moba::MobaMaxConstraint.__mro__:
        if "filterValue" in klass.__dict__:
            descriptor = klass.__dict__["filterValue"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobaminconstraint_is_not_abstract():
    assert not inspect.isabstract(moba::MobaMinConstraint)


def test_moba::mobaminconstraint_constructor_exists():
    assert callable(moba::MobaMinConstraint.__init__)


def test_moba::mobaminconstraint_constructor_args():
    sig = inspect.signature(moba::MobaMinConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "filterValue" in params, "Missing parameter 'filterValue'"

def test_moba::mobaminconstraint_has_filterValue():
    assert hasattr(moba::MobaMinConstraint, "filterValue")
    descriptor = None
    for klass in moba::MobaMinConstraint.__mro__:
        if "filterValue" in klass.__dict__:
            descriptor = klass.__dict__["filterValue"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobamuliplicity_is_not_abstract():
    assert not inspect.isabstract(moba::MobaMuliplicity)


def test_moba::mobamuliplicity_constructor_exists():
    assert callable(moba::MobaMuliplicity.__init__)


def test_moba::mobamuliplicity_constructor_args():
    sig = inspect.signature(moba::MobaMuliplicity.__init__)
    params = list(sig.parameters.keys())
    assert "upper" in params, "Missing parameter 'upper'"
    assert "lower" in params, "Missing parameter 'lower'"

def test_moba::mobamuliplicity_has_upper():
    assert hasattr(moba::MobaMuliplicity, "upper")
    descriptor = None
    for klass in moba::MobaMuliplicity.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobamuliplicity_has_lower():
    assert hasattr(moba::MobaMuliplicity, "lower")
    descriptor = None
    for klass in moba::MobaMuliplicity.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobamultiplicityable_is_not_abstract():
    assert not inspect.isabstract(moba::MobaMultiplicityAble)


def test_moba::mobamultiplicityable_constructor_exists():
    assert callable(moba::MobaMultiplicityAble.__init__)


def test_moba::mobamultiplicityable_constructor_args():
    sig = inspect.signature(moba::MobaMultiplicityAble.__init__)
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



def test_moba::mobarestdtoattribute_is_not_abstract():
    assert not inspect.isabstract(moba::MobaRESTDtoAttribute)


def test_moba::mobarestdtoattribute_constructor_exists():
    assert callable(moba::MobaRESTDtoAttribute.__init__)


def test_moba::mobarestdtoattribute_constructor_args():
    sig = inspect.signature(moba::MobaRESTDtoAttribute.__init__)
    params = list(sig.parameters.keys())



def test_moba::mobarestattribute_is_not_abstract():
    assert not inspect.isabstract(moba::MobaRESTAttribute)


def test_moba::mobarestattribute_constructor_exists():
    assert callable(moba::MobaRESTAttribute.__init__)


def test_moba::mobarestattribute_constructor_args():
    sig = inspect.signature(moba::MobaRESTAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "formatString" in params, "Missing parameter 'formatString'"
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"
    assert "keyString" in params, "Missing parameter 'keyString'"
    assert "valueInt" in params, "Missing parameter 'valueInt'"
    assert "valueDouble" in params, "Missing parameter 'valueDouble'"
    assert "valueString" in params, "Missing parameter 'valueString'"

def test_moba::mobarestattribute_has_formatString():
    assert hasattr(moba::MobaRESTAttribute, "formatString")
    descriptor = None
    for klass in moba::MobaRESTAttribute.__mro__:
        if "formatString" in klass.__dict__:
            descriptor = klass.__dict__["formatString"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobarestattribute_has_key():
    assert hasattr(moba::MobaRESTAttribute, "key")
    descriptor = None
    for klass in moba::MobaRESTAttribute.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobarestattribute_has_value():
    assert hasattr(moba::MobaRESTAttribute, "value")
    descriptor = None
    for klass in moba::MobaRESTAttribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobarestattribute_has_keyString():
    assert hasattr(moba::MobaRESTAttribute, "keyString")
    descriptor = None
    for klass in moba::MobaRESTAttribute.__mro__:
        if "keyString" in klass.__dict__:
            descriptor = klass.__dict__["keyString"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobarestattribute_has_valueInt():
    assert hasattr(moba::MobaRESTAttribute, "valueInt")
    descriptor = None
    for klass in moba::MobaRESTAttribute.__mro__:
        if "valueInt" in klass.__dict__:
            descriptor = klass.__dict__["valueInt"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobarestattribute_has_valueDouble():
    assert hasattr(moba::MobaRESTAttribute, "valueDouble")
    descriptor = None
    for klass in moba::MobaRESTAttribute.__mro__:
        if "valueDouble" in klass.__dict__:
            descriptor = klass.__dict__["valueDouble"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobarestattribute_has_valueString():
    assert hasattr(moba::MobaRESTAttribute, "valueString")
    descriptor = None
    for klass in moba::MobaRESTAttribute.__mro__:
        if "valueString" in klass.__dict__:
            descriptor = klass.__dict__["valueString"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobarestabstractattribute_is_not_abstract():
    assert not inspect.isabstract(moba::MobaRESTAbstractAttribute)


def test_moba::mobarestabstractattribute_constructor_exists():
    assert callable(moba::MobaRESTAbstractAttribute.__init__)


def test_moba::mobarestabstractattribute_constructor_args():
    sig = inspect.signature(moba::MobaRESTAbstractAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "attachment" in params, "Missing parameter 'attachment'"
    assert "alias" in params, "Missing parameter 'alias'"
    assert "aliasString" in params, "Missing parameter 'aliasString'"

def test_moba::mobarestabstractattribute_has_attachment():
    assert hasattr(moba::MobaRESTAbstractAttribute, "attachment")
    descriptor = None
    for klass in moba::MobaRESTAbstractAttribute.__mro__:
        if "attachment" in klass.__dict__:
            descriptor = klass.__dict__["attachment"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobarestabstractattribute_has_alias():
    assert hasattr(moba::MobaRESTAbstractAttribute, "alias")
    descriptor = None
    for klass in moba::MobaRESTAbstractAttribute.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobarestabstractattribute_has_aliasString():
    assert hasattr(moba::MobaRESTAbstractAttribute, "aliasString")
    descriptor = None
    for klass in moba::MobaRESTAbstractAttribute.__mro__:
        if "aliasString" in klass.__dict__:
            descriptor = klass.__dict__["aliasString"]
            break
    assert isinstance(descriptor, property)



def test_mobarest_is_not_abstract():
    assert not inspect.isabstract(MobaREST)


def test_mobarest_constructor_exists():
    assert callable(MobaREST.__init__)


def test_mobarest_constructor_args():
    sig = inspect.signature(MobaREST.__init__)
    params = list(sig.parameters.keys())



def test_moba::mobarestworkflow_is_not_abstract():
    assert not inspect.isabstract(moba::MobaRESTWorkflow)


def test_moba::mobarestworkflow_constructor_exists():
    assert callable(moba::MobaRESTWorkflow.__init__)


def test_moba::mobarestworkflow_constructor_args():
    sig = inspect.signature(moba::MobaRESTWorkflow.__init__)
    params = list(sig.parameters.keys())



def test_moba::mobarestcrud_is_not_abstract():
    assert not inspect.isabstract(moba::MobaRESTCrud)


def test_moba::mobarestcrud_constructor_exists():
    assert callable(moba::MobaRESTCrud.__init__)


def test_moba::mobarestcrud_constructor_args():
    sig = inspect.signature(moba::MobaRESTCrud.__init__)
    params = list(sig.parameters.keys())
    assert "operations" in params, "Missing parameter 'operations'"

def test_moba::mobarestcrud_has_operations():
    assert hasattr(moba::MobaRESTCrud, "operations")
    descriptor = None
    for klass in moba::MobaRESTCrud.__mro__:
        if "operations" in klass.__dict__:
            descriptor = klass.__dict__["operations"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobarestcustomservice_is_not_abstract():
    assert not inspect.isabstract(moba::MobaRESTCustomService)


def test_moba::mobarestcustomservice_constructor_exists():
    assert callable(moba::MobaRESTCustomService.__init__)


def test_moba::mobarestcustomservice_constructor_args():
    sig = inspect.signature(moba::MobaRESTCustomService.__init__)
    params = list(sig.parameters.keys())
    assert "operation" in params, "Missing parameter 'operation'"

def test_moba::mobarestcustomservice_has_operation():
    assert hasattr(moba::MobaRESTCustomService, "operation")
    descriptor = None
    for klass in moba::MobaRESTCustomService.__mro__:
        if "operation" in klass.__dict__:
            descriptor = klass.__dict__["operation"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobarestpayloaddefinition_is_not_abstract():
    assert not inspect.isabstract(moba::MobaRESTPayloadDefinition)


def test_moba::mobarestpayloaddefinition_constructor_exists():
    assert callable(moba::MobaRESTPayloadDefinition.__init__)


def test_moba::mobarestpayloaddefinition_constructor_args():
    sig = inspect.signature(moba::MobaRESTPayloadDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "array" in params, "Missing parameter 'array'"

def test_moba::mobarestpayloaddefinition_has_array():
    assert hasattr(moba::MobaRESTPayloadDefinition, "array")
    descriptor = None
    for klass in moba::MobaRESTPayloadDefinition.__mro__:
        if "array" in klass.__dict__:
            descriptor = klass.__dict__["array"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobaentityindex_is_not_abstract():
    assert not inspect.isabstract(moba::MobaEntityIndex)


def test_moba::mobaentityindex_constructor_exists():
    assert callable(moba::MobaEntityIndex.__init__)


def test_moba::mobaentityindex_constructor_args():
    sig = inspect.signature(moba::MobaEntityIndex.__init__)
    params = list(sig.parameters.keys())
    assert "unique" in params, "Missing parameter 'unique'"
    assert "name" in params, "Missing parameter 'name'"

def test_moba::mobaentityindex_has_unique():
    assert hasattr(moba::MobaEntityIndex, "unique")
    descriptor = None
    for klass in moba::MobaEntityIndex.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobaentityindex_has_name():
    assert hasattr(moba::MobaEntityIndex, "name")
    descriptor = None
    for klass in moba::MobaEntityIndex.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobarestheader_is_not_abstract():
    assert not inspect.isabstract(moba::MobaRESTHeader)


def test_moba::mobarestheader_constructor_exists():
    assert callable(moba::MobaRESTHeader.__init__)


def test_moba::mobarestheader_constructor_args():
    sig = inspect.signature(moba::MobaRESTHeader.__init__)
    params = list(sig.parameters.keys())
    assert "contentTypeHeader" in params, "Missing parameter 'contentTypeHeader'"
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"
    assert "keyString" in params, "Missing parameter 'keyString'"
    assert "rawHeader" in params, "Missing parameter 'rawHeader'"
    assert "valueString" in params, "Missing parameter 'valueString'"

def test_moba::mobarestheader_has_contentTypeHeader():
    assert hasattr(moba::MobaRESTHeader, "contentTypeHeader")
    descriptor = None
    for klass in moba::MobaRESTHeader.__mro__:
        if "contentTypeHeader" in klass.__dict__:
            descriptor = klass.__dict__["contentTypeHeader"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobarestheader_has_key():
    assert hasattr(moba::MobaRESTHeader, "key")
    descriptor = None
    for klass in moba::MobaRESTHeader.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobarestheader_has_value():
    assert hasattr(moba::MobaRESTHeader, "value")
    descriptor = None
    for klass in moba::MobaRESTHeader.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobarestheader_has_keyString():
    assert hasattr(moba::MobaRESTHeader, "keyString")
    descriptor = None
    for klass in moba::MobaRESTHeader.__mro__:
        if "keyString" in klass.__dict__:
            descriptor = klass.__dict__["keyString"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobarestheader_has_rawHeader():
    assert hasattr(moba::MobaRESTHeader, "rawHeader")
    descriptor = None
    for klass in moba::MobaRESTHeader.__mro__:
        if "rawHeader" in klass.__dict__:
            descriptor = klass.__dict__["rawHeader"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobarestheader_has_valueString():
    assert hasattr(moba::MobaRESTHeader, "valueString")
    descriptor = None
    for klass in moba::MobaRESTHeader.__mro__:
        if "valueString" in klass.__dict__:
            descriptor = klass.__dict__["valueString"]
            break
    assert isinstance(descriptor, property)



def test_mobamultiplicityable_is_not_abstract():
    assert not inspect.isabstract(MobaMultiplicityAble)


def test_mobamultiplicityable_constructor_exists():
    assert callable(MobaMultiplicityAble.__init__)


def test_mobamultiplicityable_constructor_args():
    sig = inspect.signature(MobaMultiplicityAble.__init__)
    params = list(sig.parameters.keys())



def test_moba::mobadtoembeddable_is_not_abstract():
    assert not inspect.isabstract(moba::MobaDtoEmbeddable)


def test_moba::mobadtoembeddable_constructor_exists():
    assert callable(moba::MobaDtoEmbeddable.__init__)


def test_moba::mobadtoembeddable_constructor_args():
    sig = inspect.signature(moba::MobaDtoEmbeddable.__init__)
    params = list(sig.parameters.keys())
    assert "transient" in params, "Missing parameter 'transient'"
    assert "alias" in params, "Missing parameter 'alias'"

def test_moba::mobadtoembeddable_has_transient():
    assert hasattr(moba::MobaDtoEmbeddable, "transient")
    descriptor = None
    for klass in moba::MobaDtoEmbeddable.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobadtoembeddable_has_alias():
    assert hasattr(moba::MobaDtoEmbeddable, "alias")
    descriptor = None
    for klass in moba::MobaDtoEmbeddable.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobaentityembeddable_is_not_abstract():
    assert not inspect.isabstract(moba::MobaEntityEmbeddable)


def test_moba::mobaentityembeddable_constructor_exists():
    assert callable(moba::MobaEntityEmbeddable.__init__)


def test_moba::mobaentityembeddable_constructor_args():
    sig = inspect.signature(moba::MobaEntityEmbeddable.__init__)
    params = list(sig.parameters.keys())
    assert "transient" in params, "Missing parameter 'transient'"

def test_moba::mobaentityembeddable_has_transient():
    assert hasattr(moba::MobaEntityEmbeddable, "transient")
    descriptor = None
    for klass in moba::MobaEntityEmbeddable.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobaentityreference_is_not_abstract():
    assert not inspect.isabstract(moba::MobaEntityReference)


def test_moba::mobaentityreference_constructor_exists():
    assert callable(moba::MobaEntityReference.__init__)


def test_moba::mobaentityreference_constructor_args():
    sig = inspect.signature(moba::MobaEntityReference.__init__)
    params = list(sig.parameters.keys())
    assert "lazy" in params, "Missing parameter 'lazy'"
    assert "cascading" in params, "Missing parameter 'cascading'"
    assert "transient" in params, "Missing parameter 'transient'"

def test_moba::mobaentityreference_has_lazy():
    assert hasattr(moba::MobaEntityReference, "lazy")
    descriptor = None
    for klass in moba::MobaEntityReference.__mro__:
        if "lazy" in klass.__dict__:
            descriptor = klass.__dict__["lazy"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobaentityreference_has_cascading():
    assert hasattr(moba::MobaEntityReference, "cascading")
    descriptor = None
    for klass in moba::MobaEntityReference.__mro__:
        if "cascading" in klass.__dict__:
            descriptor = klass.__dict__["cascading"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobaentityreference_has_transient():
    assert hasattr(moba::MobaEntityReference, "transient")
    descriptor = None
    for klass in moba::MobaEntityReference.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobadtoreference_is_not_abstract():
    assert not inspect.isabstract(moba::MobaDtoReference)


def test_moba::mobadtoreference_constructor_exists():
    assert callable(moba::MobaDtoReference.__init__)


def test_moba::mobadtoreference_constructor_args():
    sig = inspect.signature(moba::MobaDtoReference.__init__)
    params = list(sig.parameters.keys())
    assert "transient" in params, "Missing parameter 'transient'"
    assert "cascading" in params, "Missing parameter 'cascading'"
    assert "alias" in params, "Missing parameter 'alias'"
    assert "lazy" in params, "Missing parameter 'lazy'"

def test_moba::mobadtoreference_has_transient():
    assert hasattr(moba::MobaDtoReference, "transient")
    descriptor = None
    for klass in moba::MobaDtoReference.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobadtoreference_has_cascading():
    assert hasattr(moba::MobaDtoReference, "cascading")
    descriptor = None
    for klass in moba::MobaDtoReference.__mro__:
        if "cascading" in klass.__dict__:
            descriptor = klass.__dict__["cascading"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobadtoreference_has_alias():
    assert hasattr(moba::MobaDtoReference, "alias")
    descriptor = None
    for klass in moba::MobaDtoReference.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobadtoreference_has_lazy():
    assert hasattr(moba::MobaDtoReference, "lazy")
    descriptor = None
    for klass in moba::MobaDtoReference.__mro__:
        if "lazy" in klass.__dict__:
            descriptor = klass.__dict__["lazy"]
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



def test_moba::mobaentityfeature_is_not_abstract():
    assert not inspect.isabstract(moba::MobaEntityFeature)


def test_moba::mobaentityfeature_constructor_exists():
    assert callable(moba::MobaEntityFeature.__init__)


def test_moba::mobaentityfeature_constructor_args():
    sig = inspect.signature(moba::MobaEntityFeature.__init__)
    params = list(sig.parameters.keys())



def test_moba::mobadtofeature_is_not_abstract():
    assert not inspect.isabstract(moba::MobaDtoFeature)


def test_moba::mobadtofeature_constructor_exists():
    assert callable(moba::MobaDtoFeature.__init__)


def test_moba::mobadtofeature_constructor_args():
    sig = inspect.signature(moba::MobaDtoFeature.__init__)
    params = list(sig.parameters.keys())



def test_moba::mobaqueuefeature_is_not_abstract():
    assert not inspect.isabstract(moba::MobaQueueFeature)


def test_moba::mobaqueuefeature_constructor_exists():
    assert callable(moba::MobaQueueFeature.__init__)


def test_moba::mobaqueuefeature_constructor_args():
    sig = inspect.signature(moba::MobaQueueFeature.__init__)
    params = list(sig.parameters.keys())



def test_moba::mobasettingsfeature_is_not_abstract():
    assert not inspect.isabstract(moba::MobaSettingsFeature)


def test_moba::mobasettingsfeature_constructor_exists():
    assert callable(moba::MobaSettingsFeature.__init__)


def test_moba::mobasettingsfeature_constructor_args():
    sig = inspect.signature(moba::MobaSettingsFeature.__init__)
    params = list(sig.parameters.keys())



def test_mobadata_is_not_abstract():
    assert not inspect.isabstract(MobaData)


def test_mobadata_constructor_exists():
    assert callable(MobaData.__init__)


def test_mobadata_constructor_args():
    sig = inspect.signature(MobaData.__init__)
    params = list(sig.parameters.keys())



def test_moba::mobaqueue_is_not_abstract():
    assert not inspect.isabstract(moba::MobaQueue)


def test_moba::mobaqueue_constructor_exists():
    assert callable(moba::MobaQueue.__init__)


def test_moba::mobaqueue_constructor_args():
    sig = inspect.signature(moba::MobaQueue.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_moba::mobaqueue_has_name():
    assert hasattr(moba::MobaQueue, "name")
    descriptor = None
    for klass in moba::MobaQueue.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobadto_is_not_abstract():
    assert not inspect.isabstract(moba::MobaDto)


def test_moba::mobadto_constructor_exists():
    assert callable(moba::MobaDto.__init__)


def test_moba::mobadto_constructor_args():
    sig = inspect.signature(moba::MobaDto.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_moba::mobadto_has_name():
    assert hasattr(moba::MobaDto, "name")
    descriptor = None
    for klass in moba::MobaDto.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobaentity_is_not_abstract():
    assert not inspect.isabstract(moba::MobaEntity)


def test_moba::mobaentity_constructor_exists():
    assert callable(moba::MobaEntity.__init__)


def test_moba::mobaentity_constructor_args():
    sig = inspect.signature(moba::MobaEntity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_moba::mobaentity_has_name():
    assert hasattr(moba::MobaEntity, "name")
    descriptor = None
    for klass in moba::MobaEntity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobaconstantvalue_is_not_abstract():
    assert not inspect.isabstract(moba::MobaConstantValue)


def test_moba::mobaconstantvalue_constructor_exists():
    assert callable(moba::MobaConstantValue.__init__)


def test_moba::mobaconstantvalue_constructor_args():
    sig = inspect.signature(moba::MobaConstantValue.__init__)
    params = list(sig.parameters.keys())
    assert "valueConstFunctions" in params, "Missing parameter 'valueConstFunctions'"
    assert "valueDouble" in params, "Missing parameter 'valueDouble'"
    assert "valueConstToLowerCase" in params, "Missing parameter 'valueConstToLowerCase'"
    assert "valueInt" in params, "Missing parameter 'valueInt'"
    assert "valueString" in params, "Missing parameter 'valueString'"

def test_moba::mobaconstantvalue_has_valueConstFunctions():
    assert hasattr(moba::MobaConstantValue, "valueConstFunctions")
    descriptor = None
    for klass in moba::MobaConstantValue.__mro__:
        if "valueConstFunctions" in klass.__dict__:
            descriptor = klass.__dict__["valueConstFunctions"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobaconstantvalue_has_valueDouble():
    assert hasattr(moba::MobaConstantValue, "valueDouble")
    descriptor = None
    for klass in moba::MobaConstantValue.__mro__:
        if "valueDouble" in klass.__dict__:
            descriptor = klass.__dict__["valueDouble"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobaconstantvalue_has_valueConstToLowerCase():
    assert hasattr(moba::MobaConstantValue, "valueConstToLowerCase")
    descriptor = None
    for klass in moba::MobaConstantValue.__mro__:
        if "valueConstToLowerCase" in klass.__dict__:
            descriptor = klass.__dict__["valueConstToLowerCase"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobaconstantvalue_has_valueInt():
    assert hasattr(moba::MobaConstantValue, "valueInt")
    descriptor = None
    for klass in moba::MobaConstantValue.__mro__:
        if "valueInt" in klass.__dict__:
            descriptor = klass.__dict__["valueInt"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobaconstantvalue_has_valueString():
    assert hasattr(moba::MobaConstantValue, "valueString")
    descriptor = None
    for klass in moba::MobaConstantValue.__mro__:
        if "valueString" in klass.__dict__:
            descriptor = klass.__dict__["valueString"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobaproperty_is_not_abstract():
    assert not inspect.isabstract(moba::MobaProperty)


def test_moba::mobaproperty_constructor_exists():
    assert callable(moba::MobaProperty.__init__)


def test_moba::mobaproperty_constructor_args():
    sig = inspect.signature(moba::MobaProperty.__init__)
    params = list(sig.parameters.keys())
    assert "valueString" in params, "Missing parameter 'valueString'"
    assert "keyString" in params, "Missing parameter 'keyString'"
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_moba::mobaproperty_has_valueString():
    assert hasattr(moba::MobaProperty, "valueString")
    descriptor = None
    for klass in moba::MobaProperty.__mro__:
        if "valueString" in klass.__dict__:
            descriptor = klass.__dict__["valueString"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobaproperty_has_keyString():
    assert hasattr(moba::MobaProperty, "keyString")
    descriptor = None
    for klass in moba::MobaProperty.__mro__:
        if "keyString" in klass.__dict__:
            descriptor = klass.__dict__["keyString"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobaproperty_has_value():
    assert hasattr(moba::MobaProperty, "value")
    descriptor = None
    for klass in moba::MobaProperty.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobaproperty_has_key():
    assert hasattr(moba::MobaProperty, "key")
    descriptor = None
    for klass in moba::MobaProperty.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobapropertiesable_is_not_abstract():
    assert not inspect.isabstract(moba::MobaPropertiesAble)


def test_moba::mobapropertiesable_constructor_exists():
    assert callable(moba::MobaPropertiesAble.__init__)


def test_moba::mobapropertiesable_constructor_args():
    sig = inspect.signature(moba::MobaPropertiesAble.__init__)
    params = list(sig.parameters.keys())



def test_moba::mobageneratorfeature_is_not_abstract():
    assert not inspect.isabstract(moba::MobaGeneratorFeature)


def test_moba::mobageneratorfeature_constructor_exists():
    assert callable(moba::MobaGeneratorFeature.__init__)


def test_moba::mobageneratorfeature_constructor_args():
    sig = inspect.signature(moba::MobaGeneratorFeature.__init__)
    params = list(sig.parameters.keys())



def test_mobaapplicationfeature_is_not_abstract():
    assert not inspect.isabstract(MobaApplicationFeature)


def test_mobaapplicationfeature_constructor_exists():
    assert callable(MobaApplicationFeature.__init__)


def test_mobaapplicationfeature_constructor_args():
    sig = inspect.signature(MobaApplicationFeature.__init__)
    params = list(sig.parameters.keys())



def test_moba::mobasettings_is_not_abstract():
    assert not inspect.isabstract(moba::MobaSettings)


def test_moba::mobasettings_constructor_exists():
    assert callable(moba::MobaSettings.__init__)


def test_moba::mobasettings_constructor_args():
    sig = inspect.signature(moba::MobaSettings.__init__)
    params = list(sig.parameters.keys())
    assert "active" in params, "Missing parameter 'active'"
    assert "name" in params, "Missing parameter 'name'"

def test_moba::mobasettings_has_active():
    assert hasattr(moba::MobaSettings, "active")
    descriptor = None
    for klass in moba::MobaSettings.__mro__:
        if "active" in klass.__dict__:
            descriptor = klass.__dict__["active"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobasettings_has_name():
    assert hasattr(moba::MobaSettings, "name")
    descriptor = None
    for klass in moba::MobaSettings.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobatransportserializationtype_is_not_abstract():
    assert not inspect.isabstract(moba::MobaTransportSerializationType)


def test_moba::mobatransportserializationtype_constructor_exists():
    assert callable(moba::MobaTransportSerializationType.__init__)


def test_moba::mobatransportserializationtype_constructor_args():
    sig = inspect.signature(moba::MobaTransportSerializationType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_moba::mobatransportserializationtype_has_name():
    assert hasattr(moba::MobaTransportSerializationType, "name")
    descriptor = None
    for klass in moba::MobaTransportSerializationType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobagenerator_is_not_abstract():
    assert not inspect.isabstract(moba::MobaGenerator)


def test_moba::mobagenerator_constructor_exists():
    assert callable(moba::MobaGenerator.__init__)


def test_moba::mobagenerator_constructor_args():
    sig = inspect.signature(moba::MobaGenerator.__init__)
    params = list(sig.parameters.keys())
    assert "active" in params, "Missing parameter 'active'"
    assert "name" in params, "Missing parameter 'name'"

def test_moba::mobagenerator_has_active():
    assert hasattr(moba::MobaGenerator, "active")
    descriptor = None
    for klass in moba::MobaGenerator.__mro__:
        if "active" in klass.__dict__:
            descriptor = klass.__dict__["active"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobagenerator_has_name():
    assert hasattr(moba::MobaGenerator, "name")
    descriptor = None
    for klass in moba::MobaGenerator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobaserver_is_not_abstract():
    assert not inspect.isabstract(moba::MobaServer)


def test_moba::mobaserver_constructor_exists():
    assert callable(moba::MobaServer.__init__)


def test_moba::mobaserver_constructor_args():
    sig = inspect.signature(moba::MobaServer.__init__)
    params = list(sig.parameters.keys())
    assert "urlString" in params, "Missing parameter 'urlString'"
    assert "name" in params, "Missing parameter 'name'"

def test_moba::mobaserver_has_urlString():
    assert hasattr(moba::MobaServer, "urlString")
    descriptor = None
    for klass in moba::MobaServer.__mro__:
        if "urlString" in klass.__dict__:
            descriptor = klass.__dict__["urlString"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobaserver_has_name():
    assert hasattr(moba::MobaServer, "name")
    descriptor = None
    for klass in moba::MobaServer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobadata_is_not_abstract():
    assert not inspect.isabstract(moba::MobaData)


def test_moba::mobadata_constructor_exists():
    assert callable(moba::MobaData.__init__)


def test_moba::mobadata_constructor_args():
    sig = inspect.signature(moba::MobaData.__init__)
    params = list(sig.parameters.keys())



def test_moba::mobaenum_is_not_abstract():
    assert not inspect.isabstract(moba::MobaEnum)


def test_moba::mobaenum_constructor_exists():
    assert callable(moba::MobaEnum.__init__)


def test_moba::mobaenum_constructor_args():
    sig = inspect.signature(moba::MobaEnum.__init__)
    params = list(sig.parameters.keys())



def test_moba::mobaauthorization_is_not_abstract():
    assert not inspect.isabstract(moba::MobaAuthorization)


def test_moba::mobaauthorization_constructor_exists():
    assert callable(moba::MobaAuthorization.__init__)


def test_moba::mobaauthorization_constructor_args():
    sig = inspect.signature(moba::MobaAuthorization.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_moba::mobaauthorization_has_name():
    assert hasattr(moba::MobaAuthorization, "name")
    descriptor = None
    for klass in moba::MobaAuthorization.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobaconstant_is_not_abstract():
    assert not inspect.isabstract(moba::MobaConstant)


def test_moba::mobaconstant_constructor_exists():
    assert callable(moba::MobaConstant.__init__)


def test_moba::mobaconstant_constructor_args():
    sig = inspect.signature(moba::MobaConstant.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_moba::mobaconstant_has_name():
    assert hasattr(moba::MobaConstant, "name")
    descriptor = None
    for klass in moba::MobaConstant.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobatrigger_is_not_abstract():
    assert not inspect.isabstract(moba::MobaTrigger)


def test_moba::mobatrigger_constructor_exists():
    assert callable(moba::MobaTrigger.__init__)


def test_moba::mobatrigger_constructor_args():
    sig = inspect.signature(moba::MobaTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_moba::mobatrigger_has_name():
    assert hasattr(moba::MobaTrigger, "name")
    descriptor = None
    for klass in moba::MobaTrigger.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobaexternalmodule_is_not_abstract():
    assert not inspect.isabstract(moba::MobaExternalModule)


def test_moba::mobaexternalmodule_constructor_exists():
    assert callable(moba::MobaExternalModule.__init__)


def test_moba::mobaexternalmodule_constructor_args():
    sig = inspect.signature(moba::MobaExternalModule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_moba::mobaexternalmodule_has_name():
    assert hasattr(moba::MobaExternalModule, "name")
    descriptor = None
    for klass in moba::MobaExternalModule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobapersistencetype_is_not_abstract():
    assert not inspect.isabstract(moba::MobaPersistenceType)


def test_moba::mobapersistencetype_constructor_exists():
    assert callable(moba::MobaPersistenceType.__init__)


def test_moba::mobapersistencetype_constructor_args():
    sig = inspect.signature(moba::MobaPersistenceType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_moba::mobapersistencetype_has_name():
    assert hasattr(moba::MobaPersistenceType, "name")
    descriptor = None
    for klass in moba::MobaPersistenceType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobarest_is_not_abstract():
    assert not inspect.isabstract(moba::MobaREST)


def test_moba::mobarest_constructor_exists():
    assert callable(moba::MobaREST.__init__)


def test_moba::mobarest_constructor_args():
    sig = inspect.signature(moba::MobaREST.__init__)
    params = list(sig.parameters.keys())
    assert "bigData" in params, "Missing parameter 'bigData'"
    assert "url" in params, "Missing parameter 'url'"
    assert "path" in params, "Missing parameter 'path'"
    assert "name" in params, "Missing parameter 'name'"

def test_moba::mobarest_has_bigData():
    assert hasattr(moba::MobaREST, "bigData")
    descriptor = None
    for klass in moba::MobaREST.__mro__:
        if "bigData" in klass.__dict__:
            descriptor = klass.__dict__["bigData"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobarest_has_url():
    assert hasattr(moba::MobaREST, "url")
    descriptor = None
    for klass in moba::MobaREST.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobarest_has_path():
    assert hasattr(moba::MobaREST, "path")
    descriptor = None
    for klass in moba::MobaREST.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobarest_has_name():
    assert hasattr(moba::MobaREST, "name")
    descriptor = None
    for klass in moba::MobaREST.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobatemplate_is_not_abstract():
    assert not inspect.isabstract(moba::MobaTemplate)


def test_moba::mobatemplate_constructor_exists():
    assert callable(moba::MobaTemplate.__init__)


def test_moba::mobatemplate_constructor_args():
    sig = inspect.signature(moba::MobaTemplate.__init__)
    params = list(sig.parameters.keys())
    assert "downloadTemplate" in params, "Missing parameter 'downloadTemplate'"

def test_moba::mobatemplate_has_downloadTemplate():
    assert hasattr(moba::MobaTemplate, "downloadTemplate")
    descriptor = None
    for klass in moba::MobaTemplate.__mro__:
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



def test_moba::mobaentityattribute_is_not_abstract():
    assert not inspect.isabstract(moba::MobaEntityAttribute)


def test_moba::mobaentityattribute_constructor_exists():
    assert callable(moba::MobaEntityAttribute.__init__)


def test_moba::mobaentityattribute_constructor_args():
    sig = inspect.signature(moba::MobaEntityAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "formatString" in params, "Missing parameter 'formatString'"
    assert "domainKey" in params, "Missing parameter 'domainKey'"
    assert "transient" in params, "Missing parameter 'transient'"
    assert "lazy" in params, "Missing parameter 'lazy'"
    assert "domainDescription" in params, "Missing parameter 'domainDescription'"

def test_moba::mobaentityattribute_has_formatString():
    assert hasattr(moba::MobaEntityAttribute, "formatString")
    descriptor = None
    for klass in moba::MobaEntityAttribute.__mro__:
        if "formatString" in klass.__dict__:
            descriptor = klass.__dict__["formatString"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobaentityattribute_has_domainKey():
    assert hasattr(moba::MobaEntityAttribute, "domainKey")
    descriptor = None
    for klass in moba::MobaEntityAttribute.__mro__:
        if "domainKey" in klass.__dict__:
            descriptor = klass.__dict__["domainKey"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobaentityattribute_has_transient():
    assert hasattr(moba::MobaEntityAttribute, "transient")
    descriptor = None
    for klass in moba::MobaEntityAttribute.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobaentityattribute_has_lazy():
    assert hasattr(moba::MobaEntityAttribute, "lazy")
    descriptor = None
    for klass in moba::MobaEntityAttribute.__mro__:
        if "lazy" in klass.__dict__:
            descriptor = klass.__dict__["lazy"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobaentityattribute_has_domainDescription():
    assert hasattr(moba::MobaEntityAttribute, "domainDescription")
    descriptor = None
    for klass in moba::MobaEntityAttribute.__mro__:
        if "domainDescription" in klass.__dict__:
            descriptor = klass.__dict__["domainDescription"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobasettingsattribute_is_not_abstract():
    assert not inspect.isabstract(moba::MobaSettingsAttribute)


def test_moba::mobasettingsattribute_constructor_exists():
    assert callable(moba::MobaSettingsAttribute.__init__)


def test_moba::mobasettingsattribute_constructor_args():
    sig = inspect.signature(moba::MobaSettingsAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "formatString" in params, "Missing parameter 'formatString'"
    assert "domainDescription" in params, "Missing parameter 'domainDescription'"
    assert "lazy" in params, "Missing parameter 'lazy'"
    assert "transient" in params, "Missing parameter 'transient'"
    assert "domainKey" in params, "Missing parameter 'domainKey'"

def test_moba::mobasettingsattribute_has_formatString():
    assert hasattr(moba::MobaSettingsAttribute, "formatString")
    descriptor = None
    for klass in moba::MobaSettingsAttribute.__mro__:
        if "formatString" in klass.__dict__:
            descriptor = klass.__dict__["formatString"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobasettingsattribute_has_domainDescription():
    assert hasattr(moba::MobaSettingsAttribute, "domainDescription")
    descriptor = None
    for klass in moba::MobaSettingsAttribute.__mro__:
        if "domainDescription" in klass.__dict__:
            descriptor = klass.__dict__["domainDescription"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobasettingsattribute_has_lazy():
    assert hasattr(moba::MobaSettingsAttribute, "lazy")
    descriptor = None
    for klass in moba::MobaSettingsAttribute.__mro__:
        if "lazy" in klass.__dict__:
            descriptor = klass.__dict__["lazy"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobasettingsattribute_has_transient():
    assert hasattr(moba::MobaSettingsAttribute, "transient")
    descriptor = None
    for klass in moba::MobaSettingsAttribute.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobasettingsattribute_has_domainKey():
    assert hasattr(moba::MobaSettingsAttribute, "domainKey")
    descriptor = None
    for klass in moba::MobaSettingsAttribute.__mro__:
        if "domainKey" in klass.__dict__:
            descriptor = klass.__dict__["domainKey"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobadtoattribute_is_not_abstract():
    assert not inspect.isabstract(moba::MobaDtoAttribute)


def test_moba::mobadtoattribute_constructor_exists():
    assert callable(moba::MobaDtoAttribute.__init__)


def test_moba::mobadtoattribute_constructor_args():
    sig = inspect.signature(moba::MobaDtoAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"
    assert "domainDescription" in params, "Missing parameter 'domainDescription'"
    assert "lazy" in params, "Missing parameter 'lazy'"
    assert "domainKey" in params, "Missing parameter 'domainKey'"
    assert "transient" in params, "Missing parameter 'transient'"
    assert "formatString" in params, "Missing parameter 'formatString'"

def test_moba::mobadtoattribute_has_alias():
    assert hasattr(moba::MobaDtoAttribute, "alias")
    descriptor = None
    for klass in moba::MobaDtoAttribute.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobadtoattribute_has_domainDescription():
    assert hasattr(moba::MobaDtoAttribute, "domainDescription")
    descriptor = None
    for klass in moba::MobaDtoAttribute.__mro__:
        if "domainDescription" in klass.__dict__:
            descriptor = klass.__dict__["domainDescription"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobadtoattribute_has_lazy():
    assert hasattr(moba::MobaDtoAttribute, "lazy")
    descriptor = None
    for klass in moba::MobaDtoAttribute.__mro__:
        if "lazy" in klass.__dict__:
            descriptor = klass.__dict__["lazy"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobadtoattribute_has_domainKey():
    assert hasattr(moba::MobaDtoAttribute, "domainKey")
    descriptor = None
    for klass in moba::MobaDtoAttribute.__mro__:
        if "domainKey" in klass.__dict__:
            descriptor = klass.__dict__["domainKey"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobadtoattribute_has_transient():
    assert hasattr(moba::MobaDtoAttribute, "transient")
    descriptor = None
    for klass in moba::MobaDtoAttribute.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobadtoattribute_has_formatString():
    assert hasattr(moba::MobaDtoAttribute, "formatString")
    descriptor = None
    for klass in moba::MobaDtoAttribute.__mro__:
        if "formatString" in klass.__dict__:
            descriptor = klass.__dict__["formatString"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobasettingsentityreference_is_not_abstract():
    assert not inspect.isabstract(moba::MobaSettingsEntityReference)


def test_moba::mobasettingsentityreference_constructor_exists():
    assert callable(moba::MobaSettingsEntityReference.__init__)


def test_moba::mobasettingsentityreference_constructor_args():
    sig = inspect.signature(moba::MobaSettingsEntityReference.__init__)
    params = list(sig.parameters.keys())
    assert "lazy" in params, "Missing parameter 'lazy'"
    assert "transient" in params, "Missing parameter 'transient'"
    assert "cascading" in params, "Missing parameter 'cascading'"

def test_moba::mobasettingsentityreference_has_lazy():
    assert hasattr(moba::MobaSettingsEntityReference, "lazy")
    descriptor = None
    for klass in moba::MobaSettingsEntityReference.__mro__:
        if "lazy" in klass.__dict__:
            descriptor = klass.__dict__["lazy"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobasettingsentityreference_has_transient():
    assert hasattr(moba::MobaSettingsEntityReference, "transient")
    descriptor = None
    for klass in moba::MobaSettingsEntityReference.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobasettingsentityreference_has_cascading():
    assert hasattr(moba::MobaSettingsEntityReference, "cascading")
    descriptor = None
    for klass in moba::MobaSettingsEntityReference.__mro__:
        if "cascading" in klass.__dict__:
            descriptor = klass.__dict__["cascading"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobadatatype_is_not_abstract():
    assert not inspect.isabstract(moba::MobaDataType)


def test_moba::mobadatatype_constructor_exists():
    assert callable(moba::MobaDataType.__init__)


def test_moba::mobadatatype_constructor_args():
    sig = inspect.signature(moba::MobaDataType.__init__)
    params = list(sig.parameters.keys())
    assert "primitive" in params, "Missing parameter 'primitive'"
    assert "string" in params, "Missing parameter 'string'"
    assert "timestamp" in params, "Missing parameter 'timestamp'"
    assert "name" in params, "Missing parameter 'name'"
    assert "bool" in params, "Missing parameter 'bool'"
    assert "numeric" in params, "Missing parameter 'numeric'"
    assert "decimal" in params, "Missing parameter 'decimal'"
    assert "time" in params, "Missing parameter 'time'"
    assert "array" in params, "Missing parameter 'array'"
    assert "dateFormatString" in params, "Missing parameter 'dateFormatString'"
    assert "date" in params, "Missing parameter 'date'"
    assert "predefined" in params, "Missing parameter 'predefined'"

def test_moba::mobadatatype_has_primitive():
    assert hasattr(moba::MobaDataType, "primitive")
    descriptor = None
    for klass in moba::MobaDataType.__mro__:
        if "primitive" in klass.__dict__:
            descriptor = klass.__dict__["primitive"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobadatatype_has_string():
    assert hasattr(moba::MobaDataType, "string")
    descriptor = None
    for klass in moba::MobaDataType.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobadatatype_has_timestamp():
    assert hasattr(moba::MobaDataType, "timestamp")
    descriptor = None
    for klass in moba::MobaDataType.__mro__:
        if "timestamp" in klass.__dict__:
            descriptor = klass.__dict__["timestamp"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobadatatype_has_name():
    assert hasattr(moba::MobaDataType, "name")
    descriptor = None
    for klass in moba::MobaDataType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobadatatype_has_bool():
    assert hasattr(moba::MobaDataType, "bool")
    descriptor = None
    for klass in moba::MobaDataType.__mro__:
        if "bool" in klass.__dict__:
            descriptor = klass.__dict__["bool"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobadatatype_has_numeric():
    assert hasattr(moba::MobaDataType, "numeric")
    descriptor = None
    for klass in moba::MobaDataType.__mro__:
        if "numeric" in klass.__dict__:
            descriptor = klass.__dict__["numeric"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobadatatype_has_decimal():
    assert hasattr(moba::MobaDataType, "decimal")
    descriptor = None
    for klass in moba::MobaDataType.__mro__:
        if "decimal" in klass.__dict__:
            descriptor = klass.__dict__["decimal"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobadatatype_has_time():
    assert hasattr(moba::MobaDataType, "time")
    descriptor = None
    for klass in moba::MobaDataType.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobadatatype_has_array():
    assert hasattr(moba::MobaDataType, "array")
    descriptor = None
    for klass in moba::MobaDataType.__mro__:
        if "array" in klass.__dict__:
            descriptor = klass.__dict__["array"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobadatatype_has_dateFormatString():
    assert hasattr(moba::MobaDataType, "dateFormatString")
    descriptor = None
    for klass in moba::MobaDataType.__mro__:
        if "dateFormatString" in klass.__dict__:
            descriptor = klass.__dict__["dateFormatString"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobadatatype_has_date():
    assert hasattr(moba::MobaDataType, "date")
    descriptor = None
    for klass in moba::MobaDataType.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobadatatype_has_predefined():
    assert hasattr(moba::MobaDataType, "predefined")
    descriptor = None
    for klass in moba::MobaDataType.__mro__:
        if "predefined" in klass.__dict__:
            descriptor = klass.__dict__["predefined"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobageneratorslot_is_not_abstract():
    assert not inspect.isabstract(moba::MobaGeneratorSlot)


def test_moba::mobageneratorslot_constructor_exists():
    assert callable(moba::MobaGeneratorSlot.__init__)


def test_moba::mobageneratorslot_constructor_args():
    sig = inspect.signature(moba::MobaGeneratorSlot.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_moba::mobageneratorslot_has_name():
    assert hasattr(moba::MobaGeneratorSlot, "name")
    descriptor = None
    for klass in moba::MobaGeneratorSlot.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobageneratorslot_has_type():
    assert hasattr(moba::MobaGeneratorSlot, "type")
    descriptor = None
    for klass in moba::MobaGeneratorSlot.__mro__:
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



def test_moba::mobageneratoridfeature_is_not_abstract():
    assert not inspect.isabstract(moba::MobaGeneratorIDFeature)


def test_moba::mobageneratoridfeature_constructor_exists():
    assert callable(moba::MobaGeneratorIDFeature.__init__)


def test_moba::mobageneratoridfeature_constructor_args():
    sig = inspect.signature(moba::MobaGeneratorIDFeature.__init__)
    params = list(sig.parameters.keys())
    assert "generatorId" in params, "Missing parameter 'generatorId'"
    assert "generatorVersion" in params, "Missing parameter 'generatorVersion'"

def test_moba::mobageneratoridfeature_has_generatorId():
    assert hasattr(moba::MobaGeneratorIDFeature, "generatorId")
    descriptor = None
    for klass in moba::MobaGeneratorIDFeature.__mro__:
        if "generatorId" in klass.__dict__:
            descriptor = klass.__dict__["generatorId"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobageneratoridfeature_has_generatorVersion():
    assert hasattr(moba::MobaGeneratorIDFeature, "generatorVersion")
    descriptor = None
    for klass in moba::MobaGeneratorIDFeature.__mro__:
        if "generatorVersion" in klass.__dict__:
            descriptor = klass.__dict__["generatorVersion"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobageneratormixinfeature_is_not_abstract():
    assert not inspect.isabstract(moba::MobaGeneratorMixinFeature)


def test_moba::mobageneratormixinfeature_constructor_exists():
    assert callable(moba::MobaGeneratorMixinFeature.__init__)


def test_moba::mobageneratormixinfeature_constructor_args():
    sig = inspect.signature(moba::MobaGeneratorMixinFeature.__init__)
    params = list(sig.parameters.keys())



def test_mobafriendsable_is_not_abstract():
    assert not inspect.isabstract(MobaFriendsAble)


def test_mobafriendsable_constructor_exists():
    assert callable(MobaFriendsAble.__init__)


def test_mobafriendsable_constructor_args():
    sig = inspect.signature(MobaFriendsAble.__init__)
    params = list(sig.parameters.keys())



def test_moba::mobaapplicationfeature_is_not_abstract():
    assert not inspect.isabstract(moba::MobaApplicationFeature)


def test_moba::mobaapplicationfeature_constructor_exists():
    assert callable(moba::MobaApplicationFeature.__init__)


def test_moba::mobaapplicationfeature_constructor_args():
    sig = inspect.signature(moba::MobaApplicationFeature.__init__)
    params = list(sig.parameters.keys())



def test_moba::mobafeature_is_not_abstract():
    assert not inspect.isabstract(moba::MobaFeature)


def test_moba::mobafeature_constructor_exists():
    assert callable(moba::MobaFeature.__init__)


def test_moba::mobafeature_constructor_args():
    sig = inspect.signature(moba::MobaFeature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_moba::mobafeature_has_name():
    assert hasattr(moba::MobaFeature, "name")
    descriptor = None
    for klass in moba::MobaFeature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobamodel_is_not_abstract():
    assert not inspect.isabstract(moba::MobaModel)


def test_moba::mobamodel_constructor_exists():
    assert callable(moba::MobaModel.__init__)


def test_moba::mobamodel_constructor_args():
    sig = inspect.signature(moba::MobaModel.__init__)
    params = list(sig.parameters.keys())
    assert "copyright" in params, "Missing parameter 'copyright'"

def test_moba::mobamodel_has_copyright():
    assert hasattr(moba::MobaModel, "copyright")
    descriptor = None
    for klass in moba::MobaModel.__mro__:
        if "copyright" in klass.__dict__:
            descriptor = klass.__dict__["copyright"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobacache_is_not_abstract():
    assert not inspect.isabstract(moba::MobaCache)


def test_moba::mobacache_constructor_exists():
    assert callable(moba::MobaCache.__init__)


def test_moba::mobacache_constructor_args():
    sig = inspect.signature(moba::MobaCache.__init__)
    params = list(sig.parameters.keys())
    assert "cacheIntervalInt" in params, "Missing parameter 'cacheIntervalInt'"
    assert "cacheStrategyString" in params, "Missing parameter 'cacheStrategyString'"
    assert "name" in params, "Missing parameter 'name'"
    assert "cacheTypeString" in params, "Missing parameter 'cacheTypeString'"

def test_moba::mobacache_has_cacheIntervalInt():
    assert hasattr(moba::MobaCache, "cacheIntervalInt")
    descriptor = None
    for klass in moba::MobaCache.__mro__:
        if "cacheIntervalInt" in klass.__dict__:
            descriptor = klass.__dict__["cacheIntervalInt"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobacache_has_cacheStrategyString():
    assert hasattr(moba::MobaCache, "cacheStrategyString")
    descriptor = None
    for klass in moba::MobaCache.__mro__:
        if "cacheStrategyString" in klass.__dict__:
            descriptor = klass.__dict__["cacheStrategyString"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobacache_has_name():
    assert hasattr(moba::MobaCache, "name")
    descriptor = None
    for klass in moba::MobaCache.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobacache_has_cacheTypeString():
    assert hasattr(moba::MobaCache, "cacheTypeString")
    descriptor = None
    for klass in moba::MobaCache.__mro__:
        if "cacheTypeString" in klass.__dict__:
            descriptor = klass.__dict__["cacheTypeString"]
            break
    assert isinstance(descriptor, property)



def test_mobamodelfeature_is_not_abstract():
    assert not inspect.isabstract(MobaModelFeature)


def test_mobamodelfeature_constructor_exists():
    assert callable(MobaModelFeature.__init__)


def test_mobamodelfeature_constructor_args():
    sig = inspect.signature(MobaModelFeature.__init__)
    params = list(sig.parameters.keys())



def test_moba::mobaapplication_is_not_abstract():
    assert not inspect.isabstract(moba::MobaApplication)


def test_moba::mobaapplication_constructor_exists():
    assert callable(moba::MobaApplication.__init__)


def test_moba::mobaapplication_constructor_args():
    sig = inspect.signature(moba::MobaApplication.__init__)
    params = list(sig.parameters.keys())
    assert "javaPackage" in params, "Missing parameter 'javaPackage'"

def test_moba::mobaapplication_has_javaPackage():
    assert hasattr(moba::MobaApplication, "javaPackage")
    descriptor = None
    for klass in moba::MobaApplication.__mro__:
        if "javaPackage" in klass.__dict__:
            descriptor = klass.__dict__["javaPackage"]
            break
    assert isinstance(descriptor, property)



def test_moba::mobaproject_is_not_abstract():
    assert not inspect.isabstract(moba::MobaProject)


def test_moba::mobaproject_constructor_exists():
    assert callable(moba::MobaProject.__init__)


def test_moba::mobaproject_constructor_args():
    sig = inspect.signature(moba::MobaProject.__init__)
    params = list(sig.parameters.keys())



def test_moba::mobamodelfeature_is_not_abstract():
    assert not inspect.isabstract(moba::MobaModelFeature)


def test_moba::mobamodelfeature_constructor_exists():
    assert callable(moba::MobaModelFeature.__init__)


def test_moba::mobamodelfeature_constructor_args():
    sig = inspect.signature(moba::MobaModelFeature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "version" in params, "Missing parameter 'version'"
    assert "id" in params, "Missing parameter 'id'"

def test_moba::mobamodelfeature_has_name():
    assert hasattr(moba::MobaModelFeature, "name")
    descriptor = None
    for klass in moba::MobaModelFeature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobamodelfeature_has_version():
    assert hasattr(moba::MobaModelFeature, "version")
    descriptor = None
    for klass in moba::MobaModelFeature.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_moba::mobamodelfeature_has_id():
    assert hasattr(moba::MobaModelFeature, "id")
    descriptor = None
    for klass in moba::MobaModelFeature.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_mobalowerbound_exists():
    # Check that the Enumeration exists
    assert MobaLowerBound is not None

def test_mobalowerbound_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MobaLowerBound]
    expected_literals = [
        "ZERO",
        "ONE",
        "ATLEASTONE",
        "MANY",
        "OPTIONAL",
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

def test_mobanfcmoduletype_exists():
    # Check that the Enumeration exists
    assert MobaNFCModuleType is not None

def test_mobanfcmoduletype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MobaNFCModuleType]
    expected_literals = [
        "TEXT",
        "ID",
        "CUSTOM",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MobaNFCModuleType"

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

def test_mobarestmethods_exists():
    # Check that the Enumeration exists
    assert MobaRESTMethods is not None

def test_mobarestmethods_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MobaRESTMethods]
    expected_literals = [
        "POST",
        "GET",
        "PUT",
        "DELETE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MobaRESTMethods"

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

def test_mobaconstantvaluefunction_exists():
    # Check that the Enumeration exists
    assert MobaConstantValueFunction is not None

def test_mobaconstantvaluefunction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MobaConstantValueFunction]
    expected_literals = [
        "TO_UPPER_CASE",
        "TO_LOWER_CASE",
        "TO_FIRST_LOWER_CASE",
        "TO_FIRST_UPPER_CASE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MobaConstantValueFunction"


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
index::moba::MobaApplication_strategy = st.builds(
    index::moba::MobaApplication,
)
moba::index::MobaIndexEntry_strategy = st.builds(
    moba::index::MobaIndexEntry,
    templateId=
        safe_text,
    relativePath=
        safe_text,
    templateName=
        safe_text,
    filename=
        safe_text,
    templateDescription=
        safe_text,
    templateVersion=
        safe_text
)
MobaIndexEntry_strategy = st.builds(
    MobaIndexEntry,
)
MobaExternalModule_strategy = st.builds(
    MobaExternalModule,
)
moba::MobaNFCModule_strategy = st.builds(
    moba::MobaNFCModule,
    type=
        safe_text
)
moba::MobaPushModule_strategy = st.builds(
    moba::MobaPushModule,
)
moba::MobaBluetoothModule_strategy = st.builds(
    moba::MobaBluetoothModule,
    type=
        safe_text
)
MobaPropertiesAble_strategy = st.builds(
    MobaPropertiesAble,
)
moba::MobaFriendsAble_strategy = st.builds(
    moba::MobaFriendsAble,
)
moba::MobaFriend_strategy = st.builds(
    moba::MobaFriend,
    valueString=
        safe_text,
    value=
        safe_text
)
moba::index::MobaIndex_strategy = st.builds(
    moba::index::MobaIndex,
    name=
        safe_text,
    version=
        safe_text,
    description=
        safe_text,
    id=
        safe_text
)
moba::MobaEnumLiteral_strategy = st.builds(
    moba::MobaEnumLiteral,
    hidden=
        st.booleans(),
    undefined=
        st.booleans(),
    name=
        safe_text,
    default=
        st.booleans(),
    literal=
        safe_text,
    value=
        st.integers()
)
MobaTrigger_strategy = st.builds(
    MobaTrigger,
)
moba::MobaTimerTrigger_strategy = st.builds(
    moba::MobaTimerTrigger,
)
moba::MobaGeofenceTrigger_strategy = st.builds(
    moba::MobaGeofenceTrigger,
    eventType=
        safe_text
)
moba::MobaAppUpdateTrigger_strategy = st.builds(
    moba::MobaAppUpdateTrigger,
)
moba::MobaEmailTrigger_strategy = st.builds(
    moba::MobaEmailTrigger,
)
moba::MobaSMSTrigger_strategy = st.builds(
    moba::MobaSMSTrigger,
)
moba::MobaDeviceStartupTrigger_strategy = st.builds(
    moba::MobaDeviceStartupTrigger,
)
moba::MobaPushTrigger_strategy = st.builds(
    moba::MobaPushTrigger,
)
moba::MobaAppInstallTrigger_strategy = st.builds(
    moba::MobaAppInstallTrigger,
)
MobaConstraint_strategy = st.builds(
    MobaConstraint,
)
moba::MobaDigitsConstraint_strategy = st.builds(
    moba::MobaDigitsConstraint,
    filterIntegerValue=
        st.integers(),
    filterFractionValue=
        st.integers()
)
moba::MobaMaxLengthConstraint_strategy = st.builds(
    moba::MobaMaxLengthConstraint,
    filterValue=
        st.integers()
)
moba::MobaRegexpConstraint_strategy = st.builds(
    moba::MobaRegexpConstraint,
    filterString=
        safe_text
)
moba::MobaConstraint_strategy = st.builds(
    moba::MobaConstraint,
)
moba::MobaConstraintable_strategy = st.builds(
    moba::MobaConstraintable,
)
MobaQueueFeature_strategy = st.builds(
    MobaQueueFeature,
)
moba::MobaQueueReference_strategy = st.builds(
    moba::MobaQueueReference,
)
moba::MobaMinLengthConstraint_strategy = st.builds(
    moba::MobaMinLengthConstraint,
    filterValue=
        st.integers()
)
moba::MobaNullConstraint_strategy = st.builds(
    moba::MobaNullConstraint,
)
moba::MobaNotNullConstraint_strategy = st.builds(
    moba::MobaNotNullConstraint,
)
moba::MobaPastConstraint_strategy = st.builds(
    moba::MobaPastConstraint,
)
moba::MobaFutureConstraint_strategy = st.builds(
    moba::MobaFutureConstraint,
)
moba::MobaMaxConstraint_strategy = st.builds(
    moba::MobaMaxConstraint,
    filterValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
moba::MobaMinConstraint_strategy = st.builds(
    moba::MobaMinConstraint,
    filterValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
moba::MobaMuliplicity_strategy = st.builds(
    moba::MobaMuliplicity,
    upper=
        safe_text,
    lower=
        safe_text
)
moba::MobaMultiplicityAble_strategy = st.builds(
    moba::MobaMultiplicityAble,
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
moba::MobaRESTDtoAttribute_strategy = st.builds(
    moba::MobaRESTDtoAttribute,
)
moba::MobaRESTAttribute_strategy = st.builds(
    moba::MobaRESTAttribute,
    formatString=
        safe_text,
    key=
        safe_text,
    value=
        safe_text,
    keyString=
        safe_text,
    valueInt=
        safe_text,
    valueDouble=
        safe_text,
    valueString=
        safe_text
)
moba::MobaRESTAbstractAttribute_strategy = st.builds(
    moba::MobaRESTAbstractAttribute,
    attachment=
        st.booleans(),
    alias=
        safe_text,
    aliasString=
        safe_text
)
MobaREST_strategy = st.builds(
    MobaREST,
)
moba::MobaRESTWorkflow_strategy = st.builds(
    moba::MobaRESTWorkflow,
)
moba::MobaRESTCrud_strategy = st.builds(
    moba::MobaRESTCrud,
    operations=
        safe_text
)
moba::MobaRESTCustomService_strategy = st.builds(
    moba::MobaRESTCustomService,
    operation=
        safe_text
)
moba::MobaRESTPayloadDefinition_strategy = st.builds(
    moba::MobaRESTPayloadDefinition,
    array=
        st.booleans()
)
moba::MobaEntityIndex_strategy = st.builds(
    moba::MobaEntityIndex,
    unique=
        st.booleans(),
    name=
        safe_text
)
moba::MobaRESTHeader_strategy = st.builds(
    moba::MobaRESTHeader,
    contentTypeHeader=
        st.booleans(),
    key=
        safe_text,
    value=
        safe_text,
    keyString=
        safe_text,
    rawHeader=
        st.booleans(),
    valueString=
        safe_text
)
MobaMultiplicityAble_strategy = st.builds(
    MobaMultiplicityAble,
)
moba::MobaDtoEmbeddable_strategy = st.builds(
    moba::MobaDtoEmbeddable,
    transient=
        st.booleans(),
    alias=
        safe_text
)
moba::MobaEntityEmbeddable_strategy = st.builds(
    moba::MobaEntityEmbeddable,
    transient=
        st.booleans()
)
moba::MobaEntityReference_strategy = st.builds(
    moba::MobaEntityReference,
    lazy=
        st.booleans(),
    cascading=
        st.booleans(),
    transient=
        st.booleans()
)
moba::MobaDtoReference_strategy = st.builds(
    moba::MobaDtoReference,
    transient=
        st.booleans(),
    cascading=
        st.booleans(),
    alias=
        safe_text,
    lazy=
        st.booleans()
)
MobaSettingsFeature_strategy = st.builds(
    MobaSettingsFeature,
)
MobaFeature_strategy = st.builds(
    MobaFeature,
)
moba::MobaEntityFeature_strategy = st.builds(
    moba::MobaEntityFeature,
)
moba::MobaDtoFeature_strategy = st.builds(
    moba::MobaDtoFeature,
)
moba::MobaQueueFeature_strategy = st.builds(
    moba::MobaQueueFeature,
)
moba::MobaSettingsFeature_strategy = st.builds(
    moba::MobaSettingsFeature,
)
MobaData_strategy = st.builds(
    MobaData,
)
moba::MobaQueue_strategy = st.builds(
    moba::MobaQueue,
    name=
        safe_text
)
moba::MobaDto_strategy = st.builds(
    moba::MobaDto,
    name=
        safe_text
)
moba::MobaEntity_strategy = st.builds(
    moba::MobaEntity,
    name=
        safe_text
)
moba::MobaConstantValue_strategy = st.builds(
    moba::MobaConstantValue,
    valueConstFunctions=
        safe_text,
    valueDouble=
        safe_text,
    valueConstToLowerCase=
        st.booleans(),
    valueInt=
        safe_text,
    valueString=
        safe_text
)
moba::MobaProperty_strategy = st.builds(
    moba::MobaProperty,
    valueString=
        safe_text,
    keyString=
        safe_text,
    value=
        safe_text,
    key=
        safe_text
)
moba::MobaPropertiesAble_strategy = st.builds(
    moba::MobaPropertiesAble,
)
moba::MobaGeneratorFeature_strategy = st.builds(
    moba::MobaGeneratorFeature,
)
MobaApplicationFeature_strategy = st.builds(
    MobaApplicationFeature,
)
moba::MobaSettings_strategy = st.builds(
    moba::MobaSettings,
    active=
        st.booleans(),
    name=
        safe_text
)
moba::MobaTransportSerializationType_strategy = st.builds(
    moba::MobaTransportSerializationType,
    name=
        safe_text
)
moba::MobaGenerator_strategy = st.builds(
    moba::MobaGenerator,
    active=
        st.booleans(),
    name=
        safe_text
)
moba::MobaServer_strategy = st.builds(
    moba::MobaServer,
    urlString=
        safe_text,
    name=
        safe_text
)
moba::MobaData_strategy = st.builds(
    moba::MobaData,
)
moba::MobaEnum_strategy = st.builds(
    moba::MobaEnum,
)
moba::MobaAuthorization_strategy = st.builds(
    moba::MobaAuthorization,
    name=
        safe_text
)
moba::MobaConstant_strategy = st.builds(
    moba::MobaConstant,
    name=
        safe_text
)
moba::MobaTrigger_strategy = st.builds(
    moba::MobaTrigger,
    name=
        safe_text
)
moba::MobaExternalModule_strategy = st.builds(
    moba::MobaExternalModule,
    name=
        safe_text
)
moba::MobaPersistenceType_strategy = st.builds(
    moba::MobaPersistenceType,
    name=
        safe_text
)
moba::MobaREST_strategy = st.builds(
    moba::MobaREST,
    bigData=
        st.booleans(),
    url=
        safe_text,
    path=
        safe_text,
    name=
        safe_text
)
moba::MobaTemplate_strategy = st.builds(
    moba::MobaTemplate,
    downloadTemplate=
        safe_text
)
MobaConstraintable_strategy = st.builds(
    MobaConstraintable,
)
moba::MobaEntityAttribute_strategy = st.builds(
    moba::MobaEntityAttribute,
    formatString=
        safe_text,
    domainKey=
        st.booleans(),
    transient=
        st.booleans(),
    lazy=
        st.booleans(),
    domainDescription=
        st.booleans()
)
moba::MobaSettingsAttribute_strategy = st.builds(
    moba::MobaSettingsAttribute,
    formatString=
        safe_text,
    domainDescription=
        st.booleans(),
    lazy=
        st.booleans(),
    transient=
        st.booleans(),
    domainKey=
        st.booleans()
)
moba::MobaDtoAttribute_strategy = st.builds(
    moba::MobaDtoAttribute,
    alias=
        safe_text,
    domainDescription=
        st.booleans(),
    lazy=
        st.booleans(),
    domainKey=
        st.booleans(),
    transient=
        st.booleans(),
    formatString=
        safe_text
)
moba::MobaSettingsEntityReference_strategy = st.builds(
    moba::MobaSettingsEntityReference,
    lazy=
        st.booleans(),
    transient=
        st.booleans(),
    cascading=
        st.booleans()
)
moba::MobaDataType_strategy = st.builds(
    moba::MobaDataType,
    primitive=
        st.booleans(),
    string=
        st.booleans(),
    timestamp=
        st.booleans(),
    name=
        safe_text,
    bool=
        st.booleans(),
    numeric=
        st.booleans(),
    decimal=
        st.booleans(),
    time=
        st.booleans(),
    array=
        st.booleans(),
    dateFormatString=
        safe_text,
    date=
        st.booleans(),
    predefined=
        st.booleans()
)
moba::MobaGeneratorSlot_strategy = st.builds(
    moba::MobaGeneratorSlot,
    name=
        safe_text,
    type=
        safe_text
)
MobaGeneratorFeature_strategy = st.builds(
    MobaGeneratorFeature,
)
moba::MobaGeneratorIDFeature_strategy = st.builds(
    moba::MobaGeneratorIDFeature,
    generatorId=
        safe_text,
    generatorVersion=
        safe_text
)
moba::MobaGeneratorMixinFeature_strategy = st.builds(
    moba::MobaGeneratorMixinFeature,
)
MobaFriendsAble_strategy = st.builds(
    MobaFriendsAble,
)
moba::MobaApplicationFeature_strategy = st.builds(
    moba::MobaApplicationFeature,
)
moba::MobaFeature_strategy = st.builds(
    moba::MobaFeature,
    name=
        safe_text
)
moba::MobaModel_strategy = st.builds(
    moba::MobaModel,
    copyright=
        safe_text
)
moba::MobaCache_strategy = st.builds(
    moba::MobaCache,
    cacheIntervalInt=
        st.integers(),
    cacheStrategyString=
        safe_text,
    name=
        safe_text,
    cacheTypeString=
        safe_text
)
MobaModelFeature_strategy = st.builds(
    MobaModelFeature,
)
moba::MobaApplication_strategy = st.builds(
    moba::MobaApplication,
    javaPackage=
        safe_text
)
moba::MobaProject_strategy = st.builds(
    moba::MobaProject,
)
moba::MobaModelFeature_strategy = st.builds(
    moba::MobaModelFeature,
    name=
        safe_text,
    version=
        safe_text,
    id=
        safe_text
)

@given(instance=index::moba::MobaApplication_strategy)
@settings(max_examples=50)
def test_index::moba::mobaapplication_instantiation(instance):
    assert isinstance(instance, index::moba::MobaApplication)

@given(instance=moba::index::MobaIndexEntry_strategy)
@settings(max_examples=50)
def test_moba::index::mobaindexentry_instantiation(instance):
    assert isinstance(instance, moba::index::MobaIndexEntry)

@given(instance=moba::index::MobaIndexEntry_strategy)
def test_moba::index::mobaindexentry_templateId_type(instance):
    assert isinstance(instance.templateId, str)


@given(instance=moba::index::MobaIndexEntry_strategy)
def test_moba::index::mobaindexentry_templateId_setter(instance):
    original = instance.templateId
    instance.templateId = original
    assert instance.templateId == original

@given(instance=moba::index::MobaIndexEntry_strategy)
def test_moba::index::mobaindexentry_relativePath_type(instance):
    assert isinstance(instance.relativePath, str)


@given(instance=moba::index::MobaIndexEntry_strategy)
def test_moba::index::mobaindexentry_relativePath_setter(instance):
    original = instance.relativePath
    instance.relativePath = original
    assert instance.relativePath == original

@given(instance=moba::index::MobaIndexEntry_strategy)
def test_moba::index::mobaindexentry_templateName_type(instance):
    assert isinstance(instance.templateName, str)


@given(instance=moba::index::MobaIndexEntry_strategy)
def test_moba::index::mobaindexentry_templateName_setter(instance):
    original = instance.templateName
    instance.templateName = original
    assert instance.templateName == original

@given(instance=moba::index::MobaIndexEntry_strategy)
def test_moba::index::mobaindexentry_filename_type(instance):
    assert isinstance(instance.filename, str)


@given(instance=moba::index::MobaIndexEntry_strategy)
def test_moba::index::mobaindexentry_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=moba::index::MobaIndexEntry_strategy)
def test_moba::index::mobaindexentry_templateDescription_type(instance):
    assert isinstance(instance.templateDescription, str)


@given(instance=moba::index::MobaIndexEntry_strategy)
def test_moba::index::mobaindexentry_templateDescription_setter(instance):
    original = instance.templateDescription
    instance.templateDescription = original
    assert instance.templateDescription == original

@given(instance=moba::index::MobaIndexEntry_strategy)
def test_moba::index::mobaindexentry_templateVersion_type(instance):
    assert isinstance(instance.templateVersion, str)


@given(instance=moba::index::MobaIndexEntry_strategy)
def test_moba::index::mobaindexentry_templateVersion_setter(instance):
    original = instance.templateVersion
    instance.templateVersion = original
    assert instance.templateVersion == original

@given(instance=MobaIndexEntry_strategy)
@settings(max_examples=50)
def test_mobaindexentry_instantiation(instance):
    assert isinstance(instance, MobaIndexEntry)

@given(instance=MobaExternalModule_strategy)
@settings(max_examples=50)
def test_mobaexternalmodule_instantiation(instance):
    assert isinstance(instance, MobaExternalModule)

@given(instance=moba::MobaNFCModule_strategy)
@settings(max_examples=50)
def test_moba::mobanfcmodule_instantiation(instance):
    assert isinstance(instance, moba::MobaNFCModule)

@given(instance=moba::MobaNFCModule_strategy)
def test_moba::mobanfcmodule_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=moba::MobaNFCModule_strategy)
def test_moba::mobanfcmodule_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=moba::MobaPushModule_strategy)
@settings(max_examples=50)
def test_moba::mobapushmodule_instantiation(instance):
    assert isinstance(instance, moba::MobaPushModule)

@given(instance=moba::MobaBluetoothModule_strategy)
@settings(max_examples=50)
def test_moba::mobabluetoothmodule_instantiation(instance):
    assert isinstance(instance, moba::MobaBluetoothModule)

@given(instance=moba::MobaBluetoothModule_strategy)
def test_moba::mobabluetoothmodule_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=moba::MobaBluetoothModule_strategy)
def test_moba::mobabluetoothmodule_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=MobaPropertiesAble_strategy)
@settings(max_examples=50)
def test_mobapropertiesable_instantiation(instance):
    assert isinstance(instance, MobaPropertiesAble)

@given(instance=moba::MobaFriendsAble_strategy)
@settings(max_examples=50)
def test_moba::mobafriendsable_instantiation(instance):
    assert isinstance(instance, moba::MobaFriendsAble)

@given(instance=moba::MobaFriend_strategy)
@settings(max_examples=50)
def test_moba::mobafriend_instantiation(instance):
    assert isinstance(instance, moba::MobaFriend)

@given(instance=moba::MobaFriend_strategy)
def test_moba::mobafriend_valueString_type(instance):
    assert isinstance(instance.valueString, str)


@given(instance=moba::MobaFriend_strategy)
def test_moba::mobafriend_valueString_setter(instance):
    original = instance.valueString
    instance.valueString = original
    assert instance.valueString == original

@given(instance=moba::MobaFriend_strategy)
def test_moba::mobafriend_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=moba::MobaFriend_strategy)
def test_moba::mobafriend_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=moba::index::MobaIndex_strategy)
@settings(max_examples=50)
def test_moba::index::mobaindex_instantiation(instance):
    assert isinstance(instance, moba::index::MobaIndex)

@given(instance=moba::index::MobaIndex_strategy)
def test_moba::index::mobaindex_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=moba::index::MobaIndex_strategy)
def test_moba::index::mobaindex_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=moba::index::MobaIndex_strategy)
def test_moba::index::mobaindex_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=moba::index::MobaIndex_strategy)
def test_moba::index::mobaindex_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=moba::index::MobaIndex_strategy)
def test_moba::index::mobaindex_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=moba::index::MobaIndex_strategy)
def test_moba::index::mobaindex_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=moba::index::MobaIndex_strategy)
def test_moba::index::mobaindex_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=moba::index::MobaIndex_strategy)
def test_moba::index::mobaindex_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=moba::MobaEnumLiteral_strategy)
@settings(max_examples=50)
def test_moba::mobaenumliteral_instantiation(instance):
    assert isinstance(instance, moba::MobaEnumLiteral)

@given(instance=moba::MobaEnumLiteral_strategy)
def test_moba::mobaenumliteral_hidden_type(instance):
    assert isinstance(instance.hidden, bool)


@given(instance=moba::MobaEnumLiteral_strategy)
def test_moba::mobaenumliteral_hidden_setter(instance):
    original = instance.hidden
    instance.hidden = original
    assert instance.hidden == original

@given(instance=moba::MobaEnumLiteral_strategy)
def test_moba::mobaenumliteral_undefined_type(instance):
    assert isinstance(instance.undefined, bool)


@given(instance=moba::MobaEnumLiteral_strategy)
def test_moba::mobaenumliteral_undefined_setter(instance):
    original = instance.undefined
    instance.undefined = original
    assert instance.undefined == original

@given(instance=moba::MobaEnumLiteral_strategy)
def test_moba::mobaenumliteral_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=moba::MobaEnumLiteral_strategy)
def test_moba::mobaenumliteral_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=moba::MobaEnumLiteral_strategy)
def test_moba::mobaenumliteral_default_type(instance):
    assert isinstance(instance.default, bool)


@given(instance=moba::MobaEnumLiteral_strategy)
def test_moba::mobaenumliteral_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=moba::MobaEnumLiteral_strategy)
def test_moba::mobaenumliteral_literal_type(instance):
    assert isinstance(instance.literal, str)


@given(instance=moba::MobaEnumLiteral_strategy)
def test_moba::mobaenumliteral_literal_setter(instance):
    original = instance.literal
    instance.literal = original
    assert instance.literal == original

@given(instance=moba::MobaEnumLiteral_strategy)
def test_moba::mobaenumliteral_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=moba::MobaEnumLiteral_strategy)
def test_moba::mobaenumliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=MobaTrigger_strategy)
@settings(max_examples=50)
def test_mobatrigger_instantiation(instance):
    assert isinstance(instance, MobaTrigger)

@given(instance=moba::MobaTimerTrigger_strategy)
@settings(max_examples=50)
def test_moba::mobatimertrigger_instantiation(instance):
    assert isinstance(instance, moba::MobaTimerTrigger)

@given(instance=moba::MobaGeofenceTrigger_strategy)
@settings(max_examples=50)
def test_moba::mobageofencetrigger_instantiation(instance):
    assert isinstance(instance, moba::MobaGeofenceTrigger)

@given(instance=moba::MobaGeofenceTrigger_strategy)
def test_moba::mobageofencetrigger_eventType_type(instance):
    assert isinstance(instance.eventType, str)


@given(instance=moba::MobaGeofenceTrigger_strategy)
def test_moba::mobageofencetrigger_eventType_setter(instance):
    original = instance.eventType
    instance.eventType = original
    assert instance.eventType == original

@given(instance=moba::MobaAppUpdateTrigger_strategy)
@settings(max_examples=50)
def test_moba::mobaappupdatetrigger_instantiation(instance):
    assert isinstance(instance, moba::MobaAppUpdateTrigger)

@given(instance=moba::MobaEmailTrigger_strategy)
@settings(max_examples=50)
def test_moba::mobaemailtrigger_instantiation(instance):
    assert isinstance(instance, moba::MobaEmailTrigger)

@given(instance=moba::MobaSMSTrigger_strategy)
@settings(max_examples=50)
def test_moba::mobasmstrigger_instantiation(instance):
    assert isinstance(instance, moba::MobaSMSTrigger)

@given(instance=moba::MobaDeviceStartupTrigger_strategy)
@settings(max_examples=50)
def test_moba::mobadevicestartuptrigger_instantiation(instance):
    assert isinstance(instance, moba::MobaDeviceStartupTrigger)

@given(instance=moba::MobaPushTrigger_strategy)
@settings(max_examples=50)
def test_moba::mobapushtrigger_instantiation(instance):
    assert isinstance(instance, moba::MobaPushTrigger)

@given(instance=moba::MobaAppInstallTrigger_strategy)
@settings(max_examples=50)
def test_moba::mobaappinstalltrigger_instantiation(instance):
    assert isinstance(instance, moba::MobaAppInstallTrigger)

@given(instance=MobaConstraint_strategy)
@settings(max_examples=50)
def test_mobaconstraint_instantiation(instance):
    assert isinstance(instance, MobaConstraint)

@given(instance=moba::MobaDigitsConstraint_strategy)
@settings(max_examples=50)
def test_moba::mobadigitsconstraint_instantiation(instance):
    assert isinstance(instance, moba::MobaDigitsConstraint)

@given(instance=moba::MobaDigitsConstraint_strategy)
def test_moba::mobadigitsconstraint_filterIntegerValue_type(instance):
    assert isinstance(instance.filterIntegerValue, int)


@given(instance=moba::MobaDigitsConstraint_strategy)
def test_moba::mobadigitsconstraint_filterIntegerValue_setter(instance):
    original = instance.filterIntegerValue
    instance.filterIntegerValue = original
    assert instance.filterIntegerValue == original

@given(instance=moba::MobaDigitsConstraint_strategy)
def test_moba::mobadigitsconstraint_filterFractionValue_type(instance):
    assert isinstance(instance.filterFractionValue, int)


@given(instance=moba::MobaDigitsConstraint_strategy)
def test_moba::mobadigitsconstraint_filterFractionValue_setter(instance):
    original = instance.filterFractionValue
    instance.filterFractionValue = original
    assert instance.filterFractionValue == original

@given(instance=moba::MobaMaxLengthConstraint_strategy)
@settings(max_examples=50)
def test_moba::mobamaxlengthconstraint_instantiation(instance):
    assert isinstance(instance, moba::MobaMaxLengthConstraint)

@given(instance=moba::MobaMaxLengthConstraint_strategy)
def test_moba::mobamaxlengthconstraint_filterValue_type(instance):
    assert isinstance(instance.filterValue, int)


@given(instance=moba::MobaMaxLengthConstraint_strategy)
def test_moba::mobamaxlengthconstraint_filterValue_setter(instance):
    original = instance.filterValue
    instance.filterValue = original
    assert instance.filterValue == original

@given(instance=moba::MobaRegexpConstraint_strategy)
@settings(max_examples=50)
def test_moba::mobaregexpconstraint_instantiation(instance):
    assert isinstance(instance, moba::MobaRegexpConstraint)

@given(instance=moba::MobaRegexpConstraint_strategy)
def test_moba::mobaregexpconstraint_filterString_type(instance):
    assert isinstance(instance.filterString, str)


@given(instance=moba::MobaRegexpConstraint_strategy)
def test_moba::mobaregexpconstraint_filterString_setter(instance):
    original = instance.filterString
    instance.filterString = original
    assert instance.filterString == original

@given(instance=moba::MobaConstraint_strategy)
@settings(max_examples=50)
def test_moba::mobaconstraint_instantiation(instance):
    assert isinstance(instance, moba::MobaConstraint)

@given(instance=moba::MobaConstraintable_strategy)
@settings(max_examples=50)
def test_moba::mobaconstraintable_instantiation(instance):
    assert isinstance(instance, moba::MobaConstraintable)

@given(instance=MobaQueueFeature_strategy)
@settings(max_examples=50)
def test_mobaqueuefeature_instantiation(instance):
    assert isinstance(instance, MobaQueueFeature)

@given(instance=moba::MobaQueueReference_strategy)
@settings(max_examples=50)
def test_moba::mobaqueuereference_instantiation(instance):
    assert isinstance(instance, moba::MobaQueueReference)

@given(instance=moba::MobaMinLengthConstraint_strategy)
@settings(max_examples=50)
def test_moba::mobaminlengthconstraint_instantiation(instance):
    assert isinstance(instance, moba::MobaMinLengthConstraint)

@given(instance=moba::MobaMinLengthConstraint_strategy)
def test_moba::mobaminlengthconstraint_filterValue_type(instance):
    assert isinstance(instance.filterValue, int)


@given(instance=moba::MobaMinLengthConstraint_strategy)
def test_moba::mobaminlengthconstraint_filterValue_setter(instance):
    original = instance.filterValue
    instance.filterValue = original
    assert instance.filterValue == original

@given(instance=moba::MobaNullConstraint_strategy)
@settings(max_examples=50)
def test_moba::mobanullconstraint_instantiation(instance):
    assert isinstance(instance, moba::MobaNullConstraint)

@given(instance=moba::MobaNotNullConstraint_strategy)
@settings(max_examples=50)
def test_moba::mobanotnullconstraint_instantiation(instance):
    assert isinstance(instance, moba::MobaNotNullConstraint)

@given(instance=moba::MobaPastConstraint_strategy)
@settings(max_examples=50)
def test_moba::mobapastconstraint_instantiation(instance):
    assert isinstance(instance, moba::MobaPastConstraint)

@given(instance=moba::MobaFutureConstraint_strategy)
@settings(max_examples=50)
def test_moba::mobafutureconstraint_instantiation(instance):
    assert isinstance(instance, moba::MobaFutureConstraint)

@given(instance=moba::MobaMaxConstraint_strategy)
@settings(max_examples=50)
def test_moba::mobamaxconstraint_instantiation(instance):
    assert isinstance(instance, moba::MobaMaxConstraint)

@given(instance=moba::MobaMaxConstraint_strategy)
def test_moba::mobamaxconstraint_filterValue_type(instance):
    assert isinstance(instance.filterValue, float)


@given(instance=moba::MobaMaxConstraint_strategy)
def test_moba::mobamaxconstraint_filterValue_setter(instance):
    original = instance.filterValue
    instance.filterValue = original
    assert instance.filterValue == original

@given(instance=moba::MobaMinConstraint_strategy)
@settings(max_examples=50)
def test_moba::mobaminconstraint_instantiation(instance):
    assert isinstance(instance, moba::MobaMinConstraint)

@given(instance=moba::MobaMinConstraint_strategy)
def test_moba::mobaminconstraint_filterValue_type(instance):
    assert isinstance(instance.filterValue, float)


@given(instance=moba::MobaMinConstraint_strategy)
def test_moba::mobaminconstraint_filterValue_setter(instance):
    original = instance.filterValue
    instance.filterValue = original
    assert instance.filterValue == original

@given(instance=moba::MobaMuliplicity_strategy)
@settings(max_examples=50)
def test_moba::mobamuliplicity_instantiation(instance):
    assert isinstance(instance, moba::MobaMuliplicity)

@given(instance=moba::MobaMuliplicity_strategy)
def test_moba::mobamuliplicity_upper_type(instance):
    assert isinstance(instance.upper, str)


@given(instance=moba::MobaMuliplicity_strategy)
def test_moba::mobamuliplicity_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=moba::MobaMuliplicity_strategy)
def test_moba::mobamuliplicity_lower_type(instance):
    assert isinstance(instance.lower, str)


@given(instance=moba::MobaMuliplicity_strategy)
def test_moba::mobamuliplicity_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=moba::MobaMultiplicityAble_strategy)
@settings(max_examples=50)
def test_moba::mobamultiplicityable_instantiation(instance):
    assert isinstance(instance, moba::MobaMultiplicityAble)

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

@given(instance=moba::MobaRESTDtoAttribute_strategy)
@settings(max_examples=50)
def test_moba::mobarestdtoattribute_instantiation(instance):
    assert isinstance(instance, moba::MobaRESTDtoAttribute)

@given(instance=moba::MobaRESTAttribute_strategy)
@settings(max_examples=50)
def test_moba::mobarestattribute_instantiation(instance):
    assert isinstance(instance, moba::MobaRESTAttribute)

@given(instance=moba::MobaRESTAttribute_strategy)
def test_moba::mobarestattribute_formatString_type(instance):
    assert isinstance(instance.formatString, str)


@given(instance=moba::MobaRESTAttribute_strategy)
def test_moba::mobarestattribute_formatString_setter(instance):
    original = instance.formatString
    instance.formatString = original
    assert instance.formatString == original

@given(instance=moba::MobaRESTAttribute_strategy)
def test_moba::mobarestattribute_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=moba::MobaRESTAttribute_strategy)
def test_moba::mobarestattribute_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=moba::MobaRESTAttribute_strategy)
def test_moba::mobarestattribute_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=moba::MobaRESTAttribute_strategy)
def test_moba::mobarestattribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=moba::MobaRESTAttribute_strategy)
def test_moba::mobarestattribute_keyString_type(instance):
    assert isinstance(instance.keyString, str)


@given(instance=moba::MobaRESTAttribute_strategy)
def test_moba::mobarestattribute_keyString_setter(instance):
    original = instance.keyString
    instance.keyString = original
    assert instance.keyString == original

@given(instance=moba::MobaRESTAttribute_strategy)
def test_moba::mobarestattribute_valueInt_type(instance):
    assert isinstance(instance.valueInt, str)


@given(instance=moba::MobaRESTAttribute_strategy)
def test_moba::mobarestattribute_valueInt_setter(instance):
    original = instance.valueInt
    instance.valueInt = original
    assert instance.valueInt == original

@given(instance=moba::MobaRESTAttribute_strategy)
def test_moba::mobarestattribute_valueDouble_type(instance):
    assert isinstance(instance.valueDouble, str)


@given(instance=moba::MobaRESTAttribute_strategy)
def test_moba::mobarestattribute_valueDouble_setter(instance):
    original = instance.valueDouble
    instance.valueDouble = original
    assert instance.valueDouble == original

@given(instance=moba::MobaRESTAttribute_strategy)
def test_moba::mobarestattribute_valueString_type(instance):
    assert isinstance(instance.valueString, str)


@given(instance=moba::MobaRESTAttribute_strategy)
def test_moba::mobarestattribute_valueString_setter(instance):
    original = instance.valueString
    instance.valueString = original
    assert instance.valueString == original

@given(instance=moba::MobaRESTAbstractAttribute_strategy)
@settings(max_examples=50)
def test_moba::mobarestabstractattribute_instantiation(instance):
    assert isinstance(instance, moba::MobaRESTAbstractAttribute)

@given(instance=moba::MobaRESTAbstractAttribute_strategy)
def test_moba::mobarestabstractattribute_attachment_type(instance):
    assert isinstance(instance.attachment, bool)


@given(instance=moba::MobaRESTAbstractAttribute_strategy)
def test_moba::mobarestabstractattribute_attachment_setter(instance):
    original = instance.attachment
    instance.attachment = original
    assert instance.attachment == original

@given(instance=moba::MobaRESTAbstractAttribute_strategy)
def test_moba::mobarestabstractattribute_alias_type(instance):
    assert isinstance(instance.alias, str)


@given(instance=moba::MobaRESTAbstractAttribute_strategy)
def test_moba::mobarestabstractattribute_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=moba::MobaRESTAbstractAttribute_strategy)
def test_moba::mobarestabstractattribute_aliasString_type(instance):
    assert isinstance(instance.aliasString, str)


@given(instance=moba::MobaRESTAbstractAttribute_strategy)
def test_moba::mobarestabstractattribute_aliasString_setter(instance):
    original = instance.aliasString
    instance.aliasString = original
    assert instance.aliasString == original

@given(instance=MobaREST_strategy)
@settings(max_examples=50)
def test_mobarest_instantiation(instance):
    assert isinstance(instance, MobaREST)

@given(instance=moba::MobaRESTWorkflow_strategy)
@settings(max_examples=50)
def test_moba::mobarestworkflow_instantiation(instance):
    assert isinstance(instance, moba::MobaRESTWorkflow)

@given(instance=moba::MobaRESTCrud_strategy)
@settings(max_examples=50)
def test_moba::mobarestcrud_instantiation(instance):
    assert isinstance(instance, moba::MobaRESTCrud)

@given(instance=moba::MobaRESTCrud_strategy)
def test_moba::mobarestcrud_operations_type(instance):
    assert isinstance(instance.operations, str)


@given(instance=moba::MobaRESTCrud_strategy)
def test_moba::mobarestcrud_operations_setter(instance):
    original = instance.operations
    instance.operations = original
    assert instance.operations == original

@given(instance=moba::MobaRESTCustomService_strategy)
@settings(max_examples=50)
def test_moba::mobarestcustomservice_instantiation(instance):
    assert isinstance(instance, moba::MobaRESTCustomService)

@given(instance=moba::MobaRESTCustomService_strategy)
def test_moba::mobarestcustomservice_operation_type(instance):
    assert isinstance(instance.operation, str)


@given(instance=moba::MobaRESTCustomService_strategy)
def test_moba::mobarestcustomservice_operation_setter(instance):
    original = instance.operation
    instance.operation = original
    assert instance.operation == original

@given(instance=moba::MobaRESTPayloadDefinition_strategy)
@settings(max_examples=50)
def test_moba::mobarestpayloaddefinition_instantiation(instance):
    assert isinstance(instance, moba::MobaRESTPayloadDefinition)

@given(instance=moba::MobaRESTPayloadDefinition_strategy)
def test_moba::mobarestpayloaddefinition_array_type(instance):
    assert isinstance(instance.array, bool)


@given(instance=moba::MobaRESTPayloadDefinition_strategy)
def test_moba::mobarestpayloaddefinition_array_setter(instance):
    original = instance.array
    instance.array = original
    assert instance.array == original

@given(instance=moba::MobaEntityIndex_strategy)
@settings(max_examples=50)
def test_moba::mobaentityindex_instantiation(instance):
    assert isinstance(instance, moba::MobaEntityIndex)

@given(instance=moba::MobaEntityIndex_strategy)
def test_moba::mobaentityindex_unique_type(instance):
    assert isinstance(instance.unique, bool)


@given(instance=moba::MobaEntityIndex_strategy)
def test_moba::mobaentityindex_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original

@given(instance=moba::MobaEntityIndex_strategy)
def test_moba::mobaentityindex_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=moba::MobaEntityIndex_strategy)
def test_moba::mobaentityindex_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=moba::MobaRESTHeader_strategy)
@settings(max_examples=50)
def test_moba::mobarestheader_instantiation(instance):
    assert isinstance(instance, moba::MobaRESTHeader)

@given(instance=moba::MobaRESTHeader_strategy)
def test_moba::mobarestheader_contentTypeHeader_type(instance):
    assert isinstance(instance.contentTypeHeader, bool)


@given(instance=moba::MobaRESTHeader_strategy)
def test_moba::mobarestheader_contentTypeHeader_setter(instance):
    original = instance.contentTypeHeader
    instance.contentTypeHeader = original
    assert instance.contentTypeHeader == original

@given(instance=moba::MobaRESTHeader_strategy)
def test_moba::mobarestheader_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=moba::MobaRESTHeader_strategy)
def test_moba::mobarestheader_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=moba::MobaRESTHeader_strategy)
def test_moba::mobarestheader_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=moba::MobaRESTHeader_strategy)
def test_moba::mobarestheader_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=moba::MobaRESTHeader_strategy)
def test_moba::mobarestheader_keyString_type(instance):
    assert isinstance(instance.keyString, str)


@given(instance=moba::MobaRESTHeader_strategy)
def test_moba::mobarestheader_keyString_setter(instance):
    original = instance.keyString
    instance.keyString = original
    assert instance.keyString == original

@given(instance=moba::MobaRESTHeader_strategy)
def test_moba::mobarestheader_rawHeader_type(instance):
    assert isinstance(instance.rawHeader, bool)


@given(instance=moba::MobaRESTHeader_strategy)
def test_moba::mobarestheader_rawHeader_setter(instance):
    original = instance.rawHeader
    instance.rawHeader = original
    assert instance.rawHeader == original

@given(instance=moba::MobaRESTHeader_strategy)
def test_moba::mobarestheader_valueString_type(instance):
    assert isinstance(instance.valueString, str)


@given(instance=moba::MobaRESTHeader_strategy)
def test_moba::mobarestheader_valueString_setter(instance):
    original = instance.valueString
    instance.valueString = original
    assert instance.valueString == original

@given(instance=MobaMultiplicityAble_strategy)
@settings(max_examples=50)
def test_mobamultiplicityable_instantiation(instance):
    assert isinstance(instance, MobaMultiplicityAble)

@given(instance=moba::MobaDtoEmbeddable_strategy)
@settings(max_examples=50)
def test_moba::mobadtoembeddable_instantiation(instance):
    assert isinstance(instance, moba::MobaDtoEmbeddable)

@given(instance=moba::MobaDtoEmbeddable_strategy)
def test_moba::mobadtoembeddable_transient_type(instance):
    assert isinstance(instance.transient, bool)


@given(instance=moba::MobaDtoEmbeddable_strategy)
def test_moba::mobadtoembeddable_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original

@given(instance=moba::MobaDtoEmbeddable_strategy)
def test_moba::mobadtoembeddable_alias_type(instance):
    assert isinstance(instance.alias, str)


@given(instance=moba::MobaDtoEmbeddable_strategy)
def test_moba::mobadtoembeddable_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=moba::MobaEntityEmbeddable_strategy)
@settings(max_examples=50)
def test_moba::mobaentityembeddable_instantiation(instance):
    assert isinstance(instance, moba::MobaEntityEmbeddable)

@given(instance=moba::MobaEntityEmbeddable_strategy)
def test_moba::mobaentityembeddable_transient_type(instance):
    assert isinstance(instance.transient, bool)


@given(instance=moba::MobaEntityEmbeddable_strategy)
def test_moba::mobaentityembeddable_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original

@given(instance=moba::MobaEntityReference_strategy)
@settings(max_examples=50)
def test_moba::mobaentityreference_instantiation(instance):
    assert isinstance(instance, moba::MobaEntityReference)

@given(instance=moba::MobaEntityReference_strategy)
def test_moba::mobaentityreference_lazy_type(instance):
    assert isinstance(instance.lazy, bool)


@given(instance=moba::MobaEntityReference_strategy)
def test_moba::mobaentityreference_lazy_setter(instance):
    original = instance.lazy
    instance.lazy = original
    assert instance.lazy == original

@given(instance=moba::MobaEntityReference_strategy)
def test_moba::mobaentityreference_cascading_type(instance):
    assert isinstance(instance.cascading, bool)


@given(instance=moba::MobaEntityReference_strategy)
def test_moba::mobaentityreference_cascading_setter(instance):
    original = instance.cascading
    instance.cascading = original
    assert instance.cascading == original

@given(instance=moba::MobaEntityReference_strategy)
def test_moba::mobaentityreference_transient_type(instance):
    assert isinstance(instance.transient, bool)


@given(instance=moba::MobaEntityReference_strategy)
def test_moba::mobaentityreference_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original

@given(instance=moba::MobaDtoReference_strategy)
@settings(max_examples=50)
def test_moba::mobadtoreference_instantiation(instance):
    assert isinstance(instance, moba::MobaDtoReference)

@given(instance=moba::MobaDtoReference_strategy)
def test_moba::mobadtoreference_transient_type(instance):
    assert isinstance(instance.transient, bool)


@given(instance=moba::MobaDtoReference_strategy)
def test_moba::mobadtoreference_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original

@given(instance=moba::MobaDtoReference_strategy)
def test_moba::mobadtoreference_cascading_type(instance):
    assert isinstance(instance.cascading, bool)


@given(instance=moba::MobaDtoReference_strategy)
def test_moba::mobadtoreference_cascading_setter(instance):
    original = instance.cascading
    instance.cascading = original
    assert instance.cascading == original

@given(instance=moba::MobaDtoReference_strategy)
def test_moba::mobadtoreference_alias_type(instance):
    assert isinstance(instance.alias, str)


@given(instance=moba::MobaDtoReference_strategy)
def test_moba::mobadtoreference_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=moba::MobaDtoReference_strategy)
def test_moba::mobadtoreference_lazy_type(instance):
    assert isinstance(instance.lazy, bool)


@given(instance=moba::MobaDtoReference_strategy)
def test_moba::mobadtoreference_lazy_setter(instance):
    original = instance.lazy
    instance.lazy = original
    assert instance.lazy == original

@given(instance=MobaSettingsFeature_strategy)
@settings(max_examples=50)
def test_mobasettingsfeature_instantiation(instance):
    assert isinstance(instance, MobaSettingsFeature)

@given(instance=MobaFeature_strategy)
@settings(max_examples=50)
def test_mobafeature_instantiation(instance):
    assert isinstance(instance, MobaFeature)

@given(instance=moba::MobaEntityFeature_strategy)
@settings(max_examples=50)
def test_moba::mobaentityfeature_instantiation(instance):
    assert isinstance(instance, moba::MobaEntityFeature)

@given(instance=moba::MobaDtoFeature_strategy)
@settings(max_examples=50)
def test_moba::mobadtofeature_instantiation(instance):
    assert isinstance(instance, moba::MobaDtoFeature)

@given(instance=moba::MobaQueueFeature_strategy)
@settings(max_examples=50)
def test_moba::mobaqueuefeature_instantiation(instance):
    assert isinstance(instance, moba::MobaQueueFeature)

@given(instance=moba::MobaSettingsFeature_strategy)
@settings(max_examples=50)
def test_moba::mobasettingsfeature_instantiation(instance):
    assert isinstance(instance, moba::MobaSettingsFeature)

@given(instance=MobaData_strategy)
@settings(max_examples=50)
def test_mobadata_instantiation(instance):
    assert isinstance(instance, MobaData)

@given(instance=moba::MobaQueue_strategy)
@settings(max_examples=50)
def test_moba::mobaqueue_instantiation(instance):
    assert isinstance(instance, moba::MobaQueue)

@given(instance=moba::MobaQueue_strategy)
def test_moba::mobaqueue_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=moba::MobaQueue_strategy)
def test_moba::mobaqueue_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=moba::MobaDto_strategy)
@settings(max_examples=50)
def test_moba::mobadto_instantiation(instance):
    assert isinstance(instance, moba::MobaDto)

@given(instance=moba::MobaDto_strategy)
def test_moba::mobadto_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=moba::MobaDto_strategy)
def test_moba::mobadto_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=moba::MobaEntity_strategy)
@settings(max_examples=50)
def test_moba::mobaentity_instantiation(instance):
    assert isinstance(instance, moba::MobaEntity)

@given(instance=moba::MobaEntity_strategy)
def test_moba::mobaentity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=moba::MobaEntity_strategy)
def test_moba::mobaentity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=moba::MobaConstantValue_strategy)
@settings(max_examples=50)
def test_moba::mobaconstantvalue_instantiation(instance):
    assert isinstance(instance, moba::MobaConstantValue)

@given(instance=moba::MobaConstantValue_strategy)
def test_moba::mobaconstantvalue_valueConstFunctions_type(instance):
    assert isinstance(instance.valueConstFunctions, str)


@given(instance=moba::MobaConstantValue_strategy)
def test_moba::mobaconstantvalue_valueConstFunctions_setter(instance):
    original = instance.valueConstFunctions
    instance.valueConstFunctions = original
    assert instance.valueConstFunctions == original

@given(instance=moba::MobaConstantValue_strategy)
def test_moba::mobaconstantvalue_valueDouble_type(instance):
    assert isinstance(instance.valueDouble, str)


@given(instance=moba::MobaConstantValue_strategy)
def test_moba::mobaconstantvalue_valueDouble_setter(instance):
    original = instance.valueDouble
    instance.valueDouble = original
    assert instance.valueDouble == original

@given(instance=moba::MobaConstantValue_strategy)
def test_moba::mobaconstantvalue_valueConstToLowerCase_type(instance):
    assert isinstance(instance.valueConstToLowerCase, bool)


@given(instance=moba::MobaConstantValue_strategy)
def test_moba::mobaconstantvalue_valueConstToLowerCase_setter(instance):
    original = instance.valueConstToLowerCase
    instance.valueConstToLowerCase = original
    assert instance.valueConstToLowerCase == original

@given(instance=moba::MobaConstantValue_strategy)
def test_moba::mobaconstantvalue_valueInt_type(instance):
    assert isinstance(instance.valueInt, str)


@given(instance=moba::MobaConstantValue_strategy)
def test_moba::mobaconstantvalue_valueInt_setter(instance):
    original = instance.valueInt
    instance.valueInt = original
    assert instance.valueInt == original

@given(instance=moba::MobaConstantValue_strategy)
def test_moba::mobaconstantvalue_valueString_type(instance):
    assert isinstance(instance.valueString, str)


@given(instance=moba::MobaConstantValue_strategy)
def test_moba::mobaconstantvalue_valueString_setter(instance):
    original = instance.valueString
    instance.valueString = original
    assert instance.valueString == original

@given(instance=moba::MobaProperty_strategy)
@settings(max_examples=50)
def test_moba::mobaproperty_instantiation(instance):
    assert isinstance(instance, moba::MobaProperty)

@given(instance=moba::MobaProperty_strategy)
def test_moba::mobaproperty_valueString_type(instance):
    assert isinstance(instance.valueString, str)


@given(instance=moba::MobaProperty_strategy)
def test_moba::mobaproperty_valueString_setter(instance):
    original = instance.valueString
    instance.valueString = original
    assert instance.valueString == original

@given(instance=moba::MobaProperty_strategy)
def test_moba::mobaproperty_keyString_type(instance):
    assert isinstance(instance.keyString, str)


@given(instance=moba::MobaProperty_strategy)
def test_moba::mobaproperty_keyString_setter(instance):
    original = instance.keyString
    instance.keyString = original
    assert instance.keyString == original

@given(instance=moba::MobaProperty_strategy)
def test_moba::mobaproperty_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=moba::MobaProperty_strategy)
def test_moba::mobaproperty_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=moba::MobaProperty_strategy)
def test_moba::mobaproperty_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=moba::MobaProperty_strategy)
def test_moba::mobaproperty_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=moba::MobaPropertiesAble_strategy)
@settings(max_examples=50)
def test_moba::mobapropertiesable_instantiation(instance):
    assert isinstance(instance, moba::MobaPropertiesAble)

@given(instance=moba::MobaGeneratorFeature_strategy)
@settings(max_examples=50)
def test_moba::mobageneratorfeature_instantiation(instance):
    assert isinstance(instance, moba::MobaGeneratorFeature)

@given(instance=MobaApplicationFeature_strategy)
@settings(max_examples=50)
def test_mobaapplicationfeature_instantiation(instance):
    assert isinstance(instance, MobaApplicationFeature)

@given(instance=moba::MobaSettings_strategy)
@settings(max_examples=50)
def test_moba::mobasettings_instantiation(instance):
    assert isinstance(instance, moba::MobaSettings)

@given(instance=moba::MobaSettings_strategy)
def test_moba::mobasettings_active_type(instance):
    assert isinstance(instance.active, bool)


@given(instance=moba::MobaSettings_strategy)
def test_moba::mobasettings_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original

@given(instance=moba::MobaSettings_strategy)
def test_moba::mobasettings_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=moba::MobaSettings_strategy)
def test_moba::mobasettings_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=moba::MobaTransportSerializationType_strategy)
@settings(max_examples=50)
def test_moba::mobatransportserializationtype_instantiation(instance):
    assert isinstance(instance, moba::MobaTransportSerializationType)

@given(instance=moba::MobaTransportSerializationType_strategy)
def test_moba::mobatransportserializationtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=moba::MobaTransportSerializationType_strategy)
def test_moba::mobatransportserializationtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=moba::MobaGenerator_strategy)
@settings(max_examples=50)
def test_moba::mobagenerator_instantiation(instance):
    assert isinstance(instance, moba::MobaGenerator)

@given(instance=moba::MobaGenerator_strategy)
def test_moba::mobagenerator_active_type(instance):
    assert isinstance(instance.active, bool)


@given(instance=moba::MobaGenerator_strategy)
def test_moba::mobagenerator_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original

@given(instance=moba::MobaGenerator_strategy)
def test_moba::mobagenerator_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=moba::MobaGenerator_strategy)
def test_moba::mobagenerator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=moba::MobaServer_strategy)
@settings(max_examples=50)
def test_moba::mobaserver_instantiation(instance):
    assert isinstance(instance, moba::MobaServer)

@given(instance=moba::MobaServer_strategy)
def test_moba::mobaserver_urlString_type(instance):
    assert isinstance(instance.urlString, str)


@given(instance=moba::MobaServer_strategy)
def test_moba::mobaserver_urlString_setter(instance):
    original = instance.urlString
    instance.urlString = original
    assert instance.urlString == original

@given(instance=moba::MobaServer_strategy)
def test_moba::mobaserver_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=moba::MobaServer_strategy)
def test_moba::mobaserver_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=moba::MobaData_strategy)
@settings(max_examples=50)
def test_moba::mobadata_instantiation(instance):
    assert isinstance(instance, moba::MobaData)

@given(instance=moba::MobaEnum_strategy)
@settings(max_examples=50)
def test_moba::mobaenum_instantiation(instance):
    assert isinstance(instance, moba::MobaEnum)

@given(instance=moba::MobaAuthorization_strategy)
@settings(max_examples=50)
def test_moba::mobaauthorization_instantiation(instance):
    assert isinstance(instance, moba::MobaAuthorization)

@given(instance=moba::MobaAuthorization_strategy)
def test_moba::mobaauthorization_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=moba::MobaAuthorization_strategy)
def test_moba::mobaauthorization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=moba::MobaConstant_strategy)
@settings(max_examples=50)
def test_moba::mobaconstant_instantiation(instance):
    assert isinstance(instance, moba::MobaConstant)

@given(instance=moba::MobaConstant_strategy)
def test_moba::mobaconstant_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=moba::MobaConstant_strategy)
def test_moba::mobaconstant_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=moba::MobaTrigger_strategy)
@settings(max_examples=50)
def test_moba::mobatrigger_instantiation(instance):
    assert isinstance(instance, moba::MobaTrigger)

@given(instance=moba::MobaTrigger_strategy)
def test_moba::mobatrigger_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=moba::MobaTrigger_strategy)
def test_moba::mobatrigger_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=moba::MobaExternalModule_strategy)
@settings(max_examples=50)
def test_moba::mobaexternalmodule_instantiation(instance):
    assert isinstance(instance, moba::MobaExternalModule)

@given(instance=moba::MobaExternalModule_strategy)
def test_moba::mobaexternalmodule_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=moba::MobaExternalModule_strategy)
def test_moba::mobaexternalmodule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=moba::MobaPersistenceType_strategy)
@settings(max_examples=50)
def test_moba::mobapersistencetype_instantiation(instance):
    assert isinstance(instance, moba::MobaPersistenceType)

@given(instance=moba::MobaPersistenceType_strategy)
def test_moba::mobapersistencetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=moba::MobaPersistenceType_strategy)
def test_moba::mobapersistencetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=moba::MobaREST_strategy)
@settings(max_examples=50)
def test_moba::mobarest_instantiation(instance):
    assert isinstance(instance, moba::MobaREST)

@given(instance=moba::MobaREST_strategy)
def test_moba::mobarest_bigData_type(instance):
    assert isinstance(instance.bigData, bool)


@given(instance=moba::MobaREST_strategy)
def test_moba::mobarest_bigData_setter(instance):
    original = instance.bigData
    instance.bigData = original
    assert instance.bigData == original

@given(instance=moba::MobaREST_strategy)
def test_moba::mobarest_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=moba::MobaREST_strategy)
def test_moba::mobarest_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=moba::MobaREST_strategy)
def test_moba::mobarest_path_type(instance):
    assert isinstance(instance.path, str)


@given(instance=moba::MobaREST_strategy)
def test_moba::mobarest_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=moba::MobaREST_strategy)
def test_moba::mobarest_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=moba::MobaREST_strategy)
def test_moba::mobarest_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=moba::MobaTemplate_strategy)
@settings(max_examples=50)
def test_moba::mobatemplate_instantiation(instance):
    assert isinstance(instance, moba::MobaTemplate)

@given(instance=moba::MobaTemplate_strategy)
def test_moba::mobatemplate_downloadTemplate_type(instance):
    assert isinstance(instance.downloadTemplate, str)


@given(instance=moba::MobaTemplate_strategy)
def test_moba::mobatemplate_downloadTemplate_setter(instance):
    original = instance.downloadTemplate
    instance.downloadTemplate = original
    assert instance.downloadTemplate == original

@given(instance=MobaConstraintable_strategy)
@settings(max_examples=50)
def test_mobaconstraintable_instantiation(instance):
    assert isinstance(instance, MobaConstraintable)

@given(instance=moba::MobaEntityAttribute_strategy)
@settings(max_examples=50)
def test_moba::mobaentityattribute_instantiation(instance):
    assert isinstance(instance, moba::MobaEntityAttribute)

@given(instance=moba::MobaEntityAttribute_strategy)
def test_moba::mobaentityattribute_formatString_type(instance):
    assert isinstance(instance.formatString, str)


@given(instance=moba::MobaEntityAttribute_strategy)
def test_moba::mobaentityattribute_formatString_setter(instance):
    original = instance.formatString
    instance.formatString = original
    assert instance.formatString == original

@given(instance=moba::MobaEntityAttribute_strategy)
def test_moba::mobaentityattribute_domainKey_type(instance):
    assert isinstance(instance.domainKey, bool)


@given(instance=moba::MobaEntityAttribute_strategy)
def test_moba::mobaentityattribute_domainKey_setter(instance):
    original = instance.domainKey
    instance.domainKey = original
    assert instance.domainKey == original

@given(instance=moba::MobaEntityAttribute_strategy)
def test_moba::mobaentityattribute_transient_type(instance):
    assert isinstance(instance.transient, bool)


@given(instance=moba::MobaEntityAttribute_strategy)
def test_moba::mobaentityattribute_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original

@given(instance=moba::MobaEntityAttribute_strategy)
def test_moba::mobaentityattribute_lazy_type(instance):
    assert isinstance(instance.lazy, bool)


@given(instance=moba::MobaEntityAttribute_strategy)
def test_moba::mobaentityattribute_lazy_setter(instance):
    original = instance.lazy
    instance.lazy = original
    assert instance.lazy == original

@given(instance=moba::MobaEntityAttribute_strategy)
def test_moba::mobaentityattribute_domainDescription_type(instance):
    assert isinstance(instance.domainDescription, bool)


@given(instance=moba::MobaEntityAttribute_strategy)
def test_moba::mobaentityattribute_domainDescription_setter(instance):
    original = instance.domainDescription
    instance.domainDescription = original
    assert instance.domainDescription == original

@given(instance=moba::MobaSettingsAttribute_strategy)
@settings(max_examples=50)
def test_moba::mobasettingsattribute_instantiation(instance):
    assert isinstance(instance, moba::MobaSettingsAttribute)

@given(instance=moba::MobaSettingsAttribute_strategy)
def test_moba::mobasettingsattribute_formatString_type(instance):
    assert isinstance(instance.formatString, str)


@given(instance=moba::MobaSettingsAttribute_strategy)
def test_moba::mobasettingsattribute_formatString_setter(instance):
    original = instance.formatString
    instance.formatString = original
    assert instance.formatString == original

@given(instance=moba::MobaSettingsAttribute_strategy)
def test_moba::mobasettingsattribute_domainDescription_type(instance):
    assert isinstance(instance.domainDescription, bool)


@given(instance=moba::MobaSettingsAttribute_strategy)
def test_moba::mobasettingsattribute_domainDescription_setter(instance):
    original = instance.domainDescription
    instance.domainDescription = original
    assert instance.domainDescription == original

@given(instance=moba::MobaSettingsAttribute_strategy)
def test_moba::mobasettingsattribute_lazy_type(instance):
    assert isinstance(instance.lazy, bool)


@given(instance=moba::MobaSettingsAttribute_strategy)
def test_moba::mobasettingsattribute_lazy_setter(instance):
    original = instance.lazy
    instance.lazy = original
    assert instance.lazy == original

@given(instance=moba::MobaSettingsAttribute_strategy)
def test_moba::mobasettingsattribute_transient_type(instance):
    assert isinstance(instance.transient, bool)


@given(instance=moba::MobaSettingsAttribute_strategy)
def test_moba::mobasettingsattribute_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original

@given(instance=moba::MobaSettingsAttribute_strategy)
def test_moba::mobasettingsattribute_domainKey_type(instance):
    assert isinstance(instance.domainKey, bool)


@given(instance=moba::MobaSettingsAttribute_strategy)
def test_moba::mobasettingsattribute_domainKey_setter(instance):
    original = instance.domainKey
    instance.domainKey = original
    assert instance.domainKey == original

@given(instance=moba::MobaDtoAttribute_strategy)
@settings(max_examples=50)
def test_moba::mobadtoattribute_instantiation(instance):
    assert isinstance(instance, moba::MobaDtoAttribute)

@given(instance=moba::MobaDtoAttribute_strategy)
def test_moba::mobadtoattribute_alias_type(instance):
    assert isinstance(instance.alias, str)


@given(instance=moba::MobaDtoAttribute_strategy)
def test_moba::mobadtoattribute_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=moba::MobaDtoAttribute_strategy)
def test_moba::mobadtoattribute_domainDescription_type(instance):
    assert isinstance(instance.domainDescription, bool)


@given(instance=moba::MobaDtoAttribute_strategy)
def test_moba::mobadtoattribute_domainDescription_setter(instance):
    original = instance.domainDescription
    instance.domainDescription = original
    assert instance.domainDescription == original

@given(instance=moba::MobaDtoAttribute_strategy)
def test_moba::mobadtoattribute_lazy_type(instance):
    assert isinstance(instance.lazy, bool)


@given(instance=moba::MobaDtoAttribute_strategy)
def test_moba::mobadtoattribute_lazy_setter(instance):
    original = instance.lazy
    instance.lazy = original
    assert instance.lazy == original

@given(instance=moba::MobaDtoAttribute_strategy)
def test_moba::mobadtoattribute_domainKey_type(instance):
    assert isinstance(instance.domainKey, bool)


@given(instance=moba::MobaDtoAttribute_strategy)
def test_moba::mobadtoattribute_domainKey_setter(instance):
    original = instance.domainKey
    instance.domainKey = original
    assert instance.domainKey == original

@given(instance=moba::MobaDtoAttribute_strategy)
def test_moba::mobadtoattribute_transient_type(instance):
    assert isinstance(instance.transient, bool)


@given(instance=moba::MobaDtoAttribute_strategy)
def test_moba::mobadtoattribute_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original

@given(instance=moba::MobaDtoAttribute_strategy)
def test_moba::mobadtoattribute_formatString_type(instance):
    assert isinstance(instance.formatString, str)


@given(instance=moba::MobaDtoAttribute_strategy)
def test_moba::mobadtoattribute_formatString_setter(instance):
    original = instance.formatString
    instance.formatString = original
    assert instance.formatString == original

@given(instance=moba::MobaSettingsEntityReference_strategy)
@settings(max_examples=50)
def test_moba::mobasettingsentityreference_instantiation(instance):
    assert isinstance(instance, moba::MobaSettingsEntityReference)

@given(instance=moba::MobaSettingsEntityReference_strategy)
def test_moba::mobasettingsentityreference_lazy_type(instance):
    assert isinstance(instance.lazy, bool)


@given(instance=moba::MobaSettingsEntityReference_strategy)
def test_moba::mobasettingsentityreference_lazy_setter(instance):
    original = instance.lazy
    instance.lazy = original
    assert instance.lazy == original

@given(instance=moba::MobaSettingsEntityReference_strategy)
def test_moba::mobasettingsentityreference_transient_type(instance):
    assert isinstance(instance.transient, bool)


@given(instance=moba::MobaSettingsEntityReference_strategy)
def test_moba::mobasettingsentityreference_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original

@given(instance=moba::MobaSettingsEntityReference_strategy)
def test_moba::mobasettingsentityreference_cascading_type(instance):
    assert isinstance(instance.cascading, bool)


@given(instance=moba::MobaSettingsEntityReference_strategy)
def test_moba::mobasettingsentityreference_cascading_setter(instance):
    original = instance.cascading
    instance.cascading = original
    assert instance.cascading == original

@given(instance=moba::MobaDataType_strategy)
@settings(max_examples=50)
def test_moba::mobadatatype_instantiation(instance):
    assert isinstance(instance, moba::MobaDataType)

@given(instance=moba::MobaDataType_strategy)
def test_moba::mobadatatype_primitive_type(instance):
    assert isinstance(instance.primitive, bool)


@given(instance=moba::MobaDataType_strategy)
def test_moba::mobadatatype_primitive_setter(instance):
    original = instance.primitive
    instance.primitive = original
    assert instance.primitive == original

@given(instance=moba::MobaDataType_strategy)
def test_moba::mobadatatype_string_type(instance):
    assert isinstance(instance.string, bool)


@given(instance=moba::MobaDataType_strategy)
def test_moba::mobadatatype_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original

@given(instance=moba::MobaDataType_strategy)
def test_moba::mobadatatype_timestamp_type(instance):
    assert isinstance(instance.timestamp, bool)


@given(instance=moba::MobaDataType_strategy)
def test_moba::mobadatatype_timestamp_setter(instance):
    original = instance.timestamp
    instance.timestamp = original
    assert instance.timestamp == original

@given(instance=moba::MobaDataType_strategy)
def test_moba::mobadatatype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=moba::MobaDataType_strategy)
def test_moba::mobadatatype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=moba::MobaDataType_strategy)
def test_moba::mobadatatype_bool_type(instance):
    assert isinstance(instance.bool, bool)


@given(instance=moba::MobaDataType_strategy)
def test_moba::mobadatatype_bool_setter(instance):
    original = instance.bool
    instance.bool = original
    assert instance.bool == original

@given(instance=moba::MobaDataType_strategy)
def test_moba::mobadatatype_numeric_type(instance):
    assert isinstance(instance.numeric, bool)


@given(instance=moba::MobaDataType_strategy)
def test_moba::mobadatatype_numeric_setter(instance):
    original = instance.numeric
    instance.numeric = original
    assert instance.numeric == original

@given(instance=moba::MobaDataType_strategy)
def test_moba::mobadatatype_decimal_type(instance):
    assert isinstance(instance.decimal, bool)


@given(instance=moba::MobaDataType_strategy)
def test_moba::mobadatatype_decimal_setter(instance):
    original = instance.decimal
    instance.decimal = original
    assert instance.decimal == original

@given(instance=moba::MobaDataType_strategy)
def test_moba::mobadatatype_time_type(instance):
    assert isinstance(instance.time, bool)


@given(instance=moba::MobaDataType_strategy)
def test_moba::mobadatatype_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=moba::MobaDataType_strategy)
def test_moba::mobadatatype_array_type(instance):
    assert isinstance(instance.array, bool)


@given(instance=moba::MobaDataType_strategy)
def test_moba::mobadatatype_array_setter(instance):
    original = instance.array
    instance.array = original
    assert instance.array == original

@given(instance=moba::MobaDataType_strategy)
def test_moba::mobadatatype_dateFormatString_type(instance):
    assert isinstance(instance.dateFormatString, str)


@given(instance=moba::MobaDataType_strategy)
def test_moba::mobadatatype_dateFormatString_setter(instance):
    original = instance.dateFormatString
    instance.dateFormatString = original
    assert instance.dateFormatString == original

@given(instance=moba::MobaDataType_strategy)
def test_moba::mobadatatype_date_type(instance):
    assert isinstance(instance.date, bool)


@given(instance=moba::MobaDataType_strategy)
def test_moba::mobadatatype_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=moba::MobaDataType_strategy)
def test_moba::mobadatatype_predefined_type(instance):
    assert isinstance(instance.predefined, bool)


@given(instance=moba::MobaDataType_strategy)
def test_moba::mobadatatype_predefined_setter(instance):
    original = instance.predefined
    instance.predefined = original
    assert instance.predefined == original

@given(instance=moba::MobaGeneratorSlot_strategy)
@settings(max_examples=50)
def test_moba::mobageneratorslot_instantiation(instance):
    assert isinstance(instance, moba::MobaGeneratorSlot)

@given(instance=moba::MobaGeneratorSlot_strategy)
def test_moba::mobageneratorslot_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=moba::MobaGeneratorSlot_strategy)
def test_moba::mobageneratorslot_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=moba::MobaGeneratorSlot_strategy)
def test_moba::mobageneratorslot_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=moba::MobaGeneratorSlot_strategy)
def test_moba::mobageneratorslot_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=MobaGeneratorFeature_strategy)
@settings(max_examples=50)
def test_mobageneratorfeature_instantiation(instance):
    assert isinstance(instance, MobaGeneratorFeature)

@given(instance=moba::MobaGeneratorIDFeature_strategy)
@settings(max_examples=50)
def test_moba::mobageneratoridfeature_instantiation(instance):
    assert isinstance(instance, moba::MobaGeneratorIDFeature)

@given(instance=moba::MobaGeneratorIDFeature_strategy)
def test_moba::mobageneratoridfeature_generatorId_type(instance):
    assert isinstance(instance.generatorId, str)


@given(instance=moba::MobaGeneratorIDFeature_strategy)
def test_moba::mobageneratoridfeature_generatorId_setter(instance):
    original = instance.generatorId
    instance.generatorId = original
    assert instance.generatorId == original

@given(instance=moba::MobaGeneratorIDFeature_strategy)
def test_moba::mobageneratoridfeature_generatorVersion_type(instance):
    assert isinstance(instance.generatorVersion, str)


@given(instance=moba::MobaGeneratorIDFeature_strategy)
def test_moba::mobageneratoridfeature_generatorVersion_setter(instance):
    original = instance.generatorVersion
    instance.generatorVersion = original
    assert instance.generatorVersion == original

@given(instance=moba::MobaGeneratorMixinFeature_strategy)
@settings(max_examples=50)
def test_moba::mobageneratormixinfeature_instantiation(instance):
    assert isinstance(instance, moba::MobaGeneratorMixinFeature)

@given(instance=MobaFriendsAble_strategy)
@settings(max_examples=50)
def test_mobafriendsable_instantiation(instance):
    assert isinstance(instance, MobaFriendsAble)

@given(instance=moba::MobaApplicationFeature_strategy)
@settings(max_examples=50)
def test_moba::mobaapplicationfeature_instantiation(instance):
    assert isinstance(instance, moba::MobaApplicationFeature)

@given(instance=moba::MobaFeature_strategy)
@settings(max_examples=50)
def test_moba::mobafeature_instantiation(instance):
    assert isinstance(instance, moba::MobaFeature)

@given(instance=moba::MobaFeature_strategy)
def test_moba::mobafeature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=moba::MobaFeature_strategy)
def test_moba::mobafeature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=moba::MobaModel_strategy)
@settings(max_examples=50)
def test_moba::mobamodel_instantiation(instance):
    assert isinstance(instance, moba::MobaModel)

@given(instance=moba::MobaModel_strategy)
def test_moba::mobamodel_copyright_type(instance):
    assert isinstance(instance.copyright, str)


@given(instance=moba::MobaModel_strategy)
def test_moba::mobamodel_copyright_setter(instance):
    original = instance.copyright
    instance.copyright = original
    assert instance.copyright == original

@given(instance=moba::MobaCache_strategy)
@settings(max_examples=50)
def test_moba::mobacache_instantiation(instance):
    assert isinstance(instance, moba::MobaCache)

@given(instance=moba::MobaCache_strategy)
def test_moba::mobacache_cacheIntervalInt_type(instance):
    assert isinstance(instance.cacheIntervalInt, int)


@given(instance=moba::MobaCache_strategy)
def test_moba::mobacache_cacheIntervalInt_setter(instance):
    original = instance.cacheIntervalInt
    instance.cacheIntervalInt = original
    assert instance.cacheIntervalInt == original

@given(instance=moba::MobaCache_strategy)
def test_moba::mobacache_cacheStrategyString_type(instance):
    assert isinstance(instance.cacheStrategyString, str)


@given(instance=moba::MobaCache_strategy)
def test_moba::mobacache_cacheStrategyString_setter(instance):
    original = instance.cacheStrategyString
    instance.cacheStrategyString = original
    assert instance.cacheStrategyString == original

@given(instance=moba::MobaCache_strategy)
def test_moba::mobacache_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=moba::MobaCache_strategy)
def test_moba::mobacache_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=moba::MobaCache_strategy)
def test_moba::mobacache_cacheTypeString_type(instance):
    assert isinstance(instance.cacheTypeString, str)


@given(instance=moba::MobaCache_strategy)
def test_moba::mobacache_cacheTypeString_setter(instance):
    original = instance.cacheTypeString
    instance.cacheTypeString = original
    assert instance.cacheTypeString == original

@given(instance=MobaModelFeature_strategy)
@settings(max_examples=50)
def test_mobamodelfeature_instantiation(instance):
    assert isinstance(instance, MobaModelFeature)

@given(instance=moba::MobaApplication_strategy)
@settings(max_examples=50)
def test_moba::mobaapplication_instantiation(instance):
    assert isinstance(instance, moba::MobaApplication)

@given(instance=moba::MobaApplication_strategy)
def test_moba::mobaapplication_javaPackage_type(instance):
    assert isinstance(instance.javaPackage, str)


@given(instance=moba::MobaApplication_strategy)
def test_moba::mobaapplication_javaPackage_setter(instance):
    original = instance.javaPackage
    instance.javaPackage = original
    assert instance.javaPackage == original

@given(instance=moba::MobaProject_strategy)
@settings(max_examples=50)
def test_moba::mobaproject_instantiation(instance):
    assert isinstance(instance, moba::MobaProject)

@given(instance=moba::MobaModelFeature_strategy)
@settings(max_examples=50)
def test_moba::mobamodelfeature_instantiation(instance):
    assert isinstance(instance, moba::MobaModelFeature)

@given(instance=moba::MobaModelFeature_strategy)
def test_moba::mobamodelfeature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=moba::MobaModelFeature_strategy)
def test_moba::mobamodelfeature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=moba::MobaModelFeature_strategy)
def test_moba::mobamodelfeature_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=moba::MobaModelFeature_strategy)
def test_moba::mobamodelfeature_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=moba::MobaModelFeature_strategy)
def test_moba::mobamodelfeature_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=moba::MobaModelFeature_strategy)
def test_moba::mobamodelfeature_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
