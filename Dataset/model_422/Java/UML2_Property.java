





import java.util.List;
import java.util.ArrayList;

public class UML2_Property extends ConnectableElement, DeploymentTarget, StructuralFeature {

    private boolean isDerived;
    private String aggregation;
    private boolean isComposite;
    private boolean isDerivedUnion;





    private UML2_Property uml2_property;




    private UML2_Property uml2_property;




    private UML2_LinkEndData uml2_linkenddata;


    public UML2_Property(
        boolean isDerived,        String aggregation,        boolean isComposite,        boolean isDerivedUnion    ) {
        super(
        );
        this.isDerived = isDerived;
        this.aggregation = aggregation;
        this.isComposite = isComposite;
        this.isDerivedUnion = isDerivedUnion;
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
    public UML2_LinkEndData getUml2_linkenddata() {
        return uml2_linkenddata;
    }

    public void setUml2_linkenddata(UML2_LinkEndData uml2_linkenddata) {
        this.uml2_linkenddata = uml2_linkenddata;
    }

}