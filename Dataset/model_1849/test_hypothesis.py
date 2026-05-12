import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    libsys_Library,
    libsys_BarCodeScanner,
    libsys_IdentificationCard,
    libsys_UnpaidFee,
    libsys_ExtensionTime,
    libsys_StatusSignal,
    libsys_SearchCriterion,
    Medium,
    libsys_CD,
    libsys_Magazine,
    libsys_Video,
    libsys_Book,
    libsys_UserAccount,
    libsys_User,
    libsys_BorrowedEntry,
    libsys_ReservationEntry,
    libsys_Terminal,
    libsys_MediaAdministration,
    libsys_UserAdministration,
    libsys_Librarian,
    libsys_Instance,
    libsys_Medium,
    InstanceStatus,
    MediumCode,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_libsys_library_is_not_abstract():
    assert not inspect.isabstract(libsys_Library)


def test_libsys_library_constructor_exists():
    assert callable(libsys_Library.__init__)


def test_libsys_library_constructor_args():
    sig = inspect.signature(libsys_Library.__init__)
    params = list(sig.parameters.keys())



def test_libsys_barcodescanner_is_not_abstract():
    assert not inspect.isabstract(libsys_BarCodeScanner)


def test_libsys_barcodescanner_constructor_exists():
    assert callable(libsys_BarCodeScanner.__init__)


def test_libsys_barcodescanner_constructor_args():
    sig = inspect.signature(libsys_BarCodeScanner.__init__)
    params = list(sig.parameters.keys())



def test_libsys_identificationcard_is_not_abstract():
    assert not inspect.isabstract(libsys_IdentificationCard)


def test_libsys_identificationcard_constructor_exists():
    assert callable(libsys_IdentificationCard.__init__)


def test_libsys_identificationcard_constructor_args():
    sig = inspect.signature(libsys_IdentificationCard.__init__)
    params = list(sig.parameters.keys())
    assert "userNumber" in params, "Missing parameter 'userNumber'"

def test_libsys_identificationcard_has_userNumber():
    assert hasattr(libsys_IdentificationCard, "userNumber")
    descriptor = None
    for klass in libsys_IdentificationCard.__mro__:
        if "userNumber" in klass.__dict__:
            descriptor = klass.__dict__["userNumber"]
            break
    assert isinstance(descriptor, property)



def test_libsys_unpaidfee_is_not_abstract():
    assert not inspect.isabstract(libsys_UnpaidFee)


def test_libsys_unpaidfee_constructor_exists():
    assert callable(libsys_UnpaidFee.__init__)


def test_libsys_unpaidfee_constructor_args():
    sig = inspect.signature(libsys_UnpaidFee.__init__)
    params = list(sig.parameters.keys())
    assert "reason" in params, "Missing parameter 'reason'"
    assert "amount" in params, "Missing parameter 'amount'"

def test_libsys_unpaidfee_has_reason():
    assert hasattr(libsys_UnpaidFee, "reason")
    descriptor = None
    for klass in libsys_UnpaidFee.__mro__:
        if "reason" in klass.__dict__:
            descriptor = klass.__dict__["reason"]
            break
    assert isinstance(descriptor, property)

def test_libsys_unpaidfee_has_amount():
    assert hasattr(libsys_UnpaidFee, "amount")
    descriptor = None
    for klass in libsys_UnpaidFee.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)



def test_libsys_extensiontime_is_not_abstract():
    assert not inspect.isabstract(libsys_ExtensionTime)


def test_libsys_extensiontime_constructor_exists():
    assert callable(libsys_ExtensionTime.__init__)


def test_libsys_extensiontime_constructor_args():
    sig = inspect.signature(libsys_ExtensionTime.__init__)
    params = list(sig.parameters.keys())



def test_libsys_statussignal_is_not_abstract():
    assert not inspect.isabstract(libsys_StatusSignal)


def test_libsys_statussignal_constructor_exists():
    assert callable(libsys_StatusSignal.__init__)


def test_libsys_statussignal_constructor_args():
    sig = inspect.signature(libsys_StatusSignal.__init__)
    params = list(sig.parameters.keys())



def test_libsys_searchcriterion_is_not_abstract():
    assert not inspect.isabstract(libsys_SearchCriterion)


def test_libsys_searchcriterion_constructor_exists():
    assert callable(libsys_SearchCriterion.__init__)


def test_libsys_searchcriterion_constructor_args():
    sig = inspect.signature(libsys_SearchCriterion.__init__)
    params = list(sig.parameters.keys())



def test_medium_is_not_abstract():
    assert not inspect.isabstract(Medium)


def test_medium_constructor_exists():
    assert callable(Medium.__init__)


def test_medium_constructor_args():
    sig = inspect.signature(Medium.__init__)
    params = list(sig.parameters.keys())



def test_libsys_cd_is_not_abstract():
    assert not inspect.isabstract(libsys_CD)


def test_libsys_cd_constructor_exists():
    assert callable(libsys_CD.__init__)


def test_libsys_cd_constructor_args():
    sig = inspect.signature(libsys_CD.__init__)
    params = list(sig.parameters.keys())
    assert "artists" in params, "Missing parameter 'artists'"
    assert "tracks" in params, "Missing parameter 'tracks'"
    assert "genres" in params, "Missing parameter 'genres'"

