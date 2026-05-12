import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    application_Recipes,
    application_Mappers,
    application_MappingLayer,
    application_ApplicationMapper,
    application_ApplicationRealm,
    application_ApplicationRecipe,
    application_Form,
    application_ApplicationUIPackage,
    application_StyleLibrary,
    application_ApplicationStyle,
    application_Roles,
    application_ApplicationStyleLibraries,
    application_ApplicationInfrastructureLayers,
    application_ApplicationUILayer,
    application_MessageLibrary,
    application_Language,
    application_ApplicationLanguages,
    application_ApplicationMessageLibrary,
    application_EnterpriseInfrastructure,
    application_ApplicationInfrastructureLayer,
    application_ApplicationMessageLibraries,
    application_ApplicationRealms,
    application_ApplicationMappers,
    application_ApplicationRecipes,
    application_Application,
    application_ApplicationGroup,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_application_recipes_is_not_abstract():
    assert not inspect.isabstract(application_Recipes)


def test_application_recipes_constructor_exists():
    assert callable(application_Recipes.__init__)


def test_application_recipes_constructor_args():
    sig = inspect.signature(application_Recipes.__init__)
    params = list(sig.parameters.keys())



def test_application_mappers_is_not_abstract():
    assert not inspect.isabstract(application_Mappers)


def test_application_mappers_constructor_exists():
    assert callable(application_Mappers.__init__)


def test_application_mappers_constructor_args():
    sig = inspect.signature(application_Mappers.__init__)
    params = list(sig.parameters.keys())



def test_application_mappinglayer_is_not_abstract():
    assert not inspect.isabstract(application_MappingLayer)


def test_application_mappinglayer_constructor_exists():
    assert callable(application_MappingLayer.__init__)


def test_application_mappinglayer_constructor_args():
    sig = inspect.signature(application_MappingLayer.__init__)
    params = list(sig.parameters.keys())



def test_application_applicationmapper_is_not_abstract():
    assert not inspect.isabstract(application_ApplicationMapper)


def test_application_applicationmapper_constructor_exists():
    assert callable(application_ApplicationMapper.__init__)


