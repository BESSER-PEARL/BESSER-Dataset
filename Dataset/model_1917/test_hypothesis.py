import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Conflict,
    mancoosimm::OrConflict,
    mancoosimm::AndConflict,
    mancoosimm::SingleConflict,
    mancoosimm::SharedLibrary,
    mancoosimm::MimeType,
    mancoosimm::MimeTypeHandler,
    mancoosimm::Boot,
    File,
    mancoosimm::InformationFile,
    mancoosimm::LibraryCache,
    mancoosimm::MimeTypeHandlerCache,
    mancoosimm::DesktopDB,
    mancoosimm::IconCache,
    mancoosimm::Menu,
    mancoosimm::GConf,
    mancoosimm::XFontCache,
    mancoosimm::ModuleCache,
    mancoosimm::NotInv,
    mancoosimm::OrInv,
    mancoosimm::AndInv,
    InstalledPackage,
    mancoosimm::BinPackage,
    Dependence,
    mancoosimm::SingleDep,
    mancoosimm::OrDep,
    mancoosimm::AndDep,
    mancoosimm::Conflict,
    mancoosimm::DocumentationFile,
    mancoosimm::VirtualPackage,
    UnpackedPackage,
    mancoosimm::HalfConfiguredReinstRequiredPackage,
    mancoosimm::HalfConfiguredPackage,
    mancoosimm::Dependence,
    mancoosimm::SrcPackage,
    NamedElement,
    mancoosimm::FileSystem,
    mancoosimm::Group,
    mancoosimm::SkeeperDocument,
    mancoosimm::SGMLDocument,
    mancoosimm::Alternative,
    mancoosimm::SGMLCatalog,
    mancoosimm::File,
    mancoosimm::ApplicationMenuCatalog,
    mancoosimm::SkeeperCatalog,
    mancoosimm::Environment,
    mancoosimm::Atom,
    mancoosimm::XFont,
    mancoosimm::EmacsPackage,
    mancoosimm::Package,
    mancoosimm::User,
    mancoosimm::Service,
    mancoosimm::Module,
    mancoosimm::MenuEntry,
    mancoosimm::Invariant,
    Package,
    mancoosimm::InstalledPackage,
    mancoosimm::NotInstalledPackage,
    mancoosimm::HalfInstalledReinstRequiredPackage,
    mancoosimm::HalfInstalledPackage,
    mancoosimm::UnpackedPackage,
    mancoosimm::ConfigFilesPackage,
    mancoosimm::PackageSetting,
    mancoosimm::Configuration,
    mancoosimm::NamedElement,
    StatusType,
    VersionType,
    PriorityType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_conflict_is_not_abstract():
    assert not inspect.isabstract(Conflict)


def test_conflict_constructor_exists():
    assert callable(Conflict.__init__)


def test_conflict_constructor_args():
    sig = inspect.signature(Conflict.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::orconflict_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::OrConflict)


def test_mancoosimm::orconflict_constructor_exists():
    assert callable(mancoosimm::OrConflict.__init__)


def test_mancoosimm::orconflict_constructor_args():
    sig = inspect.signature(mancoosimm::OrConflict.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::andconflict_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::AndConflict)


def test_mancoosimm::andconflict_constructor_exists():
    assert callable(mancoosimm::AndConflict.__init__)


def test_mancoosimm::andconflict_constructor_args():
    sig = inspect.signature(mancoosimm::AndConflict.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::singleconflict_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::SingleConflict)


def test_mancoosimm::singleconflict_constructor_exists():
    assert callable(mancoosimm::SingleConflict.__init__)


def test_mancoosimm::singleconflict_constructor_args():
    sig = inspect.signature(mancoosimm::SingleConflict.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "version" in params, "Missing parameter 'version'"

def test_mancoosimm::singleconflict_has_value():
    assert hasattr(mancoosimm::SingleConflict, "value")
    descriptor = None
    for klass in mancoosimm::SingleConflict.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::singleconflict_has_version():
    assert hasattr(mancoosimm::SingleConflict, "version")
    descriptor = None
    for klass in mancoosimm::SingleConflict.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_mancoosimm::sharedlibrary_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::SharedLibrary)


def test_mancoosimm::sharedlibrary_constructor_exists():
    assert callable(mancoosimm::SharedLibrary.__init__)


def test_mancoosimm::sharedlibrary_constructor_args():
    sig = inspect.signature(mancoosimm::SharedLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "version" in params, "Missing parameter 'version'"

def test_mancoosimm::sharedlibrary_has_name():
    assert hasattr(mancoosimm::SharedLibrary, "name")
    descriptor = None
    for klass in mancoosimm::SharedLibrary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::sharedlibrary_has_version():
    assert hasattr(mancoosimm::SharedLibrary, "version")
    descriptor = None
    for klass in mancoosimm::SharedLibrary.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_mancoosimm::mimetype_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::MimeType)


def test_mancoosimm::mimetype_constructor_exists():
    assert callable(mancoosimm::MimeType.__init__)


def test_mancoosimm::mimetype_constructor_args():
    sig = inspect.signature(mancoosimm::MimeType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "extension" in params, "Missing parameter 'extension'"

def test_mancoosimm::mimetype_has_name():
    assert hasattr(mancoosimm::MimeType, "name")
    descriptor = None
    for klass in mancoosimm::MimeType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::mimetype_has_extension():
    assert hasattr(mancoosimm::MimeType, "extension")
    descriptor = None
    for klass in mancoosimm::MimeType.__mro__:
        if "extension" in klass.__dict__:
            descriptor = klass.__dict__["extension"]
            break
    assert isinstance(descriptor, property)



def test_mancoosimm::mimetypehandler_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::MimeTypeHandler)


def test_mancoosimm::mimetypehandler_constructor_exists():
    assert callable(mancoosimm::MimeTypeHandler.__init__)


def test_mancoosimm::mimetypehandler_constructor_args():
    sig = inspect.signature(mancoosimm::MimeTypeHandler.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::boot_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::Boot)


def test_mancoosimm::boot_constructor_exists():
    assert callable(mancoosimm::Boot.__init__)


def test_mancoosimm::boot_constructor_args():
    sig = inspect.signature(mancoosimm::Boot.__init__)
    params = list(sig.parameters.keys())



def test_file_is_not_abstract():
    assert not inspect.isabstract(File)


def test_file_constructor_exists():
    assert callable(File.__init__)


def test_file_constructor_args():
    sig = inspect.signature(File.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::informationfile_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::InformationFile)


def test_mancoosimm::informationfile_constructor_exists():
    assert callable(mancoosimm::InformationFile.__init__)


def test_mancoosimm::informationfile_constructor_args():
    sig = inspect.signature(mancoosimm::InformationFile.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::librarycache_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::LibraryCache)


def test_mancoosimm::librarycache_constructor_exists():
    assert callable(mancoosimm::LibraryCache.__init__)


def test_mancoosimm::librarycache_constructor_args():
    sig = inspect.signature(mancoosimm::LibraryCache.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::mimetypehandlercache_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::MimeTypeHandlerCache)


def test_mancoosimm::mimetypehandlercache_constructor_exists():
    assert callable(mancoosimm::MimeTypeHandlerCache.__init__)


def test_mancoosimm::mimetypehandlercache_constructor_args():
    sig = inspect.signature(mancoosimm::MimeTypeHandlerCache.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::desktopdb_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::DesktopDB)


def test_mancoosimm::desktopdb_constructor_exists():
    assert callable(mancoosimm::DesktopDB.__init__)


def test_mancoosimm::desktopdb_constructor_args():
    sig = inspect.signature(mancoosimm::DesktopDB.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::iconcache_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::IconCache)


def test_mancoosimm::iconcache_constructor_exists():
    assert callable(mancoosimm::IconCache.__init__)


def test_mancoosimm::iconcache_constructor_args():
    sig = inspect.signature(mancoosimm::IconCache.__init__)
    params = list(sig.parameters.keys())
    assert "mtime" in params, "Missing parameter 'mtime'"

def test_mancoosimm::iconcache_has_mtime():
    assert hasattr(mancoosimm::IconCache, "mtime")
    descriptor = None
    for klass in mancoosimm::IconCache.__mro__:
        if "mtime" in klass.__dict__:
            descriptor = klass.__dict__["mtime"]
            break
    assert isinstance(descriptor, property)



def test_mancoosimm::menu_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::Menu)


def test_mancoosimm::menu_constructor_exists():
    assert callable(mancoosimm::Menu.__init__)


def test_mancoosimm::menu_constructor_args():
    sig = inspect.signature(mancoosimm::Menu.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::gconf_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::GConf)


def test_mancoosimm::gconf_constructor_exists():
    assert callable(mancoosimm::GConf.__init__)


def test_mancoosimm::gconf_constructor_args():
    sig = inspect.signature(mancoosimm::GConf.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::xfontcache_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::XFontCache)


def test_mancoosimm::xfontcache_constructor_exists():
    assert callable(mancoosimm::XFontCache.__init__)


def test_mancoosimm::xfontcache_constructor_args():
    sig = inspect.signature(mancoosimm::XFontCache.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_mancoosimm::xfontcache_has_location():
    assert hasattr(mancoosimm::XFontCache, "location")
    descriptor = None
    for klass in mancoosimm::XFontCache.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_mancoosimm::modulecache_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::ModuleCache)


def test_mancoosimm::modulecache_constructor_exists():
    assert callable(mancoosimm::ModuleCache.__init__)


def test_mancoosimm::modulecache_constructor_args():
    sig = inspect.signature(mancoosimm::ModuleCache.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"

def test_mancoosimm::modulecache_has_version():
    assert hasattr(mancoosimm::ModuleCache, "version")
    descriptor = None
    for klass in mancoosimm::ModuleCache.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_mancoosimm::notinv_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::NotInv)


def test_mancoosimm::notinv_constructor_exists():
    assert callable(mancoosimm::NotInv.__init__)


def test_mancoosimm::notinv_constructor_args():
    sig = inspect.signature(mancoosimm::NotInv.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::orinv_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::OrInv)


def test_mancoosimm::orinv_constructor_exists():
    assert callable(mancoosimm::OrInv.__init__)


def test_mancoosimm::orinv_constructor_args():
    sig = inspect.signature(mancoosimm::OrInv.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::andinv_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::AndInv)


def test_mancoosimm::andinv_constructor_exists():
    assert callable(mancoosimm::AndInv.__init__)


