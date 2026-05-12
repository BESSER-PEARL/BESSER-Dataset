import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Effect,
    dsl_LauncherEffect,
    dsl_DamageEffect,
    dsl_PersistentEffect,
    dsl_UnitWeaponLink,
    dsl_Color,
    dsl_ActorList,
    Actor,
    dsl_ParticleActor,
    dsl_AnimtationActor,
    dsl_ModelActor,
    dsl_Projectile,
    dsl_Turrent,
    dsl_Effect,
    dsl_Actor,
    dsl_Race,
    dsl_Unit,
    dsl_Weapon,
    dsl_Model,
    dsl_Mover,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_effect_is_not_abstract():
    assert not inspect.isabstract(Effect)


def test_effect_constructor_exists():
    assert callable(Effect.__init__)


def test_effect_constructor_args():
    sig = inspect.signature(Effect.__init__)
    params = list(sig.parameters.keys())



def test_dsl_launchereffect_is_not_abstract():
    assert not inspect.isabstract(dsl_LauncherEffect)


def test_dsl_launchereffect_constructor_exists():
    assert callable(dsl_LauncherEffect.__init__)


def test_dsl_launchereffect_constructor_args():
    sig = inspect.signature(dsl_LauncherEffect.__init__)
    params = list(sig.parameters.keys())



def test_dsl_damageeffect_is_not_abstract():
    assert not inspect.isabstract(dsl_DamageEffect)


def test_dsl_damageeffect_constructor_exists():
    assert callable(dsl_DamageEffect.__init__)


def test_dsl_damageeffect_constructor_args():
    sig = inspect.signature(dsl_DamageEffect.__init__)
    params = list(sig.parameters.keys())
    assert "amount" in params, "Missing parameter 'amount'"

def test_dsl_damageeffect_has_amount():
    assert hasattr(dsl_DamageEffect, "amount")
    descriptor = None
    for klass in dsl_DamageEffect.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)



def test_dsl_persistenteffect_is_not_abstract():
    assert not inspect.isabstract(dsl_PersistentEffect)


def test_dsl_persistenteffect_constructor_exists():
    assert callable(dsl_PersistentEffect.__init__)


def test_dsl_persistenteffect_constructor_args():
    sig = inspect.signature(dsl_PersistentEffect.__init__)
    params = list(sig.parameters.keys())
    assert "ranges" in params, "Missing parameter 'ranges'"
    assert "durations" in params, "Missing parameter 'durations'"
    assert "periodCount" in params, "Missing parameter 'periodCount'"

def test_dsl_persistenteffect_has_ranges():
    assert hasattr(dsl_PersistentEffect, "ranges")
    descriptor = None
    for klass in dsl_PersistentEffect.__mro__:
        if "ranges" in klass.__dict__:
            descriptor = klass.__dict__["ranges"]
            break
    assert isinstance(descriptor, property)

def test_dsl_persistenteffect_has_durations():
    assert hasattr(dsl_PersistentEffect, "durations")
    descriptor = None
    for klass in dsl_PersistentEffect.__mro__:
        if "durations" in klass.__dict__:
            descriptor = klass.__dict__["durations"]
            break
    assert isinstance(descriptor, property)

def test_dsl_persistenteffect_has_periodCount():
    assert hasattr(dsl_PersistentEffect, "periodCount")
    descriptor = None
    for klass in dsl_PersistentEffect.__mro__:
        if "periodCount" in klass.__dict__:
            descriptor = klass.__dict__["periodCount"]
            break
    assert isinstance(descriptor, property)



def test_dsl_unitweaponlink_is_not_abstract():
    assert not inspect.isabstract(dsl_UnitWeaponLink)


def test_dsl_unitweaponlink_constructor_exists():
    assert callable(dsl_UnitWeaponLink.__init__)


def test_dsl_unitweaponlink_constructor_args():
    sig = inspect.signature(dsl_UnitWeaponLink.__init__)
    params = list(sig.parameters.keys())



def test_dsl_color_is_not_abstract():
    assert not inspect.isabstract(dsl_Color)


def test_dsl_color_constructor_exists():
    assert callable(dsl_Color.__init__)


def test_dsl_color_constructor_args():
    sig = inspect.signature(dsl_Color.__init__)
    params = list(sig.parameters.keys())
    assert "g" in params, "Missing parameter 'g'"
    assert "a" in params, "Missing parameter 'a'"
    assert "r" in params, "Missing parameter 'r'"
    assert "b" in params, "Missing parameter 'b'"

def test_dsl_color_has_g():
    assert hasattr(dsl_Color, "g")
    descriptor = None
    for klass in dsl_Color.__mro__:
        if "g" in klass.__dict__:
            descriptor = klass.__dict__["g"]
            break
    assert isinstance(descriptor, property)

def test_dsl_color_has_a():
    assert hasattr(dsl_Color, "a")
    descriptor = None
    for klass in dsl_Color.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
            break
    assert isinstance(descriptor, property)

def test_dsl_color_has_r():
    assert hasattr(dsl_Color, "r")
    descriptor = None
    for klass in dsl_Color.__mro__:
        if "r" in klass.__dict__:
            descriptor = klass.__dict__["r"]
            break
    assert isinstance(descriptor, property)

def test_dsl_color_has_b():
    assert hasattr(dsl_Color, "b")
    descriptor = None
    for klass in dsl_Color.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)



