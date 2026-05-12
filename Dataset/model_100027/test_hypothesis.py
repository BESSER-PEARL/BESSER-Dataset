import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    opf::Reference,
    opf::Itemref,
    opf::Item,
    opf::Rights,
    opf::Meta,
    opf::Language,
    opf::Source,
    opf::Identifier,
    opf::Coverage,
    opf::Relation,
    opf::Type,
    opf::Date,
    opf::Contributor,
    opf::Format,
    opf::Description,
    opf::Publisher,
    opf::Title,
    opf::Subject,
    opf::Creator,
    opf::Guide,
    opf::Spine,
    opf::Manifest,
    opf::Tours,
    opf::Package,
    opf::Metadata,
    Role,
    Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_opf::reference_is_not_abstract():
    assert not inspect.isabstract(opf::Reference)


def test_opf::reference_constructor_exists():
    assert callable(opf::Reference.__init__)


def test_opf::reference_constructor_args():
    sig = inspect.signature(opf::Reference.__init__)
    params = list(sig.parameters.keys())
    assert "href" in params, "Missing parameter 'href'"
    assert "type" in params, "Missing parameter 'type'"
    assert "title" in params, "Missing parameter 'title'"

def test_opf::reference_has_href():
    assert hasattr(opf::Reference, "href")
    descriptor = None
    for klass in opf::Reference.__mro__:
        if "href" in klass.__dict__:
            descriptor = klass.__dict__["href"]
            break
    assert isinstance(descriptor, property)

def test_opf::reference_has_type():
    assert hasattr(opf::Reference, "type")
    descriptor = None
    for klass in opf::Reference.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_opf::reference_has_title():
    assert hasattr(opf::Reference, "title")
    descriptor = None
    for klass in opf::Reference.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_opf::itemref_is_not_abstract():
    assert not inspect.isabstract(opf::Itemref)


def test_opf::itemref_constructor_exists():
    assert callable(opf::Itemref.__init__)


def test_opf::itemref_constructor_args():
    sig = inspect.signature(opf::Itemref.__init__)
    params = list(sig.parameters.keys())
    assert "linear" in params, "Missing parameter 'linear'"
    assert "idref" in params, "Missing parameter 'idref'"

def test_opf::itemref_has_linear():
    assert hasattr(opf::Itemref, "linear")
    descriptor = None
    for klass in opf::Itemref.__mro__:
        if "linear" in klass.__dict__:
            descriptor = klass.__dict__["linear"]
            break
    assert isinstance(descriptor, property)

def test_opf::itemref_has_idref():
    assert hasattr(opf::Itemref, "idref")
    descriptor = None
    for klass in opf::Itemref.__mro__:
        if "idref" in klass.__dict__:
            descriptor = klass.__dict__["idref"]
            break
    assert isinstance(descriptor, property)



def test_opf::item_is_not_abstract():
    assert not inspect.isabstract(opf::Item)


def test_opf::item_constructor_exists():
    assert callable(opf::Item.__init__)


def test_opf::item_constructor_args():
    sig = inspect.signature(opf::Item.__init__)
    params = list(sig.parameters.keys())
    assert "media_type" in params, "Missing parameter 'media_type'"
    assert "sourcePath" in params, "Missing parameter 'sourcePath'"
    assert "file" in params, "Missing parameter 'file'"
    assert "generated" in params, "Missing parameter 'generated'"
    assert "required_namespace" in params, "Missing parameter 'required_namespace'"
    assert "id" in params, "Missing parameter 'id'"
    assert "title" in params, "Missing parameter 'title'"
    assert "fallback_style" in params, "Missing parameter 'fallback_style'"
    assert "required_modules" in params, "Missing parameter 'required_modules'"
    assert "fallback" in params, "Missing parameter 'fallback'"
    assert "href" in params, "Missing parameter 'href'"
    assert "noToc" in params, "Missing parameter 'noToc'"

def test_opf::item_has_media_type():
    assert hasattr(opf::Item, "media_type")
    descriptor = None
    for klass in opf::Item.__mro__:
        if "media_type" in klass.__dict__:
            descriptor = klass.__dict__["media_type"]
            break
    assert isinstance(descriptor, property)

def test_opf::item_has_sourcePath():
    assert hasattr(opf::Item, "sourcePath")
    descriptor = None
    for klass in opf::Item.__mro__:
        if "sourcePath" in klass.__dict__:
            descriptor = klass.__dict__["sourcePath"]
            break
    assert isinstance(descriptor, property)

