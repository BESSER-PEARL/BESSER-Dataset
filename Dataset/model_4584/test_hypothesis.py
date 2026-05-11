import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Effect,
    dsl::LauncherEffect,
    dsl::DamageEffect,
    dsl::PersistentEffect,
    dsl::UnitWeaponLink,
    dsl::Color,
    dsl::ActorList,
    Actor,
    dsl::ParticleActor,
    dsl::AnimtationActor,
    dsl::ModelActor,
    dsl::Projectile,
    dsl::Turrent,
    dsl::Effect,
    dsl::Actor,
    dsl::Race,
    dsl::Unit,
    dsl::Weapon,
    dsl::Model,
    dsl::Mover,
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



def test_dsl::launchereffect_is_not_abstract():
    assert not inspect.isabstract(dsl::LauncherEffect)


def test_dsl::launchereffect_constructor_exists():
    assert callable(dsl::LauncherEffect.__init__)


def test_dsl::launchereffect_constructor_args():
    sig = inspect.signature(dsl::LauncherEffect.__init__)
    params = list(sig.parameters.keys())



def test_dsl::damageeffect_is_not_abstract():
    assert not inspect.isabstract(dsl::DamageEffect)


def test_dsl::damageeffect_constructor_exists():
    assert callable(dsl::DamageEffect.__init__)


def test_dsl::damageeffect_constructor_args():
    sig = inspect.signature(dsl::DamageEffect.__init__)
    params = list(sig.parameters.keys())
    assert "amount" in params, "Missing parameter 'amount'"

def test_dsl::damageeffect_has_amount():
    assert hasattr(dsl::DamageEffect, "amount")
    descriptor = None
    for klass in dsl::DamageEffect.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)



def test_dsl::persistenteffect_is_not_abstract():
    assert not inspect.isabstract(dsl::PersistentEffect)


def test_dsl::persistenteffect_constructor_exists():
    assert callable(dsl::PersistentEffect.__init__)


def test_dsl::persistenteffect_constructor_args():
    sig = inspect.signature(dsl::PersistentEffect.__init__)
    params = list(sig.parameters.keys())
    assert "durations" in params, "Missing parameter 'durations'"
    assert "ranges" in params, "Missing parameter 'ranges'"
    assert "periodCount" in params, "Missing parameter 'periodCount'"

def test_dsl::persistenteffect_has_durations():
    assert hasattr(dsl::PersistentEffect, "durations")
    descriptor = None
    for klass in dsl::PersistentEffect.__mro__:
        if "durations" in klass.__dict__:
            descriptor = klass.__dict__["durations"]
            break
    assert isinstance(descriptor, property)

def test_dsl::persistenteffect_has_ranges():
    assert hasattr(dsl::PersistentEffect, "ranges")
    descriptor = None
    for klass in dsl::PersistentEffect.__mro__:
        if "ranges" in klass.__dict__:
            descriptor = klass.__dict__["ranges"]
            break
    assert isinstance(descriptor, property)

def test_dsl::persistenteffect_has_periodCount():
    assert hasattr(dsl::PersistentEffect, "periodCount")
    descriptor = None
    for klass in dsl::PersistentEffect.__mro__:
        if "periodCount" in klass.__dict__:
            descriptor = klass.__dict__["periodCount"]
            break
    assert isinstance(descriptor, property)



def test_dsl::unitweaponlink_is_not_abstract():
    assert not inspect.isabstract(dsl::UnitWeaponLink)


def test_dsl::unitweaponlink_constructor_exists():
    assert callable(dsl::UnitWeaponLink.__init__)


def test_dsl::unitweaponlink_constructor_args():
    sig = inspect.signature(dsl::UnitWeaponLink.__init__)
    params = list(sig.parameters.keys())



def test_dsl::color_is_not_abstract():
    assert not inspect.isabstract(dsl::Color)


def test_dsl::color_constructor_exists():
    assert callable(dsl::Color.__init__)


def test_dsl::color_constructor_args():
    sig = inspect.signature(dsl::Color.__init__)
    params = list(sig.parameters.keys())
    assert "r" in params, "Missing parameter 'r'"
    assert "a" in params, "Missing parameter 'a'"
    assert "b" in params, "Missing parameter 'b'"
    assert "g" in params, "Missing parameter 'g'"

def test_dsl::color_has_r():
    assert hasattr(dsl::Color, "r")
    descriptor = None
    for klass in dsl::Color.__mro__:
        if "r" in klass.__dict__:
            descriptor = klass.__dict__["r"]
            break
    assert isinstance(descriptor, property)

def test_dsl::color_has_a():
    assert hasattr(dsl::Color, "a")
    descriptor = None
    for klass in dsl::Color.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
            break
    assert isinstance(descriptor, property)

def test_dsl::color_has_b():
    assert hasattr(dsl::Color, "b")
    descriptor = None
    for klass in dsl::Color.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)

def test_dsl::color_has_g():
    assert hasattr(dsl::Color, "g")
    descriptor = None
    for klass in dsl::Color.__mro__:
        if "g" in klass.__dict__:
            descriptor = klass.__dict__["g"]
            break
    assert isinstance(descriptor, property)



def test_dsl::actorlist_is_not_abstract():
    assert not inspect.isabstract(dsl::ActorList)


def test_dsl::actorlist_constructor_exists():
    assert callable(dsl::ActorList.__init__)


def test_dsl::actorlist_constructor_args():
    sig = inspect.signature(dsl::ActorList.__init__)
    params = list(sig.parameters.keys())
    assert "trigger" in params, "Missing parameter 'trigger'"

def test_dsl::actorlist_has_trigger():
    assert hasattr(dsl::ActorList, "trigger")
    descriptor = None
    for klass in dsl::ActorList.__mro__:
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



def test_dsl::particleactor_is_not_abstract():
    assert not inspect.isabstract(dsl::ParticleActor)


def test_dsl::particleactor_constructor_exists():
    assert callable(dsl::ParticleActor.__init__)