def test_mancoosimm::andinv_constructor_args():
    sig = inspect.signature(mancoosimm::AndInv.__init__)
    params = list(sig.parameters.keys())



def test_installedpackage_is_not_abstract():
    assert not inspect.isabstract(InstalledPackage)


def test_installedpackage_constructor_exists():
    assert callable(InstalledPackage.__init__)


def test_installedpackage_constructor_args():
    sig = inspect.signature(InstalledPackage.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::binpackage_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::BinPackage)


def test_mancoosimm::binpackage_constructor_exists():
    assert callable(mancoosimm::BinPackage.__init__)


def test_mancoosimm::binpackage_constructor_args():
    sig = inspect.signature(mancoosimm::BinPackage.__init__)
    params = list(sig.parameters.keys())



def test_dependence_is_not_abstract():
    assert not inspect.isabstract(Dependence)


def test_dependence_constructor_exists():
    assert callable(Dependence.__init__)


def test_dependence_constructor_args():
    sig = inspect.signature(Dependence.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::singledep_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::SingleDep)


def test_mancoosimm::singledep_constructor_exists():
    assert callable(mancoosimm::SingleDep.__init__)


def test_mancoosimm::singledep_constructor_args():
    sig = inspect.signature(mancoosimm::SingleDep.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "version" in params, "Missing parameter 'version'"

def test_mancoosimm::singledep_has_value():
    assert hasattr(mancoosimm::SingleDep, "value")
    descriptor = None
    for klass in mancoosimm::SingleDep.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::singledep_has_version():
    assert hasattr(mancoosimm::SingleDep, "version")
    descriptor = None
    for klass in mancoosimm::SingleDep.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_mancoosimm::ordep_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::OrDep)


def test_mancoosimm::ordep_constructor_exists():
    assert callable(mancoosimm::OrDep.__init__)


def test_mancoosimm::ordep_constructor_args():
    sig = inspect.signature(mancoosimm::OrDep.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::anddep_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::AndDep)


def test_mancoosimm::anddep_constructor_exists():
    assert callable(mancoosimm::AndDep.__init__)


def test_mancoosimm::anddep_constructor_args():
    sig = inspect.signature(mancoosimm::AndDep.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::conflict_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::Conflict)


def test_mancoosimm::conflict_constructor_exists():
    assert callable(mancoosimm::Conflict.__init__)


def test_mancoosimm::conflict_constructor_args():
    sig = inspect.signature(mancoosimm::Conflict.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::documentationfile_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::DocumentationFile)


def test_mancoosimm::documentationfile_constructor_exists():
    assert callable(mancoosimm::DocumentationFile.__init__)


def test_mancoosimm::documentationfile_constructor_args():
    sig = inspect.signature(mancoosimm::DocumentationFile.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::virtualpackage_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::VirtualPackage)


def test_mancoosimm::virtualpackage_constructor_exists():
    assert callable(mancoosimm::VirtualPackage.__init__)


def test_mancoosimm::virtualpackage_constructor_args():
    sig = inspect.signature(mancoosimm::VirtualPackage.__init__)
    params = list(sig.parameters.keys())



def test_unpackedpackage_is_not_abstract():
    assert not inspect.isabstract(UnpackedPackage)


def test_unpackedpackage_constructor_exists():
    assert callable(UnpackedPackage.__init__)


def test_unpackedpackage_constructor_args():
    sig = inspect.signature(UnpackedPackage.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::halfconfiguredreinstrequiredpackage_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::HalfConfiguredReinstRequiredPackage)


def test_mancoosimm::halfconfiguredreinstrequiredpackage_constructor_exists():
    assert callable(mancoosimm::HalfConfiguredReinstRequiredPackage.__init__)


def test_mancoosimm::halfconfiguredreinstrequiredpackage_constructor_args():
    sig = inspect.signature(mancoosimm::HalfConfiguredReinstRequiredPackage.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::halfconfiguredpackage_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::HalfConfiguredPackage)


def test_mancoosimm::halfconfiguredpackage_constructor_exists():
    assert callable(mancoosimm::HalfConfiguredPackage.__init__)


def test_mancoosimm::halfconfiguredpackage_constructor_args():
    sig = inspect.signature(mancoosimm::HalfConfiguredPackage.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::dependence_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::Dependence)


def test_mancoosimm::dependence_constructor_exists():
    assert callable(mancoosimm::Dependence.__init__)


def test_mancoosimm::dependence_constructor_args():
    sig = inspect.signature(mancoosimm::Dependence.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::srcpackage_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::SrcPackage)


def test_mancoosimm::srcpackage_constructor_exists():
    assert callable(mancoosimm::SrcPackage.__init__)


def test_mancoosimm::srcpackage_constructor_args():
    sig = inspect.signature(mancoosimm::SrcPackage.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::filesystem_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::FileSystem)


def test_mancoosimm::filesystem_constructor_exists():
    assert callable(mancoosimm::FileSystem.__init__)


def test_mancoosimm::filesystem_constructor_args():
    sig = inspect.signature(mancoosimm::FileSystem.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::group_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::Group)


def test_mancoosimm::group_constructor_exists():
    assert callable(mancoosimm::Group.__init__)


def test_mancoosimm::group_constructor_args():
    sig = inspect.signature(mancoosimm::Group.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::skeeperdocument_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::SkeeperDocument)


def test_mancoosimm::skeeperdocument_constructor_exists():
    assert callable(mancoosimm::SkeeperDocument.__init__)


def test_mancoosimm::skeeperdocument_constructor_args():
    sig = inspect.signature(mancoosimm::SkeeperDocument.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::sgmldocument_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::SGMLDocument)


def test_mancoosimm::sgmldocument_constructor_exists():
    assert callable(mancoosimm::SGMLDocument.__init__)


def test_mancoosimm::sgmldocument_constructor_args():
    sig = inspect.signature(mancoosimm::SGMLDocument.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::alternative_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::Alternative)


def test_mancoosimm::alternative_constructor_exists():
    assert callable(mancoosimm::Alternative.__init__)


def test_mancoosimm::alternative_constructor_args():
    sig = inspect.signature(mancoosimm::Alternative.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::sgmlcatalog_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::SGMLCatalog)


def test_mancoosimm::sgmlcatalog_constructor_exists():
    assert callable(mancoosimm::SGMLCatalog.__init__)


def test_mancoosimm::sgmlcatalog_constructor_args():
    sig = inspect.signature(mancoosimm::SGMLCatalog.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::file_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::File)


def test_mancoosimm::file_constructor_exists():
    assert callable(mancoosimm::File.__init__)


def test_mancoosimm::file_constructor_args():
    sig = inspect.signature(mancoosimm::File.__init__)
    params = list(sig.parameters.keys())
    assert "checkSum" in params, "Missing parameter 'checkSum'"
    assert "location" in params, "Missing parameter 'location'"
    assert "permission" in params, "Missing parameter 'permission'"
    assert "size" in params, "Missing parameter 'size'"
    assert "guid" in params, "Missing parameter 'guid'"
    assert "suid" in params, "Missing parameter 'suid'"
    assert "isMissing" in params, "Missing parameter 'isMissing'"
    assert "description" in params, "Missing parameter 'description'"
    assert "extension" in params, "Missing parameter 'extension'"
    assert "isDirectory" in params, "Missing parameter 'isDirectory'"

