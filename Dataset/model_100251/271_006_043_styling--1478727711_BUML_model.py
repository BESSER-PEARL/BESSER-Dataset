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
FontOption: Enumeration = Enumeration(
    name="FontOption",
    literals={
            EnumerationLiteral(name="ITALIC"),
			EnumerationLiteral(name="BOLD"),
			EnumerationLiteral(name="UNDERLINE"),
			EnumerationLiteral(name="STRIKE")
    }
)

# Classes
Styling_StylingModel = Class(name="Styling_StylingModel")
Styling_CaseStyle = Class(name="Styling_CaseStyle", is_abstract=True)
Styling_Pattern = Class(name="Styling_Pattern", is_abstract=True)
Styling_Default = Class(name="Styling_Default")
Styling_StylingPredicate = Class(name="Styling_StylingPredicate")
CaseStyle = Class(name="CaseStyle")
Styling_IPredicate = Class(name="Styling_IPredicate")
Styling_Segment = Class(name="Styling_Segment")
Styling_Style = Class(name="Styling_Style")
Styling_Icon = Class(name="Styling_Icon")
Styling_Styling = Class(name="Styling_Styling")
Styling_ConstantPattern = Class(name="Styling_ConstantPattern")
Pattern = Class(name="Pattern")
Styling_StringParameter = Class(name="Styling_StringParameter")
Styling_ModelPattern = Class(name="Styling_ModelPattern")
Styling_OperationPattern = Class(name="Styling_OperationPattern")
Styling_Parameter = Class(name="Styling_Parameter", is_abstract=True)
Styling_IntParameter = Class(name="Styling_IntParameter")
Parameter_ = Class(name="Parameter")
Styling_BooleanParameter = Class(name="Styling_BooleanParameter")
Styling_EObjectParameter = Class(name="Styling_EObjectParameter")
Styling_EObject = Class(name="Styling_EObject")

# Styling_StylingModel class attributes and methods
Styling_StylingModel_modeName: Property = Property(name="modeName", type=StringType)
Styling_StylingModel.attributes={Styling_StylingModel_modeName}

# Styling_CaseStyle class attributes and methods
Styling_CaseStyle_m_getStyledString: Method = Method(name="getStyledString", parameters={Parameter(name='Styling_object', type=StringType)}, type=StringType)
Styling_CaseStyle_m_getImage: Method = Method(name="getImage", parameters={}, type=StringType)
Styling_CaseStyle.methods={Styling_CaseStyle_m_getImage, Styling_CaseStyle_m_getStyledString}

# Styling_Pattern class attributes and methods
Styling_Pattern_m_getPattern: Method = Method(name="getPattern", parameters={}, type=StringType)
Styling_Pattern_m_getPatternValue: Method = Method(name="getPatternValue", parameters={Parameter(name='Styling_object', type=StringType)}, type=StringType)
Styling_Pattern.methods={Styling_Pattern_m_getPattern, Styling_Pattern_m_getPatternValue}

# Styling_Default class attributes and methods

# Styling_StylingPredicate class attributes and methods

# CaseStyle class attributes and methods

# Styling_IPredicate class attributes and methods

# Styling_Segment class attributes and methods
Styling_Segment_m_getColor: Method = Method(name="getColor", parameters={}, type=StringType)
Styling_Segment_m_getFont: Method = Method(name="getFont", parameters={}, type=StringType)
Styling_Segment_m_setColor: Method = Method(name="setColor", parameters={Parameter(name='Styling_color', type=StringType)})
Styling_Segment.methods={Styling_Segment_m_setColor, Styling_Segment_m_getFont, Styling_Segment_m_getColor}

# Styling_Style class attributes and methods
Styling_Style_appliedFonts: Property = Property(name="appliedFonts", type=StringType)
Styling_Style_color: Property = Property(name="color", type=StringType)
Styling_Style.attributes={Styling_Style_appliedFonts, Styling_Style_color}

# Styling_Icon class attributes and methods
Styling_Icon_image: Property = Property(name="image", type=StringType)
Styling_Icon.attributes={Styling_Icon_image}

# Styling_Styling class attributes and methods

# Styling_ConstantPattern class attributes and methods
Styling_ConstantPattern_value: Property = Property(name="value", type=StringType)
Styling_ConstantPattern.attributes={Styling_ConstantPattern_value}

# Pattern class attributes and methods

# Styling_StringParameter class attributes and methods
Styling_StringParameter_value: Property = Property(name="value", type=StringType)
Styling_StringParameter.attributes={Styling_StringParameter_value}

# Styling_ModelPattern class attributes and methods
Styling_ModelPattern_attributeName: Property = Property(name="attributeName", type=StringType)
Styling_ModelPattern.attributes={Styling_ModelPattern_attributeName}

# Styling_OperationPattern class attributes and methods
Styling_OperationPattern_operation: Property = Property(name="operation", type=StringType)
Styling_OperationPattern.attributes={Styling_OperationPattern_operation}

# Styling_Parameter class attributes and methods
Styling_Parameter_name: Property = Property(name="name", type=StringType)
Styling_Parameter_m_getObjectValue: Method = Method(name="getObjectValue", parameters={}, type=StringType)
Styling_Parameter.attributes={Styling_Parameter_name}
Styling_Parameter.methods={Styling_Parameter_m_getObjectValue}

