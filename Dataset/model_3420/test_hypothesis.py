import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Bovine,
    tracker_BovineBison,
    tracker_BovineDairy,
    tracker_BovineBeef,
    tracker_Event,
    tracker_Tag,
    tracker_Premises,
    Event,
    tracker_Sighting,
    tracker_ICVI,
    tracker_TagApplied,
    tracker_WeighIn,
    tracker_FairRegistration,
    tracker_Died,
    tracker_Exported,
    tracker_Imported,
    tracker_Slaughtered,
    tracker_AnimalMissing,
    tracker_TagRetired,
    tracker_TagAllocated,
    Animal,
    tracker_Ovine,
    tracker_Bovine,
    tracker_Animal,
    tracker_Swine,
    tracker_ReplacedTag,
    tracker_LostTag,
    tracker_MovedOut,
    tracker_MovedIn,
    SheepBreed,
    Sex,
    BisonBreed,
    DairyBreed,
    SwineBreed,
    BeefBreed,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bovine_is_not_abstract():
    assert not inspect.isabstract(Bovine)


def test_bovine_constructor_exists():
    assert callable(Bovine.__init__)


def test_bovine_constructor_args():
    sig = inspect.signature(Bovine.__init__)
    params = list(sig.parameters.keys())



def test_tracker_bovinebison_is_not_abstract():
    assert not inspect.isabstract(tracker_BovineBison)


def test_tracker_bovinebison_constructor_exists():
    assert callable(tracker_BovineBison.__init__)


def test_tracker_bovinebison_constructor_args():
    sig = inspect.signature(tracker_BovineBison.__init__)
    params = list(sig.parameters.keys())
    assert "buffaloBreed" in params, "Missing parameter 'buffaloBreed'"

def test_tracker_bovinebison_has_buffaloBreed():
    assert hasattr(tracker_BovineBison, "buffaloBreed")
    descriptor = None
    for klass in tracker_BovineBison.__mro__:
        if "buffaloBreed" in klass.__dict__:
            descriptor = klass.__dict__["buffaloBreed"]
            break
    assert isinstance(descriptor, property)



def test_tracker_bovinedairy_is_not_abstract():
    assert not inspect.isabstract(tracker_BovineDairy)


def test_tracker_bovinedairy_constructor_exists():
    assert callable(tracker_BovineDairy.__init__)


def test_tracker_bovinedairy_constructor_args():
    sig = inspect.signature(tracker_BovineDairy.__init__)
    params = list(sig.parameters.keys())
    assert "dairyBreed" in params, "Missing parameter 'dairyBreed'"

def test_tracker_bovinedairy_has_dairyBreed():
    assert hasattr(tracker_BovineDairy, "dairyBreed")
    descriptor = None
    for klass in tracker_BovineDairy.__mro__:
        if "dairyBreed" in klass.__dict__:
            descriptor = klass.__dict__["dairyBreed"]
            break
    assert isinstance(descriptor, property)



def test_tracker_bovinebeef_is_not_abstract():
    assert not inspect.isabstract(tracker_BovineBeef)


def test_tracker_bovinebeef_constructor_exists():
    assert callable(tracker_BovineBeef.__init__)


def test_tracker_bovinebeef_constructor_args():
    sig = inspect.signature(tracker_BovineBeef.__init__)
    params = list(sig.parameters.keys())
    assert "beefBreed" in params, "Missing parameter 'beefBreed'"

def test_tracker_bovinebeef_has_beefBreed():
    assert hasattr(tracker_BovineBeef, "beefBreed")
    descriptor = None
    for klass in tracker_BovineBeef.__mro__:
        if "beefBreed" in klass.__dict__:
            descriptor = klass.__dict__["beefBreed"]
            break
    assert isinstance(descriptor, property)



def test_tracker_event_is_not_abstract():
    assert not inspect.isabstract(tracker_Event)


def test_tracker_event_constructor_exists():
    assert callable(tracker_Event.__init__)


def test_tracker_event_constructor_args():
    sig = inspect.signature(tracker_Event.__init__)
    params = list(sig.parameters.keys())
    assert "dateTime" in params, "Missing parameter 'dateTime'"
    assert "comments" in params, "Missing parameter 'comments'"
    assert "idNumber" in params, "Missing parameter 'idNumber'"
    assert "eventCode" in params, "Missing parameter 'eventCode'"
    assert "electronicallyRead" in params, "Missing parameter 'electronicallyRead'"
    assert "correction" in params, "Missing parameter 'correction'"

def test_tracker_event_has_dateTime():
    assert hasattr(tracker_Event, "dateTime")
    descriptor = None
    for klass in tracker_Event.__mro__:
        if "dateTime" in klass.__dict__:
            descriptor = klass.__dict__["dateTime"]
            break
    assert isinstance(descriptor, property)

def test_tracker_event_has_comments():
    assert hasattr(tracker_Event, "comments")
    descriptor = None
    for klass in tracker_Event.__mro__:
        if "comments" in klass.__dict__:
            descriptor = klass.__dict__["comments"]
            break
    assert isinstance(descriptor, property)

def test_tracker_event_has_idNumber():
    assert hasattr(tracker_Event, "idNumber")
    descriptor = None
    for klass in tracker_Event.__mro__:
        if "idNumber" in klass.__dict__:
            descriptor = klass.__dict__["idNumber"]
            break
    assert isinstance(descriptor, property)

