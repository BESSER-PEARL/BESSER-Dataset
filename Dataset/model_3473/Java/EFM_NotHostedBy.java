





import java.util.List;
import java.util.ArrayList;

public class EFM_NotHostedBy extends FMConstraint {






    private EFM_NodeFeature efm_nodefeature;




    private List<EFM_Feature> efm_features;




    private EFM_NodeFeature efm_nodefeature;


    public EFM_NotHostedBy(
    ) {
        super(
        );
        this.efm_features = new ArrayList<>();
    }

    public EFM_NotHostedBy(
        ArrayList<EFM_Feature> efm_features    ) {
        this.efm_features = efm_features;
    }


    public EFM_NodeFeature getEfm_nodefeature() {
        return efm_nodefeature;
    }

    public void setEfm_nodefeature(EFM_NodeFeature efm_nodefeature) {
        this.efm_nodefeature = efm_nodefeature;
    }
    public List<EFM_Feature> getEfm_features() {
        return efm_features;
    }

    public void addEfm_feature(Efm_feature efm_feature) {
        this.efm_features.add(efm_feature);
    }
    public EFM_NodeFeature getEfm_nodefeature() {
        return efm_nodefeature;
    }

    public void setEfm_nodefeature(EFM_NodeFeature efm_nodefeature) {
        this.efm_nodefeature = efm_nodefeature;
    }

}