def test_mancoosimm::file_has_checkSum():
    assert hasattr(mancoosimm::File, "checkSum")
    descriptor = None
    for klass in mancoosimm::File.__mro__:
        if "checkSum" in klass.__dict__:
            descriptor = klass.__dict__["checkSum"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::file_has_location():
    assert hasattr(mancoosimm::File, "location")
    descriptor = None
    for klass in mancoosimm::File.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::file_has_permission():
    assert hasattr(mancoosimm::File, "permission")
    descriptor = None
    for klass in mancoosimm::File.__mro__:
        if "permission" in klass.__dict__:
            descriptor = klass.__dict__["permission"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::file_has_size():
    assert hasattr(mancoosimm::File, "size")
    descriptor = None
    for klass in mancoosimm::File.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::file_has_guid():
    assert hasattr(mancoosimm::File, "guid")
    descriptor = None
    for klass in mancoosimm::File.__mro__:
        if "guid" in klass.__dict__:
            descriptor = klass.__dict__["guid"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::file_has_suid():
    assert hasattr(mancoosimm::File, "suid")
    descriptor = None
    for klass in mancoosimm::File.__mro__:
        if "suid" in klass.__dict__:
            descriptor = klass.__dict__["suid"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::file_has_isMissing():
    assert hasattr(mancoosimm::File, "isMissing")
    descriptor = None
    for klass in mancoosimm::File.__mro__:
        if "isMissing" in klass.__dict__:
            descriptor = klass.__dict__["isMissing"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::file_has_description():
    assert hasattr(mancoosimm::File, "description")
    descriptor = None
    for klass in mancoosimm::File.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::file_has_extension():
    assert hasattr(mancoosimm::File, "extension")
    descriptor = None
    for klass in mancoosimm::File.__mro__:
        if "extension" in klass.__dict__:
            descriptor = klass.__dict__["extension"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::file_has_isDirectory():
    assert hasattr(mancoosimm::File, "isDirectory")
    descriptor = None
    for klass in mancoosimm::File.__mro__:
        if "isDirectory" in klass.__dict__:
            descriptor = klass.__dict__["isDirectory"]
            break
    assert isinstance(descriptor, property)



def test_mancoosimm::applicationmenucatalog_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::ApplicationMenuCatalog)


def test_mancoosimm::applicationmenucatalog_constructor_exists():
    assert callable(mancoosimm::ApplicationMenuCatalog.__init__)


def test_mancoosimm::applicationmenucatalog_constructor_args():
    sig = inspect.signature(mancoosimm::ApplicationMenuCatalog.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::skeepercatalog_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::SkeeperCatalog)


def test_mancoosimm::skeepercatalog_constructor_exists():
    assert callable(mancoosimm::SkeeperCatalog.__init__)


def test_mancoosimm::skeepercatalog_constructor_args():
    sig = inspect.signature(mancoosimm::SkeeperCatalog.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::environment_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::Environment)


def test_mancoosimm::environment_constructor_exists():
    assert callable(mancoosimm::Environment.__init__)


def test_mancoosimm::environment_constructor_args():
    sig = inspect.signature(mancoosimm::Environment.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::atom_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::Atom)


def test_mancoosimm::atom_constructor_exists():
    assert callable(mancoosimm::Atom.__init__)


def test_mancoosimm::atom_constructor_args():
    sig = inspect.signature(mancoosimm::Atom.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::xfont_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::XFont)


def test_mancoosimm::xfont_constructor_exists():
    assert callable(mancoosimm::XFont.__init__)


def test_mancoosimm::xfont_constructor_args():
    sig = inspect.signature(mancoosimm::XFont.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::emacspackage_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::EmacsPackage)


def test_mancoosimm::emacspackage_constructor_exists():
    assert callable(mancoosimm::EmacsPackage.__init__)


def test_mancoosimm::emacspackage_constructor_args():
    sig = inspect.signature(mancoosimm::EmacsPackage.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::package_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::Package)


def test_mancoosimm::package_constructor_exists():
    assert callable(mancoosimm::Package.__init__)


def test_mancoosimm::package_constructor_args():
    sig = inspect.signature(mancoosimm::Package.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "architecture" in params, "Missing parameter 'architecture'"

def test_mancoosimm::package_has_version():
    assert hasattr(mancoosimm::Package, "version")
    descriptor = None
    for klass in mancoosimm::Package.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::package_has_architecture():
    assert hasattr(mancoosimm::Package, "architecture")
    descriptor = None
    for klass in mancoosimm::Package.__mro__:
        if "architecture" in klass.__dict__:
            descriptor = klass.__dict__["architecture"]
            break
    assert isinstance(descriptor, property)



def test_mancoosimm::user_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::User)


def test_mancoosimm::user_constructor_exists():
    assert callable(mancoosimm::User.__init__)


def test_mancoosimm::user_constructor_args():
    sig = inspect.signature(mancoosimm::User.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::service_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::Service)


def test_mancoosimm::service_constructor_exists():
    assert callable(mancoosimm::Service.__init__)


def test_mancoosimm::service_constructor_args():
    sig = inspect.signature(mancoosimm::Service.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::module_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::Module)


def test_mancoosimm::module_constructor_exists():
    assert callable(mancoosimm::Module.__init__)


def test_mancoosimm::module_constructor_args():
    sig = inspect.signature(mancoosimm::Module.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::menuentry_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::MenuEntry)


def test_mancoosimm::menuentry_constructor_exists():
    assert callable(mancoosimm::MenuEntry.__init__)


def test_mancoosimm::menuentry_constructor_args():
    sig = inspect.signature(mancoosimm::MenuEntry.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::invariant_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::Invariant)


def test_mancoosimm::invariant_constructor_exists():
    assert callable(mancoosimm::Invariant.__init__)


def test_mancoosimm::invariant_constructor_args():
    sig = inspect.signature(mancoosimm::Invariant.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::installedpackage_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::InstalledPackage)


def test_mancoosimm::installedpackage_constructor_exists():
    assert callable(mancoosimm::InstalledPackage.__init__)


def test_mancoosimm::installedpackage_constructor_args():
    sig = inspect.signature(mancoosimm::InstalledPackage.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "maintainer" in params, "Missing parameter 'maintainer'"
    assert "checkSum" in params, "Missing parameter 'checkSum'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "tag" in params, "Missing parameter 'tag'"
    assert "installedSize" in params, "Missing parameter 'installedSize'"
    assert "uploaders" in params, "Missing parameter 'uploaders'"
    assert "fileSize" in params, "Missing parameter 'fileSize'"
    assert "section" in params, "Missing parameter 'section'"

def test_mancoosimm::installedpackage_has_description():
    assert hasattr(mancoosimm::InstalledPackage, "description")
    descriptor = None
    for klass in mancoosimm::InstalledPackage.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::installedpackage_has_maintainer():
    assert hasattr(mancoosimm::InstalledPackage, "maintainer")
    descriptor = None
    for klass in mancoosimm::InstalledPackage.__mro__:
        if "maintainer" in klass.__dict__:
            descriptor = klass.__dict__["maintainer"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::installedpackage_has_checkSum():
    assert hasattr(mancoosimm::InstalledPackage, "checkSum")
    descriptor = None
    for klass in mancoosimm::InstalledPackage.__mro__:
        if "checkSum" in klass.__dict__:
            descriptor = klass.__dict__["checkSum"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::installedpackage_has_priority():
    assert hasattr(mancoosimm::InstalledPackage, "priority")
    descriptor = None
    for klass in mancoosimm::InstalledPackage.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::installedpackage_has_tag():
    assert hasattr(mancoosimm::InstalledPackage, "tag")
    descriptor = None
    for klass in mancoosimm::InstalledPackage.__mro__:
        if "tag" in klass.__dict__:
            descriptor = klass.__dict__["tag"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::installedpackage_has_installedSize():
    assert hasattr(mancoosimm::InstalledPackage, "installedSize")
    descriptor = None
    for klass in mancoosimm::InstalledPackage.__mro__:
        if "installedSize" in klass.__dict__:
            descriptor = klass.__dict__["installedSize"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::installedpackage_has_uploaders():
    assert hasattr(mancoosimm::InstalledPackage, "uploaders")
    descriptor = None
    for klass in mancoosimm::InstalledPackage.__mro__:
        if "uploaders" in klass.__dict__:
            descriptor = klass.__dict__["uploaders"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::installedpackage_has_fileSize():
    assert hasattr(mancoosimm::InstalledPackage, "fileSize")
    descriptor = None
    for klass in mancoosimm::InstalledPackage.__mro__:
        if "fileSize" in klass.__dict__:
            descriptor = klass.__dict__["fileSize"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::installedpackage_has_section():
    assert hasattr(mancoosimm::InstalledPackage, "section")
    descriptor = None
    for klass in mancoosimm::InstalledPackage.__mro__:
        if "section" in klass.__dict__:
            descriptor = klass.__dict__["section"]
            break
    assert isinstance(descriptor, property)



def test_mancoosimm::notinstalledpackage_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::NotInstalledPackage)


def test_mancoosimm::notinstalledpackage_constructor_exists():
    assert callable(mancoosimm::NotInstalledPackage.__init__)


def test_mancoosimm::notinstalledpackage_constructor_args():
    sig = inspect.signature(mancoosimm::NotInstalledPackage.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::halfinstalledreinstrequiredpackage_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::HalfInstalledReinstRequiredPackage)


def test_mancoosimm::halfinstalledreinstrequiredpackage_constructor_exists():
    assert callable(mancoosimm::HalfInstalledReinstRequiredPackage.__init__)


def test_mancoosimm::halfinstalledreinstrequiredpackage_constructor_args():
    sig = inspect.signature(mancoosimm::HalfInstalledReinstRequiredPackage.__init__)
    params = list(sig.parameters.keys())
    assert "uploaders" in params, "Missing parameter 'uploaders'"
    assert "description" in params, "Missing parameter 'description'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "checkSum" in params, "Missing parameter 'checkSum'"
    assert "section" in params, "Missing parameter 'section'"
    assert "maintainer" in params, "Missing parameter 'maintainer'"
    assert "tag" in params, "Missing parameter 'tag'"

def test_mancoosimm::halfinstalledreinstrequiredpackage_has_uploaders():
    assert hasattr(mancoosimm::HalfInstalledReinstRequiredPackage, "uploaders")
    descriptor = None
    for klass in mancoosimm::HalfInstalledReinstRequiredPackage.__mro__:
        if "uploaders" in klass.__dict__:
            descriptor = klass.__dict__["uploaders"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::halfinstalledreinstrequiredpackage_has_description():
    assert hasattr(mancoosimm::HalfInstalledReinstRequiredPackage, "description")
    descriptor = None
    for klass in mancoosimm::HalfInstalledReinstRequiredPackage.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::halfinstalledreinstrequiredpackage_has_priority():
    assert hasattr(mancoosimm::HalfInstalledReinstRequiredPackage, "priority")
    descriptor = None
    for klass in mancoosimm::HalfInstalledReinstRequiredPackage.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::halfinstalledreinstrequiredpackage_has_checkSum():
    assert hasattr(mancoosimm::HalfInstalledReinstRequiredPackage, "checkSum")
    descriptor = None
    for klass in mancoosimm::HalfInstalledReinstRequiredPackage.__mro__:
        if "checkSum" in klass.__dict__:
            descriptor = klass.__dict__["checkSum"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::halfinstalledreinstrequiredpackage_has_section():
    assert hasattr(mancoosimm::HalfInstalledReinstRequiredPackage, "section")
    descriptor = None
    for klass in mancoosimm::HalfInstalledReinstRequiredPackage.__mro__:
        if "section" in klass.__dict__:
            descriptor = klass.__dict__["section"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::halfinstalledreinstrequiredpackage_has_maintainer():
    assert hasattr(mancoosimm::HalfInstalledReinstRequiredPackage, "maintainer")
    descriptor = None
    for klass in mancoosimm::HalfInstalledReinstRequiredPackage.__mro__:
        if "maintainer" in klass.__dict__:
            descriptor = klass.__dict__["maintainer"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::halfinstalledreinstrequiredpackage_has_tag():
    assert hasattr(mancoosimm::HalfInstalledReinstRequiredPackage, "tag")
    descriptor = None
    for klass in mancoosimm::HalfInstalledReinstRequiredPackage.__mro__:
        if "tag" in klass.__dict__:
            descriptor = klass.__dict__["tag"]
            break
    assert isinstance(descriptor, property)



def test_mancoosimm::halfinstalledpackage_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::HalfInstalledPackage)


def test_mancoosimm::halfinstalledpackage_constructor_exists():
    assert callable(mancoosimm::HalfInstalledPackage.__init__)


def test_mancoosimm::halfinstalledpackage_constructor_args():
    sig = inspect.signature(mancoosimm::HalfInstalledPackage.__init__)
    params = list(sig.parameters.keys())
    assert "uploaders" in params, "Missing parameter 'uploaders'"
    assert "checkSum" in params, "Missing parameter 'checkSum'"
    assert "maintainer" in params, "Missing parameter 'maintainer'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "description" in params, "Missing parameter 'description'"
    assert "section" in params, "Missing parameter 'section'"
    assert "tag" in params, "Missing parameter 'tag'"

def test_mancoosimm::halfinstalledpackage_has_uploaders():
    assert hasattr(mancoosimm::HalfInstalledPackage, "uploaders")
    descriptor = None
    for klass in mancoosimm::HalfInstalledPackage.__mro__:
        if "uploaders" in klass.__dict__:
            descriptor = klass.__dict__["uploaders"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::halfinstalledpackage_has_checkSum():
    assert hasattr(mancoosimm::HalfInstalledPackage, "checkSum")
    descriptor = None
    for klass in mancoosimm::HalfInstalledPackage.__mro__:
        if "checkSum" in klass.__dict__:
            descriptor = klass.__dict__["checkSum"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::halfinstalledpackage_has_maintainer():
    assert hasattr(mancoosimm::HalfInstalledPackage, "maintainer")
    descriptor = None
    for klass in mancoosimm::HalfInstalledPackage.__mro__:
        if "maintainer" in klass.__dict__:
            descriptor = klass.__dict__["maintainer"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::halfinstalledpackage_has_priority():
    assert hasattr(mancoosimm::HalfInstalledPackage, "priority")
    descriptor = None
    for klass in mancoosimm::HalfInstalledPackage.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::halfinstalledpackage_has_description():
    assert hasattr(mancoosimm::HalfInstalledPackage, "description")
    descriptor = None
    for klass in mancoosimm::HalfInstalledPackage.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::halfinstalledpackage_has_section():
    assert hasattr(mancoosimm::HalfInstalledPackage, "section")
    descriptor = None
    for klass in mancoosimm::HalfInstalledPackage.__mro__:
        if "section" in klass.__dict__:
            descriptor = klass.__dict__["section"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::halfinstalledpackage_has_tag():
    assert hasattr(mancoosimm::HalfInstalledPackage, "tag")
    descriptor = None
    for klass in mancoosimm::HalfInstalledPackage.__mro__:
        if "tag" in klass.__dict__:
            descriptor = klass.__dict__["tag"]
            break
    assert isinstance(descriptor, property)



def test_mancoosimm::unpackedpackage_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::UnpackedPackage)


def test_mancoosimm::unpackedpackage_constructor_exists():
    assert callable(mancoosimm::UnpackedPackage.__init__)


def test_mancoosimm::unpackedpackage_constructor_args():
    sig = inspect.signature(mancoosimm::UnpackedPackage.__init__)
    params = list(sig.parameters.keys())
    assert "checkSum" in params, "Missing parameter 'checkSum'"
    assert "tag" in params, "Missing parameter 'tag'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "maintainer" in params, "Missing parameter 'maintainer'"
    assert "uploaders" in params, "Missing parameter 'uploaders'"
    assert "section" in params, "Missing parameter 'section'"
    assert "description" in params, "Missing parameter 'description'"

def test_mancoosimm::unpackedpackage_has_checkSum():
    assert hasattr(mancoosimm::UnpackedPackage, "checkSum")
    descriptor = None
    for klass in mancoosimm::UnpackedPackage.__mro__:
        if "checkSum" in klass.__dict__:
            descriptor = klass.__dict__["checkSum"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::unpackedpackage_has_tag():
    assert hasattr(mancoosimm::UnpackedPackage, "tag")
    descriptor = None
    for klass in mancoosimm::UnpackedPackage.__mro__:
        if "tag" in klass.__dict__:
            descriptor = klass.__dict__["tag"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::unpackedpackage_has_priority():
    assert hasattr(mancoosimm::UnpackedPackage, "priority")
    descriptor = None
    for klass in mancoosimm::UnpackedPackage.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::unpackedpackage_has_maintainer():
    assert hasattr(mancoosimm::UnpackedPackage, "maintainer")
    descriptor = None
    for klass in mancoosimm::UnpackedPackage.__mro__:
        if "maintainer" in klass.__dict__:
            descriptor = klass.__dict__["maintainer"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::unpackedpackage_has_uploaders():
    assert hasattr(mancoosimm::UnpackedPackage, "uploaders")
    descriptor = None
    for klass in mancoosimm::UnpackedPackage.__mro__:
        if "uploaders" in klass.__dict__:
            descriptor = klass.__dict__["uploaders"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::unpackedpackage_has_section():
    assert hasattr(mancoosimm::UnpackedPackage, "section")
    descriptor = None
    for klass in mancoosimm::UnpackedPackage.__mro__:
        if "section" in klass.__dict__:
            descriptor = klass.__dict__["section"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::unpackedpackage_has_description():
    assert hasattr(mancoosimm::UnpackedPackage, "description")
    descriptor = None
    for klass in mancoosimm::UnpackedPackage.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_mancoosimm::configfilespackage_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::ConfigFilesPackage)


def test_mancoosimm::configfilespackage_constructor_exists():
    assert callable(mancoosimm::ConfigFilesPackage.__init__)


def test_mancoosimm::configfilespackage_constructor_args():
    sig = inspect.signature(mancoosimm::ConfigFilesPackage.__init__)
    params = list(sig.parameters.keys())
    assert "priority" in params, "Missing parameter 'priority'"
    assert "maintainer" in params, "Missing parameter 'maintainer'"
    assert "section" in params, "Missing parameter 'section'"
    assert "tag" in params, "Missing parameter 'tag'"
    assert "uploaders" in params, "Missing parameter 'uploaders'"
    assert "description" in params, "Missing parameter 'description'"
    assert "checkSum" in params, "Missing parameter 'checkSum'"

def test_mancoosimm::configfilespackage_has_priority():
    assert hasattr(mancoosimm::ConfigFilesPackage, "priority")
    descriptor = None
    for klass in mancoosimm::ConfigFilesPackage.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::configfilespackage_has_maintainer():
    assert hasattr(mancoosimm::ConfigFilesPackage, "maintainer")
    descriptor = None
    for klass in mancoosimm::ConfigFilesPackage.__mro__:
        if "maintainer" in klass.__dict__:
            descriptor = klass.__dict__["maintainer"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::configfilespackage_has_section():
    assert hasattr(mancoosimm::ConfigFilesPackage, "section")
    descriptor = None
    for klass in mancoosimm::ConfigFilesPackage.__mro__:
        if "section" in klass.__dict__:
            descriptor = klass.__dict__["section"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::configfilespackage_has_tag():
    assert hasattr(mancoosimm::ConfigFilesPackage, "tag")
    descriptor = None
    for klass in mancoosimm::ConfigFilesPackage.__mro__:
        if "tag" in klass.__dict__:
            descriptor = klass.__dict__["tag"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::configfilespackage_has_uploaders():
    assert hasattr(mancoosimm::ConfigFilesPackage, "uploaders")
    descriptor = None
    for klass in mancoosimm::ConfigFilesPackage.__mro__:
        if "uploaders" in klass.__dict__:
            descriptor = klass.__dict__["uploaders"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::configfilespackage_has_description():
    assert hasattr(mancoosimm::ConfigFilesPackage, "description")
    descriptor = None
    for klass in mancoosimm::ConfigFilesPackage.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::configfilespackage_has_checkSum():
    assert hasattr(mancoosimm::ConfigFilesPackage, "checkSum")
    descriptor = None
    for klass in mancoosimm::ConfigFilesPackage.__mro__:
        if "checkSum" in klass.__dict__:
            descriptor = klass.__dict__["checkSum"]
            break
    assert isinstance(descriptor, property)



def test_mancoosimm::packagesetting_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::PackageSetting)


def test_mancoosimm::packagesetting_constructor_exists():
    assert callable(mancoosimm::PackageSetting.__init__)


def test_mancoosimm::packagesetting_constructor_args():
    sig = inspect.signature(mancoosimm::PackageSetting.__init__)
    params = list(sig.parameters.keys())



def test_mancoosimm::configuration_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::Configuration)


def test_mancoosimm::configuration_constructor_exists():
    assert callable(mancoosimm::Configuration.__init__)


def test_mancoosimm::configuration_constructor_args():
    sig = inspect.signature(mancoosimm::Configuration.__init__)
    params = list(sig.parameters.keys())
    assert "creationTime" in params, "Missing parameter 'creationTime'"
    assert "systemType" in params, "Missing parameter 'systemType'"

def test_mancoosimm::configuration_has_creationTime():
    assert hasattr(mancoosimm::Configuration, "creationTime")
    descriptor = None
    for klass in mancoosimm::Configuration.__mro__:
        if "creationTime" in klass.__dict__:
            descriptor = klass.__dict__["creationTime"]
            break
    assert isinstance(descriptor, property)

def test_mancoosimm::configuration_has_systemType():
    assert hasattr(mancoosimm::Configuration, "systemType")
    descriptor = None
    for klass in mancoosimm::Configuration.__mro__:
        if "systemType" in klass.__dict__:
            descriptor = klass.__dict__["systemType"]
            break
    assert isinstance(descriptor, property)



def test_mancoosimm::namedelement_is_not_abstract():
    assert not inspect.isabstract(mancoosimm::NamedElement)


def test_mancoosimm::namedelement_constructor_exists():
    assert callable(mancoosimm::NamedElement.__init__)


def test_mancoosimm::namedelement_constructor_args():
    sig = inspect.signature(mancoosimm::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mancoosimm::namedelement_has_name():
    assert hasattr(mancoosimm::NamedElement, "name")
    descriptor = None
    for klass in mancoosimm::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_statustype_exists():
    # Check that the Enumeration exists
    assert StatusType is not None

def test_statustype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StatusType]
    expected_literals = [
        "half_installed",
        "not_installed",
        "installed",
        "config_files",
        "half_configured",
        "unpacked",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StatusType"

def test_versiontype_exists():
    # Check that the Enumeration exists
    assert VersionType is not None

def test_versiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VersionType]
    expected_literals = [
        "ggt",
        "ge",
        "llt",
        "le",
        "eq",
        "gt",
        "lt",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VersionType"

def test_prioritytype_exists():
    # Check that the Enumeration exists
    assert PriorityType is not None

def test_prioritytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PriorityType]
    expected_literals = [
        "optional",
        "standard",
        "required",
        "important",
        "extra",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PriorityType"


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
Conflict_strategy = st.builds(
    Conflict,
)
mancoosimm::OrConflict_strategy = st.builds(
    mancoosimm::OrConflict,
)
mancoosimm::AndConflict_strategy = st.builds(
    mancoosimm::AndConflict,
)
mancoosimm::SingleConflict_strategy = st.builds(
    mancoosimm::SingleConflict,
    value=
        safe_text,
    version=
        safe_text
)
mancoosimm::SharedLibrary_strategy = st.builds(
    mancoosimm::SharedLibrary,
    name=
        safe_text,
    version=
        safe_text
)
mancoosimm::MimeType_strategy = st.builds(
    mancoosimm::MimeType,
    name=
        safe_text,
    extension=
        safe_text
)
mancoosimm::MimeTypeHandler_strategy = st.builds(
    mancoosimm::MimeTypeHandler,
)
mancoosimm::Boot_strategy = st.builds(
    mancoosimm::Boot,
)
File_strategy = st.builds(
    File,
)
mancoosimm::InformationFile_strategy = st.builds(
    mancoosimm::InformationFile,
)
mancoosimm::LibraryCache_strategy = st.builds(
    mancoosimm::LibraryCache,
)
mancoosimm::MimeTypeHandlerCache_strategy = st.builds(
    mancoosimm::MimeTypeHandlerCache,
)
mancoosimm::DesktopDB_strategy = st.builds(
    mancoosimm::DesktopDB,
)
mancoosimm::IconCache_strategy = st.builds(
    mancoosimm::IconCache,
    mtime=
        safe_text
)
mancoosimm::Menu_strategy = st.builds(
    mancoosimm::Menu,
)
mancoosimm::GConf_strategy = st.builds(
    mancoosimm::GConf,
)
mancoosimm::XFontCache_strategy = st.builds(
    mancoosimm::XFontCache,
    location=
        safe_text
)
mancoosimm::ModuleCache_strategy = st.builds(
    mancoosimm::ModuleCache,
    version=
        safe_text
)
mancoosimm::NotInv_strategy = st.builds(
    mancoosimm::NotInv,
)
mancoosimm::OrInv_strategy = st.builds(
    mancoosimm::OrInv,
)
mancoosimm::AndInv_strategy = st.builds(
    mancoosimm::AndInv,
)
InstalledPackage_strategy = st.builds(
    InstalledPackage,
)
mancoosimm::BinPackage_strategy = st.builds(
    mancoosimm::BinPackage,
)
Dependence_strategy = st.builds(
    Dependence,
)
mancoosimm::SingleDep_strategy = st.builds(
    mancoosimm::SingleDep,
    value=
        safe_text,
    version=
        safe_text
)
mancoosimm::OrDep_strategy = st.builds(
    mancoosimm::OrDep,
)
mancoosimm::AndDep_strategy = st.builds(
    mancoosimm::AndDep,
)
mancoosimm::Conflict_strategy = st.builds(
    mancoosimm::Conflict,
)
mancoosimm::DocumentationFile_strategy = st.builds(
    mancoosimm::DocumentationFile,
)
mancoosimm::VirtualPackage_strategy = st.builds(
    mancoosimm::VirtualPackage,
)
UnpackedPackage_strategy = st.builds(
    UnpackedPackage,
)
mancoosimm::HalfConfiguredReinstRequiredPackage_strategy = st.builds(
    mancoosimm::HalfConfiguredReinstRequiredPackage,
)
mancoosimm::HalfConfiguredPackage_strategy = st.builds(
    mancoosimm::HalfConfiguredPackage,
)
mancoosimm::Dependence_strategy = st.builds(
    mancoosimm::Dependence,
)
mancoosimm::SrcPackage_strategy = st.builds(
    mancoosimm::SrcPackage,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
mancoosimm::FileSystem_strategy = st.builds(
    mancoosimm::FileSystem,
)
mancoosimm::Group_strategy = st.builds(
    mancoosimm::Group,
)
mancoosimm::SkeeperDocument_strategy = st.builds(
    mancoosimm::SkeeperDocument,
)
mancoosimm::SGMLDocument_strategy = st.builds(
    mancoosimm::SGMLDocument,
)
mancoosimm::Alternative_strategy = st.builds(
    mancoosimm::Alternative,
)
mancoosimm::SGMLCatalog_strategy = st.builds(
    mancoosimm::SGMLCatalog,
)
mancoosimm::File_strategy = st.builds(
    mancoosimm::File,
    checkSum=
        safe_text,
    location=
        safe_text,
    permission=
        safe_text,
    size=
        st.integers(),
    guid=
        st.booleans(),
    suid=
        st.booleans(),
    isMissing=
        st.booleans(),
    description=
        safe_text,
    extension=
        safe_text,
    isDirectory=
        st.booleans()
)
mancoosimm::ApplicationMenuCatalog_strategy = st.builds(
    mancoosimm::ApplicationMenuCatalog,
)
mancoosimm::SkeeperCatalog_strategy = st.builds(
    mancoosimm::SkeeperCatalog,
)
mancoosimm::Environment_strategy = st.builds(
    mancoosimm::Environment,
)
mancoosimm::Atom_strategy = st.builds(
    mancoosimm::Atom,
)
mancoosimm::XFont_strategy = st.builds(
    mancoosimm::XFont,
)
mancoosimm::EmacsPackage_strategy = st.builds(
    mancoosimm::EmacsPackage,
)
mancoosimm::Package_strategy = st.builds(
    mancoosimm::Package,
    version=
        safe_text,
    architecture=
        safe_text
)
mancoosimm::User_strategy = st.builds(
    mancoosimm::User,
)
mancoosimm::Service_strategy = st.builds(
    mancoosimm::Service,
)
mancoosimm::Module_strategy = st.builds(
    mancoosimm::Module,
)
mancoosimm::MenuEntry_strategy = st.builds(
    mancoosimm::MenuEntry,
)
mancoosimm::Invariant_strategy = st.builds(
    mancoosimm::Invariant,
)
Package_strategy = st.builds(
    Package,
)
mancoosimm::InstalledPackage_strategy = st.builds(
    mancoosimm::InstalledPackage,
    description=
        safe_text,
    maintainer=
        safe_text,
    checkSum=
        safe_text,
    priority=
        safe_text,
    tag=
        safe_text,
    installedSize=
        st.integers(),
    uploaders=
        safe_text,
    fileSize=
        st.integers(),
    section=
        safe_text
)
mancoosimm::NotInstalledPackage_strategy = st.builds(
    mancoosimm::NotInstalledPackage,
)
mancoosimm::HalfInstalledReinstRequiredPackage_strategy = st.builds(
    mancoosimm::HalfInstalledReinstRequiredPackage,
    uploaders=
        safe_text,
    description=
        safe_text,
    priority=
        safe_text,
    checkSum=
        safe_text,
    section=
        safe_text,
    maintainer=
        safe_text,
    tag=
        safe_text
)
mancoosimm::HalfInstalledPackage_strategy = st.builds(
    mancoosimm::HalfInstalledPackage,
    uploaders=
        safe_text,
    checkSum=
        safe_text,
    maintainer=
        safe_text,
    priority=
        safe_text,
    description=
        safe_text,
    section=
        safe_text,
    tag=
        safe_text
)
mancoosimm::UnpackedPackage_strategy = st.builds(
    mancoosimm::UnpackedPackage,
    checkSum=
        safe_text,
    tag=
        safe_text,
    priority=
        safe_text,
    maintainer=
        safe_text,
    uploaders=
        safe_text,
    section=
        safe_text,
    description=
        safe_text
)
mancoosimm::ConfigFilesPackage_strategy = st.builds(
    mancoosimm::ConfigFilesPackage,
    priority=
        safe_text,
    maintainer=
        safe_text,
    section=
        safe_text,
    tag=
        safe_text,
    uploaders=
        safe_text,
    description=
        safe_text,
    checkSum=
        safe_text
)
mancoosimm::PackageSetting_strategy = st.builds(
    mancoosimm::PackageSetting,
)
mancoosimm::Configuration_strategy = st.builds(
    mancoosimm::Configuration,
    creationTime=
        safe_text,
    systemType=
        safe_text
)
mancoosimm::NamedElement_strategy = st.builds(
    mancoosimm::NamedElement,
    name=
        safe_text
)

@given(instance=Conflict_strategy)
@settings(max_examples=50)
def test_conflict_instantiation(instance):
    assert isinstance(instance, Conflict)

@given(instance=mancoosimm::OrConflict_strategy)
@settings(max_examples=50)
def test_mancoosimm::orconflict_instantiation(instance):
    assert isinstance(instance, mancoosimm::OrConflict)

@given(instance=mancoosimm::AndConflict_strategy)
@settings(max_examples=50)
def test_mancoosimm::andconflict_instantiation(instance):
    assert isinstance(instance, mancoosimm::AndConflict)

@given(instance=mancoosimm::SingleConflict_strategy)
@settings(max_examples=50)
def test_mancoosimm::singleconflict_instantiation(instance):
    assert isinstance(instance, mancoosimm::SingleConflict)

@given(instance=mancoosimm::SingleConflict_strategy)
def test_mancoosimm::singleconflict_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=mancoosimm::SingleConflict_strategy)
def test_mancoosimm::singleconflict_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mancoosimm::SingleConflict_strategy)
def test_mancoosimm::singleconflict_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=mancoosimm::SingleConflict_strategy)
def test_mancoosimm::singleconflict_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=mancoosimm::SharedLibrary_strategy)
@settings(max_examples=50)
def test_mancoosimm::sharedlibrary_instantiation(instance):
    assert isinstance(instance, mancoosimm::SharedLibrary)

@given(instance=mancoosimm::SharedLibrary_strategy)
def test_mancoosimm::sharedlibrary_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mancoosimm::SharedLibrary_strategy)
def test_mancoosimm::sharedlibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mancoosimm::SharedLibrary_strategy)
def test_mancoosimm::sharedlibrary_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=mancoosimm::SharedLibrary_strategy)
def test_mancoosimm::sharedlibrary_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=mancoosimm::MimeType_strategy)
@settings(max_examples=50)
def test_mancoosimm::mimetype_instantiation(instance):
    assert isinstance(instance, mancoosimm::MimeType)

@given(instance=mancoosimm::MimeType_strategy)
def test_mancoosimm::mimetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mancoosimm::MimeType_strategy)
def test_mancoosimm::mimetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mancoosimm::MimeType_strategy)
def test_mancoosimm::mimetype_extension_type(instance):
    assert isinstance(instance.extension, str)


@given(instance=mancoosimm::MimeType_strategy)
def test_mancoosimm::mimetype_extension_setter(instance):
    original = instance.extension
    instance.extension = original
    assert instance.extension == original

@given(instance=mancoosimm::MimeTypeHandler_strategy)
@settings(max_examples=50)
def test_mancoosimm::mimetypehandler_instantiation(instance):
    assert isinstance(instance, mancoosimm::MimeTypeHandler)

@given(instance=mancoosimm::Boot_strategy)
@settings(max_examples=50)
def test_mancoosimm::boot_instantiation(instance):
    assert isinstance(instance, mancoosimm::Boot)

@given(instance=File_strategy)
@settings(max_examples=50)
def test_file_instantiation(instance):
    assert isinstance(instance, File)

@given(instance=mancoosimm::InformationFile_strategy)
@settings(max_examples=50)
def test_mancoosimm::informationfile_instantiation(instance):
    assert isinstance(instance, mancoosimm::InformationFile)

@given(instance=mancoosimm::LibraryCache_strategy)
@settings(max_examples=50)
def test_mancoosimm::librarycache_instantiation(instance):
    assert isinstance(instance, mancoosimm::LibraryCache)

@given(instance=mancoosimm::MimeTypeHandlerCache_strategy)
@settings(max_examples=50)
def test_mancoosimm::mimetypehandlercache_instantiation(instance):
    assert isinstance(instance, mancoosimm::MimeTypeHandlerCache)

@given(instance=mancoosimm::DesktopDB_strategy)
@settings(max_examples=50)
def test_mancoosimm::desktopdb_instantiation(instance):
    assert isinstance(instance, mancoosimm::DesktopDB)

@given(instance=mancoosimm::IconCache_strategy)
@settings(max_examples=50)
def test_mancoosimm::iconcache_instantiation(instance):
    assert isinstance(instance, mancoosimm::IconCache)

@given(instance=mancoosimm::IconCache_strategy)
def test_mancoosimm::iconcache_mtime_type(instance):
    assert isinstance(instance.mtime, str)


@given(instance=mancoosimm::IconCache_strategy)
def test_mancoosimm::iconcache_mtime_setter(instance):
    original = instance.mtime
    instance.mtime = original
    assert instance.mtime == original

@given(instance=mancoosimm::Menu_strategy)
@settings(max_examples=50)
def test_mancoosimm::menu_instantiation(instance):
    assert isinstance(instance, mancoosimm::Menu)

@given(instance=mancoosimm::GConf_strategy)
@settings(max_examples=50)
def test_mancoosimm::gconf_instantiation(instance):
    assert isinstance(instance, mancoosimm::GConf)

@given(instance=mancoosimm::XFontCache_strategy)
@settings(max_examples=50)
def test_mancoosimm::xfontcache_instantiation(instance):
    assert isinstance(instance, mancoosimm::XFontCache)

@given(instance=mancoosimm::XFontCache_strategy)
def test_mancoosimm::xfontcache_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=mancoosimm::XFontCache_strategy)
def test_mancoosimm::xfontcache_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=mancoosimm::ModuleCache_strategy)
@settings(max_examples=50)
def test_mancoosimm::modulecache_instantiation(instance):
    assert isinstance(instance, mancoosimm::ModuleCache)

@given(instance=mancoosimm::ModuleCache_strategy)
def test_mancoosimm::modulecache_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=mancoosimm::ModuleCache_strategy)
def test_mancoosimm::modulecache_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=mancoosimm::NotInv_strategy)
@settings(max_examples=50)
def test_mancoosimm::notinv_instantiation(instance):
    assert isinstance(instance, mancoosimm::NotInv)

@given(instance=mancoosimm::OrInv_strategy)
@settings(max_examples=50)
def test_mancoosimm::orinv_instantiation(instance):
    assert isinstance(instance, mancoosimm::OrInv)

@given(instance=mancoosimm::AndInv_strategy)
@settings(max_examples=50)
def test_mancoosimm::andinv_instantiation(instance):
    assert isinstance(instance, mancoosimm::AndInv)

@given(instance=InstalledPackage_strategy)
@settings(max_examples=50)
def test_installedpackage_instantiation(instance):
    assert isinstance(instance, InstalledPackage)

@given(instance=mancoosimm::BinPackage_strategy)
@settings(max_examples=50)
def test_mancoosimm::binpackage_instantiation(instance):
    assert isinstance(instance, mancoosimm::BinPackage)

@given(instance=Dependence_strategy)
@settings(max_examples=50)
def test_dependence_instantiation(instance):
    assert isinstance(instance, Dependence)

@given(instance=mancoosimm::SingleDep_strategy)
@settings(max_examples=50)
def test_mancoosimm::singledep_instantiation(instance):
    assert isinstance(instance, mancoosimm::SingleDep)

@given(instance=mancoosimm::SingleDep_strategy)
def test_mancoosimm::singledep_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=mancoosimm::SingleDep_strategy)
def test_mancoosimm::singledep_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mancoosimm::SingleDep_strategy)
def test_mancoosimm::singledep_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=mancoosimm::SingleDep_strategy)
def test_mancoosimm::singledep_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=mancoosimm::OrDep_strategy)
@settings(max_examples=50)
def test_mancoosimm::ordep_instantiation(instance):
    assert isinstance(instance, mancoosimm::OrDep)

@given(instance=mancoosimm::AndDep_strategy)
@settings(max_examples=50)
def test_mancoosimm::anddep_instantiation(instance):
    assert isinstance(instance, mancoosimm::AndDep)

@given(instance=mancoosimm::Conflict_strategy)
@settings(max_examples=50)
def test_mancoosimm::conflict_instantiation(instance):
    assert isinstance(instance, mancoosimm::Conflict)

@given(instance=mancoosimm::DocumentationFile_strategy)
@settings(max_examples=50)
def test_mancoosimm::documentationfile_instantiation(instance):
    assert isinstance(instance, mancoosimm::DocumentationFile)

@given(instance=mancoosimm::VirtualPackage_strategy)
@settings(max_examples=50)
def test_mancoosimm::virtualpackage_instantiation(instance):
    assert isinstance(instance, mancoosimm::VirtualPackage)

@given(instance=UnpackedPackage_strategy)
@settings(max_examples=50)
def test_unpackedpackage_instantiation(instance):
    assert isinstance(instance, UnpackedPackage)

@given(instance=mancoosimm::HalfConfiguredReinstRequiredPackage_strategy)
@settings(max_examples=50)
def test_mancoosimm::halfconfiguredreinstrequiredpackage_instantiation(instance):
    assert isinstance(instance, mancoosimm::HalfConfiguredReinstRequiredPackage)

@given(instance=mancoosimm::HalfConfiguredPackage_strategy)
@settings(max_examples=50)
def test_mancoosimm::halfconfiguredpackage_instantiation(instance):
    assert isinstance(instance, mancoosimm::HalfConfiguredPackage)

@given(instance=mancoosimm::Dependence_strategy)
@settings(max_examples=50)
def test_mancoosimm::dependence_instantiation(instance):
    assert isinstance(instance, mancoosimm::Dependence)

@given(instance=mancoosimm::SrcPackage_strategy)
@settings(max_examples=50)
def test_mancoosimm::srcpackage_instantiation(instance):
    assert isinstance(instance, mancoosimm::SrcPackage)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=mancoosimm::FileSystem_strategy)
@settings(max_examples=50)
def test_mancoosimm::filesystem_instantiation(instance):
    assert isinstance(instance, mancoosimm::FileSystem)

@given(instance=mancoosimm::Group_strategy)
@settings(max_examples=50)
def test_mancoosimm::group_instantiation(instance):
    assert isinstance(instance, mancoosimm::Group)

@given(instance=mancoosimm::SkeeperDocument_strategy)
@settings(max_examples=50)
def test_mancoosimm::skeeperdocument_instantiation(instance):
    assert isinstance(instance, mancoosimm::SkeeperDocument)

@given(instance=mancoosimm::SGMLDocument_strategy)
@settings(max_examples=50)
def test_mancoosimm::sgmldocument_instantiation(instance):
    assert isinstance(instance, mancoosimm::SGMLDocument)

@given(instance=mancoosimm::Alternative_strategy)
@settings(max_examples=50)
def test_mancoosimm::alternative_instantiation(instance):
    assert isinstance(instance, mancoosimm::Alternative)

@given(instance=mancoosimm::SGMLCatalog_strategy)
@settings(max_examples=50)
def test_mancoosimm::sgmlcatalog_instantiation(instance):
    assert isinstance(instance, mancoosimm::SGMLCatalog)

@given(instance=mancoosimm::File_strategy)
@settings(max_examples=50)
def test_mancoosimm::file_instantiation(instance):
    assert isinstance(instance, mancoosimm::File)

@given(instance=mancoosimm::File_strategy)
def test_mancoosimm::file_checkSum_type(instance):
    assert isinstance(instance.checkSum, str)


@given(instance=mancoosimm::File_strategy)
def test_mancoosimm::file_checkSum_setter(instance):
    original = instance.checkSum
    instance.checkSum = original
    assert instance.checkSum == original

@given(instance=mancoosimm::File_strategy)
def test_mancoosimm::file_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=mancoosimm::File_strategy)
def test_mancoosimm::file_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=mancoosimm::File_strategy)
def test_mancoosimm::file_permission_type(instance):
    assert isinstance(instance.permission, str)


@given(instance=mancoosimm::File_strategy)
def test_mancoosimm::file_permission_setter(instance):
    original = instance.permission
    instance.permission = original
    assert instance.permission == original

@given(instance=mancoosimm::File_strategy)
def test_mancoosimm::file_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=mancoosimm::File_strategy)
def test_mancoosimm::file_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=mancoosimm::File_strategy)
def test_mancoosimm::file_guid_type(instance):
    assert isinstance(instance.guid, bool)


@given(instance=mancoosimm::File_strategy)
def test_mancoosimm::file_guid_setter(instance):
    original = instance.guid
    instance.guid = original
    assert instance.guid == original

@given(instance=mancoosimm::File_strategy)
def test_mancoosimm::file_suid_type(instance):
    assert isinstance(instance.suid, bool)


@given(instance=mancoosimm::File_strategy)
def test_mancoosimm::file_suid_setter(instance):
    original = instance.suid
    instance.suid = original
    assert instance.suid == original

@given(instance=mancoosimm::File_strategy)
def test_mancoosimm::file_isMissing_type(instance):
    assert isinstance(instance.isMissing, bool)


@given(instance=mancoosimm::File_strategy)
def test_mancoosimm::file_isMissing_setter(instance):
    original = instance.isMissing
    instance.isMissing = original
    assert instance.isMissing == original

@given(instance=mancoosimm::File_strategy)
def test_mancoosimm::file_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=mancoosimm::File_strategy)
def test_mancoosimm::file_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=mancoosimm::File_strategy)
def test_mancoosimm::file_extension_type(instance):
    assert isinstance(instance.extension, str)


