import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    opf_Reference,
    opf_Itemref,
    opf_Item,
    opf_Rights,
    opf_Meta,
    opf_Language,
    opf_Source,
    opf_Identifier,
    opf_Coverage,
    opf_Relation,
    opf_Type,
    opf_Date,
    opf_Contributor,
    opf_Format,
    opf_Description,
    opf_Publisher,
    opf_Title,
    opf_Subject,
    opf_Creator,
    opf_Guide,
    opf_Spine,
    opf_Manifest,
    opf_Tours,
    opf_Package,
    opf_Metadata,
    Type,
    Role,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_opf_reference_is_not_abstract():
    assert not inspect.isabstract(opf_Reference)


def test_opf_reference_constructor_exists():
    assert callable(opf_Reference.__init__)


def test_opf_reference_constructor_args():
    sig = inspect.signature(opf_Reference.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "title" in params, "Missing parameter 'title'"
    assert "href" in params, "Missing parameter 'href'"

def test_opf_reference_has_type():
    assert hasattr(opf_Reference, "type")
    descriptor = None
    for klass in opf_Reference.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_opf_reference_has_title():
    assert hasattr(opf_Reference, "title")
    descriptor = None
    for klass in opf_Reference.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_opf_reference_has_href():
    assert hasattr(opf_Reference, "href")
    descriptor = None
    for klass in opf_Reference.__mro__:
        if "href" in klass.__dict__:
            descriptor = klass.__dict__["href"]
            break
    assert isinstance(descriptor, property)



def test_opf_itemref_is_not_abstract():
    assert not inspect.isabstract(opf_Itemref)


def test_opf_itemref_constructor_exists():
    assert callable(opf_Itemref.__init__)


def test_opf_itemref_constructor_args():
    sig = inspect.signature(opf_Itemref.__init__)
    params = list(sig.parameters.keys())
    assert "idref" in params, "Missing parameter 'idref'"
    assert "linear" in params, "Missing parameter 'linear'"

def test_opf_itemref_has_idref():
    assert hasattr(opf_Itemref, "idref")
    descriptor = None
    for klass in opf_Itemref.__mro__:
        if "idref" in klass.__dict__:
            descriptor = klass.__dict__["idref"]
            break
    assert isinstance(descriptor, property)

def test_opf_itemref_has_linear():
    assert hasattr(opf_Itemref, "linear")
    descriptor = None
    for klass in opf_Itemref.__mro__:
        if "linear" in klass.__dict__:
            descriptor = klass.__dict__["linear"]
            break
    assert isinstance(descriptor, property)



def test_opf_item_is_not_abstract():
    assert not inspect.isabstract(opf_Item)


def test_opf_item_constructor_exists():
    assert callable(opf_Item.__init__)


def test_opf_item_constructor_args():
    sig = inspect.signature(opf_Item.__init__)
    params = list(sig.parameters.keys())
    assert "fallback_style" in params, "Missing parameter 'fallback_style'"
    assert "required_namespace" in params, "Missing parameter 'required_namespace'"
    assert "fallback" in params, "Missing parameter 'fallback'"
    assert "required_modules" in params, "Missing parameter 'required_modules'"
    assert "title" in params, "Missing parameter 'title'"
    assert "file" in params, "Missing parameter 'file'"
    assert "generated" in params, "Missing parameter 'generated'"
    assert "media_type" in params, "Missing parameter 'media_type'"
    assert "id" in params, "Missing parameter 'id'"
    assert "href" in params, "Missing parameter 'href'"
    assert "sourcePath" in params, "Missing parameter 'sourcePath'"
    assert "noToc" in params, "Missing parameter 'noToc'"

def test_opf_item_has_fallback_style():
    assert hasattr(opf_Item, "fallback_style")
    descriptor = None
    for klass in opf_Item.__mro__:
        if "fallback_style" in klass.__dict__:
            descriptor = klass.__dict__["fallback_style"]
            break
    assert isinstance(descriptor, property)

def test_opf_item_has_required_namespace():
    assert hasattr(opf_Item, "required_namespace")
    descriptor = None
    for klass in opf_Item.__mro__:
        if "required_namespace" in klass.__dict__:
            descriptor = klass.__dict__["required_namespace"]
            break
    assert isinstance(descriptor, property)

def test_opf_item_has_fallback():
    assert hasattr(opf_Item, "fallback")
    descriptor = None
    for klass in opf_Item.__mro__:
        if "fallback" in klass.__dict__:
            descriptor = klass.__dict__["fallback"]
            break
    assert isinstance(descriptor, property)

def test_opf_item_has_required_modules():
    assert hasattr(opf_Item, "required_modules")
    descriptor = None
    for klass in opf_Item.__mro__:
        if "required_modules" in klass.__dict__:
            descriptor = klass.__dict__["required_modules"]
            break
    assert isinstance(descriptor, property)

def test_opf_item_has_title():
    assert hasattr(opf_Item, "title")
    descriptor = None
    for klass in opf_Item.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_opf_item_has_file():
    assert hasattr(opf_Item, "file")
    descriptor = None
    for klass in opf_Item.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)