def test_dsl_actorlist_is_not_abstract():
    assert not inspect.isabstract(dsl_ActorList)


def test_dsl_actorlist_constructor_exists():
    assert callable(dsl_ActorList.__init__)


def test_dsl_actorlist_constructor_args():
    sig = inspect.signature(dsl_ActorList.__init__)
    params = list(sig.parameters.keys())
    assert "trigger" in params, "Missing parameter 'trigger'"

def test_dsl_actorlist_has_trigger():
    assert hasattr(dsl_ActorList, "trigger")
    descriptor = None
    for klass in dsl_ActorList.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)



def test_actor_is_not_abstract():
    assert not inspect.isabstract(Actor)


def test_actor_constructor_exists():
    assert callable(Actor.__init__)


def test_actor_constructor_args():
    sig = inspect.signature(Actor.__init__)
    params = list(sig.parameters.keys())



def test_dsl_particleactor_is_not_abstract():
    assert not inspect.isabstract(dsl_ParticleActor)


def test_dsl_particleactor_constructor_exists():
    assert callable(dsl_ParticleActor.__init__)


def test_dsl_particleactor_constructor_args():
    sig = inspect.signature(dsl_ParticleActor.__init__)
    params = list(sig.parameters.keys())
    assert "perSecond" in params, "Missing parameter 'perSecond'"
    assert "add" in params, "Missing parameter 'add'"
    assert "nbCol" in params, "Missing parameter 'nbCol'"
    assert "duration" in params, "Missing parameter 'duration'"
    assert "nbRow" in params, "Missing parameter 'nbRow'"
    assert "emissionBone" in params, "Missing parameter 'emissionBone'"
    assert "maxCount" in params, "Missing parameter 'maxCount'"
    assert "endSize" in params, "Missing parameter 'endSize'"
    assert "startSize" in params, "Missing parameter 'startSize'"
    assert "directionBone" in params, "Missing parameter 'directionBone'"
    assert "minLife" in params, "Missing parameter 'minLife'"
    assert "startVariation" in params, "Missing parameter 'startVariation'"
    assert "spritePath" in params, "Missing parameter 'spritePath'"
    assert "maxLife" in params, "Missing parameter 'maxLife'"

def test_dsl_particleactor_has_perSecond():
    assert hasattr(dsl_ParticleActor, "perSecond")
    descriptor = None
    for klass in dsl_ParticleActor.__mro__:
        if "perSecond" in klass.__dict__:
            descriptor = klass.__dict__["perSecond"]
            break
    assert isinstance(descriptor, property)

def test_dsl_particleactor_has_add():
    assert hasattr(dsl_ParticleActor, "add")
    descriptor = None
    for klass in dsl_ParticleActor.__mro__:
        if "add" in klass.__dict__:
            descriptor = klass.__dict__["add"]
            break
    assert isinstance(descriptor, property)

def test_dsl_particleactor_has_nbCol():
    assert hasattr(dsl_ParticleActor, "nbCol")
    descriptor = None
    for klass in dsl_ParticleActor.__mro__:
        if "nbCol" in klass.__dict__:
            descriptor = klass.__dict__["nbCol"]
            break
    assert isinstance(descriptor, property)

def test_dsl_particleactor_has_duration():
    assert hasattr(dsl_ParticleActor, "duration")
    descriptor = None
    for klass in dsl_ParticleActor.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)

def test_dsl_particleactor_has_nbRow():
    assert hasattr(dsl_ParticleActor, "nbRow")
    descriptor = None
    for klass in dsl_ParticleActor.__mro__:
        if "nbRow" in klass.__dict__:
            descriptor = klass.__dict__["nbRow"]
            break
    assert isinstance(descriptor, property)

def test_dsl_particleactor_has_emissionBone():
    assert hasattr(dsl_ParticleActor, "emissionBone")
    descriptor = None
    for klass in dsl_ParticleActor.__mro__:
        if "emissionBone" in klass.__dict__:
            descriptor = klass.__dict__["emissionBone"]
            break
    assert isinstance(descriptor, property)

def test_dsl_particleactor_has_maxCount():
    assert hasattr(dsl_ParticleActor, "maxCount")
    descriptor = None
    for klass in dsl_ParticleActor.__mro__:
        if "maxCount" in klass.__dict__:
            descriptor = klass.__dict__["maxCount"]
            break
    assert isinstance(descriptor, property)

def test_dsl_particleactor_has_endSize():
    assert hasattr(dsl_ParticleActor, "endSize")
    descriptor = None
    for klass in dsl_ParticleActor.__mro__:
        if "endSize" in klass.__dict__:
            descriptor = klass.__dict__["endSize"]
            break
    assert isinstance(descriptor, property)

def test_dsl_particleactor_has_startSize():
    assert hasattr(dsl_ParticleActor, "startSize")
    descriptor = None
    for klass in dsl_ParticleActor.__mro__:
        if "startSize" in klass.__dict__:
            descriptor = klass.__dict__["startSize"]
            break
    assert isinstance(descriptor, property)

def test_dsl_particleactor_has_directionBone():
    assert hasattr(dsl_ParticleActor, "directionBone")
    descriptor = None
    for klass in dsl_ParticleActor.__mro__:
        if "directionBone" in klass.__dict__:
            descriptor = klass.__dict__["directionBone"]
            break
    assert isinstance(descriptor, property)