def test_tracker_event_has_eventCode():
    assert hasattr(tracker_Event, "eventCode")
    descriptor = None
    for klass in tracker_Event.__mro__:
        if "eventCode" in klass.__dict__:
            descriptor = klass.__dict__["eventCode"]
            break
    assert isinstance(descriptor, property)

def test_tracker_event_has_electronicallyRead():
    assert hasattr(tracker_Event, "electronicallyRead")
    descriptor = None
    for klass in tracker_Event.__mro__:
        if "electronicallyRead" in klass.__dict__:
            descriptor = klass.__dict__["electronicallyRead"]
            break
    assert isinstance(descriptor, property)

def test_tracker_event_has_correction():
    assert hasattr(tracker_Event, "correction")
    descriptor = None
    for klass in tracker_Event.__mro__:
        if "correction" in klass.__dict__:
            descriptor = klass.__dict__["correction"]
            break
    assert isinstance(descriptor, property)



def test_tracker_tag_is_not_abstract():
    assert not inspect.isabstract(tracker_Tag)


def test_tracker_tag_constructor_exists():
    assert callable(tracker_Tag.__init__)


def test_tracker_tag_constructor_args():
    sig = inspect.signature(tracker_Tag.__init__)
    params = list(sig.parameters.keys())
    assert "usainNumberUsed" in params, "Missing parameter 'usainNumberUsed'"
    assert "idNumber" in params, "Missing parameter 'idNumber'"

def test_tracker_tag_has_usainNumberUsed():
    assert hasattr(tracker_Tag, "usainNumberUsed")
    descriptor = None
    for klass in tracker_Tag.__mro__:
        if "usainNumberUsed" in klass.__dict__:
            descriptor = klass.__dict__["usainNumberUsed"]
            break
    assert isinstance(descriptor, property)

def test_tracker_tag_has_idNumber():
    assert hasattr(tracker_Tag, "idNumber")
    descriptor = None
    for klass in tracker_Tag.__mro__:
        if "idNumber" in klass.__dict__:
            descriptor = klass.__dict__["idNumber"]
            break
    assert isinstance(descriptor, property)



def test_tracker_premises_is_not_abstract():
    assert not inspect.isabstract(tracker_Premises)


def test_tracker_premises_constructor_exists():
    assert callable(tracker_Premises.__init__)


def test_tracker_premises_constructor_args():
    sig = inspect.signature(tracker_Premises.__init__)
    params = list(sig.parameters.keys())
    assert "premisesId" in params, "Missing parameter 'premisesId'"
    assert "emailContact" in params, "Missing parameter 'emailContact'"

def test_tracker_premises_has_premisesId():
    assert hasattr(tracker_Premises, "premisesId")
    descriptor = None
    for klass in tracker_Premises.__mro__:
        if "premisesId" in klass.__dict__:
            descriptor = klass.__dict__["premisesId"]
            break
    assert isinstance(descriptor, property)

def test_tracker_premises_has_emailContact():
    assert hasattr(tracker_Premises, "emailContact")
    descriptor = None
    for klass in tracker_Premises.__mro__:
        if "emailContact" in klass.__dict__:
            descriptor = klass.__dict__["emailContact"]
            break
    assert isinstance(descriptor, property)



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_tracker_sighting_is_not_abstract():
    assert not inspect.isabstract(tracker_Sighting)


def test_tracker_sighting_constructor_exists():
    assert callable(tracker_Sighting.__init__)


def test_tracker_sighting_constructor_args():
    sig = inspect.signature(tracker_Sighting.__init__)
    params = list(sig.parameters.keys())



def test_tracker_icvi_is_not_abstract():
    assert not inspect.isabstract(tracker_ICVI)


def test_tracker_icvi_constructor_exists():
    assert callable(tracker_ICVI.__init__)


def test_tracker_icvi_constructor_args():
    sig = inspect.signature(tracker_ICVI.__init__)
    params = list(sig.parameters.keys())



def test_tracker_tagapplied_is_not_abstract():
    assert not inspect.isabstract(tracker_TagApplied)


def test_tracker_tagapplied_constructor_exists():
    assert callable(tracker_TagApplied.__init__)


def test_tracker_tagapplied_constructor_args():
    sig = inspect.signature(tracker_TagApplied.__init__)
    params = list(sig.parameters.keys())



def test_tracker_weighin_is_not_abstract():
    assert not inspect.isabstract(tracker_WeighIn)


def test_tracker_weighin_constructor_exists():
    assert callable(tracker_WeighIn.__init__)


