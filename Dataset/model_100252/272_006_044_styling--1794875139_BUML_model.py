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
Styling_Default = Class(name="Styling_Default")
Styling_Basic = Class(name="Styling_Basic")
Styling_StylingPredicate = Class(name="Styling_StylingPredicate")
CaseStyle = Class(name="CaseStyle")
Styling_IPredicate = Class(name="Styling_IPredicate")
Styling_Segment = Class(name="Styling_Segment")
Styling_Pattern = Class(name="Styling_Pattern", is_abstract=True)
Styling_Icon = Class(name="Styling_Icon")
Styling_Style = Class(name="Styling_Style")
Styling_Styling = Class(name="Styling_Styling")
Styling_ModelPattern = Class(name="Styling_ModelPattern")
Styling_OperationPattern = Class(name="Styling_OperationPattern")
Styling_Parameter = Class(name="Styling_Parameter", is_abstract=True)
Styling_IntParameter = Class(name="Styling_IntParameter")
Parameter_ = Class(name="Parameter")
Styling_BooleanParameter = Class(name="Styling_BooleanParameter")
Styling_ConstantPattern = Class(name="Styling_ConstantPattern")
Pattern = Class(name="Pattern")
Styling_EObjectParameter = Class(name="Styling_EObjectParameter")
Styling_EObject = Class(name="Styling_EObject")
Styling_StringParameter = Class(name="Styling_StringParameter")

# Styling_StylingModel class attributes and methods
Styling_StylingModel_modeName: Property = Property(name="modeName", type=StringType)
Styling_StylingModel.attributes={Styling_StylingModel_modeName}

# Styling_CaseStyle class attributes and methods
Styling_CaseStyle_m_getStyledString: Method = Method(name="getStyledString", parameters={Parameter(name='Styling_object', type=StringType)}, type=StringType)
Styling_CaseStyle_m_getImage: Method = Method(name="getImage", parameters={}, type=StringType)
Styling_CaseStyle.methods={Styling_CaseStyle_m_getStyledString, Styling_CaseStyle_m_getImage}

# Styling_Default class attributes and methods

# Styling_Basic class attributes and methods

# Styling_StylingPredicate class attributes and methods

# CaseStyle class attributes and methods

# Styling_IPredicate class attributes and methods

# Styling_Segment class attributes and methods
Styling_Segment_m_getColor: Method = Method(name="getColor", parameters={}, type=StringType)
Styling_Segment_m_getFont: Method = Method(name="getFont", parameters={}, type=StringType)
Styling_Segment_m_setColor: Method = Method(name="setColor", parameters={Parameter(name='Styling_color', type=StringType)})
Styling_Segment.methods={Styling_Segment_m_getColor, Styling_Segment_m_getFont, Styling_Segment_m_setColor}

# Styling_Pattern class attributes and methods
Styling_Pattern_m_getPattern: Method = Method(name="getPattern", parameters={}, type=StringType)
Styling_Pattern_m_getPatternValue: Method = Method(name="getPatternValue", parameters={Parameter(name='Styling_object', type=StringType)}, type=StringType)
Styling_Pattern.methods={Styling_Pattern_m_getPattern, Styling_Pattern_m_getPatternValue}

# Styling_Icon class attributes and methods
Styling_Icon_image: Property = Property(name="image", type=StringType)
Styling_Icon.attributes={Styling_Icon_image}

# Styling_Style class attributes and methods
Styling_Style_appliedFonts: Property = Property(name="appliedFonts", type=StringType)
Styling_Style_color: Property = Property(name="color", type=StringType)
Styling_Style.attributes={Styling_Style_color, Styling_Style_appliedFonts}

# Styling_Styling class attributes and methods

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

# Styling_ConstantPattern class attributes and methods
Styling_ConstantPattern_value: Property = Property(name="value", type=StringType)
Styling_ConstantPattern.attributes={Styling_ConstantPattern_value}

# Pattern class attributes and methods

# Styling_EObjectParameter class attributes and methods

# Styling_EObject class attributes and methods

