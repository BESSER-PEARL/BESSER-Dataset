import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Serializable,
    pokerleague::DataVersion,
    pokerleague::DataStructureVersion,
    pokerleague::Serializable,
    DescribedEntity,
    pokerleague::Competition,
    pokerleague::Tournament,
    pokerleague::PrizeMoneyRuleSet,
    IdentifiableEntity,
    pokerleague::Player,
    pokerleague::Game,
    pokerleague::PrizeMoneyFormula,
    pokerleague::Invitation,
    pokerleague::PrizeMoneyRule,
    pokerleague::PlayerInGame,
    pokerleague::InvitationEvent,
    pokerleague::DescribedEntity,
    pokerleague::IdentifiableEntity,
    pokerleague::Settings,
    InvitationReply,
    InvitationEventType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_serializable_is_not_abstract():
    assert not inspect.isabstract(Serializable)


def test_serializable_constructor_exists():
    assert callable(Serializable.__init__)


def test_serializable_constructor_args():
    sig = inspect.signature(Serializable.__init__)
    params = list(sig.parameters.keys())



def test_pokerleague::dataversion_is_not_abstract():
    assert not inspect.isabstract(pokerleague::DataVersion)


def test_pokerleague::dataversion_constructor_exists():
    assert callable(pokerleague::DataVersion.__init__)


