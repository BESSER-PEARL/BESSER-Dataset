import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    BZ_BZEvent,
    BZ_BZComment,
    BZ_BZIssue,
    BZ_BZComponent,
    BZ_BZProduct,
    BZ_BZRepo,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bz_bzevent_is_not_abstract():
    assert not inspect.isabstract(BZ_BZEvent)


def test_bz_bzevent_constructor_exists():
    assert callable(BZ_BZEvent.__init__)


def test_bz_bzevent_constructor_args():
    sig = inspect.signature(BZ_BZEvent.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"
    assert "newValue" in params, "Missing parameter 'newValue'"
    assert "author" in params, "Missing parameter 'author'"
    assert "date" in params, "Missing parameter 'date'"
    assert "issueId" in params, "Missing parameter 'issueId'"
    assert "oldValue" in params, "Missing parameter 'oldValue'"

def test_bz_bzevent_has_field():
    assert hasattr(BZ_BZEvent, "field")
    descriptor = None
    for klass in BZ_BZEvent.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)

def test_bz_bzevent_has_newValue():
    assert hasattr(BZ_BZEvent, "newValue")
    descriptor = None
    for klass in BZ_BZEvent.__mro__:
        if "newValue" in klass.__dict__:
            descriptor = klass.__dict__["newValue"]
            break
    assert isinstance(descriptor, property)

def test_bz_bzevent_has_author():
    assert hasattr(BZ_BZEvent, "author")
    descriptor = None
    for klass in BZ_BZEvent.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_bz_bzevent_has_date():
    assert hasattr(BZ_BZEvent, "date")
    descriptor = None
    for klass in BZ_BZEvent.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_bz_bzevent_has_issueId():
    assert hasattr(BZ_BZEvent, "issueId")
    descriptor = None
    for klass in BZ_BZEvent.__mro__:
        if "issueId" in klass.__dict__:
            descriptor = klass.__dict__["issueId"]
            break
    assert isinstance(descriptor, property)

def test_bz_bzevent_has_oldValue():
    assert hasattr(BZ_BZEvent, "oldValue")
    descriptor = None
    for klass in BZ_BZEvent.__mro__:
        if "oldValue" in klass.__dict__:
            descriptor = klass.__dict__["oldValue"]
            break
    assert isinstance(descriptor, property)



def test_bz_bzcomment_is_not_abstract():
    assert not inspect.isabstract(BZ_BZComment)


def test_bz_bzcomment_constructor_exists():
    assert callable(BZ_BZComment.__init__)


def test_bz_bzcomment_constructor_args():
    sig = inspect.signature(BZ_BZComment.__init__)
    params = list(sig.parameters.keys())
    assert "commentHTML" in params, "Missing parameter 'commentHTML'"
    assert "commentTime" in params, "Missing parameter 'commentTime'"
    assert "commentText" in params, "Missing parameter 'commentText'"
    assert "issueId" in params, "Missing parameter 'issueId'"
    assert "commentId" in params, "Missing parameter 'commentId'"
    assert "commentAuthor" in params, "Missing parameter 'commentAuthor'"

def test_bz_bzcomment_has_commentHTML():
    assert hasattr(BZ_BZComment, "commentHTML")
    descriptor = None
    for klass in BZ_BZComment.__mro__:
        if "commentHTML" in klass.__dict__:
            descriptor = klass.__dict__["commentHTML"]
            break
    assert isinstance(descriptor, property)

def test_bz_bzcomment_has_commentTime():
    assert hasattr(BZ_BZComment, "commentTime")
    descriptor = None
    for klass in BZ_BZComment.__mro__:
        if "commentTime" in klass.__dict__:
            descriptor = klass.__dict__["commentTime"]
            break
    assert isinstance(descriptor, property)

def test_bz_bzcomment_has_commentText():
    assert hasattr(BZ_BZComment, "commentText")
    descriptor = None
    for klass in BZ_BZComment.__mro__:
        if "commentText" in klass.__dict__:
            descriptor = klass.__dict__["commentText"]
            break
    assert isinstance(descriptor, property)

def test_bz_bzcomment_has_issueId():
    assert hasattr(BZ_BZComment, "issueId")
    descriptor = None
    for klass in BZ_BZComment.__mro__:
        if "issueId" in klass.__dict__:
            descriptor = klass.__dict__["issueId"]
            break
    assert isinstance(descriptor, property)

