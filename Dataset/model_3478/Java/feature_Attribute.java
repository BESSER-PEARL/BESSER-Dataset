





import java.util.List;
import java.util.ArrayList;

public class feature_Attribute  {

    private String name;
    private String value;





    private feature_Domain feature_domain;




    private feature_Feature feature_feature;




    private feature_Feature feature_feature;


    public feature_Attribute(
        String name,        String value    ) {
        this.name = name;
        this.value = value;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public feature_Domain getFeature_domain() {
        return feature_domain;
    }

    public void setFeature_domain(feature_Domain feature_domain) {
        this.feature_domain = feature_domain;
    }
    public feature_Feature getFeature_feature() {
        return feature_feature;
    }

    public void setFeature_feature(feature_Feature feature_feature) {
        this.feature_feature = feature_feature;
    }
    public feature_Feature getFeature_feature() {
        return feature_feature;
    }

    public void setFeature_feature(feature_Feature feature_feature) {
        this.feature_feature = feature_feature;
    }

}