@given(instance=mancoosimm::File_strategy)
def test_mancoosimm::file_extension_setter(instance):
    original = instance.extension
    instance.extension = original
    assert instance.extension == original

@given(instance=mancoosimm::File_strategy)
def test_mancoosimm::file_isDirectory_type(instance):
    assert isinstance(instance.isDirectory, bool)


@given(instance=mancoosimm::File_strategy)
def test_mancoosimm::file_isDirectory_setter(instance):
    original = instance.isDirectory
    instance.isDirectory = original
    assert instance.isDirectory == original

@given(instance=mancoosimm::ApplicationMenuCatalog_strategy)
@settings(max_examples=50)
def test_mancoosimm::applicationmenucatalog_instantiation(instance):
    assert isinstance(instance, mancoosimm::ApplicationMenuCatalog)

@given(instance=mancoosimm::SkeeperCatalog_strategy)
@settings(max_examples=50)
def test_mancoosimm::skeepercatalog_instantiation(instance):
    assert isinstance(instance, mancoosimm::SkeeperCatalog)

@given(instance=mancoosimm::Environment_strategy)
@settings(max_examples=50)
def test_mancoosimm::environment_instantiation(instance):
    assert isinstance(instance, mancoosimm::Environment)

@given(instance=mancoosimm::Atom_strategy)
@settings(max_examples=50)
def test_mancoosimm::atom_instantiation(instance):
    assert isinstance(instance, mancoosimm::Atom)

