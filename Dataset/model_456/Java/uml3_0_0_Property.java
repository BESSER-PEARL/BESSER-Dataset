





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_Property extends ConnectableElement, DeploymentTarget, StructuralFeature {

    private String aggregation;
    private String default;
    private String isDerivedUnion;
    private String isComposite;
    private String isDerived;





    private uml3_0_0_Association uml3_0_0_association;




    private uml3_0_0_Association uml3_0_0_association;




    private uml3_0_0_DataType uml3_0_0_datatype;




    private uml3_0_0_StructuredClassifier uml3_0_0_structuredclassifier;




    private uml3_0_0_Artifact uml3_0_0_artifact;




    private uml3_0_0_Property uml3_0_0_property;




    private uml3_0_0_Signal uml3_0_0_signal;




    private uml3_0_0_Association uml3_0_0_association;




    private uml3_0_0_Association uml3_0_0_association;




    private uml3_0_0_ValueSpecification uml3_0_0_valuespecification;




    private uml3_0_0_QualifierValue uml3_0_0_qualifiervalue;




    private uml3_0_0_Classifier uml3_0_0_classifier;




    private uml3_0_0_Association uml3_0_0_association;




    private uml3_0_0_Property uml3_0_0_property;




    private uml3_0_0_Property uml3_0_0_property;




    private uml3_0_0_DataType uml3_0_0_datatype;




    private List<uml3_0_0_Property> uml3_0_0_propertys;




    private uml3_0_0_LinkEndData uml3_0_0_linkenddata;




    private List<uml3_0_0_Property> uml3_0_0_propertys;




    private uml3_0_0_StructuredClassifier uml3_0_0_structuredclassifier;




    private uml3_0_0_Interface uml3_0_0_interface;


    public uml3_0_0_Property(
        String aggregation,        String default,        String isDerivedUnion,        String isComposite,        String isDerived    ) {
        super(
        );
        this.aggregation = aggregation;
        this.default = default;
        this.isDerivedUnion = isDerivedUnion;
        this.isComposite = isComposite;
        this.isDerived = isDerived;
        this.uml3_0_0_propertys = new ArrayList<>();
        this.uml3_0_0_propertys = new ArrayList<>();
    }

    public uml3_0_0_Property(
        String aggregation,        String default,        String isDerivedUnion,        String isComposite,        String isDerived        ArrayList<uml3_0_0_Property> uml3_0_0_propertys,        ArrayList<uml3_0_0_Property> uml3_0_0_propertys    ) {
        this.aggregation = aggregation;
        this.default = default;
        this.isDerivedUnion = isDerivedUnion;
        this.isComposite = isComposite;
        this.isDerived = isDerived;
        this.uml3_0_0_propertys = uml3_0_0_propertys;
        this.uml3_0_0_propertys = uml3_0_0_propertys;
    }

    public String getAggregation() {
        return aggregation;
    }

    public void setAggregation(String aggregation) {
        this.aggregation = aggregation;
    }
    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
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
    public String getIsderived() {
        return isDerived;
    }

    public void setIsderived(String isDerived) {
        this.isDerived = isDerived;
    }

    public uml3_0_0_Association getUml3_0_0_association() {
        return uml3_0_0_association;
    }

    public void setUml3_0_0_association(uml3_0_0_Association uml3_0_0_association) {
        this.uml3_0_0_association = uml3_0_0_association;
    }
    public uml3_0_0_Association getUml3_0_0_association() {
        return uml3_0_0_association;
    }

    public void setUml3_0_0_association(uml3_0_0_Association uml3_0_0_association) {
        this.uml3_0_0_association = uml3_0_0_association;
    }
    public uml3_0_0_DataType getUml3_0_0_datatype() {
        return uml3_0_0_datatype;
    }

    public void setUml3_0_0_datatype(uml3_0_0_DataType uml3_0_0_datatype) {
        this.uml3_0_0_datatype = uml3_0_0_datatype;
    }
    public uml3_0_0_StructuredClassifier getUml3_0_0_structuredclassifier() {
        return uml3_0_0_structuredclassifier;
    }

    public void setUml3_0_0_structuredclassifier(uml3_0_0_StructuredClassifier uml3_0_0_structuredclassifier) {
        this.uml3_0_0_structuredclassifier = uml3_0_0_structuredclassifier;
    }
    public uml3_0_0_Artifact getUml3_0_0_artifact() {
        return uml3_0_0_artifact;
    }

    public void setUml3_0_0_artifact(uml3_0_0_Artifact uml3_0_0_artifact) {
        this.uml3_0_0_artifact = uml3_0_0_artifact;
    }
    public uml3_0_0_Property getUml3_0_0_property() {
        return uml3_0_0_property;
    }

    public void setUml3_0_0_property(uml3_0_0_Property uml3_0_0_property) {
        this.uml3_0_0_property = uml3_0_0_property;
    }
    public uml3_0_0_Signal getUml3_0_0_signal() {
        return uml3_0_0_signal;
    }

    public void setUml3_0_0_signal(uml3_0_0_Signal uml3_0_0_signal) {
        this.uml3_0_0_signal = uml3_0_0_signal;
    }
    public uml3_0_0_Association getUml3_0_0_association() {
        return uml3_0_0_association;
    }

    public void setUml3_0_0_association(uml3_0_0_Association uml3_0_0_association) {
        this.uml3_0_0_association = uml3_0_0_association;
    }
    public uml3_0_0_Association getUml3_0_0_association() {
        return uml3_0_0_association;
    }

    public void setUml3_0_0_association(uml3_0_0_Association uml3_0_0_association) {
        this.uml3_0_0_association = uml3_0_0_association;
    }
    public uml3_0_0_ValueSpecification getUml3_0_0_valuespecification() {
        return uml3_0_0_valuespecification;
    }

    public void setUml3_0_0_valuespecification(uml3_0_0_ValueSpecification uml3_0_0_valuespecification) {
        this.uml3_0_0_valuespecification = uml3_0_0_valuespecification;
    }
    public uml3_0_0_QualifierValue getUml3_0_0_qualifiervalue() {
        return uml3_0_0_qualifiervalue;
    }

    public void setUml3_0_0_qualifiervalue(uml3_0_0_QualifierValue uml3_0_0_qualifiervalue) {
        this.uml3_0_0_qualifiervalue = uml3_0_0_qualifiervalue;
    }
    public uml3_0_0_Classifier getUml3_0_0_classifier() {
        return uml3_0_0_classifier;
    }

    public void setUml3_0_0_classifier(uml3_0_0_Classifier uml3_0_0_classifier) {
        this.uml3_0_0_classifier = uml3_0_0_classifier;
    }
    public uml3_0_0_Association getUml3_0_0_association() {
        return uml3_0_0_association;
    }

    public void setUml3_0_0_association(uml3_0_0_Association uml3_0_0_association) {
        this.uml3_0_0_association = uml3_0_0_association;
    }
    public uml3_0_0_Property getUml3_0_0_property() {
        return uml3_0_0_property;
    }

    public void setUml3_0_0_property(uml3_0_0_Property uml3_0_0_property) {
        this.uml3_0_0_property = uml3_0_0_property;
    }
    public uml3_0_0_Property getUml3_0_0_property() {
        return uml3_0_0_property;
    }

    public void setUml3_0_0_property(uml3_0_0_Property uml3_0_0_property) {
        this.uml3_0_0_property = uml3_0_0_property;
    }
    public uml3_0_0_DataType getUml3_0_0_datatype() {
        return uml3_0_0_datatype;
    }

    public void setUml3_0_0_datatype(uml3_0_0_DataType uml3_0_0_datatype) {
        this.uml3_0_0_datatype = uml3_0_0_datatype;
    }
    public List<uml3_0_0_Property> getUml3_0_0_propertys() {
        return uml3_0_0_propertys;
    }

    public void addUml3_0_0_property(Uml3_0_0_property uml3_0_0_property) {
        this.uml3_0_0_propertys.add(uml3_0_0_property);
    }
    public uml3_0_0_LinkEndData getUml3_0_0_linkenddata() {
        return uml3_0_0_linkenddata;
    }

    public void setUml3_0_0_linkenddata(uml3_0_0_LinkEndData uml3_0_0_linkenddata) {
        this.uml3_0_0_linkenddata = uml3_0_0_linkenddata;
    }
    public List<uml3_0_0_Property> getUml3_0_0_propertys() {
        return uml3_0_0_propertys;
    }

    public void addUml3_0_0_property(Uml3_0_0_property uml3_0_0_property) {
        this.uml3_0_0_propertys.add(uml3_0_0_property);
    }
    public uml3_0_0_StructuredClassifier getUml3_0_0_structuredclassifier() {
        return uml3_0_0_structuredclassifier;
    }

    public void setUml3_0_0_structuredclassifier(uml3_0_0_StructuredClassifier uml3_0_0_structuredclassifier) {
        this.uml3_0_0_structuredclassifier = uml3_0_0_structuredclassifier;
    }
    public uml3_0_0_Interface getUml3_0_0_interface() {
        return uml3_0_0_interface;
    }

    public void setUml3_0_0_interface(uml3_0_0_Interface uml3_0_0_interface) {
        this.uml3_0_0_interface = uml3_0_0_interface;
    }

}