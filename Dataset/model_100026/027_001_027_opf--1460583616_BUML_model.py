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
Role: Enumeration = Enumeration(
    name="Role",
    literals={
            EnumerationLiteral(name="Art_copyist"),
			EnumerationLiteral(name="Actor"),
			EnumerationLiteral(name="Adapter"),
			EnumerationLiteral(name="Author_of_afterword_colophon_etc"),
			EnumerationLiteral(name="Analyst"),
			EnumerationLiteral(name="Animator"),
			EnumerationLiteral(name="Annotator"),
			EnumerationLiteral(name="Bibliographic_antecedent"),
			EnumerationLiteral(name="Applicant"),
			EnumerationLiteral(name="Author_in_quotations_or_text_abstracts"),
			EnumerationLiteral(name="Architect"),
			EnumerationLiteral(name="Artistic_director"),
			EnumerationLiteral(name="Arranger"),
			EnumerationLiteral(name="Artist"),
			EnumerationLiteral(name="Assignee"),
			EnumerationLiteral(name="Associated_name"),
			EnumerationLiteral(name="Attributed_name"),
			EnumerationLiteral(name="Auctioneer"),
			EnumerationLiteral(name="Author_of_dialog"),
			EnumerationLiteral(name="Author_of_introduction"),
			EnumerationLiteral(name="Calligrapher"),
			EnumerationLiteral(name="Colorist"),
			EnumerationLiteral(name="Collotyper"),
			EnumerationLiteral(name="Commentator"),
			EnumerationLiteral(name="Composer"),
			EnumerationLiteral(name="Compositor"),
			EnumerationLiteral(name="Cinematographer"),
			EnumerationLiteral(name="Conductor"),
			EnumerationLiteral(name="Censor"),
			EnumerationLiteral(name="Contestant_appellee"),
			EnumerationLiteral(name="Collector"),
			EnumerationLiteral(name="Compiler"),
			EnumerationLiteral(name="Conservator"),
			EnumerationLiteral(name="Contestant"),
			EnumerationLiteral(name="Contestant_appellant"),
			EnumerationLiteral(name="Cover_designer"),
			EnumerationLiteral(name="Copyright_claimant"),
			EnumerationLiteral(name="Complainant_appellee"),
			EnumerationLiteral(name="Copyright_holder"),
			EnumerationLiteral(name="Complainant"),
			EnumerationLiteral(name="Complainant_appellant"),
			EnumerationLiteral(name="Creator"),
			EnumerationLiteral(name="Correspondent"),
			EnumerationLiteral(name="Corrector"),
			EnumerationLiteral(name="Consultant"),
			EnumerationLiteral(name="Consultant_to_a_project"),
			EnumerationLiteral(name="Costume_designer"),
			EnumerationLiteral(name="Contributor"),
			EnumerationLiteral(name="Author_of_screenplay"),
			EnumerationLiteral(name="Author"),
			EnumerationLiteral(name="Binding_designer"),
			EnumerationLiteral(name="Bookjacket_designer"),
			EnumerationLiteral(name="Book_designer"),
			EnumerationLiteral(name="Book_producer"),
			EnumerationLiteral(name="Blurb_writer"),
			EnumerationLiteral(name="Binder"),
			EnumerationLiteral(name="Bookplate_designer"),
			EnumerationLiteral(name="Bookseller"),
			EnumerationLiteral(name="Conceptor"),
			EnumerationLiteral(name="Choreographer"),
			EnumerationLiteral(name="Collaborator"),
			EnumerationLiteral(name="Client"),
			EnumerationLiteral(name="Contestee_appellant"),
			EnumerationLiteral(name="Curator"),
			EnumerationLiteral(name="Commentator_for_written_text"),
			EnumerationLiteral(name="Defendant"),
			EnumerationLiteral(name="Defendant_appellee"),
			EnumerationLiteral(name="Defendant_appellant"),
			EnumerationLiteral(name="Degree_grantor"),
			EnumerationLiteral(name="Dissertant"),
			EnumerationLiteral(name="Delineator"),
			EnumerationLiteral(name="Dancer"),
			EnumerationLiteral(name="Donor"),
			EnumerationLiteral(name="Contestee_appellee"),
			EnumerationLiteral(name="Cartographer"),
			EnumerationLiteral(name="Contractor"),
			EnumerationLiteral(name="Contestee"),
			EnumerationLiteral(name="Director"),
			EnumerationLiteral(name="Designer"),
			EnumerationLiteral(name="Distributor"),
			EnumerationLiteral(name="Data_contributor"),
			EnumerationLiteral(name="Dedicatee"),
			EnumerationLiteral(name="Data_manager"),
			EnumerationLiteral(name="Dedicator"),
			EnumerationLiteral(name="Dubious_author"),
			EnumerationLiteral(name="Editor"),
			EnumerationLiteral(name="Engraver"),
			EnumerationLiteral(name="Electrician"),
			EnumerationLiteral(name="Electrotyper"),
			EnumerationLiteral(name="Engineer"),
			EnumerationLiteral(name="Distribution_place"),
			EnumerationLiteral(name="Depicted"),
			EnumerationLiteral(name="Depositor"),
			EnumerationLiteral(name="Draftsman"),
			EnumerationLiteral(name="Funder"),
			EnumerationLiteral(name="Forger"),
			EnumerationLiteral(name="Geographic_information_specialist"),
			EnumerationLiteral(name="Graphic_technician"),
			EnumerationLiteral(name="Honoree"),
			EnumerationLiteral(name="Host"),
			EnumerationLiteral(name="Illustrator"),
			EnumerationLiteral(name="Etcher"),
			EnumerationLiteral(name="Event_place"),
			EnumerationLiteral(name="Expert"),
			EnumerationLiteral(name="Facsimilist"),
			EnumerationLiteral(name="Field_director"),
			EnumerationLiteral(name="Film_editor"),
			EnumerationLiteral(name="Former_owner"),
			EnumerationLiteral(name="First_party"),
			EnumerationLiteral(name="Lead"),
			EnumerationLiteral(name="Libelee_appellee"),
			EnumerationLiteral(name="Libelee"),
			EnumerationLiteral(name="Lender"),
			EnumerationLiteral(name="Libelee_appellant"),
			EnumerationLiteral(name="Lighting_designer"),
			EnumerationLiteral(name="Libelant_appellee"),
			EnumerationLiteral(name="Libelant"),
			EnumerationLiteral(name="Libelant_appellant"),
			EnumerationLiteral(name="Landscape_architect"),
			EnumerationLiteral(name="Licensee"),
			EnumerationLiteral(name="Licensor"),
			EnumerationLiteral(name="Lithographer"),
			EnumerationLiteral(name="Lyricist"),
			EnumerationLiteral(name="Music_copyist"),
			EnumerationLiteral(name="Manufacture_place"),
			EnumerationLiteral(name="Manufacturer"),
			EnumerationLiteral(name="Metadata_contact"),
			EnumerationLiteral(name="Moderator"),
			EnumerationLiteral(name="Monitor"),
			EnumerationLiteral(name="Marbler"),
			EnumerationLiteral(name="Markup_editor"),
			EnumerationLiteral(name="Musical_director"),
			EnumerationLiteral(name="Illuminator"),
			EnumerationLiteral(name="Inscriber"),
			EnumerationLiteral(name="Inventor"),
			EnumerationLiteral(name="Instrumentalist"),
			EnumerationLiteral(name="Interviewee"),
			EnumerationLiteral(name="Interviewer"),
			EnumerationLiteral(name="Laboratory"),
			EnumerationLiteral(name="Librettist"),
			EnumerationLiteral(name="Laboratory_director"),
			EnumerationLiteral(name="Photographer"),
			EnumerationLiteral(name="Platemaker"),
			EnumerationLiteral(name="Permitting_agency"),
			EnumerationLiteral(name="Production_manager"),
			EnumerationLiteral(name="Printer_of_plates"),
			EnumerationLiteral(name="Papermaker"),
			EnumerationLiteral(name="Puppeteer"),
			EnumerationLiteral(name="Process_contact"),
			EnumerationLiteral(name="Production_personnel"),
			EnumerationLiteral(name="Performer"),
			EnumerationLiteral(name="Programmer"),
			EnumerationLiteral(name="Printmaker"),
			EnumerationLiteral(name="Producer"),
			EnumerationLiteral(name="Production_place"),
			EnumerationLiteral(name="Printer"),
			EnumerationLiteral(name="Patent_applicant"),
			EnumerationLiteral(name="Plaintiff_appellee"),
			EnumerationLiteral(name="Plaintiff"),
			EnumerationLiteral(name="Patent_holder"),
			EnumerationLiteral(name="Plaintiff_appellant"),
			EnumerationLiteral(name="Publication_place"),
			EnumerationLiteral(name="Rubricator"),
			EnumerationLiteral(name="Metal_engraver"),
			EnumerationLiteral(name="Musician"),
			EnumerationLiteral(name="Narrator"),
			EnumerationLiteral(name="Opponent"),
			EnumerationLiteral(name="Originator"),
			EnumerationLiteral(name="Organizer_of_meeting"),
			EnumerationLiteral(name="Other"),
			EnumerationLiteral(name="Owner"),
			EnumerationLiteral(name="Patron"),
			EnumerationLiteral(name="Publishing_director"),
			EnumerationLiteral(name="Publisher"),
			EnumerationLiteral(name="Project_director"),
			EnumerationLiteral(name="Proofreader"),
			EnumerationLiteral(name="Reporter"),
			EnumerationLiteral(name="Responsible_party"),
			EnumerationLiteral(name="Respondent_appellee"),
			EnumerationLiteral(name="Restager"),
			EnumerationLiteral(name="Respondent"),
			EnumerationLiteral(name="Respondent_appellant"),
			EnumerationLiteral(name="Research_team_head"),
			EnumerationLiteral(name="Research_team_member"),
			EnumerationLiteral(name="Scientific_advisor"),
			EnumerationLiteral(name="Scenarist"),
			EnumerationLiteral(name="Sculptor"),
			EnumerationLiteral(name="Scribe"),
			EnumerationLiteral(name="Sound_designer"),
			EnumerationLiteral(name="Secretary"),
			EnumerationLiteral(name="Signer"),
			EnumerationLiteral(name="Supporting_host"),
			EnumerationLiteral(name="Singer"),
			EnumerationLiteral(name="Speaker"),
			EnumerationLiteral(name="Recording_engineer"),
			EnumerationLiteral(name="Recipient"),
			EnumerationLiteral(name="Redactor"),
			EnumerationLiteral(name="Renderer"),
			EnumerationLiteral(name="Researcher"),
			EnumerationLiteral(name="Reviewer"),
			EnumerationLiteral(name="Repository"),
			EnumerationLiteral(name="Standards_body"),
			EnumerationLiteral(name="Stereotyper"),
			EnumerationLiteral(name="Technical_director"),
			EnumerationLiteral(name="Teacher"),
			EnumerationLiteral(name="Thesis_advisor"),
			EnumerationLiteral(name="Transcriber"),
			EnumerationLiteral(name="Translator"),
			EnumerationLiteral(name="Type_designer"),
			EnumerationLiteral(name="Typographer"),
			EnumerationLiteral(name="University_place"),
			EnumerationLiteral(name="Videographer"),
			EnumerationLiteral(name="Vocalist"),
			EnumerationLiteral(name="Writer_of_accompanying_material"),
			EnumerationLiteral(name="Woodcutter"),
			EnumerationLiteral(name="Wood_engraver"),
			EnumerationLiteral(name="Witness"),
			EnumerationLiteral(name="Sponsor"),
			EnumerationLiteral(name="Second_party"),
			EnumerationLiteral(name="Surveyor"),
			EnumerationLiteral(name="Set_designer"),
			EnumerationLiteral(name="Storyteller"),
			EnumerationLiteral(name="Stage_manager")
    }
)

