import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Task,
    model_TaskExport,
    model_TaskFile,
    model_TaskSQL,
    model_TaskImport,
    IFile,
    SeparatedElement,
    model_File,
    Mapping,
    model_MappingExport,
    model_MappingFile,
    model_MappingSQL,
    model_MappingImport,
    model_Mapping,
    model_SCTFile,
    FQNamedElement,
    IColumn,
    model_Field,
    model_Column,
    model_SeparatedElement,
    model_FQNamedElement,
    model_DescribedElement,
    model_NamedElement,
    Type,
    model_Domain,
    model_NativeSQLType,
    DescribedElement,
    NamedElement,
    model_Table,
    model_TaskSet,
    model_View,
    model_IFile,
    model_User,
    model_Schema,
    model_Site,
    model_FileSet,
    model_IColumn,
    model_Task,
    model_Database,
    model_Type,
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



def test_model_taskexport_is_not_abstract():
    assert not inspect.isabstract(model_TaskExport)


def test_model_taskexport_constructor_exists():
    assert callable(model_TaskExport.__init__)


def test_model_taskexport_constructor_args():
    sig = inspect.signature(model_TaskExport.__init__)
    params = list(sig.parameters.keys())



def test_model_taskfile_is_not_abstract():
    assert not inspect.isabstract(model_TaskFile)


def test_model_taskfile_constructor_exists():
    assert callable(model_TaskFile.__init__)


def test_model_taskfile_constructor_args():
    sig = inspect.signature(model_TaskFile.__init__)
    params = list(sig.parameters.keys())



def test_model_tasksql_is_not_abstract():
    assert not inspect.isabstract(model_TaskSQL)


def test_model_tasksql_constructor_exists():
    assert callable(model_TaskSQL.__init__)


def test_model_tasksql_constructor_args():
    sig = inspect.signature(model_TaskSQL.__init__)
    params = list(sig.parameters.keys())



def test_model_taskimport_is_not_abstract():
    assert not inspect.isabstract(model_TaskImport)


def test_model_taskimport_constructor_exists():
    assert callable(model_TaskImport.__init__)


def test_model_taskimport_constructor_args():
    sig = inspect.signature(model_TaskImport.__init__)
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



def test_model_file_is_not_abstract():
    assert not inspect.isabstract(model_File)


def test_model_file_constructor_exists():
    assert callable(model_File.__init__)