def test_opf_item_has_generated():
    assert hasattr(opf_Item, "generated")
    descriptor = None
    for klass in opf_Item.__mro__:
        if "generated" in klass.__dict__:
            descriptor = klass.__dict__["generated"]
            break
    assert isinstance(descriptor, property)

def test_opf_item_has_media_type():
    assert hasattr(opf_Item, "media_type")
    descriptor = None
    for klass in opf_Item.__mro__:
        if "media_type" in klass.__dict__:
            descriptor = klass.__dict__["media_type"]
            break
    assert isinstance(descriptor, property)

def test_opf_item_has_id():
    assert hasattr(opf_Item, "id")
    descriptor = None
    for klass in opf_Item.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_opf_item_has_href():
    assert hasattr(opf_Item, "href")
    descriptor = None
    for klass in opf_Item.__mro__:
        if "href" in klass.__dict__:
            descriptor = klass.__dict__["href"]
            break
    assert isinstance(descriptor, property)

def test_opf_item_has_sourcePath():
    assert hasattr(opf_Item, "sourcePath")
    descriptor = None
    for klass in opf_Item.__mro__:
        if "sourcePath" in klass.__dict__:
            descriptor = klass.__dict__["sourcePath"]
            break
    assert isinstance(descriptor, property)

def test_opf_item_has_noToc():
    assert hasattr(opf_Item, "noToc")
    descriptor = None
    for klass in opf_Item.__mro__:
        if "noToc" in klass.__dict__:
            descriptor = klass.__dict__["noToc"]
            break
    assert isinstance(descriptor, property)



def test_opf_rights_is_not_abstract():
    assert not inspect.isabstract(opf_Rights)


def test_opf_rights_constructor_exists():
    assert callable(opf_Rights.__init__)


def test_opf_rights_constructor_args():
    sig = inspect.signature(opf_Rights.__init__)
    params = list(sig.parameters.keys())



def test_opf_meta_is_not_abstract():
    assert not inspect.isabstract(opf_Meta)


def test_opf_meta_constructor_exists():
    assert callable(opf_Meta.__init__)


