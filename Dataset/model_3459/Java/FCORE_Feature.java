





import java.util.List;
import java.util.ArrayList;

public class FCORE_Feature  {

    private boolean selected;
    private String name;





    private FCORE_AttributeConstraintConnection fcore_attributeconstraintconnection;




    private List<FCORE_AttributeConstraintConnection> fcore_attributeconstraintconnections;




    private List<FCORE_FeatureToGroupConnection> fcore_featuretogroupconnections;




    private FCORE_FeatureToGroupConnection fcore_featuretogroupconnection;


    public FCORE_Feature(
        boolean selected,        String name    ) {
        this.selected = selected;
        this.name = name;
        this.fcore_attributeconstraintconnections = new ArrayList<>();
        this.fcore_featuretogroupconnections = new ArrayList<>();
    }

    public FCORE_Feature(
        boolean selected,        String name        ArrayList<FCORE_AttributeConstraintConnection> fcore_attributeconstraintconnections,        ArrayList<FCORE_FeatureToGroupConnection> fcore_featuretogroupconnections    ) {
        this.selected = selected;
        this.name = name;
        this.fcore_attributeconstraintconnections = fcore_attributeconstraintconnections;
        this.fcore_featuretogroupconnections = fcore_featuretogroupconnections;
    }

    public boolean getSelected() {
        return selected;
    }

    public void setSelected(boolean selected) {
        this.selected = selected;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public FCORE_AttributeConstraintConnection getFcore_attributeconstraintconnection() {
        return fcore_attributeconstraintconnection;
    }

    public void setFcore_attributeconstraintconnection(FCORE_AttributeConstraintConnection fcore_attributeconstraintconnection) {
        this.fcore_attributeconstraintconnection = fcore_attributeconstraintconnection;
    }
    public List<FCORE_AttributeConstraintConnection> getFcore_attributeconstraintconnections() {
        return fcore_attributeconstraintconnections;
    }

    public void addFcore_attributeconstraintconnection(Fcore_attributeconstraintconnection fcore_attributeconstraintconnection) {
        this.fcore_attributeconstraintconnections.add(fcore_attributeconstraintconnection);
    }
    public List<FCORE_FeatureToGroupConnection> getFcore_featuretogroupconnections() {
        return fcore_featuretogroupconnections;
    }

    public void addFcore_featuretogroupconnection(Fcore_featuretogroupconnection fcore_featuretogroupconnection) {
        this.fcore_featuretogroupconnections.add(fcore_featuretogroupconnection);
    }
    public FCORE_FeatureToGroupConnection getFcore_featuretogroupconnection() {
        return fcore_featuretogroupconnection;
    }

    public void setFcore_featuretogroupconnection(FCORE_FeatureToGroupConnection fcore_featuretogroupconnection) {
        this.fcore_featuretogroupconnection = fcore_featuretogroupconnection;
    }

}