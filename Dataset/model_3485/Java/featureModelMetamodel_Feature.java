





import java.util.List;
import java.util.ArrayList;

public class featureModelMetamodel_Feature  {

    private String variabilityType;
    private String id;
    private String name;





    private featureModelMetamodel_Feature featuremodelmetamodel_feature;




    private featureModelMetamodel_FeatureModel featuremodelmetamodel_featuremodel;




    private featureModelMetamodel_FeatureModel featuremodelmetamodel_featuremodel;




    private List<featureModelMetamodel_Feature> featuremodelmetamodel_features;


    public featureModelMetamodel_Feature(
        String variabilityType,        String id,        String name    ) {
        this.variabilityType = variabilityType;
        this.id = id;
        this.name = name;
        this.featuremodelmetamodel_features = new ArrayList<>();
    }

    public featureModelMetamodel_Feature(
        String variabilityType,        String id,        String name        ArrayList<featureModelMetamodel_Feature> featuremodelmetamodel_features    ) {
        this.variabilityType = variabilityType;
        this.id = id;
        this.name = name;
        this.featuremodelmetamodel_features = featuremodelmetamodel_features;
    }

    public String getVariabilitytype() {
        return variabilityType;
    }

    public void setVariabilitytype(String variabilityType) {
        this.variabilityType = variabilityType;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public featureModelMetamodel_Feature getFeaturemodelmetamodel_feature() {
        return featuremodelmetamodel_feature;
    }

    public void setFeaturemodelmetamodel_feature(featureModelMetamodel_Feature featuremodelmetamodel_feature) {
        this.featuremodelmetamodel_feature = featuremodelmetamodel_feature;
    }
    public featureModelMetamodel_FeatureModel getFeaturemodelmetamodel_featuremodel() {
        return featuremodelmetamodel_featuremodel;
    }

    public void setFeaturemodelmetamodel_featuremodel(featureModelMetamodel_FeatureModel featuremodelmetamodel_featuremodel) {
        this.featuremodelmetamodel_featuremodel = featuremodelmetamodel_featuremodel;
    }
    public featureModelMetamodel_FeatureModel getFeaturemodelmetamodel_featuremodel() {
        return featuremodelmetamodel_featuremodel;
    }

    public void setFeaturemodelmetamodel_featuremodel(featureModelMetamodel_FeatureModel featuremodelmetamodel_featuremodel) {
        this.featuremodelmetamodel_featuremodel = featuremodelmetamodel_featuremodel;
    }
    public List<featureModelMetamodel_Feature> getFeaturemodelmetamodel_features() {
        return featuremodelmetamodel_features;
    }

    public void addFeaturemodelmetamodel_feature(Featuremodelmetamodel_feature featuremodelmetamodel_feature) {
        this.featuremodelmetamodel_features.add(featuremodelmetamodel_feature);
    }

}