def test_opf_meta_constructor_args():
    sig = inspect.signature(opf_Meta.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"
    assert "name" in params, "Missing parameter 'name'"

def test_opf_meta_has_content():
    assert hasattr(opf_Meta, "content")
    descriptor = None
    for klass in opf_Meta.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_opf_meta_has_name():
    assert hasattr(opf_Meta, "name")
    descriptor = None
    for klass in opf_Meta.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_opf_language_is_not_abstract():
    assert not inspect.isabstract(opf_Language)


def test_opf_language_constructor_exists():
    assert callable(opf_Language.__init__)


def test_opf_language_constructor_args():
    sig = inspect.signature(opf_Language.__init__)
    params = list(sig.parameters.keys())



def test_opf_source_is_not_abstract():
    assert not inspect.isabstract(opf_Source)


def test_opf_source_constructor_exists():
    assert callable(opf_Source.__init__)


def test_opf_source_constructor_args():
    sig = inspect.signature(opf_Source.__init__)
    params = list(sig.parameters.keys())



def test_opf_identifier_is_not_abstract():
    assert not inspect.isabstract(opf_Identifier)


def test_opf_identifier_constructor_exists():
    assert callable(opf_Identifier.__init__)


def test_opf_identifier_constructor_args():
    sig = inspect.signature(opf_Identifier.__init__)
    params = list(sig.parameters.keys())



def test_opf_coverage_is_not_abstract():
    assert not inspect.isabstract(opf_Coverage)


def test_opf_coverage_constructor_exists():
    assert callable(opf_Coverage.__init__)


def test_opf_coverage_constructor_args():
    sig = inspect.signature(opf_Coverage.__init__)
    params = list(sig.parameters.keys())



def test_opf_relation_is_not_abstract():
    assert not inspect.isabstract(opf_Relation)


def test_opf_relation_constructor_exists():
    assert callable(opf_Relation.__init__)


def test_opf_relation_constructor_args():
    sig = inspect.signature(opf_Relation.__init__)
    params = list(sig.parameters.keys())



def test_opf_type_is_not_abstract():
    assert not inspect.isabstract(opf_Type)


def test_opf_type_constructor_exists():
    assert callable(opf_Type.__init__)


def test_opf_type_constructor_args():
    sig = inspect.signature(opf_Type.__init__)
    params = list(sig.parameters.keys())



def test_opf_date_is_not_abstract():
    assert not inspect.isabstract(opf_Date)


def test_opf_date_constructor_exists():
    assert callable(opf_Date.__init__)


def test_opf_date_constructor_args():
    sig = inspect.signature(opf_Date.__init__)
    params = list(sig.parameters.keys())



def test_opf_contributor_is_not_abstract():
    assert not inspect.isabstract(opf_Contributor)


def test_opf_contributor_constructor_exists():
    assert callable(opf_Contributor.__init__)


def test_opf_contributor_constructor_args():
    sig = inspect.signature(opf_Contributor.__init__)
    params = list(sig.parameters.keys())



def test_opf_format_is_not_abstract():
    assert not inspect.isabstract(opf_Format)


def test_opf_format_constructor_exists():
    assert callable(opf_Format.__init__)


def test_opf_format_constructor_args():
    sig = inspect.signature(opf_Format.__init__)
    params = list(sig.parameters.keys())



def test_opf_description_is_not_abstract():
    assert not inspect.isabstract(opf_Description)


def test_opf_description_constructor_exists():
    assert callable(opf_Description.__init__)


def test_opf_description_constructor_args():
    sig = inspect.signature(opf_Description.__init__)
    params = list(sig.parameters.keys())



def test_opf_publisher_is_not_abstract():
    assert not inspect.isabstract(opf_Publisher)


def test_opf_publisher_constructor_exists():
    assert callable(opf_Publisher.__init__)


def test_opf_publisher_constructor_args():
    sig = inspect.signature(opf_Publisher.__init__)
    params = list(sig.parameters.keys())



def test_opf_title_is_not_abstract():
    assert not inspect.isabstract(opf_Title)


def test_opf_title_constructor_exists():
    assert callable(opf_Title.__init__)


def test_opf_title_constructor_args():
    sig = inspect.signature(opf_Title.__init__)
    params = list(sig.parameters.keys())



def test_opf_subject_is_not_abstract():
    assert not inspect.isabstract(opf_Subject)


def test_opf_subject_constructor_exists():
    assert callable(opf_Subject.__init__)


def test_opf_subject_constructor_args():
    sig = inspect.signature(opf_Subject.__init__)
    params = list(sig.parameters.keys())



def test_opf_creator_is_not_abstract():
    assert not inspect.isabstract(opf_Creator)


def test_opf_creator_constructor_exists():
    assert callable(opf_Creator.__init__)


def test_opf_creator_constructor_args():
    sig = inspect.signature(opf_Creator.__init__)
    params = list(sig.parameters.keys())



def test_opf_guide_is_not_abstract():
    assert not inspect.isabstract(opf_Guide)


def test_opf_guide_constructor_exists():
    assert callable(opf_Guide.__init__)


def test_opf_guide_constructor_args():
    sig = inspect.signature(opf_Guide.__init__)
    params = list(sig.parameters.keys())



def test_opf_spine_is_not_abstract():
    assert not inspect.isabstract(opf_Spine)


def test_opf_spine_constructor_exists():
    assert callable(opf_Spine.__init__)


def test_opf_spine_constructor_args():
    sig = inspect.signature(opf_Spine.__init__)
    params = list(sig.parameters.keys())
    assert "toc" in params, "Missing parameter 'toc'"

def test_opf_spine_has_toc():
    assert hasattr(opf_Spine, "toc")
    descriptor = None
    for klass in opf_Spine.__mro__:
        if "toc" in klass.__dict__:
            descriptor = klass.__dict__["toc"]
            break
    assert isinstance(descriptor, property)



def test_opf_manifest_is_not_abstract():
    assert not inspect.isabstract(opf_Manifest)


def test_opf_manifest_constructor_exists():
    assert callable(opf_Manifest.__init__)


def test_opf_manifest_constructor_args():
    sig = inspect.signature(opf_Manifest.__init__)
    params = list(sig.parameters.keys())



def test_opf_tours_is_not_abstract():
    assert not inspect.isabstract(opf_Tours)


def test_opf_tours_constructor_exists():
    assert callable(opf_Tours.__init__)


def test_opf_tours_constructor_args():
    sig = inspect.signature(opf_Tours.__init__)
    params = list(sig.parameters.keys())



def test_opf_package_is_not_abstract():
    assert not inspect.isabstract(opf_Package)


def test_opf_package_constructor_exists():
    assert callable(opf_Package.__init__)


def test_opf_package_constructor_args():
    sig = inspect.signature(opf_Package.__init__)
    params = list(sig.parameters.keys())
    assert "generateCoverHTML" in params, "Missing parameter 'generateCoverHTML'"
    assert "uniqueIdentifier" in params, "Missing parameter 'uniqueIdentifier'"
    assert "generateTableOfContents" in params, "Missing parameter 'generateTableOfContents'"
    assert "includeReferencedResources" in params, "Missing parameter 'includeReferencedResources'"
    assert "version" in params, "Missing parameter 'version'"

def test_opf_package_has_generateCoverHTML():
    assert hasattr(opf_Package, "generateCoverHTML")
    descriptor = None
    for klass in opf_Package.__mro__:
        if "generateCoverHTML" in klass.__dict__:
            descriptor = klass.__dict__["generateCoverHTML"]
            break
    assert isinstance(descriptor, property)

def test_opf_package_has_uniqueIdentifier():
    assert hasattr(opf_Package, "uniqueIdentifier")
    descriptor = None
    for klass in opf_Package.__mro__:
        if "uniqueIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["uniqueIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_opf_package_has_generateTableOfContents():
    assert hasattr(opf_Package, "generateTableOfContents")
    descriptor = None
    for klass in opf_Package.__mro__:
        if "generateTableOfContents" in klass.__dict__:
            descriptor = klass.__dict__["generateTableOfContents"]
            break
    assert isinstance(descriptor, property)

def test_opf_package_has_includeReferencedResources():
    assert hasattr(opf_Package, "includeReferencedResources")
    descriptor = None
    for klass in opf_Package.__mro__:
        if "includeReferencedResources" in klass.__dict__:
            descriptor = klass.__dict__["includeReferencedResources"]
            break
    assert isinstance(descriptor, property)

def test_opf_package_has_version():
    assert hasattr(opf_Package, "version")
    descriptor = None
    for klass in opf_Package.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_opf_metadata_is_not_abstract():
    assert not inspect.isabstract(opf_Metadata)


def test_opf_metadata_constructor_exists():
    assert callable(opf_Metadata.__init__)


def test_opf_metadata_constructor_args():
    sig = inspect.signature(opf_Metadata.__init__)
    params = list(sig.parameters.keys())

def test_type_exists():
    # Check that the Enumeration exists
    assert Type is not None

def test_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Type]
    expected_literals = [
        "Title",
        "Tables",
        "Index",
        "Copyright",
        "Preface",
        "Notes",
        "Bibliography",
        "Epigraph",
        "Foreword",
        "Illustrations",
        "Colophon",
        "TOC",
        "Cover",
        "Text",
        "Glossary",
        "Acknowledgements",
        "Dedication",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Type"

def test_role_exists():
    # Check that the Enumeration exists
    assert Role is not None

def test_role_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Role]
    expected_literals = [
        "Bibliographic_antecedent",
        "Instrumentalist",
        "Funder",
        "Libelant_appellee",
        "Dedicatee",
        "Publisher",
        "Musical_director",
        "Plaintiff_appellee",
        "Teacher",
        "Colorist",
        "Etcher",
        "Actor",
        "Facsimilist",
        "Patron",
        "Patent_applicant",
        "Animator",
        "Consultant",
        "Choreographer",
        "Libelant",
        "Recording_engineer",
        "Dancer",
        "Libelant_appellant",
        "Respondent_appellant",
        "Set_designer",
        "Vocalist",
        "Donor",
        "Marbler",
        "Metadata_contact",
        "Commentator_for_written_text",
        "Engraver",
        "Manufacturer",
        "Book_producer",
        "Librettist",
        "Research_team_member",
        "Host",
        "Standards_body",
        "Depicted",
        "Contestant",
        "Geographic_information_specialist",
        "Cover_designer",
        "Libelee_appellee",
        "Illustrator",
        "Correspondent",
        "Defendant_appellant",
        "University_place",
        "Wood_engraver",
        "Platemaker",
        "Field_director",
        "Contestee",
        "Printer_of_plates",
        "Associated_name",
        "Originator",
        "Printer",
        "Dedicator",
        "Electrician",
        "Binder",
        "Performer",
        "Book_designer",
        "Art_copyist",
        "Data_manager",
        "Conductor",
        "Writer_of_accompanying_material",
        "Former_owner",
        "Delineator",
        "Research_team_head",
        "Collotyper",
        "Woodcutter",
        "Transcriber",
        "Papermaker",
        "Artistic_director",
        "Composer",
        "Laboratory_director",
        "Researcher",
        "Honoree",
        "Contestant_appellant",
        "Second_party",
        "First_party",
        "Illuminator",
        "Complainant_appellant",
        "Surveyor",
        "Interviewer",
        "Author_of_dialog",
        "Technical_director",
        "Sound_designer",
        "Moderator",
        "Publication_place",
        "Owner",
        "Renderer",
        "Annotator",
        "Bookplate_designer",
        "Contestee_appellee",
        "Laboratory",
        "Landscape_architect",
        "Organizer_of_meeting",
        "Bookseller",
        "Author_in_quotations_or_text_abstracts",
        "Contractor",
        "Singer",
        "Licensor",
        "Corrector",
        "Interviewee",
        "Defendant",
        "Libelee",
        "Director",
        "Production_place",
        "Responsible_party",
        "Distribution_place",
        "Witness",
        "Collector",
        "Blurb_writer",
        "Programmer",
        "Graphic_technician",
        "Redactor",
        "Author_of_afterword_colophon_etc",
        "Complainant",
        "Reviewer",
        "Type_designer",
        "Film_editor",
        "Censor",
        "Compiler",
        "Production_manager",
        "Reporter",
        "Cartographer",
        "Secretary",
        "Contributor",
        "Forger",
        "Music_copyist",
        "Distributor",
        "Proofreader",
        "Production_personnel",
        "Sculptor",
        "Respondent_appellee",
        "Typographer",
        "Conceptor",
        "Complainant_appellee",
        "Sponsor",
        "Event_place",
        "Contestee_appellant",
        "Signer",
        "Libelee_appellant",
        "Speaker",
        "Lighting_designer",
        "Attributed_name",
        "Photographer",
        "Cinematographer",
        "Commentator",
        "Dissertant",
        "Scenarist",
        "Creator",
        "Stage_manager",
        "Engineer",
        "Expert",
        "Scribe",
        "Defendant_appellee",
        "Publishing_director",
        "Applicant",
        "Depositor",
        "Lithographer",
        "Copyright_claimant",
        "Musician",
        "Process_contact",
        "Permitting_agency",
        "Opponent",
        "Rubricator",
        "Plaintiff",
        "Stereotyper",
        "Markup_editor",
        "Compositor",
        "Editor",
        "Author_of_screenplay",
        "Recipient",
        "Respondent",
        "Curator",
        "Author_of_introduction",
        "Inventor",
        "Scientific_advisor",
        "Thesis_advisor",
        "Dubious_author",
        "Lender",
        "Artist",
        "Assignee",
        "Electrotyper",
        "Restager",
        "Client",
        "Manufacture_place",
        "Puppeteer",
        "Supporting_host",
        "Adapter",
        "Patent_holder",
        "Consultant_to_a_project",
        "Contestant_appellee",
        "Bookjacket_designer",
        "Metal_engraver",
        "Auctioneer",
        "Data_contributor",
        "Designer",
        "Author",
        "Plaintiff_appellant",
        "Narrator",
        "Lyricist",
        "Collaborator",
        "Videographer",
        "Project_director",
        "Storyteller",
        "Inscriber",
        "Costume_designer",
        "Producer",
        "Calligrapher",
        "Architect",
        "Copyright_holder",
        "Analyst",
        "Draftsman",
        "Repository",
        "Printmaker",
        "Translator",
        "Arranger",
        "Degree_grantor",
        "Monitor",
        "Licensee",
        "Binding_designer",
        "Other",
        "Lead",
        "Conservator",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Role"


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
opf_Reference_strategy = st.builds(
    opf_Reference,
    type=
        safe_text,
    title=
        safe_text,
    href=
        safe_text
)
opf_Itemref_strategy = st.builds(
    opf_Itemref,
    idref=
        safe_text,
    linear=
        safe_text
)
opf_Item_strategy = st.builds(
    opf_Item,
    fallback_style=
        safe_text,
    required_namespace=
        safe_text,
    fallback=
        safe_text,
    required_modules=
        safe_text,
    title=
        safe_text,
    file=
        safe_text,
    generated=
        st.booleans(),
    media_type=
        safe_text,
    id=
        safe_text,
    href=
        safe_text,
    sourcePath=
        safe_text,
    noToc=
        st.booleans()
)
opf_Rights_strategy = st.builds(
    opf_Rights,
)
opf_Meta_strategy = st.builds(
    opf_Meta,
    content=
        safe_text,
    name=
        safe_text
)
opf_Language_strategy = st.builds(
    opf_Language,
)
opf_Source_strategy = st.builds(
    opf_Source,
)
opf_Identifier_strategy = st.builds(
    opf_Identifier,
)
opf_Coverage_strategy = st.builds(
    opf_Coverage,
)
opf_Relation_strategy = st.builds(
    opf_Relation,
)
opf_Type_strategy = st.builds(
    opf_Type,
)
opf_Date_strategy = st.builds(
    opf_Date,
)
opf_Contributor_strategy = st.builds(
    opf_Contributor,
)
opf_Format_strategy = st.builds(
    opf_Format,
)
opf_Description_strategy = st.builds(
    opf_Description,
)
opf_Publisher_strategy = st.builds(
    opf_Publisher,
)
opf_Title_strategy = st.builds(
    opf_Title,
)
opf_Subject_strategy = st.builds(
    opf_Subject,
)
opf_Creator_strategy = st.builds(
    opf_Creator,
)
opf_Guide_strategy = st.builds(
    opf_Guide,
)
opf_Spine_strategy = st.builds(
    opf_Spine,
    toc=
        safe_text
)
opf_Manifest_strategy = st.builds(
    opf_Manifest,
)
opf_Tours_strategy = st.builds(
    opf_Tours,
)
opf_Package_strategy = st.builds(
    opf_Package,
    generateCoverHTML=
        st.booleans(),
    uniqueIdentifier=
        safe_text,
    generateTableOfContents=
        st.booleans(),
    includeReferencedResources=
        st.booleans(),
    version=
        safe_text
)
opf_Metadata_strategy = st.builds(
    opf_Metadata,
)

@given(instance=opf_Reference_strategy)
@settings(max_examples=50)
def test_opf_reference_instantiation(instance):
    assert isinstance(instance, opf_Reference)



@given(instance=opf_Reference_strategy)
def test_opf_reference_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=opf_Reference_strategy)
def test_opf_reference_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=opf_Reference_strategy)
def test_opf_reference_href_setter(instance):
    original = instance.href
    instance.href = original
    assert instance.href == original