def test_application_applicationmapper_constructor_args():
    sig = inspect.signature(application_ApplicationMapper.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_application_applicationmapper_has_uid():
    assert hasattr(application_ApplicationMapper, "uid")
    descriptor = None
    for klass in application_ApplicationMapper.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_application_applicationmapper_has_name():
    assert hasattr(application_ApplicationMapper, "name")
    descriptor = None
    for klass in application_ApplicationMapper.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_application_applicationrealm_is_not_abstract():
    assert not inspect.isabstract(application_ApplicationRealm)


def test_application_applicationrealm_constructor_exists():
    assert callable(application_ApplicationRealm.__init__)


def test_application_applicationrealm_constructor_args():
    sig = inspect.signature(application_ApplicationRealm.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_application_applicationrealm_has_uid():
    assert hasattr(application_ApplicationRealm, "uid")
    descriptor = None
    for klass in application_ApplicationRealm.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_application_applicationrealm_has_name():
    assert hasattr(application_ApplicationRealm, "name")
    descriptor = None
    for klass in application_ApplicationRealm.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_application_applicationrecipe_is_not_abstract():
    assert not inspect.isabstract(application_ApplicationRecipe)


def test_application_applicationrecipe_constructor_exists():
    assert callable(application_ApplicationRecipe.__init__)


def test_application_applicationrecipe_constructor_args():
    sig = inspect.signature(application_ApplicationRecipe.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_application_applicationrecipe_has_uid():
    assert hasattr(application_ApplicationRecipe, "uid")
    descriptor = None
    for klass in application_ApplicationRecipe.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_application_applicationrecipe_has_name():
    assert hasattr(application_ApplicationRecipe, "name")
    descriptor = None
    for klass in application_ApplicationRecipe.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_application_form_is_not_abstract():
    assert not inspect.isabstract(application_Form)


def test_application_form_constructor_exists():
    assert callable(application_Form.__init__)


def test_application_form_constructor_args():
    sig = inspect.signature(application_Form.__init__)
    params = list(sig.parameters.keys())



def test_application_applicationuipackage_is_not_abstract():
    assert not inspect.isabstract(application_ApplicationUIPackage)


def test_application_applicationuipackage_constructor_exists():
    assert callable(application_ApplicationUIPackage.__init__)


def test_application_applicationuipackage_constructor_args():
    sig = inspect.signature(application_ApplicationUIPackage.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_application_applicationuipackage_has_name():
    assert hasattr(application_ApplicationUIPackage, "name")
    descriptor = None
    for klass in application_ApplicationUIPackage.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_application_applicationuipackage_has_uid():
    assert hasattr(application_ApplicationUIPackage, "uid")
    descriptor = None
    for klass in application_ApplicationUIPackage.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_application_stylelibrary_is_not_abstract():
    assert not inspect.isabstract(application_StyleLibrary)


def test_application_stylelibrary_constructor_exists():
    assert callable(application_StyleLibrary.__init__)


def test_application_stylelibrary_constructor_args():
    sig = inspect.signature(application_StyleLibrary.__init__)
    params = list(sig.parameters.keys())



def test_application_applicationstyle_is_not_abstract():
    assert not inspect.isabstract(application_ApplicationStyle)


def test_application_applicationstyle_constructor_exists():
    assert callable(application_ApplicationStyle.__init__)


def test_application_applicationstyle_constructor_args():
    sig = inspect.signature(application_ApplicationStyle.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_application_applicationstyle_has_uid():
    assert hasattr(application_ApplicationStyle, "uid")
    descriptor = None
    for klass in application_ApplicationStyle.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_application_applicationstyle_has_name():
    assert hasattr(application_ApplicationStyle, "name")
    descriptor = None
    for klass in application_ApplicationStyle.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_application_roles_is_not_abstract():
    assert not inspect.isabstract(application_Roles)


def test_application_roles_constructor_exists():
    assert callable(application_Roles.__init__)


def test_application_roles_constructor_args():
    sig = inspect.signature(application_Roles.__init__)
    params = list(sig.parameters.keys())



def test_application_applicationstylelibraries_is_not_abstract():
    assert not inspect.isabstract(application_ApplicationStyleLibraries)


def test_application_applicationstylelibraries_constructor_exists():
    assert callable(application_ApplicationStyleLibraries.__init__)


def test_application_applicationstylelibraries_constructor_args():
    sig = inspect.signature(application_ApplicationStyleLibraries.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_application_applicationstylelibraries_has_name():
    assert hasattr(application_ApplicationStyleLibraries, "name")
    descriptor = None
    for klass in application_ApplicationStyleLibraries.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_application_applicationstylelibraries_has_uid():
    assert hasattr(application_ApplicationStyleLibraries, "uid")
    descriptor = None
    for klass in application_ApplicationStyleLibraries.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_application_applicationinfrastructurelayers_is_not_abstract():
    assert not inspect.isabstract(application_ApplicationInfrastructureLayers)


def test_application_applicationinfrastructurelayers_constructor_exists():
    assert callable(application_ApplicationInfrastructureLayers.__init__)


def test_application_applicationinfrastructurelayers_constructor_args():
    sig = inspect.signature(application_ApplicationInfrastructureLayers.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_application_applicationinfrastructurelayers_has_name():
    assert hasattr(application_ApplicationInfrastructureLayers, "name")
    descriptor = None
    for klass in application_ApplicationInfrastructureLayers.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_application_applicationinfrastructurelayers_has_uid():
    assert hasattr(application_ApplicationInfrastructureLayers, "uid")
    descriptor = None
    for klass in application_ApplicationInfrastructureLayers.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_application_applicationuilayer_is_not_abstract():
    assert not inspect.isabstract(application_ApplicationUILayer)


def test_application_applicationuilayer_constructor_exists():
    assert callable(application_ApplicationUILayer.__init__)


def test_application_applicationuilayer_constructor_args():
    sig = inspect.signature(application_ApplicationUILayer.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_application_applicationuilayer_has_uid():
    assert hasattr(application_ApplicationUILayer, "uid")
    descriptor = None
    for klass in application_ApplicationUILayer.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_application_applicationuilayer_has_name():
    assert hasattr(application_ApplicationUILayer, "name")
    descriptor = None
    for klass in application_ApplicationUILayer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_application_messagelibrary_is_not_abstract():
    assert not inspect.isabstract(application_MessageLibrary)


def test_application_messagelibrary_constructor_exists():
    assert callable(application_MessageLibrary.__init__)


def test_application_messagelibrary_constructor_args():
    sig = inspect.signature(application_MessageLibrary.__init__)
    params = list(sig.parameters.keys())



def test_application_language_is_not_abstract():
    assert not inspect.isabstract(application_Language)


def test_application_language_constructor_exists():
    assert callable(application_Language.__init__)


def test_application_language_constructor_args():
    sig = inspect.signature(application_Language.__init__)
    params = list(sig.parameters.keys())



def test_application_applicationlanguages_is_not_abstract():
    assert not inspect.isabstract(application_ApplicationLanguages)


def test_application_applicationlanguages_constructor_exists():
    assert callable(application_ApplicationLanguages.__init__)


def test_application_applicationlanguages_constructor_args():
    sig = inspect.signature(application_ApplicationLanguages.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_application_applicationlanguages_has_name():
    assert hasattr(application_ApplicationLanguages, "name")
    descriptor = None
    for klass in application_ApplicationLanguages.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_application_applicationlanguages_has_uid():
    assert hasattr(application_ApplicationLanguages, "uid")
    descriptor = None
    for klass in application_ApplicationLanguages.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_application_applicationmessagelibrary_is_not_abstract():
    assert not inspect.isabstract(application_ApplicationMessageLibrary)


def test_application_applicationmessagelibrary_constructor_exists():
    assert callable(application_ApplicationMessageLibrary.__init__)


def test_application_applicationmessagelibrary_constructor_args():
    sig = inspect.signature(application_ApplicationMessageLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_application_applicationmessagelibrary_has_uid():
    assert hasattr(application_ApplicationMessageLibrary, "uid")
    descriptor = None
    for klass in application_ApplicationMessageLibrary.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_application_applicationmessagelibrary_has_name():
    assert hasattr(application_ApplicationMessageLibrary, "name")
    descriptor = None
    for klass in application_ApplicationMessageLibrary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_application_enterpriseinfrastructure_is_not_abstract():
    assert not inspect.isabstract(application_EnterpriseInfrastructure)


def test_application_enterpriseinfrastructure_constructor_exists():
    assert callable(application_EnterpriseInfrastructure.__init__)


def test_application_enterpriseinfrastructure_constructor_args():
    sig = inspect.signature(application_EnterpriseInfrastructure.__init__)
    params = list(sig.parameters.keys())



def test_application_applicationinfrastructurelayer_is_not_abstract():
    assert not inspect.isabstract(application_ApplicationInfrastructureLayer)


def test_application_applicationinfrastructurelayer_constructor_exists():
    assert callable(application_ApplicationInfrastructureLayer.__init__)


def test_application_applicationinfrastructurelayer_constructor_args():
    sig = inspect.signature(application_ApplicationInfrastructureLayer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_application_applicationinfrastructurelayer_has_name():
    assert hasattr(application_ApplicationInfrastructureLayer, "name")
    descriptor = None
    for klass in application_ApplicationInfrastructureLayer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_application_applicationinfrastructurelayer_has_uid():
    assert hasattr(application_ApplicationInfrastructureLayer, "uid")
    descriptor = None
    for klass in application_ApplicationInfrastructureLayer.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_application_applicationmessagelibraries_is_not_abstract():
    assert not inspect.isabstract(application_ApplicationMessageLibraries)


def test_application_applicationmessagelibraries_constructor_exists():
    assert callable(application_ApplicationMessageLibraries.__init__)


def test_application_applicationmessagelibraries_constructor_args():
    sig = inspect.signature(application_ApplicationMessageLibraries.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_application_applicationmessagelibraries_has_name():
    assert hasattr(application_ApplicationMessageLibraries, "name")
    descriptor = None
    for klass in application_ApplicationMessageLibraries.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_application_applicationmessagelibraries_has_uid():
    assert hasattr(application_ApplicationMessageLibraries, "uid")
    descriptor = None
    for klass in application_ApplicationMessageLibraries.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_application_applicationrealms_is_not_abstract():
    assert not inspect.isabstract(application_ApplicationRealms)


def test_application_applicationrealms_constructor_exists():
    assert callable(application_ApplicationRealms.__init__)


def test_application_applicationrealms_constructor_args():
    sig = inspect.signature(application_ApplicationRealms.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_application_applicationrealms_has_uid():
    assert hasattr(application_ApplicationRealms, "uid")
    descriptor = None
    for klass in application_ApplicationRealms.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_application_applicationrealms_has_name():
    assert hasattr(application_ApplicationRealms, "name")
    descriptor = None
    for klass in application_ApplicationRealms.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_application_applicationmappers_is_not_abstract():
    assert not inspect.isabstract(application_ApplicationMappers)


def test_application_applicationmappers_constructor_exists():
    assert callable(application_ApplicationMappers.__init__)


def test_application_applicationmappers_constructor_args():
    sig = inspect.signature(application_ApplicationMappers.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_application_applicationmappers_has_name():
    assert hasattr(application_ApplicationMappers, "name")
    descriptor = None
    for klass in application_ApplicationMappers.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_application_applicationmappers_has_uid():
    assert hasattr(application_ApplicationMappers, "uid")
    descriptor = None
    for klass in application_ApplicationMappers.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_application_applicationrecipes_is_not_abstract():
    assert not inspect.isabstract(application_ApplicationRecipes)


def test_application_applicationrecipes_constructor_exists():
    assert callable(application_ApplicationRecipes.__init__)


def test_application_applicationrecipes_constructor_args():
    sig = inspect.signature(application_ApplicationRecipes.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_application_applicationrecipes_has_name():
    assert hasattr(application_ApplicationRecipes, "name")
    descriptor = None
    for klass in application_ApplicationRecipes.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_application_applicationrecipes_has_uid():
    assert hasattr(application_ApplicationRecipes, "uid")
    descriptor = None
    for klass in application_ApplicationRecipes.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_application_application_is_not_abstract():
    assert not inspect.isabstract(application_Application)


def test_application_application_constructor_exists():
    assert callable(application_Application.__init__)


def test_application_application_constructor_args():
    sig = inspect.signature(application_Application.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_application_application_has_name():
    assert hasattr(application_Application, "name")
    descriptor = None
    for klass in application_Application.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_application_application_has_uid():
    assert hasattr(application_Application, "uid")
    descriptor = None
    for klass in application_Application.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_application_applicationgroup_is_not_abstract():
    assert not inspect.isabstract(application_ApplicationGroup)


def test_application_applicationgroup_constructor_exists():
    assert callable(application_ApplicationGroup.__init__)


def test_application_applicationgroup_constructor_args():
    sig = inspect.signature(application_ApplicationGroup.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_application_applicationgroup_has_name():
    assert hasattr(application_ApplicationGroup, "name")
    descriptor = None
    for klass in application_ApplicationGroup.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_application_applicationgroup_has_uid():
    assert hasattr(application_ApplicationGroup, "uid")
    descriptor = None
    for klass in application_ApplicationGroup.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)


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
application_Recipes_strategy = st.builds(
    application_Recipes,
)
application_Mappers_strategy = st.builds(
    application_Mappers,
)
application_MappingLayer_strategy = st.builds(
    application_MappingLayer,
)
application_ApplicationMapper_strategy = st.builds(
    application_ApplicationMapper,
    uid=
        safe_text,
    name=
        safe_text
)
application_ApplicationRealm_strategy = st.builds(
    application_ApplicationRealm,
    uid=
        safe_text,
    name=
        safe_text
)
application_ApplicationRecipe_strategy = st.builds(
    application_ApplicationRecipe,
    uid=
        safe_text,
    name=
        safe_text
)
application_Form_strategy = st.builds(
    application_Form,
)
application_ApplicationUIPackage_strategy = st.builds(
    application_ApplicationUIPackage,
    name=
        safe_text,
    uid=
        safe_text
)
application_StyleLibrary_strategy = st.builds(
    application_StyleLibrary,
)
application_ApplicationStyle_strategy = st.builds(
    application_ApplicationStyle,
    uid=
        safe_text,
    name=
        safe_text
)
application_Roles_strategy = st.builds(
    application_Roles,
)
application_ApplicationStyleLibraries_strategy = st.builds(
    application_ApplicationStyleLibraries,
    name=
        safe_text,
    uid=
        safe_text
)
application_ApplicationInfrastructureLayers_strategy = st.builds(
    application_ApplicationInfrastructureLayers,
    name=
        safe_text,
    uid=
        safe_text
)
application_ApplicationUILayer_strategy = st.builds(
    application_ApplicationUILayer,
    uid=
        safe_text,
    name=
        safe_text
)
application_MessageLibrary_strategy = st.builds(
    application_MessageLibrary,
)
application_Language_strategy = st.builds(
    application_Language,
)
application_ApplicationLanguages_strategy = st.builds(
    application_ApplicationLanguages,
    name=
        safe_text,
    uid=
        safe_text
)
application_ApplicationMessageLibrary_strategy = st.builds(
    application_ApplicationMessageLibrary,
    uid=
        safe_text,
    name=
        safe_text
)
application_EnterpriseInfrastructure_strategy = st.builds(
    application_EnterpriseInfrastructure,
)
application_ApplicationInfrastructureLayer_strategy = st.builds(
    application_ApplicationInfrastructureLayer,
    name=
        safe_text,
    uid=
        safe_text
)
application_ApplicationMessageLibraries_strategy = st.builds(
    application_ApplicationMessageLibraries,
    name=
        safe_text,
    uid=
        safe_text
)
application_ApplicationRealms_strategy = st.builds(
    application_ApplicationRealms,
    uid=
        safe_text,
    name=
        safe_text
)
application_ApplicationMappers_strategy = st.builds(
    application_ApplicationMappers,
    name=
        safe_text,
    uid=
        safe_text
)
application_ApplicationRecipes_strategy = st.builds(
    application_ApplicationRecipes,
    name=
        safe_text,
    uid=
        safe_text
)
application_Application_strategy = st.builds(
    application_Application,
    name=
        safe_text,
    uid=
        safe_text
)
application_ApplicationGroup_strategy = st.builds(
    application_ApplicationGroup,
    name=
        safe_text,
    uid=
        safe_text
)

@given(instance=application_Recipes_strategy)
@settings(max_examples=50)
def test_application_recipes_instantiation(instance):
    assert isinstance(instance, application_Recipes)

@given(instance=application_Mappers_strategy)
@settings(max_examples=50)
def test_application_mappers_instantiation(instance):
    assert isinstance(instance, application_Mappers)

@given(instance=application_MappingLayer_strategy)
@settings(max_examples=50)
def test_application_mappinglayer_instantiation(instance):
    assert isinstance(instance, application_MappingLayer)

@given(instance=application_ApplicationMapper_strategy)
@settings(max_examples=50)
def test_application_applicationmapper_instantiation(instance):
    assert isinstance(instance, application_ApplicationMapper)



@given(instance=application_ApplicationMapper_strategy)
def test_application_applicationmapper_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=application_ApplicationMapper_strategy)
def test_application_applicationmapper_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=application_ApplicationRealm_strategy)
@settings(max_examples=50)
def test_application_applicationrealm_instantiation(instance):
    assert isinstance(instance, application_ApplicationRealm)



@given(instance=application_ApplicationRealm_strategy)
def test_application_applicationrealm_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=application_ApplicationRealm_strategy)
def test_application_applicationrealm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=application_ApplicationRecipe_strategy)
@settings(max_examples=50)
def test_application_applicationrecipe_instantiation(instance):
    assert isinstance(instance, application_ApplicationRecipe)



@given(instance=application_ApplicationRecipe_strategy)
def test_application_applicationrecipe_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=application_ApplicationRecipe_strategy)
def test_application_applicationrecipe_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=application_Form_strategy)
@settings(max_examples=50)
def test_application_form_instantiation(instance):
    assert isinstance(instance, application_Form)

@given(instance=application_ApplicationUIPackage_strategy)
@settings(max_examples=50)
def test_application_applicationuipackage_instantiation(instance):
    assert isinstance(instance, application_ApplicationUIPackage)



@given(instance=application_ApplicationUIPackage_strategy)
def test_application_applicationuipackage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=application_ApplicationUIPackage_strategy)
def test_application_applicationuipackage_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=application_StyleLibrary_strategy)
@settings(max_examples=50)
def test_application_stylelibrary_instantiation(instance):
    assert isinstance(instance, application_StyleLibrary)

@given(instance=application_ApplicationStyle_strategy)
@settings(max_examples=50)
def test_application_applicationstyle_instantiation(instance):
    assert isinstance(instance, application_ApplicationStyle)



@given(instance=application_ApplicationStyle_strategy)
def test_application_applicationstyle_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=application_ApplicationStyle_strategy)
def test_application_applicationstyle_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=application_Roles_strategy)
@settings(max_examples=50)
def test_application_roles_instantiation(instance):
    assert isinstance(instance, application_Roles)

@given(instance=application_ApplicationStyleLibraries_strategy)
@settings(max_examples=50)
def test_application_applicationstylelibraries_instantiation(instance):
    assert isinstance(instance, application_ApplicationStyleLibraries)



@given(instance=application_ApplicationStyleLibraries_strategy)
def test_application_applicationstylelibraries_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=application_ApplicationStyleLibraries_strategy)
def test_application_applicationstylelibraries_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=application_ApplicationInfrastructureLayers_strategy)
@settings(max_examples=50)
def test_application_applicationinfrastructurelayers_instantiation(instance):
    assert isinstance(instance, application_ApplicationInfrastructureLayers)



@given(instance=application_ApplicationInfrastructureLayers_strategy)
def test_application_applicationinfrastructurelayers_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=application_ApplicationInfrastructureLayers_strategy)
def test_application_applicationinfrastructurelayers_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=application_ApplicationUILayer_strategy)
@settings(max_examples=50)
def test_application_applicationuilayer_instantiation(instance):
    assert isinstance(instance, application_ApplicationUILayer)



@given(instance=application_ApplicationUILayer_strategy)
def test_application_applicationuilayer_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=application_ApplicationUILayer_strategy)
def test_application_applicationuilayer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=application_MessageLibrary_strategy)
@settings(max_examples=50)
def test_application_messagelibrary_instantiation(instance):
    assert isinstance(instance, application_MessageLibrary)

