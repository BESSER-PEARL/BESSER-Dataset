import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Task,
    model::TaskSQL,
    model::TaskExport,
    model::TaskFile,
    model::TaskImport,
    IFile,
    SeparatedElement,
    model::File,
    Mapping,
    model::MappingExport,
    model::MappingSQL,
    model::MappingFile,
    model::MappingImport,
    model::Mapping,
    model::SCTFile,
    FQNamedElement,
    IColumn,
    model::Field,
    model::Column,
    model::SeparatedElement,
    model::FQNamedElement,
    model::DescribedElement,
    model::NamedElement,
    Type,
    model::Domain,
    model::NativeSQLType,
    DescribedElement,
    NamedElement,
    model::Database,
    model::View,
    model::Table,
    model::Schema,
    model::IColumn,
    model::Task,
    model::User,
    model::IFile,
    model::Site,
    model::TaskSet,
    model::FileSet,
    model::Type,
    FieldType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_task_is_not_abstract():
    assert not inspect.isabstract(Task)


def test_task_constructor_exists():
    assert callable(Task.__init__)


def test_task_constructor_args():
    sig = inspect.signature(Task.__init__)
    params = list(sig.parameters.keys())



def test_model::tasksql_is_not_abstract():
    assert not inspect.isabstract(model::TaskSQL)


def test_model::tasksql_constructor_exists():
    assert callable(model::TaskSQL.__init__)


def test_model::tasksql_constructor_args():
    sig = inspect.signature(model::TaskSQL.__init__)
    params = list(sig.parameters.keys())



def test_model::taskexport_is_not_abstract():
    assert not inspect.isabstract(model::TaskExport)


def test_model::taskexport_constructor_exists():
    assert callable(model::TaskExport.__init__)


def test_model::taskexport_constructor_args():
    sig = inspect.signature(model::TaskExport.__init__)
    params = list(sig.parameters.keys())



def test_model::taskfile_is_not_abstract():
    assert not inspect.isabstract(model::TaskFile)


def test_model::taskfile_constructor_exists():
    assert callable(model::TaskFile.__init__)


def test_model::taskfile_constructor_args():
    sig = inspect.signature(model::TaskFile.__init__)
    params = list(sig.parameters.keys())



def test_model::taskimport_is_not_abstract():
    assert not inspect.isabstract(model::TaskImport)


def test_model::taskimport_constructor_exists():
    assert callable(model::TaskImport.__init__)


def test_model::taskimport_constructor_args():
    sig = inspect.signature(model::TaskImport.__init__)
    params = list(sig.parameters.keys())



def test_ifile_is_not_abstract():
    assert not inspect.isabstract(IFile)


def test_ifile_constructor_exists():
    assert callable(IFile.__init__)


def test_ifile_constructor_args():
    sig = inspect.signature(IFile.__init__)
    params = list(sig.parameters.keys())



def test_separatedelement_is_not_abstract():
    assert not inspect.isabstract(SeparatedElement)


def test_separatedelement_constructor_exists():
    assert callable(SeparatedElement.__init__)


def test_separatedelement_constructor_args():
    sig = inspect.signature(SeparatedElement.__init__)
    params = list(sig.parameters.keys())



def test_model::file_is_not_abstract():
    assert not inspect.isabstract(model::File)


def test_model::file_constructor_exists():
    assert callable(model::File.__init__)


