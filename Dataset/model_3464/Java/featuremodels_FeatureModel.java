





import java.util.List;
import java.util.ArrayList;

public class featuremodels_FeatureModel  {

    private String name;





    private featuremodels_Feature featuremodels_feature;


    public featuremodels_FeatureModel(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public featuremodels_Feature getFeaturemodels_feature() {
        return featuremodels_feature;
    }

    public void setFeaturemodels_feature(featuremodels_Feature featuremodels_feature) {
        this.featuremodels_feature = featuremodels_feature;
    }

}