def test_opf::item_has_file():
    assert hasattr(opf::Item, "file")
    descriptor = None
    for klass in opf::Item.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)

def test_opf::item_has_generated():
    assert hasattr(opf::Item, "generated")
    descriptor = None
    for klass in opf::Item.__mro__:
        if "generated" in klass.__dict__:
            descriptor = klass.__dict__["generated"]
            break
    assert isinstance(descriptor, property)

def test_opf::item_has_required_namespace():
    assert hasattr(opf::Item, "required_namespace")
    descriptor = None
    for klass in opf::Item.__mro__:
        if "required_namespace" in klass.__dict__:
            descriptor = klass.__dict__["required_namespace"]
            break
    assert isinstance(descriptor, property)

def test_opf::item_has_id():
    assert hasattr(opf::Item, "id")
    descriptor = None
    for klass in opf::Item.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_opf::item_has_title():
    assert hasattr(opf::Item, "title")
    descriptor = None
    for klass in opf::Item.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_opf::item_has_fallback_style():
    assert hasattr(opf::Item, "fallback_style")
    descriptor = None
    for klass in opf::Item.__mro__:
        if "fallback_style" in klass.__dict__:
            descriptor = klass.__dict__["fallback_style"]
            break
    assert isinstance(descriptor, property)

def test_opf::item_has_required_modules():
    assert hasattr(opf::Item, "required_modules")
    descriptor = None
    for klass in opf::Item.__mro__:
        if "required_modules" in klass.__dict__:
            descriptor = klass.__dict__["required_modules"]
            break
    assert isinstance(descriptor, property)

def test_opf::item_has_fallback():
    assert hasattr(opf::Item, "fallback")
    descriptor = None
    for klass in opf::Item.__mro__:
        if "fallback" in klass.__dict__:
            descriptor = klass.__dict__["fallback"]
            break
    assert isinstance(descriptor, property)

def test_opf::item_has_href():
    assert hasattr(opf::Item, "href")
    descriptor = None
    for klass in opf::Item.__mro__:
        if "href" in klass.__dict__:
            descriptor = klass.__dict__["href"]
            break
    assert isinstance(descriptor, property)

def test_opf::item_has_noToc():
    assert hasattr(opf::Item, "noToc")
    descriptor = None
    for klass in opf::Item.__mro__:
        if "noToc" in klass.__dict__:
            descriptor = klass.__dict__["noToc"]
            break
    assert isinstance(descriptor, property)



def test_opf::rights_is_not_abstract():
    assert not inspect.isabstract(opf::Rights)


def test_opf::rights_constructor_exists():
    assert callable(opf::Rights.__init__)


def test_opf::rights_constructor_args():
    sig = inspect.signature(opf::Rights.__init__)
    params = list(sig.parameters.keys())



def test_opf::meta_is_not_abstract():
    assert not inspect.isabstract(opf::Meta)


def test_opf::meta_constructor_exists():
    assert callable(opf::Meta.__init__)


