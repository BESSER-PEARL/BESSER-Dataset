import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    DatadiagramMLXForm::CustomPropertiesCollection,
    VBProjectData,
    HeaderFooter,
    EventList,
    WindowsInfo,
    PagesCollection,
    MastersCollection,
    DocumentSheet,
    StyleSheetsCollection,
    VisioDocument,
    DatadiagramMLXForm::DocumentPropertiesCollection,
    SolutionXML,
    EmailRoutingData,
    DocumentPropertiesCollection,
    DatadiagramMLXForm::VisioDocument,
    FaceNamesTable,
    FontsTable,
    PrintSetup,
    DatadiagramMLXForm::CellType,
    ColorsTable,
    DocumentSettingsElt,
    DatadiagramMLXForm::DateTimeType,
    DatadiagramMLXForm::SolutionXML,
    DatadiagramMLXForm::HeaderFooter,
    DatadiagramMLXForm::EventList,
    DatadiagramMLXForm::WindowsInfo,
    DatadiagramMLXForm::PageElt,
    DatadiagramMLXForm::PagesCollection,
    DatadiagramMLXForm::MasterElt,
    Connect,
    ConnectsCollection,
    DatadiagramMLXForm::Connect,
    MasterShortCut,
    Master,
    Icon,
    DatadiagramMLXForm::MastersCollection,
    TabsCollection,
    Tab,
    TextElt,
    DatadiagramMLXForm::StringElt,
    XYABCDEElt,
    DatadiagramMLXForm::NURBSTo,
    XYABCDElt,
    DatadiagramMLXForm::EllipticalArcTo,
    DatadiagramMLXForm::XYABCDEElt,
    DatadiagramMLXForm::SplineStart,
    DatadiagramMLXForm::Ellipse,
    DatadiagramMLXForm::IXrequiredElt,
    Text,
    DatadiagramMLXForm::TextElt,
    Geom,
    XYElt,
    DatadiagramMLXForm::LineTo,
    XYABElt,
    DatadiagramMLXForm::XYABCDElt,
    DatadiagramMLXForm::InfiniteLine,
    XYAElt,
    DatadiagramMLXForm::SplineKnot,
    DatadiagramMLXForm::PolylineTo,
    DatadiagramMLXForm::XYABElt,
    DatadiagramMLXForm::ArcTo,
    DatadiagramMLXForm::XYAElt,
    DatadiagramMLXForm::MoveTo,
    CellType,
    NURBSTo,
    SplineStart,
    EllipticalArcTo,
    Ellipse,
    InfiniteLine,
    PolylineTo,
    SplineKnot,
    ArcTo,
    MoveTo,
    LineTo,
    DatadiagramMLXForm::IdentifiedElt,
    DatadiagramMLXForm::NamedElt,
    PageElt,
    MasterElt,
    DatadiagramMLXForm::Icon,
    DatadiagramMLXForm::ShapesCollection,
    DatadiagramMLXForm::ConnectsCollection,
    UniqueIdElt,
    DelElt,
    IXElt,
    DatadiagramMLXForm::Tab,
    DatadiagramMLXForm::XYElt,
    DatadiagramMLXForm::DelElt,
    DatadiagramMLXForm::IXElt,
    DatadiagramMLXForm::ShapeElt,
    ShapeElt,
    DatadiagramMLXForm::XForm,
    DatadiagramMLXForm::Field,
    DatadiagramMLXForm::Char,
    DatadiagramMLXForm::Text,
    DatadiagramMLXForm::TabsCollection,
    DatadiagramMLXForm::Para,
    DatadiagramMLXForm::Geom,
    ShapesCollection,
    DatadiagramMLXForm::Shape,
    DatadiagramMLXForm::UniqueIdElt,
    PageSheet,
    NamedElt,
    DatadiagramMLXForm::DocumentSheet,
    Shape,
    DatadiagramMLXForm::PageSheet,
    FaceName,
    DatadiagramMLXForm::FaceNamesTable,
    DatadiagramMLXForm::StyleSheetsCollection,
    DatadiagramMLXForm::EmailRoutingData,
    DatadiagramMLXForm::VBProjectData,
    IdentifiedElt,
    DatadiagramMLXForm::MasterShortCut,
    DatadiagramMLXForm::FaceName,
    DatadiagramMLXForm::StyleSheet,
    DatadiagramMLXForm::Page,
    DatadiagramMLXForm::Master,
    DatadiagramMLXForm::FontEntry,
    FontEntry,
    DatadiagramMLXForm::FontsTable,
    DatadiagramMLXForm::PrintSetup,
    SnapAnglesCollection,
    IXrequiredElt,
    DatadiagramMLXForm::Pp,
    DatadiagramMLXForm::Tp,
    DatadiagramMLXForm::Fld,
    DatadiagramMLXForm::Cp,
    DatadiagramMLXForm::ColorEntry,
    ColorEntry,
    StyleSheet,
    DatadiagramMLXForm::ColorsTable,
    Page,
    DatadiagramMLXForm::SnapAngle,
    SnapAngle,
    DatadiagramMLXForm::SnapAnglesCollection,
    DateTimeType,
    CustomPropertiesCollection,
    DatadiagramMLXForm::DocumentSettingsElt,
    DatadiagramMLXForm::CustomProperty,
    CustomProperty,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_datadiagrammlxform::custompropertiescollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::CustomPropertiesCollection)


def test_datadiagrammlxform::custompropertiescollection_constructor_exists():
    assert callable(DatadiagramMLXForm::CustomPropertiesCollection.__init__)


def test_datadiagrammlxform::custompropertiescollection_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::CustomPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_vbprojectdata_is_not_abstract():
    assert not inspect.isabstract(VBProjectData)


def test_vbprojectdata_constructor_exists():
    assert callable(VBProjectData.__init__)


def test_vbprojectdata_constructor_args():
    sig = inspect.signature(VBProjectData.__init__)
    params = list(sig.parameters.keys())



def test_headerfooter_is_not_abstract():
    assert not inspect.isabstract(HeaderFooter)


def test_headerfooter_constructor_exists():
    assert callable(HeaderFooter.__init__)


def test_headerfooter_constructor_args():
    sig = inspect.signature(HeaderFooter.__init__)
    params = list(sig.parameters.keys())



def test_eventlist_is_not_abstract():
    assert not inspect.isabstract(EventList)


def test_eventlist_constructor_exists():
    assert callable(EventList.__init__)


def test_eventlist_constructor_args():
    sig = inspect.signature(EventList.__init__)
    params = list(sig.parameters.keys())



def test_windowsinfo_is_not_abstract():
    assert not inspect.isabstract(WindowsInfo)


def test_windowsinfo_constructor_exists():
    assert callable(WindowsInfo.__init__)


def test_windowsinfo_constructor_args():
    sig = inspect.signature(WindowsInfo.__init__)
    params = list(sig.parameters.keys())



def test_pagescollection_is_not_abstract():
    assert not inspect.isabstract(PagesCollection)


def test_pagescollection_constructor_exists():
    assert callable(PagesCollection.__init__)


def test_pagescollection_constructor_args():
    sig = inspect.signature(PagesCollection.__init__)
    params = list(sig.parameters.keys())



def test_masterscollection_is_not_abstract():
    assert not inspect.isabstract(MastersCollection)


def test_masterscollection_constructor_exists():
    assert callable(MastersCollection.__init__)


def test_masterscollection_constructor_args():
    sig = inspect.signature(MastersCollection.__init__)
    params = list(sig.parameters.keys())



def test_documentsheet_is_not_abstract():
    assert not inspect.isabstract(DocumentSheet)


def test_documentsheet_constructor_exists():
    assert callable(DocumentSheet.__init__)


def test_documentsheet_constructor_args():
    sig = inspect.signature(DocumentSheet.__init__)
    params = list(sig.parameters.keys())



def test_stylesheetscollection_is_not_abstract():
    assert not inspect.isabstract(StyleSheetsCollection)


def test_stylesheetscollection_constructor_exists():
    assert callable(StyleSheetsCollection.__init__)


def test_stylesheetscollection_constructor_args():
    sig = inspect.signature(StyleSheetsCollection.__init__)
    params = list(sig.parameters.keys())



def test_visiodocument_is_not_abstract():
    assert not inspect.isabstract(VisioDocument)


def test_visiodocument_constructor_exists():
    assert callable(VisioDocument.__init__)


def test_visiodocument_constructor_args():
    sig = inspect.signature(VisioDocument.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::documentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::DocumentPropertiesCollection)


def test_datadiagrammlxform::documentpropertiescollection_constructor_exists():
    assert callable(DatadiagramMLXForm::DocumentPropertiesCollection.__init__)


def test_datadiagrammlxform::documentpropertiescollection_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::DocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())
    assert "category" in params, "Missing parameter 'category'"
    assert "buildNumberEdited" in params, "Missing parameter 'buildNumberEdited'"
    assert "template" in params, "Missing parameter 'template'"
    assert "hyperlinkBase_href" in params, "Missing parameter 'hyperlinkBase_href'"
    assert "alternateNames" in params, "Missing parameter 'alternateNames'"
    assert "keywords" in params, "Missing parameter 'keywords'"
    assert "subject" in params, "Missing parameter 'subject'"
    assert "creator" in params, "Missing parameter 'creator'"
    assert "title" in params, "Missing parameter 'title'"
    assert "manager" in params, "Missing parameter 'manager'"
    assert "description" in params, "Missing parameter 'description'"
    assert "buildNumberCreated" in params, "Missing parameter 'buildNumberCreated'"
    assert "company" in params, "Missing parameter 'company'"

