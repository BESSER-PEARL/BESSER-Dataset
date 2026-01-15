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
Scale: Enumeration = Enumeration(
    name="Scale",
    literals={
            EnumerationLiteral(name="nothing"),
			EnumerationLiteral(name="one"),
			EnumerationLiteral(name="two"),
			EnumerationLiteral(name="three"),
			EnumerationLiteral(name="four")
    }
)

# Classes
relationpattern_ThingA = Class(name="relationpattern::ThingA")
SourceNode = Class(name="SourceNode")
NamedElement = Class(name="NamedElement")
relationpattern_RelatedTo = Class(name="relationpattern::RelatedTo")
Arrow = Class(name="Arrow")
relationpattern_ThingB = Class(name="relationpattern::ThingB")
TargetNode = Class(name="TargetNode")
relationpattern_SourceNode = Class(name="relationpattern::SourceNode", is_abstract=True)
relationpattern_World = Class(name="relationpattern::World")
Category = Class(name="Category")
relationpattern_Category = Class(name="relationpattern::Category", is_abstract=True)
relationpattern_Arrow = Class(name="relationpattern::Arrow", is_abstract=True)
relationpattern_TargetNode = Class(name="relationpattern::TargetNode", is_abstract=True)
relationpattern_NamedElement = Class(name="relationpattern::NamedElement")

# relationpattern_ThingA class attributes and methods
relationpattern_ThingA_since: Property = Property(name="since", type=DateType)
relationpattern_ThingA_m_compare: Method = Method(name="compare", parameters={Parameter(name='personne')}, type=IntegerType)
relationpattern_ThingA_m_pred: Method = Method(name="pred", parameters={}, type=StringType)
relationpattern_ThingA_m_succ: Method = Method(name="succ", parameters={}, type=StringType)
relationpattern_ThingA.attributes={relationpattern_ThingA_since}
relationpattern_ThingA.methods={relationpattern_ThingA_m_pred, relationpattern_ThingA_m_compare, relationpattern_ThingA_m_succ}

# SourceNode class attributes and methods

# NamedElement class attributes and methods

# relationpattern_RelatedTo class attributes and methods
relationpattern_RelatedTo_m_validate: Method = Method(name="validate", parameters={}, type=BooleanType)
relationpattern_RelatedTo.methods={relationpattern_RelatedTo_m_validate}

# Arrow class attributes and methods

# relationpattern_ThingB class attributes and methods
relationpattern_ThingB_step: Property = Property(name="step", type=StringType)
relationpattern_ThingB_m_compare: Method = Method(name="compare", parameters={Parameter(name='role')}, type=IntegerType)
relationpattern_ThingB_m_pred: Method = Method(name="pred", parameters={}, type=StringType)
relationpattern_ThingB_m_succ: Method = Method(name="succ", parameters={}, type=StringType)
relationpattern_ThingB.attributes={relationpattern_ThingB_step}
relationpattern_ThingB.methods={relationpattern_ThingB_m_succ, relationpattern_ThingB_m_pred, relationpattern_ThingB_m_compare}

# TargetNode class attributes and methods

# relationpattern_SourceNode class attributes and methods
relationpattern_SourceNode_m_compare: Method = Method(name="compare", parameters={Parameter(name='noeud')}, type=IntegerType)
relationpattern_SourceNode_m_pred: Method = Method(name="pred", parameters={}, type=SourceNode)
relationpattern_SourceNode_m_succ: Method = Method(name="succ", parameters={}, type=SourceNode)
relationpattern_SourceNode.methods={relationpattern_SourceNode_m_succ, relationpattern_SourceNode_m_pred, relationpattern_SourceNode_m_compare}

# relationpattern_World class attributes and methods
relationpattern_World_m_affectation: Method = Method(name="affectation", parameters={Parameter(name='personne'), Parameter(name='role')}, type=StringType)
relationpattern_World_m_affectationInterval: Method = Method(name="affectationInterval", parameters={Parameter(name='thingb')}, type=StringType)
relationpattern_World_m_compare: Method = Method(name="compare", parameters={Parameter(name='role2'), Parameter(name='role1')}, type=IntegerType)
relationpattern_World_m_compare: Method = Method(name="compare", parameters={Parameter(name='personne1'), Parameter(name='personne2')}, type=IntegerType)
relationpattern_World.methods={relationpattern_World_m_affectation, relationpattern_World_m_compare, relationpattern_World_m_affectationInterval, relationpattern_World_m_compare}

# Category class attributes and methods

# relationpattern_Category class attributes and methods
relationpattern_Category_nom: Property = Property(name="nom", type=StringType)
relationpattern_Category_m_compare: Method = Method(name="compare", parameters={Parameter(name='n1'), Parameter(name='n2')}, type=IntegerType)
relationpattern_Category_m_compare: Method = Method(name="compare", parameters={Parameter(name='n2'), Parameter(name='n1')}, type=IntegerType)
relationpattern_Category_m_affectationInterval: Method = Method(name="affectationInterval", parameters={Parameter(name='target')}, type=SourceNode)
relationpattern_Category_m_affectation: Method = Method(name="affectation", parameters={Parameter(name='source'), Parameter(name='cible')}, type=Arrow)
relationpattern_Category.attributes={relationpattern_Category_nom}
relationpattern_Category.methods={relationpattern_Category_m_compare, relationpattern_Category_m_compare, relationpattern_Category_m_affectation, relationpattern_Category_m_affectationInterval}

# relationpattern_Arrow class attributes and methods
relationpattern_Arrow_m_validate: Method = Method(name="validate", parameters={}, type=BooleanType)
relationpattern_Arrow.methods={relationpattern_Arrow_m_validate}

