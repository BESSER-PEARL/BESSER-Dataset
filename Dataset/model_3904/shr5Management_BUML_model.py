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
GeneratorState: Enumeration = Enumeration(
    name="GeneratorState",
    literals={
            EnumerationLiteral(name="new"),
			EnumerationLiteral(name="readyForCreation"),
			EnumerationLiteral(name="commited"),
			EnumerationLiteral(name="personaCreated")
    }
)

Sex: Enumeration = Enumeration(
    name="Sex",
    literals={
            EnumerationLiteral(name="female"),
			EnumerationLiteral(name="male"),
			EnumerationLiteral(name="undefinde"),
			EnumerationLiteral(name="none")
    }
)

QuellenConstrainType: Enumeration = Enumeration(
    name="QuellenConstrainType",
    literals={
            EnumerationLiteral(name="notTogether"),
			EnumerationLiteral(name="needOneOf")
    }
)

LifeModuleType: Enumeration = Enumeration(
    name="LifeModuleType",
    literals={
            EnumerationLiteral(name="nationality"),
			EnumerationLiteral(name="formativeYears"),
			EnumerationLiteral(name="teenYears"),
			EnumerationLiteral(name="furtherEducation"),
			EnumerationLiteral(name="realLife")
    }
)

# Classes
shr5Management_ManagedCharacter = Class(name="shr5Management::ManagedCharacter", is_abstract=True)
shr5Management_AbstraktPersona = Class(name="shr5Management::AbstraktPersona")
shr5Management_Changes = Class(name="shr5Management::Changes", is_abstract=True)
shr5Management_CharacterGeneratorSystem = Class(name="shr5Management::CharacterGeneratorSystem", is_abstract=True)
Beschreibbar = Class(name="Beschreibbar")
Quelle = Class(name="Quelle")
shr5Management_GeneratorStateToEStringMapEntry = Class(name="shr5Management::GeneratorStateToEStringMapEntry")
shr5Management_LifestyleToStartMoney = Class(name="shr5Management::LifestyleToStartMoney")
shr5Management_CharacterAdvancementSystem = Class(name="shr5Management::CharacterAdvancementSystem")
shr5Management_QuellenConstrain = Class(name="shr5Management::QuellenConstrain")
shr5Management_AbstraktGegenstand = Class(name="shr5Management::AbstraktGegenstand")
shr5Management_Vertrag = Class(name="shr5Management::Vertrag")
shr5Management_Connection = Class(name="shr5Management::Connection")
shr5Management_Fahrzeug = Class(name="shr5Management::Fahrzeug")
shr5Management_Lifestyle = Class(name="shr5Management::Lifestyle")
shr5Management_Sprachfertigkeit = Class(name="shr5Management::Sprachfertigkeit")
shr5Management_KarmaGaint = Class(name="shr5Management::KarmaGaint")
Changes = Class(name="Changes")
shr5Management_FreeStyle = Class(name="shr5Management::FreeStyle")
shr5Management_Shr5System = Class(name="shr5Management::Shr5System")
PrioritySystem = Class(name="PrioritySystem")
shr5Management_PrioritySystem = Class(name="shr5Management::PrioritySystem", is_abstract=True)
CharacterGeneratorSystem = Class(name="CharacterGeneratorSystem")
shr5Management_PriorityCategorie = Class(name="shr5Management::PriorityCategorie", is_abstract=True)
shr5Management_NonPlayerCharacter = Class(name="shr5Management::NonPlayerCharacter")
ManagedCharacter = Class(name="ManagedCharacter")
shr5Management_Spezies = Class(name="shr5Management::Spezies")
shr5Management_Attributes = Class(name="shr5Management::Attributes")
shr5Management_Skill = Class(name="shr5Management::Skill")
shr5Management_Resourcen = Class(name="shr5Management::Resourcen")
shr5Management_SpecialType = Class(name="shr5Management::SpecialType", is_abstract=True)
shr5Management_Fertigkeit = Class(name="shr5Management::Fertigkeit")
shr5Management_FertigkeitsGruppe = Class(name="shr5Management::FertigkeitsGruppe")
shr5Management_Technomancer = Class(name="shr5Management::Technomancer")
SpecialType = Class(name="SpecialType")
shr5Management_EClass = Class(name="shr5Management::EClass")
shr5Management_MetaType = Class(name="shr5Management::MetaType")
PriorityCategorie = Class(name="PriorityCategorie")
shr5Management_CharacterGroup = Class(name="shr5Management::CharacterGroup")
shr5Management_FreeStyleGenerator = Class(name="shr5Management::FreeStyleGenerator")
shr5Management_Shr5Generator = Class(name="shr5Management::Shr5Generator")
shr5Management_Spellcaster = Class(name="shr5Management::Spellcaster")
Adept = Class(name="Adept")
shr5Management_Adept = Class(name="shr5Management::Adept")
shr5Management_CharacterGenerator = Class(name="shr5Management::CharacterGenerator", is_abstract=True)
shr5Management_AttributeChange = Class(name="shr5Management::AttributeChange")
PersonaValueChange = Class(name="PersonaValueChange")
shr5Management_EAttribute = Class(name="shr5Management::EAttribute")
shr5Management_PlayerCharacter = Class(name="shr5Management::PlayerCharacter")
shr5Management_CharacterDiary = Class(name="shr5Management::CharacterDiary")
shr5Management_Mudan = Class(name="shr5Management::Mudan")
shr5Management_PersonaChange = Class(name="shr5Management::PersonaChange")
shr5Management_Erlernbar = Class(name="shr5Management::Erlernbar")
shr5Management_PersonaValueChange = Class(name="shr5Management::PersonaValueChange", is_abstract=True)
shr5Management_Advancement = Class(name="shr5Management::Advancement", is_abstract=True)
shr5Management_IncreaseCharacterPart = Class(name="shr5Management::IncreaseCharacterPart")
shr5Management_GruntGroup = Class(name="shr5Management::GruntGroup")
shr5Management_GruntMembers = Class(name="shr5Management::GruntMembers")
PlayerManagement = Class(name="PlayerManagement")
shr5Management_SourceBook = Class(name="shr5Management::SourceBook")
shr5Management_Shr5RuleGenerator = Class(name="shr5Management::Shr5RuleGenerator", is_abstract=True)
shr5Management_KarmaGenerator = Class(name="shr5Management::KarmaGenerator", is_abstract=True)
shr5Management_PlayerManagement = Class(name="shr5Management::PlayerManagement")
shr5Management_GamemasterManagement = Class(name="shr5Management::GamemasterManagement")
shr5Management_Pack = Class(name="shr5Management::Pack")
GeldWert = Class(name="GeldWert")
shr5Management_DiaryEntry = Class(name="shr5Management::DiaryEntry")
shr5Management_Quelle = Class(name="shr5Management::Quelle")
shr5Management_LifeModulesSystem = Class(name="shr5Management::LifeModulesSystem")
Shr5System = Class(name="Shr5System")
shr5Management_ModuleChange = Class(name="shr5Management::ModuleChange", is_abstract=True)
shr5Management_ContractPayment = Class(name="shr5Management::ContractPayment")
DiaryEntry = Class(name="DiaryEntry")
shr5Management_CharacterChange = Class(name="shr5Management::CharacterChange")
shr5Management_SumToTenGenerator = Class(name="shr5Management::SumToTenGenerator")
Shr5Generator = Class(name="Shr5Generator")
shr5Management_LifeModulesGenerator = Class(name="shr5Management::LifeModulesGenerator")
shr5Management_LifeModule = Class(name="shr5Management::LifeModule")
shr5Management_Shr5KarmaGenerator = Class(name="shr5Management::Shr5KarmaGenerator")
shr5Management_TrainingRate = Class(name="shr5Management::TrainingRate")
RangeTableEntry = Class(name="RangeTableEntry")
shr5Management_RangeTableEntry = Class(name="shr5Management::RangeTableEntry", is_abstract=True)
shr5Management_RangeTable = Class(name="shr5Management::RangeTable", is_abstract=True)
shr5Management_ModuleSkillChange = Class(name="shr5Management::ModuleSkillChange")
shr5Management_ModuleTeachableChange = Class(name="shr5Management::ModuleTeachableChange")
shr5Management_ModuleAttributeChange = Class(name="shr5Management::ModuleAttributeChange")
shr5Management_ModuleFeatureChange = Class(name="shr5Management::ModuleFeatureChange")
ModuleChange = Class(name="ModuleChange")
shr5Management_EReference = Class(name="shr5Management::EReference")
shr5Management_EObject = Class(name="shr5Management::EObject")
shr5Management_ModuleSkillGroupChange = Class(name="shr5Management::ModuleSkillGroupChange")
shr5Management_ModuleTypeChange = Class(name="shr5Management::ModuleTypeChange", is_abstract=True)
shr5Management_TrainingsTime = Class(name="shr5Management::TrainingsTime")
CharacterChange = Class(name="CharacterChange")
shr5Management_TrainingRange = Class(name="shr5Management::TrainingRange")
shr5Management_PersonaMartialArtChange = Class(name="shr5Management::PersonaMartialArtChange")
PersonaChange = Class(name="PersonaChange")
shr5Management_MartialartStyle = Class(name="shr5Management::MartialartStyle")
shr5Management_MartialartTechnique = Class(name="shr5Management::MartialartTechnique")