def test_model_file_constructor_args():
    sig = inspect.signature(model_File.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfHeaderLines" in params, "Missing parameter 'numberOfHeaderLines'"
    assert "files" in params, "Missing parameter 'files'"

def test_model_file_has_numberOfHeaderLines():
    assert hasattr(model_File, "numberOfHeaderLines")
    descriptor = None
    for klass in model_File.__mro__:
        if "numberOfHeaderLines" in klass.__dict__:
            descriptor = klass.__dict__["numberOfHeaderLines"]
            break
    assert isinstance(descriptor, property)

def test_model_file_has_files():
    assert hasattr(model_File, "files")
    descriptor = None
    for klass in model_File.__mro__:
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



def test_model_mappingexport_is_not_abstract():
    assert not inspect.isabstract(model_MappingExport)


def test_model_mappingexport_constructor_exists():
    assert callable(model_MappingExport.__init__)


def test_model_mappingexport_constructor_args():
    sig = inspect.signature(model_MappingExport.__init__)
    params = list(sig.parameters.keys())



def test_model_mappingfile_is_not_abstract():
    assert not inspect.isabstract(model_MappingFile)


def test_model_mappingfile_constructor_exists():
    assert callable(model_MappingFile.__init__)


def test_model_mappingfile_constructor_args():
    sig = inspect.signature(model_MappingFile.__init__)
    params = list(sig.parameters.keys())



def test_model_mappingsql_is_not_abstract():
    assert not inspect.isabstract(model_MappingSQL)


def test_model_mappingsql_constructor_exists():
    assert callable(model_MappingSQL.__init__)


def test_model_mappingsql_constructor_args():
    sig = inspect.signature(model_MappingSQL.__init__)
    params = list(sig.parameters.keys())



def test_model_mappingimport_is_not_abstract():
    assert not inspect.isabstract(model_MappingImport)


def test_model_mappingimport_constructor_exists():
    assert callable(model_MappingImport.__init__)


def test_model_mappingimport_constructor_args():
    sig = inspect.signature(model_MappingImport.__init__)
    params = list(sig.parameters.keys())



def test_model_mapping_is_not_abstract():
    assert not inspect.isabstract(model_Mapping)


def test_model_mapping_constructor_exists():
    assert callable(model_Mapping.__init__)


def test_model_mapping_constructor_args():
    sig = inspect.signature(model_Mapping.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_model_mapping_has_expression():
    assert hasattr(model_Mapping, "expression")
    descriptor = None
    for klass in model_Mapping.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_model_sctfile_is_not_abstract():
    assert not inspect.isabstract(model_SCTFile)


def test_model_sctfile_constructor_exists():
    assert callable(model_SCTFile.__init__)


def test_model_sctfile_constructor_args():
    sig = inspect.signature(model_SCTFile.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"

def test_model_sctfile_has_file():
    assert hasattr(model_SCTFile, "file")
    descriptor = None
    for klass in model_SCTFile.__mro__:
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



def test_model_field_is_not_abstract():
    assert not inspect.isabstract(model_Field)


def test_model_field_constructor_exists():
    assert callable(model_Field.__init__)


def test_model_field_constructor_args():
    sig = inspect.signature(model_Field.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"
    assert "type" in params, "Missing parameter 'type'"
    assert "length" in params, "Missing parameter 'length'"

def test_model_field_has_position():
    assert hasattr(model_Field, "position")
    descriptor = None
    for klass in model_Field.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_model_field_has_type():
    assert hasattr(model_Field, "type")
    descriptor = None
    for klass in model_Field.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_model_field_has_length():
    assert hasattr(model_Field, "length")
    descriptor = None
    for klass in model_Field.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_model_column_is_not_abstract():
    assert not inspect.isabstract(model_Column)


def test_model_column_constructor_exists():
    assert callable(model_Column.__init__)


def test_model_column_constructor_args():
    sig = inspect.signature(model_Column.__init__)
    params = list(sig.parameters.keys())



def test_model_separatedelement_is_not_abstract():
    assert not inspect.isabstract(model_SeparatedElement)


def test_model_separatedelement_constructor_exists():
    assert callable(model_SeparatedElement.__init__)


def test_model_separatedelement_constructor_args():
    sig = inspect.signature(model_SeparatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "separator" in params, "Missing parameter 'separator'"

def test_model_separatedelement_has_separator():
    assert hasattr(model_SeparatedElement, "separator")
    descriptor = None
    for klass in model_SeparatedElement.__mro__:
        if "separator" in klass.__dict__:
            descriptor = klass.__dict__["separator"]
            break
    assert isinstance(descriptor, property)



def test_model_fqnamedelement_is_not_abstract():
    assert not inspect.isabstract(model_FQNamedElement)


def test_model_fqnamedelement_constructor_exists():
    assert callable(model_FQNamedElement.__init__)


def test_model_fqnamedelement_constructor_args():
    sig = inspect.signature(model_FQNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_model_describedelement_is_not_abstract():
    assert not inspect.isabstract(model_DescribedElement)


def test_model_describedelement_constructor_exists():
    assert callable(model_DescribedElement.__init__)


def test_model_describedelement_constructor_args():
    sig = inspect.signature(model_DescribedElement.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_model_describedelement_has_description():
    assert hasattr(model_DescribedElement, "description")
    descriptor = None
    for klass in model_DescribedElement.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_model_namedelement_is_not_abstract():
    assert not inspect.isabstract(model_NamedElement)


def test_model_namedelement_constructor_exists():
    assert callable(model_NamedElement.__init__)


def test_model_namedelement_constructor_args():
    sig = inspect.signature(model_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model_namedelement_has_name():
    assert hasattr(model_NamedElement, "name")
    descriptor = None
    for klass in model_NamedElement.__mro__:
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



def test_model_domain_is_not_abstract():
    assert not inspect.isabstract(model_Domain)


def test_model_domain_constructor_exists():
    assert callable(model_Domain.__init__)


def test_model_domain_constructor_args():
    sig = inspect.signature(model_Domain.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_model_domain_has_type():
    assert hasattr(model_Domain, "type")
    descriptor = None
    for klass in model_Domain.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_model_nativesqltype_is_not_abstract():
    assert not inspect.isabstract(model_NativeSQLType)


def test_model_nativesqltype_constructor_exists():
    assert callable(model_NativeSQLType.__init__)


def test_model_nativesqltype_constructor_args():
    sig = inspect.signature(model_NativeSQLType.__init__)
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



def test_model_table_is_not_abstract():
    assert not inspect.isabstract(model_Table)


def test_model_table_constructor_exists():
    assert callable(model_Table.__init__)


def test_model_table_constructor_args():
    sig = inspect.signature(model_Table.__init__)
    params = list(sig.parameters.keys())



def test_model_taskset_is_not_abstract():
    assert not inspect.isabstract(model_TaskSet)


def test_model_taskset_constructor_exists():
    assert callable(model_TaskSet.__init__)


def test_model_taskset_constructor_args():
    sig = inspect.signature(model_TaskSet.__init__)
    params = list(sig.parameters.keys())



def test_model_view_is_not_abstract():
    assert not inspect.isabstract(model_View)


def test_model_view_constructor_exists():
    assert callable(model_View.__init__)


def test_model_view_constructor_args():
    sig = inspect.signature(model_View.__init__)
    params = list(sig.parameters.keys())
    assert "sql" in params, "Missing parameter 'sql'"

def test_model_view_has_sql():
    assert hasattr(model_View, "sql")
    descriptor = None
    for klass in model_View.__mro__:
        if "sql" in klass.__dict__:
            descriptor = klass.__dict__["sql"]
            break
    assert isinstance(descriptor, property)



def test_model_ifile_is_not_abstract():
    assert not inspect.isabstract(model_IFile)


def test_model_ifile_constructor_exists():
    assert callable(model_IFile.__init__)


def test_model_ifile_constructor_args():
    sig = inspect.signature(model_IFile.__init__)
    params = list(sig.parameters.keys())



def test_model_user_is_not_abstract():
    assert not inspect.isabstract(model_User)


def test_model_user_constructor_exists():
    assert callable(model_User.__init__)


def test_model_user_constructor_args():
    sig = inspect.signature(model_User.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"

def test_model_user_has_password():
    assert hasattr(model_User, "password")
    descriptor = None
    for klass in model_User.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)



def test_model_schema_is_not_abstract():
    assert not inspect.isabstract(model_Schema)


def test_model_schema_constructor_exists():
    assert callable(model_Schema.__init__)


def test_model_schema_constructor_args():
    sig = inspect.signature(model_Schema.__init__)
    params = list(sig.parameters.keys())



def test_model_site_is_not_abstract():
    assert not inspect.isabstract(model_Site)


def test_model_site_constructor_exists():
    assert callable(model_Site.__init__)


def test_model_site_constructor_args():
    sig = inspect.signature(model_Site.__init__)
    params = list(sig.parameters.keys())



def test_model_fileset_is_not_abstract():
    assert not inspect.isabstract(model_FileSet)


def test_model_fileset_constructor_exists():
    assert callable(model_FileSet.__init__)


def test_model_fileset_constructor_args():
    sig = inspect.signature(model_FileSet.__init__)
    params = list(sig.parameters.keys())
    assert "hostname" in params, "Missing parameter 'hostname'"

def test_model_fileset_has_hostname():
    assert hasattr(model_FileSet, "hostname")
    descriptor = None
    for klass in model_FileSet.__mro__:
        if "hostname" in klass.__dict__:
            descriptor = klass.__dict__["hostname"]
            break
    assert isinstance(descriptor, property)



def test_model_icolumn_is_not_abstract():
    assert not inspect.isabstract(model_IColumn)


def test_model_icolumn_constructor_exists():
    assert callable(model_IColumn.__init__)


def test_model_icolumn_constructor_args():
    sig = inspect.signature(model_IColumn.__init__)
    params = list(sig.parameters.keys())



def test_model_task_is_not_abstract():
    assert not inspect.isabstract(model_Task)


def test_model_task_constructor_exists():
    assert callable(model_Task.__init__)


def test_model_task_constructor_args():
    sig = inspect.signature(model_Task.__init__)
    params = list(sig.parameters.keys())
    assert "fileName" in params, "Missing parameter 'fileName'"

def test_model_task_has_fileName():
    assert hasattr(model_Task, "fileName")
    descriptor = None
    for klass in model_Task.__mro__:
        if "fileName" in klass.__dict__:
            descriptor = klass.__dict__["fileName"]
            break
    assert isinstance(descriptor, property)



def test_model_database_is_not_abstract():
    assert not inspect.isabstract(model_Database)


def test_model_database_constructor_exists():
    assert callable(model_Database.__init__)


def test_model_database_constructor_args():
    sig = inspect.signature(model_Database.__init__)
    params = list(sig.parameters.keys())
    assert "dsn" in params, "Missing parameter 'dsn'"

def test_model_database_has_dsn():
    assert hasattr(model_Database, "dsn")
    descriptor = None
    for klass in model_Database.__mro__:
        if "dsn" in klass.__dict__:
            descriptor = klass.__dict__["dsn"]
            break
    assert isinstance(descriptor, property)



def test_model_type_is_not_abstract():
    assert not inspect.isabstract(model_Type)


def test_model_type_constructor_exists():
    assert callable(model_Type.__init__)


def test_model_type_constructor_args():
    sig = inspect.signature(model_Type.__init__)
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
model_TaskExport_strategy = st.builds(
    model_TaskExport,
)
model_TaskFile_strategy = st.builds(
    model_TaskFile,
)
model_TaskSQL_strategy = st.builds(
    model_TaskSQL,
)
model_TaskImport_strategy = st.builds(
    model_TaskImport,
)
IFile_strategy = st.builds(
    IFile,
)
SeparatedElement_strategy = st.builds(
    SeparatedElement,
)
model_File_strategy = st.builds(
    model_File,
    numberOfHeaderLines=
        safe_text,
    files=
        safe_text
)
Mapping_strategy = st.builds(
    Mapping,
)
model_MappingExport_strategy = st.builds(
    model_MappingExport,
)
model_MappingFile_strategy = st.builds(
    model_MappingFile,
)
model_MappingSQL_strategy = st.builds(
    model_MappingSQL,
)
model_MappingImport_strategy = st.builds(
    model_MappingImport,
)
model_Mapping_strategy = st.builds(
    model_Mapping,
    expression=
        safe_text
)
model_SCTFile_strategy = st.builds(
    model_SCTFile,
    file=
        safe_text
)
FQNamedElement_strategy = st.builds(
    FQNamedElement,
)
IColumn_strategy = st.builds(
    IColumn,
)
model_Field_strategy = st.builds(
    model_Field,
    position=
        safe_text,
    type=
        safe_text,
    length=
        safe_text
)
model_Column_strategy = st.builds(
    model_Column,
)
model_SeparatedElement_strategy = st.builds(
    model_SeparatedElement,
    separator=
        safe_text
)
model_FQNamedElement_strategy = st.builds(
    model_FQNamedElement,
)
model_DescribedElement_strategy = st.builds(
    model_DescribedElement,
    description=
        safe_text
)
model_NamedElement_strategy = st.builds(
    model_NamedElement,
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
model_Domain_strategy = st.builds(
    model_Domain,
    type=
        safe_text
)
model_NativeSQLType_strategy = st.builds(
    model_NativeSQLType,
)
DescribedElement_strategy = st.builds(
    DescribedElement,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
model_Table_strategy = st.builds(
    model_Table,
)
model_TaskSet_strategy = st.builds(
    model_TaskSet,
)
model_View_strategy = st.builds(
    model_View,
    sql=
        safe_text
)
model_IFile_strategy = st.builds(
    model_IFile,
)
model_User_strategy = st.builds(
    model_User,
    password=
        safe_text
)
model_Schema_strategy = st.builds(
    model_Schema,
)
model_Site_strategy = st.builds(
    model_Site,
)
model_FileSet_strategy = st.builds(
    model_FileSet,
    hostname=
        safe_text
)
model_IColumn_strategy = st.builds(
    model_IColumn,
)
model_Task_strategy = st.builds(
    model_Task,
    fileName=
        safe_text
)
model_Database_strategy = st.builds(
    model_Database,
    dsn=
        safe_text
)
model_Type_strategy = st.builds(
    model_Type,
)

@given(instance=Task_strategy)
@settings(max_examples=50)
def test_task_instantiation(instance):
    assert isinstance(instance, Task)

@given(instance=model_TaskExport_strategy)
@settings(max_examples=50)
def test_model_taskexport_instantiation(instance):
    assert isinstance(instance, model_TaskExport)

@given(instance=model_TaskFile_strategy)
@settings(max_examples=50)
def test_model_taskfile_instantiation(instance):
    assert isinstance(instance, model_TaskFile)

@given(instance=model_TaskSQL_strategy)
@settings(max_examples=50)
def test_model_tasksql_instantiation(instance):
    assert isinstance(instance, model_TaskSQL)

@given(instance=model_TaskImport_strategy)
@settings(max_examples=50)
def test_model_taskimport_instantiation(instance):
    assert isinstance(instance, model_TaskImport)

@given(instance=IFile_strategy)
@settings(max_examples=50)
def test_ifile_instantiation(instance):
    assert isinstance(instance, IFile)

@given(instance=SeparatedElement_strategy)
@settings(max_examples=50)
def test_separatedelement_instantiation(instance):
    assert isinstance(instance, SeparatedElement)

@given(instance=model_File_strategy)
@settings(max_examples=50)
def test_model_file_instantiation(instance):
    assert isinstance(instance, model_File)



@given(instance=model_File_strategy)
def test_model_file_numberOfHeaderLines_setter(instance):
    original = instance.numberOfHeaderLines
    instance.numberOfHeaderLines = original
    assert instance.numberOfHeaderLines == original



@given(instance=model_File_strategy)
def test_model_file_files_setter(instance):
    original = instance.files
    instance.files = original
    assert instance.files == original

@given(instance=Mapping_strategy)
@settings(max_examples=50)
def test_mapping_instantiation(instance):
    assert isinstance(instance, Mapping)

@given(instance=model_MappingExport_strategy)
@settings(max_examples=50)
def test_model_mappingexport_instantiation(instance):
    assert isinstance(instance, model_MappingExport)

@given(instance=model_MappingFile_strategy)
@settings(max_examples=50)
def test_model_mappingfile_instantiation(instance):
    assert isinstance(instance, model_MappingFile)

@given(instance=model_MappingSQL_strategy)
@settings(max_examples=50)
def test_model_mappingsql_instantiation(instance):
    assert isinstance(instance, model_MappingSQL)

@given(instance=model_MappingImport_strategy)
@settings(max_examples=50)
def test_model_mappingimport_instantiation(instance):
    assert isinstance(instance, model_MappingImport)

@given(instance=model_Mapping_strategy)
@settings(max_examples=50)
def test_model_mapping_instantiation(instance):
    assert isinstance(instance, model_Mapping)



@given(instance=model_Mapping_strategy)
def test_model_mapping_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=model_SCTFile_strategy)
@settings(max_examples=50)
def test_model_sctfile_instantiation(instance):
    assert isinstance(instance, model_SCTFile)



@given(instance=model_SCTFile_strategy)
def test_model_sctfile_file_setter(instance):
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

@given(instance=model_Field_strategy)
@settings(max_examples=50)
def test_model_field_instantiation(instance):
    assert isinstance(instance, model_Field)



@given(instance=model_Field_strategy)
def test_model_field_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original



@given(instance=model_Field_strategy)
def test_model_field_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=model_Field_strategy)
def test_model_field_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=model_Column_strategy)
@settings(max_examples=50)
def test_model_column_instantiation(instance):
    assert isinstance(instance, model_Column)

@given(instance=model_SeparatedElement_strategy)
@settings(max_examples=50)
def test_model_separatedelement_instantiation(instance):
    assert isinstance(instance, model_SeparatedElement)



@given(instance=model_SeparatedElement_strategy)
def test_model_separatedelement_separator_setter(instance):
    original = instance.separator
    instance.separator = original
    assert instance.separator == original

@given(instance=model_FQNamedElement_strategy)
@settings(max_examples=50)
def test_model_fqnamedelement_instantiation(instance):
    assert isinstance(instance, model_FQNamedElement)

@given(instance=model_DescribedElement_strategy)
@settings(max_examples=50)
def test_model_describedelement_instantiation(instance):
    assert isinstance(instance, model_DescribedElement)



@given(instance=model_DescribedElement_strategy)
def test_model_describedelement_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=model_NamedElement_strategy)
@settings(max_examples=50)
def test_model_namedelement_instantiation(instance):
    assert isinstance(instance, model_NamedElement)



@given(instance=model_NamedElement_strategy)
def test_model_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=model_Domain_strategy)
@settings(max_examples=50)
def test_model_domain_instantiation(instance):
    assert isinstance(instance, model_Domain)



@given(instance=model_Domain_strategy)
def test_model_domain_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=model_NativeSQLType_strategy)
@settings(max_examples=50)
def test_model_nativesqltype_instantiation(instance):
    assert isinstance(instance, model_NativeSQLType)

@given(instance=DescribedElement_strategy)
@settings(max_examples=50)
def test_describedelement_instantiation(instance):
    assert isinstance(instance, DescribedElement)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=model_Table_strategy)
@settings(max_examples=50)
def test_model_table_instantiation(instance):
    assert isinstance(instance, model_Table)

@given(instance=model_TaskSet_strategy)
@settings(max_examples=50)
def test_model_taskset_instantiation(instance):
    assert isinstance(instance, model_TaskSet)

@given(instance=model_View_strategy)
@settings(max_examples=50)
def test_model_view_instantiation(instance):
    assert isinstance(instance, model_View)



@given(instance=model_View_strategy)
def test_model_view_sql_setter(instance):
    original = instance.sql
    instance.sql = original
    assert instance.sql == original

@given(instance=model_IFile_strategy)
@settings(max_examples=50)
def test_model_ifile_instantiation(instance):
    assert isinstance(instance, model_IFile)

@given(instance=model_User_strategy)
@settings(max_examples=50)
def test_model_user_instantiation(instance):
    assert isinstance(instance, model_User)



@given(instance=model_User_strategy)
def test_model_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=model_Schema_strategy)
@settings(max_examples=50)
def test_model_schema_instantiation(instance):
    assert isinstance(instance, model_Schema)

@given(instance=model_Site_strategy)
@settings(max_examples=50)
def test_model_site_instantiation(instance):
    assert isinstance(instance, model_Site)

@given(instance=model_FileSet_strategy)
@settings(max_examples=50)
def test_model_fileset_instantiation(instance):
    assert isinstance(instance, model_FileSet)



@given(instance=model_FileSet_strategy)
def test_model_fileset_hostname_setter(instance):
    original = instance.hostname
    instance.hostname = original
    assert instance.hostname == original

@given(instance=model_IColumn_strategy)
@settings(max_examples=50)
def test_model_icolumn_instantiation(instance):
    assert isinstance(instance, model_IColumn)

@given(instance=model_Task_strategy)
@settings(max_examples=50)
def test_model_task_instantiation(instance):
    assert isinstance(instance, model_Task)



@given(instance=model_Task_strategy)
def test_model_task_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original

@given(instance=model_Database_strategy)
@settings(max_examples=50)
def test_model_database_instantiation(instance):
    assert isinstance(instance, model_Database)



@given(instance=model_Database_strategy)
def test_model_database_dsn_setter(instance):
    original = instance.dsn
    instance.dsn = original
    assert instance.dsn == original

@given(instance=model_Type_strategy)
@settings(max_examples=50)
def test_model_type_instantiation(instance):
    assert isinstance(instance, model_Type)
