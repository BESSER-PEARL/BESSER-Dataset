





import java.util.List;
import java.util.ArrayList;

public class featuremodels_Constraint  {

    private String rule;
    private String type;
    private String name;





    private featuremodels_FeatureModel featuremodels_featuremodel;


    public featuremodels_Constraint(
        String rule,        String type,        String name    ) {
        this.rule = rule;
        this.type = type;
        this.name = name;
    }


    public String getRule() {
        return rule;
    }

    public void setRule(String rule) {
        this.rule = rule;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public featuremodels_FeatureModel getFeaturemodels_featuremodel() {
        return featuremodels_featuremodel;
    }

    public void setFeaturemodels_featuremodel(featuremodels_FeatureModel featuremodels_featuremodel) {
        this.featuremodels_featuremodel = featuremodels_featuremodel;
    }

}