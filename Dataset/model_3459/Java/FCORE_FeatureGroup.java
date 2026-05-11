





import java.util.List;
import java.util.ArrayList;

public class FCORE_FeatureGroup  {

    private int max;
    private int min;





    private FCORE_GroupToFeatureConnection fcore_grouptofeatureconnection;




    private FCORE_FeatureModel fcore_featuremodel;




    private FCORE_FeatureToGroupConnection fcore_featuretogroupconnection;




    private FCORE_FeatureToGroupConnection fcore_featuretogroupconnection;




    private List<FCORE_GroupToFeatureConnection> fcore_grouptofeatureconnections;


    public FCORE_FeatureGroup(
        int max,        int min    ) {
        this.max = max;
        this.min = min;
        this.fcore_grouptofeatureconnections = new ArrayList<>();
    }

    public FCORE_FeatureGroup(
        int max,        int min        ArrayList<FCORE_GroupToFeatureConnection> fcore_grouptofeatureconnections    ) {
        this.max = max;
        this.min = min;
        this.fcore_grouptofeatureconnections = fcore_grouptofeatureconnections;
    }

    public int getMax() {
        return max;
    }

    public void setMax(int max) {
        this.max = max;
    }
    public int getMin() {
        return min;
    }

    public void setMin(int min) {
        this.min = min;
    }

    public FCORE_GroupToFeatureConnection getFcore_grouptofeatureconnection() {
        return fcore_grouptofeatureconnection;
    }

    public void setFcore_grouptofeatureconnection(FCORE_GroupToFeatureConnection fcore_grouptofeatureconnection) {
        this.fcore_grouptofeatureconnection = fcore_grouptofeatureconnection;
    }
    public FCORE_FeatureModel getFcore_featuremodel() {
        return fcore_featuremodel;
    }

    public void setFcore_featuremodel(FCORE_FeatureModel fcore_featuremodel) {
        this.fcore_featuremodel = fcore_featuremodel;
    }
    public FCORE_FeatureToGroupConnection getFcore_featuretogroupconnection() {
        return fcore_featuretogroupconnection;
    }

    public void setFcore_featuretogroupconnection(FCORE_FeatureToGroupConnection fcore_featuretogroupconnection) {
        this.fcore_featuretogroupconnection = fcore_featuretogroupconnection;
    }
    public FCORE_FeatureToGroupConnection getFcore_featuretogroupconnection() {
        return fcore_featuretogroupconnection;
    }

    public void setFcore_featuretogroupconnection(FCORE_FeatureToGroupConnection fcore_featuretogroupconnection) {
        this.fcore_featuretogroupconnection = fcore_featuretogroupconnection;
    }
    public List<FCORE_GroupToFeatureConnection> getFcore_grouptofeatureconnections() {
        return fcore_grouptofeatureconnections;
    }

    public void addFcore_grouptofeatureconnection(Fcore_grouptofeatureconnection fcore_grouptofeatureconnection) {
        this.fcore_grouptofeatureconnections.add(fcore_grouptofeatureconnection);
    }

}