def test_bz_bzcomment_has_commentId():
    assert hasattr(BZ_BZComment, "commentId")
    descriptor = None
    for klass in BZ_BZComment.__mro__:
        if "commentId" in klass.__dict__:
            descriptor = klass.__dict__["commentId"]
            break
    assert isinstance(descriptor, property)

def test_bz_bzcomment_has_commentAuthor():
    assert hasattr(BZ_BZComment, "commentAuthor")
    descriptor = None
    for klass in BZ_BZComment.__mro__:
        if "commentAuthor" in klass.__dict__:
            descriptor = klass.__dict__["commentAuthor"]
            break
    assert isinstance(descriptor, property)



def test_bz_bzissue_is_not_abstract():
    assert not inspect.isabstract(BZ_BZIssue)


def test_bz_bzissue_constructor_exists():
    assert callable(BZ_BZIssue.__init__)


def test_bz_bzissue_constructor_args():
    sig = inspect.signature(BZ_BZIssue.__init__)
    params = list(sig.parameters.keys())
    assert "seeAlso" in params, "Missing parameter 'seeAlso'"
    assert "platform" in params, "Missing parameter 'platform'"
    assert "dependsOn" in params, "Missing parameter 'dependsOn'"
    assert "lastModifiedOn" in params, "Missing parameter 'lastModifiedOn'"
    assert "issueId" in params, "Missing parameter 'issueId'"
    assert "latestCommit" in params, "Missing parameter 'latestCommit'"
    assert "referenceURL" in params, "Missing parameter 'referenceURL'"
    assert "status" in params, "Missing parameter 'status'"
    assert "reportedBy" in params, "Missing parameter 'reportedBy'"
    assert "versionFixedIn" in params, "Missing parameter 'versionFixedIn'"
    assert "issueURL" in params, "Missing parameter 'issueURL'"
    assert "assignedTo" in params, "Missing parameter 'assignedTo'"
    assert "classification" in params, "Missing parameter 'classification'"
    assert "reportedOn" in params, "Missing parameter 'reportedOn'"
    assert "milestone" in params, "Missing parameter 'milestone'"
    assert "issueTitle" in params, "Missing parameter 'issueTitle'"
    assert "ccList" in params, "Missing parameter 'ccList'"
    assert "blocks" in params, "Missing parameter 'blocks'"
    assert "importance" in params, "Missing parameter 'importance'"
    assert "productName" in params, "Missing parameter 'productName'"
    assert "version" in params, "Missing parameter 'version'"
    assert "reportedByUsername" in params, "Missing parameter 'reportedByUsername'"
    assert "keywords" in params, "Missing parameter 'keywords'"
    assert "componentName" in params, "Missing parameter 'componentName'"

def test_bz_bzissue_has_seeAlso():
    assert hasattr(BZ_BZIssue, "seeAlso")
    descriptor = None
    for klass in BZ_BZIssue.__mro__:
        if "seeAlso" in klass.__dict__:
            descriptor = klass.__dict__["seeAlso"]
            break
    assert isinstance(descriptor, property)

def test_bz_bzissue_has_platform():
    assert hasattr(BZ_BZIssue, "platform")
    descriptor = None
    for klass in BZ_BZIssue.__mro__:
        if "platform" in klass.__dict__:
            descriptor = klass.__dict__["platform"]
            break
    assert isinstance(descriptor, property)

def test_bz_bzissue_has_dependsOn():
    assert hasattr(BZ_BZIssue, "dependsOn")
    descriptor = None
    for klass in BZ_BZIssue.__mro__:
        if "dependsOn" in klass.__dict__:
            descriptor = klass.__dict__["dependsOn"]
            break
    assert isinstance(descriptor, property)

def test_bz_bzissue_has_lastModifiedOn():
    assert hasattr(BZ_BZIssue, "lastModifiedOn")
    descriptor = None
    for klass in BZ_BZIssue.__mro__:
        if "lastModifiedOn" in klass.__dict__:
            descriptor = klass.__dict__["lastModifiedOn"]
            break
    assert isinstance(descriptor, property)

def test_bz_bzissue_has_issueId():
    assert hasattr(BZ_BZIssue, "issueId")
    descriptor = None
    for klass in BZ_BZIssue.__mro__:
        if "issueId" in klass.__dict__:
            descriptor = klass.__dict__["issueId"]
            break
    assert isinstance(descriptor, property)

