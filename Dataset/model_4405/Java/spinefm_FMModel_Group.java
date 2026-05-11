





import java.util.List;
import java.util.ArrayList;

public class spinefm_FMModel_Group  {

    private String state;





    private List<Feature> features;


    public spinefm_FMModel_Group(
        String state    ) {
        this.state = state;
        this.features = new ArrayList<>();
    }

    public spinefm_FMModel_Group(
        String state        ArrayList<Feature> features    ) {
        this.state = state;
        this.features = features;
    }

    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }

    public List<Feature> getFeatures() {
        return features;
    }

    public void addFeature(Feature feature) {
        this.features.add(feature);
    }

}