def test_opf::meta_constructor_args():
    sig = inspect.signature(opf::Meta.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "content" in params, "Missing parameter 'content'"

def test_opf::meta_has_name():
    assert hasattr(opf::Meta, "name")
    descriptor = None
    for klass in opf::Meta.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_opf::meta_has_content():
    assert hasattr(opf::Meta, "content")
    descriptor = None
    for klass in opf::Meta.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_opf::language_is_not_abstract():
    assert not inspect.isabstract(opf::Language)


def test_opf::language_constructor_exists():
    assert callable(opf::Language.__init__)


def test_opf::language_constructor_args():
    sig = inspect.signature(opf::Language.__init__)
    params = list(sig.parameters.keys())



def test_opf::source_is_not_abstract():
    assert not inspect.isabstract(opf::Source)


def test_opf::source_constructor_exists():
    assert callable(opf::Source.__init__)


def test_opf::source_constructor_args():
    sig = inspect.signature(opf::Source.__init__)
    params = list(sig.parameters.keys())



def test_opf::identifier_is_not_abstract():
    assert not inspect.isabstract(opf::Identifier)


def test_opf::identifier_constructor_exists():
    assert callable(opf::Identifier.__init__)


def test_opf::identifier_constructor_args():
    sig = inspect.signature(opf::Identifier.__init__)
    params = list(sig.parameters.keys())



def test_opf::coverage_is_not_abstract():
    assert not inspect.isabstract(opf::Coverage)


def test_opf::coverage_constructor_exists():
    assert callable(opf::Coverage.__init__)


def test_opf::coverage_constructor_args():
    sig = inspect.signature(opf::Coverage.__init__)
    params = list(sig.parameters.keys())



def test_opf::relation_is_not_abstract():
    assert not inspect.isabstract(opf::Relation)


def test_opf::relation_constructor_exists():
    assert callable(opf::Relation.__init__)


def test_opf::relation_constructor_args():
    sig = inspect.signature(opf::Relation.__init__)
    params = list(sig.parameters.keys())



def test_opf::type_is_not_abstract():
    assert not inspect.isabstract(opf::Type)


def test_opf::type_constructor_exists():
    assert callable(opf::Type.__init__)


def test_opf::type_constructor_args():
    sig = inspect.signature(opf::Type.__init__)
    params = list(sig.parameters.keys())



def test_opf::date_is_not_abstract():
    assert not inspect.isabstract(opf::Date)


def test_opf::date_constructor_exists():
    assert callable(opf::Date.__init__)


def test_opf::date_constructor_args():
    sig = inspect.signature(opf::Date.__init__)
    params = list(sig.parameters.keys())



def test_opf::contributor_is_not_abstract():
    assert not inspect.isabstract(opf::Contributor)


def test_opf::contributor_constructor_exists():
    assert callable(opf::Contributor.__init__)


def test_opf::contributor_constructor_args():
    sig = inspect.signature(opf::Contributor.__init__)
    params = list(sig.parameters.keys())



def test_opf::format_is_not_abstract():
    assert not inspect.isabstract(opf::Format)


def test_opf::format_constructor_exists():
    assert callable(opf::Format.__init__)


def test_opf::format_constructor_args():
    sig = inspect.signature(opf::Format.__init__)
    params = list(sig.parameters.keys())



def test_opf::description_is_not_abstract():
    assert not inspect.isabstract(opf::Description)


def test_opf::description_constructor_exists():
    assert callable(opf::Description.__init__)


def test_opf::description_constructor_args():
    sig = inspect.signature(opf::Description.__init__)
    params = list(sig.parameters.keys())



def test_opf::publisher_is_not_abstract():
    assert not inspect.isabstract(opf::Publisher)


def test_opf::publisher_constructor_exists():
    assert callable(opf::Publisher.__init__)


def test_opf::publisher_constructor_args():
    sig = inspect.signature(opf::Publisher.__init__)
    params = list(sig.parameters.keys())



def test_opf::title_is_not_abstract():
    assert not inspect.isabstract(opf::Title)


def test_opf::title_constructor_exists():
    assert callable(opf::Title.__init__)


def test_opf::title_constructor_args():
    sig = inspect.signature(opf::Title.__init__)
    params = list(sig.parameters.keys())



def test_opf::subject_is_not_abstract():
    assert not inspect.isabstract(opf::Subject)


def test_opf::subject_constructor_exists():
    assert callable(opf::Subject.__init__)


def test_opf::subject_constructor_args():
    sig = inspect.signature(opf::Subject.__init__)
    params = list(sig.parameters.keys())



def test_opf::creator_is_not_abstract():
    assert not inspect.isabstract(opf::Creator)


def test_opf::creator_constructor_exists():
    assert callable(opf::Creator.__init__)


def test_opf::creator_constructor_args():
    sig = inspect.signature(opf::Creator.__init__)
    params = list(sig.parameters.keys())



def test_opf::guide_is_not_abstract():
    assert not inspect.isabstract(opf::Guide)


def test_opf::guide_constructor_exists():
    assert callable(opf::Guide.__init__)


def test_opf::guide_constructor_args():
    sig = inspect.signature(opf::Guide.__init__)
    params = list(sig.parameters.keys())



def test_opf::spine_is_not_abstract():
    assert not inspect.isabstract(opf::Spine)


def test_opf::spine_constructor_exists():
    assert callable(opf::Spine.__init__)


def test_opf::spine_constructor_args():
    sig = inspect.signature(opf::Spine.__init__)
    params = list(sig.parameters.keys())
    assert "toc" in params, "Missing parameter 'toc'"

def test_opf::spine_has_toc():
    assert hasattr(opf::Spine, "toc")
    descriptor = None
    for klass in opf::Spine.__mro__:
        if "toc" in klass.__dict__:
            descriptor = klass.__dict__["toc"]
            break
    assert isinstance(descriptor, property)



def test_opf::manifest_is_not_abstract():
    assert not inspect.isabstract(opf::Manifest)


def test_opf::manifest_constructor_exists():
    assert callable(opf::Manifest.__init__)


def test_opf::manifest_constructor_args():
    sig = inspect.signature(opf::Manifest.__init__)
    params = list(sig.parameters.keys())



def test_opf::tours_is_not_abstract():
    assert not inspect.isabstract(opf::Tours)


def test_opf::tours_constructor_exists():
    assert callable(opf::Tours.__init__)


def test_opf::tours_constructor_args():
    sig = inspect.signature(opf::Tours.__init__)
    params = list(sig.parameters.keys())



def test_opf::package_is_not_abstract():
    assert not inspect.isabstract(opf::Package)


def test_opf::package_constructor_exists():
    assert callable(opf::Package.__init__)


def test_opf::package_constructor_args():
    sig = inspect.signature(opf::Package.__init__)
    params = list(sig.parameters.keys())
    assert "includeReferencedResources" in params, "Missing parameter 'includeReferencedResources'"
    assert "generateCoverHTML" in params, "Missing parameter 'generateCoverHTML'"
    assert "version" in params, "Missing parameter 'version'"
    assert "generateTableOfContents" in params, "Missing parameter 'generateTableOfContents'"
    assert "uniqueIdentifier" in params, "Missing parameter 'uniqueIdentifier'"

def test_opf::package_has_includeReferencedResources():
    assert hasattr(opf::Package, "includeReferencedResources")
    descriptor = None
    for klass in opf::Package.__mro__:
        if "includeReferencedResources" in klass.__dict__:
            descriptor = klass.__dict__["includeReferencedResources"]
            break
    assert isinstance(descriptor, property)

def test_opf::package_has_generateCoverHTML():
    assert hasattr(opf::Package, "generateCoverHTML")
    descriptor = None
    for klass in opf::Package.__mro__:
        if "generateCoverHTML" in klass.__dict__:
            descriptor = klass.__dict__["generateCoverHTML"]
            break
    assert isinstance(descriptor, property)

def test_opf::package_has_version():
    assert hasattr(opf::Package, "version")
    descriptor = None
    for klass in opf::Package.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_opf::package_has_generateTableOfContents():
    assert hasattr(opf::Package, "generateTableOfContents")
    descriptor = None
    for klass in opf::Package.__mro__:
        if "generateTableOfContents" in klass.__dict__:
            descriptor = klass.__dict__["generateTableOfContents"]
            break
    assert isinstance(descriptor, property)

def test_opf::package_has_uniqueIdentifier():
    assert hasattr(opf::Package, "uniqueIdentifier")
    descriptor = None
    for klass in opf::Package.__mro__:
        if "uniqueIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["uniqueIdentifier"]
            break
    assert isinstance(descriptor, property)



def test_opf::metadata_is_not_abstract():
    assert not inspect.isabstract(opf::Metadata)


def test_opf::metadata_constructor_exists():
    assert callable(opf::Metadata.__init__)


def test_opf::metadata_constructor_args():
    sig = inspect.signature(opf::Metadata.__init__)
    params = list(sig.parameters.keys())

def test_role_exists():
    # Check that the Enumeration exists
    assert Role is not None

def test_role_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Role]
    expected_literals = [
        "Contributor",
        "Forger",
        "Binder",
        "Etcher",
        "Corrector",
        "Author_in_quotations_or_text_abstracts",
        "Contractor",
        "Field_director",
        "Contestee_appellant",
        "Attributed_name",
        "Respondent_appellant",
        "Analyst",
        "Assignee",
        "Designer",
        "Graphic_technician",
        "Director",
        "Engineer",
        "Vocalist",
        "Expert",
        "Research_team_head",
        "Conservator",
        "Rubricator",
        "Auctioneer",
        "Writer_of_accompanying_material",
        "Type_designer",
        "Renderer",
        "Supporting_host",
        "Markup_editor",
        "Author_of_afterword_colophon_etc",
        "Teacher",
        "Author_of_dialog",
        "Collotyper",
        "Production_personnel",
        "Adapter",
        "Commentator",
        "Editor",
        "Plaintiff",
        "Depicted",
        "Engraver",
        "Copyright_holder",
        "Plaintiff_appellee",
        "Second_party",
        "Event_place",
        "Electrician",
        "Licensee",
        "Distribution_place",
        "Dedicator",
        "Composer",
        "Consultant",
        "Depositor",
        "Lithographer",
        "Licensor",
        "Dancer",
        "Book_producer",
        "Lyricist",
        "Dissertant",
        "Publisher",
        "Standards_body",
        "Transcriber",
        "Compositor",
        "Delineator",
        "Publishing_director",
        "Degree_grantor",
        "Manufacture_place",
        "Consultant_to_a_project",
        "Music_copyist",
        "Translator",
        "Complainant_appellee",
        "Bookseller",
        "Contestant",
        "Libelant_appellee",
        "Creator",
        "Printmaker",
        "Libelant",
        "Contestant_appellant",
        "Marbler",
        "Musical_director",
        "Project_director",
        "Author_of_introduction",
        "Defendant_appellant",
        "Libelant_appellant",
        "Researcher",
        "Musician",
        "Facsimilist",
        "Metal_engraver",
        "Draftsman",
        "Landscape_architect",
        "Research_team_member",
        "Contestee_appellee",
        "Photographer",
        "Thesis_advisor",
        "Patent_applicant",
        "Narrator",
        "Opponent",
        "Printer",
        "Electrotyper",
        "Actor",
        "Donor",
        "Production_place",
        "Book_designer",
        "Dedicatee",
        "Colorist",
        "Collector",
        "Witness",
        "Dubious_author",
        "Woodcutter",
        "Redactor",
        "First_party",
        "Data_manager",
        "Producer",
        "Recipient",
        "Calligrapher",
        "Data_contributor",
        "Author_of_screenplay",
        "Lead",
        "Lighting_designer",
        "Proofreader",
        "Libelee_appellant",
        "Typographer",
        "Performer",
        "Censor",
        "Contestee",
        "Process_contact",
        "Puppeteer",
        "Artist",
        "University_place",
        "Libelee_appellee",
        "Originator",
        "Funder",
        "Patron",
        "Inscriber",
        "Platemaker",
        "Artistic_director",
        "Libelee",
        "Owner",
        "Other",
        "Client",
        "Conceptor",
        "Bookjacket_designer",
        "Applicant",
        "Librettist",
        "Defendant_appellee",
        "Organizer_of_meeting",
        "Commentator_for_written_text",
        "Curator",
        "Bookplate_designer",
        "Stage_manager",
        "Blurb_writer",
        "Annotator",
        "Recording_engineer",
        "Defendant",
        "Costume_designer",
        "Programmer",
        "Arranger",
        "Honoree",
        "Publication_place",
        "Art_copyist",
        "Host",
        "Illustrator",
        "Plaintiff_appellant",
        "Illuminator",
        "Permitting_agency",
        "Correspondent",
        "Patent_holder",
        "Interviewer",
        "Animator",
        "Laboratory_director",
        "Papermaker",
        "Complainant_appellant",
        "Printer_of_plates",
        "Instrumentalist",
        "Bibliographic_antecedent",
        "Monitor",
        "Inventor",
        "Cinematographer",
        "Production_manager",
        "Interviewee",
        "Singer",
        "Laboratory",
        "Distributor",
        "Reviewer",
        "Film_editor",
        "Wood_engraver",
        "Metadata_contact",
        "Author",
        "Signer",
        "Collaborator",
        "Conductor",
        "Secretary",
        "Former_owner",
        "Sound_designer",
        "Manufacturer",
        "Moderator",
        "Technical_director",
        "Scribe",
        "Storyteller",
        "Copyright_claimant",
        "Lender",
        "Compiler",
        "Repository",
        "Choreographer",
        "Cover_designer",
        "Surveyor",
        "Respondent_appellee",
        "Scenarist",
        "Responsible_party",
        "Sculptor",
        "Reporter",
        "Architect",
        "Set_designer",
        "Scientific_advisor",
        "Geographic_information_specialist",
        "Associated_name",
        "Sponsor",
        "Speaker",
        "Respondent",
        "Cartographer",
        "Complainant",
        "Videographer",
        "Stereotyper",
        "Contestant_appellee",
        "Binding_designer",
        "Restager",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Role"

def test_type_exists():
    # Check that the Enumeration exists
    assert Type is not None

def test_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Type]
    expected_literals = [
        "Glossary",
        "Notes",
        "Copyright",
        "Cover",
        "TOC",
        "Acknowledgements",
        "Tables",
        "Index",
        "Colophon",
        "Dedication",
        "Title",
        "Preface",
        "Illustrations",
        "Text",
        "Epigraph",
        "Bibliography",
        "Foreword",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Type"


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
opf::Reference_strategy = st.builds(
    opf::Reference,
    href=
        safe_text,
    type=
        safe_text,
    title=
        safe_text
)
opf::Itemref_strategy = st.builds(
    opf::Itemref,
    linear=
        safe_text,
    idref=
        safe_text
)
opf::Item_strategy = st.builds(
    opf::Item,
    media_type=
        safe_text,
    sourcePath=
        safe_text,
    file=
        safe_text,
    generated=
        st.booleans(),
    required_namespace=
        safe_text,
    id=
        safe_text,
    title=
        safe_text,
    fallback_style=
        safe_text,
    required_modules=
        safe_text,
    fallback=
        safe_text,
    href=
        safe_text,
    noToc=
        st.booleans()
)
opf::Rights_strategy = st.builds(
    opf::Rights,
)
opf::Meta_strategy = st.builds(
    opf::Meta,
    name=
        safe_text,
    content=
        safe_text
)
opf::Language_strategy = st.builds(
    opf::Language,
)
opf::Source_strategy = st.builds(
    opf::Source,
)
opf::Identifier_strategy = st.builds(
    opf::Identifier,
)
opf::Coverage_strategy = st.builds(
    opf::Coverage,
)
opf::Relation_strategy = st.builds(
    opf::Relation,
)
opf::Type_strategy = st.builds(
    opf::Type,
)
opf::Date_strategy = st.builds(
    opf::Date,
)
opf::Contributor_strategy = st.builds(
    opf::Contributor,
)
opf::Format_strategy = st.builds(
    opf::Format,
)
opf::Description_strategy = st.builds(
    opf::Description,
)
opf::Publisher_strategy = st.builds(
    opf::Publisher,
)
opf::Title_strategy = st.builds(
    opf::Title,
)
opf::Subject_strategy = st.builds(
    opf::Subject,
)
opf::Creator_strategy = st.builds(
    opf::Creator,
)
opf::Guide_strategy = st.builds(
    opf::Guide,
)
opf::Spine_strategy = st.builds(
    opf::Spine,
    toc=
        safe_text
)
opf::Manifest_strategy = st.builds(
    opf::Manifest,
)
opf::Tours_strategy = st.builds(
    opf::Tours,
)
opf::Package_strategy = st.builds(
    opf::Package,
    includeReferencedResources=
        st.booleans(),
    generateCoverHTML=
        st.booleans(),
    version=
        safe_text,
    generateTableOfContents=
        st.booleans(),
    uniqueIdentifier=
        safe_text
)
opf::Metadata_strategy = st.builds(
    opf::Metadata,
)

@given(instance=opf::Reference_strategy)
@settings(max_examples=50)
def test_opf::reference_instantiation(instance):
    assert isinstance(instance, opf::Reference)

@given(instance=opf::Reference_strategy)
def test_opf::reference_href_type(instance):
    assert isinstance(instance.href, str)


@given(instance=opf::Reference_strategy)
def test_opf::reference_href_setter(instance):
    original = instance.href
    instance.href = original
    assert instance.href == original

@given(instance=opf::Reference_strategy)
def test_opf::reference_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=opf::Reference_strategy)
def test_opf::reference_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=opf::Reference_strategy)
def test_opf::reference_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=opf::Reference_strategy)
def test_opf::reference_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=opf::Itemref_strategy)
@settings(max_examples=50)
def test_opf::itemref_instantiation(instance):
    assert isinstance(instance, opf::Itemref)

