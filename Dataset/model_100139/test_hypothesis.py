import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    dbmodel::ClassOrDuplicate,
    dbmodel::Stype,
    dbmodel::Type,
    dbmodel::IndexRef,
    dbmodel::Primkey,
    dbmodel::Attribute,
    dbmodel::StructOverride,
    dbmodel::StructShare,
    dbmodel::Ltype,
    dbmodel::Pdb,
    dbmodel::Index,
    dbmodel::DbModel,
    ClassOrDuplicate,
    dbmodel::Duplicate,
    dbmodel::Class,
    dbmodel::Subject,
    dbmodel::Import,
    KudaReplicate,
    KobeType,
    Mtype,
    LockSchema,
    KudaType,
    PhysicalDatabase,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dbmodel::classorduplicate_is_not_abstract():
    assert not inspect.isabstract(dbmodel::ClassOrDuplicate)


def test_dbmodel::classorduplicate_constructor_exists():
    assert callable(dbmodel::ClassOrDuplicate.__init__)


def test_dbmodel::classorduplicate_constructor_args():
    sig = inspect.signature(dbmodel::ClassOrDuplicate.__init__)
    params = list(sig.parameters.keys())
    assert "abbrev" in params, "Missing parameter 'abbrev'"
    assert "name" in params, "Missing parameter 'name'"
    assert "reps" in params, "Missing parameter 'reps'"

