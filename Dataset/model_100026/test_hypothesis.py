import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    opf::Reference,
    opf::Item,
    opf::Meta,
    opf::Itemref,
    opf::Identifier,
    opf::Format,
    opf::Rights,
    opf::Coverage,
    opf::Relation,
    opf::Language,
    opf::Source,
    opf::Subject,
    opf::Creator,
    opf::Type,
    opf::Date,
    opf::Contributor,
    opf::Publisher,
    opf::Description,
    opf::Manifest,
    opf::Metadata,
    opf::Title,
    opf::Tours,
    opf::Guide,
    opf::Spine,
    opf::Package,
    Type,
    Role,
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
    assert "title" in params, "Missing parameter 'title'"
    assert "href" in params, "Missing parameter 'href'"
    assert "type" in params, "Missing parameter 'type'"

def test_opf::reference_has_title():
    assert hasattr(opf::Reference, "title")
    descriptor = None
    for klass in opf::Reference.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

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



def test_opf::item_is_not_abstract():
    assert not inspect.isabstract(opf::Item)


def test_opf::item_constructor_exists():
    assert callable(opf::Item.__init__)


def test_opf::item_constructor_args():
    sig = inspect.signature(opf::Item.__init__)
    params = list(sig.parameters.keys())
    assert "fallback_style" in params, "Missing parameter 'fallback_style'"
    assert "sourcePath" in params, "Missing parameter 'sourcePath'"
    assert "title" in params, "Missing parameter 'title'"
    assert "required_modules" in params, "Missing parameter 'required_modules'"
    assert "media_type" in params, "Missing parameter 'media_type'"
    assert "file" in params, "Missing parameter 'file'"
    assert "required_namespace" in params, "Missing parameter 'required_namespace'"
    assert "id" in params, "Missing parameter 'id'"
    assert "fallback" in params, "Missing parameter 'fallback'"
    assert "href" in params, "Missing parameter 'href'"
    assert "noToc" in params, "Missing parameter 'noToc'"
    assert "generated" in params, "Missing parameter 'generated'"

def test_opf::item_has_fallback_style():
    assert hasattr(opf::Item, "fallback_style")
    descriptor = None
    for klass in opf::Item.__mro__:
        if "fallback_style" in klass.__dict__:
            descriptor = klass.__dict__["fallback_style"]
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

def test_opf::item_has_title():
    assert hasattr(opf::Item, "title")
    descriptor = None
    for klass in opf::Item.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
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

def test_opf::item_has_media_type():
    assert hasattr(opf::Item, "media_type")
    descriptor = None
    for klass in opf::Item.__mro__:
        if "media_type" in klass.__dict__:
            descriptor = klass.__dict__["media_type"]
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

def test_opf::item_has_generated():
    assert hasattr(opf::Item, "generated")
    descriptor = None
    for klass in opf::Item.__mro__:
        if "generated" in klass.__dict__:
            descriptor = klass.__dict__["generated"]
            break
    assert isinstance(descriptor, property)



def test_opf::meta_is_not_abstract():
    assert not inspect.isabstract(opf::Meta)


def test_opf::meta_constructor_exists():
    assert callable(opf::Meta.__init__)