@given(instance=opf_Itemref_strategy)
@settings(max_examples=50)
def test_opf_itemref_instantiation(instance):
    assert isinstance(instance, opf_Itemref)



@given(instance=opf_Itemref_strategy)
def test_opf_itemref_idref_setter(instance):
    original = instance.idref
    instance.idref = original
    assert instance.idref == original



@given(instance=opf_Itemref_strategy)
def test_opf_itemref_linear_setter(instance):
    original = instance.linear
    instance.linear = original
    assert instance.linear == original

@given(instance=opf_Item_strategy)
@settings(max_examples=50)
def test_opf_item_instantiation(instance):
    assert isinstance(instance, opf_Item)



@given(instance=opf_Item_strategy)
def test_opf_item_fallback_style_setter(instance):
    original = instance.fallback_style
    instance.fallback_style = original
    assert instance.fallback_style == original



@given(instance=opf_Item_strategy)
def test_opf_item_required_namespace_setter(instance):
    original = instance.required_namespace
    instance.required_namespace = original
    assert instance.required_namespace == original



@given(instance=opf_Item_strategy)
def test_opf_item_fallback_setter(instance):
    original = instance.fallback
    instance.fallback = original
    assert instance.fallback == original



@given(instance=opf_Item_strategy)
def test_opf_item_required_modules_setter(instance):
    original = instance.required_modules
    instance.required_modules = original
    assert instance.required_modules == original