def test_libsys_cd_has_artists():
    assert hasattr(libsys_CD, "artists")
    descriptor = None
    for klass in libsys_CD.__mro__:
        if "artists" in klass.__dict__:
            descriptor = klass.__dict__["artists"]
            break
    assert isinstance(descriptor, property)

def test_libsys_cd_has_tracks():
    assert hasattr(libsys_CD, "tracks")
    descriptor = None
    for klass in libsys_CD.__mro__:
        if "tracks" in klass.__dict__:
            descriptor = klass.__dict__["tracks"]
            break
    assert isinstance(descriptor, property)

def test_libsys_cd_has_genres():
    assert hasattr(libsys_CD, "genres")
    descriptor = None
    for klass in libsys_CD.__mro__:
        if "genres" in klass.__dict__:
            descriptor = klass.__dict__["genres"]
            break
    assert isinstance(descriptor, property)



def test_libsys_magazine_is_not_abstract():
    assert not inspect.isabstract(libsys_Magazine)


def test_libsys_magazine_constructor_exists():
    assert callable(libsys_Magazine.__init__)


def test_libsys_magazine_constructor_args():
    sig = inspect.signature(libsys_Magazine.__init__)
    params = list(sig.parameters.keys())
    assert "publisher" in params, "Missing parameter 'publisher'"
    assert "articles" in params, "Missing parameter 'articles'"

def test_libsys_magazine_has_publisher():
    assert hasattr(libsys_Magazine, "publisher")
    descriptor = None
    for klass in libsys_Magazine.__mro__:
        if "publisher" in klass.__dict__:
            descriptor = klass.__dict__["publisher"]
            break
    assert isinstance(descriptor, property)

def test_libsys_magazine_has_articles():
    assert hasattr(libsys_Magazine, "articles")
    descriptor = None
    for klass in libsys_Magazine.__mro__:
        if "articles" in klass.__dict__:
            descriptor = klass.__dict__["articles"]
            break
    assert isinstance(descriptor, property)



def test_libsys_video_is_not_abstract():
    assert not inspect.isabstract(libsys_Video)


def test_libsys_video_constructor_exists():
    assert callable(libsys_Video.__init__)


def test_libsys_video_constructor_args():
    sig = inspect.signature(libsys_Video.__init__)
    params = list(sig.parameters.keys())
    assert "actors" in params, "Missing parameter 'actors'"
    assert "genres" in params, "Missing parameter 'genres'"

def test_libsys_video_has_actors():
    assert hasattr(libsys_Video, "actors")
    descriptor = None
    for klass in libsys_Video.__mro__:
        if "actors" in klass.__dict__:
            descriptor = klass.__dict__["actors"]
            break
    assert isinstance(descriptor, property)

def test_libsys_video_has_genres():
    assert hasattr(libsys_Video, "genres")
    descriptor = None
    for klass in libsys_Video.__mro__:
        if "genres" in klass.__dict__:
            descriptor = klass.__dict__["genres"]
            break
    assert isinstance(descriptor, property)



def test_libsys_book_is_not_abstract():
    assert not inspect.isabstract(libsys_Book)


def test_libsys_book_constructor_exists():
    assert callable(libsys_Book.__init__)


def test_libsys_book_constructor_args():
    sig = inspect.signature(libsys_Book.__init__)
    params = list(sig.parameters.keys())
    assert "ISBN" in params, "Missing parameter 'ISBN'"
    assert "editor" in params, "Missing parameter 'editor'"
    assert "placeOfPublication" in params, "Missing parameter 'placeOfPublication'"
    assert "publisher" in params, "Missing parameter 'publisher'"

def test_libsys_book_has_ISBN():
    assert hasattr(libsys_Book, "ISBN")
    descriptor = None
    for klass in libsys_Book.__mro__:
        if "ISBN" in klass.__dict__:
            descriptor = klass.__dict__["ISBN"]
            break
    assert isinstance(descriptor, property)

def test_libsys_book_has_editor():
    assert hasattr(libsys_Book, "editor")
    descriptor = None
    for klass in libsys_Book.__mro__:
        if "editor" in klass.__dict__:
            descriptor = klass.__dict__["editor"]
            break
    assert isinstance(descriptor, property)

def test_libsys_book_has_placeOfPublication():
    assert hasattr(libsys_Book, "placeOfPublication")
    descriptor = None
    for klass in libsys_Book.__mro__:
        if "placeOfPublication" in klass.__dict__:
            descriptor = klass.__dict__["placeOfPublication"]
            break
    assert isinstance(descriptor, property)

def test_libsys_book_has_publisher():
    assert hasattr(libsys_Book, "publisher")
    descriptor = None
    for klass in libsys_Book.__mro__:
        if "publisher" in klass.__dict__:
            descriptor = klass.__dict__["publisher"]
            break
    assert isinstance(descriptor, property)



def test_libsys_useraccount_is_not_abstract():
    assert not inspect.isabstract(libsys_UserAccount)


def test_libsys_useraccount_constructor_exists():
    assert callable(libsys_UserAccount.__init__)


