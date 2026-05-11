





import java.util.List;
import java.util.ArrayList;

public class feature_Constraint  {

    private String expression;
    private String language;





    private feature_FeatureModel feature_featuremodel;


    public feature_Constraint(
        String expression,        String language    ) {
        this.expression = expression;
        this.language = language;
    }


    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }
    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }

    public feature_FeatureModel getFeature_featuremodel() {
        return feature_featuremodel;
    }

    public void setFeature_featuremodel(feature_FeatureModel feature_featuremodel) {
        this.feature_featuremodel = feature_featuremodel;
    }

}