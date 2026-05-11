





import java.util.List;
import java.util.ArrayList;

public class featureModelMetamodel_GroupMultiplicity extends Multiplicity_ {






    private featureModelMetamodel_Feature featuremodelmetamodel_feature;




    private List<featureModelMetamodel_Feature> featuremodelmetamodel_features;


    public featureModelMetamodel_GroupMultiplicity(
    ) {
        super(
        );
        this.featuremodelmetamodel_features = new ArrayList<>();
    }

    public featureModelMetamodel_GroupMultiplicity(
        ArrayList<featureModelMetamodel_Feature> featuremodelmetamodel_features    ) {
        this.featuremodelmetamodel_features = featuremodelmetamodel_features;
    }


    public featureModelMetamodel_Feature getFeaturemodelmetamodel_feature() {
        return featuremodelmetamodel_feature;
    }

    public void setFeaturemodelmetamodel_feature(featureModelMetamodel_Feature featuremodelmetamodel_feature) {
        this.featuremodelmetamodel_feature = featuremodelmetamodel_feature;
    }
    public List<featureModelMetamodel_Feature> getFeaturemodelmetamodel_features() {
        return featuremodelmetamodel_features;
    }

    public void addFeaturemodelmetamodel_feature(Featuremodelmetamodel_feature featuremodelmetamodel_feature) {
        this.featuremodelmetamodel_features.add(featuremodelmetamodel_feature);
    }

}