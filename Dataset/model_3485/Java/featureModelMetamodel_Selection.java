





import java.util.List;
import java.util.ArrayList;

public class featureModelMetamodel_Selection  {

    private String state;
    private String name;





    private featureModelMetamodel_Feature featuremodelmetamodel_feature;


    public featureModelMetamodel_Selection(
        String state,        String name    ) {
        this.state = state;
        this.name = name;
    }


    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
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

}