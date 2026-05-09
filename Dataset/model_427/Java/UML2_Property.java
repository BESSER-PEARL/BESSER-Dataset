





import java.util.List;
import java.util.ArrayList;

public class UML2_Property extends DeploymentTarget, StructuralFeature, ConnectableElement {

    private boolean isDerivedUnion;
    private String aggregation;
    private boolean isComposite;
    private boolean isDerived;





    private UML2_Property uml2_property;




    private UML2_Association uml2_association;




    private UML2_Property uml2_property;




    private UML2_Association uml2_association;




    private UML2_Association uml2_association;


    public UML2_Property(
        boolean isDerivedUnion,        String aggregation,        boolean isComposite,        boolean isDerived    ) {
        super(
        );
        this.isDerivedUnion = isDerivedUnion;
        this.aggregation = aggregation;
        this.isComposite = isComposite;
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

}