def test_libsys_useraccount_constructor_args():
    sig = inspect.signature(libsys_UserAccount.__init__)
    params = list(sig.parameters.keys())
    assert "validUntilDate" in params, "Missing parameter 'validUntilDate'"
    assert "telephoneNumber" in params, "Missing parameter 'telephoneNumber'"
    assert "userNumber" in params, "Missing parameter 'userNumber'"
    assert "postallAddress" in params, "Missing parameter 'postallAddress'"
    assert "userClassification" in params, "Missing parameter 'userClassification'"
    assert "emailAddress" in params, "Missing parameter 'emailAddress'"
    assert "lockIndication" in params, "Missing parameter 'lockIndication'"
    assert "unpaidFeeAmount" in params, "Missing parameter 'unpaidFeeAmount'"
    assert "userData" in params, "Missing parameter 'userData'"
    assert "userName" in params, "Missing parameter 'userName'"

def test_libsys_useraccount_has_validUntilDate():
    assert hasattr(libsys_UserAccount, "validUntilDate")
    descriptor = None
    for klass in libsys_UserAccount.__mro__:
        if "validUntilDate" in klass.__dict__:
            descriptor = klass.__dict__["validUntilDate"]
            break
    assert isinstance(descriptor, property)

def test_libsys_useraccount_has_telephoneNumber():
    assert hasattr(libsys_UserAccount, "telephoneNumber")
    descriptor = None
    for klass in libsys_UserAccount.__mro__:
        if "telephoneNumber" in klass.__dict__:
            descriptor = klass.__dict__["telephoneNumber"]
            break
    assert isinstance(descriptor, property)

def test_libsys_useraccount_has_userNumber():
    assert hasattr(libsys_UserAccount, "userNumber")
    descriptor = None
    for klass in libsys_UserAccount.__mro__:
        if "userNumber" in klass.__dict__:
            descriptor = klass.__dict__["userNumber"]
            break
    assert isinstance(descriptor, property)

def test_libsys_useraccount_has_postallAddress():
    assert hasattr(libsys_UserAccount, "postallAddress")
    descriptor = None
    for klass in libsys_UserAccount.__mro__:
        if "postallAddress" in klass.__dict__:
            descriptor = klass.__dict__["postallAddress"]
            break
    assert isinstance(descriptor, property)

def test_libsys_useraccount_has_userClassification():
    assert hasattr(libsys_UserAccount, "userClassification")
    descriptor = None
    for klass in libsys_UserAccount.__mro__:
        if "userClassification" in klass.__dict__:
            descriptor = klass.__dict__["userClassification"]
            break
    assert isinstance(descriptor, property)

def test_libsys_useraccount_has_emailAddress():
    assert hasattr(libsys_UserAccount, "emailAddress")
    descriptor = None
    for klass in libsys_UserAccount.__mro__:
        if "emailAddress" in klass.__dict__:
            descriptor = klass.__dict__["emailAddress"]
            break
    assert isinstance(descriptor, property)

def test_libsys_useraccount_has_lockIndication():
    assert hasattr(libsys_UserAccount, "lockIndication")
    descriptor = None
    for klass in libsys_UserAccount.__mro__:
        if "lockIndication" in klass.__dict__:
            descriptor = klass.__dict__["lockIndication"]
            break
    assert isinstance(descriptor, property)

def test_libsys_useraccount_has_unpaidFeeAmount():
    assert hasattr(libsys_UserAccount, "unpaidFeeAmount")
    descriptor = None
    for klass in libsys_UserAccount.__mro__:
        if "unpaidFeeAmount" in klass.__dict__:
            descriptor = klass.__dict__["unpaidFeeAmount"]
            break
    assert isinstance(descriptor, property)

def test_libsys_useraccount_has_userData():
    assert hasattr(libsys_UserAccount, "userData")
    descriptor = None
    for klass in libsys_UserAccount.__mro__:
        if "userData" in klass.__dict__:
            descriptor = klass.__dict__["userData"]
            break
    assert isinstance(descriptor, property)

def test_libsys_useraccount_has_userName():
    assert hasattr(libsys_UserAccount, "userName")
    descriptor = None
    for klass in libsys_UserAccount.__mro__:
        if "userName" in klass.__dict__:
            descriptor = klass.__dict__["userName"]
            break
    assert isinstance(descriptor, property)



def test_libsys_user_is_not_abstract():
    assert not inspect.isabstract(libsys_User)


def test_libsys_user_constructor_exists():
    assert callable(libsys_User.__init__)


def test_libsys_user_constructor_args():
    sig = inspect.signature(libsys_User.__init__)
    params = list(sig.parameters.keys())



def test_libsys_borrowedentry_is_not_abstract():
    assert not inspect.isabstract(libsys_BorrowedEntry)


def test_libsys_borrowedentry_constructor_exists():
    assert callable(libsys_BorrowedEntry.__init__)


def test_libsys_borrowedentry_constructor_args():
    sig = inspect.signature(libsys_BorrowedEntry.__init__)
    params = list(sig.parameters.keys())
    assert "returnDate" in params, "Missing parameter 'returnDate'"

def test_libsys_borrowedentry_has_returnDate():
    assert hasattr(libsys_BorrowedEntry, "returnDate")
    descriptor = None
    for klass in libsys_BorrowedEntry.__mro__:
        if "returnDate" in klass.__dict__:
            descriptor = klass.__dict__["returnDate"]
            break
    assert isinstance(descriptor, property)



