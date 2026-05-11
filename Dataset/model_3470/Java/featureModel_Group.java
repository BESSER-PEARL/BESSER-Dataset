





import java.util.List;
import java.util.ArrayList;

public class featureModel_Group  {

    private boolean inclusive;





    private List<featureModel_GroupedFeature> featuremodel_groupedfeatures;




    private featureModel_Feature featuremodel_feature;


    public featureModel_Group(
        boolean inclusive    ) {
        this.inclusive = inclusive;
        this.featuremodel_groupedfeatures = new ArrayList<>();
    }

    public featureModel_Group(
        boolean inclusive        ArrayList<featureModel_GroupedFeature> featuremodel_groupedfeatures    ) {
        this.inclusive = inclusive;
        this.featuremodel_groupedfeatures = featuremodel_groupedfeatures;
    }

    public boolean getInclusive() {
        return inclusive;
    }

    public void setInclusive(boolean inclusive) {
        this.inclusive = inclusive;
    }

    public List<featureModel_GroupedFeature> getFeaturemodel_groupedfeatures() {
        return featuremodel_groupedfeatures;
    }

    public void addFeaturemodel_groupedfeature(Featuremodel_groupedfeature featuremodel_groupedfeature) {
        this.featuremodel_groupedfeatures.add(featuremodel_groupedfeature);
    }
    public featureModel_Feature getFeaturemodel_feature() {
        return featuremodel_feature;
    }

    public void setFeaturemodel_feature(featureModel_Feature featuremodel_feature) {
        this.featuremodel_feature = featuremodel_feature;
    }

}