def test_pokerleague::dataversion_constructor_args():
    sig = inspect.signature(pokerleague::DataVersion.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "currentVersion" in params, "Missing parameter 'currentVersion'"

def test_pokerleague::dataversion_has_id():
    assert hasattr(pokerleague::DataVersion, "id")
    descriptor = None
    for klass in pokerleague::DataVersion.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague::dataversion_has_currentVersion():
    assert hasattr(pokerleague::DataVersion, "currentVersion")
    descriptor = None
    for klass in pokerleague::DataVersion.__mro__:
        if "currentVersion" in klass.__dict__:
            descriptor = klass.__dict__["currentVersion"]
            break
    assert isinstance(descriptor, property)



def test_pokerleague::datastructureversion_is_not_abstract():
    assert not inspect.isabstract(pokerleague::DataStructureVersion)


def test_pokerleague::datastructureversion_constructor_exists():
    assert callable(pokerleague::DataStructureVersion.__init__)


def test_pokerleague::datastructureversion_constructor_args():
    sig = inspect.signature(pokerleague::DataStructureVersion.__init__)
    params = list(sig.parameters.keys())
    assert "currentVersion" in params, "Missing parameter 'currentVersion'"
    assert "id" in params, "Missing parameter 'id'"

def test_pokerleague::datastructureversion_has_currentVersion():
    assert hasattr(pokerleague::DataStructureVersion, "currentVersion")
    descriptor = None
    for klass in pokerleague::DataStructureVersion.__mro__:
        if "currentVersion" in klass.__dict__:
            descriptor = klass.__dict__["currentVersion"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague::datastructureversion_has_id():
    assert hasattr(pokerleague::DataStructureVersion, "id")
    descriptor = None
    for klass in pokerleague::DataStructureVersion.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_pokerleague::serializable_is_not_abstract():
    assert not inspect.isabstract(pokerleague::Serializable)


def test_pokerleague::serializable_constructor_exists():
    assert callable(pokerleague::Serializable.__init__)


def test_pokerleague::serializable_constructor_args():
    sig = inspect.signature(pokerleague::Serializable.__init__)
    params = list(sig.parameters.keys())



def test_describedentity_is_not_abstract():
    assert not inspect.isabstract(DescribedEntity)


def test_describedentity_constructor_exists():
    assert callable(DescribedEntity.__init__)


def test_describedentity_constructor_args():
    sig = inspect.signature(DescribedEntity.__init__)
    params = list(sig.parameters.keys())



def test_pokerleague::competition_is_not_abstract():
    assert not inspect.isabstract(pokerleague::Competition)


def test_pokerleague::competition_constructor_exists():
    assert callable(pokerleague::Competition.__init__)


def test_pokerleague::competition_constructor_args():
    sig = inspect.signature(pokerleague::Competition.__init__)
    params = list(sig.parameters.keys())
    assert "defaultBuyIn" in params, "Missing parameter 'defaultBuyIn'"
    assert "endDate" in params, "Missing parameter 'endDate'"
    assert "defaultMinPlayers" in params, "Missing parameter 'defaultMinPlayers'"
    assert "defaultTournamentAnnouncementLead" in params, "Missing parameter 'defaultTournamentAnnouncementLead'"
    assert "minimalAttendance" in params, "Missing parameter 'minimalAttendance'"
    assert "startDate" in params, "Missing parameter 'startDate'"
    assert "defaultMaxPlayers" in params, "Missing parameter 'defaultMaxPlayers'"

def test_pokerleague::competition_has_defaultBuyIn():
    assert hasattr(pokerleague::Competition, "defaultBuyIn")
    descriptor = None
    for klass in pokerleague::Competition.__mro__:
        if "defaultBuyIn" in klass.__dict__:
            descriptor = klass.__dict__["defaultBuyIn"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague::competition_has_endDate():
    assert hasattr(pokerleague::Competition, "endDate")
    descriptor = None
    for klass in pokerleague::Competition.__mro__:
        if "endDate" in klass.__dict__:
            descriptor = klass.__dict__["endDate"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague::competition_has_defaultMinPlayers():
    assert hasattr(pokerleague::Competition, "defaultMinPlayers")
    descriptor = None
    for klass in pokerleague::Competition.__mro__:
        if "defaultMinPlayers" in klass.__dict__:
            descriptor = klass.__dict__["defaultMinPlayers"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague::competition_has_defaultTournamentAnnouncementLead():
    assert hasattr(pokerleague::Competition, "defaultTournamentAnnouncementLead")
    descriptor = None
    for klass in pokerleague::Competition.__mro__:
        if "defaultTournamentAnnouncementLead" in klass.__dict__:
            descriptor = klass.__dict__["defaultTournamentAnnouncementLead"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague::competition_has_minimalAttendance():
    assert hasattr(pokerleague::Competition, "minimalAttendance")
    descriptor = None
    for klass in pokerleague::Competition.__mro__:
        if "minimalAttendance" in klass.__dict__:
            descriptor = klass.__dict__["minimalAttendance"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague::competition_has_startDate():
    assert hasattr(pokerleague::Competition, "startDate")
    descriptor = None
    for klass in pokerleague::Competition.__mro__:
        if "startDate" in klass.__dict__:
            descriptor = klass.__dict__["startDate"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague::competition_has_defaultMaxPlayers():
    assert hasattr(pokerleague::Competition, "defaultMaxPlayers")
    descriptor = None
    for klass in pokerleague::Competition.__mro__:
        if "defaultMaxPlayers" in klass.__dict__:
            descriptor = klass.__dict__["defaultMaxPlayers"]
            break
    assert isinstance(descriptor, property)



def test_pokerleague::tournament_is_not_abstract():
    assert not inspect.isabstract(pokerleague::Tournament)


def test_pokerleague::tournament_constructor_exists():
    assert callable(pokerleague::Tournament.__init__)


def test_pokerleague::tournament_constructor_args():
    sig = inspect.signature(pokerleague::Tournament.__init__)
    params = list(sig.parameters.keys())
    assert "tournamentStart" in params, "Missing parameter 'tournamentStart'"
    assert "tournamentAnnouncementLead" in params, "Missing parameter 'tournamentAnnouncementLead'"
    assert "maxPlayers" in params, "Missing parameter 'maxPlayers'"
    assert "minPlayers" in params, "Missing parameter 'minPlayers'"
    assert "tournamentEnd" in params, "Missing parameter 'tournamentEnd'"
    assert "defaultBuyIn" in params, "Missing parameter 'defaultBuyIn'"

def test_pokerleague::tournament_has_tournamentStart():
    assert hasattr(pokerleague::Tournament, "tournamentStart")
    descriptor = None
    for klass in pokerleague::Tournament.__mro__:
        if "tournamentStart" in klass.__dict__:
            descriptor = klass.__dict__["tournamentStart"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague::tournament_has_tournamentAnnouncementLead():
    assert hasattr(pokerleague::Tournament, "tournamentAnnouncementLead")
    descriptor = None
    for klass in pokerleague::Tournament.__mro__:
        if "tournamentAnnouncementLead" in klass.__dict__:
            descriptor = klass.__dict__["tournamentAnnouncementLead"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague::tournament_has_maxPlayers():
    assert hasattr(pokerleague::Tournament, "maxPlayers")
    descriptor = None
    for klass in pokerleague::Tournament.__mro__:
        if "maxPlayers" in klass.__dict__:
            descriptor = klass.__dict__["maxPlayers"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague::tournament_has_minPlayers():
    assert hasattr(pokerleague::Tournament, "minPlayers")
    descriptor = None
    for klass in pokerleague::Tournament.__mro__:
        if "minPlayers" in klass.__dict__:
            descriptor = klass.__dict__["minPlayers"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague::tournament_has_tournamentEnd():
    assert hasattr(pokerleague::Tournament, "tournamentEnd")
    descriptor = None
    for klass in pokerleague::Tournament.__mro__:
        if "tournamentEnd" in klass.__dict__:
            descriptor = klass.__dict__["tournamentEnd"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague::tournament_has_defaultBuyIn():
    assert hasattr(pokerleague::Tournament, "defaultBuyIn")
    descriptor = None
    for klass in pokerleague::Tournament.__mro__:
        if "defaultBuyIn" in klass.__dict__:
            descriptor = klass.__dict__["defaultBuyIn"]
            break
    assert isinstance(descriptor, property)



def test_pokerleague::prizemoneyruleset_is_not_abstract():
    assert not inspect.isabstract(pokerleague::PrizeMoneyRuleSet)


def test_pokerleague::prizemoneyruleset_constructor_exists():
    assert callable(pokerleague::PrizeMoneyRuleSet.__init__)


def test_pokerleague::prizemoneyruleset_constructor_args():
    sig = inspect.signature(pokerleague::PrizeMoneyRuleSet.__init__)
    params = list(sig.parameters.keys())



def test_identifiableentity_is_not_abstract():
    assert not inspect.isabstract(IdentifiableEntity)


def test_identifiableentity_constructor_exists():
    assert callable(IdentifiableEntity.__init__)


def test_identifiableentity_constructor_args():
    sig = inspect.signature(IdentifiableEntity.__init__)
    params = list(sig.parameters.keys())



def test_pokerleague::player_is_not_abstract():
    assert not inspect.isabstract(pokerleague::Player)


def test_pokerleague::player_constructor_exists():
    assert callable(pokerleague::Player.__init__)


def test_pokerleague::player_constructor_args():
    sig = inspect.signature(pokerleague::Player.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "active" in params, "Missing parameter 'active'"
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "nick" in params, "Missing parameter 'nick'"
    assert "emailAddress" in params, "Missing parameter 'emailAddress'"

def test_pokerleague::player_has_lastName():
    assert hasattr(pokerleague::Player, "lastName")
    descriptor = None
    for klass in pokerleague::Player.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague::player_has_active():
    assert hasattr(pokerleague::Player, "active")
    descriptor = None
    for klass in pokerleague::Player.__mro__:
        if "active" in klass.__dict__:
            descriptor = klass.__dict__["active"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague::player_has_firstName():
    assert hasattr(pokerleague::Player, "firstName")
    descriptor = None
    for klass in pokerleague::Player.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague::player_has_nick():
    assert hasattr(pokerleague::Player, "nick")
    descriptor = None
    for klass in pokerleague::Player.__mro__:
        if "nick" in klass.__dict__:
            descriptor = klass.__dict__["nick"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague::player_has_emailAddress():
    assert hasattr(pokerleague::Player, "emailAddress")
    descriptor = None
    for klass in pokerleague::Player.__mro__:
        if "emailAddress" in klass.__dict__:
            descriptor = klass.__dict__["emailAddress"]
            break
    assert isinstance(descriptor, property)



def test_pokerleague::game_is_not_abstract():
    assert not inspect.isabstract(pokerleague::Game)


def test_pokerleague::game_constructor_exists():
    assert callable(pokerleague::Game.__init__)


def test_pokerleague::game_constructor_args():
    sig = inspect.signature(pokerleague::Game.__init__)
    params = list(sig.parameters.keys())
    assert "buyIn" in params, "Missing parameter 'buyIn'"
    assert "ordinal" in params, "Missing parameter 'ordinal'"

def test_pokerleague::game_has_buyIn():
    assert hasattr(pokerleague::Game, "buyIn")
    descriptor = None
    for klass in pokerleague::Game.__mro__:
        if "buyIn" in klass.__dict__:
            descriptor = klass.__dict__["buyIn"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague::game_has_ordinal():
    assert hasattr(pokerleague::Game, "ordinal")
    descriptor = None
    for klass in pokerleague::Game.__mro__:
        if "ordinal" in klass.__dict__:
            descriptor = klass.__dict__["ordinal"]
            break
    assert isinstance(descriptor, property)



def test_pokerleague::prizemoneyformula_is_not_abstract():
    assert not inspect.isabstract(pokerleague::PrizeMoneyFormula)


def test_pokerleague::prizemoneyformula_constructor_exists():
    assert callable(pokerleague::PrizeMoneyFormula.__init__)


def test_pokerleague::prizemoneyformula_constructor_args():
    sig = inspect.signature(pokerleague::PrizeMoneyFormula.__init__)
    params = list(sig.parameters.keys())
    assert "relativePrizeMoney" in params, "Missing parameter 'relativePrizeMoney'"
    assert "rank" in params, "Missing parameter 'rank'"

def test_pokerleague::prizemoneyformula_has_relativePrizeMoney():
    assert hasattr(pokerleague::PrizeMoneyFormula, "relativePrizeMoney")
    descriptor = None
    for klass in pokerleague::PrizeMoneyFormula.__mro__:
        if "relativePrizeMoney" in klass.__dict__:
            descriptor = klass.__dict__["relativePrizeMoney"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague::prizemoneyformula_has_rank():
    assert hasattr(pokerleague::PrizeMoneyFormula, "rank")
    descriptor = None
    for klass in pokerleague::PrizeMoneyFormula.__mro__:
        if "rank" in klass.__dict__:
            descriptor = klass.__dict__["rank"]
            break
    assert isinstance(descriptor, property)



def test_pokerleague::invitation_is_not_abstract():
    assert not inspect.isabstract(pokerleague::Invitation)


def test_pokerleague::invitation_constructor_exists():
    assert callable(pokerleague::Invitation.__init__)


def test_pokerleague::invitation_constructor_args():
    sig = inspect.signature(pokerleague::Invitation.__init__)
    params = list(sig.parameters.keys())
    assert "ordinal" in params, "Missing parameter 'ordinal'"
    assert "uuid" in params, "Missing parameter 'uuid'"
    assert "reply" in params, "Missing parameter 'reply'"

def test_pokerleague::invitation_has_ordinal():
    assert hasattr(pokerleague::Invitation, "ordinal")
    descriptor = None
    for klass in pokerleague::Invitation.__mro__:
        if "ordinal" in klass.__dict__:
            descriptor = klass.__dict__["ordinal"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague::invitation_has_uuid():
    assert hasattr(pokerleague::Invitation, "uuid")
    descriptor = None
    for klass in pokerleague::Invitation.__mro__:
        if "uuid" in klass.__dict__:
            descriptor = klass.__dict__["uuid"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague::invitation_has_reply():
    assert hasattr(pokerleague::Invitation, "reply")
    descriptor = None
    for klass in pokerleague::Invitation.__mro__:
        if "reply" in klass.__dict__:
            descriptor = klass.__dict__["reply"]
            break
    assert isinstance(descriptor, property)



def test_pokerleague::prizemoneyrule_is_not_abstract():
    assert not inspect.isabstract(pokerleague::PrizeMoneyRule)


def test_pokerleague::prizemoneyrule_constructor_exists():
    assert callable(pokerleague::PrizeMoneyRule.__init__)


def test_pokerleague::prizemoneyrule_constructor_args():
    sig = inspect.signature(pokerleague::PrizeMoneyRule.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfPlayers" in params, "Missing parameter 'numberOfPlayers'"

def test_pokerleague::prizemoneyrule_has_numberOfPlayers():
    assert hasattr(pokerleague::PrizeMoneyRule, "numberOfPlayers")
    descriptor = None
    for klass in pokerleague::PrizeMoneyRule.__mro__:
        if "numberOfPlayers" in klass.__dict__:
            descriptor = klass.__dict__["numberOfPlayers"]
            break
    assert isinstance(descriptor, property)



def test_pokerleague::playeringame_is_not_abstract():
    assert not inspect.isabstract(pokerleague::PlayerInGame)


def test_pokerleague::playeringame_constructor_exists():
    assert callable(pokerleague::PlayerInGame.__init__)


def test_pokerleague::playeringame_constructor_args():
    sig = inspect.signature(pokerleague::PlayerInGame.__init__)
    params = list(sig.parameters.keys())
    assert "rank" in params, "Missing parameter 'rank'"

def test_pokerleague::playeringame_has_rank():
    assert hasattr(pokerleague::PlayerInGame, "rank")
    descriptor = None
    for klass in pokerleague::PlayerInGame.__mro__:
        if "rank" in klass.__dict__:
            descriptor = klass.__dict__["rank"]
            break
    assert isinstance(descriptor, property)



def test_pokerleague::invitationevent_is_not_abstract():
    assert not inspect.isabstract(pokerleague::InvitationEvent)


def test_pokerleague::invitationevent_constructor_exists():
    assert callable(pokerleague::InvitationEvent.__init__)


def test_pokerleague::invitationevent_constructor_args():
    sig = inspect.signature(pokerleague::InvitationEvent.__init__)
    params = list(sig.parameters.keys())
    assert "sent" in params, "Missing parameter 'sent'"
    assert "eventTime" in params, "Missing parameter 'eventTime'"
    assert "eventType" in params, "Missing parameter 'eventType'"

def test_pokerleague::invitationevent_has_sent():
    assert hasattr(pokerleague::InvitationEvent, "sent")
    descriptor = None
    for klass in pokerleague::InvitationEvent.__mro__:
        if "sent" in klass.__dict__:
            descriptor = klass.__dict__["sent"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague::invitationevent_has_eventTime():
    assert hasattr(pokerleague::InvitationEvent, "eventTime")
    descriptor = None
    for klass in pokerleague::InvitationEvent.__mro__:
        if "eventTime" in klass.__dict__:
            descriptor = klass.__dict__["eventTime"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague::invitationevent_has_eventType():
    assert hasattr(pokerleague::InvitationEvent, "eventType")
    descriptor = None
    for klass in pokerleague::InvitationEvent.__mro__:
        if "eventType" in klass.__dict__:
            descriptor = klass.__dict__["eventType"]
            break
    assert isinstance(descriptor, property)



def test_pokerleague::describedentity_is_not_abstract():
    assert not inspect.isabstract(pokerleague::DescribedEntity)


def test_pokerleague::describedentity_constructor_exists():
    assert callable(pokerleague::DescribedEntity.__init__)


def test_pokerleague::describedentity_constructor_args():
    sig = inspect.signature(pokerleague::DescribedEntity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_pokerleague::describedentity_has_name():
    assert hasattr(pokerleague::DescribedEntity, "name")
    descriptor = None
    for klass in pokerleague::DescribedEntity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague::describedentity_has_description():
    assert hasattr(pokerleague::DescribedEntity, "description")
    descriptor = None
    for klass in pokerleague::DescribedEntity.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_pokerleague::identifiableentity_is_not_abstract():
    assert not inspect.isabstract(pokerleague::IdentifiableEntity)


def test_pokerleague::identifiableentity_constructor_exists():
    assert callable(pokerleague::IdentifiableEntity.__init__)


def test_pokerleague::identifiableentity_constructor_args():
    sig = inspect.signature(pokerleague::IdentifiableEntity.__init__)
    params = list(sig.parameters.keys())
    assert "proxy" in params, "Missing parameter 'proxy'"
    assert "obsolete" in params, "Missing parameter 'obsolete'"
    assert "id" in params, "Missing parameter 'id'"

def test_pokerleague::identifiableentity_has_proxy():
    assert hasattr(pokerleague::IdentifiableEntity, "proxy")
    descriptor = None
    for klass in pokerleague::IdentifiableEntity.__mro__:
        if "proxy" in klass.__dict__:
            descriptor = klass.__dict__["proxy"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague::identifiableentity_has_obsolete():
    assert hasattr(pokerleague::IdentifiableEntity, "obsolete")
    descriptor = None
    for klass in pokerleague::IdentifiableEntity.__mro__:
        if "obsolete" in klass.__dict__:
            descriptor = klass.__dict__["obsolete"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague::identifiableentity_has_id():
    assert hasattr(pokerleague::IdentifiableEntity, "id")
    descriptor = None
    for klass in pokerleague::IdentifiableEntity.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_pokerleague::settings_is_not_abstract():
    assert not inspect.isabstract(pokerleague::Settings)


def test_pokerleague::settings_constructor_exists():
    assert callable(pokerleague::Settings.__init__)


def test_pokerleague::settings_constructor_args():
    sig = inspect.signature(pokerleague::Settings.__init__)
    params = list(sig.parameters.keys())
    assert "adminPassword" in params, "Missing parameter 'adminPassword'"
    assert "defaultTimeZone" in params, "Missing parameter 'defaultTimeZone'"
    assert "id" in params, "Missing parameter 'id'"

def test_pokerleague::settings_has_adminPassword():
    assert hasattr(pokerleague::Settings, "adminPassword")
    descriptor = None
    for klass in pokerleague::Settings.__mro__:
        if "adminPassword" in klass.__dict__:
            descriptor = klass.__dict__["adminPassword"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague::settings_has_defaultTimeZone():
    assert hasattr(pokerleague::Settings, "defaultTimeZone")
    descriptor = None
    for klass in pokerleague::Settings.__mro__:
        if "defaultTimeZone" in klass.__dict__:
            descriptor = klass.__dict__["defaultTimeZone"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague::settings_has_id():
    assert hasattr(pokerleague::Settings, "id")
    descriptor = None
    for klass in pokerleague::Settings.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_invitationreply_exists():
    # Check that the Enumeration exists
    assert InvitationReply is not None

def test_invitationreply_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InvitationReply]
    expected_literals = [
        "REJECTED",
        "NO_REPLY",
        "ACCEPTED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InvitationReply"

def test_invitationeventtype_exists():
    # Check that the Enumeration exists
    assert InvitationEventType is not None

def test_invitationeventtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InvitationEventType]
    expected_literals = [
        "CHANGED",
        "GENERATED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InvitationEventType"


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
Serializable_strategy = st.builds(
    Serializable,
)
pokerleague::DataVersion_strategy = st.builds(
    pokerleague::DataVersion,
    id=
        st.integers(),
    currentVersion=
        safe_text
)
pokerleague::DataStructureVersion_strategy = st.builds(
    pokerleague::DataStructureVersion,
    currentVersion=
        safe_text,
    id=
        st.integers()
)
pokerleague::Serializable_strategy = st.builds(
    pokerleague::Serializable,
)
DescribedEntity_strategy = st.builds(
    DescribedEntity,
)
pokerleague::Competition_strategy = st.builds(
    pokerleague::Competition,
    defaultBuyIn=
        st.integers(),
    endDate=
        st.dates(),
    defaultMinPlayers=
        st.integers(),
    defaultTournamentAnnouncementLead=
        st.integers(),
    minimalAttendance=
        st.integers(),
    startDate=
        st.dates(),
    defaultMaxPlayers=
        st.integers()
)
pokerleague::Tournament_strategy = st.builds(
    pokerleague::Tournament,
    tournamentStart=
        safe_text,
    tournamentAnnouncementLead=
        st.integers(),
    maxPlayers=
        st.integers(),
    minPlayers=
        st.integers(),
    tournamentEnd=
        safe_text,
    defaultBuyIn=
        st.integers()
)
pokerleague::PrizeMoneyRuleSet_strategy = st.builds(
    pokerleague::PrizeMoneyRuleSet,
)
IdentifiableEntity_strategy = st.builds(
    IdentifiableEntity,
)
pokerleague::Player_strategy = st.builds(
    pokerleague::Player,
    lastName=
        safe_text,
    active=
        st.booleans(),
    firstName=
        safe_text,
    nick=
        safe_text,
    emailAddress=
        safe_text
)
pokerleague::Game_strategy = st.builds(
    pokerleague::Game,
    buyIn=
        st.integers(),
    ordinal=
        st.integers()
)
pokerleague::PrizeMoneyFormula_strategy = st.builds(
    pokerleague::PrizeMoneyFormula,
    relativePrizeMoney=
        st.integers(),
    rank=
        st.integers()
)
pokerleague::Invitation_strategy = st.builds(
    pokerleague::Invitation,
    ordinal=
        st.integers(),
    uuid=
        safe_text,
    reply=
        safe_text
)
pokerleague::PrizeMoneyRule_strategy = st.builds(
    pokerleague::PrizeMoneyRule,
    numberOfPlayers=
        st.integers()
)
pokerleague::PlayerInGame_strategy = st.builds(
    pokerleague::PlayerInGame,
    rank=
        st.integers()
)
pokerleague::InvitationEvent_strategy = st.builds(
    pokerleague::InvitationEvent,
    sent=
        st.booleans(),
    eventTime=
        safe_text,
    eventType=
        safe_text
)
pokerleague::DescribedEntity_strategy = st.builds(
    pokerleague::DescribedEntity,
    name=
        safe_text,
    description=
        safe_text
)
pokerleague::IdentifiableEntity_strategy = st.builds(
    pokerleague::IdentifiableEntity,
    proxy=
        st.booleans(),
    obsolete=
        st.booleans(),
    id=
        st.integers()
)
pokerleague::Settings_strategy = st.builds(
    pokerleague::Settings,
    adminPassword=
        safe_text,
    defaultTimeZone=
        safe_text,
    id=
        st.integers()
)

@given(instance=Serializable_strategy)
@settings(max_examples=50)
def test_serializable_instantiation(instance):
    assert isinstance(instance, Serializable)

@given(instance=pokerleague::DataVersion_strategy)
@settings(max_examples=50)
def test_pokerleague::dataversion_instantiation(instance):
    assert isinstance(instance, pokerleague::DataVersion)

@given(instance=pokerleague::DataVersion_strategy)
def test_pokerleague::dataversion_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=pokerleague::DataVersion_strategy)
def test_pokerleague::dataversion_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=pokerleague::DataVersion_strategy)
def test_pokerleague::dataversion_currentVersion_type(instance):
    assert isinstance(instance.currentVersion, str)


@given(instance=pokerleague::DataVersion_strategy)
def test_pokerleague::dataversion_currentVersion_setter(instance):
    original = instance.currentVersion
    instance.currentVersion = original
    assert instance.currentVersion == original

@given(instance=pokerleague::DataStructureVersion_strategy)
@settings(max_examples=50)
def test_pokerleague::datastructureversion_instantiation(instance):
    assert isinstance(instance, pokerleague::DataStructureVersion)

@given(instance=pokerleague::DataStructureVersion_strategy)
def test_pokerleague::datastructureversion_currentVersion_type(instance):
    assert isinstance(instance.currentVersion, str)


@given(instance=pokerleague::DataStructureVersion_strategy)
def test_pokerleague::datastructureversion_currentVersion_setter(instance):
    original = instance.currentVersion
    instance.currentVersion = original
    assert instance.currentVersion == original

@given(instance=pokerleague::DataStructureVersion_strategy)
def test_pokerleague::datastructureversion_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=pokerleague::DataStructureVersion_strategy)
def test_pokerleague::datastructureversion_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=pokerleague::Serializable_strategy)
@settings(max_examples=50)
def test_pokerleague::serializable_instantiation(instance):
    assert isinstance(instance, pokerleague::Serializable)

@given(instance=DescribedEntity_strategy)
@settings(max_examples=50)
def test_describedentity_instantiation(instance):
    assert isinstance(instance, DescribedEntity)

@given(instance=pokerleague::Competition_strategy)
@settings(max_examples=50)
def test_pokerleague::competition_instantiation(instance):
    assert isinstance(instance, pokerleague::Competition)

@given(instance=pokerleague::Competition_strategy)
def test_pokerleague::competition_defaultBuyIn_type(instance):
    assert isinstance(instance.defaultBuyIn, int)


@given(instance=pokerleague::Competition_strategy)
def test_pokerleague::competition_defaultBuyIn_setter(instance):
    original = instance.defaultBuyIn
    instance.defaultBuyIn = original
    assert instance.defaultBuyIn == original

@given(instance=pokerleague::Competition_strategy)
def test_pokerleague::competition_endDate_type(instance):
    assert isinstance(instance.endDate, date)


@given(instance=pokerleague::Competition_strategy)
def test_pokerleague::competition_endDate_setter(instance):
    original = instance.endDate
    instance.endDate = original
    assert instance.endDate == original

@given(instance=pokerleague::Competition_strategy)
def test_pokerleague::competition_defaultMinPlayers_type(instance):
    assert isinstance(instance.defaultMinPlayers, int)


@given(instance=pokerleague::Competition_strategy)
def test_pokerleague::competition_defaultMinPlayers_setter(instance):
    original = instance.defaultMinPlayers
    instance.defaultMinPlayers = original
    assert instance.defaultMinPlayers == original

@given(instance=pokerleague::Competition_strategy)
def test_pokerleague::competition_defaultTournamentAnnouncementLead_type(instance):
    assert isinstance(instance.defaultTournamentAnnouncementLead, int)


@given(instance=pokerleague::Competition_strategy)
def test_pokerleague::competition_defaultTournamentAnnouncementLead_setter(instance):
    original = instance.defaultTournamentAnnouncementLead
    instance.defaultTournamentAnnouncementLead = original
    assert instance.defaultTournamentAnnouncementLead == original

@given(instance=pokerleague::Competition_strategy)
def test_pokerleague::competition_minimalAttendance_type(instance):
    assert isinstance(instance.minimalAttendance, int)


@given(instance=pokerleague::Competition_strategy)
def test_pokerleague::competition_minimalAttendance_setter(instance):
    original = instance.minimalAttendance
    instance.minimalAttendance = original
    assert instance.minimalAttendance == original

@given(instance=pokerleague::Competition_strategy)
def test_pokerleague::competition_startDate_type(instance):
    assert isinstance(instance.startDate, date)


@given(instance=pokerleague::Competition_strategy)
def test_pokerleague::competition_startDate_setter(instance):
    original = instance.startDate
    instance.startDate = original
    assert instance.startDate == original

@given(instance=pokerleague::Competition_strategy)
def test_pokerleague::competition_defaultMaxPlayers_type(instance):
    assert isinstance(instance.defaultMaxPlayers, int)


@given(instance=pokerleague::Competition_strategy)
def test_pokerleague::competition_defaultMaxPlayers_setter(instance):
    original = instance.defaultMaxPlayers
    instance.defaultMaxPlayers = original
    assert instance.defaultMaxPlayers == original

@given(instance=pokerleague::Tournament_strategy)
@settings(max_examples=50)
def test_pokerleague::tournament_instantiation(instance):
    assert isinstance(instance, pokerleague::Tournament)

@given(instance=pokerleague::Tournament_strategy)
def test_pokerleague::tournament_tournamentStart_type(instance):
    assert isinstance(instance.tournamentStart, str)


@given(instance=pokerleague::Tournament_strategy)
def test_pokerleague::tournament_tournamentStart_setter(instance):
    original = instance.tournamentStart
    instance.tournamentStart = original
    assert instance.tournamentStart == original

@given(instance=pokerleague::Tournament_strategy)
def test_pokerleague::tournament_tournamentAnnouncementLead_type(instance):
    assert isinstance(instance.tournamentAnnouncementLead, int)


@given(instance=pokerleague::Tournament_strategy)
def test_pokerleague::tournament_tournamentAnnouncementLead_setter(instance):
    original = instance.tournamentAnnouncementLead
    instance.tournamentAnnouncementLead = original
    assert instance.tournamentAnnouncementLead == original

@given(instance=pokerleague::Tournament_strategy)
def test_pokerleague::tournament_maxPlayers_type(instance):
    assert isinstance(instance.maxPlayers, int)


@given(instance=pokerleague::Tournament_strategy)
def test_pokerleague::tournament_maxPlayers_setter(instance):
    original = instance.maxPlayers
    instance.maxPlayers = original
    assert instance.maxPlayers == original

@given(instance=pokerleague::Tournament_strategy)
def test_pokerleague::tournament_minPlayers_type(instance):
    assert isinstance(instance.minPlayers, int)


@given(instance=pokerleague::Tournament_strategy)
def test_pokerleague::tournament_minPlayers_setter(instance):
    original = instance.minPlayers
    instance.minPlayers = original
    assert instance.minPlayers == original

@given(instance=pokerleague::Tournament_strategy)
def test_pokerleague::tournament_tournamentEnd_type(instance):
    assert isinstance(instance.tournamentEnd, str)


@given(instance=pokerleague::Tournament_strategy)
def test_pokerleague::tournament_tournamentEnd_setter(instance):
    original = instance.tournamentEnd
    instance.tournamentEnd = original
    assert instance.tournamentEnd == original

@given(instance=pokerleague::Tournament_strategy)
def test_pokerleague::tournament_defaultBuyIn_type(instance):
    assert isinstance(instance.defaultBuyIn, int)


@given(instance=pokerleague::Tournament_strategy)
def test_pokerleague::tournament_defaultBuyIn_setter(instance):
    original = instance.defaultBuyIn
    instance.defaultBuyIn = original
    assert instance.defaultBuyIn == original

@given(instance=pokerleague::PrizeMoneyRuleSet_strategy)
@settings(max_examples=50)
def test_pokerleague::prizemoneyruleset_instantiation(instance):
    assert isinstance(instance, pokerleague::PrizeMoneyRuleSet)

@given(instance=IdentifiableEntity_strategy)
@settings(max_examples=50)
def test_identifiableentity_instantiation(instance):
    assert isinstance(instance, IdentifiableEntity)

@given(instance=pokerleague::Player_strategy)
@settings(max_examples=50)
def test_pokerleague::player_instantiation(instance):
    assert isinstance(instance, pokerleague::Player)

@given(instance=pokerleague::Player_strategy)
def test_pokerleague::player_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=pokerleague::Player_strategy)
def test_pokerleague::player_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=pokerleague::Player_strategy)
def test_pokerleague::player_active_type(instance):
    assert isinstance(instance.active, bool)


@given(instance=pokerleague::Player_strategy)
def test_pokerleague::player_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original

@given(instance=pokerleague::Player_strategy)
def test_pokerleague::player_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=pokerleague::Player_strategy)
def test_pokerleague::player_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=pokerleague::Player_strategy)
def test_pokerleague::player_nick_type(instance):
    assert isinstance(instance.nick, str)


@given(instance=pokerleague::Player_strategy)
def test_pokerleague::player_nick_setter(instance):
    original = instance.nick
    instance.nick = original
    assert instance.nick == original

@given(instance=pokerleague::Player_strategy)
def test_pokerleague::player_emailAddress_type(instance):
    assert isinstance(instance.emailAddress, str)


@given(instance=pokerleague::Player_strategy)
def test_pokerleague::player_emailAddress_setter(instance):
    original = instance.emailAddress
    instance.emailAddress = original
    assert instance.emailAddress == original

@given(instance=pokerleague::Game_strategy)
@settings(max_examples=50)
def test_pokerleague::game_instantiation(instance):
    assert isinstance(instance, pokerleague::Game)

@given(instance=pokerleague::Game_strategy)
def test_pokerleague::game_buyIn_type(instance):
    assert isinstance(instance.buyIn, int)


@given(instance=pokerleague::Game_strategy)
def test_pokerleague::game_buyIn_setter(instance):
    original = instance.buyIn
    instance.buyIn = original
    assert instance.buyIn == original

@given(instance=pokerleague::Game_strategy)
def test_pokerleague::game_ordinal_type(instance):
    assert isinstance(instance.ordinal, int)


@given(instance=pokerleague::Game_strategy)
def test_pokerleague::game_ordinal_setter(instance):
    original = instance.ordinal
    instance.ordinal = original
    assert instance.ordinal == original

@given(instance=pokerleague::PrizeMoneyFormula_strategy)
@settings(max_examples=50)
def test_pokerleague::prizemoneyformula_instantiation(instance):
    assert isinstance(instance, pokerleague::PrizeMoneyFormula)

@given(instance=pokerleague::PrizeMoneyFormula_strategy)
def test_pokerleague::prizemoneyformula_relativePrizeMoney_type(instance):
    assert isinstance(instance.relativePrizeMoney, int)


@given(instance=pokerleague::PrizeMoneyFormula_strategy)
def test_pokerleague::prizemoneyformula_relativePrizeMoney_setter(instance):
    original = instance.relativePrizeMoney
    instance.relativePrizeMoney = original
    assert instance.relativePrizeMoney == original

@given(instance=pokerleague::PrizeMoneyFormula_strategy)
def test_pokerleague::prizemoneyformula_rank_type(instance):
    assert isinstance(instance.rank, int)


@given(instance=pokerleague::PrizeMoneyFormula_strategy)
def test_pokerleague::prizemoneyformula_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original

@given(instance=pokerleague::Invitation_strategy)
@settings(max_examples=50)
def test_pokerleague::invitation_instantiation(instance):
    assert isinstance(instance, pokerleague::Invitation)

@given(instance=pokerleague::Invitation_strategy)
def test_pokerleague::invitation_ordinal_type(instance):
    assert isinstance(instance.ordinal, int)


@given(instance=pokerleague::Invitation_strategy)
def test_pokerleague::invitation_ordinal_setter(instance):
    original = instance.ordinal
    instance.ordinal = original
    assert instance.ordinal == original

@given(instance=pokerleague::Invitation_strategy)
def test_pokerleague::invitation_uuid_type(instance):
    assert isinstance(instance.uuid, str)


@given(instance=pokerleague::Invitation_strategy)
def test_pokerleague::invitation_uuid_setter(instance):
    original = instance.uuid
    instance.uuid = original
    assert instance.uuid == original

@given(instance=pokerleague::Invitation_strategy)
def test_pokerleague::invitation_reply_type(instance):
    assert isinstance(instance.reply, str)


@given(instance=pokerleague::Invitation_strategy)
def test_pokerleague::invitation_reply_setter(instance):
    original = instance.reply
    instance.reply = original
    assert instance.reply == original

@given(instance=pokerleague::PrizeMoneyRule_strategy)
@settings(max_examples=50)
def test_pokerleague::prizemoneyrule_instantiation(instance):
    assert isinstance(instance, pokerleague::PrizeMoneyRule)

@given(instance=pokerleague::PrizeMoneyRule_strategy)
def test_pokerleague::prizemoneyrule_numberOfPlayers_type(instance):
    assert isinstance(instance.numberOfPlayers, int)


@given(instance=pokerleague::PrizeMoneyRule_strategy)
def test_pokerleague::prizemoneyrule_numberOfPlayers_setter(instance):
    original = instance.numberOfPlayers
    instance.numberOfPlayers = original
    assert instance.numberOfPlayers == original

@given(instance=pokerleague::PlayerInGame_strategy)
@settings(max_examples=50)
def test_pokerleague::playeringame_instantiation(instance):
    assert isinstance(instance, pokerleague::PlayerInGame)

@given(instance=pokerleague::PlayerInGame_strategy)
def test_pokerleague::playeringame_rank_type(instance):
    assert isinstance(instance.rank, int)


@given(instance=pokerleague::PlayerInGame_strategy)
def test_pokerleague::playeringame_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original

@given(instance=pokerleague::InvitationEvent_strategy)
@settings(max_examples=50)
def test_pokerleague::invitationevent_instantiation(instance):
    assert isinstance(instance, pokerleague::InvitationEvent)

@given(instance=pokerleague::InvitationEvent_strategy)
def test_pokerleague::invitationevent_sent_type(instance):
    assert isinstance(instance.sent, bool)


@given(instance=pokerleague::InvitationEvent_strategy)
def test_pokerleague::invitationevent_sent_setter(instance):
    original = instance.sent
    instance.sent = original
    assert instance.sent == original

@given(instance=pokerleague::InvitationEvent_strategy)
def test_pokerleague::invitationevent_eventTime_type(instance):
    assert isinstance(instance.eventTime, str)


@given(instance=pokerleague::InvitationEvent_strategy)
def test_pokerleague::invitationevent_eventTime_setter(instance):
    original = instance.eventTime
    instance.eventTime = original
    assert instance.eventTime == original

@given(instance=pokerleague::InvitationEvent_strategy)
def test_pokerleague::invitationevent_eventType_type(instance):
    assert isinstance(instance.eventType, str)


@given(instance=pokerleague::InvitationEvent_strategy)
def test_pokerleague::invitationevent_eventType_setter(instance):
    original = instance.eventType
    instance.eventType = original
    assert instance.eventType == original

@given(instance=pokerleague::DescribedEntity_strategy)
@settings(max_examples=50)
def test_pokerleague::describedentity_instantiation(instance):
    assert isinstance(instance, pokerleague::DescribedEntity)

@given(instance=pokerleague::DescribedEntity_strategy)
def test_pokerleague::describedentity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=pokerleague::DescribedEntity_strategy)
def test_pokerleague::describedentity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pokerleague::DescribedEntity_strategy)
def test_pokerleague::describedentity_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=pokerleague::DescribedEntity_strategy)
def test_pokerleague::describedentity_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=pokerleague::IdentifiableEntity_strategy)
@settings(max_examples=50)
def test_pokerleague::identifiableentity_instantiation(instance):
    assert isinstance(instance, pokerleague::IdentifiableEntity)

@given(instance=pokerleague::IdentifiableEntity_strategy)
def test_pokerleague::identifiableentity_proxy_type(instance):
    assert isinstance(instance.proxy, bool)


@given(instance=pokerleague::IdentifiableEntity_strategy)
def test_pokerleague::identifiableentity_proxy_setter(instance):
    original = instance.proxy
    instance.proxy = original
    assert instance.proxy == original

@given(instance=pokerleague::IdentifiableEntity_strategy)
def test_pokerleague::identifiableentity_obsolete_type(instance):
    assert isinstance(instance.obsolete, bool)


@given(instance=pokerleague::IdentifiableEntity_strategy)
def test_pokerleague::identifiableentity_obsolete_setter(instance):
    original = instance.obsolete
    instance.obsolete = original
    assert instance.obsolete == original

@given(instance=pokerleague::IdentifiableEntity_strategy)
def test_pokerleague::identifiableentity_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=pokerleague::IdentifiableEntity_strategy)
def test_pokerleague::identifiableentity_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=pokerleague::Settings_strategy)
@settings(max_examples=50)
def test_pokerleague::settings_instantiation(instance):
    assert isinstance(instance, pokerleague::Settings)

@given(instance=pokerleague::Settings_strategy)
def test_pokerleague::settings_adminPassword_type(instance):
    assert isinstance(instance.adminPassword, str)


@given(instance=pokerleague::Settings_strategy)
def test_pokerleague::settings_adminPassword_setter(instance):
    original = instance.adminPassword
    instance.adminPassword = original
    assert instance.adminPassword == original

@given(instance=pokerleague::Settings_strategy)
def test_pokerleague::settings_defaultTimeZone_type(instance):
    assert isinstance(instance.defaultTimeZone, str)


@given(instance=pokerleague::Settings_strategy)
def test_pokerleague::settings_defaultTimeZone_setter(instance):
    original = instance.defaultTimeZone
    instance.defaultTimeZone = original
    assert instance.defaultTimeZone == original

@given(instance=pokerleague::Settings_strategy)
def test_pokerleague::settings_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=pokerleague::Settings_strategy)
def test_pokerleague::settings_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