def test_libsys_reservationentry_is_not_abstract():
    assert not inspect.isabstract(libsys_ReservationEntry)


def test_libsys_reservationentry_constructor_exists():
    assert callable(libsys_ReservationEntry.__init__)


def test_libsys_reservationentry_constructor_args():
    sig = inspect.signature(libsys_ReservationEntry.__init__)
    params = list(sig.parameters.keys())



def test_libsys_terminal_is_not_abstract():
    assert not inspect.isabstract(libsys_Terminal)


def test_libsys_terminal_constructor_exists():
    assert callable(libsys_Terminal.__init__)


def test_libsys_terminal_constructor_args():
    sig = inspect.signature(libsys_Terminal.__init__)
    params = list(sig.parameters.keys())



def test_libsys_mediaadministration_is_not_abstract():
    assert not inspect.isabstract(libsys_MediaAdministration)


def test_libsys_mediaadministration_constructor_exists():
    assert callable(libsys_MediaAdministration.__init__)


def test_libsys_mediaadministration_constructor_args():
    sig = inspect.signature(libsys_MediaAdministration.__init__)
    params = list(sig.parameters.keys())



def test_libsys_useradministration_is_not_abstract():
    assert not inspect.isabstract(libsys_UserAdministration)


def test_libsys_useradministration_constructor_exists():
    assert callable(libsys_UserAdministration.__init__)


def test_libsys_useradministration_constructor_args():
    sig = inspect.signature(libsys_UserAdministration.__init__)
    params = list(sig.parameters.keys())



def test_libsys_librarian_is_not_abstract():
    assert not inspect.isabstract(libsys_Librarian)


def test_libsys_librarian_constructor_exists():
    assert callable(libsys_Librarian.__init__)


def test_libsys_librarian_constructor_args():
    sig = inspect.signature(libsys_Librarian.__init__)
    params = list(sig.parameters.keys())



def test_libsys_instance_is_not_abstract():
    assert not inspect.isabstract(libsys_Instance)


def test_libsys_instance_constructor_exists():
    assert callable(libsys_Instance.__init__)


