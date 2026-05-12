





import java.util.List;
import java.util.ArrayList;

public class UML2_Property extends StructuralFeature, ConnectableElement, DeploymentTarget {

    private boolean isComposite;
    private boolean isDerived;
    private boolean isDerivedUnion;
    private String aggregation;
    private String default;





    private UML2_Property uml2_property;




    private UML2_QualifierValue uml2_qualifiervalue;




    private UML2_Property uml2_property;




    private UML2_ValueSpecification uml2_valuespecification;




    private UML2_Property uml2_property;




    private UML2_Association uml2_association;




    private UML2_Association uml2_association;




    private UML2_Property uml2_property;




    private UML2_LinkEndData uml2_linkenddata;




    private UML2_Association uml2_association;




    private UML2_Class uml2_class;




    private List<UML2_Property> uml2_propertys;




    private UML2_Classifier uml2_classifier;




    private UML2_Association uml2_association;


    public UML2_Property(
        boolean isComposite,        boolean isDerived,        boolean isDerivedUnion,        String aggregation,        String default    ) {
        super(
        );
        this.isComposite = isComposite;
        this.isDerived = isDerived;
        this.isDerivedUnion = isDerivedUnion;
        this.aggregation = aggregation;
        this.default = default;
        this.uml2_propertys = new ArrayList<>();
    }

    public UML2_Property(
        boolean isComposite,        boolean isDerived,        boolean isDerivedUnion,        String aggregation,        String default        ArrayList<UML2_Property> uml2_propertys    ) {
        this.isComposite = isComposite;
        this.isDerived = isDerived;
        this.isDerivedUnion = isDerivedUnion;
        this.aggregation = aggregation;
        this.default = default;
        this.uml2_propertys = uml2_propertys;
    }

    public boolean getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(boolean isComposite) {
        this.isComposite = isComposite;
    }
    public boolean getIsderived() {
        return isDerived;
    }

    public void setIsderived(boolean isDerived) {
        this.isDerived = isDerived;
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

    public UML2_Property getUml2_property() {
        return uml2_property;
    }

    public void setUml2_property(UML2_Property uml2_property) {
        this.uml2_property = uml2_property;
    }
    public UML2_QualifierValue getUml2_qualifiervalue() {
        return uml2_qualifiervalue;
    }

    public void setUml2_qualifiervalue(UML2_QualifierValue uml2_qualifiervalue) {
        this.uml2_qualifiervalue = uml2_qualifiervalue;
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
    public UML2_Property getUml2_property() {
        return uml2_property;
    }

    public void setUml2_property(UML2_Property uml2_property) {
        this.uml2_property = uml2_property;
    }
    public UML2_Association getUml2_association() {
        return uml2_association;
    }

    public void setUml2_association(UML2_Association uml2_association) {
        this.uml2_association = uml2_association;
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
    public UML2_LinkEndData getUml2_linkenddata() {
        return uml2_linkenddata;
    }

    public void setUml2_linkenddata(UML2_LinkEndData uml2_linkenddata) {
        this.uml2_linkenddata = uml2_linkenddata;
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
    public List<UML2_Property> getUml2_propertys() {
        return uml2_propertys;
    }

    public void addUml2_property(Uml2_property uml2_property) {
        this.uml2_propertys.add(uml2_property);
    }
    public UML2_Classifier getUml2_classifier() {
        return uml2_classifier;
    }

    public void setUml2_classifier(UML2_Classifier uml2_classifier) {
        this.uml2_classifier = uml2_classifier;
    }
    public UML2_Association getUml2_association() {
        return uml2_association;
    }

    public void setUml2_association(UML2_Association uml2_association) {
        this.uml2_association = uml2_association;
    }

}