@given(instance=opf_Item_strategy)
def test_opf_item_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=opf_Item_strategy)
def test_opf_item_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original



@given(instance=opf_Item_strategy)
def test_opf_item_generated_setter(instance):
    original = instance.generated
    instance.generated = original
    assert instance.generated == original



@given(instance=opf_Item_strategy)
def test_opf_item_media_type_setter(instance):
    original = instance.media_type
    instance.media_type = original
    assert instance.media_type == original



@given(instance=opf_Item_strategy)
def test_opf_item_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=opf_Item_strategy)
def test_opf_item_href_setter(instance):
    original = instance.href
    instance.href = original
    assert instance.href == original



@given(instance=opf_Item_strategy)
def test_opf_item_sourcePath_setter(instance):
    original = instance.sourcePath
    instance.sourcePath = original
    assert instance.sourcePath == original



@given(instance=opf_Item_strategy)
def test_opf_item_noToc_setter(instance):
    original = instance.noToc
    instance.noToc = original
    assert instance.noToc == original

@given(instance=opf_Rights_strategy)
@settings(max_examples=50)
def test_opf_rights_instantiation(instance):
    assert isinstance(instance, opf_Rights)

@given(instance=opf_Meta_strategy)
@settings(max_examples=50)
def test_opf_meta_instantiation(instance):
    assert isinstance(instance, opf_Meta)



