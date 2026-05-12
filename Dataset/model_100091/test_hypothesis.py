import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    MavenProject_Person,
    MavenProject_Resource,
    Resource,
    MavenProject_Build,
    Project,
    Build,
    Person,
    MavenProject_Contributor,
    MavenProject_Developer,
    MailingList,
    MavenProject_MailingList,
    MavenProject_Project,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mavenproject_person_is_not_abstract():
    assert not inspect.isabstract(MavenProject_Person)


def test_mavenproject_person_constructor_exists():
    assert callable(MavenProject_Person.__init__)


def test_mavenproject_person_constructor_args():
    sig = inspect.signature(MavenProject_Person.__init__)
    params = list(sig.parameters.keys())
    assert "properties" in params, "Missing parameter 'properties'"
    assert "timezone" in params, "Missing parameter 'timezone'"
    assert "email" in params, "Missing parameter 'email'"
    assert "url" in params, "Missing parameter 'url'"
    assert "name" in params, "Missing parameter 'name'"
    assert "roles" in params, "Missing parameter 'roles'"
    assert "organizationUrl" in params, "Missing parameter 'organizationUrl'"
    assert "organization" in params, "Missing parameter 'organization'"

def test_mavenproject_person_has_properties():
    assert hasattr(MavenProject_Person, "properties")
    descriptor = None
    for klass in MavenProject_Person.__mro__:
        if "properties" in klass.__dict__:
            descriptor = klass.__dict__["properties"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject_person_has_timezone():
    assert hasattr(MavenProject_Person, "timezone")
    descriptor = None
    for klass in MavenProject_Person.__mro__:
        if "timezone" in klass.__dict__:
            descriptor = klass.__dict__["timezone"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject_person_has_email():
    assert hasattr(MavenProject_Person, "email")
    descriptor = None
    for klass in MavenProject_Person.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject_person_has_url():
    assert hasattr(MavenProject_Person, "url")
    descriptor = None
    for klass in MavenProject_Person.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject_person_has_name():
    assert hasattr(MavenProject_Person, "name")
    descriptor = None
    for klass in MavenProject_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject_person_has_roles():
    assert hasattr(MavenProject_Person, "roles")
    descriptor = None
    for klass in MavenProject_Person.__mro__:
        if "roles" in klass.__dict__:
            descriptor = klass.__dict__["roles"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject_person_has_organizationUrl():
    assert hasattr(MavenProject_Person, "organizationUrl")
    descriptor = None
    for klass in MavenProject_Person.__mro__:
        if "organizationUrl" in klass.__dict__:
            descriptor = klass.__dict__["organizationUrl"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject_person_has_organization():
    assert hasattr(MavenProject_Person, "organization")
    descriptor = None
    for klass in MavenProject_Person.__mro__:
        if "organization" in klass.__dict__:
            descriptor = klass.__dict__["organization"]
            break
    assert isinstance(descriptor, property)



def test_mavenproject_resource_is_not_abstract():
    assert not inspect.isabstract(MavenProject_Resource)


def test_mavenproject_resource_constructor_exists():
    assert callable(MavenProject_Resource.__init__)


def test_mavenproject_resource_constructor_args():
    sig = inspect.signature(MavenProject_Resource.__init__)
    params = list(sig.parameters.keys())
    assert "directory" in params, "Missing parameter 'directory'"
    assert "includes" in params, "Missing parameter 'includes'"
    assert "targetPath" in params, "Missing parameter 'targetPath'"
    assert "filtering" in params, "Missing parameter 'filtering'"
    assert "excludes" in params, "Missing parameter 'excludes'"

def test_mavenproject_resource_has_directory():
    assert hasattr(MavenProject_Resource, "directory")
    descriptor = None
    for klass in MavenProject_Resource.__mro__:
        if "directory" in klass.__dict__:
            descriptor = klass.__dict__["directory"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject_resource_has_includes():
    assert hasattr(MavenProject_Resource, "includes")
    descriptor = None
    for klass in MavenProject_Resource.__mro__:
        if "includes" in klass.__dict__:
            descriptor = klass.__dict__["includes"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject_resource_has_targetPath():
    assert hasattr(MavenProject_Resource, "targetPath")
    descriptor = None
    for klass in MavenProject_Resource.__mro__:
        if "targetPath" in klass.__dict__:
            descriptor = klass.__dict__["targetPath"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject_resource_has_filtering():
    assert hasattr(MavenProject_Resource, "filtering")
    descriptor = None
    for klass in MavenProject_Resource.__mro__:
        if "filtering" in klass.__dict__:
            descriptor = klass.__dict__["filtering"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject_resource_has_excludes():
    assert hasattr(MavenProject_Resource, "excludes")
    descriptor = None
    for klass in MavenProject_Resource.__mro__:
        if "excludes" in klass.__dict__:
            descriptor = klass.__dict__["excludes"]
            break
    assert isinstance(descriptor, property)



def test_resource_is_not_abstract():
    assert not inspect.isabstract(Resource)


def test_resource_constructor_exists():
    assert callable(Resource.__init__)


def test_resource_constructor_args():
    sig = inspect.signature(Resource.__init__)
    params = list(sig.parameters.keys())



def test_mavenproject_build_is_not_abstract():
    assert not inspect.isabstract(MavenProject_Build)


def test_mavenproject_build_constructor_exists():
    assert callable(MavenProject_Build.__init__)


def test_mavenproject_build_constructor_args():
    sig = inspect.signature(MavenProject_Build.__init__)
    params = list(sig.parameters.keys())
    assert "unitTestSourceDirectory" in params, "Missing parameter 'unitTestSourceDirectory'"
    assert "sourceDirectory" in params, "Missing parameter 'sourceDirectory'"
    assert "defaultGoal" in params, "Missing parameter 'defaultGoal'"

def test_mavenproject_build_has_unitTestSourceDirectory():
    assert hasattr(MavenProject_Build, "unitTestSourceDirectory")
    descriptor = None
    for klass in MavenProject_Build.__mro__:
        if "unitTestSourceDirectory" in klass.__dict__:
            descriptor = klass.__dict__["unitTestSourceDirectory"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject_build_has_sourceDirectory():
    assert hasattr(MavenProject_Build, "sourceDirectory")
    descriptor = None
    for klass in MavenProject_Build.__mro__:
        if "sourceDirectory" in klass.__dict__:
            descriptor = klass.__dict__["sourceDirectory"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject_build_has_defaultGoal():
    assert hasattr(MavenProject_Build, "defaultGoal")
    descriptor = None
    for klass in MavenProject_Build.__mro__:
        if "defaultGoal" in klass.__dict__:
            descriptor = klass.__dict__["defaultGoal"]
            break
    assert isinstance(descriptor, property)



def test_project_is_not_abstract():
    assert not inspect.isabstract(Project)


def test_project_constructor_exists():
    assert callable(Project.__init__)


def test_project_constructor_args():
    sig = inspect.signature(Project.__init__)
    params = list(sig.parameters.keys())



def test_build_is_not_abstract():
    assert not inspect.isabstract(Build)


def test_build_constructor_exists():
    assert callable(Build.__init__)


def test_build_constructor_args():
    sig = inspect.signature(Build.__init__)
    params = list(sig.parameters.keys())



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_mavenproject_contributor_is_not_abstract():
    assert not inspect.isabstract(MavenProject_Contributor)


def test_mavenproject_contributor_constructor_exists():
    assert callable(MavenProject_Contributor.__init__)


def test_mavenproject_contributor_constructor_args():
    sig = inspect.signature(MavenProject_Contributor.__init__)
    params = list(sig.parameters.keys())



def test_mavenproject_developer_is_not_abstract():
    assert not inspect.isabstract(MavenProject_Developer)


def test_mavenproject_developer_constructor_exists():
    assert callable(MavenProject_Developer.__init__)


def test_mavenproject_developer_constructor_args():
    sig = inspect.signature(MavenProject_Developer.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mavenproject_developer_has_id():
    assert hasattr(MavenProject_Developer, "id")
    descriptor = None
    for klass in MavenProject_Developer.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mailinglist_is_not_abstract():
    assert not inspect.isabstract(MailingList)


def test_mailinglist_constructor_exists():
    assert callable(MailingList.__init__)


def test_mailinglist_constructor_args():
    sig = inspect.signature(MailingList.__init__)
    params = list(sig.parameters.keys())



def test_mavenproject_mailinglist_is_not_abstract():
    assert not inspect.isabstract(MavenProject_MailingList)


def test_mavenproject_mailinglist_constructor_exists():
    assert callable(MavenProject_MailingList.__init__)


def test_mavenproject_mailinglist_constructor_args():
    sig = inspect.signature(MavenProject_MailingList.__init__)
    params = list(sig.parameters.keys())
    assert "otherArchives" in params, "Missing parameter 'otherArchives'"
    assert "unsubscribe" in params, "Missing parameter 'unsubscribe'"
    assert "subscribe" in params, "Missing parameter 'subscribe'"
    assert "name" in params, "Missing parameter 'name'"
    assert "archive" in params, "Missing parameter 'archive'"
    assert "post" in params, "Missing parameter 'post'"

def test_mavenproject_mailinglist_has_otherArchives():
    assert hasattr(MavenProject_MailingList, "otherArchives")
    descriptor = None
    for klass in MavenProject_MailingList.__mro__:
        if "otherArchives" in klass.__dict__:
            descriptor = klass.__dict__["otherArchives"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject_mailinglist_has_unsubscribe():
    assert hasattr(MavenProject_MailingList, "unsubscribe")
    descriptor = None
    for klass in MavenProject_MailingList.__mro__:
        if "unsubscribe" in klass.__dict__:
            descriptor = klass.__dict__["unsubscribe"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject_mailinglist_has_subscribe():
    assert hasattr(MavenProject_MailingList, "subscribe")
    descriptor = None
    for klass in MavenProject_MailingList.__mro__:
        if "subscribe" in klass.__dict__:
            descriptor = klass.__dict__["subscribe"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject_mailinglist_has_name():
    assert hasattr(MavenProject_MailingList, "name")
    descriptor = None
    for klass in MavenProject_MailingList.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject_mailinglist_has_archive():
    assert hasattr(MavenProject_MailingList, "archive")
    descriptor = None
    for klass in MavenProject_MailingList.__mro__:
        if "archive" in klass.__dict__:
            descriptor = klass.__dict__["archive"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject_mailinglist_has_post():
    assert hasattr(MavenProject_MailingList, "post")
    descriptor = None
    for klass in MavenProject_MailingList.__mro__:
        if "post" in klass.__dict__:
            descriptor = klass.__dict__["post"]
            break
    assert isinstance(descriptor, property)



def test_mavenproject_project_is_not_abstract():
    assert not inspect.isabstract(MavenProject_Project)


def test_mavenproject_project_constructor_exists():
    assert callable(MavenProject_Project.__init__)


def test_mavenproject_project_constructor_args():
    sig = inspect.signature(MavenProject_Project.__init__)
    params = list(sig.parameters.keys())
    assert "artifactId" in params, "Missing parameter 'artifactId'"
    assert "id" in params, "Missing parameter 'id'"
    assert "groupId" in params, "Missing parameter 'groupId'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"

def test_mavenproject_project_has_artifactId():
    assert hasattr(MavenProject_Project, "artifactId")
    descriptor = None
    for klass in MavenProject_Project.__mro__:
        if "artifactId" in klass.__dict__:
            descriptor = klass.__dict__["artifactId"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject_project_has_id():
    assert hasattr(MavenProject_Project, "id")
    descriptor = None
    for klass in MavenProject_Project.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject_project_has_groupId():
    assert hasattr(MavenProject_Project, "groupId")
    descriptor = None
    for klass in MavenProject_Project.__mro__:
        if "groupId" in klass.__dict__:
            descriptor = klass.__dict__["groupId"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject_project_has_description():
    assert hasattr(MavenProject_Project, "description")
    descriptor = None
    for klass in MavenProject_Project.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject_project_has_name():
    assert hasattr(MavenProject_Project, "name")
    descriptor = None
    for klass in MavenProject_Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
MavenProject_Person_strategy = st.builds(
    MavenProject_Person,
    properties=
        safe_text,
    timezone=
        safe_text,
    email=
        safe_text,
    url=
        safe_text,
    name=
        safe_text,
    roles=
        safe_text,
    organizationUrl=
        safe_text,
    organization=
        safe_text
)
MavenProject_Resource_strategy = st.builds(
    MavenProject_Resource,
    directory=
        safe_text,
    includes=
        safe_text,
    targetPath=
        safe_text,
    filtering=
        safe_text,
    excludes=
        safe_text
)
Resource_strategy = st.builds(
    Resource,
)
MavenProject_Build_strategy = st.builds(
    MavenProject_Build,
    unitTestSourceDirectory=
        safe_text,
    sourceDirectory=
        safe_text,
    defaultGoal=
        safe_text
)
Project_strategy = st.builds(
    Project,
)
Build_strategy = st.builds(
    Build,
)
Person_strategy = st.builds(
    Person,
)
MavenProject_Contributor_strategy = st.builds(
    MavenProject_Contributor,
)
MavenProject_Developer_strategy = st.builds(
    MavenProject_Developer,
    id=
        safe_text
)
MailingList_strategy = st.builds(
    MailingList,
)
MavenProject_MailingList_strategy = st.builds(
    MavenProject_MailingList,
    otherArchives=
        safe_text,
    unsubscribe=
        safe_text,
    subscribe=
        safe_text,
    name=
        safe_text,
    archive=
        safe_text,
    post=
        safe_text
)
MavenProject_Project_strategy = st.builds(
    MavenProject_Project,
    artifactId=
        safe_text,
    id=
        safe_text,
    groupId=
        safe_text,
    description=
        safe_text,
    name=
        safe_text
)

@given(instance=MavenProject_Person_strategy)
@settings(max_examples=50)
def test_mavenproject_person_instantiation(instance):
    assert isinstance(instance, MavenProject_Person)



@given(instance=MavenProject_Person_strategy)
def test_mavenproject_person_properties_setter(instance):
    original = instance.properties
    instance.properties = original
    assert instance.properties == original



@given(instance=MavenProject_Person_strategy)
def test_mavenproject_person_timezone_setter(instance):
    original = instance.timezone
    instance.timezone = original
    assert instance.timezone == original



@given(instance=MavenProject_Person_strategy)
def test_mavenproject_person_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=MavenProject_Person_strategy)
def test_mavenproject_person_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original



@given(instance=MavenProject_Person_strategy)
def test_mavenproject_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=MavenProject_Person_strategy)
def test_mavenproject_person_roles_setter(instance):
    original = instance.roles
    instance.roles = original
    assert instance.roles == original



@given(instance=MavenProject_Person_strategy)
def test_mavenproject_person_organizationUrl_setter(instance):
    original = instance.organizationUrl
    instance.organizationUrl = original
    assert instance.organizationUrl == original



@given(instance=MavenProject_Person_strategy)
def test_mavenproject_person_organization_setter(instance):
    original = instance.organization
    instance.organization = original
    assert instance.organization == original

@given(instance=MavenProject_Resource_strategy)
@settings(max_examples=50)
def test_mavenproject_resource_instantiation(instance):
    assert isinstance(instance, MavenProject_Resource)



@given(instance=MavenProject_Resource_strategy)
def test_mavenproject_resource_directory_setter(instance):
    original = instance.directory
    instance.directory = original
    assert instance.directory == original



@given(instance=MavenProject_Resource_strategy)
def test_mavenproject_resource_includes_setter(instance):
    original = instance.includes
    instance.includes = original
    assert instance.includes == original



@given(instance=MavenProject_Resource_strategy)
def test_mavenproject_resource_targetPath_setter(instance):
    original = instance.targetPath
    instance.targetPath = original
    assert instance.targetPath == original



@given(instance=MavenProject_Resource_strategy)
def test_mavenproject_resource_filtering_setter(instance):
    original = instance.filtering
    instance.filtering = original
    assert instance.filtering == original



@given(instance=MavenProject_Resource_strategy)
def test_mavenproject_resource_excludes_setter(instance):
    original = instance.excludes
    instance.excludes = original
    assert instance.excludes == original

@given(instance=Resource_strategy)
@settings(max_examples=50)
def test_resource_instantiation(instance):
    assert isinstance(instance, Resource)

@given(instance=MavenProject_Build_strategy)
@settings(max_examples=50)
def test_mavenproject_build_instantiation(instance):
    assert isinstance(instance, MavenProject_Build)



@given(instance=MavenProject_Build_strategy)
def test_mavenproject_build_unitTestSourceDirectory_setter(instance):
    original = instance.unitTestSourceDirectory
    instance.unitTestSourceDirectory = original
    assert instance.unitTestSourceDirectory == original



@given(instance=MavenProject_Build_strategy)
def test_mavenproject_build_sourceDirectory_setter(instance):
    original = instance.sourceDirectory
    instance.sourceDirectory = original
    assert instance.sourceDirectory == original



@given(instance=MavenProject_Build_strategy)
def test_mavenproject_build_defaultGoal_setter(instance):
    original = instance.defaultGoal
    instance.defaultGoal = original
    assert instance.defaultGoal == original

@given(instance=Project_strategy)
@settings(max_examples=50)
def test_project_instantiation(instance):
    assert isinstance(instance, Project)

@given(instance=Build_strategy)
@settings(max_examples=50)
def test_build_instantiation(instance):
    assert isinstance(instance, Build)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=MavenProject_Contributor_strategy)
@settings(max_examples=50)
def test_mavenproject_contributor_instantiation(instance):
    assert isinstance(instance, MavenProject_Contributor)

@given(instance=MavenProject_Developer_strategy)
@settings(max_examples=50)
def test_mavenproject_developer_instantiation(instance):
    assert isinstance(instance, MavenProject_Developer)



@given(instance=MavenProject_Developer_strategy)
def test_mavenproject_developer_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=MailingList_strategy)
@settings(max_examples=50)
def test_mailinglist_instantiation(instance):
    assert isinstance(instance, MailingList)

@given(instance=MavenProject_MailingList_strategy)
@settings(max_examples=50)
def test_mavenproject_mailinglist_instantiation(instance):
    assert isinstance(instance, MavenProject_MailingList)



@given(instance=MavenProject_MailingList_strategy)
def test_mavenproject_mailinglist_otherArchives_setter(instance):
    original = instance.otherArchives
    instance.otherArchives = original
    assert instance.otherArchives == original



@given(instance=MavenProject_MailingList_strategy)
def test_mavenproject_mailinglist_unsubscribe_setter(instance):
    original = instance.unsubscribe
    instance.unsubscribe = original
    assert instance.unsubscribe == original



@given(instance=MavenProject_MailingList_strategy)
def test_mavenproject_mailinglist_subscribe_setter(instance):
    original = instance.subscribe
    instance.subscribe = original
    assert instance.subscribe == original



@given(instance=MavenProject_MailingList_strategy)
def test_mavenproject_mailinglist_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=MavenProject_MailingList_strategy)
def test_mavenproject_mailinglist_archive_setter(instance):
    original = instance.archive
    instance.archive = original
    assert instance.archive == original



@given(instance=MavenProject_MailingList_strategy)
def test_mavenproject_mailinglist_post_setter(instance):
    original = instance.post
    instance.post = original
    assert instance.post == original

@given(instance=MavenProject_Project_strategy)
@settings(max_examples=50)
def test_mavenproject_project_instantiation(instance):
    assert isinstance(instance, MavenProject_Project)



@given(instance=MavenProject_Project_strategy)
def test_mavenproject_project_artifactId_setter(instance):
    original = instance.artifactId
    instance.artifactId = original
    assert instance.artifactId == original



@given(instance=MavenProject_Project_strategy)
def test_mavenproject_project_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=MavenProject_Project_strategy)
def test_mavenproject_project_groupId_setter(instance):
    original = instance.groupId
    instance.groupId = original
    assert instance.groupId == original



@given(instance=MavenProject_Project_strategy)
def test_mavenproject_project_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=MavenProject_Project_strategy)
def test_mavenproject_project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