def test_bz_bzissue_has_latestCommit():
    assert hasattr(BZ_BZIssue, "latestCommit")
    descriptor = None
    for klass in BZ_BZIssue.__mro__:
        if "latestCommit" in klass.__dict__:
            descriptor = klass.__dict__["latestCommit"]
            break
    assert isinstance(descriptor, property)

def test_bz_bzissue_has_referenceURL():
    assert hasattr(BZ_BZIssue, "referenceURL")
    descriptor = None
    for klass in BZ_BZIssue.__mro__:
        if "referenceURL" in klass.__dict__:
            descriptor = klass.__dict__["referenceURL"]
            break
    assert isinstance(descriptor, property)

def test_bz_bzissue_has_status():
    assert hasattr(BZ_BZIssue, "status")
    descriptor = None
    for klass in BZ_BZIssue.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_bz_bzissue_has_reportedBy():
    assert hasattr(BZ_BZIssue, "reportedBy")
    descriptor = None
    for klass in BZ_BZIssue.__mro__:
        if "reportedBy" in klass.__dict__:
            descriptor = klass.__dict__["reportedBy"]
            break
    assert isinstance(descriptor, property)

def test_bz_bzissue_has_versionFixedIn():
    assert hasattr(BZ_BZIssue, "versionFixedIn")
    descriptor = None
    for klass in BZ_BZIssue.__mro__:
        if "versionFixedIn" in klass.__dict__:
            descriptor = klass.__dict__["versionFixedIn"]
            break
    assert isinstance(descriptor, property)

def test_bz_bzissue_has_issueURL():
    assert hasattr(BZ_BZIssue, "issueURL")
    descriptor = None
    for klass in BZ_BZIssue.__mro__:
        if "issueURL" in klass.__dict__:
            descriptor = klass.__dict__["issueURL"]
            break
    assert isinstance(descriptor, property)

def test_bz_bzissue_has_assignedTo():
    assert hasattr(BZ_BZIssue, "assignedTo")
    descriptor = None
    for klass in BZ_BZIssue.__mro__:
        if "assignedTo" in klass.__dict__:
            descriptor = klass.__dict__["assignedTo"]
            break
    assert isinstance(descriptor, property)

def test_bz_bzissue_has_classification():
    assert hasattr(BZ_BZIssue, "classification")
    descriptor = None
    for klass in BZ_BZIssue.__mro__:
        if "classification" in klass.__dict__:
            descriptor = klass.__dict__["classification"]
            break
    assert isinstance(descriptor, property)

def test_bz_bzissue_has_reportedOn():
    assert hasattr(BZ_BZIssue, "reportedOn")
    descriptor = None
    for klass in BZ_BZIssue.__mro__:
        if "reportedOn" in klass.__dict__:
            descriptor = klass.__dict__["reportedOn"]
            break
    assert isinstance(descriptor, property)

def test_bz_bzissue_has_milestone():
    assert hasattr(BZ_BZIssue, "milestone")
    descriptor = None
    for klass in BZ_BZIssue.__mro__:
        if "milestone" in klass.__dict__:
            descriptor = klass.__dict__["milestone"]
            break
    assert isinstance(descriptor, property)

def test_bz_bzissue_has_issueTitle():
    assert hasattr(BZ_BZIssue, "issueTitle")
    descriptor = None
    for klass in BZ_BZIssue.__mro__:
        if "issueTitle" in klass.__dict__:
            descriptor = klass.__dict__["issueTitle"]
            break
    assert isinstance(descriptor, property)

def test_bz_bzissue_has_ccList():
    assert hasattr(BZ_BZIssue, "ccList")
    descriptor = None
    for klass in BZ_BZIssue.__mro__:
        if "ccList" in klass.__dict__:
            descriptor = klass.__dict__["ccList"]
            break
    assert isinstance(descriptor, property)

def test_bz_bzissue_has_blocks():
    assert hasattr(BZ_BZIssue, "blocks")
    descriptor = None
    for klass in BZ_BZIssue.__mro__:
        if "blocks" in klass.__dict__:
            descriptor = klass.__dict__["blocks"]
            break
    assert isinstance(descriptor, property)

