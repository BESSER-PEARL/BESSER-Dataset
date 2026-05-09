





import java.util.List;
import java.util.ArrayList;

public class UML2_Property extends DeploymentTarget, ConnectableElement, StructuralFeature {

    private boolean isComposite;
    private boolean isDerivedUnion;
    private String aggregation;
    private String default;
    private boolean isDerived;





    private UML2_DataType uml2_datatype;




    private UML2_Artifact uml2_artifact;




    private UML2_Association uml2_association;




    private UML2_Property uml2_property;




    private UML2_ValueSpecification uml2_valuespecification;




    private UML2_Association uml2_association;




    private UML2_StructuredClassifier uml2_structuredclassifier;




    private UML2_LinkEndData uml2_linkenddata;




    private UML2_Classifier uml2_classifier;




    private UML2_QualifierValue uml2_qualifiervalue;




    private UML2_StructuredClassifier uml2_structuredclassifier;




    private UML2_ReadLinkObjectEndAction uml2_readlinkobjectendaction;




    private UML2_Association uml2_association;




    private UML2_Class uml2_class;




    private UML2_Property uml2_property;




    private UML2_DataType uml2_datatype;




    private List<UML2_Property> uml2_propertys;




    private UML2_Interface uml2_interface;




    private UML2_Signal uml2_signal;




    private UML2_Association uml2_association;




    private UML2_ConnectorEnd uml2_connectorend;




    private List<UML2_Property> uml2_propertys;




    private UML2_ConnectorEnd uml2_connectorend;




    private UML2_ReadLinkObjectEndQualifierAction uml2_readlinkobjectendqualifieraction;




    private List<UML2_Property> uml2_propertys;


    public UML2_Property(
        boolean isComposite,        boolean isDerivedUnion,        String aggregation,        String default,        boolean isDerived    ) {
        super(
        );
        this.isComposite = isComposite;
        this.isDerivedUnion = isDerivedUnion;
        this.aggregation = aggregation;
        this.default = default;
        this.isDerived = isDerived;
        this.uml2_propertys = new ArrayList<>();
        this.uml2_propertys = new ArrayList<>();
        this.uml2_propertys = new ArrayList<>();
    }

    public UML2_Property(
        boolean isComposite,        boolean isDerivedUnion,        String aggregation,        String default,        boolean isDerived        ArrayList<UML2_Property> uml2_propertys,        ArrayList<UML2_Property> uml2_propertys,        ArrayList<UML2_Property> uml2_propertys    ) {
        this.isComposite = isComposite;
        this.isDerivedUnion = isDerivedUnion;
        this.aggregation = aggregation;
        this.default = default;
        this.isDerived = isDerived;
        this.uml2_propertys = uml2_propertys;
        this.uml2_propertys = uml2_propertys;
        this.uml2_propertys = uml2_propertys;
    }

    public boolean getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(boolean isComposite) {
        this.isComposite = isComposite;
    }
    public boolean getIsderivedunion() {
        return isDerivedUnion;
    }

