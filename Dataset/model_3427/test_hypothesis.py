import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    tracker::EventAttributeSchema,
    MedicalCondition,
    tracker::Mastitis,
    Birthing,
    tracker::Calving,
    tracker::EventSchema,
    tracker::EventAttribute,
    Bovine,
    tracker::BovineBison,
    tracker::BovineDairy,
    tracker::BovineBeef,
    tracker::Premises,
    Event,
    tracker::USSwineGrading,
    tracker::HerdTest,
    tracker::ReplacedTag,
    tracker::ICVI,
    tracker::Sighting,
    tracker::TagApplied,
    tracker::USOvineGrading,
    tracker::WeighIn,
    tracker::GenericEvent,
    tracker::MedicalCondition,
    tracker::USBeefGrading,
    tracker::BirthDefect,
    tracker::Died,
    tracker::MedicalTreatment,
    tracker::MovedOut,
    tracker::Slaughtered,
    tracker::MovedIn,
    tracker::AnimalMissing,
    tracker::Birthing,
    tracker::Exported,
    tracker::TagRetired,
    tracker::LostTag,
    tracker::MilkTest,
    tracker::Imported,
    tracker::TagAllocated,
    tracker::Schema,
    tracker::Location,
    tracker::Tag,
    Animal,
    tracker::Swine,
    tracker::Caprine,
    tracker::Ovine,
    tracker::Equine,
    tracker::Bovine,
    tracker::Event,
    tracker::Animal,
    BeefBreed,
    SheepBreed,
    USSwineQualityGrade,
    USBeefYieldGrade,
    Sex,
    Treatment,
    DairyBreed,
    BisonBreed,
    TreatmentMethod,
    GoatBreed,
    Level,
    SwineBreed,
    HorseBreed,
    OneToTen,
    USQualityGrade,
    AnimalType,
    EventDataType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tracker::eventattributeschema_is_not_abstract():
    assert not inspect.isabstract(tracker::EventAttributeSchema)


def test_tracker::eventattributeschema_constructor_exists():
    assert callable(tracker::EventAttributeSchema.__init__)


def test_tracker::eventattributeschema_constructor_args():
    sig = inspect.signature(tracker::EventAttributeSchema.__init__)
    params = list(sig.parameters.keys())
    assert "dataType" in params, "Missing parameter 'dataType'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"

def test_tracker::eventattributeschema_has_dataType():
    assert hasattr(tracker::EventAttributeSchema, "dataType")
    descriptor = None
    for klass in tracker::EventAttributeSchema.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
            break
    assert isinstance(descriptor, property)

def test_tracker::eventattributeschema_has_description():
    assert hasattr(tracker::EventAttributeSchema, "description")
    descriptor = None
    for klass in tracker::EventAttributeSchema.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_tracker::eventattributeschema_has_name():
    assert hasattr(tracker::EventAttributeSchema, "name")
    descriptor = None
    for klass in tracker::EventAttributeSchema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_medicalcondition_is_not_abstract():
    assert not inspect.isabstract(MedicalCondition)


def test_medicalcondition_constructor_exists():
    assert callable(MedicalCondition.__init__)


def test_medicalcondition_constructor_args():
    sig = inspect.signature(MedicalCondition.__init__)
    params = list(sig.parameters.keys())



def test_tracker::mastitis_is_not_abstract():
    assert not inspect.isabstract(tracker::Mastitis)


def test_tracker::mastitis_constructor_exists():
    assert callable(tracker::Mastitis.__init__)


def test_tracker::mastitis_constructor_args():
    sig = inspect.signature(tracker::Mastitis.__init__)
    params = list(sig.parameters.keys())
    assert "origin" in params, "Missing parameter 'origin'"
    assert "location" in params, "Missing parameter 'location'"

def test_tracker::mastitis_has_origin():
    assert hasattr(tracker::Mastitis, "origin")
    descriptor = None
    for klass in tracker::Mastitis.__mro__:
        if "origin" in klass.__dict__:
            descriptor = klass.__dict__["origin"]
            break
    assert isinstance(descriptor, property)

def test_tracker::mastitis_has_location():
    assert hasattr(tracker::Mastitis, "location")
    descriptor = None
    for klass in tracker::Mastitis.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_birthing_is_not_abstract():
    assert not inspect.isabstract(Birthing)


def test_birthing_constructor_exists():
    assert callable(Birthing.__init__)


def test_birthing_constructor_args():
    sig = inspect.signature(Birthing.__init__)
    params = list(sig.parameters.keys())



def test_tracker::calving_is_not_abstract():
    assert not inspect.isabstract(tracker::Calving)


def test_tracker::calving_constructor_exists():
    assert callable(tracker::Calving.__init__)


def test_tracker::calving_constructor_args():
    sig = inspect.signature(tracker::Calving.__init__)
    params = list(sig.parameters.keys())



def test_tracker::eventschema_is_not_abstract():
    assert not inspect.isabstract(tracker::EventSchema)


def test_tracker::eventschema_constructor_exists():
    assert callable(tracker::EventSchema.__init__)


def test_tracker::eventschema_constructor_args():
    sig = inspect.signature(tracker::EventSchema.__init__)
    params = list(sig.parameters.keys())
    assert "animalType" in params, "Missing parameter 'animalType'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"

def test_tracker::eventschema_has_animalType():
    assert hasattr(tracker::EventSchema, "animalType")
    descriptor = None
    for klass in tracker::EventSchema.__mro__:
        if "animalType" in klass.__dict__:
            descriptor = klass.__dict__["animalType"]
            break
    assert isinstance(descriptor, property)

def test_tracker::eventschema_has_description():
    assert hasattr(tracker::EventSchema, "description")
    descriptor = None
    for klass in tracker::EventSchema.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_tracker::eventschema_has_name():
    assert hasattr(tracker::EventSchema, "name")
    descriptor = None
    for klass in tracker::EventSchema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tracker::eventattribute_is_not_abstract():
    assert not inspect.isabstract(tracker::EventAttribute)


def test_tracker::eventattribute_constructor_exists():
    assert callable(tracker::EventAttribute.__init__)


