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
grammar_features_AbstractSuperclass = Class(name="grammar::features::AbstractSuperclass", is_abstract=True)
grammar_features_ConcreteSubclassA = Class(name="grammar::features::ConcreteSubclassA")
AbstractSuperclass = Class(name="AbstractSuperclass")
grammar_features_Root = Class(name="grammar::features::Root")
grammar_features_Child = Class(name="grammar::features::Child", is_abstract=True)
grammar_features_AlternativeSyntax = Class(name="grammar::features::AlternativeSyntax")
Child = Class(name="Child")
grammar_features_ConcreteSubclassB = Class(name="grammar::features::ConcreteSubclassB")
grammar_features_OptionalContainment = Class(name="grammar::features::OptionalContainment")
grammar_features_X = Class(name="grammar::features::X")
grammar_features_MandatoryContainment = Class(name="grammar::features::MandatoryContainment")
grammar_features_OptionalNonContainment = Class(name="grammar::features::OptionalNonContainment")
grammar_features_PlusContainment = Class(name="grammar::features::PlusContainment")
grammar_features_StarContainment = Class(name="grammar::features::StarContainment")
grammar_features_StarNonContainment = Class(name="grammar::features::StarNonContainment")
grammar_features_CompoundStar = Class(name="grammar::features::CompoundStar")
grammar_features_MandatoryNonContainment = Class(name="grammar::features::MandatoryNonContainment")
grammar_features_PlusNonContainment = Class(name="grammar::features::PlusNonContainment")
grammar_features_CompoundPlus = Class(name="grammar::features::CompoundPlus")
grammar_features_CompoundOptional = Class(name="grammar::features::CompoundOptional")
grammar_features_ClassWithAttributes = Class(name="grammar::features::ClassWithAttributes")
grammar_features_SecondRoot = Class(name="grammar::features::SecondRoot")
grammar_features_OptionalPrefix = Class(name="grammar::features::OptionalPrefix")
grammar_features_StarPrefix = Class(name="grammar::features::StarPrefix")
grammar_features_PlusPrefix = Class(name="grammar::features::PlusPrefix")

# grammar_features_AbstractSuperclass class attributes and methods

# grammar_features_ConcreteSubclassA class attributes and methods

# AbstractSuperclass class attributes and methods

# grammar_features_Root class attributes and methods

# grammar_features_Child class attributes and methods

# grammar_features_AlternativeSyntax class attributes and methods

# Child class attributes and methods

# grammar_features_ConcreteSubclassB class attributes and methods

# grammar_features_OptionalContainment class attributes and methods

# grammar_features_X class attributes and methods
grammar_features_X_name: Property = Property(name="name", type=StringType)
grammar_features_X.attributes={grammar_features_X_name}

# grammar_features_MandatoryContainment class attributes and methods

# grammar_features_OptionalNonContainment class attributes and methods

# grammar_features_PlusContainment class attributes and methods

# grammar_features_StarContainment class attributes and methods

# grammar_features_StarNonContainment class attributes and methods

# grammar_features_CompoundStar class attributes and methods

# grammar_features_MandatoryNonContainment class attributes and methods

# grammar_features_PlusNonContainment class attributes and methods

# grammar_features_CompoundPlus class attributes and methods

# grammar_features_CompoundOptional class attributes and methods

# grammar_features_ClassWithAttributes class attributes and methods
grammar_features_ClassWithAttributes_a1: Property = Property(name="a1", type=StringType)
grammar_features_ClassWithAttributes_a2: Property = Property(name="a2", type=BooleanType)
grammar_features_ClassWithAttributes.attributes={grammar_features_ClassWithAttributes_a1, grammar_features_ClassWithAttributes_a2}

# grammar_features_SecondRoot class attributes and methods

# grammar_features_OptionalPrefix class attributes and methods

# grammar_features_StarPrefix class attributes and methods

# grammar_features_PlusPrefix class attributes and methods