def test_dbmodel::classorduplicate_has_abbrev():
    assert hasattr(dbmodel::ClassOrDuplicate, "abbrev")
    descriptor = None
    for klass in dbmodel::ClassOrDuplicate.__mro__:
        if "abbrev" in klass.__dict__:
            descriptor = klass.__dict__["abbrev"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel::classorduplicate_has_name():
    assert hasattr(dbmodel::ClassOrDuplicate, "name")
    descriptor = None
    for klass in dbmodel::ClassOrDuplicate.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel::classorduplicate_has_reps():
    assert hasattr(dbmodel::ClassOrDuplicate, "reps")
    descriptor = None
    for klass in dbmodel::ClassOrDuplicate.__mro__:
        if "reps" in klass.__dict__:
            descriptor = klass.__dict__["reps"]
            break
    assert isinstance(descriptor, property)



def test_dbmodel::stype_is_not_abstract():
    assert not inspect.isabstract(dbmodel::Stype)


def test_dbmodel::stype_constructor_exists():
    assert callable(dbmodel::Stype.__init__)


def test_dbmodel::stype_constructor_args():
    sig = inspect.signature(dbmodel::Stype.__init__)
    params = list(sig.parameters.keys())



def test_dbmodel::type_is_not_abstract():
    assert not inspect.isabstract(dbmodel::Type)


def test_dbmodel::type_constructor_exists():
    assert callable(dbmodel::Type.__init__)


def test_dbmodel::type_constructor_args():
    sig = inspect.signature(dbmodel::Type.__init__)
    params = list(sig.parameters.keys())



def test_dbmodel::indexref_is_not_abstract():
    assert not inspect.isabstract(dbmodel::IndexRef)


def test_dbmodel::indexref_constructor_exists():
    assert callable(dbmodel::IndexRef.__init__)


def test_dbmodel::indexref_constructor_args():
    sig = inspect.signature(dbmodel::IndexRef.__init__)
    params = list(sig.parameters.keys())
    assert "isPrimkey" in params, "Missing parameter 'isPrimkey'"
    assert "clustered" in params, "Missing parameter 'clustered'"

def test_dbmodel::indexref_has_isPrimkey():
    assert hasattr(dbmodel::IndexRef, "isPrimkey")
    descriptor = None
    for klass in dbmodel::IndexRef.__mro__:
        if "isPrimkey" in klass.__dict__:
            descriptor = klass.__dict__["isPrimkey"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel::indexref_has_clustered():
    assert hasattr(dbmodel::IndexRef, "clustered")
    descriptor = None
    for klass in dbmodel::IndexRef.__mro__:
        if "clustered" in klass.__dict__:
            descriptor = klass.__dict__["clustered"]
            break
    assert isinstance(descriptor, property)



def test_dbmodel::primkey_is_not_abstract():
    assert not inspect.isabstract(dbmodel::Primkey)


def test_dbmodel::primkey_constructor_exists():
    assert callable(dbmodel::Primkey.__init__)


def test_dbmodel::primkey_constructor_args():
    sig = inspect.signature(dbmodel::Primkey.__init__)
    params = list(sig.parameters.keys())



def test_dbmodel::attribute_is_not_abstract():
    assert not inspect.isabstract(dbmodel::Attribute)


def test_dbmodel::attribute_constructor_exists():
    assert callable(dbmodel::Attribute.__init__)


def test_dbmodel::attribute_constructor_args():
    sig = inspect.signature(dbmodel::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "isPublic" in params, "Missing parameter 'isPublic'"
    assert "shared" in params, "Missing parameter 'shared'"
    assert "exttable" in params, "Missing parameter 'exttable'"
    assert "immutable" in params, "Missing parameter 'immutable'"
    assert "sybident" in params, "Missing parameter 'sybident'"
    assert "descr" in params, "Missing parameter 'descr'"
    assert "name" in params, "Missing parameter 'name'"
    assert "archiv" in params, "Missing parameter 'archiv'"
    assert "nullOK" in params, "Missing parameter 'nullOK'"
    assert "aName" in params, "Missing parameter 'aName'"
    assert "optional" in params, "Missing parameter 'optional'"
    assert "extattr" in params, "Missing parameter 'extattr'"
    assert "foreign" in params, "Missing parameter 'foreign'"
    assert "kukoindex" in params, "Missing parameter 'kukoindex'"
    assert "kukoonly" in params, "Missing parameter 'kukoonly'"
    assert "isInDB" in params, "Missing parameter 'isInDB'"
    assert "kuko" in params, "Missing parameter 'kuko'"

def test_dbmodel::attribute_has_isPublic():
    assert hasattr(dbmodel::Attribute, "isPublic")
    descriptor = None
    for klass in dbmodel::Attribute.__mro__:
        if "isPublic" in klass.__dict__:
            descriptor = klass.__dict__["isPublic"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel::attribute_has_shared():
    assert hasattr(dbmodel::Attribute, "shared")
    descriptor = None
    for klass in dbmodel::Attribute.__mro__:
        if "shared" in klass.__dict__:
            descriptor = klass.__dict__["shared"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel::attribute_has_exttable():
    assert hasattr(dbmodel::Attribute, "exttable")
    descriptor = None
    for klass in dbmodel::Attribute.__mro__:
        if "exttable" in klass.__dict__:
            descriptor = klass.__dict__["exttable"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel::attribute_has_immutable():
    assert hasattr(dbmodel::Attribute, "immutable")
    descriptor = None
    for klass in dbmodel::Attribute.__mro__:
        if "immutable" in klass.__dict__:
            descriptor = klass.__dict__["immutable"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel::attribute_has_sybident():
    assert hasattr(dbmodel::Attribute, "sybident")
    descriptor = None
    for klass in dbmodel::Attribute.__mro__:
        if "sybident" in klass.__dict__:
            descriptor = klass.__dict__["sybident"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel::attribute_has_descr():
    assert hasattr(dbmodel::Attribute, "descr")
    descriptor = None
    for klass in dbmodel::Attribute.__mro__:
        if "descr" in klass.__dict__:
            descriptor = klass.__dict__["descr"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel::attribute_has_name():
    assert hasattr(dbmodel::Attribute, "name")
    descriptor = None
    for klass in dbmodel::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel::attribute_has_archiv():
    assert hasattr(dbmodel::Attribute, "archiv")
    descriptor = None
    for klass in dbmodel::Attribute.__mro__:
        if "archiv" in klass.__dict__:
            descriptor = klass.__dict__["archiv"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel::attribute_has_nullOK():
    assert hasattr(dbmodel::Attribute, "nullOK")
    descriptor = None
    for klass in dbmodel::Attribute.__mro__:
        if "nullOK" in klass.__dict__:
            descriptor = klass.__dict__["nullOK"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel::attribute_has_aName():
    assert hasattr(dbmodel::Attribute, "aName")
    descriptor = None
    for klass in dbmodel::Attribute.__mro__:
        if "aName" in klass.__dict__:
            descriptor = klass.__dict__["aName"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel::attribute_has_optional():
    assert hasattr(dbmodel::Attribute, "optional")
    descriptor = None
    for klass in dbmodel::Attribute.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel::attribute_has_extattr():
    assert hasattr(dbmodel::Attribute, "extattr")
    descriptor = None
    for klass in dbmodel::Attribute.__mro__:
        if "extattr" in klass.__dict__:
            descriptor = klass.__dict__["extattr"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel::attribute_has_foreign():
    assert hasattr(dbmodel::Attribute, "foreign")
    descriptor = None
    for klass in dbmodel::Attribute.__mro__:
        if "foreign" in klass.__dict__:
            descriptor = klass.__dict__["foreign"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel::attribute_has_kukoindex():
    assert hasattr(dbmodel::Attribute, "kukoindex")
    descriptor = None
    for klass in dbmodel::Attribute.__mro__:
        if "kukoindex" in klass.__dict__:
            descriptor = klass.__dict__["kukoindex"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel::attribute_has_kukoonly():
    assert hasattr(dbmodel::Attribute, "kukoonly")
    descriptor = None
    for klass in dbmodel::Attribute.__mro__:
        if "kukoonly" in klass.__dict__:
            descriptor = klass.__dict__["kukoonly"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel::attribute_has_isInDB():
    assert hasattr(dbmodel::Attribute, "isInDB")
    descriptor = None
    for klass in dbmodel::Attribute.__mro__:
        if "isInDB" in klass.__dict__:
            descriptor = klass.__dict__["isInDB"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel::attribute_has_kuko():
    assert hasattr(dbmodel::Attribute, "kuko")
    descriptor = None
    for klass in dbmodel::Attribute.__mro__:
        if "kuko" in klass.__dict__:
            descriptor = klass.__dict__["kuko"]
            break
    assert isinstance(descriptor, property)



def test_dbmodel::structoverride_is_not_abstract():
    assert not inspect.isabstract(dbmodel::StructOverride)


def test_dbmodel::structoverride_constructor_exists():
    assert callable(dbmodel::StructOverride.__init__)


def test_dbmodel::structoverride_constructor_args():
    sig = inspect.signature(dbmodel::StructOverride.__init__)
    params = list(sig.parameters.keys())
    assert "altname" in params, "Missing parameter 'altname'"

def test_dbmodel::structoverride_has_altname():
    assert hasattr(dbmodel::StructOverride, "altname")
    descriptor = None
    for klass in dbmodel::StructOverride.__mro__:
        if "altname" in klass.__dict__:
            descriptor = klass.__dict__["altname"]
            break
    assert isinstance(descriptor, property)



def test_dbmodel::structshare_is_not_abstract():
    assert not inspect.isabstract(dbmodel::StructShare)


def test_dbmodel::structshare_constructor_exists():
    assert callable(dbmodel::StructShare.__init__)


def test_dbmodel::structshare_constructor_args():
    sig = inspect.signature(dbmodel::StructShare.__init__)
    params = list(sig.parameters.keys())



def test_dbmodel::ltype_is_not_abstract():
    assert not inspect.isabstract(dbmodel::Ltype)


def test_dbmodel::ltype_constructor_exists():
    assert callable(dbmodel::Ltype.__init__)


def test_dbmodel::ltype_constructor_args():
    sig = inspect.signature(dbmodel::Ltype.__init__)
    params = list(sig.parameters.keys())



def test_dbmodel::pdb_is_not_abstract():
    assert not inspect.isabstract(dbmodel::Pdb)


def test_dbmodel::pdb_constructor_exists():
    assert callable(dbmodel::Pdb.__init__)


def test_dbmodel::pdb_constructor_args():
    sig = inspect.signature(dbmodel::Pdb.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "tablePartitioning" in params, "Missing parameter 'tablePartitioning'"
    assert "lockSchema" in params, "Missing parameter 'lockSchema'"

def test_dbmodel::pdb_has_name():
    assert hasattr(dbmodel::Pdb, "name")
    descriptor = None
    for klass in dbmodel::Pdb.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel::pdb_has_tablePartitioning():
    assert hasattr(dbmodel::Pdb, "tablePartitioning")
    descriptor = None
    for klass in dbmodel::Pdb.__mro__:
        if "tablePartitioning" in klass.__dict__:
            descriptor = klass.__dict__["tablePartitioning"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel::pdb_has_lockSchema():
    assert hasattr(dbmodel::Pdb, "lockSchema")
    descriptor = None
    for klass in dbmodel::Pdb.__mro__:
        if "lockSchema" in klass.__dict__:
            descriptor = klass.__dict__["lockSchema"]
            break
    assert isinstance(descriptor, property)



def test_dbmodel::index_is_not_abstract():
    assert not inspect.isabstract(dbmodel::Index)


def test_dbmodel::index_constructor_exists():
    assert callable(dbmodel::Index.__init__)


def test_dbmodel::index_constructor_args():
    sig = inspect.signature(dbmodel::Index.__init__)
    params = list(sig.parameters.keys())
    assert "unique" in params, "Missing parameter 'unique'"
    assert "kuko" in params, "Missing parameter 'kuko'"
    assert "name" in params, "Missing parameter 'name'"

def test_dbmodel::index_has_unique():
    assert hasattr(dbmodel::Index, "unique")
    descriptor = None
    for klass in dbmodel::Index.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel::index_has_kuko():
    assert hasattr(dbmodel::Index, "kuko")
    descriptor = None
    for klass in dbmodel::Index.__mro__:
        if "kuko" in klass.__dict__:
            descriptor = klass.__dict__["kuko"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel::index_has_name():
    assert hasattr(dbmodel::Index, "name")
    descriptor = None
    for klass in dbmodel::Index.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dbmodel::dbmodel_is_not_abstract():
    assert not inspect.isabstract(dbmodel::DbModel)


def test_dbmodel::dbmodel_constructor_exists():
    assert callable(dbmodel::DbModel.__init__)


def test_dbmodel::dbmodel_constructor_args():
    sig = inspect.signature(dbmodel::DbModel.__init__)
    params = list(sig.parameters.keys())
    assert "kobeType" in params, "Missing parameter 'kobeType'"
    assert "kudaType" in params, "Missing parameter 'kudaType'"
    assert "version" in params, "Missing parameter 'version'"
    assert "name" in params, "Missing parameter 'name'"
    assert "mtype" in params, "Missing parameter 'mtype'"
    assert "doAll" in params, "Missing parameter 'doAll'"

def test_dbmodel::dbmodel_has_kobeType():
    assert hasattr(dbmodel::DbModel, "kobeType")
    descriptor = None
    for klass in dbmodel::DbModel.__mro__:
        if "kobeType" in klass.__dict__:
            descriptor = klass.__dict__["kobeType"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel::dbmodel_has_kudaType():
    assert hasattr(dbmodel::DbModel, "kudaType")
    descriptor = None
    for klass in dbmodel::DbModel.__mro__:
        if "kudaType" in klass.__dict__:
            descriptor = klass.__dict__["kudaType"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel::dbmodel_has_version():
    assert hasattr(dbmodel::DbModel, "version")
    descriptor = None
    for klass in dbmodel::DbModel.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel::dbmodel_has_name():
    assert hasattr(dbmodel::DbModel, "name")
    descriptor = None
    for klass in dbmodel::DbModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel::dbmodel_has_mtype():
    assert hasattr(dbmodel::DbModel, "mtype")
    descriptor = None
    for klass in dbmodel::DbModel.__mro__:
        if "mtype" in klass.__dict__:
            descriptor = klass.__dict__["mtype"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel::dbmodel_has_doAll():
    assert hasattr(dbmodel::DbModel, "doAll")
    descriptor = None
    for klass in dbmodel::DbModel.__mro__:
        if "doAll" in klass.__dict__:
            descriptor = klass.__dict__["doAll"]
            break
    assert isinstance(descriptor, property)



def test_classorduplicate_is_not_abstract():
    assert not inspect.isabstract(ClassOrDuplicate)


def test_classorduplicate_constructor_exists():
    assert callable(ClassOrDuplicate.__init__)


def test_classorduplicate_constructor_args():
    sig = inspect.signature(ClassOrDuplicate.__init__)
    params = list(sig.parameters.keys())



def test_dbmodel::duplicate_is_not_abstract():
    assert not inspect.isabstract(dbmodel::Duplicate)


def test_dbmodel::duplicate_constructor_exists():
    assert callable(dbmodel::Duplicate.__init__)


def test_dbmodel::duplicate_constructor_args():
    sig = inspect.signature(dbmodel::Duplicate.__init__)
    params = list(sig.parameters.keys())



def test_dbmodel::class_is_not_abstract():
    assert not inspect.isabstract(dbmodel::Class)


def test_dbmodel::class_constructor_exists():
    assert callable(dbmodel::Class.__init__)


def test_dbmodel::class_constructor_args():
    sig = inspect.signature(dbmodel::Class.__init__)
    params = list(sig.parameters.keys())
    assert "archivIndex" in params, "Missing parameter 'archivIndex'"
    assert "noDBio" in params, "Missing parameter 'noDBio'"
    assert "descr" in params, "Missing parameter 'descr'"
    assert "vmin" in params, "Missing parameter 'vmin'"
    assert "publish" in params, "Missing parameter 'publish'"
    assert "whereclause" in params, "Missing parameter 'whereclause'"
    assert "vmaj" in params, "Missing parameter 'vmaj'"
    assert "aName" in params, "Missing parameter 'aName'"
    assert "pubspec" in params, "Missing parameter 'pubspec'"
    assert "pubname" in params, "Missing parameter 'pubname'"

def test_dbmodel::class_has_archivIndex():
    assert hasattr(dbmodel::Class, "archivIndex")
    descriptor = None
    for klass in dbmodel::Class.__mro__:
        if "archivIndex" in klass.__dict__:
            descriptor = klass.__dict__["archivIndex"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel::class_has_noDBio():
    assert hasattr(dbmodel::Class, "noDBio")
    descriptor = None
    for klass in dbmodel::Class.__mro__:
        if "noDBio" in klass.__dict__:
            descriptor = klass.__dict__["noDBio"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel::class_has_descr():
    assert hasattr(dbmodel::Class, "descr")
    descriptor = None
    for klass in dbmodel::Class.__mro__:
        if "descr" in klass.__dict__:
            descriptor = klass.__dict__["descr"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel::class_has_vmin():
    assert hasattr(dbmodel::Class, "vmin")
    descriptor = None
    for klass in dbmodel::Class.__mro__:
        if "vmin" in klass.__dict__:
            descriptor = klass.__dict__["vmin"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel::class_has_publish():
    assert hasattr(dbmodel::Class, "publish")
    descriptor = None
    for klass in dbmodel::Class.__mro__:
        if "publish" in klass.__dict__:
            descriptor = klass.__dict__["publish"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel::class_has_whereclause():
    assert hasattr(dbmodel::Class, "whereclause")
    descriptor = None
    for klass in dbmodel::Class.__mro__:
        if "whereclause" in klass.__dict__:
            descriptor = klass.__dict__["whereclause"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel::class_has_vmaj():
    assert hasattr(dbmodel::Class, "vmaj")
    descriptor = None
    for klass in dbmodel::Class.__mro__:
        if "vmaj" in klass.__dict__:
            descriptor = klass.__dict__["vmaj"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel::class_has_aName():
    assert hasattr(dbmodel::Class, "aName")
    descriptor = None
    for klass in dbmodel::Class.__mro__:
        if "aName" in klass.__dict__:
            descriptor = klass.__dict__["aName"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel::class_has_pubspec():
    assert hasattr(dbmodel::Class, "pubspec")
    descriptor = None
    for klass in dbmodel::Class.__mro__:
        if "pubspec" in klass.__dict__:
            descriptor = klass.__dict__["pubspec"]
            break
    assert isinstance(descriptor, property)

def test_dbmodel::class_has_pubname():
    assert hasattr(dbmodel::Class, "pubname")
    descriptor = None
    for klass in dbmodel::Class.__mro__:
        if "pubname" in klass.__dict__:
            descriptor = klass.__dict__["pubname"]
            break
    assert isinstance(descriptor, property)



def test_dbmodel::subject_is_not_abstract():
    assert not inspect.isabstract(dbmodel::Subject)


def test_dbmodel::subject_constructor_exists():
    assert callable(dbmodel::Subject.__init__)


def test_dbmodel::subject_constructor_args():
    sig = inspect.signature(dbmodel::Subject.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dbmodel::subject_has_name():
    assert hasattr(dbmodel::Subject, "name")
    descriptor = None
    for klass in dbmodel::Subject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dbmodel::import_is_not_abstract():
    assert not inspect.isabstract(dbmodel::Import)


def test_dbmodel::import_constructor_exists():
    assert callable(dbmodel::Import.__init__)


def test_dbmodel::import_constructor_args():
    sig = inspect.signature(dbmodel::Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_dbmodel::import_has_importedNamespace():
    assert hasattr(dbmodel::Import, "importedNamespace")
    descriptor = None
    for klass in dbmodel::Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)

def test_kudareplicate_exists():
    # Check that the Enumeration exists
    assert KudaReplicate is not None

def test_kudareplicate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in KudaReplicate]
    expected_literals = [
        "PUBLISHSTV",
        "SNAP",
        "PUBLISH",
        "DWH",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in KudaReplicate"

def test_kobetype_exists():
    # Check that the Enumeration exists
    assert KobeType is not None

def test_kobetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in KobeType]
    expected_literals = [
        "AUSW",
        "MAIN",
        "KORA",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in KobeType"

def test_mtype_exists():
    # Check that the Enumeration exists
    assert Mtype is not None

def test_mtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Mtype]
    expected_literals = [
        "KOBE",
        "KUDA",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Mtype"

def test_lockschema_exists():
    # Check that the Enumeration exists
    assert LockSchema is not None

def test_lockschema_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LockSchema]
    expected_literals = [
        "ALLPAGES",
        "DATAROWS",
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
        "MAIN",
        "PUBLISH",
        "TIPO",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in KudaType"

def test_physicaldatabase_exists():
    # Check that the Enumeration exists
    assert PhysicalDatabase is not None

def test_physicaldatabase_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PhysicalDatabase]
    expected_literals = [
        "PDB_ABFRAGE_BUCH_STAMM",
        "PDB_AUSW_KOBE_PKT_STAMM",
        "PDB_MANDANT_PKT_STAMM",
        "PDB_KOBE_KNDTEST",
        "PDB_PART_PKT_DATA",
        "PDB_KOBE_DEZ_STAMM",
        "PDB_PART_TAG_A",
        "PDB_PART_AUFT",
        "PDB_ABFRAGE_FZK",
        "PDB_PART_BUCH_STAMM",
        "PDB_KOBE_AUSW_ADMIN",
        "PDB_KOBE_DATA",
        "PDB_KOBE_PMON",
        "PDB_MANDANT_TAG_A",
        "PDB_AUSW_KOBE_BUCH_STAMM",
        "PDB_PART_MON",
        "PDB_ABFRAGE_PKT_STAMM",
        "PDB_PART_JAHR",
        "PDB_AUSW_KOBE_ARCHIV",
        "PDB_ABFRAGE_ARCHIV",
        "PDB_MANDANT_BUCH_PROV",
        "PDB_KUDA_TRANS_TRANSIT",
        "PDB_KOBE_GLOBAL",
        "PDB_ABFRAGE_VSTI",
        "PDB_PART_PKT_STAMM",
        "PDB_PART_TAG",
        "PDB_AUSW_KOBE_MON",
        "PDB_MANDANT_BUCH_STAMM",
        "PDB_AUSW_KOBE_STATISTIK",
        "PDB_MANDANT_MON",
        "PDB_ABFRAGE_ETV",
        "PDB_KOBE_STAMM",
        "PDB_ABFRAGE_MON",
        "PDB_MANDANT_TAG",
        "PDB_PART_BUCH_PROV",
        "PDB_MANDANT_PKT_DATA",
        "PDB_KOBE_STEUERUNG",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PhysicalDatabase"


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
dbmodel::ClassOrDuplicate_strategy = st.builds(
    dbmodel::ClassOrDuplicate,
    abbrev=
        safe_text,
    name=
        safe_text,
    reps=
        safe_text
)
dbmodel::Stype_strategy = st.builds(
    dbmodel::Stype,
)
dbmodel::Type_strategy = st.builds(
    dbmodel::Type,
)
dbmodel::IndexRef_strategy = st.builds(
    dbmodel::IndexRef,
    isPrimkey=
        st.booleans(),
    clustered=
        st.booleans()
)
dbmodel::Primkey_strategy = st.builds(
    dbmodel::Primkey,
)
dbmodel::Attribute_strategy = st.builds(
    dbmodel::Attribute,
    isPublic=
        st.booleans(),
    shared=
        st.booleans(),
    exttable=
        safe_text,
    immutable=
        st.booleans(),
    sybident=
        st.booleans(),
    descr=
        safe_text,
    name=
        safe_text,
    archiv=
        st.booleans(),
    nullOK=
        st.booleans(),
    aName=
        safe_text,
    optional=
        st.booleans(),
    extattr=
        safe_text,
    foreign=
        st.booleans(),
    kukoindex=
        st.booleans(),
    kukoonly=
        st.booleans(),
    isInDB=
        st.booleans(),
    kuko=
        st.booleans()
)
dbmodel::StructOverride_strategy = st.builds(
    dbmodel::StructOverride,
    altname=
        safe_text
)
dbmodel::StructShare_strategy = st.builds(
    dbmodel::StructShare,
)
dbmodel::Ltype_strategy = st.builds(
    dbmodel::Ltype,
)
dbmodel::Pdb_strategy = st.builds(
    dbmodel::Pdb,
    name=
        safe_text,
    tablePartitioning=
        st.integers(),
    lockSchema=
        safe_text
)
dbmodel::Index_strategy = st.builds(
    dbmodel::Index,
    unique=
        st.booleans(),
    kuko=
        st.booleans(),
    name=
        safe_text
)
dbmodel::DbModel_strategy = st.builds(
    dbmodel::DbModel,
    kobeType=
        safe_text,
    kudaType=
        safe_text,
    version=
        safe_text,
    name=
        safe_text,
    mtype=
        safe_text,
    doAll=
        st.booleans()
)
ClassOrDuplicate_strategy = st.builds(
    ClassOrDuplicate,
)
dbmodel::Duplicate_strategy = st.builds(
    dbmodel::Duplicate,
)
dbmodel::Class_strategy = st.builds(
    dbmodel::Class,
    archivIndex=
        safe_text,
    noDBio=
        st.booleans(),
    descr=
        safe_text,
    vmin=
        st.integers(),
    publish=
        st.booleans(),
    whereclause=
        safe_text,
    vmaj=
        st.integers(),
    aName=
        safe_text,
    pubspec=
        st.booleans(),
    pubname=
        safe_text
)
dbmodel::Subject_strategy = st.builds(
    dbmodel::Subject,
    name=
        safe_text
)
dbmodel::Import_strategy = st.builds(
    dbmodel::Import,
    importedNamespace=
        safe_text
)

@given(instance=dbmodel::ClassOrDuplicate_strategy)
@settings(max_examples=50)
def test_dbmodel::classorduplicate_instantiation(instance):
    assert isinstance(instance, dbmodel::ClassOrDuplicate)

@given(instance=dbmodel::ClassOrDuplicate_strategy)
def test_dbmodel::classorduplicate_abbrev_type(instance):
    assert isinstance(instance.abbrev, str)


@given(instance=dbmodel::ClassOrDuplicate_strategy)
def test_dbmodel::classorduplicate_abbrev_setter(instance):
    original = instance.abbrev
    instance.abbrev = original
    assert instance.abbrev == original

@given(instance=dbmodel::ClassOrDuplicate_strategy)
def test_dbmodel::classorduplicate_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dbmodel::ClassOrDuplicate_strategy)
def test_dbmodel::classorduplicate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dbmodel::ClassOrDuplicate_strategy)
def test_dbmodel::classorduplicate_reps_type(instance):
    assert isinstance(instance.reps, str)


@given(instance=dbmodel::ClassOrDuplicate_strategy)
def test_dbmodel::classorduplicate_reps_setter(instance):
    original = instance.reps
    instance.reps = original
    assert instance.reps == original

@given(instance=dbmodel::Stype_strategy)
@settings(max_examples=50)
def test_dbmodel::stype_instantiation(instance):
    assert isinstance(instance, dbmodel::Stype)

@given(instance=dbmodel::Type_strategy)
@settings(max_examples=50)
def test_dbmodel::type_instantiation(instance):
    assert isinstance(instance, dbmodel::Type)

@given(instance=dbmodel::IndexRef_strategy)
@settings(max_examples=50)
def test_dbmodel::indexref_instantiation(instance):
    assert isinstance(instance, dbmodel::IndexRef)

@given(instance=dbmodel::IndexRef_strategy)
def test_dbmodel::indexref_isPrimkey_type(instance):
    assert isinstance(instance.isPrimkey, bool)


@given(instance=dbmodel::IndexRef_strategy)
def test_dbmodel::indexref_isPrimkey_setter(instance):
    original = instance.isPrimkey
    instance.isPrimkey = original
    assert instance.isPrimkey == original

@given(instance=dbmodel::IndexRef_strategy)
def test_dbmodel::indexref_clustered_type(instance):
    assert isinstance(instance.clustered, bool)


@given(instance=dbmodel::IndexRef_strategy)
def test_dbmodel::indexref_clustered_setter(instance):
    original = instance.clustered
    instance.clustered = original
    assert instance.clustered == original

@given(instance=dbmodel::Primkey_strategy)
@settings(max_examples=50)
def test_dbmodel::primkey_instantiation(instance):
    assert isinstance(instance, dbmodel::Primkey)

@given(instance=dbmodel::Attribute_strategy)
@settings(max_examples=50)
def test_dbmodel::attribute_instantiation(instance):
    assert isinstance(instance, dbmodel::Attribute)

@given(instance=dbmodel::Attribute_strategy)
def test_dbmodel::attribute_isPublic_type(instance):
    assert isinstance(instance.isPublic, bool)


@given(instance=dbmodel::Attribute_strategy)
def test_dbmodel::attribute_isPublic_setter(instance):
    original = instance.isPublic
    instance.isPublic = original
    assert instance.isPublic == original

@given(instance=dbmodel::Attribute_strategy)
def test_dbmodel::attribute_shared_type(instance):
    assert isinstance(instance.shared, bool)


@given(instance=dbmodel::Attribute_strategy)
def test_dbmodel::attribute_shared_setter(instance):
    original = instance.shared
    instance.shared = original
    assert instance.shared == original

@given(instance=dbmodel::Attribute_strategy)
def test_dbmodel::attribute_exttable_type(instance):
    assert isinstance(instance.exttable, str)


@given(instance=dbmodel::Attribute_strategy)
def test_dbmodel::attribute_exttable_setter(instance):
    original = instance.exttable
    instance.exttable = original
    assert instance.exttable == original

@given(instance=dbmodel::Attribute_strategy)
def test_dbmodel::attribute_immutable_type(instance):
    assert isinstance(instance.immutable, bool)


@given(instance=dbmodel::Attribute_strategy)
def test_dbmodel::attribute_immutable_setter(instance):
    original = instance.immutable
    instance.immutable = original
    assert instance.immutable == original

@given(instance=dbmodel::Attribute_strategy)
def test_dbmodel::attribute_sybident_type(instance):
    assert isinstance(instance.sybident, bool)


@given(instance=dbmodel::Attribute_strategy)
def test_dbmodel::attribute_sybident_setter(instance):
    original = instance.sybident
    instance.sybident = original
    assert instance.sybident == original

@given(instance=dbmodel::Attribute_strategy)
def test_dbmodel::attribute_descr_type(instance):
    assert isinstance(instance.descr, str)


@given(instance=dbmodel::Attribute_strategy)
def test_dbmodel::attribute_descr_setter(instance):
    original = instance.descr
    instance.descr = original
    assert instance.descr == original

@given(instance=dbmodel::Attribute_strategy)
def test_dbmodel::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dbmodel::Attribute_strategy)
def test_dbmodel::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dbmodel::Attribute_strategy)
def test_dbmodel::attribute_archiv_type(instance):
    assert isinstance(instance.archiv, bool)


@given(instance=dbmodel::Attribute_strategy)
def test_dbmodel::attribute_archiv_setter(instance):
    original = instance.archiv
    instance.archiv = original
    assert instance.archiv == original

@given(instance=dbmodel::Attribute_strategy)
def test_dbmodel::attribute_nullOK_type(instance):
    assert isinstance(instance.nullOK, bool)


@given(instance=dbmodel::Attribute_strategy)
def test_dbmodel::attribute_nullOK_setter(instance):
    original = instance.nullOK
    instance.nullOK = original
    assert instance.nullOK == original

@given(instance=dbmodel::Attribute_strategy)
def test_dbmodel::attribute_aName_type(instance):
    assert isinstance(instance.aName, str)


@given(instance=dbmodel::Attribute_strategy)
def test_dbmodel::attribute_aName_setter(instance):
    original = instance.aName
    instance.aName = original
    assert instance.aName == original

@given(instance=dbmodel::Attribute_strategy)
def test_dbmodel::attribute_optional_type(instance):
    assert isinstance(instance.optional, bool)


@given(instance=dbmodel::Attribute_strategy)
def test_dbmodel::attribute_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=dbmodel::Attribute_strategy)
def test_dbmodel::attribute_extattr_type(instance):
    assert isinstance(instance.extattr, str)


@given(instance=dbmodel::Attribute_strategy)
def test_dbmodel::attribute_extattr_setter(instance):
    original = instance.extattr
    instance.extattr = original
    assert instance.extattr == original

@given(instance=dbmodel::Attribute_strategy)
def test_dbmodel::attribute_foreign_type(instance):
    assert isinstance(instance.foreign, bool)


@given(instance=dbmodel::Attribute_strategy)
def test_dbmodel::attribute_foreign_setter(instance):
    original = instance.foreign
    instance.foreign = original
    assert instance.foreign == original

@given(instance=dbmodel::Attribute_strategy)
def test_dbmodel::attribute_kukoindex_type(instance):
    assert isinstance(instance.kukoindex, bool)


@given(instance=dbmodel::Attribute_strategy)
def test_dbmodel::attribute_kukoindex_setter(instance):
    original = instance.kukoindex
    instance.kukoindex = original
    assert instance.kukoindex == original

@given(instance=dbmodel::Attribute_strategy)
def test_dbmodel::attribute_kukoonly_type(instance):
    assert isinstance(instance.kukoonly, bool)


@given(instance=dbmodel::Attribute_strategy)
def test_dbmodel::attribute_kukoonly_setter(instance):
    original = instance.kukoonly
    instance.kukoonly = original
    assert instance.kukoonly == original

@given(instance=dbmodel::Attribute_strategy)
def test_dbmodel::attribute_isInDB_type(instance):
    assert isinstance(instance.isInDB, bool)


@given(instance=dbmodel::Attribute_strategy)
def test_dbmodel::attribute_isInDB_setter(instance):
    original = instance.isInDB
    instance.isInDB = original
    assert instance.isInDB == original

@given(instance=dbmodel::Attribute_strategy)
def test_dbmodel::attribute_kuko_type(instance):
    assert isinstance(instance.kuko, bool)


@given(instance=dbmodel::Attribute_strategy)
def test_dbmodel::attribute_kuko_setter(instance):
    original = instance.kuko
    instance.kuko = original
    assert instance.kuko == original

@given(instance=dbmodel::StructOverride_strategy)
@settings(max_examples=50)
def test_dbmodel::structoverride_instantiation(instance):
    assert isinstance(instance, dbmodel::StructOverride)

@given(instance=dbmodel::StructOverride_strategy)
def test_dbmodel::structoverride_altname_type(instance):
    assert isinstance(instance.altname, str)


@given(instance=dbmodel::StructOverride_strategy)
def test_dbmodel::structoverride_altname_setter(instance):
    original = instance.altname
    instance.altname = original
    assert instance.altname == original

@given(instance=dbmodel::StructShare_strategy)
@settings(max_examples=50)
def test_dbmodel::structshare_instantiation(instance):
    assert isinstance(instance, dbmodel::StructShare)

@given(instance=dbmodel::Ltype_strategy)
@settings(max_examples=50)
def test_dbmodel::ltype_instantiation(instance):
    assert isinstance(instance, dbmodel::Ltype)

@given(instance=dbmodel::Pdb_strategy)
@settings(max_examples=50)
def test_dbmodel::pdb_instantiation(instance):
    assert isinstance(instance, dbmodel::Pdb)

@given(instance=dbmodel::Pdb_strategy)
def test_dbmodel::pdb_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dbmodel::Pdb_strategy)
def test_dbmodel::pdb_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dbmodel::Pdb_strategy)
def test_dbmodel::pdb_tablePartitioning_type(instance):
    assert isinstance(instance.tablePartitioning, int)


@given(instance=dbmodel::Pdb_strategy)
def test_dbmodel::pdb_tablePartitioning_setter(instance):
    original = instance.tablePartitioning
    instance.tablePartitioning = original
    assert instance.tablePartitioning == original

@given(instance=dbmodel::Pdb_strategy)
def test_dbmodel::pdb_lockSchema_type(instance):
    assert isinstance(instance.lockSchema, str)


@given(instance=dbmodel::Pdb_strategy)
def test_dbmodel::pdb_lockSchema_setter(instance):
    original = instance.lockSchema
    instance.lockSchema = original
    assert instance.lockSchema == original

@given(instance=dbmodel::Index_strategy)
@settings(max_examples=50)
def test_dbmodel::index_instantiation(instance):
    assert isinstance(instance, dbmodel::Index)

@given(instance=dbmodel::Index_strategy)
def test_dbmodel::index_unique_type(instance):
    assert isinstance(instance.unique, bool)


@given(instance=dbmodel::Index_strategy)
def test_dbmodel::index_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original

@given(instance=dbmodel::Index_strategy)
def test_dbmodel::index_kuko_type(instance):
    assert isinstance(instance.kuko, bool)


@given(instance=dbmodel::Index_strategy)
def test_dbmodel::index_kuko_setter(instance):
    original = instance.kuko
    instance.kuko = original
    assert instance.kuko == original

@given(instance=dbmodel::Index_strategy)
def test_dbmodel::index_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dbmodel::Index_strategy)
def test_dbmodel::index_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dbmodel::DbModel_strategy)
@settings(max_examples=50)
def test_dbmodel::dbmodel_instantiation(instance):
    assert isinstance(instance, dbmodel::DbModel)

@given(instance=dbmodel::DbModel_strategy)
def test_dbmodel::dbmodel_kobeType_type(instance):
    assert isinstance(instance.kobeType, str)


@given(instance=dbmodel::DbModel_strategy)
def test_dbmodel::dbmodel_kobeType_setter(instance):
    original = instance.kobeType
    instance.kobeType = original
    assert instance.kobeType == original

@given(instance=dbmodel::DbModel_strategy)
def test_dbmodel::dbmodel_kudaType_type(instance):
    assert isinstance(instance.kudaType, str)


@given(instance=dbmodel::DbModel_strategy)
def test_dbmodel::dbmodel_kudaType_setter(instance):
    original = instance.kudaType
    instance.kudaType = original
    assert instance.kudaType == original

@given(instance=dbmodel::DbModel_strategy)
def test_dbmodel::dbmodel_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=dbmodel::DbModel_strategy)
def test_dbmodel::dbmodel_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=dbmodel::DbModel_strategy)
def test_dbmodel::dbmodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dbmodel::DbModel_strategy)
def test_dbmodel::dbmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dbmodel::DbModel_strategy)
def test_dbmodel::dbmodel_mtype_type(instance):
    assert isinstance(instance.mtype, str)


@given(instance=dbmodel::DbModel_strategy)
def test_dbmodel::dbmodel_mtype_setter(instance):
    original = instance.mtype
    instance.mtype = original
    assert instance.mtype == original

@given(instance=dbmodel::DbModel_strategy)
def test_dbmodel::dbmodel_doAll_type(instance):
    assert isinstance(instance.doAll, bool)


@given(instance=dbmodel::DbModel_strategy)
def test_dbmodel::dbmodel_doAll_setter(instance):
    original = instance.doAll
    instance.doAll = original
    assert instance.doAll == original

@given(instance=ClassOrDuplicate_strategy)
@settings(max_examples=50)
def test_classorduplicate_instantiation(instance):
    assert isinstance(instance, ClassOrDuplicate)

@given(instance=dbmodel::Duplicate_strategy)
@settings(max_examples=50)
def test_dbmodel::duplicate_instantiation(instance):
    assert isinstance(instance, dbmodel::Duplicate)

@given(instance=dbmodel::Class_strategy)
@settings(max_examples=50)
def test_dbmodel::class_instantiation(instance):
    assert isinstance(instance, dbmodel::Class)

@given(instance=dbmodel::Class_strategy)
def test_dbmodel::class_archivIndex_type(instance):
    assert isinstance(instance.archivIndex, str)


@given(instance=dbmodel::Class_strategy)
def test_dbmodel::class_archivIndex_setter(instance):
    original = instance.archivIndex
    instance.archivIndex = original
    assert instance.archivIndex == original

@given(instance=dbmodel::Class_strategy)
def test_dbmodel::class_noDBio_type(instance):
    assert isinstance(instance.noDBio, bool)


@given(instance=dbmodel::Class_strategy)
def test_dbmodel::class_noDBio_setter(instance):
    original = instance.noDBio
    instance.noDBio = original
    assert instance.noDBio == original

@given(instance=dbmodel::Class_strategy)
def test_dbmodel::class_descr_type(instance):
    assert isinstance(instance.descr, str)


@given(instance=dbmodel::Class_strategy)
def test_dbmodel::class_descr_setter(instance):
    original = instance.descr
    instance.descr = original
    assert instance.descr == original

@given(instance=dbmodel::Class_strategy)
def test_dbmodel::class_vmin_type(instance):
    assert isinstance(instance.vmin, int)


@given(instance=dbmodel::Class_strategy)
def test_dbmodel::class_vmin_setter(instance):
    original = instance.vmin
    instance.vmin = original
    assert instance.vmin == original

@given(instance=dbmodel::Class_strategy)
def test_dbmodel::class_publish_type(instance):
    assert isinstance(instance.publish, bool)


@given(instance=dbmodel::Class_strategy)
def test_dbmodel::class_publish_setter(instance):
    original = instance.publish
    instance.publish = original
    assert instance.publish == original

@given(instance=dbmodel::Class_strategy)
def test_dbmodel::class_whereclause_type(instance):
    assert isinstance(instance.whereclause, str)


@given(instance=dbmodel::Class_strategy)
def test_dbmodel::class_whereclause_setter(instance):
    original = instance.whereclause
    instance.whereclause = original
    assert instance.whereclause == original

@given(instance=dbmodel::Class_strategy)
def test_dbmodel::class_vmaj_type(instance):
    assert isinstance(instance.vmaj, int)


@given(instance=dbmodel::Class_strategy)
def test_dbmodel::class_vmaj_setter(instance):
    original = instance.vmaj
    instance.vmaj = original
    assert instance.vmaj == original

@given(instance=dbmodel::Class_strategy)
def test_dbmodel::class_aName_type(instance):
    assert isinstance(instance.aName, str)


@given(instance=dbmodel::Class_strategy)
def test_dbmodel::class_aName_setter(instance):
    original = instance.aName
    instance.aName = original
    assert instance.aName == original

@given(instance=dbmodel::Class_strategy)
def test_dbmodel::class_pubspec_type(instance):
    assert isinstance(instance.pubspec, bool)


@given(instance=dbmodel::Class_strategy)
def test_dbmodel::class_pubspec_setter(instance):
    original = instance.pubspec
    instance.pubspec = original
    assert instance.pubspec == original

@given(instance=dbmodel::Class_strategy)
def test_dbmodel::class_pubname_type(instance):
    assert isinstance(instance.pubname, str)


@given(instance=dbmodel::Class_strategy)
def test_dbmodel::class_pubname_setter(instance):
    original = instance.pubname
    instance.pubname = original
    assert instance.pubname == original

@given(instance=dbmodel::Subject_strategy)
@settings(max_examples=50)
def test_dbmodel::subject_instantiation(instance):
    assert isinstance(instance, dbmodel::Subject)

@given(instance=dbmodel::Subject_strategy)
def test_dbmodel::subject_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dbmodel::Subject_strategy)
def test_dbmodel::subject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dbmodel::Import_strategy)
@settings(max_examples=50)
def test_dbmodel::import_instantiation(instance):
    assert isinstance(instance, dbmodel::Import)

@given(instance=dbmodel::Import_strategy)
def test_dbmodel::import_importedNamespace_type(instance):
    assert isinstance(instance.importedNamespace, str)


@given(instance=dbmodel::Import_strategy)
def test_dbmodel::import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original
