





import java.util.List;
import java.util.ArrayList;

public class UML2_Property extends ConnectableElement, StructuralFeature, DeploymentTarget {

    private boolean isComposite;
    private boolean isDerived;
    private String aggregation;
    private boolean isDerivedUnion;





    private UML2_Property uml2_property;




    private List<UML2_Property> uml2_propertys;


    public UML2_Property(
        boolean isComposite,        boolean isDerived,        String aggregation,        boolean isDerivedUnion    ) {
        super(
        );
        this.isComposite = isComposite;
        this.isDerived = isDerived;
        this.aggregation = aggregation;
        this.isDerivedUnion = isDerivedUnion;
        this.uml2_propertys = new ArrayList<>();
    }

    public UML2_Property(
        boolean isComposite,        boolean isDerived,        String aggregation,        boolean isDerivedUnion        ArrayList<UML2_Property> uml2_propertys    ) {
        this.isComposite = isComposite;
        this.isDerived = isDerived;
        this.aggregation = aggregation;
        this.isDerivedUnion = isDerivedUnion;
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
    public String getAggregation() {
        return aggregation;
    }

    public void setAggregation(String aggregation) {
        this.aggregation = aggregation;
    }
    public boolean getIsderivedunion() {
        return isDerivedUnion;
    }

    public void setIsderivedunion(boolean isDerivedUnion) {
        this.isDerivedUnion = isDerivedUnion;
    }

    public UML2_Property getUml2_property() {
        return uml2_property;
    }

    public void setUml2_property(UML2_Property uml2_property) {
        this.uml2_property = uml2_property;
    }
    public List<UML2_Property> getUml2_propertys() {
        return uml2_propertys;
    }

    public void addUml2_property(Uml2_property uml2_property) {
        this.uml2_propertys.add(uml2_property);
    }

}