Type: Enumeration = Enumeration(
    name="Type",
    literals={
            EnumerationLiteral(name="Cover"),
			EnumerationLiteral(name="Title"),
			EnumerationLiteral(name="TOC"),
			EnumerationLiteral(name="Index"),
			EnumerationLiteral(name="Glossary"),
			EnumerationLiteral(name="Acknowledgements"),
			EnumerationLiteral(name="Bibliography"),
			EnumerationLiteral(name="Colophon"),
			EnumerationLiteral(name="Copyright"),
			EnumerationLiteral(name="Dedication"),
			EnumerationLiteral(name="Epigraph"),
			EnumerationLiteral(name="Foreword"),
			EnumerationLiteral(name="Illustrations"),
			EnumerationLiteral(name="Tables"),
			EnumerationLiteral(name="Notes"),
			EnumerationLiteral(name="Preface"),
			EnumerationLiteral(name="Text")
    }
)

# Classes
opf_Package = Class(name="opf_Package")
opf_Spine = Class(name="opf_Spine")
opf_Guide = Class(name="opf_Guide")
opf_Tours = Class(name="opf_Tours")
opf_Title = Class(name="opf_Title")
opf_Metadata = Class(name="opf_Metadata")
opf_Manifest = Class(name="opf_Manifest")
opf_Description = Class(name="opf_Description")
opf_Publisher = Class(name="opf_Publisher")
opf_Contributor = Class(name="opf_Contributor")
opf_Date = Class(name="opf_Date")
opf_Type = Class(name="opf_Type")
opf_Creator = Class(name="opf_Creator")
opf_Subject = Class(name="opf_Subject")
opf_Source = Class(name="opf_Source")
opf_Language = Class(name="opf_Language")
opf_Relation = Class(name="opf_Relation")
opf_Coverage = Class(name="opf_Coverage")
opf_Rights = Class(name="opf_Rights")
opf_Format = Class(name="opf_Format")
opf_Identifier = Class(name="opf_Identifier")
opf_Itemref = Class(name="opf_Itemref")
opf_Meta = Class(name="opf_Meta")
opf_Item = Class(name="opf_Item")
opf_Reference = Class(name="opf_Reference")