@given(instance=opf::Itemref_strategy)
def test_opf::itemref_linear_type(instance):
    assert isinstance(instance.linear, str)


@given(instance=opf::Itemref_strategy)
def test_opf::itemref_linear_setter(instance):
    original = instance.linear
    instance.linear = original
    assert instance.linear == original

@given(instance=opf::Itemref_strategy)
def test_opf::itemref_idref_type(instance):
    assert isinstance(instance.idref, str)


@given(instance=opf::Itemref_strategy)
def test_opf::itemref_idref_setter(instance):
    original = instance.idref
    instance.idref = original
    assert instance.idref == original

@given(instance=opf::Item_strategy)
@settings(max_examples=50)
def test_opf::item_instantiation(instance):
    assert isinstance(instance, opf::Item)

@given(instance=opf::Item_strategy)
def test_opf::item_media_type_type(instance):
    assert isinstance(instance.media_type, str)


@given(instance=opf::Item_strategy)
def test_opf::item_media_type_setter(instance):
    original = instance.media_type
    instance.media_type = original
    assert instance.media_type == original

@given(instance=opf::Item_strategy)
def test_opf::item_sourcePath_type(instance):
    assert isinstance(instance.sourcePath, str)


@given(instance=opf::Item_strategy)
def test_opf::item_sourcePath_setter(instance):
    original = instance.sourcePath
    instance.sourcePath = original
    assert instance.sourcePath == original

