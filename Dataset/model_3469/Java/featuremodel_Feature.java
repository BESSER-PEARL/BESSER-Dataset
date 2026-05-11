





import java.util.List;
import java.util.ArrayList;

public class featuremodel_Feature  {

    private String id;
    private String name;
    private String type;





    private featuremodel_FeatureModel featuremodel_featuremodel;




    private featuremodel_Description featuremodel_description;




    private List<featuremodel_Attribute> featuremodel_attributes;


    public featuremodel_Feature(
        String id,        String name,        String type    ) {
        this.id = id;
        this.name = name;
        this.type = type;
        this.featuremodel_attributes = new ArrayList<>();
    }

    public featuremodel_Feature(
        String id,        String name,        String type        ArrayList<featuremodel_Attribute> featuremodel_attributes    ) {
        this.id = id;
        this.name = name;
        this.type = type;
        this.featuremodel_attributes = featuremodel_attributes;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
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

    public featuremodel_FeatureModel getFeaturemodel_featuremodel() {
        return featuremodel_featuremodel;
    }

    public void setFeaturemodel_featuremodel(featuremodel_FeatureModel featuremodel_featuremodel) {
        this.featuremodel_featuremodel = featuremodel_featuremodel;
    }
    public featuremodel_Description getFeaturemodel_description() {
        return featuremodel_description;
    }

    public void setFeaturemodel_description(featuremodel_Description featuremodel_description) {
        this.featuremodel_description = featuremodel_description;
    }
    public List<featuremodel_Attribute> getFeaturemodel_attributes() {
        return featuremodel_attributes;
    }

    public void addFeaturemodel_attribute(Featuremodel_attribute featuremodel_attribute) {
        this.featuremodel_attributes.add(featuremodel_attribute);
    }

}