def test_bz_bzissue_has_importance():
    assert hasattr(BZ_BZIssue, "importance")
    descriptor = None
    for klass in BZ_BZIssue.__mro__:
        if "importance" in klass.__dict__:
            descriptor = klass.__dict__["importance"]
            break
    assert isinstance(descriptor, property)

def test_bz_bzissue_has_productName():
    assert hasattr(BZ_BZIssue, "productName")
    descriptor = None
    for klass in BZ_BZIssue.__mro__:
        if "productName" in klass.__dict__:
            descriptor = klass.__dict__["productName"]
            break
    assert isinstance(descriptor, property)

def test_bz_bzissue_has_version():
    assert hasattr(BZ_BZIssue, "version")
    descriptor = None
    for klass in BZ_BZIssue.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_bz_bzissue_has_reportedByUsername():
    assert hasattr(BZ_BZIssue, "reportedByUsername")
    descriptor = None
    for klass in BZ_BZIssue.__mro__:
        if "reportedByUsername" in klass.__dict__:
            descriptor = klass.__dict__["reportedByUsername"]
            break
    assert isinstance(descriptor, property)

def test_bz_bzissue_has_keywords():
    assert hasattr(BZ_BZIssue, "keywords")
    descriptor = None
    for klass in BZ_BZIssue.__mro__:
        if "keywords" in klass.__dict__:
            descriptor = klass.__dict__["keywords"]
            break
    assert isinstance(descriptor, property)

def test_bz_bzissue_has_componentName():
    assert hasattr(BZ_BZIssue, "componentName")
    descriptor = None
    for klass in BZ_BZIssue.__mro__:
        if "componentName" in klass.__dict__:
            descriptor = klass.__dict__["componentName"]
            break
    assert isinstance(descriptor, property)



def test_bz_bzcomponent_is_not_abstract():
    assert not inspect.isabstract(BZ_BZComponent)


def test_bz_bzcomponent_constructor_exists():
    assert callable(BZ_BZComponent.__init__)


def test_bz_bzcomponent_constructor_args():
    sig = inspect.signature(BZ_BZComponent.__init__)
    params = list(sig.parameters.keys())
    assert "componentURL" in params, "Missing parameter 'componentURL'"
    assert "componentDescription" in params, "Missing parameter 'componentDescription'"
    assert "defaultAssignee" in params, "Missing parameter 'defaultAssignee'"
    assert "componentId" in params, "Missing parameter 'componentId'"

def test_bz_bzcomponent_has_componentURL():
    assert hasattr(BZ_BZComponent, "componentURL")
    descriptor = None
    for klass in BZ_BZComponent.__mro__:
        if "componentURL" in klass.__dict__:
            descriptor = klass.__dict__["componentURL"]
            break
    assert isinstance(descriptor, property)

def test_bz_bzcomponent_has_componentDescription():
    assert hasattr(BZ_BZComponent, "componentDescription")
    descriptor = None
    for klass in BZ_BZComponent.__mro__:
        if "componentDescription" in klass.__dict__:
            descriptor = klass.__dict__["componentDescription"]
            break
    assert isinstance(descriptor, property)

def test_bz_bzcomponent_has_defaultAssignee():
    assert hasattr(BZ_BZComponent, "defaultAssignee")
    descriptor = None
    for klass in BZ_BZComponent.__mro__:
        if "defaultAssignee" in klass.__dict__:
            descriptor = klass.__dict__["defaultAssignee"]
            break
    assert isinstance(descriptor, property)

def test_bz_bzcomponent_has_componentId():
    assert hasattr(BZ_BZComponent, "componentId")
    descriptor = None
    for klass in BZ_BZComponent.__mro__:
        if "componentId" in klass.__dict__:
            descriptor = klass.__dict__["componentId"]
            break
    assert isinstance(descriptor, property)



def test_bz_bzproduct_is_not_abstract():
    assert not inspect.isabstract(BZ_BZProduct)


def test_bz_bzproduct_constructor_exists():
    assert callable(BZ_BZProduct.__init__)


def test_bz_bzproduct_constructor_args():
    sig = inspect.signature(BZ_BZProduct.__init__)
    params = list(sig.parameters.keys())
    assert "productDescription" in params, "Missing parameter 'productDescription'"
    assert "productId" in params, "Missing parameter 'productId'"
    assert "productURL" in params, "Missing parameter 'productURL'"