def test_model::file_constructor_args():
    sig = inspect.signature(model::File.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfHeaderLines" in params, "Missing parameter 'numberOfHeaderLines'"
    assert "files" in params, "Missing parameter 'files'"

def test_model::file_has_numberOfHeaderLines():
    assert hasattr(model::File, "numberOfHeaderLines")
    descriptor = None
    for klass in model::File.__mro__:
        if "numberOfHeaderLines" in klass.__dict__:
            descriptor = klass.__dict__["numberOfHeaderLines"]
            break
    assert isinstance(descriptor, property)

def test_model::file_has_files():
    assert hasattr(model::File, "files")
    descriptor = None
    for klass in model::File.__mro__:
        if "files" in klass.__dict__:
            descriptor = klass.__dict__["files"]
            break
    assert isinstance(descriptor, property)



def test_mapping_is_not_abstract():
    assert not inspect.isabstract(Mapping)


def test_mapping_constructor_exists():
    assert callable(Mapping.__init__)


def test_mapping_constructor_args():
    sig = inspect.signature(Mapping.__init__)
    params = list(sig.parameters.keys())



def test_model::mappingexport_is_not_abstract():
    assert not inspect.isabstract(model::MappingExport)


def test_model::mappingexport_constructor_exists():
    assert callable(model::MappingExport.__init__)


def test_model::mappingexport_constructor_args():
    sig = inspect.signature(model::MappingExport.__init__)
    params = list(sig.parameters.keys())



def test_model::mappingsql_is_not_abstract():
    assert not inspect.isabstract(model::MappingSQL)


def test_model::mappingsql_constructor_exists():
    assert callable(model::MappingSQL.__init__)


def test_model::mappingsql_constructor_args():
    sig = inspect.signature(model::MappingSQL.__init__)
    params = list(sig.parameters.keys())



def test_model::mappingfile_is_not_abstract():
    assert not inspect.isabstract(model::MappingFile)


def test_model::mappingfile_constructor_exists():
    assert callable(model::MappingFile.__init__)


def test_model::mappingfile_constructor_args():
    sig = inspect.signature(model::MappingFile.__init__)
    params = list(sig.parameters.keys())



def test_model::mappingimport_is_not_abstract():
    assert not inspect.isabstract(model::MappingImport)


def test_model::mappingimport_constructor_exists():
    assert callable(model::MappingImport.__init__)


def test_model::mappingimport_constructor_args():
    sig = inspect.signature(model::MappingImport.__init__)
    params = list(sig.parameters.keys())



def test_model::mapping_is_not_abstract():
    assert not inspect.isabstract(model::Mapping)


def test_model::mapping_constructor_exists():
    assert callable(model::Mapping.__init__)


def test_model::mapping_constructor_args():
    sig = inspect.signature(model::Mapping.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_model::mapping_has_expression():
    assert hasattr(model::Mapping, "expression")
    descriptor = None
    for klass in model::Mapping.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_model::sctfile_is_not_abstract():
    assert not inspect.isabstract(model::SCTFile)


def test_model::sctfile_constructor_exists():
    assert callable(model::SCTFile.__init__)


def test_model::sctfile_constructor_args():
    sig = inspect.signature(model::SCTFile.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"

def test_model::sctfile_has_file():
    assert hasattr(model::SCTFile, "file")
    descriptor = None
    for klass in model::SCTFile.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)



def test_fqnamedelement_is_not_abstract():
    assert not inspect.isabstract(FQNamedElement)


def test_fqnamedelement_constructor_exists():
    assert callable(FQNamedElement.__init__)


def test_fqnamedelement_constructor_args():
    sig = inspect.signature(FQNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_icolumn_is_not_abstract():
    assert not inspect.isabstract(IColumn)


def test_icolumn_constructor_exists():
    assert callable(IColumn.__init__)


def test_icolumn_constructor_args():
    sig = inspect.signature(IColumn.__init__)
    params = list(sig.parameters.keys())



def test_model::field_is_not_abstract():
    assert not inspect.isabstract(model::Field)


def test_model::field_constructor_exists():
    assert callable(model::Field.__init__)


def test_model::field_constructor_args():
    sig = inspect.signature(model::Field.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "type" in params, "Missing parameter 'type'"
    assert "position" in params, "Missing parameter 'position'"

def test_model::field_has_length():
    assert hasattr(model::Field, "length")
    descriptor = None
    for klass in model::Field.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_model::field_has_type():
    assert hasattr(model::Field, "type")
    descriptor = None
    for klass in model::Field.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_model::field_has_position():
    assert hasattr(model::Field, "position")
    descriptor = None
    for klass in model::Field.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_model::column_is_not_abstract():
    assert not inspect.isabstract(model::Column)


def test_model::column_constructor_exists():
    assert callable(model::Column.__init__)


def test_model::column_constructor_args():
    sig = inspect.signature(model::Column.__init__)
    params = list(sig.parameters.keys())



def test_model::separatedelement_is_not_abstract():
    assert not inspect.isabstract(model::SeparatedElement)


def test_model::separatedelement_constructor_exists():
    assert callable(model::SeparatedElement.__init__)


def test_model::separatedelement_constructor_args():
    sig = inspect.signature(model::SeparatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "separator" in params, "Missing parameter 'separator'"

def test_model::separatedelement_has_separator():
    assert hasattr(model::SeparatedElement, "separator")
    descriptor = None
    for klass in model::SeparatedElement.__mro__:
        if "separator" in klass.__dict__:
            descriptor = klass.__dict__["separator"]
            break
    assert isinstance(descriptor, property)



def test_model::fqnamedelement_is_not_abstract():
    assert not inspect.isabstract(model::FQNamedElement)


def test_model::fqnamedelement_constructor_exists():
    assert callable(model::FQNamedElement.__init__)


def test_model::fqnamedelement_constructor_args():
    sig = inspect.signature(model::FQNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_model::describedelement_is_not_abstract():
    assert not inspect.isabstract(model::DescribedElement)


def test_model::describedelement_constructor_exists():
    assert callable(model::DescribedElement.__init__)


def test_model::describedelement_constructor_args():
    sig = inspect.signature(model::DescribedElement.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_model::describedelement_has_description():
    assert hasattr(model::DescribedElement, "description")
    descriptor = None
    for klass in model::DescribedElement.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_model::namedelement_is_not_abstract():
    assert not inspect.isabstract(model::NamedElement)


def test_model::namedelement_constructor_exists():
    assert callable(model::NamedElement.__init__)


def test_model::namedelement_constructor_args():
    sig = inspect.signature(model::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model::namedelement_has_name():
    assert hasattr(model::NamedElement, "name")
    descriptor = None
    for klass in model::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_model::domain_is_not_abstract():
    assert not inspect.isabstract(model::Domain)


def test_model::domain_constructor_exists():
    assert callable(model::Domain.__init__)


def test_model::domain_constructor_args():
    sig = inspect.signature(model::Domain.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_model::domain_has_type():
    assert hasattr(model::Domain, "type")
    descriptor = None
    for klass in model::Domain.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_model::nativesqltype_is_not_abstract():
    assert not inspect.isabstract(model::NativeSQLType)


def test_model::nativesqltype_constructor_exists():
    assert callable(model::NativeSQLType.__init__)


def test_model::nativesqltype_constructor_args():
    sig = inspect.signature(model::NativeSQLType.__init__)
    params = list(sig.parameters.keys())



def test_describedelement_is_not_abstract():
    assert not inspect.isabstract(DescribedElement)


def test_describedelement_constructor_exists():
    assert callable(DescribedElement.__init__)


def test_describedelement_constructor_args():
    sig = inspect.signature(DescribedElement.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_model::database_is_not_abstract():
    assert not inspect.isabstract(model::Database)


def test_model::database_constructor_exists():
    assert callable(model::Database.__init__)


def test_model::database_constructor_args():
    sig = inspect.signature(model::Database.__init__)
    params = list(sig.parameters.keys())
    assert "dsn" in params, "Missing parameter 'dsn'"

def test_model::database_has_dsn():
    assert hasattr(model::Database, "dsn")
    descriptor = None
    for klass in model::Database.__mro__:
        if "dsn" in klass.__dict__:
            descriptor = klass.__dict__["dsn"]
            break
    assert isinstance(descriptor, property)



def test_model::view_is_not_abstract():
    assert not inspect.isabstract(model::View)


def test_model::view_constructor_exists():
    assert callable(model::View.__init__)


def test_model::view_constructor_args():
    sig = inspect.signature(model::View.__init__)
    params = list(sig.parameters.keys())
    assert "sql" in params, "Missing parameter 'sql'"

def test_model::view_has_sql():
    assert hasattr(model::View, "sql")
    descriptor = None
    for klass in model::View.__mro__:
        if "sql" in klass.__dict__:
            descriptor = klass.__dict__["sql"]
            break
    assert isinstance(descriptor, property)



def test_model::table_is_not_abstract():
    assert not inspect.isabstract(model::Table)


def test_model::table_constructor_exists():
    assert callable(model::Table.__init__)


def test_model::table_constructor_args():
    sig = inspect.signature(model::Table.__init__)
    params = list(sig.parameters.keys())



def test_model::schema_is_not_abstract():
    assert not inspect.isabstract(model::Schema)


def test_model::schema_constructor_exists():
    assert callable(model::Schema.__init__)


def test_model::schema_constructor_args():
    sig = inspect.signature(model::Schema.__init__)
    params = list(sig.parameters.keys())



def test_model::icolumn_is_not_abstract():
    assert not inspect.isabstract(model::IColumn)


def test_model::icolumn_constructor_exists():
    assert callable(model::IColumn.__init__)


def test_model::icolumn_constructor_args():
    sig = inspect.signature(model::IColumn.__init__)
    params = list(sig.parameters.keys())



def test_model::task_is_not_abstract():
    assert not inspect.isabstract(model::Task)


def test_model::task_constructor_exists():
    assert callable(model::Task.__init__)


def test_model::task_constructor_args():
    sig = inspect.signature(model::Task.__init__)
    params = list(sig.parameters.keys())
    assert "fileName" in params, "Missing parameter 'fileName'"

def test_model::task_has_fileName():
    assert hasattr(model::Task, "fileName")
    descriptor = None
    for klass in model::Task.__mro__:
        if "fileName" in klass.__dict__:
            descriptor = klass.__dict__["fileName"]
            break
    assert isinstance(descriptor, property)



def test_model::user_is_not_abstract():
    assert not inspect.isabstract(model::User)


def test_model::user_constructor_exists():
    assert callable(model::User.__init__)


def test_model::user_constructor_args():
    sig = inspect.signature(model::User.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"

def test_model::user_has_password():
    assert hasattr(model::User, "password")
    descriptor = None
    for klass in model::User.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)



def test_model::ifile_is_not_abstract():
    assert not inspect.isabstract(model::IFile)


def test_model::ifile_constructor_exists():
    assert callable(model::IFile.__init__)


def test_model::ifile_constructor_args():
    sig = inspect.signature(model::IFile.__init__)
    params = list(sig.parameters.keys())



def test_model::site_is_not_abstract():
    assert not inspect.isabstract(model::Site)


def test_model::site_constructor_exists():
    assert callable(model::Site.__init__)


def test_model::site_constructor_args():
    sig = inspect.signature(model::Site.__init__)
    params = list(sig.parameters.keys())



def test_model::taskset_is_not_abstract():
    assert not inspect.isabstract(model::TaskSet)


def test_model::taskset_constructor_exists():
    assert callable(model::TaskSet.__init__)


def test_model::taskset_constructor_args():
    sig = inspect.signature(model::TaskSet.__init__)
    params = list(sig.parameters.keys())



def test_model::fileset_is_not_abstract():
    assert not inspect.isabstract(model::FileSet)


def test_model::fileset_constructor_exists():
    assert callable(model::FileSet.__init__)


def test_model::fileset_constructor_args():
    sig = inspect.signature(model::FileSet.__init__)
    params = list(sig.parameters.keys())
    assert "hostname" in params, "Missing parameter 'hostname'"

def test_model::fileset_has_hostname():
    assert hasattr(model::FileSet, "hostname")
    descriptor = None
    for klass in model::FileSet.__mro__:
        if "hostname" in klass.__dict__:
            descriptor = klass.__dict__["hostname"]
            break
    assert isinstance(descriptor, property)



def test_model::type_is_not_abstract():
    assert not inspect.isabstract(model::Type)


def test_model::type_constructor_exists():
    assert callable(model::Type.__init__)


def test_model::type_constructor_args():
    sig = inspect.signature(model::Type.__init__)
    params = list(sig.parameters.keys())

def test_fieldtype_exists():
    # Check that the Enumeration exists
    assert FieldType is not None

def test_fieldtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FieldType]
    expected_literals = [
        "ABSOLUTE",
        "RELATIVE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FieldType"


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
Task_strategy = st.builds(
    Task,
)
model::TaskSQL_strategy = st.builds(
    model::TaskSQL,
)
model::TaskExport_strategy = st.builds(
    model::TaskExport,
)
model::TaskFile_strategy = st.builds(
    model::TaskFile,
)
model::TaskImport_strategy = st.builds(
    model::TaskImport,
)
IFile_strategy = st.builds(
    IFile,
)
SeparatedElement_strategy = st.builds(
    SeparatedElement,
)
model::File_strategy = st.builds(
    model::File,
    numberOfHeaderLines=
        safe_text,
    files=
        safe_text
)
Mapping_strategy = st.builds(
    Mapping,
)
model::MappingExport_strategy = st.builds(
    model::MappingExport,
)
model::MappingSQL_strategy = st.builds(
    model::MappingSQL,
)
model::MappingFile_strategy = st.builds(
    model::MappingFile,
)
model::MappingImport_strategy = st.builds(
    model::MappingImport,
)
model::Mapping_strategy = st.builds(
    model::Mapping,
    expression=
        safe_text
)
model::SCTFile_strategy = st.builds(
    model::SCTFile,
    file=
        safe_text
)
FQNamedElement_strategy = st.builds(
    FQNamedElement,
)
IColumn_strategy = st.builds(
    IColumn,
)
model::Field_strategy = st.builds(
    model::Field,
    length=
        safe_text,
    type=
        safe_text,
    position=
        safe_text
)
model::Column_strategy = st.builds(
    model::Column,
)
model::SeparatedElement_strategy = st.builds(
    model::SeparatedElement,
    separator=
        safe_text
)
model::FQNamedElement_strategy = st.builds(
    model::FQNamedElement,
)
model::DescribedElement_strategy = st.builds(
    model::DescribedElement,
    description=
        safe_text
)
model::NamedElement_strategy = st.builds(
    model::NamedElement,
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
model::Domain_strategy = st.builds(
    model::Domain,
    type=
        safe_text
)
model::NativeSQLType_strategy = st.builds(
    model::NativeSQLType,
)
DescribedElement_strategy = st.builds(
    DescribedElement,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
model::Database_strategy = st.builds(
    model::Database,
    dsn=
        safe_text
)
model::View_strategy = st.builds(
    model::View,
    sql=
        safe_text
)
model::Table_strategy = st.builds(
    model::Table,
)
model::Schema_strategy = st.builds(
    model::Schema,
)
model::IColumn_strategy = st.builds(
    model::IColumn,
)
model::Task_strategy = st.builds(
    model::Task,
    fileName=
        safe_text
)
model::User_strategy = st.builds(
    model::User,
    password=
        safe_text
)
model::IFile_strategy = st.builds(
    model::IFile,
)
model::Site_strategy = st.builds(
    model::Site,
)
model::TaskSet_strategy = st.builds(
    model::TaskSet,
)
model::FileSet_strategy = st.builds(
    model::FileSet,
    hostname=
        safe_text
)
model::Type_strategy = st.builds(
    model::Type,
)

@given(instance=Task_strategy)
@settings(max_examples=50)
def test_task_instantiation(instance):
    assert isinstance(instance, Task)

@given(instance=model::TaskSQL_strategy)
@settings(max_examples=50)
def test_model::tasksql_instantiation(instance):
    assert isinstance(instance, model::TaskSQL)

@given(instance=model::TaskExport_strategy)
@settings(max_examples=50)
def test_model::taskexport_instantiation(instance):
    assert isinstance(instance, model::TaskExport)

@given(instance=model::TaskFile_strategy)
@settings(max_examples=50)
def test_model::taskfile_instantiation(instance):
    assert isinstance(instance, model::TaskFile)

@given(instance=model::TaskImport_strategy)
@settings(max_examples=50)
def test_model::taskimport_instantiation(instance):
    assert isinstance(instance, model::TaskImport)

@given(instance=IFile_strategy)
@settings(max_examples=50)
def test_ifile_instantiation(instance):
    assert isinstance(instance, IFile)

@given(instance=SeparatedElement_strategy)
@settings(max_examples=50)
def test_separatedelement_instantiation(instance):
    assert isinstance(instance, SeparatedElement)

@given(instance=model::File_strategy)
@settings(max_examples=50)
def test_model::file_instantiation(instance):
    assert isinstance(instance, model::File)

@given(instance=model::File_strategy)
def test_model::file_numberOfHeaderLines_type(instance):
    assert isinstance(instance.numberOfHeaderLines, str)


@given(instance=model::File_strategy)
def test_model::file_numberOfHeaderLines_setter(instance):
    original = instance.numberOfHeaderLines
    instance.numberOfHeaderLines = original
    assert instance.numberOfHeaderLines == original

@given(instance=model::File_strategy)
def test_model::file_files_type(instance):
    assert isinstance(instance.files, str)


@given(instance=model::File_strategy)
def test_model::file_files_setter(instance):
    original = instance.files
    instance.files = original
    assert instance.files == original

@given(instance=Mapping_strategy)
@settings(max_examples=50)
def test_mapping_instantiation(instance):
    assert isinstance(instance, Mapping)

@given(instance=model::MappingExport_strategy)
@settings(max_examples=50)
def test_model::mappingexport_instantiation(instance):
    assert isinstance(instance, model::MappingExport)

@given(instance=model::MappingSQL_strategy)
@settings(max_examples=50)
def test_model::mappingsql_instantiation(instance):
    assert isinstance(instance, model::MappingSQL)

@given(instance=model::MappingFile_strategy)
@settings(max_examples=50)
def test_model::mappingfile_instantiation(instance):
    assert isinstance(instance, model::MappingFile)

@given(instance=model::MappingImport_strategy)
@settings(max_examples=50)
def test_model::mappingimport_instantiation(instance):
    assert isinstance(instance, model::MappingImport)

@given(instance=model::Mapping_strategy)
@settings(max_examples=50)
def test_model::mapping_instantiation(instance):
    assert isinstance(instance, model::Mapping)

@given(instance=model::Mapping_strategy)
def test_model::mapping_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=model::Mapping_strategy)
def test_model::mapping_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=model::SCTFile_strategy)
@settings(max_examples=50)
def test_model::sctfile_instantiation(instance):
    assert isinstance(instance, model::SCTFile)

@given(instance=model::SCTFile_strategy)
def test_model::sctfile_file_type(instance):
    assert isinstance(instance.file, str)


@given(instance=model::SCTFile_strategy)
def test_model::sctfile_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=FQNamedElement_strategy)
@settings(max_examples=50)
def test_fqnamedelement_instantiation(instance):
    assert isinstance(instance, FQNamedElement)

@given(instance=IColumn_strategy)
@settings(max_examples=50)
def test_icolumn_instantiation(instance):
    assert isinstance(instance, IColumn)

@given(instance=model::Field_strategy)
@settings(max_examples=50)
def test_model::field_instantiation(instance):
    assert isinstance(instance, model::Field)

@given(instance=model::Field_strategy)
def test_model::field_length_type(instance):
    assert isinstance(instance.length, str)


@given(instance=model::Field_strategy)
def test_model::field_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=model::Field_strategy)
def test_model::field_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=model::Field_strategy)
def test_model::field_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=model::Field_strategy)
def test_model::field_position_type(instance):
    assert isinstance(instance.position, str)


@given(instance=model::Field_strategy)
def test_model::field_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=model::Column_strategy)
@settings(max_examples=50)
def test_model::column_instantiation(instance):
    assert isinstance(instance, model::Column)

@given(instance=model::SeparatedElement_strategy)
@settings(max_examples=50)
def test_model::separatedelement_instantiation(instance):
    assert isinstance(instance, model::SeparatedElement)

@given(instance=model::SeparatedElement_strategy)
def test_model::separatedelement_separator_type(instance):
    assert isinstance(instance.separator, str)


@given(instance=model::SeparatedElement_strategy)
def test_model::separatedelement_separator_setter(instance):
    original = instance.separator
    instance.separator = original
    assert instance.separator == original

@given(instance=model::FQNamedElement_strategy)
@settings(max_examples=50)
def test_model::fqnamedelement_instantiation(instance):
    assert isinstance(instance, model::FQNamedElement)

@given(instance=model::DescribedElement_strategy)
@settings(max_examples=50)
def test_model::describedelement_instantiation(instance):
    assert isinstance(instance, model::DescribedElement)

@given(instance=model::DescribedElement_strategy)
def test_model::describedelement_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=model::DescribedElement_strategy)
def test_model::describedelement_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=model::NamedElement_strategy)
@settings(max_examples=50)
def test_model::namedelement_instantiation(instance):
    assert isinstance(instance, model::NamedElement)

@given(instance=model::NamedElement_strategy)
def test_model::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::NamedElement_strategy)
def test_model::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=model::Domain_strategy)
@settings(max_examples=50)
def test_model::domain_instantiation(instance):
    assert isinstance(instance, model::Domain)

@given(instance=model::Domain_strategy)
def test_model::domain_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=model::Domain_strategy)
def test_model::domain_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=model::NativeSQLType_strategy)
@settings(max_examples=50)
def test_model::nativesqltype_instantiation(instance):
    assert isinstance(instance, model::NativeSQLType)

