





import java.util.List;
import java.util.ArrayList;

public class featuremodel_Group  {

    private int upper;
    private String id;
    private int lower;





    private List<featuremodel_Feature> featuremodel_features;




    private featuremodel_Feature featuremodel_feature;


    public featuremodel_Group(
        int upper,        String id,        int lower    ) {
        this.upper = upper;
        this.id = id;
        this.lower = lower;
        this.featuremodel_features = new ArrayList<>();
    }

    public featuremodel_Group(
        int upper,        String id,        int lower        ArrayList<featuremodel_Feature> featuremodel_features    ) {
        this.upper = upper;
        this.id = id;
        this.lower = lower;
        this.featuremodel_features = featuremodel_features;
    }

    public int getUpper() {
        return upper;
    }

    public void setUpper(int upper) {
        this.upper = upper;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public int getLower() {
        return lower;
    }

    public void setLower(int lower) {
        this.lower = lower;
    }

    public List<featuremodel_Feature> getFeaturemodel_features() {
        return featuremodel_features;
    }

    public void addFeaturemodel_feature(Featuremodel_feature featuremodel_feature) {
        this.featuremodel_features.add(featuremodel_feature);
    }
    public featuremodel_Feature getFeaturemodel_feature() {
        return featuremodel_feature;
    }

    public void setFeaturemodel_feature(featuremodel_Feature featuremodel_feature) {
        this.featuremodel_feature = featuremodel_feature;
    }

}