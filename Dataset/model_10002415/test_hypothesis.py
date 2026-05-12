import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Role,
    Attachment,
    Comment,
    Activity,
    Project,
    User,
    String,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_role_is_not_abstract():
    assert not inspect.isabstract(Role)


def test_role_constructor_exists():
    assert callable(Role.__init__)


def test_role_constructor_args():
    sig = inspect.signature(Role.__init__)
    params = list(sig.parameters.keys())
    assert "Description" in params, "Missing parameter 'Description'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "RoleID" in params, "Missing parameter 'RoleID'"

def test_role_has_Description():
    assert hasattr(Role, "Description")
    descriptor = None
    for klass in Role.__mro__:
        if "Description" in klass.__dict__:
            descriptor = klass.__dict__["Description"]
            break
    assert isinstance(descriptor, property)

def test_role_has_Name():
    assert hasattr(Role, "Name")
    descriptor = None
    for klass in Role.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_role_has_RoleID():
    assert hasattr(Role, "RoleID")
    descriptor = None
    for klass in Role.__mro__:
        if "RoleID" in klass.__dict__:
            descriptor = klass.__dict__["RoleID"]
            break
    assert isinstance(descriptor, property)



def test_attachment_is_not_abstract():
    assert not inspect.isabstract(Attachment)


def test_attachment_constructor_exists():
    assert callable(Attachment.__init__)


def test_attachment_constructor_args():
    sig = inspect.signature(Attachment.__init__)
    params = list(sig.parameters.keys())
    assert "AttachmentID" in params, "Missing parameter 'AttachmentID'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Project" in params, "Missing parameter 'Project'"
    assert "User" in params, "Missing parameter 'User'"
    assert "Size" in params, "Missing parameter 'Size'"
    assert "Extension" in params, "Missing parameter 'Extension'"
    assert "Path" in params, "Missing parameter 'Path'"
    assert "Created" in params, "Missing parameter 'Created'"

def test_attachment_has_AttachmentID():
    assert hasattr(Attachment, "AttachmentID")
    descriptor = None
    for klass in Attachment.__mro__:
        if "AttachmentID" in klass.__dict__:
            descriptor = klass.__dict__["AttachmentID"]
            break
    assert isinstance(descriptor, property)

def test_attachment_has_Name():
    assert hasattr(Attachment, "Name")
    descriptor = None
    for klass in Attachment.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_attachment_has_Project():
    assert hasattr(Attachment, "Project")
    descriptor = None
    for klass in Attachment.__mro__:
        if "Project" in klass.__dict__:
            descriptor = klass.__dict__["Project"]
            break
    assert isinstance(descriptor, property)

def test_attachment_has_User():
    assert hasattr(Attachment, "User")
    descriptor = None
    for klass in Attachment.__mro__:
        if "User" in klass.__dict__:
            descriptor = klass.__dict__["User"]
            break
    assert isinstance(descriptor, property)

def test_attachment_has_Size():
    assert hasattr(Attachment, "Size")
    descriptor = None
    for klass in Attachment.__mro__:
        if "Size" in klass.__dict__:
            descriptor = klass.__dict__["Size"]
            break
    assert isinstance(descriptor, property)

def test_attachment_has_Extension():
    assert hasattr(Attachment, "Extension")
    descriptor = None
    for klass in Attachment.__mro__:
        if "Extension" in klass.__dict__:
            descriptor = klass.__dict__["Extension"]
            break
    assert isinstance(descriptor, property)

def test_attachment_has_Path():
    assert hasattr(Attachment, "Path")
    descriptor = None
    for klass in Attachment.__mro__:
        if "Path" in klass.__dict__:
            descriptor = klass.__dict__["Path"]
            break
    assert isinstance(descriptor, property)

