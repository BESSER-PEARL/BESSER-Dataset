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

# Classes
SWRC_Bibliography = Class(name="SWRC_Bibliography")
SWRC_Publication = Class(name="SWRC_Publication", is_abstract=True)
Publication = Class(name="Publication")
SWRC_Book = Class(name="SWRC_Book")
SWRC_Article = Class(name="SWRC_Article")
Person = Class(name="Person")
Organization = Class(name="Organization")
SWRC_InBook = Class(name="SWRC_InBook")
SWRC_Booklet = Class(name="SWRC_Booklet")
SWRC_InCollection = Class(name="SWRC_InCollection")
SWRC_InProceedings = Class(name="SWRC_InProceedings")
SWRC_Proceedings = Class(name="SWRC_Proceedings")
SWRC_Manual = Class(name="SWRC_Manual")
SWRC_Misc = Class(name="SWRC_Misc")
SWRC_Unpublished = Class(name="SWRC_Unpublished")
SWRC_Thesis = Class(name="SWRC_Thesis", is_abstract=True)
University = Class(name="University")
SWRC_MasterThesis = Class(name="SWRC_MasterThesis")
Thesis = Class(name="Thesis")
SWRC_PhDThesis = Class(name="SWRC_PhDThesis")
SWRC_Report = Class(name="SWRC_Report", is_abstract=True)
SWRC_ProjectReport = Class(name="SWRC_ProjectReport")
Report = Class(name="Report")
Project = Class(name="Project")
SWRC_TechnicalReport = Class(name="SWRC_TechnicalReport")
SWRC_Event = Class(name="SWRC_Event")
Event = Class(name="Event")
SWRC_Conference = Class(name="SWRC_Conference")
SWRC_Workshop = Class(name="SWRC_Workshop")
SWRC_Exhibition = Class(name="SWRC_Exhibition")
SWRC_Lecture = Class(name="SWRC_Lecture")
SWRC_Meeting = Class(name="SWRC_Meeting")
SWRC_ProjectMeeting = Class(name="SWRC_ProjectMeeting")
Meeting = Class(name="Meeting")
SWRC_Person = Class(name="SWRC_Person")
SWRC_Employee = Class(name="SWRC_Employee")
SWRC_AcademicStaff = Class(name="SWRC_AcademicStaff")
AcademicStaff = Class(name="AcademicStaff")
SWRC_Manager = Class(name="SWRC_Manager")
Employee = Class(name="Employee")
SWRC_AdministrativeStaff = Class(name="SWRC_AdministrativeStaff")
SWRC_TechnicalStaff = Class(name="SWRC_TechnicalStaff")
ResearchGroup = Class(name="ResearchGroup")
PhDStudent = Class(name="PhDStudent")
ResearchTopic = Class(name="ResearchTopic")
SWRC_Lecturer = Class(name="SWRC_Lecturer")
SWRC_FacultyMember = Class(name="SWRC_FacultyMember")
SWRC_FullProfessor = Class(name="SWRC_FullProfessor")
FacultyMember = Class(name="FacultyMember")
SWRC_AssistantProfessor = Class(name="SWRC_AssistantProfessor")
SWRC_AssociateProfessor = Class(name="SWRC_AssociateProfessor")
SWRC_Student = Class(name="SWRC_Student")
SWRC_Undergraduate = Class(name="SWRC_Undergraduate")
Student = Class(name="Student")
SWRC_Graduate = Class(name="SWRC_Graduate")
SWRC_PhDStudent = Class(name="SWRC_PhDStudent")
Graduate = Class(name="Graduate")
SWRC_Organization = Class(name="SWRC_Organization")
TechnicalReport = Class(name="TechnicalReport")
SWRC_ResearchGroup = Class(name="SWRC_ResearchGroup")
Product = Class(name="Product")
SWRC_Association = Class(name="SWRC_Association")
SWRC_Department = Class(name="SWRC_Department")
Institute = Class(name="Institute")
SWRC_Enterprise = Class(name="SWRC_Enterprise")
SWRC_Institute = Class(name="SWRC_Institute")
SWRC_Project = Class(name="SWRC_Project", is_abstract=True)
SWRC_University = Class(name="SWRC_University")
Department = Class(name="Department")
ProjectReport = Class(name="ProjectReport")
SWRC_Product = Class(name="SWRC_Product")
SWRC_ResearchProject = Class(name="SWRC_ResearchProject")
SWRC_DevelopmentProject = Class(name="SWRC_DevelopmentProject")
SWRC_SoftwareProject = Class(name="SWRC_SoftwareProject")
SWRC_Topic = Class(name="SWRC_Topic")
SWRC_ResearchTopic = Class(name="SWRC_ResearchTopic")
Topic = Class(name="Topic")
SWRC_SoftwareComponent = Class(name="SWRC_SoftwareComponent")

# SWRC_Bibliography class attributes and methods

# SWRC_Publication class attributes and methods
SWRC_Publication_title: Property = Property(name="title", type=StringType)
SWRC_Publication_abstract: Property = Property(name="abstract", type=StringType)
SWRC_Publication_keywords: Property = Property(name="keywords", type=StringType)
SWRC_Publication_note: Property = Property(name="note", type=StringType)
SWRC_Publication_year: Property = Property(name="year", type=StringType)
SWRC_Publication.attributes={SWRC_Publication_keywords, SWRC_Publication_year, SWRC_Publication_title, SWRC_Publication_note, SWRC_Publication_abstract}

# Publication class attributes and methods