def test_dsl_particleactor_has_minLife():
    assert hasattr(dsl_ParticleActor, "minLife")
    descriptor = None
    for klass in dsl_ParticleActor.__mro__:
        if "minLife" in klass.__dict__:
            descriptor = klass.__dict__["minLife"]
            break
    assert isinstance(descriptor, property)

def test_dsl_particleactor_has_startVariation():
    assert hasattr(dsl_ParticleActor, "startVariation")
    descriptor = None
    for klass in dsl_ParticleActor.__mro__:
        if "startVariation" in klass.__dict__:
            descriptor = klass.__dict__["startVariation"]
            break
    assert isinstance(descriptor, property)

def test_dsl_particleactor_has_spritePath():
    assert hasattr(dsl_ParticleActor, "spritePath")
    descriptor = None
    for klass in dsl_ParticleActor.__mro__:
        if "spritePath" in klass.__dict__:
            descriptor = klass.__dict__["spritePath"]
            break
    assert isinstance(descriptor, property)

def test_dsl_particleactor_has_maxLife():
    assert hasattr(dsl_ParticleActor, "maxLife")
    descriptor = None
    for klass in dsl_ParticleActor.__mro__:
        if "maxLife" in klass.__dict__:
            descriptor = klass.__dict__["maxLife"]
            break
    assert isinstance(descriptor, property)



def test_dsl_animtationactor_is_not_abstract():
    assert not inspect.isabstract(dsl_AnimtationActor)


def test_dsl_animtationactor_constructor_exists():
    assert callable(dsl_AnimtationActor.__init__)


def test_dsl_animtationactor_constructor_args():
    sig = inspect.signature(dsl_AnimtationActor.__init__)
    params = list(sig.parameters.keys())
    assert "animName" in params, "Missing parameter 'animName'"
    assert "cycle" in params, "Missing parameter 'cycle'"
    assert "speed" in params, "Missing parameter 'speed'"

def test_dsl_animtationactor_has_animName():
    assert hasattr(dsl_AnimtationActor, "animName")
    descriptor = None
    for klass in dsl_AnimtationActor.__mro__:
        if "animName" in klass.__dict__:
            descriptor = klass.__dict__["animName"]
            break
    assert isinstance(descriptor, property)

def test_dsl_animtationactor_has_cycle():
    assert hasattr(dsl_AnimtationActor, "cycle")
    descriptor = None
    for klass in dsl_AnimtationActor.__mro__:
        if "cycle" in klass.__dict__:
            descriptor = klass.__dict__["cycle"]
            break
    assert isinstance(descriptor, property)

def test_dsl_animtationactor_has_speed():
    assert hasattr(dsl_AnimtationActor, "speed")
    descriptor = None
    for klass in dsl_AnimtationActor.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)



def test_dsl_modelactor_is_not_abstract():
    assert not inspect.isabstract(dsl_ModelActor)


def test_dsl_modelactor_constructor_exists():
    assert callable(dsl_ModelActor.__init__)


def test_dsl_modelactor_constructor_args():
    sig = inspect.signature(dsl_ModelActor.__init__)
    params = list(sig.parameters.keys())
    assert "modelPath" in params, "Missing parameter 'modelPath'"
    assert "scale" in params, "Missing parameter 'scale'"

def test_dsl_modelactor_has_modelPath():
    assert hasattr(dsl_ModelActor, "modelPath")
    descriptor = None
    for klass in dsl_ModelActor.__mro__:
        if "modelPath" in klass.__dict__:
            descriptor = klass.__dict__["modelPath"]
            break
    assert isinstance(descriptor, property)

def test_dsl_modelactor_has_scale():
    assert hasattr(dsl_ModelActor, "scale")
    descriptor = None
    for klass in dsl_ModelActor.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)



def test_dsl_projectile_is_not_abstract():
    assert not inspect.isabstract(dsl_Projectile)


def test_dsl_projectile_constructor_exists():
    assert callable(dsl_Projectile.__init__)


def test_dsl_projectile_constructor_args():
    sig = inspect.signature(dsl_Projectile.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "mass" in params, "Missing parameter 'mass'"
    assert "precision" in params, "Missing parameter 'precision'"
    assert "speed" in params, "Missing parameter 'speed'"

def test_dsl_projectile_has_name():
    assert hasattr(dsl_Projectile, "name")
    descriptor = None
    for klass in dsl_Projectile.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dsl_projectile_has_mass():
    assert hasattr(dsl_Projectile, "mass")
    descriptor = None
    for klass in dsl_Projectile.__mro__:
        if "mass" in klass.__dict__:
            descriptor = klass.__dict__["mass"]
            break
    assert isinstance(descriptor, property)

def test_dsl_projectile_has_precision():
    assert hasattr(dsl_Projectile, "precision")
    descriptor = None
    for klass in dsl_Projectile.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)

def test_dsl_projectile_has_speed():
    assert hasattr(dsl_Projectile, "speed")
    descriptor = None
    for klass in dsl_Projectile.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)



def test_dsl_turrent_is_not_abstract():
    assert not inspect.isabstract(dsl_Turrent)


def test_dsl_turrent_constructor_exists():
    assert callable(dsl_Turrent.__init__)


