





import java.util.List;
import java.util.ArrayList;

public class feature_Constraint extends Identifiable {






    private feature_FeatureModel feature_featuremodel;




    private feature_Expression feature_expression;


    public feature_Constraint(
    ) {
        super(
        );
    }



    public feature_FeatureModel getFeature_featuremodel() {
        return feature_featuremodel;
    }

    public void setFeature_featuremodel(feature_FeatureModel feature_featuremodel) {
        this.feature_featuremodel = feature_featuremodel;
    }
    public feature_Expression getFeature_expression() {
        return feature_expression;
    }

    public void setFeature_expression(feature_Expression feature_expression) {
        this.feature_expression = feature_expression;
    }

}