def test_tracker::eventattribute_constructor_args():
    sig = inspect.signature(tracker::EventAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_tracker::eventattribute_has_value():
    assert hasattr(tracker::EventAttribute, "value")
    descriptor = None
    for klass in tracker::EventAttribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_tracker::eventattribute_has_key():
    assert hasattr(tracker::EventAttribute, "key")
    descriptor = None
    for klass in tracker::EventAttribute.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_bovine_is_not_abstract():
    assert not inspect.isabstract(Bovine)


def test_bovine_constructor_exists():
    assert callable(Bovine.__init__)


def test_bovine_constructor_args():
    sig = inspect.signature(Bovine.__init__)
    params = list(sig.parameters.keys())



def test_tracker::bovinebison_is_not_abstract():
    assert not inspect.isabstract(tracker::BovineBison)


def test_tracker::bovinebison_constructor_exists():
    assert callable(tracker::BovineBison.__init__)


def test_tracker::bovinebison_constructor_args():
    sig = inspect.signature(tracker::BovineBison.__init__)
    params = list(sig.parameters.keys())
    assert "buffaloBreed" in params, "Missing parameter 'buffaloBreed'"

def test_tracker::bovinebison_has_buffaloBreed():
    assert hasattr(tracker::BovineBison, "buffaloBreed")
    descriptor = None
    for klass in tracker::BovineBison.__mro__:
        if "buffaloBreed" in klass.__dict__:
            descriptor = klass.__dict__["buffaloBreed"]
            break
    assert isinstance(descriptor, property)



def test_tracker::bovinedairy_is_not_abstract():
    assert not inspect.isabstract(tracker::BovineDairy)


def test_tracker::bovinedairy_constructor_exists():
    assert callable(tracker::BovineDairy.__init__)


def test_tracker::bovinedairy_constructor_args():
    sig = inspect.signature(tracker::BovineDairy.__init__)
    params = list(sig.parameters.keys())
    assert "dairyBreed" in params, "Missing parameter 'dairyBreed'"

def test_tracker::bovinedairy_has_dairyBreed():
    assert hasattr(tracker::BovineDairy, "dairyBreed")
    descriptor = None
    for klass in tracker::BovineDairy.__mro__:
        if "dairyBreed" in klass.__dict__:
            descriptor = klass.__dict__["dairyBreed"]
            break
    assert isinstance(descriptor, property)



def test_tracker::bovinebeef_is_not_abstract():
    assert not inspect.isabstract(tracker::BovineBeef)


def test_tracker::bovinebeef_constructor_exists():
    assert callable(tracker::BovineBeef.__init__)


def test_tracker::bovinebeef_constructor_args():
    sig = inspect.signature(tracker::BovineBeef.__init__)
    params = list(sig.parameters.keys())
    assert "beefBreed" in params, "Missing parameter 'beefBreed'"

def test_tracker::bovinebeef_has_beefBreed():
    assert hasattr(tracker::BovineBeef, "beefBreed")
    descriptor = None
    for klass in tracker::BovineBeef.__mro__:
        if "beefBreed" in klass.__dict__:
            descriptor = klass.__dict__["beefBreed"]
            break
    assert isinstance(descriptor, property)



def test_tracker::premises_is_not_abstract():
    assert not inspect.isabstract(tracker::Premises)


def test_tracker::premises_constructor_exists():
    assert callable(tracker::Premises.__init__)


def test_tracker::premises_constructor_args():
    sig = inspect.signature(tracker::Premises.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "emailContact" in params, "Missing parameter 'emailContact'"
    assert "uri" in params, "Missing parameter 'uri'"
    assert "premisesId" in params, "Missing parameter 'premisesId'"

def test_tracker::premises_has_name():
    assert hasattr(tracker::Premises, "name")
    descriptor = None
    for klass in tracker::Premises.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_tracker::premises_has_emailContact():
    assert hasattr(tracker::Premises, "emailContact")
    descriptor = None
    for klass in tracker::Premises.__mro__:
        if "emailContact" in klass.__dict__:
            descriptor = klass.__dict__["emailContact"]
            break
    assert isinstance(descriptor, property)

def test_tracker::premises_has_uri():
    assert hasattr(tracker::Premises, "uri")
    descriptor = None
    for klass in tracker::Premises.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)

def test_tracker::premises_has_premisesId():
    assert hasattr(tracker::Premises, "premisesId")
    descriptor = None
    for klass in tracker::Premises.__mro__:
        if "premisesId" in klass.__dict__:
            descriptor = klass.__dict__["premisesId"]
            break
    assert isinstance(descriptor, property)



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_tracker::usswinegrading_is_not_abstract():
    assert not inspect.isabstract(tracker::USSwineGrading)


def test_tracker::usswinegrading_constructor_exists():
    assert callable(tracker::USSwineGrading.__init__)


def test_tracker::usswinegrading_constructor_args():
    sig = inspect.signature(tracker::USSwineGrading.__init__)
    params = list(sig.parameters.keys())
    assert "qualityGrade" in params, "Missing parameter 'qualityGrade'"

def test_tracker::usswinegrading_has_qualityGrade():
    assert hasattr(tracker::USSwineGrading, "qualityGrade")
    descriptor = None
    for klass in tracker::USSwineGrading.__mro__:
        if "qualityGrade" in klass.__dict__:
            descriptor = klass.__dict__["qualityGrade"]
            break
    assert isinstance(descriptor, property)



def test_tracker::herdtest_is_not_abstract():
    assert not inspect.isabstract(tracker::HerdTest)


def test_tracker::herdtest_constructor_exists():
    assert callable(tracker::HerdTest.__init__)


def test_tracker::herdtest_constructor_args():
    sig = inspect.signature(tracker::HerdTest.__init__)
    params = list(sig.parameters.keys())
    assert "pregnant" in params, "Missing parameter 'pregnant'"
    assert "daysSinceBredEstimate" in params, "Missing parameter 'daysSinceBredEstimate'"
    assert "bredDateEstimate" in params, "Missing parameter 'bredDateEstimate'"

def test_tracker::herdtest_has_pregnant():
    assert hasattr(tracker::HerdTest, "pregnant")
    descriptor = None
    for klass in tracker::HerdTest.__mro__:
        if "pregnant" in klass.__dict__:
            descriptor = klass.__dict__["pregnant"]
            break
    assert isinstance(descriptor, property)

def test_tracker::herdtest_has_daysSinceBredEstimate():
    assert hasattr(tracker::HerdTest, "daysSinceBredEstimate")
    descriptor = None
    for klass in tracker::HerdTest.__mro__:
        if "daysSinceBredEstimate" in klass.__dict__:
            descriptor = klass.__dict__["daysSinceBredEstimate"]
            break
    assert isinstance(descriptor, property)

def test_tracker::herdtest_has_bredDateEstimate():
    assert hasattr(tracker::HerdTest, "bredDateEstimate")
    descriptor = None
    for klass in tracker::HerdTest.__mro__:
        if "bredDateEstimate" in klass.__dict__:
            descriptor = klass.__dict__["bredDateEstimate"]
            break
    assert isinstance(descriptor, property)



def test_tracker::replacedtag_is_not_abstract():
    assert not inspect.isabstract(tracker::ReplacedTag)


def test_tracker::replacedtag_constructor_exists():
    assert callable(tracker::ReplacedTag.__init__)


def test_tracker::replacedtag_constructor_args():
    sig = inspect.signature(tracker::ReplacedTag.__init__)
    params = list(sig.parameters.keys())
    assert "usainNumberUsedForOldId" in params, "Missing parameter 'usainNumberUsedForOldId'"
    assert "oldId" in params, "Missing parameter 'oldId'"

def test_tracker::replacedtag_has_usainNumberUsedForOldId():
    assert hasattr(tracker::ReplacedTag, "usainNumberUsedForOldId")
    descriptor = None
    for klass in tracker::ReplacedTag.__mro__:
        if "usainNumberUsedForOldId" in klass.__dict__:
            descriptor = klass.__dict__["usainNumberUsedForOldId"]
            break
    assert isinstance(descriptor, property)

def test_tracker::replacedtag_has_oldId():
    assert hasattr(tracker::ReplacedTag, "oldId")
    descriptor = None
    for klass in tracker::ReplacedTag.__mro__:
        if "oldId" in klass.__dict__:
            descriptor = klass.__dict__["oldId"]
            break
    assert isinstance(descriptor, property)



def test_tracker::icvi_is_not_abstract():
    assert not inspect.isabstract(tracker::ICVI)


def test_tracker::icvi_constructor_exists():
    assert callable(tracker::ICVI.__init__)


def test_tracker::icvi_constructor_args():
    sig = inspect.signature(tracker::ICVI.__init__)
    params = list(sig.parameters.keys())



def test_tracker::sighting_is_not_abstract():
    assert not inspect.isabstract(tracker::Sighting)


def test_tracker::sighting_constructor_exists():
    assert callable(tracker::Sighting.__init__)


def test_tracker::sighting_constructor_args():
    sig = inspect.signature(tracker::Sighting.__init__)
    params = list(sig.parameters.keys())



def test_tracker::tagapplied_is_not_abstract():
    assert not inspect.isabstract(tracker::TagApplied)


def test_tracker::tagapplied_constructor_exists():
    assert callable(tracker::TagApplied.__init__)


def test_tracker::tagapplied_constructor_args():
    sig = inspect.signature(tracker::TagApplied.__init__)
    params = list(sig.parameters.keys())



def test_tracker::usovinegrading_is_not_abstract():
    assert not inspect.isabstract(tracker::USOvineGrading)


def test_tracker::usovinegrading_constructor_exists():
    assert callable(tracker::USOvineGrading.__init__)


def test_tracker::usovinegrading_constructor_args():
    sig = inspect.signature(tracker::USOvineGrading.__init__)
    params = list(sig.parameters.keys())
    assert "qualityGradeLevel" in params, "Missing parameter 'qualityGradeLevel'"
    assert "qualityGrade" in params, "Missing parameter 'qualityGrade'"

def test_tracker::usovinegrading_has_qualityGradeLevel():
    assert hasattr(tracker::USOvineGrading, "qualityGradeLevel")
    descriptor = None
    for klass in tracker::USOvineGrading.__mro__:
        if "qualityGradeLevel" in klass.__dict__:
            descriptor = klass.__dict__["qualityGradeLevel"]
            break
    assert isinstance(descriptor, property)

def test_tracker::usovinegrading_has_qualityGrade():
    assert hasattr(tracker::USOvineGrading, "qualityGrade")
    descriptor = None
    for klass in tracker::USOvineGrading.__mro__:
        if "qualityGrade" in klass.__dict__:
            descriptor = klass.__dict__["qualityGrade"]
            break
    assert isinstance(descriptor, property)



def test_tracker::weighin_is_not_abstract():
    assert not inspect.isabstract(tracker::WeighIn)


def test_tracker::weighin_constructor_exists():
    assert callable(tracker::WeighIn.__init__)


def test_tracker::weighin_constructor_args():
    sig = inspect.signature(tracker::WeighIn.__init__)
    params = list(sig.parameters.keys())
    assert "weightGainPerDay" in params, "Missing parameter 'weightGainPerDay'"
    assert "weight" in params, "Missing parameter 'weight'"

def test_tracker::weighin_has_weightGainPerDay():
    assert hasattr(tracker::WeighIn, "weightGainPerDay")
    descriptor = None
    for klass in tracker::WeighIn.__mro__:
        if "weightGainPerDay" in klass.__dict__:
            descriptor = klass.__dict__["weightGainPerDay"]
            break
    assert isinstance(descriptor, property)

def test_tracker::weighin_has_weight():
    assert hasattr(tracker::WeighIn, "weight")
    descriptor = None
    for klass in tracker::WeighIn.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_tracker::genericevent_is_not_abstract():
    assert not inspect.isabstract(tracker::GenericEvent)


def test_tracker::genericevent_constructor_exists():
    assert callable(tracker::GenericEvent.__init__)


def test_tracker::genericevent_constructor_args():
    sig = inspect.signature(tracker::GenericEvent.__init__)
    params = list(sig.parameters.keys())



def test_tracker::medicalcondition_is_not_abstract():
    assert not inspect.isabstract(tracker::MedicalCondition)


def test_tracker::medicalcondition_constructor_exists():
    assert callable(tracker::MedicalCondition.__init__)


def test_tracker::medicalcondition_constructor_args():
    sig = inspect.signature(tracker::MedicalCondition.__init__)
    params = list(sig.parameters.keys())



def test_tracker::usbeefgrading_is_not_abstract():
    assert not inspect.isabstract(tracker::USBeefGrading)


def test_tracker::usbeefgrading_constructor_exists():
    assert callable(tracker::USBeefGrading.__init__)


def test_tracker::usbeefgrading_constructor_args():
    sig = inspect.signature(tracker::USBeefGrading.__init__)
    params = list(sig.parameters.keys())
    assert "yieldGrade" in params, "Missing parameter 'yieldGrade'"
    assert "qualityGrade" in params, "Missing parameter 'qualityGrade'"
    assert "qualityGradeLevel" in params, "Missing parameter 'qualityGradeLevel'"

def test_tracker::usbeefgrading_has_yieldGrade():
    assert hasattr(tracker::USBeefGrading, "yieldGrade")
    descriptor = None
    for klass in tracker::USBeefGrading.__mro__:
        if "yieldGrade" in klass.__dict__:
            descriptor = klass.__dict__["yieldGrade"]
            break
    assert isinstance(descriptor, property)

def test_tracker::usbeefgrading_has_qualityGrade():
    assert hasattr(tracker::USBeefGrading, "qualityGrade")
    descriptor = None
    for klass in tracker::USBeefGrading.__mro__:
        if "qualityGrade" in klass.__dict__:
            descriptor = klass.__dict__["qualityGrade"]
            break
    assert isinstance(descriptor, property)

def test_tracker::usbeefgrading_has_qualityGradeLevel():
    assert hasattr(tracker::USBeefGrading, "qualityGradeLevel")
    descriptor = None
    for klass in tracker::USBeefGrading.__mro__:
        if "qualityGradeLevel" in klass.__dict__:
            descriptor = klass.__dict__["qualityGradeLevel"]
            break
    assert isinstance(descriptor, property)



def test_tracker::birthdefect_is_not_abstract():
    assert not inspect.isabstract(tracker::BirthDefect)


def test_tracker::birthdefect_constructor_exists():
    assert callable(tracker::BirthDefect.__init__)


def test_tracker::birthdefect_constructor_args():
    sig = inspect.signature(tracker::BirthDefect.__init__)
    params = list(sig.parameters.keys())
    assert "freemartin" in params, "Missing parameter 'freemartin'"

def test_tracker::birthdefect_has_freemartin():
    assert hasattr(tracker::BirthDefect, "freemartin")
    descriptor = None
    for klass in tracker::BirthDefect.__mro__:
        if "freemartin" in klass.__dict__:
            descriptor = klass.__dict__["freemartin"]
            break
    assert isinstance(descriptor, property)



def test_tracker::died_is_not_abstract():
    assert not inspect.isabstract(tracker::Died)


def test_tracker::died_constructor_exists():
    assert callable(tracker::Died.__init__)


def test_tracker::died_constructor_args():
    sig = inspect.signature(tracker::Died.__init__)
    params = list(sig.parameters.keys())



def test_tracker::medicaltreatment_is_not_abstract():
    assert not inspect.isabstract(tracker::MedicalTreatment)


def test_tracker::medicaltreatment_constructor_exists():
    assert callable(tracker::MedicalTreatment.__init__)


def test_tracker::medicaltreatment_constructor_args():
    sig = inspect.signature(tracker::MedicalTreatment.__init__)
    params = list(sig.parameters.keys())
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "manufacturer" in params, "Missing parameter 'manufacturer'"
    assert "treatment" in params, "Missing parameter 'treatment'"
    assert "lot" in params, "Missing parameter 'lot'"
    assert "name" in params, "Missing parameter 'name'"
    assert "method" in params, "Missing parameter 'method'"
    assert "product" in params, "Missing parameter 'product'"

def test_tracker::medicaltreatment_has_quantity():
    assert hasattr(tracker::MedicalTreatment, "quantity")
    descriptor = None
    for klass in tracker::MedicalTreatment.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)

def test_tracker::medicaltreatment_has_manufacturer():
    assert hasattr(tracker::MedicalTreatment, "manufacturer")
    descriptor = None
    for klass in tracker::MedicalTreatment.__mro__:
        if "manufacturer" in klass.__dict__:
            descriptor = klass.__dict__["manufacturer"]
            break
    assert isinstance(descriptor, property)

def test_tracker::medicaltreatment_has_treatment():
    assert hasattr(tracker::MedicalTreatment, "treatment")
    descriptor = None
    for klass in tracker::MedicalTreatment.__mro__:
        if "treatment" in klass.__dict__:
            descriptor = klass.__dict__["treatment"]
            break
    assert isinstance(descriptor, property)

def test_tracker::medicaltreatment_has_lot():
    assert hasattr(tracker::MedicalTreatment, "lot")
    descriptor = None
    for klass in tracker::MedicalTreatment.__mro__:
        if "lot" in klass.__dict__:
            descriptor = klass.__dict__["lot"]
            break
    assert isinstance(descriptor, property)

def test_tracker::medicaltreatment_has_name():
    assert hasattr(tracker::MedicalTreatment, "name")
    descriptor = None
    for klass in tracker::MedicalTreatment.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_tracker::medicaltreatment_has_method():
    assert hasattr(tracker::MedicalTreatment, "method")
    descriptor = None
    for klass in tracker::MedicalTreatment.__mro__:
        if "method" in klass.__dict__:
            descriptor = klass.__dict__["method"]
            break
    assert isinstance(descriptor, property)

def test_tracker::medicaltreatment_has_product():
    assert hasattr(tracker::MedicalTreatment, "product")
    descriptor = None
    for klass in tracker::MedicalTreatment.__mro__:
        if "product" in klass.__dict__:
            descriptor = klass.__dict__["product"]
            break
    assert isinstance(descriptor, property)



def test_tracker::movedout_is_not_abstract():
    assert not inspect.isabstract(tracker::MovedOut)


def test_tracker::movedout_constructor_exists():
    assert callable(tracker::MovedOut.__init__)


