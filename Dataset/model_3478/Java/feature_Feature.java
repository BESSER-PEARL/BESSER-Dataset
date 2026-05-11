





import java.util.List;
import java.util.ArrayList;

public class feature_Feature extends Identifiable {

    private String selected;
    private String name;





    private feature_FeatureModel feature_featuremodel;


    public feature_Feature(
        String selected,        String name    ) {
        super(
        );
        this.selected = selected;
        this.name = name;
    }


    public String getSelected() {
        return selected;
    }

    public void setSelected(String selected) {
        this.selected = selected;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public feature_FeatureModel getFeature_featuremodel() {
        return feature_featuremodel;
    }

    public void setFeature_featuremodel(feature_FeatureModel feature_featuremodel) {
        this.feature_featuremodel = feature_featuremodel;
    }

}