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
dsl_Model = Class(name="dsl::Model")
dsl_Weapon = Class(name="dsl::Weapon")
dsl_Unit = Class(name="dsl::Unit")
dsl_Race = Class(name="dsl::Race")
dsl_Projectile = Class(name="dsl::Projectile")
dsl_ModelActor = Class(name="dsl::ModelActor")
Actor = Class(name="Actor")
dsl_ActorList = Class(name="dsl::ActorList")
dsl_ParticleActor = Class(name="dsl::ParticleActor")
dsl_Mover = Class(name="dsl::Mover")
dsl_Actor = Class(name="dsl::Actor")
dsl_Effect = Class(name="dsl::Effect")
dsl_Turrent = Class(name="dsl::Turrent")
dsl_UnitWeaponLink = Class(name="dsl::UnitWeaponLink")
dsl_Color = Class(name="dsl::Color")
dsl_AnimtationActor = Class(name="dsl::AnimtationActor")
Effect = Class(name="Effect")
dsl_DamageEffect = Class(name="dsl::DamageEffect")
dsl_LauncherEffect = Class(name="dsl::LauncherEffect")
dsl_PersistentEffect = Class(name="dsl::PersistentEffect")

# dsl_Model class attributes and methods

# dsl_Weapon class attributes and methods
dsl_Weapon_name: Property = Property(name="name", type=StringType)
dsl_Weapon_uIName: Property = Property(name="uIName", type=StringType)
dsl_Weapon_range: Property = Property(name="range", type=StringType)
dsl_Weapon_scanRange: Property = Property(name="scanRange", type=IntegerType)
dsl_Weapon_period: Property = Property(name="period", type=IntegerType)
dsl_Weapon_sourceBone: Property = Property(name="sourceBone", type=StringType)
dsl_Weapon_directionBone: Property = Property(name="directionBone", type=StringType)
dsl_Weapon.attributes={dsl_Weapon_range, dsl_Weapon_scanRange, dsl_Weapon_sourceBone, dsl_Weapon_uIName, dsl_Weapon_directionBone, dsl_Weapon_name, dsl_Weapon_period}

# dsl_Unit class attributes and methods
dsl_Unit_name: Property = Property(name="name", type=StringType)
dsl_Unit_uIName: Property = Property(name="uIName", type=StringType)
dsl_Unit_radius: Property = Property(name="radius", type=StringType)
dsl_Unit_separationRadius: Property = Property(name="separationRadius", type=StringType)
dsl_Unit_speed: Property = Property(name="speed", type=StringType)
dsl_Unit_mass: Property = Property(name="mass", type=StringType)
dsl_Unit_maxHealth: Property = Property(name="maxHealth", type=IntegerType)
dsl_Unit_sight: Property = Property(name="sight", type=IntegerType)
dsl_Unit.attributes={dsl_Unit_speed, dsl_Unit_separationRadius, dsl_Unit_uIName, dsl_Unit_mass, dsl_Unit_maxHealth, dsl_Unit_sight, dsl_Unit_radius, dsl_Unit_name}

# dsl_Race class attributes and methods
dsl_Race_name: Property = Property(name="name", type=StringType)
dsl_Race.attributes={dsl_Race_name}

# dsl_Projectile class attributes and methods
dsl_Projectile_name: Property = Property(name="name", type=StringType)
dsl_Projectile_speed: Property = Property(name="speed", type=IntegerType)
dsl_Projectile_mass: Property = Property(name="mass", type=IntegerType)
dsl_Projectile_precision: Property = Property(name="precision", type=StringType)
dsl_Projectile.attributes={dsl_Projectile_precision, dsl_Projectile_speed, dsl_Projectile_mass, dsl_Projectile_name}

# dsl_ModelActor class attributes and methods
dsl_ModelActor_modelPath: Property = Property(name="modelPath", type=StringType)
dsl_ModelActor_scale: Property = Property(name="scale", type=IntegerType)
dsl_ModelActor.attributes={dsl_ModelActor_modelPath, dsl_ModelActor_scale}

# Actor class attributes and methods

# dsl_ActorList class attributes and methods
dsl_ActorList_trigger: Property = Property(name="trigger", type=StringType)
dsl_ActorList.attributes={dsl_ActorList_trigger}

