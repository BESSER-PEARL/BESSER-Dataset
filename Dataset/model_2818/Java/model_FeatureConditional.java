





import java.util.List;
import java.util.ArrayList;

public class model_FeatureConditional  {

    private String operator;





    private model_Feature model_feature;


    public model_FeatureConditional(
        String operator    ) {
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public model_Feature getModel_feature() {
        return model_feature;
    }

    public void setModel_feature(model_Feature model_feature) {
        this.model_feature = model_feature;
    }

}