# SWRC_Book class attributes and methods
SWRC_Book_address: Property = Property(name="address", type=StringType)
SWRC_Book_month: Property = Property(name="month", type=StringType)
SWRC_Book_number: Property = Property(name="number", type=StringType)
SWRC_Book_volume: Property = Property(name="volume", type=StringType)
SWRC_Book_series: Property = Property(name="series", type=StringType)
SWRC_Book_source: Property = Property(name="source", type=StringType)
SWRC_Book_edition: Property = Property(name="edition", type=StringType)
SWRC_Book_isbn: Property = Property(name="isbn", type=StringType)
SWRC_Book_price: Property = Property(name="price", type=StringType)
SWRC_Book.attributes={SWRC_Book_source, SWRC_Book_address, SWRC_Book_price, SWRC_Book_month, SWRC_Book_edition, SWRC_Book_isbn, SWRC_Book_volume, SWRC_Book_series, SWRC_Book_number}

# SWRC_Article class attributes and methods
SWRC_Article_journal: Property = Property(name="journal", type=StringType)
SWRC_Article_month: Property = Property(name="month", type=StringType)
SWRC_Article_number: Property = Property(name="number", type=StringType)
SWRC_Article_pages: Property = Property(name="pages", type=StringType)
SWRC_Article_volume: Property = Property(name="volume", type=StringType)
SWRC_Article.attributes={SWRC_Article_pages, SWRC_Article_volume, SWRC_Article_month, SWRC_Article_number, SWRC_Article_journal}

# Person class attributes and methods

# Organization class attributes and methods

# SWRC_InBook class attributes and methods
SWRC_InBook_pages: Property = Property(name="pages", type=StringType)
SWRC_InBook_volume: Property = Property(name="volume", type=StringType)
SWRC_InBook_month: Property = Property(name="month", type=StringType)
SWRC_InBook_number: Property = Property(name="number", type=StringType)
SWRC_InBook_series: Property = Property(name="series", type=StringType)
SWRC_InBook_chapter: Property = Property(name="chapter", type=StringType)
SWRC_InBook_type: Property = Property(name="type", type=StringType)
SWRC_InBook_address: Property = Property(name="address", type=StringType)
SWRC_InBook.attributes={SWRC_InBook_chapter, SWRC_InBook_volume, SWRC_InBook_month, SWRC_InBook_type, SWRC_InBook_pages, SWRC_InBook_address, SWRC_InBook_series, SWRC_InBook_number}

# SWRC_Booklet class attributes and methods
SWRC_Booklet_edition: Property = Property(name="edition", type=StringType)
SWRC_Booklet_month: Property = Property(name="month", type=StringType)
SWRC_Booklet_address: Property = Property(name="address", type=StringType)
SWRC_Booklet_howpublished: Property = Property(name="howpublished", type=StringType)
SWRC_Booklet.attributes={SWRC_Booklet_month, SWRC_Booklet_address, SWRC_Booklet_edition, SWRC_Booklet_howpublished}

# SWRC_InCollection class attributes and methods
SWRC_InCollection_month: Property = Property(name="month", type=StringType)
SWRC_InCollection_number: Property = Property(name="number", type=StringType)
SWRC_InCollection_pages: Property = Property(name="pages", type=StringType)
SWRC_InCollection_address: Property = Property(name="address", type=StringType)
SWRC_InCollection_edition: Property = Property(name="edition", type=StringType)
SWRC_InCollection_volume: Property = Property(name="volume", type=StringType)
SWRC_InCollection_series: Property = Property(name="series", type=StringType)
SWRC_InCollection_chapter: Property = Property(name="chapter", type=StringType)
SWRC_InCollection_type: Property = Property(name="type", type=StringType)
SWRC_InCollection_booktitle: Property = Property(name="booktitle", type=StringType)
SWRC_InCollection.attributes={SWRC_InCollection_volume, SWRC_InCollection_chapter, SWRC_InCollection_booktitle, SWRC_InCollection_month, SWRC_InCollection_pages, SWRC_InCollection_series, SWRC_InCollection_edition, SWRC_InCollection_type, SWRC_InCollection_number, SWRC_InCollection_address}

# SWRC_InProceedings class attributes and methods
SWRC_InProceedings_month: Property = Property(name="month", type=StringType)
SWRC_InProceedings_number: Property = Property(name="number", type=StringType)
SWRC_InProceedings_pages: Property = Property(name="pages", type=StringType)
SWRC_InProceedings_address: Property = Property(name="address", type=StringType)
SWRC_InProceedings_volume: Property = Property(name="volume", type=StringType)
SWRC_InProceedings_series: Property = Property(name="series", type=StringType)
SWRC_InProceedings_booktitle: Property = Property(name="booktitle", type=StringType)
SWRC_InProceedings.attributes={SWRC_InProceedings_booktitle, SWRC_InProceedings_number, SWRC_InProceedings_pages, SWRC_InProceedings_volume, SWRC_InProceedings_month, SWRC_InProceedings_series, SWRC_InProceedings_address}

# SWRC_Proceedings class attributes and methods
SWRC_Proceedings_month: Property = Property(name="month", type=StringType)
SWRC_Proceedings_number: Property = Property(name="number", type=StringType)
SWRC_Proceedings_volume: Property = Property(name="volume", type=StringType)
SWRC_Proceedings_address: Property = Property(name="address", type=StringType)
SWRC_Proceedings_series: Property = Property(name="series", type=StringType)
SWRC_Proceedings.attributes={SWRC_Proceedings_volume, SWRC_Proceedings_month, SWRC_Proceedings_number, SWRC_Proceedings_series, SWRC_Proceedings_address}

# SWRC_Manual class attributes and methods
SWRC_Manual_month: Property = Property(name="month", type=StringType)
SWRC_Manual_address: Property = Property(name="address", type=StringType)
SWRC_Manual_edition: Property = Property(name="edition", type=StringType)
SWRC_Manual.attributes={SWRC_Manual_month, SWRC_Manual_address, SWRC_Manual_edition}