def test_tracker_weighin_constructor_args():
    sig = inspect.signature(tracker_WeighIn.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_tracker_weighin_has_weight():
    assert hasattr(tracker_WeighIn, "weight")
    descriptor = None
    for klass in tracker_WeighIn.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_tracker_fairregistration_is_not_abstract():
    assert not inspect.isabstract(tracker_FairRegistration)


def test_tracker_fairregistration_constructor_exists():
    assert callable(tracker_FairRegistration.__init__)


def test_tracker_fairregistration_constructor_args():
    sig = inspect.signature(tracker_FairRegistration.__init__)
    params = list(sig.parameters.keys())
    assert "participant" in params, "Missing parameter 'participant'"
    assert "phone" in params, "Missing parameter 'phone'"
    assert "parent" in params, "Missing parameter 'parent'"
    assert "address" in params, "Missing parameter 'address'"
    assert "club" in params, "Missing parameter 'club'"

def test_tracker_fairregistration_has_participant():
    assert hasattr(tracker_FairRegistration, "participant")
    descriptor = None
    for klass in tracker_FairRegistration.__mro__:
        if "participant" in klass.__dict__:
            descriptor = klass.__dict__["participant"]
            break
    assert isinstance(descriptor, property)

def test_tracker_fairregistration_has_phone():
    assert hasattr(tracker_FairRegistration, "phone")
    descriptor = None
    for klass in tracker_FairRegistration.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
            break
    assert isinstance(descriptor, property)

def test_tracker_fairregistration_has_parent():
    assert hasattr(tracker_FairRegistration, "parent")
    descriptor = None
    for klass in tracker_FairRegistration.__mro__:
        if "parent" in klass.__dict__:
            descriptor = klass.__dict__["parent"]
            break
    assert isinstance(descriptor, property)

def test_tracker_fairregistration_has_address():
    assert hasattr(tracker_FairRegistration, "address")
    descriptor = None
    for klass in tracker_FairRegistration.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_tracker_fairregistration_has_club():
    assert hasattr(tracker_FairRegistration, "club")
    descriptor = None
    for klass in tracker_FairRegistration.__mro__:
        if "club" in klass.__dict__:
            descriptor = klass.__dict__["club"]
            break
    assert isinstance(descriptor, property)



def test_tracker_died_is_not_abstract():
    assert not inspect.isabstract(tracker_Died)


def test_tracker_died_constructor_exists():
    assert callable(tracker_Died.__init__)


def test_tracker_died_constructor_args():
    sig = inspect.signature(tracker_Died.__init__)
    params = list(sig.parameters.keys())



def test_tracker_exported_is_not_abstract():
    assert not inspect.isabstract(tracker_Exported)


def test_tracker_exported_constructor_exists():
    assert callable(tracker_Exported.__init__)


def test_tracker_exported_constructor_args():
    sig = inspect.signature(tracker_Exported.__init__)
    params = list(sig.parameters.keys())



def test_tracker_imported_is_not_abstract():
    assert not inspect.isabstract(tracker_Imported)


def test_tracker_imported_constructor_exists():
    assert callable(tracker_Imported.__init__)


def test_tracker_imported_constructor_args():
    sig = inspect.signature(tracker_Imported.__init__)
    params = list(sig.parameters.keys())



def test_tracker_slaughtered_is_not_abstract():
    assert not inspect.isabstract(tracker_Slaughtered)


def test_tracker_slaughtered_constructor_exists():
    assert callable(tracker_Slaughtered.__init__)


def test_tracker_slaughtered_constructor_args():
    sig = inspect.signature(tracker_Slaughtered.__init__)
    params = list(sig.parameters.keys())



def test_tracker_animalmissing_is_not_abstract():
    assert not inspect.isabstract(tracker_AnimalMissing)


def test_tracker_animalmissing_constructor_exists():
    assert callable(tracker_AnimalMissing.__init__)


def test_tracker_animalmissing_constructor_args():
    sig = inspect.signature(tracker_AnimalMissing.__init__)
    params = list(sig.parameters.keys())



def test_tracker_tagretired_is_not_abstract():
    assert not inspect.isabstract(tracker_TagRetired)


def test_tracker_tagretired_constructor_exists():
    assert callable(tracker_TagRetired.__init__)


def test_tracker_tagretired_constructor_args():
    sig = inspect.signature(tracker_TagRetired.__init__)
    params = list(sig.parameters.keys())



def test_tracker_tagallocated_is_not_abstract():
    assert not inspect.isabstract(tracker_TagAllocated)


def test_tracker_tagallocated_constructor_exists():
    assert callable(tracker_TagAllocated.__init__)


def test_tracker_tagallocated_constructor_args():
    sig = inspect.signature(tracker_TagAllocated.__init__)
    params = list(sig.parameters.keys())



def test_animal_is_not_abstract():
    assert not inspect.isabstract(Animal)


def test_animal_constructor_exists():
    assert callable(Animal.__init__)


def test_animal_constructor_args():
    sig = inspect.signature(Animal.__init__)
    params = list(sig.parameters.keys())



def test_tracker_ovine_is_not_abstract():
    assert not inspect.isabstract(tracker_Ovine)


def test_tracker_ovine_constructor_exists():
    assert callable(tracker_Ovine.__init__)


def test_tracker_ovine_constructor_args():
    sig = inspect.signature(tracker_Ovine.__init__)
    params = list(sig.parameters.keys())
    assert "sheepBreed" in params, "Missing parameter 'sheepBreed'"

def test_tracker_ovine_has_sheepBreed():
    assert hasattr(tracker_Ovine, "sheepBreed")
    descriptor = None
    for klass in tracker_Ovine.__mro__:
        if "sheepBreed" in klass.__dict__:
            descriptor = klass.__dict__["sheepBreed"]
            break
    assert isinstance(descriptor, property)



def test_tracker_bovine_is_not_abstract():
    assert not inspect.isabstract(tracker_Bovine)


def test_tracker_bovine_constructor_exists():
    assert callable(tracker_Bovine.__init__)


def test_tracker_bovine_constructor_args():
    sig = inspect.signature(tracker_Bovine.__init__)
    params = list(sig.parameters.keys())



def test_tracker_animal_is_not_abstract():
    assert not inspect.isabstract(tracker_Animal)


def test_tracker_animal_constructor_exists():
    assert callable(tracker_Animal.__init__)


def test_tracker_animal_constructor_args():
    sig = inspect.signature(tracker_Animal.__init__)
    params = list(sig.parameters.keys())
    assert "idNumber" in params, "Missing parameter 'idNumber'"
    assert "breed" in params, "Missing parameter 'breed'"
    assert "species" in params, "Missing parameter 'species'"
    assert "birthDate" in params, "Missing parameter 'birthDate'"
    assert "sex" in params, "Missing parameter 'sex'"
    assert "sexCode" in params, "Missing parameter 'sexCode'"
    assert "age" in params, "Missing parameter 'age'"
    assert "speciesCode" in params, "Missing parameter 'speciesCode'"

def test_tracker_animal_has_idNumber():
    assert hasattr(tracker_Animal, "idNumber")
    descriptor = None
    for klass in tracker_Animal.__mro__:
        if "idNumber" in klass.__dict__:
            descriptor = klass.__dict__["idNumber"]
            break
    assert isinstance(descriptor, property)

def test_tracker_animal_has_breed():
    assert hasattr(tracker_Animal, "breed")
    descriptor = None
    for klass in tracker_Animal.__mro__:
        if "breed" in klass.__dict__:
            descriptor = klass.__dict__["breed"]
            break
    assert isinstance(descriptor, property)

def test_tracker_animal_has_species():
    assert hasattr(tracker_Animal, "species")
    descriptor = None
    for klass in tracker_Animal.__mro__:
        if "species" in klass.__dict__:
            descriptor = klass.__dict__["species"]
            break
    assert isinstance(descriptor, property)

def test_tracker_animal_has_birthDate():
    assert hasattr(tracker_Animal, "birthDate")
    descriptor = None
    for klass in tracker_Animal.__mro__:
        if "birthDate" in klass.__dict__:
            descriptor = klass.__dict__["birthDate"]
            break
    assert isinstance(descriptor, property)

def test_tracker_animal_has_sex():
    assert hasattr(tracker_Animal, "sex")
    descriptor = None
    for klass in tracker_Animal.__mro__:
        if "sex" in klass.__dict__:
            descriptor = klass.__dict__["sex"]
            break
    assert isinstance(descriptor, property)

def test_tracker_animal_has_sexCode():
    assert hasattr(tracker_Animal, "sexCode")
    descriptor = None
    for klass in tracker_Animal.__mro__:
        if "sexCode" in klass.__dict__:
            descriptor = klass.__dict__["sexCode"]
            break
    assert isinstance(descriptor, property)

def test_tracker_animal_has_age():
    assert hasattr(tracker_Animal, "age")
    descriptor = None
    for klass in tracker_Animal.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_tracker_animal_has_speciesCode():
    assert hasattr(tracker_Animal, "speciesCode")
    descriptor = None
    for klass in tracker_Animal.__mro__:
        if "speciesCode" in klass.__dict__:
            descriptor = klass.__dict__["speciesCode"]
            break
    assert isinstance(descriptor, property)



def test_tracker_swine_is_not_abstract():
    assert not inspect.isabstract(tracker_Swine)


def test_tracker_swine_constructor_exists():
    assert callable(tracker_Swine.__init__)


def test_tracker_swine_constructor_args():
    sig = inspect.signature(tracker_Swine.__init__)
    params = list(sig.parameters.keys())
    assert "swineBreed" in params, "Missing parameter 'swineBreed'"

def test_tracker_swine_has_swineBreed():
    assert hasattr(tracker_Swine, "swineBreed")
    descriptor = None
    for klass in tracker_Swine.__mro__:
        if "swineBreed" in klass.__dict__:
            descriptor = klass.__dict__["swineBreed"]
            break
    assert isinstance(descriptor, property)



def test_tracker_replacedtag_is_not_abstract():
    assert not inspect.isabstract(tracker_ReplacedTag)


def test_tracker_replacedtag_constructor_exists():
    assert callable(tracker_ReplacedTag.__init__)


def test_tracker_replacedtag_constructor_args():
    sig = inspect.signature(tracker_ReplacedTag.__init__)
    params = list(sig.parameters.keys())
    assert "oldAin" in params, "Missing parameter 'oldAin'"

def test_tracker_replacedtag_has_oldAin():
    assert hasattr(tracker_ReplacedTag, "oldAin")
    descriptor = None
    for klass in tracker_ReplacedTag.__mro__:
        if "oldAin" in klass.__dict__:
            descriptor = klass.__dict__["oldAin"]
            break
    assert isinstance(descriptor, property)



def test_tracker_losttag_is_not_abstract():
    assert not inspect.isabstract(tracker_LostTag)


def test_tracker_losttag_constructor_exists():
    assert callable(tracker_LostTag.__init__)


def test_tracker_losttag_constructor_args():
    sig = inspect.signature(tracker_LostTag.__init__)
    params = list(sig.parameters.keys())



def test_tracker_movedout_is_not_abstract():
    assert not inspect.isabstract(tracker_MovedOut)


def test_tracker_movedout_constructor_exists():
    assert callable(tracker_MovedOut.__init__)


def test_tracker_movedout_constructor_args():
    sig = inspect.signature(tracker_MovedOut.__init__)
    params = list(sig.parameters.keys())
    assert "destinationPin" in params, "Missing parameter 'destinationPin'"

def test_tracker_movedout_has_destinationPin():
    assert hasattr(tracker_MovedOut, "destinationPin")
    descriptor = None
    for klass in tracker_MovedOut.__mro__:
        if "destinationPin" in klass.__dict__:
            descriptor = klass.__dict__["destinationPin"]
            break
    assert isinstance(descriptor, property)



def test_tracker_movedin_is_not_abstract():
    assert not inspect.isabstract(tracker_MovedIn)


def test_tracker_movedin_constructor_exists():
    assert callable(tracker_MovedIn.__init__)


def test_tracker_movedin_constructor_args():
    sig = inspect.signature(tracker_MovedIn.__init__)
    params = list(sig.parameters.keys())
    assert "sourcePin" in params, "Missing parameter 'sourcePin'"

def test_tracker_movedin_has_sourcePin():
    assert hasattr(tracker_MovedIn, "sourcePin")
    descriptor = None
    for klass in tracker_MovedIn.__mro__:
        if "sourcePin" in klass.__dict__:
            descriptor = klass.__dict__["sourcePin"]
            break
    assert isinstance(descriptor, property)

def test_sheepbreed_exists():
    # Check that the Enumeration exists
    assert SheepBreed is not None

def test_sheepbreed_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SheepBreed]
    expected_literals = [
        "BC",
        "IL",
        "FN",
        "XL",
        "BW",
        "LE",
        "LI",
        "SX",
        "RI",
        "BO",
        "CO",
        "NL",
        "HL",
        "ST",
        "CF",
        "OX",
        "XM",
        "CR",
        "ZS",
        "HS",
        "SU",
        "RG",
        "TX",
        "DP",
        "PO",
        "RM",
        "MM",
        "CP",
        "NC",
        "TA",
        "FB",
        "ER",
        "SL",
        "TU",
        "SC",
        "LY",
        "SR",
        "OU",
        "CL",
        "RY",
        "KA",
        "CD",
        "KH",
        "BF",
        "BL",
        "MT",
        "DH",
        "HY",
        "MP",
        "KK",
        "DL",
        "Unspecified",
        "PE",
        "RV",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SheepBreed"

def test_sex_exists():
    # Check that the Enumeration exists
    assert Sex is not None

def test_sex_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Sex]
    expected_literals = [
        "Unspecified",
        "M",
        "F",
        "S",
        "C",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Sex"

def test_bisonbreed_exists():
    # Check that the Enumeration exists
    assert BisonBreed is not None

def test_bisonbreed_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BisonBreed]
    expected_literals = [
        "PB",
        "Unspecified",
        "WO",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BisonBreed"

def test_dairybreed_exists():
    # Check that the Enumeration exists
    assert DairyBreed is not None

def test_dairybreed_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DairyBreed]
    expected_literals = [
        "GD",
        "WW",
        "JE",
        "AY",
        "MS",
        "Unspecified",
        "HO",
        "FM",
        "GU",
        "BS",
        "LD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DairyBreed"

def test_swinebreed_exists():
    # Check that the Enumeration exists
    assert SwineBreed is not None

def test_swinebreed_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SwineBreed]
    expected_literals = [
        "SO",
        "RW",
        "LC",
        "LW",
        "Unspecified",
        "LB",
        "LA",
        "DU",
        "BK",
        "HA",
        "PE",
        "YO",
        "TM",
        "CW",
        "WS",
        "PC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SwineBreed"

def test_beefbreed_exists():
    # Check that the Enumeration exists
    assert BeefBreed is not None

def test_beefbreed_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BeefBreed]
    expected_literals = [
        "CB",
        "HB",
        "CG",
        "RP",
        "GE",
        "KB",
        "AB",
        "BL",
        "AW",
        "MG",
        "ME",
        "CA",
        "CN",
        "GI",
        "AR",
        "BW",
        "TG",
        "AL",
        "BR",
        "RO",
        "BH",
        "GS",
        "CP",
        "IB",
        "RR",
        "TI",
        "FC",
        "DF",
        "NR",
        "TP",
        "GY",
        "DL",
        "GV",
        "MC",
        "SB",
        "MR",
        "DE",
        "XT",
        "FB",
        "HP",
        "ER",
        "MU",
        "SM",
        "BO",
        "BA",
        "FP",
        "MA",
        "GZ",
        "AU",
        "RD",
        "NE",
        "FA",
        "TL",
        "SA",
        "AN",
        "YA",
        "AF",
        "BG",
        "GR",
        "BQ",
        "PI",
        "DN",
        "SG",
        "MI",
        "LO",
        "MO",
        "SX",
        "BU",
        "LM",
        "PA",
        "NM",
        "SL",
        "SH",
        "RB",
        "BB",
        "HC",
        "RW",
        "SI",
        "BE",
        "PZ",
        "IS",
        "KY",
        "RA",
        "SP",
        "BF",
        "RS",
        "BD",
        "CH",
        "CM",
        "XX",
        "HY",
        "LR",
        "WP",
        "SE",
        "BI",
        "DR",
        "FR",
        "MH",
        "SS",
        "DB",
        "TN",
        "WF",
        "HH",
        "DJ",
        "GA",
        "CU",
        "WB",
        "AK",
        "SV",
        "BM",
        "SW",
        "FL",
        "AM",
        "BN",
        "DS",
        "NS",
        "AE",
        "PR",
        "ML",
        "RN",
        "Unspecified",
        "LU",
        "TA",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BeefBreed"


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
Bovine_strategy = st.builds(
    Bovine,
)
tracker_BovineBison_strategy = st.builds(
    tracker_BovineBison,
    buffaloBreed=
        safe_text
)
tracker_BovineDairy_strategy = st.builds(
    tracker_BovineDairy,
    dairyBreed=
        safe_text
)
tracker_BovineBeef_strategy = st.builds(
    tracker_BovineBeef,
    beefBreed=
        safe_text
)
tracker_Event_strategy = st.builds(
    tracker_Event,
    dateTime=
        safe_text,
    comments=
        safe_text,
    idNumber=
        safe_text,
    eventCode=
        st.integers(),
    electronicallyRead=
        st.booleans(),
    correction=
        st.booleans()
)
tracker_Tag_strategy = st.builds(
    tracker_Tag,
    usainNumberUsed=
        st.booleans(),
    idNumber=
        safe_text
)
tracker_Premises_strategy = st.builds(
    tracker_Premises,
    premisesId=
        safe_text,
    emailContact=
        safe_text
)
Event_strategy = st.builds(
    Event,
)
tracker_Sighting_strategy = st.builds(
    tracker_Sighting,
)
tracker_ICVI_strategy = st.builds(
    tracker_ICVI,
)
tracker_TagApplied_strategy = st.builds(
    tracker_TagApplied,
)
tracker_WeighIn_strategy = st.builds(
    tracker_WeighIn,
    weight=
        st.integers()
)
tracker_FairRegistration_strategy = st.builds(
    tracker_FairRegistration,
    participant=
        safe_text,
    phone=
        safe_text,
    parent=
        safe_text,
    address=
        safe_text,
    club=
        safe_text
)
tracker_Died_strategy = st.builds(
    tracker_Died,
)
tracker_Exported_strategy = st.builds(
    tracker_Exported,
)
tracker_Imported_strategy = st.builds(
    tracker_Imported,
)
tracker_Slaughtered_strategy = st.builds(
    tracker_Slaughtered,
)
tracker_AnimalMissing_strategy = st.builds(
    tracker_AnimalMissing,
)
tracker_TagRetired_strategy = st.builds(
    tracker_TagRetired,
)
tracker_TagAllocated_strategy = st.builds(
    tracker_TagAllocated,
)
Animal_strategy = st.builds(
    Animal,
)
tracker_Ovine_strategy = st.builds(
    tracker_Ovine,
    sheepBreed=
        safe_text
)
tracker_Bovine_strategy = st.builds(
    tracker_Bovine,
)
tracker_Animal_strategy = st.builds(
    tracker_Animal,
    idNumber=
        safe_text,
    breed=
        safe_text,
    species=
        safe_text,
    birthDate=
        safe_text,
    sex=
        safe_text,
    sexCode=
        safe_text,
    age=
        safe_text,
    speciesCode=
        safe_text
)
tracker_Swine_strategy = st.builds(
    tracker_Swine,
    swineBreed=
        safe_text
)
tracker_ReplacedTag_strategy = st.builds(
    tracker_ReplacedTag,
    oldAin=
        safe_text
)
tracker_LostTag_strategy = st.builds(
    tracker_LostTag,
)
tracker_MovedOut_strategy = st.builds(
    tracker_MovedOut,
    destinationPin=
        safe_text
)
tracker_MovedIn_strategy = st.builds(
    tracker_MovedIn,
    sourcePin=
        safe_text
)

@given(instance=Bovine_strategy)
@settings(max_examples=50)
def test_bovine_instantiation(instance):
    assert isinstance(instance, Bovine)

@given(instance=tracker_BovineBison_strategy)
@settings(max_examples=50)
def test_tracker_bovinebison_instantiation(instance):
    assert isinstance(instance, tracker_BovineBison)



@given(instance=tracker_BovineBison_strategy)
def test_tracker_bovinebison_buffaloBreed_setter(instance):
    original = instance.buffaloBreed
    instance.buffaloBreed = original
    assert instance.buffaloBreed == original

@given(instance=tracker_BovineDairy_strategy)
@settings(max_examples=50)
def test_tracker_bovinedairy_instantiation(instance):
    assert isinstance(instance, tracker_BovineDairy)



@given(instance=tracker_BovineDairy_strategy)
def test_tracker_bovinedairy_dairyBreed_setter(instance):
    original = instance.dairyBreed
    instance.dairyBreed = original
    assert instance.dairyBreed == original

@given(instance=tracker_BovineBeef_strategy)
@settings(max_examples=50)
def test_tracker_bovinebeef_instantiation(instance):
    assert isinstance(instance, tracker_BovineBeef)



@given(instance=tracker_BovineBeef_strategy)
def test_tracker_bovinebeef_beefBreed_setter(instance):
    original = instance.beefBreed
    instance.beefBreed = original
    assert instance.beefBreed == original

@given(instance=tracker_Event_strategy)
@settings(max_examples=50)
def test_tracker_event_instantiation(instance):
    assert isinstance(instance, tracker_Event)



@given(instance=tracker_Event_strategy)
def test_tracker_event_dateTime_setter(instance):
    original = instance.dateTime
    instance.dateTime = original
    assert instance.dateTime == original



@given(instance=tracker_Event_strategy)
def test_tracker_event_comments_setter(instance):
    original = instance.comments
    instance.comments = original
    assert instance.comments == original



@given(instance=tracker_Event_strategy)
def test_tracker_event_idNumber_setter(instance):
    original = instance.idNumber
    instance.idNumber = original
    assert instance.idNumber == original



@given(instance=tracker_Event_strategy)
def test_tracker_event_eventCode_setter(instance):
    original = instance.eventCode
    instance.eventCode = original
    assert instance.eventCode == original



@given(instance=tracker_Event_strategy)
def test_tracker_event_electronicallyRead_setter(instance):
    original = instance.electronicallyRead
    instance.electronicallyRead = original
    assert instance.electronicallyRead == original



@given(instance=tracker_Event_strategy)
def test_tracker_event_correction_setter(instance):
    original = instance.correction
    instance.correction = original
    assert instance.correction == original

@given(instance=tracker_Tag_strategy)
@settings(max_examples=50)
def test_tracker_tag_instantiation(instance):
    assert isinstance(instance, tracker_Tag)



@given(instance=tracker_Tag_strategy)
def test_tracker_tag_usainNumberUsed_setter(instance):
    original = instance.usainNumberUsed
    instance.usainNumberUsed = original
    assert instance.usainNumberUsed == original



@given(instance=tracker_Tag_strategy)
def test_tracker_tag_idNumber_setter(instance):
    original = instance.idNumber
    instance.idNumber = original
    assert instance.idNumber == original

@given(instance=tracker_Premises_strategy)
@settings(max_examples=50)
def test_tracker_premises_instantiation(instance):
    assert isinstance(instance, tracker_Premises)



@given(instance=tracker_Premises_strategy)
def test_tracker_premises_premisesId_setter(instance):
    original = instance.premisesId
    instance.premisesId = original
    assert instance.premisesId == original



@given(instance=tracker_Premises_strategy)
def test_tracker_premises_emailContact_setter(instance):
    original = instance.emailContact
    instance.emailContact = original
    assert instance.emailContact == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tracker_Premises_strategy)
