





import java.util.List;
import java.util.ArrayList;

public class UML2_Property extends StructuralFeature, ConnectableElement, DeploymentTarget {

    private boolean isComposite;
    private String aggregation;
    private boolean isDerivedUnion;
    private boolean isDerived;





    private UML2_QualifierValue uml2_qualifiervalue;




    private UML2_LinkEndData uml2_linkenddata;




    private List<UML2_Property> uml2_propertys;




    private List<UML2_Property> uml2_propertys;


    public UML2_Property(
        boolean isComposite,        String aggregation,        boolean isDerivedUnion,        boolean isDerived    ) {
        super(
        );
        this.isComposite = isComposite;
        this.aggregation = aggregation;
        this.isDerivedUnion = isDerivedUnion;
        this.isDerived = isDerived;
        this.uml2_propertys = new ArrayList<>();
        this.uml2_propertys = new ArrayList<>();
    }

    public UML2_Property(
        boolean isComposite,        String aggregation,        boolean isDerivedUnion,        boolean isDerived        ArrayList<UML2_Property> uml2_propertys,        ArrayList<UML2_Property> uml2_propertys    ) {
        this.isComposite = isComposite;
        this.aggregation = aggregation;
        this.isDerivedUnion = isDerivedUnion;
        this.isDerived = isDerived;
        this.uml2_propertys = uml2_propertys;
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

    public UML2_QualifierValue getUml2_qualifiervalue() {
        return uml2_qualifiervalue;
    }

    public void setUml2_qualifiervalue(UML2_QualifierValue uml2_qualifiervalue) {
        this.uml2_qualifiervalue = uml2_qualifiervalue;
    }
    public UML2_LinkEndData getUml2_linkenddata() {
        return uml2_linkenddata;
    }

    public void setUml2_linkenddata(UML2_LinkEndData uml2_linkenddata) {
        this.uml2_linkenddata = uml2_linkenddata;
    }
    public List<UML2_Property> getUml2_propertys() {
        return uml2_propertys;
    }

    public void addUml2_property(Uml2_property uml2_property) {
        this.uml2_propertys.add(uml2_property);
    }
    public List<UML2_Property> getUml2_propertys() {
        return uml2_propertys;
    }

    public void addUml2_property(Uml2_property uml2_property) {
        this.uml2_propertys.add(uml2_property);
    }

}