# shr5Management_ManagedCharacter class attributes and methods
shr5Management_ManagedCharacter_sex: Property = Property(name="sex", type=StringType)
shr5Management_ManagedCharacter_streetCred: Property = Property(name="streetCred", type=IntegerType)
shr5Management_ManagedCharacter_notoriety: Property = Property(name="notoriety", type=IntegerType)
shr5Management_ManagedCharacter_notorietyBasic: Property = Property(name="notorietyBasic", type=IntegerType)
shr5Management_ManagedCharacter_publicAwareness: Property = Property(name="publicAwareness", type=IntegerType)
shr5Management_ManagedCharacter_karmaGaint: Property = Property(name="karmaGaint", type=IntegerType)
shr5Management_ManagedCharacter_currentKarma: Property = Property(name="currentKarma", type=IntegerType)
shr5Management_ManagedCharacter_height: Property = Property(name="height", type=IntegerType)
shr5Management_ManagedCharacter_dateofbirth: Property = Property(name="dateofbirth", type=StringType)
shr5Management_ManagedCharacter_weight: Property = Property(name="weight", type=IntegerType)
shr5Management_ManagedCharacter.attributes={shr5Management_ManagedCharacter_publicAwareness, shr5Management_ManagedCharacter_weight, shr5Management_ManagedCharacter_notoriety, shr5Management_ManagedCharacter_sex, shr5Management_ManagedCharacter_height, shr5Management_ManagedCharacter_karmaGaint, shr5Management_ManagedCharacter_streetCred, shr5Management_ManagedCharacter_dateofbirth, shr5Management_ManagedCharacter_notorietyBasic, shr5Management_ManagedCharacter_currentKarma}

# shr5Management_AbstraktPersona class attributes and methods

# shr5Management_Changes class attributes and methods
shr5Management_Changes_changeApplied: Property = Property(name="changeApplied", type=BooleanType)
shr5Management_Changes_dateApplied: Property = Property(name="dateApplied", type=StringType)
shr5Management_Changes_date: Property = Property(name="date", type=StringType)
shr5Management_Changes_karmaCost: Property = Property(name="karmaCost", type=IntegerType)
shr5Management_Changes_m_applyChanges: Method = Method(name="applyChanges", parameters={})
shr5Management_Changes.attributes={shr5Management_Changes_date, shr5Management_Changes_changeApplied, shr5Management_Changes_dateApplied, shr5Management_Changes_karmaCost}
shr5Management_Changes.methods={shr5Management_Changes_m_applyChanges}

# shr5Management_CharacterGeneratorSystem class attributes and methods

# Beschreibbar class attributes and methods

# Quelle class attributes and methods

# shr5Management_GeneratorStateToEStringMapEntry class attributes and methods
shr5Management_GeneratorStateToEStringMapEntry_key: Property = Property(name="key", type=StringType)
shr5Management_GeneratorStateToEStringMapEntry_value: Property = Property(name="value", type=StringType)
shr5Management_GeneratorStateToEStringMapEntry.attributes={shr5Management_GeneratorStateToEStringMapEntry_key, shr5Management_GeneratorStateToEStringMapEntry_value}

# shr5Management_LifestyleToStartMoney class attributes and methods
shr5Management_LifestyleToStartMoney_numberOfW: Property = Property(name="numberOfW", type=IntegerType)
shr5Management_LifestyleToStartMoney_moneyFactor: Property = Property(name="moneyFactor", type=IntegerType)
shr5Management_LifestyleToStartMoney.attributes={shr5Management_LifestyleToStartMoney_numberOfW, shr5Management_LifestyleToStartMoney_moneyFactor}

# shr5Management_CharacterAdvancementSystem class attributes and methods

# shr5Management_QuellenConstrain class attributes and methods
shr5Management_QuellenConstrain_constrainType: Property = Property(name="constrainType", type=StringType)
shr5Management_QuellenConstrain.attributes={shr5Management_QuellenConstrain_constrainType}

# shr5Management_AbstraktGegenstand class attributes and methods

# shr5Management_Vertrag class attributes and methods

# shr5Management_Connection class attributes and methods
shr5Management_Connection_influence: Property = Property(name="influence", type=IntegerType)
shr5Management_Connection_loyality: Property = Property(name="loyality", type=IntegerType)
shr5Management_Connection.attributes={shr5Management_Connection_loyality, shr5Management_Connection_influence}

# shr5Management_Fahrzeug class attributes and methods

# shr5Management_Lifestyle class attributes and methods

# shr5Management_Sprachfertigkeit class attributes and methods

# shr5Management_KarmaGaint class attributes and methods
shr5Management_KarmaGaint_karma: Property = Property(name="karma", type=IntegerType)
shr5Management_KarmaGaint.attributes={shr5Management_KarmaGaint_karma}

# Changes class attributes and methods

# shr5Management_FreeStyle class attributes and methods

# shr5Management_Shr5System class attributes and methods
shr5Management_Shr5System_karmaToResourceFactor: Property = Property(name="karmaToResourceFactor", type=IntegerType)
shr5Management_Shr5System_karmaToMagicFactor: Property = Property(name="karmaToMagicFactor", type=IntegerType)
shr5Management_Shr5System_numberOfMaxAttributes: Property = Property(name="numberOfMaxAttributes", type=IntegerType)
shr5Management_Shr5System_knowlegeSkillFactor: Property = Property(name="knowlegeSkillFactor", type=IntegerType)
shr5Management_Shr5System_charismaToConnectionFactor: Property = Property(name="charismaToConnectionFactor", type=IntegerType)
shr5Management_Shr5System_maxResourceToKeep: Property = Property(name="maxResourceToKeep", type=IntegerType)
shr5Management_Shr5System_maxKarmaToResources: Property = Property(name="maxKarmaToResources", type=IntegerType)
shr5Management_Shr5System_maxKarmaToKeep: Property = Property(name="maxKarmaToKeep", type=IntegerType)
shr5Management_Shr5System_skillMax: Property = Property(name="skillMax", type=IntegerType)
shr5Management_Shr5System_numberOfSpecalism: Property = Property(name="numberOfSpecalism", type=IntegerType)
shr5Management_Shr5System_karmaToConnectionFactor: Property = Property(name="karmaToConnectionFactor", type=IntegerType)
shr5Management_Shr5System_boundSprititServiceCost: Property = Property(name="boundSprititServiceCost", type=IntegerType)
shr5Management_Shr5System_maxConnectionRating: Property = Property(name="maxConnectionRating", type=IntegerType)
shr5Management_Shr5System_freeMartialArtTechniques: Property = Property(name="freeMartialArtTechniques", type=IntegerType)
shr5Management_Shr5System_maxMartialArtStyles: Property = Property(name="maxMartialArtStyles", type=IntegerType)
shr5Management_Shr5System_sumToTenValue: Property = Property(name="sumToTenValue", type=IntegerType)
shr5Management_Shr5System.attributes={shr5Management_Shr5System_charismaToConnectionFactor, shr5Management_Shr5System_maxResourceToKeep, shr5Management_Shr5System_maxConnectionRating, shr5Management_Shr5System_numberOfSpecalism, shr5Management_Shr5System_numberOfMaxAttributes, shr5Management_Shr5System_maxKarmaToKeep, shr5Management_Shr5System_freeMartialArtTechniques, shr5Management_Shr5System_maxMartialArtStyles, shr5Management_Shr5System_maxKarmaToResources, shr5Management_Shr5System_boundSprititServiceCost, shr5Management_Shr5System_karmaToConnectionFactor, shr5Management_Shr5System_knowlegeSkillFactor, shr5Management_Shr5System_karmaToMagicFactor, shr5Management_Shr5System_sumToTenValue, shr5Management_Shr5System_skillMax, shr5Management_Shr5System_karmaToResourceFactor}

# PrioritySystem class attributes and methods

# shr5Management_PrioritySystem class attributes and methods
shr5Management_PrioritySystem_karmaPoints: Property = Property(name="karmaPoints", type=IntegerType)
shr5Management_PrioritySystem.attributes={shr5Management_PrioritySystem_karmaPoints}

# CharacterGeneratorSystem class attributes and methods

# shr5Management_PriorityCategorie class attributes and methods
shr5Management_PriorityCategorie_categorieName: Property = Property(name="categorieName", type=StringType)
shr5Management_PriorityCategorie_cost: Property = Property(name="cost", type=IntegerType)
shr5Management_PriorityCategorie.attributes={shr5Management_PriorityCategorie_cost, shr5Management_PriorityCategorie_categorieName}

# shr5Management_NonPlayerCharacter class attributes and methods

# ManagedCharacter class attributes and methods

# shr5Management_Spezies class attributes and methods

# shr5Management_Attributes class attributes and methods
shr5Management_Attributes_attibutePoints: Property = Property(name="attibutePoints", type=IntegerType)
shr5Management_Attributes_m_calcAttributesSpend: Method = Method(name="calcAttributesSpend", parameters={Parameter(name='context')}, type=IntegerType)
shr5Management_Attributes.attributes={shr5Management_Attributes_attibutePoints}
shr5Management_Attributes.methods={shr5Management_Attributes_m_calcAttributesSpend}

