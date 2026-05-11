





import java.util.List;
import java.util.ArrayList;

public class FeatureModel_Feature extends NamedElement {

    private boolean abstract;
    private boolean mandatory;





    private FeatureModel_Group featuremodel_group;




    private FeatureModel_RequireConstraint featuremodel_requireconstraint;




    private FeatureModel_FeatureModel featuremodel_featuremodel;




    private List<FeatureModel_Feature> featuremodel_features;




    private FeatureModel_Group featuremodel_group;




    private List<FeatureModel_RequireConstraint> featuremodel_requireconstraints;




    private List<FeatureModel_RequireConstraint> featuremodel_requireconstraints;




    private FeatureModel_RequireConstraint featuremodel_requireconstraint;


    public FeatureModel_Feature(
        boolean abstract,        boolean mandatory    ) {
        super(
        );
        this.abstract = abstract;
        this.mandatory = mandatory;
        this.featuremodel_features = new ArrayList<>();
        this.featuremodel_requireconstraints = new ArrayList<>();
        this.featuremodel_requireconstraints = new ArrayList<>();
    }

    public FeatureModel_Feature(
        boolean abstract,        boolean mandatory        ArrayList<FeatureModel_Feature> featuremodel_features,        ArrayList<FeatureModel_RequireConstraint> featuremodel_requireconstraints,        ArrayList<FeatureModel_RequireConstraint> featuremodel_requireconstraints    ) {
        this.abstract = abstract;
        this.mandatory = mandatory;
        this.featuremodel_features = featuremodel_features;
        this.featuremodel_requireconstraints = featuremodel_requireconstraints;
        this.featuremodel_requireconstraints = featuremodel_requireconstraints;
    }

    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }
    public boolean getMandatory() {
        return mandatory;
    }

    public void setMandatory(boolean mandatory) {
        this.mandatory = mandatory;
    }

    public FeatureModel_Group getFeaturemodel_group() {
        return featuremodel_group;
    }

    public void setFeaturemodel_group(FeatureModel_Group featuremodel_group) {
        this.featuremodel_group = featuremodel_group;
    }
    public FeatureModel_RequireConstraint getFeaturemodel_requireconstraint() {
        return featuremodel_requireconstraint;
    }

    public void setFeaturemodel_requireconstraint(FeatureModel_RequireConstraint featuremodel_requireconstraint) {
        this.featuremodel_requireconstraint = featuremodel_requireconstraint;
    }
    public FeatureModel_FeatureModel getFeaturemodel_featuremodel() {
        return featuremodel_featuremodel;
    }

    public void setFeaturemodel_featuremodel(FeatureModel_FeatureModel featuremodel_featuremodel) {
        this.featuremodel_featuremodel = featuremodel_featuremodel;
    }
    public List<FeatureModel_Feature> getFeaturemodel_features() {
        return featuremodel_features;
    }

    public void addFeaturemodel_feature(Featuremodel_feature featuremodel_feature) {
        this.featuremodel_features.add(featuremodel_feature);
    }
    public FeatureModel_Group getFeaturemodel_group() {
        return featuremodel_group;
    }

    public void setFeaturemodel_group(FeatureModel_Group featuremodel_group) {
        this.featuremodel_group = featuremodel_group;
    }
    public List<FeatureModel_RequireConstraint> getFeaturemodel_requireconstraints() {
        return featuremodel_requireconstraints;
    }

    public void addFeaturemodel_requireconstraint(Featuremodel_requireconstraint featuremodel_requireconstraint) {
        this.featuremodel_requireconstraints.add(featuremodel_requireconstraint);
    }
    public List<FeatureModel_RequireConstraint> getFeaturemodel_requireconstraints() {
        return featuremodel_requireconstraints;
    }

    public void addFeaturemodel_requireconstraint(Featuremodel_requireconstraint featuremodel_requireconstraint) {
        this.featuremodel_requireconstraints.add(featuremodel_requireconstraint);
    }
    public FeatureModel_RequireConstraint getFeaturemodel_requireconstraint() {
        return featuremodel_requireconstraint;
    }

    public void setFeaturemodel_requireconstraint(FeatureModel_RequireConstraint featuremodel_requireconstraint) {
        this.featuremodel_requireconstraint = featuremodel_requireconstraint;
    }

}