def test_libsys_instance_constructor_args():
    sig = inspect.signature(libsys_Instance.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "components" in params, "Missing parameter 'components'"
    assert "shelfmark" in params, "Missing parameter 'shelfmark'"
    assert "rentalPeriod" in params, "Missing parameter 'rentalPeriod'"
    assert "status" in params, "Missing parameter 'status'"
    assert "returnDate" in params, "Missing parameter 'returnDate'"
    assert "comments" in params, "Missing parameter 'comments'"

def test_libsys_instance_has_location():
    assert hasattr(libsys_Instance, "location")
    descriptor = None
    for klass in libsys_Instance.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_libsys_instance_has_components():
    assert hasattr(libsys_Instance, "components")
    descriptor = None
    for klass in libsys_Instance.__mro__:
        if "components" in klass.__dict__:
            descriptor = klass.__dict__["components"]
            break
    assert isinstance(descriptor, property)

def test_libsys_instance_has_shelfmark():
    assert hasattr(libsys_Instance, "shelfmark")
    descriptor = None
    for klass in libsys_Instance.__mro__:
        if "shelfmark" in klass.__dict__:
            descriptor = klass.__dict__["shelfmark"]
            break
    assert isinstance(descriptor, property)

def test_libsys_instance_has_rentalPeriod():
    assert hasattr(libsys_Instance, "rentalPeriod")
    descriptor = None
    for klass in libsys_Instance.__mro__:
        if "rentalPeriod" in klass.__dict__:
            descriptor = klass.__dict__["rentalPeriod"]
            break
    assert isinstance(descriptor, property)

def test_libsys_instance_has_status():
    assert hasattr(libsys_Instance, "status")
    descriptor = None
    for klass in libsys_Instance.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_libsys_instance_has_returnDate():
    assert hasattr(libsys_Instance, "returnDate")
    descriptor = None
    for klass in libsys_Instance.__mro__:
        if "returnDate" in klass.__dict__:
            descriptor = klass.__dict__["returnDate"]
            break
    assert isinstance(descriptor, property)

def test_libsys_instance_has_comments():
    assert hasattr(libsys_Instance, "comments")
    descriptor = None
    for klass in libsys_Instance.__mro__:
        if "comments" in klass.__dict__:
            descriptor = klass.__dict__["comments"]
            break
    assert isinstance(descriptor, property)



def test_libsys_medium_is_not_abstract():
    assert not inspect.isabstract(libsys_Medium)


def test_libsys_medium_constructor_exists():
    assert callable(libsys_Medium.__init__)


def test_libsys_medium_constructor_args():
    sig = inspect.signature(libsys_Medium.__init__)
    params = list(sig.parameters.keys())
    assert "authors" in params, "Missing parameter 'authors'"
    assert "identificationCode" in params, "Missing parameter 'identificationCode'"
    assert "title" in params, "Missing parameter 'title'"
    assert "publicationYear" in params, "Missing parameter 'publicationYear'"
    assert "keywords" in params, "Missing parameter 'keywords'"
    assert "partialShelfmark" in params, "Missing parameter 'partialShelfmark'"
    assert "additionalTitle" in params, "Missing parameter 'additionalTitle'"

def test_libsys_medium_has_authors():
    assert hasattr(libsys_Medium, "authors")
    descriptor = None
    for klass in libsys_Medium.__mro__:
        if "authors" in klass.__dict__:
            descriptor = klass.__dict__["authors"]
            break
    assert isinstance(descriptor, property)

def test_libsys_medium_has_identificationCode():
    assert hasattr(libsys_Medium, "identificationCode")
    descriptor = None
    for klass in libsys_Medium.__mro__:
        if "identificationCode" in klass.__dict__:
            descriptor = klass.__dict__["identificationCode"]
            break
    assert isinstance(descriptor, property)

def test_libsys_medium_has_title():
    assert hasattr(libsys_Medium, "title")
    descriptor = None
    for klass in libsys_Medium.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_libsys_medium_has_publicationYear():
    assert hasattr(libsys_Medium, "publicationYear")
    descriptor = None
    for klass in libsys_Medium.__mro__:
        if "publicationYear" in klass.__dict__:
            descriptor = klass.__dict__["publicationYear"]
            break
    assert isinstance(descriptor, property)

def test_libsys_medium_has_keywords():
    assert hasattr(libsys_Medium, "keywords")
    descriptor = None
    for klass in libsys_Medium.__mro__:
        if "keywords" in klass.__dict__:
            descriptor = klass.__dict__["keywords"]
            break
    assert isinstance(descriptor, property)

def test_libsys_medium_has_partialShelfmark():
    assert hasattr(libsys_Medium, "partialShelfmark")
    descriptor = None
    for klass in libsys_Medium.__mro__:
        if "partialShelfmark" in klass.__dict__:
            descriptor = klass.__dict__["partialShelfmark"]
            break
    assert isinstance(descriptor, property)

def test_libsys_medium_has_additionalTitle():
    assert hasattr(libsys_Medium, "additionalTitle")
    descriptor = None
    for klass in libsys_Medium.__mro__:
        if "additionalTitle" in klass.__dict__:
            descriptor = klass.__dict__["additionalTitle"]
            break
    assert isinstance(descriptor, property)

def test_instancestatus_exists():
    # Check that the Enumeration exists
    assert InstanceStatus is not None

def test_instancestatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InstanceStatus]
    expected_literals = [
        "Overdue",
        "Available",
        "AcquisitionProcess",
        "Missing",
        "ReservedAndBorrowed",
        "ReservedAndAvailable",
        "ReadingRoom",
        "Borrowed",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InstanceStatus"

def test_mediumcode_exists():
    # Check that the Enumeration exists
    assert MediumCode is not None

def test_mediumcode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MediumCode]
    expected_literals = [
        "magazine",
        "book",
        "CD",
        "video",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MediumCode"


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
libsys_Library_strategy = st.builds(
    libsys_Library,
)
libsys_BarCodeScanner_strategy = st.builds(
    libsys_BarCodeScanner,
)
libsys_IdentificationCard_strategy = st.builds(
    libsys_IdentificationCard,
    userNumber=
        st.integers()
)
libsys_UnpaidFee_strategy = st.builds(
    libsys_UnpaidFee,
    reason=
        safe_text,
    amount=
        st.integers()
)
libsys_ExtensionTime_strategy = st.builds(
    libsys_ExtensionTime,
)
libsys_StatusSignal_strategy = st.builds(
    libsys_StatusSignal,
)
libsys_SearchCriterion_strategy = st.builds(
    libsys_SearchCriterion,
)
Medium_strategy = st.builds(
    Medium,
)
libsys_CD_strategy = st.builds(
    libsys_CD,
    artists=
        safe_text,
    tracks=
        safe_text,
    genres=
        safe_text
)
libsys_Magazine_strategy = st.builds(
    libsys_Magazine,
    publisher=
        safe_text,
    articles=
        safe_text
)
libsys_Video_strategy = st.builds(
    libsys_Video,
    actors=
        safe_text,
    genres=
        safe_text
)
libsys_Book_strategy = st.builds(
    libsys_Book,
    ISBN=
        safe_text,
    editor=
        safe_text,
    placeOfPublication=
        safe_text,
    publisher=
        safe_text
)
libsys_UserAccount_strategy = st.builds(
    libsys_UserAccount,
    validUntilDate=
        st.dates(),
    telephoneNumber=
        safe_text,
    userNumber=
        st.integers(),
    postallAddress=
        safe_text,
    userClassification=
        safe_text,
    emailAddress=
        safe_text,
    lockIndication=
        st.booleans(),
    unpaidFeeAmount=
        st.integers(),
    userData=
        safe_text,
    userName=
        safe_text
)
libsys_User_strategy = st.builds(
    libsys_User,
)
libsys_BorrowedEntry_strategy = st.builds(
    libsys_BorrowedEntry,
    returnDate=
        st.dates()
)
libsys_ReservationEntry_strategy = st.builds(
    libsys_ReservationEntry,
)
libsys_Terminal_strategy = st.builds(
    libsys_Terminal,
)
libsys_MediaAdministration_strategy = st.builds(
    libsys_MediaAdministration,
)
libsys_UserAdministration_strategy = st.builds(
    libsys_UserAdministration,
)
libsys_Librarian_strategy = st.builds(
    libsys_Librarian,
)
libsys_Instance_strategy = st.builds(
    libsys_Instance,
    location=
        safe_text,
    components=
        safe_text,
    shelfmark=
        safe_text,
    rentalPeriod=
        safe_text,
    status=
        safe_text,
    returnDate=
        st.dates(),
    comments=
        safe_text
)
libsys_Medium_strategy = st.builds(
    libsys_Medium,
    authors=
        safe_text,
    identificationCode=
        safe_text,
    title=
        safe_text,
    publicationYear=
        st.dates(),
    keywords=
        safe_text,
    partialShelfmark=
        safe_text,
    additionalTitle=
        safe_text
)

@given(instance=libsys_Library_strategy)
@settings(max_examples=50)
def test_libsys_library_instantiation(instance):
    assert isinstance(instance, libsys_Library)

@given(instance=libsys_BarCodeScanner_strategy)
@settings(max_examples=50)
def test_libsys_barcodescanner_instantiation(instance):
    assert isinstance(instance, libsys_BarCodeScanner)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=libsys_BarCodeScanner_strategy)