def test_dsl::particleactor_constructor_args():
    sig = inspect.signature(dsl::ParticleActor.__init__)
    params = list(sig.parameters.keys())
    assert "nbRow" in params, "Missing parameter 'nbRow'"
    assert "startSize" in params, "Missing parameter 'startSize'"
    assert "maxCount" in params, "Missing parameter 'maxCount'"
    assert "spritePath" in params, "Missing parameter 'spritePath'"
    assert "startVariation" in params, "Missing parameter 'startVariation'"
    assert "add" in params, "Missing parameter 'add'"
    assert "nbCol" in params, "Missing parameter 'nbCol'"
    assert "endSize" in params, "Missing parameter 'endSize'"
    assert "directionBone" in params, "Missing parameter 'directionBone'"
    assert "duration" in params, "Missing parameter 'duration'"
    assert "maxLife" in params, "Missing parameter 'maxLife'"
    assert "minLife" in params, "Missing parameter 'minLife'"
    assert "perSecond" in params, "Missing parameter 'perSecond'"
    assert "emissionBone" in params, "Missing parameter 'emissionBone'"

def test_dsl::particleactor_has_nbRow():
    assert hasattr(dsl::ParticleActor, "nbRow")
    descriptor = None
    for klass in dsl::ParticleActor.__mro__:
        if "nbRow" in klass.__dict__:
            descriptor = klass.__dict__["nbRow"]
            break
    assert isinstance(descriptor, property)

def test_dsl::particleactor_has_startSize():
    assert hasattr(dsl::ParticleActor, "startSize")
    descriptor = None
    for klass in dsl::ParticleActor.__mro__:
        if "startSize" in klass.__dict__:
            descriptor = klass.__dict__["startSize"]
            break
    assert isinstance(descriptor, property)

def test_dsl::particleactor_has_maxCount():
    assert hasattr(dsl::ParticleActor, "maxCount")
    descriptor = None
    for klass in dsl::ParticleActor.__mro__:
        if "maxCount" in klass.__dict__:
            descriptor = klass.__dict__["maxCount"]
            break
    assert isinstance(descriptor, property)

def test_dsl::particleactor_has_spritePath():
    assert hasattr(dsl::ParticleActor, "spritePath")
    descriptor = None
    for klass in dsl::ParticleActor.__mro__:
        if "spritePath" in klass.__dict__:
            descriptor = klass.__dict__["spritePath"]
            break
    assert isinstance(descriptor, property)

def test_dsl::particleactor_has_startVariation():
    assert hasattr(dsl::ParticleActor, "startVariation")
    descriptor = None
    for klass in dsl::ParticleActor.__mro__:
        if "startVariation" in klass.__dict__:
            descriptor = klass.__dict__["startVariation"]
            break
    assert isinstance(descriptor, property)

def test_dsl::particleactor_has_add():
    assert hasattr(dsl::ParticleActor, "add")
    descriptor = None
    for klass in dsl::ParticleActor.__mro__:
        if "add" in klass.__dict__:
            descriptor = klass.__dict__["add"]
            break
    assert isinstance(descriptor, property)

def test_dsl::particleactor_has_nbCol():
    assert hasattr(dsl::ParticleActor, "nbCol")
    descriptor = None
    for klass in dsl::ParticleActor.__mro__:
        if "nbCol" in klass.__dict__:
            descriptor = klass.__dict__["nbCol"]
            break
    assert isinstance(descriptor, property)

def test_dsl::particleactor_has_endSize():
    assert hasattr(dsl::ParticleActor, "endSize")
    descriptor = None
    for klass in dsl::ParticleActor.__mro__:
        if "endSize" in klass.__dict__:
            descriptor = klass.__dict__["endSize"]
            break
    assert isinstance(descriptor, property)

def test_dsl::particleactor_has_directionBone():
    assert hasattr(dsl::ParticleActor, "directionBone")
    descriptor = None
    for klass in dsl::ParticleActor.__mro__:
        if "directionBone" in klass.__dict__:
            descriptor = klass.__dict__["directionBone"]
            break
    assert isinstance(descriptor, property)

def test_dsl::particleactor_has_duration():
    assert hasattr(dsl::ParticleActor, "duration")
    descriptor = None
    for klass in dsl::ParticleActor.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)

def test_dsl::particleactor_has_maxLife():
    assert hasattr(dsl::ParticleActor, "maxLife")
    descriptor = None
    for klass in dsl::ParticleActor.__mro__:
        if "maxLife" in klass.__dict__:
            descriptor = klass.__dict__["maxLife"]
            break
    assert isinstance(descriptor, property)

def test_dsl::particleactor_has_minLife():
    assert hasattr(dsl::ParticleActor, "minLife")
    descriptor = None
    for klass in dsl::ParticleActor.__mro__:
        if "minLife" in klass.__dict__:
            descriptor = klass.__dict__["minLife"]
            break
    assert isinstance(descriptor, property)

def test_dsl::particleactor_has_perSecond():
    assert hasattr(dsl::ParticleActor, "perSecond")
    descriptor = None
    for klass in dsl::ParticleActor.__mro__:
        if "perSecond" in klass.__dict__:
            descriptor = klass.__dict__["perSecond"]
            break
    assert isinstance(descriptor, property)

def test_dsl::particleactor_has_emissionBone():
    assert hasattr(dsl::ParticleActor, "emissionBone")
    descriptor = None
    for klass in dsl::ParticleActor.__mro__:
        if "emissionBone" in klass.__dict__:
            descriptor = klass.__dict__["emissionBone"]
            break
    assert isinstance(descriptor, property)



def test_dsl::animtationactor_is_not_abstract():
    assert not inspect.isabstract(dsl::AnimtationActor)


def test_dsl::animtationactor_constructor_exists():
    assert callable(dsl::AnimtationActor.__init__)


def test_dsl::animtationactor_constructor_args():
    sig = inspect.signature(dsl::AnimtationActor.__init__)
    params = list(sig.parameters.keys())
    assert "animName" in params, "Missing parameter 'animName'"
    assert "cycle" in params, "Missing parameter 'cycle'"
    assert "speed" in params, "Missing parameter 'speed'"

def test_dsl::animtationactor_has_animName():
    assert hasattr(dsl::AnimtationActor, "animName")
    descriptor = None
    for klass in dsl::AnimtationActor.__mro__:
        if "animName" in klass.__dict__:
            descriptor = klass.__dict__["animName"]
            break
    assert isinstance(descriptor, property)

