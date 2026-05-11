





import java.util.List;
import java.util.ArrayList;

public class FeatureModel_Feature extends NamedElement {

    private boolean mandatory;
    private boolean abstract;





    private List<FeatureModel_Feature> featuremodel_features;




    private FeatureModel_FeatureModel featuremodel_featuremodel;


    public FeatureModel_Feature(
        boolean mandatory,        boolean abstract    ) {
        super(
        );
        this.mandatory = mandatory;
        this.abstract = abstract;
        this.featuremodel_features = new ArrayList<>();
    }

    public FeatureModel_Feature(
        boolean mandatory,        boolean abstract        ArrayList<FeatureModel_Feature> featuremodel_features    ) {
        this.mandatory = mandatory;
        this.abstract = abstract;
        this.featuremodel_features = featuremodel_features;
    }

    public boolean getMandatory() {
        return mandatory;
    }

    public void setMandatory(boolean mandatory) {
        this.mandatory = mandatory;
    }
    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }

    public List<FeatureModel_Feature> getFeaturemodel_features() {
        return featuremodel_features;
    }

    public void addFeaturemodel_feature(Featuremodel_feature featuremodel_feature) {
        this.featuremodel_features.add(featuremodel_feature);
    }
    public FeatureModel_FeatureModel getFeaturemodel_featuremodel() {
        return featuremodel_featuremodel;
    }

    public void setFeaturemodel_featuremodel(FeatureModel_FeatureModel featuremodel_featuremodel) {
        this.featuremodel_featuremodel = featuremodel_featuremodel;
    }

}