def test_opf::meta_constructor_args():
    sig = inspect.signature(opf::Meta.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"
    assert "name" in params, "Missing parameter 'name'"

def test_opf::meta_has_content():
    assert hasattr(opf::Meta, "content")
    descriptor = None
    for klass in opf::Meta.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_opf::meta_has_name():
    assert hasattr(opf::Meta, "name")
    descriptor = None
    for klass in opf::Meta.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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



def test_opf::identifier_is_not_abstract():
    assert not inspect.isabstract(opf::Identifier)


def test_opf::identifier_constructor_exists():
    assert callable(opf::Identifier.__init__)


def test_opf::identifier_constructor_args():
    sig = inspect.signature(opf::Identifier.__init__)
    params = list(sig.parameters.keys())



def test_opf::format_is_not_abstract():
    assert not inspect.isabstract(opf::Format)


def test_opf::format_constructor_exists():
    assert callable(opf::Format.__init__)


def test_opf::format_constructor_args():
    sig = inspect.signature(opf::Format.__init__)
    params = list(sig.parameters.keys())



def test_opf::rights_is_not_abstract():
    assert not inspect.isabstract(opf::Rights)


def test_opf::rights_constructor_exists():
    assert callable(opf::Rights.__init__)


def test_opf::rights_constructor_args():
    sig = inspect.signature(opf::Rights.__init__)
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



def test_opf::publisher_is_not_abstract():
    assert not inspect.isabstract(opf::Publisher)


def test_opf::publisher_constructor_exists():
    assert callable(opf::Publisher.__init__)


def test_opf::publisher_constructor_args():
    sig = inspect.signature(opf::Publisher.__init__)
    params = list(sig.parameters.keys())



def test_opf::description_is_not_abstract():
    assert not inspect.isabstract(opf::Description)


def test_opf::description_constructor_exists():
    assert callable(opf::Description.__init__)


def test_opf::description_constructor_args():
    sig = inspect.signature(opf::Description.__init__)
    params = list(sig.parameters.keys())



def test_opf::manifest_is_not_abstract():
    assert not inspect.isabstract(opf::Manifest)


def test_opf::manifest_constructor_exists():
    assert callable(opf::Manifest.__init__)


def test_opf::manifest_constructor_args():
    sig = inspect.signature(opf::Manifest.__init__)
    params = list(sig.parameters.keys())



def test_opf::metadata_is_not_abstract():
    assert not inspect.isabstract(opf::Metadata)


def test_opf::metadata_constructor_exists():
    assert callable(opf::Metadata.__init__)


def test_opf::metadata_constructor_args():
    sig = inspect.signature(opf::Metadata.__init__)
    params = list(sig.parameters.keys())



def test_opf::title_is_not_abstract():
    assert not inspect.isabstract(opf::Title)


def test_opf::title_constructor_exists():
    assert callable(opf::Title.__init__)


def test_opf::title_constructor_args():
    sig = inspect.signature(opf::Title.__init__)
    params = list(sig.parameters.keys())



def test_opf::tours_is_not_abstract():
    assert not inspect.isabstract(opf::Tours)


def test_opf::tours_constructor_exists():
    assert callable(opf::Tours.__init__)


def test_opf::tours_constructor_args():
    sig = inspect.signature(opf::Tours.__init__)
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



def test_opf::package_is_not_abstract():
    assert not inspect.isabstract(opf::Package)


def test_opf::package_constructor_exists():
    assert callable(opf::Package.__init__)


def test_opf::package_constructor_args():
    sig = inspect.signature(opf::Package.__init__)
    params = list(sig.parameters.keys())
    assert "uniqueIdentifier" in params, "Missing parameter 'uniqueIdentifier'"
    assert "includeReferencedResources" in params, "Missing parameter 'includeReferencedResources'"
    assert "generateTableOfContents" in params, "Missing parameter 'generateTableOfContents'"
    assert "version" in params, "Missing parameter 'version'"
    assert "generateCoverHTML" in params, "Missing parameter 'generateCoverHTML'"

def test_opf::package_has_uniqueIdentifier():
    assert hasattr(opf::Package, "uniqueIdentifier")
    descriptor = None
    for klass in opf::Package.__mro__:
        if "uniqueIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["uniqueIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_opf::package_has_includeReferencedResources():
    assert hasattr(opf::Package, "includeReferencedResources")
    descriptor = None
    for klass in opf::Package.__mro__:
        if "includeReferencedResources" in klass.__dict__:
            descriptor = klass.__dict__["includeReferencedResources"]
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

def test_opf::package_has_version():
    assert hasattr(opf::Package, "version")
    descriptor = None
    for klass in opf::Package.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
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

def test_type_exists():
    # Check that the Enumeration exists
    assert Type is not None

def test_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Type]
    expected_literals = [
        "Index",
        "Acknowledgements",
        "Preface",
        "Text",
        "Title",
        "Bibliography",
        "Notes",
        "Foreword",
        "Cover",
        "Tables",
        "Epigraph",
        "Copyright",
        "Colophon",
        "Illustrations",
        "Glossary",
        "Dedication",
        "TOC",
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
        "Publisher",
        "Bibliographic_antecedent",
        "Consultant_to_a_project",
        "Responsible_party",
        "Respondent_appellant",
        "Moderator",
        "Writer_of_accompanying_material",
        "Reviewer",
        "Publication_place",
        "Scribe",
        "Sound_designer",
        "Supporting_host",
        "Witness",
        "Vocalist",
        "Contestant_appellant",
        "Creator",
        "Director",
        "Production_place",
        "Second_party",
        "Librettist",
        "Owner",
        "Other",
        "Puppeteer",
        "Singer",
        "Collaborator",
        "Libelant",
        "Author_of_dialog",
        "Plaintiff_appellee",
        "University_place",
        "Lithographer",
        "Author_in_quotations_or_text_abstracts",
        "Contestee_appellee",
        "Researcher",
        "Author_of_introduction",
        "Photographer",
        "Standards_body",
        "Libelant_appellee",
        "Former_owner",
        "Depositor",
        "Scenarist",
        "Respondent_appellee",
        "Donor",
        "Translator",
        "Curator",
        "Recording_engineer",
        "Teacher",
        "Dancer",
        "Organizer_of_meeting",
        "Defendant_appellant",
        "Art_copyist",
        "Contestee",
        "Compositor",
        "Plaintiff",
        "Dedicator",
        "Inventor",
        "Laboratory_director",
        "Platemaker",
        "Commentator",
        "Opponent",
        "Research_team_head",
        "Binding_designer",
        "Facsimilist",
        "Videographer",
        "Dedicatee",
        "Respondent",
        "Graphic_technician",
        "Proofreader",
        "Markup_editor",
        "Surveyor",
        "Patron",
        "Contestant_appellee",
        "Secretary",
        "Arranger",
        "Collector",
        "Blurb_writer",
        "Defendant_appellee",
        "Libelee_appellant",
        "Cover_designer",
        "Project_director",
        "Marbler",
        "Thesis_advisor",
        "Composer",
        "Illustrator",
        "Plaintiff_appellant",
        "Designer",
        "Complainant_appellee",
        "Renderer",
        "Electrotyper",
        "Collotyper",
        "Restager",
        "Redactor",
        "Technical_director",
        "Printer_of_plates",
        "Compiler",
        "Host",
        "Bookplate_designer",
        "Contractor",
        "Research_team_member",
        "Sculptor",
        "Licensor",
        "Publishing_director",
        "Speaker",
        "Patent_applicant",
        "Artistic_director",
        "Transcriber",
        "Conductor",
        "Auctioneer",
        "Repository",
        "Book_designer",
        "Engineer",
        "Colorist",
        "Narrator",
        "Dubious_author",
        "Contributor",
        "Forger",
        "Distributor",
        "Set_designer",
        "Libelee_appellee",
        "Patent_holder",
        "Musical_director",
        "Data_contributor",
        "Libelee",
        "Originator",
        "Engraver",
        "Typographer",
        "Geographic_information_specialist",
        "Papermaker",
        "Attributed_name",
        "Dissertant",
        "Reporter",
        "Annotator",
        "Calligrapher",
        "Licensee",
        "Manufacturer",
        "Process_contact",
        "Copyright_holder",
        "Editor",
        "Consultant",
        "Expert",
        "Animator",
        "Associated_name",
        "Landscape_architect",
        "Instrumentalist",
        "Funder",
        "Adapter",
        "Production_manager",
        "Event_place",
        "Costume_designer",
        "Corrector",
        "Author_of_screenplay",
        "Author_of_afterword_colophon_etc",
        "Depicted",
        "Assignee",
        "Analyst",
        "Type_designer",
        "Defendant",
        "Laboratory",
        "Scientific_advisor",
        "Rubricator",
        "Client",
        "Musician",
        "Applicant",
        "Architect",
        "Field_director",
        "Inscriber",
        "Storyteller",
        "Censor",
        "Interviewer",
        "Film_editor",
        "Book_producer",
        "Contestant",
        "Sponsor",
        "Contestee_appellant",
        "Binder",
        "Manufacture_place",
        "Complainant",
        "Commentator_for_written_text",
        "Metal_engraver",
        "Actor",
        "Music_copyist",
        "Bookseller",
        "Printmaker",
        "First_party",
        "Producer",
        "Lighting_designer",
        "Conservator",
        "Performer",
        "Stereotyper",
        "Cinematographer",
        "Delineator",
        "Correspondent",
        "Production_personnel",
        "Recipient",
        "Wood_engraver",
        "Degree_grantor",
        "Stage_manager",
        "Copyright_claimant",
        "Printer",
        "Conceptor",
        "Lender",
        "Monitor",
        "Author",
        "Lead",
        "Metadata_contact",
        "Signer",
        "Interviewee",
        "Illuminator",
        "Electrician",
        "Woodcutter",
        "Bookjacket_designer",
        "Libelant_appellant",
        "Etcher",
        "Distribution_place",
        "Choreographer",
        "Data_manager",
        "Permitting_agency",
        "Programmer",
        "Honoree",
        "Complainant_appellant",
        "Artist",
        "Draftsman",
        "Lyricist",
        "Cartographer",
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
opf::Reference_strategy = st.builds(
    opf::Reference,
    title=
        safe_text,
    href=
        safe_text,
    type=
        safe_text
)
opf::Item_strategy = st.builds(
    opf::Item,
    fallback_style=
        safe_text,
    sourcePath=
        safe_text,
    title=
        safe_text,
    required_modules=
        safe_text,
    media_type=
        safe_text,
    file=
        safe_text,
    required_namespace=
        safe_text,
    id=
        safe_text,
    fallback=
        safe_text,
    href=
        safe_text,
    noToc=
        st.booleans(),
    generated=
        st.booleans()
)
opf::Meta_strategy = st.builds(
    opf::Meta,
    content=
        safe_text,
    name=
        safe_text
)
opf::Itemref_strategy = st.builds(
    opf::Itemref,
    linear=
        safe_text,
    idref=
        safe_text
)
opf::Identifier_strategy = st.builds(
    opf::Identifier,
)
opf::Format_strategy = st.builds(
    opf::Format,
)
opf::Rights_strategy = st.builds(
    opf::Rights,
)
opf::Coverage_strategy = st.builds(
    opf::Coverage,
)
opf::Relation_strategy = st.builds(
    opf::Relation,
)
opf::Language_strategy = st.builds(
    opf::Language,
)
opf::Source_strategy = st.builds(
    opf::Source,
)
opf::Subject_strategy = st.builds(
    opf::Subject,
)
opf::Creator_strategy = st.builds(
    opf::Creator,
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
opf::Publisher_strategy = st.builds(
    opf::Publisher,
)
opf::Description_strategy = st.builds(
    opf::Description,
)
opf::Manifest_strategy = st.builds(
    opf::Manifest,
)
opf::Metadata_strategy = st.builds(
    opf::Metadata,
)
opf::Title_strategy = st.builds(
    opf::Title,
)
opf::Tours_strategy = st.builds(
    opf::Tours,
)
opf::Guide_strategy = st.builds(
    opf::Guide,
)
opf::Spine_strategy = st.builds(
    opf::Spine,
    toc=
        safe_text
)
opf::Package_strategy = st.builds(
    opf::Package,
    uniqueIdentifier=
        safe_text,
    includeReferencedResources=
        st.booleans(),
    generateTableOfContents=
        st.booleans(),
    version=
        safe_text,
    generateCoverHTML=
        st.booleans()
)

@given(instance=opf::Reference_strategy)
@settings(max_examples=50)
def test_opf::reference_instantiation(instance):
    assert isinstance(instance, opf::Reference)

@given(instance=opf::Reference_strategy)
def test_opf::reference_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=opf::Reference_strategy)
def test_opf::reference_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

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

@given(instance=opf::Item_strategy)
@settings(max_examples=50)
def test_opf::item_instantiation(instance):
    assert isinstance(instance, opf::Item)

@given(instance=opf::Item_strategy)
def test_opf::item_fallback_style_type(instance):
    assert isinstance(instance.fallback_style, str)


@given(instance=opf::Item_strategy)
def test_opf::item_fallback_style_setter(instance):
    original = instance.fallback_style
    instance.fallback_style = original
    assert instance.fallback_style == original

@given(instance=opf::Item_strategy)
def test_opf::item_sourcePath_type(instance):
    assert isinstance(instance.sourcePath, str)


@given(instance=opf::Item_strategy)
def test_opf::item_sourcePath_setter(instance):
    original = instance.sourcePath
    instance.sourcePath = original
    assert instance.sourcePath == original

@given(instance=opf::Item_strategy)
def test_opf::item_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=opf::Item_strategy)
def test_opf::item_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=opf::Item_strategy)
def test_opf::item_required_modules_type(instance):
    assert isinstance(instance.required_modules, str)