# shr5Management_Skill class attributes and methods
shr5Management_Skill_skillPoints: Property = Property(name="skillPoints", type=IntegerType)
shr5Management_Skill_groupPoints: Property = Property(name="groupPoints", type=IntegerType)
shr5Management_Skill_m_calcSkillSpend: Method = Method(name="calcSkillSpend", parameters={Parameter(name='context')}, type=IntegerType)
shr5Management_Skill_m_calcGroupSpend: Method = Method(name="calcGroupSpend", parameters={Parameter(name='context')}, type=IntegerType)
shr5Management_Skill_m_calcKnowledgeSkillSpend: Method = Method(name="calcKnowledgeSkillSpend", parameters={Parameter(name='context')}, type=IntegerType)
shr5Management_Skill_m_calcKnowledgeSkillPoints: Method = Method(name="calcKnowledgeSkillPoints", parameters={Parameter(name='context')}, type=IntegerType)
shr5Management_Skill.attributes={shr5Management_Skill_groupPoints, shr5Management_Skill_skillPoints}
shr5Management_Skill.methods={shr5Management_Skill_m_calcSkillSpend, shr5Management_Skill_m_calcGroupSpend, shr5Management_Skill_m_calcKnowledgeSkillPoints, shr5Management_Skill_m_calcKnowledgeSkillSpend}

# shr5Management_Resourcen class attributes and methods
shr5Management_Resourcen_resource: Property = Property(name="resource", type=IntegerType)
shr5Management_Resourcen_m_calcResourceSpend: Method = Method(name="calcResourceSpend", parameters={Parameter(name='context')}, type=IntegerType)
shr5Management_Resourcen.attributes={shr5Management_Resourcen_resource}
shr5Management_Resourcen.methods={shr5Management_Resourcen_m_calcResourceSpend}

# shr5Management_SpecialType class attributes and methods
shr5Management_SpecialType_skillValue: Property = Property(name="skillValue", type=IntegerType)
shr5Management_SpecialType_skillNumber: Property = Property(name="skillNumber", type=IntegerType)
shr5Management_SpecialType_m_calcSkillsSpend: Method = Method(name="calcSkillsSpend", parameters={Parameter(name='context')}, type=IntegerType)
shr5Management_SpecialType.attributes={shr5Management_SpecialType_skillNumber, shr5Management_SpecialType_skillValue}
shr5Management_SpecialType.methods={shr5Management_SpecialType_m_calcSkillsSpend}

# shr5Management_Fertigkeit class attributes and methods

# shr5Management_FertigkeitsGruppe class attributes and methods

# shr5Management_Technomancer class attributes and methods
shr5Management_Technomancer_resonanz: Property = Property(name="resonanz", type=IntegerType)
shr5Management_Technomancer_complexForms: Property = Property(name="complexForms", type=IntegerType)
shr5Management_Technomancer_m_calcComplexFormsSpend: Method = Method(name="calcComplexFormsSpend", parameters={Parameter(name='context')}, type=IntegerType)
shr5Management_Technomancer.attributes={shr5Management_Technomancer_resonanz, shr5Management_Technomancer_complexForms}
shr5Management_Technomancer.methods={shr5Management_Technomancer_m_calcComplexFormsSpend}

# SpecialType class attributes and methods

# shr5Management_EClass class attributes and methods

# shr5Management_MetaType class attributes and methods
shr5Management_MetaType_specialPoints: Property = Property(name="specialPoints", type=IntegerType)
shr5Management_MetaType_m_calcSpecialPointsSpend: Method = Method(name="calcSpecialPointsSpend", parameters={Parameter(name='context')}, type=IntegerType)
shr5Management_MetaType.attributes={shr5Management_MetaType_specialPoints}
shr5Management_MetaType.methods={shr5Management_MetaType_m_calcSpecialPointsSpend}

# PriorityCategorie class attributes and methods

# shr5Management_CharacterGroup class attributes and methods

# shr5Management_FreeStyleGenerator class attributes and methods