def test_attachment_has_Created():
    assert hasattr(Attachment, "Created")
    descriptor = None
    for klass in Attachment.__mro__:
        if "Created" in klass.__dict__:
            descriptor = klass.__dict__["Created"]
            break
    assert isinstance(descriptor, property)



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())
    assert "User" in params, "Missing parameter 'User'"
    assert "CommentID" in params, "Missing parameter 'CommentID'"
    assert "Created" in params, "Missing parameter 'Created'"
    assert "Content" in params, "Missing parameter 'Content'"
    assert "Project" in params, "Missing parameter 'Project'"

def test_comment_has_User():
    assert hasattr(Comment, "User")
    descriptor = None
    for klass in Comment.__mro__:
        if "User" in klass.__dict__:
            descriptor = klass.__dict__["User"]
            break
    assert isinstance(descriptor, property)

def test_comment_has_CommentID():
    assert hasattr(Comment, "CommentID")
    descriptor = None
    for klass in Comment.__mro__:
        if "CommentID" in klass.__dict__:
            descriptor = klass.__dict__["CommentID"]
            break
    assert isinstance(descriptor, property)

def test_comment_has_Created():
    assert hasattr(Comment, "Created")
    descriptor = None
    for klass in Comment.__mro__:
        if "Created" in klass.__dict__:
            descriptor = klass.__dict__["Created"]
            break
    assert isinstance(descriptor, property)

def test_comment_has_Content():
    assert hasattr(Comment, "Content")
    descriptor = None
    for klass in Comment.__mro__:
        if "Content" in klass.__dict__:
            descriptor = klass.__dict__["Content"]
            break
    assert isinstance(descriptor, property)

def test_comment_has_Project():
    assert hasattr(Comment, "Project")
    descriptor = None
    for klass in Comment.__mro__:
        if "Project" in klass.__dict__:
            descriptor = klass.__dict__["Project"]
            break
    assert isinstance(descriptor, property)



def test_activity_is_not_abstract():
    assert not inspect.isabstract(Activity)


def test_activity_constructor_exists():
    assert callable(Activity.__init__)


def test_activity_constructor_args():
    sig = inspect.signature(Activity.__init__)
    params = list(sig.parameters.keys())
    assert "ActivitySubType" in params, "Missing parameter 'ActivitySubType'"
    assert "ActivityID" in params, "Missing parameter 'ActivityID'"
    assert "NewValue" in params, "Missing parameter 'NewValue'"
    assert "Seen" in params, "Missing parameter 'Seen'"
    assert "Project" in params, "Missing parameter 'Project'"
    assert "PrevValue" in params, "Missing parameter 'PrevValue'"
    assert "User" in params, "Missing parameter 'User'"
    assert "ActivityType" in params, "Missing parameter 'ActivityType'"

def test_activity_has_ActivitySubType():
    assert hasattr(Activity, "ActivitySubType")
    descriptor = None
    for klass in Activity.__mro__:
        if "ActivitySubType" in klass.__dict__:
            descriptor = klass.__dict__["ActivitySubType"]
            break
    assert isinstance(descriptor, property)

def test_activity_has_ActivityID():
    assert hasattr(Activity, "ActivityID")
    descriptor = None
    for klass in Activity.__mro__:
        if "ActivityID" in klass.__dict__:
            descriptor = klass.__dict__["ActivityID"]
            break
    assert isinstance(descriptor, property)

def test_activity_has_NewValue():
    assert hasattr(Activity, "NewValue")
    descriptor = None
    for klass in Activity.__mro__:
        if "NewValue" in klass.__dict__:
            descriptor = klass.__dict__["NewValue"]
            break
    assert isinstance(descriptor, property)

def test_activity_has_Seen():
    assert hasattr(Activity, "Seen")
    descriptor = None
    for klass in Activity.__mro__:
        if "Seen" in klass.__dict__:
            descriptor = klass.__dict__["Seen"]
            break
    assert isinstance(descriptor, property)

def test_activity_has_Project():
    assert hasattr(Activity, "Project")
    descriptor = None
    for klass in Activity.__mro__:
        if "Project" in klass.__dict__:
            descriptor = klass.__dict__["Project"]
            break
    assert isinstance(descriptor, property)

