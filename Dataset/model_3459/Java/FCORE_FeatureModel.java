





import java.util.List;
import java.util.ArrayList;

public class FCORE_FeatureModel  {






    private List<FCORE_MandatoryConnection> fcore_mandatoryconnections;




    private List<FCORE_GroupToFeatureConnection> fcore_grouptofeatureconnections;




    private List<FCORE_OptionalConnection> fcore_optionalconnections;




    private List<FCORE_FeatureToGroupConnection> fcore_featuretogroupconnections;




    private List<FCORE_AttributeConstraintConnection> fcore_attributeconstraintconnections;


    public FCORE_FeatureModel(
    ) {
        this.fcore_mandatoryconnections = new ArrayList<>();
        this.fcore_grouptofeatureconnections = new ArrayList<>();
        this.fcore_optionalconnections = new ArrayList<>();
        this.fcore_featuretogroupconnections = new ArrayList<>();
        this.fcore_attributeconstraintconnections = new ArrayList<>();
    }

    public FCORE_FeatureModel(
        ArrayList<FCORE_MandatoryConnection> fcore_mandatoryconnections,        ArrayList<FCORE_GroupToFeatureConnection> fcore_grouptofeatureconnections,        ArrayList<FCORE_OptionalConnection> fcore_optionalconnections,        ArrayList<FCORE_FeatureToGroupConnection> fcore_featuretogroupconnections,        ArrayList<FCORE_AttributeConstraintConnection> fcore_attributeconstraintconnections    ) {
        this.fcore_mandatoryconnections = fcore_mandatoryconnections;
        this.fcore_grouptofeatureconnections = fcore_grouptofeatureconnections;
        this.fcore_optionalconnections = fcore_optionalconnections;
        this.fcore_featuretogroupconnections = fcore_featuretogroupconnections;
        this.fcore_attributeconstraintconnections = fcore_attributeconstraintconnections;
    }


    public List<FCORE_MandatoryConnection> getFcore_mandatoryconnections() {
        return fcore_mandatoryconnections;
    }

    public void addFcore_mandatoryconnection(Fcore_mandatoryconnection fcore_mandatoryconnection) {
        this.fcore_mandatoryconnections.add(fcore_mandatoryconnection);
    }
    public List<FCORE_GroupToFeatureConnection> getFcore_grouptofeatureconnections() {
        return fcore_grouptofeatureconnections;
    }

    public void addFcore_grouptofeatureconnection(Fcore_grouptofeatureconnection fcore_grouptofeatureconnection) {
        this.fcore_grouptofeatureconnections.add(fcore_grouptofeatureconnection);
    }
    public List<FCORE_OptionalConnection> getFcore_optionalconnections() {
        return fcore_optionalconnections;
    }

    public void addFcore_optionalconnection(Fcore_optionalconnection fcore_optionalconnection) {
        this.fcore_optionalconnections.add(fcore_optionalconnection);
    }
    public List<FCORE_FeatureToGroupConnection> getFcore_featuretogroupconnections() {
        return fcore_featuretogroupconnections;
    }

    public void addFcore_featuretogroupconnection(Fcore_featuretogroupconnection fcore_featuretogroupconnection) {
        this.fcore_featuretogroupconnections.add(fcore_featuretogroupconnection);
    }
    public List<FCORE_AttributeConstraintConnection> getFcore_attributeconstraintconnections() {
        return fcore_attributeconstraintconnections;
    }

    public void addFcore_attributeconstraintconnection(Fcore_attributeconstraintconnection fcore_attributeconstraintconnection) {
        this.fcore_attributeconstraintconnections.add(fcore_attributeconstraintconnection);
    }

}