# shr5Management_Shr5Generator class attributes and methods
shr5Management_Shr5Generator_karmaToResource: Property = Property(name="karmaToResource", type=IntegerType)
shr5Management_Shr5Generator_karmaSpend: Property = Property(name="karmaSpend", type=IntegerType)
shr5Management_Shr5Generator_attributeSpend: Property = Property(name="attributeSpend", type=IntegerType)
shr5Management_Shr5Generator_resourceSpend: Property = Property(name="resourceSpend", type=IntegerType)
shr5Management_Shr5Generator_connectionSpend: Property = Property(name="connectionSpend", type=IntegerType)
shr5Management_Shr5Generator_skillPointSpend: Property = Property(name="skillPointSpend", type=IntegerType)
shr5Management_Shr5Generator_specialPointSpend: Property = Property(name="specialPointSpend", type=IntegerType)
shr5Management_Shr5Generator_groupPointSpend: Property = Property(name="groupPointSpend", type=IntegerType)
shr5Management_Shr5Generator_knownlegePointSpend: Property = Property(name="knownlegePointSpend", type=IntegerType)
shr5Management_Shr5Generator_spellPointSpend: Property = Property(name="spellPointSpend", type=IntegerType)
shr5Management_Shr5Generator_startKarma: Property = Property(name="startKarma", type=IntegerType)
shr5Management_Shr5Generator_startResources: Property = Property(name="startResources", type=IntegerType)
shr5Management_Shr5Generator_m_hasCategoryOnlyOnce: Method = Method(name="hasCategoryOnlyOnce", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
shr5Management_Shr5Generator_m_hasNotMoreMaxAttributes: Method = Method(name="hasNotMoreMaxAttributes", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
shr5Management_Shr5Generator_m_hasSpendAllConnectionPoints: Method = Method(name="hasSpendAllConnectionPoints", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
shr5Management_Shr5Generator_m_hasSpendAllResourcePoints: Method = Method(name="hasSpendAllResourcePoints", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
shr5Management_Shr5Generator_m_hasSpendAllMagicSkillsPoints: Method = Method(name="hasSpendAllMagicSkillsPoints", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
shr5Management_Shr5Generator_m_hasSpendAllMagicPoints: Method = Method(name="hasSpendAllMagicPoints", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
shr5Management_Shr5Generator_m_hasSpendAllGroupPoints: Method = Method(name="hasSpendAllGroupPoints", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
shr5Management_Shr5Generator_m_hasSpendAllKnowlegeSkillPoints: Method = Method(name="hasSpendAllKnowlegeSkillPoints", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
shr5Management_Shr5Generator_m_hasSpendAllKarmaPoints: Method = Method(name="hasSpendAllKarmaPoints", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
shr5Management_Shr5Generator_m_hasSpendAllSpellPoints: Method = Method(name="hasSpendAllSpellPoints", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
shr5Management_Shr5Generator_m_hasSpendAllPowerPoints: Method = Method(name="hasSpendAllPowerPoints", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
shr5Management_Shr5Generator_m_hasSpendAllAttributesPoints: Method = Method(name="hasSpendAllAttributesPoints", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
shr5Management_Shr5Generator_m_hasSpendAllSkillPoints: Method = Method(name="hasSpendAllSkillPoints", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
shr5Management_Shr5Generator_m_hasSpendAllSpecialPoints: Method = Method(name="hasSpendAllSpecialPoints", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
shr5Management_Shr5Generator_m_hasSpendAllSpecialTypePoints: Method = Method(name="hasSpendAllSpecialTypePoints", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
shr5Management_Shr5Generator.attributes={shr5Management_Shr5Generator_attributeSpend, shr5Management_Shr5Generator_knownlegePointSpend, shr5Management_Shr5Generator_karmaToResource, shr5Management_Shr5Generator_spellPointSpend, shr5Management_Shr5Generator_startResources, shr5Management_Shr5Generator_resourceSpend, shr5Management_Shr5Generator_specialPointSpend, shr5Management_Shr5Generator_karmaSpend, shr5Management_Shr5Generator_groupPointSpend, shr5Management_Shr5Generator_startKarma, shr5Management_Shr5Generator_skillPointSpend, shr5Management_Shr5Generator_connectionSpend}
shr5Management_Shr5Generator.methods={shr5Management_Shr5Generator_m_hasSpendAllAttributesPoints, shr5Management_Shr5Generator_m_hasSpendAllConnectionPoints, shr5Management_Shr5Generator_m_hasSpendAllSkillPoints, shr5Management_Shr5Generator_m_hasSpendAllSpecialPoints, shr5Management_Shr5Generator_m_hasSpendAllSpellPoints, shr5Management_Shr5Generator_m_hasSpendAllResourcePoints, shr5Management_Shr5Generator_m_hasSpendAllSpecialTypePoints, shr5Management_Shr5Generator_m_hasSpendAllMagicPoints, shr5Management_Shr5Generator_m_hasCategoryOnlyOnce, shr5Management_Shr5Generator_m_hasSpendAllGroupPoints, shr5Management_Shr5Generator_m_hasNotMoreMaxAttributes, shr5Management_Shr5Generator_m_hasSpendAllKnowlegeSkillPoints, shr5Management_Shr5Generator_m_hasSpendAllKarmaPoints, shr5Management_Shr5Generator_m_hasSpendAllMagicSkillsPoints, shr5Management_Shr5Generator_m_hasSpendAllPowerPoints}

# shr5Management_Spellcaster class attributes and methods
shr5Management_Spellcaster_spellPoints: Property = Property(name="spellPoints", type=IntegerType)
shr5Management_Spellcaster_m_calcSpellPointsSpend: Method = Method(name="calcSpellPointsSpend", parameters={Parameter(name='context')}, type=IntegerType)
shr5Management_Spellcaster.attributes={shr5Management_Spellcaster_spellPoints}
shr5Management_Spellcaster.methods={shr5Management_Spellcaster_m_calcSpellPointsSpend}

# Adept class attributes and methods

# shr5Management_Adept class attributes and methods
shr5Management_Adept_magic: Property = Property(name="magic", type=IntegerType)
shr5Management_Adept_m_calcPowerPointsSpend: Method = Method(name="calcPowerPointsSpend", parameters={Parameter(name='context')}, type=IntegerType)
shr5Management_Adept.attributes={shr5Management_Adept_magic}
shr5Management_Adept.methods={shr5Management_Adept_m_calcPowerPointsSpend}

# shr5Management_CharacterGenerator class attributes and methods
shr5Management_CharacterGenerator_state: Property = Property(name="state", type=StringType)
shr5Management_CharacterGenerator_characterName: Property = Property(name="characterName", type=StringType)
shr5Management_CharacterGenerator_currentInstruction: Property = Property(name="currentInstruction", type=StringType)
shr5Management_CharacterGenerator.attributes={shr5Management_CharacterGenerator_characterName, shr5Management_CharacterGenerator_currentInstruction, shr5Management_CharacterGenerator_state}

# shr5Management_AttributeChange class attributes and methods

# PersonaValueChange class attributes and methods

# shr5Management_EAttribute class attributes and methods

# shr5Management_PlayerCharacter class attributes and methods
shr5Management_PlayerCharacter_age: Property = Property(name="age", type=IntegerType)
shr5Management_PlayerCharacter.attributes={shr5Management_PlayerCharacter_age}

# shr5Management_CharacterDiary class attributes and methods
shr5Management_CharacterDiary_characterDate: Property = Property(name="characterDate", type=StringType)
shr5Management_CharacterDiary.attributes={shr5Management_CharacterDiary_characterDate}

# shr5Management_Mudan class attributes and methods

# shr5Management_PersonaChange class attributes and methods

# shr5Management_Erlernbar class attributes and methods

# shr5Management_PersonaValueChange class attributes and methods
shr5Management_PersonaValueChange_from: Property = Property(name="from", type=IntegerType)
shr5Management_PersonaValueChange_to: Property = Property(name="to", type=IntegerType)
shr5Management_PersonaValueChange.attributes={shr5Management_PersonaValueChange_from, shr5Management_PersonaValueChange_to}

# shr5Management_Advancement class attributes and methods
shr5Management_Advancement_karmaFactor: Property = Property(name="karmaFactor", type=IntegerType)
shr5Management_Advancement.attributes={shr5Management_Advancement_karmaFactor}

# shr5Management_IncreaseCharacterPart class attributes and methods

# shr5Management_GruntGroup class attributes and methods
shr5Management_GruntGroup_professionalRating: Property = Property(name="professionalRating", type=IntegerType)
shr5Management_GruntGroup.attributes={shr5Management_GruntGroup_professionalRating}

# shr5Management_GruntMembers class attributes and methods
shr5Management_GruntMembers_count: Property = Property(name="count", type=IntegerType)
shr5Management_GruntMembers.attributes={shr5Management_GruntMembers_count}

# PlayerManagement class attributes and methods

# shr5Management_SourceBook class attributes and methods

# shr5Management_Shr5RuleGenerator class attributes and methods
shr5Management_Shr5RuleGenerator_m_hasBasicViolations: Method = Method(name="hasBasicViolations", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
shr5Management_Shr5RuleGenerator_m_hasSpendAllPoints: Method = Method(name="hasSpendAllPoints", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
shr5Management_Shr5RuleGenerator_m_hasNotMoreMaxAttributes: Method = Method(name="hasNotMoreMaxAttributes", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
shr5Management_Shr5RuleGenerator_m_hasNoSkillsOverMax: Method = Method(name="hasNoSkillsOverMax", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
shr5Management_Shr5RuleGenerator_m_hasNotMoreSpecalism: Method = Method(name="hasNotMoreSpecalism", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
shr5Management_Shr5RuleGenerator_m_hasNoAttributesOverSpeciesAtt: Method = Method(name="hasNoAttributesOverSpeciesAtt", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
shr5Management_Shr5RuleGenerator_m_hasNoConstrainVoilation: Method = Method(name="hasNoConstrainVoilation", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
shr5Management_Shr5RuleGenerator_m_hasLifestyleChoosen: Method = Method(name="hasLifestyleChoosen", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
shr5Management_Shr5RuleGenerator_m_hasOnlyAllowedSources: Method = Method(name="hasOnlyAllowedSources", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
shr5Management_Shr5RuleGenerator_m_hasKiPowerOverLimit: Method = Method(name="hasKiPowerOverLimit", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
shr5Management_Shr5RuleGenerator.methods={shr5Management_Shr5RuleGenerator_m_hasOnlyAllowedSources, shr5Management_Shr5RuleGenerator_m_hasKiPowerOverLimit, shr5Management_Shr5RuleGenerator_m_hasLifestyleChoosen, shr5Management_Shr5RuleGenerator_m_hasSpendAllPoints, shr5Management_Shr5RuleGenerator_m_hasBasicViolations, shr5Management_Shr5RuleGenerator_m_hasNotMoreMaxAttributes, shr5Management_Shr5RuleGenerator_m_hasNoConstrainVoilation, shr5Management_Shr5RuleGenerator_m_hasNoAttributesOverSpeciesAtt, shr5Management_Shr5RuleGenerator_m_hasNotMoreSpecalism, shr5Management_Shr5RuleGenerator_m_hasNoSkillsOverMax}

# shr5Management_KarmaGenerator class attributes and methods
shr5Management_KarmaGenerator_karmaToResource: Property = Property(name="karmaToResource", type=IntegerType)
shr5Management_KarmaGenerator_karmaSpend: Property = Property(name="karmaSpend", type=IntegerType)
shr5Management_KarmaGenerator_resourceSpend: Property = Property(name="resourceSpend", type=IntegerType)
shr5Management_KarmaGenerator_startKarma: Property = Property(name="startKarma", type=IntegerType)
shr5Management_KarmaGenerator_startResources: Property = Property(name="startResources", type=IntegerType)
shr5Management_KarmaGenerator_choiseKarmaCost: Property = Property(name="choiseKarmaCost", type=IntegerType)
shr5Management_KarmaGenerator_m_hasSpendAllKarmaPoints: Method = Method(name="hasSpendAllKarmaPoints", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
shr5Management_KarmaGenerator_m_hasSpendAllResources: Method = Method(name="hasSpendAllResources", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
shr5Management_KarmaGenerator.attributes={shr5Management_KarmaGenerator_karmaSpend, shr5Management_KarmaGenerator_karmaToResource, shr5Management_KarmaGenerator_startResources, shr5Management_KarmaGenerator_resourceSpend, shr5Management_KarmaGenerator_choiseKarmaCost, shr5Management_KarmaGenerator_startKarma}
shr5Management_KarmaGenerator.methods={shr5Management_KarmaGenerator_m_hasSpendAllKarmaPoints, shr5Management_KarmaGenerator_m_hasSpendAllResources}

# shr5Management_PlayerManagement class attributes and methods

# shr5Management_GamemasterManagement class attributes and methods

# shr5Management_Pack class attributes and methods

# GeldWert class attributes and methods

# shr5Management_DiaryEntry class attributes and methods
shr5Management_DiaryEntry_date: Property = Property(name="date", type=StringType)
shr5Management_DiaryEntry_message: Property = Property(name="message", type=StringType)
shr5Management_DiaryEntry.attributes={shr5Management_DiaryEntry_date, shr5Management_DiaryEntry_message}

# shr5Management_Quelle class attributes and methods

# shr5Management_LifeModulesSystem class attributes and methods
shr5Management_LifeModulesSystem_knowlegeSkillMax: Property = Property(name="knowlegeSkillMax", type=IntegerType)
shr5Management_LifeModulesSystem.attributes={shr5Management_LifeModulesSystem_knowlegeSkillMax}

# Shr5System class attributes and methods

# shr5Management_ModuleChange class attributes and methods

# shr5Management_ContractPayment class attributes and methods
shr5Management_ContractPayment_payed: Property = Property(name="payed", type=BooleanType)
shr5Management_ContractPayment.attributes={shr5Management_ContractPayment_payed}

# DiaryEntry class attributes and methods

# shr5Management_CharacterChange class attributes and methods

# shr5Management_SumToTenGenerator class attributes and methods
shr5Management_SumToTenGenerator_m_hasSumToTen: Method = Method(name="hasSumToTen", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
shr5Management_SumToTenGenerator.methods={shr5Management_SumToTenGenerator_m_hasSumToTen}

# Shr5Generator class attributes and methods

# shr5Management_LifeModulesGenerator class attributes and methods
shr5Management_LifeModulesGenerator_moduleKarmaCost: Property = Property(name="moduleKarmaCost", type=IntegerType)
shr5Management_LifeModulesGenerator_startingAge: Property = Property(name="startingAge", type=IntegerType)
shr5Management_LifeModulesGenerator.attributes={shr5Management_LifeModulesGenerator_startingAge, shr5Management_LifeModulesGenerator_moduleKarmaCost}

# shr5Management_LifeModule class attributes and methods
shr5Management_LifeModule_karmaCost: Property = Property(name="karmaCost", type=IntegerType)
shr5Management_LifeModule_moduleType: Property = Property(name="moduleType", type=StringType)
shr5Management_LifeModule_time: Property = Property(name="time", type=IntegerType)
shr5Management_LifeModule.attributes={shr5Management_LifeModule_time, shr5Management_LifeModule_moduleType, shr5Management_LifeModule_karmaCost}

# shr5Management_Shr5KarmaGenerator class attributes and methods

# shr5Management_TrainingRate class attributes and methods
shr5Management_TrainingRate_factor: Property = Property(name="factor", type=IntegerType)
shr5Management_TrainingRate_timeUnit: Property = Property(name="timeUnit", type=StringType)
shr5Management_TrainingRate.attributes={shr5Management_TrainingRate_timeUnit, shr5Management_TrainingRate_factor}

# RangeTableEntry class attributes and methods

# shr5Management_RangeTableEntry class attributes and methods
shr5Management_RangeTableEntry_from: Property = Property(name="from", type=IntegerType)
shr5Management_RangeTableEntry_to: Property = Property(name="to", type=IntegerType)
shr5Management_RangeTableEntry.attributes={shr5Management_RangeTableEntry_to, shr5Management_RangeTableEntry_from}

# shr5Management_RangeTable class attributes and methods

# shr5Management_ModuleSkillChange class attributes and methods

# shr5Management_ModuleTeachableChange class attributes and methods

# shr5Management_ModuleAttributeChange class attributes and methods

# shr5Management_ModuleFeatureChange class attributes and methods

# ModuleChange class attributes and methods

# shr5Management_EReference class attributes and methods

# shr5Management_EObject class attributes and methods

# shr5Management_ModuleSkillGroupChange class attributes and methods

# shr5Management_ModuleTypeChange class attributes and methods
shr5Management_ModuleTypeChange_grade: Property = Property(name="grade", type=IntegerType)
shr5Management_ModuleTypeChange.attributes={shr5Management_ModuleTypeChange_grade}

# shr5Management_TrainingsTime class attributes and methods
shr5Management_TrainingsTime_daysTrained: Property = Property(name="daysTrained", type=IntegerType)
shr5Management_TrainingsTime_daysRemains: Property = Property(name="daysRemains", type=IntegerType)
shr5Management_TrainingsTime_trainingComplete: Property = Property(name="trainingComplete", type=BooleanType)
shr5Management_TrainingsTime_m_hasValidRange: Method = Method(name="hasValidRange", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
shr5Management_TrainingsTime.attributes={shr5Management_TrainingsTime_daysRemains, shr5Management_TrainingsTime_trainingComplete, shr5Management_TrainingsTime_daysTrained}
shr5Management_TrainingsTime.methods={shr5Management_TrainingsTime_m_hasValidRange}

# CharacterChange class attributes and methods

# shr5Management_TrainingRange class attributes and methods
shr5Management_TrainingRange_start: Property = Property(name="start", type=StringType)
shr5Management_TrainingRange_end: Property = Property(name="end", type=StringType)
shr5Management_TrainingRange_daysTrained: Property = Property(name="daysTrained", type=IntegerType)
shr5Management_TrainingRange.attributes={shr5Management_TrainingRange_end, shr5Management_TrainingRange_daysTrained, shr5Management_TrainingRange_start}

# shr5Management_PersonaMartialArtChange class attributes and methods

# PersonaChange class attributes and methods

# shr5Management_MartialartStyle class attributes and methods

# shr5Management_MartialartTechnique class attributes and methods

# Relationships
persona0: BinaryAssociation = BinaryAssociation(
    name="persona0",
    ends={
        Property(name="shr5Management_AbstraktPersona", type=shr5Management_ManagedCharacter, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_ManagedCharacter", type=shr5Management_AbstraktPersona, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
changes1: BinaryAssociation = BinaryAssociation(
    name="changes1",
    ends={
        Property(name="Changes", type=shr5Management_ManagedCharacter, multiplicity=Multiplicity(1, 1)),
        Property(name="character", type=shr5Management_Changes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instructions14: BinaryAssociation = BinaryAssociation(
    name="instructions14",
    ends={
        Property(name="shr5Management_GeneratorStateToEStringMapEntry", type=shr5Management_CharacterGeneratorSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_CharacterGeneratorSystem", type=shr5Management_GeneratorStateToEStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lifestyleToStartMoney15: BinaryAssociation = BinaryAssociation(
    name="lifestyleToStartMoney15",
    ends={
        Property(name="shr5Management_LifestyleToStartMoney", type=shr5Management_CharacterGeneratorSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_CharacterGeneratorSystem16", type=shr5Management_LifestyleToStartMoney, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
characterAdvancements17: BinaryAssociation = BinaryAssociation(
    name="characterAdvancements17",
    ends={
        Property(name="shr5Management_CharacterAdvancementSystem", type=shr5Management_CharacterGeneratorSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_CharacterGeneratorSystem18", type=shr5Management_CharacterAdvancementSystem, multiplicity=Multiplicity(1, 1))
    }
)
additionalConstrains19: BinaryAssociation = BinaryAssociation(
    name="additionalConstrains19",
    ends={
        Property(name="shr5Management_QuellenConstrain", type=shr5Management_CharacterGeneratorSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_CharacterGeneratorSystem20", type=shr5Management_QuellenConstrain, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inventar2: BinaryAssociation = BinaryAssociation(
    name="inventar2",
    ends={
        Property(name="shr5Management_AbstraktGegenstand", type=shr5Management_ManagedCharacter, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_ManagedCharacter3", type=shr5Management_AbstraktGegenstand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contracts4: BinaryAssociation = BinaryAssociation(
    name="contracts4",
    ends={
        Property(name="shr5Management_Vertrag", type=shr5Management_ManagedCharacter, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_ManagedCharacter5", type=shr5Management_Vertrag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connections6: BinaryAssociation = BinaryAssociation(
    name="connections6",
    ends={
        Property(name="shr5Management_Connection", type=shr5Management_ManagedCharacter, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_ManagedCharacter7", type=shr5Management_Connection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vehicels8: BinaryAssociation = BinaryAssociation(
    name="vehicels8",
    ends={
        Property(name="shr5Management_Fahrzeug", type=shr5Management_ManagedCharacter, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_ManagedCharacter9", type=shr5Management_Fahrzeug, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
choosenLifestyle10: BinaryAssociation = BinaryAssociation(
    name="choosenLifestyle10",
    ends={
        Property(name="shr5Management_Lifestyle", type=shr5Management_ManagedCharacter, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_ManagedCharacter11", type=shr5Management_Lifestyle, multiplicity=Multiplicity(1, 1))
    }
)
nativeLanguage12: BinaryAssociation = BinaryAssociation(
    name="nativeLanguage12",
    ends={
        Property(name="shr5Management_Sprachfertigkeit", type=shr5Management_ManagedCharacter, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_ManagedCharacter13", type=shr5Management_Sprachfertigkeit, multiplicity=Multiplicity(1, 1))
    }
)
priorities21: BinaryAssociation = BinaryAssociation(
    name="priorities21",
    ends={
        Property(name="shr5Management_PriorityCategorie", type=shr5Management_PrioritySystem, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_PrioritySystem", type=shr5Management_PriorityCategorie, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
character22: BinaryAssociation = BinaryAssociation(
    name="character22",
    ends={
        Property(name="ManagedCharacter", type=shr5Management_Changes, multiplicity=Multiplicity(1, 1)),
        Property(name="changes", type=shr5Management_ManagedCharacter, multiplicity=Multiplicity(0, 1))
    }
)
choosableTypes24: BinaryAssociation = BinaryAssociation(
    name="choosableTypes24",
    ends={
        Property(name="shr5Management_Spezies", type=shr5Management_MetaType, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_MetaType", type=shr5Management_Spezies, multiplicity=Multiplicity(1, 1))
    }
)
selectableTypes25: BinaryAssociation = BinaryAssociation(
    name="selectableTypes25",
    ends={
        Property(name="shr5Management_EClass26", type=shr5Management_SpecialType, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_SpecialType", type=shr5Management_EClass, multiplicity=Multiplicity(1, 1))
    }
)
selectableSkills27: BinaryAssociation = BinaryAssociation(
    name="selectableSkills27",
    ends={
        Property(name="shr5Management_Fertigkeit", type=shr5Management_SpecialType, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_SpecialType28", type=shr5Management_Fertigkeit, multiplicity=Multiplicity(0, 9999))
    }
)
selectableSkillGroups29: BinaryAssociation = BinaryAssociation(
    name="selectableSkillGroups29",
    ends={
        Property(name="shr5Management_FertigkeitsGruppe", type=shr5Management_SpecialType, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_SpecialType30", type=shr5Management_FertigkeitsGruppe, multiplicity=Multiplicity(0, 9999))
    }
)
applicableGenerators23: BinaryAssociation = BinaryAssociation(
    name="applicableGenerators23",
    ends={
        Property(name="shr5Management_EClass", type=shr5Management_Shr5System, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_Shr5System", type=shr5Management_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
character31: BinaryAssociation = BinaryAssociation(
    name="character31",
    ends={
        Property(name="ManagedCharacter32", type=shr5Management_CharacterGenerator, multiplicity=Multiplicity(1, 1)),
        Property(name="chracterSource", type=shr5Management_ManagedCharacter, multiplicity=Multiplicity(1, 1))
    }
)
selectedGroup33: BinaryAssociation = BinaryAssociation(
    name="selectedGroup33",
    ends={
        Property(name="shr5Management_CharacterGroup", type=shr5Management_CharacterGenerator, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_CharacterGenerator", type=shr5Management_CharacterGroup, multiplicity=Multiplicity(1, 1))
    }
)
freestyleGenerator34: BinaryAssociation = BinaryAssociation(
    name="freestyleGenerator34",
    ends={
        Property(name="shr5Management_FreeStyle", type=shr5Management_FreeStyleGenerator, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_FreeStyleGenerator", type=shr5Management_FreeStyle, multiplicity=Multiplicity(0, 1))
    }
)
selectedPersona35: BinaryAssociation = BinaryAssociation(
    name="selectedPersona35",
    ends={
        Property(name="shr5Management_AbstraktPersona37", type=shr5Management_FreeStyleGenerator, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_FreeStyleGenerator36", type=shr5Management_AbstraktPersona, multiplicity=Multiplicity(0, 1))
    }
)
selectedSpecies38: BinaryAssociation = BinaryAssociation(
    name="selectedSpecies38",
    ends={
        Property(name="shr5Management_Spezies40", type=shr5Management_FreeStyleGenerator, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_FreeStyleGenerator39", type=shr5Management_Spezies, multiplicity=Multiplicity(0, 1))
    }
)
selectedType41: BinaryAssociation = BinaryAssociation(
    name="selectedType41",
    ends={
        Property(name="shr5Management_EClass43", type=shr5Management_FreeStyleGenerator, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_FreeStyleGenerator42", type=shr5Management_EClass, multiplicity=Multiplicity(0, 1))
    }
)
attibute55: BinaryAssociation = BinaryAssociation(
    name="attibute55",
    ends={
        Property(name="shr5Management_EAttribute", type=shr5Management_AttributeChange, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_AttributeChange", type=shr5Management_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
diary56: BinaryAssociation = BinaryAssociation(
    name="diary56",
    ends={
        Property(name="shr5Management_CharacterDiary", type=shr5Management_PlayerCharacter, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_PlayerCharacter", type=shr5Management_CharacterDiary, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
resourcen44: BinaryAssociation = BinaryAssociation(
    name="resourcen44",
    ends={
        Property(name="shr5Management_Resourcen", type=shr5Management_Shr5Generator, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_Shr5Generator", type=shr5Management_Resourcen, multiplicity=Multiplicity(1, 1))
    }
)
skills45: BinaryAssociation = BinaryAssociation(
    name="skills45",
    ends={
        Property(name="shr5Management_Skill", type=shr5Management_Shr5Generator, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_Shr5Generator46", type=shr5Management_Skill, multiplicity=Multiplicity(1, 1))
    }
)
attribute47: BinaryAssociation = BinaryAssociation(
    name="attribute47",
    ends={
        Property(name="shr5Management_Attributes", type=shr5Management_Shr5Generator, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_Shr5Generator48", type=shr5Management_Attributes, multiplicity=Multiplicity(1, 1))
    }
)
metaType49: BinaryAssociation = BinaryAssociation(
    name="metaType49",
    ends={
        Property(name="shr5Management_MetaType51", type=shr5Management_Shr5Generator, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_Shr5Generator50", type=shr5Management_MetaType, multiplicity=Multiplicity(1, 1))
    }
)
magic52: BinaryAssociation = BinaryAssociation(
    name="magic52",
    ends={
        Property(name="shr5Management_SpecialType54", type=shr5Management_Shr5Generator, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_Shr5Generator53", type=shr5Management_SpecialType, multiplicity=Multiplicity(1, 1))
    }
)
changeable63: BinaryAssociation = BinaryAssociation(
    name="changeable63",
    ends={
        Property(name="shr5Management_Erlernbar", type=shr5Management_PersonaChange, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_PersonaChange", type=shr5Management_Erlernbar, multiplicity=Multiplicity(1, 1))
    }
)
type64: BinaryAssociation = BinaryAssociation(
    name="type64",
    ends={
        Property(name="shr5Management_EClass65", type=shr5Management_IncreaseCharacterPart, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_IncreaseCharacterPart", type=shr5Management_EClass, multiplicity=Multiplicity(1, 1))
    }
)
lifeStyles66: BinaryAssociation = BinaryAssociation(
    name="lifeStyles66",
    ends={
        Property(name="shr5Management_Lifestyle68", type=shr5Management_LifestyleToStartMoney, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_LifestyleToStartMoney67", type=shr5Management_Lifestyle, multiplicity=Multiplicity(0, 9999))
    }
)
members69: BinaryAssociation = BinaryAssociation(
    name="members69",
    ends={
        Property(name="shr5Management_GruntMembers", type=shr5Management_GruntGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_GruntGroup", type=shr5Management_GruntMembers, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leader70: BinaryAssociation = BinaryAssociation(
    name="leader70",
    ends={
        Property(name="shr5Management_GruntMembers72", type=shr5Management_GruntGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_GruntGroup71", type=shr5Management_GruntMembers, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
members57: BinaryAssociation = BinaryAssociation(
    name="members57",
    ends={
        Property(name="shr5Management_ManagedCharacter59", type=shr5Management_CharacterGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_CharacterGroup58", type=shr5Management_ManagedCharacter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
character60: BinaryAssociation = BinaryAssociation(
    name="character60",
    ends={
        Property(name="shr5Management_ManagedCharacter62", type=shr5Management_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_Connection61", type=shr5Management_ManagedCharacter, multiplicity=Multiplicity(1, 1))
    }
)
grunts80: BinaryAssociation = BinaryAssociation(
    name="grunts80",
    ends={
        Property(name="shr5Management_GruntGroup81", type=shr5Management_GamemasterManagement, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_GamemasterManagement", type=shr5Management_GruntGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
characterAdvancements82: BinaryAssociation = BinaryAssociation(
    name="characterAdvancements82",
    ends={
        Property(name="shr5Management_Advancement", type=shr5Management_CharacterAdvancementSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_CharacterAdvancementSystem83", type=shr5Management_Advancement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allowedSources84: BinaryAssociation = BinaryAssociation(
    name="allowedSources84",
    ends={
        Property(name="shr5Management_SourceBook", type=shr5Management_Shr5RuleGenerator, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_Shr5RuleGenerator", type=shr5Management_SourceBook, multiplicity=Multiplicity(0, 9999))
    }
)
nsc73: BinaryAssociation = BinaryAssociation(
    name="nsc73",
    ends={
        Property(name="shr5Management_NonPlayerCharacter", type=shr5Management_GruntMembers, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_GruntMembers74", type=shr5Management_NonPlayerCharacter, multiplicity=Multiplicity(1, 1))
    }
)
groups75: BinaryAssociation = BinaryAssociation(
    name="groups75",
    ends={
        Property(name="shr5Management_CharacterGroup76", type=shr5Management_PlayerManagement, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_PlayerManagement", type=shr5Management_CharacterGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries78: BinaryAssociation = BinaryAssociation(
    name="entries78",
    ends={
        Property(name="shr5Management_PlayerManagement79", type=shr5Management_PlayerManagement, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_PlayerManagement77", type=shr5Management_PlayerManagement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items95: BinaryAssociation = BinaryAssociation(
    name="items95",
    ends={
        Property(name="shr5Management_Quelle96", type=shr5Management_Pack, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_Pack", type=shr5Management_Quelle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries97: BinaryAssociation = BinaryAssociation(
    name="entries97",
    ends={
        Property(name="shr5Management_DiaryEntry", type=shr5Management_CharacterDiary, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_CharacterDiary98", type=shr5Management_DiaryEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metaType85: BinaryAssociation = BinaryAssociation(
    name="metaType85",
    ends={
        Property(name="shr5Management_MetaType86", type=shr5Management_KarmaGenerator, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_KarmaGenerator", type=shr5Management_MetaType, multiplicity=Multiplicity(1, 1))
    }
)
characterConcept87: BinaryAssociation = BinaryAssociation(
    name="characterConcept87",
    ends={
        Property(name="shr5Management_SpecialType89", type=shr5Management_KarmaGenerator, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_KarmaGenerator88", type=shr5Management_SpecialType, multiplicity=Multiplicity(1, 1))
    }
)
source90: BinaryAssociation = BinaryAssociation(
    name="source90",
    ends={
        Property(name="shr5Management_Quelle", type=shr5Management_QuellenConstrain, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_QuellenConstrain91", type=shr5Management_Quelle, multiplicity=Multiplicity(1, 1))
    }
)
targets92: BinaryAssociation = BinaryAssociation(
    name="targets92",
    ends={
        Property(name="shr5Management_Quelle94", type=shr5Management_QuellenConstrain, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_QuellenConstrain93", type=shr5Management_Quelle, multiplicity=Multiplicity(0, 9999))
    }
)
furtherEducation109: BinaryAssociation = BinaryAssociation(
    name="furtherEducation109",
    ends={
        Property(name="shr5Management_LifeModulesGenerator110", type=shr5Management_LifeModule, multiplicity=Multiplicity(0, 1)),
        Property(name="shr5Management_LifeModule111", type=shr5Management_LifeModulesGenerator, multiplicity=Multiplicity(1, 1))
    }
)
realLife112: BinaryAssociation = BinaryAssociation(
    name="realLife112",
    ends={
        Property(name="shr5Management_LifeModule114", type=shr5Management_LifeModulesGenerator, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_LifeModulesGenerator113", type=shr5Management_LifeModule, multiplicity=Multiplicity(1, 9999))
    }
)
modules115: BinaryAssociation = BinaryAssociation(
    name="modules115",
    ends={
        Property(name="shr5Management_LifeModule116", type=shr5Management_LifeModulesSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_LifeModulesSystem", type=shr5Management_LifeModule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
characterChanges117: BinaryAssociation = BinaryAssociation(
    name="characterChanges117",
    ends={
        Property(name="shr5Management_ModuleChange", type=shr5Management_LifeModule, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_LifeModule118", type=shr5Management_ModuleChange, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contractToPay99: BinaryAssociation = BinaryAssociation(
    name="contractToPay99",
    ends={
        Property(name="shr5Management_Vertrag100", type=shr5Management_ContractPayment, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_ContractPayment", type=shr5Management_Vertrag, multiplicity=Multiplicity(1, 1))
    }
)
change101: BinaryAssociation = BinaryAssociation(
    name="change101",
    ends={
        Property(name="shr5Management_Changes", type=shr5Management_CharacterChange, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_CharacterChange", type=shr5Management_Changes, multiplicity=Multiplicity(1, 1))
    }
)
nationality102: BinaryAssociation = BinaryAssociation(
    name="nationality102",
    ends={
        Property(name="shr5Management_LifeModule", type=shr5Management_LifeModulesGenerator, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_LifeModulesGenerator", type=shr5Management_LifeModule, multiplicity=Multiplicity(1, 1))
    }
)
formativeYears103: BinaryAssociation = BinaryAssociation(
    name="formativeYears103",
    ends={
        Property(name="shr5Management_LifeModule105", type=shr5Management_LifeModulesGenerator, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_LifeModulesGenerator104", type=shr5Management_LifeModule, multiplicity=Multiplicity(1, 1))
    }
)
teenYears106: BinaryAssociation = BinaryAssociation(
    name="teenYears106",
    ends={
        Property(name="shr5Management_LifeModule108", type=shr5Management_LifeModulesGenerator, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_LifeModulesGenerator107", type=shr5Management_LifeModule, multiplicity=Multiplicity(1, 1))
    }
)
skill119: BinaryAssociation = BinaryAssociation(
    name="skill119",
    ends={
        Property(name="shr5Management_Fertigkeit120", type=shr5Management_ModuleSkillChange, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_ModuleSkillChange", type=shr5Management_Fertigkeit, multiplicity=Multiplicity(0, 1))
    }
)
teachable121: BinaryAssociation = BinaryAssociation(
    name="teachable121",
    ends={
        Property(name="shr5Management_Erlernbar122", type=shr5Management_ModuleTeachableChange, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_ModuleTeachableChange", type=shr5Management_Erlernbar, multiplicity=Multiplicity(0, 1))
    }
)
attribute123: BinaryAssociation = BinaryAssociation(
    name="attribute123",
    ends={
        Property(name="shr5Management_EAttribute124", type=shr5Management_ModuleAttributeChange, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_ModuleAttributeChange", type=shr5Management_EAttribute, multiplicity=Multiplicity(1, 1))
    }
)
feature125: BinaryAssociation = BinaryAssociation(
    name="feature125",
    ends={
        Property(name="shr5Management_EReference", type=shr5Management_ModuleFeatureChange, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_ModuleFeatureChange", type=shr5Management_EReference, multiplicity=Multiplicity(0, 1))
    }
)
value126: BinaryAssociation = BinaryAssociation(
    name="value126",
    ends={
        Property(name="shr5Management_EObject", type=shr5Management_ModuleFeatureChange, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_ModuleFeatureChange127", type=shr5Management_EObject, multiplicity=Multiplicity(0, 1))
    }
)
skillGroup128: BinaryAssociation = BinaryAssociation(
    name="skillGroup128",
    ends={
        Property(name="shr5Management_FertigkeitsGruppe129", type=shr5Management_ModuleSkillGroupChange, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_ModuleSkillGroupChange", type=shr5Management_FertigkeitsGruppe, multiplicity=Multiplicity(0, 1))
    }
)
training130: BinaryAssociation = BinaryAssociation(
    name="training130",
    ends={
        Property(name="TrainingRange", type=shr5Management_TrainingsTime, multiplicity=Multiplicity(1, 1)),
        Property(name="trainingTime", type=shr5Management_TrainingRange, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
style131: BinaryAssociation = BinaryAssociation(
    name="style131",
    ends={
        Property(name="shr5Management_MartialartStyle", type=shr5Management_PersonaMartialArtChange, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_PersonaMartialArtChange", type=shr5Management_MartialartStyle, multiplicity=Multiplicity(0, 1))
    }
)
technique132: BinaryAssociation = BinaryAssociation(
    name="technique132",
    ends={
        Property(name="shr5Management_MartialartTechnique", type=shr5Management_PersonaMartialArtChange, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5Management_PersonaMartialArtChange133", type=shr5Management_MartialartTechnique, multiplicity=Multiplicity(0, 1))
    }
)
trainingTime134: BinaryAssociation = BinaryAssociation(
    name="trainingTime134",
    ends={
        Property(name="TrainingsTime", type=shr5Management_TrainingRange, multiplicity=Multiplicity(1, 1)),
        Property(name="training", type=shr5Management_TrainingsTime, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_shr5Management_CharacterGeneratorSystem_Beschreibbar = Generalization(general=Beschreibbar, specific=shr5Management_CharacterGeneratorSystem)
gen_shr5Management_CharacterGeneratorSystem_Quelle = Generalization(general=Quelle, specific=shr5Management_CharacterGeneratorSystem)
gen_shr5Management_KarmaGaint_Changes = Generalization(general=Changes, specific=shr5Management_KarmaGaint)
gen_shr5Management_FreeStyle_CharacterGeneratorSystem = Generalization(general=CharacterGeneratorSystem, specific=shr5Management_FreeStyle)
gen_shr5Management_Shr5System_PrioritySystem = Generalization(general=PrioritySystem, specific=shr5Management_Shr5System)
gen_shr5Management_PrioritySystem_CharacterGeneratorSystem = Generalization(general=CharacterGeneratorSystem, specific=shr5Management_PrioritySystem)
gen_shr5Management_NonPlayerCharacter_ManagedCharacter = Generalization(general=ManagedCharacter, specific=shr5Management_NonPlayerCharacter)
gen_shr5Management_Attributes_PriorityCategorie = Generalization(general=PriorityCategorie, specific=shr5Management_Attributes)
gen_shr5Management_Skill_PriorityCategorie = Generalization(general=PriorityCategorie, specific=shr5Management_Skill)
gen_shr5Management_Resourcen_PriorityCategorie = Generalization(general=PriorityCategorie, specific=shr5Management_Resourcen)
gen_shr5Management_SpecialType_PriorityCategorie = Generalization(general=PriorityCategorie, specific=shr5Management_SpecialType)
gen_shr5Management_Technomancer_SpecialType = Generalization(general=SpecialType, specific=shr5Management_Technomancer)
gen_shr5Management_MetaType_PriorityCategorie = Generalization(general=PriorityCategorie, specific=shr5Management_MetaType)
gen_shr5Management_Spellcaster_Adept = Generalization(general=Adept, specific=shr5Management_Spellcaster)
gen_shr5Management_Adept_SpecialType = Generalization(general=SpecialType, specific=shr5Management_Adept)
gen_shr5Management_AttributeChange_PersonaValueChange = Generalization(general=PersonaValueChange, specific=shr5Management_AttributeChange)
gen_shr5Management_PlayerCharacter_ManagedCharacter = Generalization(general=ManagedCharacter, specific=shr5Management_PlayerCharacter)
gen_shr5Management_Mudan_SpecialType = Generalization(general=SpecialType, specific=shr5Management_Mudan)
gen_shr5Management_PersonaChange_PersonaValueChange = Generalization(general=PersonaValueChange, specific=shr5Management_PersonaChange)
gen_shr5Management_PersonaValueChange_Changes = Generalization(general=Changes, specific=shr5Management_PersonaValueChange)
gen_shr5Management_GruntGroup_Beschreibbar = Generalization(general=Beschreibbar, specific=shr5Management_GruntGroup)
gen_shr5Management_CharacterGroup_Beschreibbar = Generalization(general=Beschreibbar, specific=shr5Management_CharacterGroup)
gen_shr5Management_GamemasterManagement_PlayerManagement = Generalization(general=PlayerManagement, specific=shr5Management_GamemasterManagement)
gen_shr5Management_CharacterAdvancementSystem_Beschreibbar = Generalization(general=Beschreibbar, specific=shr5Management_CharacterAdvancementSystem)
gen_shr5Management_PlayerManagement_Beschreibbar = Generalization(general=Beschreibbar, specific=shr5Management_PlayerManagement)
gen_shr5Management_Pack_Beschreibbar = Generalization(general=Beschreibbar, specific=shr5Management_Pack)
gen_shr5Management_Pack_Quelle = Generalization(general=Quelle, specific=shr5Management_Pack)
gen_shr5Management_Pack_GeldWert = Generalization(general=GeldWert, specific=shr5Management_Pack)
gen_shr5Management_LifeModulesSystem_Shr5System = Generalization(general=Shr5System, specific=shr5Management_LifeModulesSystem)
gen_shr5Management_LifeModule_Beschreibbar = Generalization(general=Beschreibbar, specific=shr5Management_LifeModule)
gen_shr5Management_LifeModule_Quelle = Generalization(general=Quelle, specific=shr5Management_LifeModule)
gen_shr5Management_ContractPayment_DiaryEntry = Generalization(general=DiaryEntry, specific=shr5Management_ContractPayment)
gen_shr5Management_CharacterChange_DiaryEntry = Generalization(general=DiaryEntry, specific=shr5Management_CharacterChange)
gen_shr5Management_SumToTenGenerator_Shr5Generator = Generalization(general=Shr5Generator, specific=shr5Management_SumToTenGenerator)
gen_shr5Management_TrainingRate_RangeTableEntry = Generalization(general=RangeTableEntry, specific=shr5Management_TrainingRate)
gen_shr5Management_ModuleFeatureChange_ModuleChange = Generalization(general=ModuleChange, specific=shr5Management_ModuleFeatureChange)
gen_shr5Management_ModuleTypeChange_ModuleChange = Generalization(general=ModuleChange, specific=shr5Management_ModuleTypeChange)
gen_shr5Management_TrainingsTime_CharacterChange = Generalization(general=CharacterChange, specific=shr5Management_TrainingsTime)
gen_shr5Management_PersonaMartialArtChange_PersonaChange = Generalization(general=PersonaChange, specific=shr5Management_PersonaMartialArtChange)

# Domain Model
domain_model = DomainModel(
    name="shr5Management",
    types={shr5Management_ManagedCharacter, shr5Management_AbstraktPersona, shr5Management_Changes, shr5Management_CharacterGeneratorSystem, Beschreibbar, Quelle, shr5Management_GeneratorStateToEStringMapEntry, shr5Management_LifestyleToStartMoney, shr5Management_CharacterAdvancementSystem, shr5Management_QuellenConstrain, shr5Management_AbstraktGegenstand, shr5Management_Vertrag, shr5Management_Connection, shr5Management_Fahrzeug, shr5Management_Lifestyle, shr5Management_Sprachfertigkeit, shr5Management_KarmaGaint, Changes, shr5Management_FreeStyle, shr5Management_Shr5System, PrioritySystem, shr5Management_PrioritySystem, CharacterGeneratorSystem, shr5Management_PriorityCategorie, shr5Management_NonPlayerCharacter, ManagedCharacter, shr5Management_Spezies, shr5Management_Attributes, shr5Management_Skill, shr5Management_Resourcen, shr5Management_SpecialType, shr5Management_Fertigkeit, shr5Management_FertigkeitsGruppe, shr5Management_Technomancer, SpecialType, shr5Management_EClass, shr5Management_MetaType, PriorityCategorie, shr5Management_CharacterGroup, shr5Management_FreeStyleGenerator, shr5Management_Shr5Generator, shr5Management_Spellcaster, Adept, shr5Management_Adept, shr5Management_CharacterGenerator, shr5Management_AttributeChange, PersonaValueChange, shr5Management_EAttribute, shr5Management_PlayerCharacter, shr5Management_CharacterDiary, shr5Management_Mudan, shr5Management_PersonaChange, shr5Management_Erlernbar, shr5Management_PersonaValueChange, shr5Management_Advancement, shr5Management_IncreaseCharacterPart, shr5Management_GruntGroup, shr5Management_GruntMembers, PlayerManagement, shr5Management_SourceBook, shr5Management_Shr5RuleGenerator, shr5Management_KarmaGenerator, shr5Management_PlayerManagement, shr5Management_GamemasterManagement, shr5Management_Pack, GeldWert, shr5Management_DiaryEntry, shr5Management_Quelle, shr5Management_LifeModulesSystem, Shr5System, shr5Management_ModuleChange, shr5Management_ContractPayment, DiaryEntry, shr5Management_CharacterChange, shr5Management_SumToTenGenerator, Shr5Generator, shr5Management_LifeModulesGenerator, shr5Management_LifeModule, shr5Management_Shr5KarmaGenerator, shr5Management_TrainingRate, RangeTableEntry, shr5Management_RangeTableEntry, shr5Management_RangeTable, shr5Management_ModuleSkillChange, shr5Management_ModuleTeachableChange, shr5Management_ModuleAttributeChange, shr5Management_ModuleFeatureChange, ModuleChange, shr5Management_EReference, shr5Management_EObject, shr5Management_ModuleSkillGroupChange, shr5Management_ModuleTypeChange, shr5Management_TrainingsTime, CharacterChange, shr5Management_TrainingRange, shr5Management_PersonaMartialArtChange, PersonaChange, shr5Management_MartialartStyle, shr5Management_MartialartTechnique, GeneratorState, Sex, QuellenConstrainType, LifeModuleType},
    associations={persona0, changes1, instructions14, lifestyleToStartMoney15, characterAdvancements17, additionalConstrains19, inventar2, contracts4, connections6, vehicels8, choosenLifestyle10, nativeLanguage12, priorities21, character22, choosableTypes24, selectableTypes25, selectableSkills27, selectableSkillGroups29, applicableGenerators23, character31, selectedGroup33, freestyleGenerator34, selectedPersona35, selectedSpecies38, selectedType41, attibute55, diary56, resourcen44, skills45, attribute47, metaType49, magic52, changeable63, type64, lifeStyles66, members69, leader70, members57, character60, grunts80, characterAdvancements82, allowedSources84, nsc73, groups75, entries78, items95, entries97, metaType85, characterConcept87, source90, targets92, furtherEducation109, realLife112, modules115, characterChanges117, contractToPay99, change101, nationality102, formativeYears103, teenYears106, skill119, teachable121, attribute123, feature125, value126, skillGroup128, training130, style131, technique132, trainingTime134},
    generalizations={gen_shr5Management_CharacterGeneratorSystem_Beschreibbar, gen_shr5Management_CharacterGeneratorSystem_Quelle, gen_shr5Management_KarmaGaint_Changes, gen_shr5Management_FreeStyle_CharacterGeneratorSystem, gen_shr5Management_Shr5System_PrioritySystem, gen_shr5Management_PrioritySystem_CharacterGeneratorSystem, gen_shr5Management_NonPlayerCharacter_ManagedCharacter, gen_shr5Management_Attributes_PriorityCategorie, gen_shr5Management_Skill_PriorityCategorie, gen_shr5Management_Resourcen_PriorityCategorie, gen_shr5Management_SpecialType_PriorityCategorie, gen_shr5Management_Technomancer_SpecialType, gen_shr5Management_MetaType_PriorityCategorie, gen_shr5Management_Spellcaster_Adept, gen_shr5Management_Adept_SpecialType, gen_shr5Management_AttributeChange_PersonaValueChange, gen_shr5Management_PlayerCharacter_ManagedCharacter, gen_shr5Management_Mudan_SpecialType, gen_shr5Management_PersonaChange_PersonaValueChange, gen_shr5Management_PersonaValueChange_Changes, gen_shr5Management_GruntGroup_Beschreibbar, gen_shr5Management_CharacterGroup_Beschreibbar, gen_shr5Management_GamemasterManagement_PlayerManagement, gen_shr5Management_CharacterAdvancementSystem_Beschreibbar, gen_shr5Management_PlayerManagement_Beschreibbar, gen_shr5Management_Pack_Beschreibbar, gen_shr5Management_Pack_Quelle, gen_shr5Management_Pack_GeldWert, gen_shr5Management_LifeModulesSystem_Shr5System, gen_shr5Management_LifeModule_Beschreibbar, gen_shr5Management_LifeModule_Quelle, gen_shr5Management_ContractPayment_DiaryEntry, gen_shr5Management_CharacterChange_DiaryEntry, gen_shr5Management_SumToTenGenerator_Shr5Generator, gen_shr5Management_TrainingRate_RangeTableEntry, gen_shr5Management_ModuleFeatureChange_ModuleChange, gen_shr5Management_ModuleTypeChange_ModuleChange, gen_shr5Management_TrainingsTime_CharacterChange, gen_shr5Management_PersonaMartialArtChange_PersonaChange},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)