def test_dsl::animtationactor_has_cycle():
    assert hasattr(dsl::AnimtationActor, "cycle")
    descriptor = None
    for klass in dsl::AnimtationActor.__mro__:
        if "cycle" in klass.__dict__:
            descriptor = klass.__dict__["cycle"]
            break
    assert isinstance(descriptor, property)

def test_dsl::animtationactor_has_speed():
    assert hasattr(dsl::AnimtationActor, "speed")
    descriptor = None
    for klass in dsl::AnimtationActor.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)



def test_dsl::modelactor_is_not_abstract():
    assert not inspect.isabstract(dsl::ModelActor)


def test_dsl::modelactor_constructor_exists():
    assert callable(dsl::ModelActor.__init__)


def test_dsl::modelactor_constructor_args():
    sig = inspect.signature(dsl::ModelActor.__init__)
    params = list(sig.parameters.keys())
    assert "scale" in params, "Missing parameter 'scale'"
    assert "modelPath" in params, "Missing parameter 'modelPath'"

def test_dsl::modelactor_has_scale():
    assert hasattr(dsl::ModelActor, "scale")
    descriptor = None
    for klass in dsl::ModelActor.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)

def test_dsl::modelactor_has_modelPath():
    assert hasattr(dsl::ModelActor, "modelPath")
    descriptor = None
    for klass in dsl::ModelActor.__mro__:
        if "modelPath" in klass.__dict__:
            descriptor = klass.__dict__["modelPath"]
            break
    assert isinstance(descriptor, property)



def test_dsl::projectile_is_not_abstract():
    assert not inspect.isabstract(dsl::Projectile)


def test_dsl::projectile_constructor_exists():
    assert callable(dsl::Projectile.__init__)


def test_dsl::projectile_constructor_args():
    sig = inspect.signature(dsl::Projectile.__init__)
    params = list(sig.parameters.keys())
    assert "speed" in params, "Missing parameter 'speed'"
    assert "mass" in params, "Missing parameter 'mass'"
    assert "precision" in params, "Missing parameter 'precision'"
    assert "name" in params, "Missing parameter 'name'"

def test_dsl::projectile_has_speed():
    assert hasattr(dsl::Projectile, "speed")
    descriptor = None
    for klass in dsl::Projectile.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)

def test_dsl::projectile_has_mass():
    assert hasattr(dsl::Projectile, "mass")
    descriptor = None
    for klass in dsl::Projectile.__mro__:
        if "mass" in klass.__dict__:
            descriptor = klass.__dict__["mass"]
            break
    assert isinstance(descriptor, property)

def test_dsl::projectile_has_precision():
    assert hasattr(dsl::Projectile, "precision")
    descriptor = None
    for klass in dsl::Projectile.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)

def test_dsl::projectile_has_name():
    assert hasattr(dsl::Projectile, "name")
    descriptor = None
    for klass in dsl::Projectile.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dsl::turrent_is_not_abstract():
    assert not inspect.isabstract(dsl::Turrent)


def test_dsl::turrent_constructor_exists():
    assert callable(dsl::Turrent.__init__)


def test_dsl::turrent_constructor_args():
    sig = inspect.signature(dsl::Turrent.__init__)
    params = list(sig.parameters.keys())
    assert "onIdle" in params, "Missing parameter 'onIdle'"
    assert "boneName" in params, "Missing parameter 'boneName'"
    assert "idleSpeed" in params, "Missing parameter 'idleSpeed'"
    assert "name" in params, "Missing parameter 'name'"
    assert "speed" in params, "Missing parameter 'speed'"

def test_dsl::turrent_has_onIdle():
    assert hasattr(dsl::Turrent, "onIdle")
    descriptor = None
    for klass in dsl::Turrent.__mro__:
        if "onIdle" in klass.__dict__:
            descriptor = klass.__dict__["onIdle"]
            break
    assert isinstance(descriptor, property)

def test_dsl::turrent_has_boneName():
    assert hasattr(dsl::Turrent, "boneName")
    descriptor = None
    for klass in dsl::Turrent.__mro__:
        if "boneName" in klass.__dict__:
            descriptor = klass.__dict__["boneName"]
            break
    assert isinstance(descriptor, property)

def test_dsl::turrent_has_idleSpeed():
    assert hasattr(dsl::Turrent, "idleSpeed")
    descriptor = None
    for klass in dsl::Turrent.__mro__:
        if "idleSpeed" in klass.__dict__:
            descriptor = klass.__dict__["idleSpeed"]
            break
    assert isinstance(descriptor, property)

def test_dsl::turrent_has_name():
    assert hasattr(dsl::Turrent, "name")
    descriptor = None
    for klass in dsl::Turrent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dsl::turrent_has_speed():
    assert hasattr(dsl::Turrent, "speed")
    descriptor = None
    for klass in dsl::Turrent.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)



def test_dsl::effect_is_not_abstract():
    assert not inspect.isabstract(dsl::Effect)


def test_dsl::effect_constructor_exists():
    assert callable(dsl::Effect.__init__)


