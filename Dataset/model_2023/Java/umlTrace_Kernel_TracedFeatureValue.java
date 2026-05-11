





import java.util.List;
import java.util.ArrayList;

public class umlTrace_Kernel_TracedFeatureValue  {






    private List<FeatureValue_feature_Value> featurevalue_feature_values;




    private List<FeatureValue_values_FeatureValue_Value> featurevalue_values_featurevalue_values;




    private List<FeatureValue_position_Value> featurevalue_position_values;


    public umlTrace_Kernel_TracedFeatureValue(
    ) {
        this.featurevalue_feature_values = new ArrayList<>();
        this.featurevalue_values_featurevalue_values = new ArrayList<>();
        this.featurevalue_position_values = new ArrayList<>();
    }

    public umlTrace_Kernel_TracedFeatureValue(
        ArrayList<FeatureValue_feature_Value> featurevalue_feature_values,        ArrayList<FeatureValue_values_FeatureValue_Value> featurevalue_values_featurevalue_values,        ArrayList<FeatureValue_position_Value> featurevalue_position_values    ) {
        this.featurevalue_feature_values = featurevalue_feature_values;
        this.featurevalue_values_featurevalue_values = featurevalue_values_featurevalue_values;
        this.featurevalue_position_values = featurevalue_position_values;
    }


    public List<FeatureValue_feature_Value> getFeaturevalue_feature_values() {
        return featurevalue_feature_values;
    }

    public void addFeaturevalue_feature_value(Featurevalue_feature_value featurevalue_feature_value) {
        this.featurevalue_feature_values.add(featurevalue_feature_value);
    }
    public List<FeatureValue_values_FeatureValue_Value> getFeaturevalue_values_featurevalue_values() {
        return featurevalue_values_featurevalue_values;
    }

    public void addFeaturevalue_values_featurevalue_value(Featurevalue_values_featurevalue_value featurevalue_values_featurevalue_value) {
        this.featurevalue_values_featurevalue_values.add(featurevalue_values_featurevalue_value);
    }
    public List<FeatureValue_position_Value> getFeaturevalue_position_values() {
        return featurevalue_position_values;
    }

    public void addFeaturevalue_position_value(Featurevalue_position_value featurevalue_position_value) {
        this.featurevalue_position_values.add(featurevalue_position_value);
    }

}