def test_datadiagrammlxform::documentpropertiescollection_has_category():
    assert hasattr(DatadiagramMLXForm::DocumentPropertiesCollection, "category")
    descriptor = None
    for klass in DatadiagramMLXForm::DocumentPropertiesCollection.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::documentpropertiescollection_has_buildNumberEdited():
    assert hasattr(DatadiagramMLXForm::DocumentPropertiesCollection, "buildNumberEdited")
    descriptor = None
    for klass in DatadiagramMLXForm::DocumentPropertiesCollection.__mro__:
        if "buildNumberEdited" in klass.__dict__:
            descriptor = klass.__dict__["buildNumberEdited"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::documentpropertiescollection_has_template():
    assert hasattr(DatadiagramMLXForm::DocumentPropertiesCollection, "template")
    descriptor = None
    for klass in DatadiagramMLXForm::DocumentPropertiesCollection.__mro__:
        if "template" in klass.__dict__:
            descriptor = klass.__dict__["template"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::documentpropertiescollection_has_hyperlinkBase_href():
    assert hasattr(DatadiagramMLXForm::DocumentPropertiesCollection, "hyperlinkBase_href")
    descriptor = None
    for klass in DatadiagramMLXForm::DocumentPropertiesCollection.__mro__:
        if "hyperlinkBase_href" in klass.__dict__:
            descriptor = klass.__dict__["hyperlinkBase_href"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::documentpropertiescollection_has_alternateNames():
    assert hasattr(DatadiagramMLXForm::DocumentPropertiesCollection, "alternateNames")
    descriptor = None
    for klass in DatadiagramMLXForm::DocumentPropertiesCollection.__mro__:
        if "alternateNames" in klass.__dict__:
            descriptor = klass.__dict__["alternateNames"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::documentpropertiescollection_has_keywords():
    assert hasattr(DatadiagramMLXForm::DocumentPropertiesCollection, "keywords")
    descriptor = None
    for klass in DatadiagramMLXForm::DocumentPropertiesCollection.__mro__:
        if "keywords" in klass.__dict__:
            descriptor = klass.__dict__["keywords"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::documentpropertiescollection_has_subject():
    assert hasattr(DatadiagramMLXForm::DocumentPropertiesCollection, "subject")
    descriptor = None
    for klass in DatadiagramMLXForm::DocumentPropertiesCollection.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::documentpropertiescollection_has_creator():
    assert hasattr(DatadiagramMLXForm::DocumentPropertiesCollection, "creator")
    descriptor = None
    for klass in DatadiagramMLXForm::DocumentPropertiesCollection.__mro__:
        if "creator" in klass.__dict__:
            descriptor = klass.__dict__["creator"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::documentpropertiescollection_has_title():
    assert hasattr(DatadiagramMLXForm::DocumentPropertiesCollection, "title")
    descriptor = None
    for klass in DatadiagramMLXForm::DocumentPropertiesCollection.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::documentpropertiescollection_has_manager():
    assert hasattr(DatadiagramMLXForm::DocumentPropertiesCollection, "manager")
    descriptor = None
    for klass in DatadiagramMLXForm::DocumentPropertiesCollection.__mro__:
        if "manager" in klass.__dict__:
            descriptor = klass.__dict__["manager"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::documentpropertiescollection_has_description():
    assert hasattr(DatadiagramMLXForm::DocumentPropertiesCollection, "description")
    descriptor = None
    for klass in DatadiagramMLXForm::DocumentPropertiesCollection.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::documentpropertiescollection_has_buildNumberCreated():
    assert hasattr(DatadiagramMLXForm::DocumentPropertiesCollection, "buildNumberCreated")
    descriptor = None
    for klass in DatadiagramMLXForm::DocumentPropertiesCollection.__mro__:
        if "buildNumberCreated" in klass.__dict__:
            descriptor = klass.__dict__["buildNumberCreated"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::documentpropertiescollection_has_company():
    assert hasattr(DatadiagramMLXForm::DocumentPropertiesCollection, "company")
    descriptor = None
    for klass in DatadiagramMLXForm::DocumentPropertiesCollection.__mro__:
        if "company" in klass.__dict__:
            descriptor = klass.__dict__["company"]
            break
    assert isinstance(descriptor, property)



def test_solutionxml_is_not_abstract():
    assert not inspect.isabstract(SolutionXML)


def test_solutionxml_constructor_exists():
    assert callable(SolutionXML.__init__)


def test_solutionxml_constructor_args():
    sig = inspect.signature(SolutionXML.__init__)
    params = list(sig.parameters.keys())



def test_emailroutingdata_is_not_abstract():
    assert not inspect.isabstract(EmailRoutingData)


def test_emailroutingdata_constructor_exists():
    assert callable(EmailRoutingData.__init__)


def test_emailroutingdata_constructor_args():
    sig = inspect.signature(EmailRoutingData.__init__)
    params = list(sig.parameters.keys())



def test_documentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(DocumentPropertiesCollection)


def test_documentpropertiescollection_constructor_exists():
    assert callable(DocumentPropertiesCollection.__init__)


def test_documentpropertiescollection_constructor_args():
    sig = inspect.signature(DocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::visiodocument_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::VisioDocument)


def test_datadiagrammlxform::visiodocument_constructor_exists():
    assert callable(DatadiagramMLXForm::VisioDocument.__init__)


def test_datadiagrammlxform::visiodocument_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::VisioDocument.__init__)
    params = list(sig.parameters.keys())
    assert "docLangId" in params, "Missing parameter 'docLangId'"
    assert "key" in params, "Missing parameter 'key'"
    assert "start" in params, "Missing parameter 'start'"
    assert "buildnum" in params, "Missing parameter 'buildnum'"
    assert "version" in params, "Missing parameter 'version'"
    assert "metric" in params, "Missing parameter 'metric'"

def test_datadiagrammlxform::visiodocument_has_docLangId():
    assert hasattr(DatadiagramMLXForm::VisioDocument, "docLangId")
    descriptor = None
    for klass in DatadiagramMLXForm::VisioDocument.__mro__:
        if "docLangId" in klass.__dict__:
            descriptor = klass.__dict__["docLangId"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::visiodocument_has_key():
    assert hasattr(DatadiagramMLXForm::VisioDocument, "key")
    descriptor = None
    for klass in DatadiagramMLXForm::VisioDocument.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::visiodocument_has_start():
    assert hasattr(DatadiagramMLXForm::VisioDocument, "start")
    descriptor = None
    for klass in DatadiagramMLXForm::VisioDocument.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::visiodocument_has_buildnum():
    assert hasattr(DatadiagramMLXForm::VisioDocument, "buildnum")
    descriptor = None
    for klass in DatadiagramMLXForm::VisioDocument.__mro__:
        if "buildnum" in klass.__dict__:
            descriptor = klass.__dict__["buildnum"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::visiodocument_has_version():
    assert hasattr(DatadiagramMLXForm::VisioDocument, "version")
    descriptor = None
    for klass in DatadiagramMLXForm::VisioDocument.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::visiodocument_has_metric():
    assert hasattr(DatadiagramMLXForm::VisioDocument, "metric")
    descriptor = None
    for klass in DatadiagramMLXForm::VisioDocument.__mro__:
        if "metric" in klass.__dict__:
            descriptor = klass.__dict__["metric"]
            break
    assert isinstance(descriptor, property)



def test_facenamestable_is_not_abstract():
    assert not inspect.isabstract(FaceNamesTable)


def test_facenamestable_constructor_exists():
    assert callable(FaceNamesTable.__init__)


def test_facenamestable_constructor_args():
    sig = inspect.signature(FaceNamesTable.__init__)
    params = list(sig.parameters.keys())



def test_fontstable_is_not_abstract():
    assert not inspect.isabstract(FontsTable)


def test_fontstable_constructor_exists():
    assert callable(FontsTable.__init__)


def test_fontstable_constructor_args():
    sig = inspect.signature(FontsTable.__init__)
    params = list(sig.parameters.keys())



def test_printsetup_is_not_abstract():
    assert not inspect.isabstract(PrintSetup)


def test_printsetup_constructor_exists():
    assert callable(PrintSetup.__init__)


def test_printsetup_constructor_args():
    sig = inspect.signature(PrintSetup.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::celltype_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::CellType)


def test_datadiagrammlxform::celltype_constructor_exists():
    assert callable(DatadiagramMLXForm::CellType.__init__)


def test_datadiagrammlxform::celltype_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::CellType.__init__)
    params = list(sig.parameters.keys())
    assert "err" in params, "Missing parameter 'err'"
    assert "unit" in params, "Missing parameter 'unit'"
    assert "value" in params, "Missing parameter 'value'"
    assert "formula" in params, "Missing parameter 'formula'"

def test_datadiagrammlxform::celltype_has_err():
    assert hasattr(DatadiagramMLXForm::CellType, "err")
    descriptor = None
    for klass in DatadiagramMLXForm::CellType.__mro__:
        if "err" in klass.__dict__:
            descriptor = klass.__dict__["err"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::celltype_has_unit():
    assert hasattr(DatadiagramMLXForm::CellType, "unit")
    descriptor = None
    for klass in DatadiagramMLXForm::CellType.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::celltype_has_value():
    assert hasattr(DatadiagramMLXForm::CellType, "value")
    descriptor = None
    for klass in DatadiagramMLXForm::CellType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::celltype_has_formula():
    assert hasattr(DatadiagramMLXForm::CellType, "formula")
    descriptor = None
    for klass in DatadiagramMLXForm::CellType.__mro__:
        if "formula" in klass.__dict__:
            descriptor = klass.__dict__["formula"]
            break
    assert isinstance(descriptor, property)



def test_colorstable_is_not_abstract():
    assert not inspect.isabstract(ColorsTable)


def test_colorstable_constructor_exists():
    assert callable(ColorsTable.__init__)


def test_colorstable_constructor_args():
    sig = inspect.signature(ColorsTable.__init__)
    params = list(sig.parameters.keys())



def test_documentsettingselt_is_not_abstract():
    assert not inspect.isabstract(DocumentSettingsElt)


def test_documentsettingselt_constructor_exists():
    assert callable(DocumentSettingsElt.__init__)


def test_documentsettingselt_constructor_args():
    sig = inspect.signature(DocumentSettingsElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::datetimetype_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::DateTimeType)


def test_datadiagrammlxform::datetimetype_constructor_exists():
    assert callable(DatadiagramMLXForm::DateTimeType.__init__)


def test_datadiagrammlxform::datetimetype_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::DateTimeType.__init__)
    params = list(sig.parameters.keys())
    assert "second" in params, "Missing parameter 'second'"
    assert "minute" in params, "Missing parameter 'minute'"
    assert "day" in params, "Missing parameter 'day'"
    assert "month" in params, "Missing parameter 'month'"
    assert "hour" in params, "Missing parameter 'hour'"
    assert "year" in params, "Missing parameter 'year'"

def test_datadiagrammlxform::datetimetype_has_second():
    assert hasattr(DatadiagramMLXForm::DateTimeType, "second")
    descriptor = None
    for klass in DatadiagramMLXForm::DateTimeType.__mro__:
        if "second" in klass.__dict__:
            descriptor = klass.__dict__["second"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::datetimetype_has_minute():
    assert hasattr(DatadiagramMLXForm::DateTimeType, "minute")
    descriptor = None
    for klass in DatadiagramMLXForm::DateTimeType.__mro__:
        if "minute" in klass.__dict__:
            descriptor = klass.__dict__["minute"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::datetimetype_has_day():
    assert hasattr(DatadiagramMLXForm::DateTimeType, "day")
    descriptor = None
    for klass in DatadiagramMLXForm::DateTimeType.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::datetimetype_has_month():
    assert hasattr(DatadiagramMLXForm::DateTimeType, "month")
    descriptor = None
    for klass in DatadiagramMLXForm::DateTimeType.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::datetimetype_has_hour():
    assert hasattr(DatadiagramMLXForm::DateTimeType, "hour")
    descriptor = None
    for klass in DatadiagramMLXForm::DateTimeType.__mro__:
        if "hour" in klass.__dict__:
            descriptor = klass.__dict__["hour"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::datetimetype_has_year():
    assert hasattr(DatadiagramMLXForm::DateTimeType, "year")
    descriptor = None
    for klass in DatadiagramMLXForm::DateTimeType.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlxform::solutionxml_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::SolutionXML)


def test_datadiagrammlxform::solutionxml_constructor_exists():
    assert callable(DatadiagramMLXForm::SolutionXML.__init__)


def test_datadiagrammlxform::solutionxml_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::SolutionXML.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::headerfooter_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::HeaderFooter)


def test_datadiagrammlxform::headerfooter_constructor_exists():
    assert callable(DatadiagramMLXForm::HeaderFooter.__init__)


def test_datadiagrammlxform::headerfooter_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::HeaderFooter.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::eventlist_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::EventList)


def test_datadiagrammlxform::eventlist_constructor_exists():
    assert callable(DatadiagramMLXForm::EventList.__init__)


def test_datadiagrammlxform::eventlist_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::EventList.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::windowsinfo_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::WindowsInfo)


def test_datadiagrammlxform::windowsinfo_constructor_exists():
    assert callable(DatadiagramMLXForm::WindowsInfo.__init__)


def test_datadiagrammlxform::windowsinfo_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::WindowsInfo.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::pageelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::PageElt)


def test_datadiagrammlxform::pageelt_constructor_exists():
    assert callable(DatadiagramMLXForm::PageElt.__init__)


def test_datadiagrammlxform::pageelt_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::PageElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::pagescollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::PagesCollection)


def test_datadiagrammlxform::pagescollection_constructor_exists():
    assert callable(DatadiagramMLXForm::PagesCollection.__init__)


def test_datadiagrammlxform::pagescollection_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::PagesCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::masterelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::MasterElt)


def test_datadiagrammlxform::masterelt_constructor_exists():
    assert callable(DatadiagramMLXForm::MasterElt.__init__)


def test_datadiagrammlxform::masterelt_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::MasterElt.__init__)
    params = list(sig.parameters.keys())



def test_connect_is_not_abstract():
    assert not inspect.isabstract(Connect)


def test_connect_constructor_exists():
    assert callable(Connect.__init__)


def test_connect_constructor_args():
    sig = inspect.signature(Connect.__init__)
    params = list(sig.parameters.keys())



def test_connectscollection_is_not_abstract():
    assert not inspect.isabstract(ConnectsCollection)


def test_connectscollection_constructor_exists():
    assert callable(ConnectsCollection.__init__)


def test_connectscollection_constructor_args():
    sig = inspect.signature(ConnectsCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::connect_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::Connect)


def test_datadiagrammlxform::connect_constructor_exists():
    assert callable(DatadiagramMLXForm::Connect.__init__)


def test_datadiagrammlxform::connect_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::Connect.__init__)
    params = list(sig.parameters.keys())
    assert "fromCell" in params, "Missing parameter 'fromCell'"
    assert "toSheet" in params, "Missing parameter 'toSheet'"
    assert "fromPart" in params, "Missing parameter 'fromPart'"
    assert "toCell" in params, "Missing parameter 'toCell'"
    assert "fromSheet" in params, "Missing parameter 'fromSheet'"
    assert "toPart" in params, "Missing parameter 'toPart'"

def test_datadiagrammlxform::connect_has_fromCell():
    assert hasattr(DatadiagramMLXForm::Connect, "fromCell")
    descriptor = None
    for klass in DatadiagramMLXForm::Connect.__mro__:
        if "fromCell" in klass.__dict__:
            descriptor = klass.__dict__["fromCell"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::connect_has_toSheet():
    assert hasattr(DatadiagramMLXForm::Connect, "toSheet")
    descriptor = None
    for klass in DatadiagramMLXForm::Connect.__mro__:
        if "toSheet" in klass.__dict__:
            descriptor = klass.__dict__["toSheet"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::connect_has_fromPart():
    assert hasattr(DatadiagramMLXForm::Connect, "fromPart")
    descriptor = None
    for klass in DatadiagramMLXForm::Connect.__mro__:
        if "fromPart" in klass.__dict__:
            descriptor = klass.__dict__["fromPart"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::connect_has_toCell():
    assert hasattr(DatadiagramMLXForm::Connect, "toCell")
    descriptor = None
    for klass in DatadiagramMLXForm::Connect.__mro__:
        if "toCell" in klass.__dict__:
            descriptor = klass.__dict__["toCell"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::connect_has_fromSheet():
    assert hasattr(DatadiagramMLXForm::Connect, "fromSheet")
    descriptor = None
    for klass in DatadiagramMLXForm::Connect.__mro__:
        if "fromSheet" in klass.__dict__:
            descriptor = klass.__dict__["fromSheet"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::connect_has_toPart():
    assert hasattr(DatadiagramMLXForm::Connect, "toPart")
    descriptor = None
    for klass in DatadiagramMLXForm::Connect.__mro__:
        if "toPart" in klass.__dict__:
            descriptor = klass.__dict__["toPart"]
            break
    assert isinstance(descriptor, property)



def test_mastershortcut_is_not_abstract():
    assert not inspect.isabstract(MasterShortCut)


def test_mastershortcut_constructor_exists():
    assert callable(MasterShortCut.__init__)


def test_mastershortcut_constructor_args():
    sig = inspect.signature(MasterShortCut.__init__)
    params = list(sig.parameters.keys())



def test_master_is_not_abstract():
    assert not inspect.isabstract(Master)


def test_master_constructor_exists():
    assert callable(Master.__init__)


def test_master_constructor_args():
    sig = inspect.signature(Master.__init__)
    params = list(sig.parameters.keys())



def test_icon_is_not_abstract():
    assert not inspect.isabstract(Icon)


def test_icon_constructor_exists():
    assert callable(Icon.__init__)


def test_icon_constructor_args():
    sig = inspect.signature(Icon.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::masterscollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::MastersCollection)


def test_datadiagrammlxform::masterscollection_constructor_exists():
    assert callable(DatadiagramMLXForm::MastersCollection.__init__)


def test_datadiagrammlxform::masterscollection_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::MastersCollection.__init__)
    params = list(sig.parameters.keys())



def test_tabscollection_is_not_abstract():
    assert not inspect.isabstract(TabsCollection)


def test_tabscollection_constructor_exists():
    assert callable(TabsCollection.__init__)


def test_tabscollection_constructor_args():
    sig = inspect.signature(TabsCollection.__init__)
    params = list(sig.parameters.keys())



def test_tab_is_not_abstract():
    assert not inspect.isabstract(Tab)


def test_tab_constructor_exists():
    assert callable(Tab.__init__)


def test_tab_constructor_args():
    sig = inspect.signature(Tab.__init__)
    params = list(sig.parameters.keys())



def test_textelt_is_not_abstract():
    assert not inspect.isabstract(TextElt)


def test_textelt_constructor_exists():
    assert callable(TextElt.__init__)


def test_textelt_constructor_args():
    sig = inspect.signature(TextElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::stringelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::StringElt)


def test_datadiagrammlxform::stringelt_constructor_exists():
    assert callable(DatadiagramMLXForm::StringElt.__init__)


def test_datadiagrammlxform::stringelt_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::StringElt.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_datadiagrammlxform::stringelt_has_value():
    assert hasattr(DatadiagramMLXForm::StringElt, "value")
    descriptor = None
    for klass in DatadiagramMLXForm::StringElt.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_xyabcdeelt_is_not_abstract():
    assert not inspect.isabstract(XYABCDEElt)


def test_xyabcdeelt_constructor_exists():
    assert callable(XYABCDEElt.__init__)


def test_xyabcdeelt_constructor_args():
    sig = inspect.signature(XYABCDEElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::nurbsto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::NURBSTo)


def test_datadiagrammlxform::nurbsto_constructor_exists():
    assert callable(DatadiagramMLXForm::NURBSTo.__init__)


def test_datadiagrammlxform::nurbsto_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::NURBSTo.__init__)
    params = list(sig.parameters.keys())



def test_xyabcdelt_is_not_abstract():
    assert not inspect.isabstract(XYABCDElt)


def test_xyabcdelt_constructor_exists():
    assert callable(XYABCDElt.__init__)


def test_xyabcdelt_constructor_args():
    sig = inspect.signature(XYABCDElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::ellipticalarcto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::EllipticalArcTo)


def test_datadiagrammlxform::ellipticalarcto_constructor_exists():
    assert callable(DatadiagramMLXForm::EllipticalArcTo.__init__)


def test_datadiagrammlxform::ellipticalarcto_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::EllipticalArcTo.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::xyabcdeelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::XYABCDEElt)


def test_datadiagrammlxform::xyabcdeelt_constructor_exists():
    assert callable(DatadiagramMLXForm::XYABCDEElt.__init__)


def test_datadiagrammlxform::xyabcdeelt_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::XYABCDEElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::splinestart_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::SplineStart)


def test_datadiagrammlxform::splinestart_constructor_exists():
    assert callable(DatadiagramMLXForm::SplineStart.__init__)


def test_datadiagrammlxform::splinestart_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::SplineStart.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::ellipse_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::Ellipse)


def test_datadiagrammlxform::ellipse_constructor_exists():
    assert callable(DatadiagramMLXForm::Ellipse.__init__)


def test_datadiagrammlxform::ellipse_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::Ellipse.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::ixrequiredelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::IXrequiredElt)


def test_datadiagrammlxform::ixrequiredelt_constructor_exists():
    assert callable(DatadiagramMLXForm::IXrequiredElt.__init__)


def test_datadiagrammlxform::ixrequiredelt_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::IXrequiredElt.__init__)
    params = list(sig.parameters.keys())
    assert "iX" in params, "Missing parameter 'iX'"

def test_datadiagrammlxform::ixrequiredelt_has_iX():
    assert hasattr(DatadiagramMLXForm::IXrequiredElt, "iX")
    descriptor = None
    for klass in DatadiagramMLXForm::IXrequiredElt.__mro__:
        if "iX" in klass.__dict__:
            descriptor = klass.__dict__["iX"]
            break
    assert isinstance(descriptor, property)



def test_text_is_not_abstract():
    assert not inspect.isabstract(Text)


def test_text_constructor_exists():
    assert callable(Text.__init__)


def test_text_constructor_args():
    sig = inspect.signature(Text.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::textelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::TextElt)


def test_datadiagrammlxform::textelt_constructor_exists():
    assert callable(DatadiagramMLXForm::TextElt.__init__)


def test_datadiagrammlxform::textelt_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::TextElt.__init__)
    params = list(sig.parameters.keys())



def test_geom_is_not_abstract():
    assert not inspect.isabstract(Geom)


def test_geom_constructor_exists():
    assert callable(Geom.__init__)


def test_geom_constructor_args():
    sig = inspect.signature(Geom.__init__)
    params = list(sig.parameters.keys())



def test_xyelt_is_not_abstract():
    assert not inspect.isabstract(XYElt)


def test_xyelt_constructor_exists():
    assert callable(XYElt.__init__)


def test_xyelt_constructor_args():
    sig = inspect.signature(XYElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::lineto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::LineTo)


def test_datadiagrammlxform::lineto_constructor_exists():
    assert callable(DatadiagramMLXForm::LineTo.__init__)


def test_datadiagrammlxform::lineto_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::LineTo.__init__)
    params = list(sig.parameters.keys())



def test_xyabelt_is_not_abstract():
    assert not inspect.isabstract(XYABElt)


def test_xyabelt_constructor_exists():
    assert callable(XYABElt.__init__)


def test_xyabelt_constructor_args():
    sig = inspect.signature(XYABElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::xyabcdelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::XYABCDElt)


def test_datadiagrammlxform::xyabcdelt_constructor_exists():
    assert callable(DatadiagramMLXForm::XYABCDElt.__init__)


def test_datadiagrammlxform::xyabcdelt_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::XYABCDElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::infiniteline_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::InfiniteLine)


def test_datadiagrammlxform::infiniteline_constructor_exists():
    assert callable(DatadiagramMLXForm::InfiniteLine.__init__)


def test_datadiagrammlxform::infiniteline_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::InfiniteLine.__init__)
    params = list(sig.parameters.keys())



def test_xyaelt_is_not_abstract():
    assert not inspect.isabstract(XYAElt)


def test_xyaelt_constructor_exists():
    assert callable(XYAElt.__init__)


def test_xyaelt_constructor_args():
    sig = inspect.signature(XYAElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::splineknot_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::SplineKnot)


def test_datadiagrammlxform::splineknot_constructor_exists():
    assert callable(DatadiagramMLXForm::SplineKnot.__init__)


def test_datadiagrammlxform::splineknot_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::SplineKnot.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::polylineto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::PolylineTo)


def test_datadiagrammlxform::polylineto_constructor_exists():
    assert callable(DatadiagramMLXForm::PolylineTo.__init__)


def test_datadiagrammlxform::polylineto_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::PolylineTo.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::xyabelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::XYABElt)


def test_datadiagrammlxform::xyabelt_constructor_exists():
    assert callable(DatadiagramMLXForm::XYABElt.__init__)


def test_datadiagrammlxform::xyabelt_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::XYABElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::arcto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::ArcTo)


def test_datadiagrammlxform::arcto_constructor_exists():
    assert callable(DatadiagramMLXForm::ArcTo.__init__)


def test_datadiagrammlxform::arcto_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::ArcTo.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::xyaelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::XYAElt)


def test_datadiagrammlxform::xyaelt_constructor_exists():
    assert callable(DatadiagramMLXForm::XYAElt.__init__)


def test_datadiagrammlxform::xyaelt_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::XYAElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::moveto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::MoveTo)


def test_datadiagrammlxform::moveto_constructor_exists():
    assert callable(DatadiagramMLXForm::MoveTo.__init__)


def test_datadiagrammlxform::moveto_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::MoveTo.__init__)
    params = list(sig.parameters.keys())



def test_celltype_is_not_abstract():
    assert not inspect.isabstract(CellType)


def test_celltype_constructor_exists():
    assert callable(CellType.__init__)


def test_celltype_constructor_args():
    sig = inspect.signature(CellType.__init__)
    params = list(sig.parameters.keys())



def test_nurbsto_is_not_abstract():
    assert not inspect.isabstract(NURBSTo)


def test_nurbsto_constructor_exists():
    assert callable(NURBSTo.__init__)


def test_nurbsto_constructor_args():
    sig = inspect.signature(NURBSTo.__init__)
    params = list(sig.parameters.keys())



def test_splinestart_is_not_abstract():
    assert not inspect.isabstract(SplineStart)


def test_splinestart_constructor_exists():
    assert callable(SplineStart.__init__)


def test_splinestart_constructor_args():
    sig = inspect.signature(SplineStart.__init__)
    params = list(sig.parameters.keys())



def test_ellipticalarcto_is_not_abstract():
    assert not inspect.isabstract(EllipticalArcTo)


def test_ellipticalarcto_constructor_exists():
    assert callable(EllipticalArcTo.__init__)


def test_ellipticalarcto_constructor_args():
    sig = inspect.signature(EllipticalArcTo.__init__)
    params = list(sig.parameters.keys())



def test_ellipse_is_not_abstract():
    assert not inspect.isabstract(Ellipse)


def test_ellipse_constructor_exists():
    assert callable(Ellipse.__init__)


def test_ellipse_constructor_args():
    sig = inspect.signature(Ellipse.__init__)
    params = list(sig.parameters.keys())