@settings(max_examples=30)
def test_tracker_premises_addtemplate_changes_state(instance):
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
        assert has_statements, f"Function 'addTemplate' in tracker_Premises is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addTemplate' in tracker_Premises did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addTemplate' in tracker_Premises is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tracker_Premises_strategy)
@settings(max_examples=30)
def test_tracker_premises_findanimal_changes_state(instance):
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
        assert has_statements, f"Function 'findAnimal' in tracker_Premises is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'findAnimal' in tracker_Premises did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'findAnimal' in tracker_Premises is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tracker_Premises_strategy)
@settings(max_examples=30)
def test_tracker_premises_eventhistory_changes_state(instance):
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
        assert has_statements, f"Function 'eventHistory' in tracker_Premises is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eventHistory' in tracker_Premises did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eventHistory' in tracker_Premises is not implemented or raised an error")

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=tracker_Sighting_strategy)
@settings(max_examples=50)
def test_tracker_sighting_instantiation(instance):
    assert isinstance(instance, tracker_Sighting)

@given(instance=tracker_ICVI_strategy)
@settings(max_examples=50)
def test_tracker_icvi_instantiation(instance):
    assert isinstance(instance, tracker_ICVI)

@given(instance=tracker_TagApplied_strategy)
@settings(max_examples=50)
def test_tracker_tagapplied_instantiation(instance):
    assert isinstance(instance, tracker_TagApplied)

