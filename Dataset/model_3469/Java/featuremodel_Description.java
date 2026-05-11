





import java.util.List;
import java.util.ArrayList;

public class featuremodel_Description  {

    private String id;
    private String text;





    private featuremodel_FeatureModel featuremodel_featuremodel;


    public featuremodel_Description(
        String id,        String text    ) {
        this.id = id;
        this.text = text;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public featuremodel_FeatureModel getFeaturemodel_featuremodel() {
        return featuremodel_featuremodel;
    }

    public void setFeaturemodel_featuremodel(featuremodel_FeatureModel featuremodel_featuremodel) {
        this.featuremodel_featuremodel = featuremodel_featuremodel;
    }

}