def test_dsl::effect_constructor_args():
    sig = inspect.signature(dsl::Effect.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dsl::effect_has_name():
    assert hasattr(dsl::Effect, "name")
    descriptor = None
    for klass in dsl::Effect.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dsl::actor_is_not_abstract():
    assert not inspect.isabstract(dsl::Actor)


def test_dsl::actor_constructor_exists():
    assert callable(dsl::Actor.__init__)


def test_dsl::actor_constructor_args():
    sig = inspect.signature(dsl::Actor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dsl::actor_has_name():
    assert hasattr(dsl::Actor, "name")
    descriptor = None
    for klass in dsl::Actor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dsl::race_is_not_abstract():
    assert not inspect.isabstract(dsl::Race)


def test_dsl::race_constructor_exists():
    assert callable(dsl::Race.__init__)


def test_dsl::race_constructor_args():
    sig = inspect.signature(dsl::Race.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dsl::race_has_name():
    assert hasattr(dsl::Race, "name")
    descriptor = None
    for klass in dsl::Race.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dsl::unit_is_not_abstract():
    assert not inspect.isabstract(dsl::Unit)


def test_dsl::unit_constructor_exists():
    assert callable(dsl::Unit.__init__)


def test_dsl::unit_constructor_args():
    sig = inspect.signature(dsl::Unit.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uIName" in params, "Missing parameter 'uIName'"
    assert "radius" in params, "Missing parameter 'radius'"
    assert "separationRadius" in params, "Missing parameter 'separationRadius'"
    assert "speed" in params, "Missing parameter 'speed'"
    assert "sight" in params, "Missing parameter 'sight'"
    assert "mass" in params, "Missing parameter 'mass'"
    assert "maxHealth" in params, "Missing parameter 'maxHealth'"

def test_dsl::unit_has_name():
    assert hasattr(dsl::Unit, "name")
    descriptor = None
    for klass in dsl::Unit.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dsl::unit_has_uIName():
    assert hasattr(dsl::Unit, "uIName")
    descriptor = None
    for klass in dsl::Unit.__mro__:
        if "uIName" in klass.__dict__:
            descriptor = klass.__dict__["uIName"]
            break
    assert isinstance(descriptor, property)

def test_dsl::unit_has_radius():
    assert hasattr(dsl::Unit, "radius")
    descriptor = None
    for klass in dsl::Unit.__mro__:
        if "radius" in klass.__dict__:
            descriptor = klass.__dict__["radius"]
            break
    assert isinstance(descriptor, property)

def test_dsl::unit_has_separationRadius():
    assert hasattr(dsl::Unit, "separationRadius")
    descriptor = None
    for klass in dsl::Unit.__mro__:
        if "separationRadius" in klass.__dict__:
            descriptor = klass.__dict__["separationRadius"]
            break
    assert isinstance(descriptor, property)

def test_dsl::unit_has_speed():
    assert hasattr(dsl::Unit, "speed")
    descriptor = None
    for klass in dsl::Unit.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)

def test_dsl::unit_has_sight():
    assert hasattr(dsl::Unit, "sight")
    descriptor = None
    for klass in dsl::Unit.__mro__:
        if "sight" in klass.__dict__:
            descriptor = klass.__dict__["sight"]
            break
    assert isinstance(descriptor, property)

def test_dsl::unit_has_mass():
    assert hasattr(dsl::Unit, "mass")
    descriptor = None
    for klass in dsl::Unit.__mro__:
        if "mass" in klass.__dict__:
            descriptor = klass.__dict__["mass"]
            break
    assert isinstance(descriptor, property)

def test_dsl::unit_has_maxHealth():
    assert hasattr(dsl::Unit, "maxHealth")
    descriptor = None
    for klass in dsl::Unit.__mro__:
        if "maxHealth" in klass.__dict__:
            descriptor = klass.__dict__["maxHealth"]
            break
    assert isinstance(descriptor, property)



def test_dsl::weapon_is_not_abstract():
    assert not inspect.isabstract(dsl::Weapon)


def test_dsl::weapon_constructor_exists():
    assert callable(dsl::Weapon.__init__)


def test_dsl::weapon_constructor_args():
    sig = inspect.signature(dsl::Weapon.__init__)
    params = list(sig.parameters.keys())
    assert "period" in params, "Missing parameter 'period'"
    assert "name" in params, "Missing parameter 'name'"
    assert "range" in params, "Missing parameter 'range'"
    assert "directionBone" in params, "Missing parameter 'directionBone'"
    assert "sourceBone" in params, "Missing parameter 'sourceBone'"
    assert "scanRange" in params, "Missing parameter 'scanRange'"
    assert "uIName" in params, "Missing parameter 'uIName'"

def test_dsl::weapon_has_period():
    assert hasattr(dsl::Weapon, "period")
    descriptor = None
    for klass in dsl::Weapon.__mro__:
        if "period" in klass.__dict__:
            descriptor = klass.__dict__["period"]
            break
    assert isinstance(descriptor, property)

def test_dsl::weapon_has_name():
    assert hasattr(dsl::Weapon, "name")
    descriptor = None
    for klass in dsl::Weapon.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dsl::weapon_has_range():
    assert hasattr(dsl::Weapon, "range")
    descriptor = None
    for klass in dsl::Weapon.__mro__:
        if "range" in klass.__dict__:
            descriptor = klass.__dict__["range"]
            break
    assert isinstance(descriptor, property)

def test_dsl::weapon_has_directionBone():
    assert hasattr(dsl::Weapon, "directionBone")
    descriptor = None
    for klass in dsl::Weapon.__mro__:
        if "directionBone" in klass.__dict__:
            descriptor = klass.__dict__["directionBone"]
            break
    assert isinstance(descriptor, property)

def test_dsl::weapon_has_sourceBone():
    assert hasattr(dsl::Weapon, "sourceBone")
    descriptor = None
    for klass in dsl::Weapon.__mro__:
        if "sourceBone" in klass.__dict__:
            descriptor = klass.__dict__["sourceBone"]
            break
    assert isinstance(descriptor, property)

def test_dsl::weapon_has_scanRange():
    assert hasattr(dsl::Weapon, "scanRange")
    descriptor = None
    for klass in dsl::Weapon.__mro__:
        if "scanRange" in klass.__dict__:
            descriptor = klass.__dict__["scanRange"]
            break
    assert isinstance(descriptor, property)

def test_dsl::weapon_has_uIName():
    assert hasattr(dsl::Weapon, "uIName")
    descriptor = None
    for klass in dsl::Weapon.__mro__:
        if "uIName" in klass.__dict__:
            descriptor = klass.__dict__["uIName"]
            break
    assert isinstance(descriptor, property)



def test_dsl::model_is_not_abstract():
    assert not inspect.isabstract(dsl::Model)


def test_dsl::model_constructor_exists():
    assert callable(dsl::Model.__init__)


def test_dsl::model_constructor_args():
    sig = inspect.signature(dsl::Model.__init__)
    params = list(sig.parameters.keys())



def test_dsl::mover_is_not_abstract():
    assert not inspect.isabstract(dsl::Mover)


def test_dsl::mover_constructor_exists():
    assert callable(dsl::Mover.__init__)


def test_dsl::mover_constructor_args():
    sig = inspect.signature(dsl::Mover.__init__)
    params = list(sig.parameters.keys())
    assert "heightmap" in params, "Missing parameter 'heightmap'"
    assert "name" in params, "Missing parameter 'name'"
    assert "standingMode" in params, "Missing parameter 'standingMode'"
    assert "pathfindingMode" in params, "Missing parameter 'pathfindingMode'"

def test_dsl::mover_has_heightmap():
    assert hasattr(dsl::Mover, "heightmap")
    descriptor = None
    for klass in dsl::Mover.__mro__:
        if "heightmap" in klass.__dict__:
            descriptor = klass.__dict__["heightmap"]
            break
    assert isinstance(descriptor, property)

def test_dsl::mover_has_name():
    assert hasattr(dsl::Mover, "name")
    descriptor = None
    for klass in dsl::Mover.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dsl::mover_has_standingMode():
    assert hasattr(dsl::Mover, "standingMode")
    descriptor = None
    for klass in dsl::Mover.__mro__:
        if "standingMode" in klass.__dict__:
            descriptor = klass.__dict__["standingMode"]
            break
    assert isinstance(descriptor, property)

def test_dsl::mover_has_pathfindingMode():
    assert hasattr(dsl::Mover, "pathfindingMode")
    descriptor = None
    for klass in dsl::Mover.__mro__:
        if "pathfindingMode" in klass.__dict__:
            descriptor = klass.__dict__["pathfindingMode"]
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
dsl::LauncherEffect_strategy = st.builds(
    dsl::LauncherEffect,
)
dsl::DamageEffect_strategy = st.builds(
    dsl::DamageEffect,
    amount=
        st.integers()
)
dsl::PersistentEffect_strategy = st.builds(
    dsl::PersistentEffect,
    durations=
        safe_text,
    ranges=
        safe_text,
    periodCount=
        st.integers()
)
dsl::UnitWeaponLink_strategy = st.builds(
    dsl::UnitWeaponLink,
)
dsl::Color_strategy = st.builds(
    dsl::Color,
    r=
        st.integers(),
    a=
        st.integers(),
    b=
        st.integers(),
    g=
        st.integers()
)
dsl::ActorList_strategy = st.builds(
    dsl::ActorList,
    trigger=
        safe_text
)
Actor_strategy = st.builds(
    Actor,
)
dsl::ParticleActor_strategy = st.builds(
    dsl::ParticleActor,
    nbRow=
        st.integers(),
    startSize=
        safe_text,
    maxCount=
        st.integers(),
    spritePath=
        safe_text,
    startVariation=
        safe_text,
    add=
        safe_text,
    nbCol=
        st.integers(),
    endSize=
        safe_text,
    directionBone=
        safe_text,
    duration=
        st.integers(),
    maxLife=
        safe_text,
    minLife=
        safe_text,
    perSecond=
        st.integers(),
    emissionBone=
        safe_text
)
dsl::AnimtationActor_strategy = st.builds(
    dsl::AnimtationActor,
    animName=
        safe_text,
    cycle=
        safe_text,
    speed=
        safe_text
)
dsl::ModelActor_strategy = st.builds(
    dsl::ModelActor,
    scale=
        st.integers(),
    modelPath=
        safe_text
)
dsl::Projectile_strategy = st.builds(
    dsl::Projectile,
    speed=
        st.integers(),
    mass=
        st.integers(),
    precision=
        safe_text,
    name=
        safe_text
)
dsl::Turrent_strategy = st.builds(
    dsl::Turrent,
    onIdle=
        safe_text,
    boneName=
        safe_text,
    idleSpeed=
        st.integers(),
    name=
        safe_text,
    speed=
        st.integers()
)
dsl::Effect_strategy = st.builds(
    dsl::Effect,
    name=
        safe_text
)
dsl::Actor_strategy = st.builds(
    dsl::Actor,
    name=
        safe_text
)
dsl::Race_strategy = st.builds(
    dsl::Race,
    name=
        safe_text
)
dsl::Unit_strategy = st.builds(
    dsl::Unit,
    name=
        safe_text,
    uIName=
        safe_text,
    radius=
        safe_text,
    separationRadius=
        safe_text,
    speed=
        safe_text,
    sight=
        st.integers(),
    mass=
        safe_text,
    maxHealth=
        st.integers()
)
dsl::Weapon_strategy = st.builds(
    dsl::Weapon,
    period=
        st.integers(),
    name=
        safe_text,
    range=
        safe_text,
    directionBone=
        safe_text,
    sourceBone=
        safe_text,
    scanRange=
        st.integers(),
    uIName=
        safe_text
)
dsl::Model_strategy = st.builds(
    dsl::Model,
)
dsl::Mover_strategy = st.builds(
    dsl::Mover,
    heightmap=
        safe_text,
    name=
        safe_text,
    standingMode=
        safe_text,
    pathfindingMode=
        safe_text
)

@given(instance=Effect_strategy)
@settings(max_examples=50)
def test_effect_instantiation(instance):
    assert isinstance(instance, Effect)

@given(instance=dsl::LauncherEffect_strategy)
@settings(max_examples=50)
def test_dsl::launchereffect_instantiation(instance):
    assert isinstance(instance, dsl::LauncherEffect)

@given(instance=dsl::DamageEffect_strategy)
@settings(max_examples=50)
def test_dsl::damageeffect_instantiation(instance):
    assert isinstance(instance, dsl::DamageEffect)

@given(instance=dsl::DamageEffect_strategy)
def test_dsl::damageeffect_amount_type(instance):
    assert isinstance(instance.amount, int)


@given(instance=dsl::DamageEffect_strategy)
def test_dsl::damageeffect_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=dsl::PersistentEffect_strategy)
@settings(max_examples=50)
def test_dsl::persistenteffect_instantiation(instance):
    assert isinstance(instance, dsl::PersistentEffect)

@given(instance=dsl::PersistentEffect_strategy)
def test_dsl::persistenteffect_durations_type(instance):
    assert isinstance(instance.durations, str)


@given(instance=dsl::PersistentEffect_strategy)
def test_dsl::persistenteffect_durations_setter(instance):
    original = instance.durations
    instance.durations = original
    assert instance.durations == original

@given(instance=dsl::PersistentEffect_strategy)
def test_dsl::persistenteffect_ranges_type(instance):
    assert isinstance(instance.ranges, str)


@given(instance=dsl::PersistentEffect_strategy)
def test_dsl::persistenteffect_ranges_setter(instance):
    original = instance.ranges
    instance.ranges = original
    assert instance.ranges == original

@given(instance=dsl::PersistentEffect_strategy)
def test_dsl::persistenteffect_periodCount_type(instance):
    assert isinstance(instance.periodCount, int)


@given(instance=dsl::PersistentEffect_strategy)
def test_dsl::persistenteffect_periodCount_setter(instance):
    original = instance.periodCount
    instance.periodCount = original
    assert instance.periodCount == original

@given(instance=dsl::UnitWeaponLink_strategy)
@settings(max_examples=50)
def test_dsl::unitweaponlink_instantiation(instance):
    assert isinstance(instance, dsl::UnitWeaponLink)

@given(instance=dsl::Color_strategy)
@settings(max_examples=50)
def test_dsl::color_instantiation(instance):
    assert isinstance(instance, dsl::Color)

@given(instance=dsl::Color_strategy)
def test_dsl::color_r_type(instance):
    assert isinstance(instance.r, int)


@given(instance=dsl::Color_strategy)
def test_dsl::color_r_setter(instance):
    original = instance.r
    instance.r = original
    assert instance.r == original

@given(instance=dsl::Color_strategy)
def test_dsl::color_a_type(instance):
    assert isinstance(instance.a, int)


@given(instance=dsl::Color_strategy)
def test_dsl::color_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original

@given(instance=dsl::Color_strategy)
def test_dsl::color_b_type(instance):
    assert isinstance(instance.b, int)


@given(instance=dsl::Color_strategy)
def test_dsl::color_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=dsl::Color_strategy)
def test_dsl::color_g_type(instance):
    assert isinstance(instance.g, int)


@given(instance=dsl::Color_strategy)
def test_dsl::color_g_setter(instance):
    original = instance.g
    instance.g = original
    assert instance.g == original

@given(instance=dsl::ActorList_strategy)
@settings(max_examples=50)
def test_dsl::actorlist_instantiation(instance):
    assert isinstance(instance, dsl::ActorList)

@given(instance=dsl::ActorList_strategy)
def test_dsl::actorlist_trigger_type(instance):
    assert isinstance(instance.trigger, str)


@given(instance=dsl::ActorList_strategy)
def test_dsl::actorlist_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original

@given(instance=Actor_strategy)
@settings(max_examples=50)
def test_actor_instantiation(instance):
    assert isinstance(instance, Actor)

@given(instance=dsl::ParticleActor_strategy)
@settings(max_examples=50)
def test_dsl::particleactor_instantiation(instance):
    assert isinstance(instance, dsl::ParticleActor)

@given(instance=dsl::ParticleActor_strategy)
def test_dsl::particleactor_nbRow_type(instance):
    assert isinstance(instance.nbRow, int)


@given(instance=dsl::ParticleActor_strategy)
def test_dsl::particleactor_nbRow_setter(instance):
    original = instance.nbRow
    instance.nbRow = original
    assert instance.nbRow == original

@given(instance=dsl::ParticleActor_strategy)
def test_dsl::particleactor_startSize_type(instance):
    assert isinstance(instance.startSize, str)


@given(instance=dsl::ParticleActor_strategy)
def test_dsl::particleactor_startSize_setter(instance):
    original = instance.startSize
    instance.startSize = original
    assert instance.startSize == original

@given(instance=dsl::ParticleActor_strategy)
def test_dsl::particleactor_maxCount_type(instance):
    assert isinstance(instance.maxCount, int)


@given(instance=dsl::ParticleActor_strategy)
def test_dsl::particleactor_maxCount_setter(instance):
    original = instance.maxCount
    instance.maxCount = original
    assert instance.maxCount == original

@given(instance=dsl::ParticleActor_strategy)
def test_dsl::particleactor_spritePath_type(instance):
    assert isinstance(instance.spritePath, str)


@given(instance=dsl::ParticleActor_strategy)
def test_dsl::particleactor_spritePath_setter(instance):
    original = instance.spritePath
    instance.spritePath = original
    assert instance.spritePath == original

@given(instance=dsl::ParticleActor_strategy)
def test_dsl::particleactor_startVariation_type(instance):
    assert isinstance(instance.startVariation, str)


@given(instance=dsl::ParticleActor_strategy)
def test_dsl::particleactor_startVariation_setter(instance):
    original = instance.startVariation
    instance.startVariation = original
    assert instance.startVariation == original

@given(instance=dsl::ParticleActor_strategy)
def test_dsl::particleactor_add_type(instance):
    assert isinstance(instance.add, str)


@given(instance=dsl::ParticleActor_strategy)
def test_dsl::particleactor_add_setter(instance):
    original = instance.add
    instance.add = original
    assert instance.add == original

@given(instance=dsl::ParticleActor_strategy)
def test_dsl::particleactor_nbCol_type(instance):
    assert isinstance(instance.nbCol, int)


@given(instance=dsl::ParticleActor_strategy)
def test_dsl::particleactor_nbCol_setter(instance):
    original = instance.nbCol
    instance.nbCol = original
    assert instance.nbCol == original

@given(instance=dsl::ParticleActor_strategy)
def test_dsl::particleactor_endSize_type(instance):
    assert isinstance(instance.endSize, str)


@given(instance=dsl::ParticleActor_strategy)
def test_dsl::particleactor_endSize_setter(instance):
    original = instance.endSize
    instance.endSize = original
    assert instance.endSize == original

@given(instance=dsl::ParticleActor_strategy)
def test_dsl::particleactor_directionBone_type(instance):
    assert isinstance(instance.directionBone, str)


@given(instance=dsl::ParticleActor_strategy)
def test_dsl::particleactor_directionBone_setter(instance):
    original = instance.directionBone
    instance.directionBone = original
    assert instance.directionBone == original

@given(instance=dsl::ParticleActor_strategy)
def test_dsl::particleactor_duration_type(instance):
    assert isinstance(instance.duration, int)


@given(instance=dsl::ParticleActor_strategy)
def test_dsl::particleactor_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=dsl::ParticleActor_strategy)
def test_dsl::particleactor_maxLife_type(instance):
    assert isinstance(instance.maxLife, str)