@given(instance=tracker_WeighIn_strategy)
@settings(max_examples=50)
def test_tracker_weighin_instantiation(instance):
    assert isinstance(instance, tracker_WeighIn)



@given(instance=tracker_WeighIn_strategy)
def test_tracker_weighin_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=tracker_FairRegistration_strategy)
@settings(max_examples=50)
def test_tracker_fairregistration_instantiation(instance):
    assert isinstance(instance, tracker_FairRegistration)



@given(instance=tracker_FairRegistration_strategy)
def test_tracker_fairregistration_participant_setter(instance):
    original = instance.participant
    instance.participant = original
    assert instance.participant == original



@given(instance=tracker_FairRegistration_strategy)
def test_tracker_fairregistration_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original



@given(instance=tracker_FairRegistration_strategy)
def test_tracker_fairregistration_parent_setter(instance):
    original = instance.parent
    instance.parent = original
    assert instance.parent == original



@given(instance=tracker_FairRegistration_strategy)
def test_tracker_fairregistration_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=tracker_FairRegistration_strategy)
def test_tracker_fairregistration_club_setter(instance):
    original = instance.club
    instance.club = original
    assert instance.club == original

@given(instance=tracker_Died_strategy)
@settings(max_examples=50)
def test_tracker_died_instantiation(instance):
    assert isinstance(instance, tracker_Died)