@given(instance=mancoosimm::XFont_strategy)
@settings(max_examples=50)
def test_mancoosimm::xfont_instantiation(instance):
    assert isinstance(instance, mancoosimm::XFont)

@given(instance=mancoosimm::EmacsPackage_strategy)
@settings(max_examples=50)
def test_mancoosimm::emacspackage_instantiation(instance):
    assert isinstance(instance, mancoosimm::EmacsPackage)

@given(instance=mancoosimm::Package_strategy)
@settings(max_examples=50)
def test_mancoosimm::package_instantiation(instance):
    assert isinstance(instance, mancoosimm::Package)

@given(instance=mancoosimm::Package_strategy)
def test_mancoosimm::package_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=mancoosimm::Package_strategy)
def test_mancoosimm::package_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=mancoosimm::Package_strategy)
def test_mancoosimm::package_architecture_type(instance):
    assert isinstance(instance.architecture, str)


@given(instance=mancoosimm::Package_strategy)
def test_mancoosimm::package_architecture_setter(instance):
    original = instance.architecture
    instance.architecture = original
    assert instance.architecture == original

@given(instance=mancoosimm::User_strategy)
@settings(max_examples=50)
def test_mancoosimm::user_instantiation(instance):
    assert isinstance(instance, mancoosimm::User)

