####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Enumerations
MonthStringType: Enumeration = Enumeration(
    name="MonthStringType",
    literals={
            EnumerationLiteral(name="Jan"),
			EnumerationLiteral(name="Feb"),
			EnumerationLiteral(name="Mar"),
			EnumerationLiteral(name="Apr"),
			EnumerationLiteral(name="May"),
			EnumerationLiteral(name="Jun"),
			EnumerationLiteral(name="Jul"),
			EnumerationLiteral(name="Aug"),
			EnumerationLiteral(name="Sep"),
			EnumerationLiteral(name="Oct"),
			EnumerationLiteral(name="Nov"),
			EnumerationLiteral(name="Dec")
    }
)

# Classes
bibtexml_ArticleType = Class(name="bibtexml::ArticleType")
bibtexml_BibTeXMLEntriesClass = Class(name="bibtexml::BibTeXMLEntriesClass")
bibtexml_PhdthesisType = Class(name="bibtexml::PhdthesisType")
bibtexml_BookType = Class(name="bibtexml::BookType")
bibtexml_BookletType = Class(name="bibtexml::BookletType")
bibtexml_ManualType = Class(name="bibtexml::ManualType")
bibtexml_TechreportType = Class(name="bibtexml::TechreportType")
bibtexml_MastersthesisType = Class(name="bibtexml::MastersthesisType")
bibtexml_ConferenceType = Class(name="bibtexml::ConferenceType")
bibtexml_InbookType = Class(name="bibtexml::InbookType")
bibtexml_IncollectionType = Class(name="bibtexml::IncollectionType")
bibtexml_ProceedingsType = Class(name="bibtexml::ProceedingsType")
bibtexml_InproceedingsType = Class(name="bibtexml::InproceedingsType")
bibtexml_UnpublishedType = Class(name="bibtexml::UnpublishedType")
bibtexml_MiscType = Class(name="bibtexml::MiscType")
bibtexml_BibTeXMLEntryType = Class(name="bibtexml::BibTeXMLEntryType")
BibTeXMLEntriesClass = Class(name="BibTeXMLEntriesClass")
bibtexml_DocumentRoot = Class(name="bibtexml::DocumentRoot")
bibtexml_EStringToStringMapEntry = Class(name="bibtexml::EStringToStringMapEntry")
bibtexml_FileType = Class(name="bibtexml::FileType")

# bibtexml_ArticleType class attributes and methods
bibtexml_ArticleType_journal: Property = Property(name="journal", type=StringType)
bibtexml_ArticleType_author: Property = Property(name="author", type=StringType)
bibtexml_ArticleType_title: Property = Property(name="title", type=StringType)
bibtexml_ArticleType_note: Property = Property(name="note", type=StringType)
bibtexml_ArticleType_year: Property = Property(name="year", type=StringType)
bibtexml_ArticleType_volume: Property = Property(name="volume", type=StringType)
bibtexml_ArticleType_number: Property = Property(name="number", type=StringType)
bibtexml_ArticleType_pages: Property = Property(name="pages", type=StringType)
bibtexml_ArticleType_month: Property = Property(name="month", type=StringType)
bibtexml_ArticleType_key: Property = Property(name="key", type=StringType)
bibtexml_ArticleType_crossref: Property = Property(name="crossref", type=StringType)
bibtexml_ArticleType_doi: Property = Property(name="doi", type=StringType)
bibtexml_ArticleType_url: Property = Property(name="url", type=StringType)
bibtexml_ArticleType.attributes={bibtexml_ArticleType_key, bibtexml_ArticleType_doi, bibtexml_ArticleType_journal, bibtexml_ArticleType_month, bibtexml_ArticleType_author, bibtexml_ArticleType_note, bibtexml_ArticleType_url, bibtexml_ArticleType_crossref, bibtexml_ArticleType_pages, bibtexml_ArticleType_year, bibtexml_ArticleType_volume, bibtexml_ArticleType_title, bibtexml_ArticleType_number}

# bibtexml_BibTeXMLEntriesClass class attributes and methods

# bibtexml_PhdthesisType class attributes and methods
bibtexml_PhdthesisType_year: Property = Property(name="year", type=StringType)
bibtexml_PhdthesisType_type: Property = Property(name="type", type=StringType)
bibtexml_PhdthesisType_author: Property = Property(name="author", type=StringType)
bibtexml_PhdthesisType_title: Property = Property(name="title", type=StringType)
bibtexml_PhdthesisType_school: Property = Property(name="school", type=StringType)
bibtexml_PhdthesisType_doi: Property = Property(name="doi", type=StringType)
bibtexml_PhdthesisType_url: Property = Property(name="url", type=StringType)
bibtexml_PhdthesisType_address: Property = Property(name="address", type=StringType)
bibtexml_PhdthesisType_month: Property = Property(name="month", type=StringType)
bibtexml_PhdthesisType_note: Property = Property(name="note", type=StringType)
bibtexml_PhdthesisType_key: Property = Property(name="key", type=StringType)
bibtexml_PhdthesisType_crossref: Property = Property(name="crossref", type=StringType)
bibtexml_PhdthesisType.attributes={bibtexml_PhdthesisType_year, bibtexml_PhdthesisType_crossref, bibtexml_PhdthesisType_type, bibtexml_PhdthesisType_title, bibtexml_PhdthesisType_key, bibtexml_PhdthesisType_author, bibtexml_PhdthesisType_note, bibtexml_PhdthesisType_address, bibtexml_PhdthesisType_school, bibtexml_PhdthesisType_url, bibtexml_PhdthesisType_month, bibtexml_PhdthesisType_doi}