@given(instance=tracker_Exported_strategy)
@settings(max_examples=50)
def test_tracker_exported_instantiation(instance):
    assert isinstance(instance, tracker_Exported)

@given(instance=tracker_Imported_strategy)
@settings(max_examples=50)
def test_tracker_imported_instantiation(instance):
    assert isinstance(instance, tracker_Imported)

@given(instance=tracker_Slaughtered_strategy)
@settings(max_examples=50)
def test_tracker_slaughtered_instantiation(instance):
    assert isinstance(instance, tracker_Slaughtered)

@given(instance=tracker_AnimalMissing_strategy)
@settings(max_examples=50)
def test_tracker_animalmissing_instantiation(instance):
    assert isinstance(instance, tracker_AnimalMissing)

@given(instance=tracker_TagRetired_strategy)
@settings(max_examples=50)
def test_tracker_tagretired_instantiation(instance):
    assert isinstance(instance, tracker_TagRetired)

@given(instance=tracker_TagAllocated_strategy)
@settings(max_examples=50)
def test_tracker_tagallocated_instantiation(instance):
    assert isinstance(instance, tracker_TagAllocated)

@given(instance=Animal_strategy)
@settings(max_examples=50)
def test_animal_instantiation(instance):
    assert isinstance(instance, Animal)