@given(instance=opf::Item_strategy)
def test_opf::item_required_modules_setter(instance):
    original = instance.required_modules
    instance.required_modules = original
    assert instance.required_modules == original

@given(instance=opf::Item_strategy)
def test_opf::item_media_type_type(instance):
    assert isinstance(instance.media_type, str)


@given(instance=opf::Item_strategy)
def test_opf::item_media_type_setter(instance):
    original = instance.media_type
    instance.media_type = original
    assert instance.media_type == original

@given(instance=opf::Item_strategy)
def test_opf::item_file_type(instance):
    assert isinstance(instance.file, str)


@given(instance=opf::Item_strategy)
def test_opf::item_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

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

@given(instance=opf::Item_strategy)
def test_opf::item_generated_type(instance):
    assert isinstance(instance.generated, bool)


@given(instance=opf::Item_strategy)
def test_opf::item_generated_setter(instance):
    original = instance.generated
    instance.generated = original
    assert instance.generated == original

@given(instance=opf::Meta_strategy)
@settings(max_examples=50)
def test_opf::meta_instantiation(instance):
    assert isinstance(instance, opf::Meta)

@given(instance=opf::Meta_strategy)
def test_opf::meta_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=opf::Meta_strategy)
def test_opf::meta_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=opf::Meta_strategy)
def test_opf::meta_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=opf::Meta_strategy)
def test_opf::meta_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

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