@given(instance=dsl::ParticleActor_strategy)
def test_dsl::particleactor_maxLife_setter(instance):
    original = instance.maxLife
    instance.maxLife = original
    assert instance.maxLife == original

@given(instance=dsl::ParticleActor_strategy)
def test_dsl::particleactor_minLife_type(instance):
    assert isinstance(instance.minLife, str)


@given(instance=dsl::ParticleActor_strategy)
def test_dsl::particleactor_minLife_setter(instance):
    original = instance.minLife
    instance.minLife = original
    assert instance.minLife == original

@given(instance=dsl::ParticleActor_strategy)
def test_dsl::particleactor_perSecond_type(instance):
    assert isinstance(instance.perSecond, int)


@given(instance=dsl::ParticleActor_strategy)
def test_dsl::particleactor_perSecond_setter(instance):
    original = instance.perSecond
    instance.perSecond = original
    assert instance.perSecond == original

@given(instance=dsl::ParticleActor_strategy)
def test_dsl::particleactor_emissionBone_type(instance):
    assert isinstance(instance.emissionBone, str)


@given(instance=dsl::ParticleActor_strategy)
def test_dsl::particleactor_emissionBone_setter(instance):
    original = instance.emissionBone
    instance.emissionBone = original
    assert instance.emissionBone == original

