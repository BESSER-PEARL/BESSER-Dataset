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
Visibility: Enumeration = Enumeration(
    name="Visibility",
    literals={
            EnumerationLiteral(name="unspecified"),
			EnumerationLiteral(name="public"),
			EnumerationLiteral(name="private"),
			EnumerationLiteral(name="protected"),
			EnumerationLiteral(name="package")
    }
)

AssociationType: Enumeration = Enumeration(
    name="AssociationType",
    literals={
            EnumerationLiteral(name="simpleAssociation"),
			EnumerationLiteral(name="aggregation"),
			EnumerationLiteral(name="composition")
    }
)

# Classes
yuml_Model = Class(name="yuml::Model")
yuml_ModelElement = Class(name="yuml::ModelElement", is_abstract=True)
yuml_ColorableElement = Class(name="yuml::ColorableElement", is_abstract=True)
ModelElement = Class(name="ModelElement")
yuml_Inheritance = Class(name="yuml::Inheritance")
yuml_Class = Class(name="yuml::Class")
ColorableElement = Class(name="ColorableElement")
yuml_Attribute = Class(name="yuml::Attribute")
yuml_Method = Class(name="yuml::Method")
yuml_Relationship = Class(name="yuml::Relationship", is_abstract=True)
yuml_Association = Class(name="yuml::Association")
Relationship = Class(name="Relationship")
yuml_Cardinality = Class(name="yuml::Cardinality")
yuml_ClassMember = Class(name="yuml::ClassMember", is_abstract=True)
ClassMember = Class(name="ClassMember")
yuml_Note = Class(name="yuml::Note")
yuml_NoteAssociation = Class(name="yuml::NoteAssociation")
yuml_Equivalence = Class(name="yuml::Equivalence")

# yuml_Model class attributes and methods

# yuml_ModelElement class attributes and methods

# yuml_ColorableElement class attributes and methods
yuml_ColorableElement_color: Property = Property(name="color", type=StringType)
yuml_ColorableElement.attributes={yuml_ColorableElement_color}

# ModelElement class attributes and methods

# yuml_Inheritance class attributes and methods

# yuml_Class class attributes and methods
yuml_Class_stereotype: Property = Property(name="stereotype", type=StringType)
yuml_Class_name: Property = Property(name="name", type=StringType)
yuml_Class.attributes={yuml_Class_name, yuml_Class_stereotype}

# ColorableElement class attributes and methods

# yuml_Attribute class attributes and methods
yuml_Attribute_stereotype: Property = Property(name="stereotype", type=StringType)
yuml_Attribute_type: Property = Property(name="type", type=StringType)
yuml_Attribute.attributes={yuml_Attribute_stereotype, yuml_Attribute_type}

# yuml_Method class attributes and methods
yuml_Method_arguments: Property = Property(name="arguments", type=StringType)
yuml_Method.attributes={yuml_Method_arguments}

# yuml_Relationship class attributes and methods
yuml_Relationship_sourceLabel: Property = Property(name="sourceLabel", type=StringType)
yuml_Relationship_targetLabel: Property = Property(name="targetLabel", type=StringType)
yuml_Relationship.attributes={yuml_Relationship_targetLabel, yuml_Relationship_sourceLabel}

# yuml_Association class attributes and methods
yuml_Association_sourceVisibility: Property = Property(name="sourceVisibility", type=StringType)
yuml_Association_navigableTarget: Property = Property(name="navigableTarget", type=BooleanType)
yuml_Association_targetVisibility: Property = Property(name="targetVisibility", type=StringType)
yuml_Association_type: Property = Property(name="type", type=StringType)
yuml_Association_navigableSource: Property = Property(name="navigableSource", type=BooleanType)
yuml_Association.attributes={yuml_Association_navigableTarget, yuml_Association_navigableSource, yuml_Association_targetVisibility, yuml_Association_type, yuml_Association_sourceVisibility}

# Relationship class attributes and methods

# yuml_Cardinality class attributes and methods
yuml_Cardinality_lowerBound: Property = Property(name="lowerBound", type=StringType)
yuml_Cardinality_upperBound: Property = Property(name="upperBound", type=StringType)
yuml_Cardinality.attributes={yuml_Cardinality_upperBound, yuml_Cardinality_lowerBound}

