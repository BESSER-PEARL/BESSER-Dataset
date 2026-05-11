





import java.util.List;
import java.util.ArrayList;

public class EFM_Feature extends FMElement {

    private String name;





    private EFM_FeatureModel efm_featuremodel;




    private List<EFM_Feature> efm_features;


    public EFM_Feature(
        String name    ) {
        super(
        );
        this.name = name;
        this.efm_features = new ArrayList<>();
    }

    public EFM_Feature(
        String name        ArrayList<EFM_Feature> efm_features    ) {
        this.name = name;
        this.efm_features = efm_features;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public EFM_FeatureModel getEfm_featuremodel() {
        return efm_featuremodel;
    }

    public void setEfm_featuremodel(EFM_FeatureModel efm_featuremodel) {
        this.efm_featuremodel = efm_featuremodel;
    }
    public List<EFM_Feature> getEfm_features() {
        return efm_features;
    }

    public void addEfm_feature(Efm_feature efm_feature) {
        this.efm_features.add(efm_feature);
    }

}