@given(instance=dsl::AnimtationActor_strategy)
@settings(max_examples=50)
def test_dsl::animtationactor_instantiation(instance):
    assert isinstance(instance, dsl::AnimtationActor)

@given(instance=dsl::AnimtationActor_strategy)
def test_dsl::animtationactor_animName_type(instance):
    assert isinstance(instance.animName, str)


@given(instance=dsl::AnimtationActor_strategy)
def test_dsl::animtationactor_animName_setter(instance):
    original = instance.animName
    instance.animName = original
    assert instance.animName == original

@given(instance=dsl::AnimtationActor_strategy)
def test_dsl::animtationactor_cycle_type(instance):
    assert isinstance(instance.cycle, str)


@given(instance=dsl::AnimtationActor_strategy)
def test_dsl::animtationactor_cycle_setter(instance):
    original = instance.cycle
    instance.cycle = original
    assert instance.cycle == original

@given(instance=dsl::AnimtationActor_strategy)
def test_dsl::animtationactor_speed_type(instance):
    assert isinstance(instance.speed, str)


@given(instance=dsl::AnimtationActor_strategy)
def test_dsl::animtationactor_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original

@given(instance=dsl::ModelActor_strategy)
@settings(max_examples=50)
def test_dsl::modelactor_instantiation(instance):
    assert isinstance(instance, dsl::ModelActor)

