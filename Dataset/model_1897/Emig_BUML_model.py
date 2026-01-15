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
emig_MigrationProgram = Class(name="emig::MigrationProgram")
emig_MyModel = Class(name="emig::MyModel")
emig_MigrationLibrary = Class(name="emig::MigrationLibrary")
emig_EPackage = Class(name="emig::EPackage")
emig_Rule = Class(name="emig::Rule")
emig_LocatedElement = Class(name="emig::LocatedElement")
LocatedElement = Class(name="LocatedElement")
emig_Artifact = Class(name="emig::Artifact")
OpDef = Class(name="OpDef")
emig_OpDef = Class(name="emig::OpDef")
emig_RewritingRule = Class(name="emig::RewritingRule")
emig_setterDef = Class(name="emig::setterDef")
emig_EPackageOpDef = Class(name="emig::EPackageOpDef")
emig_EClassOpDef = Class(name="emig::EClassOpDef")
emig_EClass = Class(name="emig::EClass")
emig_EAttributeOpDef = Class(name="emig::EAttributeOpDef")
emig_EReferenceOpDef = Class(name="emig::EReferenceOpDef")
emig_EAttribute = Class(name="emig::EAttribute")
Migrator = Class(name="Migrator")
emig_EReference = Class(name="emig::EReference")
emig_EStructuralFeature = Class(name="emig::EStructuralFeature")
emig_Parameter = Class(name="emig::Parameter")
emig_MigratorSX = Class(name="emig::MigratorSX")
emig_MigratorDX = Class(name="emig::MigratorDX")
emig_Migrator = Class(name="emig::Migrator")
emig_DotNavigationObjDX = Class(name="emig::DotNavigationObjDX")
emig_FilterMigrator = Class(name="emig::FilterMigrator")
emig_DotNavigationObjSX = Class(name="emig::DotNavigationObjSX")
emig_EObject = Class(name="emig::EObject")
emig_Package = Class(name="emig::Package")
EPackage = Class(name="EPackage")
emig_Class = Class(name="emig::Class")
EClass = Class(name="EClass")
emig_Attribute = Class(name="emig::Attribute")
EAttribute = Class(name="EAttribute")
emig_Reference = Class(name="emig::Reference")
EReference = Class(name="EReference")

# emig_MigrationProgram class attributes and methods
emig_MigrationProgram_artifact: Property = Property(name="artifact", type=StringType)
emig_MigrationProgram_name: Property = Property(name="name", type=StringType)
emig_MigrationProgram_libs: Property = Property(name="libs", type=StringType)
emig_MigrationProgram_migr: Property = Property(name="migr", type=StringType)
emig_MigrationProgram_delta: Property = Property(name="delta", type=StringType)
emig_MigrationProgram.attributes={emig_MigrationProgram_libs, emig_MigrationProgram_delta, emig_MigrationProgram_artifact, emig_MigrationProgram_migr, emig_MigrationProgram_name}

# emig_MyModel class attributes and methods

# emig_MigrationLibrary class attributes and methods
emig_MigrationLibrary_name: Property = Property(name="name", type=StringType)
emig_MigrationLibrary.attributes={emig_MigrationLibrary_name}

# emig_EPackage class attributes and methods

# emig_Rule class attributes and methods
emig_Rule_name: Property = Property(name="name", type=StringType)
emig_Rule.attributes={emig_Rule_name}

# emig_LocatedElement class attributes and methods
emig_LocatedElement_line: Property = Property(name="line", type=IntegerType)
emig_LocatedElement_endline: Property = Property(name="endline", type=IntegerType)
emig_LocatedElement_offset: Property = Property(name="offset", type=IntegerType)
emig_LocatedElement_endoffset: Property = Property(name="endoffset", type=IntegerType)
emig_LocatedElement.attributes={emig_LocatedElement_endoffset, emig_LocatedElement_line, emig_LocatedElement_endline, emig_LocatedElement_offset}

