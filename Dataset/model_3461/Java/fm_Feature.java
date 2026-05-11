





import java.util.List;
import java.util.ArrayList;

public class fm_Feature  {

    private String name;





    private List<fm_Feature> fm_features;




    private fm_FeatureModel fm_featuremodel;


    public fm_Feature(
        String name    ) {
        this.name = name;
        this.fm_features = new ArrayList<>();
    }

    public fm_Feature(
        String name        ArrayList<fm_Feature> fm_features    ) {
        this.name = name;
        this.fm_features = fm_features;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<fm_Feature> getFm_features() {
        return fm_features;
    }

    public void addFm_feature(Fm_feature fm_feature) {
        this.fm_features.add(fm_feature);
    }
    public fm_FeatureModel getFm_featuremodel() {
        return fm_featuremodel;
    }

    public void setFm_featuremodel(fm_FeatureModel fm_featuremodel) {
        this.fm_featuremodel = fm_featuremodel;
    }

}