# bibtexml_BookType class attributes and methods
bibtexml_BookType_title: Property = Property(name="title", type=StringType)
bibtexml_BookType_author: Property = Property(name="author", type=StringType)
bibtexml_BookType_editor: Property = Property(name="editor", type=StringType)
bibtexml_BookType_address: Property = Property(name="address", type=StringType)
bibtexml_BookType_publisher: Property = Property(name="publisher", type=StringType)
bibtexml_BookType_year: Property = Property(name="year", type=StringType)
bibtexml_BookType_volume: Property = Property(name="volume", type=StringType)
bibtexml_BookType_number: Property = Property(name="number", type=StringType)
bibtexml_BookType_series: Property = Property(name="series", type=StringType)
bibtexml_BookType_doi: Property = Property(name="doi", type=StringType)
bibtexml_BookType_url: Property = Property(name="url", type=StringType)
bibtexml_BookType_edition: Property = Property(name="edition", type=StringType)
bibtexml_BookType_month: Property = Property(name="month", type=StringType)
bibtexml_BookType_note: Property = Property(name="note", type=StringType)
bibtexml_BookType_key: Property = Property(name="key", type=StringType)
bibtexml_BookType_crossref: Property = Property(name="crossref", type=StringType)
bibtexml_BookType.attributes={bibtexml_BookType_title, bibtexml_BookType_year, bibtexml_BookType_doi, bibtexml_BookType_author, bibtexml_BookType_publisher, bibtexml_BookType_url, bibtexml_BookType_address, bibtexml_BookType_number, bibtexml_BookType_series, bibtexml_BookType_key, bibtexml_BookType_volume, bibtexml_BookType_edition, bibtexml_BookType_note, bibtexml_BookType_month, bibtexml_BookType_crossref, bibtexml_BookType_editor}

# bibtexml_BookletType class attributes and methods
bibtexml_BookletType_author: Property = Property(name="author", type=StringType)
bibtexml_BookletType_title: Property = Property(name="title", type=StringType)
bibtexml_BookletType_key: Property = Property(name="key", type=StringType)
bibtexml_BookletType_howpublished: Property = Property(name="howpublished", type=StringType)
bibtexml_BookletType_address: Property = Property(name="address", type=StringType)
bibtexml_BookletType_month: Property = Property(name="month", type=StringType)
bibtexml_BookletType_year: Property = Property(name="year", type=StringType)
bibtexml_BookletType_note: Property = Property(name="note", type=StringType)
bibtexml_BookletType_crossref: Property = Property(name="crossref", type=StringType)
bibtexml_BookletType_doi: Property = Property(name="doi", type=StringType)
bibtexml_BookletType_url: Property = Property(name="url", type=StringType)
bibtexml_BookletType.attributes={bibtexml_BookletType_title, bibtexml_BookletType_key, bibtexml_BookletType_url, bibtexml_BookletType_address, bibtexml_BookletType_year, bibtexml_BookletType_month, bibtexml_BookletType_note, bibtexml_BookletType_doi, bibtexml_BookletType_crossref, bibtexml_BookletType_howpublished, bibtexml_BookletType_author}

# bibtexml_ManualType class attributes and methods
bibtexml_ManualType_title: Property = Property(name="title", type=StringType)
bibtexml_ManualType_author: Property = Property(name="author", type=StringType)
bibtexml_ManualType_month: Property = Property(name="month", type=StringType)
bibtexml_ManualType_organization: Property = Property(name="organization", type=StringType)
bibtexml_ManualType_address: Property = Property(name="address", type=StringType)
bibtexml_ManualType_edition: Property = Property(name="edition", type=StringType)
bibtexml_ManualType_year: Property = Property(name="year", type=StringType)
bibtexml_ManualType_note: Property = Property(name="note", type=StringType)
bibtexml_ManualType_key: Property = Property(name="key", type=StringType)
bibtexml_ManualType_crossref: Property = Property(name="crossref", type=StringType)
bibtexml_ManualType_doi: Property = Property(name="doi", type=StringType)
bibtexml_ManualType_url: Property = Property(name="url", type=StringType)
bibtexml_ManualType.attributes={bibtexml_ManualType_crossref, bibtexml_ManualType_note, bibtexml_ManualType_month, bibtexml_ManualType_year, bibtexml_ManualType_author, bibtexml_ManualType_edition, bibtexml_ManualType_address, bibtexml_ManualType_doi, bibtexml_ManualType_title, bibtexml_ManualType_url, bibtexml_ManualType_organization, bibtexml_ManualType_key}

