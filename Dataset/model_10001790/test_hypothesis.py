import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Calculate_caloriesBurnt,
    Count_Steps,
    Give_Weight,
    Give_Name,
    Weekly_Chart,
    Update_Data,
    Draw_Path,
    Count_Steps_and_Calories,
    User,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_calculate_caloriesburnt_is_not_abstract():
    assert not inspect.isabstract(Calculate_caloriesBurnt)


def test_calculate_caloriesburnt_constructor_exists():
    assert callable(Calculate_caloriesBurnt.__init__)


def test_calculate_caloriesburnt_constructor_args():
    sig = inspect.signature(Calculate_caloriesBurnt.__init__)
    params = list(sig.parameters.keys())
    assert "CaloriesBurnt" in params, "Missing parameter 'CaloriesBurnt'"
    assert "Steps" in params, "Missing parameter 'Steps'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_calculate_caloriesburnt_has_CaloriesBurnt():
    assert hasattr(Calculate_caloriesBurnt, "CaloriesBurnt")
    descriptor = None
    for klass in Calculate_caloriesBurnt.__mro__:
        if "CaloriesBurnt" in klass.__dict__:
            descriptor = klass.__dict__["CaloriesBurnt"]
            break
    assert isinstance(descriptor, property)

def test_calculate_caloriesburnt_has_Steps():
    assert hasattr(Calculate_caloriesBurnt, "Steps")
    descriptor = None
    for klass in Calculate_caloriesBurnt.__mro__:
        if "Steps" in klass.__dict__:
            descriptor = klass.__dict__["Steps"]
            break
    assert isinstance(descriptor, property)

def test_calculate_caloriesburnt_has_Name():
    assert hasattr(Calculate_caloriesBurnt, "Name")
    descriptor = None
    for klass in Calculate_caloriesBurnt.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_count_steps_is_not_abstract():
    assert not inspect.isabstract(Count_Steps)


def test_count_steps_constructor_exists():
    assert callable(Count_Steps.__init__)


def test_count_steps_constructor_args():
    sig = inspect.signature(Count_Steps.__init__)
    params = list(sig.parameters.keys())
    assert "Steps" in params, "Missing parameter 'Steps'"

def test_count_steps_has_Steps():
    assert hasattr(Count_Steps, "Steps")
    descriptor = None
    for klass in Count_Steps.__mro__:
        if "Steps" in klass.__dict__:
            descriptor = klass.__dict__["Steps"]
            break
    assert isinstance(descriptor, property)



def test_give_weight_is_not_abstract():
    assert not inspect.isabstract(Give_Weight)


def test_give_weight_constructor_exists():
    assert callable(Give_Weight.__init__)


def test_give_weight_constructor_args():
    sig = inspect.signature(Give_Weight.__init__)
    params = list(sig.parameters.keys())
    assert "Weight" in params, "Missing parameter 'Weight'"

def test_give_weight_has_Weight():
    assert hasattr(Give_Weight, "Weight")
    descriptor = None
    for klass in Give_Weight.__mro__:
        if "Weight" in klass.__dict__:
            descriptor = klass.__dict__["Weight"]
            break
    assert isinstance(descriptor, property)



def test_give_name_is_not_abstract():
    assert not inspect.isabstract(Give_Name)


def test_give_name_constructor_exists():
    assert callable(Give_Name.__init__)


