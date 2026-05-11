





import java.util.List;
import java.util.ArrayList;

public class cmof_Property extends StructuralFeature {

    private String default;
    private String aggregation;
    private String isID;
    private String isDerived;
    private String isDerivedUnion;
    private String isComposite;





    private cmof_Property cmof_property;




    private List<cmof_Property> cmof_propertys;




    private cmof_Property cmof_property;


    public cmof_Property(
        String default,        String aggregation,        String isID,        String isDerived,        String isDerivedUnion,        String isComposite    ) {
        super(
        );
        this.default = default;
        this.aggregation = aggregation;
        this.isID = isID;
        this.isDerived = isDerived;
        this.isDerivedUnion = isDerivedUnion;
        this.isComposite = isComposite;
        this.cmof_propertys = new ArrayList<>();
    }

    public cmof_Property(
        String default,        String aggregation,        String isID,        String isDerived,        String isDerivedUnion,        String isComposite        ArrayList<cmof_Property> cmof_propertys    ) {
        this.default = default;
        this.aggregation = aggregation;
        this.isID = isID;
        this.isDerived = isDerived;
        this.isDerivedUnion = isDerivedUnion;
        this.isComposite = isComposite;
        this.cmof_propertys = cmof_propertys;
    }

    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
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
    public String getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(String isComposite) {
        this.isComposite = isComposite;
    }

    public cmof_Property getCmof_property() {
        return cmof_property;
    }

    public void setCmof_property(cmof_Property cmof_property) {
        this.cmof_property = cmof_property;
    }
    public List<cmof_Property> getCmof_propertys() {
        return cmof_propertys;
    }

    public void addCmof_property(Cmof_property cmof_property) {
        this.cmof_propertys.add(cmof_property);
    }
    public cmof_Property getCmof_property() {
        return cmof_property;
    }

    public void setCmof_property(cmof_Property cmof_property) {
        this.cmof_property = cmof_property;
    }

}