def test_dsl_turrent_constructor_args():
    sig = inspect.signature(dsl_Turrent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "idleSpeed" in params, "Missing parameter 'idleSpeed'"
    assert "boneName" in params, "Missing parameter 'boneName'"
    assert "onIdle" in params, "Missing parameter 'onIdle'"
    assert "speed" in params, "Missing parameter 'speed'"

def test_dsl_turrent_has_name():
    assert hasattr(dsl_Turrent, "name")
    descriptor = None
    for klass in dsl_Turrent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dsl_turrent_has_idleSpeed():
    assert hasattr(dsl_Turrent, "idleSpeed")
    descriptor = None
    for klass in dsl_Turrent.__mro__:
        if "idleSpeed" in klass.__dict__:
            descriptor = klass.__dict__["idleSpeed"]
            break
    assert isinstance(descriptor, property)

def test_dsl_turrent_has_boneName():
    assert hasattr(dsl_Turrent, "boneName")
    descriptor = None
    for klass in dsl_Turrent.__mro__:
        if "boneName" in klass.__dict__:
            descriptor = klass.__dict__["boneName"]
            break
    assert isinstance(descriptor, property)

def test_dsl_turrent_has_onIdle():
    assert hasattr(dsl_Turrent, "onIdle")
    descriptor = None
    for klass in dsl_Turrent.__mro__:
        if "onIdle" in klass.__dict__:
            descriptor = klass.__dict__["onIdle"]
            break
    assert isinstance(descriptor, property)

def test_dsl_turrent_has_speed():
    assert hasattr(dsl_Turrent, "speed")
    descriptor = None
    for klass in dsl_Turrent.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)



def test_dsl_effect_is_not_abstract():
    assert not inspect.isabstract(dsl_Effect)


def test_dsl_effect_constructor_exists():
    assert callable(dsl_Effect.__init__)