# yuml_ClassMember class attributes and methods
yuml_ClassMember_visibility: Property = Property(name="visibility", type=StringType)
yuml_ClassMember_name: Property = Property(name="name", type=StringType)
yuml_ClassMember.attributes={yuml_ClassMember_name, yuml_ClassMember_visibility}

# ClassMember class attributes and methods

# yuml_Note class attributes and methods
yuml_Note_text: Property = Property(name="text", type=StringType)
yuml_Note.attributes={yuml_Note_text}

# yuml_NoteAssociation class attributes and methods

# yuml_Equivalence class attributes and methods

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="yuml_ModelElement", type=yuml_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="yuml_Model", type=yuml_ModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetCardinality9: BinaryAssociation = BinaryAssociation(
    name="targetCardinality9",
    ends={
        Property(name="yuml_Cardinality11", type=yuml_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="yuml_Association10", type=yuml_Cardinality, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes1: BinaryAssociation = BinaryAssociation(
    name="attributes1",
    ends={
        Property(name="yuml_Attribute", type=yuml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="yuml_Class", type=yuml_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods2: BinaryAssociation = BinaryAssociation(
    name="methods2",
    ends={
        Property(name="yuml_Method", type=yuml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="yuml_Class3", type=yuml_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source4: BinaryAssociation = BinaryAssociation(
    name="source4",
    ends={
        Property(name="yuml_Class5", type=yuml_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="yuml_Relationship", type=yuml_Class, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="yuml_ColorableElement", type=yuml_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="yuml_Relationship7", type=yuml_ColorableElement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sourceCardinality8: BinaryAssociation = BinaryAssociation(
    name="sourceCardinality8",
    ends={
        Property(name="yuml_Cardinality", type=yuml_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="yuml_Association", type=yuml_Cardinality, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
note12: BinaryAssociation = BinaryAssociation(
    name="note12",
    ends={
        Property(name="yuml_Note", type=yuml_NoteAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="yuml_NoteAssociation", type=yuml_Note, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_yuml_ColorableElement_ModelElement = Generalization(general=ModelElement, specific=yuml_ColorableElement)
gen_yuml_Inheritance_Relationship = Generalization(general=Relationship, specific=yuml_Inheritance)
gen_yuml_Class_ColorableElement = Generalization(general=ColorableElement, specific=yuml_Class)
gen_yuml_Relationship_ModelElement = Generalization(general=ModelElement, specific=yuml_Relationship)
gen_yuml_Association_Relationship = Generalization(general=Relationship, specific=yuml_Association)
gen_yuml_Attribute_ClassMember = Generalization(general=ClassMember, specific=yuml_Attribute)
gen_yuml_Method_ClassMember = Generalization(general=ClassMember, specific=yuml_Method)
gen_yuml_Note_ColorableElement = Generalization(general=ColorableElement, specific=yuml_Note)
gen_yuml_NoteAssociation_Relationship = Generalization(general=Relationship, specific=yuml_NoteAssociation)
gen_yuml_Equivalence_Relationship = Generalization(general=Relationship, specific=yuml_Equivalence)

# Domain Model
domain_model = DomainModel(
    name="yuml",
    types={yuml_Model, yuml_ModelElement, yuml_ColorableElement, ModelElement, yuml_Inheritance, yuml_Class, ColorableElement, yuml_Attribute, yuml_Method, yuml_Relationship, yuml_Association, Relationship, yuml_Cardinality, yuml_ClassMember, ClassMember, yuml_Note, yuml_NoteAssociation, yuml_Equivalence, Visibility, AssociationType},
    associations={elements0, targetCardinality9, attributes1, methods2, source4, target6, sourceCardinality8, note12},
    generalizations={gen_yuml_ColorableElement_ModelElement, gen_yuml_Inheritance_Relationship, gen_yuml_Class_ColorableElement, gen_yuml_Relationship_ModelElement, gen_yuml_Association_Relationship, gen_yuml_Attribute_ClassMember, gen_yuml_Method_ClassMember, gen_yuml_Note_ColorableElement, gen_yuml_NoteAssociation_Relationship, gen_yuml_Equivalence_Relationship},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)