@given(instance=opf_Meta_strategy)
def test_opf_meta_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original



@given(instance=opf_Meta_strategy)
def test_opf_meta_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=opf_Language_strategy)
@settings(max_examples=50)
def test_opf_language_instantiation(instance):
    assert isinstance(instance, opf_Language)

@given(instance=opf_Source_strategy)
@settings(max_examples=50)
def test_opf_source_instantiation(instance):
    assert isinstance(instance, opf_Source)

@given(instance=opf_Identifier_strategy)
@settings(max_examples=50)
def test_opf_identifier_instantiation(instance):
    assert isinstance(instance, opf_Identifier)

@given(instance=opf_Coverage_strategy)
@settings(max_examples=50)
def test_opf_coverage_instantiation(instance):
    assert isinstance(instance, opf_Coverage)

@given(instance=opf_Relation_strategy)
@settings(max_examples=50)
def test_opf_relation_instantiation(instance):
    assert isinstance(instance, opf_Relation)

@given(instance=opf_Type_strategy)
@settings(max_examples=50)
def test_opf_type_instantiation(instance):
    assert isinstance(instance, opf_Type)

@given(instance=opf_Date_strategy)
@settings(max_examples=50)
def test_opf_date_instantiation(instance):
    assert isinstance(instance, opf_Date)