@given(instance=opf::Item_strategy)
def test_opf::item_file_type(instance):
    assert isinstance(instance.file, str)


@given(instance=opf::Item_strategy)
def test_opf::item_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=opf::Item_strategy)
def test_opf::item_generated_type(instance):
    assert isinstance(instance.generated, bool)


@given(instance=opf::Item_strategy)
def test_opf::item_generated_setter(instance):
    original = instance.generated
    instance.generated = original
    assert instance.generated == original

@given(instance=opf::Item_strategy)
def test_opf::item_required_namespace_type(instance):
    assert isinstance(instance.required_namespace, str)


@given(instance=opf::Item_strategy)
def test_opf::item_required_namespace_setter(instance):
    original = instance.required_namespace
    instance.required_namespace = original
    assert instance.required_namespace == original

@given(instance=opf::Item_strategy)
def test_opf::item_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=opf::Item_strategy)
def test_opf::item_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=opf::Item_strategy)
def test_opf::item_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=opf::Item_strategy)
def test_opf::item_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=opf::Item_strategy)
def test_opf::item_fallback_style_type(instance):
    assert isinstance(instance.fallback_style, str)


@given(instance=opf::Item_strategy)
def test_opf::item_fallback_style_setter(instance):
    original = instance.fallback_style
    instance.fallback_style = original
    assert instance.fallback_style == original