@given(instance=opf::Identifier_strategy)
@settings(max_examples=50)
def test_opf::identifier_instantiation(instance):
    assert isinstance(instance, opf::Identifier)

@given(instance=opf::Format_strategy)
@settings(max_examples=50)
def test_opf::format_instantiation(instance):
    assert isinstance(instance, opf::Format)

@given(instance=opf::Rights_strategy)
@settings(max_examples=50)
def test_opf::rights_instantiation(instance):
    assert isinstance(instance, opf::Rights)

@given(instance=opf::Coverage_strategy)
@settings(max_examples=50)
def test_opf::coverage_instantiation(instance):
    assert isinstance(instance, opf::Coverage)

@given(instance=opf::Relation_strategy)
@settings(max_examples=50)
def test_opf::relation_instantiation(instance):
    assert isinstance(instance, opf::Relation)

@given(instance=opf::Language_strategy)
@settings(max_examples=50)
def test_opf::language_instantiation(instance):
    assert isinstance(instance, opf::Language)

@given(instance=opf::Source_strategy)
@settings(max_examples=50)
def test_opf::source_instantiation(instance):
    assert isinstance(instance, opf::Source)

@given(instance=opf::Subject_strategy)
@settings(max_examples=50)
def test_opf::subject_instantiation(instance):
    assert isinstance(instance, opf::Subject)

