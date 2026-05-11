





import java.util.List;
import java.util.ArrayList;

public class FeatureModel_FeatureModel  {






    private List<FeatureModel_FeatureConstraint> featuremodel_featureconstraints;


    public FeatureModel_FeatureModel(
    ) {
        this.featuremodel_featureconstraints = new ArrayList<>();
    }

    public FeatureModel_FeatureModel(
        ArrayList<FeatureModel_FeatureConstraint> featuremodel_featureconstraints    ) {
        this.featuremodel_featureconstraints = featuremodel_featureconstraints;
    }


    public List<FeatureModel_FeatureConstraint> getFeaturemodel_featureconstraints() {
        return featuremodel_featureconstraints;
    }

    public void addFeaturemodel_featureconstraint(Featuremodel_featureconstraint featuremodel_featureconstraint) {
        this.featuremodel_featureconstraints.add(featuremodel_featureconstraint);
    }

}