def test_dsl_effect_constructor_args():
    sig = inspect.signature(dsl_Effect.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dsl_effect_has_name():
    assert hasattr(dsl_Effect, "name")
    descriptor = None
    for klass in dsl_Effect.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dsl_actor_is_not_abstract():
    assert not inspect.isabstract(dsl_Actor)


def test_dsl_actor_constructor_exists():
    assert callable(dsl_Actor.__init__)


def test_dsl_actor_constructor_args():
    sig = inspect.signature(dsl_Actor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dsl_actor_has_name():
    assert hasattr(dsl_Actor, "name")
    descriptor = None
    for klass in dsl_Actor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dsl_race_is_not_abstract():
    assert not inspect.isabstract(dsl_Race)


def test_dsl_race_constructor_exists():
    assert callable(dsl_Race.__init__)


def test_dsl_race_constructor_args():
    sig = inspect.signature(dsl_Race.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dsl_race_has_name():
    assert hasattr(dsl_Race, "name")
    descriptor = None
    for klass in dsl_Race.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dsl_unit_is_not_abstract():
    assert not inspect.isabstract(dsl_Unit)


def test_dsl_unit_constructor_exists():
    assert callable(dsl_Unit.__init__)


def test_dsl_unit_constructor_args():
    sig = inspect.signature(dsl_Unit.__init__)
    params = list(sig.parameters.keys())
    assert "radius" in params, "Missing parameter 'radius'"
    assert "maxHealth" in params, "Missing parameter 'maxHealth'"
    assert "mass" in params, "Missing parameter 'mass'"
    assert "sight" in params, "Missing parameter 'sight'"
    assert "name" in params, "Missing parameter 'name'"
    assert "separationRadius" in params, "Missing parameter 'separationRadius'"
    assert "speed" in params, "Missing parameter 'speed'"
    assert "uIName" in params, "Missing parameter 'uIName'"

def test_dsl_unit_has_radius():
    assert hasattr(dsl_Unit, "radius")
    descriptor = None
    for klass in dsl_Unit.__mro__:
        if "radius" in klass.__dict__:
            descriptor = klass.__dict__["radius"]
            break
    assert isinstance(descriptor, property)

def test_dsl_unit_has_maxHealth():
    assert hasattr(dsl_Unit, "maxHealth")
    descriptor = None
    for klass in dsl_Unit.__mro__:
        if "maxHealth" in klass.__dict__:
            descriptor = klass.__dict__["maxHealth"]
            break
    assert isinstance(descriptor, property)

def test_dsl_unit_has_mass():
    assert hasattr(dsl_Unit, "mass")
    descriptor = None
    for klass in dsl_Unit.__mro__:
        if "mass" in klass.__dict__:
            descriptor = klass.__dict__["mass"]
            break
    assert isinstance(descriptor, property)

def test_dsl_unit_has_sight():
    assert hasattr(dsl_Unit, "sight")
    descriptor = None
    for klass in dsl_Unit.__mro__:
        if "sight" in klass.__dict__:
            descriptor = klass.__dict__["sight"]
            break
    assert isinstance(descriptor, property)

def test_dsl_unit_has_name():
    assert hasattr(dsl_Unit, "name")
    descriptor = None
    for klass in dsl_Unit.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dsl_unit_has_separationRadius():
    assert hasattr(dsl_Unit, "separationRadius")
    descriptor = None
    for klass in dsl_Unit.__mro__:
        if "separationRadius" in klass.__dict__:
            descriptor = klass.__dict__["separationRadius"]
            break
    assert isinstance(descriptor, property)

def test_dsl_unit_has_speed():
    assert hasattr(dsl_Unit, "speed")
    descriptor = None
    for klass in dsl_Unit.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)

def test_dsl_unit_has_uIName():
    assert hasattr(dsl_Unit, "uIName")
    descriptor = None
    for klass in dsl_Unit.__mro__:
        if "uIName" in klass.__dict__:
            descriptor = klass.__dict__["uIName"]
            break
    assert isinstance(descriptor, property)



def test_dsl_weapon_is_not_abstract():
    assert not inspect.isabstract(dsl_Weapon)


def test_dsl_weapon_constructor_exists():
    assert callable(dsl_Weapon.__init__)


def test_dsl_weapon_constructor_args():
    sig = inspect.signature(dsl_Weapon.__init__)
    params = list(sig.parameters.keys())
    assert "uIName" in params, "Missing parameter 'uIName'"
    assert "scanRange" in params, "Missing parameter 'scanRange'"
    assert "range" in params, "Missing parameter 'range'"
    assert "sourceBone" in params, "Missing parameter 'sourceBone'"
    assert "name" in params, "Missing parameter 'name'"
    assert "directionBone" in params, "Missing parameter 'directionBone'"
    assert "period" in params, "Missing parameter 'period'"

def test_dsl_weapon_has_uIName():
    assert hasattr(dsl_Weapon, "uIName")
    descriptor = None
    for klass in dsl_Weapon.__mro__:
        if "uIName" in klass.__dict__:
            descriptor = klass.__dict__["uIName"]
            break
    assert isinstance(descriptor, property)

def test_dsl_weapon_has_scanRange():
    assert hasattr(dsl_Weapon, "scanRange")
    descriptor = None
    for klass in dsl_Weapon.__mro__:
        if "scanRange" in klass.__dict__:
            descriptor = klass.__dict__["scanRange"]
            break
    assert isinstance(descriptor, property)

def test_dsl_weapon_has_range():
    assert hasattr(dsl_Weapon, "range")
    descriptor = None
    for klass in dsl_Weapon.__mro__:
        if "range" in klass.__dict__:
            descriptor = klass.__dict__["range"]
            break
    assert isinstance(descriptor, property)

def test_dsl_weapon_has_sourceBone():
    assert hasattr(dsl_Weapon, "sourceBone")
    descriptor = None
    for klass in dsl_Weapon.__mro__:
        if "sourceBone" in klass.__dict__:
            descriptor = klass.__dict__["sourceBone"]
            break
    assert isinstance(descriptor, property)

def test_dsl_weapon_has_name():
    assert hasattr(dsl_Weapon, "name")
    descriptor = None
    for klass in dsl_Weapon.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dsl_weapon_has_directionBone():
    assert hasattr(dsl_Weapon, "directionBone")
    descriptor = None
    for klass in dsl_Weapon.__mro__:
        if "directionBone" in klass.__dict__:
            descriptor = klass.__dict__["directionBone"]
            break
    assert isinstance(descriptor, property)

def test_dsl_weapon_has_period():
    assert hasattr(dsl_Weapon, "period")
    descriptor = None
    for klass in dsl_Weapon.__mro__:
        if "period" in klass.__dict__:
            descriptor = klass.__dict__["period"]
            break
    assert isinstance(descriptor, property)



def test_dsl_model_is_not_abstract():
    assert not inspect.isabstract(dsl_Model)


def test_dsl_model_constructor_exists():
    assert callable(dsl_Model.__init__)


def test_dsl_model_constructor_args():
    sig = inspect.signature(dsl_Model.__init__)
    params = list(sig.parameters.keys())



def test_dsl_mover_is_not_abstract():
    assert not inspect.isabstract(dsl_Mover)


def test_dsl_mover_constructor_exists():
    assert callable(dsl_Mover.__init__)


def test_dsl_mover_constructor_args():
    sig = inspect.signature(dsl_Mover.__init__)
    params = list(sig.parameters.keys())
    assert "pathfindingMode" in params, "Missing parameter 'pathfindingMode'"
    assert "name" in params, "Missing parameter 'name'"
    assert "standingMode" in params, "Missing parameter 'standingMode'"
    assert "heightmap" in params, "Missing parameter 'heightmap'"

def test_dsl_mover_has_pathfindingMode():
    assert hasattr(dsl_Mover, "pathfindingMode")
    descriptor = None
    for klass in dsl_Mover.__mro__:
        if "pathfindingMode" in klass.__dict__:
            descriptor = klass.__dict__["pathfindingMode"]
            break
    assert isinstance(descriptor, property)

def test_dsl_mover_has_name():
    assert hasattr(dsl_Mover, "name")
    descriptor = None
    for klass in dsl_Mover.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dsl_mover_has_standingMode():
    assert hasattr(dsl_Mover, "standingMode")
    descriptor = None
    for klass in dsl_Mover.__mro__:
        if "standingMode" in klass.__dict__:
            descriptor = klass.__dict__["standingMode"]
            break
    assert isinstance(descriptor, property)

def test_dsl_mover_has_heightmap():
    assert hasattr(dsl_Mover, "heightmap")
    descriptor = None
    for klass in dsl_Mover.__mro__:
        if "heightmap" in klass.__dict__:
            descriptor = klass.__dict__["heightmap"]
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
Effect_strategy = st.builds(
    Effect,
)
dsl_LauncherEffect_strategy = st.builds(
    dsl_LauncherEffect,
)
dsl_DamageEffect_strategy = st.builds(
    dsl_DamageEffect,
    amount=
        st.integers()
)
dsl_PersistentEffect_strategy = st.builds(
    dsl_PersistentEffect,
    ranges=
        safe_text,
    durations=
        safe_text,
    periodCount=
        st.integers()
)
dsl_UnitWeaponLink_strategy = st.builds(
    dsl_UnitWeaponLink,
)
dsl_Color_strategy = st.builds(
    dsl_Color,
    g=
        st.integers(),
    a=
        st.integers(),
    r=
        st.integers(),
    b=
        st.integers()
)
dsl_ActorList_strategy = st.builds(
    dsl_ActorList,
    trigger=
        safe_text
)
Actor_strategy = st.builds(
    Actor,
)
dsl_ParticleActor_strategy = st.builds(
    dsl_ParticleActor,
    perSecond=
        st.integers(),
    add=
        safe_text,
    nbCol=
        st.integers(),
    duration=
        st.integers(),
    nbRow=
        st.integers(),
    emissionBone=
        safe_text,
    maxCount=
        st.integers(),
    endSize=
        safe_text,
    startSize=
        safe_text,
    directionBone=
        safe_text,
    minLife=
        safe_text,
    startVariation=
        safe_text,
    spritePath=
        safe_text,
    maxLife=
        safe_text
)
dsl_AnimtationActor_strategy = st.builds(
    dsl_AnimtationActor,
    animName=
        safe_text,
    cycle=
        safe_text,
    speed=
        safe_text
)
dsl_ModelActor_strategy = st.builds(
    dsl_ModelActor,
    modelPath=
        safe_text,
    scale=
        st.integers()
)
dsl_Projectile_strategy = st.builds(
    dsl_Projectile,
    name=
        safe_text,
    mass=
        st.integers(),
    precision=
        safe_text,
    speed=
        st.integers()
)
dsl_Turrent_strategy = st.builds(
    dsl_Turrent,
    name=
        safe_text,
    idleSpeed=
        st.integers(),
    boneName=
        safe_text,
    onIdle=
        safe_text,
    speed=
        st.integers()
)
dsl_Effect_strategy = st.builds(
    dsl_Effect,
    name=
        safe_text
)
dsl_Actor_strategy = st.builds(
    dsl_Actor,
    name=
        safe_text
)
dsl_Race_strategy = st.builds(
    dsl_Race,
    name=
        safe_text
)
dsl_Unit_strategy = st.builds(
    dsl_Unit,
    radius=
        safe_text,
    maxHealth=
        st.integers(),
    mass=
        safe_text,
    sight=
        st.integers(),
    name=
        safe_text,
    separationRadius=
        safe_text,
    speed=
        safe_text,
    uIName=
        safe_text
)
dsl_Weapon_strategy = st.builds(
    dsl_Weapon,
    uIName=
        safe_text,
    scanRange=
        st.integers(),
    range=
        safe_text,
    sourceBone=
        safe_text,
    name=
        safe_text,
    directionBone=
        safe_text,
    period=
        st.integers()
)
dsl_Model_strategy = st.builds(
    dsl_Model,
)
dsl_Mover_strategy = st.builds(
    dsl_Mover,
    pathfindingMode=
        safe_text,
    name=
        safe_text,
    standingMode=
        safe_text,
    heightmap=
        safe_text
)

@given(instance=Effect_strategy)
@settings(max_examples=50)
def test_effect_instantiation(instance):
    assert isinstance(instance, Effect)

@given(instance=dsl_LauncherEffect_strategy)
@settings(max_examples=50)
def test_dsl_launchereffect_instantiation(instance):
    assert isinstance(instance, dsl_LauncherEffect)

@given(instance=dsl_DamageEffect_strategy)
@settings(max_examples=50)
def test_dsl_damageeffect_instantiation(instance):
    assert isinstance(instance, dsl_DamageEffect)



@given(instance=dsl_DamageEffect_strategy)
def test_dsl_damageeffect_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=dsl_PersistentEffect_strategy)
@settings(max_examples=50)
def test_dsl_persistenteffect_instantiation(instance):
    assert isinstance(instance, dsl_PersistentEffect)



@given(instance=dsl_PersistentEffect_strategy)
def test_dsl_persistenteffect_ranges_setter(instance):
    original = instance.ranges
    instance.ranges = original
    assert instance.ranges == original



@given(instance=dsl_PersistentEffect_strategy)
def test_dsl_persistenteffect_durations_setter(instance):
    original = instance.durations
    instance.durations = original
    assert instance.durations == original



@given(instance=dsl_PersistentEffect_strategy)
def test_dsl_persistenteffect_periodCount_setter(instance):
    original = instance.periodCount
    instance.periodCount = original
    assert instance.periodCount == original

@given(instance=dsl_UnitWeaponLink_strategy)
@settings(max_examples=50)
def test_dsl_unitweaponlink_instantiation(instance):
    assert isinstance(instance, dsl_UnitWeaponLink)

@given(instance=dsl_Color_strategy)
@settings(max_examples=50)
def test_dsl_color_instantiation(instance):
    assert isinstance(instance, dsl_Color)



@given(instance=dsl_Color_strategy)
def test_dsl_color_g_setter(instance):
    original = instance.g
    instance.g = original
    assert instance.g == original



@given(instance=dsl_Color_strategy)
def test_dsl_color_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original



@given(instance=dsl_Color_strategy)
def test_dsl_color_r_setter(instance):
    original = instance.r
    instance.r = original
    assert instance.r == original



@given(instance=dsl_Color_strategy)
def test_dsl_color_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=dsl_ActorList_strategy)
@settings(max_examples=50)
def test_dsl_actorlist_instantiation(instance):
    assert isinstance(instance, dsl_ActorList)



