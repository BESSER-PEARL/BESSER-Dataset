





import java.util.List;
import java.util.ArrayList;

public class UML2_Property extends DeploymentTarget, ConnectableElement, StructuralFeature {

    private String aggregation;
    private boolean isDerived;
    private boolean isDerivedUnion;
    private boolean isComposite;





    private UML2_Property uml2_property;




    private List<UML2_Property> uml2_propertys;


    public UML2_Property(
        String aggregation,        boolean isDerived,        boolean isDerivedUnion,        boolean isComposite    ) {
        super(
        );
        this.aggregation = aggregation;
        this.isDerived = isDerived;
        this.isDerivedUnion = isDerivedUnion;
        this.isComposite = isComposite;
        this.uml2_propertys = new ArrayList<>();
    }

    public UML2_Property(
        String aggregation,        boolean isDerived,        boolean isDerivedUnion,        boolean isComposite        ArrayList<UML2_Property> uml2_propertys    ) {
        this.aggregation = aggregation;
        this.isDerived = isDerived;
        this.isDerivedUnion = isDerivedUnion;
        this.isComposite = isComposite;
        this.uml2_propertys = uml2_propertys;
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
    public boolean getIsderivedunion() {
        return isDerivedUnion;
    }

    public void setIsderivedunion(boolean isDerivedUnion) {
        this.isDerivedUnion = isDerivedUnion;
    }
    public boolean getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(boolean isComposite) {
        this.isComposite = isComposite;
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