def test_bz_bzproduct_has_productDescription():
    assert hasattr(BZ_BZProduct, "productDescription")
    descriptor = None
    for klass in BZ_BZProduct.__mro__:
        if "productDescription" in klass.__dict__:
            descriptor = klass.__dict__["productDescription"]
            break
    assert isinstance(descriptor, property)

def test_bz_bzproduct_has_productId():
    assert hasattr(BZ_BZProduct, "productId")
    descriptor = None
    for klass in BZ_BZProduct.__mro__:
        if "productId" in klass.__dict__:
            descriptor = klass.__dict__["productId"]
            break
    assert isinstance(descriptor, property)

def test_bz_bzproduct_has_productURL():
    assert hasattr(BZ_BZProduct, "productURL")
    descriptor = None
    for klass in BZ_BZProduct.__mro__:
        if "productURL" in klass.__dict__:
            descriptor = klass.__dict__["productURL"]
            break
    assert isinstance(descriptor, property)



def test_bz_bzrepo_is_not_abstract():
    assert not inspect.isabstract(BZ_BZRepo)


def test_bz_bzrepo_constructor_exists():
    assert callable(BZ_BZRepo.__init__)


def test_bz_bzrepo_constructor_args():
    sig = inspect.signature(BZ_BZRepo.__init__)
    params = list(sig.parameters.keys())
    assert "repoURL" in params, "Missing parameter 'repoURL'"

def test_bz_bzrepo_has_repoURL():
    assert hasattr(BZ_BZRepo, "repoURL")
    descriptor = None
    for klass in BZ_BZRepo.__mro__:
        if "repoURL" in klass.__dict__:
            descriptor = klass.__dict__["repoURL"]
            break
    assert isinstance(descriptor, property)


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
BZ_BZEvent_strategy = st.builds(
    BZ_BZEvent,
    field=
        safe_text,
    newValue=
        safe_text,
    author=
        safe_text,
    date=
        st.dates(),
    issueId=
        st.integers(),
    oldValue=
        safe_text
)
BZ_BZComment_strategy = st.builds(
    BZ_BZComment,
    commentHTML=
        safe_text,
    commentTime=
        st.dates(),
    commentText=
        safe_text,
    issueId=
        st.integers(),
    commentId=
        safe_text,
    commentAuthor=
        safe_text
)
BZ_BZIssue_strategy = st.builds(
    BZ_BZIssue,
    seeAlso=
        safe_text,
    platform=
        safe_text,
    dependsOn=
        safe_text,
    lastModifiedOn=
        st.dates(),
    issueId=
        st.integers(),
    latestCommit=
        safe_text,
    referenceURL=
        safe_text,
    status=
        safe_text,
    reportedBy=
        safe_text,
    versionFixedIn=
        safe_text,
    issueURL=
        safe_text,
    assignedTo=
        safe_text,
    classification=
        safe_text,
    reportedOn=
        st.dates(),
    milestone=
        safe_text,
    issueTitle=
        safe_text,
    ccList=
        safe_text,
    blocks=
        safe_text,
    importance=
        safe_text,
    productName=
        safe_text,
    version=
        safe_text,
    reportedByUsername=
        safe_text,
    keywords=
        safe_text,
    componentName=
        safe_text
)
BZ_BZComponent_strategy = st.builds(
    BZ_BZComponent,
    componentURL=
        safe_text,
    componentDescription=
        safe_text,
    defaultAssignee=
        safe_text,
    componentId=
        safe_text
)
BZ_BZProduct_strategy = st.builds(
    BZ_BZProduct,
    productDescription=
        safe_text,
    productId=
        safe_text,
    productURL=
        safe_text
)
BZ_BZRepo_strategy = st.builds(
    BZ_BZRepo,
    repoURL=
        safe_text
)

@given(instance=BZ_BZEvent_strategy)
@settings(max_examples=50)
def test_bz_bzevent_instantiation(instance):
    assert isinstance(instance, BZ_BZEvent)



@given(instance=BZ_BZEvent_strategy)
def test_bz_bzevent_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original



@given(instance=BZ_BZEvent_strategy)
def test_bz_bzevent_newValue_setter(instance):
    original = instance.newValue
    instance.newValue = original
    assert instance.newValue == original



@given(instance=BZ_BZEvent_strategy)
def test_bz_bzevent_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=BZ_BZEvent_strategy)
def test_bz_bzevent_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=BZ_BZEvent_strategy)
def test_bz_bzevent_issueId_setter(instance):
    original = instance.issueId
    instance.issueId = original
    assert instance.issueId == original



