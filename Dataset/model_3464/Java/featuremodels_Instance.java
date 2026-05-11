





import java.util.List;
import java.util.ArrayList;

public class featuremodels_Instance  {

    private String id;
    private String descritpion;





    private featuremodels_FeatureModel featuremodels_featuremodel;




    private List<featuremodels_Feature> featuremodels_features;


    public featuremodels_Instance(
        String id,        String descritpion    ) {
        this.id = id;
        this.descritpion = descritpion;
        this.featuremodels_features = new ArrayList<>();
    }

    public featuremodels_Instance(
        String id,        String descritpion        ArrayList<featuremodels_Feature> featuremodels_features    ) {
        this.id = id;
        this.descritpion = descritpion;
        this.featuremodels_features = featuremodels_features;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getDescritpion() {
        return descritpion;
    }

    public void setDescritpion(String descritpion) {
        this.descritpion = descritpion;
    }

    public featuremodels_FeatureModel getFeaturemodels_featuremodel() {
        return featuremodels_featuremodel;
    }

    public void setFeaturemodels_featuremodel(featuremodels_FeatureModel featuremodels_featuremodel) {
        this.featuremodels_featuremodel = featuremodels_featuremodel;
    }
    public List<featuremodels_Feature> getFeaturemodels_features() {
        return featuremodels_features;
    }

    public void addFeaturemodels_feature(Featuremodels_feature featuremodels_feature) {
        this.featuremodels_features.add(featuremodels_feature);
    }

}