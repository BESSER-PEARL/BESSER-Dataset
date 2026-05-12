from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Role(Enum):
    Art_copyist = "Art_copyist"
    Actor = "Actor"
    Adapter = "Adapter"
    Author_of_afterword_colophon_etc = "Author_of_afterword_colophon_etc"
    Analyst = "Analyst"
    Animator = "Animator"
    Annotator = "Annotator"
    Bibliographic_antecedent = "Bibliographic_antecedent"
    Applicant = "Applicant"
    Author_in_quotations_or_text_abstracts = "Author_in_quotations_or_text_abstracts"
    Architect = "Architect"
    Artistic_director = "Artistic_director"
    Arranger = "Arranger"
    Artist = "Artist"
    Associated_name = "Associated_name"
    Attributed_name = "Attributed_name"
    Auctioneer = "Auctioneer"
    Author_of_dialog = "Author_of_dialog"
    Author_of_introduction = "Author_of_introduction"
    Author_of_screenplay = "Author_of_screenplay"
    Author = "Author"
    Binding_designer = "Binding_designer"
    Bookjacket_designer = "Bookjacket_designer"
    Book_designer = "Book_designer"
    Book_producer = "Book_producer"
    Blurb_writer = "Blurb_writer"
    Binder = "Binder"
    Bookplate_designer = "Bookplate_designer"
    Bookseller = "Bookseller"
    Conceptor = "Conceptor"
    Choreographer = "Choreographer"
    Collaborator = "Collaborator"
    Client = "Client"
    Assignee = "Assignee"
    Colorist = "Colorist"
    Collotyper = "Collotyper"
    Commentator = "Commentator"
    Composer = "Composer"
    Compositor = "Compositor"
    Cinematographer = "Cinematographer"
    Conductor = "Conductor"
    Censor = "Censor"
    Contestant_appellee = "Contestant_appellee"
    Collector = "Collector"
    Compiler = "Compiler"
    Conservator = "Conservator"
    Contestant = "Contestant"
    Contestant_appellant = "Contestant_appellant"
    Cover_designer = "Cover_designer"
    Copyright_claimant = "Copyright_claimant"
    Complainant_appellee = "Complainant_appellee"
    Copyright_holder = "Copyright_holder"
    Calligrapher = "Calligrapher"
    Complainant = "Complainant"
    Complainant_appellant = "Complainant_appellant"
    Creator = "Creator"
    Correspondent = "Correspondent"
    Corrector = "Corrector"
    Consultant = "Consultant"
    Consultant_to_a_project = "Consultant_to_a_project"
    Costume_designer = "Costume_designer"
    Contributor = "Contributor"
    Contestee_appellee = "Contestee_appellee"
    Cartographer = "Cartographer"
    Contractor = "Contractor"
    Contestee = "Contestee"
    Contestee_appellant = "Contestee_appellant"
    Curator = "Curator"
    Commentator_for_written_text = "Commentator_for_written_text"
    Defendant = "Defendant"
    Defendant_appellant = "Defendant_appellant"
    Degree_grantor = "Degree_grantor"
    Dissertant = "Dissertant"
    Delineator = "Delineator"
    Dancer = "Dancer"
    Donor = "Donor"
    Distribution_place = "Distribution_place"
    Depicted = "Depicted"
    Depositor = "Depositor"
    Draftsman = "Draftsman"
    Director = "Director"
    Designer = "Designer"
    Distributor = "Distributor"
    Data_contributor = "Data_contributor"
    Dedicatee = "Dedicatee"
    Data_manager = "Data_manager"
    Defendant_appellee = "Defendant_appellee"
    Dubious_author = "Dubious_author"
    Editor = "Editor"
    Engraver = "Engraver"
    Electrician = "Electrician"
    Electrotyper = "Electrotyper"
    Engineer = "Engineer"
    Etcher = "Etcher"
    Event_place = "Event_place"
    Expert = "Expert"
    Facsimilist = "Facsimilist"
    Field_director = "Field_director"
    Film_editor = "Film_editor"
    Former_owner = "Former_owner"
    First_party = "First_party"
    Dedicator = "Dedicator"
    Forger = "Forger"
    Geographic_information_specialist = "Geographic_information_specialist"
    Graphic_technician = "Graphic_technician"
    Honoree = "Honoree"
    Host = "Host"
    Illustrator = "Illustrator"
    Illuminator = "Illuminator"
    Inscriber = "Inscriber"
    Inventor = "Inventor"
    Instrumentalist = "Instrumentalist"
    Interviewee = "Interviewee"
    Interviewer = "Interviewer"
    Laboratory = "Laboratory"
    Librettist = "Librettist"
    Laboratory_director = "Laboratory_director"
    Funder = "Funder"
    Libelee_appellee = "Libelee_appellee"
    Libelee = "Libelee"
    Lender = "Lender"
    Libelee_appellant = "Libelee_appellant"
    Lighting_designer = "Lighting_designer"
    Libelant_appellee = "Libelant_appellee"
    Libelant = "Libelant"
    Libelant_appellant = "Libelant_appellant"
    Landscape_architect = "Landscape_architect"
    Licensee = "Licensee"
    Licensor = "Licensor"
    Lithographer = "Lithographer"
    Lyricist = "Lyricist"
    Music_copyist = "Music_copyist"
    Lead = "Lead"
    Manufacturer = "Manufacturer"
    Metadata_contact = "Metadata_contact"
    Moderator = "Moderator"
    Monitor = "Monitor"
    Marbler = "Marbler"
    Markup_editor = "Markup_editor"
    Musical_director = "Musical_director"
    Metal_engraver = "Metal_engraver"
    Musician = "Musician"
    Narrator = "Narrator"
    Opponent = "Opponent"
    Originator = "Originator"
    Organizer_of_meeting = "Organizer_of_meeting"
    Other = "Other"
    Manufacture_place = "Manufacture_place"
    Patron = "Patron"
    Publishing_director = "Publishing_director"
    Publisher = "Publisher"
    Project_director = "Project_director"
    Proofreader = "Proofreader"
    Photographer = "Photographer"
    Platemaker = "Platemaker"
    Permitting_agency = "Permitting_agency"
    Production_manager = "Production_manager"
    Printer_of_plates = "Printer_of_plates"
    Papermaker = "Papermaker"
    Puppeteer = "Puppeteer"
    Process_contact = "Process_contact"
    Owner = "Owner"
    Production_personnel = "Production_personnel"
    Performer = "Performer"
    Programmer = "Programmer"
    Printmaker = "Printmaker"
    Producer = "Producer"
    Production_place = "Production_place"
    Printer = "Printer"
    Patent_applicant = "Patent_applicant"
    Plaintiff_appellee = "Plaintiff_appellee"
    Plaintiff = "Plaintiff"
    Patent_holder = "Patent_holder"
    Plaintiff_appellant = "Plaintiff_appellant"
    Publication_place = "Publication_place"
    Recording_engineer = "Recording_engineer"
    Recipient = "Recipient"
    Redactor = "Redactor"
    Renderer = "Renderer"
    Researcher = "Researcher"
    Reviewer = "Reviewer"
    Repository = "Repository"
    Reporter = "Reporter"
    Responsible_party = "Responsible_party"
    Respondent_appellee = "Respondent_appellee"
    Restager = "Restager"
    Respondent = "Respondent"
    Respondent_appellant = "Respondent_appellant"
    Rubricator = "Rubricator"
    Research_team_head = "Research_team_head"
    Research_team_member = "Research_team_member"
    Scientific_advisor = "Scientific_advisor"
    Scenarist = "Scenarist"
    Sculptor = "Sculptor"
    Scribe = "Scribe"
    Sound_designer = "Sound_designer"
    Secretary = "Secretary"
    Signer = "Signer"
    Supporting_host = "Supporting_host"
    Speaker = "Speaker"
    Sponsor = "Sponsor"
    Second_party = "Second_party"
    Surveyor = "Surveyor"
    Set_designer = "Set_designer"
    Storyteller = "Storyteller"
    Stage_manager = "Stage_manager"
    Standards_body = "Standards_body"
    Stereotyper = "Stereotyper"
    Technical_director = "Technical_director"
    Teacher = "Teacher"
    Singer = "Singer"
    Transcriber = "Transcriber"
    Translator = "Translator"
    Type_designer = "Type_designer"
    Typographer = "Typographer"
    University_place = "University_place"
    Videographer = "Videographer"
    Vocalist = "Vocalist"
    Writer_of_accompanying_material = "Writer_of_accompanying_material"
    Woodcutter = "Woodcutter"
    Wood_engraver = "Wood_engraver"
    Witness = "Witness"
    Thesis_advisor = "Thesis_advisor"