# opf_Package class attributes and methods
opf_Package_version: Property = Property(name="version", type=StringType)
opf_Package_uniqueIdentifier: Property = Property(name="uniqueIdentifier", type=StringType)
opf_Package_generateCoverHTML: Property = Property(name="generateCoverHTML", type=BooleanType)
opf_Package_generateTableOfContents: Property = Property(name="generateTableOfContents", type=BooleanType)
opf_Package_includeReferencedResources: Property = Property(name="includeReferencedResources", type=BooleanType)
opf_Package.attributes={opf_Package_generateTableOfContents, opf_Package_includeReferencedResources, opf_Package_generateCoverHTML, opf_Package_version, opf_Package_uniqueIdentifier}

# opf_Spine class attributes and methods
opf_Spine_toc: Property = Property(name="toc", type=StringType)
opf_Spine.attributes={opf_Spine_toc}

# opf_Guide class attributes and methods

# opf_Tours class attributes and methods

# opf_Title class attributes and methods

# opf_Metadata class attributes and methods

# opf_Manifest class attributes and methods

# opf_Description class attributes and methods

# opf_Publisher class attributes and methods

# opf_Contributor class attributes and methods

# opf_Date class attributes and methods

# opf_Type class attributes and methods

# opf_Creator class attributes and methods