@given(instance=BZ_BZEvent_strategy)
def test_bz_bzevent_oldValue_setter(instance):
    original = instance.oldValue
    instance.oldValue = original
    assert instance.oldValue == original

@given(instance=BZ_BZComment_strategy)
@settings(max_examples=50)
def test_bz_bzcomment_instantiation(instance):
    assert isinstance(instance, BZ_BZComment)



@given(instance=BZ_BZComment_strategy)
def test_bz_bzcomment_commentHTML_setter(instance):
    original = instance.commentHTML
    instance.commentHTML = original
    assert instance.commentHTML == original



@given(instance=BZ_BZComment_strategy)
def test_bz_bzcomment_commentTime_setter(instance):
    original = instance.commentTime
    instance.commentTime = original
    assert instance.commentTime == original



@given(instance=BZ_BZComment_strategy)
def test_bz_bzcomment_commentText_setter(instance):
    original = instance.commentText
    instance.commentText = original
    assert instance.commentText == original



@given(instance=BZ_BZComment_strategy)
def test_bz_bzcomment_issueId_setter(instance):
    original = instance.issueId
    instance.issueId = original
    assert instance.issueId == original



@given(instance=BZ_BZComment_strategy)
def test_bz_bzcomment_commentId_setter(instance):
    original = instance.commentId
    instance.commentId = original
    assert instance.commentId == original



@given(instance=BZ_BZComment_strategy)
def test_bz_bzcomment_commentAuthor_setter(instance):
    original = instance.commentAuthor
    instance.commentAuthor = original
    assert instance.commentAuthor == original

@given(instance=BZ_BZIssue_strategy)
@settings(max_examples=50)
def test_bz_bzissue_instantiation(instance):
    assert isinstance(instance, BZ_BZIssue)



@given(instance=BZ_BZIssue_strategy)
def test_bz_bzissue_seeAlso_setter(instance):
    original = instance.seeAlso
    instance.seeAlso = original
    assert instance.seeAlso == original



@given(instance=BZ_BZIssue_strategy)
def test_bz_bzissue_platform_setter(instance):
    original = instance.platform
    instance.platform = original
    assert instance.platform == original



@given(instance=BZ_BZIssue_strategy)
def test_bz_bzissue_dependsOn_setter(instance):
    original = instance.dependsOn
    instance.dependsOn = original
    assert instance.dependsOn == original



@given(instance=BZ_BZIssue_strategy)
def test_bz_bzissue_lastModifiedOn_setter(instance):
    original = instance.lastModifiedOn
    instance.lastModifiedOn = original
    assert instance.lastModifiedOn == original



@given(instance=BZ_BZIssue_strategy)
def test_bz_bzissue_issueId_setter(instance):
    original = instance.issueId
    instance.issueId = original
    assert instance.issueId == original



@given(instance=BZ_BZIssue_strategy)
def test_bz_bzissue_latestCommit_setter(instance):
    original = instance.latestCommit
    instance.latestCommit = original
    assert instance.latestCommit == original



@given(instance=BZ_BZIssue_strategy)
def test_bz_bzissue_referenceURL_setter(instance):
    original = instance.referenceURL
    instance.referenceURL = original
    assert instance.referenceURL == original



@given(instance=BZ_BZIssue_strategy)
def test_bz_bzissue_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=BZ_BZIssue_strategy)
def test_bz_bzissue_reportedBy_setter(instance):
    original = instance.reportedBy
    instance.reportedBy = original
    assert instance.reportedBy == original



@given(instance=BZ_BZIssue_strategy)
def test_bz_bzissue_versionFixedIn_setter(instance):
    original = instance.versionFixedIn
    instance.versionFixedIn = original
    assert instance.versionFixedIn == original



@given(instance=BZ_BZIssue_strategy)
def test_bz_bzissue_issueURL_setter(instance):
    original = instance.issueURL
    instance.issueURL = original
    assert instance.issueURL == original



@given(instance=BZ_BZIssue_strategy)
def test_bz_bzissue_assignedTo_setter(instance):
    original = instance.assignedTo
    instance.assignedTo = original
    assert instance.assignedTo == original