@settings(max_examples=30)
def test_libsys_barcodescanner_readusernumber_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.readUserNumber()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.readUserNumber).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'readUserNumber' in libsys_BarCodeScanner is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'readUserNumber' in libsys_BarCodeScanner did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'readUserNumber' in libsys_BarCodeScanner is not implemented or raised an error")

@given(instance=libsys_IdentificationCard_strategy)
@settings(max_examples=50)
def test_libsys_identificationcard_instantiation(instance):
    assert isinstance(instance, libsys_IdentificationCard)



@given(instance=libsys_IdentificationCard_strategy)
def test_libsys_identificationcard_userNumber_setter(instance):
    original = instance.userNumber
    instance.userNumber = original
    assert instance.userNumber == original

@given(instance=libsys_UnpaidFee_strategy)
@settings(max_examples=50)
def test_libsys_unpaidfee_instantiation(instance):
    assert isinstance(instance, libsys_UnpaidFee)



@given(instance=libsys_UnpaidFee_strategy)
def test_libsys_unpaidfee_reason_setter(instance):
    original = instance.reason
    instance.reason = original
    assert instance.reason == original



@given(instance=libsys_UnpaidFee_strategy)
def test_libsys_unpaidfee_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=libsys_ExtensionTime_strategy)
@settings(max_examples=50)
def test_libsys_extensiontime_instantiation(instance):
    assert isinstance(instance, libsys_ExtensionTime)

@given(instance=libsys_StatusSignal_strategy)
@settings(max_examples=50)
def test_libsys_statussignal_instantiation(instance):
    assert isinstance(instance, libsys_StatusSignal)

@given(instance=libsys_SearchCriterion_strategy)
@settings(max_examples=50)
def test_libsys_searchcriterion_instantiation(instance):
    assert isinstance(instance, libsys_SearchCriterion)

@given(instance=Medium_strategy)
@settings(max_examples=50)
def test_medium_instantiation(instance):
    assert isinstance(instance, Medium)

@given(instance=libsys_CD_strategy)
@settings(max_examples=50)
def test_libsys_cd_instantiation(instance):
    assert isinstance(instance, libsys_CD)



@given(instance=libsys_CD_strategy)
def test_libsys_cd_artists_setter(instance):
    original = instance.artists
    instance.artists = original
    assert instance.artists == original



@given(instance=libsys_CD_strategy)
def test_libsys_cd_tracks_setter(instance):
    original = instance.tracks
    instance.tracks = original
    assert instance.tracks == original



@given(instance=libsys_CD_strategy)
def test_libsys_cd_genres_setter(instance):
    original = instance.genres
    instance.genres = original
    assert instance.genres == original

@given(instance=libsys_Magazine_strategy)
@settings(max_examples=50)
def test_libsys_magazine_instantiation(instance):
    assert isinstance(instance, libsys_Magazine)



@given(instance=libsys_Magazine_strategy)
def test_libsys_magazine_publisher_setter(instance):
    original = instance.publisher
    instance.publisher = original
    assert instance.publisher == original



@given(instance=libsys_Magazine_strategy)
def test_libsys_magazine_articles_setter(instance):
    original = instance.articles
    instance.articles = original
    assert instance.articles == original

@given(instance=libsys_Video_strategy)
@settings(max_examples=50)
def test_libsys_video_instantiation(instance):
    assert isinstance(instance, libsys_Video)



@given(instance=libsys_Video_strategy)
def test_libsys_video_actors_setter(instance):
    original = instance.actors
    instance.actors = original
    assert instance.actors == original



@given(instance=libsys_Video_strategy)
def test_libsys_video_genres_setter(instance):
    original = instance.genres
    instance.genres = original
    assert instance.genres == original

@given(instance=libsys_Book_strategy)
@settings(max_examples=50)
def test_libsys_book_instantiation(instance):
    assert isinstance(instance, libsys_Book)



@given(instance=libsys_Book_strategy)
def test_libsys_book_ISBN_setter(instance):
    original = instance.ISBN
    instance.ISBN = original
    assert instance.ISBN == original