# opf_Subject class attributes and methods

# opf_Source class attributes and methods

# opf_Language class attributes and methods

# opf_Relation class attributes and methods

# opf_Coverage class attributes and methods

# opf_Rights class attributes and methods

# opf_Format class attributes and methods

# opf_Identifier class attributes and methods

# opf_Itemref class attributes and methods
opf_Itemref_idref: Property = Property(name="idref", type=StringType)
opf_Itemref_linear: Property = Property(name="linear", type=StringType)
opf_Itemref.attributes={opf_Itemref_linear, opf_Itemref_idref}

# opf_Meta class attributes and methods
opf_Meta_name: Property = Property(name="name", type=StringType)
opf_Meta_content: Property = Property(name="content", type=StringType)
opf_Meta.attributes={opf_Meta_content, opf_Meta_name}

# opf_Item class attributes and methods
opf_Item_id: Property = Property(name="id", type=StringType)
opf_Item_href: Property = Property(name="href", type=StringType)
opf_Item_media_type: Property = Property(name="media_type", type=StringType)
opf_Item_fallback: Property = Property(name="fallback", type=StringType)
opf_Item_fallback_style: Property = Property(name="fallback_style", type=StringType)
opf_Item_required_namespace: Property = Property(name="required_namespace", type=StringType)
opf_Item_required_modules: Property = Property(name="required_modules", type=StringType)
opf_Item_file: Property = Property(name="file", type=StringType)
opf_Item_noToc: Property = Property(name="noToc", type=BooleanType)
opf_Item_title: Property = Property(name="title", type=StringType)
opf_Item_generated: Property = Property(name="generated", type=BooleanType)
opf_Item_sourcePath: Property = Property(name="sourcePath", type=StringType)
opf_Item.attributes={opf_Item_fallback, opf_Item_href, opf_Item_media_type, opf_Item_sourcePath, opf_Item_id, opf_Item_required_modules, opf_Item_required_namespace, opf_Item_title, opf_Item_noToc, opf_Item_file, opf_Item_fallback_style, opf_Item_generated}

