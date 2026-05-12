import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    dbmodel_ClassOrDuplicate,
    dbmodel_Stype,
    dbmodel_Type,
    dbmodel_IndexRef,
    dbmodel_Primkey,
    dbmodel_Attribute,
    dbmodel_StructOverride,
    dbmodel_StructShare,
    dbmodel_Ltype,
    dbmodel_Pdb,
    dbmodel_Index,
    dbmodel_DbModel,
    ClassOrDuplicate,
    dbmodel_Duplicate,
    dbmodel_Class,
    dbmodel_Subject,
    dbmodel_Import,
    KobeType,
    LockSchema,
    KudaType,
    Mtype,
    PhysicalDatabase,
    KudaReplicate,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dbmodel_classorduplicate_is_not_abstract():
    assert not inspect.isabstract(dbmodel_ClassOrDuplicate)


def test_dbmodel_classorduplicate_constructor_exists():
    assert callable(dbmodel_ClassOrDuplicate.__init__)


def test_dbmodel_classorduplicate_constructor_args():
    sig = inspect.signature(dbmodel_ClassOrDuplicate.__init__)
    params = list(sig.parameters.keys())
    assert "abbrev" in params, "Missing parameter 'abbrev'"
    assert "name" in params, "Missing parameter 'name'"
    assert "reps" in params, "Missing parameter 'reps'"

