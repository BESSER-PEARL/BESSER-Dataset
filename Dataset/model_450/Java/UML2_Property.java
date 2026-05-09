





import java.util.List;
import java.util.ArrayList;

public class UML2_Property extends StructuralFeature, DeploymentTarget, ConnectableElement {

    private boolean isComposite;
    private String aggregation;
    private String default;
    private boolean isDerived;
    private boolean isDerivedUnion;





    private UML2_Classifier uml2_classifier;




    private UML2_Property uml2_property;




    private UML2_Property uml2_property;




    private UML2_Class uml2_class;




    private List<UML2_Property> uml2_propertys;




    private UML2_Property uml2_property;




    private UML2_Property uml2_property;


    public UML2_Property(
        boolean isComposite,        String aggregation,        String default,        boolean isDerived,        boolean isDerivedUnion    ) {
        super(
        );
        this.isComposite = isComposite;
        this.aggregation = aggregation;
        this.default = default;
        this.isDerived = isDerived;
        this.isDerivedUnion = isDerivedUnion;
        this.uml2_propertys = new ArrayList<>();
    }

    public UML2_Property(
        boolean isComposite,        String aggregation,        String default,        boolean isDerived,        boolean isDerivedUnion        ArrayList<UML2_Property> uml2_propertys    ) {
        this.isComposite = isComposite;
        this.aggregation = aggregation;
        this.default = default;
        this.isDerived = isDerived;
        this.isDerivedUnion = isDerivedUnion;
        this.uml2_propertys = uml2_propertys;
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
    public boolean getIsderivedunion() {
        return isDerivedUnion;
    }

    public void setIsderivedunion(boolean isDerivedUnion) {
        this.isDerivedUnion = isDerivedUnion;
    }

    public UML2_Classifier getUml2_classifier() {
        return uml2_classifier;
    }

    public void setUml2_classifier(UML2_Classifier uml2_classifier) {
        this.uml2_classifier = uml2_classifier;
    }
    public UML2_Property getUml2_property() {
        return uml2_property;
    }

    public void setUml2_property(UML2_Property uml2_property) {
        this.uml2_property = uml2_property;
    }
    public UML2_Property getUml2_property() {
        return uml2_property;
    }

    public void setUml2_property(UML2_Property uml2_property) {
        this.uml2_property = uml2_property;
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
    public UML2_Property getUml2_property() {
        return uml2_property;
    }

    public void setUml2_property(UML2_Property uml2_property) {
        this.uml2_property = uml2_property;
    }
    public UML2_Property getUml2_property() {
        return uml2_property;
    }

    public void setUml2_property(UML2_Property uml2_property) {
        this.uml2_property = uml2_property;
    }

}