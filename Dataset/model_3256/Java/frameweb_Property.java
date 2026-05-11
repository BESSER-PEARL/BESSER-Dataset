





import java.util.List;
import java.util.ArrayList;

public class frameweb_Property extends DeploymentTarget, ConnectableElement, StructuralFeature {

    private String isDerived;
    private String isDerivedUnion;
    private String default;
    private String isComposite;
    private String aggregation;
    private String isID;





    private frameweb_Property frameweb_property;




    private List<frameweb_Property> frameweb_propertys;




    private frameweb_Property frameweb_property;




    private frameweb_Property frameweb_property;




    private frameweb_Property frameweb_property;


    public frameweb_Property(
        String isDerived,        String isDerivedUnion,        String default,        String isComposite,        String aggregation,        String isID    ) {
        super(
        );
        this.isDerived = isDerived;
        this.isDerivedUnion = isDerivedUnion;
        this.default = default;
        this.isComposite = isComposite;
        this.aggregation = aggregation;
        this.isID = isID;
        this.frameweb_propertys = new ArrayList<>();
    }

    public frameweb_Property(
        String isDerived,        String isDerivedUnion,        String default,        String isComposite,        String aggregation,        String isID        ArrayList<frameweb_Property> frameweb_propertys    ) {
        this.isDerived = isDerived;
        this.isDerivedUnion = isDerivedUnion;
        this.default = default;
        this.isComposite = isComposite;
        this.aggregation = aggregation;
        this.isID = isID;
        this.frameweb_propertys = frameweb_propertys;
    }

    public String getIsderived() {
        return isDerived;
    }

    public void setIsderived(String isDerived) {
        this.isDerived = isDerived;
    }
    public String getIsderivedunion() {
        return isDerivedUnion;
    }

    public void setIsderivedunion(String isDerivedUnion) {
        this.isDerivedUnion = isDerivedUnion;
    }
    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }
    public String getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(String isComposite) {
        this.isComposite = isComposite;
    }
    public String getAggregation() {
        return aggregation;
    }

    public void setAggregation(String aggregation) {
        this.aggregation = aggregation;
    }
    public String getIsid() {
        return isID;
    }

    public void setIsid(String isID) {
        this.isID = isID;
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
    public frameweb_Property getFrameweb_property() {
        return frameweb_property;
    }

    public void setFrameweb_property(frameweb_Property frameweb_property) {
        this.frameweb_property = frameweb_property;
    }

}