@given(instance=mancoosimm::Service_strategy)
@settings(max_examples=50)
def test_mancoosimm::service_instantiation(instance):
    assert isinstance(instance, mancoosimm::Service)

@given(instance=mancoosimm::Module_strategy)
@settings(max_examples=50)
def test_mancoosimm::module_instantiation(instance):
    assert isinstance(instance, mancoosimm::Module)

@given(instance=mancoosimm::MenuEntry_strategy)
@settings(max_examples=50)
def test_mancoosimm::menuentry_instantiation(instance):
    assert isinstance(instance, mancoosimm::MenuEntry)

@given(instance=mancoosimm::Invariant_strategy)
@settings(max_examples=50)
def test_mancoosimm::invariant_instantiation(instance):
    assert isinstance(instance, mancoosimm::Invariant)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=mancoosimm::InstalledPackage_strategy)
@settings(max_examples=50)
def test_mancoosimm::installedpackage_instantiation(instance):
    assert isinstance(instance, mancoosimm::InstalledPackage)

@given(instance=mancoosimm::InstalledPackage_strategy)
def test_mancoosimm::installedpackage_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=mancoosimm::InstalledPackage_strategy)
def test_mancoosimm::installedpackage_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=mancoosimm::InstalledPackage_strategy)
def test_mancoosimm::installedpackage_maintainer_type(instance):
    assert isinstance(instance.maintainer, str)