# dsl_ParticleActor class attributes and methods
dsl_ParticleActor_spritePath: Property = Property(name="spritePath", type=StringType)
dsl_ParticleActor_nbCol: Property = Property(name="nbCol", type=IntegerType)
dsl_ParticleActor_nbRow: Property = Property(name="nbRow", type=IntegerType)
dsl_ParticleActor_add: Property = Property(name="add", type=StringType)
dsl_ParticleActor_emissionBone: Property = Property(name="emissionBone", type=StringType)
dsl_ParticleActor_directionBone: Property = Property(name="directionBone", type=StringType)
dsl_ParticleActor_maxCount: Property = Property(name="maxCount", type=IntegerType)
dsl_ParticleActor_perSecond: Property = Property(name="perSecond", type=IntegerType)
dsl_ParticleActor_duration: Property = Property(name="duration", type=IntegerType)
dsl_ParticleActor_startSize: Property = Property(name="startSize", type=StringType)
dsl_ParticleActor_endSize: Property = Property(name="endSize", type=StringType)
dsl_ParticleActor_minLife: Property = Property(name="minLife", type=StringType)
dsl_ParticleActor_maxLife: Property = Property(name="maxLife", type=StringType)
dsl_ParticleActor_startVariation: Property = Property(name="startVariation", type=StringType)
dsl_ParticleActor.attributes={dsl_ParticleActor_emissionBone, dsl_ParticleActor_spritePath, dsl_ParticleActor_perSecond, dsl_ParticleActor_startSize, dsl_ParticleActor_nbRow, dsl_ParticleActor_directionBone, dsl_ParticleActor_maxLife, dsl_ParticleActor_maxCount, dsl_ParticleActor_minLife, dsl_ParticleActor_endSize, dsl_ParticleActor_nbCol, dsl_ParticleActor_add, dsl_ParticleActor_startVariation, dsl_ParticleActor_duration}

# dsl_Mover class attributes and methods
dsl_Mover_name: Property = Property(name="name", type=StringType)
dsl_Mover_pathfindingMode: Property = Property(name="pathfindingMode", type=StringType)
dsl_Mover_heightmap: Property = Property(name="heightmap", type=StringType)
dsl_Mover_standingMode: Property = Property(name="standingMode", type=StringType)
dsl_Mover.attributes={dsl_Mover_pathfindingMode, dsl_Mover_standingMode, dsl_Mover_heightmap, dsl_Mover_name}

# dsl_Actor class attributes and methods
dsl_Actor_name: Property = Property(name="name", type=StringType)
dsl_Actor.attributes={dsl_Actor_name}

# dsl_Effect class attributes and methods
dsl_Effect_name: Property = Property(name="name", type=StringType)
dsl_Effect.attributes={dsl_Effect_name}

# dsl_Turrent class attributes and methods
dsl_Turrent_name: Property = Property(name="name", type=StringType)
dsl_Turrent_speed: Property = Property(name="speed", type=IntegerType)
dsl_Turrent_idleSpeed: Property = Property(name="idleSpeed", type=IntegerType)
dsl_Turrent_onIdle: Property = Property(name="onIdle", type=StringType)
dsl_Turrent_boneName: Property = Property(name="boneName", type=StringType)
dsl_Turrent.attributes={dsl_Turrent_onIdle, dsl_Turrent_speed, dsl_Turrent_name, dsl_Turrent_idleSpeed, dsl_Turrent_boneName}

# dsl_UnitWeaponLink class attributes and methods

# dsl_Color class attributes and methods
dsl_Color_r: Property = Property(name="r", type=IntegerType)
dsl_Color_g: Property = Property(name="g", type=IntegerType)
dsl_Color_b: Property = Property(name="b", type=IntegerType)
dsl_Color_a: Property = Property(name="a", type=IntegerType)
dsl_Color.attributes={dsl_Color_b, dsl_Color_r, dsl_Color_a, dsl_Color_g}

# dsl_AnimtationActor class attributes and methods
dsl_AnimtationActor_animName: Property = Property(name="animName", type=StringType)
dsl_AnimtationActor_speed: Property = Property(name="speed", type=StringType)
dsl_AnimtationActor_cycle: Property = Property(name="cycle", type=StringType)
dsl_AnimtationActor.attributes={dsl_AnimtationActor_speed, dsl_AnimtationActor_animName, dsl_AnimtationActor_cycle}

