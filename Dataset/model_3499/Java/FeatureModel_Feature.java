





import java.util.List;
import java.util.ArrayList;

public class FeatureModel_Feature  {

    private int id;
    private String name;





    private FeatureModel_FeatureConstraint featuremodel_featureconstraint;




    private FeatureModel_ConfigConstraint featuremodel_configconstraint;




    private FeatureModel_ConfigConstraint featuremodel_configconstraint;


    public FeatureModel_Feature(
        int id,        String name    ) {
        this.id = id;
        this.name = name;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public FeatureModel_FeatureConstraint getFeaturemodel_featureconstraint() {
        return featuremodel_featureconstraint;
    }

    public void setFeaturemodel_featureconstraint(FeatureModel_FeatureConstraint featuremodel_featureconstraint) {
        this.featuremodel_featureconstraint = featuremodel_featureconstraint;
    }
    public FeatureModel_ConfigConstraint getFeaturemodel_configconstraint() {
        return featuremodel_configconstraint;
    }

    public void setFeaturemodel_configconstraint(FeatureModel_ConfigConstraint featuremodel_configconstraint) {
        this.featuremodel_configconstraint = featuremodel_configconstraint;
    }
    public FeatureModel_ConfigConstraint getFeaturemodel_configconstraint() {
        return featuremodel_configconstraint;
    }

    public void setFeaturemodel_configconstraint(FeatureModel_ConfigConstraint featuremodel_configconstraint) {
        this.featuremodel_configconstraint = featuremodel_configconstraint;
    }

}