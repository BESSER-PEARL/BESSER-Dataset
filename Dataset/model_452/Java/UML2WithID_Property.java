





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Property extends StructuralFeature, DeploymentTarget, ConnectableElement {

    private String default;
    private boolean isDerivedUnion;
    private boolean isDerived;
    private boolean isComposite;
    private String aggregation;





    private UML2WithID_Signal uml2withid_signal;




    private UML2WithID_Association uml2withid_association;




    private List<UML2WithID_Property> uml2withid_propertys;




    private UML2WithID_DataType uml2withid_datatype;




    private UML2WithID_Association uml2withid_association;




    private UML2WithID_Classifier uml2withid_classifier;




    private UML2WithID_DataType uml2withid_datatype;




    private UML2WithID_Property uml2withid_property;




    private UML2WithID_StructuredClassifier uml2withid_structuredclassifier;




    private UML2WithID_Interface uml2withid_interface;




    private UML2WithID_ValueSpecification uml2withid_valuespecification;




    private UML2WithID_QualifierValue uml2withid_qualifiervalue;




    private UML2WithID_Association uml2withid_association;




    private List<UML2WithID_Property> uml2withid_propertys;




    private UML2WithID_StructuredClassifier uml2withid_structuredclassifier;




    private UML2WithID_Property uml2withid_property;




    private UML2WithID_Association uml2withid_association;




    private UML2WithID_Artifact uml2withid_artifact;




    private List<UML2WithID_Property> uml2withid_propertys;




    private UML2WithID_LinkEndData uml2withid_linkenddata;


    public UML2WithID_Property(
        String default,        boolean isDerivedUnion,        boolean isDerived,        boolean isComposite,        String aggregation    ) {
        super(
        );
        this.default = default;
        this.isDerivedUnion = isDerivedUnion;
        this.isDerived = isDerived;
        this.isComposite = isComposite;
        this.aggregation = aggregation;
        this.uml2withid_propertys = new ArrayList<>();
        this.uml2withid_propertys = new ArrayList<>();
        this.uml2withid_propertys = new ArrayList<>();
    }

    public UML2WithID_Property(
        String default,        boolean isDerivedUnion,        boolean isDerived,        boolean isComposite,        String aggregation        ArrayList<UML2WithID_Property> uml2withid_propertys,        ArrayList<UML2WithID_Property> uml2withid_propertys,        ArrayList<UML2WithID_Property> uml2withid_propertys    ) {
        this.default = default;
        this.isDerivedUnion = isDerivedUnion;
        this.isDerived = isDerived;
        this.isComposite = isComposite;
        this.aggregation = aggregation;
        this.uml2withid_propertys = uml2withid_propertys;
        this.uml2withid_propertys = uml2withid_propertys;
        this.uml2withid_propertys = uml2withid_propertys;
    }

    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }
    public boolean getIsderivedunion() {
        return isDerivedUnion;
    }

    public void setIsderivedunion(boolean isDerivedUnion) {
        this.isDerivedUnion = isDerivedUnion;
    }
    public boolean getIsderived() {
        return isDerived;
    }

    public void setIsderived(boolean isDerived) {
        this.isDerived = isDerived;
    }
    public boolean getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(boolean isComposite) {
        this.isComposite = isComposite;
    }
    public String getAggregation() {
        return aggregation;
    }

    public void setAggregation(String aggregation) {
        this.aggregation = aggregation;
    }

    public UML2WithID_Signal getUml2withid_signal() {
        return uml2withid_signal;
    }

    public void setUml2withid_signal(UML2WithID_Signal uml2withid_signal) {
        this.uml2withid_signal = uml2withid_signal;
    }
    public UML2WithID_Association getUml2withid_association() {
        return uml2withid_association;
    }

    public void setUml2withid_association(UML2WithID_Association uml2withid_association) {
        this.uml2withid_association = uml2withid_association;
    }
    public List<UML2WithID_Property> getUml2withid_propertys() {
        return uml2withid_propertys;
    }

    public void addUml2withid_property(Uml2withid_property uml2withid_property) {
        this.uml2withid_propertys.add(uml2withid_property);
    }
    public UML2WithID_DataType getUml2withid_datatype() {
        return uml2withid_datatype;
    }

    public void setUml2withid_datatype(UML2WithID_DataType uml2withid_datatype) {
        this.uml2withid_datatype = uml2withid_datatype;
    }
    public UML2WithID_Association getUml2withid_association() {
        return uml2withid_association;
    }

    public void setUml2withid_association(UML2WithID_Association uml2withid_association) {
        this.uml2withid_association = uml2withid_association;
    }
    public UML2WithID_Classifier getUml2withid_classifier() {
        return uml2withid_classifier;
    }

    public void setUml2withid_classifier(UML2WithID_Classifier uml2withid_classifier) {
        this.uml2withid_classifier = uml2withid_classifier;
    }
    public UML2WithID_DataType getUml2withid_datatype() {
        return uml2withid_datatype;
    }

    public void setUml2withid_datatype(UML2WithID_DataType uml2withid_datatype) {
        this.uml2withid_datatype = uml2withid_datatype;
    }
    public UML2WithID_Property getUml2withid_property() {
        return uml2withid_property;
    }

    public void setUml2withid_property(UML2WithID_Property uml2withid_property) {
        this.uml2withid_property = uml2withid_property;
    }
    public UML2WithID_StructuredClassifier getUml2withid_structuredclassifier() {
        return uml2withid_structuredclassifier;
    }

    public void setUml2withid_structuredclassifier(UML2WithID_StructuredClassifier uml2withid_structuredclassifier) {
        this.uml2withid_structuredclassifier = uml2withid_structuredclassifier;
    }
    public UML2WithID_Interface getUml2withid_interface() {
        return uml2withid_interface;
    }

    public void setUml2withid_interface(UML2WithID_Interface uml2withid_interface) {
        this.uml2withid_interface = uml2withid_interface;
    }
    public UML2WithID_ValueSpecification getUml2withid_valuespecification() {
        return uml2withid_valuespecification;
    }

    public void setUml2withid_valuespecification(UML2WithID_ValueSpecification uml2withid_valuespecification) {
        this.uml2withid_valuespecification = uml2withid_valuespecification;
    }
    public UML2WithID_QualifierValue getUml2withid_qualifiervalue() {
        return uml2withid_qualifiervalue;
    }

    public void setUml2withid_qualifiervalue(UML2WithID_QualifierValue uml2withid_qualifiervalue) {
        this.uml2withid_qualifiervalue = uml2withid_qualifiervalue;
    }
    public UML2WithID_Association getUml2withid_association() {
        return uml2withid_association;
    }

    public void setUml2withid_association(UML2WithID_Association uml2withid_association) {
        this.uml2withid_association = uml2withid_association;
    }
    public List<UML2WithID_Property> getUml2withid_propertys() {
        return uml2withid_propertys;
    }

    public void addUml2withid_property(Uml2withid_property uml2withid_property) {
        this.uml2withid_propertys.add(uml2withid_property);
    }
    public UML2WithID_StructuredClassifier getUml2withid_structuredclassifier() {
        return uml2withid_structuredclassifier;
    }

    public void setUml2withid_structuredclassifier(UML2WithID_StructuredClassifier uml2withid_structuredclassifier) {
        this.uml2withid_structuredclassifier = uml2withid_structuredclassifier;
    }
    public UML2WithID_Property getUml2withid_property() {
        return uml2withid_property;
    }

    public void setUml2withid_property(UML2WithID_Property uml2withid_property) {
        this.uml2withid_property = uml2withid_property;
    }
    public UML2WithID_Association getUml2withid_association() {
        return uml2withid_association;
    }

    public void setUml2withid_association(UML2WithID_Association uml2withid_association) {
        this.uml2withid_association = uml2withid_association;
    }
    public UML2WithID_Artifact getUml2withid_artifact() {
        return uml2withid_artifact;
    }

    public void setUml2withid_artifact(UML2WithID_Artifact uml2withid_artifact) {
        this.uml2withid_artifact = uml2withid_artifact;
    }
    public List<UML2WithID_Property> getUml2withid_propertys() {
        return uml2withid_propertys;
    }

    public void addUml2withid_property(Uml2withid_property uml2withid_property) {
        this.uml2withid_propertys.add(uml2withid_property);
    }
    public UML2WithID_LinkEndData getUml2withid_linkenddata() {
        return uml2withid_linkenddata;
    }

    public void setUml2withid_linkenddata(UML2WithID_LinkEndData uml2withid_linkenddata) {
        this.uml2withid_linkenddata = uml2withid_linkenddata;
    }

}