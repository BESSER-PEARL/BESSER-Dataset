





import java.util.List;
import java.util.ArrayList;

public class featuretree_TreeFeature extends Feature {

    private boolean mandatory;





    private List<featuretree_TreeFeature> featuretree_treefeatures;




    private featuretree_FeatureTree featuretree_featuretree;


    public featuretree_TreeFeature(
        boolean mandatory    ) {
        super(
        );
        this.mandatory = mandatory;
        this.featuretree_treefeatures = new ArrayList<>();
    }

    public featuretree_TreeFeature(
        boolean mandatory        ArrayList<featuretree_TreeFeature> featuretree_treefeatures    ) {
        this.mandatory = mandatory;
        this.featuretree_treefeatures = featuretree_treefeatures;
    }

    public boolean getMandatory() {
        return mandatory;
    }

    public void setMandatory(boolean mandatory) {
        this.mandatory = mandatory;
    }

    public List<featuretree_TreeFeature> getFeaturetree_treefeatures() {
        return featuretree_treefeatures;
    }

    public void addFeaturetree_treefeature(Featuretree_treefeature featuretree_treefeature) {
        this.featuretree_treefeatures.add(featuretree_treefeature);
    }
    public featuretree_FeatureTree getFeaturetree_featuretree() {
        return featuretree_featuretree;
    }

    public void setFeaturetree_featuretree(featuretree_FeatureTree featuretree_featuretree) {
        this.featuretree_featuretree = featuretree_featuretree;
    }

}