def test_give_name_constructor_args():
    sig = inspect.signature(Give_Name.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_give_name_has_Name():
    assert hasattr(Give_Name, "Name")
    descriptor = None
    for klass in Give_Name.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_weekly_chart_is_not_abstract():
    assert not inspect.isabstract(Weekly_Chart)


def test_weekly_chart_constructor_exists():
    assert callable(Weekly_Chart.__init__)


def test_weekly_chart_constructor_args():
    sig = inspect.signature(Weekly_Chart.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Steps" in params, "Missing parameter 'Steps'"
    assert "CaloriesBurnt" in params, "Missing parameter 'CaloriesBurnt'"

def test_weekly_chart_has_Name():
    assert hasattr(Weekly_Chart, "Name")
    descriptor = None
    for klass in Weekly_Chart.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_weekly_chart_has_Steps():
    assert hasattr(Weekly_Chart, "Steps")
    descriptor = None
    for klass in Weekly_Chart.__mro__:
        if "Steps" in klass.__dict__:
            descriptor = klass.__dict__["Steps"]
            break
    assert isinstance(descriptor, property)

def test_weekly_chart_has_CaloriesBurnt():
    assert hasattr(Weekly_Chart, "CaloriesBurnt")
    descriptor = None
    for klass in Weekly_Chart.__mro__:
        if "CaloriesBurnt" in klass.__dict__:
            descriptor = klass.__dict__["CaloriesBurnt"]
            break
    assert isinstance(descriptor, property)



def test_update_data_is_not_abstract():
    assert not inspect.isabstract(Update_Data)


def test_update_data_constructor_exists():
    assert callable(Update_Data.__init__)


def test_update_data_constructor_args():
    sig = inspect.signature(Update_Data.__init__)
    params = list(sig.parameters.keys())
    assert "Weight" in params, "Missing parameter 'Weight'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_update_data_has_Weight():
    assert hasattr(Update_Data, "Weight")
    descriptor = None
    for klass in Update_Data.__mro__:
        if "Weight" in klass.__dict__:
            descriptor = klass.__dict__["Weight"]
            break
    assert isinstance(descriptor, property)

def test_update_data_has_Name():
    assert hasattr(Update_Data, "Name")
    descriptor = None
    for klass in Update_Data.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_draw_path_is_not_abstract():
    assert not inspect.isabstract(Draw_Path)


def test_draw_path_constructor_exists():
    assert callable(Draw_Path.__init__)


def test_draw_path_constructor_args():
    sig = inspect.signature(Draw_Path.__init__)
    params = list(sig.parameters.keys())
    assert "Route" in params, "Missing parameter 'Route'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_draw_path_has_Route():
    assert hasattr(Draw_Path, "Route")
    descriptor = None
    for klass in Draw_Path.__mro__:
        if "Route" in klass.__dict__:
            descriptor = klass.__dict__["Route"]
            break
    assert isinstance(descriptor, property)

def test_draw_path_has_Name():
    assert hasattr(Draw_Path, "Name")
    descriptor = None
    for klass in Draw_Path.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_count_steps_and_calories_is_not_abstract():
    assert not inspect.isabstract(Count_Steps_and_Calories)


def test_count_steps_and_calories_constructor_exists():
    assert callable(Count_Steps_and_Calories.__init__)


def test_count_steps_and_calories_constructor_args():
    sig = inspect.signature(Count_Steps_and_Calories.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "CaloriesBurnt" in params, "Missing parameter 'CaloriesBurnt'"
    assert "Steps" in params, "Missing parameter 'Steps'"

def test_count_steps_and_calories_has_Name():
    assert hasattr(Count_Steps_and_Calories, "Name")
    descriptor = None
    for klass in Count_Steps_and_Calories.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_count_steps_and_calories_has_CaloriesBurnt():
    assert hasattr(Count_Steps_and_Calories, "CaloriesBurnt")
    descriptor = None
    for klass in Count_Steps_and_Calories.__mro__:
        if "CaloriesBurnt" in klass.__dict__:
            descriptor = klass.__dict__["CaloriesBurnt"]
            break
    assert isinstance(descriptor, property)

def test_count_steps_and_calories_has_Steps():
    assert hasattr(Count_Steps_and_Calories, "Steps")
    descriptor = None
    for klass in Count_Steps_and_Calories.__mro__:
        if "Steps" in klass.__dict__:
            descriptor = klass.__dict__["Steps"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "Path_Drawn" in params, "Missing parameter 'Path_Drawn'"
    assert "Calories_Burnt" in params, "Missing parameter 'Calories_Burnt'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Steps" in params, "Missing parameter 'Steps'"
    assert "Weight" in params, "Missing parameter 'Weight'"

def test_user_has_Path_Drawn():
    assert hasattr(User, "Path_Drawn")
    descriptor = None
    for klass in User.__mro__:
        if "Path_Drawn" in klass.__dict__:
            descriptor = klass.__dict__["Path_Drawn"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Calories_Burnt():
    assert hasattr(User, "Calories_Burnt")
    descriptor = None
    for klass in User.__mro__:
        if "Calories_Burnt" in klass.__dict__:
            descriptor = klass.__dict__["Calories_Burnt"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Name():
    assert hasattr(User, "Name")
    descriptor = None
    for klass in User.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Steps():
    assert hasattr(User, "Steps")
    descriptor = None
    for klass in User.__mro__:
        if "Steps" in klass.__dict__:
            descriptor = klass.__dict__["Steps"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Weight():
    assert hasattr(User, "Weight")
    descriptor = None
    for klass in User.__mro__:
        if "Weight" in klass.__dict__:
            descriptor = klass.__dict__["Weight"]
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
Calculate_caloriesBurnt_strategy = st.builds(
    Calculate_caloriesBurnt,
    CaloriesBurnt=
        safe_text,
    Steps=
        st.integers(),
    Name=
        safe_text
)
Count_Steps_strategy = st.builds(
    Count_Steps,
    Steps=
        st.integers()
)
Give_Weight_strategy = st.builds(
    Give_Weight,
    Weight=
        st.integers()
)
Give_Name_strategy = st.builds(
    Give_Name,
    Name=
        safe_text
)
Weekly_Chart_strategy = st.builds(
    Weekly_Chart,
    Name=
        safe_text,
    Steps=
        st.integers(),
    CaloriesBurnt=
        safe_text
)
Update_Data_strategy = st.builds(
    Update_Data,
    Weight=
        st.integers(),
    Name=
        safe_text
)
Draw_Path_strategy = st.builds(
    Draw_Path,
    Route=
        safe_text,
    Name=
        safe_text
)
Count_Steps_and_Calories_strategy = st.builds(
    Count_Steps_and_Calories,
    Name=
        safe_text,
    CaloriesBurnt=
        safe_text,
    Steps=
        st.integers()
)
User_strategy = st.builds(
    User,
    Path_Drawn=
        safe_text,
    Calories_Burnt=
        safe_text,
    Name=
        safe_text,
    Steps=
        st.integers(),
    Weight=
        st.integers()
)

@given(instance=Calculate_caloriesBurnt_strategy)
@settings(max_examples=50)
def test_calculate_caloriesburnt_instantiation(instance):
    assert isinstance(instance, Calculate_caloriesBurnt)



@given(instance=Calculate_caloriesBurnt_strategy)
def test_calculate_caloriesburnt_CaloriesBurnt_setter(instance):
    original = instance.CaloriesBurnt
    instance.CaloriesBurnt = original
    assert instance.CaloriesBurnt == original



@given(instance=Calculate_caloriesBurnt_strategy)
def test_calculate_caloriesburnt_Steps_setter(instance):
    original = instance.Steps
    instance.Steps = original
    assert instance.Steps == original



@given(instance=Calculate_caloriesBurnt_strategy)
def test_calculate_caloriesburnt_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Count_Steps_strategy)
@settings(max_examples=50)
def test_count_steps_instantiation(instance):
    assert isinstance(instance, Count_Steps)



@given(instance=Count_Steps_strategy)
def test_count_steps_Steps_setter(instance):
    original = instance.Steps
    instance.Steps = original
    assert instance.Steps == original

@given(instance=Give_Weight_strategy)
@settings(max_examples=50)
def test_give_weight_instantiation(instance):
    assert isinstance(instance, Give_Weight)



@given(instance=Give_Weight_strategy)
def test_give_weight_Weight_setter(instance):
    original = instance.Weight
    instance.Weight = original
    assert instance.Weight == original

@given(instance=Give_Name_strategy)
@settings(max_examples=50)
def test_give_name_instantiation(instance):
    assert isinstance(instance, Give_Name)



@given(instance=Give_Name_strategy)
def test_give_name_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Weekly_Chart_strategy)
@settings(max_examples=50)
def test_weekly_chart_instantiation(instance):
    assert isinstance(instance, Weekly_Chart)



@given(instance=Weekly_Chart_strategy)
def test_weekly_chart_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Weekly_Chart_strategy)
def test_weekly_chart_Steps_setter(instance):
    original = instance.Steps
    instance.Steps = original
    assert instance.Steps == original



@given(instance=Weekly_Chart_strategy)
def test_weekly_chart_CaloriesBurnt_setter(instance):
    original = instance.CaloriesBurnt
    instance.CaloriesBurnt = original
    assert instance.CaloriesBurnt == original

@given(instance=Update_Data_strategy)
@settings(max_examples=50)
def test_update_data_instantiation(instance):
    assert isinstance(instance, Update_Data)



@given(instance=Update_Data_strategy)
def test_update_data_Weight_setter(instance):
    original = instance.Weight
    instance.Weight = original
    assert instance.Weight == original



@given(instance=Update_Data_strategy)
def test_update_data_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Draw_Path_strategy)
@settings(max_examples=50)
def test_draw_path_instantiation(instance):
    assert isinstance(instance, Draw_Path)



@given(instance=Draw_Path_strategy)
def test_draw_path_Route_setter(instance):
    original = instance.Route
    instance.Route = original
    assert instance.Route == original



@given(instance=Draw_Path_strategy)
def test_draw_path_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Count_Steps_and_Calories_strategy)
@settings(max_examples=50)
def test_count_steps_and_calories_instantiation(instance):
    assert isinstance(instance, Count_Steps_and_Calories)



@given(instance=Count_Steps_and_Calories_strategy)
def test_count_steps_and_calories_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Count_Steps_and_Calories_strategy)
def test_count_steps_and_calories_CaloriesBurnt_setter(instance):
    original = instance.CaloriesBurnt
    instance.CaloriesBurnt = original
    assert instance.CaloriesBurnt == original



@given(instance=Count_Steps_and_Calories_strategy)
def test_count_steps_and_calories_Steps_setter(instance):
    original = instance.Steps
    instance.Steps = original
    assert instance.Steps == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_Path_Drawn_setter(instance):
    original = instance.Path_Drawn
    instance.Path_Drawn = original
    assert instance.Path_Drawn == original



@given(instance=User_strategy)
def test_user_Calories_Burnt_setter(instance):
    original = instance.Calories_Burnt
    instance.Calories_Burnt = original
    assert instance.Calories_Burnt == original



@given(instance=User_strategy)
def test_user_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=User_strategy)
def test_user_Steps_setter(instance):
    original = instance.Steps
    instance.Steps = original
    assert instance.Steps == original



@given(instance=User_strategy)
def test_user_Weight_setter(instance):
    original = instance.Weight
    instance.Weight = original
    assert instance.Weight == original
