





import java.util.List;
import java.util.ArrayList;

public class feature_Feature extends Identifiable {

    private String name;
    private String selected;





    private feature_FeatureModel feature_featuremodel;




    private feature_FeatureReference feature_featurereference;


    public feature_Feature(
        String name,        String selected    ) {
        super(
        );
        this.name = name;
        this.selected = selected;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSelected() {
        return selected;
    }

    public void setSelected(String selected) {
        this.selected = selected;
    }

    public feature_FeatureModel getFeature_featuremodel() {
        return feature_featuremodel;
    }

    public void setFeature_featuremodel(feature_FeatureModel feature_featuremodel) {
        this.feature_featuremodel = feature_featuremodel;
    }
    public feature_FeatureReference getFeature_featurereference() {
        return feature_featurereference;
    }

    public void setFeature_featurereference(feature_FeatureReference feature_featurereference) {
        this.feature_featurereference = feature_featurereference;
    }

}