@given(instance=opf::Creator_strategy)
@settings(max_examples=50)
def test_opf::creator_instantiation(instance):
    assert isinstance(instance, opf::Creator)

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

@given(instance=opf::Publisher_strategy)
@settings(max_examples=50)
def test_opf::publisher_instantiation(instance):
    assert isinstance(instance, opf::Publisher)

@given(instance=opf::Description_strategy)
@settings(max_examples=50)
def test_opf::description_instantiation(instance):
    assert isinstance(instance, opf::Description)

@given(instance=opf::Manifest_strategy)
@settings(max_examples=50)
def test_opf::manifest_instantiation(instance):
    assert isinstance(instance, opf::Manifest)

@given(instance=opf::Metadata_strategy)
@settings(max_examples=50)
def test_opf::metadata_instantiation(instance):
    assert isinstance(instance, opf::Metadata)

@given(instance=opf::Title_strategy)
@settings(max_examples=50)
def test_opf::title_instantiation(instance):
    assert isinstance(instance, opf::Title)

@given(instance=opf::Tours_strategy)
@settings(max_examples=50)
def test_opf::tours_instantiation(instance):
    assert isinstance(instance, opf::Tours)

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

@given(instance=opf::Package_strategy)
@settings(max_examples=50)
def test_opf::package_instantiation(instance):
    assert isinstance(instance, opf::Package)

@given(instance=opf::Package_strategy)
def test_opf::package_uniqueIdentifier_type(instance):
    assert isinstance(instance.uniqueIdentifier, str)


@given(instance=opf::Package_strategy)
def test_opf::package_uniqueIdentifier_setter(instance):
    original = instance.uniqueIdentifier
    instance.uniqueIdentifier = original
    assert instance.uniqueIdentifier == original

@given(instance=opf::Package_strategy)
def test_opf::package_includeReferencedResources_type(instance):
    assert isinstance(instance.includeReferencedResources, bool)


@given(instance=opf::Package_strategy)
def test_opf::package_includeReferencedResources_setter(instance):
    original = instance.includeReferencedResources
    instance.includeReferencedResources = original
    assert instance.includeReferencedResources == original

@given(instance=opf::Package_strategy)
def test_opf::package_generateTableOfContents_type(instance):
    assert isinstance(instance.generateTableOfContents, bool)


@given(instance=opf::Package_strategy)
def test_opf::package_generateTableOfContents_setter(instance):
    original = instance.generateTableOfContents
    instance.generateTableOfContents = original
    assert instance.generateTableOfContents == original

@given(instance=opf::Package_strategy)
def test_opf::package_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=opf::Package_strategy)
def test_opf::package_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=opf::Package_strategy)
def test_opf::package_generateCoverHTML_type(instance):
    assert isinstance(instance.generateCoverHTML, bool)


@given(instance=opf::Package_strategy)
def test_opf::package_generateCoverHTML_setter(instance):
    original = instance.generateCoverHTML
    instance.generateCoverHTML = original
    assert instance.generateCoverHTML == original
