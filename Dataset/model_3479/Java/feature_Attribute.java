





import java.util.List;
import java.util.ArrayList;

public class feature_Attribute  {

    private String value;
    private String name;





    private feature_AttributeReference feature_attributereference;




    private feature_Feature feature_feature;




    private feature_Domain feature_domain;




    private feature_Feature feature_feature;


    public feature_Attribute(
        String value,        String name    ) {
        this.value = value;
        this.name = name;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public feature_AttributeReference getFeature_attributereference() {
        return feature_attributereference;
    }

    public void setFeature_attributereference(feature_AttributeReference feature_attributereference) {
        this.feature_attributereference = feature_attributereference;
    }
    public feature_Feature getFeature_feature() {
        return feature_feature;
    }

    public void setFeature_feature(feature_Feature feature_feature) {
        this.feature_feature = feature_feature;
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

}