# Styling_StringParameter class attributes and methods
Styling_StringParameter_value: Property = Property(name="value", type=StringType)
Styling_StringParameter.attributes={Styling_StringParameter_value}

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
basic3: BinaryAssociation = BinaryAssociation(
    name="basic3",
    ends={
        Property(name="Styling_Basic", type=Styling_StylingModel, multiplicity=Multiplicity(1, 1)),
        Property(name="Styling_StylingModel4", type=Styling_Basic, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
predicate5: BinaryAssociation = BinaryAssociation(
    name="predicate5",
    ends={
        Property(name="Styling_IPredicate", type=Styling_StylingPredicate, multiplicity=Multiplicity(1, 1)),
        Property(name="Styling_StylingPredicate", type=Styling_IPredicate, multiplicity=Multiplicity(0, 1))
    }
)
style6: BinaryAssociation = BinaryAssociation(
    name="style6",
    ends={
        Property(name="Styling_Style", type=Styling_Segment, multiplicity=Multiplicity(1, 1)),
        Property(name="Styling_Segment", type=Styling_Style, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
pattern7: BinaryAssociation = BinaryAssociation(
    name="pattern7",
    ends={
        Property(name="Styling_Pattern", type=Styling_Segment, multiplicity=Multiplicity(1, 1)),
        Property(name="Styling_Segment8", type=Styling_Pattern, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
segments9: BinaryAssociation = BinaryAssociation(
    name="segments9",
    ends={
        Property(name="Styling_Segment11", type=Styling_CaseStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="Styling_CaseStyle10", type=Styling_Segment, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
models14: BinaryAssociation = BinaryAssociation(
    name="models14",
    ends={
        Property(name="Styling_StylingModel15", type=Styling_Styling, multiplicity=Multiplicity(1, 1)),
        Property(name="Styling_Styling", type=Styling_StylingModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
icon12: BinaryAssociation = BinaryAssociation(
    name="icon12",
    ends={
        Property(name="Styling_Icon", type=Styling_CaseStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="Styling_CaseStyle13", type=Styling_Icon, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters16: BinaryAssociation = BinaryAssociation(
    name="parameters16",
    ends={
        Property(name="Styling_Parameter", type=Styling_OperationPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="Styling_OperationPattern", type=Styling_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value17: BinaryAssociation = BinaryAssociation(
    name="value17",
    ends={
        Property(name="Styling_EObject", type=Styling_EObjectParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="Styling_EObjectParameter", type=Styling_EObject, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_Styling_StylingPredicate_CaseStyle = Generalization(general=CaseStyle, specific=Styling_StylingPredicate)
gen_Styling_Default_CaseStyle = Generalization(general=CaseStyle, specific=Styling_Default)
gen_Styling_ModelPattern_Pattern = Generalization(general=Pattern, specific=Styling_ModelPattern)
gen_Styling_OperationPattern_Pattern = Generalization(general=Pattern, specific=Styling_OperationPattern)
gen_Styling_IntParameter_Parameter = Generalization(general=Parameter_, specific=Styling_IntParameter)
gen_Styling_ConstantPattern_Pattern = Generalization(general=Pattern, specific=Styling_ConstantPattern)
gen_Styling_EObjectParameter_Parameter = Generalization(general=Parameter_, specific=Styling_EObjectParameter)
gen_Styling_Basic_CaseStyle = Generalization(general=CaseStyle, specific=Styling_Basic)
gen_Styling_BooleanParameter_Parameter = Generalization(general=Parameter_, specific=Styling_BooleanParameter)
gen_Styling_StringParameter_Parameter = Generalization(general=Parameter_, specific=Styling_StringParameter)

# Domain Model
domain_model = DomainModel(
    name="Styling",
    types={Styling_StylingModel, Styling_CaseStyle, Styling_Default, Styling_Basic, Styling_StylingPredicate, CaseStyle, Styling_IPredicate, Styling_Segment, Styling_Pattern, Styling_Icon, Styling_Style, Styling_Styling, Styling_ModelPattern, Styling_OperationPattern, Styling_Parameter, Styling_IntParameter, Parameter_, Styling_BooleanParameter, Styling_ConstantPattern, Pattern, Styling_EObjectParameter, Styling_EObject, Styling_StringParameter, FontOption},
    associations={styles0, default1, basic3, predicate5, style6, pattern7, segments9, models14, icon12, parameters16, value17},
    generalizations={gen_Styling_StylingPredicate_CaseStyle, gen_Styling_Default_CaseStyle, gen_Styling_ModelPattern_Pattern, gen_Styling_OperationPattern_Pattern, gen_Styling_IntParameter_Parameter, gen_Styling_ConstantPattern_Pattern, gen_Styling_EObjectParameter_Parameter, gen_Styling_Basic_CaseStyle, gen_Styling_BooleanParameter_Parameter, gen_Styling_StringParameter_Parameter},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)