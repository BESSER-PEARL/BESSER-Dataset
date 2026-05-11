





import java.util.List;
import java.util.ArrayList;

public class EFM_Alternative extends Feature {






    private List<EFM_Feature> efm_features;


    public EFM_Alternative(
    ) {
        super(
        );
        this.efm_features = new ArrayList<>();
    }

    public EFM_Alternative(
        ArrayList<EFM_Feature> efm_features    ) {
        this.efm_features = efm_features;
    }


    public List<EFM_Feature> getEfm_features() {
        return efm_features;
    }

    public void addEfm_feature(Efm_feature efm_feature) {
        this.efm_features.add(efm_feature);
    }

}