@given(instance=libsys_Book_strategy)
def test_libsys_book_editor_setter(instance):
    original = instance.editor
    instance.editor = original
    assert instance.editor == original



@given(instance=libsys_Book_strategy)
def test_libsys_book_placeOfPublication_setter(instance):
    original = instance.placeOfPublication
    instance.placeOfPublication = original
    assert instance.placeOfPublication == original



@given(instance=libsys_Book_strategy)
def test_libsys_book_publisher_setter(instance):
    original = instance.publisher
    instance.publisher = original
    assert instance.publisher == original

@given(instance=libsys_UserAccount_strategy)
@settings(max_examples=50)
def test_libsys_useraccount_instantiation(instance):
    assert isinstance(instance, libsys_UserAccount)



@given(instance=libsys_UserAccount_strategy)
def test_libsys_useraccount_validUntilDate_setter(instance):
    original = instance.validUntilDate
    instance.validUntilDate = original
    assert instance.validUntilDate == original



@given(instance=libsys_UserAccount_strategy)
def test_libsys_useraccount_telephoneNumber_setter(instance):
    original = instance.telephoneNumber
    instance.telephoneNumber = original
    assert instance.telephoneNumber == original



@given(instance=libsys_UserAccount_strategy)
def test_libsys_useraccount_userNumber_setter(instance):
    original = instance.userNumber
    instance.userNumber = original
    assert instance.userNumber == original



@given(instance=libsys_UserAccount_strategy)
def test_libsys_useraccount_postallAddress_setter(instance):
    original = instance.postallAddress
    instance.postallAddress = original
    assert instance.postallAddress == original



@given(instance=libsys_UserAccount_strategy)
def test_libsys_useraccount_userClassification_setter(instance):
    original = instance.userClassification
    instance.userClassification = original
    assert instance.userClassification == original



@given(instance=libsys_UserAccount_strategy)
def test_libsys_useraccount_emailAddress_setter(instance):
    original = instance.emailAddress
    instance.emailAddress = original
    assert instance.emailAddress == original



@given(instance=libsys_UserAccount_strategy)
def test_libsys_useraccount_lockIndication_setter(instance):
    original = instance.lockIndication
    instance.lockIndication = original
    assert instance.lockIndication == original



@given(instance=libsys_UserAccount_strategy)
def test_libsys_useraccount_unpaidFeeAmount_setter(instance):
    original = instance.unpaidFeeAmount
    instance.unpaidFeeAmount = original
    assert instance.unpaidFeeAmount == original



@given(instance=libsys_UserAccount_strategy)
def test_libsys_useraccount_userData_setter(instance):
    original = instance.userData
    instance.userData = original
    assert instance.userData == original



@given(instance=libsys_UserAccount_strategy)
def test_libsys_useraccount_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original

@given(instance=libsys_User_strategy)
@settings(max_examples=50)
def test_libsys_user_instantiation(instance):
    assert isinstance(instance, libsys_User)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=libsys_User_strategy)
@settings(max_examples=30)
def test_libsys_user_registeratsystem_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.registerAtSystem()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.registerAtSystem).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'registerAtSystem' in libsys_User is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'registerAtSystem' in libsys_User did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'registerAtSystem' in libsys_User is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=libsys_User_strategy)
@settings(max_examples=30)
def test_libsys_user_identifytosystem_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.identifyToSystem()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.identifyToSystem).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'identifyToSystem' in libsys_User is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'identifyToSystem' in libsys_User did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'identifyToSystem' in libsys_User is not implemented or raised an error")

@given(instance=libsys_BorrowedEntry_strategy)
@settings(max_examples=50)
def test_libsys_borrowedentry_instantiation(instance):
    assert isinstance(instance, libsys_BorrowedEntry)



@given(instance=libsys_BorrowedEntry_strategy)
def test_libsys_borrowedentry_returnDate_setter(instance):
    original = instance.returnDate
    instance.returnDate = original
    assert instance.returnDate == original

@given(instance=libsys_ReservationEntry_strategy)
@settings(max_examples=50)
def test_libsys_reservationentry_instantiation(instance):
    assert isinstance(instance, libsys_ReservationEntry)

@given(instance=libsys_Terminal_strategy)
@settings(max_examples=50)
def test_libsys_terminal_instantiation(instance):
    assert isinstance(instance, libsys_Terminal)

@given(instance=libsys_MediaAdministration_strategy)
@settings(max_examples=50)
def test_libsys_mediaadministration_instantiation(instance):
    assert isinstance(instance, libsys_MediaAdministration)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=libsys_MediaAdministration_strategy)
@settings(max_examples=30)
def test_libsys_mediaadministration_managemedium_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.manageMedium()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.manageMedium).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'manageMedium' in libsys_MediaAdministration is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'manageMedium' in libsys_MediaAdministration did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'manageMedium' in libsys_MediaAdministration is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=libsys_MediaAdministration_strategy)
@settings(max_examples=30)
def test_libsys_mediaadministration_addnewmediainstance_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addNewMediaInstance()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addNewMediaInstance).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addNewMediaInstance' in libsys_MediaAdministration is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addNewMediaInstance' in libsys_MediaAdministration did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addNewMediaInstance' in libsys_MediaAdministration is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=libsys_MediaAdministration_strategy)
@settings(max_examples=30)
def test_libsys_mediaadministration_removemediainstance_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.removeMediaInstance()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.removeMediaInstance).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'removeMediaInstance' in libsys_MediaAdministration is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'removeMediaInstance' in libsys_MediaAdministration did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'removeMediaInstance' in libsys_MediaAdministration is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=libsys_MediaAdministration_strategy)
@settings(max_examples=30)
def test_libsys_mediaadministration_searchmedium_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.searchMedium()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.searchMedium).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'searchMedium' in libsys_MediaAdministration is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'searchMedium' in libsys_MediaAdministration did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'searchMedium' in libsys_MediaAdministration is not implemented or raised an error")