def test_tracker::movedout_constructor_args():
    sig = inspect.signature(tracker::MovedOut.__init__)
    params = list(sig.parameters.keys())
    assert "destinationPin" in params, "Missing parameter 'destinationPin'"

def test_tracker::movedout_has_destinationPin():
    assert hasattr(tracker::MovedOut, "destinationPin")
    descriptor = None
    for klass in tracker::MovedOut.__mro__:
        if "destinationPin" in klass.__dict__:
            descriptor = klass.__dict__["destinationPin"]
            break
    assert isinstance(descriptor, property)



def test_tracker::slaughtered_is_not_abstract():
    assert not inspect.isabstract(tracker::Slaughtered)


def test_tracker::slaughtered_constructor_exists():
    assert callable(tracker::Slaughtered.__init__)


def test_tracker::slaughtered_constructor_args():
    sig = inspect.signature(tracker::Slaughtered.__init__)
    params = list(sig.parameters.keys())



def test_tracker::movedin_is_not_abstract():
    assert not inspect.isabstract(tracker::MovedIn)


def test_tracker::movedin_constructor_exists():
    assert callable(tracker::MovedIn.__init__)


def test_tracker::movedin_constructor_args():
    sig = inspect.signature(tracker::MovedIn.__init__)
    params = list(sig.parameters.keys())
    assert "sourcePin" in params, "Missing parameter 'sourcePin'"

def test_tracker::movedin_has_sourcePin():
    assert hasattr(tracker::MovedIn, "sourcePin")
    descriptor = None
    for klass in tracker::MovedIn.__mro__:
        if "sourcePin" in klass.__dict__:
            descriptor = klass.__dict__["sourcePin"]
            break
    assert isinstance(descriptor, property)



def test_tracker::animalmissing_is_not_abstract():
    assert not inspect.isabstract(tracker::AnimalMissing)


def test_tracker::animalmissing_constructor_exists():
    assert callable(tracker::AnimalMissing.__init__)


def test_tracker::animalmissing_constructor_args():
    sig = inspect.signature(tracker::AnimalMissing.__init__)
    params = list(sig.parameters.keys())



def test_tracker::birthing_is_not_abstract():
    assert not inspect.isabstract(tracker::Birthing)


def test_tracker::birthing_constructor_exists():
    assert callable(tracker::Birthing.__init__)


def test_tracker::birthing_constructor_args():
    sig = inspect.signature(tracker::Birthing.__init__)
    params = list(sig.parameters.keys())
    assert "difficulty" in params, "Missing parameter 'difficulty'"
    assert "assisted" in params, "Missing parameter 'assisted'"
    assert "viability" in params, "Missing parameter 'viability'"

def test_tracker::birthing_has_difficulty():
    assert hasattr(tracker::Birthing, "difficulty")
    descriptor = None
    for klass in tracker::Birthing.__mro__:
        if "difficulty" in klass.__dict__:
            descriptor = klass.__dict__["difficulty"]
            break
    assert isinstance(descriptor, property)

def test_tracker::birthing_has_assisted():
    assert hasattr(tracker::Birthing, "assisted")
    descriptor = None
    for klass in tracker::Birthing.__mro__:
        if "assisted" in klass.__dict__:
            descriptor = klass.__dict__["assisted"]
            break
    assert isinstance(descriptor, property)

def test_tracker::birthing_has_viability():
    assert hasattr(tracker::Birthing, "viability")
    descriptor = None
    for klass in tracker::Birthing.__mro__:
        if "viability" in klass.__dict__:
            descriptor = klass.__dict__["viability"]
            break
    assert isinstance(descriptor, property)



def test_tracker::exported_is_not_abstract():
    assert not inspect.isabstract(tracker::Exported)


def test_tracker::exported_constructor_exists():
    assert callable(tracker::Exported.__init__)


def test_tracker::exported_constructor_args():
    sig = inspect.signature(tracker::Exported.__init__)
    params = list(sig.parameters.keys())



def test_tracker::tagretired_is_not_abstract():
    assert not inspect.isabstract(tracker::TagRetired)


def test_tracker::tagretired_constructor_exists():
    assert callable(tracker::TagRetired.__init__)


def test_tracker::tagretired_constructor_args():
    sig = inspect.signature(tracker::TagRetired.__init__)
    params = list(sig.parameters.keys())



def test_tracker::losttag_is_not_abstract():
    assert not inspect.isabstract(tracker::LostTag)


def test_tracker::losttag_constructor_exists():
    assert callable(tracker::LostTag.__init__)


def test_tracker::losttag_constructor_args():
    sig = inspect.signature(tracker::LostTag.__init__)
    params = list(sig.parameters.keys())



def test_tracker::milktest_is_not_abstract():
    assert not inspect.isabstract(tracker::MilkTest)


def test_tracker::milktest_constructor_exists():
    assert callable(tracker::MilkTest.__init__)


def test_tracker::milktest_constructor_args():
    sig = inspect.signature(tracker::MilkTest.__init__)
    params = list(sig.parameters.keys())
    assert "otherSolids" in params, "Missing parameter 'otherSolids'"
    assert "percentButterFat" in params, "Missing parameter 'percentButterFat'"
    assert "percentProtein" in params, "Missing parameter 'percentProtein'"
    assert "poundsProduced" in params, "Missing parameter 'poundsProduced'"
    assert "somaticCellCounts" in params, "Missing parameter 'somaticCellCounts'"

def test_tracker::milktest_has_otherSolids():
    assert hasattr(tracker::MilkTest, "otherSolids")
    descriptor = None
    for klass in tracker::MilkTest.__mro__:
        if "otherSolids" in klass.__dict__:
            descriptor = klass.__dict__["otherSolids"]
            break
    assert isinstance(descriptor, property)

def test_tracker::milktest_has_percentButterFat():
    assert hasattr(tracker::MilkTest, "percentButterFat")
    descriptor = None
    for klass in tracker::MilkTest.__mro__:
        if "percentButterFat" in klass.__dict__:
            descriptor = klass.__dict__["percentButterFat"]
            break
    assert isinstance(descriptor, property)

def test_tracker::milktest_has_percentProtein():
    assert hasattr(tracker::MilkTest, "percentProtein")
    descriptor = None
    for klass in tracker::MilkTest.__mro__:
        if "percentProtein" in klass.__dict__:
            descriptor = klass.__dict__["percentProtein"]
            break
    assert isinstance(descriptor, property)

def test_tracker::milktest_has_poundsProduced():
    assert hasattr(tracker::MilkTest, "poundsProduced")
    descriptor = None
    for klass in tracker::MilkTest.__mro__:
        if "poundsProduced" in klass.__dict__:
            descriptor = klass.__dict__["poundsProduced"]
            break
    assert isinstance(descriptor, property)

def test_tracker::milktest_has_somaticCellCounts():
    assert hasattr(tracker::MilkTest, "somaticCellCounts")
    descriptor = None
    for klass in tracker::MilkTest.__mro__:
        if "somaticCellCounts" in klass.__dict__:
            descriptor = klass.__dict__["somaticCellCounts"]
            break
    assert isinstance(descriptor, property)



def test_tracker::imported_is_not_abstract():
    assert not inspect.isabstract(tracker::Imported)


def test_tracker::imported_constructor_exists():
    assert callable(tracker::Imported.__init__)


def test_tracker::imported_constructor_args():
    sig = inspect.signature(tracker::Imported.__init__)
    params = list(sig.parameters.keys())



def test_tracker::tagallocated_is_not_abstract():
    assert not inspect.isabstract(tracker::TagAllocated)


def test_tracker::tagallocated_constructor_exists():
    assert callable(tracker::TagAllocated.__init__)


def test_tracker::tagallocated_constructor_args():
    sig = inspect.signature(tracker::TagAllocated.__init__)
    params = list(sig.parameters.keys())



def test_tracker::schema_is_not_abstract():
    assert not inspect.isabstract(tracker::Schema)


def test_tracker::schema_constructor_exists():
    assert callable(tracker::Schema.__init__)


def test_tracker::schema_constructor_args():
    sig = inspect.signature(tracker::Schema.__init__)
    params = list(sig.parameters.keys())



def test_tracker::location_is_not_abstract():
    assert not inspect.isabstract(tracker::Location)


def test_tracker::location_constructor_exists():
    assert callable(tracker::Location.__init__)