@given(instance=opf::Item_strategy)
def test_opf::item_required_modules_type(instance):
    assert isinstance(instance.required_modules, str)


@given(instance=opf::Item_strategy)
def test_opf::item_required_modules_setter(instance):
    original = instance.required_modules
    instance.required_modules = original
    assert instance.required_modules == original

@given(instance=opf::Item_strategy)
def test_opf::item_fallback_type(instance):
    assert isinstance(instance.fallback, str)


@given(instance=opf::Item_strategy)
def test_opf::item_fallback_setter(instance):
    original = instance.fallback
    instance.fallback = original
    assert instance.fallback == original

@given(instance=opf::Item_strategy)
def test_opf::item_href_type(instance):
    assert isinstance(instance.href, str)


@given(instance=opf::Item_strategy)
def test_opf::item_href_setter(instance):
    original = instance.href
    instance.href = original
    assert instance.href == original

@given(instance=opf::Item_strategy)
def test_opf::item_noToc_type(instance):
    assert isinstance(instance.noToc, bool)


@given(instance=opf::Item_strategy)
def test_opf::item_noToc_setter(instance):
    original = instance.noToc
    instance.noToc = original
    assert instance.noToc == original

@given(instance=opf::Rights_strategy)
@settings(max_examples=50)
def test_opf::rights_instantiation(instance):
    assert isinstance(instance, opf::Rights)