@given(instance=dsl_ActorList_strategy)
def test_dsl_actorlist_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original

@given(instance=Actor_strategy)
@settings(max_examples=50)
def test_actor_instantiation(instance):
    assert isinstance(instance, Actor)

@given(instance=dsl_ParticleActor_strategy)
@settings(max_examples=50)
def test_dsl_particleactor_instantiation(instance):
    assert isinstance(instance, dsl_ParticleActor)



@given(instance=dsl_ParticleActor_strategy)
def test_dsl_particleactor_perSecond_setter(instance):
    original = instance.perSecond
    instance.perSecond = original
    assert instance.perSecond == original



@given(instance=dsl_ParticleActor_strategy)
def test_dsl_particleactor_add_setter(instance):
    original = instance.add
    instance.add = original
    assert instance.add == original



@given(instance=dsl_ParticleActor_strategy)
def test_dsl_particleactor_nbCol_setter(instance):
    original = instance.nbCol
    instance.nbCol = original
    assert instance.nbCol == original



@given(instance=dsl_ParticleActor_strategy)
def test_dsl_particleactor_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original



@given(instance=dsl_ParticleActor_strategy)
def test_dsl_particleactor_nbRow_setter(instance):
    original = instance.nbRow
    instance.nbRow = original
    assert instance.nbRow == original