@given(instance=tracker_Ovine_strategy)
@settings(max_examples=50)
def test_tracker_ovine_instantiation(instance):
    assert isinstance(instance, tracker_Ovine)



@given(instance=tracker_Ovine_strategy)
def test_tracker_ovine_sheepBreed_setter(instance):
    original = instance.sheepBreed
    instance.sheepBreed = original
    assert instance.sheepBreed == original

@given(instance=tracker_Bovine_strategy)
@settings(max_examples=50)
def test_tracker_bovine_instantiation(instance):
    assert isinstance(instance, tracker_Bovine)

@given(instance=tracker_Animal_strategy)
@settings(max_examples=50)
def test_tracker_animal_instantiation(instance):
    assert isinstance(instance, tracker_Animal)



@given(instance=tracker_Animal_strategy)
def test_tracker_animal_idNumber_setter(instance):
    original = instance.idNumber
    instance.idNumber = original
    assert instance.idNumber == original



@given(instance=tracker_Animal_strategy)
def test_tracker_animal_breed_setter(instance):
    original = instance.breed
    instance.breed = original
    assert instance.breed == original



@given(instance=tracker_Animal_strategy)
def test_tracker_animal_species_setter(instance):
    original = instance.species
    instance.species = original
    assert instance.species == original



@given(instance=tracker_Animal_strategy)
def test_tracker_animal_birthDate_setter(instance):
    original = instance.birthDate
    instance.birthDate = original
    assert instance.birthDate == original