def test_infiniteline_is_not_abstract():
    assert not inspect.isabstract(InfiniteLine)


def test_infiniteline_constructor_exists():
    assert callable(InfiniteLine.__init__)


def test_infiniteline_constructor_args():
    sig = inspect.signature(InfiniteLine.__init__)
    params = list(sig.parameters.keys())



def test_polylineto_is_not_abstract():
    assert not inspect.isabstract(PolylineTo)


def test_polylineto_constructor_exists():
    assert callable(PolylineTo.__init__)


def test_polylineto_constructor_args():
    sig = inspect.signature(PolylineTo.__init__)
    params = list(sig.parameters.keys())



def test_splineknot_is_not_abstract():
    assert not inspect.isabstract(SplineKnot)


def test_splineknot_constructor_exists():
    assert callable(SplineKnot.__init__)


def test_splineknot_constructor_args():
    sig = inspect.signature(SplineKnot.__init__)
    params = list(sig.parameters.keys())



def test_arcto_is_not_abstract():
    assert not inspect.isabstract(ArcTo)


def test_arcto_constructor_exists():
    assert callable(ArcTo.__init__)


def test_arcto_constructor_args():
    sig = inspect.signature(ArcTo.__init__)
    params = list(sig.parameters.keys())



def test_moveto_is_not_abstract():
    assert not inspect.isabstract(MoveTo)


def test_moveto_constructor_exists():
    assert callable(MoveTo.__init__)


def test_moveto_constructor_args():
    sig = inspect.signature(MoveTo.__init__)
    params = list(sig.parameters.keys())



def test_lineto_is_not_abstract():
    assert not inspect.isabstract(LineTo)


def test_lineto_constructor_exists():
    assert callable(LineTo.__init__)


def test_lineto_constructor_args():
    sig = inspect.signature(LineTo.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::identifiedelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::IdentifiedElt)


def test_datadiagrammlxform::identifiedelt_constructor_exists():
    assert callable(DatadiagramMLXForm::IdentifiedElt.__init__)


def test_datadiagrammlxform::identifiedelt_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::IdentifiedElt.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"

def test_datadiagrammlxform::identifiedelt_has_ID():
    assert hasattr(DatadiagramMLXForm::IdentifiedElt, "ID")
    descriptor = None
    for klass in DatadiagramMLXForm::IdentifiedElt.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlxform::namedelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::NamedElt)


def test_datadiagrammlxform::namedelt_constructor_exists():
    assert callable(DatadiagramMLXForm::NamedElt.__init__)


def test_datadiagrammlxform::namedelt_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::NamedElt.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "nameU" in params, "Missing parameter 'nameU'"

def test_datadiagrammlxform::namedelt_has_name():
    assert hasattr(DatadiagramMLXForm::NamedElt, "name")
    descriptor = None
    for klass in DatadiagramMLXForm::NamedElt.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::namedelt_has_nameU():
    assert hasattr(DatadiagramMLXForm::NamedElt, "nameU")
    descriptor = None
    for klass in DatadiagramMLXForm::NamedElt.__mro__:
        if "nameU" in klass.__dict__:
            descriptor = klass.__dict__["nameU"]
            break
    assert isinstance(descriptor, property)



def test_pageelt_is_not_abstract():
    assert not inspect.isabstract(PageElt)


def test_pageelt_constructor_exists():
    assert callable(PageElt.__init__)


def test_pageelt_constructor_args():
    sig = inspect.signature(PageElt.__init__)
    params = list(sig.parameters.keys())



def test_masterelt_is_not_abstract():
    assert not inspect.isabstract(MasterElt)


def test_masterelt_constructor_exists():
    assert callable(MasterElt.__init__)


def test_masterelt_constructor_args():
    sig = inspect.signature(MasterElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::icon_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::Icon)


def test_datadiagrammlxform::icon_constructor_exists():
    assert callable(DatadiagramMLXForm::Icon.__init__)


def test_datadiagrammlxform::icon_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::Icon.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_datadiagrammlxform::icon_has_value():
    assert hasattr(DatadiagramMLXForm::Icon, "value")
    descriptor = None
    for klass in DatadiagramMLXForm::Icon.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlxform::shapescollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::ShapesCollection)


def test_datadiagrammlxform::shapescollection_constructor_exists():
    assert callable(DatadiagramMLXForm::ShapesCollection.__init__)


def test_datadiagrammlxform::shapescollection_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::ShapesCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::connectscollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::ConnectsCollection)


def test_datadiagrammlxform::connectscollection_constructor_exists():
    assert callable(DatadiagramMLXForm::ConnectsCollection.__init__)


def test_datadiagrammlxform::connectscollection_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::ConnectsCollection.__init__)
    params = list(sig.parameters.keys())



def test_uniqueidelt_is_not_abstract():
    assert not inspect.isabstract(UniqueIdElt)


def test_uniqueidelt_constructor_exists():
    assert callable(UniqueIdElt.__init__)


def test_uniqueidelt_constructor_args():
    sig = inspect.signature(UniqueIdElt.__init__)
    params = list(sig.parameters.keys())



def test_delelt_is_not_abstract():
    assert not inspect.isabstract(DelElt)


def test_delelt_constructor_exists():
    assert callable(DelElt.__init__)


def test_delelt_constructor_args():
    sig = inspect.signature(DelElt.__init__)
    params = list(sig.parameters.keys())



def test_ixelt_is_not_abstract():
    assert not inspect.isabstract(IXElt)


def test_ixelt_constructor_exists():
    assert callable(IXElt.__init__)


def test_ixelt_constructor_args():
    sig = inspect.signature(IXElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::tab_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::Tab)


def test_datadiagrammlxform::tab_constructor_exists():
    assert callable(DatadiagramMLXForm::Tab.__init__)


def test_datadiagrammlxform::tab_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::Tab.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::xyelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::XYElt)


def test_datadiagrammlxform::xyelt_constructor_exists():
    assert callable(DatadiagramMLXForm::XYElt.__init__)


def test_datadiagrammlxform::xyelt_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::XYElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::delelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::DelElt)


def test_datadiagrammlxform::delelt_constructor_exists():
    assert callable(DatadiagramMLXForm::DelElt.__init__)


def test_datadiagrammlxform::delelt_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::DelElt.__init__)
    params = list(sig.parameters.keys())
    assert "del_" in params, "Missing parameter 'del_'"

def test_datadiagrammlxform::delelt_has_del_():
    assert hasattr(DatadiagramMLXForm::DelElt, "del_")
    descriptor = None
    for klass in DatadiagramMLXForm::DelElt.__mro__:
        if "del_" in klass.__dict__:
            descriptor = klass.__dict__["del_"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlxform::ixelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::IXElt)


def test_datadiagrammlxform::ixelt_constructor_exists():
    assert callable(DatadiagramMLXForm::IXElt.__init__)


def test_datadiagrammlxform::ixelt_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::IXElt.__init__)
    params = list(sig.parameters.keys())
    assert "iX" in params, "Missing parameter 'iX'"

def test_datadiagrammlxform::ixelt_has_iX():
    assert hasattr(DatadiagramMLXForm::IXElt, "iX")
    descriptor = None
    for klass in DatadiagramMLXForm::IXElt.__mro__:
        if "iX" in klass.__dict__:
            descriptor = klass.__dict__["iX"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlxform::shapeelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::ShapeElt)


def test_datadiagrammlxform::shapeelt_constructor_exists():
    assert callable(DatadiagramMLXForm::ShapeElt.__init__)


def test_datadiagrammlxform::shapeelt_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::ShapeElt.__init__)
    params = list(sig.parameters.keys())



def test_shapeelt_is_not_abstract():
    assert not inspect.isabstract(ShapeElt)


def test_shapeelt_constructor_exists():
    assert callable(ShapeElt.__init__)


def test_shapeelt_constructor_args():
    sig = inspect.signature(ShapeElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::xform_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::XForm)


def test_datadiagrammlxform::xform_constructor_exists():
    assert callable(DatadiagramMLXForm::XForm.__init__)


def test_datadiagrammlxform::xform_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::XForm.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::field_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::Field)


def test_datadiagrammlxform::field_constructor_exists():
    assert callable(DatadiagramMLXForm::Field.__init__)


def test_datadiagrammlxform::field_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::Field.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::char_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::Char)


def test_datadiagrammlxform::char_constructor_exists():
    assert callable(DatadiagramMLXForm::Char.__init__)


def test_datadiagrammlxform::char_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::Char.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::text_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::Text)


def test_datadiagrammlxform::text_constructor_exists():
    assert callable(DatadiagramMLXForm::Text.__init__)


def test_datadiagrammlxform::text_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::Text.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::tabscollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::TabsCollection)


def test_datadiagrammlxform::tabscollection_constructor_exists():
    assert callable(DatadiagramMLXForm::TabsCollection.__init__)


def test_datadiagrammlxform::tabscollection_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::TabsCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::para_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::Para)


def test_datadiagrammlxform::para_constructor_exists():
    assert callable(DatadiagramMLXForm::Para.__init__)


def test_datadiagrammlxform::para_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::Para.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::geom_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::Geom)


def test_datadiagrammlxform::geom_constructor_exists():
    assert callable(DatadiagramMLXForm::Geom.__init__)


def test_datadiagrammlxform::geom_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::Geom.__init__)
    params = list(sig.parameters.keys())



def test_shapescollection_is_not_abstract():
    assert not inspect.isabstract(ShapesCollection)


def test_shapescollection_constructor_exists():
    assert callable(ShapesCollection.__init__)


def test_shapescollection_constructor_args():
    sig = inspect.signature(ShapesCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::shape_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::Shape)


def test_datadiagrammlxform::shape_constructor_exists():
    assert callable(DatadiagramMLXForm::Shape.__init__)


def test_datadiagrammlxform::shape_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::Shape.__init__)
    params = list(sig.parameters.keys())
    assert "lineStyle" in params, "Missing parameter 'lineStyle'"
    assert "fillStyle" in params, "Missing parameter 'fillStyle'"
    assert "textStyle" in params, "Missing parameter 'textStyle'"

def test_datadiagrammlxform::shape_has_lineStyle():
    assert hasattr(DatadiagramMLXForm::Shape, "lineStyle")
    descriptor = None
    for klass in DatadiagramMLXForm::Shape.__mro__:
        if "lineStyle" in klass.__dict__:
            descriptor = klass.__dict__["lineStyle"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::shape_has_fillStyle():
    assert hasattr(DatadiagramMLXForm::Shape, "fillStyle")
    descriptor = None
    for klass in DatadiagramMLXForm::Shape.__mro__:
        if "fillStyle" in klass.__dict__:
            descriptor = klass.__dict__["fillStyle"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::shape_has_textStyle():
    assert hasattr(DatadiagramMLXForm::Shape, "textStyle")
    descriptor = None
    for klass in DatadiagramMLXForm::Shape.__mro__:
        if "textStyle" in klass.__dict__:
            descriptor = klass.__dict__["textStyle"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlxform::uniqueidelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::UniqueIdElt)


def test_datadiagrammlxform::uniqueidelt_constructor_exists():
    assert callable(DatadiagramMLXForm::UniqueIdElt.__init__)


def test_datadiagrammlxform::uniqueidelt_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::UniqueIdElt.__init__)
    params = list(sig.parameters.keys())
    assert "UniqueID" in params, "Missing parameter 'UniqueID'"

def test_datadiagrammlxform::uniqueidelt_has_UniqueID():
    assert hasattr(DatadiagramMLXForm::UniqueIdElt, "UniqueID")
    descriptor = None
    for klass in DatadiagramMLXForm::UniqueIdElt.__mro__:
        if "UniqueID" in klass.__dict__:
            descriptor = klass.__dict__["UniqueID"]
            break
    assert isinstance(descriptor, property)



def test_pagesheet_is_not_abstract():
    assert not inspect.isabstract(PageSheet)


def test_pagesheet_constructor_exists():
    assert callable(PageSheet.__init__)


def test_pagesheet_constructor_args():
    sig = inspect.signature(PageSheet.__init__)
    params = list(sig.parameters.keys())



def test_namedelt_is_not_abstract():
    assert not inspect.isabstract(NamedElt)


def test_namedelt_constructor_exists():
    assert callable(NamedElt.__init__)


def test_namedelt_constructor_args():
    sig = inspect.signature(NamedElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::documentsheet_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::DocumentSheet)


def test_datadiagrammlxform::documentsheet_constructor_exists():
    assert callable(DatadiagramMLXForm::DocumentSheet.__init__)


def test_datadiagrammlxform::documentsheet_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::DocumentSheet.__init__)
    params = list(sig.parameters.keys())



def test_shape_is_not_abstract():
    assert not inspect.isabstract(Shape)


def test_shape_constructor_exists():
    assert callable(Shape.__init__)


def test_shape_constructor_args():
    sig = inspect.signature(Shape.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::pagesheet_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::PageSheet)


def test_datadiagrammlxform::pagesheet_constructor_exists():
    assert callable(DatadiagramMLXForm::PageSheet.__init__)


def test_datadiagrammlxform::pagesheet_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::PageSheet.__init__)
    params = list(sig.parameters.keys())



def test_facename_is_not_abstract():
    assert not inspect.isabstract(FaceName)


def test_facename_constructor_exists():
    assert callable(FaceName.__init__)


def test_facename_constructor_args():
    sig = inspect.signature(FaceName.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::facenamestable_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::FaceNamesTable)


def test_datadiagrammlxform::facenamestable_constructor_exists():
    assert callable(DatadiagramMLXForm::FaceNamesTable.__init__)


def test_datadiagrammlxform::facenamestable_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::FaceNamesTable.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::stylesheetscollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::StyleSheetsCollection)


def test_datadiagrammlxform::stylesheetscollection_constructor_exists():
    assert callable(DatadiagramMLXForm::StyleSheetsCollection.__init__)


def test_datadiagrammlxform::stylesheetscollection_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::StyleSheetsCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::emailroutingdata_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::EmailRoutingData)


def test_datadiagrammlxform::emailroutingdata_constructor_exists():
    assert callable(DatadiagramMLXForm::EmailRoutingData.__init__)


def test_datadiagrammlxform::emailroutingdata_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::EmailRoutingData.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "data" in params, "Missing parameter 'data'"

def test_datadiagrammlxform::emailroutingdata_has_size():
    assert hasattr(DatadiagramMLXForm::EmailRoutingData, "size")
    descriptor = None
    for klass in DatadiagramMLXForm::EmailRoutingData.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::emailroutingdata_has_data():
    assert hasattr(DatadiagramMLXForm::EmailRoutingData, "data")
    descriptor = None
    for klass in DatadiagramMLXForm::EmailRoutingData.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlxform::vbprojectdata_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::VBProjectData)


def test_datadiagrammlxform::vbprojectdata_constructor_exists():
    assert callable(DatadiagramMLXForm::VBProjectData.__init__)


def test_datadiagrammlxform::vbprojectdata_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::VBProjectData.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"

def test_datadiagrammlxform::vbprojectdata_has_data():
    assert hasattr(DatadiagramMLXForm::VBProjectData, "data")
    descriptor = None
    for klass in DatadiagramMLXForm::VBProjectData.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)



def test_identifiedelt_is_not_abstract():
    assert not inspect.isabstract(IdentifiedElt)


def test_identifiedelt_constructor_exists():
    assert callable(IdentifiedElt.__init__)


def test_identifiedelt_constructor_args():
    sig = inspect.signature(IdentifiedElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::mastershortcut_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::MasterShortCut)


def test_datadiagrammlxform::mastershortcut_constructor_exists():
    assert callable(DatadiagramMLXForm::MasterShortCut.__init__)


def test_datadiagrammlxform::mastershortcut_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::MasterShortCut.__init__)
    params = list(sig.parameters.keys())
    assert "shortcutHelp" in params, "Missing parameter 'shortcutHelp'"
    assert "patternFlags" in params, "Missing parameter 'patternFlags'"
    assert "iconSize" in params, "Missing parameter 'iconSize'"
    assert "prompt" in params, "Missing parameter 'prompt'"
    assert "shortcutURL" in params, "Missing parameter 'shortcutURL'"
    assert "alignName" in params, "Missing parameter 'alignName'"

