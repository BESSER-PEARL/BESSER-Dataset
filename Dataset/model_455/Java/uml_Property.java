





import java.util.List;
import java.util.ArrayList;

public class uml_Property extends DeploymentTarget, ConnectableElement, StructuralFeature {

    private String isDerivedUnion;
    private String isComposite;
    private String default;
    private String isDerived;
    private String aggregation;





    private uml_Association uml_association;




    private uml_StructuredClassifier uml_structuredclassifier;




    private uml_Artifact uml_artifact;




    private uml_DataType uml_datatype;




    private uml_ValueSpecification uml_valuespecification;




    private uml_Association uml_association;




    private uml_LinkEndData uml_linkenddata;




    private uml_Classifier uml_classifier;




    private uml_Property uml_property;




    private List<uml_Property> uml_propertys;




    private uml_StructuredClassifier uml_structuredclassifier;




    private uml_QualifierValue uml_qualifiervalue;




    private uml_Property uml_property;




    private uml_Association uml_association;




    private uml_Association uml_association;




    private uml_DataType uml_datatype;




    private uml_Interface uml_interface;




    private uml_Signal uml_signal;




    private uml_Association uml_association;




    private List<uml_Property> uml_propertys;




    private uml_Property uml_property;


    public uml_Property(
        String isDerivedUnion,        String isComposite,        String default,        String isDerived,        String aggregation    ) {
        super(
        );
        this.isDerivedUnion = isDerivedUnion;
        this.isComposite = isComposite;
        this.default = default;
        this.isDerived = isDerived;
        this.aggregation = aggregation;
        this.uml_propertys = new ArrayList<>();
        this.uml_propertys = new ArrayList<>();
    }

    public uml_Property(
        String isDerivedUnion,        String isComposite,        String default,        String isDerived,        String aggregation        ArrayList<uml_Property> uml_propertys,        ArrayList<uml_Property> uml_propertys    ) {
        this.isDerivedUnion = isDerivedUnion;
        this.isComposite = isComposite;
        this.default = default;
        this.isDerived = isDerived;
        this.aggregation = aggregation;
        this.uml_propertys = uml_propertys;
        this.uml_propertys = uml_propertys;
    }

    public String getIsderivedunion() {
        return isDerivedUnion;
    }

    public void setIsderivedunion(String isDerivedUnion) {
        this.isDerivedUnion = isDerivedUnion;
    }
    public String getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(String isComposite) {
        this.isComposite = isComposite;
    }
    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }
    public String getIsderived() {
        return isDerived;
    }

    public void setIsderived(String isDerived) {
        this.isDerived = isDerived;
    }
    public String getAggregation() {
        return aggregation;
    }

    public void setAggregation(String aggregation) {
        this.aggregation = aggregation;
    }

    public uml_Association getUml_association() {
        return uml_association;
    }

    public void setUml_association(uml_Association uml_association) {
        this.uml_association = uml_association;
    }
    public uml_StructuredClassifier getUml_structuredclassifier() {
        return uml_structuredclassifier;
    }

    public void setUml_structuredclassifier(uml_StructuredClassifier uml_structuredclassifier) {
        this.uml_structuredclassifier = uml_structuredclassifier;
    }
    public uml_Artifact getUml_artifact() {
        return uml_artifact;
    }

    public void setUml_artifact(uml_Artifact uml_artifact) {
        this.uml_artifact = uml_artifact;
    }
    public uml_DataType getUml_datatype() {
        return uml_datatype;
    }

    public void setUml_datatype(uml_DataType uml_datatype) {
        this.uml_datatype = uml_datatype;
    }
    public uml_ValueSpecification getUml_valuespecification() {
        return uml_valuespecification;
    }

    public void setUml_valuespecification(uml_ValueSpecification uml_valuespecification) {
        this.uml_valuespecification = uml_valuespecification;
    }
    public uml_Association getUml_association() {
        return uml_association;
    }

    public void setUml_association(uml_Association uml_association) {
        this.uml_association = uml_association;
    }
    public uml_LinkEndData getUml_linkenddata() {
        return uml_linkenddata;
    }

    public void setUml_linkenddata(uml_LinkEndData uml_linkenddata) {
        this.uml_linkenddata = uml_linkenddata;
    }
    public uml_Classifier getUml_classifier() {
        return uml_classifier;
    }

    public void setUml_classifier(uml_Classifier uml_classifier) {
        this.uml_classifier = uml_classifier;
    }
    public uml_Property getUml_property() {
        return uml_property;
    }

    public void setUml_property(uml_Property uml_property) {
        this.uml_property = uml_property;
    }
    public List<uml_Property> getUml_propertys() {
        return uml_propertys;
    }

    public void addUml_property(Uml_property uml_property) {
        this.uml_propertys.add(uml_property);
    }
    public uml_StructuredClassifier getUml_structuredclassifier() {
        return uml_structuredclassifier;
    }

    public void setUml_structuredclassifier(uml_StructuredClassifier uml_structuredclassifier) {
        this.uml_structuredclassifier = uml_structuredclassifier;
    }
    public uml_QualifierValue getUml_qualifiervalue() {
        return uml_qualifiervalue;
    }

    public void setUml_qualifiervalue(uml_QualifierValue uml_qualifiervalue) {
        this.uml_qualifiervalue = uml_qualifiervalue;
    }
    public uml_Property getUml_property() {
        return uml_property;
    }

    public void setUml_property(uml_Property uml_property) {
        this.uml_property = uml_property;
    }
    public uml_Association getUml_association() {
        return uml_association;
    }

    public void setUml_association(uml_Association uml_association) {
        this.uml_association = uml_association;
    }
    public uml_Association getUml_association() {
        return uml_association;
    }

    public void setUml_association(uml_Association uml_association) {
        this.uml_association = uml_association;
    }
    public uml_DataType getUml_datatype() {
        return uml_datatype;
    }

    public void setUml_datatype(uml_DataType uml_datatype) {
        this.uml_datatype = uml_datatype;
    }
    public uml_Interface getUml_interface() {
        return uml_interface;
    }

    public void setUml_interface(uml_Interface uml_interface) {
        this.uml_interface = uml_interface;
    }
    public uml_Signal getUml_signal() {
        return uml_signal;
    }

    public void setUml_signal(uml_Signal uml_signal) {
        this.uml_signal = uml_signal;
    }
    public uml_Association getUml_association() {
        return uml_association;
    }

    public void setUml_association(uml_Association uml_association) {
        this.uml_association = uml_association;
    }
    public List<uml_Property> getUml_propertys() {
        return uml_propertys;
    }

    public void addUml_property(Uml_property uml_property) {
        this.uml_propertys.add(uml_property);
    }
    public uml_Property getUml_property() {
        return uml_property;
    }

    public void setUml_property(uml_Property uml_property) {
        this.uml_property = uml_property;
    }

}