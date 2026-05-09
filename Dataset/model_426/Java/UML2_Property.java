





import java.util.List;
import java.util.ArrayList;

public class UML2_Property extends DeploymentTarget, StructuralFeature, ConnectableElement {

    private boolean isComposite;
    private boolean isDerivedUnion;
    private boolean isDerived;
    private String aggregation;





    private List<UML2_Property> uml2_propertys;




    private UML2_Property uml2_property;




    private UML2_QualifierValue uml2_qualifiervalue;


    public UML2_Property(
        boolean isComposite,        boolean isDerivedUnion,        boolean isDerived,        String aggregation    ) {
        super(
        );
        this.isComposite = isComposite;
        this.isDerivedUnion = isDerivedUnion;
        this.isDerived = isDerived;
        this.aggregation = aggregation;
        this.uml2_propertys = new ArrayList<>();
    }

    public UML2_Property(
        boolean isComposite,        boolean isDerivedUnion,        boolean isDerived,        String aggregation        ArrayList<UML2_Property> uml2_propertys    ) {
        this.isComposite = isComposite;
        this.isDerivedUnion = isDerivedUnion;
        this.isDerived = isDerived;
        this.aggregation = aggregation;
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
    public UML2_QualifierValue getUml2_qualifiervalue() {
        return uml2_qualifiervalue;
    }

    public void setUml2_qualifiervalue(UML2_QualifierValue uml2_qualifiervalue) {
        this.uml2_qualifiervalue = uml2_qualifiervalue;
    }

}