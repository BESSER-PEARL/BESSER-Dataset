





import java.util.List;
import java.util.ArrayList;

public class feature_Feature extends HybridElement, UUIDElement {

    private String transitiveEliminationState;





    private feature_FeatureDependency feature_featuredependency;




    private feature_FeatureModel feature_featuremodel;




    private List<feature_FeatureDependency> feature_featuredependencys;




    private feature_RootRelationship feature_rootrelationship;




    private List<feature_Feature> feature_features;




    private feature_FeatureDependency feature_featuredependency;




    private List<feature_FeatureDependency> feature_featuredependencys;




    private feature_FeatureModel feature_featuremodel;




    private List<feature_RootRelationship> feature_rootrelationships;


    public feature_Feature(
        String transitiveEliminationState    ) {
        super(
        );
        this.transitiveEliminationState = transitiveEliminationState;
        this.feature_featuredependencys = new ArrayList<>();
        this.feature_features = new ArrayList<>();
        this.feature_featuredependencys = new ArrayList<>();
        this.feature_rootrelationships = new ArrayList<>();
    }

    public feature_Feature(
        String transitiveEliminationState        ArrayList<feature_FeatureDependency> feature_featuredependencys,        ArrayList<feature_Feature> feature_features,        ArrayList<feature_FeatureDependency> feature_featuredependencys,        ArrayList<feature_RootRelationship> feature_rootrelationships    ) {
        this.transitiveEliminationState = transitiveEliminationState;
        this.feature_featuredependencys = feature_featuredependencys;
        this.feature_features = feature_features;
        this.feature_featuredependencys = feature_featuredependencys;
        this.feature_rootrelationships = feature_rootrelationships;
    }

    public String getTransitiveeliminationstate() {
        return transitiveEliminationState;
    }

    public void setTransitiveeliminationstate(String transitiveEliminationState) {
        this.transitiveEliminationState = transitiveEliminationState;
    }

    public feature_FeatureDependency getFeature_featuredependency() {
        return feature_featuredependency;
    }

    public void setFeature_featuredependency(feature_FeatureDependency feature_featuredependency) {
        this.feature_featuredependency = feature_featuredependency;
    }
    public feature_FeatureModel getFeature_featuremodel() {
        return feature_featuremodel;
    }

    public void setFeature_featuremodel(feature_FeatureModel feature_featuremodel) {
        this.feature_featuremodel = feature_featuremodel;
    }
    public List<feature_FeatureDependency> getFeature_featuredependencys() {
        return feature_featuredependencys;
    }

    public void addFeature_featuredependency(Feature_featuredependency feature_featuredependency) {
        this.feature_featuredependencys.add(feature_featuredependency);
    }
    public feature_RootRelationship getFeature_rootrelationship() {
        return feature_rootrelationship;
    }

    public void setFeature_rootrelationship(feature_RootRelationship feature_rootrelationship) {
        this.feature_rootrelationship = feature_rootrelationship;
    }
    public List<feature_Feature> getFeature_features() {
        return feature_features;
    }

    public void addFeature_feature(Feature_feature feature_feature) {
        this.feature_features.add(feature_feature);
    }
    public feature_FeatureDependency getFeature_featuredependency() {
        return feature_featuredependency;
    }

    public void setFeature_featuredependency(feature_FeatureDependency feature_featuredependency) {
        this.feature_featuredependency = feature_featuredependency;
    }
    public List<feature_FeatureDependency> getFeature_featuredependencys() {
        return feature_featuredependencys;
    }

    public void addFeature_featuredependency(Feature_featuredependency feature_featuredependency) {
        this.feature_featuredependencys.add(feature_featuredependency);
    }
    public feature_FeatureModel getFeature_featuremodel() {
        return feature_featuremodel;
    }

    public void setFeature_featuremodel(feature_FeatureModel feature_featuremodel) {
        this.feature_featuremodel = feature_featuremodel;
    }
    public List<feature_RootRelationship> getFeature_rootrelationships() {
        return feature_rootrelationships;
    }

    public void addFeature_rootrelationship(Feature_rootrelationship feature_rootrelationship) {
        this.feature_rootrelationships.add(feature_rootrelationship);
    }

}