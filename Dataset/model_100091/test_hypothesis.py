import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    MavenProject::Person,
    MavenProject::Resource,
    Resource,
    MavenProject::Build,
    Project,
    Build,
    Person,
    MavenProject::Developer,
    MavenProject::Contributor,
    MailingList,
    MavenProject::MailingList,
    MavenProject::Project,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mavenproject::person_is_not_abstract():
    assert not inspect.isabstract(MavenProject::Person)


def test_mavenproject::person_constructor_exists():
    assert callable(MavenProject::Person.__init__)


def test_mavenproject::person_constructor_args():
    sig = inspect.signature(MavenProject::Person.__init__)
    params = list(sig.parameters.keys())
    assert "properties" in params, "Missing parameter 'properties'"
    assert "name" in params, "Missing parameter 'name'"
    assert "organization" in params, "Missing parameter 'organization'"
    assert "email" in params, "Missing parameter 'email'"
    assert "url" in params, "Missing parameter 'url'"
    assert "organizationUrl" in params, "Missing parameter 'organizationUrl'"
    assert "roles" in params, "Missing parameter 'roles'"
    assert "timezone" in params, "Missing parameter 'timezone'"

def test_mavenproject::person_has_properties():
    assert hasattr(MavenProject::Person, "properties")
    descriptor = None
    for klass in MavenProject::Person.__mro__:
        if "properties" in klass.__dict__:
            descriptor = klass.__dict__["properties"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject::person_has_name():
    assert hasattr(MavenProject::Person, "name")
    descriptor = None
    for klass in MavenProject::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject::person_has_organization():
    assert hasattr(MavenProject::Person, "organization")
    descriptor = None
    for klass in MavenProject::Person.__mro__:
        if "organization" in klass.__dict__:
            descriptor = klass.__dict__["organization"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject::person_has_email():
    assert hasattr(MavenProject::Person, "email")
    descriptor = None
    for klass in MavenProject::Person.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject::person_has_url():
    assert hasattr(MavenProject::Person, "url")
    descriptor = None
    for klass in MavenProject::Person.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject::person_has_organizationUrl():
    assert hasattr(MavenProject::Person, "organizationUrl")
    descriptor = None
    for klass in MavenProject::Person.__mro__:
        if "organizationUrl" in klass.__dict__:
            descriptor = klass.__dict__["organizationUrl"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject::person_has_roles():
    assert hasattr(MavenProject::Person, "roles")
    descriptor = None
    for klass in MavenProject::Person.__mro__:
        if "roles" in klass.__dict__:
            descriptor = klass.__dict__["roles"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject::person_has_timezone():
    assert hasattr(MavenProject::Person, "timezone")
    descriptor = None
    for klass in MavenProject::Person.__mro__:
        if "timezone" in klass.__dict__:
            descriptor = klass.__dict__["timezone"]
            break
    assert isinstance(descriptor, property)



def test_mavenproject::resource_is_not_abstract():
    assert not inspect.isabstract(MavenProject::Resource)


def test_mavenproject::resource_constructor_exists():
    assert callable(MavenProject::Resource.__init__)


def test_mavenproject::resource_constructor_args():
    sig = inspect.signature(MavenProject::Resource.__init__)
    params = list(sig.parameters.keys())
    assert "includes" in params, "Missing parameter 'includes'"
    assert "directory" in params, "Missing parameter 'directory'"
    assert "targetPath" in params, "Missing parameter 'targetPath'"
    assert "excludes" in params, "Missing parameter 'excludes'"
    assert "filtering" in params, "Missing parameter 'filtering'"

def test_mavenproject::resource_has_includes():
    assert hasattr(MavenProject::Resource, "includes")
    descriptor = None
    for klass in MavenProject::Resource.__mro__:
        if "includes" in klass.__dict__:
            descriptor = klass.__dict__["includes"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject::resource_has_directory():
    assert hasattr(MavenProject::Resource, "directory")
    descriptor = None
    for klass in MavenProject::Resource.__mro__:
        if "directory" in klass.__dict__:
            descriptor = klass.__dict__["directory"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject::resource_has_targetPath():
    assert hasattr(MavenProject::Resource, "targetPath")
    descriptor = None
    for klass in MavenProject::Resource.__mro__:
        if "targetPath" in klass.__dict__:
            descriptor = klass.__dict__["targetPath"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject::resource_has_excludes():
    assert hasattr(MavenProject::Resource, "excludes")
    descriptor = None
    for klass in MavenProject::Resource.__mro__:
        if "excludes" in klass.__dict__:
            descriptor = klass.__dict__["excludes"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject::resource_has_filtering():
    assert hasattr(MavenProject::Resource, "filtering")
    descriptor = None
    for klass in MavenProject::Resource.__mro__:
        if "filtering" in klass.__dict__:
            descriptor = klass.__dict__["filtering"]
            break
    assert isinstance(descriptor, property)



def test_resource_is_not_abstract():
    assert not inspect.isabstract(Resource)


def test_resource_constructor_exists():
    assert callable(Resource.__init__)


def test_resource_constructor_args():
    sig = inspect.signature(Resource.__init__)
    params = list(sig.parameters.keys())



def test_mavenproject::build_is_not_abstract():
    assert not inspect.isabstract(MavenProject::Build)


def test_mavenproject::build_constructor_exists():
    assert callable(MavenProject::Build.__init__)


def test_mavenproject::build_constructor_args():
    sig = inspect.signature(MavenProject::Build.__init__)
    params = list(sig.parameters.keys())
    assert "sourceDirectory" in params, "Missing parameter 'sourceDirectory'"
    assert "defaultGoal" in params, "Missing parameter 'defaultGoal'"
    assert "unitTestSourceDirectory" in params, "Missing parameter 'unitTestSourceDirectory'"

def test_mavenproject::build_has_sourceDirectory():
    assert hasattr(MavenProject::Build, "sourceDirectory")
    descriptor = None
    for klass in MavenProject::Build.__mro__:
        if "sourceDirectory" in klass.__dict__:
            descriptor = klass.__dict__["sourceDirectory"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject::build_has_defaultGoal():
    assert hasattr(MavenProject::Build, "defaultGoal")
    descriptor = None
    for klass in MavenProject::Build.__mro__:
        if "defaultGoal" in klass.__dict__:
            descriptor = klass.__dict__["defaultGoal"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject::build_has_unitTestSourceDirectory():
    assert hasattr(MavenProject::Build, "unitTestSourceDirectory")
    descriptor = None
    for klass in MavenProject::Build.__mro__:
        if "unitTestSourceDirectory" in klass.__dict__:
            descriptor = klass.__dict__["unitTestSourceDirectory"]
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



def test_mavenproject::developer_is_not_abstract():
    assert not inspect.isabstract(MavenProject::Developer)


def test_mavenproject::developer_constructor_exists():
    assert callable(MavenProject::Developer.__init__)


def test_mavenproject::developer_constructor_args():
    sig = inspect.signature(MavenProject::Developer.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mavenproject::developer_has_id():
    assert hasattr(MavenProject::Developer, "id")
    descriptor = None
    for klass in MavenProject::Developer.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mavenproject::contributor_is_not_abstract():
    assert not inspect.isabstract(MavenProject::Contributor)


def test_mavenproject::contributor_constructor_exists():
    assert callable(MavenProject::Contributor.__init__)


def test_mavenproject::contributor_constructor_args():
    sig = inspect.signature(MavenProject::Contributor.__init__)
    params = list(sig.parameters.keys())



def test_mailinglist_is_not_abstract():
    assert not inspect.isabstract(MailingList)


def test_mailinglist_constructor_exists():
    assert callable(MailingList.__init__)


def test_mailinglist_constructor_args():
    sig = inspect.signature(MailingList.__init__)
    params = list(sig.parameters.keys())



def test_mavenproject::mailinglist_is_not_abstract():
    assert not inspect.isabstract(MavenProject::MailingList)


def test_mavenproject::mailinglist_constructor_exists():
    assert callable(MavenProject::MailingList.__init__)


def test_mavenproject::mailinglist_constructor_args():
    sig = inspect.signature(MavenProject::MailingList.__init__)
    params = list(sig.parameters.keys())
    assert "otherArchives" in params, "Missing parameter 'otherArchives'"
    assert "subscribe" in params, "Missing parameter 'subscribe'"
    assert "post" in params, "Missing parameter 'post'"
    assert "unsubscribe" in params, "Missing parameter 'unsubscribe'"
    assert "name" in params, "Missing parameter 'name'"
    assert "archive" in params, "Missing parameter 'archive'"

def test_mavenproject::mailinglist_has_otherArchives():
    assert hasattr(MavenProject::MailingList, "otherArchives")
    descriptor = None
    for klass in MavenProject::MailingList.__mro__:
        if "otherArchives" in klass.__dict__:
            descriptor = klass.__dict__["otherArchives"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject::mailinglist_has_subscribe():
    assert hasattr(MavenProject::MailingList, "subscribe")
    descriptor = None
    for klass in MavenProject::MailingList.__mro__:
        if "subscribe" in klass.__dict__:
            descriptor = klass.__dict__["subscribe"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject::mailinglist_has_post():
    assert hasattr(MavenProject::MailingList, "post")
    descriptor = None
    for klass in MavenProject::MailingList.__mro__:
        if "post" in klass.__dict__:
            descriptor = klass.__dict__["post"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject::mailinglist_has_unsubscribe():
    assert hasattr(MavenProject::MailingList, "unsubscribe")
    descriptor = None
    for klass in MavenProject::MailingList.__mro__:
        if "unsubscribe" in klass.__dict__:
            descriptor = klass.__dict__["unsubscribe"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject::mailinglist_has_name():
    assert hasattr(MavenProject::MailingList, "name")
    descriptor = None
    for klass in MavenProject::MailingList.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject::mailinglist_has_archive():
    assert hasattr(MavenProject::MailingList, "archive")
    descriptor = None
    for klass in MavenProject::MailingList.__mro__:
        if "archive" in klass.__dict__:
            descriptor = klass.__dict__["archive"]
            break
    assert isinstance(descriptor, property)



def test_mavenproject::project_is_not_abstract():
    assert not inspect.isabstract(MavenProject::Project)


def test_mavenproject::project_constructor_exists():
    assert callable(MavenProject::Project.__init__)


def test_mavenproject::project_constructor_args():
    sig = inspect.signature(MavenProject::Project.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "artifactId" in params, "Missing parameter 'artifactId'"
    assert "description" in params, "Missing parameter 'description'"
    assert "groupId" in params, "Missing parameter 'groupId'"

def test_mavenproject::project_has_name():
    assert hasattr(MavenProject::Project, "name")
    descriptor = None
    for klass in MavenProject::Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject::project_has_id():
    assert hasattr(MavenProject::Project, "id")
    descriptor = None
    for klass in MavenProject::Project.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject::project_has_artifactId():
    assert hasattr(MavenProject::Project, "artifactId")
    descriptor = None
    for klass in MavenProject::Project.__mro__:
        if "artifactId" in klass.__dict__:
            descriptor = klass.__dict__["artifactId"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject::project_has_description():
    assert hasattr(MavenProject::Project, "description")
    descriptor = None
    for klass in MavenProject::Project.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_mavenproject::project_has_groupId():
    assert hasattr(MavenProject::Project, "groupId")
    descriptor = None
    for klass in MavenProject::Project.__mro__:
        if "groupId" in klass.__dict__:
            descriptor = klass.__dict__["groupId"]
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
MavenProject::Person_strategy = st.builds(
    MavenProject::Person,
    properties=
        safe_text,
    name=
        safe_text,
    organization=
        safe_text,
    email=
        safe_text,
    url=
        safe_text,
    organizationUrl=
        safe_text,
    roles=
        safe_text,
    timezone=
        safe_text
)
MavenProject::Resource_strategy = st.builds(
    MavenProject::Resource,
    includes=
        safe_text,
    directory=
        safe_text,
    targetPath=
        safe_text,
    excludes=
        safe_text,
    filtering=
        safe_text
)
Resource_strategy = st.builds(
    Resource,
)
MavenProject::Build_strategy = st.builds(
    MavenProject::Build,
    sourceDirectory=
        safe_text,
    defaultGoal=
        safe_text,
    unitTestSourceDirectory=
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
MavenProject::Developer_strategy = st.builds(
    MavenProject::Developer,
    id=
        safe_text
)
MavenProject::Contributor_strategy = st.builds(
    MavenProject::Contributor,
)
MailingList_strategy = st.builds(
    MailingList,
)
MavenProject::MailingList_strategy = st.builds(
    MavenProject::MailingList,
    otherArchives=
        safe_text,
    subscribe=
        safe_text,
    post=
        safe_text,
    unsubscribe=
        safe_text,
    name=
        safe_text,
    archive=
        safe_text
)
MavenProject::Project_strategy = st.builds(
    MavenProject::Project,
    name=
        safe_text,
    id=
        safe_text,
    artifactId=
        safe_text,
    description=
        safe_text,
    groupId=
        safe_text
)

@given(instance=MavenProject::Person_strategy)
@settings(max_examples=50)
def test_mavenproject::person_instantiation(instance):
    assert isinstance(instance, MavenProject::Person)

@given(instance=MavenProject::Person_strategy)
def test_mavenproject::person_properties_type(instance):
    assert isinstance(instance.properties, str)


@given(instance=MavenProject::Person_strategy)
def test_mavenproject::person_properties_setter(instance):
    original = instance.properties
    instance.properties = original
    assert instance.properties == original

@given(instance=MavenProject::Person_strategy)
def test_mavenproject::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MavenProject::Person_strategy)
def test_mavenproject::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MavenProject::Person_strategy)
def test_mavenproject::person_organization_type(instance):
    assert isinstance(instance.organization, str)


@given(instance=MavenProject::Person_strategy)
def test_mavenproject::person_organization_setter(instance):
    original = instance.organization
    instance.organization = original
    assert instance.organization == original

@given(instance=MavenProject::Person_strategy)
def test_mavenproject::person_email_type(instance):
    assert isinstance(instance.email, str)


@given(instance=MavenProject::Person_strategy)
def test_mavenproject::person_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=MavenProject::Person_strategy)
def test_mavenproject::person_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=MavenProject::Person_strategy)
def test_mavenproject::person_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=MavenProject::Person_strategy)
def test_mavenproject::person_organizationUrl_type(instance):
    assert isinstance(instance.organizationUrl, str)


@given(instance=MavenProject::Person_strategy)
def test_mavenproject::person_organizationUrl_setter(instance):
    original = instance.organizationUrl
    instance.organizationUrl = original
    assert instance.organizationUrl == original

@given(instance=MavenProject::Person_strategy)
def test_mavenproject::person_roles_type(instance):
    assert isinstance(instance.roles, str)


@given(instance=MavenProject::Person_strategy)
def test_mavenproject::person_roles_setter(instance):
    original = instance.roles
    instance.roles = original
    assert instance.roles == original

@given(instance=MavenProject::Person_strategy)
def test_mavenproject::person_timezone_type(instance):
    assert isinstance(instance.timezone, str)


@given(instance=MavenProject::Person_strategy)
def test_mavenproject::person_timezone_setter(instance):
    original = instance.timezone
    instance.timezone = original
    assert instance.timezone == original

@given(instance=MavenProject::Resource_strategy)
@settings(max_examples=50)
def test_mavenproject::resource_instantiation(instance):
    assert isinstance(instance, MavenProject::Resource)

@given(instance=MavenProject::Resource_strategy)
def test_mavenproject::resource_includes_type(instance):
    assert isinstance(instance.includes, str)


@given(instance=MavenProject::Resource_strategy)
def test_mavenproject::resource_includes_setter(instance):
    original = instance.includes
    instance.includes = original
    assert instance.includes == original

@given(instance=MavenProject::Resource_strategy)
def test_mavenproject::resource_directory_type(instance):
    assert isinstance(instance.directory, str)


@given(instance=MavenProject::Resource_strategy)
def test_mavenproject::resource_directory_setter(instance):
    original = instance.directory
    instance.directory = original
    assert instance.directory == original

@given(instance=MavenProject::Resource_strategy)
def test_mavenproject::resource_targetPath_type(instance):
    assert isinstance(instance.targetPath, str)


@given(instance=MavenProject::Resource_strategy)
def test_mavenproject::resource_targetPath_setter(instance):
    original = instance.targetPath
    instance.targetPath = original
    assert instance.targetPath == original

@given(instance=MavenProject::Resource_strategy)
def test_mavenproject::resource_excludes_type(instance):
    assert isinstance(instance.excludes, str)


@given(instance=MavenProject::Resource_strategy)
def test_mavenproject::resource_excludes_setter(instance):
    original = instance.excludes
    instance.excludes = original
    assert instance.excludes == original

@given(instance=MavenProject::Resource_strategy)
def test_mavenproject::resource_filtering_type(instance):
    assert isinstance(instance.filtering, str)


@given(instance=MavenProject::Resource_strategy)
def test_mavenproject::resource_filtering_setter(instance):
    original = instance.filtering
    instance.filtering = original
    assert instance.filtering == original

@given(instance=Resource_strategy)
@settings(max_examples=50)
def test_resource_instantiation(instance):
    assert isinstance(instance, Resource)

@given(instance=MavenProject::Build_strategy)
@settings(max_examples=50)
def test_mavenproject::build_instantiation(instance):
    assert isinstance(instance, MavenProject::Build)

@given(instance=MavenProject::Build_strategy)
def test_mavenproject::build_sourceDirectory_type(instance):
    assert isinstance(instance.sourceDirectory, str)


@given(instance=MavenProject::Build_strategy)
def test_mavenproject::build_sourceDirectory_setter(instance):
    original = instance.sourceDirectory
    instance.sourceDirectory = original
    assert instance.sourceDirectory == original

@given(instance=MavenProject::Build_strategy)
def test_mavenproject::build_defaultGoal_type(instance):
    assert isinstance(instance.defaultGoal, str)


@given(instance=MavenProject::Build_strategy)
def test_mavenproject::build_defaultGoal_setter(instance):
    original = instance.defaultGoal
    instance.defaultGoal = original
    assert instance.defaultGoal == original

@given(instance=MavenProject::Build_strategy)
def test_mavenproject::build_unitTestSourceDirectory_type(instance):
    assert isinstance(instance.unitTestSourceDirectory, str)


@given(instance=MavenProject::Build_strategy)
def test_mavenproject::build_unitTestSourceDirectory_setter(instance):
    original = instance.unitTestSourceDirectory
    instance.unitTestSourceDirectory = original
    assert instance.unitTestSourceDirectory == original

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

@given(instance=MavenProject::Developer_strategy)
@settings(max_examples=50)
def test_mavenproject::developer_instantiation(instance):
    assert isinstance(instance, MavenProject::Developer)

@given(instance=MavenProject::Developer_strategy)
def test_mavenproject::developer_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=MavenProject::Developer_strategy)
def test_mavenproject::developer_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=MavenProject::Contributor_strategy)
@settings(max_examples=50)
def test_mavenproject::contributor_instantiation(instance):
    assert isinstance(instance, MavenProject::Contributor)

@given(instance=MailingList_strategy)
@settings(max_examples=50)
def test_mailinglist_instantiation(instance):
    assert isinstance(instance, MailingList)

@given(instance=MavenProject::MailingList_strategy)
@settings(max_examples=50)
def test_mavenproject::mailinglist_instantiation(instance):
    assert isinstance(instance, MavenProject::MailingList)

@given(instance=MavenProject::MailingList_strategy)
def test_mavenproject::mailinglist_otherArchives_type(instance):
    assert isinstance(instance.otherArchives, str)


@given(instance=MavenProject::MailingList_strategy)
def test_mavenproject::mailinglist_otherArchives_setter(instance):
    original = instance.otherArchives
    instance.otherArchives = original
    assert instance.otherArchives == original

@given(instance=MavenProject::MailingList_strategy)
def test_mavenproject::mailinglist_subscribe_type(instance):
    assert isinstance(instance.subscribe, str)


@given(instance=MavenProject::MailingList_strategy)
def test_mavenproject::mailinglist_subscribe_setter(instance):
    original = instance.subscribe
    instance.subscribe = original
    assert instance.subscribe == original

@given(instance=MavenProject::MailingList_strategy)
def test_mavenproject::mailinglist_post_type(instance):
    assert isinstance(instance.post, str)


@given(instance=MavenProject::MailingList_strategy)
def test_mavenproject::mailinglist_post_setter(instance):
    original = instance.post
    instance.post = original
    assert instance.post == original

@given(instance=MavenProject::MailingList_strategy)
def test_mavenproject::mailinglist_unsubscribe_type(instance):
    assert isinstance(instance.unsubscribe, str)


@given(instance=MavenProject::MailingList_strategy)
def test_mavenproject::mailinglist_unsubscribe_setter(instance):
    original = instance.unsubscribe
    instance.unsubscribe = original
    assert instance.unsubscribe == original

@given(instance=MavenProject::MailingList_strategy)
def test_mavenproject::mailinglist_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MavenProject::MailingList_strategy)
def test_mavenproject::mailinglist_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MavenProject::MailingList_strategy)
def test_mavenproject::mailinglist_archive_type(instance):
    assert isinstance(instance.archive, str)


@given(instance=MavenProject::MailingList_strategy)
def test_mavenproject::mailinglist_archive_setter(instance):
    original = instance.archive
    instance.archive = original
    assert instance.archive == original

@given(instance=MavenProject::Project_strategy)
@settings(max_examples=50)
def test_mavenproject::project_instantiation(instance):
    assert isinstance(instance, MavenProject::Project)

@given(instance=MavenProject::Project_strategy)
def test_mavenproject::project_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MavenProject::Project_strategy)
def test_mavenproject::project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MavenProject::Project_strategy)
def test_mavenproject::project_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=MavenProject::Project_strategy)
def test_mavenproject::project_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=MavenProject::Project_strategy)
def test_mavenproject::project_artifactId_type(instance):
    assert isinstance(instance.artifactId, str)


@given(instance=MavenProject::Project_strategy)
def test_mavenproject::project_artifactId_setter(instance):
    original = instance.artifactId
    instance.artifactId = original
    assert instance.artifactId == original

@given(instance=MavenProject::Project_strategy)
def test_mavenproject::project_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=MavenProject::Project_strategy)
def test_mavenproject::project_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=MavenProject::Project_strategy)
def test_mavenproject::project_groupId_type(instance):
    assert isinstance(instance.groupId, str)


@given(instance=MavenProject::Project_strategy)
def test_mavenproject::project_groupId_setter(instance):
    original = instance.groupId
    instance.groupId = original
    assert instance.groupId == original