def test_activity_has_PrevValue():
    assert hasattr(Activity, "PrevValue")
    descriptor = None
    for klass in Activity.__mro__:
        if "PrevValue" in klass.__dict__:
            descriptor = klass.__dict__["PrevValue"]
            break
    assert isinstance(descriptor, property)

def test_activity_has_User():
    assert hasattr(Activity, "User")
    descriptor = None
    for klass in Activity.__mro__:
        if "User" in klass.__dict__:
            descriptor = klass.__dict__["User"]
            break
    assert isinstance(descriptor, property)

def test_activity_has_ActivityType():
    assert hasattr(Activity, "ActivityType")
    descriptor = None
    for klass in Activity.__mro__:
        if "ActivityType" in klass.__dict__:
            descriptor = klass.__dict__["ActivityType"]
            break
    assert isinstance(descriptor, property)



def test_project_is_not_abstract():
    assert not inspect.isabstract(Project)


def test_project_constructor_exists():
    assert callable(Project.__init__)


def test_project_constructor_args():
    sig = inspect.signature(Project.__init__)
    params = list(sig.parameters.keys())
    assert "PorjectID" in params, "Missing parameter 'PorjectID'"
    assert "Comments___" in params, "Missing parameter 'Comments___'"
    assert "Attachments___" in params, "Missing parameter 'Attachments___'"
    assert "Assignee" in params, "Missing parameter 'Assignee'"
    assert "StatusID" in params, "Missing parameter 'StatusID'"
    assert "Author" in params, "Missing parameter 'Author'"
    assert "Created" in params, "Missing parameter 'Created'"
    assert "ProjectManager" in params, "Missing parameter 'ProjectManager'"
    assert "Deadline" in params, "Missing parameter 'Deadline'"
    assert "Activities___" in params, "Missing parameter 'Activities___'"
    assert "PriorityID" in params, "Missing parameter 'PriorityID'"
    assert "Title" in params, "Missing parameter 'Title'"
    assert "Description" in params, "Missing parameter 'Description'"
    assert "Subscriptions___" in params, "Missing parameter 'Subscriptions___'"
    assert "Team___" in params, "Missing parameter 'Team___'"

def test_project_has_PorjectID():
    assert hasattr(Project, "PorjectID")
    descriptor = None
    for klass in Project.__mro__:
        if "PorjectID" in klass.__dict__:
            descriptor = klass.__dict__["PorjectID"]
            break
    assert isinstance(descriptor, property)

def test_project_has_Comments___():
    assert hasattr(Project, "Comments___")
    descriptor = None
    for klass in Project.__mro__:
        if "Comments___" in klass.__dict__:
            descriptor = klass.__dict__["Comments___"]
            break
    assert isinstance(descriptor, property)

def test_project_has_Attachments___():
    assert hasattr(Project, "Attachments___")
    descriptor = None
    for klass in Project.__mro__:
        if "Attachments___" in klass.__dict__:
            descriptor = klass.__dict__["Attachments___"]
            break
    assert isinstance(descriptor, property)

def test_project_has_Assignee():
    assert hasattr(Project, "Assignee")
    descriptor = None
    for klass in Project.__mro__:
        if "Assignee" in klass.__dict__:
            descriptor = klass.__dict__["Assignee"]
            break
    assert isinstance(descriptor, property)

def test_project_has_StatusID():
    assert hasattr(Project, "StatusID")
    descriptor = None
    for klass in Project.__mro__:
        if "StatusID" in klass.__dict__:
            descriptor = klass.__dict__["StatusID"]
            break
    assert isinstance(descriptor, property)

def test_project_has_Author():
    assert hasattr(Project, "Author")
    descriptor = None
    for klass in Project.__mro__:
        if "Author" in klass.__dict__:
            descriptor = klass.__dict__["Author"]
            break
    assert isinstance(descriptor, property)