@given(instance=opf::Meta_strategy)
@settings(max_examples=50)
def test_opf::meta_instantiation(instance):
    assert isinstance(instance, opf::Meta)

@given(instance=opf::Meta_strategy)
def test_opf::meta_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=opf::Meta_strategy)
def test_opf::meta_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=opf::Meta_strategy)
def test_opf::meta_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=opf::Meta_strategy)
def test_opf::meta_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=opf::Language_strategy)
@settings(max_examples=50)
def test_opf::language_instantiation(instance):
    assert isinstance(instance, opf::Language)

@given(instance=opf::Source_strategy)
@settings(max_examples=50)
def test_opf::source_instantiation(instance):
    assert isinstance(instance, opf::Source)

@given(instance=opf::Identifier_strategy)
@settings(max_examples=50)
def test_opf::identifier_instantiation(instance):
    assert isinstance(instance, opf::Identifier)

@given(instance=opf::Coverage_strategy)
@settings(max_examples=50)
def test_opf::coverage_instantiation(instance):
    assert isinstance(instance, opf::Coverage)

@given(instance=opf::Relation_strategy)
@settings(max_examples=50)
def test_opf::relation_instantiation(instance):
    assert isinstance(instance, opf::Relation)

@given(instance=opf::Type_strategy)
@settings(max_examples=50)
def test_opf::type_instantiation(instance):
    assert isinstance(instance, opf::Type)