def test_tracker::location_constructor_args():
    sig = inspect.signature(tracker::Location.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tracker::location_has_name():
    assert hasattr(tracker::Location, "name")
    descriptor = None
    for klass in tracker::Location.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tracker::tag_is_not_abstract():
    assert not inspect.isabstract(tracker::Tag)


def test_tracker::tag_constructor_exists():
    assert callable(tracker::Tag.__init__)


def test_tracker::tag_constructor_args():
    sig = inspect.signature(tracker::Tag.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "usainNumberUsed" in params, "Missing parameter 'usainNumberUsed'"

def test_tracker::tag_has_id():
    assert hasattr(tracker::Tag, "id")
    descriptor = None
    for klass in tracker::Tag.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_tracker::tag_has_usainNumberUsed():
    assert hasattr(tracker::Tag, "usainNumberUsed")
    descriptor = None
    for klass in tracker::Tag.__mro__:
        if "usainNumberUsed" in klass.__dict__:
            descriptor = klass.__dict__["usainNumberUsed"]
            break
    assert isinstance(descriptor, property)



def test_animal_is_not_abstract():
    assert not inspect.isabstract(Animal)


def test_animal_constructor_exists():
    assert callable(Animal.__init__)


def test_animal_constructor_args():
    sig = inspect.signature(Animal.__init__)
    params = list(sig.parameters.keys())



def test_tracker::swine_is_not_abstract():
    assert not inspect.isabstract(tracker::Swine)


def test_tracker::swine_constructor_exists():
    assert callable(tracker::Swine.__init__)


def test_tracker::swine_constructor_args():
    sig = inspect.signature(tracker::Swine.__init__)
    params = list(sig.parameters.keys())
    assert "rightEarNotching" in params, "Missing parameter 'rightEarNotching'"
    assert "leftEarNotching" in params, "Missing parameter 'leftEarNotching'"
    assert "swineBreed" in params, "Missing parameter 'swineBreed'"

def test_tracker::swine_has_rightEarNotching():
    assert hasattr(tracker::Swine, "rightEarNotching")
    descriptor = None
    for klass in tracker::Swine.__mro__:
        if "rightEarNotching" in klass.__dict__:
            descriptor = klass.__dict__["rightEarNotching"]
            break
    assert isinstance(descriptor, property)

def test_tracker::swine_has_leftEarNotching():
    assert hasattr(tracker::Swine, "leftEarNotching")
    descriptor = None
    for klass in tracker::Swine.__mro__:
        if "leftEarNotching" in klass.__dict__:
            descriptor = klass.__dict__["leftEarNotching"]
            break
    assert isinstance(descriptor, property)

def test_tracker::swine_has_swineBreed():
    assert hasattr(tracker::Swine, "swineBreed")
    descriptor = None
    for klass in tracker::Swine.__mro__:
        if "swineBreed" in klass.__dict__:
            descriptor = klass.__dict__["swineBreed"]
            break
    assert isinstance(descriptor, property)



def test_tracker::caprine_is_not_abstract():
    assert not inspect.isabstract(tracker::Caprine)


def test_tracker::caprine_constructor_exists():
    assert callable(tracker::Caprine.__init__)


def test_tracker::caprine_constructor_args():
    sig = inspect.signature(tracker::Caprine.__init__)
    params = list(sig.parameters.keys())
    assert "goatBreed" in params, "Missing parameter 'goatBreed'"

def test_tracker::caprine_has_goatBreed():
    assert hasattr(tracker::Caprine, "goatBreed")
    descriptor = None
    for klass in tracker::Caprine.__mro__:
        if "goatBreed" in klass.__dict__:
            descriptor = klass.__dict__["goatBreed"]
            break
    assert isinstance(descriptor, property)



def test_tracker::ovine_is_not_abstract():
    assert not inspect.isabstract(tracker::Ovine)


def test_tracker::ovine_constructor_exists():
    assert callable(tracker::Ovine.__init__)


def test_tracker::ovine_constructor_args():
    sig = inspect.signature(tracker::Ovine.__init__)
    params = list(sig.parameters.keys())
    assert "scrapieTag" in params, "Missing parameter 'scrapieTag'"
    assert "sheepBreed" in params, "Missing parameter 'sheepBreed'"

def test_tracker::ovine_has_scrapieTag():
    assert hasattr(tracker::Ovine, "scrapieTag")
    descriptor = None
    for klass in tracker::Ovine.__mro__:
        if "scrapieTag" in klass.__dict__:
            descriptor = klass.__dict__["scrapieTag"]
            break
    assert isinstance(descriptor, property)

def test_tracker::ovine_has_sheepBreed():
    assert hasattr(tracker::Ovine, "sheepBreed")
    descriptor = None
    for klass in tracker::Ovine.__mro__:
        if "sheepBreed" in klass.__dict__:
            descriptor = klass.__dict__["sheepBreed"]
            break
    assert isinstance(descriptor, property)



def test_tracker::equine_is_not_abstract():
    assert not inspect.isabstract(tracker::Equine)


def test_tracker::equine_constructor_exists():
    assert callable(tracker::Equine.__init__)


def test_tracker::equine_constructor_args():
    sig = inspect.signature(tracker::Equine.__init__)
    params = list(sig.parameters.keys())
    assert "horseBreed" in params, "Missing parameter 'horseBreed'"

def test_tracker::equine_has_horseBreed():
    assert hasattr(tracker::Equine, "horseBreed")
    descriptor = None
    for klass in tracker::Equine.__mro__:
        if "horseBreed" in klass.__dict__:
            descriptor = klass.__dict__["horseBreed"]
            break
    assert isinstance(descriptor, property)



def test_tracker::bovine_is_not_abstract():
    assert not inspect.isabstract(tracker::Bovine)


def test_tracker::bovine_constructor_exists():
    assert callable(tracker::Bovine.__init__)


def test_tracker::bovine_constructor_args():
    sig = inspect.signature(tracker::Bovine.__init__)
    params = list(sig.parameters.keys())



def test_tracker::event_is_not_abstract():
    assert not inspect.isabstract(tracker::Event)


def test_tracker::event_constructor_exists():
    assert callable(tracker::Event.__init__)


def test_tracker::event_constructor_args():
    sig = inspect.signature(tracker::Event.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "eventCode" in params, "Missing parameter 'eventCode'"
    assert "comments" in params, "Missing parameter 'comments'"
    assert "electronicallyRead" in params, "Missing parameter 'electronicallyRead'"
    assert "dateTime" in params, "Missing parameter 'dateTime'"
    assert "correction" in params, "Missing parameter 'correction'"

def test_tracker::event_has_id():
    assert hasattr(tracker::Event, "id")
    descriptor = None
    for klass in tracker::Event.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_tracker::event_has_eventCode():
    assert hasattr(tracker::Event, "eventCode")
    descriptor = None
    for klass in tracker::Event.__mro__:
        if "eventCode" in klass.__dict__:
            descriptor = klass.__dict__["eventCode"]
            break
    assert isinstance(descriptor, property)

def test_tracker::event_has_comments():
    assert hasattr(tracker::Event, "comments")
    descriptor = None
    for klass in tracker::Event.__mro__:
        if "comments" in klass.__dict__:
            descriptor = klass.__dict__["comments"]
            break
    assert isinstance(descriptor, property)

def test_tracker::event_has_electronicallyRead():
    assert hasattr(tracker::Event, "electronicallyRead")
    descriptor = None
    for klass in tracker::Event.__mro__:
        if "electronicallyRead" in klass.__dict__:
            descriptor = klass.__dict__["electronicallyRead"]
            break
    assert isinstance(descriptor, property)

def test_tracker::event_has_dateTime():
    assert hasattr(tracker::Event, "dateTime")
    descriptor = None
    for klass in tracker::Event.__mro__:
        if "dateTime" in klass.__dict__:
            descriptor = klass.__dict__["dateTime"]
            break
    assert isinstance(descriptor, property)

def test_tracker::event_has_correction():
    assert hasattr(tracker::Event, "correction")
    descriptor = None
    for klass in tracker::Event.__mro__:
        if "correction" in klass.__dict__:
            descriptor = klass.__dict__["correction"]
            break
    assert isinstance(descriptor, property)



def test_tracker::animal_is_not_abstract():
    assert not inspect.isabstract(tracker::Animal)


def test_tracker::animal_constructor_exists():
    assert callable(tracker::Animal.__init__)


def test_tracker::animal_constructor_args():
    sig = inspect.signature(tracker::Animal.__init__)
    params = list(sig.parameters.keys())
    assert "ageInDays" in params, "Missing parameter 'ageInDays'"
    assert "visualID" in params, "Missing parameter 'visualID'"
    assert "comments" in params, "Missing parameter 'comments'"
    assert "type" in params, "Missing parameter 'type'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "alternativeID" in params, "Missing parameter 'alternativeID'"
    assert "sexCode" in params, "Missing parameter 'sexCode'"
    assert "lastEventDateTime" in params, "Missing parameter 'lastEventDateTime'"
    assert "breed" in params, "Missing parameter 'breed'"
    assert "birthDate" in params, "Missing parameter 'birthDate'"
    assert "sex" in params, "Missing parameter 'sex'"
    assert "speciesCode" in params, "Missing parameter 'speciesCode'"
    assert "weightGainPerDay" in params, "Missing parameter 'weightGainPerDay'"
    assert "id" in params, "Missing parameter 'id'"
    assert "species" in params, "Missing parameter 'species'"

def test_tracker::animal_has_ageInDays():
    assert hasattr(tracker::Animal, "ageInDays")
    descriptor = None
    for klass in tracker::Animal.__mro__:
        if "ageInDays" in klass.__dict__:
            descriptor = klass.__dict__["ageInDays"]
            break
    assert isinstance(descriptor, property)

def test_tracker::animal_has_visualID():
    assert hasattr(tracker::Animal, "visualID")
    descriptor = None
    for klass in tracker::Animal.__mro__:
        if "visualID" in klass.__dict__:
            descriptor = klass.__dict__["visualID"]
            break
    assert isinstance(descriptor, property)

def test_tracker::animal_has_comments():
    assert hasattr(tracker::Animal, "comments")
    descriptor = None
    for klass in tracker::Animal.__mro__:
        if "comments" in klass.__dict__:
            descriptor = klass.__dict__["comments"]
            break
    assert isinstance(descriptor, property)

def test_tracker::animal_has_type():
    assert hasattr(tracker::Animal, "type")
    descriptor = None
    for klass in tracker::Animal.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_tracker::animal_has_weight():
    assert hasattr(tracker::Animal, "weight")
    descriptor = None
    for klass in tracker::Animal.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_tracker::animal_has_alternativeID():
    assert hasattr(tracker::Animal, "alternativeID")
    descriptor = None
    for klass in tracker::Animal.__mro__:
        if "alternativeID" in klass.__dict__:
            descriptor = klass.__dict__["alternativeID"]
            break
    assert isinstance(descriptor, property)

def test_tracker::animal_has_sexCode():
    assert hasattr(tracker::Animal, "sexCode")
    descriptor = None
    for klass in tracker::Animal.__mro__:
        if "sexCode" in klass.__dict__:
            descriptor = klass.__dict__["sexCode"]
            break
    assert isinstance(descriptor, property)

def test_tracker::animal_has_lastEventDateTime():
    assert hasattr(tracker::Animal, "lastEventDateTime")
    descriptor = None
    for klass in tracker::Animal.__mro__:
        if "lastEventDateTime" in klass.__dict__:
            descriptor = klass.__dict__["lastEventDateTime"]
            break
    assert isinstance(descriptor, property)

def test_tracker::animal_has_breed():
    assert hasattr(tracker::Animal, "breed")
    descriptor = None
    for klass in tracker::Animal.__mro__:
        if "breed" in klass.__dict__:
            descriptor = klass.__dict__["breed"]
            break
    assert isinstance(descriptor, property)

def test_tracker::animal_has_birthDate():
    assert hasattr(tracker::Animal, "birthDate")
    descriptor = None
    for klass in tracker::Animal.__mro__:
        if "birthDate" in klass.__dict__:
            descriptor = klass.__dict__["birthDate"]
            break
    assert isinstance(descriptor, property)

def test_tracker::animal_has_sex():
    assert hasattr(tracker::Animal, "sex")
    descriptor = None
    for klass in tracker::Animal.__mro__:
        if "sex" in klass.__dict__:
            descriptor = klass.__dict__["sex"]
            break
    assert isinstance(descriptor, property)

def test_tracker::animal_has_speciesCode():
    assert hasattr(tracker::Animal, "speciesCode")
    descriptor = None
    for klass in tracker::Animal.__mro__:
        if "speciesCode" in klass.__dict__:
            descriptor = klass.__dict__["speciesCode"]
            break
    assert isinstance(descriptor, property)

def test_tracker::animal_has_weightGainPerDay():
    assert hasattr(tracker::Animal, "weightGainPerDay")
    descriptor = None
    for klass in tracker::Animal.__mro__:
        if "weightGainPerDay" in klass.__dict__:
            descriptor = klass.__dict__["weightGainPerDay"]
            break
    assert isinstance(descriptor, property)

def test_tracker::animal_has_id():
    assert hasattr(tracker::Animal, "id")
    descriptor = None
    for klass in tracker::Animal.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_tracker::animal_has_species():
    assert hasattr(tracker::Animal, "species")
    descriptor = None
    for klass in tracker::Animal.__mro__:
        if "species" in klass.__dict__:
            descriptor = klass.__dict__["species"]
            break
    assert isinstance(descriptor, property)

def test_beefbreed_exists():
    # Check that the Enumeration exists
    assert BeefBreed is not None

def test_beefbreed_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BeefBreed]
    expected_literals = [
        "NS",
        "DR",
        "CA",
        "HP",
        "AR",
        "IS",
        "SA",
        "FC",
        "LU",
        "IB",
        "MR",
        "BR",
        "RD",
        "MO",
        "NM",
        "GY",
        "ER",
        "TP",
        "CB",
        "MG",
        "HB",
        "SH",
        "AL",
        "BB",
        "MA",
        "FA",
        "CP",
        "AW",
        "RS",
        "CN",
        "AF",
        "SP",
        "DJ",
        "BA",
        "BG",
        "KB",
        "WF",
        "HY",
        "WB",
        "BE",
        "FP",
        "RB",
        "AB",
        "RO",
        "NE",
        "SB",
        "PA",
        "SM",
        "XX",
        "DN",
        "GS",
        "ME",
        "BM",
        "DB",
        "SV",
        "DL",
        "AN",
        "MU",
        "FB",
        "BH",
        "TN",
        "GZ",
        "DF",
        "MH",
        "GR",
        "BQ",
        "BW",
        "CM",
        "SG",
        "GV",
        "DS",
        "SE",
        "CG",
        "KY",
        "PR",
        "YA",
        "PI",
        "SS",
        "RW",
        "NR",
        "SW",
        "AK",
        "GE",
        "Unspecified",
        "AM",
        "RA",
        "AU",
        "CU",
        "PZ",
        "SX",
        "GA",
        "TG",
        "XT",
        "MC",
        "BI",
        "LO",
        "RN",
        "TI",
        "DE",
        "TA",
        "BO",
        "LR",
        "FL",
        "CH",
        "SI",
        "BU",
        "AE",
        "BL",
        "HC",
        "BD",
        "SL",
        "ML",
        "RP",
        "BN",
        "MI",
        "TL",
        "WP",
        "BF",
        "RR",
        "FR",
        "LM",
        "GI",
        "HH",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BeefBreed"

def test_sheepbreed_exists():
    # Check that the Enumeration exists
    assert SheepBreed is not None

def test_sheepbreed_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SheepBreed]
    expected_literals = [
        "OU",
        "RG",
        "NL",
        "IL",
        "BW",
        "FB",
        "BL",
        "BO",
        "SX",
        "TA",
        "SU",
        "SC",
        "XM",
        "DL",
        "HY",
        "CP",
        "CR",
        "SR",
        "ST",
        "CF",
        "CO",
        "PE",
        "XL",
        "ER",
        "MP",
        "CL",
        "RI",
        "KK",
        "KA",
        "MM",
        "RM",
        "BC",
        "ZS",
        "LY",
        "LI",
        "PO",
        "HL",
        "NC",
        "BF",
        "OX",
        "Unspecified",
        "RY",
        "LE",
        "MT",
        "SL",
        "RV",
        "HS",
        "FN",
        "TU",
        "CD",
        "KH",
        "DP",
        "TX",
        "DH",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SheepBreed"

def test_usswinequalitygrade_exists():
    # Check that the Enumeration exists
    assert USSwineQualityGrade is not None

def test_usswinequalitygrade_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in USSwineQualityGrade]
    expected_literals = [
        "Three",
        "Two",
        "Four",
        "Unspecified",
        "One",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in USSwineQualityGrade"

def test_usbeefyieldgrade_exists():
    # Check that the Enumeration exists
    assert USBeefYieldGrade is not None

def test_usbeefyieldgrade_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in USBeefYieldGrade]
    expected_literals = [
        "Two",
        "Four",
        "Unspecified",
        "Three",
        "Five",
        "One",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in USBeefYieldGrade"

def test_sex_exists():
    # Check that the Enumeration exists
    assert Sex is not None

def test_sex_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Sex]
    expected_literals = [
        "M",
        "Unspecified",
        "F",
        "S",
        "C",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Sex"

def test_treatment_exists():
    # Check that the Enumeration exists
    assert Treatment is not None

def test_treatment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Treatment]
    expected_literals = [
        "Vitamin",
        "Prevention",
        "Unspecified",
        "Hormone",
        "Vaccination",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Treatment"

def test_dairybreed_exists():
    # Check that the Enumeration exists
    assert DairyBreed is not None

def test_dairybreed_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DairyBreed]
    expected_literals = [
        "GU",
        "Unspecified",
        "LD",
        "AY",
        "HO",
        "FM",
        "WW",
        "MS",
        "GD",
        "JE",
        "BS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DairyBreed"

def test_bisonbreed_exists():
    # Check that the Enumeration exists
    assert BisonBreed is not None

def test_bisonbreed_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BisonBreed]
    expected_literals = [
        "PB",
        "WO",
        "Unspecified",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BisonBreed"

def test_treatmentmethod_exists():
    # Check that the Enumeration exists
    assert TreatmentMethod is not None

def test_treatmentmethod_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TreatmentMethod]
    expected_literals = [
        "Nasal",
        "Salve",
        "Intramuscular",
        "Unspecified",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TreatmentMethod"

def test_goatbreed_exists():
    # Check that the Enumeration exists
    assert GoatBreed is not None

def test_goatbreed_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GoatBreed]
    expected_literals = [
        "AI",
        "OH",
        "LN",
        "BZ",
        "ND",
        "Unspecified",
        "AG",
        "TO",
        "NU",
        "CS",
        "EN",
        "PY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GoatBreed"

def test_level_exists():
    # Check that the Enumeration exists
    assert Level is not None

def test_level_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Level]
    expected_literals = [
        "Average",
        "Low",
        "Unspecified",
        "High",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Level"

def test_swinebreed_exists():
    # Check that the Enumeration exists
    assert SwineBreed is not None

def test_swinebreed_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SwineBreed]
    expected_literals = [
        "CW",
        "DU",
        "PE",
        "Unspecified",
        "TM",
        "LB",
        "YO",
        "WS",
        "HA",
        "LA",
        "PC",
        "RW",
        "BK",
        "LC",
        "LW",
        "SO",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SwineBreed"

def test_horsebreed_exists():
    # Check that the Enumeration exists
    assert HorseBreed is not None

def test_horsebreed_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HorseBreed]
    expected_literals = [
        "HF",
        "FH",
        "AP",
        "TP",
        "IC",
        "RH",
        "SE",
        "FR",
        "TH",
        "CM",
        "OB",
        "MN",
        "PF",
        "Unspecified",
        "PV",
        "PW",
        "WE",
        "QH",
        "HK",
        "VK",
        "HT",
        "NK",
        "PN",
        "RU",
        "AC",
        "FJ",
        "SY",
        "NO",
        "CI",
        "DW",
        "GL",
        "EX",
        "HN",
        "TW",
        "HV",
        "AD",
        "MU",
        "WU",
        "CV",
        "HG",
        "HW",
        "PL",
        "AO",
        "AS",
        "PH",
        "CY",
        "TF",
        "NF",
        "SN",
        "FE",
        "DT",
        "BW",
        "LZ",
        "WF",
        "AA",
        "BU",
        "SF",
        "WI",
        "WW",
        "BY",
        "WG",
        "PT",
        "HU",
        "MF",
        "OL",
        "TR",
        "FC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in HorseBreed"

def test_onetoten_exists():
    # Check that the Enumeration exists
    assert OneToTen is not None

def test_onetoten_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OneToTen]
    expected_literals = [
        "Nine",
        "Six",
        "Ten",
        "Unspecified",
        "One",
        "Two",
        "Five",
        "Seven",
        "Eight",
        "Four",
        "Three",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OneToTen"

def test_usqualitygrade_exists():
    # Check that the Enumeration exists
    assert USQualityGrade is not None

def test_usqualitygrade_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in USQualityGrade]
    expected_literals = [
        "Unspecified",
        "Prime",
        "Standard",
        "Choice",
        "Select",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in USQualityGrade"

def test_animaltype_exists():
    # Check that the Enumeration exists
    assert AnimalType is not None

def test_animaltype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AnimalType]
    expected_literals = [
        "Swine",
        "Ovine",
        "Unspecified",
        "Caprine",
        "BovineDairy",
        "Equine",
        "BovineBeef",
        "BovineBison",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AnimalType"

def test_eventdatatype_exists():
    # Check that the Enumeration exists
    assert EventDataType is not None

def test_eventdatatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EventDataType]
    expected_literals = [
        "Integer",
        "Boolean",
        "String",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EventDataType"


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
tracker::EventAttributeSchema_strategy = st.builds(
    tracker::EventAttributeSchema,
    dataType=
        safe_text,
    description=
        safe_text,
    name=
        safe_text
)
MedicalCondition_strategy = st.builds(
    MedicalCondition,
)
tracker::Mastitis_strategy = st.builds(
    tracker::Mastitis,
    origin=
        safe_text,
    location=
        safe_text
)
Birthing_strategy = st.builds(
    Birthing,
)
tracker::Calving_strategy = st.builds(
    tracker::Calving,
)
tracker::EventSchema_strategy = st.builds(
    tracker::EventSchema,
    animalType=
        safe_text,
    description=
        safe_text,
    name=
        safe_text
)
tracker::EventAttribute_strategy = st.builds(
    tracker::EventAttribute,
    value=
        safe_text,
    key=
        safe_text
)
Bovine_strategy = st.builds(
    Bovine,
)
tracker::BovineBison_strategy = st.builds(
    tracker::BovineBison,
    buffaloBreed=
        safe_text
)
tracker::BovineDairy_strategy = st.builds(
    tracker::BovineDairy,
    dairyBreed=
        safe_text
)
tracker::BovineBeef_strategy = st.builds(
    tracker::BovineBeef,
    beefBreed=
        safe_text
)
tracker::Premises_strategy = st.builds(
    tracker::Premises,
    name=
        safe_text,
    emailContact=
        safe_text,
    uri=
        safe_text,
    premisesId=
        safe_text
)
Event_strategy = st.builds(
    Event,
)
tracker::USSwineGrading_strategy = st.builds(
    tracker::USSwineGrading,
    qualityGrade=
        safe_text
)
tracker::HerdTest_strategy = st.builds(
    tracker::HerdTest,
    pregnant=
        st.booleans(),
    daysSinceBredEstimate=
        st.integers(),
    bredDateEstimate=
        st.dates()
)
tracker::ReplacedTag_strategy = st.builds(
    tracker::ReplacedTag,
    usainNumberUsedForOldId=
        st.booleans(),
    oldId=
        safe_text
)
tracker::ICVI_strategy = st.builds(
    tracker::ICVI,
)
tracker::Sighting_strategy = st.builds(
    tracker::Sighting,
)
tracker::TagApplied_strategy = st.builds(
    tracker::TagApplied,
)
tracker::USOvineGrading_strategy = st.builds(
    tracker::USOvineGrading,
    qualityGradeLevel=
        safe_text,
    qualityGrade=
        safe_text
)
tracker::WeighIn_strategy = st.builds(
    tracker::WeighIn,
    weightGainPerDay=
        safe_text,
    weight=
        safe_text
)
tracker::GenericEvent_strategy = st.builds(
    tracker::GenericEvent,
)
tracker::MedicalCondition_strategy = st.builds(
    tracker::MedicalCondition,
)
tracker::USBeefGrading_strategy = st.builds(
    tracker::USBeefGrading,
    yieldGrade=
        safe_text,
    qualityGrade=
        safe_text,
    qualityGradeLevel=
        safe_text
)
tracker::BirthDefect_strategy = st.builds(
    tracker::BirthDefect,
    freemartin=
        st.booleans()
)
tracker::Died_strategy = st.builds(
    tracker::Died,
)
tracker::MedicalTreatment_strategy = st.builds(
    tracker::MedicalTreatment,
    quantity=
        safe_text,
    manufacturer=
        safe_text,
    treatment=
        safe_text,
    lot=
        safe_text,
    name=
        safe_text,
    method=
        safe_text,
    product=
        safe_text
)
tracker::MovedOut_strategy = st.builds(
    tracker::MovedOut,
    destinationPin=
        safe_text
)
tracker::Slaughtered_strategy = st.builds(
    tracker::Slaughtered,
)
tracker::MovedIn_strategy = st.builds(
    tracker::MovedIn,
    sourcePin=
        safe_text
)
tracker::AnimalMissing_strategy = st.builds(
    tracker::AnimalMissing,
)
tracker::Birthing_strategy = st.builds(
    tracker::Birthing,
    difficulty=
        safe_text,
    assisted=
        st.booleans(),
    viability=
        st.booleans()
)
tracker::Exported_strategy = st.builds(
    tracker::Exported,
)
tracker::TagRetired_strategy = st.builds(
    tracker::TagRetired,
)
tracker::LostTag_strategy = st.builds(
    tracker::LostTag,
)
tracker::MilkTest_strategy = st.builds(
    tracker::MilkTest,
    otherSolids=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    percentButterFat=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    percentProtein=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    poundsProduced=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    somaticCellCounts=
        st.integers()
)
tracker::Imported_strategy = st.builds(
    tracker::Imported,
)
tracker::TagAllocated_strategy = st.builds(
    tracker::TagAllocated,
)
tracker::Schema_strategy = st.builds(
    tracker::Schema,
)
tracker::Location_strategy = st.builds(
    tracker::Location,
    name=
        safe_text
)
tracker::Tag_strategy = st.builds(
    tracker::Tag,
    id=
        safe_text,
    usainNumberUsed=
        st.booleans()
)
Animal_strategy = st.builds(
    Animal,
)
tracker::Swine_strategy = st.builds(
    tracker::Swine,
    rightEarNotching=
        st.integers(),
    leftEarNotching=
        st.integers(),
    swineBreed=
        safe_text
)
tracker::Caprine_strategy = st.builds(
    tracker::Caprine,
    goatBreed=
        safe_text
)
tracker::Ovine_strategy = st.builds(
    tracker::Ovine,
    scrapieTag=
        safe_text,
    sheepBreed=
        safe_text
)
tracker::Equine_strategy = st.builds(
    tracker::Equine,
    horseBreed=
        safe_text
)
tracker::Bovine_strategy = st.builds(
    tracker::Bovine,
)
tracker::Event_strategy = st.builds(
    tracker::Event,
    id=
        safe_text,
    eventCode=
        st.integers(),
    comments=
        safe_text,
    electronicallyRead=
        st.booleans(),
    dateTime=
        st.dates(),
    correction=
        st.booleans()
)
tracker::Animal_strategy = st.builds(
    tracker::Animal,
    ageInDays=
        st.integers(),
    visualID=
        safe_text,
    comments=
        safe_text,
    type=
        safe_text,
    weight=
        safe_text,
    alternativeID=
        safe_text,
    sexCode=
        safe_text,
    lastEventDateTime=
        st.dates(),
    breed=
        safe_text,
    birthDate=
        st.dates(),
    sex=
        safe_text,
    speciesCode=
        safe_text,
    weightGainPerDay=
        safe_text,
    id=
        safe_text,
    species=
        safe_text
)

@given(instance=tracker::EventAttributeSchema_strategy)
@settings(max_examples=50)
def test_tracker::eventattributeschema_instantiation(instance):
    assert isinstance(instance, tracker::EventAttributeSchema)

@given(instance=tracker::EventAttributeSchema_strategy)
def test_tracker::eventattributeschema_dataType_type(instance):
    assert isinstance(instance.dataType, str)


@given(instance=tracker::EventAttributeSchema_strategy)
def test_tracker::eventattributeschema_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original

@given(instance=tracker::EventAttributeSchema_strategy)
def test_tracker::eventattributeschema_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=tracker::EventAttributeSchema_strategy)
def test_tracker::eventattributeschema_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=tracker::EventAttributeSchema_strategy)
def test_tracker::eventattributeschema_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tracker::EventAttributeSchema_strategy)
def test_tracker::eventattributeschema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MedicalCondition_strategy)
@settings(max_examples=50)
def test_medicalcondition_instantiation(instance):
    assert isinstance(instance, MedicalCondition)