# opf_Reference class attributes and methods
opf_Reference_href: Property = Property(name="href", type=StringType)
opf_Reference_type: Property = Property(name="type", type=StringType)
opf_Reference_title: Property = Property(name="title", type=StringType)
opf_Reference.attributes={opf_Reference_href, opf_Reference_type, opf_Reference_title}

# Relationships
spine3: BinaryAssociation = BinaryAssociation(
    name="spine3",
    ends={
        Property(name="opf_Spine", type=opf_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="opf_Package4", type=opf_Spine, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
guide5: BinaryAssociation = BinaryAssociation(
    name="guide5",
    ends={
        Property(name="opf_Guide", type=opf_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="opf_Package6", type=opf_Guide, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tours7: BinaryAssociation = BinaryAssociation(
    name="tours7",
    ends={
        Property(name="opf_Tours", type=opf_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="opf_Package8", type=opf_Tours, multiplicity=Multiplicity(0, 1))
    }
)
titles9: BinaryAssociation = BinaryAssociation(
    name="titles9",
    ends={
        Property(name="opf_Title", type=opf_Metadata, multiplicity=Multiplicity(1, 1)),
        Property(name="opf_Metadata10", type=opf_Title, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
metadata0: BinaryAssociation = BinaryAssociation(
    name="metadata0",
    ends={
        Property(name="opf_Metadata", type=opf_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="opf_Package", type=opf_Metadata, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
manifest1: BinaryAssociation = BinaryAssociation(
    name="manifest1",
    ends={
        Property(name="opf_Manifest", type=opf_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="opf_Package2", type=opf_Manifest, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
descriptions15: BinaryAssociation = BinaryAssociation(
    name="descriptions15",
    ends={
        Property(name="opf_Description", type=opf_Metadata, multiplicity=Multiplicity(1, 1)),
        Property(name="opf_Metadata16", type=opf_Description, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
publishers17: BinaryAssociation = BinaryAssociation(
    name="publishers17",
    ends={
        Property(name="opf_Publisher", type=opf_Metadata, multiplicity=Multiplicity(1, 1)),
        Property(name="opf_Metadata18", type=opf_Publisher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contributors19: BinaryAssociation = BinaryAssociation(
    name="contributors19",
    ends={
        Property(name="opf_Contributor", type=opf_Metadata, multiplicity=Multiplicity(1, 1)),
        Property(name="opf_Metadata20", type=opf_Contributor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dates21: BinaryAssociation = BinaryAssociation(
    name="dates21",
    ends={
        Property(name="opf_Date", type=opf_Metadata, multiplicity=Multiplicity(1, 1)),
        Property(name="opf_Metadata22", type=opf_Date, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types23: BinaryAssociation = BinaryAssociation(
    name="types23",
    ends={
        Property(name="opf_Type", type=opf_Metadata, multiplicity=Multiplicity(1, 1)),
        Property(name="opf_Metadata24", type=opf_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
creators11: BinaryAssociation = BinaryAssociation(
    name="creators11",
    ends={
        Property(name="opf_Creator", type=opf_Metadata, multiplicity=Multiplicity(1, 1)),
        Property(name="opf_Metadata12", type=opf_Creator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subjects13: BinaryAssociation = BinaryAssociation(
    name="subjects13",
    ends={
        Property(name="opf_Subject", type=opf_Metadata, multiplicity=Multiplicity(1, 1)),
        Property(name="opf_Metadata14", type=opf_Subject, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
sources29: BinaryAssociation = BinaryAssociation(
    name="sources29",
    ends={
        Property(name="opf_Source", type=opf_Metadata, multiplicity=Multiplicity(1, 1)),
        Property(name="opf_Metadata30", type=opf_Source, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
languages31: BinaryAssociation = BinaryAssociation(
    name="languages31",
    ends={
        Property(name="opf_Language", type=opf_Metadata, multiplicity=Multiplicity(1, 1)),
        Property(name="opf_Metadata32", type=opf_Language, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
relations33: BinaryAssociation = BinaryAssociation(
    name="relations33",
    ends={
        Property(name="opf_Relation", type=opf_Metadata, multiplicity=Multiplicity(1, 1)),
        Property(name="opf_Metadata34", type=opf_Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
coverages35: BinaryAssociation = BinaryAssociation(
    name="coverages35",
    ends={
        Property(name="opf_Coverage", type=opf_Metadata, multiplicity=Multiplicity(1, 1)),
        Property(name="opf_Metadata36", type=opf_Coverage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rights37: BinaryAssociation = BinaryAssociation(
    name="rights37",
    ends={
        Property(name="opf_Rights", type=opf_Metadata, multiplicity=Multiplicity(1, 1)),
        Property(name="opf_Metadata38", type=opf_Rights, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formats25: BinaryAssociation = BinaryAssociation(
    name="formats25",
    ends={
        Property(name="opf_Format", type=opf_Metadata, multiplicity=Multiplicity(1, 1)),
        Property(name="opf_Metadata26", type=opf_Format, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identifiers27: BinaryAssociation = BinaryAssociation(
    name="identifiers27",
    ends={
        Property(name="opf_Identifier", type=opf_Metadata, multiplicity=Multiplicity(1, 1)),
        Property(name="opf_Metadata28", type=opf_Identifier, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
metas39: BinaryAssociation = BinaryAssociation(
    name="metas39",
    ends={
        Property(name="opf_Meta", type=opf_Metadata, multiplicity=Multiplicity(1, 1)),
        Property(name="opf_Metadata40", type=opf_Meta, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items41: BinaryAssociation = BinaryAssociation(
    name="items41",
    ends={
        Property(name="opf_Item", type=opf_Manifest, multiplicity=Multiplicity(1, 1)),
        Property(name="opf_Manifest42", type=opf_Item, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
spineItems43: BinaryAssociation = BinaryAssociation(
    name="spineItems43",
    ends={
        Property(name="opf_Itemref", type=opf_Spine, multiplicity=Multiplicity(1, 1)),
        Property(name="opf_Spine44", type=opf_Itemref, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guideItems45: BinaryAssociation = BinaryAssociation(
    name="guideItems45",
    ends={
        Property(name="opf_Reference", type=opf_Guide, multiplicity=Multiplicity(1, 1)),
        Property(name="opf_Guide46", type=opf_Reference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="opf",
    types={opf_Package, opf_Spine, opf_Guide, opf_Tours, opf_Title, opf_Metadata, opf_Manifest, opf_Description, opf_Publisher, opf_Contributor, opf_Date, opf_Type, opf_Creator, opf_Subject, opf_Source, opf_Language, opf_Relation, opf_Coverage, opf_Rights, opf_Format, opf_Identifier, opf_Itemref, opf_Meta, opf_Item, opf_Reference, Role, Type},
    associations={spine3, guide5, tours7, titles9, metadata0, manifest1, descriptions15, publishers17, contributors19, dates21, types23, creators11, subjects13, sources29, languages31, relations33, coverages35, rights37, formats25, identifiers27, metas39, items41, spineItems43, guideItems45},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)