# Styling_IntParameter class attributes and methods
Styling_IntParameter_value: Property = Property(name="value", type=IntegerType)
Styling_IntParameter.attributes={Styling_IntParameter_value}

# Parameter class attributes and methods

# Styling_BooleanParameter class attributes and methods
Styling_BooleanParameter_value: Property = Property(name="value", type=BooleanType)
Styling_BooleanParameter.attributes={Styling_BooleanParameter_value}

# Styling_EObjectParameter class attributes and methods

# Styling_EObject class attributes and methods

# Relationships
styles0: BinaryAssociation = BinaryAssociation(
    name="styles0",
    ends={
        Property(name="Styling_CaseStyle", type=Styling_StylingModel, multiplicity=Multiplicity(1, 1)),
        Property(name="Styling_StylingModel", type=Styling_CaseStyle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
default1: BinaryAssociation = BinaryAssociation(
    name="default1",
    ends={
        Property(name="Styling_Default", type=Styling_StylingModel, multiplicity=Multiplicity(1, 1)),
        Property(name="Styling_StylingModel2", type=Styling_Default, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
predicate3: BinaryAssociation = BinaryAssociation(
    name="predicate3",
    ends={
        Property(name="Styling_IPredicate", type=Styling_StylingPredicate, multiplicity=Multiplicity(1, 1)),
        Property(name="Styling_StylingPredicate", type=Styling_IPredicate, multiplicity=Multiplicity(0, 1))
    }
)
style4: BinaryAssociation = BinaryAssociation(
    name="style4",
    ends={
        Property(name="Styling_Style", type=Styling_Segment, multiplicity=Multiplicity(1, 1)),
        Property(name="Styling_Segment", type=Styling_Style, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
pattern5: BinaryAssociation = BinaryAssociation(
    name="pattern5",
    ends={
        Property(name="Styling_Pattern", type=Styling_Segment, multiplicity=Multiplicity(1, 1)),
        Property(name="Styling_Segment6", type=Styling_Pattern, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
segments7: BinaryAssociation = BinaryAssociation(
    name="segments7",
    ends={
        Property(name="Styling_Segment9", type=Styling_CaseStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="Styling_CaseStyle8", type=Styling_Segment, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
icon10: BinaryAssociation = BinaryAssociation(
    name="icon10",
    ends={
        Property(name="Styling_Icon", type=Styling_CaseStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="Styling_CaseStyle11", type=Styling_Icon, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
models12: BinaryAssociation = BinaryAssociation(
    name="models12",
    ends={
        Property(name="Styling_StylingModel13", type=Styling_Styling, multiplicity=Multiplicity(1, 1)),
        Property(name="Styling_Styling", type=Styling_StylingModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters14: BinaryAssociation = BinaryAssociation(
    name="parameters14",
    ends={
        Property(name="Styling_Parameter", type=Styling_OperationPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="Styling_OperationPattern", type=Styling_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value15: BinaryAssociation = BinaryAssociation(
    name="value15",
    ends={
        Property(name="Styling_EObject", type=Styling_EObjectParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="Styling_EObjectParameter", type=Styling_EObject, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_Styling_StylingPredicate_CaseStyle = Generalization(general=CaseStyle, specific=Styling_StylingPredicate)
gen_Styling_Default_CaseStyle = Generalization(general=CaseStyle, specific=Styling_Default)
gen_Styling_ConstantPattern_Pattern = Generalization(general=Pattern, specific=Styling_ConstantPattern)
gen_Styling_ModelPattern_Pattern = Generalization(general=Pattern, specific=Styling_ModelPattern)
gen_Styling_OperationPattern_Pattern = Generalization(general=Pattern, specific=Styling_OperationPattern)
gen_Styling_IntParameter_Parameter = Generalization(general=Parameter_, specific=Styling_IntParameter)
gen_Styling_BooleanParameter_Parameter = Generalization(general=Parameter_, specific=Styling_BooleanParameter)
gen_Styling_StringParameter_Parameter = Generalization(general=Parameter_, specific=Styling_StringParameter)
gen_Styling_EObjectParameter_Parameter = Generalization(general=Parameter_, specific=Styling_EObjectParameter)

# Domain Model
domain_model = DomainModel(
    name="Styling",
    types={Styling_StylingModel, Styling_CaseStyle, Styling_Pattern, Styling_Default, Styling_StylingPredicate, CaseStyle, Styling_IPredicate, Styling_Segment, Styling_Style, Styling_Icon, Styling_Styling, Styling_ConstantPattern, Pattern, Styling_StringParameter, Styling_ModelPattern, Styling_OperationPattern, Styling_Parameter, Styling_IntParameter, Parameter_, Styling_BooleanParameter, Styling_EObjectParameter, Styling_EObject, FontOption},
    associations={styles0, default1, predicate3, style4, pattern5, segments7, icon10, models12, parameters14, value15},
    generalizations={gen_Styling_StylingPredicate_CaseStyle, gen_Styling_Default_CaseStyle, gen_Styling_ConstantPattern_Pattern, gen_Styling_ModelPattern_Pattern, gen_Styling_OperationPattern_Pattern, gen_Styling_IntParameter_Parameter, gen_Styling_BooleanParameter_Parameter, gen_Styling_StringParameter_Parameter, gen_Styling_EObjectParameter_Parameter},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)