# relationpattern_TargetNode class attributes and methods
relationpattern_TargetNode_m_compare: Method = Method(name="compare", parameters={Parameter(name='noeud')}, type=IntegerType)
relationpattern_TargetNode_m_pred: Method = Method(name="pred", parameters={}, type=TargetNode)
relationpattern_TargetNode_m_succ: Method = Method(name="succ", parameters={}, type=TargetNode)
relationpattern_TargetNode.methods={relationpattern_TargetNode_m_succ, relationpattern_TargetNode_m_compare, relationpattern_TargetNode_m_pred}

# relationpattern_NamedElement class attributes and methods
relationpattern_NamedElement_name: Property = Property(name="name", type=StringType)
relationpattern_NamedElement.attributes={relationpattern_NamedElement_name}

# Relationships
thingA0: BinaryAssociation = BinaryAssociation(
    name="thingA0",
    ends={
        Property(name="relationpattern_ThingA", type=relationpattern_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="relationpattern_RelatedTo", type=relationpattern_ThingA, multiplicity=Multiplicity(0, 1))
    }
)
thingsa3: BinaryAssociation = BinaryAssociation(
    name="thingsa3",
    ends={
        Property(name="relationpattern_ThingA4", type=relationpattern_World, multiplicity=Multiplicity(1, 1)),
        Property(name="relationpattern_World", type=relationpattern_ThingA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thingsb5: BinaryAssociation = BinaryAssociation(
    name="thingsb5",
    ends={
        Property(name="relationpattern_ThingB7", type=relationpattern_World, multiplicity=Multiplicity(1, 1)),
        Property(name="relationpattern_World6", type=relationpattern_ThingB, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations8: BinaryAssociation = BinaryAssociation(
    name="relations8",
    ends={
        Property(name="relationpattern_RelatedTo10", type=relationpattern_World, multiplicity=Multiplicity(1, 1)),
        Property(name="relationpattern_World9", type=relationpattern_RelatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thingB1: BinaryAssociation = BinaryAssociation(
    name="thingB1",
    ends={
        Property(name="relationpattern_ThingB", type=relationpattern_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="relationpattern_RelatedTo2", type=relationpattern_ThingB, multiplicity=Multiplicity(0, 1))
    }
)
sources14: BinaryAssociation = BinaryAssociation(
    name="sources14",
    ends={
        Property(name="relationpattern_SourceNode15", type=relationpattern_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="relationpattern_Category", type=relationpattern_SourceNode, multiplicity=Multiplicity(0, 9999))
    }
)
source11: BinaryAssociation = BinaryAssociation(
    name="source11",
    ends={
        Property(name="relationpattern_SourceNode", type=relationpattern_Arrow, multiplicity=Multiplicity(1, 1)),
        Property(name="relationpattern_Arrow", type=relationpattern_SourceNode, multiplicity=Multiplicity(0, 1))
    }
)
cible12: BinaryAssociation = BinaryAssociation(
    name="cible12",
    ends={
        Property(name="relationpattern_TargetNode", type=relationpattern_Arrow, multiplicity=Multiplicity(1, 1)),
        Property(name="relationpattern_Arrow13", type=relationpattern_TargetNode, multiplicity=Multiplicity(0, 1))
    }
)
fleches16: BinaryAssociation = BinaryAssociation(
    name="fleches16",
    ends={
        Property(name="relationpattern_Arrow18", type=relationpattern_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="relationpattern_Category17", type=relationpattern_Arrow, multiplicity=Multiplicity(0, 9999))
    }
)
targets19: BinaryAssociation = BinaryAssociation(
    name="targets19",
    ends={
        Property(name="relationpattern_TargetNode21", type=relationpattern_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="relationpattern_Category20", type=relationpattern_TargetNode, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_relationpattern_ThingA_SourceNode = Generalization(general=SourceNode, specific=relationpattern_ThingA)
gen_relationpattern_ThingA_NamedElement = Generalization(general=NamedElement, specific=relationpattern_ThingA)
gen_relationpattern_RelatedTo_Arrow = Generalization(general=Arrow, specific=relationpattern_RelatedTo)
gen_relationpattern_RelatedTo_NamedElement = Generalization(general=NamedElement, specific=relationpattern_RelatedTo)
gen_relationpattern_ThingB_TargetNode = Generalization(general=TargetNode, specific=relationpattern_ThingB)
gen_relationpattern_ThingB_NamedElement = Generalization(general=NamedElement, specific=relationpattern_ThingB)
gen_relationpattern_World_Category = Generalization(general=Category, specific=relationpattern_World)

# Domain Model
domain_model = DomainModel(
    name="relationpattern",
    types={relationpattern_ThingA, SourceNode, NamedElement, relationpattern_RelatedTo, Arrow, relationpattern_ThingB, TargetNode, relationpattern_SourceNode, relationpattern_World, Category, relationpattern_Category, relationpattern_Arrow, relationpattern_TargetNode, relationpattern_NamedElement, Scale},
    associations={thingA0, thingsa3, thingsb5, relations8, thingB1, sources14, source11, cible12, fleches16, targets19},
    generalizations={gen_relationpattern_ThingA_SourceNode, gen_relationpattern_ThingA_NamedElement, gen_relationpattern_RelatedTo_Arrow, gen_relationpattern_RelatedTo_NamedElement, gen_relationpattern_ThingB_TargetNode, gen_relationpattern_ThingB_NamedElement, gen_relationpattern_World_Category},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)