





import java.util.List;
import java.util.ArrayList;

public class featureModel_Condition  {

    private String type;





    private featureModel_AdaptationRule featuremodel_adaptationrule;




    private featureModel_Attribute featuremodel_attribute;




    private featureModel_Feature featuremodel_feature;


    public featureModel_Condition(
        String type    ) {
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public featureModel_AdaptationRule getFeaturemodel_adaptationrule() {
        return featuremodel_adaptationrule;
    }

    public void setFeaturemodel_adaptationrule(featureModel_AdaptationRule featuremodel_adaptationrule) {
        this.featuremodel_adaptationrule = featuremodel_adaptationrule;
    }
    public featureModel_Attribute getFeaturemodel_attribute() {
        return featuremodel_attribute;
    }

    public void setFeaturemodel_attribute(featureModel_Attribute featuremodel_attribute) {
        this.featuremodel_attribute = featuremodel_attribute;
    }
    public featureModel_Feature getFeaturemodel_feature() {
        return featuremodel_feature;
    }

    public void setFeaturemodel_feature(featureModel_Feature featuremodel_feature) {
        this.featuremodel_feature = featuremodel_feature;
    }

}