def test_datadiagrammlxform::mastershortcut_has_shortcutHelp():
    assert hasattr(DatadiagramMLXForm::MasterShortCut, "shortcutHelp")
    descriptor = None
    for klass in DatadiagramMLXForm::MasterShortCut.__mro__:
        if "shortcutHelp" in klass.__dict__:
            descriptor = klass.__dict__["shortcutHelp"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::mastershortcut_has_patternFlags():
    assert hasattr(DatadiagramMLXForm::MasterShortCut, "patternFlags")
    descriptor = None
    for klass in DatadiagramMLXForm::MasterShortCut.__mro__:
        if "patternFlags" in klass.__dict__:
            descriptor = klass.__dict__["patternFlags"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::mastershortcut_has_iconSize():
    assert hasattr(DatadiagramMLXForm::MasterShortCut, "iconSize")
    descriptor = None
    for klass in DatadiagramMLXForm::MasterShortCut.__mro__:
        if "iconSize" in klass.__dict__:
            descriptor = klass.__dict__["iconSize"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::mastershortcut_has_prompt():
    assert hasattr(DatadiagramMLXForm::MasterShortCut, "prompt")
    descriptor = None
    for klass in DatadiagramMLXForm::MasterShortCut.__mro__:
        if "prompt" in klass.__dict__:
            descriptor = klass.__dict__["prompt"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::mastershortcut_has_shortcutURL():
    assert hasattr(DatadiagramMLXForm::MasterShortCut, "shortcutURL")
    descriptor = None
    for klass in DatadiagramMLXForm::MasterShortCut.__mro__:
        if "shortcutURL" in klass.__dict__:
            descriptor = klass.__dict__["shortcutURL"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::mastershortcut_has_alignName():
    assert hasattr(DatadiagramMLXForm::MasterShortCut, "alignName")
    descriptor = None
    for klass in DatadiagramMLXForm::MasterShortCut.__mro__:
        if "alignName" in klass.__dict__:
            descriptor = klass.__dict__["alignName"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlxform::facename_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::FaceName)


def test_datadiagrammlxform::facename_constructor_exists():
    assert callable(DatadiagramMLXForm::FaceName.__init__)


def test_datadiagrammlxform::facename_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::FaceName.__init__)
    params = list(sig.parameters.keys())
    assert "charSet" in params, "Missing parameter 'charSet'"
    assert "panos" in params, "Missing parameter 'panos'"
    assert "name" in params, "Missing parameter 'name'"
    assert "unicodeRanges" in params, "Missing parameter 'unicodeRanges'"
    assert "flags" in params, "Missing parameter 'flags'"

def test_datadiagrammlxform::facename_has_charSet():
    assert hasattr(DatadiagramMLXForm::FaceName, "charSet")
    descriptor = None
    for klass in DatadiagramMLXForm::FaceName.__mro__:
        if "charSet" in klass.__dict__:
            descriptor = klass.__dict__["charSet"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::facename_has_panos():
    assert hasattr(DatadiagramMLXForm::FaceName, "panos")
    descriptor = None
    for klass in DatadiagramMLXForm::FaceName.__mro__:
        if "panos" in klass.__dict__:
            descriptor = klass.__dict__["panos"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::facename_has_name():
    assert hasattr(DatadiagramMLXForm::FaceName, "name")
    descriptor = None
    for klass in DatadiagramMLXForm::FaceName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::facename_has_unicodeRanges():
    assert hasattr(DatadiagramMLXForm::FaceName, "unicodeRanges")
    descriptor = None
    for klass in DatadiagramMLXForm::FaceName.__mro__:
        if "unicodeRanges" in klass.__dict__:
            descriptor = klass.__dict__["unicodeRanges"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::facename_has_flags():
    assert hasattr(DatadiagramMLXForm::FaceName, "flags")
    descriptor = None
    for klass in DatadiagramMLXForm::FaceName.__mro__:
        if "flags" in klass.__dict__:
            descriptor = klass.__dict__["flags"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlxform::stylesheet_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::StyleSheet)


def test_datadiagrammlxform::stylesheet_constructor_exists():
    assert callable(DatadiagramMLXForm::StyleSheet.__init__)


def test_datadiagrammlxform::stylesheet_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::StyleSheet.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::page_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::Page)


def test_datadiagrammlxform::page_constructor_exists():
    assert callable(DatadiagramMLXForm::Page.__init__)


def test_datadiagrammlxform::page_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::Page.__init__)
    params = list(sig.parameters.keys())
    assert "ViewCenterY" in params, "Missing parameter 'ViewCenterY'"
    assert "reviewerID" in params, "Missing parameter 'reviewerID'"
    assert "backPage" in params, "Missing parameter 'backPage'"
    assert "viewScale" in params, "Missing parameter 'viewScale'"
    assert "background" in params, "Missing parameter 'background'"
    assert "associatedPage" in params, "Missing parameter 'associatedPage'"
    assert "viewCenterX" in params, "Missing parameter 'viewCenterX'"

def test_datadiagrammlxform::page_has_ViewCenterY():
    assert hasattr(DatadiagramMLXForm::Page, "ViewCenterY")
    descriptor = None
    for klass in DatadiagramMLXForm::Page.__mro__:
        if "ViewCenterY" in klass.__dict__:
            descriptor = klass.__dict__["ViewCenterY"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::page_has_reviewerID():
    assert hasattr(DatadiagramMLXForm::Page, "reviewerID")
    descriptor = None
    for klass in DatadiagramMLXForm::Page.__mro__:
        if "reviewerID" in klass.__dict__:
            descriptor = klass.__dict__["reviewerID"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::page_has_backPage():
    assert hasattr(DatadiagramMLXForm::Page, "backPage")
    descriptor = None
    for klass in DatadiagramMLXForm::Page.__mro__:
        if "backPage" in klass.__dict__:
            descriptor = klass.__dict__["backPage"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::page_has_viewScale():
    assert hasattr(DatadiagramMLXForm::Page, "viewScale")
    descriptor = None
    for klass in DatadiagramMLXForm::Page.__mro__:
        if "viewScale" in klass.__dict__:
            descriptor = klass.__dict__["viewScale"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::page_has_background():
    assert hasattr(DatadiagramMLXForm::Page, "background")
    descriptor = None
    for klass in DatadiagramMLXForm::Page.__mro__:
        if "background" in klass.__dict__:
            descriptor = klass.__dict__["background"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::page_has_associatedPage():
    assert hasattr(DatadiagramMLXForm::Page, "associatedPage")
    descriptor = None
    for klass in DatadiagramMLXForm::Page.__mro__:
        if "associatedPage" in klass.__dict__:
            descriptor = klass.__dict__["associatedPage"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::page_has_viewCenterX():
    assert hasattr(DatadiagramMLXForm::Page, "viewCenterX")
    descriptor = None
    for klass in DatadiagramMLXForm::Page.__mro__:
        if "viewCenterX" in klass.__dict__:
            descriptor = klass.__dict__["viewCenterX"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlxform::master_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::Master)


def test_datadiagrammlxform::master_constructor_exists():
    assert callable(DatadiagramMLXForm::Master.__init__)


def test_datadiagrammlxform::master_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::Master.__init__)
    params = list(sig.parameters.keys())
    assert "prompt" in params, "Missing parameter 'prompt'"
    assert "matchByName" in params, "Missing parameter 'matchByName'"
    assert "patternFlags" in params, "Missing parameter 'patternFlags'"
    assert "baseID" in params, "Missing parameter 'baseID'"
    assert "hidden" in params, "Missing parameter 'hidden'"
    assert "iconSize" in params, "Missing parameter 'iconSize'"
    assert "iconUpdate" in params, "Missing parameter 'iconUpdate'"
    assert "alignName" in params, "Missing parameter 'alignName'"

def test_datadiagrammlxform::master_has_prompt():
    assert hasattr(DatadiagramMLXForm::Master, "prompt")
    descriptor = None
    for klass in DatadiagramMLXForm::Master.__mro__:
        if "prompt" in klass.__dict__:
            descriptor = klass.__dict__["prompt"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::master_has_matchByName():
    assert hasattr(DatadiagramMLXForm::Master, "matchByName")
    descriptor = None
    for klass in DatadiagramMLXForm::Master.__mro__:
        if "matchByName" in klass.__dict__:
            descriptor = klass.__dict__["matchByName"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::master_has_patternFlags():
    assert hasattr(DatadiagramMLXForm::Master, "patternFlags")
    descriptor = None
    for klass in DatadiagramMLXForm::Master.__mro__:
        if "patternFlags" in klass.__dict__:
            descriptor = klass.__dict__["patternFlags"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::master_has_baseID():
    assert hasattr(DatadiagramMLXForm::Master, "baseID")
    descriptor = None
    for klass in DatadiagramMLXForm::Master.__mro__:
        if "baseID" in klass.__dict__:
            descriptor = klass.__dict__["baseID"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::master_has_hidden():
    assert hasattr(DatadiagramMLXForm::Master, "hidden")
    descriptor = None
    for klass in DatadiagramMLXForm::Master.__mro__:
        if "hidden" in klass.__dict__:
            descriptor = klass.__dict__["hidden"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::master_has_iconSize():
    assert hasattr(DatadiagramMLXForm::Master, "iconSize")
    descriptor = None
    for klass in DatadiagramMLXForm::Master.__mro__:
        if "iconSize" in klass.__dict__:
            descriptor = klass.__dict__["iconSize"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::master_has_iconUpdate():
    assert hasattr(DatadiagramMLXForm::Master, "iconUpdate")
    descriptor = None
    for klass in DatadiagramMLXForm::Master.__mro__:
        if "iconUpdate" in klass.__dict__:
            descriptor = klass.__dict__["iconUpdate"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::master_has_alignName():
    assert hasattr(DatadiagramMLXForm::Master, "alignName")
    descriptor = None
    for klass in DatadiagramMLXForm::Master.__mro__:
        if "alignName" in klass.__dict__:
            descriptor = klass.__dict__["alignName"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlxform::fontentry_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::FontEntry)


def test_datadiagrammlxform::fontentry_constructor_exists():
    assert callable(DatadiagramMLXForm::FontEntry.__init__)


def test_datadiagrammlxform::fontentry_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::FontEntry.__init__)
    params = list(sig.parameters.keys())
    assert "attributes" in params, "Missing parameter 'attributes'"
    assert "name" in params, "Missing parameter 'name'"
    assert "unicode" in params, "Missing parameter 'unicode'"
    assert "charSet" in params, "Missing parameter 'charSet'"
    assert "pitchAndFamily" in params, "Missing parameter 'pitchAndFamily'"
    assert "weight" in params, "Missing parameter 'weight'"

def test_datadiagrammlxform::fontentry_has_attributes():
    assert hasattr(DatadiagramMLXForm::FontEntry, "attributes")
    descriptor = None
    for klass in DatadiagramMLXForm::FontEntry.__mro__:
        if "attributes" in klass.__dict__:
            descriptor = klass.__dict__["attributes"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::fontentry_has_name():
    assert hasattr(DatadiagramMLXForm::FontEntry, "name")
    descriptor = None
    for klass in DatadiagramMLXForm::FontEntry.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::fontentry_has_unicode():
    assert hasattr(DatadiagramMLXForm::FontEntry, "unicode")
    descriptor = None
    for klass in DatadiagramMLXForm::FontEntry.__mro__:
        if "unicode" in klass.__dict__:
            descriptor = klass.__dict__["unicode"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::fontentry_has_charSet():
    assert hasattr(DatadiagramMLXForm::FontEntry, "charSet")
    descriptor = None
    for klass in DatadiagramMLXForm::FontEntry.__mro__:
        if "charSet" in klass.__dict__:
            descriptor = klass.__dict__["charSet"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::fontentry_has_pitchAndFamily():
    assert hasattr(DatadiagramMLXForm::FontEntry, "pitchAndFamily")
    descriptor = None
    for klass in DatadiagramMLXForm::FontEntry.__mro__:
        if "pitchAndFamily" in klass.__dict__:
            descriptor = klass.__dict__["pitchAndFamily"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::fontentry_has_weight():
    assert hasattr(DatadiagramMLXForm::FontEntry, "weight")
    descriptor = None
    for klass in DatadiagramMLXForm::FontEntry.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_fontentry_is_not_abstract():
    assert not inspect.isabstract(FontEntry)


def test_fontentry_constructor_exists():
    assert callable(FontEntry.__init__)


def test_fontentry_constructor_args():
    sig = inspect.signature(FontEntry.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::fontstable_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::FontsTable)


def test_datadiagrammlxform::fontstable_constructor_exists():
    assert callable(DatadiagramMLXForm::FontsTable.__init__)


def test_datadiagrammlxform::fontstable_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::FontsTable.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::printsetup_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::PrintSetup)


def test_datadiagrammlxform::printsetup_constructor_exists():
    assert callable(DatadiagramMLXForm::PrintSetup.__init__)


def test_datadiagrammlxform::printsetup_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::PrintSetup.__init__)
    params = list(sig.parameters.keys())



def test_snapanglescollection_is_not_abstract():
    assert not inspect.isabstract(SnapAnglesCollection)


def test_snapanglescollection_constructor_exists():
    assert callable(SnapAnglesCollection.__init__)


def test_snapanglescollection_constructor_args():
    sig = inspect.signature(SnapAnglesCollection.__init__)
    params = list(sig.parameters.keys())



def test_ixrequiredelt_is_not_abstract():
    assert not inspect.isabstract(IXrequiredElt)


def test_ixrequiredelt_constructor_exists():
    assert callable(IXrequiredElt.__init__)


def test_ixrequiredelt_constructor_args():
    sig = inspect.signature(IXrequiredElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::pp_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::Pp)


def test_datadiagrammlxform::pp_constructor_exists():
    assert callable(DatadiagramMLXForm::Pp.__init__)


def test_datadiagrammlxform::pp_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::Pp.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::tp_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::Tp)


def test_datadiagrammlxform::tp_constructor_exists():
    assert callable(DatadiagramMLXForm::Tp.__init__)


def test_datadiagrammlxform::tp_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::Tp.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::fld_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::Fld)


def test_datadiagrammlxform::fld_constructor_exists():
    assert callable(DatadiagramMLXForm::Fld.__init__)


def test_datadiagrammlxform::fld_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::Fld.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::cp_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::Cp)


def test_datadiagrammlxform::cp_constructor_exists():
    assert callable(DatadiagramMLXForm::Cp.__init__)


def test_datadiagrammlxform::cp_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::Cp.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::colorentry_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::ColorEntry)


def test_datadiagrammlxform::colorentry_constructor_exists():
    assert callable(DatadiagramMLXForm::ColorEntry.__init__)


def test_datadiagrammlxform::colorentry_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::ColorEntry.__init__)
    params = list(sig.parameters.keys())
    assert "rgb" in params, "Missing parameter 'rgb'"

def test_datadiagrammlxform::colorentry_has_rgb():
    assert hasattr(DatadiagramMLXForm::ColorEntry, "rgb")
    descriptor = None
    for klass in DatadiagramMLXForm::ColorEntry.__mro__:
        if "rgb" in klass.__dict__:
            descriptor = klass.__dict__["rgb"]
            break
    assert isinstance(descriptor, property)



def test_colorentry_is_not_abstract():
    assert not inspect.isabstract(ColorEntry)


def test_colorentry_constructor_exists():
    assert callable(ColorEntry.__init__)


def test_colorentry_constructor_args():
    sig = inspect.signature(ColorEntry.__init__)
    params = list(sig.parameters.keys())



def test_stylesheet_is_not_abstract():
    assert not inspect.isabstract(StyleSheet)


def test_stylesheet_constructor_exists():
    assert callable(StyleSheet.__init__)


def test_stylesheet_constructor_args():
    sig = inspect.signature(StyleSheet.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::colorstable_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::ColorsTable)


def test_datadiagrammlxform::colorstable_constructor_exists():
    assert callable(DatadiagramMLXForm::ColorsTable.__init__)


def test_datadiagrammlxform::colorstable_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::ColorsTable.__init__)
    params = list(sig.parameters.keys())



def test_page_is_not_abstract():
    assert not inspect.isabstract(Page)


def test_page_constructor_exists():
    assert callable(Page.__init__)


def test_page_constructor_args():
    sig = inspect.signature(Page.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::snapangle_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::SnapAngle)


def test_datadiagrammlxform::snapangle_constructor_exists():
    assert callable(DatadiagramMLXForm::SnapAngle.__init__)


def test_datadiagrammlxform::snapangle_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::SnapAngle.__init__)
    params = list(sig.parameters.keys())
    assert "angleValue" in params, "Missing parameter 'angleValue'"

def test_datadiagrammlxform::snapangle_has_angleValue():
    assert hasattr(DatadiagramMLXForm::SnapAngle, "angleValue")
    descriptor = None
    for klass in DatadiagramMLXForm::SnapAngle.__mro__:
        if "angleValue" in klass.__dict__:
            descriptor = klass.__dict__["angleValue"]
            break
    assert isinstance(descriptor, property)



def test_snapangle_is_not_abstract():
    assert not inspect.isabstract(SnapAngle)


def test_snapangle_constructor_exists():
    assert callable(SnapAngle.__init__)


def test_snapangle_constructor_args():
    sig = inspect.signature(SnapAngle.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::snapanglescollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::SnapAnglesCollection)


def test_datadiagrammlxform::snapanglescollection_constructor_exists():
    assert callable(DatadiagramMLXForm::SnapAnglesCollection.__init__)


def test_datadiagrammlxform::snapanglescollection_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::SnapAnglesCollection.__init__)
    params = list(sig.parameters.keys())



def test_datetimetype_is_not_abstract():
    assert not inspect.isabstract(DateTimeType)


def test_datetimetype_constructor_exists():
    assert callable(DateTimeType.__init__)


def test_datetimetype_constructor_args():
    sig = inspect.signature(DateTimeType.__init__)
    params = list(sig.parameters.keys())



def test_custompropertiescollection_is_not_abstract():
    assert not inspect.isabstract(CustomPropertiesCollection)


def test_custompropertiescollection_constructor_exists():
    assert callable(CustomPropertiesCollection.__init__)


def test_custompropertiescollection_constructor_args():
    sig = inspect.signature(CustomPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform::documentsettingselt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::DocumentSettingsElt)


def test_datadiagrammlxform::documentsettingselt_constructor_exists():
    assert callable(DatadiagramMLXForm::DocumentSettingsElt.__init__)


def test_datadiagrammlxform::documentsettingselt_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::DocumentSettingsElt.__init__)
    params = list(sig.parameters.keys())
    assert "customMenusFile" in params, "Missing parameter 'customMenusFile'"
    assert "attachedToolbars" in params, "Missing parameter 'attachedToolbars'"
    assert "customToolbarsFile" in params, "Missing parameter 'customToolbarsFile'"
    assert "protectBkgnds" in params, "Missing parameter 'protectBkgnds'"
    assert "protectStyles" in params, "Missing parameter 'protectStyles'"
    assert "protectMasters" in params, "Missing parameter 'protectMasters'"
    assert "protectShapes" in params, "Missing parameter 'protectShapes'"
    assert "snapSettings" in params, "Missing parameter 'snapSettings'"
    assert "dynamicGridEnabled" in params, "Missing parameter 'dynamicGridEnabled'"
    assert "glueSettings" in params, "Missing parameter 'glueSettings'"
    assert "snapExtensions" in params, "Missing parameter 'snapExtensions'"

def test_datadiagrammlxform::documentsettingselt_has_customMenusFile():
    assert hasattr(DatadiagramMLXForm::DocumentSettingsElt, "customMenusFile")
    descriptor = None
    for klass in DatadiagramMLXForm::DocumentSettingsElt.__mro__:
        if "customMenusFile" in klass.__dict__:
            descriptor = klass.__dict__["customMenusFile"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::documentsettingselt_has_attachedToolbars():
    assert hasattr(DatadiagramMLXForm::DocumentSettingsElt, "attachedToolbars")
    descriptor = None
    for klass in DatadiagramMLXForm::DocumentSettingsElt.__mro__:
        if "attachedToolbars" in klass.__dict__:
            descriptor = klass.__dict__["attachedToolbars"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::documentsettingselt_has_customToolbarsFile():
    assert hasattr(DatadiagramMLXForm::DocumentSettingsElt, "customToolbarsFile")
    descriptor = None
    for klass in DatadiagramMLXForm::DocumentSettingsElt.__mro__:
        if "customToolbarsFile" in klass.__dict__:
            descriptor = klass.__dict__["customToolbarsFile"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::documentsettingselt_has_protectBkgnds():
    assert hasattr(DatadiagramMLXForm::DocumentSettingsElt, "protectBkgnds")
    descriptor = None
    for klass in DatadiagramMLXForm::DocumentSettingsElt.__mro__:
        if "protectBkgnds" in klass.__dict__:
            descriptor = klass.__dict__["protectBkgnds"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::documentsettingselt_has_protectStyles():
    assert hasattr(DatadiagramMLXForm::DocumentSettingsElt, "protectStyles")
    descriptor = None
    for klass in DatadiagramMLXForm::DocumentSettingsElt.__mro__:
        if "protectStyles" in klass.__dict__:
            descriptor = klass.__dict__["protectStyles"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::documentsettingselt_has_protectMasters():
    assert hasattr(DatadiagramMLXForm::DocumentSettingsElt, "protectMasters")
    descriptor = None
    for klass in DatadiagramMLXForm::DocumentSettingsElt.__mro__:
        if "protectMasters" in klass.__dict__:
            descriptor = klass.__dict__["protectMasters"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::documentsettingselt_has_protectShapes():
    assert hasattr(DatadiagramMLXForm::DocumentSettingsElt, "protectShapes")
    descriptor = None
    for klass in DatadiagramMLXForm::DocumentSettingsElt.__mro__:
        if "protectShapes" in klass.__dict__:
            descriptor = klass.__dict__["protectShapes"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::documentsettingselt_has_snapSettings():
    assert hasattr(DatadiagramMLXForm::DocumentSettingsElt, "snapSettings")
    descriptor = None
    for klass in DatadiagramMLXForm::DocumentSettingsElt.__mro__:
        if "snapSettings" in klass.__dict__:
            descriptor = klass.__dict__["snapSettings"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::documentsettingselt_has_dynamicGridEnabled():
    assert hasattr(DatadiagramMLXForm::DocumentSettingsElt, "dynamicGridEnabled")
    descriptor = None
    for klass in DatadiagramMLXForm::DocumentSettingsElt.__mro__:
        if "dynamicGridEnabled" in klass.__dict__:
            descriptor = klass.__dict__["dynamicGridEnabled"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::documentsettingselt_has_glueSettings():
    assert hasattr(DatadiagramMLXForm::DocumentSettingsElt, "glueSettings")
    descriptor = None
    for klass in DatadiagramMLXForm::DocumentSettingsElt.__mro__:
        if "glueSettings" in klass.__dict__:
            descriptor = klass.__dict__["glueSettings"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::documentsettingselt_has_snapExtensions():
    assert hasattr(DatadiagramMLXForm::DocumentSettingsElt, "snapExtensions")
    descriptor = None
    for klass in DatadiagramMLXForm::DocumentSettingsElt.__mro__:
        if "snapExtensions" in klass.__dict__:
            descriptor = klass.__dict__["snapExtensions"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlxform::customproperty_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm::CustomProperty)


def test_datadiagrammlxform::customproperty_constructor_exists():
    assert callable(DatadiagramMLXForm::CustomProperty.__init__)


def test_datadiagrammlxform::customproperty_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm::CustomProperty.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "dataType" in params, "Missing parameter 'dataType'"

def test_datadiagrammlxform::customproperty_has_name():
    assert hasattr(DatadiagramMLXForm::CustomProperty, "name")
    descriptor = None
    for klass in DatadiagramMLXForm::CustomProperty.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform::customproperty_has_dataType():
    assert hasattr(DatadiagramMLXForm::CustomProperty, "dataType")
    descriptor = None
    for klass in DatadiagramMLXForm::CustomProperty.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
            break
    assert isinstance(descriptor, property)



def test_customproperty_is_not_abstract():
    assert not inspect.isabstract(CustomProperty)


def test_customproperty_constructor_exists():
    assert callable(CustomProperty.__init__)


def test_customproperty_constructor_args():
    sig = inspect.signature(CustomProperty.__init__)
    params = list(sig.parameters.keys())


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
DatadiagramMLXForm::CustomPropertiesCollection_strategy = st.builds(
    DatadiagramMLXForm::CustomPropertiesCollection,
)
VBProjectData_strategy = st.builds(
    VBProjectData,
)
HeaderFooter_strategy = st.builds(
    HeaderFooter,
)
EventList_strategy = st.builds(
    EventList,
)
WindowsInfo_strategy = st.builds(
    WindowsInfo,
)
PagesCollection_strategy = st.builds(
    PagesCollection,
)
MastersCollection_strategy = st.builds(
    MastersCollection,
)
DocumentSheet_strategy = st.builds(
    DocumentSheet,
)
StyleSheetsCollection_strategy = st.builds(
    StyleSheetsCollection,
)
VisioDocument_strategy = st.builds(
    VisioDocument,
)
DatadiagramMLXForm::DocumentPropertiesCollection_strategy = st.builds(
    DatadiagramMLXForm::DocumentPropertiesCollection,
    category=
        safe_text,
    buildNumberEdited=
        safe_text,
    template=
        safe_text,
    hyperlinkBase_href=
        safe_text,
    alternateNames=
        safe_text,
    keywords=
        safe_text,
    subject=
        safe_text,
    creator=
        safe_text,
    title=
        safe_text,
    manager=
        safe_text,
    description=
        safe_text,
    buildNumberCreated=
        safe_text,
    company=
        safe_text
)
SolutionXML_strategy = st.builds(
    SolutionXML,
)
EmailRoutingData_strategy = st.builds(
    EmailRoutingData,
)
DocumentPropertiesCollection_strategy = st.builds(
    DocumentPropertiesCollection,
)
DatadiagramMLXForm::VisioDocument_strategy = st.builds(
    DatadiagramMLXForm::VisioDocument,
    docLangId=
        safe_text,
    key=
        safe_text,
    start=
        safe_text,
    buildnum=
        safe_text,
    version=
        safe_text,
    metric=
        safe_text
)
FaceNamesTable_strategy = st.builds(
    FaceNamesTable,
)
FontsTable_strategy = st.builds(
    FontsTable,
)
PrintSetup_strategy = st.builds(
    PrintSetup,
)
DatadiagramMLXForm::CellType_strategy = st.builds(
    DatadiagramMLXForm::CellType,
    err=
        safe_text,
    unit=
        safe_text,
    value=
        safe_text,
    formula=
        safe_text
)
ColorsTable_strategy = st.builds(
    ColorsTable,
)
DocumentSettingsElt_strategy = st.builds(
    DocumentSettingsElt,
)
DatadiagramMLXForm::DateTimeType_strategy = st.builds(
    DatadiagramMLXForm::DateTimeType,
    second=
        safe_text,
    minute=
        safe_text,
    day=
        safe_text,
    month=
        safe_text,
    hour=
        safe_text,
    year=
        safe_text
)
DatadiagramMLXForm::SolutionXML_strategy = st.builds(
    DatadiagramMLXForm::SolutionXML,
)
DatadiagramMLXForm::HeaderFooter_strategy = st.builds(
    DatadiagramMLXForm::HeaderFooter,
)
DatadiagramMLXForm::EventList_strategy = st.builds(
    DatadiagramMLXForm::EventList,
)
DatadiagramMLXForm::WindowsInfo_strategy = st.builds(
    DatadiagramMLXForm::WindowsInfo,
)
DatadiagramMLXForm::PageElt_strategy = st.builds(
    DatadiagramMLXForm::PageElt,
)
DatadiagramMLXForm::PagesCollection_strategy = st.builds(
    DatadiagramMLXForm::PagesCollection,
)
DatadiagramMLXForm::MasterElt_strategy = st.builds(
    DatadiagramMLXForm::MasterElt,
)
Connect_strategy = st.builds(
    Connect,
)
ConnectsCollection_strategy = st.builds(
    ConnectsCollection,
)
DatadiagramMLXForm::Connect_strategy = st.builds(
    DatadiagramMLXForm::Connect,
    fromCell=
        safe_text,
    toSheet=
        safe_text,
    fromPart=
        safe_text,
    toCell=
        safe_text,
    fromSheet=
        safe_text,
    toPart=
        safe_text
)
MasterShortCut_strategy = st.builds(
    MasterShortCut,
)
Master_strategy = st.builds(
    Master,
)
Icon_strategy = st.builds(
    Icon,
)
DatadiagramMLXForm::MastersCollection_strategy = st.builds(
    DatadiagramMLXForm::MastersCollection,
)
TabsCollection_strategy = st.builds(
    TabsCollection,
)
Tab_strategy = st.builds(
    Tab,
)
TextElt_strategy = st.builds(
    TextElt,
)
DatadiagramMLXForm::StringElt_strategy = st.builds(
    DatadiagramMLXForm::StringElt,
    value=
        safe_text
)
XYABCDEElt_strategy = st.builds(
    XYABCDEElt,
)
DatadiagramMLXForm::NURBSTo_strategy = st.builds(
    DatadiagramMLXForm::NURBSTo,
)
XYABCDElt_strategy = st.builds(
    XYABCDElt,
)
DatadiagramMLXForm::EllipticalArcTo_strategy = st.builds(
    DatadiagramMLXForm::EllipticalArcTo,
)
DatadiagramMLXForm::XYABCDEElt_strategy = st.builds(
    DatadiagramMLXForm::XYABCDEElt,
)
DatadiagramMLXForm::SplineStart_strategy = st.builds(
    DatadiagramMLXForm::SplineStart,
)
DatadiagramMLXForm::Ellipse_strategy = st.builds(
    DatadiagramMLXForm::Ellipse,
)
DatadiagramMLXForm::IXrequiredElt_strategy = st.builds(
    DatadiagramMLXForm::IXrequiredElt,
    iX=
        safe_text
)
Text_strategy = st.builds(
    Text,
)
DatadiagramMLXForm::TextElt_strategy = st.builds(
    DatadiagramMLXForm::TextElt,
)
Geom_strategy = st.builds(
    Geom,
)
XYElt_strategy = st.builds(
    XYElt,
)
DatadiagramMLXForm::LineTo_strategy = st.builds(
    DatadiagramMLXForm::LineTo,
)
XYABElt_strategy = st.builds(
    XYABElt,
)
DatadiagramMLXForm::XYABCDElt_strategy = st.builds(
    DatadiagramMLXForm::XYABCDElt,
)
DatadiagramMLXForm::InfiniteLine_strategy = st.builds(
    DatadiagramMLXForm::InfiniteLine,
)
XYAElt_strategy = st.builds(
    XYAElt,
)
DatadiagramMLXForm::SplineKnot_strategy = st.builds(
    DatadiagramMLXForm::SplineKnot,
)
DatadiagramMLXForm::PolylineTo_strategy = st.builds(
    DatadiagramMLXForm::PolylineTo,
)
DatadiagramMLXForm::XYABElt_strategy = st.builds(
    DatadiagramMLXForm::XYABElt,
)
DatadiagramMLXForm::ArcTo_strategy = st.builds(
    DatadiagramMLXForm::ArcTo,
)
DatadiagramMLXForm::XYAElt_strategy = st.builds(
    DatadiagramMLXForm::XYAElt,
)
DatadiagramMLXForm::MoveTo_strategy = st.builds(
    DatadiagramMLXForm::MoveTo,
)
CellType_strategy = st.builds(
    CellType,
)
NURBSTo_strategy = st.builds(
    NURBSTo,
)
SplineStart_strategy = st.builds(
    SplineStart,
)
EllipticalArcTo_strategy = st.builds(
    EllipticalArcTo,
)
Ellipse_strategy = st.builds(
    Ellipse,
)
InfiniteLine_strategy = st.builds(
    InfiniteLine,
)
PolylineTo_strategy = st.builds(
    PolylineTo,
)
SplineKnot_strategy = st.builds(
    SplineKnot,
)
ArcTo_strategy = st.builds(
    ArcTo,
)
MoveTo_strategy = st.builds(
    MoveTo,
)
LineTo_strategy = st.builds(
    LineTo,
)
DatadiagramMLXForm::IdentifiedElt_strategy = st.builds(
    DatadiagramMLXForm::IdentifiedElt,
    ID=
        safe_text
)
DatadiagramMLXForm::NamedElt_strategy = st.builds(
    DatadiagramMLXForm::NamedElt,
    name=
        safe_text,
    nameU=
        safe_text
)
PageElt_strategy = st.builds(
    PageElt,
)
MasterElt_strategy = st.builds(
    MasterElt,
)
DatadiagramMLXForm::Icon_strategy = st.builds(
    DatadiagramMLXForm::Icon,
    value=
        safe_text
)
DatadiagramMLXForm::ShapesCollection_strategy = st.builds(
    DatadiagramMLXForm::ShapesCollection,
)
DatadiagramMLXForm::ConnectsCollection_strategy = st.builds(
    DatadiagramMLXForm::ConnectsCollection,
)
UniqueIdElt_strategy = st.builds(
    UniqueIdElt,
)
DelElt_strategy = st.builds(
    DelElt,
)
IXElt_strategy = st.builds(
    IXElt,
)
DatadiagramMLXForm::Tab_strategy = st.builds(
    DatadiagramMLXForm::Tab,
)
DatadiagramMLXForm::XYElt_strategy = st.builds(
    DatadiagramMLXForm::XYElt,
)
DatadiagramMLXForm::DelElt_strategy = st.builds(
    DatadiagramMLXForm::DelElt,
    del_=
        safe_text
)
DatadiagramMLXForm::IXElt_strategy = st.builds(
    DatadiagramMLXForm::IXElt,
    iX=
        safe_text
)
DatadiagramMLXForm::ShapeElt_strategy = st.builds(
    DatadiagramMLXForm::ShapeElt,
)
ShapeElt_strategy = st.builds(
    ShapeElt,
)
DatadiagramMLXForm::XForm_strategy = st.builds(
    DatadiagramMLXForm::XForm,
)
DatadiagramMLXForm::Field_strategy = st.builds(
    DatadiagramMLXForm::Field,
)
DatadiagramMLXForm::Char_strategy = st.builds(
    DatadiagramMLXForm::Char,
)
DatadiagramMLXForm::Text_strategy = st.builds(
    DatadiagramMLXForm::Text,
)
DatadiagramMLXForm::TabsCollection_strategy = st.builds(
    DatadiagramMLXForm::TabsCollection,
)
DatadiagramMLXForm::Para_strategy = st.builds(
    DatadiagramMLXForm::Para,
)
DatadiagramMLXForm::Geom_strategy = st.builds(
    DatadiagramMLXForm::Geom,
)
ShapesCollection_strategy = st.builds(
    ShapesCollection,
)
DatadiagramMLXForm::Shape_strategy = st.builds(
    DatadiagramMLXForm::Shape,
    lineStyle=
        safe_text,
    fillStyle=
        safe_text,
    textStyle=
        safe_text
)
DatadiagramMLXForm::UniqueIdElt_strategy = st.builds(
    DatadiagramMLXForm::UniqueIdElt,
    UniqueID=
        safe_text
)
PageSheet_strategy = st.builds(
    PageSheet,
)
NamedElt_strategy = st.builds(
    NamedElt,
)
DatadiagramMLXForm::DocumentSheet_strategy = st.builds(
    DatadiagramMLXForm::DocumentSheet,
)
Shape_strategy = st.builds(
    Shape,
)
DatadiagramMLXForm::PageSheet_strategy = st.builds(
    DatadiagramMLXForm::PageSheet,
)
FaceName_strategy = st.builds(
    FaceName,
)
DatadiagramMLXForm::FaceNamesTable_strategy = st.builds(
    DatadiagramMLXForm::FaceNamesTable,
)
DatadiagramMLXForm::StyleSheetsCollection_strategy = st.builds(
    DatadiagramMLXForm::StyleSheetsCollection,
)
DatadiagramMLXForm::EmailRoutingData_strategy = st.builds(
    DatadiagramMLXForm::EmailRoutingData,
    size=
        safe_text,
    data=
        safe_text
)
DatadiagramMLXForm::VBProjectData_strategy = st.builds(
    DatadiagramMLXForm::VBProjectData,
    data=
        safe_text
)
IdentifiedElt_strategy = st.builds(
    IdentifiedElt,
)
DatadiagramMLXForm::MasterShortCut_strategy = st.builds(
    DatadiagramMLXForm::MasterShortCut,
    shortcutHelp=
        safe_text,
    patternFlags=
        safe_text,
    iconSize=
        safe_text,
    prompt=
        safe_text,
    shortcutURL=
        safe_text,
    alignName=
        safe_text
)
DatadiagramMLXForm::FaceName_strategy = st.builds(
    DatadiagramMLXForm::FaceName,
    charSet=
        safe_text,
    panos=
        safe_text,
    name=
        safe_text,
    unicodeRanges=
        safe_text,
    flags=
        safe_text
)
DatadiagramMLXForm::StyleSheet_strategy = st.builds(
    DatadiagramMLXForm::StyleSheet,
)
DatadiagramMLXForm::Page_strategy = st.builds(
    DatadiagramMLXForm::Page,
    ViewCenterY=
        safe_text,
    reviewerID=
        safe_text,
    backPage=
        safe_text,
    viewScale=
        safe_text,
    background=
        safe_text,
    associatedPage=
        safe_text,
    viewCenterX=
        safe_text
)
DatadiagramMLXForm::Master_strategy = st.builds(
    DatadiagramMLXForm::Master,
    prompt=
        safe_text,
    matchByName=
        safe_text,
    patternFlags=
        safe_text,
    baseID=
        safe_text,
    hidden=
        safe_text,
    iconSize=
        safe_text,
    iconUpdate=
        safe_text,
    alignName=
        safe_text
)
DatadiagramMLXForm::FontEntry_strategy = st.builds(
    DatadiagramMLXForm::FontEntry,
    attributes=
        safe_text,
    name=
        safe_text,
    unicode=
        safe_text,
    charSet=
        safe_text,
    pitchAndFamily=
        safe_text,
    weight=
        safe_text
)
FontEntry_strategy = st.builds(
    FontEntry,
)
DatadiagramMLXForm::FontsTable_strategy = st.builds(
    DatadiagramMLXForm::FontsTable,
)
DatadiagramMLXForm::PrintSetup_strategy = st.builds(
    DatadiagramMLXForm::PrintSetup,
)
SnapAnglesCollection_strategy = st.builds(
    SnapAnglesCollection,
)
IXrequiredElt_strategy = st.builds(
    IXrequiredElt,
)
DatadiagramMLXForm::Pp_strategy = st.builds(
    DatadiagramMLXForm::Pp,
)
DatadiagramMLXForm::Tp_strategy = st.builds(
    DatadiagramMLXForm::Tp,
)
DatadiagramMLXForm::Fld_strategy = st.builds(
    DatadiagramMLXForm::Fld,
)
DatadiagramMLXForm::Cp_strategy = st.builds(
    DatadiagramMLXForm::Cp,
)
DatadiagramMLXForm::ColorEntry_strategy = st.builds(
    DatadiagramMLXForm::ColorEntry,
    rgb=
        safe_text
)
ColorEntry_strategy = st.builds(
    ColorEntry,
)
StyleSheet_strategy = st.builds(
    StyleSheet,
)
DatadiagramMLXForm::ColorsTable_strategy = st.builds(
    DatadiagramMLXForm::ColorsTable,
)
Page_strategy = st.builds(
    Page,
)
DatadiagramMLXForm::SnapAngle_strategy = st.builds(
    DatadiagramMLXForm::SnapAngle,
    angleValue=
        safe_text
)
SnapAngle_strategy = st.builds(
    SnapAngle,
)
DatadiagramMLXForm::SnapAnglesCollection_strategy = st.builds(
    DatadiagramMLXForm::SnapAnglesCollection,
)
DateTimeType_strategy = st.builds(
    DateTimeType,
)
CustomPropertiesCollection_strategy = st.builds(
    CustomPropertiesCollection,
)
DatadiagramMLXForm::DocumentSettingsElt_strategy = st.builds(
    DatadiagramMLXForm::DocumentSettingsElt,
    customMenusFile=
        safe_text,
    attachedToolbars=
        safe_text,
    customToolbarsFile=
        safe_text,
    protectBkgnds=
        safe_text,
    protectStyles=
        safe_text,
    protectMasters=
        safe_text,
    protectShapes=
        safe_text,
    snapSettings=
        safe_text,
    dynamicGridEnabled=
        safe_text,
    glueSettings=
        safe_text,
    snapExtensions=
        safe_text
)
DatadiagramMLXForm::CustomProperty_strategy = st.builds(
    DatadiagramMLXForm::CustomProperty,
    name=
        safe_text,
    dataType=
        safe_text
)
CustomProperty_strategy = st.builds(
    CustomProperty,
)

@given(instance=DatadiagramMLXForm::CustomPropertiesCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::custompropertiescollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::CustomPropertiesCollection)

@given(instance=VBProjectData_strategy)
@settings(max_examples=50)
def test_vbprojectdata_instantiation(instance):
    assert isinstance(instance, VBProjectData)

@given(instance=HeaderFooter_strategy)
@settings(max_examples=50)
def test_headerfooter_instantiation(instance):
    assert isinstance(instance, HeaderFooter)

@given(instance=EventList_strategy)
@settings(max_examples=50)
def test_eventlist_instantiation(instance):
    assert isinstance(instance, EventList)

@given(instance=WindowsInfo_strategy)
@settings(max_examples=50)
def test_windowsinfo_instantiation(instance):
    assert isinstance(instance, WindowsInfo)

@given(instance=PagesCollection_strategy)
@settings(max_examples=50)
def test_pagescollection_instantiation(instance):
    assert isinstance(instance, PagesCollection)

@given(instance=MastersCollection_strategy)
@settings(max_examples=50)
def test_masterscollection_instantiation(instance):
    assert isinstance(instance, MastersCollection)

@given(instance=DocumentSheet_strategy)
@settings(max_examples=50)
def test_documentsheet_instantiation(instance):
    assert isinstance(instance, DocumentSheet)

@given(instance=StyleSheetsCollection_strategy)
@settings(max_examples=50)
def test_stylesheetscollection_instantiation(instance):
    assert isinstance(instance, StyleSheetsCollection)

@given(instance=VisioDocument_strategy)
@settings(max_examples=50)
def test_visiodocument_instantiation(instance):
    assert isinstance(instance, VisioDocument)

@given(instance=DatadiagramMLXForm::DocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::documentpropertiescollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::DocumentPropertiesCollection)

@given(instance=DatadiagramMLXForm::DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform::documentpropertiescollection_category_type(instance):
    assert isinstance(instance.category, str)


@given(instance=DatadiagramMLXForm::DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform::documentpropertiescollection_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=DatadiagramMLXForm::DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform::documentpropertiescollection_buildNumberEdited_type(instance):
    assert isinstance(instance.buildNumberEdited, str)


@given(instance=DatadiagramMLXForm::DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform::documentpropertiescollection_buildNumberEdited_setter(instance):
    original = instance.buildNumberEdited
    instance.buildNumberEdited = original
    assert instance.buildNumberEdited == original

@given(instance=DatadiagramMLXForm::DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform::documentpropertiescollection_template_type(instance):
    assert isinstance(instance.template, str)


@given(instance=DatadiagramMLXForm::DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform::documentpropertiescollection_template_setter(instance):
    original = instance.template
    instance.template = original
    assert instance.template == original

@given(instance=DatadiagramMLXForm::DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform::documentpropertiescollection_hyperlinkBase_href_type(instance):
    assert isinstance(instance.hyperlinkBase_href, str)


@given(instance=DatadiagramMLXForm::DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform::documentpropertiescollection_hyperlinkBase_href_setter(instance):
    original = instance.hyperlinkBase_href
    instance.hyperlinkBase_href = original
    assert instance.hyperlinkBase_href == original

@given(instance=DatadiagramMLXForm::DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform::documentpropertiescollection_alternateNames_type(instance):
    assert isinstance(instance.alternateNames, str)


@given(instance=DatadiagramMLXForm::DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform::documentpropertiescollection_alternateNames_setter(instance):
    original = instance.alternateNames
    instance.alternateNames = original
    assert instance.alternateNames == original

@given(instance=DatadiagramMLXForm::DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform::documentpropertiescollection_keywords_type(instance):
    assert isinstance(instance.keywords, str)


@given(instance=DatadiagramMLXForm::DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform::documentpropertiescollection_keywords_setter(instance):
    original = instance.keywords
    instance.keywords = original
    assert instance.keywords == original

@given(instance=DatadiagramMLXForm::DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform::documentpropertiescollection_subject_type(instance):
    assert isinstance(instance.subject, str)


@given(instance=DatadiagramMLXForm::DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform::documentpropertiescollection_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original

@given(instance=DatadiagramMLXForm::DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform::documentpropertiescollection_creator_type(instance):
    assert isinstance(instance.creator, str)


@given(instance=DatadiagramMLXForm::DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform::documentpropertiescollection_creator_setter(instance):
    original = instance.creator
    instance.creator = original
    assert instance.creator == original

@given(instance=DatadiagramMLXForm::DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform::documentpropertiescollection_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=DatadiagramMLXForm::DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform::documentpropertiescollection_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=DatadiagramMLXForm::DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform::documentpropertiescollection_manager_type(instance):
    assert isinstance(instance.manager, str)


@given(instance=DatadiagramMLXForm::DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform::documentpropertiescollection_manager_setter(instance):
    original = instance.manager
    instance.manager = original
    assert instance.manager == original

@given(instance=DatadiagramMLXForm::DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform::documentpropertiescollection_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=DatadiagramMLXForm::DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform::documentpropertiescollection_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=DatadiagramMLXForm::DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform::documentpropertiescollection_buildNumberCreated_type(instance):
    assert isinstance(instance.buildNumberCreated, str)


@given(instance=DatadiagramMLXForm::DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform::documentpropertiescollection_buildNumberCreated_setter(instance):
    original = instance.buildNumberCreated
    instance.buildNumberCreated = original
    assert instance.buildNumberCreated == original

@given(instance=DatadiagramMLXForm::DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform::documentpropertiescollection_company_type(instance):
    assert isinstance(instance.company, str)


@given(instance=DatadiagramMLXForm::DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform::documentpropertiescollection_company_setter(instance):
    original = instance.company
    instance.company = original
    assert instance.company == original

@given(instance=SolutionXML_strategy)
@settings(max_examples=50)
def test_solutionxml_instantiation(instance):
    assert isinstance(instance, SolutionXML)

@given(instance=EmailRoutingData_strategy)
@settings(max_examples=50)
def test_emailroutingdata_instantiation(instance):
    assert isinstance(instance, EmailRoutingData)

@given(instance=DocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_documentpropertiescollection_instantiation(instance):
    assert isinstance(instance, DocumentPropertiesCollection)

@given(instance=DatadiagramMLXForm::VisioDocument_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::visiodocument_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::VisioDocument)

@given(instance=DatadiagramMLXForm::VisioDocument_strategy)
def test_datadiagrammlxform::visiodocument_docLangId_type(instance):
    assert isinstance(instance.docLangId, str)


@given(instance=DatadiagramMLXForm::VisioDocument_strategy)
def test_datadiagrammlxform::visiodocument_docLangId_setter(instance):
    original = instance.docLangId
    instance.docLangId = original
    assert instance.docLangId == original

@given(instance=DatadiagramMLXForm::VisioDocument_strategy)
def test_datadiagrammlxform::visiodocument_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=DatadiagramMLXForm::VisioDocument_strategy)
def test_datadiagrammlxform::visiodocument_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=DatadiagramMLXForm::VisioDocument_strategy)
def test_datadiagrammlxform::visiodocument_start_type(instance):
    assert isinstance(instance.start, str)


@given(instance=DatadiagramMLXForm::VisioDocument_strategy)
def test_datadiagrammlxform::visiodocument_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=DatadiagramMLXForm::VisioDocument_strategy)
def test_datadiagrammlxform::visiodocument_buildnum_type(instance):
    assert isinstance(instance.buildnum, str)


@given(instance=DatadiagramMLXForm::VisioDocument_strategy)
def test_datadiagrammlxform::visiodocument_buildnum_setter(instance):
    original = instance.buildnum
    instance.buildnum = original
    assert instance.buildnum == original

@given(instance=DatadiagramMLXForm::VisioDocument_strategy)
def test_datadiagrammlxform::visiodocument_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=DatadiagramMLXForm::VisioDocument_strategy)
def test_datadiagrammlxform::visiodocument_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=DatadiagramMLXForm::VisioDocument_strategy)
def test_datadiagrammlxform::visiodocument_metric_type(instance):
    assert isinstance(instance.metric, str)


@given(instance=DatadiagramMLXForm::VisioDocument_strategy)
def test_datadiagrammlxform::visiodocument_metric_setter(instance):
    original = instance.metric
    instance.metric = original
    assert instance.metric == original

@given(instance=FaceNamesTable_strategy)
@settings(max_examples=50)
def test_facenamestable_instantiation(instance):
    assert isinstance(instance, FaceNamesTable)

@given(instance=FontsTable_strategy)
@settings(max_examples=50)
def test_fontstable_instantiation(instance):
    assert isinstance(instance, FontsTable)

@given(instance=PrintSetup_strategy)
@settings(max_examples=50)
def test_printsetup_instantiation(instance):
    assert isinstance(instance, PrintSetup)

@given(instance=DatadiagramMLXForm::CellType_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::celltype_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::CellType)

@given(instance=DatadiagramMLXForm::CellType_strategy)
def test_datadiagrammlxform::celltype_err_type(instance):
    assert isinstance(instance.err, str)


@given(instance=DatadiagramMLXForm::CellType_strategy)
def test_datadiagrammlxform::celltype_err_setter(instance):
    original = instance.err
    instance.err = original
    assert instance.err == original

@given(instance=DatadiagramMLXForm::CellType_strategy)
def test_datadiagrammlxform::celltype_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=DatadiagramMLXForm::CellType_strategy)
def test_datadiagrammlxform::celltype_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=DatadiagramMLXForm::CellType_strategy)
def test_datadiagrammlxform::celltype_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=DatadiagramMLXForm::CellType_strategy)
def test_datadiagrammlxform::celltype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=DatadiagramMLXForm::CellType_strategy)
def test_datadiagrammlxform::celltype_formula_type(instance):
    assert isinstance(instance.formula, str)


@given(instance=DatadiagramMLXForm::CellType_strategy)
def test_datadiagrammlxform::celltype_formula_setter(instance):
    original = instance.formula
    instance.formula = original
    assert instance.formula == original

@given(instance=ColorsTable_strategy)
@settings(max_examples=50)
def test_colorstable_instantiation(instance):
    assert isinstance(instance, ColorsTable)

@given(instance=DocumentSettingsElt_strategy)
@settings(max_examples=50)
def test_documentsettingselt_instantiation(instance):
    assert isinstance(instance, DocumentSettingsElt)

@given(instance=DatadiagramMLXForm::DateTimeType_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::datetimetype_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::DateTimeType)

@given(instance=DatadiagramMLXForm::DateTimeType_strategy)
def test_datadiagrammlxform::datetimetype_second_type(instance):
    assert isinstance(instance.second, str)


@given(instance=DatadiagramMLXForm::DateTimeType_strategy)
def test_datadiagrammlxform::datetimetype_second_setter(instance):
    original = instance.second
    instance.second = original
    assert instance.second == original

@given(instance=DatadiagramMLXForm::DateTimeType_strategy)
def test_datadiagrammlxform::datetimetype_minute_type(instance):
    assert isinstance(instance.minute, str)


@given(instance=DatadiagramMLXForm::DateTimeType_strategy)
def test_datadiagrammlxform::datetimetype_minute_setter(instance):
    original = instance.minute
    instance.minute = original
    assert instance.minute == original

@given(instance=DatadiagramMLXForm::DateTimeType_strategy)
def test_datadiagrammlxform::datetimetype_day_type(instance):
    assert isinstance(instance.day, str)


@given(instance=DatadiagramMLXForm::DateTimeType_strategy)
def test_datadiagrammlxform::datetimetype_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original

@given(instance=DatadiagramMLXForm::DateTimeType_strategy)
def test_datadiagrammlxform::datetimetype_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=DatadiagramMLXForm::DateTimeType_strategy)
def test_datadiagrammlxform::datetimetype_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=DatadiagramMLXForm::DateTimeType_strategy)
def test_datadiagrammlxform::datetimetype_hour_type(instance):
    assert isinstance(instance.hour, str)


@given(instance=DatadiagramMLXForm::DateTimeType_strategy)
def test_datadiagrammlxform::datetimetype_hour_setter(instance):
    original = instance.hour
    instance.hour = original
    assert instance.hour == original

@given(instance=DatadiagramMLXForm::DateTimeType_strategy)
def test_datadiagrammlxform::datetimetype_year_type(instance):
    assert isinstance(instance.year, str)


@given(instance=DatadiagramMLXForm::DateTimeType_strategy)
def test_datadiagrammlxform::datetimetype_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=DatadiagramMLXForm::SolutionXML_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::solutionxml_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::SolutionXML)

@given(instance=DatadiagramMLXForm::HeaderFooter_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::headerfooter_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::HeaderFooter)

@given(instance=DatadiagramMLXForm::EventList_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::eventlist_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::EventList)

@given(instance=DatadiagramMLXForm::WindowsInfo_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::windowsinfo_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::WindowsInfo)

@given(instance=DatadiagramMLXForm::PageElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::pageelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::PageElt)

@given(instance=DatadiagramMLXForm::PagesCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::pagescollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::PagesCollection)

@given(instance=DatadiagramMLXForm::MasterElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::masterelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::MasterElt)

@given(instance=Connect_strategy)
@settings(max_examples=50)
def test_connect_instantiation(instance):
    assert isinstance(instance, Connect)

@given(instance=ConnectsCollection_strategy)
@settings(max_examples=50)
def test_connectscollection_instantiation(instance):
    assert isinstance(instance, ConnectsCollection)

@given(instance=DatadiagramMLXForm::Connect_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::connect_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::Connect)

@given(instance=DatadiagramMLXForm::Connect_strategy)
def test_datadiagrammlxform::connect_fromCell_type(instance):
    assert isinstance(instance.fromCell, str)


@given(instance=DatadiagramMLXForm::Connect_strategy)
def test_datadiagrammlxform::connect_fromCell_setter(instance):
    original = instance.fromCell
    instance.fromCell = original
    assert instance.fromCell == original

@given(instance=DatadiagramMLXForm::Connect_strategy)
def test_datadiagrammlxform::connect_toSheet_type(instance):
    assert isinstance(instance.toSheet, str)


@given(instance=DatadiagramMLXForm::Connect_strategy)
def test_datadiagrammlxform::connect_toSheet_setter(instance):
    original = instance.toSheet
    instance.toSheet = original
    assert instance.toSheet == original

@given(instance=DatadiagramMLXForm::Connect_strategy)
def test_datadiagrammlxform::connect_fromPart_type(instance):
    assert isinstance(instance.fromPart, str)


@given(instance=DatadiagramMLXForm::Connect_strategy)
def test_datadiagrammlxform::connect_fromPart_setter(instance):
    original = instance.fromPart
    instance.fromPart = original
    assert instance.fromPart == original

@given(instance=DatadiagramMLXForm::Connect_strategy)
def test_datadiagrammlxform::connect_toCell_type(instance):
    assert isinstance(instance.toCell, str)


@given(instance=DatadiagramMLXForm::Connect_strategy)
def test_datadiagrammlxform::connect_toCell_setter(instance):
    original = instance.toCell
    instance.toCell = original
    assert instance.toCell == original

@given(instance=DatadiagramMLXForm::Connect_strategy)
def test_datadiagrammlxform::connect_fromSheet_type(instance):
    assert isinstance(instance.fromSheet, str)


@given(instance=DatadiagramMLXForm::Connect_strategy)
def test_datadiagrammlxform::connect_fromSheet_setter(instance):
    original = instance.fromSheet
    instance.fromSheet = original
    assert instance.fromSheet == original

@given(instance=DatadiagramMLXForm::Connect_strategy)
def test_datadiagrammlxform::connect_toPart_type(instance):
    assert isinstance(instance.toPart, str)


@given(instance=DatadiagramMLXForm::Connect_strategy)
def test_datadiagrammlxform::connect_toPart_setter(instance):
    original = instance.toPart
    instance.toPart = original
    assert instance.toPart == original

@given(instance=MasterShortCut_strategy)
@settings(max_examples=50)
def test_mastershortcut_instantiation(instance):
    assert isinstance(instance, MasterShortCut)

@given(instance=Master_strategy)
@settings(max_examples=50)
def test_master_instantiation(instance):
    assert isinstance(instance, Master)

@given(instance=Icon_strategy)
@settings(max_examples=50)
def test_icon_instantiation(instance):
    assert isinstance(instance, Icon)

@given(instance=DatadiagramMLXForm::MastersCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::masterscollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::MastersCollection)

@given(instance=TabsCollection_strategy)
@settings(max_examples=50)
def test_tabscollection_instantiation(instance):
    assert isinstance(instance, TabsCollection)

@given(instance=Tab_strategy)
@settings(max_examples=50)
def test_tab_instantiation(instance):
    assert isinstance(instance, Tab)

@given(instance=TextElt_strategy)
@settings(max_examples=50)
def test_textelt_instantiation(instance):
    assert isinstance(instance, TextElt)

@given(instance=DatadiagramMLXForm::StringElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::stringelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::StringElt)

@given(instance=DatadiagramMLXForm::StringElt_strategy)
def test_datadiagrammlxform::stringelt_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=DatadiagramMLXForm::StringElt_strategy)
def test_datadiagrammlxform::stringelt_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=XYABCDEElt_strategy)
@settings(max_examples=50)
def test_xyabcdeelt_instantiation(instance):
    assert isinstance(instance, XYABCDEElt)

@given(instance=DatadiagramMLXForm::NURBSTo_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::nurbsto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::NURBSTo)

@given(instance=XYABCDElt_strategy)
@settings(max_examples=50)
def test_xyabcdelt_instantiation(instance):
    assert isinstance(instance, XYABCDElt)

@given(instance=DatadiagramMLXForm::EllipticalArcTo_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::ellipticalarcto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::EllipticalArcTo)

@given(instance=DatadiagramMLXForm::XYABCDEElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::xyabcdeelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::XYABCDEElt)

@given(instance=DatadiagramMLXForm::SplineStart_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::splinestart_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::SplineStart)

@given(instance=DatadiagramMLXForm::Ellipse_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::ellipse_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::Ellipse)

@given(instance=DatadiagramMLXForm::IXrequiredElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::ixrequiredelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::IXrequiredElt)

@given(instance=DatadiagramMLXForm::IXrequiredElt_strategy)
def test_datadiagrammlxform::ixrequiredelt_iX_type(instance):
    assert isinstance(instance.iX, str)


@given(instance=DatadiagramMLXForm::IXrequiredElt_strategy)
def test_datadiagrammlxform::ixrequiredelt_iX_setter(instance):
    original = instance.iX
    instance.iX = original
    assert instance.iX == original

@given(instance=Text_strategy)
@settings(max_examples=50)
def test_text_instantiation(instance):
    assert isinstance(instance, Text)

@given(instance=DatadiagramMLXForm::TextElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::textelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::TextElt)

@given(instance=Geom_strategy)
@settings(max_examples=50)
def test_geom_instantiation(instance):
    assert isinstance(instance, Geom)

@given(instance=XYElt_strategy)
@settings(max_examples=50)
def test_xyelt_instantiation(instance):
    assert isinstance(instance, XYElt)

@given(instance=DatadiagramMLXForm::LineTo_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::lineto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::LineTo)

@given(instance=XYABElt_strategy)
@settings(max_examples=50)
def test_xyabelt_instantiation(instance):
    assert isinstance(instance, XYABElt)

@given(instance=DatadiagramMLXForm::XYABCDElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::xyabcdelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::XYABCDElt)

@given(instance=DatadiagramMLXForm::InfiniteLine_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::infiniteline_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::InfiniteLine)

@given(instance=XYAElt_strategy)
@settings(max_examples=50)
def test_xyaelt_instantiation(instance):
    assert isinstance(instance, XYAElt)

@given(instance=DatadiagramMLXForm::SplineKnot_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::splineknot_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::SplineKnot)

@given(instance=DatadiagramMLXForm::PolylineTo_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::polylineto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::PolylineTo)

@given(instance=DatadiagramMLXForm::XYABElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::xyabelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::XYABElt)

@given(instance=DatadiagramMLXForm::ArcTo_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::arcto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::ArcTo)

@given(instance=DatadiagramMLXForm::XYAElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::xyaelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::XYAElt)

@given(instance=DatadiagramMLXForm::MoveTo_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::moveto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::MoveTo)

@given(instance=CellType_strategy)
@settings(max_examples=50)
def test_celltype_instantiation(instance):
    assert isinstance(instance, CellType)

@given(instance=NURBSTo_strategy)
@settings(max_examples=50)
def test_nurbsto_instantiation(instance):
    assert isinstance(instance, NURBSTo)

@given(instance=SplineStart_strategy)
@settings(max_examples=50)
def test_splinestart_instantiation(instance):
    assert isinstance(instance, SplineStart)

@given(instance=EllipticalArcTo_strategy)
@settings(max_examples=50)
def test_ellipticalarcto_instantiation(instance):
    assert isinstance(instance, EllipticalArcTo)

@given(instance=Ellipse_strategy)
@settings(max_examples=50)
def test_ellipse_instantiation(instance):
    assert isinstance(instance, Ellipse)

@given(instance=InfiniteLine_strategy)
@settings(max_examples=50)
def test_infiniteline_instantiation(instance):
    assert isinstance(instance, InfiniteLine)

@given(instance=PolylineTo_strategy)
@settings(max_examples=50)
def test_polylineto_instantiation(instance):
    assert isinstance(instance, PolylineTo)

@given(instance=SplineKnot_strategy)
@settings(max_examples=50)
def test_splineknot_instantiation(instance):
    assert isinstance(instance, SplineKnot)

@given(instance=ArcTo_strategy)
@settings(max_examples=50)
def test_arcto_instantiation(instance):
    assert isinstance(instance, ArcTo)

@given(instance=MoveTo_strategy)
@settings(max_examples=50)
def test_moveto_instantiation(instance):
    assert isinstance(instance, MoveTo)

@given(instance=LineTo_strategy)
@settings(max_examples=50)
def test_lineto_instantiation(instance):
    assert isinstance(instance, LineTo)

@given(instance=DatadiagramMLXForm::IdentifiedElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::identifiedelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::IdentifiedElt)

@given(instance=DatadiagramMLXForm::IdentifiedElt_strategy)
def test_datadiagrammlxform::identifiedelt_ID_type(instance):
    assert isinstance(instance.ID, str)


@given(instance=DatadiagramMLXForm::IdentifiedElt_strategy)
def test_datadiagrammlxform::identifiedelt_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=DatadiagramMLXForm::NamedElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::namedelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::NamedElt)

@given(instance=DatadiagramMLXForm::NamedElt_strategy)
def test_datadiagrammlxform::namedelt_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=DatadiagramMLXForm::NamedElt_strategy)
def test_datadiagrammlxform::namedelt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DatadiagramMLXForm::NamedElt_strategy)
def test_datadiagrammlxform::namedelt_nameU_type(instance):
    assert isinstance(instance.nameU, str)


@given(instance=DatadiagramMLXForm::NamedElt_strategy)
def test_datadiagrammlxform::namedelt_nameU_setter(instance):
    original = instance.nameU
    instance.nameU = original
    assert instance.nameU == original

@given(instance=PageElt_strategy)
@settings(max_examples=50)
def test_pageelt_instantiation(instance):
    assert isinstance(instance, PageElt)

@given(instance=MasterElt_strategy)
@settings(max_examples=50)
def test_masterelt_instantiation(instance):
    assert isinstance(instance, MasterElt)

@given(instance=DatadiagramMLXForm::Icon_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::icon_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::Icon)

@given(instance=DatadiagramMLXForm::Icon_strategy)
def test_datadiagrammlxform::icon_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=DatadiagramMLXForm::Icon_strategy)
def test_datadiagrammlxform::icon_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=DatadiagramMLXForm::ShapesCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::shapescollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::ShapesCollection)

@given(instance=DatadiagramMLXForm::ConnectsCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::connectscollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::ConnectsCollection)

@given(instance=UniqueIdElt_strategy)
@settings(max_examples=50)
def test_uniqueidelt_instantiation(instance):
    assert isinstance(instance, UniqueIdElt)

@given(instance=DelElt_strategy)
@settings(max_examples=50)
def test_delelt_instantiation(instance):
    assert isinstance(instance, DelElt)

@given(instance=IXElt_strategy)
@settings(max_examples=50)
def test_ixelt_instantiation(instance):
    assert isinstance(instance, IXElt)

@given(instance=DatadiagramMLXForm::Tab_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::tab_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::Tab)

@given(instance=DatadiagramMLXForm::XYElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::xyelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::XYElt)

@given(instance=DatadiagramMLXForm::DelElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::delelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::DelElt)

@given(instance=DatadiagramMLXForm::DelElt_strategy)
def test_datadiagrammlxform::delelt_del__type(instance):
    assert isinstance(instance.del_, str)


@given(instance=DatadiagramMLXForm::DelElt_strategy)
def test_datadiagrammlxform::delelt_del__setter(instance):
    original = instance.del_
    instance.del_ = original
    assert instance.del_ == original

@given(instance=DatadiagramMLXForm::IXElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::ixelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::IXElt)

@given(instance=DatadiagramMLXForm::IXElt_strategy)
def test_datadiagrammlxform::ixelt_iX_type(instance):
    assert isinstance(instance.iX, str)


@given(instance=DatadiagramMLXForm::IXElt_strategy)
def test_datadiagrammlxform::ixelt_iX_setter(instance):
    original = instance.iX
    instance.iX = original
    assert instance.iX == original

@given(instance=DatadiagramMLXForm::ShapeElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::shapeelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::ShapeElt)

@given(instance=ShapeElt_strategy)
@settings(max_examples=50)
def test_shapeelt_instantiation(instance):
    assert isinstance(instance, ShapeElt)

@given(instance=DatadiagramMLXForm::XForm_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::xform_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::XForm)

@given(instance=DatadiagramMLXForm::Field_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::field_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::Field)

@given(instance=DatadiagramMLXForm::Char_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::char_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::Char)

@given(instance=DatadiagramMLXForm::Text_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::text_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::Text)

@given(instance=DatadiagramMLXForm::TabsCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::tabscollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::TabsCollection)

@given(instance=DatadiagramMLXForm::Para_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::para_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::Para)

@given(instance=DatadiagramMLXForm::Geom_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::geom_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::Geom)

@given(instance=ShapesCollection_strategy)
@settings(max_examples=50)
def test_shapescollection_instantiation(instance):
    assert isinstance(instance, ShapesCollection)

@given(instance=DatadiagramMLXForm::Shape_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::shape_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::Shape)

@given(instance=DatadiagramMLXForm::Shape_strategy)
def test_datadiagrammlxform::shape_lineStyle_type(instance):
    assert isinstance(instance.lineStyle, str)


@given(instance=DatadiagramMLXForm::Shape_strategy)
def test_datadiagrammlxform::shape_lineStyle_setter(instance):
    original = instance.lineStyle
    instance.lineStyle = original
    assert instance.lineStyle == original

@given(instance=DatadiagramMLXForm::Shape_strategy)
def test_datadiagrammlxform::shape_fillStyle_type(instance):
    assert isinstance(instance.fillStyle, str)


@given(instance=DatadiagramMLXForm::Shape_strategy)
def test_datadiagrammlxform::shape_fillStyle_setter(instance):
    original = instance.fillStyle
    instance.fillStyle = original
    assert instance.fillStyle == original

@given(instance=DatadiagramMLXForm::Shape_strategy)
def test_datadiagrammlxform::shape_textStyle_type(instance):
    assert isinstance(instance.textStyle, str)


@given(instance=DatadiagramMLXForm::Shape_strategy)
def test_datadiagrammlxform::shape_textStyle_setter(instance):
    original = instance.textStyle
    instance.textStyle = original
    assert instance.textStyle == original

@given(instance=DatadiagramMLXForm::UniqueIdElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::uniqueidelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::UniqueIdElt)

@given(instance=DatadiagramMLXForm::UniqueIdElt_strategy)
def test_datadiagrammlxform::uniqueidelt_UniqueID_type(instance):
    assert isinstance(instance.UniqueID, str)


@given(instance=DatadiagramMLXForm::UniqueIdElt_strategy)
def test_datadiagrammlxform::uniqueidelt_UniqueID_setter(instance):
    original = instance.UniqueID
    instance.UniqueID = original
    assert instance.UniqueID == original

@given(instance=PageSheet_strategy)
@settings(max_examples=50)
def test_pagesheet_instantiation(instance):
    assert isinstance(instance, PageSheet)

@given(instance=NamedElt_strategy)
@settings(max_examples=50)
def test_namedelt_instantiation(instance):
    assert isinstance(instance, NamedElt)

@given(instance=DatadiagramMLXForm::DocumentSheet_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::documentsheet_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::DocumentSheet)

@given(instance=Shape_strategy)
@settings(max_examples=50)
def test_shape_instantiation(instance):
    assert isinstance(instance, Shape)

@given(instance=DatadiagramMLXForm::PageSheet_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::pagesheet_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::PageSheet)

@given(instance=FaceName_strategy)
@settings(max_examples=50)
def test_facename_instantiation(instance):
    assert isinstance(instance, FaceName)

@given(instance=DatadiagramMLXForm::FaceNamesTable_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::facenamestable_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::FaceNamesTable)

@given(instance=DatadiagramMLXForm::StyleSheetsCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::stylesheetscollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::StyleSheetsCollection)

@given(instance=DatadiagramMLXForm::EmailRoutingData_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::emailroutingdata_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::EmailRoutingData)

@given(instance=DatadiagramMLXForm::EmailRoutingData_strategy)
def test_datadiagrammlxform::emailroutingdata_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=DatadiagramMLXForm::EmailRoutingData_strategy)
def test_datadiagrammlxform::emailroutingdata_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=DatadiagramMLXForm::EmailRoutingData_strategy)
def test_datadiagrammlxform::emailroutingdata_data_type(instance):
    assert isinstance(instance.data, str)


@given(instance=DatadiagramMLXForm::EmailRoutingData_strategy)
def test_datadiagrammlxform::emailroutingdata_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=DatadiagramMLXForm::VBProjectData_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::vbprojectdata_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::VBProjectData)

@given(instance=DatadiagramMLXForm::VBProjectData_strategy)
def test_datadiagrammlxform::vbprojectdata_data_type(instance):
    assert isinstance(instance.data, str)


@given(instance=DatadiagramMLXForm::VBProjectData_strategy)
def test_datadiagrammlxform::vbprojectdata_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=IdentifiedElt_strategy)
@settings(max_examples=50)
def test_identifiedelt_instantiation(instance):
    assert isinstance(instance, IdentifiedElt)

@given(instance=DatadiagramMLXForm::MasterShortCut_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::mastershortcut_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::MasterShortCut)

@given(instance=DatadiagramMLXForm::MasterShortCut_strategy)
def test_datadiagrammlxform::mastershortcut_shortcutHelp_type(instance):
    assert isinstance(instance.shortcutHelp, str)


@given(instance=DatadiagramMLXForm::MasterShortCut_strategy)
def test_datadiagrammlxform::mastershortcut_shortcutHelp_setter(instance):
    original = instance.shortcutHelp
    instance.shortcutHelp = original
    assert instance.shortcutHelp == original

@given(instance=DatadiagramMLXForm::MasterShortCut_strategy)
def test_datadiagrammlxform::mastershortcut_patternFlags_type(instance):
    assert isinstance(instance.patternFlags, str)


@given(instance=DatadiagramMLXForm::MasterShortCut_strategy)
def test_datadiagrammlxform::mastershortcut_patternFlags_setter(instance):
    original = instance.patternFlags
    instance.patternFlags = original
    assert instance.patternFlags == original

@given(instance=DatadiagramMLXForm::MasterShortCut_strategy)
def test_datadiagrammlxform::mastershortcut_iconSize_type(instance):
    assert isinstance(instance.iconSize, str)


@given(instance=DatadiagramMLXForm::MasterShortCut_strategy)
def test_datadiagrammlxform::mastershortcut_iconSize_setter(instance):
    original = instance.iconSize
    instance.iconSize = original
    assert instance.iconSize == original

@given(instance=DatadiagramMLXForm::MasterShortCut_strategy)
def test_datadiagrammlxform::mastershortcut_prompt_type(instance):
    assert isinstance(instance.prompt, str)


@given(instance=DatadiagramMLXForm::MasterShortCut_strategy)
def test_datadiagrammlxform::mastershortcut_prompt_setter(instance):
    original = instance.prompt
    instance.prompt = original
    assert instance.prompt == original

@given(instance=DatadiagramMLXForm::MasterShortCut_strategy)
def test_datadiagrammlxform::mastershortcut_shortcutURL_type(instance):
    assert isinstance(instance.shortcutURL, str)


@given(instance=DatadiagramMLXForm::MasterShortCut_strategy)
def test_datadiagrammlxform::mastershortcut_shortcutURL_setter(instance):
    original = instance.shortcutURL
    instance.shortcutURL = original
    assert instance.shortcutURL == original

@given(instance=DatadiagramMLXForm::MasterShortCut_strategy)
def test_datadiagrammlxform::mastershortcut_alignName_type(instance):
    assert isinstance(instance.alignName, str)


@given(instance=DatadiagramMLXForm::MasterShortCut_strategy)
def test_datadiagrammlxform::mastershortcut_alignName_setter(instance):
    original = instance.alignName
    instance.alignName = original
    assert instance.alignName == original

@given(instance=DatadiagramMLXForm::FaceName_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::facename_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::FaceName)

@given(instance=DatadiagramMLXForm::FaceName_strategy)
def test_datadiagrammlxform::facename_charSet_type(instance):
    assert isinstance(instance.charSet, str)


@given(instance=DatadiagramMLXForm::FaceName_strategy)
def test_datadiagrammlxform::facename_charSet_setter(instance):
    original = instance.charSet
    instance.charSet = original
    assert instance.charSet == original

@given(instance=DatadiagramMLXForm::FaceName_strategy)
def test_datadiagrammlxform::facename_panos_type(instance):
    assert isinstance(instance.panos, str)


@given(instance=DatadiagramMLXForm::FaceName_strategy)
def test_datadiagrammlxform::facename_panos_setter(instance):
    original = instance.panos
    instance.panos = original
    assert instance.panos == original

@given(instance=DatadiagramMLXForm::FaceName_strategy)
def test_datadiagrammlxform::facename_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=DatadiagramMLXForm::FaceName_strategy)
def test_datadiagrammlxform::facename_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DatadiagramMLXForm::FaceName_strategy)
def test_datadiagrammlxform::facename_unicodeRanges_type(instance):
    assert isinstance(instance.unicodeRanges, str)


@given(instance=DatadiagramMLXForm::FaceName_strategy)
def test_datadiagrammlxform::facename_unicodeRanges_setter(instance):
    original = instance.unicodeRanges
    instance.unicodeRanges = original
    assert instance.unicodeRanges == original

@given(instance=DatadiagramMLXForm::FaceName_strategy)
def test_datadiagrammlxform::facename_flags_type(instance):
    assert isinstance(instance.flags, str)


@given(instance=DatadiagramMLXForm::FaceName_strategy)
def test_datadiagrammlxform::facename_flags_setter(instance):
    original = instance.flags
    instance.flags = original
    assert instance.flags == original

@given(instance=DatadiagramMLXForm::StyleSheet_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::stylesheet_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::StyleSheet)

@given(instance=DatadiagramMLXForm::Page_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::page_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::Page)

@given(instance=DatadiagramMLXForm::Page_strategy)
def test_datadiagrammlxform::page_ViewCenterY_type(instance):
    assert isinstance(instance.ViewCenterY, str)


@given(instance=DatadiagramMLXForm::Page_strategy)
def test_datadiagrammlxform::page_ViewCenterY_setter(instance):
    original = instance.ViewCenterY
    instance.ViewCenterY = original
    assert instance.ViewCenterY == original

@given(instance=DatadiagramMLXForm::Page_strategy)
def test_datadiagrammlxform::page_reviewerID_type(instance):
    assert isinstance(instance.reviewerID, str)


@given(instance=DatadiagramMLXForm::Page_strategy)
def test_datadiagrammlxform::page_reviewerID_setter(instance):
    original = instance.reviewerID
    instance.reviewerID = original
    assert instance.reviewerID == original

@given(instance=DatadiagramMLXForm::Page_strategy)
def test_datadiagrammlxform::page_backPage_type(instance):
    assert isinstance(instance.backPage, str)


@given(instance=DatadiagramMLXForm::Page_strategy)
def test_datadiagrammlxform::page_backPage_setter(instance):
    original = instance.backPage
    instance.backPage = original
    assert instance.backPage == original

@given(instance=DatadiagramMLXForm::Page_strategy)
def test_datadiagrammlxform::page_viewScale_type(instance):
    assert isinstance(instance.viewScale, str)


@given(instance=DatadiagramMLXForm::Page_strategy)
def test_datadiagrammlxform::page_viewScale_setter(instance):
    original = instance.viewScale
    instance.viewScale = original
    assert instance.viewScale == original

@given(instance=DatadiagramMLXForm::Page_strategy)
def test_datadiagrammlxform::page_background_type(instance):
    assert isinstance(instance.background, str)


@given(instance=DatadiagramMLXForm::Page_strategy)
def test_datadiagrammlxform::page_background_setter(instance):
    original = instance.background
    instance.background = original
    assert instance.background == original

@given(instance=DatadiagramMLXForm::Page_strategy)
def test_datadiagrammlxform::page_associatedPage_type(instance):
    assert isinstance(instance.associatedPage, str)


@given(instance=DatadiagramMLXForm::Page_strategy)
def test_datadiagrammlxform::page_associatedPage_setter(instance):
    original = instance.associatedPage
    instance.associatedPage = original
    assert instance.associatedPage == original

@given(instance=DatadiagramMLXForm::Page_strategy)
def test_datadiagrammlxform::page_viewCenterX_type(instance):
    assert isinstance(instance.viewCenterX, str)


@given(instance=DatadiagramMLXForm::Page_strategy)
def test_datadiagrammlxform::page_viewCenterX_setter(instance):
    original = instance.viewCenterX
    instance.viewCenterX = original
    assert instance.viewCenterX == original

@given(instance=DatadiagramMLXForm::Master_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::master_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::Master)

@given(instance=DatadiagramMLXForm::Master_strategy)
def test_datadiagrammlxform::master_prompt_type(instance):
    assert isinstance(instance.prompt, str)


@given(instance=DatadiagramMLXForm::Master_strategy)
def test_datadiagrammlxform::master_prompt_setter(instance):
    original = instance.prompt
    instance.prompt = original
    assert instance.prompt == original

@given(instance=DatadiagramMLXForm::Master_strategy)
def test_datadiagrammlxform::master_matchByName_type(instance):
    assert isinstance(instance.matchByName, str)


@given(instance=DatadiagramMLXForm::Master_strategy)
def test_datadiagrammlxform::master_matchByName_setter(instance):
    original = instance.matchByName
    instance.matchByName = original
    assert instance.matchByName == original

@given(instance=DatadiagramMLXForm::Master_strategy)
def test_datadiagrammlxform::master_patternFlags_type(instance):
    assert isinstance(instance.patternFlags, str)


@given(instance=DatadiagramMLXForm::Master_strategy)
def test_datadiagrammlxform::master_patternFlags_setter(instance):
    original = instance.patternFlags
    instance.patternFlags = original
    assert instance.patternFlags == original

@given(instance=DatadiagramMLXForm::Master_strategy)
def test_datadiagrammlxform::master_baseID_type(instance):
    assert isinstance(instance.baseID, str)


@given(instance=DatadiagramMLXForm::Master_strategy)
def test_datadiagrammlxform::master_baseID_setter(instance):
    original = instance.baseID
    instance.baseID = original
    assert instance.baseID == original

@given(instance=DatadiagramMLXForm::Master_strategy)
def test_datadiagrammlxform::master_hidden_type(instance):
    assert isinstance(instance.hidden, str)


@given(instance=DatadiagramMLXForm::Master_strategy)
def test_datadiagrammlxform::master_hidden_setter(instance):
    original = instance.hidden
    instance.hidden = original
    assert instance.hidden == original

@given(instance=DatadiagramMLXForm::Master_strategy)
def test_datadiagrammlxform::master_iconSize_type(instance):
    assert isinstance(instance.iconSize, str)


@given(instance=DatadiagramMLXForm::Master_strategy)
def test_datadiagrammlxform::master_iconSize_setter(instance):
    original = instance.iconSize
    instance.iconSize = original
    assert instance.iconSize == original

@given(instance=DatadiagramMLXForm::Master_strategy)
def test_datadiagrammlxform::master_iconUpdate_type(instance):
    assert isinstance(instance.iconUpdate, str)


@given(instance=DatadiagramMLXForm::Master_strategy)
def test_datadiagrammlxform::master_iconUpdate_setter(instance):
    original = instance.iconUpdate
    instance.iconUpdate = original
    assert instance.iconUpdate == original

@given(instance=DatadiagramMLXForm::Master_strategy)
def test_datadiagrammlxform::master_alignName_type(instance):
    assert isinstance(instance.alignName, str)


@given(instance=DatadiagramMLXForm::Master_strategy)
def test_datadiagrammlxform::master_alignName_setter(instance):
    original = instance.alignName
    instance.alignName = original
    assert instance.alignName == original

@given(instance=DatadiagramMLXForm::FontEntry_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::fontentry_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::FontEntry)

@given(instance=DatadiagramMLXForm::FontEntry_strategy)
def test_datadiagrammlxform::fontentry_attributes_type(instance):
    assert isinstance(instance.attributes, str)


@given(instance=DatadiagramMLXForm::FontEntry_strategy)
def test_datadiagrammlxform::fontentry_attributes_setter(instance):
    original = instance.attributes
    instance.attributes = original
    assert instance.attributes == original

@given(instance=DatadiagramMLXForm::FontEntry_strategy)
def test_datadiagrammlxform::fontentry_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=DatadiagramMLXForm::FontEntry_strategy)
def test_datadiagrammlxform::fontentry_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DatadiagramMLXForm::FontEntry_strategy)
def test_datadiagrammlxform::fontentry_unicode_type(instance):
    assert isinstance(instance.unicode, str)


@given(instance=DatadiagramMLXForm::FontEntry_strategy)
def test_datadiagrammlxform::fontentry_unicode_setter(instance):
    original = instance.unicode
    instance.unicode = original
    assert instance.unicode == original

@given(instance=DatadiagramMLXForm::FontEntry_strategy)
def test_datadiagrammlxform::fontentry_charSet_type(instance):
    assert isinstance(instance.charSet, str)


@given(instance=DatadiagramMLXForm::FontEntry_strategy)
def test_datadiagrammlxform::fontentry_charSet_setter(instance):
    original = instance.charSet
    instance.charSet = original
    assert instance.charSet == original

@given(instance=DatadiagramMLXForm::FontEntry_strategy)
def test_datadiagrammlxform::fontentry_pitchAndFamily_type(instance):
    assert isinstance(instance.pitchAndFamily, str)


@given(instance=DatadiagramMLXForm::FontEntry_strategy)
def test_datadiagrammlxform::fontentry_pitchAndFamily_setter(instance):
    original = instance.pitchAndFamily
    instance.pitchAndFamily = original
    assert instance.pitchAndFamily == original

@given(instance=DatadiagramMLXForm::FontEntry_strategy)
def test_datadiagrammlxform::fontentry_weight_type(instance):
    assert isinstance(instance.weight, str)


@given(instance=DatadiagramMLXForm::FontEntry_strategy)
def test_datadiagrammlxform::fontentry_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=FontEntry_strategy)
@settings(max_examples=50)
def test_fontentry_instantiation(instance):
    assert isinstance(instance, FontEntry)

@given(instance=DatadiagramMLXForm::FontsTable_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::fontstable_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::FontsTable)

@given(instance=DatadiagramMLXForm::PrintSetup_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::printsetup_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::PrintSetup)

@given(instance=SnapAnglesCollection_strategy)
@settings(max_examples=50)
def test_snapanglescollection_instantiation(instance):
    assert isinstance(instance, SnapAnglesCollection)

@given(instance=IXrequiredElt_strategy)
@settings(max_examples=50)
def test_ixrequiredelt_instantiation(instance):
    assert isinstance(instance, IXrequiredElt)

@given(instance=DatadiagramMLXForm::Pp_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::pp_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::Pp)

@given(instance=DatadiagramMLXForm::Tp_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::tp_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::Tp)

@given(instance=DatadiagramMLXForm::Fld_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::fld_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::Fld)

@given(instance=DatadiagramMLXForm::Cp_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::cp_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::Cp)

@given(instance=DatadiagramMLXForm::ColorEntry_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::colorentry_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::ColorEntry)

@given(instance=DatadiagramMLXForm::ColorEntry_strategy)
def test_datadiagrammlxform::colorentry_rgb_type(instance):
    assert isinstance(instance.rgb, str)


@given(instance=DatadiagramMLXForm::ColorEntry_strategy)
def test_datadiagrammlxform::colorentry_rgb_setter(instance):
    original = instance.rgb
    instance.rgb = original
    assert instance.rgb == original

@given(instance=ColorEntry_strategy)
@settings(max_examples=50)
def test_colorentry_instantiation(instance):
    assert isinstance(instance, ColorEntry)

@given(instance=StyleSheet_strategy)
@settings(max_examples=50)
def test_stylesheet_instantiation(instance):
    assert isinstance(instance, StyleSheet)

@given(instance=DatadiagramMLXForm::ColorsTable_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::colorstable_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::ColorsTable)

@given(instance=Page_strategy)
@settings(max_examples=50)
def test_page_instantiation(instance):
    assert isinstance(instance, Page)

@given(instance=DatadiagramMLXForm::SnapAngle_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::snapangle_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::SnapAngle)

@given(instance=DatadiagramMLXForm::SnapAngle_strategy)
def test_datadiagrammlxform::snapangle_angleValue_type(instance):
    assert isinstance(instance.angleValue, str)


@given(instance=DatadiagramMLXForm::SnapAngle_strategy)
def test_datadiagrammlxform::snapangle_angleValue_setter(instance):
    original = instance.angleValue
    instance.angleValue = original
    assert instance.angleValue == original

@given(instance=SnapAngle_strategy)
@settings(max_examples=50)
def test_snapangle_instantiation(instance):
    assert isinstance(instance, SnapAngle)

@given(instance=DatadiagramMLXForm::SnapAnglesCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::snapanglescollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::SnapAnglesCollection)

@given(instance=DateTimeType_strategy)
@settings(max_examples=50)
def test_datetimetype_instantiation(instance):
    assert isinstance(instance, DateTimeType)

@given(instance=CustomPropertiesCollection_strategy)
@settings(max_examples=50)
def test_custompropertiescollection_instantiation(instance):
    assert isinstance(instance, CustomPropertiesCollection)

@given(instance=DatadiagramMLXForm::DocumentSettingsElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::documentsettingselt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::DocumentSettingsElt)

@given(instance=DatadiagramMLXForm::DocumentSettingsElt_strategy)
def test_datadiagrammlxform::documentsettingselt_customMenusFile_type(instance):
    assert isinstance(instance.customMenusFile, str)


@given(instance=DatadiagramMLXForm::DocumentSettingsElt_strategy)
def test_datadiagrammlxform::documentsettingselt_customMenusFile_setter(instance):
    original = instance.customMenusFile
    instance.customMenusFile = original
    assert instance.customMenusFile == original

@given(instance=DatadiagramMLXForm::DocumentSettingsElt_strategy)
def test_datadiagrammlxform::documentsettingselt_attachedToolbars_type(instance):
    assert isinstance(instance.attachedToolbars, str)


@given(instance=DatadiagramMLXForm::DocumentSettingsElt_strategy)
def test_datadiagrammlxform::documentsettingselt_attachedToolbars_setter(instance):
    original = instance.attachedToolbars
    instance.attachedToolbars = original
    assert instance.attachedToolbars == original

@given(instance=DatadiagramMLXForm::DocumentSettingsElt_strategy)
def test_datadiagrammlxform::documentsettingselt_customToolbarsFile_type(instance):
    assert isinstance(instance.customToolbarsFile, str)


@given(instance=DatadiagramMLXForm::DocumentSettingsElt_strategy)
def test_datadiagrammlxform::documentsettingselt_customToolbarsFile_setter(instance):
    original = instance.customToolbarsFile
    instance.customToolbarsFile = original
    assert instance.customToolbarsFile == original

@given(instance=DatadiagramMLXForm::DocumentSettingsElt_strategy)
def test_datadiagrammlxform::documentsettingselt_protectBkgnds_type(instance):
    assert isinstance(instance.protectBkgnds, str)


@given(instance=DatadiagramMLXForm::DocumentSettingsElt_strategy)
def test_datadiagrammlxform::documentsettingselt_protectBkgnds_setter(instance):
    original = instance.protectBkgnds
    instance.protectBkgnds = original
    assert instance.protectBkgnds == original

@given(instance=DatadiagramMLXForm::DocumentSettingsElt_strategy)
def test_datadiagrammlxform::documentsettingselt_protectStyles_type(instance):
    assert isinstance(instance.protectStyles, str)


@given(instance=DatadiagramMLXForm::DocumentSettingsElt_strategy)
def test_datadiagrammlxform::documentsettingselt_protectStyles_setter(instance):
    original = instance.protectStyles
    instance.protectStyles = original
    assert instance.protectStyles == original

@given(instance=DatadiagramMLXForm::DocumentSettingsElt_strategy)
def test_datadiagrammlxform::documentsettingselt_protectMasters_type(instance):
    assert isinstance(instance.protectMasters, str)


@given(instance=DatadiagramMLXForm::DocumentSettingsElt_strategy)
def test_datadiagrammlxform::documentsettingselt_protectMasters_setter(instance):
    original = instance.protectMasters
    instance.protectMasters = original
    assert instance.protectMasters == original

@given(instance=DatadiagramMLXForm::DocumentSettingsElt_strategy)
def test_datadiagrammlxform::documentsettingselt_protectShapes_type(instance):
    assert isinstance(instance.protectShapes, str)


@given(instance=DatadiagramMLXForm::DocumentSettingsElt_strategy)
def test_datadiagrammlxform::documentsettingselt_protectShapes_setter(instance):
    original = instance.protectShapes
    instance.protectShapes = original
    assert instance.protectShapes == original

@given(instance=DatadiagramMLXForm::DocumentSettingsElt_strategy)
def test_datadiagrammlxform::documentsettingselt_snapSettings_type(instance):
    assert isinstance(instance.snapSettings, str)


@given(instance=DatadiagramMLXForm::DocumentSettingsElt_strategy)
def test_datadiagrammlxform::documentsettingselt_snapSettings_setter(instance):
    original = instance.snapSettings
    instance.snapSettings = original
    assert instance.snapSettings == original

@given(instance=DatadiagramMLXForm::DocumentSettingsElt_strategy)
def test_datadiagrammlxform::documentsettingselt_dynamicGridEnabled_type(instance):
    assert isinstance(instance.dynamicGridEnabled, str)


@given(instance=DatadiagramMLXForm::DocumentSettingsElt_strategy)
def test_datadiagrammlxform::documentsettingselt_dynamicGridEnabled_setter(instance):
    original = instance.dynamicGridEnabled
    instance.dynamicGridEnabled = original
    assert instance.dynamicGridEnabled == original

@given(instance=DatadiagramMLXForm::DocumentSettingsElt_strategy)
def test_datadiagrammlxform::documentsettingselt_glueSettings_type(instance):
    assert isinstance(instance.glueSettings, str)


@given(instance=DatadiagramMLXForm::DocumentSettingsElt_strategy)
def test_datadiagrammlxform::documentsettingselt_glueSettings_setter(instance):
    original = instance.glueSettings
    instance.glueSettings = original
    assert instance.glueSettings == original

@given(instance=DatadiagramMLXForm::DocumentSettingsElt_strategy)
def test_datadiagrammlxform::documentsettingselt_snapExtensions_type(instance):
    assert isinstance(instance.snapExtensions, str)


@given(instance=DatadiagramMLXForm::DocumentSettingsElt_strategy)
def test_datadiagrammlxform::documentsettingselt_snapExtensions_setter(instance):
    original = instance.snapExtensions
    instance.snapExtensions = original
    assert instance.snapExtensions == original

@given(instance=DatadiagramMLXForm::CustomProperty_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform::customproperty_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm::CustomProperty)

@given(instance=DatadiagramMLXForm::CustomProperty_strategy)
def test_datadiagrammlxform::customproperty_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=DatadiagramMLXForm::CustomProperty_strategy)
def test_datadiagrammlxform::customproperty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DatadiagramMLXForm::CustomProperty_strategy)
def test_datadiagrammlxform::customproperty_dataType_type(instance):
    assert isinstance(instance.dataType, str)


@given(instance=DatadiagramMLXForm::CustomProperty_strategy)
def test_datadiagrammlxform::customproperty_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original

@given(instance=CustomProperty_strategy)
@settings(max_examples=50)
def test_customproperty_instantiation(instance):
    assert isinstance(instance, CustomProperty)
