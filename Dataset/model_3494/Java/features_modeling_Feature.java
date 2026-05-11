





import java.util.List;
import java.util.ArrayList;

public class features_modeling_Feature  {

    private String ID;





    private features_modeling_Feature features_modeling_feature;


    public features_modeling_Feature(
        String ID    ) {
        this.ID = ID;
    }


    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }

    public features_modeling_Feature getFeatures_modeling_feature() {
        return features_modeling_feature;
    }

    public void setFeatures_modeling_feature(features_modeling_Feature features_modeling_feature) {
        this.features_modeling_feature = features_modeling_feature;
    }

}