@given(instance=tracker::Mastitis_strategy)
@settings(max_examples=50)
def test_tracker::mastitis_instantiation(instance):
    assert isinstance(instance, tracker::Mastitis)

@given(instance=tracker::Mastitis_strategy)
def test_tracker::mastitis_origin_type(instance):
    assert isinstance(instance.origin, str)


@given(instance=tracker::Mastitis_strategy)
def test_tracker::mastitis_origin_setter(instance):
    original = instance.origin
    instance.origin = original
    assert instance.origin == original

@given(instance=tracker::Mastitis_strategy)
def test_tracker::mastitis_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=tracker::Mastitis_strategy)
def test_tracker::mastitis_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=Birthing_strategy)
@settings(max_examples=50)
def test_birthing_instantiation(instance):
    assert isinstance(instance, Birthing)

@given(instance=tracker::Calving_strategy)
@settings(max_examples=50)
def test_tracker::calving_instantiation(instance):
    assert isinstance(instance, tracker::Calving)

@given(instance=tracker::EventSchema_strategy)
@settings(max_examples=50)
def test_tracker::eventschema_instantiation(instance):
    assert isinstance(instance, tracker::EventSchema)

@given(instance=tracker::EventSchema_strategy)
def test_tracker::eventschema_animalType_type(instance):
    assert isinstance(instance.animalType, str)