@given(instance=dsl_ParticleActor_strategy)
def test_dsl_particleactor_emissionBone_setter(instance):
    original = instance.emissionBone
    instance.emissionBone = original
    assert instance.emissionBone == original



@given(instance=dsl_ParticleActor_strategy)
def test_dsl_particleactor_maxCount_setter(instance):
    original = instance.maxCount
    instance.maxCount = original
    assert instance.maxCount == original



@given(instance=dsl_ParticleActor_strategy)
def test_dsl_particleactor_endSize_setter(instance):
    original = instance.endSize
    instance.endSize = original
    assert instance.endSize == original



@given(instance=dsl_ParticleActor_strategy)
def test_dsl_particleactor_startSize_setter(instance):
    original = instance.startSize
    instance.startSize = original
    assert instance.startSize == original



@given(instance=dsl_ParticleActor_strategy)
def test_dsl_particleactor_directionBone_setter(instance):
    original = instance.directionBone
    instance.directionBone = original
    assert instance.directionBone == original



@given(instance=dsl_ParticleActor_strategy)
def test_dsl_particleactor_minLife_setter(instance):
    original = instance.minLife
    instance.minLife = original
    assert instance.minLife == original



@given(instance=dsl_ParticleActor_strategy)
def test_dsl_particleactor_startVariation_setter(instance):
    original = instance.startVariation
    instance.startVariation = original
    assert instance.startVariation == original



@given(instance=dsl_ParticleActor_strategy)
def test_dsl_particleactor_spritePath_setter(instance):
    original = instance.spritePath
    instance.spritePath = original
    assert instance.spritePath == original



@given(instance=dsl_ParticleActor_strategy)
def test_dsl_particleactor_maxLife_setter(instance):
    original = instance.maxLife
    instance.maxLife = original
    assert instance.maxLife == original

@given(instance=dsl_AnimtationActor_strategy)
@settings(max_examples=50)
def test_dsl_animtationactor_instantiation(instance):
    assert isinstance(instance, dsl_AnimtationActor)



@given(instance=dsl_AnimtationActor_strategy)
def test_dsl_animtationactor_animName_setter(instance):
    original = instance.animName
    instance.animName = original
    assert instance.animName == original



@given(instance=dsl_AnimtationActor_strategy)
def test_dsl_animtationactor_cycle_setter(instance):
    original = instance.cycle
    instance.cycle = original
    assert instance.cycle == original



@given(instance=dsl_AnimtationActor_strategy)
def test_dsl_animtationactor_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original

@given(instance=dsl_ModelActor_strategy)
@settings(max_examples=50)
def test_dsl_modelactor_instantiation(instance):
    assert isinstance(instance, dsl_ModelActor)



@given(instance=dsl_ModelActor_strategy)
def test_dsl_modelactor_modelPath_setter(instance):
    original = instance.modelPath
    instance.modelPath = original
    assert instance.modelPath == original



@given(instance=dsl_ModelActor_strategy)
def test_dsl_modelactor_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original

@given(instance=dsl_Projectile_strategy)
@settings(max_examples=50)
def test_dsl_projectile_instantiation(instance):
    assert isinstance(instance, dsl_Projectile)



@given(instance=dsl_Projectile_strategy)
def test_dsl_projectile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dsl_Projectile_strategy)
def test_dsl_projectile_mass_setter(instance):
    original = instance.mass
    instance.mass = original
    assert instance.mass == original



@given(instance=dsl_Projectile_strategy)
def test_dsl_projectile_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original



@given(instance=dsl_Projectile_strategy)
def test_dsl_projectile_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original