# SWRC_Misc class attributes and methods
SWRC_Misc_month: Property = Property(name="month", type=StringType)
SWRC_Misc_howpublished: Property = Property(name="howpublished", type=StringType)
SWRC_Misc.attributes={SWRC_Misc_month, SWRC_Misc_howpublished}

# SWRC_Unpublished class attributes and methods
SWRC_Unpublished_month: Property = Property(name="month", type=StringType)
SWRC_Unpublished.attributes={SWRC_Unpublished_month}

# SWRC_Thesis class attributes and methods
SWRC_Thesis_month: Property = Property(name="month", type=StringType)
SWRC_Thesis_address: Property = Property(name="address", type=StringType)
SWRC_Thesis_type: Property = Property(name="type", type=StringType)
SWRC_Thesis.attributes={SWRC_Thesis_month, SWRC_Thesis_address, SWRC_Thesis_type}

# University class attributes and methods

# SWRC_MasterThesis class attributes and methods

# Thesis class attributes and methods

# SWRC_PhDThesis class attributes and methods

# SWRC_Report class attributes and methods

# SWRC_ProjectReport class attributes and methods

# Report class attributes and methods

# Project class attributes and methods

# SWRC_TechnicalReport class attributes and methods
SWRC_TechnicalReport_series: Property = Property(name="series", type=StringType)
SWRC_TechnicalReport.attributes={SWRC_TechnicalReport_series}

# SWRC_Event class attributes and methods
SWRC_Event_name: Property = Property(name="name", type=StringType)
SWRC_Event_date: Property = Property(name="date", type=StringType)
SWRC_Event_eventTitle: Property = Property(name="eventTitle", type=StringType)
SWRC_Event_location: Property = Property(name="location", type=StringType)
SWRC_Event.attributes={SWRC_Event_eventTitle, SWRC_Event_name, SWRC_Event_location, SWRC_Event_date}

# Event class attributes and methods

# SWRC_Conference class attributes and methods
SWRC_Conference_series: Property = Property(name="series", type=StringType)
SWRC_Conference.attributes={SWRC_Conference_series}

# SWRC_Workshop class attributes and methods
SWRC_Workshop_series: Property = Property(name="series", type=StringType)
SWRC_Workshop.attributes={SWRC_Workshop_series}

# SWRC_Exhibition class attributes and methods

# SWRC_Lecture class attributes and methods

# SWRC_Meeting class attributes and methods
SWRC_Meeting_title: Property = Property(name="title", type=StringType)
SWRC_Meeting.attributes={SWRC_Meeting_title}

# SWRC_ProjectMeeting class attributes and methods

# Meeting class attributes and methods

# SWRC_Person class attributes and methods
SWRC_Person_address: Property = Property(name="address", type=StringType)
SWRC_Person_name: Property = Property(name="name", type=StringType)
SWRC_Person_email: Property = Property(name="email", type=StringType)
SWRC_Person_fax: Property = Property(name="fax", type=StringType)
SWRC_Person_homepage: Property = Property(name="homepage", type=StringType)
SWRC_Person_phone: Property = Property(name="phone", type=StringType)
SWRC_Person_photo: Property = Property(name="photo", type=StringType)
SWRC_Person.attributes={SWRC_Person_name, SWRC_Person_email, SWRC_Person_homepage, SWRC_Person_phone, SWRC_Person_photo, SWRC_Person_address, SWRC_Person_fax}

# SWRC_Employee class attributes and methods

# SWRC_AcademicStaff class attributes and methods

# AcademicStaff class attributes and methods

# SWRC_Manager class attributes and methods

# Employee class attributes and methods

# SWRC_AdministrativeStaff class attributes and methods

# SWRC_TechnicalStaff class attributes and methods

# ResearchGroup class attributes and methods

# PhDStudent class attributes and methods

# ResearchTopic class attributes and methods

# SWRC_Lecturer class attributes and methods

# SWRC_FacultyMember class attributes and methods

# SWRC_FullProfessor class attributes and methods

# FacultyMember class attributes and methods

# SWRC_AssistantProfessor class attributes and methods

# SWRC_AssociateProfessor class attributes and methods

# SWRC_Student class attributes and methods

# SWRC_Undergraduate class attributes and methods

# Student class attributes and methods

# SWRC_Graduate class attributes and methods

# SWRC_PhDStudent class attributes and methods

# Graduate class attributes and methods

# SWRC_Organization class attributes and methods
SWRC_Organization_location: Property = Property(name="location", type=StringType)
SWRC_Organization_name: Property = Property(name="name", type=StringType)
SWRC_Organization.attributes={SWRC_Organization_name, SWRC_Organization_location}

# TechnicalReport class attributes and methods

# SWRC_ResearchGroup class attributes and methods

# Product class attributes and methods

# SWRC_Association class attributes and methods

# SWRC_Department class attributes and methods

# Institute class attributes and methods

# SWRC_Enterprise class attributes and methods

# SWRC_Institute class attributes and methods

# SWRC_Project class attributes and methods
SWRC_Project_name: Property = Property(name="name", type=StringType)
SWRC_Project.attributes={SWRC_Project_name}

# SWRC_University class attributes and methods

# Department class attributes and methods

# ProjectReport class attributes and methods

# SWRC_Product class attributes and methods
SWRC_Product_name: Property = Property(name="name", type=StringType)
SWRC_Product.attributes={SWRC_Product_name}

# SWRC_ResearchProject class attributes and methods

# SWRC_DevelopmentProject class attributes and methods