@given(instance=opf_Contributor_strategy)
@settings(max_examples=50)
def test_opf_contributor_instantiation(instance):
    assert isinstance(instance, opf_Contributor)

@given(instance=opf_Format_strategy)
@settings(max_examples=50)
def test_opf_format_instantiation(instance):
    assert isinstance(instance, opf_Format)

@given(instance=opf_Description_strategy)
@settings(max_examples=50)
def test_opf_description_instantiation(instance):
    assert isinstance(instance, opf_Description)

@given(instance=opf_Publisher_strategy)
@settings(max_examples=50)
def test_opf_publisher_instantiation(instance):
    assert isinstance(instance, opf_Publisher)

@given(instance=opf_Title_strategy)
@settings(max_examples=50)
def test_opf_title_instantiation(instance):
    assert isinstance(instance, opf_Title)

@given(instance=opf_Subject_strategy)
@settings(max_examples=50)
def test_opf_subject_instantiation(instance):
    assert isinstance(instance, opf_Subject)

@given(instance=opf_Creator_strategy)
@settings(max_examples=50)
def test_opf_creator_instantiation(instance):
    assert isinstance(instance, opf_Creator)

@given(instance=opf_Guide_strategy)
@settings(max_examples=50)
def test_opf_guide_instantiation(instance):
    assert isinstance(instance, opf_Guide)

