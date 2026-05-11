





import java.util.List;
import java.util.ArrayList;

public class featuremodel_Attribute  {

    private boolean setable;
    private String name;
    private String id;





    private featuremodel_Description featuremodel_description;




    private featuremodel_FeatureModel featuremodel_featuremodel;


    public featuremodel_Attribute(
        boolean setable,        String name,        String id    ) {
        this.setable = setable;
        this.name = name;
        this.id = id;
    }


    public boolean getSetable() {
        return setable;
    }

    public void setSetable(boolean setable) {
        this.setable = setable;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public featuremodel_Description getFeaturemodel_description() {
        return featuremodel_description;
    }

    public void setFeaturemodel_description(featuremodel_Description featuremodel_description) {
        this.featuremodel_description = featuremodel_description;
    }
    public featuremodel_FeatureModel getFeaturemodel_featuremodel() {
        return featuremodel_featuremodel;
    }

    public void setFeaturemodel_featuremodel(featuremodel_FeatureModel featuremodel_featuremodel) {
        this.featuremodel_featuremodel = featuremodel_featuremodel;
    }

}