    public void setIsderivedunion(boolean isDerivedUnion) {
        this.isDerivedUnion = isDerivedUnion;
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
    public boolean getIsderived() {
        return isDerived;
    }

    public void setIsderived(boolean isDerived) {
        this.isDerived = isDerived;
    }

    public UML2_DataType getUml2_datatype() {
        return uml2_datatype;
    }

    public void setUml2_datatype(UML2_DataType uml2_datatype) {
        this.uml2_datatype = uml2_datatype;
    }
    public UML2_Artifact getUml2_artifact() {
        return uml2_artifact;
    }

    public void setUml2_artifact(UML2_Artifact uml2_artifact) {
        this.uml2_artifact = uml2_artifact;
    }
    public UML2_Association getUml2_association() {
        return uml2_association;
    }

    public void setUml2_association(UML2_Association uml2_association) {
        this.uml2_association = uml2_association;
    }
    public UML2_Property getUml2_property() {
        return uml2_property;
    }

    public void setUml2_property(UML2_Property uml2_property) {
        this.uml2_property = uml2_property;
    }
    public UML2_ValueSpecification getUml2_valuespecification() {
        return uml2_valuespecification;
    }

    public void setUml2_valuespecification(UML2_ValueSpecification uml2_valuespecification) {
        this.uml2_valuespecification = uml2_valuespecification;
    }
    public UML2_Association getUml2_association() {
        return uml2_association;
    }

    public void setUml2_association(UML2_Association uml2_association) {
        this.uml2_association = uml2_association;
    }
    public UML2_StructuredClassifier getUml2_structuredclassifier() {
        return uml2_structuredclassifier;
    }

    public void setUml2_structuredclassifier(UML2_StructuredClassifier uml2_structuredclassifier) {
        this.uml2_structuredclassifier = uml2_structuredclassifier;
    }
    public UML2_LinkEndData getUml2_linkenddata() {
        return uml2_linkenddata;
    }

    public void setUml2_linkenddata(UML2_LinkEndData uml2_linkenddata) {
        this.uml2_linkenddata = uml2_linkenddata;
    }
    public UML2_Classifier getUml2_classifier() {
        return uml2_classifier;
    }

    public void setUml2_classifier(UML2_Classifier uml2_classifier) {
        this.uml2_classifier = uml2_classifier;
    }
    public UML2_QualifierValue getUml2_qualifiervalue() {
        return uml2_qualifiervalue;
    }

    public void setUml2_qualifiervalue(UML2_QualifierValue uml2_qualifiervalue) {
        this.uml2_qualifiervalue = uml2_qualifiervalue;
    }
    public UML2_StructuredClassifier getUml2_structuredclassifier() {
        return uml2_structuredclassifier;
    }

    public void setUml2_structuredclassifier(UML2_StructuredClassifier uml2_structuredclassifier) {
        this.uml2_structuredclassifier = uml2_structuredclassifier;
    }
    public UML2_ReadLinkObjectEndAction getUml2_readlinkobjectendaction() {
        return uml2_readlinkobjectendaction;
    }

    public void setUml2_readlinkobjectendaction(UML2_ReadLinkObjectEndAction uml2_readlinkobjectendaction) {
        this.uml2_readlinkobjectendaction = uml2_readlinkobjectendaction;
    }
    public UML2_Association getUml2_association() {
        return uml2_association;
    }

    public void setUml2_association(UML2_Association uml2_association) {
        this.uml2_association = uml2_association;
    }
    public UML2_Class getUml2_class() {
        return uml2_class;
    }

    public void setUml2_class(UML2_Class uml2_class) {
        this.uml2_class = uml2_class;
    }
    public UML2_Property getUml2_property() {
        return uml2_property;
    }

    public void setUml2_property(UML2_Property uml2_property) {
        this.uml2_property = uml2_property;
    }
    public UML2_DataType getUml2_datatype() {
        return uml2_datatype;
    }

    public void setUml2_datatype(UML2_DataType uml2_datatype) {
        this.uml2_datatype = uml2_datatype;
    }
    public List<UML2_Property> getUml2_propertys() {
        return uml2_propertys;
    }

    public void addUml2_property(Uml2_property uml2_property) {
        this.uml2_propertys.add(uml2_property);
    }
    public UML2_Interface getUml2_interface() {
        return uml2_interface;
    }

    public void setUml2_interface(UML2_Interface uml2_interface) {
        this.uml2_interface = uml2_interface;
    }
    public UML2_Signal getUml2_signal() {
        return uml2_signal;
    }

    public void setUml2_signal(UML2_Signal uml2_signal) {
        this.uml2_signal = uml2_signal;
    }
    public UML2_Association getUml2_association() {
        return uml2_association;
    }

    public void setUml2_association(UML2_Association uml2_association) {
        this.uml2_association = uml2_association;
    }
    public UML2_ConnectorEnd getUml2_connectorend() {
        return uml2_connectorend;
    }

    public void setUml2_connectorend(UML2_ConnectorEnd uml2_connectorend) {
        this.uml2_connectorend = uml2_connectorend;
    }
    public List<UML2_Property> getUml2_propertys() {
        return uml2_propertys;
    }

    public void addUml2_property(Uml2_property uml2_property) {
        this.uml2_propertys.add(uml2_property);
    }
    public UML2_ConnectorEnd getUml2_connectorend() {
        return uml2_connectorend;
    }

    public void setUml2_connectorend(UML2_ConnectorEnd uml2_connectorend) {
        this.uml2_connectorend = uml2_connectorend;
    }
    public UML2_ReadLinkObjectEndQualifierAction getUml2_readlinkobjectendqualifieraction() {
        return uml2_readlinkobjectendqualifieraction;
    }

    public void setUml2_readlinkobjectendqualifieraction(UML2_ReadLinkObjectEndQualifierAction uml2_readlinkobjectendqualifieraction) {
        this.uml2_readlinkobjectendqualifieraction = uml2_readlinkobjectendqualifieraction;
    }
    public List<UML2_Property> getUml2_propertys() {
        return uml2_propertys;
    }

    public void addUml2_property(Uml2_property uml2_property) {
        this.uml2_propertys.add(uml2_property);
    }

}