@given(instance=DescribedElement_strategy)
@settings(max_examples=50)
def test_describedelement_instantiation(instance):
    assert isinstance(instance, DescribedElement)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=model::Database_strategy)
@settings(max_examples=50)
def test_model::database_instantiation(instance):
    assert isinstance(instance, model::Database)

@given(instance=model::Database_strategy)
def test_model::database_dsn_type(instance):
    assert isinstance(instance.dsn, str)


@given(instance=model::Database_strategy)
def test_model::database_dsn_setter(instance):
    original = instance.dsn
    instance.dsn = original
    assert instance.dsn == original

@given(instance=model::View_strategy)
@settings(max_examples=50)
def test_model::view_instantiation(instance):
    assert isinstance(instance, model::View)

@given(instance=model::View_strategy)
def test_model::view_sql_type(instance):
    assert isinstance(instance.sql, str)


@given(instance=model::View_strategy)
def test_model::view_sql_setter(instance):
    original = instance.sql
    instance.sql = original
    assert instance.sql == original

@given(instance=model::Table_strategy)
@settings(max_examples=50)
def test_model::table_instantiation(instance):
    assert isinstance(instance, model::Table)

@given(instance=model::Schema_strategy)
@settings(max_examples=50)
def test_model::schema_instantiation(instance):
    assert isinstance(instance, model::Schema)