# SWRC_SoftwareProject class attributes and methods

# SWRC_Topic class attributes and methods
SWRC_Topic_name: Property = Property(name="name", type=StringType)
SWRC_Topic.attributes={SWRC_Topic_name}

# SWRC_ResearchTopic class attributes and methods

# Topic class attributes and methods

# SWRC_SoftwareComponent class attributes and methods
SWRC_SoftwareComponent_hasPrice: Property = Property(name="hasPrice", type=StringType)
SWRC_SoftwareComponent.attributes={SWRC_SoftwareComponent_hasPrice}

# Relationships
publications0: BinaryAssociation = BinaryAssociation(
    name="publications0",
    ends={
        Property(name="SWRC_Bibliography", type=Publication, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="Publication", type=SWRC_Bibliography, multiplicity=Multiplicity(1, 1))
    }
)
author1: BinaryAssociation = BinaryAssociation(
    name="author1",
    ends={
        Property(name="Person", type=SWRC_Article, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_Article", type=Person, multiplicity=Multiplicity(1, 9999))
    }
)
publisher4: BinaryAssociation = BinaryAssociation(
    name="publisher4",
    ends={
        Property(name="Organization", type=SWRC_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_Book5", type=Organization, multiplicity=Multiplicity(1, 1))
    }
)
editor2: BinaryAssociation = BinaryAssociation(
    name="editor2",
    ends={
        Property(name="Person3", type=SWRC_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_Book", type=Person, multiplicity=Multiplicity(1, 1))
    }
)
author6: BinaryAssociation = BinaryAssociation(
    name="author6",
    ends={
        Property(name="Person8", type=SWRC_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_Book7", type=Person, multiplicity=Multiplicity(1, 9999))
    }
)
author9: BinaryAssociation = BinaryAssociation(
    name="author9",
    ends={
        Property(name="Person10", type=SWRC_InBook, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_InBook", type=Person, multiplicity=Multiplicity(1, 9999))
    }
)
publisher11: BinaryAssociation = BinaryAssociation(
    name="publisher11",
    ends={
        Property(name="Organization13", type=SWRC_InBook, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_InBook12", type=Organization, multiplicity=Multiplicity(1, 1))
    }
)
editor14: BinaryAssociation = BinaryAssociation(
    name="editor14",
    ends={
        Property(name="Person16", type=SWRC_InBook, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_InBook15", type=Person, multiplicity=Multiplicity(1, 1))
    }
)
author17: BinaryAssociation = BinaryAssociation(
    name="author17",
    ends={
        Property(name="Person18", type=SWRC_Booklet, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_Booklet", type=Person, multiplicity=Multiplicity(1, 9999))
    }
)
author21: BinaryAssociation = BinaryAssociation(
    name="author21",
    ends={
        Property(name="SWRC_InCollection22", type=Person, multiplicity=Multiplicity(1, 9999)),
        Property(name="Person23", type=SWRC_InCollection, multiplicity=Multiplicity(1, 1))
    }
)
editor19: BinaryAssociation = BinaryAssociation(
    name="editor19",
    ends={
        Property(name="Person20", type=SWRC_InCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_InCollection", type=Person, multiplicity=Multiplicity(1, 1))
    }
)
publisher24: BinaryAssociation = BinaryAssociation(
    name="publisher24",
    ends={
        Property(name="Organization26", type=SWRC_InCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_InCollection25", type=Organization, multiplicity=Multiplicity(1, 1))
    }
)
author29: BinaryAssociation = BinaryAssociation(
    name="author29",
    ends={
        Property(name="Person31", type=SWRC_InProceedings, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_InProceedings30", type=Person, multiplicity=Multiplicity(1, 9999))
    }
)
editor27: BinaryAssociation = BinaryAssociation(
    name="editor27",
    ends={
        Property(name="Person28", type=SWRC_InProceedings, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_InProceedings", type=Person, multiplicity=Multiplicity(1, 1))
    }
)
organization32: BinaryAssociation = BinaryAssociation(
    name="organization32",
    ends={
        Property(name="Organization34", type=SWRC_InProceedings, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_InProceedings33", type=Organization, multiplicity=Multiplicity(1, 1))
    }
)
editor38: BinaryAssociation = BinaryAssociation(
    name="editor38",
    ends={
        Property(name="Person39", type=SWRC_Proceedings, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_Proceedings", type=Person, multiplicity=Multiplicity(1, 1))
    }
)
publisher40: BinaryAssociation = BinaryAssociation(
    name="publisher40",
    ends={
        Property(name="Organization42", type=SWRC_Proceedings, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_Proceedings41", type=Organization, multiplicity=Multiplicity(1, 1))
    }
)
publisher35: BinaryAssociation = BinaryAssociation(
    name="publisher35",
    ends={
        Property(name="Organization37", type=SWRC_InProceedings, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_InProceedings36", type=Organization, multiplicity=Multiplicity(1, 1))
    }
)
organization43: BinaryAssociation = BinaryAssociation(
    name="organization43",
    ends={
        Property(name="Organization45", type=SWRC_Proceedings, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_Proceedings44", type=Organization, multiplicity=Multiplicity(1, 1))
    }
)
author46: BinaryAssociation = BinaryAssociation(
    name="author46",
    ends={
        Property(name="Person47", type=SWRC_Manual, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_Manual", type=Person, multiplicity=Multiplicity(1, 9999))
    }
)
organization48: BinaryAssociation = BinaryAssociation(
    name="organization48",
    ends={
        Property(name="Organization50", type=SWRC_Manual, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_Manual49", type=Organization, multiplicity=Multiplicity(1, 1))
    }
)
author51: BinaryAssociation = BinaryAssociation(
    name="author51",
    ends={
        Property(name="Person52", type=SWRC_Unpublished, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_Unpublished", type=Person, multiplicity=Multiplicity(1, 9999))
    }
)
author53: BinaryAssociation = BinaryAssociation(
    name="author53",
    ends={
        Property(name="Person54", type=SWRC_Thesis, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_Thesis", type=Person, multiplicity=Multiplicity(1, 9999))
    }
)
school55: BinaryAssociation = BinaryAssociation(
    name="school55",
    ends={
        Property(name="University", type=SWRC_Thesis, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_Thesis56", type=University, multiplicity=Multiplicity(1, 1))
    }
)
author57: BinaryAssociation = BinaryAssociation(
    name="author57",
    ends={
        Property(name="Person58", type=SWRC_Report, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_Report", type=Person, multiplicity=Multiplicity(0, 9999))
    }
)
describesProject59: BinaryAssociation = BinaryAssociation(
    name="describesProject59",
    ends={
        Property(name="Project", type=SWRC_ProjectReport, multiplicity=Multiplicity(1, 1)),
        Property(name="projectInfo", type=Project, multiplicity=Multiplicity(1, 1))
    }
)
organization60: BinaryAssociation = BinaryAssociation(
    name="organization60",
    ends={
        Property(name="SWRC_TechnicalReport", type=Organization, multiplicity=Multiplicity(1, 1)),
        Property(name="Organization61", type=SWRC_TechnicalReport, multiplicity=Multiplicity(1, 1))
    }
)
atEvent62: BinaryAssociation = BinaryAssociation(
    name="atEvent62",
    ends={
        Property(name="Event", type=SWRC_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="hasPartEvent", type=Event, multiplicity=Multiplicity(1, 1))
    }
)
hasPartEvent63: BinaryAssociation = BinaryAssociation(
    name="hasPartEvent63",
    ends={
        Property(name="Event64", type=SWRC_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="atEvent", type=Event, multiplicity=Multiplicity(1, 1))
    }
)
participant67: BinaryAssociation = BinaryAssociation(
    name="participant67",
    ends={
        Property(name="Person68", type=SWRC_Meeting, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_Meeting", type=Person, multiplicity=Multiplicity(0, 9999))
    }
)
givenBy65: BinaryAssociation = BinaryAssociation(
    name="givenBy65",
    ends={
        Property(name="Person66", type=SWRC_Lecture, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_Lecture", type=Person, multiplicity=Multiplicity(1, 1))
    }
)
affiliation69: BinaryAssociation = BinaryAssociation(
    name="affiliation69",
    ends={
        Property(name="employs", type=Organization, multiplicity=Multiplicity(1, 1)),
        Property(name="Organization70", type=SWRC_Employee, multiplicity=Multiplicity(1, 1))
    }
)
cooperateWith71: BinaryAssociation = BinaryAssociation(
    name="cooperateWith71",
    ends={
        Property(name="AcademicStaff", type=SWRC_AcademicStaff, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_AcademicStaff", type=AcademicStaff, multiplicity=Multiplicity(0, 9999))
    }
)
headOfGroup77: BinaryAssociation = BinaryAssociation(
    name="headOfGroup77",
    ends={
        Property(name="ResearchGroup", type=SWRC_AcademicStaff, multiplicity=Multiplicity(1, 1)),
        Property(name="head78", type=ResearchGroup, multiplicity=Multiplicity(1, 1))
    }
)
memberOfPC79: BinaryAssociation = BinaryAssociation(
    name="memberOfPC79",
    ends={
        Property(name="Event81", type=SWRC_AcademicStaff, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_AcademicStaff80", type=Event, multiplicity=Multiplicity(1, 1))
    }
)
organizerOrChairOf82: BinaryAssociation = BinaryAssociation(
    name="organizerOrChairOf82",
    ends={
        Property(name="Event84", type=SWRC_AcademicStaff, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_AcademicStaff83", type=Event, multiplicity=Multiplicity(1, 1))
    }
)
editor72: BinaryAssociation = BinaryAssociation(
    name="editor72",
    ends={
        Property(name="Publication74", type=SWRC_AcademicStaff, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_AcademicStaff73", type=Publication, multiplicity=Multiplicity(1, 1))
    }
)
publication85: BinaryAssociation = BinaryAssociation(
    name="publication85",
    ends={
        Property(name="Publication87", type=SWRC_AcademicStaff, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_AcademicStaff86", type=Publication, multiplicity=Multiplicity(0, 9999))
    }
)
headOf75: BinaryAssociation = BinaryAssociation(
    name="headOf75",
    ends={
        Property(name="Project76", type=SWRC_AcademicStaff, multiplicity=Multiplicity(1, 1)),
        Property(name="head", type=Project, multiplicity=Multiplicity(1, 1))
    }
)
supervises88: BinaryAssociation = BinaryAssociation(
    name="supervises88",
    ends={
        Property(name="PhDStudent", type=SWRC_AcademicStaff, multiplicity=Multiplicity(1, 1)),
        Property(name="supervisor", type=PhDStudent, multiplicity=Multiplicity(0, 9999))
    }
)
worksAtProject89: BinaryAssociation = BinaryAssociation(
    name="worksAtProject89",
    ends={
        Property(name="ResearchTopic", type=SWRC_AcademicStaff, multiplicity=Multiplicity(1, 1)),
        Property(name="isWorkedOnBy", type=ResearchTopic, multiplicity=Multiplicity(1, 1))
    }
)
supervisor97: BinaryAssociation = BinaryAssociation(
    name="supervisor97",
    ends={
        Property(name="AcademicStaff98", type=SWRC_PhDStudent, multiplicity=Multiplicity(1, 1)),
        Property(name="supervises", type=AcademicStaff, multiplicity=Multiplicity(1, 1))
    }
)
studiesAt90: BinaryAssociation = BinaryAssociation(
    name="studiesAt90",
    ends={
        Property(name="SWRC_Student", type=University, multiplicity=Multiplicity(1, 1)),
        Property(name="University91", type=SWRC_Student, multiplicity=Multiplicity(1, 1))
    }
)
publication92: BinaryAssociation = BinaryAssociation(
    name="publication92",
    ends={
        Property(name="Publication93", type=SWRC_PhDStudent, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_PhDStudent", type=Publication, multiplicity=Multiplicity(0, 9999))
    }
)
worksAtProject94: BinaryAssociation = BinaryAssociation(
    name="worksAtProject94",
    ends={
        Property(name="Project96", type=SWRC_PhDStudent, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_PhDStudent95", type=Project, multiplicity=Multiplicity(1, 1))
    }
)
finances103: BinaryAssociation = BinaryAssociation(
    name="finances103",
    ends={
        Property(name="Project104", type=SWRC_Organization, multiplicity=Multiplicity(1, 1)),
        Property(name="financedBy", type=Project, multiplicity=Multiplicity(0, 9999))
    }
)
publishes105: BinaryAssociation = BinaryAssociation(
    name="publishes105",
    ends={
        Property(name="Publication106", type=SWRC_Organization, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_Organization", type=Publication, multiplicity=Multiplicity(0, 9999))
    }
)
technicalReport107: BinaryAssociation = BinaryAssociation(
    name="technicalReport107",
    ends={
        Property(name="TechnicalReport", type=SWRC_Organization, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_Organization108", type=TechnicalReport, multiplicity=Multiplicity(0, 9999))
    }
)
carriesOut99: BinaryAssociation = BinaryAssociation(
    name="carriesOut99",
    ends={
        Property(name="Project100", type=SWRC_Organization, multiplicity=Multiplicity(1, 1)),
        Property(name="carriedOutBy", type=Project, multiplicity=Multiplicity(0, 9999))
    }
)
develops101: BinaryAssociation = BinaryAssociation(
    name="develops101",
    ends={
        Property(name="Product", type=SWRC_Organization, multiplicity=Multiplicity(1, 1)),
        Property(name="developedBy", type=Product, multiplicity=Multiplicity(0, 9999))
    }
)
employs102: BinaryAssociation = BinaryAssociation(
    name="employs102",
    ends={
        Property(name="Employee", type=SWRC_Organization, multiplicity=Multiplicity(1, 1)),
        Property(name="affiliation", type=Employee, multiplicity=Multiplicity(0, 9999))
    }
)
member111: BinaryAssociation = BinaryAssociation(
    name="member111",
    ends={
        Property(name="Employee112", type=SWRC_ResearchGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_ResearchGroup", type=Employee, multiplicity=Multiplicity(0, 9999))
    }
)
head109: BinaryAssociation = BinaryAssociation(
    name="head109",
    ends={
        Property(name="AcademicStaff110", type=SWRC_ResearchGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="headOfGroup", type=AcademicStaff, multiplicity=Multiplicity(1, 1))
    }
)
hasParts113: BinaryAssociation = BinaryAssociation(
    name="hasParts113",
    ends={
        Property(name="Institute", type=SWRC_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_Department", type=Institute, multiplicity=Multiplicity(1, 1))
    }
)
cooperateWith114: BinaryAssociation = BinaryAssociation(
    name="cooperateWith114",
    ends={
        Property(name="Institute115", type=SWRC_Institute, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_Institute", type=Institute, multiplicity=Multiplicity(1, 1))
    }
)
hasParts116: BinaryAssociation = BinaryAssociation(
    name="hasParts116",
    ends={
        Property(name="ResearchGroup118", type=SWRC_Institute, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_Institute117", type=ResearchGroup, multiplicity=Multiplicity(0, 9999))
    }
)
carriedOutBy122: BinaryAssociation = BinaryAssociation(
    name="carriedOutBy122",
    ends={
        Property(name="Organization123", type=SWRC_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="carriesOut", type=Organization, multiplicity=Multiplicity(1, 1))
    }
)
financedBy124: BinaryAssociation = BinaryAssociation(
    name="financedBy124",
    ends={
        Property(name="Organization125", type=SWRC_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="finances", type=Organization, multiplicity=Multiplicity(1, 1))
    }
)
hasParts119: BinaryAssociation = BinaryAssociation(
    name="hasParts119",
    ends={
        Property(name="Department", type=SWRC_University, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_University", type=Department, multiplicity=Multiplicity(0, 9999))
    }
)
student120: BinaryAssociation = BinaryAssociation(
    name="student120",
    ends={
        Property(name="Student", type=SWRC_University, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_University121", type=Student, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
isAbout128: BinaryAssociation = BinaryAssociation(
    name="isAbout128",
    ends={
        Property(name="ResearchTopic129", type=SWRC_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="dealWithIn", type=ResearchTopic, multiplicity=Multiplicity(1, 9999))
    }
)
member130: BinaryAssociation = BinaryAssociation(
    name="member130",
    ends={
        Property(name="Person131", type=SWRC_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_Project", type=Person, multiplicity=Multiplicity(0, 9999))
    }
)
projectInfo132: BinaryAssociation = BinaryAssociation(
    name="projectInfo132",
    ends={
        Property(name="ProjectReport", type=SWRC_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="describesProject", type=ProjectReport, multiplicity=Multiplicity(0, 9999))
    }
)
head126: BinaryAssociation = BinaryAssociation(
    name="head126",
    ends={
        Property(name="AcademicStaff127", type=SWRC_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="headOf", type=AcademicStaff, multiplicity=Multiplicity(1, 1))
    }
)
product133: BinaryAssociation = BinaryAssociation(
    name="product133",
    ends={
        Property(name="Product134", type=SWRC_SoftwareProject, multiplicity=Multiplicity(1, 1)),
        Property(name="SWRC_SoftwareProject", type=Product, multiplicity=Multiplicity(1, 1))
    }
)
developedBy135: BinaryAssociation = BinaryAssociation(
    name="developedBy135",
    ends={
        Property(name="Organization136", type=SWRC_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="develops", type=Organization, multiplicity=Multiplicity(1, 1))
    }
)
dealWithIn137: BinaryAssociation = BinaryAssociation(
    name="dealWithIn137",
    ends={
        Property(name="Project138", type=SWRC_ResearchTopic, multiplicity=Multiplicity(1, 1)),
        Property(name="isAbout", type=Project, multiplicity=Multiplicity(1, 1))
    }
)
isWorkedOnBy139: BinaryAssociation = BinaryAssociation(
    name="isWorkedOnBy139",
    ends={
        Property(name="AcademicStaff140", type=SWRC_ResearchTopic, multiplicity=Multiplicity(1, 1)),
        Property(name="worksAtProject", type=AcademicStaff, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_SWRC_Book_Publication = Generalization(general=Publication, specific=SWRC_Book)
gen_SWRC_Article_Publication = Generalization(general=Publication, specific=SWRC_Article)
gen_SWRC_InBook_Publication = Generalization(general=Publication, specific=SWRC_InBook)
gen_SWRC_Booklet_Publication = Generalization(general=Publication, specific=SWRC_Booklet)
gen_SWRC_InCollection_Publication = Generalization(general=Publication, specific=SWRC_InCollection)
gen_SWRC_InProceedings_Publication = Generalization(general=Publication, specific=SWRC_InProceedings)
gen_SWRC_Proceedings_Publication = Generalization(general=Publication, specific=SWRC_Proceedings)
gen_SWRC_Manual_Publication = Generalization(general=Publication, specific=SWRC_Manual)
gen_SWRC_Unpublished_Publication = Generalization(general=Publication, specific=SWRC_Unpublished)
gen_SWRC_Misc_Publication = Generalization(general=Publication, specific=SWRC_Misc)
gen_SWRC_Thesis_Publication = Generalization(general=Publication, specific=SWRC_Thesis)
gen_SWRC_MasterThesis_Thesis = Generalization(general=Thesis, specific=SWRC_MasterThesis)
gen_SWRC_PhDThesis_Thesis = Generalization(general=Thesis, specific=SWRC_PhDThesis)
gen_SWRC_Report_Publication = Generalization(general=Publication, specific=SWRC_Report)
gen_SWRC_ProjectReport_Report = Generalization(general=Report, specific=SWRC_ProjectReport)
gen_SWRC_TechnicalReport_Report = Generalization(general=Report, specific=SWRC_TechnicalReport)
gen_SWRC_Conference_Event = Generalization(general=Event, specific=SWRC_Conference)
gen_SWRC_Workshop_Event = Generalization(general=Event, specific=SWRC_Workshop)
gen_SWRC_Exhibition_Event = Generalization(general=Event, specific=SWRC_Exhibition)
gen_SWRC_Lecture_Event = Generalization(general=Event, specific=SWRC_Lecture)
gen_SWRC_Meeting_Event = Generalization(general=Event, specific=SWRC_Meeting)
gen_SWRC_ProjectMeeting_Meeting = Generalization(general=Meeting, specific=SWRC_ProjectMeeting)
gen_SWRC_Employee_Person = Generalization(general=Person, specific=SWRC_Employee)
gen_SWRC_AcademicStaff_Person = Generalization(general=Person, specific=SWRC_AcademicStaff)
gen_SWRC_Manager_Employee = Generalization(general=Employee, specific=SWRC_Manager)
gen_SWRC_AdministrativeStaff_Employee = Generalization(general=Employee, specific=SWRC_AdministrativeStaff)
gen_SWRC_TechnicalStaff_Employee = Generalization(general=Employee, specific=SWRC_TechnicalStaff)
gen_SWRC_Lecturer_AcademicStaff = Generalization(general=AcademicStaff, specific=SWRC_Lecturer)
gen_SWRC_FacultyMember_AcademicStaff = Generalization(general=AcademicStaff, specific=SWRC_FacultyMember)
gen_SWRC_FullProfessor_FacultyMember = Generalization(general=FacultyMember, specific=SWRC_FullProfessor)
gen_SWRC_AssistantProfessor_FacultyMember = Generalization(general=FacultyMember, specific=SWRC_AssistantProfessor)
gen_SWRC_AssociateProfessor_FacultyMember = Generalization(general=FacultyMember, specific=SWRC_AssociateProfessor)
gen_SWRC_Student_Person = Generalization(general=Person, specific=SWRC_Student)
gen_SWRC_Undergraduate_Student = Generalization(general=Student, specific=SWRC_Undergraduate)
gen_SWRC_Graduate_Student = Generalization(general=Student, specific=SWRC_Graduate)
gen_SWRC_PhDStudent_Graduate = Generalization(general=Graduate, specific=SWRC_PhDStudent)
gen_SWRC_ResearchGroup_Organization = Generalization(general=Organization, specific=SWRC_ResearchGroup)
gen_SWRC_Association_Organization = Generalization(general=Organization, specific=SWRC_Association)
gen_SWRC_Department_Organization = Generalization(general=Organization, specific=SWRC_Department)
gen_SWRC_Enterprise_Organization = Generalization(general=Organization, specific=SWRC_Enterprise)
gen_SWRC_Institute_Organization = Generalization(general=Organization, specific=SWRC_Institute)
gen_SWRC_University_Organization = Generalization(general=Organization, specific=SWRC_University)
gen_SWRC_ResearchProject_Project = Generalization(general=Project, specific=SWRC_ResearchProject)
gen_SWRC_DevelopmentProject_Project = Generalization(general=Project, specific=SWRC_DevelopmentProject)
gen_SWRC_SoftwareProject_Project = Generalization(general=Project, specific=SWRC_SoftwareProject)
gen_SWRC_ResearchTopic_Topic = Generalization(general=Topic, specific=SWRC_ResearchTopic)
gen_SWRC_SoftwareComponent_Product = Generalization(general=Product, specific=SWRC_SoftwareComponent)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={SWRC_Bibliography, SWRC_Publication, Publication, SWRC_Book, SWRC_Article, Person, Organization, SWRC_InBook, SWRC_Booklet, SWRC_InCollection, SWRC_InProceedings, SWRC_Proceedings, SWRC_Manual, SWRC_Misc, SWRC_Unpublished, SWRC_Thesis, University, SWRC_MasterThesis, Thesis, SWRC_PhDThesis, SWRC_Report, SWRC_ProjectReport, Report, Project, SWRC_TechnicalReport, SWRC_Event, Event, SWRC_Conference, SWRC_Workshop, SWRC_Exhibition, SWRC_Lecture, SWRC_Meeting, SWRC_ProjectMeeting, Meeting, SWRC_Person, SWRC_Employee, SWRC_AcademicStaff, AcademicStaff, SWRC_Manager, Employee, SWRC_AdministrativeStaff, SWRC_TechnicalStaff, ResearchGroup, PhDStudent, ResearchTopic, SWRC_Lecturer, SWRC_FacultyMember, SWRC_FullProfessor, FacultyMember, SWRC_AssistantProfessor, SWRC_AssociateProfessor, SWRC_Student, SWRC_Undergraduate, Student, SWRC_Graduate, SWRC_PhDStudent, Graduate, SWRC_Organization, TechnicalReport, SWRC_ResearchGroup, Product, SWRC_Association, SWRC_Department, Institute, SWRC_Enterprise, SWRC_Institute, SWRC_Project, SWRC_University, Department, ProjectReport, SWRC_Product, SWRC_ResearchProject, SWRC_DevelopmentProject, SWRC_SoftwareProject, SWRC_Topic, SWRC_ResearchTopic, Topic, SWRC_SoftwareComponent},
    associations={publications0, author1, publisher4, editor2, author6, author9, publisher11, editor14, author17, author21, editor19, publisher24, author29, editor27, organization32, editor38, publisher40, publisher35, organization43, author46, organization48, author51, author53, school55, author57, describesProject59, organization60, atEvent62, hasPartEvent63, participant67, givenBy65, affiliation69, cooperateWith71, headOfGroup77, memberOfPC79, organizerOrChairOf82, editor72, publication85, headOf75, supervises88, worksAtProject89, supervisor97, studiesAt90, publication92, worksAtProject94, finances103, publishes105, technicalReport107, carriesOut99, develops101, employs102, member111, head109, hasParts113, cooperateWith114, hasParts116, carriedOutBy122, financedBy124, hasParts119, student120, isAbout128, member130, projectInfo132, head126, product133, developedBy135, dealWithIn137, isWorkedOnBy139},
    generalizations={gen_SWRC_Book_Publication, gen_SWRC_Article_Publication, gen_SWRC_InBook_Publication, gen_SWRC_Booklet_Publication, gen_SWRC_InCollection_Publication, gen_SWRC_InProceedings_Publication, gen_SWRC_Proceedings_Publication, gen_SWRC_Manual_Publication, gen_SWRC_Unpublished_Publication, gen_SWRC_Misc_Publication, gen_SWRC_Thesis_Publication, gen_SWRC_MasterThesis_Thesis, gen_SWRC_PhDThesis_Thesis, gen_SWRC_Report_Publication, gen_SWRC_ProjectReport_Report, gen_SWRC_TechnicalReport_Report, gen_SWRC_Conference_Event, gen_SWRC_Workshop_Event, gen_SWRC_Exhibition_Event, gen_SWRC_Lecture_Event, gen_SWRC_Meeting_Event, gen_SWRC_ProjectMeeting_Meeting, gen_SWRC_Employee_Person, gen_SWRC_AcademicStaff_Person, gen_SWRC_Manager_Employee, gen_SWRC_AdministrativeStaff_Employee, gen_SWRC_TechnicalStaff_Employee, gen_SWRC_Lecturer_AcademicStaff, gen_SWRC_FacultyMember_AcademicStaff, gen_SWRC_FullProfessor_FacultyMember, gen_SWRC_AssistantProfessor_FacultyMember, gen_SWRC_AssociateProfessor_FacultyMember, gen_SWRC_Student_Person, gen_SWRC_Undergraduate_Student, gen_SWRC_Graduate_Student, gen_SWRC_PhDStudent_Graduate, gen_SWRC_ResearchGroup_Organization, gen_SWRC_Association_Organization, gen_SWRC_Department_Organization, gen_SWRC_Enterprise_Organization, gen_SWRC_Institute_Organization, gen_SWRC_University_Organization, gen_SWRC_ResearchProject_Project, gen_SWRC_DevelopmentProject_Project, gen_SWRC_SoftwareProject_Project, gen_SWRC_ResearchTopic_Topic, gen_SWRC_SoftwareComponent_Product},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)