





import java.util.List;
import java.util.ArrayList;

public class feature_AttributeReference extends AttributeOperand {






    private feature_Attribute feature_attribute;




    private feature_Feature feature_feature;


    public feature_AttributeReference(
    ) {
        super(
        );
    }



    public feature_Attribute getFeature_attribute() {
        return feature_attribute;
    }

    public void setFeature_attribute(feature_Attribute feature_attribute) {
        this.feature_attribute = feature_attribute;
    }
    public feature_Feature getFeature_feature() {
        return feature_feature;
    }

    public void setFeature_feature(feature_Feature feature_feature) {
        this.feature_feature = feature_feature;
    }

}