# bibtexml_TechreportType class attributes and methods
bibtexml_TechreportType_institution: Property = Property(name="institution", type=StringType)
bibtexml_TechreportType_year: Property = Property(name="year", type=StringType)
bibtexml_TechreportType_type: Property = Property(name="type", type=StringType)
bibtexml_TechreportType_author: Property = Property(name="author", type=StringType)
bibtexml_TechreportType_title: Property = Property(name="title", type=StringType)
bibtexml_TechreportType_key: Property = Property(name="key", type=StringType)
bibtexml_TechreportType_crossref: Property = Property(name="crossref", type=StringType)
bibtexml_TechreportType_doi: Property = Property(name="doi", type=StringType)
bibtexml_TechreportType_number: Property = Property(name="number", type=StringType)
bibtexml_TechreportType_address: Property = Property(name="address", type=StringType)
bibtexml_TechreportType_month: Property = Property(name="month", type=StringType)
bibtexml_TechreportType_note: Property = Property(name="note", type=StringType)
bibtexml_TechreportType_url: Property = Property(name="url", type=StringType)
bibtexml_TechreportType.attributes={bibtexml_TechreportType_doi, bibtexml_TechreportType_crossref, bibtexml_TechreportType_title, bibtexml_TechreportType_key, bibtexml_TechreportType_address, bibtexml_TechreportType_month, bibtexml_TechreportType_institution, bibtexml_TechreportType_type, bibtexml_TechreportType_url, bibtexml_TechreportType_note, bibtexml_TechreportType_author, bibtexml_TechreportType_number, bibtexml_TechreportType_year}

# bibtexml_MastersthesisType class attributes and methods
bibtexml_MastersthesisType_author: Property = Property(name="author", type=StringType)
bibtexml_MastersthesisType_title: Property = Property(name="title", type=StringType)
bibtexml_MastersthesisType_school: Property = Property(name="school", type=StringType)
bibtexml_MastersthesisType_year: Property = Property(name="year", type=StringType)
bibtexml_MastersthesisType_type: Property = Property(name="type", type=StringType)
bibtexml_MastersthesisType_address: Property = Property(name="address", type=StringType)
bibtexml_MastersthesisType_month: Property = Property(name="month", type=StringType)
bibtexml_MastersthesisType_note: Property = Property(name="note", type=StringType)
bibtexml_MastersthesisType_key: Property = Property(name="key", type=StringType)
bibtexml_MastersthesisType_crossref: Property = Property(name="crossref", type=StringType)
bibtexml_MastersthesisType_doi: Property = Property(name="doi", type=StringType)
bibtexml_MastersthesisType_url: Property = Property(name="url", type=StringType)
bibtexml_MastersthesisType.attributes={bibtexml_MastersthesisType_author, bibtexml_MastersthesisType_school, bibtexml_MastersthesisType_doi, bibtexml_MastersthesisType_year, bibtexml_MastersthesisType_url, bibtexml_MastersthesisType_title, bibtexml_MastersthesisType_type, bibtexml_MastersthesisType_month, bibtexml_MastersthesisType_key, bibtexml_MastersthesisType_note, bibtexml_MastersthesisType_address, bibtexml_MastersthesisType_crossref}

# bibtexml_ConferenceType class attributes and methods
bibtexml_ConferenceType_author: Property = Property(name="author", type=StringType)
bibtexml_ConferenceType_title: Property = Property(name="title", type=StringType)
bibtexml_ConferenceType_year: Property = Property(name="year", type=StringType)
bibtexml_ConferenceType_editor: Property = Property(name="editor", type=StringType)
bibtexml_ConferenceType_volume: Property = Property(name="volume", type=StringType)
bibtexml_ConferenceType_number: Property = Property(name="number", type=StringType)
bibtexml_ConferenceType_series: Property = Property(name="series", type=StringType)
bibtexml_ConferenceType_booktitle: Property = Property(name="booktitle", type=StringType)
bibtexml_ConferenceType_month: Property = Property(name="month", type=StringType)
bibtexml_ConferenceType_organization: Property = Property(name="organization", type=StringType)
bibtexml_ConferenceType_publisher: Property = Property(name="publisher", type=StringType)
bibtexml_ConferenceType_note: Property = Property(name="note", type=StringType)
bibtexml_ConferenceType_pages: Property = Property(name="pages", type=StringType)
bibtexml_ConferenceType_address: Property = Property(name="address", type=StringType)
bibtexml_ConferenceType_doi: Property = Property(name="doi", type=StringType)
bibtexml_ConferenceType_url: Property = Property(name="url", type=StringType)
bibtexml_ConferenceType_key: Property = Property(name="key", type=StringType)
bibtexml_ConferenceType_crossref: Property = Property(name="crossref", type=StringType)
bibtexml_ConferenceType.attributes={bibtexml_ConferenceType_volume, bibtexml_ConferenceType_organization, bibtexml_ConferenceType_note, bibtexml_ConferenceType_year, bibtexml_ConferenceType_title, bibtexml_ConferenceType_number, bibtexml_ConferenceType_url, bibtexml_ConferenceType_address, bibtexml_ConferenceType_pages, bibtexml_ConferenceType_month, bibtexml_ConferenceType_doi, bibtexml_ConferenceType_author, bibtexml_ConferenceType_crossref, bibtexml_ConferenceType_publisher, bibtexml_ConferenceType_key, bibtexml_ConferenceType_booktitle, bibtexml_ConferenceType_series, bibtexml_ConferenceType_editor}