# LocatedElement class attributes and methods

# emig_Artifact class attributes and methods
emig_Artifact_type: Property = Property(name="type", type=StringType)
emig_Artifact.attributes={emig_Artifact_type}

# OpDef class attributes and methods

# emig_OpDef class attributes and methods
emig_OpDef_op: Property = Property(name="op", type=StringType)
emig_OpDef.attributes={emig_OpDef_op}

# emig_RewritingRule class attributes and methods

# emig_setterDef class attributes and methods
emig_setterDef_operator: Property = Property(name="operator", type=StringType)
emig_setterDef.attributes={emig_setterDef_operator}

# emig_EPackageOpDef class attributes and methods

# emig_EClassOpDef class attributes and methods

# emig_EClass class attributes and methods

# emig_EAttributeOpDef class attributes and methods

# emig_EReferenceOpDef class attributes and methods

# emig_EAttribute class attributes and methods

# Migrator class attributes and methods

# emig_EReference class attributes and methods

# emig_EStructuralFeature class attributes and methods

# emig_Parameter class attributes and methods
emig_Parameter_name: Property = Property(name="name", type=StringType)
emig_Parameter.attributes={emig_Parameter_name}

# emig_MigratorSX class attributes and methods

# emig_MigratorDX class attributes and methods

# emig_Migrator class attributes and methods
emig_Migrator_name: Property = Property(name="name", type=StringType)
emig_Migrator.attributes={emig_Migrator_name}

# emig_DotNavigationObjDX class attributes and methods

# emig_FilterMigrator class attributes and methods
emig_FilterMigrator_op: Property = Property(name="op", type=StringType)
emig_FilterMigrator.attributes={emig_FilterMigrator_op}

# emig_DotNavigationObjSX class attributes and methods

# emig_EObject class attributes and methods

# emig_Package class attributes and methods

# EPackage class attributes and methods

# emig_Class class attributes and methods

# EClass class attributes and methods

# emig_Attribute class attributes and methods

# EAttribute class attributes and methods

# emig_Reference class attributes and methods

# EReference class attributes and methods

