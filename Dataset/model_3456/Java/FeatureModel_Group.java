





import java.util.List;
import java.util.ArrayList;

public class FeatureModel_Group extends NamedElement {

    private String groupType;





    private FeatureModel_FeatureModel featuremodel_featuremodel;




    private FeatureModel_Feature featuremodel_feature;




    private List<FeatureModel_Feature> featuremodel_features;


    public FeatureModel_Group(
        String groupType    ) {
        super(
        );
        this.groupType = groupType;
        this.featuremodel_features = new ArrayList<>();
    }

    public FeatureModel_Group(
        String groupType        ArrayList<FeatureModel_Feature> featuremodel_features    ) {
        this.groupType = groupType;
        this.featuremodel_features = featuremodel_features;
    }

    public String getGrouptype() {
        return groupType;
    }

    public void setGrouptype(String groupType) {
        this.groupType = groupType;
    }

    public FeatureModel_FeatureModel getFeaturemodel_featuremodel() {
        return featuremodel_featuremodel;
    }

    public void setFeaturemodel_featuremodel(FeatureModel_FeatureModel featuremodel_featuremodel) {
        this.featuremodel_featuremodel = featuremodel_featuremodel;
    }
    public FeatureModel_Feature getFeaturemodel_feature() {
        return featuremodel_feature;
    }

    public void setFeaturemodel_feature(FeatureModel_Feature featuremodel_feature) {
        this.featuremodel_feature = featuremodel_feature;
    }
    public List<FeatureModel_Feature> getFeaturemodel_features() {
        return featuremodel_features;
    }

    public void addFeaturemodel_feature(Featuremodel_feature featuremodel_feature) {
        this.featuremodel_features.add(featuremodel_feature);
    }

}