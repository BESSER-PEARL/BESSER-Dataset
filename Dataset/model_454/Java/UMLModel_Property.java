





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Property extends TemplateableElement, DeploymentTarget, ConnectableElement, StructuralFeature {

    private String subsettedProperty;
    private String owningAssociation;
    private String isDerived;
    private String association;
    private String associationEnd;
    private String opposite;
    private String isComposite;
    private String aggregation;
    private String class_;
    private String datatype;
    private String isDerivedUnion;
    private String default;
    private String redefinedProperty;





    private UMLModel_Artifact umlmodel_artifact;




    private UMLModel_ValueSpecification umlmodel_valuespecification;




    private UMLModel_Property umlmodel_property;




    private UMLModel_Association umlmodel_association;




    private UMLModel_Interface umlmodel_interface;




    private UMLModel_DataType umlmodel_datatype;




    private UMLModel_Signal umlmodel_signal;




    private UMLModel_StructuredClassifier umlmodel_structuredclassifier;


    public UMLModel_Property(
        String subsettedProperty,        String owningAssociation,        String isDerived,        String association,        String associationEnd,        String opposite,        String isComposite,        String aggregation,        String class_,        String datatype,        String isDerivedUnion,        String default,        String redefinedProperty    ) {
        super(
        );
        this.subsettedProperty = subsettedProperty;
        this.owningAssociation = owningAssociation;
        this.isDerived = isDerived;
        this.association = association;
        this.associationEnd = associationEnd;
        this.opposite = opposite;
        this.isComposite = isComposite;
        this.aggregation = aggregation;
        this.class_ = class_;
        this.datatype = datatype;
        this.isDerivedUnion = isDerivedUnion;
        this.default = default;
        this.redefinedProperty = redefinedProperty;
    }


    public String getSubsettedproperty() {
        return subsettedProperty;
    }

    public void setSubsettedproperty(String subsettedProperty) {
        this.subsettedProperty = subsettedProperty;
    }
    public String getOwningassociation() {
        return owningAssociation;
    }

    public void setOwningassociation(String owningAssociation) {
        this.owningAssociation = owningAssociation;
    }
    public String getIsderived() {
        return isDerived;
    }

    public void setIsderived(String isDerived) {
        this.isDerived = isDerived;
    }
    public String getAssociation() {
        return association;
    }

    public void setAssociation(String association) {
        this.association = association;
    }
    public String getAssociationend() {
        return associationEnd;
    }

    public void setAssociationend(String associationEnd) {
        this.associationEnd = associationEnd;
    }
    public String getOpposite() {
        return opposite;
    }

    public void setOpposite(String opposite) {
        this.opposite = opposite;
    }
    public String getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(String isComposite) {
        this.isComposite = isComposite;
    }
    public String getAggregation() {
        return aggregation;
    }

    public void setAggregation(String aggregation) {
        this.aggregation = aggregation;
    }
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }
    public String getDatatype() {
        return datatype;
    }

    public void setDatatype(String datatype) {
        this.datatype = datatype;
    }
    public String getIsderivedunion() {
        return isDerivedUnion;
    }

    public void setIsderivedunion(String isDerivedUnion) {
        this.isDerivedUnion = isDerivedUnion;
    }
    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }
    public String getRedefinedproperty() {
        return redefinedProperty;
    }

    public void setRedefinedproperty(String redefinedProperty) {
        this.redefinedProperty = redefinedProperty;
    }

    public UMLModel_Artifact getUmlmodel_artifact() {
        return umlmodel_artifact;
    }

    public void setUmlmodel_artifact(UMLModel_Artifact umlmodel_artifact) {
        this.umlmodel_artifact = umlmodel_artifact;
    }
    public UMLModel_ValueSpecification getUmlmodel_valuespecification() {
        return umlmodel_valuespecification;
    }

    public void setUmlmodel_valuespecification(UMLModel_ValueSpecification umlmodel_valuespecification) {
        this.umlmodel_valuespecification = umlmodel_valuespecification;
    }
    public UMLModel_Property getUmlmodel_property() {
        return umlmodel_property;
    }

    public void setUmlmodel_property(UMLModel_Property umlmodel_property) {
        this.umlmodel_property = umlmodel_property;
    }
    public UMLModel_Association getUmlmodel_association() {
        return umlmodel_association;
    }

    public void setUmlmodel_association(UMLModel_Association umlmodel_association) {
        this.umlmodel_association = umlmodel_association;
    }
    public UMLModel_Interface getUmlmodel_interface() {
        return umlmodel_interface;
    }

    public void setUmlmodel_interface(UMLModel_Interface umlmodel_interface) {
        this.umlmodel_interface = umlmodel_interface;
    }
    public UMLModel_DataType getUmlmodel_datatype() {
        return umlmodel_datatype;
    }

    public void setUmlmodel_datatype(UMLModel_DataType umlmodel_datatype) {
        this.umlmodel_datatype = umlmodel_datatype;
    }
    public UMLModel_Signal getUmlmodel_signal() {
        return umlmodel_signal;
    }

    public void setUmlmodel_signal(UMLModel_Signal umlmodel_signal) {
        this.umlmodel_signal = umlmodel_signal;
    }
    public UMLModel_StructuredClassifier getUmlmodel_structuredclassifier() {
        return umlmodel_structuredclassifier;
    }

    public void setUmlmodel_structuredclassifier(UMLModel_StructuredClassifier umlmodel_structuredclassifier) {
        this.umlmodel_structuredclassifier = umlmodel_structuredclassifier;
    }

}