# Relationships
migrationLib0: BinaryAssociation = BinaryAssociation(
    name="migrationLib0",
    ends={
        Property(name="emig_MyModel", type=emig_MigrationLibrary, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="emig_MigrationLibrary", type=emig_MyModel, multiplicity=Multiplicity(1, 1))
    }
)
typeArt5: BinaryAssociation = BinaryAssociation(
    name="typeArt5",
    ends={
        Property(name="emig_Artifact", type=emig_MigrationProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_MigrationProgram6", type=emig_Artifact, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
MigrationProgr1: BinaryAssociation = BinaryAssociation(
    name="MigrationProgr1",
    ends={
        Property(name="emig_MigrationProgram", type=emig_MyModel, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_MyModel2", type=emig_MigrationProgram, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rules3: BinaryAssociation = BinaryAssociation(
    name="rules3",
    ends={
        Property(name="emig_Rule", type=emig_MigrationLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_MigrationLibrary4", type=emig_Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
var18: BinaryAssociation = BinaryAssociation(
    name="var18",
    ends={
        Property(name="emig_EPackage19", type=emig_EPackageOpDef, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_EPackageOpDef", type=emig_EPackage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transformationPackage7: BinaryAssociation = BinaryAssociation(
    name="transformationPackage7",
    ends={
        Property(name="emig_EPackage", type=emig_MigrationProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_MigrationProgram8", type=emig_EPackage, multiplicity=Multiplicity(0, 9999))
    }
)
rules9: BinaryAssociation = BinaryAssociation(
    name="rules9",
    ends={
        Property(name="emig_Rule11", type=emig_MigrationProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_MigrationProgram10", type=emig_Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
filter12: BinaryAssociation = BinaryAssociation(
    name="filter12",
    ends={
        Property(name="emig_OpDef", type=emig_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_Rule13", type=emig_OpDef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rewritingRules14: BinaryAssociation = BinaryAssociation(
    name="rewritingRules14",
    ends={
        Property(name="emig_RewritingRule", type=emig_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_Rule15", type=emig_RewritingRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
setters16: BinaryAssociation = BinaryAssociation(
    name="setters16",
    ends={
        Property(name="emig_setterDef", type=emig_OpDef, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_OpDef17", type=emig_setterDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref36: BinaryAssociation = BinaryAssociation(
    name="ref36",
    ends={
        Property(name="emig_EAttributeOpDef37", type=emig_EAttribute, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="emig_EAttribute38", type=emig_EAttributeOpDef, multiplicity=Multiplicity(1, 1))
    }
)
ref20: BinaryAssociation = BinaryAssociation(
    name="ref20",
    ends={
        Property(name="emig_EPackage22", type=emig_EPackageOpDef, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_EPackageOpDef21", type=emig_EPackage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classes23: BinaryAssociation = BinaryAssociation(
    name="classes23",
    ends={
        Property(name="emig_EClassOpDef", type=emig_EPackageOpDef, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_EPackageOpDef24", type=emig_EClassOpDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
var25: BinaryAssociation = BinaryAssociation(
    name="var25",
    ends={
        Property(name="emig_EClass", type=emig_EClassOpDef, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_EClassOpDef26", type=emig_EClass, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref27: BinaryAssociation = BinaryAssociation(
    name="ref27",
    ends={
        Property(name="emig_EClass29", type=emig_EClassOpDef, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_EClassOpDef28", type=emig_EClass, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes30: BinaryAssociation = BinaryAssociation(
    name="attributes30",
    ends={
        Property(name="emig_EAttributeOpDef", type=emig_EClassOpDef, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_EClassOpDef31", type=emig_EAttributeOpDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references32: BinaryAssociation = BinaryAssociation(
    name="references32",
    ends={
        Property(name="emig_EReferenceOpDef", type=emig_EClassOpDef, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_EClassOpDef33", type=emig_EReferenceOpDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
var34: BinaryAssociation = BinaryAssociation(
    name="var34",
    ends={
        Property(name="emig_EAttribute", type=emig_EAttributeOpDef, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_EAttributeOpDef35", type=emig_EAttribute, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
var39: BinaryAssociation = BinaryAssociation(
    name="var39",
    ends={
        Property(name="emig_EReference", type=emig_EReferenceOpDef, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_EReferenceOpDef40", type=emig_EReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref41: BinaryAssociation = BinaryAssociation(
    name="ref41",
    ends={
        Property(name="emig_EReference43", type=emig_EReferenceOpDef, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_EReferenceOpDef42", type=emig_EReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
metafeature44: BinaryAssociation = BinaryAssociation(
    name="metafeature44",
    ends={
        Property(name="emig_EStructuralFeature", type=emig_setterDef, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_setterDef45", type=emig_EStructuralFeature, multiplicity=Multiplicity(0, 1))
    }
)
par46: BinaryAssociation = BinaryAssociation(
    name="par46",
    ends={
        Property(name="emig_Parameter", type=emig_setterDef, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_setterDef47", type=emig_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
migratorSX48: BinaryAssociation = BinaryAssociation(
    name="migratorSX48",
    ends={
        Property(name="MigratorSX", type=emig_RewritingRule, multiplicity=Multiplicity(1, 1)),
        Property(name="rewritingRule", type=emig_MigratorSX, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
migratorDX49: BinaryAssociation = BinaryAssociation(
    name="migratorDX49",
    ends={
        Property(name="MigratorDX", type=emig_RewritingRule, multiplicity=Multiplicity(1, 1)),
        Property(name="rewritingRule50", type=emig_MigratorDX, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value65: BinaryAssociation = BinaryAssociation(
    name="value65",
    ends={
        Property(name="emig_DotNavigationObjDX", type=emig_FilterMigrator, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_FilterMigrator66", type=emig_DotNavigationObjDX, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elementSX51: BinaryAssociation = BinaryAssociation(
    name="elementSX51",
    ends={
        Property(name="emig_EClass52", type=emig_MigratorSX, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_MigratorSX", type=emig_EClass, multiplicity=Multiplicity(0, 1))
    }
)
filterSX53: BinaryAssociation = BinaryAssociation(
    name="filterSX53",
    ends={
        Property(name="emig_FilterMigrator", type=emig_MigratorSX, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_MigratorSX54", type=emig_FilterMigrator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rewritingRule55: BinaryAssociation = BinaryAssociation(
    name="rewritingRule55",
    ends={
        Property(name="RewritingRule", type=emig_MigratorSX, multiplicity=Multiplicity(1, 1)),
        Property(name="migratorSX", type=emig_RewritingRule, multiplicity=Multiplicity(0, 1))
    }
)
elementDX56: BinaryAssociation = BinaryAssociation(
    name="elementDX56",
    ends={
        Property(name="emig_EClass57", type=emig_MigratorDX, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_MigratorDX", type=emig_EClass, multiplicity=Multiplicity(0, 1))
    }
)
filterDX58: BinaryAssociation = BinaryAssociation(
    name="filterDX58",
    ends={
        Property(name="emig_FilterMigrator60", type=emig_MigratorDX, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_MigratorDX59", type=emig_FilterMigrator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rewritingRule61: BinaryAssociation = BinaryAssociation(
    name="rewritingRule61",
    ends={
        Property(name="RewritingRule62", type=emig_MigratorDX, multiplicity=Multiplicity(1, 1)),
        Property(name="migratorDX", type=emig_RewritingRule, multiplicity=Multiplicity(0, 1))
    }
)
featureSX63: BinaryAssociation = BinaryAssociation(
    name="featureSX63",
    ends={
        Property(name="emig_DotNavigationObjSX", type=emig_FilterMigrator, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_FilterMigrator64", type=emig_DotNavigationObjSX, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
obj67: BinaryAssociation = BinaryAssociation(
    name="obj67",
    ends={
        Property(name="emig_EObject", type=emig_DotNavigationObjSX, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_DotNavigationObjSX68", type=emig_EObject, multiplicity=Multiplicity(0, 1))
    }
)
ref69: BinaryAssociation = BinaryAssociation(
    name="ref69",
    ends={
        Property(name="emig_EStructuralFeature71", type=emig_DotNavigationObjSX, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_DotNavigationObjSX70", type=emig_EStructuralFeature, multiplicity=Multiplicity(0, 1))
    }
)
obj72: BinaryAssociation = BinaryAssociation(
    name="obj72",
    ends={
        Property(name="emig_EObject74", type=emig_DotNavigationObjDX, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_DotNavigationObjDX73", type=emig_EObject, multiplicity=Multiplicity(0, 1))
    }
)
ref75: BinaryAssociation = BinaryAssociation(
    name="ref75",
    ends={
        Property(name="emig_EStructuralFeature77", type=emig_DotNavigationObjDX, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_DotNavigationObjDX76", type=emig_EStructuralFeature, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_emig_MigrationProgram_LocatedElement = Generalization(general=LocatedElement, specific=emig_MigrationProgram)
gen_emig_EPackageOpDef_OpDef = Generalization(general=OpDef, specific=emig_EPackageOpDef)
gen_emig_Artifact_LocatedElement = Generalization(general=LocatedElement, specific=emig_Artifact)
gen_emig_Rule_LocatedElement = Generalization(general=LocatedElement, specific=emig_Rule)
gen_emig_OpDef_LocatedElement = Generalization(general=LocatedElement, specific=emig_OpDef)
gen_emig_EReferenceOpDef_OpDef = Generalization(general=OpDef, specific=emig_EReferenceOpDef)
gen_emig_EClassOpDef_OpDef = Generalization(general=OpDef, specific=emig_EClassOpDef)
gen_emig_EAttributeOpDef_OpDef = Generalization(general=OpDef, specific=emig_EAttributeOpDef)
gen_emig_MigratorSX_Migrator = Generalization(general=Migrator, specific=emig_MigratorSX)
gen_emig_setterDef_LocatedElement = Generalization(general=LocatedElement, specific=emig_setterDef)
gen_emig_RewritingRule_LocatedElement = Generalization(general=LocatedElement, specific=emig_RewritingRule)
gen_emig_Migrator_LocatedElement = Generalization(general=LocatedElement, specific=emig_Migrator)
gen_emig_MigratorDX_Migrator = Generalization(general=Migrator, specific=emig_MigratorDX)
gen_emig_FilterMigrator_LocatedElement = Generalization(general=LocatedElement, specific=emig_FilterMigrator)
gen_emig_DotNavigationObjSX_LocatedElement = Generalization(general=LocatedElement, specific=emig_DotNavigationObjSX)
gen_emig_DotNavigationObjDX_LocatedElement = Generalization(general=LocatedElement, specific=emig_DotNavigationObjDX)
gen_emig_Parameter_LocatedElement = Generalization(general=LocatedElement, specific=emig_Parameter)
gen_emig_Package_EPackage = Generalization(general=EPackage, specific=emig_Package)
gen_emig_Class_EClass = Generalization(general=EClass, specific=emig_Class)
gen_emig_Attribute_EAttribute = Generalization(general=EAttribute, specific=emig_Attribute)
gen_emig_Reference_EReference = Generalization(general=EReference, specific=emig_Reference)

# Domain Model
domain_model = DomainModel(
    name="emig",
    types={emig_MigrationProgram, emig_MyModel, emig_MigrationLibrary, emig_EPackage, emig_Rule, emig_LocatedElement, LocatedElement, emig_Artifact, OpDef, emig_OpDef, emig_RewritingRule, emig_setterDef, emig_EPackageOpDef, emig_EClassOpDef, emig_EClass, emig_EAttributeOpDef, emig_EReferenceOpDef, emig_EAttribute, Migrator, emig_EReference, emig_EStructuralFeature, emig_Parameter, emig_MigratorSX, emig_MigratorDX, emig_Migrator, emig_DotNavigationObjDX, emig_FilterMigrator, emig_DotNavigationObjSX, emig_EObject, emig_Package, EPackage, emig_Class, EClass, emig_Attribute, EAttribute, emig_Reference, EReference},
    associations={migrationLib0, typeArt5, MigrationProgr1, rules3, var18, transformationPackage7, rules9, filter12, rewritingRules14, setters16, ref36, ref20, classes23, var25, ref27, attributes30, references32, var34, var39, ref41, metafeature44, par46, migratorSX48, migratorDX49, value65, elementSX51, filterSX53, rewritingRule55, elementDX56, filterDX58, rewritingRule61, featureSX63, obj67, ref69, obj72, ref75},
    generalizations={gen_emig_MigrationProgram_LocatedElement, gen_emig_EPackageOpDef_OpDef, gen_emig_Artifact_LocatedElement, gen_emig_Rule_LocatedElement, gen_emig_OpDef_LocatedElement, gen_emig_EReferenceOpDef_OpDef, gen_emig_EClassOpDef_OpDef, gen_emig_EAttributeOpDef_OpDef, gen_emig_MigratorSX_Migrator, gen_emig_setterDef_LocatedElement, gen_emig_RewritingRule_LocatedElement, gen_emig_Migrator_LocatedElement, gen_emig_MigratorDX_Migrator, gen_emig_FilterMigrator_LocatedElement, gen_emig_DotNavigationObjSX_LocatedElement, gen_emig_DotNavigationObjDX_LocatedElement, gen_emig_Parameter_LocatedElement, gen_emig_Package_EPackage, gen_emig_Class_EClass, gen_emig_Attribute_EAttribute, gen_emig_Reference_EReference},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)