# Effect class attributes and methods

# dsl_DamageEffect class attributes and methods
dsl_DamageEffect_amount: Property = Property(name="amount", type=IntegerType)
dsl_DamageEffect.attributes={dsl_DamageEffect_amount}

# dsl_LauncherEffect class attributes and methods

# dsl_PersistentEffect class attributes and methods
dsl_PersistentEffect_periodCount: Property = Property(name="periodCount", type=IntegerType)
dsl_PersistentEffect_durations: Property = Property(name="durations", type=StringType)
dsl_PersistentEffect_ranges: Property = Property(name="ranges", type=StringType)
dsl_PersistentEffect.attributes={dsl_PersistentEffect_ranges, dsl_PersistentEffect_durations, dsl_PersistentEffect_periodCount}

# Relationships
weapons0: BinaryAssociation = BinaryAssociation(
    name="weapons0",
    ends={
        Property(name="dsl_Weapon", type=dsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Model", type=dsl_Weapon, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
units1: BinaryAssociation = BinaryAssociation(
    name="units1",
    ends={
        Property(name="dsl_Unit", type=dsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Model2", type=dsl_Unit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
races3: BinaryAssociation = BinaryAssociation(
    name="races3",
    ends={
        Property(name="dsl_Race", type=dsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Model4", type=dsl_Race, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
projectiles13: BinaryAssociation = BinaryAssociation(
    name="projectiles13",
    ends={
        Property(name="dsl_Projectile", type=dsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Model14", type=dsl_Projectile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actorlist15: BinaryAssociation = BinaryAssociation(
    name="actorlist15",
    ends={
        Property(name="dsl_ActorList", type=dsl_ModelActor, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ModelActor", type=dsl_ActorList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
movers5: BinaryAssociation = BinaryAssociation(
    name="movers5",
    ends={
        Property(name="dsl_Mover", type=dsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Model6", type=dsl_Mover, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actors7: BinaryAssociation = BinaryAssociation(
    name="actors7",
    ends={
        Property(name="dsl_Actor", type=dsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Model8", type=dsl_Actor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
effects9: BinaryAssociation = BinaryAssociation(
    name="effects9",
    ends={
        Property(name="dsl_Effect", type=dsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Model10", type=dsl_Effect, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
turrents11: BinaryAssociation = BinaryAssociation(
    name="turrents11",
    ends={
        Property(name="dsl_Turrent", type=dsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Model12", type=dsl_Turrent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actor20: BinaryAssociation = BinaryAssociation(
    name="actor20",
    ends={
        Property(name="dsl_Actor22", type=dsl_ActorList, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ActorList21", type=dsl_Actor, multiplicity=Multiplicity(0, 1))
    }
)
race23: BinaryAssociation = BinaryAssociation(
    name="race23",
    ends={
        Property(name="dsl_Race25", type=dsl_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Unit24", type=dsl_Race, multiplicity=Multiplicity(0, 1))
    }
)
mover26: BinaryAssociation = BinaryAssociation(
    name="mover26",
    ends={
        Property(name="dsl_Mover28", type=dsl_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Unit27", type=dsl_Mover, multiplicity=Multiplicity(0, 1))
    }
)
weapons29: BinaryAssociation = BinaryAssociation(
    name="weapons29",
    ends={
        Property(name="dsl_UnitWeaponLink", type=dsl_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Unit30", type=dsl_UnitWeaponLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actor31: BinaryAssociation = BinaryAssociation(
    name="actor31",
    ends={
        Property(name="dsl_Actor33", type=dsl_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Unit32", type=dsl_Actor, multiplicity=Multiplicity(0, 1))
    }
)
startColor16: BinaryAssociation = BinaryAssociation(
    name="startColor16",
    ends={
        Property(name="dsl_Color", type=dsl_ParticleActor, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ParticleActor", type=dsl_Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
endColor17: BinaryAssociation = BinaryAssociation(
    name="endColor17",
    ends={
        Property(name="dsl_Color19", type=dsl_ParticleActor, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ParticleActor18", type=dsl_Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
effects46: BinaryAssociation = BinaryAssociation(
    name="effects46",
    ends={
        Property(name="dsl_Effect47", type=dsl_PersistentEffect, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_PersistentEffect", type=dsl_Effect, multiplicity=Multiplicity(0, 9999))
    }
)
effects48: BinaryAssociation = BinaryAssociation(
    name="effects48",
    ends={
        Property(name="dsl_Effect49", type=dsl_LauncherEffect, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_LauncherEffect", type=dsl_Effect, multiplicity=Multiplicity(0, 9999))
    }
)
projectiles50: BinaryAssociation = BinaryAssociation(
    name="projectiles50",
    ends={
        Property(name="dsl_Projectile52", type=dsl_LauncherEffect, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_LauncherEffect51", type=dsl_Projectile, multiplicity=Multiplicity(0, 9999))
    }
)
mover53: BinaryAssociation = BinaryAssociation(
    name="mover53",
    ends={
        Property(name="dsl_Mover55", type=dsl_Projectile, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Projectile54", type=dsl_Mover, multiplicity=Multiplicity(0, 1))
    }
)
actor56: BinaryAssociation = BinaryAssociation(
    name="actor56",
    ends={
        Property(name="dsl_Actor58", type=dsl_Projectile, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Projectile57", type=dsl_Actor, multiplicity=Multiplicity(0, 1))
    }
)
weapon34: BinaryAssociation = BinaryAssociation(
    name="weapon34",
    ends={
        Property(name="dsl_Weapon36", type=dsl_UnitWeaponLink, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_UnitWeaponLink35", type=dsl_Weapon, multiplicity=Multiplicity(0, 1))
    }
)
turrent37: BinaryAssociation = BinaryAssociation(
    name="turrent37",
    ends={
        Property(name="dsl_Turrent39", type=dsl_UnitWeaponLink, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_UnitWeaponLink38", type=dsl_Turrent, multiplicity=Multiplicity(0, 1))
    }
)
effect40: BinaryAssociation = BinaryAssociation(
    name="effect40",
    ends={
        Property(name="dsl_Effect42", type=dsl_Weapon, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Weapon41", type=dsl_Effect, multiplicity=Multiplicity(0, 1))
    }
)
actor43: BinaryAssociation = BinaryAssociation(
    name="actor43",
    ends={
        Property(name="dsl_Actor45", type=dsl_Weapon, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Weapon44", type=dsl_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_dsl_ModelActor_Actor = Generalization(general=Actor, specific=dsl_ModelActor)
gen_dsl_ParticleActor_Actor = Generalization(general=Actor, specific=dsl_ParticleActor)
gen_dsl_AnimtationActor_Actor = Generalization(general=Actor, specific=dsl_AnimtationActor)
gen_dsl_PersistentEffect_Effect = Generalization(general=Effect, specific=dsl_PersistentEffect)
gen_dsl_DamageEffect_Effect = Generalization(general=Effect, specific=dsl_DamageEffect)
gen_dsl_LauncherEffect_Effect = Generalization(general=Effect, specific=dsl_LauncherEffect)

# Domain Model
domain_model = DomainModel(
    name="dsl",
    types={dsl_Model, dsl_Weapon, dsl_Unit, dsl_Race, dsl_Projectile, dsl_ModelActor, Actor, dsl_ActorList, dsl_ParticleActor, dsl_Mover, dsl_Actor, dsl_Effect, dsl_Turrent, dsl_UnitWeaponLink, dsl_Color, dsl_AnimtationActor, Effect, dsl_DamageEffect, dsl_LauncherEffect, dsl_PersistentEffect},
    associations={weapons0, units1, races3, projectiles13, actorlist15, movers5, actors7, effects9, turrents11, actor20, race23, mover26, weapons29, actor31, startColor16, endColor17, effects46, effects48, projectiles50, mover53, actor56, weapon34, turrent37, effect40, actor43},
    generalizations={gen_dsl_ModelActor_Actor, gen_dsl_ParticleActor_Actor, gen_dsl_AnimtationActor_Actor, gen_dsl_PersistentEffect_Effect, gen_dsl_DamageEffect_Effect, gen_dsl_LauncherEffect_Effect},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)