@given(instance=mancoosimm::InstalledPackage_strategy)
def test_mancoosimm::installedpackage_maintainer_setter(instance):
    original = instance.maintainer
    instance.maintainer = original
    assert instance.maintainer == original

@given(instance=mancoosimm::InstalledPackage_strategy)
def test_mancoosimm::installedpackage_checkSum_type(instance):
    assert isinstance(instance.checkSum, str)


@given(instance=mancoosimm::InstalledPackage_strategy)
def test_mancoosimm::installedpackage_checkSum_setter(instance):
    original = instance.checkSum
    instance.checkSum = original
    assert instance.checkSum == original

@given(instance=mancoosimm::InstalledPackage_strategy)
def test_mancoosimm::installedpackage_priority_type(instance):
    assert isinstance(instance.priority, str)


@given(instance=mancoosimm::InstalledPackage_strategy)
def test_mancoosimm::installedpackage_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=mancoosimm::InstalledPackage_strategy)
def test_mancoosimm::installedpackage_tag_type(instance):
    assert isinstance(instance.tag, str)


@given(instance=mancoosimm::InstalledPackage_strategy)
def test_mancoosimm::installedpackage_tag_setter(instance):
    original = instance.tag
    instance.tag = original
    assert instance.tag == original

@given(instance=mancoosimm::InstalledPackage_strategy)
def test_mancoosimm::installedpackage_installedSize_type(instance):
    assert isinstance(instance.installedSize, int)


@given(instance=mancoosimm::InstalledPackage_strategy)
def test_mancoosimm::installedpackage_installedSize_setter(instance):
    original = instance.installedSize
    instance.installedSize = original
    assert instance.installedSize == original

@given(instance=mancoosimm::InstalledPackage_strategy)
def test_mancoosimm::installedpackage_uploaders_type(instance):
    assert isinstance(instance.uploaders, str)


@given(instance=mancoosimm::InstalledPackage_strategy)
def test_mancoosimm::installedpackage_uploaders_setter(instance):
    original = instance.uploaders
    instance.uploaders = original
    assert instance.uploaders == original

@given(instance=mancoosimm::InstalledPackage_strategy)
def test_mancoosimm::installedpackage_fileSize_type(instance):
    assert isinstance(instance.fileSize, int)


@given(instance=mancoosimm::InstalledPackage_strategy)
def test_mancoosimm::installedpackage_fileSize_setter(instance):
    original = instance.fileSize
    instance.fileSize = original
    assert instance.fileSize == original

@given(instance=mancoosimm::InstalledPackage_strategy)
def test_mancoosimm::installedpackage_section_type(instance):
    assert isinstance(instance.section, str)


@given(instance=mancoosimm::InstalledPackage_strategy)
def test_mancoosimm::installedpackage_section_setter(instance):
    original = instance.section
    instance.section = original
    assert instance.section == original

@given(instance=mancoosimm::NotInstalledPackage_strategy)
@settings(max_examples=50)
def test_mancoosimm::notinstalledpackage_instantiation(instance):
    assert isinstance(instance, mancoosimm::NotInstalledPackage)

@given(instance=mancoosimm::HalfInstalledReinstRequiredPackage_strategy)
@settings(max_examples=50)
def test_mancoosimm::halfinstalledreinstrequiredpackage_instantiation(instance):
    assert isinstance(instance, mancoosimm::HalfInstalledReinstRequiredPackage)

@given(instance=mancoosimm::HalfInstalledReinstRequiredPackage_strategy)
def test_mancoosimm::halfinstalledreinstrequiredpackage_uploaders_type(instance):
    assert isinstance(instance.uploaders, str)


@given(instance=mancoosimm::HalfInstalledReinstRequiredPackage_strategy)
def test_mancoosimm::halfinstalledreinstrequiredpackage_uploaders_setter(instance):
    original = instance.uploaders
    instance.uploaders = original
    assert instance.uploaders == original

@given(instance=mancoosimm::HalfInstalledReinstRequiredPackage_strategy)
def test_mancoosimm::halfinstalledreinstrequiredpackage_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=mancoosimm::HalfInstalledReinstRequiredPackage_strategy)
def test_mancoosimm::halfinstalledreinstrequiredpackage_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=mancoosimm::HalfInstalledReinstRequiredPackage_strategy)
def test_mancoosimm::halfinstalledreinstrequiredpackage_priority_type(instance):
    assert isinstance(instance.priority, str)


@given(instance=mancoosimm::HalfInstalledReinstRequiredPackage_strategy)
def test_mancoosimm::halfinstalledreinstrequiredpackage_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=mancoosimm::HalfInstalledReinstRequiredPackage_strategy)
def test_mancoosimm::halfinstalledreinstrequiredpackage_checkSum_type(instance):
    assert isinstance(instance.checkSum, str)


@given(instance=mancoosimm::HalfInstalledReinstRequiredPackage_strategy)
def test_mancoosimm::halfinstalledreinstrequiredpackage_checkSum_setter(instance):
    original = instance.checkSum
    instance.checkSum = original
    assert instance.checkSum == original

@given(instance=mancoosimm::HalfInstalledReinstRequiredPackage_strategy)
def test_mancoosimm::halfinstalledreinstrequiredpackage_section_type(instance):
    assert isinstance(instance.section, str)


@given(instance=mancoosimm::HalfInstalledReinstRequiredPackage_strategy)
def test_mancoosimm::halfinstalledreinstrequiredpackage_section_setter(instance):
    original = instance.section
    instance.section = original
    assert instance.section == original

@given(instance=mancoosimm::HalfInstalledReinstRequiredPackage_strategy)
def test_mancoosimm::halfinstalledreinstrequiredpackage_maintainer_type(instance):
    assert isinstance(instance.maintainer, str)


@given(instance=mancoosimm::HalfInstalledReinstRequiredPackage_strategy)
def test_mancoosimm::halfinstalledreinstrequiredpackage_maintainer_setter(instance):
    original = instance.maintainer
    instance.maintainer = original
    assert instance.maintainer == original

