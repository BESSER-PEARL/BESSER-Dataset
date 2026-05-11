





import java.util.List;
import java.util.ArrayList;

public class fm_OrFeature extends Feature {






    private List<fm_Feature> fm_features;


    public fm_OrFeature(
    ) {
        super(
        );
        this.fm_features = new ArrayList<>();
    }

    public fm_OrFeature(
        ArrayList<fm_Feature> fm_features    ) {
        this.fm_features = fm_features;
    }


    public List<fm_Feature> getFm_features() {
        return fm_features;
    }

    public void addFm_feature(Fm_feature fm_feature) {
        this.fm_features.add(fm_feature);
    }

}