@given(instance=opf_Spine_strategy)
@settings(max_examples=50)
def test_opf_spine_instantiation(instance):
    assert isinstance(instance, opf_Spine)



@given(instance=opf_Spine_strategy)
def test_opf_spine_toc_setter(instance):
    original = instance.toc
    instance.toc = original
    assert instance.toc == original

@given(instance=opf_Manifest_strategy)
@settings(max_examples=50)
def test_opf_manifest_instantiation(instance):
    assert isinstance(instance, opf_Manifest)

@given(instance=opf_Tours_strategy)
@settings(max_examples=50)
def test_opf_tours_instantiation(instance):
    assert isinstance(instance, opf_Tours)

@given(instance=opf_Package_strategy)
@settings(max_examples=50)
def test_opf_package_instantiation(instance):
    assert isinstance(instance, opf_Package)



@given(instance=opf_Package_strategy)
def test_opf_package_generateCoverHTML_setter(instance):
    original = instance.generateCoverHTML
    instance.generateCoverHTML = original
    assert instance.generateCoverHTML == original



@given(instance=opf_Package_strategy)
def test_opf_package_uniqueIdentifier_setter(instance):
    original = instance.uniqueIdentifier
    instance.uniqueIdentifier = original
    assert instance.uniqueIdentifier == original



@given(instance=opf_Package_strategy)
def test_opf_package_generateTableOfContents_setter(instance):
    original = instance.generateTableOfContents
    instance.generateTableOfContents = original
    assert instance.generateTableOfContents == original



@given(instance=opf_Package_strategy)
def test_opf_package_includeReferencedResources_setter(instance):
    original = instance.includeReferencedResources
    instance.includeReferencedResources = original
    assert instance.includeReferencedResources == original



@given(instance=opf_Package_strategy)
def test_opf_package_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=opf_Metadata_strategy)
@settings(max_examples=50)
def test_opf_metadata_instantiation(instance):
    assert isinstance(instance, opf_Metadata)