@given(instance=mancoosimm::HalfInstalledReinstRequiredPackage_strategy)
def test_mancoosimm::halfinstalledreinstrequiredpackage_tag_type(instance):
    assert isinstance(instance.tag, str)


@given(instance=mancoosimm::HalfInstalledReinstRequiredPackage_strategy)
def test_mancoosimm::halfinstalledreinstrequiredpackage_tag_setter(instance):
    original = instance.tag
    instance.tag = original
    assert instance.tag == original

@given(instance=mancoosimm::HalfInstalledPackage_strategy)
@settings(max_examples=50)
def test_mancoosimm::halfinstalledpackage_instantiation(instance):
    assert isinstance(instance, mancoosimm::HalfInstalledPackage)

@given(instance=mancoosimm::HalfInstalledPackage_strategy)
def test_mancoosimm::halfinstalledpackage_uploaders_type(instance):
    assert isinstance(instance.uploaders, str)


@given(instance=mancoosimm::HalfInstalledPackage_strategy)
def test_mancoosimm::halfinstalledpackage_uploaders_setter(instance):
    original = instance.uploaders
    instance.uploaders = original
    assert instance.uploaders == original

@given(instance=mancoosimm::HalfInstalledPackage_strategy)
def test_mancoosimm::halfinstalledpackage_checkSum_type(instance):
    assert isinstance(instance.checkSum, str)


@given(instance=mancoosimm::HalfInstalledPackage_strategy)
def test_mancoosimm::halfinstalledpackage_checkSum_setter(instance):
    original = instance.checkSum
    instance.checkSum = original
    assert instance.checkSum == original

@given(instance=mancoosimm::HalfInstalledPackage_strategy)
def test_mancoosimm::halfinstalledpackage_maintainer_type(instance):
    assert isinstance(instance.maintainer, str)


@given(instance=mancoosimm::HalfInstalledPackage_strategy)
def test_mancoosimm::halfinstalledpackage_maintainer_setter(instance):
    original = instance.maintainer
    instance.maintainer = original
    assert instance.maintainer == original

@given(instance=mancoosimm::HalfInstalledPackage_strategy)
def test_mancoosimm::halfinstalledpackage_priority_type(instance):
    assert isinstance(instance.priority, str)


@given(instance=mancoosimm::HalfInstalledPackage_strategy)
def test_mancoosimm::halfinstalledpackage_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=mancoosimm::HalfInstalledPackage_strategy)
def test_mancoosimm::halfinstalledpackage_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=mancoosimm::HalfInstalledPackage_strategy)
def test_mancoosimm::halfinstalledpackage_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=mancoosimm::HalfInstalledPackage_strategy)
def test_mancoosimm::halfinstalledpackage_section_type(instance):
    assert isinstance(instance.section, str)


@given(instance=mancoosimm::HalfInstalledPackage_strategy)
def test_mancoosimm::halfinstalledpackage_section_setter(instance):
    original = instance.section
    instance.section = original
    assert instance.section == original

@given(instance=mancoosimm::HalfInstalledPackage_strategy)
def test_mancoosimm::halfinstalledpackage_tag_type(instance):
    assert isinstance(instance.tag, str)


@given(instance=mancoosimm::HalfInstalledPackage_strategy)
def test_mancoosimm::halfinstalledpackage_tag_setter(instance):
    original = instance.tag
    instance.tag = original
    assert instance.tag == original

@given(instance=mancoosimm::UnpackedPackage_strategy)
@settings(max_examples=50)
def test_mancoosimm::unpackedpackage_instantiation(instance):
    assert isinstance(instance, mancoosimm::UnpackedPackage)

@given(instance=mancoosimm::UnpackedPackage_strategy)
def test_mancoosimm::unpackedpackage_checkSum_type(instance):
    assert isinstance(instance.checkSum, str)


@given(instance=mancoosimm::UnpackedPackage_strategy)
def test_mancoosimm::unpackedpackage_checkSum_setter(instance):
    original = instance.checkSum
    instance.checkSum = original
    assert instance.checkSum == original

@given(instance=mancoosimm::UnpackedPackage_strategy)
def test_mancoosimm::unpackedpackage_tag_type(instance):
    assert isinstance(instance.tag, str)


@given(instance=mancoosimm::UnpackedPackage_strategy)
def test_mancoosimm::unpackedpackage_tag_setter(instance):
    original = instance.tag
    instance.tag = original
    assert instance.tag == original

@given(instance=mancoosimm::UnpackedPackage_strategy)
def test_mancoosimm::unpackedpackage_priority_type(instance):
    assert isinstance(instance.priority, str)


@given(instance=mancoosimm::UnpackedPackage_strategy)
def test_mancoosimm::unpackedpackage_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=mancoosimm::UnpackedPackage_strategy)
def test_mancoosimm::unpackedpackage_maintainer_type(instance):
    assert isinstance(instance.maintainer, str)


@given(instance=mancoosimm::UnpackedPackage_strategy)
def test_mancoosimm::unpackedpackage_maintainer_setter(instance):
    original = instance.maintainer
    instance.maintainer = original
    assert instance.maintainer == original

@given(instance=mancoosimm::UnpackedPackage_strategy)
def test_mancoosimm::unpackedpackage_uploaders_type(instance):
    assert isinstance(instance.uploaders, str)


@given(instance=mancoosimm::UnpackedPackage_strategy)
def test_mancoosimm::unpackedpackage_uploaders_setter(instance):
    original = instance.uploaders
    instance.uploaders = original
    assert instance.uploaders == original

@given(instance=mancoosimm::UnpackedPackage_strategy)
def test_mancoosimm::unpackedpackage_section_type(instance):
    assert isinstance(instance.section, str)


@given(instance=mancoosimm::UnpackedPackage_strategy)
def test_mancoosimm::unpackedpackage_section_setter(instance):
    original = instance.section
    instance.section = original
    assert instance.section == original

@given(instance=mancoosimm::UnpackedPackage_strategy)
def test_mancoosimm::unpackedpackage_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=mancoosimm::UnpackedPackage_strategy)
def test_mancoosimm::unpackedpackage_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=mancoosimm::ConfigFilesPackage_strategy)
@settings(max_examples=50)
def test_mancoosimm::configfilespackage_instantiation(instance):
    assert isinstance(instance, mancoosimm::ConfigFilesPackage)

@given(instance=mancoosimm::ConfigFilesPackage_strategy)
def test_mancoosimm::configfilespackage_priority_type(instance):
    assert isinstance(instance.priority, str)


@given(instance=mancoosimm::ConfigFilesPackage_strategy)
def test_mancoosimm::configfilespackage_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=mancoosimm::ConfigFilesPackage_strategy)
def test_mancoosimm::configfilespackage_maintainer_type(instance):
    assert isinstance(instance.maintainer, str)


@given(instance=mancoosimm::ConfigFilesPackage_strategy)
def test_mancoosimm::configfilespackage_maintainer_setter(instance):
    original = instance.maintainer
    instance.maintainer = original
    assert instance.maintainer == original

@given(instance=mancoosimm::ConfigFilesPackage_strategy)
def test_mancoosimm::configfilespackage_section_type(instance):
    assert isinstance(instance.section, str)


@given(instance=mancoosimm::ConfigFilesPackage_strategy)
def test_mancoosimm::configfilespackage_section_setter(instance):
    original = instance.section
    instance.section = original
    assert instance.section == original

@given(instance=mancoosimm::ConfigFilesPackage_strategy)
def test_mancoosimm::configfilespackage_tag_type(instance):
    assert isinstance(instance.tag, str)


@given(instance=mancoosimm::ConfigFilesPackage_strategy)
def test_mancoosimm::configfilespackage_tag_setter(instance):
    original = instance.tag
    instance.tag = original
    assert instance.tag == original

@given(instance=mancoosimm::ConfigFilesPackage_strategy)
def test_mancoosimm::configfilespackage_uploaders_type(instance):
    assert isinstance(instance.uploaders, str)


@given(instance=mancoosimm::ConfigFilesPackage_strategy)
def test_mancoosimm::configfilespackage_uploaders_setter(instance):
    original = instance.uploaders
    instance.uploaders = original
    assert instance.uploaders == original

@given(instance=mancoosimm::ConfigFilesPackage_strategy)
def test_mancoosimm::configfilespackage_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=mancoosimm::ConfigFilesPackage_strategy)
def test_mancoosimm::configfilespackage_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=mancoosimm::ConfigFilesPackage_strategy)
def test_mancoosimm::configfilespackage_checkSum_type(instance):
    assert isinstance(instance.checkSum, str)


@given(instance=mancoosimm::ConfigFilesPackage_strategy)
def test_mancoosimm::configfilespackage_checkSum_setter(instance):
    original = instance.checkSum
    instance.checkSum = original
    assert instance.checkSum == original

@given(instance=mancoosimm::PackageSetting_strategy)
@settings(max_examples=50)
def test_mancoosimm::packagesetting_instantiation(instance):
    assert isinstance(instance, mancoosimm::PackageSetting)

@given(instance=mancoosimm::Configuration_strategy)
@settings(max_examples=50)
def test_mancoosimm::configuration_instantiation(instance):
    assert isinstance(instance, mancoosimm::Configuration)

@given(instance=mancoosimm::Configuration_strategy)
def test_mancoosimm::configuration_creationTime_type(instance):
    assert isinstance(instance.creationTime, str)


@given(instance=mancoosimm::Configuration_strategy)
def test_mancoosimm::configuration_creationTime_setter(instance):
    original = instance.creationTime
    instance.creationTime = original
    assert instance.creationTime == original

@given(instance=mancoosimm::Configuration_strategy)
def test_mancoosimm::configuration_systemType_type(instance):
    assert isinstance(instance.systemType, str)


@given(instance=mancoosimm::Configuration_strategy)
def test_mancoosimm::configuration_systemType_setter(instance):
    original = instance.systemType
    instance.systemType = original
    assert instance.systemType == original

@given(instance=mancoosimm::NamedElement_strategy)
@settings(max_examples=50)
def test_mancoosimm::namedelement_instantiation(instance):
    assert isinstance(instance, mancoosimm::NamedElement)

@given(instance=mancoosimm::NamedElement_strategy)
def test_mancoosimm::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mancoosimm::NamedElement_strategy)
def test_mancoosimm::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
