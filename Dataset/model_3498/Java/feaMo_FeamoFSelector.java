





import java.util.List;
import java.util.ArrayList;

public class feaMo_FeamoFSelector  {






    private List<feaMo_Feature> feamo_features;


    public feaMo_FeamoFSelector(
    ) {
        this.feamo_features = new ArrayList<>();
    }

    public feaMo_FeamoFSelector(
        ArrayList<feaMo_Feature> feamo_features    ) {
        this.feamo_features = feamo_features;
    }


    public List<feaMo_Feature> getFeamo_features() {
        return feamo_features;
    }

    public void addFeamo_feature(Feamo_feature feamo_feature) {
        this.feamo_features.add(feamo_feature);
    }

}