@given(instance=model::IColumn_strategy)
@settings(max_examples=50)
def test_model::icolumn_instantiation(instance):
    assert isinstance(instance, model::IColumn)

@given(instance=model::Task_strategy)
@settings(max_examples=50)
def test_model::task_instantiation(instance):
    assert isinstance(instance, model::Task)

@given(instance=model::Task_strategy)
def test_model::task_fileName_type(instance):
    assert isinstance(instance.fileName, str)


@given(instance=model::Task_strategy)
def test_model::task_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original

@given(instance=model::User_strategy)
@settings(max_examples=50)
def test_model::user_instantiation(instance):
    assert isinstance(instance, model::User)

@given(instance=model::User_strategy)
def test_model::user_password_type(instance):
    assert isinstance(instance.password, str)


@given(instance=model::User_strategy)
def test_model::user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=model::IFile_strategy)
@settings(max_examples=50)
def test_model::ifile_instantiation(instance):
    assert isinstance(instance, model::IFile)

@given(instance=model::Site_strategy)
@settings(max_examples=50)
def test_model::site_instantiation(instance):
    assert isinstance(instance, model::Site)

@given(instance=model::TaskSet_strategy)
@settings(max_examples=50)
def test_model::taskset_instantiation(instance):
    assert isinstance(instance, model::TaskSet)

@given(instance=model::FileSet_strategy)
@settings(max_examples=50)
def test_model::fileset_instantiation(instance):
    assert isinstance(instance, model::FileSet)

@given(instance=model::FileSet_strategy)
def test_model::fileset_hostname_type(instance):
    assert isinstance(instance.hostname, str)


@given(instance=model::FileSet_strategy)
def test_model::fileset_hostname_setter(instance):
    original = instance.hostname
    instance.hostname = original
    assert instance.hostname == original

@given(instance=model::Type_strategy)
@settings(max_examples=50)
def test_model::type_instantiation(instance):
    assert isinstance(instance, model::Type)