@given(instance=BZ_BZIssue_strategy)
def test_bz_bzissue_classification_setter(instance):
    original = instance.classification
    instance.classification = original
    assert instance.classification == original



@given(instance=BZ_BZIssue_strategy)
def test_bz_bzissue_reportedOn_setter(instance):
    original = instance.reportedOn
    instance.reportedOn = original
    assert instance.reportedOn == original



@given(instance=BZ_BZIssue_strategy)
def test_bz_bzissue_milestone_setter(instance):
    original = instance.milestone
    instance.milestone = original
    assert instance.milestone == original



@given(instance=BZ_BZIssue_strategy)
def test_bz_bzissue_issueTitle_setter(instance):
    original = instance.issueTitle
    instance.issueTitle = original
    assert instance.issueTitle == original



@given(instance=BZ_BZIssue_strategy)
def test_bz_bzissue_ccList_setter(instance):
    original = instance.ccList
    instance.ccList = original
    assert instance.ccList == original



@given(instance=BZ_BZIssue_strategy)
def test_bz_bzissue_blocks_setter(instance):
    original = instance.blocks
    instance.blocks = original
    assert instance.blocks == original



@given(instance=BZ_BZIssue_strategy)
def test_bz_bzissue_importance_setter(instance):
    original = instance.importance
    instance.importance = original
    assert instance.importance == original



@given(instance=BZ_BZIssue_strategy)
def test_bz_bzissue_productName_setter(instance):
    original = instance.productName
    instance.productName = original
    assert instance.productName == original



@given(instance=BZ_BZIssue_strategy)
def test_bz_bzissue_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=BZ_BZIssue_strategy)
def test_bz_bzissue_reportedByUsername_setter(instance):
    original = instance.reportedByUsername
    instance.reportedByUsername = original
    assert instance.reportedByUsername == original



@given(instance=BZ_BZIssue_strategy)
def test_bz_bzissue_keywords_setter(instance):
    original = instance.keywords
    instance.keywords = original
    assert instance.keywords == original



@given(instance=BZ_BZIssue_strategy)
def test_bz_bzissue_componentName_setter(instance):
    original = instance.componentName
    instance.componentName = original
    assert instance.componentName == original

@given(instance=BZ_BZComponent_strategy)
@settings(max_examples=50)
def test_bz_bzcomponent_instantiation(instance):
    assert isinstance(instance, BZ_BZComponent)



@given(instance=BZ_BZComponent_strategy)
def test_bz_bzcomponent_componentURL_setter(instance):
    original = instance.componentURL
    instance.componentURL = original
    assert instance.componentURL == original



@given(instance=BZ_BZComponent_strategy)
def test_bz_bzcomponent_componentDescription_setter(instance):
    original = instance.componentDescription
    instance.componentDescription = original
    assert instance.componentDescription == original



@given(instance=BZ_BZComponent_strategy)
def test_bz_bzcomponent_defaultAssignee_setter(instance):
    original = instance.defaultAssignee
    instance.defaultAssignee = original
    assert instance.defaultAssignee == original



@given(instance=BZ_BZComponent_strategy)
def test_bz_bzcomponent_componentId_setter(instance):
    original = instance.componentId
    instance.componentId = original
    assert instance.componentId == original

@given(instance=BZ_BZProduct_strategy)
@settings(max_examples=50)
def test_bz_bzproduct_instantiation(instance):
    assert isinstance(instance, BZ_BZProduct)



@given(instance=BZ_BZProduct_strategy)
def test_bz_bzproduct_productDescription_setter(instance):
    original = instance.productDescription
    instance.productDescription = original
    assert instance.productDescription == original



@given(instance=BZ_BZProduct_strategy)
def test_bz_bzproduct_productId_setter(instance):
    original = instance.productId
    instance.productId = original
    assert instance.productId == original



@given(instance=BZ_BZProduct_strategy)
def test_bz_bzproduct_productURL_setter(instance):
    original = instance.productURL
    instance.productURL = original
    assert instance.productURL == original

@given(instance=BZ_BZRepo_strategy)
@settings(max_examples=50)
def test_bz_bzrepo_instantiation(instance):
    assert isinstance(instance, BZ_BZRepo)



@given(instance=BZ_BZRepo_strategy)
def test_bz_bzrepo_repoURL_setter(instance):
    original = instance.repoURL
    instance.repoURL = original
    assert instance.repoURL == original