@given(instance=application_Language_strategy)
@settings(max_examples=50)
def test_application_language_instantiation(instance):
    assert isinstance(instance, application_Language)

@given(instance=application_ApplicationLanguages_strategy)
@settings(max_examples=50)
def test_application_applicationlanguages_instantiation(instance):
    assert isinstance(instance, application_ApplicationLanguages)



@given(instance=application_ApplicationLanguages_strategy)
def test_application_applicationlanguages_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=application_ApplicationLanguages_strategy)
def test_application_applicationlanguages_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=application_ApplicationMessageLibrary_strategy)
@settings(max_examples=50)
def test_application_applicationmessagelibrary_instantiation(instance):
    assert isinstance(instance, application_ApplicationMessageLibrary)



@given(instance=application_ApplicationMessageLibrary_strategy)
def test_application_applicationmessagelibrary_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=application_ApplicationMessageLibrary_strategy)
def test_application_applicationmessagelibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=application_EnterpriseInfrastructure_strategy)
@settings(max_examples=50)
def test_application_enterpriseinfrastructure_instantiation(instance):
    assert isinstance(instance, application_EnterpriseInfrastructure)

@given(instance=application_ApplicationInfrastructureLayer_strategy)
@settings(max_examples=50)
def test_application_applicationinfrastructurelayer_instantiation(instance):
    assert isinstance(instance, application_ApplicationInfrastructureLayer)



