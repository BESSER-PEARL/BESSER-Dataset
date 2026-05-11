





import java.util.List;
import java.util.ArrayList;

public class FeatureModel_Feature extends NamedElement {

    private boolean abstract;
    private boolean mandatory;





    private FeatureModel_Feature featuremodel_feature;




    private FeatureModel_FeatureModel featuremodel_featuremodel;


    public FeatureModel_Feature(
        boolean abstract,        boolean mandatory    ) {
        super(
        );
        this.abstract = abstract;
        this.mandatory = mandatory;
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

    public FeatureModel_Feature getFeaturemodel_feature() {
        return featuremodel_feature;
    }

    public void setFeaturemodel_feature(FeatureModel_Feature featuremodel_feature) {
        this.featuremodel_feature = featuremodel_feature;
    }
    public FeatureModel_FeatureModel getFeaturemodel_featuremodel() {
        return featuremodel_featuremodel;
    }

    public void setFeaturemodel_featuremodel(FeatureModel_FeatureModel featuremodel_featuremodel) {
        this.featuremodel_featuremodel = featuremodel_featuremodel;
    }

}