def test_dbmodel_classorduplicate_has_abbrev():
    assert hasattr(dbmodel_ClassOrDuplicate, "abbrev")
    descriptor = None
    for klass in dbmodel_ClassOrDuplicate.__mro__:
        if "abbrev" in klass.__dict__:
            descriptor = klass.__dict__["abbrev"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel_classorduplicate_has_name():
    assert hasattr(dbmodel_ClassOrDuplicate, "name")
    descriptor = None
    for klass in dbmodel_ClassOrDuplicate.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel_classorduplicate_has_reps():
    assert hasattr(dbmodel_ClassOrDuplicate, "reps")
    descriptor = None
    for klass in dbmodel_ClassOrDuplicate.__mro__:
        if "reps" in klass.__dict__:
            descriptor = klass.__dict__["reps"]
            break
    assert isinstance(descriptor, property)



def test_dbmodel_stype_is_not_abstract():
    assert not inspect.isabstract(dbmodel_Stype)


def test_dbmodel_stype_constructor_exists():
    assert callable(dbmodel_Stype.__init__)


def test_dbmodel_stype_constructor_args():
    sig = inspect.signature(dbmodel_Stype.__init__)
    params = list(sig.parameters.keys())



def test_dbmodel_type_is_not_abstract():
    assert not inspect.isabstract(dbmodel_Type)


def test_dbmodel_type_constructor_exists():
    assert callable(dbmodel_Type.__init__)


def test_dbmodel_type_constructor_args():
    sig = inspect.signature(dbmodel_Type.__init__)
    params = list(sig.parameters.keys())



def test_dbmodel_indexref_is_not_abstract():
    assert not inspect.isabstract(dbmodel_IndexRef)


def test_dbmodel_indexref_constructor_exists():
    assert callable(dbmodel_IndexRef.__init__)


def test_dbmodel_indexref_constructor_args():
    sig = inspect.signature(dbmodel_IndexRef.__init__)
    params = list(sig.parameters.keys())
    assert "isPrimkey" in params, "Missing parameter 'isPrimkey'"
    assert "clustered" in params, "Missing parameter 'clustered'"

def test_dbmodel_indexref_has_isPrimkey():
    assert hasattr(dbmodel_IndexRef, "isPrimkey")
    descriptor = None
    for klass in dbmodel_IndexRef.__mro__:
        if "isPrimkey" in klass.__dict__:
            descriptor = klass.__dict__["isPrimkey"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel_indexref_has_clustered():
    assert hasattr(dbmodel_IndexRef, "clustered")
    descriptor = None
    for klass in dbmodel_IndexRef.__mro__:
        if "clustered" in klass.__dict__:
            descriptor = klass.__dict__["clustered"]
            break
    assert isinstance(descriptor, property)



def test_dbmodel_primkey_is_not_abstract():
    assert not inspect.isabstract(dbmodel_Primkey)


def test_dbmodel_primkey_constructor_exists():
    assert callable(dbmodel_Primkey.__init__)


def test_dbmodel_primkey_constructor_args():
    sig = inspect.signature(dbmodel_Primkey.__init__)
    params = list(sig.parameters.keys())



def test_dbmodel_attribute_is_not_abstract():
    assert not inspect.isabstract(dbmodel_Attribute)


def test_dbmodel_attribute_constructor_exists():
    assert callable(dbmodel_Attribute.__init__)


def test_dbmodel_attribute_constructor_args():
    sig = inspect.signature(dbmodel_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "isPublic" in params, "Missing parameter 'isPublic'"
    assert "immutable" in params, "Missing parameter 'immutable'"
    assert "shared" in params, "Missing parameter 'shared'"
    assert "descr" in params, "Missing parameter 'descr'"
    assert "kuko" in params, "Missing parameter 'kuko'"
    assert "exttable" in params, "Missing parameter 'exttable'"
    assert "kukoindex" in params, "Missing parameter 'kukoindex'"
    assert "kukoonly" in params, "Missing parameter 'kukoonly'"
    assert "archiv" in params, "Missing parameter 'archiv'"
    assert "optional" in params, "Missing parameter 'optional'"
    assert "isInDB" in params, "Missing parameter 'isInDB'"
    assert "aName" in params, "Missing parameter 'aName'"
    assert "sybident" in params, "Missing parameter 'sybident'"
    assert "foreign" in params, "Missing parameter 'foreign'"
    assert "name" in params, "Missing parameter 'name'"
    assert "extattr" in params, "Missing parameter 'extattr'"
    assert "nullOK" in params, "Missing parameter 'nullOK'"

def test_dbmodel_attribute_has_isPublic():
    assert hasattr(dbmodel_Attribute, "isPublic")
    descriptor = None
    for klass in dbmodel_Attribute.__mro__:
        if "isPublic" in klass.__dict__:
            descriptor = klass.__dict__["isPublic"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel_attribute_has_immutable():
    assert hasattr(dbmodel_Attribute, "immutable")
    descriptor = None
    for klass in dbmodel_Attribute.__mro__:
        if "immutable" in klass.__dict__:
            descriptor = klass.__dict__["immutable"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel_attribute_has_shared():
    assert hasattr(dbmodel_Attribute, "shared")
    descriptor = None
    for klass in dbmodel_Attribute.__mro__:
        if "shared" in klass.__dict__:
            descriptor = klass.__dict__["shared"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel_attribute_has_descr():
    assert hasattr(dbmodel_Attribute, "descr")
    descriptor = None
    for klass in dbmodel_Attribute.__mro__:
        if "descr" in klass.__dict__:
            descriptor = klass.__dict__["descr"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel_attribute_has_kuko():
    assert hasattr(dbmodel_Attribute, "kuko")
    descriptor = None
    for klass in dbmodel_Attribute.__mro__:
        if "kuko" in klass.__dict__:
            descriptor = klass.__dict__["kuko"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel_attribute_has_exttable():
    assert hasattr(dbmodel_Attribute, "exttable")
    descriptor = None
    for klass in dbmodel_Attribute.__mro__:
        if "exttable" in klass.__dict__:
            descriptor = klass.__dict__["exttable"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel_attribute_has_kukoindex():
    assert hasattr(dbmodel_Attribute, "kukoindex")
    descriptor = None
    for klass in dbmodel_Attribute.__mro__:
        if "kukoindex" in klass.__dict__:
            descriptor = klass.__dict__["kukoindex"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel_attribute_has_kukoonly():
    assert hasattr(dbmodel_Attribute, "kukoonly")
    descriptor = None
    for klass in dbmodel_Attribute.__mro__:
        if "kukoonly" in klass.__dict__:
            descriptor = klass.__dict__["kukoonly"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel_attribute_has_archiv():
    assert hasattr(dbmodel_Attribute, "archiv")
    descriptor = None
    for klass in dbmodel_Attribute.__mro__:
        if "archiv" in klass.__dict__:
            descriptor = klass.__dict__["archiv"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel_attribute_has_optional():
    assert hasattr(dbmodel_Attribute, "optional")
    descriptor = None
    for klass in dbmodel_Attribute.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel_attribute_has_isInDB():
    assert hasattr(dbmodel_Attribute, "isInDB")
    descriptor = None
    for klass in dbmodel_Attribute.__mro__:
        if "isInDB" in klass.__dict__:
            descriptor = klass.__dict__["isInDB"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel_attribute_has_aName():
    assert hasattr(dbmodel_Attribute, "aName")
    descriptor = None
    for klass in dbmodel_Attribute.__mro__:
        if "aName" in klass.__dict__:
            descriptor = klass.__dict__["aName"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel_attribute_has_sybident():
    assert hasattr(dbmodel_Attribute, "sybident")
    descriptor = None
    for klass in dbmodel_Attribute.__mro__:
        if "sybident" in klass.__dict__:
            descriptor = klass.__dict__["sybident"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel_attribute_has_foreign():
    assert hasattr(dbmodel_Attribute, "foreign")
    descriptor = None
    for klass in dbmodel_Attribute.__mro__:
        if "foreign" in klass.__dict__:
            descriptor = klass.__dict__["foreign"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel_attribute_has_name():
    assert hasattr(dbmodel_Attribute, "name")
    descriptor = None
    for klass in dbmodel_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel_attribute_has_extattr():
    assert hasattr(dbmodel_Attribute, "extattr")
    descriptor = None
    for klass in dbmodel_Attribute.__mro__:
        if "extattr" in klass.__dict__:
            descriptor = klass.__dict__["extattr"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel_attribute_has_nullOK():
    assert hasattr(dbmodel_Attribute, "nullOK")
    descriptor = None
    for klass in dbmodel_Attribute.__mro__:
        if "nullOK" in klass.__dict__:
            descriptor = klass.__dict__["nullOK"]
            break
    assert isinstance(descriptor, property)



def test_dbmodel_structoverride_is_not_abstract():
    assert not inspect.isabstract(dbmodel_StructOverride)


def test_dbmodel_structoverride_constructor_exists():
    assert callable(dbmodel_StructOverride.__init__)


def test_dbmodel_structoverride_constructor_args():
    sig = inspect.signature(dbmodel_StructOverride.__init__)
    params = list(sig.parameters.keys())
    assert "altname" in params, "Missing parameter 'altname'"

def test_dbmodel_structoverride_has_altname():
    assert hasattr(dbmodel_StructOverride, "altname")
    descriptor = None
    for klass in dbmodel_StructOverride.__mro__:
        if "altname" in klass.__dict__:
            descriptor = klass.__dict__["altname"]
            break
    assert isinstance(descriptor, property)



def test_dbmodel_structshare_is_not_abstract():
    assert not inspect.isabstract(dbmodel_StructShare)


def test_dbmodel_structshare_constructor_exists():
    assert callable(dbmodel_StructShare.__init__)


def test_dbmodel_structshare_constructor_args():
    sig = inspect.signature(dbmodel_StructShare.__init__)
    params = list(sig.parameters.keys())



def test_dbmodel_ltype_is_not_abstract():
    assert not inspect.isabstract(dbmodel_Ltype)


def test_dbmodel_ltype_constructor_exists():
    assert callable(dbmodel_Ltype.__init__)


def test_dbmodel_ltype_constructor_args():
    sig = inspect.signature(dbmodel_Ltype.__init__)
    params = list(sig.parameters.keys())



def test_dbmodel_pdb_is_not_abstract():
    assert not inspect.isabstract(dbmodel_Pdb)


def test_dbmodel_pdb_constructor_exists():
    assert callable(dbmodel_Pdb.__init__)


def test_dbmodel_pdb_constructor_args():
    sig = inspect.signature(dbmodel_Pdb.__init__)
    params = list(sig.parameters.keys())
    assert "tablePartitioning" in params, "Missing parameter 'tablePartitioning'"
    assert "lockSchema" in params, "Missing parameter 'lockSchema'"
    assert "name" in params, "Missing parameter 'name'"

def test_dbmodel_pdb_has_tablePartitioning():
    assert hasattr(dbmodel_Pdb, "tablePartitioning")
    descriptor = None
    for klass in dbmodel_Pdb.__mro__:
        if "tablePartitioning" in klass.__dict__:
            descriptor = klass.__dict__["tablePartitioning"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel_pdb_has_lockSchema():
    assert hasattr(dbmodel_Pdb, "lockSchema")
    descriptor = None
    for klass in dbmodel_Pdb.__mro__:
        if "lockSchema" in klass.__dict__:
            descriptor = klass.__dict__["lockSchema"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel_pdb_has_name():
    assert hasattr(dbmodel_Pdb, "name")
    descriptor = None
    for klass in dbmodel_Pdb.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dbmodel_index_is_not_abstract():
    assert not inspect.isabstract(dbmodel_Index)


def test_dbmodel_index_constructor_exists():
    assert callable(dbmodel_Index.__init__)


def test_dbmodel_index_constructor_args():
    sig = inspect.signature(dbmodel_Index.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "unique" in params, "Missing parameter 'unique'"
    assert "kuko" in params, "Missing parameter 'kuko'"

def test_dbmodel_index_has_name():
    assert hasattr(dbmodel_Index, "name")
    descriptor = None
    for klass in dbmodel_Index.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel_index_has_unique():
    assert hasattr(dbmodel_Index, "unique")
    descriptor = None
    for klass in dbmodel_Index.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel_index_has_kuko():
    assert hasattr(dbmodel_Index, "kuko")
    descriptor = None
    for klass in dbmodel_Index.__mro__:
        if "kuko" in klass.__dict__:
            descriptor = klass.__dict__["kuko"]
            break
    assert isinstance(descriptor, property)



def test_dbmodel_dbmodel_is_not_abstract():
    assert not inspect.isabstract(dbmodel_DbModel)


def test_dbmodel_dbmodel_constructor_exists():
    assert callable(dbmodel_DbModel.__init__)


def test_dbmodel_dbmodel_constructor_args():
    sig = inspect.signature(dbmodel_DbModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "version" in params, "Missing parameter 'version'"
    assert "kobeType" in params, "Missing parameter 'kobeType'"
    assert "doAll" in params, "Missing parameter 'doAll'"
    assert "mtype" in params, "Missing parameter 'mtype'"
    assert "kudaType" in params, "Missing parameter 'kudaType'"

def test_dbmodel_dbmodel_has_name():
    assert hasattr(dbmodel_DbModel, "name")
    descriptor = None
    for klass in dbmodel_DbModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel_dbmodel_has_version():
    assert hasattr(dbmodel_DbModel, "version")
    descriptor = None
    for klass in dbmodel_DbModel.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel_dbmodel_has_kobeType():
    assert hasattr(dbmodel_DbModel, "kobeType")
    descriptor = None
    for klass in dbmodel_DbModel.__mro__:
        if "kobeType" in klass.__dict__:
            descriptor = klass.__dict__["kobeType"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel_dbmodel_has_doAll():
    assert hasattr(dbmodel_DbModel, "doAll")
    descriptor = None
    for klass in dbmodel_DbModel.__mro__:
        if "doAll" in klass.__dict__:
            descriptor = klass.__dict__["doAll"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel_dbmodel_has_mtype():
    assert hasattr(dbmodel_DbModel, "mtype")
    descriptor = None
    for klass in dbmodel_DbModel.__mro__:
        if "mtype" in klass.__dict__:
            descriptor = klass.__dict__["mtype"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel_dbmodel_has_kudaType():
    assert hasattr(dbmodel_DbModel, "kudaType")
    descriptor = None
    for klass in dbmodel_DbModel.__mro__:
        if "kudaType" in klass.__dict__:
            descriptor = klass.__dict__["kudaType"]
            break
    assert isinstance(descriptor, property)



def test_classorduplicate_is_not_abstract():
    assert not inspect.isabstract(ClassOrDuplicate)


def test_classorduplicate_constructor_exists():
    assert callable(ClassOrDuplicate.__init__)


def test_classorduplicate_constructor_args():
    sig = inspect.signature(ClassOrDuplicate.__init__)
    params = list(sig.parameters.keys())



def test_dbmodel_duplicate_is_not_abstract():
    assert not inspect.isabstract(dbmodel_Duplicate)


def test_dbmodel_duplicate_constructor_exists():
    assert callable(dbmodel_Duplicate.__init__)


def test_dbmodel_duplicate_constructor_args():
    sig = inspect.signature(dbmodel_Duplicate.__init__)
    params = list(sig.parameters.keys())



def test_dbmodel_class_is_not_abstract():
    assert not inspect.isabstract(dbmodel_Class)


def test_dbmodel_class_constructor_exists():
    assert callable(dbmodel_Class.__init__)


def test_dbmodel_class_constructor_args():
    sig = inspect.signature(dbmodel_Class.__init__)
    params = list(sig.parameters.keys())
    assert "pubspec" in params, "Missing parameter 'pubspec'"
    assert "aName" in params, "Missing parameter 'aName'"
    assert "descr" in params, "Missing parameter 'descr'"
    assert "pubname" in params, "Missing parameter 'pubname'"
    assert "noDBio" in params, "Missing parameter 'noDBio'"
    assert "whereclause" in params, "Missing parameter 'whereclause'"
    assert "archivIndex" in params, "Missing parameter 'archivIndex'"
    assert "publish" in params, "Missing parameter 'publish'"
    assert "vmin" in params, "Missing parameter 'vmin'"
    assert "vmaj" in params, "Missing parameter 'vmaj'"

def test_dbmodel_class_has_pubspec():
    assert hasattr(dbmodel_Class, "pubspec")
    descriptor = None
    for klass in dbmodel_Class.__mro__:
        if "pubspec" in klass.__dict__:
            descriptor = klass.__dict__["pubspec"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel_class_has_aName():
    assert hasattr(dbmodel_Class, "aName")
    descriptor = None
    for klass in dbmodel_Class.__mro__:
        if "aName" in klass.__dict__:
            descriptor = klass.__dict__["aName"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel_class_has_descr():
    assert hasattr(dbmodel_Class, "descr")
    descriptor = None
    for klass in dbmodel_Class.__mro__:
        if "descr" in klass.__dict__:
            descriptor = klass.__dict__["descr"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel_class_has_pubname():
    assert hasattr(dbmodel_Class, "pubname")
    descriptor = None
    for klass in dbmodel_Class.__mro__:
        if "pubname" in klass.__dict__:
            descriptor = klass.__dict__["pubname"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel_class_has_noDBio():
    assert hasattr(dbmodel_Class, "noDBio")
    descriptor = None
    for klass in dbmodel_Class.__mro__:
        if "noDBio" in klass.__dict__:
            descriptor = klass.__dict__["noDBio"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel_class_has_whereclause():
    assert hasattr(dbmodel_Class, "whereclause")
    descriptor = None
    for klass in dbmodel_Class.__mro__:
        if "whereclause" in klass.__dict__:
            descriptor = klass.__dict__["whereclause"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel_class_has_archivIndex():
    assert hasattr(dbmodel_Class, "archivIndex")
    descriptor = None
    for klass in dbmodel_Class.__mro__:
        if "archivIndex" in klass.__dict__:
            descriptor = klass.__dict__["archivIndex"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel_class_has_publish():
    assert hasattr(dbmodel_Class, "publish")
    descriptor = None
    for klass in dbmodel_Class.__mro__:
        if "publish" in klass.__dict__:
            descriptor = klass.__dict__["publish"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel_class_has_vmin():
    assert hasattr(dbmodel_Class, "vmin")
    descriptor = None
    for klass in dbmodel_Class.__mro__:
        if "vmin" in klass.__dict__:
            descriptor = klass.__dict__["vmin"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel_class_has_vmaj():
    assert hasattr(dbmodel_Class, "vmaj")
    descriptor = None
    for klass in dbmodel_Class.__mro__:
        if "vmaj" in klass.__dict__:
            descriptor = klass.__dict__["vmaj"]
            break
    assert isinstance(descriptor, property)



def test_dbmodel_subject_is_not_abstract():
    assert not inspect.isabstract(dbmodel_Subject)


def test_dbmodel_subject_constructor_exists():
    assert callable(dbmodel_Subject.__init__)


def test_dbmodel_subject_constructor_args():
    sig = inspect.signature(dbmodel_Subject.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dbmodel_subject_has_name():
    assert hasattr(dbmodel_Subject, "name")
    descriptor = None
    for klass in dbmodel_Subject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dbmodel_import_is_not_abstract():
    assert not inspect.isabstract(dbmodel_Import)


def test_dbmodel_import_constructor_exists():
    assert callable(dbmodel_Import.__init__)


def test_dbmodel_import_constructor_args():
    sig = inspect.signature(dbmodel_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_dbmodel_import_has_importedNamespace():
    assert hasattr(dbmodel_Import, "importedNamespace")
    descriptor = None
    for klass in dbmodel_Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)

def test_kobetype_exists():
    # Check that the Enumeration exists
    assert KobeType is not None

def test_kobetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in KobeType]
    expected_literals = [
        "KORA",
        "AUSW",
        "MAIN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in KobeType"

def test_lockschema_exists():
    # Check that the Enumeration exists
    assert LockSchema is not None

def test_lockschema_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LockSchema]
    expected_literals = [
        "DATAROWS",
        "ALLPAGES",
        "DATAPAGES",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LockSchema"

def test_kudatype_exists():
    # Check that the Enumeration exists
    assert KudaType is not None

def test_kudatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in KudaType]
    expected_literals = [
        "PUBLISH",
        "MAIN",
        "TIPO",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in KudaType"

def test_mtype_exists():
    # Check that the Enumeration exists
    assert Mtype is not None

def test_mtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Mtype]
    expected_literals = [
        "KUDA",
        "KOBE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Mtype"

def test_physicaldatabase_exists():
    # Check that the Enumeration exists
    assert PhysicalDatabase is not None

def test_physicaldatabase_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PhysicalDatabase]
    expected_literals = [
        "PDB_AUSW_KOBE_STATISTIK",
        "PDB_AUSW_KOBE_PKT_STAMM",
        "PDB_ABFRAGE_FZK",
        "PDB_PART_BUCH_PROV",
        "PDB_KOBE_AUSW_ADMIN",
        "PDB_ABFRAGE_ARCHIV",
        "PDB_MANDANT_BUCH_STAMM",
        "PDB_ABFRAGE_VSTI",
        "PDB_PART_JAHR",
        "PDB_ABFRAGE_PKT_STAMM",
        "PDB_AUSW_KOBE_BUCH_STAMM",
        "PDB_PART_BUCH_STAMM",
        "PDB_ABFRAGE_BUCH_STAMM",
        "PDB_ABFRAGE_ETV",
        "PDB_PART_MON",
        "PDB_MANDANT_PKT_DATA",
        "PDB_MANDANT_TAG",
        "PDB_KOBE_STEUERUNG",
        "PDB_MANDANT_PKT_STAMM",
        "PDB_KOBE_KNDTEST",
        "PDB_PART_PKT_DATA",
        "PDB_AUSW_KOBE_MON",
        "PDB_KUDA_TRANS_TRANSIT",
        "PDB_MANDANT_MON",
        "PDB_PART_PKT_STAMM",
        "PDB_AUSW_KOBE_ARCHIV",
        "PDB_KOBE_DEZ_STAMM",
        "PDB_MANDANT_TAG_A",
        "PDB_MANDANT_BUCH_PROV",
        "PDB_KOBE_GLOBAL",
        "PDB_PART_AUFT",
        "PDB_PART_TAG_A",
        "PDB_KOBE_PMON",
        "PDB_KOBE_DATA",
        "PDB_PART_TAG",
        "PDB_KOBE_STAMM",
        "PDB_ABFRAGE_MON",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PhysicalDatabase"

def test_kudareplicate_exists():
    # Check that the Enumeration exists
    assert KudaReplicate is not None

def test_kudareplicate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in KudaReplicate]
    expected_literals = [
        "PUBLISHSTV",
        "PUBLISH",
        "SNAP",
        "DWH",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in KudaReplicate"


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
dbmodel_ClassOrDuplicate_strategy = st.builds(
    dbmodel_ClassOrDuplicate,
    abbrev=
        safe_text,
    name=
        safe_text,
    reps=
        safe_text
)
dbmodel_Stype_strategy = st.builds(
    dbmodel_Stype,
)
dbmodel_Type_strategy = st.builds(
    dbmodel_Type,
)
dbmodel_IndexRef_strategy = st.builds(
    dbmodel_IndexRef,
    isPrimkey=
        st.booleans(),
    clustered=
        st.booleans()
)
dbmodel_Primkey_strategy = st.builds(
    dbmodel_Primkey,
)
dbmodel_Attribute_strategy = st.builds(
    dbmodel_Attribute,
    isPublic=
        st.booleans(),
    immutable=
        st.booleans(),
    shared=
        st.booleans(),
    descr=
        safe_text,
    kuko=
        st.booleans(),
    exttable=
        safe_text,
    kukoindex=
        st.booleans(),
    kukoonly=
        st.booleans(),
    archiv=
        st.booleans(),
    optional=
        st.booleans(),
    isInDB=
        st.booleans(),
    aName=
        safe_text,
    sybident=
        st.booleans(),
    foreign=
        st.booleans(),
    name=
        safe_text,
    extattr=
        safe_text,
    nullOK=
        st.booleans()
)
dbmodel_StructOverride_strategy = st.builds(
    dbmodel_StructOverride,
    altname=
        safe_text
)
dbmodel_StructShare_strategy = st.builds(
    dbmodel_StructShare,
)
dbmodel_Ltype_strategy = st.builds(
    dbmodel_Ltype,
)
dbmodel_Pdb_strategy = st.builds(
    dbmodel_Pdb,
    tablePartitioning=
        st.integers(),
    lockSchema=
        safe_text,
    name=
        safe_text
)
dbmodel_Index_strategy = st.builds(
    dbmodel_Index,
    name=
        safe_text,
    unique=
        st.booleans(),
    kuko=
        st.booleans()
)
dbmodel_DbModel_strategy = st.builds(
    dbmodel_DbModel,
    name=
        safe_text,
    version=
        safe_text,
    kobeType=
        safe_text,
    doAll=
        st.booleans(),
    mtype=
        safe_text,
    kudaType=
        safe_text
)
ClassOrDuplicate_strategy = st.builds(
    ClassOrDuplicate,
)
dbmodel_Duplicate_strategy = st.builds(
    dbmodel_Duplicate,
)
dbmodel_Class_strategy = st.builds(
    dbmodel_Class,
    pubspec=
        st.booleans(),
    aName=
        safe_text,
    descr=
        safe_text,
    pubname=
        safe_text,
    noDBio=
        st.booleans(),
    whereclause=
        safe_text,
    archivIndex=
        safe_text,
    publish=
        st.booleans(),
    vmin=
        st.integers(),
    vmaj=
        st.integers()
)
dbmodel_Subject_strategy = st.builds(
    dbmodel_Subject,
    name=
        safe_text
)
dbmodel_Import_strategy = st.builds(
    dbmodel_Import,
    importedNamespace=
        safe_text
)

@given(instance=dbmodel_ClassOrDuplicate_strategy)
@settings(max_examples=50)
def test_dbmodel_classorduplicate_instantiation(instance):
    assert isinstance(instance, dbmodel_ClassOrDuplicate)



@given(instance=dbmodel_ClassOrDuplicate_strategy)
def test_dbmodel_classorduplicate_abbrev_setter(instance):
    original = instance.abbrev
    instance.abbrev = original
    assert instance.abbrev == original



@given(instance=dbmodel_ClassOrDuplicate_strategy)
def test_dbmodel_classorduplicate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dbmodel_ClassOrDuplicate_strategy)
def test_dbmodel_classorduplicate_reps_setter(instance):
    original = instance.reps
    instance.reps = original
    assert instance.reps == original

@given(instance=dbmodel_Stype_strategy)
@settings(max_examples=50)
def test_dbmodel_stype_instantiation(instance):
    assert isinstance(instance, dbmodel_Stype)

@given(instance=dbmodel_Type_strategy)
@settings(max_examples=50)
def test_dbmodel_type_instantiation(instance):
    assert isinstance(instance, dbmodel_Type)

@given(instance=dbmodel_IndexRef_strategy)
@settings(max_examples=50)
def test_dbmodel_indexref_instantiation(instance):
    assert isinstance(instance, dbmodel_IndexRef)



@given(instance=dbmodel_IndexRef_strategy)
def test_dbmodel_indexref_isPrimkey_setter(instance):
    original = instance.isPrimkey
    instance.isPrimkey = original
    assert instance.isPrimkey == original



@given(instance=dbmodel_IndexRef_strategy)
def test_dbmodel_indexref_clustered_setter(instance):
    original = instance.clustered
    instance.clustered = original
    assert instance.clustered == original

@given(instance=dbmodel_Primkey_strategy)
@settings(max_examples=50)
def test_dbmodel_primkey_instantiation(instance):
    assert isinstance(instance, dbmodel_Primkey)

@given(instance=dbmodel_Attribute_strategy)
@settings(max_examples=50)
def test_dbmodel_attribute_instantiation(instance):
    assert isinstance(instance, dbmodel_Attribute)



@given(instance=dbmodel_Attribute_strategy)
def test_dbmodel_attribute_isPublic_setter(instance):
    original = instance.isPublic
    instance.isPublic = original
    assert instance.isPublic == original



@given(instance=dbmodel_Attribute_strategy)
def test_dbmodel_attribute_immutable_setter(instance):
    original = instance.immutable
    instance.immutable = original
    assert instance.immutable == original



@given(instance=dbmodel_Attribute_strategy)
def test_dbmodel_attribute_shared_setter(instance):
    original = instance.shared
    instance.shared = original
    assert instance.shared == original



@given(instance=dbmodel_Attribute_strategy)
def test_dbmodel_attribute_descr_setter(instance):
    original = instance.descr
    instance.descr = original
    assert instance.descr == original



@given(instance=dbmodel_Attribute_strategy)
def test_dbmodel_attribute_kuko_setter(instance):
    original = instance.kuko
    instance.kuko = original
    assert instance.kuko == original



@given(instance=dbmodel_Attribute_strategy)
def test_dbmodel_attribute_exttable_setter(instance):
    original = instance.exttable
    instance.exttable = original
    assert instance.exttable == original



@given(instance=dbmodel_Attribute_strategy)
def test_dbmodel_attribute_kukoindex_setter(instance):
    original = instance.kukoindex
    instance.kukoindex = original
    assert instance.kukoindex == original



@given(instance=dbmodel_Attribute_strategy)
def test_dbmodel_attribute_kukoonly_setter(instance):
    original = instance.kukoonly
    instance.kukoonly = original
    assert instance.kukoonly == original



@given(instance=dbmodel_Attribute_strategy)
def test_dbmodel_attribute_archiv_setter(instance):
    original = instance.archiv
    instance.archiv = original
    assert instance.archiv == original



@given(instance=dbmodel_Attribute_strategy)
def test_dbmodel_attribute_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original



@given(instance=dbmodel_Attribute_strategy)
def test_dbmodel_attribute_isInDB_setter(instance):
    original = instance.isInDB
    instance.isInDB = original
    assert instance.isInDB == original



@given(instance=dbmodel_Attribute_strategy)
def test_dbmodel_attribute_aName_setter(instance):
    original = instance.aName
    instance.aName = original
    assert instance.aName == original



@given(instance=dbmodel_Attribute_strategy)
def test_dbmodel_attribute_sybident_setter(instance):
    original = instance.sybident
    instance.sybident = original
    assert instance.sybident == original



@given(instance=dbmodel_Attribute_strategy)
def test_dbmodel_attribute_foreign_setter(instance):
    original = instance.foreign
    instance.foreign = original
    assert instance.foreign == original



@given(instance=dbmodel_Attribute_strategy)
def test_dbmodel_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dbmodel_Attribute_strategy)
def test_dbmodel_attribute_extattr_setter(instance):
    original = instance.extattr
    instance.extattr = original
    assert instance.extattr == original



@given(instance=dbmodel_Attribute_strategy)
def test_dbmodel_attribute_nullOK_setter(instance):
    original = instance.nullOK
    instance.nullOK = original
    assert instance.nullOK == original

@given(instance=dbmodel_StructOverride_strategy)
@settings(max_examples=50)
def test_dbmodel_structoverride_instantiation(instance):
    assert isinstance(instance, dbmodel_StructOverride)



@given(instance=dbmodel_StructOverride_strategy)
def test_dbmodel_structoverride_altname_setter(instance):
    original = instance.altname
    instance.altname = original
    assert instance.altname == original

@given(instance=dbmodel_StructShare_strategy)
@settings(max_examples=50)
def test_dbmodel_structshare_instantiation(instance):
    assert isinstance(instance, dbmodel_StructShare)

@given(instance=dbmodel_Ltype_strategy)
@settings(max_examples=50)
def test_dbmodel_ltype_instantiation(instance):
    assert isinstance(instance, dbmodel_Ltype)

@given(instance=dbmodel_Pdb_strategy)
@settings(max_examples=50)
def test_dbmodel_pdb_instantiation(instance):
    assert isinstance(instance, dbmodel_Pdb)



@given(instance=dbmodel_Pdb_strategy)
def test_dbmodel_pdb_tablePartitioning_setter(instance):
    original = instance.tablePartitioning
    instance.tablePartitioning = original
    assert instance.tablePartitioning == original



@given(instance=dbmodel_Pdb_strategy)
def test_dbmodel_pdb_lockSchema_setter(instance):
    original = instance.lockSchema
    instance.lockSchema = original
    assert instance.lockSchema == original



@given(instance=dbmodel_Pdb_strategy)
def test_dbmodel_pdb_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dbmodel_Index_strategy)
@settings(max_examples=50)
def test_dbmodel_index_instantiation(instance):
    assert isinstance(instance, dbmodel_Index)



@given(instance=dbmodel_Index_strategy)
def test_dbmodel_index_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dbmodel_Index_strategy)
def test_dbmodel_index_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original



@given(instance=dbmodel_Index_strategy)
def test_dbmodel_index_kuko_setter(instance):
    original = instance.kuko
    instance.kuko = original
    assert instance.kuko == original

@given(instance=dbmodel_DbModel_strategy)
@settings(max_examples=50)
def test_dbmodel_dbmodel_instantiation(instance):
    assert isinstance(instance, dbmodel_DbModel)



@given(instance=dbmodel_DbModel_strategy)
def test_dbmodel_dbmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dbmodel_DbModel_strategy)
def test_dbmodel_dbmodel_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=dbmodel_DbModel_strategy)
def test_dbmodel_dbmodel_kobeType_setter(instance):
    original = instance.kobeType
    instance.kobeType = original
    assert instance.kobeType == original



@given(instance=dbmodel_DbModel_strategy)
def test_dbmodel_dbmodel_doAll_setter(instance):
    original = instance.doAll
    instance.doAll = original
    assert instance.doAll == original



@given(instance=dbmodel_DbModel_strategy)
def test_dbmodel_dbmodel_mtype_setter(instance):
    original = instance.mtype
    instance.mtype = original
    assert instance.mtype == original



@given(instance=dbmodel_DbModel_strategy)
def test_dbmodel_dbmodel_kudaType_setter(instance):
    original = instance.kudaType
    instance.kudaType = original
    assert instance.kudaType == original

@given(instance=ClassOrDuplicate_strategy)
@settings(max_examples=50)
def test_classorduplicate_instantiation(instance):
    assert isinstance(instance, ClassOrDuplicate)

@given(instance=dbmodel_Duplicate_strategy)
@settings(max_examples=50)
def test_dbmodel_duplicate_instantiation(instance):
    assert isinstance(instance, dbmodel_Duplicate)

@given(instance=dbmodel_Class_strategy)
@settings(max_examples=50)
def test_dbmodel_class_instantiation(instance):
    assert isinstance(instance, dbmodel_Class)



@given(instance=dbmodel_Class_strategy)
def test_dbmodel_class_pubspec_setter(instance):
    original = instance.pubspec
    instance.pubspec = original
    assert instance.pubspec == original



@given(instance=dbmodel_Class_strategy)
def test_dbmodel_class_aName_setter(instance):
    original = instance.aName
    instance.aName = original
    assert instance.aName == original



@given(instance=dbmodel_Class_strategy)
def test_dbmodel_class_descr_setter(instance):
    original = instance.descr
    instance.descr = original
    assert instance.descr == original



@given(instance=dbmodel_Class_strategy)
def test_dbmodel_class_pubname_setter(instance):
    original = instance.pubname
    instance.pubname = original
    assert instance.pubname == original



@given(instance=dbmodel_Class_strategy)
def test_dbmodel_class_noDBio_setter(instance):
    original = instance.noDBio
    instance.noDBio = original
    assert instance.noDBio == original



@given(instance=dbmodel_Class_strategy)
def test_dbmodel_class_whereclause_setter(instance):
    original = instance.whereclause
    instance.whereclause = original
    assert instance.whereclause == original



@given(instance=dbmodel_Class_strategy)
def test_dbmodel_class_archivIndex_setter(instance):
    original = instance.archivIndex
    instance.archivIndex = original
    assert instance.archivIndex == original



@given(instance=dbmodel_Class_strategy)
def test_dbmodel_class_publish_setter(instance):
    original = instance.publish
    instance.publish = original
    assert instance.publish == original



@given(instance=dbmodel_Class_strategy)
def test_dbmodel_class_vmin_setter(instance):
    original = instance.vmin
    instance.vmin = original
    assert instance.vmin == original



@given(instance=dbmodel_Class_strategy)
def test_dbmodel_class_vmaj_setter(instance):
    original = instance.vmaj
    instance.vmaj = original
    assert instance.vmaj == original

@given(instance=dbmodel_Subject_strategy)
@settings(max_examples=50)
def test_dbmodel_subject_instantiation(instance):
    assert isinstance(instance, dbmodel_Subject)



@given(instance=dbmodel_Subject_strategy)
def test_dbmodel_subject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dbmodel_Import_strategy)
@settings(max_examples=50)
def test_dbmodel_import_instantiation(instance):
    assert isinstance(instance, dbmodel_Import)



@given(instance=dbmodel_Import_strategy)
def test_dbmodel_import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original