class Type(Enum):
    Cover = "Cover"
    Title = "Title"
    TOC = "TOC"
    Index = "Index"
    Glossary = "Glossary"
    Acknowledgements = "Acknowledgements"
    Bibliography = "Bibliography"
    Colophon = "Colophon"
    Copyright = "Copyright"
    Dedication = "Dedication"
    Epigraph = "Epigraph"
    Foreword = "Foreword"
    Illustrations = "Illustrations"
    Tables = "Tables"
    Notes = "Notes"
    Preface = "Preface"
    Text = "Text"


############################################
# Definition of Classes
############################################

class opf_Reference:

    def __init__(self, type: str, title: str, href: str, opf_Reference: "opf_Guide" = None):
        self.type = type
        self.title = title
        self.href = href
        self.opf_Reference = opf_Reference
        
        pass
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def href(self):
        return self.__href

    @href.setter
    def href(self, href: str):
        self.__href = href


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def opf_Reference(self):
        return self.__opf_Reference

    @opf_Reference.setter
    def opf_Reference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_opf_Reference__opf_Reference", None)
        self.__opf_Reference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "opf_Guide46"):
                opp_val = getattr(old_value, "opf_Guide46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "opf_Guide46"):
                opp_val = getattr(value, "opf_Guide46", None)
                if opp_val is None:
                    setattr(value, "opf_Guide46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class opf_Itemref:

    def __init__(self, linear: str, idref: str, opf_Itemref: "opf_Spine" = None):
        self.linear = linear
        self.idref = idref
        self.opf_Itemref = opf_Itemref
        
        pass
    @property
    def linear(self):
        return self.__linear

    @linear.setter
    def linear(self, linear: str):
        self.__linear = linear


    @property
    def idref(self):
        return self.__idref

    @idref.setter
    def idref(self, idref: str):
        self.__idref = idref


    @property
    def opf_Itemref(self):
        return self.__opf_Itemref

    @opf_Itemref.setter
    def opf_Itemref(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_opf_Itemref__opf_Itemref", None)
        self.__opf_Itemref = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "opf_Spine44"):
                opp_val = getattr(old_value, "opf_Spine44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "opf_Spine44"):
                opp_val = getattr(value, "opf_Spine44", None)
                if opp_val is None:
                    setattr(value, "opf_Spine44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class opf_Rights:

    pass
class opf_Item:

    def __init__(self, id: str, href: str, media_type: str, fallback: str, fallback_style: str, required_namespace: str, required_modules: str, file: str, noToc: bool, title: str, generated: bool, sourcePath: str, properties: str, media_overlay: str, opf_Item: "opf_Manifest" = None):
        self.id = id
        self.href = href
        self.media_type = media_type
        self.fallback = fallback
        self.fallback_style = fallback_style
        self.required_namespace = required_namespace
        self.required_modules = required_modules
        self.file = file
        self.noToc = noToc
        self.title = title
        self.generated = generated
        self.sourcePath = sourcePath
        self.properties = properties
        self.media_overlay = media_overlay
        self.opf_Item = opf_Item
        
        pass
    @property
    def sourcePath(self):
        return self.__sourcePath

    @sourcePath.setter
    def sourcePath(self, sourcePath: str):
        self.__sourcePath = sourcePath


    @property
    def properties(self):
        return self.__properties

    @properties.setter
    def properties(self, properties: str):
        self.__properties = properties


    @property
    def fallback(self):
        return self.__fallback

    @fallback.setter
    def fallback(self, fallback: str):
        self.__fallback = fallback


    @property
    def fallback_style(self):
        return self.__fallback_style

    @fallback_style.setter
    def fallback_style(self, fallback_style: str):
        self.__fallback_style = fallback_style


    @property
    def href(self):
        return self.__href

    @href.setter
    def href(self, href: str):
        self.__href = href


    @property
    def required_namespace(self):
        return self.__required_namespace

    @required_namespace.setter
    def required_namespace(self, required_namespace: str):
        self.__required_namespace = required_namespace


    @property
    def generated(self):
        return self.__generated

    @generated.setter
    def generated(self, generated: bool):
        self.__generated = generated


    @property
    def media_type(self):
        return self.__media_type

    @media_type.setter
    def media_type(self, media_type: str):
        self.__media_type = media_type


    @property
    def noToc(self):
        return self.__noToc

    @noToc.setter
    def noToc(self, noToc: bool):
        self.__noToc = noToc


    @property
    def required_modules(self):
        return self.__required_modules

    @required_modules.setter
    def required_modules(self, required_modules: str):
        self.__required_modules = required_modules


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def media_overlay(self):
        return self.__media_overlay

    @media_overlay.setter
    def media_overlay(self, media_overlay: str):
        self.__media_overlay = media_overlay


    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def opf_Item(self):
        return self.__opf_Item

    @opf_Item.setter
    def opf_Item(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_opf_Item__opf_Item", None)
        self.__opf_Item = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "opf_Manifest42"):
                opp_val = getattr(old_value, "opf_Manifest42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "opf_Manifest42"):
                opp_val = getattr(value, "opf_Manifest42", None)
                if opp_val is None:
                    setattr(value, "opf_Manifest42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class opf_Meta:

    def __init__(self, name: str, content: str, id: str, property1: str, refines: str, scheme: str, dir: str, opf_Meta: "opf_Metadata" = None):
        self.name = name
        self.content = content
        self.id = id
        self.property1 = property1
        self.refines = refines
        self.scheme = scheme
        self.dir = dir
        self.opf_Meta = opf_Meta
        
        pass
    @property
    def scheme(self):
        return self.__scheme

    @scheme.setter
    def scheme(self, scheme: str):
        self.__scheme = scheme


    @property
    def property1(self):
        return self.__property1

    @property1.setter
    def property1(self, property: str):
        self.__property1 = property


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def dir(self):
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir


    @property
    def refines(self):
        return self.__refines

    @refines.setter
    def refines(self, refines: str):
        self.__refines = refines


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content


    @property
    def opf_Meta(self):
        return self.__opf_Meta

    @opf_Meta.setter
    def opf_Meta(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_opf_Meta__opf_Meta", None)
        self.__opf_Meta = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "opf_Metadata40"):
                opp_val = getattr(old_value, "opf_Metadata40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "opf_Metadata40"):
                opp_val = getattr(value, "opf_Metadata40", None)
                if opp_val is None:
                    setattr(value, "opf_Metadata40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class opf_Language:

    pass
class opf_Coverage:

    pass
class opf_Relation:

    pass
class opf_Type:

    pass
class opf_Source:

    pass
class opf_Identifier:

    pass
class opf_Format:

    pass
class opf_Publisher:

    pass
class opf_Description:

    pass
class opf_Date:

    pass
class opf_Subject:

    pass
class opf_Contributor:

    pass
class opf_Creator:

    pass
class opf_Title:

    pass
class opf_Tours:

    pass
class opf_Guide:

    pass
class opf_Spine:

    def __init__(self, toc: str, opf_Spine: "opf_Package" = None, opf_Spine44: set["opf_Itemref"] = None):
        self.toc = toc
        self.opf_Spine = opf_Spine
        self.opf_Spine44 = opf_Spine44 if opf_Spine44 is not None else set()
        
        pass
    @property
    def toc(self):
        return self.__toc

    @toc.setter
    def toc(self, toc: str):
        self.__toc = toc


    @property
    def opf_Spine44(self):
        return self.__opf_Spine44

    @opf_Spine44.setter
    def opf_Spine44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_opf_Spine__opf_Spine44", None)
        self.__opf_Spine44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "opf_Itemref"):
                    opp_val = getattr(item, "opf_Itemref", None)
                    
                    if opp_val == self:
                        setattr(item, "opf_Itemref", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "opf_Itemref"):
                    opp_val = getattr(item, "opf_Itemref", None)
                    
                    setattr(item, "opf_Itemref", self)
                    

    @property
    def opf_Spine(self):
        return self.__opf_Spine

    @opf_Spine.setter
    def opf_Spine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_opf_Spine__opf_Spine", None)
        self.__opf_Spine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "opf_Package4"):
                opp_val = getattr(old_value, "opf_Package4", None)
                if opp_val == self:
                    setattr(old_value, "opf_Package4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "opf_Package4"):
                opp_val = getattr(value, "opf_Package4", None)
                setattr(value, "opf_Package4", self)

class opf_Manifest:

    pass
class opf_Metadata:

    pass
class opf_Package:

    def __init__(self, version: str, uniqueIdentifier: str, generateCoverHTML: bool, generateTableOfContents: bool, includeReferencedResources: bool, prefix: str, lang: str, dir: str, id: str, opf_Package: "opf_Metadata" = None, opf_Package2: "opf_Manifest" = None, opf_Package4: "opf_Spine" = None, opf_Package6: "opf_Guide" = None, opf_Package8: "opf_Tours" = None):
        self.version = version
        self.uniqueIdentifier = uniqueIdentifier
        self.generateCoverHTML = generateCoverHTML
        self.generateTableOfContents = generateTableOfContents
        self.includeReferencedResources = includeReferencedResources
        self.prefix = prefix
        self.lang = lang
        self.dir = dir
        self.id = id
        self.opf_Package = opf_Package
        self.opf_Package2 = opf_Package2
        self.opf_Package4 = opf_Package4
        self.opf_Package6 = opf_Package6
        self.opf_Package8 = opf_Package8
        
        pass
    @property
    def generateTableOfContents(self):
        return self.__generateTableOfContents

    @generateTableOfContents.setter
    def generateTableOfContents(self, generateTableOfContents: bool):
        self.__generateTableOfContents = generateTableOfContents


    @property
    def lang(self):
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang


    @property
    def includeReferencedResources(self):
        return self.__includeReferencedResources

    @includeReferencedResources.setter
    def includeReferencedResources(self, includeReferencedResources: bool):
        self.__includeReferencedResources = includeReferencedResources


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def uniqueIdentifier(self):
        return self.__uniqueIdentifier

    @uniqueIdentifier.setter
    def uniqueIdentifier(self, uniqueIdentifier: str):
        self.__uniqueIdentifier = uniqueIdentifier


    @property
    def prefix(self):
        return self.__prefix

    @prefix.setter
    def prefix(self, prefix: str):
        self.__prefix = prefix


    @property
    def dir(self):
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def generateCoverHTML(self):
        return self.__generateCoverHTML

    @generateCoverHTML.setter
    def generateCoverHTML(self, generateCoverHTML: bool):
        self.__generateCoverHTML = generateCoverHTML


    @property
    def opf_Package(self):
        return self.__opf_Package

    @opf_Package.setter
    def opf_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_opf_Package__opf_Package", None)
        self.__opf_Package = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "opf_Metadata"):
                opp_val = getattr(old_value, "opf_Metadata", None)
                if opp_val == self:
                    setattr(old_value, "opf_Metadata", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "opf_Metadata"):
                opp_val = getattr(value, "opf_Metadata", None)
                setattr(value, "opf_Metadata", self)

    @property
    def opf_Package6(self):
        return self.__opf_Package6

    @opf_Package6.setter
    def opf_Package6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_opf_Package__opf_Package6", None)
        self.__opf_Package6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "opf_Guide"):
                opp_val = getattr(old_value, "opf_Guide", None)
                if opp_val == self:
                    setattr(old_value, "opf_Guide", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "opf_Guide"):
                opp_val = getattr(value, "opf_Guide", None)
                setattr(value, "opf_Guide", self)

    @property
    def opf_Package2(self):
        return self.__opf_Package2

    @opf_Package2.setter
    def opf_Package2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_opf_Package__opf_Package2", None)
        self.__opf_Package2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "opf_Manifest"):
                opp_val = getattr(old_value, "opf_Manifest", None)
                if opp_val == self:
                    setattr(old_value, "opf_Manifest", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "opf_Manifest"):
                opp_val = getattr(value, "opf_Manifest", None)
                setattr(value, "opf_Manifest", self)

    @property
    def opf_Package4(self):
        return self.__opf_Package4

    @opf_Package4.setter
    def opf_Package4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_opf_Package__opf_Package4", None)
        self.__opf_Package4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "opf_Spine"):
                opp_val = getattr(old_value, "opf_Spine", None)
                if opp_val == self:
                    setattr(old_value, "opf_Spine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "opf_Spine"):
                opp_val = getattr(value, "opf_Spine", None)
                setattr(value, "opf_Spine", self)

    @property
    def opf_Package8(self):
        return self.__opf_Package8

    @opf_Package8.setter
    def opf_Package8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_opf_Package__opf_Package8", None)
        self.__opf_Package8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "opf_Tours"):
                opp_val = getattr(old_value, "opf_Tours", None)
                if opp_val == self:
                    setattr(old_value, "opf_Tours", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "opf_Tours"):
                opp_val = getattr(value, "opf_Tours", None)
                setattr(value, "opf_Tours", self)