# bibtexml_InbookType class attributes and methods
bibtexml_InbookType_chapter: Property = Property(name="chapter", type=StringType)
bibtexml_InbookType_author: Property = Property(name="author", type=StringType)
bibtexml_InbookType_editor: Property = Property(name="editor", type=StringType)
bibtexml_InbookType_title: Property = Property(name="title", type=StringType)
bibtexml_InbookType_number: Property = Property(name="number", type=StringType)
bibtexml_InbookType_pages: Property = Property(name="pages", type=StringType)
bibtexml_InbookType_pages1: Property = Property(name="pages1", type=StringType)
bibtexml_InbookType_publisher: Property = Property(name="publisher", type=StringType)
bibtexml_InbookType_year: Property = Property(name="year", type=StringType)
bibtexml_InbookType_volume: Property = Property(name="volume", type=StringType)
bibtexml_InbookType_month: Property = Property(name="month", type=StringType)
bibtexml_InbookType_series: Property = Property(name="series", type=StringType)
bibtexml_InbookType_type: Property = Property(name="type", type=StringType)
bibtexml_InbookType_address: Property = Property(name="address", type=StringType)
bibtexml_InbookType_edition: Property = Property(name="edition", type=StringType)
bibtexml_InbookType_crossref: Property = Property(name="crossref", type=StringType)
bibtexml_InbookType_doi: Property = Property(name="doi", type=StringType)
bibtexml_InbookType_note: Property = Property(name="note", type=StringType)
bibtexml_InbookType_key: Property = Property(name="key", type=StringType)
bibtexml_InbookType_url: Property = Property(name="url", type=StringType)
bibtexml_InbookType.attributes={bibtexml_InbookType_chapter, bibtexml_InbookType_volume, bibtexml_InbookType_editor, bibtexml_InbookType_edition, bibtexml_InbookType_year, bibtexml_InbookType_note, bibtexml_InbookType_crossref, bibtexml_InbookType_series, bibtexml_InbookType_title, bibtexml_InbookType_type, bibtexml_InbookType_author, bibtexml_InbookType_publisher, bibtexml_InbookType_pages, bibtexml_InbookType_key, bibtexml_InbookType_month, bibtexml_InbookType_number, bibtexml_InbookType_pages1, bibtexml_InbookType_address, bibtexml_InbookType_url, bibtexml_InbookType_doi}

# bibtexml_IncollectionType class attributes and methods
bibtexml_IncollectionType_title: Property = Property(name="title", type=StringType)
bibtexml_IncollectionType_author: Property = Property(name="author", type=StringType)
bibtexml_IncollectionType_editor: Property = Property(name="editor", type=StringType)
bibtexml_IncollectionType_booktitle: Property = Property(name="booktitle", type=StringType)
bibtexml_IncollectionType_publisher: Property = Property(name="publisher", type=StringType)
bibtexml_IncollectionType_year: Property = Property(name="year", type=StringType)
bibtexml_IncollectionType_type: Property = Property(name="type", type=StringType)
bibtexml_IncollectionType_volume: Property = Property(name="volume", type=StringType)
bibtexml_IncollectionType_number: Property = Property(name="number", type=StringType)
bibtexml_IncollectionType_series: Property = Property(name="series", type=StringType)
bibtexml_IncollectionType_edition: Property = Property(name="edition", type=StringType)
bibtexml_IncollectionType_chapter: Property = Property(name="chapter", type=StringType)
bibtexml_IncollectionType_pages: Property = Property(name="pages", type=StringType)
bibtexml_IncollectionType_address: Property = Property(name="address", type=StringType)
bibtexml_IncollectionType_crossref: Property = Property(name="crossref", type=StringType)
bibtexml_IncollectionType_month: Property = Property(name="month", type=StringType)
bibtexml_IncollectionType_note: Property = Property(name="note", type=StringType)
bibtexml_IncollectionType_key: Property = Property(name="key", type=StringType)
bibtexml_IncollectionType_doi: Property = Property(name="doi", type=StringType)
bibtexml_IncollectionType_url: Property = Property(name="url", type=StringType)
bibtexml_IncollectionType.attributes={bibtexml_IncollectionType_title, bibtexml_IncollectionType_booktitle, bibtexml_IncollectionType_key, bibtexml_IncollectionType_author, bibtexml_IncollectionType_note, bibtexml_IncollectionType_month, bibtexml_IncollectionType_edition, bibtexml_IncollectionType_crossref, bibtexml_IncollectionType_address, bibtexml_IncollectionType_pages, bibtexml_IncollectionType_type, bibtexml_IncollectionType_chapter, bibtexml_IncollectionType_editor, bibtexml_IncollectionType_year, bibtexml_IncollectionType_doi, bibtexml_IncollectionType_url, bibtexml_IncollectionType_volume, bibtexml_IncollectionType_publisher, bibtexml_IncollectionType_number, bibtexml_IncollectionType_series}