# Relationships
children0: BinaryAssociation = BinaryAssociation(
    name="children0",
    ends={
        Property(name="grammar_features_Child", type=grammar_features_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="grammar_features_Root", type=grammar_features_Child, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reference2: BinaryAssociation = BinaryAssociation(
    name="reference2",
    ends={
        Property(name="grammar_features_X3", type=grammar_features_MandatoryContainment, multiplicity=Multiplicity(1, 1)),
        Property(name="grammar_features_MandatoryContainment", type=grammar_features_X, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reference1: BinaryAssociation = BinaryAssociation(
    name="reference1",
    ends={
        Property(name="grammar_features_X", type=grammar_features_OptionalContainment, multiplicity=Multiplicity(1, 1)),
        Property(name="grammar_features_OptionalContainment", type=grammar_features_X, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reference4: BinaryAssociation = BinaryAssociation(
    name="reference4",
    ends={
        Property(name="grammar_features_X5", type=grammar_features_PlusContainment, multiplicity=Multiplicity(1, 1)),
        Property(name="grammar_features_PlusContainment", type=grammar_features_X, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
reference6: BinaryAssociation = BinaryAssociation(
    name="reference6",
    ends={
        Property(name="grammar_features_X7", type=grammar_features_StarContainment, multiplicity=Multiplicity(1, 1)),
        Property(name="grammar_features_StarContainment", type=grammar_features_X, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reference14: BinaryAssociation = BinaryAssociation(
    name="reference14",
    ends={
        Property(name="grammar_features_X15", type=grammar_features_StarNonContainment, multiplicity=Multiplicity(1, 1)),
        Property(name="grammar_features_StarNonContainment", type=grammar_features_X, multiplicity=Multiplicity(0, 9999))
    }
)
reference8: BinaryAssociation = BinaryAssociation(
    name="reference8",
    ends={
        Property(name="grammar_features_X9", type=grammar_features_OptionalNonContainment, multiplicity=Multiplicity(1, 1)),
        Property(name="grammar_features_OptionalNonContainment", type=grammar_features_X, multiplicity=Multiplicity(0, 1))
    }
)
reference10: BinaryAssociation = BinaryAssociation(
    name="reference10",
    ends={
        Property(name="grammar_features_X11", type=grammar_features_MandatoryNonContainment, multiplicity=Multiplicity(1, 1)),
        Property(name="grammar_features_MandatoryNonContainment", type=grammar_features_X, multiplicity=Multiplicity(1, 1))
    }
)
reference12: BinaryAssociation = BinaryAssociation(
    name="reference12",
    ends={
        Property(name="grammar_features_X13", type=grammar_features_PlusNonContainment, multiplicity=Multiplicity(1, 1)),
        Property(name="grammar_features_PlusNonContainment", type=grammar_features_X, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_grammar_features_AbstractSuperclass_Child = Generalization(general=Child, specific=grammar_features_AbstractSuperclass)
gen_grammar_features_AlternativeSyntax_Child = Generalization(general=Child, specific=grammar_features_AlternativeSyntax)
gen_grammar_features_ConcreteSubclassA_AbstractSuperclass = Generalization(general=AbstractSuperclass, specific=grammar_features_ConcreteSubclassA)
gen_grammar_features_ConcreteSubclassB_AbstractSuperclass = Generalization(general=AbstractSuperclass, specific=grammar_features_ConcreteSubclassB)
gen_grammar_features_OptionalContainment_Child = Generalization(general=Child, specific=grammar_features_OptionalContainment)
gen_grammar_features_MandatoryContainment_Child = Generalization(general=Child, specific=grammar_features_MandatoryContainment)
gen_grammar_features_OptionalNonContainment_Child = Generalization(general=Child, specific=grammar_features_OptionalNonContainment)
gen_grammar_features_PlusContainment_Child = Generalization(general=Child, specific=grammar_features_PlusContainment)
gen_grammar_features_StarContainment_Child = Generalization(general=Child, specific=grammar_features_StarContainment)
gen_grammar_features_StarNonContainment_Child = Generalization(general=Child, specific=grammar_features_StarNonContainment)
gen_grammar_features_MandatoryNonContainment_Child = Generalization(general=Child, specific=grammar_features_MandatoryNonContainment)
gen_grammar_features_PlusNonContainment_Child = Generalization(general=Child, specific=grammar_features_PlusNonContainment)
gen_grammar_features_CompoundStar_Child = Generalization(general=Child, specific=grammar_features_CompoundStar)
gen_grammar_features_CompoundPlus_Child = Generalization(general=Child, specific=grammar_features_CompoundPlus)
gen_grammar_features_CompoundOptional_Child = Generalization(general=Child, specific=grammar_features_CompoundOptional)
gen_grammar_features_ClassWithAttributes_Child = Generalization(general=Child, specific=grammar_features_ClassWithAttributes)
gen_grammar_features_OptionalPrefix_Child = Generalization(general=Child, specific=grammar_features_OptionalPrefix)
gen_grammar_features_StarPrefix_Child = Generalization(general=Child, specific=grammar_features_StarPrefix)
gen_grammar_features_PlusPrefix_Child = Generalization(general=Child, specific=grammar_features_PlusPrefix)

# Domain Model
domain_model = DomainModel(
    name="grammar_features",
    types={grammar_features_AbstractSuperclass, grammar_features_ConcreteSubclassA, AbstractSuperclass, grammar_features_Root, grammar_features_Child, grammar_features_AlternativeSyntax, Child, grammar_features_ConcreteSubclassB, grammar_features_OptionalContainment, grammar_features_X, grammar_features_MandatoryContainment, grammar_features_OptionalNonContainment, grammar_features_PlusContainment, grammar_features_StarContainment, grammar_features_StarNonContainment, grammar_features_CompoundStar, grammar_features_MandatoryNonContainment, grammar_features_PlusNonContainment, grammar_features_CompoundPlus, grammar_features_CompoundOptional, grammar_features_ClassWithAttributes, grammar_features_SecondRoot, grammar_features_OptionalPrefix, grammar_features_StarPrefix, grammar_features_PlusPrefix},
    associations={children0, reference2, reference1, reference4, reference6, reference14, reference8, reference10, reference12},
    generalizations={gen_grammar_features_AbstractSuperclass_Child, gen_grammar_features_AlternativeSyntax_Child, gen_grammar_features_ConcreteSubclassA_AbstractSuperclass, gen_grammar_features_ConcreteSubclassB_AbstractSuperclass, gen_grammar_features_OptionalContainment_Child, gen_grammar_features_MandatoryContainment_Child, gen_grammar_features_OptionalNonContainment_Child, gen_grammar_features_PlusContainment_Child, gen_grammar_features_StarContainment_Child, gen_grammar_features_StarNonContainment_Child, gen_grammar_features_MandatoryNonContainment_Child, gen_grammar_features_PlusNonContainment_Child, gen_grammar_features_CompoundStar_Child, gen_grammar_features_CompoundPlus_Child, gen_grammar_features_CompoundOptional_Child, gen_grammar_features_ClassWithAttributes_Child, gen_grammar_features_OptionalPrefix_Child, gen_grammar_features_StarPrefix_Child, gen_grammar_features_PlusPrefix_Child},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)