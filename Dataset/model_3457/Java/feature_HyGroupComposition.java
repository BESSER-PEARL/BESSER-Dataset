





import java.util.List;
import java.util.ArrayList;

public class feature_HyGroupComposition extends HyLinearTemporalElement {






    private List<feature_HyFeature> feature_hyfeatures;




    private feature_HyFeature feature_hyfeature;




    private feature_HyGroup feature_hygroup;




    private feature_HyGroup feature_hygroup;


    public feature_HyGroupComposition(
    ) {
        super(
        );
        this.feature_hyfeatures = new ArrayList<>();
    }

    public feature_HyGroupComposition(
        ArrayList<feature_HyFeature> feature_hyfeatures    ) {
        this.feature_hyfeatures = feature_hyfeatures;
    }


    public List<feature_HyFeature> getFeature_hyfeatures() {
        return feature_hyfeatures;
    }

    public void addFeature_hyfeature(Feature_hyfeature feature_hyfeature) {
        this.feature_hyfeatures.add(feature_hyfeature);
    }
    public feature_HyFeature getFeature_hyfeature() {
        return feature_hyfeature;
    }

    public void setFeature_hyfeature(feature_HyFeature feature_hyfeature) {
        this.feature_hyfeature = feature_hyfeature;
    }
    public feature_HyGroup getFeature_hygroup() {
        return feature_hygroup;
    }

    public void setFeature_hygroup(feature_HyGroup feature_hygroup) {
        this.feature_hygroup = feature_hygroup;
    }
    public feature_HyGroup getFeature_hygroup() {
        return feature_hygroup;
    }

    public void setFeature_hygroup(feature_HyGroup feature_hygroup) {
        this.feature_hygroup = feature_hygroup;
    }

}