# bibtexml_ProceedingsType class attributes and methods
bibtexml_ProceedingsType_number: Property = Property(name="number", type=StringType)
bibtexml_ProceedingsType_series: Property = Property(name="series", type=StringType)
bibtexml_ProceedingsType_editor: Property = Property(name="editor", type=StringType)
bibtexml_ProceedingsType_title: Property = Property(name="title", type=StringType)
bibtexml_ProceedingsType_year: Property = Property(name="year", type=StringType)
bibtexml_ProceedingsType_volume: Property = Property(name="volume", type=StringType)
bibtexml_ProceedingsType_key: Property = Property(name="key", type=StringType)
bibtexml_ProceedingsType_crossref: Property = Property(name="crossref", type=StringType)
bibtexml_ProceedingsType_address: Property = Property(name="address", type=StringType)
bibtexml_ProceedingsType_month: Property = Property(name="month", type=StringType)
bibtexml_ProceedingsType_organization: Property = Property(name="organization", type=StringType)
bibtexml_ProceedingsType_publisher: Property = Property(name="publisher", type=StringType)
bibtexml_ProceedingsType_note: Property = Property(name="note", type=StringType)
bibtexml_ProceedingsType_doi: Property = Property(name="doi", type=StringType)
bibtexml_ProceedingsType_url: Property = Property(name="url", type=StringType)
bibtexml_ProceedingsType.attributes={bibtexml_ProceedingsType_crossref, bibtexml_ProceedingsType_organization, bibtexml_ProceedingsType_publisher, bibtexml_ProceedingsType_month, bibtexml_ProceedingsType_note, bibtexml_ProceedingsType_url, bibtexml_ProceedingsType_editor, bibtexml_ProceedingsType_series, bibtexml_ProceedingsType_address, bibtexml_ProceedingsType_volume, bibtexml_ProceedingsType_key, bibtexml_ProceedingsType_title, bibtexml_ProceedingsType_doi, bibtexml_ProceedingsType_number, bibtexml_ProceedingsType_year}

# bibtexml_InproceedingsType class attributes and methods
bibtexml_InproceedingsType_author: Property = Property(name="author", type=StringType)
bibtexml_InproceedingsType_editor: Property = Property(name="editor", type=StringType)
bibtexml_InproceedingsType_title: Property = Property(name="title", type=StringType)
bibtexml_InproceedingsType_booktitle: Property = Property(name="booktitle", type=StringType)
bibtexml_InproceedingsType_year: Property = Property(name="year", type=StringType)
bibtexml_InproceedingsType_pages: Property = Property(name="pages", type=StringType)
bibtexml_InproceedingsType_volume: Property = Property(name="volume", type=StringType)
bibtexml_InproceedingsType_number: Property = Property(name="number", type=StringType)
bibtexml_InproceedingsType_series: Property = Property(name="series", type=StringType)
bibtexml_InproceedingsType_publisher: Property = Property(name="publisher", type=StringType)
bibtexml_InproceedingsType_address: Property = Property(name="address", type=StringType)
bibtexml_InproceedingsType_month: Property = Property(name="month", type=StringType)
bibtexml_InproceedingsType_organization: Property = Property(name="organization", type=StringType)
bibtexml_InproceedingsType_doi: Property = Property(name="doi", type=StringType)
bibtexml_InproceedingsType_note: Property = Property(name="note", type=StringType)
bibtexml_InproceedingsType_key: Property = Property(name="key", type=StringType)
bibtexml_InproceedingsType_crossref: Property = Property(name="crossref", type=StringType)
bibtexml_InproceedingsType_url: Property = Property(name="url", type=StringType)
bibtexml_InproceedingsType.attributes={bibtexml_InproceedingsType_number, bibtexml_InproceedingsType_note, bibtexml_InproceedingsType_key, bibtexml_InproceedingsType_series, bibtexml_InproceedingsType_address, bibtexml_InproceedingsType_publisher, bibtexml_InproceedingsType_volume, bibtexml_InproceedingsType_organization, bibtexml_InproceedingsType_title, bibtexml_InproceedingsType_doi, bibtexml_InproceedingsType_author, bibtexml_InproceedingsType_month, bibtexml_InproceedingsType_url, bibtexml_InproceedingsType_year, bibtexml_InproceedingsType_crossref, bibtexml_InproceedingsType_booktitle, bibtexml_InproceedingsType_editor, bibtexml_InproceedingsType_pages}

# bibtexml_UnpublishedType class attributes and methods
bibtexml_UnpublishedType_note: Property = Property(name="note", type=StringType)
bibtexml_UnpublishedType_month: Property = Property(name="month", type=StringType)
bibtexml_UnpublishedType_year: Property = Property(name="year", type=StringType)
bibtexml_UnpublishedType_author: Property = Property(name="author", type=StringType)
bibtexml_UnpublishedType_title: Property = Property(name="title", type=StringType)
bibtexml_UnpublishedType_key: Property = Property(name="key", type=StringType)
bibtexml_UnpublishedType_crossref: Property = Property(name="crossref", type=StringType)
bibtexml_UnpublishedType_doi: Property = Property(name="doi", type=StringType)
bibtexml_UnpublishedType_url: Property = Property(name="url", type=StringType)
bibtexml_UnpublishedType.attributes={bibtexml_UnpublishedType_year, bibtexml_UnpublishedType_doi, bibtexml_UnpublishedType_key, bibtexml_UnpublishedType_crossref, bibtexml_UnpublishedType_url, bibtexml_UnpublishedType_note, bibtexml_UnpublishedType_author, bibtexml_UnpublishedType_month, bibtexml_UnpublishedType_title}

