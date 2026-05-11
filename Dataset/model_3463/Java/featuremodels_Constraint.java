





import java.util.List;
import java.util.ArrayList;

public class featuremodels_Constraint  {

    private String rule;
    private String name;
    private String type;





    private featuremodels_FeatureModel featuremodels_featuremodel;


    public featuremodels_Constraint(
        String rule,        String name,        String type    ) {
        this.rule = rule;
        this.name = name;
        this.type = type;
    }


    public String getRule() {
        return rule;
    }

    public void setRule(String rule) {
        this.rule = rule;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public featuremodels_FeatureModel getFeaturemodels_featuremodel() {
        return featuremodels_featuremodel;
    }

    public void setFeaturemodels_featuremodel(featuremodels_FeatureModel featuremodels_featuremodel) {
        this.featuremodels_featuremodel = featuremodels_featuremodel;
    }

}