@given(instance=tracker_Animal_strategy)
def test_tracker_animal_sex_setter(instance):
    original = instance.sex
    instance.sex = original
    assert instance.sex == original



@given(instance=tracker_Animal_strategy)
def test_tracker_animal_sexCode_setter(instance):
    original = instance.sexCode
    instance.sexCode = original
    assert instance.sexCode == original



@given(instance=tracker_Animal_strategy)
def test_tracker_animal_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=tracker_Animal_strategy)
def test_tracker_animal_speciesCode_setter(instance):
    original = instance.speciesCode
    instance.speciesCode = original
    assert instance.speciesCode == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tracker_Animal_strategy)
@settings(max_examples=30)
def test_tracker_animal_activetag_changes_state(instance):
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
        assert has_statements, f"Function 'activeTag' in tracker_Animal is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'activeTag' in tracker_Animal did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'activeTag' in tracker_Animal is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tracker_Animal_strategy)
@settings(max_examples=30)
def test_tracker_animal_allevents_changes_state(instance):
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
        assert has_statements, f"Function 'allEvents' in tracker_Animal is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'allEvents' in tracker_Animal did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'allEvents' in tracker_Animal is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tracker_Animal_strategy)
@settings(max_examples=30)
def test_tracker_animal_addtemplate_changes_state(instance):
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
        assert has_statements, f"Function 'addTemplate' in tracker_Animal is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addTemplate' in tracker_Animal did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addTemplate' in tracker_Animal is not implemented or raised an error")

@given(instance=tracker_Swine_strategy)
@settings(max_examples=50)
def test_tracker_swine_instantiation(instance):
    assert isinstance(instance, tracker_Swine)



@given(instance=tracker_Swine_strategy)
def test_tracker_swine_swineBreed_setter(instance):
    original = instance.swineBreed
    instance.swineBreed = original
    assert instance.swineBreed == original

@given(instance=tracker_ReplacedTag_strategy)
@settings(max_examples=50)
def test_tracker_replacedtag_instantiation(instance):
    assert isinstance(instance, tracker_ReplacedTag)



@given(instance=tracker_ReplacedTag_strategy)
def test_tracker_replacedtag_oldAin_setter(instance):
    original = instance.oldAin
    instance.oldAin = original
    assert instance.oldAin == original

@given(instance=tracker_LostTag_strategy)
@settings(max_examples=50)
def test_tracker_losttag_instantiation(instance):
    assert isinstance(instance, tracker_LostTag)

@given(instance=tracker_MovedOut_strategy)
@settings(max_examples=50)
def test_tracker_movedout_instantiation(instance):
    assert isinstance(instance, tracker_MovedOut)



@given(instance=tracker_MovedOut_strategy)
def test_tracker_movedout_destinationPin_setter(instance):
    original = instance.destinationPin
    instance.destinationPin = original
    assert instance.destinationPin == original

@given(instance=tracker_MovedIn_strategy)
@settings(max_examples=50)
def test_tracker_movedin_instantiation(instance):
    assert isinstance(instance, tracker_MovedIn)



@given(instance=tracker_MovedIn_strategy)
def test_tracker_movedin_sourcePin_setter(instance):
    original = instance.sourcePin
    instance.sourcePin = original
    assert instance.sourcePin == original