@given(instance=dsl::ModelActor_strategy)
def test_dsl::modelactor_scale_type(instance):
    assert isinstance(instance.scale, int)


@given(instance=dsl::ModelActor_strategy)
def test_dsl::modelactor_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original

@given(instance=dsl::ModelActor_strategy)
def test_dsl::modelactor_modelPath_type(instance):
    assert isinstance(instance.modelPath, str)


@given(instance=dsl::ModelActor_strategy)
def test_dsl::modelactor_modelPath_setter(instance):
    original = instance.modelPath
    instance.modelPath = original
    assert instance.modelPath == original

@given(instance=dsl::Projectile_strategy)
@settings(max_examples=50)
def test_dsl::projectile_instantiation(instance):
    assert isinstance(instance, dsl::Projectile)

@given(instance=dsl::Projectile_strategy)
def test_dsl::projectile_speed_type(instance):
    assert isinstance(instance.speed, int)


@given(instance=dsl::Projectile_strategy)
def test_dsl::projectile_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original

@given(instance=dsl::Projectile_strategy)
def test_dsl::projectile_mass_type(instance):
    assert isinstance(instance.mass, int)


@given(instance=dsl::Projectile_strategy)
def test_dsl::projectile_mass_setter(instance):
    original = instance.mass
    instance.mass = original
    assert instance.mass == original

@given(instance=dsl::Projectile_strategy)
def test_dsl::projectile_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=dsl::Projectile_strategy)
def test_dsl::projectile_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=dsl::Projectile_strategy)
def test_dsl::projectile_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dsl::Projectile_strategy)
def test_dsl::projectile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dsl::Turrent_strategy)
@settings(max_examples=50)
def test_dsl::turrent_instantiation(instance):
    assert isinstance(instance, dsl::Turrent)

@given(instance=dsl::Turrent_strategy)
def test_dsl::turrent_onIdle_type(instance):
    assert isinstance(instance.onIdle, str)


@given(instance=dsl::Turrent_strategy)
def test_dsl::turrent_onIdle_setter(instance):
    original = instance.onIdle
    instance.onIdle = original
    assert instance.onIdle == original

@given(instance=dsl::Turrent_strategy)
def test_dsl::turrent_boneName_type(instance):
    assert isinstance(instance.boneName, str)


@given(instance=dsl::Turrent_strategy)
def test_dsl::turrent_boneName_setter(instance):
    original = instance.boneName
    instance.boneName = original
    assert instance.boneName == original

@given(instance=dsl::Turrent_strategy)
def test_dsl::turrent_idleSpeed_type(instance):
    assert isinstance(instance.idleSpeed, int)


@given(instance=dsl::Turrent_strategy)
def test_dsl::turrent_idleSpeed_setter(instance):
    original = instance.idleSpeed
    instance.idleSpeed = original
    assert instance.idleSpeed == original

@given(instance=dsl::Turrent_strategy)
def test_dsl::turrent_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dsl::Turrent_strategy)
def test_dsl::turrent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dsl::Turrent_strategy)
def test_dsl::turrent_speed_type(instance):
    assert isinstance(instance.speed, int)


@given(instance=dsl::Turrent_strategy)
def test_dsl::turrent_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original

@given(instance=dsl::Effect_strategy)
@settings(max_examples=50)
def test_dsl::effect_instantiation(instance):
    assert isinstance(instance, dsl::Effect)

@given(instance=dsl::Effect_strategy)
def test_dsl::effect_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dsl::Effect_strategy)
def test_dsl::effect_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dsl::Actor_strategy)
@settings(max_examples=50)
def test_dsl::actor_instantiation(instance):
    assert isinstance(instance, dsl::Actor)

@given(instance=dsl::Actor_strategy)
def test_dsl::actor_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dsl::Actor_strategy)
def test_dsl::actor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dsl::Race_strategy)
@settings(max_examples=50)
def test_dsl::race_instantiation(instance):
    assert isinstance(instance, dsl::Race)

