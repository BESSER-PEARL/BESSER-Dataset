





import java.util.List;
import java.util.ArrayList;

public class frameweb_Property extends DeploymentTarget, ConnectableElement, StructuralFeature {

    private String isDerivedUnion;
    private String isDerived;
    private String default;
    private String isID;
    private String aggregation;
    private String isComposite;





    private frameweb_Property frameweb_property;




    private frameweb_Property frameweb_property;




    private List<frameweb_Property> frameweb_propertys;




    private List<frameweb_Property> frameweb_propertys;




    private frameweb_Property frameweb_property;


    public frameweb_Property(
        String isDerivedUnion,        String isDerived,        String default,        String isID,        String aggregation,        String isComposite    ) {
        super(
        );
        this.isDerivedUnion = isDerivedUnion;
        this.isDerived = isDerived;
        this.default = default;
        this.isID = isID;
        this.aggregation = aggregation;
        this.isComposite = isComposite;
        this.frameweb_propertys = new ArrayList<>();
        this.frameweb_propertys = new ArrayList<>();
    }

    public frameweb_Property(
        String isDerivedUnion,        String isDerived,        String default,        String isID,        String aggregation,        String isComposite        ArrayList<frameweb_Property> frameweb_propertys,        ArrayList<frameweb_Property> frameweb_propertys    ) {
        this.isDerivedUnion = isDerivedUnion;
        this.isDerived = isDerived;
        this.default = default;
        this.isID = isID;
        this.aggregation = aggregation;
        this.isComposite = isComposite;
        this.frameweb_propertys = frameweb_propertys;
        this.frameweb_propertys = frameweb_propertys;
    }

    public String getIsderivedunion() {
        return isDerivedUnion;
    }

    public void setIsderivedunion(String isDerivedUnion) {
        this.isDerivedUnion = isDerivedUnion;
    }
    public String getIsderived() {
        return isDerived;
    }

    public void setIsderived(String isDerived) {
        this.isDerived = isDerived;
    }
    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }
    public String getIsid() {
        return isID;
    }

    public void setIsid(String isID) {
        this.isID = isID;
    }
    public String getAggregation() {
        return aggregation;
    }

    public void setAggregation(String aggregation) {
        this.aggregation = aggregation;
    }
    public String getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(String isComposite) {
        this.isComposite = isComposite;
    }

    public frameweb_Property getFrameweb_property() {
        return frameweb_property;
    }

    public void setFrameweb_property(frameweb_Property frameweb_property) {
        this.frameweb_property = frameweb_property;
    }
    public frameweb_Property getFrameweb_property() {
        return frameweb_property;
    }

    public void setFrameweb_property(frameweb_Property frameweb_property) {
        this.frameweb_property = frameweb_property;
    }
    public List<frameweb_Property> getFrameweb_propertys() {
        return frameweb_propertys;
    }

    public void addFrameweb_property(Frameweb_property frameweb_property) {
        this.frameweb_propertys.add(frameweb_property);
    }
    public List<frameweb_Property> getFrameweb_propertys() {
        return frameweb_propertys;
    }

    public void addFrameweb_property(Frameweb_property frameweb_property) {
        this.frameweb_propertys.add(frameweb_property);
    }
    public frameweb_Property getFrameweb_property() {
        return frameweb_property;
    }

    public void setFrameweb_property(frameweb_Property frameweb_property) {
        this.frameweb_property = frameweb_property;
    }

}