def test_project_has_Created():
    assert hasattr(Project, "Created")
    descriptor = None
    for klass in Project.__mro__:
        if "Created" in klass.__dict__:
            descriptor = klass.__dict__["Created"]
            break
    assert isinstance(descriptor, property)

def test_project_has_ProjectManager():
    assert hasattr(Project, "ProjectManager")
    descriptor = None
    for klass in Project.__mro__:
        if "ProjectManager" in klass.__dict__:
            descriptor = klass.__dict__["ProjectManager"]
            break
    assert isinstance(descriptor, property)

def test_project_has_Deadline():
    assert hasattr(Project, "Deadline")
    descriptor = None
    for klass in Project.__mro__:
        if "Deadline" in klass.__dict__:
            descriptor = klass.__dict__["Deadline"]
            break
    assert isinstance(descriptor, property)

def test_project_has_Activities___():
    assert hasattr(Project, "Activities___")
    descriptor = None
    for klass in Project.__mro__:
        if "Activities___" in klass.__dict__:
            descriptor = klass.__dict__["Activities___"]
            break
    assert isinstance(descriptor, property)

def test_project_has_PriorityID():
    assert hasattr(Project, "PriorityID")
    descriptor = None
    for klass in Project.__mro__:
        if "PriorityID" in klass.__dict__:
            descriptor = klass.__dict__["PriorityID"]
            break
    assert isinstance(descriptor, property)

def test_project_has_Title():
    assert hasattr(Project, "Title")
    descriptor = None
    for klass in Project.__mro__:
        if "Title" in klass.__dict__:
            descriptor = klass.__dict__["Title"]
            break
    assert isinstance(descriptor, property)

def test_project_has_Description():
    assert hasattr(Project, "Description")
    descriptor = None
    for klass in Project.__mro__:
        if "Description" in klass.__dict__:
            descriptor = klass.__dict__["Description"]
            break
    assert isinstance(descriptor, property)

def test_project_has_Subscriptions___():
    assert hasattr(Project, "Subscriptions___")
    descriptor = None
    for klass in Project.__mro__:
        if "Subscriptions___" in klass.__dict__:
            descriptor = klass.__dict__["Subscriptions___"]
            break
    assert isinstance(descriptor, property)