# bibtexml_MiscType class attributes and methods
bibtexml_MiscType_author: Property = Property(name="author", type=StringType)
bibtexml_MiscType_title: Property = Property(name="title", type=StringType)
bibtexml_MiscType_howpublished: Property = Property(name="howpublished", type=StringType)
bibtexml_MiscType_url: Property = Property(name="url", type=StringType)
bibtexml_MiscType_month: Property = Property(name="month", type=StringType)
bibtexml_MiscType_year: Property = Property(name="year", type=StringType)
bibtexml_MiscType_note: Property = Property(name="note", type=StringType)
bibtexml_MiscType_key: Property = Property(name="key", type=StringType)
bibtexml_MiscType_crossref: Property = Property(name="crossref", type=StringType)
bibtexml_MiscType_doi: Property = Property(name="doi", type=StringType)
bibtexml_MiscType.attributes={bibtexml_MiscType_title, bibtexml_MiscType_crossref, bibtexml_MiscType_url, bibtexml_MiscType_note, bibtexml_MiscType_author, bibtexml_MiscType_howpublished, bibtexml_MiscType_doi, bibtexml_MiscType_month, bibtexml_MiscType_year, bibtexml_MiscType_key}

# bibtexml_BibTeXMLEntryType class attributes and methods
bibtexml_BibTeXMLEntryType_id: Property = Property(name="id", type=StringType)
bibtexml_BibTeXMLEntryType.attributes={bibtexml_BibTeXMLEntryType_id}

# BibTeXMLEntriesClass class attributes and methods

# bibtexml_DocumentRoot class attributes and methods
bibtexml_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
bibtexml_DocumentRoot_address: Property = Property(name="address", type=StringType)
bibtexml_DocumentRoot_annote: Property = Property(name="annote", type=StringType)
bibtexml_DocumentRoot_author: Property = Property(name="author", type=StringType)
bibtexml_DocumentRoot_booktitle: Property = Property(name="booktitle", type=StringType)
bibtexml_DocumentRoot_chapter: Property = Property(name="chapter", type=StringType)
bibtexml_DocumentRoot_edition: Property = Property(name="edition", type=StringType)
bibtexml_DocumentRoot_editor: Property = Property(name="editor", type=StringType)
bibtexml_DocumentRoot_crossref: Property = Property(name="crossref", type=StringType)
bibtexml_DocumentRoot_doi: Property = Property(name="doi", type=StringType)
bibtexml_DocumentRoot_institution: Property = Property(name="institution", type=StringType)
bibtexml_DocumentRoot_howpublished: Property = Property(name="howpublished", type=StringType)
bibtexml_DocumentRoot_key: Property = Property(name="key", type=StringType)
bibtexml_DocumentRoot_journal: Property = Property(name="journal", type=StringType)
bibtexml_DocumentRoot_note: Property = Property(name="note", type=StringType)
bibtexml_DocumentRoot_number: Property = Property(name="number", type=StringType)
bibtexml_DocumentRoot_organization: Property = Property(name="organization", type=StringType)
bibtexml_DocumentRoot_pages: Property = Property(name="pages", type=StringType)
bibtexml_DocumentRoot_month: Property = Property(name="month", type=StringType)
bibtexml_DocumentRoot_publisher: Property = Property(name="publisher", type=StringType)
bibtexml_DocumentRoot_school: Property = Property(name="school", type=StringType)
bibtexml_DocumentRoot_series: Property = Property(name="series", type=StringType)
bibtexml_DocumentRoot_type: Property = Property(name="type", type=StringType)
bibtexml_DocumentRoot_url: Property = Property(name="url", type=StringType)
bibtexml_DocumentRoot_volume: Property = Property(name="volume", type=StringType)
bibtexml_DocumentRoot_title: Property = Property(name="title", type=StringType)
bibtexml_DocumentRoot_year: Property = Property(name="year", type=StringType)
bibtexml_DocumentRoot.attributes={bibtexml_DocumentRoot_edition, bibtexml_DocumentRoot_school, bibtexml_DocumentRoot_journal, bibtexml_DocumentRoot_month, bibtexml_DocumentRoot_author, bibtexml_DocumentRoot_crossref, bibtexml_DocumentRoot_mixed, bibtexml_DocumentRoot_number, bibtexml_DocumentRoot_year, bibtexml_DocumentRoot_title, bibtexml_DocumentRoot_doi, bibtexml_DocumentRoot_howpublished, bibtexml_DocumentRoot_chapter, bibtexml_DocumentRoot_annote, bibtexml_DocumentRoot_pages, bibtexml_DocumentRoot_institution, bibtexml_DocumentRoot_url, bibtexml_DocumentRoot_organization, bibtexml_DocumentRoot_booktitle, bibtexml_DocumentRoot_key, bibtexml_DocumentRoot_address, bibtexml_DocumentRoot_editor, bibtexml_DocumentRoot_publisher, bibtexml_DocumentRoot_type, bibtexml_DocumentRoot_note, bibtexml_DocumentRoot_volume, bibtexml_DocumentRoot_series}

