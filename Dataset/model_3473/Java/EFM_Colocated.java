





import java.util.List;
import java.util.ArrayList;

public class EFM_Colocated extends FMConstraint {






    private List<EFM_Feature> efm_features;




    private EFM_Feature efm_feature;


    public EFM_Colocated(
    ) {
        super(
        );
        this.efm_features = new ArrayList<>();
    }

    public EFM_Colocated(
        ArrayList<EFM_Feature> efm_features    ) {
        this.efm_features = efm_features;
    }


    public List<EFM_Feature> getEfm_features() {
        return efm_features;
    }

    public void addEfm_feature(Efm_feature efm_feature) {
        this.efm_features.add(efm_feature);
    }
    public EFM_Feature getEfm_feature() {
        return efm_feature;
    }

    public void setEfm_feature(EFM_Feature efm_feature) {
        this.efm_feature = efm_feature;
    }

}