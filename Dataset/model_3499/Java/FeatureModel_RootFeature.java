





import java.util.List;
import java.util.ArrayList;

public class FeatureModel_RootFeature  {






    private List<FeatureModel_ConfigConstraint> featuremodel_configconstraints;




    private FeatureModel_FeatureModel featuremodel_featuremodel;


    public FeatureModel_RootFeature(
    ) {
        this.featuremodel_configconstraints = new ArrayList<>();
    }

    public FeatureModel_RootFeature(
        ArrayList<FeatureModel_ConfigConstraint> featuremodel_configconstraints    ) {
        this.featuremodel_configconstraints = featuremodel_configconstraints;
    }


    public List<FeatureModel_ConfigConstraint> getFeaturemodel_configconstraints() {
        return featuremodel_configconstraints;
    }

    public void addFeaturemodel_configconstraint(Featuremodel_configconstraint featuremodel_configconstraint) {
        this.featuremodel_configconstraints.add(featuremodel_configconstraint);
    }
    public FeatureModel_FeatureModel getFeaturemodel_featuremodel() {
        return featuremodel_featuremodel;
    }

    public void setFeaturemodel_featuremodel(FeatureModel_FeatureModel featuremodel_featuremodel) {
        this.featuremodel_featuremodel = featuremodel_featuremodel;
    }

}