# bibtexml_EStringToStringMapEntry class attributes and methods

# bibtexml_FileType class attributes and methods

# Relationships
article0: BinaryAssociation = BinaryAssociation(
    name="article0",
    ends={
        Property(name="bibtexml_ArticleType", type=bibtexml_BibTeXMLEntriesClass, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtexml_BibTeXMLEntriesClass", type=bibtexml_ArticleType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
phdthesis11: BinaryAssociation = BinaryAssociation(
    name="phdthesis11",
    ends={
        Property(name="bibtexml_PhdthesisType", type=bibtexml_BibTeXMLEntriesClass, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtexml_BibTeXMLEntriesClass12", type=bibtexml_PhdthesisType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
book1: BinaryAssociation = BinaryAssociation(
    name="book1",
    ends={
        Property(name="bibtexml_BookType", type=bibtexml_BibTeXMLEntriesClass, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtexml_BibTeXMLEntriesClass2", type=bibtexml_BookType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
booklet3: BinaryAssociation = BinaryAssociation(
    name="booklet3",
    ends={
        Property(name="bibtexml_BookletType", type=bibtexml_BibTeXMLEntriesClass, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtexml_BibTeXMLEntriesClass4", type=bibtexml_BookletType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
manual5: BinaryAssociation = BinaryAssociation(
    name="manual5",
    ends={
        Property(name="bibtexml_ManualType", type=bibtexml_BibTeXMLEntriesClass, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtexml_BibTeXMLEntriesClass6", type=bibtexml_ManualType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
techreport7: BinaryAssociation = BinaryAssociation(
    name="techreport7",
    ends={
        Property(name="bibtexml_TechreportType", type=bibtexml_BibTeXMLEntriesClass, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtexml_BibTeXMLEntriesClass8", type=bibtexml_TechreportType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mastersthesis9: BinaryAssociation = BinaryAssociation(
    name="mastersthesis9",
    ends={
        Property(name="bibtexml_MastersthesisType", type=bibtexml_BibTeXMLEntriesClass, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtexml_BibTeXMLEntriesClass10", type=bibtexml_MastersthesisType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conference21: BinaryAssociation = BinaryAssociation(
    name="conference21",
    ends={
        Property(name="bibtexml_ConferenceType", type=bibtexml_BibTeXMLEntriesClass, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtexml_BibTeXMLEntriesClass22", type=bibtexml_ConferenceType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inbook13: BinaryAssociation = BinaryAssociation(
    name="inbook13",
    ends={
        Property(name="bibtexml_InbookType", type=bibtexml_BibTeXMLEntriesClass, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtexml_BibTeXMLEntriesClass14", type=bibtexml_InbookType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
incollection15: BinaryAssociation = BinaryAssociation(
    name="incollection15",
    ends={
        Property(name="bibtexml_IncollectionType", type=bibtexml_BibTeXMLEntriesClass, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtexml_BibTeXMLEntriesClass16", type=bibtexml_IncollectionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
proceedings17: BinaryAssociation = BinaryAssociation(
    name="proceedings17",
    ends={
        Property(name="bibtexml_ProceedingsType", type=bibtexml_BibTeXMLEntriesClass, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtexml_BibTeXMLEntriesClass18", type=bibtexml_ProceedingsType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inproceedings19: BinaryAssociation = BinaryAssociation(
    name="inproceedings19",
    ends={
        Property(name="bibtexml_InproceedingsType", type=bibtexml_BibTeXMLEntriesClass, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtexml_BibTeXMLEntriesClass20", type=bibtexml_InproceedingsType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unpublished23: BinaryAssociation = BinaryAssociation(
    name="unpublished23",
    ends={
        Property(name="bibtexml_UnpublishedType", type=bibtexml_BibTeXMLEntriesClass, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtexml_BibTeXMLEntriesClass24", type=bibtexml_UnpublishedType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
misc25: BinaryAssociation = BinaryAssociation(
    name="misc25",
    ends={
        Property(name="bibtexml_MiscType", type=bibtexml_BibTeXMLEntriesClass, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtexml_BibTeXMLEntriesClass26", type=bibtexml_MiscType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
xMLNSPrefixMap27: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap27",
    ends={
        Property(name="bibtexml_EStringToStringMapEntry", type=bibtexml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtexml_DocumentRoot", type=bibtexml_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
article31: BinaryAssociation = BinaryAssociation(
    name="article31",
    ends={
        Property(name="bibtexml_ArticleType33", type=bibtexml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtexml_DocumentRoot32", type=bibtexml_ArticleType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation28: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation28",
    ends={
        Property(name="bibtexml_EStringToStringMapEntry30", type=bibtexml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtexml_DocumentRoot29", type=bibtexml_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
booklet37: BinaryAssociation = BinaryAssociation(
    name="booklet37",
    ends={
        Property(name="bibtexml_BookletType39", type=bibtexml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtexml_DocumentRoot38", type=bibtexml_BookletType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conference40: BinaryAssociation = BinaryAssociation(
    name="conference40",
    ends={
        Property(name="bibtexml_ConferenceType42", type=bibtexml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtexml_DocumentRoot41", type=bibtexml_ConferenceType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
book34: BinaryAssociation = BinaryAssociation(
    name="book34",
    ends={
        Property(name="bibtexml_BookType36", type=bibtexml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtexml_DocumentRoot35", type=bibtexml_BookType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entry43: BinaryAssociation = BinaryAssociation(
    name="entry43",
    ends={
        Property(name="bibtexml_BibTeXMLEntryType", type=bibtexml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtexml_DocumentRoot44", type=bibtexml_BibTeXMLEntryType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inbook47: BinaryAssociation = BinaryAssociation(
    name="inbook47",
    ends={
        Property(name="bibtexml_InbookType49", type=bibtexml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtexml_DocumentRoot48", type=bibtexml_InbookType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incollection50: BinaryAssociation = BinaryAssociation(
    name="incollection50",
    ends={
        Property(name="bibtexml_IncollectionType52", type=bibtexml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtexml_DocumentRoot51", type=bibtexml_IncollectionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inproceedings53: BinaryAssociation = BinaryAssociation(
    name="inproceedings53",
    ends={
        Property(name="bibtexml_InproceedingsType55", type=bibtexml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtexml_DocumentRoot54", type=bibtexml_InproceedingsType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
file45: BinaryAssociation = BinaryAssociation(
    name="file45",
    ends={
        Property(name="bibtexml_FileType", type=bibtexml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtexml_DocumentRoot46", type=bibtexml_FileType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
manual56: BinaryAssociation = BinaryAssociation(
    name="manual56",
    ends={
        Property(name="bibtexml_ManualType58", type=bibtexml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtexml_DocumentRoot57", type=bibtexml_ManualType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mastersthesis59: BinaryAssociation = BinaryAssociation(
    name="mastersthesis59",
    ends={
        Property(name="bibtexml_MastersthesisType61", type=bibtexml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtexml_DocumentRoot60", type=bibtexml_MastersthesisType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
misc62: BinaryAssociation = BinaryAssociation(
    name="misc62",
    ends={
        Property(name="bibtexml_MiscType64", type=bibtexml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtexml_DocumentRoot63", type=bibtexml_MiscType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
phdthesis65: BinaryAssociation = BinaryAssociation(
    name="phdthesis65",
    ends={
        Property(name="bibtexml_PhdthesisType67", type=bibtexml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtexml_DocumentRoot66", type=bibtexml_PhdthesisType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
proceedings68: BinaryAssociation = BinaryAssociation(
    name="proceedings68",
    ends={
        Property(name="bibtexml_ProceedingsType70", type=bibtexml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtexml_DocumentRoot69", type=bibtexml_ProceedingsType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unpublished74: BinaryAssociation = BinaryAssociation(
    name="unpublished74",
    ends={
        Property(name="bibtexml_UnpublishedType76", type=bibtexml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtexml_DocumentRoot75", type=bibtexml_UnpublishedType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
techreport71: BinaryAssociation = BinaryAssociation(
    name="techreport71",
    ends={
        Property(name="bibtexml_TechreportType73", type=bibtexml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtexml_DocumentRoot72", type=bibtexml_TechreportType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entry77: BinaryAssociation = BinaryAssociation(
    name="entry77",
    ends={
        Property(name="bibtexml_BibTeXMLEntryType79", type=bibtexml_FileType, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtexml_FileType78", type=bibtexml_BibTeXMLEntryType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_bibtexml_BibTeXMLEntryType_BibTeXMLEntriesClass = Generalization(general=BibTeXMLEntriesClass, specific=bibtexml_BibTeXMLEntryType)

# Domain Model
domain_model = DomainModel(
    name="bibtexml",
    types={bibtexml_ArticleType, bibtexml_BibTeXMLEntriesClass, bibtexml_PhdthesisType, bibtexml_BookType, bibtexml_BookletType, bibtexml_ManualType, bibtexml_TechreportType, bibtexml_MastersthesisType, bibtexml_ConferenceType, bibtexml_InbookType, bibtexml_IncollectionType, bibtexml_ProceedingsType, bibtexml_InproceedingsType, bibtexml_UnpublishedType, bibtexml_MiscType, bibtexml_BibTeXMLEntryType, BibTeXMLEntriesClass, bibtexml_DocumentRoot, bibtexml_EStringToStringMapEntry, bibtexml_FileType, MonthStringType},
    associations={article0, phdthesis11, book1, booklet3, manual5, techreport7, mastersthesis9, conference21, inbook13, incollection15, proceedings17, inproceedings19, unpublished23, misc25, xMLNSPrefixMap27, article31, xSISchemaLocation28, booklet37, conference40, book34, entry43, inbook47, incollection50, inproceedings53, file45, manual56, mastersthesis59, misc62, phdthesis65, proceedings68, unpublished74, techreport71, entry77},
    generalizations={gen_bibtexml_BibTeXMLEntryType_BibTeXMLEntriesClass},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)