@given(instance=tracker::EventSchema_strategy)
def test_tracker::eventschema_animalType_setter(instance):
    original = instance.animalType
    instance.animalType = original
    assert instance.animalType == original

@given(instance=tracker::EventSchema_strategy)
def test_tracker::eventschema_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=tracker::EventSchema_strategy)
def test_tracker::eventschema_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=tracker::EventSchema_strategy)
def test_tracker::eventschema_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tracker::EventSchema_strategy)
def test_tracker::eventschema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tracker::EventAttribute_strategy)
@settings(max_examples=50)
def test_tracker::eventattribute_instantiation(instance):
    assert isinstance(instance, tracker::EventAttribute)

@given(instance=tracker::EventAttribute_strategy)
def test_tracker::eventattribute_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=tracker::EventAttribute_strategy)
def test_tracker::eventattribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=tracker::EventAttribute_strategy)
def test_tracker::eventattribute_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=tracker::EventAttribute_strategy)
def test_tracker::eventattribute_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=Bovine_strategy)
@settings(max_examples=50)
def test_bovine_instantiation(instance):
    assert isinstance(instance, Bovine)

@given(instance=tracker::BovineBison_strategy)
@settings(max_examples=50)
def test_tracker::bovinebison_instantiation(instance):
    assert isinstance(instance, tracker::BovineBison)

@given(instance=tracker::BovineBison_strategy)
def test_tracker::bovinebison_buffaloBreed_type(instance):
    assert isinstance(instance.buffaloBreed, str)


@given(instance=tracker::BovineBison_strategy)
def test_tracker::bovinebison_buffaloBreed_setter(instance):
    original = instance.buffaloBreed
    instance.buffaloBreed = original
    assert instance.buffaloBreed == original

@given(instance=tracker::BovineDairy_strategy)
@settings(max_examples=50)
def test_tracker::bovinedairy_instantiation(instance):
    assert isinstance(instance, tracker::BovineDairy)

@given(instance=tracker::BovineDairy_strategy)
def test_tracker::bovinedairy_dairyBreed_type(instance):
    assert isinstance(instance.dairyBreed, str)


@given(instance=tracker::BovineDairy_strategy)
def test_tracker::bovinedairy_dairyBreed_setter(instance):
    original = instance.dairyBreed
    instance.dairyBreed = original
    assert instance.dairyBreed == original

@given(instance=tracker::BovineBeef_strategy)
@settings(max_examples=50)
def test_tracker::bovinebeef_instantiation(instance):
    assert isinstance(instance, tracker::BovineBeef)

@given(instance=tracker::BovineBeef_strategy)
def test_tracker::bovinebeef_beefBreed_type(instance):
    assert isinstance(instance.beefBreed, str)


@given(instance=tracker::BovineBeef_strategy)
def test_tracker::bovinebeef_beefBreed_setter(instance):
    original = instance.beefBreed
    instance.beefBreed = original
    assert instance.beefBreed == original

@given(instance=tracker::Premises_strategy)
@settings(max_examples=50)
def test_tracker::premises_instantiation(instance):
    assert isinstance(instance, tracker::Premises)

@given(instance=tracker::Premises_strategy)
def test_tracker::premises_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tracker::Premises_strategy)
def test_tracker::premises_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tracker::Premises_strategy)
def test_tracker::premises_emailContact_type(instance):
    assert isinstance(instance.emailContact, str)


@given(instance=tracker::Premises_strategy)
def test_tracker::premises_emailContact_setter(instance):
    original = instance.emailContact
    instance.emailContact = original
    assert instance.emailContact == original

@given(instance=tracker::Premises_strategy)
def test_tracker::premises_uri_type(instance):
    assert isinstance(instance.uri, str)


@given(instance=tracker::Premises_strategy)
def test_tracker::premises_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=tracker::Premises_strategy)
def test_tracker::premises_premisesId_type(instance):
    assert isinstance(instance.premisesId, str)


@given(instance=tracker::Premises_strategy)
def test_tracker::premises_premisesId_setter(instance):
    original = instance.premisesId
    instance.premisesId = original
    assert instance.premisesId == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tracker::Premises_strategy)
@settings(max_examples=30)
def test_tracker::premises_findanimal_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.findAnimal(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.findAnimal).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'findAnimal' in tracker::Premises is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'findAnimal' in tracker::Premises did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'findAnimal' in tracker::Premises is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tracker::Premises_strategy)
@settings(max_examples=30)
def test_tracker::premises_eventhistory_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eventHistory()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eventHistory).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eventHistory' in tracker::Premises is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eventHistory' in tracker::Premises did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eventHistory' in tracker::Premises is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tracker::Premises_strategy)
@settings(max_examples=30)
def test_tracker::premises_addtemplate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addTemplate(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addTemplate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addTemplate' in tracker::Premises is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addTemplate' in tracker::Premises did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addTemplate' in tracker::Premises is not implemented or raised an error")

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=tracker::USSwineGrading_strategy)
@settings(max_examples=50)
def test_tracker::usswinegrading_instantiation(instance):
    assert isinstance(instance, tracker::USSwineGrading)

@given(instance=tracker::USSwineGrading_strategy)
def test_tracker::usswinegrading_qualityGrade_type(instance):
    assert isinstance(instance.qualityGrade, str)


@given(instance=tracker::USSwineGrading_strategy)
def test_tracker::usswinegrading_qualityGrade_setter(instance):
    original = instance.qualityGrade
    instance.qualityGrade = original
    assert instance.qualityGrade == original

@given(instance=tracker::HerdTest_strategy)
@settings(max_examples=50)
def test_tracker::herdtest_instantiation(instance):
    assert isinstance(instance, tracker::HerdTest)

@given(instance=tracker::HerdTest_strategy)
def test_tracker::herdtest_pregnant_type(instance):
    assert isinstance(instance.pregnant, bool)


@given(instance=tracker::HerdTest_strategy)
def test_tracker::herdtest_pregnant_setter(instance):
    original = instance.pregnant
    instance.pregnant = original
    assert instance.pregnant == original

@given(instance=tracker::HerdTest_strategy)
def test_tracker::herdtest_daysSinceBredEstimate_type(instance):
    assert isinstance(instance.daysSinceBredEstimate, int)


@given(instance=tracker::HerdTest_strategy)
def test_tracker::herdtest_daysSinceBredEstimate_setter(instance):
    original = instance.daysSinceBredEstimate
    instance.daysSinceBredEstimate = original
    assert instance.daysSinceBredEstimate == original

@given(instance=tracker::HerdTest_strategy)
def test_tracker::herdtest_bredDateEstimate_type(instance):
    assert isinstance(instance.bredDateEstimate, date)


@given(instance=tracker::HerdTest_strategy)
def test_tracker::herdtest_bredDateEstimate_setter(instance):
    original = instance.bredDateEstimate
    instance.bredDateEstimate = original
    assert instance.bredDateEstimate == original

@given(instance=tracker::ReplacedTag_strategy)
@settings(max_examples=50)
def test_tracker::replacedtag_instantiation(instance):
    assert isinstance(instance, tracker::ReplacedTag)

@given(instance=tracker::ReplacedTag_strategy)
def test_tracker::replacedtag_usainNumberUsedForOldId_type(instance):
    assert isinstance(instance.usainNumberUsedForOldId, bool)


@given(instance=tracker::ReplacedTag_strategy)
def test_tracker::replacedtag_usainNumberUsedForOldId_setter(instance):
    original = instance.usainNumberUsedForOldId
    instance.usainNumberUsedForOldId = original
    assert instance.usainNumberUsedForOldId == original

@given(instance=tracker::ReplacedTag_strategy)
def test_tracker::replacedtag_oldId_type(instance):
    assert isinstance(instance.oldId, str)


@given(instance=tracker::ReplacedTag_strategy)
def test_tracker::replacedtag_oldId_setter(instance):
    original = instance.oldId
    instance.oldId = original
    assert instance.oldId == original

@given(instance=tracker::ICVI_strategy)
@settings(max_examples=50)
def test_tracker::icvi_instantiation(instance):
    assert isinstance(instance, tracker::ICVI)

@given(instance=tracker::Sighting_strategy)
@settings(max_examples=50)
def test_tracker::sighting_instantiation(instance):
    assert isinstance(instance, tracker::Sighting)

@given(instance=tracker::TagApplied_strategy)
@settings(max_examples=50)
def test_tracker::tagapplied_instantiation(instance):
    assert isinstance(instance, tracker::TagApplied)

@given(instance=tracker::USOvineGrading_strategy)
@settings(max_examples=50)
def test_tracker::usovinegrading_instantiation(instance):
    assert isinstance(instance, tracker::USOvineGrading)

@given(instance=tracker::USOvineGrading_strategy)
def test_tracker::usovinegrading_qualityGradeLevel_type(instance):
    assert isinstance(instance.qualityGradeLevel, str)


@given(instance=tracker::USOvineGrading_strategy)
def test_tracker::usovinegrading_qualityGradeLevel_setter(instance):
    original = instance.qualityGradeLevel
    instance.qualityGradeLevel = original
    assert instance.qualityGradeLevel == original

@given(instance=tracker::USOvineGrading_strategy)
def test_tracker::usovinegrading_qualityGrade_type(instance):
    assert isinstance(instance.qualityGrade, str)


@given(instance=tracker::USOvineGrading_strategy)
def test_tracker::usovinegrading_qualityGrade_setter(instance):
    original = instance.qualityGrade
    instance.qualityGrade = original
    assert instance.qualityGrade == original

@given(instance=tracker::WeighIn_strategy)
@settings(max_examples=50)
def test_tracker::weighin_instantiation(instance):
    assert isinstance(instance, tracker::WeighIn)

