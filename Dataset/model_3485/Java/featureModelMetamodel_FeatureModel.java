





import java.util.List;
import java.util.ArrayList;

public class featureModelMetamodel_FeatureModel  {






    private List<featureModelMetamodel_Constraint> featuremodelmetamodel_constraints;


    public featureModelMetamodel_FeatureModel(
    ) {
        this.featuremodelmetamodel_constraints = new ArrayList<>();
    }

    public featureModelMetamodel_FeatureModel(
        ArrayList<featureModelMetamodel_Constraint> featuremodelmetamodel_constraints    ) {
        this.featuremodelmetamodel_constraints = featuremodelmetamodel_constraints;
    }


    public List<featureModelMetamodel_Constraint> getFeaturemodelmetamodel_constraints() {
        return featuremodelmetamodel_constraints;
    }

    public void addFeaturemodelmetamodel_constraint(Featuremodelmetamodel_constraint featuremodelmetamodel_constraint) {
        this.featuremodelmetamodel_constraints.add(featuremodelmetamodel_constraint);
    }

}