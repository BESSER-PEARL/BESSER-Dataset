import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Serializable,
    pokerleague_Settings,
    pokerleague_IdentifiableEntity,
    pokerleague_DataVersion,
    pokerleague_DataStructureVersion,
    pokerleague_Serializable,
    DescribedEntity,
    pokerleague_Competition,
    pokerleague_Tournament,
    pokerleague_PrizeMoneyRuleSet,
    IdentifiableEntity,
    pokerleague_PrizeMoneyRule,
    pokerleague_Player,
    pokerleague_Game,
    pokerleague_Invitation,
    pokerleague_InvitationEvent,
    pokerleague_PrizeMoneyFormula,
    pokerleague_PlayerInGame,
    pokerleague_DescribedEntity,
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



def test_pokerleague_settings_is_not_abstract():
    assert not inspect.isabstract(pokerleague_Settings)


def test_pokerleague_settings_constructor_exists():
    assert callable(pokerleague_Settings.__init__)


def test_pokerleague_settings_constructor_args():
    sig = inspect.signature(pokerleague_Settings.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "defaultTimeZone" in params, "Missing parameter 'defaultTimeZone'"
    assert "adminPassword" in params, "Missing parameter 'adminPassword'"

def test_pokerleague_settings_has_id():
    assert hasattr(pokerleague_Settings, "id")
    descriptor = None
    for klass in pokerleague_Settings.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague_settings_has_defaultTimeZone():
    assert hasattr(pokerleague_Settings, "defaultTimeZone")
    descriptor = None
    for klass in pokerleague_Settings.__mro__:
        if "defaultTimeZone" in klass.__dict__:
            descriptor = klass.__dict__["defaultTimeZone"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague_settings_has_adminPassword():
    assert hasattr(pokerleague_Settings, "adminPassword")
    descriptor = None
    for klass in pokerleague_Settings.__mro__:
        if "adminPassword" in klass.__dict__:
            descriptor = klass.__dict__["adminPassword"]
            break
    assert isinstance(descriptor, property)



def test_pokerleague_identifiableentity_is_not_abstract():
    assert not inspect.isabstract(pokerleague_IdentifiableEntity)


def test_pokerleague_identifiableentity_constructor_exists():
    assert callable(pokerleague_IdentifiableEntity.__init__)


def test_pokerleague_identifiableentity_constructor_args():
    sig = inspect.signature(pokerleague_IdentifiableEntity.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "obsolete" in params, "Missing parameter 'obsolete'"
    assert "proxy" in params, "Missing parameter 'proxy'"

def test_pokerleague_identifiableentity_has_id():
    assert hasattr(pokerleague_IdentifiableEntity, "id")
    descriptor = None
    for klass in pokerleague_IdentifiableEntity.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague_identifiableentity_has_obsolete():
    assert hasattr(pokerleague_IdentifiableEntity, "obsolete")
    descriptor = None
    for klass in pokerleague_IdentifiableEntity.__mro__:
        if "obsolete" in klass.__dict__:
            descriptor = klass.__dict__["obsolete"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague_identifiableentity_has_proxy():
    assert hasattr(pokerleague_IdentifiableEntity, "proxy")
    descriptor = None
    for klass in pokerleague_IdentifiableEntity.__mro__:
        if "proxy" in klass.__dict__:
            descriptor = klass.__dict__["proxy"]
            break
    assert isinstance(descriptor, property)



def test_pokerleague_dataversion_is_not_abstract():
    assert not inspect.isabstract(pokerleague_DataVersion)


def test_pokerleague_dataversion_constructor_exists():
    assert callable(pokerleague_DataVersion.__init__)


def test_pokerleague_dataversion_constructor_args():
    sig = inspect.signature(pokerleague_DataVersion.__init__)
    params = list(sig.parameters.keys())
    assert "currentVersion" in params, "Missing parameter 'currentVersion'"
    assert "id" in params, "Missing parameter 'id'"

def test_pokerleague_dataversion_has_currentVersion():
    assert hasattr(pokerleague_DataVersion, "currentVersion")
    descriptor = None
    for klass in pokerleague_DataVersion.__mro__:
        if "currentVersion" in klass.__dict__:
            descriptor = klass.__dict__["currentVersion"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague_dataversion_has_id():
    assert hasattr(pokerleague_DataVersion, "id")
    descriptor = None
    for klass in pokerleague_DataVersion.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_pokerleague_datastructureversion_is_not_abstract():
    assert not inspect.isabstract(pokerleague_DataStructureVersion)


def test_pokerleague_datastructureversion_constructor_exists():
    assert callable(pokerleague_DataStructureVersion.__init__)


def test_pokerleague_datastructureversion_constructor_args():
    sig = inspect.signature(pokerleague_DataStructureVersion.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "currentVersion" in params, "Missing parameter 'currentVersion'"

def test_pokerleague_datastructureversion_has_id():
    assert hasattr(pokerleague_DataStructureVersion, "id")
    descriptor = None
    for klass in pokerleague_DataStructureVersion.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague_datastructureversion_has_currentVersion():
    assert hasattr(pokerleague_DataStructureVersion, "currentVersion")
    descriptor = None
    for klass in pokerleague_DataStructureVersion.__mro__:
        if "currentVersion" in klass.__dict__:
            descriptor = klass.__dict__["currentVersion"]
            break
    assert isinstance(descriptor, property)



def test_pokerleague_serializable_is_not_abstract():
    assert not inspect.isabstract(pokerleague_Serializable)


def test_pokerleague_serializable_constructor_exists():
    assert callable(pokerleague_Serializable.__init__)


def test_pokerleague_serializable_constructor_args():
    sig = inspect.signature(pokerleague_Serializable.__init__)
    params = list(sig.parameters.keys())



def test_describedentity_is_not_abstract():
    assert not inspect.isabstract(DescribedEntity)


def test_describedentity_constructor_exists():
    assert callable(DescribedEntity.__init__)


def test_describedentity_constructor_args():
    sig = inspect.signature(DescribedEntity.__init__)
    params = list(sig.parameters.keys())



def test_pokerleague_competition_is_not_abstract():
    assert not inspect.isabstract(pokerleague_Competition)


def test_pokerleague_competition_constructor_exists():
    assert callable(pokerleague_Competition.__init__)


def test_pokerleague_competition_constructor_args():
    sig = inspect.signature(pokerleague_Competition.__init__)
    params = list(sig.parameters.keys())
    assert "defaultTournamentAnnouncementLead" in params, "Missing parameter 'defaultTournamentAnnouncementLead'"
    assert "defaultMinPlayers" in params, "Missing parameter 'defaultMinPlayers'"
    assert "startDate" in params, "Missing parameter 'startDate'"
    assert "defaultMaxPlayers" in params, "Missing parameter 'defaultMaxPlayers'"
    assert "endDate" in params, "Missing parameter 'endDate'"
    assert "defaultBuyIn" in params, "Missing parameter 'defaultBuyIn'"
    assert "minimalAttendance" in params, "Missing parameter 'minimalAttendance'"

def test_pokerleague_competition_has_defaultTournamentAnnouncementLead():
    assert hasattr(pokerleague_Competition, "defaultTournamentAnnouncementLead")
    descriptor = None
    for klass in pokerleague_Competition.__mro__:
        if "defaultTournamentAnnouncementLead" in klass.__dict__:
            descriptor = klass.__dict__["defaultTournamentAnnouncementLead"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague_competition_has_defaultMinPlayers():
    assert hasattr(pokerleague_Competition, "defaultMinPlayers")
    descriptor = None
    for klass in pokerleague_Competition.__mro__:
        if "defaultMinPlayers" in klass.__dict__:
            descriptor = klass.__dict__["defaultMinPlayers"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague_competition_has_startDate():
    assert hasattr(pokerleague_Competition, "startDate")
    descriptor = None
    for klass in pokerleague_Competition.__mro__:
        if "startDate" in klass.__dict__:
            descriptor = klass.__dict__["startDate"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague_competition_has_defaultMaxPlayers():
    assert hasattr(pokerleague_Competition, "defaultMaxPlayers")
    descriptor = None
    for klass in pokerleague_Competition.__mro__:
        if "defaultMaxPlayers" in klass.__dict__:
            descriptor = klass.__dict__["defaultMaxPlayers"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague_competition_has_endDate():
    assert hasattr(pokerleague_Competition, "endDate")
    descriptor = None
    for klass in pokerleague_Competition.__mro__:
        if "endDate" in klass.__dict__:
            descriptor = klass.__dict__["endDate"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague_competition_has_defaultBuyIn():
    assert hasattr(pokerleague_Competition, "defaultBuyIn")
    descriptor = None
    for klass in pokerleague_Competition.__mro__:
        if "defaultBuyIn" in klass.__dict__:
            descriptor = klass.__dict__["defaultBuyIn"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague_competition_has_minimalAttendance():
    assert hasattr(pokerleague_Competition, "minimalAttendance")
    descriptor = None
    for klass in pokerleague_Competition.__mro__:
        if "minimalAttendance" in klass.__dict__:
            descriptor = klass.__dict__["minimalAttendance"]
            break
    assert isinstance(descriptor, property)



def test_pokerleague_tournament_is_not_abstract():
    assert not inspect.isabstract(pokerleague_Tournament)


def test_pokerleague_tournament_constructor_exists():
    assert callable(pokerleague_Tournament.__init__)


def test_pokerleague_tournament_constructor_args():
    sig = inspect.signature(pokerleague_Tournament.__init__)
    params = list(sig.parameters.keys())
    assert "maxPlayers" in params, "Missing parameter 'maxPlayers'"
    assert "defaultBuyIn" in params, "Missing parameter 'defaultBuyIn'"
    assert "minPlayers" in params, "Missing parameter 'minPlayers'"
    assert "tournamentAnnouncementLead" in params, "Missing parameter 'tournamentAnnouncementLead'"
    assert "tournamentStart" in params, "Missing parameter 'tournamentStart'"
    assert "tournamentEnd" in params, "Missing parameter 'tournamentEnd'"

def test_pokerleague_tournament_has_maxPlayers():
    assert hasattr(pokerleague_Tournament, "maxPlayers")
    descriptor = None
    for klass in pokerleague_Tournament.__mro__:
        if "maxPlayers" in klass.__dict__:
            descriptor = klass.__dict__["maxPlayers"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague_tournament_has_defaultBuyIn():
    assert hasattr(pokerleague_Tournament, "defaultBuyIn")
    descriptor = None
    for klass in pokerleague_Tournament.__mro__:
        if "defaultBuyIn" in klass.__dict__:
            descriptor = klass.__dict__["defaultBuyIn"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague_tournament_has_minPlayers():
    assert hasattr(pokerleague_Tournament, "minPlayers")
    descriptor = None
    for klass in pokerleague_Tournament.__mro__:
        if "minPlayers" in klass.__dict__:
            descriptor = klass.__dict__["minPlayers"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague_tournament_has_tournamentAnnouncementLead():
    assert hasattr(pokerleague_Tournament, "tournamentAnnouncementLead")
    descriptor = None
    for klass in pokerleague_Tournament.__mro__:
        if "tournamentAnnouncementLead" in klass.__dict__:
            descriptor = klass.__dict__["tournamentAnnouncementLead"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague_tournament_has_tournamentStart():
    assert hasattr(pokerleague_Tournament, "tournamentStart")
    descriptor = None
    for klass in pokerleague_Tournament.__mro__:
        if "tournamentStart" in klass.__dict__:
            descriptor = klass.__dict__["tournamentStart"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague_tournament_has_tournamentEnd():
    assert hasattr(pokerleague_Tournament, "tournamentEnd")
    descriptor = None
    for klass in pokerleague_Tournament.__mro__:
        if "tournamentEnd" in klass.__dict__:
            descriptor = klass.__dict__["tournamentEnd"]
            break
    assert isinstance(descriptor, property)



def test_pokerleague_prizemoneyruleset_is_not_abstract():
    assert not inspect.isabstract(pokerleague_PrizeMoneyRuleSet)


def test_pokerleague_prizemoneyruleset_constructor_exists():
    assert callable(pokerleague_PrizeMoneyRuleSet.__init__)


def test_pokerleague_prizemoneyruleset_constructor_args():
    sig = inspect.signature(pokerleague_PrizeMoneyRuleSet.__init__)
    params = list(sig.parameters.keys())



def test_identifiableentity_is_not_abstract():
    assert not inspect.isabstract(IdentifiableEntity)


def test_identifiableentity_constructor_exists():
    assert callable(IdentifiableEntity.__init__)


def test_identifiableentity_constructor_args():
    sig = inspect.signature(IdentifiableEntity.__init__)
    params = list(sig.parameters.keys())



def test_pokerleague_prizemoneyrule_is_not_abstract():
    assert not inspect.isabstract(pokerleague_PrizeMoneyRule)


def test_pokerleague_prizemoneyrule_constructor_exists():
    assert callable(pokerleague_PrizeMoneyRule.__init__)


def test_pokerleague_prizemoneyrule_constructor_args():
    sig = inspect.signature(pokerleague_PrizeMoneyRule.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfPlayers" in params, "Missing parameter 'numberOfPlayers'"

def test_pokerleague_prizemoneyrule_has_numberOfPlayers():
    assert hasattr(pokerleague_PrizeMoneyRule, "numberOfPlayers")
    descriptor = None
    for klass in pokerleague_PrizeMoneyRule.__mro__:
        if "numberOfPlayers" in klass.__dict__:
            descriptor = klass.__dict__["numberOfPlayers"]
            break
    assert isinstance(descriptor, property)



def test_pokerleague_player_is_not_abstract():
    assert not inspect.isabstract(pokerleague_Player)


def test_pokerleague_player_constructor_exists():
    assert callable(pokerleague_Player.__init__)


def test_pokerleague_player_constructor_args():
    sig = inspect.signature(pokerleague_Player.__init__)
    params = list(sig.parameters.keys())
    assert "active" in params, "Missing parameter 'active'"
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "emailAddress" in params, "Missing parameter 'emailAddress'"
    assert "nick" in params, "Missing parameter 'nick'"

def test_pokerleague_player_has_active():
    assert hasattr(pokerleague_Player, "active")
    descriptor = None
    for klass in pokerleague_Player.__mro__:
        if "active" in klass.__dict__:
            descriptor = klass.__dict__["active"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague_player_has_lastName():
    assert hasattr(pokerleague_Player, "lastName")
    descriptor = None
    for klass in pokerleague_Player.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague_player_has_firstName():
    assert hasattr(pokerleague_Player, "firstName")
    descriptor = None
    for klass in pokerleague_Player.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague_player_has_emailAddress():
    assert hasattr(pokerleague_Player, "emailAddress")
    descriptor = None
    for klass in pokerleague_Player.__mro__:
        if "emailAddress" in klass.__dict__:
            descriptor = klass.__dict__["emailAddress"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague_player_has_nick():
    assert hasattr(pokerleague_Player, "nick")
    descriptor = None
    for klass in pokerleague_Player.__mro__:
        if "nick" in klass.__dict__:
            descriptor = klass.__dict__["nick"]
            break
    assert isinstance(descriptor, property)



def test_pokerleague_game_is_not_abstract():
    assert not inspect.isabstract(pokerleague_Game)


def test_pokerleague_game_constructor_exists():
    assert callable(pokerleague_Game.__init__)


def test_pokerleague_game_constructor_args():
    sig = inspect.signature(pokerleague_Game.__init__)
    params = list(sig.parameters.keys())
    assert "buyIn" in params, "Missing parameter 'buyIn'"
    assert "ordinal" in params, "Missing parameter 'ordinal'"

def test_pokerleague_game_has_buyIn():
    assert hasattr(pokerleague_Game, "buyIn")
    descriptor = None
    for klass in pokerleague_Game.__mro__:
        if "buyIn" in klass.__dict__:
            descriptor = klass.__dict__["buyIn"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague_game_has_ordinal():
    assert hasattr(pokerleague_Game, "ordinal")
    descriptor = None
    for klass in pokerleague_Game.__mro__:
        if "ordinal" in klass.__dict__:
            descriptor = klass.__dict__["ordinal"]
            break
    assert isinstance(descriptor, property)



def test_pokerleague_invitation_is_not_abstract():
    assert not inspect.isabstract(pokerleague_Invitation)


def test_pokerleague_invitation_constructor_exists():
    assert callable(pokerleague_Invitation.__init__)


def test_pokerleague_invitation_constructor_args():
    sig = inspect.signature(pokerleague_Invitation.__init__)
    params = list(sig.parameters.keys())
    assert "reply" in params, "Missing parameter 'reply'"
    assert "ordinal" in params, "Missing parameter 'ordinal'"
    assert "uuid" in params, "Missing parameter 'uuid'"

def test_pokerleague_invitation_has_reply():
    assert hasattr(pokerleague_Invitation, "reply")
    descriptor = None
    for klass in pokerleague_Invitation.__mro__:
        if "reply" in klass.__dict__:
            descriptor = klass.__dict__["reply"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague_invitation_has_ordinal():
    assert hasattr(pokerleague_Invitation, "ordinal")
    descriptor = None
    for klass in pokerleague_Invitation.__mro__:
        if "ordinal" in klass.__dict__:
            descriptor = klass.__dict__["ordinal"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague_invitation_has_uuid():
    assert hasattr(pokerleague_Invitation, "uuid")
    descriptor = None
    for klass in pokerleague_Invitation.__mro__:
        if "uuid" in klass.__dict__:
            descriptor = klass.__dict__["uuid"]
            break
    assert isinstance(descriptor, property)



def test_pokerleague_invitationevent_is_not_abstract():
    assert not inspect.isabstract(pokerleague_InvitationEvent)


def test_pokerleague_invitationevent_constructor_exists():
    assert callable(pokerleague_InvitationEvent.__init__)


def test_pokerleague_invitationevent_constructor_args():
    sig = inspect.signature(pokerleague_InvitationEvent.__init__)
    params = list(sig.parameters.keys())
    assert "sent" in params, "Missing parameter 'sent'"
    assert "eventType" in params, "Missing parameter 'eventType'"
    assert "eventTime" in params, "Missing parameter 'eventTime'"

def test_pokerleague_invitationevent_has_sent():
    assert hasattr(pokerleague_InvitationEvent, "sent")
    descriptor = None
    for klass in pokerleague_InvitationEvent.__mro__:
        if "sent" in klass.__dict__:
            descriptor = klass.__dict__["sent"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague_invitationevent_has_eventType():
    assert hasattr(pokerleague_InvitationEvent, "eventType")
    descriptor = None
    for klass in pokerleague_InvitationEvent.__mro__:
        if "eventType" in klass.__dict__:
            descriptor = klass.__dict__["eventType"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague_invitationevent_has_eventTime():
    assert hasattr(pokerleague_InvitationEvent, "eventTime")
    descriptor = None
    for klass in pokerleague_InvitationEvent.__mro__:
        if "eventTime" in klass.__dict__:
            descriptor = klass.__dict__["eventTime"]
            break
    assert isinstance(descriptor, property)



def test_pokerleague_prizemoneyformula_is_not_abstract():
    assert not inspect.isabstract(pokerleague_PrizeMoneyFormula)


def test_pokerleague_prizemoneyformula_constructor_exists():
    assert callable(pokerleague_PrizeMoneyFormula.__init__)


def test_pokerleague_prizemoneyformula_constructor_args():
    sig = inspect.signature(pokerleague_PrizeMoneyFormula.__init__)
    params = list(sig.parameters.keys())
    assert "relativePrizeMoney" in params, "Missing parameter 'relativePrizeMoney'"
    assert "rank" in params, "Missing parameter 'rank'"

def test_pokerleague_prizemoneyformula_has_relativePrizeMoney():
    assert hasattr(pokerleague_PrizeMoneyFormula, "relativePrizeMoney")
    descriptor = None
    for klass in pokerleague_PrizeMoneyFormula.__mro__:
        if "relativePrizeMoney" in klass.__dict__:
            descriptor = klass.__dict__["relativePrizeMoney"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague_prizemoneyformula_has_rank():
    assert hasattr(pokerleague_PrizeMoneyFormula, "rank")
    descriptor = None
    for klass in pokerleague_PrizeMoneyFormula.__mro__:
        if "rank" in klass.__dict__:
            descriptor = klass.__dict__["rank"]
            break
    assert isinstance(descriptor, property)



def test_pokerleague_playeringame_is_not_abstract():
    assert not inspect.isabstract(pokerleague_PlayerInGame)


def test_pokerleague_playeringame_constructor_exists():
    assert callable(pokerleague_PlayerInGame.__init__)


def test_pokerleague_playeringame_constructor_args():
    sig = inspect.signature(pokerleague_PlayerInGame.__init__)
    params = list(sig.parameters.keys())
    assert "rank" in params, "Missing parameter 'rank'"

def test_pokerleague_playeringame_has_rank():
    assert hasattr(pokerleague_PlayerInGame, "rank")
    descriptor = None
    for klass in pokerleague_PlayerInGame.__mro__:
        if "rank" in klass.__dict__:
            descriptor = klass.__dict__["rank"]
            break
    assert isinstance(descriptor, property)



def test_pokerleague_describedentity_is_not_abstract():
    assert not inspect.isabstract(pokerleague_DescribedEntity)


def test_pokerleague_describedentity_constructor_exists():
    assert callable(pokerleague_DescribedEntity.__init__)


def test_pokerleague_describedentity_constructor_args():
    sig = inspect.signature(pokerleague_DescribedEntity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_pokerleague_describedentity_has_name():
    assert hasattr(pokerleague_DescribedEntity, "name")
    descriptor = None
    for klass in pokerleague_DescribedEntity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_pokerleague_describedentity_has_description():
    assert hasattr(pokerleague_DescribedEntity, "description")
    descriptor = None
    for klass in pokerleague_DescribedEntity.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_invitationreply_exists():
    # Check that the Enumeration exists
    assert InvitationReply is not None

def test_invitationreply_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InvitationReply]
    expected_literals = [
        "NO_REPLY",
        "REJECTED",
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
pokerleague_Settings_strategy = st.builds(
    pokerleague_Settings,
    id=
        st.integers(),
    defaultTimeZone=
        safe_text,
    adminPassword=
        safe_text
)
pokerleague_IdentifiableEntity_strategy = st.builds(
    pokerleague_IdentifiableEntity,
    id=
        st.integers(),
    obsolete=
        st.booleans(),
    proxy=
        st.booleans()
)
pokerleague_DataVersion_strategy = st.builds(
    pokerleague_DataVersion,
    currentVersion=
        safe_text,
    id=
        st.integers()
)
pokerleague_DataStructureVersion_strategy = st.builds(
    pokerleague_DataStructureVersion,
    id=
        st.integers(),
    currentVersion=
        safe_text
)
pokerleague_Serializable_strategy = st.builds(
    pokerleague_Serializable,
)
DescribedEntity_strategy = st.builds(
    DescribedEntity,
)
pokerleague_Competition_strategy = st.builds(
    pokerleague_Competition,
    defaultTournamentAnnouncementLead=
        st.integers(),
    defaultMinPlayers=
        st.integers(),
    startDate=
        st.dates(),
    defaultMaxPlayers=
        st.integers(),
    endDate=
        st.dates(),
    defaultBuyIn=
        st.integers(),
    minimalAttendance=
        st.integers()
)
pokerleague_Tournament_strategy = st.builds(
    pokerleague_Tournament,
    maxPlayers=
        st.integers(),
    defaultBuyIn=
        st.integers(),
    minPlayers=
        st.integers(),
    tournamentAnnouncementLead=
        st.integers(),
    tournamentStart=
        safe_text,
    tournamentEnd=
        safe_text
)
pokerleague_PrizeMoneyRuleSet_strategy = st.builds(
    pokerleague_PrizeMoneyRuleSet,
)
IdentifiableEntity_strategy = st.builds(
    IdentifiableEntity,
)
pokerleague_PrizeMoneyRule_strategy = st.builds(
    pokerleague_PrizeMoneyRule,
    numberOfPlayers=
        st.integers()
)
pokerleague_Player_strategy = st.builds(
    pokerleague_Player,
    active=
        st.booleans(),
    lastName=
        safe_text,
    firstName=
        safe_text,
    emailAddress=
        safe_text,
    nick=
        safe_text
)
pokerleague_Game_strategy = st.builds(
    pokerleague_Game,
    buyIn=
        st.integers(),
    ordinal=
        st.integers()
)
pokerleague_Invitation_strategy = st.builds(
    pokerleague_Invitation,
    reply=
        safe_text,
    ordinal=
        st.integers(),
    uuid=
        safe_text
)
pokerleague_InvitationEvent_strategy = st.builds(
    pokerleague_InvitationEvent,
    sent=
        st.booleans(),
    eventType=
        safe_text,
    eventTime=
        safe_text
)
pokerleague_PrizeMoneyFormula_strategy = st.builds(
    pokerleague_PrizeMoneyFormula,
    relativePrizeMoney=
        st.integers(),
    rank=
        st.integers()
)
pokerleague_PlayerInGame_strategy = st.builds(
    pokerleague_PlayerInGame,
    rank=
        st.integers()
)
pokerleague_DescribedEntity_strategy = st.builds(
    pokerleague_DescribedEntity,
    name=
        safe_text,
    description=
        safe_text
)

@given(instance=Serializable_strategy)
@settings(max_examples=50)
def test_serializable_instantiation(instance):
    assert isinstance(instance, Serializable)

@given(instance=pokerleague_Settings_strategy)
@settings(max_examples=50)
def test_pokerleague_settings_instantiation(instance):
    assert isinstance(instance, pokerleague_Settings)



@given(instance=pokerleague_Settings_strategy)
def test_pokerleague_settings_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=pokerleague_Settings_strategy)
def test_pokerleague_settings_defaultTimeZone_setter(instance):
    original = instance.defaultTimeZone
    instance.defaultTimeZone = original
    assert instance.defaultTimeZone == original



@given(instance=pokerleague_Settings_strategy)
def test_pokerleague_settings_adminPassword_setter(instance):
    original = instance.adminPassword
    instance.adminPassword = original
    assert instance.adminPassword == original

@given(instance=pokerleague_IdentifiableEntity_strategy)
@settings(max_examples=50)
def test_pokerleague_identifiableentity_instantiation(instance):
    assert isinstance(instance, pokerleague_IdentifiableEntity)



@given(instance=pokerleague_IdentifiableEntity_strategy)
def test_pokerleague_identifiableentity_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=pokerleague_IdentifiableEntity_strategy)
def test_pokerleague_identifiableentity_obsolete_setter(instance):
    original = instance.obsolete
    instance.obsolete = original
    assert instance.obsolete == original



@given(instance=pokerleague_IdentifiableEntity_strategy)
def test_pokerleague_identifiableentity_proxy_setter(instance):
    original = instance.proxy
    instance.proxy = original
    assert instance.proxy == original

@given(instance=pokerleague_DataVersion_strategy)
@settings(max_examples=50)
def test_pokerleague_dataversion_instantiation(instance):
    assert isinstance(instance, pokerleague_DataVersion)



@given(instance=pokerleague_DataVersion_strategy)
def test_pokerleague_dataversion_currentVersion_setter(instance):
    original = instance.currentVersion
    instance.currentVersion = original
    assert instance.currentVersion == original



@given(instance=pokerleague_DataVersion_strategy)
def test_pokerleague_dataversion_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=pokerleague_DataStructureVersion_strategy)
@settings(max_examples=50)
def test_pokerleague_datastructureversion_instantiation(instance):
    assert isinstance(instance, pokerleague_DataStructureVersion)



@given(instance=pokerleague_DataStructureVersion_strategy)
def test_pokerleague_datastructureversion_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=pokerleague_DataStructureVersion_strategy)
def test_pokerleague_datastructureversion_currentVersion_setter(instance):
    original = instance.currentVersion
    instance.currentVersion = original
    assert instance.currentVersion == original

@given(instance=pokerleague_Serializable_strategy)
@settings(max_examples=50)
def test_pokerleague_serializable_instantiation(instance):
    assert isinstance(instance, pokerleague_Serializable)

@given(instance=DescribedEntity_strategy)
@settings(max_examples=50)
def test_describedentity_instantiation(instance):
    assert isinstance(instance, DescribedEntity)

@given(instance=pokerleague_Competition_strategy)
@settings(max_examples=50)
def test_pokerleague_competition_instantiation(instance):
    assert isinstance(instance, pokerleague_Competition)



@given(instance=pokerleague_Competition_strategy)
def test_pokerleague_competition_defaultTournamentAnnouncementLead_setter(instance):
    original = instance.defaultTournamentAnnouncementLead
    instance.defaultTournamentAnnouncementLead = original
    assert instance.defaultTournamentAnnouncementLead == original



@given(instance=pokerleague_Competition_strategy)
def test_pokerleague_competition_defaultMinPlayers_setter(instance):
    original = instance.defaultMinPlayers
    instance.defaultMinPlayers = original
    assert instance.defaultMinPlayers == original



@given(instance=pokerleague_Competition_strategy)
def test_pokerleague_competition_startDate_setter(instance):
    original = instance.startDate
    instance.startDate = original
    assert instance.startDate == original



@given(instance=pokerleague_Competition_strategy)
def test_pokerleague_competition_defaultMaxPlayers_setter(instance):
    original = instance.defaultMaxPlayers
    instance.defaultMaxPlayers = original
    assert instance.defaultMaxPlayers == original



@given(instance=pokerleague_Competition_strategy)
def test_pokerleague_competition_endDate_setter(instance):
    original = instance.endDate
    instance.endDate = original
    assert instance.endDate == original



@given(instance=pokerleague_Competition_strategy)
def test_pokerleague_competition_defaultBuyIn_setter(instance):
    original = instance.defaultBuyIn
    instance.defaultBuyIn = original
    assert instance.defaultBuyIn == original



@given(instance=pokerleague_Competition_strategy)
def test_pokerleague_competition_minimalAttendance_setter(instance):
    original = instance.minimalAttendance
    instance.minimalAttendance = original
    assert instance.minimalAttendance == original

@given(instance=pokerleague_Tournament_strategy)
@settings(max_examples=50)
def test_pokerleague_tournament_instantiation(instance):
    assert isinstance(instance, pokerleague_Tournament)



@given(instance=pokerleague_Tournament_strategy)
def test_pokerleague_tournament_maxPlayers_setter(instance):
    original = instance.maxPlayers
    instance.maxPlayers = original
    assert instance.maxPlayers == original



@given(instance=pokerleague_Tournament_strategy)
def test_pokerleague_tournament_defaultBuyIn_setter(instance):
    original = instance.defaultBuyIn
    instance.defaultBuyIn = original
    assert instance.defaultBuyIn == original



@given(instance=pokerleague_Tournament_strategy)
def test_pokerleague_tournament_minPlayers_setter(instance):
    original = instance.minPlayers
    instance.minPlayers = original
    assert instance.minPlayers == original



@given(instance=pokerleague_Tournament_strategy)
def test_pokerleague_tournament_tournamentAnnouncementLead_setter(instance):
    original = instance.tournamentAnnouncementLead
    instance.tournamentAnnouncementLead = original
    assert instance.tournamentAnnouncementLead == original



@given(instance=pokerleague_Tournament_strategy)
def test_pokerleague_tournament_tournamentStart_setter(instance):
    original = instance.tournamentStart
    instance.tournamentStart = original
    assert instance.tournamentStart == original



@given(instance=pokerleague_Tournament_strategy)
def test_pokerleague_tournament_tournamentEnd_setter(instance):
    original = instance.tournamentEnd
    instance.tournamentEnd = original
    assert instance.tournamentEnd == original

@given(instance=pokerleague_PrizeMoneyRuleSet_strategy)
@settings(max_examples=50)
def test_pokerleague_prizemoneyruleset_instantiation(instance):
    assert isinstance(instance, pokerleague_PrizeMoneyRuleSet)

@given(instance=IdentifiableEntity_strategy)
@settings(max_examples=50)
def test_identifiableentity_instantiation(instance):
    assert isinstance(instance, IdentifiableEntity)

@given(instance=pokerleague_PrizeMoneyRule_strategy)
@settings(max_examples=50)
def test_pokerleague_prizemoneyrule_instantiation(instance):
    assert isinstance(instance, pokerleague_PrizeMoneyRule)



@given(instance=pokerleague_PrizeMoneyRule_strategy)
def test_pokerleague_prizemoneyrule_numberOfPlayers_setter(instance):
    original = instance.numberOfPlayers
    instance.numberOfPlayers = original
    assert instance.numberOfPlayers == original

@given(instance=pokerleague_Player_strategy)
@settings(max_examples=50)
def test_pokerleague_player_instantiation(instance):
    assert isinstance(instance, pokerleague_Player)



@given(instance=pokerleague_Player_strategy)
def test_pokerleague_player_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original



@given(instance=pokerleague_Player_strategy)
def test_pokerleague_player_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



@given(instance=pokerleague_Player_strategy)
def test_pokerleague_player_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=pokerleague_Player_strategy)
def test_pokerleague_player_emailAddress_setter(instance):
    original = instance.emailAddress
    instance.emailAddress = original
    assert instance.emailAddress == original



@given(instance=pokerleague_Player_strategy)
def test_pokerleague_player_nick_setter(instance):
    original = instance.nick
    instance.nick = original
    assert instance.nick == original

@given(instance=pokerleague_Game_strategy)
@settings(max_examples=50)
def test_pokerleague_game_instantiation(instance):
    assert isinstance(instance, pokerleague_Game)



@given(instance=pokerleague_Game_strategy)
def test_pokerleague_game_buyIn_setter(instance):
    original = instance.buyIn
    instance.buyIn = original
    assert instance.buyIn == original



@given(instance=pokerleague_Game_strategy)
def test_pokerleague_game_ordinal_setter(instance):
    original = instance.ordinal
    instance.ordinal = original
    assert instance.ordinal == original

@given(instance=pokerleague_Invitation_strategy)
@settings(max_examples=50)
def test_pokerleague_invitation_instantiation(instance):
    assert isinstance(instance, pokerleague_Invitation)



@given(instance=pokerleague_Invitation_strategy)
def test_pokerleague_invitation_reply_setter(instance):
    original = instance.reply
    instance.reply = original
    assert instance.reply == original



@given(instance=pokerleague_Invitation_strategy)
def test_pokerleague_invitation_ordinal_setter(instance):
    original = instance.ordinal
    instance.ordinal = original
    assert instance.ordinal == original



@given(instance=pokerleague_Invitation_strategy)
def test_pokerleague_invitation_uuid_setter(instance):
    original = instance.uuid
    instance.uuid = original
    assert instance.uuid == original

@given(instance=pokerleague_InvitationEvent_strategy)
@settings(max_examples=50)
def test_pokerleague_invitationevent_instantiation(instance):
    assert isinstance(instance, pokerleague_InvitationEvent)



@given(instance=pokerleague_InvitationEvent_strategy)
def test_pokerleague_invitationevent_sent_setter(instance):
    original = instance.sent
    instance.sent = original
    assert instance.sent == original



@given(instance=pokerleague_InvitationEvent_strategy)
def test_pokerleague_invitationevent_eventType_setter(instance):
    original = instance.eventType
    instance.eventType = original
    assert instance.eventType == original



@given(instance=pokerleague_InvitationEvent_strategy)
def test_pokerleague_invitationevent_eventTime_setter(instance):
    original = instance.eventTime
    instance.eventTime = original
    assert instance.eventTime == original

@given(instance=pokerleague_PrizeMoneyFormula_strategy)
@settings(max_examples=50)
def test_pokerleague_prizemoneyformula_instantiation(instance):
    assert isinstance(instance, pokerleague_PrizeMoneyFormula)



@given(instance=pokerleague_PrizeMoneyFormula_strategy)
def test_pokerleague_prizemoneyformula_relativePrizeMoney_setter(instance):
    original = instance.relativePrizeMoney
    instance.relativePrizeMoney = original
    assert instance.relativePrizeMoney == original



@given(instance=pokerleague_PrizeMoneyFormula_strategy)
def test_pokerleague_prizemoneyformula_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original

@given(instance=pokerleague_PlayerInGame_strategy)
@settings(max_examples=50)
def test_pokerleague_playeringame_instantiation(instance):
    assert isinstance(instance, pokerleague_PlayerInGame)



@given(instance=pokerleague_PlayerInGame_strategy)
def test_pokerleague_playeringame_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original

@given(instance=pokerleague_DescribedEntity_strategy)
@settings(max_examples=50)
def test_pokerleague_describedentity_instantiation(instance):
    assert isinstance(instance, pokerleague_DescribedEntity)



@given(instance=pokerleague_DescribedEntity_strategy)
def test_pokerleague_describedentity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=pokerleague_DescribedEntity_strategy)
def test_pokerleague_describedentity_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original
