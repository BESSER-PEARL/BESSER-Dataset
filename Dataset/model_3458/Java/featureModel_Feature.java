





import java.util.List;
import java.util.ArrayList;

public class featureModel_Feature extends VariabilityElement {

    private boolean mandatory;
    private String name;
    private boolean unselected;
    private boolean selected;





    private featureModel_FeatureModel featuremodel_featuremodel;




    private featureModel_Feature featuremodel_feature;


    public featureModel_Feature(
        boolean mandatory,        String name,        boolean unselected,        boolean selected    ) {
        super(
        );
        this.mandatory = mandatory;
        this.name = name;
        this.unselected = unselected;
        this.selected = selected;
    }


    public boolean getMandatory() {
        return mandatory;
    }

    public void setMandatory(boolean mandatory) {
        this.mandatory = mandatory;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getUnselected() {
        return unselected;
    }

    public void setUnselected(boolean unselected) {
        this.unselected = unselected;
    }
    public boolean getSelected() {
        return selected;
    }

    public void setSelected(boolean selected) {
        this.selected = selected;
    }

    public featureModel_FeatureModel getFeaturemodel_featuremodel() {
        return featuremodel_featuremodel;
    }

    public void setFeaturemodel_featuremodel(featureModel_FeatureModel featuremodel_featuremodel) {
        this.featuremodel_featuremodel = featuremodel_featuremodel;
    }
    public featureModel_Feature getFeaturemodel_feature() {
        return featuremodel_feature;
    }

    public void setFeaturemodel_feature(featureModel_Feature featuremodel_feature) {
        this.featuremodel_feature = featuremodel_feature;
    }

}