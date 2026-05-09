





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Property extends StructuralFeature, DeploymentTarget, ConnectableElement {

    private String aggregation;
    private boolean isDerived;
    private String default;
    private boolean isComposite;
    private boolean isDerivedUnion;





    private UML2WithID_ValueSpecification uml2withid_valuespecification;




    private UML2WithID_Property uml2withid_property;




    private UML2WithID_Classifier uml2withid_classifier;




    private UML2WithID_QualifierValue uml2withid_qualifiervalue;




    private UML2WithID_Property uml2withid_property;




    private UML2WithID_Property uml2withid_property;




    private UML2WithID_Property uml2withid_property;




    private List<UML2WithID_Property> uml2withid_propertys;




    private UML2WithID_LinkEndData uml2withid_linkenddata;


    public UML2WithID_Property(
        String aggregation,        boolean isDerived,        String default,        boolean isComposite,        boolean isDerivedUnion    ) {
        super(
        );
        this.aggregation = aggregation;
        this.isDerived = isDerived;
        this.default = default;
        this.isComposite = isComposite;
        this.isDerivedUnion = isDerivedUnion;
        this.uml2withid_propertys = new ArrayList<>();
    }

    public UML2WithID_Property(
        String aggregation,        boolean isDerived,        String default,        boolean isComposite,        boolean isDerivedUnion        ArrayList<UML2WithID_Property> uml2withid_propertys    ) {
        this.aggregation = aggregation;
        this.isDerived = isDerived;
        this.default = default;
        this.isComposite = isComposite;
        this.isDerivedUnion = isDerivedUnion;
        this.uml2withid_propertys = uml2withid_propertys;
    }

    public String getAggregation() {
        return aggregation;
    }

    public void setAggregation(String aggregation) {
        this.aggregation = aggregation;
    }
    public boolean getIsderived() {
        return isDerived;
    }

    public void setIsderived(boolean isDerived) {
        this.isDerived = isDerived;
    }
    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
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

    public UML2WithID_ValueSpecification getUml2withid_valuespecification() {
        return uml2withid_valuespecification;
    }

    public void setUml2withid_valuespecification(UML2WithID_ValueSpecification uml2withid_valuespecification) {
        this.uml2withid_valuespecification = uml2withid_valuespecification;
    }
    public UML2WithID_Property getUml2withid_property() {
        return uml2withid_property;
    }

    public void setUml2withid_property(UML2WithID_Property uml2withid_property) {
        this.uml2withid_property = uml2withid_property;
    }
    public UML2WithID_Classifier getUml2withid_classifier() {
        return uml2withid_classifier;
    }

    public void setUml2withid_classifier(UML2WithID_Classifier uml2withid_classifier) {
        this.uml2withid_classifier = uml2withid_classifier;
    }
    public UML2WithID_QualifierValue getUml2withid_qualifiervalue() {
        return uml2withid_qualifiervalue;
    }

    public void setUml2withid_qualifiervalue(UML2WithID_QualifierValue uml2withid_qualifiervalue) {
        this.uml2withid_qualifiervalue = uml2withid_qualifiervalue;
    }
    public UML2WithID_Property getUml2withid_property() {
        return uml2withid_property;
    }

    public void setUml2withid_property(UML2WithID_Property uml2withid_property) {
        this.uml2withid_property = uml2withid_property;
    }
    public UML2WithID_Property getUml2withid_property() {
        return uml2withid_property;
    }

    public void setUml2withid_property(UML2WithID_Property uml2withid_property) {
        this.uml2withid_property = uml2withid_property;
    }
    public UML2WithID_Property getUml2withid_property() {
        return uml2withid_property;
    }

    public void setUml2withid_property(UML2WithID_Property uml2withid_property) {
        this.uml2withid_property = uml2withid_property;
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