@given(instance=application_ApplicationInfrastructureLayer_strategy)
def test_application_applicationinfrastructurelayer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=application_ApplicationInfrastructureLayer_strategy)
def test_application_applicationinfrastructurelayer_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=application_ApplicationMessageLibraries_strategy)
@settings(max_examples=50)
def test_application_applicationmessagelibraries_instantiation(instance):
    assert isinstance(instance, application_ApplicationMessageLibraries)



@given(instance=application_ApplicationMessageLibraries_strategy)
def test_application_applicationmessagelibraries_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=application_ApplicationMessageLibraries_strategy)
def test_application_applicationmessagelibraries_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=application_ApplicationRealms_strategy)
@settings(max_examples=50)
def test_application_applicationrealms_instantiation(instance):
    assert isinstance(instance, application_ApplicationRealms)



@given(instance=application_ApplicationRealms_strategy)
def test_application_applicationrealms_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=application_ApplicationRealms_strategy)
def test_application_applicationrealms_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=application_ApplicationMappers_strategy)
@settings(max_examples=50)
def test_application_applicationmappers_instantiation(instance):
    assert isinstance(instance, application_ApplicationMappers)



@given(instance=application_ApplicationMappers_strategy)
def test_application_applicationmappers_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=application_ApplicationMappers_strategy)
def test_application_applicationmappers_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=application_ApplicationRecipes_strategy)
@settings(max_examples=50)
def test_application_applicationrecipes_instantiation(instance):
    assert isinstance(instance, application_ApplicationRecipes)



@given(instance=application_ApplicationRecipes_strategy)
def test_application_applicationrecipes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=application_ApplicationRecipes_strategy)
def test_application_applicationrecipes_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=application_Application_strategy)
@settings(max_examples=50)
def test_application_application_instantiation(instance):
    assert isinstance(instance, application_Application)



@given(instance=application_Application_strategy)
def test_application_application_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=application_Application_strategy)
def test_application_application_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=application_ApplicationGroup_strategy)
@settings(max_examples=50)
def test_application_applicationgroup_instantiation(instance):
    assert isinstance(instance, application_ApplicationGroup)



@given(instance=application_ApplicationGroup_strategy)
def test_application_applicationgroup_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=application_ApplicationGroup_strategy)
def test_application_applicationgroup_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original
