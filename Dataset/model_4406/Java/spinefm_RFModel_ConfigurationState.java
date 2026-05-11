





import java.util.List;
import java.util.ArrayList;

public class spinefm_RFModel_ConfigurationState  {

    private String id;





    private List<Feature> features;




    private FeatureModel featuremodel;




    private List<Feature> features;


    public spinefm_RFModel_ConfigurationState(
        String id    ) {
        this.id = id;
        this.features = new ArrayList<>();
        this.features = new ArrayList<>();
    }

    public spinefm_RFModel_ConfigurationState(
        String id        ArrayList<Feature> features,        ArrayList<Feature> features    ) {
        this.id = id;
        this.features = features;
        this.features = features;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<Feature> getFeatures() {
        return features;
    }

    public void addFeature(Feature feature) {
        this.features.add(feature);
    }
    public FeatureModel getFeaturemodel() {
        return featuremodel;
    }

    public void setFeaturemodel(FeatureModel featuremodel) {
        this.featuremodel = featuremodel;
    }
    public List<Feature> getFeatures() {
        return features;
    }

    public void addFeature(Feature feature) {
        this.features.add(feature);
    }

}