@given(instance=dsl::Race_strategy)
def test_dsl::race_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dsl::Race_strategy)
def test_dsl::race_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dsl::Unit_strategy)
@settings(max_examples=50)
def test_dsl::unit_instantiation(instance):
    assert isinstance(instance, dsl::Unit)

@given(instance=dsl::Unit_strategy)
def test_dsl::unit_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dsl::Unit_strategy)
def test_dsl::unit_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dsl::Unit_strategy)
def test_dsl::unit_uIName_type(instance):
    assert isinstance(instance.uIName, str)


@given(instance=dsl::Unit_strategy)
def test_dsl::unit_uIName_setter(instance):
    original = instance.uIName
    instance.uIName = original
    assert instance.uIName == original

@given(instance=dsl::Unit_strategy)
def test_dsl::unit_radius_type(instance):
    assert isinstance(instance.radius, str)


@given(instance=dsl::Unit_strategy)
def test_dsl::unit_radius_setter(instance):
    original = instance.radius
    instance.radius = original
    assert instance.radius == original

@given(instance=dsl::Unit_strategy)
def test_dsl::unit_separationRadius_type(instance):
    assert isinstance(instance.separationRadius, str)


@given(instance=dsl::Unit_strategy)
def test_dsl::unit_separationRadius_setter(instance):
    original = instance.separationRadius
    instance.separationRadius = original
    assert instance.separationRadius == original

@given(instance=dsl::Unit_strategy)
def test_dsl::unit_speed_type(instance):
    assert isinstance(instance.speed, str)


@given(instance=dsl::Unit_strategy)
def test_dsl::unit_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original

@given(instance=dsl::Unit_strategy)
def test_dsl::unit_sight_type(instance):
    assert isinstance(instance.sight, int)


@given(instance=dsl::Unit_strategy)
def test_dsl::unit_sight_setter(instance):
    original = instance.sight
    instance.sight = original
    assert instance.sight == original

@given(instance=dsl::Unit_strategy)
def test_dsl::unit_mass_type(instance):
    assert isinstance(instance.mass, str)


@given(instance=dsl::Unit_strategy)
def test_dsl::unit_mass_setter(instance):
    original = instance.mass
    instance.mass = original
    assert instance.mass == original

@given(instance=dsl::Unit_strategy)
def test_dsl::unit_maxHealth_type(instance):
    assert isinstance(instance.maxHealth, int)


@given(instance=dsl::Unit_strategy)
def test_dsl::unit_maxHealth_setter(instance):
    original = instance.maxHealth
    instance.maxHealth = original
    assert instance.maxHealth == original

@given(instance=dsl::Weapon_strategy)
@settings(max_examples=50)
def test_dsl::weapon_instantiation(instance):
    assert isinstance(instance, dsl::Weapon)

@given(instance=dsl::Weapon_strategy)
def test_dsl::weapon_period_type(instance):
    assert isinstance(instance.period, int)


@given(instance=dsl::Weapon_strategy)
def test_dsl::weapon_period_setter(instance):
    original = instance.period
    instance.period = original
    assert instance.period == original

@given(instance=dsl::Weapon_strategy)
def test_dsl::weapon_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dsl::Weapon_strategy)
def test_dsl::weapon_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dsl::Weapon_strategy)
def test_dsl::weapon_range_type(instance):
    assert isinstance(instance.range, str)


@given(instance=dsl::Weapon_strategy)
def test_dsl::weapon_range_setter(instance):
    original = instance.range
    instance.range = original
    assert instance.range == original

@given(instance=dsl::Weapon_strategy)
def test_dsl::weapon_directionBone_type(instance):
    assert isinstance(instance.directionBone, str)


@given(instance=dsl::Weapon_strategy)
def test_dsl::weapon_directionBone_setter(instance):
    original = instance.directionBone
    instance.directionBone = original
    assert instance.directionBone == original

@given(instance=dsl::Weapon_strategy)
def test_dsl::weapon_sourceBone_type(instance):
    assert isinstance(instance.sourceBone, str)


@given(instance=dsl::Weapon_strategy)
def test_dsl::weapon_sourceBone_setter(instance):
    original = instance.sourceBone
    instance.sourceBone = original
    assert instance.sourceBone == original

@given(instance=dsl::Weapon_strategy)
def test_dsl::weapon_scanRange_type(instance):
    assert isinstance(instance.scanRange, int)


@given(instance=dsl::Weapon_strategy)
def test_dsl::weapon_scanRange_setter(instance):
    original = instance.scanRange
    instance.scanRange = original
    assert instance.scanRange == original

@given(instance=dsl::Weapon_strategy)
def test_dsl::weapon_uIName_type(instance):
    assert isinstance(instance.uIName, str)


@given(instance=dsl::Weapon_strategy)
def test_dsl::weapon_uIName_setter(instance):
    original = instance.uIName
    instance.uIName = original
    assert instance.uIName == original

@given(instance=dsl::Model_strategy)
@settings(max_examples=50)
def test_dsl::model_instantiation(instance):
    assert isinstance(instance, dsl::Model)

@given(instance=dsl::Mover_strategy)
@settings(max_examples=50)
def test_dsl::mover_instantiation(instance):
    assert isinstance(instance, dsl::Mover)

@given(instance=dsl::Mover_strategy)
def test_dsl::mover_heightmap_type(instance):
    assert isinstance(instance.heightmap, str)


@given(instance=dsl::Mover_strategy)
def test_dsl::mover_heightmap_setter(instance):
    original = instance.heightmap
    instance.heightmap = original
    assert instance.heightmap == original

@given(instance=dsl::Mover_strategy)
def test_dsl::mover_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dsl::Mover_strategy)
def test_dsl::mover_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dsl::Mover_strategy)
def test_dsl::mover_standingMode_type(instance):
    assert isinstance(instance.standingMode, str)


@given(instance=dsl::Mover_strategy)
def test_dsl::mover_standingMode_setter(instance):
    original = instance.standingMode
    instance.standingMode = original
    assert instance.standingMode == original

@given(instance=dsl::Mover_strategy)
def test_dsl::mover_pathfindingMode_type(instance):
    assert isinstance(instance.pathfindingMode, str)


@given(instance=dsl::Mover_strategy)
def test_dsl::mover_pathfindingMode_setter(instance):
    original = instance.pathfindingMode
    instance.pathfindingMode = original
    assert instance.pathfindingMode == original