def test_project_has_Team___():
    assert hasattr(Project, "Team___")
    descriptor = None
    for klass in Project.__mro__:
        if "Team___" in klass.__dict__:
            descriptor = klass.__dict__["Team___"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "Email" in params, "Missing parameter 'Email'"
    assert "Roles___" in params, "Missing parameter 'Roles___'"
    assert "UserID" in params, "Missing parameter 'UserID'"
    assert "Phone" in params, "Missing parameter 'Phone'"
    assert "Google_plus_link" in params, "Missing parameter 'Google_plus_link'"
    assert "About" in params, "Missing parameter 'About'"
    assert "Settings" in params, "Missing parameter 'Settings'"
    assert "Dateofbirth" in params, "Missing parameter 'Dateofbirth'"
    assert "DepartmentID" in params, "Missing parameter 'DepartmentID'"
    assert "Position" in params, "Missing parameter 'Position'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "Linkedin_link" in params, "Missing parameter 'Linkedin_link'"
    assert "Active" in params, "Missing parameter 'Active'"
    assert "TitleID" in params, "Missing parameter 'TitleID'"
    assert "Firstname" in params, "Missing parameter 'Firstname'"
    assert "Lastname" in params, "Missing parameter 'Lastname'"
    assert "Hiredate" in params, "Missing parameter 'Hiredate'"
    assert "Facebook_link" in params, "Missing parameter 'Facebook_link'"
    assert "Username" in params, "Missing parameter 'Username'"

def test_user_has_Email():
    assert hasattr(User, "Email")
    descriptor = None
    for klass in User.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Roles___():
    assert hasattr(User, "Roles___")
    descriptor = None
    for klass in User.__mro__:
        if "Roles___" in klass.__dict__:
            descriptor = klass.__dict__["Roles___"]
            break
    assert isinstance(descriptor, property)

def test_user_has_UserID():
    assert hasattr(User, "UserID")
    descriptor = None
    for klass in User.__mro__:
        if "UserID" in klass.__dict__:
            descriptor = klass.__dict__["UserID"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Phone():
    assert hasattr(User, "Phone")
    descriptor = None
    for klass in User.__mro__:
        if "Phone" in klass.__dict__:
            descriptor = klass.__dict__["Phone"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Google_plus_link():
    assert hasattr(User, "Google_plus_link")
    descriptor = None
    for klass in User.__mro__:
        if "Google_plus_link" in klass.__dict__:
            descriptor = klass.__dict__["Google_plus_link"]
            break
    assert isinstance(descriptor, property)

def test_user_has_About():
    assert hasattr(User, "About")
    descriptor = None
    for klass in User.__mro__:
        if "About" in klass.__dict__:
            descriptor = klass.__dict__["About"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Settings():
    assert hasattr(User, "Settings")
    descriptor = None
    for klass in User.__mro__:
        if "Settings" in klass.__dict__:
            descriptor = klass.__dict__["Settings"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Dateofbirth():
    assert hasattr(User, "Dateofbirth")
    descriptor = None
    for klass in User.__mro__:
        if "Dateofbirth" in klass.__dict__:
            descriptor = klass.__dict__["Dateofbirth"]
            break
    assert isinstance(descriptor, property)

def test_user_has_DepartmentID():
    assert hasattr(User, "DepartmentID")
    descriptor = None
    for klass in User.__mro__:
        if "DepartmentID" in klass.__dict__:
            descriptor = klass.__dict__["DepartmentID"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Position():
    assert hasattr(User, "Position")
    descriptor = None
    for klass in User.__mro__:
        if "Position" in klass.__dict__:
            descriptor = klass.__dict__["Position"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Password():
    assert hasattr(User, "Password")
    descriptor = None
    for klass in User.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Linkedin_link():
    assert hasattr(User, "Linkedin_link")
    descriptor = None
    for klass in User.__mro__:
        if "Linkedin_link" in klass.__dict__:
            descriptor = klass.__dict__["Linkedin_link"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Active():
    assert hasattr(User, "Active")
    descriptor = None
    for klass in User.__mro__:
        if "Active" in klass.__dict__:
            descriptor = klass.__dict__["Active"]
            break
    assert isinstance(descriptor, property)

def test_user_has_TitleID():
    assert hasattr(User, "TitleID")
    descriptor = None
    for klass in User.__mro__:
        if "TitleID" in klass.__dict__:
            descriptor = klass.__dict__["TitleID"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Firstname():
    assert hasattr(User, "Firstname")
    descriptor = None
    for klass in User.__mro__:
        if "Firstname" in klass.__dict__:
            descriptor = klass.__dict__["Firstname"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Lastname():
    assert hasattr(User, "Lastname")
    descriptor = None
    for klass in User.__mro__:
        if "Lastname" in klass.__dict__:
            descriptor = klass.__dict__["Lastname"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Hiredate():
    assert hasattr(User, "Hiredate")
    descriptor = None
    for klass in User.__mro__:
        if "Hiredate" in klass.__dict__:
            descriptor = klass.__dict__["Hiredate"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Facebook_link():
    assert hasattr(User, "Facebook_link")
    descriptor = None
    for klass in User.__mro__:
        if "Facebook_link" in klass.__dict__:
            descriptor = klass.__dict__["Facebook_link"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Username():
    assert hasattr(User, "Username")
    descriptor = None
    for klass in User.__mro__:
        if "Username" in klass.__dict__:
            descriptor = klass.__dict__["Username"]
            break
    assert isinstance(descriptor, property)

def test_string_exists():
    # Check that the Enumeration exists
    assert String is not None

def test_string_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in String]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in String"


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
Role_strategy = st.builds(
    Role,
    Description=
        safe_text,
    Name=
        st.none(),
    RoleID=
        st.integers()
)
Attachment_strategy = st.builds(
    Attachment,
    AttachmentID=
        st.integers(),
    Name=
        safe_text,
    Project=
        st.none(),
    User=
        st.none(),
    Size=
        safe_text,
    Extension=
        safe_text,
    Path=
        safe_text,
    Created=
        safe_text
)
Comment_strategy = st.builds(
    Comment,
    User=
        st.none(),
    CommentID=
        st.integers(),
    Created=
        safe_text,
    Content=
        safe_text,
    Project=
        st.none()
)
Activity_strategy = st.builds(
    Activity,
    ActivitySubType=
        st.integers(),
    ActivityID=
        st.integers(),
    NewValue=
        safe_text,
    Seen=
        st.booleans(),
    Project=
        st.none(),
    PrevValue=
        safe_text,
    User=
        st.none(),
    ActivityType=
        st.integers()
)
Project_strategy = st.builds(
    Project,
    PorjectID=
        st.integers(),
    Comments___=
        safe_text,
    Attachments___=
        safe_text,
    Assignee=
        st.none(),
    StatusID=
        st.integers(),
    Author=
        st.none(),
    Created=
        safe_text,
    ProjectManager=
        st.none(),
    Deadline=
        safe_text,
    Activities___=
        safe_text,
    PriorityID=
        st.integers(),
    Title=
        safe_text,
    Description=
        safe_text,
    Subscriptions___=
        safe_text,
    Team___=
        safe_text
)
User_strategy = st.builds(
    User,
    Email=
        safe_text,
    Roles___=
        safe_text,
    UserID=
        st.integers(),
    Phone=
        safe_text,
    Google_plus_link=
        safe_text,
    About=
        safe_text,
    Settings=
        safe_text,
    Dateofbirth=
        safe_text,
    DepartmentID=
        st.integers(),
    Position=
        safe_text,
    Password=
        safe_text,
    Linkedin_link=
        safe_text,
    Active=
        st.booleans(),
    TitleID=
        st.integers(),
    Firstname=
        safe_text,
    Lastname=
        safe_text,
    Hiredate=
        safe_text,
    Facebook_link=
        safe_text,
    Username=
        safe_text
)

@given(instance=Role_strategy)
@settings(max_examples=50)
def test_role_instantiation(instance):
    assert isinstance(instance, Role)



@given(instance=Role_strategy)
def test_role_Description_setter(instance):
    original = instance.Description
    instance.Description = original
    assert instance.Description == original



@given(instance=Role_strategy)
def test_role_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Role_strategy)
def test_role_RoleID_setter(instance):
    original = instance.RoleID
    instance.RoleID = original
    assert instance.RoleID == original

@given(instance=Attachment_strategy)
@settings(max_examples=50)
def test_attachment_instantiation(instance):
    assert isinstance(instance, Attachment)



@given(instance=Attachment_strategy)
def test_attachment_AttachmentID_setter(instance):
    original = instance.AttachmentID
    instance.AttachmentID = original
    assert instance.AttachmentID == original



@given(instance=Attachment_strategy)
def test_attachment_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Attachment_strategy)
def test_attachment_Project_setter(instance):
    original = instance.Project
    instance.Project = original
    assert instance.Project == original



@given(instance=Attachment_strategy)
def test_attachment_User_setter(instance):
    original = instance.User
    instance.User = original
    assert instance.User == original



@given(instance=Attachment_strategy)
def test_attachment_Size_setter(instance):
    original = instance.Size
    instance.Size = original
    assert instance.Size == original



@given(instance=Attachment_strategy)
def test_attachment_Extension_setter(instance):
    original = instance.Extension
    instance.Extension = original
    assert instance.Extension == original



@given(instance=Attachment_strategy)
def test_attachment_Path_setter(instance):
    original = instance.Path
    instance.Path = original
    assert instance.Path == original



@given(instance=Attachment_strategy)
def test_attachment_Created_setter(instance):
    original = instance.Created
    instance.Created = original
    assert instance.Created == original

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)



@given(instance=Comment_strategy)
def test_comment_User_setter(instance):
    original = instance.User
    instance.User = original
    assert instance.User == original



@given(instance=Comment_strategy)
def test_comment_CommentID_setter(instance):
    original = instance.CommentID
    instance.CommentID = original
    assert instance.CommentID == original



@given(instance=Comment_strategy)
def test_comment_Created_setter(instance):
    original = instance.Created
    instance.Created = original
    assert instance.Created == original



@given(instance=Comment_strategy)
def test_comment_Content_setter(instance):
    original = instance.Content
    instance.Content = original
    assert instance.Content == original



@given(instance=Comment_strategy)
def test_comment_Project_setter(instance):
    original = instance.Project
    instance.Project = original
    assert instance.Project == original

@given(instance=Activity_strategy)
@settings(max_examples=50)
def test_activity_instantiation(instance):
    assert isinstance(instance, Activity)



@given(instance=Activity_strategy)
def test_activity_ActivitySubType_setter(instance):
    original = instance.ActivitySubType
    instance.ActivitySubType = original
    assert instance.ActivitySubType == original



@given(instance=Activity_strategy)
def test_activity_ActivityID_setter(instance):
    original = instance.ActivityID
    instance.ActivityID = original
    assert instance.ActivityID == original



@given(instance=Activity_strategy)
def test_activity_NewValue_setter(instance):
    original = instance.NewValue
    instance.NewValue = original
    assert instance.NewValue == original



@given(instance=Activity_strategy)
def test_activity_Seen_setter(instance):
    original = instance.Seen
    instance.Seen = original
    assert instance.Seen == original



@given(instance=Activity_strategy)
def test_activity_Project_setter(instance):
    original = instance.Project
    instance.Project = original
    assert instance.Project == original



@given(instance=Activity_strategy)
def test_activity_PrevValue_setter(instance):
    original = instance.PrevValue
    instance.PrevValue = original
    assert instance.PrevValue == original



@given(instance=Activity_strategy)
def test_activity_User_setter(instance):
    original = instance.User
    instance.User = original
    assert instance.User == original



@given(instance=Activity_strategy)
def test_activity_ActivityType_setter(instance):
    original = instance.ActivityType
    instance.ActivityType = original
    assert instance.ActivityType == original

@given(instance=Project_strategy)
@settings(max_examples=50)
def test_project_instantiation(instance):
    assert isinstance(instance, Project)



@given(instance=Project_strategy)
def test_project_PorjectID_setter(instance):
    original = instance.PorjectID
    instance.PorjectID = original
    assert instance.PorjectID == original



@given(instance=Project_strategy)
def test_project_Comments____setter(instance):
    original = instance.Comments___
    instance.Comments___ = original
    assert instance.Comments___ == original



@given(instance=Project_strategy)
def test_project_Attachments____setter(instance):
    original = instance.Attachments___
    instance.Attachments___ = original
    assert instance.Attachments___ == original



@given(instance=Project_strategy)
def test_project_Assignee_setter(instance):
    original = instance.Assignee
    instance.Assignee = original
    assert instance.Assignee == original



@given(instance=Project_strategy)
def test_project_StatusID_setter(instance):
    original = instance.StatusID
    instance.StatusID = original
    assert instance.StatusID == original



@given(instance=Project_strategy)
def test_project_Author_setter(instance):
    original = instance.Author
    instance.Author = original
    assert instance.Author == original



@given(instance=Project_strategy)
def test_project_Created_setter(instance):
    original = instance.Created
    instance.Created = original
    assert instance.Created == original



@given(instance=Project_strategy)
def test_project_ProjectManager_setter(instance):
    original = instance.ProjectManager
    instance.ProjectManager = original
    assert instance.ProjectManager == original



@given(instance=Project_strategy)
def test_project_Deadline_setter(instance):
    original = instance.Deadline
    instance.Deadline = original
    assert instance.Deadline == original



@given(instance=Project_strategy)
def test_project_Activities____setter(instance):
    original = instance.Activities___
    instance.Activities___ = original
    assert instance.Activities___ == original



@given(instance=Project_strategy)
def test_project_PriorityID_setter(instance):
    original = instance.PriorityID
    instance.PriorityID = original
    assert instance.PriorityID == original



@given(instance=Project_strategy)
def test_project_Title_setter(instance):
    original = instance.Title
    instance.Title = original
    assert instance.Title == original



@given(instance=Project_strategy)
def test_project_Description_setter(instance):
    original = instance.Description
    instance.Description = original
    assert instance.Description == original



@given(instance=Project_strategy)
def test_project_Subscriptions____setter(instance):
    original = instance.Subscriptions___
    instance.Subscriptions___ = original
    assert instance.Subscriptions___ == original



@given(instance=Project_strategy)
def test_project_Team____setter(instance):
    original = instance.Team___
    instance.Team___ = original
    assert instance.Team___ == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=User_strategy)
def test_user_Roles____setter(instance):
    original = instance.Roles___
    instance.Roles___ = original
    assert instance.Roles___ == original



@given(instance=User_strategy)
def test_user_UserID_setter(instance):
    original = instance.UserID
    instance.UserID = original
    assert instance.UserID == original



@given(instance=User_strategy)
def test_user_Phone_setter(instance):
    original = instance.Phone
    instance.Phone = original
    assert instance.Phone == original



@given(instance=User_strategy)
def test_user_Google_plus_link_setter(instance):
    original = instance.Google_plus_link
    instance.Google_plus_link = original
    assert instance.Google_plus_link == original



@given(instance=User_strategy)
def test_user_About_setter(instance):
    original = instance.About
    instance.About = original
    assert instance.About == original



@given(instance=User_strategy)
def test_user_Settings_setter(instance):
    original = instance.Settings
    instance.Settings = original
    assert instance.Settings == original



@given(instance=User_strategy)
def test_user_Dateofbirth_setter(instance):
    original = instance.Dateofbirth
    instance.Dateofbirth = original
    assert instance.Dateofbirth == original



@given(instance=User_strategy)
def test_user_DepartmentID_setter(instance):
    original = instance.DepartmentID
    instance.DepartmentID = original
    assert instance.DepartmentID == original



@given(instance=User_strategy)
def test_user_Position_setter(instance):
    original = instance.Position
    instance.Position = original
    assert instance.Position == original



@given(instance=User_strategy)
def test_user_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=User_strategy)
def test_user_Linkedin_link_setter(instance):
    original = instance.Linkedin_link
    instance.Linkedin_link = original
    assert instance.Linkedin_link == original



@given(instance=User_strategy)
def test_user_Active_setter(instance):
    original = instance.Active
    instance.Active = original
    assert instance.Active == original



@given(instance=User_strategy)
def test_user_TitleID_setter(instance):
    original = instance.TitleID
    instance.TitleID = original
    assert instance.TitleID == original



@given(instance=User_strategy)
def test_user_Firstname_setter(instance):
    original = instance.Firstname
    instance.Firstname = original
    assert instance.Firstname == original



@given(instance=User_strategy)
def test_user_Lastname_setter(instance):
    original = instance.Lastname
    instance.Lastname = original
    assert instance.Lastname == original



@given(instance=User_strategy)
def test_user_Hiredate_setter(instance):
    original = instance.Hiredate
    instance.Hiredate = original
    assert instance.Hiredate == original



@given(instance=User_strategy)
def test_user_Facebook_link_setter(instance):
    original = instance.Facebook_link
    instance.Facebook_link = original
    assert instance.Facebook_link == original



@given(instance=User_strategy)
def test_user_Username_setter(instance):
    original = instance.Username
    instance.Username = original
    assert instance.Username == original