@given(instance=dsl_Turrent_strategy)
@settings(max_examples=50)
def test_dsl_turrent_instantiation(instance):
    assert isinstance(instance, dsl_Turrent)



@given(instance=dsl_Turrent_strategy)
def test_dsl_turrent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dsl_Turrent_strategy)
def test_dsl_turrent_idleSpeed_setter(instance):
    original = instance.idleSpeed
    instance.idleSpeed = original
    assert instance.idleSpeed == original



@given(instance=dsl_Turrent_strategy)
def test_dsl_turrent_boneName_setter(instance):
    original = instance.boneName
    instance.boneName = original
    assert instance.boneName == original



@given(instance=dsl_Turrent_strategy)
def test_dsl_turrent_onIdle_setter(instance):
    original = instance.onIdle
    instance.onIdle = original
    assert instance.onIdle == original



@given(instance=dsl_Turrent_strategy)
def test_dsl_turrent_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original

@given(instance=dsl_Effect_strategy)
@settings(max_examples=50)
def test_dsl_effect_instantiation(instance):
    assert isinstance(instance, dsl_Effect)



@given(instance=dsl_Effect_strategy)
def test_dsl_effect_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dsl_Actor_strategy)
@settings(max_examples=50)
def test_dsl_actor_instantiation(instance):
    assert isinstance(instance, dsl_Actor)



@given(instance=dsl_Actor_strategy)
def test_dsl_actor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dsl_Race_strategy)
@settings(max_examples=50)
def test_dsl_race_instantiation(instance):
    assert isinstance(instance, dsl_Race)



@given(instance=dsl_Race_strategy)
def test_dsl_race_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dsl_Unit_strategy)
@settings(max_examples=50)
def test_dsl_unit_instantiation(instance):
    assert isinstance(instance, dsl_Unit)



@given(instance=dsl_Unit_strategy)
def test_dsl_unit_radius_setter(instance):
    original = instance.radius
    instance.radius = original
    assert instance.radius == original



@given(instance=dsl_Unit_strategy)
def test_dsl_unit_maxHealth_setter(instance):
    original = instance.maxHealth
    instance.maxHealth = original
    assert instance.maxHealth == original



@given(instance=dsl_Unit_strategy)
def test_dsl_unit_mass_setter(instance):
    original = instance.mass
    instance.mass = original
    assert instance.mass == original



@given(instance=dsl_Unit_strategy)
def test_dsl_unit_sight_setter(instance):
    original = instance.sight
    instance.sight = original
    assert instance.sight == original



@given(instance=dsl_Unit_strategy)
def test_dsl_unit_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dsl_Unit_strategy)
def test_dsl_unit_separationRadius_setter(instance):
    original = instance.separationRadius
    instance.separationRadius = original
    assert instance.separationRadius == original



@given(instance=dsl_Unit_strategy)
def test_dsl_unit_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original



@given(instance=dsl_Unit_strategy)
def test_dsl_unit_uIName_setter(instance):
    original = instance.uIName
    instance.uIName = original
    assert instance.uIName == original

@given(instance=dsl_Weapon_strategy)
@settings(max_examples=50)
def test_dsl_weapon_instantiation(instance):
    assert isinstance(instance, dsl_Weapon)



@given(instance=dsl_Weapon_strategy)
def test_dsl_weapon_uIName_setter(instance):
    original = instance.uIName
    instance.uIName = original
    assert instance.uIName == original



@given(instance=dsl_Weapon_strategy)
def test_dsl_weapon_scanRange_setter(instance):
    original = instance.scanRange
    instance.scanRange = original
    assert instance.scanRange == original



@given(instance=dsl_Weapon_strategy)
def test_dsl_weapon_range_setter(instance):
    original = instance.range
    instance.range = original
    assert instance.range == original



@given(instance=dsl_Weapon_strategy)
def test_dsl_weapon_sourceBone_setter(instance):
    original = instance.sourceBone
    instance.sourceBone = original
    assert instance.sourceBone == original



@given(instance=dsl_Weapon_strategy)
def test_dsl_weapon_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dsl_Weapon_strategy)
def test_dsl_weapon_directionBone_setter(instance):
    original = instance.directionBone
    instance.directionBone = original
    assert instance.directionBone == original



@given(instance=dsl_Weapon_strategy)
def test_dsl_weapon_period_setter(instance):
    original = instance.period
    instance.period = original
    assert instance.period == original

@given(instance=dsl_Model_strategy)
@settings(max_examples=50)
def test_dsl_model_instantiation(instance):
    assert isinstance(instance, dsl_Model)

@given(instance=dsl_Mover_strategy)
@settings(max_examples=50)
def test_dsl_mover_instantiation(instance):
    assert isinstance(instance, dsl_Mover)



@given(instance=dsl_Mover_strategy)
def test_dsl_mover_pathfindingMode_setter(instance):
    original = instance.pathfindingMode
    instance.pathfindingMode = original
    assert instance.pathfindingMode == original



@given(instance=dsl_Mover_strategy)
def test_dsl_mover_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dsl_Mover_strategy)
def test_dsl_mover_standingMode_setter(instance):
    original = instance.standingMode
    instance.standingMode = original
    assert instance.standingMode == original



@given(instance=dsl_Mover_strategy)
def test_dsl_mover_heightmap_setter(instance):
    original = instance.heightmap
    instance.heightmap = original
    assert instance.heightmap == original