@given(instance=opf::Date_strategy)
@settings(max_examples=50)
def test_opf::date_instantiation(instance):
    assert isinstance(instance, opf::Date)

@given(instance=opf::Contributor_strategy)
@settings(max_examples=50)
def test_opf::contributor_instantiation(instance):
    assert isinstance(instance, opf::Contributor)

@given(instance=opf::Format_strategy)
@settings(max_examples=50)
def test_opf::format_instantiation(instance):
    assert isinstance(instance, opf::Format)

@given(instance=opf::Description_strategy)
@settings(max_examples=50)
def test_opf::description_instantiation(instance):
    assert isinstance(instance, opf::Description)

@given(instance=opf::Publisher_strategy)
@settings(max_examples=50)
def test_opf::publisher_instantiation(instance):
    assert isinstance(instance, opf::Publisher)

@given(instance=opf::Title_strategy)
@settings(max_examples=50)
def test_opf::title_instantiation(instance):
    assert isinstance(instance, opf::Title)

@given(instance=opf::Subject_strategy)
@settings(max_examples=50)
def test_opf::subject_instantiation(instance):
    assert isinstance(instance, opf::Subject)

@given(instance=opf::Creator_strategy)
@settings(max_examples=50)
def test_opf::creator_instantiation(instance):
    assert isinstance(instance, opf::Creator)

@given(instance=opf::Guide_strategy)
@settings(max_examples=50)
def test_opf::guide_instantiation(instance):
    assert isinstance(instance, opf::Guide)

@given(instance=opf::Spine_strategy)
@settings(max_examples=50)
def test_opf::spine_instantiation(instance):
    assert isinstance(instance, opf::Spine)

@given(instance=opf::Spine_strategy)
def test_opf::spine_toc_type(instance):
    assert isinstance(instance.toc, str)


@given(instance=opf::Spine_strategy)
def test_opf::spine_toc_setter(instance):
    original = instance.toc
    instance.toc = original
    assert instance.toc == original

@given(instance=opf::Manifest_strategy)
@settings(max_examples=50)
def test_opf::manifest_instantiation(instance):
    assert isinstance(instance, opf::Manifest)

@given(instance=opf::Tours_strategy)
@settings(max_examples=50)
def test_opf::tours_instantiation(instance):
    assert isinstance(instance, opf::Tours)

@given(instance=opf::Package_strategy)
@settings(max_examples=50)
def test_opf::package_instantiation(instance):
    assert isinstance(instance, opf::Package)

@given(instance=opf::Package_strategy)
def test_opf::package_includeReferencedResources_type(instance):
    assert isinstance(instance.includeReferencedResources, bool)


@given(instance=opf::Package_strategy)
def test_opf::package_includeReferencedResources_setter(instance):
    original = instance.includeReferencedResources
    instance.includeReferencedResources = original
    assert instance.includeReferencedResources == original

@given(instance=opf::Package_strategy)
def test_opf::package_generateCoverHTML_type(instance):
    assert isinstance(instance.generateCoverHTML, bool)


@given(instance=opf::Package_strategy)
def test_opf::package_generateCoverHTML_setter(instance):
    original = instance.generateCoverHTML
    instance.generateCoverHTML = original
    assert instance.generateCoverHTML == original

@given(instance=opf::Package_strategy)
def test_opf::package_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=opf::Package_strategy)
def test_opf::package_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=opf::Package_strategy)
def test_opf::package_generateTableOfContents_type(instance):
    assert isinstance(instance.generateTableOfContents, bool)


@given(instance=opf::Package_strategy)
def test_opf::package_generateTableOfContents_setter(instance):
    original = instance.generateTableOfContents
    instance.generateTableOfContents = original
    assert instance.generateTableOfContents == original

@given(instance=opf::Package_strategy)
def test_opf::package_uniqueIdentifier_type(instance):
    assert isinstance(instance.uniqueIdentifier, str)


@given(instance=opf::Package_strategy)
def test_opf::package_uniqueIdentifier_setter(instance):
    original = instance.uniqueIdentifier
    instance.uniqueIdentifier = original
    assert instance.uniqueIdentifier == original

@given(instance=opf::Metadata_strategy)
@settings(max_examples=50)
def test_opf::metadata_instantiation(instance):
    assert isinstance(instance, opf::Metadata)