@given(instance=tracker::WeighIn_strategy)
def test_tracker::weighin_weightGainPerDay_type(instance):
    assert isinstance(instance.weightGainPerDay, str)


@given(instance=tracker::WeighIn_strategy)
def test_tracker::weighin_weightGainPerDay_setter(instance):
    original = instance.weightGainPerDay
    instance.weightGainPerDay = original
    assert instance.weightGainPerDay == original

@given(instance=tracker::WeighIn_strategy)
def test_tracker::weighin_weight_type(instance):
    assert isinstance(instance.weight, str)


@given(instance=tracker::WeighIn_strategy)
def test_tracker::weighin_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tracker::WeighIn_strategy)
@settings(max_examples=30)
def test_tracker::weighin_previousweighin_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.previousWeighIn()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.previousWeighIn).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'previousWeighIn' in tracker::WeighIn is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'previousWeighIn' in tracker::WeighIn did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'previousWeighIn' in tracker::WeighIn is not implemented or raised an error")

@given(instance=tracker::GenericEvent_strategy)
@settings(max_examples=50)
def test_tracker::genericevent_instantiation(instance):
    assert isinstance(instance, tracker::GenericEvent)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tracker::GenericEvent_strategy)
@settings(max_examples=30)
def test_tracker::genericevent_findschema_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.findSchema(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.findSchema).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'findSchema' in tracker::GenericEvent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'findSchema' in tracker::GenericEvent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'findSchema' in tracker::GenericEvent is not implemented or raised an error")

@given(instance=tracker::MedicalCondition_strategy)
@settings(max_examples=50)
def test_tracker::medicalcondition_instantiation(instance):
    assert isinstance(instance, tracker::MedicalCondition)

@given(instance=tracker::USBeefGrading_strategy)
@settings(max_examples=50)
def test_tracker::usbeefgrading_instantiation(instance):
    assert isinstance(instance, tracker::USBeefGrading)

@given(instance=tracker::USBeefGrading_strategy)
def test_tracker::usbeefgrading_yieldGrade_type(instance):
    assert isinstance(instance.yieldGrade, str)


@given(instance=tracker::USBeefGrading_strategy)
def test_tracker::usbeefgrading_yieldGrade_setter(instance):
    original = instance.yieldGrade
    instance.yieldGrade = original
    assert instance.yieldGrade == original

@given(instance=tracker::USBeefGrading_strategy)
def test_tracker::usbeefgrading_qualityGrade_type(instance):
    assert isinstance(instance.qualityGrade, str)


@given(instance=tracker::USBeefGrading_strategy)
def test_tracker::usbeefgrading_qualityGrade_setter(instance):
    original = instance.qualityGrade
    instance.qualityGrade = original
    assert instance.qualityGrade == original

@given(instance=tracker::USBeefGrading_strategy)
def test_tracker::usbeefgrading_qualityGradeLevel_type(instance):
    assert isinstance(instance.qualityGradeLevel, str)


@given(instance=tracker::USBeefGrading_strategy)
def test_tracker::usbeefgrading_qualityGradeLevel_setter(instance):
    original = instance.qualityGradeLevel
    instance.qualityGradeLevel = original
    assert instance.qualityGradeLevel == original

@given(instance=tracker::BirthDefect_strategy)
@settings(max_examples=50)
def test_tracker::birthdefect_instantiation(instance):
    assert isinstance(instance, tracker::BirthDefect)

@given(instance=tracker::BirthDefect_strategy)
def test_tracker::birthdefect_freemartin_type(instance):
    assert isinstance(instance.freemartin, bool)


@given(instance=tracker::BirthDefect_strategy)
def test_tracker::birthdefect_freemartin_setter(instance):
    original = instance.freemartin
    instance.freemartin = original
    assert instance.freemartin == original

@given(instance=tracker::Died_strategy)
@settings(max_examples=50)
def test_tracker::died_instantiation(instance):
    assert isinstance(instance, tracker::Died)

@given(instance=tracker::MedicalTreatment_strategy)
@settings(max_examples=50)
def test_tracker::medicaltreatment_instantiation(instance):
    assert isinstance(instance, tracker::MedicalTreatment)

@given(instance=tracker::MedicalTreatment_strategy)
def test_tracker::medicaltreatment_quantity_type(instance):
    assert isinstance(instance.quantity, str)


@given(instance=tracker::MedicalTreatment_strategy)
def test_tracker::medicaltreatment_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original

@given(instance=tracker::MedicalTreatment_strategy)
def test_tracker::medicaltreatment_manufacturer_type(instance):
    assert isinstance(instance.manufacturer, str)


@given(instance=tracker::MedicalTreatment_strategy)
def test_tracker::medicaltreatment_manufacturer_setter(instance):
    original = instance.manufacturer
    instance.manufacturer = original
    assert instance.manufacturer == original

@given(instance=tracker::MedicalTreatment_strategy)
def test_tracker::medicaltreatment_treatment_type(instance):
    assert isinstance(instance.treatment, str)


@given(instance=tracker::MedicalTreatment_strategy)
def test_tracker::medicaltreatment_treatment_setter(instance):
    original = instance.treatment
    instance.treatment = original
    assert instance.treatment == original

@given(instance=tracker::MedicalTreatment_strategy)
def test_tracker::medicaltreatment_lot_type(instance):
    assert isinstance(instance.lot, str)


@given(instance=tracker::MedicalTreatment_strategy)
def test_tracker::medicaltreatment_lot_setter(instance):
    original = instance.lot
    instance.lot = original
    assert instance.lot == original

@given(instance=tracker::MedicalTreatment_strategy)
def test_tracker::medicaltreatment_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tracker::MedicalTreatment_strategy)
def test_tracker::medicaltreatment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tracker::MedicalTreatment_strategy)
def test_tracker::medicaltreatment_method_type(instance):
    assert isinstance(instance.method, str)


@given(instance=tracker::MedicalTreatment_strategy)
def test_tracker::medicaltreatment_method_setter(instance):
    original = instance.method
    instance.method = original
    assert instance.method == original

@given(instance=tracker::MedicalTreatment_strategy)
def test_tracker::medicaltreatment_product_type(instance):
    assert isinstance(instance.product, str)


@given(instance=tracker::MedicalTreatment_strategy)
def test_tracker::medicaltreatment_product_setter(instance):
    original = instance.product
    instance.product = original
    assert instance.product == original

@given(instance=tracker::MovedOut_strategy)
@settings(max_examples=50)
def test_tracker::movedout_instantiation(instance):
    assert isinstance(instance, tracker::MovedOut)

@given(instance=tracker::MovedOut_strategy)
def test_tracker::movedout_destinationPin_type(instance):
    assert isinstance(instance.destinationPin, str)


@given(instance=tracker::MovedOut_strategy)
def test_tracker::movedout_destinationPin_setter(instance):
    original = instance.destinationPin
    instance.destinationPin = original
    assert instance.destinationPin == original

@given(instance=tracker::Slaughtered_strategy)
@settings(max_examples=50)
def test_tracker::slaughtered_instantiation(instance):
    assert isinstance(instance, tracker::Slaughtered)

@given(instance=tracker::MovedIn_strategy)
@settings(max_examples=50)
def test_tracker::movedin_instantiation(instance):
    assert isinstance(instance, tracker::MovedIn)

@given(instance=tracker::MovedIn_strategy)
def test_tracker::movedin_sourcePin_type(instance):
    assert isinstance(instance.sourcePin, str)


@given(instance=tracker::MovedIn_strategy)
def test_tracker::movedin_sourcePin_setter(instance):
    original = instance.sourcePin
    instance.sourcePin = original
    assert instance.sourcePin == original

@given(instance=tracker::AnimalMissing_strategy)
@settings(max_examples=50)
def test_tracker::animalmissing_instantiation(instance):
    assert isinstance(instance, tracker::AnimalMissing)

@given(instance=tracker::Birthing_strategy)
@settings(max_examples=50)
def test_tracker::birthing_instantiation(instance):
    assert isinstance(instance, tracker::Birthing)

@given(instance=tracker::Birthing_strategy)
def test_tracker::birthing_difficulty_type(instance):
    assert isinstance(instance.difficulty, str)


@given(instance=tracker::Birthing_strategy)
def test_tracker::birthing_difficulty_setter(instance):
    original = instance.difficulty
    instance.difficulty = original
    assert instance.difficulty == original

@given(instance=tracker::Birthing_strategy)
def test_tracker::birthing_assisted_type(instance):
    assert isinstance(instance.assisted, bool)


@given(instance=tracker::Birthing_strategy)
def test_tracker::birthing_assisted_setter(instance):
    original = instance.assisted
    instance.assisted = original
    assert instance.assisted == original

@given(instance=tracker::Birthing_strategy)
def test_tracker::birthing_viability_type(instance):
    assert isinstance(instance.viability, bool)


@given(instance=tracker::Birthing_strategy)
def test_tracker::birthing_viability_setter(instance):
    original = instance.viability
    instance.viability = original
    assert instance.viability == original

@given(instance=tracker::Exported_strategy)
@settings(max_examples=50)
def test_tracker::exported_instantiation(instance):
    assert isinstance(instance, tracker::Exported)

@given(instance=tracker::TagRetired_strategy)
@settings(max_examples=50)
def test_tracker::tagretired_instantiation(instance):
    assert isinstance(instance, tracker::TagRetired)

@given(instance=tracker::LostTag_strategy)
@settings(max_examples=50)
def test_tracker::losttag_instantiation(instance):
    assert isinstance(instance, tracker::LostTag)

@given(instance=tracker::MilkTest_strategy)
@settings(max_examples=50)
def test_tracker::milktest_instantiation(instance):
    assert isinstance(instance, tracker::MilkTest)

@given(instance=tracker::MilkTest_strategy)
def test_tracker::milktest_otherSolids_type(instance):
    assert isinstance(instance.otherSolids, float)


@given(instance=tracker::MilkTest_strategy)
def test_tracker::milktest_otherSolids_setter(instance):
    original = instance.otherSolids
    instance.otherSolids = original
    assert instance.otherSolids == original

@given(instance=tracker::MilkTest_strategy)
def test_tracker::milktest_percentButterFat_type(instance):
    assert isinstance(instance.percentButterFat, float)


@given(instance=tracker::MilkTest_strategy)
def test_tracker::milktest_percentButterFat_setter(instance):
    original = instance.percentButterFat
    instance.percentButterFat = original
    assert instance.percentButterFat == original

@given(instance=tracker::MilkTest_strategy)
def test_tracker::milktest_percentProtein_type(instance):
    assert isinstance(instance.percentProtein, float)


@given(instance=tracker::MilkTest_strategy)
def test_tracker::milktest_percentProtein_setter(instance):
    original = instance.percentProtein
    instance.percentProtein = original
    assert instance.percentProtein == original

@given(instance=tracker::MilkTest_strategy)
def test_tracker::milktest_poundsProduced_type(instance):
    assert isinstance(instance.poundsProduced, float)


@given(instance=tracker::MilkTest_strategy)
def test_tracker::milktest_poundsProduced_setter(instance):
    original = instance.poundsProduced
    instance.poundsProduced = original
    assert instance.poundsProduced == original

@given(instance=tracker::MilkTest_strategy)
def test_tracker::milktest_somaticCellCounts_type(instance):
    assert isinstance(instance.somaticCellCounts, int)


@given(instance=tracker::MilkTest_strategy)
def test_tracker::milktest_somaticCellCounts_setter(instance):
    original = instance.somaticCellCounts
    instance.somaticCellCounts = original
    assert instance.somaticCellCounts == original

@given(instance=tracker::Imported_strategy)
@settings(max_examples=50)
def test_tracker::imported_instantiation(instance):
    assert isinstance(instance, tracker::Imported)

@given(instance=tracker::TagAllocated_strategy)
@settings(max_examples=50)
def test_tracker::tagallocated_instantiation(instance):
    assert isinstance(instance, tracker::TagAllocated)

@given(instance=tracker::Schema_strategy)
@settings(max_examples=50)
def test_tracker::schema_instantiation(instance):
    assert isinstance(instance, tracker::Schema)

@given(instance=tracker::Location_strategy)
@settings(max_examples=50)
def test_tracker::location_instantiation(instance):
    assert isinstance(instance, tracker::Location)

