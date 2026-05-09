





import java.util.List;
import java.util.ArrayList;

public class UML2_Property extends ConnectableElement, StructuralFeature, DeploymentTarget {

    private boolean isDerived;
    private boolean isComposite;
    private String aggregation;
    private boolean isDerivedUnion;





    private UML2_Property uml2_property;




    private UML2_Property uml2_property;


    public UML2_Property(
        boolean isDerived,        boolean isComposite,        String aggregation,        boolean isDerivedUnion    ) {
        super(
        );
        this.isDerived = isDerived;
        this.isComposite = isComposite;
        this.aggregation = aggregation;
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
    public UML2_Property getUml2_property() {
        return uml2_property;
    }

    public void setUml2_property(UML2_Property uml2_property) {
        this.uml2_property = uml2_property;
    }

}