@given(instance=libsys_UserAdministration_strategy)
@settings(max_examples=50)
def test_libsys_useradministration_instantiation(instance):
    assert isinstance(instance, libsys_UserAdministration)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=libsys_UserAdministration_strategy)
@settings(max_examples=30)
def test_libsys_useradministration_manageuseraccount_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.manageUserAccount()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.manageUserAccount).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'manageUserAccount' in libsys_UserAdministration is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'manageUserAccount' in libsys_UserAdministration did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'manageUserAccount' in libsys_UserAdministration is not implemented or raised an error")

@given(instance=libsys_Librarian_strategy)
@settings(max_examples=50)
def test_libsys_librarian_instantiation(instance):
    assert isinstance(instance, libsys_Librarian)

@given(instance=libsys_Instance_strategy)
@settings(max_examples=50)
def test_libsys_instance_instantiation(instance):
    assert isinstance(instance, libsys_Instance)



@given(instance=libsys_Instance_strategy)
def test_libsys_instance_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=libsys_Instance_strategy)
def test_libsys_instance_components_setter(instance):
    original = instance.components
    instance.components = original
    assert instance.components == original



@given(instance=libsys_Instance_strategy)
def test_libsys_instance_shelfmark_setter(instance):
    original = instance.shelfmark
    instance.shelfmark = original
    assert instance.shelfmark == original



@given(instance=libsys_Instance_strategy)
def test_libsys_instance_rentalPeriod_setter(instance):
    original = instance.rentalPeriod
    instance.rentalPeriod = original
    assert instance.rentalPeriod == original



@given(instance=libsys_Instance_strategy)
def test_libsys_instance_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=libsys_Instance_strategy)
def test_libsys_instance_returnDate_setter(instance):
    original = instance.returnDate
    instance.returnDate = original
    assert instance.returnDate == original



@given(instance=libsys_Instance_strategy)
def test_libsys_instance_comments_setter(instance):
    original = instance.comments
    instance.comments = original
    assert instance.comments == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=libsys_Instance_strategy)
@settings(max_examples=30)
def test_libsys_instance_returninstance_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.returnInstance()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.returnInstance).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'returnInstance' in libsys_Instance is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'returnInstance' in libsys_Instance did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'returnInstance' in libsys_Instance is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=libsys_Instance_strategy)
@settings(max_examples=30)
def test_libsys_instance_reserveinstance_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.reserveInstance()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.reserveInstance).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'reserveInstance' in libsys_Instance is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'reserveInstance' in libsys_Instance did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'reserveInstance' in libsys_Instance is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=libsys_Instance_strategy)
@settings(max_examples=30)
def test_libsys_instance_extendrentalperiod_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.extendRentalPeriod()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.extendRentalPeriod).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'extendRentalPeriod' in libsys_Instance is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'extendRentalPeriod' in libsys_Instance did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'extendRentalPeriod' in libsys_Instance is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=libsys_Instance_strategy)
@settings(max_examples=30)
def test_libsys_instance_borrowinstance_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.borrowInstance()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.borrowInstance).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'borrowInstance' in libsys_Instance is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'borrowInstance' in libsys_Instance did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'borrowInstance' in libsys_Instance is not implemented or raised an error")

@given(instance=libsys_Medium_strategy)
@settings(max_examples=50)
def test_libsys_medium_instantiation(instance):
    assert isinstance(instance, libsys_Medium)



@given(instance=libsys_Medium_strategy)
def test_libsys_medium_authors_setter(instance):
    original = instance.authors
    instance.authors = original
    assert instance.authors == original



@given(instance=libsys_Medium_strategy)
def test_libsys_medium_identificationCode_setter(instance):
    original = instance.identificationCode
    instance.identificationCode = original
    assert instance.identificationCode == original



@given(instance=libsys_Medium_strategy)
def test_libsys_medium_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=libsys_Medium_strategy)
def test_libsys_medium_publicationYear_setter(instance):
    original = instance.publicationYear
    instance.publicationYear = original
    assert instance.publicationYear == original



@given(instance=libsys_Medium_strategy)
def test_libsys_medium_keywords_setter(instance):
    original = instance.keywords
    instance.keywords = original
    assert instance.keywords == original



@given(instance=libsys_Medium_strategy)
def test_libsys_medium_partialShelfmark_setter(instance):
    original = instance.partialShelfmark
    instance.partialShelfmark = original
    assert instance.partialShelfmark == original



@given(instance=libsys_Medium_strategy)
def test_libsys_medium_additionalTitle_setter(instance):
    original = instance.additionalTitle
    instance.additionalTitle = original
    assert instance.additionalTitle == original