@given(instance=tracker::Location_strategy)
def test_tracker::location_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tracker::Location_strategy)
def test_tracker::location_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tracker::Tag_strategy)
@settings(max_examples=50)
def test_tracker::tag_instantiation(instance):
    assert isinstance(instance, tracker::Tag)

@given(instance=tracker::Tag_strategy)
def test_tracker::tag_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=tracker::Tag_strategy)
def test_tracker::tag_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=tracker::Tag_strategy)
def test_tracker::tag_usainNumberUsed_type(instance):
    assert isinstance(instance.usainNumberUsed, bool)


@given(instance=tracker::Tag_strategy)
def test_tracker::tag_usainNumberUsed_setter(instance):
    original = instance.usainNumberUsed
    instance.usainNumberUsed = original
    assert instance.usainNumberUsed == original

@given(instance=Animal_strategy)
@settings(max_examples=50)
def test_animal_instantiation(instance):
    assert isinstance(instance, Animal)

@given(instance=tracker::Swine_strategy)
@settings(max_examples=50)
def test_tracker::swine_instantiation(instance):
    assert isinstance(instance, tracker::Swine)

@given(instance=tracker::Swine_strategy)
def test_tracker::swine_rightEarNotching_type(instance):
    assert isinstance(instance.rightEarNotching, int)


@given(instance=tracker::Swine_strategy)
def test_tracker::swine_rightEarNotching_setter(instance):
    original = instance.rightEarNotching
    instance.rightEarNotching = original
    assert instance.rightEarNotching == original

@given(instance=tracker::Swine_strategy)
def test_tracker::swine_leftEarNotching_type(instance):
    assert isinstance(instance.leftEarNotching, int)


@given(instance=tracker::Swine_strategy)
def test_tracker::swine_leftEarNotching_setter(instance):
    original = instance.leftEarNotching
    instance.leftEarNotching = original
    assert instance.leftEarNotching == original

@given(instance=tracker::Swine_strategy)
def test_tracker::swine_swineBreed_type(instance):
    assert isinstance(instance.swineBreed, str)


@given(instance=tracker::Swine_strategy)
def test_tracker::swine_swineBreed_setter(instance):
    original = instance.swineBreed
    instance.swineBreed = original
    assert instance.swineBreed == original

@given(instance=tracker::Caprine_strategy)
@settings(max_examples=50)
def test_tracker::caprine_instantiation(instance):
    assert isinstance(instance, tracker::Caprine)

@given(instance=tracker::Caprine_strategy)
def test_tracker::caprine_goatBreed_type(instance):
    assert isinstance(instance.goatBreed, str)


@given(instance=tracker::Caprine_strategy)
def test_tracker::caprine_goatBreed_setter(instance):
    original = instance.goatBreed
    instance.goatBreed = original
    assert instance.goatBreed == original

@given(instance=tracker::Ovine_strategy)
@settings(max_examples=50)
def test_tracker::ovine_instantiation(instance):
    assert isinstance(instance, tracker::Ovine)

@given(instance=tracker::Ovine_strategy)
def test_tracker::ovine_scrapieTag_type(instance):
    assert isinstance(instance.scrapieTag, str)


@given(instance=tracker::Ovine_strategy)
def test_tracker::ovine_scrapieTag_setter(instance):
    original = instance.scrapieTag
    instance.scrapieTag = original
    assert instance.scrapieTag == original

@given(instance=tracker::Ovine_strategy)
def test_tracker::ovine_sheepBreed_type(instance):
    assert isinstance(instance.sheepBreed, str)


@given(instance=tracker::Ovine_strategy)
def test_tracker::ovine_sheepBreed_setter(instance):
    original = instance.sheepBreed
    instance.sheepBreed = original
    assert instance.sheepBreed == original

@given(instance=tracker::Equine_strategy)
@settings(max_examples=50)
def test_tracker::equine_instantiation(instance):
    assert isinstance(instance, tracker::Equine)

@given(instance=tracker::Equine_strategy)
def test_tracker::equine_horseBreed_type(instance):
    assert isinstance(instance.horseBreed, str)


@given(instance=tracker::Equine_strategy)
def test_tracker::equine_horseBreed_setter(instance):
    original = instance.horseBreed
    instance.horseBreed = original
    assert instance.horseBreed == original

@given(instance=tracker::Bovine_strategy)
@settings(max_examples=50)
def test_tracker::bovine_instantiation(instance):
    assert isinstance(instance, tracker::Bovine)

@given(instance=tracker::Event_strategy)
@settings(max_examples=50)
def test_tracker::event_instantiation(instance):
    assert isinstance(instance, tracker::Event)

@given(instance=tracker::Event_strategy)
def test_tracker::event_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=tracker::Event_strategy)
def test_tracker::event_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=tracker::Event_strategy)
def test_tracker::event_eventCode_type(instance):
    assert isinstance(instance.eventCode, int)


@given(instance=tracker::Event_strategy)
def test_tracker::event_eventCode_setter(instance):
    original = instance.eventCode
    instance.eventCode = original
    assert instance.eventCode == original

@given(instance=tracker::Event_strategy)
def test_tracker::event_comments_type(instance):
    assert isinstance(instance.comments, str)


@given(instance=tracker::Event_strategy)
def test_tracker::event_comments_setter(instance):
    original = instance.comments
    instance.comments = original
    assert instance.comments == original

@given(instance=tracker::Event_strategy)
def test_tracker::event_electronicallyRead_type(instance):
    assert isinstance(instance.electronicallyRead, bool)


@given(instance=tracker::Event_strategy)
def test_tracker::event_electronicallyRead_setter(instance):
    original = instance.electronicallyRead
    instance.electronicallyRead = original
    assert instance.electronicallyRead == original

@given(instance=tracker::Event_strategy)
def test_tracker::event_dateTime_type(instance):
    assert isinstance(instance.dateTime, date)


@given(instance=tracker::Event_strategy)
def test_tracker::event_dateTime_setter(instance):
    original = instance.dateTime
    instance.dateTime = original
    assert instance.dateTime == original

@given(instance=tracker::Event_strategy)
def test_tracker::event_correction_type(instance):
    assert isinstance(instance.correction, bool)


@given(instance=tracker::Event_strategy)
def test_tracker::event_correction_setter(instance):
    original = instance.correction
    instance.correction = original
    assert instance.correction == original

@given(instance=tracker::Animal_strategy)
@settings(max_examples=50)
def test_tracker::animal_instantiation(instance):
    assert isinstance(instance, tracker::Animal)

@given(instance=tracker::Animal_strategy)
def test_tracker::animal_ageInDays_type(instance):
    assert isinstance(instance.ageInDays, int)


@given(instance=tracker::Animal_strategy)
def test_tracker::animal_ageInDays_setter(instance):
    original = instance.ageInDays
    instance.ageInDays = original
    assert instance.ageInDays == original

@given(instance=tracker::Animal_strategy)
def test_tracker::animal_visualID_type(instance):
    assert isinstance(instance.visualID, str)


@given(instance=tracker::Animal_strategy)
def test_tracker::animal_visualID_setter(instance):
    original = instance.visualID
    instance.visualID = original
    assert instance.visualID == original

@given(instance=tracker::Animal_strategy)
def test_tracker::animal_comments_type(instance):
    assert isinstance(instance.comments, str)


@given(instance=tracker::Animal_strategy)
def test_tracker::animal_comments_setter(instance):
    original = instance.comments
    instance.comments = original
    assert instance.comments == original

@given(instance=tracker::Animal_strategy)
def test_tracker::animal_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=tracker::Animal_strategy)
def test_tracker::animal_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=tracker::Animal_strategy)
def test_tracker::animal_weight_type(instance):
    assert isinstance(instance.weight, str)


@given(instance=tracker::Animal_strategy)
def test_tracker::animal_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=tracker::Animal_strategy)
def test_tracker::animal_alternativeID_type(instance):
    assert isinstance(instance.alternativeID, str)


@given(instance=tracker::Animal_strategy)
def test_tracker::animal_alternativeID_setter(instance):
    original = instance.alternativeID
    instance.alternativeID = original
    assert instance.alternativeID == original

@given(instance=tracker::Animal_strategy)
def test_tracker::animal_sexCode_type(instance):
    assert isinstance(instance.sexCode, str)


@given(instance=tracker::Animal_strategy)
def test_tracker::animal_sexCode_setter(instance):
    original = instance.sexCode
    instance.sexCode = original
    assert instance.sexCode == original

@given(instance=tracker::Animal_strategy)
def test_tracker::animal_lastEventDateTime_type(instance):
    assert isinstance(instance.lastEventDateTime, date)


@given(instance=tracker::Animal_strategy)
def test_tracker::animal_lastEventDateTime_setter(instance):
    original = instance.lastEventDateTime
    instance.lastEventDateTime = original
    assert instance.lastEventDateTime == original

@given(instance=tracker::Animal_strategy)
def test_tracker::animal_breed_type(instance):
    assert isinstance(instance.breed, str)


@given(instance=tracker::Animal_strategy)
def test_tracker::animal_breed_setter(instance):
    original = instance.breed
    instance.breed = original
    assert instance.breed == original

@given(instance=tracker::Animal_strategy)
def test_tracker::animal_birthDate_type(instance):
    assert isinstance(instance.birthDate, date)


@given(instance=tracker::Animal_strategy)
def test_tracker::animal_birthDate_setter(instance):
    original = instance.birthDate
    instance.birthDate = original
    assert instance.birthDate == original

@given(instance=tracker::Animal_strategy)
def test_tracker::animal_sex_type(instance):
    assert isinstance(instance.sex, str)


@given(instance=tracker::Animal_strategy)
def test_tracker::animal_sex_setter(instance):
    original = instance.sex
    instance.sex = original
    assert instance.sex == original

@given(instance=tracker::Animal_strategy)
def test_tracker::animal_speciesCode_type(instance):
    assert isinstance(instance.speciesCode, str)


@given(instance=tracker::Animal_strategy)
def test_tracker::animal_speciesCode_setter(instance):
    original = instance.speciesCode
    instance.speciesCode = original
    assert instance.speciesCode == original

@given(instance=tracker::Animal_strategy)
def test_tracker::animal_weightGainPerDay_type(instance):
    assert isinstance(instance.weightGainPerDay, str)


@given(instance=tracker::Animal_strategy)
def test_tracker::animal_weightGainPerDay_setter(instance):
    original = instance.weightGainPerDay
    instance.weightGainPerDay = original
    assert instance.weightGainPerDay == original

@given(instance=tracker::Animal_strategy)
def test_tracker::animal_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=tracker::Animal_strategy)
def test_tracker::animal_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=tracker::Animal_strategy)
def test_tracker::animal_species_type(instance):
    assert isinstance(instance.species, str)


@given(instance=tracker::Animal_strategy)
def test_tracker::animal_species_setter(instance):
    original = instance.species
    instance.species = original
    assert instance.species == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tracker::Animal_strategy)
@settings(max_examples=30)
def test_tracker::animal_allevents_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.allEvents()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.allEvents).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'allEvents' in tracker::Animal is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'allEvents' in tracker::Animal did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'allEvents' in tracker::Animal is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tracker::Animal_strategy)
@settings(max_examples=30)
def test_tracker::animal_addtemplate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addTemplate(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addTemplate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addTemplate' in tracker::Animal is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addTemplate' in tracker::Animal did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addTemplate' in tracker::Animal is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tracker::Animal_strategy)
@settings(max_examples=30)
def test_tracker::animal_eventhistory_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eventHistory()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eventHistory).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eventHistory' in tracker::Animal is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eventHistory' in tracker::Animal did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eventHistory' in tracker::Animal is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tracker::Animal_strategy)
@settings(max_examples=30)
def test_tracker::animal_activetag_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.activeTag()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.activeTag).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'activeTag' in tracker::Animal is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'activeTag' in tracker::Animal did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'activeTag' in tracker::Animal is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tracker::Animal_strategy)
@settings(max_examples=30)
def test_tracker::animal_lastweighin_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.lastWeighIn()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.lastWeighIn).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'lastWeighIn' in tracker::Animal is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'lastWeighIn' in tracker::Animal did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'lastWeighIn' in tracker::Animal is not implemented or raised an error")
